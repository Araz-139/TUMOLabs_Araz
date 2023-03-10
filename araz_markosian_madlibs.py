# -*- coding: utf-8 -*-
"""araz_markosian_madlibs.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LNAN7-ss2ppAogz9uvQbe319d0Dtf_CH
"""

# define a function to run the 1st template scenario:
def story_1():
  # ask to input words for template_1
  number = input("Input a number: ")
  number_2 = input("Input a 2nd number: ")
  measure_of_time = input("Input a time duration: ")
  mode_of_transportation = input("Input a mode of transportation: ")
  adjective = input("Input an adjecive: ")
  adjective_2 = input("Input a 2nd adjective: ")
  adjective_3 = input("Input a 3rd adjective: ")
  noun = input("Input a plural noun: ")
  noun_2 = input("Input a 2nd noun in plural: ")
  noun_3 = input("Input a 3rd noun: ")
  noun_4 =  input("Input a 4th noun: ")
  color = input("Input a color: ")
  part_of_body = input("Input a body part's name in plural: ")
  part_of_body_2 = input("Input another body part name: ")
  verb = input("Input a verb: ")
  silly_word = input("Input a silly word ;): ")

  # define the template_1
  template_1 = f"""
  It was about {number} 
  {measure_of_time} ago when 
  I arrived at the hospital in a/an {mode_of_transportation}. 
  The hospital is a/an {adjective} place, 
  there are a lot of {adjective_2} {noun} here. 
  There are nurses here who have {color} {part_of_body}. 
  If someone wants to come into my room I told them that they have to {verb} first. 
  I’ve decorated my room with {number_2} {noun_2}. 
  Today I talked to a doctor and they were wearing a {noun_3} on their {part_of_body_2}. 
  I heard that all doctors {verb} {noun_4} every day for breakfast. 
  The most {adjective_3} thing about being in the hospital is 
  the {silly_word} {noun} !
  """

  # print personalized template_1
  print(template_1)

# define a function to run the second scenario
def story_2():
  # ask to inmput words for template_2
  person_name = input("Input a person's name: ")
  noun = input("Input a noun: ")
  noun_2 = input("Input a second noun: ")
  adjective_feeling = input("Input an adjective that describes a feeling: ")
  adjective_feeling_2 = input("Input a second adjective that describes a feeing: ")
  adverb_ly = input("Input an adverb ending with 'ly': ")
  verb = input("Input a verb: ")
  verb_2 = input("Input a second verb: ")
  verb_ing = input("Input a verb that ends with 'ing': ")
  animal = input("Input an animal name: ")
  color = input("Input a color: ")
  number = input("Input a number: ")
  measure_of_time = input("Input a duration (length) of time: ")
  silly_word = input("Input a silly word: ")

  # define template_2
  template_2 = f"""
  This weekend I am going camping with {person_name}. 
  I packed my lantern, sleeping bag, and {noun}. 
  I am so {adjective_feeling} to {verb} in a tent. 
  I am {adjective_feeling_2} 
  we might see a(n) {animal}, 
  I hear they’re kind of dangerous. 
  While we’re camping, we are going to hike, fish, and {verb_2}. 
  I have heard that the {color} lake is great for {verb_ing}. 
  Then we will {adverb_ly} hike through the forest 
  for {number} {measure_of_time}. 
  If I see a {color} {animal} while hiking, 
  I am going to bring it home as a pet! 
  At night we will tell {number} {silly_word} stories and roast {noun_2} around the campfire!!
  """

  # print personalized template_2
  print(template_2)

# define a function to run the 3rd scenario using template_3
def story_3():
  # words for template_3
  person_name = input("Input a person's name: ")
  noun = input("Input a noun: ")
  noun_2 = input("Input a 2nd noun: ")
  noun_3_plural = input("Input a 3rd noun in plural: ")
  noun_4 = input("Input a 4th noun: ")
  adjective = input("Input an adjective: ")
  adjective_2 = input("Input a 2nd adjective: ")
  adjective_3 = input("Input a 3rd adjective: ")
  adjective_4 = input("Input a 4th adjective: ")
  adjective_5 = input("Input a 5th adjective: ")
  noun_4_plural = input("Input a 4th noun in plural: ")
  adjective_feeling = input("Input an adjective that describes feeling: ")
  adjective_feeling_2 = input("Input a 2nd adjective that describes a feeling: ")
  verb = input("Input a verb: ")
  verb_2 = input("Input a 2nd verb: ")
  verb_ing = input("Input a verb that ends with ing: ")
  animal = input("Input an animal name: ")
  magical_creatures = input("Input the name of magical creatures (plural): ")
  magical_creatures_2 = input("Input other magical creatures (plural): ")
  color = input("Input a color: ")
  adverb_ly = input("Input an adverb ending with ly : ")
  number = input("Input a number: ")
  room = input("Input a room name: ")
  place = input("Input a place name: ")
  measure_of_time = input("Input a measure of time: ")
  silly_word = input("Input a silly word: ")

  # define template_3
  template_3 = f"""
   Dear {person_name}, 
   I am writing to you from a {adjective} castle in an enchanted forest. 
   I found myself here one day after going for a ride on a {color} {animal} in {place}. 
   There are {adjective_2} {magical_creatures} 
   and {adjective_3} {magical_creatures_2} here! 
   In the {room} there is a pool full of {noun}. 
   I fall asleep each night on a {noun_2} of {noun_3_plural} 
   and dream of {adjective_4} {noun_4_plural}. 
   It feels as though I have lived here for {number} {measure_of_time}. 
   I hope one day you can visit, although the only way to get here now is {verb_ing} on a {adjective_5} {noun_4}!!
  """
  # print personalized template_3
  print(template_3)

# import the random module
import random

# define a function to run a story adventure based on the user's choice
def adventure():
  if user_choice == "1":
    story_1()
  elif user_choice == "2":
    story_2()
  elif user_choice == "3":
    story_3()

# define a list of available choices for the random module and other purposes...
choices_list = ["1", "2", "3"]

# The game starts here - prompt the user to select a template
user_name = input("Hello there! What is your name? ")
user_choice = (input(f"""Well {user_name}, you have discovered an enchanted door! 
To open the door and start your adventure, 
input one of the following magical words:

1
2
3
random

""")).lower() 

# conditionals based,  on the user's choice
while True:
  if user_choice in choices_list:
    # run the adventure function
    adventure()
    break
  elif user_choice == "random":
    # assign a random choice to the user_choice variable and run the adventure function
    user_choice = random.choice(choices_list)
    adventure()
    break
  else:
    #prompt the user again until they give a valid magical word
    user_choice = (input("""Sorry, that is not a valid magical word. 
    Please, input one of the following magical words without spaces:

    1
    2
    3
    random

    """)).lower()

