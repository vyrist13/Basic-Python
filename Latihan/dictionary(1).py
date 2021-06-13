thisdict={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
print(thisdict)

x=thisdict["model"]

thisdict={
    "Brand":"Ford",
    "Model":"Mustang",
    "Year":1964
}
thisdict["year"]=2018

for x in thisdict:
    print (x,"=",thisdict[x])