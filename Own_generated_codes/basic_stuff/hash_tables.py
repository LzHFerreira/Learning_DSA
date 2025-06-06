# Simple Hash Map Implementation. Hashing handled by Python's built-in dictionary.
class HashMap:
    def __init__(self):
        self._map = {}  # Use Python's built-in dictionary for storage

    def put(self, key, value):
        # Store the value using the key in the dictionary
        self._map[key] = value

    def get(self, key):
        # Retrieve the value for the given key, or None if not found
        return self._map.get(key)

    def remove(self, key):
        # Remove the key-value pair if the key exists
        if key in self._map:
            del self._map[key]

    def contains(self, key):
        # Check if the key exists in the hash map
        return key in self._map

    def keys(self):
        # Return a list of all keys
        return list(self._map.keys())

    def values(self):
        # Return a list of all values
        return list(self._map.values())

    def items(self):
        # Return a list of all key-value pairs
        return list(self._map.items())


# Example usage:
if __name__ == "__main__":
    hashmap = HashMap()  # Create a new hash map
    hashmap.put("apple", 3)  # Insert key "apple" with value 3
    hashmap.put("banana", 5)  # Insert key "banana" with value 5
    print(hashmap.get("apple"))  # Output: 3
    print(hashmap.contains("banana"))  # Output: True
    hashmap.remove("apple")  # Remove key "apple"
    print(hashmap.get("apple"))  # Output: None
    print(hashmap.keys())  # Output: ['banana']
    print(hashmap.values())  # Output: [5]
    print(hashmap.items())  # Output: [('banana', 5)]
