## 3. Operator Task

## Instructions:
- In this task, you'll work with arithmetic, relational, and logical operators.
- Perform basic arithmetic operations (addition, multiplication) on two numbers.
- Use relational operators to compare two numbers.
- Use logical operators to evaluate conditions and combine them.

## Example:
```
#include <stdio.h>

int main() {
    int a = 10, b = 5;

    // Arithmetic operators
    int sum_result = a + b;
    int product_result = a * b;

    // Relational operator
    int is_equal = (a == b);

    // Logical operator
    int is_true = (a > b) && (b > 0);

    printf("Sum: %d, Product: %d, Is Equal: %d, Is True: %d\n", sum_result, product_result, is_equal, is_true);
    
    return 0;
}
```
