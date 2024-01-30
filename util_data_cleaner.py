# process all the .txt files in the text/ folder
# remove timestamps
# creates new files with the new fotmat

import os
import re


def print_filenames():
    directory = 'text/'
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            print(filename)


def process_files():
    directory = 'text/'
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            with open(directory + filename, 'r') as file:
                lines = file.readlines()

            # Extract channel and date from filename
            channel, video_type, date, *title = filename[:-4].split('_')
            title = '_'.join(title).replace(' ', '_')

            # Prepare new content
            new_content = f"Channel: {channel}\nDate: {date}\nContent:\n"
            for line in lines:
                # Remove timestamps
                cleaned_line = re.sub(
                    r'\[\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}\.\d{3}\]\s*', '', line)
                new_content += cleaned_line

            # Write new content to new file
            new_filename = f"Textonly_{channel}_{
                video_type}_{date}_{title}.txt"
            with open(directory + new_filename, 'w') as new_file:
                new_file.write(new_content)


if __name__ == "__main__":
    process_files()
