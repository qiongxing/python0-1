def build_profile(first,last,**user_info):
    profile = {}
    profile['first_name']=first
    profile['last_name']=last
    for key,value in user_info.items():
        profile[key]=value
    print(profile)

build_profile("qiong","xing",second_name="1412")
