class ListNode:
   def __init__(self,key):
      self.key=key
      self.next=None
class hashSet:
  def __init__(self):
      self.set=[ListNode(0) for i in range(10^^4)]

  def add(self,key:int):
      index=key%len(self.set)
      cur=self.set[index]
      while cur.next:
        if cur.next.key==key:
        return
        cur=cur.next
      cur.next.key=ListNode(key)

  def contains(self,key:int)->bool:
       cur=self.set[key%len(self.set)]
       while cur.next:
          if cur.next.key==key:
             return True
          cur=cur.next
         return False

  def remove(self,key:int):
     cur=self.set[key%len(self.set)]
     while cur.next:
         if cur.next.key==key:
           cur.next=cur.next.next
         cur=cur.next
       
