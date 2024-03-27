
#include "Logica/ClasseMainClass_C1_priv.h"
#include "Logica/ClasseSubClass_C2_priv.h"
#include "config.h"
#include "PlatformMacros.h"

int L_P1_C1_cmd_tmp_id = -1; 

// ********** Dichiarazione guardie **********

static bool L_P1__guard10(instance_id_t const my_id);
static bool L_P1__guard12(instance_id_t const my_id);

// ********** Dichiarazione comandi manuali **********
static bool L_P1__GetInEvent(instance_id_t const my_id) ;
static bool L_P1__GetInEvent1(instance_id_t const my_id) ;

static void L_P1__SetOutEvent3(
	instance_id_t const my_id, 
	ManCmdResponse const value);

static void L_P1__SetOutEvent4(
	instance_id_t const my_id, 
	ManCmdResponse const value);



// ********** Definizione guardie **********

static bool L_P1__guard10(instance_id_t const my_id)
{
    bool res_AndLogicOP_0 = true;
    
    //  *86,*  Almeno una delle seguenti {
    //   *82,*  Ricezione del comando manuale   MainClass_C1_command_comm5   *75,*
    //   *83,*  Tutte le seguenti {
    //   Ricezione del  comando manuale   MainClass_C1_command_comm5   *75,*
    //   *34,*  se il parametro MainClass_C1_parametro_P8 non è  uguale a RossoGialloVerde, Verifica che   *50,*  *,*  la variabile MainClass_C1_variabile_V5 sia  diverso da c270x
    //  }
    //  }
    bool res_OrLogicOP_1 = false;
    res_OrLogicOP_1 = (res_OrLogicOP_1 || L_P1__GetInEvent1(my_id));
    bool res_AndLogicOP_2 = true;
    res_AndLogicOP_2 = (res_AndLogicOP_2 && L_P1__GetInEvent1(my_id));
    bool res_ImpliesLogicOp_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetParamMainc11(my_id) == rossogiallo));
    if(res_NotLogicOP_4){
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetMainc34(my_id) == c270x));
    res_ImpliesLogicOp_3 = (res_ImpliesLogicOp_3 && res_NotLogicOP_5);
    }
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_ImpliesLogicOp_3);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_2);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_1);
    
    if(res_OrLogicOP_1){
    L_P1__SetOutEvent4(my_id,LDS_MANCMD_PROCESSED);
    }
    else{
    
    }
    
    
    return res_AndLogicOP_0;
}

static bool L_P1__guard12(instance_id_t const my_id)
{
    bool res_AndLogicOP_0 = true;
    
    //  comando manuale   MainClass_C1_command_comm5
    res_AndLogicOP_0 = (res_AndLogicOP_0 && L_P1__GetInEvent1(my_id));
    
    if(res_AndLogicOP_0){
    L_P1__SetOutEvent4(my_id,LDS_MANCMD_PROCESSED);
    }
    else{
    
    }
    
    
    return res_AndLogicOP_0;
}


// ********** Definizione macro **********

// Macro di verifica


// Macro valorizzate



//FEASIBILIT
int L_P1_C1_getFeasibility(instance_id_t const my_id, int cmd_id)
{
L_P1_C1_cmd_tmp_id = cmd_id;
int ret = 1;

switch (L_P1_C1_GetState(my_id)) {
	case C1_St_state1:
		switch (cmd_id){
			case 53:
				if(L_P1__guard12(my_id)){
			    	ret = 0;
			    }

				else if(L_P1__guard10(my_id)){
			    	ret = 0;
			    }
		        else { ret = 1; }
		    break;
			default:
			break;
		}
	break;
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
static bool L_P1__GetInEvent(instance_id_t const my_id) 
{
    UNUSED(my_id);
    if(L_P1__event_ID==L_P1_C1_cmd_tmp_id){
		return true;
	}	
	else{
		return false;
	}
}
static bool L_P1__GetInEvent1(instance_id_t const my_id) 
{
    UNUSED(my_id);
    if(L_P1__event1_ID==L_P1_C1_cmd_tmp_id){
		return true;
	}	
	else{
		return false;
	}
}

// risposte ai comandi manuali
static void L_P1__SetOutEvent3(
	instance_id_t const my_id, 
	ManCmdResponse const value) 
{
    UNUSED(my_id);
    UNUSED(value);
}

static void L_P1__SetOutEvent4(
	instance_id_t const my_id, 
	ManCmdResponse const value) 
{
    UNUSED(my_id);
    UNUSED(value);
}



