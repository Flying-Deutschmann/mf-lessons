## 7. Create a Vulnrable program that exploits strcpy to cause a buffer overflow.


## Add the header files (libs)
```
#include <stdio.h>
#include <string.h>
```

## Create a secret function that can be exploited in a buffer overflow.
```
void secret_function() {
    // This function is called if a buffer overflow occurs and it gets executed.
    printf("You've reached the secret function!\n");
}
```

## Create a function that includes strcpy 
```
void vulnerable_function(char *input) {
    char buffer[64];  // A buffer of fixed size 64 bytes

    // strcpy is unsafe because it does not check the length of the input string.
    // If the input string is larger than 64 bytes, it will overflow the buffer and write past the end of the array.
    strcpy(buffer, input);  // Vulnerable to buffer overflow
}
```

## Create a main function to call and handle the other functions.
```
int main(int argc, char *argv[]) {
    if (argc < 2) {
        // If the user doesn't provide an argument, it tells them how to run the program.
        printf("Usage: %s <input_string>\n", argv[0]);
        return 1;
    }

    // The program takes an argument (argv[1]) and passes it to vulnerable_function.
    vulnerable_function(argv[1]);

    return 0;
}
```

## Compile Program
```
gcc -o vulnerable_program vulnerable.c
```

## Run Executable (program)
```
./vulnreable_program
```

