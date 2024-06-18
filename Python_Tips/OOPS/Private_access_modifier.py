'''
In Python, there is no strict concept of "private" access modifiers like in some other
programming languages. However, a convention has been established to indicate that a
variable or method should be considered private by prefixing its name with a double underscore (__). 
This is known as a "weak internal use indicator" and it is a convention only, not a strict rule. 
Code outside the class can still access these "private" variables and methods, but it is generally 
understood that they should not be accessed or modified.
'''

class Student: 
    def __init__(self, age, name): 
        self.__age = age      # An indication of private variable
        
        def __funName(self):  # An indication of private function
            self.y = 34
            print(self.y)

class Subject(Student):
    pass

obj = Student(21,"Harry")
obj1 = Subject

# calling by object of class Student
print(obj.__age)
print(obj.__funName())

# calling by object  of class Subject
print(obj1.__age)
print(obj1.__funName())


'''
Name Mangling -
Name mangling in Python is a technique used to protect class-private and 
superclass-private attributes from being accidentally overwritten by subclasses. 
Names of class-private and superclass-private attributes are transformed by the addition 
of a single leading underscore and a double leading underscore respectively.
'''

class MyClass:
    def __init__(self):
        self._nonmangled_attribute = "I am a nonmangled attribute"
        self.__mangled_attribute = "I am a mangled attribute"
my_object = MyClass()
print(my_object._nonmangled_attribute) # Output: I am a nonmangled attribute
print(my_object.__mangled_attribute) # Throws an AttributeError
print(my_object._MyClass__mangled_attribute) # Output: I am a mangled attribute