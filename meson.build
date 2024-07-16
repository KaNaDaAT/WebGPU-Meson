project(
  'webgpu_example',
  ['cpp', 'c'],
  version: '0.1',
  default_options: [
    'cpp_std=c++20',
    'optimization=3',
	'buildtype=release',
	'warning_level=3'
  ]
)

base_include = include_directories(
	'lib/webgpu/include'
)

project_includes = [base_include]


# -------------------- Options -----------------------

buildtype = get_option('buildtype')
arch = get_option('arch')
hostsystem = get_option('hostsystem')

if arch == ''
	arch = host_machine.cpu()
	if arch == 'amd64'
		arch = 'x86_64'
	endif
endif
if hostsystem == ''
	sys = host_machine.system()
endif

# ---------------------------------------------------

# -------------------- WEB GPU ----------------------

if hostsystem == 'windows'
	webgpu_architecture = 'windows-' + arch
elif hostsystem == 'linux'
	webgpu_architecture = 'linux-' + arch
elif hostsystem == 'darwin'
	webgpu_architecture = 'macos-' + arch
elif hostsystem == 'macos'
	webgpu_architecture = 'macos-' + arch
else
	error('Platform ' + hostsystem + ' not supported by this release of WebGPU.')
endif

webgpu_path = join_paths(meson.global_source_root(), 'lib','webgpu', 'bin', webgpu_architecture)
project_includes += include_directories(join_paths('lib','webgpu', 'bin', webgpu_architecture)) 

message('Searching for wgpu_native.dll in ' + webgpu_path)
cc = meson.get_compiler('cpp')
webgpu_dll = cc.find_library('wgpu_native.dll', dirs: [webgpu_path])


# ---------------------------------------------------

install_out = join_paths(meson.global_source_root(), 'out', hostsystem, buildtype)
subdir('src')