def sum_list(num):
    sum=0
    for i in num:
        sum= sum+i
    return sum
list1=[8,7,6,5,4,3,2]
num=tuple(list1)
print("sum of the list is : ",sum_list(num))