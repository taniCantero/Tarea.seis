
# class Dog:
    
#     def __init__(self, name):
#         self.name = name
    
#     def eat(self):
#         print("eating")
    
#     def move(self):
#         print("moving")
    
#     def bark(self):
#         print("barking")
    
#     def shake_tail(self):
#         print("tail shaking")
        
# class Title:
#     TITLE_WORD = "Python"
    
#     def main(self):
#         print("Book title is %s" %self.TITLE_WORD)


# class Cafe:
#     @classmethod
#     def drink(self):
#         print("drinking")
        
#     def coffee(self):
#         print(type(self))


class Cafe:
    def drink(self, kind):
        print("{} Ha, {} es. ".format(kind, self.__coffee(kind)))
    
    def __coffee(self, kind):
        if kind == "moca":
            return "Acidez y dulzor afrutados"
        elif kind == "Kilimanjaro":
            return "Sabor salvaje"
        elif kind == "Blue Mountain":
            return "El rey del cafe"


cafe = Cafe()
cafe.drink("moca")


class Animal:
    def __init__(self, name, owner = None):
        self.name = name
        self.owner = owner
    def eat(self):
        return "eat"
    
    def move(self):
        return "move freely"
    
    def voice(self, arg1="war", arg2="talk"):
        return f"{self.name}, But {arg1} and {arg2}"
    
    from pet import look, calm
    


class Cat(Animal):
    def voice(self):
        return super().voice(arg1="miau")
    
    def scratch(self):
        return "rayar"

class Dog(Animal):
    def voice(self):
        return super().voice(arg1="bow-wow", arg2="bark!")
    
    def shake_tail(self):
        return "shake the tail"

pochi = Dog("Pochi")
mike = Cat("Mike")

print(
pochi.look(),
pochi.look("Taro Yamada"),
Dog.calm()
)
print(pochi.voice())