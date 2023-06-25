# Formatter with 4 placeholders
formatter = "{} {} {} {}"

# Putting an extra 5 here would only print '1 2 3 4'
print(formatter.format(1, 2, 3, 4, 5))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
# Sees 'formatter' as text, prints 16 {} in total
print(formatter.format(formatter,formatter,formatter,formatter))
# Putting carriage return here does not make a difference
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))