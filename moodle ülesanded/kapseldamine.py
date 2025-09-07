class Cat:

    def __init__(self, name,age=2):
        self.name = name
        self.age = age

cat_kitty = Cat("Kitty")
cat_miisu = Cat("Miisu", 10)

print(cat_kitty.age)
print(cat_miisu.age)