class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def __iter__(self):
        node=self.head
        while node:
            yield node
            if node.next==self.head:
                break
            node=node.next
    
    def createCSLL(self,nodeValue):
        node=Node(nodeValue)
        node.next=node
        self.head=node
        self.tail=node
        return "The CSLL has been created"

    def insertCSLL(self,value,location):
        if self.head is None:
            return "The head refernce is None"
        else:
            newNode=Node(value)
            if location==0:
                newNode.next=self.head
                self.head=newNode
                self.tail.next=newNode

            elif location==-1:
                newNode.next=self.tail.next
                self.tail.next=newNode
                self.tail=newNode
            else:
                tempNode=self.head
                index=0
                while index<location-1:
                    tempNode=tempNode.next
                    index+=1
                nextNode=tempNode.next
                tempNode.next=newNode
                newNode.next=nextNode
            return "The node has been successfully inserted"



csll=CircularSinglyLinkedList()
print(csll.createCSLL(1))
csll.insertCSLL(0,0)
csll.insertCSLL(2,1)
csll.insertCSLL(3,1)
csll.insertCSLL(2,2)

print([node.value for node in csll])




