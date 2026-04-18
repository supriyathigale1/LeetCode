#idempotent payment processing To be expanded
processed_ids = set()

def process_payment(payment):
    pid = payment["id"]
    
    if pid in processed_ids:
        return "Duplicate - Skipped"
    
    # process payment
    processed_ids.add(pid)
    return "Processed"