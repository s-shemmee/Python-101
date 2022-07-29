# type a script that take the bill amound and give u the tip of 5% 10% 15% and 20%

bill = float(input("What is your the bill, please ?").strip('$'))

tip_5 = bill * 0.5
tip_10 = bill * 0.10
tip_15 = bill * 0.15
tip_20 = bill * 0.20

print(f"So you tips are for 5% is {tip_5:.2f}$, for 10% is {tip_10:.2f}$, for 15% is{tip_15:.2f}$, and for 20% is {tip_20:.2f}$")