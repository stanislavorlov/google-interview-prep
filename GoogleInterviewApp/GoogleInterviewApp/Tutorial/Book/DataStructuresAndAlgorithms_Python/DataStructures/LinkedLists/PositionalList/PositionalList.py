from tkinter import SEL

from Tutorial.Book.DataStructuresAndAlgorithms_Python.DataStructures.LinkedLists._DoublyLinkedBase import _DoublyLinkedBase

class PositionalList(_DoublyLinkedBase):

    #-------------------------- nested Position class --------------------------
    class Position:
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element
        
        def __eq__(self, other) -> bool:
            return type(other) is type(self) and other._node is self._node
        
        def __ne__(self, other) -> bool:
            return not (self == other)
        
    #------------------------------- utility method -------------------------------
    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        
        if p._node._next is None:
            raise ValueError('p is no longer valid')
        
        return p._node
    
    def _make_position(self, node):
        # if node is sentinel
        if node is self._header or node is self._trailer:
            return None
        else:
            # return position
            return self.Position(self, node)
        
    #------------------------------- accessors -------------------------------
    def first(self):
        return self._make_position(self._header._next)
    
    def last(self):
        return self._make_position(self._trailer._prev)
    
    def before(self, p):
        node = self._validate(p)
        return self._make_position(node._prev)
    
    def after(self, p):
        node = self._validate(p)
        return self._make_position(node._next)
    
    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    #------------------------------- mutators -------------------------------
    def _insert_between(self, e, predecessor, successor):
        """Add element between existing nodes and return new Position."""
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)
    
    def add_first(self, e):
        """Insert element e at the front of the list and return new Position."""
        return self._insert_between(e, self._header, self._header._next)
    
    def add_last(self, e):
        """Insert element e at the back of the list and return new Position."""
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        """Insert element e into list before Position p and return new Position."""
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        """Insert element e into list after Position p and return new Position."""
        original = self._validate(p)
        return self._insert_between(e, original, original._next)
    
    def delete(self, p):
        """Remove and return the element at Position p."""
        original = self._validate(p)
        return self._delete_node(original)   # inherited method returns element

    def replace(self, p, e):
        """Replace the element at Position p with e.
        Return the element formerly at Position p.
        """
        original = self._validate(p)
        old_value = original._element        # temporarily store old element
        original._element = e                # replace with new element
        return old_value                    # return the old element value
    
    def print(self):
        for n in self:
            print(n)

    def insertion_sort(self):
        if len(self) > 1:
            marker = self.first()
            while marker != self.last():
                pivot = self.after(marker)
                value = pivot.element()
                if value > marker.element():
                    marker = pivot
                else:
                    walk = marker
                    while walk != self.first() and self.before(walk).element() > value:
                        walk = self.before(walk)
                    self.delete(pivot)
                    self.add_before(walk, value)

pList = PositionalList()
p1 = pList.add_first(5)
p5 = pList.add_last(1)
p2 = pList.add_after(p1,4)
p31 = pList.add_before(p5,3)
p4 = pList.add_before(p5,2)
p32 = pList.add_before(p4,3)
pList.print()
print(f'3 = 3: {p31.__eq__(p32)}')
pList.insertion_sort()
pList.print()