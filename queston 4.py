def bubblesort(array):
    for i in range(len(array)-1,0,-1):
        for j in range(i):
            if array[j]>array[j+1]:
                temp= array[j]
                array[j]=array[j+1]
                array[j+1]=temp
array=["a","b","d","c"]
bubblesort(array)
print(array)