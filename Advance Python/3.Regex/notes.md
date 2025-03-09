# Regular Expressions (Regex) in Python

## What is Regex?
- Regular Expressions (**regex**) are patterns used to match **strings**.
- Python provides the `re` module for working with regex.

## Importing the `re` Module
```python
import re
```

## Common Regex Functions

### 1. `re.match()`
- Checks for a match **only at the beginning** of a string.
```python
pattern = r'hello'
text = 'hello world'
match = re.match(pattern, text)
if match:
    print(match.group())  # Output: hello
```

### 2. `re.search()`
- Searches **anywhere** in the string for a match.
```python
text = 'Say hello to the world'
match = re.search(r'hello', text)
if match:
    print(match.group())  # Output: hello
```

### 3. `re.findall()`
- Returns **all matches** in a list.
```python
text = 'apple banana apple orange'
matches = re.findall(r'apple', text)
print(matches)  # Output: ['apple', 'apple']
```

### 4. `re.sub()`
- Replaces **all matches** with a given string.
```python
text = 'Hello world!'
new_text = re.sub(r'world', 'Python', text)
print(new_text)  # Output: Hello Python!
```

### 5. `re.split()`
- Splits the string **at each match**.
```python
text = 'one,two;three.four'
result = re.split(r'[;,\.]', text)
print(result)  # Output: ['one', 'two', 'three', 'four']
```

### 6. `re.compile()`
- Precompiles a regex pattern for reuse.
```python
pattern = re.compile(r'\d+')
text = 'The price is 100 dollars'
match = pattern.search(text)
print(match.group())  # Output: 100
```

## Regex Metacharacters
- `.` → Any character except newline
- `^` → Start of a string
- `$` → End of a string
- `*` → Zero or more occurrences
- `+` → One or more occurrences
- `?` → Zero or one occurrence
- `{n,m}` → Between `n` and `m` occurrences
- `[]` → Set of characters
- `|` → OR operator
- `\\d` → Digit
- `\\w` → Word character
- `\\s` → Whitespace

## Advanced Regex Features

### 1. Lookaheads and Lookbehinds
#### Positive Lookahead (`?=`)
- Matches if a pattern is **followed by** another pattern.
```python
text = 'apple123'
match = re.search(r'apple(?=\d+)', text)
print(match.group())  # Output: apple
```

#### Negative Lookahead (`?!`)
- Matches if a pattern is **not followed by** another pattern.
```python
text = 'appleXYZ'
match = re.search(r'apple(?!\d+)', text)
print(match.group())  # Output: apple
```

#### Positive Lookbehind (`?<=`)
- Matches if a pattern is **preceded by** another pattern.
```python
text = '123apple'
match = re.search(r'(?<=\d)apple', text)
print(match.group())  # Output: apple
```

#### Negative Lookbehind (`?<!`)
- Matches if a pattern is **not preceded by** another pattern.
```python
text = 'XYZapple'
match = re.search(r'(?<!\d)apple', text)
print(match.group())  # Output: apple
```

### 2. Flags in Regex
- `re.IGNORECASE (re.I)` → Case-insensitive matching.
- `re.MULTILINE (re.M)` → `^` and `$` match start and end of each line.
- `re.DOTALL (re.S)` → `.` matches **newline** characters too.

#### Example:
```python
text = 'Hello\nWorld'
match = re.search(r'hello.world', text, re.IGNORECASE | re.DOTALL)
print(match.group())  # Output: Hello\nWorld
```

### 3. Named Groups
- Allows capturing groups with names.
```python
text = 'Name: John, Age: 30'
match = re.search(r'Name: (?P<name>\w+), Age: (?P<age>\d+)', text)
print(match.group('name'))  # Output: John
print(match.group('age'))   # Output: 30
```

### 4. Non-Capturing Groups
- Use `(?:...)` to group without capturing.
```python
text = 'apple123'
match = re.search(r'(?:apple)\d+', text)
print(match.group())  # Output: apple123
```

## Conclusion
Regular expressions are powerful for string matching and manipulation. The `re` module provides extensive functionality, including advanced features like lookaheads, lookbehinds, flags, named groups, and non-capturing groups. Mastering regex can significantly improve text processing efficiency.
