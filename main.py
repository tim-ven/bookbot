def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")

    # Move the character_count function call inside main
    character_counts = character_count(text)

    # Create and sort character dictionary
    char_dict = [{'character': key, 'count': value} for key, value in character_counts.items()]
    sorted_items = sorted(char_dict, reverse=True, key=sort_on)

    # Print sorted character counts line by line
    for item in sorted_items:
        character = item['character']
        count = item['count']
        print(f"'{character}' appears {count} times")

    print("--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def character_count(count):
    characters = {}
    lower_case = count.lower()
    for character in lower_case:
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
    return characters

def sort_on(char_dict):
    return char_dict['count']

# Call the main function to run the program
if __name__ == "__main__":
    main()



