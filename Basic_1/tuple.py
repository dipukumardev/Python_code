# list = are the mutable in python (means it can manuplate the data )
# but
# TUPLE = ARE NOT  CHANGE THE DATA MEANS TUPLE ARE NOT MUTABLE ;

# tuple are discribe the ();
# dis are the discribe the {};
# list are the discribe teh [];

family = ("Brother", "Laxime", "maa", "papa", "fav persion")
print(family[0]) # print the 0 index;
print(family[-1]) # print the last index;
print(family[1:]) # print the laxime to last index;

print(len(family))

new = ("dipu", "aditya")
new_add = family + new
print(new_add)