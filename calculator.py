#A simple calculator app
print ("""What our app does
1. Addition
2. subtraction
3. Multiplication
4. Division
5. Exponential""")

print ("Enter two numbers to add: ")
first_number = float( input("First Number:"))
second_number = float(input("Second Number:"))
sum = ((first_number + second_number))
print (f"{first_number} + {second_number} is {sum:.2f}")

print ("Enter two numbers to subtract: ")
first_number = float( input("First Number:"))
second_number = float(input("Second Number:"))
sub = first_number - second_number
print (f"{first_number} - {second_number} is {sub:.2f}")
 
print ("Enter two numbers to multiply: ")
first_number = float( input("First Number:"))
second_number = float(input("Second Number:"))
mul = first_number * second_number
print (f"{first_number} * {second_number} is {mul:.2f}")


print ("Enter two numbers to divide: ")
first_number = float( input("First Number:"))
second_number = float(input("Second Number:"))
div = first_number / second_number
print (f"{first_number} / {second_number} is {div:.2f}")


print ("Enter two numbers to get exponential: ")
first_number = float( input("First Number:"))
second_number = float(input("Second Number:"))
exp = first_number ** second_number
print (f"{first_number} ** {second_number} is {exp:.2f}")
