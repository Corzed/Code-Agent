import os
import subprocess
from typing import Optional, List, Union, Dict
from orchestrai import AgentTool

def read_file(path: str) -> str:
    """Read the contents of a file."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {str(e)}"

def list_files(directory: str = ".") -> List[str]:
    """List all files in a directory."""
    try:
        items = os.listdir(directory)
        result = []
        for item in items:
            full_path = os.path.join(directory, item)
            item_type = "📁" if os.path.isdir(full_path) else "📄"
            result.append(f"{item_type} {item}")
        return result
    except Exception as e:
        return [f"Error listing directory: {str(e)}"]

def write_file(path: str, content: str, mode: str = "w") -> str:
    """Write content to a file. Mode can be 'w' for overwrite or 'a' for append."""
    try:
        with open(path, mode, encoding='utf-8') as f:
            f.write(content)
        return f"Successfully wrote to {path}"
    except Exception as e:
        return f"Error writing file: {str(e)}"

def edit_file_segment(path: str, content: str, start_line: int, end_line: Optional[int] = None) -> str:
    """Edit a specific segment of a file."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Convert to 0-based indexing
        start_line -= 1
        if end_line is not None:
            end_line -= 1
        
        # Handle insertion or replacement
        new_lines = content.split('\n')
        if end_line is None:
            # Insert at position
            lines[start_line:start_line] = [line + '\n' for line in new_lines]
        else:
            # Replace segment
            lines[start_line:end_line + 1] = [line + '\n' for line in new_lines]
        
        # Write back to file
        with open(path, 'w', encoding='utf-8') as f:
            f.writelines(lines)
        
        return f"Successfully edited {path}"
    except Exception as e:
        return f"Error editing file: {str(e)}"

def create_file(path: str, content: str = "") -> str:
    """Create a new file or folder."""
    try:
        if path.endswith('/') or '.' not in os.path.basename(path):
            os.makedirs(path, exist_ok=True)
            return f"Created directory: {path}"
        else:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            return f"Created file: {path}"
    except Exception as e:
        return f"Error creating file/directory: {str(e)}"

def rename_file(old_path: str, new_path: str) -> str:
    """Rename a file or folder."""
    try:
        os.rename(old_path, new_path)
        return f"Renamed {old_path} to {new_path}"
    except Exception as e:
        return f"Error renaming: {str(e)}"

def delete_file(path: str) -> str:
    """Delete a file or folder."""
    try:
        if os.path.isdir(path):
            os.rmdir(path)  # This will only delete empty directories
            return f"Deleted directory: {path}"
        else:
            os.remove(path)
            return f"Deleted file: {path}"
    except Exception as e:
        return f"Error deleting: {str(e)}"

def execute_command(command: str) -> Dict[str, str]:
    """Execute a terminal command and return its output."""
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True
        )
        return {
            "stdout": result.stdout,
            "stderr": result.stderr,
            "return_code": str(result.returncode)
        }
    except Exception as e:
        return {
            "stdout": "",
            "stderr": str(e),
            "return_code": "-1"
        }

# Create AgentTools with detailed descriptions
FILE_TOOLS = {
    "read_file": AgentTool(
        name="read_file",
        description="""Read and return the contents of a file.
Arguments:
- path (str): The path to the file to read
Returns: The contents of the file as a string""",
        func=read_file
    ),
    
    "list_files": AgentTool(
        name="list_files",
        description="""List all files and directories in a specified directory.
Arguments:
- directory (str, optional): The directory path to list (defaults to current directory ".")
Returns: List of strings, each representing a file/directory with an emoji prefix (📁 for directories, 📄 for files)""",
        func=list_files
    ),
    
    "write_file": AgentTool(
        name="write_file",
        description="""Write or append content to a file.
Arguments:
- path (str): The path to the file to write to
- content (str): The content to write to the file
- mode (str, optional): Write mode - 'w' to overwrite file (default), 'a' to append
Returns: Success message or error message""",
        func=write_file
    ),
    
    "edit_file_segment": AgentTool(
        name="edit_file_segment",
        description="""Edit a specific segment of a file by line numbers.
Arguments:
- path (str): The path to the file to edit
- content (str): The new content to insert or replace
- start_line (int): The line number where to start the edit (1-based indexing)
- end_line (int, optional): The line number where to end the replacement (if not provided, content is inserted at start_line)
Returns: Success message or error message""",
        func=edit_file_segment
    ),
    
    "create_file": AgentTool(
        name="create_file",
        description="""Create a new file or directory.
Arguments:
- path (str): The path for the new file/directory (use trailing slash or no extension for directories)
- content (str, optional): Initial content for the file (ignored for directories)
Returns: Success message or error message""",
        func=create_file
    ),
    
    "rename_file": AgentTool(
        name="rename_file",
        description="""Rename a file or directory.
Arguments:
- old_path (str): The current path of the file/directory
- new_path (str): The new path/name for the file/directory
Returns: Success message or error message""",
        func=rename_file
    ),
    
    "delete_file": AgentTool(
        name="delete_file",
        description="""Delete a file or empty directory.
Arguments:
- path (str): The path to the file/directory to delete
Returns: Success message or error message
Note: For directories, only empty directories can be deleted""",
        func=delete_file
    ),
    
    "execute_command": AgentTool(
        name="execute_command",
        description="""Execute a terminal command and capture its output.
Arguments:
- command (str): The terminal command to execute
Returns: Dictionary containing:
- stdout (str): Standard output from the command
- stderr (str): Standard error output from the command
- return_code (str): Command's exit code (0 typically means success)""",
        func=execute_command
    )
}