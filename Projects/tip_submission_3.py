# One Month Python Week 1 Assignment

# This script takes an input from the user for a restaurant check in USD.
# After a 1- to 2-sentence description of each tipping rate, 
# it provides a guide on how much a tip of 15%, 18%, and 20% would total.
# It then prompts the user for the rate of tip they wish to leave. 
# Finally, it provides the bill amount, tip amount, and grand total.

import os
os.system('clear')                       # start with a blank screen

########### G A T H E R  B A S I C  I N F O #####################                   

name = input("What is your name? ")
restaurant = input("What is the name of the restaurant? ")
check = float((input("What is the total amount of the check, in U.S. Dollars (example: 18.29)? $")))

########## C A L C U L A T I O N S   F O R   P A R T  I ##############

tip_amt_15 = float( check * 15  / 100 )   # calc 15% tip rate: display in Part I
tip_amt_18 = float( check * 18  / 100 )   # calc 18% tip rate: display in Part I
tip_amt_20 = float( check * 20  / 100 )   # calc 20% tip rate: display in Part I
gt15 = float( check + tip_amt_15 )        # calc Grand Total: display in Part I - 15%
gt18 = float( check + tip_amt_18 )        # calc Grand Total: display in Part I - 18%
gt20 = float( check + tip_amt_20 )        # calc Grand Total: display in Part I - 20%

#################### D I S P L A Y  P A R T  I ##############################

print()
print("===============================================================================")
print(f" Okay, {name}, you say your check at {restaurant} was ${check:.2f}")
print("  so you should decide at which rate you wish to tip.")
print("     Read the following brief guidelines then select your tip rate.")
print(" NOTE: you don't have to pick one of these...you can make your rate anything. ")
print()
print("  15% - Server was slow to arrive, slow with drinks, generally unpleasant")
print()
print("  18% - Server was average in arriving at the table, was average in")
print("        getting out the drinks, forgot something on the order")
print()
print("  20% - Server was quick in all aspects, knew the menu well, refilled")
print( "        drinks without being asked, suggested particular dishes, and")
print("        offered dessert")
print()
print("  Tip & Grand Totals for suggested levels provided for your convenience:")
print()
print("       15%         18%          20%")
print(f"      ${tip_amt_15:.2f}       ${tip_amt_18:.2f}        ${tip_amt_20:.2f}    ")
print(f"      ${gt15:.2f}      ${gt18:.2f}       ${gt20:.2f}    ")
print() 
print("===============================================================================")
print()

rate = float(input("Enter your desired tip rate (example: 15): "))

tip = float(check * rate / 100)
grand_total = float(check + tip)

#################### D I S P L A Y  P A R T  II ##############################

print()
print(f"""{name}, your check amount for {restaurant} was ${check:.2f} 
and you generously selected {rate:.2f} percent as your tip rate.
Your tip amount is ${tip:.2f} 
which makes your Grand Total ${grand_total:.2f}""")
print()
print()