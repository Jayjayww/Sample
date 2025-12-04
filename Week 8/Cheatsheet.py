# import pandas as pd

# data = {
#     'Temperature': [23, 22, 12, 32, 14, 20, 22, 22, 22, 21],
#     'Movement': [1, 0, 1, 1, 1, 1, 0, 0, 0, 1]
# }

# df = pd.DataFrame(data)
# print(df)

# plt.figure(figsize=(10,5))
# plt.plot(df['Temperature'], label="Temperature")
# plt.plot(df['Movement'], label="Movement")
# plt.xlabel('Time')
# plt.ylabel('Value')
# plt.legend()
# plt.show()

#########################################################

# import turtle

# # from turtle import Screen
# # turtle_screen = Screen()

# # from turtle import *
# # turtle_Screen = Screen()

# sipi = turtle.Turtle() # Luo uusi olio eli Turtle instanssi
# sipi.shape("turtle") # Metodi
# sipi.color("green") # Metodi
# sipi.forward(100) # Metodi

# turtle_screen = turtle.Screen() # Luo uusi ikkuna-olio eli instanssi
# turtle_screen.exitonclick() # Metodi

from lab_student import LABStudent
    
John = LABStudent("John", 32, "Computer science")
Jane = LABStudent("Jane", 25, "Physics")


print(John.Introduce())
print(Jane.study())