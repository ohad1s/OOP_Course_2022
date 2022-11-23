from abc import abstractmethod, ABC
# from math import sin
class human_being(ABC):

    @abstractmethod
    def get_gender(self)->str:
        """
        :return: gender of a human being
        """
    pass

    @abstractmethod
    def hug_sound(self)->str:
        """
        :return: hug sound of human being
        """
    pass


if __name__ == "__main__":
    hb1= human_being()
