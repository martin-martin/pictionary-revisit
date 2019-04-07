import random
# get all the weeks, however many are defined
from topics import *

# pick the imported weekly pictionary suggestions from globals
weeks = [week for key, week in globals().items() if key.startswith('week')]

num = None
# start at one and add +1 at the end in order to make the range
# more logical for human users
while num not in range(1, len(weeks)+1):
    print("which week do you want to revisit?")
    try:
        num = int(input("enter the week number: "))
    except ValueError as e:
        print("just a simple number, mkay?")

# querying by 0-based index, so we need to reduce by one to get
# the right week
pics = weeks[num-1].split('\n')
print("\n\nYOUR TASK: DRAW THE FOLLOWING:\n")
print("=================")
print(random.choice(pics))
print("=================")
print("\nNOTE: no words, no code, just pictures!")
