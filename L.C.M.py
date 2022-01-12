def lcm(x,y):
    if x>y:
        greter = x
    else:
        greter = y
    i=2
    lcm =1
    while (True):
        if(((greter%x==0)and (greter%y==0))):
            lcm = greter
            break
        greter+=1
    return lcm
num1 = 12
num2 = 8
print("the L.C.M of",num1,"and",num2,"is",lcm(num1,num2))

