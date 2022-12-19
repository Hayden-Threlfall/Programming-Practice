arr1 = [3,4,5]
arr2 = [1,2,3]
arr2.append(arr1[-2:])
arr1[-2:]=[]
print(arr2)