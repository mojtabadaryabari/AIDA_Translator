#include "cmdFeasibilityIfc.h"

#include "Stazione/include/Logica/ClasseMainClass_C1.h"
#include "Stazione/include/Logica/ClasseSubClass_C2.h"
#include "Stazione/include/Logica/ClasseSubClass_C3.h"

static int isAttach = 1;

int commandFeasibility(int station_id, int class_id, instance_id_t const my_id, int cmd_id)
{
	int out = 1;
	
	switch(class_id)
	{
		case 1:
			out = L_P1_C1_getFeasibility((instance_id_t)my_id,
										(int)cmd_id);
		break;
		case 2:
			out = L_P1_C2_getFeasibility((instance_id_t)my_id,
										(int)cmd_id);
		break;
		case 3:
			out = L_P1_C3_getFeasibility((instance_id_t)my_id,
										(int)cmd_id);
		break;

		default:
		break;

	}

	return out;
}
extern void StazioneConfAndDataAttach();

int attachCofigurationDS()
{
	if(1 == isAttach){
		StazioneConfAndDataAttach();
		isAttach = 0;
	}
	return isAttach;
}

