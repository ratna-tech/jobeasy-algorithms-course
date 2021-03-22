#Find the biggest number in the list (divide and rule)
original_array= []
length_of_array = int(input("Input a number for array length "))
for i in range(length_of_array):
  original_array.append(int(input("Input numbers for array ")))

def findmaxnum(anArray,size):
  if size == 0:
    return 0

  if (size == 1):
   return anArray[0]

  #divide and conquer
  mid = size // 2
  rsize = size - mid
  lnum = findmaxnum(anArray[0:mid], mid)
  rnum = findmaxnum(anArray[mid:], rsize)
  if lnum > rnum:
   return lnum
  else: return rnum

print(findmaxnum(original_array,length_of_array))

