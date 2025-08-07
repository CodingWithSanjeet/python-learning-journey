import os
import sys

# Step 1: Create a virtual environment
# Use 'py -m venv' followed by the environment name
# This creates a new directory with the virtual environment files
os.system("py -m venv env_name")

# Step 2: Activate the virtual environment
# On Windows: Use Scripts\activate (or Scripts\activate.bat)
# On Linux/Mac: Use bin/activate
# Note: os.system() runs this but doesn't persist the activation
# For manual activation, run: env_name\Scripts\activate in command prompt
os.system(r"env_name\Scripts\activate")

# Step 3: Install required packages
# Once activated, pip installs packages only in the virtual environment
# This keeps your project dependencies isolated from system Python
os.system("pip install -r requirements.txt")

# Additional Notes:
# - To deactivate: type 'deactivate' in the activated environment
# - To delete: simply delete the environment folder (env_name)
# - Always activate before installing packages for your project