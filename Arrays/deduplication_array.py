# Deduplication of events based on user_id and event type, keeping the latest timestamp
from datetime import datetime

# Sample event data with potential duplicates
events = [
    {"user_id": 1, "event": "click", "ts": "2026-04-15 10:00:00"},
    {"user_id": 1, "event": "click", "ts": "2026-04-15 10:05:00"},  # Later timestamp for same user/event
    {"user_id": 2, "event": "view", "ts": "2026-04-15 09:00:00"},
]

# Dictionary to store the latest event for each (user_id, event) combination
latest = {}

# Process each event
for e in events:
    # Create a unique key for each user-event combination
    key = (e["user_id"], e["event"])
    # Parse the timestamp string into a datetime object
    ts = datetime.strptime(e["ts"], "%Y-%m-%d %H:%M:%S")

    # If this is the first occurrence or a later timestamp, update the latest record
    if key not in latest or ts > latest[key]["ts"]:
        latest[key] = {"data": e, "ts": ts}

# Extract the deduplicated event data
result = [v["data"] for v in latest.values()]
print(result)
