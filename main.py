# File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.

# opening files

with open("studies.txt", "r") as file:
    data = file.read()
    
# print(data)

# modified version
modified = data.upper()

# write new file
with open("exams.txt", "w") as new_file:
    new_file.write(modified)




# Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.

filename = input("Enter the filename: ")

try:
    with open(filename, "r") as file:
        data = file.read()
        print(data)

except FileNotFoundError:
    print(f"The file '{filename}' was not found.")
except IOError:
    print(f"An error occurred while reading the file '{filename}'.")
finally:
    print("Operation is done")


