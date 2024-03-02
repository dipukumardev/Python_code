# diff_name = ["dipu", "aditya" , "singh", "kumar"]
# print(diff_name)
# # print(",  ".join(diff_name)) is use to convert list to string
# print(len(diff_name))
# print(diff_name[0]) 


# diff_name[3] = "Rohit"
# print(diff_name)


# using the some property in list operations;
# replacing the list items and add new elements;


# frind_group = ["Aditya", "Rohit", "Vishal", "Manji", "rupa", "shivke"]
# print(frind_group)
# frind_group[1:2] = ["dipu"]
# print(frind_group[1])
# frind_group[2:4] = ["Ritesh", "Kajal"]
# print(frind_group)


# some more extra compactiaion addition on the list or arrays;

# tea = ["masal", "black", "white", "broune"]
# print(tea)
# tea[1:1] = ["Aditya", "Aditya"]
# print(tea)
# # to perform empty array oprations;
# tea[1:3] = []
# print(tea)


# conditions in the python for  use in python

# tea = ["Masala tea", "White tea", "Broune tea", "Elechi Tea"]
# for loo in tea:
#         print(loo)


# for loo in tea:
#         print(loo , end=" - ")



#  if statement in python

# pop delete the last elements 

# tea = ["Masala", "Black", "White", "Broune"]
# tea.append("Aditya")
# tea.pop()
# tea.remove("Black")
# tea.insert(1, "Black")
# tea.insert(4, "Aditya")
# print(tea)
# if "Masala" in tea:
#     print("This order willl be conform")



# copy refrance in python
# tea = ["Masala", "Ginger", "Lemon", "Black"]
# tea_copy = tea
# print(tea)
# print(tea_copy)


#  how to use the range in python

num = [x**2 for x in  range(10)]
print(num)