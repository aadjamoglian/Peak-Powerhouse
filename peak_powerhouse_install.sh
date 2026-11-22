# !/bin/bash

echo "Beginning Peak Powerhouse Installation..."

# Install Python modules
python3 "./python_quick_install_modules.py"

if [ $? -ne 0 ]; then
    echo "ERROR: Module installation failed."
    exit 1
fi

echo "Virtual environment and modules installation complete! (1/3)"

# Activate virtual environment
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/.venv/bin/activate"

if [ $? -ne 0 ]; then
    echo "ERROR: Virtual environment activation failed."
    exit 1
fi

echo "Virtual environment activated! (2/3)"

# Load DDL into database
python3 "./python_quick_install_ddl.py"

if [ $? -ne 0 ]; then
    echo "ERROR: DDL installation failed."
    exit 1
fi

echo "DDL Loaded To DB! (3/3)"

echo "Installation has completed successfully!"

echo "Initiating program now..."

# Load DDL into database
python3 "./peak_cli.py"