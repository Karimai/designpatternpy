from abc import ABCMeta, abstractmethod


class IBuilder(metaclass=ABCMeta):
    @abstractmethod
    def build_walls(self):
        """
        build walls
        """
        pass

    @abstractmethod
    def build_roof(self):
        """
        build roof
        """
        pass

    @abstractmethod
    def build_door(self):
        """
        Build doors
        """
        pass

    @abstractmethod
    def build_window(self):
        """
        Build window
        """
        pass
