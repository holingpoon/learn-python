print("I will count my chickens:")

# Division happened first and returned decimal number 5.0
# so 25 + 5.0 = 30.0
print("Hens", 25 + 30 / 6)

# Multiply 25 * 3: 100 - 75 % 4
# Modulo 75 % 4: 100 - 3 = 97
print("Roosters", 100.0 - 25 * 3 % 4)

print("Now I will count the eggs:")

# 3 + 2 + 1 - 5 + 4 % 2 - 0.25 + 6
# 3 + 2 + 1 - 5 + 0 - 0.25 + 6
# 5 + 1 - 5 + 0 - 0.25 + 6
# 6 - 5 + 0 - 0.25 + 6
# 0.75 + 6 = 6.75
print(3.0 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

print("Is it true that 3 + 2 < 5 - 7?")

# (5 < -2) returns false
print(3.0 + 2 < 5 - 7)

print("What is 3 + 2?", 3.0 + 2) # 5
print("What is 5 - 7?", 5.0 - 7) # -2

print("Oh, that's why it's False")

print("How about some more.")

print("Is it greater?", 5.0 > -2) # returns True
print("Is it greater or equal?", 5.0 >= -2) # returns True
print("Is it less or equal?", 5.0 <= -2) # returns False

print("The approximation of pi is ", 22 / 7)
