# Muaaz Abed mma210009 CS 4348-502

import os
from btree import BTree

def ui(filename):
    while 1:
        print("--- Menu ---" if filename == "" else "--- Menu(" + f"{filename}) ---")
        print("\tcreate\tCreate new index")
        print("\topen\tSet current index")
        print("\tinsert\tInsert a new key/value pair into current index")
        print("\tsearch\tSearch for a key in current index")
        print("\tload\tinsert key/value pairs from a file into current index")
        print("\tprint\tprint all key/value pairs in current index in key order")
        print("\textract\tsave all key/value pairs in current index into a file")
        print("\tquit\tExit the program\n")
        
        choice = input("Enter command: ").lower()
        match choice:
            case "create":
                return choice
            case "open":
                return choice
            case "insert":
                return choice
            case "search":
                return choice
            case "load":
                return choice
            case "print":
                return choice
            case "extract":
                return choice
            case "quit":
                return choice
            case _:
                print("\n!! No command \"" + choice + "\". Try again !!\n")
                
def main():
    MAGIC_NUMBER = b"4337PRJ3"
    filename = ""
    btree = None
    
    while 1:
        match ui(filename):
            case "create":
                filename = input("Enter the filename: ")
                if os.path.exists(filename):
                    if input("File already exists. Overwrite? (Y/N): ").lower() != 'y':
                        continue
                with open(filename, "wb") as f:
                    f.write(MAGIC_NUMBER)
                    f.write((0).to_bytes(8, 'big'))  # Root node block ID
                    f.write((1).to_bytes(8, 'big'))  # Next block ID
                    f.write(b'\x00' * (512 - 24))  # Padding
                print(f"Created new file: {filename}")
                btree = BTree(root_block_id=0)
                print(f"{filename} is open.\n")
            
            case "open":
                current_files = os.listdir(os.getcwd())
                if not current_files:
                    print("Error: No available files.\n")
                    continue
                print("Available files:")
                for file in current_files:
                    print(f"\t{file}")
                filename = input("Enter the filename: ")
                path = os.path.join(os.getcwd(), filename)
                if not os.path.exists(path):
                    print(f"Error: {filename} doesn't exist.")
                    continue
                with open(filename, "rb") as f:
                    if f.read(8) != MAGIC_NUMBER:
                        print("Error: File format is invalid.")
                        btree = None
                        continue
                    root_block_id = int.from_bytes(f.read(8), 'big')
                print(f"Opened file: {filename}")
                btree = BTree(root_block_id=root_block_id)
                print(f"{filename} is open.\n")
                
            case "insert":
                if not btree:
                    print("Error: No file is open.\n")
                    continue
                try:
                    key = to_unsigned_int(input("Enter key: "))
                    value = to_unsigned_int(input("Enter value: "))
                    btree.insert(key, value)
                except ValueError as e:
                    print(f"Error: {e}")

            case "search":
                if not btree:
                    print("Error: No file is open.")
                    continue
                try:
                    key = to_unsigned_int(input("Enter key to search: "))
                    result = btree.search(key)
                    if result is None:
                        print("Key not found.")
                    else:
                        print(f"Found: Key={result[0]}, Value={result[1]}")
                except ValueError as e:
                    print(f"Error: {e}")
                    
            case "load":
                pass
            case "print":
                if not btree:
                    print("Error: No file is open.")
                    continue
                btree.print_tree()
                
            case "extract":
                pass
            
            case "quit":
                print("Exiting the program...")
                break
            
def to_unsigned_int(value):
    n = int(value)
    if n < 0:
        raise ValueError("Value must be positive.")
    return n

def validate_file_overwrite(filename):
    response = input("File already exists. Overwrite? (Y/N): ").lower()
    return response == "y"
    
if __name__ == '__main__':
    main()