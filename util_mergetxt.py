# script that takes all the txt files in a specified folder and outputs one single txt file also in a specified folder and name where the content is the contents of all txt files merged, and divided by an empty row

import os

input_folder_path = './text/ThinkingBasketballSmallSample/'
output_folder_path = './text_library/'
output_file_name = 'ThinkingBasketball_202306-202401.txt'


def merge_files(input_folder, output_folder, output_filename):
    with open(os.path.join(output_folder, output_filename), 'w') as outfile:
        for filename in os.listdir(input_folder):
            if filename.endswith(".txt"):
                with open(os.path.join(input_folder, filename), 'r') as infile:
                    outfile.write(infile.read())
                    outfile.write('\n\n')  # Add an empty row between files


if __name__ == "__main__":
    merge_files(input_folder_path, output_folder_path, output_file_name)
