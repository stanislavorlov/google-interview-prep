set1 = set()
set2 = {'a','b','c'}

print(set1)
print(set2)

dict1 = { 'ga' : 'Irish' , 'de' : 'German' }    # dict
dict2 = [('ga', 'Irish'), ('de', 'German')]     # list

print(dict1, dict1.keys())
print(dict2)

class CreditCard:
    def __init__(self, customer, bank, acnt, limit):
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        return self._customer
    
    def get_bank(self):
        return self._bank
    
    def get_account(self):
        return self._account
    
    def get_limit(self):
        return self._limit
    
    def get_balance(self):
        return self._balance
    
    def charge(self, price):
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True
        
    def make_payment(self, amount):
        self._balance -= amount

cc = CreditCard('Stan Orlov', 'City Bank', '1234 5678 9011 1234', 1200)
print(cc.get_customer())
print(cc.get_bank())
print(cc.get_balance())
print(cc.get_account())
print(cc.get_limit())
cc.charge(1000)
print(cc.get_balance())
cc.make_payment(54.00)
print(cc.get_balance())

# Operator Overloads

class Vector:

    def __init__(self, d):
        self._coords = [0] * d

    def __len__(self):
        return len(self._coords)
    
    def __getitem__(self, j):
        return self._coords[j]

    def __setitem__(self, j, val):
        self._coords[j] = val

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    
    def __eq__(self, other) -> bool:
        return self._coords == other._coords
    
    def __ne__(self, other) -> bool:
        return not self == other
    
    def __str__(self) -> str:
        return '<' + str(self._coords)[1:-1] + '>'
    
vector1 = Vector(10)
vector1[0] = 5
vector1[2] = 4
vector1[6] = 9
vector1[9] = 55

print(len(vector1))
print(vector1[2])
print(vector1)

vector2 = Vector(10)
vector2[0] = 5
vector2[2] = 4
vector2[6] = 9
vector2[9] = 556

print(vector1 == vector2)

## Iterator

class SequenceIterator:

    def __init__(self, sequence):
        self._seq = sequence
        self._k = -1

    def __next__(self):
        self._k += 1
        if self._k < len(self._seq):
            return self._seq[self._k]
        else:
            raise StopIteration()
        
    def __iter__(self):
        return self
    
    def __len__(self):
        return len(self._seq)
    
sequnce = SequenceIterator([1,2,3,4,5,6,7])
for i in sequnce:
    print(i)

# Inheritance

class PredatoryPaymentCard(CreditCard):

    def __init__(self, customer, bank, acnt, limit, apr):
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr

    def charge(self, price):
        success = super().charge(price)
        if not success:
            self._balance += 5

        return success
    
    def process_month(self):
        if self._balance > 0:
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor

# Abstract Class

from abc import ABCMeta, abstractmethod

class Sequence(metaclass=ABCMeta):

    @abstractmethod
    def __len__(self):
        """Return the length of the sequence"""

    @abstractmethod
    def __getitem__(self, j):
        """Return the element at index j of the sequence"""

    def index(self, val):
        for j in range(len(self)):
            if self[j] == val:
                return j
        
        raise ValueError('value not in sequence')
    
print(list('bird'))                     # ['b', 'i', 'r', 'd']
print(''.join(['b','i','r','d']))       # bird

# two-dimensional list
data = [ [22, 18, 709, 5, 33], [45, 32, 830, 120, 750], [4, 880, 45, 66, 61] ]

print(data)

data1 = [ [0] * 5 for j in range(3)]
print(data1)