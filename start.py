import os
import time

def editfile():
    filename = input('what file do you want to edit: ')
    print('what do you want to edit with')
    print('here are your options')
    print('***************')
    print('*hit 1 for vim*')
    print('***************')
    texteditor = int(input('what is your choise:'))
    if texteditor == 1:
        os.system('vim '+filename)
    else:
        print('invalid input')

def runfile():
    filename = input('what file do you want to run: ')
    os.system('python3 '+filename)

def cd():
    change = input('which directory should I change to: ')
    os.chdir(change)
    print(os.getcwd())

def gitcomit():
    os.system('python3 gitAutomate.py')

def new():
    newfile = input('what do you want to call this file: ')
    os.system('touch '+newfile)

print('Hello Vladyslav')
time.sleep(2)

os.chdir('Desktop/code/python-projects')
print(os.getcwd())

another_time='y'

while another_time == 'y' or another_time == 'Y':
    print('here are your files')
    os.system('ls -l')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print('*******************************')
    print('*hit 1 to edit a file         *')
    print('*hit 2 to run a file          *')
    print('*hit 3 to change into a folder*')
    print('*hit 4 to commit to github    *')
    print('*hit 5 to create a new file   *')
    print('*******************************')
    action = int(input('what action do you want to do: '))
    if action == 1:
        editfile()
    elif action == 2:
        runfile()
    elif action == 3:
        cd()
    elif action == 4:
        gitcomit()
    elif action == 5:
        new()
    else:
        print('invalid input')

    another_time = input('do you want to do another action: ')

print('You quit the program')
print('Goodbye Vladyslav')
time.sleep(2)
os.system('clear')
