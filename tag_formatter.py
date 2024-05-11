import pyperclip
import re

def extract_tag_names(text):
    # Split the text on any combination of carriage return and newline characters
    lines = re.split(r'\r?\n', text)
    extracted_tags = []
    
    for line in lines:
        # Adjust the regular expression to allow for multiple spaces between the tag name and the number
        match = re.search(r'\?\s+(.+?)\s+\d+$', line)
        if match:
            extracted_tags.append(match.group(1).strip())  # Strip any trailing spaces from the tag name
    
    return ', '.join(extracted_tags)

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def main():
    text = pyperclip.paste()  # Read text from clipboard
    extracted_tags = extract_tag_names(text)  # Extract tag names
    cleaned_tags = clean_text(extracted_tags)  # Clean the extracted tag names
    pyperclip.copy(cleaned_tags)  # Update the clipboard with cleaned tag names
    print("Clipboard updated with cleaned tag names:", cleaned_tags)

if __name__ == "__main__":
    main()

