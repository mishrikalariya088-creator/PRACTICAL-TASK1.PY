with open ("one.txt","r")as f,open("data.txt","r")as f2,open("creat.txt","w")as f3:
f3.write(f1.read())
f3.write("\n")
f3.write(f2.read())
print("files merged successfully")