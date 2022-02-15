#print("20 days is " + str(50) + " minutes")
#print(f"20 days are {50} minutes")

calculation_to_units =  24
name_of_unit = "hours"

def days_to_units(num_of_days):
    return f"{num_of_days} days is {num_of_days * calculation_to_units} {name_of_unit}"
    

def validate_and_execute():
    if user_input.isdigit():
        user_input_number = int(user_input)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
        elif user_input_number == 0:
            print("you entered 0, plese enter positive")

    else: 
        print("your input is not a valid number")



user_input = input("user, enter a number and I will convert to hours\n")
validate_and_execute()

