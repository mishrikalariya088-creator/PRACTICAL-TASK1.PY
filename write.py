f=open("0ne.txt","w")
f.write("hello!\n")
f.write("welcome to python file\n")
f.write("lerning is fun! \n")
f.close()

f=open("two.txt","w")
f.write("new content only\n")
f.close()

f=open("two.txt","a")
f.write("this line is addad at the end.\n")
f.close()

f=open("two.txt","w")
lines=[
    "python programming\n"
    "file handling\n"
    "error handling\n"
    "exception handling\n"
]
f.writelines(lines)
f.close()