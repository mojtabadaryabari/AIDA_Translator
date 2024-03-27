sources = ['src/config.c']

sources_logica = [
    'src/Logica/ClasseMainClass_C1.c',
    'src/Logica/ClasseSubClass_C2.c',
    'src/Logica/ClasseSubClass_C3.c',
]

sources_viste = [
]

logic_Stazione_lib = static_library(
    'logic_Stazione',
    sources + sources_logica + sources_viste,
    include_directories: ['include'],
    dependencies: [common_dep, logic_utils_dep],
    c_args: '-DSIMULENV',
)