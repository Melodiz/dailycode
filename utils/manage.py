import os

def replace_spaces_in_filenames(directory):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if ' ' in filename or '-' in filename:
                new_filename = filename.strip().replace(' ', '_').replace('-', '_')
                old_file = os.path.join(root, filename)
                new_file = os.path.join(root, new_filename)
                os.rename(old_file, new_file)
                print(f'Renamed: {filename} -> {new_filename}')

if __name__ == "__main__":
    directory = "/Users/melodiz/code/leetcode"
    replace_spaces_in_filenames(directory)