# src/nodes.py
from datetime import datetime
from .models import DiscoveredNode
from .db import SessionLocal

def upsert_node(node_id: int, rssi=None, snr=None, via_node_id=None, hops=1, node_name=None):
    db = SessionLocal()
    node = db.get(DiscoveredNode, node_id)
    now = datetime.utcnow()
    
    if node:
        node.last_seen = now
        node.is_active = True
        if rssi is not None: node.rssi = rssi
        if snr is not None: node.snr = snr
        if via_node_id is not None: node.via_node_id = via_node_id
        if hops > node.hops: node.hops = hops
        if node_name: node.node_name = node_name
    else:
        node = DiscoveredNode(
            node_id=node_id,
            node_name=node_name,
            rssi=rssi,
            snr=snr,
            first_seen=now,
            last_seen=now,
            via_node_id=via_node_id,
            hops=hops,
            is_active=True
        )
        db.add(node)
    
    db.commit()
    db.close()

def get_all_nodes():
    db = SessionLocal()
    nodes = db.query(DiscoveredNode).order_by(DiscoveredNode.last_seen.desc()).all()
    db.close()
    return nodes

def mark_all_inactive():
    db = SessionLocal()
    db.query(DiscoveredNode).update({DiscoveredNode.is_active: False})
    db.commit()
    db.close()