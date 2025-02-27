#TASK1
import os

path = "." 

print("Directories:", [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])
print("Files:", [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
print("All items:", os.listdir(path)) 

#TASK2
import os

path = "nurzhan.txt" 

print("Exists:", os.path.exists(path))
print("Readable:", os.access(path, os.R_OK))
print("Writable:", os.access(path, os.W_OK))
print("Executable:", os.access(path, os.X_OK))

#TASK3
import os

path = "nurzhan.txt"

if os.path.exists(path):
    print("Directory:", os.path.dirname(path))
    print("Filename:", os.path.basename(path))
else:
    print("Path does not exist.")

#TASK4
with open("nurzhan.txt", "r", encoding="utf-8") as file:
    print(len(file.readlines()))

#TASK5
my_list = ["apple", "banana", "cherry"]

with open("fruits.txt", "w", encoding="utf-8") as file:
    file.writelines(item + "\n" for item in my_list)

#TASK6
import string

for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", "w") as file:
        file.write(f"This is {letter}.txt\n")

#TASK7
with open("source.txt", "r", encoding="utf-8") as src, open("destination.txt", "w", encoding="utf-8") as dest:
    dest.write(src.read()) 

#TASK8
import os

file = "nyrzhan.txt"

if os.path.exists(file) and os.access(file, os.W_OK):
    os.remove(file) 
    print("File deleted.")
else:
    print("File not found.")
