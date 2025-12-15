class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")

    def display_timeline(self):
        print(self.username)
        for i in range(len(self.posts)):  # zaczynamy od 0
            print(f'{i + 1} {self.posts[i]}')

user1 = SocialMediaProfile('johndoe')
user1.add_post('Hello, world!')
user1.add_post('Hello, world!')
user1.add_post('Whats up, Natalie? How are you?')

user1.display_timeline()
    


