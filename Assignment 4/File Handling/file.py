# File Handling in Python:
# File handling is essential for reading and writing data to files, enabling persistent storage.
# Python provides built-in functions and methods to handle files efficiently.

# Opening a File
# Use the open() function to open a file. Specify the mode (read, write, append, etc.).

# Modes:
# r: Read (default)
# w: Write (Opens the file for writing. Creates the file if it doesn't exist, or overwrites it if it does.)
# a: Append (Opens the file for appending. Creates the file if it doesn't exist, or adds to it if it does.)
# x: Exclusive creation (fails if file exists)
# b: Binary mode (Used with the other modes (e.g., "rb", "wb") for working with binary files.)
# +: Update mode (Can be combined with other modes (e.g., "r+", "w+") to allow both reading and writing.)

# w: Write mode.

file = open("new_file.txt", "w")
file.write("Learning Python! \n")
file.write("Happy Coding! \n")
file.close()

# writelines(list): Writes a list of strings to the file.

lines = ["Line 1:In Karachi \n", "Line 2:At GIAIC \n", "Line 3:Quarter 3 \n"]
file = open("new_file.txt", "a")
file.writelines(lines)
file.close()

# file = open("my_file.txt", "r")  # Error: FileNotFoundError

file = open("new_file.txt", "r")   # Correct the name of the file
content = file.read()
print(content)

line = file.readline()
print(line)

# Move pointer back to start.

print(file.seek(0))

# Check the file cursor/pointer position after running seek(0) method.

print("Position after seek(0):", file.tell())

line = file.readline()
print(line)

# readlines(): Reads all lines into a list.
file.seek(0)
lines = file.readlines()
for line in lines:
    print(line)

file = open("new_file.txt", "r")
for line in file:          # Iterating directly over the file reads line by line
    print(line.strip())    # .strip() removes leading/trailing whitespace

# Closing Files:
# It's crucial to close files after you're finished with them. This releases system resources and ensures that data is properly written to the disk. 
# The close() method is used for this:

file.close()

# Additional Tips
# Exclusive Creation (x mode):

# Best Practices:
# Use with for automatic cleanup.
# Handle exceptions to avoid crashes.

try:
    with open("unique.txt", "x") as file:
        file.write("Create Exclusively!")
        print("File Created Successfully!")
except FileExistsError:
    print("File already exists.")

# The with Statement (Context Manager):
# The best practice for file handling is to use the with statement. 
# This ensures that the file is automatically closed, even if errors occur.

with open("new_file.txt", "r") as file:
    content = file.read()
    print(content)
    # File is automatically closed here

# ValueError: I/O operation on closed file.
# print(file.tell())

# Reading in chunks
with open("new_file.txt", "r") as file:
    print(file.tell())

    i = 0
    while True:
        content = file.read(10)
        if not content:
            print("End of the file.")
            break
        print(content)
        i += 1

    print(file.tell())  # now at position 5
    print(file.seek(0))  # back to start


# You can only seek() in text mode with offsets from the beginning (i.e., whence=0).
# If you want to use whence=1 or whence=2, open the file in binary mode ('rb' or 'wb').

with open("new_file.txt", "rb") as f:
    print("Tell:", f.tell())
    f.seek(5)
    print("Tell:", f.tell())
    f.seek(2, 1)   # move 2 bytes forward from current
    print("Tell:", f.tell())
    f.seek(-3, 2)  # go 3 bytes *before* end of file
    print("Tell:", f.tell())

# Example: Copying a file

def copy_file(source_path, destination_path):
    try:
        with open(source_path, "r") as source_file, open(destination_path, "w") as destination_file:
            for line in source_file:
                destination_file.write(line)
            print(f"File '{source_path}' copied to '{destination_path}' successfully!")
    except FileNotFoundError:
        print(f"Error: Source file '{source_path}' not found!")
    except Exception as e:
        print(f"An error occured: {e}")
    
copy_file("unique.txt", "unique_copy.txt")


# Binary mode (Used with the other modes (e.g., "rb", "wb") for working with binary files.)

def copy_image(source_path, destination_path):
    try:
        with open(source_path, "rb") as source_file:
            with open(destination_path, "wb") as destination_file:
                while True:
                    chunks = source_file.read(1024)  # Read in chunks
                    if not chunks:
                        break
                    destination_file.write(chunks)
        print(f"Image copied successfuly from {source_path} to {destination_path}")
    except FileNotFoundError:
        print(f"Error: Source File {source_path} not found!")
    except Exception as e:
        print(f"An error occured: {e}")

copy_image("Artificial.jpg", "Copy_Artificial.jpg")

# File Operations Demo

# Create and write to a file
with open("demo.txt", "w") as file:
    file.write("Learning File Handling in Python.\n")
    file.write("Coding Vibes!\n Learn with Fun\n Then Earn!")

# Read and print content
with open("demo.txt", "r") as file:
    content = file.read()
    print("Content:", content)

# Append a new line
with open("demo.txt", "a") as file:
    file.write("Practice makes men perfect!\n")

# Read lines using seek
with open("demo.txt", "r+") as file:
    file.seek(0)
    print("First Line:", file.readline())


# comprehensive example of file handling using all the functions

# Create a file and write to it
with open("learn.txt", "w") as file:
    file.write("Learning File Hadling!\n")
    file.write("Using all its functions.\n")
    file.writelines(["open()\n", "read()\n", "write()\n", "close()\n"])

# Read the file and print its content
with open("learn.txt", "r") as file:
    print("Content:")
    print(file.read())

# Read the file line by line and print each lines
with open("learn.txt", "r") as f:
    print("----Read file line by line-----")
    for line in f:
        print(line, end="")

print("\n")

# Read a single line
with open("learn.txt", "r") as f:
    print("Readline\n")
    print(f.readline(), end="")

print("\n")

# Read all lines into a list
with open("learn.txt", "r") as file:
    lines = file.readlines()
    print("Readlines\n")
    for line in lines:
        print(line, end="")

# Append to the file
with open("learn.txt", "a") as file:
    file.write("using with for safety and close file automatically.")

# Reading with seek and tell
with open("learn.txt", "r") as file:
    print("\n----Seek and Tell---")
    print("Current Position:", file.tell())
    print("First Line:", file.readline(), end="")
    print("Current Position:", file.tell())
    file.seek(0)
    print("After seek(0):", file.tell())
    print("First line again:", file.readline(), end="")

# Demonstrating 'x' mode (exclusive creation)
try:
    with open("new_file.txt", "x") as f:
        f.write("This is the new file created in 'x' mode.")
        print("new_file.txt created successfully!")
except FileExistsError:
    print("File 'new_file.txt' already exists!")


# Copy file example
def copy_file(source, destination):
    try:
        with open(source, "r") as src, open(destination, "w") as dest:
            for line in src:
                dest.write(line)
            print(f"{source} successfully copied to {destination}")
    except FileNotFoundError:
        print(f"Error: File not found {source}")
    except Exception as e:
        print(f"Error: error during copying: {e}")

copy_file("learn.txt", "copy_learn.txt")





