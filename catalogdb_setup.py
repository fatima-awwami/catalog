from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key = True)
    name = Column(String(250), nullable = False)
    email = Column(String(250),nullable = False)
    picture = Column(String(250))


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False,unique=True)
    status = Column(String(1), nullable=False)
    image = Column(String(250))
    user_id = Column(Integer,ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'id'           : self.id,
           'name'         : self.name,
           'image'        : self.image,
       }

class CategoryItem(Base):
    __tablename__ = 'category_item'
    title =Column(String(250), nullable = False, unique=True)
    id = Column(Integer, primary_key = True)
    description = Column(String(250))
    price = Column(Integer,nullable=False)
    status = Column(String(1),nullable = False)
    image = Column(String(250))
    category_id = Column(Integer,ForeignKey('category.id'))
    category = relationship(Category)
    user_id = Column(Integer,ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'id'           : self.id,
           'title'        : self.title,
           'price'        : self.price,
           'description'  : self.description,
           'image'        : self.image,
       }

engine = create_engine('sqlite:///catalog.db',connect_args={'check_same_thread':False})

Base.metadata.create_all(engine)
