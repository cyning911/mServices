#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+pymysql://root:root@47.118.49.97:3306/edu?charset=utf8')

# 生成连接数据库的类
DbSession = sessionmaker(bind=engine)

# 创建会话类对象
session = DbSession()

# 生成所有模型类的父类
Base = declarative_base(bind=engine)