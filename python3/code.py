#  Strings(are not muttable)
'''
word1 = "I love"
word2 = "python"
sentence = word1 + " " + word2

#concatenate
print(sentence)

#slicing
print(word1[2:4])
print(word1[2:])'''

'''
a=5
b=7
sum = a+b

##formatting
# normal
print("sum = {}".format(sum))
print("sum of {} and {} is {}".format(5,7,sum))

# index based formatting 
print("sum of {1} and {0} is {2}".format(5,7,sum))

## f-strings
print(f"sum of {a} + {b} is {a+b}")'''

##lists(are muttable)
'''
marks = [70,59,68,89,87,"abc",90.49]

marks[1] = 90

print(marks)
print(marks[:5])
print(marks[5:])'''

'''
nums = [1,2,4,6,7]

nums.append(5)

nums.insert(2,3)

nums.sort()
print(nums)
nums.sort(reverse=True)

print(nums)'''

#loops in lists

'''
linear search in list
nums = [2,4,1,53,5]

x = 53
idx = 0

for val in nums:
    if(val == x):
        print(f"{x} is at the index {idx}")
        break
    idx +=1'''

##Tuples(are not muttable just like strings)
'''
tup = (2,4,2,5,1,5,2,0)

sum = 0

for val in tup:
    sum = sum+val

print(f"sum of all values in tup is {sum}")

#Methods
print(tup.index(2))
print(tup.count(2))'''

##Dictionary(key:val)

##Sets
# sets are muttable but the values in it are not
'''
s = {0,1,2,3,3}

s.add(4)
s.remove(2)
print(s)
s.pop()
print(s)
s.clear()
print(s)

# print(type(s))'''


