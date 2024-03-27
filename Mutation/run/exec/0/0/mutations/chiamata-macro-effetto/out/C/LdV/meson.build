plant_type_dep = declare_dependency(
  include_directories: '.'  # this is for LogicInterface.h and other includes in plant type
  )

subdirs = [
'Stazione',
]
foreach subdir: subdirs
    subdir(subdir)
endforeach

sys_libs = []
sys_libs += gcov_lib

dep = declare_dependency(
    link_whole: [
                 logic_Stazione_lib,
                ]
)


ldv_stlib = static_library(
    'ldv',
    ['LogicInterface.c', transcoder],
    c_args: ['-DSIMULENV'],
    dependencies: [dep, common_dep, sys_libs, logic_utils_dep, logic_dep],
)
