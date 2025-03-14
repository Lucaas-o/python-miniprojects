import json

class RecipeManager:
    def __init__(self, filename="recipes.json"):
        self.filename = filename
        self.load_recipes()

    def load_recipes(self):
        try:
            with open(self.filename, "r") as file:
                self.recipes = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.recipes = {}

    def save_recipes(self):
        with open(self.filename, "w") as file:
            json.dump(self.recipes, file, indent=4)

    def add_recipe(self, name, ingredients, steps):
        self.recipes[name] = {"ingredients": ingredients, "steps": steps}
        self.save_recipes()
        print(f"Recipe '{name}' added successfully!")

    def edit_recipe(self, name, ingredients=None, steps=None):
        if name in self.recipes:
            if ingredients:
                self.recipes[name]["ingredients"] = ingredients
            if steps:
                self.recipes[name]["steps"] = steps
            self.save_recipes()
            print(f"Recipe '{name}' updated successfully!")
        else:
            print(f"Recipe '{name}' not found.")

    def remove_recipe(self, name):
        if name in self.recipes:
            del self.recipes[name]
            self.save_recipes()
            print(f"Recipe '{name}' removed successfully!")
        else:
            print(f"Recipe '{name}' not found.")

    def search_recipes(self, keyword):
        results = {name: data for name, data in self.recipes.items() if keyword.lower() in name.lower() or any(keyword.lower() in ing.lower() for ing in data["ingredients"])}
        if results:
            for name, details in results.items():
                self.display_recipe(name)
        else:
            print("No matching recipes found.")

    def list_recipes(self):
        if not self.recipes:
            print("No recipes available.")
        else:
            for name in self.recipes:
                self.display_recipe(name)

    def display_recipe(self, name):
        if name in self.recipes:
            print(f"\nRecipe: {name}")
            print("Ingredients:")
            for ingredient in self.recipes[name]["ingredients"]:
                print(f"- {ingredient}")
            print("Steps:")
            for i, step in enumerate(self.recipes[name]["steps"], 1):
                print(f"{i}. {step}")
        else:
            print(f"Recipe '{name}' not found.")

if __name__ == "__main__":
    manager = RecipeManager()
    while True:
        print("\nOptions: add, edit, remove, search, list, exit")
        choice = input("Choose an action: ").strip().lower()
        if choice == "add":
            name = input("Recipe name: ")
            ingredients = input("Ingredients (comma-separated): ").split(",")
            steps = input("Steps (comma-separated): ").split(",")
            manager.add_recipe(name, [i.strip() for i in ingredients], [s.strip() for s in steps])
        elif choice == "edit":
            name = input("Recipe name to edit: ")
            ingredients = input("New ingredients (leave blank to keep current): ")
            steps = input("New steps (leave blank to keep current): ")
            manager.edit_recipe(name, ingredients.split(",") if ingredients else None, steps.split(",") if steps else None)
        elif choice == "remove":
            name = input("Recipe name to remove: ")
            manager.remove_recipe(name)
        elif choice == "search":
            keyword = input("Enter keyword to search: ")
            manager.search_recipes(keyword)
        elif choice == "list":
            manager.list_recipes()
        elif choice == "exit":
            break
        else:
            print("Invalid choice. Try again.")
