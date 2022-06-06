# Balanced-parentheses
This is a Python solution for balanced parenthesis without the use of Hash map. 

For this solution, we have used a function that takes in an expression (only opening and closing brackets).

How does this work:
- We have used stack for its implementation.
- Alongside dictionary datatype that maps for an opening bracket when a closing bracket is encountered.
- If the closing bracket pairs perfectly with the top-most elements of the stack, the top-most element is popped.
- As this goes on, 
  - if the list is empty, then the expression is balanced
  - if not, the expression is not balanced
- There are cases like,
  - The stack is empty and we encounter a closing parenthesis. This is invalid so we directly return False
  - Stack is not empty but expression traversal has ended. Hence, the expression isn't balanced. Return False.
