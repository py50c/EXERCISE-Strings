text = "Python is an amazing programming language."

# Step 1: Convert to uppercase
text = text.upper()
print("Uppercase:", text)

# Step 2: Replace 'amazing' with 'powerful'
text = text.replace("AMAZING", "POWERFUL")
print("Replaced text:", text)

# Step 3: Find the position of 'PROGRAMMING'
position = text.find("PROGRAMMING")
print("Position of 'PROGRAMMING':", position)

# Step 4: Slice from index 10 to 19
substring = text[10:19]
print("Sliced substring:", substring)

# Step 5: Format the final result
final_result = f"Result after processing: {text}"
print(final_result)
