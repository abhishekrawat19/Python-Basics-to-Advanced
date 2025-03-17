# Python Modules, Packages, Pip, and REST API

## 🔹 Python Modules
A **module** in Python is a file containing Python code, which can include functions, classes, and variables. It allows for better code organization and reusability.

### ✅ **Types of Modules**
1. **Built-in Modules** → Pre-installed in Python (e.g., `math`, `os`, `sys`, `datetime`)
2. **User-defined Modules** → Custom modules created by users
3. **Third-party Modules** → Installed using `pip` (e.g., `requests`, `numpy`)

### ✅ **Commonly Used Modules in Real-World Projects**

#### 🔹 Web Development
- `flask` / `django` → Web frameworks for backend development
- `requests` → Handling HTTP requests
- `beautifulsoup4` / `scrapy` → Web scraping

#### 🔹 Data Science & Machine Learning
- `numpy` → Numerical computations
- `pandas` → Data manipulation
- `matplotlib` / `seaborn` → Data visualization
- `scikit-learn` → Machine learning
- `tensorflow` / `pytorch` → Deep learning

#### 🔹 Automation & Scripting
- `os` → Interacting with OS
- `shutil` → File operations
- `subprocess` → Running system commands
- `pyautogui` → Automating keyboard/mouse
- `schedule` → Task scheduling

#### 🔹 Databases
- `sqlite3` → SQLite database
- `sqlalchemy` → ORM for databases
- `pymysql` / `psycopg2` → MySQL/PostgreSQL support

#### 🔹 Security & Encryption
- `hashlib` → Hashing (MD5, SHA)
- `cryptography` → Secure encryption

#### 🔹 Date & Time Handling
- `datetime` → Working with dates and times
- `time` → Time-related functions

---

## 🔹 Python Packages
A **package** is a collection of modules. It contains an `__init__.py` file (optional in Python 3.x), which makes Python treat the directory as a package.

### ✅ **Example of a Package Structure**
```
my_package/
│── __init__.py  # Marks it as a package
│── module1.py   # Module 1
│── module2.py   # Module 2
```

### ✅ **Importing a Module from a Package**
```python
from my_package import module1
```

---

## 🔹 PIP (Python Package Installer)
`pip` is the package manager for Python, used to install, update, and manage third-party libraries.

### ✅ **Common `pip` Commands**
- Install a package: `pip install package_name`
- Install a specific version: `pip install package_name==1.2.3`
- Upgrade a package: `pip install --upgrade package_name`
- Uninstall a package: `pip uninstall package_name`
- List installed packages: `pip list`
- Show details of a package: `pip show package_name`
- Install from `requirements.txt`: `pip install -r requirements.txt`

---

## 🔹 REST API (Representational State Transfer API)
A **REST API** is a web service that allows communication between clients and servers using HTTP methods.

### ✅ **Common HTTP Methods in REST API**
| Method | Description |
|--------|-------------|
| `GET`  | Retrieve data |
| `POST` | Send data (create resource) |
| `PUT`  | Update existing data |
| `DELETE` | Remove data |

### ✅ **Example: Fetching Data from an API using `requests`**
```python
import requests
response = requests.get("https://api.example.com/data")
print(response.json())
```

### ✅ **Key Characteristics of REST API**
- **Stateless** → Each request is independent; the server does not store client state.
- **Client-Server Architecture** → Separation between frontend and backend.
- **Uniform Interface** → Uses standard HTTP methods.
- **JSON or XML Format** → Data exchange typically uses JSON.

---

## 🔹 Conclusion
- **Modules** help organize code into reusable files.
- **Packages** group multiple modules into a single directory.
- **PIP** is used for package management in Python.
- **REST APIs** allow interaction between systems using HTTP methods.

This structure ensures efficient development and easy maintenance in real-world projects! 🚀

