import random

def find_score(user):
    if user == 'new user':
        score = 0
    elif user == 'returning student':
        score = random.randint(1,10000)
    return score    

def find_name(iD):
    if iD > 0 and iD <= 100:
        user = ('John N Stewart')
    elif iD > 100 and iD <= 200:
        user = ('Thomas B Adams')
    elif iD > 200 and iD <= 300:
        user = ('Susan V Sullivan')
    elif iD > 300 and iD <= 400:
        user = ('Martha D Collins')
    elif iD > 400 and iD <= 500:
        user = ('Samuel A Cortez')
    elif iD > 500 and iD <= 600:
        user = ('Marshall C Lahr')
    elif iD > 600 and iD <= 700:
        user = ('Alicia M Edwards')
    elif iD > 700 and iD <= 800:
        user = ('Valentina W Stewarts')
    elif iD > 800 and iD <= 900:
        user = ('Juan O Ricardo')
    elif id > 900 and iD <= 1000:
        user = ('Nadine M Litt')
    return user

def find_subject(Class):
    while True:
        if Class == 'math':
            lesson = ('math')
            break
        elif Class == 'science':
            lesson = ('science')
            break
        elif Class == 'history':
            lesson =('history')
            break
        elif Class == 'english':
            lesson =('english')
            break
        elif Class == 'foreign languages':
            lesson =('new language')
            break
        elif Class == 'computer science':
            lesson = ('computer science')
            break
    return lesson

def find_grade(Level):
    while True:
        if Level > 0 and Level <= 6:
            grade = ('Elementary School')
            break
        elif Level > 6 and Level <= 8:
            grade = ('Middle School')
            break
        elif Level > 8 and Level <= 12:
            grade = ('High School')
            break
    return grade

def find_activity(Set):
    if Set == 'addition':
        Problem = ('You want to practice Addition.')
    elif Set == 'subtraction':
        Problem = ('You want to practice Subtraction.')
    elif Set == 'multiplication':
        Problem = ('You want to practice Multiplication.')
    elif Set == 'division':
        Problem = ('You want to practice Division.')  
    return Problem   

def find_activity2(Set):
    if Set == 'biology':
        Problem = ('You want to practice Biology.')
    elif Set == 'chemistry':
        Problem = ('You want to practice Chemistry.')
    elif Set == 'physics':
        Problem = ('You want to practice Physics.')
    elif Set == 'anatomy':
        Problem = ('You want to practice Anatomy.') 
    return Problem       

def find_activity3(Set):
    if Set == 'reading comprehension':
        Problem = ('You want to practice Reading Comprehension.')
    elif Set == 'writing skills':
        Problem = ('You want to practice Writing Skills.')
    elif Set == 'vocabulary building':
        Problem = ('You want to practice Vocabulary Building.')
    elif Set == 'grammar skills':
        Problem = ('You want to practice Grammar skills.')
    elif Set == 'speaking ability':
        Problem = ('You want to practice Speaking Ability.')
    elif Set == 'figurative language':
        Problem = ('You want to practice Figurative Language.')
    elif Set == 'essays':
        Problem = ('You want to practice Essays')   
    return Problem  

def find_activity4(Set):
    if Set == 'ancient':
        Problem = ('You want to practice Ancient History.')
    elif Set == 'medieval':
        Problem = ('You want to practice Medieval History.')
    elif Set == 'renaissance':
        Problem = ('You want to practice Renaissance and Reform.')
    elif Set == 'early modern':
        Problem = ('You want to practice Early Modern History.')
    elif Set == 'modern':
        Problem = ('You want to practice Modern History.')
    elif Set == 'global':
        Problem = ('You want to practice Global History.')
    elif Set == 'civics':
        Problem = ('You want to practice Civics')   
    return Problem 

def find_activity5(Set):
    if Set == 'spanish':
        Problem = ('You want to practice Spanish.')
    elif Set == 'french':
        Problem = ('You want to practice French.')
    elif Set == 'german':
        Problem = ('You want to practice German.')
    elif Set == 'mandarin':
        Problem = ('You want to practice Mandarin.')
    elif Set == 'japanese':
        Problem = ('You want to practice Japanese.')
    elif Set == 'arabic':
        Problem = ('You want to practice Arabic.')
    elif Set == 'russian':
        Problem = ('You want to practice Russian.')   
    return Problem 

def find_activity6(Set):
    if Set == 'python':
        Problem = ('You want to practice Python.')
    elif Set == 'java':
        Problem = ('You want to practice Java.')
    elif Set == 'c++':
        Problem = ('You want to practice C++.')
    elif Set == 'javascript':
        Problem = ('You want to practice JavaScript.')
    elif Set == 'html':
        Problem = ('You want to practice HTML.')
    elif Set == 'css':
        Problem = ('You want to practice CSS.')
    elif Set == 'matlab':
        Problem = ('You want to practice MATLAB')   
    return Problem 