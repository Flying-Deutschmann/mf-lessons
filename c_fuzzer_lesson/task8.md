
## Requirements
- WSL
 - gcc
 - g++
 - llvm
 - git
 - afl
 - make

## Installing AFL
From within the WSL environment

Clone the AFL repository from GitHub:
```
git clone https://github.com/google/AFL.git

cd AFL
```
### Build AFL using make:
```
make
sudo make install
```

### Verify AFL Installation
Check if AFL is installed successfully by running:
```
afl-fuzz -h
```
This should display AFL's help message, confirming that it's installed.

## Compile the vulnerable program with AFL

```powershell
gcc -o vulnerable_program vulnerable.c -fno-stack-protector -z execstack -g
```

### Explanation of Parameters:
- `-fno-stack-protector`: Disables stack protection, making the program more vulnerable to buffer overflow attacks.
- `-z execstack`: Makes the stack executable, which is necessary for running code that is injected into the stack during exploitation.
- `-g`: Includes debugging symbols in the compiled binary, useful for debugging and analysis.

This command is identical to the one in Bash, as it is a standard GCC compiler invocation. Just ensure that GCC is installed and properly set up on your system, which can be verified by running `gcc --version` in PowerShell.
