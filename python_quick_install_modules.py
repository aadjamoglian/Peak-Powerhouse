import subprocess
import sys
import platform

# Get OS name
os_name = platform.system()
print("Operating System: " + os_name)

# Install virtual environment
try:
    subprocess.run(
        [sys.executable, "-m", "venv", ".venv"],
        check=True
    )

    print("Virtual environment created successfully.")
except subprocess.CalledProcessError as e:
    print(f"Failed to create virtual environment: {e}")

if platform.system() == "Windows":
    venv_python = r".venv\Scripts\python.exe"
else:
    venv_python = ".venv/bin/python"

# Install modules listed in requirements.txt
subprocess.run(
    [venv_python, "-m", "pip", "install", "-r", "requirements.txt"],
    check=True
)

print("Modules installed successfully!")