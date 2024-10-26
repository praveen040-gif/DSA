from collections import Counter
# Counter() Method:it is like a dictionary it returns the [descending sorted dictionary] based on values
# Sample dictionary
sample_dict = {1: 5, 3: 2, 2: 8, 0: 1}

# Sorting using a for loop
s=Counter(sample_dict)

print(s)

# output:Counter({2: 8, 1: 5, 3: 2, 0: 1})

print(s[1]) #----> output 5

