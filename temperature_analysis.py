# Name: Kalaivani
# Roll Number: iitp_aimltn_2602650
# Assignment: Python Loops & Automation - Subjective Question

print("===== Task 1: Find Maximum and Minimum =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]
high_temp = temperatures[0]
low_temp = temperatures[0]
for temp in temperatures: 
    if(temp > high_temp):
        high_temp = temp
    elif(temp < low_temp):
        low_temp = temp

print(f"Highest Temperature: {high_temp}°C")
print(f"Lowest Temperature: {low_temp}°C")


print("\n===== Task 2: Count Hot Days =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]

hot_days = 0
for temp in temperatures:
    if(temp <= 30):
        continue
    hot_days +=1

print(f"Hot Days (>30°C): {hot_days}")


print("\n===== Task 3: Alert System =====")
temperatures = [28, 32, 35, 40, 31, 33, 30]

hot_days = 0
days = 0
for day, temp in enumerate(temperatures,start=1):
    if(temp == 40):
        days = day
        break
    elif(temp > 30):
        hot_days +=1

print(f"Hot Days before alert: {hot_days}")
print(f"Alert! Extreme temperature 40°C detected on Day {days}")