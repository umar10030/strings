#lets check the datatypes of different values

a = 5
print("type of a:",type(a))

b=2.5
print( "type of b:",type(b))

c= "coding"
print("type of c:",type(c))

d = True
print("type of d:",type(d))

#activity 2

# assing diffrent variables
name = "Alice"
age = 30
is_student = False
height = 5.5

# printing different variables and their types

print("name:", name)
print("type of name:", type(name))

print("age:", age)
print("type of age:", type(age))

print("is_student:", is_student)
print("type of is_student:", type(is_student))

print("height:", height)
print("type of height:", type(height))

#type casting to convert one data type to another

print("\n after type casting...")
age = str(age)
print(age)
print("type of age after type casting:", type(age))
height = int(height)
print(height)
print("type of height after type casting:", type(height))

# activity 3
# string operations

text = str(input("Enter a string: "))
revtext = text[::-1]
text = revtext
print("Reversed string:")
print(text)