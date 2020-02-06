import sys
a = int(sys.argv[1])
H = ""
M = ""
if a < 0:
    raise ValueError
else:
    H = a // 60
    M = a % 60
print("transformed {}hours and {}minutes".format(H,M))

#key
import sys

def Hour(minute):
    if minute < 0:
        raise ValueError("Input number cannot be negative")
    else:
        print("{} H,{} M".format(int(minute // 60),minute % 60))
try:
    Hours(int(sys.argv[1]))
except:
    print("Parameter Error")

