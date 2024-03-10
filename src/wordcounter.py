import string

def count_words(text):
    # Removing punctuation and converting to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    # Splitting text into words
    words = text.split()
    # Counting the number of words
    word_count = len(words)
    return word_count

def main():
    print("Welcome to the Word Counter Program!")

    while True:
        choice = input("Enter '1' to input text manually, '2' to input text from a file, or '3' to quit: ")

        if choice == '1':
            text = input("Enter your text: ")
            word_count = count_words(text)
            print(f"Word count: {word_count}\n")
        elif choice == '2':
            file_name = input("Enter the name of the file (including extension): ")
            try:
                with open(file_name, 'r') as file:
                    text = file.read()
                    if not text.strip():
                        print("File is empty.")
                    else:
                        word_count = count_words(text)
                        print(f"Word count: {word_count}\n")
            except FileNotFoundError:
                print("File not found.")
        elif choice == '3':
            print("Thank you for using the Word Counter Program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter '1', '2', or '3'.")

if __name__ == "__main__":
    main()
