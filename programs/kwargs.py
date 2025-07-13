def det(**kwargs):
    print("--Student Profile--")
    for key,value in kwargs.items():
        print(f"{key}: {value}")

det(Name="Levi",age = 25 ,city = "Madurai" , hobby = "games")