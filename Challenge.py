# Accept user input to create a list of integers
numbers = input("Enter integers separated by spaces: ").split()
numbers = [int(num) for num in numbers]  # Convert strings to integers

# Compute the sum
total = sum(numbers)
print(f"Sum of the integers: {total}")



# Create a tuple of favorite books
favorite_books = ("The Alchemist", "1984", "To Kill a Mockingbird", "The Great Gatsby", "Atomic Habits")

# Print each book on a new line
for book in favorite_books:
    print(book)

    # Store person's info in a dictionary
person = {}

# Ask for user input
person["name"] = input("Enter your name: ")
person["age"] = int(input("Enter your age: "))
person["favorite_color"] = input("Enter your favorite color: ")

# Print the dictionary
print("\nPerson's Information:")
print(person)

# Accept user input for two sets of integers
set1 = set(map(int, input("Enter integers for set 1 (separated by spaces): ").split()))
set2 = set(map(int, input("Enter integers for set 2 (separated by spaces): ").split()))

# Find common elements
common_elements = set1 & set2  # or set1.intersection(set2)
print(f"Common elements: {common_elements}")


# List of words
words = ["apple", "banana", "cat", "dog", "elephant", "fox"]

# New list with words having odd number of characters
odd_length_words = [word for word in words if len(word) % 2 != 0]
print(f"Words with odd number of characters: {odd_length_words}")