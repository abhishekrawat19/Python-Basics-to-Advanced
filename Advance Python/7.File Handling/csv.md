# Working with CSV in Python (Advanced Guide)

## Why Use CSV Over TXT?
CSV (Comma-Separated Values) is preferred over TXT for structured data because:
- **Standardized Format**: CSV is widely accepted for tabular data, making it easy to share and integrate.
- **Efficient Parsing**: CSV files can be processed efficiently using built-in Python libraries, unlike raw TXT files that require manual parsing.
- **Compatibility**: Used by Excel, databases, and analytics tools for easy data exchange.
- **Structured Data Storage**: Unlike TXT, CSV maintains a structured format with rows and columns.
- **Supports Large Data Processing**: CSV files can handle millions of rows efficiently compared to plain text files.

---

## How to Work with CSV Files in Python
Python’s `csv` module provides easy methods to read, write, and process CSV files.

### 1. Reading a CSV File
```python
import csv

with open("data.csv", "r", encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # Each row is a list
```
✅ Reads each line and stores it as a list.

### 2. Writing to a CSV File
```python
import csv

data = [["Name", "Age"], ["Alice", 25], ["Bob", 30]]

with open("output.csv", "w", newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)
```
✅ Writes data efficiently without manual formatting.

---

## Handling CSV with Dictionaries
Instead of lists, `csv.DictReader` and `csv.DictWriter` allow handling CSV as dictionaries.

### 3. Reading CSV as Dictionary
```python
import csv

with open("data.csv", "r", encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["Name"], row["Age"])  # Access by column name
```
✅ Easier access using column headers.

### 4. Writing CSV as Dictionary
```python
import csv

data = [{"Name": "Alice", "Age": 25}, {"Name": "Bob", "Age": 30}]

with open("output.csv", "w", newline='', encoding='utf-8') as file:
    fieldnames = ["Name", "Age"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)
```
✅ Automatically structures data with headers.

---

## Advanced Topics in CSV Handling
### 5. Handling Large CSV Files
For large files, process data in chunks using `pandas` for efficiency.

```python
import pandas as pd

for chunk in pd.read_csv("large_data.csv", chunksize=1000):
    print(chunk.head())
```
✅ Prevents memory overload by reading in batches.

### 6. Streaming CSV Data
To handle massive CSV files efficiently:
```python
import csv

def read_large_csv(file_path):
    with open(file_path, "r", encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            yield row  # Using generator to read row by row

for row in read_large_csv("large_data.csv"):
    print(row)
```
✅ Uses a generator to process data row by row without high memory usage.

---

## Working with Different Delimiters
CSV files may use different delimiters (e.g., `;` instead of `,`). Handle them using `delimiter` parameter.

```python
with open("data.csv", "r", encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=';')
    for row in reader:
        print(row)
```
✅ Ensures correct parsing of non-standard CSV formats.

### 7. Handling Missing Values
CSV files often contain missing values. Use `pandas` to fill or drop missing values:
```python
import pandas as pd

df = pd.read_csv("data.csv")
df.fillna("Unknown", inplace=True)  # Replace NaN values
df.dropna(inplace=True)  # Remove rows with missing values
print(df.head())
```
✅ Keeps data clean and structured.

### 8. Appending to an Existing CSV File
```python
import csv

data = [["Charlie", 35]]

with open("output.csv", "a", newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)
```
✅ Ensures new data is added without overwriting existing content.

---

## Real-Time Project Applications
| Feature | Real-World Use Case |
|---------|----------------------|
| Streaming CSV Data | Processing real-time logs, IoT data, stock market feeds |
| Handling Large Files | Analyzing financial or healthcare datasets efficiently |
| Custom Delimiters | Parsing CSV from legacy systems with different formats |
| Handling Missing Values | Cleaning and preparing data for machine learning |
| Appending Data | Updating logs or transaction records incrementally |

CSV files offer a structured, efficient, and widely accepted way to handle tabular data, making them the preferred choice over TXT files in real-time data processing, analytics, and automation.

