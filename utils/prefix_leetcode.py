import json
import os

def read_json_and_form_dict(file_path = 'utils/leetcode_data/problemslist.json'):
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    question_dict = {}
    for item in data['stat_status_pairs']:
        question_dict[item['stat']['question__title_slug'].replace('-', '_').lower()] = item['stat']['frontend_question_id']
        question_dict[item['stat']['question__title'].replace(' ', '_').lower()] = item['stat']['frontend_question_id']
    
    return question_dict

def add_prefix_number(directory, map_dict):
    count = 0
    total = 0
    for root, dirs, files in os.walk(directory):
        for filename in files:
            total+=1
            name = (filename.split('.')[0]).lower()
            if '-' in filename or filename[0].isdigit(): continue
            elif name in map_dict and '-' not in filename:
                new_filename = f"{map_dict[name]}-{filename}"
                print(f'Renamed: {filename} -> {new_filename}')
                os.rename(os.path.join(root, filename), os.path.join(root, new_filename))
                count += 1
            else:
                print(f'Missing: {root.split("/")[-1]} {name}')
    print(f'Renamed files: {count}, Total files: {total}')

def simple_spaces_replacer(directory):
    # rename all files in the directory (including subdirectories) 
    # example: "124. Reverse Words in a String III.cpp" -> "124-Reverse_Words_in_a_String_III.cpp"
    count = 0
    total = 0
    for root, dirs, files in os.walk(directory):
        for filename in files:
            total += 1
            if ' ' in filename:
                # Split the filename into number part and the rest
                parts = filename.split('. ', 1)
                if len(parts) == 2:
                    number, rest = parts
                    # Replace spaces with underscores in the rest of the filename
                    rest = rest.replace(' ', '_')
                    new_filename = f"{number}-{rest}"
                else:
                    # If there's no number part, just replace spaces with underscores
                    new_filename = filename.replace(' ', '_')

                old_path = os.path.join(root, filename)
                new_path = os.path.join(root, new_filename)
                try:
                    # os.rename(old_path, new_path)
                    print(f'Renamed: {filename} -> {new_filename}')
                    count += 1
                except OSError as e:
                    print(f'Error renaming {filename}: {e}')
    
    print(f'Renamed files: {count}, Total files: {total}')

if __name__ == "__main__":
    # question_dict = read_json_and_form_dict()
    # directory = "/Users/melodiz/code/leetcode"
    # add_prefix_number(directory, question_dict)
    simple_spaces_replacer('/Users/melodiz/code/leetcode')
