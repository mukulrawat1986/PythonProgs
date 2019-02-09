nums = [1,2,3]

# print all numbers in a list
print([num for num in nums])

# operate on numbers in the list
print([num*10 for num in nums])

friends = ['matt', 'mona', 'michael']

# operate on the string
print([friend[0].upper() + friend[1:] for friend in friends])

# list comprehension with conditional logic
nums = range(1,7)

evens = [num for num in nums if num % 2 == 0]
odds = [num for num in nums if num % 2 != 0]

# when using else keyword
print([num*2 if num % 2 == 0 else num/2 for num in nums])
