"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""
import collections


class Node:
    def __init__(self, key=None, data=None):
        self.val = data
        self.next = None
        self.pre = None
        self.key = key


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.pre = self.head
        self.dict_node = collections.defaultdict(Node)

    def get(self, key: int) -> int:
        if key in self.dict_node:
            # move to pre tail
            self.dict_node[key].pre.next = self.dict_node[key].next
            self.dict_node[key].next.pre = self.dict_node[key].pre
            self.dict_node[key].pre = self.tail.pre
            self.tail.pre.next = self.dict_node[key]
            self.tail.pre = self.dict_node[key]
            self.dict_node[key].next = self.tail
            self.print_list()
            return self.dict_node[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict_node:
            # update
            self.dict_node[key].pre.next = self.dict_node[key].next
            self.dict_node[key].next.pre = self.dict_node[key].pre
            self.dict_node[key].pre = self.tail.pre
            self.tail.pre.next = self.dict_node[key]
            self.tail.pre = self.dict_node[key]
            self.dict_node[key].next = self.tail
            self.dict_node[key].val = value
        elif len(self.dict_node) < self.capacity:  # not full insert from tail
            new_node = Node(key, value)
            self.dict_node[key] = new_node
            new_node.pre = self.tail.pre
            new_node.next = self.tail
            self.tail.pre.next = new_node
            self.tail.pre = new_node
        else:  # remove the least recently used from head
            # remove from dictionary
            del self.dict_node[self.head.next.key]
            # remove from chain
            self.head.next = self.head.next.next
            self.head.next.pre = self.head
            self.put(key, value)
        self.print_list()

    def print_list(self):
        node = self.head
        while (node.next is not None):
            print(node.val if node.val is not None else 'head ', end='', sep='')
            node = node.next
        print(' tail')
        print('-----------------------')


"""
from collections import OrderedDict

class LRUCache:
    dict = None
    capacity = None

    def __init__(self, capacity: int):
        self.dict = OrderedDict()
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        
        self.dict.move_to_end(key)
        return self.dict[key]

    def put(self, key: int, value: int) -> None:
        self.dict[key] = value
        self.dict.move_to_end(key)
        if len(self.dict) > self.capacity:
            self.dict.popitem(last=False)
"""