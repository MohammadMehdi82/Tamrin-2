# revers the elemnts within an array

a = [23,65,10,12,14,18,95,62,34,65,57,555]
n = len(a)
for i in range(n//2):
    temp = a[i]
    a[i] = a[n - 1 - i]
    a[n - 1 - i] = temp
print(a)