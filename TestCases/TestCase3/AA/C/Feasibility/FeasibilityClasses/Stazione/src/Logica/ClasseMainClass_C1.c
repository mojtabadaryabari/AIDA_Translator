
#include "Logica/ClasseMainClass_C1_priv.h"
#include "config.h"
#include "PlatformMacros.h"

int L_P1_C1_cmd_tmp_id = -1; 

// ********** Dichiarazione guardie **********

static bool L_P1__guard1(instance_id_t const my_id);

// ********** Dichiarazione comandi manuali **********
static bool L_P1__GetInEvent(instance_id_t const my_id) ;

static void L_P1__SetOutEvent3(
	instance_id_t const my_id, 
	ManCmdResponse const value);



// ********** Definizione guardie **********

static bool L_P1__guard1(instance_id_t const my_id)
{
    bool res_AndLogicOP_0 = true;
    
    //  comando manuale   MainClass_C1_command_comm10 da  Senderac49796
    res_AndLogicOP_0 = (res_AndLogicOP_0 && L_P1__GetInEvent(my_id));
    
    //  *76,*
    //   *67,* *37,*  se la variabile MainClass_C1_variabile_V1 è  diverso da RossoGialloxVerdex e  se il controllo ConsDef  è  uguale a FALSE  *37,* o  se la variabile MainClass_C1_variabile_V3 è  uguale a RossoGialloxVerdex *35,* o  se il controllo MainClass_C1_controllo_C1 è  diverso da  True  e  se il controllo ConsDef  è  uguale a FALSE  *35,* o  se il controllo MainClass_C1_controllo_C9 è  diverso da RossoGialloxVerdex, Tutte le seguenti { 
    //   *69,* *37,*  se la variabile MainClass_C1_variabile_V9 è  uguale a c180x *37,* e  se la variabile MainClass_C1_variabile_V9 non è  uguale a c180x o  se il controllo ConsDef  è  uguale a FALSE  *34,* o  se il parametro MainClass_C1_parametro_P3 non è  uguale a  *53,* 2 *34,* o  se il parametro MainClass_C1_parametro_P8 è  uguale a  *53,* 8 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
    //   *38,*  se il contatore MainClass_C1_contatore_Co3 è  minore di  *55,* 13 e  se il controllo ConsDef  è  uguale a FALSE  *38,* o  se il contatore MainClass_C1_contatore_Co3 non è  diverso da  *56,* 14 *36,* o  se il timer MainClass_C1_timer_T2 non è scaduto, Verifica che   *49,*  *,*  il timer MainClass_C1_timer_T5 sia scaduto
    //   } Verifica che   *51,*  *,*  il contatore MainClass_C1_contatore_Co3 sia  minore di  *55,* 12
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_OrLogicOP_4 = false;
    bool res_AndLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetMainc37(my_id) == rossogiallo1));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_6);
    res_AndLogicOP_5 = (res_AndLogicOP_5 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_AndLogicOP_5);
    res_OrLogicOP_4 = (res_OrLogicOP_4 || (L_P1__GetMainc40(my_id) == rossogiallo1));
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_OrLogicOP_4);
    bool res_AndLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetInMainc5(my_id) == true));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_8);
    res_AndLogicOP_7 = (res_AndLogicOP_7 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_AndLogicOP_7);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetInMainc7(my_id) == rossogiallo1));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_9);
    
    if(res_OrLogicOP_2){
    bool res_AndLogicOP_10 = true;
    bool res_ImpliesLogicOp_11 = true;
    bool res_OrLogicOP_12 = false;
    bool res_OrLogicOP_13 = false;
    bool res_OrLogicOP_14 = false;
    bool res_AndLogicOP_15 = true;
    res_AndLogicOP_15 = (res_AndLogicOP_15 && (L_P1__GetMainc41(my_id) == c180x));
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (L_P1__GetMainc41(my_id) == c180x));
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_NotLogicOP_16);
    
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_AndLogicOP_15);
    res_OrLogicOP_14 = (res_OrLogicOP_14 || (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_OrLogicOP_14);
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! (L_P1__GetParamMainc9(my_id) == 2u));
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_NotLogicOP_17);
    
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_OrLogicOP_13);
    bool res_AndLogicOP_18 = true;
    res_AndLogicOP_18 = (res_AndLogicOP_18 && (L_P1__GetParamMainc12(my_id) == 8u));
    res_AndLogicOP_18 = (res_AndLogicOP_18 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_AndLogicOP_18);
    
    if(res_OrLogicOP_12){
    bool res_ImpliesLogicOp_19 = true;
    bool res_OrLogicOP_20 = false;
    bool res_OrLogicOP_21 = false;
    bool res_AndLogicOP_22 = true;
    res_AndLogicOP_22 = (res_AndLogicOP_22 && (Counter_GetValore(L_P1__GetMainc52(my_id)) < 13u));
    res_AndLogicOP_22 = (res_AndLogicOP_22 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_21 = (res_OrLogicOP_21 || res_AndLogicOP_22);
    bool res_NotLogicOP_23 = true;
    bool res_NotLogicOP_24 = true;
    res_NotLogicOP_24 = (res_NotLogicOP_24 && ! (Counter_GetValore(L_P1__GetMainc52(my_id)) == 14u));
    res_NotLogicOP_23 = (res_NotLogicOP_23 && ! res_NotLogicOP_24);
    res_OrLogicOP_21 = (res_OrLogicOP_21 || res_NotLogicOP_23);
    
    res_OrLogicOP_20 = (res_OrLogicOP_20 || res_OrLogicOP_21);
    bool res_NotLogicOP_25 = true;
    res_NotLogicOP_25 = (res_NotLogicOP_25 && ! Timer_Scaduto(L_P1__GetMainc50(my_id)));
    res_OrLogicOP_20 = (res_OrLogicOP_20 || res_NotLogicOP_25);
    
    if(res_OrLogicOP_20){
    res_ImpliesLogicOp_19 = (res_ImpliesLogicOp_19 && Timer_Scaduto(L_P1__GetMainc51(my_id)));
    }
    res_ImpliesLogicOp_11 = (res_ImpliesLogicOp_11 && res_ImpliesLogicOp_19);
    }
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_ImpliesLogicOp_11);
    res_AndLogicOP_10 = (res_AndLogicOP_10 && (Counter_GetValore(L_P1__GetMainc52(my_id)) < 12u));
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_AndLogicOP_10);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *47,*  *34,*  il parametro MainClass_C1_parametro_P6 sia  diverso da  False
    bool res_NotLogicOP_26 = true;
    res_NotLogicOP_26 = (res_NotLogicOP_26 && ! (L_P1__GetParamMainc10(my_id) == false));
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_NotLogicOP_26);
    
    if(res_AndLogicOP_0){
    L_P1__SetOutEvent3(my_id,LDS_MANCMD_PROCESSED);
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

// risposte ai comandi manuali
static void L_P1__SetOutEvent3(
	instance_id_t const my_id, 
	ManCmdResponse const value) 
{
    UNUSED(my_id);
    UNUSED(value);
}



