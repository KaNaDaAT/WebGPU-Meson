fs = import('fs')

src = [
	'main.cpp',
	'sdl2webgpu.h',
	'sdl2webgpu.c',
]

sdl2_dep = dependency('sdl2')
sdl2_main_dep = dependency('sdl-sdl2main')

executable(
	meson.project_name(),
	sources: src,
	dependencies: [sdl2_dep, sdl2_main_dep, webgpu_dll],
	install : true, 
	install_dir: install_out,
	include_directories: project_includes
)

fs.copyfile(join_paths(webgpu_path, 'wgpu_native.dll'), install: true, install_dir: install_out )