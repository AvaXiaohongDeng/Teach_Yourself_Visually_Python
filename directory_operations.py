import os       # Provides methods for working with the file system.
import glob     # Provides a list of files and directories using wildcards.
import sys      # Provides access to system-specific parameters and functions.
import shutil   # Provides methods for file and directory operations.
import getpass  # Provides a way to get the current user's username.

# Get the current directory
thisDir = os.getcwd()
print("\nCurrent directory:", thisDir)

# Get the parent directory
parentDir = os.path.dirname(thisDir)
print("Parent directory:", parentDir)

# List files and directories in the current directory
print("\nListing files and directories:")
ff = os.listdir(thisDir)  # Get a list of files and directories
for item in ff:
    print(item)

# Sort and display the list of files and directories
ff.sort()
print("\nSorted list of files and directories:")
print(ff)

# Search for files and directories whose names begin with 'f'
print("\nFiles and directories starting with 'f':")
fg = glob.glob("f*")
print(fg)

# Move up one directory
os.chdir('..')
print("\nReturned to the parent directory:", os.getcwd())

# Navigate to directory 'Teach_Yourself_Visually_Python'
if os.path.isdir("Teach_Yourself_Visually_Python"):
    os.chdir("Teach_Yourself_Visually_Python")
else:
    print("\nDirectory 'Teach_Yourself_Visually_Python' does not exist.")

# Create a new directory inside 'Teach_Yourself_Visually_Python'
print("\nCreating 'New_Dir' inside 'Teach_Yourself_Visually_Python'")
os.makedirs('New_Dir', exist_ok=True)

# Rename directory 'New_Dir' to 'Renamed_Dir'
print("\nRenaming 'New_Dir' to 'Renamed_Dir'")
os.rename('New_Dir', 'Renamed_Dir')

# Remove the 'Renamed_Dir' directory tree
print("\nRemoving 'Renamed_Dir' directory tree")
shutil.rmtree('Renamed_Dir')
print("Current directory contents after removal:", os.listdir())

# Get the home directory
homeDir = os.path.expanduser("~")
print("\nHome directory:", homeDir)

# Display system information
print("\nUser and System information:")
print("Platform:", sys.platform)
print("Python version:", sys.version_info)

# Get the current user using os.getlogin() and getpass.getuser()
try:
    print("Current User (using os.getlogin()):", os.getlogin())
except OSError:
    print("Current User (using os.getlogin()): Not available in this environment")

# Fallback for getting the current user using getpass
print("Current User (using getpass.getuser()):", getpass.getuser())

# Get environment variables (platform-specific)
print("User from environment (USERNAME):", os.environ.get("USERNAME"))  # Works on Windows
print("Home directory (USERPROFILE):", os.environ.get("USERPROFILE"))  # Home directory on Windows
print("Language setting (LANG):", os.environ.get("LANG"))  # This works on Unix-based systems; may be empty on Windows

# Get the absolute path of the current script
file_path = os.path.abspath(__file__)
print("Current script path:", file_path)

# Split a file path into its components
print("\nSplitting file path:")
print("Directory:", os.path.dirname(file_path))
print("File Name:", os.path.basename(file_path))

d, f = os.path.split(file_path)
print("Directory:", d)
print("File Name:", f)

fn, x = os.path.splitext(f)
print("File Name without Extension:", fn)
print("Extension:", x)