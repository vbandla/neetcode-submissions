class MyHashMap:

    def __init__(self):
       self.hash_set = [ListNode(0,0) for _ in range(10**4)] 

    def put(self, key: int, value: int) -> None:
        listNode = self.hash_set[key % len(self.hash_set)]
        while listNode.next :
            if (listNode.next.key == key):
                listNode.next.value = value
                return
            listNode = listNode.next    
        listNode.next =  ListNode(key,value)

    def get(self, key: int) -> int:
        listNode = self.hash_set[key % len(self.hash_set)]
        while listNode.next :
            if (listNode.next.key == key):
                return listNode.next.value
            listNode = listNode.next
        return -1        

    def remove(self, key: int) -> None:
        listNode = self.hash_set[key % len(self.hash_set)]
        while listNode.next :
            if (listNode.next.key == key):
                listNode.next = listNode.next.next
                return
            else:
                listNode = listNode.next
        
class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

            
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)