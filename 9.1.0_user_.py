class User:
    def __init__(self, first_name, last_name):
        """user details"""
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = f"{first_name} {last_name}"
    def describe_user(self):
        """Summry of the user details."""
        print(f"User name is {self.first_name.title()} {self.last_name}.")

    def greet_user(self):
        """Greeting a user."""
        print(f"Hello Mr.{self.full_name.upper()}")

client = User("rishu", "singh")

client.describe_user()
client.greet_user()