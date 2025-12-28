import os
from leetcode_check_utils import validate_problem_folder, validate_global_readme, validate_local_readme


def create_solution_files(problem_slug, topic_folder, problem_data):
    """
    Create problem folder with README and solution template
    
    Args:
        problem_slug: The problem slug from URL
        topic_folder: Target folder (e.g., 'leetcode/Easy')
        problem_data: Extracted problem data
    """
    # Create folder name: number_slug
    folder_name = f"{problem_data['title_num']}_{problem_slug.replace('-', '_')}"
    folder_path = os.path.join(topic_folder, folder_name)
    
    validate_problem_folder(folder_path)
    os.makedirs(folder_path)
    
    # Create README with problem description
    readme_path = os.path.join(folder_path, "readme.md")
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(problem_data['description_text'])
    
    # Create solution.py with template
    solution_path = os.path.join(folder_path, "solution.py")
    with open(solution_path, 'w', encoding='utf-8') as f:
        f.write(f"# Solution for {problem_data['problem_link']}\n")
        f.write(f"# Other solutions: https://github.com/Melodiz/dailycode/tree/main/leetcode\n\n")
        
        # Add common imports
        f.write("from typing import List, Optional\n\n")
        
        # Add the LeetCode code template if available
        if problem_data.get('python_code'):
            f.write(problem_data['python_code'])
            f.write("\n\n")
        else:
            # Default template
            f.write("class Solution:\n")
            f.write("    def solve(self):\n")
            f.write("        pass\n\n")
        
        # Get the method name from the code template
        method_name = "solve"  # default
        if problem_data.get('python_code'):
            import re
            # Find 'class Solution:' then the first 'def' after it (excluding __init__)
            solution_class_match = re.search(r'class Solution.*?:\s*\n\s*def (\w+)\(self', problem_data['python_code'], re.DOTALL)
            if solution_class_match:
                method_name = solution_class_match.group(1)
                # Skip __init__ and other magic methods
                if method_name.startswith('__'):
                    # Try to find the next non-magic method
                    all_methods = re.findall(r'class Solution.*?def (\w+)\(self', problem_data['python_code'], re.DOTALL)
                    for method in all_methods:
                        if not method.startswith('__'):
                            method_name = method
                            break
        
        # Add main function with active test cases
        f.write("def run_tests():\n")
        f.write("    solution = Solution()\n")
        f.write("    \n")
        f.write("    # Test cases: (input_args, expected_output, test_name)\n")
        f.write("    test_cases = [\n")
        
        # Add parsed test cases if available
        test_cases = problem_data.get('case_data', [])
        if test_cases and len(test_cases) > 0:
            for i, test_case in enumerate(test_cases, 1):
                test_input = test_case.get('input', '')
                test_output = test_case.get('output', '')
                
                if test_input and test_input != 'See problem description':
                    # Format: (input_args, expected_output, test_name)
                    if test_output != 'See problem description' and test_output:
                        f.write(f"        ({test_input}, {test_output}, \"Example {i}\"),\n")
                    else:
                        # Add placeholder for expected output - user can fill in from problem description
                        f.write(f"        ({test_input}, None, \"Example {i}\"),  # TODO: Add expected output\n")
        
        f.write("    ]\n")
        f.write("    \n")
        f.write("    for test_input, expected, name in test_cases:\n")
        f.write("        try:\n")
        f.write(f"            result = solution.{method_name}(test_input)\n")
        f.write("            \n")
        f.write("            if expected is not None:\n")
        f.write("                status = \"✓ PASS\" if result == expected else \"✗ FAIL\"\n")
        f.write("                print(f\"{name}: {status}\")\n")
        f.write("                print(f\"  Input:    {test_input}\")\n")
        f.write("                print(f\"  Expected: {expected}\")\n")
        f.write("                print(f\"  Got:      {result}\")\n")
        f.write("            else:\n")
        f.write("                print(f\"{name}:\")\n")
        f.write("                print(f\"  Input:  {test_input}\")\n")
        f.write("                print(f\"  Output: {result}\")\n")
        f.write("        except Exception as e:\n")
        f.write("            print(f\"{name}: ✗ ERROR\")\n")
        f.write("            print(f\"  Input: {test_input}\")\n")
        f.write("            print(f\"  Error: {e}\")\n")
        f.write("        print()\n")
        f.write("\n")
        f.write("if __name__ == \"__main__\":\n")
        f.write("    run_tests()\n")
    
    print(f"OK: created problem folder '{folder_name}' with files")


def update_global_readme(readme_path, problem_slug, topic_folder, problem_data):
    """
    Update the main LeetCode README with new problem entry
    
    Args:
        readme_path: Path to the global README
        problem_slug: The problem slug from URL
        topic_folder: Target folder (e.g., 'leetcode/Easy')
        problem_data: Extracted problem data
    """
    validate_global_readme(readme_path)
    
    # Read current README content
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract difficulty from topic_folder (e.g., 'leetcode/Easy' -> 'Easy')
    difficulty = topic_folder.split('/')[-1]
    
    # Find the appropriate section
    section_marker = f"## {difficulty} <a name=\"leetcode-{difficulty.lower()}\"></a>"
    
    if section_marker not in content:
        print(f"ERROR: section {section_marker} not found in {readme_path}")
        print("Global README.md wasn't updated.")
        return
    
    # Build the new entry
    title_with_num = f"{problem_data['title_num']}. {problem_data['title']}"
    tags_str = f" [{', '.join(problem_data['tags'])}]" if problem_data['tags'] else ""
    
    folder_name = f"{problem_data['title_num']}_{problem_slug.replace('-', '_')}"
    solution_path = f"{difficulty}/{folder_name}"
    
    new_entry = f"* [{title_with_num}]({problem_data['problem_link']}){tags_str} - [Solution]({solution_path})\n"
    
    # Find position to insert
    section_pos = content.find(section_marker)
    next_section_pos = content.find("##", section_pos + len(section_marker))
    
    if next_section_pos == -1:
        # Last section, find next major section
        next_section_pos = content.find("# ", section_pos + len(section_marker))
    
    if next_section_pos == -1:
        insert_pos = len(content)
    else:
        insert_pos = next_section_pos
    
    # Find last entry in current section
    section_content = content[section_pos:insert_pos]
    last_entry_pos = section_content.rfind("* [")
    
    if last_entry_pos == -1:
        # No entries yet, add after section marker
        new_content = (content[:section_pos + len(section_marker)] + 
                      "\n\n" + new_entry + 
                      content[section_pos + len(section_marker):])
    else:
        # Add after last entry
        absolute_pos = section_pos + last_entry_pos
        line_end = content.find("\n", absolute_pos)
        if line_end == -1:
            line_end = len(content)
        
        new_content = content[:line_end + 1] + new_entry + content[line_end + 1:]
    
    # Write updated content
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"OK: updated global README.md with new problem entry")
    return new_entry


def update_local_readme(readme_path, problem_slug, topic_folder, problem_data):
    """
    Update the difficulty-specific README with new problem entry
    
    Args:
        readme_path: Path to the local README
        problem_slug: The problem slug from URL
        topic_folder: Target folder (e.g., 'leetcode/Easy')
        problem_data: Extracted problem data
    """
    validate_local_readme(readme_path)
    
    # Read current README content
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract difficulty
    difficulty = topic_folder.split('/')[-1]
    
    # Find the appropriate section
    section_marker = f"## {difficulty}"
    
    if section_marker not in content:
        print(f"ERROR: section {section_marker} not found in {readme_path}")
        print("Local README.md wasn't updated.")
        return
    
    # Build the new entry
    title_with_num = f"{problem_data['title_num']}. {problem_data['title']}"
    tags_str = f" [{', '.join(problem_data['tags'])}]" if problem_data['tags'] else ""
    
    folder_name = f"{problem_data['title_num']}_{problem_slug.replace('-', '_')}"
    solution_path = f"{topic_folder}/{folder_name}"
    
    new_entry = f"* [{title_with_num}]({problem_data['problem_link']}){tags_str} - [Solution]({solution_path})\n"
    
    # Find position to insert
    section_pos = content.find(section_marker)
    next_section_pos = content.find("##", section_pos + len(section_marker))
    
    if next_section_pos == -1:
        next_section_pos = content.find("# ", section_pos + len(section_marker))
    
    if next_section_pos == -1:
        insert_pos = len(content)
    else:
        insert_pos = next_section_pos
    
    # Find last entry in current section
    section_content = content[section_pos:insert_pos]
    last_entry_pos = section_content.rfind("* [")
    
    if last_entry_pos == -1:
        # No entries yet
        new_content = (content[:section_pos + len(section_marker)] + 
                      "\n\n" + new_entry + 
                      content[section_pos + len(section_marker):])
    else:
        # Add after last entry
        absolute_pos = section_pos + last_entry_pos
        line_end = content.find("\n", absolute_pos)
        if line_end == -1:
            line_end = len(content)
        
        new_content = content[:line_end + 1] + new_entry + content[line_end + 1:]
    
    # Write updated content
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"OK: updated local README.md with new problem entry")
    return new_entry

