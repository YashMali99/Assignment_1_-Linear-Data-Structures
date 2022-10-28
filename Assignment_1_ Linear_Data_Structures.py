

# Q.1) Write a program to find all pairs of an integer array whose sum is equal to a given number?

def printPairs(arr, n, sum):
 
    
 
    
    for i in range(0, n ):
        for j in range(i + 1, n ):
            if (arr[i] + arr[j] == sum):
                print("(", arr[i],
                      ", ", arr[j],
                      ")", sep = "")
 
 

arr = [1, 5, 7, -1, 5]
n = len(arr)
sum = 6
printPairs(arr, n, sum)

# Q.2) Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.
 

def reverseList(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1
 
A = [1, 2, 3, 4, 5, 6]
print(A)
reverseList(A, 0, 5)
print("Reversed list is")
print(A)







# # Q.3) Write a program to check if two strings are a rotation of each other?

str1 = "abcde";  
str2 = "deabc";  
   
if(len(str1) != len(str2)):  
    print("Second string is not a rotation of first string");  
else:  
    try:  
         
        str1 = str1 + str1;  
          
        
        if(str1.index(str2)):  
            print("Second string is a rotation of first string");  
    except ValueError:  
            print("Second string is not a rotation of first string");  

# Q.4) Write a program to print the first non-repeated character from a string?
# 
 
string = "Yash Bhaskar Mali"
index = -1
fnc = ""
for i in string:
    if string.count(i) == 1:
        fnc += i
        break
    else:
        index += 1
if index == 1:
    print("Either all characters are repeating or string is empty")
else:
    print("First non-repeating character is", fnc)
 
# Q.5) Read about the Tower of Hanoi algorithm. Write a program to implement it.

 
 
def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n == 0:
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)
 
 

N = 3
 

TowerOfHanoi(N, 'A', 'C', 'B')

# Q.6) Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.

 
def isOperator(x):
 
    if x == "+":
        return True
 
    if x == "-":
        return True
 
    if x == "/":
        return True
 
    if x == "*":
        return True
 
    return False
 

 
 
def postToPre(post_exp):
 
    s = []
 
    
    length = len(post_exp)
 
    
    for i in range(length):
 
        
        if (isOperator(post_exp[i])):
 
            
            op1 = s[-1]
            s.pop()
            op2 = s[-1]
            s.pop()
 
            
            temp = post_exp[i] + op2 + op1

            
            s.append(temp)
 
        
        else:
 
            
            s.append(post_exp[i])
 
    
    ans = ""
    for i in s:
        ans += i
    return ans
 
 

if __name__ == "__main__":
 
    post_exp = "AB+CD-"
     
    
    print("Prefix : ", postToPre(post_exp))

# Q.7) Write a program to convert prefix expression to infix expression.

def prefixToInfix(prefix):
    stack = []
     
    
    i = len(prefix) - 1
    while i >= 0:
        if not isOperator(prefix[i]):
             
            
            stack.append(prefix[i])
            i -= 1
        else:
           
        
            str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
            stack.append(str)
            i -= 1
     
    return stack.pop()
 
def isOperator(c):
    if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
        return True
    else:
        return False
 

if __name__=="__main__":
    str = "*-A/BC-/AKL"
    print(prefixToInfix(str))



# Q.8) Write a program to check if all the brackets are closed in a given code snippet.


 
 
def areBracketsBalanced(expr):
    stack = []
 
    
    for char in expr:
        if char in ["(", "{", "["]:
 
            stack.append(char)
        else:
 
        
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False
 
    
    if stack:
        return False
    return True
 
 

if __name__ == "__main__":
    expr = "{()}[]"
 
    
    if areBracketsBalanced(expr):
        print("Closed")
    else:
        print("Not closed")


# Q.9) Write a program to reverse a stack.

class Stack:
    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return self.items == []
 
    def push(self, data):
        self.items.append(data)
 
    def pop(self):
        return self.items.pop()
 
    def display(self):
        for data in reversed(self.items):
            print(data)
 
def insert_at_bottom(s, data):
    if s.is_empty():
        s.push(data)
    else:
        popped = s.pop()
        insert_at_bottom(s, data)
        s.push(popped)
 
 
def reverse_stack(s):
    if not s.is_empty():
        popped = s.pop()
        reverse_stack(s)
        insert_at_bottom(s, popped)
 
 
s = Stack()
data_list = input('Please enter the elements to push: ').split()
for data in data_list:
    s.push(int(data))
 
print('The stack:')
s.display()
reverse_stack(s)
print('After reversing:')
s.display()

# # Q.10) Write a program to find the smallest number using a stack.

class MinStack(object):
   min=float('inf')
   def __init__(self):
      self.min=float('inf')
      self.stack = []
   def push(self, x):
      if x<=self.min:
         self.stack.append(self.min)
         self.min = x
      self.stack.append(x)
   def pop(self):
      t = self.stack[-1]
      self.stack.pop()
      if self.min == t:
         self.min = self.stack[-1]
         self.stack.pop()
   def top(self):
      return self.stack[-1]
   def getMin(self):
      return self.min
m = MinStack()
m.push(-2)
m.push(0)
m.push(-3)
print(m.getMin())
m.pop()
print(m.top())
print(m.getMin())
