
#include "Logica/ClasseMainClass_C1_priv.h"
#include "Logica/ClasseSubClass_C2_priv.h"
#include "Logica/ClasseSubClass_C3_priv.h"
#include "Logica/ClasseSubClass_C4_priv.h"
#include "config.h"
#include "PlatformMacros.h"

int L_P1_C1_cmd_tmp_id = -1; 

// ********** Dichiarazione guardie **********


// ********** Dichiarazione comandi manuali **********
static bool L_P1__GetInEvent(instance_id_t const my_id) ;
static bool L_P1__GetInEvent1(instance_id_t const my_id) ;
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



