#!/usr/bin/env python3
"""
LeetCode Problem Addition Tool

Usage:
    python add_leetcode.py <problem-slug>

Example:
    python add_leetcode.py count-negative-numbers-in-a-sorted-matrix

The script will:
1. Fetch problem data from LeetCode
2. Determine the difficulty level
3. Create a folder with README and solution template
4. Update the main and local READMEs
"""

import argparse
import os
import sys

from leetcode_check_utils import check_topic_id, validate_problem_data, validate_difficulty
from leetcode_fetch_parse import get_problem_data_from_leetcode, extract_problem_data, validate_html_content
from leetcode_utils import create_solution_files, update_global_readme, update_local_readme


def main():
    # Parse command-line arguments
    arg_parser = argparse.ArgumentParser(
        description='Add a new LeetCode problem to the repository',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python add_leetcode.py count-negative-numbers-in-a-sorted-matrix
  python add_leetcode.py two-sum
  python add_leetcode.py median-of-two-sorted-arrays
        """
    )
    arg_parser.add_argument('problem_slug', help='Problem slug from LeetCode URL (e.g., count-negative-numbers-in-a-sorted-matrix)')
    
    args = arg_parser.parse_args()
    
    # Fetch problem data from LeetCode
    print(f"Fetching problem data for: {args.problem_slug}")
    raw_problem_data = get_problem_data_from_leetcode(args.problem_slug)
    validate_html_content(raw_problem_data)
    
    # Extract and format problem data
    print("Extracting and formatting problem data...")
    problem_data = extract_problem_data(raw_problem_data)
    
    # Determine difficulty and construct topic folder
    difficulty = problem_data['difficulty']
    validate_difficulty(difficulty)
    
    # Get the leetcode root directory (parent of utils)
    leetcode_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    topic_folder = os.path.join(leetcode_root, difficulty)
    
    # Validate that the topic folder exists
    check_topic_id(topic_folder)
    
    print(f"\nProblem Details:")
    print(f"  Title: {problem_data['title']}")
    print(f"  Number: {problem_data['title_num']}")
    print(f"  Difficulty: {difficulty}")
    print(f"  Tags: {', '.join(problem_data['tags']) if problem_data['tags'] else 'None'}")
    print(f"  URL: {problem_data['problem_link']}")
    
    # Create solution files
    print(f"\nCreating problem folder in: {topic_folder}")
    create_solution_files(args.problem_slug, topic_folder, problem_data)
    
    # Update main README.md
    main_readme_path = os.path.join(leetcode_root, 'README.md')
    update_global_readme(main_readme_path, args.problem_slug, topic_folder, problem_data)
    
    # Update local readme.md
    local_readme_path = os.path.join(leetcode_root, difficulty, 'readme.md')
    update_local_readme(local_readme_path, args.problem_slug, topic_folder, problem_data)
    
    # Generate git command shortcut
    folder_name = f"{problem_data['title_num']}_{args.problem_slug.replace('-', '_')}"
    clean_title = f"{problem_data['title_num']}. {problem_data['title']}"
    
    print("\n" + "="*60)
    print("SUCCESS! Problem added successfully.")
    print("="*60)
    print(f"\nFolder created: {difficulty}/{folder_name}")
    print(f"\nGit command shortcut:")
    print(f'git add . && git commit -m "LeetCode: {clean_title}" && git push origin main')
    print()
    
    return 0


if __name__ == "__main__":
    sys.exit(main())

