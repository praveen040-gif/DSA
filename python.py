# from collections import Counter
# # Counter() Method:it is like a dictionary it returns the [descending sorted dictionary] based on values
# # Sample dictionary
# sample_dict = {1: 5, 3: 2, 2: 8, 0: 1}

# # Sorting using a for loop
# s=Counter(sample_dict)

# print(s)

# # output:Counter({2: 8, 1: 5, 3: 2, 0: 1})

# print(s[2]) #----> output 5

# l1=[2,4,1,3]
# l2=[7,5,6,8]
# l=[]
# for i in zip(l1,l2):
#     l.append(list(i))
#     print(i)
# print(l)
# l.sort(key=lambda x:x[1])
# print(l)

# ans=lambda x:x*x
# l=[1,2,3,4,5]
# print(ans(l[4]))

# n=5
# l=[]
# for i in range(n):
#     l.append('.'*n)
# # print(l)
# l[0]=l[0][:3]+'Q'+l[0][4:n]
# print(l)
# if str(5)=='5':
#     print("yes")
# else:
#     print("no")

# s=""
# for i in range(1,4):
#     s=s+str(i)
# print(s)
# l=['1','2','3']
# print("".join(l))
# print(-3%10)
# l=[0]*5
# print(l)
# Python implementation of above approach
from collections import defaultdict

# Function for calculating 
# minimum operations
def minimum_operations(arr):
	
	# Declare defaultdict for storing the 
	# index of each element
	mpp = defaultdict(list)
	
	for i, x in enumerate(arr):
		mpp[x].append(i)

	# Declare a queue which stores the count 
	# of previously non-zero elements
	q = []
	st = set()

	# Count the total operations
	count = 0
	for i in range(len(arr) - 1):
		if arr[i] not in st and arr[i] != 0:
			q.append(arr[i])
			st.add(arr[i])

		# If found the violating condition
		if arr[i] > arr[i + 1]:
			
			# Increase the count by the 
			# previously non-zero elements
			count += len(q)
			while q:
				top = q.pop(0)
				if top in mpp:
					
					# Set all occurrences of previously 
					# assigned zero elements to zero
					for idx in mpp[top]:
						arr[idx] = 0
						
	# Returning the count
	return count

# Driver code

arr = [3,3,2]
# Function call
print(minimum_operations(arr))

# This Code is Contributed by Prasad Kandekar(prasad264)



    





