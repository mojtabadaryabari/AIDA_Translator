// Codice del modello 'TestCase11', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#include "Logica/ClasseMainClass_C1.h"
#include "Logica/ClasseSubClass_C2.h"
#include "Logica/ClasseSubClass_C3.h"
#include "Logica/ClasseSubClass_C4.h"
#include "Logica/ClasseMainClass_C1_priv.h"
#include "config.h"
#include "scheduler.h"


// ********** Gestione comandi automatici **********

static size_t L_P1_C1_NumAutoCmds(instance_id_t const my_id)
{
    size_t n = 0u;
    if (L_P1__GetCAEvent2(my_id)) {
        ++n;
    }
    return n;
}


// ********** Gestione comandi manuali **********

static void L_P1_C1_InitCmdsResponse(instance_id_t const my_id)
{
    // for each manual command of L_P1_C1
    if (L_P1__GetInEvent(my_id)) {
	    L_P1__SetOutEvent5(my_id, LDS_MANCMD_UNEXPECTED);
    } else {
        L_P1__SetOutEvent5(my_id, LDS_MANCMD_NOOP);
    }
    if (L_P1__GetInEvent1(my_id)) {
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
    
      se il controllo ConsDef  è  uguale a FALSE  commento: {37,} o  se la variabile MainClass_C1_variabile_V8 non è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE ,  Applica gli effetti
           della macro MainClass_C1_macroef_M8   commento: {73,}
    
       
     commento: {38,}  se il contatore MainClass_C1_contatore_Co7 è  uguale a  commento: {53,} 11 commento: {36,} e  se il timer MainClass_C1_timer_T6 non è attivo commento: {38,} o  se il contatore MainClass_C1_contatore_Co1 è  maggiore di  commento: {54,} 14 commento: {34,} o  se il parametro MainClass_C1_parametro_P9 non è  uguale a  True  commento: {34,} e  se il parametro MainClass_C1_parametro_P1 non è  uguale a c270 commento: {36,} e  se il timer MainClass_C1_timer_T6 non è disattivo, commento: {69,}Disattiva il timer MainClass_C1_timer_T6
    
       
      se il controllo ConsDef è uguale a FALSE ,  Applica gli effetti
           della macro MainClass_C1_macroef_M7  commento: {73,}
    
     ,altrimenti  commento: {70,}Incrementa il contatore MainClass_C1_contatore_Co1
    
    
    
    }
*/
static inline void L_P1__Effec1(instance_id_t const my_id)
{
    
    //  se il controllo ConsDef  è  uguale a FALSE  *37,* o  se la variabile MainClass_C1_variabile_V8 non è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE ,  Applica gli effetti
    //         della macro MainClass_C1_macroef_M8
    bool res_OrLogicOP_0 = false;
    res_OrLogicOP_0 = (res_OrLogicOP_0 || (L_P1__GetInConsd(my_id) == false));
    bool res_AndLogicOP_1 = true;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (L_P1__GetMainc33(my_id) == false));
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_2);
    res_AndLogicOP_1 = (res_AndLogicOP_1 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_1);
    
    if(res_OrLogicOP_0){
    
    L_P1__Macro2(my_id);
    }
    
    //  *73,*
    //     
    //   *38,*  se il contatore MainClass_C1_contatore_Co7 è  uguale a  *53,* 11 *36,* e  se il timer MainClass_C1_timer_T6 non è attivo *38,* o  se il contatore MainClass_C1_contatore_Co1 è  maggiore di  *54,* 14 *34,* o  se il parametro MainClass_C1_parametro_P9 non è  uguale a  True  *34,* e  se il parametro MainClass_C1_parametro_P1 non è  uguale a c270 *36,* e  se il timer MainClass_C1_timer_T6 non è disattivo, *69,*Disattiva il timer MainClass_C1_timer_T6
    bool res_OrLogicOP_3 = false;
    bool res_OrLogicOP_4 = false;
    bool res_AndLogicOP_5 = true;
    res_AndLogicOP_5 = (res_AndLogicOP_5 && (Counter_GetValore(L_P1__GetMainc44(my_id)) == 11u));
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! Timer_Attivo(L_P1__GetMainc42(my_id)));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_6);
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_AndLogicOP_5);
    res_OrLogicOP_4 = (res_OrLogicOP_4 || (Counter_GetValore(L_P1__GetMainc43(my_id)) > 14u));
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_OrLogicOP_4);
    bool res_AndLogicOP_7 = true;
    bool res_AndLogicOP_8 = true;
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetParamMainc7(my_id) == true));
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_9);
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__GetParamMainc5(my_id) == c270));
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_10);
    
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_AndLogicOP_8);
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! Timer_Disattivo(L_P1__GetMainc42(my_id)));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_11);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_AndLogicOP_7);
    
    if(res_OrLogicOP_3){
    
    Timer_Disattiva(L_P1__GetMainc42(my_id));
    }
    
    //  se il controllo ConsDef è uguale a FALSE ,  Applica gli effetti
    //         della macro MainClass_C1_macroef_M7  *73,*
    //   ,altrimenti  *70,*Incrementa il contatore MainClass_C1_contatore_Co1
    if((L_P1__GetInConsd(my_id) == false)){
    
    L_P1__Macro1(my_id);
    }else{
    
    Counter_Incr(L_P1__GetMainc43(my_id));
    }
}



// ********** Definizione metodi **********

// Metodi standard

void L_P1_C1_Init(instance_id_t const my_id)
{
    // init variabili di stato
    L_P1__SetMainc18(my_id, 0);
    L_P1__SetMainc20(my_id, avviox);
    L_P1__SetMainc22(my_id, false);
    L_P1__SetMainc24(my_id, false);
    L_P1__SetMainc26(my_id, false);
    L_P1__SetMainc27(my_id, false);
    L_P1__SetMainc28(my_id, false);
    L_P1__SetMainc29(my_id, false);
    L_P1__SetMainc30(my_id, 0);
    L_P1__SetMainc31(my_id, 0);
    L_P1__SetMainc32(my_id, 0);
    L_P1__SetMainc33(my_id, false);
    L_P1__SetStato1(my_id, C1_St_Stato);
    // init controlli precedenti
    L_P1__SetMainc9(my_id, c180x);
    L_P1__SetMainc11(my_id, false);
    L_P1__SetMainc13(my_id, false);
    L_P1__SetMainc15(my_id, avanzamento);
    L_P1__SetMainc17(my_id, avanzamento);
    // init Timer e Counter
    Timer_AggmInit(L_P1__GetMainc34(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc34_ID);
    Timer_Init(L_P1__GetMainc34(my_id), 545000);
    Timer_AggmInit(L_P1__GetMainc35(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc35_ID);
    Timer_Init(L_P1__GetMainc35(my_id), 545000);
    Timer_AggmInit(L_P1__GetMainc36(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc36_ID);
    Timer_Init(L_P1__GetMainc36(my_id), 20213000);
    Timer_AggmInit(L_P1__GetMainc37(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc37_ID);
    Timer_Init(L_P1__GetMainc37(my_id), 20213000);
    Timer_AggmInit(L_P1__GetMainc38(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc38_ID);
    Timer_Init(L_P1__GetMainc38(my_id), 245000);
    Timer_AggmInit(L_P1__GetMainc39(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc39_ID);
    Timer_Init(L_P1__GetMainc39(my_id), 245000);
    Timer_AggmInit(L_P1__GetMainc40(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc40_ID);
    Timer_Init(L_P1__GetMainc40(my_id), 3000);
    Timer_AggmInit(L_P1__GetMainc41(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc41_ID);
    Timer_Init(L_P1__GetMainc41(my_id), 3000);
    Timer_AggmInit(L_P1__GetMainc42(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc42_ID);
    Timer_Init(L_P1__GetMainc42(my_id), 2000);
    Counter_AggmInit(L_P1__GetMainc43(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc43_ID);
    Counter_Init(L_P1__GetMainc43(my_id));
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
    Timer_Exec(L_P1__GetMainc34(my_id));
    Timer_Exec(L_P1__GetMainc35(my_id));
    Timer_Exec(L_P1__GetMainc36(my_id));
    Timer_Exec(L_P1__GetMainc37(my_id));
    Timer_Exec(L_P1__GetMainc38(my_id));
    Timer_Exec(L_P1__GetMainc39(my_id));
    Timer_Exec(L_P1__GetMainc40(my_id));
    Timer_Exec(L_P1__GetMainc41(my_id));
    Timer_Exec(L_P1__GetMainc42(my_id));
}

void L_P1_C1_GSetSafe(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C1(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C1(proc_id);
    L_P1__SetOutMainc(my_id, avanzamento);
    L_P1__SetOutMainc1(my_id, true);
}

void L_P1_C1_GUpdatePrev(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C1(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C1(proc_id);
    L_P1__SetMainc9(my_id, L_P1__GetInMainc8(my_id));
    L_P1__SetMainc11(my_id, L_P1__GetInMainc10(my_id));
    L_P1__SetMainc13(my_id, L_P1__GetInMainc12(my_id));
    L_P1__SetMainc15(my_id, L_P1__GetInMainc14(my_id));
    L_P1__SetMainc17(my_id, L_P1__GetInMainc16(my_id));
    L_P1__SetMainc19(my_id, L_P1__GetMainc18(my_id));
    L_P1__SetMainc21(my_id, L_P1__GetMainc20(my_id));
    L_P1__SetMainc23(my_id, L_P1__GetMainc22(my_id));
    L_P1__SetMainc25(my_id, L_P1__GetMainc24(my_id));
}

// ********** Definizione macro **********

// Macro di effetto

/*
    CNL corrispondente:
    
    {  se il controllo ConsDef è uguale a FALSE  commento: {35,} o  se il controllo MainClass_C1_controllo_C1 è  diverso da  True  commento: {36,} e  se il timer MainClass_C1_timer_T6 non è scaduto commento: {38,} o  se il contatore MainClass_C1_contatore_Co1 non è  maggiore di  commento: {54,} 14021 commento: {35,} e  se il controllo MainClass_C1_controllo_C1 è  uguale a  False , commento: {67,} Assegna alla variabile MainClass_C1_variabile_V6 il valore 8
    
       
    
    }
*/
void L_P1__Macro(instance_id_t const my_id )
{
//  se il controllo ConsDef è uguale a FALSE  *35,* o  se il controllo MainClass_C1_controllo_C1 è  diverso da  True  *36,* e  se il timer MainClass_C1_timer_T6 non è scaduto *38,* o  se il contatore MainClass_C1_contatore_Co1 non è  maggiore di  *54,* 14021 *35,* e  se il controllo MainClass_C1_controllo_C1 è  uguale a  False , *67,* Assegna alla variabile MainClass_C1_variabile_V6 il valore 8
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    res_OrLogicOP_1 = (res_OrLogicOP_1 || (L_P1__GetInConsd(my_id) == false));
    bool res_AndLogicOP_2 = true;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__GetInMainc2(my_id) == true));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_3);
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! Timer_Scaduto(L_P1__GetMainc42(my_id)));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_4);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_2);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_AndLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (Counter_GetValore(L_P1__GetMainc43(my_id)) > 14021u));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_6);
    res_AndLogicOP_5 = (res_AndLogicOP_5 && (L_P1__GetInMainc2(my_id) == false));
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_5);
    
    if(res_OrLogicOP_0){
    
    L_P1__SetMainc32(my_id,8u);
    }
}

/*
    CNL corrispondente:
    
    { commento: {38,}  se il contatore MainClass_C1_contatore_Co7 non è  diverso da  commento: {56,} 1345 o  se il controllo ConsDef  è  uguale a FALSE , commento: {66,} Assegna al comando MainClass_C1_comando_C10 il valore avanzamento
    
       
      se la macro  MainClass_C1_macrova_M1 ( con argomento_a1   uguale a True ,argomento_a3   uguale a avviox ,argomento_a2   uguale a c180x ,argomento_a4   uguale a GialloxVerdex ,argomento_a9   uguale a RossoVerde ,argomento_a8   uguale a avviox  e argomento_a7   uguale a avanzamento )  non  è  uguale a avanzamento commento: {40,} ,  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V8 il valore  True  commento: {67,}
    
       
    
    }
*/
void L_P1__Macro1(instance_id_t const my_id )
{
//  *38,*  se il contatore MainClass_C1_contatore_Co7 non è  diverso da  *56,* 1345 o  se il controllo ConsDef  è  uguale a FALSE , *66,* Assegna al comando MainClass_C1_comando_C10 il valore avanzamento
    bool res_OrLogicOP_0 = false;
    bool res_NotLogicOP_1 = true;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (Counter_GetValore(L_P1__GetMainc44(my_id)) == 1345u));
    res_NotLogicOP_1 = (res_NotLogicOP_1 && ! res_NotLogicOP_2);
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_1);
    res_OrLogicOP_0 = (res_OrLogicOP_0 || (L_P1__GetInConsd(my_id) == false));
    
    if(res_OrLogicOP_0){
    
    L_P1__SetOutMainc(my_id,avanzamento);
    }
    //  se la macro  MainClass_C1_macrova_M1 ( con argomento_a1   uguale a True ,argomento_a3   uguale a avviox ,argomento_a2   uguale a c180x ,argomento_a4   uguale a GialloxVerdex ,argomento_a9   uguale a RossoVerde ,argomento_a8   uguale a avviox  e argomento_a7   uguale a avanzamento )  non  è  uguale a avanzamento *40,* ,  *67,* Assegna alla variabile MainClass_C1_variabile_V8 il valore  True
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__Macro3(my_id,true,c180x,avviox,gialloxverd,avanzamento,avviox,rossoverde) == avanzamento));
    if(res_NotLogicOP_3){
    
    L_P1__SetMainc33(my_id,true);
    }
}

/*
    CNL corrispondente:
     
    { commento: {34,}  se il parametro MainClass_C1_parametro_P1 è  uguale a c270 o  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} e  se la variabile MainClass_C1_variabile_V8 non è  diverso da  True  commento: {36,} e  se il timer MainClass_C1_timer_T6 non è attivo commento: {34,} o  se il parametro MainClass_C1_parametro_P2 non è  maggiore di  commento: {54,} 5 commento: {35,} e  se il controllo MainClass_C1_controllo_C7 non è  diverso da c180x,  Applica gli effetti
           della macro MainClass_C1_macroef_M7  commento: {73,}
    
       
      se il ripristino dello stato  è  diverso da  commento: {56,}  state1  commento: {107,} o  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} o  se il timer MainClass_C1_timer_T6 è disattivo commento: {34,} e  se il parametro MainClass_C1_parametro_P1 non è  diverso da c270 commento: {34,} e  se il parametro MainClass_C1_parametro_P2 è  diverso da  commento: {56,} 4 commento: {35,} e  se il controllo MainClass_C1_controllo_C8 non è  uguale a avanzamento,  Applica gli effetti
           della macro MainClass_C1_macroef_M7  commento: {73,}
    
       
      se la macro  MainClass_C1_macrova_M9 ( con argomento_a7   uguale a avviox ,argomento_a5   uguale a RossoGialloVerde ,argomento_a10   uguale a c270 ,argomento_a6   uguale a c180x ,argomento_a1   uguale a c180 ,argomento_a3   uguale a RossoGialloVerde  e argomento_a2   uguale a GialloxVerdex )  non  è  uguale a RossoVerde commento: {40,} , commento: {67,} Assegna alla variabile MainClass_C1_variabile_V6 il valore 2
    
       
     commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo,  Applica gli effetti
           della macro MainClass_C1_macroef_M7  commento: {73,}
    
       
     commento: {35,}  se il controllo MainClass_C1_controllo_C8 è  diverso da avanzamento commento: {35,} o  se il controllo MainClass_C1_controllo_C7 non è  diverso da c180x o  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} o  se il parametro MainClass_C1_parametro_P1 è  diverso da c270,  Applica gli effetti
           della macro MainClass_C1_macroef_M7  commento: {73,}
    
     ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V6 il valore 9
    
    
    
    }
*/
void L_P1__Macro2(instance_id_t const my_id )
{
//  *34,*  se il parametro MainClass_C1_parametro_P1 è  uguale a c270 o  se il controllo ConsDef  è  uguale a FALSE  *37,* e  se la variabile MainClass_C1_variabile_V8 non è  diverso da  True  *36,* e  se il timer MainClass_C1_timer_T6 non è attivo *34,* o  se il parametro MainClass_C1_parametro_P2 non è  maggiore di  *54,* 5 *35,* e  se il controllo MainClass_C1_controllo_C7 non è  diverso da c180x,  Applica gli effetti
    //       della macro MainClass_C1_macroef_M7
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    res_OrLogicOP_1 = (res_OrLogicOP_1 || (L_P1__GetParamMainc5(my_id) == c270));
    bool res_AndLogicOP_2 = true;
    bool res_AndLogicOP_3 = true;
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_4 = true;
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetMainc33(my_id) == true));
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! res_NotLogicOP_5);
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_4);
    
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_AndLogicOP_3);
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! Timer_Attivo(L_P1__GetMainc42(my_id)));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_6);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_2);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_AndLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetParamMainc6(my_id) > 5u));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_8);
    bool res_NotLogicOP_9 = true;
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__GetInMainc3(my_id) == c180x));
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! res_NotLogicOP_10);
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_9);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_7);
    
    if(res_OrLogicOP_0){
    
    L_P1__Macro1(my_id);
    }
    //  *73,*
    //   
    //  se il ripristino dello stato  è  diverso da  *56,*  state1  *107,* o  se il controllo ConsDef  è  uguale a FALSE  *36,* o  se il timer MainClass_C1_timer_T6 è disattivo *34,* e  se il parametro MainClass_C1_parametro_P1 non è  diverso da c270 *34,* e  se il parametro MainClass_C1_parametro_P2 è  diverso da  *56,* 4 *35,* e  se il controllo MainClass_C1_controllo_C8 non è  uguale a avanzamento,  Applica gli effetti
    //       della macro MainClass_C1_macroef_M7
    bool res_OrLogicOP_11 = false;
    bool res_OrLogicOP_12 = false;
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (L_P1__GetStato1(my_id) == C1_St_state));
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_NotLogicOP_13);
    res_OrLogicOP_12 = (res_OrLogicOP_12 || (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_OrLogicOP_12);
    bool res_AndLogicOP_14 = true;
    bool res_AndLogicOP_15 = true;
    bool res_AndLogicOP_16 = true;
    res_AndLogicOP_16 = (res_AndLogicOP_16 && Timer_Disattivo(L_P1__GetMainc42(my_id)));
    bool res_NotLogicOP_17 = true;
    bool res_NotLogicOP_18 = true;
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! (L_P1__GetParamMainc5(my_id) == c270));
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! res_NotLogicOP_18);
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_NotLogicOP_17);
    
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_AndLogicOP_16);
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (L_P1__GetParamMainc6(my_id) == 4u));
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_NotLogicOP_19);
    
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_AndLogicOP_15);
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! (L_P1__GetInMainc4(my_id) == avanzamento));
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_NotLogicOP_20);
    
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_AndLogicOP_14);
    
    if(res_OrLogicOP_11){
    
    L_P1__Macro1(my_id);
    }
    //  *73,*
    //   
    //  se la macro  MainClass_C1_macrova_M9 ( con argomento_a7   uguale a avviox ,argomento_a5   uguale a RossoGialloVerde ,argomento_a10   uguale a c270 ,argomento_a6   uguale a c180x ,argomento_a1   uguale a c180 ,argomento_a3   uguale a RossoGialloVerde  e argomento_a2   uguale a GialloxVerdex )  non  è  uguale a RossoVerde *40,* , *67,* Assegna alla variabile MainClass_C1_variabile_V6 il valore 2
    bool res_NotLogicOP_21 = true;
    res_NotLogicOP_21 = (res_NotLogicOP_21 && ! (L_P1__Macro6(my_id,c180,c270,gialloxverd,rossogiallo1,rossogiallo1,c180x,avviox) == rossoverde));
    if(res_NotLogicOP_21){
    
    L_P1__SetMainc32(my_id,2u);
    }
    //  *110,*  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo,  Applica gli effetti
    //       della macro MainClass_C1_macroef_M7
    bool res_NotLogicOP_22 = true;
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! Timer_Attivo(L_P1__GetMainc35(my_id)));
    if(res_NotLogicOP_22){
    
    L_P1__Macro1(my_id);
    }
    //  *73,*
    //   
    // *35,*  se il controllo MainClass_C1_controllo_C8 è  diverso da avanzamento *35,* o  se il controllo MainClass_C1_controllo_C7 non è  diverso da c180x o  se il controllo ConsDef  è  uguale a FALSE  *34,* o  se il parametro MainClass_C1_parametro_P1 è  diverso da c270,  Applica gli effetti
    //       della macro MainClass_C1_macroef_M7  *73,*
    // ,altrimenti  *67,* Assegna alla variabile MainClass_C1_variabile_V6 il valore 9
    bool res_OrLogicOP_23 = false;
    bool res_OrLogicOP_24 = false;
    bool res_OrLogicOP_25 = false;
    bool res_NotLogicOP_26 = true;
    res_NotLogicOP_26 = (res_NotLogicOP_26 && ! (L_P1__GetInMainc4(my_id) == avanzamento));
    res_OrLogicOP_25 = (res_OrLogicOP_25 || res_NotLogicOP_26);
    bool res_NotLogicOP_27 = true;
    bool res_NotLogicOP_28 = true;
    res_NotLogicOP_28 = (res_NotLogicOP_28 && ! (L_P1__GetInMainc3(my_id) == c180x));
    res_NotLogicOP_27 = (res_NotLogicOP_27 && ! res_NotLogicOP_28);
    res_OrLogicOP_25 = (res_OrLogicOP_25 || res_NotLogicOP_27);
    
    res_OrLogicOP_24 = (res_OrLogicOP_24 || res_OrLogicOP_25);
    res_OrLogicOP_24 = (res_OrLogicOP_24 || (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_23 = (res_OrLogicOP_23 || res_OrLogicOP_24);
    bool res_NotLogicOP_29 = true;
    res_NotLogicOP_29 = (res_NotLogicOP_29 && ! (L_P1__GetParamMainc5(my_id) == c270));
    res_OrLogicOP_23 = (res_OrLogicOP_23 || res_NotLogicOP_29);
    
    if(res_OrLogicOP_23){
    
    L_P1__Macro1(my_id);
    }else{
    
    L_P1__SetMainc32(my_id,9u);
    }
}


// Macro di verifica

/*
    CNL corrispondente:
    
    { commento: {61,} commento: {34,}  se lo stato  è  diverso da  commento: {56,}  state1  commento: {106,}, Tutte le seguenti { 
     commento: {63,} commento: {36,}  se il timer MainClass_C1_timer_T6 è attivo commento: {36,} e  se il timer MainClass_C1_timer_T6 è attivo commento: {37,} e  se la variabile MainClass_C1_variabile_V6 è  minore di  commento: {55,} 4 o  se l'argomento argomento_ave4 non  è  uguale a c270 commento: {39,} , Solo una delle seguenti { 
     commento: {34,}  se il parametro MainClass_C1_parametro_P1 è  uguale a c270 commento: {38,} e  se il contatore MainClass_C1_contatore_Co7 non è  minore di  commento: {55,} 14 commento: {36,} o  se il timer MainClass_C1_timer_T6 è scaduto commento: {37,} e  se la variabile MainClass_C1_variabile_V8 non è  diverso da  False  commento: {36,} e  se il timer MainClass_C1_timer_T6 è attivo, Verifica che   commento: {47,49,51,}  commento: {34,}  il parametro MainClass_C1_parametro_P9 sia  uguale a  True 
     commento: {104,} o  che  commento: {,}  il contatore MainClass_C1_contatore_Co7 non sia  maggiore di  commento: {54,} 102
     commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T6 sia scaduto
     commento: {104,} e  che  commento: {36,}  il timer MainClass_C1_timer_T6 sia scaduto
    
    
     } Verifica che   commento: {47,48,50,}  commento: {,}  il controllo MainClass_C1_controllo_C8 non sia  uguale a avanzamento
     commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V8 sia  uguale a  False 
     commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P1 non sia  uguale a c270
    
    
     } Verifica che   commento: {48,}  commento: {,}  il controllo MainClass_C1_controllo_C8 sia  uguale a avanzamento
    
    
    }
*/
bool L_P1__Macro7(instance_id_t const my_id , C1_Enumerat1 argom27, C1_Enumerat2 argom28, bool argom29, bool argom30, C1_Enumerat4 argom31)
{
bool res_AndLogicOP_0 = true;
    
    //  *61,* *34,*  se lo stato  è  diverso da  *56,*  state1  *106,*, Tutte le seguenti { 
    //   *63,* *36,*  se il timer MainClass_C1_timer_T6 è attivo *36,* e  se il timer MainClass_C1_timer_T6 è attivo *37,* e  se la variabile MainClass_C1_variabile_V6 è  minore di  *55,* 4 o  se l'argomento argomento_ave4 non  è  uguale a c270 *39,* , Solo una delle seguenti { 
    //   *34,*  se il parametro MainClass_C1_parametro_P1 è  uguale a c270 *38,* e  se il contatore MainClass_C1_contatore_Co7 non è  minore di  *55,* 14 *36,* o  se il timer MainClass_C1_timer_T6 è scaduto *37,* e  se la variabile MainClass_C1_variabile_V8 non è  diverso da  False  *36,* e  se il timer MainClass_C1_timer_T6 è attivo, Verifica che   *47,49,51,*  *34,*  il parametro MainClass_C1_parametro_P9 sia  uguale a  True 
    //   *104,* o  che  *,*  il contatore MainClass_C1_contatore_Co7 non sia  maggiore di  *54,* 102
    //   *104,* o  che  *,*  il timer MainClass_C1_timer_T6 sia scaduto
    //   *104,* e  che  *36,*  il timer MainClass_C1_timer_T6 sia scaduto
    //   } Verifica che   *47,48,50,*  *,*  il controllo MainClass_C1_controllo_C8 non sia  uguale a avanzamento
    //   *104,* o  che  *,*  la variabile MainClass_C1_variabile_V8 sia  uguale a  False 
    //   *104,* e  che  *34,*  il parametro MainClass_C1_parametro_P1 non sia  uguale a c270
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (L_P1_C1_GetState(my_id) == C1_St_state));
    if(res_NotLogicOP_2){
    bool res_AndLogicOP_3 = true;
    bool res_ImpliesLogicOp_4 = true;
    bool res_OrLogicOP_5 = false;
    bool res_AndLogicOP_6 = true;
    bool res_AndLogicOP_7 = true;
    res_AndLogicOP_7 = (res_AndLogicOP_7 && Timer_Attivo(L_P1__GetMainc42(my_id)));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && Timer_Attivo(L_P1__GetMainc42(my_id)));
    
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_AndLogicOP_7);
    res_AndLogicOP_6 = (res_AndLogicOP_6 && (L_P1__GetMainc32(my_id) < 4u));
    
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_AndLogicOP_6);
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (argom27 == c270));
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_NotLogicOP_8);
    
    if(res_OrLogicOP_5){
    bool res_ImpliesLogicOp_9 = true;
    bool res_OrLogicOP_10 = false;
    bool res_AndLogicOP_11 = true;
    res_AndLogicOP_11 = (res_AndLogicOP_11 && (L_P1__GetParamMainc5(my_id) == c270));
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (Counter_GetValore(L_P1__GetMainc44(my_id)) < 14u));
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_NotLogicOP_12);
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_AndLogicOP_11);
    bool res_AndLogicOP_13 = true;
    bool res_AndLogicOP_14 = true;
    res_AndLogicOP_14 = (res_AndLogicOP_14 && Timer_Scaduto(L_P1__GetMainc42(my_id)));
    bool res_NotLogicOP_15 = true;
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (L_P1__GetMainc33(my_id) == false));
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! res_NotLogicOP_16);
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_NotLogicOP_15);
    
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_AndLogicOP_14);
    res_AndLogicOP_13 = (res_AndLogicOP_13 && Timer_Attivo(L_P1__GetMainc42(my_id)));
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_AndLogicOP_13);
    
    if(res_OrLogicOP_10){
    bool res_OrLogicOP_17 = false;
    bool res_OrLogicOP_18 = false;
    res_OrLogicOP_18 = (res_OrLogicOP_18 || (L_P1__GetParamMainc7(my_id) == true));
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (Counter_GetValore(L_P1__GetMainc44(my_id)) > 102u));
    res_OrLogicOP_18 = (res_OrLogicOP_18 || res_NotLogicOP_19);
    
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_OrLogicOP_18);
    bool res_AndLogicOP_20 = true;
    res_AndLogicOP_20 = (res_AndLogicOP_20 && Timer_Scaduto(L_P1__GetMainc42(my_id)));
    res_AndLogicOP_20 = (res_AndLogicOP_20 && Timer_Scaduto(L_P1__GetMainc42(my_id)));
    
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_AndLogicOP_20);
    
    res_ImpliesLogicOp_9 = (res_ImpliesLogicOp_9 && res_OrLogicOP_17);
    }
    res_ImpliesLogicOp_4 = (res_ImpliesLogicOp_4 && res_ImpliesLogicOp_9);
    }
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_ImpliesLogicOp_4);
    bool res_OrLogicOP_21 = false;
    bool res_NotLogicOP_22 = true;
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! (L_P1__GetInMainc4(my_id) == avanzamento));
    res_OrLogicOP_21 = (res_OrLogicOP_21 || res_NotLogicOP_22);
    bool res_AndLogicOP_23 = true;
    res_AndLogicOP_23 = (res_AndLogicOP_23 && (L_P1__GetMainc33(my_id) == false));
    bool res_NotLogicOP_24 = true;
    res_NotLogicOP_24 = (res_NotLogicOP_24 && ! (L_P1__GetParamMainc5(my_id) == c270));
    res_AndLogicOP_23 = (res_AndLogicOP_23 && res_NotLogicOP_24);
    
    res_OrLogicOP_21 = (res_OrLogicOP_21 || res_AndLogicOP_23);
    
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_OrLogicOP_21);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_AndLogicOP_3);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *48,*  *,*  il controllo MainClass_C1_controllo_C8 sia  uguale a avanzamento
    res_AndLogicOP_0 = (res_AndLogicOP_0 && (L_P1__GetInMainc4(my_id) == avanzamento));
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
     
    { commento: {63,}  se il ripristino dello stato  è  diverso da  commento: {56,}  state1  commento: {107,}, Solo una delle seguenti { 
     commento: {62,}  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} e  se la variabile MainClass_C1_variabile_V8 non è  uguale a  True  commento: {34,} o  se il parametro MainClass_C1_parametro_P2 è  minore di  commento: {55,} 1 commento: {38,} e  se il contatore MainClass_C1_contatore_Co7 è  diverso da  commento: {56,} 1150213 commento: {38,} e  se il contatore MainClass_C1_contatore_Co7 non è  minore di  commento: {55,} 124, Almeno una delle seguenti { 
     commento: {63,}  se il ripristino dello stato  è  diverso da  commento: {56,}  state1  commento: {107,} commento: {37,} o  se la variabile MainClass_C1_variabile_V8 non è  diverso da  False  commento: {34,} o  se il parametro MainClass_C1_parametro_P9 non è  diverso da  True , Solo una delle seguenti { 
     commento: {63,} commento: {38,}  se il contatore MainClass_C1_contatore_Co1 non è  diverso da  commento: {56,} 135 commento: {36,} e  se il timer MainClass_C1_timer_T6 è attivo commento: {34,} e  se il parametro MainClass_C1_parametro_P1 è  diverso da c270 commento: {35,} o  se il controllo MainClass_C1_controllo_C7 non è  uguale a c180x commento: {34,} o  se il parametro MainClass_C1_parametro_P2 non è  diverso da  commento: {56,} 10 commento: {34,} o  se il parametro MainClass_C1_parametro_P9 è  diverso da  True , Solo una delle seguenti { 
     commento: {63,} commento: {34,}  se il parametro MainClass_C1_parametro_P2 è  uguale a  commento: {53,} 8 commento: {34,} e  se il parametro MainClass_C1_parametro_P1 è  diverso da c270 o  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} o  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  commento: {54,} 120213 commento: {38,} e  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  commento: {54,} 14, Solo una delle seguenti { 
     commento: {63,} commento: {36,}  se il timer MainClass_C1_timer_T6 è scaduto, Solo una delle seguenti { 
     commento: {61,} commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI4 non è scaduto commento: {37,} e  se la variabile MainClass_C1_variabile_V6 è  diverso da  commento: {56,} 9 commento: {35,} o  se il controllo MainClass_C1_controllo_C1 non è  uguale a  False  commento: {35,} e  se il controllo MainClass_C1_controllo_C7 è  uguale a c180x, Tutte le seguenti { 
     commento: {63,} commento: {38,}  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  commento: {53,} 14 commento: {35,} o  se il controllo MainClass_C1_controllo_C1 è  uguale a  True  commento: {37,} o  se la variabile MainClass_C1_variabile_V8 non è  uguale a  True  commento: {34,} o  se il parametro MainClass_C1_parametro_P2 non è  maggiore di  commento: {54,} 4 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
     commento: {62,} commento: {34,}  se il parametro MainClass_C1_parametro_P9 è  diverso da  True  commento: {38,} o  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  commento: {54,} 11 o  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} e  se la variabile MainClass_C1_variabile_V6 non è  minore di  commento: {55,} 10 commento: {38,} o  se il contatore MainClass_C1_contatore_Co7 non è  minore di  commento: {55,} 124 e  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
     commento: {61,} commento: {34,}  se lo stato  è  uguale a  commento: {53,}  state1  commento: {106,} commento: {34,} o  se il parametro MainClass_C1_parametro_P1 è  diverso da c270, Tutte le seguenti { 
     commento: {62,}  se il controllo ConsDef è uguale a FALSE  commento: {34,} o  se il parametro MainClass_C1_parametro_P2 è  diverso da  commento: {56,} 9 commento: {37,} o  se la variabile MainClass_C1_variabile_V6 è  minore di  commento: {55,} 9 o  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
      se il controllo ConsDef è uguale a FALSE , Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
    
    
     } Verifica che   commento: {47,48,51,}  commento: {,}  il contatore MainClass_C1_contatore_Co1 non sia  diverso da  commento: {56,} 12
     commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P1 sia  uguale a c270
     commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} o  che  commento: {38,}  il contatore MainClass_C1_contatore_Co7 non sia  maggiore di  commento: {54,} 13
     commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C1 non sia  diverso da  True 
    
    
     } Verifica che   commento: {48,}  commento: {,}  il controllo MainClass_C1_controllo_C8 non sia  uguale a avanzamento
    
    
     } Verifica che   commento: {47,48,49,50,}  commento: {34,}  il parametro MainClass_C1_parametro_P1 non sia  uguale a c270
     commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V8 sia  diverso da  True 
     commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T6 non sia disattivo
     commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P1 non sia  uguale a c270
    
    
     } Verifica che   commento: {48,49,50,51,}  commento: {,}  la variabile MainClass_C1_variabile_V6 sia  maggiore di  commento: {54,} 5
     commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T6 non sia attivo
     commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C8 sia  diverso da avanzamento
     commento: {104,} o  che  commento: {,}  il contatore MainClass_C1_contatore_Co1 non sia  minore di  commento: {55,} 1150213
     commento: {104,} e  che  commento: {37,}  la variabile MainClass_C1_variabile_V6 non sia  diverso da  commento: {56,} 8
    
    
     } Verifica che   commento: {47,48,50,51,}   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V8 non sia  uguale a  False 
     commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P9 sia  diverso da  False 
     commento: {104,} o  che  commento: {37,}  la variabile MainClass_C1_variabile_V6 sia  maggiore di  commento: {54,} 7
     commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C1 non sia  diverso da  True 
     commento: {104,} o  che  commento: {,}  il contatore MainClass_C1_contatore_Co7 sia  minore di  commento: {55,} 14
    
    
     } Verifica che   commento: {47,51,}  commento: {,}  il contatore MainClass_C1_contatore_Co7 sia  minore di  commento: {55,} 14
     commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P1 non sia  diverso da c270
    
    
     } Verifica che   commento: {47,49,51,}  commento: {34,}  il parametro MainClass_C1_parametro_P2 sia  maggiore di  commento: {54,} 6
     commento: {104,} o  che  commento: {,}  il contatore MainClass_C1_contatore_Co1 non sia  uguale a  commento: {53,} 1
     commento: {104,} o  che  commento: {38,}  il contatore MainClass_C1_contatore_Co7 sia  maggiore di  commento: {54,} 102
     commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T6 non sia disattivo
    
    
     } Verifica che   commento: {48,51,}   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C8 non sia  uguale a avanzamento
     commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co7 sia  diverso da  commento: {56,} 11
     commento: {104,} e  che  commento: {38,}  il contatore MainClass_C1_contatore_Co1 non sia  minore di  commento: {55,} 1113
    
    
     } Verifica che   commento: {48,}  commento: {,}  il controllo MainClass_C1_controllo_C7 sia  uguale a c180x
    
    
     } Verifica che   commento: {47,49,50,51,}  commento: {,}  il contatore MainClass_C1_contatore_Co7 sia  uguale a  commento: {53,} 13
     commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P2 sia  minore di  commento: {55,} 6
     commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V6 sia  minore di  commento: {55,} 10
     commento: {104,} o  che  commento: {37,}  la variabile MainClass_C1_variabile_V6 sia  maggiore di  commento: {54,} 3
     commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T6 non sia disattivo
     commento: {104,} o  che  commento: {36,}  il timer MainClass_C1_timer_T6 non sia attivo
    
    
     } Verifica che   commento: {47,48,49,50,}  commento: {,}  il timer MainClass_C1_timer_T6 non sia scaduto
     commento: {104,} e  che  commento: {36,}  il timer MainClass_C1_timer_T6 sia attivo
     commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} o  che  commento: {36,}  il timer MainClass_C1_timer_T6 sia disattivo
     commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P9 non sia  uguale a  True 
     commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V8 sia  uguale a  False 
    
    
    }
*/
bool L_P1__Macro8(instance_id_t const my_id )
{
bool res_AndLogicOP_0 = true;
    
    //  *63,*  se il ripristino dello stato  è  diverso da  *56,*  state1  *107,*, Solo una delle seguenti { 
    //   *62,*  se il controllo ConsDef  è  uguale a FALSE  *37,* e  se la variabile MainClass_C1_variabile_V8 non è  uguale a  True  *34,* o  se il parametro MainClass_C1_parametro_P2 è  minore di  *55,* 1 *38,* e  se il contatore MainClass_C1_contatore_Co7 è  diverso da  *56,* 1150213 *38,* e  se il contatore MainClass_C1_contatore_Co7 non è  minore di  *55,* 124, Almeno una delle seguenti { 
    //   *63,*  se il ripristino dello stato  è  diverso da  *56,*  state1  *107,* *37,* o  se la variabile MainClass_C1_variabile_V8 non è  diverso da  False  *34,* o  se il parametro MainClass_C1_parametro_P9 non è  diverso da  True , Solo una delle seguenti { 
    //   *63,* *38,*  se il contatore MainClass_C1_contatore_Co1 non è  diverso da  *56,* 135 *36,* e  se il timer MainClass_C1_timer_T6 è attivo *34,* e  se il parametro MainClass_C1_parametro_P1 è  diverso da c270 *35,* o  se il controllo MainClass_C1_controllo_C7 non è  uguale a c180x *34,* o  se il parametro MainClass_C1_parametro_P2 non è  diverso da  *56,* 10 *34,* o  se il parametro MainClass_C1_parametro_P9 è  diverso da  True , Solo una delle seguenti { 
    //   *63,* *34,*  se il parametro MainClass_C1_parametro_P2 è  uguale a  *53,* 8 *34,* e  se il parametro MainClass_C1_parametro_P1 è  diverso da c270 o  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  *38,* o  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  *54,* 120213 *38,* e  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  *54,* 14, Solo una delle seguenti { 
    //   *63,* *36,*  se il timer MainClass_C1_timer_T6 è scaduto, Solo una delle seguenti { 
    //   *61,* *110,*  se il ripristino del timer  MainClass_C1_restoreTI_TI4 non è scaduto *37,* e  se la variabile MainClass_C1_variabile_V6 è  diverso da  *56,* 9 *35,* o  se il controllo MainClass_C1_controllo_C1 non è  uguale a  False  *35,* e  se il controllo MainClass_C1_controllo_C7 è  uguale a c180x, Tutte le seguenti { 
    //   *63,* *38,*  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  *53,* 14 *35,* o  se il controllo MainClass_C1_controllo_C1 è  uguale a  True  *37,* o  se la variabile MainClass_C1_variabile_V8 non è  uguale a  True  *34,* o  se il parametro MainClass_C1_parametro_P2 non è  maggiore di  *54,* 4 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
    //   *62,* *34,*  se il parametro MainClass_C1_parametro_P9 è  diverso da  True  *38,* o  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  *54,* 11 o  se il controllo ConsDef  è  uguale a FALSE  *37,* e  se la variabile MainClass_C1_variabile_V6 non è  minore di  *55,* 10 *38,* o  se il contatore MainClass_C1_contatore_Co7 non è  minore di  *55,* 124 e  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
    //   *61,* *34,*  se lo stato  è  uguale a  *53,*  state1  *106,* *34,* o  se il parametro MainClass_C1_parametro_P1 è  diverso da c270, Tutte le seguenti { 
    //   *62,*  se il controllo ConsDef è uguale a FALSE  *34,* o  se il parametro MainClass_C1_parametro_P2 è  diverso da  *56,* 9 *37,* o  se la variabile MainClass_C1_variabile_V6 è  minore di  *55,* 9 o  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
    //    se il controllo ConsDef è uguale a FALSE , Verifica che   *48,*   il controllo ConsDef  sia  uguale a FALSE 
    //   } Verifica che   *47,48,51,*  *,*  il contatore MainClass_C1_contatore_Co1 non sia  diverso da  *56,* 12
    //   *104,* e  che  *34,*  il parametro MainClass_C1_parametro_P1 sia  uguale a c270
    //   *104,* o  che   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* o  che  *38,*  il contatore MainClass_C1_contatore_Co7 non sia  maggiore di  *54,* 13
    //   *104,* e  che  *,*  il controllo MainClass_C1_controllo_C1 non sia  diverso da  True 
    //   } Verifica che   *48,*  *,*  il controllo MainClass_C1_controllo_C8 non sia  uguale a avanzamento
    //   } Verifica che   *47,48,49,50,*  *34,*  il parametro MainClass_C1_parametro_P1 non sia  uguale a c270
    //   *104,* o  che  *,*  la variabile MainClass_C1_variabile_V8 sia  diverso da  True 
    //   *104,* e  che   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* e  che  *,*  il timer MainClass_C1_timer_T6 non sia disattivo
    //   *104,* o  che  *34,*  il parametro MainClass_C1_parametro_P1 non sia  uguale a c270
    //   } Verifica che   *48,49,50,51,*  *,*  la variabile MainClass_C1_variabile_V6 sia  maggiore di  *54,* 5
    //   *104,* e  che  *,*  il timer MainClass_C1_timer_T6 non sia attivo
    //   *104,* e  che   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* o  che  *,*  il controllo MainClass_C1_controllo_C8 sia  diverso da avanzamento
    //   *104,* o  che  *,*  il contatore MainClass_C1_contatore_Co1 non sia  minore di  *55,* 1150213
    //   *104,* e  che  *37,*  la variabile MainClass_C1_variabile_V6 non sia  diverso da  *56,* 8
    //   } Verifica che   *47,48,50,51,*   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* o  che  *,*  la variabile MainClass_C1_variabile_V8 non sia  uguale a  False 
    //   *104,* e  che  *34,*  il parametro MainClass_C1_parametro_P9 sia  diverso da  False 
    //   *104,* o  che  *37,*  la variabile MainClass_C1_variabile_V6 sia  maggiore di  *54,* 7
    //   *104,* o  che  *,*  il controllo MainClass_C1_controllo_C1 non sia  diverso da  True 
    //   *104,* o  che  *,*  il contatore MainClass_C1_contatore_Co7 sia  minore di  *55,* 14
    //   } Verifica che   *47,51,*  *,*  il contatore MainClass_C1_contatore_Co7 sia  minore di  *55,* 14
    //   *104,* o  che  *34,*  il parametro MainClass_C1_parametro_P1 non sia  diverso da c270
    //   } Verifica che   *47,49,51,*  *34,*  il parametro MainClass_C1_parametro_P2 sia  maggiore di  *54,* 6
    //   *104,* o  che  *,*  il contatore MainClass_C1_contatore_Co1 non sia  uguale a  *53,* 1
    //   *104,* o  che  *38,*  il contatore MainClass_C1_contatore_Co7 sia  maggiore di  *54,* 102
    //   *104,* e  che  *,*  il timer MainClass_C1_timer_T6 non sia disattivo
    //   } Verifica che   *48,51,*   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* o  che  *,*  il controllo MainClass_C1_controllo_C8 non sia  uguale a avanzamento
    //   *104,* e  che  *,*  il contatore MainClass_C1_contatore_Co7 sia  diverso da  *56,* 11
    //   *104,* e  che  *38,*  il contatore MainClass_C1_contatore_Co1 non sia  minore di  *55,* 1113
    //   } Verifica che   *48,*  *,*  il controllo MainClass_C1_controllo_C7 sia  uguale a c180x
    //   } Verifica che   *47,49,50,51,*  *,*  il contatore MainClass_C1_contatore_Co7 sia  uguale a  *53,* 13
    //   *104,* o  che  *34,*  il parametro MainClass_C1_parametro_P2 sia  minore di  *55,* 6
    //   *104,* e  che  *,*  la variabile MainClass_C1_variabile_V6 sia  minore di  *55,* 10
    //   *104,* o  che  *37,*  la variabile MainClass_C1_variabile_V6 sia  maggiore di  *54,* 3
    //   *104,* e  che  *,*  il timer MainClass_C1_timer_T6 non sia disattivo
    //   *104,* o  che  *36,*  il timer MainClass_C1_timer_T6 non sia attivo
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (L_P1__GetStato1(my_id) == C1_St_state));
    if(res_NotLogicOP_2){
    bool res_XorLogicOP_3 = true;
    int xorIndex_res_XorLogicOP_3 = 0;
    bool res_ImpliesLogicOp_4 = true;
    bool res_OrLogicOP_5 = false;
    bool res_AndLogicOP_6 = true;
    res_AndLogicOP_6 = (res_AndLogicOP_6 && (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetMainc33(my_id) == true));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_7);
    
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_AndLogicOP_6);
    bool res_AndLogicOP_8 = true;
    bool res_AndLogicOP_9 = true;
    res_AndLogicOP_9 = (res_AndLogicOP_9 && (L_P1__GetParamMainc6(my_id) < 1u));
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (Counter_GetValore(L_P1__GetMainc44(my_id)) == 1150213u));
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_NotLogicOP_10);
    
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_AndLogicOP_9);
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (Counter_GetValore(L_P1__GetMainc44(my_id)) < 124u));
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_11);
    
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_AndLogicOP_8);
    
    if(res_OrLogicOP_5){
    bool res_OrLogicOP_12 = false;
    bool res_ImpliesLogicOp_13 = true;
    bool res_OrLogicOP_14 = false;
    bool res_OrLogicOP_15 = false;
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (L_P1__GetStato1(my_id) == C1_St_state));
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_NotLogicOP_16);
    bool res_NotLogicOP_17 = true;
    bool res_NotLogicOP_18 = true;
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! (L_P1__GetMainc33(my_id) == false));
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! res_NotLogicOP_18);
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_NotLogicOP_17);
    
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_OrLogicOP_15);
    bool res_NotLogicOP_19 = true;
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! (L_P1__GetParamMainc7(my_id) == true));
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! res_NotLogicOP_20);
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_NotLogicOP_19);
    
    if(res_OrLogicOP_14){
    bool res_XorLogicOP_21 = true;
    int xorIndex_res_XorLogicOP_21 = 0;
    bool res_ImpliesLogicOp_22 = true;
    bool res_OrLogicOP_23 = false;
    bool res_OrLogicOP_24 = false;
    bool res_OrLogicOP_25 = false;
    bool res_AndLogicOP_26 = true;
    bool res_AndLogicOP_27 = true;
    bool res_NotLogicOP_28 = true;
    bool res_NotLogicOP_29 = true;
    res_NotLogicOP_29 = (res_NotLogicOP_29 && ! (Counter_GetValore(L_P1__GetMainc43(my_id)) == 135u));
    res_NotLogicOP_28 = (res_NotLogicOP_28 && ! res_NotLogicOP_29);
    res_AndLogicOP_27 = (res_AndLogicOP_27 && res_NotLogicOP_28);
    res_AndLogicOP_27 = (res_AndLogicOP_27 && Timer_Attivo(L_P1__GetMainc42(my_id)));
    
    res_AndLogicOP_26 = (res_AndLogicOP_26 && res_AndLogicOP_27);
    bool res_NotLogicOP_30 = true;
    res_NotLogicOP_30 = (res_NotLogicOP_30 && ! (L_P1__GetParamMainc5(my_id) == c270));
    res_AndLogicOP_26 = (res_AndLogicOP_26 && res_NotLogicOP_30);
    
    res_OrLogicOP_25 = (res_OrLogicOP_25 || res_AndLogicOP_26);
    bool res_NotLogicOP_31 = true;
    res_NotLogicOP_31 = (res_NotLogicOP_31 && ! (L_P1__GetInMainc3(my_id) == c180x));
    res_OrLogicOP_25 = (res_OrLogicOP_25 || res_NotLogicOP_31);
    
    res_OrLogicOP_24 = (res_OrLogicOP_24 || res_OrLogicOP_25);
    bool res_NotLogicOP_32 = true;
    bool res_NotLogicOP_33 = true;
    res_NotLogicOP_33 = (res_NotLogicOP_33 && ! (L_P1__GetParamMainc6(my_id) == 10u));
    res_NotLogicOP_32 = (res_NotLogicOP_32 && ! res_NotLogicOP_33);
    res_OrLogicOP_24 = (res_OrLogicOP_24 || res_NotLogicOP_32);
    
    res_OrLogicOP_23 = (res_OrLogicOP_23 || res_OrLogicOP_24);
    bool res_NotLogicOP_34 = true;
    res_NotLogicOP_34 = (res_NotLogicOP_34 && ! (L_P1__GetParamMainc7(my_id) == true));
    res_OrLogicOP_23 = (res_OrLogicOP_23 || res_NotLogicOP_34);
    
    if(res_OrLogicOP_23){
    bool res_XorLogicOP_35 = true;
    int xorIndex_res_XorLogicOP_35 = 0;
    bool res_ImpliesLogicOp_36 = true;
    bool res_OrLogicOP_37 = false;
    bool res_OrLogicOP_38 = false;
    bool res_AndLogicOP_39 = true;
    res_AndLogicOP_39 = (res_AndLogicOP_39 && (L_P1__GetParamMainc6(my_id) == 8u));
    bool res_NotLogicOP_40 = true;
    res_NotLogicOP_40 = (res_NotLogicOP_40 && ! (L_P1__GetParamMainc5(my_id) == c270));
    res_AndLogicOP_39 = (res_AndLogicOP_39 && res_NotLogicOP_40);
    
    res_OrLogicOP_38 = (res_OrLogicOP_38 || res_AndLogicOP_39);
    bool res_AndLogicOP_41 = true;
    res_AndLogicOP_41 = (res_AndLogicOP_41 && (L_P1__GetInConsd(my_id) == false));
    res_AndLogicOP_41 = (res_AndLogicOP_41 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_38 = (res_OrLogicOP_38 || res_AndLogicOP_41);
    
    res_OrLogicOP_37 = (res_OrLogicOP_37 || res_OrLogicOP_38);
    bool res_AndLogicOP_42 = true;
    bool res_NotLogicOP_43 = true;
    res_NotLogicOP_43 = (res_NotLogicOP_43 && ! (Counter_GetValore(L_P1__GetMainc44(my_id)) > 120213u));
    res_AndLogicOP_42 = (res_AndLogicOP_42 && res_NotLogicOP_43);
    bool res_NotLogicOP_44 = true;
    res_NotLogicOP_44 = (res_NotLogicOP_44 && ! (Counter_GetValore(L_P1__GetMainc44(my_id)) > 14u));
    res_AndLogicOP_42 = (res_AndLogicOP_42 && res_NotLogicOP_44);
    
    res_OrLogicOP_37 = (res_OrLogicOP_37 || res_AndLogicOP_42);
    
    if(res_OrLogicOP_37){
    bool res_XorLogicOP_45 = true;
    int xorIndex_res_XorLogicOP_45 = 0;
    bool res_ImpliesLogicOp_46 = true;
    if(Timer_Scaduto(L_P1__GetMainc42(my_id))){
    bool res_XorLogicOP_47 = true;
    int xorIndex_res_XorLogicOP_47 = 0;
    bool res_ImpliesLogicOp_48 = true;
    bool res_OrLogicOP_49 = false;
    bool res_AndLogicOP_50 = true;
    bool res_NotLogicOP_51 = true;
    res_NotLogicOP_51 = (res_NotLogicOP_51 && ! Timer_Scaduto(L_P1__GetMainc41(my_id)));
    res_AndLogicOP_50 = (res_AndLogicOP_50 && res_NotLogicOP_51);
    bool res_NotLogicOP_52 = true;
    res_NotLogicOP_52 = (res_NotLogicOP_52 && ! (L_P1__GetMainc32(my_id) == 9u));
    res_AndLogicOP_50 = (res_AndLogicOP_50 && res_NotLogicOP_52);
    
    res_OrLogicOP_49 = (res_OrLogicOP_49 || res_AndLogicOP_50);
    bool res_AndLogicOP_53 = true;
    bool res_NotLogicOP_54 = true;
    res_NotLogicOP_54 = (res_NotLogicOP_54 && ! (L_P1__GetInMainc2(my_id) == false));
    res_AndLogicOP_53 = (res_AndLogicOP_53 && res_NotLogicOP_54);
    res_AndLogicOP_53 = (res_AndLogicOP_53 && (L_P1__GetInMainc3(my_id) == c180x));
    
    res_OrLogicOP_49 = (res_OrLogicOP_49 || res_AndLogicOP_53);
    
    if(res_OrLogicOP_49){
    bool res_AndLogicOP_55 = true;
    bool res_ImpliesLogicOp_56 = true;
    bool res_OrLogicOP_57 = false;
    bool res_OrLogicOP_58 = false;
    bool res_OrLogicOP_59 = false;
    bool res_NotLogicOP_60 = true;
    res_NotLogicOP_60 = (res_NotLogicOP_60 && ! (Counter_GetValore(L_P1__GetMainc44(my_id)) == 14u));
    res_OrLogicOP_59 = (res_OrLogicOP_59 || res_NotLogicOP_60);
    res_OrLogicOP_59 = (res_OrLogicOP_59 || (L_P1__GetInMainc2(my_id) == true));
    
    res_OrLogicOP_58 = (res_OrLogicOP_58 || res_OrLogicOP_59);
    bool res_NotLogicOP_61 = true;
    res_NotLogicOP_61 = (res_NotLogicOP_61 && ! (L_P1__GetMainc33(my_id) == true));
    res_OrLogicOP_58 = (res_OrLogicOP_58 || res_NotLogicOP_61);
    
    res_OrLogicOP_57 = (res_OrLogicOP_57 || res_OrLogicOP_58);
    bool res_AndLogicOP_62 = true;
    bool res_NotLogicOP_63 = true;
    res_NotLogicOP_63 = (res_NotLogicOP_63 && ! (L_P1__GetParamMainc6(my_id) > 4u));
    res_AndLogicOP_62 = (res_AndLogicOP_62 && res_NotLogicOP_63);
    res_AndLogicOP_62 = (res_AndLogicOP_62 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_57 = (res_OrLogicOP_57 || res_AndLogicOP_62);
    
    if(res_OrLogicOP_57){
    bool res_XorLogicOP_64 = true;
    int xorIndex_res_XorLogicOP_64 = 0;
    bool res_ImpliesLogicOp_65 = true;
    bool res_OrLogicOP_66 = false;
    bool res_OrLogicOP_67 = false;
    bool res_OrLogicOP_68 = false;
    bool res_NotLogicOP_69 = true;
    res_NotLogicOP_69 = (res_NotLogicOP_69 && ! (L_P1__GetParamMainc7(my_id) == true));
    res_OrLogicOP_68 = (res_OrLogicOP_68 || res_NotLogicOP_69);
    bool res_NotLogicOP_70 = true;
    res_NotLogicOP_70 = (res_NotLogicOP_70 && ! (Counter_GetValore(L_P1__GetMainc44(my_id)) > 11u));
    res_OrLogicOP_68 = (res_OrLogicOP_68 || res_NotLogicOP_70);
    
    res_OrLogicOP_67 = (res_OrLogicOP_67 || res_OrLogicOP_68);
    bool res_AndLogicOP_71 = true;
    res_AndLogicOP_71 = (res_AndLogicOP_71 && (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_72 = true;
    res_NotLogicOP_72 = (res_NotLogicOP_72 && ! (L_P1__GetMainc32(my_id) < 10u));
    res_AndLogicOP_71 = (res_AndLogicOP_71 && res_NotLogicOP_72);
    
    res_OrLogicOP_67 = (res_OrLogicOP_67 || res_AndLogicOP_71);
    
    res_OrLogicOP_66 = (res_OrLogicOP_66 || res_OrLogicOP_67);
    bool res_AndLogicOP_73 = true;
    bool res_NotLogicOP_74 = true;
    res_NotLogicOP_74 = (res_NotLogicOP_74 && ! (Counter_GetValore(L_P1__GetMainc44(my_id)) < 124u));
    res_AndLogicOP_73 = (res_AndLogicOP_73 && res_NotLogicOP_74);
    res_AndLogicOP_73 = (res_AndLogicOP_73 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_66 = (res_OrLogicOP_66 || res_AndLogicOP_73);
    
    if(res_OrLogicOP_66){
    bool res_OrLogicOP_75 = false;
    bool res_ImpliesLogicOp_76 = true;
    bool res_OrLogicOP_77 = false;
    res_OrLogicOP_77 = (res_OrLogicOP_77 || (L_P1_C1_GetState(my_id) == C1_St_state));
    bool res_NotLogicOP_78 = true;
    res_NotLogicOP_78 = (res_NotLogicOP_78 && ! (L_P1__GetParamMainc5(my_id) == c270));
    res_OrLogicOP_77 = (res_OrLogicOP_77 || res_NotLogicOP_78);
    
    if(res_OrLogicOP_77){
    bool res_AndLogicOP_79 = true;
    bool res_ImpliesLogicOp_80 = true;
    bool res_OrLogicOP_81 = false;
    bool res_OrLogicOP_82 = false;
    bool res_OrLogicOP_83 = false;
    res_OrLogicOP_83 = (res_OrLogicOP_83 || (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_84 = true;
    res_NotLogicOP_84 = (res_NotLogicOP_84 && ! (L_P1__GetParamMainc6(my_id) == 9u));
    res_OrLogicOP_83 = (res_OrLogicOP_83 || res_NotLogicOP_84);
    
    res_OrLogicOP_82 = (res_OrLogicOP_82 || res_OrLogicOP_83);
    res_OrLogicOP_82 = (res_OrLogicOP_82 || (L_P1__GetMainc32(my_id) < 9u));
    
    res_OrLogicOP_81 = (res_OrLogicOP_81 || res_OrLogicOP_82);
    res_OrLogicOP_81 = (res_OrLogicOP_81 || (L_P1__GetInConsd(my_id) == false));
    
    if(res_OrLogicOP_81){
    bool res_ImpliesLogicOp_85 = true;
    if((L_P1__GetInConsd(my_id) == false)){
    res_ImpliesLogicOp_85 = (res_ImpliesLogicOp_85 && (L_P1__GetInConsd(my_id) == false));
    }
    res_ImpliesLogicOp_80 = (res_ImpliesLogicOp_80 && res_ImpliesLogicOp_85);
    }
    res_AndLogicOP_79 = (res_AndLogicOP_79 && res_ImpliesLogicOp_80);
    bool res_OrLogicOP_86 = false;
    bool res_OrLogicOP_87 = false;
    bool res_AndLogicOP_88 = true;
    bool res_NotLogicOP_89 = true;
    bool res_NotLogicOP_90 = true;
    res_NotLogicOP_90 = (res_NotLogicOP_90 && ! (Counter_GetValore(L_P1__GetMainc43(my_id)) == 12u));
    res_NotLogicOP_89 = (res_NotLogicOP_89 && ! res_NotLogicOP_90);
    res_AndLogicOP_88 = (res_AndLogicOP_88 && res_NotLogicOP_89);
    res_AndLogicOP_88 = (res_AndLogicOP_88 && (L_P1__GetParamMainc5(my_id) == c270));
    
    res_OrLogicOP_87 = (res_OrLogicOP_87 || res_AndLogicOP_88);
    res_OrLogicOP_87 = (res_OrLogicOP_87 || (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_86 = (res_OrLogicOP_86 || res_OrLogicOP_87);
    bool res_AndLogicOP_91 = true;
    bool res_NotLogicOP_92 = true;
    res_NotLogicOP_92 = (res_NotLogicOP_92 && ! (Counter_GetValore(L_P1__GetMainc44(my_id)) > 13u));
    res_AndLogicOP_91 = (res_AndLogicOP_91 && res_NotLogicOP_92);
    bool res_NotLogicOP_93 = true;
    bool res_NotLogicOP_94 = true;
    res_NotLogicOP_94 = (res_NotLogicOP_94 && ! (L_P1__GetInMainc2(my_id) == true));
    res_NotLogicOP_93 = (res_NotLogicOP_93 && ! res_NotLogicOP_94);
    res_AndLogicOP_91 = (res_AndLogicOP_91 && res_NotLogicOP_93);
    
    res_OrLogicOP_86 = (res_OrLogicOP_86 || res_AndLogicOP_91);
    
    res_AndLogicOP_79 = (res_AndLogicOP_79 && res_OrLogicOP_86);
    
    res_ImpliesLogicOp_76 = (res_ImpliesLogicOp_76 && res_AndLogicOP_79);
    }
    res_OrLogicOP_75 = (res_OrLogicOP_75 || res_ImpliesLogicOp_76);
    bool res_NotLogicOP_95 = true;
    res_NotLogicOP_95 = (res_NotLogicOP_95 && ! (L_P1__GetInMainc4(my_id) == avanzamento));
    res_OrLogicOP_75 = (res_OrLogicOP_75 || res_NotLogicOP_95);
    
    res_ImpliesLogicOp_65 = (res_ImpliesLogicOp_65 && res_OrLogicOP_75);
    }
    if(res_ImpliesLogicOp_65){
    xorIndex_res_XorLogicOP_64 = (xorIndex_res_XorLogicOP_64 + 1);
    }
    bool res_OrLogicOP_96 = false;
    bool res_OrLogicOP_97 = false;
    bool res_NotLogicOP_98 = true;
    res_NotLogicOP_98 = (res_NotLogicOP_98 && ! (L_P1__GetParamMainc5(my_id) == c270));
    res_OrLogicOP_97 = (res_OrLogicOP_97 || res_NotLogicOP_98);
    bool res_AndLogicOP_99 = true;
    bool res_AndLogicOP_100 = true;
    bool res_NotLogicOP_101 = true;
    res_NotLogicOP_101 = (res_NotLogicOP_101 && ! (L_P1__GetMainc33(my_id) == true));
    res_AndLogicOP_100 = (res_AndLogicOP_100 && res_NotLogicOP_101);
    res_AndLogicOP_100 = (res_AndLogicOP_100 && (L_P1__GetInConsd(my_id) == false));
    
    res_AndLogicOP_99 = (res_AndLogicOP_99 && res_AndLogicOP_100);
    bool res_NotLogicOP_102 = true;
    res_NotLogicOP_102 = (res_NotLogicOP_102 && ! Timer_Disattivo(L_P1__GetMainc42(my_id)));
    res_AndLogicOP_99 = (res_AndLogicOP_99 && res_NotLogicOP_102);
    
    res_OrLogicOP_97 = (res_OrLogicOP_97 || res_AndLogicOP_99);
    
    res_OrLogicOP_96 = (res_OrLogicOP_96 || res_OrLogicOP_97);
    bool res_NotLogicOP_103 = true;
    res_NotLogicOP_103 = (res_NotLogicOP_103 && ! (L_P1__GetParamMainc5(my_id) == c270));
    res_OrLogicOP_96 = (res_OrLogicOP_96 || res_NotLogicOP_103);
    
    if(res_OrLogicOP_96){
    xorIndex_res_XorLogicOP_64 = (xorIndex_res_XorLogicOP_64 + 1);
    }
    
    res_XorLogicOP_64 = (res_XorLogicOP_64 && (xorIndex_res_XorLogicOP_64 == 1));
    res_ImpliesLogicOp_56 = (res_ImpliesLogicOp_56 && res_XorLogicOP_64);
    }
    res_AndLogicOP_55 = (res_AndLogicOP_55 && res_ImpliesLogicOp_56);
    bool res_OrLogicOP_104 = false;
    bool res_OrLogicOP_105 = false;
    bool res_AndLogicOP_106 = true;
    bool res_AndLogicOP_107 = true;
    res_AndLogicOP_107 = (res_AndLogicOP_107 && (L_P1__GetMainc32(my_id) > 5u));
    bool res_NotLogicOP_108 = true;
    res_NotLogicOP_108 = (res_NotLogicOP_108 && ! Timer_Attivo(L_P1__GetMainc42(my_id)));
    res_AndLogicOP_107 = (res_AndLogicOP_107 && res_NotLogicOP_108);
    
    res_AndLogicOP_106 = (res_AndLogicOP_106 && res_AndLogicOP_107);
    res_AndLogicOP_106 = (res_AndLogicOP_106 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_105 = (res_OrLogicOP_105 || res_AndLogicOP_106);
    bool res_NotLogicOP_109 = true;
    res_NotLogicOP_109 = (res_NotLogicOP_109 && ! (L_P1__GetInMainc4(my_id) == avanzamento));
    res_OrLogicOP_105 = (res_OrLogicOP_105 || res_NotLogicOP_109);
    
    res_OrLogicOP_104 = (res_OrLogicOP_104 || res_OrLogicOP_105);
    bool res_AndLogicOP_110 = true;
    bool res_NotLogicOP_111 = true;
    res_NotLogicOP_111 = (res_NotLogicOP_111 && ! (Counter_GetValore(L_P1__GetMainc43(my_id)) < 1150213u));
    res_AndLogicOP_110 = (res_AndLogicOP_110 && res_NotLogicOP_111);
    bool res_NotLogicOP_112 = true;
    bool res_NotLogicOP_113 = true;
    res_NotLogicOP_113 = (res_NotLogicOP_113 && ! (L_P1__GetMainc32(my_id) == 8u));
    res_NotLogicOP_112 = (res_NotLogicOP_112 && ! res_NotLogicOP_113);
    res_AndLogicOP_110 = (res_AndLogicOP_110 && res_NotLogicOP_112);
    
    res_OrLogicOP_104 = (res_OrLogicOP_104 || res_AndLogicOP_110);
    
    res_AndLogicOP_55 = (res_AndLogicOP_55 && res_OrLogicOP_104);
    
    res_ImpliesLogicOp_48 = (res_ImpliesLogicOp_48 && res_AndLogicOP_55);
    }
    if(res_ImpliesLogicOp_48){
    xorIndex_res_XorLogicOP_47 = (xorIndex_res_XorLogicOP_47 + 1);
    }
    bool res_OrLogicOP_114 = false;
    bool res_OrLogicOP_115 = false;
    bool res_OrLogicOP_116 = false;
    bool res_OrLogicOP_117 = false;
    res_OrLogicOP_117 = (res_OrLogicOP_117 || (L_P1__GetInConsd(my_id) == false));
    bool res_AndLogicOP_118 = true;
    bool res_NotLogicOP_119 = true;
    res_NotLogicOP_119 = (res_NotLogicOP_119 && ! (L_P1__GetMainc33(my_id) == false));
    res_AndLogicOP_118 = (res_AndLogicOP_118 && res_NotLogicOP_119);
    bool res_NotLogicOP_120 = true;
    res_NotLogicOP_120 = (res_NotLogicOP_120 && ! (L_P1__GetParamMainc7(my_id) == false));
    res_AndLogicOP_118 = (res_AndLogicOP_118 && res_NotLogicOP_120);
    
    res_OrLogicOP_117 = (res_OrLogicOP_117 || res_AndLogicOP_118);
    
    res_OrLogicOP_116 = (res_OrLogicOP_116 || res_OrLogicOP_117);
    res_OrLogicOP_116 = (res_OrLogicOP_116 || (L_P1__GetMainc32(my_id) > 7u));
    
    res_OrLogicOP_115 = (res_OrLogicOP_115 || res_OrLogicOP_116);
    bool res_NotLogicOP_121 = true;
    bool res_NotLogicOP_122 = true;
    res_NotLogicOP_122 = (res_NotLogicOP_122 && ! (L_P1__GetInMainc2(my_id) == true));
    res_NotLogicOP_121 = (res_NotLogicOP_121 && ! res_NotLogicOP_122);
    res_OrLogicOP_115 = (res_OrLogicOP_115 || res_NotLogicOP_121);
    
    res_OrLogicOP_114 = (res_OrLogicOP_114 || res_OrLogicOP_115);
    res_OrLogicOP_114 = (res_OrLogicOP_114 || (Counter_GetValore(L_P1__GetMainc44(my_id)) < 14u));
    
    if(res_OrLogicOP_114){
    xorIndex_res_XorLogicOP_47 = (xorIndex_res_XorLogicOP_47 + 1);
    }
    
    res_XorLogicOP_47 = (res_XorLogicOP_47 && (xorIndex_res_XorLogicOP_47 == 1));
    res_ImpliesLogicOp_46 = (res_ImpliesLogicOp_46 && res_XorLogicOP_47);
    }
    if(res_ImpliesLogicOp_46){
    xorIndex_res_XorLogicOP_45 = (xorIndex_res_XorLogicOP_45 + 1);
    }
    bool res_OrLogicOP_123 = false;
    res_OrLogicOP_123 = (res_OrLogicOP_123 || (Counter_GetValore(L_P1__GetMainc44(my_id)) < 14u));
    bool res_NotLogicOP_124 = true;
    bool res_NotLogicOP_125 = true;
    res_NotLogicOP_125 = (res_NotLogicOP_125 && ! (L_P1__GetParamMainc5(my_id) == c270));
    res_NotLogicOP_124 = (res_NotLogicOP_124 && ! res_NotLogicOP_125);
    res_OrLogicOP_123 = (res_OrLogicOP_123 || res_NotLogicOP_124);
    
    if(res_OrLogicOP_123){
    xorIndex_res_XorLogicOP_45 = (xorIndex_res_XorLogicOP_45 + 1);
    }
    
    res_XorLogicOP_45 = (res_XorLogicOP_45 && (xorIndex_res_XorLogicOP_45 == 1));
    res_ImpliesLogicOp_36 = (res_ImpliesLogicOp_36 && res_XorLogicOP_45);
    }
    if(res_ImpliesLogicOp_36){
    xorIndex_res_XorLogicOP_35 = (xorIndex_res_XorLogicOP_35 + 1);
    }
    bool res_OrLogicOP_126 = false;
    bool res_OrLogicOP_127 = false;
    res_OrLogicOP_127 = (res_OrLogicOP_127 || (L_P1__GetParamMainc6(my_id) > 6u));
    bool res_NotLogicOP_128 = true;
    res_NotLogicOP_128 = (res_NotLogicOP_128 && ! (Counter_GetValore(L_P1__GetMainc43(my_id)) == 1u));
    res_OrLogicOP_127 = (res_OrLogicOP_127 || res_NotLogicOP_128);
    
    res_OrLogicOP_126 = (res_OrLogicOP_126 || res_OrLogicOP_127);
    bool res_AndLogicOP_129 = true;
    res_AndLogicOP_129 = (res_AndLogicOP_129 && (Counter_GetValore(L_P1__GetMainc44(my_id)) > 102u));
    bool res_NotLogicOP_130 = true;
    res_NotLogicOP_130 = (res_NotLogicOP_130 && ! Timer_Disattivo(L_P1__GetMainc42(my_id)));
    res_AndLogicOP_129 = (res_AndLogicOP_129 && res_NotLogicOP_130);
    
    res_OrLogicOP_126 = (res_OrLogicOP_126 || res_AndLogicOP_129);
    
    if(res_OrLogicOP_126){
    xorIndex_res_XorLogicOP_35 = (xorIndex_res_XorLogicOP_35 + 1);
    }
    
    res_XorLogicOP_35 = (res_XorLogicOP_35 && (xorIndex_res_XorLogicOP_35 == 1));
    res_ImpliesLogicOp_22 = (res_ImpliesLogicOp_22 && res_XorLogicOP_35);
    }
    if(res_ImpliesLogicOp_22){
    xorIndex_res_XorLogicOP_21 = (xorIndex_res_XorLogicOP_21 + 1);
    }
    bool res_OrLogicOP_131 = false;
    res_OrLogicOP_131 = (res_OrLogicOP_131 || (L_P1__GetInConsd(my_id) == false));
    bool res_AndLogicOP_132 = true;
    bool res_AndLogicOP_133 = true;
    bool res_NotLogicOP_134 = true;
    res_NotLogicOP_134 = (res_NotLogicOP_134 && ! (L_P1__GetInMainc4(my_id) == avanzamento));
    res_AndLogicOP_133 = (res_AndLogicOP_133 && res_NotLogicOP_134);
    bool res_NotLogicOP_135 = true;
    res_NotLogicOP_135 = (res_NotLogicOP_135 && ! (Counter_GetValore(L_P1__GetMainc44(my_id)) == 11u));
    res_AndLogicOP_133 = (res_AndLogicOP_133 && res_NotLogicOP_135);
    
    res_AndLogicOP_132 = (res_AndLogicOP_132 && res_AndLogicOP_133);
    bool res_NotLogicOP_136 = true;
    res_NotLogicOP_136 = (res_NotLogicOP_136 && ! (Counter_GetValore(L_P1__GetMainc43(my_id)) < 1113u));
    res_AndLogicOP_132 = (res_AndLogicOP_132 && res_NotLogicOP_136);
    
    res_OrLogicOP_131 = (res_OrLogicOP_131 || res_AndLogicOP_132);
    
    if(res_OrLogicOP_131){
    xorIndex_res_XorLogicOP_21 = (xorIndex_res_XorLogicOP_21 + 1);
    }
    
    res_XorLogicOP_21 = (res_XorLogicOP_21 && (xorIndex_res_XorLogicOP_21 == 1));
    res_ImpliesLogicOp_13 = (res_ImpliesLogicOp_13 && res_XorLogicOP_21);
    }
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_ImpliesLogicOp_13);
    res_OrLogicOP_12 = (res_OrLogicOP_12 || (L_P1__GetInMainc3(my_id) == c180x));
    
    res_ImpliesLogicOp_4 = (res_ImpliesLogicOp_4 && res_OrLogicOP_12);
    }
    if(res_ImpliesLogicOp_4){
    xorIndex_res_XorLogicOP_3 = (xorIndex_res_XorLogicOP_3 + 1);
    }
    bool res_OrLogicOP_137 = false;
    bool res_OrLogicOP_138 = false;
    bool res_OrLogicOP_139 = false;
    res_OrLogicOP_139 = (res_OrLogicOP_139 || (Counter_GetValore(L_P1__GetMainc44(my_id)) == 13u));
    bool res_AndLogicOP_140 = true;
    res_AndLogicOP_140 = (res_AndLogicOP_140 && (L_P1__GetParamMainc6(my_id) < 6u));
    res_AndLogicOP_140 = (res_AndLogicOP_140 && (L_P1__GetMainc32(my_id) < 10u));
    
    res_OrLogicOP_139 = (res_OrLogicOP_139 || res_AndLogicOP_140);
    
    res_OrLogicOP_138 = (res_OrLogicOP_138 || res_OrLogicOP_139);
    bool res_AndLogicOP_141 = true;
    res_AndLogicOP_141 = (res_AndLogicOP_141 && (L_P1__GetMainc32(my_id) > 3u));
    bool res_NotLogicOP_142 = true;
    res_NotLogicOP_142 = (res_NotLogicOP_142 && ! Timer_Disattivo(L_P1__GetMainc42(my_id)));
    res_AndLogicOP_141 = (res_AndLogicOP_141 && res_NotLogicOP_142);
    
    res_OrLogicOP_138 = (res_OrLogicOP_138 || res_AndLogicOP_141);
    
    res_OrLogicOP_137 = (res_OrLogicOP_137 || res_OrLogicOP_138);
    bool res_NotLogicOP_143 = true;
    res_NotLogicOP_143 = (res_NotLogicOP_143 && ! Timer_Attivo(L_P1__GetMainc42(my_id)));
    res_OrLogicOP_137 = (res_OrLogicOP_137 || res_NotLogicOP_143);
    
    if(res_OrLogicOP_137){
    xorIndex_res_XorLogicOP_3 = (xorIndex_res_XorLogicOP_3 + 1);
    }
    
    res_XorLogicOP_3 = (res_XorLogicOP_3 && (xorIndex_res_XorLogicOP_3 == 1));
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_XorLogicOP_3);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *47,48,49,50,*  *,*  il timer MainClass_C1_timer_T6 non sia scaduto
    //   *104,* e  che  *36,*  il timer MainClass_C1_timer_T6 sia attivo
    //   *104,* e  che   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* o  che  *36,*  il timer MainClass_C1_timer_T6 sia disattivo
    //   *104,* o  che  *34,*  il parametro MainClass_C1_parametro_P9 non sia  uguale a  True 
    //   *104,* e  che  *,*  la variabile MainClass_C1_variabile_V8 sia  uguale a  False
    bool res_OrLogicOP_144 = false;
    bool res_OrLogicOP_145 = false;
    bool res_AndLogicOP_146 = true;
    bool res_AndLogicOP_147 = true;
    bool res_NotLogicOP_148 = true;
    res_NotLogicOP_148 = (res_NotLogicOP_148 && ! Timer_Scaduto(L_P1__GetMainc42(my_id)));
    res_AndLogicOP_147 = (res_AndLogicOP_147 && res_NotLogicOP_148);
    res_AndLogicOP_147 = (res_AndLogicOP_147 && Timer_Attivo(L_P1__GetMainc42(my_id)));
    
    res_AndLogicOP_146 = (res_AndLogicOP_146 && res_AndLogicOP_147);
    res_AndLogicOP_146 = (res_AndLogicOP_146 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_145 = (res_OrLogicOP_145 || res_AndLogicOP_146);
    res_OrLogicOP_145 = (res_OrLogicOP_145 || Timer_Disattivo(L_P1__GetMainc42(my_id)));
    
    res_OrLogicOP_144 = (res_OrLogicOP_144 || res_OrLogicOP_145);
    bool res_AndLogicOP_149 = true;
    bool res_NotLogicOP_150 = true;
    res_NotLogicOP_150 = (res_NotLogicOP_150 && ! (L_P1__GetParamMainc7(my_id) == true));
    res_AndLogicOP_149 = (res_AndLogicOP_149 && res_NotLogicOP_150);
    res_AndLogicOP_149 = (res_AndLogicOP_149 && (L_P1__GetMainc33(my_id) == false));
    
    res_OrLogicOP_144 = (res_OrLogicOP_144 || res_AndLogicOP_149);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_144);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
     
    { commento: {62,} commento: {38,}  se il contatore MainClass_C1_contatore_Co7 è  minore di  commento: {55,} 1113 commento: {37,} e  se la variabile MainClass_C1_variabile_V6 non è  minore di  commento: {55,} 10 commento: {37,} o  se la variabile MainClass_C1_variabile_V8 non è  diverso da  False  e  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} e  se la variabile MainClass_C1_variabile_V6 non è  maggiore di  commento: {54,} 2 commento: {38,} e  se il contatore MainClass_C1_contatore_Co7 non è  diverso da  commento: {56,} 1145, Almeno una delle seguenti { 
     commento: {36,}  se il timer MainClass_C1_timer_T6 non è disattivo commento: {35,} e  se il controllo MainClass_C1_controllo_C8 è  diverso da avanzamento commento: {35,} e  se il controllo MainClass_C1_controllo_C1 non è  diverso da  True  commento: {38,} e  se il contatore MainClass_C1_contatore_Co1 non è  maggiore di  commento: {54,} 15021 commento: {34,} e  se il parametro MainClass_C1_parametro_P9 è  diverso da  True , Verifica che   commento: {47,48,49,51,}  commento: {34,}  il parametro MainClass_C1_parametro_P1 sia  uguale a c270
     commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co7 sia  maggiore di  commento: {54,} 14
     commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T6 non sia attivo
     commento: {104,} e  che  commento: {36,}  il timer MainClass_C1_timer_T6 sia disattivo
     commento: {104,} o  che  commento: {36,}  il timer MainClass_C1_timer_T6 sia attivo
     commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C7 non sia  uguale a c180x
    
    
     } Verifica che   commento: {48,49,51,}  commento: {,}  il timer MainClass_C1_timer_T6 sia attivo
     commento: {104,} o  che  commento: {,}  il contatore MainClass_C1_contatore_Co1 non sia  minore di  commento: {55,} 15
     commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} o  che  commento: {36,}  il timer MainClass_C1_timer_T6 non sia attivo
    
    
    }
*/
bool L_P1__Macro9(instance_id_t const my_id )
{
bool res_AndLogicOP_0 = true;
    
    //  *62,* *38,*  se il contatore MainClass_C1_contatore_Co7 è  minore di  *55,* 1113 *37,* e  se la variabile MainClass_C1_variabile_V6 non è  minore di  *55,* 10 *37,* o  se la variabile MainClass_C1_variabile_V8 non è  diverso da  False  e  se il controllo ConsDef  è  uguale a FALSE  *37,* e  se la variabile MainClass_C1_variabile_V6 non è  maggiore di  *54,* 2 *38,* e  se il contatore MainClass_C1_contatore_Co7 non è  diverso da  *56,* 1145, Almeno una delle seguenti { 
    //   *36,*  se il timer MainClass_C1_timer_T6 non è disattivo *35,* e  se il controllo MainClass_C1_controllo_C8 è  diverso da avanzamento *35,* e  se il controllo MainClass_C1_controllo_C1 non è  diverso da  True  *38,* e  se il contatore MainClass_C1_contatore_Co1 non è  maggiore di  *54,* 15021 *34,* e  se il parametro MainClass_C1_parametro_P9 è  diverso da  True , Verifica che   *47,48,49,51,*  *34,*  il parametro MainClass_C1_parametro_P1 sia  uguale a c270
    //   *104,* e  che  *,*  il contatore MainClass_C1_contatore_Co7 sia  maggiore di  *54,* 14
    //   *104,* e  che  *,*  il timer MainClass_C1_timer_T6 non sia attivo
    //   *104,* e  che  *36,*  il timer MainClass_C1_timer_T6 sia disattivo
    //   *104,* o  che  *36,*  il timer MainClass_C1_timer_T6 sia attivo
    //   *104,* e  che  *,*  il controllo MainClass_C1_controllo_C7 non sia  uguale a c180x
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_AndLogicOP_3 = true;
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (Counter_GetValore(L_P1__GetMainc44(my_id)) < 1113u));
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetMainc32(my_id) < 10u));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_4);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_3);
    bool res_AndLogicOP_5 = true;
    bool res_AndLogicOP_6 = true;
    bool res_AndLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetMainc33(my_id) == false));
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! res_NotLogicOP_9);
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_8);
    res_AndLogicOP_7 = (res_AndLogicOP_7 && (L_P1__GetInConsd(my_id) == false));
    
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_AndLogicOP_7);
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__GetMainc32(my_id) > 2u));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_10);
    
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_AndLogicOP_6);
    bool res_NotLogicOP_11 = true;
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (Counter_GetValore(L_P1__GetMainc44(my_id)) == 1145u));
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! res_NotLogicOP_12);
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_11);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_5);
    
    if(res_OrLogicOP_2){
    bool res_ImpliesLogicOp_13 = true;
    bool res_AndLogicOP_14 = true;
    bool res_AndLogicOP_15 = true;
    bool res_AndLogicOP_16 = true;
    bool res_AndLogicOP_17 = true;
    bool res_NotLogicOP_18 = true;
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! Timer_Disattivo(L_P1__GetMainc42(my_id)));
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_NotLogicOP_18);
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (L_P1__GetInMainc4(my_id) == avanzamento));
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_NotLogicOP_19);
    
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_AndLogicOP_17);
    bool res_NotLogicOP_20 = true;
    bool res_NotLogicOP_21 = true;
    res_NotLogicOP_21 = (res_NotLogicOP_21 && ! (L_P1__GetInMainc2(my_id) == true));
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! res_NotLogicOP_21);
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_NotLogicOP_20);
    
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_AndLogicOP_16);
    bool res_NotLogicOP_22 = true;
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! (Counter_GetValore(L_P1__GetMainc43(my_id)) > 15021u));
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_NotLogicOP_22);
    
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_AndLogicOP_15);
    bool res_NotLogicOP_23 = true;
    res_NotLogicOP_23 = (res_NotLogicOP_23 && ! (L_P1__GetParamMainc7(my_id) == true));
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_NotLogicOP_23);
    
    if(res_AndLogicOP_14){
    bool res_OrLogicOP_24 = false;
    bool res_AndLogicOP_25 = true;
    bool res_AndLogicOP_26 = true;
    bool res_AndLogicOP_27 = true;
    res_AndLogicOP_27 = (res_AndLogicOP_27 && (L_P1__GetParamMainc5(my_id) == c270));
    res_AndLogicOP_27 = (res_AndLogicOP_27 && (Counter_GetValore(L_P1__GetMainc44(my_id)) > 14u));
    
    res_AndLogicOP_26 = (res_AndLogicOP_26 && res_AndLogicOP_27);
    bool res_NotLogicOP_28 = true;
    res_NotLogicOP_28 = (res_NotLogicOP_28 && ! Timer_Attivo(L_P1__GetMainc42(my_id)));
    res_AndLogicOP_26 = (res_AndLogicOP_26 && res_NotLogicOP_28);
    
    res_AndLogicOP_25 = (res_AndLogicOP_25 && res_AndLogicOP_26);
    res_AndLogicOP_25 = (res_AndLogicOP_25 && Timer_Disattivo(L_P1__GetMainc42(my_id)));
    
    res_OrLogicOP_24 = (res_OrLogicOP_24 || res_AndLogicOP_25);
    bool res_AndLogicOP_29 = true;
    res_AndLogicOP_29 = (res_AndLogicOP_29 && Timer_Attivo(L_P1__GetMainc42(my_id)));
    bool res_NotLogicOP_30 = true;
    res_NotLogicOP_30 = (res_NotLogicOP_30 && ! (L_P1__GetInMainc3(my_id) == c180x));
    res_AndLogicOP_29 = (res_AndLogicOP_29 && res_NotLogicOP_30);
    
    res_OrLogicOP_24 = (res_OrLogicOP_24 || res_AndLogicOP_29);
    
    res_ImpliesLogicOp_13 = (res_ImpliesLogicOp_13 && res_OrLogicOP_24);
    }
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_ImpliesLogicOp_13);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *48,49,51,*  *,*  il timer MainClass_C1_timer_T6 sia attivo
    //   *104,* o  che  *,*  il contatore MainClass_C1_contatore_Co1 non sia  minore di  *55,* 15
    //   *104,* o  che   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* o  che  *36,*  il timer MainClass_C1_timer_T6 non sia attivo
    bool res_OrLogicOP_31 = false;
    bool res_OrLogicOP_32 = false;
    bool res_OrLogicOP_33 = false;
    res_OrLogicOP_33 = (res_OrLogicOP_33 || Timer_Attivo(L_P1__GetMainc42(my_id)));
    bool res_NotLogicOP_34 = true;
    res_NotLogicOP_34 = (res_NotLogicOP_34 && ! (Counter_GetValore(L_P1__GetMainc43(my_id)) < 15u));
    res_OrLogicOP_33 = (res_OrLogicOP_33 || res_NotLogicOP_34);
    
    res_OrLogicOP_32 = (res_OrLogicOP_32 || res_OrLogicOP_33);
    res_OrLogicOP_32 = (res_OrLogicOP_32 || (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_31 = (res_OrLogicOP_31 || res_OrLogicOP_32);
    bool res_NotLogicOP_35 = true;
    res_NotLogicOP_35 = (res_NotLogicOP_35 && ! Timer_Attivo(L_P1__GetMainc42(my_id)));
    res_OrLogicOP_31 = (res_OrLogicOP_31 || res_NotLogicOP_35);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_31);
    
    
    
    return res_AndLogicOP_0;
}


// Macro valorizzate

/*
    CNL corrispondente:
    
    { commento: {[} commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI4 è attivo   commento: {38,} o  se il contatore MainClass_C1_contatore_Co1 è  minore di  commento: {55,} 1245  , assegna alla macro il valore avanzamento
    
     commento: {46,} assegna alla macro il valore avanzamento commento: {],}
    }
*/
C1_Enumerat2 L_P1__Macro3(instance_id_t const my_id , bool argom2, C1_Enumerat4 argom3, C1_Enumerat1 argom4, C1_Enumerat2 argom5, C1_Enumerat2 argom6, C1_Enumerat1 argom7, C1_Enumerat3 argom8)
{
C1_Enumerat2 res_macro_val;
    
    //  *[* *110,*  se il ripristino del timer  MainClass_C1_restoreTI_TI4 è attivo   *38,* o  se il contatore MainClass_C1_contatore_Co1 è  minore di  *55,* 1245
    bool res_OrLogicOP_0 = false;
    res_OrLogicOP_0 = (res_OrLogicOP_0 || Timer_Attivo(L_P1__GetMainc41(my_id)));
    res_OrLogicOP_0 = (res_OrLogicOP_0 || (Counter_GetValore(L_P1__GetMainc43(my_id)) < 1245u));
    
    if(res_OrLogicOP_0){
    
    res_macro_val = avanzamento;
    }
    else{
    res_macro_val = avanzamento;
    }
    return res_macro_val;
}

/*
    CNL corrispondente:
    
    { commento: {[} commento: {36,}  se il timer MainClass_C1_timer_T6 è scaduto commento: {109,} o  se il ripristino della variabile  MainClass_C1_restoreva_RV2 non è  uguale a  True  commento: {35,} o  se il controllo MainClass_C1_controllo_C1 è  uguale a  False  e  se il controllo ConsDef è uguale a FALSE  commento: {110,} o  se il ripristino del timer  MainClass_C1_restoreTI_TI2 è scaduto e  se il controllo ConsDef è uguale a FALSE  , assegna alla macro il valore RossoVerde
    
     commento: {46,} assegna alla macro il valore RossoVerde commento: {],}
    }
*/
C1_Enumerat3 L_P1__Macro4(instance_id_t const my_id , C1_Enumerat2 argom9, C1_Enumerat2 argom10, C1_Enumerat1 argom11, C1_Enumerat2 argom12, C1_Enumerat2 argom13, C1_Enumerat2 argom14)
{
C1_Enumerat3 res_macro_val;
    
    //  *[* *36,*  se il timer MainClass_C1_timer_T6 è scaduto *109,* o  se il ripristino della variabile  MainClass_C1_restoreva_RV2 non è  uguale a  True  *35,* o  se il controllo MainClass_C1_controllo_C1 è  uguale a  False  e  se il controllo ConsDef è uguale a FALSE  *110,* o  se il ripristino del timer  MainClass_C1_restoreTI_TI2 è scaduto e  se il controllo ConsDef è uguale a FALSE
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_OrLogicOP_2 = false;
    res_OrLogicOP_2 = (res_OrLogicOP_2 || Timer_Scaduto(L_P1__GetMainc42(my_id)));
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__GetMainc29(my_id) == true));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_3);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_OrLogicOP_2);
    bool res_AndLogicOP_4 = true;
    res_AndLogicOP_4 = (res_AndLogicOP_4 && (L_P1__GetInMainc2(my_id) == false));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_4);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_AndLogicOP_5 = true;
    res_AndLogicOP_5 = (res_AndLogicOP_5 && Timer_Scaduto(L_P1__GetMainc37(my_id)));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_5);
    
    if(res_OrLogicOP_0){
    
    res_macro_val = rossoverde;
    }
    else{
    res_macro_val = rossoverde;
    }
    return res_macro_val;
}

/*
    CNL corrispondente:
    
    { commento: {[} commento: {34,}  se lo stato  è  uguale a  commento: {53,}  state1  commento: {106,} commento: {38,} e  se il contatore MainClass_C1_contatore_Co7 è  maggiore di  commento: {54,} 12213 , assegna alla macro il valore c270
    
     commento: {46,} assegna alla macro il valore c270 commento: {],}
    }
*/
C1_Enumerat1 L_P1__Macro5(instance_id_t const my_id , C1_Enumerat1 argom15, C1_Enumerat3 argom16, C1_Enumerat1 argom17, C1_Enumerat1 argom18, C1_Enumerat4 argom19)
{
C1_Enumerat1 res_macro_val;
    
    //  *[* *34,*  se lo stato  è  uguale a  *53,*  state1  *106,* *38,* e  se il contatore MainClass_C1_contatore_Co7 è  maggiore di  *54,* 12213
    bool res_AndLogicOP_0 = true;
    res_AndLogicOP_0 = (res_AndLogicOP_0 && (L_P1_C1_GetState(my_id) == C1_St_state));
    res_AndLogicOP_0 = (res_AndLogicOP_0 && (Counter_GetValore(L_P1__GetMainc44(my_id)) > 12213u));
    
    if(res_AndLogicOP_0){
    
    res_macro_val = c270;
    }
    else{
    res_macro_val = c270;
    }
    return res_macro_val;
}

/*
    CNL corrispondente:
    
    { commento: {[} commento: {35,}  se il controllo MainClass_C1_controllo_C1 non è  uguale a  True  , assegna alla macro il valore RossoVerde
    
     commento: {46,} assegna alla macro il valore RossoVerde commento: {],}
    }
*/
C1_Enumerat3 L_P1__Macro6(instance_id_t const my_id , C1_Enumerat4 argom20, C1_Enumerat1 argom21, C1_Enumerat2 argom22, C1_Enumerat3 argom23, C1_Enumerat3 argom24, C1_Enumerat4 argom25, C1_Enumerat1 argom26)
{
C1_Enumerat3 res_macro_val;
    
    //  il controllo MainClass_C1_controllo_C1 non è  uguale a  True
    bool res_NotLogicOP_0 = true;
    res_NotLogicOP_0 = (res_NotLogicOP_0 && ! (L_P1__GetInMainc2(my_id) == true));
    if(res_NotLogicOP_0){
    
    res_macro_val = rossoverde;
    }
    else{
    res_macro_val = rossoverde;
    }
    return res_macro_val;
}



