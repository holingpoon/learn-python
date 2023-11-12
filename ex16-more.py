from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print("First line:", txt.readline())
print("Second line:", txt.readline())
print("Third line:", txt.readline())