def display_message():
    """Display a one sentence message telling what your studying"""
    print("I am learning python crash course.")
display_message()
def favorite_book(book):
    """function to display my favorite book"""
    print(f"One of my favorite book is {book.title()}!")
favorite_book('Atomic habit')
def make_shirt(size, message):
    """Summarize the shirt that's going to be made."""
    print("\nI'm going to make a " + size + " t-shirt.")
    print('That means, "' + message + '"')

make_shirt('large', 'It made for big size men!')
make_shirt(message="That is for people like us.", size='medium')
def make_shirt(size='large', message='for big size men!'):
    """Summarize the shirt that's going to be made."""
    print("\nI'm going to make a " + size + " t-shirt.")
    print('That is made,'+ message +'')

make_shirt()
make_shirt(size='medium',message='for medium size men')
make_shirt('small', 'for small size men.')
"""describe cities"""
def describe_city(city, country):
    msg = city.title() + " is in " + country.title() + "."
    print(msg)

describe_city('Abuja', 'Nigeria')
describe_city('Accra', 'Ghana')
describe_city('Nairobi','Kenya')
def city_country(city, country):
    """Return a string like 'Santiago, Chile'."""
    return(city.title() + "," + country.title())

city = city_country('Abuja','Nigeria')
print(city)

city = city_country('Accra','Ghana')
print(city)

city = city_country('Nairobi','Kenya')
print(city)
def make_album(artist, title):
    """Build a dictionary containing information about an album."""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    return album_dict

album = make_album('The beatley', 'Abbey Road')
print(album)

album = make_album('Elvis prestley', 'Something for Everybody')
print(album)

album = make_album('Michael Jackson', 'Trailers')
print(album)
def make_album(artist, title, tracks=0):
    """Build a dictionary containing information about an album."""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict

album = make_album('The beatley', 'Abbey Road')
print(album)

album = make_album('Elvis Prestley', 'Something for Everybody')
print(album)

album = make_album('Micheal Jackson', 'Trailers')
print(album)

album = make_album('Taylor swift', 'forklore', tracks=50)
print(album)
def make_album(artist, title, tracks=0):
    """Build a dictionary containing information about an album."""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict

# Prepare the prompts.
title_prompt = "\nWhat album are you thinking of? "
artist_prompt = "Who's the artist? "

# Let the user know how to quit.
print("Enter 'quit' at any time to stop.")

while True:
    title = input(title_prompt)
    if title == 'quit':
        break
    
    artist = input(artist_prompt)
    if artist == 'quit':
        break

    album = make_album(artist, title)
    print(album)

print("\nThanks for responding!")

def show_messages(messages):
    """Print all messages in the list."""
    for message in messages:
        print(message)

messages = ["hello Bala", "how are u?"]
show_messages(messages)
def show_messages(messages):
    """Print all messages in the list."""
    print("Showing all messages:")
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    """Print each message, and then move it to sent_messages."""
    print("\nSending all messages:")
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

messages = ["hello Bala", "how are u doing?"]
show_messages(messages)

sent_messages = []
send_messages(messages, sent_messages)

print("\nFinal lists:")
print(messages)
print(sent_messages)



def send_messages(messages, sent_messages):
    """Print each message, and then move it to sent_messages."""
    print("\nSending all messages:")
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

messages = ["hello Bala", "how are u doing?"]
show_messages(messages)

sent_messages = []
send_messages(messages, sent_messages)

print("\nFinal lists:")
print(messages)
print(sent_messages)

def make_sandwich(*items):
    """Make a sandwich with the given items."""
    print("\nI'll make you a great sandwich:")
    for item in items:
        print("Will be adding " + item + " to your sandwich.")
    print("Your sandwich is ready!")

make_sandwich('roast beef', 'cheddar cheese', 'lettuce', 'honey dijon')
make_sandwich('turkey', 'apple slices', 'honey mustard')
make_sandwich('peanut butter', 'strawberry jam')

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
    
    
user_profile = build_profile('Bala', 'Abduljalil', location='Maiduguri',
field='Computing')
my_profile = build_profile('Bala', 'Abduljalil', location = 'Maiduguri', field = 'Computing')
print(user_profile)
print(my_profile)


def make_car(manufacturer, model, **options):
    """Make a dictionary representing a car."""
    car_dict = {
        'manufacturer': manufacturer.title(),
        'model': model.title(),
        }
    for option, value in options.items():
        car_dict[option] = value

    return car_dict

my_outback = make_car('subaru', 'outback', color='blue', tow_package=True)
print(my_outback)

my_new_benz = make_car('Mercedez', 'Benz', year=2022,color='Black',
        headlights='popup')
print(my_new_benz)

def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
        
def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
import printing_functions as pf

unprinted_designs = ['Samsung mobile', 'headpiece', 'xender']
completed_models = []

pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)