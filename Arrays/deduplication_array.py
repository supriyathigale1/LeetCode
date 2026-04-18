#depduplication of data based on user_id,event 
from datetime import datetime

events = [
    {"user_id": 1, "event": "click", "ts": "2026-04-15 10:00:00"},
    {"user_id": 1, "event": "click", "ts": "2026-04-15 10:05:00"},
    {"user_id": 2, "event": "view", "ts": "2026-04-15 09:00:00"},
]

latest = {}

for e in events:
    key = (e["user_id"], e["event"])
    ts = datetime.strptime(e["ts"], "%Y-%m-%d %H:%M:%S")
    
    if key not in latest or ts > latest[key]["ts"]:
        latest[key] = {"data": e, "ts": ts}

result = [v["data"] for v in latest.values()]
print(result)
