
fruits = [
    ('apple', 285),
    ('orange', 45),
    ('grapes', 125),
    ('pineapple', 90),
    ('gauva', 110),
    ('pears', 225),
    ('watermelon', 74),
    ('strawberry', 350)
]

print(f"fruits :{fruits}")

print("-" * 40)

price = ['fruit' for fruit in fruits]
print(f"prices :{price}")

print("-" * 40)

price = [fruit for fruit in fruits]
print(f"price :{price}")

print("-" * 40)

price = [fruit[0] for fruit in fruits]
print(f"price :{price}")

print("-" * 40)

price = [fruit[1] for fruit in fruits]
print(f"price :{price}")

prices = [(fruit[1], fruit[1] * 0.9) for fruit in fruits]
print(f"prices :{prices}")

print("-" * 40)
# print(fruits[0])
prices = [(fruit[1], fruit[1] * 0.75) for fruit in fruits]
print(f"prices :{prices}")

print("-" * 40)
expnsvFrts = [fruit for fruit in fruits if fruit[1] >= 100]
print(f"Expensive Fruits :{expnsvFrts}")

print("-" * 40)

expnsvFrts = [(fruit[0], fruit[1], fruit[1] * 0.9, fruit[1] * 0.75) for fruit in fruits if fruit[1] >= 100]
print(f"expensive fruits :{expnsvFrts}")

print("-" * 40)

sentence = "the quick brown fox jumps over the lazy dog"
print(f"sentence :{sentence}")

print("-" * 40)

words = [word for word in sentence.split()]
print(f"words  :{words}")

print("-" * 40)

words = [word for word in sentence.split() if word != 'the']
print(f"words :{words}")

print("-" * 40)

words = [(word, len(word)) for word in sentence.split() if word != 'the']
print(f"words :{words}")

print("-" * 40)

numbers = [45.9, 59.7, -35.3, -40.02, -30.29, 63.6, -58.5, 61.85]
print(f"numbers :{numbers}")

posNum = [number for number in numbers if number > 0]
print(f"positive numbers :{posNum}")

print("-" * 40)
squares = [n ** 2 for n in range(1, 11)]
print(f"squares :{squares}")
