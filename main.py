<<<<<<< HEAD
from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json
from PyInquirer import Validator, ValidationError
from PyInquirer import style_from_dict, Token, prompt

style = style_from_dict({
    Token.QuestionMark: '#E91E63 bold',
    Token.Selected: '#673AB7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#2196f3 bold',
    Token.Question: '',
})

print("Add your work hours:")

#testing if user inputs are correct
class start_time_validator(Validator):
    def validate(self, document):
        is_good = str(document)
        if not is_good:
            raise ValidationError(
                print("please input in correct format ex. 202107141555"),
                cursor_position=len(document.text) #move the cursor to empty space 
            )


#questions for user to input
questions = [
    {
        'type': 'input',
        'name': 'project_name',
        'message': 'Project name:'
    },
    {
        'type': 'input',
        'name': 'task',
        'message': 'Task:'
    },
    {
        'type': 'input',
        'name': 'start_time',
        'message': 'Start time(format YYYYMMDDHHMM):'
        #'validate': start_time_validator
    },
    {
        'type': 'input',
        'name': 'end_time',
        'message': 'End time(format YYYYMMDDHHMM):'
    },
    {
        'type':'list',
        'name':'continue',
        'message':'Do you want to add more hours?',
        'choices': ["yes","no"]
    }
]

#User inputs to values
answers = prompt(questions)
project_name = answers.get('project_name')
task_explanation = answers.get('task')
start_time_str = answers.get('start_time')
end_time_str = answers.get('end_time')
continue_info = answers.get('continue')

#printing values to user 
print(project_name, task_explanation, start_time_str, end_time_str, continue_info)

task_started_year = start_time_str[:4]
task_started_month = start_time_str[4:6]
task_started_day = start_time_str[6:8]
task_started_hour = start_time_str[8:10]
task_started_minutes = start_time_str[10:]

task_ended_year = end_time_str[:4]
task_ended_month = end_time_str[4:6]
task_ended_day = end_time_str[6:8]
task_ended_hour = end_time_str[8:10]
task_ended_minutes = end_time_str[10:]



""" project_name = ""
=======
#import curses
from datetime import datetime

project_name = ""
>>>>>>> fe6da58553298f1985ca0c5d687e1fca48f9ec7a
task_explanation = ""
task_started_year = 0
task_started_month = 0
task_started_day = 0
task_started_hour = 0
task_started_minutes = 0
task_ended_year = 0
task_ended_month = 0
task_ended_day = 0
task_ended_hour = 0
<<<<<<< HEAD
task_ended_minutes = 0 """
=======
task_ended_minutes = 0



""" #draws the window 
def c_window(stdscr: 'curses._CursesWindow') -> int:
    #import time; time.sleep(2)
    while True:
        project_name = stdscr.getstr(0,0,20)
        #rendering phase

    
    return 0

#starts the program
def main() -> int: 
    return curses.wrapper(c_window)

#ends program
if __name__=='__main__':
    exit(main()) """
>>>>>>> fe6da58553298f1985ca0c5d687e1fca48f9ec7a

#2020, 6, 30, 13, 00

#helppokäyttöliittymä
<<<<<<< HEAD
""" while True:
=======

while True:
>>>>>>> fe6da58553298f1985ca0c5d687e1fca48f9ec7a
    print("Add your worktime for today")
    project_name = input("Which project you worked today on?")
    task_explanation = input("What did you do today?")


    while True:
        start_time_str= input("When did you start today? format: YYYYMMDDHHMM")
        if len(start_time_str) != 12:
            print("You did not put the starting time in correct format. Put it as YYYYMMDDHHMM ex. 202112241805")
        else:
            break

    while True:
        end_time_str= input("When did you end today? format: YYYYMMDDHHMM")
        if len(end_time_str) != 12:
            print("You did not put the starting time in correct format. Put it as YYYYMMDDHHMM ex. 202112241805")
        else: 
            break
    

<<<<<<< HEAD
    task_started_year = start_time_str[:4]
    task_started_month = start_time_str[4:6]
    task_started_day = start_time_str[6:8]
    task_started_hour = start_time_str[8:10]
    task_started_minutes = start_time_str[10:]

    task_ended_year = end_time_str[:4]
    task_ended_month = end_time_str[4:6]
    task_ended_day = end_time_str[6:8]
    task_ended_hour = end_time_str[8:10]
    task_ended_minutes = end_time_str[10:]
=======
    task_started_year = int(startingtime[:4])
    task_started_month = int(startingtime[4:6])
    task_started_day = int(startingtime[6:8])
    task_started_hour = int(startingtime[8:10])
    task_started_minutes = int(startingtime[10:])

    task_ended_year = int(endingday[:4])
    task_ended_month = int(endingday[4:6])
    task_ended_day = int(endingday[6:8])
    task_ended_hour = int(endingday[8:10])
    task_ended_minutes = int(endingday[10:])

  
>>>>>>> fe6da58553298f1985ca0c5d687e1fca48f9ec7a

    doIcontinue = input("Do you want to continue? Answer yes or no ").lower()

    if doIcontinue == "no":
        break
 """

#test for datetime format parsing
start = datetime(task_started_year,task_started_month,task_started_day,task_started_hour,task_ended_minutes)
end = datetime(task_ended_year,task_ended_month,task_ended_day,task_ended_hour,task_ended_minutes)

print(start)
print(end)



