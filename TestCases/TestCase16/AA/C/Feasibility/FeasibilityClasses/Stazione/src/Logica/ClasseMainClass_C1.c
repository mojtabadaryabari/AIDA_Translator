
#include "Logica/ClasseMainClass_C1_priv.h"
#include "config.h"
#include "PlatformMacros.h"

int L_P1_C1_cmd_tmp_id = -1; 

// ********** Dichiarazione guardie **********


// ********** Dichiarazione comandi manuali **********



// ********** Definizione guardie **********


// ********** Definizione macro **********

// Macro di verifica


// Macro valorizzate



//FEASIBILIT
int L_P1_C1_getFeasibility(instance_id_t const my_id, int cmd_id)
{
L_P1_C1_cmd_tmp_id = cmd_id;
int ret = 1;

switch (L_P1_C1_GetState(my_id)) {
	case C1_St_state:
		switch (cmd_id){
			default:
			break;
		}
	break;

    default:
        break;  // Needed for MISRA C syntactic compliance
    } // switch sugli stati chiuso
    
    return ret;
}

// comandi manuali

// risposte ai comandi manuali


