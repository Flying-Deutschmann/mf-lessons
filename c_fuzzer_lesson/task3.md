## 2. IO Task

### Instructions:
- This task requires you to get input from the user and display output based on that input.
- Use scanf() to ask the user for their name and age, then output a greeting message using printf().

### Example:
```
#include <stdio.h>

int main() {
    char name[50];
    int age;

    // Input from the user
    printf("Enter your name: ");
    scanf("%s", name);
    printf("Enter your age: ");
    scanf("%d", &age);

    // Output the user input
    printf("Hello, %s! You are %d years old.\n", name, age);
    
    return 0;
}
```
