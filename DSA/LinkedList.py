class ListNode:
    #Init
    def __init__(self, data):
        self.data = data
        self.nextNode = None
        
    #Set Data for the node
    def setData(self, data):
        self.data = data
        
    #set next node
    def setNextNode(self, node):
        self.nextNode = node
        
    #Get node data
    def getData(self):
        return self.data
    
    #Get next node
    def getNextNode(self):
        return self.nextNode
    

class LinkedList:
    #init
    def __init__(self):
        self.headNode = None

    #add node to a position
    def insert(self, position, data):
        listNode = ListNode(data)
        if self.headNode == None:
            self.headNode = listNode
            return True
        if position < 0 or position > self.getCount() - 1:
            return False
        if position == 0:
            listNode.setNextNode(self.headNode)
            self.headNode = listNode
        else:
            previousNode = findNode(position-1)
            currentNode = previousNode.getNextNode()
            previousNode.setNextNode(listNode)
            listNode.setNextNode(currentNode)
        return True

    #add Node
    def add(self, data):
        listNode = ListNode(data)
        if self.headNode == None:
            self.headNode = listNode
        else:
            node = self.headNode
            while node != None:
                lastNode = node
                node = node.getNextNode()
            lastNode.setNextNode(listNode)
            listNode.setNextNode(None)

    #remove node in the position
    def remove(self, position):
        if position < 0 or position > self.getCount() - 1:
            return None
        if position == 0:
            returnNode = self.headNode
            nextNode = self.headNode.getNextNode()
            self.headNode = nextNode
            return returnNode.getData()
        else:
            previousNode = findNode(position-1)
            currentNode = previousNode.getNextNode()
            nextNode = currentNode.getNextNode()
            previousNode.setNextNode(nextNode)
            return currentNode.getData()

    #Get the count of nodes
    def getCount(self):
        node = self.headNode
        count = 0
        while node.getNextNode != None:
            count = count + 1
            node = node.getNextNode()
        return count

    #Find node in a position
    def findNode(self, position):
        node = headerNode
        if position < 0 or position > getCount() - 1:
            return None
        else:
            count = 0
            while count <= position:
                node = node.getNextNode()
        return node
    
class Stack:
    def __init__(self):
        self.linkedList = LinkedList()
        
    def push(self, data):
          self.linkedList.insert(0, data)

    def pop(self):
        return self.linkedList.remove(0)

    def count(self):
        return self.linkedList.getCount()
    
