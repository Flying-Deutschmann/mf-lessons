# PowerShell script to uninstall WSL, Git, and Notepad++ via winget

# Step 1: Uninstall WSL (Windows Subsystem for Linux)
Write-Host "Uninstalling WSL..."

# Unregister all installed WSL distros
$distros = wsl.exe --list --quiet
foreach ($distro in $distros) {
    Write-Host "Unregistering WSL distro: $distro"
    wsl.exe --unregister $distro
}

# Disable WSL feature
Write-Host "Disabling WSL feature..."
Disable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux -NoRestart

# Uninstall WSL using PowerShell
Write-Host "Uninstalling Windows Subsystem for Linux..."
wsl --uninstall

# Step 2: Uninstall Git installed via winget
Write-Host "Uninstalling Git..."

# Check if Git is installed using winget
$gitInstalled = winget list git
if ($gitInstalled) {
    winget uninstall --id Git.Git -e --source winget
    Write-Host "Git uninstalled successfully."
} else {
    Write-Host "Git is not installed via winget."
}

# Step 3: Uninstall Notepad++ installed via winget
Write-Host "Uninstalling Notepad++..."

# Check if Notepad++ is installed using winget
$notepadInstalled = winget list Notepad++
if ($notepadInstalled) {
    winget uninstall --id Notepad++.Notepad++ -e --source winget
    Write-Host "Notepad++ uninstalled successfully."
} else {
    Write-Host "Notepad++ is not installed via winget."
}

Write-Host "Uninstallation process completed."

shutdown /r
