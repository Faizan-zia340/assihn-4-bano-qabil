def read_file_and_store_in_list(file_path):
    lines_list = []

    try:
        with open(file_path, 'r') as file:
            lines_list = file.readlines()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

    return lines_list

# Example usage:
file_path = 'fibonacci eries.pys'  # Replace with the path to your file
lines = read_file_and_store_in_list(file_path)

if lines:
    print(f"Contents of the file '{file_path}':")
    for line in lines:
        print(line.strip())
else:
    print("No lines read from the file.")
