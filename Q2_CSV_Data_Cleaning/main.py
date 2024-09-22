import csv
import re

class CSVProcessor:
    """Class for cleaning CSV data."""
    
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def is_valid_email(self, email):
        """Check if email is valid using regex."""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email)

    def clean_data(self):
        """Remove duplicates and invalid emails, then write to a new CSV."""
        users = {}
        with open(self.input_file, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                user_id = row['user_id']
                email = row['email']
                if user_id not in users and self.is_valid_email(email):
                    users[user_id] = row

        with open(self.output_file, 'w', newline='') as csvfile:
            fieldnames = ['user_id', 'name', 'email']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(users.values())

# Example usage:
if __name__ == "__main__":
    processor = CSVProcessor('input.csv', 'output.csv')
    processor.clean_data()
    print("Task completed.")
