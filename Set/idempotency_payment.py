# Idempotent payment processing using a set to prevent duplicate processing
# Idempotency ensures that processing the same payment multiple times has the same effect as processing it once

# Set to track payment IDs that have already been processed
processed_ids = set()

def process_payment(payment):
    """
    Process a payment with idempotency check.

    Args:
        payment: Dictionary containing payment data with an 'id' key

    Returns:
        "Processed" if payment was successfully processed
        "Duplicate - Skipped" if payment was already processed
    """
    pid = payment["id"]  # Extract payment ID

    # Check if this payment has already been processed
    if pid in processed_ids:
        return "Duplicate - Skipped"

    # Process the payment (placeholder for actual payment logic)
    processed_ids.add(pid)  # Mark as processed
    return "Processed"