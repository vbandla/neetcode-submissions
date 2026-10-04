class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None
class MyHashSet:

    def __init__(self):
        self.hash_set = [ListNode(0) for _ in range(10**4)]

    def add(self, key: int) -> None:
        listNode = self.hash_set[key % len(self.hash_set)]
        while listNode.next :
            if (listNode.next.key == key):
                return
            listNode = listNode.next    
        listNode.next =  ListNode(key)

            

    def remove(self, key: int) -> None:
        listNode = self.hash_set[key % len(self.hash_set)]
        while listNode.next :
            if (listNode.next.key == key):
                listNode.next = listNode.next.next
                return
            else:
                listNode = listNode.next    
        

    def contains(self, key: int) -> bool:
        
        listNode = self.hash_set[key % len(self.hash_set)]
        while listNode.next :
            if (listNode.next.key == key):
                return True
            listNode = listNode.next  
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)