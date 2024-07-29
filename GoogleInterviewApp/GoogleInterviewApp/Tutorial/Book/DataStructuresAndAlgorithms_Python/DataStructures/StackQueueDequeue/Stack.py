# Stack
class ArrayStack:

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return len(self._data) == 0
    
    def push(self, e):
        self._data.append(e)

    # return an element at the top of stack
    def top(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        
        return self._data[-1]
    
    def pop(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        
        return self._data.pop()
    
class Stack:

    def __init__(self):
        self._data = [0] * 5
        self._len = 0

    def push(self, val):
        if self._len == len(self._data):
            self._data = self._data + [0] * 5
        
        self._data[self._len] = val
        self._len += 1

    def pop(self):
        if self.is_empty():
            return

        val = self._data[self._len-1]
        self._data[self._len-1] = 0
        self._len -= 1

        return val

    def peek(self):
        if self.is_empty():
            return
        
        return self._data[0]
    
    def is_empty(self):
        return self._len == 0
    
stack = Stack()
for i in range(0, 5):
    stack.push(i)

for i in range(0, 5):
    print(stack.pop())

### Matching parentheses ####

# Parentheses: “(” and “)”
# Braces: “{” and “}”
# Brackets: “[” and “]”

correct1 = "( )(( )){([( )])}"
correct2 = "((( )(( )){([( )])}))"
incorrect1 = ")(( )){([( )])}"
incorrect2 = "({[])}"
incorrect3 = "("

def is_correct(exp):
    stack = []

    lefty = "({["
    righty = ")}]"

    for c in exp:
        if c in lefty:
            stack.append(c)
        elif c in righty:
            if len(stack) < 1:
                return False

            cur = stack.pop()
            if lefty.index(cur) != righty.index(c):
                return False
            
    return len(stack) == 0

print(is_correct(correct1))
print(is_correct(correct2))
print(is_correct(incorrect1))
print(is_correct(incorrect2))
print(is_correct(incorrect3))

html = """<body>
<center>
<h1> The Little Boat </h1>
</center>
<p> The storm tossed the little
boat like a cheap sneaker in an
old washing machine. The three
drunken fishermen were used to
such treatment, of course, but
not the tree salesman, who even as
a stowaway now felt that he
had overpaid for the voyage. </p>
<ol>
<li> Will the salesman die? </li>
<li> What color is the boat? </li>
<li> And what about Naomi? </li>
</ol>
</body>"""

def is_matched_html(raw):
    stack = Stack()
    tag = ""
    for ch in raw:
        if ch == '<':
            tag = ch
        elif ch == '>':
            tag += ch
            if tag[1] == '/':
                opened_tag = stack.pop()
                if opened_tag[1:-1] != tag[2:-1]:
                    return False
            else:
                stack.push(tag)
            tag = ''
        elif tag.startswith('<') and ch.strip():
            tag += ch

    return stack.is_empty()

print(is_matched_html(html))