# directory_operations.py

import os       # Provides methods for working with the file system.
import glob     # Provides a list of files and directories using wildcards.
import sys      # Provides access to system-specific parameters and functions.
import shutil   # Provides methods for file and directory operations.
import getpass  # Provides a way to get the current user's username.

def get_current_directory():
    """Get and display the current directory."""
    thisDir = os.getcwd()
    print("\nCurrent directory:", thisDir)
    return thisDir

def get_parent_directory(current_directory):
    """Get and display the parent directory."""
    parentDir = os.path.dirname(current_directory)
    print("Parent directory:", parentDir)
    return parentDir

def list_directory_contents(directory):
    """List and display files and directories in the given directory."""
    print("\nListing files and directories:")
    files_and_dirs = os.listdir(directory)  
    for item in files_and_dirs:
        print(item)
    return files_and_dirs

def sort_and_display_contents(contents):
    """Sort and display the list of files and directories."""
    contents.sort()
    print("\nSorted list of files and directories:")
    print(contents)

def search_files_starting_with(prefix):
    """Search and display files starting with a given prefix."""
    print(f"\nFiles and directories starting with '{prefix}':")
    matching_files = glob.glob(f"{prefix}*")
    print(matching_files)

def move_up_one_directory():
    """Move up one directory."""
    os.chdir('..')
    print("\nReturned to the parent directory:", os.getcwd())

def navigate_to_directory(directory_name):
    """Navigate to a given directory if it exists."""
    if os.path.isdir(directory_name):
        os.chdir(directory_name)
        print(f"\nNavigated to '{directory_name}' directory.")
    else:
        print(f"\nDirectory '{directory_name}' does not exist.")

def create_directory(directory_name):
    """Create a new directory with the specified name."""
    print(f"\nCreating '{directory_name}'")
    os.makedirs(directory_name, exist_ok=True)

def rename_directory(old_name, new_name):
    """Rename an existing directory."""
    print(f"\nRenaming '{old_name}' to '{new_name}'")
    os.rename(old_name, new_name)

def remove_directory(directory_name):
    """Remove the specified directory."""
    print(f"\nRemoving '{directory_name}' directory tree")
    shutil.rmtree(directory_name)
    print("Directory removed.")

def get_home_directory():
    """Get and display the user's home directory."""
    homeDir = os.path.expanduser("~")
    print("\nHome directory:", homeDir)
    return homeDir

def display_system_information():
    """Display platform and Python version information."""
    print("\nUser and System information:")
    print("Platform:", sys.platform)
    print("Python version:", sys.version_info)

def get_current_user():
    """Get the current user using os.getlogin() and getpass.getuser()."""
    try:
        print("Current User (using os.getlogin()):", os.getlogin())
    except OSError:
        print("Current User (using os.getlogin()): Not available in this environment")
    print("Current User (using getpass.getuser()):", getpass.getuser())

def get_environment_variables():
    """Display common environment variables."""
    print("User from environment (USERNAME):", os.environ.get("USERNAME"))  # Works on Windows
    print("Home directory (USERPROFILE):", os.environ.get("USERPROFILE"))  # Home directory on Windows
    print("Language setting (LANG):", os.environ.get("LANG"))  # Works on Unix-based systems; may be empty on Windows

def get_current_script_path():
    """Get and display the absolute path of the current script."""
    file_path = os.path.abspath(__file__)
    print("Current script path:", file_path)
    return file_path

def split_file_path(file_path):
    """Split the file path into directory and file name."""
    print("\nSplitting file path:")
    print("Directory:", os.path.dirname(file_path))
    print("File Name:", os.path.basename(file_path))

    directory, file_name = os.path.split(file_path)
    print("Directory:", directory)
    print("File Name:", file_name)

    file_name_without_ext, ext = os.path.splitext(file_name)
    print("File Name without Extension:", file_name_without_ext)
    print("Extension:", ext)

if __name__ == "__main__":
    # Execute the modular functions

    current_dir = get_current_directory()
    parent_dir = get_parent_directory(current_dir)
    
    contents = list_directory_contents(current_dir)
    sort_and_display_contents(contents)
    
    search_files_starting_with('f')
    
    move_up_one_directory()
    navigate_to_directory('Teach_Yourself_Visually_Python')
    
    create_directory('New_Dir')
    rename_directory('New_Dir', 'Renamed_Dir')
    remove_directory('Renamed_Dir')
    
    get_home_directory()
    
    display_system_information()
    get_current_user()
    get_environment_variables()
    
    script_path = get_current_script_path()
    split_file_path(script_path)
