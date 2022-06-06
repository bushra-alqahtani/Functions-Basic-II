#Countdown - Create a function that accepts a number as an input. Return a 
#new list that counts down by one, from the number (as the 0th element)
#down to 0 (as the last element).

def countdown(a):
    array=[]
    for x in range(a,-1,-1):
       array.append(x)
    return array   
       
print(countdown(5))



#Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
def print_and_return(list):
    print(list[0])
    return list[1]
print(print_and_return([2,1])) 


#Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.


def sumoflist(list):
    sum=list[0]+len(list)
    return sum
print(sumoflist([2,2,23,4,5,6]))

#Write a function that accepts a list and creates a new list containing only the 
# values from the original list that are greater than its 2nd value. Print how many values this is and then return
#  the new list. If the list has less than 2 elements, have the function return False


def values_greater_than_second(a):
    newa=[]
    if len(a) > 1:    
        for x in range(len(a)):
            if a[x]>a[1]:
               newa +=[a[x]]    
        return (newa)
    
print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))


 # Write a function that accepts two integers as parameters: size and value

def length_and_value(s,v):
    new_list = []
    for x in range (0,s,1):
        new_list += [v]
    return new_list

print(length_and_value(5,4))
        
        
