# Log filtering example: Extract error logs from a list of log entries

# Sample log data
logs = [
    "2026-04-15 INFO User logged in",
    "2026-04-15 ERROR Payment failed"
]

# Filter logs to get only ERROR level entries using list comprehension
error_logs = [log for log in logs if "ERROR" in log]

# The error_logs list now contains only the ERROR entries
# This demonstrates basic log filtering and list comprehensions