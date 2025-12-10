marks=[67,89,45,92,56,78,88,90,45,67]
k=10   #updated size
for i in range(0,k-1):
    for j in range(i+1,k):
        if marks[i]==marks[j]:
            marks.pop(j)
            k-=1
sum=0
for i in range(0,k):
    print("updated marks ",marks[i])
    sum+=marks[i]

max=0
min=sum
for i in range(0,k):
    if marks[i]<min:
        min=marks[i]
    if marks[i]>max:
        max=marks[i]

Marks_m={"highest":max,"lowest":min,"average":sum/k}
print("Minimum is :",Marks_m["lowest"])
print("Maximum is :",Marks_m["highest"])
print("Average is :",Marks_m["average"])
