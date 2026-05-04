from S1E9 import Character


class Baratheon(Character):
    """Class representing a member of House Baratheon."""

    def __init__(self, first_name, is_alive=True):
        """Initialize a Baratheon character with predefined attributes."""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """Return a readable string representation of the character."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Return an unambiguous string representation of the character."""
        return self.__str__()

    def die(self):
        """Set the character state to dead."""
        self.is_alive = False

    def represent(self):
        """Return the representation message for the Baratheon family."""
        return "Representing the Baratheon family."


class Lannister(Character):
    """Class representing a member of House Lannister."""

    def __init__(self, first_name, is_alive=True):
        """Initialize a Lannister character with predefined attributes."""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        """Return a readable string representation of the character."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Return an unambiguous string representation of the character."""
        return self.__str__()

    def die(self):
        """Set the character state to dead."""
        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """Create and return a new Lannister character instance."""
        return cls(first_name, is_alive)
