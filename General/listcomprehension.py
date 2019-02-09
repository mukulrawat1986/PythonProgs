nums = [1,2,3]

# print all numbers in a list
print([num for num in nums])

# operate on numbers in the list
print([num*10 for num in nums])

friends = ['matt', 'mona', 'michael']

# operate on the string
print([friend[0].upper() + friend[1:] for friend in friends])
