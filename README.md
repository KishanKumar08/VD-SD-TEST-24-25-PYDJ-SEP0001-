

```markdown
# Technical Assessment: VD-SD-TEST-24-25-PYDJ-SEP0001

## Purpose
This repository contains solutions to the technical assessment for the Software Engineer position at Vakildesk. Each solution demonstrates proficiency in Python programming and the Django framework, showcasing problem-solving skills and the ability to implement real-world scenarios.

```
## Folder Structure
VD-SD-TEST-24-25-PYDJ-SEP0001/
<br>
<br>
├── Q1_Web_Scraping/
│   └── main.py
<br>
<br>
├── Q2_CSV_Data_Cleaning/
│   └── main.py
<br>
<br>
├── Q3_Django_Top_Customers/
│   └── main.py
<br>
<br>
├── Q4_Rate_Limiter/
│   └── main.py
<br>
<br>
├── Q5_Data_Aggregation/
│   └── main.py
<br>
<br>
├── Q6_Find_Duplicate_In_Array/
│   └── main.py
<br>
<br>
├── README.md
└── requirements.txt

## Questions and Solutions

### Q1: Web Scraping using BeautifulSoup
- **Description**: This script scrapes the titles and URLs of the latest articles from a news website using the `BeautifulSoup` and `requests` libraries.
- **Folder**: `Q1_Web_Scraping/`
- **Dependencies**: `requests`, `beautifulsoup4`
- **Usage**:
  1. Run the script:
     ```bash
     python main.py
     ```
  2. **Output**: The script will print a list of article titles and their corresponding URLs. 

### Q2: CSV Data Cleaning
- **Description**: This script reads a CSV file, removes duplicate entries based on `user_id`, filters out rows with invalid email formats, and writes the cleaned data to a new CSV file.
- **Folder**: `Q2_CSV_Data_Cleaning/`
- **Usage**:
  1. Ensure you have an `input.csv` file in the same directory with the required fields (`user_id`, `name`, `email`).
  2. Run the script:
     ```bash
     python main.py
     ```
  3. **Output**: The cleaned data will be saved to `output.csv`, free of duplicates and invalid emails.

### Q3: Django Top Customers Query
- **Description**: This Django-based solution retrieves the top 5 customers who have spent the most in the last 6 months.
- **Folder**: `Q3_Django_Top_Customers/`
- **Setup**:
  1. Ensure you have Django installed.
  2. Create a Django project and add this code to an app.
  3. Define an `Order` model with the required fields (`customer`, `order_date`, `status`, and `total_amount`).
  4. Run migrations:
     ```bash
     python manage.py migrate
     ```
- **Usage**:
  1. Create a view to call `top_customers_view`.
  2. Access the corresponding URL to see the output, which lists the top customers by total spending.

### Q4: Rate Limiter
- **Description**: This script implements a rate limiter that allows a maximum of 5 requests per user per minute.
- **Folder**: `Q4_Rate_Limiter/`
- **Usage**:
  1. Run the script:
     ```bash
     python main.py
     ```
  2. **Testing**: Test different user IDs to see whether requests are allowed based on the rate limiting rules. The output indicates whether a request is permitted.

### Q5: Data Aggregator Function
- **Description**: This function aggregates values from a list of dictionaries based on a specified key and applies a provided aggregator function.
- **Folder**: `Q5_Data_Aggregation/`
- **Usage**:
  1. Run the script:
     ```bash
     python main.py
     ```
  2. **Output**: The output will display aggregated values grouped by the specified key, demonstrating the effectiveness of the aggregation function.

### Q6: Find Duplicate in Array (O(1) Space)
- **Description**: This script finds a duplicate number in an array using O(1) extra space.
- **Folder**: `Q6_Find_Duplicate_In_Array/`
- **Usage**:
  1. Run the script:
     ```bash
     python main.py
     ```
  2. **Output**: The output will display the duplicate number found in the input array.

## Setup Instructions
1. **Clone the repository**:
   ```bash
   git clone https://github.com/KishanKumar08/VD-SD-TEST-24-25-PYDJ-SEP0001.git
   ```
2. **Navigate into the repository**:
   ```bash
   cd VD-SD-TEST-24-25-PYDJ-SEP0001
   ```
3. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **For Django-related questions**, ensure migrations are run using:
   ```bash
   python manage.py migrate
   ```

## Requirements
- Python 3.8+
- Django (for Q3)
- BeautifulSoup and requests (for Q1)

## Notes
- Ensure that you have the necessary environment set up for running Django applications if you're working on Q3.
- Each question's folder contains a `main.py` file where the solution resides. Make sure to read any inline comments for clarification on the code.
