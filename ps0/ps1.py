import math
def ps1(x,y):
    
   # x = arg[0]
    #y = arg[1]
    return math.pow(x,y),math.log(x)

x= int(input('entry number x:'))
y= int(input('entry number y:'))

result = ps1(x,y)
print(result)