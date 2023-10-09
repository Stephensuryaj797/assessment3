String1=input("enter a string:")
def rev_str(string1):
    lenght=len(string1)
    sum=""
    for i in range(-1,(-lenght-1),-1):
        sum=sum+string1[i]
    return sum
print("reverse a string: ",rev_str(String1))