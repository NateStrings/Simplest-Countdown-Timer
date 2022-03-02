import time

s = int(input("Seconds: ")) # Get users input as an integer

for i in range(s):
# you can also replace above line with "while  s > 0 :""
    print(str(s), end = "\r")
    s -= 1 #this is essentially s = s - 1
    time.sleep(1) # sleep for one second between loops

print("Time is up!") 





