#question 1
print("\nquestion 1")
a = float(input('Enter the first number: '))
b = float(input('Enter the second number: '))
c = float(input('Enter the third number: '))
numAverage = (a+b+c)/3
print('The Average of the numbers entered is: %0.5f' %numAverage)


#question 2
print("\nquestion 2")
grossIncome = float(input('What is your Gross Income(to the nearest penny): '))
dependentsNum = int(input('What are the total number of dependents: '))
taxOnIncome = (grossIncome - 10000 - (3000 * dependentsNum))*0.20
print('The income tax to be paid by you is: ', taxOnIncome)


#question 3
print("\nquestion 3")
studentInfo = []
print('Hello Student!')
studentInfo.append(int(input('Enter your SID: ')))
studentInfo.append(input('Enter your Name: '))
studentInfo.append(input('Enter your Gender(F,M,U(For Unknown)): '))
studentInfo.append(input('Enter the Course Name: '))
studentInfo.append(float(input('Enter your CGPA: ')))
print(studentInfo)


#question 4 (assuming input is of the form....  1 2 3 4 5  )
print("\nquestion 4")
studentMarks = [float(x) for x in input('Enter the marks of all the students: ').split()]
print(sorted(studentMarks))


#question 5
    #question 5a
print("\nquestion 5a")
colors = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
del colors[3]
print(colors)

    #question 5b
print("\nquestion 5b")
colors = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
colors[3:5] = ['Purple']
print(colors)
