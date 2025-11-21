-- ===============================
-- 股票财经平台数据库表结构
-- 数据源: 东方财富、雪球、同花顺、新浪财经、金融界、和讯
-- ===============================

-- ----------------------------
-- Table structure for eastmoney_post
-- 东方财富股吧帖子表
-- ----------------------------
DROP TABLE IF EXISTS `eastmoney_post`;
CREATE TABLE `eastmoney_post`
(
    `id`               int          NOT NULL AUTO_INCREMENT COMMENT '自增ID',
    `post_id`          bigint       NOT NULL COMMENT '帖子ID',
    `post_url`         text         NOT NULL COMMENT '帖子链接',
    `user_id`          varchar(255) DEFAULT NULL COMMENT '用户ID',
    `author_name`      text         DEFAULT NULL COMMENT '作者名称',
    `avatar`           text         DEFAULT NULL COMMENT '用户头像地址',
    `liked_count`      int          DEFAULT NULL COMMENT '点赞数',
    `add_ts`           bigint       DEFAULT NULL COMMENT '记录添加时间戳',
    `last_modify_ts`   bigint       DEFAULT NULL COMMENT '记录最后修改时间戳',
    `post_type`        text         DEFAULT NULL COMMENT '帖子类型',
    `title`            text         DEFAULT NULL COMMENT '帖子标题',
    `content`          text         DEFAULT NULL COMMENT '帖子内容',
    `create_time`      bigint       DEFAULT NULL COMMENT '发布时间戳',
    `read_count`       text         DEFAULT NULL COMMENT '阅读数',
    `comment_count`    text         DEFAULT NULL COMMENT '评论数',
    `share_count`      text         DEFAULT NULL COMMENT '分享数',
    `stock_code`       varchar(20)  DEFAULT NULL COMMENT '股票代码',
    `stock_name`       text         DEFAULT NULL COMMENT '股票名称',
    `source_keyword`   text         DEFAULT '' COMMENT '搜索来源关键字',
    PRIMARY KEY (`id`),
    UNIQUE KEY `idx_eastmoney_post_id` (`post_id`),
    KEY `idx_eastmoney_user_id` (`user_id`),
    KEY `idx_eastmoney_create_time` (`create_time`),
    KEY `idx_eastmoney_stock_code` (`stock_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='东方财富股吧帖子';

-- ----------------------------
-- Table structure for eastmoney_comment
-- 东方财富评论表
-- ----------------------------
DROP TABLE IF EXISTS `eastmoney_comment`;
CREATE TABLE `eastmoney_comment`
(
    `id`                int          NOT NULL AUTO_INCREMENT COMMENT '自增ID',
    `user_id`           varchar(255) DEFAULT NULL COMMENT '用户ID',
    `user_name`         text         DEFAULT NULL COMMENT '用户名',
    `avatar`            text         DEFAULT NULL COMMENT '用户头像地址',
    `add_ts`            bigint       DEFAULT NULL COMMENT '记录添加时间戳',
    `last_modify_ts`    bigint       DEFAULT NULL COMMENT '记录最后修改时间戳',
    `comment_id`        bigint       DEFAULT NULL COMMENT '评论ID',
    `post_id`           bigint       DEFAULT NULL COMMENT '帖子ID',
    `content`           text         DEFAULT NULL COMMENT '评论内容',
    `create_time`       bigint       DEFAULT NULL COMMENT '评论时间戳',
    `sub_comment_count` text         DEFAULT NULL COMMENT '子评论数',
    `parent_comment_id` varchar(255) DEFAULT NULL COMMENT '父评论ID',
    `like_count`        text         DEFAULT '0' COMMENT '点赞数',
    PRIMARY KEY (`id`),
    KEY `idx_eastmoney_comment_id` (`comment_id`),
    KEY `idx_eastmoney_comment_post_id` (`post_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='东方财富评论';

-- ----------------------------
-- Table structure for eastmoney_user_info
-- 东方财富用户信息表
-- ----------------------------
DROP TABLE IF EXISTS `eastmoney_user_info`;
CREATE TABLE `eastmoney_user_info`
(
    `id`             int          NOT NULL AUTO_INCREMENT COMMENT '自增ID',
    `user_id`        varchar(255) NOT NULL COMMENT '用户ID',
    `user_name`      text         DEFAULT NULL COMMENT '用户名',
    `avatar`         text         DEFAULT NULL COMMENT '用户头像地址',
    `add_ts`         bigint       DEFAULT NULL COMMENT '记录添加时间戳',
    `last_modify_ts` bigint       DEFAULT NULL COMMENT '记录最后修改时间戳',
    `total_fans`     int          DEFAULT NULL COMMENT '粉丝数',
    `total_follows`  int          DEFAULT NULL COMMENT '关注数',
    `total_posts`    int          DEFAULT NULL COMMENT '帖子数',
    `is_verified`    int          DEFAULT NULL COMMENT '是否认证用户',
    `user_level`     int          DEFAULT NULL COMMENT '用户等级',
    PRIMARY KEY (`id`),
    UNIQUE KEY `idx_eastmoney_user_unique` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='东方财富用户信息';

-- ----------------------------
-- Table structure for xueqiu_post
-- 雪球帖子表
-- ----------------------------
DROP TABLE IF EXISTS `xueqiu_post`;
CREATE TABLE `xueqiu_post`
(
    `id`              int          NOT NULL AUTO_INCREMENT COMMENT '自增ID',
    `post_id`         bigint       NOT NULL COMMENT '帖子ID',
    `user_id`         varchar(255) DEFAULT NULL COMMENT '用户ID',
    `author_name`     text         DEFAULT NULL COMMENT '作者名称',
    `avatar`          text         DEFAULT NULL COMMENT '用户头像地址',
    `user_signature`  text         DEFAULT NULL COMMENT '用户签名',
    `add_ts`          bigint       DEFAULT NULL COMMENT '记录添加时间戳',
    `last_modify_ts`  bigint       DEFAULT NULL COMMENT '记录最后修改时间戳',
    `post_type`       text         DEFAULT NULL COMMENT '帖子类型',
    `title`           text         DEFAULT NULL COMMENT '帖子标题',
    `content`         text         DEFAULT NULL COMMENT '帖子内容',
    `create_time`     bigint       DEFAULT NULL COMMENT '发布时间戳',
    `liked_count`     text         DEFAULT NULL COMMENT '点赞数',
    `comment_count`   text         DEFAULT NULL COMMENT '评论数',
    `retweet_count`   text         DEFAULT NULL COMMENT '转发数',
    `read_count`      text         DEFAULT NULL COMMENT '阅读数',
    `post_url`        text         DEFAULT NULL COMMENT '帖子链接',
    `stock_code`      varchar(20)  DEFAULT NULL COMMENT '股票代码',
    `stock_name`      text         DEFAULT NULL COMMENT '股票名称',
    `source_keyword`  text         DEFAULT '' COMMENT '搜索来源关键字',
    PRIMARY KEY (`id`),
    UNIQUE KEY `idx_xueqiu_post_id` (`post_id`),
    KEY `idx_xueqiu_user_id` (`user_id`),
    KEY `idx_xueqiu_create_time` (`create_time`),
    KEY `idx_xueqiu_stock_code` (`stock_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='雪球帖子';

-- ----------------------------
-- Table structure for xueqiu_comment
-- 雪球评论表
-- ----------------------------
DROP TABLE IF EXISTS `xueqiu_comment`;
CREATE TABLE `xueqiu_comment`
(
    `id`                int          NOT NULL AUTO_INCREMENT COMMENT '自增ID',
    `user_id`           varchar(255) DEFAULT NULL COMMENT '用户ID',
    `user_name`         text         DEFAULT NULL COMMENT '用户名',
    `avatar`            text         DEFAULT NULL COMMENT '用户头像地址',
    `add_ts`            bigint       DEFAULT NULL COMMENT '记录添加时间戳',
    `last_modify_ts`    bigint       DEFAULT NULL COMMENT '记录最后修改时间戳',
    `comment_id`        bigint       DEFAULT NULL COMMENT '评论ID',
    `post_id`           bigint       DEFAULT NULL COMMENT '帖子ID',
    `content`           text         DEFAULT NULL COMMENT '评论内容',
    `create_time`       bigint       DEFAULT NULL COMMENT '评论时间戳',
    `sub_comment_count` text         DEFAULT NULL COMMENT '子评论数',
    `parent_comment_id` varchar(255) DEFAULT NULL COMMENT '父评论ID',
    `like_count`        text         DEFAULT '0' COMMENT '点赞数',
    PRIMARY KEY (`id`),
    KEY `idx_xueqiu_comment_id` (`comment_id`),
    KEY `idx_xueqiu_comment_post_id` (`post_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='雪球评论';

-- ----------------------------
-- Table structure for xueqiu_user_info
-- 雪球用户信息表
-- ----------------------------
DROP TABLE IF EXISTS `xueqiu_user_info`;
CREATE TABLE `xueqiu_user_info`
(
    `id`             int          NOT NULL AUTO_INCREMENT COMMENT '自增ID',
    `user_id`        varchar(255) NOT NULL COMMENT '用户ID',
    `user_name`      text         DEFAULT NULL COMMENT '用户名',
    `avatar`         text         DEFAULT NULL COMMENT '用户头像地址',
    `add_ts`         bigint       DEFAULT NULL COMMENT '记录添加时间戳',
    `last_modify_ts` bigint       DEFAULT NULL COMMENT '记录最后修改时间戳',
    `desc`           text         DEFAULT NULL COMMENT '用户描述',
    `follows`        int          DEFAULT NULL COMMENT '关注数',
    `fans`           int          DEFAULT NULL COMMENT '粉丝数',
    `total_posts`    int          DEFAULT NULL COMMENT '帖子数',
    `is_verified`    int          DEFAULT NULL COMMENT '是否认证',
    PRIMARY KEY (`id`),
    UNIQUE KEY `idx_xueqiu_user_unique` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='雪球用户信息';

-- ----------------------------
-- Table structure for tonghuashun_post
-- 同花顺帖子表
-- ----------------------------
DROP TABLE IF EXISTS `tonghuashun_post`;
CREATE TABLE `tonghuashun_post`
(
    `id`              int          NOT NULL AUTO_INCREMENT COMMENT '自增ID',
    `post_id`         varchar(255) NOT NULL COMMENT '帖子ID',
    `user_id`         varchar(255) DEFAULT NULL COMMENT '用户ID',
    `author_name`     text         DEFAULT NULL COMMENT '作者名称',
    `avatar`          text         DEFAULT NULL COMMENT '用户头像地址',
    `add_ts`          bigint       DEFAULT NULL COMMENT '记录添加时间戳',
    `last_modify_ts`  bigint       DEFAULT NULL COMMENT '记录最后修改时间戳',
    `post_type`       text         DEFAULT NULL COMMENT '帖子类型',
    `title`           text         DEFAULT NULL COMMENT '帖子标题',
    `content`         text         DEFAULT NULL COMMENT '帖子内容',
    `create_time`     bigint       DEFAULT NULL COMMENT '发布时间戳',
    `liked_count`     text         DEFAULT NULL COMMENT '点赞数',
    `comment_count`   text         DEFAULT NULL COMMENT '评论数',
    `share_count`     text         DEFAULT NULL COMMENT '分享数',
    `post_url`        text         DEFAULT NULL COMMENT '帖子链接',
    `stock_code`      varchar(20)  DEFAULT NULL COMMENT '股票代码',
    `stock_name`      text         DEFAULT NULL COMMENT '股票名称',
    `source_keyword`  text         DEFAULT '' COMMENT '搜索来源关键字',
    PRIMARY KEY (`id`),
    UNIQUE KEY `idx_tonghuashun_post_id` (`post_id`),
    KEY `idx_tonghuashun_user_id` (`user_id`),
    KEY `idx_tonghuashun_create_time` (`create_time`),
    KEY `idx_tonghuashun_stock_code` (`stock_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='同花顺帖子';

-- ----------------------------
-- Table structure for tonghuashun_comment
-- 同花顺评论表
-- ----------------------------
DROP TABLE IF EXISTS `tonghuashun_comment`;
CREATE TABLE `tonghuashun_comment`
(
    `id`                int          NOT NULL AUTO_INCREMENT COMMENT '自增ID',
    `user_id`           varchar(255) DEFAULT NULL COMMENT '用户ID',
    `user_name`         text         DEFAULT NULL COMMENT '用户名',
    `avatar`            text         DEFAULT NULL COMMENT '用户头像地址',
    `add_ts`            bigint       DEFAULT NULL COMMENT '记录添加时间戳',
    `last_modify_ts`    bigint       DEFAULT NULL COMMENT '记录最后修改时间戳',
    `comment_id`        bigint       DEFAULT NULL COMMENT '评论ID',
    `post_id`           varchar(255) DEFAULT NULL COMMENT '帖子ID',
    `content`           text         DEFAULT NULL COMMENT '评论内容',
    `create_time`       bigint       DEFAULT NULL COMMENT '评论时间戳',
    `sub_comment_count` text         DEFAULT NULL COMMENT '子评论数',
    PRIMARY KEY (`id`),
    KEY `idx_tonghuashun_comment_id` (`comment_id`),
    KEY `idx_tonghuashun_comment_post_id` (`post_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='同花顺评论';

-- ----------------------------
-- Table structure for sina_finance_post
-- 新浪财经帖子表
-- ----------------------------
DROP TABLE IF EXISTS `sina_finance_post`;
CREATE TABLE `sina_finance_post`
(
    `id`              int          NOT NULL AUTO_INCREMENT COMMENT '自增ID',
    `post_id`         bigint       NOT NULL COMMENT '帖子ID',
    `user_id`         varchar(255) DEFAULT NULL COMMENT '用户ID',
    `author_name`     text         DEFAULT NULL COMMENT '作者名称',
    `avatar`          text         DEFAULT NULL COMMENT '用户头像地址',
    `add_ts`          bigint       DEFAULT NULL COMMENT '记录添加时间戳',
    `last_modify_ts`  bigint       DEFAULT NULL COMMENT '记录最后修改时间戳',
    `post_type`       text         DEFAULT NULL COMMENT '帖子类型',
    `title`           text         DEFAULT NULL COMMENT '帖子标题',
    `content`         text         DEFAULT NULL COMMENT '帖子内容',
    `publish_time`    varchar(255) DEFAULT NULL COMMENT '发布时间',
    `liked_count`     text         DEFAULT NULL COMMENT '点赞数',
    `comment_count`   text         DEFAULT NULL COMMENT '评论数',
    `share_count`     text         DEFAULT NULL COMMENT '分享数',
    `post_url`        text         DEFAULT NULL COMMENT '帖子链接',
    `stock_code`      varchar(20)  DEFAULT NULL COMMENT '股票代码',
    `stock_name`      text         DEFAULT NULL COMMENT '股票名称',
    `source_keyword`  text         DEFAULT '' COMMENT '搜索来源关键字',
    PRIMARY KEY (`id`),
    UNIQUE KEY `idx_sina_finance_post_id` (`post_id`),
    KEY `idx_sina_finance_user_id` (`user_id`),
    KEY `idx_sina_finance_publish_time` (`publish_time`),
    KEY `idx_sina_finance_stock_code` (`stock_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='新浪财经帖子';

-- ----------------------------
-- Table structure for sina_finance_comment
-- 新浪财经评论表
-- ----------------------------
DROP TABLE IF EXISTS `sina_finance_comment`;
CREATE TABLE `sina_finance_comment`
(
    `id`                int          NOT NULL AUTO_INCREMENT COMMENT '自增ID',
    `user_id`           varchar(255) DEFAULT NULL COMMENT '用户ID',
    `user_name`         text         DEFAULT NULL COMMENT '用户名',
    `avatar`            text         DEFAULT NULL COMMENT '用户头像地址',
    `add_ts`            bigint       DEFAULT NULL COMMENT '记录添加时间戳',
    `last_modify_ts`    bigint       DEFAULT NULL COMMENT '记录最后修改时间戳',
    `comment_id`        bigint       DEFAULT NULL COMMENT '评论ID',
    `post_id`           bigint       DEFAULT NULL COMMENT '帖子ID',
    `content`           text         DEFAULT NULL COMMENT '评论内容',
    `publish_time`      varchar(255) DEFAULT NULL COMMENT '发布时间',
    `like_count`        text         DEFAULT NULL COMMENT '点赞数',
    `sub_comment_count` text         DEFAULT NULL COMMENT '子评论数',
    `parent_comment_id` varchar(255) DEFAULT NULL COMMENT '父评论ID',
    PRIMARY KEY (`id`),
    KEY `idx_sina_finance_comment_id` (`comment_id`),
    KEY `idx_sina_finance_comment_post_id` (`post_id`),
    KEY `idx_sina_finance_comment_time` (`publish_time`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='新浪财经评论';

-- ----------------------------
-- Table structure for sina_finance_user_info
-- 新浪财经用户信息表
-- ----------------------------
DROP TABLE IF EXISTS `sina_finance_user_info`;
CREATE TABLE `sina_finance_user_info`
(
    `id`             int          NOT NULL AUTO_INCREMENT COMMENT '自增ID',
    `user_id`        varchar(255) NOT NULL COMMENT '用户ID',
    `user_name`      text         DEFAULT NULL COMMENT '用户名',
    `avatar`         text         DEFAULT NULL COMMENT '用户头像地址',
    `add_ts`         bigint       DEFAULT NULL COMMENT '记录添加时间戳',
    `last_modify_ts` bigint       DEFAULT NULL COMMENT '记录最后修改时间戳',
    `desc`           text         DEFAULT NULL COMMENT '用户描述',
    `follows`        int          DEFAULT NULL COMMENT '关注数',
    `fans`           int          DEFAULT NULL COMMENT '粉丝数',
    PRIMARY KEY (`id`),
    UNIQUE KEY `idx_sina_finance_user_unique` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='新浪财经用户信息';

-- ----------------------------
-- Table structure for jinrongjie_post
-- 金融界帖子表
-- ----------------------------
DROP TABLE IF EXISTS `jinrongjie_post`;
CREATE TABLE `jinrongjie_post`
(
    `id`              int          NOT NULL AUTO_INCREMENT COMMENT '自增ID',
    `post_id`         varchar(255) NOT NULL COMMENT '帖子ID',
    `user_id`         varchar(255) DEFAULT NULL COMMENT '用户ID',
    `author_name`     text         DEFAULT NULL COMMENT '作者名称',
    `avatar`          text         DEFAULT NULL COMMENT '用户头像地址',
    `add_ts`          bigint       DEFAULT NULL COMMENT '记录添加时间戳',
    `last_modify_ts`  bigint       DEFAULT NULL COMMENT '记录最后修改时间戳',
    `post_type`       text         DEFAULT NULL COMMENT '帖子类型',
    `title`           text         DEFAULT NULL COMMENT '帖子标题',
    `content`         text         DEFAULT NULL COMMENT '帖子内容',
    `publish_time`    varchar(32)  DEFAULT NULL COMMENT '发布时间',
    `liked_count`     int          DEFAULT 0 COMMENT '点赞数',
    `comment_count`   int          DEFAULT 0 COMMENT '评论数',
    `post_url`        text         DEFAULT NULL COMMENT '帖子链接',
    `stock_code`      varchar(20)  DEFAULT NULL COMMENT '股票代码',
    `stock_name`      text         DEFAULT NULL COMMENT '股票名称',
    `source_keyword`  text         DEFAULT '' COMMENT '搜索来源关键字',
    PRIMARY KEY (`id`),
    UNIQUE KEY `idx_jinrongjie_post_id` (`post_id`),
    KEY `idx_jinrongjie_user_id` (`user_id`),
    KEY `idx_jinrongjie_publish_time` (`publish_time`),
    KEY `idx_jinrongjie_stock_code` (`stock_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='金融界帖子';

-- ----------------------------
-- Table structure for jinrongjie_comment
-- 金融界评论表
-- ----------------------------
DROP TABLE IF EXISTS `jinrongjie_comment`;
CREATE TABLE `jinrongjie_comment`
(
    `id`                int          NOT NULL AUTO_INCREMENT COMMENT '自增ID',
    `user_id`           varchar(255) DEFAULT NULL COMMENT '用户ID',
    `user_name`         text         DEFAULT NULL COMMENT '用户名',
    `avatar`            text         DEFAULT NULL COMMENT '用户头像地址',
    `add_ts`            bigint       DEFAULT NULL COMMENT '记录添加时间戳',
    `last_modify_ts`    bigint       DEFAULT NULL COMMENT '记录最后修改时间戳',
    `comment_id`        varchar(255) DEFAULT NULL COMMENT '评论ID',
    `post_id`           varchar(255) DEFAULT NULL COMMENT '帖子ID',
    `content`           text         DEFAULT NULL COMMENT '评论内容',
    `publish_time`      varchar(32)  DEFAULT NULL COMMENT '发布时间',
    `sub_comment_count` int          DEFAULT 0 COMMENT '子评论数',
    `parent_comment_id` varchar(255) DEFAULT NULL COMMENT '父评论ID',
    `like_count`        int          DEFAULT 0 COMMENT '点赞数',
    PRIMARY KEY (`id`),
    KEY `idx_jinrongjie_comment_id` (`comment_id`),
    KEY `idx_jinrongjie_comment_post_id` (`post_id`),
    KEY `idx_jinrongjie_comment_time` (`publish_time`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='金融界评论';

-- ----------------------------
-- Table structure for hexun_post
-- 和讯帖子表
-- ----------------------------
DROP TABLE IF EXISTS `hexun_post`;
CREATE TABLE `hexun_post`
(
    `id`              int          NOT NULL AUTO_INCREMENT COMMENT '自增ID',
    `post_id`         varchar(255) NOT NULL COMMENT '帖子ID',
    `title`           text         DEFAULT NULL COMMENT '帖子标题',
    `content`         text         DEFAULT NULL COMMENT '帖子内容',
    `post_url`        text         DEFAULT NULL COMMENT '帖子链接',
    `publish_time`    varchar(32)  DEFAULT NULL COMMENT '发布时间',
    `author_name`     text         DEFAULT '' COMMENT '作者名称',
    `user_id`         varchar(255) DEFAULT NULL COMMENT '用户ID',
    `avatar`          text         DEFAULT '' COMMENT '用户头像地址',
    `liked_count`     int          DEFAULT 0 COMMENT '点赞数',
    `comment_count`   int          DEFAULT 0 COMMENT '评论数',
    `stock_code`      varchar(20)  DEFAULT NULL COMMENT '股票代码',
    `stock_name`      text         DEFAULT NULL COMMENT '股票名称',
    `add_ts`          bigint       DEFAULT NULL COMMENT '记录添加时间戳',
    `last_modify_ts`  bigint       DEFAULT NULL COMMENT '记录最后修改时间戳',
    `source_keyword`  text         DEFAULT '' COMMENT '搜索来源关键字',
    PRIMARY KEY (`id`),
    UNIQUE KEY `idx_hexun_post_id` (`post_id`),
    KEY `idx_hexun_user_id` (`user_id`),
    KEY `idx_hexun_publish_time` (`publish_time`),
    KEY `idx_hexun_stock_code` (`stock_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='和讯帖子';

-- ----------------------------
-- Table structure for hexun_comment
-- 和讯评论表
-- ----------------------------
DROP TABLE IF EXISTS `hexun_comment`;
CREATE TABLE `hexun_comment`
(
    `id`                int          NOT NULL AUTO_INCREMENT COMMENT '自增ID',
    `comment_id`        varchar(255) DEFAULT NULL COMMENT '评论ID',
    `parent_comment_id` varchar(255) DEFAULT '' COMMENT '父评论ID',
    `content`           text         DEFAULT NULL COMMENT '评论内容',
    `user_name`         text         DEFAULT '' COMMENT '用户名',
    `user_id`           varchar(255) DEFAULT NULL COMMENT '用户ID',
    `avatar`            text         DEFAULT '' COMMENT '用户头像地址',
    `publish_time`      varchar(32)  DEFAULT NULL COMMENT '发布时间',
    `sub_comment_count` int          DEFAULT 0 COMMENT '子评论数',
    `post_id`           varchar(255) DEFAULT NULL COMMENT '帖子ID',
    `post_url`          text         DEFAULT NULL COMMENT '帖子链接',
    `like_count`        int          DEFAULT 0 COMMENT '点赞数',
    `add_ts`            bigint       DEFAULT NULL COMMENT '记录添加时间戳',
    `last_modify_ts`    bigint       DEFAULT NULL COMMENT '记录最后修改时间戳',
    PRIMARY KEY (`id`),
    KEY `idx_hexun_comment_id` (`comment_id`),
    KEY `idx_hexun_comment_post_id` (`post_id`),
    KEY `idx_hexun_comment_time` (`publish_time`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='和讯评论';

-- ----------------------------
-- Table structure for stock_info
-- 股票基础信息表
-- ----------------------------
DROP TABLE IF EXISTS `stock_info`;
CREATE TABLE `stock_info`
(
    `id`             int         NOT NULL AUTO_INCREMENT COMMENT '自增ID',
    `stock_code`     varchar(20) NOT NULL COMMENT '股票代码',
    `stock_name`     text        DEFAULT NULL COMMENT '股票名称',
    `stock_type`     varchar(20) DEFAULT NULL COMMENT '股票类型:A股/港股/美股',
    `exchange`       varchar(20) DEFAULT NULL COMMENT '交易所:上交所/深交所',
    `industry`       text        DEFAULT NULL COMMENT '所属行业',
    `sector`         text        DEFAULT NULL COMMENT '所属板块',
    `listing_date`   varchar(32) DEFAULT NULL COMMENT '上市日期',
    `market_cap`     bigint      DEFAULT NULL COMMENT '市值',
    `total_shares`   bigint      DEFAULT NULL COMMENT '总股本',
    `add_ts`         bigint      DEFAULT NULL COMMENT '记录添加时间戳',
    `last_modify_ts` bigint      DEFAULT NULL COMMENT '记录最后修改时间戳',
    PRIMARY KEY (`id`),
    UNIQUE KEY `idx_stock_code_unique` (`stock_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='股票基础信息';

-- ----------------------------
-- Table structure for daily_news
-- 每日新闻表(用于热点新闻)
-- ----------------------------
DROP TABLE IF EXISTS `daily_news`;
CREATE TABLE `daily_news`
(
    `id`              int          NOT NULL AUTO_INCREMENT COMMENT '自增ID',
    `news_id`         varchar(128) NOT NULL COMMENT '新闻唯一ID',
    `source_platform` varchar(32)  DEFAULT NULL COMMENT '新闻源平台',
    `title`           text         DEFAULT NULL COMMENT '新闻标题',
    `url`             text         DEFAULT NULL COMMENT '新闻链接',
    `description`     text         DEFAULT NULL COMMENT '新闻描述',
    `crawl_date`      varchar(32)  DEFAULT NULL COMMENT '爬取日期',
    `rank_position`   int          DEFAULT NULL COMMENT '排名位置',
    `stock_code`      varchar(20)  DEFAULT NULL COMMENT '相关股票代码',
    `stock_name`      text         DEFAULT NULL COMMENT '相关股票名称',
    `add_ts`          bigint       DEFAULT NULL COMMENT '记录添加时间戳',
    `last_modify_ts`  bigint       DEFAULT NULL COMMENT '记录最后修改时间戳',
    PRIMARY KEY (`id`),
    UNIQUE KEY `idx_daily_news_unique` (`news_id`),
    KEY `idx_daily_news_crawl_date` (`crawl_date`),
    KEY `idx_daily_news_stock_code` (`stock_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='每日新闻表';
