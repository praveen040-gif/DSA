s=" "
print(len(s))
l=[]
for i in s:
    if i not in l:
        l.append(s)
print(len(l))