init 10 python:
    class Door:
        def __init__(self, id, name, description, image, durability = 100):
            self.id = id 
            self.name = name
            self.description = description
            self.image = image
            self.durability = durability
            self.container = []
