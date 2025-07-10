name = input("Enter your name: ")
age = int(input("Enter your age: "))
is_student = int(input("Are you a student? (1 for Yes, 0 for No): "))
num_seats = int(input("Enter number of seats you want: "))

available_seats = ["A1", "A2", "A3", "A4", "A5", "B1", "B2", "B3", "B4", "B5"]
print("Available seats:", available_seats)

selected_seats = []
for i in range(num_seats):
    seat = input(f"Enter seat {i+1} you want to book: ")
    if seat in available_seats:
        selected_seats.append(seat)
        available_seats.remove(seat)
    else:
        print("Seat not available, choose a different one.")
        seat = input(f"Enter seat {i+1} you want to book: ")
        if seat in available_seats:
            selected_seats.append(seat)
            available_seats.remove(seat)

price_per_seat = 190
total_amount = price_per_seat * num_seats

if is_student == 1 or age > 60:
    discount = 0.10 * total_amount
    total_amount = total_amount - discount

print("\n--- Booking Summary ---")
print("Name:", name)
print("Age:", age)
print("Number of Seats:", num_seats)
print("Selected Seats:", selected_seats)
print("Total Amount to Pay: ₹", total_amount)
