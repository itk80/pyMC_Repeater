# src/models.py
from sqlalchemy import Column, Integer, Float, String, DateTime, Boolean, func
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class DiscoveredNode(Base):
    __tablename__ = "discovered_nodes"

    node_id = Column(Integer, primary_key=True)     # adres LoRa, np. 0x12
    node_name = Column(String, nullable=True)       # opcjonalnie
    rssi = Column(Integer, nullable=True)
    snr = Column(Float, nullable=True)
    first_seen = Column(DateTime, default=datetime.utcnow)
    last_seen = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    hops = Column(Integer, default=1)
    via_node_id = Column(Integer, nullable=True)
    is_active = Column(Boolean, default=True)

# Tworzy tabelę przy pierwszym imporcie
from .db import engine
Base.metadata.create_all(engine)