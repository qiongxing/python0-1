import json
"""写入数字"""
def write_num():
    with open("10.11.json","w") as txt_obj:
        userNum = int(input("喜欢的数字:"))
        json.dump(userNum, txt_obj)


# 读取数字
def load_num():
    try:
        with open("10.11.json") as txt_obj:
            num= json.load(txt_obj)
            return str(num)
    except:
        return None

num= load_num()
if num:
    print("you like num:"+num)
else:
    write_num()
