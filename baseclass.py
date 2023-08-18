#basetable class
#a linked list where each node represents a table and 
# every table contains an array with all available slots
#slots from 11 am to 2 pm and 7 pm to 10 pm; ie 6 slots

import ctypes

#defining the node ("Tree") which contains the table_id, availability and number of seats

class Table():
    def __init__(self,table_id,no_of_slots = 6):
        self.table_id = table_id
        self.availability = AvailabilityArray().gen_slots(no_of_slots)
        self.no_of_seats=4
        self.next=None

#defining an array which will store a collection of all available slots

class AvailabilityArray():
    def __init__(self):
        self._arr = (2*ctypes.py_object)()
        self._size = 0
        self._capacity = 2

    def __len__(self):
        return self._size

    def __str__(self):
        s=''
        for i in range(self._size):
          s+=str(self._arr[i])
          s+='/'
        return s

    def _resize(self,new_capacity):
        temp_arr = (new_capacity * ctypes.py_object)()
        for i in range(self._size):
            temp_arr[i] = self._arr[i]
        self._arr = temp_arr
        self._capacity = new_capacity

    def __getitem__(self,index):
        if not 0<=index<=self._size:
            raise IndexError("index not valid")
        return self._arr[index]

    def append(self,item):
        if self._size == self._capacity:
            self._resize(2*self._capacity)
        self._arr[self._size] = item
        self._size +=1

    def remove(self, value):
      for k in range(self._size):
        if self._arr[k] == value:             
          for j in range(k, self._size - 1):    
            self._arr[j] = self._arr[j+1]
          self._arr[self._size - 1] = None       
          self._size -= 1                       
          return                             
      raise ValueError('value not found')

    def __iter__(self):
      for i in range(self._size):
        yield self._arr[i]

    def gen_slots(self,no):
      for i in range(no):
        self.append(i+1)
      return self


#defining the main ds of the program

class BaseTableClass():
    def __init__(self):
        self.head = self.tail = Table(None)

    def add_Table(self,table_id):   #to add an extra table
        self.tail.next = Table(table_id)
        self.tail = self.tail.next

    def __str__(self):  #returns a string representation of data stored
        res = ''
        p = self.head
        while p.next is not None:
            res = res + str(p.next.table_id) + ':' + str(p.next.availability) +  ', '
            p = p.next
        return res

    def __iter__(self): #creating an iterator
        p = self.head
        while p.next is not None:
            yield [p.next.table_id, p.next.availability]
            p = p.next

    def book_slot(self,table_id,slot): #to book a slot at given table
        p=self.head
        while p.next is not None:
            if table_id == p.next.table_id and (slot in p.next.availability):
                p.next.availability.remove(slot)
            p=p.next
            
    def cancel_slot(self,table_id,slot): #to cancel a slot at given table 
        p=self.head
        while p.next is not None:
            if table_id == p.next.table_id:
                p.next.availability.append(slot)
            p=p.next
            


BaseTable = BaseTableClass()
BaseTable.add_Table(1)
BaseTable.add_Table(2)
BaseTable.add_Table(3)
BaseTable.add_Table(4)
BaseTable.add_Table(5)
BaseTable.add_Table(6)

