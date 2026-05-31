import random
marks=[]
for i in range(20):
    marks.append(random.randint(0,100))
fail=[]
avg=[]
good=[]

print("marks",marks)
for j in marks:
    if j<=30:
        fail.append(j)
    if j<=31 and j>=69:
        avg.append(j)
    if j>=70:
        good.append(j)

print("fail:",len(fail))
print("avg:",len(avg))
print("good:",len(good))