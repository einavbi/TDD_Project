def calculate_bmi(height,weight):
    if weight=='0' or height=='0':
        return
    elif not(height.isnumeric()) or not(weight.isnumeric()):
        return
    elif float(height)<0 or float(weight)<0:
        return
    height_m = float(float(height) / 100)
    BMI = float(weight) / ((height_m) * (height_m))
    return float(BMI)

def bmi_check(BMI):
    if BMI==None:
        return 'wrong input'
    elif BMI<18.5:
        return 'Underweight'
    elif 18.5<BMI<24.9:
        return 'OK'
    elif 25<BMI<29.9:
        return 'overweight'
    elif 30<BMI<34.9:
        return 'obesity'
    elif 35<BMI:
        return 'Severe obesity'


weight=input("enter your weight")
height=input("enter your height- in M, not in X.XX form")
BMI=calculate_bmi(height,weight)
print(bmi_check(BMI))
