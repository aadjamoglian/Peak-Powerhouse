Write-Host "Beginning Peak Powerhouse Installation..."
python ".\python_quick_install_modules.py"
Write-Host "Virtual environment and modules installation complete! (1/3)"
& "$PSScriptRoot\.venv\Scripts\Activate.ps1"
Write-Host "Virtual environment activated! (2/3)"
python ".\python_quick_install_ddl.py"
Write-Host "DDL Loaded To DB! (3/3)"
Write-Host "Installation has completed successfully!"


