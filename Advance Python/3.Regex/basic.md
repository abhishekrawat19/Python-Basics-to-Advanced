# Regular Expressions (Regex) Topics and Answers

## 1. Introduction to Regular Expressions
- **What is a regular expression?**
  - A regex is a pattern used to match character combinations in strings. It allows for advanced search, validation, and manipulation of text.
  
- **Common Use Cases of Regex:**
  - Data validation (email, phone numbers)
  - String manipulation (replace, split)
  - Searching (find specific patterns)

---

## 2. Basic Syntax and Metacharacters
- **Literal Characters:**
  - Match the exact characters (e.g., `a`, `b`, `1`, `@`).
  - **Q:** How would you match the literal string `"apple"` in a regex?
    - **Answer:** `apple` (matches the exact string "apple").
  
- **Metacharacters:**
  - **Dot (`.`):** Matches any character except a newline.
  - **Caret (`^`):** Anchors the match to the start of the string.
  - **Dollar (`$`):** Anchors the match to the end of the string.
  - **Q:** What is the difference between `^a` and `a$` in a regex?
    - **Answer:** `^a` matches "a" at the beginning of a string, while `a$` matches "a" at the end of a string.

---

## 3. Character Classes
- **Character Sets:**
  - `[abc]`: Matches any character inside the brackets (`a`, `b`, or `c`).
  - `[^abc]`: Matches any character **except** those listed inside the brackets.
  
- **Predefined Character Classes:**
  - `\d`: Matches any digit (equivalent to `[0-9]`).
  - `\w`: Matches any word character (alphanumeric + underscore).
  - `\s`: Matches any whitespace character (spaces, tabs, line breaks).
  - **Q:** How would you match any non-digit character in a string?
    - **Answer:** `\D` (matches any character that is not a digit).

---

## 4. Quantifiers
- **Quantifiers:**
  - `*`: Matches 0 or more occurrences of the preceding element.
  - `+`: Matches 1 or more occurrences of the preceding element.
  - `?`: Matches 0 or 1 occurrence of the preceding element.
  - `{n}`: Matches exactly n occurrences of the preceding element.
  - `{n,}`: Matches n or more occurrences.
  - `{n,m}`: Matches between n and m occurrences.
  - **Q:** What is the difference between `a*` and `a+` in a regex?
    - **Answer:** `a*` matches zero or more "a"s, while `a+` matches one or more "a"s.

---

## 5. Grouping and Alternation
- **Parentheses `()`**: Used to group expressions.
  - `(abc)+`: Matches one or more occurrences of "abc".
  
- **Alternation `|`:**
  - Matches either of two patterns.
  - `(cat|dog)`: Matches either "cat" or "dog".
  
- **Q:** How would you match either a 3-digit or a 5-digit number using alternation?
  - **Answer:** `\d{3}|\d{5}`

---

## 6. Anchors
- **Anchors:** Used to match positions rather than characters.
  - `^`: Start of a string.
  - `$`: End of a string.
  - `\b`: Word boundary.
  - `\B`: Non-word boundary.
  
- **Q:** How would you match a string that starts with "apple" and ends with "pie"?
  - **Answer:** `^apple.*pie$`

---

## 7. Lookahead and Lookbehind (Advanced)
- **Lookahead (`?=` and `?!`):** Matches a group of characters only if they are followed (or not followed) by a certain pattern.
  - Positive lookahead: `a(?=b)` matches "a" only if it’s followed by "b".
  - Negative lookahead: `a(?!b)` matches "a" only if it’s **not** followed by "b".
  
- **Lookbehind (`?<=` and `?<!`):** Matches a group of characters only if they are preceded (or not preceded) by a certain pattern.
  - Positive lookbehind: `(?<=a)b` matches "b" only if it’s preceded by "a".
  - Negative lookbehind: `(?<!a)b` matches "b" only if it’s **not** preceded by "a".

- **Q:** How would you match a word that is preceded by "apple" but not followed by "pie"?
  - **Answer:** `(?<=apple)\w+(?=!pie)`

---

## 8. Escape Sequences
- **Escape Metacharacters:**
  - To match metacharacters literally, you use a backslash (`\`), such as `\.` for a literal dot.
  - **Q:** How would you match a literal dollar sign (`$`) using a regular expression?
    - **Answer:** `\$`

---

## 9. Regex in Programming Languages
- **Regex in Python:**
  - `re.match()`, `re.search()`, `re.findall()`, `re.sub()`
  - **Q:** How would you extract all digits from a string in Python using regex?
    - **Answer:** `re.findall(r'\d+', text)` (finds all sequences of digits).

- **Regex in JavaScript:**
  - `/pattern/.test()`, `/pattern/.exec()`, `.match()`, `.replace()`
  - **Q:** How would you replace all occurrences of "apple" with "orange" in JavaScript?
    - **Answer:** `str.replace(/apple/g, 'orange')`

---

## 10. Performance Considerations
- **Greedy vs Non-Greedy Matching:**
  - **Greedy (`*` and `+`)** matches as many characters as possible.
  - **Non-Greedy (`*?` and `+?`)** matches as few characters as possible.
  - **Q:** What is the difference between greedy and non-greedy quantifiers?
    - **Answer:** Greedy quantifiers match the longest possible string, while non-greedy quantifiers match the shortest.

---

## 11. Common Regex Problems
- **Validate an Email Address:**
  - Write a regex to validate a basic email address format.
    - **Answer:** `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$`
  
- **Extracting Dates:**
  - Write a regex to match dates in the format `dd/mm/yyyy`.
    - **Answer:** `\b\d{2}/\d{2}/\d{4}\b`

- **Q:** How would you match a date in the form `12-25-2025`?
  - **Answer:** `\b\d{2}-\d{2}-\d{4}\b`

---

## 12. Tips & Best Practices
- **Avoiding Overcomplicated Regexes:**
  - Break complex patterns into smaller parts to make them more readable and maintainable.
  
- **Testing Regular Expressions:**
  - Use online tools like regex101.com or regexr.com to test and debug regex patterns.
  
- **Q:** When would you use a non-capturing group `(?:...)` in a regex?
  - **Answer:** Use non-capturing groups when you want to group elements but do not need to capture the matched text for later use (e.g., `(?:abc)`).

---

## Conclusion
Regular expressions are a powerful tool for pattern matching and text manipulation.To improve, try solving real-world problems (e.g., email validation, data extraction, or text parsing) using regex.
