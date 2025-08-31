class emp:
    name = "Khushi"

    def __init__(self):
        print("Object created")

    def getInfo(self):
        print(f"Name is {emp.name}")
    

khushi = emp()
khushi.name = "Pawar"
print(khushi.name)
khushi.getInfo()