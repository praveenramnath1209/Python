#Movie_Booking

seats_available = ["a1", "a2", "a3", "a4", "a5", "b1", "b2", "b3", "b4", "b5"]
price = 190
ss = []

n = input("Enter name: ")
a = int(input("Enter age: "))
s = int(input("If you are a student then enter (1), if not enter (0): "))
nn = int(input("Enter number of seats: "))

print("Available Seats:")
print(seats_available)


for i in range(nn):
    seat = input(f"Enter seat {i+1}: ")
    if seat in seats_available:
        ss.append(seat)
        seats_available.remove(seat)
    else:
        print(f"{seat} is not available. Try again.")
        seat = input(f"Enter seat {i+1} again: ")
        ss.append(seat)
        seats_available.remove(seat)


if a>=60 or s == 1:
    total = price * nn
    total  = ((total - (total*0.10)))

print("\n----------Ticket----------")
print("Name:",n)
print("age:",a)
print("Seats:",ss)
print("Amount:",total)
print("------------------------")

