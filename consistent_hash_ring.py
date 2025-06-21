import hashlib
import bisect
from typing import List, Dict

class ConsistentHashRing:

    def __init__(self, nodes: List[str], virtual_nodes:int = 100):
        self.virtual_nodes = virtual_nodes
        self.ring: Dict[int, str] = {}
        self.sorted_keys: List[int] = []

        for node in nodes:
            self.add_node(node)


    def _hash_value(self, key:str) -> int:
        return int(hashlib.sha256(key.encode()).hexdigest(), 16)
    

    def add_node(self, node: str):
        for i in range(self.virtual_nodes):
            virtual_node_id = f"{node}-vn{i}"
            hash_val = self._hash_value(virtual_node_id)
            self.ring[hash_val] = node
            bisect.insort(self.sorted_keys, hash_val)


    def remove_node(self, node: str):
        for i in range(self.virtual_nodes):
            virtual_node_id = f"{node}-vn{i}"
            hash_val = self._hash_value(virtual_node_id)
            self.ring.pop(hash_val, None)
            idx = bisect.bisect_left(self.sorted_keys, hash_val)
            if idx < len(self.sorted_keys) and self.sorted_keys[idx] == hash:
                self.sorted_keys.pop(idx)


    def get_nodes(self, key: str, n: int =1) -> List[str]:
        hash = self._hash_value(key)
        start = bisect.bisect(self.sorted_keys, hash)
        result = []
        i = start
        while len(result) < n:
            index = i%len(self.sorted_keys)
            node = self.ring[self.sorted_keys[index]]
            if node not in result:
                result.append(node)
            i += 1
        return result