from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json
from PyInquirer import Validator, ValidationError
from PyInquirer import style_from_dict, Token, prompt
import datetime
from datetime import datetime

def user_interface():
    style = style_from_dict({
        Token.QuestionMark: '#E91E63 bold',
        Token.Selected: '#673AB7 bold',
        Token.Instruction: '',  # default
        Token.Answer: '#2196f3 bold',
        Token.Question: '',
    })

    print("Input your work hours")

    #testing if user inputs are correct (not ready)
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
            'message': 'Enter start time(yyyy-mm-dd hh:mm):'
            #'validate': start_time_validator
        },
        {
            'type': 'input',
            'name': 'end_time',
            'message': 'Enter end time(yyyy-mm-dd hh:mm):'
        },
        {
            'type':'list',
            'name':'continue',
            'message':'Do you want to add more hours?',
            'choices': ["yes","no"]
        }
    ]

    #User inputs to values
    answers = prompt(questions, style=style)
    project_name = answers.get('project_name')
    task_explanation = answers.get('task')
    start_time_str = answers.get('start_time')
    end_time_str = answers.get('end_time')
    continue_info = answers.get('continue')

    #printing values to user 
    #print(project_name, task_explanation, start_time_str, end_time_str, continue_info)

    #test for datetime format parsing
    start = datetime.strptime(start_time_str, "%Y-%m-%d %H:%M")
    end = datetime.strptime(end_time_str, "%Y-%m-%d %H:%M")

    return [project_name,task_explanation,start,end,continue_info]

def start():

    answers = user_interface()
    print(answers)

if __name__ == "__main__":
    start()