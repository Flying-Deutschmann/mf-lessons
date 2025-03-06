# Function to install AWS CLI
Write-Host "Installing AWS CLI..."
Invoke-WebRequest -Uri "https://awscli.amazonaws.com/AWSCLIV2/latest/AWSCLIV2.msi" -OutFile "$env:TEMP\AWSCLIV2.msi"
Start-Process msiexec.exe -ArgumentList "/i", "$env:TEMP\AWSCLIV2.msi", "/quiet", "/norestart" -Wait
Remove-Item "$env:TEMP\AWSCLIV2.msi" -Force

# Function to install Python 3
Write-Host "Installing Python 3..."
Invoke-WebRequest -Uri "https://www.python.org/ftp/python/3.9.7/python-3.9.7-amd64.exe" -OutFile "$env:TEMP\python-3.9.7-amd64.exe"
Start-Process "$env:TEMP\python-3.9.7-amd64.exe" -ArgumentList "/quiet", "InstallAllUsers=1", "PrependPath=1" -Wait
Remove-Item "$env:TEMP\python-3.9.7-amd64.exe" -Force

# Function to install Pip3
Write-Host "Pip3 should have been installed along with Python 3, checking..."
python -m ensurepip --upgrade

# Function to install Git
Write-Host "Installing Git..."
Invoke-WebRequest -Uri "https://github.com/git-for-windows/git/releases/download/v2.33.0.windows.2/Git-2.33.0-64-bit.exe" -OutFile "$env:TEMP\Git-2.33.0-64-bit.exe"
Start-Process "$env:TEMP\Git-2.33.0-64-bit.exe" -ArgumentList "/VERYSILENT", "/NORESTART" -Wait
Remove-Item "$env:TEMP\Git-2.33.0-64-bit.exe" -Force

# Function to install Git Bash (Git for Windows includes Git Bash)
Write-Host "Git Bash should be installed with Git..."

# Verify installations
Write-Host "Verifying AWS CLI installation..."
aws --version

Write-Host "Verifying Python 3 installation..."
python --version

Write-Host "Verifying Git installation..."
git --version

Write-Host "All tools installed successfully!"
