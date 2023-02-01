from datetime import datetime

# store the current year
current_year = datetime.now().year

# define a maximum human age
age_limit = 123

# define a minimum year for input
year_limit = current_year - age_limit

# define a dictionary of user types and their age ranges
user_types = {
    "baby": (1, 3),
    "kid": (4, 9),
    "teen": (10, 15),
    "young": (16, 18),
    "adult": (19, 50),
    "old": (51, age_limit)
}

# function to get the user type based on their age
def get_user_type(age):
    # loop through the user types and their age ranges
    for user_type, age_range in user_types.items():
        # check if the user's age is within the current age range
        if age_range[0] <= age <= age_range[1]:
            # If so, return the user type
            return user_type
    # if no user type is found, return "invalid"
    return "invalid"

# function to calculate the user type based on their birth year
def calc_user_type(birth_year):
    # calculate the user's age
    age = current_year - birth_year
    # check if the age is less than or equal to 0
    if age <= 0:
        # if so, return "invalid"
        return "invalid"
    # get the user type based on their age
    user_type = get_user_type(age)
    # check if the user type is "invalid"
    if user_type == "invalid":
        # if so, return an error message
        return f"Error: Invalid birth year. Please enter a year between 1900 and {current_year}."
    # otherwise, return a message indicating the user's age and type
    return f"Your age is {age}, you are a {user_type}."

# start a loop to continuously prompt the user for their birth year
while True:
    # prompt the user for their birth year
    birth_year = input("Please enter your birth year: ")
    try:
        # try to convert the user's input to an integer
        birth_year = int(birth_year)
        # check if the birth year is outside the valid range
        if birth_year < year_limit or birth_year > current_year:
            # if so, return an error message
            print(
                f"Error: Invalid birth year. Please enter a year between {year_limit} and {current_year-1}.")
        else:
            # calculate the user type based on the birth year
            result = calc_user_type(birth_year)
            # print the result
            print(result)
            # break out of the loop
            break
    except ValueError:
        # if the user's input can't be converted to an integer, return an error message
        print("Error: Please enter a valid number for your birth year.")