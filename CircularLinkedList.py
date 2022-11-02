class Node:    
  def __init__(self,data):    
    self.data = data;    
    self.next = None;    
     
    
class CircularLinkedlist:    
  #Declaring head and tail pointer as null.    
  def __init__(self,cap):    
    self.head = Node(None)
    self.tail = Node(None) 
    self.head.next = self.tail   
    self.tail.next = self.head
    self.size = 0
    self.capacity=cap

  def enqueue(self,data): 
    if self.size<self.capacity:   
      newNode = Node(data);    
      #Checks if the list is empty.    
      if self.head.data is None:    
      #If list is empty, both head and tail would point to new node.    
          self.head = newNode   
          self.tail = newNode    
          newNode.next = self.head    
      else:    
          #tail will point to new node.    
          self.tail.next = newNode;    
          #New node will become new tail.    
          self.tail = newNode;    
           
          self.tail.next = self.head
    else: 
      print("Antrian Penuh")

  def dequeue(self):
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                hapus = self.head
                self.head = self.head.next
                hapus._next = None
                self.head.prev = None
                del hapus
                self.size = self.size - 1
        # else:
        #     print("Data Kosong!!")
       
  def display(self):    
      current = self.head    
      if self.head is None:    
        print("kosong");       
      else:    
          print("Yang ada pada antrian adalah: ");    
          #Prints each node by incrementing pointer.    
          print(current.data)  
          while(current.next != self.head):    
              current = current.next    
              print(current.data) 
antrian = CircularLinkedlist(5);    
antrian.enqueue(14)
antrian.enqueue(22)
antrian.enqueue(13)
antrian.enqueue(-6)
antrian.display()         
print("Data yang dihapus adalah= ", antrian.dequeue())
print("Data yang dihapus adalah= ", antrian.dequeue())
antrian.display()
antrian.enqueue(9)
antrian.enqueue(20)
antrian.enqueue(5)
antrian.display()   