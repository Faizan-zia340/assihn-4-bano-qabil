def create_alphabet(file_path, letters_per_line):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    file = open(file_path, 'w')

    for i in range(0, len(alphabet), letters_per_line):
        line = alphabet[i:i + letters_per_line]
        file.write(line + '\n')

    print(f"File '{file_path}' created successfully!")

    file.close()


file1 = input("Enter the path for the alphabet file: ")
letters_per_line = int(input("Enter the number of letters per line: "))

create_alphabet(file1, letters_per_line)