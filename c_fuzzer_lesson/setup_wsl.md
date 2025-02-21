# This instruction will guid you through installing WSL and setting up your CLI dev environment.

## Using Windows Subsystem for Linux (WSL)
WSL allows you to run a Linux environment directly on Windows, making it a great way to use AFL.

## Install WSL (Windows Subsystem for Linux)
Open PowerShell as an administrator and run the following command:
```powershell
wsl --install
```
Restart your machine if required.
```powershell
reboot
```
## Setup WSL
After restarting, choose a Linux distribution from the Microsoft Store (e.g., Ubuntu).

By default, Ubuntu will be installed. If you want to choose a different Linux distribution (like Debian, Kali, or Fedora), follow these steps:
List available distributions: Run the following command to see the list of available Linux distributions:
```
wsl --list --online
```

Install a specific distribution: To install a specific Linux distribution (e.g., Debian or Kali), use the following command:
```
wsl --install -d <DistroName>
```
For example, to install Debian:
```
wsl --install -d Debian
```
Set your default distribution: If you installed multiple distributions, you can set one as the default by running:
```
wsl --setdefault <DistroName>
```
For example:
```
wsl --setdefault Ubuntu
```
### Set WSL Version to 2 (Optional, but recommended)
WSL 2 offers better performance and compatibility with Linux apps than WSL 1. To ensure you're using WSL 2:
Check the installed WSL version: Run the following command:
```
wsl --list --verbose
```

Set your distribution to WSL 2: If your distribution is set to WSL 1, you can change it to WSL 2 with this command:
```
wsl --set-version <DistroName> 2
```

For example:
```
wsl --set-version Ubuntu 2
```

Verify the version change: Check that the version has been set to WSL 2:
```
wsl --list --verbose
```

## Install Dependencies in WSL
Open your WSL terminal (e.g., Ubuntu).
```
wsl
```
Update your package lists:
```
sudo apt update
sudo apt upgrade
```
Install the necessary build tools:
```
sudo apt install build-essential clang llvm gcc g++ make git
```

You can access your Windows files from within WSL using the /mnt directory. For example:
To access the C: drive from WSL:
```
cd /mnt/c/
```

To open files 
