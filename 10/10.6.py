try:
    oneNumber= int(input("one number:"))
    twoNumber= int(input("two number:"))
except TypeError:
    print("不是数字")
else:
    print(oneNumber, twoNumber)