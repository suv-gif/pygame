s1=[1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8]
set1=set(s1)
print(set1)
#sets are indexable
#print(set1[0])
#can not get index of set

if 4 in set1:
    print("yes")
else:
    print("no")

#adding element to set
set1.add(0)
print(set1)
set1.remove(0)
print(set1)
# iterating through the set
for i in set1:
    print(1)

#set operations
print("union of sets")
set2={4,5,3,9,9,2,4,85,2,5,276,3,849}
set3={1,4,5,4,5,65,5,13,23,54,52,32,46,42,54,5,3,23,463}
print(set2.union(set1))
print(set2.intersection(set3))
print(set2.difference(set3))
print(set2.symmetric_difference(set3))
total=0
for j in set1:
    total=total+j
avg=total/len(set1)
print(avg)