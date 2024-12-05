def ui():
    while 1:
        print("--- Menu ---")
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
                print("!! No command \"" + choice + "\". Try again !!\n")
                
def main():
    print(ui())
    
if __name__ == '__main__':
    main()