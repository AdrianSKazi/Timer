import time
import subprocess
from os import system

def countdown(n):
    n=int(n)
    while n>0:
          print(n)
          time.sleep(1)
          n=n-1
          os.system('clear')
    else:
        print('Finish')
        subprocess.call(['afplay','bell.wav'])
        
n=input('time in seconds: ')
countdown(n)
