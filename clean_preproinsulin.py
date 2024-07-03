import re

# Read the content of the file
with open('preproinsulin-seq.txt', 'r') as file:
    content = file.read()

# Use regex to clean the content
cleaned_content = re.sub(r'[^a-zA-Z]', '', content)

# Write the cleaned content to a new file
with open('cleaned_preproinsulin-seq.txt', 'w') as file:
    file.write(cleaned_content)

# Confirm the file has 110 characters
if len(cleaned_content) == 110:
    print("The cleaned sequence has 110 characters.")
else:
    print(f"The cleaned sequence has {len(cleaned_content)} characters.")

print(cleaned_content)