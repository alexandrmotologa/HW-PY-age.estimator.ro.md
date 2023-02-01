from datetime import datetime

current_year = datetime.now().year
BABY = [1, 3]
KID = [4, 9]
TEEN = [10, 15]
YOUNG = [16, 18]
ADULT = [19, 50]
OLD = [51, 999]


def calc_user_type(age):
    if age in list(range(BABY[0], BABY[1])):
        print(f"your age is {age}, you are a baby")
    elif age in list(range(KID[0], KID[1])):
        print(f"your age is {age}, you are kid")
    elif age in list(range(TEEN[0], TEEN[1])):
        print(f"your age is {age}, you are teen")
    elif age in list(range(YOUNG[0], YOUNG[1])):
        print(f"your age is {age}, you are young")
    elif age in list(range(ADULT[0], ADULT[1])):
        print(f"your age is {age}, you are adult")
    elif age in list(range(OLD[0], OLD[1])):
        print(f"your age is {age}, you are old")
    elif age <= 0:
        print(f"your age is very small, you are a little baby")


while True:
    try:
        data_from_user = int(input("Please type your birth year: "))
        if data_from_user >= 1900 and data_from_user <= current_year:
            user_age = current_year - data_from_user
            calc_user_type(user_age)

        else:
            print(
                f"Value error, the range of years allowed from 1900 to {current_year}")

    except:
        print(
            f"Error, Please type your birth year, the range of years allowed from 1900 to {current_year}")