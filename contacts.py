contact = {
    "number": 4,
    "student": [
        {
            "name": "John Doe",
            "email": "john.doe@example.com",
        },
        {
            "name": "Jane Smith",
            "email": "jane.smith@example.com",
        },
        {
            "name": "Alice Johnson",
            "email": "alice.johnson@example.com",
        },
        {
            "name": "Bob Brown",
            "email": "bob.brown@example.com",
        },
    ],
}

print(f"Total Students: {contact['number']}")
for student in contact["student"]:
    print(f"Name: {student['name']}, Email: {student['email']}")