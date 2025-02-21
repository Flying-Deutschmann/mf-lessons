
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

```
gcc -o vulnerable_program vulnerable.c -fno-stack-protector -z execstack -g
```

### Explanation of Parameters:
- `-fno-stack-protector`: Disables stack protection, making the program more vulnerable to buffer overflow attacks.
- `-z execstack`: Makes the stack executable, which is necessary for running code that is injected into the stack during exploitation.
- `-g`: Includes debugging symbols in the compiled binary, useful for debugging and analysis.

This command is identical to the one in Bash, as it is a standard GCC compiler invocation. Just ensure that GCC is installed and properly set up on your system, which can be verified by running `gcc --version` in PowerShell.

## Create a Test Input Corpus
Fuzzers like AFL need initial "seeds" to start the fuzzing process. In this case, we can start with a simple test case that the program expects. 

### Create a folder for input files:
```
mkdir input_corpus
echo "test" > input_corpus/test_case
```
### Run AFL Fuzzer
Run AFL to start fuzzing the program. AFL will generate new input files based on the initial test case and feed them to the vulnerable program to see how it behaves.

Run AFL with the following command:
```
afl-fuzz -i input_corpus -o output_corpus -- ./vulnerable_program @@
```

   - `-i input_corpus`: Specifies the input directory with initial test cases.
   - `-o output_corpus`: Specifies the output directory where AFL will store its findings.
   - `@@`: A placeholder for AFL to insert the fuzzed input into the program.

### Monitor the Results
After AFL starts fuzzing, monitor the progress:
   - AFL will display output such as the number of crashes, hangs, and how much code coverage it has achieved.
   - If a crash occurs, AFL will save the input that caused the crash.

Example output:
```
[+] AFL has detected a crash in the program. Check the output directory for the problematic input file.
```

### Analyze the Crash
If AFL finds a crash, it will save the problematic input to a file inside the `output_corpus` directory. For example, you might find a file like `crash-01`.

Check the contents of the `crash-01` file:
```
cat output_corpus/crashes/crash-01
```



