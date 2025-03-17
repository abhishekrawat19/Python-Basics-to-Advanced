# DateTime Module Methods in Python

## 🔹 Introduction

The `datetime` module in Python provides classes and functions for working with dates and times. To use these functions, **import the ****`datetime`**** module** first:

```python
import datetime
```

---

## 🔹 Getting the Current Date & Time

### ✅ `datetime.datetime.now()` – Returns the current date and time

```python
import datetime
now = datetime.datetime.now()
print(now)
```

🔹 **Output:**

```
2025-03-13 14:30:45.678901
```

### ✅ `datetime.datetime.now().hour` – Returns the current hour

```python
current_hour = datetime.datetime.now().hour
print(current_hour)
```

🔹 **Output:**

```
14
```

### ✅ `datetime.date.today()` – Returns the current date (without time)

```python
today = datetime.date.today()
print(today)
```

🔹 **Output:**

```
2025-03-13
```

### ✅ `datetime.datetime.utcnow()` – Returns the current UTC date and time

```python
utc_now = datetime.datetime.utcnow()
print(utc_now)
```

🔹 **Output:**

```
2025-03-13 12:30:45.678901
```

---

## 🔹 Creating Date & Time Objects

### ✅ Creating a `datetime` object

```python
dt = datetime.datetime(2025, 3, 13, 14, 30, 45)
print(dt)
```

🔹 **Output:**

```
2025-03-13 14:30:45
```

### ✅ Creating a `date` object

```python
d = datetime.date(2025, 3, 13)
print(d)
```

🔹 **Output:**

```
2025-03-13
```

### ✅ Creating a `time` object

```python
t = datetime.time(14, 30, 45)
print(t)
```

🔹 **Output:**

```
14:30:45
```

---

## 🔹 Formatting & Parsing Dates

### ✅ `strftime()` – Convert `datetime` object to formatted string

```python
dt = datetime.datetime(2025, 3, 13, 14, 30, 45)
formatted_date = dt.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date)
```

🔹 **Output:**

```
2025-03-13 14:30:45
```

### ✅ `strptime()` – Convert string to `datetime` object

```python
date_string = "2025-03-13 14:30:45"
dt = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(dt)
```

🔹 **Output:**

```
2025-03-13 14:30:45
```

---

## 🔹 Date Arithmetic & Time Differences

### ✅ Finding difference between two dates

```python
dt1 = datetime.datetime(2025, 3, 13, 14, 30, 45)
dt2 = datetime.datetime(2025, 3, 10, 10, 15, 30)
delta = dt1 - dt2
print(delta)
print(delta.days, "days")
```

🔹 **Output:**

```
3 days, 4:15:15
3 days
```

### ✅ Adding and subtracting days

```python
dt = datetime.datetime(2025, 3, 13, 14, 30, 45)
new_dt = dt + datetime.timedelta(days=7)
print(new_dt)
```

🔹 **Output:**

```
2025-03-20 14:30:45
```

---

## 🔹 Extracting Components from a DateTime Object

### ✅ Extracting year, month, day, hour, minute, second

```python
dt = datetime.datetime(2025, 3, 13, 14, 30, 45)
print(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
```

🔹 **Output:**

```
2025 3 13 14 30 45
```

### ✅ Finding weekday

```python
dt = datetime.datetime(2025, 3, 13)
print(dt.weekday())  # Monday = 0, Sunday = 6
print(dt.isoweekday())  # Monday = 1, Sunday = 7
```

🔹 **Output:**

```
3
4
```

---

## 🔹 Time Zone Handling

### ✅ Getting UTC time

```python
utc_time = datetime.datetime.utcnow()
print(utc_time)
```

🔹 **Output:**

```
2025-03-13 12:30:45.678901
```

### ✅ Converting to a specific timezone

```python
from datetime import timezone

dt = datetime.datetime(2025, 3, 13, 14, 30, 45, tzinfo=timezone.utc)
print(dt)
```

🔹 **Output:**

```
2025-03-13 14:30:45+00:00
```

---

## 🔹 Conclusion

- The `datetime` module is essential for handling dates and times in Python.
- Supports **formatting, parsing, arithmetic, and timezone management**.
- Use `datetime.datetime.now()` to get the current date and time.
- Use `datetime.datetime.now().hour` to get the current hour directly.
- Use `strftime()` to format dates and `strptime()` to parse date strings.
- Use `timedelta` for date arithmetic.

Lets begin🚀

