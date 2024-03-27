
#include "Logica/ClasseMainClass_C1_priv.h"
#include "config.h"
#include "PlatformMacros.h"

int L_P1_C1_cmd_tmp_id = -1; 

// ********** Dichiarazione guardie **********

static bool L_P1__guard1(instance_id_t const my_id);

// ********** Dichiarazione comandi manuali **********
static bool L_P1__GetInEvent1(instance_id_t const my_id) ;
static bool L_P1__GetInEvent2(instance_id_t const my_id) ;
static bool L_P1__GetInEvent3(instance_id_t const my_id) ;
static bool L_P1__GetInEvent4(instance_id_t const my_id) ;

static void L_P1__SetOutEvent5(
	instance_id_t const my_id, 
	ManCmdResponse const value);

static void L_P1__SetOutEvent6(
	instance_id_t const my_id, 
	ManCmdResponse const value);

static void L_P1__SetOutEvent7(
	instance_id_t const my_id, 
	ManCmdResponse const value);

static void L_P1__SetOutEvent8(
	instance_id_t const my_id, 
	ManCmdResponse const value);



// ********** Definizione guardie **********

static bool L_P1__guard1(instance_id_t const my_id)
{
    bool res_AndLogicOP_0 = true;
    
    //  comando manuale   MainClass_C1_command_comm8 da  Sender1a75134
    res_AndLogicOP_0 = (res_AndLogicOP_0 && L_P1__GetInEvent4(my_id));
    
    //  *76,*
    //   *69,* *34,*  se il parametro MainClass_C1_parametro_P9 non è  uguale a  *53,* 1 *37,* o  se la variabile MainClass_C1_variabile_V4 non è  uguale a  *53,* 3 *38,* o  se il contatore MainClass_C1_contatore_Co8 è  maggiore di  *54,* 12 *34,* e  se il parametro MainClass_C1_parametro_P3 non è  maggiore di  *54,* 2, Solo una delle seguenti { 
    //   *38,*  se il contatore MainClass_C1_contatore_Co8 è  uguale a  *53,* 15315 e  se il controllo ConsDef  è  uguale a FALSE  *34,* o  se il parametro MainClass_C1_parametro_P3 è  minore di  *55,* 10 *35,* e  se il controllo MainClass_C1_controllo_C3 non è  uguale a RossoGiallo *37,* e  se la variabile MainClass_C1_variabile_V9 non è  maggiore di  *54,* 6, Verifica che   *49,*  *,*  il timer MainClass_C1_timer_T9 non sia attivo
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetParamMainc9(my_id) == 1u));
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_NotLogicOP_4);
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetMainc33(my_id) == 3u));
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_NotLogicOP_5);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    bool res_AndLogicOP_6 = true;
    res_AndLogicOP_6 = (res_AndLogicOP_6 && (Counter_GetValore(L_P1__GetMainc44(my_id)) > 12u));
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetParamMainc7(my_id) > 2u));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_7);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_6);
    
    if(res_OrLogicOP_2){
    bool res_ImpliesLogicOp_8 = true;
    bool res_OrLogicOP_9 = false;
    bool res_AndLogicOP_10 = true;
    res_AndLogicOP_10 = (res_AndLogicOP_10 && (Counter_GetValore(L_P1__GetMainc44(my_id)) == 15315u));
    res_AndLogicOP_10 = (res_AndLogicOP_10 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_AndLogicOP_10);
    bool res_AndLogicOP_11 = true;
    bool res_AndLogicOP_12 = true;
    res_AndLogicOP_12 = (res_AndLogicOP_12 && (L_P1__GetParamMainc7(my_id) < 10u));
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (L_P1__GetInMainc4(my_id) == rossogiallo));
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_NotLogicOP_13);
    
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_AndLogicOP_12);
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1__GetMainc34(my_id) > 6u));
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_NotLogicOP_14);
    
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_AndLogicOP_11);
    
    if(res_OrLogicOP_9){
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! Timer_Attivo(L_P1__GetMainc43(my_id)));
    res_ImpliesLogicOp_8 = (res_ImpliesLogicOp_8 && res_NotLogicOP_15);
    }
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_ImpliesLogicOp_8);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *50,*  *,*  la variabile MainClass_C1_variabile_V9 sia  uguale a  *53,* 2
    res_AndLogicOP_0 = (res_AndLogicOP_0 && (L_P1__GetMainc34(my_id) == 2u));
    
    if(res_AndLogicOP_0){
    L_P1__SetOutEvent8(my_id,LDS_MANCMD_PROCESSED);
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
			default:
			break;
		}
	break;
	case C1_St_state:
		switch (cmd_id){
			case 52:
				if(L_P1__guard1(my_id)){
			    	ret = 0;
			    }
		        else { ret = 1; }
		    break;
			default:
			break;
		}
	break;
	case C1_St_state5:
		switch (cmd_id){
			default:
			break;
		}
	break;
	case C1_St_state4:
		switch (cmd_id){
			default:
			break;
		}
	break;
	case C1_St_state3:
		switch (cmd_id){
			default:
			break;
		}
	break;
	case C1_St_state2:
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
static bool L_P1__GetInEvent2(instance_id_t const my_id) 
{
    UNUSED(my_id);
    if(L_P1__event2_ID==L_P1_C1_cmd_tmp_id){
		return true;
	}	
	else{
		return false;
	}
}
static bool L_P1__GetInEvent3(instance_id_t const my_id) 
{
    UNUSED(my_id);
    if(L_P1__event3_ID==L_P1_C1_cmd_tmp_id){
		return true;
	}	
	else{
		return false;
	}
}
static bool L_P1__GetInEvent4(instance_id_t const my_id) 
{
    UNUSED(my_id);
    if(L_P1__event4_ID==L_P1_C1_cmd_tmp_id){
		return true;
	}	
	else{
		return false;
	}
}

// risposte ai comandi manuali
static void L_P1__SetOutEvent5(
	instance_id_t const my_id, 
	ManCmdResponse const value) 
{
    UNUSED(my_id);
    UNUSED(value);
}

static void L_P1__SetOutEvent6(
	instance_id_t const my_id, 
	ManCmdResponse const value) 
{
    UNUSED(my_id);
    UNUSED(value);
}

static void L_P1__SetOutEvent7(
	instance_id_t const my_id, 
	ManCmdResponse const value) 
{
    UNUSED(my_id);
    UNUSED(value);
}

static void L_P1__SetOutEvent8(
	instance_id_t const my_id, 
	ManCmdResponse const value) 
{
    UNUSED(my_id);
    UNUSED(value);
}



