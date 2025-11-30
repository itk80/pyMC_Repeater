# src/models.py
from sqlalchemy import Column, Integer, Float, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class DiscoveredNode(Base):
    __tablename__ = "discovered_nodes"

    node_id = Column(Integer, primary_key=True)          # hash 0–255
    pubkey = Column(String, unique=True, nullable=False) # pełny klucz publiczny (hex)
    node_name = Column(String)
    contact_type = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    rssi = Column(Integer)
    snr = Column(Float)
    first_seen = Column(DateTime, default=datetime.utcnow)
    last_seen = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    advert_count = Column(Integer, default=1)
    is_active = Column(Boolean, default=True)

from .db import engine
Base.metadata.create_all(engine)