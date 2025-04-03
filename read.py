file=open("C:\python\Text.txt", "a")
while True:
    S=input()
    if S == "exit":
        print("Exited")
        break
    if S == "remove":
        file =open("C:\python\Text.txt","r+")
        file.truncate()
        print("removed")


    else:
        content =file.write(S + "\n")
file.close()

myfile=open("C:\python\Text.txt", "r+")
content=myfile.read()
print(content)
