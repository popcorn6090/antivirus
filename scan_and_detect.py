import os

#A product of what we have learned so far to create our very first antivirus

def is_file_corrupted(file_path, expected_signature):
    try:
        with open(file_path, 'rb') as file:
            actual_signature = file.read(len(expected_signature))
            return actual_signature == expected_signature
           
        
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return False
    except Exception as e:
        print(f"An error occurred while checking {file_path}: {e}")
        return False

def scan_files(directory, expected_signature):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            print(file_path)
            is_file_corrupted(file_path, expected_signature)
            if is_file_corrupted(file_path, expected_signature):
              print("File is not corrupted.")
            else:
              print("File may be corrupted.")
            

if __name__ == "__main__":
    target_directory = r"C:\dev"        # Replace with the directory you want to scan.
    expected_signature = b"GIF89a" 
    scan_files(target_directory, expected_signature)
    