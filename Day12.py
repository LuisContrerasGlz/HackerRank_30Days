"""

You are given two classes, Person and Student, where Person is the base class and Student is the derived class. 
Completed code for Person and a declaration for Student are provided for you in the editor. 
Observe that Student inherits all the properties of Person.


Complete the Student class by writing the following:

A Student class constructor, which has 4 parameters:
A string, firstName.
A string, lastName.
An integer, idNumber.
An integer array (or vector) of test scores,scores.

A char calculate() method that calculates a Student object's average and returns the grade character representative of their calculated average

Input format:

The locked stub code in the editor reads the input and calls the Student class constructor with the necessary arguments. 

It also calls the calculate method which takes no arguments.

The first line contains firstName, lastName, and idNumber, separated by a space. 
The second line contains the number of test scores. The third line of space-separated integers describes scores.

Constraints

1 <= length of firstName, lenght of lastName <= 10
length of idNumber = 7
0 <= scrore <= 100

"""


class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    # Declaring the __init__ function and then calling the __init__ function of the Person class using the super() function, and sets the scores of the student to the scores parameter.
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores
    
    # Calculating the average of the scores and returns a grade character based on the average score.
    def calculate(self):
        total = sum(self.scores)
        average = total / len(self.scores)
        
        if average >= 90:
            return 'O'
        elif average >= 80:
            return 'E'
        elif average >= 70:
            return 'A'
        elif average >= 55:
            return 'P'
        elif average >= 40:
            return 'D'
        else:
            return 'T'


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())