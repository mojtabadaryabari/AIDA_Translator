// Codice del modello 'TestCase24', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#include "Logica/ClasseMainClass_C1.h"
#include "Logica/ClasseSubClass_C2.h"
#include "Logica/ClasseMainClass_C1_priv.h"
#include "config.h"
#include "scheduler.h"


// ********** Gestione comandi automatici **********

static size_t L_P1_C1_NumAutoCmds(instance_id_t const my_id)
{
    size_t n = 0u;
    if (L_P1__GetCAEvent3(my_id)) {
        ++n;
    }
    return n;
}


// ********** Gestione comandi manuali **********

static void L_P1_C1_InitCmdsResponse(instance_id_t const my_id)
{
    // for each manual command of L_P1_C1
    if (L_P1__GetInEvent(my_id)) {
	    L_P1__SetOutEvent4(my_id, LDS_MANCMD_UNEXPECTED);
    } else {
        L_P1__SetOutEvent4(my_id, LDS_MANCMD_NOOP);
    }
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
    L_P1__SetMainc19(my_id, avanzamento1);
    L_P1__SetMainc21(my_id, 0);
    L_P1__SetMainc23(my_id, gialloverde);
    L_P1__SetMainc25(my_id, verde);
    L_P1__SetMainc27(my_id, 0);
    L_P1__SetMainc28(my_id, 0);
    L_P1__SetMainc29(my_id, false);
    L_P1__SetMainc30(my_id, false);
    L_P1__SetMainc31(my_id, false);
    L_P1__SetMainc32(my_id, false);
    L_P1__SetMainc33(my_id, false);
    L_P1__SetMainc34(my_id, false);
    L_P1__SetMainc35(my_id, false);
    L_P1__SetMainc36(my_id, false);
    L_P1__SetMainc37(my_id, 0);
    L_P1__SetMainc38(my_id, false);
    L_P1__SetMainc39(my_id, false);
    L_P1__SetMainc40(my_id, 0);
    L_P1__SetStato1(my_id, C1_St_Stato);
    // init controlli precedenti
    L_P1__SetMainc14(my_id, rossogiallo1);
    L_P1__SetMainc16(my_id, false);
    L_P1__SetMainc18(my_id, false);
    // init Timer e Counter
    Timer_AggmInit(L_P1__GetMainc41(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc41_ID);
    Timer_Init(L_P1__GetMainc41(my_id), 24000);
    Timer_AggmInit(L_P1__GetMainc42(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc42_ID);
    Timer_Init(L_P1__GetMainc42(my_id), 24000);
    Timer_AggmInit(L_P1__GetMainc43(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc43_ID);
    Timer_Init(L_P1__GetMainc43(my_id), 32000);
    Timer_AggmInit(L_P1__GetMainc44(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc44_ID);
    Timer_Init(L_P1__GetMainc44(my_id), 32000);
    Timer_AggmInit(L_P1__GetMainc45(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc45_ID);
    Timer_Init(L_P1__GetMainc45(my_id), 2130000);
    Timer_AggmInit(L_P1__GetMainc46(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc46_ID);
    Timer_Init(L_P1__GetMainc46(my_id), 2130000);
    Timer_AggmInit(L_P1__GetMainc47(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc47_ID);
    Timer_Init(L_P1__GetMainc47(my_id), 305000);
    Counter_AggmInit(L_P1__GetMainc48(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc48_ID);
    Counter_Init(L_P1__GetMainc48(my_id));
    Counter_AggmInit(L_P1__GetMainc49(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc49_ID);
    Counter_Init(L_P1__GetMainc49(my_id));
    Counter_AggmInit(L_P1__GetMainc50(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc50_ID);
    Counter_Init(L_P1__GetMainc50(my_id));
    Counter_AggmInit(L_P1__GetMainc51(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc51_ID);
    Counter_Init(L_P1__GetMainc51(my_id));
    Counter_AggmInit(L_P1__GetMainc52(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc52_ID);
    Counter_Init(L_P1__GetMainc52(my_id));
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
    L_P1__SetMainc26(my_id, L_P1__GetMainc25(my_id));
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
    Timer_Exec(L_P1__GetMainc41(my_id));
    Timer_Exec(L_P1__GetMainc42(my_id));
    Timer_Exec(L_P1__GetMainc43(my_id));
    Timer_Exec(L_P1__GetMainc44(my_id));
    Timer_Exec(L_P1__GetMainc45(my_id));
    Timer_Exec(L_P1__GetMainc46(my_id));
    Timer_Exec(L_P1__GetMainc47(my_id));
}

void L_P1_C1_GSetSafe(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C1(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C1(proc_id);
    L_P1__SetOutMainc(my_id, rossogiallo1);
    L_P1__SetOutMainc1(my_id, true);
    L_P1__SetOutMainc2(my_id, rossogiallo1);
    L_P1__SetOutMainc3(my_id, ac);
}

void L_P1_C1_GUpdatePrev(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C1(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C1(proc_id);
    L_P1__SetMainc14(my_id, L_P1__GetInMainc13(my_id));
    L_P1__SetMainc16(my_id, L_P1__GetInMainc15(my_id));
    L_P1__SetMainc18(my_id, L_P1__GetInMainc17(my_id));
    L_P1__SetMainc20(my_id, L_P1__GetMainc19(my_id));
    L_P1__SetMainc22(my_id, L_P1__GetMainc21(my_id));
    L_P1__SetMainc24(my_id, L_P1__GetMainc23(my_id));
    L_P1__SetMainc26(my_id, L_P1__GetMainc25(my_id));
}

// ********** Definizione macro **********

// Macro di effetto

/*
    CNL corrispondente:
    
    { commento: {38,}  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  commento: {53,} 12 commento: {38,} o  se il contatore MainClass_C1_contatore_Co9 non è  uguale a  commento: {53,} 120 commento: {38,} o  se il contatore MainClass_C1_contatore_Co6 non è  maggiore di  commento: {54,} 11 commento: {35,} o  se il controllo MainClass_C1_controllo_C3 non è  uguale a  False , commento: {69,}Disattiva il timer MainClass_C1_timer_T10
    
       
     commento: {34,}  se lo stato  è  uguale a  commento: {53,}  state1  commento: {106,}, commento: {71,}Decrementa il contatore MainClass_C1_contatore_Co7
    
     ,altrimenti  commento: {72,}Azzera il contatore MainClass_C1_contatore_Co7
    
    
     commento: {37,}  se la variabile MainClass_C1_variabile_V3 non è  uguale a  False  commento: {37,} e  se la variabile MainClass_C1_variabile_V3 è  uguale a  True  commento: {37,} o  se la variabile MainClass_C1_variabile_V4 non è  diverso da  True  commento: {37,} e  se la variabile MainClass_C1_variabile_V4 è  diverso da  False ,  Applica gli effetti
           della macro MainClass_C1_macroef_M3( con argomento_af9   uguale a GialloVerde ,argomento_af1   uguale a True ,argomento_af6   uguale a Verde ,argomento_af5   uguale a AC ,argomento_af7   uguale a GialloVerde ,argomento_af3   uguale a avanzamentox ) commento: {73,}
    
     ,altrimenti   Applica gli effetti
           della macro MainClass_C1_macroef_M4  commento: {73,}
    
    
    
    }
*/
void L_P1__Macro(instance_id_t const my_id )
{
//  *38,*  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  *53,* 12 *38,* o  se il contatore MainClass_C1_contatore_Co9 non è  uguale a  *53,* 120 *38,* o  se il contatore MainClass_C1_contatore_Co6 non è  maggiore di  *54,* 11 *35,* o  se il controllo MainClass_C1_controllo_C3 non è  uguale a  False , *69,*Disattiva il timer MainClass_C1_timer_T10
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_OrLogicOP_2 = false;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (Counter_GetValore(L_P1__GetMainc51(my_id)) == 12u));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_3);
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (Counter_GetValore(L_P1__GetMainc52(my_id)) == 120u));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_4);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_OrLogicOP_2);
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (Counter_GetValore(L_P1__GetMainc50(my_id)) > 11u));
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_NotLogicOP_5);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetInMainc4(my_id) == false));
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_6);
    
    if(res_OrLogicOP_0){
    
    Timer_Disattiva(L_P1__GetMainc47(my_id));
    }
    //  *34,*  se lo stato  è  uguale a  *53,*  state1  *106,*, *71,*Decrementa il contatore MainClass_C1_contatore_Co7
    // ,altrimenti  *72,*Azzera il contatore MainClass_C1_contatore_Co7
    if((L_P1_C1_GetState(my_id) == C1_St_state)){
    
    Counter_Decr(L_P1__GetMainc51(my_id));
    }else{
    
    Counter_Res(L_P1__GetMainc51(my_id));
    }
    //  *37,*  se la variabile MainClass_C1_variabile_V3 non è  uguale a  False  *37,* e  se la variabile MainClass_C1_variabile_V3 è  uguale a  True  *37,* o  se la variabile MainClass_C1_variabile_V4 non è  diverso da  True  *37,* e  se la variabile MainClass_C1_variabile_V4 è  diverso da  False ,  Applica gli effetti
    //       della macro MainClass_C1_macroef_M3( con argomento_af9   uguale a GialloVerde ,argomento_af1   uguale a True ,argomento_af6   uguale a Verde ,argomento_af5   uguale a AC ,argomento_af7   uguale a GialloVerde ,argomento_af3   uguale a avanzamentox ) *73,*
    // ,altrimenti   Applica gli effetti
    //       della macro MainClass_C1_macroef_M4
    bool res_OrLogicOP_7 = false;
    bool res_AndLogicOP_8 = true;
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetMainc38(my_id) == false));
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_9);
    res_AndLogicOP_8 = (res_AndLogicOP_8 && (L_P1__GetMainc38(my_id) == true));
    
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_AndLogicOP_8);
    bool res_AndLogicOP_10 = true;
    bool res_NotLogicOP_11 = true;
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (L_P1__GetMainc39(my_id) == true));
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! res_NotLogicOP_12);
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_NotLogicOP_11);
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (L_P1__GetMainc39(my_id) == false));
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_NotLogicOP_13);
    
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_AndLogicOP_10);
    
    if(res_OrLogicOP_7){
    
    L_P1__Macro1(my_id,true,avanzamento1,ac,verde,gialloverde,gialloverde);
    }else{
    
    L_P1__Macro2(my_id);
    }
}

/*
    CNL corrispondente:
    
    { commento: {38,}  se il contatore MainClass_C1_contatore_Co7 è  minore di  commento: {55,} 141 e  se l'argomento argomento_af1 è  diverso da  False  commento: {39,} , commento: {66,} Assegna al comando MainClass_C1_comando_C2 il valore  True 
    
     ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V2 il valore 5
    
    
     commento: {34,}  se il parametro MainClass_C1_parametro_P10 è  uguale a  commento: {53,} 2 commento: {34,} o  se il parametro MainClass_C1_parametro_P8 è  uguale a RossoGialloVerde, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V2 il valore 2
    
       
    
    }
*/
void L_P1__Macro1(instance_id_t const my_id , bool argom4, C1_Enumerat4 argom5, C1_Enumerat2 argom6, C1_Enumerat3 argom7, C1_Enumerat2 argom8, C1_Enumerat2 argom9)
{
//  *38,*  se il contatore MainClass_C1_contatore_Co7 è  minore di  *55,* 141 e  se l'argomento argomento_af1 è  diverso da  False  *39,* , *66,* Assegna al comando MainClass_C1_comando_C2 il valore  True 
    // ,altrimenti  *67,* Assegna alla variabile MainClass_C1_variabile_V2 il valore 5
    bool res_AndLogicOP_0 = true;
    res_AndLogicOP_0 = (res_AndLogicOP_0 && (Counter_GetValore(L_P1__GetMainc51(my_id)) < 141u));
    bool res_NotLogicOP_1 = true;
    res_NotLogicOP_1 = (res_NotLogicOP_1 && ! (argom4 == false));
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_NotLogicOP_1);
    
    if(res_AndLogicOP_0){
    
    L_P1__SetOutMainc1(my_id,true);
    }else{
    
    L_P1__SetMainc37(my_id,5u);
    }
    //  *34,*  se il parametro MainClass_C1_parametro_P10 è  uguale a  *53,* 2 *34,* o  se il parametro MainClass_C1_parametro_P8 è  uguale a RossoGialloVerde, *67,* Assegna alla variabile MainClass_C1_variabile_V2 il valore 2
    bool res_OrLogicOP_2 = false;
    res_OrLogicOP_2 = (res_OrLogicOP_2 || (L_P1__GetParamMainc9(my_id) == 2u));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || (L_P1__GetParamMainc12(my_id) == rossogiallo1));
    
    if(res_OrLogicOP_2){
    
    L_P1__SetMainc37(my_id,2u);
    }
}

/*
    CNL corrispondente:
    
    { commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  minore di  commento: {55,} 5 commento: {35,} e  se il controllo MainClass_C1_controllo_C7 è  diverso da c120x commento: {36,} o  se il timer MainClass_C1_timer_T10 non è disattivo, commento: {68,}Attiva il timer MainClass_C1_timer_T10
    
     ,altrimenti  commento: {69,}Disattiva il timer MainClass_C1_timer_T10
    
    
     commento: {34,}  se il parametro MainClass_C1_parametro_P8 non è  diverso da RossoGialloVerde e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE , commento: {67,} Assegna alla variabile MainClass_C1_variabile_V3 il valore  False 
    
       
    
    }
*/
void L_P1__Macro2(instance_id_t const my_id )
{
//  *109,*  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  minore di  *55,* 5 *35,* e  se il controllo MainClass_C1_controllo_C7 è  diverso da c120x *36,* o  se il timer MainClass_C1_timer_T10 non è disattivo, *68,*Attiva il timer MainClass_C1_timer_T10
    // ,altrimenti  *69,*Disattiva il timer MainClass_C1_timer_T10
    bool res_OrLogicOP_0 = false;
    bool res_AndLogicOP_1 = true;
    res_AndLogicOP_1 = (res_AndLogicOP_1 && (L_P1__GetMainc28(my_id) < 5u));
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (L_P1__GetInMainc6(my_id) == c120x));
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_2);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_1);
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! Timer_Disattivo(L_P1__GetMainc47(my_id)));
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_3);
    
    if(res_OrLogicOP_0){
    
    Timer_Attiva(L_P1__GetMainc47(my_id));
    }else{
    
    Timer_Disattiva(L_P1__GetMainc47(my_id));
    }
    //  *34,*  se il parametro MainClass_C1_parametro_P8 non è  diverso da RossoGialloVerde e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE , *67,* Assegna alla variabile MainClass_C1_variabile_V3 il valore  False
    bool res_AndLogicOP_4 = true;
    bool res_AndLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetParamMainc12(my_id) == rossogiallo1));
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! res_NotLogicOP_7);
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_6);
    res_AndLogicOP_5 = (res_AndLogicOP_5 && (L_P1__GetInConsd(my_id) == false));
    
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_AndLogicOP_5);
    res_AndLogicOP_4 = (res_AndLogicOP_4 && (L_P1__GetInConsd(my_id) == false));
    
    if(res_AndLogicOP_4){
    
    L_P1__SetMainc38(my_id,false);
    }
}

/*
    CNL corrispondente:
     
    {  se il ripristino dello stato  è  uguale a  commento: {53,}  state1  commento: {107,} commento: {34,} o  se il parametro MainClass_C1_parametro_P10 è  diverso da  commento: {56,} 10, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V8 il valore 4
    
     ,altrimenti  commento: {68,}Attiva il timer MainClass_C1_timer_T10
    
    
     commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI2 è disattivo o  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} o  se il contatore MainClass_C1_contatore_Co7 è  diverso da  commento: {56,} 133 commento: {37,} e  se la variabile MainClass_C1_variabile_V3 è  uguale a  True  commento: {37,} o  se la variabile MainClass_C1_variabile_V3 non è  diverso da  True  commento: {38,} o  se il contatore MainClass_C1_contatore_Co6 non è  minore di  commento: {55,} 12, commento: {68,}Attiva il timer MainClass_C1_timer_T10
    
     ,altrimenti  commento: {68,}Attiva il timer MainClass_C1_timer_T10
    
    
     commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI3 non è scaduto commento: {38,} o  se il contatore MainClass_C1_contatore_Co5 è  minore di  commento: {55,} 15 commento: {35,} e  se il controllo MainClass_C1_controllo_C6 non è  diverso da  True  commento: {37,} e  se la variabile MainClass_C1_variabile_V3 è  diverso da  False  commento: {37,} e  se la variabile MainClass_C1_variabile_V2 è  minore di  commento: {55,} 1,  Applica gli effetti
           della macro MainClass_C1_macroef_M3( con argomento_af9   uguale a AC ,argomento_af1   uguale a True ,argomento_af6   uguale a avanzamento ,argomento_af5   uguale a GialloVerde ,argomento_af7   uguale a GialloVerde ,argomento_af3   uguale a avanzamentox ) commento: {73,}
    
       
    
    }
*/
void L_P1__Macro3(instance_id_t const my_id )
{
//  se il ripristino dello stato  è  uguale a  *53,*  state1  *107,* *34,* o  se il parametro MainClass_C1_parametro_P10 è  diverso da  *56,* 10, *67,* Assegna alla variabile MainClass_C1_variabile_V8 il valore 4
    // ,altrimenti  *68,*Attiva il timer MainClass_C1_timer_T10
    bool res_OrLogicOP_0 = false;
    res_OrLogicOP_0 = (res_OrLogicOP_0 || (L_P1__GetStato1(my_id) == C1_St_state));
    bool res_NotLogicOP_1 = true;
    res_NotLogicOP_1 = (res_NotLogicOP_1 && ! (L_P1__GetParamMainc9(my_id) == 10u));
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_1);
    
    if(res_OrLogicOP_0){
    
    L_P1__SetMainc40(my_id,4u);
    }else{
    
    Timer_Attiva(L_P1__GetMainc47(my_id));
    }
    //  *110,*  se il ripristino del timer  MainClass_C1_restoreTI_TI2 è disattivo o  se il controllo ConsDef  è  uguale a FALSE  *38,* o  se il contatore MainClass_C1_contatore_Co7 è  diverso da  *56,* 133 *37,* e  se la variabile MainClass_C1_variabile_V3 è  uguale a  True  *37,* o  se la variabile MainClass_C1_variabile_V3 non è  diverso da  True  *38,* o  se il contatore MainClass_C1_contatore_Co6 non è  minore di  *55,* 12, *68,*Attiva il timer MainClass_C1_timer_T10
    // ,altrimenti  *68,*Attiva il timer MainClass_C1_timer_T10
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_OrLogicOP_4 = false;
    bool res_OrLogicOP_5 = false;
    res_OrLogicOP_5 = (res_OrLogicOP_5 || Timer_Disattivo(L_P1__GetMainc44(my_id)));
    res_OrLogicOP_5 = (res_OrLogicOP_5 || (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_OrLogicOP_5);
    bool res_AndLogicOP_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (Counter_GetValore(L_P1__GetMainc51(my_id)) == 133u));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_7);
    res_AndLogicOP_6 = (res_AndLogicOP_6 && (L_P1__GetMainc38(my_id) == true));
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_AndLogicOP_6);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_OrLogicOP_4);
    bool res_NotLogicOP_8 = true;
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetMainc38(my_id) == true));
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! res_NotLogicOP_9);
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_NotLogicOP_8);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (Counter_GetValore(L_P1__GetMainc50(my_id)) < 12u));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_10);
    
    if(res_OrLogicOP_2){
    
    Timer_Attiva(L_P1__GetMainc47(my_id));
    }else{
    
    Timer_Attiva(L_P1__GetMainc47(my_id));
    }
    //  *110,*  se il ripristino del timer  MainClass_C1_restoreTI_TI3 non è scaduto *38,* o  se il contatore MainClass_C1_contatore_Co5 è  minore di  *55,* 15 *35,* e  se il controllo MainClass_C1_controllo_C6 non è  diverso da  True  *37,* e  se la variabile MainClass_C1_variabile_V3 è  diverso da  False  *37,* e  se la variabile MainClass_C1_variabile_V2 è  minore di  *55,* 1,  Applica gli effetti
    //       della macro MainClass_C1_macroef_M3( con argomento_af9   uguale a AC ,argomento_af1   uguale a True ,argomento_af6   uguale a avanzamento ,argomento_af5   uguale a GialloVerde ,argomento_af7   uguale a GialloVerde ,argomento_af3   uguale a avanzamentox )
    bool res_OrLogicOP_11 = false;
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! Timer_Scaduto(L_P1__GetMainc46(my_id)));
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_NotLogicOP_12);
    bool res_AndLogicOP_13 = true;
    bool res_AndLogicOP_14 = true;
    bool res_AndLogicOP_15 = true;
    res_AndLogicOP_15 = (res_AndLogicOP_15 && (Counter_GetValore(L_P1__GetMainc49(my_id)) < 15u));
    bool res_NotLogicOP_16 = true;
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! (L_P1__GetInMainc5(my_id) == true));
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! res_NotLogicOP_17);
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_NotLogicOP_16);
    
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_AndLogicOP_15);
    bool res_NotLogicOP_18 = true;
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! (L_P1__GetMainc38(my_id) == false));
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_NotLogicOP_18);
    
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_AndLogicOP_14);
    res_AndLogicOP_13 = (res_AndLogicOP_13 && (L_P1__GetMainc37(my_id) < 1u));
    
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_AndLogicOP_13);
    
    if(res_OrLogicOP_11){
    
    L_P1__Macro1(my_id,true,avanzamento1,gialloverde,avanzamento,gialloverde,ac);
    }
}


// Macro di verifica

/*
    CNL corrispondente:
     
    { commento: {61,}  se il ripristino dello stato  è  uguale a  commento: {53,}  state1  commento: {107,}, Tutte le seguenti { 
     commento: {61,} commento: {34,}  se lo stato  è  diverso da  commento: {56,}  state1  commento: {106,} commento: {34,} o  se il parametro MainClass_C1_parametro_P10 non è  maggiore di  commento: {54,} 10 commento: {36,} o  se il timer MainClass_C1_timer_T10 non è disattivo commento: {37,} o  se la variabile MainClass_C1_variabile_V3 non è  diverso da  False , Tutte le seguenti { 
     commento: {62,} commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV2 è  diverso da  False , Almeno una delle seguenti { 
     commento: {38,}  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  commento: {53,} 13054 commento: {34,} e  se il parametro MainClass_C1_parametro_P10 non è  maggiore di  commento: {54,} 4 commento: {38,} e  se il contatore MainClass_C1_contatore_Co3 non è  diverso da  commento: {56,} 132 commento: {38,} e  se il contatore MainClass_C1_contatore_Co9 è  uguale a  commento: {53,} 1313, Verifica che   commento: {47,48,50,}  commento: {34,}  il parametro MainClass_C1_parametro_P10 non sia  maggiore di  commento: {54,} 3
     commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C7 non sia  diverso da c120x
     commento: {104,} e  che  commento: {35,}  il controllo MainClass_C1_controllo_C9 non sia  diverso da  False 
     commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V8 non sia  diverso da  commento: {56,} 2
    
    
     } Verifica che   commento: {47,48,51,}  commento: {,}  il contatore MainClass_C1_contatore_Co7 non sia  maggiore di  commento: {54,} 13054
     commento: {104,} e  che  commento: {38,}  il contatore MainClass_C1_contatore_Co7 non sia  minore di  commento: {55,} 11
     commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P10 sia  minore di  commento: {55,} 10
     commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C7 non sia  diverso da c120x
     commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
    
    
     } Verifica che   commento: {47,48,50,}  commento: {,}  il controllo MainClass_C1_controllo_C6 sia  diverso da  False 
     commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P10 sia  maggiore di  commento: {54,} 7
     commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V2 non sia  minore di  commento: {55,} 10
     commento: {104,} e  che  commento: {37,}  la variabile MainClass_C1_variabile_V3 non sia  diverso da  True 
     commento: {104,} o  che  commento: {37,}  la variabile MainClass_C1_variabile_V2 sia  diverso da  commento: {56,} 2
     commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P10 non sia  minore di  commento: {55,} 3
    
    
     } Verifica che   commento: {49,51,}  commento: {,}  il contatore MainClass_C1_contatore_Co5 sia  maggiore di  commento: {54,} 113
     commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T10 non sia attivo
    
    
    }
*/
bool L_P1__Macro9(instance_id_t const my_id )
{
bool res_AndLogicOP_0 = true;
    
    //  *61,*  se il ripristino dello stato  è  uguale a  *53,*  state1  *107,*, Tutte le seguenti { 
    //   *61,* *34,*  se lo stato  è  diverso da  *56,*  state1  *106,* *34,* o  se il parametro MainClass_C1_parametro_P10 non è  maggiore di  *54,* 10 *36,* o  se il timer MainClass_C1_timer_T10 non è disattivo *37,* o  se la variabile MainClass_C1_variabile_V3 non è  diverso da  False , Tutte le seguenti { 
    //   *62,* *109,*  se il ripristino della variabile  MainClass_C1_restoreva_RV2 è  diverso da  False , Almeno una delle seguenti { 
    //   *38,*  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  *53,* 13054 *34,* e  se il parametro MainClass_C1_parametro_P10 non è  maggiore di  *54,* 4 *38,* e  se il contatore MainClass_C1_contatore_Co3 non è  diverso da  *56,* 132 *38,* e  se il contatore MainClass_C1_contatore_Co9 è  uguale a  *53,* 1313, Verifica che   *47,48,50,*  *34,*  il parametro MainClass_C1_parametro_P10 non sia  maggiore di  *54,* 3
    //   *104,* o  che  *,*  il controllo MainClass_C1_controllo_C7 non sia  diverso da c120x
    //   *104,* e  che  *35,*  il controllo MainClass_C1_controllo_C9 non sia  diverso da  False 
    //   *104,* e  che  *,*  la variabile MainClass_C1_variabile_V8 non sia  diverso da  *56,* 2
    //   } Verifica che   *47,48,51,*  *,*  il contatore MainClass_C1_contatore_Co7 non sia  maggiore di  *54,* 13054
    //   *104,* e  che  *38,*  il contatore MainClass_C1_contatore_Co7 non sia  minore di  *55,* 11
    //   *104,* e  che  *34,*  il parametro MainClass_C1_parametro_P10 sia  minore di  *55,* 10
    //   *104,* e  che  *,*  il controllo MainClass_C1_controllo_C7 non sia  diverso da c120x
    //   *104,* e  che   il controllo ConsDef  sia  uguale a FALSE 
    //   } Verifica che   *47,48,50,*  *,*  il controllo MainClass_C1_controllo_C6 sia  diverso da  False 
    //   *104,* e  che  *34,*  il parametro MainClass_C1_parametro_P10 sia  maggiore di  *54,* 7
    //   *104,* o  che  *,*  la variabile MainClass_C1_variabile_V2 non sia  minore di  *55,* 10
    //   *104,* e  che  *37,*  la variabile MainClass_C1_variabile_V3 non sia  diverso da  True 
    //   *104,* o  che  *37,*  la variabile MainClass_C1_variabile_V2 sia  diverso da  *56,* 2
    //   *104,* o  che  *34,*  il parametro MainClass_C1_parametro_P10 non sia  minore di  *55,* 3
    //   }
    bool res_ImpliesLogicOp_1 = true;
    if((L_P1__GetStato1(my_id) == C1_St_state)){
    bool res_AndLogicOP_2 = true;
    bool res_ImpliesLogicOp_3 = true;
    bool res_OrLogicOP_4 = false;
    bool res_OrLogicOP_5 = false;
    bool res_OrLogicOP_6 = false;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1_C1_GetState(my_id) == C1_St_state));
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_NotLogicOP_7);
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetParamMainc9(my_id) > 10u));
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_NotLogicOP_8);
    
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_OrLogicOP_6);
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! Timer_Disattivo(L_P1__GetMainc47(my_id)));
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_NotLogicOP_9);
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_OrLogicOP_5);
    bool res_NotLogicOP_10 = true;
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (L_P1__GetMainc38(my_id) == false));
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! res_NotLogicOP_11);
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_NotLogicOP_10);
    
    if(res_OrLogicOP_4){
    bool res_AndLogicOP_12 = true;
    bool res_ImpliesLogicOp_13 = true;
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1__GetMainc30(my_id) == false));
    if(res_NotLogicOP_14){
    bool res_ImpliesLogicOp_15 = true;
    bool res_AndLogicOP_16 = true;
    bool res_AndLogicOP_17 = true;
    bool res_AndLogicOP_18 = true;
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (Counter_GetValore(L_P1__GetMainc51(my_id)) == 13054u));
    res_AndLogicOP_18 = (res_AndLogicOP_18 && res_NotLogicOP_19);
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! (L_P1__GetParamMainc9(my_id) > 4u));
    res_AndLogicOP_18 = (res_AndLogicOP_18 && res_NotLogicOP_20);
    
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_AndLogicOP_18);
    bool res_NotLogicOP_21 = true;
    bool res_NotLogicOP_22 = true;
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! (Counter_GetValore(L_P1__GetMainc48(my_id)) == 132u));
    res_NotLogicOP_21 = (res_NotLogicOP_21 && ! res_NotLogicOP_22);
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_NotLogicOP_21);
    
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_AndLogicOP_17);
    res_AndLogicOP_16 = (res_AndLogicOP_16 && (Counter_GetValore(L_P1__GetMainc52(my_id)) == 1313u));
    
    if(res_AndLogicOP_16){
    bool res_OrLogicOP_23 = false;
    bool res_NotLogicOP_24 = true;
    res_NotLogicOP_24 = (res_NotLogicOP_24 && ! (L_P1__GetParamMainc9(my_id) > 3u));
    res_OrLogicOP_23 = (res_OrLogicOP_23 || res_NotLogicOP_24);
    bool res_AndLogicOP_25 = true;
    bool res_AndLogicOP_26 = true;
    bool res_NotLogicOP_27 = true;
    bool res_NotLogicOP_28 = true;
    res_NotLogicOP_28 = (res_NotLogicOP_28 && ! (L_P1__GetInMainc6(my_id) == c120x));
    res_NotLogicOP_27 = (res_NotLogicOP_27 && ! res_NotLogicOP_28);
    res_AndLogicOP_26 = (res_AndLogicOP_26 && res_NotLogicOP_27);
    bool res_NotLogicOP_29 = true;
    bool res_NotLogicOP_30 = true;
    res_NotLogicOP_30 = (res_NotLogicOP_30 && ! (L_P1__GetInMainc7(my_id) == false));
    res_NotLogicOP_29 = (res_NotLogicOP_29 && ! res_NotLogicOP_30);
    res_AndLogicOP_26 = (res_AndLogicOP_26 && res_NotLogicOP_29);
    
    res_AndLogicOP_25 = (res_AndLogicOP_25 && res_AndLogicOP_26);
    bool res_NotLogicOP_31 = true;
    bool res_NotLogicOP_32 = true;
    res_NotLogicOP_32 = (res_NotLogicOP_32 && ! (L_P1__GetMainc40(my_id) == 2u));
    res_NotLogicOP_31 = (res_NotLogicOP_31 && ! res_NotLogicOP_32);
    res_AndLogicOP_25 = (res_AndLogicOP_25 && res_NotLogicOP_31);
    
    res_OrLogicOP_23 = (res_OrLogicOP_23 || res_AndLogicOP_25);
    
    res_ImpliesLogicOp_15 = (res_ImpliesLogicOp_15 && res_OrLogicOP_23);
    }
    res_ImpliesLogicOp_13 = (res_ImpliesLogicOp_13 && res_ImpliesLogicOp_15);
    }
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_ImpliesLogicOp_13);
    bool res_AndLogicOP_33 = true;
    bool res_AndLogicOP_34 = true;
    bool res_AndLogicOP_35 = true;
    bool res_AndLogicOP_36 = true;
    bool res_NotLogicOP_37 = true;
    res_NotLogicOP_37 = (res_NotLogicOP_37 && ! (Counter_GetValore(L_P1__GetMainc51(my_id)) > 13054u));
    res_AndLogicOP_36 = (res_AndLogicOP_36 && res_NotLogicOP_37);
    bool res_NotLogicOP_38 = true;
    res_NotLogicOP_38 = (res_NotLogicOP_38 && ! (Counter_GetValore(L_P1__GetMainc51(my_id)) < 11u));
    res_AndLogicOP_36 = (res_AndLogicOP_36 && res_NotLogicOP_38);
    
    res_AndLogicOP_35 = (res_AndLogicOP_35 && res_AndLogicOP_36);
    res_AndLogicOP_35 = (res_AndLogicOP_35 && (L_P1__GetParamMainc9(my_id) < 10u));
    
    res_AndLogicOP_34 = (res_AndLogicOP_34 && res_AndLogicOP_35);
    bool res_NotLogicOP_39 = true;
    bool res_NotLogicOP_40 = true;
    res_NotLogicOP_40 = (res_NotLogicOP_40 && ! (L_P1__GetInMainc6(my_id) == c120x));
    res_NotLogicOP_39 = (res_NotLogicOP_39 && ! res_NotLogicOP_40);
    res_AndLogicOP_34 = (res_AndLogicOP_34 && res_NotLogicOP_39);
    
    res_AndLogicOP_33 = (res_AndLogicOP_33 && res_AndLogicOP_34);
    res_AndLogicOP_33 = (res_AndLogicOP_33 && (L_P1__GetInConsd(my_id) == false));
    
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_AndLogicOP_33);
    
    res_ImpliesLogicOp_3 = (res_ImpliesLogicOp_3 && res_AndLogicOP_12);
    }
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_ImpliesLogicOp_3);
    bool res_OrLogicOP_41 = false;
    bool res_OrLogicOP_42 = false;
    bool res_OrLogicOP_43 = false;
    bool res_AndLogicOP_44 = true;
    bool res_NotLogicOP_45 = true;
    res_NotLogicOP_45 = (res_NotLogicOP_45 && ! (L_P1__GetInMainc5(my_id) == false));
    res_AndLogicOP_44 = (res_AndLogicOP_44 && res_NotLogicOP_45);
    res_AndLogicOP_44 = (res_AndLogicOP_44 && (L_P1__GetParamMainc9(my_id) > 7u));
    
    res_OrLogicOP_43 = (res_OrLogicOP_43 || res_AndLogicOP_44);
    bool res_AndLogicOP_46 = true;
    bool res_NotLogicOP_47 = true;
    res_NotLogicOP_47 = (res_NotLogicOP_47 && ! (L_P1__GetMainc37(my_id) < 10u));
    res_AndLogicOP_46 = (res_AndLogicOP_46 && res_NotLogicOP_47);
    bool res_NotLogicOP_48 = true;
    bool res_NotLogicOP_49 = true;
    res_NotLogicOP_49 = (res_NotLogicOP_49 && ! (L_P1__GetMainc38(my_id) == true));
    res_NotLogicOP_48 = (res_NotLogicOP_48 && ! res_NotLogicOP_49);
    res_AndLogicOP_46 = (res_AndLogicOP_46 && res_NotLogicOP_48);
    
    res_OrLogicOP_43 = (res_OrLogicOP_43 || res_AndLogicOP_46);
    
    res_OrLogicOP_42 = (res_OrLogicOP_42 || res_OrLogicOP_43);
    bool res_NotLogicOP_50 = true;
    res_NotLogicOP_50 = (res_NotLogicOP_50 && ! (L_P1__GetMainc37(my_id) == 2u));
    res_OrLogicOP_42 = (res_OrLogicOP_42 || res_NotLogicOP_50);
    
    res_OrLogicOP_41 = (res_OrLogicOP_41 || res_OrLogicOP_42);
    bool res_NotLogicOP_51 = true;
    res_NotLogicOP_51 = (res_NotLogicOP_51 && ! (L_P1__GetParamMainc9(my_id) < 3u));
    res_OrLogicOP_41 = (res_OrLogicOP_41 || res_NotLogicOP_51);
    
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_OrLogicOP_41);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_AndLogicOP_2);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *49,51,*  *,*  il contatore MainClass_C1_contatore_Co5 sia  maggiore di  *54,* 113
    //   *104,* e  che  *,*  il timer MainClass_C1_timer_T10 non sia attivo
    bool res_AndLogicOP_52 = true;
    res_AndLogicOP_52 = (res_AndLogicOP_52 && (Counter_GetValore(L_P1__GetMainc49(my_id)) > 113u));
    bool res_NotLogicOP_53 = true;
    res_NotLogicOP_53 = (res_NotLogicOP_53 && ! Timer_Attivo(L_P1__GetMainc47(my_id)));
    res_AndLogicOP_52 = (res_AndLogicOP_52 && res_NotLogicOP_53);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_AndLogicOP_52);
    
    
    
    return res_AndLogicOP_0;
}


// Macro valorizzate

/*
    CNL corrispondente:
     
    { commento: {[}  se la macro  MainClass_C1_macrova_M7 ( con argomento_a6   uguale a RossoGialloxVerdex ,argomento_a5   uguale a avanzamento ,argomento_a7   uguale a Verde ,argomento_a3   uguale a RossoGialloxVerdex ,argomento_a10   uguale a RossoGialloVerde  e argomento_a2   uguale a RossoGialloxVerdex )  non  è  uguale a  True  commento: {40,}  , assegna alla macro il valore RossoGialloVerde
    
     commento: {46,} assegna alla macro il valore RossoGialloVerde commento: {],}
    }
*/
C1_Enumerat4 L_P1__Macro4(instance_id_t const my_id )
{
C1_Enumerat4 res_macro_val;
    
    //  la macro  MainClass_C1_macrova_M7 ( con argomento_a6   uguale a RossoGialloxVerdex ,argomento_a5   uguale a avanzamento ,argomento_a7   uguale a Verde ,argomento_a3   uguale a RossoGialloxVerdex ,argomento_a10   uguale a RossoGialloVerde  e argomento_a2   uguale a RossoGialloxVerdex )  non  è  uguale a  True
    bool res_NotLogicOP_0 = true;
    res_NotLogicOP_0 = (res_NotLogicOP_0 && ! (L_P1__Macro8(my_id,rossogiallo1,rossogiallo,rossogiallo,avanzamento,rossogiallo,verde) == true));
    if(res_NotLogicOP_0){
    
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
bool L_P1__Macro5(instance_id_t const my_id , C1_Enumerat3 argom10, C1_Enumerat1 argom11, C1_Enumerat2 argom12, bool argom13, C1_Enumerat1 argom14)
{
return true;
}

/*
    CNL corrispondente:
    
    { commento: {[} commento: {34,}  se lo stato  non è  uguale a  commento: {53,}  state1  commento: {106,} commento: {36,} e  se il timer MainClass_C1_timer_T10 è attivo e  se la macro  MainClass_C1_macrova_M1   non  è  uguale a RossoGialloVerde commento: {40,}  , assegna alla macro il valore  False 
    
     commento: {46,} assegna alla macro il valore  False  commento: {],}
    }
*/
bool L_P1__Macro6(instance_id_t const my_id , C1_Enumerat2 argom15, C1_Enumerat3 argom16, C1_Enumerat3 argom17, C1_Enumerat1 argom18, bool argom19, C1_Enumerat3 argom20, C1_Enumerat1 argom21)
{
bool res_macro_val;
    
    //  *[* *34,*  se lo stato  non è  uguale a  *53,*  state1  *106,* *36,* e  se il timer MainClass_C1_timer_T10 è attivo e  se la macro  MainClass_C1_macrova_M1   non  è  uguale a RossoGialloVerde
    bool res_AndLogicOP_0 = true;
    bool res_AndLogicOP_1 = true;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (L_P1_C1_GetState(my_id) == C1_St_state));
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_2);
    res_AndLogicOP_1 = (res_AndLogicOP_1 && Timer_Attivo(L_P1__GetMainc47(my_id)));
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_AndLogicOP_1);
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__Macro4(my_id) == rossogiallo1));
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_NotLogicOP_3);
    
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
     
    { commento: {[} commento: {34,}  se il parametro MainClass_C1_parametro_P10 è  minore di  commento: {55,} 6 o  se il controllo ConsDef è uguale a FALSE  commento: {110,} o  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è scaduto o  se il controllo ConsDef è uguale a FALSE  commento: {34,} e  se il parametro MainClass_C1_parametro_P1 è  diverso da  commento: {56,} 6 , assegna alla macro il valore RossoGialloVerde
    
     commento: {46,} assegna alla macro il valore RossoGialloVerde commento: {],}
    }
*/
C1_Enumerat4 L_P1__Macro7(instance_id_t const my_id )
{
C1_Enumerat4 res_macro_val;
    
    //  *[* *34,*  se il parametro MainClass_C1_parametro_P10 è  minore di  *55,* 6 o  se il controllo ConsDef è uguale a FALSE  *110,* o  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è scaduto o  se il controllo ConsDef è uguale a FALSE  *34,* e  se il parametro MainClass_C1_parametro_P1 è  diverso da  *56,* 6
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_OrLogicOP_2 = false;
    res_OrLogicOP_2 = (res_OrLogicOP_2 || (L_P1__GetParamMainc9(my_id) < 6u));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_OrLogicOP_2);
    res_OrLogicOP_1 = (res_OrLogicOP_1 || Timer_Scaduto(L_P1__GetMainc42(my_id)));
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_AndLogicOP_3 = true;
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetParamMainc8(my_id) == 6u));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_4);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_3);
    
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
    
    { commento: {[}  commento: {35,}   se il controllo MainClass_C1_controllo_C9 non è  diverso da  False  commento: {110,} e  se il ripristino del timer  MainClass_C1_restoreTI_TI2 è disattivo , assegna alla macro il valore  True 
    
     commento: {46,} assegna alla macro il valore  False  commento: {],}
    }
*/
bool L_P1__Macro8(instance_id_t const my_id , C1_Enumerat4 argom22, C1_Enumerat1 argom23, C1_Enumerat1 argom24, C1_Enumerat3 argom25, C1_Enumerat1 argom26, C1_Enumerat3 argom27)
{
bool res_macro_val;
    
    //  *[*  *35,*   se il controllo MainClass_C1_controllo_C9 non è  diverso da  False  *110,* e  se il ripristino del timer  MainClass_C1_restoreTI_TI2 è disattivo
    bool res_AndLogicOP_0 = true;
    bool res_NotLogicOP_1 = true;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (L_P1__GetInMainc7(my_id) == false));
    res_NotLogicOP_1 = (res_NotLogicOP_1 && ! res_NotLogicOP_2);
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_NotLogicOP_1);
    res_AndLogicOP_0 = (res_AndLogicOP_0 && Timer_Disattivo(L_P1__GetMainc44(my_id)));
    
    if(res_AndLogicOP_0){
    
    res_macro_val = true;
    }
    else{
    res_macro_val = false;
    }
    return res_macro_val;
}



