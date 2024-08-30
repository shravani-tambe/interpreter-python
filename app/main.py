import sys

def main():
    print("Logs from your program will appear here!", file=sys.stderr)
    
    if len(sys.argv) < 3:
        print("Usage: ./your_program.sh tokenize <filename>", file=sys.stderr)
        exit(1)
    
    command = sys.argv[1] #no of arguments
    filename = sys.argv[2] #name of file
    
    if command != "tokenize":
        print(f"Unknown command: {command}", file=sys.stderr)
        exit(1)
    
    with open(filename) as file:
        file_contents = file.read()
    
    if file_contents:
        for i in file_contents:
            if i == "(":
                print("LEFT_PAREN ( null")
            elif i == ")":
                print("RIGHT_PAREN ) null")
    
    print("EOF  null")

if __name__ == "__main__":
    main()
