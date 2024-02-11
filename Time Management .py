#  1
todo_List = []
title = input("enter task title:")
duedate = input("enter duedate (yyyy-mm-dd):")
priority = input("enter your priority as(urgent,important and less important):").lower()

def add_task(title,duedate,priority):
    
    task =(title,duedate,priority)
    todo_List.append(task)
    return f"task{title} added in todo list"
print(add_task(title,duedate,priority))
print(todo_List)

if priority == 'urgent':
    print("its urgent")
elif priority == 'important':
    print("its important but not urgent")
else:
    print('less important')
    
#  2
pomodoro = 0
work = 25
target = 4

while pomodoro < target:

    work_time = int(input("enter minutes you work:")) 
    if work_time < work:    
        print(f"You should work more {work - work_time} minutes")
    else:
        pomodoro += 1
        print("You should take a rest")
   
    if pomodoro == target:
        break
print(pomodoro)


#  3
user1 = set(["monday", "friday", "sunday"])
user2 = set(["tuesday", "thursday", "sunday"])
user3 = set(["sunday", "monday", "friday"])



common_day = user1.intersection(user2, user3)

if common_day:
    print("Common meeting times:", common_day)
else:
    print("No common meeting time.")
