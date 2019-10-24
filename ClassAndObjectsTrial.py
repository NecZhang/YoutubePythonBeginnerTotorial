from Student import Student         # the 1st Student means .py file, the 2nd means class

student1 = Student("Nec", "BME", 3.4, False)

print(student1.name)
print(student1.gpa)

student2 = Student("KK", "JPL", 3.7, False)

print(student2.on_honor_roll())
print(student1.on_honor_roll())