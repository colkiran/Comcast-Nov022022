
def get_name(surname):
    print(f"surname is  {surname}")

    while True:
        name = yield                # accepting data from the user
        print(f"Name received....{name}")
        print("-" * 40)
        if surname in name:
            print(f"surname {surname} found in {name}......")

coObj = get_name("birla")
print(coObj)
print(type(coObj))
coObj.__next__()
coObj.send("ratan tata")
coObj.send("mukesh ambani")
coObj.send("aditya birla")
