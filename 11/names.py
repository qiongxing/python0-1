from name_function import get_formatted_name
print("q:End")
while True:
    first =input("\nPlease give me a first name:")
    if first == "q":
        break
    last =input("Please give me a last name:")
    if last == "q":
        break
    formatted_name = get_formatted_name(first,last)
    print("\t Neatly formatted name:"+formatted_name)