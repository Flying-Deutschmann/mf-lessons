# Function to uninstall AWS CLI
Write-Host "Uninstalling AWS CLI..."
$awsCliUninstall = Get-WmiObject -Class Win32_Product | Where-Object { $_.Name -like "AWS CLI*" }
if ($awsCliUninstall) {
    $awsCliUninstall.Uninstall()
    Write-Host "AWS CLI uninstalled successfully."
} else {
    Write-Host "AWS CLI not found."
}

# Function to uninstall Python 3
Write-Host "Uninstalling Python 3..."
$pythonUninstall = Get-WmiObject -Class Win32_Product | Where-Object { $_.Name -like "Python 3*" }
if ($pythonUninstall) {
    $pythonUninstall.Uninstall()
    Write-Host "Python 3 uninstalled successfully."
} else {
    Write-Host "Python 3 not found."
}

# Function to uninstall Git
Write-Host "Uninstalling Git..."
$gitUninstall = Get-WmiObject -Class Win32_Product | Where-Object { $_.Name -like "Git*" }
if ($gitUninstall) {
    $gitUninstall.Uninstall()
    Write-Host "Git uninstalled successfully."
} else {
    Write-Host "Git not found."
}

Write-Host "Uninstalling Notepad++..."
$notepadUninstall = Get-WmiObject -Query "SELECT * FROM Win32_Product WHERE Name LIKE '%Notepad++%'" | Select-Object Name
if ($notepadUninstall) {
    $notepadUninstall.Uninstall()
    Write-Host "Notepad++ uninstalled successfully."
} else {
    Write-Host "Notepad not found."
}

# Function to check if Git Bash is still there
Write-Host "Checking for Git Bash..."
$gitBashPath = "C:\Program Files\Git\bin\bash.exe"
if (Test-Path $gitBashPath) {
    Write-Host "Git Bash found at $gitBashPath. Removing Git..."
    $gitBashUninstall = Get-WmiObject -Class Win32_Product | Where-Object { $_.Name -like "Git*" }
    if ($gitBashUninstall) {
        $gitBashUninstall.Uninstall()
        Write-Host "Git Bash uninstalled successfully."
    } else {
        Write-Host "Git Bash uninstallation failed."
    }
} else {
    Write-Host "Git Bash not found."
}

# Deactivate the Python virtual environment (if it's activated)
Write-Host "Checking if a Python virtual environment is active..."

# Check if the Python virtual environment is active by inspecting the 'VIRTUAL_ENV' environment variable
if ($env:VIRTUAL_ENV) {
    Write-Host "Deactivating Python virtual environment..."
    deactivate
    Write-Host "Python virtual environment deactivated."
} else {
    Write-Host "No active Python virtual environment found."
}

# Verify uninstallations
Write-Host "Verifying AWS CLI uninstallation..."
$awsCliCheck = Get-WmiObject -Query "SELECT * FROM Win32_Product WHERE Name LIKE '%Notepad++%'" | Select-Object Name
if ($awsCliCheck) {
    Write-Host "AWS CLI is still installed."
} else {
    Write-Host "AWS CLI uninstalled successfully."
}

Write-Host "Verifying Python 3 uninstallation..."
$pythonCheck = Get-WmiObject -Class Win32_Product | Where-Object { $_.Name -like "Python 3*" }
if ($pythonCheck) {
    Write-Host "Python 3 is still installed."
} else {
    Write-Host "Python 3 uninstalled successfully."
}

Write-Host "Verifying Notepad++ uninstallation..."
$notepadCheck = Get-WmiObject -Class Win32_Product | Where-Object { $_.Name -like "Git*" }
if ($notepadCheck) {
    Write-Host "Notepad++ is still installed."
} else {
    Write-Host "Git uninstalled successfully."
}
Write-Host "Verifying Notepad++ uninstallation"

Write-Host "Verifying Git uninstallation..."
$gitCheck = Get-WmiObject -Class Win32_Product | Where-Object { $_.Name -like "Git*" }
if ($gitCheck) {
    Write-Host "Git is still installed."
} else {
    Write-Host "Git uninstalled successfully."
}
Write-Host "Verifying Git uninstallation"

Write-Host "Uninstallation complete!"
