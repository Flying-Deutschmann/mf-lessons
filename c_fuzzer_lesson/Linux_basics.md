# Basic Ubuntu Commands
This guide provides a list of essential commands for navigating and managing a system in Ubuntu Linux.

## Table of Contents
1. [Navigating the Filesystem](#navigating-the-filesystem)
2. [File Operations](#file-operations)
3. [Process Management](#process-management)
4. [System Information](#system-information)
5. [Package Management](#package-management)
6. [User Management](#user-management)
7. [Networking](#networking)

---

## Navigating the Filesystem

- **`pwd`**: Display the current working directory.
  ```bash
  pwd
  ```

- **`ls`**: List files and directories in the current directory.
  ```bash
  ls
  ```

- **`cd`**: Change the directory.
  ```bash
  cd /path/to/directory
  ```

---

## File Operations

- **`touch`**: Create a new empty file.
  ```bash
  touch filename.txt
  ```

- **`cp`**: Copy files or directories.
  ```bash
  cp source.txt destination.txt
  ```

- **`mv`**: Move or rename files or directories.
  ```bash
  mv old_name.txt new_name.txt
  ```

- **`rm`**: Remove files or directories.
  ```bash
  rm filename.txt
  ```

- **`cat`**: View the contents of a file.
  ```bash
  cat filename.txt
  ```

---

## Process Management

- **`ps`**: List running processes.
  ```bash
  ps aux
  ```

- **`top`**: Display real-time system information and running processes.
  ```bash
  top
  ```

- **`kill`**: Terminate a process by its PID.
  ```bash
  kill <PID>
  ```

---

## System Information

- **`df`**: Show disk space usage.
  ```bash
  df -h
  ```

- **`free`**: Display memory usage.
  ```bash
  free -h
  ```

- **`uname`**: Display system information.
  ```bash
  uname -a
  ```

---

## Package Management

- **`apt update`**: Update the package list.
  ```bash
  sudo apt update
  ```

- **`apt install`**: Install a package.
  ```bash
  sudo apt install package_name
  ```

- **`apt upgrade`**: Upgrade all installed packages.
  ```bash
  sudo apt upgrade
  ```

---

## User Management

- **`adduser`**: Add a new user.
  ```bash
  sudo adduser username
  ```

- **`passwd`**: Change a user’s password.
  ```bash
  sudo passwd username
  ```

---

## Networking

- **`ping`**: Test network connectivity.
  ```bash
  ping google.com
  ```

---

This is a basic guide to some common Ubuntu commands. For more advanced usage, consult the man pages or Ubuntu documentation.
