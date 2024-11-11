# find the maximum of the array values

a= [3,10,12,1,4,9,8,14,41,23,20]
maximum = a[0]
for v in a[1:]:
    if (v > maximum):
       maximum = v
       print(maximum)