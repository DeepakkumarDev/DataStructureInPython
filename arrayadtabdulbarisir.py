import array
"""
'b': Signed char (1 byte)
'B': Unsigned char (1 byte)
'u': Unicode character (2 bytes, deprecated in Python 3)
'h': Signed short (2 bytes)
'H': Unsigned short (2 bytes)
'i': Signed integer (4 bytes)
'I': Unsigned integer (4 bytes)
'l': Signed long (4 bytes)
'L': Unsigned long (4 bytes)
'q': Signed long long (8 bytes)
'Q': Unsigned long long (8 bytes)
'f': Float (4 bytes)
'd': Double (8 bytes)
"""
# Create an array of size 10 with all elements initialized to 0
arr1= array.array('i', [0] * 10)  # 'i' stands for integer type code
print(arr1)

size=10
length=size
type='i'
a=array.array(type,[0]*length)
print(a)
"""
import array
from functools import wraps

def log_method_call(method):
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        print(f"Calling {method.__name__} with args: {args}, kwargs: {kwargs}")
        result = method(self, *args, **kwargs)
        print(f"{method.__name__} returned: {result}")
        return result
    return wrapper

class Array:
    def __init__(self, size, type_code):
        self.size = size
        self.type_code = type_code
        self.array = array.array(type_code, [0] * size)
        self.current_length = 0  # Track the number of elements

    def __str__(self):
        return str(self.array[:self.current_length])

    @log_method_call
    def insert(self, index, value):
        #Insert a value at a specific index.
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        self.array[index] = value
        self.current_length = max(self.current_length, index + 1)

    @log_method_call
    def delete(self, index):
        #Delete the value at a specific index (set to 0 for integer arrays).
        if index < 0 or index >= self.current_length:
            raise IndexError("Index out of range")
        self.array[index] = 0
        self.current_length = max(0, self.current_length - 1)

    @log_method_call
    def set(self, index, value):
        # Set the value at a specific index.
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        self.array[index] = value
        self.current_length = max(self.current_length, index + 1)

    @log_method_call
    def get(self, index):
        # Get the value at a specific index.
        if index < 0 or index >= self.current_length:
            raise IndexError("Index out of range")
        return self.array[index]

    @log_method_call
    def append(self, value):
        # Append a value to the array, resizing if necessary.
        if self.current_length >= self.size:
            # Resize the array
            new_size = self.size * 2
            new_array = array.array(self.type_code, [0] * new_size)
            new_array[:self.size] = self.array
            self.array = new_array
            self.size = new_size
        
        self.array[self.current_length] = value
        self.current_length += 1

# Example usage
arr = Array(10, 'i')
print("Initial array:", arr)

arr.set(5, 42)
print("After setting index 5 to 42:", arr)

print("Value at index 5:", arr.get(5))

arr.insert(3, 99)
print("After inserting 99 at index 3:", arr)

arr.delete(3)
print("After deleting value at index 3:", arr)

arr.append(123)
print("After appending 123:", arr)
"""

class Array:
    def __init__(self,size,type_code):
        self.size=size
        self.array=array.array(type_code,[0]*size)
        self.length=0

    def __str__(self):
        return str(self.array[:self.length])
    
    def insert(self,index,value):
        if index<0 or index>self.size:
            raise IndexError("Index out of range")
        self.array[index]=value
        self.length=max(self.length,index+1)

    def append(self,value):
        if self.length==self.size:
            raise IndexError("Index out of range")
        if self.length<self.size:
            self.array[self.length]=value
            self.length+=1
        
    def delete(self,index):
        if index<0 or index>self.size:
            raise IndexError("Index out of range")
        x=self.array[index]
        for i in range(index,self.length-1):
            self.array[i]=self.array[i+1]
        self.length-=1
    
    def search(self,value):
        for i in range(self.length):
            if self.array[i]==value:
                return i
        else:
            return -1
    def improvedsearch(self,value):
        #Improving linear search using Transpositon
        for i in range(self.length):
            if self.array[i]==value:
                self.array[i-1],self.array[i]=self.array[i],self.array[i-1]
                return i
        else:
            return -1
    
    def movetofront(self, value):
        for i in range(self.length):
            if self.array[i] == value:
                # Swap the found element with the first element
                self.array[0], self.array[i] = self.array[i], self.array[0]
                return
        # Return -1 if the value was not found
        return -1
    
    def misingSingleElement(self):
        sum=0
        for i in range(self.length):
            sum+=self.array[i]
        lastelemnt=self.array[self.length-1]
        s=(lastelemnt*(lastelemnt+1))/2
        diff=s-sum
        return diff
    
    def singleMissingElemnt2ndMethod(self):
        diff=self.array[0]-0
        for i in range(self.length):
            if self.array[i]-i!=diff:
                # print(f"Missing Element is {i+diff}")
                # break
                return f"Missing Element is {i+diff}"
        else:
            return -1
        

    def multipleMissingElement(self):
        diff=self.array[0]-0
        for i in range(self.length-1):
            if self.array[i]-i!=diff:
                while(diff<self.array[i]-i):
                    print(i+diff,sep='\n')
                    diff+=1


    def maxEle(self):
        max=self.array[0]
        for i in range(self.length-1):
            if self.array[i]>max:
                max=self.array[i]
        return max
    
    def missingElemHashMethod(self):
        maximum = self.maxEle()
        if maximum is None:
            print("Array is empty")
            return

        # H = array.array('i', [0] * (maximum + 1))
        H=[0] * (maximum + 1)
        for i in range(self.length):
            H[self.array[i]] += 1

        missing_elements = []
        for j in range(1, maximum):
            if H[j] == 0:
                missing_elements.append(j)

        if missing_elements:
            print("Missing elements are:", *missing_elements, sep='\n')
        else:
            print("No missing elements")


    def duplicateEle(self):
        if self.length <= 1:
            print("No duplicates")
            return

        lastDuplicate = None
        for i in range(self.length - 1):
            if self.array[i] == self.array[i + 1] and self.array[i] != lastDuplicate:
                print(self.array[i])
                lastDuplicate = self.array[i]
    def duplicateCount(self):
        if self.length <= 1:
            print("No duplicates")
            return

        for i in range(self.length ):
            if self.array[i] == self.array[i + 1]:
                count = 1
                j = i + 1
                while j < self.length and self.array[j] == self.array[i]:
                    count += 1
                    j += 1
                print(f"{self.array[i]} is appearing {j-i} times")
                # i = j  # Move i to the end of the current sequence of duplicates
    def duplicateHashElem(self):
        max = self.maxEle()
        if max is None:
            print("Array is empty")
            return

        H = [0] * (max + 1)
        for i in range(self.length):
            H[self.array[i]] += 1

        for j in range(max + 1):
            if H[j] > 1:
                print(f"Duplicate element is {j} and it is duplicated {H[j]} times")

    def deuplicateUnsorted(self):
        count=0
        for i in range(self.length-1):
            count=1
            if self.array[i]!=-1:
                for j in range(i+1,self.length-1):
                    if self.array[i]==self.array[j]:
                        count+=1
                        self.array[j]=-1
                if count>1:
                    print(self.array[i],count)


    def pairSum(self,value):
        for i in range(self.length-1):
            for  j in range(self.length-1):
                if self.array[i]+self.array[j]==value:
                    print(self.array[i],self.array[j],value)


    def pairSumHashing(self,k):
        max=self.maxEle()
        H=[0]*(max+1)
        for i in range(self.length):
            if(H[k-self.array[i]]!=0):
                print(self.array[i],(k-self.array[i]),k)
            H[self.array[i]]+=1


    def pairsumSortedArray(self, k):
        i = 0
        j = self.length - 1
        while i < j:
            current_sum = self.array[i] + self.array[j]
            if current_sum == k:
                print(f"Pair found: {self.array[i]} + {self.array[j]} = {k}")
                i += 1
                j -= 1
            elif current_sum < k:
                i += 1
            else:
                j -= 1


    def maxmin(self):
        min=self.array[0]
        max=self.array[0]
        for i in range(self.length):
            if self.array[i]<min:
                min=self.array[i]
            elif self.array[i]>max:
                max=self.array[i]
        print(f"Mininum Element is {min} and Maximum Element is {max}")









        








arr=Array(20,'i')
# arr.insert(0,16)
# arr.insert(1,12)
# arr.insert(2,18)
# arr.insert(3,9)
# arr.insert(4,12)
# arr.insert(5,12)
# arr.insert(6,15)
# arr.insert(7,16)
# arr.insert(8,17)
# arr.insert(9,18)
# arr.insert(10,19)
# arr.insert(11,16)
# arr.insert(0,6)
# arr.insert(1,7)
# arr.insert(2,8)
# arr.insert(3,9)
# arr.insert(4,10)
# arr.insert(5,11)
# arr.insert(6,13)
# arr.insert(7,14)
# arr.insert(8,15)
# arr.insert(9,16)
# arr.insert(10,17)
arr.insert(0,1)
arr.insert(1,2)
arr.insert(2,3)
arr.insert(3,4)
arr.insert(4,5)
arr.insert(5,6)
arr.insert(6,7)
arr.insert(7,8)
# arr.insert(8,10)
# arr.insert(9,10)
# arr.insert(10,11)
# arr.insert(11,12)
# arr.insert(12,13)
# arr.insert(13,14)
# arr.insert(14,15)
# arr.append(13)
# arr.append(15)
# arr.delete(0)

# print(arr)
# print(arr.search(12))
# print(arr.improvedsearch(10))
# print(arr)
# print(arr.movetofront(8))
print(arr)
# print(arr.misingSingleElement())
# print(arr.singleMissingElemnt2ndMethod())
# arr.multipleMissingElement()
# arr.missingElemHashMethod()
# arr.duplicateEle()
# arr.duplicateCount()
# arr.duplicateHashElem()
# arr.deuplicateUnsorted()
# arr.pairSum(24)
# arr.pairSumHashing(24)

# arr.pairsumSortedArray(10)
arr.maxmin()
print([x for x in range(8)])