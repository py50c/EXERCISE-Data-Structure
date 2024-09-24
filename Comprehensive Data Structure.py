# 1. Lists
def list_operations():
    print("List Operations:")
    # Creating a list of 5 numbers (user input)
    numbers = [int(input(f"Enter number {i+1}: ")) for i in range(5)]
    
    # Appending a new number to the list
    numbers.append(int(input("Enter a number to append: ")))
    
    # Inserting a number at a specific position
    insert_num = int(input("Enter a number to insert: "))
    position = int(input(f"Enter the position to insert {insert_num} (0-{len(numbers)}): "))
    numbers.insert(position, insert_num)
    
    # Removing a number from the list
    remove_num = int(input("Enter a number to remove from the list: "))
    if remove_num in numbers:
        numbers.remove(remove_num)
    else:
        print(f"{remove_num} not found in the list.")
    
    # Slicing the list to display the first 3 elements
    print(f"First 3 elements of the list: {numbers[:3]}")
    
    # Using list comprehension to create a new list with each number squared
    squared_numbers = [num ** 2 for num in numbers]
    print(f"List with squared numbers: {squared_numbers}")
    print("-" * 30)

# 2. Tuples
def tuple_operations():
    print("Tuple Operations:")
    # Creating a tuple with 3 strings
    cities = ("New York", "Paris", "Tokyo")
    
    # Accessing and printing the second element
    print(f"Second city: {cities[1]}")
    
    # Unpacking the tuple into individual variables
    city1, city2, city3 = cities
    print(f"Unpacked cities: {city1}, {city2}, {city3}")
    
    # Demonstrating tuple immutability
    try:
        cities[1] = "London"  # This will raise an error
    except TypeError as e:
        print(f"Error: {e}")
    print("-" * 30)

# 3. Dictionaries
def dictionary_operations():
    print("Dictionary Operations:")
    # Creating a dictionary with information about a book
    book = {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "year": 1925
    }
    
    # Accessing and printing the title
    print(f"Book title: {book['title']}")
    
    # Adding a new key-value pair (e.g., genre)
    book["genre"] = "Novel"
    print(f"Updated book dictionary: {book}")
    
    # Using a method to retrieve the value of a key that might not exist
    isbn = book.get("ISBN", "ISBN not available")
    print(f"ISBN: {isbn}")
    
    # Creating a nested dictionary for multiple books
    library = {
        "book1": {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
        "book2": {"title": "1984", "author": "George Orwell", "year": 1949}
    }
    
    # Accessing the author of the second book
    print(f"Author of the second book: {library['book2']['author']}")
    print("-" * 30)

# 4. Sets
def set_operations():
    print("Set Operations:")
    # Creating a set of 5 unique numbers (user input)
    numbers_set = {int(input(f"Enter unique number {i+1}: ")) for i in range(5)}
    
    # Adding a new number to the set
    numbers_set.add(int(input("Enter a number to add to the set: ")))
    
    # Removing a number from the set
    remove_num = int(input("Enter a number to remove from the set: "))
    if remove_num in numbers_set:
        numbers_set.remove(remove_num)
    else:
        print(f"{remove_num} is not in the set.")
    
    # Performing union and intersection with another set
    other_set = {6, 7, 8, 9, 10}
    union_set = numbers_set.union(other_set)
    intersection_set = numbers_set.intersection(other_set)
    
    print(f"Union of sets: {union_set}")
    print(f"Intersection of sets: {intersection_set}")
    
    # Set difference (elements only in the first set)
    difference_set = numbers_set.difference(other_set)
    print(f"Difference (only in the first set): {difference_set}")
    print("-" * 30)

# Main function to run all operations
def main():
    list_operations()
    tuple_operations()
    dictionary_operations()
    set_operations()

main()
