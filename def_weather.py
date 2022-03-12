def weather(answer):
  while answer == 'y':
    temperature = float(input("Enter the temperature for today: "))
    print("You have entered ", round(temperature, 2))
    print(displayResult(temperature))
    answer = input("Would you like to enter the temperature for today? (y/n)")
  print("Goodbye!")

def displayResult(temperature):
  if temperature >= 30:
    return "The weather is very hot today"
  elif temperature >= 20:
    return "The weather is beautiful today"
  elif temperature >= 10:
    return "The weather is cool today"
  else:
    return "The weather is very cold today"
  print("Goodbye")

answer = input("Would you like to enter the temperature for today? (y/n)? ")
weather(answer)