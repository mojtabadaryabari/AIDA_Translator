// Codice del modello 'TestCase5', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#include "Logica/ClasseMainClass_C1.h"
#include "Logica/ClasseMainClass_C1_priv.h"
#include "config.h"
#include "scheduler.h"


// ********** Gestione comandi automatici **********

static size_t L_P1_C1_NumAutoCmds(instance_id_t const my_id)
{
    size_t n = 0u;
    if (L_P1__GetCAEvent(my_id)) {
        ++n;
    }
    return n;
}


// ********** Gestione comandi manuali **********

static void L_P1_C1_InitCmdsResponse(instance_id_t const my_id)
{
    // for each manual command of L_P1_C1
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
    if (L_P1__GetInEvent4(my_id)) {
	    L_P1__SetOutEvent8(my_id, LDS_MANCMD_UNEXPECTED);
    } else {
        L_P1__SetOutEvent8(my_id, LDS_MANCMD_NOOP);
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
        if (L_P1__GetInEvent4(my_id)) {
            L_P1__SetOutEvent8(my_id, LDS_MANCMD_BLOCKED);
        }
	break;

    case C1_St_state5:
        // manual commands of L_P1_C1 that can be received in C1_St_state5
	break;

    case C1_St_state4:
        // manual commands of L_P1_C1 that can be received in C1_St_state4
	break;

    case C1_St_state3:
        // manual commands of L_P1_C1 that can be received in C1_St_state3
	break;

    case C1_St_state2:
        // manual commands of L_P1_C1 that can be received in C1_St_state2
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
    
     commento: {81,}  Ricezione del  comando manuale   MainClass_C1_command_comm8 da  Sender1a75134   commento: {76,}
     commento: {69,} commento: {34,}  se il parametro MainClass_C1_parametro_P9 non è  uguale a  commento: {53,} 1 commento: {37,} o  se la variabile MainClass_C1_variabile_V4 non è  uguale a  commento: {53,} 3 commento: {38,} o  se il contatore MainClass_C1_contatore_Co8 è  maggiore di  commento: {54,} 12 commento: {34,} e  se il parametro MainClass_C1_parametro_P3 non è  maggiore di  commento: {54,} 2, Solo una delle seguenti { 
     commento: {38,}  se il contatore MainClass_C1_contatore_Co8 è  uguale a  commento: {53,} 15315 e  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} o  se il parametro MainClass_C1_parametro_P3 è  minore di  commento: {55,} 10 commento: {35,} e  se il controllo MainClass_C1_controllo_C3 non è  uguale a RossoGiallo commento: {37,} e  se la variabile MainClass_C1_variabile_V9 non è  maggiore di  commento: {54,} 6, Verifica che   commento: {49,}  commento: {,}  il timer MainClass_C1_timer_T9 non sia attivo
    
    
     } Verifica che   commento: {50,}  commento: {,}  la variabile MainClass_C1_variabile_V9 sia  uguale a  commento: {53,} 2
    
    
    
    }
*/
static inline bool L_P1__Guard1(instance_id_t const my_id)
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
     {  Nessuna  }
*/
static inline bool L_P1__Guard3(instance_id_t const my_id)
{
    return true;
}


/*
    CNL corrispondente:
    
    {
    
     commento: {67,}  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} o  se il contatore MainClass_C1_contatore_Co8 non è  minore di  commento: {55,} 123 commento: {38,} e  se il contatore MainClass_C1_contatore_Co8 non è  uguale a  commento: {53,} 12, Tutte le seguenti { 
     commento: {69,} commento: {34,}  se il parametro MainClass_C1_parametro_P3 è  diverso da  commento: {56,} 6 commento: {37,} e  se la variabile MainClass_C1_variabile_V9 non è  maggiore di  commento: {54,} 4 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
     commento: {36,}  se il timer MainClass_C1_timer_T10 è attivo o  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro MainClass_C1_parametro_P3 è  minore di  commento: {55,} 1 commento: {37,} o  se la variabile MainClass_C1_variabile_V2 non è  minore di  commento: {55,} 8 commento: {37,} e  se la variabile MainClass_C1_variabile_V4 è  uguale a  commento: {53,} 4 commento: {38,} e  se il contatore MainClass_C1_contatore_Co8 non è  maggiore di  commento: {54,} 13, Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
    
    
     } Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
    
    
     } Verifica che   commento: {50,}  commento: {,}  la variabile MainClass_C1_variabile_V9 sia  maggiore di  commento: {54,} 10
    
    
    }
*/
static inline bool L_P1__Guard4(instance_id_t const my_id)
{
    bool res_AndLogicOP_0 = true;
    
    //  *67,*  se il controllo ConsDef  è  uguale a FALSE  *38,* o  se il contatore MainClass_C1_contatore_Co8 non è  minore di  *55,* 123 *38,* e  se il contatore MainClass_C1_contatore_Co8 non è  uguale a  *53,* 12, Tutte le seguenti { 
    //   *69,* *34,*  se il parametro MainClass_C1_parametro_P3 è  diverso da  *56,* 6 *37,* e  se la variabile MainClass_C1_variabile_V9 non è  maggiore di  *54,* 4 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
    //   *36,*  se il timer MainClass_C1_timer_T10 è attivo o  se il controllo ConsDef  è  uguale a FALSE  *34,* e  se il parametro MainClass_C1_parametro_P3 è  minore di  *55,* 1 *37,* o  se la variabile MainClass_C1_variabile_V2 non è  minore di  *55,* 8 *37,* e  se la variabile MainClass_C1_variabile_V4 è  uguale a  *53,* 4 *38,* e  se il contatore MainClass_C1_contatore_Co8 non è  maggiore di  *54,* 13, Verifica che   *48,*   il controllo ConsDef  sia  uguale a FALSE 
    //   } Verifica che   *48,*   il controllo ConsDef  sia  uguale a FALSE 
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    res_OrLogicOP_2 = (res_OrLogicOP_2 || (L_P1__GetInConsd(my_id) == false));
    bool res_AndLogicOP_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (Counter_GetValore(L_P1__GetMainc44(my_id)) < 123u));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_4);
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (Counter_GetValore(L_P1__GetMainc44(my_id)) == 12u));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_5);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_3);
    
    if(res_OrLogicOP_2){
    bool res_AndLogicOP_6 = true;
    bool res_ImpliesLogicOp_7 = true;
    bool res_AndLogicOP_8 = true;
    bool res_AndLogicOP_9 = true;
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__GetParamMainc7(my_id) == 6u));
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_NotLogicOP_10);
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (L_P1__GetMainc34(my_id) > 4u));
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_NotLogicOP_11);
    
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_AndLogicOP_9);
    res_AndLogicOP_8 = (res_AndLogicOP_8 && (L_P1__GetInConsd(my_id) == false));
    
    if(res_AndLogicOP_8){
    bool res_ImpliesLogicOp_12 = true;
    bool res_OrLogicOP_13 = false;
    bool res_OrLogicOP_14 = false;
    res_OrLogicOP_14 = (res_OrLogicOP_14 || Timer_Attivo(L_P1__GetMainc41(my_id)));
    bool res_AndLogicOP_15 = true;
    res_AndLogicOP_15 = (res_AndLogicOP_15 && (L_P1__GetInConsd(my_id) == false));
    res_AndLogicOP_15 = (res_AndLogicOP_15 && (L_P1__GetParamMainc7(my_id) < 1u));
    
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_AndLogicOP_15);
    
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_OrLogicOP_14);
    bool res_AndLogicOP_16 = true;
    bool res_AndLogicOP_17 = true;
    bool res_NotLogicOP_18 = true;
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! (L_P1__GetMainc32(my_id) < 8u));
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_NotLogicOP_18);
    res_AndLogicOP_17 = (res_AndLogicOP_17 && (L_P1__GetMainc33(my_id) == 4u));
    
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_AndLogicOP_17);
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (Counter_GetValore(L_P1__GetMainc44(my_id)) > 13u));
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_NotLogicOP_19);
    
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_AndLogicOP_16);
    
    if(res_OrLogicOP_13){
    res_ImpliesLogicOp_12 = (res_ImpliesLogicOp_12 && (L_P1__GetInConsd(my_id) == false));
    }
    res_ImpliesLogicOp_7 = (res_ImpliesLogicOp_7 && res_ImpliesLogicOp_12);
    }
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_ImpliesLogicOp_7);
    res_AndLogicOP_6 = (res_AndLogicOP_6 && (L_P1__GetInConsd(my_id) == false));
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_AndLogicOP_6);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *50,*  *,*  la variabile MainClass_C1_variabile_V9 sia  maggiore di  *54,* 10
    res_AndLogicOP_0 = (res_AndLogicOP_0 && (L_P1__GetMainc34(my_id) > 10u));
    
    
    
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


/*
    CNL corrispondente:
     {  commento: {87,}  Almeno una delle seguenti {
     commento: {85,}  Tutte le seguenti {
     Ricezione del comando   MainClass_C1_command_comm1    commento: {79,}
     commento: {68,} commento: {34,}  se il parametro MainClass_C1_parametro_P6 non è  diverso da c270 commento: {36,} e  se il timer MainClass_C1_timer_T4 è scaduto commento: {37,} e  se la variabile MainClass_C1_variabile_V2 non è  maggiore di  commento: {54,} 2 commento: {35,} e  se il controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo commento: {36,} o  se il timer MainClass_C1_timer_T10 non è scaduto commento: {36,} o  se il timer MainClass_C1_timer_T4 è attivo, Almeno una delle seguenti { 
     commento: {68,} commento: {34,}  se il parametro MainClass_C1_parametro_P6 è  diverso da c270 commento: {36,} e  se il timer MainClass_C1_timer_T4 è attivo commento: {34,} e  se il parametro MainClass_C1_parametro_P3 è  diverso da  commento: {56,} 2 commento: {36,} e  se il timer MainClass_C1_timer_T9 non è attivo commento: {36,} o  se il timer MainClass_C1_timer_T10 non è disattivo, Almeno una delle seguenti { 
     commento: {68,} commento: {35,}  se il controllo MainClass_C1_controllo_C5 è  uguale a RossoGialloGiallo, Almeno una delle seguenti { 
     commento: {34,}  se il parametro MainClass_C1_parametro_P6 non è  uguale a c270 commento: {37,} e  se la variabile MainClass_C1_variabile_V9 è  uguale a  commento: {53,} 3 commento: {38,} e  se il contatore MainClass_C1_contatore_Co8 non è  diverso da  commento: {56,} 15150 commento: {35,} o  se il controllo MainClass_C1_controllo_C3 non è  diverso da RossoGiallo e  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   commento: {50,}  commento: {,}  la variabile MainClass_C1_variabile_V9 non sia  maggiore di  commento: {54,} 3
    
    
     } Verifica che   commento: {51,}  commento: {,}  il contatore MainClass_C1_contatore_Co8 non sia  uguale a  commento: {53,} 11
    
    
     } Verifica che   commento: {47,}  commento: {34,}  il parametro MainClass_C1_parametro_P3 non sia  uguale a  commento: {53,} 7
    
    
     } Verifica che   commento: {51,}  commento: {,}  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  commento: {54,} 1
    
    
    }
    } }
*/
static inline bool L_P1__Guard6(instance_id_t const my_id)
{
    bool res_AndLogicOP_0 = true;
    
    //  *85,*  Tutte le seguenti {
    //   Ricezione del comando   MainClass_C1_command_comm1    *79,*
    //   *68,* *34,*  se il parametro MainClass_C1_parametro_P6 non è  diverso da c270 *36,* e  se il timer MainClass_C1_timer_T4 è scaduto *37,* e  se la variabile MainClass_C1_variabile_V2 non è  maggiore di  *54,* 2 *35,* e  se il controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo *36,* o  se il timer MainClass_C1_timer_T10 non è scaduto *36,* o  se il timer MainClass_C1_timer_T4 è attivo, Almeno una delle seguenti { 
    //   *68,* *34,*  se il parametro MainClass_C1_parametro_P6 è  diverso da c270 *36,* e  se il timer MainClass_C1_timer_T4 è attivo *34,* e  se il parametro MainClass_C1_parametro_P3 è  diverso da  *56,* 2 *36,* e  se il timer MainClass_C1_timer_T9 non è attivo *36,* o  se il timer MainClass_C1_timer_T10 non è disattivo, Almeno una delle seguenti { 
    //   *68,* *35,*  se il controllo MainClass_C1_controllo_C5 è  uguale a RossoGialloGiallo, Almeno una delle seguenti { 
    //   *34,*  se il parametro MainClass_C1_parametro_P6 non è  uguale a c270 *37,* e  se la variabile MainClass_C1_variabile_V9 è  uguale a  *53,* 3 *38,* e  se il contatore MainClass_C1_contatore_Co8 non è  diverso da  *56,* 15150 *35,* o  se il controllo MainClass_C1_controllo_C3 non è  diverso da RossoGiallo e  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   *50,*  *,*  la variabile MainClass_C1_variabile_V9 non sia  maggiore di  *54,* 3
    //   } Verifica che   *51,*  *,*  il contatore MainClass_C1_contatore_Co8 non sia  uguale a  *53,* 11
    //   } Verifica che   *47,*  *34,*  il parametro MainClass_C1_parametro_P3 non sia  uguale a  *53,* 7
    //   } Verifica che   *51,*  *,*  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  *54,* 1
    //  }
    bool res_AndLogicOP_1 = true;
    res_AndLogicOP_1 = (res_AndLogicOP_1 && L_P1__GetCAEvent(my_id));
    bool res_ImpliesLogicOp_2 = true;
    bool res_OrLogicOP_3 = false;
    bool res_OrLogicOP_4 = false;
    bool res_AndLogicOP_5 = true;
    bool res_AndLogicOP_6 = true;
    bool res_AndLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetParamMainc8(my_id) == c270));
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! res_NotLogicOP_9);
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_8);
    res_AndLogicOP_7 = (res_AndLogicOP_7 && Timer_Scaduto(L_P1__GetMainc42(my_id)));
    
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_AndLogicOP_7);
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__GetMainc32(my_id) > 2u));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_10);
    
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_AndLogicOP_6);
    res_AndLogicOP_5 = (res_AndLogicOP_5 && (L_P1__GetInMainc4(my_id) == rossogiallo));
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_AndLogicOP_5);
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! Timer_Scaduto(L_P1__GetMainc41(my_id)));
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_NotLogicOP_11);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_OrLogicOP_4);
    res_OrLogicOP_3 = (res_OrLogicOP_3 || Timer_Attivo(L_P1__GetMainc42(my_id)));
    
    if(res_OrLogicOP_3){
    bool res_OrLogicOP_12 = false;
    bool res_ImpliesLogicOp_13 = true;
    bool res_OrLogicOP_14 = false;
    bool res_AndLogicOP_15 = true;
    bool res_AndLogicOP_16 = true;
    bool res_AndLogicOP_17 = true;
    bool res_NotLogicOP_18 = true;
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! (L_P1__GetParamMainc8(my_id) == c270));
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_NotLogicOP_18);
    res_AndLogicOP_17 = (res_AndLogicOP_17 && Timer_Attivo(L_P1__GetMainc42(my_id)));
    
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_AndLogicOP_17);
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (L_P1__GetParamMainc7(my_id) == 2u));
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_NotLogicOP_19);
    
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_AndLogicOP_16);
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! Timer_Attivo(L_P1__GetMainc43(my_id)));
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_NotLogicOP_20);
    
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_AndLogicOP_15);
    bool res_NotLogicOP_21 = true;
    res_NotLogicOP_21 = (res_NotLogicOP_21 && ! Timer_Disattivo(L_P1__GetMainc41(my_id)));
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_NotLogicOP_21);
    
    if(res_OrLogicOP_14){
    bool res_OrLogicOP_22 = false;
    bool res_ImpliesLogicOp_23 = true;
    if((L_P1__GetInMainc5(my_id) == rossogiallo1)){
    bool res_ImpliesLogicOp_24 = true;
    bool res_OrLogicOP_25 = false;
    bool res_OrLogicOP_26 = false;
    bool res_AndLogicOP_27 = true;
    bool res_AndLogicOP_28 = true;
    bool res_NotLogicOP_29 = true;
    res_NotLogicOP_29 = (res_NotLogicOP_29 && ! (L_P1__GetParamMainc8(my_id) == c270));
    res_AndLogicOP_28 = (res_AndLogicOP_28 && res_NotLogicOP_29);
    res_AndLogicOP_28 = (res_AndLogicOP_28 && (L_P1__GetMainc34(my_id) == 3u));
    
    res_AndLogicOP_27 = (res_AndLogicOP_27 && res_AndLogicOP_28);
    bool res_NotLogicOP_30 = true;
    bool res_NotLogicOP_31 = true;
    res_NotLogicOP_31 = (res_NotLogicOP_31 && ! (Counter_GetValore(L_P1__GetMainc44(my_id)) == 15150u));
    res_NotLogicOP_30 = (res_NotLogicOP_30 && ! res_NotLogicOP_31);
    res_AndLogicOP_27 = (res_AndLogicOP_27 && res_NotLogicOP_30);
    
    res_OrLogicOP_26 = (res_OrLogicOP_26 || res_AndLogicOP_27);
    bool res_AndLogicOP_32 = true;
    bool res_NotLogicOP_33 = true;
    bool res_NotLogicOP_34 = true;
    res_NotLogicOP_34 = (res_NotLogicOP_34 && ! (L_P1__GetInMainc4(my_id) == rossogiallo));
    res_NotLogicOP_33 = (res_NotLogicOP_33 && ! res_NotLogicOP_34);
    res_AndLogicOP_32 = (res_AndLogicOP_32 && res_NotLogicOP_33);
    res_AndLogicOP_32 = (res_AndLogicOP_32 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_26 = (res_OrLogicOP_26 || res_AndLogicOP_32);
    
    res_OrLogicOP_25 = (res_OrLogicOP_25 || res_OrLogicOP_26);
    res_OrLogicOP_25 = (res_OrLogicOP_25 || (L_P1__GetInConsd(my_id) == false));
    
    if(res_OrLogicOP_25){
    bool res_NotLogicOP_35 = true;
    res_NotLogicOP_35 = (res_NotLogicOP_35 && ! (L_P1__GetMainc34(my_id) > 3u));
    res_ImpliesLogicOp_24 = (res_ImpliesLogicOp_24 && res_NotLogicOP_35);
    }
    res_ImpliesLogicOp_23 = (res_ImpliesLogicOp_23 && res_ImpliesLogicOp_24);
    }
    res_OrLogicOP_22 = (res_OrLogicOP_22 || res_ImpliesLogicOp_23);
    bool res_NotLogicOP_36 = true;
    res_NotLogicOP_36 = (res_NotLogicOP_36 && ! (Counter_GetValore(L_P1__GetMainc44(my_id)) == 11u));
    res_OrLogicOP_22 = (res_OrLogicOP_22 || res_NotLogicOP_36);
    
    res_ImpliesLogicOp_13 = (res_ImpliesLogicOp_13 && res_OrLogicOP_22);
    }
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_ImpliesLogicOp_13);
    bool res_NotLogicOP_37 = true;
    res_NotLogicOP_37 = (res_NotLogicOP_37 && ! (L_P1__GetParamMainc7(my_id) == 7u));
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_NotLogicOP_37);
    
    res_ImpliesLogicOp_2 = (res_ImpliesLogicOp_2 && res_OrLogicOP_12);
    }
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_ImpliesLogicOp_2);
    res_AndLogicOP_1 = (res_AndLogicOP_1 && (Counter_GetValore(L_P1__GetMainc44(my_id)) > 1u));
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_AndLogicOP_1);
    
    if(res_AndLogicOP_1){
    L_P1__SetCAEvent(my_id,false);
    }
    else{
    
    }
    
    
    return res_AndLogicOP_0;
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
     {   se il controllo ConsDef  è  uguale a FALSE  commento: {35,} o  se il controllo MainClass_C1_controllo_C3 non è  uguale a RossoGiallo o  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} e  se il timer MainClass_C1_timer_T10 è attivo commento: {36,} o  se il timer MainClass_C1_timer_T4 non è attivo, Verifica che   commento: {48,}  commento: {,}  il controllo MainClass_C1_controllo_C1 sia  uguale a  False 
    
     }
*/
static inline bool L_P1__Guard9(instance_id_t const my_id)
{
    bool res_AndLogicOP_0 = true;
    
    //  se il controllo ConsDef  è  uguale a FALSE  *35,* o  se il controllo MainClass_C1_controllo_C3 non è  uguale a RossoGiallo o  se il controllo ConsDef  è  uguale a FALSE  *36,* e  se il timer MainClass_C1_timer_T10 è attivo *36,* o  se il timer MainClass_C1_timer_T4 non è attivo, Verifica che   *48,*  *,*  il controllo MainClass_C1_controllo_C1 sia  uguale a  False
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_OrLogicOP_4 = false;
    res_OrLogicOP_4 = (res_OrLogicOP_4 || (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetInMainc4(my_id) == rossogiallo));
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_NotLogicOP_5);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_OrLogicOP_4);
    bool res_AndLogicOP_6 = true;
    res_AndLogicOP_6 = (res_AndLogicOP_6 && (L_P1__GetInConsd(my_id) == false));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && Timer_Attivo(L_P1__GetMainc41(my_id)));
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_AndLogicOP_6);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! Timer_Attivo(L_P1__GetMainc42(my_id)));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_7);
    
    if(res_OrLogicOP_2){
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && (L_P1__GetInMainc3(my_id) == false));
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    
    
    return res_AndLogicOP_0;
}


/*
    CNL corrispondente:
     {  Nessuna  }
*/
static inline bool L_P1__Guard10(instance_id_t const my_id)
{
    return true;
}


/*
    CNL corrispondente:
    
    {
    
     Nessuna  commento: {80,}
    }
*/
static inline bool L_P1__Guard11(instance_id_t const my_id)
{
    return true;
}


/*
    CNL corrispondente:
    
    {
    
     Nessuna  commento: {80,}
    }
*/
static inline bool L_P1__Guard12(instance_id_t const my_id)
{
    return true;
}


/*
    CNL corrispondente:
     {  commento: {34,}  se il parametro MainClass_C1_parametro_P6 è  diverso da c270 commento: {35,} o  se il controllo MainClass_C1_controllo_C3 non è  uguale a RossoGiallo commento: {36,} o  se il timer MainClass_C1_timer_T10 non è attivo, Verifica che   commento: {47,}  commento: {34,}  il parametro MainClass_C1_parametro_P6 non sia  diverso da c270
    
     }
*/
static inline bool L_P1__Guard13(instance_id_t const my_id)
{
    bool res_AndLogicOP_0 = true;
    
    //  *34,*  se il parametro MainClass_C1_parametro_P6 è  diverso da c270 *35,* o  se il controllo MainClass_C1_controllo_C3 non è  uguale a RossoGiallo *36,* o  se il timer MainClass_C1_timer_T10 non è attivo, Verifica che   *47,*  *34,*  il parametro MainClass_C1_parametro_P6 non sia  diverso da c270
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetParamMainc8(my_id) == c270));
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_NotLogicOP_4);
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetInMainc4(my_id) == rossogiallo));
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_NotLogicOP_5);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! Timer_Attivo(L_P1__GetMainc41(my_id)));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_6);
    
    if(res_OrLogicOP_2){
    bool res_NotLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetParamMainc8(my_id) == c270));
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! res_NotLogicOP_8);
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_NotLogicOP_7);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    
    
    return res_AndLogicOP_0;
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
    
     commento: {34,}  se lo stato  non è  diverso da  commento: {56,}  state1  commento: {106,} commento: {34,} o  se il parametro MainClass_C1_parametro_P3 è  uguale a  commento: {53,} 4 e  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} e  se il contatore MainClass_C1_contatore_Co8 non è  maggiore di  commento: {54,} 12, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V4 il valore 3
    
     ,altrimenti   Applica gli effetti
           della macro MainClass_C1_macroef_M4( con argomento_af9   uguale a True ,argomento_af5   uguale a GialloVerde ) commento: {73,}
    
    
    
    }
*/
static inline void L_P1__Effec1(instance_id_t const my_id)
{
    
    //  *34,*  se lo stato  non è  diverso da  *56,*  state1  *106,* *34,* o  se il parametro MainClass_C1_parametro_P3 è  uguale a  *53,* 4 e  se il controllo ConsDef  è  uguale a FALSE  *38,* e  se il contatore MainClass_C1_contatore_Co8 non è  maggiore di  *54,* 12, *67,* Assegna alla variabile MainClass_C1_variabile_V4 il valore 3
    //   ,altrimenti   Applica gli effetti
    //         della macro MainClass_C1_macroef_M4( con argomento_af9   uguale a True ,argomento_af5   uguale a GialloVerde )
    bool res_OrLogicOP_0 = false;
    bool res_NotLogicOP_1 = true;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (L_P1_C1_GetState(my_id) == C1_St_state));
    res_NotLogicOP_1 = (res_NotLogicOP_1 && ! res_NotLogicOP_2);
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_1);
    bool res_AndLogicOP_3 = true;
    bool res_AndLogicOP_4 = true;
    res_AndLogicOP_4 = (res_AndLogicOP_4 && (L_P1__GetParamMainc7(my_id) == 4u));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && (L_P1__GetInConsd(my_id) == false));
    
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_AndLogicOP_4);
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (Counter_GetValore(L_P1__GetMainc44(my_id)) > 12u));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_5);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_3);
    
    if(res_OrLogicOP_0){
    
    L_P1__SetMainc33(my_id,3u);
    }else{
    
    L_P1__Macro(my_id,gialloverde,true);
    }
}


/*
    CNL corrispondente:
    
    {
    
     commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI3 non è scaduto commento: {37,} e  se la variabile MainClass_C1_variabile_V9 è  diverso da  commento: {56,} 5,  Applica gli effetti
           della macro MainClass_C1_macroef_M4( con argomento_af9   uguale a True ,argomento_af5   uguale a GialloVerde ) commento: {73,}
    
     ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V9 il valore 9
    
    
     commento: {36,}  se il timer MainClass_C1_timer_T4 è disattivo e  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE , commento: {67,} Assegna alla variabile MainClass_C1_variabile_V2 il valore 3
    
     ,altrimenti   Applica gli effetti
           della macro MainClass_C1_macroef_M8  commento: {73,}
    
    
     commento: {35,}  se il controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo commento: {36,} o  se il timer MainClass_C1_timer_T4 è attivo,  Applica gli effetti
           della macro MainClass_C1_macroef_M4( con argomento_af9   uguale a True ,argomento_af5   uguale a avvio ) commento: {73,}
    
     ,altrimenti   Applica gli effetti
           della macro MainClass_C1_macroef_M8  commento: {73,}
    
    
      se la macro  MainClass_C1_macrova_M3 ( con argomento_a4   uguale a True ,argomento_a7   uguale a GialloVerde ,argomento_a10   uguale a RossoGialloGiallo ,argomento_a2   uguale a RossoGialloGiallo ,argomento_a6   uguale a RossoGiallo  e argomento_a1   uguale a c270x )  non  è  uguale a RossoGialloGiallo commento: {40,}  e  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} o  se la variabile MainClass_C1_variabile_V9 è  maggiore di  commento: {54,} 10 o  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} e  se il controllo MainClass_C1_controllo_C3 è  diverso da RossoGiallo commento: {37,} o  se la variabile MainClass_C1_variabile_V9 non è  diverso da  commento: {56,} 5,  Applica gli effetti
           della macro MainClass_C1_macroef_M4( con argomento_af9   uguale a True ,argomento_af5   uguale a avvio ) commento: {73,}
    
       
    
    }
*/
static inline void L_P1__Effec2(instance_id_t const my_id)
{
    
    //  *110,*  se il ripristino del timer  MainClass_C1_restoreTI_TI3 non è scaduto *37,* e  se la variabile MainClass_C1_variabile_V9 è  diverso da  *56,* 5,  Applica gli effetti
    //         della macro MainClass_C1_macroef_M4( con argomento_af9   uguale a True ,argomento_af5   uguale a GialloVerde ) *73,*
    //   ,altrimenti  *67,* Assegna alla variabile MainClass_C1_variabile_V9 il valore 9
    bool res_AndLogicOP_0 = true;
    bool res_NotLogicOP_1 = true;
    res_NotLogicOP_1 = (res_NotLogicOP_1 && ! Timer_Scaduto(L_P1__GetMainc40(my_id)));
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_NotLogicOP_1);
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (L_P1__GetMainc34(my_id) == 5u));
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_NotLogicOP_2);
    
    if(res_AndLogicOP_0){
    
    L_P1__Macro(my_id,gialloverde,true);
    }else{
    
    L_P1__SetMainc34(my_id,9u);
    }
    
    //  *36,*  se il timer MainClass_C1_timer_T4 è disattivo e  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE , *67,* Assegna alla variabile MainClass_C1_variabile_V2 il valore 3
    //   ,altrimenti   Applica gli effetti
    //         della macro MainClass_C1_macroef_M8
    bool res_OrLogicOP_3 = false;
    bool res_AndLogicOP_4 = true;
    res_AndLogicOP_4 = (res_AndLogicOP_4 && Timer_Disattivo(L_P1__GetMainc42(my_id)));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_AndLogicOP_4);
    res_OrLogicOP_3 = (res_OrLogicOP_3 || (L_P1__GetInConsd(my_id) == false));
    
    if(res_OrLogicOP_3){
    
    L_P1__SetMainc32(my_id,3u);
    }else{
    
    L_P1__Macro1(my_id);
    }
    
    //  *73,*
    //   *35,*  se il controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo *36,* o  se il timer MainClass_C1_timer_T4 è attivo,  Applica gli effetti
    //         della macro MainClass_C1_macroef_M4( con argomento_af9   uguale a True ,argomento_af5   uguale a avvio ) *73,*
    //   ,altrimenti   Applica gli effetti
    //         della macro MainClass_C1_macroef_M8
    bool res_OrLogicOP_5 = false;
    res_OrLogicOP_5 = (res_OrLogicOP_5 || (L_P1__GetInMainc4(my_id) == rossogiallo));
    res_OrLogicOP_5 = (res_OrLogicOP_5 || Timer_Attivo(L_P1__GetMainc42(my_id)));
    
    if(res_OrLogicOP_5){
    
    L_P1__Macro(my_id,avvio,true);
    }else{
    
    L_P1__Macro1(my_id);
    }
    
    //  *73,*
    //    se la macro  MainClass_C1_macrova_M3 ( con argomento_a4   uguale a True ,argomento_a7   uguale a GialloVerde ,argomento_a10   uguale a RossoGialloGiallo ,argomento_a2   uguale a RossoGialloGiallo ,argomento_a6   uguale a RossoGiallo  e argomento_a1   uguale a c270x )  non  è  uguale a RossoGialloGiallo *40,*  e  se il controllo ConsDef  è  uguale a FALSE  *37,* o  se la variabile MainClass_C1_variabile_V9 è  maggiore di  *54,* 10 o  se il controllo ConsDef  è  uguale a FALSE  *35,* e  se il controllo MainClass_C1_controllo_C3 è  diverso da RossoGiallo *37,* o  se la variabile MainClass_C1_variabile_V9 non è  diverso da  *56,* 5,  Applica gli effetti
    //         della macro MainClass_C1_macroef_M4( con argomento_af9   uguale a True ,argomento_af5   uguale a avvio )
    bool res_OrLogicOP_6 = false;
    bool res_OrLogicOP_7 = false;
    bool res_OrLogicOP_8 = false;
    bool res_AndLogicOP_9 = true;
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__Macro2(my_id,c270x,rossogiallo1,rossogiallo1,true,rossogiallo,gialloverde) == rossogiallo1));
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_NotLogicOP_10);
    res_AndLogicOP_9 = (res_AndLogicOP_9 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_AndLogicOP_9);
    res_OrLogicOP_8 = (res_OrLogicOP_8 || (L_P1__GetMainc34(my_id) > 10u));
    
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_OrLogicOP_8);
    bool res_AndLogicOP_11 = true;
    res_AndLogicOP_11 = (res_AndLogicOP_11 && (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (L_P1__GetInMainc4(my_id) == rossogiallo));
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_NotLogicOP_12);
    
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_AndLogicOP_11);
    
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_OrLogicOP_7);
    bool res_NotLogicOP_13 = true;
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1__GetMainc34(my_id) == 5u));
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! res_NotLogicOP_14);
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_NotLogicOP_13);
    
    if(res_OrLogicOP_6){
    
    L_P1__Macro(my_id,avvio,true);
    }
}


/*
    CNL corrispondente:
     { commento: {34,}  se lo stato  non è  uguale a  commento: {53,}  state1  commento: {106,} commento: {36,} o  se il timer MainClass_C1_timer_T4 non è disattivo commento: {36,} e  se il timer MainClass_C1_timer_T4 è disattivo commento: {37,} o  se la variabile MainClass_C1_variabile_V4 è  minore di  commento: {55,} 1 e  se il controllo ConsDef  è  uguale a FALSE ,  Applica gli effetti
           della macro MainClass_C1_macroef_M4( con argomento_af9   uguale a True ,argomento_af5   uguale a avvio ) commento: {73,}
    
     ,altrimenti  commento: {66,} Assegna al comando MainClass_C1_comando_C4 il valore  True 
    
    
     }
*/
static inline void L_P1__Effec3(instance_id_t const my_id)
{
    
    //  *34,*  se lo stato  non è  uguale a  *53,*  state1  *106,* *36,* o  se il timer MainClass_C1_timer_T4 non è disattivo *36,* e  se il timer MainClass_C1_timer_T4 è disattivo *37,* o  se la variabile MainClass_C1_variabile_V4 è  minore di  *55,* 1 e  se il controllo ConsDef  è  uguale a FALSE ,  Applica gli effetti
    //         della macro MainClass_C1_macroef_M4( con argomento_af9   uguale a True ,argomento_af5   uguale a avvio ) *73,*
    //   ,altrimenti  *66,* Assegna al comando MainClass_C1_comando_C4 il valore  True
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (L_P1_C1_GetState(my_id) == C1_St_state));
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_NotLogicOP_2);
    bool res_AndLogicOP_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! Timer_Disattivo(L_P1__GetMainc42(my_id)));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_4);
    res_AndLogicOP_3 = (res_AndLogicOP_3 && Timer_Disattivo(L_P1__GetMainc42(my_id)));
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_3);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_AndLogicOP_5 = true;
    res_AndLogicOP_5 = (res_AndLogicOP_5 && (L_P1__GetMainc33(my_id) < 1u));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_5);
    
    if(res_OrLogicOP_0){
    
    L_P1__Macro(my_id,avvio,true);
    }else{
    
    L_P1__SetOutMainc1(my_id,true);
    }
}


/*
    CNL corrispondente:
    
    {
    
     commento: {34,}  se lo stato  è  diverso da  commento: {56,}  state1  commento: {106,} commento: {35,} e  se il controllo MainClass_C1_controllo_C3 non è  diverso da RossoGiallo commento: {34,} e  se il parametro MainClass_C1_parametro_P9 non è  diverso da  commento: {56,} 9 commento: {35,} e  se il controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo commento: {34,} e  se il parametro MainClass_C1_parametro_P6 è  diverso da c270, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V9 il valore 1
    
     ,altrimenti  commento: {66,} Assegna al comando MainClass_C1_comando_C4 il valore  False 
    
    
    
    }
*/
static inline void L_P1__Effec4(instance_id_t const my_id)
{
    
    //  *34,*  se lo stato  è  diverso da  *56,*  state1  *106,* *35,* e  se il controllo MainClass_C1_controllo_C3 non è  diverso da RossoGiallo *34,* e  se il parametro MainClass_C1_parametro_P9 non è  diverso da  *56,* 9 *35,* e  se il controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo *34,* e  se il parametro MainClass_C1_parametro_P6 è  diverso da c270, *67,* Assegna alla variabile MainClass_C1_variabile_V9 il valore 1
    //   ,altrimenti  *66,* Assegna al comando MainClass_C1_comando_C4 il valore  False
    bool res_AndLogicOP_0 = true;
    bool res_AndLogicOP_1 = true;
    bool res_AndLogicOP_2 = true;
    bool res_AndLogicOP_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1_C1_GetState(my_id) == C1_St_state));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_4);
    bool res_NotLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetInMainc4(my_id) == rossogiallo));
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! res_NotLogicOP_6);
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_5);
    
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_AndLogicOP_3);
    bool res_NotLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetParamMainc9(my_id) == 9u));
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! res_NotLogicOP_8);
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_7);
    
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_AndLogicOP_2);
    res_AndLogicOP_1 = (res_AndLogicOP_1 && (L_P1__GetInMainc4(my_id) == rossogiallo));
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_AndLogicOP_1);
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetParamMainc8(my_id) == c270));
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_NotLogicOP_9);
    
    if(res_AndLogicOP_0){
    
    L_P1__SetMainc34(my_id,1u);
    }else{
    
    L_P1__SetOutMainc1(my_id,false);
    }
}


/*
    CNL corrispondente:
    
    {
    
      se il controllo ConsDef è uguale a FALSE  commento: {35,} o  se il controllo MainClass_C1_controllo_C5 è  diverso da RossoGialloGiallo commento: {36,} o  se il timer MainClass_C1_timer_T4 è disattivo o  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} e  se il timer MainClass_C1_timer_T9 è disattivo commento: {36,} o  se il timer MainClass_C1_timer_T4 non è disattivo, commento: {72,}Azzera il contatore MainClass_C1_contatore_Co8
    
       
      se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE ,  Applica gli effetti
           della macro MainClass_C1_macroef_M8  commento: {73,}
    
     ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V2 il valore 1
    
    
     commento: {35,}  se il controllo MainClass_C1_controllo_C8 non è  diverso da  True  commento: {38,} e  se il contatore MainClass_C1_contatore_Co8 non è  uguale a  commento: {53,} 15423 commento: {35,} o  se il controllo MainClass_C1_controllo_C5 è  diverso da RossoGialloGiallo commento: {38,} e  se il contatore MainClass_C1_contatore_Co8 non è  diverso da  commento: {56,} 13 commento: {35,} o  se il controllo MainClass_C1_controllo_C3 è  diverso da RossoGiallo commento: {35,} e  se il controllo MainClass_C1_controllo_C3 non è  uguale a RossoGiallo,  Applica gli effetti
           della macro MainClass_C1_macroef_M8  commento: {73,}
    
       
    
    }
*/
static inline void L_P1__Effec5(instance_id_t const my_id)
{
    
    //  se il controllo ConsDef è uguale a FALSE  *35,* o  se il controllo MainClass_C1_controllo_C5 è  diverso da RossoGialloGiallo *36,* o  se il timer MainClass_C1_timer_T4 è disattivo o  se il controllo ConsDef  è  uguale a FALSE  *36,* e  se il timer MainClass_C1_timer_T9 è disattivo *36,* o  se il timer MainClass_C1_timer_T4 non è disattivo, *72,*Azzera il contatore MainClass_C1_contatore_Co8
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    res_OrLogicOP_3 = (res_OrLogicOP_3 || (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetInMainc5(my_id) == rossogiallo1));
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_NotLogicOP_4);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    res_OrLogicOP_2 = (res_OrLogicOP_2 || Timer_Disattivo(L_P1__GetMainc42(my_id)));
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_OrLogicOP_2);
    bool res_AndLogicOP_5 = true;
    res_AndLogicOP_5 = (res_AndLogicOP_5 && (L_P1__GetInConsd(my_id) == false));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && Timer_Disattivo(L_P1__GetMainc43(my_id)));
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_5);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! Timer_Disattivo(L_P1__GetMainc42(my_id)));
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_6);
    
    if(res_OrLogicOP_0){
    
    Counter_Res(L_P1__GetMainc44(my_id));
    }
    
    //  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE ,  Applica gli effetti
    //         della macro MainClass_C1_macroef_M8  *73,*
    //   ,altrimenti  *67,* Assegna alla variabile MainClass_C1_variabile_V2 il valore 1
    bool res_AndLogicOP_7 = true;
    res_AndLogicOP_7 = (res_AndLogicOP_7 && (L_P1__GetInConsd(my_id) == false));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && (L_P1__GetInConsd(my_id) == false));
    
    if(res_AndLogicOP_7){
    
    L_P1__Macro1(my_id);
    }else{
    
    L_P1__SetMainc32(my_id,1u);
    }
    
    //  *35,*  se il controllo MainClass_C1_controllo_C8 non è  diverso da  True  *38,* e  se il contatore MainClass_C1_contatore_Co8 non è  uguale a  *53,* 15423 *35,* o  se il controllo MainClass_C1_controllo_C5 è  diverso da RossoGialloGiallo *38,* e  se il contatore MainClass_C1_contatore_Co8 non è  diverso da  *56,* 13 *35,* o  se il controllo MainClass_C1_controllo_C3 è  diverso da RossoGiallo *35,* e  se il controllo MainClass_C1_controllo_C3 non è  uguale a RossoGiallo,  Applica gli effetti
    //         della macro MainClass_C1_macroef_M8
    bool res_OrLogicOP_8 = false;
    bool res_OrLogicOP_9 = false;
    bool res_AndLogicOP_10 = true;
    bool res_NotLogicOP_11 = true;
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (L_P1__GetInMainc6(my_id) == true));
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! res_NotLogicOP_12);
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_NotLogicOP_11);
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (Counter_GetValore(L_P1__GetMainc44(my_id)) == 15423u));
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_NotLogicOP_13);
    
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_AndLogicOP_10);
    bool res_AndLogicOP_14 = true;
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (L_P1__GetInMainc5(my_id) == rossogiallo1));
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_NotLogicOP_15);
    bool res_NotLogicOP_16 = true;
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! (Counter_GetValore(L_P1__GetMainc44(my_id)) == 13u));
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! res_NotLogicOP_17);
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_NotLogicOP_16);
    
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_AndLogicOP_14);
    
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_OrLogicOP_9);
    bool res_AndLogicOP_18 = true;
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (L_P1__GetInMainc4(my_id) == rossogiallo));
    res_AndLogicOP_18 = (res_AndLogicOP_18 && res_NotLogicOP_19);
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! (L_P1__GetInMainc4(my_id) == rossogiallo));
    res_AndLogicOP_18 = (res_AndLogicOP_18 && res_NotLogicOP_20);
    
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_AndLogicOP_18);
    
    if(res_OrLogicOP_8){
    
    L_P1__Macro1(my_id);
    }
}


/*
    CNL corrispondente:
     { commento: {36,}  se il timer MainClass_C1_timer_T4 non è disattivo commento: {35,} o  se il controllo MainClass_C1_controllo_C8 non è  diverso da  True  commento: {35,} o  se il controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo e  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} e  se il timer MainClass_C1_timer_T10 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE , commento: {71,}Decrementa il contatore MainClass_C1_contatore_Co8
    
     ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V4 il valore 1
    
    
     commento: {34,}  se lo stato  non è  uguale a  commento: {53,}  state1  commento: {106,} commento: {37,} e  se la variabile MainClass_C1_variabile_V2 non è  maggiore di  commento: {54,} 8, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V9 il valore 5
    
       
      se il controllo ConsDef  è  uguale a FALSE  commento: {34,} o  se il parametro MainClass_C1_parametro_P3 non è  diverso da  commento: {56,} 2 commento: {38,} o  se il contatore MainClass_C1_contatore_Co8 non è  maggiore di  commento: {54,} 11150 commento: {38,} e  se il contatore MainClass_C1_contatore_Co8 non è  uguale a  commento: {53,} 1542 commento: {34,} e  se il parametro MainClass_C1_parametro_P3 non è  minore di  commento: {55,} 10 commento: {35,} o  se il controllo MainClass_C1_controllo_C1 è  uguale a  False , commento: {68,}Attiva il timer MainClass_C1_timer_T4
    
       
     }
*/
static inline void L_P1__Effec6(instance_id_t const my_id)
{
    
    //  *36,*  se il timer MainClass_C1_timer_T4 non è disattivo *35,* o  se il controllo MainClass_C1_controllo_C8 non è  diverso da  True  *35,* o  se il controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo e  se il controllo ConsDef  è  uguale a FALSE  *36,* e  se il timer MainClass_C1_timer_T10 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE , *71,*Decrementa il contatore MainClass_C1_contatore_Co8
    //   ,altrimenti  *67,* Assegna alla variabile MainClass_C1_variabile_V4 il valore 1
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_OrLogicOP_2 = false;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! Timer_Disattivo(L_P1__GetMainc42(my_id)));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_3);
    bool res_NotLogicOP_4 = true;
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetInMainc6(my_id) == true));
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! res_NotLogicOP_5);
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_4);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_OrLogicOP_2);
    bool res_AndLogicOP_6 = true;
    bool res_AndLogicOP_7 = true;
    res_AndLogicOP_7 = (res_AndLogicOP_7 && (L_P1__GetInMainc4(my_id) == rossogiallo));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && (L_P1__GetInConsd(my_id) == false));
    
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_AndLogicOP_7);
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! Timer_Disattivo(L_P1__GetMainc41(my_id)));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_8);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_6);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    res_OrLogicOP_0 = (res_OrLogicOP_0 || (L_P1__GetInConsd(my_id) == false));
    
    if(res_OrLogicOP_0){
    
    Counter_Decr(L_P1__GetMainc44(my_id));
    }else{
    
    L_P1__SetMainc33(my_id,1u);
    }
    
    //  *34,*  se lo stato  non è  uguale a  *53,*  state1  *106,* *37,* e  se la variabile MainClass_C1_variabile_V2 non è  maggiore di  *54,* 8, *67,* Assegna alla variabile MainClass_C1_variabile_V9 il valore 5
    bool res_AndLogicOP_9 = true;
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1_C1_GetState(my_id) == C1_St_state));
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_NotLogicOP_10);
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (L_P1__GetMainc32(my_id) > 8u));
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_NotLogicOP_11);
    
    if(res_AndLogicOP_9){
    
    L_P1__SetMainc34(my_id,5u);
    }
    
    //  se il controllo ConsDef  è  uguale a FALSE  *34,* o  se il parametro MainClass_C1_parametro_P3 non è  diverso da  *56,* 2 *38,* o  se il contatore MainClass_C1_contatore_Co8 non è  maggiore di  *54,* 11150 *38,* e  se il contatore MainClass_C1_contatore_Co8 non è  uguale a  *53,* 1542 *34,* e  se il parametro MainClass_C1_parametro_P3 non è  minore di  *55,* 10 *35,* o  se il controllo MainClass_C1_controllo_C1 è  uguale a  False , *68,*Attiva il timer MainClass_C1_timer_T4
    bool res_OrLogicOP_12 = false;
    bool res_OrLogicOP_13 = false;
    bool res_OrLogicOP_14 = false;
    res_OrLogicOP_14 = (res_OrLogicOP_14 || (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_15 = true;
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (L_P1__GetParamMainc7(my_id) == 2u));
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! res_NotLogicOP_16);
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_NotLogicOP_15);
    
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_OrLogicOP_14);
    bool res_AndLogicOP_17 = true;
    bool res_AndLogicOP_18 = true;
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (Counter_GetValore(L_P1__GetMainc44(my_id)) > 11150u));
    res_AndLogicOP_18 = (res_AndLogicOP_18 && res_NotLogicOP_19);
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! (Counter_GetValore(L_P1__GetMainc44(my_id)) == 1542u));
    res_AndLogicOP_18 = (res_AndLogicOP_18 && res_NotLogicOP_20);
    
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_AndLogicOP_18);
    bool res_NotLogicOP_21 = true;
    res_NotLogicOP_21 = (res_NotLogicOP_21 && ! (L_P1__GetParamMainc7(my_id) < 10u));
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_NotLogicOP_21);
    
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_AndLogicOP_17);
    
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_OrLogicOP_13);
    res_OrLogicOP_12 = (res_OrLogicOP_12 || (L_P1__GetInMainc3(my_id) == false));
    
    if(res_OrLogicOP_12){
    
    Timer_Attiva(L_P1__GetMainc42(my_id));
    }
}


/*
    CNL corrispondente:
     { commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  maggiore di  commento: {54,} 5 commento: {35,} o  se il controllo MainClass_C1_controllo_C3 non è  uguale a RossoGiallo commento: {37,} o  se la variabile MainClass_C1_variabile_V2 non è  uguale a  commento: {53,} 7, commento: {70,}Incrementa il contatore MainClass_C1_contatore_Co8
    
     ,altrimenti  commento: {68,}Attiva il timer MainClass_C1_timer_T10
    
    
     }
*/
static inline void L_P1__Effec7(instance_id_t const my_id)
{
    
    //  *109,*  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  maggiore di  *54,* 5 *35,* o  se il controllo MainClass_C1_controllo_C3 non è  uguale a RossoGiallo *37,* o  se la variabile MainClass_C1_variabile_V2 non è  uguale a  *53,* 7, *70,*Incrementa il contatore MainClass_C1_contatore_Co8
    //   ,altrimenti  *68,*Attiva il timer MainClass_C1_timer_T10
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    res_OrLogicOP_1 = (res_OrLogicOP_1 || (L_P1__GetMainc29(my_id) > 5u));
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (L_P1__GetInMainc4(my_id) == rossogiallo));
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_NotLogicOP_2);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__GetMainc32(my_id) == 7u));
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_3);
    
    if(res_OrLogicOP_0){
    
    Counter_Incr(L_P1__GetMainc44(my_id));
    }else{
    
    Timer_Attiva(L_P1__GetMainc41(my_id));
    }
}


/*
    CNL corrispondente:
     {  se la macro  MainClass_C1_macrova_M3 ( con argomento_a4   uguale a True ,argomento_a7   uguale a GialloVerde ,argomento_a10   uguale a RossoGialloGiallo ,argomento_a2   uguale a c270x ,argomento_a6   uguale a GialloGiallo  e argomento_a1   uguale a RossoGialloGiallo )   è  uguale a RossoGialloGiallo commento: {40,}  commento: {35,} o  se il controllo MainClass_C1_controllo_C3 non è  diverso da RossoGiallo, commento: {70,}Incrementa il contatore MainClass_C1_contatore_Co8
    
       
     commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo commento: {35,} e  se il controllo MainClass_C1_controllo_C1 non è  uguale a  True  commento: {38,} o  se il contatore MainClass_C1_contatore_Co8 non è  maggiore di  commento: {54,} 14150, commento: {66,} Assegna al comando MainClass_C1_comando_C4 il valore  True 
    
       
     commento: {38,}  se il contatore MainClass_C1_contatore_Co8 è  maggiore di  commento: {54,} 15423 commento: {37,} o  se la variabile MainClass_C1_variabile_V9 è  diverso da  commento: {56,} 4 commento: {34,} e  se il parametro MainClass_C1_parametro_P3 è  minore di  commento: {55,} 9,  Applica gli effetti
           della macro MainClass_C1_macroef_M4( con argomento_af9   uguale a True ,argomento_af5   uguale a GialloVerde ) commento: {73,}
    
       
     }
*/
static inline void L_P1__Effec8(instance_id_t const my_id)
{
    
    //  se la macro  MainClass_C1_macrova_M3 ( con argomento_a4   uguale a True ,argomento_a7   uguale a GialloVerde ,argomento_a10   uguale a RossoGialloGiallo ,argomento_a2   uguale a c270x ,argomento_a6   uguale a GialloGiallo  e argomento_a1   uguale a RossoGialloGiallo )   è  uguale a RossoGialloGiallo *40,*  *35,* o  se il controllo MainClass_C1_controllo_C3 non è  diverso da RossoGiallo, *70,*Incrementa il contatore MainClass_C1_contatore_Co8
    bool res_OrLogicOP_0 = false;
    res_OrLogicOP_0 = (res_OrLogicOP_0 || (L_P1__Macro2(my_id,rossogiallo1,rossogiallo1,c270x,true,giallogiall,gialloverde) == rossogiallo1));
    bool res_NotLogicOP_1 = true;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (L_P1__GetInMainc4(my_id) == rossogiallo));
    res_NotLogicOP_1 = (res_NotLogicOP_1 && ! res_NotLogicOP_2);
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_1);
    
    if(res_OrLogicOP_0){
    
    Counter_Incr(L_P1__GetMainc44(my_id));
    }
    
    //  *110,*  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo *35,* e  se il controllo MainClass_C1_controllo_C1 non è  uguale a  True  *38,* o  se il contatore MainClass_C1_contatore_Co8 non è  maggiore di  *54,* 14150, *66,* Assegna al comando MainClass_C1_comando_C4 il valore  True
    bool res_OrLogicOP_3 = false;
    bool res_AndLogicOP_4 = true;
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! Timer_Attivo(L_P1__GetMainc36(my_id)));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_5);
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetInMainc3(my_id) == true));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_6);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_AndLogicOP_4);
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (Counter_GetValore(L_P1__GetMainc44(my_id)) > 14150u));
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_NotLogicOP_7);
    
    if(res_OrLogicOP_3){
    
    L_P1__SetOutMainc1(my_id,true);
    }
    
    //  *38,*  se il contatore MainClass_C1_contatore_Co8 è  maggiore di  *54,* 15423 *37,* o  se la variabile MainClass_C1_variabile_V9 è  diverso da  *56,* 4 *34,* e  se il parametro MainClass_C1_parametro_P3 è  minore di  *55,* 9,  Applica gli effetti
    //         della macro MainClass_C1_macroef_M4( con argomento_af9   uguale a True ,argomento_af5   uguale a GialloVerde )
    bool res_OrLogicOP_8 = false;
    res_OrLogicOP_8 = (res_OrLogicOP_8 || (Counter_GetValore(L_P1__GetMainc44(my_id)) > 15423u));
    bool res_AndLogicOP_9 = true;
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__GetMainc34(my_id) == 4u));
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_NotLogicOP_10);
    res_AndLogicOP_9 = (res_AndLogicOP_9 && (L_P1__GetParamMainc7(my_id) < 9u));
    
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_AndLogicOP_9);
    
    if(res_OrLogicOP_8){
    
    L_P1__Macro(my_id,gialloverde,true);
    }
}


/*
    CNL corrispondente:
     {  se il controllo ConsDef è uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} o  se il timer MainClass_C1_timer_T4 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} o  se il contatore MainClass_C1_contatore_Co8 non è  uguale a  commento: {53,} 14, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V2 il valore 7
    
       
     commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  diverso da  commento: {56,} 8, commento: {69,}Disattiva il timer MainClass_C1_timer_T4
    
       
      se il controllo ConsDef è uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE , commento: {71,}Decrementa il contatore MainClass_C1_contatore_Co8
    
       
     commento: {36,}  se il timer MainClass_C1_timer_T10 è attivo commento: {37,} e  se la variabile MainClass_C1_variabile_V9 non è  minore di  commento: {55,} 3 commento: {38,} e  se il contatore MainClass_C1_contatore_Co8 non è  minore di  commento: {55,} 14150 commento: {37,} e  se la variabile MainClass_C1_variabile_V4 è  minore di  commento: {55,} 6 commento: {35,} e  se il controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo,  Applica gli effetti
           della macro MainClass_C1_macroef_M4( con argomento_af9   uguale a True ,argomento_af5   uguale a avvio ) commento: {73,}
    
       
     commento: {37,}  se la variabile MainClass_C1_variabile_V9 non è  minore di  commento: {55,} 7 commento: {37,} o  se la variabile MainClass_C1_variabile_V9 è  uguale a  commento: {53,} 3, commento: {69,}Disattiva il timer MainClass_C1_timer_T4
    
       
     }
*/
static inline void L_P1__Effec9(instance_id_t const my_id)
{
    
    //  se il controllo ConsDef è uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  *36,* o  se il timer MainClass_C1_timer_T4 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  *38,* o  se il contatore MainClass_C1_contatore_Co8 non è  uguale a  *53,* 14, *67,* Assegna alla variabile MainClass_C1_variabile_V2 il valore 7
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_AndLogicOP_2 = true;
    res_AndLogicOP_2 = (res_AndLogicOP_2 && (L_P1__GetInConsd(my_id) == false));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_2);
    bool res_AndLogicOP_3 = true;
    bool res_AndLogicOP_4 = true;
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! Timer_Scaduto(L_P1__GetMainc42(my_id)));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_5);
    res_AndLogicOP_4 = (res_AndLogicOP_4 && (L_P1__GetInConsd(my_id) == false));
    
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_AndLogicOP_4);
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_3);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (Counter_GetValore(L_P1__GetMainc44(my_id)) == 14u));
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_6);
    
    if(res_OrLogicOP_0){
    
    L_P1__SetMainc32(my_id,7u);
    }
    
    //  *109,*  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  diverso da  *56,* 8, *69,*Disattiva il timer MainClass_C1_timer_T4
    bool res_NotLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetMainc29(my_id) == 8u));
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! res_NotLogicOP_8);
    if(res_NotLogicOP_7){
    
    Timer_Disattiva(L_P1__GetMainc42(my_id));
    }
    
    //  se il controllo ConsDef è uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE , *71,*Decrementa il contatore MainClass_C1_contatore_Co8
    bool res_AndLogicOP_9 = true;
    res_AndLogicOP_9 = (res_AndLogicOP_9 && (L_P1__GetInConsd(my_id) == false));
    res_AndLogicOP_9 = (res_AndLogicOP_9 && (L_P1__GetInConsd(my_id) == false));
    
    if(res_AndLogicOP_9){
    
    Counter_Decr(L_P1__GetMainc44(my_id));
    }
    
    //  *36,*  se il timer MainClass_C1_timer_T10 è attivo *37,* e  se la variabile MainClass_C1_variabile_V9 non è  minore di  *55,* 3 *38,* e  se il contatore MainClass_C1_contatore_Co8 non è  minore di  *55,* 14150 *37,* e  se la variabile MainClass_C1_variabile_V4 è  minore di  *55,* 6 *35,* e  se il controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo,  Applica gli effetti
    //         della macro MainClass_C1_macroef_M4( con argomento_af9   uguale a True ,argomento_af5   uguale a avvio )
    bool res_AndLogicOP_10 = true;
    bool res_AndLogicOP_11 = true;
    bool res_AndLogicOP_12 = true;
    bool res_AndLogicOP_13 = true;
    res_AndLogicOP_13 = (res_AndLogicOP_13 && Timer_Attivo(L_P1__GetMainc41(my_id)));
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1__GetMainc34(my_id) < 3u));
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_NotLogicOP_14);
    
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_AndLogicOP_13);
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (Counter_GetValore(L_P1__GetMainc44(my_id)) < 14150u));
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_NotLogicOP_15);
    
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_AndLogicOP_12);
    res_AndLogicOP_11 = (res_AndLogicOP_11 && (L_P1__GetMainc33(my_id) < 6u));
    
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_AndLogicOP_11);
    res_AndLogicOP_10 = (res_AndLogicOP_10 && (L_P1__GetInMainc4(my_id) == rossogiallo));
    
    if(res_AndLogicOP_10){
    
    L_P1__Macro(my_id,avvio,true);
    }
    
    //  *73,*
    //     
    //   *37,*  se la variabile MainClass_C1_variabile_V9 non è  minore di  *55,* 7 *37,* o  se la variabile MainClass_C1_variabile_V9 è  uguale a  *53,* 3, *69,*Disattiva il timer MainClass_C1_timer_T4
    bool res_OrLogicOP_16 = false;
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! (L_P1__GetMainc34(my_id) < 7u));
    res_OrLogicOP_16 = (res_OrLogicOP_16 || res_NotLogicOP_17);
    res_OrLogicOP_16 = (res_OrLogicOP_16 || (L_P1__GetMainc34(my_id) == 3u));
    
    if(res_OrLogicOP_16){
    
    Timer_Disattiva(L_P1__GetMainc42(my_id));
    }
}


/*
    CNL corrispondente:
     { commento: {37,}  se la variabile MainClass_C1_variabile_V9 è  maggiore di  commento: {54,} 6 commento: {35,} o  se il controllo MainClass_C1_controllo_C3 è  diverso da RossoGiallo commento: {34,} e  se il parametro MainClass_C1_parametro_P6 è  diverso da c270 commento: {36,} o  se il timer MainClass_C1_timer_T9 è disattivo commento: {36,} o  se il timer MainClass_C1_timer_T9 è attivo o  se il controllo ConsDef  è  uguale a FALSE , commento: {70,}Incrementa il contatore MainClass_C1_contatore_Co8
    
     ,altrimenti  commento: {66,} Assegna al comando MainClass_C1_comando_C4 il valore  True 
    
    
     commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo, commento: {66,} Assegna al comando MainClass_C1_comando_C4 il valore  False 
    
     ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V9 il valore 10
    
    
      se il ripristino dello stato  è  diverso da  commento: {56,}  state1  commento: {107,} e  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro MainClass_C1_parametro_P9 è  diverso da  commento: {56,} 1 commento: {34,} e  se il parametro MainClass_C1_parametro_P9 è  maggiore di  commento: {54,} 9 commento: {36,} e  se il timer MainClass_C1_timer_T4 è disattivo commento: {38,} o  se il contatore MainClass_C1_contatore_Co8 è  minore di  commento: {55,} 11, commento: {69,}Disattiva il timer MainClass_C1_timer_T10
    
     ,altrimenti  commento: {72,}Azzera il contatore MainClass_C1_contatore_Co8
    
    
     commento: {37,}  se la variabile MainClass_C1_variabile_V9 è  minore di  commento: {55,} 5 commento: {35,} e  se il controllo MainClass_C1_controllo_C1 è  diverso da  False  commento: {34,} o  se il parametro MainClass_C1_parametro_P9 non è  maggiore di  commento: {54,} 3 commento: {37,} e  se la variabile MainClass_C1_variabile_V2 non è  diverso da  commento: {56,} 9 commento: {37,} e  se la variabile MainClass_C1_variabile_V2 è  diverso da  commento: {56,} 8, commento: {69,}Disattiva il timer MainClass_C1_timer_T4
    
       
     }
*/
static inline void L_P1__Effec10(instance_id_t const my_id)
{
    
    //  *37,*  se la variabile MainClass_C1_variabile_V9 è  maggiore di  *54,* 6 *35,* o  se il controllo MainClass_C1_controllo_C3 è  diverso da RossoGiallo *34,* e  se il parametro MainClass_C1_parametro_P6 è  diverso da c270 *36,* o  se il timer MainClass_C1_timer_T9 è disattivo *36,* o  se il timer MainClass_C1_timer_T9 è attivo o  se il controllo ConsDef  è  uguale a FALSE , *70,*Incrementa il contatore MainClass_C1_contatore_Co8
    //   ,altrimenti  *66,* Assegna al comando MainClass_C1_comando_C4 il valore  True
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    res_OrLogicOP_3 = (res_OrLogicOP_3 || (L_P1__GetMainc34(my_id) > 6u));
    bool res_AndLogicOP_4 = true;
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetInMainc4(my_id) == rossogiallo));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_5);
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetParamMainc8(my_id) == c270));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_6);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_AndLogicOP_4);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    res_OrLogicOP_2 = (res_OrLogicOP_2 || Timer_Disattivo(L_P1__GetMainc43(my_id)));
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_OrLogicOP_2);
    res_OrLogicOP_1 = (res_OrLogicOP_1 || Timer_Attivo(L_P1__GetMainc43(my_id)));
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    res_OrLogicOP_0 = (res_OrLogicOP_0 || (L_P1__GetInConsd(my_id) == false));
    
    if(res_OrLogicOP_0){
    
    Counter_Incr(L_P1__GetMainc44(my_id));
    }else{
    
    L_P1__SetOutMainc1(my_id,true);
    }
    
    //  *110,*  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo, *66,* Assegna al comando MainClass_C1_comando_C4 il valore  False 
    //   ,altrimenti  *67,* Assegna alla variabile MainClass_C1_variabile_V9 il valore 10
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! Timer_Attivo(L_P1__GetMainc36(my_id)));
    if(res_NotLogicOP_7){
    
    L_P1__SetOutMainc1(my_id,false);
    }else{
    
    L_P1__SetMainc34(my_id,10u);
    }
    
    //  se il ripristino dello stato  è  diverso da  *56,*  state1  *107,* e  se il controllo ConsDef  è  uguale a FALSE  *34,* e  se il parametro MainClass_C1_parametro_P9 è  diverso da  *56,* 1 *34,* e  se il parametro MainClass_C1_parametro_P9 è  maggiore di  *54,* 9 *36,* e  se il timer MainClass_C1_timer_T4 è disattivo *38,* o  se il contatore MainClass_C1_contatore_Co8 è  minore di  *55,* 11, *69,*Disattiva il timer MainClass_C1_timer_T10
    //   ,altrimenti  *72,*Azzera il contatore MainClass_C1_contatore_Co8
    bool res_OrLogicOP_8 = false;
    bool res_AndLogicOP_9 = true;
    bool res_AndLogicOP_10 = true;
    bool res_AndLogicOP_11 = true;
    bool res_AndLogicOP_12 = true;
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (L_P1__GetStato1(my_id) == C1_St_state));
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_NotLogicOP_13);
    res_AndLogicOP_12 = (res_AndLogicOP_12 && (L_P1__GetInConsd(my_id) == false));
    
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_AndLogicOP_12);
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1__GetParamMainc9(my_id) == 1u));
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_NotLogicOP_14);
    
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_AndLogicOP_11);
    res_AndLogicOP_10 = (res_AndLogicOP_10 && (L_P1__GetParamMainc9(my_id) > 9u));
    
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_AndLogicOP_10);
    res_AndLogicOP_9 = (res_AndLogicOP_9 && Timer_Disattivo(L_P1__GetMainc42(my_id)));
    
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_AndLogicOP_9);
    res_OrLogicOP_8 = (res_OrLogicOP_8 || (Counter_GetValore(L_P1__GetMainc44(my_id)) < 11u));
    
    if(res_OrLogicOP_8){
    
    Timer_Disattiva(L_P1__GetMainc41(my_id));
    }else{
    
    Counter_Res(L_P1__GetMainc44(my_id));
    }
    
    //  *37,*  se la variabile MainClass_C1_variabile_V9 è  minore di  *55,* 5 *35,* e  se il controllo MainClass_C1_controllo_C1 è  diverso da  False  *34,* o  se il parametro MainClass_C1_parametro_P9 non è  maggiore di  *54,* 3 *37,* e  se la variabile MainClass_C1_variabile_V2 non è  diverso da  *56,* 9 *37,* e  se la variabile MainClass_C1_variabile_V2 è  diverso da  *56,* 8, *69,*Disattiva il timer MainClass_C1_timer_T4
    bool res_OrLogicOP_15 = false;
    bool res_AndLogicOP_16 = true;
    res_AndLogicOP_16 = (res_AndLogicOP_16 && (L_P1__GetMainc34(my_id) < 5u));
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! (L_P1__GetInMainc3(my_id) == false));
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_NotLogicOP_17);
    
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_AndLogicOP_16);
    bool res_AndLogicOP_18 = true;
    bool res_AndLogicOP_19 = true;
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! (L_P1__GetParamMainc9(my_id) > 3u));
    res_AndLogicOP_19 = (res_AndLogicOP_19 && res_NotLogicOP_20);
    bool res_NotLogicOP_21 = true;
    bool res_NotLogicOP_22 = true;
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! (L_P1__GetMainc32(my_id) == 9u));
    res_NotLogicOP_21 = (res_NotLogicOP_21 && ! res_NotLogicOP_22);
    res_AndLogicOP_19 = (res_AndLogicOP_19 && res_NotLogicOP_21);
    
    res_AndLogicOP_18 = (res_AndLogicOP_18 && res_AndLogicOP_19);
    bool res_NotLogicOP_23 = true;
    res_NotLogicOP_23 = (res_NotLogicOP_23 && ! (L_P1__GetMainc32(my_id) == 8u));
    res_AndLogicOP_18 = (res_AndLogicOP_18 && res_NotLogicOP_23);
    
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_AndLogicOP_18);
    
    if(res_OrLogicOP_15){
    
    Timer_Disattiva(L_P1__GetMainc42(my_id));
    }
}


/*
    CNL corrispondente:
    
    {
    
     commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  maggiore di  commento: {54,} 5,  Applica gli effetti
           della macro MainClass_C1_macroef_M8  commento: {73,}
    
       
     commento: {35,}  se il controllo MainClass_C1_controllo_C3 non è  diverso da RossoGiallo commento: {37,} e  se la variabile MainClass_C1_variabile_V4 non è  uguale a  commento: {53,} 7 commento: {38,} o  se il contatore MainClass_C1_contatore_Co8 è  uguale a  commento: {53,} 11 commento: {38,} e  se il contatore MainClass_C1_contatore_Co8 è  diverso da  commento: {56,} 12 commento: {37,} o  se la variabile MainClass_C1_variabile_V9 non è  minore di  commento: {55,} 9, commento: {66,} Assegna al comando MainClass_C1_comando_C4 il valore  True 
    
     ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V4 il valore 6
    
    
     commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo e  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} o  se il timer MainClass_C1_timer_T4 è scaduto commento: {35,} o  se il controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo, commento: {72,}Azzera il contatore MainClass_C1_contatore_Co8
    
     ,altrimenti  commento: {66,} Assegna al comando MainClass_C1_comando_C4 il valore  True 
    
    
     commento: {37,}  se la variabile MainClass_C1_variabile_V4 è  minore di  commento: {55,} 9,  Applica gli effetti
           della macro MainClass_C1_macroef_M8  commento: {73,}
    
     ,altrimenti  commento: {68,}Attiva il timer MainClass_C1_timer_T4
    
    
     commento: {34,}  se il parametro MainClass_C1_parametro_P9 è  maggiore di  commento: {54,} 8 commento: {34,} e  se il parametro MainClass_C1_parametro_P3 non è  diverso da  commento: {56,} 4, commento: {69,}Disattiva il timer MainClass_C1_timer_T10
    
       
    
    }
*/
static inline void L_P1__Effec11(instance_id_t const my_id)
{
    
    //  *109,*  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  maggiore di  *54,* 5,  Applica gli effetti
    //         della macro MainClass_C1_macroef_M8
    if((L_P1__GetMainc29(my_id) > 5u)){
    
    L_P1__Macro1(my_id);
    }
    
    //  *73,*
    //     
    //   *35,*  se il controllo MainClass_C1_controllo_C3 non è  diverso da RossoGiallo *37,* e  se la variabile MainClass_C1_variabile_V4 non è  uguale a  *53,* 7 *38,* o  se il contatore MainClass_C1_contatore_Co8 è  uguale a  *53,* 11 *38,* e  se il contatore MainClass_C1_contatore_Co8 è  diverso da  *56,* 12 *37,* o  se la variabile MainClass_C1_variabile_V9 non è  minore di  *55,* 9, *66,* Assegna al comando MainClass_C1_comando_C4 il valore  True 
    //   ,altrimenti  *67,* Assegna alla variabile MainClass_C1_variabile_V4 il valore 6
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_AndLogicOP_2 = true;
    bool res_NotLogicOP_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetInMainc4(my_id) == rossogiallo));
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! res_NotLogicOP_4);
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_3);
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetMainc33(my_id) == 7u));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_5);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_2);
    bool res_AndLogicOP_6 = true;
    res_AndLogicOP_6 = (res_AndLogicOP_6 && (Counter_GetValore(L_P1__GetMainc44(my_id)) == 11u));
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (Counter_GetValore(L_P1__GetMainc44(my_id)) == 12u));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_7);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_6);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetMainc34(my_id) < 9u));
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_8);
    
    if(res_OrLogicOP_0){
    
    L_P1__SetOutMainc1(my_id,true);
    }else{
    
    L_P1__SetMainc33(my_id,6u);
    }
    
    //  *110,*  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo e  se il controllo ConsDef  è  uguale a FALSE  *36,* o  se il timer MainClass_C1_timer_T4 è scaduto *35,* o  se il controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo, *72,*Azzera il contatore MainClass_C1_contatore_Co8
    //   ,altrimenti  *66,* Assegna al comando MainClass_C1_comando_C4 il valore  True
    bool res_OrLogicOP_9 = false;
    bool res_OrLogicOP_10 = false;
    bool res_AndLogicOP_11 = true;
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! Timer_Attivo(L_P1__GetMainc36(my_id)));
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_NotLogicOP_12);
    res_AndLogicOP_11 = (res_AndLogicOP_11 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_AndLogicOP_11);
    res_OrLogicOP_10 = (res_OrLogicOP_10 || Timer_Scaduto(L_P1__GetMainc42(my_id)));
    
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_OrLogicOP_10);
    res_OrLogicOP_9 = (res_OrLogicOP_9 || (L_P1__GetInMainc4(my_id) == rossogiallo));
    
    if(res_OrLogicOP_9){
    
    Counter_Res(L_P1__GetMainc44(my_id));
    }else{
    
    L_P1__SetOutMainc1(my_id,true);
    }
    
    //  *37,*  se la variabile MainClass_C1_variabile_V4 è  minore di  *55,* 9,  Applica gli effetti
    //         della macro MainClass_C1_macroef_M8  *73,*
    //   ,altrimenti  *68,*Attiva il timer MainClass_C1_timer_T4
    if((L_P1__GetMainc33(my_id) < 9u)){
    
    L_P1__Macro1(my_id);
    }else{
    
    Timer_Attiva(L_P1__GetMainc42(my_id));
    }
    
    //  *34,*  se il parametro MainClass_C1_parametro_P9 è  maggiore di  *54,* 8 *34,* e  se il parametro MainClass_C1_parametro_P3 non è  diverso da  *56,* 4, *69,*Disattiva il timer MainClass_C1_timer_T10
    bool res_AndLogicOP_13 = true;
    res_AndLogicOP_13 = (res_AndLogicOP_13 && (L_P1__GetParamMainc9(my_id) > 8u));
    bool res_NotLogicOP_14 = true;
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (L_P1__GetParamMainc7(my_id) == 4u));
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! res_NotLogicOP_15);
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_NotLogicOP_14);
    
    if(res_AndLogicOP_13){
    
    Timer_Disattiva(L_P1__GetMainc41(my_id));
    }
}


/*
    CNL corrispondente:
    
    {
    
     commento: {34,}  se il parametro MainClass_C1_parametro_P3 è  minore di  commento: {55,} 9 commento: {38,} o  se il contatore MainClass_C1_contatore_Co8 è  diverso da  commento: {56,} 1323 commento: {35,} o  se il controllo MainClass_C1_controllo_C3 non è  uguale a RossoGiallo commento: {38,} o  se il contatore MainClass_C1_contatore_Co8 non è  diverso da  commento: {56,} 11150 commento: {37,} o  se la variabile MainClass_C1_variabile_V9 è  diverso da  commento: {56,} 10, commento: {66,} Assegna al comando MainClass_C1_comando_C3 il valore  False 
    
     ,altrimenti  commento: {66,} Assegna al comando MainClass_C1_comando_C4 il valore  True 
    
    
    
    }
*/
static inline void L_P1__Effec12(instance_id_t const my_id)
{
    
    //  *34,*  se il parametro MainClass_C1_parametro_P3 è  minore di  *55,* 9 *38,* o  se il contatore MainClass_C1_contatore_Co8 è  diverso da  *56,* 1323 *35,* o  se il controllo MainClass_C1_controllo_C3 non è  uguale a RossoGiallo *38,* o  se il contatore MainClass_C1_contatore_Co8 non è  diverso da  *56,* 11150 *37,* o  se la variabile MainClass_C1_variabile_V9 è  diverso da  *56,* 10, *66,* Assegna al comando MainClass_C1_comando_C3 il valore  False 
    //   ,altrimenti  *66,* Assegna al comando MainClass_C1_comando_C4 il valore  True
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    res_OrLogicOP_3 = (res_OrLogicOP_3 || (L_P1__GetParamMainc7(my_id) < 9u));
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (Counter_GetValore(L_P1__GetMainc44(my_id)) == 1323u));
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_NotLogicOP_4);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetInMainc4(my_id) == rossogiallo));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_5);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_OrLogicOP_2);
    bool res_NotLogicOP_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (Counter_GetValore(L_P1__GetMainc44(my_id)) == 11150u));
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! res_NotLogicOP_7);
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_NotLogicOP_6);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetMainc34(my_id) == 10u));
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_8);
    
    if(res_OrLogicOP_0){
    
    L_P1__SetOutMainc(my_id,false);
    }else{
    
    L_P1__SetOutMainc1(my_id,true);
    }
}


/*
    CNL corrispondente:
     { commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI3 non è scaduto commento: {35,} e  se il controllo MainClass_C1_controllo_C3 è  diverso da RossoGiallo,  Applica gli effetti
           della macro MainClass_C1_macroef_M8  commento: {73,}
    
       
     commento: {34,}  se il parametro MainClass_C1_parametro_P6 non è  uguale a c270 commento: {34,} e  se il parametro MainClass_C1_parametro_P3 è  diverso da  commento: {56,} 3 o  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} o  se il controllo MainClass_C1_controllo_C8 non è  uguale a  False  commento: {35,} e  se il controllo MainClass_C1_controllo_C5 è  diverso da RossoGialloGiallo,  Applica gli effetti
           della macro MainClass_C1_macroef_M4( con argomento_af9   uguale a True ,argomento_af5   uguale a avvio ) commento: {73,}
    
       
      se il ripristino dello stato  non è  uguale a  commento: {53,}  state1  commento: {107,}, commento: {70,}Incrementa il contatore MainClass_C1_contatore_Co8
    
     ,altrimenti  commento: {66,} Assegna al comando MainClass_C1_comando_C3 il valore  True 
    
    
     }
*/
static inline void L_P1__Effec13(instance_id_t const my_id)
{
    
    //  *110,*  se il ripristino del timer  MainClass_C1_restoreTI_TI3 non è scaduto *35,* e  se il controllo MainClass_C1_controllo_C3 è  diverso da RossoGiallo,  Applica gli effetti
    //         della macro MainClass_C1_macroef_M8
    bool res_AndLogicOP_0 = true;
    bool res_NotLogicOP_1 = true;
    res_NotLogicOP_1 = (res_NotLogicOP_1 && ! Timer_Scaduto(L_P1__GetMainc40(my_id)));
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_NotLogicOP_1);
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (L_P1__GetInMainc4(my_id) == rossogiallo));
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_NotLogicOP_2);
    
    if(res_AndLogicOP_0){
    
    L_P1__Macro1(my_id);
    }
    
    //  *73,*
    //     
    //   *34,*  se il parametro MainClass_C1_parametro_P6 non è  uguale a c270 *34,* e  se il parametro MainClass_C1_parametro_P3 è  diverso da  *56,* 3 o  se il controllo ConsDef  è  uguale a FALSE  *35,* o  se il controllo MainClass_C1_controllo_C8 non è  uguale a  False  *35,* e  se il controllo MainClass_C1_controllo_C5 è  diverso da RossoGialloGiallo,  Applica gli effetti
    //         della macro MainClass_C1_macroef_M4( con argomento_af9   uguale a True ,argomento_af5   uguale a avvio )
    bool res_OrLogicOP_3 = false;
    bool res_OrLogicOP_4 = false;
    bool res_AndLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetParamMainc8(my_id) == c270));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_6);
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetParamMainc7(my_id) == 3u));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_7);
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_AndLogicOP_5);
    res_OrLogicOP_4 = (res_OrLogicOP_4 || (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_OrLogicOP_4);
    bool res_AndLogicOP_8 = true;
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetInMainc6(my_id) == false));
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_9);
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__GetInMainc5(my_id) == rossogiallo1));
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_10);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_AndLogicOP_8);
    
    if(res_OrLogicOP_3){
    
    L_P1__Macro(my_id,avvio,true);
    }
    
    //  *73,*
    //     
    //    se il ripristino dello stato  non è  uguale a  *53,*  state1  *107,*, *70,*Incrementa il contatore MainClass_C1_contatore_Co8
    //   ,altrimenti  *66,* Assegna al comando MainClass_C1_comando_C3 il valore  True
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (L_P1__GetStato1(my_id) == C1_St_state));
    if(res_NotLogicOP_11){
    
    Counter_Incr(L_P1__GetMainc44(my_id));
    }else{
    
    L_P1__SetOutMainc(my_id,true);
    }
}



// ********** Definizione metodi **********

// Metodi standard

void L_P1_C1_Init(instance_id_t const my_id)
{
    // init variabili di stato
    L_P1__SetMainc18(my_id, 0);
    L_P1__SetMainc20(my_id, false);
    L_P1__SetMainc22(my_id, false);
    L_P1__SetMainc24(my_id, giallogiall);
    L_P1__SetMainc26(my_id, false);
    L_P1__SetMainc28(my_id, 0);
    L_P1__SetMainc29(my_id, 0);
    L_P1__SetMainc30(my_id, c270x);
    L_P1__SetMainc31(my_id, c270x);
    L_P1__SetMainc32(my_id, 0);
    L_P1__SetMainc33(my_id, 0);
    L_P1__SetMainc34(my_id, 0);
    L_P1__SetStato1(my_id, C1_St_Stato);
    // init controlli precedenti
    L_P1__SetMainc11(my_id, c270);
    L_P1__SetMainc13(my_id, true);
    L_P1__SetMainc15(my_id, false);
    L_P1__SetMainc17(my_id, c270);
    // init Timer e Counter
    Timer_AggmInit(L_P1__GetMainc35(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc35_ID);
    Timer_Init(L_P1__GetMainc35(my_id), 10000);
    Timer_AggmInit(L_P1__GetMainc36(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc36_ID);
    Timer_Init(L_P1__GetMainc36(my_id), 10000);
    Timer_AggmInit(L_P1__GetMainc37(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc37_ID);
    Timer_Init(L_P1__GetMainc37(my_id), 24000);
    Timer_AggmInit(L_P1__GetMainc38(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc38_ID);
    Timer_Init(L_P1__GetMainc38(my_id), 24000);
    Timer_AggmInit(L_P1__GetMainc39(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc39_ID);
    Timer_Init(L_P1__GetMainc39(my_id), 42000);
    Timer_AggmInit(L_P1__GetMainc40(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc40_ID);
    Timer_Init(L_P1__GetMainc40(my_id), 42000);
    Timer_AggmInit(L_P1__GetMainc41(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc41_ID);
    Timer_Init(L_P1__GetMainc41(my_id), 35000);
    Timer_AggmInit(L_P1__GetMainc42(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc42_ID);
    Timer_Init(L_P1__GetMainc42(my_id), 43000);
    Timer_AggmInit(L_P1__GetMainc43(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc43_ID);
    Timer_Init(L_P1__GetMainc43(my_id), 51000);
    Counter_AggmInit(L_P1__GetMainc44(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc44_ID);
    Counter_Init(L_P1__GetMainc44(my_id));
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
    L_P1__SetMainc19(my_id, L_P1__GetMainc18(my_id));
    L_P1__SetMainc21(my_id, L_P1__GetMainc20(my_id));
    L_P1__SetMainc23(my_id, L_P1__GetMainc22(my_id));
    L_P1__SetMainc25(my_id, L_P1__GetMainc24(my_id));
    L_P1__SetMainc27(my_id, L_P1__GetMainc26(my_id));
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
            if (L_P1__Guard1(my_id)) {
                L_P1_C1_SetState(my_id, C1_St_state);
                L_P1__Effec1(my_id);				
            }
            else
                { } // fine transizioni da state nella fase LDS_PHASE_MANUAL
            break;

        case C1_St_state5:
                { } // fine transizioni da state5 nella fase LDS_PHASE_MANUAL
            break;

        case C1_St_state4:
                { } // fine transizioni da state4 nella fase LDS_PHASE_MANUAL
            break;

        case C1_St_state3:
                { } // fine transizioni da state3 nella fase LDS_PHASE_MANUAL
            break;

        case C1_St_state2:
                { } // fine transizioni da state2 nella fase LDS_PHASE_MANUAL
            break;

        default:
            STOP_EXECUTION(LOGIC_ERROR);
            break;  // Needed for MISRA C syntactic compliance
        } // switch sugli stati chiuso
        break;
 

    case LDS_PHASE_STATE:

        switch (L_P1_C1_GetState(my_id)) {

        case C1_St_state1:
            if (L_P1__Guard3(my_id)) {
                L_P1_C1_SetState(my_id, C1_St_state);
                L_P1__Effec3(my_id);				
            }
            else if (L_P1__Guard2(my_id)) {
                L_P1_C1_SetState(my_id, C1_St_state1);
                L_P1__Effec2(my_id);				
            }
            else
                {STOP_EXECUTION(LOGIC_ERROR); } // fine transizioni da state1 nella fase LDS_PHASE_STATE
            break;

        case C1_St_state:
                {STOP_EXECUTION(LOGIC_ERROR); } // fine transizioni da state nella fase LDS_PHASE_STATE
            break;

        case C1_St_state5:
            if (L_P1__Guard13(my_id)) {
                L_P1_C1_SetState(my_id, C1_St_state3);
                L_P1__Effec13(my_id);				
            }
            else if (L_P1__Guard12(my_id)) {
                L_P1_C1_SetState(my_id, C1_St_state5);
                L_P1__Effec12(my_id);				
            }
            else
                {STOP_EXECUTION(LOGIC_ERROR); } // fine transizioni da state5 nella fase LDS_PHASE_STATE
            break;

        case C1_St_state4:
            if (L_P1__Guard11(my_id)) {
                L_P1_C1_SetState(my_id, C1_St_state4);
                L_P1__Effec11(my_id);				
            }
            else
                {STOP_EXECUTION(LOGIC_ERROR); } // fine transizioni da state4 nella fase LDS_PHASE_STATE
            break;

        case C1_St_state3:
            if (L_P1__Guard7(my_id)) {
                L_P1_C1_SetState(my_id, C1_St_state5);
                L_P1__Effec7(my_id);				
            }
            else if (L_P1__Guard8(my_id)) {
                L_P1_C1_SetState(my_id, C1_St_state4);
                L_P1__Effec8(my_id);				
            }
            else if (L_P1__Guard9(my_id)) {
                L_P1_C1_SetState(my_id, C1_St_state);
                L_P1__Effec9(my_id);				
            }
            else if (L_P1__Guard10(my_id)) {
                L_P1_C1_SetState(my_id, C1_St_state2);
                L_P1__Effec10(my_id);				
            }
            else if (L_P1__Guard5(my_id)) {
                L_P1_C1_SetState(my_id, C1_St_state3);
                L_P1__Effec5(my_id);				
            }
            else
                {STOP_EXECUTION(LOGIC_ERROR); } // fine transizioni da state3 nella fase LDS_PHASE_STATE
            break;

        case C1_St_state2:
            if (L_P1__Guard4(my_id)) {
                L_P1_C1_SetState(my_id, C1_St_state2);
                L_P1__Effec4(my_id);				
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
        {
        size_t auto_commands_before = L_P1_C1_NumAutoCmds(my_id);
        switch (L_P1_C1_GetState(my_id)) {

        case C1_St_state1:
                { } // fine transizioni da state1 nella fase LDS_PHASE_AUTO
            break;

        case C1_St_state:
                { } // fine transizioni da state nella fase LDS_PHASE_AUTO
            break;

        case C1_St_state5:
                { } // fine transizioni da state5 nella fase LDS_PHASE_AUTO
            break;

        case C1_St_state4:
                { } // fine transizioni da state4 nella fase LDS_PHASE_AUTO
            break;

        case C1_St_state3:
            if (L_P1__Guard6(my_id)) {
                L_P1_C1_SetState(my_id, C1_St_state1);
                L_P1__Effec6(my_id);				
            }
            else
                { } // fine transizioni da state3 nella fase LDS_PHASE_AUTO
            break;

        case C1_St_state2:
                { } // fine transizioni da state2 nella fase LDS_PHASE_AUTO
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
    Timer_Exec(L_P1__GetMainc35(my_id));
    Timer_Exec(L_P1__GetMainc36(my_id));
    Timer_Exec(L_P1__GetMainc37(my_id));
    Timer_Exec(L_P1__GetMainc38(my_id));
    Timer_Exec(L_P1__GetMainc39(my_id));
    Timer_Exec(L_P1__GetMainc40(my_id));
    Timer_Exec(L_P1__GetMainc41(my_id));
    Timer_Exec(L_P1__GetMainc42(my_id));
    Timer_Exec(L_P1__GetMainc43(my_id));
}

void L_P1_C1_GSetSafe(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C1(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C1(proc_id);
    L_P1__SetOutMainc(my_id, false);
    L_P1__SetOutMainc1(my_id, false);
    L_P1__SetOutMainc2(my_id, false);
}

void L_P1_C1_GUpdatePrev(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C1(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C1(proc_id);
    L_P1__SetMainc11(my_id, L_P1__GetInMainc10(my_id));
    L_P1__SetMainc13(my_id, L_P1__GetInMainc12(my_id));
    L_P1__SetMainc15(my_id, L_P1__GetInMainc14(my_id));
    L_P1__SetMainc17(my_id, L_P1__GetInMainc16(my_id));
    L_P1__SetMainc19(my_id, L_P1__GetMainc18(my_id));
    L_P1__SetMainc21(my_id, L_P1__GetMainc20(my_id));
    L_P1__SetMainc23(my_id, L_P1__GetMainc22(my_id));
    L_P1__SetMainc25(my_id, L_P1__GetMainc24(my_id));
    L_P1__SetMainc27(my_id, L_P1__GetMainc26(my_id));
}

// ********** Definizione macro **********

// Macro di effetto

/*
    CNL corrispondente:
    
    {  se la macro  MainClass_C1_macrova_M3 ( con argomento_a4   uguale a True ,argomento_a7   uguale a GialloVerde ,argomento_a10   uguale a c270x ,argomento_a2   uguale a RossoGialloGiallo ,argomento_a6   uguale a GialloGiallo  e argomento_a1   uguale a c270x )   è  diverso da RossoGialloGiallo commento: {40,}  commento: {35,} o  se il controllo MainClass_C1_controllo_C3 non è  uguale a RossoGiallo commento: {37,} o  se la variabile MainClass_C1_variabile_V9 non è  diverso da  commento: {56,} 5 commento: {34,} e  se il parametro MainClass_C1_parametro_P6 non è  diverso da c270, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V4 il valore 6
    
       
     commento: {37,}  se la variabile MainClass_C1_variabile_V9 non è  minore di  commento: {55,} 2 commento: {36,} e  se il timer MainClass_C1_timer_T10 è disattivo commento: {36,} e  se il timer MainClass_C1_timer_T4 è scaduto commento: {38,} o  se il contatore MainClass_C1_contatore_Co8 è  minore di  commento: {55,} 15 commento: {36,} e  se il timer MainClass_C1_timer_T4 è attivo commento: {38,} o  se il contatore MainClass_C1_contatore_Co8 è  diverso da  commento: {56,} 122, commento: {66,} Assegna al comando MainClass_C1_comando_C4 il valore  False 
    
     ,altrimenti  commento: {72,}Azzera il contatore MainClass_C1_contatore_Co8
    
    
    
    }
*/
void L_P1__Macro(instance_id_t const my_id , C1_Enumerat2 argom, bool argom1)
{
//  se la macro  MainClass_C1_macrova_M3 ( con argomento_a4   uguale a True ,argomento_a7   uguale a GialloVerde ,argomento_a10   uguale a c270x ,argomento_a2   uguale a RossoGialloGiallo ,argomento_a6   uguale a GialloGiallo  e argomento_a1   uguale a c270x )   è  diverso da RossoGialloGiallo *40,*  *35,* o  se il controllo MainClass_C1_controllo_C3 non è  uguale a RossoGiallo *37,* o  se la variabile MainClass_C1_variabile_V9 non è  diverso da  *56,* 5 *34,* e  se il parametro MainClass_C1_parametro_P6 non è  diverso da c270, *67,* Assegna alla variabile MainClass_C1_variabile_V4 il valore 6
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (L_P1__Macro2(my_id,c270x,c270x,rossogiallo1,true,giallogiall,gialloverde) == rossogiallo1));
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_NotLogicOP_2);
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__GetInMainc4(my_id) == rossogiallo));
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_NotLogicOP_3);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_AndLogicOP_4 = true;
    bool res_NotLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetMainc34(my_id) == 5u));
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! res_NotLogicOP_6);
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_5);
    bool res_NotLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetParamMainc8(my_id) == c270));
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! res_NotLogicOP_8);
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_7);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_4);
    
    if(res_OrLogicOP_0){
    
    L_P1__SetMainc33(my_id,6u);
    }
    //  *37,*  se la variabile MainClass_C1_variabile_V9 non è  minore di  *55,* 2 *36,* e  se il timer MainClass_C1_timer_T10 è disattivo *36,* e  se il timer MainClass_C1_timer_T4 è scaduto *38,* o  se il contatore MainClass_C1_contatore_Co8 è  minore di  *55,* 15 *36,* e  se il timer MainClass_C1_timer_T4 è attivo *38,* o  se il contatore MainClass_C1_contatore_Co8 è  diverso da  *56,* 122, *66,* Assegna al comando MainClass_C1_comando_C4 il valore  False 
    // ,altrimenti  *72,*Azzera il contatore MainClass_C1_contatore_Co8
    bool res_OrLogicOP_9 = false;
    bool res_OrLogicOP_10 = false;
    bool res_AndLogicOP_11 = true;
    bool res_AndLogicOP_12 = true;
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (L_P1__GetMainc34(my_id) < 2u));
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_NotLogicOP_13);
    res_AndLogicOP_12 = (res_AndLogicOP_12 && Timer_Disattivo(L_P1__GetMainc41(my_id)));
    
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_AndLogicOP_12);
    res_AndLogicOP_11 = (res_AndLogicOP_11 && Timer_Scaduto(L_P1__GetMainc42(my_id)));
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_AndLogicOP_11);
    bool res_AndLogicOP_14 = true;
    res_AndLogicOP_14 = (res_AndLogicOP_14 && (Counter_GetValore(L_P1__GetMainc44(my_id)) < 15u));
    res_AndLogicOP_14 = (res_AndLogicOP_14 && Timer_Attivo(L_P1__GetMainc42(my_id)));
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_AndLogicOP_14);
    
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_OrLogicOP_10);
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (Counter_GetValore(L_P1__GetMainc44(my_id)) == 122u));
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_NotLogicOP_15);
    
    if(res_OrLogicOP_9){
    
    L_P1__SetOutMainc1(my_id,false);
    }else{
    
    Counter_Res(L_P1__GetMainc44(my_id));
    }
}

/*
    CNL corrispondente:
    
    {  se la macro  MainClass_C1_macrova_M3 ( con argomento_a4   uguale a True ,argomento_a7   uguale a GialloVerde ,argomento_a10   uguale a RossoGialloGiallo ,argomento_a2   uguale a c270x ,argomento_a6   uguale a GialloGiallo  e argomento_a1   uguale a RossoGialloGiallo )   è  diverso da RossoGialloGiallo commento: {40,} ,  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V9 il valore 8 commento: {67,}
    
       
     commento: {36,}  se il timer MainClass_C1_timer_T9 è disattivo, commento: {66,} Assegna al comando MainClass_C1_comando_C4 il valore  True 
    
       
     commento: {37,}  se la variabile MainClass_C1_variabile_V2 è  diverso da  commento: {56,} 6, commento: {69,}Disattiva il timer MainClass_C1_timer_T10
    
     ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V2 il valore 9
    
    
    
    }
*/
void L_P1__Macro1(instance_id_t const my_id )
{
//  se la macro  MainClass_C1_macrova_M3 ( con argomento_a4   uguale a True ,argomento_a7   uguale a GialloVerde ,argomento_a10   uguale a RossoGialloGiallo ,argomento_a2   uguale a c270x ,argomento_a6   uguale a GialloGiallo  e argomento_a1   uguale a RossoGialloGiallo )   è  diverso da RossoGialloGiallo *40,* ,  *67,* Assegna alla variabile MainClass_C1_variabile_V9 il valore 8
    bool res_NotLogicOP_0 = true;
    res_NotLogicOP_0 = (res_NotLogicOP_0 && ! (L_P1__Macro2(my_id,rossogiallo1,rossogiallo1,c270x,true,giallogiall,gialloverde) == rossogiallo1));
    if(res_NotLogicOP_0){
    
    L_P1__SetMainc34(my_id,8u);
    }
    //  *67,*
    //   
    // *36,*  se il timer MainClass_C1_timer_T9 è disattivo, *66,* Assegna al comando MainClass_C1_comando_C4 il valore  True
    if(Timer_Disattivo(L_P1__GetMainc43(my_id))){
    
    L_P1__SetOutMainc1(my_id,true);
    }
    //  *37,*  se la variabile MainClass_C1_variabile_V2 è  diverso da  *56,* 6, *69,*Disattiva il timer MainClass_C1_timer_T10
    // ,altrimenti  *67,* Assegna alla variabile MainClass_C1_variabile_V2 il valore 9
    bool res_NotLogicOP_1 = true;
    res_NotLogicOP_1 = (res_NotLogicOP_1 && ! (L_P1__GetMainc32(my_id) == 6u));
    if(res_NotLogicOP_1){
    
    Timer_Disattiva(L_P1__GetMainc41(my_id));
    }else{
    
    L_P1__SetMainc32(my_id,9u);
    }
}


// Macro di verifica

/*
    CNL corrispondente:
     
    { commento: {61,} commento: {35,}  se il controllo MainClass_C1_controllo_C5 non è  diverso da RossoGialloGiallo commento: {38,} o  se il contatore MainClass_C1_contatore_Co8 non è  uguale a  commento: {53,} 150 commento: {35,} o  se il controllo MainClass_C1_controllo_C3 non è  uguale a RossoGiallo o  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} o  se il parametro MainClass_C1_parametro_P3 è  uguale a  commento: {53,} 9, Tutte le seguenti { 
     commento: {63,}  se il controllo ConsDef è uguale a FALSE  commento: {36,} e  se il timer MainClass_C1_timer_T10 non è scaduto commento: {38,} e  se il contatore MainClass_C1_contatore_Co8 non è  maggiore di  commento: {54,} 1542, Solo una delle seguenti { 
      se la macro  MainClass_C1_macrova_M3 ( con argomento_a4   uguale a True ,argomento_a7   uguale a GialloVerde ,argomento_a10   uguale a c270x ,argomento_a2   uguale a c270x ,argomento_a6   uguale a GialloGiallo  e argomento_a1   uguale a RossoGialloGiallo )   è  uguale a RossoGialloGiallo commento: {40,}  commento: {35,} e  se il controllo MainClass_C1_controllo_C1 è  diverso da  False  commento: {34,} o  se il parametro MainClass_C1_parametro_P3 non è  diverso da  commento: {56,} 6, Verifica che   commento: {50,51,}  commento: {,}  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  commento: {54,} 123
     commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V9 sia  maggiore di  commento: {54,} 7
    
    
     } Verifica che   commento: {47,49,}  commento: {34,}  il parametro MainClass_C1_parametro_P3 sia  diverso da  commento: {56,} 3
     commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T9 sia attivo
    
    
     } Verifica che   commento: {48,50,51,}  commento: {,}  il controllo MainClass_C1_controllo_C8 sia  diverso da  True 
     commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V2 non sia  uguale a  commento: {53,} 10
     commento: {104,} o  che  commento: {,}  il contatore MainClass_C1_contatore_Co8 non sia  maggiore di  commento: {54,} 15150
     commento: {104,} o  che  commento: {37,}  la variabile MainClass_C1_variabile_V4 sia  maggiore di  commento: {54,} 7
    
    
    }
*/
bool L_P1__Macro3(instance_id_t const my_id )
{
bool res_AndLogicOP_0 = true;
    
    //  *61,* *35,*  se il controllo MainClass_C1_controllo_C5 non è  diverso da RossoGialloGiallo *38,* o  se il contatore MainClass_C1_contatore_Co8 non è  uguale a  *53,* 150 *35,* o  se il controllo MainClass_C1_controllo_C3 non è  uguale a RossoGiallo o  se il controllo ConsDef  è  uguale a FALSE  *34,* o  se il parametro MainClass_C1_parametro_P3 è  uguale a  *53,* 9, Tutte le seguenti { 
    //   *63,*  se il controllo ConsDef è uguale a FALSE  *36,* e  se il timer MainClass_C1_timer_T10 non è scaduto *38,* e  se il contatore MainClass_C1_contatore_Co8 non è  maggiore di  *54,* 1542, Solo una delle seguenti { 
    //    se la macro  MainClass_C1_macrova_M3 ( con argomento_a4   uguale a True ,argomento_a7   uguale a GialloVerde ,argomento_a10   uguale a c270x ,argomento_a2   uguale a c270x ,argomento_a6   uguale a GialloGiallo  e argomento_a1   uguale a RossoGialloGiallo )   è  uguale a RossoGialloGiallo *40,*  *35,* e  se il controllo MainClass_C1_controllo_C1 è  diverso da  False  *34,* o  se il parametro MainClass_C1_parametro_P3 non è  diverso da  *56,* 6, Verifica che   *50,51,*  *,*  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  *54,* 123
    //   *104,* e  che  *,*  la variabile MainClass_C1_variabile_V9 sia  maggiore di  *54,* 7
    //   } Verifica che   *47,49,*  *34,*  il parametro MainClass_C1_parametro_P3 sia  diverso da  *56,* 3
    //   *104,* e  che  *,*  il timer MainClass_C1_timer_T9 sia attivo
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_OrLogicOP_4 = false;
    bool res_OrLogicOP_5 = false;
    bool res_NotLogicOP_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetInMainc5(my_id) == rossogiallo1));
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! res_NotLogicOP_7);
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_NotLogicOP_6);
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (Counter_GetValore(L_P1__GetMainc44(my_id)) == 150u));
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_NotLogicOP_8);
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_OrLogicOP_5);
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetInMainc4(my_id) == rossogiallo));
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_NotLogicOP_9);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_OrLogicOP_4);
    res_OrLogicOP_3 = (res_OrLogicOP_3 || (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    res_OrLogicOP_2 = (res_OrLogicOP_2 || (L_P1__GetParamMainc7(my_id) == 9u));
    
    if(res_OrLogicOP_2){
    bool res_AndLogicOP_10 = true;
    bool res_ImpliesLogicOp_11 = true;
    bool res_AndLogicOP_12 = true;
    bool res_AndLogicOP_13 = true;
    res_AndLogicOP_13 = (res_AndLogicOP_13 && (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! Timer_Scaduto(L_P1__GetMainc41(my_id)));
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_NotLogicOP_14);
    
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_AndLogicOP_13);
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (Counter_GetValore(L_P1__GetMainc44(my_id)) > 1542u));
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_NotLogicOP_15);
    
    if(res_AndLogicOP_12){
    bool res_ImpliesLogicOp_16 = true;
    bool res_OrLogicOP_17 = false;
    bool res_AndLogicOP_18 = true;
    res_AndLogicOP_18 = (res_AndLogicOP_18 && (L_P1__Macro2(my_id,rossogiallo1,c270x,c270x,true,giallogiall,gialloverde) == rossogiallo1));
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (L_P1__GetInMainc3(my_id) == false));
    res_AndLogicOP_18 = (res_AndLogicOP_18 && res_NotLogicOP_19);
    
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_AndLogicOP_18);
    bool res_NotLogicOP_20 = true;
    bool res_NotLogicOP_21 = true;
    res_NotLogicOP_21 = (res_NotLogicOP_21 && ! (L_P1__GetParamMainc7(my_id) == 6u));
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! res_NotLogicOP_21);
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_NotLogicOP_20);
    
    if(res_OrLogicOP_17){
    bool res_AndLogicOP_22 = true;
    res_AndLogicOP_22 = (res_AndLogicOP_22 && (Counter_GetValore(L_P1__GetMainc44(my_id)) > 123u));
    res_AndLogicOP_22 = (res_AndLogicOP_22 && (L_P1__GetMainc34(my_id) > 7u));
    
    res_ImpliesLogicOp_16 = (res_ImpliesLogicOp_16 && res_AndLogicOP_22);
    }
    res_ImpliesLogicOp_11 = (res_ImpliesLogicOp_11 && res_ImpliesLogicOp_16);
    }
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_ImpliesLogicOp_11);
    bool res_AndLogicOP_23 = true;
    bool res_NotLogicOP_24 = true;
    res_NotLogicOP_24 = (res_NotLogicOP_24 && ! (L_P1__GetParamMainc7(my_id) == 3u));
    res_AndLogicOP_23 = (res_AndLogicOP_23 && res_NotLogicOP_24);
    res_AndLogicOP_23 = (res_AndLogicOP_23 && Timer_Attivo(L_P1__GetMainc43(my_id)));
    
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_AndLogicOP_23);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_AndLogicOP_10);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *48,50,51,*  *,*  il controllo MainClass_C1_controllo_C8 sia  diverso da  True 
    //   *104,* e  che  *,*  la variabile MainClass_C1_variabile_V2 non sia  uguale a  *53,* 10
    //   *104,* o  che  *,*  il contatore MainClass_C1_contatore_Co8 non sia  maggiore di  *54,* 15150
    //   *104,* o  che  *37,*  la variabile MainClass_C1_variabile_V4 sia  maggiore di  *54,* 7
    bool res_OrLogicOP_25 = false;
    bool res_OrLogicOP_26 = false;
    bool res_AndLogicOP_27 = true;
    bool res_NotLogicOP_28 = true;
    res_NotLogicOP_28 = (res_NotLogicOP_28 && ! (L_P1__GetInMainc6(my_id) == true));
    res_AndLogicOP_27 = (res_AndLogicOP_27 && res_NotLogicOP_28);
    bool res_NotLogicOP_29 = true;
    res_NotLogicOP_29 = (res_NotLogicOP_29 && ! (L_P1__GetMainc32(my_id) == 10u));
    res_AndLogicOP_27 = (res_AndLogicOP_27 && res_NotLogicOP_29);
    
    res_OrLogicOP_26 = (res_OrLogicOP_26 || res_AndLogicOP_27);
    bool res_NotLogicOP_30 = true;
    res_NotLogicOP_30 = (res_NotLogicOP_30 && ! (Counter_GetValore(L_P1__GetMainc44(my_id)) > 15150u));
    res_OrLogicOP_26 = (res_OrLogicOP_26 || res_NotLogicOP_30);
    
    res_OrLogicOP_25 = (res_OrLogicOP_25 || res_OrLogicOP_26);
    res_OrLogicOP_25 = (res_OrLogicOP_25 || (L_P1__GetMainc33(my_id) > 7u));
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_25);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
     
    { commento: {62,}  se il ripristino dello stato  non è  diverso da  commento: {56,}  state1  commento: {107,}, Almeno una delle seguenti { 
     commento: {61,}  se il ripristino dello stato  è  diverso da  commento: {56,}  state1  commento: {107,} commento: {37,} e  se la variabile MainClass_C1_variabile_V9 non è  maggiore di  commento: {54,} 8, Tutte le seguenti { 
     commento: {63,} commento: {34,}  se il parametro MainClass_C1_parametro_P3 è  uguale a  commento: {53,} 8, Solo una delle seguenti { 
     commento: {61,}  se il ripristino dello stato  è  uguale a  commento: {53,}  state1  commento: {107,} commento: {35,} o  se il controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo e  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
     commento: {61,} commento: {34,}  se lo stato  non è  diverso da  commento: {56,}  state1  commento: {106,} commento: {38,} e  se il contatore MainClass_C1_contatore_Co8 è  minore di  commento: {55,} 1242, Tutte le seguenti { 
     commento: {61,} commento: {35,}  se il controllo MainClass_C1_controllo_C8 non è  diverso da  True , Tutte le seguenti { 
      se il controllo ConsDef è uguale a FALSE  commento: {36,} e  se il timer MainClass_C1_timer_T4 è disattivo, Verifica che   commento: {48,49,}   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T9 sia attivo
    
    
     } Verifica che   commento: {47,48,51,}   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} o  che  commento: {,}  il contatore MainClass_C1_contatore_Co8 non sia  minore di  commento: {55,} 13
     commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C3 non sia  diverso da RossoGiallo
     commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P9 sia  maggiore di  commento: {54,} 6
    
    
     } Verifica che   commento: {50,}  commento: {,}  la variabile MainClass_C1_variabile_V9 sia  minore di  commento: {55,} 3
    
    
     } Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C8 sia  uguale a  False 
    
    
     } Verifica che   commento: {47,48,49,50,}  commento: {34,}  il parametro MainClass_C1_parametro_P6 non sia  diverso da c270
     commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V2 sia  diverso da  commento: {56,} 10
     commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T4 sia disattivo
     commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C3 non sia  diverso da RossoGiallo
     commento: {104,} o  che  commento: {35,}  il controllo MainClass_C1_controllo_C8 sia  uguale a  True 
    
    
     } Verifica che   commento: {50,}  commento: {,}  la variabile MainClass_C1_variabile_V9 sia  minore di  commento: {55,} 1
    
    
     } Verifica che   commento: {47,48,}  commento: {34,}  il parametro MainClass_C1_parametro_P3 sia  uguale a  commento: {53,} 2
     commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C3 non sia  uguale a RossoGiallo
    
    
    }
*/
bool L_P1__Macro4(instance_id_t const my_id )
{
bool res_AndLogicOP_0 = true;
    
    //  *62,*  se il ripristino dello stato  non è  diverso da  *56,*  state1  *107,*, Almeno una delle seguenti { 
    //   *61,*  se il ripristino dello stato  è  diverso da  *56,*  state1  *107,* *37,* e  se la variabile MainClass_C1_variabile_V9 non è  maggiore di  *54,* 8, Tutte le seguenti { 
    //   *63,* *34,*  se il parametro MainClass_C1_parametro_P3 è  uguale a  *53,* 8, Solo una delle seguenti { 
    //   *61,*  se il ripristino dello stato  è  uguale a  *53,*  state1  *107,* *35,* o  se il controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo e  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
    //   *61,* *34,*  se lo stato  non è  diverso da  *56,*  state1  *106,* *38,* e  se il contatore MainClass_C1_contatore_Co8 è  minore di  *55,* 1242, Tutte le seguenti { 
    //   *61,* *35,*  se il controllo MainClass_C1_controllo_C8 non è  diverso da  True , Tutte le seguenti { 
    //    se il controllo ConsDef è uguale a FALSE  *36,* e  se il timer MainClass_C1_timer_T4 è disattivo, Verifica che   *48,49,*   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* o  che  *,*  il timer MainClass_C1_timer_T9 sia attivo
    //   } Verifica che   *47,48,51,*   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* o  che  *,*  il contatore MainClass_C1_contatore_Co8 non sia  minore di  *55,* 13
    //   *104,* o  che  *,*  il controllo MainClass_C1_controllo_C3 non sia  diverso da RossoGiallo
    //   *104,* e  che  *34,*  il parametro MainClass_C1_parametro_P9 sia  maggiore di  *54,* 6
    //   } Verifica che   *50,*  *,*  la variabile MainClass_C1_variabile_V9 sia  minore di  *55,* 3
    //   } Verifica che   *48,*   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* o  che  *,*  il controllo MainClass_C1_controllo_C8 sia  uguale a  False 
    //   } Verifica che   *47,48,49,50,*  *34,*  il parametro MainClass_C1_parametro_P6 non sia  diverso da c270
    //   *104,* e  che  *,*  la variabile MainClass_C1_variabile_V2 sia  diverso da  *56,* 10
    //   *104,* e  che   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* e  che  *,*  il timer MainClass_C1_timer_T4 sia disattivo
    //   *104,* e  che  *,*  il controllo MainClass_C1_controllo_C3 non sia  diverso da RossoGiallo
    //   *104,* o  che  *35,*  il controllo MainClass_C1_controllo_C8 sia  uguale a  True 
    //   } Verifica che   *50,*  *,*  la variabile MainClass_C1_variabile_V9 sia  minore di  *55,* 1
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_NotLogicOP_2 = true;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__GetStato1(my_id) == C1_St_state));
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! res_NotLogicOP_3);
    if(res_NotLogicOP_2){
    bool res_OrLogicOP_4 = false;
    bool res_ImpliesLogicOp_5 = true;
    bool res_AndLogicOP_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetStato1(my_id) == C1_St_state));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_7);
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetMainc34(my_id) > 8u));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_8);
    
    if(res_AndLogicOP_6){
    bool res_AndLogicOP_9 = true;
    bool res_ImpliesLogicOp_10 = true;
    if((L_P1__GetParamMainc7(my_id) == 8u)){
    bool res_XorLogicOP_11 = true;
    int xorIndex_res_XorLogicOP_11 = 0;
    bool res_ImpliesLogicOp_12 = true;
    bool res_OrLogicOP_13 = false;
    res_OrLogicOP_13 = (res_OrLogicOP_13 || (L_P1__GetStato1(my_id) == C1_St_state));
    bool res_AndLogicOP_14 = true;
    res_AndLogicOP_14 = (res_AndLogicOP_14 && (L_P1__GetInMainc4(my_id) == rossogiallo));
    res_AndLogicOP_14 = (res_AndLogicOP_14 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_AndLogicOP_14);
    
    if(res_OrLogicOP_13){
    bool res_AndLogicOP_15 = true;
    bool res_ImpliesLogicOp_16 = true;
    bool res_AndLogicOP_17 = true;
    bool res_NotLogicOP_18 = true;
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (L_P1_C1_GetState(my_id) == C1_St_state));
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! res_NotLogicOP_19);
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_NotLogicOP_18);
    res_AndLogicOP_17 = (res_AndLogicOP_17 && (Counter_GetValore(L_P1__GetMainc44(my_id)) < 1242u));
    
    if(res_AndLogicOP_17){
    bool res_AndLogicOP_20 = true;
    bool res_ImpliesLogicOp_21 = true;
    bool res_NotLogicOP_22 = true;
    bool res_NotLogicOP_23 = true;
    res_NotLogicOP_23 = (res_NotLogicOP_23 && ! (L_P1__GetInMainc6(my_id) == true));
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! res_NotLogicOP_23);
    if(res_NotLogicOP_22){
    bool res_ImpliesLogicOp_24 = true;
    bool res_AndLogicOP_25 = true;
    res_AndLogicOP_25 = (res_AndLogicOP_25 && (L_P1__GetInConsd(my_id) == false));
    res_AndLogicOP_25 = (res_AndLogicOP_25 && Timer_Disattivo(L_P1__GetMainc42(my_id)));
    
    if(res_AndLogicOP_25){
    bool res_OrLogicOP_26 = false;
    res_OrLogicOP_26 = (res_OrLogicOP_26 || (L_P1__GetInConsd(my_id) == false));
    res_OrLogicOP_26 = (res_OrLogicOP_26 || Timer_Attivo(L_P1__GetMainc43(my_id)));
    
    res_ImpliesLogicOp_24 = (res_ImpliesLogicOp_24 && res_OrLogicOP_26);
    }
    res_ImpliesLogicOp_21 = (res_ImpliesLogicOp_21 && res_ImpliesLogicOp_24);
    }
    res_AndLogicOP_20 = (res_AndLogicOP_20 && res_ImpliesLogicOp_21);
    bool res_OrLogicOP_27 = false;
    bool res_OrLogicOP_28 = false;
    res_OrLogicOP_28 = (res_OrLogicOP_28 || (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_29 = true;
    res_NotLogicOP_29 = (res_NotLogicOP_29 && ! (Counter_GetValore(L_P1__GetMainc44(my_id)) < 13u));
    res_OrLogicOP_28 = (res_OrLogicOP_28 || res_NotLogicOP_29);
    
    res_OrLogicOP_27 = (res_OrLogicOP_27 || res_OrLogicOP_28);
    bool res_AndLogicOP_30 = true;
    bool res_NotLogicOP_31 = true;
    bool res_NotLogicOP_32 = true;
    res_NotLogicOP_32 = (res_NotLogicOP_32 && ! (L_P1__GetInMainc4(my_id) == rossogiallo));
    res_NotLogicOP_31 = (res_NotLogicOP_31 && ! res_NotLogicOP_32);
    res_AndLogicOP_30 = (res_AndLogicOP_30 && res_NotLogicOP_31);
    res_AndLogicOP_30 = (res_AndLogicOP_30 && (L_P1__GetParamMainc9(my_id) > 6u));
    
    res_OrLogicOP_27 = (res_OrLogicOP_27 || res_AndLogicOP_30);
    
    res_AndLogicOP_20 = (res_AndLogicOP_20 && res_OrLogicOP_27);
    
    res_ImpliesLogicOp_16 = (res_ImpliesLogicOp_16 && res_AndLogicOP_20);
    }
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_ImpliesLogicOp_16);
    res_AndLogicOP_15 = (res_AndLogicOP_15 && (L_P1__GetMainc34(my_id) < 3u));
    
    res_ImpliesLogicOp_12 = (res_ImpliesLogicOp_12 && res_AndLogicOP_15);
    }
    if(res_ImpliesLogicOp_12){
    xorIndex_res_XorLogicOP_11 = (xorIndex_res_XorLogicOP_11 + 1);
    }
    bool res_OrLogicOP_33 = false;
    res_OrLogicOP_33 = (res_OrLogicOP_33 || (L_P1__GetInConsd(my_id) == false));
    res_OrLogicOP_33 = (res_OrLogicOP_33 || (L_P1__GetInMainc6(my_id) == false));
    
    if(res_OrLogicOP_33){
    xorIndex_res_XorLogicOP_11 = (xorIndex_res_XorLogicOP_11 + 1);
    }
    
    res_XorLogicOP_11 = (res_XorLogicOP_11 && (xorIndex_res_XorLogicOP_11 == 1));
    res_ImpliesLogicOp_10 = (res_ImpliesLogicOp_10 && res_XorLogicOP_11);
    }
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_ImpliesLogicOp_10);
    bool res_OrLogicOP_34 = false;
    bool res_AndLogicOP_35 = true;
    bool res_AndLogicOP_36 = true;
    bool res_AndLogicOP_37 = true;
    bool res_AndLogicOP_38 = true;
    bool res_NotLogicOP_39 = true;
    bool res_NotLogicOP_40 = true;
    res_NotLogicOP_40 = (res_NotLogicOP_40 && ! (L_P1__GetParamMainc8(my_id) == c270));
    res_NotLogicOP_39 = (res_NotLogicOP_39 && ! res_NotLogicOP_40);
    res_AndLogicOP_38 = (res_AndLogicOP_38 && res_NotLogicOP_39);
    bool res_NotLogicOP_41 = true;
    res_NotLogicOP_41 = (res_NotLogicOP_41 && ! (L_P1__GetMainc32(my_id) == 10u));
    res_AndLogicOP_38 = (res_AndLogicOP_38 && res_NotLogicOP_41);
    
    res_AndLogicOP_37 = (res_AndLogicOP_37 && res_AndLogicOP_38);
    res_AndLogicOP_37 = (res_AndLogicOP_37 && (L_P1__GetInConsd(my_id) == false));
    
    res_AndLogicOP_36 = (res_AndLogicOP_36 && res_AndLogicOP_37);
    res_AndLogicOP_36 = (res_AndLogicOP_36 && Timer_Disattivo(L_P1__GetMainc42(my_id)));
    
    res_AndLogicOP_35 = (res_AndLogicOP_35 && res_AndLogicOP_36);
    bool res_NotLogicOP_42 = true;
    bool res_NotLogicOP_43 = true;
    res_NotLogicOP_43 = (res_NotLogicOP_43 && ! (L_P1__GetInMainc4(my_id) == rossogiallo));
    res_NotLogicOP_42 = (res_NotLogicOP_42 && ! res_NotLogicOP_43);
    res_AndLogicOP_35 = (res_AndLogicOP_35 && res_NotLogicOP_42);
    
    res_OrLogicOP_34 = (res_OrLogicOP_34 || res_AndLogicOP_35);
    res_OrLogicOP_34 = (res_OrLogicOP_34 || (L_P1__GetInMainc6(my_id) == true));
    
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_OrLogicOP_34);
    
    res_ImpliesLogicOp_5 = (res_ImpliesLogicOp_5 && res_AndLogicOP_9);
    }
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_ImpliesLogicOp_5);
    res_OrLogicOP_4 = (res_OrLogicOP_4 || (L_P1__GetMainc34(my_id) < 1u));
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_OrLogicOP_4);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *47,48,*  *34,*  il parametro MainClass_C1_parametro_P3 sia  uguale a  *53,* 2
    //   *104,* o  che  *,*  il controllo MainClass_C1_controllo_C3 non sia  uguale a RossoGiallo
    bool res_OrLogicOP_44 = false;
    res_OrLogicOP_44 = (res_OrLogicOP_44 || (L_P1__GetParamMainc7(my_id) == 2u));
    bool res_NotLogicOP_45 = true;
    res_NotLogicOP_45 = (res_NotLogicOP_45 && ! (L_P1__GetInMainc4(my_id) == rossogiallo));
    res_OrLogicOP_44 = (res_OrLogicOP_44 || res_NotLogicOP_45);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_44);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
    
    { commento: {63,} commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI2 è attivo commento: {38,} e  se il contatore MainClass_C1_contatore_Co8 è  uguale a  commento: {53,} 14150, Solo una delle seguenti { 
     commento: {62,}  se la macro  MainClass_C1_macrova_M3 ( con argomento_a4   uguale a True ,argomento_a7   uguale a GialloVerde ,argomento_a10   uguale a c270x ,argomento_a2   uguale a c270x ,argomento_a6   uguale a RossoGiallo  e argomento_a1   uguale a c270x )   è  diverso da RossoGialloGiallo commento: {40,}  commento: {34,} o  se il parametro MainClass_C1_parametro_P6 è  uguale a c270 o  se l'argomento argomento_ave8 non  è  diverso da GialloVerde commento: {39,}  e  se l'argomento argomento_ave3 non  è  uguale a  True  commento: {39,} , Almeno una delle seguenti { 
     commento: {62,} commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV2 non è  diverso da RossoGialloGiallo commento: {38,} e  se il contatore MainClass_C1_contatore_Co8 non è  minore di  commento: {55,} 12 o  se l'argomento argomento_ave8 non  è  diverso da GialloVerde commento: {39,}  commento: {34,} e  se il parametro MainClass_C1_parametro_P3 è  diverso da  commento: {56,} 4 commento: {36,} o  se il timer MainClass_C1_timer_T9 non è disattivo, Almeno una delle seguenti { 
     commento: {61,}  se il ripristino dello stato  non è  uguale a  commento: {53,}  state1  commento: {107,} commento: {34,} o  se il parametro MainClass_C1_parametro_P3 non è  minore di  commento: {55,} 7 commento: {36,} o  se il timer MainClass_C1_timer_T9 è attivo commento: {35,} o  se il controllo MainClass_C1_controllo_C8 non è  uguale a  True  commento: {34,} e  se il parametro MainClass_C1_parametro_P6 è  uguale a c270 commento: {35,} e  se il controllo MainClass_C1_controllo_C3 non è  diverso da RossoGiallo, Tutte le seguenti { 
     commento: {37,}  se la variabile MainClass_C1_variabile_V9 è  uguale a  commento: {53,} 1 commento: {38,} e  se il contatore MainClass_C1_contatore_Co8 è  minore di  commento: {55,} 11423 commento: {37,} e  se la variabile MainClass_C1_variabile_V4 non è  minore di  commento: {55,} 5 commento: {37,} o  se la variabile MainClass_C1_variabile_V4 è  minore di  commento: {55,} 2 commento: {36,} e  se il timer MainClass_C1_timer_T10 non è attivo, Verifica che   commento: {50,51,}  commento: {,}  la variabile MainClass_C1_variabile_V2 sia  maggiore di  commento: {54,} 6
     commento: {104,} o  che  commento: {,}  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  commento: {54,} 121
     commento: {104,} e  che  commento: {37,}  la variabile MainClass_C1_variabile_V4 non sia  uguale a  commento: {53,} 6
     commento: {104,} e  che  commento: {37,}  la variabile MainClass_C1_variabile_V2 sia  minore di  commento: {55,} 2
     commento: {104,} e  che  commento: {37,}  la variabile MainClass_C1_variabile_V2 sia  uguale a  commento: {53,} 5
    
    
     } Verifica che   commento: {49,51,52,}  commento: {,}  il contatore MainClass_C1_contatore_Co8 sia  diverso da  commento: {56,} 115
     commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T4 sia scaduto
     commento: {104,} o  che   l'argomento argomento_ave3 sia  uguale a  False  commento: {,} 
    
    
     } Verifica che   commento: {47,48,49,50,51,52,}  commento: {,}  il contatore MainClass_C1_contatore_Co8 sia  uguale a  commento: {53,} 150
     commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V2 non sia  diverso da  commento: {56,} 9
     commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C8 non sia  diverso da  True 
     commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P9 non sia  uguale a  commento: {53,} 3
     commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T4 sia scaduto
     commento: {104,} o  che   l'argomento argomento_ave3 non  sia  diverso da  False  commento: {,} 
    
    
     } Verifica che   commento: {47,48,50,52,}  commento: {34,}  il parametro MainClass_C1_parametro_P6 non sia  uguale a c270
     commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C8 non sia  diverso da  False 
     commento: {104,} o  che   l'argomento argomento_ave3 sia  diverso da  False  commento: {,} 
     commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V2 sia  maggiore di  commento: {54,} 1
    
    
     } Verifica che   commento: {48,49,50,51,52,}  commento: {,}  il timer MainClass_C1_timer_T10 non sia attivo
     commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V9 non sia  diverso da  commento: {56,} 6
     commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co8 sia  diverso da  commento: {56,} 115
     commento: {104,} o  che  commento: {36,}  il timer MainClass_C1_timer_T10 sia scaduto
     commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C5 non sia  uguale a RossoGialloGiallo
     commento: {104,} e  che   l'argomento argomento_ave4 non  sia  diverso da RossoGiallo commento: {,} 
    
    
    }
*/
bool L_P1__Macro5(instance_id_t const my_id , bool argom8, C1_Enumerat1 argom9, C1_Enumerat2 argom10, C1_Enumerat2 argom11)
{
bool res_AndLogicOP_0 = true;
    
    //  *63,* *110,*  se il ripristino del timer  MainClass_C1_restoreTI_TI2 è attivo *38,* e  se il contatore MainClass_C1_contatore_Co8 è  uguale a  *53,* 14150, Solo una delle seguenti { 
    //   *62,*  se la macro  MainClass_C1_macrova_M3 ( con argomento_a4   uguale a True ,argomento_a7   uguale a GialloVerde ,argomento_a10   uguale a c270x ,argomento_a2   uguale a c270x ,argomento_a6   uguale a RossoGiallo  e argomento_a1   uguale a c270x )   è  diverso da RossoGialloGiallo *40,*  *34,* o  se il parametro MainClass_C1_parametro_P6 è  uguale a c270 o  se l'argomento argomento_ave8 non  è  diverso da GialloVerde *39,*  e  se l'argomento argomento_ave3 non  è  uguale a  True  *39,* , Almeno una delle seguenti { 
    //   *62,* *109,*  se il ripristino della variabile  MainClass_C1_restoreva_RV2 non è  diverso da RossoGialloGiallo *38,* e  se il contatore MainClass_C1_contatore_Co8 non è  minore di  *55,* 12 o  se l'argomento argomento_ave8 non  è  diverso da GialloVerde *39,*  *34,* e  se il parametro MainClass_C1_parametro_P3 è  diverso da  *56,* 4 *36,* o  se il timer MainClass_C1_timer_T9 non è disattivo, Almeno una delle seguenti { 
    //   *61,*  se il ripristino dello stato  non è  uguale a  *53,*  state1  *107,* *34,* o  se il parametro MainClass_C1_parametro_P3 non è  minore di  *55,* 7 *36,* o  se il timer MainClass_C1_timer_T9 è attivo *35,* o  se il controllo MainClass_C1_controllo_C8 non è  uguale a  True  *34,* e  se il parametro MainClass_C1_parametro_P6 è  uguale a c270 *35,* e  se il controllo MainClass_C1_controllo_C3 non è  diverso da RossoGiallo, Tutte le seguenti { 
    //   *37,*  se la variabile MainClass_C1_variabile_V9 è  uguale a  *53,* 1 *38,* e  se il contatore MainClass_C1_contatore_Co8 è  minore di  *55,* 11423 *37,* e  se la variabile MainClass_C1_variabile_V4 non è  minore di  *55,* 5 *37,* o  se la variabile MainClass_C1_variabile_V4 è  minore di  *55,* 2 *36,* e  se il timer MainClass_C1_timer_T10 non è attivo, Verifica che   *50,51,*  *,*  la variabile MainClass_C1_variabile_V2 sia  maggiore di  *54,* 6
    //   *104,* o  che  *,*  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  *54,* 121
    //   *104,* e  che  *37,*  la variabile MainClass_C1_variabile_V4 non sia  uguale a  *53,* 6
    //   *104,* e  che  *37,*  la variabile MainClass_C1_variabile_V2 sia  minore di  *55,* 2
    //   *104,* e  che  *37,*  la variabile MainClass_C1_variabile_V2 sia  uguale a  *53,* 5
    //   } Verifica che   *49,51,52,*  *,*  il contatore MainClass_C1_contatore_Co8 sia  diverso da  *56,* 115
    //   *104,* e  che  *,*  il timer MainClass_C1_timer_T4 sia scaduto
    //   *104,* o  che   l'argomento argomento_ave3 sia  uguale a  False  *,* 
    //   } Verifica che   *47,48,49,50,51,52,*  *,*  il contatore MainClass_C1_contatore_Co8 sia  uguale a  *53,* 150
    //   *104,* e  che  *,*  la variabile MainClass_C1_variabile_V2 non sia  diverso da  *56,* 9
    //   *104,* o  che  *,*  il controllo MainClass_C1_controllo_C8 non sia  diverso da  True 
    //   *104,* e  che  *34,*  il parametro MainClass_C1_parametro_P9 non sia  uguale a  *53,* 3
    //   *104,* e  che  *,*  il timer MainClass_C1_timer_T4 sia scaduto
    //   *104,* o  che   l'argomento argomento_ave3 non  sia  diverso da  False  *,* 
    //   } Verifica che   *47,48,50,52,*  *34,*  il parametro MainClass_C1_parametro_P6 non sia  uguale a c270
    //   *104,* o  che  *,*  il controllo MainClass_C1_controllo_C8 non sia  diverso da  False 
    //   *104,* o  che   l'argomento argomento_ave3 sia  diverso da  False  *,* 
    //   *104,* o  che  *,*  la variabile MainClass_C1_variabile_V2 sia  maggiore di  *54,* 1
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_AndLogicOP_2 = true;
    res_AndLogicOP_2 = (res_AndLogicOP_2 && Timer_Attivo(L_P1__GetMainc38(my_id)));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && (Counter_GetValore(L_P1__GetMainc44(my_id)) == 14150u));
    
    if(res_AndLogicOP_2){
    bool res_XorLogicOP_3 = true;
    int xorIndex_res_XorLogicOP_3 = 0;
    bool res_ImpliesLogicOp_4 = true;
    bool res_OrLogicOP_5 = false;
    bool res_OrLogicOP_6 = false;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__Macro2(my_id,c270x,c270x,c270x,true,rossogiallo,gialloverde) == rossogiallo1));
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_NotLogicOP_7);
    res_OrLogicOP_6 = (res_OrLogicOP_6 || (L_P1__GetParamMainc8(my_id) == c270));
    
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_OrLogicOP_6);
    bool res_AndLogicOP_8 = true;
    bool res_NotLogicOP_9 = true;
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (argom11 == gialloverde));
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! res_NotLogicOP_10);
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_9);
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (argom8 == true));
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_11);
    
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_AndLogicOP_8);
    
    if(res_OrLogicOP_5){
    bool res_OrLogicOP_12 = false;
    bool res_ImpliesLogicOp_13 = true;
    bool res_OrLogicOP_14 = false;
    bool res_OrLogicOP_15 = false;
    bool res_AndLogicOP_16 = true;
    bool res_NotLogicOP_17 = true;
    bool res_NotLogicOP_18 = true;
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! (L_P1__GetMainc31(my_id) == rossogiallo1));
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! res_NotLogicOP_18);
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_NotLogicOP_17);
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (Counter_GetValore(L_P1__GetMainc44(my_id)) < 12u));
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_NotLogicOP_19);
    
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_AndLogicOP_16);
    bool res_AndLogicOP_20 = true;
    bool res_NotLogicOP_21 = true;
    bool res_NotLogicOP_22 = true;
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! (argom11 == gialloverde));
    res_NotLogicOP_21 = (res_NotLogicOP_21 && ! res_NotLogicOP_22);
    res_AndLogicOP_20 = (res_AndLogicOP_20 && res_NotLogicOP_21);
    bool res_NotLogicOP_23 = true;
    res_NotLogicOP_23 = (res_NotLogicOP_23 && ! (L_P1__GetParamMainc7(my_id) == 4u));
    res_AndLogicOP_20 = (res_AndLogicOP_20 && res_NotLogicOP_23);
    
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_AndLogicOP_20);
    
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_OrLogicOP_15);
    bool res_NotLogicOP_24 = true;
    res_NotLogicOP_24 = (res_NotLogicOP_24 && ! Timer_Disattivo(L_P1__GetMainc43(my_id)));
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_NotLogicOP_24);
    
    if(res_OrLogicOP_14){
    bool res_OrLogicOP_25 = false;
    bool res_ImpliesLogicOp_26 = true;
    bool res_OrLogicOP_27 = false;
    bool res_OrLogicOP_28 = false;
    bool res_OrLogicOP_29 = false;
    bool res_NotLogicOP_30 = true;
    res_NotLogicOP_30 = (res_NotLogicOP_30 && ! (L_P1__GetStato1(my_id) == C1_St_state));
    res_OrLogicOP_29 = (res_OrLogicOP_29 || res_NotLogicOP_30);
    bool res_NotLogicOP_31 = true;
    res_NotLogicOP_31 = (res_NotLogicOP_31 && ! (L_P1__GetParamMainc7(my_id) < 7u));
    res_OrLogicOP_29 = (res_OrLogicOP_29 || res_NotLogicOP_31);
    
    res_OrLogicOP_28 = (res_OrLogicOP_28 || res_OrLogicOP_29);
    res_OrLogicOP_28 = (res_OrLogicOP_28 || Timer_Attivo(L_P1__GetMainc43(my_id)));
    
    res_OrLogicOP_27 = (res_OrLogicOP_27 || res_OrLogicOP_28);
    bool res_AndLogicOP_32 = true;
    bool res_AndLogicOP_33 = true;
    bool res_NotLogicOP_34 = true;
    res_NotLogicOP_34 = (res_NotLogicOP_34 && ! (L_P1__GetInMainc6(my_id) == true));
    res_AndLogicOP_33 = (res_AndLogicOP_33 && res_NotLogicOP_34);
    res_AndLogicOP_33 = (res_AndLogicOP_33 && (L_P1__GetParamMainc8(my_id) == c270));
    
    res_AndLogicOP_32 = (res_AndLogicOP_32 && res_AndLogicOP_33);
    bool res_NotLogicOP_35 = true;
    bool res_NotLogicOP_36 = true;
    res_NotLogicOP_36 = (res_NotLogicOP_36 && ! (L_P1__GetInMainc4(my_id) == rossogiallo));
    res_NotLogicOP_35 = (res_NotLogicOP_35 && ! res_NotLogicOP_36);
    res_AndLogicOP_32 = (res_AndLogicOP_32 && res_NotLogicOP_35);
    
    res_OrLogicOP_27 = (res_OrLogicOP_27 || res_AndLogicOP_32);
    
    if(res_OrLogicOP_27){
    bool res_ImpliesLogicOp_37 = true;
    bool res_OrLogicOP_38 = false;
    bool res_AndLogicOP_39 = true;
    bool res_AndLogicOP_40 = true;
    res_AndLogicOP_40 = (res_AndLogicOP_40 && (L_P1__GetMainc34(my_id) == 1u));
    res_AndLogicOP_40 = (res_AndLogicOP_40 && (Counter_GetValore(L_P1__GetMainc44(my_id)) < 11423u));
    
    res_AndLogicOP_39 = (res_AndLogicOP_39 && res_AndLogicOP_40);
    bool res_NotLogicOP_41 = true;
    res_NotLogicOP_41 = (res_NotLogicOP_41 && ! (L_P1__GetMainc33(my_id) < 5u));
    res_AndLogicOP_39 = (res_AndLogicOP_39 && res_NotLogicOP_41);
    
    res_OrLogicOP_38 = (res_OrLogicOP_38 || res_AndLogicOP_39);
    bool res_AndLogicOP_42 = true;
    res_AndLogicOP_42 = (res_AndLogicOP_42 && (L_P1__GetMainc33(my_id) < 2u));
    bool res_NotLogicOP_43 = true;
    res_NotLogicOP_43 = (res_NotLogicOP_43 && ! Timer_Attivo(L_P1__GetMainc41(my_id)));
    res_AndLogicOP_42 = (res_AndLogicOP_42 && res_NotLogicOP_43);
    
    res_OrLogicOP_38 = (res_OrLogicOP_38 || res_AndLogicOP_42);
    
    if(res_OrLogicOP_38){
    bool res_OrLogicOP_44 = false;
    res_OrLogicOP_44 = (res_OrLogicOP_44 || (L_P1__GetMainc32(my_id) > 6u));
    bool res_AndLogicOP_45 = true;
    bool res_AndLogicOP_46 = true;
    bool res_AndLogicOP_47 = true;
    res_AndLogicOP_47 = (res_AndLogicOP_47 && (Counter_GetValore(L_P1__GetMainc44(my_id)) > 121u));
    bool res_NotLogicOP_48 = true;
    res_NotLogicOP_48 = (res_NotLogicOP_48 && ! (L_P1__GetMainc33(my_id) == 6u));
    res_AndLogicOP_47 = (res_AndLogicOP_47 && res_NotLogicOP_48);
    
    res_AndLogicOP_46 = (res_AndLogicOP_46 && res_AndLogicOP_47);
    res_AndLogicOP_46 = (res_AndLogicOP_46 && (L_P1__GetMainc32(my_id) < 2u));
    
    res_AndLogicOP_45 = (res_AndLogicOP_45 && res_AndLogicOP_46);
    res_AndLogicOP_45 = (res_AndLogicOP_45 && (L_P1__GetMainc32(my_id) == 5u));
    
    res_OrLogicOP_44 = (res_OrLogicOP_44 || res_AndLogicOP_45);
    
    res_ImpliesLogicOp_37 = (res_ImpliesLogicOp_37 && res_OrLogicOP_44);
    }
    res_ImpliesLogicOp_26 = (res_ImpliesLogicOp_26 && res_ImpliesLogicOp_37);
    }
    res_OrLogicOP_25 = (res_OrLogicOP_25 || res_ImpliesLogicOp_26);
    bool res_OrLogicOP_49 = false;
    bool res_AndLogicOP_50 = true;
    bool res_NotLogicOP_51 = true;
    res_NotLogicOP_51 = (res_NotLogicOP_51 && ! (Counter_GetValore(L_P1__GetMainc44(my_id)) == 115u));
    res_AndLogicOP_50 = (res_AndLogicOP_50 && res_NotLogicOP_51);
    res_AndLogicOP_50 = (res_AndLogicOP_50 && Timer_Scaduto(L_P1__GetMainc42(my_id)));
    
    res_OrLogicOP_49 = (res_OrLogicOP_49 || res_AndLogicOP_50);
    res_OrLogicOP_49 = (res_OrLogicOP_49 || (argom8 == false));
    
    res_OrLogicOP_25 = (res_OrLogicOP_25 || res_OrLogicOP_49);
    
    res_ImpliesLogicOp_13 = (res_ImpliesLogicOp_13 && res_OrLogicOP_25);
    }
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_ImpliesLogicOp_13);
    bool res_OrLogicOP_52 = false;
    bool res_OrLogicOP_53 = false;
    bool res_AndLogicOP_54 = true;
    res_AndLogicOP_54 = (res_AndLogicOP_54 && (Counter_GetValore(L_P1__GetMainc44(my_id)) == 150u));
    bool res_NotLogicOP_55 = true;
    bool res_NotLogicOP_56 = true;
    res_NotLogicOP_56 = (res_NotLogicOP_56 && ! (L_P1__GetMainc32(my_id) == 9u));
    res_NotLogicOP_55 = (res_NotLogicOP_55 && ! res_NotLogicOP_56);
    res_AndLogicOP_54 = (res_AndLogicOP_54 && res_NotLogicOP_55);
    
    res_OrLogicOP_53 = (res_OrLogicOP_53 || res_AndLogicOP_54);
    bool res_AndLogicOP_57 = true;
    bool res_AndLogicOP_58 = true;
    bool res_NotLogicOP_59 = true;
    bool res_NotLogicOP_60 = true;
    res_NotLogicOP_60 = (res_NotLogicOP_60 && ! (L_P1__GetInMainc6(my_id) == true));
    res_NotLogicOP_59 = (res_NotLogicOP_59 && ! res_NotLogicOP_60);
    res_AndLogicOP_58 = (res_AndLogicOP_58 && res_NotLogicOP_59);
    bool res_NotLogicOP_61 = true;
    res_NotLogicOP_61 = (res_NotLogicOP_61 && ! (L_P1__GetParamMainc9(my_id) == 3u));
    res_AndLogicOP_58 = (res_AndLogicOP_58 && res_NotLogicOP_61);
    
    res_AndLogicOP_57 = (res_AndLogicOP_57 && res_AndLogicOP_58);
    res_AndLogicOP_57 = (res_AndLogicOP_57 && Timer_Scaduto(L_P1__GetMainc42(my_id)));
    
    res_OrLogicOP_53 = (res_OrLogicOP_53 || res_AndLogicOP_57);
    
    res_OrLogicOP_52 = (res_OrLogicOP_52 || res_OrLogicOP_53);
    bool res_NotLogicOP_62 = true;
    bool res_NotLogicOP_63 = true;
    res_NotLogicOP_63 = (res_NotLogicOP_63 && ! (argom8 == false));
    res_NotLogicOP_62 = (res_NotLogicOP_62 && ! res_NotLogicOP_63);
    res_OrLogicOP_52 = (res_OrLogicOP_52 || res_NotLogicOP_62);
    
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_OrLogicOP_52);
    
    res_ImpliesLogicOp_4 = (res_ImpliesLogicOp_4 && res_OrLogicOP_12);
    }
    if(res_ImpliesLogicOp_4){
    xorIndex_res_XorLogicOP_3 = (xorIndex_res_XorLogicOP_3 + 1);
    }
    bool res_OrLogicOP_64 = false;
    bool res_OrLogicOP_65 = false;
    bool res_OrLogicOP_66 = false;
    bool res_NotLogicOP_67 = true;
    res_NotLogicOP_67 = (res_NotLogicOP_67 && ! (L_P1__GetParamMainc8(my_id) == c270));
    res_OrLogicOP_66 = (res_OrLogicOP_66 || res_NotLogicOP_67);
    bool res_NotLogicOP_68 = true;
    bool res_NotLogicOP_69 = true;
    res_NotLogicOP_69 = (res_NotLogicOP_69 && ! (L_P1__GetInMainc6(my_id) == false));
    res_NotLogicOP_68 = (res_NotLogicOP_68 && ! res_NotLogicOP_69);
    res_OrLogicOP_66 = (res_OrLogicOP_66 || res_NotLogicOP_68);
    
    res_OrLogicOP_65 = (res_OrLogicOP_65 || res_OrLogicOP_66);
    bool res_NotLogicOP_70 = true;
    res_NotLogicOP_70 = (res_NotLogicOP_70 && ! (argom8 == false));
    res_OrLogicOP_65 = (res_OrLogicOP_65 || res_NotLogicOP_70);
    
    res_OrLogicOP_64 = (res_OrLogicOP_64 || res_OrLogicOP_65);
    res_OrLogicOP_64 = (res_OrLogicOP_64 || (L_P1__GetMainc32(my_id) > 1u));
    
    if(res_OrLogicOP_64){
    xorIndex_res_XorLogicOP_3 = (xorIndex_res_XorLogicOP_3 + 1);
    }
    
    res_XorLogicOP_3 = (res_XorLogicOP_3 && (xorIndex_res_XorLogicOP_3 == 1));
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_XorLogicOP_3);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *48,49,50,51,52,*  *,*  il timer MainClass_C1_timer_T10 non sia attivo
    //   *104,* e  che  *,*  la variabile MainClass_C1_variabile_V9 non sia  diverso da  *56,* 6
    //   *104,* e  che  *,*  il contatore MainClass_C1_contatore_Co8 sia  diverso da  *56,* 115
    //   *104,* o  che  *36,*  il timer MainClass_C1_timer_T10 sia scaduto
    //   *104,* e  che  *,*  il controllo MainClass_C1_controllo_C5 non sia  uguale a RossoGialloGiallo
    //   *104,* e  che   l'argomento argomento_ave4 non  sia  diverso da RossoGiallo
    bool res_OrLogicOP_71 = false;
    bool res_AndLogicOP_72 = true;
    bool res_AndLogicOP_73 = true;
    bool res_NotLogicOP_74 = true;
    res_NotLogicOP_74 = (res_NotLogicOP_74 && ! Timer_Attivo(L_P1__GetMainc41(my_id)));
    res_AndLogicOP_73 = (res_AndLogicOP_73 && res_NotLogicOP_74);
    bool res_NotLogicOP_75 = true;
    bool res_NotLogicOP_76 = true;
    res_NotLogicOP_76 = (res_NotLogicOP_76 && ! (L_P1__GetMainc34(my_id) == 6u));
    res_NotLogicOP_75 = (res_NotLogicOP_75 && ! res_NotLogicOP_76);
    res_AndLogicOP_73 = (res_AndLogicOP_73 && res_NotLogicOP_75);
    
    res_AndLogicOP_72 = (res_AndLogicOP_72 && res_AndLogicOP_73);
    bool res_NotLogicOP_77 = true;
    res_NotLogicOP_77 = (res_NotLogicOP_77 && ! (Counter_GetValore(L_P1__GetMainc44(my_id)) == 115u));
    res_AndLogicOP_72 = (res_AndLogicOP_72 && res_NotLogicOP_77);
    
    res_OrLogicOP_71 = (res_OrLogicOP_71 || res_AndLogicOP_72);
    bool res_AndLogicOP_78 = true;
    bool res_AndLogicOP_79 = true;
    res_AndLogicOP_79 = (res_AndLogicOP_79 && Timer_Scaduto(L_P1__GetMainc41(my_id)));
    bool res_NotLogicOP_80 = true;
    res_NotLogicOP_80 = (res_NotLogicOP_80 && ! (L_P1__GetInMainc5(my_id) == rossogiallo1));
    res_AndLogicOP_79 = (res_AndLogicOP_79 && res_NotLogicOP_80);
    
    res_AndLogicOP_78 = (res_AndLogicOP_78 && res_AndLogicOP_79);
    bool res_NotLogicOP_81 = true;
    bool res_NotLogicOP_82 = true;
    res_NotLogicOP_82 = (res_NotLogicOP_82 && ! (argom9 == rossogiallo));
    res_NotLogicOP_81 = (res_NotLogicOP_81 && ! res_NotLogicOP_82);
    res_AndLogicOP_78 = (res_AndLogicOP_78 && res_NotLogicOP_81);
    
    res_OrLogicOP_71 = (res_OrLogicOP_71 || res_AndLogicOP_78);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_71);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
    
    {  se il ripristino dello stato  non è  diverso da  commento: {56,}  state1  commento: {107,} commento: {35,} o  se il controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo commento: {38,} o  se il contatore MainClass_C1_contatore_Co8 non è  maggiore di  commento: {54,} 123 o  se l'argomento argomento_ave2 non  è  uguale a c270 commento: {39,}  commento: {37,} o  se la variabile MainClass_C1_variabile_V2 è  minore di  commento: {55,} 5 commento: {35,} o  se il controllo MainClass_C1_controllo_C1 non è  diverso da  False , Verifica che   commento: {47,48,49,51,}  commento: {,}  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  commento: {54,} 13150
     commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T4 sia disattivo
     commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P6 non sia  diverso da c270
     commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P9 non sia  maggiore di  commento: {54,} 7
     commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C5 sia  diverso da RossoGialloGiallo
    
    
    }
*/
bool L_P1__Macro6(instance_id_t const my_id , bool argom12, C1_Enumerat4 argom13, C1_Enumerat2 argom14, C1_Enumerat2 argom15, bool argom16, C1_Enumerat2 argom17, bool argom18)
{
bool res_AndLogicOP_0 = true;
    
    //  se il ripristino dello stato  non è  diverso da  *56,*  state1  *107,* *35,* o  se il controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo *38,* o  se il contatore MainClass_C1_contatore_Co8 non è  maggiore di  *54,* 123 o  se l'argomento argomento_ave2 non  è  uguale a c270 *39,*  *37,* o  se la variabile MainClass_C1_variabile_V2 è  minore di  *55,* 5 *35,* o  se il controllo MainClass_C1_controllo_C1 non è  diverso da  False , Verifica che   *47,48,49,51,*  *,*  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  *54,* 13150
    //   *104,* e  che  *,*  il timer MainClass_C1_timer_T4 sia disattivo
    //   *104,* e  che  *34,*  il parametro MainClass_C1_parametro_P6 non sia  diverso da c270
    //   *104,* e  che  *34,*  il parametro MainClass_C1_parametro_P9 non sia  maggiore di  *54,* 7
    //   *104,* o  che  *,*  il controllo MainClass_C1_controllo_C5 sia  diverso da RossoGialloGiallo
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_OrLogicOP_4 = false;
    bool res_OrLogicOP_5 = false;
    bool res_OrLogicOP_6 = false;
    bool res_NotLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetStato1(my_id) == C1_St_state));
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! res_NotLogicOP_8);
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_NotLogicOP_7);
    res_OrLogicOP_6 = (res_OrLogicOP_6 || (L_P1__GetInMainc4(my_id) == rossogiallo));
    
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_OrLogicOP_6);
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (Counter_GetValore(L_P1__GetMainc44(my_id)) > 123u));
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_NotLogicOP_9);
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_OrLogicOP_5);
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (argom13 == c270));
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_NotLogicOP_10);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_OrLogicOP_4);
    res_OrLogicOP_3 = (res_OrLogicOP_3 || (L_P1__GetMainc32(my_id) < 5u));
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    bool res_NotLogicOP_11 = true;
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (L_P1__GetInMainc3(my_id) == false));
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! res_NotLogicOP_12);
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_11);
    
    if(res_OrLogicOP_2){
    bool res_OrLogicOP_13 = false;
    bool res_AndLogicOP_14 = true;
    bool res_AndLogicOP_15 = true;
    bool res_AndLogicOP_16 = true;
    res_AndLogicOP_16 = (res_AndLogicOP_16 && (Counter_GetValore(L_P1__GetMainc44(my_id)) > 13150u));
    res_AndLogicOP_16 = (res_AndLogicOP_16 && Timer_Disattivo(L_P1__GetMainc42(my_id)));
    
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_AndLogicOP_16);
    bool res_NotLogicOP_17 = true;
    bool res_NotLogicOP_18 = true;
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! (L_P1__GetParamMainc8(my_id) == c270));
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! res_NotLogicOP_18);
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_NotLogicOP_17);
    
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_AndLogicOP_15);
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (L_P1__GetParamMainc9(my_id) > 7u));
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_NotLogicOP_19);
    
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_AndLogicOP_14);
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! (L_P1__GetInMainc5(my_id) == rossogiallo1));
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_NotLogicOP_20);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_OrLogicOP_13);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
    
    { commento: {61,}  se il controllo ConsDef è uguale a FALSE  commento: {37,} o  se la variabile MainClass_C1_variabile_V9 non è  minore di  commento: {55,} 2 commento: {35,} e  se il controllo MainClass_C1_controllo_C8 non è  diverso da  False , Tutte le seguenti { 
      se la macro  MainClass_C1_macrova_M3 ( con argomento_a4   uguale a True ,argomento_a7   uguale a avvio ,argomento_a10   uguale a c270x ,argomento_a2   uguale a RossoGialloGiallo ,argomento_a6   uguale a RossoGiallo  e argomento_a1   uguale a c270x )   è  diverso da RossoGialloGiallo commento: {40,}  commento: {37,} e  se la variabile MainClass_C1_variabile_V9 è  maggiore di  commento: {54,} 4, Verifica che   commento: {50,51,}  commento: {,}  la variabile MainClass_C1_variabile_V9 non sia  uguale a  commento: {53,} 4
     commento: {104,} o  che  commento: {,}  il contatore MainClass_C1_contatore_Co8 sia  minore di  commento: {55,} 1
     commento: {104,} e  che  commento: {38,}  il contatore MainClass_C1_contatore_Co8 non sia  diverso da  commento: {56,} 13
     commento: {104,} e  che  commento: {38,}  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  commento: {54,} 151
     commento: {104,} o  che  commento: {38,}  il contatore MainClass_C1_contatore_Co8 non sia  uguale a  commento: {53,} 104
    
    
     } Verifica che   commento: {49,52,}  commento: {,}  il timer MainClass_C1_timer_T9 non sia scaduto
     commento: {104,} o  che   l'argomento argomento_ave5 sia  uguale a RossoGialloGiallo commento: {,} 
    
    
    }
*/
bool L_P1__Macro7(instance_id_t const my_id , C1_Enumerat1 argom19, C1_Enumerat3 argom20, C1_Enumerat2 argom21)
{
bool res_AndLogicOP_0 = true;
    
    //  *61,*  se il controllo ConsDef è uguale a FALSE  *37,* o  se la variabile MainClass_C1_variabile_V9 non è  minore di  *55,* 2 *35,* e  se il controllo MainClass_C1_controllo_C8 non è  diverso da  False , Tutte le seguenti { 
    //    se la macro  MainClass_C1_macrova_M3 ( con argomento_a4   uguale a True ,argomento_a7   uguale a avvio ,argomento_a10   uguale a c270x ,argomento_a2   uguale a RossoGialloGiallo ,argomento_a6   uguale a RossoGiallo  e argomento_a1   uguale a c270x )   è  diverso da RossoGialloGiallo *40,*  *37,* e  se la variabile MainClass_C1_variabile_V9 è  maggiore di  *54,* 4, Verifica che   *50,51,*  *,*  la variabile MainClass_C1_variabile_V9 non sia  uguale a  *53,* 4
    //   *104,* o  che  *,*  il contatore MainClass_C1_contatore_Co8 sia  minore di  *55,* 1
    //   *104,* e  che  *38,*  il contatore MainClass_C1_contatore_Co8 non sia  diverso da  *56,* 13
    //   *104,* e  che  *38,*  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  *54,* 151
    //   *104,* o  che  *38,*  il contatore MainClass_C1_contatore_Co8 non sia  uguale a  *53,* 104
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    res_OrLogicOP_2 = (res_OrLogicOP_2 || (L_P1__GetInConsd(my_id) == false));
    bool res_AndLogicOP_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetMainc34(my_id) < 2u));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_4);
    bool res_NotLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetInMainc6(my_id) == false));
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! res_NotLogicOP_6);
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_5);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_3);
    
    if(res_OrLogicOP_2){
    bool res_ImpliesLogicOp_7 = true;
    bool res_AndLogicOP_8 = true;
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__Macro2(my_id,c270x,c270x,rossogiallo1,true,rossogiallo,avvio) == rossogiallo1));
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_9);
    res_AndLogicOP_8 = (res_AndLogicOP_8 && (L_P1__GetMainc34(my_id) > 4u));
    
    if(res_AndLogicOP_8){
    bool res_OrLogicOP_10 = false;
    bool res_OrLogicOP_11 = false;
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (L_P1__GetMainc34(my_id) == 4u));
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_NotLogicOP_12);
    bool res_AndLogicOP_13 = true;
    bool res_AndLogicOP_14 = true;
    res_AndLogicOP_14 = (res_AndLogicOP_14 && (Counter_GetValore(L_P1__GetMainc44(my_id)) < 1u));
    bool res_NotLogicOP_15 = true;
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (Counter_GetValore(L_P1__GetMainc44(my_id)) == 13u));
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! res_NotLogicOP_16);
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_NotLogicOP_15);
    
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_AndLogicOP_14);
    res_AndLogicOP_13 = (res_AndLogicOP_13 && (Counter_GetValore(L_P1__GetMainc44(my_id)) > 151u));
    
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_AndLogicOP_13);
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_OrLogicOP_11);
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! (Counter_GetValore(L_P1__GetMainc44(my_id)) == 104u));
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_NotLogicOP_17);
    
    res_ImpliesLogicOp_7 = (res_ImpliesLogicOp_7 && res_OrLogicOP_10);
    }
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_ImpliesLogicOp_7);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *49,52,*  *,*  il timer MainClass_C1_timer_T9 non sia scaduto
    //   *104,* o  che   l'argomento argomento_ave5 sia  uguale a RossoGialloGiallo
    bool res_OrLogicOP_18 = false;
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! Timer_Scaduto(L_P1__GetMainc43(my_id)));
    res_OrLogicOP_18 = (res_OrLogicOP_18 || res_NotLogicOP_19);
    res_OrLogicOP_18 = (res_OrLogicOP_18 || (argom20 == rossogiallo1));
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_18);
    
    
    
    return res_AndLogicOP_0;
}


// Macro valorizzate

/*
    CNL corrispondente:
    
    { commento: {[}
     commento: {46,} assegna alla macro il valore RossoGialloGiallo commento: {],}
    }
*/
C1_Enumerat3 L_P1__Macro2(instance_id_t const my_id , C1_Enumerat3 argom2, C1_Enumerat3 argom3, C1_Enumerat3 argom4, bool argom5, C1_Enumerat1 argom6, C1_Enumerat2 argom7)
{
return rossogiallo1;
}



