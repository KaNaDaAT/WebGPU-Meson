import os

# Function to find vcvarsall.bat on all drives
def find_vcvarsall_bat():
    typical_paths = [
        r"Microsoft Visual Studio\2019\Community\VC\Auxiliary\Build\vcvarsall.bat",
        r"Microsoft Visual Studio\2019\Professional\VC\Auxiliary\Build\vcvarsall.bat",
        r"Microsoft Visual Studio\2019\Enterprise\VC\Auxiliary\Build\vcvarsall.bat",
        r"Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvarsall.bat",
        r"Microsoft Visual Studio\2022\Professional\VC\Auxiliary\Build\vcvarsall.bat",
        r"Microsoft Visual Studio\2022\Enterprise\VC\Auxiliary\Build\vcvarsall.bat"
    ]
    directories = ["\\Program Files", "\\Program Files (x86)"]

    drives = ["C:", "D:", "E:", "F:", "G:", "H:", "I:", "J:", "K:", "L:", "M:", "N:", "O:", "P:", "Q:", "R:", "S:", "T:", "U:", "V:", "W:", "X:", "Y:", "Z:"]

    
    for drive in drives:
        for directory in directories:
            for path in typical_paths:
                full_path = os.path.join(drive, directory, path)
                if os.path.exists(full_path):
                    return full_path

    return None

# Example usage:
vcvarsall_bat_path = find_vcvarsall_bat()

if vcvarsall_bat_path:
    print(f"\"{vcvarsall_bat_path}\"")
else:
    print("vcvarsall.bat not found.")
