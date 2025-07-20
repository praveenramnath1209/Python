diction = {
    "UXX1":{"Name":"Alice","Score":9},
    "UXX2":{"Name":"Bob","Score":8},
    "UXX3":{"Name":"Max","Score":7},
    "UXX4":{"Name":"Hamilton","Score":6},
}

print("\n------------Student Details------------\n")
for k,v in diction.items():
    print(f"Student ID: {k}")
    print(f"Student Name : {v['Name']}")
    print(f"Student Mark: {v['Score']}\n")
print("\n----------------------------------------")