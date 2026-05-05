from dataclasses import dataclass
from datetime import datetime

@dataclass
class NetworkNode:
    ip: str
    hostname: str
    snmp_community: str

@dataclass
class TrafficMetric:
    node_id: str
    timestamp: datetime
    bytes_in: int
    bytes_out: int
