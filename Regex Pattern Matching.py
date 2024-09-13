import re

# Given string
text = "Contact us at support@example.com or call 123-456-7890. Alternatively, email admin@domain.org or phone 987-654-3210."

# Step 1: Find all email addresses
emails = re.findall(r"\w+@\w+\.\w+", text)
print("Emails found:", emails)
# Output: ['support@example.com', 'admin@domain.org']

# Step 2: Find all phone numbers
phone_numbers = re.findall(r"\d{3}-\d{3}-\d{4}", text)
print("Phone numbers found:", phone_numbers)
# Output: ['123-456-7890', '987-654-3210']

# Step 3: Replace all phone numbers with '[REDACTED]'
redacted_text = re.sub(r"\d{3}-\d{3}-\d{4}", "[REDACTED]", text)
print("Text after redacting phone numbers:", redacted_text)
# Output: Contact us at support@example.com or call [REDACTED]. Alternatively, email admin@domain.org or phone [REDACTED].
