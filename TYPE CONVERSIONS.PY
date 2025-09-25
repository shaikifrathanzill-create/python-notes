#TYPE CONVERSION:

#List-tuple
my_list=[1,2,3,4]
my_tuple=tuple(my_list)
print (my_tuple)
print(type(my_tuple))

#Tuple-list
my_list=[5,6,7]
my_set=set(my_list)
print(my_set)
print(type(my_set))

#List-set(Remove Duplication)
my_list=[1,2,2,3,3,4]
my_set=set(my_list)
print(my_set)
print(type(my_set))

#Set-list
my_set={10,20,30}
my_list=list(my_set)
print(my_list)
print(type(my_list))

#Dictionary-List of Keys
student={'name':'ifra','age':'10','grade':'A'}
keys_list=list(student.keys())
print(keys_list)

#Dictionary-list of values
student={'name':'ifra','age':'10','grade':'A'}
values_list=list(student.values())
print(values_list)

#Dictionary-list of items
student={'name':'ifra','age':'10','grade':'A'}
items_list=list(student.items())
print(items_list) 