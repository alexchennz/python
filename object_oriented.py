class Animal:
    """Base class for all animals"""
    
    def __init__(self, name, age):
        """
        Initialize an animal
        
        Args:
            name (str): Name of the animal
            age (int): Age of the animal in years
        """
        self.name = name
        self.age = age
        self.energy = 100
    
    def sleep(self, hours):
        """
        Restore energy by sleeping
        
        Args:
            hours (int): Number of hours to sleep
        """
        self.energy = min(100, self.energy + (hours * 10))
        return f"{self.name} slept for {hours} hours and now has {self.energy}% energy"
    
    def make_sound(self):
        """Make a generic animal sound"""
        return "Some generic animal sound"
    
    def get_info(self):
        """Return basic information about the animal"""
        return f"Name: {self.name}, Age: {self.age}, Energy: {self.energy}%"


class Dog(Animal):
    """Dog class that inherits from Animal"""
    
    def __init__(self, name, age, breed):
        """
        Initialize a dog
        
        Args:
            name (str): Name of the dog
            age (int): Age of the dog in years
            breed (str): Breed of the dog
        """
        super().__init__(name, age)
        self.breed = breed
        self.tricks = []
    
    def make_sound(self):
        """Override the make_sound method"""
        return "Woof! Woof!"
    
    def learn_trick(self, trick):
        """
        Learn a new trick
        
        Args:
            trick (str): Name of the trick to learn
        """
        self.tricks.append(trick)
        return f"{self.name} learned to {trick}!"
    
    def do_trick(self, trick):
        """
        Perform a learned trick
        
        Args:
            trick (str): Name of the trick to perform
        """
        if trick in self.tricks:
            self.energy -= 10
            return f"{self.name} performs: {trick}"
        return f"{self.name} doesn't know how to {trick}"
    
    def get_info(self):
        """Override get_info to include breed and tricks"""
        base_info = super().get_info()
        tricks_info = f"Tricks known: {', '.join(self.tricks) if self.tricks else 'None'}"
        return f"{base_info}, Breed: {self.breed}, {tricks_info}"


class Cat(Animal):
    """Cat class that inherits from Animal"""
    
    def __init__(self, name, age, color):
        """
        Initialize a cat
        
        Args:
            name (str): Name of the cat
            age (int): Age of the cat in years
            color (str): Color of the cat's fur
        """
        super().__init__(name, age)
        self.color = color
        self.mice_caught = 0
    
    def make_sound(self):
        """Override the make_sound method"""
        return "Meow!"
    
    def hunt(self):
        """Go hunting for mice"""
        if self.energy >= 20:
            self.energy -= 20
            self.mice_caught += 1
            return f"{self.name} caught a mouse! Total mice caught: {self.mice_caught}"
        return f"{self.name} is too tired to hunt"
    
    def groom(self):
        """Groom self"""
        self.energy -= 5
        return f"{self.name} is grooming their {self.color} fur"
    
    def get_info(self):
        """Override get_info to include color and mice caught"""
        base_info = super().get_info()
        return f"{base_info}, Color: {self.color}, Mice caught: {self.mice_caught}"


def main():
    # Create some animals
    dog = Dog("Buddy", 3, "Golden Retriever")
    cat = Cat("Whiskers", 2, "Orange")
    
    # Demonstrate some functionality
    print("=== Animal Demo ===")
    
    # Dog demo
    print("\nDog Demo:")
    print(dog.get_info())
    print(dog.make_sound())
    print(dog.learn_trick("sit"))
    print(dog.learn_trick("roll over"))
    print(dog.do_trick("sit"))
    print(dog.do_trick("play dead"))
    print(dog.sleep(2))
    
    # Cat demo
    print("\nCat Demo:")
    print(cat.get_info())
    print(cat.make_sound())
    print(cat.hunt())
    print(cat.groom())
    print(cat.hunt())
    print(cat.sleep(5))


if __name__ == "__main__":
    main() 