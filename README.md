•	Multi-Level Grade Engine - Debugging Task

Objective
The purpose of this task was to identify and correct errors in a given Python program. This activity helped improve debugging skills and understanding of Python syntax and logic.

## Errors Found in the Original Code

1. Indentation Errors:
   The statements inside the while loop were not properly indented. In Python, indentation defines the structure of loops and conditions.

2. Missing Colon:
   The condition "if percentage > 100" was missing a colon at the end.

3. Incorrect Print Statement:
   The line:
   print("Percentage:", percentage) print("Fails:", fail
   had two print statements written on the same line and one closing bracket was missing.

4. Logical Structure Issue:
   The percentage validation was placed after grade calculation logic, which could lead to incorrect output flow.

Corrections Made

1. Proper indentation was applied inside the while loop.
2. Missing colon was added in the conditional statement.
3. Print statements were separated and syntax was corrected.
4. Validation for invalid percentage (>100) was structured properly before grade calculation.
5. Overall code structure was organized for correct execution flow.

 Learning Outcomes

Through this debugging activity, I learned:

- Importance of indentation in Python
- How to identify syntax errors
- How to fix logical mistakes
- Proper structure of conditional statements
- Writing clean and error-free Python code 

 Conclusion

After correcting the errors, the program now successfully:
- Accepts subject marks
- Calculates total percentage
- Counts failed subjects
- Displays overall result and grade
- Handles invalid percentage cases correctly

