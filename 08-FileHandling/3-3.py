import re

text = """
Alice was born on March 12, 1992. Her brother, John, was born on June 5, 1988.
They have a mutual friend named Mike, whose phone number is 555-123-4567.
In their hometown, which has a population of 1,234 or 1,235 people, a holiday festival
is held every year on December 25. Alice works in an office with 30 employees.
Her phone number is 555-765-4321.
"""

# 1. Dates in "Month DD, YYYY"
date_pattern = r"\b(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+\d{4}\b"

# 2. Phone numbers "XXX-XXX-XXXX"
phone_pattern = r"\b\d{3}-\d{3}-\d{4}\b"

# 3. Numbers with commas as thousand separators
comma_number_pattern = r"\b\d{1,3}(?:,\d{3})+\b"

# 4. Capitalized words
capitalized_word_pattern = r"\b[A-Z][a-z]+\b"

# 5. Whole numbers (digits only)
whole_number_pattern = r"\b\d+\b"

# Apply all patterns
dates = re.findall(date_pattern, text)
phones = re.findall(phone_pattern, text)
comma_numbers = re.findall(comma_number_pattern, text)
capitalized_words = re.findall(capitalized_word_pattern, text)
whole_numbers = re.findall(whole_number_pattern, text)

# Print results
print("Dates:", dates)
print("Phone numbers:", phones)
print("Comma-separated numbers:", comma_numbers)
print("Capitalized words:", capitalized_words)
print("Whole numbers:", whole_numbers)
