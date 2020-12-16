#Single line version, input format = 60, 1.6
# weight, height = eval(input('input your weight in kg and height in m '))
weight = eval(input('Enter your weight in kg '))
height = eval(input('Enter your height in m '))
BMI = weight / (height * height)
print('Your BMI is:{}'.format(BMI))
if BMI < 18.5:
    print('You are too Thin')
elif BMI < 24:
    print('You are Normal')
elif BMI < 28:
    print('You are Overweight')
else:
    print('FAT')