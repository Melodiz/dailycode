import requests
import json
import sys
import re


def get_problem_data_from_leetcode(problem_slug):
    """
    Fetch problem data from LeetCode using their GraphQL API
    
    Args:
        problem_slug: The problem slug from URL (e.g., 'count-negative-numbers-in-a-sorted-matrix')
    
    Returns:
        dict: Problem data including description, test cases, tags, and code template
    """
    
    # LeetCode GraphQL endpoint
    url = "https://leetcode.com/graphql"
    
    # GraphQL query to fetch problem details
    query = """
    query getQuestionDetail($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
            questionId
            questionFrontendId
            title
            titleSlug
            content
            difficulty
            likes
            dislikes
            exampleTestcases
            topicTags {
                name
                slug
            }
            codeSnippets {
                lang
                langSlug
                code
            }
            sampleTestCase
            hints
        }
    }
    """
    
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    variables = {
        "titleSlug": problem_slug
    }
    
    payload = {
        "query": query,
        "variables": variables
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        
        data = response.json()
        
        if 'errors' in data:
            print(f"ERROR: GraphQL returned errors: {data['errors']}")
            return None
            
        if not data.get('data') or not data['data'].get('question'):
            print(f"ERROR: Problem '{problem_slug}' not found")
            return None
            
        return data['data']['question']
        
    except requests.exceptions.RequestException as e:
        print(f"ERROR: Failed to fetch problem data: {e}")
        return None


def clean_html_content(html_content):
    """
    Clean HTML content and convert to markdown
    
    Args:
        html_content: Raw HTML content from LeetCode
    
    Returns:
        str: Cleaned markdown content
    """
    if not html_content:
        return ""
    
    # Replace HTML tags with markdown equivalents
    # Remove HTML tags but keep content
    content = html_content
    
    # Replace <p> with newlines
    content = re.sub(r'<p>', '', content)
    content = re.sub(r'</p>', '\n\n', content)
    
    # Replace <strong> with **
    content = re.sub(r'<strong>', '**', content)
    content = re.sub(r'</strong>', '**', content)
    
    # Replace <em> with *
    content = re.sub(r'<em>', '*', content)
    content = re.sub(r'</em>', '*', content)
    
    # Replace <code> with `
    content = re.sub(r'<code>', '`', content)
    content = re.sub(r'</code>', '`', content)
    
    # Replace <pre> blocks with code blocks
    content = re.sub(r'<pre>', '\n```\n', content)
    content = re.sub(r'</pre>', '\n```\n', content)
    
    # Replace <ul> and <li>
    content = re.sub(r'<ul>', '\n', content)
    content = re.sub(r'</ul>', '\n', content)
    content = re.sub(r'<li>', '- ', content)
    content = re.sub(r'</li>', '\n', content)
    
    # Replace <ol> and <li> with numbered lists
    content = re.sub(r'<ol>', '\n', content)
    content = re.sub(r'</ol>', '\n', content)
    
    # Remove other HTML tags
    content = re.sub(r'<[^>]+>', '', content)
    
    # Decode HTML entities
    content = content.replace('&lt;', '<')
    content = content.replace('&gt;', '>')
    content = content.replace('&amp;', '&')
    content = content.replace('&quot;', '"')
    content = content.replace('&#39;', "'")
    content = content.replace('&nbsp;', ' ')
    
    # Clean up excessive newlines
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    # Fix common formatting issues
    content = re.sub(r'\*\*\s*Example\s+(\d+):\s*\*\*', r'**Example \1:**', content)
    content = re.sub(r'\*\*\s*Input:\s*\*\*', r'**Input:**', content)
    content = re.sub(r'\*\*\s*Output:\s*\*\*', r'**Output:**', content)
    content = re.sub(r'\*\*\s*Explanation:\s*\*\*', r'**Explanation:**', content)
    
    return content.strip()


def parse_test_cases(example_testcases, html_content, python_code):
    """
    Parse test cases from LeetCode format
    
    Args:
        example_testcases: Example test cases string from GraphQL
        html_content: Raw HTML content to extract expected outputs
        python_code: Python code template to determine number of arguments
    
    Returns:
        list: List of test case dictionaries
    """
    test_cases = []
    
    if not example_testcases:
        return test_cases
    
    # Determine number of arguments from python_code
    arg_count = 1
    if python_code:
        match = re.search(r'def \w+\(self,?\s*([^)]*)\)', python_code)
        if match:
            args_str = match.group(1).strip()
            if args_str:
                # Count arguments by counting commas at top level
                arg_count = 1
                depth = 0
                for char in args_str:
                    if char in '([{': depth += 1
                    elif char in ')]}': depth -= 1
                    elif char == ',' and depth == 0:
                        arg_count += 1
    
    # Split test cases by newline (LeetCode format)
    lines = [line.strip() for line in example_testcases.strip().split('\n') if line.strip()]
    
    # Group lines by arg_count
    input_groups = []
    for i in range(0, len(lines), arg_count):
        group = lines[i:i+arg_count]
        if len(group) == arg_count:
            # Clean up each arg in group (convert JSON-style to Python-style)
            cleaned_group = []
            for arg in group:
                # Replace boolean and null values
                arg = arg.replace('true', 'True').replace('false', 'False').replace('null', 'None')
                cleaned_group.append(arg)
            
            if arg_count > 1:
                input_groups.append(f"({', '.join(cleaned_group)})")
            else:
                input_groups.append(cleaned_group[0])
    
    # Try to extract outputs from HTML
    outputs = re.findall(r'<strong>Output:</strong>\s*(.*?)\s*(?:<\/pre>|<strong>Explanation:</strong>|<p>|<strong>|\Z)', html_content, re.DOTALL)
    clean_outputs = []
    for out in outputs:
        # Remove HTML tags and clean up
        out = re.sub(r'<[^>]+>', '', out).strip()
        out = out.replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&').replace('&quot;', '"').replace('&#39;', "'").replace('&nbsp;', ' ')
        # LeetCode sometimes uses "null", "true", "false" in HTML but they should be Python-style
        if out.lower() == 'true': out = 'True'
        elif out.lower() == 'false': out = 'False'
        elif out.lower() == 'null': out = 'None'
        clean_outputs.append(out)
    
    for i, input_val in enumerate(input_groups):
        output_val = clean_outputs[i] if i < len(clean_outputs) else 'See problem description'
        test_cases.append({
            'input': input_val,
            'output': output_val
        })
    
    return test_cases


def extract_problem_data(problem_data):
    """
    Extract and format problem data into our standardized format
    
    Args:
        problem_data: Raw problem data from LeetCode API
    
    Returns:
        dict: Formatted problem data
    """
    if not problem_data:
        print("ERROR: Empty problem data provided")
        sys.exit(1)
    
    # Extract basic information
    title = problem_data.get('title', 'Unknown Title')
    problem_id = problem_data.get('questionFrontendId', '0')
    difficulty = problem_data.get('difficulty', 'Unknown')
    title_slug = problem_data.get('titleSlug', '')
    problem_link = f"https://leetcode.com/problems/{title_slug}/"
    
    # Extract and clean description
    raw_content = problem_data.get('content', '')
    description = clean_html_content(raw_content)
    
    # Extract tags
    topic_tags = problem_data.get('topicTags', [])
    tags = [tag['name'] for tag in topic_tags]
    
    # Extract Python code template
    code_snippets = problem_data.get('codeSnippets', [])
    python_code = ""
    for snippet in code_snippets:
        if snippet['langSlug'] == 'python3':
            python_code = snippet['code']
            break
    
    # Extract test cases
    example_testcases = problem_data.get('exampleTestcases', '')
    sample_test_case = problem_data.get('sampleTestCase', '')
    test_cases = parse_test_cases(example_testcases, raw_content, python_code)
    
    # Extract hints
    hints = problem_data.get('hints', [])
    
    # Build complete description text
    description_text = f"# [{problem_id}. {title}]({problem_link})\n\n"
    description_text += f"**Difficulty:** {difficulty}\n\n"
    
    if tags:
        description_text += f"**Tags:** {', '.join(tags)}\n\n"
    
    description_text += "## Description\n\n"
    description_text += description + "\n\n"
    
    if test_cases:
        description_text += "## Example Test Cases\n\n"
        for i, test_case in enumerate(test_cases):
            description_text += f"### Example {i+1}\n\n"
            description_text += f"**Input:**\n```\n{test_case['input']}\n```\n\n"
            if test_case['output'] != 'See problem description':
                description_text += f"**Output:**\n```\n{test_case['output']}\n```\n\n"
    
    if hints:
        description_text += "## Hints\n\n"
        for i, hint in enumerate(hints):
            description_text += f"{i+1}. {hint}\n"
        description_text += "\n"
    
    return {
        'title': title,
        'title_num': problem_id,
        'difficulty': difficulty,
        'legend_data': description,
        'case_data': test_cases,
        'problem_link': problem_link,
        'tags': tags,
        'description_text': description_text,
        'python_code': python_code,
        'hints': hints
    }


def validate_html_content(problem_data):
    """
    Validate that problem data was successfully fetched
    
    Args:
        problem_data: Problem data to validate
    """
    if not problem_data:
        print('ERROR: Failed to fetch problem data from LeetCode')
        sys.exit(1)
    
    print(f"OK: fetched problem data from LeetCode")

