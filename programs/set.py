# Set is An unordered, unindexed collection , and set contains only unique values (no duplicates).
# Written using curly braces {} or the set() function.
#set is mutable .

a = {1,2,3,4,5,6,7}
b = set([2,2,3,4,5,6,7,9,0,1,2])
c = {"Zoro" , 1 , 3 , "Shanks"}
print(a)
print(b)
print(c)

#adding to a list
a.add(10)
print("\nAfter adding 10 : ",a)


#union (| or union()) -- prints unique elements from both sets
print("\n after performing union operation :",a | b)
print("\n after performing union operation :",a.union(c))

#Intersection (& or intersection())  -- Common elements between sets
print("\n after performing Intersection operation :",a & b)           
print("\n after performing Intersection operation :",a.intersection(b))

#difference (- or difference())  -- elements in x , but not in y
print("\n after performing difference operation :",b-a)
print("\n after performing difference operation :",a.difference(c))

#symmetric difference (^)   - - prints elements either in a or b , but not in both 
print("\n after performing symmetric diff operation :",a^c)
print("\n after performing symmetric diff operation :",b^c)

#removing an element
c.remove("Zoro")
c.discard(1)          # Safe remove (no error if not found)
print("\n after removing Zoro and 1  in c :",c)  


#clearing a set 
a.clear()               # Removes all elements
print("\nAfter removing all : ",a)

print(len(b))        
