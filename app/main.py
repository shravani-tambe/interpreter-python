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
        raise NotImplementedError("Scanner not implemented")
    else:
        print("EOF  null")
        
        
    for i in file_contents: 
        if i=="(": 
            print("LEFT PARANTHESE ( NULL")
        if i==")": 
            print("LEFT PARANTHESE ) NULL")
            
    print("EOF Null")

if __name__ == "__main__":
    main()
