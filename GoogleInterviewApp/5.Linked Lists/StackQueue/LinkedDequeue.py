from queue import Empty

from _DoublyLinkedBase import _DoublyLinkedBase

class LinkedDequeue(_DoublyLinkedBase):

    def first(self):
        if self.is_empty():
            raise Empty('Dequeue is empty')
        return self._header._next._element
    
    def last(self):
        if self.is_empty():
            raise Empty('Dequeue is empty')
        return self._trailer._prev._element
    
    def insert_first(self, e):
        self._insert_between(e, self._header, self._header._next)

    def insert_last(self, e):
        self._insert_between(e, self._trailer._prev, self._trailer)

    def delete_first(self):
        if self.is_empty():
            raise Empty('Dequeue is empty')

        self._delete_node(self._header._next)

    def delete_last(self):
        if self.is_empty():
            raise Empty('Dequeue is empty')
        
        self._delete_node(self._trailer._prev)

q = LinkedDequeue()
q.insert_first(1)
q.insert_last(5)
print(q.first())
print(q.last())
q.insert_first(2)
q.insert_last(3)
print(q.first())
print(q.last())
q.delete_first()
q.delete_last()
print(q.first())
print(q.last())