#sessionization based on 30 minutes window
from datetime import datetime, timedelta

events = [
    ("u1", "2026-04-15 10:00:00"),
    ("u1", "2026-04-15 10:10:00"),
    ("u1", "2026-04-15 11:00:00"),
]

SESSION_GAP = timedelta(minutes=30)
print(f"Session gap: {SESSION_GAP}")
sessions = []
current_session = []

prev_time = None

for user, ts in events:
    time = datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")
    
    if not prev_time or (time - prev_time) <= SESSION_GAP:
        current_session.append((user, ts))
    else:
        sessions.append(current_session)
        current_session = [(user, ts)]
    
    prev_time = time

if current_session:
    sessions.append(current_session)
print(f"Sessions: {sessions}")
print(f"Current session: {current_session}")