

print("I am the age wizard. What is your name?.")
name = input()

print("What is your age?")
age = input()

#print(type(age))

age2 = int(age)

if age2 >= 99:
    print("whoa you're old as hek")
elif age2 > 12 and age2 <20:
    print("ayyyy same")
else:
    print("You seem younger than 100")

print("I'm gonna tell you something about you...")
print("Your name is %s and your age is %d." %(name, age2))
