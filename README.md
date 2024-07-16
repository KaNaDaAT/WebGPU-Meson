# WebGPU Build Setup with Meson and Conda

This repository serves as a simple test environment demonstrating how to set up a build system for WebGPU projects using Meson and Conda. The provided setup includes all necessary configuration files and scripts to get you started with building WebGPU applications efficiently.

## Features

- **WebGPU Integration**: Demonstrates the basic setup required to develop WebGPU applications.
- **Meson Build System**: Utilizes the Meson build system for its simplicity and speed, ensuring a seamless build process.
- **Conda Environment**: Leverages Conda for managing dependencies and creating a consistent development environment.

## Getting Started

### Prerequisites

Ensure you have the following installed on your system:

- [Conan2](https://docs.conan.io/2/reference/commands/install.html)
- [Meson](https://mesonbuild.com/SimpleStart.html)
- [Ninja](https://ninja-build.org/) (optional, but recommended for building)

You may use `pip install -r requirements.txt`. It will install the versions used while development. Other versions may work as well.

### Setup

1. **Clone the repository**:

2. **Install the Prerequisites**
    ```sh
    pip install -r requirements.txt
    ```

3. **Run setup.py**:
    ```sh
    python setup.py
    ```

> [!IMPORTANT]  
> The Conan profile will be automatically detected during `setup.py`. However, it will most likely neet to be reconfigured as for now, on Windows, not all compilers work. See [Chapter Known Issues](#known-issues). 
>
> You can use `conan profile detect --name webgpu_engine` to manually create the profile and `conan profile path webgpu_engine` to find the file's location in order to edit it (The path will be written during the `setup.py`). The used Conan configuration is:
>
> ```conan
> [settings]
> arch=x86_64
> build_type=Debug
> compiler=msvc
> compiler.cppstd=20
> compiler.runtime=dynamic
> compiler.version=193
> os=Windows
> ```


## Notes

The setup for the project is optimized for windows and VSC. It does not yet work for other platforms.

The project does not yet support **emscripten**. 

## Plans

- Support for debug and release configurations via parameters.
- Support for emscripten via parameters.
- Web Example
- setting up conan profiles in relative path
- Supporting easy debug functionality

  
## Known Issues

### Compiling on Windows with MinGW

Challenges arose when attempting to compile using MinGW due to issues with libraries like `libiconv` [Conan Center Index Issue #506](https://github.com/conan-io/conan-center-index/issues/506).

### Compiling on Windows with GCC

Compiling on Windows using GCC, particularly with Mingw, presents challenges due to compatibility issues and specific compiler quirks. Issues such as [Conan Issue #2760](https://github.com/conan-io/conan/issues/2760) highlight difficulties in ensuring correct library linking and toolchain configuration, which are crucial for successful compilation.

### Issues with Clang as well as gcc and SDL2

Compiling with Clang encountered errors related to SDL2, specifically concerning invalid use of undefined types [LLVM Project Issue #44502](https://github.com/llvm/llvm-project/issues/44502).
