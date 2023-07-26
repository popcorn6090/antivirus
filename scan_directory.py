import os

#function to scan a directory

def scan_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            print(file_path)
            
            
            
if __name__ == "__main__":
    target_directory = r"C:\bin"            # You have to replace the "C:\bin" with the directory you want to scan. 
    scan_files(target_directory)
                
            
            
            
            
            
            