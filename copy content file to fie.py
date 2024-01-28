source = input("Enter the path to the source file: ")

destin = input("Enter the path to the destination file: ")

with open(source, 'r') as source_file:
    content = source_file.read()

with open(destin, 'w') as destination_file:
    destination_file.write(content)

print("File copied successfully!")