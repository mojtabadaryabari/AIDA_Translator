RFILibs_incs = [
  common_incs,
  logic_utils_incs,
]

subdirs = [
	'FeasibilityClasses/Stazione',
]


foreach subdir: subdirs
    subdir(subdir)
endforeach

sys_libs = []
sys_libs += gcov_lib


dep = declare_dependency(
    link_whole: [
                 logic_Stazione_feas_lib,
                ]
)

LibFeas_ifc_files = files('FeasibilityIfc/src/cmdFeasibilityIfc.c',)

LibFeas_ifc_incs = include_directories(
  'FeasibilityIfc/include', 
  'FeasibilityClasses',
)

LibFeas_inc_dirs = [LibFeas_ifc_incs,
			RFILibs_incs,
			Stazione_feas_ifc_incs,
		   ]

static_library('feasibility', LibFeas_ifc_files,
        include_directories: LibFeas_inc_dirs,
        c_args: ['-DSIMULENV=1'],
       )

