## 4. Flow Control Task

## Instructions:
- Implement a flow control structure to evaluate the value of a number entered by the user.
- If the number is positive, print a message saying it's positive.
- If the number is zero, print that it is zero.
- If the number is negative, print that it is negative.

## Example:
```
#include <stdio.h>

int main() {
    int number;

    // Input the number from the user
    printf("Enter a number: ");
    scanf("%d", &number);

    // Flow control based on the value of the number
    if (number > 0) {
        printf("The number is positive.\n");
    } else if (number == 0) {
        printf("The number is zero.\n");
    } else {
        printf("The number is negative.\n");
    }

    return 0;
}
```

