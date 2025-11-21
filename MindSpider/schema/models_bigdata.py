"""
股票财经平台大数据聚合主表ORM模型(基于SQLAlchemy 2.x, 对应MediaCrawler stock tables)

数据模型定义位置:
- MindSpider/DeepSentimentCrawling/MediaCrawler/database/models.py  # 主表结构来源文件
- 本模块(映射股票平台表,适配MySQL/PostgreSQL)
- MindSpider/schema/models_sa.py  # Base 定义来源

本模块以MindSpider\DeepSentimentCrawling\MediaCrawler\database\models.py为准
所有字段与 MediaCrawler/database/models.py 保持一致
"""

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, BigInteger, Text, ForeignKey

# 使用 models_sa 中的 Base,确保所有表在同一个 metadata 中,外键引用可以正常工作
from models_sa import Base

# ==================== 东方财富 ====================

class EastmoneyPost(Base):
    __tablename__ = "eastmoney_post"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    post_id: Mapped[int | None] = mapped_column(BigInteger, nullable=False, index=True, unique=True)
    post_url: Mapped[str | None] = mapped_column(Text, nullable=False)
    user_id: Mapped[str | None] = mapped_column(String(255), index=True, nullable=True)
    author_name: Mapped[str | None] = mapped_column(Text, nullable=True)
    avatar: Mapped[str | None] = mapped_column(Text, nullable=True)
    liked_count: Mapped[int | None] = mapped_column(Integer, nullable=True)
    add_ts: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
    last_modify_ts: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
    post_type: Mapped[str | None] = mapped_column(Text, nullable=True)
    title: Mapped[str | None] = mapped_column(Text, nullable=True)
    content: Mapped[str | None] = mapped_column(Text, nullable=True)
    create_time: Mapped[int | None] = mapped_column(BigInteger, index=True, nullable=True)
    read_count: Mapped[str | None] = mapped_column(Text, nullable=True)
    comment_count: Mapped[str | None] = mapped_column(Text, nullable=True)
    share_count: Mapped[str | None] = mapped_column(Text, nullable=True)
    stock_code: Mapped[str | None] = mapped_column(String(20), index=True, nullable=True)
    stock_name: Mapped[str | None] = mapped_column(Text, nullable=True)
    source_keyword: Mapped[str | None] = mapped_column(Text, default='', nullable=True)
    topic_id: Mapped[str | None] = mapped_column(String(64), ForeignKey("daily_topics.topic_id", ondelete="SET NULL"), nullable=True)
    crawling_task_id: Mapped[str | None] = mapped_column(String(64), ForeignKey("crawling_tasks.task_id", ondelete="SET NULL"), nullable=True)


class EastmoneyComment(Base):
    __tablename__ = "eastmoney_comment"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[str | None] = mapped_column(String(255), nullable=True)
    user_name: Mapped[str | None] = mapped_column(Text, nullable=True)
    avatar: Mapped[str | None] = mapped_column(Text, nullable=True)
    add_ts: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
    last_modify_ts: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
    comment_id: Mapped[int | None] = mapped_column(BigInteger, index=True, nullable=True)
    post_id: Mapped[int | None] = mapped_column(BigInteger, index=True, nullable=True)
    content: Mapped[str | None] = mapped_column(Text, nullable=True)
    create_time: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
    sub_comment_count: Mapped[str | None] = mapped_column(Text, nullable=True)
    parent_comment_id: Mapped[str | None] = mapped_column(String(255), nullable=True)
    like_count: Mapped[str | None] = mapped_column(Text, default='0', nullable=True)


class EastmoneyUserInfo(Base):
    __tablename__ = "eastmoney_user_info"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[str | None] = mapped_column(String(255), index=True, unique=True, nullable=True)
    user_name: Mapped[str | None] = mapped_column(Text, nullable=True)
    avatar: Mapped[str | None] = mapped_column(Text, nullable=True)
    add_ts: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
    last_modify_ts: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
    total_fans: Mapped[int | None] = mapped_column(Integer, nullable=True)
    total_follows: Mapped[int | None] = mapped_column(Integer, nullable=True)
    total_posts: Mapped[int | None] = mapped_column(Integer, nullable=True)
    is_verified: Mapped[int | None] = mapped_column(Integer, nullable=True)
    user_level: Mapped[int | None] = mapped_column(Integer, nullable=True)


# ==================== 雪球 ====================

class XueqiuPost(Base):
    __tablename__ = "xueqiu_post"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    post_id: Mapped[int | None] = mapped_column(BigInteger, index=True, unique=True, nullable=True)
    user_id: Mapped[str | None] = mapped_column(String(255), index=True, nullable=True)
    author_name: Mapped[str | None] = mapped_column(Text, nullable=True)
    avatar: Mapped[str | None] = mapped_column(Text, nullable=True)
    user_signature: Mapped[str | None] = mapped_column(Text, nullable=True)
    add_ts: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
    last_modify_ts: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
    post_type: Mapped[str | None] = mapped_column(Text, nullable=True)
    title: Mapped[str | None] = mapped_column(Text, nullable=True)
    content: Mapped[str | None] = mapped_column(Text, nullable=True)
    create_time: Mapped[int | None] = mapped_column(BigInteger, index=True, nullable=True)
    liked_count: Mapped[str | None] = mapped_column(Text, nullable=True)
    comment_count: Mapped[str | None] = mapped_column(Text, nullable=True)
    retweet_count: Mapped[str | None] = mapped_column(Text, nullable=True)
    read_count: Mapped[str | None] = mapped_column(Text, nullable=True)
    post_url: Mapped[str | None] = mapped_column(Text, nullable=True)
    stock_code: Mapped[str | None] = mapped_column(String(20), index=True, nullable=True)
    stock_name: Mapped[str | None] = mapped_column(Text, nullable=True)
    source_keyword: Mapped[str | None] = mapped_column(Text, default='', nullable=True)
    topic_id: Mapped[str | None] = mapped_column(String(64), ForeignKey("daily_topics.topic_id", ondelete="SET NULL"), nullable=True)
    crawling_task_id: Mapped[str | None] = mapped_column(String(64), ForeignKey("crawling_tasks.task_id", ondelete="SET NULL"), nullable=True)


class XueqiuComment(Base):
    __tablename__ = "xueqiu_comment"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[str | None] = mapped_column(String(255), nullable=True)
    user_name: Mapped[str | None] = mapped_column(Text, nullable=True)
    avatar: Mapped[str | None] = mapped_column(Text, nullable=True)
    add_ts: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
    last_modify_ts: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
    comment_id: Mapped[int | None] = mapped_column(BigInteger, index=True, nullable=True)
    post_id: Mapped[int | None] = mapped_column(BigInteger, index=True, nullable=True)
    content: Mapped[str | None] = mapped_column(Text, nullable=True)
    create_time: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
    sub_comment_count: Mapped[str | None] = mapped_column(Text, nullable=True)
    parent_comment_id: Mapped[str | None] = mapped_column(String(255), nullable=True)
    like_count: Mapped[str | None] = mapped_column(Text, default='0', nullable=True)


class XueqiuUserInfo(Base):
    __tablename__ = "xueqiu_user_info"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[str | None] = mapped_column(String(255), index=True, unique=True, nullable=True)
    user_name: Mapped[str | None] = mapped_column(Text, nullable=True)
    avatar: Mapped[str | None] = mapped_column(Text, nullable=True)
    add_ts: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
    last_modify_ts: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
    desc: Mapped[str | None] = mapped_column(Text, nullable=True)
    follows: Mapped[int | None] = mapped_column(Integer, nullable=True)
    fans: Mapped[int | None] = mapped_column(Integer, nullable=True)
    total_posts: Mapped[int | None] = mapped_column(Integer, nullable=True)
    is_verified: Mapped[int | None] = mapped_column(Integer, nullable=True)


# ==================== 同花顺 ====================

class TonghuashunPost(Base):
    __tablename__ = "tonghuashun_post"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    post_id: Mapped[str | None] = mapped_column(String(255), index=True, unique=True, nullable=True)
    user_id: Mapped[str | None] = mapped_column(String(255), index=True, nullable=True)
    author_name: Mapped[str | None] = mapped_column(Text, nullable=True)
    avatar: Mapped[str | None] = mapped_column(Text, nullable=True)
    add_ts: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
    last_modify_ts: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
    post_type: Mapped[str | None] = mapped_column(Text, nullable=True)
    title: Mapped[str | None] = mapped_column(Text, nullable=True)
    content: Mapped[str | None] = mapped_column(Text, nullable=True)
    create_time: Mapped[int | None] = mapped_column(BigInteger, index=True, nullable=True)
    liked_count: Mapped[str | None] = mapped_column(Text, nullable=True)
    comment_count: Mapped[str | None] = mapped_column(Text, nullable=True)
    share_count: Mapped[str | None] = mapped_column(Text, nullable=True)
    post_url: Mapped[str | None] = mapped_column(Text, nullable=True)
    stock_code: Mapped[str | None] = mapped_column(String(20), index=True, nullable=True)
    stock_name: Mapped[str | None] = mapped_column(Text, nullable=True)
    source_keyword: Mapped[str | None] = mapped_column(Text, default='', nullable=True)
    topic_id: Mapped[str | None] = mapped_column(String(64), ForeignKey("daily_topics.topic_id", ondelete="SET NULL"), nullable=True)
    crawling_task_id: Mapped[str | None] = mapped_column(String(64), ForeignKey("crawling_tasks.task_id", ondelete="SET NULL"), nullable=True)


class TonghuashunComment(Base):
    __tablename__ = "tonghuashun_comment"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[str | None] = mapped_column(String(255), nullable=True)
    user_name: Mapped[str | None] = mapped_column(Text, nullable=True)
    avatar: Mapped[str | None] = mapped_column(Text, nullable=True)
    add_ts: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
    last_modify_ts: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
    comment_id: Mapped[int | None] = mapped_column(BigInteger, index=True, nullable=True)
    post_id: Mapped[str | None] = mapped_column(String(255), index=True, nullable=True)
    content: Mapped[str | None] = mapped_column(Text, nullable=True)
    create_time: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
    sub_comment_count: Mapped[str | None] = mapped_column(Text, nullable=True)


# ==================== 新浪财经 ====================

class SinaFinancePost(Base):
    __tablename__ = "sina_finance_post"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    post_id: Mapped[int | None] = mapped_column(BigInteger, index=True, unique=True, nullable=True)
    user_id: Mapped[str | None] = mapped_column(String(255), index=True, nullable=True)
    author_name: Mapped[str | None] = mapped_column(Text, nullable=True)
    avatar: Mapped[str | None] = mapped_column(Text, nullable=True)
    add_ts: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
    last_modify_ts: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
    post_type: Mapped[str | None] = mapped_column(Text, nullable=True)
    title: Mapped[str | None] = mapped_column(Text, nullable=True)
    content: Mapped[str | None] = mapped_column(Text, nullable=True)
    publish_time: Mapped[str | None] = mapped_column(String(255), index=True, nullable=True)
    liked_count: Mapped[str | None] = mapped_column(Text, nullable=True)
    comment_count: Mapped[str | None] = mapped_column(Text, nullable=True)
    share_count: Mapped[str | None] = mapped_column(Text, nullable=True)
    post_url: Mapped[str | None] = mapped_column(Text, nullable=True)
    stock_code: Mapped[str | None] = mapped_column(String(20), index=True, nullable=True)
    stock_name: Mapped[str | None] = mapped_column(Text, nullable=True)
    source_keyword: Mapped[str | None] = mapped_column(Text, default='', nullable=True)
    topic_id: Mapped[str | None] = mapped_column(String(64), ForeignKey("daily_topics.topic_id", ondelete="SET NULL"), nullable=True)
    crawling_task_id: Mapped[str | None] = mapped_column(String(64), ForeignKey("crawling_tasks.task_id", ondelete="SET NULL"), nullable=True)


class SinaFinanceComment(Base):
    __tablename__ = "sina_finance_comment"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[str | None] = mapped_column(String(255), nullable=True)
    user_name: Mapped[str | None] = mapped_column(Text, nullable=True)
    avatar: Mapped[str | None] = mapped_column(Text, nullable=True)
    add_ts: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
    last_modify_ts: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
    comment_id: Mapped[int | None] = mapped_column(BigInteger, index=True, nullable=True)
    post_id: Mapped[int | None] = mapped_column(BigInteger, index=True, nullable=True)
    content: Mapped[str | None] = mapped_column(Text, nullable=True)
    publish_time: Mapped[str | None] = mapped_column(String(255), index=True, nullable=True)
    like_count: Mapped[str | None] = mapped_column(Text, nullable=True)
    sub_comment_count: Mapped[str | None] = mapped_column(Text, nullable=True)
    parent_comment_id: Mapped[str | None] = mapped_column(String(255), nullable=True)


class SinaFinanceUserInfo(Base):
    __tablename__ = "sina_finance_user_info"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[str | None] = mapped_column(String(255), index=True, unique=True, nullable=True)
    user_name: Mapped[str | None] = mapped_column(Text, nullable=True)
    avatar: Mapped[str | None] = mapped_column(Text, nullable=True)
    add_ts: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
    last_modify_ts: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
    desc: Mapped[str | None] = mapped_column(Text, nullable=True)
    follows: Mapped[int | None] = mapped_column(Integer, nullable=True)
    fans: Mapped[int | None] = mapped_column(Integer, nullable=True)


# ==================== 金融界 ====================

class JinrongjiePost(Base):
    __tablename__ = "jinrongjie_post"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    post_id: Mapped[str | None] = mapped_column(String(255), index=True, unique=True, nullable=True)
    user_id: Mapped[str | None] = mapped_column(String(255), index=True, nullable=True)
    author_name: Mapped[str | None] = mapped_column(Text, nullable=True)
    avatar: Mapped[str | None] = mapped_column(Text, nullable=True)
    add_ts: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
    last_modify_ts: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
    post_type: Mapped[str | None] = mapped_column(Text, nullable=True)
    title: Mapped[str | None] = mapped_column(Text, nullable=True)
    content: Mapped[str | None] = mapped_column(Text, nullable=True)
    publish_time: Mapped[str | None] = mapped_column(String(32), index=True, nullable=True)
    liked_count: Mapped[int | None] = mapped_column(Integer, default=0, nullable=True)
    comment_count: Mapped[int | None] = mapped_column(Integer, default=0, nullable=True)
    post_url: Mapped[str | None] = mapped_column(Text, nullable=True)
    stock_code: Mapped[str | None] = mapped_column(String(20), index=True, nullable=True)
    stock_name: Mapped[str | None] = mapped_column(Text, nullable=True)
    source_keyword: Mapped[str | None] = mapped_column(Text, default='', nullable=True)
    topic_id: Mapped[str | None] = mapped_column(String(64), ForeignKey("daily_topics.topic_id", ondelete="SET NULL"), nullable=True)
    crawling_task_id: Mapped[str | None] = mapped_column(String(64), ForeignKey("crawling_tasks.task_id", ondelete="SET NULL"), nullable=True)


class JinrongjieComment(Base):
    __tablename__ = "jinrongjie_comment"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[str | None] = mapped_column(String(255), nullable=True)
    user_name: Mapped[str | None] = mapped_column(Text, nullable=True)
    avatar: Mapped[str | None] = mapped_column(Text, nullable=True)
    add_ts: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
    last_modify_ts: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
    comment_id: Mapped[str | None] = mapped_column(String(255), index=True, nullable=True)
    post_id: Mapped[str | None] = mapped_column(String(255), index=True, nullable=True)
    content: Mapped[str | None] = mapped_column(Text, nullable=True)
    publish_time: Mapped[str | None] = mapped_column(String(32), index=True, nullable=True)
    sub_comment_count: Mapped[int | None] = mapped_column(Integer, default=0, nullable=True)
    parent_comment_id: Mapped[str | None] = mapped_column(String(255), nullable=True)
    like_count: Mapped[int | None] = mapped_column(Integer, default=0, nullable=True)


# ==================== 和讯 ====================

class HexunPost(Base):
    __tablename__ = "hexun_post"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    post_id: Mapped[str | None] = mapped_column(String(255), index=True, unique=True, nullable=True)
    title: Mapped[str | None] = mapped_column(Text, nullable=True)
    content: Mapped[str | None] = mapped_column(Text, nullable=True)
    post_url: Mapped[str | None] = mapped_column(Text, nullable=True)
    publish_time: Mapped[str | None] = mapped_column(String(32), index=True, nullable=True)
    author_name: Mapped[str | None] = mapped_column(Text, default='', nullable=True)
    user_id: Mapped[str | None] = mapped_column(String(255), index=True, nullable=True)
    avatar: Mapped[str | None] = mapped_column(Text, default='', nullable=True)
    liked_count: Mapped[int | None] = mapped_column(Integer, default=0, nullable=True)
    comment_count: Mapped[int | None] = mapped_column(Integer, default=0, nullable=True)
    stock_code: Mapped[str | None] = mapped_column(String(20), index=True, nullable=True)
    stock_name: Mapped[str | None] = mapped_column(Text, nullable=True)
    add_ts: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
    last_modify_ts: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
    source_keyword: Mapped[str | None] = mapped_column(Text, default='', nullable=True)
    topic_id: Mapped[str | None] = mapped_column(String(64), ForeignKey("daily_topics.topic_id", ondelete="SET NULL"), nullable=True)
    crawling_task_id: Mapped[str | None] = mapped_column(String(64), ForeignKey("crawling_tasks.task_id", ondelete="SET NULL"), nullable=True)


class HexunComment(Base):
    __tablename__ = "hexun_comment"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    comment_id: Mapped[str | None] = mapped_column(String(255), index=True, nullable=True)
    parent_comment_id: Mapped[str | None] = mapped_column(String(255), default='', nullable=True)
    content: Mapped[str | None] = mapped_column(Text, nullable=True)
    user_name: Mapped[str | None] = mapped_column(Text, default='', nullable=True)
    user_id: Mapped[str | None] = mapped_column(String(255), nullable=True)
    avatar: Mapped[str | None] = mapped_column(Text, default='', nullable=True)
    publish_time: Mapped[str | None] = mapped_column(String(32), index=True, nullable=True)
    sub_comment_count: Mapped[int | None] = mapped_column(Integer, default=0, nullable=True)
    post_id: Mapped[str | None] = mapped_column(String(255), index=True, nullable=True)
    post_url: Mapped[str | None] = mapped_column(Text, nullable=True)
    like_count: Mapped[int | None] = mapped_column(Integer, default=0, nullable=True)
    add_ts: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
    last_modify_ts: Mapped[int | None] = mapped_column(BigInteger, nullable=True)


# ==================== 股票基础信息 ====================

class StockInfo(Base):
    __tablename__ = "stock_info"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    stock_code: Mapped[str | None] = mapped_column(String(20), unique=True, index=True, nullable=True)
    stock_name: Mapped[str | None] = mapped_column(Text, nullable=True)
    stock_type: Mapped[str | None] = mapped_column(String(20), nullable=True)
    exchange: Mapped[str | None] = mapped_column(String(20), nullable=True)
    industry: Mapped[str | None] = mapped_column(Text, nullable=True)
    sector: Mapped[str | None] = mapped_column(Text, nullable=True)
    listing_date: Mapped[str | None] = mapped_column(String(32), nullable=True)
    market_cap: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
    total_shares: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
    add_ts: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
    last_modify_ts: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
