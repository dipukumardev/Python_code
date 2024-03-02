# how to define disnary in python


dost_age ={"Dipu":20, "nirbhay":23 , "rohit":19, "manji":23, "vishal":25}
print(dost_age)
print(dost_age["manji"])
print(dost_age.get("Dipu"))

print("keys of the dost_age")

for dost in dost_age:
        print(dost)

print("Print the keys and values fo the dost")
for key, values in dost_age.items():
     print(key ,  values)

print("how to use if and else in python:")
if "Dipu" in dost_age:
       print("yes dipu are present in dost_age")


       print("find the length of the distnary")
       print(len(dost_age))

       print("how to add the new key and values in dis")

print("HOW TO PUT DIS INTO DIS")
trust = {
       "family" : {"Ritesh ": "Singh", "Kajal":"devi"},
       "dream"  :{"papa":"true","maa":"happy" }
}

print(trust["family"])
print(trust["dream"])


print(trust)
for key,values in trust.items():
       print(key,values)


# THIS LINE RUN IN TERMINAL;
#        dost_age["rupa"] = 34;
# >>> dost_age
# {'Dipu': 20, 'nirbhay': 23, 'rohit': 19, 'manji': 23, 'vishal': 25, 'rupa': 34}
       


#how to remove the dis items 
       

#        >>> dost_age.pop("rupa")
# 34
# >>> dost_age
# {'Dipu': 20, 'nirbhay': 23, 'rohit': 19, 'manji': 23, 'vishal': 25}
       


#         del dost_age["rohit"]

# >>> dost_age
# {'Dipu': 20, 'nirbhay': 23}
       


       #to find the squate fo the range of the number;
#        squ = {x:x**2 for x in range(5)} 
# >>> squ
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}