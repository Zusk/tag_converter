import pyperclip
import re

def extract_tag_names(text):
    # Split the text into lines
    lines = text.split('\n')
    # Prepare to collect results
    extracted_tags = []

    for line in lines:
        # Use regular expression to match the pattern: starts with '?', then text, then ends with a number
        match = re.search(r'\?\s+(\w+)\s+\d+', line)
        if match:
            # Append the tag name found
            extracted_tags.append(match.group(1))
    
    # Join all extracted tag names into a single string separated by commas
    return ', '.join(extracted_tags)

def clean_text(text):
    # Replace multiple spaces with a single space
    text = re.sub(r'\s+', ' ', text)
    # Clean any other formatting issues if necessary
    return text.strip()

def main():
    text = pyperclip.paste()  # Read text from clipboard
    extracted_tags = extract_tag_names(text)  # Extract tag names
    cleaned_tags = clean_text(extracted_tags)  # Clean the extracted tag names
    pyperclip.copy(cleaned_tags)  # Update the clipboard with cleaned tag names
    print("Clipboard updated with cleaned tag names:", cleaned_tags)

if __name__ == "__main__":
    main()

