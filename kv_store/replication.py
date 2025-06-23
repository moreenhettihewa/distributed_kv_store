class Replication:

    def get_replicas(self,key_hash, ring, replication_factor):
        ring_hashes = [hash for hash, _ in ring]
        # Find nodes which are clockwise directed  
        for i, h in enumerate(ring_hashes):
            if key_hash <= h:
                start = i
                break
        else:
            start = 0

        result = []
        seen_nodes = set()
        i = start
        while len(result) < replication_factor:
            _, node_id = ring[i%len(ring)]
            if node_id not in seen_nodes:
                result.append(node_id)
                seen_nodes.add(node_id)
            i+=1

        return result
    
# TODO Replicate KV for replicas ( via REST)
