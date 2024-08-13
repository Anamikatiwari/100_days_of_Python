
## creating class
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    
    def follow(self, user): 
        user.followers += 1
        self.following += 1
  
user_1 = User("001", "anamika") 
user_2 = User("002", "ABC") 

user_1.follow(user_2)
user_1.followers
user_1.following
user



print(user_1.followers)

# PascalCase 
# camelCase
# snake_case






