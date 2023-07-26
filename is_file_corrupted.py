#Function to find if a file is malicious or corrupted
def isFileCorrupted(file_path, expected_signature):
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
    

if __name__ == "__main__":
    file_path = r"C:\Users\USER\Desktop\nonerror\comp.jpg"         # Kindly substitute it with the file path you want to scan
    expected_signature = b"GIF89a" 
    isFileCorrupted(file_path, expected_signature)
    if isFileCorrupted(file_path, expected_signature):
        print("File is not corrupted.")
    else:
        print("File may be corrupted.")
        