# Exercise 9
# Here's some new strange stuff, remember type it exactly.

# This is one single line with spaces.
days = "Mon Tue Wed Thu Fri Sat Sun"
# I added another \n before 'Jan.' I like 'Jan' on its own line too
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

# Write the prompt, print text as-is
print("Here are the days: ", days)
print("Here are the months: ", months)

# Three double-quotes behaves like a HEREDOC
print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")