// Codice del modello 'TestCase17', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#include "Logica/ClasseMainClass_C1.h"
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
    L_P1__SetMainc15(my_id, rossoverde);
    L_P1__SetMainc17(my_id, 0);
    L_P1__SetMainc19(my_id, 0);
    L_P1__SetMainc20(my_id, 0);
    L_P1__SetMainc21(my_id, rossogiallo);
    L_P1__SetMainc22(my_id, rossogiallo);
    L_P1__SetMainc23(my_id, 0);
    L_P1__SetMainc24(my_id, 0);
    L_P1__SetMainc25(my_id, false);
    L_P1__SetMainc26(my_id, false);
    L_P1__SetMainc27(my_id, 0);
    L_P1__SetMainc28(my_id, rossogiallo);
    L_P1__SetMainc29(my_id, avviox);
    L_P1__SetMainc30(my_id, 0);
    L_P1__SetMainc31(my_id, false);
    L_P1__SetStato1(my_id, C1_St_Stato);
    // init controlli precedenti
    L_P1__SetMainc14(my_id, true);
    // init Timer e Counter
    Timer_AggmInit(L_P1__GetMainc32(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc32_ID);
    Timer_Init(L_P1__GetMainc32(my_id), 5421000);
    Timer_AggmInit(L_P1__GetMainc33(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc33_ID);
    Timer_Init(L_P1__GetMainc33(my_id), 5421000);
    Timer_AggmInit(L_P1__GetMainc34(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc34_ID);
    Timer_Init(L_P1__GetMainc34(my_id), 33000);
    Timer_AggmInit(L_P1__GetMainc35(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc35_ID);
    Timer_Init(L_P1__GetMainc35(my_id), 33000);
    Timer_AggmInit(L_P1__GetMainc36(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc36_ID);
    Timer_Init(L_P1__GetMainc36(my_id), 40000);
    Timer_AggmInit(L_P1__GetMainc37(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc37_ID);
    Timer_Init(L_P1__GetMainc37(my_id), 40000);
    Timer_AggmInit(L_P1__GetMainc38(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc38_ID);
    Timer_Init(L_P1__GetMainc38(my_id), 2000);
    Timer_AggmInit(L_P1__GetMainc39(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc39_ID);
    Timer_Init(L_P1__GetMainc39(my_id), 354000);
    Timer_AggmInit(L_P1__GetMainc40(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc40_ID);
    Timer_Init(L_P1__GetMainc40(my_id), 1000);
    Timer_AggmInit(L_P1__GetMainc41(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc41_ID);
    Timer_Init(L_P1__GetMainc41(my_id), 32130000);
    Timer_AggmInit(L_P1__GetMainc42(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc42_ID);
    Timer_Init(L_P1__GetMainc42(my_id), 55000);
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
    L_P1__SetMainc16(my_id, L_P1__GetMainc15(my_id));
    L_P1__SetMainc18(my_id, L_P1__GetMainc17(my_id));
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
    Timer_Exec(L_P1__GetMainc32(my_id));
    Timer_Exec(L_P1__GetMainc33(my_id));
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
    L_P1__SetOutMainc(my_id, false);
    L_P1__SetOutMainc1(my_id, false);
    L_P1__SetOutMainc2(my_id, false);
    L_P1__SetOutMainc3(my_id, true);
    L_P1__SetOutMainc4(my_id, ac);
}

void L_P1_C1_GUpdatePrev(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C1(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C1(proc_id);
    L_P1__SetMainc14(my_id, L_P1__GetInMainc13(my_id));
    L_P1__SetMainc16(my_id, L_P1__GetMainc15(my_id));
    L_P1__SetMainc18(my_id, L_P1__GetMainc17(my_id));
}

// ********** Definizione macro **********

// Macro di effetto

/*
    CNL corrispondente:
     
    { commento: {34,}  se lo stato  è  uguale a  commento: {53,}  state1  commento: {106,} commento: {38,} o  se il contatore MainClass_C1_contatore_Co5 è  uguale a  commento: {53,} 123 commento: {37,} e  se la variabile MainClass_C1_variabile_V10 non è  minore di  commento: {55,} 2 commento: {34,} e  se il parametro MainClass_C1_parametro_P10 è  minore di  commento: {55,} 10 commento: {34,} o  se il parametro MainClass_C1_parametro_P10 è  uguale a  commento: {53,} 5,  Applica gli effetti
           della macro MainClass_C1_macroef_M8( con argomento_af3   uguale a c75Giallo ,argomento_af8   uguale a c75Giallo ) commento: {73,}
    
       
      se il controllo ConsDef è uguale a FALSE , commento: {66,} Assegna al comando MainClass_C1_comando_C2 il valore  True 
    
       
      se il controllo ConsDef  è  uguale a FALSE  commento: {38,} o  se il contatore MainClass_C1_contatore_Co5 è  minore di  commento: {55,} 154 o  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} o  se il timer MainClass_C1_timer_T4 non è attivo commento: {38,} o  se il contatore MainClass_C1_contatore_Co5 non è  minore di  commento: {55,} 1221, commento: {68,}Attiva il timer MainClass_C1_timer_T8
    
       
    
    }
*/
void L_P1__Macro(instance_id_t const my_id )
{
//  *34,*  se lo stato  è  uguale a  *53,*  state1  *106,* *38,* o  se il contatore MainClass_C1_contatore_Co5 è  uguale a  *53,* 123 *37,* e  se la variabile MainClass_C1_variabile_V10 non è  minore di  *55,* 2 *34,* e  se il parametro MainClass_C1_parametro_P10 è  minore di  *55,* 10 *34,* o  se il parametro MainClass_C1_parametro_P10 è  uguale a  *53,* 5,  Applica gli effetti
    //       della macro MainClass_C1_macroef_M8( con argomento_af3   uguale a c75Giallo ,argomento_af8   uguale a c75Giallo )
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    res_OrLogicOP_1 = (res_OrLogicOP_1 || (L_P1_C1_GetState(my_id) == C1_St_state));
    bool res_AndLogicOP_2 = true;
    bool res_AndLogicOP_3 = true;
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (Counter_GetValore(L_P1__GetMainc44(my_id)) == 123u));
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetMainc27(my_id) < 2u));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_4);
    
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_AndLogicOP_3);
    res_AndLogicOP_2 = (res_AndLogicOP_2 && (L_P1__GetParamMainc9(my_id) < 10u));
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_2);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    res_OrLogicOP_0 = (res_OrLogicOP_0 || (L_P1__GetParamMainc9(my_id) == 5u));
    
    if(res_OrLogicOP_0){
    
    L_P1__Macro2(my_id,c75giallo,c75giallo);
    }
    //  *73,*
    //   
    //  se il controllo ConsDef è uguale a FALSE , *66,* Assegna al comando MainClass_C1_comando_C2 il valore  True
    if((L_P1__GetInConsd(my_id) == false)){
    
    L_P1__SetOutMainc(my_id,true);
    }
    //  se il controllo ConsDef  è  uguale a FALSE  *38,* o  se il contatore MainClass_C1_contatore_Co5 è  minore di  *55,* 154 o  se il controllo ConsDef  è  uguale a FALSE  *36,* o  se il timer MainClass_C1_timer_T4 non è attivo *38,* o  se il contatore MainClass_C1_contatore_Co5 non è  minore di  *55,* 1221, *68,*Attiva il timer MainClass_C1_timer_T8
    bool res_OrLogicOP_5 = false;
    bool res_OrLogicOP_6 = false;
    bool res_OrLogicOP_7 = false;
    bool res_OrLogicOP_8 = false;
    res_OrLogicOP_8 = (res_OrLogicOP_8 || (L_P1__GetInConsd(my_id) == false));
    res_OrLogicOP_8 = (res_OrLogicOP_8 || (Counter_GetValore(L_P1__GetMainc44(my_id)) < 154u));
    
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_OrLogicOP_8);
    res_OrLogicOP_7 = (res_OrLogicOP_7 || (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_OrLogicOP_7);
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! Timer_Attivo(L_P1__GetMainc39(my_id)));
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_NotLogicOP_9);
    
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_OrLogicOP_6);
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (Counter_GetValore(L_P1__GetMainc44(my_id)) < 1221u));
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_NotLogicOP_10);
    
    if(res_OrLogicOP_5){
    
    Timer_Attiva(L_P1__GetMainc41(my_id));
    }
}

/*
    CNL corrispondente:
    
    { commento: {34,}  se il parametro MainClass_C1_parametro_P10 è  maggiore di  commento: {54,} 4 e  se il controllo ConsDef  è  uguale a FALSE ,  Applica gli effetti
           della macro MainClass_C1_macroef_M3   commento: {73,}
    
       
    
    }
*/
void L_P1__Macro1(instance_id_t const my_id )
{
//  *34,*  se il parametro MainClass_C1_parametro_P10 è  maggiore di  *54,* 4 e  se il controllo ConsDef  è  uguale a FALSE ,  Applica gli effetti
    //       della macro MainClass_C1_macroef_M3
    bool res_AndLogicOP_0 = true;
    res_AndLogicOP_0 = (res_AndLogicOP_0 && (L_P1__GetParamMainc9(my_id) > 4u));
    res_AndLogicOP_0 = (res_AndLogicOP_0 && (L_P1__GetInConsd(my_id) == false));
    
    if(res_AndLogicOP_0){
    
    L_P1__Macro(my_id);
    }
}

/*
    CNL corrispondente:
    
    {  se l'argomento argomento_af3 non  è  diverso da c75Giallo commento: {39,}  commento: {38,} e  se il contatore MainClass_C1_contatore_Co2 non è  minore di  commento: {55,} 111 commento: {34,} o  se il parametro MainClass_C1_parametro_P8 è  diverso da  True  commento: {36,} o  se il timer MainClass_C1_timer_T5 è attivo, commento: {66,} Assegna al comando MainClass_C1_comando_C2 il valore  True 
    
     ,altrimenti  commento: {68,}Attiva il timer MainClass_C1_timer_T4
    
    
    
    }
*/
void L_P1__Macro2(instance_id_t const my_id , C1_Enumerat1 argom, C1_Enumerat1 argom1)
{
//  se l'argomento argomento_af3 non  è  diverso da c75Giallo *39,*  *38,* e  se il contatore MainClass_C1_contatore_Co2 non è  minore di  *55,* 111 *34,* o  se il parametro MainClass_C1_parametro_P8 è  diverso da  True  *36,* o  se il timer MainClass_C1_timer_T5 è attivo, *66,* Assegna al comando MainClass_C1_comando_C2 il valore  True 
    // ,altrimenti  *68,*Attiva il timer MainClass_C1_timer_T4
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_AndLogicOP_2 = true;
    bool res_NotLogicOP_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (argom == c75giallo));
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! res_NotLogicOP_4);
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_3);
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (Counter_GetValore(L_P1__GetMainc43(my_id)) < 111u));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_5);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_2);
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetParamMainc11(my_id) == true));
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_NotLogicOP_6);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    res_OrLogicOP_0 = (res_OrLogicOP_0 || Timer_Attivo(L_P1__GetMainc40(my_id)));
    
    if(res_OrLogicOP_0){
    
    L_P1__SetOutMainc(my_id,true);
    }else{
    
    Timer_Attiva(L_P1__GetMainc39(my_id));
    }
}


// Macro di verifica

/*
    CNL corrispondente:
    
    { commento: {61,} commento: {37,}  se la variabile MainClass_C1_variabile_V9 è  diverso da  False , Tutte le seguenti { 
     commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è scaduto commento: {36,} o  se il timer MainClass_C1_timer_T4 è attivo o  se l'argomento argomento_ave9 è  uguale a avanzamento commento: {39,}  commento: {36,} o  se il timer MainClass_C1_timer_T8 non è disattivo, Verifica che   commento: {49,50,52,}   l'argomento argomento_ave6 non  sia  uguale a  True  commento: {,} 
     commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V8 non sia  minore di  commento: {55,} 4
     commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T1 sia disattivo
    
    
     } Verifica che   commento: {48,52,}   l'argomento argomento_ave6 sia  uguale a  True  commento: {,} 
     commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C4 sia  diverso da avanzamento
     commento: {104,} e  che  commento: {35,}  il controllo MainClass_C1_controllo_C5 sia  uguale a  False 
     commento: {104,} o  che  commento: {35,}  il controllo MainClass_C1_controllo_C5 sia  diverso da  False 
     commento: {104,} o  che   l'argomento argomento_ave6 sia  diverso da  True  commento: {39,} 
    
    
    }
*/
bool L_P1__Macro8(instance_id_t const my_id , bool argom22, C1_Enumerat4 argom23)
{
bool res_AndLogicOP_0 = true;
    
    //  *61,* *37,*  se la variabile MainClass_C1_variabile_V9 è  diverso da  False , Tutte le seguenti { 
    //   *110,*  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è scaduto *36,* o  se il timer MainClass_C1_timer_T4 è attivo o  se l'argomento argomento_ave9 è  uguale a avanzamento *39,*  *36,* o  se il timer MainClass_C1_timer_T8 non è disattivo, Verifica che   *49,50,52,*   l'argomento argomento_ave6 non  sia  uguale a  True  *,* 
    //   *104,* e  che  *,*  la variabile MainClass_C1_variabile_V8 non sia  minore di  *55,* 4
    //   *104,* e  che  *,*  il timer MainClass_C1_timer_T1 sia disattivo
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (L_P1__GetMainc31(my_id) == false));
    if(res_NotLogicOP_2){
    bool res_ImpliesLogicOp_3 = true;
    bool res_OrLogicOP_4 = false;
    bool res_OrLogicOP_5 = false;
    bool res_OrLogicOP_6 = false;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! Timer_Scaduto(L_P1__GetMainc33(my_id)));
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_NotLogicOP_7);
    res_OrLogicOP_6 = (res_OrLogicOP_6 || Timer_Attivo(L_P1__GetMainc39(my_id)));
    
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_OrLogicOP_6);
    res_OrLogicOP_5 = (res_OrLogicOP_5 || (argom23 == avanzamento));
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_OrLogicOP_5);
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! Timer_Disattivo(L_P1__GetMainc41(my_id)));
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_NotLogicOP_8);
    
    if(res_OrLogicOP_4){
    bool res_AndLogicOP_9 = true;
    bool res_AndLogicOP_10 = true;
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (argom22 == true));
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_NotLogicOP_11);
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (L_P1__GetMainc30(my_id) < 4u));
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_NotLogicOP_12);
    
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_AndLogicOP_10);
    res_AndLogicOP_9 = (res_AndLogicOP_9 && Timer_Disattivo(L_P1__GetMainc38(my_id)));
    
    res_ImpliesLogicOp_3 = (res_ImpliesLogicOp_3 && res_AndLogicOP_9);
    }
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_ImpliesLogicOp_3);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *48,52,*   l'argomento argomento_ave6 sia  uguale a  True  *,* 
    //   *104,* o  che  *,*  il controllo MainClass_C1_controllo_C4 sia  diverso da avanzamento
    //   *104,* e  che  *35,*  il controllo MainClass_C1_controllo_C5 sia  uguale a  False 
    //   *104,* o  che  *35,*  il controllo MainClass_C1_controllo_C5 sia  diverso da  False 
    //   *104,* o  che   l'argomento argomento_ave6 sia  diverso da  True
    bool res_OrLogicOP_13 = false;
    bool res_OrLogicOP_14 = false;
    bool res_OrLogicOP_15 = false;
    res_OrLogicOP_15 = (res_OrLogicOP_15 || (argom22 == true));
    bool res_AndLogicOP_16 = true;
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! (L_P1__GetInMainc6(my_id) == avanzamento));
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_NotLogicOP_17);
    res_AndLogicOP_16 = (res_AndLogicOP_16 && (L_P1__GetInMainc7(my_id) == false));
    
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_AndLogicOP_16);
    
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_OrLogicOP_15);
    bool res_NotLogicOP_18 = true;
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! (L_P1__GetInMainc7(my_id) == false));
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_NotLogicOP_18);
    
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_OrLogicOP_14);
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (argom22 == true));
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_NotLogicOP_19);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_13);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
    
    { commento: {34,}  se il parametro MainClass_C1_parametro_P1 è  diverso da  True , Verifica che   commento: {49,50,52,}   l'argomento argomento_ave10 non  sia  diverso da AC commento: {,} 
     commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T5 non sia disattivo
     commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V10 sia  uguale a  commento: {53,} 2
     commento: {104,} e  che   l'argomento argomento_ave10 sia  uguale a AC commento: {39,} 
     commento: {104,} o  che  commento: {37,}  la variabile MainClass_C1_variabile_V10 non sia  minore di  commento: {55,} 2
    
    
    }
*/
bool L_P1__Macro9(instance_id_t const my_id , C1_Enumerat2 argom24, C1_Enumerat4 argom25)
{
bool res_AndLogicOP_0 = true;
    
    //  *34,*  se il parametro MainClass_C1_parametro_P1 è  diverso da  True , Verifica che   *49,50,52,*   l'argomento argomento_ave10 non  sia  diverso da AC *,* 
    //   *104,* o  che  *,*  il timer MainClass_C1_timer_T5 non sia disattivo
    //   *104,* e  che  *,*  la variabile MainClass_C1_variabile_V10 sia  uguale a  *53,* 2
    //   *104,* e  che   l'argomento argomento_ave10 sia  uguale a AC *39,* 
    //   *104,* o  che  *37,*  la variabile MainClass_C1_variabile_V10 non sia  minore di  *55,* 2
    bool res_ImpliesLogicOp_1 = true;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (L_P1__GetParamMainc8(my_id) == true));
    if(res_NotLogicOP_2){
    bool res_OrLogicOP_3 = false;
    bool res_OrLogicOP_4 = false;
    bool res_NotLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (argom24 == ac));
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! res_NotLogicOP_6);
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_NotLogicOP_5);
    bool res_AndLogicOP_7 = true;
    bool res_AndLogicOP_8 = true;
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! Timer_Disattivo(L_P1__GetMainc40(my_id)));
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_9);
    res_AndLogicOP_8 = (res_AndLogicOP_8 && (L_P1__GetMainc27(my_id) == 2u));
    
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_AndLogicOP_8);
    res_AndLogicOP_7 = (res_AndLogicOP_7 && (argom24 == ac));
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_AndLogicOP_7);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_OrLogicOP_4);
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__GetMainc27(my_id) < 2u));
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_NotLogicOP_10);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_OrLogicOP_3);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    
    
    return res_AndLogicOP_0;
}


// Macro valorizzate

/*
    CNL corrispondente:
    
    { commento: {[}
     commento: {46,} assegna alla macro il valore c75Giallo commento: {],}
    }
*/
C1_Enumerat1 L_P1__Macro3(instance_id_t const my_id , C1_Enumerat3 argom2, bool argom3, C1_Enumerat2 argom4)
{
return c75giallo;
}

/*
    CNL corrispondente:
    
    { commento: {[}
     commento: {46,} assegna alla macro il valore c75Giallo commento: {],}
    }
*/
C1_Enumerat1 L_P1__Macro4(instance_id_t const my_id , C1_Enumerat2 argom5, C1_Enumerat2 argom6, C1_Enumerat4 argom7, C1_Enumerat2 argom8, C1_Enumerat2 argom9, C1_Enumerat2 argom10)
{
return c75giallo;
}

/*
    CNL corrispondente:
    
    { commento: {[}  se l'argomento argomento_a7 è  uguale a  False  commento: {39,}  , assegna alla macro il valore c75Giallo
    
     commento: {46,} assegna alla macro il valore c75Giallo commento: {],}
    }
*/
C1_Enumerat1 L_P1__Macro5(instance_id_t const my_id , C1_Enumerat4 argom11, C1_Enumerat4 argom12, bool argom13, C1_Enumerat3 argom14)
{
C1_Enumerat1 res_macro_val;
    if((argom13 == false)){
    
    res_macro_val = c75giallo;
    }
    else{
    res_macro_val = c75giallo;
    }
    return res_macro_val;
}

/*
    CNL corrispondente:
    
    { commento: {[} commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI2 è scaduto commento: {34,} e  se il parametro MainClass_C1_parametro_P10 è  maggiore di  commento: {54,} 2 commento: {34,} e  se il parametro MainClass_C1_parametro_P8 è  uguale a  False  commento: {37,} e  se la variabile MainClass_C1_variabile_V10 non è  minore di  commento: {55,} 7 commento: {110,} o  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è disattivo commento: {34,} e  se lo stato  è  diverso da  commento: {56,}  state1  commento: {106,} , assegna alla macro il valore  True 
    
     commento: {46,} assegna alla macro il valore  True  commento: {],}
    }
*/
bool L_P1__Macro6(instance_id_t const my_id , bool argom15, C1_Enumerat3 argom16)
{
bool res_macro_val;
    
    //  *[* *110,*  se il ripristino del timer  MainClass_C1_restoreTI_TI2 è scaduto *34,* e  se il parametro MainClass_C1_parametro_P10 è  maggiore di  *54,* 2 *34,* e  se il parametro MainClass_C1_parametro_P8 è  uguale a  False  *37,* e  se la variabile MainClass_C1_variabile_V10 non è  minore di  *55,* 7 *110,* o  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è disattivo *34,* e  se lo stato  è  diverso da  *56,*  state1
    bool res_OrLogicOP_0 = false;
    bool res_AndLogicOP_1 = true;
    bool res_AndLogicOP_2 = true;
    bool res_AndLogicOP_3 = true;
    res_AndLogicOP_3 = (res_AndLogicOP_3 && Timer_Scaduto(L_P1__GetMainc35(my_id)));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (L_P1__GetParamMainc9(my_id) > 2u));
    
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_AndLogicOP_3);
    res_AndLogicOP_2 = (res_AndLogicOP_2 && (L_P1__GetParamMainc11(my_id) == false));
    
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_AndLogicOP_2);
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetMainc27(my_id) < 7u));
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_4);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_1);
    bool res_AndLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! Timer_Disattivo(L_P1__GetMainc33(my_id)));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_6);
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1_C1_GetState(my_id) == C1_St_state));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_7);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_5);
    
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
     commento: {46,} assegna alla macro il valore AC commento: {],}
    }
*/
C1_Enumerat2 L_P1__Macro7(instance_id_t const my_id , C1_Enumerat3 argom17, C1_Enumerat3 argom18, C1_Enumerat2 argom19, C1_Enumerat4 argom20, C1_Enumerat4 argom21)
{
return ac;
}



