#Assignment 1 for One Month Pyhon

import random

#Input from server
server_name = input("Hello Kick Ass Steak House servant, please enter your name.\n")
sub_total = float(input(f"Thank you {server_name}, please enter the subtotal of the patron's meal without the dollar sign ($)\n"))
rounded_subtotal = float(f"{sub_total:.2f} \n")

server_passover = input(f"Great {server_name}.  Now hit [ENTER] and pass the device to the patron\n")

#Input from patron
patron_name = input("We hope you enjoyed your meal at Kick Asss Steak House, can I please get your name?\n")

tip_selection = int(input(f"Thank you {patron_name}. The subtotal for your meal is ${rounded_subtotal}.\n" 
	"Please enter your tip percentage (15, 18, 20): \n" 
	"15 - average service\n"
	"18 - good service\n"
	"20 - fantastic service\n"))

#Convert inputs to manipulate mathematically
converted_subtotal = float(rounded_subtotal)	 
total = (converted_subtotal * ( 1 + tip_selection /100))

salutation = ["Thank you for visiting us",
	"We hope to see you again soon",
	"Have a safe drive home"]

random_salutation = random.choice(salutation)

#Final messsage for patron showing total with tip
print(f"{random_salutation} {patron_name}.\n")
print(f"Your total with tip is ${total:.2f} \n")

thoughts = ["Man, what a cheapskate.  Hope they don't come back!",
	"Interesting tip, looks like they're celebrating big tonight!",
	"That person just gave me their number.  Going to give them a call after my shift for some - Netflix and Chill!"]

#Bonus thoughts from waiters and waitress at Kick Ass Steak House
random_thoughts = random.choice(thoughts)

see_thoughts = input("BONUS: Hit [ENTER] to see what our waiters & waitresses really thought of their patrons\n")
print(random_thoughts)
