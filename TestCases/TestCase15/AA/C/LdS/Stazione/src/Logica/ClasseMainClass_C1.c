// Codice del modello 'TestCase15', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
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
	    L_P1__SetOutEvent4(my_id, LDS_MANCMD_UNEXPECTED);
    } else {
        L_P1__SetOutEvent4(my_id, LDS_MANCMD_NOOP);
    }
    if (L_P1__GetInEvent2(my_id)) {
	    L_P1__SetOutEvent5(my_id, LDS_MANCMD_UNEXPECTED);
    } else {
        L_P1__SetOutEvent5(my_id, LDS_MANCMD_NOOP);
    }
    if (L_P1__GetInEvent3(my_id)) {
	    L_P1__SetOutEvent6(my_id, LDS_MANCMD_UNEXPECTED);
    } else {
        L_P1__SetOutEvent6(my_id, LDS_MANCMD_NOOP);
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
    L_P1__SetMainc22(my_id, 0);
    L_P1__SetMainc24(my_id, giallox);
    L_P1__SetMainc26(my_id, 0);
    L_P1__SetMainc28(my_id, c180x);
    L_P1__SetMainc30(my_id, false);
    L_P1__SetMainc31(my_id, false);
    L_P1__SetMainc32(my_id, false);
    L_P1__SetMainc33(my_id, false);
    L_P1__SetMainc34(my_id, false);
    L_P1__SetMainc35(my_id, false);
    L_P1__SetMainc36(my_id, rossogiallo2);
    L_P1__SetMainc37(my_id, rossogiallo2);
    L_P1__SetMainc38(my_id, false);
    L_P1__SetMainc39(my_id, false);
    L_P1__SetStato1(my_id, C1_St_Stato);
    // init controlli precedenti
    L_P1__SetMainc15(my_id, avanzamento);
    L_P1__SetMainc17(my_id, false);
    L_P1__SetMainc19(my_id, true);
    L_P1__SetMainc21(my_id, rossogiallo3);
    // init Timer e Counter
    Timer_AggmInit(L_P1__GetMainc40(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc40_ID);
    Timer_Init(L_P1__GetMainc40(my_id), 20254000);
    Timer_AggmInit(L_P1__GetMainc41(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc41_ID);
    Timer_Init(L_P1__GetMainc41(my_id), 20254000);
    Timer_AggmInit(L_P1__GetMainc42(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc42_ID);
    Timer_Init(L_P1__GetMainc42(my_id), 113000);
    Timer_AggmInit(L_P1__GetMainc43(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc43_ID);
    Timer_Init(L_P1__GetMainc43(my_id), 113000);
    Timer_AggmInit(L_P1__GetMainc44(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc44_ID);
    Timer_Init(L_P1__GetMainc44(my_id), 1000);
    Timer_AggmInit(L_P1__GetMainc45(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc45_ID);
    Timer_Init(L_P1__GetMainc45(my_id), 1000);
    Timer_AggmInit(L_P1__GetMainc46(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc46_ID);
    Timer_Init(L_P1__GetMainc46(my_id), 4000);
    Timer_AggmInit(L_P1__GetMainc47(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc47_ID);
    Timer_Init(L_P1__GetMainc47(my_id), 4000);
    Timer_AggmInit(L_P1__GetMainc48(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc48_ID);
    Timer_Init(L_P1__GetMainc48(my_id), 413000);
    Timer_AggmInit(L_P1__GetMainc49(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc49_ID);
    Timer_Init(L_P1__GetMainc49(my_id), 330000);
    Timer_AggmInit(L_P1__GetMainc50(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc50_ID);
    Timer_Init(L_P1__GetMainc50(my_id), 3254000);
    Counter_AggmInit(L_P1__GetMainc51(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc51_ID);
    Counter_Init(L_P1__GetMainc51(my_id));
    Counter_AggmInit(L_P1__GetMainc52(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc52_ID);
    Counter_Init(L_P1__GetMainc52(my_id));
    Counter_AggmInit(L_P1__GetMainc53(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc53_ID);
    Counter_Init(L_P1__GetMainc53(my_id));
    Counter_AggmInit(L_P1__GetMainc54(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc54_ID);
    Counter_Init(L_P1__GetMainc54(my_id));
    Counter_AggmInit(L_P1__GetMainc55(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc55_ID);
    Counter_Init(L_P1__GetMainc55(my_id));
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
    L_P1__SetMainc23(my_id, L_P1__GetMainc22(my_id));
    L_P1__SetMainc25(my_id, L_P1__GetMainc24(my_id));
    L_P1__SetMainc27(my_id, L_P1__GetMainc26(my_id));
    L_P1__SetMainc29(my_id, L_P1__GetMainc28(my_id));
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
    Timer_Exec(L_P1__GetMainc40(my_id));
    Timer_Exec(L_P1__GetMainc41(my_id));
    Timer_Exec(L_P1__GetMainc42(my_id));
    Timer_Exec(L_P1__GetMainc43(my_id));
    Timer_Exec(L_P1__GetMainc44(my_id));
    Timer_Exec(L_P1__GetMainc45(my_id));
    Timer_Exec(L_P1__GetMainc46(my_id));
    Timer_Exec(L_P1__GetMainc47(my_id));
    Timer_Exec(L_P1__GetMainc48(my_id));
    Timer_Exec(L_P1__GetMainc49(my_id));
    Timer_Exec(L_P1__GetMainc50(my_id));
}

void L_P1_C1_GSetSafe(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C1(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C1(proc_id);
    L_P1__SetOutMainc(my_id, false);
    L_P1__SetOutMainc1(my_id, true);
    L_P1__SetOutMainc2(my_id, rossogiallo3);
    L_P1__SetOutMainc3(my_id, rossogiallo1);
    L_P1__SetOutMainc4(my_id, false);
}

void L_P1_C1_GUpdatePrev(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C1(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C1(proc_id);
    L_P1__SetMainc15(my_id, L_P1__GetInMainc14(my_id));
    L_P1__SetMainc17(my_id, L_P1__GetInMainc16(my_id));
    L_P1__SetMainc19(my_id, L_P1__GetInMainc18(my_id));
    L_P1__SetMainc21(my_id, L_P1__GetInMainc20(my_id));
    L_P1__SetMainc23(my_id, L_P1__GetMainc22(my_id));
    L_P1__SetMainc25(my_id, L_P1__GetMainc24(my_id));
    L_P1__SetMainc27(my_id, L_P1__GetMainc26(my_id));
    L_P1__SetMainc29(my_id, L_P1__GetMainc28(my_id));
}

// ********** Definizione macro **********

// Macro di effetto

/*
    CNL corrispondente:
    
    { commento: {38,}  se il contatore MainClass_C1_contatore_Co6 non è  diverso da  commento: {56,} 14, commento: {66,} Assegna al comando MainClass_C1_comando_C10 il valore  False 
    
       
     commento: {35,}  se il controllo MainClass_C1_controllo_C3 è  diverso da  True  o  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} e  se il timer MainClass_C1_timer_T2 non è attivo,  Applica gli effetti
           della macro MainClass_C1_macroef_M9  commento: {73,}
    
     ,altrimenti  commento: {66,} Assegna al comando MainClass_C1_comando_C5 il valore RossoGiallox
    
    
     commento: {34,}  se lo stato  è  diverso da  commento: {56,}  state1  commento: {106,} commento: {36,} o  se il timer MainClass_C1_timer_T2 non è scaduto commento: {35,} o  se il controllo MainClass_C1_controllo_C3 è  uguale a  False  commento: {34,} e  se il parametro MainClass_C1_parametro_P8 è  maggiore di  commento: {54,} 2, commento: {71,}Decrementa il contatore MainClass_C1_contatore_Co6
    
     ,altrimenti   Applica gli effetti
           della macro MainClass_C1_macroef_M9  commento: {73,}
    
    
      se il ripristino dello stato  è  diverso da  commento: {56,}  state1  commento: {107,}, commento: {71,}Decrementa il contatore MainClass_C1_contatore_Co10
    
     ,altrimenti  commento: {66,} Assegna al comando MainClass_C1_comando_C5 il valore RossoGiallox
    
    
     commento: {36,}  se il timer MainClass_C1_timer_T2 non è scaduto commento: {37,} o  se la variabile MainClass_C1_variabile_V10 è  diverso da  False  commento: {36,} e  se il timer MainClass_C1_timer_T10 non è disattivo, commento: {66,} Assegna al comando MainClass_C1_comando_C5 il valore RossoGiallox
    
       
    
    }
*/
void L_P1__Macro(instance_id_t const my_id )
{
//  *38,*  se il contatore MainClass_C1_contatore_Co6 non è  diverso da  *56,* 14, *66,* Assegna al comando MainClass_C1_comando_C10 il valore  False
    bool res_NotLogicOP_0 = true;
    bool res_NotLogicOP_1 = true;
    res_NotLogicOP_1 = (res_NotLogicOP_1 && ! (Counter_GetValore(L_P1__GetMainc53(my_id)) == 14u));
    res_NotLogicOP_0 = (res_NotLogicOP_0 && ! res_NotLogicOP_1);
    if(res_NotLogicOP_0){
    
    L_P1__SetOutMainc(my_id,false);
    }
    //  *35,*  se il controllo MainClass_C1_controllo_C3 è  diverso da  True  o  se il controllo ConsDef  è  uguale a FALSE  *36,* e  se il timer MainClass_C1_timer_T2 non è attivo,  Applica gli effetti
    //       della macro MainClass_C1_macroef_M9  *73,*
    // ,altrimenti  *66,* Assegna al comando MainClass_C1_comando_C5 il valore RossoGiallox
    bool res_OrLogicOP_2 = false;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__GetInMainc6(my_id) == true));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_3);
    bool res_AndLogicOP_4 = true;
    res_AndLogicOP_4 = (res_AndLogicOP_4 && (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! Timer_Attivo(L_P1__GetMainc49(my_id)));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_5);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_4);
    
    if(res_OrLogicOP_2){
    
    L_P1__Macro1(my_id);
    }else{
    
    L_P1__SetOutMainc2(my_id,rossogiallo3);
    }
    //  *34,*  se lo stato  è  diverso da  *56,*  state1  *106,* *36,* o  se il timer MainClass_C1_timer_T2 non è scaduto *35,* o  se il controllo MainClass_C1_controllo_C3 è  uguale a  False  *34,* e  se il parametro MainClass_C1_parametro_P8 è  maggiore di  *54,* 2, *71,*Decrementa il contatore MainClass_C1_contatore_Co6
    // ,altrimenti   Applica gli effetti
    //       della macro MainClass_C1_macroef_M9
    bool res_OrLogicOP_6 = false;
    bool res_OrLogicOP_7 = false;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1_C1_GetState(my_id) == C1_St_state));
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_NotLogicOP_8);
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! Timer_Scaduto(L_P1__GetMainc49(my_id)));
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_NotLogicOP_9);
    
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_OrLogicOP_7);
    bool res_AndLogicOP_10 = true;
    res_AndLogicOP_10 = (res_AndLogicOP_10 && (L_P1__GetInMainc6(my_id) == false));
    res_AndLogicOP_10 = (res_AndLogicOP_10 && (L_P1__GetParamMainc12(my_id) > 2u));
    
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_AndLogicOP_10);
    
    if(res_OrLogicOP_6){
    
    Counter_Decr(L_P1__GetMainc53(my_id));
    }else{
    
    L_P1__Macro1(my_id);
    }
    //  *73,*
    //  se il ripristino dello stato  è  diverso da  *56,*  state1  *107,*, *71,*Decrementa il contatore MainClass_C1_contatore_Co10
    // ,altrimenti  *66,* Assegna al comando MainClass_C1_comando_C5 il valore RossoGiallox
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (L_P1__GetStato1(my_id) == C1_St_state));
    if(res_NotLogicOP_11){
    
    Counter_Decr(L_P1__GetMainc51(my_id));
    }else{
    
    L_P1__SetOutMainc2(my_id,rossogiallo3);
    }
    //  *36,*  se il timer MainClass_C1_timer_T2 non è scaduto *37,* o  se la variabile MainClass_C1_variabile_V10 è  diverso da  False  *36,* e  se il timer MainClass_C1_timer_T10 non è disattivo, *66,* Assegna al comando MainClass_C1_comando_C5 il valore RossoGiallox
    bool res_OrLogicOP_12 = false;
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! Timer_Scaduto(L_P1__GetMainc49(my_id)));
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_NotLogicOP_13);
    bool res_AndLogicOP_14 = true;
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (L_P1__GetMainc38(my_id) == false));
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_NotLogicOP_15);
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! Timer_Disattivo(L_P1__GetMainc48(my_id)));
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_NotLogicOP_16);
    
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_AndLogicOP_14);
    
    if(res_OrLogicOP_12){
    
    L_P1__SetOutMainc2(my_id,rossogiallo3);
    }
}

/*
    CNL corrispondente:
    
    { commento: {34,}  se lo stato  non è  uguale a  commento: {53,}  state1  commento: {106,} commento: {35,} o  se il controllo MainClass_C1_controllo_C3 è  diverso da  False  commento: {38,} o  se il contatore MainClass_C1_contatore_Co7 non è  minore di  commento: {55,} 122 commento: {34,} o  se il parametro MainClass_C1_parametro_P8 è  uguale a  commento: {53,} 1 commento: {34,} o  se il parametro MainClass_C1_parametro_P9 non è  diverso da RossoGialloxVerdex commento: {37,} e  se la variabile MainClass_C1_variabile_V10 è  uguale a  True , commento: {72,}Azzera il contatore MainClass_C1_contatore_Co6
    
       
     commento: {34,}  se lo stato  non è  uguale a  commento: {53,}  state1  commento: {106,}, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V9 il valore  False 
    
       
    
    }
*/
void L_P1__Macro1(instance_id_t const my_id )
{
//  *34,*  se lo stato  non è  uguale a  *53,*  state1  *106,* *35,* o  se il controllo MainClass_C1_controllo_C3 è  diverso da  False  *38,* o  se il contatore MainClass_C1_contatore_Co7 non è  minore di  *55,* 122 *34,* o  se il parametro MainClass_C1_parametro_P8 è  uguale a  *53,* 1 *34,* o  se il parametro MainClass_C1_parametro_P9 non è  diverso da RossoGialloxVerdex *37,* e  se la variabile MainClass_C1_variabile_V10 è  uguale a  True , *72,*Azzera il contatore MainClass_C1_contatore_Co6
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1_C1_GetState(my_id) == C1_St_state));
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_NotLogicOP_4);
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetInMainc6(my_id) == false));
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_NotLogicOP_5);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (Counter_GetValore(L_P1__GetMainc54(my_id)) < 122u));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_6);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_OrLogicOP_2);
    res_OrLogicOP_1 = (res_OrLogicOP_1 || (L_P1__GetParamMainc12(my_id) == 1u));
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_AndLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetParamMainc13(my_id) == rossogiallo1));
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! res_NotLogicOP_9);
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_8);
    res_AndLogicOP_7 = (res_AndLogicOP_7 && (L_P1__GetMainc38(my_id) == true));
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_7);
    
    if(res_OrLogicOP_0){
    
    Counter_Res(L_P1__GetMainc53(my_id));
    }
    //  *34,*  se lo stato  non è  uguale a  *53,*  state1  *106,*, *67,* Assegna alla variabile MainClass_C1_variabile_V9 il valore  False
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1_C1_GetState(my_id) == C1_St_state));
    if(res_NotLogicOP_10){
    
    L_P1__SetMainc39(my_id,false);
    }
}


// Macro di verifica

/*
    CNL corrispondente:
     
    {  se il ripristino dello stato  non è  diverso da  commento: {56,}  state1  commento: {107,} commento: {38,} e  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  commento: {53,} 131 commento: {37,} o  se la variabile MainClass_C1_variabile_V9 è  uguale a  True  commento: {34,} o  se il parametro MainClass_C1_parametro_P8 non è  diverso da  commento: {56,} 7 o  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} e  se la variabile MainClass_C1_variabile_V9 non è  diverso da  False , Verifica che   commento: {48,49,50,51,}  commento: {,}  la variabile MainClass_C1_variabile_V10 sia  diverso da  True 
     commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C8 non sia  diverso da  False 
     commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T2 sia attivo
     commento: {104,} o  che  commento: {,}  il contatore MainClass_C1_contatore_Co6 sia  maggiore di  commento: {54,} 1130
    
    
    }
*/
bool L_P1__Macro7(instance_id_t const my_id )
{
bool res_AndLogicOP_0 = true;
    
    //  se il ripristino dello stato  non è  diverso da  *56,*  state1  *107,* *38,* e  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  *53,* 131 *37,* o  se la variabile MainClass_C1_variabile_V9 è  uguale a  True  *34,* o  se il parametro MainClass_C1_parametro_P8 non è  diverso da  *56,* 7 o  se il controllo ConsDef  è  uguale a FALSE  *37,* e  se la variabile MainClass_C1_variabile_V9 non è  diverso da  False , Verifica che   *48,49,50,51,*  *,*  la variabile MainClass_C1_variabile_V10 sia  diverso da  True 
    //   *104,* o  che  *,*  il controllo MainClass_C1_controllo_C8 non sia  diverso da  False 
    //   *104,* e  che  *,*  il timer MainClass_C1_timer_T2 sia attivo
    //   *104,* o  che  *,*  il contatore MainClass_C1_contatore_Co6 sia  maggiore di  *54,* 1130
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_OrLogicOP_4 = false;
    bool res_AndLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetStato1(my_id) == C1_St_state));
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! res_NotLogicOP_7);
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_6);
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (Counter_GetValore(L_P1__GetMainc54(my_id)) == 131u));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_8);
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_AndLogicOP_5);
    res_OrLogicOP_4 = (res_OrLogicOP_4 || (L_P1__GetMainc39(my_id) == true));
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_OrLogicOP_4);
    bool res_NotLogicOP_9 = true;
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__GetParamMainc12(my_id) == 7u));
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! res_NotLogicOP_10);
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_NotLogicOP_9);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    bool res_AndLogicOP_11 = true;
    res_AndLogicOP_11 = (res_AndLogicOP_11 && (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_12 = true;
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (L_P1__GetMainc39(my_id) == false));
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! res_NotLogicOP_13);
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_NotLogicOP_12);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_11);
    
    if(res_OrLogicOP_2){
    bool res_OrLogicOP_14 = false;
    bool res_OrLogicOP_15 = false;
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (L_P1__GetMainc38(my_id) == true));
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_NotLogicOP_16);
    bool res_AndLogicOP_17 = true;
    bool res_NotLogicOP_18 = true;
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (L_P1__GetInMainc8(my_id) == false));
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! res_NotLogicOP_19);
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_NotLogicOP_18);
    res_AndLogicOP_17 = (res_AndLogicOP_17 && Timer_Attivo(L_P1__GetMainc49(my_id)));
    
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_AndLogicOP_17);
    
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_OrLogicOP_15);
    res_OrLogicOP_14 = (res_OrLogicOP_14 || (Counter_GetValore(L_P1__GetMainc53(my_id)) > 1130u));
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_OrLogicOP_14);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
     
    { commento: {63,}  se la macro  MainClass_C1_macrova_M7 ( con argomento_a4   uguale a True ,argomento_a7   uguale a RossoGialloGiallo ,argomento_a1   uguale a Giallox ,argomento_a3   uguale a c180x ,argomento_a6   uguale a RossoGiallo  e argomento_a5   uguale a c180x )   è  diverso da RossoGialloGiallo commento: {40,}  commento: {34,} e  se il parametro MainClass_C1_parametro_P8 non è  maggiore di  commento: {54,} 4 commento: {37,} o  se la variabile MainClass_C1_variabile_V9 non è  diverso da  True  commento: {38,} o  se il contatore MainClass_C1_contatore_Co6 non è  uguale a  commento: {53,} 1202 commento: {36,} e  se il timer MainClass_C1_timer_T10 è disattivo commento: {36,} e  se il timer MainClass_C1_timer_T2 non è scaduto, Solo una delle seguenti { 
     commento: {35,}  se il controllo MainClass_C1_controllo_C3 è  uguale a  False  commento: {36,} e  se il timer MainClass_C1_timer_T10 non è scaduto o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   commento: {47,48,49,}  commento: {34,}  il parametro MainClass_C1_parametro_P4 sia  uguale a RossoGialloxVerdex
     commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T2 sia attivo
     commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C3 non sia  diverso da  True 
     commento: {104,} o  che  commento: {36,}  il timer MainClass_C1_timer_T9 non sia disattivo
    
    
     } Verifica che   commento: {47,51,}  commento: {34,}  il parametro MainClass_C1_parametro_P4 sia  diverso da RossoGialloxVerdex
     commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co8 sia  minore di  commento: {55,} 14
    
    
    }
*/
bool L_P1__Macro8(instance_id_t const my_id )
{
bool res_AndLogicOP_0 = true;
    
    //  *63,*  se la macro  MainClass_C1_macrova_M7 ( con argomento_a4   uguale a True ,argomento_a7   uguale a RossoGialloGiallo ,argomento_a1   uguale a Giallox ,argomento_a3   uguale a c180x ,argomento_a6   uguale a RossoGiallo  e argomento_a5   uguale a c180x )   è  diverso da RossoGialloGiallo *40,*  *34,* e  se il parametro MainClass_C1_parametro_P8 non è  maggiore di  *54,* 4 *37,* o  se la variabile MainClass_C1_variabile_V9 non è  diverso da  True  *38,* o  se il contatore MainClass_C1_contatore_Co6 non è  uguale a  *53,* 1202 *36,* e  se il timer MainClass_C1_timer_T10 è disattivo *36,* e  se il timer MainClass_C1_timer_T2 non è scaduto, Solo una delle seguenti { 
    //   *35,*  se il controllo MainClass_C1_controllo_C3 è  uguale a  False  *36,* e  se il timer MainClass_C1_timer_T10 non è scaduto o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   *47,48,49,*  *34,*  il parametro MainClass_C1_parametro_P4 sia  uguale a RossoGialloxVerdex
    //   *104,* o  che  *,*  il timer MainClass_C1_timer_T2 sia attivo
    //   *104,* o  che   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* e  che  *,*  il controllo MainClass_C1_controllo_C3 non sia  diverso da  True 
    //   *104,* o  che  *36,*  il timer MainClass_C1_timer_T9 non sia disattivo
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_AndLogicOP_4 = true;
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__Macro6(my_id,giallox,c180x,true,c180x,rossogiallo2,rossogiallo) == rossogiallo));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_5);
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetParamMainc12(my_id) > 4u));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_6);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_AndLogicOP_4);
    bool res_NotLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetMainc39(my_id) == true));
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! res_NotLogicOP_8);
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_NotLogicOP_7);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    bool res_AndLogicOP_9 = true;
    bool res_AndLogicOP_10 = true;
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (Counter_GetValore(L_P1__GetMainc53(my_id)) == 1202u));
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_NotLogicOP_11);
    res_AndLogicOP_10 = (res_AndLogicOP_10 && Timer_Disattivo(L_P1__GetMainc48(my_id)));
    
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_AndLogicOP_10);
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! Timer_Scaduto(L_P1__GetMainc49(my_id)));
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_NotLogicOP_12);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_9);
    
    if(res_OrLogicOP_2){
    bool res_ImpliesLogicOp_13 = true;
    bool res_OrLogicOP_14 = false;
    bool res_AndLogicOP_15 = true;
    res_AndLogicOP_15 = (res_AndLogicOP_15 && (L_P1__GetInMainc6(my_id) == false));
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! Timer_Scaduto(L_P1__GetMainc48(my_id)));
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_NotLogicOP_16);
    
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_AndLogicOP_15);
    res_OrLogicOP_14 = (res_OrLogicOP_14 || (L_P1__GetInConsd(my_id) == false));
    
    if(res_OrLogicOP_14){
    bool res_OrLogicOP_17 = false;
    bool res_OrLogicOP_18 = false;
    bool res_OrLogicOP_19 = false;
    res_OrLogicOP_19 = (res_OrLogicOP_19 || (L_P1__GetParamMainc11(my_id) == rossogiallo1));
    res_OrLogicOP_19 = (res_OrLogicOP_19 || Timer_Attivo(L_P1__GetMainc49(my_id)));
    
    res_OrLogicOP_18 = (res_OrLogicOP_18 || res_OrLogicOP_19);
    bool res_AndLogicOP_20 = true;
    res_AndLogicOP_20 = (res_AndLogicOP_20 && (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_21 = true;
    bool res_NotLogicOP_22 = true;
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! (L_P1__GetInMainc6(my_id) == true));
    res_NotLogicOP_21 = (res_NotLogicOP_21 && ! res_NotLogicOP_22);
    res_AndLogicOP_20 = (res_AndLogicOP_20 && res_NotLogicOP_21);
    
    res_OrLogicOP_18 = (res_OrLogicOP_18 || res_AndLogicOP_20);
    
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_OrLogicOP_18);
    bool res_NotLogicOP_23 = true;
    res_NotLogicOP_23 = (res_NotLogicOP_23 && ! Timer_Disattivo(L_P1__GetMainc50(my_id)));
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_NotLogicOP_23);
    
    res_ImpliesLogicOp_13 = (res_ImpliesLogicOp_13 && res_OrLogicOP_17);
    }
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_ImpliesLogicOp_13);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *47,51,*  *34,*  il parametro MainClass_C1_parametro_P4 sia  diverso da RossoGialloxVerdex
    //   *104,* e  che  *,*  il contatore MainClass_C1_contatore_Co8 sia  minore di  *55,* 14
    bool res_AndLogicOP_24 = true;
    bool res_NotLogicOP_25 = true;
    res_NotLogicOP_25 = (res_NotLogicOP_25 && ! (L_P1__GetParamMainc11(my_id) == rossogiallo1));
    res_AndLogicOP_24 = (res_AndLogicOP_24 && res_NotLogicOP_25);
    res_AndLogicOP_24 = (res_AndLogicOP_24 && (Counter_GetValore(L_P1__GetMainc55(my_id)) < 14u));
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_AndLogicOP_24);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
     
    { commento: {36,}  se il timer MainClass_C1_timer_T2 è attivo e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   commento: {48,51,}  commento: {,}  il contatore MainClass_C1_contatore_Co6 non sia  maggiore di  commento: {54,} 13
     commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
    
    
    }
*/
bool L_P1__Macro9(instance_id_t const my_id )
{
bool res_AndLogicOP_0 = true;
    
    //  *36,*  se il timer MainClass_C1_timer_T2 è attivo e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   *48,51,*  *,*  il contatore MainClass_C1_contatore_Co6 non sia  maggiore di  *54,* 13
    //   *104,* e  che   il controllo ConsDef  sia  uguale a FALSE
    bool res_ImpliesLogicOp_1 = true;
    bool res_AndLogicOP_2 = true;
    res_AndLogicOP_2 = (res_AndLogicOP_2 && Timer_Attivo(L_P1__GetMainc49(my_id)));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && (L_P1__GetInConsd(my_id) == false));
    
    if(res_AndLogicOP_2){
    bool res_AndLogicOP_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (Counter_GetValore(L_P1__GetMainc53(my_id)) > 13u));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_4);
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (L_P1__GetInConsd(my_id) == false));
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_AndLogicOP_3);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
     
    { commento: {61,} commento: {34,}  se il parametro MainClass_C1_parametro_P4 è  uguale a RossoGialloxVerdex commento: {37,} e  se la variabile MainClass_C1_variabile_V10 è  diverso da  False  commento: {37,} e  se la variabile MainClass_C1_variabile_V9 è  uguale a  True  commento: {36,} e  se il timer MainClass_C1_timer_T10 non è scaduto commento: {36,} o  se il timer MainClass_C1_timer_T10 è scaduto commento: {35,} o  se il controllo MainClass_C1_controllo_C3 non è  uguale a  True , Tutte le seguenti { 
     commento: {63,}  se il controllo ConsDef è uguale a FALSE , Solo una delle seguenti { 
     commento: {61,}  se la macro  MainClass_C1_macrova_M3 ( con argomento_a6   uguale a True ,argomento_a5   uguale a RossoGiallox  e argomento_a10   uguale a avvio )   è  diverso da  False  commento: {40,}  commento: {38,} e  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  commento: {53,} 131 commento: {36,} o  se il timer MainClass_C1_timer_T10 non è disattivo commento: {38,} o  se il contatore MainClass_C1_contatore_Co6 non è  minore di  commento: {55,} 11 commento: {37,} o  se la variabile MainClass_C1_variabile_V9 è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
     commento: {63,} commento: {34,}  se il parametro MainClass_C1_parametro_P2 è  uguale a RossoGialloGiallo, Solo una delle seguenti { 
     commento: {62,}  se la macro  MainClass_C1_macrova_M3 ( con argomento_a6   uguale a True ,argomento_a5   uguale a RossoGiallox  e argomento_a10   uguale a avvio )  non  è  uguale a  True  commento: {40,}  o  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro MainClass_C1_parametro_P9 è  uguale a RossoGialloxVerdex commento: {36,} o  se il timer MainClass_C1_timer_T2 non è scaduto commento: {38,} e  se il contatore MainClass_C1_contatore_Co5 non è  diverso da  commento: {56,} 14, Almeno una delle seguenti { 
     commento: {62,} commento: {36,}  se il timer MainClass_C1_timer_T2 è disattivo commento: {36,} e  se il timer MainClass_C1_timer_T2 è attivo commento: {38,} e  se il contatore MainClass_C1_contatore_Co5 non è  minore di  commento: {55,} 11 commento: {36,} o  se il timer MainClass_C1_timer_T9 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
     commento: {35,}  se il controllo MainClass_C1_controllo_C6 è  uguale a  True , Verifica che   commento: {48,50,51,}  commento: {,}  la variabile MainClass_C1_variabile_V9 sia  diverso da  True 
     commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co6 non sia  uguale a  commento: {53,} 1130
     commento: {104,} e  che  commento: {38,}  il contatore MainClass_C1_contatore_Co6 non sia  maggiore di  commento: {54,} 11
     commento: {104,} o  che  commento: {38,}  il contatore MainClass_C1_contatore_Co10 non sia  maggiore di  commento: {54,} 13254
     commento: {104,} o  che  commento: {37,}  la variabile MainClass_C1_variabile_V10 sia  diverso da  False 
    
    
     } Verifica che   commento: {47,49,51,}  commento: {,}  il timer MainClass_C1_timer_T9 sia scaduto
     commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P8 non sia  uguale a  commento: {53,} 8
     commento: {104,} o  che  commento: {,}  il contatore MainClass_C1_contatore_Co6 sia  uguale a  commento: {53,} 13
     commento: {104,} o  che  commento: {38,}  il contatore MainClass_C1_contatore_Co6 sia  maggiore di  commento: {54,} 125
    
    
     } Verifica che   commento: {47,49,51,}  commento: {,}  il timer MainClass_C1_timer_T10 non sia attivo
     commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co7 non sia  diverso da  commento: {56,} 11
     commento: {104,} e  che  commento: {36,}  il timer MainClass_C1_timer_T2 sia scaduto
     commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P9 non sia  diverso da RossoGialloxVerdex
    
    
     } Verifica che   commento: {47,48,51,}   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C3 non sia  uguale a  False 
     commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P8 non sia  uguale a  commento: {53,} 4
     commento: {104,} o  che  commento: {,}  il contatore MainClass_C1_contatore_Co7 non sia  minore di  commento: {55,} 133
    
    
     } Verifica che   commento: {48,49,51,}  commento: {,}  il contatore MainClass_C1_contatore_Co7 non sia  diverso da  commento: {56,} 13025
     commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T2 sia attivo
     commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C3 sia  diverso da  False 
     commento: {104,} e  che  commento: {36,}  il timer MainClass_C1_timer_T10 non sia disattivo
    
    
     } Verifica che   commento: {47,49,51,}  commento: {,}  il contatore MainClass_C1_contatore_Co7 non sia  uguale a  commento: {53,} 15
     commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T9 sia attivo
     commento: {104,} e  che  commento: {38,}  il contatore MainClass_C1_contatore_Co10 non sia  minore di  commento: {55,} 113
     commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P4 sia  diverso da RossoGialloxVerdex
    
    
     } Verifica che   commento: {48,49,50,}  commento: {,}  il timer MainClass_C1_timer_T10 sia disattivo
     commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V10 sia  diverso da  True 
     commento: {104,} o  che  commento: {37,}  la variabile MainClass_C1_variabile_V10 sia  uguale a  True 
     commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C3 sia  uguale a  False 
    
    
    }
*/
bool L_P1__Macro10(instance_id_t const my_id )
{
bool res_AndLogicOP_0 = true;
    
    //  *61,* *34,*  se il parametro MainClass_C1_parametro_P4 è  uguale a RossoGialloxVerdex *37,* e  se la variabile MainClass_C1_variabile_V10 è  diverso da  False  *37,* e  se la variabile MainClass_C1_variabile_V9 è  uguale a  True  *36,* e  se il timer MainClass_C1_timer_T10 non è scaduto *36,* o  se il timer MainClass_C1_timer_T10 è scaduto *35,* o  se il controllo MainClass_C1_controllo_C3 non è  uguale a  True , Tutte le seguenti { 
    //   *63,*  se il controllo ConsDef è uguale a FALSE , Solo una delle seguenti { 
    //   *61,*  se la macro  MainClass_C1_macrova_M3 ( con argomento_a6   uguale a True ,argomento_a5   uguale a RossoGiallox  e argomento_a10   uguale a avvio )   è  diverso da  False  *40,*  *38,* e  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  *53,* 131 *36,* o  se il timer MainClass_C1_timer_T10 non è disattivo *38,* o  se il contatore MainClass_C1_contatore_Co6 non è  minore di  *55,* 11 *37,* o  se la variabile MainClass_C1_variabile_V9 è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
    //   *63,* *34,*  se il parametro MainClass_C1_parametro_P2 è  uguale a RossoGialloGiallo, Solo una delle seguenti { 
    //   *62,*  se la macro  MainClass_C1_macrova_M3 ( con argomento_a6   uguale a True ,argomento_a5   uguale a RossoGiallox  e argomento_a10   uguale a avvio )  non  è  uguale a  True  *40,*  o  se il controllo ConsDef  è  uguale a FALSE  *34,* e  se il parametro MainClass_C1_parametro_P9 è  uguale a RossoGialloxVerdex *36,* o  se il timer MainClass_C1_timer_T2 non è scaduto *38,* e  se il contatore MainClass_C1_contatore_Co5 non è  diverso da  *56,* 14, Almeno una delle seguenti { 
    //   *62,* *36,*  se il timer MainClass_C1_timer_T2 è disattivo *36,* e  se il timer MainClass_C1_timer_T2 è attivo *38,* e  se il contatore MainClass_C1_contatore_Co5 non è  minore di  *55,* 11 *36,* o  se il timer MainClass_C1_timer_T9 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
    //   *35,*  se il controllo MainClass_C1_controllo_C6 è  uguale a  True , Verifica che   *48,50,51,*  *,*  la variabile MainClass_C1_variabile_V9 sia  diverso da  True 
    //   *104,* e  che   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* e  che  *,*  il contatore MainClass_C1_contatore_Co6 non sia  uguale a  *53,* 1130
    //   *104,* e  che  *38,*  il contatore MainClass_C1_contatore_Co6 non sia  maggiore di  *54,* 11
    //   *104,* o  che  *38,*  il contatore MainClass_C1_contatore_Co10 non sia  maggiore di  *54,* 13254
    //   *104,* o  che  *37,*  la variabile MainClass_C1_variabile_V10 sia  diverso da  False 
    //   } Verifica che   *47,49,51,*  *,*  il timer MainClass_C1_timer_T9 sia scaduto
    //   *104,* e  che  *34,*  il parametro MainClass_C1_parametro_P8 non sia  uguale a  *53,* 8
    //   *104,* o  che  *,*  il contatore MainClass_C1_contatore_Co6 sia  uguale a  *53,* 13
    //   *104,* o  che  *38,*  il contatore MainClass_C1_contatore_Co6 sia  maggiore di  *54,* 125
    //   } Verifica che   *47,49,51,*  *,*  il timer MainClass_C1_timer_T10 non sia attivo
    //   *104,* e  che  *,*  il contatore MainClass_C1_contatore_Co7 non sia  diverso da  *56,* 11
    //   *104,* e  che  *36,*  il timer MainClass_C1_timer_T2 sia scaduto
    //   *104,* e  che  *34,*  il parametro MainClass_C1_parametro_P9 non sia  diverso da RossoGialloxVerdex
    //   } Verifica che   *47,48,51,*   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* e  che   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* e  che  *,*  il controllo MainClass_C1_controllo_C3 non sia  uguale a  False 
    //   *104,* e  che  *34,*  il parametro MainClass_C1_parametro_P8 non sia  uguale a  *53,* 4
    //   *104,* o  che  *,*  il contatore MainClass_C1_contatore_Co7 non sia  minore di  *55,* 133
    //   } Verifica che   *48,49,51,*  *,*  il contatore MainClass_C1_contatore_Co7 non sia  diverso da  *56,* 13025
    //   *104,* e  che  *,*  il timer MainClass_C1_timer_T2 sia attivo
    //   *104,* e  che  *,*  il controllo MainClass_C1_controllo_C3 sia  diverso da  False 
    //   *104,* e  che  *36,*  il timer MainClass_C1_timer_T10 non sia disattivo
    //   } Verifica che   *47,49,51,*  *,*  il contatore MainClass_C1_contatore_Co7 non sia  uguale a  *53,* 15
    //   *104,* e  che  *,*  il timer MainClass_C1_timer_T9 sia attivo
    //   *104,* e  che  *38,*  il contatore MainClass_C1_contatore_Co10 non sia  minore di  *55,* 113
    //   *104,* o  che  *34,*  il parametro MainClass_C1_parametro_P4 sia  diverso da RossoGialloxVerdex
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_AndLogicOP_4 = true;
    bool res_AndLogicOP_5 = true;
    bool res_AndLogicOP_6 = true;
    res_AndLogicOP_6 = (res_AndLogicOP_6 && (L_P1__GetParamMainc11(my_id) == rossogiallo1));
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetMainc38(my_id) == false));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_7);
    
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_AndLogicOP_6);
    res_AndLogicOP_5 = (res_AndLogicOP_5 && (L_P1__GetMainc39(my_id) == true));
    
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_AndLogicOP_5);
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! Timer_Scaduto(L_P1__GetMainc48(my_id)));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_8);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_AndLogicOP_4);
    res_OrLogicOP_3 = (res_OrLogicOP_3 || Timer_Scaduto(L_P1__GetMainc48(my_id)));
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetInMainc6(my_id) == true));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_9);
    
    if(res_OrLogicOP_2){
    bool res_AndLogicOP_10 = true;
    bool res_ImpliesLogicOp_11 = true;
    if((L_P1__GetInConsd(my_id) == false)){
    bool res_XorLogicOP_12 = true;
    int xorIndex_res_XorLogicOP_12 = 0;
    bool res_ImpliesLogicOp_13 = true;
    bool res_OrLogicOP_14 = false;
    bool res_OrLogicOP_15 = false;
    bool res_OrLogicOP_16 = false;
    bool res_OrLogicOP_17 = false;
    bool res_AndLogicOP_18 = true;
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (L_P1__Macro3(my_id,avvio,rossogiallo3,true) == false));
    res_AndLogicOP_18 = (res_AndLogicOP_18 && res_NotLogicOP_19);
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! (Counter_GetValore(L_P1__GetMainc54(my_id)) == 131u));
    res_AndLogicOP_18 = (res_AndLogicOP_18 && res_NotLogicOP_20);
    
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_AndLogicOP_18);
    bool res_NotLogicOP_21 = true;
    res_NotLogicOP_21 = (res_NotLogicOP_21 && ! Timer_Disattivo(L_P1__GetMainc48(my_id)));
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_NotLogicOP_21);
    
    res_OrLogicOP_16 = (res_OrLogicOP_16 || res_OrLogicOP_17);
    bool res_NotLogicOP_22 = true;
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! (Counter_GetValore(L_P1__GetMainc53(my_id)) < 11u));
    res_OrLogicOP_16 = (res_OrLogicOP_16 || res_NotLogicOP_22);
    
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_OrLogicOP_16);
    res_OrLogicOP_15 = (res_OrLogicOP_15 || (L_P1__GetMainc39(my_id) == false));
    
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_OrLogicOP_15);
    res_OrLogicOP_14 = (res_OrLogicOP_14 || (L_P1__GetInConsd(my_id) == false));
    
    if(res_OrLogicOP_14){
    bool res_AndLogicOP_23 = true;
    bool res_ImpliesLogicOp_24 = true;
    if((L_P1__GetParamMainc10(my_id) == rossogiallo)){
    bool res_XorLogicOP_25 = true;
    int xorIndex_res_XorLogicOP_25 = 0;
    bool res_ImpliesLogicOp_26 = true;
    bool res_OrLogicOP_27 = false;
    bool res_OrLogicOP_28 = false;
    bool res_NotLogicOP_29 = true;
    res_NotLogicOP_29 = (res_NotLogicOP_29 && ! (L_P1__Macro3(my_id,avvio,rossogiallo3,true) == true));
    res_OrLogicOP_28 = (res_OrLogicOP_28 || res_NotLogicOP_29);
    bool res_AndLogicOP_30 = true;
    res_AndLogicOP_30 = (res_AndLogicOP_30 && (L_P1__GetInConsd(my_id) == false));
    res_AndLogicOP_30 = (res_AndLogicOP_30 && (L_P1__GetParamMainc13(my_id) == rossogiallo1));
    
    res_OrLogicOP_28 = (res_OrLogicOP_28 || res_AndLogicOP_30);
    
    res_OrLogicOP_27 = (res_OrLogicOP_27 || res_OrLogicOP_28);
    bool res_AndLogicOP_31 = true;
    bool res_NotLogicOP_32 = true;
    res_NotLogicOP_32 = (res_NotLogicOP_32 && ! Timer_Scaduto(L_P1__GetMainc49(my_id)));
    res_AndLogicOP_31 = (res_AndLogicOP_31 && res_NotLogicOP_32);
    bool res_NotLogicOP_33 = true;
    bool res_NotLogicOP_34 = true;
    res_NotLogicOP_34 = (res_NotLogicOP_34 && ! (Counter_GetValore(L_P1__GetMainc52(my_id)) == 14u));
    res_NotLogicOP_33 = (res_NotLogicOP_33 && ! res_NotLogicOP_34);
    res_AndLogicOP_31 = (res_AndLogicOP_31 && res_NotLogicOP_33);
    
    res_OrLogicOP_27 = (res_OrLogicOP_27 || res_AndLogicOP_31);
    
    if(res_OrLogicOP_27){
    bool res_OrLogicOP_35 = false;
    bool res_ImpliesLogicOp_36 = true;
    bool res_OrLogicOP_37 = false;
    bool res_AndLogicOP_38 = true;
    bool res_AndLogicOP_39 = true;
    res_AndLogicOP_39 = (res_AndLogicOP_39 && Timer_Disattivo(L_P1__GetMainc49(my_id)));
    res_AndLogicOP_39 = (res_AndLogicOP_39 && Timer_Attivo(L_P1__GetMainc49(my_id)));
    
    res_AndLogicOP_38 = (res_AndLogicOP_38 && res_AndLogicOP_39);
    bool res_NotLogicOP_40 = true;
    res_NotLogicOP_40 = (res_NotLogicOP_40 && ! (Counter_GetValore(L_P1__GetMainc52(my_id)) < 11u));
    res_AndLogicOP_38 = (res_AndLogicOP_38 && res_NotLogicOP_40);
    
    res_OrLogicOP_37 = (res_OrLogicOP_37 || res_AndLogicOP_38);
    bool res_AndLogicOP_41 = true;
    bool res_NotLogicOP_42 = true;
    res_NotLogicOP_42 = (res_NotLogicOP_42 && ! Timer_Scaduto(L_P1__GetMainc50(my_id)));
    res_AndLogicOP_41 = (res_AndLogicOP_41 && res_NotLogicOP_42);
    res_AndLogicOP_41 = (res_AndLogicOP_41 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_37 = (res_OrLogicOP_37 || res_AndLogicOP_41);
    
    if(res_OrLogicOP_37){
    bool res_ImpliesLogicOp_43 = true;
    if((L_P1__GetInMainc7(my_id) == true)){
    bool res_OrLogicOP_44 = false;
    bool res_OrLogicOP_45 = false;
    bool res_AndLogicOP_46 = true;
    bool res_AndLogicOP_47 = true;
    bool res_AndLogicOP_48 = true;
    bool res_NotLogicOP_49 = true;
    res_NotLogicOP_49 = (res_NotLogicOP_49 && ! (L_P1__GetMainc39(my_id) == true));
    res_AndLogicOP_48 = (res_AndLogicOP_48 && res_NotLogicOP_49);
    res_AndLogicOP_48 = (res_AndLogicOP_48 && (L_P1__GetInConsd(my_id) == false));
    
    res_AndLogicOP_47 = (res_AndLogicOP_47 && res_AndLogicOP_48);
    bool res_NotLogicOP_50 = true;
    res_NotLogicOP_50 = (res_NotLogicOP_50 && ! (Counter_GetValore(L_P1__GetMainc53(my_id)) == 1130u));
    res_AndLogicOP_47 = (res_AndLogicOP_47 && res_NotLogicOP_50);
    
    res_AndLogicOP_46 = (res_AndLogicOP_46 && res_AndLogicOP_47);
    bool res_NotLogicOP_51 = true;
    res_NotLogicOP_51 = (res_NotLogicOP_51 && ! (Counter_GetValore(L_P1__GetMainc53(my_id)) > 11u));
    res_AndLogicOP_46 = (res_AndLogicOP_46 && res_NotLogicOP_51);
    
    res_OrLogicOP_45 = (res_OrLogicOP_45 || res_AndLogicOP_46);
    bool res_NotLogicOP_52 = true;
    res_NotLogicOP_52 = (res_NotLogicOP_52 && ! (Counter_GetValore(L_P1__GetMainc51(my_id)) > 13254u));
    res_OrLogicOP_45 = (res_OrLogicOP_45 || res_NotLogicOP_52);
    
    res_OrLogicOP_44 = (res_OrLogicOP_44 || res_OrLogicOP_45);
    bool res_NotLogicOP_53 = true;
    res_NotLogicOP_53 = (res_NotLogicOP_53 && ! (L_P1__GetMainc38(my_id) == false));
    res_OrLogicOP_44 = (res_OrLogicOP_44 || res_NotLogicOP_53);
    
    res_ImpliesLogicOp_43 = (res_ImpliesLogicOp_43 && res_OrLogicOP_44);
    }
    res_ImpliesLogicOp_36 = (res_ImpliesLogicOp_36 && res_ImpliesLogicOp_43);
    }
    res_OrLogicOP_35 = (res_OrLogicOP_35 || res_ImpliesLogicOp_36);
    bool res_OrLogicOP_54 = false;
    bool res_OrLogicOP_55 = false;
    bool res_AndLogicOP_56 = true;
    res_AndLogicOP_56 = (res_AndLogicOP_56 && Timer_Scaduto(L_P1__GetMainc50(my_id)));
    bool res_NotLogicOP_57 = true;
    res_NotLogicOP_57 = (res_NotLogicOP_57 && ! (L_P1__GetParamMainc12(my_id) == 8u));
    res_AndLogicOP_56 = (res_AndLogicOP_56 && res_NotLogicOP_57);
    
    res_OrLogicOP_55 = (res_OrLogicOP_55 || res_AndLogicOP_56);
    res_OrLogicOP_55 = (res_OrLogicOP_55 || (Counter_GetValore(L_P1__GetMainc53(my_id)) == 13u));
    
    res_OrLogicOP_54 = (res_OrLogicOP_54 || res_OrLogicOP_55);
    res_OrLogicOP_54 = (res_OrLogicOP_54 || (Counter_GetValore(L_P1__GetMainc53(my_id)) > 125u));
    
    res_OrLogicOP_35 = (res_OrLogicOP_35 || res_OrLogicOP_54);
    
    res_ImpliesLogicOp_26 = (res_ImpliesLogicOp_26 && res_OrLogicOP_35);
    }
    if(res_ImpliesLogicOp_26){
    xorIndex_res_XorLogicOP_25 = (xorIndex_res_XorLogicOP_25 + 1);
    }
    bool res_AndLogicOP_58 = true;
    bool res_AndLogicOP_59 = true;
    bool res_AndLogicOP_60 = true;
    bool res_NotLogicOP_61 = true;
    res_NotLogicOP_61 = (res_NotLogicOP_61 && ! Timer_Attivo(L_P1__GetMainc48(my_id)));
    res_AndLogicOP_60 = (res_AndLogicOP_60 && res_NotLogicOP_61);
    bool res_NotLogicOP_62 = true;
    bool res_NotLogicOP_63 = true;
    res_NotLogicOP_63 = (res_NotLogicOP_63 && ! (Counter_GetValore(L_P1__GetMainc54(my_id)) == 11u));
    res_NotLogicOP_62 = (res_NotLogicOP_62 && ! res_NotLogicOP_63);
    res_AndLogicOP_60 = (res_AndLogicOP_60 && res_NotLogicOP_62);
    
    res_AndLogicOP_59 = (res_AndLogicOP_59 && res_AndLogicOP_60);
    res_AndLogicOP_59 = (res_AndLogicOP_59 && Timer_Scaduto(L_P1__GetMainc49(my_id)));
    
    res_AndLogicOP_58 = (res_AndLogicOP_58 && res_AndLogicOP_59);
    bool res_NotLogicOP_64 = true;
    bool res_NotLogicOP_65 = true;
    res_NotLogicOP_65 = (res_NotLogicOP_65 && ! (L_P1__GetParamMainc13(my_id) == rossogiallo1));
    res_NotLogicOP_64 = (res_NotLogicOP_64 && ! res_NotLogicOP_65);
    res_AndLogicOP_58 = (res_AndLogicOP_58 && res_NotLogicOP_64);
    
    if(res_AndLogicOP_58){
    xorIndex_res_XorLogicOP_25 = (xorIndex_res_XorLogicOP_25 + 1);
    }
    
    res_XorLogicOP_25 = (res_XorLogicOP_25 && (xorIndex_res_XorLogicOP_25 == 1));
    res_ImpliesLogicOp_24 = (res_ImpliesLogicOp_24 && res_XorLogicOP_25);
    }
    res_AndLogicOP_23 = (res_AndLogicOP_23 && res_ImpliesLogicOp_24);
    bool res_OrLogicOP_66 = false;
    bool res_AndLogicOP_67 = true;
    bool res_AndLogicOP_68 = true;
    bool res_AndLogicOP_69 = true;
    res_AndLogicOP_69 = (res_AndLogicOP_69 && (L_P1__GetInConsd(my_id) == false));
    res_AndLogicOP_69 = (res_AndLogicOP_69 && (L_P1__GetInConsd(my_id) == false));
    
    res_AndLogicOP_68 = (res_AndLogicOP_68 && res_AndLogicOP_69);
    bool res_NotLogicOP_70 = true;
    res_NotLogicOP_70 = (res_NotLogicOP_70 && ! (L_P1__GetInMainc6(my_id) == false));
    res_AndLogicOP_68 = (res_AndLogicOP_68 && res_NotLogicOP_70);
    
    res_AndLogicOP_67 = (res_AndLogicOP_67 && res_AndLogicOP_68);
    bool res_NotLogicOP_71 = true;
    res_NotLogicOP_71 = (res_NotLogicOP_71 && ! (L_P1__GetParamMainc12(my_id) == 4u));
    res_AndLogicOP_67 = (res_AndLogicOP_67 && res_NotLogicOP_71);
    
    res_OrLogicOP_66 = (res_OrLogicOP_66 || res_AndLogicOP_67);
    bool res_NotLogicOP_72 = true;
    res_NotLogicOP_72 = (res_NotLogicOP_72 && ! (Counter_GetValore(L_P1__GetMainc54(my_id)) < 133u));
    res_OrLogicOP_66 = (res_OrLogicOP_66 || res_NotLogicOP_72);
    
    res_AndLogicOP_23 = (res_AndLogicOP_23 && res_OrLogicOP_66);
    
    res_ImpliesLogicOp_13 = (res_ImpliesLogicOp_13 && res_AndLogicOP_23);
    }
    if(res_ImpliesLogicOp_13){
    xorIndex_res_XorLogicOP_12 = (xorIndex_res_XorLogicOP_12 + 1);
    }
    bool res_AndLogicOP_73 = true;
    bool res_AndLogicOP_74 = true;
    bool res_AndLogicOP_75 = true;
    bool res_NotLogicOP_76 = true;
    bool res_NotLogicOP_77 = true;
    res_NotLogicOP_77 = (res_NotLogicOP_77 && ! (Counter_GetValore(L_P1__GetMainc54(my_id)) == 13025u));
    res_NotLogicOP_76 = (res_NotLogicOP_76 && ! res_NotLogicOP_77);
    res_AndLogicOP_75 = (res_AndLogicOP_75 && res_NotLogicOP_76);
    res_AndLogicOP_75 = (res_AndLogicOP_75 && Timer_Attivo(L_P1__GetMainc49(my_id)));
    
    res_AndLogicOP_74 = (res_AndLogicOP_74 && res_AndLogicOP_75);
    bool res_NotLogicOP_78 = true;
    res_NotLogicOP_78 = (res_NotLogicOP_78 && ! (L_P1__GetInMainc6(my_id) == false));
    res_AndLogicOP_74 = (res_AndLogicOP_74 && res_NotLogicOP_78);
    
    res_AndLogicOP_73 = (res_AndLogicOP_73 && res_AndLogicOP_74);
    bool res_NotLogicOP_79 = true;
    res_NotLogicOP_79 = (res_NotLogicOP_79 && ! Timer_Disattivo(L_P1__GetMainc48(my_id)));
    res_AndLogicOP_73 = (res_AndLogicOP_73 && res_NotLogicOP_79);
    
    if(res_AndLogicOP_73){
    xorIndex_res_XorLogicOP_12 = (xorIndex_res_XorLogicOP_12 + 1);
    }
    
    res_XorLogicOP_12 = (res_XorLogicOP_12 && (xorIndex_res_XorLogicOP_12 == 1));
    res_ImpliesLogicOp_11 = (res_ImpliesLogicOp_11 && res_XorLogicOP_12);
    }
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_ImpliesLogicOp_11);
    bool res_OrLogicOP_80 = false;
    bool res_AndLogicOP_81 = true;
    bool res_AndLogicOP_82 = true;
    bool res_NotLogicOP_83 = true;
    res_NotLogicOP_83 = (res_NotLogicOP_83 && ! (Counter_GetValore(L_P1__GetMainc54(my_id)) == 15u));
    res_AndLogicOP_82 = (res_AndLogicOP_82 && res_NotLogicOP_83);
    res_AndLogicOP_82 = (res_AndLogicOP_82 && Timer_Attivo(L_P1__GetMainc50(my_id)));
    
    res_AndLogicOP_81 = (res_AndLogicOP_81 && res_AndLogicOP_82);
    bool res_NotLogicOP_84 = true;
    res_NotLogicOP_84 = (res_NotLogicOP_84 && ! (Counter_GetValore(L_P1__GetMainc51(my_id)) < 113u));
    res_AndLogicOP_81 = (res_AndLogicOP_81 && res_NotLogicOP_84);
    
    res_OrLogicOP_80 = (res_OrLogicOP_80 || res_AndLogicOP_81);
    bool res_NotLogicOP_85 = true;
    res_NotLogicOP_85 = (res_NotLogicOP_85 && ! (L_P1__GetParamMainc11(my_id) == rossogiallo1));
    res_OrLogicOP_80 = (res_OrLogicOP_80 || res_NotLogicOP_85);
    
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_OrLogicOP_80);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_AndLogicOP_10);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *48,49,50,*  *,*  il timer MainClass_C1_timer_T10 sia disattivo
    //   *104,* e  che   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* e  che  *,*  la variabile MainClass_C1_variabile_V10 sia  diverso da  True 
    //   *104,* o  che  *37,*  la variabile MainClass_C1_variabile_V10 sia  uguale a  True 
    //   *104,* o  che  *,*  il controllo MainClass_C1_controllo_C3 sia  uguale a  False
    bool res_OrLogicOP_86 = false;
    bool res_OrLogicOP_87 = false;
    bool res_AndLogicOP_88 = true;
    bool res_AndLogicOP_89 = true;
    res_AndLogicOP_89 = (res_AndLogicOP_89 && Timer_Disattivo(L_P1__GetMainc48(my_id)));
    res_AndLogicOP_89 = (res_AndLogicOP_89 && (L_P1__GetInConsd(my_id) == false));
    
    res_AndLogicOP_88 = (res_AndLogicOP_88 && res_AndLogicOP_89);
    bool res_NotLogicOP_90 = true;
    res_NotLogicOP_90 = (res_NotLogicOP_90 && ! (L_P1__GetMainc38(my_id) == true));
    res_AndLogicOP_88 = (res_AndLogicOP_88 && res_NotLogicOP_90);
    
    res_OrLogicOP_87 = (res_OrLogicOP_87 || res_AndLogicOP_88);
    res_OrLogicOP_87 = (res_OrLogicOP_87 || (L_P1__GetMainc38(my_id) == true));
    
    res_OrLogicOP_86 = (res_OrLogicOP_86 || res_OrLogicOP_87);
    res_OrLogicOP_86 = (res_OrLogicOP_86 || (L_P1__GetInMainc6(my_id) == false));
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_86);
    
    
    
    return res_AndLogicOP_0;
}


// Macro valorizzate

/*
    CNL corrispondente:
    
    { commento: {[}
     commento: {46,} assegna alla macro il valore RossoGialloGiallo commento: {],}
    }
*/
C1_Enumerat1 L_P1__Macro2(instance_id_t const my_id , C1_Enumerat2 argom, C1_Enumerat1 argom1, bool argom2, C1_Enumerat2 argom3, C1_Enumerat4 argom4, C1_Enumerat3 argom5, C1_Enumerat4 argom6)
{
return rossogiallo;
}

/*
    CNL corrispondente:
    
    { commento: {[}
     commento: {46,} assegna alla macro il valore  False  commento: {],}
    }
*/
bool L_P1__Macro3(instance_id_t const my_id , C1_Enumerat4 argom7, C1_Enumerat4 argom8, bool argom9)
{
return false;
}

/*
    CNL corrispondente:
    
    { commento: {[}
     commento: {46,} assegna alla macro il valore RossoGialloxVerdex commento: {],}
    }
*/
C1_Enumerat2 L_P1__Macro4(instance_id_t const my_id , C1_Enumerat2 argom10, C1_Enumerat1 argom11, C1_Enumerat3 argom12, C1_Enumerat2 argom13, C1_Enumerat3 argom14, C1_Enumerat4 argom15)
{
return rossogiallo1;
}

/*
    CNL corrispondente:
    
    { commento: {[} commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI2 non è attivo commento: {34,} e  se il parametro MainClass_C1_parametro_P8 non è  uguale a  commento: {53,} 4 commento: {37,} e  se la variabile MainClass_C1_variabile_V10 è  diverso da  False  commento: {34,} e  se il parametro MainClass_C1_parametro_P2 è  uguale a RossoGialloGiallo , assegna alla macro il valore  True 
    
     commento: {46,} assegna alla macro il valore  False  commento: {],}
    }
*/
bool L_P1__Macro5(instance_id_t const my_id , C1_Enumerat1 argom16, C1_Enumerat2 argom17)
{
bool res_macro_val;
    
    //  *[* *110,*  se il ripristino del timer  MainClass_C1_restoreTI_TI2 non è attivo *34,* e  se il parametro MainClass_C1_parametro_P8 non è  uguale a  *53,* 4 *37,* e  se la variabile MainClass_C1_variabile_V10 è  diverso da  False  *34,* e  se il parametro MainClass_C1_parametro_P2 è  uguale a RossoGialloGiallo
    bool res_AndLogicOP_0 = true;
    bool res_AndLogicOP_1 = true;
    bool res_AndLogicOP_2 = true;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! Timer_Attivo(L_P1__GetMainc43(my_id)));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_3);
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetParamMainc12(my_id) == 4u));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_4);
    
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_AndLogicOP_2);
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetMainc38(my_id) == false));
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_5);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_AndLogicOP_1);
    res_AndLogicOP_0 = (res_AndLogicOP_0 && (L_P1__GetParamMainc10(my_id) == rossogiallo));
    
    if(res_AndLogicOP_0){
    
    res_macro_val = true;
    }
    else{
    res_macro_val = false;
    }
    return res_macro_val;
}

/*
    CNL corrispondente:
    
    { commento: {[}
     commento: {46,} assegna alla macro il valore RossoGialloGiallo commento: {],}
    }
*/
C1_Enumerat1 L_P1__Macro6(instance_id_t const my_id , C1_Enumerat1 argom18, C1_Enumerat2 argom19, bool argom20, C1_Enumerat2 argom21, C1_Enumerat3 argom22, C1_Enumerat1 argom23)
{
return rossogiallo;
}



