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
        self.min = 8
        self.storage_count = 0

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
        # Understand:
            # Search list for key
            # If key matches another, replace the value
            # if not, append record to the list

        # the value being placed at the given spot
        index = self.hash_index(key)
        # each new entry is placed within a node which will create a linked list
        new_input = HashTableEntry(key, value)
        # if there's nothing there, place new input in that bucket
        if self.storage[index] is None:
            self.storage[index] = new_input
            self.storage_count += 1
        else:
            # will have a key, value of current node
            curr_node = self.storage[index]
            # print("curr_node k/v ----> ", curr_node.key ,curr_node.value)
            # while the current node exists, check to see if key matches, otherwise attach curr node to tail and place new node at the beginning
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
                self.storage_count += 1
                # print("curr node next--->", curr_node.key)
            tail.next = new_input
    

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        warning = "There's nothing to delete dude."
        index = self.hash_index(key)
        # self.storage[index] brings you the value of an element at that end point
        curr_node = self.storage[index]
        # if storage bucket is empty, print warning that nothing can be deleted
        if not self.storage[index]:
            print(warning)
            return None
        # As long as self.storage exists search for the key and delete
        else: 
            # while the node isn't empty
            while curr_node is not None: 
                # print("Next node", curr_node.next.value)
                if curr_node.key == key:
                    self.storage[index] = curr_node.next
                    curr_node = None
                    print(f'{key} deleted')
                    self.storage_count -= 1
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
        

    def resize(self):
        """
        Load Factor: number of elements in list / number of slots
        25 items in 6 slots would be a nightmare. 

        If load > 0.7: double
        If load < 0.2: halve
            min: 8

        Need to resize the hash table based on the Load Factor

        Creates new table either larger or smaller based on LF.

        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
        # make a new, bigger table/array
        # Go through all linked lists/indexes to count each element and create our new table 
        # Resize is a double either larger or smaller
        
        # gather original storage container
        old = self.storage
        new_capacity = self.capacity * 2
        print("storage count --> ", self.storage_count)
        # contains length of old storage to determine size adjust
        # use self.capacity as length of old storage
        load_factor = self.storage_count / self.capacity
        print("load factor --> ", load_factor)

        if load_factor > .7:
            self.storage = [None] * new_capacity
        for node in old:
            while node is not None:
                self.put(node.key, node.value)
                node = node.next

        return
        # iterate through the old storage to see if there are collisions
        # for i in range(len(old)):
        #     node = old[i]
        #     count += 1
        #     print("node", node.next)
        #     print("count", count)
        #     while node is not None:
        #         if node.next is not None:
        #             count += 1
        #             self.storage[i].next = None
 

        # count the number of nodes within the storage
        # Get load factor count / self.capacity
        # if lf > .7: 
        #   new capacity * 2
        #   rehash all key, value pairs
        

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
    ht.resize()
    # new_capacity = len(ht.storage)

    # # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    # print(ht.get("line_1"))
    # print(ht.get("line_2"))
    # print(ht.get("line_3"))

    print("")
