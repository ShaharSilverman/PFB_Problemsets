#!/usr/bin/env python3
import sys
## first script writing variable values and printing them
#my_name = "Shahar"
#my_favorite_color = "Purple"
#my_favorite_activity = "Reading"
#my_favorite_animal = "Cat"

#print(f"my name is: {my_name} my favorite color is: {my_favorite_color} my favorite activity is: {my_favorite_activity} my favorite animal is: {my_favorite_animal}")

## second task - now I can feed the system with different values through the command line
my_name = sys.argv[1]
my_favorite_color = sys.argv[2]
my_favorite_activity = sys.argv[3]
my_favorite_animal = sys.argv[4]

## use \n within the string to get the text in seperate lines
print("my name is:",  my_name, "\n my favorite color is:",  my_favorite_color, "\n my favorite activity is:",  my_favorite_activity, "\n my favorite animal is:",  my_favorite_animal)

