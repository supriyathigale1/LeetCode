logs = [
    "2026-04-15 INFO User logged in",
    "2026-04-15 ERROR Payment failed"
]

error_logs = [log for log in logs if "ERROR" in log]