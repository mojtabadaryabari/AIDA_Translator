// Codice del modello 'TestCase23', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#include "Logica/ClasseMainClass_C1.h"
#include "Logica/ClasseSubClass_C2.h"
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
	    L_P1__SetOutEvent3(my_id, LDS_MANCMD_UNEXPECTED);
    } else {
        L_P1__SetOutEvent3(my_id, LDS_MANCMD_NOOP);
    }
    if (L_P1__GetInEvent2(my_id)) {
	    L_P1__SetOutEvent4(my_id, LDS_MANCMD_UNEXPECTED);
    } else {
        L_P1__SetOutEvent4(my_id, LDS_MANCMD_NOOP);
    }
}

static void L_P1_C1_SetExpectedCmdsResponse(instance_id_t const my_id, C1_Stateenu state)
{        
    switch (state) {
    case C1_St_state:
        // manual commands of L_P1_C1 that can be received in C1_St_state
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
    Nessuna
    }
*/
static inline bool L_P1__Guard1(instance_id_t const my_id)
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
    Nessuna
    }
*/
static inline void L_P1__Effec1(instance_id_t const my_id)
{
    
}



// ********** Definizione metodi **********

// Metodi standard

void L_P1_C1_Init(instance_id_t const my_id)
{
    // init variabili di stato
    L_P1__SetMainc19(my_id, 0);
    L_P1__SetMainc21(my_id, false);
    L_P1__SetMainc23(my_id, 0);
    L_P1__SetMainc25(my_id, 0);
    L_P1__SetMainc26(my_id, 0);
    L_P1__SetMainc27(my_id, 0);
    L_P1__SetStato1(my_id, C1_St_Stato);
    // init controlli precedenti
    L_P1__SetMainc12(my_id, true);
    L_P1__SetMainc14(my_id, true);
    L_P1__SetMainc16(my_id, gialloxverd);
    L_P1__SetMainc18(my_id, false);
    // init Timer e Counter
    Timer_AggmInit(L_P1__GetMainc28(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc28_ID);
    Timer_Init(L_P1__GetMainc28(my_id), 130000);
    Timer_AggmInit(L_P1__GetMainc29(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc29_ID);
    Timer_Init(L_P1__GetMainc29(my_id), 130000);
    Timer_AggmInit(L_P1__GetMainc30(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc30_ID);
    Timer_Init(L_P1__GetMainc30(my_id), 4542000);
    Timer_AggmInit(L_P1__GetMainc31(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc31_ID);
    Timer_Init(L_P1__GetMainc31(my_id), 4542000);
    Timer_AggmInit(L_P1__GetMainc32(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc32_ID);
    Timer_Init(L_P1__GetMainc32(my_id), 113000);
    Timer_AggmInit(L_P1__GetMainc33(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc33_ID);
    Timer_Init(L_P1__GetMainc33(my_id), 113000);
    Timer_AggmInit(L_P1__GetMainc34(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc34_ID);
    Timer_Init(L_P1__GetMainc34(my_id), 40542000);
    Timer_AggmInit(L_P1__GetMainc35(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc35_ID);
    Timer_Init(L_P1__GetMainc35(my_id), 40542000);
    Timer_AggmInit(L_P1__GetMainc36(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc36_ID);
    Timer_Init(L_P1__GetMainc36(my_id), 5000);
    Timer_AggmInit(L_P1__GetMainc37(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc37_ID);
    Timer_Init(L_P1__GetMainc37(my_id), 5000);
    Timer_AggmInit(L_P1__GetMainc38(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc38_ID);
    Timer_Init(L_P1__GetMainc38(my_id), 1000);
    Counter_AggmInit(L_P1__GetMainc39(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc39_ID);
    Counter_Init(L_P1__GetMainc39(my_id));
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
    L_P1__SetMainc20(my_id, L_P1__GetMainc19(my_id));
    L_P1__SetMainc22(my_id, L_P1__GetMainc21(my_id));
    L_P1__SetMainc24(my_id, L_P1__GetMainc23(my_id));
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

        case C1_St_state:
                { } // fine transizioni da state nella fase LDS_PHASE_MANUAL
            break;

        default:
            STOP_EXECUTION(LOGIC_ERROR);
            break;  // Needed for MISRA C syntactic compliance
        } // switch sugli stati chiuso
        break;
 

    case LDS_PHASE_STATE:

        switch (L_P1_C1_GetState(my_id)) {

        case C1_St_state:
            if (L_P1__Guard1(my_id)) {
                L_P1_C1_SetState(my_id, C1_St_state);
                L_P1__Effec1(my_id);				
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
    Timer_Exec(L_P1__GetMainc28(my_id));
    Timer_Exec(L_P1__GetMainc29(my_id));
    Timer_Exec(L_P1__GetMainc30(my_id));
    Timer_Exec(L_P1__GetMainc31(my_id));
    Timer_Exec(L_P1__GetMainc32(my_id));
    Timer_Exec(L_P1__GetMainc33(my_id));
    Timer_Exec(L_P1__GetMainc34(my_id));
    Timer_Exec(L_P1__GetMainc35(my_id));
    Timer_Exec(L_P1__GetMainc36(my_id));
    Timer_Exec(L_P1__GetMainc37(my_id));
    Timer_Exec(L_P1__GetMainc38(my_id));
}

void L_P1_C1_GSetSafe(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C1(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C1(proc_id);
    L_P1__SetOutMainc(my_id, c270xx);
    L_P1__SetOutMainc1(my_id, gialloxverd);
    L_P1__SetOutMainc2(my_id, gialloxverd);
    L_P1__SetOutMainc3(my_id, false);
    L_P1__SetOutMainc4(my_id, rosso);
}

void L_P1_C1_GUpdatePrev(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C1(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C1(proc_id);
    L_P1__SetMainc12(my_id, L_P1__GetInMainc11(my_id));
    L_P1__SetMainc14(my_id, L_P1__GetInMainc13(my_id));
    L_P1__SetMainc16(my_id, L_P1__GetInMainc15(my_id));
    L_P1__SetMainc18(my_id, L_P1__GetInMainc17(my_id));
    L_P1__SetMainc20(my_id, L_P1__GetMainc19(my_id));
    L_P1__SetMainc22(my_id, L_P1__GetMainc21(my_id));
    L_P1__SetMainc24(my_id, L_P1__GetMainc23(my_id));
}

// ********** Definizione macro **********

// Macro di effetto

/*
    CNL corrispondente:
    
    { commento: {34,}  se il parametro MainClass_C1_parametro_P8 è  uguale a GialloxVerdex commento: {38,} o  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  commento: {56,} 1442 commento: {34,} e  se il parametro MainClass_C1_parametro_P5 non è  diverso da  False , commento: {66,} Assegna al comando MainClass_C1_comando_C1 il valore c270xx
    
       
     commento: {34,}  se lo stato  non è  diverso da  commento: {56,}  state1  commento: {106,} commento: {38,} e  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  commento: {53,} 13 commento: {34,} e  se il parametro MainClass_C1_parametro_P8 non è  uguale a GialloxVerdex commento: {34,} o  se il parametro MainClass_C1_parametro_P5 non è  diverso da  True  commento: {35,} e  se il controllo MainClass_C1_controllo_C9 è  diverso da GialloxVerdex, commento: {66,} Assegna al comando MainClass_C1_comando_C10 il valore GialloxVerdex
    
       
     commento: {34,}  se lo stato  è  uguale a  commento: {53,}  state1  commento: {106,} e  se l'argomento argomento_af6 è  diverso da GialloVerde commento: {39,}  o  se l'argomento argomento_af6 non  è  uguale a GialloVerde commento: {39,}  commento: {34,} o  se il parametro MainClass_C1_parametro_P8 è  uguale a GialloxVerdex, commento: {71,}Decrementa il contatore MainClass_C1_contatore_Co2
    
     ,altrimenti  commento: {68,}Attiva il timer MainClass_C1_timer_T3
    
    
     commento: {38,}  se il contatore MainClass_C1_contatore_Co2 è  maggiore di  commento: {54,} 12 commento: {36,} o  se il timer MainClass_C1_timer_T3 non è scaduto commento: {37,} o  se la variabile MainClass_C1_variabile_V7 è  maggiore di  commento: {54,} 5 commento: {35,} o  se il controllo MainClass_C1_controllo_C3 non è  diverso da  False  commento: {34,} o  se il parametro MainClass_C1_parametro_P8 non è  diverso da GialloxVerdex, commento: {66,} Assegna al comando MainClass_C1_comando_C10 il valore GialloxVerdex
    
       
    
    }
*/
void L_P1__Macro(instance_id_t const my_id , C1_Enumerat2 argom, C1_Enumerat1 argom1)
{
//  *34,*  se il parametro MainClass_C1_parametro_P8 è  uguale a GialloxVerdex *38,* o  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  *56,* 1442 *34,* e  se il parametro MainClass_C1_parametro_P5 non è  diverso da  False , *66,* Assegna al comando MainClass_C1_comando_C1 il valore c270xx
    bool res_OrLogicOP_0 = false;
    res_OrLogicOP_0 = (res_OrLogicOP_0 || (L_P1__GetParamMainc10(my_id) == gialloxverd));
    bool res_AndLogicOP_1 = true;
    bool res_NotLogicOP_2 = true;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (Counter_GetValore(L_P1__GetMainc39(my_id)) == 1442u));
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! res_NotLogicOP_3);
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_2);
    bool res_NotLogicOP_4 = true;
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetParamMainc8(my_id) == false));
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! res_NotLogicOP_5);
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_4);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_1);
    
    if(res_OrLogicOP_0){
    
    L_P1__SetOutMainc(my_id,c270xx);
    }
    //  *34,*  se lo stato  non è  diverso da  *56,*  state1  *106,* *38,* e  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  *53,* 13 *34,* e  se il parametro MainClass_C1_parametro_P8 non è  uguale a GialloxVerdex *34,* o  se il parametro MainClass_C1_parametro_P5 non è  diverso da  True  *35,* e  se il controllo MainClass_C1_controllo_C9 è  diverso da GialloxVerdex, *66,* Assegna al comando MainClass_C1_comando_C10 il valore GialloxVerdex
    bool res_OrLogicOP_6 = false;
    bool res_AndLogicOP_7 = true;
    bool res_AndLogicOP_8 = true;
    bool res_NotLogicOP_9 = true;
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1_C1_GetState(my_id) == C1_St_state));
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! res_NotLogicOP_10);
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_9);
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (Counter_GetValore(L_P1__GetMainc39(my_id)) == 13u));
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_11);
    
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_AndLogicOP_8);
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (L_P1__GetParamMainc10(my_id) == gialloxverd));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_12);
    
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_AndLogicOP_7);
    bool res_AndLogicOP_13 = true;
    bool res_NotLogicOP_14 = true;
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (L_P1__GetParamMainc8(my_id) == true));
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! res_NotLogicOP_15);
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_NotLogicOP_14);
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (L_P1__GetInMainc6(my_id) == gialloxverd));
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_NotLogicOP_16);
    
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_AndLogicOP_13);
    
    if(res_OrLogicOP_6){
    
    L_P1__SetOutMainc1(my_id,gialloxverd);
    }
    //  *34,*  se lo stato  è  uguale a  *53,*  state1  *106,* e  se l'argomento argomento_af6 è  diverso da GialloVerde *39,*  o  se l'argomento argomento_af6 non  è  uguale a GialloVerde *39,*  *34,* o  se il parametro MainClass_C1_parametro_P8 è  uguale a GialloxVerdex, *71,*Decrementa il contatore MainClass_C1_contatore_Co2
    // ,altrimenti  *68,*Attiva il timer MainClass_C1_timer_T3
    bool res_OrLogicOP_17 = false;
    bool res_OrLogicOP_18 = false;
    bool res_AndLogicOP_19 = true;
    res_AndLogicOP_19 = (res_AndLogicOP_19 && (L_P1_C1_GetState(my_id) == C1_St_state));
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! (argom == gialloverde));
    res_AndLogicOP_19 = (res_AndLogicOP_19 && res_NotLogicOP_20);
    
    res_OrLogicOP_18 = (res_OrLogicOP_18 || res_AndLogicOP_19);
    bool res_NotLogicOP_21 = true;
    res_NotLogicOP_21 = (res_NotLogicOP_21 && ! (argom == gialloverde));
    res_OrLogicOP_18 = (res_OrLogicOP_18 || res_NotLogicOP_21);
    
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_OrLogicOP_18);
    res_OrLogicOP_17 = (res_OrLogicOP_17 || (L_P1__GetParamMainc10(my_id) == gialloxverd));
    
    if(res_OrLogicOP_17){
    
    Counter_Decr(L_P1__GetMainc39(my_id));
    }else{
    
    Timer_Attiva(L_P1__GetMainc38(my_id));
    }
    //  *38,*  se il contatore MainClass_C1_contatore_Co2 è  maggiore di  *54,* 12 *36,* o  se il timer MainClass_C1_timer_T3 non è scaduto *37,* o  se la variabile MainClass_C1_variabile_V7 è  maggiore di  *54,* 5 *35,* o  se il controllo MainClass_C1_controllo_C3 non è  diverso da  False  *34,* o  se il parametro MainClass_C1_parametro_P8 non è  diverso da GialloxVerdex, *66,* Assegna al comando MainClass_C1_comando_C10 il valore GialloxVerdex
    bool res_OrLogicOP_22 = false;
    bool res_OrLogicOP_23 = false;
    bool res_OrLogicOP_24 = false;
    bool res_OrLogicOP_25 = false;
    res_OrLogicOP_25 = (res_OrLogicOP_25 || (Counter_GetValore(L_P1__GetMainc39(my_id)) > 12u));
    bool res_NotLogicOP_26 = true;
    res_NotLogicOP_26 = (res_NotLogicOP_26 && ! Timer_Scaduto(L_P1__GetMainc38(my_id)));
    res_OrLogicOP_25 = (res_OrLogicOP_25 || res_NotLogicOP_26);
    
    res_OrLogicOP_24 = (res_OrLogicOP_24 || res_OrLogicOP_25);
    res_OrLogicOP_24 = (res_OrLogicOP_24 || (L_P1__GetMainc27(my_id) > 5u));
    
    res_OrLogicOP_23 = (res_OrLogicOP_23 || res_OrLogicOP_24);
    bool res_NotLogicOP_27 = true;
    bool res_NotLogicOP_28 = true;
    res_NotLogicOP_28 = (res_NotLogicOP_28 && ! (L_P1__GetInMainc5(my_id) == false));
    res_NotLogicOP_27 = (res_NotLogicOP_27 && ! res_NotLogicOP_28);
    res_OrLogicOP_23 = (res_OrLogicOP_23 || res_NotLogicOP_27);
    
    res_OrLogicOP_22 = (res_OrLogicOP_22 || res_OrLogicOP_23);
    bool res_NotLogicOP_29 = true;
    bool res_NotLogicOP_30 = true;
    res_NotLogicOP_30 = (res_NotLogicOP_30 && ! (L_P1__GetParamMainc10(my_id) == gialloxverd));
    res_NotLogicOP_29 = (res_NotLogicOP_29 && ! res_NotLogicOP_30);
    res_OrLogicOP_22 = (res_OrLogicOP_22 || res_NotLogicOP_29);
    
    if(res_OrLogicOP_22){
    
    L_P1__SetOutMainc1(my_id,gialloxverd);
    }
}

/*
    CNL corrispondente:
    
    { commento: {34,}  se lo stato  non è  uguale a  commento: {53,}  state1  commento: {106,}, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V7 il valore 8
    
     ,altrimenti  commento: {66,} Assegna al comando MainClass_C1_comando_C1 il valore c270xx
    
    
      se il ripristino dello stato  non è  uguale a  commento: {53,}  state1  commento: {107,} commento: {36,} e  se il timer MainClass_C1_timer_T3 non è attivo commento: {35,} e  se il controllo MainClass_C1_controllo_C3 non è  diverso da  False  commento: {38,} e  se il contatore MainClass_C1_contatore_Co2 non è  maggiore di  commento: {54,} 11, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V7 il valore 3
    
     ,altrimenti   Applica gli effetti
           della macro MainClass_C1_macroef_M9  commento: {73,}
    
    
     commento: {34,}  se lo stato  è  uguale a  commento: {53,}  state1  commento: {106,} o  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} e  se il contatore MainClass_C1_contatore_Co2 non è  maggiore di  commento: {54,} 14 commento: {36,} e  se il timer MainClass_C1_timer_T3 è attivo commento: {38,} e  se il contatore MainClass_C1_contatore_Co2 non è  maggiore di  commento: {54,} 1442, commento: {70,}Incrementa il contatore MainClass_C1_contatore_Co2
    
     ,altrimenti   Applica gli effetti
           della macro MainClass_C1_macroef_M9  commento: {73,}
    
    
     commento: {35,}  se il controllo MainClass_C1_controllo_C3 non è  diverso da  False , commento: {67,} Assegna alla variabile MainClass_C1_variabile_V7 il valore 6
    
     ,altrimenti  commento: {69,}Disattiva il timer MainClass_C1_timer_T3
    
    
    
    }
*/
void L_P1__Macro1(instance_id_t const my_id )
{
//  *34,*  se lo stato  non è  uguale a  *53,*  state1  *106,*, *67,* Assegna alla variabile MainClass_C1_variabile_V7 il valore 8
    // ,altrimenti  *66,* Assegna al comando MainClass_C1_comando_C1 il valore c270xx
    bool res_NotLogicOP_0 = true;
    res_NotLogicOP_0 = (res_NotLogicOP_0 && ! (L_P1_C1_GetState(my_id) == C1_St_state));
    if(res_NotLogicOP_0){
    
    L_P1__SetMainc27(my_id,8u);
    }else{
    
    L_P1__SetOutMainc(my_id,c270xx);
    }
    //  se il ripristino dello stato  non è  uguale a  *53,*  state1  *107,* *36,* e  se il timer MainClass_C1_timer_T3 non è attivo *35,* e  se il controllo MainClass_C1_controllo_C3 non è  diverso da  False  *38,* e  se il contatore MainClass_C1_contatore_Co2 non è  maggiore di  *54,* 11, *67,* Assegna alla variabile MainClass_C1_variabile_V7 il valore 3
    // ,altrimenti   Applica gli effetti
    //       della macro MainClass_C1_macroef_M9
    bool res_AndLogicOP_1 = true;
    bool res_AndLogicOP_2 = true;
    bool res_AndLogicOP_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetStato1(my_id) == C1_St_state));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_4);
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! Timer_Attivo(L_P1__GetMainc38(my_id)));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_5);
    
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_AndLogicOP_3);
    bool res_NotLogicOP_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetInMainc5(my_id) == false));
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! res_NotLogicOP_7);
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_6);
    
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_AndLogicOP_2);
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (Counter_GetValore(L_P1__GetMainc39(my_id)) > 11u));
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_8);
    
    if(res_AndLogicOP_1){
    
    L_P1__SetMainc27(my_id,3u);
    }else{
    
    L_P1__Macro3(my_id);
    }
    //  *73,*
    // *34,*  se lo stato  è  uguale a  *53,*  state1  *106,* o  se il controllo ConsDef  è  uguale a FALSE  *38,* e  se il contatore MainClass_C1_contatore_Co2 non è  maggiore di  *54,* 14 *36,* e  se il timer MainClass_C1_timer_T3 è attivo *38,* e  se il contatore MainClass_C1_contatore_Co2 non è  maggiore di  *54,* 1442, *70,*Incrementa il contatore MainClass_C1_contatore_Co2
    // ,altrimenti   Applica gli effetti
    //       della macro MainClass_C1_macroef_M9
    bool res_OrLogicOP_9 = false;
    res_OrLogicOP_9 = (res_OrLogicOP_9 || (L_P1_C1_GetState(my_id) == C1_St_state));
    bool res_AndLogicOP_10 = true;
    bool res_AndLogicOP_11 = true;
    bool res_AndLogicOP_12 = true;
    res_AndLogicOP_12 = (res_AndLogicOP_12 && (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (Counter_GetValore(L_P1__GetMainc39(my_id)) > 14u));
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_NotLogicOP_13);
    
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_AndLogicOP_12);
    res_AndLogicOP_11 = (res_AndLogicOP_11 && Timer_Attivo(L_P1__GetMainc38(my_id)));
    
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_AndLogicOP_11);
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (Counter_GetValore(L_P1__GetMainc39(my_id)) > 1442u));
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_NotLogicOP_14);
    
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_AndLogicOP_10);
    
    if(res_OrLogicOP_9){
    
    Counter_Incr(L_P1__GetMainc39(my_id));
    }else{
    
    L_P1__Macro3(my_id);
    }
    //  *73,*
    // *35,*  se il controllo MainClass_C1_controllo_C3 non è  diverso da  False , *67,* Assegna alla variabile MainClass_C1_variabile_V7 il valore 6
    // ,altrimenti  *69,*Disattiva il timer MainClass_C1_timer_T3
    bool res_NotLogicOP_15 = true;
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (L_P1__GetInMainc5(my_id) == false));
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! res_NotLogicOP_16);
    if(res_NotLogicOP_15){
    
    L_P1__SetMainc27(my_id,6u);
    }else{
    
    Timer_Disattiva(L_P1__GetMainc38(my_id));
    }
}

/*
    CNL corrispondente:
    
    { commento: {35,}  se il controllo MainClass_C1_controllo_C3 non è  diverso da  True  o  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} e  se il timer MainClass_C1_timer_T3 non è disattivo commento: {34,} o  se il parametro MainClass_C1_parametro_P5 non è  uguale a  False  commento: {37,} e  se la variabile MainClass_C1_variabile_V7 non è  diverso da  commento: {56,} 10, commento: {66,} Assegna al comando MainClass_C1_comando_C10 il valore GialloxVerdex
    
       
     commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è disattivo commento: {35,} e  se il controllo MainClass_C1_controllo_C3 non è  uguale a  True , commento: {71,}Decrementa il contatore MainClass_C1_contatore_Co2
    
       
     commento: {35,}  se il controllo MainClass_C1_controllo_C3 non è  uguale a  False  commento: {35,} o  se il controllo MainClass_C1_controllo_C9 è  uguale a GialloxVerdex commento: {37,} e  se la variabile MainClass_C1_variabile_V7 non è  maggiore di  commento: {54,} 1 commento: {38,} e  se il contatore MainClass_C1_contatore_Co2 non è  minore di  commento: {55,} 12305 commento: {34,} e  se il parametro MainClass_C1_parametro_P5 è  diverso da  True  commento: {34,} e  se il parametro MainClass_C1_parametro_P10 non è  diverso da  commento: {56,} 10,  Applica gli effetti
           della macro MainClass_C1_macroef_M10( con argomento_af6   uguale a GialloVerde ,argomento_af9   uguale a avanzamento ) commento: {73,}
    
       
    
    }
*/
void L_P1__Macro2(instance_id_t const my_id )
{
//  *35,*  se il controllo MainClass_C1_controllo_C3 non è  diverso da  True  o  se il controllo ConsDef  è  uguale a FALSE  *36,* e  se il timer MainClass_C1_timer_T3 non è disattivo *34,* o  se il parametro MainClass_C1_parametro_P5 non è  uguale a  False  *37,* e  se la variabile MainClass_C1_variabile_V7 non è  diverso da  *56,* 10, *66,* Assegna al comando MainClass_C1_comando_C10 il valore GialloxVerdex
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_NotLogicOP_2 = true;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__GetInMainc5(my_id) == true));
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! res_NotLogicOP_3);
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_NotLogicOP_2);
    bool res_AndLogicOP_4 = true;
    res_AndLogicOP_4 = (res_AndLogicOP_4 && (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! Timer_Disattivo(L_P1__GetMainc38(my_id)));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_5);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_4);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_AndLogicOP_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetParamMainc8(my_id) == false));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_7);
    bool res_NotLogicOP_8 = true;
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetMainc27(my_id) == 10u));
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! res_NotLogicOP_9);
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_8);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_6);
    
    if(res_OrLogicOP_0){
    
    L_P1__SetOutMainc1(my_id,gialloxverd);
    }
    //  *110,*  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è disattivo *35,* e  se il controllo MainClass_C1_controllo_C3 non è  uguale a  True , *71,*Decrementa il contatore MainClass_C1_contatore_Co2
    bool res_AndLogicOP_10 = true;
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! Timer_Disattivo(L_P1__GetMainc29(my_id)));
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_NotLogicOP_11);
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (L_P1__GetInMainc5(my_id) == true));
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_NotLogicOP_12);
    
    if(res_AndLogicOP_10){
    
    Counter_Decr(L_P1__GetMainc39(my_id));
    }
    //  *35,*  se il controllo MainClass_C1_controllo_C3 non è  uguale a  False  *35,* o  se il controllo MainClass_C1_controllo_C9 è  uguale a GialloxVerdex *37,* e  se la variabile MainClass_C1_variabile_V7 non è  maggiore di  *54,* 1 *38,* e  se il contatore MainClass_C1_contatore_Co2 non è  minore di  *55,* 12305 *34,* e  se il parametro MainClass_C1_parametro_P5 è  diverso da  True  *34,* e  se il parametro MainClass_C1_parametro_P10 non è  diverso da  *56,* 10,  Applica gli effetti
    //       della macro MainClass_C1_macroef_M10( con argomento_af6   uguale a GialloVerde ,argomento_af9   uguale a avanzamento )
    bool res_OrLogicOP_13 = false;
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1__GetInMainc5(my_id) == false));
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_NotLogicOP_14);
    bool res_AndLogicOP_15 = true;
    bool res_AndLogicOP_16 = true;
    bool res_AndLogicOP_17 = true;
    bool res_AndLogicOP_18 = true;
    res_AndLogicOP_18 = (res_AndLogicOP_18 && (L_P1__GetInMainc6(my_id) == gialloxverd));
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (L_P1__GetMainc27(my_id) > 1u));
    res_AndLogicOP_18 = (res_AndLogicOP_18 && res_NotLogicOP_19);
    
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_AndLogicOP_18);
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! (Counter_GetValore(L_P1__GetMainc39(my_id)) < 12305u));
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_NotLogicOP_20);
    
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_AndLogicOP_17);
    bool res_NotLogicOP_21 = true;
    res_NotLogicOP_21 = (res_NotLogicOP_21 && ! (L_P1__GetParamMainc8(my_id) == true));
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_NotLogicOP_21);
    
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_AndLogicOP_16);
    bool res_NotLogicOP_22 = true;
    bool res_NotLogicOP_23 = true;
    res_NotLogicOP_23 = (res_NotLogicOP_23 && ! (L_P1__GetParamMainc7(my_id) == 10u));
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! res_NotLogicOP_23);
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_NotLogicOP_22);
    
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_AndLogicOP_15);
    
    if(res_OrLogicOP_13){
    
    L_P1__Macro(my_id,gialloverde,avanzamento);
    }
}

/*
    CNL corrispondente:
    
    { commento: {38,}  se il contatore MainClass_C1_contatore_Co2 è  diverso da  commento: {56,} 13 commento: {37,} o  se la variabile MainClass_C1_variabile_V7 non è  minore di  commento: {55,} 10 commento: {36,} e  se il timer MainClass_C1_timer_T3 è disattivo commento: {35,} e  se il controllo MainClass_C1_controllo_C3 non è  diverso da  True  commento: {34,} o  se il parametro MainClass_C1_parametro_P8 non è  uguale a GialloxVerdex, commento: {69,}Disattiva il timer MainClass_C1_timer_T3
    
       
    
    }
*/
void L_P1__Macro3(instance_id_t const my_id )
{
//  *38,*  se il contatore MainClass_C1_contatore_Co2 è  diverso da  *56,* 13 *37,* o  se la variabile MainClass_C1_variabile_V7 non è  minore di  *55,* 10 *36,* e  se il timer MainClass_C1_timer_T3 è disattivo *35,* e  se il controllo MainClass_C1_controllo_C3 non è  diverso da  True  *34,* o  se il parametro MainClass_C1_parametro_P8 non è  uguale a GialloxVerdex, *69,*Disattiva il timer MainClass_C1_timer_T3
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (Counter_GetValore(L_P1__GetMainc39(my_id)) == 13u));
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_NotLogicOP_2);
    bool res_AndLogicOP_3 = true;
    bool res_AndLogicOP_4 = true;
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetMainc27(my_id) < 10u));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_5);
    res_AndLogicOP_4 = (res_AndLogicOP_4 && Timer_Disattivo(L_P1__GetMainc38(my_id)));
    
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_AndLogicOP_4);
    bool res_NotLogicOP_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetInMainc5(my_id) == true));
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! res_NotLogicOP_7);
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_6);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_3);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetParamMainc10(my_id) == gialloxverd));
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_8);
    
    if(res_OrLogicOP_0){
    
    Timer_Disattiva(L_P1__GetMainc38(my_id));
    }
}


// Macro di verifica

/*
    CNL corrispondente:
    
    { commento: {63,}  se il controllo ConsDef è uguale a FALSE  commento: {36,} e  se il timer MainClass_C1_timer_T3 è disattivo commento: {34,} e  se il parametro MainClass_C1_parametro_P8 è  uguale a GialloxVerdex e  se l'argomento argomento_ave10 è  uguale a  True  commento: {39,}  commento: {34,} o  se il parametro MainClass_C1_parametro_P8 è  uguale a GialloxVerdex commento: {36,} o  se il timer MainClass_C1_timer_T3 non è disattivo, Solo una delle seguenti { 
     commento: {62,} commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è attivo commento: {37,} o  se la variabile MainClass_C1_variabile_V7 è  uguale a  commento: {53,} 1 e  se l'argomento argomento_ave7 non  è  diverso da  False  commento: {39,}  o  se l'argomento argomento_ave7 è  uguale a  False  commento: {39,}  e  se l'argomento argomento_ave7 non  è  diverso da  False  commento: {39,}  commento: {35,} o  se il controllo MainClass_C1_controllo_C3 è  uguale a  False , Almeno una delle seguenti { 
     commento: {61,}  se il controllo ConsDef è uguale a FALSE  commento: {38,} e  se il contatore MainClass_C1_contatore_Co2 è  diverso da  commento: {56,} 155 commento: {36,} e  se il timer MainClass_C1_timer_T3 non è disattivo commento: {34,} e  se il parametro MainClass_C1_parametro_P5 è  diverso da  True , Tutte le seguenti { 
     commento: {61,} commento: {38,}  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  commento: {53,} 1342 o  se l'argomento argomento_ave2 è  diverso da c270xx commento: {39,}  commento: {36,} e  se il timer MainClass_C1_timer_T3 non è scaduto, Tutte le seguenti { 
     commento: {61,} commento: {34,}  se lo stato  è  diverso da  commento: {56,}  state1  commento: {106,} commento: {36,} e  se il timer MainClass_C1_timer_T3 non è attivo commento: {34,} e  se il parametro MainClass_C1_parametro_P7 non è  maggiore di  commento: {54,} 2 commento: {34,} o  se il parametro MainClass_C1_parametro_P8 non è  uguale a GialloxVerdex, Tutte le seguenti { 
     commento: {63,} commento: {35,}  se il controllo MainClass_C1_controllo_C3 non è  diverso da  False  e  se l'argomento argomento_ave10 non  è  diverso da  True  commento: {39,}  commento: {38,} o  se il contatore MainClass_C1_contatore_Co2 non è  minore di  commento: {55,} 13 commento: {36,} o  se il timer MainClass_C1_timer_T3 non è disattivo commento: {34,} o  se il parametro MainClass_C1_parametro_P7 è  diverso da  commento: {56,} 9 commento: {35,} e  se il controllo MainClass_C1_controllo_C9 è  uguale a GialloxVerdex, Solo una delle seguenti { 
     commento: {63,} commento: {36,}  se il timer MainClass_C1_timer_T3 non è scaduto commento: {38,} o  se il contatore MainClass_C1_contatore_Co2 è  diverso da  commento: {56,} 12130 o  se l'argomento argomento_ave7 non  è  diverso da  True  commento: {39,}  commento: {35,} e  se il controllo MainClass_C1_controllo_C9 non è  uguale a GialloxVerdex commento: {34,} o  se il parametro MainClass_C1_parametro_P8 è  uguale a GialloxVerdex, Solo una delle seguenti { 
     commento: {38,}  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  commento: {53,} 155 commento: {37,} e  se la variabile MainClass_C1_variabile_V7 è  uguale a  commento: {53,} 3 commento: {38,} e  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  commento: {53,} 1342 commento: {38,} o  se il contatore MainClass_C1_contatore_Co2 non è  maggiore di  commento: {54,} 151 commento: {38,} o  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  commento: {56,} 14305, Verifica che   commento: {47,49,52,}  commento: {,}  il timer MainClass_C1_timer_T3 non sia attivo
     commento: {104,} o  che  commento: {36,}  il timer MainClass_C1_timer_T3 sia scaduto
     commento: {104,} o  che   l'argomento argomento_ave7 sia  uguale a  False  commento: {,} 
     commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P10 sia  maggiore di  commento: {54,} 5
    
    
     } Verifica che   commento: {49,}  commento: {,}  il timer MainClass_C1_timer_T3 non sia scaduto
    
    
     } Verifica che   commento: {47,48,49,50,52,}   l'argomento argomento_ave7 non  sia  uguale a  False  commento: {,} 
     commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C9 sia  uguale a GialloxVerdex
     commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T3 sia attivo
     commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V7 non sia  diverso da  commento: {56,} 7
     commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P8 sia  uguale a GialloxVerdex
    
    
     } Verifica che   commento: {48,50,51,52,}  commento: {,}  la variabile MainClass_C1_variabile_V7 sia  maggiore di  commento: {54,} 3
     commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C3 sia  uguale a  True 
     commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co2 sia  uguale a  commento: {53,} 14
     commento: {104,} o  che  commento: {37,}  la variabile MainClass_C1_variabile_V7 non sia  minore di  commento: {55,} 5
     commento: {104,} e  che  commento: {38,}  il contatore MainClass_C1_contatore_Co2 sia  minore di  commento: {55,} 1305
     commento: {104,} o  che   l'argomento argomento_ave7 sia  diverso da  True  commento: {,} 
    
    
     } Verifica che   commento: {48,50,}  commento: {,}  la variabile MainClass_C1_variabile_V7 sia  maggiore di  commento: {54,} 4
     commento: {104,} o  che  commento: {37,}  la variabile MainClass_C1_variabile_V7 sia  minore di  commento: {55,} 10
     commento: {104,} e  che  commento: {37,}  la variabile MainClass_C1_variabile_V7 sia  uguale a  commento: {53,} 1
     commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C9 sia  uguale a GialloxVerdex
    
    
     } Verifica che   commento: {51,}  commento: {,}  il contatore MainClass_C1_contatore_Co2 non sia  diverso da  commento: {56,} 1
    
    
     } Verifica che   commento: {47,48,49,}  commento: {34,}  il parametro MainClass_C1_parametro_P7 non sia  minore di  commento: {55,} 4
     commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T3 sia attivo
     commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C9 sia  diverso da GialloxVerdex
    
    
     } Verifica che   commento: {48,49,50,51,}  commento: {,}  il timer MainClass_C1_timer_T3 sia attivo
     commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C9 sia  uguale a GialloxVerdex
     commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co2 non sia  maggiore di  commento: {54,} 1321
     commento: {104,} o  che  commento: {38,}  il contatore MainClass_C1_contatore_Co2 non sia  diverso da  commento: {56,} 10
     commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V7 non sia  maggiore di  commento: {54,} 5
     commento: {104,} e  che  commento: {35,}  il controllo MainClass_C1_controllo_C9 non sia  diverso da GialloxVerdex
    
    
    }
*/
bool L_P1__Macro6(instance_id_t const my_id , C1_Enumerat2 argom9, bool argom10, C1_Enumerat3 argom11, C1_Enumerat2 argom12, bool argom13)
{
bool res_AndLogicOP_0 = true;
    
    //  *63,*  se il controllo ConsDef è uguale a FALSE  *36,* e  se il timer MainClass_C1_timer_T3 è disattivo *34,* e  se il parametro MainClass_C1_parametro_P8 è  uguale a GialloxVerdex e  se l'argomento argomento_ave10 è  uguale a  True  *39,*  *34,* o  se il parametro MainClass_C1_parametro_P8 è  uguale a GialloxVerdex *36,* o  se il timer MainClass_C1_timer_T3 non è disattivo, Solo una delle seguenti { 
    //   *62,* *110,*  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è attivo *37,* o  se la variabile MainClass_C1_variabile_V7 è  uguale a  *53,* 1 e  se l'argomento argomento_ave7 non  è  diverso da  False  *39,*  o  se l'argomento argomento_ave7 è  uguale a  False  *39,*  e  se l'argomento argomento_ave7 non  è  diverso da  False  *39,*  *35,* o  se il controllo MainClass_C1_controllo_C3 è  uguale a  False , Almeno una delle seguenti { 
    //   *61,*  se il controllo ConsDef è uguale a FALSE  *38,* e  se il contatore MainClass_C1_contatore_Co2 è  diverso da  *56,* 155 *36,* e  se il timer MainClass_C1_timer_T3 non è disattivo *34,* e  se il parametro MainClass_C1_parametro_P5 è  diverso da  True , Tutte le seguenti { 
    //   *61,* *38,*  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  *53,* 1342 o  se l'argomento argomento_ave2 è  diverso da c270xx *39,*  *36,* e  se il timer MainClass_C1_timer_T3 non è scaduto, Tutte le seguenti { 
    //   *61,* *34,*  se lo stato  è  diverso da  *56,*  state1  *106,* *36,* e  se il timer MainClass_C1_timer_T3 non è attivo *34,* e  se il parametro MainClass_C1_parametro_P7 non è  maggiore di  *54,* 2 *34,* o  se il parametro MainClass_C1_parametro_P8 non è  uguale a GialloxVerdex, Tutte le seguenti { 
    //   *63,* *35,*  se il controllo MainClass_C1_controllo_C3 non è  diverso da  False  e  se l'argomento argomento_ave10 non  è  diverso da  True  *39,*  *38,* o  se il contatore MainClass_C1_contatore_Co2 non è  minore di  *55,* 13 *36,* o  se il timer MainClass_C1_timer_T3 non è disattivo *34,* o  se il parametro MainClass_C1_parametro_P7 è  diverso da  *56,* 9 *35,* e  se il controllo MainClass_C1_controllo_C9 è  uguale a GialloxVerdex, Solo una delle seguenti { 
    //   *63,* *36,*  se il timer MainClass_C1_timer_T3 non è scaduto *38,* o  se il contatore MainClass_C1_contatore_Co2 è  diverso da  *56,* 12130 o  se l'argomento argomento_ave7 non  è  diverso da  True  *39,*  *35,* e  se il controllo MainClass_C1_controllo_C9 non è  uguale a GialloxVerdex *34,* o  se il parametro MainClass_C1_parametro_P8 è  uguale a GialloxVerdex, Solo una delle seguenti { 
    //   *38,*  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  *53,* 155 *37,* e  se la variabile MainClass_C1_variabile_V7 è  uguale a  *53,* 3 *38,* e  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  *53,* 1342 *38,* o  se il contatore MainClass_C1_contatore_Co2 non è  maggiore di  *54,* 151 *38,* o  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  *56,* 14305, Verifica che   *47,49,52,*  *,*  il timer MainClass_C1_timer_T3 non sia attivo
    //   *104,* o  che  *36,*  il timer MainClass_C1_timer_T3 sia scaduto
    //   *104,* o  che   l'argomento argomento_ave7 sia  uguale a  False  *,* 
    //   *104,* e  che  *34,*  il parametro MainClass_C1_parametro_P10 sia  maggiore di  *54,* 5
    //   } Verifica che   *49,*  *,*  il timer MainClass_C1_timer_T3 non sia scaduto
    //   } Verifica che   *47,48,49,50,52,*   l'argomento argomento_ave7 non  sia  uguale a  False  *,* 
    //   *104,* o  che  *,*  il controllo MainClass_C1_controllo_C9 sia  uguale a GialloxVerdex
    //   *104,* e  che  *,*  il timer MainClass_C1_timer_T3 sia attivo
    //   *104,* o  che  *,*  la variabile MainClass_C1_variabile_V7 non sia  diverso da  *56,* 7
    //   *104,* o  che  *34,*  il parametro MainClass_C1_parametro_P8 sia  uguale a GialloxVerdex
    //   } Verifica che   *48,50,51,52,*  *,*  la variabile MainClass_C1_variabile_V7 sia  maggiore di  *54,* 3
    //   *104,* e  che  *,*  il controllo MainClass_C1_controllo_C3 sia  uguale a  True 
    //   *104,* e  che  *,*  il contatore MainClass_C1_contatore_Co2 sia  uguale a  *53,* 14
    //   *104,* o  che  *37,*  la variabile MainClass_C1_variabile_V7 non sia  minore di  *55,* 5
    //   *104,* e  che  *38,*  il contatore MainClass_C1_contatore_Co2 sia  minore di  *55,* 1305
    //   *104,* o  che   l'argomento argomento_ave7 sia  diverso da  True  *,* 
    //   } Verifica che   *48,50,*  *,*  la variabile MainClass_C1_variabile_V7 sia  maggiore di  *54,* 4
    //   *104,* o  che  *37,*  la variabile MainClass_C1_variabile_V7 sia  minore di  *55,* 10
    //   *104,* e  che  *37,*  la variabile MainClass_C1_variabile_V7 sia  uguale a  *53,* 1
    //   *104,* e  che  *,*  il controllo MainClass_C1_controllo_C9 sia  uguale a GialloxVerdex
    //   } Verifica che   *51,*  *,*  il contatore MainClass_C1_contatore_Co2 non sia  diverso da  *56,* 1
    //   } Verifica che   *47,48,49,*  *34,*  il parametro MainClass_C1_parametro_P7 non sia  minore di  *55,* 4
    //   *104,* e  che  *,*  il timer MainClass_C1_timer_T3 sia attivo
    //   *104,* e  che  *,*  il controllo MainClass_C1_controllo_C9 sia  diverso da GialloxVerdex
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_AndLogicOP_4 = true;
    bool res_AndLogicOP_5 = true;
    bool res_AndLogicOP_6 = true;
    res_AndLogicOP_6 = (res_AndLogicOP_6 && (L_P1__GetInConsd(my_id) == false));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && Timer_Disattivo(L_P1__GetMainc38(my_id)));
    
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_AndLogicOP_6);
    res_AndLogicOP_5 = (res_AndLogicOP_5 && (L_P1__GetParamMainc10(my_id) == gialloxverd));
    
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_AndLogicOP_5);
    res_AndLogicOP_4 = (res_AndLogicOP_4 && (argom10 == true));
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_AndLogicOP_4);
    res_OrLogicOP_3 = (res_OrLogicOP_3 || (L_P1__GetParamMainc10(my_id) == gialloxverd));
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! Timer_Disattivo(L_P1__GetMainc38(my_id)));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_7);
    
    if(res_OrLogicOP_2){
    bool res_XorLogicOP_8 = true;
    int xorIndex_res_XorLogicOP_8 = 0;
    bool res_ImpliesLogicOp_9 = true;
    bool res_OrLogicOP_10 = false;
    bool res_OrLogicOP_11 = false;
    bool res_OrLogicOP_12 = false;
    res_OrLogicOP_12 = (res_OrLogicOP_12 || Timer_Attivo(L_P1__GetMainc29(my_id)));
    bool res_AndLogicOP_13 = true;
    res_AndLogicOP_13 = (res_AndLogicOP_13 && (L_P1__GetMainc27(my_id) == 1u));
    bool res_NotLogicOP_14 = true;
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (argom13 == false));
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! res_NotLogicOP_15);
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_NotLogicOP_14);
    
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_AndLogicOP_13);
    
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_OrLogicOP_12);
    bool res_AndLogicOP_16 = true;
    res_AndLogicOP_16 = (res_AndLogicOP_16 && (argom13 == false));
    bool res_NotLogicOP_17 = true;
    bool res_NotLogicOP_18 = true;
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! (argom13 == false));
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! res_NotLogicOP_18);
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_NotLogicOP_17);
    
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_AndLogicOP_16);
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_OrLogicOP_11);
    res_OrLogicOP_10 = (res_OrLogicOP_10 || (L_P1__GetInMainc5(my_id) == false));
    
    if(res_OrLogicOP_10){
    bool res_OrLogicOP_19 = false;
    bool res_ImpliesLogicOp_20 = true;
    bool res_AndLogicOP_21 = true;
    bool res_AndLogicOP_22 = true;
    bool res_AndLogicOP_23 = true;
    res_AndLogicOP_23 = (res_AndLogicOP_23 && (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_24 = true;
    res_NotLogicOP_24 = (res_NotLogicOP_24 && ! (Counter_GetValore(L_P1__GetMainc39(my_id)) == 155u));
    res_AndLogicOP_23 = (res_AndLogicOP_23 && res_NotLogicOP_24);
    
    res_AndLogicOP_22 = (res_AndLogicOP_22 && res_AndLogicOP_23);
    bool res_NotLogicOP_25 = true;
    res_NotLogicOP_25 = (res_NotLogicOP_25 && ! Timer_Disattivo(L_P1__GetMainc38(my_id)));
    res_AndLogicOP_22 = (res_AndLogicOP_22 && res_NotLogicOP_25);
    
    res_AndLogicOP_21 = (res_AndLogicOP_21 && res_AndLogicOP_22);
    bool res_NotLogicOP_26 = true;
    res_NotLogicOP_26 = (res_NotLogicOP_26 && ! (L_P1__GetParamMainc8(my_id) == true));
    res_AndLogicOP_21 = (res_AndLogicOP_21 && res_NotLogicOP_26);
    
    if(res_AndLogicOP_21){
    bool res_AndLogicOP_27 = true;
    bool res_ImpliesLogicOp_28 = true;
    bool res_OrLogicOP_29 = false;
    bool res_NotLogicOP_30 = true;
    res_NotLogicOP_30 = (res_NotLogicOP_30 && ! (Counter_GetValore(L_P1__GetMainc39(my_id)) == 1342u));
    res_OrLogicOP_29 = (res_OrLogicOP_29 || res_NotLogicOP_30);
    bool res_AndLogicOP_31 = true;
    bool res_NotLogicOP_32 = true;
    res_NotLogicOP_32 = (res_NotLogicOP_32 && ! (argom11 == c270xx));
    res_AndLogicOP_31 = (res_AndLogicOP_31 && res_NotLogicOP_32);
    bool res_NotLogicOP_33 = true;
    res_NotLogicOP_33 = (res_NotLogicOP_33 && ! Timer_Scaduto(L_P1__GetMainc38(my_id)));
    res_AndLogicOP_31 = (res_AndLogicOP_31 && res_NotLogicOP_33);
    
    res_OrLogicOP_29 = (res_OrLogicOP_29 || res_AndLogicOP_31);
    
    if(res_OrLogicOP_29){
    bool res_AndLogicOP_34 = true;
    bool res_ImpliesLogicOp_35 = true;
    bool res_OrLogicOP_36 = false;
    bool res_AndLogicOP_37 = true;
    bool res_AndLogicOP_38 = true;
    bool res_NotLogicOP_39 = true;
    res_NotLogicOP_39 = (res_NotLogicOP_39 && ! (L_P1_C1_GetState(my_id) == C1_St_state));
    res_AndLogicOP_38 = (res_AndLogicOP_38 && res_NotLogicOP_39);
    bool res_NotLogicOP_40 = true;
    res_NotLogicOP_40 = (res_NotLogicOP_40 && ! Timer_Attivo(L_P1__GetMainc38(my_id)));
    res_AndLogicOP_38 = (res_AndLogicOP_38 && res_NotLogicOP_40);
    
    res_AndLogicOP_37 = (res_AndLogicOP_37 && res_AndLogicOP_38);
    bool res_NotLogicOP_41 = true;
    res_NotLogicOP_41 = (res_NotLogicOP_41 && ! (L_P1__GetParamMainc9(my_id) > 2u));
    res_AndLogicOP_37 = (res_AndLogicOP_37 && res_NotLogicOP_41);
    
    res_OrLogicOP_36 = (res_OrLogicOP_36 || res_AndLogicOP_37);
    bool res_NotLogicOP_42 = true;
    res_NotLogicOP_42 = (res_NotLogicOP_42 && ! (L_P1__GetParamMainc10(my_id) == gialloxverd));
    res_OrLogicOP_36 = (res_OrLogicOP_36 || res_NotLogicOP_42);
    
    if(res_OrLogicOP_36){
    bool res_AndLogicOP_43 = true;
    bool res_ImpliesLogicOp_44 = true;
    bool res_OrLogicOP_45 = false;
    bool res_OrLogicOP_46 = false;
    bool res_OrLogicOP_47 = false;
    bool res_AndLogicOP_48 = true;
    bool res_NotLogicOP_49 = true;
    bool res_NotLogicOP_50 = true;
    res_NotLogicOP_50 = (res_NotLogicOP_50 && ! (L_P1__GetInMainc5(my_id) == false));
    res_NotLogicOP_49 = (res_NotLogicOP_49 && ! res_NotLogicOP_50);
    res_AndLogicOP_48 = (res_AndLogicOP_48 && res_NotLogicOP_49);
    bool res_NotLogicOP_51 = true;
    bool res_NotLogicOP_52 = true;
    res_NotLogicOP_52 = (res_NotLogicOP_52 && ! (argom10 == true));
    res_NotLogicOP_51 = (res_NotLogicOP_51 && ! res_NotLogicOP_52);
    res_AndLogicOP_48 = (res_AndLogicOP_48 && res_NotLogicOP_51);
    
    res_OrLogicOP_47 = (res_OrLogicOP_47 || res_AndLogicOP_48);
    bool res_NotLogicOP_53 = true;
    res_NotLogicOP_53 = (res_NotLogicOP_53 && ! (Counter_GetValore(L_P1__GetMainc39(my_id)) < 13u));
    res_OrLogicOP_47 = (res_OrLogicOP_47 || res_NotLogicOP_53);
    
    res_OrLogicOP_46 = (res_OrLogicOP_46 || res_OrLogicOP_47);
    bool res_NotLogicOP_54 = true;
    res_NotLogicOP_54 = (res_NotLogicOP_54 && ! Timer_Disattivo(L_P1__GetMainc38(my_id)));
    res_OrLogicOP_46 = (res_OrLogicOP_46 || res_NotLogicOP_54);
    
    res_OrLogicOP_45 = (res_OrLogicOP_45 || res_OrLogicOP_46);
    bool res_AndLogicOP_55 = true;
    bool res_NotLogicOP_56 = true;
    res_NotLogicOP_56 = (res_NotLogicOP_56 && ! (L_P1__GetParamMainc9(my_id) == 9u));
    res_AndLogicOP_55 = (res_AndLogicOP_55 && res_NotLogicOP_56);
    res_AndLogicOP_55 = (res_AndLogicOP_55 && (L_P1__GetInMainc6(my_id) == gialloxverd));
    
    res_OrLogicOP_45 = (res_OrLogicOP_45 || res_AndLogicOP_55);
    
    if(res_OrLogicOP_45){
    bool res_XorLogicOP_57 = true;
    int xorIndex_res_XorLogicOP_57 = 0;
    bool res_ImpliesLogicOp_58 = true;
    bool res_OrLogicOP_59 = false;
    bool res_OrLogicOP_60 = false;
    bool res_OrLogicOP_61 = false;
    bool res_NotLogicOP_62 = true;
    res_NotLogicOP_62 = (res_NotLogicOP_62 && ! Timer_Scaduto(L_P1__GetMainc38(my_id)));
    res_OrLogicOP_61 = (res_OrLogicOP_61 || res_NotLogicOP_62);
    bool res_NotLogicOP_63 = true;
    res_NotLogicOP_63 = (res_NotLogicOP_63 && ! (Counter_GetValore(L_P1__GetMainc39(my_id)) == 12130u));
    res_OrLogicOP_61 = (res_OrLogicOP_61 || res_NotLogicOP_63);
    
    res_OrLogicOP_60 = (res_OrLogicOP_60 || res_OrLogicOP_61);
    bool res_AndLogicOP_64 = true;
    bool res_NotLogicOP_65 = true;
    bool res_NotLogicOP_66 = true;
    res_NotLogicOP_66 = (res_NotLogicOP_66 && ! (argom13 == true));
    res_NotLogicOP_65 = (res_NotLogicOP_65 && ! res_NotLogicOP_66);
    res_AndLogicOP_64 = (res_AndLogicOP_64 && res_NotLogicOP_65);
    bool res_NotLogicOP_67 = true;
    res_NotLogicOP_67 = (res_NotLogicOP_67 && ! (L_P1__GetInMainc6(my_id) == gialloxverd));
    res_AndLogicOP_64 = (res_AndLogicOP_64 && res_NotLogicOP_67);
    
    res_OrLogicOP_60 = (res_OrLogicOP_60 || res_AndLogicOP_64);
    
    res_OrLogicOP_59 = (res_OrLogicOP_59 || res_OrLogicOP_60);
    res_OrLogicOP_59 = (res_OrLogicOP_59 || (L_P1__GetParamMainc10(my_id) == gialloxverd));
    
    if(res_OrLogicOP_59){
    bool res_ImpliesLogicOp_68 = true;
    bool res_OrLogicOP_69 = false;
    bool res_OrLogicOP_70 = false;
    bool res_AndLogicOP_71 = true;
    bool res_AndLogicOP_72 = true;
    bool res_NotLogicOP_73 = true;
    res_NotLogicOP_73 = (res_NotLogicOP_73 && ! (Counter_GetValore(L_P1__GetMainc39(my_id)) == 155u));
    res_AndLogicOP_72 = (res_AndLogicOP_72 && res_NotLogicOP_73);
    res_AndLogicOP_72 = (res_AndLogicOP_72 && (L_P1__GetMainc27(my_id) == 3u));
    
    res_AndLogicOP_71 = (res_AndLogicOP_71 && res_AndLogicOP_72);
    bool res_NotLogicOP_74 = true;
    res_NotLogicOP_74 = (res_NotLogicOP_74 && ! (Counter_GetValore(L_P1__GetMainc39(my_id)) == 1342u));
    res_AndLogicOP_71 = (res_AndLogicOP_71 && res_NotLogicOP_74);
    
    res_OrLogicOP_70 = (res_OrLogicOP_70 || res_AndLogicOP_71);
    bool res_NotLogicOP_75 = true;
    res_NotLogicOP_75 = (res_NotLogicOP_75 && ! (Counter_GetValore(L_P1__GetMainc39(my_id)) > 151u));
    res_OrLogicOP_70 = (res_OrLogicOP_70 || res_NotLogicOP_75);
    
    res_OrLogicOP_69 = (res_OrLogicOP_69 || res_OrLogicOP_70);
    bool res_NotLogicOP_76 = true;
    bool res_NotLogicOP_77 = true;
    res_NotLogicOP_77 = (res_NotLogicOP_77 && ! (Counter_GetValore(L_P1__GetMainc39(my_id)) == 14305u));
    res_NotLogicOP_76 = (res_NotLogicOP_76 && ! res_NotLogicOP_77);
    res_OrLogicOP_69 = (res_OrLogicOP_69 || res_NotLogicOP_76);
    
    if(res_OrLogicOP_69){
    bool res_OrLogicOP_78 = false;
    bool res_OrLogicOP_79 = false;
    bool res_NotLogicOP_80 = true;
    res_NotLogicOP_80 = (res_NotLogicOP_80 && ! Timer_Attivo(L_P1__GetMainc38(my_id)));
    res_OrLogicOP_79 = (res_OrLogicOP_79 || res_NotLogicOP_80);
    res_OrLogicOP_79 = (res_OrLogicOP_79 || Timer_Scaduto(L_P1__GetMainc38(my_id)));
    
    res_OrLogicOP_78 = (res_OrLogicOP_78 || res_OrLogicOP_79);
    bool res_AndLogicOP_81 = true;
    res_AndLogicOP_81 = (res_AndLogicOP_81 && (argom13 == false));
    res_AndLogicOP_81 = (res_AndLogicOP_81 && (L_P1__GetParamMainc7(my_id) > 5u));
    
    res_OrLogicOP_78 = (res_OrLogicOP_78 || res_AndLogicOP_81);
    
    res_ImpliesLogicOp_68 = (res_ImpliesLogicOp_68 && res_OrLogicOP_78);
    }
    res_ImpliesLogicOp_58 = (res_ImpliesLogicOp_58 && res_ImpliesLogicOp_68);
    }
    if(res_ImpliesLogicOp_58){
    xorIndex_res_XorLogicOP_57 = (xorIndex_res_XorLogicOP_57 + 1);
    }
    bool res_NotLogicOP_82 = true;
    res_NotLogicOP_82 = (res_NotLogicOP_82 && ! Timer_Scaduto(L_P1__GetMainc38(my_id)));
    if(res_NotLogicOP_82){
    xorIndex_res_XorLogicOP_57 = (xorIndex_res_XorLogicOP_57 + 1);
    }
    
    res_XorLogicOP_57 = (res_XorLogicOP_57 && (xorIndex_res_XorLogicOP_57 == 1));
    res_ImpliesLogicOp_44 = (res_ImpliesLogicOp_44 && res_XorLogicOP_57);
    }
    res_AndLogicOP_43 = (res_AndLogicOP_43 && res_ImpliesLogicOp_44);
    bool res_OrLogicOP_83 = false;
    bool res_OrLogicOP_84 = false;
    bool res_OrLogicOP_85 = false;
    bool res_NotLogicOP_86 = true;
    res_NotLogicOP_86 = (res_NotLogicOP_86 && ! (argom13 == false));
    res_OrLogicOP_85 = (res_OrLogicOP_85 || res_NotLogicOP_86);
    bool res_AndLogicOP_87 = true;
    res_AndLogicOP_87 = (res_AndLogicOP_87 && (L_P1__GetInMainc6(my_id) == gialloxverd));
    res_AndLogicOP_87 = (res_AndLogicOP_87 && Timer_Attivo(L_P1__GetMainc38(my_id)));
    
    res_OrLogicOP_85 = (res_OrLogicOP_85 || res_AndLogicOP_87);
    
    res_OrLogicOP_84 = (res_OrLogicOP_84 || res_OrLogicOP_85);
    bool res_NotLogicOP_88 = true;
    bool res_NotLogicOP_89 = true;
    res_NotLogicOP_89 = (res_NotLogicOP_89 && ! (L_P1__GetMainc27(my_id) == 7u));
    res_NotLogicOP_88 = (res_NotLogicOP_88 && ! res_NotLogicOP_89);
    res_OrLogicOP_84 = (res_OrLogicOP_84 || res_NotLogicOP_88);
    
    res_OrLogicOP_83 = (res_OrLogicOP_83 || res_OrLogicOP_84);
    res_OrLogicOP_83 = (res_OrLogicOP_83 || (L_P1__GetParamMainc10(my_id) == gialloxverd));
    
    res_AndLogicOP_43 = (res_AndLogicOP_43 && res_OrLogicOP_83);
    
    res_ImpliesLogicOp_35 = (res_ImpliesLogicOp_35 && res_AndLogicOP_43);
    }
    res_AndLogicOP_34 = (res_AndLogicOP_34 && res_ImpliesLogicOp_35);
    bool res_OrLogicOP_90 = false;
    bool res_OrLogicOP_91 = false;
    bool res_AndLogicOP_92 = true;
    bool res_AndLogicOP_93 = true;
    res_AndLogicOP_93 = (res_AndLogicOP_93 && (L_P1__GetMainc27(my_id) > 3u));
    res_AndLogicOP_93 = (res_AndLogicOP_93 && (L_P1__GetInMainc5(my_id) == true));
    
    res_AndLogicOP_92 = (res_AndLogicOP_92 && res_AndLogicOP_93);
    res_AndLogicOP_92 = (res_AndLogicOP_92 && (Counter_GetValore(L_P1__GetMainc39(my_id)) == 14u));
    
    res_OrLogicOP_91 = (res_OrLogicOP_91 || res_AndLogicOP_92);
    bool res_AndLogicOP_94 = true;
    bool res_NotLogicOP_95 = true;
    res_NotLogicOP_95 = (res_NotLogicOP_95 && ! (L_P1__GetMainc27(my_id) < 5u));
    res_AndLogicOP_94 = (res_AndLogicOP_94 && res_NotLogicOP_95);
    res_AndLogicOP_94 = (res_AndLogicOP_94 && (Counter_GetValore(L_P1__GetMainc39(my_id)) < 1305u));
    
    res_OrLogicOP_91 = (res_OrLogicOP_91 || res_AndLogicOP_94);
    
    res_OrLogicOP_90 = (res_OrLogicOP_90 || res_OrLogicOP_91);
    bool res_NotLogicOP_96 = true;
    res_NotLogicOP_96 = (res_NotLogicOP_96 && ! (argom13 == true));
    res_OrLogicOP_90 = (res_OrLogicOP_90 || res_NotLogicOP_96);
    
    res_AndLogicOP_34 = (res_AndLogicOP_34 && res_OrLogicOP_90);
    
    res_ImpliesLogicOp_28 = (res_ImpliesLogicOp_28 && res_AndLogicOP_34);
    }
    res_AndLogicOP_27 = (res_AndLogicOP_27 && res_ImpliesLogicOp_28);
    bool res_OrLogicOP_97 = false;
    res_OrLogicOP_97 = (res_OrLogicOP_97 || (L_P1__GetMainc27(my_id) > 4u));
    bool res_AndLogicOP_98 = true;
    bool res_AndLogicOP_99 = true;
    res_AndLogicOP_99 = (res_AndLogicOP_99 && (L_P1__GetMainc27(my_id) < 10u));
    res_AndLogicOP_99 = (res_AndLogicOP_99 && (L_P1__GetMainc27(my_id) == 1u));
    
    res_AndLogicOP_98 = (res_AndLogicOP_98 && res_AndLogicOP_99);
    res_AndLogicOP_98 = (res_AndLogicOP_98 && (L_P1__GetInMainc6(my_id) == gialloxverd));
    
    res_OrLogicOP_97 = (res_OrLogicOP_97 || res_AndLogicOP_98);
    
    res_AndLogicOP_27 = (res_AndLogicOP_27 && res_OrLogicOP_97);
    
    res_ImpliesLogicOp_20 = (res_ImpliesLogicOp_20 && res_AndLogicOP_27);
    }
    res_OrLogicOP_19 = (res_OrLogicOP_19 || res_ImpliesLogicOp_20);
    bool res_NotLogicOP_100 = true;
    bool res_NotLogicOP_101 = true;
    res_NotLogicOP_101 = (res_NotLogicOP_101 && ! (Counter_GetValore(L_P1__GetMainc39(my_id)) == 1u));
    res_NotLogicOP_100 = (res_NotLogicOP_100 && ! res_NotLogicOP_101);
    res_OrLogicOP_19 = (res_OrLogicOP_19 || res_NotLogicOP_100);
    
    res_ImpliesLogicOp_9 = (res_ImpliesLogicOp_9 && res_OrLogicOP_19);
    }
    if(res_ImpliesLogicOp_9){
    xorIndex_res_XorLogicOP_8 = (xorIndex_res_XorLogicOP_8 + 1);
    }
    bool res_AndLogicOP_102 = true;
    bool res_AndLogicOP_103 = true;
    bool res_NotLogicOP_104 = true;
    res_NotLogicOP_104 = (res_NotLogicOP_104 && ! (L_P1__GetParamMainc9(my_id) < 4u));
    res_AndLogicOP_103 = (res_AndLogicOP_103 && res_NotLogicOP_104);
    res_AndLogicOP_103 = (res_AndLogicOP_103 && Timer_Attivo(L_P1__GetMainc38(my_id)));
    
    res_AndLogicOP_102 = (res_AndLogicOP_102 && res_AndLogicOP_103);
    bool res_NotLogicOP_105 = true;
    res_NotLogicOP_105 = (res_NotLogicOP_105 && ! (L_P1__GetInMainc6(my_id) == gialloxverd));
    res_AndLogicOP_102 = (res_AndLogicOP_102 && res_NotLogicOP_105);
    
    if(res_AndLogicOP_102){
    xorIndex_res_XorLogicOP_8 = (xorIndex_res_XorLogicOP_8 + 1);
    }
    
    res_XorLogicOP_8 = (res_XorLogicOP_8 && (xorIndex_res_XorLogicOP_8 == 1));
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_XorLogicOP_8);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *48,49,50,51,*  *,*  il timer MainClass_C1_timer_T3 sia attivo
    //   *104,* o  che  *,*  il controllo MainClass_C1_controllo_C9 sia  uguale a GialloxVerdex
    //   *104,* e  che  *,*  il contatore MainClass_C1_contatore_Co2 non sia  maggiore di  *54,* 1321
    //   *104,* o  che  *38,*  il contatore MainClass_C1_contatore_Co2 non sia  diverso da  *56,* 10
    //   *104,* o  che  *,*  la variabile MainClass_C1_variabile_V7 non sia  maggiore di  *54,* 5
    //   *104,* e  che  *35,*  il controllo MainClass_C1_controllo_C9 non sia  diverso da GialloxVerdex
    bool res_OrLogicOP_106 = false;
    bool res_OrLogicOP_107 = false;
    bool res_OrLogicOP_108 = false;
    res_OrLogicOP_108 = (res_OrLogicOP_108 || Timer_Attivo(L_P1__GetMainc38(my_id)));
    bool res_AndLogicOP_109 = true;
    res_AndLogicOP_109 = (res_AndLogicOP_109 && (L_P1__GetInMainc6(my_id) == gialloxverd));
    bool res_NotLogicOP_110 = true;
    res_NotLogicOP_110 = (res_NotLogicOP_110 && ! (Counter_GetValore(L_P1__GetMainc39(my_id)) > 1321u));
    res_AndLogicOP_109 = (res_AndLogicOP_109 && res_NotLogicOP_110);
    
    res_OrLogicOP_108 = (res_OrLogicOP_108 || res_AndLogicOP_109);
    
    res_OrLogicOP_107 = (res_OrLogicOP_107 || res_OrLogicOP_108);
    bool res_NotLogicOP_111 = true;
    bool res_NotLogicOP_112 = true;
    res_NotLogicOP_112 = (res_NotLogicOP_112 && ! (Counter_GetValore(L_P1__GetMainc39(my_id)) == 10u));
    res_NotLogicOP_111 = (res_NotLogicOP_111 && ! res_NotLogicOP_112);
    res_OrLogicOP_107 = (res_OrLogicOP_107 || res_NotLogicOP_111);
    
    res_OrLogicOP_106 = (res_OrLogicOP_106 || res_OrLogicOP_107);
    bool res_AndLogicOP_113 = true;
    bool res_NotLogicOP_114 = true;
    res_NotLogicOP_114 = (res_NotLogicOP_114 && ! (L_P1__GetMainc27(my_id) > 5u));
    res_AndLogicOP_113 = (res_AndLogicOP_113 && res_NotLogicOP_114);
    bool res_NotLogicOP_115 = true;
    bool res_NotLogicOP_116 = true;
    res_NotLogicOP_116 = (res_NotLogicOP_116 && ! (L_P1__GetInMainc6(my_id) == gialloxverd));
    res_NotLogicOP_115 = (res_NotLogicOP_115 && ! res_NotLogicOP_116);
    res_AndLogicOP_113 = (res_AndLogicOP_113 && res_NotLogicOP_115);
    
    res_OrLogicOP_106 = (res_OrLogicOP_106 || res_AndLogicOP_113);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_106);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
    
    { commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI5 non è attivo o  se l'argomento argomento_ave3 non  è  diverso da  True  commento: {39,}  commento: {37,} e  se la variabile MainClass_C1_variabile_V7 è  uguale a  commento: {53,} 6, Verifica che   commento: {47,52,}   l'argomento argomento_ave3 non  sia  uguale a  False  commento: {,} 
     commento: {104,} e  che   l'argomento argomento_ave3 non  sia  uguale a  True  commento: {39,} 
     commento: {104,} e  che   l'argomento argomento_ave3 sia  uguale a  False  commento: {39,} 
     commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P8 non sia  uguale a GialloxVerdex
    
    
    }
*/
bool L_P1__Macro7(instance_id_t const my_id , bool argom14, C1_Enumerat4 argom15)
{
bool res_AndLogicOP_0 = true;
    
    //  *110,*  se il ripristino del timer  MainClass_C1_restoreTI_TI5 non è attivo o  se l'argomento argomento_ave3 non  è  diverso da  True  *39,*  *37,* e  se la variabile MainClass_C1_variabile_V7 è  uguale a  *53,* 6, Verifica che   *47,52,*   l'argomento argomento_ave3 non  sia  uguale a  False  *,* 
    //   *104,* e  che   l'argomento argomento_ave3 non  sia  uguale a  True  *39,* 
    //   *104,* e  che   l'argomento argomento_ave3 sia  uguale a  False  *39,* 
    //   *104,* o  che  *34,*  il parametro MainClass_C1_parametro_P8 non sia  uguale a GialloxVerdex
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! Timer_Attivo(L_P1__GetMainc37(my_id)));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_3);
    bool res_AndLogicOP_4 = true;
    bool res_NotLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (argom14 == true));
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! res_NotLogicOP_6);
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_5);
    res_AndLogicOP_4 = (res_AndLogicOP_4 && (L_P1__GetMainc27(my_id) == 6u));
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_4);
    
    if(res_OrLogicOP_2){
    bool res_OrLogicOP_7 = false;
    bool res_AndLogicOP_8 = true;
    bool res_AndLogicOP_9 = true;
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (argom14 == false));
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_NotLogicOP_10);
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (argom14 == true));
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_NotLogicOP_11);
    
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_AndLogicOP_9);
    res_AndLogicOP_8 = (res_AndLogicOP_8 && (argom14 == false));
    
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_AndLogicOP_8);
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (L_P1__GetParamMainc10(my_id) == gialloxverd));
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_NotLogicOP_12);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_OrLogicOP_7);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    
    
    return res_AndLogicOP_0;
}


// Macro valorizzate

/*
    CNL corrispondente:
    
    { commento: {[}
     commento: {46,} assegna alla macro il valore c270xx commento: {],}
    }
*/
C1_Enumerat3 L_P1__Macro4(instance_id_t const my_id , C1_Enumerat2 argom2, bool argom3)
{
return c270xx;
}

/*
    CNL corrispondente:
    
    { commento: {[}
     commento: {46,} assegna alla macro il valore Rosso commento: {],}
    }
*/
C1_Enumerat1 L_P1__Macro5(instance_id_t const my_id , C1_Enumerat1 argom4, C1_Enumerat3 argom5, C1_Enumerat2 argom6, C1_Enumerat3 argom7, C1_Enumerat4 argom8)
{
return rosso;
}



