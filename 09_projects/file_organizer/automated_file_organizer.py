import os
import shutil

def organize_directory(path):
    
    for file in os.listdir(path):
        if os.path.isdir(os.path.join(path, file)):
            continue
        
        filename, file_extension = os.path.splitext(file)
        directory = file_extension[1:].upper()
        
        if not directory:
            directory = "Others"
        
        new_dir_path = os.path.join(path, directory)
        os.makedirs(new_dir_path, exist_ok=True)
        
        shutil.move(src=os.path.join(path, file), dst=os.path.join(new_dir_path, file))
        print(f"Moved {file} --> {new_dir_path}")
        
def main():
    r""" When you prefix a string with r, Python treats it as a "raw string" - it doesn't interpret backslashes (\) as escape characters.
    Without r (regular string): Python sees \U and tries to interpret it as a Unicode escape sequence, causing a SyntaxError.
    """
    organize_directory(r"C:\Users\sanjeekumar\Documents\Test")
    
if __name__ == "__main__":
    main()