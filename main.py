# file = open("my_file.txt")
# file.close()

# open file
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# write to file
with open("my_file.txt", mode="a") as file:
    file.write("\nNew text.")

# create new file if file doesn't exist
with open("new_file.txt", mode="w") as file:
    file.write("New text.")
