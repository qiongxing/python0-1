def make_car(name,color,**args):
    cars = {}
    cars["name"]=name
    cars["color"]=color
    for k,v in args.items():
        cars[k]=v
    return cars

car = make_car("subaru","red",tow_package=True)
print(car)
