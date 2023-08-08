# We are using command line arguments
from sys import argv

# We are taking two command line arguments
script, filename = argv

# We are loading the file into txt
txt = open(filename)

# We are printing the contents of the file
print(f"Here's your file {filename}:")
print(txt.read())
txt.close()
print("txt is closed")

# We are printing the contents of the file, but ask user to provide filename
print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

txt_again.close()
print("txt_again is closed")