from carClass import Car

car1 = Car("Honda", "2014", "2000")
car1.start()  # Start the car's engine
#You can access the attributes or variable if they were not meant to pass th evalues to.
car1.status=True
print(f"The car is named {car1.name} and the car year is {car1.year} and the car status is {car1.currentStatus()}")
