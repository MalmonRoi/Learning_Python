
import random

name = "Enter name: "
print(input(name))
question = "Enter Question: "
print(input(question))
answers = [["Yes"], ["It is decidedly so"], ["Without a doubt"]
    , ["Reply hazy, try again."], ["Ask again later"], ["Better not tell you now"]
    , ["My sources say no"], ["Outlook not so good"], ["Very doubtful"]]

random.shuffle(answers)
print("****Magic 8 Ball****")
print(answers[-1:])
