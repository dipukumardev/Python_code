d = {1:"dipu", 2:"kumar", 3:"aditya", 4:"singh"}
print(d)
dk = sorted(d.keysc())
print(dk)
dv= sorted(d.values())
print(dv)
ds = sorted(d.items(),key= lambda X:X[0])
print(ds)
ds1 = sorted(d.items(), key=lambda Y:Y[1])
print(ds1)
dr = {v:k for k,v in d.items()}
print(dr)