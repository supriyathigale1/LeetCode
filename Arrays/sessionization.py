# Sessionization: Group events into sessions based on a 30-minute time window
from datetime import datetime, timedelta

# Sample event data: (user_id, timestamp)
events = [
    ("u1", "2026-04-15 10:00:00"),
    ("u1", "2026-04-15 10:10:00"),  # Within 30 min of previous
    ("u1", "2026-04-15 11:00:00"),  # More than 30 min later - new session
]

# Define session gap threshold (30 minutes)
SESSION_GAP = timedelta(minutes=30)
print(f"Session gap: {SESSION_GAP}")

# Store completed sessions
sessions = []
# Current session being built
current_session = []

# Track previous event time for gap calculation
prev_time = None

# Process each event
for user, ts in events:
    # Parse timestamp string to datetime object
    time = datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")

    # Check if this event belongs to current session or starts a new one
    if not prev_time or (time - prev_time) <= SESSION_GAP:
        # Same session: add event to current session
        current_session.append((user, ts))
    else:
        # New session: save current session and start new one
        sessions.append(current_session)
        current_session = [(user, ts)]

    # Update previous time for next iteration
    prev_time = time

# Add the final session if it has events
if current_session:
    sessions.append(current_session)

print(f"Sessions: {sessions}")
print(f"Current session: {current_session}")