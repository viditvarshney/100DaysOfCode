# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

trueCount = 0
loveCount = 0
combineNames = name1+name2

for i in 'true':

    temp = combineNames.count(i)
    trueCount += temp

for i in 'love':

    temp = combineNames.count(i)
    loveCount += temp

loveScore = int(str(trueCount)+str(loveCount))

if loveScore < 10 or loveScore > 90:
    print(f"Your score is {loveScore}, you go together like coke and mentos.")

elif loveScore > 40 and loveScore < 50:
    print(f"Your score is {loveScore}, you are alright together.")
else:
    print(f"Your Score is {loveScore}")
