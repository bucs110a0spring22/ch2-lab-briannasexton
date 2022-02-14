import random
#Part A
weeks = 16
print ("Weeks:", weeks)
print(weeks, type(weeks))
classes = 5
print("Classes:", classes)
print (classes, type(classes))
tuition = 6000
print("Tuition:", tuition)
print(tuition, type(tuition))
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)
print(cost_per_week, type(cost_per_week))
classes_per_week = 2
print("Classes per week:", classes_per_week)
print(classes_per_week, type(classes_per_week))
cost_per_class = (cost_per_week / classes_per_week)
print("Cost per class:", cost_per_class) 
print(cost_per_class, type(cost_per_class))
print("Have a nice day!")

#Part B
#random.randrange(1,9)
listcolors= ["red", "orange", "yellow", "green", "blue", "purple", "pink", "black", "white"]


random.choice(listcolors)
your_color = random.choice(listcolors)
print ("You have the color:",(your_color))