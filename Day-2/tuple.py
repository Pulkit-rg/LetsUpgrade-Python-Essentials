# Tuple and its associated functions

tupp=(1, 2, 3,1,86,97,0,98)

#1. len function- for getting the length of the tuple
tupp=(1, 2, 3,1,86,97,0,98)
print("lenght of tuple is", len(tupp))

#2.index function-for finding out the index of an element
tupp=(1, 2, 3,1,86,97,0,98)
print("Index of the element '2' is ", tupp.index(2))
      
#3. min function- to find the minimum value
tupp=(1, 2, 3,1,86,97,0,98)
print("Minimum value in the tuple is ", min(tupp))

#4. max function- to find the maximum value
tupp=(1, 2, 3,1,86,97,0,98)
print("Maximum value in the tuple is ", max(tupp))

#5.tuple function- converts a list into tuple

lis=["hello", "hii","bye"]
print(tuple(lis))
