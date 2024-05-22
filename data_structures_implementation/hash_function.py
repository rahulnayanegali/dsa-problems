class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self.hash(key)
        self.table[index] = value

    def get(self, key):
        index = self.hash(key)
        return self.table[index]

    def delete(self, key):
        index = self.hash(key)
        self.table[index] = None


hash_map = HashTable(10)
hash_map.put('apple', 5)
hash_map.put('banana', 10)
print(hash_map.get('apple'))  # Output: 5
print(hash_map.get('banana'))  # Output: 10
hash_map.delete('apple')
print(hash_map.get('apple'))  # Output: None