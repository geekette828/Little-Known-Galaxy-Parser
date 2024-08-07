import json
import os
import re

def log_debug(message):
    with open(debug_output_path, 'a', encoding='utf-8') as debug_file:
        debug_file.write(message + '\n')

# File paths
input_file_path = 'Input/Assets/TextAsset/English_Items.txt'
output_file_path = 'Output/item_descriptions.lua'
debug_output_path = '.hidden/debug_output/item_description_debug.txt'

# Ensure output directories exist
os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
os.makedirs(os.path.dirname(debug_output_path), exist_ok=True)

try:
    # Read the input file
    with open(input_file_path, 'r', encoding='utf-8') as file:
        data = file.read()

    # Regular expression to find item names and descriptions
    item_pattern = re.compile(r'"itemName":\s*"([^"]+)",\s*"itemDescription":\s*"([^"]+)"')

    # Find all matches
    items = item_pattern.findall(data)

    # Debug information
    debug_info = f"Found {len(items)} items\n"
    log_debug(debug_info)

    # Dictionary to hold items sorted by first letter
    sorted_items = {}

    # Process each item
    for name, description in items:
        first_letter = name[0].lower()
        if first_letter not in sorted_items:
            sorted_items[first_letter] = {}
        sorted_items[first_letter][name.lower()] = description

    # Sort items alphabetically by key
    for key in sorted_items:
        sorted_items[key] = dict(sorted(sorted_items[key].items()))

    # Prepare the Lua output format
    output_data = ["return {"]
    for key in sorted(sorted_items.keys()):
        output_data.append(f'    ["{key}"] = {{')
        for item_name, item_description in sorted_items[key].items():
            output_data.append(f'        ["{item_name}"] = "{item_description}",')
        output_data.append('    },')
    output_data.append("}")

    # Write to the output file
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write('\n'.join(output_data))

    # Print the required messages to the terminal
    print(f"Item descriptions have been successfully written to '{output_file_path}'")

except Exception as e:
    log_debug(f'An error occurred: {str(e)}')
    print(f"An error occurred. Check the debug output for details: '{debug_output_path}'")
