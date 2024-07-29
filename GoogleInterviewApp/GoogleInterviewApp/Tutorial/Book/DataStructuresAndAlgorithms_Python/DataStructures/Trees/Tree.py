class Tree:
    
    class Position:
        
        def element(self):
            pass
        
        def __eq__(self, __value) -> bool:
            return self == __value
        
        def __ne__(self, __value) -> bool:
            return not (self == __value)
        
    def root(self):
        pass
    
    def parent(self, p):
        pass
    
    def num_children(self, p):
        pass
    
    def children(self):
        pass
    
    def __len__(self):
        pass
    
    def is_root(self, p):
        return self.root() == p

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def is_empty(self):
        return len(self) == 0
    
    def depth(self, p):
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))
        
    def _height(self, p):
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height(c) for c in self.children(p))