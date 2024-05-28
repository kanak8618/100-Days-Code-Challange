# Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.


class Person:
    def getGender(self):
        print( "I'm Human")
class Male(Person):
    def getGender(self):
        super().getGender()  # invoke parent class method
        return "Male"
class Female(Person):
    def getGender(self):
        return "Female"

male = Male()
female = Female()
print(Male.mro())  # Show the which method call first
print(male.getGender())
print(female.getGender())

