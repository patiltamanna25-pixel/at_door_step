# 1.Create a file named data.txt and write your name into it.  
with open("data.txt","w") as f:
    f.write("My Name is Tamanna")
#1.	Read content from data.txt and print it. 
with open("data.txt","r") as f:
    print(f.read())
#3.	Append your city name to the same file. 
with open("data.txt","a+")as f:
    print(f.write("\n I live in Shimla "))
    f.seek(0)
    print(f.read())
#4.1.	Count total characters in a file. 
with open("data.txt","r") as f:
     d=f.read()
     print(d)
     print(len(d))
#or
total_chars = 0

with open("data.txt", "r") as file:
    for line in file:
        total_chars += len(line)

print(f"Total characters: {total_chars}")
#5.	Count total words in a text file. 
def count_words("data.txt"):
    try:
        with open("data.txt") as file:
            data = file.read()
            words = data.split()
            return len(words)
    except FileNotFoundError:
        return "File not found."

# Example usage:
file_name = "example.txt"
total_words = count_words(file_name)
print(f"Total words: {total_words}")



