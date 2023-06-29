import time
def countouttimer(seconds):
    while seconds>0:
        mins=int(seconds/60)
        second=int(seconds%60)
        timer=f"{mins}:{second}"
        print(timer)
        seconds-=1
    print("time up")  
seconds=input("enter the time in numbers of seconds") 
countouttimer(int(seconds))     


