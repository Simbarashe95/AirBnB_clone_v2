#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel):
    """ Review classto store review information """
    _tablename_ = 'reviews'
    place_id = Column(String(60), ForeignKey("places.id"),
			   nulluable=False
    user_id = Column(String(60), ForeignKey("users.id"),
		      nullable=False)
    text = Column(String(1024), nullable=FALSE)
