#function to add two numbers
def add(x,y):
    return x + y
#function to substract two numbers
def substract(x,y):
    return x - y

#function to multiply two numbers
def prod(x,y):
    return x * y

#function to divide two numbers
def div(x,y):
    if(y == 0):
        return "Error! Division by Zero is not allowed"
    else:
        return x / y
    

print("Select Operation: ")
print("1. Add")
print("2. Substract")
print("3. product")
print("4. division")

while True:
        #Take the input from user
    choice = input("Enter choice(1/2/3/4): ")

    if choice in ['1','2','3','4']:
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))

        if choice == "1":
             print(f"{num1} + {num2} = {add(num1,num2)}")
        if choice == "2":
            print(f"{num1} + {num2} = {substract(num1,num2)}")
        if choice == "3":
            print(f"{num1} + {num2} = {prod(num1,num2)}")
        if choice == "4":
            print(f"{num1} + {num2} = {div(num1,num2)}")

        #option to exit the loop
    next_calculation = input("Do you want to perform another calculation? (y/n): ")
    if next_calculation != 'y':
        break

print("Exiting Calculator. GOODBYE")