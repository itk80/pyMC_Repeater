# src/nodes.py
from datetime import datetime
from .models import DiscoveredNode
from .db import SessionLocal

def upsert_repeater(
    pubkey: str,
    node_id: int,
    node_name: str = None,
    contact_type: str = None,
    latitude: float = None,
    longitude: float = None,
    rssi: int = None,
    snr: float = None,
):
    db = SessionLocal()
    node = db.query(DiscoveredNode).filter(DiscoveredNode.pubkey == pubkey).first()
    now = datetime.utcnow()

    if node:
        node.last_seen = now
        node.is_active = True
        node.advert_count += 1
    else:
        node = DiscoveredNode(
            node_id=node_id,
            pubkey=pubkey,
            node_name=node_name,
            contact_type=contact_type,
            latitude=latitude,
            longitude=longitude,
            first_seen=now,
            last_seen=now,
            advert_count=1,
            is_active=True
        )
        db.add(node)

    if node_name: node.node_name = node_name
    if contact_type: node.contact_type = contact_type
    if latitude is not None: node.latitude = latitude
    if longitude is not None: node.longitude = longitude
    if rssi is not None: node.rssi = rssi
    if snr is not None: node.snr = snr

    db.commit()
    db.close()

def get_all_repeaters():
    db = SessionLocal()
    nodes = db.query(DiscoveredNode).order_by(DiscoveredNode.last_seen.desc()).all()
    db.close()
    return nodes