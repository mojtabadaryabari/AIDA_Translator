// Codice del modello 'TestCase6', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#include "Logica/ClasseMainClass_C1.h"
#include "Logica/ClasseSubClass_C2.h"
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
	    L_P1__SetOutEvent2(my_id, LDS_MANCMD_UNEXPECTED);
    } else {
        L_P1__SetOutEvent2(my_id, LDS_MANCMD_NOOP);
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
    L_P1__SetMainc20(my_id, 0);
    L_P1__SetMainc22(my_id, 0);
    L_P1__SetMainc24(my_id, rosso);
    L_P1__SetMainc25(my_id, rosso);
    L_P1__SetMainc26(my_id, c75giallo);
    L_P1__SetMainc27(my_id, c75giallo);
    L_P1__SetMainc28(my_id, 0);
    L_P1__SetMainc29(my_id, 0);
    L_P1__SetMainc30(my_id, verde);
    L_P1__SetMainc31(my_id, false);
    L_P1__SetMainc32(my_id, false);
    L_P1__SetMainc33(my_id, rossogiallo1);
    L_P1__SetMainc34(my_id, 0);
    L_P1__SetStato1(my_id, C1_St_Stato);
    // init controlli precedenti
    L_P1__SetMainc15(my_id, true);
    L_P1__SetMainc17(my_id, true);
    L_P1__SetMainc19(my_id, c270);
    // init Timer e Counter
    Timer_AggmInit(L_P1__GetMainc35(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc35_ID);
    Timer_Init(L_P1__GetMainc35(my_id), 4000);
    Timer_AggmInit(L_P1__GetMainc36(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc36_ID);
    Timer_Init(L_P1__GetMainc36(my_id), 4000);
    Timer_AggmInit(L_P1__GetMainc37(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc37_ID);
    Timer_Init(L_P1__GetMainc37(my_id), 4302000);
    Timer_AggmInit(L_P1__GetMainc38(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc38_ID);
    Timer_Init(L_P1__GetMainc38(my_id), 4302000);
    Timer_AggmInit(L_P1__GetMainc39(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc39_ID);
    Timer_Init(L_P1__GetMainc39(my_id), 151000);
    Timer_AggmInit(L_P1__GetMainc40(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc40_ID);
    Timer_Init(L_P1__GetMainc40(my_id), 4000);
    Timer_AggmInit(L_P1__GetMainc41(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc41_ID);
    Timer_Init(L_P1__GetMainc41(my_id), 3024000);
    Timer_AggmInit(L_P1__GetMainc42(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc42_ID);
    Timer_Init(L_P1__GetMainc42(my_id), 113000);
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
    L_P1__SetMainc21(my_id, L_P1__GetMainc20(my_id));
    L_P1__SetMainc23(my_id, L_P1__GetMainc22(my_id));
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
    L_P1__SetOutMainc(my_id, true);
    L_P1__SetOutMainc1(my_id, true);
    L_P1__SetOutMainc2(my_id, c270);
    L_P1__SetOutMainc3(my_id, false);
    L_P1__SetOutMainc4(my_id, false);
}

void L_P1_C1_GUpdatePrev(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C1(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C1(proc_id);
    L_P1__SetMainc15(my_id, L_P1__GetInMainc14(my_id));
    L_P1__SetMainc17(my_id, L_P1__GetInMainc16(my_id));
    L_P1__SetMainc19(my_id, L_P1__GetInMainc18(my_id));
    L_P1__SetMainc21(my_id, L_P1__GetMainc20(my_id));
    L_P1__SetMainc23(my_id, L_P1__GetMainc22(my_id));
}

// ********** Definizione macro **********

// Macro di effetto

/*
    CNL corrispondente:
     
    { commento: {38,}  se il contatore MainClass_C1_contatore_Co7 non è  diverso da  commento: {56,} 125 o  se il controllo ConsDef  è  uguale a FALSE , commento: {69,}Disattiva il timer MainClass_C1_timer_T9
    
     ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V10 il valore  False 
    
    
     commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  uguale a GialloGiallo commento: {35,} o  se il controllo MainClass_C1_controllo_C6 è  uguale a  False  commento: {36,} e  se il timer MainClass_C1_timer_T2 non è attivo o  se il controllo ConsDef  è  uguale a FALSE ,  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V10 il valore  FALSE commento: {67,}
    
       
     commento: {35,}  se il controllo MainClass_C1_controllo_C2 è  diverso da avanzamento commento: {34,} e  se il parametro MainClass_C1_parametro_P8 è  uguale a  True  e  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} o  se il timer MainClass_C1_timer_T9 non è scaduto,  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V2 il valore  True  commento: {67,}
    
       
      se il ripristino dello stato  non è  diverso da  commento: {56,}  state1  commento: {107,} commento: {35,} o  se il controllo MainClass_C1_controllo_C4 è  diverso da c270 commento: {36,} o  se il timer MainClass_C1_timer_T5 non è attivo e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} e  se il contatore MainClass_C1_contatore_Co9 è  uguale a  commento: {53,} 11130, commento: {66,} Assegna al comando MainClass_C1_comando_C4 il valore c270
    
     ,altrimenti  commento: {72,}Azzera il contatore MainClass_C1_contatore_Co7
    
    
    
    }
*/
void L_P1__Macro(instance_id_t const my_id )
{
//  *38,*  se il contatore MainClass_C1_contatore_Co7 non è  diverso da  *56,* 125 o  se il controllo ConsDef  è  uguale a FALSE , *69,*Disattiva il timer MainClass_C1_timer_T9
    // ,altrimenti  *67,* Assegna alla variabile MainClass_C1_variabile_V10 il valore  False
    bool res_OrLogicOP_0 = false;
    bool res_NotLogicOP_1 = true;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (Counter_GetValore(L_P1__GetMainc43(my_id)) == 125u));
    res_NotLogicOP_1 = (res_NotLogicOP_1 && ! res_NotLogicOP_2);
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_1);
    res_OrLogicOP_0 = (res_OrLogicOP_0 || (L_P1__GetInConsd(my_id) == false));
    
    if(res_OrLogicOP_0){
    
    Timer_Disattiva(L_P1__GetMainc42(my_id));
    }else{
    
    L_P1__SetMainc31(my_id,false);
    }
    //  *109,*  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  uguale a GialloGiallo *35,* o  se il controllo MainClass_C1_controllo_C6 è  uguale a  False  *36,* e  se il timer MainClass_C1_timer_T2 non è attivo o  se il controllo ConsDef  è  uguale a FALSE ,  *67,* Assegna alla variabile MainClass_C1_variabile_V10 il valore  FALSE
    bool res_OrLogicOP_3 = false;
    bool res_OrLogicOP_4 = false;
    res_OrLogicOP_4 = (res_OrLogicOP_4 || (L_P1__GetMainc25(my_id) == giallogiall));
    bool res_AndLogicOP_5 = true;
    res_AndLogicOP_5 = (res_AndLogicOP_5 && (L_P1__GetInMainc7(my_id) == false));
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! Timer_Attivo(L_P1__GetMainc40(my_id)));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_6);
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_AndLogicOP_5);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_OrLogicOP_4);
    res_OrLogicOP_3 = (res_OrLogicOP_3 || (L_P1__GetInConsd(my_id) == false));
    
    if(res_OrLogicOP_3){
    
    L_P1__SetMainc31(my_id,false);
    }
    //  *67,*
    //   
    // *35,*  se il controllo MainClass_C1_controllo_C2 è  diverso da avanzamento *34,* e  se il parametro MainClass_C1_parametro_P8 è  uguale a  True  e  se il controllo ConsDef  è  uguale a FALSE  *36,* o  se il timer MainClass_C1_timer_T9 non è scaduto,  *67,* Assegna alla variabile MainClass_C1_variabile_V2 il valore  True
    bool res_OrLogicOP_7 = false;
    bool res_AndLogicOP_8 = true;
    bool res_AndLogicOP_9 = true;
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__GetInMainc5(my_id) == avanzamento));
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_NotLogicOP_10);
    res_AndLogicOP_9 = (res_AndLogicOP_9 && (L_P1__GetParamMainc12(my_id) == true));
    
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_AndLogicOP_9);
    res_AndLogicOP_8 = (res_AndLogicOP_8 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_AndLogicOP_8);
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! Timer_Scaduto(L_P1__GetMainc42(my_id)));
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_NotLogicOP_11);
    
    if(res_OrLogicOP_7){
    
    L_P1__SetMainc32(my_id,true);
    }
    //  *67,*
    //   
    //  se il ripristino dello stato  non è  diverso da  *56,*  state1  *107,* *35,* o  se il controllo MainClass_C1_controllo_C4 è  diverso da c270 *36,* o  se il timer MainClass_C1_timer_T5 non è attivo e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  *38,* e  se il contatore MainClass_C1_contatore_Co9 è  uguale a  *53,* 11130, *66,* Assegna al comando MainClass_C1_comando_C4 il valore c270
    // ,altrimenti  *72,*Azzera il contatore MainClass_C1_contatore_Co7
    bool res_OrLogicOP_12 = false;
    bool res_OrLogicOP_13 = false;
    bool res_NotLogicOP_14 = true;
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (L_P1__GetStato1(my_id) == C1_St_state));
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! res_NotLogicOP_15);
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_NotLogicOP_14);
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (L_P1__GetInMainc6(my_id) == c270));
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_NotLogicOP_16);
    
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_OrLogicOP_13);
    bool res_AndLogicOP_17 = true;
    bool res_AndLogicOP_18 = true;
    bool res_AndLogicOP_19 = true;
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! Timer_Attivo(L_P1__GetMainc41(my_id)));
    res_AndLogicOP_19 = (res_AndLogicOP_19 && res_NotLogicOP_20);
    res_AndLogicOP_19 = (res_AndLogicOP_19 && (L_P1__GetInConsd(my_id) == false));
    
    res_AndLogicOP_18 = (res_AndLogicOP_18 && res_AndLogicOP_19);
    res_AndLogicOP_18 = (res_AndLogicOP_18 && (L_P1__GetInConsd(my_id) == false));
    
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_AndLogicOP_18);
    res_AndLogicOP_17 = (res_AndLogicOP_17 && (Counter_GetValore(L_P1__GetMainc44(my_id)) == 11130u));
    
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_AndLogicOP_17);
    
    if(res_OrLogicOP_12){
    
    L_P1__SetOutMainc2(my_id,c270);
    }else{
    
    Counter_Res(L_P1__GetMainc43(my_id));
    }
}

/*
    CNL corrispondente:
    
    { commento: {37,}  se la variabile MainClass_C1_variabile_V10 non è  diverso da  True  commento: {35,} e  se il controllo MainClass_C1_controllo_C4 non è  uguale a c270, commento: {66,} Assegna al comando MainClass_C1_comando_C10 il valore  True 
    
       
     commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI2 è disattivo commento: {34,} e  se il parametro MainClass_C1_parametro_P8 è  diverso da  True  commento: {35,} o  se il controllo MainClass_C1_controllo_C4 non è  uguale a c270 commento: {35,} e  se il controllo MainClass_C1_controllo_C6 non è  uguale a  True , commento: {72,}Azzera il contatore MainClass_C1_contatore_Co7
    
       
      se il controllo ConsDef è uguale a FALSE  commento: {37,} e  se la variabile MainClass_C1_variabile_V8 è  uguale a  commento: {53,} 6 commento: {37,} e  se la variabile MainClass_C1_variabile_V1 non è  diverso da c270 commento: {37,} e  se la variabile MainClass_C1_variabile_V1 non è  uguale a c270 commento: {35,} e  se il controllo MainClass_C1_controllo_C2 è  uguale a avanzamento commento: {34,} e  se il parametro MainClass_C1_parametro_P10 è  diverso da RossoGiallo, commento: {68,}Attiva il timer MainClass_C1_timer_T9
    
       
     commento: {34,}  se il parametro MainClass_C1_parametro_P7 non è  diverso da  False  commento: {35,} e  se il controllo MainClass_C1_controllo_C4 non è  diverso da c270 commento: {35,} e  se il controllo MainClass_C1_controllo_C4 non è  diverso da c270 e  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} o  se il contatore MainClass_C1_contatore_Co9 non è  minore di  commento: {55,} 132, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V1 il valore c270
    
       
    
    }
*/
void L_P1__Macro1(instance_id_t const my_id )
{
//  *37,*  se la variabile MainClass_C1_variabile_V10 non è  diverso da  True  *35,* e  se il controllo MainClass_C1_controllo_C4 non è  uguale a c270, *66,* Assegna al comando MainClass_C1_comando_C10 il valore  True
    bool res_AndLogicOP_0 = true;
    bool res_NotLogicOP_1 = true;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (L_P1__GetMainc31(my_id) == true));
    res_NotLogicOP_1 = (res_NotLogicOP_1 && ! res_NotLogicOP_2);
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_NotLogicOP_1);
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__GetInMainc6(my_id) == c270));
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_NotLogicOP_3);
    
    if(res_AndLogicOP_0){
    
    L_P1__SetOutMainc1(my_id,true);
    }
    //  *110,*  se il ripristino del timer  MainClass_C1_restoreTI_TI2 è disattivo *34,* e  se il parametro MainClass_C1_parametro_P8 è  diverso da  True  *35,* o  se il controllo MainClass_C1_controllo_C4 non è  uguale a c270 *35,* e  se il controllo MainClass_C1_controllo_C6 non è  uguale a  True , *72,*Azzera il contatore MainClass_C1_contatore_Co7
    bool res_OrLogicOP_4 = false;
    bool res_AndLogicOP_5 = true;
    res_AndLogicOP_5 = (res_AndLogicOP_5 && Timer_Disattivo(L_P1__GetMainc38(my_id)));
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetParamMainc12(my_id) == true));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_6);
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_AndLogicOP_5);
    bool res_AndLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetInMainc6(my_id) == c270));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_8);
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetInMainc7(my_id) == true));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_9);
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_AndLogicOP_7);
    
    if(res_OrLogicOP_4){
    
    Counter_Res(L_P1__GetMainc43(my_id));
    }
    //  se il controllo ConsDef è uguale a FALSE  *37,* e  se la variabile MainClass_C1_variabile_V8 è  uguale a  *53,* 6 *37,* e  se la variabile MainClass_C1_variabile_V1 non è  diverso da c270 *37,* e  se la variabile MainClass_C1_variabile_V1 non è  uguale a c270 *35,* e  se il controllo MainClass_C1_controllo_C2 è  uguale a avanzamento *34,* e  se il parametro MainClass_C1_parametro_P10 è  diverso da RossoGiallo, *68,*Attiva il timer MainClass_C1_timer_T9
    bool res_AndLogicOP_10 = true;
    bool res_AndLogicOP_11 = true;
    bool res_AndLogicOP_12 = true;
    bool res_AndLogicOP_13 = true;
    bool res_AndLogicOP_14 = true;
    res_AndLogicOP_14 = (res_AndLogicOP_14 && (L_P1__GetInConsd(my_id) == false));
    res_AndLogicOP_14 = (res_AndLogicOP_14 && (L_P1__GetMainc34(my_id) == 6u));
    
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_AndLogicOP_14);
    bool res_NotLogicOP_15 = true;
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (L_P1__GetMainc30(my_id) == c270));
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! res_NotLogicOP_16);
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_NotLogicOP_15);
    
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_AndLogicOP_13);
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! (L_P1__GetMainc30(my_id) == c270));
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_NotLogicOP_17);
    
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_AndLogicOP_12);
    res_AndLogicOP_11 = (res_AndLogicOP_11 && (L_P1__GetInMainc5(my_id) == avanzamento));
    
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_AndLogicOP_11);
    bool res_NotLogicOP_18 = true;
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! (L_P1__GetParamMainc9(my_id) == rossogiallo2));
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_NotLogicOP_18);
    
    if(res_AndLogicOP_10){
    
    Timer_Attiva(L_P1__GetMainc42(my_id));
    }
    //  *34,*  se il parametro MainClass_C1_parametro_P7 non è  diverso da  False  *35,* e  se il controllo MainClass_C1_controllo_C4 non è  diverso da c270 *35,* e  se il controllo MainClass_C1_controllo_C4 non è  diverso da c270 e  se il controllo ConsDef  è  uguale a FALSE  *38,* o  se il contatore MainClass_C1_contatore_Co9 non è  minore di  *55,* 132, *67,* Assegna alla variabile MainClass_C1_variabile_V1 il valore c270
    bool res_OrLogicOP_19 = false;
    bool res_AndLogicOP_20 = true;
    bool res_AndLogicOP_21 = true;
    bool res_AndLogicOP_22 = true;
    bool res_NotLogicOP_23 = true;
    bool res_NotLogicOP_24 = true;
    res_NotLogicOP_24 = (res_NotLogicOP_24 && ! (L_P1__GetParamMainc11(my_id) == false));
    res_NotLogicOP_23 = (res_NotLogicOP_23 && ! res_NotLogicOP_24);
    res_AndLogicOP_22 = (res_AndLogicOP_22 && res_NotLogicOP_23);
    bool res_NotLogicOP_25 = true;
    bool res_NotLogicOP_26 = true;
    res_NotLogicOP_26 = (res_NotLogicOP_26 && ! (L_P1__GetInMainc6(my_id) == c270));
    res_NotLogicOP_25 = (res_NotLogicOP_25 && ! res_NotLogicOP_26);
    res_AndLogicOP_22 = (res_AndLogicOP_22 && res_NotLogicOP_25);
    
    res_AndLogicOP_21 = (res_AndLogicOP_21 && res_AndLogicOP_22);
    bool res_NotLogicOP_27 = true;
    bool res_NotLogicOP_28 = true;
    res_NotLogicOP_28 = (res_NotLogicOP_28 && ! (L_P1__GetInMainc6(my_id) == c270));
    res_NotLogicOP_27 = (res_NotLogicOP_27 && ! res_NotLogicOP_28);
    res_AndLogicOP_21 = (res_AndLogicOP_21 && res_NotLogicOP_27);
    
    res_AndLogicOP_20 = (res_AndLogicOP_20 && res_AndLogicOP_21);
    res_AndLogicOP_20 = (res_AndLogicOP_20 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_19 = (res_OrLogicOP_19 || res_AndLogicOP_20);
    bool res_NotLogicOP_29 = true;
    res_NotLogicOP_29 = (res_NotLogicOP_29 && ! (Counter_GetValore(L_P1__GetMainc44(my_id)) < 132u));
    res_OrLogicOP_19 = (res_OrLogicOP_19 || res_NotLogicOP_29);
    
    if(res_OrLogicOP_19){
    
    L_P1__SetMainc30(my_id,c270);
    }
}


// Macro di verifica

/*
    CNL corrispondente:
     
    { commento: {62,} commento: {34,}  se lo stato  è  diverso da  commento: {56,}  state1  commento: {106,} e  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} o  se il parametro MainClass_C1_parametro_P8 è  uguale a  True  commento: {36,} e  se il timer MainClass_C1_timer_T5 non è attivo commento: {34,} o  se il parametro MainClass_C1_parametro_P8 non è  diverso da  True  commento: {34,} o  se il parametro MainClass_C1_parametro_P9 è  maggiore di  commento: {54,} 6, Almeno una delle seguenti { 
     commento: {37,}  se la variabile MainClass_C1_variabile_V10 è  diverso da  False  commento: {38,} o  se il contatore MainClass_C1_contatore_Co9 è  minore di  commento: {55,} 1302, Verifica che   commento: {49,}  commento: {,}  il timer MainClass_C1_timer_T9 sia scaduto
     commento: {104,} e  che  commento: {36,}  il timer MainClass_C1_timer_T2 non sia attivo
    
    
     } Verifica che   commento: {48,49,50,51,}  commento: {,}  il timer MainClass_C1_timer_T2 sia attivo
     commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C6 sia  diverso da  False 
     commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co7 sia  diverso da  commento: {56,} 154
     commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V1 sia  diverso da c270
    
    
    }
*/
bool L_P1__Macro5(instance_id_t const my_id )
{
bool res_AndLogicOP_0 = true;
    
    //  *62,* *34,*  se lo stato  è  diverso da  *56,*  state1  *106,* e  se il controllo ConsDef  è  uguale a FALSE  *34,* o  se il parametro MainClass_C1_parametro_P8 è  uguale a  True  *36,* e  se il timer MainClass_C1_timer_T5 non è attivo *34,* o  se il parametro MainClass_C1_parametro_P8 non è  diverso da  True  *34,* o  se il parametro MainClass_C1_parametro_P9 è  maggiore di  *54,* 6, Almeno una delle seguenti { 
    //   *37,*  se la variabile MainClass_C1_variabile_V10 è  diverso da  False  *38,* o  se il contatore MainClass_C1_contatore_Co9 è  minore di  *55,* 1302, Verifica che   *49,*  *,*  il timer MainClass_C1_timer_T9 sia scaduto
    //   *104,* e  che  *36,*  il timer MainClass_C1_timer_T2 non sia attivo
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_OrLogicOP_4 = false;
    bool res_AndLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1_C1_GetState(my_id) == C1_St_state));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_6);
    res_AndLogicOP_5 = (res_AndLogicOP_5 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_AndLogicOP_5);
    bool res_AndLogicOP_7 = true;
    res_AndLogicOP_7 = (res_AndLogicOP_7 && (L_P1__GetParamMainc12(my_id) == true));
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! Timer_Attivo(L_P1__GetMainc41(my_id)));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_8);
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_AndLogicOP_7);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_OrLogicOP_4);
    bool res_NotLogicOP_9 = true;
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__GetParamMainc12(my_id) == true));
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! res_NotLogicOP_10);
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_NotLogicOP_9);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    res_OrLogicOP_2 = (res_OrLogicOP_2 || (L_P1__GetParamMainc13(my_id) > 6u));
    
    if(res_OrLogicOP_2){
    bool res_ImpliesLogicOp_11 = true;
    bool res_OrLogicOP_12 = false;
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (L_P1__GetMainc31(my_id) == false));
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_NotLogicOP_13);
    res_OrLogicOP_12 = (res_OrLogicOP_12 || (Counter_GetValore(L_P1__GetMainc44(my_id)) < 1302u));
    
    if(res_OrLogicOP_12){
    bool res_AndLogicOP_14 = true;
    res_AndLogicOP_14 = (res_AndLogicOP_14 && Timer_Scaduto(L_P1__GetMainc42(my_id)));
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! Timer_Attivo(L_P1__GetMainc40(my_id)));
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_NotLogicOP_15);
    
    res_ImpliesLogicOp_11 = (res_ImpliesLogicOp_11 && res_AndLogicOP_14);
    }
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_ImpliesLogicOp_11);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *48,49,50,51,*  *,*  il timer MainClass_C1_timer_T2 sia attivo
    //   *104,* o  che  *,*  il controllo MainClass_C1_controllo_C6 sia  diverso da  False 
    //   *104,* e  che   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* e  che  *,*  il contatore MainClass_C1_contatore_Co7 sia  diverso da  *56,* 154
    //   *104,* e  che  *,*  la variabile MainClass_C1_variabile_V1 sia  diverso da c270
    bool res_OrLogicOP_16 = false;
    res_OrLogicOP_16 = (res_OrLogicOP_16 || Timer_Attivo(L_P1__GetMainc40(my_id)));
    bool res_AndLogicOP_17 = true;
    bool res_AndLogicOP_18 = true;
    bool res_AndLogicOP_19 = true;
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! (L_P1__GetInMainc7(my_id) == false));
    res_AndLogicOP_19 = (res_AndLogicOP_19 && res_NotLogicOP_20);
    res_AndLogicOP_19 = (res_AndLogicOP_19 && (L_P1__GetInConsd(my_id) == false));
    
    res_AndLogicOP_18 = (res_AndLogicOP_18 && res_AndLogicOP_19);
    bool res_NotLogicOP_21 = true;
    res_NotLogicOP_21 = (res_NotLogicOP_21 && ! (Counter_GetValore(L_P1__GetMainc43(my_id)) == 154u));
    res_AndLogicOP_18 = (res_AndLogicOP_18 && res_NotLogicOP_21);
    
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_AndLogicOP_18);
    bool res_NotLogicOP_22 = true;
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! (L_P1__GetMainc30(my_id) == c270));
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_NotLogicOP_22);
    
    res_OrLogicOP_16 = (res_OrLogicOP_16 || res_AndLogicOP_17);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_16);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
    
    { commento: {62,}  se la macro  MainClass_C1_macrova_M3 ( con argomento_a5   uguale a c75Giallo ,argomento_a9   uguale a Rosso ,argomento_a8   uguale a c75Giallo ,argomento_a6   uguale a c75Giallo  e argomento_a2   uguale a Verde )  non  è  uguale a c270 commento: {40,}  commento: {35,} e  se il controllo MainClass_C1_controllo_C6 è  uguale a  True  commento: {34,} e  se il parametro MainClass_C1_parametro_P9 è  maggiore di  commento: {54,} 7 e  se l'argomento argomento_ave8 non  è  diverso da RossoGiallo commento: {39,} , Almeno una delle seguenti { 
      se la macro  MainClass_C1_macrova_M6 ( con argomento_a7   uguale a RossoGialloVerde ,argomento_a4   uguale a RossoGialloVerde  e argomento_a10   uguale a RossoGiallo )  non  è  uguale a RossoGiallo commento: {40,}  o  se l'argomento argomento_ave1 è  uguale a  True  commento: {39,} , Verifica che   commento: {48,49,51,}  commento: {,}  il controllo MainClass_C1_controllo_C4 non sia  uguale a c270
     commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co7 sia  maggiore di  commento: {54,} 12
     commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T1 sia scaduto
    
    
     } Verifica che   commento: {48,49,52,}   l'argomento argomento_ave1 sia  uguale a  True  commento: {,} 
     commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T9 sia disattivo
     commento: {104,} e  che  commento: {36,}  il timer MainClass_C1_timer_T9 sia scaduto
     commento: {104,} e  che   l'argomento argomento_ave1 sia  diverso da  False  commento: {39,} 
     commento: {104,} o  che   l'argomento argomento_ave1 non  sia  diverso da  False  commento: {39,} 
     commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C2 sia  uguale a avanzamento
    
    
    }
*/
bool L_P1__Macro6(instance_id_t const my_id , bool argom18, bool argom19, bool argom20, C1_Enumerat4 argom21, C1_Enumerat4 argom22, C1_Enumerat1 argom23)
{
bool res_AndLogicOP_0 = true;
    
    //  *62,*  se la macro  MainClass_C1_macrova_M3 ( con argomento_a5   uguale a c75Giallo ,argomento_a9   uguale a Rosso ,argomento_a8   uguale a c75Giallo ,argomento_a6   uguale a c75Giallo  e argomento_a2   uguale a Verde )  non  è  uguale a c270 *40,*  *35,* e  se il controllo MainClass_C1_controllo_C6 è  uguale a  True  *34,* e  se il parametro MainClass_C1_parametro_P9 è  maggiore di  *54,* 7 e  se l'argomento argomento_ave8 non  è  diverso da RossoGiallo *39,* , Almeno una delle seguenti { 
    //    se la macro  MainClass_C1_macrova_M6 ( con argomento_a7   uguale a RossoGialloVerde ,argomento_a4   uguale a RossoGialloVerde  e argomento_a10   uguale a RossoGiallo )  non  è  uguale a RossoGiallo *40,*  o  se l'argomento argomento_ave1 è  uguale a  True  *39,* , Verifica che   *48,49,51,*  *,*  il controllo MainClass_C1_controllo_C4 non sia  uguale a c270
    //   *104,* e  che  *,*  il contatore MainClass_C1_contatore_Co7 sia  maggiore di  *54,* 12
    //   *104,* e  che  *,*  il timer MainClass_C1_timer_T1 sia scaduto
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_AndLogicOP_2 = true;
    bool res_AndLogicOP_3 = true;
    bool res_AndLogicOP_4 = true;
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__Macro2(my_id,verde,c75giallo,c75giallo,c75giallo,rosso) == c270));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_5);
    res_AndLogicOP_4 = (res_AndLogicOP_4 && (L_P1__GetInMainc7(my_id) == true));
    
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_AndLogicOP_4);
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (L_P1__GetParamMainc13(my_id) > 7u));
    
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_AndLogicOP_3);
    bool res_NotLogicOP_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (argom22 == rossogiallo2));
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! res_NotLogicOP_7);
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_6);
    
    if(res_AndLogicOP_2){
    bool res_ImpliesLogicOp_8 = true;
    bool res_OrLogicOP_9 = false;
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__Macro3(my_id,rossogiallo2,rossogiallo1,rossogiallo1) == rossogiallo2));
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_NotLogicOP_10);
    res_OrLogicOP_9 = (res_OrLogicOP_9 || (argom18 == true));
    
    if(res_OrLogicOP_9){
    bool res_AndLogicOP_11 = true;
    bool res_AndLogicOP_12 = true;
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (L_P1__GetInMainc6(my_id) == c270));
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_NotLogicOP_13);
    res_AndLogicOP_12 = (res_AndLogicOP_12 && (Counter_GetValore(L_P1__GetMainc43(my_id)) > 12u));
    
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_AndLogicOP_12);
    res_AndLogicOP_11 = (res_AndLogicOP_11 && Timer_Scaduto(L_P1__GetMainc39(my_id)));
    
    res_ImpliesLogicOp_8 = (res_ImpliesLogicOp_8 && res_AndLogicOP_11);
    }
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_ImpliesLogicOp_8);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *48,49,52,*   l'argomento argomento_ave1 sia  uguale a  True  *,* 
    //   *104,* o  che  *,*  il timer MainClass_C1_timer_T9 sia disattivo
    //   *104,* e  che  *36,*  il timer MainClass_C1_timer_T9 sia scaduto
    //   *104,* e  che   l'argomento argomento_ave1 sia  diverso da  False  *39,* 
    //   *104,* o  che   l'argomento argomento_ave1 non  sia  diverso da  False  *39,* 
    //   *104,* o  che  *,*  il controllo MainClass_C1_controllo_C2 sia  uguale a avanzamento
    bool res_OrLogicOP_14 = false;
    bool res_OrLogicOP_15 = false;
    bool res_OrLogicOP_16 = false;
    res_OrLogicOP_16 = (res_OrLogicOP_16 || (argom18 == true));
    bool res_AndLogicOP_17 = true;
    bool res_AndLogicOP_18 = true;
    res_AndLogicOP_18 = (res_AndLogicOP_18 && Timer_Disattivo(L_P1__GetMainc42(my_id)));
    res_AndLogicOP_18 = (res_AndLogicOP_18 && Timer_Scaduto(L_P1__GetMainc42(my_id)));
    
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_AndLogicOP_18);
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (argom18 == false));
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_NotLogicOP_19);
    
    res_OrLogicOP_16 = (res_OrLogicOP_16 || res_AndLogicOP_17);
    
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_OrLogicOP_16);
    bool res_NotLogicOP_20 = true;
    bool res_NotLogicOP_21 = true;
    res_NotLogicOP_21 = (res_NotLogicOP_21 && ! (argom18 == false));
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! res_NotLogicOP_21);
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_NotLogicOP_20);
    
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_OrLogicOP_15);
    res_OrLogicOP_14 = (res_OrLogicOP_14 || (L_P1__GetInMainc5(my_id) == avanzamento));
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_14);
    
    
    
    return res_AndLogicOP_0;
}


// Macro valorizzate

/*
    CNL corrispondente:
    
    { commento: {[} commento: {35,}  se il controllo MainClass_C1_controllo_C6 è  uguale a  False  commento: {37,} e  se la variabile MainClass_C1_variabile_V10 non è  uguale a  False  commento: {34,} o  se lo stato  non è  uguale a  commento: {53,}  state1  commento: {106,} commento: {38,} e  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  commento: {53,} 153  , assegna alla macro il valore c270
    
     commento: {46,} assegna alla macro il valore c270 commento: {],}
    }
*/
C1_Enumerat3 L_P1__Macro2(instance_id_t const my_id , C1_Enumerat3 argom3, C1_Enumerat2 argom4, C1_Enumerat2 argom5, C1_Enumerat2 argom6, C1_Enumerat1 argom7)
{
C1_Enumerat3 res_macro_val;
    
    //  *[* *35,*  se il controllo MainClass_C1_controllo_C6 è  uguale a  False  *37,* e  se la variabile MainClass_C1_variabile_V10 non è  uguale a  False  *34,* o  se lo stato  non è  uguale a  *53,*  state1  *106,* *38,* e  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  *53,* 153
    bool res_OrLogicOP_0 = false;
    bool res_AndLogicOP_1 = true;
    res_AndLogicOP_1 = (res_AndLogicOP_1 && (L_P1__GetInMainc7(my_id) == false));
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (L_P1__GetMainc31(my_id) == false));
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_2);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_1);
    bool res_AndLogicOP_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1_C1_GetState(my_id) == C1_St_state));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_4);
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (Counter_GetValore(L_P1__GetMainc43(my_id)) == 153u));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_5);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_3);
    
    if(res_OrLogicOP_0){
    
    res_macro_val = c270;
    }
    else{
    res_macro_val = c270;
    }
    return res_macro_val;
}

/*
    CNL corrispondente:
    
    { commento: {[}
     commento: {46,} assegna alla macro il valore RossoGiallo commento: {],}
    }
*/
C1_Enumerat4 L_P1__Macro3(instance_id_t const my_id , C1_Enumerat4 argom8, C1_Enumerat4 argom9, C1_Enumerat4 argom10)
{
return rossogiallo2;
}

/*
    CNL corrispondente:
    
    { commento: {[}  se l'argomento argomento_a1 è  uguale a  False  commento: {39,}  , assegna alla macro il valore  False 
    
     commento: {46,} assegna alla macro il valore  False  commento: {],}
    }
*/
bool L_P1__Macro4(instance_id_t const my_id , bool argom11, C1_Enumerat3 argom12, C1_Enumerat1 argom13, C1_Enumerat1 argom14, C1_Enumerat1 argom15, C1_Enumerat1 argom16, C1_Enumerat1 argom17)
{
bool res_macro_val;
    if((argom11 == false)){
    
    res_macro_val = false;
    }
    else{
    res_macro_val = false;
    }
    return res_macro_val;
}



