import csv
import sys
from faker import Faker

# Initialize Faker with Ukrainian locale
faker = Faker('uk_UA')

# Get the number of records to generate and output file path from the command line arguments
if len(sys.argv) != 3:
    print("Usage: python generate_students.py <number_of_records> <output_file_path>")
    sys.exit(1)

number_of_records = int(sys.argv[1])
output_file_path = sys.argv[2]

# Open a CSV file for writing
with open(output_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write header
    writer.writerow(['internalId', 'email', 'firstName', 'lastName', 'cityOfBirth', 'grade'])

    # Generate data and write to CSV
    for i in range(1, number_of_records + 1):
        id = i
        email = faker.safe_email()
        name = faker.first_name()
        surname = faker.last_name()
        city_of_birth = faker.city_name()
        grade = faker.random_int(min=1, max=12)

        # Write row to CSV
        writer.writerow([id, email, name, surname, city_of_birth, grade])

print(f'{number_of_records} records generated and written to {output_file_path}')
