array1=[3,7,1,9,4]
def deleteElement(array,tar_index):
    
    for i in range(len(array)):
        if i==tar_index:
            array.remove(array[tar_index])
            return array
    if tar_index >= len(array):
        print("invalid index")
        return array
        
            
            
    
print(deleteElement(array1,3))