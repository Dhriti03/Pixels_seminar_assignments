# Assignment



## A few basic exercises
### Variable Assignment
* Try a program to display your name using a variable
* Try changing that variable in code itself to something else
* Try assiging one variable to other and changing one's value



```python
a= "Dhriti"
b= "Mabian"

# Write code to print the variable a 
print(a)
############

# Write Code to Change variable a into 30
a=30
print(a)
############

# Write Code to assign variable a the value of b
a=b
print(a)
############

```

    Dhriti
    30
    Mabian


### Multiple Assignment

* Try Reversing the assignements i.e. new a should be 3, b should be 2 and c should be 1


```python
a,b,c = 1,2,3

## write a single line code to reverse a,b,c using multiple assignment
a,b,c = 3,2,1
######
print(a,b,c)
```

    3 2 1


### String

* Try reversing string in one line as compared to conventional loops



```python
string = "this is a test!"

## Write Code to reverse string in one line
reversed=''.join(reversed(string))
##

print(reversed)
```

    !tset a si siht


# Operators

You are provided with a list of Clubs in VJTI:
clubs = ['SRA' , 'Aero' , 'Racing' , 'DSC' , 'COC']
And a list of clubs you are a member of:
membership= ['SRA' , 'DSC']

You have to perform the following tasks:

1.   Create a boolean list respective to the clubs you are a member of without using the '==' operator:
Expected output: [true,false,false,true,false] HINT: use the membership operator

2.   Convert the boolean list into a list of binary one or zero without using the operator '=='. Expected output: [1,0,0,1,0]
HINT: Check out identity operator

You are provided with the following:
expression = 4_6_9_3_23_19
Using the operators: +,-,*, /, % in places of the _ make an expression that reads the value: 25.0.


```python
clubs = ['SRA', 'Aero', 'Racing', 'DSC', 'COC']

membership = ['SRA', 'DSC']

Boolean = [ ]

for i in range(len(clubs)):
    if clubs[i] in membership:
        Boolean.append(True)
    else:
        Boolean.append(False)

print("The Boolean List is:", Boolean)

Binary = [ ]

for i in range(len(Boolean)):
    if Boolean[i] is True:
        Binary.append(1)
    else:
        Binary.append(0)

print("The Binary List is:", Binary)



    
 


```

    The Boolean List is: [True, False, False, True, False]
    The Binary List is: [1, 0, 0, 1, 0]



```python
(expression) = (4)+(6)-(9)*(3)+(23)+(19)
#write your code here
print(expression)
```

# Control Statements

Complete the for loop such that whenever there is an prime number it prints the number plus "I was a prime" in the same line, otherwise it prints nothing.  


Using the looping statement and the control statements  




```python
  for num in range(0, 100):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
    else:
            print(num, end = ", ")
            print("I was prime")
            
```

# Lists

Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. Go to the editor  
**Sample Input** :['abc', 'xyz', 'aba', '1221']   
**Sample Output** :2  
**Explanation** :'aba' and '1221' have length greater than 2 and also has matching first and last character.   


```python
list1 = ['abc','xyz','aba','1221']
# Write your code here
List = ['abc', 'xyz', 'aba', '1221']

c = 0

for i in range(len(List)):
    if len(List[i]) >= 2:
        Str = List[i]
        end = len(Str) - 1
        if Str[i] == Str[end]:
            c += 1

print(c)
```

Write a Python program to print the numbers of a specified list after removing even numbers from it.  
**Hint** : Use List Comprehension


```python
# Write your code here
num = [93,7, 485, 1254, 43, 88, 76]
num = [x for x in num if x%2!=0]
print(num)
```

    [93, 7, 485, 43]


# Dictionaries

Delete set of keys (keysToRemove) from a dictionary and display the resultant dictionary  
**Given** :

**Expected Output**:

{'city': 'New york', 'age': 25}


```python

sampleDict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

del sampleDict['name']

del sampleDict['salary']

print(sampleDict)
```

    {'age': 25, 'city': 'New york'}


Write a program in Python to read the admission number, name of student and his/her stream of 10 students and create a dictionary from this information. print the dictionary 


```python
# Write your code here 
List = []

for i in range(11):
    Dict = {}
    
    num =  input("\nEnter admission number of the student: ").split()
    name = input("Enter name of the student: ").split()
    stream = input("Enter stream of the student: ").split()
    Dict["admission_number"] = num
    Dict["name"] = name
    Dict["stream"] = stream
    List.append(Dict)

print(Dict)
     



```

## Sets and Tuples

Check if two sets have any elements in common. If yes, display the common elements.

set1 = {10, 20, 30, 40, 50}

set2 = {60, 70, 80, 90, 10}


**Expected output:**

Two sets have items in common

{10}


```python


# Write your code here to get common elements among them
set1 = {10, 20, 30, 40, 50}

set2 = {60, 70, 80, 90, 10}

set3 = set()

List = list(set1)

for i in range(len(List)):
     if List[i] in set2:
         set3.add(List[i])

print(set3)
```

    {10}


Write a Python program to replace last value of tuples in a list.

**Sample list:** [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

**Expected Output:** [(10, 20, 100), (40, 50, 100), (70, 80, 100)]


```python
list1 = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

# Write your code here to replace last value of tuples in the list
TupList = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

NewList = []

for subTup in TupList:
    subList = list(subTup)
    subList[2] = 100
    subTup = tuple(subList)
    NewList.append(subTup)

print(NewList)
```

    [(10, 20, 100), (40, 50, 100), (70, 80, 100)]


## Functions

1) Write a function called ```showNumbers``` that takes a parameter called limit. It should print all the numbers between 0 and limit with a label to identify the even and odd numbers. For example, if the limit is 3, it should print:
* 0 EVEN
* 1 ODD
* 2 EVEN
* 3 ODD



```python
# Write Your code here
def showNumbers(limit):
    for i in range(0, limit+1):
        if i % 2 == 0:
            print(i, "EVEN")
        else:
            print(i, "ODD")
    return "End"

print(showNumbers(10))
```

    0 EVEN
    1 ODD
    2 EVEN
    3 ODD
    4 EVEN
    5 ODD
    6 EVEN
    7 ODD
    8 EVEN
    9 ODD
    10 EVEN
    End


2) Write a function that takes limit(integer) as a paramter and prints all the prime numbers between 0 and limit.





```python
# Write your code here
def prime(limit):
    for num in range(0, limit + 1):
       if num > 1:
           for i in range(2, num):
               if (num % i) == 0:
                   break
           else:
               print(num)
prime(20) 
```

    2
    3
    5
    7
    11
    13
    17
    19


# Classes and Objects

Write a Python Program to create a class named **Student**. 
- It should be initialised with attributes like **name, age, rollno, favourite subject**(a single subject).

- Write a class method **getDetails()** which prints the name, age and rollno of the object in the below format.
 
  * **Expected Output Format**
> Name   : <em>name</em></br>
> Age    : <em>age</em></br>
> RollNo : <em>rollno</em></br>

  * **Expected Example Output**
> Name : Gautam</br>
Age : 20</br>
RollNo : 68

- Now, there is a list **fav_list** such that it contains a list of subjects which are favourite to the Principal.

  ``` python
    fav_list = ["EG","Mechanics","Chemistry"]
  ``` 
- You have to write a class Method **isFav()** which returns a boolean value i.e either <em>**true**</em> if any of the favourite subject of the principal matches with that of the student. Think of some suitable logic here.

- Create 2 objects of class **Student** with attributes of your choice taken via user input.

- Call Both the methods for both the objects. **Note** - Print the result of the **isFav()** method.

- **Bonus Task** - Write the body of **isFav()** method in just one line.


```python
# Write your code here 
class Student:

    def __init__(self, name, age, rollno, fav):
        self.name = name
        self.age = age
        self.rollno = rollno
        self.fav = fav

    def getDetails(self):
        print("Name :", self.name, end = "  ")
        print("Age :", self.age, end = "  ")
        print("RollNo:", self.rollno)

    def isFav(self):
        print(True if self.fav in ["EG","Mechanics","Chemistry"]else False)

a = Student("Student1", 18, 1, "Mechanics")
a.getDetails()
a.isFav()

print()

b = Student("Student2", 19, 2, "Python")
b.getDetails()
b.isFav()



```

    Name : Student1  Age : 18  RollNo: 1
    True
    
    Name : Student2  Age : 19  RollNo: 2
    False



```python

```
