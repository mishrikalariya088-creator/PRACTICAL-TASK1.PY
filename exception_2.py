try:
    my_list=[10,20,30,40,50]
    print(my_list[1])

except ImportError:
    print("index is out of range")

else:
    print("element found successfully")

finally:
    print("program finished")