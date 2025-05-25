# 3. CSV File Handling
#example:-
import csv
data = [["Name", "Age"], ["Alice", 30], ["Bob", 25]]
with open("example.csv", "w", newline="") as f:  # Open a CSV file in write mode
    writer = csv.writer(f)  # Create a CSV writer object
    writer.writerows(data)  # Write data to the CSV file
#
# 4. JSON File Handling
#example:-
import json
data = {"name": "Alice", "age": 30}
with open("example.json", "w") as f:  # Open a JSON file in write mode
    json.dump(data, f)  # Write JSON data to the file

#
# 5. XML File Handling
#example:-
import xml.etree.ElementTree as ET
data = ET.Element("data")
item1 = ET.SubElement(data, "item")
item1.text = "Item 1"
item2 = ET.SubElement(data, "item")
item2.text = "Item 2"
tree = ET.ElementTree(data)
with open("example.xml", "wb") as f:  # Open an XML file in binary write mode
    tree.write(f)  # Write XML data to the file
#

# 6. Pickle File Handling
#example:-
import pickle
data = {"name": "Alice", "age": 30}
with open("example.pkl", "wb") as f:  # Open a pickle file in binary write mode
    pickle.dump(data, f)  # Write data to the pickle file

# 7. SQLite Database Handling
#example:-
import sqlite3
conn = sqlite3.connect("example.db")  # Connect to a SQLite database
cursor = conn.cursor()  # Create a cursor object
cursor.execute("CREATE TABLE IF NOT EXISTS users (name TEXT, age INTEGER)")  # Create a table
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 30))  # Insert data into the table
conn.commit()  # Commit the changes
cursor.execute("SELECT * FROM users")  # Select data from the table
rows = cursor.fetchall()  # Fetch all rows
for row in rows:
    print(row)  # Print each row
conn.close()  # Close the database connection
#
# 8. Excel File Handling
#example:-
import pandas as pd
data = {"Name": ["Alice", "Bob"], "Age": [30, 25]}
df = pd.DataFrame(data)  # Create a DataFrame
df.to_excel("example.xlsx", index=False)  # Write DataFrame to an Excel file
#
# 9. YAML File Handling
#example:-
import yaml
data = {"name": "Alice", "age": 30}
with open("example.yaml", "w") as f:  # Open a YAML file in write mode
    yaml.dump(data, f)  # Write YAML data to the file

# 10. Log File Handling
#example:-
import logging
logging.basicConfig(filename="example.log", level=logging.DEBUG)  # Configure logging
logging.debug("This is a debug message")  # Write a debug message to the log file
logging.info("This is an info message")  # Write an info message to the log file
logging.warning("This is a warning message")  # Write a warning message to the log file
logging.error("This is an error message")  # Write an error message to the log file
logging.critical("This is a critical message")  # Write a critical message to the log file
#
# 11. HTML File Handling
#example:-
data = "<html><body><h1>Hello, World!</h1></body></html>"  # HTML data
with open("example.html", "w") as f:  # Open an HTML file in write mode
    f.write(data)  # Write HTML data to the file
#
# 12. PDF File Handling
#example:-
from fpdf import FPDF
pdf = FPDF()  # Create a PDF object
pdf.add_page()  # Add a page to the PDF
pdf.set_font("Arial", size=12)  # Set the font
pdf.cell(200, 10, txt="Hello, World!", ln=True, align="C")  # Add a cell to the PDF
pdf.output("example.pdf")  # Save the PDF to a file
#
# 13. ZIP File Handling
#example:-
import zipfile
with zipfile.ZipFile("example.zip", "w") as zipf:  # Open a ZIP file in write mode
    zipf.write("example.txt")  # Add a file to the ZIP archive
    zipf.write("example.csv")  # Add another file to the ZIP archive
#
# 14. Tar File Handling
#example:-
import tarfile
with tarfile.open("example.tar", "w") as tarf:  # Open a TAR file in write mode
    tarf.add("example.txt")  # Add a file to the TAR archive
    tarf.add("example.csv")  # Add another file to the TAR archive
#
# 15. Gzip File Handling
#example:-
import gzip
with gzip.open("example.gz", "wb") as gzf:  # Open a GZIP file in binary write mode
    gzf.write(b"Hello, World!")  # Write binary data to the GZIP file
#
# 16. Bzip2 File Handling
#example:-
import bz2
with bz2.open("example.bz2", "wb") as bzf:  # Open a BZIP2 file in binary write mode
    bzf.write(b"Hello, World!")  # Write binary data to the BZIP2 file
#
# 17. XML Parsing
#example:-
import xml.etree.ElementTree as ET
tree = ET.parse("example.xml")  # Parse an XML file
root = tree.getroot()  # Get the root element
for child in root:
    print(child.tag, child.text)  # Print the tag and text of each child element
# 18. JSON Parsing
#example:-
import json
with open("example.json", "r") as f:  # Open a JSON file in read mode
    data = json.load(f)  # Load JSON data from the file
    print(data)  # Print the loaded data
# 19. CSV Parsing
#example:-
import csv
with open("example.csv", "r") as f:  # Open a CSV file in read mode
    reader = csv.reader(f)  # Create a CSV reader object
    for row in reader:
        print(row)  # Print each row of the CSV file
# 20. Excel Parsing
#example:-
import pandas as pd
df = pd.read_excel("example.xlsx")  # Read data from an Excel file
print(df)  # Print the DataFrame
# 21. YAML Parsing
#example:-
import yaml
with open("example.yaml", "r") as f:  # Open a YAML file in read mode
    data = yaml.safe_load(f)  # Load YAML data from the file
    print(data)  # Print the loaded data
# 22. SQLite Database Querying
#example:-
import sqlite3
conn = sqlite3.connect("example.db")  # Connect to a SQLite database
cursor = conn.cursor()  # Create a cursor object
cursor.execute("SELECT * FROM users")  # Select data from the table
rows = cursor.fetchall()  # Fetch all rows
for row in rows:
    print(row)  # Print each row
conn.close()  # Close the database connection
# 23. PDF Parsing
#example:-
from PyPDF2 import PdfReader
reader = PdfReader("example.pdf")  # Open a PDF file
for page in reader.pages:
    print(page.extract_text())  # Print the text of each page
# 24. HTML Parsing
#example:-
from bs4 import BeautifulSoup
with open("example.html", "r") as f:  # Open an HTML file in read mode
    soup = BeautifulSoup(f, "html.parser")  # Parse the HTML file
    print(soup.prettify())  # Print the parsed HTML
# 25. Log File Parsing
#example:-
import re
with open("example.log", "r") as f:  # Open a log file in read mode
    for line in f:
        if re.search(r"ERROR", line):  # Search for lines containing "ERROR"
            print(line.strip())  # Print the matching lines
# 26. ZIP File Extraction
#example:-
import zipfile
with zipfile.ZipFile("example.zip", "r") as zipf:  # Open a ZIP file in read mode
    zipf.extractall("extracted_files")  # Extract all files to a directory
# 27. Tar File Extraction
#example:-
import tarfile
with tarfile.open("example.tar", "r") as tarf:  # Open a TAR file in read mode
    tarf.extractall("extracted_files")  # Extract all files to a directory
# 28. Gzip File Extraction
#example:-
import gzip
with gzip.open("example.gz", "rb") as gzf:  # Open a GZIP file in binary read mode
    data = gzf.read()  # Read the data from the GZIP file
    print(data)  # Print the extracted data
# 29. Bzip2 File Extraction
#example:-
import bz2
with bz2.open("example.bz2", "rb") as bzf:  # Open a BZIP2 file in binary read mode
    data = bzf.read()  # Read the data from the BZIP2 file
    print(data)  # Print the extracted data
# 30. File Compression
#example:-
import zipfile
with zipfile.ZipFile("example_compressed.zip", "w") as zipf:  # Open a ZIP file in write mode
    zipf.write("example.txt")  # Add a file to the ZIP archive
    zipf.write("example.csv")  # Add another file to the ZIP archive
# 31. File Decompression
#example:-
import zipfile
with zipfile.ZipFile("example_compressed.zip", "r") as zipf:  # Open a ZIP file in read mode
    zipf.extractall("decompressed_files")  # Extract all files to a directory
# 32. File Renaming
#example:-
import os
os.rename("example.txt", "example_renamed.txt")  # Rename a file



