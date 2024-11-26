# Lab 12 OOP
# Robert Zuchowski
# 2024-11-25
# Pet Class


class Pet:
    """Pet class to model an animal pet."""

    def __init__(self, name: str=None, type: str=None, age: int=0) -> None:
        """Initialize a Pet object."""

        self._name = name
        self._type = type
        self._age = age

    
    def set_name(self, name: str) -> None:
        name = str(name)
        if len(name) < 1:
            raise ValueError('name must be non-empty string.')
        self._name = name

    def get_name(self) -> str:
        return self._name

    def set_type(self, type: str) -> None:
        type = str(type)
        if len(type) < 1:
            raise ValueError('type must be non-empty string.')
        self._type = type

    def get_type(self) -> str:
        return self._type
    
    def set_age(self, age: int) -> None:
        age = int(age)
        if age < 0:
            raise ValueError('age must be 0 or greater.')
        self._age = age

    def get_age(self) -> int:
        return self._age



def main():

    # instantiate Pet object
    pet = Pet()

    # call each setter method in try/except block for input validation
    while True:
        try:
            pet.set_name(input('Enter a pet name:\n').strip())
            break
        except Exception as e:
            print(e)

    while True:
        try:
            pet.set_type(input('Enter a pet type:\n').strip())
            break
        except Exception as e:
            print(e)

    while True:
        try:
            pet.set_age(input('Enter a pet age:\n'))
            break
        except Exception as e:
            print(e)

    # print results of each getter method
    print(f'The pet name is {pet.get_name()}')
    print(f'The pet type is {pet.get_type()}')
    print(f'The pet age is {pet.get_age()}')


if __name__ == "__main__":
    main()