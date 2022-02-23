# nested for

class_1 = [86, 80, 75, 82, 80, 70]
class_2 = [40, 55, 60, 48, 50]
class_3 = [90, 85, 30, 86, 78, 75, 54]

classes = (class_1, class_2, class_3)
average_class = []

for i in classes:
    total = sum(i)
    number = len(i)
    average = total / number
    average_class.append(average)

formatted_class = [round(float(i), 2) for i in average_class]
# print(formatted_class)

print("Average Mark for Class 1 is " + str(formatted_class[0]))
print("Average Mark for Class 2 is " + str(formatted_class[1]) + '0')
print("Average Mark for Class 3 is " + str(formatted_class[2]))

# Q1:
# You have to design a programme/ function to achieve below objectives:
# Given that there is an array contains number from 1 to 100.
# When the number is multiple of 3, print "bug"
# When the number is multiple of 5, print "fix"
# When the number is multiple of 3 and 5, print "bugfix"

num_list = []                       # List to Store Values
for i in range(1, 101):
    if i % 3 == 0 and i % 5 ==0:    # Find Multiples of 3 & 5
        num_list.append("bugfix")
    elif i % 3 == 0:                # Find Multiples of 3
        num_list.append("Bug")
    elif i % 5 == 0:                # Find Multiples of 5
        num_list.append("Fix")
    else:
        num_list.append(i)          # Numbers that are not multiples of 3 and/ or 5

print(num_list)

# Q2:
# You have to design a programme/ function to achieve below objectives:
# Given two arrays, [1,2,3,4,5] and [2,3,1,0,5]
# find which number(s) is/are not present in the second array

list_1 = [1,2,3,4,5]
list_2 = [2,3,1,0,5]

list_diff = []

for i in list_1:
    if i not in list_2:
        list_diff.append(i)

print(list_diff)


# Q3:
# You have to design a programme/ function to achieve below objectives:
# Given two arrays, [1,2,3,4,5] and [2,3,1,0,5]
# find which number(s) is/are common in both array

list_1 = [1,2,3,4,5]
list_2 = [2,3,1,0,5]

list_common = []

for i in list_1:
    if i in list_2:
        list_common.append(i)

print(list_common)

#Q4:
# You have to design a programme/ function to achieve below objectives:
# Given two arrays, [1,2,3,4,5] and [2,3,1,0,5]
# merge these two arrays and unique to display 
# Answer: [0 ,1, 2, 3, 4, 5]

list_1 = [1,2,3,4,5]
list_2 = [2,3,1,0,5]

merge_list = list_1 + list_2
no_duplicates = list(dict.fromkeys(merge_list)) # Dictionaries cannot contain duplicates
no_duplicates.sort()

print(no_duplicates)


# Q5: 
# You have to design a programme/ function to achieve below objectives:
# How do you find the closest integer 17 in [30, 1, 5, 16, 19, 21, 2, 55]? 
# Answer: 16

list_1 = [30, 1, 5, 16, 19, 21, 2, 55]
val = 17
ans = []

for i in range(5):
    for n in list_1:
        if n - i == val:
            ans.append(n)
        elif n + 1 == val:
            ans.append(n)
close_int = list(dict.fromkeys(ans))    # Remove Duplicates
print(close_int[0])

