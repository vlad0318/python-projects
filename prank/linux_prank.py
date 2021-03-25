import os
import time

def restart():
    t = 10*60
    print('your computer will restart')
    while t:
        mins = t // 60
        secs = t % 60
        timer = '{:02d}:{:02d}'.format(mins,secs)
        print(timer,end="\r")
        time.sleep(1)
        t -= 1
    os.system('sudo shutdown -h now')

times = 0
for times in range (10):
    osCommandString = "gedit file.txt"
    os.system(osCommandString)

restart()
