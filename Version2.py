# Version 2: Student Information Formatter with String Methods

first_name = input("Enter your first name: ").strip()
last_name = input("Enter your last name: ").strip()
section = input("Enter your section: ").strip()
favorite_subject = input("Enter your favorite subject: ").strip()

full_name = f"{first_name} {last_name}".strip().title()
name_code = full_name.upper()
formatted_section = section.upper()
formatted_subject = favorite_subject.title()
char_count = len(full_name)

print("\nFormatted Output:")
print(f"Name: {full_name}")
print(f"Name Code: {name_code}")
print(f"Section: {formatted_section}")
print(f"Favorite Subject: {formatted_subject}")
print(f"Character Count: {char_count}")
