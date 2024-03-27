// Codice del modello 'TestCase19', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#include "Logica/ClasseMainClass_C1.h"
#include "Logica/ClasseSubClass_C2.h"
#include "Logica/ClasseSubClass_C2_priv.h"
#include "config.h"
#include "scheduler.h"


// ********** Gestione comandi automatici **********

static size_t L_P1_C2_NumAutoCmds(instance_id_t const my_id)
{
    size_t n = 0u;
    if (L_P1__GetCAEvent4(my_id)) {
        ++n;
    }
    return n;
}


// ********** Gestione comandi manuali **********

static void L_P1_C2_InitCmdsResponse(instance_id_t const my_id)
{
    // for each manual command of L_P1_C2
    if (L_P1__GetInEvent1(my_id)) {
	    L_P1__SetOutEvent5(my_id, LDS_MANCMD_UNEXPECTED);
    } else {
        L_P1__SetOutEvent5(my_id, LDS_MANCMD_NOOP);
    }
    if (L_P1__GetInEvent2(my_id)) {
	    L_P1__SetOutEvent6(my_id, LDS_MANCMD_UNEXPECTED);
    } else {
        L_P1__SetOutEvent6(my_id, LDS_MANCMD_NOOP);
    }
    if (L_P1__GetInEvent3(my_id)) {
	    L_P1__SetOutEvent7(my_id, LDS_MANCMD_UNEXPECTED);
    } else {
        L_P1__SetOutEvent7(my_id, LDS_MANCMD_NOOP);
    }
}

static void L_P1_C2_SetExpectedCmdsResponse(instance_id_t const my_id, C2_Stateenu state)
{        
    switch (state) {
    case C2_St_state:
        // manual commands of L_P1_C2 that can be received in C2_St_state
	break;

    case C2_St_state1:
        // manual commands of L_P1_C2 that can be received in C2_St_state1
        if (L_P1__GetInEvent3(my_id)) {
            L_P1__SetOutEvent7(my_id, LDS_MANCMD_BLOCKED);
        }
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
    
     Nessuna  commento: {80,}
    }
*/
static inline bool L_P1__Guard3(instance_id_t const my_id)
{
    return true;
}


/*
    CNL corrispondente:
     {  commento: {69,} commento: {37,}  se la variabile SubClass_C2_variabile_V7 non è  uguale a RossoGialloVerde commento: {38,} o  se il contatore SubClass_C2_contatore_Co4 è  uguale a  commento: {53,} 1545 commento: {34,} e  se il parametro SubClass_C2_parametro_P6 non è  diverso da c270 commento: {34,} e  se il parametro SubClass_C2_parametro_P7 è  uguale a  True , Solo una delle seguenti { 
     commento: {69,}  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} e  se la variabile SubClass_C2_variabile_V7 è  diverso da RossoGialloVerde commento: {36,} o  se il timer SubClass_C2_timer_T6 è attivo commento: {38,} o  se il contatore SubClass_C2_contatore_Co9 non è  uguale a  commento: {53,} 13 commento: {38,} o  se il contatore SubClass_C2_contatore_Co8 non è  uguale a  commento: {53,} 13, Solo una delle seguenti { 
     commento: {68,} commento: {35,}  se il controllo SubClass_C2_controllo_C1 non è  diverso da c270 commento: {35,} o  se il controllo SubClass_C2_controllo_C8 non è  diverso da  True  commento: {38,} e  se il contatore SubClass_C2_contatore_Co8 non è  maggiore di  commento: {54,} 153 commento: {38,} e  se il contatore SubClass_C2_contatore_Co9 è  uguale a  commento: {53,} 13210 commento: {34,} e  se il parametro SubClass_C2_parametro_P4 non è  uguale a RossoGialloVerde commento: {35,} e  se il controllo SubClass_C2_controllo_C8 non è  uguale a  False , Almeno una delle seguenti { 
     commento: {67,} commento: {35,}  se il controllo SubClass_C2_controllo_C7 non è  diverso da RossoGiallo commento: {37,} e  se la variabile SubClass_C2_variabile_V7 non è  diverso da RossoGialloVerde commento: {35,} o  se il controllo SubClass_C2_controllo_C7 è  diverso da RossoGiallo commento: {38,} o  se il contatore SubClass_C2_contatore_Co9 è  minore di  commento: {55,} 11, Tutte le seguenti { 
     commento: {69,} commento: {34,}  se il parametro SubClass_C2_parametro_P6 non è  diverso da c270 commento: {35,} o  se il controllo SubClass_C2_controllo_C8 è  diverso da  True  commento: {35,} e  se il controllo SubClass_C2_controllo_C1 è  uguale a c270, Solo una delle seguenti { 
     commento: {34,}  se il parametro SubClass_C2_parametro_P6 non è  uguale a c270 commento: {34,} e  se il parametro SubClass_C2_parametro_P8 è  maggiore di  commento: {54,} 3, Verifica che   commento: {48,}  commento: {,}  il controllo SubClass_C2_controllo_C1 sia  uguale a c270
    
    
     } Verifica che   commento: {48,}  commento: {,}  il controllo SubClass_C2_controllo_C8 non sia  uguale a  True 
    
    
     } Verifica che   commento: {51,}  commento: {,}  il contatore SubClass_C2_contatore_Co9 non sia  maggiore di  commento: {54,} 13
    
    
     } Verifica che   commento: {48,}  commento: {,}  il controllo SubClass_C2_controllo_C8 non sia  uguale a  False 
    
    
     } Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
    
    
     } Verifica che   commento: {47,}  commento: {34,}  il parametro SubClass_C2_parametro_P6 sia  uguale a c270
    
     }
*/
static inline bool L_P1__Guard4(instance_id_t const my_id)
{
    bool res_AndLogicOP_0 = true;
    
    //  *69,* *37,*  se la variabile SubClass_C2_variabile_V7 non è  uguale a RossoGialloVerde *38,* o  se il contatore SubClass_C2_contatore_Co4 è  uguale a  *53,* 1545 *34,* e  se il parametro SubClass_C2_parametro_P6 non è  diverso da c270 *34,* e  se il parametro SubClass_C2_parametro_P7 è  uguale a  True , Solo una delle seguenti { 
    //   *69,*  se il controllo ConsDef  è  uguale a FALSE  *37,* e  se la variabile SubClass_C2_variabile_V7 è  diverso da RossoGialloVerde *36,* o  se il timer SubClass_C2_timer_T6 è attivo *38,* o  se il contatore SubClass_C2_contatore_Co9 non è  uguale a  *53,* 13 *38,* o  se il contatore SubClass_C2_contatore_Co8 non è  uguale a  *53,* 13, Solo una delle seguenti { 
    //   *68,* *35,*  se il controllo SubClass_C2_controllo_C1 non è  diverso da c270 *35,* o  se il controllo SubClass_C2_controllo_C8 non è  diverso da  True  *38,* e  se il contatore SubClass_C2_contatore_Co8 non è  maggiore di  *54,* 153 *38,* e  se il contatore SubClass_C2_contatore_Co9 è  uguale a  *53,* 13210 *34,* e  se il parametro SubClass_C2_parametro_P4 non è  uguale a RossoGialloVerde *35,* e  se il controllo SubClass_C2_controllo_C8 non è  uguale a  False , Almeno una delle seguenti { 
    //   *67,* *35,*  se il controllo SubClass_C2_controllo_C7 non è  diverso da RossoGiallo *37,* e  se la variabile SubClass_C2_variabile_V7 non è  diverso da RossoGialloVerde *35,* o  se il controllo SubClass_C2_controllo_C7 è  diverso da RossoGiallo *38,* o  se il contatore SubClass_C2_contatore_Co9 è  minore di  *55,* 11, Tutte le seguenti { 
    //   *69,* *34,*  se il parametro SubClass_C2_parametro_P6 non è  diverso da c270 *35,* o  se il controllo SubClass_C2_controllo_C8 è  diverso da  True  *35,* e  se il controllo SubClass_C2_controllo_C1 è  uguale a c270, Solo una delle seguenti { 
    //   *34,*  se il parametro SubClass_C2_parametro_P6 non è  uguale a c270 *34,* e  se il parametro SubClass_C2_parametro_P8 è  maggiore di  *54,* 3, Verifica che   *48,*  *,*  il controllo SubClass_C2_controllo_C1 sia  uguale a c270
    //   } Verifica che   *48,*  *,*  il controllo SubClass_C2_controllo_C8 non sia  uguale a  True 
    //   } Verifica che   *51,*  *,*  il contatore SubClass_C2_contatore_Co9 non sia  maggiore di  *54,* 13
    //   } Verifica che   *48,*  *,*  il controllo SubClass_C2_controllo_C8 non sia  uguale a  False 
    //   } Verifica che   *48,*   il controllo ConsDef  sia  uguale a FALSE 
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__GetSubcl36(my_id) == rossogiallo3));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_3);
    bool res_AndLogicOP_4 = true;
    bool res_AndLogicOP_5 = true;
    res_AndLogicOP_5 = (res_AndLogicOP_5 && (Counter_GetValore(L_P1__GetSubcl50(my_id)) == 1545u));
    bool res_NotLogicOP_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetParamSubcl9(my_id) == c270));
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! res_NotLogicOP_7);
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_6);
    
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_AndLogicOP_5);
    res_AndLogicOP_4 = (res_AndLogicOP_4 && (L_P1__GetParamSubcl10(my_id) == true));
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_4);
    
    if(res_OrLogicOP_2){
    bool res_XorLogicOP_8 = true;
    int xorIndex_res_XorLogicOP_8 = 0;
    bool res_ImpliesLogicOp_9 = true;
    bool res_OrLogicOP_10 = false;
    bool res_OrLogicOP_11 = false;
    bool res_OrLogicOP_12 = false;
    bool res_AndLogicOP_13 = true;
    res_AndLogicOP_13 = (res_AndLogicOP_13 && (L_P1__GetInConsd1(my_id) == false));
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1__GetSubcl36(my_id) == rossogiallo3));
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_NotLogicOP_14);
    
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_AndLogicOP_13);
    res_OrLogicOP_12 = (res_OrLogicOP_12 || Timer_Attivo(L_P1__GetSubcl47(my_id)));
    
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_OrLogicOP_12);
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (Counter_GetValore(L_P1__GetSubcl52(my_id)) == 13u));
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_NotLogicOP_15);
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_OrLogicOP_11);
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (Counter_GetValore(L_P1__GetSubcl51(my_id)) == 13u));
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_NotLogicOP_16);
    
    if(res_OrLogicOP_10){
    bool res_XorLogicOP_17 = true;
    int xorIndex_res_XorLogicOP_17 = 0;
    bool res_ImpliesLogicOp_18 = true;
    bool res_OrLogicOP_19 = false;
    bool res_NotLogicOP_20 = true;
    bool res_NotLogicOP_21 = true;
    res_NotLogicOP_21 = (res_NotLogicOP_21 && ! (L_P1__GetInSubcl2(my_id) == c270));
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! res_NotLogicOP_21);
    res_OrLogicOP_19 = (res_OrLogicOP_19 || res_NotLogicOP_20);
    bool res_AndLogicOP_22 = true;
    bool res_AndLogicOP_23 = true;
    bool res_AndLogicOP_24 = true;
    bool res_AndLogicOP_25 = true;
    bool res_NotLogicOP_26 = true;
    bool res_NotLogicOP_27 = true;
    res_NotLogicOP_27 = (res_NotLogicOP_27 && ! (L_P1__GetInSubcl4(my_id) == true));
    res_NotLogicOP_26 = (res_NotLogicOP_26 && ! res_NotLogicOP_27);
    res_AndLogicOP_25 = (res_AndLogicOP_25 && res_NotLogicOP_26);
    bool res_NotLogicOP_28 = true;
    res_NotLogicOP_28 = (res_NotLogicOP_28 && ! (Counter_GetValore(L_P1__GetSubcl51(my_id)) > 153u));
    res_AndLogicOP_25 = (res_AndLogicOP_25 && res_NotLogicOP_28);
    
    res_AndLogicOP_24 = (res_AndLogicOP_24 && res_AndLogicOP_25);
    res_AndLogicOP_24 = (res_AndLogicOP_24 && (Counter_GetValore(L_P1__GetSubcl52(my_id)) == 13210u));
    
    res_AndLogicOP_23 = (res_AndLogicOP_23 && res_AndLogicOP_24);
    bool res_NotLogicOP_29 = true;
    res_NotLogicOP_29 = (res_NotLogicOP_29 && ! (L_P1__GetParamSubcl8(my_id) == rossogiallo3));
    res_AndLogicOP_23 = (res_AndLogicOP_23 && res_NotLogicOP_29);
    
    res_AndLogicOP_22 = (res_AndLogicOP_22 && res_AndLogicOP_23);
    bool res_NotLogicOP_30 = true;
    res_NotLogicOP_30 = (res_NotLogicOP_30 && ! (L_P1__GetInSubcl4(my_id) == false));
    res_AndLogicOP_22 = (res_AndLogicOP_22 && res_NotLogicOP_30);
    
    res_OrLogicOP_19 = (res_OrLogicOP_19 || res_AndLogicOP_22);
    
    if(res_OrLogicOP_19){
    bool res_OrLogicOP_31 = false;
    bool res_ImpliesLogicOp_32 = true;
    bool res_OrLogicOP_33 = false;
    bool res_OrLogicOP_34 = false;
    bool res_AndLogicOP_35 = true;
    bool res_NotLogicOP_36 = true;
    bool res_NotLogicOP_37 = true;
    res_NotLogicOP_37 = (res_NotLogicOP_37 && ! (L_P1__GetInSubcl3(my_id) == rossogiallo1));
    res_NotLogicOP_36 = (res_NotLogicOP_36 && ! res_NotLogicOP_37);
    res_AndLogicOP_35 = (res_AndLogicOP_35 && res_NotLogicOP_36);
    bool res_NotLogicOP_38 = true;
    bool res_NotLogicOP_39 = true;
    res_NotLogicOP_39 = (res_NotLogicOP_39 && ! (L_P1__GetSubcl36(my_id) == rossogiallo3));
    res_NotLogicOP_38 = (res_NotLogicOP_38 && ! res_NotLogicOP_39);
    res_AndLogicOP_35 = (res_AndLogicOP_35 && res_NotLogicOP_38);
    
    res_OrLogicOP_34 = (res_OrLogicOP_34 || res_AndLogicOP_35);
    bool res_NotLogicOP_40 = true;
    res_NotLogicOP_40 = (res_NotLogicOP_40 && ! (L_P1__GetInSubcl3(my_id) == rossogiallo1));
    res_OrLogicOP_34 = (res_OrLogicOP_34 || res_NotLogicOP_40);
    
    res_OrLogicOP_33 = (res_OrLogicOP_33 || res_OrLogicOP_34);
    res_OrLogicOP_33 = (res_OrLogicOP_33 || (Counter_GetValore(L_P1__GetSubcl52(my_id)) < 11u));
    
    if(res_OrLogicOP_33){
    bool res_AndLogicOP_41 = true;
    bool res_ImpliesLogicOp_42 = true;
    bool res_OrLogicOP_43 = false;
    bool res_NotLogicOP_44 = true;
    bool res_NotLogicOP_45 = true;
    res_NotLogicOP_45 = (res_NotLogicOP_45 && ! (L_P1__GetParamSubcl9(my_id) == c270));
    res_NotLogicOP_44 = (res_NotLogicOP_44 && ! res_NotLogicOP_45);
    res_OrLogicOP_43 = (res_OrLogicOP_43 || res_NotLogicOP_44);
    bool res_AndLogicOP_46 = true;
    bool res_NotLogicOP_47 = true;
    res_NotLogicOP_47 = (res_NotLogicOP_47 && ! (L_P1__GetInSubcl4(my_id) == true));
    res_AndLogicOP_46 = (res_AndLogicOP_46 && res_NotLogicOP_47);
    res_AndLogicOP_46 = (res_AndLogicOP_46 && (L_P1__GetInSubcl2(my_id) == c270));
    
    res_OrLogicOP_43 = (res_OrLogicOP_43 || res_AndLogicOP_46);
    
    if(res_OrLogicOP_43){
    bool res_ImpliesLogicOp_48 = true;
    bool res_AndLogicOP_49 = true;
    bool res_NotLogicOP_50 = true;
    res_NotLogicOP_50 = (res_NotLogicOP_50 && ! (L_P1__GetParamSubcl9(my_id) == c270));
    res_AndLogicOP_49 = (res_AndLogicOP_49 && res_NotLogicOP_50);
    res_AndLogicOP_49 = (res_AndLogicOP_49 && (L_P1__GetParamSubcl11(my_id) > 3u));
    
    if(res_AndLogicOP_49){
    res_ImpliesLogicOp_48 = (res_ImpliesLogicOp_48 && (L_P1__GetInSubcl2(my_id) == c270));
    }
    res_ImpliesLogicOp_42 = (res_ImpliesLogicOp_42 && res_ImpliesLogicOp_48);
    }
    res_AndLogicOP_41 = (res_AndLogicOP_41 && res_ImpliesLogicOp_42);
    bool res_NotLogicOP_51 = true;
    res_NotLogicOP_51 = (res_NotLogicOP_51 && ! (L_P1__GetInSubcl4(my_id) == true));
    res_AndLogicOP_41 = (res_AndLogicOP_41 && res_NotLogicOP_51);
    
    res_ImpliesLogicOp_32 = (res_ImpliesLogicOp_32 && res_AndLogicOP_41);
    }
    res_OrLogicOP_31 = (res_OrLogicOP_31 || res_ImpliesLogicOp_32);
    bool res_NotLogicOP_52 = true;
    res_NotLogicOP_52 = (res_NotLogicOP_52 && ! (Counter_GetValore(L_P1__GetSubcl52(my_id)) > 13u));
    res_OrLogicOP_31 = (res_OrLogicOP_31 || res_NotLogicOP_52);
    
    res_ImpliesLogicOp_18 = (res_ImpliesLogicOp_18 && res_OrLogicOP_31);
    }
    if(res_ImpliesLogicOp_18){
    xorIndex_res_XorLogicOP_17 = (xorIndex_res_XorLogicOP_17 + 1);
    }
    bool res_NotLogicOP_53 = true;
    res_NotLogicOP_53 = (res_NotLogicOP_53 && ! (L_P1__GetInSubcl4(my_id) == false));
    if(res_NotLogicOP_53){
    xorIndex_res_XorLogicOP_17 = (xorIndex_res_XorLogicOP_17 + 1);
    }
    
    res_XorLogicOP_17 = (res_XorLogicOP_17 && (xorIndex_res_XorLogicOP_17 == 1));
    res_ImpliesLogicOp_9 = (res_ImpliesLogicOp_9 && res_XorLogicOP_17);
    }
    if(res_ImpliesLogicOp_9){
    xorIndex_res_XorLogicOP_8 = (xorIndex_res_XorLogicOP_8 + 1);
    }
    if((L_P1__GetInConsd1(my_id) == false)){
    xorIndex_res_XorLogicOP_8 = (xorIndex_res_XorLogicOP_8 + 1);
    }
    
    res_XorLogicOP_8 = (res_XorLogicOP_8 && (xorIndex_res_XorLogicOP_8 == 1));
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_XorLogicOP_8);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *47,*  *34,*  il parametro SubClass_C2_parametro_P6 sia  uguale a c270
    res_AndLogicOP_0 = (res_AndLogicOP_0 && (L_P1__GetParamSubcl9(my_id) == c270));
    
    
    
    return res_AndLogicOP_0;
}


/*
    CNL corrispondente:
    
    {
    
     commento: {86,}  Almeno una delle seguenti {
     commento: {82,}  Ricezione del comando manuale   SubClass_C2_command_comm3 da  Sender855df2bd   commento: {76,}
     commento: {82,}  Ricezione del comando manuale   SubClass_C2_command_comm3 da  Sender855df2bd   commento: {76,}
     commento: {83,}  Tutte le seguenti {
     Ricezione del  comando manuale   SubClass_C2_command_comm3 da  Sender855df2bd   commento: {76,}
     commento: {67,} commento: {35,}  se il controllo SubClass_C2_controllo_C8 non è  diverso da  True  commento: {36,} e  se il timer SubClass_C2_timer_T9 non è disattivo commento: {35,} e  se il controllo SubClass_C2_controllo_C1 non è  diverso da c270 commento: {35,} o  se il controllo SubClass_C2_controllo_C1 è  diverso da c270 commento: {37,} e  se la variabile SubClass_C2_variabile_V7 non è  diverso da RossoGialloVerde commento: {37,} o  se la variabile SubClass_C2_variabile_V7 è  uguale a RossoGialloVerde, Tutte le seguenti { 
     commento: {68,} commento: {38,}  se il contatore SubClass_C2_contatore_Co9 non è  uguale a  commento: {53,} 1545 commento: {35,} o  se il controllo SubClass_C2_controllo_C8 è  diverso da  True , Almeno una delle seguenti { 
     commento: {36,}  se il timer SubClass_C2_timer_T10 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} e  se il timer SubClass_C2_timer_T8 non è attivo commento: {38,} o  se il contatore SubClass_C2_contatore_Co4 non è  minore di  commento: {55,} 123 e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   commento: {47,}  commento: {34,}  il parametro SubClass_C2_parametro_P6 non sia  uguale a c270
    
    
     } Verifica che   commento: {51,}  commento: {,}  il contatore SubClass_C2_contatore_Co9 sia  minore di  commento: {55,} 11210
    
    
     } Verifica che   commento: {49,}  commento: {,}  il timer SubClass_C2_timer_T6 sia attivo
    
    
    }
    }
    }
*/
static inline bool L_P1__Guard5(instance_id_t const my_id)
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
    
    Comanda al campo MainClass_C1 di SubClass_C2_lista_L5
     di eseguire  commento: {113,}  MainClass_C1_command_comm7( con argomento_ave1   uguale a True ,argomento_ave10   uguale a GialloVerde )
    }
*/
static inline void L_P1__Effec3(instance_id_t const my_id)
{
    
    //  Comanda al campo MainClass_C1 di SubClass_C2_lista_L5
    //   di eseguire  *113,*  MainClass_C1_command_comm7( con argomento_ave1   uguale a True ,argomento_ave10   uguale a GialloVerde )
    for (index_t i = 0; i < L_P1__GetParamSubcl7Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl7(my_id,i);
    
    L_P1__SetCAEvent(it.mainc39,true);
    L_P1__SetCAArgom(it.mainc39,true);
    L_P1__SetCAArgom1(it.mainc39,gialloverde);
    scheduler_NotifyCommand(L_P1_C1_TO_GLOBAL(it.mainc39));
    }
}


/*
    CNL corrispondente:
     {Comanda al campo MainClass_C1 di SubClass_C2_lista_L10
     di eseguire  commento: {113,}  MainClass_C1_command_comm7( con argomento_ave1   uguale a True ,argomento_ave10   uguale a GialloVerde ) }
*/
static inline void L_P1__Effec4(instance_id_t const my_id)
{
    
    //  Comanda al campo MainClass_C1 di SubClass_C2_lista_L10
    //   di eseguire  *113,*  MainClass_C1_command_comm7( con argomento_ave1   uguale a True ,argomento_ave10   uguale a GialloVerde )
    for (index_t i = 0; i < L_P1__GetParamSubcl5Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl5(my_id,i);
    
    L_P1__SetCAEvent(it.mainc39,true);
    L_P1__SetCAArgom(it.mainc39,true);
    L_P1__SetCAArgom1(it.mainc39,gialloverde);
    scheduler_NotifyCommand(L_P1_C1_TO_GLOBAL(it.mainc39));
    }
}


/*
    CNL corrispondente:
    
    {
    
    Comanda al campo MainClass_C1 di SubClass_C2_lista_L2
     di eseguire  commento: {113,}  MainClass_C1_command_comm7( con argomento_ave1   uguale a True ,argomento_ave10   uguale a GialloVerde )
    }
*/
static inline void L_P1__Effec5(instance_id_t const my_id)
{
    
    //  Comanda al campo MainClass_C1 di SubClass_C2_lista_L2
    //   di eseguire  *113,*  MainClass_C1_command_comm7( con argomento_ave1   uguale a True ,argomento_ave10   uguale a GialloVerde )
    for (index_t i = 0; i < L_P1__GetParamSubcl6Length(my_id); ++i)
    {
    L_P1__Recor1 it = L_P1__GetRecSubcl6(my_id,i);
    
    L_P1__SetCAEvent(it.mainc40,true);
    L_P1__SetCAArgom(it.mainc40,true);
    L_P1__SetCAArgom1(it.mainc40,gialloverde);
    scheduler_NotifyCommand(L_P1_C1_TO_GLOBAL(it.mainc40));
    }
}



// ********** Definizione metodi **********

// Metodi standard

void L_P1_C2_Init(instance_id_t const my_id)
{
    // init variabili di stato
    L_P1__SetStato3(my_id, C2_St_Stato);
    L_P1__SetSubcl22(my_id, 0);
    L_P1__SetSubcl24(my_id, rossogiallo2);
    L_P1__SetSubcl26(my_id, 0);
    L_P1__SetSubcl28(my_id, giallogiall);
    L_P1__SetSubcl30(my_id, 0);
    L_P1__SetSubcl32(my_id, giallox);
    L_P1__SetSubcl33(my_id, giallox);
    L_P1__SetSubcl34(my_id, 0);
    L_P1__SetSubcl35(my_id, 0);
    L_P1__SetSubcl36(my_id, rossogiallo2);
    // init controlli precedenti
    L_P1__SetSubcl13(my_id, true);
    L_P1__SetSubcl15(my_id, false);
    L_P1__SetSubcl17(my_id, true);
    L_P1__SetSubcl19(my_id, avvio);
    L_P1__SetSubcl21(my_id, false);
    // init Timer e Counter
    Timer_AggmInit(L_P1__GetSubcl37(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl37_ID);
    Timer_Init(L_P1__GetSubcl37(my_id), 204000);
    Timer_AggmInit(L_P1__GetSubcl38(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl38_ID);
    Timer_Init(L_P1__GetSubcl38(my_id), 204000);
    Timer_AggmInit(L_P1__GetSubcl39(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl39_ID);
    Timer_Init(L_P1__GetSubcl39(my_id), 45000);
    Timer_AggmInit(L_P1__GetSubcl40(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl40_ID);
    Timer_Init(L_P1__GetSubcl40(my_id), 45000);
    Timer_AggmInit(L_P1__GetSubcl41(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl41_ID);
    Timer_Init(L_P1__GetSubcl41(my_id), 1000);
    Timer_AggmInit(L_P1__GetSubcl42(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl42_ID);
    Timer_Init(L_P1__GetSubcl42(my_id), 1000);
    Timer_AggmInit(L_P1__GetSubcl43(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl43_ID);
    Timer_Init(L_P1__GetSubcl43(my_id), 332000);
    Timer_AggmInit(L_P1__GetSubcl44(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl44_ID);
    Timer_Init(L_P1__GetSubcl44(my_id), 332000);
    Timer_AggmInit(L_P1__GetSubcl45(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl45_ID);
    Timer_Init(L_P1__GetSubcl45(my_id), 5000);
    Timer_AggmInit(L_P1__GetSubcl46(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl46_ID);
    Timer_Init(L_P1__GetSubcl46(my_id), 2000);
    Timer_AggmInit(L_P1__GetSubcl47(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl47_ID);
    Timer_Init(L_P1__GetSubcl47(my_id), 410000);
    Timer_AggmInit(L_P1__GetSubcl48(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl48_ID);
    Timer_Init(L_P1__GetSubcl48(my_id), 121000);
    Timer_AggmInit(L_P1__GetSubcl49(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl49_ID);
    Timer_Init(L_P1__GetSubcl49(my_id), 4453000);
    Counter_AggmInit(L_P1__GetSubcl50(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl50_ID);
    Counter_Init(L_P1__GetSubcl50(my_id));
    Counter_AggmInit(L_P1__GetSubcl51(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl51_ID);
    Counter_Init(L_P1__GetSubcl51(my_id));
    Counter_AggmInit(L_P1__GetSubcl52(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl52_ID);
    Counter_Init(L_P1__GetSubcl52(my_id));
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
    L_P1__SetSubcl23(my_id, L_P1__GetSubcl22(my_id));
    L_P1__SetSubcl25(my_id, L_P1__GetSubcl24(my_id));
    L_P1__SetSubcl27(my_id, L_P1__GetSubcl26(my_id));
    L_P1__SetSubcl29(my_id, L_P1__GetSubcl28(my_id));
    L_P1__SetSubcl31(my_id, L_P1__GetSubcl30(my_id));
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

        case C2_St_state:
                { } // fine transizioni da state nella fase LDS_PHASE_MANUAL
            break;

        case C2_St_state1:
            if (L_P1__Guard5(my_id)) {
                L_P1_C2_SetState(my_id, C2_St_state1);
                L_P1__Effec5(my_id);				
            }
            else
                { } // fine transizioni da state1 nella fase LDS_PHASE_MANUAL
            break;

        default:
            STOP_EXECUTION(LOGIC_ERROR);
            break;  // Needed for MISRA C syntactic compliance
        } // switch sugli stati chiuso
        break;
 

    case LDS_PHASE_STATE:

        switch (L_P1_C2_GetState(my_id)) {

        case C2_St_state:
            if (L_P1__Guard4(my_id)) {
                L_P1_C2_SetState(my_id, C2_St_state1);
                L_P1__Effec4(my_id);				
            }
            else if (L_P1__Guard3(my_id)) {
                L_P1_C2_SetState(my_id, C2_St_state);
                L_P1__Effec3(my_id);				
            }
            else
                {STOP_EXECUTION(LOGIC_ERROR); } // fine transizioni da state nella fase LDS_PHASE_STATE
            break;

        case C2_St_state1:
                {STOP_EXECUTION(LOGIC_ERROR); } // fine transizioni da state1 nella fase LDS_PHASE_STATE
            break;

        default:
            STOP_EXECUTION(LOGIC_ERROR);
            break;  // Needed for MISRA C syntactic compliance
        } // switch sugli stati chiuso
        break;


    case LDS_PHASE_AUTO:
        {
        size_t auto_commands_before = L_P1_C2_NumAutoCmds(my_id);
        switch (L_P1_C2_GetState(my_id)) {

        case C2_St_state:
                { } // fine transizioni da state nella fase LDS_PHASE_AUTO
            break;

        case C2_St_state1:
                { } // fine transizioni da state1 nella fase LDS_PHASE_AUTO
            break;

        default:
            STOP_EXECUTION(LOGIC_ERROR);
            break;  // Needed for MISRA C syntactic compliance
        } // switch sugli stati chiuso
        size_t auto_commands_after = L_P1_C2_NumAutoCmds(my_id);
        CHECK_GE(auto_commands_before, auto_commands_after);

        if ((auto_commands_after > 0u) && (auto_commands_before > auto_commands_after)) {
            L_P1_C2_SetResponse(my_id, LDS_SCHED_CONTINUE);
        } else if (auto_commands_after > 0u) {
            // TODO -- log the lost/discarded/unexpected commands
        } else {}
        }
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
    Timer_Exec(L_P1__GetSubcl37(my_id));
    Timer_Exec(L_P1__GetSubcl38(my_id));
    Timer_Exec(L_P1__GetSubcl39(my_id));
    Timer_Exec(L_P1__GetSubcl40(my_id));
    Timer_Exec(L_P1__GetSubcl41(my_id));
    Timer_Exec(L_P1__GetSubcl42(my_id));
    Timer_Exec(L_P1__GetSubcl43(my_id));
    Timer_Exec(L_P1__GetSubcl44(my_id));
    Timer_Exec(L_P1__GetSubcl45(my_id));
    Timer_Exec(L_P1__GetSubcl46(my_id));
    Timer_Exec(L_P1__GetSubcl47(my_id));
    Timer_Exec(L_P1__GetSubcl48(my_id));
    Timer_Exec(L_P1__GetSubcl49(my_id));
}

void L_P1_C2_GSetSafe(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C2(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C2(proc_id);
    L_P1__SetOutSubcl(my_id, avvio);
    L_P1__SetOutSubcl1(my_id, rossogiallo1);
}

void L_P1_C2_GUpdatePrev(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C2(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C2(proc_id);
    L_P1__SetSubcl13(my_id, L_P1__GetInSubcl12(my_id));
    L_P1__SetSubcl15(my_id, L_P1__GetInSubcl14(my_id));
    L_P1__SetSubcl17(my_id, L_P1__GetInSubcl16(my_id));
    L_P1__SetSubcl19(my_id, L_P1__GetInSubcl18(my_id));
    L_P1__SetSubcl21(my_id, L_P1__GetInSubcl20(my_id));
    L_P1__SetSubcl23(my_id, L_P1__GetSubcl22(my_id));
    L_P1__SetSubcl25(my_id, L_P1__GetSubcl24(my_id));
    L_P1__SetSubcl27(my_id, L_P1__GetSubcl26(my_id));
    L_P1__SetSubcl29(my_id, L_P1__GetSubcl28(my_id));
    L_P1__SetSubcl31(my_id, L_P1__GetSubcl30(my_id));
}

// ********** Definizione macro **********

// Macro di effetto

/*
    CNL corrispondente:
    
    { commento: {37,}  se la variabile SubClass_C2_variabile_V7 non è  uguale a RossoGialloVerde, commento: {70,}Incrementa il contatore SubClass_C2_contatore_Co8
    
       
     commento: {34,}  se il parametro SubClass_C2_parametro_P6 è  diverso da c270, commento: {71,}Decrementa il contatore SubClass_C2_contatore_Co4
    
     ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V7 il valore RossoGialloVerde
    
    
    
    }
*/
void L_P1__Macro5(instance_id_t const my_id )
{
//  *37,*  se la variabile SubClass_C2_variabile_V7 non è  uguale a RossoGialloVerde, *70,*Incrementa il contatore SubClass_C2_contatore_Co8
    bool res_NotLogicOP_0 = true;
    res_NotLogicOP_0 = (res_NotLogicOP_0 && ! (L_P1__GetSubcl36(my_id) == rossogiallo3));
    if(res_NotLogicOP_0){
    
    Counter_Incr(L_P1__GetSubcl51(my_id));
    }
    //  *34,*  se il parametro SubClass_C2_parametro_P6 è  diverso da c270, *71,*Decrementa il contatore SubClass_C2_contatore_Co4
    // ,altrimenti  *67,* Assegna alla variabile SubClass_C2_variabile_V7 il valore RossoGialloVerde
    bool res_NotLogicOP_1 = true;
    res_NotLogicOP_1 = (res_NotLogicOP_1 && ! (L_P1__GetParamSubcl9(my_id) == c270));
    if(res_NotLogicOP_1){
    
    Counter_Decr(L_P1__GetSubcl50(my_id));
    }else{
    
    L_P1__SetSubcl36(my_id,rossogiallo3);
    }
}

/*
    CNL corrispondente:
    
    { commento: {41,}  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C2_lista_L10 è  uguale a  commento: {53,} 4 o  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} e  se il controllo SubClass_C2_controllo_C8 è  uguale a  True , commento: {69,}Disattiva il timer SubClass_C2_timer_T6
    
       
    
    }
*/
void L_P1__Macro6(instance_id_t const my_id )
{
//  *41,*  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C2_lista_L10 è  uguale a  *53,* 4 o  se il controllo ConsDef  è  uguale a FALSE  *35,* e  se il controllo SubClass_C2_controllo_C8 è  uguale a  True , *69,*Disattiva il timer SubClass_C2_timer_T6
    bool res_OrLogicOP_0 = false;
    bool res_ForAllPredicate_1 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl5Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl5(my_id,i);
    bool res_ImpliesLogicOp_2 = true;
    res_ImpliesLogicOp_2 = (res_ImpliesLogicOp_2 && (L_P1__GetParamMainc7(it.mainc39) == 4u));
    res_ForAllPredicate_1 = res_ImpliesLogicOp_2;
    if(!res_ForAllPredicate_1) {break;}
    }
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_ForAllPredicate_1);
    bool res_AndLogicOP_3 = true;
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (L_P1__GetInConsd1(my_id) == false));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (L_P1__GetInSubcl4(my_id) == true));
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_3);
    
    if(res_OrLogicOP_0){
    
    Timer_Disattiva(L_P1__GetSubcl47(my_id));
    }
}

/*
    CNL corrispondente:
    
    { commento: {109,}  se il ripristino della variabile  SubClass_C2_restoreva_RV2 non è  maggiore di  commento: {54,} 9 commento: {34,} e  se il parametro SubClass_C2_parametro_P4 è  uguale a RossoGialloVerde, commento: {71,}Decrementa il contatore SubClass_C2_contatore_Co9
    
       
     commento: {34,}  se il parametro SubClass_C2_parametro_P7 non è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} e  se la variabile SubClass_C2_variabile_V7 non è  uguale a RossoGialloVerde commento: {37,} o  se la variabile SubClass_C2_variabile_V7 non è  uguale a RossoGialloVerde, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V7 il valore RossoGialloVerde
    
       
    
    }
*/
void L_P1__Macro7(instance_id_t const my_id )
{
//  *109,*  se il ripristino della variabile  SubClass_C2_restoreva_RV2 non è  maggiore di  *54,* 9 *34,* e  se il parametro SubClass_C2_parametro_P4 è  uguale a RossoGialloVerde, *71,*Decrementa il contatore SubClass_C2_contatore_Co9
    bool res_AndLogicOP_0 = true;
    bool res_NotLogicOP_1 = true;
    res_NotLogicOP_1 = (res_NotLogicOP_1 && ! (L_P1__GetSubcl35(my_id) > 9u));
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_NotLogicOP_1);
    res_AndLogicOP_0 = (res_AndLogicOP_0 && (L_P1__GetParamSubcl8(my_id) == rossogiallo3));
    
    if(res_AndLogicOP_0){
    
    Counter_Decr(L_P1__GetSubcl52(my_id));
    }
    //  *34,*  se il parametro SubClass_C2_parametro_P7 non è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE  *37,* e  se la variabile SubClass_C2_variabile_V7 non è  uguale a RossoGialloVerde *37,* o  se la variabile SubClass_C2_variabile_V7 non è  uguale a RossoGialloVerde, *67,* Assegna alla variabile SubClass_C2_variabile_V7 il valore RossoGialloVerde
    bool res_OrLogicOP_2 = false;
    bool res_AndLogicOP_3 = true;
    bool res_AndLogicOP_4 = true;
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetParamSubcl10(my_id) == false));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_5);
    res_AndLogicOP_4 = (res_AndLogicOP_4 && (L_P1__GetInConsd1(my_id) == false));
    
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_AndLogicOP_4);
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetSubcl36(my_id) == rossogiallo3));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_6);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_3);
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetSubcl36(my_id) == rossogiallo3));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_7);
    
    if(res_OrLogicOP_2){
    
    L_P1__SetSubcl36(my_id,rossogiallo3);
    }
}

/*
    CNL corrispondente:
    
    { commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  commento: {105,} è  uguale a  commento: {53,}  state1  commento: {35,} e  se il controllo SubClass_C2_controllo_C8 non è  uguale a  False  o  se l'argomento argomento_af3 è  diverso da c270 commento: {39,} ,  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V7 il valore RossoGialloVerde commento: {67,}
    
       
     commento: {36,}  se il timer SubClass_C2_timer_T10 è attivo commento: {35,} o  se il controllo SubClass_C2_controllo_C8 è  uguale a  True  commento: {34,} e  se il parametro SubClass_C2_parametro_P6 è  uguale a c270 commento: {34,} e  se il parametro SubClass_C2_parametro_P4 non è  diverso da RossoGialloVerde commento: {38,} o  se il contatore SubClass_C2_contatore_Co8 è  minore di  commento: {55,} 1210 commento: {35,} o  se il controllo SubClass_C2_controllo_C8 non è  diverso da  False , commento: {72,}Azzera il contatore SubClass_C2_contatore_Co8
    
     ,altrimenti  commento: {66,} Assegna al comando SubClass_C2_comando_C6 il valore RossoGiallo
    
    
    
    }
*/
void L_P1__Macro8(instance_id_t const my_id , C2_Enumerat3 argom23, C2_Enumerat2 argom24)
{
//  *111,*  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  *105,* è  uguale a  *53,*  state1  *35,* e  se il controllo SubClass_C2_controllo_C8 non è  uguale a  False  o  se l'argomento argomento_af3 è  diverso da c270 *39,* ,  *67,* Assegna alla variabile SubClass_C2_variabile_V7 il valore RossoGialloVerde
    bool res_OrLogicOP_0 = false;
    bool res_AndLogicOP_1 = true;
    bool res_ForAllPredicateNotEmpty_2 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl5Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl5(my_id,i);
    bool res_ImpliesLogicOp_3 = true;
    res_ImpliesLogicOp_3 = (res_ImpliesLogicOp_3 && (L_P1_C1_GetState(it.mainc39) == C1_St_state));
    res_ForAllPredicateNotEmpty_2 = res_ImpliesLogicOp_3;
    if(!res_ForAllPredicateNotEmpty_2) {break;}
    }
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_ForAllPredicateNotEmpty_2);
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetInSubcl4(my_id) == false));
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_4);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_1);
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (argom23 == c270));
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_5);
    
    if(res_OrLogicOP_0){
    
    L_P1__SetSubcl36(my_id,rossogiallo3);
    }
    //  *67,*
    //   
    // *36,*  se il timer SubClass_C2_timer_T10 è attivo *35,* o  se il controllo SubClass_C2_controllo_C8 è  uguale a  True  *34,* e  se il parametro SubClass_C2_parametro_P6 è  uguale a c270 *34,* e  se il parametro SubClass_C2_parametro_P4 non è  diverso da RossoGialloVerde *38,* o  se il contatore SubClass_C2_contatore_Co8 è  minore di  *55,* 1210 *35,* o  se il controllo SubClass_C2_controllo_C8 non è  diverso da  False , *72,*Azzera il contatore SubClass_C2_contatore_Co8
    // ,altrimenti  *66,* Assegna al comando SubClass_C2_comando_C6 il valore RossoGiallo
    bool res_OrLogicOP_6 = false;
    bool res_OrLogicOP_7 = false;
    bool res_OrLogicOP_8 = false;
    res_OrLogicOP_8 = (res_OrLogicOP_8 || Timer_Attivo(L_P1__GetSubcl45(my_id)));
    bool res_AndLogicOP_9 = true;
    bool res_AndLogicOP_10 = true;
    res_AndLogicOP_10 = (res_AndLogicOP_10 && (L_P1__GetInSubcl4(my_id) == true));
    res_AndLogicOP_10 = (res_AndLogicOP_10 && (L_P1__GetParamSubcl9(my_id) == c270));
    
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_AndLogicOP_10);
    bool res_NotLogicOP_11 = true;
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (L_P1__GetParamSubcl8(my_id) == rossogiallo3));
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! res_NotLogicOP_12);
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_NotLogicOP_11);
    
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_AndLogicOP_9);
    
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_OrLogicOP_8);
    res_OrLogicOP_7 = (res_OrLogicOP_7 || (Counter_GetValore(L_P1__GetSubcl51(my_id)) < 1210u));
    
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_OrLogicOP_7);
    bool res_NotLogicOP_13 = true;
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1__GetInSubcl4(my_id) == false));
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! res_NotLogicOP_14);
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_NotLogicOP_13);
    
    if(res_OrLogicOP_6){
    
    Counter_Res(L_P1__GetSubcl51(my_id));
    }else{
    
    L_P1__SetOutSubcl1(my_id,rossogiallo1);
    }
}


// Macro di verifica

/*
    CNL corrispondente:
    
    { commento: {63,} commento: {36,}  se il timer SubClass_C2_timer_T9 non è disattivo commento: {38,} o  se il contatore SubClass_C2_contatore_Co9 è  minore di  commento: {55,} 142 commento: {36,} o  se il timer SubClass_C2_timer_T10 è scaduto commento: {35,} o  se il controllo SubClass_C2_controllo_C8 non è  uguale a  False , Solo una delle seguenti { 
     commento: {62,} commento: {34,}  se il parametro SubClass_C2_parametro_P6 è  diverso da c270,  commento: {41,}  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  commento: {105,} è  uguale a c180, commento: {88,} quando  commento: {111,}   lo stato del campo  MainClass_C1     è  uguale a  commento: {53,}  state1  e  se l'argomento argomento_ave6 è  uguale a  False  commento: {39,}  commento: {35,} e  se il controllo SubClass_C2_controllo_C1 non è  diverso da c270 commento: {34,} o  se il parametro SubClass_C2_parametro_P4 è  diverso da RossoGialloVerde commento: {36,} o  se il timer SubClass_C2_timer_T6 è disattivo commento: {36,} o  se il timer SubClass_C2_timer_T6 è scaduto, Almeno una delle seguenti { 
     commento: {63,} commento: {43,}  se MainClass_C1_timer_T2 del campo  MainClass_C1 di SubClass_C2_lista_L5 esiste e  commento: {105,} è disattivo commento: {37,} o  se la variabile SubClass_C2_variabile_V7 è  diverso da RossoGialloVerde commento: {34,} e  se il parametro SubClass_C2_parametro_P8 è  minore di  commento: {55,} 7 commento: {35,} o  se il controllo SubClass_C2_controllo_C1 è  diverso da c270, Solo una delle seguenti { 
     commento: {62,} commento: {35,}  se il controllo SubClass_C2_controllo_C1 non è  uguale a c270 commento: {35,} o  se il controllo SubClass_C2_controllo_C7 non è  uguale a RossoGiallo commento: {38,} e  se il contatore SubClass_C2_contatore_Co9 non è  uguale a  commento: {53,} 1510, Almeno una delle seguenti { 
     commento: {63,}  se l'argomento argomento_ave5 non  è  uguale a avvio commento: {39,} ,  commento: {44,}  se  MainClass_C1_variabile_V7 del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  commento: {105,} è  uguale a c180x, commento: {88,} quando  commento: {45,}    MainClass_C1_contatore_Co7 del campo  MainClass_C1     è  diverso da  commento: {56,} 144 o  se l'argomento argomento_ave8 è  diverso da RossoGiallo commento: {39,}  commento: {38,} e  se il contatore SubClass_C2_contatore_Co8 è  diverso da  commento: {56,} 13 commento: {38,} e  se il contatore SubClass_C2_contatore_Co4 è  maggiore di  commento: {54,} 155, Solo una delle seguenti { 
     commento: {61,} commento: {41,}  se MainClass_C1_parametro_P10 del campo  MainClass_C1 di SubClass_C2_lista_L10 è  diverso da GialloVerde e  se l'argomento argomento_ave10 è  diverso da c270 commento: {39,}  commento: {37,} e  se la variabile SubClass_C2_variabile_V7 non è  diverso da RossoGialloVerde, Tutte le seguenti { 
     commento: {61,} commento: {37,}  se la variabile SubClass_C2_variabile_V7 è  uguale a RossoGialloVerde o  se l'argomento argomento_ave10 è  diverso da c270 commento: {39,}  commento: {35,} o  se il controllo SubClass_C2_controllo_C1 è  uguale a c270 commento: {36,} o  se il timer SubClass_C2_timer_T6 è disattivo commento: {38,} e  se il contatore SubClass_C2_contatore_Co8 è  minore di  commento: {55,} 111, Tutte le seguenti { 
     commento: {110,}  se il ripristino del timer  SubClass_C2_restoreTI_TI2 è disattivo, Verifica che   commento: {51,}  commento: {,}  il contatore SubClass_C2_contatore_Co9 sia  minore di  commento: {55,} 1
    
    
     } Verifica che   commento: {48,}  commento: {,}  il controllo SubClass_C2_controllo_C7 non sia  diverso da RossoGiallo
    
    
     } Verifica che   commento: {49,51,}  commento: {,}  il timer SubClass_C2_timer_T9 sia attivo
     commento: {104,} o  che  commento: {,}  il contatore SubClass_C2_contatore_Co4 non sia  minore di  commento: {55,} 1232
     commento: {104,} e  che  commento: {36,}  il timer SubClass_C2_timer_T6 sia scaduto
    
    
     } Verifica che   commento: {47,}  commento: {34,}  il parametro SubClass_C2_parametro_P4 non sia  diverso da RossoGialloVerde
    
    
     } Verifica che   commento: {51,52,}   l'argomento argomento_ave10 non  sia  diverso da c270 commento: {,} 
     commento: {104,} e  che  commento: {,}  il contatore SubClass_C2_contatore_Co9 sia  uguale a  commento: {53,} 1310
    
    
     } Verifica che   commento: {49,50,51,}  commento: {,}  la variabile SubClass_C2_variabile_V7 sia  uguale a RossoGialloVerde
     commento: {104,} o  che  commento: {,}  il contatore SubClass_C2_contatore_Co4 sia  minore di  commento: {55,} 154
     commento: {104,} o  che  commento: {,}  il timer SubClass_C2_timer_T6 sia disattivo
    
    
     } Verifica che   commento: {47,50,51,}  commento: {34,}  il parametro SubClass_C2_parametro_P6 non sia  diverso da c270
     commento: {104,} o  che  commento: {,}  la variabile SubClass_C2_variabile_V7 non sia  uguale a RossoGialloVerde
     commento: {104,} o  che  commento: {,}  il contatore SubClass_C2_contatore_Co8 sia  diverso da  commento: {56,} 13
    
    
     } Verifica che   commento: {48,51,}  commento: {,}  il controllo SubClass_C2_controllo_C7 sia  uguale a RossoGiallo
     commento: {104,} e  che  commento: {,}  il contatore SubClass_C2_contatore_Co8 sia  uguale a  commento: {53,} 1153
    
    
    }
*/
bool L_P1__Macro14(instance_id_t const my_id , C2_Enumerat3 argom42, C2_Enumerat2 argom43, C2_Enumerat2 argom44, bool argom45, C2_Enumerat1 argom46, C2_Enumerat4 argom47)
{
bool res_AndLogicOP_0 = true;
    
    //  *63,* *36,*  se il timer SubClass_C2_timer_T9 non è disattivo *38,* o  se il contatore SubClass_C2_contatore_Co9 è  minore di  *55,* 142 *36,* o  se il timer SubClass_C2_timer_T10 è scaduto *35,* o  se il controllo SubClass_C2_controllo_C8 non è  uguale a  False , Solo una delle seguenti { 
    //   *62,* *34,*  se il parametro SubClass_C2_parametro_P6 è  diverso da c270,  *41,*  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  *105,* è  uguale a c180, *88,* quando  *111,*   lo stato del campo  MainClass_C1     è  uguale a  *53,*  state1  e  se l'argomento argomento_ave6 è  uguale a  False  *39,*  *35,* e  se il controllo SubClass_C2_controllo_C1 non è  diverso da c270 *34,* o  se il parametro SubClass_C2_parametro_P4 è  diverso da RossoGialloVerde *36,* o  se il timer SubClass_C2_timer_T6 è disattivo *36,* o  se il timer SubClass_C2_timer_T6 è scaduto, Almeno una delle seguenti { 
    //   *63,* *43,*  se MainClass_C1_timer_T2 del campo  MainClass_C1 di SubClass_C2_lista_L5 esiste e  *105,* è disattivo *37,* o  se la variabile SubClass_C2_variabile_V7 è  diverso da RossoGialloVerde *34,* e  se il parametro SubClass_C2_parametro_P8 è  minore di  *55,* 7 *35,* o  se il controllo SubClass_C2_controllo_C1 è  diverso da c270, Solo una delle seguenti { 
    //   *62,* *35,*  se il controllo SubClass_C2_controllo_C1 non è  uguale a c270 *35,* o  se il controllo SubClass_C2_controllo_C7 non è  uguale a RossoGiallo *38,* e  se il contatore SubClass_C2_contatore_Co9 non è  uguale a  *53,* 1510, Almeno una delle seguenti { 
    //   *63,*  se l'argomento argomento_ave5 non  è  uguale a avvio *39,* ,  *44,*  se  MainClass_C1_variabile_V7 del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  *105,* è  uguale a c180x, *88,* quando  *45,*    MainClass_C1_contatore_Co7 del campo  MainClass_C1     è  diverso da  *56,* 144 o  se l'argomento argomento_ave8 è  diverso da RossoGiallo *39,*  *38,* e  se il contatore SubClass_C2_contatore_Co8 è  diverso da  *56,* 13 *38,* e  se il contatore SubClass_C2_contatore_Co4 è  maggiore di  *54,* 155, Solo una delle seguenti { 
    //   *61,* *41,*  se MainClass_C1_parametro_P10 del campo  MainClass_C1 di SubClass_C2_lista_L10 è  diverso da GialloVerde e  se l'argomento argomento_ave10 è  diverso da c270 *39,*  *37,* e  se la variabile SubClass_C2_variabile_V7 non è  diverso da RossoGialloVerde, Tutte le seguenti { 
    //   *61,* *37,*  se la variabile SubClass_C2_variabile_V7 è  uguale a RossoGialloVerde o  se l'argomento argomento_ave10 è  diverso da c270 *39,*  *35,* o  se il controllo SubClass_C2_controllo_C1 è  uguale a c270 *36,* o  se il timer SubClass_C2_timer_T6 è disattivo *38,* e  se il contatore SubClass_C2_contatore_Co8 è  minore di  *55,* 111, Tutte le seguenti { 
    //   *110,*  se il ripristino del timer  SubClass_C2_restoreTI_TI2 è disattivo, Verifica che   *51,*  *,*  il contatore SubClass_C2_contatore_Co9 sia  minore di  *55,* 1
    //   } Verifica che   *48,*  *,*  il controllo SubClass_C2_controllo_C7 non sia  diverso da RossoGiallo
    //   } Verifica che   *49,51,*  *,*  il timer SubClass_C2_timer_T9 sia attivo
    //   *104,* o  che  *,*  il contatore SubClass_C2_contatore_Co4 non sia  minore di  *55,* 1232
    //   *104,* e  che  *36,*  il timer SubClass_C2_timer_T6 sia scaduto
    //   } Verifica che   *47,*  *34,*  il parametro SubClass_C2_parametro_P4 non sia  diverso da RossoGialloVerde
    //   } Verifica che   *51,52,*   l'argomento argomento_ave10 non  sia  diverso da c270 *,* 
    //   *104,* e  che  *,*  il contatore SubClass_C2_contatore_Co9 sia  uguale a  *53,* 1310
    //   } Verifica che   *49,50,51,*  *,*  la variabile SubClass_C2_variabile_V7 sia  uguale a RossoGialloVerde
    //   *104,* o  che  *,*  il contatore SubClass_C2_contatore_Co4 sia  minore di  *55,* 154
    //   *104,* o  che  *,*  il timer SubClass_C2_timer_T6 sia disattivo
    //   } Verifica che   *47,50,51,*  *34,*  il parametro SubClass_C2_parametro_P6 non sia  diverso da c270
    //   *104,* o  che  *,*  la variabile SubClass_C2_variabile_V7 non sia  uguale a RossoGialloVerde
    //   *104,* o  che  *,*  il contatore SubClass_C2_contatore_Co8 sia  diverso da  *56,* 13
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_OrLogicOP_4 = false;
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! Timer_Disattivo(L_P1__GetSubcl49(my_id)));
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_NotLogicOP_5);
    res_OrLogicOP_4 = (res_OrLogicOP_4 || (Counter_GetValore(L_P1__GetSubcl52(my_id)) < 142u));
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_OrLogicOP_4);
    res_OrLogicOP_3 = (res_OrLogicOP_3 || Timer_Scaduto(L_P1__GetSubcl45(my_id)));
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetInSubcl4(my_id) == false));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_6);
    
    if(res_OrLogicOP_2){
    bool res_XorLogicOP_7 = true;
    int xorIndex_res_XorLogicOP_7 = 0;
    bool res_ImpliesLogicOp_8 = true;
    bool res_OrLogicOP_9 = false;
    bool res_OrLogicOP_10 = false;
    bool res_OrLogicOP_11 = false;
    bool res_AndLogicOP_12 = true;
    bool res_AndLogicOP_13 = true;
    bool res_AndLogicOP_14 = true;
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (L_P1__GetParamSubcl9(my_id) == c270));
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_NotLogicOP_15);
    bool res_ForAllPredicateNotEmpty_16 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl5Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl5(my_id,i);
    bool res_ImpliesLogicOp_17 = true;
    if((L_P1_C1_GetState(it.mainc39) == C1_St_state)){
    res_ImpliesLogicOp_17 = (res_ImpliesLogicOp_17 && (L_P1__GetParamMainc5(it.mainc39) == c180));
    res_ForAllPredicateNotEmpty_16 = res_ImpliesLogicOp_17;
    if(!res_ForAllPredicateNotEmpty_16) {break;}
    }
    }
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_ForAllPredicateNotEmpty_16);
    
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_AndLogicOP_14);
    res_AndLogicOP_13 = (res_AndLogicOP_13 && (argom45 == false));
    
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_AndLogicOP_13);
    bool res_NotLogicOP_18 = true;
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (L_P1__GetInSubcl2(my_id) == c270));
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! res_NotLogicOP_19);
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_NotLogicOP_18);
    
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_AndLogicOP_12);
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! (L_P1__GetParamSubcl8(my_id) == rossogiallo3));
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_NotLogicOP_20);
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_OrLogicOP_11);
    res_OrLogicOP_10 = (res_OrLogicOP_10 || Timer_Disattivo(L_P1__GetSubcl47(my_id)));
    
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_OrLogicOP_10);
    res_OrLogicOP_9 = (res_OrLogicOP_9 || Timer_Scaduto(L_P1__GetSubcl47(my_id)));
    
    if(res_OrLogicOP_9){
    bool res_OrLogicOP_21 = false;
    bool res_ImpliesLogicOp_22 = true;
    bool res_OrLogicOP_23 = false;
    bool res_OrLogicOP_24 = false;
    bool res_ForAllPredicateNotEmpty_25 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl7Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl7(my_id,i);
    bool res_ImpliesLogicOp_26 = true;
    res_ImpliesLogicOp_26 = (res_ImpliesLogicOp_26 && Timer_Disattivo(L_P1__GetMainc33(it.mainc39)));
    res_ForAllPredicateNotEmpty_25 = res_ImpliesLogicOp_26;
    if(!res_ForAllPredicateNotEmpty_25) {break;}
    }
    res_OrLogicOP_24 = (res_OrLogicOP_24 || res_ForAllPredicateNotEmpty_25);
    bool res_AndLogicOP_27 = true;
    bool res_NotLogicOP_28 = true;
    res_NotLogicOP_28 = (res_NotLogicOP_28 && ! (L_P1__GetSubcl36(my_id) == rossogiallo3));
    res_AndLogicOP_27 = (res_AndLogicOP_27 && res_NotLogicOP_28);
    res_AndLogicOP_27 = (res_AndLogicOP_27 && (L_P1__GetParamSubcl11(my_id) < 7u));
    
    res_OrLogicOP_24 = (res_OrLogicOP_24 || res_AndLogicOP_27);
    
    res_OrLogicOP_23 = (res_OrLogicOP_23 || res_OrLogicOP_24);
    bool res_NotLogicOP_29 = true;
    res_NotLogicOP_29 = (res_NotLogicOP_29 && ! (L_P1__GetInSubcl2(my_id) == c270));
    res_OrLogicOP_23 = (res_OrLogicOP_23 || res_NotLogicOP_29);
    
    if(res_OrLogicOP_23){
    bool res_XorLogicOP_30 = true;
    int xorIndex_res_XorLogicOP_30 = 0;
    bool res_ImpliesLogicOp_31 = true;
    bool res_OrLogicOP_32 = false;
    bool res_NotLogicOP_33 = true;
    res_NotLogicOP_33 = (res_NotLogicOP_33 && ! (L_P1__GetInSubcl2(my_id) == c270));
    res_OrLogicOP_32 = (res_OrLogicOP_32 || res_NotLogicOP_33);
    bool res_AndLogicOP_34 = true;
    bool res_NotLogicOP_35 = true;
    res_NotLogicOP_35 = (res_NotLogicOP_35 && ! (L_P1__GetInSubcl3(my_id) == rossogiallo1));
    res_AndLogicOP_34 = (res_AndLogicOP_34 && res_NotLogicOP_35);
    bool res_NotLogicOP_36 = true;
    res_NotLogicOP_36 = (res_NotLogicOP_36 && ! (Counter_GetValore(L_P1__GetSubcl52(my_id)) == 1510u));
    res_AndLogicOP_34 = (res_AndLogicOP_34 && res_NotLogicOP_36);
    
    res_OrLogicOP_32 = (res_OrLogicOP_32 || res_AndLogicOP_34);
    
    if(res_OrLogicOP_32){
    bool res_OrLogicOP_37 = false;
    bool res_ImpliesLogicOp_38 = true;
    bool res_OrLogicOP_39 = false;
    bool res_AndLogicOP_40 = true;
    bool res_NotLogicOP_41 = true;
    res_NotLogicOP_41 = (res_NotLogicOP_41 && ! (argom44 == avvio));
    res_AndLogicOP_40 = (res_AndLogicOP_40 && res_NotLogicOP_41);
    bool res_ForAllPredicateNotEmpty_42 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl5Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl5(my_id,i);
    bool res_ImpliesLogicOp_43 = true;
    bool res_NotLogicOP_44 = true;
    res_NotLogicOP_44 = (res_NotLogicOP_44 && ! (Counter_GetValore(L_P1__GetMainc38(it.mainc39)) == 144u));
    if(res_NotLogicOP_44){
    res_ImpliesLogicOp_43 = (res_ImpliesLogicOp_43 && (L_P1__GetMainc28(it.mainc39) == c180x));
    res_ForAllPredicateNotEmpty_42 = res_ImpliesLogicOp_43;
    if(!res_ForAllPredicateNotEmpty_42) {break;}
    }
    }
    res_AndLogicOP_40 = (res_AndLogicOP_40 && res_ForAllPredicateNotEmpty_42);
    
    res_OrLogicOP_39 = (res_OrLogicOP_39 || res_AndLogicOP_40);
    bool res_AndLogicOP_45 = true;
    bool res_AndLogicOP_46 = true;
    bool res_NotLogicOP_47 = true;
    res_NotLogicOP_47 = (res_NotLogicOP_47 && ! (argom46 == rossogiallo1));
    res_AndLogicOP_46 = (res_AndLogicOP_46 && res_NotLogicOP_47);
    bool res_NotLogicOP_48 = true;
    res_NotLogicOP_48 = (res_NotLogicOP_48 && ! (Counter_GetValore(L_P1__GetSubcl51(my_id)) == 13u));
    res_AndLogicOP_46 = (res_AndLogicOP_46 && res_NotLogicOP_48);
    
    res_AndLogicOP_45 = (res_AndLogicOP_45 && res_AndLogicOP_46);
    res_AndLogicOP_45 = (res_AndLogicOP_45 && (Counter_GetValore(L_P1__GetSubcl50(my_id)) > 155u));
    
    res_OrLogicOP_39 = (res_OrLogicOP_39 || res_AndLogicOP_45);
    
    if(res_OrLogicOP_39){
    bool res_XorLogicOP_49 = true;
    int xorIndex_res_XorLogicOP_49 = 0;
    bool res_ImpliesLogicOp_50 = true;
    bool res_AndLogicOP_51 = true;
    bool res_AndLogicOP_52 = true;
    bool res_ForAllPredicate_53 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl5Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl5(my_id,i);
    bool res_ImpliesLogicOp_54 = true;
    bool res_NotLogicOP_55 = true;
    res_NotLogicOP_55 = (res_NotLogicOP_55 && ! (L_P1__GetParamMainc6(it.mainc39) == gialloverde));
    res_ImpliesLogicOp_54 = (res_ImpliesLogicOp_54 && res_NotLogicOP_55);
    res_ForAllPredicate_53 = res_ImpliesLogicOp_54;
    if(!res_ForAllPredicate_53) {break;}
    }
    res_AndLogicOP_52 = (res_AndLogicOP_52 && res_ForAllPredicate_53);
    bool res_NotLogicOP_56 = true;
    res_NotLogicOP_56 = (res_NotLogicOP_56 && ! (argom42 == c270));
    res_AndLogicOP_52 = (res_AndLogicOP_52 && res_NotLogicOP_56);
    
    res_AndLogicOP_51 = (res_AndLogicOP_51 && res_AndLogicOP_52);
    bool res_NotLogicOP_57 = true;
    bool res_NotLogicOP_58 = true;
    res_NotLogicOP_58 = (res_NotLogicOP_58 && ! (L_P1__GetSubcl36(my_id) == rossogiallo3));
    res_NotLogicOP_57 = (res_NotLogicOP_57 && ! res_NotLogicOP_58);
    res_AndLogicOP_51 = (res_AndLogicOP_51 && res_NotLogicOP_57);
    
    if(res_AndLogicOP_51){
    bool res_AndLogicOP_59 = true;
    bool res_ImpliesLogicOp_60 = true;
    bool res_OrLogicOP_61 = false;
    bool res_OrLogicOP_62 = false;
    bool res_OrLogicOP_63 = false;
    res_OrLogicOP_63 = (res_OrLogicOP_63 || (L_P1__GetSubcl36(my_id) == rossogiallo3));
    bool res_NotLogicOP_64 = true;
    res_NotLogicOP_64 = (res_NotLogicOP_64 && ! (argom42 == c270));
    res_OrLogicOP_63 = (res_OrLogicOP_63 || res_NotLogicOP_64);
    
    res_OrLogicOP_62 = (res_OrLogicOP_62 || res_OrLogicOP_63);
    res_OrLogicOP_62 = (res_OrLogicOP_62 || (L_P1__GetInSubcl2(my_id) == c270));
    
    res_OrLogicOP_61 = (res_OrLogicOP_61 || res_OrLogicOP_62);
    bool res_AndLogicOP_65 = true;
    res_AndLogicOP_65 = (res_AndLogicOP_65 && Timer_Disattivo(L_P1__GetSubcl47(my_id)));
    res_AndLogicOP_65 = (res_AndLogicOP_65 && (Counter_GetValore(L_P1__GetSubcl51(my_id)) < 111u));
    
    res_OrLogicOP_61 = (res_OrLogicOP_61 || res_AndLogicOP_65);
    
    if(res_OrLogicOP_61){
    bool res_ImpliesLogicOp_66 = true;
    if(Timer_Disattivo(L_P1__GetSubcl40(my_id))){
    res_ImpliesLogicOp_66 = (res_ImpliesLogicOp_66 && (Counter_GetValore(L_P1__GetSubcl52(my_id)) < 1u));
    }
    res_ImpliesLogicOp_60 = (res_ImpliesLogicOp_60 && res_ImpliesLogicOp_66);
    }
    res_AndLogicOP_59 = (res_AndLogicOP_59 && res_ImpliesLogicOp_60);
    bool res_NotLogicOP_67 = true;
    bool res_NotLogicOP_68 = true;
    res_NotLogicOP_68 = (res_NotLogicOP_68 && ! (L_P1__GetInSubcl3(my_id) == rossogiallo1));
    res_NotLogicOP_67 = (res_NotLogicOP_67 && ! res_NotLogicOP_68);
    res_AndLogicOP_59 = (res_AndLogicOP_59 && res_NotLogicOP_67);
    
    res_ImpliesLogicOp_50 = (res_ImpliesLogicOp_50 && res_AndLogicOP_59);
    }
    if(res_ImpliesLogicOp_50){
    xorIndex_res_XorLogicOP_49 = (xorIndex_res_XorLogicOP_49 + 1);
    }
    bool res_OrLogicOP_69 = false;
    res_OrLogicOP_69 = (res_OrLogicOP_69 || Timer_Attivo(L_P1__GetSubcl49(my_id)));
    bool res_AndLogicOP_70 = true;
    bool res_NotLogicOP_71 = true;
    res_NotLogicOP_71 = (res_NotLogicOP_71 && ! (Counter_GetValore(L_P1__GetSubcl50(my_id)) < 1232u));
    res_AndLogicOP_70 = (res_AndLogicOP_70 && res_NotLogicOP_71);
    res_AndLogicOP_70 = (res_AndLogicOP_70 && Timer_Scaduto(L_P1__GetSubcl47(my_id)));
    
    res_OrLogicOP_69 = (res_OrLogicOP_69 || res_AndLogicOP_70);
    
    if(res_OrLogicOP_69){
    xorIndex_res_XorLogicOP_49 = (xorIndex_res_XorLogicOP_49 + 1);
    }
    
    res_XorLogicOP_49 = (res_XorLogicOP_49 && (xorIndex_res_XorLogicOP_49 == 1));
    res_ImpliesLogicOp_38 = (res_ImpliesLogicOp_38 && res_XorLogicOP_49);
    }
    res_OrLogicOP_37 = (res_OrLogicOP_37 || res_ImpliesLogicOp_38);
    bool res_NotLogicOP_72 = true;
    bool res_NotLogicOP_73 = true;
    res_NotLogicOP_73 = (res_NotLogicOP_73 && ! (L_P1__GetParamSubcl8(my_id) == rossogiallo3));
    res_NotLogicOP_72 = (res_NotLogicOP_72 && ! res_NotLogicOP_73);
    res_OrLogicOP_37 = (res_OrLogicOP_37 || res_NotLogicOP_72);
    
    res_ImpliesLogicOp_31 = (res_ImpliesLogicOp_31 && res_OrLogicOP_37);
    }
    if(res_ImpliesLogicOp_31){
    xorIndex_res_XorLogicOP_30 = (xorIndex_res_XorLogicOP_30 + 1);
    }
    bool res_AndLogicOP_74 = true;
    bool res_NotLogicOP_75 = true;
    bool res_NotLogicOP_76 = true;
    res_NotLogicOP_76 = (res_NotLogicOP_76 && ! (argom42 == c270));
    res_NotLogicOP_75 = (res_NotLogicOP_75 && ! res_NotLogicOP_76);
    res_AndLogicOP_74 = (res_AndLogicOP_74 && res_NotLogicOP_75);
    res_AndLogicOP_74 = (res_AndLogicOP_74 && (Counter_GetValore(L_P1__GetSubcl52(my_id)) == 1310u));
    
    if(res_AndLogicOP_74){
    xorIndex_res_XorLogicOP_30 = (xorIndex_res_XorLogicOP_30 + 1);
    }
    
    res_XorLogicOP_30 = (res_XorLogicOP_30 && (xorIndex_res_XorLogicOP_30 == 1));
    res_ImpliesLogicOp_22 = (res_ImpliesLogicOp_22 && res_XorLogicOP_30);
    }
    res_OrLogicOP_21 = (res_OrLogicOP_21 || res_ImpliesLogicOp_22);
    bool res_OrLogicOP_77 = false;
    bool res_OrLogicOP_78 = false;
    res_OrLogicOP_78 = (res_OrLogicOP_78 || (L_P1__GetSubcl36(my_id) == rossogiallo3));
    res_OrLogicOP_78 = (res_OrLogicOP_78 || (Counter_GetValore(L_P1__GetSubcl50(my_id)) < 154u));
    
    res_OrLogicOP_77 = (res_OrLogicOP_77 || res_OrLogicOP_78);
    res_OrLogicOP_77 = (res_OrLogicOP_77 || Timer_Disattivo(L_P1__GetSubcl47(my_id)));
    
    res_OrLogicOP_21 = (res_OrLogicOP_21 || res_OrLogicOP_77);
    
    res_ImpliesLogicOp_8 = (res_ImpliesLogicOp_8 && res_OrLogicOP_21);
    }
    if(res_ImpliesLogicOp_8){
    xorIndex_res_XorLogicOP_7 = (xorIndex_res_XorLogicOP_7 + 1);
    }
    bool res_OrLogicOP_79 = false;
    bool res_OrLogicOP_80 = false;
    bool res_NotLogicOP_81 = true;
    bool res_NotLogicOP_82 = true;
    res_NotLogicOP_82 = (res_NotLogicOP_82 && ! (L_P1__GetParamSubcl9(my_id) == c270));
    res_NotLogicOP_81 = (res_NotLogicOP_81 && ! res_NotLogicOP_82);
    res_OrLogicOP_80 = (res_OrLogicOP_80 || res_NotLogicOP_81);
    bool res_NotLogicOP_83 = true;
    res_NotLogicOP_83 = (res_NotLogicOP_83 && ! (L_P1__GetSubcl36(my_id) == rossogiallo3));
    res_OrLogicOP_80 = (res_OrLogicOP_80 || res_NotLogicOP_83);
    
    res_OrLogicOP_79 = (res_OrLogicOP_79 || res_OrLogicOP_80);
    bool res_NotLogicOP_84 = true;
    res_NotLogicOP_84 = (res_NotLogicOP_84 && ! (Counter_GetValore(L_P1__GetSubcl51(my_id)) == 13u));
    res_OrLogicOP_79 = (res_OrLogicOP_79 || res_NotLogicOP_84);
    
    if(res_OrLogicOP_79){
    xorIndex_res_XorLogicOP_7 = (xorIndex_res_XorLogicOP_7 + 1);
    }
    
    res_XorLogicOP_7 = (res_XorLogicOP_7 && (xorIndex_res_XorLogicOP_7 == 1));
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_XorLogicOP_7);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *48,51,*  *,*  il controllo SubClass_C2_controllo_C7 sia  uguale a RossoGiallo
    //   *104,* e  che  *,*  il contatore SubClass_C2_contatore_Co8 sia  uguale a  *53,* 1153
    bool res_AndLogicOP_85 = true;
    res_AndLogicOP_85 = (res_AndLogicOP_85 && (L_P1__GetInSubcl3(my_id) == rossogiallo1));
    res_AndLogicOP_85 = (res_AndLogicOP_85 && (Counter_GetValore(L_P1__GetSubcl51(my_id)) == 1153u));
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_AndLogicOP_85);
    
    
    
    return res_AndLogicOP_0;
}


// Macro valorizzate

/*
    CNL corrispondente:
    
    { commento: {[}  se l'argomento argomento_a8 è  uguale a RossoGiallo commento: {39,}  commento: {111,} e  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L10 è  uguale a  commento: {53,}  state1  commento: {35,} o  se il controllo SubClass_C2_controllo_C8 non è  uguale a  True  commento: {38,} o  se il contatore SubClass_C2_contatore_Co9 non è  uguale a  commento: {53,} 1345 commento: {37,} e  se la variabile SubClass_C2_variabile_V7 è  uguale a RossoGialloVerde , assegna alla macro il valore  False 
    
     commento: {46,} assegna alla macro il valore  True  commento: {],}
    }
*/
bool L_P1__Macro9(instance_id_t const my_id , bool argom25, C2_Enumerat1 argom26, C2_Enumerat1 argom27)
{
bool res_macro_val;
    
    //  *[*  se l'argomento argomento_a8 è  uguale a RossoGiallo *39,*  *111,* e  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L10 è  uguale a  *53,*  state1  *35,* o  se il controllo SubClass_C2_controllo_C8 non è  uguale a  True  *38,* o  se il contatore SubClass_C2_contatore_Co9 non è  uguale a  *53,* 1345 *37,* e  se la variabile SubClass_C2_variabile_V7 è  uguale a RossoGialloVerde
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_AndLogicOP_2 = true;
    res_AndLogicOP_2 = (res_AndLogicOP_2 && (argom27 == rossogiallo1));
    bool res_ForAllPredicate_3 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl5Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl5(my_id,i);
    bool res_ImpliesLogicOp_4 = true;
    res_ImpliesLogicOp_4 = (res_ImpliesLogicOp_4 && (L_P1_C1_GetState(it.mainc39) == C1_St_state));
    res_ForAllPredicate_3 = res_ImpliesLogicOp_4;
    if(!res_ForAllPredicate_3) {break;}
    }
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_ForAllPredicate_3);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_2);
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetInSubcl4(my_id) == true));
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_NotLogicOP_5);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_AndLogicOP_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (Counter_GetValore(L_P1__GetSubcl52(my_id)) == 1345u));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_7);
    res_AndLogicOP_6 = (res_AndLogicOP_6 && (L_P1__GetSubcl36(my_id) == rossogiallo3));
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_6);
    
    if(res_OrLogicOP_0){
    
    res_macro_val = false;
    }
    else{
    res_macro_val = true;
    }
    return res_macro_val;
}

/*
    CNL corrispondente:
    
    { commento: {[}  se la macro  SubClass_C2_macrova_M4 ( con argomento_a2   uguale a True ,argomento_a1   uguale a RossoGialloGiallo ,argomento_a10   uguale a c120x ,argomento_a8   uguale a RossoGialloGiallo ,argomento_a5   uguale a RossoGialloVerde  e argomento_a6   uguale a GialloGiallo )  non  è  uguale a avvio commento: {40,}  commento: {34,} e  se il parametro SubClass_C2_parametro_P8 è  uguale a  commento: {53,} 8 commento: {110,} e  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è disattivo commento: {109,} e  se il ripristino della variabile  SubClass_C2_restoreva_RV2 è  minore di  commento: {55,} 1 commento: {37,} o  se la variabile SubClass_C2_variabile_V7 è  uguale a RossoGialloVerde commento: {45,} o  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  commento: {105,} è  minore di  commento: {55,} 141 , assegna alla macro il valore  True 
    
     commento: {46,} assegna alla macro il valore  True  commento: {],}
    }
*/
bool L_P1__Macro10(instance_id_t const my_id , C2_Enumerat1 argom28, C2_Enumerat4 argom29, bool argom30)
{
bool res_macro_val;
    
    //  *[*  se la macro  SubClass_C2_macrova_M4 ( con argomento_a2   uguale a True ,argomento_a1   uguale a RossoGialloGiallo ,argomento_a10   uguale a c120x ,argomento_a8   uguale a RossoGialloGiallo ,argomento_a5   uguale a RossoGialloVerde  e argomento_a6   uguale a GialloGiallo )  non  è  uguale a avvio *40,*  *34,* e  se il parametro SubClass_C2_parametro_P8 è  uguale a  *53,* 8 *110,* e  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è disattivo *109,* e  se il ripristino della variabile  SubClass_C2_restoreva_RV2 è  minore di  *55,* 1 *37,* o  se la variabile SubClass_C2_variabile_V7 è  uguale a RossoGialloVerde *45,* o  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  *105,* è  minore di  *55,* 141
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_AndLogicOP_2 = true;
    bool res_AndLogicOP_3 = true;
    bool res_AndLogicOP_4 = true;
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__Macro11(my_id,rossogiallo2,c120x,true,rossogiallo3,giallogiall,rossogiallo2) == avvio));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_5);
    res_AndLogicOP_4 = (res_AndLogicOP_4 && (L_P1__GetParamSubcl11(my_id) == 8u));
    
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_AndLogicOP_4);
    res_AndLogicOP_3 = (res_AndLogicOP_3 && Timer_Disattivo(L_P1__GetSubcl38(my_id)));
    
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_AndLogicOP_3);
    res_AndLogicOP_2 = (res_AndLogicOP_2 && (L_P1__GetSubcl35(my_id) < 1u));
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_2);
    res_OrLogicOP_1 = (res_OrLogicOP_1 || (L_P1__GetSubcl36(my_id) == rossogiallo3));
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_ForAllPredicateNotEmpty_6 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl5Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl5(my_id,i);
    bool res_ImpliesLogicOp_7 = true;
    res_ImpliesLogicOp_7 = (res_ImpliesLogicOp_7 && (Counter_GetValore(L_P1__GetMainc36(it.mainc39)) < 141u));
    res_ForAllPredicateNotEmpty_6 = res_ImpliesLogicOp_7;
    if(!res_ForAllPredicateNotEmpty_6) {break;}
    }
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_ForAllPredicateNotEmpty_6);
    
    if(res_OrLogicOP_0){
    
    res_macro_val = true;
    }
    else{
    res_macro_val = true;
    }
    return res_macro_val;
}

/*
    CNL corrispondente:
    
    { commento: {[}
     commento: {46,} assegna alla macro il valore avvio commento: {],}
    }
*/
C2_Enumerat2 L_P1__Macro11(instance_id_t const my_id , C2_Enumerat4 argom31, C2_Enumerat1 argom32, bool argom33, C2_Enumerat4 argom34, C2_Enumerat2 argom35, C2_Enumerat4 argom36)
{
return avvio;
}

/*
    CNL corrispondente:
    
    { commento: {[}  se la macro  SubClass_C2_macrova_M10 ( con argomento_a9   uguale a True ,argomento_a4   uguale a RossoGialloVerde  e argomento_a3   uguale a c120x )  non  è  diverso da  True  commento: {40,} ,  commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L10 è  uguale a  commento: {53,}  state1 , commento: {88,} quando  commento: {43,}   MainClass_C1_timer_T4 del campo  MainClass_C1     è attivo o  se il ripristino dello stato  non è  uguale a  commento: {53,}  state1  commento: {107,} , assegna alla macro il valore RossoGiallo
    
     commento: {46,} assegna alla macro il valore RossoGiallo commento: {],}
    }
*/
C2_Enumerat1 L_P1__Macro12(instance_id_t const my_id , C2_Enumerat3 argom37, C2_Enumerat4 argom38, C2_Enumerat1 argom39)
{
C2_Enumerat1 res_macro_val;
    
    //  *[*  se la macro  SubClass_C2_macrova_M10 ( con argomento_a9   uguale a True ,argomento_a4   uguale a RossoGialloVerde  e argomento_a3   uguale a c120x )  non  è  diverso da  True  *40,* ,  *111,*  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L10 è  uguale a  *53,*  state1 , *88,* quando  *43,*   MainClass_C1_timer_T4 del campo  MainClass_C1     è attivo o  se il ripristino dello stato  non è  uguale a  *53,*  state1
    bool res_OrLogicOP_0 = false;
    bool res_AndLogicOP_1 = true;
    bool res_NotLogicOP_2 = true;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__Macro10(my_id,c120x,rossogiallo3,true) == true));
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! res_NotLogicOP_3);
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_2);
    bool res_ForAllPredicate_4 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl5Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl5(my_id,i);
    bool res_ImpliesLogicOp_5 = true;
    if(Timer_Attivo(L_P1__GetMainc35(it.mainc39))){
    res_ImpliesLogicOp_5 = (res_ImpliesLogicOp_5 && (L_P1_C1_GetState(it.mainc39) == C1_St_state));
    }
    res_ForAllPredicate_4 = res_ImpliesLogicOp_5;
    if(!res_ForAllPredicate_4) {break;}
    }
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_ForAllPredicate_4);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_1);
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetStato3(my_id) == C2_St_state));
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_6);
    
    if(res_OrLogicOP_0){
    
    res_macro_val = rossogiallo1;
    }
    else{
    res_macro_val = rossogiallo1;
    }
    return res_macro_val;
}

/*
    CNL corrispondente:
    
    { commento: {[}
     commento: {46,} assegna alla macro il valore  True  commento: {],}
    }
*/
bool L_P1__Macro13(instance_id_t const my_id , C2_Enumerat2 argom40, bool argom41)
{
return true;
}



