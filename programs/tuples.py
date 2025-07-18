#tuples are like list , it allows multi data type values , it allows duplicates but we cannot change (immutable) any data from the Tuple
#for read only operations , tuple is faster than list .


#simple value insertion to tuple 
n = int(input("Enter no of characters/records :"))
tup = ()
for i in range(n):
    x = input(f"Enter record no {i+1} : ")
    tup+=(x,)

print(tup)

#it can accept all data types ,just like tuple
tup2 = (1,"Shanks",'m',0.5,455)
print(tup2)
print(tup2[::-1])

#looping through the tuple 
for  x in tup2 :
    print(f"\n{x} is at the index of ",tup2.index(x))

#concat
print("After combining tup and tup2: ",tup+tup2)


#nested tuple
tupn = (2,(1,2,3),(4,5,6),("seven"))
print(tupn)
#printing seven in reverse 
print(tupn[3][::-1])

#length
print(len(tupn))

#count
print(tupn.count(2))

#trying to change the values 
tupn[0]  = "trying to update"  #error

