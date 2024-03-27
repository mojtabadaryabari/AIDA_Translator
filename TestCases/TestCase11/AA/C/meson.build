project('logic', ['c'], default_options: [])

pyexe = find_program('python3', 'python', required: true)

system_dir = get_option('system-dir')
logic_utils_dir = get_option('logic-utils-dir')

cur_dir = meson.current_source_dir()
common_dir = system_dir / 'Common'

with_feasibility = get_option('with-feasibility')

common_build_dir = cur_dir / common_dir / 'build'
logic_utils_build_dir = cur_dir / logic_utils_dir / 'build'

subdirs = ['LdS', 'LdV']
if with_feasibility
  subdirs += ['Feasibility']
endif

cc = meson.get_compiler('c')
gcov_lib = []

transcoder = custom_target(
  'transcoder',
  input: ['attributes.csv', 'enumeratives.csv',
          logic_utils_dir / 'src' / 'transcoding_cfg.c.jinja',],
  output: 'transcoding_cfg.c',
  command: [pyexe, cur_dir / logic_utils_dir / 'scripts/gen_transcoding.py',
            '@INPUT@',
            '-o', '@OUTPUT@'],
  )

logic_utils_incs = include_directories(logic_utils_dir / 'include')
logic_utils_lib = cc.find_library('logicutils',
                                  dirs: [logic_utils_build_dir])
logic_utils_dep = declare_dependency(
  dependencies: [logic_utils_lib],
  include_directories: logic_utils_incs,
  )

if cc.get_id() == 'gcc' and get_option('coverage-enabled')
    message('Coverage enabled')
    gcov_lib = cc.find_library('gcov')
    add_global_arguments(['-fprofile-arcs', '-ftest-coverage'], language : 'c')
endif

common_incs = include_directories(common_dir / 'Platform/include',
                                  common_dir / 'AGGM/include',
                                  common_dir / 'Mst/include',
                                 )

common_stlibs = [cc.find_library(
  'Common',
  dirs: [common_build_dir]
)]
common_dep = declare_dependency(
  dependencies: common_stlibs,
  include_directories: common_incs,
  )

foreach subdir: subdirs
    subdir(subdir)
endforeach
