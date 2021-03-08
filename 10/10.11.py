import json

"""写入数字"""
# with open("10.11.json","w") as txt_obj:
#     userNum = int(input("喜欢的数字:"))
#     json.dump(userNum, txt_obj)

# 读取数字
with open("10.11.json") as txt_obj:
    num= json.load(txt_obj)
    print("I know you love:"+str(num))
