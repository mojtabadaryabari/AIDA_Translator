// Codice del modello 'TestCase2', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#include "Logica/ClasseMainClass_C1.h"
#include "Logica/ClasseSubClass_C2.h"
#include "Logica/ClasseSubClass_C3.h"
#include "Logica/ClasseMainClass_C1_priv.h"
#include "config.h"
#include "scheduler.h"


// ********** Gestione comandi automatici **********

static size_t L_P1_C1_NumAutoCmds(instance_id_t const my_id)
{
    size_t n = 0u;
    if (L_P1__GetCAEvent1(my_id)) {
        ++n;
    }
    return n;
}


// ********** Gestione comandi manuali **********

static void L_P1_C1_InitCmdsResponse(instance_id_t const my_id)
{
    // for each manual command of L_P1_C1
    if (L_P1__GetInEvent(my_id)) {
	    L_P1__SetOutEvent2(my_id, LDS_MANCMD_UNEXPECTED);
    } else {
        L_P1__SetOutEvent2(my_id, LDS_MANCMD_NOOP);
    }
}

static void L_P1_C1_SetExpectedCmdsResponse(instance_id_t const my_id, C1_Stateenu state)
{        
    switch (state) {
    case C1_St_state1:
        // manual commands of L_P1_C1 that can be received in C1_St_state1
	break;

    case C1_St_state:
        // manual commands of L_P1_C1 that can be received in C1_St_state
        if (L_P1__GetInEvent(my_id)) {
            L_P1__SetOutEvent2(my_id, LDS_MANCMD_BLOCKED);
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
static inline bool L_P1__Guard(instance_id_t const my_id)
{
    return true;
}


/*
    CNL corrispondente:
    
    {
    
     commento: {93,}  Tutte le seguenti {
     Ricezione del comando manuale   MainClass_C1_command_comm7   commento: {77,}
     commento: {36,}  se il timer MainClass_C1_timer_T4 è attivo e  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} e  se il controllo MainClass_C1_controllo_C7 non è  diverso da GialloxVerdex commento: {37,} o  se la variabile MainClass_C1_variabile_V6 è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   commento: {49,}  commento: {,}  il timer MainClass_C1_timer_T4 sia disattivo
    
    
    }
    }
*/
static inline bool L_P1__Guard1(instance_id_t const my_id)
{
    bool res_AndLogicOP_0 = true;
    
    //  *93,*  Tutte le seguenti {
    //   Ricezione del comando manuale   MainClass_C1_command_comm7   *77,*
    //   *36,*  se il timer MainClass_C1_timer_T4 è attivo e  se il controllo ConsDef  è  uguale a FALSE  *35,* e  se il controllo MainClass_C1_controllo_C7 non è  diverso da GialloxVerdex *37,* o  se la variabile MainClass_C1_variabile_V6 è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   *49,*  *,*  il timer MainClass_C1_timer_T4 sia disattivo
    //  }
    bool res_AndLogicOP_1 = true;
    res_AndLogicOP_1 = (res_AndLogicOP_1 && L_P1__GetInEvent(my_id));
    bool res_ImpliesLogicOp_2 = true;
    bool res_OrLogicOP_3 = false;
    bool res_OrLogicOP_4 = false;
    bool res_AndLogicOP_5 = true;
    bool res_AndLogicOP_6 = true;
    res_AndLogicOP_6 = (res_AndLogicOP_6 && Timer_Attivo(L_P1__GetMainc31(my_id)));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && (L_P1__GetInConsd(my_id) == false));
    
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_AndLogicOP_6);
    bool res_NotLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetInMainc2(my_id) == gialloxverd));
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! res_NotLogicOP_8);
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_7);
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_AndLogicOP_5);
    res_OrLogicOP_4 = (res_OrLogicOP_4 || (L_P1__GetMainc22(my_id) == false));
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_OrLogicOP_4);
    res_OrLogicOP_3 = (res_OrLogicOP_3 || (L_P1__GetInConsd(my_id) == false));
    
    if(res_OrLogicOP_3){
    res_ImpliesLogicOp_2 = (res_ImpliesLogicOp_2 && Timer_Disattivo(L_P1__GetMainc31(my_id)));
    }
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_ImpliesLogicOp_2);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_AndLogicOP_1);
    
    if(res_AndLogicOP_1){
    L_P1__SetOutEvent2(my_id,LDS_MANCMD_PROCESSED);
    }
    else{
    
    }
    
    
    return res_AndLogicOP_0;
}


/*
    CNL corrispondente:
     {  Nessuna  }
*/
static inline bool L_P1__Guard2(instance_id_t const my_id)
{
    return true;
}


/*
    CNL corrispondente:
     {  commento: {86,}  Almeno una delle seguenti {
     commento: {82,}  Ricezione del comando manuale   MainClass_C1_command_comm7   commento: {77,}
     commento: {83,}  Tutte le seguenti {
     Ricezione del  comando manuale   MainClass_C1_command_comm7   commento: {77,}
     commento: {38,}  se il contatore MainClass_C1_contatore_Co5 non è  maggiore di  commento: {54,} 13 commento: {37,} o  se la variabile MainClass_C1_variabile_V2 non è  uguale a AC commento: {34,} o  se il parametro MainClass_C1_parametro_P3 non è  uguale a c270x, Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
    
    
    } commento: {82,}  Ricezione del comando manuale   MainClass_C1_command_comm7   commento: {77,}
     commento: {83,}  Tutte le seguenti {
     Ricezione del  comando manuale   MainClass_C1_command_comm7   commento: {77,}
     commento: {69,} commento: {37,}  se la variabile MainClass_C1_variabile_V7 non è  uguale a avviox commento: {37,} e  se la variabile MainClass_C1_variabile_V7 non è  uguale a avviox commento: {37,} o  se la variabile MainClass_C1_variabile_V6 è  uguale a  True  commento: {36,} o  se il timer MainClass_C1_timer_T6 è attivo commento: {34,} e  se il parametro MainClass_C1_parametro_P3 non è  uguale a c270x commento: {37,} e  se la variabile MainClass_C1_variabile_V6 è  diverso da  True , Solo una delle seguenti { 
     commento: {68,} commento: {35,}  se il controllo MainClass_C1_controllo_C9 non è  uguale a GialloxVerdex, Almeno una delle seguenti { 
     commento: {67,}  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} o  se il parametro MainClass_C1_parametro_P3 non è  diverso da c270x, Tutte le seguenti { 
     commento: {38,}  se il contatore MainClass_C1_contatore_Co1 è  maggiore di  commento: {54,} 1415, Verifica che   commento: {50,}  commento: {,}  la variabile MainClass_C1_variabile_V6 non sia  uguale a  False 
    
    
     } Verifica che   commento: {48,}  commento: {,}  il controllo MainClass_C1_controllo_C7 sia  uguale a GialloxVerdex
    
    
     } Verifica che   commento: {48,}  commento: {,}  il controllo MainClass_C1_controllo_C7 sia  uguale a GialloxVerdex
    
    
     } Verifica che   commento: {50,}  commento: {,}  la variabile MainClass_C1_variabile_V6 non sia  uguale a  True 
    
    
    }
    } }
*/
static inline bool L_P1__Guard3(instance_id_t const my_id)
{
    bool res_AndLogicOP_0 = true;
    
    //  *86,*  Almeno una delle seguenti {
    //   *82,*  Ricezione del comando manuale   MainClass_C1_command_comm7   *77,*
    //   *83,*  Tutte le seguenti {
    //   Ricezione del  comando manuale   MainClass_C1_command_comm7   *77,*
    //   *38,*  se il contatore MainClass_C1_contatore_Co5 non è  maggiore di  *54,* 13 *37,* o  se la variabile MainClass_C1_variabile_V2 non è  uguale a AC *34,* o  se il parametro MainClass_C1_parametro_P3 non è  uguale a c270x, Verifica che   *48,*   il controllo ConsDef  sia  uguale a FALSE 
    //  } *82,*  Ricezione del comando manuale   MainClass_C1_command_comm7   *77,*
    //   *83,*  Tutte le seguenti {
    //   Ricezione del  comando manuale   MainClass_C1_command_comm7   *77,*
    //   *69,* *37,*  se la variabile MainClass_C1_variabile_V7 non è  uguale a avviox *37,* e  se la variabile MainClass_C1_variabile_V7 non è  uguale a avviox *37,* o  se la variabile MainClass_C1_variabile_V6 è  uguale a  True  *36,* o  se il timer MainClass_C1_timer_T6 è attivo *34,* e  se il parametro MainClass_C1_parametro_P3 non è  uguale a c270x *37,* e  se la variabile MainClass_C1_variabile_V6 è  diverso da  True , Solo una delle seguenti { 
    //   *68,* *35,*  se il controllo MainClass_C1_controllo_C9 non è  uguale a GialloxVerdex, Almeno una delle seguenti { 
    //   *67,*  se il controllo ConsDef  è  uguale a FALSE  *34,* o  se il parametro MainClass_C1_parametro_P3 non è  diverso da c270x, Tutte le seguenti { 
    //   *38,*  se il contatore MainClass_C1_contatore_Co1 è  maggiore di  *54,* 1415, Verifica che   *50,*  *,*  la variabile MainClass_C1_variabile_V6 non sia  uguale a  False 
    //   } Verifica che   *48,*  *,*  il controllo MainClass_C1_controllo_C7 sia  uguale a GialloxVerdex
    //   } Verifica che   *48,*  *,*  il controllo MainClass_C1_controllo_C7 sia  uguale a GialloxVerdex
    //   } Verifica che   *50,*  *,*  la variabile MainClass_C1_variabile_V6 non sia  uguale a  True 
    //  }
    //  }
    bool res_OrLogicOP_1 = false;
    res_OrLogicOP_1 = (res_OrLogicOP_1 || L_P1__GetInEvent(my_id));
    bool res_AndLogicOP_2 = true;
    res_AndLogicOP_2 = (res_AndLogicOP_2 && L_P1__GetInEvent(my_id));
    bool res_ImpliesLogicOp_3 = true;
    bool res_OrLogicOP_4 = false;
    bool res_OrLogicOP_5 = false;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (Counter_GetValore(L_P1__GetMainc35(my_id)) > 13u));
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_NotLogicOP_6);
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetMainc20(my_id) == ac));
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_NotLogicOP_7);
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_OrLogicOP_5);
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetParamMainc5(my_id) == c270x));
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_NotLogicOP_8);
    
    if(res_OrLogicOP_4){
    res_ImpliesLogicOp_3 = (res_ImpliesLogicOp_3 && (L_P1__GetInConsd(my_id) == false));
    }
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_ImpliesLogicOp_3);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_2);
    res_OrLogicOP_1 = (res_OrLogicOP_1 || L_P1__GetInEvent(my_id));
    bool res_AndLogicOP_9 = true;
    res_AndLogicOP_9 = (res_AndLogicOP_9 && L_P1__GetInEvent(my_id));
    bool res_ImpliesLogicOp_10 = true;
    bool res_OrLogicOP_11 = false;
    bool res_OrLogicOP_12 = false;
    bool res_AndLogicOP_13 = true;
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1__GetMainc23(my_id) == avviox));
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_NotLogicOP_14);
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (L_P1__GetMainc23(my_id) == avviox));
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_NotLogicOP_15);
    
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_AndLogicOP_13);
    res_OrLogicOP_12 = (res_OrLogicOP_12 || (L_P1__GetMainc22(my_id) == true));
    
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_OrLogicOP_12);
    bool res_AndLogicOP_16 = true;
    bool res_AndLogicOP_17 = true;
    res_AndLogicOP_17 = (res_AndLogicOP_17 && Timer_Attivo(L_P1__GetMainc32(my_id)));
    bool res_NotLogicOP_18 = true;
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! (L_P1__GetParamMainc5(my_id) == c270x));
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_NotLogicOP_18);
    
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_AndLogicOP_17);
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (L_P1__GetMainc22(my_id) == true));
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_NotLogicOP_19);
    
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_AndLogicOP_16);
    
    if(res_OrLogicOP_11){
    bool res_XorLogicOP_20 = true;
    int xorIndex_res_XorLogicOP_20 = 0;
    bool res_ImpliesLogicOp_21 = true;
    bool res_NotLogicOP_22 = true;
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! (L_P1__GetInMainc4(my_id) == gialloxverd));
    if(res_NotLogicOP_22){
    bool res_OrLogicOP_23 = false;
    bool res_ImpliesLogicOp_24 = true;
    bool res_OrLogicOP_25 = false;
    res_OrLogicOP_25 = (res_OrLogicOP_25 || (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_26 = true;
    bool res_NotLogicOP_27 = true;
    res_NotLogicOP_27 = (res_NotLogicOP_27 && ! (L_P1__GetParamMainc5(my_id) == c270x));
    res_NotLogicOP_26 = (res_NotLogicOP_26 && ! res_NotLogicOP_27);
    res_OrLogicOP_25 = (res_OrLogicOP_25 || res_NotLogicOP_26);
    
    if(res_OrLogicOP_25){
    bool res_ImpliesLogicOp_28 = true;
    if((Counter_GetValore(L_P1__GetMainc33(my_id)) > 1415u)){
    bool res_NotLogicOP_29 = true;
    res_NotLogicOP_29 = (res_NotLogicOP_29 && ! (L_P1__GetMainc22(my_id) == false));
    res_ImpliesLogicOp_28 = (res_ImpliesLogicOp_28 && res_NotLogicOP_29);
    }
    res_ImpliesLogicOp_24 = (res_ImpliesLogicOp_24 && res_ImpliesLogicOp_28);
    }
    res_OrLogicOP_23 = (res_OrLogicOP_23 || res_ImpliesLogicOp_24);
    res_OrLogicOP_23 = (res_OrLogicOP_23 || (L_P1__GetInMainc2(my_id) == gialloxverd));
    
    res_ImpliesLogicOp_21 = (res_ImpliesLogicOp_21 && res_OrLogicOP_23);
    }
    if(res_ImpliesLogicOp_21){
    xorIndex_res_XorLogicOP_20 = (xorIndex_res_XorLogicOP_20 + 1);
    }
    if((L_P1__GetInMainc2(my_id) == gialloxverd)){
    xorIndex_res_XorLogicOP_20 = (xorIndex_res_XorLogicOP_20 + 1);
    }
    
    res_XorLogicOP_20 = (res_XorLogicOP_20 && (xorIndex_res_XorLogicOP_20 == 1));
    res_ImpliesLogicOp_10 = (res_ImpliesLogicOp_10 && res_XorLogicOP_20);
    }
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_ImpliesLogicOp_10);
    bool res_NotLogicOP_30 = true;
    res_NotLogicOP_30 = (res_NotLogicOP_30 && ! (L_P1__GetMainc22(my_id) == true));
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_NotLogicOP_30);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_9);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_1);
    
    if(res_OrLogicOP_1){
    L_P1__SetOutEvent2(my_id,LDS_MANCMD_PROCESSED);
    }
    else{
    
    }
    
    
    return res_AndLogicOP_0;
}


/*
    CNL corrispondente:
     {  commento: {93,}  Tutte le seguenti {
     Ricezione del comando manuale   MainClass_C1_command_comm7   commento: {77,}
     commento: {69,} commento: {35,}  se il controllo MainClass_C1_controllo_C7 non è  uguale a GialloxVerdex, Solo una delle seguenti { 
     commento: {69,} commento: {36,}  se il timer MainClass_C1_timer_T6 non è attivo commento: {34,} e  se il parametro MainClass_C1_parametro_P3 non è  diverso da c270x, Solo una delle seguenti { 
     commento: {69,} commento: {34,}  se il parametro MainClass_C1_parametro_P3 non è  uguale a c270x, Solo una delle seguenti { 
     commento: {67,} commento: {38,}  se il contatore MainClass_C1_contatore_Co1 non è  uguale a  commento: {53,} 12150 commento: {38,} e  se il contatore MainClass_C1_contatore_Co1 non è  minore di  commento: {55,} 154 commento: {38,} o  se il contatore MainClass_C1_contatore_Co2 è  uguale a  commento: {53,} 11 commento: {36,} e  se il timer MainClass_C1_timer_T6 non è disattivo, Tutte le seguenti { 
     commento: {69,}  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x commento: {37,} e  se la variabile MainClass_C1_variabile_V6 non è  uguale a  True , Solo una delle seguenti { 
     commento: {68,} commento: {38,}  se il contatore MainClass_C1_contatore_Co1 non è  minore di  commento: {55,} 123 e  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro MainClass_C1_parametro_P3 non è  diverso da c270x, Almeno una delle seguenti { 
     commento: {68,} commento: {37,}  se la variabile MainClass_C1_variabile_V6 è  uguale a  True  commento: {38,} o  se il contatore MainClass_C1_contatore_Co1 non è  minore di  commento: {55,} 11 commento: {35,} e  se il controllo MainClass_C1_controllo_C5 è  uguale a c270x e  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} e  se il controllo MainClass_C1_controllo_C7 è  diverso da GialloxVerdex, Almeno una delle seguenti { 
     commento: {67,} commento: {37,}  se la variabile MainClass_C1_variabile_V2 è  uguale a AC commento: {34,} e  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x commento: {34,} o  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x commento: {36,} e  se il timer MainClass_C1_timer_T4 è disattivo, Tutte le seguenti { 
      se il controllo ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x commento: {38,} e  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  commento: {56,} 13215, Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
    
    
     } Verifica che   commento: {48,}  commento: {,}  il controllo MainClass_C1_controllo_C8 sia  diverso da c270x
    
    
     } Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
    
    
     } Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
    
    
     } Verifica che   commento: {48,}  commento: {,}  il controllo MainClass_C1_controllo_C7 sia  uguale a GialloxVerdex
    
    
     } Verifica che   commento: {50,}  commento: {,}  la variabile MainClass_C1_variabile_V6 sia  diverso da  False 
    
    
     } Verifica che   commento: {47,}  commento: {34,}  il parametro MainClass_C1_parametro_P3 sia  uguale a c270x
    
    
     } Verifica che   commento: {47,}  commento: {34,}  il parametro MainClass_C1_parametro_P3 sia  uguale a c270x
    
    
     } Verifica che   commento: {51,}  commento: {,}  il contatore MainClass_C1_contatore_Co2 non sia  diverso da  commento: {56,} 120
    
    
    } }
*/
static inline bool L_P1__Guard4(instance_id_t const my_id)
{
    bool res_AndLogicOP_0 = true;
    
    //  *93,*  Tutte le seguenti {
    //   Ricezione del comando manuale   MainClass_C1_command_comm7   *77,*
    //   *69,* *35,*  se il controllo MainClass_C1_controllo_C7 non è  uguale a GialloxVerdex, Solo una delle seguenti { 
    //   *69,* *36,*  se il timer MainClass_C1_timer_T6 non è attivo *34,* e  se il parametro MainClass_C1_parametro_P3 non è  diverso da c270x, Solo una delle seguenti { 
    //   *69,* *34,*  se il parametro MainClass_C1_parametro_P3 non è  uguale a c270x, Solo una delle seguenti { 
    //   *67,* *38,*  se il contatore MainClass_C1_contatore_Co1 non è  uguale a  *53,* 12150 *38,* e  se il contatore MainClass_C1_contatore_Co1 non è  minore di  *55,* 154 *38,* o  se il contatore MainClass_C1_contatore_Co2 è  uguale a  *53,* 11 *36,* e  se il timer MainClass_C1_timer_T6 non è disattivo, Tutte le seguenti { 
    //   *69,*  se il controllo ConsDef  è  uguale a FALSE  *34,* e  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x *37,* e  se la variabile MainClass_C1_variabile_V6 non è  uguale a  True , Solo una delle seguenti { 
    //   *68,* *38,*  se il contatore MainClass_C1_contatore_Co1 non è  minore di  *55,* 123 e  se il controllo ConsDef  è  uguale a FALSE  *34,* e  se il parametro MainClass_C1_parametro_P3 non è  diverso da c270x, Almeno una delle seguenti { 
    //   *68,* *37,*  se la variabile MainClass_C1_variabile_V6 è  uguale a  True  *38,* o  se il contatore MainClass_C1_contatore_Co1 non è  minore di  *55,* 11 *35,* e  se il controllo MainClass_C1_controllo_C5 è  uguale a c270x e  se il controllo ConsDef  è  uguale a FALSE  *35,* e  se il controllo MainClass_C1_controllo_C7 è  diverso da GialloxVerdex, Almeno una delle seguenti { 
    //   *67,* *37,*  se la variabile MainClass_C1_variabile_V2 è  uguale a AC *34,* e  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x *34,* o  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x *36,* e  se il timer MainClass_C1_timer_T4 è disattivo, Tutte le seguenti { 
    //    se il controllo ConsDef  è  uguale a FALSE  *34,* e  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x *38,* e  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  *56,* 13215, Verifica che   *48,*   il controllo ConsDef  sia  uguale a FALSE 
    //   } Verifica che   *48,*  *,*  il controllo MainClass_C1_controllo_C8 sia  diverso da c270x
    //   } Verifica che   *48,*   il controllo ConsDef  sia  uguale a FALSE 
    //   } Verifica che   *48,*   il controllo ConsDef  sia  uguale a FALSE 
    //   } Verifica che   *48,*  *,*  il controllo MainClass_C1_controllo_C7 sia  uguale a GialloxVerdex
    //   } Verifica che   *50,*  *,*  la variabile MainClass_C1_variabile_V6 sia  diverso da  False 
    //   } Verifica che   *47,*  *34,*  il parametro MainClass_C1_parametro_P3 sia  uguale a c270x
    //   } Verifica che   *47,*  *34,*  il parametro MainClass_C1_parametro_P3 sia  uguale a c270x
    //   } Verifica che   *51,*  *,*  il contatore MainClass_C1_contatore_Co2 non sia  diverso da  *56,* 120
    //  }
    bool res_AndLogicOP_1 = true;
    res_AndLogicOP_1 = (res_AndLogicOP_1 && L_P1__GetInEvent(my_id));
    bool res_ImpliesLogicOp_2 = true;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__GetInMainc2(my_id) == gialloxverd));
    if(res_NotLogicOP_3){
    bool res_XorLogicOP_4 = true;
    int xorIndex_res_XorLogicOP_4 = 0;
    bool res_ImpliesLogicOp_5 = true;
    bool res_AndLogicOP_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! Timer_Attivo(L_P1__GetMainc32(my_id)));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_7);
    bool res_NotLogicOP_8 = true;
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetParamMainc5(my_id) == c270x));
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! res_NotLogicOP_9);
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_8);
    
    if(res_AndLogicOP_6){
    bool res_XorLogicOP_10 = true;
    int xorIndex_res_XorLogicOP_10 = 0;
    bool res_ImpliesLogicOp_11 = true;
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (L_P1__GetParamMainc5(my_id) == c270x));
    if(res_NotLogicOP_12){
    bool res_XorLogicOP_13 = true;
    int xorIndex_res_XorLogicOP_13 = 0;
    bool res_ImpliesLogicOp_14 = true;
    bool res_OrLogicOP_15 = false;
    bool res_AndLogicOP_16 = true;
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! (Counter_GetValore(L_P1__GetMainc33(my_id)) == 12150u));
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_NotLogicOP_17);
    bool res_NotLogicOP_18 = true;
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! (Counter_GetValore(L_P1__GetMainc33(my_id)) < 154u));
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_NotLogicOP_18);
    
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_AndLogicOP_16);
    bool res_AndLogicOP_19 = true;
    res_AndLogicOP_19 = (res_AndLogicOP_19 && (Counter_GetValore(L_P1__GetMainc34(my_id)) == 11u));
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! Timer_Disattivo(L_P1__GetMainc32(my_id)));
    res_AndLogicOP_19 = (res_AndLogicOP_19 && res_NotLogicOP_20);
    
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_AndLogicOP_19);
    
    if(res_OrLogicOP_15){
    bool res_AndLogicOP_21 = true;
    bool res_ImpliesLogicOp_22 = true;
    bool res_AndLogicOP_23 = true;
    bool res_AndLogicOP_24 = true;
    res_AndLogicOP_24 = (res_AndLogicOP_24 && (L_P1__GetInConsd(my_id) == false));
    res_AndLogicOP_24 = (res_AndLogicOP_24 && (L_P1__GetParamMainc5(my_id) == c270x));
    
    res_AndLogicOP_23 = (res_AndLogicOP_23 && res_AndLogicOP_24);
    bool res_NotLogicOP_25 = true;
    res_NotLogicOP_25 = (res_NotLogicOP_25 && ! (L_P1__GetMainc22(my_id) == true));
    res_AndLogicOP_23 = (res_AndLogicOP_23 && res_NotLogicOP_25);
    
    if(res_AndLogicOP_23){
    bool res_XorLogicOP_26 = true;
    int xorIndex_res_XorLogicOP_26 = 0;
    bool res_ImpliesLogicOp_27 = true;
    bool res_AndLogicOP_28 = true;
    bool res_AndLogicOP_29 = true;
    bool res_NotLogicOP_30 = true;
    res_NotLogicOP_30 = (res_NotLogicOP_30 && ! (Counter_GetValore(L_P1__GetMainc33(my_id)) < 123u));
    res_AndLogicOP_29 = (res_AndLogicOP_29 && res_NotLogicOP_30);
    res_AndLogicOP_29 = (res_AndLogicOP_29 && (L_P1__GetInConsd(my_id) == false));
    
    res_AndLogicOP_28 = (res_AndLogicOP_28 && res_AndLogicOP_29);
    bool res_NotLogicOP_31 = true;
    bool res_NotLogicOP_32 = true;
    res_NotLogicOP_32 = (res_NotLogicOP_32 && ! (L_P1__GetParamMainc5(my_id) == c270x));
    res_NotLogicOP_31 = (res_NotLogicOP_31 && ! res_NotLogicOP_32);
    res_AndLogicOP_28 = (res_AndLogicOP_28 && res_NotLogicOP_31);
    
    if(res_AndLogicOP_28){
    bool res_OrLogicOP_33 = false;
    bool res_ImpliesLogicOp_34 = true;
    bool res_OrLogicOP_35 = false;
    res_OrLogicOP_35 = (res_OrLogicOP_35 || (L_P1__GetMainc22(my_id) == true));
    bool res_AndLogicOP_36 = true;
    bool res_AndLogicOP_37 = true;
    bool res_AndLogicOP_38 = true;
    bool res_NotLogicOP_39 = true;
    res_NotLogicOP_39 = (res_NotLogicOP_39 && ! (Counter_GetValore(L_P1__GetMainc33(my_id)) < 11u));
    res_AndLogicOP_38 = (res_AndLogicOP_38 && res_NotLogicOP_39);
    res_AndLogicOP_38 = (res_AndLogicOP_38 && (L_P1__GetInMainc1(my_id) == c270x));
    
    res_AndLogicOP_37 = (res_AndLogicOP_37 && res_AndLogicOP_38);
    res_AndLogicOP_37 = (res_AndLogicOP_37 && (L_P1__GetInConsd(my_id) == false));
    
    res_AndLogicOP_36 = (res_AndLogicOP_36 && res_AndLogicOP_37);
    bool res_NotLogicOP_40 = true;
    res_NotLogicOP_40 = (res_NotLogicOP_40 && ! (L_P1__GetInMainc2(my_id) == gialloxverd));
    res_AndLogicOP_36 = (res_AndLogicOP_36 && res_NotLogicOP_40);
    
    res_OrLogicOP_35 = (res_OrLogicOP_35 || res_AndLogicOP_36);
    
    if(res_OrLogicOP_35){
    bool res_OrLogicOP_41 = false;
    bool res_ImpliesLogicOp_42 = true;
    bool res_OrLogicOP_43 = false;
    bool res_AndLogicOP_44 = true;
    res_AndLogicOP_44 = (res_AndLogicOP_44 && (L_P1__GetMainc20(my_id) == ac));
    bool res_NotLogicOP_45 = true;
    res_NotLogicOP_45 = (res_NotLogicOP_45 && ! (L_P1__GetParamMainc5(my_id) == c270x));
    res_AndLogicOP_44 = (res_AndLogicOP_44 && res_NotLogicOP_45);
    
    res_OrLogicOP_43 = (res_OrLogicOP_43 || res_AndLogicOP_44);
    bool res_AndLogicOP_46 = true;
    bool res_NotLogicOP_47 = true;
    res_NotLogicOP_47 = (res_NotLogicOP_47 && ! (L_P1__GetParamMainc5(my_id) == c270x));
    res_AndLogicOP_46 = (res_AndLogicOP_46 && res_NotLogicOP_47);
    res_AndLogicOP_46 = (res_AndLogicOP_46 && Timer_Disattivo(L_P1__GetMainc31(my_id)));
    
    res_OrLogicOP_43 = (res_OrLogicOP_43 || res_AndLogicOP_46);
    
    if(res_OrLogicOP_43){
    bool res_ImpliesLogicOp_48 = true;
    bool res_AndLogicOP_49 = true;
    bool res_AndLogicOP_50 = true;
    res_AndLogicOP_50 = (res_AndLogicOP_50 && (L_P1__GetInConsd(my_id) == false));
    res_AndLogicOP_50 = (res_AndLogicOP_50 && (L_P1__GetParamMainc5(my_id) == c270x));
    
    res_AndLogicOP_49 = (res_AndLogicOP_49 && res_AndLogicOP_50);
    bool res_NotLogicOP_51 = true;
    bool res_NotLogicOP_52 = true;
    res_NotLogicOP_52 = (res_NotLogicOP_52 && ! (Counter_GetValore(L_P1__GetMainc34(my_id)) == 13215u));
    res_NotLogicOP_51 = (res_NotLogicOP_51 && ! res_NotLogicOP_52);
    res_AndLogicOP_49 = (res_AndLogicOP_49 && res_NotLogicOP_51);
    
    if(res_AndLogicOP_49){
    res_ImpliesLogicOp_48 = (res_ImpliesLogicOp_48 && (L_P1__GetInConsd(my_id) == false));
    }
    res_ImpliesLogicOp_42 = (res_ImpliesLogicOp_42 && res_ImpliesLogicOp_48);
    }
    res_OrLogicOP_41 = (res_OrLogicOP_41 || res_ImpliesLogicOp_42);
    bool res_NotLogicOP_53 = true;
    res_NotLogicOP_53 = (res_NotLogicOP_53 && ! (L_P1__GetInMainc3(my_id) == c270x));
    res_OrLogicOP_41 = (res_OrLogicOP_41 || res_NotLogicOP_53);
    
    res_ImpliesLogicOp_34 = (res_ImpliesLogicOp_34 && res_OrLogicOP_41);
    }
    res_OrLogicOP_33 = (res_OrLogicOP_33 || res_ImpliesLogicOp_34);
    res_OrLogicOP_33 = (res_OrLogicOP_33 || (L_P1__GetInConsd(my_id) == false));
    
    res_ImpliesLogicOp_27 = (res_ImpliesLogicOp_27 && res_OrLogicOP_33);
    }
    if(res_ImpliesLogicOp_27){
    xorIndex_res_XorLogicOP_26 = (xorIndex_res_XorLogicOP_26 + 1);
    }
    if((L_P1__GetInConsd(my_id) == false)){
    xorIndex_res_XorLogicOP_26 = (xorIndex_res_XorLogicOP_26 + 1);
    }
    
    res_XorLogicOP_26 = (res_XorLogicOP_26 && (xorIndex_res_XorLogicOP_26 == 1));
    res_ImpliesLogicOp_22 = (res_ImpliesLogicOp_22 && res_XorLogicOP_26);
    }
    res_AndLogicOP_21 = (res_AndLogicOP_21 && res_ImpliesLogicOp_22);
    res_AndLogicOP_21 = (res_AndLogicOP_21 && (L_P1__GetInMainc2(my_id) == gialloxverd));
    
    res_ImpliesLogicOp_14 = (res_ImpliesLogicOp_14 && res_AndLogicOP_21);
    }
    if(res_ImpliesLogicOp_14){
    xorIndex_res_XorLogicOP_13 = (xorIndex_res_XorLogicOP_13 + 1);
    }
    bool res_NotLogicOP_54 = true;
    res_NotLogicOP_54 = (res_NotLogicOP_54 && ! (L_P1__GetMainc22(my_id) == false));
    if(res_NotLogicOP_54){
    xorIndex_res_XorLogicOP_13 = (xorIndex_res_XorLogicOP_13 + 1);
    }
    
    res_XorLogicOP_13 = (res_XorLogicOP_13 && (xorIndex_res_XorLogicOP_13 == 1));
    res_ImpliesLogicOp_11 = (res_ImpliesLogicOp_11 && res_XorLogicOP_13);
    }
    if(res_ImpliesLogicOp_11){
    xorIndex_res_XorLogicOP_10 = (xorIndex_res_XorLogicOP_10 + 1);
    }
    if((L_P1__GetParamMainc5(my_id) == c270x)){
    xorIndex_res_XorLogicOP_10 = (xorIndex_res_XorLogicOP_10 + 1);
    }
    
    res_XorLogicOP_10 = (res_XorLogicOP_10 && (xorIndex_res_XorLogicOP_10 == 1));
    res_ImpliesLogicOp_5 = (res_ImpliesLogicOp_5 && res_XorLogicOP_10);
    }
    if(res_ImpliesLogicOp_5){
    xorIndex_res_XorLogicOP_4 = (xorIndex_res_XorLogicOP_4 + 1);
    }
    if((L_P1__GetParamMainc5(my_id) == c270x)){
    xorIndex_res_XorLogicOP_4 = (xorIndex_res_XorLogicOP_4 + 1);
    }
    
    res_XorLogicOP_4 = (res_XorLogicOP_4 && (xorIndex_res_XorLogicOP_4 == 1));
    res_ImpliesLogicOp_2 = (res_ImpliesLogicOp_2 && res_XorLogicOP_4);
    }
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_ImpliesLogicOp_2);
    bool res_NotLogicOP_55 = true;
    bool res_NotLogicOP_56 = true;
    res_NotLogicOP_56 = (res_NotLogicOP_56 && ! (Counter_GetValore(L_P1__GetMainc34(my_id)) == 120u));
    res_NotLogicOP_55 = (res_NotLogicOP_55 && ! res_NotLogicOP_56);
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_55);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_AndLogicOP_1);
    
    if(res_AndLogicOP_1){
    L_P1__SetOutEvent2(my_id,LDS_MANCMD_PROCESSED);
    }
    else{
    
    }
    
    
    return res_AndLogicOP_0;
}


/*
    CNL corrispondente:
    
    {
    
     Nessuna 
    }
*/
static inline bool L_P1__Guard5(instance_id_t const my_id)
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
static inline void L_P1__Effec(instance_id_t const my_id)
{
    
}


/*
    CNL corrispondente:
    
    {
    
     commento: {34,}  se il parametro MainClass_C1_parametro_P3 non è  uguale a c270x commento: {36,} o  se il timer MainClass_C1_timer_T6 è attivo commento: {35,} o  se il controllo MainClass_C1_controllo_C7 è  diverso da GialloxVerdex, commento: {70,}Incrementa il contatore MainClass_C1_contatore_Co5
    
     ,altrimenti  commento: {71,}Decrementa il contatore MainClass_C1_contatore_Co2
    
    
      se il controllo ConsDef  è  uguale a FALSE  commento: {34,} o  se il parametro MainClass_C1_parametro_P3 non è  uguale a c270x e  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} o  se la variabile MainClass_C1_variabile_V6 non è  diverso da  False  commento: {34,} e  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x commento: {35,} o  se il controllo MainClass_C1_controllo_C8 non è  diverso da c270x, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V2 il valore AC
    
     ,altrimenti  commento: {71,}Decrementa il contatore MainClass_C1_contatore_Co1
    
    
      se il controllo ConsDef è uguale a FALSE , commento: {72,}Azzera il contatore MainClass_C1_contatore_Co1
    
       
     commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  uguale a  commento: {53,} 3 commento: {36,} o  se il timer MainClass_C1_timer_T6 non è disattivo, commento: {66,} Assegna al comando MainClass_C1_comando_C2 il valore GialloxVerdex
    
     ,altrimenti  commento: {68,}Attiva il timer MainClass_C1_timer_T6
    
    
     commento: {34,}  se lo stato  non è  uguale a  commento: {53,}  state1  commento: {106,} commento: {34,} o  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x, commento: {66,} Assegna al comando MainClass_C1_comando_C2 il valore GialloxVerdex
    
     ,altrimenti   Applica gli effetti
           della macro MainClass_C1_macroef_M4  commento: {73,}
    
    
    
    }
*/
static inline void L_P1__Effec1(instance_id_t const my_id)
{
    
    //  *34,*  se il parametro MainClass_C1_parametro_P3 non è  uguale a c270x *36,* o  se il timer MainClass_C1_timer_T6 è attivo *35,* o  se il controllo MainClass_C1_controllo_C7 è  diverso da GialloxVerdex, *70,*Incrementa il contatore MainClass_C1_contatore_Co5
    //   ,altrimenti  *71,*Decrementa il contatore MainClass_C1_contatore_Co2
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (L_P1__GetParamMainc5(my_id) == c270x));
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_NotLogicOP_2);
    res_OrLogicOP_1 = (res_OrLogicOP_1 || Timer_Attivo(L_P1__GetMainc32(my_id)));
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__GetInMainc2(my_id) == gialloxverd));
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_3);
    
    if(res_OrLogicOP_0){
    
    Counter_Incr(L_P1__GetMainc35(my_id));
    }else{
    
    Counter_Decr(L_P1__GetMainc34(my_id));
    }
    
    //  se il controllo ConsDef  è  uguale a FALSE  *34,* o  se il parametro MainClass_C1_parametro_P3 non è  uguale a c270x e  se il controllo ConsDef  è  uguale a FALSE  *37,* o  se la variabile MainClass_C1_variabile_V6 non è  diverso da  False  *34,* e  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x *35,* o  se il controllo MainClass_C1_controllo_C8 non è  diverso da c270x, *67,* Assegna alla variabile MainClass_C1_variabile_V2 il valore AC
    //   ,altrimenti  *71,*Decrementa il contatore MainClass_C1_contatore_Co1
    bool res_OrLogicOP_4 = false;
    bool res_OrLogicOP_5 = false;
    bool res_OrLogicOP_6 = false;
    res_OrLogicOP_6 = (res_OrLogicOP_6 || (L_P1__GetInConsd(my_id) == false));
    bool res_AndLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetParamMainc5(my_id) == c270x));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_8);
    res_AndLogicOP_7 = (res_AndLogicOP_7 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_AndLogicOP_7);
    
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_OrLogicOP_6);
    bool res_AndLogicOP_9 = true;
    bool res_NotLogicOP_10 = true;
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (L_P1__GetMainc22(my_id) == false));
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! res_NotLogicOP_11);
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_NotLogicOP_10);
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (L_P1__GetParamMainc5(my_id) == c270x));
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_NotLogicOP_12);
    
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_AndLogicOP_9);
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_OrLogicOP_5);
    bool res_NotLogicOP_13 = true;
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1__GetInMainc3(my_id) == c270x));
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! res_NotLogicOP_14);
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_NotLogicOP_13);
    
    if(res_OrLogicOP_4){
    
    L_P1__SetMainc20(my_id,ac);
    }else{
    
    Counter_Decr(L_P1__GetMainc33(my_id));
    }
    
    //  se il controllo ConsDef è uguale a FALSE , *72,*Azzera il contatore MainClass_C1_contatore_Co1
    if((L_P1__GetInConsd(my_id) == false)){
    
    Counter_Res(L_P1__GetMainc33(my_id));
    }
    
    //  *109,*  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  uguale a  *53,* 3 *36,* o  se il timer MainClass_C1_timer_T6 non è disattivo, *66,* Assegna al comando MainClass_C1_comando_C2 il valore GialloxVerdex
    //   ,altrimenti  *68,*Attiva il timer MainClass_C1_timer_T6
    bool res_OrLogicOP_15 = false;
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (L_P1__GetMainc19(my_id) == 3u));
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_NotLogicOP_16);
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! Timer_Disattivo(L_P1__GetMainc32(my_id)));
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_NotLogicOP_17);
    
    if(res_OrLogicOP_15){
    
    L_P1__SetOutMainc(my_id,gialloxverd);
    }else{
    
    Timer_Attiva(L_P1__GetMainc32(my_id));
    }
    
    //  *34,*  se lo stato  non è  uguale a  *53,*  state1  *106,* *34,* o  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x, *66,* Assegna al comando MainClass_C1_comando_C2 il valore GialloxVerdex
    //   ,altrimenti   Applica gli effetti
    //         della macro MainClass_C1_macroef_M4
    bool res_OrLogicOP_18 = false;
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (L_P1_C1_GetState(my_id) == C1_St_state));
    res_OrLogicOP_18 = (res_OrLogicOP_18 || res_NotLogicOP_19);
    res_OrLogicOP_18 = (res_OrLogicOP_18 || (L_P1__GetParamMainc5(my_id) == c270x));
    
    if(res_OrLogicOP_18){
    
    L_P1__SetOutMainc(my_id,gialloxverd);
    }else{
    
    L_P1__Macro1(my_id);
    }
}


/*
    CNL corrispondente:
     { commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI3 è disattivo commento: {36,} e  se il timer MainClass_C1_timer_T6 è disattivo commento: {38,} e  se il contatore MainClass_C1_contatore_Co1 non è  minore di  commento: {55,} 13043,  Applica gli effetti
           della macro MainClass_C1_macroef_M3  commento: {73,}
    
       
     commento: {36,}  se il timer MainClass_C1_timer_T6 è scaduto commento: {34,} o  se il parametro MainClass_C1_parametro_P3 non è  diverso da c270x commento: {38,} e  se il contatore MainClass_C1_contatore_Co5 è  uguale a  commento: {53,} 152 commento: {35,} o  se il controllo MainClass_C1_controllo_C7 non è  uguale a GialloxVerdex commento: {34,} e  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V8 il valore c270x
    
     ,altrimenti  commento: {72,}Azzera il contatore MainClass_C1_contatore_Co2
    
    
     commento: {36,}  se il timer MainClass_C1_timer_T6 è attivo commento: {35,} e  se il controllo MainClass_C1_controllo_C8 non è  diverso da c270x commento: {37,} e  se la variabile MainClass_C1_variabile_V6 non è  diverso da  True , commento: {67,} Assegna alla variabile MainClass_C1_variabile_V6 il valore  False 
    
       
     }
*/
static inline void L_P1__Effec2(instance_id_t const my_id)
{
    
    //  *110,*  se il ripristino del timer  MainClass_C1_restoreTI_TI3 è disattivo *36,* e  se il timer MainClass_C1_timer_T6 è disattivo *38,* e  se il contatore MainClass_C1_contatore_Co1 non è  minore di  *55,* 13043,  Applica gli effetti
    //         della macro MainClass_C1_macroef_M3
    bool res_AndLogicOP_0 = true;
    bool res_AndLogicOP_1 = true;
    res_AndLogicOP_1 = (res_AndLogicOP_1 && Timer_Disattivo(L_P1__GetMainc30(my_id)));
    res_AndLogicOP_1 = (res_AndLogicOP_1 && Timer_Disattivo(L_P1__GetMainc32(my_id)));
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_AndLogicOP_1);
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (Counter_GetValore(L_P1__GetMainc33(my_id)) < 13043u));
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_NotLogicOP_2);
    
    if(res_AndLogicOP_0){
    
    L_P1__Macro(my_id);
    }
    
    //  *73,*
    //     
    //   *36,*  se il timer MainClass_C1_timer_T6 è scaduto *34,* o  se il parametro MainClass_C1_parametro_P3 non è  diverso da c270x *38,* e  se il contatore MainClass_C1_contatore_Co5 è  uguale a  *53,* 152 *35,* o  se il controllo MainClass_C1_controllo_C7 non è  uguale a GialloxVerdex *34,* e  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x, *67,* Assegna alla variabile MainClass_C1_variabile_V8 il valore c270x
    //   ,altrimenti  *72,*Azzera il contatore MainClass_C1_contatore_Co2
    bool res_OrLogicOP_3 = false;
    bool res_OrLogicOP_4 = false;
    res_OrLogicOP_4 = (res_OrLogicOP_4 || Timer_Scaduto(L_P1__GetMainc32(my_id)));
    bool res_AndLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetParamMainc5(my_id) == c270x));
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! res_NotLogicOP_7);
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_6);
    res_AndLogicOP_5 = (res_AndLogicOP_5 && (Counter_GetValore(L_P1__GetMainc35(my_id)) == 152u));
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_AndLogicOP_5);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_OrLogicOP_4);
    bool res_AndLogicOP_8 = true;
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetInMainc2(my_id) == gialloxverd));
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_9);
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__GetParamMainc5(my_id) == c270x));
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_10);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_AndLogicOP_8);
    
    if(res_OrLogicOP_3){
    
    L_P1__SetMainc24(my_id,c270x);
    }else{
    
    Counter_Res(L_P1__GetMainc34(my_id));
    }
    
    //  *36,*  se il timer MainClass_C1_timer_T6 è attivo *35,* e  se il controllo MainClass_C1_controllo_C8 non è  diverso da c270x *37,* e  se la variabile MainClass_C1_variabile_V6 non è  diverso da  True , *67,* Assegna alla variabile MainClass_C1_variabile_V6 il valore  False
    bool res_AndLogicOP_11 = true;
    bool res_AndLogicOP_12 = true;
    res_AndLogicOP_12 = (res_AndLogicOP_12 && Timer_Attivo(L_P1__GetMainc32(my_id)));
    bool res_NotLogicOP_13 = true;
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1__GetInMainc3(my_id) == c270x));
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! res_NotLogicOP_14);
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_NotLogicOP_13);
    
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_AndLogicOP_12);
    bool res_NotLogicOP_15 = true;
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (L_P1__GetMainc22(my_id) == true));
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! res_NotLogicOP_16);
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_NotLogicOP_15);
    
    if(res_AndLogicOP_11){
    
    L_P1__SetMainc22(my_id,false);
    }
}


/*
    CNL corrispondente:
     {  se la macro  MainClass_C1_macrova_M1 ( con argomento_a5   uguale a avviox ,argomento_a10   uguale a avviox ,argomento_a4   uguale a Rosso  e argomento_a3   uguale a c270x )  non  è  uguale a  False  commento: {40,} , commento: {70,}Incrementa il contatore MainClass_C1_contatore_Co1
    
       
     commento: {38,}  se il contatore MainClass_C1_contatore_Co1 non è  maggiore di  commento: {54,} 11043 commento: {36,} e  se il timer MainClass_C1_timer_T4 non è disattivo commento: {38,} e  se il contatore MainClass_C1_contatore_Co2 è  uguale a  commento: {53,} 14, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V6 il valore  True 
    
     ,altrimenti   Applica gli effetti
           della macro MainClass_C1_macroef_M3  commento: {73,}
    
    
      se il controllo ConsDef  è  uguale a FALSE  commento: {35,} e  se il controllo MainClass_C1_controllo_C7 non è  diverso da GialloxVerdex o  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} o  se il contatore MainClass_C1_contatore_Co1 non è  minore di  commento: {55,} 132 commento: {37,} e  se la variabile MainClass_C1_variabile_V2 non è  diverso da AC, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V6 il valore  False 
    
       
     commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI3 non è disattivo commento: {36,} o  se il timer MainClass_C1_timer_T4 non è disattivo e  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} o  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x commento: {36,} e  se il timer MainClass_C1_timer_T4 è attivo commento: {35,} o  se il controllo MainClass_C1_controllo_C7 è  uguale a GialloxVerdex,  Applica gli effetti
           della macro MainClass_C1_macroef_M3  commento: {73,}
    
     ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V6 il valore  True 
    
    
     }
*/
static inline void L_P1__Effec3(instance_id_t const my_id)
{
    
    //  se la macro  MainClass_C1_macrova_M1 ( con argomento_a5   uguale a avviox ,argomento_a10   uguale a avviox ,argomento_a4   uguale a Rosso  e argomento_a3   uguale a c270x )  non  è  uguale a  False  *40,* , *70,*Incrementa il contatore MainClass_C1_contatore_Co1
    bool res_NotLogicOP_0 = true;
    res_NotLogicOP_0 = (res_NotLogicOP_0 && ! (L_P1__Macro2(my_id,avviox,c270x,rosso,avviox) == false));
    if(res_NotLogicOP_0){
    
    Counter_Incr(L_P1__GetMainc33(my_id));
    }
    
    //  *38,*  se il contatore MainClass_C1_contatore_Co1 non è  maggiore di  *54,* 11043 *36,* e  se il timer MainClass_C1_timer_T4 non è disattivo *38,* e  se il contatore MainClass_C1_contatore_Co2 è  uguale a  *53,* 14, *67,* Assegna alla variabile MainClass_C1_variabile_V6 il valore  True 
    //   ,altrimenti   Applica gli effetti
    //         della macro MainClass_C1_macroef_M3
    bool res_AndLogicOP_1 = true;
    bool res_AndLogicOP_2 = true;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (Counter_GetValore(L_P1__GetMainc33(my_id)) > 11043u));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_3);
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! Timer_Disattivo(L_P1__GetMainc31(my_id)));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_4);
    
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_AndLogicOP_2);
    res_AndLogicOP_1 = (res_AndLogicOP_1 && (Counter_GetValore(L_P1__GetMainc34(my_id)) == 14u));
    
    if(res_AndLogicOP_1){
    
    L_P1__SetMainc22(my_id,true);
    }else{
    
    L_P1__Macro(my_id);
    }
    
    //  *73,*
    //    se il controllo ConsDef  è  uguale a FALSE  *35,* e  se il controllo MainClass_C1_controllo_C7 non è  diverso da GialloxVerdex o  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  *38,* o  se il contatore MainClass_C1_contatore_Co1 non è  minore di  *55,* 132 *37,* e  se la variabile MainClass_C1_variabile_V2 non è  diverso da AC, *67,* Assegna alla variabile MainClass_C1_variabile_V6 il valore  False
    bool res_OrLogicOP_5 = false;
    bool res_OrLogicOP_6 = false;
    bool res_OrLogicOP_7 = false;
    bool res_AndLogicOP_8 = true;
    res_AndLogicOP_8 = (res_AndLogicOP_8 && (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_9 = true;
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__GetInMainc2(my_id) == gialloxverd));
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! res_NotLogicOP_10);
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_9);
    
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_AndLogicOP_8);
    res_OrLogicOP_7 = (res_OrLogicOP_7 || (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_OrLogicOP_7);
    res_OrLogicOP_6 = (res_OrLogicOP_6 || (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_OrLogicOP_6);
    bool res_AndLogicOP_11 = true;
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (Counter_GetValore(L_P1__GetMainc33(my_id)) < 132u));
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_NotLogicOP_12);
    bool res_NotLogicOP_13 = true;
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1__GetMainc20(my_id) == ac));
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! res_NotLogicOP_14);
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_NotLogicOP_13);
    
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_AndLogicOP_11);
    
    if(res_OrLogicOP_5){
    
    L_P1__SetMainc22(my_id,false);
    }
    
    //  *110,*  se il ripristino del timer  MainClass_C1_restoreTI_TI3 non è disattivo *36,* o  se il timer MainClass_C1_timer_T4 non è disattivo e  se il controllo ConsDef  è  uguale a FALSE  *34,* o  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x *36,* e  se il timer MainClass_C1_timer_T4 è attivo *35,* o  se il controllo MainClass_C1_controllo_C7 è  uguale a GialloxVerdex,  Applica gli effetti
    //         della macro MainClass_C1_macroef_M3  *73,*
    //   ,altrimenti  *67,* Assegna alla variabile MainClass_C1_variabile_V6 il valore  True
    bool res_OrLogicOP_15 = false;
    bool res_OrLogicOP_16 = false;
    bool res_OrLogicOP_17 = false;
    bool res_NotLogicOP_18 = true;
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! Timer_Disattivo(L_P1__GetMainc30(my_id)));
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_NotLogicOP_18);
    bool res_AndLogicOP_19 = true;
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! Timer_Disattivo(L_P1__GetMainc31(my_id)));
    res_AndLogicOP_19 = (res_AndLogicOP_19 && res_NotLogicOP_20);
    res_AndLogicOP_19 = (res_AndLogicOP_19 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_AndLogicOP_19);
    
    res_OrLogicOP_16 = (res_OrLogicOP_16 || res_OrLogicOP_17);
    bool res_AndLogicOP_21 = true;
    bool res_NotLogicOP_22 = true;
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! (L_P1__GetParamMainc5(my_id) == c270x));
    res_AndLogicOP_21 = (res_AndLogicOP_21 && res_NotLogicOP_22);
    res_AndLogicOP_21 = (res_AndLogicOP_21 && Timer_Attivo(L_P1__GetMainc31(my_id)));
    
    res_OrLogicOP_16 = (res_OrLogicOP_16 || res_AndLogicOP_21);
    
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_OrLogicOP_16);
    res_OrLogicOP_15 = (res_OrLogicOP_15 || (L_P1__GetInMainc2(my_id) == gialloxverd));
    
    if(res_OrLogicOP_15){
    
    L_P1__Macro(my_id);
    }else{
    
    L_P1__SetMainc22(my_id,true);
    }
}


/*
    CNL corrispondente:
     { commento: {37,}  se la variabile MainClass_C1_variabile_V6 è  uguale a  False  commento: {38,} e  se il contatore MainClass_C1_contatore_Co1 non è  diverso da  commento: {56,} 144, commento: {66,} Assegna al comando MainClass_C1_comando_C2 il valore GialloxVerdex
    
     ,altrimenti   Applica gli effetti
           della macro MainClass_C1_macroef_M4  commento: {73,}
    
    
     commento: {37,}  se la variabile MainClass_C1_variabile_V6 è  diverso da  False  commento: {37,} e  se la variabile MainClass_C1_variabile_V8 è  diverso da c270x commento: {35,} o  se il controllo MainClass_C1_controllo_C8 è  diverso da c270x, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V6 il valore  False 
    
     ,altrimenti  commento: {71,}Decrementa il contatore MainClass_C1_contatore_Co5
    
    
      se il controllo ConsDef è uguale a FALSE  commento: {38,} o  se il contatore MainClass_C1_contatore_Co5 è  uguale a  commento: {53,} 1532 commento: {38,} e  se il contatore MainClass_C1_contatore_Co1 è  maggiore di  commento: {54,} 15 commento: {35,} o  se il controllo MainClass_C1_controllo_C7 è  diverso da GialloxVerdex commento: {37,} e  se la variabile MainClass_C1_variabile_V2 è  diverso da AC commento: {38,} o  se il contatore MainClass_C1_contatore_Co1 non è  maggiore di  commento: {54,} 151, commento: {70,}Incrementa il contatore MainClass_C1_contatore_Co2
    
       
      se il controllo ConsDef  è  uguale a FALSE  commento: {38,} e  se il contatore MainClass_C1_contatore_Co5 è  minore di  commento: {55,} 115 commento: {37,} e  se la variabile MainClass_C1_variabile_V6 è  uguale a  False  commento: {34,} o  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x commento: {35,} e  se il controllo MainClass_C1_controllo_C7 è  diverso da GialloxVerdex, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V2 il valore AC
    
       
     }
*/
static inline void L_P1__Effec4(instance_id_t const my_id)
{
    
    //  *37,*  se la variabile MainClass_C1_variabile_V6 è  uguale a  False  *38,* e  se il contatore MainClass_C1_contatore_Co1 non è  diverso da  *56,* 144, *66,* Assegna al comando MainClass_C1_comando_C2 il valore GialloxVerdex
    //   ,altrimenti   Applica gli effetti
    //         della macro MainClass_C1_macroef_M4
    bool res_AndLogicOP_0 = true;
    res_AndLogicOP_0 = (res_AndLogicOP_0 && (L_P1__GetMainc22(my_id) == false));
    bool res_NotLogicOP_1 = true;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (Counter_GetValore(L_P1__GetMainc33(my_id)) == 144u));
    res_NotLogicOP_1 = (res_NotLogicOP_1 && ! res_NotLogicOP_2);
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_NotLogicOP_1);
    
    if(res_AndLogicOP_0){
    
    L_P1__SetOutMainc(my_id,gialloxverd);
    }else{
    
    L_P1__Macro1(my_id);
    }
    
    //  *73,*
    //   *37,*  se la variabile MainClass_C1_variabile_V6 è  diverso da  False  *37,* e  se la variabile MainClass_C1_variabile_V8 è  diverso da c270x *35,* o  se il controllo MainClass_C1_controllo_C8 è  diverso da c270x, *67,* Assegna alla variabile MainClass_C1_variabile_V6 il valore  False 
    //   ,altrimenti  *71,*Decrementa il contatore MainClass_C1_contatore_Co5
    bool res_OrLogicOP_3 = false;
    bool res_AndLogicOP_4 = true;
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetMainc22(my_id) == false));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_5);
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetMainc24(my_id) == c270x));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_6);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_AndLogicOP_4);
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetInMainc3(my_id) == c270x));
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_NotLogicOP_7);
    
    if(res_OrLogicOP_3){
    
    L_P1__SetMainc22(my_id,false);
    }else{
    
    Counter_Decr(L_P1__GetMainc35(my_id));
    }
    
    //  se il controllo ConsDef è uguale a FALSE  *38,* o  se il contatore MainClass_C1_contatore_Co5 è  uguale a  *53,* 1532 *38,* e  se il contatore MainClass_C1_contatore_Co1 è  maggiore di  *54,* 15 *35,* o  se il controllo MainClass_C1_controllo_C7 è  diverso da GialloxVerdex *37,* e  se la variabile MainClass_C1_variabile_V2 è  diverso da AC *38,* o  se il contatore MainClass_C1_contatore_Co1 non è  maggiore di  *54,* 151, *70,*Incrementa il contatore MainClass_C1_contatore_Co2
    bool res_OrLogicOP_8 = false;
    bool res_OrLogicOP_9 = false;
    bool res_OrLogicOP_10 = false;
    res_OrLogicOP_10 = (res_OrLogicOP_10 || (L_P1__GetInConsd(my_id) == false));
    bool res_AndLogicOP_11 = true;
    res_AndLogicOP_11 = (res_AndLogicOP_11 && (Counter_GetValore(L_P1__GetMainc35(my_id)) == 1532u));
    res_AndLogicOP_11 = (res_AndLogicOP_11 && (Counter_GetValore(L_P1__GetMainc33(my_id)) > 15u));
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_AndLogicOP_11);
    
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_OrLogicOP_10);
    bool res_AndLogicOP_12 = true;
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (L_P1__GetInMainc2(my_id) == gialloxverd));
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_NotLogicOP_13);
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1__GetMainc20(my_id) == ac));
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_NotLogicOP_14);
    
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_AndLogicOP_12);
    
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_OrLogicOP_9);
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (Counter_GetValore(L_P1__GetMainc33(my_id)) > 151u));
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_NotLogicOP_15);
    
    if(res_OrLogicOP_8){
    
    Counter_Incr(L_P1__GetMainc34(my_id));
    }
    
    //  se il controllo ConsDef  è  uguale a FALSE  *38,* e  se il contatore MainClass_C1_contatore_Co5 è  minore di  *55,* 115 *37,* e  se la variabile MainClass_C1_variabile_V6 è  uguale a  False  *34,* o  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x *35,* e  se il controllo MainClass_C1_controllo_C7 è  diverso da GialloxVerdex, *67,* Assegna alla variabile MainClass_C1_variabile_V2 il valore AC
    bool res_OrLogicOP_16 = false;
    bool res_AndLogicOP_17 = true;
    bool res_AndLogicOP_18 = true;
    res_AndLogicOP_18 = (res_AndLogicOP_18 && (L_P1__GetInConsd(my_id) == false));
    res_AndLogicOP_18 = (res_AndLogicOP_18 && (Counter_GetValore(L_P1__GetMainc35(my_id)) < 115u));
    
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_AndLogicOP_18);
    res_AndLogicOP_17 = (res_AndLogicOP_17 && (L_P1__GetMainc22(my_id) == false));
    
    res_OrLogicOP_16 = (res_OrLogicOP_16 || res_AndLogicOP_17);
    bool res_AndLogicOP_19 = true;
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! (L_P1__GetParamMainc5(my_id) == c270x));
    res_AndLogicOP_19 = (res_AndLogicOP_19 && res_NotLogicOP_20);
    bool res_NotLogicOP_21 = true;
    res_NotLogicOP_21 = (res_NotLogicOP_21 && ! (L_P1__GetInMainc2(my_id) == gialloxverd));
    res_AndLogicOP_19 = (res_AndLogicOP_19 && res_NotLogicOP_21);
    
    res_OrLogicOP_16 = (res_OrLogicOP_16 || res_AndLogicOP_19);
    
    if(res_OrLogicOP_16){
    
    L_P1__SetMainc20(my_id,ac);
    }
}


/*
    CNL corrispondente:
    
    {
    
     commento: {34,}  se lo stato  non è  diverso da  commento: {56,}  state1  commento: {106,} commento: {37,} o  se la variabile MainClass_C1_variabile_V6 è  uguale a  False , commento: {68,}Attiva il timer MainClass_C1_timer_T6
    
     ,altrimenti  commento: {66,} Assegna al comando MainClass_C1_comando_C2 il valore GialloxVerdex
    
    
     commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI2 è scaduto, commento: {66,} Assegna al comando MainClass_C1_comando_C2 il valore GialloxVerdex
    
       
    
    }
*/
static inline void L_P1__Effec5(instance_id_t const my_id)
{
    
    //  *34,*  se lo stato  non è  diverso da  *56,*  state1  *106,* *37,* o  se la variabile MainClass_C1_variabile_V6 è  uguale a  False , *68,*Attiva il timer MainClass_C1_timer_T6
    //   ,altrimenti  *66,* Assegna al comando MainClass_C1_comando_C2 il valore GialloxVerdex
    bool res_OrLogicOP_0 = false;
    bool res_NotLogicOP_1 = true;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (L_P1_C1_GetState(my_id) == C1_St_state));
    res_NotLogicOP_1 = (res_NotLogicOP_1 && ! res_NotLogicOP_2);
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_1);
    res_OrLogicOP_0 = (res_OrLogicOP_0 || (L_P1__GetMainc22(my_id) == false));
    
    if(res_OrLogicOP_0){
    
    Timer_Attiva(L_P1__GetMainc32(my_id));
    }else{
    
    L_P1__SetOutMainc(my_id,gialloxverd);
    }
    
    //  *110,*  se il ripristino del timer  MainClass_C1_restoreTI_TI2 è scaduto, *66,* Assegna al comando MainClass_C1_comando_C2 il valore GialloxVerdex
    if(Timer_Scaduto(L_P1__GetMainc28(my_id))){
    
    L_P1__SetOutMainc(my_id,gialloxverd);
    }
}



// ********** Definizione metodi **********

// Metodi standard

void L_P1_C1_Init(instance_id_t const my_id)
{
    // init variabili di stato
    L_P1__SetMainc8(my_id, rossogiallo);
    L_P1__SetMainc10(my_id, false);
    L_P1__SetMainc12(my_id, false);
    L_P1__SetMainc14(my_id, false);
    L_P1__SetMainc16(my_id, 0);
    L_P1__SetMainc18(my_id, 0);
    L_P1__SetMainc19(my_id, 0);
    L_P1__SetMainc20(my_id, rossogiallo);
    L_P1__SetMainc21(my_id, rosso);
    L_P1__SetMainc22(my_id, false);
    L_P1__SetMainc23(my_id, rosso);
    L_P1__SetMainc24(my_id, c180x);
    L_P1__SetStato1(my_id, C1_St_Stato);
    // init controlli precedenti
    L_P1__SetMainc7(my_id, false);
    // init Timer e Counter
    Timer_AggmInit(L_P1__GetMainc25(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc25_ID);
    Timer_Init(L_P1__GetMainc25(my_id), 2000);
    Timer_AggmInit(L_P1__GetMainc26(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc26_ID);
    Timer_Init(L_P1__GetMainc26(my_id), 2000);
    Timer_AggmInit(L_P1__GetMainc27(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc27_ID);
    Timer_Init(L_P1__GetMainc27(my_id), 5000);
    Timer_AggmInit(L_P1__GetMainc28(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc28_ID);
    Timer_Init(L_P1__GetMainc28(my_id), 5000);
    Timer_AggmInit(L_P1__GetMainc29(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc29_ID);
    Timer_Init(L_P1__GetMainc29(my_id), 40000);
    Timer_AggmInit(L_P1__GetMainc30(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc30_ID);
    Timer_Init(L_P1__GetMainc30(my_id), 40000);
    Timer_AggmInit(L_P1__GetMainc31(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc31_ID);
    Timer_Init(L_P1__GetMainc31(my_id), 5432000);
    Timer_AggmInit(L_P1__GetMainc32(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc32_ID);
    Timer_Init(L_P1__GetMainc32(my_id), 415000);
    Counter_AggmInit(L_P1__GetMainc33(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc33_ID);
    Counter_Init(L_P1__GetMainc33(my_id));
    Counter_AggmInit(L_P1__GetMainc34(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc34_ID);
    Counter_Init(L_P1__GetMainc34(my_id));
    Counter_AggmInit(L_P1__GetMainc35(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc35_ID);
    Counter_Init(L_P1__GetMainc35(my_id));
    // init response
    L_P1_C1_SetResponse(my_id, LDS_SCHED_NOP);

    // transizione iniziale
    if(L_P1__Guard(my_id)) {
        L_P1_C1_SetState(my_id, C1_St_state);
	L_P1__Effec(my_id);
    } else {
        STOP_EXECUTION(LOGIC_ERROR);
    }
    // init variabili precedenti
    L_P1__SetMainc9(my_id, L_P1__GetMainc8(my_id));
    L_P1__SetMainc11(my_id, L_P1__GetMainc10(my_id));
    L_P1__SetMainc13(my_id, L_P1__GetMainc12(my_id));
    L_P1__SetMainc15(my_id, L_P1__GetMainc14(my_id));
    L_P1__SetMainc17(my_id, L_P1__GetMainc16(my_id));
}

void L_P1_C1_Exec(instance_id_t const my_id, Phase const p)
{
    L_P1_C1_SetResponse(my_id, LDS_SCHED_NOP);
    switch (p) {

    case LDS_PHASE_MANUAL:
        // Reset risposte ai comandi manuali
        L_P1_C1_InitCmdsResponse(my_id);
	L_P1_C1_SetExpectedCmdsResponse(my_id, L_P1_C1_GetState(my_id));
        switch (L_P1_C1_GetState(my_id)) {

        case C1_St_state1:
                { } // fine transizioni da state1 nella fase LDS_PHASE_MANUAL
            break;

        case C1_St_state:
            if (L_P1__Guard3(my_id)) {
                L_P1_C1_SetState(my_id, C1_St_state1);
                L_P1__Effec3(my_id);				
            }
            else if (L_P1__Guard4(my_id)) {
                L_P1_C1_SetState(my_id, C1_St_state);
                L_P1__Effec4(my_id);				
            }
            else if (L_P1__Guard1(my_id)) {
                L_P1_C1_SetState(my_id, C1_St_state);
                L_P1__Effec1(my_id);				
            }
            else
                { } // fine transizioni da state nella fase LDS_PHASE_MANUAL
            break;

        default:
            STOP_EXECUTION(LOGIC_ERROR);
            break;  // Needed for MISRA C syntactic compliance
        } // switch sugli stati chiuso
        break;
 

    case LDS_PHASE_STATE:

        switch (L_P1_C1_GetState(my_id)) {

        case C1_St_state1:
            if (L_P1__Guard5(my_id)) {
                L_P1_C1_SetState(my_id, C1_St_state1);
                L_P1__Effec5(my_id);				
            }
            else
                {STOP_EXECUTION(LOGIC_ERROR); } // fine transizioni da state1 nella fase LDS_PHASE_STATE
            break;

        case C1_St_state:
            if (L_P1__Guard2(my_id)) {
                L_P1_C1_SetState(my_id, C1_St_state1);
                L_P1__Effec2(my_id);				
            }
            else
                {STOP_EXECUTION(LOGIC_ERROR); } // fine transizioni da state nella fase LDS_PHASE_STATE
            break;

        default:
            STOP_EXECUTION(LOGIC_ERROR);
            break;  // Needed for MISRA C syntactic compliance
        } // switch sugli stati chiuso
        break;


    case LDS_PHASE_AUTO:
        {
        size_t auto_commands_before = L_P1_C1_NumAutoCmds(my_id);
        switch (L_P1_C1_GetState(my_id)) {

        case C1_St_state1:
                { } // fine transizioni da state1 nella fase LDS_PHASE_AUTO
            break;

        case C1_St_state:
                { } // fine transizioni da state nella fase LDS_PHASE_AUTO
            break;

        default:
            STOP_EXECUTION(LOGIC_ERROR);
            break;  // Needed for MISRA C syntactic compliance
        } // switch sugli stati chiuso
        size_t auto_commands_after = L_P1_C1_NumAutoCmds(my_id);
        CHECK_GE(auto_commands_before, auto_commands_after);

        if ((auto_commands_after > 0u) && (auto_commands_before > auto_commands_after)) {
            L_P1_C1_SetResponse(my_id, LDS_SCHED_CONTINUE);
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

ExecResponse L_P1_C1_GExec(global_id_t const proc_id, Phase const p)
{
    CHECK_LT(GLOBAL_TO_L_P1_C1(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C1(proc_id);
    L_P1_C1_Exec(my_id, p);
    return L_P1_C1_GetResponse(my_id);
}

void L_P1_C1_GTick(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C1(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C1(proc_id);
    Timer_Exec(L_P1__GetMainc25(my_id));
    Timer_Exec(L_P1__GetMainc26(my_id));
    Timer_Exec(L_P1__GetMainc27(my_id));
    Timer_Exec(L_P1__GetMainc28(my_id));
    Timer_Exec(L_P1__GetMainc29(my_id));
    Timer_Exec(L_P1__GetMainc30(my_id));
    Timer_Exec(L_P1__GetMainc31(my_id));
    Timer_Exec(L_P1__GetMainc32(my_id));
}

void L_P1_C1_GSetSafe(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C1(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C1(proc_id);
    L_P1__SetOutMainc(my_id, gialloxverd);
}

void L_P1_C1_GUpdatePrev(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C1(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C1(proc_id);
    L_P1__SetMainc7(my_id, L_P1__GetInMainc6(my_id));
    L_P1__SetMainc9(my_id, L_P1__GetMainc8(my_id));
    L_P1__SetMainc11(my_id, L_P1__GetMainc10(my_id));
    L_P1__SetMainc13(my_id, L_P1__GetMainc12(my_id));
    L_P1__SetMainc15(my_id, L_P1__GetMainc14(my_id));
    L_P1__SetMainc17(my_id, L_P1__GetMainc16(my_id));
}

// ********** Definizione macro **********

// Macro di effetto

/*
    CNL corrispondente:
    
    {  se la macro  MainClass_C1_macrova_M1 ( con argomento_a5   uguale a avviox ,argomento_a10   uguale a Rosso ,argomento_a4   uguale a avviox  e argomento_a3   uguale a c270x )   è  diverso da  False  commento: {40,}  commento: {37,} e  se la variabile MainClass_C1_variabile_V8 è  diverso da c270x commento: {37,} o  se la variabile MainClass_C1_variabile_V5 non è  uguale a avviox commento: {35,} o  se il controllo MainClass_C1_controllo_C7 non è  diverso da GialloxVerdex commento: {34,} e  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x o  se il controllo ConsDef  è  uguale a FALSE , commento: {66,} Assegna al comando MainClass_C1_comando_C2 il valore GialloxVerdex
    
     ,altrimenti  commento: {68,}Attiva il timer MainClass_C1_timer_T6
    
    
      se il controllo ConsDef è uguale a FALSE , commento: {67,} Assegna alla variabile MainClass_C1_variabile_V8 il valore c270x
    
     ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V6 il valore  True 
    
    
      se il controllo ConsDef  è  uguale a FALSE  commento: {38,} o  se il contatore MainClass_C1_contatore_Co1 è  maggiore di  commento: {54,} 12 commento: {35,} o  se il controllo MainClass_C1_controllo_C7 è  diverso da GialloxVerdex commento: {38,} e  se il contatore MainClass_C1_contatore_Co1 non è  minore di  commento: {55,} 115 o  se il controllo ConsDef  è  uguale a FALSE , commento: {66,} Assegna al comando MainClass_C1_comando_C2 il valore GialloxVerdex
    
     ,altrimenti  commento: {66,} Assegna al comando MainClass_C1_comando_C2 il valore GialloxVerdex
    
    
     commento: {35,}  se il controllo MainClass_C1_controllo_C7 è  diverso da GialloxVerdex commento: {35,} o  se il controllo MainClass_C1_controllo_C8 è  diverso da c270x commento: {38,} e  se il contatore MainClass_C1_contatore_Co1 non è  diverso da  commento: {56,} 1304, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V8 il valore c270x
    
       
     commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  maggiore di  commento: {54,} 4 commento: {38,} e  se il contatore MainClass_C1_contatore_Co5 non è  diverso da  commento: {56,} 1132 commento: {38,} o  se il contatore MainClass_C1_contatore_Co1 non è  maggiore di  commento: {54,} 13, commento: {70,}Incrementa il contatore MainClass_C1_contatore_Co5
    
       
    
    }
*/
void L_P1__Macro(instance_id_t const my_id )
{
//  se la macro  MainClass_C1_macrova_M1 ( con argomento_a5   uguale a avviox ,argomento_a10   uguale a Rosso ,argomento_a4   uguale a avviox  e argomento_a3   uguale a c270x )   è  diverso da  False  *40,*  *37,* e  se la variabile MainClass_C1_variabile_V8 è  diverso da c270x *37,* o  se la variabile MainClass_C1_variabile_V5 non è  uguale a avviox *35,* o  se il controllo MainClass_C1_controllo_C7 non è  diverso da GialloxVerdex *34,* e  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x o  se il controllo ConsDef  è  uguale a FALSE , *66,* Assegna al comando MainClass_C1_comando_C2 il valore GialloxVerdex
    // ,altrimenti  *68,*Attiva il timer MainClass_C1_timer_T6
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_OrLogicOP_2 = false;
    bool res_AndLogicOP_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__Macro2(my_id,rosso,c270x,avviox,avviox) == false));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_4);
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetMainc24(my_id) == c270x));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_5);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_3);
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetMainc21(my_id) == avviox));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_6);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_OrLogicOP_2);
    bool res_AndLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetInMainc2(my_id) == gialloxverd));
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! res_NotLogicOP_9);
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_8);
    res_AndLogicOP_7 = (res_AndLogicOP_7 && (L_P1__GetParamMainc5(my_id) == c270x));
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_7);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    res_OrLogicOP_0 = (res_OrLogicOP_0 || (L_P1__GetInConsd(my_id) == false));
    
    if(res_OrLogicOP_0){
    
    L_P1__SetOutMainc(my_id,gialloxverd);
    }else{
    
    Timer_Attiva(L_P1__GetMainc32(my_id));
    }
    //  se il controllo ConsDef è uguale a FALSE , *67,* Assegna alla variabile MainClass_C1_variabile_V8 il valore c270x
    // ,altrimenti  *67,* Assegna alla variabile MainClass_C1_variabile_V6 il valore  True
    if((L_P1__GetInConsd(my_id) == false)){
    
    L_P1__SetMainc24(my_id,c270x);
    }else{
    
    L_P1__SetMainc22(my_id,true);
    }
    //  se il controllo ConsDef  è  uguale a FALSE  *38,* o  se il contatore MainClass_C1_contatore_Co1 è  maggiore di  *54,* 12 *35,* o  se il controllo MainClass_C1_controllo_C7 è  diverso da GialloxVerdex *38,* e  se il contatore MainClass_C1_contatore_Co1 non è  minore di  *55,* 115 o  se il controllo ConsDef  è  uguale a FALSE , *66,* Assegna al comando MainClass_C1_comando_C2 il valore GialloxVerdex
    // ,altrimenti  *66,* Assegna al comando MainClass_C1_comando_C2 il valore GialloxVerdex
    bool res_OrLogicOP_10 = false;
    bool res_OrLogicOP_11 = false;
    bool res_OrLogicOP_12 = false;
    res_OrLogicOP_12 = (res_OrLogicOP_12 || (L_P1__GetInConsd(my_id) == false));
    res_OrLogicOP_12 = (res_OrLogicOP_12 || (Counter_GetValore(L_P1__GetMainc33(my_id)) > 12u));
    
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_OrLogicOP_12);
    bool res_AndLogicOP_13 = true;
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1__GetInMainc2(my_id) == gialloxverd));
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_NotLogicOP_14);
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (Counter_GetValore(L_P1__GetMainc33(my_id)) < 115u));
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_NotLogicOP_15);
    
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_AndLogicOP_13);
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_OrLogicOP_11);
    res_OrLogicOP_10 = (res_OrLogicOP_10 || (L_P1__GetInConsd(my_id) == false));
    
    if(res_OrLogicOP_10){
    
    L_P1__SetOutMainc(my_id,gialloxverd);
    }else{
    
    L_P1__SetOutMainc(my_id,gialloxverd);
    }
    //  *35,*  se il controllo MainClass_C1_controllo_C7 è  diverso da GialloxVerdex *35,* o  se il controllo MainClass_C1_controllo_C8 è  diverso da c270x *38,* e  se il contatore MainClass_C1_contatore_Co1 non è  diverso da  *56,* 1304, *67,* Assegna alla variabile MainClass_C1_variabile_V8 il valore c270x
    bool res_OrLogicOP_16 = false;
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! (L_P1__GetInMainc2(my_id) == gialloxverd));
    res_OrLogicOP_16 = (res_OrLogicOP_16 || res_NotLogicOP_17);
    bool res_AndLogicOP_18 = true;
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (L_P1__GetInMainc3(my_id) == c270x));
    res_AndLogicOP_18 = (res_AndLogicOP_18 && res_NotLogicOP_19);
    bool res_NotLogicOP_20 = true;
    bool res_NotLogicOP_21 = true;
    res_NotLogicOP_21 = (res_NotLogicOP_21 && ! (Counter_GetValore(L_P1__GetMainc33(my_id)) == 1304u));
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! res_NotLogicOP_21);
    res_AndLogicOP_18 = (res_AndLogicOP_18 && res_NotLogicOP_20);
    
    res_OrLogicOP_16 = (res_OrLogicOP_16 || res_AndLogicOP_18);
    
    if(res_OrLogicOP_16){
    
    L_P1__SetMainc24(my_id,c270x);
    }
    //  *109,*  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  maggiore di  *54,* 4 *38,* e  se il contatore MainClass_C1_contatore_Co5 non è  diverso da  *56,* 1132 *38,* o  se il contatore MainClass_C1_contatore_Co1 non è  maggiore di  *54,* 13, *70,*Incrementa il contatore MainClass_C1_contatore_Co5
    bool res_OrLogicOP_22 = false;
    bool res_AndLogicOP_23 = true;
    res_AndLogicOP_23 = (res_AndLogicOP_23 && (L_P1__GetMainc19(my_id) > 4u));
    bool res_NotLogicOP_24 = true;
    bool res_NotLogicOP_25 = true;
    res_NotLogicOP_25 = (res_NotLogicOP_25 && ! (Counter_GetValore(L_P1__GetMainc35(my_id)) == 1132u));
    res_NotLogicOP_24 = (res_NotLogicOP_24 && ! res_NotLogicOP_25);
    res_AndLogicOP_23 = (res_AndLogicOP_23 && res_NotLogicOP_24);
    
    res_OrLogicOP_22 = (res_OrLogicOP_22 || res_AndLogicOP_23);
    bool res_NotLogicOP_26 = true;
    res_NotLogicOP_26 = (res_NotLogicOP_26 && ! (Counter_GetValore(L_P1__GetMainc33(my_id)) > 13u));
    res_OrLogicOP_22 = (res_OrLogicOP_22 || res_NotLogicOP_26);
    
    if(res_OrLogicOP_22){
    
    Counter_Incr(L_P1__GetMainc35(my_id));
    }
}

/*
    CNL corrispondente:
    
    { commento: {34,}  se lo stato  non è  uguale a  commento: {53,}  state1  commento: {106,} commento: {38,} e  se il contatore MainClass_C1_contatore_Co5 è  maggiore di  commento: {54,} 120 commento: {38,} e  se il contatore MainClass_C1_contatore_Co1 non è  uguale a  commento: {53,} 14432 o  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} e  se la variabile MainClass_C1_variabile_V8 è  uguale a c270x, commento: {71,}Decrementa il contatore MainClass_C1_contatore_Co5
    
       
    
    }
*/
void L_P1__Macro1(instance_id_t const my_id )
{
//  *34,*  se lo stato  non è  uguale a  *53,*  state1  *106,* *38,* e  se il contatore MainClass_C1_contatore_Co5 è  maggiore di  *54,* 120 *38,* e  se il contatore MainClass_C1_contatore_Co1 non è  uguale a  *53,* 14432 o  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  *37,* e  se la variabile MainClass_C1_variabile_V8 è  uguale a c270x, *71,*Decrementa il contatore MainClass_C1_contatore_Co5
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_AndLogicOP_2 = true;
    bool res_AndLogicOP_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1_C1_GetState(my_id) == C1_St_state));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_4);
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (Counter_GetValore(L_P1__GetMainc35(my_id)) > 120u));
    
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_AndLogicOP_3);
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (Counter_GetValore(L_P1__GetMainc33(my_id)) == 14432u));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_5);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_2);
    res_OrLogicOP_1 = (res_OrLogicOP_1 || (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_AndLogicOP_6 = true;
    res_AndLogicOP_6 = (res_AndLogicOP_6 && (L_P1__GetInConsd(my_id) == false));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && (L_P1__GetMainc24(my_id) == c270x));
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_6);
    
    if(res_OrLogicOP_0){
    
    Counter_Decr(L_P1__GetMainc35(my_id));
    }
}


// Macro di verifica

/*
    CNL corrispondente:
     
    { commento: {61,} commento: {37,}  se la variabile MainClass_C1_variabile_V6 è  uguale a  True  commento: {38,} o  se il contatore MainClass_C1_contatore_Co1 non è  uguale a  commento: {53,} 14, Tutte le seguenti { 
     commento: {61,} commento: {34,}  se lo stato  è  diverso da  commento: {56,}  state1  commento: {106,} commento: {38,} o  se il contatore MainClass_C1_contatore_Co1 è  uguale a  commento: {53,} 1521 o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
      se la macro  MainClass_C1_macrova_M1 ( con argomento_a5   uguale a Rosso ,argomento_a10   uguale a avviox ,argomento_a4   uguale a avviox  e argomento_a3   uguale a c270x )  non  è  uguale a  True  commento: {40,}  commento: {34,} e  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x commento: {37,} o  se la variabile MainClass_C1_variabile_V6 non è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro MainClass_C1_parametro_P3 non è  uguale a c270x e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   commento: {48,51,}  commento: {,}  il controllo MainClass_C1_controllo_C5 non sia  uguale a c270x
     commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co2 non sia  minore di  commento: {55,} 135
    
    
     } Verifica che   commento: {48,49,}  commento: {,}  il controllo MainClass_C1_controllo_C7 non sia  uguale a GialloxVerdex
     commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T6 sia disattivo
     commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} e  che  commento: {36,}  il timer MainClass_C1_timer_T4 sia disattivo
     commento: {104,} o  che  commento: {36,}  il timer MainClass_C1_timer_T4 sia attivo
    
    
     } Verifica che   commento: {49,50,}  commento: {,}  la variabile MainClass_C1_variabile_V6 sia  diverso da  False 
     commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T4 non sia disattivo
    
    
    }
*/
bool L_P1__Macro3(instance_id_t const my_id )
{
bool res_AndLogicOP_0 = true;
    
    //  *61,* *37,*  se la variabile MainClass_C1_variabile_V6 è  uguale a  True  *38,* o  se il contatore MainClass_C1_contatore_Co1 non è  uguale a  *53,* 14, Tutte le seguenti { 
    //   *61,* *34,*  se lo stato  è  diverso da  *56,*  state1  *106,* *38,* o  se il contatore MainClass_C1_contatore_Co1 è  uguale a  *53,* 1521 o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
    //    se la macro  MainClass_C1_macrova_M1 ( con argomento_a5   uguale a Rosso ,argomento_a10   uguale a avviox ,argomento_a4   uguale a avviox  e argomento_a3   uguale a c270x )  non  è  uguale a  True  *40,*  *34,* e  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x *37,* o  se la variabile MainClass_C1_variabile_V6 non è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE  *34,* e  se il parametro MainClass_C1_parametro_P3 non è  uguale a c270x e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   *48,51,*  *,*  il controllo MainClass_C1_controllo_C5 non sia  uguale a c270x
    //   *104,* e  che  *,*  il contatore MainClass_C1_contatore_Co2 non sia  minore di  *55,* 135
    //   } Verifica che   *48,49,*  *,*  il controllo MainClass_C1_controllo_C7 non sia  uguale a GialloxVerdex
    //   *104,* o  che  *,*  il timer MainClass_C1_timer_T6 sia disattivo
    //   *104,* e  che   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* e  che  *36,*  il timer MainClass_C1_timer_T4 sia disattivo
    //   *104,* o  che  *36,*  il timer MainClass_C1_timer_T4 sia attivo
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    res_OrLogicOP_2 = (res_OrLogicOP_2 || (L_P1__GetMainc22(my_id) == true));
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (Counter_GetValore(L_P1__GetMainc33(my_id)) == 14u));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_3);
    
    if(res_OrLogicOP_2){
    bool res_AndLogicOP_4 = true;
    bool res_ImpliesLogicOp_5 = true;
    bool res_OrLogicOP_6 = false;
    bool res_OrLogicOP_7 = false;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1_C1_GetState(my_id) == C1_St_state));
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_NotLogicOP_8);
    res_OrLogicOP_7 = (res_OrLogicOP_7 || (Counter_GetValore(L_P1__GetMainc33(my_id)) == 1521u));
    
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_OrLogicOP_7);
    res_OrLogicOP_6 = (res_OrLogicOP_6 || (L_P1__GetInConsd(my_id) == false));
    
    if(res_OrLogicOP_6){
    bool res_ImpliesLogicOp_9 = true;
    bool res_OrLogicOP_10 = false;
    bool res_AndLogicOP_11 = true;
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (L_P1__Macro2(my_id,avviox,c270x,avviox,rosso) == true));
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_NotLogicOP_12);
    res_AndLogicOP_11 = (res_AndLogicOP_11 && (L_P1__GetParamMainc5(my_id) == c270x));
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_AndLogicOP_11);
    bool res_AndLogicOP_13 = true;
    bool res_AndLogicOP_14 = true;
    bool res_AndLogicOP_15 = true;
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (L_P1__GetMainc22(my_id) == false));
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_NotLogicOP_16);
    res_AndLogicOP_15 = (res_AndLogicOP_15 && (L_P1__GetInConsd(my_id) == false));
    
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_AndLogicOP_15);
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! (L_P1__GetParamMainc5(my_id) == c270x));
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_NotLogicOP_17);
    
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_AndLogicOP_14);
    res_AndLogicOP_13 = (res_AndLogicOP_13 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_AndLogicOP_13);
    
    if(res_OrLogicOP_10){
    bool res_AndLogicOP_18 = true;
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (L_P1__GetInMainc1(my_id) == c270x));
    res_AndLogicOP_18 = (res_AndLogicOP_18 && res_NotLogicOP_19);
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! (Counter_GetValore(L_P1__GetMainc34(my_id)) < 135u));
    res_AndLogicOP_18 = (res_AndLogicOP_18 && res_NotLogicOP_20);
    
    res_ImpliesLogicOp_9 = (res_ImpliesLogicOp_9 && res_AndLogicOP_18);
    }
    res_ImpliesLogicOp_5 = (res_ImpliesLogicOp_5 && res_ImpliesLogicOp_9);
    }
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_ImpliesLogicOp_5);
    bool res_OrLogicOP_21 = false;
    bool res_OrLogicOP_22 = false;
    bool res_NotLogicOP_23 = true;
    res_NotLogicOP_23 = (res_NotLogicOP_23 && ! (L_P1__GetInMainc2(my_id) == gialloxverd));
    res_OrLogicOP_22 = (res_OrLogicOP_22 || res_NotLogicOP_23);
    bool res_AndLogicOP_24 = true;
    bool res_AndLogicOP_25 = true;
    res_AndLogicOP_25 = (res_AndLogicOP_25 && Timer_Disattivo(L_P1__GetMainc32(my_id)));
    res_AndLogicOP_25 = (res_AndLogicOP_25 && (L_P1__GetInConsd(my_id) == false));
    
    res_AndLogicOP_24 = (res_AndLogicOP_24 && res_AndLogicOP_25);
    res_AndLogicOP_24 = (res_AndLogicOP_24 && Timer_Disattivo(L_P1__GetMainc31(my_id)));
    
    res_OrLogicOP_22 = (res_OrLogicOP_22 || res_AndLogicOP_24);
    
    res_OrLogicOP_21 = (res_OrLogicOP_21 || res_OrLogicOP_22);
    res_OrLogicOP_21 = (res_OrLogicOP_21 || Timer_Attivo(L_P1__GetMainc31(my_id)));
    
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_OrLogicOP_21);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_AndLogicOP_4);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *49,50,*  *,*  la variabile MainClass_C1_variabile_V6 sia  diverso da  False 
    //   *104,* o  che  *,*  il timer MainClass_C1_timer_T4 non sia disattivo
    bool res_OrLogicOP_26 = false;
    bool res_NotLogicOP_27 = true;
    res_NotLogicOP_27 = (res_NotLogicOP_27 && ! (L_P1__GetMainc22(my_id) == false));
    res_OrLogicOP_26 = (res_OrLogicOP_26 || res_NotLogicOP_27);
    bool res_NotLogicOP_28 = true;
    res_NotLogicOP_28 = (res_NotLogicOP_28 && ! Timer_Disattivo(L_P1__GetMainc31(my_id)));
    res_OrLogicOP_26 = (res_OrLogicOP_26 || res_NotLogicOP_28);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_26);
    
    
    
    return res_AndLogicOP_0;
}


// Macro valorizzate

/*
    CNL corrispondente:
    
    { commento: {[}  se il ripristino dello stato  è  uguale a  commento: {53,}  state1  commento: {107,} e  se l'argomento argomento_a10 è  diverso da avviox commento: {39,}  commento: {38,} o  se il contatore MainClass_C1_contatore_Co1 è  uguale a  commento: {53,} 1515 , assegna alla macro il valore  True 
    
     commento: {46,} assegna alla macro il valore  False  commento: {],}
    }
*/
bool L_P1__Macro2(instance_id_t const my_id , C1_Enumerat2 argom5, C1_Enumerat4 argom6, C1_Enumerat2 argom7, C1_Enumerat2 argom8)
{
bool res_macro_val;
    
    //  *[*  se il ripristino dello stato  è  uguale a  *53,*  state1  *107,* e  se l'argomento argomento_a10 è  diverso da avviox *39,*  *38,* o  se il contatore MainClass_C1_contatore_Co1 è  uguale a  *53,* 1515
    bool res_OrLogicOP_0 = false;
    bool res_AndLogicOP_1 = true;
    res_AndLogicOP_1 = (res_AndLogicOP_1 && (L_P1__GetStato1(my_id) == C1_St_state));
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (argom5 == avviox));
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_2);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_1);
    res_OrLogicOP_0 = (res_OrLogicOP_0 || (Counter_GetValore(L_P1__GetMainc33(my_id)) == 1515u));
    
    if(res_OrLogicOP_0){
    
    res_macro_val = true;
    }
    else{
    res_macro_val = false;
    }
    return res_macro_val;
}



