from sqlalchemy import create_engine, Column, Integer, Text, String, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# 东方财富股吧帖子表
class EastmoneyPost(Base):
    __tablename__ = 'eastmoney_post'
    id = Column(Integer, primary_key=True)
    post_id = Column(BigInteger, nullable=False, index=True, unique=True)
    post_url = Column(Text, nullable=False)
    user_id = Column(String(255), index=True)
    author_name = Column(Text)
    avatar = Column(Text)
    liked_count = Column(Integer)
    add_ts = Column(BigInteger)
    last_modify_ts = Column(BigInteger)
    post_type = Column(Text)
    title = Column(Text)
    content = Column(Text)
    create_time = Column(BigInteger, index=True)
    read_count = Column(Text)
    comment_count = Column(Text)
    share_count = Column(Text)
    stock_code = Column(String(20), index=True)  # 股票代码
    stock_name = Column(Text)  # 股票名称
    source_keyword = Column(Text, default='')

# 东方财富评论表
class EastmoneyComment(Base):
    __tablename__ = 'eastmoney_comment'
    id = Column(Integer, primary_key=True)
    user_id = Column(String(255))
    user_name = Column(Text)
    avatar = Column(Text)
    add_ts = Column(BigInteger)
    last_modify_ts = Column(BigInteger)
    comment_id = Column(BigInteger, index=True)
    post_id = Column(BigInteger, index=True)
    content = Column(Text)
    create_time = Column(BigInteger)
    sub_comment_count = Column(Text)
    parent_comment_id = Column(String(255))
    like_count = Column(Text, default='0')

# 东方财富用户信息表
class EastmoneyUserInfo(Base):
    __tablename__ = 'eastmoney_user_info'
    id = Column(Integer, primary_key=True)
    user_id = Column(String(255), index=True, unique=True)
    user_name = Column(Text)
    avatar = Column(Text)
    add_ts = Column(BigInteger)
    last_modify_ts = Column(BigInteger)
    total_fans = Column(Integer)
    total_follows = Column(Integer)
    total_posts = Column(Integer)
    is_verified = Column(Integer)  # 是否认证用户
    user_level = Column(Integer)  # 用户等级

# 雪球帖子表
class XueqiuPost(Base):
    __tablename__ = 'xueqiu_post'
    id = Column(Integer, primary_key=True)
    post_id = Column(BigInteger, index=True, unique=True)
    user_id = Column(String(255), index=True)
    author_name = Column(Text)
    avatar = Column(Text)
    user_signature = Column(Text)
    add_ts = Column(BigInteger)
    last_modify_ts = Column(BigInteger)
    post_type = Column(Text)  # 帖子类型：原创/转发
    title = Column(Text)
    content = Column(Text)
    create_time = Column(BigInteger, index=True)
    liked_count = Column(Text)
    comment_count = Column(Text)
    retweet_count = Column(Text)  # 转发数
    read_count = Column(Text)  # 阅读数
    post_url = Column(Text)
    stock_code = Column(String(20), index=True)  # 股票代码
    stock_name = Column(Text)  # 股票名称
    source_keyword = Column(Text, default='')

# 雪球评论表
class XueqiuComment(Base):
    __tablename__ = 'xueqiu_comment'
    id = Column(Integer, primary_key=True)
    user_id = Column(String(255))
    user_name = Column(Text)
    avatar = Column(Text)
    add_ts = Column(BigInteger)
    last_modify_ts = Column(BigInteger)
    comment_id = Column(BigInteger, index=True)
    post_id = Column(BigInteger, index=True)
    content = Column(Text)
    create_time = Column(BigInteger)
    sub_comment_count = Column(Text)
    parent_comment_id = Column(String(255))
    like_count = Column(Text, default='0')

# 雪球用户信息表
class XueqiuUserInfo(Base):
    __tablename__ = 'xueqiu_user_info'
    id = Column(Integer, primary_key=True)
    user_id = Column(String(255), index=True, unique=True)
    user_name = Column(Text)
    avatar = Column(Text)
    add_ts = Column(BigInteger)
    last_modify_ts = Column(BigInteger)
    desc = Column(Text)
    follows = Column(Integer)
    fans = Column(Integer)
    total_posts = Column(Integer)
    is_verified = Column(Integer)  # 是否认证

# 同花顺帖子表
class TonghuashunPost(Base):
    __tablename__ = 'tonghuashun_post'
    id = Column(Integer, primary_key=True)
    post_id = Column(String(255), index=True, unique=True)
    user_id = Column(String(255), index=True)
    author_name = Column(Text)
    avatar = Column(Text)
    add_ts = Column(BigInteger)
    last_modify_ts = Column(BigInteger)
    post_type = Column(Text)
    title = Column(Text)
    content = Column(Text)
    create_time = Column(BigInteger, index=True)
    liked_count = Column(Text)
    comment_count = Column(Text)
    share_count = Column(Text)
    post_url = Column(Text)
    stock_code = Column(String(20), index=True)  # 股票代码
    stock_name = Column(Text)  # 股票名称
    source_keyword = Column(Text, default='')

# 同花顺评论表
class TonghuashunComment(Base):
    __tablename__ = 'tonghuashun_comment'
    id = Column(Integer, primary_key=True)
    user_id = Column(String(255))
    user_name = Column(Text)
    avatar = Column(Text)
    add_ts = Column(BigInteger)
    last_modify_ts = Column(BigInteger)
    comment_id = Column(BigInteger, index=True)
    post_id = Column(String(255), index=True)
    content = Column(Text)
    create_time = Column(BigInteger)
    sub_comment_count = Column(Text)

# 新浪财经帖子表
class SinaFinancePost(Base):
    __tablename__ = 'sina_finance_post'
    id = Column(Integer, primary_key=True)
    post_id = Column(BigInteger, index=True, unique=True)
    user_id = Column(String(255), index=True)
    author_name = Column(Text)
    avatar = Column(Text)
    add_ts = Column(BigInteger)
    last_modify_ts = Column(BigInteger)
    post_type = Column(Text)
    title = Column(Text)
    content = Column(Text)
    publish_time = Column(String(255), index=True)
    liked_count = Column(Text)
    comment_count = Column(Text)
    share_count = Column(Text)
    post_url = Column(Text)
    stock_code = Column(String(20), index=True)  # 股票代码
    stock_name = Column(Text)  # 股票名称
    source_keyword = Column(Text, default='')

# 新浪财经评论表
class SinaFinanceComment(Base):
    __tablename__ = 'sina_finance_comment'
    id = Column(Integer, primary_key=True)
    user_id = Column(String(255))
    user_name = Column(Text)
    avatar = Column(Text)
    add_ts = Column(BigInteger)
    last_modify_ts = Column(BigInteger)
    comment_id = Column(BigInteger, index=True)
    post_id = Column(BigInteger, index=True)
    content = Column(Text)
    publish_time = Column(String(255), index=True)
    like_count = Column(Text)
    sub_comment_count = Column(Text)
    parent_comment_id = Column(String(255))

# 新浪财经用户信息表
class SinaFinanceUserInfo(Base):
    __tablename__ = 'sina_finance_user_info'
    id = Column(Integer, primary_key=True)
    user_id = Column(String(255), index=True, unique=True)
    user_name = Column(Text)
    avatar = Column(Text)
    add_ts = Column(BigInteger)
    last_modify_ts = Column(BigInteger)
    desc = Column(Text)
    follows = Column(Integer)
    fans = Column(Integer)

# 金融界帖子表
class JinrongjiePost(Base):
    __tablename__ = 'jinrongjie_post'
    id = Column(Integer, primary_key=True)
    post_id = Column(String(255), index=True, unique=True)
    user_id = Column(String(255), index=True)
    author_name = Column(Text)
    avatar = Column(Text)
    add_ts = Column(BigInteger)
    last_modify_ts = Column(BigInteger)
    post_type = Column(Text)
    title = Column(Text)
    content = Column(Text)
    publish_time = Column(String(32), index=True)
    liked_count = Column(Integer, default=0)
    comment_count = Column(Integer, default=0)
    post_url = Column(Text)
    stock_code = Column(String(20), index=True)  # 股票代码
    stock_name = Column(Text)  # 股票名称
    source_keyword = Column(Text, default='')

# 金融界评论表
class JinrongjieComment(Base):
    __tablename__ = 'jinrongjie_comment'
    id = Column(Integer, primary_key=True)
    user_id = Column(String(255))
    user_name = Column(Text)
    avatar = Column(Text)
    add_ts = Column(BigInteger)
    last_modify_ts = Column(BigInteger)
    comment_id = Column(String(255), index=True)
    post_id = Column(String(255), index=True)
    content = Column(Text)
    publish_time = Column(String(32), index=True)
    sub_comment_count = Column(Integer, default=0)
    parent_comment_id = Column(String(255))
    like_count = Column(Integer, default=0)

# 和讯帖子表
class HexunPost(Base):
    __tablename__ = 'hexun_post'
    id = Column(Integer, primary_key=True)
    post_id = Column(String(255), index=True, unique=True)
    title = Column(Text)
    content = Column(Text)
    post_url = Column(Text)
    publish_time = Column(String(32), index=True)
    author_name = Column(Text, default='')
    user_id = Column(String(255), index=True)
    avatar = Column(Text, default='')
    liked_count = Column(Integer, default=0)
    comment_count = Column(Integer, default=0)
    stock_code = Column(String(20), index=True)  # 股票代码
    stock_name = Column(Text)  # 股票名称
    add_ts = Column(BigInteger)
    last_modify_ts = Column(BigInteger)
    source_keyword = Column(Text, default='')

# 和讯评论表
class HexunComment(Base):
    __tablename__ = 'hexun_comment'
    id = Column(Integer, primary_key=True)
    comment_id = Column(String(255), index=True)
    parent_comment_id = Column(String(255), default='')
    content = Column(Text)
    user_name = Column(Text, default='')
    user_id = Column(String(255))
    avatar = Column(Text, default='')
    publish_time = Column(String(32), index=True)
    sub_comment_count = Column(Integer, default=0)
    post_id = Column(String(255), index=True)
    post_url = Column(Text)
    like_count = Column(Integer, default=0)
    add_ts = Column(BigInteger)
    last_modify_ts = Column(BigInteger)

# 股票基础信息表
class StockInfo(Base):
    __tablename__ = 'stock_info'
    id = Column(Integer, primary_key=True)
    stock_code = Column(String(20), unique=True, index=True)  # 股票代码
    stock_name = Column(Text)  # 股票名称
    stock_type = Column(String(20))  # 股票类型：A股/港股/美股
    exchange = Column(String(20))  # 交易所：上交所/深交所
    industry = Column(Text)  # 所属行业
    sector = Column(Text)  # 所属板块
    listing_date = Column(String(32))  # 上市日期
    market_cap = Column(BigInteger)  # 市值
    total_shares = Column(BigInteger)  # 总股本
    add_ts = Column(BigInteger)
    last_modify_ts = Column(BigInteger)

# 每日新闻表（保留用于热点新闻）
class DailyNews(Base):
    __tablename__ = 'daily_news'
    id = Column(Integer, primary_key=True)
    news_id = Column(String(128), index=True, unique=True)
    source_platform = Column(String(32))  # 新闻源平台
    title = Column(Text)
    url = Column(Text)
    description = Column(Text)
    crawl_date = Column(String(32), index=True)
    rank_position = Column(Integer)
    stock_code = Column(String(20), index=True)  # 相关股票代码
    stock_name = Column(Text)  # 相关股票名称
    add_ts = Column(BigInteger)
    last_modify_ts = Column(BigInteger)