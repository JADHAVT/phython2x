#find max from 3 num
num1 = int(input("enter num1"))
num2 = int(input("enter num2"))
num3 = int(input("enter num3"))
#max_num = max(num1,num2,num3)
#print(max_num)
if num1 > num2 and num1 > num3:
    print("Max num is ",num1)
elif num2> num1 and num2 > num3:
    print("max num is",num2)
else:
    print("Max num is ",num3)