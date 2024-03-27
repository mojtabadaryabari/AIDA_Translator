sources = ['src/config.c']

sources_logica = [
    'src/Logica/ClasseLDS_MainClass_C1.c',
    'src/Logica/ClasseLDS_SubClass_C2.c',
]

sources_viste = [
]

logic_Stazione_lib = static_library(
    'logic_Stazione',
    sources + sources_logica + sources_viste,
    include_directories: ['include'],
    dependencies: [common_dep, logic_utils_dep, logic_dep, plant_type_dep],
    c_args: '-DSIMULENV',
)
