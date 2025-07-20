data = {
    "Name":"Shanks",
    "Age" :20,
    "Mark1":83,
    "Mark2":90,
    "Mark3":99
}

for key,value in data.items():
    print(f"{key}:{value}")

print(data["Name"])
print(data.get("Shanks"))

#update values
data.update({"Age":19})
for key,value in data.items():
    print(f"{key}:{value}")

#delete
data.pop("Mark2")
for key,value in data.items():
    print(f"{key}:{value}")
