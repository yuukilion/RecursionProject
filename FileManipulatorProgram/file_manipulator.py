import sys
import os

def reverse(input_path, output_path):
    with open(input_path, 'r') as input_file:
        original_str = input_file.read()
        reverse_str = original_str[::-1]
    with open(output_path, 'w') as output_file:
        output_file.write(reverse_str)

def copy(input_path, output_path):
    with open(input_path, 'r') as input_file:
        target_str = input_file.read()
    with open(output_path, 'w') as output_file:
        output_file.write(target_str)

def duplicate_contents(input_path, num):
    with open(input_path, 'r') as input_file:
        original_str = input_file.read()
    with open(input_path, 'w') as input_file:
        duplicated_str = ''
        for i in range(num):
            duplicated_str += original_str
        input_file.write(duplicated_str)

def replace_string(input_path, needle, newstring):
    with open(input_path,'r') as input_file:
        original_str = input_file.read()
    with open(input_path,'w') as input_file:
        replaced_str = original_str.replace(needle,newstring)
        input_file.write(replaced_str)

def main():
    
    arg_length = len(sys.argv)
    command_name = sys.argv[1]
    input_path = sys.argv[2]

    if not os.path.exists(input_path):
        print('The entered Path does not exist')
        sys.exit(1)

    if arg_length == 4:

        if command_name == 'reverse':
            output_path = sys.argv[3]
            reverse(input_path, output_path)

        elif command_name == 'copy':
            output_path = sys.argv[3]
            copy(input_path, output_path)

        elif command_name == 'duplicate-contents':
            num = int(sys.argv[3])
            duplicate_contents(input_path, num)

        else:
            print('invalid argument')
            sys.exit(1)
    
    elif arg_length == 5:
        
        if command_name == 'replace-string':
            target_str = sys.argv[3]
            newstring = sys.argv[4]
            replace_string(input_path, target_str, newstring)
        else:
            print('invalid argument')
            sys.exit(1)

    else:
        print('invalid number of arguments')
        sys.exit(1)

    sys.exit(0)

if __name__ == "__main__":
    main()