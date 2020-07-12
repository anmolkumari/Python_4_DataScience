# This is about Tuples
# tuples
# sequences
#immutable->unchangable,unupdatble, un deletable,un removable
#what is immutable in python->string, tuple, number
#declared in ()
#indexed
#sliced

#list->[]
#tuple->()
#dictionary->{}

#declare
tup=(1,2,3)
print(tup)

#update
#tup[0]=4
print(tup)
# not possible, since it in immutable

#concat
tup2=(4,5,6)
tup1=(1,2,3)
tup3=tup1+tup2
tupc=(1,)
print(tupc)

print(tup3)

#indexed
print(tup2[0])
print(tup3[2])

#slicing
print(tup2[1:3])
print(tup1[2:3])
print(tup3[-4:])

#how to make a tuple from a tuple
tupnew=tup2[1:3]
print(tupnew)


an=(1,)
print(an)


# traversal
for x in tup3:
    print(x)
    

