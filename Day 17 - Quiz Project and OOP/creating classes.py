# PascalCase = start of each word is capitalized
# camelCase = first word is capitalized, and next words are capitalized
# snake case = snake_case words separated by underscores
# constructor by using __init__ = initialize attributes

# attributes are something an object HAS
# a methond is something an object can DO
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    
    
    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "angela")
user_2 = User("002", "jack")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)

user_2.follow(user_1)
print(user_2.followers)
print(user_2.following)


print(user_1.followers)
print(user_1.following)
