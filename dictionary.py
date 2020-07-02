#This is about dictionary:

"""it is actually a datatype that is unordered,non indexable,hash like structure with key and value pair where the key is supposed to be a immuatble type while no suc restriction happens for the value
"""

"""why we cannot index dictionary?
->because it is unordered"""

#declaration

dic={1:"A",2:"B",3:"C",4:"D",5:"E"}
print(dic)



#list of dictionaries
#list of dictionary inside dictionary
person=[{
    "name":{"Anmol","Kumari","none"},
    "age":19,
    "height":160
       },{
           "name":"Anshu",
           "age":20,
           "height":170
       }]



#list of dictionary
person2=[{
    "name":"Tridib",
    "Age":20,
    "height":177
},{
    "name":"Ankit",
    "age":20,
    "height":175
}]
print(person2)


"""Homework: level1 : ------------
         level 2:------------
         level3:------------
         level 4:------"""
         


x=dic[3]  # we pass the key to fetch value
print(x)
print(dic[5])
#using get()->value, we pass the key to fetch value
x=dic.get(5)
p