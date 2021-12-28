class Node:
    #->代表返回的数据类型，后面跟数据类型
    def __init__(self,val) -> None:
        self.val=val
        self.next=None

class SingleLinkList:
    def __init__(self) -> None:
        self._head=None

    #头部添加节点
    def add(self,new_val):
        node=Node(new_val)
        node.next=self._head
        self._head=node

    #尾部添加节点
    def append(self,new_val):
        #定位头节点
        cur=self._head
        #如果尾节点为空，则将该新节点加入头部
        if not cur:
            self.add(new_val)
        else:
        #尾节点不为空，遍历到最后一个节点
            node=Node(new_val)
            while cur.next:
                cur=cur.next
            cur.next=node
    
    @property
    def is_empty(self):
        if self._head:
            print("Not empty.")
            return False
        else:
            print("Empty list.")
            return True
    
    @property
    def length(self):
        count=0
        cur=self._head
        while cur:
            count+=1
            cur=cur.next
        return count
        
    def print(self):
        cur=self._head
        if not cur:
            print("Empty lit.")
        else:
            while cur:
                print(cur.val)
                cur=cur.next
            print(cur.val)
    
    def insert(self,index,new_val):
        new_node=Node(new_val)
        cur=self._head
        if not cur:
            print("Empty list.")
            self.add(new_val)
        elif index>self.length or index<0:
            print("Wrong position.")
            return
        else:
            count=0
            while cur.next:
                count+=1
                if(count==index):
                    new_node.next=cur.next
                    cur.next=new_node
                    return

    def delete(self,target_val):
        cur=self._head
        if not cur:
            print("Empty list.")
            return
        else:
            while cur.next:
                pre=cur
                cur=cur.next
                if cur.val==target_val:
                    pre.next=cur.next
    
    def search(self,target_val):
        cur=self._head
        if not cur:
            print("Empty list.")
            return

mylist=SingleLinkList()
print(mylist._head)
node1=Node(1)
node2=Node(2)
node3=Node(3)
mylist._head=node1
node1.next=node2
node2.next=node3

print(mylist._head.next.val)

print(mylist.length)