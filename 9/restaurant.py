class Restaurant():
    def __init__(self,name,r_type):
        self.restaurant_name = name
        self.cuisine_type = r_type

    def describe_restaurant(self):
        print("name:"+self.restaurant_name)
        print("type:"+self.cuisine_type)

    def open_restaurant(self):
        print("open restaurant")