import random
from Function import find_name
from Function import find_score
from Function import find_subject
from Function import find_grade
from Function import find_activity
from Function import find_activity2
from Function import find_activity3
from Function import find_activity4
from Function import find_activity5
from Function import find_activity6


print("Welcome STUDENTS!!!\n")

count = 1
LOCKOUT = 3
while count <= LOCKOUT:
    user = input("Are you a returning student or a new user?\n")
    if user == 'new user' or user == 'new student':
        print('\nWelcome new student:')
        firstName = input('What is your first name?')
        lastName = input('What is your last name?')
        middleInitial = input('What is your middle initial?')
        name = (firstName," ", lastName," ", middleInitial)
        name = "".join(name)
        print('\nWelcome',name)
        score = find_score(user)
        print('You have',score,'points.')
        break
    elif user == 'returning student' or user == 'returning user':
        print('\nWelcome returning student:')
        iD = int(input('What is your id number?(Enter a # between 0 and 1000)'))   
        name = find_name(iD)
        print('\nWelcome back',name)
        score = find_score(user)
        print('You have',score,'points.')
        break
    else:
        print('\nPlease indicate if you are a new user or returning student.')
        print('You have', LOCKOUT - count,'attempts left before you get locked out.')
        count += 1
        if count == 0:
            exit()

Level = (input('What Grade are you in?'))
Level = int(Level)
grade = find_grade(Level)
print(grade,'\n')

print('Choose one of the following subjects:')
print('Math')
Class = input('What subject would you like to work on today?')
Class = Class.lower()
lesson = find_subject(Class)
print('You have decided to practice',lesson,'\n')

if lesson == 'math':
    print('What Math topic do you want to review?')
    print('Addition')
    print('Subtraction')
    print('Multiplication')
    print('Division')
    Set = input('What is your choice?')
    Set = Set.lower()
    problem = find_activity(Set)
    print(problem,'\n')
    
    if Set == 'addition':
        obstacle = 1
        while Set == 'addition':
            num1 = random.randint(1,50)
            num2 = random.randint(1,50)
            equation = num1 + num2
            print('Problem',obstacle,)
            print(f'{num1} + {num2} = ?')
            answer = input('What is the correct answer?(type exit to end practice)')
            if answer == 'exit':
                break
            answer = int(answer)
            if answer == equation:
                print('You got the right answer!')
                score += 100
                print('Score', score)
                obstacle += 1
            else:
                print('You got the wrong answer.') 
                score -= 100
                print('Score', score)
                obstacle += 1
    if Set == 'subtraction':
        obstacle = 1
        while Set == 'subtraction':
            num1 = random.randint(1,50)
            num2 = random.randint(1,50)
            equation = num1 - num2
            print('Problem',obstacle,)
            print(f'{num1} - {num2} = ?')
            answer = input('What is the correct answer?(type exit to end practice)')
            if answer == 'exit':
                break
                answer = int(answer)
            if answer == equation:
                print('You got the right answer!')
                score += 100
                print('Score', score)
                obstacle += 1
            else:
                print('You got the wrong answer.') 
                score -= 100
                print('Score', score)
                obstacle += 1
    if Set == 'multiplication':
        obstacle = 1
        while Set == 'multiplication':
            num1 = random.randint(1,50)
            num2 = random.randint(1,50)
            equation = num1 * num2
            print('Problem',obstacle,)
            print(f'{num1} x {num2} = ?')
            answer = input('What is the correct answer?(type exit to end practice)')
            if answer == 'exit':
                break
                answer = int(answer)
            if answer == equation:
                print('You got the right answer!')
                score += 100
                print('Score', score)
                obstacle += 1
            else:
                print('You got the wrong answer.') 
                score -= 100
                print('Score', score)
                obstacle += 1
    if Set == 'division':
        obstacle = 1
        while Set == 'division':
            num1 = random.randint(1,100)
            num2 = random.randint(1,10)
            equation = round((num1 / num2),2)
            print('Problem',obstacle,)
            print(f'{num1} / {num2} = ?')
            answer = input('What is the correct answer?(type exit to end practice)')
            if answer == 'exit':
                break
                answer = int(answer)
            if answer == equation:
                print('You got the right answer!')
                score += 100
                print('Score', score)
                obstacle += 1
            else:
                print('You got the wrong answer.') 
                score -= 100
                print('Score', score)
                obstacle += 1

print('Thank you for practicing Math today!')

