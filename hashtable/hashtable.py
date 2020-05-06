class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """
    def __init__(self, key, value, head=None):
        self.key = key
        self.value = value
        self.next = None
        self.head = None
    

    
class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * self.capacity

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """
        fnv_offset = str(key).encode()
        total = 0

        for i in fnv_offset:
            total += i
            total &= 0xffffffffffffffff

        return total 
        # Implement to last line of the loop

    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # index = random assignment of the key
        # self.storage[index] is the value of the key
        
        # print("PUT INDEX --> ", index)
        # the value being placed at the given spot
        # self.storage[index] = value
        # print("PUT self.storage value--> ", index)
        # each new entry is placed within a node which will create a linked list
        # if there is nothing inside of the index, place the new input node inside of the storage index
        # The random place each k/v pair is placed
        index = self.hash_index(key)
        new_input = HashTableEntry(key, value)
        if self.storage[index] is None:
            self.storage[index] = new_input
        else:
            # will have an key, value of current node
            curr_node = self.storage[index]
            # print("curr_node k/v ----> ", curr_node.key ,curr_node.value)
            while curr_node:
                # does the key match?
                if curr_node.key == key:
                    # swap the values
                    curr_node.value = value
                    return
                # assign our current node as tail
                tail = curr_node
                # make our current node the next node
                curr_node = curr_node.next
                # print("curr node next--->", curr_node.key)
            tail.next = new_input
                
        # Search list for key
        # If key matches another, replace the value
        # if not, append record to the list



    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        warning = "Cannot Delete"
        index = self.hash_index(key)
        curr_node = self.storage[index]
        # self.storage[index] brings you the value of an element at that end point
        # if not found display warning
        if not self.storage[index]:
            print(warning)
            return None
        # As long as self.storage exists search for the key and delete
        else: 
            while curr_node is not None: 
            #       if self.storage exists, delete the key
                # print("Next node", curr_node.next.value)
                if curr_node.key == key:
                    self.storage[index] = curr_node.next
                    curr_node = None
                    print(f'{key} deleted')
                    return curr_node
                elif curr_node.next is not None:
                    curr_node = curr_node.next
                    # print("curr_node.next", curr_node)
                else:
                    print(warning)
                    return None

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        curr_node = self.storage[index]
        if curr_node is not None:
            while curr_node:
                if curr_node.key == key:
                    # print("STORAGE VALUE -->", curr_node.value)
                    return curr_node.value
                curr_node = curr_node.next
                # print("GET CURR NODE -->", curr_node)
            return None
        else:
            return None
        

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """

if __name__ == "__main__":
    ht = HashTable(2)
    print(ht.storage)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    
    ht.put("line_3", "Linked list saves the day!")
    ht.put("line_4", "replacement value")

    print(ht.storage)
    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print("Next value before deletion --> ", ht.get("line_1"))
    # print(ht.get("line_2"))
    # print(ht.get("line_3"))
    # print(ht.delete("line_44"))
    # print("line after deletion --> ", ht.get("line_4"))


    # # Test resizing
    # old_capacity = len(ht.storage)
    # ht.resize()
    # new_capacity = len(ht.storage)

    # # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    # print(ht.get("line_1"))
    # print(ht.get("line_2"))
    # print(ht.get("line_3"))

    print("")
