#!/usr/bin/python3

from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from utils.conn import Base

class Menu(Base):
    __tablename__ = 'menu'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(20), unique=True, nullable=False)
    url = Column(String(50), unique=True)
    note = Column(Text)

    parent_id = Column(Integer, ForeignKey('menu.id', name='parent_id_fk'),
                       default=0, server_default='0')

    children = relationship('Menu', backref='parent')
