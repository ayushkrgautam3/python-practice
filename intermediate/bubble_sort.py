#Bubble Sorting
l = [5, 1, 4, 2, 8]
for i in range(len(l)):
    for j in range(0, len(l)-i-1):
        if l[j] > l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]
print("Sorted list:", l)
