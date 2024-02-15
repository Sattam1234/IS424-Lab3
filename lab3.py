''''
solve num 1


x={}
f=False
print("Welcome to the dictionary storage system. If you want to exit the system")
print()
while f==False:
    employees=input("Please enter employee name ")
    print()
    salaries=input("Please enter salaries ")
    x[employees]=salaries
    m=input("Do you want to stay? Yes/No ")
    if m=="No":
        f= True
print()
print(x)
print()
print("Thank you for using the storage system ")
'''''

#----------------------------------------------------------------------------------------
''''
solve num 2

numbers = []

for i in range(10):
    print()
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
print()
print(f"The largest number is {largest}")
'''''

#----------------------------------------------------------------------------------------

'''''
solve num 3


celsius = float(input("Enter the temperature in Celsius: "))

fahrenheit = 9/5 * celsius + 32

print(f"The equivalent temperature in Fahrenheit is {fahrenheit} degrees.")

'''''
'''''
number = int(input("Enter a number: "))

for i in range(1, 11):
    product = number * i
    print(f"{number} * {i} = {product}")
'''''

#----------------------------------------------------------------------------------------

'''''

solve num 4


number = int(input("Enter a number: "))

for i in range(1, 11):
    product = number * i
    print(f"{number} * {i} = {product}")
'''''


#----------------------------------------------------------------------------------------


'''''

solve num 5


x = int(input("Enter a number of repetitions "))

def repeat(n):
    def decorator(func):
        def wrapper():
            for i in range(n):
                func()
        return wrapper
    return decorator

@repeat(x)
def hello():
    print('Hello')

hello()

'''''






























