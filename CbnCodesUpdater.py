import re

# Read data from file 1
with open('/Users/olamigokeolabampe/Downloads/UPDATED CBN CODES.csv', 'r') as file1:
    file1_data = file1.read()

# Read data from file 2
with open('/Users/olamigokeolabampe/Downloads/financial_institutions.conf', 'r') as file2:
    file2_data = file2.read()

# Extract institution-code and code from file 1
code_mapping = {}
for line in file1_data.split('\n'):
    if line.strip():
        match = re.search(r'"(.*?)","(.*?)","(.*?)"', line)
        if match:
            institution_code = match.group(2)
            code = match.group(1)
            code_mapping[institution_code] = code

# Update code in file 2 based on code_mapping
updated_file2_data = file2_data
for institution_code, code in code_mapping.items():
    pattern = fr'{{code: "(.*?)", institution-code: "{institution_code}"'
    replacement = fr'{{code: "{code}", institution-code: "{institution_code}"'
    updated_file2_data = re.sub(pattern, replacement, updated_file2_data)

# Write updated data back to file 2
with open('/Users/olamigokeolabampe/Downloads/financial_institutions_updated_001.conf', 'w') as updated_file2:
    updated_file2.write(updated_file2_data)
