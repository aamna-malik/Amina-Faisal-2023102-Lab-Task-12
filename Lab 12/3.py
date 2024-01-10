def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(f"File content:\n{content}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
file_path = "example.txt"

read_file(file_path)
