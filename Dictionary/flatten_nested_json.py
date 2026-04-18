def flatten_json(data, parent_key="", sep="_"):
    items = {}
    
    for k, v in data.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        
        if isinstance(v, dict):
            items.update(flatten_json(v, new_key))
        else:
            items[new_key] = v
            
    return items

# Example
data = {"user": {"id": 1, "name": "Alice", "address": {"city": "New York", "zip": "10001"}}}
flatten_json(data)
print("\nFlattened JSON:")
print(flatten_json(data))