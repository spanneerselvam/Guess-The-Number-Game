import random
print("Hey Friend! Let's play guess the number. So how this works is that I've chosen a number between 1-20 and you have to figure it out! Are you ready?")
print("Hit 'Enter' if you're ready!")
input()
rounds = 0 #rounds is the number of times you play
leaveprogram = 0
while leaveprogram != 'q':
  rounds += 1
  number = random.randint(1,20)
  print("This is round {}".format(rounds))
  print("I've chosen a number. Now it's your turn to guess!")
  guess = int(input("Guess Integer: "))
  print()
  if number == guess:
    print("Nice! You got it dude!")
    print(number)
    print()
    print("Sick of this game? Hit 'q' to quit program.")
    print("Otherwise, press enter to play again!")
    leaveprogram = input()
  if not guess in range(1, 20):
    print ("Incorrect range. Please try again!")
    print("Please enter a number between 1-20.")
    guess = int(input("Guess Integer: "))
  if number != guess:
    print("Ah man, better luck next time!")
    print("This was the real number: {}".format(number))
    print()
    print("Sick of this game? Hit 'q' to quit program.")
    print("Otherwise, press enter to play again!")
    leaveprogram = input()
    print()
