class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.preferences = {}
        self.saved_items = []
        self.categories = {}

    def update_preferences(self, preferences):
        self.preferences.update(preferences)

    def save_item(self, item):
        self.saved_items.append(item)

    def create_category(self, category_name):
        if category_name not in self.categories:
            self.categories[category_name] = []

    def add_to_category(self, category_name, item):
        if category_name in self.categories:
            self.categories[category_name].append(item)

    def get_saved_items(self):
        return self.saved_items

    def get_categories(self):
        return self.categories

    def __str__(self):
        return f"User(username={self.username}, email={self.email}, preferences={self.preferences})"