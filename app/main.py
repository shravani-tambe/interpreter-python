import sys

def main():
    print("Logs from your program will appear here!", file=sys.stderr)
    
    if len(sys.argv) < 3:
        print("Usage: ./your_program.sh tokenize <filename>", file=sys.stderr)
        exit(1)
    
    command = sys.argv[1]
    filename = sys.argv[2]
    
    if command != "tokenize":
        print(f"Unknown command: {command}", file=sys.stderr)
        exit(1)
    
    with open(filename) as file:
        file_contents = file.read()
    
    if file_contents:
        for c in file_contents:
            if c == "(":
                print("LEFT_PAREN ( null")
            elif c == ")":
                print("RIGHT_PAREN ) null")
    else:
        print("EOF  null")  # Handle empty file case
    
    print("EOF  null")  # Ensure EOF is printed at the end

if __name__ == "__main__":
    main()
