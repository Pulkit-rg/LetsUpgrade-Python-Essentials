# Sets and its Default functions

set1= {"priya", "jain", 1, 2, 3, 3, 4, 1, 6,7 }
set2= {"Nandini", "Pihu", 2, 5, 7, 9}

#1. Add function- for adding an element in the set
set1= {"priya", "jain", 1, 2, 3, 3, 4, 1, 6,7 }
set1.add("Hello")
print(set1)

#2. Discard function- for removing an element fron the set
set1= {"priya", "jain", 1, 2, 3, 3, 4, 1, 6,7 }
set1.discard("priya")
print(set1)

#3. Difference function- gives the difference between two sets
set1= {"priya", "jain", 1, 2, 3, 3, 4, 1, 6,7 }
set2= {"Nandini", "Pihu", 2, 5, 7, 9}
diff=set1.difference(set2)
print(diff)

#4. Union Function- for combining two sets 
set1= {"priya", "jain", 1, 2, 3, 3, 4, 1, 6,7 }
set2= {"Nandini", "Pihu", 2, 5, 7, 9}
un=set1.union(set2)
print(un)

#5. Intersection Function- for finding out the comman elements between two sets
set1= {"priya", "jain", 1, 2, 3, 3, 4, 1, 6,7 }
set2= {"Nandini", "Pihu", 2, 5, 7, 9}
inte=set1.intersection(set2)
print(inte)

#6. pop function- removes a randowm item from the set
set1= {"priya", "jain", 1, 2, 3, 3, 4, 1, 6,7 }
set1.pop()
print(set1)


