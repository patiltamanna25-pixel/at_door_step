#***********FILE HANDLING************
with open  ("data.txt","r") as file:
    content=file.read()
    print(content)
with open  ("data.txt","w") as file:
    content=file.write("Read books")
    print(content)

    