word = 'Python'
print(word[2])      #t
print(word[-1])     #n
print(word[0:2])    #Py
print(len(word))

squares = [1, 4, 9, 16, 25]
print(squares)
print(squares[0])       #1
print(squares[-1])      #25
print(squares[0:2])     #1,4
print(squares[:])       #[1, 4, 9, 16, 25]

squares.append(36)
print(squares)

words = ['cat', 'window', 'defenestrate']
for word in words:
    print(word, len(word))

#Create a sample collection
collection = { 'first': 1, 'second': 2 }
for item, cnum in collection.items():
    print(item, cnum)

print(list(range(0,10)))

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 200:
            return "OK"
        case 500:
            return "Internal Server error"
        case 401:
            return "Unauthorized"
        case 403 | 404:
            return "Not allowed"
        case _:
            return "Default"
        
print(http_error(400))      #Bad request

from enum import Enum
class Color(Enum):
    RED = 'red'
    BLUE = 'blue'
    GREEN = 'green'

redColor = Color('red')
blueColor = Color('blue')
greenColor = Color('green')

def getColor(color):
    match color:
        case Color.RED:
            print("This is red color")
        case Color.BLUE:
            print("This is blue color")
        case Color.GREEN:
            print("This is green color")

print(getColor('red'))
print(getColor('green'))
print(getColor('blue'))

