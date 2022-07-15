import random

bars = ["Shoolbred's",
        "The Wren",
        "The Scratcher",
        "ACME",
        "Blind Barber"]

people = ["Mattan",
          "Chris",
          "that person you forgot to text back",
          "Kanye West",
          "Samuel L. Jackson",
          "Kosta"]

random_bar = random.choice(bars)
random_person_one = random.choice(people)
random_person_two = random.choice(people)

print(f"How about you go to {random_bar} with {random_person_one} and {random_person_two}?")
