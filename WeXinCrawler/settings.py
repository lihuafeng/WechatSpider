# -*- coding: utf-8 -*-

# Scrapy settings for WeXinCrawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'WeXinCrawler'

SPIDER_MODULES = ['WeXinCrawler.spiders']
NEWSPIDER_MODULE = 'WeXinCrawler.spiders'

ROBOTSTXT_OBEY = False

DOWNLOAD_DELAY = 30

ITEM_PIPELINES = {
  # 'WeXinCrawler.pipelines.MongDBPipeline': 300,
    'WeXinCrawler.pipelines.MysqlTwistedPipline': 300,
}



# 公账号授权的信息的list，用于在爬虫被禁掉时，自动切换账户
AUTH_LIST = [
             {'Account':'puji2017@139.com','PassWord':'xsp19890910'},
             # {'Account':'lhflhm20081989@sina.com','PassWord':'1234Qwer'}
            ]
# 需要爬取的公帐号的名称，暂不支持同时爬取多个公帐号
# OFFICIAL_ACCOUNTS = 'Shuiku-net'
# OFFICIAL_ACCOUNTS = 'worldofboss'
OFFICIAL_ACCOUNTS = 'jingshuoriben'

# 是否需要使用语音播报，爬虫运行状态,当为True时，需要安装 python win32com 模块
SPEEK_ALLOW = False

# MongDB数据库配置
MONGO_HOST = "127.0.0.1"  # 主机IP
MONGO_PORT = 27017  # 端口号
MONGO_DB = "Weixin_Spider"  # 库名
MONGO_COLLECTION = "weixin_article"  # collection名

# MySQL数据库连接
MYSQL_HOST = "127.0.0.1"
MYSQL_DBNAME = "test"
MYSQL_USER = "root"
MYSQL_PASSWORD = ""