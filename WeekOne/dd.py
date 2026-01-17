age = int(input("Please enter your age:"))
has_id = input("Do you have an ID? (yes/no): ").strip().lower()
if age >=22 and has_id == "yes":
    print("You can enter the club.")
else: 
    print("You cannot enter the club.")