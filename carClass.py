class Car:
    """
    A class representing a car.

    Note:
    - How to declare a class.
    - The use of "__" before and after method names.

    Attributes:
    - name (str): The name of the car.
    - year (str): The year of the car.
    - model (str): The model of the car.
    - status (bool): The status of the car's engine (True if running, False if off).
    """

    def __init__(self, name, year, model):
        """
        Initialize a Car object with the given attributes.
        you want to pass name,model, year because ech instance needs to be unique , for status you can access it sperately as it not fixed and would need cahnges.
        """
        self.name = name
        self.year = year
        self.model = model
        self.status = False  # Default status is set to False (car engine is off)

    def start(self):
        """
        Start the car's engine by setting the status to True.
        """
        self.status = True

    def stop(self):
        """
        Stop the car's engine by setting the status to False.
        """
        self.status = False

    def currentStatus(self):
        """
        Get the current status of the car's engine.

        Returns:
        - str: The status message indicating whether the car's engine is running or off.
        """
        if self.status:
            return "The engine is running"
        else:
            return "The engine is off"
