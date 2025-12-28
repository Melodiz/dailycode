import os
import sys


def check_topic_id(topic_folder):
    """
    Validate that the topic folder exists
    
    Args:
        topic_folder: Path to the topic folder (e.g., 'leetcode/Easy')
    """
    if not os.path.exists(topic_folder):
        print(f"ERROR: Topic folder '{topic_folder}' does not exist")
        sys.exit(1)


def validate_problem_data(problem_data):
    """
    Validate that problem data was successfully fetched
    
    Args:
        problem_data: Problem data to validate
    """
    if not problem_data:
        print('ERROR: Failed to fetch problem data from LeetCode')
        sys.exit(1)


def validate_problem_folder(problem_folder):
    """
    Validate that the problem folder doesn't already exist
    
    Args:
        problem_folder: Path to the problem folder
    """
    if os.path.exists(problem_folder):
        print(f"ERROR: Problem folder '{problem_folder}' already exists")
        sys.exit(1)


def validate_global_readme(readme_path):
    """
    Validate that the global README exists
    
    Args:
        readme_path: Path to the global README
    """
    if not os.path.exists(readme_path):
        print(f"ERROR: Global README.md file does not exist at {readme_path}")
        sys.exit(1)


def validate_local_readme(readme_path):
    """
    Validate that the local README exists
    
    Args:
        readme_path: Path to the local README
    """
    if not os.path.exists(readme_path):
        print(f"ERROR: Local README.md file does not exist at {readme_path}")
        sys.exit(1)


def validate_difficulty(difficulty):
    """
    Validate that the difficulty is one of the expected values
    
    Args:
        difficulty: Difficulty level (Easy, Medium, Hard)
    """
    valid_difficulties = ['Easy', 'Medium', 'Hard']
    if difficulty not in valid_difficulties:
        print(f"ERROR: Invalid difficulty '{difficulty}'. Must be one of: {', '.join(valid_difficulties)}")
        sys.exit(1)

