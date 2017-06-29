


print("I'm going to Costco, do you need anything?")
print("Here is my grocery list!")

groceryList = ["kale", "spinach", "strawberries", "raspberries", "tofu"]
#length = len(groceryList)
groceryList.append("almond milk")
#length = len(groceryList)

for x in groceryList:
     print(x)

print ("Do you want to add anything else? y/n")

answer = input()
if answer == ("Yes"):
    print ("What do you want to add")
    groceryAdd = input()
    groceryList.append(groceryAdd)
    print("Is this okay?")
    print(groceryList)
    input()
    if answer == ("Yes"):
        print("Okay, great!")
        exit()
    elif answer == ("No"):
        print ("oh okay!")
        print("Do you want to add anything else?")
        groceryAdd = input()
        groceryList.append(groceryAdd)
        exit()

elif answer == ("No"):
        print ("oh okay!")
        exit()

else:
    print ("okay, thats fine :)")
    print ("Let me know if you change your mind!")
    exit()

#for x in groceryList:
    #print (x)
