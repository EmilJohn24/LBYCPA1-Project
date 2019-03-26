import os


def signup():
    input1 = input("Enter Username: ")
    input2 = input("Enter Password: ")

    users = open('user.txt', 'a')
    users.write("\n{0},{1}".format(input1, input2))


def login(user_info):
    us_input = input("Enter Username: ")
    pw_input = input("Enter Password: ")
    users = open('user.txt', 'r').readlines()
    userbase = dict()
    for user in users:
        data = user.split(',')
        userbase[data[0]] = data[1]

    if (us_input, pw_input) in userbase.items():
        user_info['user'] = us_input
        user_info['pw'] = pw_input
    else:
        print("Invalid login")
        login(user_info)


def calculatebmi(height, weight):
    height = float(height)
    weight = float(weight)
    return (weight / height ** 2)


def calculatebmr(sex, weight, height, age):
    height = float(height)
    weight = float(weight)
    age = int(age)
    if sex == 'M':
        BMR = (10 * weight) + (6.25 * height) - (5 * age) + 5
    elif sex == 'F':
        BMR = (10 * weight) + (6.25 * height) - (5 * age) - 161
    else:
        raise RuntimeError
    return BMR

def convert_to_metric(val: str):
    initial_val = ""
    unit = ""
    for c in val:
        if c.isdigit():
            initial_val += c
        elif c.isalpha():
            unit += c

    initial_val = float(initial_val)

    if unit == "lb":
        return initial_val / 2.2 # to kilograms

    elif unit == "ft": # feet
        return initial_val / 3.28084 # to meters

    elif unit == "in":
        return initial_val * 2.54 # to centimeters
    else:
        return initial_val




def welcome(user_info):
    height = convert_to_metric(input("What is your height: "))
    weight = convert_to_metric(input("What is your weight: "))
    sex = input("What is your sex(M/F): ")
    age = input("What is your age: ")
    os.system(
        'start "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" https://www.vertex42.com/ExcelTemplates/Images/body-mass-index-chart.gif')
    print("Use the image as a guide...")
    desiredweight = input("What is your desired weight: ")
    BMR = calculatebmr(sex, weight, height, age)
    user_info['Weight'] = weight
    user_info['Height'] = height
    user_info['Sex'] = sex
    user_info['Age'] = age
    user_info['BMI'] = calculatebmi(height, weight)
    user_info['BMR'] = BMR
    user_info['DesiredWeight'] = desiredweight


print("Welcome to FITBEST")
print("best best best")
user_info = {'user': '', 'pw': ''}
signup()
login(user_info)
welcome(user_info)
print("Your BMI is: ", user_info['BMI'])
print("Your BMR is: ", user_info['BMR'])




