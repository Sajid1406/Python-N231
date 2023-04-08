# Class Object Method

# 1
class person:

    def __init__(self,name):
        self.name = name

    def say_hello(self):
        print(f"Hello my name is {self.name}")

Sajid = person("Sajid")
Shakil = person("Shakil")

Sajid.say_hello()
Shakil.say_hello()

# 2
class Animal:
    # so=""

    def __init__(self,sound01):
        self.so = sound01

    def sound(self):
        print(f"Voice {self.so}")

dog = Animal("Gheu")
cat = Animal("Meow")
crow = Animal("kaka")

dog.sound()
cat.sound()
crow.sound()

# 3 
class person:
    def __init__(self,name,relationship_status):
        self.name = name
        self.relationship_status = relationship_status

    def check_status(self):
        print(f"{self.name} is {self. relationship_status}")

person01 = person("X","Single")
person02 = person("Y","Mingle")

person01.check_status()
person02.check_status()

# 4
class person:
    def __init__(self,name,relationship_status):
        self.name = name
        self.relationship_status = relationship_status

    def fall_in_love(self,other_person):
        self.relationship_status = f"in a relationship with {other_person.name}"
        other_person.relationship_status = f"in a relationship with {self.name}"
    
    def check_status(self):
        print(f"{self.name} is {self. relationship_status}")

person01 = person("Romeo","Single")
person02 = person("Juliet","Single")

person01.fall_in_love(person02)

person01.check_status()
person02.check_status()

# Inheritance

class RomanticPoet(person):
    def recite_poem(self):
        print("Twinkle Twinkle Little Star")

class LoveAdvisor(person):
    def give_advice(self):
        print("Follow your heart and be true to yourself")

poet = RomanticPoet("Shakespeare","single")
advisor = LoveAdvisor("Someone","mingle")

poet.recite_poem()
advisor.give_advice()

poet.check_status()
advisor.check_status()

# Polymorphism

class RomanticPoet(person):
    def recite_poem(self):
        print("Twinkle Twinkle Little Star")

class LoveAdvisor(person):
    def give_advice(self):
        print("Follow your heart and be true to yourself")

def express_love(person):
    if isinstance(person,RomanticPoet):
        person.recite_poem()
    elif isinstance(person,LoveAdvisor):
        person.give_advice()
    else:
        print(f"{person.name} says, I Love you!")

express_love(person01)
express_love(person02)

express_love(poet)
express_love(advisor)

# Another One

# class food:
#     def eat(name,eat):
#         print("something")
# class hungry:
#     def eat(name):
#         print(name)

# me=food()
# me.eat()
# me.eat("Apple")

# Another One

class Dog:
    def speak(self):
        return "Gheu"
class Cat:
    def speak(self):
        return "meow"
    
def make_animal_speak(animal):
    print(animal.speak())

dog = Dog()
cat = Cat()

make_animal_speak(dog)
make_animal_speak(cat)