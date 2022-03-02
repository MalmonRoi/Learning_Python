# Your code below:

toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]

num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

#Make Some Pizzas
num_pizzas = len(toppings)

print("We sell", num_pizzas, "kinds of pizza!")

pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]

cheapest_pizza = pizza_and_prices

priciest_pizza = pizza_and_prices[-1]
pizza_and_prices.sort()
pizza_and_prices.pop()

pizza_and_prices.insert(4 , [2.5, "peppers"])

three_cheapest = pizza_and_prices[:3]

print(three_cheapest)




