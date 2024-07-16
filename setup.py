import os
import subprocess
import shutil

            

conan_profile_command = 'conan profile detect --name webgpu_engine'
conan_path_command = 'conan profile path webgpu_engine'
conan_install_command = 'conan install . --output-folder=build --build=missing --profile:host=webgpu_engine --profile:build=webgpu_engine'
meson_setup_command = 'meson setup --native-file conan_meson_native.ini .. meson-src'
meson_compile_command = 'meson compile -C meson-src'
meson_install_command = 'meson install --no-rebuild --only-changed'


def run_command(command, ignore_errors=False):
    """Run a shell command and ensure it's executed properly unless errors should be ignored."""
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        if ignore_errors:
            print(f"Ignored error while executing: {command}")
            print(e)
        else:
            print(f"An error occurred while executing: {command}")
            print(e)
            exit(1)
            

def print_build_step(text):
    """Print a build step message with a banner of dashes before and after, based on terminal width."""
    terminal_width, _ = shutil.get_terminal_size(fallback=(80, 20))  # Default width if terminal size can't be determined
    text_lines = text.split('\n')
    longest_line = max(text_lines, key=len)
    banner_length = min(len(longest_line) + 4, terminal_width)  # Add padding to the length of the longest line
    
    print("\n" + "-" * banner_length)
    for line in text_lines:
        centered_line = line.center(banner_length)
        print(centered_line)
    print("-" * banner_length + "\n")

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
                    return f"\"{full_path.strip()}\""

    return None

def run_vcvarsall(command):
    vcvarsall_bat = find_vcvarsall_bat()
    if vcvarsall_bat is None or vcvarsall_bat == "":
        print("No 'vcvarsall.bat' was found. Make sure you installed the VS C++ Development Toolkit. If you did try to set the path by your self inside of the 'setup.py'.")
        exit(1)
    print("Found 'vcvarsall.bat':\n" + vcvarsall_bat)
    run_command(vcvarsall_bat + " x64 && " + command)
        
    return True

def main():
    
    # Step 1: Detect and create a Conan profile named 'webgpu_engine'
    print_build_step("Running Conan profile detection...")
    run_command(conan_profile_command, True)

    print_build_step("Conan profile 'webgpu_engine' has been detected. You may need to edit the profile.\nYou can find the profile via:")
    run_command(conan_path_command, True)

    # Step 2: Install dependencies using Conan
    print_build_step("Installing dependencies with Conan...")
    run_command(conan_install_command)
    
    # Step 3: Run Meson setup
    os.chdir('build')
    print_build_step("Setting up the Meson build environment...")
    run_vcvarsall(meson_setup_command)
    
    # Step 4: Compile Meson
    print_build_step("Compiling with Meson...")
    run_vcvarsall(meson_compile_command)
    
    # Step 4: Install Meson
    os.chdir('meson-src')
    print_build_step("Installing with Meson...")
    run_vcvarsall(meson_install_command)
    
    print("Setup completed successfully.")

if __name__ == '__main__':
    main()
