import sys
import re

# Get the input argument
brazilian_input = sys.argv[1] if len(sys.argv) > 1 else None

# Set the BREZILIAN value based on the input
brazilian_value = 'True' if brazilian_input == 'true' else 'False'

# Open the file in read mode and read the lines
with open('utils/constants.py', 'r') as file:
    lines = file.readlines()

# Open the file in write mode
with open('utils/constants.py', 'w') as file:
    for line in lines:
        # Replace DEBUG = True with DEBUG = False
        if 'DEBUG = True' in line:
            line = line.replace('DEBUG = True', 'DEBUG = False')
        # Replace the BREZILIAN value
        if 'BREZILIAN' in line:
            line = re.sub(r'BREZILIAN = .*', f'BREZILIAN = {brazilian_value}', line)
        # Write the line back to the file
        file.write(line)
