class GotCharacter :
    """
    A class representing a character.
    """
    def __init__(self, first_name=None, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive


class Stark(GotCharacter):
    """
    A class representing the Stark family. Or when bad things happen to good people.
    """
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False
    
    def __str__(self):
        """Return the string to print with the character info"""

        txt = f"\n Name: {self.first_name} {self.family_name}\n"
        txt += f"Alive : {self.is_alive}\n"
        txt += f"House words: {self.house_words}"

        return txt

class Parker(GotCharacter):
    """
    A class representing the Stark family. Or when bad things happen to good people.
    """
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Parker"
        self.house_words = "Summer is Coming"

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False
    
    def __str__(self):
        """Return the string to print with the character info"""

        txt = f"\n Name: {self.first_name} {self.family_name}\n"
        txt += f"Alive : {self.is_alive}\n"
        txt += f"House words: {self.house_words}"

        return txt

if __name__ == "__main__" :

    arya = Stark("Arya")

    print("-> Information about Arya Stark:")
    print(arya.__dict__)

    print("\n-> Print house words:")
    arya.print_house_words()

    print("\n-> Arya Stark is alive:")
    print(arya.is_alive)

    arya.die()
    print("\n-> Stark dies, is she still alive ?")
    print(arya.is_alive)

    print("\n-> Information of the class:")
    print(arya.__doc__)

    peter = Parker("Peter")
    print("\n-> Information about Peter Parker:")
    print(peter.__dict__)

    print("\n-> Print house words:")
    peter.print_house_words()

    peter.die()
    print("\n-> Parker dies, is he still alive ?")
    print(peter.is_alive)