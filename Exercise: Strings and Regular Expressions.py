import re

# Given string
text = "John's email is john@example.com and his number is 555-123-4567. Jane's email is jane.doe@service.org and her number is 987-654-3210."

# Step 1: Convert the string to all lowercase
text = text.lower()
print("Lowercase text:", text)

# Step 2: Find and print all email addresses
emails = re.findall(r"\w+@\w+\.\w+", text)
print("Emails found:", emails)

# Step 3: Find and print all phone numbers in the format xxx-xxx-xxxx
phone_numbers = re.findall(r"\d{3}-\d{3}-\d{4}", text)
print("Phone numbers found:", phone_numbers)

# Step 4: Replace all phone numbers with 'XXXX-XXX-XXXX'
modified_text = re.sub(r"\d{3}-\d{3}-\d{4}", "XXXX-XXX-XXXX", text)
print("Text after replacing phone numbers:", modified_text)

# Step 5: Format the output as "Processed string: [your final string]"
final_output = f"Processed string: {modified_text}"
print(final_output)
