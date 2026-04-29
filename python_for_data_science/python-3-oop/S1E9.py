from abc import ABC, abstractmethod


class Character(ABC):
    """Base abstract class representing a character."""

    def __init__(self, first_name, is_alive=True):
        """Initialize the character with a name and life status."""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Change the character state from alive to dead."""
        pass


class Stark(Character):
    """Class representing a member of House Stark."""

    def die(self):
        """Marks the Stark as dead and triggers house-specific behavior."""
        self.is_alive = False
