# FuzzyMatcher

The **FuzzyMatcher** class is a Python class that allows you to perform fuzzy string matching tasks on input text using the **rapidfuzz library**. It offers a method for finding the closest match to an input string from a list of choices based on partial string matching. The class can be easily integrated into your Python projects by following the simple installation and usage instructions provided below. Contributions to the project are welcome and the class is licensed under the MIT License.

**Installation**
To install the **rapidfuzz** library, you can use pip:


`pip install rapidfuzz`

**Usage**

To use the **FuzzyMatcher** class in your Python project, simply import the class and create an instance with an optional threshold value:

```python
from fuzz_matcher import FuzzyMatcher

# Create an instance of the FuzzyMatcher class with a threshold of 90
matcher = FuzzyMatcher(90)

# Find the closest match to "appel" from the list of choices
choices = ["apple", "banana", "orange", "kiwi"]
closest_match = matcher.match("appel", choices)

print(closest_match)
# Output: "apple"
```

The match method of the **FuzzyMatcher** class takes an input string and a list of choices. It iterates over each choice and computes a partial string match ratio between the input string and the choice. If the ratio is higher than the previous highest ratio and above the threshold, the current choice is considered the best match so far. The method returns the best match found.

You can customize the threshold value in the constructor of the **FuzzyMatcher** class to adjust the sensitivity of the matching algorithm. The default threshold value is set to 80, but you can set it to any value between 0 and 100.

------------


**License**
The **FuzzyMatcher** class is licensed under the MIT License. Feel free to use, modify, and distribute this code as needed.