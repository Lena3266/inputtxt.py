# Step 1: Create 'input.txt' and write 5 lines into it
with open('input.txt', 'w', encoding='utf-8') as f:
    f.write("Hi there\n")
    f.write("My name is Lena\n")
    f.write("I love this class❤️\n")
    f.write("Its a bit challenging\n")
    f.write("We win nonetheless👌\n")

# Step 2: Read the contents of 'input.txt'
with open('input.txt', 'r', encoding='utf-8') as f:
    contents = f.read()

# Step 3: Count the number of words
word_count = len(contents.split())

# Step 4: Convert all text to uppercase
uppercase_contents = contents.upper()

# Step 5: Write uppercase text and word count to 'output.txt'
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(uppercase_contents)
    f.write(f"\n\nWORD COUNT: {word_count}\n")

# Step 6: Print a success message
print("✅ output.txt created successfully with uppercase text and word count.")
