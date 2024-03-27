
#include "Logica/ClasseMainClass_C1_priv.h"
#include "Logica/ClasseSubClass_C2_priv.h"
#include "config.h"
#include "PlatformMacros.h"

int L_P1_C2_cmd_tmp_id = -1; 

// ********** Dichiarazione guardie **********

static bool L_P1__guard5(instance_id_t const my_id);

// ********** Dichiarazione comandi manuali **********
static bool L_P1__GetInEvent1(instance_id_t const my_id) ;
static bool L_P1__GetInEvent2(instance_id_t const my_id) ;
static bool L_P1__GetInEvent3(instance_id_t const my_id) ;

static void L_P1__SetOutEvent5(
	instance_id_t const my_id, 
	ManCmdResponse const value);

static void L_P1__SetOutEvent6(
	instance_id_t const my_id, 
	ManCmdResponse const value);

static void L_P1__SetOutEvent7(
	instance_id_t const my_id, 
	ManCmdResponse const value);



// ********** Definizione guardie **********

static bool L_P1__guard5(instance_id_t const my_id)
{
    bool res_AndLogicOP_0 = true;
    
    //  *86,*  Almeno una delle seguenti {
    //   *82,*  Ricezione del comando manuale   SubClass_C2_command_comm3 da  Sender855df2bd   *76,*
    //   *82,*  Ricezione del comando manuale   SubClass_C2_command_comm3 da  Sender855df2bd   *76,*
    //   *83,*  Tutte le seguenti {
    //   Ricezione del  comando manuale   SubClass_C2_command_comm3 da  Sender855df2bd   *76,*
    //   *67,* *35,*  se il controllo SubClass_C2_controllo_C8 non è  diverso da  True  *36,* e  se il timer SubClass_C2_timer_T9 non è disattivo *35,* e  se il controllo SubClass_C2_controllo_C1 non è  diverso da c270 *35,* o  se il controllo SubClass_C2_controllo_C1 è  diverso da c270 *37,* e  se la variabile SubClass_C2_variabile_V7 non è  diverso da RossoGialloVerde *37,* o  se la variabile SubClass_C2_variabile_V7 è  uguale a RossoGialloVerde, Tutte le seguenti { 
    //   *68,* *38,*  se il contatore SubClass_C2_contatore_Co9 non è  uguale a  *53,* 1545 *35,* o  se il controllo SubClass_C2_controllo_C8 è  diverso da  True , Almeno una delle seguenti { 
    //   *36,*  se il timer SubClass_C2_timer_T10 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE  *36,* e  se il timer SubClass_C2_timer_T8 non è attivo *38,* o  se il contatore SubClass_C2_contatore_Co4 non è  minore di  *55,* 123 e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   *47,*  *34,*  il parametro SubClass_C2_parametro_P6 non sia  uguale a c270
    //   } Verifica che   *51,*  *,*  il contatore SubClass_C2_contatore_Co9 sia  minore di  *55,* 11210
    //   } Verifica che   *49,*  *,*  il timer SubClass_C2_timer_T6 sia attivo
    //  }
    //  }
    bool res_OrLogicOP_1 = false;
    res_OrLogicOP_1 = (res_OrLogicOP_1 || L_P1__GetInEvent3(my_id));
    res_OrLogicOP_1 = (res_OrLogicOP_1 || L_P1__GetInEvent3(my_id));
    bool res_AndLogicOP_2 = true;
    res_AndLogicOP_2 = (res_AndLogicOP_2 && L_P1__GetInEvent3(my_id));
    bool res_ImpliesLogicOp_3 = true;
    bool res_OrLogicOP_4 = false;
    bool res_OrLogicOP_5 = false;
    bool res_AndLogicOP_6 = true;
    bool res_AndLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetInSubcl4(my_id) == true));
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! res_NotLogicOP_9);
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_8);
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! Timer_Disattivo(L_P1__GetSubcl49(my_id)));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_10);
    
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_AndLogicOP_7);
    bool res_NotLogicOP_11 = true;
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (L_P1__GetInSubcl2(my_id) == c270));
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! res_NotLogicOP_12);
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_11);
    
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_AndLogicOP_6);
    bool res_AndLogicOP_13 = true;
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1__GetInSubcl2(my_id) == c270));
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_NotLogicOP_14);
    bool res_NotLogicOP_15 = true;
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (L_P1__GetSubcl36(my_id) == rossogiallo3));
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! res_NotLogicOP_16);
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_NotLogicOP_15);
    
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_AndLogicOP_13);
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_OrLogicOP_5);
    res_OrLogicOP_4 = (res_OrLogicOP_4 || (L_P1__GetSubcl36(my_id) == rossogiallo3));
    
    if(res_OrLogicOP_4){
    bool res_AndLogicOP_17 = true;
    bool res_ImpliesLogicOp_18 = true;
    bool res_OrLogicOP_19 = false;
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! (Counter_GetValore(L_P1__GetSubcl52(my_id)) == 1545u));
    res_OrLogicOP_19 = (res_OrLogicOP_19 || res_NotLogicOP_20);
    bool res_NotLogicOP_21 = true;
    res_NotLogicOP_21 = (res_NotLogicOP_21 && ! (L_P1__GetInSubcl4(my_id) == true));
    res_OrLogicOP_19 = (res_OrLogicOP_19 || res_NotLogicOP_21);
    
    if(res_OrLogicOP_19){
    bool res_ImpliesLogicOp_22 = true;
    bool res_OrLogicOP_23 = false;
    bool res_OrLogicOP_24 = false;
    bool res_NotLogicOP_25 = true;
    res_NotLogicOP_25 = (res_NotLogicOP_25 && ! Timer_Disattivo(L_P1__GetSubcl45(my_id)));
    res_OrLogicOP_24 = (res_OrLogicOP_24 || res_NotLogicOP_25);
    bool res_AndLogicOP_26 = true;
    res_AndLogicOP_26 = (res_AndLogicOP_26 && (L_P1__GetInConsd1(my_id) == false));
    bool res_NotLogicOP_27 = true;
    res_NotLogicOP_27 = (res_NotLogicOP_27 && ! Timer_Attivo(L_P1__GetSubcl48(my_id)));
    res_AndLogicOP_26 = (res_AndLogicOP_26 && res_NotLogicOP_27);
    
    res_OrLogicOP_24 = (res_OrLogicOP_24 || res_AndLogicOP_26);
    
    res_OrLogicOP_23 = (res_OrLogicOP_23 || res_OrLogicOP_24);
    bool res_AndLogicOP_28 = true;
    bool res_NotLogicOP_29 = true;
    res_NotLogicOP_29 = (res_NotLogicOP_29 && ! (Counter_GetValore(L_P1__GetSubcl50(my_id)) < 123u));
    res_AndLogicOP_28 = (res_AndLogicOP_28 && res_NotLogicOP_29);
    res_AndLogicOP_28 = (res_AndLogicOP_28 && (L_P1__GetInConsd1(my_id) == false));
    
    res_OrLogicOP_23 = (res_OrLogicOP_23 || res_AndLogicOP_28);
    
    if(res_OrLogicOP_23){
    bool res_NotLogicOP_30 = true;
    res_NotLogicOP_30 = (res_NotLogicOP_30 && ! (L_P1__GetParamSubcl9(my_id) == c270));
    res_ImpliesLogicOp_22 = (res_ImpliesLogicOp_22 && res_NotLogicOP_30);
    }
    res_ImpliesLogicOp_18 = (res_ImpliesLogicOp_18 && res_ImpliesLogicOp_22);
    }
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_ImpliesLogicOp_18);
    res_AndLogicOP_17 = (res_AndLogicOP_17 && (Counter_GetValore(L_P1__GetSubcl52(my_id)) < 11210u));
    
    res_ImpliesLogicOp_3 = (res_ImpliesLogicOp_3 && res_AndLogicOP_17);
    }
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_ImpliesLogicOp_3);
    res_AndLogicOP_2 = (res_AndLogicOP_2 && Timer_Attivo(L_P1__GetSubcl47(my_id)));
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_2);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_1);
    
    if(res_OrLogicOP_1){
    L_P1__SetOutEvent7(my_id,LDS_MANCMD_PROCESSED);
    }
    else{
    
    }
    
    
    return res_AndLogicOP_0;
}


// ********** Definizione macro **********

// Macro di verifica


// Macro valorizzate



//FEASIBILIT
int L_P1_C2_getFeasibility(instance_id_t const my_id, int cmd_id)
{
L_P1_C2_cmd_tmp_id = cmd_id;
int ret = 1;

switch (L_P1_C2_GetState(my_id)) {
	case C2_St_state:
		switch (cmd_id){
			default:
			break;
		}
	break;
	case C2_St_state1:
		switch (cmd_id){
			case 54:
				if(L_P1__guard5(my_id)){
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
static bool L_P1__GetInEvent1(instance_id_t const my_id) 
{
    UNUSED(my_id);
    if(L_P1__event1_ID==L_P1_C2_cmd_tmp_id){
		return true;
	}	
	else{
		return false;
	}
}
static bool L_P1__GetInEvent2(instance_id_t const my_id) 
{
    UNUSED(my_id);
    if(L_P1__event2_ID==L_P1_C2_cmd_tmp_id){
		return true;
	}	
	else{
		return false;
	}
}
static bool L_P1__GetInEvent3(instance_id_t const my_id) 
{
    UNUSED(my_id);
    if(L_P1__event3_ID==L_P1_C2_cmd_tmp_id){
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



