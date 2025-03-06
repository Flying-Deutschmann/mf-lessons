## Build Requirements:

- git installed
- python3.10+ install

## Setup Lab
In an admin PS terminal enable remote signed scripts
```powershell
Set-ExecutionPolicy RemoteSigned
```

Install lab tools
```powershell
.\setup_lab.ps1
```

## Tasks:

1. **Demonstration**: Introduction to python code              task1.md
2. **Setup Python**: Setup python env and deps                 task2.md
3. **Setup Awsconf**: Setup auth for AWS                       task3.md
4. **Create EC2**: Create EC2 container                        task4.md
5. **SSH to instance**: SSH to created container               task5.md
6. **Create S3 Bucket**: Create bucket and file                task6.md

## Examples
Examples of these tasks are provided in the task instructions, can be found in `code\`.

## Cleanup Lab
Unnstall lab tools
```powershell
.\cleanup_lab.ps1
```
