# read all files and get last two numbers separated by _
import os
import sys

def get_last_two_numbers(filename):
    # split the filename by _ and get the last two numbers
    parts = filename.split('_')
    if len(parts) < 2:
        return None
    try:
        num1 = int(parts[-2])
        num2 = int(parts[-1].split('.')[0])  # remove file extension
        return num1, num2
    except ValueError:
        return None

def sort_files_by_numbers(directory):
    files = os.listdir(directory)
    files_with_numbers = []
    
    for file in files:
        numbers = get_last_two_numbers(file)
        if numbers is not None:
            files_with_numbers.append((file, numbers))
    
    # sort by the last two numbers
    sorted_files = sorted(files_with_numbers, key=lambda x: (x[1][0], x[1][1]))
    
    return [file[0] for file in sorted_files]

if __name__ == "__main__":
    directory = sys.argv[1] if len(sys.argv) > 1 else "."
    sorted_files = sort_files_by_numbers(directory)
        
    # extract the last two numbers and get the charcter in the second number position in each file content
    string = ""
    for file in sorted_files:
        numbers = get_last_two_numbers(file)
        if numbers is not None:
            num1, num2 = numbers
            with open(os.path.join(directory, file), 'r') as f:
                content = f.read()
                if num2 < len(content):
                    string += content[num2]
    print(string)