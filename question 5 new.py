def number5program():
    newlist=[]
    
    numbers=input("enter the elements:")
    
    newnum=numbers.split(",")
    for i in newnum:
        newlist.append(int(i))
    print("here is the sorted list: ")
    print(mergesort(newlist))









def mergesort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left_half=arr[:mid]
    right_half=arr[mid:]

    left_half=mergesort(left_half)
    right_half=mergesort(right_half)

    return merge(left_half,right_half)
def merge(left,right):
    merged=[]
    left_in=0
    right_in=0

    while left_in<len(left)and right_in<len(right):
        if left[left_in]<right[right_in]:
            merged.append(left[left_in])
            left_in+=1
        else:
            merged.append(right[right_in])
            right_in+=1
    while left_in<len(left):
        merged.append(left[left_in])
        left_in+=1
    while right_in<len(right):
        merged.append(right[right_in])
    return merged
number5program()