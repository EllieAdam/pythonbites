rain_speed = 8
if rain_speed < 5:
    print("Just a Scotch mist")
else:
    print("It's a real Cow-quaker out there")


#-----------
Question2:
Rock, paper, python gam:
Answer
computer_choice = 'rock' or 'paper' or 'python'
user_choice = input("Enter rock, paper, or python:\n")
if computer_choice == user_choice:
    print('TIE')
else:
    print('You lose :( Computer wins :D')


#-------More detailed
computer_choice = 'rock'
user_choice = input("Enter rock, paper, or python:\n")

if computer_choice == user_choice:
    print('TIE')
elif user_choice == 'rock' and computer_choice == 'python':
    print('WIN')
elif user_choice == 'paper' and computer_choice == 'rock':
    print('WIN')
elif user_choice == 'python' and computer_choice == 'paper':
    print('WIN')
else:
    print('You lose :( Computer wins :D')

#------------
Q: remove item from list
Answer

performances = ['Ventriloquism', 'Amazing Acrobatics', 'Snake Charmer', 'Enchanted Elephants', 'Bearded Lady', 'Tiniest Man']
performances.remove('Bearded Lady')
performances.remove('Tiniest Man')
print(performances)

Q: Add key and values to current dictionary

Answer:
performances = {'Ventriloquism':'9:00am', 'Snake Charmer': '12:00pm'}
performances['Amazing Acrobatics'] = '2:00pm'
performances['Enchanted Elephants'] = '5:00pm'
print(performances)

Q:
Showtime??

Answer:
performances = {'Ventriloquism':'9:00am', 
               'Snake Charmer': '12:00pm', 
               'Amazing Acrobatics': '2:00pm', 
               'Bearded Lady':'5:00pm'}
showtime = performances.get('Bearded Lady')
if showtime == None:
    print("Performance doesn't exist")
else:
    print("The time of the Bearded Lady show is ", showtime)


 Q:print welcome vertically


Answer
word = 'Welcome!'
letter = i
for letter in word:
    print(letter)

Q:print random ticket??

Answer:
import random
import random
for i in range(5):
    ticket = random.randint(1,53)
    print(ticket)


    Answer2: This pass

import random
for i in range(5):
     print(random.randint(1,53))


 Q: fix spacing
 Answer:

 performances = {'Ventriloquism':'9:00am', 
                'Snake Charmer': '12:00pm', 
                'Amazing Acrobatics': '2:00pm', 
                'Enchanted Elephants':'5:00pm'}
for name, time in performances.items():
    print(name, ': ', time, sep='')

Q:
We want to create a "guess the number" game for our fortune-teller robot. 
If you guess the random number between 1 and 10, you win a crystal ball!

Answer:
import random

num = random.randint(1,10)

# Add your code here
guess = int(input('Guess a number between 1 and 10'))
while guess != num:
    guess = int(input('Guess again'))
    
print('You win!') 

 Q:

 Answer:

guess = int(input('Guess a number between 1 and 10'))
times = 1

while guess != num:
    guess = int(input('Guess again'))
    times = times + 1
    if times == 3:
        break

if guess == num:
      print('You win!')
else:
    print('You lose! The number was ', num)

Q:Avg function


Answer:

def average(number):
	total = 0
	for num in mumbers:
		total = total + num
	avg = total/len(numbers)
	return avg

prices = [2.5, 4, 5, 5.5, 6]

result = average(prices)

print(result)

Q: 
The fortune-teller robot wants us to create a function for generating lottery ticket numbers.
 We will take the code we already created in Level 2, but instead of printing out the numbers
  one by one, our function will return a list of the numbers.

Answer:
import random
def lotto_numbers():
      lotto_nums = []
      for i in range(5):
          lotto_nums.append(random.randint(1, 53)) 
      return lotto_nums
  
Q:
lets create lotto_nums

Ans:
import random

def lotto_numbers():
    lotto_nums = []
    for i in range(5):
        lotto_nums.append(random.randint(1, 53)) 
        
    return lotto_nums

numbers = lotto_numbers()
print(numbers)
#----------
Explanation
#---------
Main function


def average(numbers):
	total = 0
	for num in list:
		total = total + num
	avg = total/len(numbers)
	return avg

def main()
	prices = [23, 34, 56, 67,]
	result = average (prices)
	print(result)
main()

#-----------
def main():
    # code in the main function goes here
    numbers = lotto_numbers()
    print(numbers)
main()
#------------

def bill_total(orders, menu):
	menu = 0

	for order in orders:
		total += menu[order]
	return total

#-------------
def print_menu(menu):
	...
def get_order(menu):
	...

def main():
	menu = {'k spam': .50, 'b spam': .60, 'h spam': 2.2}
	print_menu(menu)
	orders = get_order(menu)
	total = bill_total(orders, menu)
	print("you ordered:", order, "your total is: $", formate(total, '.2f'), sep='')
	main()

	#-----------
	Q: "guess the number" game into its own function.
	Ans:
import random

def guessing_game():
    num = random.randint(1, 10)

    guess = int(input('Guess a number between 1 and 10'))
    times = 1

    while guess != num:
        guess = int(input('Guess again'))
        times += 1
        if times == 3:
            break

    if guess == num:
        print('You win!')
    else:
        print('You lose! The number was', num)


    

def lotto_numbers():
    lotto_nums = []
    for i in range(5):
        lotto_nums.append(random.randint(1, 53)) 
    
    return lotto_nums
  
def main():
    numbers = lotto_numbers()
    print(numbers)
    guessing_game()

main()

Q:
We want the fortune-teller robot to be able to ask the user if they want 
to play the guess the number game or if they want lottery numbers.
Ans:
import random

def guessing_game():
    num = random.randint(1, 10)

    guess = int(input('Guess a number between 1 and 10'))
    times = 1

    while guess != num:
        guess = int(input('Guess again'))
        times += 1
        if times == 3:
            break

    if guess == num:
        print('You win!')
    else:
        print('You lose! The number was', num)
    

def lotto_numbers():
    lotto_nums = []
    for i in range(5):
        lotto_nums.append(random.randint(1, 53)) 
    
    return lotto_nums
  
def main():
    answer = input('Do you want to get lottery numbers (1) or play the game (2) or quit (Q)?' )

    numbers = lotto_numbers()
    if answer == '1':
        print(numbers)
    elif answer == '2':
        guessing_game()
    else:
        print('Toodles!')
    
main()

#---------
Q:

performances = {'Ventriloquism':       '9:00am', 
                'Snake Charmer':       '12:00pm', 
                'Amazing Acrobatics':  '2:00pm', 
                'Enchanted Elephants': '5:00pm'}

schedule_file = open('schedule.txt', 'w')

for key, val in performances.items():
  schedule_file.write( key + ' - ' + val + '\n')  
schedule_file.close()

#---------
Q:

schedule_file = open('schedule.txt', 'r')
for line in schedule_file:
    print(line)
schedule_file.close()

#----------
Q:

schedule_file = open('schedule.txt', 'r')
for line in schedule_file:
    (show, time) = line.split(' - ') 
    
    print(show, time)
schedule_file.close()
#---------
Q:

performances = {(show, time)}

schedule_file = open('schedule.txt', 'r')

for line in my_file:
    (show, time) = line.split(' - ')
    performances[show] = time.strip()
    print(show, time)
    

schedule_file.close() 
print(performances)

#--------
Q:

performances = {}
try:
    schedule_file = open('schedule.txt', 'r')
except FileNotFoundError as err:
    print(err)   
for line in schedule_file:
    (show, time) = line.split(' - ')
    performances[show] = time

schedule_file.close()
print(performances)

#----------
Q:

Jason requests


import requests
  
url = "http://api.openweathermap.org/data/2.5/weather?q=Orlando,fl&units=imperial&appid=2de143494c0b295cca9337e1e96b00e0"
request = requests.get(url)

weather_json = request.json()
print(weather_json)
main_weather = weather_json['main']
temp = main_weather['temp']
print("The Circus's current temperature is ", temp)

#-----------
Q:


importing files

import weather
def main():
    weather.current_weather()

dmain()
main()

#----------
Q:

import requests
def current_weather():
    url = "http://api.openweathermap.org/data/2.5/weather?q=Orlando,fl&units=imperial&appid=2de143494c0b295cca9337e1e96b00e0"
    r = requests.get(url)

    weather_json = r.json()
    print(weather_json)

    min = weather_json['main']['temp_min']
    max = weather_json['main']['temp_max']

    print("The circus' forecast is", min , "as the low and", max, "as the high")
#--------------------
Q:

import time
import webbrowser

total_breakes = 3
break_count = 0

print("This progra srarted on "+time.ctime())
while(break_count < total_breakes):
	time.sleep(2*60*60)
	webbrowser.open("https://www.youtube.com/watch?v=YQHsXMglC9A")
	break_count += break_count

#--------------------
Q:How to organize jumbled files and reveal secret message.

Ans.
import os

def rename_file ():
	# (1) get file names from a folder
	file_list = os.listdir(r"C:\folder")
	#print(file_list)
	saved_path = os.getcwd()
	print ("Current Working Directory is "+saved_path)
	os.chdir(r"C:\folder")
	#(2) for each file, rename filename

	for file_name in file_list:
		print ("Old Name - "+file_name)
		print ("New Name - "+file_name.translate(None, "0123456789"))
		os.rename(file_name, file_name.translate(None, "0123456789"))
	os.chdir(saved_path)
rename_files()


#--------------------
Q: Draw square in python

Answer:

import turtle

def draw_shapes():
	window = turtle_Screen()
	wndow.bgcolor("blue")

	draw_square()
	draw_circle()
	draw_triangle()

	window.exitonclick()


def draw_square():	
	brad = turtle.Turtle()
	brad.shape("arrow")
	brad.color("red")
	brad.speed(10)

	i = 0
	while( 1 < 4):
		brad.forward(100)
		brad.right(90)
		i += i

def draw_circle():

	ann = turtle.Turtle()
	ann.shape("circle")
	ann.color("pink")
	ann.circle(100)

	

def draw_triangle():

	ben = turtle.Turtle()
	ben.shape("triangle")
	ben.color("green")
	ben.speed(30)

	i = 0
	while( i < 3):
		ben.forward(60)
		ben.left(120)
		i = i + 1
	

draw_shapes()

#--------------------
Q:


import turtle

def draw_square():
	window = turtle.Screen()
	window.bgcolor("pink")

	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("red")
	brad.speed(10)

	for i in range(0, 4):
	    brad.forward(100)
	    brad.right(90)

def draw_circle():
	abee = turtle.Turtle()
	abee.shape("arrow")
	abee.color("blue")
	abee.circle(100)

def draw_triangle():
	rick = turtle.Turtle()
	rick.shape("arrow")
	rick.color("blue")

	for i in range(0, 3):
	    rick.forward(200)
	    rick.left(120)

draw_square()
draw_circle()
draw_triangle()
#--------------------
Q:
#--------------------
Q:
#--------------------
Q:

#--------------------
Q:

#--------------------
Q:

#--------------------
Q:

#--------------------
Q:

#--------------------
Q:

#--------------------
Q:

#--------------------
Q:

#--------------------
Q:

#--------------------
Q:

#--------------------
Q:

#--------------------
Q:

#--------------------
Q:

#--------------------
Q:

#--------------------
Q:

#--------------------
Q:

#--------------------
Q:

#--------------------
Q:

#--------------------
Q:

#--------------------
Q:

#--------------------
Q:

#--------------------
Q:

#--------------------
Q:

#--------------------
Q:

#--------------------
Q:

#--------------------
Q:

#--------------------
Q:




