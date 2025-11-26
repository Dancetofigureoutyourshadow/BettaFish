"""
Unified OpenAI-compatible LLM client for the Report Engine, with retry support.
"""

import os
import sys
from typing import Any, Dict, Optional, Generator
from loguru import logger

from openai import OpenAI

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
utils_dir = os.path.join(project_root, "utils")
if utils_dir not in sys.path:
    sys.path.append(utils_dir)

try:
    from retry_helper import with_retry, LLM_RETRY_CONFIG
except ImportError:
    def with_retry(config=None):
        def decorator(func):
            return func
        return decorator

    LLM_RETRY_CONFIG = None


class LLMClient:
    """Minimal wrapper around the OpenAI-compatible chat completion API."""

    def __init__(self, api_key: str, model_name: str, base_url: Optional[str] = None):
        if not api_key:
            raise ValueError("Report Engine LLM API key is required.")
        if not model_name:
            raise ValueError("Report Engine model name is required.")

        self.api_key = api_key
        self.base_url = base_url
        self.model_name = model_name
        self.provider = model_name
        timeout_fallback = os.getenv("LLM_REQUEST_TIMEOUT") or os.getenv("REPORT_ENGINE_REQUEST_TIMEOUT") or "3000"
        try:
            self.timeout = float(timeout_fallback)
        except ValueError:
            self.timeout = 3000.0

        client_kwargs: Dict[str, Any] = {
            "api_key": api_key,
            "max_retries": 0,
        }
        if base_url:
            client_kwargs["base_url"] = base_url
        self.client = OpenAI(**client_kwargs)

    @with_retry(LLM_RETRY_CONFIG)
    def invoke(self, system_prompt: str, user_prompt: str, **kwargs) -> str:
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]

        allowed_keys = {"temperature", "top_p", "presence_penalty", "frequency_penalty", "stream"}
        extra_params = {key: value for key, value in kwargs.items() if key in allowed_keys and value is not None}

        timeout = kwargs.pop("timeout", self.timeout)

        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=messages,
            timeout=timeout,
            **extra_params,
        )

        if response.choices and response.choices[0].message:
            return self.validate_response(response.choices[0].message.content)
        return ""

    def stream_invoke(self, system_prompt: str, user_prompt: str, **kwargs) -> Generator[str, None, None]:
        """
        流式调用LLM，逐步返回响应内容
        
        Args:
            system_prompt: 系统提示词
            user_prompt: 用户提示词
            **kwargs: 额外参数（temperature, top_p等）
            
        Yields:
            响应文本块（str）
        """
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]

        allowed_keys = {"temperature", "top_p", "presence_penalty", "frequency_penalty"}
        extra_params = {key: value for key, value in kwargs.items() if key in allowed_keys and value is not None}
        # 强制使用流式
        extra_params["stream"] = True

        timeout = kwargs.pop("timeout", self.timeout)

        try:
            stream = self.client.chat.completions.create(
                model=self.model_name,
                messages=messages,
                timeout=timeout,
                **extra_params,
            )
            
            for chunk in stream:
                if chunk.choices and len(chunk.choices) > 0:
                    delta = chunk.choices[0].delta
                    if delta and delta.content:
                        yield delta.content
        except Exception as e:
            logger.error(f"流式请求失败: {str(e)}")
            raise e
    
    @with_retry(LLM_RETRY_CONFIG)
    def stream_invoke_to_string(self, system_prompt: str, user_prompt: str, **kwargs) -> str:
        """
        流式调用LLM并安全地拼接为完整字符串（避免UTF-8多字节字符截断）
        处理模型响应长度限制，通过循环请求直到获取完整输出
        
        Args:
            system_prompt: 系统提示词
            user_prompt: 用户提示词
            **kwargs: 额外参数（temperature, top_p等）
            
        Returns:
            完整的响应字符串
        """
        full_response = ""
        
        # 设置合理的最大迭代次数以防止无限循环
        max_iterations = 5
        iteration = 0
        
        # 检查是否是由于长度限制导致的截断
        is_truncated = True
        
        while iteration < max_iterations and is_truncated:
            # 构造当前轮次的提示词
            current_system_prompt = system_prompt
            # 如果不是第一轮，添加继续指令
            if iteration > 0:
                current_user_prompt = f"{user_prompt}\n\n请继续完成前面未完成的部分。前面的内容：...{full_response[-1000:]}"
            else:
                current_user_prompt = user_prompt
            
            try:
                # 以字节形式收集所有块
                byte_chunks = []
                for chunk in self.stream_invoke(current_system_prompt, current_user_prompt, **kwargs):
                    byte_chunks.append(chunk.encode('utf-8'))
                
                # 拼接所有字节，然后一次性解码
                if byte_chunks:
                    chunk_response = b''.join(byte_chunks).decode('utf-8', errors='replace')
                    full_response += chunk_response
                    
                    # 检查响应是否表明已完成
                    # 如果响应较短或者以完整的句子结尾，则认为已完成
                    # 同时检查是否可能因为长度限制被截断
                    if (len(chunk_response) < 100 or 
                        chunk_response.rstrip().endswith(('.', '。', '!', '！', '?', '？', '"', '”', "'", '’'))):
                        is_truncated = False
                    else:
                        # 可能是由于长度限制被截断，需要继续请求
                        is_truncated = True
                else:
                    # 没有更多内容了
                    is_truncated = False
                    
            except Exception as e:
                # 如果出现异常，记录日志并返回已获取的部分内容
                logger.warning(f"流式调用出现异常: {e}，返回已获取的部分内容")
                break
            
            iteration += 1
        
        return full_response

    @staticmethod
    def validate_response(response: Optional[str]) -> str:
        if response is None:
            return ""
        return response.strip()

    def get_model_info(self) -> Dict[str, Any]:
        return {
            "provider": self.provider,
            "model": self.model_name,
            "api_base": self.base_url or "default",
        }
