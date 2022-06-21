from dataclasses import dataclass, field

"""
Example of using the dataclass module in python
"""

'''
'order=True' give the object the functionality to be sorted and compared with one another
'frozen=True' makes the data of the object read only. This mean data cannot be altered or 
    change within the code after is has been set
'''

'''
Sort_index field parameters
'init=False' let python know that this field isn't required to set or initialised upon
creating the object. 
'repr=False' lets python know not to print this field when displaying the object in the terminal.
'''


@dataclass(order=True, frozen=True)
class Person:
    sort_index: int = field(init=False, repr=False)
    name: str
    age: int
    job: str
    relationship_status: str
    pets: int = 0  # Setting a default value for pets within the data class

    def __post_init__(self):
        '''
            Post init method sets the attribute sort_index after the object has been intialised.
            This is done using the setattr (set attribute) function as the dataclass is set to frozen (read only).
            Meaning that data variables can't be altered within the code after initialisation.
        '''
        object.__setattr__(self, 'sort_index', self.age)
        # settattr(object, attribute, value)

    def __str__(self):
        return f'{self.name}, {self.job} is {self.age} of age, {self.relationship_status} and has {self.pets} pets'


person_one = Person('Michael', 30, 'Janitor', 'Married')
person_two = Person('Jeffery', 40, 'Accountant', 'Divorced', 3)
person_three = Person('Jennifer', 22, 'Doctor', 'Single', 2)
person_four = Person('Anna', 50, 'Retired', 'Single', 1)

print(person_one > person_four)
print(person_one)


'''
Attempting to update the object variable will result in an error as the dataclass is set to read only.
person_one.age = 43 

'''

