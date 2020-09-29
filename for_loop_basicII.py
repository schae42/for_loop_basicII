# 1.    Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

def biggie_size(list):
    for i in range(len(list)):
        if list[i] > 0:
            list[i] = "big"
    print(list)
biggie_size([-1, 3, 5, -5])

# 2.    Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. 
# (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

def count_positives(list):
    count=0
    for i in range(len(list)):
        if list[i] > 0:
            count+=1
    arr[len(list)-1]= count
    print(list)
count_positives([-1,1,1,1])
count_positives([1,6,-4,-2,-7,-2])    


# 3.    Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

def sum_total(list):
    total=0
    for i in range(len(list)):
        total+=arr[i]
    print(total)
sum_total([1,2,3,4])
sum_total([6,3,-2])

# 4.    Average - Create a function that takes a list and returns the average of all the values.x
# Example: average([1,2,3,4]) should return 2.5

def average(list):
    total=0
    avg=0
    for i in range(len(list)):
        total+=list[i]
    avg=total/len(arr)
    print(avg)
average([1,2,3,4])

# 5.    Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0

def length(list):
    length_list =len(list)
    print(length_list)
length([37,2,1,-9])
length([])

# 6.    Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False

def minimum(list):
    minimum=list[0]
    for i in range(len(list)):
            if minimum>list[i]:
                minimum=list[i]
    print(minimum)
minimum([37,2,1,-9])
minimum([])   

# 7.    Maximum - Create a function that takes a list and returns the maximum value in the list. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False

def maximum(list):
    maximum=list[0]
    i=1
    if len(list)<=1:
        return False
    for i in range(len(list)):
        if maximum<list[i]:
            maximum=list[i]
    print(maximum)
maximum([37,2,1,-9])
maximum([])

# 8.    Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

def ultimate_analysis(list):
    min=list[0]
    max=list[0]
    total=0
    i=0
    for i in range(len(list)):
        if min > list[i]:
            min=list[i]
        else max < list[i]:
            max=list[i]
        total+=list[i]
    avg=total/len9list
    length=len(list)
    print("minimun:" + str(min))
    print("maximum:" + str(max))
    print("sumTotal:"+ str(total))
    print("average:" + str(avg))
    print("length:" + str(length))
ultimate_analysis([37,2,1,-9])

# 9.    Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. 
# (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

def reverse_list(list):
    length=len(list)
    for i in range(0, length/2):
        length=length-1
        temp=list[i]
        list[i]=list[length]
        list[length]=temp
    print(list)
reverse_list([37,2,1,-9])