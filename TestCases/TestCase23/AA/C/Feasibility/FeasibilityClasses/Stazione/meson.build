sources = ['src/config.c']

sources_logica = [
    'src/Logica/ClasseMainClass_C1.c',
    'src/Logica/ClasseSubClass_C2.c',
]
sources_viste = [
]

Stazione_feas_ifc_incs = include_directories(
  'include',
   'include/Logica', 
)

logic_Stazione_feas_lib = static_library(
    'logic_Stazione_feas',
    sources + sources_logica + sources_viste,
    include_directories: [Stazione_feas_ifc_incs],
    dependencies: [common_dep, logic_utils_dep],
    c_args: '-DSIMULENV',
)