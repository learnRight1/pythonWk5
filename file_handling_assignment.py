# file_handling_assignment.py

def create_and_write_file():
    try:
        # File Creation
        with open("my_file.txt", 'w') as file:
            file.write("Hello, friend!\n")
            file.write("Python file handling is fun.\n")
            file.write("Here's my number if you need help: +2349012713755.\n")
        print("File created and data written successfully.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"An error occurred: {e}")
    finally:
        print("File creation and writing process completed.")

def read_and_display_file():
    try:
        # File Reading and Display
        with open("my_file.txt", 'r') as file:
            content = file.read()
        print("\nFile content:")
        print(content)
    except (FileNotFoundError, PermissionError) as e:
        print(f"An error occurred: {e}")
    finally:
        print("File reading process completed.")

def append_to_file():
    try:
        # File Appending
        with open("my_file.txt", 'a') as file:
            file.write("Learning python is easy.\n")
            file.write("If you choose to learn it in PLP.\n")
            file.write("Our instructors are great.\n")
        print("Data appended to the file successfully.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"An error occurred: {e}")
    finally:
        print("File appending process completed.")

def main():
    create_and_write_file()
    read_and_display_file()
    append_to_file()
    read_and_display_file()

if __name__ == "__main__":
    main()
