from user import Admin

my_user = Admin('Bala', 'Abduljalil', 'Balla', 'ballaabduljalil@gmail.com', 'Maiduguri')
my_user.describe_user()

my_user_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
my_user.privileges.privileges = my_user_privileges

print(f"\nThe admin {my_user.username} has these privileges: ")
my_user.privileges.show_privileges()