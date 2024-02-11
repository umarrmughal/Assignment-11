#  1 Calorie counter
age = int(input("Enter your age:"))
weight = int(input("Enter your weight:"))
activity_level = input("Enter your activity level as (setendary,moderate and active):").lower()

base_calorie_per_KG = 24

setendary_multiplier = 1.2
moderate_multiplier = 1.55
active_multiplier = 1.9

bmr = base_calorie_per_KG * weight

if activity_level == 'setendary':
    print("your calorie goal is:",bmr * setendary_multiplier)
elif activity_level == 'moderate':
    print("your calorie goal is:",bmr * moderate_multiplier)
elif activity_level == 'active':
    print("your calorie goal is:",bmr * active_multiplier)
else:
    print("invalid activity level please choose activity level from (setendary,moderate and active)")

#  2 sleep tracker
bed_time = int(input("Enter the bed time "))
wake_up_time = int(input("Enter the wake up time  "))

duration = wake_up_time - bed_time

if duration < 8:
    print("your duration is:",duration,"You need proper sleep")
elif duration > 8:
    print("your duration is:",duration," you should watch your sleep timing")
else:
    print("prefect sleep")

#  3 Hydration helper
weight = int(input("enter your weight:"))
hydration_level = input("enter your hydration level as(light,moderate and intense exersice):").lower()

if weight >= 40 and weight <= 59:
    if hydration_level == 'light':
        print("drink 1.5 litre of water")
    elif hydration_level == 'moderate':
        print("drink 1.8 litre of water")
    elif hydration_level == 'intense exersice':
        print("drink 2.1 liter of water")
elif weight >= 60 and weight <= 90:
    if hydration_level == 'light':
        print("drink 2.4 litre of water")
    elif hydration_level == 'moderate':
        print("drink 2.7 litre of water")
    elif hydration_level == 'intense exersice':
        print("drink 3.0 liter of water")
elif weight >= 91 and weight <= 120:
    if hydration_level == 'light':
        print("drink 3.3 litre of water")
    elif hydration_level == 'moderate':
        print("drink 3.5 litre of water")
    elif hydration_level == 'intense exersice':
        print("drink 3.8 liter of water")
elif weight >= 121 and weight <= 145:
    if hydration_level == 'light':
        print("drink 4.1 litre of water")
    elif hydration_level == 'moderate':
        print("drink 4.4 litre of water")
    elif hydration_level == 'intense exersice':
        print("drink 4.7 liter of water")

