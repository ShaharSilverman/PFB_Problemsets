#!/usr/bin/env python

#Question_1:
my_favorite_things = {}
my_favorite_things['book'] = 'The beautiful cure'
my_favorite_things['song'] = 'imagine'
my_favorite_things['tree'] = 'oak'


#Question_2:
print(my_favorite_things['book'])

#Question_3:
fav_thing = 'book'
print(my_favorite_things[fav_thing])

#Question_4:
print(my_favorite_things['tree'])

#Question_5:
my_favorite_things['organism'] = 'mouse'
#fav_thing = 'organism'
#print(my_favorite_things[fav_thing])

#Question_6:
for key in my_favorite_things:
  print("the key name is " + key)

#fav_thing = input("choose your favorite thing: ")
#if fav_thing.find("\n") == -1:
#  print(my_favorite_things[fav_thing])

#work on a way to add a key that's not in the dictionary 

#Question_7:
my_favorite_things['organism'] = 'bacteria'

#Question_8:

fav_thing = input("choose your category: ")
my_favorite_things[fav_thing] = input("choose you favorite thing: ")
print(my_favorite_things)


#Question_9:
for key in my_favorite_things:
  print (key)
  print(my_favorite_things[key])


  
  











  

