from modules import Json

def generator():

    contents = dict()
    
    contents["TOKEN"] = input("Input Taiwan Central Weather Bureau OPENDATA API'S Token\n> ")

    with open("config.json", mode="w") as _:

        Json.dump_nowait(file="config.json", data=contents)

    return
