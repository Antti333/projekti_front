import curses

project_name = ""
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

#2020, 6, 30, 13, 00

#helppokäyttöliittymä
while True:
    print("Add your worktime for today")
    project_name = input("Which project you worked today on?")
    task_explanation = input("What did you do today?")

    while True:
        startingtime= input("When did you start today? format: YYYYMMDDHHMM")
        if len(startingtime) != 12:
            print("You did not put the starting time in correct format. Put it as YYYYMMDDHHMM ex. 202112241805")
        else:
            break

    while True:
        endingday= input("When did you end today? format: YYYYMMDDHHMM")
        if len(endingday) != 12:
            print("You did not put the starting time in correct format. Put it as YYYYMMDDHHMM ex. 202112241805")
        else:
            break
    

    task_started_year = startingtime[:4]
    task_started_month = startingtime[4:6]
    task_started_day = startingtime[6:8]
    task_started_hour = startingtime[8:10]
    task_started_minutes = startingtime[10:]

    task_ended_year = endingday[:4]
    task_ended_month = endingday[4:6]
    task_ended_day = endingday[6:8]
    task_ended_hour = endingday[8:10]
    task_ended_minutes = endingday[10:]

    print(endingday)
    print(task_ended_hour)

    print(startingtime)
    print(task_ended_hour)
    print(task_started_year,task_started_month, task_started_day, task_ended_hour,task_started_minutes)
    doIcontinue = input("Do you want to continue? Answer yes or no ").lower()

    if doIcontinue == "no":
        break

