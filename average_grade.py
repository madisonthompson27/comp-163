'''
Madison Thompson
09/03/2022
COMP 163-001
This program's purpose is to use user inputs, converted to floats, to find numeric grades and index a list to assign the numeric grades letter grades.
It will output the user's numeric and letter grades, based on conditional elif statements.
'''
from asyncio import constants
gradeOne = 0
gradeTwo = 0
gradeThree = 0
gradeFour = 0
gradeFive = 0
averageGrade = 0
gradeAssignment = 0
constants = 5
#initializing reference variables
print('The following program uses your numeric quiz grades for five quizzes to calculate your total grade in a class.\nThe grading scale used is that of COMP 163.')
gradeOne = float(input('What is your first quiz grade?\n'))
gradeTwo = float(input('What is your second quiz grade?\n'))
gradeThree = float(input('What is your third quiz grade?\n'))
gradeFour = float(input('What is your fourth quiz grade?\n'))
gradeFive = float(input('What is your fifth quize grade?\n'))
averageGrade = (gradeOne + gradeTwo + gradeThree + gradeFour + gradeFive) / constants
gradeAssignment = ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'F'] #list values will be indexed in elif statements
#finding the average grade by accepting user inputs for each quiz. The list for gradeAssignment helps with organization and each prompt helps to make sure no repeats are used.
if 94 <= averageGrade <= 110: #110 allows for grades with extra credit 
    print(f'Your numeric grade is {averageGrade:.2f} and your letter grade is an {gradeAssignment[0]}.')
elif 90 <= averageGrade <= 93:
    print(f'Your numeric grade is {averageGrade:.2f} and your letter grade is an {gradeAssignment[1]}.')
elif 87 <= averageGrade <= 89:
    print(f'Your numeric grade is {averageGrade:.2f} and your letter grade is a {gradeAssignment[2]}.')
elif 84 <= averageGrade <= 86:
    print(f'Your numeric grade is {averageGrade:.2f} and your letter grade is a {gradeAssignment[3]}.')
elif 80 <= averageGrade <= 83:
    print(f'Your numeric grade is {averageGrade:.2f} and your letter grade is a {gradeAssignment[4]}.')
elif 77 <= averageGrade <= 79:
    print(f'Your numeric grade is {averageGrade:.2f} and your letter grade is a {gradeAssignment[5]}.')
elif 74 <= averageGrade <= 76:
    print(f'Your numeric grade is {averageGrade:.2f} and your letter grade is a {gradeAssignment[6]}.')
elif 70 <= averageGrade <= 73:
    print(f'Your numeric grade is {averageGrade:.2f} and your letter grade is a {gradeAssignment[7]}.')
elif 67 <= averageGrade <= 69:
    print(f'Your numeric grade is {averageGrade:.2f} and your letter grade is a {gradeAssignment[8]}.')
elif 64 <= averageGrade <= 66:
    print(f'Your numeric grade is {averageGrade:.2f} and your letter grade is a {gradeAssignment[9]}.')
elif 0 <= averageGrade <= 63:
    print(f'Your numeric grade is {averageGrade:.2f} and your letter grade is a {gradeAssignment[10]}.')
#referencing list variables eases the assignment process. the elif statements allow each numeric grade, including over 100, a letter-grade assignment.