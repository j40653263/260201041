import time
def timer(t):
    if t == 0:
        print("Done!")
    else:
        print(t)
        time.sleep(5)
        timer(t-1)
        
timer(3)