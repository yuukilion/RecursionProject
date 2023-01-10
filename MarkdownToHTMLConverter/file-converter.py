import sys
import markdown
import os

def convert_to_HTML(input_path, output_path):
    with open(input_path, 'r') as input_file:
        input_contents = input_file.read()
        processed_contents = markdown.markdown(input_contents)
    with open(output_path, 'w') as output_file:
        output_file.write(processed_contents)

def main():
    arg_length = len(sys.argv)
    
    if arg_length != 4:
        print('Error: wrong number of arguments')
        sys.exit(1)

    command = sys.argv[1]
    input_path = sys.argv[2]
    output_path = sys.argv[3]
    
    if command != 'markdown':
        print('Error: unknown command')
        sys.exit(1)

    elif not os.path.exists(input_path):
        print('Error: The entered Path does not exist')
        sys.exit(1)

    convert_to_HTML(input_path,output_path)
    sys.exit(0)

if __name__ == "__main__":
    main()