def flatten_json(data, parent_key="", sep="_"):
    """
    Recursively flatten a nested dictionary/JSON structure.

    Args:
        data: The nested dictionary to flatten
        parent_key: The parent key path (used in recursion)
        sep: Separator for nested keys (default: "_")

    Returns:
        A flattened dictionary with concatenated keys
    """
    items = {}  # Store flattened key-value pairs

    # Iterate through each key-value pair in the current dictionary
    for k, v in data.items():
        # Create new key by appending current key to parent key path
        new_key = f"{parent_key}{sep}{k}" if parent_key else k

        # If value is a dictionary, recursively flatten it
        if isinstance(v, dict):
            items.update(flatten_json(v, new_key, sep))
        else:
            # If value is not a dict, add it to flattened items
            items[new_key] = v

    return items

# Example usage
data = {"user": {"id": 1, "name": "Alice", "address": {"city": "New York", "zip": "10001"}}}
flatten_json(data)  # This call doesn't print anything
print("\nFlattened JSON:")
print(flatten_json(data))