class Restaurant():
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        msg = self.name + " serves wonderful " + self.cuisine_type + "."
        print("\n" + msg)
    def open_restaurant(self):
        msg = self.name + " is open for service from today. Come on in!"
        print("\n" + msg)
restaurant = Restaurant('Alheri Restaurant', 'eatering')
print(restaurant.name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

class Restaurant():
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = self.name + " serves wonderful " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = self.name + " is open. Come on in!"
        print("\n" + msg)

Alhari_Restaurant = Restaurant('Alhari Restaurant', 'pizza')
Alhari_Restaurant.describe_restaurant()

Unique = Restaurant('The unique Restuarant', 'snacks')
Unique.describe_restaurant()

HauBala_Restaurant = Restaurant('HauBala Restaurant', 'Hausa Food')
HauBala_Restaurant.describe_restaurant()


class User():
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()

    def describe_user(self):
        """Display a summary of the user's information."""
        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print("\nYou are welcome, " + self.username + "!")

my_user = User('Bala', 'Abduljalil', 'Engr.Balla', 'ballaabduljalil@gmail.com', 'Maiduguri')
my_user.describe_user()
my_user.greet_user()

self_user = User('hauwa', 'bashir', 'h_bashir', 'h_bashir@mom.com', 'Jalingo')
self_user.describe_user()
self_user.greet_user()

class Restaurant():
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = f"{self.name} is open. Come on in!"
        print(f"\n{msg}")

    def set_number_served(self, number_served):
        """Allow user to set the number of customers that have been served."""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """Allow user to increment the number of customers served."""
        self.number_served += additional_served


restaurant = Restaurant('Alhari Restaurant', 'eatering')
restaurant.describe_restaurant()

print(f"\nNumber served: {restaurant.number_served}")
restaurant.number_served = 340
print(f"Number served: {restaurant.number_served}")

restaurant.set_number_served(1327)
print(f"Number served: {restaurant.number_served}")

restaurant.increment_number_served(945)
print(f"Number served: {restaurant.number_served}")


class User():
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, location):      
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0
    def describe_user(self):
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")

    def greet_user(self):
        print(f"\nWelcome back, {self.username}!")

    def increment_login_attempts(self):        
        self.login_attempts += 1
    def reset_login_attempts(self):        
        self.login_attempts = 0
my_user = User('Bala', 'Abduljalil', 'Balla', 'ballaabduljalil@gmail.com', 'Maiduguri')
my_user.describe_user()
my_user.greet_user()
print("\nMaking 3 login attempts...")
my_user.increment_login_attempts()
my_user.increment_login_attempts()
my_user.increment_login_attempts()
print(f"  Login attempts: {my_user.login_attempts}")

print("Resetting login attempts...")
my_user.reset_login_attempts()
print(f"  Login attempts: {my_user.login_attempts}")


class Restaurant():
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):      
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):      
        msg = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")
    def open_restaurant(self):        
        msg = f"{self.name} is open. Come on in!"
        print(f"\n{msg}")
    def set_number_served(self, number_served):        
        self.number_served = number_served
    def increment_number_served(self, additional_served):        
        self.number_served += additional_served
class IceCreamStand(Restaurant):   
    def __init__(self, name, cuisine_type='ice cream'):        
        super().__init__(name, cuisine_type)
        self.flavors = []
    def show_flavors(self):        
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")
big_one = IceCreamStand('Alhari Restaurant')
big_one.flavors = ['strewberry', 'cookies and cream', 'caramel']
big_one.describe_restaurant()
big_one.show_flavors()

class User():
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """Display a summary of the user's information."""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")
    def greet_user(self):       
        print(f"\nWelcome back, {self.username}!")
    def increment_login_attempts(self):       
        self.login_attempts += 1
    def reset_login_attempts(self):
        """Reset login_attempts to 0."""
        self.login_attempts = 0
class Admin(User):
    """A user with administrative privileges."""
    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the admin."""
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = []
    def show_privileges(self):       
        print("\nPrivileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")
my_user = Admin('Bala', 'Abduljalil', 'Balla', 'ballaabduljalil@gmail.com', 'Maiduguri')
my_user.describe_user()
my_user.privileges = [
    '...You can reset passwords',
    '...You can moderate discussions',
    '...You can suspend accounts',
    ]

my_user.show_privileges()

class User():
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):      
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")

    def greet_user(self):
        print(f"\nWelcome back, {self.username}!")
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0
class Admin(User):
    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)     
        self.privileges = Privileges()
class Privileges():
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("- This user has no privileges.")


my_user = Admin('Bala', 'Abduljalil', 'Balla', 'ballaabduljalil@gmail.com', 'Maiduguri')
my_user.describe_user()
my_user.privileges.show_privileges()

print("\nAdding privileges...")
my_user_privileges = [
    '...You can reset passwords',
    '...You can moderate discussions',
    '...You can suspend accounts',
    ]
my_user.privileges.privileges = my_user_privileges
my_user.privileges.show_privileges()



class Car():
    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
        
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles
class Battery():
    def __init__(self, battery_size=75):   
        self.battery_size = battery_size
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315          
        message = f"This car can go approximately {range}"
        message += " miles on a full charge."
        print(message)
    def upgrade_battery(self):
        if self.battery_size == 75:
            self.battery_size = 100
            print("Upgraded the battery to 100 kWh.")
        else:
            print("The battery is already upgraded.")     
class ElectricCar(Car):
    def __init__(self, manufacturer, model, year):
        super().__init__(manufacturer, model, year)
        self.battery = Battery()
print("Make an electric car, and check the range:")
my_tesla = ElectricCar('tesla', 'roadster', 2019)
my_tesla.battery.get_range()

print("\nUpgrade the battery, and check the range again:")
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()


class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        msg = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        msg = f"{self.name} is open. Come on in!"
        print(f"\n{msg}")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        self.number_served += additional_served

#user.py
class User():
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")

    def greet_user(self):
        print(f"\nWelcome back, {self.username}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
class Admin(User):
    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)     
        self.privileges = Privileges()
class Privileges():
    def __init__(self, privileges=[]):
        self.privileges = privileges
    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("- This user has no privileges.")

#dice            
from random import randint
class Die():
    def __init__(self, sides=6):
        self.sides = sides
    def roll_die(self):
        return randint(1, self.sides)
d6 = Die()
results = []
for roll_num in range(10):
    result = d6.roll_die()
    results.append(result)
print("The 10 rolls of a 6-sided die are:")
print(results)
d10 = Die(sides=10)
results = []
for roll_num in range(10):
    result = d10.roll_die()
    results.append(result)
print("\nThe 10 rolls of a 10-sided die are:")
print(results)
d20 = Die(sides=20)
results = []
for roll_num in range(10):
    result = d20.roll_die()
    results.append(result)
print("\nThe 10 rolls of a 20-sided die are:")
print(results)

#lottery
from random import choice
possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
winning_ticket = []
print("Let's see what the winning ticket is...")
while len(winning_ticket) < 3:
    pulled_item = choice(possibilities)
    if pulled_item not in winning_ticket:
        print(f"  We pulled a {pulled_item}!")
        winning_ticket.append(pulled_item)
#lottery analysis
from random import choice
def get_winning_ticket(possibilities):
    winning_ticket = []
    while len(winning_ticket) < 4:
        pulled_item = choice(possibilities)
        if pulled_item not in winning_ticket:
            winning_ticket.append(pulled_item)
    return winning_ticket
def check_ticket(played_ticket, winning_ticket):
    for element in played_ticket:
        if element not in winning_ticket:
            return False
    return True
def make_random_ticket(possibilities):
    ticket = []
    while len(ticket) < 4:
        pulled_item = choice(possibilities)
        if pulled_item not in ticket:
            ticket.append(pulled_item)
    return ticket
possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
winning_ticket = get_winning_ticket(possibilities)
plays = 0
won = False
max_tries = 1_000_000
while not won:
    new_ticket = make_random_ticket(possibilities)
    won = check_ticket(new_ticket, winning_ticket)
    plays += 1
    if plays >= max_tries:
        break
if won:
    print("We have a winning ticket!")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")
    print(f"It only took you {plays} tries to win!")
else:
    print(f"Tried {plays} times, without pulling a winner. :(")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")