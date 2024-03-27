// Codice del modello 'TestCase10', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#include "Logica/ClasseMainClass_C1.h"
#include "Logica/ClasseSubClass_C2.h"
#include "Logica/ClasseSubClass_C3.h"
#include "Logica/ClasseSubClass_C2_priv.h"
#include "config.h"
#include "scheduler.h"


// ********** Gestione comandi manuali **********

static void L_P1_C2_InitCmdsResponse(instance_id_t const my_id)
{
    // for each manual command of L_P1_C2
    if (L_P1__GetInEvent6(my_id)) {
	    L_P1__SetOutEvent7(my_id, LDS_MANCMD_UNEXPECTED);
    } else {
        L_P1__SetOutEvent7(my_id, LDS_MANCMD_NOOP);
    }
}

static void L_P1_C2_SetExpectedCmdsResponse(instance_id_t const my_id, C2_Stateenu state)
{        
    switch (state) {
    case C2_St_state1:
        // manual commands of L_P1_C2 that can be received in C2_St_state1
	break;

    case C2_St_state:
        // manual commands of L_P1_C2 that can be received in C2_St_state
	break;

    case C2_St_state3:
        // manual commands of L_P1_C2 that can be received in C2_St_state3
        if (L_P1__GetInEvent6(my_id)) {
            L_P1__SetOutEvent7(my_id, LDS_MANCMD_BLOCKED);
        }
	break;

    case C2_St_state2:
        // manual commands of L_P1_C2 that can be received in C2_St_state2
	break;

    default:
        STOP_EXECUTION(LOGIC_ERROR);
        break;
    }
}


// ********** Definizione guardie **********

/*
    CNL corrispondente:
    
     {
     Nessuna 
     }
*/
static inline bool L_P1__Guard2(instance_id_t const my_id)
{
    return true;
}


/*
    CNL corrispondente:
    
    {
    
     Nessuna 
    }
*/
static inline bool L_P1__Guard3(instance_id_t const my_id)
{
    return true;
}


/*
    CNL corrispondente:
    
    {
    
     commento: {68,} commento: {37,}  se la variabile SubClass_C2_variabile_V9 è  diverso da  True  commento: {35,} o  se il controllo SubClass_C2_controllo_C3 è  uguale a  False  commento: {38,} e  se il contatore SubClass_C2_contatore_Co10 non è  maggiore di  commento: {54,} 11215 commento: {38,} e  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  commento: {56,} 13403 commento: {38,} o  se il contatore SubClass_C2_contatore_Co10 è  diverso da  commento: {56,} 11215, Almeno una delle seguenti { 
     commento: {67,} commento: {35,}  se il controllo SubClass_C2_controllo_C3 non è  uguale a  False  commento: {37,} o  se la variabile SubClass_C2_variabile_V5 non è  diverso da  False , Tutte le seguenti { 
     commento: {67,} commento: {37,}  se la variabile SubClass_C2_variabile_V5 è  uguale a  True  commento: {37,} e  se la variabile SubClass_C2_variabile_V9 è  uguale a  False  commento: {34,} e  se il parametro SubClass_C2_parametro_P8 non è  diverso da  commento: {56,} 3 commento: {35,} e  se il controllo SubClass_C2_controllo_C9 non è  diverso da RossoGiallo, Tutte le seguenti { 
     commento: {67,} commento: {36,}  se il timer SubClass_C2_timer_T5 è scaduto, Tutte le seguenti { 
     commento: {36,}  se il timer SubClass_C2_timer_T5 non è disattivo commento: {38,} o  se il contatore SubClass_C2_contatore_Co10 non è  minore di  commento: {55,} 11, Verifica che   commento: {50,}  commento: {,}  la variabile SubClass_C2_variabile_V5 sia  diverso da  True 
    
    
     } Verifica che   commento: {49,}  commento: {,}  il timer SubClass_C2_timer_T8 non sia scaduto
    
    
     } Verifica che   commento: {48,}  commento: {,}  il controllo SubClass_C2_controllo_C3 sia  uguale a  True 
    
    
     } Verifica che   commento: {51,}  commento: {,}  il contatore SubClass_C2_contatore_Co10 non sia  minore di  commento: {55,} 153
    
    
     } Verifica che   commento: {51,}  commento: {,}  il contatore SubClass_C2_contatore_Co10 non sia  diverso da  commento: {56,} 15
    
    
    }
*/
static inline bool L_P1__Guard4(instance_id_t const my_id)
{
    bool res_AndLogicOP_0 = true;
    
    //  *68,* *37,*  se la variabile SubClass_C2_variabile_V9 è  diverso da  True  *35,* o  se il controllo SubClass_C2_controllo_C3 è  uguale a  False  *38,* e  se il contatore SubClass_C2_contatore_Co10 non è  maggiore di  *54,* 11215 *38,* e  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  *56,* 13403 *38,* o  se il contatore SubClass_C2_contatore_Co10 è  diverso da  *56,* 11215, Almeno una delle seguenti { 
    //   *67,* *35,*  se il controllo SubClass_C2_controllo_C3 non è  uguale a  False  *37,* o  se la variabile SubClass_C2_variabile_V5 non è  diverso da  False , Tutte le seguenti { 
    //   *67,* *37,*  se la variabile SubClass_C2_variabile_V5 è  uguale a  True  *37,* e  se la variabile SubClass_C2_variabile_V9 è  uguale a  False  *34,* e  se il parametro SubClass_C2_parametro_P8 non è  diverso da  *56,* 3 *35,* e  se il controllo SubClass_C2_controllo_C9 non è  diverso da RossoGiallo, Tutte le seguenti { 
    //   *67,* *36,*  se il timer SubClass_C2_timer_T5 è scaduto, Tutte le seguenti { 
    //   *36,*  se il timer SubClass_C2_timer_T5 non è disattivo *38,* o  se il contatore SubClass_C2_contatore_Co10 non è  minore di  *55,* 11, Verifica che   *50,*  *,*  la variabile SubClass_C2_variabile_V5 sia  diverso da  True 
    //   } Verifica che   *49,*  *,*  il timer SubClass_C2_timer_T8 non sia scaduto
    //   } Verifica che   *48,*  *,*  il controllo SubClass_C2_controllo_C3 sia  uguale a  True 
    //   } Verifica che   *51,*  *,*  il contatore SubClass_C2_contatore_Co10 non sia  minore di  *55,* 153
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetSubcl28(my_id) == true));
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_NotLogicOP_4);
    bool res_AndLogicOP_5 = true;
    bool res_AndLogicOP_6 = true;
    res_AndLogicOP_6 = (res_AndLogicOP_6 && (L_P1__GetInSubcl5(my_id) == false));
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (Counter_GetValore(L_P1__GetSubcl36(my_id)) > 11215u));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_7);
    
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_AndLogicOP_6);
    bool res_NotLogicOP_8 = true;
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (Counter_GetValore(L_P1__GetSubcl36(my_id)) == 13403u));
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! res_NotLogicOP_9);
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_8);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_AndLogicOP_5);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (Counter_GetValore(L_P1__GetSubcl36(my_id)) == 11215u));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_10);
    
    if(res_OrLogicOP_2){
    bool res_OrLogicOP_11 = false;
    bool res_ImpliesLogicOp_12 = true;
    bool res_OrLogicOP_13 = false;
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1__GetInSubcl5(my_id) == false));
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_NotLogicOP_14);
    bool res_NotLogicOP_15 = true;
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (L_P1__GetSubcl27(my_id) == false));
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! res_NotLogicOP_16);
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_NotLogicOP_15);
    
    if(res_OrLogicOP_13){
    bool res_AndLogicOP_17 = true;
    bool res_ImpliesLogicOp_18 = true;
    bool res_AndLogicOP_19 = true;
    bool res_AndLogicOP_20 = true;
    bool res_AndLogicOP_21 = true;
    res_AndLogicOP_21 = (res_AndLogicOP_21 && (L_P1__GetSubcl27(my_id) == true));
    res_AndLogicOP_21 = (res_AndLogicOP_21 && (L_P1__GetSubcl28(my_id) == false));
    
    res_AndLogicOP_20 = (res_AndLogicOP_20 && res_AndLogicOP_21);
    bool res_NotLogicOP_22 = true;
    bool res_NotLogicOP_23 = true;
    res_NotLogicOP_23 = (res_NotLogicOP_23 && ! (L_P1__GetParamSubcl8(my_id) == 3u));
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! res_NotLogicOP_23);
    res_AndLogicOP_20 = (res_AndLogicOP_20 && res_NotLogicOP_22);
    
    res_AndLogicOP_19 = (res_AndLogicOP_19 && res_AndLogicOP_20);
    bool res_NotLogicOP_24 = true;
    bool res_NotLogicOP_25 = true;
    res_NotLogicOP_25 = (res_NotLogicOP_25 && ! (L_P1__GetInSubcl6(my_id) == rossogiallo1));
    res_NotLogicOP_24 = (res_NotLogicOP_24 && ! res_NotLogicOP_25);
    res_AndLogicOP_19 = (res_AndLogicOP_19 && res_NotLogicOP_24);
    
    if(res_AndLogicOP_19){
    bool res_AndLogicOP_26 = true;
    bool res_ImpliesLogicOp_27 = true;
    if(Timer_Scaduto(L_P1__GetSubcl32(my_id))){
    bool res_ImpliesLogicOp_28 = true;
    bool res_OrLogicOP_29 = false;
    bool res_NotLogicOP_30 = true;
    res_NotLogicOP_30 = (res_NotLogicOP_30 && ! Timer_Disattivo(L_P1__GetSubcl32(my_id)));
    res_OrLogicOP_29 = (res_OrLogicOP_29 || res_NotLogicOP_30);
    bool res_NotLogicOP_31 = true;
    res_NotLogicOP_31 = (res_NotLogicOP_31 && ! (Counter_GetValore(L_P1__GetSubcl36(my_id)) < 11u));
    res_OrLogicOP_29 = (res_OrLogicOP_29 || res_NotLogicOP_31);
    
    if(res_OrLogicOP_29){
    bool res_NotLogicOP_32 = true;
    res_NotLogicOP_32 = (res_NotLogicOP_32 && ! (L_P1__GetSubcl27(my_id) == true));
    res_ImpliesLogicOp_28 = (res_ImpliesLogicOp_28 && res_NotLogicOP_32);
    }
    res_ImpliesLogicOp_27 = (res_ImpliesLogicOp_27 && res_ImpliesLogicOp_28);
    }
    res_AndLogicOP_26 = (res_AndLogicOP_26 && res_ImpliesLogicOp_27);
    bool res_NotLogicOP_33 = true;
    res_NotLogicOP_33 = (res_NotLogicOP_33 && ! Timer_Scaduto(L_P1__GetSubcl34(my_id)));
    res_AndLogicOP_26 = (res_AndLogicOP_26 && res_NotLogicOP_33);
    
    res_ImpliesLogicOp_18 = (res_ImpliesLogicOp_18 && res_AndLogicOP_26);
    }
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_ImpliesLogicOp_18);
    res_AndLogicOP_17 = (res_AndLogicOP_17 && (L_P1__GetInSubcl5(my_id) == true));
    
    res_ImpliesLogicOp_12 = (res_ImpliesLogicOp_12 && res_AndLogicOP_17);
    }
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_ImpliesLogicOp_12);
    bool res_NotLogicOP_34 = true;
    res_NotLogicOP_34 = (res_NotLogicOP_34 && ! (Counter_GetValore(L_P1__GetSubcl36(my_id)) < 153u));
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_NotLogicOP_34);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_OrLogicOP_11);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *51,*  *,*  il contatore SubClass_C2_contatore_Co10 non sia  diverso da  *56,* 15
    bool res_NotLogicOP_35 = true;
    bool res_NotLogicOP_36 = true;
    res_NotLogicOP_36 = (res_NotLogicOP_36 && ! (Counter_GetValore(L_P1__GetSubcl36(my_id)) == 15u));
    res_NotLogicOP_35 = (res_NotLogicOP_35 && ! res_NotLogicOP_36);
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_NotLogicOP_35);
    
    
    
    return res_AndLogicOP_0;
}


/*
    CNL corrispondente:
    
    {
    
     commento: {68,} commento: {34,}  se il parametro SubClass_C2_parametro_P8 non è  minore di  commento: {55,} 9 commento: {37,} e  se la variabile SubClass_C2_variabile_V5 non è  uguale a  False , Almeno una delle seguenti { 
      se il controllo ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro SubClass_C2_parametro_P8 è  maggiore di  commento: {54,} 10 commento: {35,} e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  True  commento: {34,} e  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  commento: {54,} 9 commento: {34,} o  se il parametro SubClass_C2_parametro_P8 non è  minore di  commento: {55,} 5 commento: {37,} o  se la variabile SubClass_C2_variabile_V9 è  diverso da  False , Verifica che   commento: {51,}  commento: {,}  il contatore SubClass_C2_contatore_Co10 non sia  uguale a  commento: {53,} 122
    
    
     } Verifica che   commento: {49,}  commento: {,}  il timer SubClass_C2_timer_T7 sia disattivo
    
    
    }
*/
static inline bool L_P1__Guard5(instance_id_t const my_id)
{
    bool res_AndLogicOP_0 = true;
    
    //  *68,* *34,*  se il parametro SubClass_C2_parametro_P8 non è  minore di  *55,* 9 *37,* e  se la variabile SubClass_C2_variabile_V5 non è  uguale a  False , Almeno una delle seguenti { 
    //    se il controllo ConsDef  è  uguale a FALSE  *34,* e  se il parametro SubClass_C2_parametro_P8 è  maggiore di  *54,* 10 *35,* e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  True  *34,* e  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  *54,* 9 *34,* o  se il parametro SubClass_C2_parametro_P8 non è  minore di  *55,* 5 *37,* o  se la variabile SubClass_C2_variabile_V9 è  diverso da  False , Verifica che   *51,*  *,*  il contatore SubClass_C2_contatore_Co10 non sia  uguale a  *53,* 122
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_AndLogicOP_2 = true;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__GetParamSubcl8(my_id) < 9u));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_3);
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetSubcl27(my_id) == false));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_4);
    
    if(res_AndLogicOP_2){
    bool res_ImpliesLogicOp_5 = true;
    bool res_OrLogicOP_6 = false;
    bool res_OrLogicOP_7 = false;
    bool res_AndLogicOP_8 = true;
    bool res_AndLogicOP_9 = true;
    bool res_AndLogicOP_10 = true;
    res_AndLogicOP_10 = (res_AndLogicOP_10 && (L_P1__GetInConsd1(my_id) == false));
    res_AndLogicOP_10 = (res_AndLogicOP_10 && (L_P1__GetParamSubcl8(my_id) > 10u));
    
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_AndLogicOP_10);
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (L_P1__GetInSubcl5(my_id) == true));
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_NotLogicOP_11);
    
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_AndLogicOP_9);
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (L_P1__GetParamSubcl8(my_id) > 9u));
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_12);
    
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_AndLogicOP_8);
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (L_P1__GetParamSubcl8(my_id) < 5u));
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_NotLogicOP_13);
    
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_OrLogicOP_7);
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1__GetSubcl28(my_id) == false));
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_NotLogicOP_14);
    
    if(res_OrLogicOP_6){
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (Counter_GetValore(L_P1__GetSubcl36(my_id)) == 122u));
    res_ImpliesLogicOp_5 = (res_ImpliesLogicOp_5 && res_NotLogicOP_15);
    }
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_ImpliesLogicOp_5);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *49,*  *,*  il timer SubClass_C2_timer_T7 sia disattivo
    res_AndLogicOP_0 = (res_AndLogicOP_0 && Timer_Disattivo(L_P1__GetSubcl33(my_id)));
    
    
    
    return res_AndLogicOP_0;
}


/*
    CNL corrispondente:
     {  Nessuna  commento: {80,} }
*/
static inline bool L_P1__Guard6(instance_id_t const my_id)
{
    return true;
}


/*
    CNL corrispondente:
     {  Nessuna  commento: {80,} }
*/
static inline bool L_P1__Guard7(instance_id_t const my_id)
{
    return true;
}


/*
    CNL corrispondente:
     {  Nessuna  }
*/
static inline bool L_P1__Guard8(instance_id_t const my_id)
{
    return true;
}


/*
    CNL corrispondente:
     {  Nessuna  }
*/
static inline bool L_P1__Guard9(instance_id_t const my_id)
{
    return true;
}


/*
    CNL corrispondente:
    
    {
    
     commento: {36,}  se il timer SubClass_C2_timer_T3 non è scaduto, Verifica che   commento: {50,}  commento: {,}  la variabile SubClass_C2_variabile_V5 sia  diverso da  True 
    
    
    }
*/
static inline bool L_P1__Guard10(instance_id_t const my_id)
{
    bool res_AndLogicOP_0 = true;
    
    //  *36,*  se il timer SubClass_C2_timer_T3 non è scaduto, Verifica che   *50,*  *,*  la variabile SubClass_C2_variabile_V5 sia  diverso da  True
    bool res_ImpliesLogicOp_1 = true;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! Timer_Scaduto(L_P1__GetSubcl31(my_id)));
    if(res_NotLogicOP_2){
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__GetSubcl27(my_id) == true));
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_NotLogicOP_3);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    
    
    return res_AndLogicOP_0;
}


/*
    CNL corrispondente:
     {  Nessuna  }
*/
static inline bool L_P1__Guard11(instance_id_t const my_id)
{
    return true;
}


/*
    CNL corrispondente:
     {   se il controllo ConsDef  è  uguale a FALSE  commento: {36,} e  se il timer SubClass_C2_timer_T9 è disattivo commento: {38,} e  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  commento: {56,} 12215 e  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} o  se il timer SubClass_C2_timer_T3 è attivo commento: {38,} e  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  commento: {56,} 13403, Verifica che   commento: {47,}  commento: {34,}  il parametro SubClass_C2_parametro_P8 non sia  minore di  commento: {55,} 1
    
     }
*/
static inline bool L_P1__Guard12(instance_id_t const my_id)
{
    bool res_AndLogicOP_0 = true;
    
    //  se il controllo ConsDef  è  uguale a FALSE  *36,* e  se il timer SubClass_C2_timer_T9 è disattivo *38,* e  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  *56,* 12215 e  se il controllo ConsDef  è  uguale a FALSE  *36,* o  se il timer SubClass_C2_timer_T3 è attivo *38,* e  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  *56,* 13403, Verifica che   *47,*  *34,*  il parametro SubClass_C2_parametro_P8 non sia  minore di  *55,* 1
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_AndLogicOP_3 = true;
    bool res_AndLogicOP_4 = true;
    bool res_AndLogicOP_5 = true;
    res_AndLogicOP_5 = (res_AndLogicOP_5 && (L_P1__GetInConsd1(my_id) == false));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && Timer_Disattivo(L_P1__GetSubcl35(my_id)));
    
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_AndLogicOP_5);
    bool res_NotLogicOP_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (Counter_GetValore(L_P1__GetSubcl36(my_id)) == 12215u));
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! res_NotLogicOP_7);
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_6);
    
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_AndLogicOP_4);
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (L_P1__GetInConsd1(my_id) == false));
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_3);
    bool res_AndLogicOP_8 = true;
    res_AndLogicOP_8 = (res_AndLogicOP_8 && Timer_Attivo(L_P1__GetSubcl31(my_id)));
    bool res_NotLogicOP_9 = true;
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (Counter_GetValore(L_P1__GetSubcl36(my_id)) == 13403u));
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! res_NotLogicOP_10);
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_9);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_8);
    
    if(res_OrLogicOP_2){
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (L_P1__GetParamSubcl8(my_id) < 1u));
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_NotLogicOP_11);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    
    
    return res_AndLogicOP_0;
}


/*
    CNL corrispondente:
     {  commento: {86,}  Almeno una delle seguenti {
     commento: {83,}  Tutte le seguenti {
     Ricezione del  comando manuale   SubClass_C2_command_comm4   commento: {77,}
     commento: {68,} commento: {35,}  se il controllo SubClass_C2_controllo_C3 è  diverso da  True , Almeno una delle seguenti { 
     commento: {38,}  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  commento: {54,} 14, Verifica che   commento: {47,}  commento: {34,}  il parametro SubClass_C2_parametro_P8 non sia  uguale a  commento: {53,} 4
    
    
     } Verifica che   commento: {51,}  commento: {,}  il contatore SubClass_C2_contatore_Co10 non sia  minore di  commento: {55,} 15
    
    
    } commento: {83,}  Tutte le seguenti {
     Ricezione del  comando manuale   SubClass_C2_command_comm4   commento: {77,}
     commento: {68,} commento: {35,}  se il controllo SubClass_C2_controllo_C9 non è  uguale a RossoGiallo commento: {37,} e  se la variabile SubClass_C2_variabile_V9 è  diverso da  True  commento: {37,} o  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False  commento: {37,} o  se la variabile SubClass_C2_variabile_V9 è  uguale a  True , Almeno una delle seguenti { 
     commento: {69,}  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
     commento: {68,} commento: {35,}  se il controllo SubClass_C2_controllo_C3 è  diverso da  True  commento: {36,} o  se il timer SubClass_C2_timer_T3 è scaduto, Almeno una delle seguenti { 
     commento: {69,} commento: {35,}  se il controllo SubClass_C2_controllo_C3 è  uguale a  True  commento: {36,} o  se il timer SubClass_C2_timer_T8 è scaduto, Solo una delle seguenti { 
     commento: {69,}  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} o  se il timer SubClass_C2_timer_T5 non è scaduto, Solo una delle seguenti { 
     commento: {36,}  se il timer SubClass_C2_timer_T9 è attivo o  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} e  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False  commento: {35,} e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  True , Verifica che   commento: {49,}  commento: {,}  il timer SubClass_C2_timer_T9 sia attivo
    
    
     } Verifica che   commento: {49,}  commento: {,}  il timer SubClass_C2_timer_T8 non sia scaduto
    
    
     } Verifica che   commento: {51,}  commento: {,}  il contatore SubClass_C2_contatore_Co10 sia  minore di  commento: {55,} 13
    
    
     } Verifica che   commento: {48,}  commento: {,}  il controllo SubClass_C2_controllo_C3 non sia  diverso da  True 
    
    
     } Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
    
    
     } Verifica che   commento: {51,}  commento: {,}  il contatore SubClass_C2_contatore_Co10 non sia  uguale a  commento: {53,} 11215
    
    
    } commento: {83,}  Tutte le seguenti {
     Ricezione del  comando manuale   SubClass_C2_command_comm4   commento: {77,}
     commento: {68,} commento: {36,}  se il timer SubClass_C2_timer_T5 è scaduto commento: {34,} o  se il parametro SubClass_C2_parametro_P8 è  diverso da  commento: {56,} 2 commento: {38,} o  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  commento: {56,} 12 o  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} e  se il contatore SubClass_C2_contatore_Co10 è  uguale a  commento: {53,} 124, Almeno una delle seguenti { 
     commento: {69,} commento: {37,}  se la variabile SubClass_C2_variabile_V5 non è  diverso da  True  commento: {38,} o  se il contatore SubClass_C2_contatore_Co10 è  minore di  commento: {55,} 130 commento: {35,} e  se il controllo SubClass_C2_controllo_C3 è  uguale a  False  commento: {36,} o  se il timer SubClass_C2_timer_T5 è attivo commento: {38,} e  se il contatore SubClass_C2_contatore_Co10 è  minore di  commento: {55,} 11321 commento: {38,} o  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  commento: {56,} 125, Solo una delle seguenti { 
     commento: {68,} commento: {38,}  se il contatore SubClass_C2_contatore_Co10 è  uguale a  commento: {53,} 13403, Almeno una delle seguenti { 
     commento: {69,}  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} o  se il parametro SubClass_C2_parametro_P8 è  uguale a  commento: {53,} 6 commento: {37,} o  se la variabile SubClass_C2_variabile_V9 è  diverso da  True  commento: {35,} o  se il controllo SubClass_C2_controllo_C9 è  uguale a RossoGiallo commento: {38,} e  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  commento: {56,} 13 commento: {38,} o  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  commento: {54,} 15, Solo una delle seguenti { 
     commento: {67,}  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} o  se il contatore SubClass_C2_contatore_Co10 è  minore di  commento: {55,} 14 commento: {34,} o  se il parametro SubClass_C2_parametro_P8 non è  uguale a  commento: {53,} 7 commento: {38,} o  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  commento: {54,} 1421 o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
     commento: {67,} commento: {36,}  se il timer SubClass_C2_timer_T7 non è scaduto, Tutte le seguenti { 
     commento: {69,} commento: {38,}  se il contatore SubClass_C2_contatore_Co10 non è  minore di  commento: {55,} 11540 commento: {36,} e  se il timer SubClass_C2_timer_T9 è scaduto commento: {38,} o  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  commento: {56,} 11321 commento: {35,} e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  False  commento: {36,} e  se il timer SubClass_C2_timer_T5 è attivo, Solo una delle seguenti { 
     commento: {68,} commento: {34,}  se il parametro SubClass_C2_parametro_P8 è  minore di  commento: {55,} 8 commento: {37,} e  se la variabile SubClass_C2_variabile_V9 non è  diverso da  True  commento: {34,} e  se il parametro SubClass_C2_parametro_P8 è  minore di  commento: {55,} 9 commento: {36,} e  se il timer SubClass_C2_timer_T5 è scaduto commento: {38,} e  se il contatore SubClass_C2_contatore_Co10 non è  uguale a  commento: {53,} 13, Almeno una delle seguenti { 
     commento: {36,}  se il timer SubClass_C2_timer_T5 non è scaduto commento: {34,} o  se il parametro SubClass_C2_parametro_P8 è  uguale a  commento: {53,} 6 commento: {37,} o  se la variabile SubClass_C2_variabile_V9 non è  uguale a  True  commento: {37,} e  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False  commento: {38,} e  se il contatore SubClass_C2_contatore_Co10 è  uguale a  commento: {53,} 135 commento: {38,} o  se il contatore SubClass_C2_contatore_Co10 non è  maggiore di  commento: {54,} 11403, Verifica che   commento: {49,}  commento: {,}  il timer SubClass_C2_timer_T5 non sia disattivo
    
    
     } Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
    
    
     } Verifica che   commento: {50,}  commento: {,}  la variabile SubClass_C2_variabile_V5 sia  uguale a  False 
    
    
     } Verifica che   commento: {49,}  commento: {,}  il timer SubClass_C2_timer_T5 sia disattivo
    
    
     } Verifica che   commento: {47,}  commento: {34,}  il parametro SubClass_C2_parametro_P8 sia  uguale a  commento: {53,} 10
    
    
     } Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
    
    
     } Verifica che   commento: {48,}  commento: {,}  il controllo SubClass_C2_controllo_C9 non sia  diverso da RossoGiallo
    
    
     } Verifica che   commento: {48,}  commento: {,}  il controllo SubClass_C2_controllo_C9 non sia  diverso da RossoGiallo
    
    
     } Verifica che   commento: {48,}  commento: {,}  il controllo SubClass_C2_controllo_C3 non sia  uguale a  True 
    
    
    } commento: {83,}  Tutte le seguenti {
     Ricezione del  comando manuale   SubClass_C2_command_comm4   commento: {77,}
     commento: {69,} commento: {38,}  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  commento: {54,} 13 commento: {35,} e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  False  commento: {35,} e  se il controllo SubClass_C2_controllo_C3 non è  diverso da  False  commento: {38,} o  se il contatore SubClass_C2_contatore_Co10 è  uguale a  commento: {53,} 13215 commento: {36,} e  se il timer SubClass_C2_timer_T9 è disattivo commento: {38,} e  se il contatore SubClass_C2_contatore_Co10 non è  minore di  commento: {55,} 14, Solo una delle seguenti { 
     commento: {67,} commento: {36,}  se il timer SubClass_C2_timer_T5 è disattivo commento: {38,} e  se il contatore SubClass_C2_contatore_Co10 è  diverso da  commento: {56,} 14403 commento: {34,} o  se il parametro SubClass_C2_parametro_P8 è  diverso da  commento: {56,} 1 commento: {35,} e  se il controllo SubClass_C2_controllo_C9 è  diverso da RossoGiallo commento: {36,} o  se il timer SubClass_C2_timer_T9 non è scaduto, Tutte le seguenti { 
     commento: {67,} commento: {35,}  se il controllo SubClass_C2_controllo_C9 è  uguale a RossoGiallo commento: {34,} e  se il parametro SubClass_C2_parametro_P8 è  maggiore di  commento: {54,} 2 commento: {35,} o  se il controllo SubClass_C2_controllo_C3 non è  diverso da  False  commento: {37,} o  se la variabile SubClass_C2_variabile_V5 non è  diverso da  False  commento: {36,} e  se il timer SubClass_C2_timer_T8 è attivo commento: {36,} e  se il timer SubClass_C2_timer_T5 non è disattivo, Tutte le seguenti { 
     commento: {67,} commento: {36,}  se il timer SubClass_C2_timer_T3 è disattivo commento: {35,} e  se il controllo SubClass_C2_controllo_C9 è  uguale a RossoGiallo commento: {37,} e  se la variabile SubClass_C2_variabile_V5 non è  uguale a  False , Tutte le seguenti { 
     commento: {67,} commento: {36,}  se il timer SubClass_C2_timer_T5 è scaduto, Tutte le seguenti { 
     commento: {69,} commento: {34,}  se il parametro SubClass_C2_parametro_P8 non è  minore di  commento: {55,} 5 commento: {38,} e  se il contatore SubClass_C2_contatore_Co10 è  diverso da  commento: {56,} 15215 commento: {36,} o  se il timer SubClass_C2_timer_T5 non è scaduto commento: {35,} e  se il controllo SubClass_C2_controllo_C9 è  diverso da RossoGiallo commento: {38,} e  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  commento: {54,} 12403, Solo una delle seguenti { 
     commento: {67,} commento: {38,}  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  commento: {56,} 11215 commento: {35,} o  se il controllo SubClass_C2_controllo_C3 è  diverso da  False  commento: {35,} o  se il controllo SubClass_C2_controllo_C3 è  uguale a  True , Tutte le seguenti { 
     commento: {34,}  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  commento: {54,} 7 commento: {34,} o  se il parametro SubClass_C2_parametro_P8 non è  minore di  commento: {55,} 4 commento: {38,} o  se il contatore SubClass_C2_contatore_Co10 è  uguale a  commento: {53,} 13, Verifica che   commento: {47,}  commento: {34,}  il parametro SubClass_C2_parametro_P8 sia  maggiore di  commento: {54,} 9
    
    
     } Verifica che   commento: {47,}  commento: {34,}  il parametro SubClass_C2_parametro_P8 non sia  minore di  commento: {55,} 3
    
    
     } Verifica che   commento: {51,}  commento: {,}  il contatore SubClass_C2_contatore_Co10 non sia  maggiore di  commento: {54,} 154
    
    
     } Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
    
    
     } Verifica che   commento: {47,}  commento: {34,}  il parametro SubClass_C2_parametro_P8 non sia  uguale a  commento: {53,} 7
    
    
     } Verifica che   commento: {51,}  commento: {,}  il contatore SubClass_C2_contatore_Co10 non sia  uguale a  commento: {53,} 13
    
    
     } Verifica che   commento: {50,}  commento: {,}  la variabile SubClass_C2_variabile_V5 sia  diverso da  False 
    
    
     } Verifica che   commento: {50,}  commento: {,}  la variabile SubClass_C2_variabile_V9 non sia  uguale a  True 
    
    
    }
    } }
*/
static inline bool L_P1__Guard13(instance_id_t const my_id)
{
    bool res_AndLogicOP_0 = true;
    
    //  *86,*  Almeno una delle seguenti {
    //   *83,*  Tutte le seguenti {
    //   Ricezione del  comando manuale   SubClass_C2_command_comm4   *77,*
    //   *68,* *35,*  se il controllo SubClass_C2_controllo_C3 è  diverso da  True , Almeno una delle seguenti { 
    //   *38,*  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  *54,* 14, Verifica che   *47,*  *34,*  il parametro SubClass_C2_parametro_P8 non sia  uguale a  *53,* 4
    //   } Verifica che   *51,*  *,*  il contatore SubClass_C2_contatore_Co10 non sia  minore di  *55,* 15
    //  } *83,*  Tutte le seguenti {
    //   Ricezione del  comando manuale   SubClass_C2_command_comm4   *77,*
    //   *68,* *35,*  se il controllo SubClass_C2_controllo_C9 non è  uguale a RossoGiallo *37,* e  se la variabile SubClass_C2_variabile_V9 è  diverso da  True  *37,* o  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False  *37,* o  se la variabile SubClass_C2_variabile_V9 è  uguale a  True , Almeno una delle seguenti { 
    //   *69,*  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
    //   *68,* *35,*  se il controllo SubClass_C2_controllo_C3 è  diverso da  True  *36,* o  se il timer SubClass_C2_timer_T3 è scaduto, Almeno una delle seguenti { 
    //   *69,* *35,*  se il controllo SubClass_C2_controllo_C3 è  uguale a  True  *36,* o  se il timer SubClass_C2_timer_T8 è scaduto, Solo una delle seguenti { 
    //   *69,*  se il controllo ConsDef  è  uguale a FALSE  *36,* o  se il timer SubClass_C2_timer_T5 non è scaduto, Solo una delle seguenti { 
    //   *36,*  se il timer SubClass_C2_timer_T9 è attivo o  se il controllo ConsDef  è  uguale a FALSE  *37,* e  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False  *35,* e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  True , Verifica che   *49,*  *,*  il timer SubClass_C2_timer_T9 sia attivo
    //   } Verifica che   *49,*  *,*  il timer SubClass_C2_timer_T8 non sia scaduto
    //   } Verifica che   *51,*  *,*  il contatore SubClass_C2_contatore_Co10 sia  minore di  *55,* 13
    //   } Verifica che   *48,*  *,*  il controllo SubClass_C2_controllo_C3 non sia  diverso da  True 
    //   } Verifica che   *48,*   il controllo ConsDef  sia  uguale a FALSE 
    //   } Verifica che   *51,*  *,*  il contatore SubClass_C2_contatore_Co10 non sia  uguale a  *53,* 11215
    //  } *83,*  Tutte le seguenti {
    //   Ricezione del  comando manuale   SubClass_C2_command_comm4   *77,*
    //   *68,* *36,*  se il timer SubClass_C2_timer_T5 è scaduto *34,* o  se il parametro SubClass_C2_parametro_P8 è  diverso da  *56,* 2 *38,* o  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  *56,* 12 o  se il controllo ConsDef  è  uguale a FALSE  *38,* e  se il contatore SubClass_C2_contatore_Co10 è  uguale a  *53,* 124, Almeno una delle seguenti { 
    //   *69,* *37,*  se la variabile SubClass_C2_variabile_V5 non è  diverso da  True  *38,* o  se il contatore SubClass_C2_contatore_Co10 è  minore di  *55,* 130 *35,* e  se il controllo SubClass_C2_controllo_C3 è  uguale a  False  *36,* o  se il timer SubClass_C2_timer_T5 è attivo *38,* e  se il contatore SubClass_C2_contatore_Co10 è  minore di  *55,* 11321 *38,* o  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  *56,* 125, Solo una delle seguenti { 
    //   *68,* *38,*  se il contatore SubClass_C2_contatore_Co10 è  uguale a  *53,* 13403, Almeno una delle seguenti { 
    //   *69,*  se il controllo ConsDef  è  uguale a FALSE  *34,* o  se il parametro SubClass_C2_parametro_P8 è  uguale a  *53,* 6 *37,* o  se la variabile SubClass_C2_variabile_V9 è  diverso da  True  *35,* o  se il controllo SubClass_C2_controllo_C9 è  uguale a RossoGiallo *38,* e  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  *56,* 13 *38,* o  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  *54,* 15, Solo una delle seguenti { 
    //   *67,*  se il controllo ConsDef  è  uguale a FALSE  *38,* o  se il contatore SubClass_C2_contatore_Co10 è  minore di  *55,* 14 *34,* o  se il parametro SubClass_C2_parametro_P8 non è  uguale a  *53,* 7 *38,* o  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  *54,* 1421 o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
    //   *67,* *36,*  se il timer SubClass_C2_timer_T7 non è scaduto, Tutte le seguenti { 
    //   *69,* *38,*  se il contatore SubClass_C2_contatore_Co10 non è  minore di  *55,* 11540 *36,* e  se il timer SubClass_C2_timer_T9 è scaduto *38,* o  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  *56,* 11321 *35,* e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  False  *36,* e  se il timer SubClass_C2_timer_T5 è attivo, Solo una delle seguenti { 
    //   *68,* *34,*  se il parametro SubClass_C2_parametro_P8 è  minore di  *55,* 8 *37,* e  se la variabile SubClass_C2_variabile_V9 non è  diverso da  True  *34,* e  se il parametro SubClass_C2_parametro_P8 è  minore di  *55,* 9 *36,* e  se il timer SubClass_C2_timer_T5 è scaduto *38,* e  se il contatore SubClass_C2_contatore_Co10 non è  uguale a  *53,* 13, Almeno una delle seguenti { 
    //   *36,*  se il timer SubClass_C2_timer_T5 non è scaduto *34,* o  se il parametro SubClass_C2_parametro_P8 è  uguale a  *53,* 6 *37,* o  se la variabile SubClass_C2_variabile_V9 non è  uguale a  True  *37,* e  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False  *38,* e  se il contatore SubClass_C2_contatore_Co10 è  uguale a  *53,* 135 *38,* o  se il contatore SubClass_C2_contatore_Co10 non è  maggiore di  *54,* 11403, Verifica che   *49,*  *,*  il timer SubClass_C2_timer_T5 non sia disattivo
    //   } Verifica che   *48,*   il controllo ConsDef  sia  uguale a FALSE 
    //   } Verifica che   *50,*  *,*  la variabile SubClass_C2_variabile_V5 sia  uguale a  False 
    //   } Verifica che   *49,*  *,*  il timer SubClass_C2_timer_T5 sia disattivo
    //   } Verifica che   *47,*  *34,*  il parametro SubClass_C2_parametro_P8 sia  uguale a  *53,* 10
    //   } Verifica che   *48,*   il controllo ConsDef  sia  uguale a FALSE 
    //   } Verifica che   *48,*  *,*  il controllo SubClass_C2_controllo_C9 non sia  diverso da RossoGiallo
    //   } Verifica che   *48,*  *,*  il controllo SubClass_C2_controllo_C9 non sia  diverso da RossoGiallo
    //   } Verifica che   *48,*  *,*  il controllo SubClass_C2_controllo_C3 non sia  uguale a  True 
    //  } *83,*  Tutte le seguenti {
    //   Ricezione del  comando manuale   SubClass_C2_command_comm4   *77,*
    //   *69,* *38,*  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  *54,* 13 *35,* e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  False  *35,* e  se il controllo SubClass_C2_controllo_C3 non è  diverso da  False  *38,* o  se il contatore SubClass_C2_contatore_Co10 è  uguale a  *53,* 13215 *36,* e  se il timer SubClass_C2_timer_T9 è disattivo *38,* e  se il contatore SubClass_C2_contatore_Co10 non è  minore di  *55,* 14, Solo una delle seguenti { 
    //   *67,* *36,*  se il timer SubClass_C2_timer_T5 è disattivo *38,* e  se il contatore SubClass_C2_contatore_Co10 è  diverso da  *56,* 14403 *34,* o  se il parametro SubClass_C2_parametro_P8 è  diverso da  *56,* 1 *35,* e  se il controllo SubClass_C2_controllo_C9 è  diverso da RossoGiallo *36,* o  se il timer SubClass_C2_timer_T9 non è scaduto, Tutte le seguenti { 
    //   *67,* *35,*  se il controllo SubClass_C2_controllo_C9 è  uguale a RossoGiallo *34,* e  se il parametro SubClass_C2_parametro_P8 è  maggiore di  *54,* 2 *35,* o  se il controllo SubClass_C2_controllo_C3 non è  diverso da  False  *37,* o  se la variabile SubClass_C2_variabile_V5 non è  diverso da  False  *36,* e  se il timer SubClass_C2_timer_T8 è attivo *36,* e  se il timer SubClass_C2_timer_T5 non è disattivo, Tutte le seguenti { 
    //   *67,* *36,*  se il timer SubClass_C2_timer_T3 è disattivo *35,* e  se il controllo SubClass_C2_controllo_C9 è  uguale a RossoGiallo *37,* e  se la variabile SubClass_C2_variabile_V5 non è  uguale a  False , Tutte le seguenti { 
    //   *67,* *36,*  se il timer SubClass_C2_timer_T5 è scaduto, Tutte le seguenti { 
    //   *69,* *34,*  se il parametro SubClass_C2_parametro_P8 non è  minore di  *55,* 5 *38,* e  se il contatore SubClass_C2_contatore_Co10 è  diverso da  *56,* 15215 *36,* o  se il timer SubClass_C2_timer_T5 non è scaduto *35,* e  se il controllo SubClass_C2_controllo_C9 è  diverso da RossoGiallo *38,* e  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  *54,* 12403, Solo una delle seguenti { 
    //   *67,* *38,*  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  *56,* 11215 *35,* o  se il controllo SubClass_C2_controllo_C3 è  diverso da  False  *35,* o  se il controllo SubClass_C2_controllo_C3 è  uguale a  True , Tutte le seguenti { 
    //   *34,*  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  *54,* 7 *34,* o  se il parametro SubClass_C2_parametro_P8 non è  minore di  *55,* 4 *38,* o  se il contatore SubClass_C2_contatore_Co10 è  uguale a  *53,* 13, Verifica che   *47,*  *34,*  il parametro SubClass_C2_parametro_P8 sia  maggiore di  *54,* 9
    //   } Verifica che   *47,*  *34,*  il parametro SubClass_C2_parametro_P8 non sia  minore di  *55,* 3
    //   } Verifica che   *51,*  *,*  il contatore SubClass_C2_contatore_Co10 non sia  maggiore di  *54,* 154
    //   } Verifica che   *48,*   il controllo ConsDef  sia  uguale a FALSE 
    //   } Verifica che   *47,*  *34,*  il parametro SubClass_C2_parametro_P8 non sia  uguale a  *53,* 7
    //   } Verifica che   *51,*  *,*  il contatore SubClass_C2_contatore_Co10 non sia  uguale a  *53,* 13
    //   } Verifica che   *50,*  *,*  la variabile SubClass_C2_variabile_V5 sia  diverso da  False 
    //   } Verifica che   *50,*  *,*  la variabile SubClass_C2_variabile_V9 non sia  uguale a  True 
    //  }
    //  }
    bool res_OrLogicOP_1 = false;
    bool res_AndLogicOP_2 = true;
    res_AndLogicOP_2 = (res_AndLogicOP_2 && L_P1__GetInEvent6(my_id));
    bool res_ImpliesLogicOp_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetInSubcl5(my_id) == true));
    if(res_NotLogicOP_4){
    bool res_ImpliesLogicOp_5 = true;
    if((Counter_GetValore(L_P1__GetSubcl36(my_id)) > 14u)){
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetParamSubcl8(my_id) == 4u));
    res_ImpliesLogicOp_5 = (res_ImpliesLogicOp_5 && res_NotLogicOP_6);
    }
    res_ImpliesLogicOp_3 = (res_ImpliesLogicOp_3 && res_ImpliesLogicOp_5);
    }
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_ImpliesLogicOp_3);
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (Counter_GetValore(L_P1__GetSubcl36(my_id)) < 15u));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_7);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_2);
    bool res_AndLogicOP_8 = true;
    res_AndLogicOP_8 = (res_AndLogicOP_8 && L_P1__GetInEvent6(my_id));
    bool res_ImpliesLogicOp_9 = true;
    bool res_OrLogicOP_10 = false;
    bool res_OrLogicOP_11 = false;
    bool res_AndLogicOP_12 = true;
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (L_P1__GetInSubcl6(my_id) == rossogiallo1));
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_NotLogicOP_13);
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1__GetSubcl28(my_id) == true));
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_NotLogicOP_14);
    
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_AndLogicOP_12);
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (L_P1__GetSubcl28(my_id) == false));
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_NotLogicOP_15);
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_OrLogicOP_11);
    res_OrLogicOP_10 = (res_OrLogicOP_10 || (L_P1__GetSubcl28(my_id) == true));
    
    if(res_OrLogicOP_10){
    bool res_OrLogicOP_16 = false;
    bool res_ImpliesLogicOp_17 = true;
    if((L_P1__GetInConsd1(my_id) == false)){
    bool res_XorLogicOP_18 = true;
    int xorIndex_res_XorLogicOP_18 = 0;
    bool res_ImpliesLogicOp_19 = true;
    bool res_OrLogicOP_20 = false;
    bool res_NotLogicOP_21 = true;
    res_NotLogicOP_21 = (res_NotLogicOP_21 && ! (L_P1__GetInSubcl5(my_id) == true));
    res_OrLogicOP_20 = (res_OrLogicOP_20 || res_NotLogicOP_21);
    res_OrLogicOP_20 = (res_OrLogicOP_20 || Timer_Scaduto(L_P1__GetSubcl31(my_id)));
    
    if(res_OrLogicOP_20){
    bool res_OrLogicOP_22 = false;
    bool res_ImpliesLogicOp_23 = true;
    bool res_OrLogicOP_24 = false;
    res_OrLogicOP_24 = (res_OrLogicOP_24 || (L_P1__GetInSubcl5(my_id) == true));
    res_OrLogicOP_24 = (res_OrLogicOP_24 || Timer_Scaduto(L_P1__GetSubcl34(my_id)));
    
    if(res_OrLogicOP_24){
    bool res_XorLogicOP_25 = true;
    int xorIndex_res_XorLogicOP_25 = 0;
    bool res_ImpliesLogicOp_26 = true;
    bool res_OrLogicOP_27 = false;
    res_OrLogicOP_27 = (res_OrLogicOP_27 || (L_P1__GetInConsd1(my_id) == false));
    bool res_NotLogicOP_28 = true;
    res_NotLogicOP_28 = (res_NotLogicOP_28 && ! Timer_Scaduto(L_P1__GetSubcl32(my_id)));
    res_OrLogicOP_27 = (res_OrLogicOP_27 || res_NotLogicOP_28);
    
    if(res_OrLogicOP_27){
    bool res_ImpliesLogicOp_29 = true;
    bool res_OrLogicOP_30 = false;
    res_OrLogicOP_30 = (res_OrLogicOP_30 || Timer_Attivo(L_P1__GetSubcl35(my_id)));
    bool res_AndLogicOP_31 = true;
    bool res_AndLogicOP_32 = true;
    res_AndLogicOP_32 = (res_AndLogicOP_32 && (L_P1__GetInConsd1(my_id) == false));
    bool res_NotLogicOP_33 = true;
    res_NotLogicOP_33 = (res_NotLogicOP_33 && ! (L_P1__GetSubcl28(my_id) == false));
    res_AndLogicOP_32 = (res_AndLogicOP_32 && res_NotLogicOP_33);
    
    res_AndLogicOP_31 = (res_AndLogicOP_31 && res_AndLogicOP_32);
    bool res_NotLogicOP_34 = true;
    res_NotLogicOP_34 = (res_NotLogicOP_34 && ! (L_P1__GetInSubcl5(my_id) == true));
    res_AndLogicOP_31 = (res_AndLogicOP_31 && res_NotLogicOP_34);
    
    res_OrLogicOP_30 = (res_OrLogicOP_30 || res_AndLogicOP_31);
    
    if(res_OrLogicOP_30){
    res_ImpliesLogicOp_29 = (res_ImpliesLogicOp_29 && Timer_Attivo(L_P1__GetSubcl35(my_id)));
    }
    res_ImpliesLogicOp_26 = (res_ImpliesLogicOp_26 && res_ImpliesLogicOp_29);
    }
    if(res_ImpliesLogicOp_26){
    xorIndex_res_XorLogicOP_25 = (xorIndex_res_XorLogicOP_25 + 1);
    }
    bool res_NotLogicOP_35 = true;
    res_NotLogicOP_35 = (res_NotLogicOP_35 && ! Timer_Scaduto(L_P1__GetSubcl34(my_id)));
    if(res_NotLogicOP_35){
    xorIndex_res_XorLogicOP_25 = (xorIndex_res_XorLogicOP_25 + 1);
    }
    
    res_XorLogicOP_25 = (res_XorLogicOP_25 && (xorIndex_res_XorLogicOP_25 == 1));
    res_ImpliesLogicOp_23 = (res_ImpliesLogicOp_23 && res_XorLogicOP_25);
    }
    res_OrLogicOP_22 = (res_OrLogicOP_22 || res_ImpliesLogicOp_23);
    res_OrLogicOP_22 = (res_OrLogicOP_22 || (Counter_GetValore(L_P1__GetSubcl36(my_id)) < 13u));
    
    res_ImpliesLogicOp_19 = (res_ImpliesLogicOp_19 && res_OrLogicOP_22);
    }
    if(res_ImpliesLogicOp_19){
    xorIndex_res_XorLogicOP_18 = (xorIndex_res_XorLogicOP_18 + 1);
    }
    bool res_NotLogicOP_36 = true;
    bool res_NotLogicOP_37 = true;
    res_NotLogicOP_37 = (res_NotLogicOP_37 && ! (L_P1__GetInSubcl5(my_id) == true));
    res_NotLogicOP_36 = (res_NotLogicOP_36 && ! res_NotLogicOP_37);
    if(res_NotLogicOP_36){
    xorIndex_res_XorLogicOP_18 = (xorIndex_res_XorLogicOP_18 + 1);
    }
    
    res_XorLogicOP_18 = (res_XorLogicOP_18 && (xorIndex_res_XorLogicOP_18 == 1));
    res_ImpliesLogicOp_17 = (res_ImpliesLogicOp_17 && res_XorLogicOP_18);
    }
    res_OrLogicOP_16 = (res_OrLogicOP_16 || res_ImpliesLogicOp_17);
    res_OrLogicOP_16 = (res_OrLogicOP_16 || (L_P1__GetInConsd1(my_id) == false));
    
    res_ImpliesLogicOp_9 = (res_ImpliesLogicOp_9 && res_OrLogicOP_16);
    }
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_ImpliesLogicOp_9);
    bool res_NotLogicOP_38 = true;
    res_NotLogicOP_38 = (res_NotLogicOP_38 && ! (Counter_GetValore(L_P1__GetSubcl36(my_id)) == 11215u));
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_38);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_8);
    bool res_AndLogicOP_39 = true;
    res_AndLogicOP_39 = (res_AndLogicOP_39 && L_P1__GetInEvent6(my_id));
    bool res_ImpliesLogicOp_40 = true;
    bool res_OrLogicOP_41 = false;
    bool res_OrLogicOP_42 = false;
    bool res_OrLogicOP_43 = false;
    res_OrLogicOP_43 = (res_OrLogicOP_43 || Timer_Scaduto(L_P1__GetSubcl32(my_id)));
    bool res_NotLogicOP_44 = true;
    res_NotLogicOP_44 = (res_NotLogicOP_44 && ! (L_P1__GetParamSubcl8(my_id) == 2u));
    res_OrLogicOP_43 = (res_OrLogicOP_43 || res_NotLogicOP_44);
    
    res_OrLogicOP_42 = (res_OrLogicOP_42 || res_OrLogicOP_43);
    bool res_NotLogicOP_45 = true;
    bool res_NotLogicOP_46 = true;
    res_NotLogicOP_46 = (res_NotLogicOP_46 && ! (Counter_GetValore(L_P1__GetSubcl36(my_id)) == 12u));
    res_NotLogicOP_45 = (res_NotLogicOP_45 && ! res_NotLogicOP_46);
    res_OrLogicOP_42 = (res_OrLogicOP_42 || res_NotLogicOP_45);
    
    res_OrLogicOP_41 = (res_OrLogicOP_41 || res_OrLogicOP_42);
    bool res_AndLogicOP_47 = true;
    res_AndLogicOP_47 = (res_AndLogicOP_47 && (L_P1__GetInConsd1(my_id) == false));
    res_AndLogicOP_47 = (res_AndLogicOP_47 && (Counter_GetValore(L_P1__GetSubcl36(my_id)) == 124u));
    
    res_OrLogicOP_41 = (res_OrLogicOP_41 || res_AndLogicOP_47);
    
    if(res_OrLogicOP_41){
    bool res_OrLogicOP_48 = false;
    bool res_ImpliesLogicOp_49 = true;
    bool res_OrLogicOP_50 = false;
    bool res_OrLogicOP_51 = false;
    bool res_OrLogicOP_52 = false;
    bool res_NotLogicOP_53 = true;
    bool res_NotLogicOP_54 = true;
    res_NotLogicOP_54 = (res_NotLogicOP_54 && ! (L_P1__GetSubcl27(my_id) == true));
    res_NotLogicOP_53 = (res_NotLogicOP_53 && ! res_NotLogicOP_54);
    res_OrLogicOP_52 = (res_OrLogicOP_52 || res_NotLogicOP_53);
    bool res_AndLogicOP_55 = true;
    res_AndLogicOP_55 = (res_AndLogicOP_55 && (Counter_GetValore(L_P1__GetSubcl36(my_id)) < 130u));
    res_AndLogicOP_55 = (res_AndLogicOP_55 && (L_P1__GetInSubcl5(my_id) == false));
    
    res_OrLogicOP_52 = (res_OrLogicOP_52 || res_AndLogicOP_55);
    
    res_OrLogicOP_51 = (res_OrLogicOP_51 || res_OrLogicOP_52);
    bool res_AndLogicOP_56 = true;
    res_AndLogicOP_56 = (res_AndLogicOP_56 && Timer_Attivo(L_P1__GetSubcl32(my_id)));
    res_AndLogicOP_56 = (res_AndLogicOP_56 && (Counter_GetValore(L_P1__GetSubcl36(my_id)) < 11321u));
    
    res_OrLogicOP_51 = (res_OrLogicOP_51 || res_AndLogicOP_56);
    
    res_OrLogicOP_50 = (res_OrLogicOP_50 || res_OrLogicOP_51);
    bool res_NotLogicOP_57 = true;
    bool res_NotLogicOP_58 = true;
    res_NotLogicOP_58 = (res_NotLogicOP_58 && ! (Counter_GetValore(L_P1__GetSubcl36(my_id)) == 125u));
    res_NotLogicOP_57 = (res_NotLogicOP_57 && ! res_NotLogicOP_58);
    res_OrLogicOP_50 = (res_OrLogicOP_50 || res_NotLogicOP_57);
    
    if(res_OrLogicOP_50){
    bool res_XorLogicOP_59 = true;
    int xorIndex_res_XorLogicOP_59 = 0;
    bool res_ImpliesLogicOp_60 = true;
    if((Counter_GetValore(L_P1__GetSubcl36(my_id)) == 13403u)){
    bool res_OrLogicOP_61 = false;
    bool res_ImpliesLogicOp_62 = true;
    bool res_OrLogicOP_63 = false;
    bool res_OrLogicOP_64 = false;
    bool res_OrLogicOP_65 = false;
    bool res_OrLogicOP_66 = false;
    res_OrLogicOP_66 = (res_OrLogicOP_66 || (L_P1__GetInConsd1(my_id) == false));
    res_OrLogicOP_66 = (res_OrLogicOP_66 || (L_P1__GetParamSubcl8(my_id) == 6u));
    
    res_OrLogicOP_65 = (res_OrLogicOP_65 || res_OrLogicOP_66);
    bool res_NotLogicOP_67 = true;
    res_NotLogicOP_67 = (res_NotLogicOP_67 && ! (L_P1__GetSubcl28(my_id) == true));
    res_OrLogicOP_65 = (res_OrLogicOP_65 || res_NotLogicOP_67);
    
    res_OrLogicOP_64 = (res_OrLogicOP_64 || res_OrLogicOP_65);
    bool res_AndLogicOP_68 = true;
    res_AndLogicOP_68 = (res_AndLogicOP_68 && (L_P1__GetInSubcl6(my_id) == rossogiallo1));
    bool res_NotLogicOP_69 = true;
    bool res_NotLogicOP_70 = true;
    res_NotLogicOP_70 = (res_NotLogicOP_70 && ! (Counter_GetValore(L_P1__GetSubcl36(my_id)) == 13u));
    res_NotLogicOP_69 = (res_NotLogicOP_69 && ! res_NotLogicOP_70);
    res_AndLogicOP_68 = (res_AndLogicOP_68 && res_NotLogicOP_69);
    
    res_OrLogicOP_64 = (res_OrLogicOP_64 || res_AndLogicOP_68);
    
    res_OrLogicOP_63 = (res_OrLogicOP_63 || res_OrLogicOP_64);
    res_OrLogicOP_63 = (res_OrLogicOP_63 || (Counter_GetValore(L_P1__GetSubcl36(my_id)) > 15u));
    
    if(res_OrLogicOP_63){
    bool res_XorLogicOP_71 = true;
    int xorIndex_res_XorLogicOP_71 = 0;
    bool res_ImpliesLogicOp_72 = true;
    bool res_OrLogicOP_73 = false;
    bool res_OrLogicOP_74 = false;
    bool res_OrLogicOP_75 = false;
    bool res_OrLogicOP_76 = false;
    res_OrLogicOP_76 = (res_OrLogicOP_76 || (L_P1__GetInConsd1(my_id) == false));
    res_OrLogicOP_76 = (res_OrLogicOP_76 || (Counter_GetValore(L_P1__GetSubcl36(my_id)) < 14u));
    
    res_OrLogicOP_75 = (res_OrLogicOP_75 || res_OrLogicOP_76);
    bool res_NotLogicOP_77 = true;
    res_NotLogicOP_77 = (res_NotLogicOP_77 && ! (L_P1__GetParamSubcl8(my_id) == 7u));
    res_OrLogicOP_75 = (res_OrLogicOP_75 || res_NotLogicOP_77);
    
    res_OrLogicOP_74 = (res_OrLogicOP_74 || res_OrLogicOP_75);
    res_OrLogicOP_74 = (res_OrLogicOP_74 || (Counter_GetValore(L_P1__GetSubcl36(my_id)) > 1421u));
    
    res_OrLogicOP_73 = (res_OrLogicOP_73 || res_OrLogicOP_74);
    res_OrLogicOP_73 = (res_OrLogicOP_73 || (L_P1__GetInConsd1(my_id) == false));
    
    if(res_OrLogicOP_73){
    bool res_AndLogicOP_78 = true;
    bool res_ImpliesLogicOp_79 = true;
    bool res_NotLogicOP_80 = true;
    res_NotLogicOP_80 = (res_NotLogicOP_80 && ! Timer_Scaduto(L_P1__GetSubcl33(my_id)));
    if(res_NotLogicOP_80){
    bool res_AndLogicOP_81 = true;
    bool res_ImpliesLogicOp_82 = true;
    bool res_OrLogicOP_83 = false;
    bool res_AndLogicOP_84 = true;
    bool res_NotLogicOP_85 = true;
    res_NotLogicOP_85 = (res_NotLogicOP_85 && ! (Counter_GetValore(L_P1__GetSubcl36(my_id)) < 11540u));
    res_AndLogicOP_84 = (res_AndLogicOP_84 && res_NotLogicOP_85);
    res_AndLogicOP_84 = (res_AndLogicOP_84 && Timer_Scaduto(L_P1__GetSubcl35(my_id)));
    
    res_OrLogicOP_83 = (res_OrLogicOP_83 || res_AndLogicOP_84);
    bool res_AndLogicOP_86 = true;
    bool res_AndLogicOP_87 = true;
    bool res_NotLogicOP_88 = true;
    bool res_NotLogicOP_89 = true;
    res_NotLogicOP_89 = (res_NotLogicOP_89 && ! (Counter_GetValore(L_P1__GetSubcl36(my_id)) == 11321u));
    res_NotLogicOP_88 = (res_NotLogicOP_88 && ! res_NotLogicOP_89);
    res_AndLogicOP_87 = (res_AndLogicOP_87 && res_NotLogicOP_88);
    bool res_NotLogicOP_90 = true;
    res_NotLogicOP_90 = (res_NotLogicOP_90 && ! (L_P1__GetInSubcl5(my_id) == false));
    res_AndLogicOP_87 = (res_AndLogicOP_87 && res_NotLogicOP_90);
    
    res_AndLogicOP_86 = (res_AndLogicOP_86 && res_AndLogicOP_87);
    res_AndLogicOP_86 = (res_AndLogicOP_86 && Timer_Attivo(L_P1__GetSubcl32(my_id)));
    
    res_OrLogicOP_83 = (res_OrLogicOP_83 || res_AndLogicOP_86);
    
    if(res_OrLogicOP_83){
    bool res_XorLogicOP_91 = true;
    int xorIndex_res_XorLogicOP_91 = 0;
    bool res_ImpliesLogicOp_92 = true;
    bool res_AndLogicOP_93 = true;
    bool res_AndLogicOP_94 = true;
    bool res_AndLogicOP_95 = true;
    bool res_AndLogicOP_96 = true;
    res_AndLogicOP_96 = (res_AndLogicOP_96 && (L_P1__GetParamSubcl8(my_id) < 8u));
    bool res_NotLogicOP_97 = true;
    bool res_NotLogicOP_98 = true;
    res_NotLogicOP_98 = (res_NotLogicOP_98 && ! (L_P1__GetSubcl28(my_id) == true));
    res_NotLogicOP_97 = (res_NotLogicOP_97 && ! res_NotLogicOP_98);
    res_AndLogicOP_96 = (res_AndLogicOP_96 && res_NotLogicOP_97);
    
    res_AndLogicOP_95 = (res_AndLogicOP_95 && res_AndLogicOP_96);
    res_AndLogicOP_95 = (res_AndLogicOP_95 && (L_P1__GetParamSubcl8(my_id) < 9u));
    
    res_AndLogicOP_94 = (res_AndLogicOP_94 && res_AndLogicOP_95);
    res_AndLogicOP_94 = (res_AndLogicOP_94 && Timer_Scaduto(L_P1__GetSubcl32(my_id)));
    
    res_AndLogicOP_93 = (res_AndLogicOP_93 && res_AndLogicOP_94);
    bool res_NotLogicOP_99 = true;
    res_NotLogicOP_99 = (res_NotLogicOP_99 && ! (Counter_GetValore(L_P1__GetSubcl36(my_id)) == 13u));
    res_AndLogicOP_93 = (res_AndLogicOP_93 && res_NotLogicOP_99);
    
    if(res_AndLogicOP_93){
    bool res_ImpliesLogicOp_100 = true;
    bool res_OrLogicOP_101 = false;
    bool res_OrLogicOP_102 = false;
    bool res_OrLogicOP_103 = false;
    bool res_NotLogicOP_104 = true;
    res_NotLogicOP_104 = (res_NotLogicOP_104 && ! Timer_Scaduto(L_P1__GetSubcl32(my_id)));
    res_OrLogicOP_103 = (res_OrLogicOP_103 || res_NotLogicOP_104);
    res_OrLogicOP_103 = (res_OrLogicOP_103 || (L_P1__GetParamSubcl8(my_id) == 6u));
    
    res_OrLogicOP_102 = (res_OrLogicOP_102 || res_OrLogicOP_103);
    bool res_AndLogicOP_105 = true;
    bool res_AndLogicOP_106 = true;
    bool res_NotLogicOP_107 = true;
    res_NotLogicOP_107 = (res_NotLogicOP_107 && ! (L_P1__GetSubcl28(my_id) == true));
    res_AndLogicOP_106 = (res_AndLogicOP_106 && res_NotLogicOP_107);
    bool res_NotLogicOP_108 = true;
    res_NotLogicOP_108 = (res_NotLogicOP_108 && ! (L_P1__GetSubcl28(my_id) == false));
    res_AndLogicOP_106 = (res_AndLogicOP_106 && res_NotLogicOP_108);
    
    res_AndLogicOP_105 = (res_AndLogicOP_105 && res_AndLogicOP_106);
    res_AndLogicOP_105 = (res_AndLogicOP_105 && (Counter_GetValore(L_P1__GetSubcl36(my_id)) == 135u));
    
    res_OrLogicOP_102 = (res_OrLogicOP_102 || res_AndLogicOP_105);
    
    res_OrLogicOP_101 = (res_OrLogicOP_101 || res_OrLogicOP_102);
    bool res_NotLogicOP_109 = true;
    res_NotLogicOP_109 = (res_NotLogicOP_109 && ! (Counter_GetValore(L_P1__GetSubcl36(my_id)) > 11403u));
    res_OrLogicOP_101 = (res_OrLogicOP_101 || res_NotLogicOP_109);
    
    if(res_OrLogicOP_101){
    bool res_NotLogicOP_110 = true;
    res_NotLogicOP_110 = (res_NotLogicOP_110 && ! Timer_Disattivo(L_P1__GetSubcl32(my_id)));
    res_ImpliesLogicOp_100 = (res_ImpliesLogicOp_100 && res_NotLogicOP_110);
    }
    res_ImpliesLogicOp_92 = (res_ImpliesLogicOp_92 && res_ImpliesLogicOp_100);
    }
    if(res_ImpliesLogicOp_92){
    xorIndex_res_XorLogicOP_91 = (xorIndex_res_XorLogicOP_91 + 1);
    }
    if((L_P1__GetInConsd1(my_id) == false)){
    xorIndex_res_XorLogicOP_91 = (xorIndex_res_XorLogicOP_91 + 1);
    }
    
    res_XorLogicOP_91 = (res_XorLogicOP_91 && (xorIndex_res_XorLogicOP_91 == 1));
    res_ImpliesLogicOp_82 = (res_ImpliesLogicOp_82 && res_XorLogicOP_91);
    }
    res_AndLogicOP_81 = (res_AndLogicOP_81 && res_ImpliesLogicOp_82);
    res_AndLogicOP_81 = (res_AndLogicOP_81 && (L_P1__GetSubcl27(my_id) == false));
    
    res_ImpliesLogicOp_79 = (res_ImpliesLogicOp_79 && res_AndLogicOP_81);
    }
    res_AndLogicOP_78 = (res_AndLogicOP_78 && res_ImpliesLogicOp_79);
    res_AndLogicOP_78 = (res_AndLogicOP_78 && Timer_Disattivo(L_P1__GetSubcl32(my_id)));
    
    res_ImpliesLogicOp_72 = (res_ImpliesLogicOp_72 && res_AndLogicOP_78);
    }
    if(res_ImpliesLogicOp_72){
    xorIndex_res_XorLogicOP_71 = (xorIndex_res_XorLogicOP_71 + 1);
    }
    if((L_P1__GetParamSubcl8(my_id) == 10u)){
    xorIndex_res_XorLogicOP_71 = (xorIndex_res_XorLogicOP_71 + 1);
    }
    
    res_XorLogicOP_71 = (res_XorLogicOP_71 && (xorIndex_res_XorLogicOP_71 == 1));
    res_ImpliesLogicOp_62 = (res_ImpliesLogicOp_62 && res_XorLogicOP_71);
    }
    res_OrLogicOP_61 = (res_OrLogicOP_61 || res_ImpliesLogicOp_62);
    res_OrLogicOP_61 = (res_OrLogicOP_61 || (L_P1__GetInConsd1(my_id) == false));
    
    res_ImpliesLogicOp_60 = (res_ImpliesLogicOp_60 && res_OrLogicOP_61);
    }
    if(res_ImpliesLogicOp_60){
    xorIndex_res_XorLogicOP_59 = (xorIndex_res_XorLogicOP_59 + 1);
    }
    bool res_NotLogicOP_111 = true;
    bool res_NotLogicOP_112 = true;
    res_NotLogicOP_112 = (res_NotLogicOP_112 && ! (L_P1__GetInSubcl6(my_id) == rossogiallo1));
    res_NotLogicOP_111 = (res_NotLogicOP_111 && ! res_NotLogicOP_112);
    if(res_NotLogicOP_111){
    xorIndex_res_XorLogicOP_59 = (xorIndex_res_XorLogicOP_59 + 1);
    }
    
    res_XorLogicOP_59 = (res_XorLogicOP_59 && (xorIndex_res_XorLogicOP_59 == 1));
    res_ImpliesLogicOp_49 = (res_ImpliesLogicOp_49 && res_XorLogicOP_59);
    }
    res_OrLogicOP_48 = (res_OrLogicOP_48 || res_ImpliesLogicOp_49);
    bool res_NotLogicOP_113 = true;
    bool res_NotLogicOP_114 = true;
    res_NotLogicOP_114 = (res_NotLogicOP_114 && ! (L_P1__GetInSubcl6(my_id) == rossogiallo1));
    res_NotLogicOP_113 = (res_NotLogicOP_113 && ! res_NotLogicOP_114);
    res_OrLogicOP_48 = (res_OrLogicOP_48 || res_NotLogicOP_113);
    
    res_ImpliesLogicOp_40 = (res_ImpliesLogicOp_40 && res_OrLogicOP_48);
    }
    res_AndLogicOP_39 = (res_AndLogicOP_39 && res_ImpliesLogicOp_40);
    bool res_NotLogicOP_115 = true;
    res_NotLogicOP_115 = (res_NotLogicOP_115 && ! (L_P1__GetInSubcl5(my_id) == true));
    res_AndLogicOP_39 = (res_AndLogicOP_39 && res_NotLogicOP_115);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_39);
    bool res_AndLogicOP_116 = true;
    res_AndLogicOP_116 = (res_AndLogicOP_116 && L_P1__GetInEvent6(my_id));
    bool res_ImpliesLogicOp_117 = true;
    bool res_OrLogicOP_118 = false;
    bool res_AndLogicOP_119 = true;
    bool res_AndLogicOP_120 = true;
    res_AndLogicOP_120 = (res_AndLogicOP_120 && (Counter_GetValore(L_P1__GetSubcl36(my_id)) > 13u));
    bool res_NotLogicOP_121 = true;
    res_NotLogicOP_121 = (res_NotLogicOP_121 && ! (L_P1__GetInSubcl5(my_id) == false));
    res_AndLogicOP_120 = (res_AndLogicOP_120 && res_NotLogicOP_121);
    
    res_AndLogicOP_119 = (res_AndLogicOP_119 && res_AndLogicOP_120);
    bool res_NotLogicOP_122 = true;
    bool res_NotLogicOP_123 = true;
    res_NotLogicOP_123 = (res_NotLogicOP_123 && ! (L_P1__GetInSubcl5(my_id) == false));
    res_NotLogicOP_122 = (res_NotLogicOP_122 && ! res_NotLogicOP_123);
    res_AndLogicOP_119 = (res_AndLogicOP_119 && res_NotLogicOP_122);
    
    res_OrLogicOP_118 = (res_OrLogicOP_118 || res_AndLogicOP_119);
    bool res_AndLogicOP_124 = true;
    bool res_AndLogicOP_125 = true;
    res_AndLogicOP_125 = (res_AndLogicOP_125 && (Counter_GetValore(L_P1__GetSubcl36(my_id)) == 13215u));
    res_AndLogicOP_125 = (res_AndLogicOP_125 && Timer_Disattivo(L_P1__GetSubcl35(my_id)));
    
    res_AndLogicOP_124 = (res_AndLogicOP_124 && res_AndLogicOP_125);
    bool res_NotLogicOP_126 = true;
    res_NotLogicOP_126 = (res_NotLogicOP_126 && ! (Counter_GetValore(L_P1__GetSubcl36(my_id)) < 14u));
    res_AndLogicOP_124 = (res_AndLogicOP_124 && res_NotLogicOP_126);
    
    res_OrLogicOP_118 = (res_OrLogicOP_118 || res_AndLogicOP_124);
    
    if(res_OrLogicOP_118){
    bool res_XorLogicOP_127 = true;
    int xorIndex_res_XorLogicOP_127 = 0;
    bool res_ImpliesLogicOp_128 = true;
    bool res_OrLogicOP_129 = false;
    bool res_OrLogicOP_130 = false;
    bool res_AndLogicOP_131 = true;
    res_AndLogicOP_131 = (res_AndLogicOP_131 && Timer_Disattivo(L_P1__GetSubcl32(my_id)));
    bool res_NotLogicOP_132 = true;
    res_NotLogicOP_132 = (res_NotLogicOP_132 && ! (Counter_GetValore(L_P1__GetSubcl36(my_id)) == 14403u));
    res_AndLogicOP_131 = (res_AndLogicOP_131 && res_NotLogicOP_132);
    
    res_OrLogicOP_130 = (res_OrLogicOP_130 || res_AndLogicOP_131);
    bool res_AndLogicOP_133 = true;
    bool res_NotLogicOP_134 = true;
    res_NotLogicOP_134 = (res_NotLogicOP_134 && ! (L_P1__GetParamSubcl8(my_id) == 1u));
    res_AndLogicOP_133 = (res_AndLogicOP_133 && res_NotLogicOP_134);
    bool res_NotLogicOP_135 = true;
    res_NotLogicOP_135 = (res_NotLogicOP_135 && ! (L_P1__GetInSubcl6(my_id) == rossogiallo1));
    res_AndLogicOP_133 = (res_AndLogicOP_133 && res_NotLogicOP_135);
    
    res_OrLogicOP_130 = (res_OrLogicOP_130 || res_AndLogicOP_133);
    
    res_OrLogicOP_129 = (res_OrLogicOP_129 || res_OrLogicOP_130);
    bool res_NotLogicOP_136 = true;
    res_NotLogicOP_136 = (res_NotLogicOP_136 && ! Timer_Scaduto(L_P1__GetSubcl35(my_id)));
    res_OrLogicOP_129 = (res_OrLogicOP_129 || res_NotLogicOP_136);
    
    if(res_OrLogicOP_129){
    bool res_AndLogicOP_137 = true;
    bool res_ImpliesLogicOp_138 = true;
    bool res_OrLogicOP_139 = false;
    bool res_OrLogicOP_140 = false;
    bool res_AndLogicOP_141 = true;
    res_AndLogicOP_141 = (res_AndLogicOP_141 && (L_P1__GetInSubcl6(my_id) == rossogiallo1));
    res_AndLogicOP_141 = (res_AndLogicOP_141 && (L_P1__GetParamSubcl8(my_id) > 2u));
    
    res_OrLogicOP_140 = (res_OrLogicOP_140 || res_AndLogicOP_141);
    bool res_NotLogicOP_142 = true;
    bool res_NotLogicOP_143 = true;
    res_NotLogicOP_143 = (res_NotLogicOP_143 && ! (L_P1__GetInSubcl5(my_id) == false));
    res_NotLogicOP_142 = (res_NotLogicOP_142 && ! res_NotLogicOP_143);
    res_OrLogicOP_140 = (res_OrLogicOP_140 || res_NotLogicOP_142);
    
    res_OrLogicOP_139 = (res_OrLogicOP_139 || res_OrLogicOP_140);
    bool res_AndLogicOP_144 = true;
    bool res_AndLogicOP_145 = true;
    bool res_NotLogicOP_146 = true;
    bool res_NotLogicOP_147 = true;
    res_NotLogicOP_147 = (res_NotLogicOP_147 && ! (L_P1__GetSubcl27(my_id) == false));
    res_NotLogicOP_146 = (res_NotLogicOP_146 && ! res_NotLogicOP_147);
    res_AndLogicOP_145 = (res_AndLogicOP_145 && res_NotLogicOP_146);
    res_AndLogicOP_145 = (res_AndLogicOP_145 && Timer_Attivo(L_P1__GetSubcl34(my_id)));
    
    res_AndLogicOP_144 = (res_AndLogicOP_144 && res_AndLogicOP_145);
    bool res_NotLogicOP_148 = true;
    res_NotLogicOP_148 = (res_NotLogicOP_148 && ! Timer_Disattivo(L_P1__GetSubcl32(my_id)));
    res_AndLogicOP_144 = (res_AndLogicOP_144 && res_NotLogicOP_148);
    
    res_OrLogicOP_139 = (res_OrLogicOP_139 || res_AndLogicOP_144);
    
    if(res_OrLogicOP_139){
    bool res_AndLogicOP_149 = true;
    bool res_ImpliesLogicOp_150 = true;
    bool res_AndLogicOP_151 = true;
    bool res_AndLogicOP_152 = true;
    res_AndLogicOP_152 = (res_AndLogicOP_152 && Timer_Disattivo(L_P1__GetSubcl31(my_id)));
    res_AndLogicOP_152 = (res_AndLogicOP_152 && (L_P1__GetInSubcl6(my_id) == rossogiallo1));
    
    res_AndLogicOP_151 = (res_AndLogicOP_151 && res_AndLogicOP_152);
    bool res_NotLogicOP_153 = true;
    res_NotLogicOP_153 = (res_NotLogicOP_153 && ! (L_P1__GetSubcl27(my_id) == false));
    res_AndLogicOP_151 = (res_AndLogicOP_151 && res_NotLogicOP_153);
    
    if(res_AndLogicOP_151){
    bool res_AndLogicOP_154 = true;
    bool res_ImpliesLogicOp_155 = true;
    if(Timer_Scaduto(L_P1__GetSubcl32(my_id))){
    bool res_AndLogicOP_156 = true;
    bool res_ImpliesLogicOp_157 = true;
    bool res_OrLogicOP_158 = false;
    bool res_AndLogicOP_159 = true;
    bool res_NotLogicOP_160 = true;
    res_NotLogicOP_160 = (res_NotLogicOP_160 && ! (L_P1__GetParamSubcl8(my_id) < 5u));
    res_AndLogicOP_159 = (res_AndLogicOP_159 && res_NotLogicOP_160);
    bool res_NotLogicOP_161 = true;
    res_NotLogicOP_161 = (res_NotLogicOP_161 && ! (Counter_GetValore(L_P1__GetSubcl36(my_id)) == 15215u));
    res_AndLogicOP_159 = (res_AndLogicOP_159 && res_NotLogicOP_161);
    
    res_OrLogicOP_158 = (res_OrLogicOP_158 || res_AndLogicOP_159);
    bool res_AndLogicOP_162 = true;
    bool res_AndLogicOP_163 = true;
    bool res_NotLogicOP_164 = true;
    res_NotLogicOP_164 = (res_NotLogicOP_164 && ! Timer_Scaduto(L_P1__GetSubcl32(my_id)));
    res_AndLogicOP_163 = (res_AndLogicOP_163 && res_NotLogicOP_164);
    bool res_NotLogicOP_165 = true;
    res_NotLogicOP_165 = (res_NotLogicOP_165 && ! (L_P1__GetInSubcl6(my_id) == rossogiallo1));
    res_AndLogicOP_163 = (res_AndLogicOP_163 && res_NotLogicOP_165);
    
    res_AndLogicOP_162 = (res_AndLogicOP_162 && res_AndLogicOP_163);
    res_AndLogicOP_162 = (res_AndLogicOP_162 && (Counter_GetValore(L_P1__GetSubcl36(my_id)) > 12403u));
    
    res_OrLogicOP_158 = (res_OrLogicOP_158 || res_AndLogicOP_162);
    
    if(res_OrLogicOP_158){
    bool res_XorLogicOP_166 = true;
    int xorIndex_res_XorLogicOP_166 = 0;
    bool res_ImpliesLogicOp_167 = true;
    bool res_OrLogicOP_168 = false;
    bool res_OrLogicOP_169 = false;
    bool res_NotLogicOP_170 = true;
    bool res_NotLogicOP_171 = true;
    res_NotLogicOP_171 = (res_NotLogicOP_171 && ! (Counter_GetValore(L_P1__GetSubcl36(my_id)) == 11215u));
    res_NotLogicOP_170 = (res_NotLogicOP_170 && ! res_NotLogicOP_171);
    res_OrLogicOP_169 = (res_OrLogicOP_169 || res_NotLogicOP_170);
    bool res_NotLogicOP_172 = true;
    res_NotLogicOP_172 = (res_NotLogicOP_172 && ! (L_P1__GetInSubcl5(my_id) == false));
    res_OrLogicOP_169 = (res_OrLogicOP_169 || res_NotLogicOP_172);
    
    res_OrLogicOP_168 = (res_OrLogicOP_168 || res_OrLogicOP_169);
    res_OrLogicOP_168 = (res_OrLogicOP_168 || (L_P1__GetInSubcl5(my_id) == true));
    
    if(res_OrLogicOP_168){
    bool res_ImpliesLogicOp_173 = true;
    bool res_OrLogicOP_174 = false;
    bool res_OrLogicOP_175 = false;
    bool res_NotLogicOP_176 = true;
    res_NotLogicOP_176 = (res_NotLogicOP_176 && ! (L_P1__GetParamSubcl8(my_id) > 7u));
    res_OrLogicOP_175 = (res_OrLogicOP_175 || res_NotLogicOP_176);
    bool res_NotLogicOP_177 = true;
    res_NotLogicOP_177 = (res_NotLogicOP_177 && ! (L_P1__GetParamSubcl8(my_id) < 4u));
    res_OrLogicOP_175 = (res_OrLogicOP_175 || res_NotLogicOP_177);
    
    res_OrLogicOP_174 = (res_OrLogicOP_174 || res_OrLogicOP_175);
    res_OrLogicOP_174 = (res_OrLogicOP_174 || (Counter_GetValore(L_P1__GetSubcl36(my_id)) == 13u));
    
    if(res_OrLogicOP_174){
    res_ImpliesLogicOp_173 = (res_ImpliesLogicOp_173 && (L_P1__GetParamSubcl8(my_id) > 9u));
    }
    res_ImpliesLogicOp_167 = (res_ImpliesLogicOp_167 && res_ImpliesLogicOp_173);
    }
    if(res_ImpliesLogicOp_167){
    xorIndex_res_XorLogicOP_166 = (xorIndex_res_XorLogicOP_166 + 1);
    }
    bool res_NotLogicOP_178 = true;
    res_NotLogicOP_178 = (res_NotLogicOP_178 && ! (L_P1__GetParamSubcl8(my_id) < 3u));
    if(res_NotLogicOP_178){
    xorIndex_res_XorLogicOP_166 = (xorIndex_res_XorLogicOP_166 + 1);
    }
    
    res_XorLogicOP_166 = (res_XorLogicOP_166 && (xorIndex_res_XorLogicOP_166 == 1));
    res_ImpliesLogicOp_157 = (res_ImpliesLogicOp_157 && res_XorLogicOP_166);
    }
    res_AndLogicOP_156 = (res_AndLogicOP_156 && res_ImpliesLogicOp_157);
    bool res_NotLogicOP_179 = true;
    res_NotLogicOP_179 = (res_NotLogicOP_179 && ! (Counter_GetValore(L_P1__GetSubcl36(my_id)) > 154u));
    res_AndLogicOP_156 = (res_AndLogicOP_156 && res_NotLogicOP_179);
    
    res_ImpliesLogicOp_155 = (res_ImpliesLogicOp_155 && res_AndLogicOP_156);
    }
    res_AndLogicOP_154 = (res_AndLogicOP_154 && res_ImpliesLogicOp_155);
    res_AndLogicOP_154 = (res_AndLogicOP_154 && (L_P1__GetInConsd1(my_id) == false));
    
    res_ImpliesLogicOp_150 = (res_ImpliesLogicOp_150 && res_AndLogicOP_154);
    }
    res_AndLogicOP_149 = (res_AndLogicOP_149 && res_ImpliesLogicOp_150);
    bool res_NotLogicOP_180 = true;
    res_NotLogicOP_180 = (res_NotLogicOP_180 && ! (L_P1__GetParamSubcl8(my_id) == 7u));
    res_AndLogicOP_149 = (res_AndLogicOP_149 && res_NotLogicOP_180);
    
    res_ImpliesLogicOp_138 = (res_ImpliesLogicOp_138 && res_AndLogicOP_149);
    }
    res_AndLogicOP_137 = (res_AndLogicOP_137 && res_ImpliesLogicOp_138);
    bool res_NotLogicOP_181 = true;
    res_NotLogicOP_181 = (res_NotLogicOP_181 && ! (Counter_GetValore(L_P1__GetSubcl36(my_id)) == 13u));
    res_AndLogicOP_137 = (res_AndLogicOP_137 && res_NotLogicOP_181);
    
    res_ImpliesLogicOp_128 = (res_ImpliesLogicOp_128 && res_AndLogicOP_137);
    }
    if(res_ImpliesLogicOp_128){
    xorIndex_res_XorLogicOP_127 = (xorIndex_res_XorLogicOP_127 + 1);
    }
    bool res_NotLogicOP_182 = true;
    res_NotLogicOP_182 = (res_NotLogicOP_182 && ! (L_P1__GetSubcl27(my_id) == false));
    if(res_NotLogicOP_182){
    xorIndex_res_XorLogicOP_127 = (xorIndex_res_XorLogicOP_127 + 1);
    }
    
    res_XorLogicOP_127 = (res_XorLogicOP_127 && (xorIndex_res_XorLogicOP_127 == 1));
    res_ImpliesLogicOp_117 = (res_ImpliesLogicOp_117 && res_XorLogicOP_127);
    }
    res_AndLogicOP_116 = (res_AndLogicOP_116 && res_ImpliesLogicOp_117);
    bool res_NotLogicOP_183 = true;
    res_NotLogicOP_183 = (res_NotLogicOP_183 && ! (L_P1__GetSubcl28(my_id) == true));
    res_AndLogicOP_116 = (res_AndLogicOP_116 && res_NotLogicOP_183);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_116);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_1);
    
    if(res_AndLogicOP_2){
    L_P1__SetOutEvent7(my_id,LDS_MANCMD_PROCESSED);
    }
    else if(res_AndLogicOP_8){
    L_P1__SetOutEvent7(my_id,LDS_MANCMD_PROCESSED);
    }
    else if(res_AndLogicOP_39){
    L_P1__SetOutEvent7(my_id,LDS_MANCMD_PROCESSED);
    }
    else if(res_AndLogicOP_116){
    L_P1__SetOutEvent7(my_id,LDS_MANCMD_PROCESSED);
    }
    else{
    
    }
    
    
    return res_AndLogicOP_0;
}


/*
    CNL corrispondente:
     {  Nessuna  }
*/
static inline bool L_P1__Guard14(instance_id_t const my_id)
{
    return true;
}


// ********** Definizione effetti **********

/*
    CNL corrispondente:
    
     {
     Nessuna 
     }
*/
static inline void L_P1__Effec2(instance_id_t const my_id)
{
    
}


/*
    CNL corrispondente:
    
    {
    
    Comanda al campo MainClass_C1 di SubClass_C2_lista_L9
     di eseguire  commento: {113,}  MainClass_C1_command_comm2    commento: {79,}
    }
*/
static inline void L_P1__Effec3(instance_id_t const my_id)
{
    
    //  Comanda al campo MainClass_C1 di SubClass_C2_lista_L9
    //   di eseguire  *113,*  MainClass_C1_command_comm2
    for (index_t i = 0; i < L_P1__GetParamSubcl7Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl7(my_id,i);
    
    L_P1__SetCAEvent2(it.mainc32,true);
    scheduler_NotifyCommand(L_P1_C1_TO_GLOBAL(it.mainc32));
    }
}


/*
    CNL corrispondente:
    
    {
    
    Comanda al campo MainClass_C1 di SubClass_C2_lista_L9
     di eseguire  commento: {113,}  MainClass_C1_command_comm2    commento: {79,}
    }
*/
static inline void L_P1__Effec4(instance_id_t const my_id)
{
    
    //  Comanda al campo MainClass_C1 di SubClass_C2_lista_L9
    //   di eseguire  *113,*  MainClass_C1_command_comm2
    for (index_t i = 0; i < L_P1__GetParamSubcl7Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl7(my_id,i);
    
    L_P1__SetCAEvent2(it.mainc32,true);
    scheduler_NotifyCommand(L_P1_C1_TO_GLOBAL(it.mainc32));
    }
}


/*
    CNL corrispondente:
    
    {
    
    Comanda al campo MainClass_C1 di SubClass_C2_lista_L9
     di eseguire  commento: {113,}  MainClass_C1_command_comm2    commento: {79,}
    }
*/
static inline void L_P1__Effec5(instance_id_t const my_id)
{
    
    //  Comanda al campo MainClass_C1 di SubClass_C2_lista_L9
    //   di eseguire  *113,*  MainClass_C1_command_comm2
    for (index_t i = 0; i < L_P1__GetParamSubcl7Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl7(my_id,i);
    
    L_P1__SetCAEvent2(it.mainc32,true);
    scheduler_NotifyCommand(L_P1_C1_TO_GLOBAL(it.mainc32));
    }
}


/*
    CNL corrispondente:
     {Comanda al campo MainClass_C1 di SubClass_C2_lista_L9
     di eseguire  commento: {113,}  MainClass_C1_command_comm2    commento: {79,} }
*/
static inline void L_P1__Effec6(instance_id_t const my_id)
{
    
    //  Comanda al campo MainClass_C1 di SubClass_C2_lista_L9
    //   di eseguire  *113,*  MainClass_C1_command_comm2
    for (index_t i = 0; i < L_P1__GetParamSubcl7Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl7(my_id,i);
    
    L_P1__SetCAEvent2(it.mainc32,true);
    scheduler_NotifyCommand(L_P1_C1_TO_GLOBAL(it.mainc32));
    }
}


/*
    CNL corrispondente:
     {Comanda al campo MainClass_C1 di SubClass_C2_lista_L9
     di eseguire  commento: {113,}  MainClass_C1_command_comm2    commento: {79,} }
*/
static inline void L_P1__Effec7(instance_id_t const my_id)
{
    
    //  Comanda al campo MainClass_C1 di SubClass_C2_lista_L9
    //   di eseguire  *113,*  MainClass_C1_command_comm2
    for (index_t i = 0; i < L_P1__GetParamSubcl7Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl7(my_id,i);
    
    L_P1__SetCAEvent2(it.mainc32,true);
    scheduler_NotifyCommand(L_P1_C1_TO_GLOBAL(it.mainc32));
    }
}


/*
    CNL corrispondente:
     {Comanda al campo MainClass_C1 di SubClass_C2_lista_L9
     di eseguire  commento: {113,}  MainClass_C1_command_comm2    commento: {79,} }
*/
static inline void L_P1__Effec8(instance_id_t const my_id)
{
    
    //  Comanda al campo MainClass_C1 di SubClass_C2_lista_L9
    //   di eseguire  *113,*  MainClass_C1_command_comm2
    for (index_t i = 0; i < L_P1__GetParamSubcl7Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl7(my_id,i);
    
    L_P1__SetCAEvent2(it.mainc32,true);
    scheduler_NotifyCommand(L_P1_C1_TO_GLOBAL(it.mainc32));
    }
}


/*
    CNL corrispondente:
     {Comanda al campo MainClass_C1 di SubClass_C2_lista_L9
     di eseguire  commento: {113,}  MainClass_C1_command_comm2    commento: {79,} }
*/
static inline void L_P1__Effec9(instance_id_t const my_id)
{
    
    //  Comanda al campo MainClass_C1 di SubClass_C2_lista_L9
    //   di eseguire  *113,*  MainClass_C1_command_comm2
    for (index_t i = 0; i < L_P1__GetParamSubcl7Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl7(my_id,i);
    
    L_P1__SetCAEvent2(it.mainc32,true);
    scheduler_NotifyCommand(L_P1_C1_TO_GLOBAL(it.mainc32));
    }
}


/*
    CNL corrispondente:
    
    {
    
    Comanda al campo MainClass_C1 di SubClass_C2_lista_L9
     di eseguire  commento: {113,}  MainClass_C1_command_comm2    commento: {79,}
    }
*/
static inline void L_P1__Effec10(instance_id_t const my_id)
{
    
    //  Comanda al campo MainClass_C1 di SubClass_C2_lista_L9
    //   di eseguire  *113,*  MainClass_C1_command_comm2
    for (index_t i = 0; i < L_P1__GetParamSubcl7Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl7(my_id,i);
    
    L_P1__SetCAEvent2(it.mainc32,true);
    scheduler_NotifyCommand(L_P1_C1_TO_GLOBAL(it.mainc32));
    }
}


/*
    CNL corrispondente:
     {Comanda al campo MainClass_C1 di SubClass_C2_lista_L9
     di eseguire  commento: {113,}  MainClass_C1_command_comm2    commento: {79,} }
*/
static inline void L_P1__Effec11(instance_id_t const my_id)
{
    
    //  Comanda al campo MainClass_C1 di SubClass_C2_lista_L9
    //   di eseguire  *113,*  MainClass_C1_command_comm2
    for (index_t i = 0; i < L_P1__GetParamSubcl7Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl7(my_id,i);
    
    L_P1__SetCAEvent2(it.mainc32,true);
    scheduler_NotifyCommand(L_P1_C1_TO_GLOBAL(it.mainc32));
    }
}


/*
    CNL corrispondente:
     {Comanda al campo MainClass_C1 di SubClass_C2_lista_L9
     di eseguire  commento: {113,}  MainClass_C1_command_comm2    commento: {79,} }
*/
static inline void L_P1__Effec12(instance_id_t const my_id)
{
    
    //  Comanda al campo MainClass_C1 di SubClass_C2_lista_L9
    //   di eseguire  *113,*  MainClass_C1_command_comm2
    for (index_t i = 0; i < L_P1__GetParamSubcl7Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl7(my_id,i);
    
    L_P1__SetCAEvent2(it.mainc32,true);
    scheduler_NotifyCommand(L_P1_C1_TO_GLOBAL(it.mainc32));
    }
}


/*
    CNL corrispondente:
     {Comanda al campo MainClass_C1 di SubClass_C2_lista_L9
     di eseguire  commento: {113,}  MainClass_C1_command_comm2    commento: {79,} }
*/
static inline void L_P1__Effec13(instance_id_t const my_id)
{
    
    //  Comanda al campo MainClass_C1 di SubClass_C2_lista_L9
    //   di eseguire  *113,*  MainClass_C1_command_comm2
    for (index_t i = 0; i < L_P1__GetParamSubcl7Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl7(my_id,i);
    
    L_P1__SetCAEvent2(it.mainc32,true);
    scheduler_NotifyCommand(L_P1_C1_TO_GLOBAL(it.mainc32));
    }
}


/*
    CNL corrispondente:
     {Comanda al campo MainClass_C1 di SubClass_C2_lista_L9
     di eseguire  commento: {113,}  MainClass_C1_command_comm2    commento: {79,} }
*/
static inline void L_P1__Effec14(instance_id_t const my_id)
{
    
    //  Comanda al campo MainClass_C1 di SubClass_C2_lista_L9
    //   di eseguire  *113,*  MainClass_C1_command_comm2
    for (index_t i = 0; i < L_P1__GetParamSubcl7Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl7(my_id,i);
    
    L_P1__SetCAEvent2(it.mainc32,true);
    scheduler_NotifyCommand(L_P1_C1_TO_GLOBAL(it.mainc32));
    }
}



// ********** Definizione metodi **********

// Metodi standard

void L_P1_C2_Init(instance_id_t const my_id)
{
    // init variabili di stato
    L_P1__SetStato3(my_id, C2_St_Stato);
    L_P1__SetSubcl17(my_id, 0);
    L_P1__SetSubcl19(my_id, false);
    L_P1__SetSubcl21(my_id, 0);
    L_P1__SetSubcl23(my_id, false);
    L_P1__SetSubcl25(my_id, rosso);
    L_P1__SetSubcl26(my_id, rosso);
    L_P1__SetSubcl27(my_id, false);
    L_P1__SetSubcl28(my_id, false);
    // init controlli precedenti
    L_P1__SetSubcl10(my_id, true);
    L_P1__SetSubcl12(my_id, rossogiallo);
    L_P1__SetSubcl14(my_id, false);
    L_P1__SetSubcl16(my_id, false);
    // init Timer e Counter
    Timer_AggmInit(L_P1__GetSubcl29(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl29_ID);
    Timer_Init(L_P1__GetSubcl29(my_id), 4000);
    Timer_AggmInit(L_P1__GetSubcl30(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl30_ID);
    Timer_Init(L_P1__GetSubcl30(my_id), 4000);
    Timer_AggmInit(L_P1__GetSubcl31(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl31_ID);
    Timer_Init(L_P1__GetSubcl31(my_id), 3000);
    Timer_AggmInit(L_P1__GetSubcl32(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl32_ID);
    Timer_Init(L_P1__GetSubcl32(my_id), 45000);
    Timer_AggmInit(L_P1__GetSubcl33(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl33_ID);
    Timer_Init(L_P1__GetSubcl33(my_id), 4403000);
    Timer_AggmInit(L_P1__GetSubcl34(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl34_ID);
    Timer_Init(L_P1__GetSubcl34(my_id), 5215000);
    Timer_AggmInit(L_P1__GetSubcl35(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl35_ID);
    Timer_Init(L_P1__GetSubcl35(my_id), 3000);
    Counter_AggmInit(L_P1__GetSubcl36(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl36_ID);
    Counter_Init(L_P1__GetSubcl36(my_id));
    // init response
    L_P1_C2_SetResponse(my_id, LDS_SCHED_NOP);

    // transizione iniziale
    if(L_P1__Guard2(my_id)) {
        L_P1_C2_SetState(my_id, C2_St_state);
	L_P1__Effec2(my_id);
    } else {
        STOP_EXECUTION(LOGIC_ERROR);
    }
    // init variabili precedenti
    L_P1__SetSubcl18(my_id, L_P1__GetSubcl17(my_id));
    L_P1__SetSubcl20(my_id, L_P1__GetSubcl19(my_id));
    L_P1__SetSubcl22(my_id, L_P1__GetSubcl21(my_id));
    L_P1__SetSubcl24(my_id, L_P1__GetSubcl23(my_id));
}

void L_P1_C2_Exec(instance_id_t const my_id, Phase const p)
{
    L_P1_C2_SetResponse(my_id, LDS_SCHED_NOP);
    switch (p) {

    case LDS_PHASE_MANUAL:
        // Reset risposte ai comandi manuali
        L_P1_C2_InitCmdsResponse(my_id);
	L_P1_C2_SetExpectedCmdsResponse(my_id, L_P1_C2_GetState(my_id));
        switch (L_P1_C2_GetState(my_id)) {

        case C2_St_state1:
                { } // fine transizioni da state1 nella fase LDS_PHASE_MANUAL
            break;

        case C2_St_state:
                { } // fine transizioni da state nella fase LDS_PHASE_MANUAL
            break;

        case C2_St_state3:
            if (L_P1__Guard13(my_id)) {
                L_P1_C2_SetState(my_id, C2_St_state2);
                L_P1__Effec13(my_id);				
            }
            else
                { } // fine transizioni da state3 nella fase LDS_PHASE_MANUAL
            break;

        case C2_St_state2:
                { } // fine transizioni da state2 nella fase LDS_PHASE_MANUAL
            break;

        default:
            STOP_EXECUTION(LOGIC_ERROR);
            break;  // Needed for MISRA C syntactic compliance
        } // switch sugli stati chiuso
        break;
 

    case LDS_PHASE_STATE:

        switch (L_P1_C2_GetState(my_id)) {

        case C2_St_state1:
            if (L_P1__Guard4(my_id)) {
                L_P1_C2_SetState(my_id, C2_St_state1);
                L_P1__Effec4(my_id);				
            }
            else
                {STOP_EXECUTION(LOGIC_ERROR); } // fine transizioni da state1 nella fase LDS_PHASE_STATE
            break;

        case C2_St_state:
            if (L_P1__Guard3(my_id)) {
                L_P1_C2_SetState(my_id, C2_St_state);
                L_P1__Effec3(my_id);				
            }
            else
                {STOP_EXECUTION(LOGIC_ERROR); } // fine transizioni da state nella fase LDS_PHASE_STATE
            break;

        case C2_St_state3:
            if (L_P1__Guard11(my_id)) {
                L_P1_C2_SetState(my_id, C2_St_state);
                L_P1__Effec11(my_id);				
            }
            else if (L_P1__Guard12(my_id)) {
                L_P1_C2_SetState(my_id, C2_St_state1);
                L_P1__Effec12(my_id);				
            }
            else if (L_P1__Guard14(my_id)) {
                L_P1_C2_SetState(my_id, C2_St_state3);
                L_P1__Effec14(my_id);				
            }
            else if (L_P1__Guard10(my_id)) {
                L_P1_C2_SetState(my_id, C2_St_state3);
                L_P1__Effec10(my_id);				
            }
            else
                {STOP_EXECUTION(LOGIC_ERROR); } // fine transizioni da state3 nella fase LDS_PHASE_STATE
            break;

        case C2_St_state2:
            if (L_P1__Guard9(my_id)) {
                L_P1_C2_SetState(my_id, C2_St_state3);
                L_P1__Effec9(my_id);				
            }
            else if (L_P1__Guard6(my_id)) {
                L_P1_C2_SetState(my_id, C2_St_state3);
                L_P1__Effec6(my_id);				
            }
            else if (L_P1__Guard7(my_id)) {
                L_P1_C2_SetState(my_id, C2_St_state3);
                L_P1__Effec7(my_id);				
            }
            else if (L_P1__Guard8(my_id)) {
                L_P1_C2_SetState(my_id, C2_St_state);
                L_P1__Effec8(my_id);				
            }
            else if (L_P1__Guard5(my_id)) {
                L_P1_C2_SetState(my_id, C2_St_state2);
                L_P1__Effec5(my_id);				
            }
            else
                {STOP_EXECUTION(LOGIC_ERROR); } // fine transizioni da state2 nella fase LDS_PHASE_STATE
            break;

        default:
            STOP_EXECUTION(LOGIC_ERROR);
            break;  // Needed for MISRA C syntactic compliance
        } // switch sugli stati chiuso
        break;


    case LDS_PHASE_AUTO:
        break;
 
    default:
        STOP_EXECUTION(LOGIC_ERROR);
        break;
    }
}

ExecResponse L_P1_C2_GExec(global_id_t const proc_id, Phase const p)
{
    CHECK_LT(GLOBAL_TO_L_P1_C2(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C2(proc_id);
    L_P1_C2_Exec(my_id, p);
    return L_P1_C2_GetResponse(my_id);
}

void L_P1_C2_GTick(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C2(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C2(proc_id);
    Timer_Exec(L_P1__GetSubcl29(my_id));
    Timer_Exec(L_P1__GetSubcl30(my_id));
    Timer_Exec(L_P1__GetSubcl31(my_id));
    Timer_Exec(L_P1__GetSubcl32(my_id));
    Timer_Exec(L_P1__GetSubcl33(my_id));
    Timer_Exec(L_P1__GetSubcl34(my_id));
    Timer_Exec(L_P1__GetSubcl35(my_id));
}

void L_P1_C2_GSetSafe(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C2(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C2(proc_id);
    L_P1__SetOutSubcl(my_id, true);
    L_P1__SetOutSubcl1(my_id, avvio);
    L_P1__SetOutSubcl2(my_id, false);
    L_P1__SetOutSubcl3(my_id, rossogiallo);
    L_P1__SetOutSubcl4(my_id, false);
}

void L_P1_C2_GUpdatePrev(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C2(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C2(proc_id);
    L_P1__SetSubcl10(my_id, L_P1__GetInSubcl9(my_id));
    L_P1__SetSubcl12(my_id, L_P1__GetInSubcl11(my_id));
    L_P1__SetSubcl14(my_id, L_P1__GetInSubcl13(my_id));
    L_P1__SetSubcl16(my_id, L_P1__GetInSubcl15(my_id));
    L_P1__SetSubcl18(my_id, L_P1__GetSubcl17(my_id));
    L_P1__SetSubcl20(my_id, L_P1__GetSubcl19(my_id));
    L_P1__SetSubcl22(my_id, L_P1__GetSubcl21(my_id));
    L_P1__SetSubcl24(my_id, L_P1__GetSubcl23(my_id));
}

// ********** Definizione macro **********

// Macro di effetto

/*
    CNL corrispondente:
    
    {  se il controllo ConsDef  è  uguale a FALSE , commento: {72,}Azzera il contatore SubClass_C2_contatore_Co10
    
     ,altrimenti  commento: {66,} Assegna al comando SubClass_C2_comando_C7 il valore RossoGialloxVerdex
    
    
     commento: {36,}  se il timer SubClass_C2_timer_T8 è attivo commento: {35,} e  se il controllo SubClass_C2_controllo_C3 non è  diverso da  False  commento: {35,} o  se il controllo SubClass_C2_controllo_C3 è  diverso da  False  commento: {35,} e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  False  commento: {36,} e  se il timer SubClass_C2_timer_T9 è disattivo, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V9 il valore  True 
    
       
     commento: {45,}  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  diverso da  commento: {56,} 11 commento: {34,} e  se il parametro SubClass_C2_parametro_P8 è  maggiore di  commento: {54,} 9 e  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  True , commento: {66,} Assegna al comando SubClass_C2_comando_C6 il valore  True 
    
     ,altrimenti  commento: {71,}Decrementa il contatore SubClass_C2_contatore_Co10
    
    
     commento: {34,}  se il parametro SubClass_C2_parametro_P8 è  uguale a  commento: {53,} 1 commento: {35,} o  se il controllo SubClass_C2_controllo_C9 è  diverso da RossoGiallo, commento: {66,} Assegna al comando SubClass_C2_comando_C7 il valore RossoGialloxVerdex
    
       
    
    }
*/
void L_P1__Macro6(instance_id_t const my_id )
{
//  se il controllo ConsDef  è  uguale a FALSE , *72,*Azzera il contatore SubClass_C2_contatore_Co10
    // ,altrimenti  *66,* Assegna al comando SubClass_C2_comando_C7 il valore RossoGialloxVerdex
    if((L_P1__GetInConsd1(my_id) == false)){
    
    Counter_Res(L_P1__GetSubcl36(my_id));
    }else{
    
    L_P1__SetOutSubcl3(my_id,rossogiallo);
    }
    //  *36,*  se il timer SubClass_C2_timer_T8 è attivo *35,* e  se il controllo SubClass_C2_controllo_C3 non è  diverso da  False  *35,* o  se il controllo SubClass_C2_controllo_C3 è  diverso da  False  *35,* e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  False  *36,* e  se il timer SubClass_C2_timer_T9 è disattivo, *67,* Assegna alla variabile SubClass_C2_variabile_V9 il valore  True
    bool res_OrLogicOP_0 = false;
    bool res_AndLogicOP_1 = true;
    res_AndLogicOP_1 = (res_AndLogicOP_1 && Timer_Attivo(L_P1__GetSubcl34(my_id)));
    bool res_NotLogicOP_2 = true;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__GetInSubcl5(my_id) == false));
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! res_NotLogicOP_3);
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_2);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_1);
    bool res_AndLogicOP_4 = true;
    bool res_AndLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetInSubcl5(my_id) == false));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_6);
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetInSubcl5(my_id) == false));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_7);
    
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_AndLogicOP_5);
    res_AndLogicOP_4 = (res_AndLogicOP_4 && Timer_Disattivo(L_P1__GetSubcl35(my_id)));
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_4);
    
    if(res_OrLogicOP_0){
    
    L_P1__SetSubcl28(my_id,true);
    }
    //  *45,*  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  diverso da  *56,* 11 *34,* e  se il parametro SubClass_C2_parametro_P8 è  maggiore di  *54,* 9 e  se il controllo ConsDef  è  uguale a FALSE  *35,* e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  True , *66,* Assegna al comando SubClass_C2_comando_C6 il valore  True 
    // ,altrimenti  *71,*Decrementa il contatore SubClass_C2_contatore_Co10
    bool res_AndLogicOP_8 = true;
    bool res_AndLogicOP_9 = true;
    bool res_AndLogicOP_10 = true;
    bool res_ForAllPredicate_11 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl7Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl7(my_id,i);
    bool res_ImpliesLogicOp_12 = true;
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (Counter_GetValore(L_P1__GetMainc31(it.mainc32)) == 11u));
    res_ImpliesLogicOp_12 = (res_ImpliesLogicOp_12 && res_NotLogicOP_13);
    res_ForAllPredicate_11 = res_ImpliesLogicOp_12;
    if(!res_ForAllPredicate_11) {break;}
    }
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_ForAllPredicate_11);
    res_AndLogicOP_10 = (res_AndLogicOP_10 && (L_P1__GetParamSubcl8(my_id) > 9u));
    
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_AndLogicOP_10);
    res_AndLogicOP_9 = (res_AndLogicOP_9 && (L_P1__GetInConsd1(my_id) == false));
    
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_AndLogicOP_9);
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1__GetInSubcl5(my_id) == true));
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_14);
    
    if(res_AndLogicOP_8){
    
    L_P1__SetOutSubcl2(my_id,true);
    }else{
    
    Counter_Decr(L_P1__GetSubcl36(my_id));
    }
    //  *34,*  se il parametro SubClass_C2_parametro_P8 è  uguale a  *53,* 1 *35,* o  se il controllo SubClass_C2_controllo_C9 è  diverso da RossoGiallo, *66,* Assegna al comando SubClass_C2_comando_C7 il valore RossoGialloxVerdex
    bool res_OrLogicOP_15 = false;
    res_OrLogicOP_15 = (res_OrLogicOP_15 || (L_P1__GetParamSubcl8(my_id) == 1u));
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (L_P1__GetInSubcl6(my_id) == rossogiallo1));
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_NotLogicOP_16);
    
    if(res_OrLogicOP_15){
    
    L_P1__SetOutSubcl3(my_id,rossogiallo);
    }
}

/*
    CNL corrispondente:
    
    { commento: {38,}  se il contatore SubClass_C2_contatore_Co10 è  diverso da  commento: {56,} 1103 commento: {38,} o  se il contatore SubClass_C2_contatore_Co10 è  minore di  commento: {55,} 15215 commento: {38,} o  se il contatore SubClass_C2_contatore_Co10 non è  uguale a  commento: {53,} 13 commento: {35,} e  se il controllo SubClass_C2_controllo_C9 è  diverso da RossoGiallo o  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE , commento: {66,} Assegna al comando SubClass_C2_comando_C2 il valore avvio
    
       
      se il controllo ConsDef  è  uguale a FALSE  commento: {37,} o  se la variabile SubClass_C2_variabile_V5 è  diverso da  True  commento: {36,} o  se il timer SubClass_C2_timer_T5 non è scaduto commento: {38,} e  se il contatore SubClass_C2_contatore_Co10 è  diverso da  commento: {56,} 1240 commento: {35,} e  se il controllo SubClass_C2_controllo_C9 è  uguale a RossoGiallo commento: {36,} o  se il timer SubClass_C2_timer_T5 non è attivo, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V9 il valore  False 
    
       
    
    }
*/
void L_P1__Macro7(instance_id_t const my_id )
{
//  *38,*  se il contatore SubClass_C2_contatore_Co10 è  diverso da  *56,* 1103 *38,* o  se il contatore SubClass_C2_contatore_Co10 è  minore di  *55,* 15215 *38,* o  se il contatore SubClass_C2_contatore_Co10 non è  uguale a  *53,* 13 *35,* e  se il controllo SubClass_C2_controllo_C9 è  diverso da RossoGiallo o  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE , *66,* Assegna al comando SubClass_C2_comando_C2 il valore avvio
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (Counter_GetValore(L_P1__GetSubcl36(my_id)) == 1103u));
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_NotLogicOP_4);
    res_OrLogicOP_3 = (res_OrLogicOP_3 || (Counter_GetValore(L_P1__GetSubcl36(my_id)) < 15215u));
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    bool res_AndLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (Counter_GetValore(L_P1__GetSubcl36(my_id)) == 13u));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_6);
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetInSubcl6(my_id) == rossogiallo1));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_7);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_5);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_OrLogicOP_2);
    res_OrLogicOP_1 = (res_OrLogicOP_1 || (L_P1__GetInConsd1(my_id) == false));
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    res_OrLogicOP_0 = (res_OrLogicOP_0 || (L_P1__GetInConsd1(my_id) == false));
    
    if(res_OrLogicOP_0){
    
    L_P1__SetOutSubcl1(my_id,avvio);
    }
    //  se il controllo ConsDef  è  uguale a FALSE  *37,* o  se la variabile SubClass_C2_variabile_V5 è  diverso da  True  *36,* o  se il timer SubClass_C2_timer_T5 non è scaduto *38,* e  se il contatore SubClass_C2_contatore_Co10 è  diverso da  *56,* 1240 *35,* e  se il controllo SubClass_C2_controllo_C9 è  uguale a RossoGiallo *36,* o  se il timer SubClass_C2_timer_T5 non è attivo, *67,* Assegna alla variabile SubClass_C2_variabile_V9 il valore  False
    bool res_OrLogicOP_8 = false;
    bool res_OrLogicOP_9 = false;
    bool res_OrLogicOP_10 = false;
    res_OrLogicOP_10 = (res_OrLogicOP_10 || (L_P1__GetInConsd1(my_id) == false));
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (L_P1__GetSubcl27(my_id) == true));
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_NotLogicOP_11);
    
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_OrLogicOP_10);
    bool res_AndLogicOP_12 = true;
    bool res_AndLogicOP_13 = true;
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! Timer_Scaduto(L_P1__GetSubcl32(my_id)));
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_NotLogicOP_14);
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (Counter_GetValore(L_P1__GetSubcl36(my_id)) == 1240u));
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_NotLogicOP_15);
    
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_AndLogicOP_13);
    res_AndLogicOP_12 = (res_AndLogicOP_12 && (L_P1__GetInSubcl6(my_id) == rossogiallo1));
    
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_AndLogicOP_12);
    
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_OrLogicOP_9);
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! Timer_Attivo(L_P1__GetSubcl32(my_id)));
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_NotLogicOP_16);
    
    if(res_OrLogicOP_8){
    
    L_P1__SetSubcl28(my_id,false);
    }
}


// Macro di verifica

/*
    CNL corrispondente:
     
    { commento: {63,}  se la macro  SubClass_C2_macrova_M6 ( con argomento_a2   uguale a Rosso ,argomento_a6   uguale a Rosso ,argomento_a10   uguale a RossoGiallo  e argomento_a7   uguale a c75Giallo )   è  uguale a  True  commento: {40,} , Solo una delle seguenti { 
     commento: {61,} commento: {35,}  se il controllo SubClass_C2_controllo_C3 è  diverso da  True  o  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} o  se il contatore SubClass_C2_contatore_Co10 non è  uguale a  commento: {53,} 144 e  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
     commento: {36,}  se il timer SubClass_C2_timer_T5 è disattivo commento: {37,} o  se la variabile SubClass_C2_variabile_V5 è  uguale a  True  commento: {38,} e  se il contatore SubClass_C2_contatore_Co10 non è  minore di  commento: {55,} 13032 commento: {36,} o  se il timer SubClass_C2_timer_T7 è disattivo commento: {38,} e  se il contatore SubClass_C2_contatore_Co10 è  diverso da  commento: {56,} 1415, Verifica che   commento: {47,50,51,}  commento: {34,}  il parametro SubClass_C2_parametro_P8 sia  uguale a  commento: {53,} 3
     commento: {104,} e  che  commento: {,}  il contatore SubClass_C2_contatore_Co10 non sia  diverso da  commento: {56,} 15
     commento: {104,} e  che  commento: {34,}  il parametro SubClass_C2_parametro_P8 non sia  diverso da  commento: {56,} 4
     commento: {104,} e  che  commento: {34,}  il parametro SubClass_C2_parametro_P8 non sia  diverso da  commento: {56,} 5
     commento: {104,} o  che  commento: {,}  la variabile SubClass_C2_variabile_V9 non sia  uguale a  True 
     commento: {104,} o  che  commento: {38,}  il contatore SubClass_C2_contatore_Co10 non sia  maggiore di  commento: {54,} 13
    
    
     } Verifica che   commento: {48,51,}  commento: {,}  il contatore SubClass_C2_contatore_Co10 non sia  maggiore di  commento: {54,} 11
     commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
    
    
     } Verifica che   commento: {48,49,}  commento: {,}  il controllo SubClass_C2_controllo_C9 sia  diverso da RossoGiallo
     commento: {104,} o  che  commento: {,}  il timer SubClass_C2_timer_T3 non sia disattivo
     commento: {104,} o  che  commento: {36,}  il timer SubClass_C2_timer_T5 non sia disattivo
    
    
    }
*/
bool L_P1__Macro13(instance_id_t const my_id )
{
bool res_AndLogicOP_0 = true;
    
    //  *63,*  se la macro  SubClass_C2_macrova_M6 ( con argomento_a2   uguale a Rosso ,argomento_a6   uguale a Rosso ,argomento_a10   uguale a RossoGiallo  e argomento_a7   uguale a c75Giallo )   è  uguale a  True  *40,* , Solo una delle seguenti { 
    //   *61,* *35,*  se il controllo SubClass_C2_controllo_C3 è  diverso da  True  o  se il controllo ConsDef  è  uguale a FALSE  *38,* o  se il contatore SubClass_C2_contatore_Co10 non è  uguale a  *53,* 144 e  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
    //   *36,*  se il timer SubClass_C2_timer_T5 è disattivo *37,* o  se la variabile SubClass_C2_variabile_V5 è  uguale a  True  *38,* e  se il contatore SubClass_C2_contatore_Co10 non è  minore di  *55,* 13032 *36,* o  se il timer SubClass_C2_timer_T7 è disattivo *38,* e  se il contatore SubClass_C2_contatore_Co10 è  diverso da  *56,* 1415, Verifica che   *47,50,51,*  *34,*  il parametro SubClass_C2_parametro_P8 sia  uguale a  *53,* 3
    //   *104,* e  che  *,*  il contatore SubClass_C2_contatore_Co10 non sia  diverso da  *56,* 15
    //   *104,* e  che  *34,*  il parametro SubClass_C2_parametro_P8 non sia  diverso da  *56,* 4
    //   *104,* e  che  *34,*  il parametro SubClass_C2_parametro_P8 non sia  diverso da  *56,* 5
    //   *104,* o  che  *,*  la variabile SubClass_C2_variabile_V9 non sia  uguale a  True 
    //   *104,* o  che  *38,*  il contatore SubClass_C2_contatore_Co10 non sia  maggiore di  *54,* 13
    //   } Verifica che   *48,51,*  *,*  il contatore SubClass_C2_contatore_Co10 non sia  maggiore di  *54,* 11
    //   *104,* o  che   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* o  che   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* o  che   il controllo ConsDef  sia  uguale a FALSE 
    //   }
    bool res_ImpliesLogicOp_1 = true;
    if((L_P1__Macro11(my_id,rossogiallo1,rosso,rosso,c75giallo) == true)){
    bool res_XorLogicOP_2 = true;
    int xorIndex_res_XorLogicOP_2 = 0;
    bool res_ImpliesLogicOp_3 = true;
    bool res_OrLogicOP_4 = false;
    bool res_OrLogicOP_5 = false;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetInSubcl5(my_id) == true));
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_NotLogicOP_6);
    res_OrLogicOP_5 = (res_OrLogicOP_5 || (L_P1__GetInConsd1(my_id) == false));
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_OrLogicOP_5);
    bool res_AndLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (Counter_GetValore(L_P1__GetSubcl36(my_id)) == 144u));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_8);
    res_AndLogicOP_7 = (res_AndLogicOP_7 && (L_P1__GetInConsd1(my_id) == false));
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_AndLogicOP_7);
    
    if(res_OrLogicOP_4){
    bool res_ImpliesLogicOp_9 = true;
    bool res_OrLogicOP_10 = false;
    bool res_OrLogicOP_11 = false;
    res_OrLogicOP_11 = (res_OrLogicOP_11 || Timer_Disattivo(L_P1__GetSubcl32(my_id)));
    bool res_AndLogicOP_12 = true;
    res_AndLogicOP_12 = (res_AndLogicOP_12 && (L_P1__GetSubcl27(my_id) == true));
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (Counter_GetValore(L_P1__GetSubcl36(my_id)) < 13032u));
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_NotLogicOP_13);
    
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_AndLogicOP_12);
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_OrLogicOP_11);
    bool res_AndLogicOP_14 = true;
    res_AndLogicOP_14 = (res_AndLogicOP_14 && Timer_Disattivo(L_P1__GetSubcl33(my_id)));
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (Counter_GetValore(L_P1__GetSubcl36(my_id)) == 1415u));
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_NotLogicOP_15);
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_AndLogicOP_14);
    
    if(res_OrLogicOP_10){
    bool res_OrLogicOP_16 = false;
    bool res_OrLogicOP_17 = false;
    bool res_AndLogicOP_18 = true;
    bool res_AndLogicOP_19 = true;
    bool res_AndLogicOP_20 = true;
    res_AndLogicOP_20 = (res_AndLogicOP_20 && (L_P1__GetParamSubcl8(my_id) == 3u));
    bool res_NotLogicOP_21 = true;
    bool res_NotLogicOP_22 = true;
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! (Counter_GetValore(L_P1__GetSubcl36(my_id)) == 15u));
    res_NotLogicOP_21 = (res_NotLogicOP_21 && ! res_NotLogicOP_22);
    res_AndLogicOP_20 = (res_AndLogicOP_20 && res_NotLogicOP_21);
    
    res_AndLogicOP_19 = (res_AndLogicOP_19 && res_AndLogicOP_20);
    bool res_NotLogicOP_23 = true;
    bool res_NotLogicOP_24 = true;
    res_NotLogicOP_24 = (res_NotLogicOP_24 && ! (L_P1__GetParamSubcl8(my_id) == 4u));
    res_NotLogicOP_23 = (res_NotLogicOP_23 && ! res_NotLogicOP_24);
    res_AndLogicOP_19 = (res_AndLogicOP_19 && res_NotLogicOP_23);
    
    res_AndLogicOP_18 = (res_AndLogicOP_18 && res_AndLogicOP_19);
    bool res_NotLogicOP_25 = true;
    bool res_NotLogicOP_26 = true;
    res_NotLogicOP_26 = (res_NotLogicOP_26 && ! (L_P1__GetParamSubcl8(my_id) == 5u));
    res_NotLogicOP_25 = (res_NotLogicOP_25 && ! res_NotLogicOP_26);
    res_AndLogicOP_18 = (res_AndLogicOP_18 && res_NotLogicOP_25);
    
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_AndLogicOP_18);
    bool res_NotLogicOP_27 = true;
    res_NotLogicOP_27 = (res_NotLogicOP_27 && ! (L_P1__GetSubcl28(my_id) == true));
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_NotLogicOP_27);
    
    res_OrLogicOP_16 = (res_OrLogicOP_16 || res_OrLogicOP_17);
    bool res_NotLogicOP_28 = true;
    res_NotLogicOP_28 = (res_NotLogicOP_28 && ! (Counter_GetValore(L_P1__GetSubcl36(my_id)) > 13u));
    res_OrLogicOP_16 = (res_OrLogicOP_16 || res_NotLogicOP_28);
    
    res_ImpliesLogicOp_9 = (res_ImpliesLogicOp_9 && res_OrLogicOP_16);
    }
    res_ImpliesLogicOp_3 = (res_ImpliesLogicOp_3 && res_ImpliesLogicOp_9);
    }
    if(res_ImpliesLogicOp_3){
    xorIndex_res_XorLogicOP_2 = (xorIndex_res_XorLogicOP_2 + 1);
    }
    bool res_OrLogicOP_29 = false;
    bool res_OrLogicOP_30 = false;
    bool res_OrLogicOP_31 = false;
    bool res_NotLogicOP_32 = true;
    res_NotLogicOP_32 = (res_NotLogicOP_32 && ! (Counter_GetValore(L_P1__GetSubcl36(my_id)) > 11u));
    res_OrLogicOP_31 = (res_OrLogicOP_31 || res_NotLogicOP_32);
    res_OrLogicOP_31 = (res_OrLogicOP_31 || (L_P1__GetInConsd1(my_id) == false));
    
    res_OrLogicOP_30 = (res_OrLogicOP_30 || res_OrLogicOP_31);
    res_OrLogicOP_30 = (res_OrLogicOP_30 || (L_P1__GetInConsd1(my_id) == false));
    
    res_OrLogicOP_29 = (res_OrLogicOP_29 || res_OrLogicOP_30);
    res_OrLogicOP_29 = (res_OrLogicOP_29 || (L_P1__GetInConsd1(my_id) == false));
    
    if(res_OrLogicOP_29){
    xorIndex_res_XorLogicOP_2 = (xorIndex_res_XorLogicOP_2 + 1);
    }
    
    res_XorLogicOP_2 = (res_XorLogicOP_2 && (xorIndex_res_XorLogicOP_2 == 1));
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_XorLogicOP_2);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *48,49,*  *,*  il controllo SubClass_C2_controllo_C9 sia  diverso da RossoGiallo
    //   *104,* o  che  *,*  il timer SubClass_C2_timer_T3 non sia disattivo
    //   *104,* o  che  *36,*  il timer SubClass_C2_timer_T5 non sia disattivo
    bool res_OrLogicOP_33 = false;
    bool res_OrLogicOP_34 = false;
    bool res_NotLogicOP_35 = true;
    res_NotLogicOP_35 = (res_NotLogicOP_35 && ! (L_P1__GetInSubcl6(my_id) == rossogiallo1));
    res_OrLogicOP_34 = (res_OrLogicOP_34 || res_NotLogicOP_35);
    bool res_NotLogicOP_36 = true;
    res_NotLogicOP_36 = (res_NotLogicOP_36 && ! Timer_Disattivo(L_P1__GetSubcl31(my_id)));
    res_OrLogicOP_34 = (res_OrLogicOP_34 || res_NotLogicOP_36);
    
    res_OrLogicOP_33 = (res_OrLogicOP_33 || res_OrLogicOP_34);
    bool res_NotLogicOP_37 = true;
    res_NotLogicOP_37 = (res_NotLogicOP_37 && ! Timer_Disattivo(L_P1__GetSubcl32(my_id)));
    res_OrLogicOP_33 = (res_OrLogicOP_33 || res_NotLogicOP_37);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_33);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
    
    { commento: {63,} commento: {38,}  se il contatore SubClass_C2_contatore_Co10 non è  minore di  commento: {55,} 11154, Solo una delle seguenti { 
     commento: {61,} commento: {41,}  se MainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  commento: {105,} è  diverso da AC, Tutte le seguenti { 
     commento: {63,} commento: {35,}  se il controllo SubClass_C2_controllo_C3 è  uguale a  True ,  commento: {42,}  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  commento: {105,} è  diverso da  True , commento: {88,} quando  commento: {41,}   MainClass_C1_parametro_P4 del campo  MainClass_C1     commento: {105,} è  uguale a AC commento: {37,} o  se la variabile SubClass_C2_variabile_V5 è  uguale a  True  commento: {37,} e  se la variabile SubClass_C2_variabile_V5 è  uguale a  True  commento: {38,} e  se il contatore SubClass_C2_contatore_Co10 è  minore di  commento: {55,} 11, Solo una delle seguenti { 
     commento: {43,}  se MainClass_C1_timer_T7 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  commento: {105,} è attivo, Verifica che   commento: {47,49,50,51,}  commento: {34,}  il parametro SubClass_C2_parametro_P8 sia  diverso da  commento: {56,} 9
     commento: {104,} e  che  commento: {,}  la variabile SubClass_C2_variabile_V5 sia  uguale a  False 
     commento: {104,} e  che  commento: {,}  il contatore SubClass_C2_contatore_Co10 non sia  minore di  commento: {55,} 1121
     commento: {104,} e  che  commento: {38,}  il contatore SubClass_C2_contatore_Co10 sia  maggiore di  commento: {54,} 155
     commento: {104,} o  che  commento: {,}  il timer SubClass_C2_timer_T9 non sia disattivo
    
    
     } Verifica che   commento: {47,48,50,51,}  commento: {34,}  il parametro SubClass_C2_parametro_P8 sia  maggiore di  commento: {54,} 4
     commento: {104,} o  che  commento: {,}  il contatore SubClass_C2_contatore_Co10 sia  uguale a  commento: {53,} 154
     commento: {104,} o  che  commento: {38,}  il contatore SubClass_C2_contatore_Co10 sia  diverso da  commento: {56,} 13032
     commento: {104,} o  che  commento: {,}  il controllo SubClass_C2_controllo_C3 non sia  diverso da  False 
     commento: {104,} o  che  commento: {,}  la variabile SubClass_C2_variabile_V9 non sia  uguale a  False 
     commento: {104,} o  che  commento: {35,}  il controllo SubClass_C2_controllo_C3 non sia  diverso da  True 
    
    
     } Verifica che   commento: {47,48,52,}   l'argomento argomento_ave7 non  sia  diverso da  False  commento: {,} 
     commento: {104,} e  che   l'argomento argomento_ave7 non  sia  diverso da  False  commento: {39,} 
     commento: {104,} e  che  commento: {34,}  il parametro SubClass_C2_parametro_P8 non sia  diverso da  commento: {56,} 7
     commento: {104,} o  che  commento: {34,}  il parametro SubClass_C2_parametro_P8 non sia  uguale a  commento: {53,} 9
     commento: {104,} e  che  commento: {,}  il controllo SubClass_C2_controllo_C9 sia  diverso da RossoGiallo
    
    
     } Verifica che   commento: {48,51,52,}  commento: {,}  il contatore SubClass_C2_contatore_Co10 non sia  minore di  commento: {55,} 1
     commento: {104,} o  che   l'argomento argomento_ave7 non  sia  diverso da  True  commento: {,} 
     commento: {104,} e  che  commento: {,}  il controllo SubClass_C2_controllo_C9 sia  diverso da RossoGiallo
     commento: {104,} e  che  commento: {38,}  il contatore SubClass_C2_contatore_Co10 non sia  minore di  commento: {55,} 125
    
    
    }
*/
bool L_P1__Macro14(instance_id_t const my_id , C2_Enumerat2 argom28, C2_Enumerat3 argom29, bool argom30, C2_Enumerat2 argom31, bool argom32, bool argom33, bool argom34)
{
bool res_AndLogicOP_0 = true;
    
    //  *63,* *38,*  se il contatore SubClass_C2_contatore_Co10 non è  minore di  *55,* 11154, Solo una delle seguenti { 
    //   *61,* *41,*  se MainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  *105,* è  diverso da AC, Tutte le seguenti { 
    //   *63,* *35,*  se il controllo SubClass_C2_controllo_C3 è  uguale a  True ,  *42,*  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  *105,* è  diverso da  True , *88,* quando  *41,*   MainClass_C1_parametro_P4 del campo  MainClass_C1     *105,* è  uguale a AC *37,* o  se la variabile SubClass_C2_variabile_V5 è  uguale a  True  *37,* e  se la variabile SubClass_C2_variabile_V5 è  uguale a  True  *38,* e  se il contatore SubClass_C2_contatore_Co10 è  minore di  *55,* 11, Solo una delle seguenti { 
    //   *43,*  se MainClass_C1_timer_T7 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  *105,* è attivo, Verifica che   *47,49,50,51,*  *34,*  il parametro SubClass_C2_parametro_P8 sia  diverso da  *56,* 9
    //   *104,* e  che  *,*  la variabile SubClass_C2_variabile_V5 sia  uguale a  False 
    //   *104,* e  che  *,*  il contatore SubClass_C2_contatore_Co10 non sia  minore di  *55,* 1121
    //   *104,* e  che  *38,*  il contatore SubClass_C2_contatore_Co10 sia  maggiore di  *54,* 155
    //   *104,* o  che  *,*  il timer SubClass_C2_timer_T9 non sia disattivo
    //   } Verifica che   *47,48,50,51,*  *34,*  il parametro SubClass_C2_parametro_P8 sia  maggiore di  *54,* 4
    //   *104,* o  che  *,*  il contatore SubClass_C2_contatore_Co10 sia  uguale a  *53,* 154
    //   *104,* o  che  *38,*  il contatore SubClass_C2_contatore_Co10 sia  diverso da  *56,* 13032
    //   *104,* o  che  *,*  il controllo SubClass_C2_controllo_C3 non sia  diverso da  False 
    //   *104,* o  che  *,*  la variabile SubClass_C2_variabile_V9 non sia  uguale a  False 
    //   *104,* o  che  *35,*  il controllo SubClass_C2_controllo_C3 non sia  diverso da  True 
    //   } Verifica che   *47,48,52,*   l'argomento argomento_ave7 non  sia  diverso da  False  *,* 
    //   *104,* e  che   l'argomento argomento_ave7 non  sia  diverso da  False  *39,* 
    //   *104,* e  che  *34,*  il parametro SubClass_C2_parametro_P8 non sia  diverso da  *56,* 7
    //   *104,* o  che  *34,*  il parametro SubClass_C2_parametro_P8 non sia  uguale a  *53,* 9
    //   *104,* e  che  *,*  il controllo SubClass_C2_controllo_C9 sia  diverso da RossoGiallo
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (Counter_GetValore(L_P1__GetSubcl36(my_id)) < 11154u));
    if(res_NotLogicOP_2){
    bool res_XorLogicOP_3 = true;
    int xorIndex_res_XorLogicOP_3 = 0;
    bool res_ImpliesLogicOp_4 = true;
    bool res_ForAllPredicateNotEmpty_5 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl7Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl7(my_id,i);
    bool res_ImpliesLogicOp_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetParamMainc7(it.mainc32) == ac));
    res_ImpliesLogicOp_6 = (res_ImpliesLogicOp_6 && res_NotLogicOP_7);
    res_ForAllPredicateNotEmpty_5 = res_ImpliesLogicOp_6;
    if(!res_ForAllPredicateNotEmpty_5) {break;}
    }
    if(res_ForAllPredicateNotEmpty_5){
    bool res_AndLogicOP_8 = true;
    bool res_ImpliesLogicOp_9 = true;
    bool res_OrLogicOP_10 = false;
    bool res_AndLogicOP_11 = true;
    res_AndLogicOP_11 = (res_AndLogicOP_11 && (L_P1__GetInSubcl5(my_id) == true));
    bool res_ForAllPredicateNotEmpty_12 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl7Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl7(my_id,i);
    bool res_ImpliesLogicOp_13 = true;
    if((L_P1__GetParamMainc7(it.mainc32) == ac)){
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1__GetInMainc6(it.mainc32) == true));
    res_ImpliesLogicOp_13 = (res_ImpliesLogicOp_13 && res_NotLogicOP_14);
    res_ForAllPredicateNotEmpty_12 = res_ImpliesLogicOp_13;
    if(!res_ForAllPredicateNotEmpty_12) {break;}
    }
    }
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_ForAllPredicateNotEmpty_12);
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_AndLogicOP_11);
    bool res_AndLogicOP_15 = true;
    bool res_AndLogicOP_16 = true;
    res_AndLogicOP_16 = (res_AndLogicOP_16 && (L_P1__GetSubcl27(my_id) == true));
    res_AndLogicOP_16 = (res_AndLogicOP_16 && (L_P1__GetSubcl27(my_id) == true));
    
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_AndLogicOP_16);
    res_AndLogicOP_15 = (res_AndLogicOP_15 && (Counter_GetValore(L_P1__GetSubcl36(my_id)) < 11u));
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_AndLogicOP_15);
    
    if(res_OrLogicOP_10){
    bool res_ImpliesLogicOp_17 = true;
    bool res_ForAllPredicateNotEmpty_18 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl7Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl7(my_id,i);
    bool res_ImpliesLogicOp_19 = true;
    res_ImpliesLogicOp_19 = (res_ImpliesLogicOp_19 && Timer_Attivo(L_P1__GetMainc29(it.mainc32)));
    res_ForAllPredicateNotEmpty_18 = res_ImpliesLogicOp_19;
    if(!res_ForAllPredicateNotEmpty_18) {break;}
    }
    if(res_ForAllPredicateNotEmpty_18){
    bool res_OrLogicOP_20 = false;
    bool res_AndLogicOP_21 = true;
    bool res_AndLogicOP_22 = true;
    bool res_AndLogicOP_23 = true;
    bool res_NotLogicOP_24 = true;
    res_NotLogicOP_24 = (res_NotLogicOP_24 && ! (L_P1__GetParamSubcl8(my_id) == 9u));
    res_AndLogicOP_23 = (res_AndLogicOP_23 && res_NotLogicOP_24);
    res_AndLogicOP_23 = (res_AndLogicOP_23 && (L_P1__GetSubcl27(my_id) == false));
    
    res_AndLogicOP_22 = (res_AndLogicOP_22 && res_AndLogicOP_23);
    bool res_NotLogicOP_25 = true;
    res_NotLogicOP_25 = (res_NotLogicOP_25 && ! (Counter_GetValore(L_P1__GetSubcl36(my_id)) < 1121u));
    res_AndLogicOP_22 = (res_AndLogicOP_22 && res_NotLogicOP_25);
    
    res_AndLogicOP_21 = (res_AndLogicOP_21 && res_AndLogicOP_22);
    res_AndLogicOP_21 = (res_AndLogicOP_21 && (Counter_GetValore(L_P1__GetSubcl36(my_id)) > 155u));
    
    res_OrLogicOP_20 = (res_OrLogicOP_20 || res_AndLogicOP_21);
    bool res_NotLogicOP_26 = true;
    res_NotLogicOP_26 = (res_NotLogicOP_26 && ! Timer_Disattivo(L_P1__GetSubcl35(my_id)));
    res_OrLogicOP_20 = (res_OrLogicOP_20 || res_NotLogicOP_26);
    
    res_ImpliesLogicOp_17 = (res_ImpliesLogicOp_17 && res_OrLogicOP_20);
    }
    res_ImpliesLogicOp_9 = (res_ImpliesLogicOp_9 && res_ImpliesLogicOp_17);
    }
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_ImpliesLogicOp_9);
    bool res_OrLogicOP_27 = false;
    bool res_OrLogicOP_28 = false;
    bool res_OrLogicOP_29 = false;
    bool res_OrLogicOP_30 = false;
    bool res_OrLogicOP_31 = false;
    res_OrLogicOP_31 = (res_OrLogicOP_31 || (L_P1__GetParamSubcl8(my_id) > 4u));
    res_OrLogicOP_31 = (res_OrLogicOP_31 || (Counter_GetValore(L_P1__GetSubcl36(my_id)) == 154u));
    
    res_OrLogicOP_30 = (res_OrLogicOP_30 || res_OrLogicOP_31);
    bool res_NotLogicOP_32 = true;
    res_NotLogicOP_32 = (res_NotLogicOP_32 && ! (Counter_GetValore(L_P1__GetSubcl36(my_id)) == 13032u));
    res_OrLogicOP_30 = (res_OrLogicOP_30 || res_NotLogicOP_32);
    
    res_OrLogicOP_29 = (res_OrLogicOP_29 || res_OrLogicOP_30);
    bool res_NotLogicOP_33 = true;
    bool res_NotLogicOP_34 = true;
    res_NotLogicOP_34 = (res_NotLogicOP_34 && ! (L_P1__GetInSubcl5(my_id) == false));
    res_NotLogicOP_33 = (res_NotLogicOP_33 && ! res_NotLogicOP_34);
    res_OrLogicOP_29 = (res_OrLogicOP_29 || res_NotLogicOP_33);
    
    res_OrLogicOP_28 = (res_OrLogicOP_28 || res_OrLogicOP_29);
    bool res_NotLogicOP_35 = true;
    res_NotLogicOP_35 = (res_NotLogicOP_35 && ! (L_P1__GetSubcl28(my_id) == false));
    res_OrLogicOP_28 = (res_OrLogicOP_28 || res_NotLogicOP_35);
    
    res_OrLogicOP_27 = (res_OrLogicOP_27 || res_OrLogicOP_28);
    bool res_NotLogicOP_36 = true;
    bool res_NotLogicOP_37 = true;
    res_NotLogicOP_37 = (res_NotLogicOP_37 && ! (L_P1__GetInSubcl5(my_id) == true));
    res_NotLogicOP_36 = (res_NotLogicOP_36 && ! res_NotLogicOP_37);
    res_OrLogicOP_27 = (res_OrLogicOP_27 || res_NotLogicOP_36);
    
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_OrLogicOP_27);
    
    res_ImpliesLogicOp_4 = (res_ImpliesLogicOp_4 && res_AndLogicOP_8);
    }
    if(res_ImpliesLogicOp_4){
    xorIndex_res_XorLogicOP_3 = (xorIndex_res_XorLogicOP_3 + 1);
    }
    bool res_OrLogicOP_38 = false;
    bool res_AndLogicOP_39 = true;
    bool res_AndLogicOP_40 = true;
    bool res_NotLogicOP_41 = true;
    bool res_NotLogicOP_42 = true;
    res_NotLogicOP_42 = (res_NotLogicOP_42 && ! (argom32 == false));
    res_NotLogicOP_41 = (res_NotLogicOP_41 && ! res_NotLogicOP_42);
    res_AndLogicOP_40 = (res_AndLogicOP_40 && res_NotLogicOP_41);
    bool res_NotLogicOP_43 = true;
    bool res_NotLogicOP_44 = true;
    res_NotLogicOP_44 = (res_NotLogicOP_44 && ! (argom32 == false));
    res_NotLogicOP_43 = (res_NotLogicOP_43 && ! res_NotLogicOP_44);
    res_AndLogicOP_40 = (res_AndLogicOP_40 && res_NotLogicOP_43);
    
    res_AndLogicOP_39 = (res_AndLogicOP_39 && res_AndLogicOP_40);
    bool res_NotLogicOP_45 = true;
    bool res_NotLogicOP_46 = true;
    res_NotLogicOP_46 = (res_NotLogicOP_46 && ! (L_P1__GetParamSubcl8(my_id) == 7u));
    res_NotLogicOP_45 = (res_NotLogicOP_45 && ! res_NotLogicOP_46);
    res_AndLogicOP_39 = (res_AndLogicOP_39 && res_NotLogicOP_45);
    
    res_OrLogicOP_38 = (res_OrLogicOP_38 || res_AndLogicOP_39);
    bool res_AndLogicOP_47 = true;
    bool res_NotLogicOP_48 = true;
    res_NotLogicOP_48 = (res_NotLogicOP_48 && ! (L_P1__GetParamSubcl8(my_id) == 9u));
    res_AndLogicOP_47 = (res_AndLogicOP_47 && res_NotLogicOP_48);
    bool res_NotLogicOP_49 = true;
    res_NotLogicOP_49 = (res_NotLogicOP_49 && ! (L_P1__GetInSubcl6(my_id) == rossogiallo1));
    res_AndLogicOP_47 = (res_AndLogicOP_47 && res_NotLogicOP_49);
    
    res_OrLogicOP_38 = (res_OrLogicOP_38 || res_AndLogicOP_47);
    
    if(res_OrLogicOP_38){
    xorIndex_res_XorLogicOP_3 = (xorIndex_res_XorLogicOP_3 + 1);
    }
    
    res_XorLogicOP_3 = (res_XorLogicOP_3 && (xorIndex_res_XorLogicOP_3 == 1));
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_XorLogicOP_3);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *48,51,52,*  *,*  il contatore SubClass_C2_contatore_Co10 non sia  minore di  *55,* 1
    //   *104,* o  che   l'argomento argomento_ave7 non  sia  diverso da  True  *,* 
    //   *104,* e  che  *,*  il controllo SubClass_C2_controllo_C9 sia  diverso da RossoGiallo
    //   *104,* e  che  *38,*  il contatore SubClass_C2_contatore_Co10 non sia  minore di  *55,* 125
    bool res_OrLogicOP_50 = false;
    bool res_NotLogicOP_51 = true;
    res_NotLogicOP_51 = (res_NotLogicOP_51 && ! (Counter_GetValore(L_P1__GetSubcl36(my_id)) < 1u));
    res_OrLogicOP_50 = (res_OrLogicOP_50 || res_NotLogicOP_51);
    bool res_AndLogicOP_52 = true;
    bool res_AndLogicOP_53 = true;
    bool res_NotLogicOP_54 = true;
    bool res_NotLogicOP_55 = true;
    res_NotLogicOP_55 = (res_NotLogicOP_55 && ! (argom32 == true));
    res_NotLogicOP_54 = (res_NotLogicOP_54 && ! res_NotLogicOP_55);
    res_AndLogicOP_53 = (res_AndLogicOP_53 && res_NotLogicOP_54);
    bool res_NotLogicOP_56 = true;
    res_NotLogicOP_56 = (res_NotLogicOP_56 && ! (L_P1__GetInSubcl6(my_id) == rossogiallo1));
    res_AndLogicOP_53 = (res_AndLogicOP_53 && res_NotLogicOP_56);
    
    res_AndLogicOP_52 = (res_AndLogicOP_52 && res_AndLogicOP_53);
    bool res_NotLogicOP_57 = true;
    res_NotLogicOP_57 = (res_NotLogicOP_57 && ! (Counter_GetValore(L_P1__GetSubcl36(my_id)) < 125u));
    res_AndLogicOP_52 = (res_AndLogicOP_52 && res_NotLogicOP_57);
    
    res_OrLogicOP_50 = (res_OrLogicOP_50 || res_AndLogicOP_52);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_50);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
     
    { commento: {63,} commento: {44,}  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  commento: {105,} è  uguale a c270x commento: {36,} o  se il timer SubClass_C2_timer_T5 non è attivo commento: {36,} o  se il timer SubClass_C2_timer_T7 non è scaduto, Solo una delle seguenti { 
     commento: {62,} commento: {38,}  se il contatore SubClass_C2_contatore_Co10 non è  maggiore di  commento: {54,} 14403,  commento: {43,}  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  commento: {105,} è disattivo, commento: {88,} quando  commento: {44,}    MainClass_C1_variabile_V8 del campo  MainClass_C1     è  diverso da avviox commento: {34,} e  se il parametro SubClass_C2_parametro_P8 è  diverso da  commento: {56,} 2 commento: {38,} o  se il contatore SubClass_C2_contatore_Co10 non è  uguale a  commento: {53,} 14 commento: {38,} e  se il contatore SubClass_C2_contatore_Co10 è  minore di  commento: {55,} 1121 commento: {36,} e  se il timer SubClass_C2_timer_T5 è attivo, Almeno una delle seguenti { 
      se il controllo ConsDef  è  uguale a FALSE  commento: {36,} e  se il timer SubClass_C2_timer_T7 è attivo commento: {36,} e  se il timer SubClass_C2_timer_T5 non è scaduto, Verifica che   commento: {48,}  commento: {,}  il controllo SubClass_C2_controllo_C3 non sia  diverso da  True 
    
    
     } Verifica che   commento: {47,48,51,}  commento: {34,}  il parametro SubClass_C2_parametro_P8 non sia  diverso da  commento: {56,} 7
     commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} o  che  commento: {,}  il controllo SubClass_C2_controllo_C3 non sia  uguale a  True 
     commento: {104,} e  che  commento: {,}  il contatore SubClass_C2_contatore_Co10 sia  uguale a  commento: {53,} 11
     commento: {104,} e  che  commento: {35,}  il controllo SubClass_C2_controllo_C9 non sia  uguale a RossoGiallo
    
    
     } Verifica che   commento: {48,51,}  commento: {,}  il contatore SubClass_C2_contatore_Co10 non sia  diverso da  commento: {56,} 1154
     commento: {104,} e  che  commento: {,}  il controllo SubClass_C2_controllo_C9 non sia  diverso da RossoGiallo
     commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
    
    
    }
*/
bool L_P1__Macro15(instance_id_t const my_id )
{
bool res_AndLogicOP_0 = true;
    
    //  *63,* *44,*  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  *105,* è  uguale a c270x *36,* o  se il timer SubClass_C2_timer_T5 non è attivo *36,* o  se il timer SubClass_C2_timer_T7 non è scaduto, Solo una delle seguenti { 
    //   *62,* *38,*  se il contatore SubClass_C2_contatore_Co10 non è  maggiore di  *54,* 14403,  *43,*  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  *105,* è disattivo, *88,* quando  *44,*    MainClass_C1_variabile_V8 del campo  MainClass_C1     è  diverso da avviox *34,* e  se il parametro SubClass_C2_parametro_P8 è  diverso da  *56,* 2 *38,* o  se il contatore SubClass_C2_contatore_Co10 non è  uguale a  *53,* 14 *38,* e  se il contatore SubClass_C2_contatore_Co10 è  minore di  *55,* 1121 *36,* e  se il timer SubClass_C2_timer_T5 è attivo, Almeno una delle seguenti { 
    //    se il controllo ConsDef  è  uguale a FALSE  *36,* e  se il timer SubClass_C2_timer_T7 è attivo *36,* e  se il timer SubClass_C2_timer_T5 non è scaduto, Verifica che   *48,*  *,*  il controllo SubClass_C2_controllo_C3 non sia  diverso da  True 
    //   } Verifica che   *47,48,51,*  *34,*  il parametro SubClass_C2_parametro_P8 non sia  diverso da  *56,* 7
    //   *104,* o  che   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* o  che  *,*  il controllo SubClass_C2_controllo_C3 non sia  uguale a  True 
    //   *104,* e  che  *,*  il contatore SubClass_C2_contatore_Co10 sia  uguale a  *53,* 11
    //   *104,* e  che  *35,*  il controllo SubClass_C2_controllo_C9 non sia  uguale a RossoGiallo
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_ForAllPredicateNotEmpty_4 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl7Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl7(my_id,i);
    bool res_ImpliesLogicOp_5 = true;
    res_ImpliesLogicOp_5 = (res_ImpliesLogicOp_5 && (L_P1__GetMainc19(it.mainc32) == c270x));
    res_ForAllPredicateNotEmpty_4 = res_ImpliesLogicOp_5;
    if(!res_ForAllPredicateNotEmpty_4) {break;}
    }
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_ForAllPredicateNotEmpty_4);
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! Timer_Attivo(L_P1__GetSubcl32(my_id)));
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_NotLogicOP_6);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! Timer_Scaduto(L_P1__GetSubcl33(my_id)));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_7);
    
    if(res_OrLogicOP_2){
    bool res_XorLogicOP_8 = true;
    int xorIndex_res_XorLogicOP_8 = 0;
    bool res_ImpliesLogicOp_9 = true;
    bool res_OrLogicOP_10 = false;
    bool res_AndLogicOP_11 = true;
    bool res_AndLogicOP_12 = true;
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (Counter_GetValore(L_P1__GetSubcl36(my_id)) > 14403u));
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_NotLogicOP_13);
    bool res_ForAllPredicateNotEmpty_14 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl7Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl7(my_id,i);
    bool res_ImpliesLogicOp_15 = true;
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (L_P1__GetMainc21(it.mainc32) == avviox));
    if(res_NotLogicOP_16){
    res_ImpliesLogicOp_15 = (res_ImpliesLogicOp_15 && Timer_Disattivo(L_P1__GetMainc27(it.mainc32)));
    res_ForAllPredicateNotEmpty_14 = res_ImpliesLogicOp_15;
    if(!res_ForAllPredicateNotEmpty_14) {break;}
    }
    }
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_ForAllPredicateNotEmpty_14);
    
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_AndLogicOP_12);
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! (L_P1__GetParamSubcl8(my_id) == 2u));
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_NotLogicOP_17);
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_AndLogicOP_11);
    bool res_AndLogicOP_18 = true;
    bool res_AndLogicOP_19 = true;
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! (Counter_GetValore(L_P1__GetSubcl36(my_id)) == 14u));
    res_AndLogicOP_19 = (res_AndLogicOP_19 && res_NotLogicOP_20);
    res_AndLogicOP_19 = (res_AndLogicOP_19 && (Counter_GetValore(L_P1__GetSubcl36(my_id)) < 1121u));
    
    res_AndLogicOP_18 = (res_AndLogicOP_18 && res_AndLogicOP_19);
    res_AndLogicOP_18 = (res_AndLogicOP_18 && Timer_Attivo(L_P1__GetSubcl32(my_id)));
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_AndLogicOP_18);
    
    if(res_OrLogicOP_10){
    bool res_ImpliesLogicOp_21 = true;
    bool res_AndLogicOP_22 = true;
    bool res_AndLogicOP_23 = true;
    res_AndLogicOP_23 = (res_AndLogicOP_23 && (L_P1__GetInConsd1(my_id) == false));
    res_AndLogicOP_23 = (res_AndLogicOP_23 && Timer_Attivo(L_P1__GetSubcl33(my_id)));
    
    res_AndLogicOP_22 = (res_AndLogicOP_22 && res_AndLogicOP_23);
    bool res_NotLogicOP_24 = true;
    res_NotLogicOP_24 = (res_NotLogicOP_24 && ! Timer_Scaduto(L_P1__GetSubcl32(my_id)));
    res_AndLogicOP_22 = (res_AndLogicOP_22 && res_NotLogicOP_24);
    
    if(res_AndLogicOP_22){
    bool res_NotLogicOP_25 = true;
    bool res_NotLogicOP_26 = true;
    res_NotLogicOP_26 = (res_NotLogicOP_26 && ! (L_P1__GetInSubcl5(my_id) == true));
    res_NotLogicOP_25 = (res_NotLogicOP_25 && ! res_NotLogicOP_26);
    res_ImpliesLogicOp_21 = (res_ImpliesLogicOp_21 && res_NotLogicOP_25);
    }
    res_ImpliesLogicOp_9 = (res_ImpliesLogicOp_9 && res_ImpliesLogicOp_21);
    }
    if(res_ImpliesLogicOp_9){
    xorIndex_res_XorLogicOP_8 = (xorIndex_res_XorLogicOP_8 + 1);
    }
    bool res_OrLogicOP_27 = false;
    bool res_OrLogicOP_28 = false;
    bool res_NotLogicOP_29 = true;
    bool res_NotLogicOP_30 = true;
    res_NotLogicOP_30 = (res_NotLogicOP_30 && ! (L_P1__GetParamSubcl8(my_id) == 7u));
    res_NotLogicOP_29 = (res_NotLogicOP_29 && ! res_NotLogicOP_30);
    res_OrLogicOP_28 = (res_OrLogicOP_28 || res_NotLogicOP_29);
    res_OrLogicOP_28 = (res_OrLogicOP_28 || (L_P1__GetInConsd1(my_id) == false));
    
    res_OrLogicOP_27 = (res_OrLogicOP_27 || res_OrLogicOP_28);
    bool res_AndLogicOP_31 = true;
    bool res_AndLogicOP_32 = true;
    bool res_NotLogicOP_33 = true;
    res_NotLogicOP_33 = (res_NotLogicOP_33 && ! (L_P1__GetInSubcl5(my_id) == true));
    res_AndLogicOP_32 = (res_AndLogicOP_32 && res_NotLogicOP_33);
    res_AndLogicOP_32 = (res_AndLogicOP_32 && (Counter_GetValore(L_P1__GetSubcl36(my_id)) == 11u));
    
    res_AndLogicOP_31 = (res_AndLogicOP_31 && res_AndLogicOP_32);
    bool res_NotLogicOP_34 = true;
    res_NotLogicOP_34 = (res_NotLogicOP_34 && ! (L_P1__GetInSubcl6(my_id) == rossogiallo1));
    res_AndLogicOP_31 = (res_AndLogicOP_31 && res_NotLogicOP_34);
    
    res_OrLogicOP_27 = (res_OrLogicOP_27 || res_AndLogicOP_31);
    
    if(res_OrLogicOP_27){
    xorIndex_res_XorLogicOP_8 = (xorIndex_res_XorLogicOP_8 + 1);
    }
    
    res_XorLogicOP_8 = (res_XorLogicOP_8 && (xorIndex_res_XorLogicOP_8 == 1));
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_XorLogicOP_8);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *48,51,*  *,*  il contatore SubClass_C2_contatore_Co10 non sia  diverso da  *56,* 1154
    //   *104,* e  che  *,*  il controllo SubClass_C2_controllo_C9 non sia  diverso da RossoGiallo
    //   *104,* o  che   il controllo ConsDef  sia  uguale a FALSE
    bool res_OrLogicOP_35 = false;
    bool res_AndLogicOP_36 = true;
    bool res_NotLogicOP_37 = true;
    bool res_NotLogicOP_38 = true;
    res_NotLogicOP_38 = (res_NotLogicOP_38 && ! (Counter_GetValore(L_P1__GetSubcl36(my_id)) == 1154u));
    res_NotLogicOP_37 = (res_NotLogicOP_37 && ! res_NotLogicOP_38);
    res_AndLogicOP_36 = (res_AndLogicOP_36 && res_NotLogicOP_37);
    bool res_NotLogicOP_39 = true;
    bool res_NotLogicOP_40 = true;
    res_NotLogicOP_40 = (res_NotLogicOP_40 && ! (L_P1__GetInSubcl6(my_id) == rossogiallo1));
    res_NotLogicOP_39 = (res_NotLogicOP_39 && ! res_NotLogicOP_40);
    res_AndLogicOP_36 = (res_AndLogicOP_36 && res_NotLogicOP_39);
    
    res_OrLogicOP_35 = (res_OrLogicOP_35 || res_AndLogicOP_36);
    res_OrLogicOP_35 = (res_OrLogicOP_35 || (L_P1__GetInConsd1(my_id) == false));
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_35);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
    
    { commento: {63,} commento: {45,}  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a  commento: {53,} 13215 o  se l'argomento argomento_ave10 è  uguale a  False  commento: {39,}  o  se l'argomento argomento_ave10 è  uguale a  False  commento: {39,} , Solo una delle seguenti { 
     commento: {61,} commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L9 è  diverso da  commento: {56,}  state1  commento: {38,} o  se il contatore SubClass_C2_contatore_Co10 non è  maggiore di  commento: {54,} 14403, Tutte le seguenti { 
     commento: {61,} commento: {34,}  se lo stato  è  uguale a  commento: {53,}  state1  commento: {106,} commento: {34,} o  se il parametro SubClass_C2_parametro_P8 non è  diverso da  commento: {56,} 9 commento: {37,} o  se la variabile SubClass_C2_variabile_V5 è  uguale a  True  commento: {35,} e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  False  commento: {36,} o  se il timer SubClass_C2_timer_T7 è attivo, Tutte le seguenti { 
     commento: {43,}  se MainClass_C1_timer_T4 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  commento: {105,} è attivo, Verifica che   commento: {48,50,51,52,}  commento: {,}  la variabile SubClass_C2_variabile_V9 sia  diverso da  False 
     commento: {104,} e  che  commento: {,}  il controllo SubClass_C2_controllo_C3 sia  diverso da  True 
     commento: {104,} o  che   l'argomento argomento_ave10 non  sia  uguale a  True  commento: {,} 
     commento: {104,} e  che  commento: {,}  il contatore SubClass_C2_contatore_Co10 non sia  maggiore di  commento: {54,} 132
    
    
     } Verifica che   commento: {47,48,49,51,}  commento: {,}  il controllo SubClass_C2_controllo_C9 sia  uguale a RossoGiallo
     commento: {104,} o  che  commento: {,}  il timer SubClass_C2_timer_T8 non sia attivo
     commento: {104,} o  che  commento: {,}  il contatore SubClass_C2_contatore_Co10 sia  minore di  commento: {55,} 1115
     commento: {104,} o  che  commento: {34,}  il parametro SubClass_C2_parametro_P8 non sia  maggiore di  commento: {54,} 2
    
    
     } Verifica che   commento: {48,52,}  commento: {,}  il controllo SubClass_C2_controllo_C3 non sia  diverso da  True 
     commento: {104,} o  che   l'argomento argomento_ave8 non  sia  uguale a RossoGialloxVerdex commento: {,} 
    
    
     } Verifica che   commento: {47,}  commento: {34,}  il parametro SubClass_C2_parametro_P8 non sia  maggiore di  commento: {54,} 4
    
    
    }
*/
bool L_P1__Macro16(instance_id_t const my_id , C2_Enumerat1 argom35, bool argom36, C2_Enumerat3 argom37, C2_Enumerat4 argom38, C2_Enumerat2 argom39, C2_Enumerat1 argom40, C2_Enumerat1 argom41)
{
bool res_AndLogicOP_0 = true;
    
    //  *63,* *45,*  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a  *53,* 13215 o  se l'argomento argomento_ave10 è  uguale a  False  *39,*  o  se l'argomento argomento_ave10 è  uguale a  False  *39,* , Solo una delle seguenti { 
    //   *61,* *111,*  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L9 è  diverso da  *56,*  state1  *38,* o  se il contatore SubClass_C2_contatore_Co10 non è  maggiore di  *54,* 14403, Tutte le seguenti { 
    //   *61,* *34,*  se lo stato  è  uguale a  *53,*  state1  *106,* *34,* o  se il parametro SubClass_C2_parametro_P8 non è  diverso da  *56,* 9 *37,* o  se la variabile SubClass_C2_variabile_V5 è  uguale a  True  *35,* e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  False  *36,* o  se il timer SubClass_C2_timer_T7 è attivo, Tutte le seguenti { 
    //   *43,*  se MainClass_C1_timer_T4 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  *105,* è attivo, Verifica che   *48,50,51,52,*  *,*  la variabile SubClass_C2_variabile_V9 sia  diverso da  False 
    //   *104,* e  che  *,*  il controllo SubClass_C2_controllo_C3 sia  diverso da  True 
    //   *104,* o  che   l'argomento argomento_ave10 non  sia  uguale a  True  *,* 
    //   *104,* e  che  *,*  il contatore SubClass_C2_contatore_Co10 non sia  maggiore di  *54,* 132
    //   } Verifica che   *47,48,49,51,*  *,*  il controllo SubClass_C2_controllo_C9 sia  uguale a RossoGiallo
    //   *104,* o  che  *,*  il timer SubClass_C2_timer_T8 non sia attivo
    //   *104,* o  che  *,*  il contatore SubClass_C2_contatore_Co10 sia  minore di  *55,* 1115
    //   *104,* o  che  *34,*  il parametro SubClass_C2_parametro_P8 non sia  maggiore di  *54,* 2
    //   } Verifica che   *48,52,*  *,*  il controllo SubClass_C2_controllo_C3 non sia  diverso da  True 
    //   *104,* o  che   l'argomento argomento_ave8 non  sia  uguale a RossoGialloxVerdex *,* 
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_ForAllPredicate_4 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl7Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl7(my_id,i);
    bool res_ImpliesLogicOp_5 = true;
    res_ImpliesLogicOp_5 = (res_ImpliesLogicOp_5 && (Counter_GetValore(L_P1__GetMainc31(it.mainc32)) == 13215u));
    res_ForAllPredicate_4 = res_ImpliesLogicOp_5;
    if(!res_ForAllPredicate_4) {break;}
    }
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_ForAllPredicate_4);
    res_OrLogicOP_3 = (res_OrLogicOP_3 || (argom36 == false));
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    res_OrLogicOP_2 = (res_OrLogicOP_2 || (argom36 == false));
    
    if(res_OrLogicOP_2){
    bool res_XorLogicOP_6 = true;
    int xorIndex_res_XorLogicOP_6 = 0;
    bool res_ImpliesLogicOp_7 = true;
    bool res_OrLogicOP_8 = false;
    bool res_ForAllPredicate_9 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl7Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl7(my_id,i);
    bool res_ImpliesLogicOp_10 = true;
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (L_P1_C1_GetState(it.mainc32) == C1_St_state));
    res_ImpliesLogicOp_10 = (res_ImpliesLogicOp_10 && res_NotLogicOP_11);
    res_ForAllPredicate_9 = res_ImpliesLogicOp_10;
    if(!res_ForAllPredicate_9) {break;}
    }
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_ForAllPredicate_9);
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (Counter_GetValore(L_P1__GetSubcl36(my_id)) > 14403u));
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_NotLogicOP_12);
    
    if(res_OrLogicOP_8){
    bool res_AndLogicOP_13 = true;
    bool res_ImpliesLogicOp_14 = true;
    bool res_OrLogicOP_15 = false;
    bool res_OrLogicOP_16 = false;
    bool res_OrLogicOP_17 = false;
    res_OrLogicOP_17 = (res_OrLogicOP_17 || (L_P1_C2_GetState(my_id) == C2_St_state));
    bool res_NotLogicOP_18 = true;
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (L_P1__GetParamSubcl8(my_id) == 9u));
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! res_NotLogicOP_19);
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_NotLogicOP_18);
    
    res_OrLogicOP_16 = (res_OrLogicOP_16 || res_OrLogicOP_17);
    bool res_AndLogicOP_20 = true;
    res_AndLogicOP_20 = (res_AndLogicOP_20 && (L_P1__GetSubcl27(my_id) == true));
    bool res_NotLogicOP_21 = true;
    res_NotLogicOP_21 = (res_NotLogicOP_21 && ! (L_P1__GetInSubcl5(my_id) == false));
    res_AndLogicOP_20 = (res_AndLogicOP_20 && res_NotLogicOP_21);
    
    res_OrLogicOP_16 = (res_OrLogicOP_16 || res_AndLogicOP_20);
    
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_OrLogicOP_16);
    res_OrLogicOP_15 = (res_OrLogicOP_15 || Timer_Attivo(L_P1__GetSubcl33(my_id)));
    
    if(res_OrLogicOP_15){
    bool res_ImpliesLogicOp_22 = true;
    bool res_ForAllPredicateNotEmpty_23 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl7Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl7(my_id,i);
    bool res_ImpliesLogicOp_24 = true;
    res_ImpliesLogicOp_24 = (res_ImpliesLogicOp_24 && Timer_Attivo(L_P1__GetMainc28(it.mainc32)));
    res_ForAllPredicateNotEmpty_23 = res_ImpliesLogicOp_24;
    if(!res_ForAllPredicateNotEmpty_23) {break;}
    }
    if(res_ForAllPredicateNotEmpty_23){
    bool res_OrLogicOP_25 = false;
    bool res_AndLogicOP_26 = true;
    bool res_NotLogicOP_27 = true;
    res_NotLogicOP_27 = (res_NotLogicOP_27 && ! (L_P1__GetSubcl28(my_id) == false));
    res_AndLogicOP_26 = (res_AndLogicOP_26 && res_NotLogicOP_27);
    bool res_NotLogicOP_28 = true;
    res_NotLogicOP_28 = (res_NotLogicOP_28 && ! (L_P1__GetInSubcl5(my_id) == true));
    res_AndLogicOP_26 = (res_AndLogicOP_26 && res_NotLogicOP_28);
    
    res_OrLogicOP_25 = (res_OrLogicOP_25 || res_AndLogicOP_26);
    bool res_AndLogicOP_29 = true;
    bool res_NotLogicOP_30 = true;
    res_NotLogicOP_30 = (res_NotLogicOP_30 && ! (argom36 == true));
    res_AndLogicOP_29 = (res_AndLogicOP_29 && res_NotLogicOP_30);
    bool res_NotLogicOP_31 = true;
    res_NotLogicOP_31 = (res_NotLogicOP_31 && ! (Counter_GetValore(L_P1__GetSubcl36(my_id)) > 132u));
    res_AndLogicOP_29 = (res_AndLogicOP_29 && res_NotLogicOP_31);
    
    res_OrLogicOP_25 = (res_OrLogicOP_25 || res_AndLogicOP_29);
    
    res_ImpliesLogicOp_22 = (res_ImpliesLogicOp_22 && res_OrLogicOP_25);
    }
    res_ImpliesLogicOp_14 = (res_ImpliesLogicOp_14 && res_ImpliesLogicOp_22);
    }
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_ImpliesLogicOp_14);
    bool res_OrLogicOP_32 = false;
    bool res_OrLogicOP_33 = false;
    bool res_OrLogicOP_34 = false;
    res_OrLogicOP_34 = (res_OrLogicOP_34 || (L_P1__GetInSubcl6(my_id) == rossogiallo1));
    bool res_NotLogicOP_35 = true;
    res_NotLogicOP_35 = (res_NotLogicOP_35 && ! Timer_Attivo(L_P1__GetSubcl34(my_id)));
    res_OrLogicOP_34 = (res_OrLogicOP_34 || res_NotLogicOP_35);
    
    res_OrLogicOP_33 = (res_OrLogicOP_33 || res_OrLogicOP_34);
    res_OrLogicOP_33 = (res_OrLogicOP_33 || (Counter_GetValore(L_P1__GetSubcl36(my_id)) < 1115u));
    
    res_OrLogicOP_32 = (res_OrLogicOP_32 || res_OrLogicOP_33);
    bool res_NotLogicOP_36 = true;
    res_NotLogicOP_36 = (res_NotLogicOP_36 && ! (L_P1__GetParamSubcl8(my_id) > 2u));
    res_OrLogicOP_32 = (res_OrLogicOP_32 || res_NotLogicOP_36);
    
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_OrLogicOP_32);
    
    res_ImpliesLogicOp_7 = (res_ImpliesLogicOp_7 && res_AndLogicOP_13);
    }
    if(res_ImpliesLogicOp_7){
    xorIndex_res_XorLogicOP_6 = (xorIndex_res_XorLogicOP_6 + 1);
    }
    bool res_OrLogicOP_37 = false;
    bool res_NotLogicOP_38 = true;
    bool res_NotLogicOP_39 = true;
    res_NotLogicOP_39 = (res_NotLogicOP_39 && ! (L_P1__GetInSubcl5(my_id) == true));
    res_NotLogicOP_38 = (res_NotLogicOP_38 && ! res_NotLogicOP_39);
    res_OrLogicOP_37 = (res_OrLogicOP_37 || res_NotLogicOP_38);
    bool res_NotLogicOP_40 = true;
    res_NotLogicOP_40 = (res_NotLogicOP_40 && ! (argom40 == rossogiallo));
    res_OrLogicOP_37 = (res_OrLogicOP_37 || res_NotLogicOP_40);
    
    if(res_OrLogicOP_37){
    xorIndex_res_XorLogicOP_6 = (xorIndex_res_XorLogicOP_6 + 1);
    }
    
    res_XorLogicOP_6 = (res_XorLogicOP_6 && (xorIndex_res_XorLogicOP_6 == 1));
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_XorLogicOP_6);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *47,*  *34,*  il parametro SubClass_C2_parametro_P8 non sia  maggiore di  *54,* 4
    bool res_NotLogicOP_41 = true;
    res_NotLogicOP_41 = (res_NotLogicOP_41 && ! (L_P1__GetParamSubcl8(my_id) > 4u));
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_NotLogicOP_41);
    
    
    
    return res_AndLogicOP_0;
}


// Macro valorizzate

/*
    CNL corrispondente:
    
    { commento: {[}
     commento: {46,} assegna alla macro il valore  True  commento: {],}
    }
*/
bool L_P1__Macro8(instance_id_t const my_id , C2_Enumerat3 argom10, C2_Enumerat3 argom11, C2_Enumerat2 argom12, C2_Enumerat3 argom13)
{
return true;
}

/*
    CNL corrispondente:
    
    { commento: {[} commento: {42,}  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a  False  commento: {37,} e  se la variabile SubClass_C2_variabile_V5 è  diverso da  False  commento: {37,} e  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False ,  commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a  commento: {53,}  state1 , commento: {88,} quando  commento: {41,}   MainClass_C1_parametro_P4 del campo  MainClass_C1     è  uguale a AC  , assegna alla macro il valore  False 
    
     commento: {46,} assegna alla macro il valore  False  commento: {],}
    }
*/
bool L_P1__Macro9(instance_id_t const my_id , C2_Enumerat2 argom14, C2_Enumerat2 argom15, C2_Enumerat3 argom16, bool argom17, C2_Enumerat4 argom18, C2_Enumerat4 argom19)
{
bool res_macro_val;
    
    //  *[* *42,*  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a  False  *37,* e  se la variabile SubClass_C2_variabile_V5 è  diverso da  False  *37,* e  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False ,  *111,*  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a  *53,*  state1 , *88,* quando  *41,*   MainClass_C1_parametro_P4 del campo  MainClass_C1     è  uguale a AC
    bool res_AndLogicOP_0 = true;
    bool res_AndLogicOP_1 = true;
    bool res_ForAllPredicate_2 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl7Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl7(my_id,i);
    bool res_ImpliesLogicOp_3 = true;
    res_ImpliesLogicOp_3 = (res_ImpliesLogicOp_3 && (L_P1__GetInMainc6(it.mainc32) == false));
    res_ForAllPredicate_2 = res_ImpliesLogicOp_3;
    if(!res_ForAllPredicate_2) {break;}
    }
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_ForAllPredicate_2);
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetSubcl27(my_id) == false));
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_4);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_AndLogicOP_1);
    bool res_AndLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetSubcl28(my_id) == false));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_6);
    bool res_ForAllPredicate_7 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl7Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl7(my_id,i);
    bool res_ImpliesLogicOp_8 = true;
    if((L_P1__GetParamMainc7(it.mainc32) == ac)){
    res_ImpliesLogicOp_8 = (res_ImpliesLogicOp_8 && (L_P1_C1_GetState(it.mainc32) == C1_St_state));
    }
    res_ForAllPredicate_7 = res_ImpliesLogicOp_8;
    if(!res_ForAllPredicate_7) {break;}
    }
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_ForAllPredicate_7);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_AndLogicOP_5);
    
    if(res_AndLogicOP_0){
    
    res_macro_val = false;
    }
    else{
    res_macro_val = false;
    }
    return res_macro_val;
}

/*
    CNL corrispondente:
    
    { commento: {[}
     commento: {46,} assegna alla macro il valore RossoGialloxVerdex commento: {],}
    }
*/
C2_Enumerat1 L_P1__Macro10(instance_id_t const my_id , C2_Enumerat4 argom20, C2_Enumerat1 argom21, C2_Enumerat4 argom22, bool argom23)
{
return rossogiallo;
}

/*
    CNL corrispondente:
    
    { commento: {[}
     commento: {46,} assegna alla macro il valore  True  commento: {],}
    }
*/
bool L_P1__Macro11(instance_id_t const my_id , C2_Enumerat3 argom24, C2_Enumerat3 argom25, C2_Enumerat3 argom26, C2_Enumerat4 argom27)
{
return true;
}

/*
    CNL corrispondente:
     
    { commento: {[} commento: {35,}  se il controllo SubClass_C2_controllo_C3 non è  diverso da  True  commento: {44,} o  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a c270x , assegna alla macro il valore  False 
    
     commento: {46,} assegna alla macro il valore  True  commento: {],}
    }
*/
bool L_P1__Macro12(instance_id_t const my_id )
{
bool res_macro_val;
    
    //  *[* *35,*  se il controllo SubClass_C2_controllo_C3 non è  diverso da  True  *44,* o  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a c270x
    bool res_OrLogicOP_0 = false;
    bool res_NotLogicOP_1 = true;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (L_P1__GetInSubcl5(my_id) == true));
    res_NotLogicOP_1 = (res_NotLogicOP_1 && ! res_NotLogicOP_2);
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_1);
    bool res_ForAllPredicate_3 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl7Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl7(my_id,i);
    bool res_ImpliesLogicOp_4 = true;
    res_ImpliesLogicOp_4 = (res_ImpliesLogicOp_4 && (L_P1__GetMainc19(it.mainc32) == c270x));
    res_ForAllPredicate_3 = res_ImpliesLogicOp_4;
    if(!res_ForAllPredicate_3) {break;}
    }
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_ForAllPredicate_3);
    
    if(res_OrLogicOP_0){
    
    res_macro_val = false;
    }
    else{
    res_macro_val = true;
    }
    return res_macro_val;
}



