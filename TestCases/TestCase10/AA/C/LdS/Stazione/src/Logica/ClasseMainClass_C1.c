// Codice del modello 'TestCase10', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
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
    if (L_P1__GetCAEvent2(my_id)) {
        ++n;
    }
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
    L_P1__SetMainc12(my_id, 0);
    L_P1__SetMainc14(my_id, false);
    L_P1__SetMainc15(my_id, false);
    L_P1__SetMainc16(my_id, 0);
    L_P1__SetMainc17(my_id, 0);
    L_P1__SetMainc18(my_id, 0);
    L_P1__SetMainc19(my_id, c270xx);
    L_P1__SetMainc20(my_id, false);
    L_P1__SetMainc21(my_id, c180x);
    L_P1__SetMainc22(my_id, 0);
    L_P1__SetStato1(my_id, C1_St_Stato);
    // init controlli precedenti
    L_P1__SetMainc9(my_id, true);
    L_P1__SetMainc11(my_id, false);
    // init Timer e Counter
    Timer_AggmInit(L_P1__GetMainc23(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc23_ID);
    Timer_Init(L_P1__GetMainc23(my_id), 43000);
    Timer_AggmInit(L_P1__GetMainc24(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc24_ID);
    Timer_Init(L_P1__GetMainc24(my_id), 43000);
    Timer_AggmInit(L_P1__GetMainc25(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc25_ID);
    Timer_Init(L_P1__GetMainc25(my_id), 3000);
    Timer_AggmInit(L_P1__GetMainc26(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc26_ID);
    Timer_Init(L_P1__GetMainc26(my_id), 3000);
    Timer_AggmInit(L_P1__GetMainc27(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc27_ID);
    Timer_Init(L_P1__GetMainc27(my_id), 5403000);
    Timer_AggmInit(L_P1__GetMainc28(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc28_ID);
    Timer_Init(L_P1__GetMainc28(my_id), 240000);
    Timer_AggmInit(L_P1__GetMainc29(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc29_ID);
    Timer_Init(L_P1__GetMainc29(my_id), 3215000);
    Timer_AggmInit(L_P1__GetMainc30(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc30_ID);
    Timer_Init(L_P1__GetMainc30(my_id), 4215000);
    Counter_AggmInit(L_P1__GetMainc31(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc31_ID);
    Counter_Init(L_P1__GetMainc31(my_id));
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
    L_P1__SetMainc13(my_id, L_P1__GetMainc12(my_id));
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
    Timer_Exec(L_P1__GetMainc23(my_id));
    Timer_Exec(L_P1__GetMainc24(my_id));
    Timer_Exec(L_P1__GetMainc25(my_id));
    Timer_Exec(L_P1__GetMainc26(my_id));
    Timer_Exec(L_P1__GetMainc27(my_id));
    Timer_Exec(L_P1__GetMainc28(my_id));
    Timer_Exec(L_P1__GetMainc29(my_id));
    Timer_Exec(L_P1__GetMainc30(my_id));
}

void L_P1_C1_GSetSafe(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C1(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C1(proc_id);
    L_P1__SetOutMainc(my_id, true);
    L_P1__SetOutMainc1(my_id, avviox);
    L_P1__SetOutMainc2(my_id, true);
    L_P1__SetOutMainc3(my_id, c270x);
    L_P1__SetOutMainc4(my_id, c270x);
}

void L_P1_C1_GUpdatePrev(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C1(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C1(proc_id);
    L_P1__SetMainc9(my_id, L_P1__GetInMainc8(my_id));
    L_P1__SetMainc11(my_id, L_P1__GetInMainc10(my_id));
    L_P1__SetMainc13(my_id, L_P1__GetMainc12(my_id));
}

// ********** Definizione macro **********

// Macro di effetto

/*
    CNL corrispondente:
    
    { commento: {35,}  se il controllo MainClass_C1_controllo_C6 non è  diverso da AC commento: {36,} o  se il timer MainClass_C1_timer_T3 è scaduto, commento: {71,}Decrementa il contatore MainClass_C1_contatore_Co1
    
     ,altrimenti   commento: {67,} Assegna alla variabile MainClass_C1_variabile_V8 il valore avviox commento: {67,}
    
    
     commento: {38,}  se il contatore MainClass_C1_contatore_Co1 è  diverso da  commento: {56,} 13403 commento: {36,} e  se il timer MainClass_C1_timer_T3 non è disattivo commento: {35,} o  se il controllo MainClass_C1_controllo_C7 è  uguale a  False  commento: {36,} e  se il timer MainClass_C1_timer_T3 non è attivo commento: {37,} e  se la variabile MainClass_C1_variabile_V8 è  diverso da avviox commento: {36,} e  se il timer MainClass_C1_timer_T8 è attivo, commento: {71,}Decrementa il contatore MainClass_C1_contatore_Co1
    
     ,altrimenti  commento: {71,}Decrementa il contatore MainClass_C1_contatore_Co1
    
    
      se il controllo ConsDef è uguale a FALSE  commento: {37,} e  se la variabile MainClass_C1_variabile_V3 è  uguale a c270x commento: {36,} o  se il timer MainClass_C1_timer_T3 è scaduto,  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V3 il valore c270x commento: {67,}
    
       
      se il controllo ConsDef è uguale a FALSE  commento: {34,} o  se il parametro MainClass_C1_parametro_P4 non è  uguale a AC commento: {37,} e  se la variabile MainClass_C1_variabile_V8 è  uguale a avviox, commento: {66,} Assegna al comando MainClass_C1_comando_C10 il valore  True 
    
     ,altrimenti  commento: {66,} Assegna al comando MainClass_C1_comando_C8 il valore c270x
    
    
    
    }
*/
void L_P1__Macro(instance_id_t const my_id )
{
//  *35,*  se il controllo MainClass_C1_controllo_C6 non è  diverso da AC *36,* o  se il timer MainClass_C1_timer_T3 è scaduto, *71,*Decrementa il contatore MainClass_C1_contatore_Co1
    // ,altrimenti   *67,* Assegna alla variabile MainClass_C1_variabile_V8 il valore avviox
    bool res_OrLogicOP_0 = false;
    bool res_NotLogicOP_1 = true;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (L_P1__GetInMainc5(my_id) == ac));
    res_NotLogicOP_1 = (res_NotLogicOP_1 && ! res_NotLogicOP_2);
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_1);
    res_OrLogicOP_0 = (res_OrLogicOP_0 || Timer_Scaduto(L_P1__GetMainc27(my_id)));
    
    if(res_OrLogicOP_0){
    
    Counter_Decr(L_P1__GetMainc31(my_id));
    }else{
    
    L_P1__SetMainc21(my_id,avviox);
    }
    //  *67,*
    // *38,*  se il contatore MainClass_C1_contatore_Co1 è  diverso da  *56,* 13403 *36,* e  se il timer MainClass_C1_timer_T3 non è disattivo *35,* o  se il controllo MainClass_C1_controllo_C7 è  uguale a  False  *36,* e  se il timer MainClass_C1_timer_T3 non è attivo *37,* e  se la variabile MainClass_C1_variabile_V8 è  diverso da avviox *36,* e  se il timer MainClass_C1_timer_T8 è attivo, *71,*Decrementa il contatore MainClass_C1_contatore_Co1
    // ,altrimenti  *71,*Decrementa il contatore MainClass_C1_contatore_Co1
    bool res_OrLogicOP_3 = false;
    bool res_AndLogicOP_4 = true;
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (Counter_GetValore(L_P1__GetMainc31(my_id)) == 13403u));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_5);
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! Timer_Disattivo(L_P1__GetMainc27(my_id)));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_6);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_AndLogicOP_4);
    bool res_AndLogicOP_7 = true;
    bool res_AndLogicOP_8 = true;
    bool res_AndLogicOP_9 = true;
    res_AndLogicOP_9 = (res_AndLogicOP_9 && (L_P1__GetInMainc6(my_id) == false));
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! Timer_Attivo(L_P1__GetMainc27(my_id)));
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_NotLogicOP_10);
    
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_AndLogicOP_9);
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (L_P1__GetMainc21(my_id) == avviox));
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_11);
    
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_AndLogicOP_8);
    res_AndLogicOP_7 = (res_AndLogicOP_7 && Timer_Attivo(L_P1__GetMainc30(my_id)));
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_AndLogicOP_7);
    
    if(res_OrLogicOP_3){
    
    Counter_Decr(L_P1__GetMainc31(my_id));
    }else{
    
    Counter_Decr(L_P1__GetMainc31(my_id));
    }
    //  se il controllo ConsDef è uguale a FALSE  *37,* e  se la variabile MainClass_C1_variabile_V3 è  uguale a c270x *36,* o  se il timer MainClass_C1_timer_T3 è scaduto,  *67,* Assegna alla variabile MainClass_C1_variabile_V3 il valore c270x
    bool res_OrLogicOP_12 = false;
    bool res_AndLogicOP_13 = true;
    res_AndLogicOP_13 = (res_AndLogicOP_13 && (L_P1__GetInConsd(my_id) == false));
    res_AndLogicOP_13 = (res_AndLogicOP_13 && (L_P1__GetMainc19(my_id) == c270x));
    
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_AndLogicOP_13);
    res_OrLogicOP_12 = (res_OrLogicOP_12 || Timer_Scaduto(L_P1__GetMainc27(my_id)));
    
    if(res_OrLogicOP_12){
    
    L_P1__SetMainc19(my_id,c270x);
    }
    //  *67,*
    //   
    //  se il controllo ConsDef è uguale a FALSE  *34,* o  se il parametro MainClass_C1_parametro_P4 non è  uguale a AC *37,* e  se la variabile MainClass_C1_variabile_V8 è  uguale a avviox, *66,* Assegna al comando MainClass_C1_comando_C10 il valore  True 
    // ,altrimenti  *66,* Assegna al comando MainClass_C1_comando_C8 il valore c270x
    bool res_OrLogicOP_14 = false;
    res_OrLogicOP_14 = (res_OrLogicOP_14 || (L_P1__GetInConsd(my_id) == false));
    bool res_AndLogicOP_15 = true;
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (L_P1__GetParamMainc7(my_id) == ac));
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_NotLogicOP_16);
    res_AndLogicOP_15 = (res_AndLogicOP_15 && (L_P1__GetMainc21(my_id) == avviox));
    
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_AndLogicOP_15);
    
    if(res_OrLogicOP_14){
    
    L_P1__SetOutMainc(my_id,true);
    }else{
    
    L_P1__SetOutMainc3(my_id,c270x);
    }
}


// Macro di verifica

/*
    CNL corrispondente:
     
    { commento: {63,}  se il ripristino dello stato  non è  diverso da  commento: {56,}  state1  commento: {107,} commento: {37,} e  se la variabile MainClass_C1_variabile_V8 è  uguale a avviox commento: {34,} o  se il parametro MainClass_C1_parametro_P4 è  diverso da AC commento: {38,} e  se il contatore MainClass_C1_contatore_Co1 è  uguale a  commento: {53,} 14 o  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
     commento: {38,}  se il contatore MainClass_C1_contatore_Co1 è  minore di  commento: {55,} 14 e  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} o  se il timer MainClass_C1_timer_T7 è disattivo commento: {37,} e  se la variabile MainClass_C1_variabile_V8 è  uguale a avviox commento: {38,} e  se il contatore MainClass_C1_contatore_Co1 è  uguale a  commento: {53,} 13154, Verifica che   commento: {48,51,}  commento: {,}  il controllo MainClass_C1_controllo_C6 sia  diverso da AC
     commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co1 non sia  uguale a  commento: {53,} 110
     commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} o  che  commento: {35,}  il controllo MainClass_C1_controllo_C7 non sia  uguale a  True 
    
    
     } Verifica che   commento: {47,}  commento: {34,}  il parametro MainClass_C1_parametro_P4 non sia  diverso da AC
    
    
    }
*/
bool L_P1__Macro3(instance_id_t const my_id )
{
bool res_AndLogicOP_0 = true;
    
    //  *63,*  se il ripristino dello stato  non è  diverso da  *56,*  state1  *107,* *37,* e  se la variabile MainClass_C1_variabile_V8 è  uguale a avviox *34,* o  se il parametro MainClass_C1_parametro_P4 è  diverso da AC *38,* e  se il contatore MainClass_C1_contatore_Co1 è  uguale a  *53,* 14 o  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
    //   *38,*  se il contatore MainClass_C1_contatore_Co1 è  minore di  *55,* 14 e  se il controllo ConsDef  è  uguale a FALSE  *36,* o  se il timer MainClass_C1_timer_T7 è disattivo *37,* e  se la variabile MainClass_C1_variabile_V8 è  uguale a avviox *38,* e  se il contatore MainClass_C1_contatore_Co1 è  uguale a  *53,* 13154, Verifica che   *48,51,*  *,*  il controllo MainClass_C1_controllo_C6 sia  diverso da AC
    //   *104,* e  che  *,*  il contatore MainClass_C1_contatore_Co1 non sia  uguale a  *53,* 110
    //   *104,* e  che   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* e  che   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* o  che  *35,*  il controllo MainClass_C1_controllo_C7 non sia  uguale a  True 
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_AndLogicOP_4 = true;
    bool res_NotLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetStato1(my_id) == C1_St_state));
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! res_NotLogicOP_6);
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_5);
    res_AndLogicOP_4 = (res_AndLogicOP_4 && (L_P1__GetMainc21(my_id) == avviox));
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_AndLogicOP_4);
    bool res_AndLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetParamMainc7(my_id) == ac));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_8);
    res_AndLogicOP_7 = (res_AndLogicOP_7 && (Counter_GetValore(L_P1__GetMainc31(my_id)) == 14u));
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_AndLogicOP_7);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    res_OrLogicOP_2 = (res_OrLogicOP_2 || (L_P1__GetInConsd(my_id) == false));
    
    if(res_OrLogicOP_2){
    bool res_ImpliesLogicOp_9 = true;
    bool res_OrLogicOP_10 = false;
    bool res_AndLogicOP_11 = true;
    res_AndLogicOP_11 = (res_AndLogicOP_11 && (Counter_GetValore(L_P1__GetMainc31(my_id)) < 14u));
    res_AndLogicOP_11 = (res_AndLogicOP_11 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_AndLogicOP_11);
    bool res_AndLogicOP_12 = true;
    bool res_AndLogicOP_13 = true;
    res_AndLogicOP_13 = (res_AndLogicOP_13 && Timer_Disattivo(L_P1__GetMainc29(my_id)));
    res_AndLogicOP_13 = (res_AndLogicOP_13 && (L_P1__GetMainc21(my_id) == avviox));
    
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_AndLogicOP_13);
    res_AndLogicOP_12 = (res_AndLogicOP_12 && (Counter_GetValore(L_P1__GetMainc31(my_id)) == 13154u));
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_AndLogicOP_12);
    
    if(res_OrLogicOP_10){
    bool res_OrLogicOP_14 = false;
    bool res_AndLogicOP_15 = true;
    bool res_AndLogicOP_16 = true;
    bool res_AndLogicOP_17 = true;
    bool res_NotLogicOP_18 = true;
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! (L_P1__GetInMainc5(my_id) == ac));
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_NotLogicOP_18);
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (Counter_GetValore(L_P1__GetMainc31(my_id)) == 110u));
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_NotLogicOP_19);
    
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_AndLogicOP_17);
    res_AndLogicOP_16 = (res_AndLogicOP_16 && (L_P1__GetInConsd(my_id) == false));
    
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_AndLogicOP_16);
    res_AndLogicOP_15 = (res_AndLogicOP_15 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_AndLogicOP_15);
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! (L_P1__GetInMainc6(my_id) == true));
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_NotLogicOP_20);
    
    res_ImpliesLogicOp_9 = (res_ImpliesLogicOp_9 && res_OrLogicOP_14);
    }
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_ImpliesLogicOp_9);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *47,*  *34,*  il parametro MainClass_C1_parametro_P4 non sia  diverso da AC
    bool res_NotLogicOP_21 = true;
    bool res_NotLogicOP_22 = true;
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! (L_P1__GetParamMainc7(my_id) == ac));
    res_NotLogicOP_21 = (res_NotLogicOP_21 && ! res_NotLogicOP_22);
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_NotLogicOP_21);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
    
    { commento: {61,} commento: {35,}  se il controllo MainClass_C1_controllo_C7 non è  diverso da  True , Tutte le seguenti { 
     commento: {61,} commento: {35,}  se il controllo MainClass_C1_controllo_C7 non è  diverso da  True  commento: {38,} e  se il contatore MainClass_C1_contatore_Co1 non è  maggiore di  commento: {54,} 11 commento: {35,} o  se il controllo MainClass_C1_controllo_C7 è  uguale a  True  e  se l'argomento argomento_ave8 è  diverso da  False  commento: {39,} , Tutte le seguenti { 
      se il ripristino dello stato  è  uguale a  commento: {53,}  state1  commento: {107,} commento: {37,} e  se la variabile MainClass_C1_variabile_V9 non è  maggiore di  commento: {54,} 5 commento: {34,} e  se il parametro MainClass_C1_parametro_P4 non è  diverso da AC, Verifica che   commento: {47,48,49,50,52,}  commento: {34,}  il parametro MainClass_C1_parametro_P4 sia  diverso da AC
     commento: {104,} e  che   l'argomento argomento_ave9 non  sia  diverso da  False  commento: {,} 
     commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C7 sia  diverso da  True 
     commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V3 sia  diverso da c270x
     commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T7 non sia disattivo
     commento: {104,} o  che  commento: {36,}  il timer MainClass_C1_timer_T7 sia scaduto
    
    
     } Verifica che   commento: {47,48,52,}  commento: {34,}  il parametro MainClass_C1_parametro_P4 non sia  uguale a AC
     commento: {104,} e  che   l'argomento argomento_ave9 sia  diverso da  True  commento: {,} 
     commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C6 sia  diverso da AC
    
    
     } Verifica che   commento: {47,48,49,50,}  commento: {34,}  il parametro MainClass_C1_parametro_P4 non sia  diverso da AC
     commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V9 non sia  maggiore di  commento: {54,} 7
     commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T8 non sia scaduto
     commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C7 non sia  diverso da  False 
     commento: {104,} e  che  commento: {37,}  la variabile MainClass_C1_variabile_V10 non sia  diverso da  commento: {56,} 5
    
    
    }
*/
bool L_P1__Macro4(instance_id_t const my_id , C1_Enumerat4 argom5, C1_Enumerat4 argom6, C1_Enumerat1 argom7, bool argom8, bool argom9)
{
bool res_AndLogicOP_0 = true;
    
    //  *61,* *35,*  se il controllo MainClass_C1_controllo_C7 non è  diverso da  True , Tutte le seguenti { 
    //   *61,* *35,*  se il controllo MainClass_C1_controllo_C7 non è  diverso da  True  *38,* e  se il contatore MainClass_C1_contatore_Co1 non è  maggiore di  *54,* 11 *35,* o  se il controllo MainClass_C1_controllo_C7 è  uguale a  True  e  se l'argomento argomento_ave8 è  diverso da  False  *39,* , Tutte le seguenti { 
    //    se il ripristino dello stato  è  uguale a  *53,*  state1  *107,* *37,* e  se la variabile MainClass_C1_variabile_V9 non è  maggiore di  *54,* 5 *34,* e  se il parametro MainClass_C1_parametro_P4 non è  diverso da AC, Verifica che   *47,48,49,50,52,*  *34,*  il parametro MainClass_C1_parametro_P4 sia  diverso da AC
    //   *104,* e  che   l'argomento argomento_ave9 non  sia  diverso da  False  *,* 
    //   *104,* e  che  *,*  il controllo MainClass_C1_controllo_C7 sia  diverso da  True 
    //   *104,* o  che  *,*  la variabile MainClass_C1_variabile_V3 sia  diverso da c270x
    //   *104,* e  che  *,*  il timer MainClass_C1_timer_T7 non sia disattivo
    //   *104,* o  che  *36,*  il timer MainClass_C1_timer_T7 sia scaduto
    //   } Verifica che   *47,48,52,*  *34,*  il parametro MainClass_C1_parametro_P4 non sia  uguale a AC
    //   *104,* e  che   l'argomento argomento_ave9 sia  diverso da  True  *,* 
    //   *104,* e  che  *,*  il controllo MainClass_C1_controllo_C6 sia  diverso da AC
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_NotLogicOP_2 = true;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__GetInMainc6(my_id) == true));
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! res_NotLogicOP_3);
    if(res_NotLogicOP_2){
    bool res_AndLogicOP_4 = true;
    bool res_ImpliesLogicOp_5 = true;
    bool res_OrLogicOP_6 = false;
    bool res_AndLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetInMainc6(my_id) == true));
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! res_NotLogicOP_9);
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_8);
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (Counter_GetValore(L_P1__GetMainc31(my_id)) > 11u));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_10);
    
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_AndLogicOP_7);
    bool res_AndLogicOP_11 = true;
    res_AndLogicOP_11 = (res_AndLogicOP_11 && (L_P1__GetInMainc6(my_id) == true));
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (argom8 == false));
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_NotLogicOP_12);
    
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_AndLogicOP_11);
    
    if(res_OrLogicOP_6){
    bool res_ImpliesLogicOp_13 = true;
    bool res_AndLogicOP_14 = true;
    bool res_AndLogicOP_15 = true;
    res_AndLogicOP_15 = (res_AndLogicOP_15 && (L_P1__GetStato1(my_id) == C1_St_state));
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (L_P1__GetMainc22(my_id) > 5u));
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_NotLogicOP_16);
    
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_AndLogicOP_15);
    bool res_NotLogicOP_17 = true;
    bool res_NotLogicOP_18 = true;
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! (L_P1__GetParamMainc7(my_id) == ac));
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! res_NotLogicOP_18);
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_NotLogicOP_17);
    
    if(res_AndLogicOP_14){
    bool res_OrLogicOP_19 = false;
    bool res_OrLogicOP_20 = false;
    bool res_AndLogicOP_21 = true;
    bool res_AndLogicOP_22 = true;
    bool res_NotLogicOP_23 = true;
    res_NotLogicOP_23 = (res_NotLogicOP_23 && ! (L_P1__GetParamMainc7(my_id) == ac));
    res_AndLogicOP_22 = (res_AndLogicOP_22 && res_NotLogicOP_23);
    bool res_NotLogicOP_24 = true;
    bool res_NotLogicOP_25 = true;
    res_NotLogicOP_25 = (res_NotLogicOP_25 && ! (argom9 == false));
    res_NotLogicOP_24 = (res_NotLogicOP_24 && ! res_NotLogicOP_25);
    res_AndLogicOP_22 = (res_AndLogicOP_22 && res_NotLogicOP_24);
    
    res_AndLogicOP_21 = (res_AndLogicOP_21 && res_AndLogicOP_22);
    bool res_NotLogicOP_26 = true;
    res_NotLogicOP_26 = (res_NotLogicOP_26 && ! (L_P1__GetInMainc6(my_id) == true));
    res_AndLogicOP_21 = (res_AndLogicOP_21 && res_NotLogicOP_26);
    
    res_OrLogicOP_20 = (res_OrLogicOP_20 || res_AndLogicOP_21);
    bool res_AndLogicOP_27 = true;
    bool res_NotLogicOP_28 = true;
    res_NotLogicOP_28 = (res_NotLogicOP_28 && ! (L_P1__GetMainc19(my_id) == c270x));
    res_AndLogicOP_27 = (res_AndLogicOP_27 && res_NotLogicOP_28);
    bool res_NotLogicOP_29 = true;
    res_NotLogicOP_29 = (res_NotLogicOP_29 && ! Timer_Disattivo(L_P1__GetMainc29(my_id)));
    res_AndLogicOP_27 = (res_AndLogicOP_27 && res_NotLogicOP_29);
    
    res_OrLogicOP_20 = (res_OrLogicOP_20 || res_AndLogicOP_27);
    
    res_OrLogicOP_19 = (res_OrLogicOP_19 || res_OrLogicOP_20);
    res_OrLogicOP_19 = (res_OrLogicOP_19 || Timer_Scaduto(L_P1__GetMainc29(my_id)));
    
    res_ImpliesLogicOp_13 = (res_ImpliesLogicOp_13 && res_OrLogicOP_19);
    }
    res_ImpliesLogicOp_5 = (res_ImpliesLogicOp_5 && res_ImpliesLogicOp_13);
    }
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_ImpliesLogicOp_5);
    bool res_AndLogicOP_30 = true;
    bool res_AndLogicOP_31 = true;
    bool res_NotLogicOP_32 = true;
    res_NotLogicOP_32 = (res_NotLogicOP_32 && ! (L_P1__GetParamMainc7(my_id) == ac));
    res_AndLogicOP_31 = (res_AndLogicOP_31 && res_NotLogicOP_32);
    bool res_NotLogicOP_33 = true;
    res_NotLogicOP_33 = (res_NotLogicOP_33 && ! (argom9 == true));
    res_AndLogicOP_31 = (res_AndLogicOP_31 && res_NotLogicOP_33);
    
    res_AndLogicOP_30 = (res_AndLogicOP_30 && res_AndLogicOP_31);
    bool res_NotLogicOP_34 = true;
    res_NotLogicOP_34 = (res_NotLogicOP_34 && ! (L_P1__GetInMainc5(my_id) == ac));
    res_AndLogicOP_30 = (res_AndLogicOP_30 && res_NotLogicOP_34);
    
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_AndLogicOP_30);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_AndLogicOP_4);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *47,48,49,50,*  *34,*  il parametro MainClass_C1_parametro_P4 non sia  diverso da AC
    //   *104,* e  che  *,*  la variabile MainClass_C1_variabile_V9 non sia  maggiore di  *54,* 7
    //   *104,* e  che  *,*  il timer MainClass_C1_timer_T8 non sia scaduto
    //   *104,* o  che  *,*  il controllo MainClass_C1_controllo_C7 non sia  diverso da  False 
    //   *104,* e  che  *37,*  la variabile MainClass_C1_variabile_V10 non sia  diverso da  *56,* 5
    bool res_OrLogicOP_35 = false;
    bool res_AndLogicOP_36 = true;
    bool res_AndLogicOP_37 = true;
    bool res_NotLogicOP_38 = true;
    bool res_NotLogicOP_39 = true;
    res_NotLogicOP_39 = (res_NotLogicOP_39 && ! (L_P1__GetParamMainc7(my_id) == ac));
    res_NotLogicOP_38 = (res_NotLogicOP_38 && ! res_NotLogicOP_39);
    res_AndLogicOP_37 = (res_AndLogicOP_37 && res_NotLogicOP_38);
    bool res_NotLogicOP_40 = true;
    res_NotLogicOP_40 = (res_NotLogicOP_40 && ! (L_P1__GetMainc22(my_id) > 7u));
    res_AndLogicOP_37 = (res_AndLogicOP_37 && res_NotLogicOP_40);
    
    res_AndLogicOP_36 = (res_AndLogicOP_36 && res_AndLogicOP_37);
    bool res_NotLogicOP_41 = true;
    res_NotLogicOP_41 = (res_NotLogicOP_41 && ! Timer_Scaduto(L_P1__GetMainc30(my_id)));
    res_AndLogicOP_36 = (res_AndLogicOP_36 && res_NotLogicOP_41);
    
    res_OrLogicOP_35 = (res_OrLogicOP_35 || res_AndLogicOP_36);
    bool res_AndLogicOP_42 = true;
    bool res_NotLogicOP_43 = true;
    bool res_NotLogicOP_44 = true;
    res_NotLogicOP_44 = (res_NotLogicOP_44 && ! (L_P1__GetInMainc6(my_id) == false));
    res_NotLogicOP_43 = (res_NotLogicOP_43 && ! res_NotLogicOP_44);
    res_AndLogicOP_42 = (res_AndLogicOP_42 && res_NotLogicOP_43);
    bool res_NotLogicOP_45 = true;
    bool res_NotLogicOP_46 = true;
    res_NotLogicOP_46 = (res_NotLogicOP_46 && ! (L_P1__GetMainc18(my_id) == 5u));
    res_NotLogicOP_45 = (res_NotLogicOP_45 && ! res_NotLogicOP_46);
    res_AndLogicOP_42 = (res_AndLogicOP_42 && res_NotLogicOP_45);
    
    res_OrLogicOP_35 = (res_OrLogicOP_35 || res_AndLogicOP_42);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_35);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
     
    { commento: {62,} commento: {34,}  se il parametro MainClass_C1_parametro_P4 non è  diverso da AC commento: {38,} o  se il contatore MainClass_C1_contatore_Co1 è  maggiore di  commento: {54,} 15 commento: {37,} e  se la variabile MainClass_C1_variabile_V3 non è  diverso da c270x e  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} o  se la variabile MainClass_C1_variabile_V3 non è  diverso da c270x commento: {34,} o  se il parametro MainClass_C1_parametro_P4 non è  uguale a AC, Almeno una delle seguenti { 
     commento: {62,} commento: {34,}  se lo stato  è  diverso da  commento: {56,}  state1  commento: {106,} commento: {38,} e  se il contatore MainClass_C1_contatore_Co1 è  diverso da  commento: {56,} 11 e  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} e  se la variabile MainClass_C1_variabile_V5 non è  uguale a  True  commento: {35,} e  se il controllo MainClass_C1_controllo_C7 non è  diverso da  False , Almeno una delle seguenti { 
     commento: {63,} commento: {36,}  se il timer MainClass_C1_timer_T4 non è disattivo commento: {36,} o  se il timer MainClass_C1_timer_T3 è scaduto commento: {34,} e  se il parametro MainClass_C1_parametro_P4 è  diverso da AC commento: {35,} e  se il controllo MainClass_C1_controllo_C6 non è  diverso da AC commento: {37,} e  se la variabile MainClass_C1_variabile_V3 è  uguale a c270x e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
     commento: {61,} commento: {38,}  se il contatore MainClass_C1_contatore_Co1 è  uguale a  commento: {53,} 14 o  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} o  se il parametro MainClass_C1_parametro_P4 non è  uguale a AC o  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro MainClass_C1_parametro_P4 non è  uguale a AC commento: {38,} o  se il contatore MainClass_C1_contatore_Co1 è  diverso da  commento: {56,} 123, Tutte le seguenti { 
     commento: {62,} commento: {36,}  se il timer MainClass_C1_timer_T7 è attivo commento: {35,} o  se il controllo MainClass_C1_controllo_C6 è  diverso da AC commento: {35,} e  se il controllo MainClass_C1_controllo_C7 è  diverso da  False  commento: {35,} o  se il controllo MainClass_C1_controllo_C7 è  diverso da  False  commento: {38,} o  se il contatore MainClass_C1_contatore_Co1 è  diverso da  commento: {56,} 12215 commento: {38,} e  se il contatore MainClass_C1_contatore_Co1 non è  minore di  commento: {55,} 114, Almeno una delle seguenti { 
      se il controllo ConsDef  è  uguale a FALSE  commento: {35,} o  se il controllo MainClass_C1_controllo_C7 non è  uguale a  False  commento: {38,} e  se il contatore MainClass_C1_contatore_Co1 è  minore di  commento: {55,} 1103 commento: {36,} e  se il timer MainClass_C1_timer_T7 è scaduto commento: {36,} e  se il timer MainClass_C1_timer_T7 non è disattivo, Verifica che   commento: {47,48,49,}  commento: {34,}  il parametro MainClass_C1_parametro_P4 non sia  uguale a AC
     commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P4 non sia  uguale a AC
     commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T7 non sia attivo
    
    
     } Verifica che   commento: {47,48,50,51,}  commento: {,}  la variabile MainClass_C1_variabile_V3 non sia  uguale a c270x
     commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P4 non sia  uguale a AC
     commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co1 sia  minore di  commento: {55,} 13215
     commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C6 non sia  uguale a AC
     commento: {104,} o  che  commento: {38,}  il contatore MainClass_C1_contatore_Co1 non sia  maggiore di  commento: {54,} 12
    
    
     } Verifica che   commento: {47,}  commento: {34,}  il parametro MainClass_C1_parametro_P4 sia  uguale a AC
    
    
     } Verifica che   commento: {47,48,51,}   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P4 non sia  diverso da AC
     commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C7 sia  uguale a  True 
     commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co1 sia  uguale a  commento: {53,} 1
    
    
     } Verifica che   commento: {50,}  commento: {,}  la variabile MainClass_C1_variabile_V3 non sia  uguale a c270x
     commento: {104,} o  che  commento: {37,}  la variabile MainClass_C1_variabile_V8 sia  uguale a avviox
    
    
     } Verifica che   commento: {47,48,49,}  commento: {,}  il timer MainClass_C1_timer_T7 sia attivo
     commento: {104,} e  che  commento: {36,}  il timer MainClass_C1_timer_T7 sia disattivo
     commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P4 non sia  diverso da AC
     commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
    
    
    }
*/
bool L_P1__Macro5(instance_id_t const my_id )
{
bool res_AndLogicOP_0 = true;
    
    //  *62,* *34,*  se il parametro MainClass_C1_parametro_P4 non è  diverso da AC *38,* o  se il contatore MainClass_C1_contatore_Co1 è  maggiore di  *54,* 15 *37,* e  se la variabile MainClass_C1_variabile_V3 non è  diverso da c270x e  se il controllo ConsDef  è  uguale a FALSE  *37,* o  se la variabile MainClass_C1_variabile_V3 non è  diverso da c270x *34,* o  se il parametro MainClass_C1_parametro_P4 non è  uguale a AC, Almeno una delle seguenti { 
    //   *62,* *34,*  se lo stato  è  diverso da  *56,*  state1  *106,* *38,* e  se il contatore MainClass_C1_contatore_Co1 è  diverso da  *56,* 11 e  se il controllo ConsDef  è  uguale a FALSE  *37,* e  se la variabile MainClass_C1_variabile_V5 non è  uguale a  True  *35,* e  se il controllo MainClass_C1_controllo_C7 non è  diverso da  False , Almeno una delle seguenti { 
    //   *63,* *36,*  se il timer MainClass_C1_timer_T4 non è disattivo *36,* o  se il timer MainClass_C1_timer_T3 è scaduto *34,* e  se il parametro MainClass_C1_parametro_P4 è  diverso da AC *35,* e  se il controllo MainClass_C1_controllo_C6 non è  diverso da AC *37,* e  se la variabile MainClass_C1_variabile_V3 è  uguale a c270x e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
    //   *61,* *38,*  se il contatore MainClass_C1_contatore_Co1 è  uguale a  *53,* 14 o  se il controllo ConsDef  è  uguale a FALSE  *34,* o  se il parametro MainClass_C1_parametro_P4 non è  uguale a AC o  se il controllo ConsDef  è  uguale a FALSE  *34,* e  se il parametro MainClass_C1_parametro_P4 non è  uguale a AC *38,* o  se il contatore MainClass_C1_contatore_Co1 è  diverso da  *56,* 123, Tutte le seguenti { 
    //   *62,* *36,*  se il timer MainClass_C1_timer_T7 è attivo *35,* o  se il controllo MainClass_C1_controllo_C6 è  diverso da AC *35,* e  se il controllo MainClass_C1_controllo_C7 è  diverso da  False  *35,* o  se il controllo MainClass_C1_controllo_C7 è  diverso da  False  *38,* o  se il contatore MainClass_C1_contatore_Co1 è  diverso da  *56,* 12215 *38,* e  se il contatore MainClass_C1_contatore_Co1 non è  minore di  *55,* 114, Almeno una delle seguenti { 
    //    se il controllo ConsDef  è  uguale a FALSE  *35,* o  se il controllo MainClass_C1_controllo_C7 non è  uguale a  False  *38,* e  se il contatore MainClass_C1_contatore_Co1 è  minore di  *55,* 1103 *36,* e  se il timer MainClass_C1_timer_T7 è scaduto *36,* e  se il timer MainClass_C1_timer_T7 non è disattivo, Verifica che   *47,48,49,*  *34,*  il parametro MainClass_C1_parametro_P4 non sia  uguale a AC
    //   *104,* e  che  *34,*  il parametro MainClass_C1_parametro_P4 non sia  uguale a AC
    //   *104,* o  che   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* o  che  *,*  il timer MainClass_C1_timer_T7 non sia attivo
    //   } Verifica che   *47,48,50,51,*  *,*  la variabile MainClass_C1_variabile_V3 non sia  uguale a c270x
    //   *104,* o  che  *34,*  il parametro MainClass_C1_parametro_P4 non sia  uguale a AC
    //   *104,* e  che  *,*  il contatore MainClass_C1_contatore_Co1 sia  minore di  *55,* 13215
    //   *104,* e  che  *,*  il controllo MainClass_C1_controllo_C6 non sia  uguale a AC
    //   *104,* o  che  *38,*  il contatore MainClass_C1_contatore_Co1 non sia  maggiore di  *54,* 12
    //   } Verifica che   *47,*  *34,*  il parametro MainClass_C1_parametro_P4 sia  uguale a AC
    //   } Verifica che   *47,48,51,*   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* e  che  *34,*  il parametro MainClass_C1_parametro_P4 non sia  diverso da AC
    //   *104,* e  che  *,*  il controllo MainClass_C1_controllo_C7 sia  uguale a  True 
    //   *104,* e  che  *,*  il contatore MainClass_C1_contatore_Co1 sia  uguale a  *53,* 1
    //   } Verifica che   *50,*  *,*  la variabile MainClass_C1_variabile_V3 non sia  uguale a c270x
    //   *104,* o  che  *37,*  la variabile MainClass_C1_variabile_V8 sia  uguale a avviox
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_OrLogicOP_4 = false;
    bool res_NotLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetParamMainc7(my_id) == ac));
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! res_NotLogicOP_6);
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_NotLogicOP_5);
    bool res_AndLogicOP_7 = true;
    bool res_AndLogicOP_8 = true;
    res_AndLogicOP_8 = (res_AndLogicOP_8 && (Counter_GetValore(L_P1__GetMainc31(my_id)) > 15u));
    bool res_NotLogicOP_9 = true;
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__GetMainc19(my_id) == c270x));
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! res_NotLogicOP_10);
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_9);
    
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_AndLogicOP_8);
    res_AndLogicOP_7 = (res_AndLogicOP_7 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_AndLogicOP_7);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_OrLogicOP_4);
    bool res_NotLogicOP_11 = true;
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (L_P1__GetMainc19(my_id) == c270x));
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! res_NotLogicOP_12);
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_NotLogicOP_11);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (L_P1__GetParamMainc7(my_id) == ac));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_13);
    
    if(res_OrLogicOP_2){
    bool res_OrLogicOP_14 = false;
    bool res_ImpliesLogicOp_15 = true;
    bool res_AndLogicOP_16 = true;
    bool res_AndLogicOP_17 = true;
    bool res_AndLogicOP_18 = true;
    bool res_AndLogicOP_19 = true;
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! (L_P1_C1_GetState(my_id) == C1_St_state));
    res_AndLogicOP_19 = (res_AndLogicOP_19 && res_NotLogicOP_20);
    bool res_NotLogicOP_21 = true;
    res_NotLogicOP_21 = (res_NotLogicOP_21 && ! (Counter_GetValore(L_P1__GetMainc31(my_id)) == 11u));
    res_AndLogicOP_19 = (res_AndLogicOP_19 && res_NotLogicOP_21);
    
    res_AndLogicOP_18 = (res_AndLogicOP_18 && res_AndLogicOP_19);
    res_AndLogicOP_18 = (res_AndLogicOP_18 && (L_P1__GetInConsd(my_id) == false));
    
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_AndLogicOP_18);
    bool res_NotLogicOP_22 = true;
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! (L_P1__GetMainc20(my_id) == true));
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_NotLogicOP_22);
    
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_AndLogicOP_17);
    bool res_NotLogicOP_23 = true;
    bool res_NotLogicOP_24 = true;
    res_NotLogicOP_24 = (res_NotLogicOP_24 && ! (L_P1__GetInMainc6(my_id) == false));
    res_NotLogicOP_23 = (res_NotLogicOP_23 && ! res_NotLogicOP_24);
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_NotLogicOP_23);
    
    if(res_AndLogicOP_16){
    bool res_OrLogicOP_25 = false;
    bool res_ImpliesLogicOp_26 = true;
    bool res_OrLogicOP_27 = false;
    bool res_NotLogicOP_28 = true;
    res_NotLogicOP_28 = (res_NotLogicOP_28 && ! Timer_Disattivo(L_P1__GetMainc28(my_id)));
    res_OrLogicOP_27 = (res_OrLogicOP_27 || res_NotLogicOP_28);
    bool res_AndLogicOP_29 = true;
    bool res_AndLogicOP_30 = true;
    bool res_AndLogicOP_31 = true;
    bool res_AndLogicOP_32 = true;
    res_AndLogicOP_32 = (res_AndLogicOP_32 && Timer_Scaduto(L_P1__GetMainc27(my_id)));
    bool res_NotLogicOP_33 = true;
    res_NotLogicOP_33 = (res_NotLogicOP_33 && ! (L_P1__GetParamMainc7(my_id) == ac));
    res_AndLogicOP_32 = (res_AndLogicOP_32 && res_NotLogicOP_33);
    
    res_AndLogicOP_31 = (res_AndLogicOP_31 && res_AndLogicOP_32);
    bool res_NotLogicOP_34 = true;
    bool res_NotLogicOP_35 = true;
    res_NotLogicOP_35 = (res_NotLogicOP_35 && ! (L_P1__GetInMainc5(my_id) == ac));
    res_NotLogicOP_34 = (res_NotLogicOP_34 && ! res_NotLogicOP_35);
    res_AndLogicOP_31 = (res_AndLogicOP_31 && res_NotLogicOP_34);
    
    res_AndLogicOP_30 = (res_AndLogicOP_30 && res_AndLogicOP_31);
    res_AndLogicOP_30 = (res_AndLogicOP_30 && (L_P1__GetMainc19(my_id) == c270x));
    
    res_AndLogicOP_29 = (res_AndLogicOP_29 && res_AndLogicOP_30);
    res_AndLogicOP_29 = (res_AndLogicOP_29 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_27 = (res_OrLogicOP_27 || res_AndLogicOP_29);
    
    if(res_OrLogicOP_27){
    bool res_XorLogicOP_36 = true;
    int xorIndex_res_XorLogicOP_36 = 0;
    bool res_ImpliesLogicOp_37 = true;
    bool res_OrLogicOP_38 = false;
    bool res_OrLogicOP_39 = false;
    bool res_OrLogicOP_40 = false;
    bool res_OrLogicOP_41 = false;
    res_OrLogicOP_41 = (res_OrLogicOP_41 || (Counter_GetValore(L_P1__GetMainc31(my_id)) == 14u));
    res_OrLogicOP_41 = (res_OrLogicOP_41 || (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_40 = (res_OrLogicOP_40 || res_OrLogicOP_41);
    bool res_NotLogicOP_42 = true;
    res_NotLogicOP_42 = (res_NotLogicOP_42 && ! (L_P1__GetParamMainc7(my_id) == ac));
    res_OrLogicOP_40 = (res_OrLogicOP_40 || res_NotLogicOP_42);
    
    res_OrLogicOP_39 = (res_OrLogicOP_39 || res_OrLogicOP_40);
    bool res_AndLogicOP_43 = true;
    res_AndLogicOP_43 = (res_AndLogicOP_43 && (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_44 = true;
    res_NotLogicOP_44 = (res_NotLogicOP_44 && ! (L_P1__GetParamMainc7(my_id) == ac));
    res_AndLogicOP_43 = (res_AndLogicOP_43 && res_NotLogicOP_44);
    
    res_OrLogicOP_39 = (res_OrLogicOP_39 || res_AndLogicOP_43);
    
    res_OrLogicOP_38 = (res_OrLogicOP_38 || res_OrLogicOP_39);
    bool res_NotLogicOP_45 = true;
    res_NotLogicOP_45 = (res_NotLogicOP_45 && ! (Counter_GetValore(L_P1__GetMainc31(my_id)) == 123u));
    res_OrLogicOP_38 = (res_OrLogicOP_38 || res_NotLogicOP_45);
    
    if(res_OrLogicOP_38){
    bool res_AndLogicOP_46 = true;
    bool res_ImpliesLogicOp_47 = true;
    bool res_OrLogicOP_48 = false;
    bool res_OrLogicOP_49 = false;
    bool res_OrLogicOP_50 = false;
    res_OrLogicOP_50 = (res_OrLogicOP_50 || Timer_Attivo(L_P1__GetMainc29(my_id)));
    bool res_AndLogicOP_51 = true;
    bool res_NotLogicOP_52 = true;
    res_NotLogicOP_52 = (res_NotLogicOP_52 && ! (L_P1__GetInMainc5(my_id) == ac));
    res_AndLogicOP_51 = (res_AndLogicOP_51 && res_NotLogicOP_52);
    bool res_NotLogicOP_53 = true;
    res_NotLogicOP_53 = (res_NotLogicOP_53 && ! (L_P1__GetInMainc6(my_id) == false));
    res_AndLogicOP_51 = (res_AndLogicOP_51 && res_NotLogicOP_53);
    
    res_OrLogicOP_50 = (res_OrLogicOP_50 || res_AndLogicOP_51);
    
    res_OrLogicOP_49 = (res_OrLogicOP_49 || res_OrLogicOP_50);
    bool res_NotLogicOP_54 = true;
    res_NotLogicOP_54 = (res_NotLogicOP_54 && ! (L_P1__GetInMainc6(my_id) == false));
    res_OrLogicOP_49 = (res_OrLogicOP_49 || res_NotLogicOP_54);
    
    res_OrLogicOP_48 = (res_OrLogicOP_48 || res_OrLogicOP_49);
    bool res_AndLogicOP_55 = true;
    bool res_NotLogicOP_56 = true;
    res_NotLogicOP_56 = (res_NotLogicOP_56 && ! (Counter_GetValore(L_P1__GetMainc31(my_id)) == 12215u));
    res_AndLogicOP_55 = (res_AndLogicOP_55 && res_NotLogicOP_56);
    bool res_NotLogicOP_57 = true;
    res_NotLogicOP_57 = (res_NotLogicOP_57 && ! (Counter_GetValore(L_P1__GetMainc31(my_id)) < 114u));
    res_AndLogicOP_55 = (res_AndLogicOP_55 && res_NotLogicOP_57);
    
    res_OrLogicOP_48 = (res_OrLogicOP_48 || res_AndLogicOP_55);
    
    if(res_OrLogicOP_48){
    bool res_ImpliesLogicOp_58 = true;
    bool res_OrLogicOP_59 = false;
    res_OrLogicOP_59 = (res_OrLogicOP_59 || (L_P1__GetInConsd(my_id) == false));
    bool res_AndLogicOP_60 = true;
    bool res_AndLogicOP_61 = true;
    bool res_AndLogicOP_62 = true;
    bool res_NotLogicOP_63 = true;
    res_NotLogicOP_63 = (res_NotLogicOP_63 && ! (L_P1__GetInMainc6(my_id) == false));
    res_AndLogicOP_62 = (res_AndLogicOP_62 && res_NotLogicOP_63);
    res_AndLogicOP_62 = (res_AndLogicOP_62 && (Counter_GetValore(L_P1__GetMainc31(my_id)) < 1103u));
    
    res_AndLogicOP_61 = (res_AndLogicOP_61 && res_AndLogicOP_62);
    res_AndLogicOP_61 = (res_AndLogicOP_61 && Timer_Scaduto(L_P1__GetMainc29(my_id)));
    
    res_AndLogicOP_60 = (res_AndLogicOP_60 && res_AndLogicOP_61);
    bool res_NotLogicOP_64 = true;
    res_NotLogicOP_64 = (res_NotLogicOP_64 && ! Timer_Disattivo(L_P1__GetMainc29(my_id)));
    res_AndLogicOP_60 = (res_AndLogicOP_60 && res_NotLogicOP_64);
    
    res_OrLogicOP_59 = (res_OrLogicOP_59 || res_AndLogicOP_60);
    
    if(res_OrLogicOP_59){
    bool res_OrLogicOP_65 = false;
    bool res_OrLogicOP_66 = false;
    bool res_AndLogicOP_67 = true;
    bool res_NotLogicOP_68 = true;
    res_NotLogicOP_68 = (res_NotLogicOP_68 && ! (L_P1__GetParamMainc7(my_id) == ac));
    res_AndLogicOP_67 = (res_AndLogicOP_67 && res_NotLogicOP_68);
    bool res_NotLogicOP_69 = true;
    res_NotLogicOP_69 = (res_NotLogicOP_69 && ! (L_P1__GetParamMainc7(my_id) == ac));
    res_AndLogicOP_67 = (res_AndLogicOP_67 && res_NotLogicOP_69);
    
    res_OrLogicOP_66 = (res_OrLogicOP_66 || res_AndLogicOP_67);
    res_OrLogicOP_66 = (res_OrLogicOP_66 || (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_65 = (res_OrLogicOP_65 || res_OrLogicOP_66);
    bool res_NotLogicOP_70 = true;
    res_NotLogicOP_70 = (res_NotLogicOP_70 && ! Timer_Attivo(L_P1__GetMainc29(my_id)));
    res_OrLogicOP_65 = (res_OrLogicOP_65 || res_NotLogicOP_70);
    
    res_ImpliesLogicOp_58 = (res_ImpliesLogicOp_58 && res_OrLogicOP_65);
    }
    res_ImpliesLogicOp_47 = (res_ImpliesLogicOp_47 && res_ImpliesLogicOp_58);
    }
    res_AndLogicOP_46 = (res_AndLogicOP_46 && res_ImpliesLogicOp_47);
    bool res_OrLogicOP_71 = false;
    bool res_OrLogicOP_72 = false;
    bool res_NotLogicOP_73 = true;
    res_NotLogicOP_73 = (res_NotLogicOP_73 && ! (L_P1__GetMainc19(my_id) == c270x));
    res_OrLogicOP_72 = (res_OrLogicOP_72 || res_NotLogicOP_73);
    bool res_AndLogicOP_74 = true;
    bool res_AndLogicOP_75 = true;
    bool res_NotLogicOP_76 = true;
    res_NotLogicOP_76 = (res_NotLogicOP_76 && ! (L_P1__GetParamMainc7(my_id) == ac));
    res_AndLogicOP_75 = (res_AndLogicOP_75 && res_NotLogicOP_76);
    res_AndLogicOP_75 = (res_AndLogicOP_75 && (Counter_GetValore(L_P1__GetMainc31(my_id)) < 13215u));
    
    res_AndLogicOP_74 = (res_AndLogicOP_74 && res_AndLogicOP_75);
    bool res_NotLogicOP_77 = true;
    res_NotLogicOP_77 = (res_NotLogicOP_77 && ! (L_P1__GetInMainc5(my_id) == ac));
    res_AndLogicOP_74 = (res_AndLogicOP_74 && res_NotLogicOP_77);
    
    res_OrLogicOP_72 = (res_OrLogicOP_72 || res_AndLogicOP_74);
    
    res_OrLogicOP_71 = (res_OrLogicOP_71 || res_OrLogicOP_72);
    bool res_NotLogicOP_78 = true;
    res_NotLogicOP_78 = (res_NotLogicOP_78 && ! (Counter_GetValore(L_P1__GetMainc31(my_id)) > 12u));
    res_OrLogicOP_71 = (res_OrLogicOP_71 || res_NotLogicOP_78);
    
    res_AndLogicOP_46 = (res_AndLogicOP_46 && res_OrLogicOP_71);
    
    res_ImpliesLogicOp_37 = (res_ImpliesLogicOp_37 && res_AndLogicOP_46);
    }
    if(res_ImpliesLogicOp_37){
    xorIndex_res_XorLogicOP_36 = (xorIndex_res_XorLogicOP_36 + 1);
    }
    if((L_P1__GetParamMainc7(my_id) == ac)){
    xorIndex_res_XorLogicOP_36 = (xorIndex_res_XorLogicOP_36 + 1);
    }
    
    res_XorLogicOP_36 = (res_XorLogicOP_36 && (xorIndex_res_XorLogicOP_36 == 1));
    res_ImpliesLogicOp_26 = (res_ImpliesLogicOp_26 && res_XorLogicOP_36);
    }
    res_OrLogicOP_25 = (res_OrLogicOP_25 || res_ImpliesLogicOp_26);
    bool res_AndLogicOP_79 = true;
    bool res_AndLogicOP_80 = true;
    bool res_AndLogicOP_81 = true;
    res_AndLogicOP_81 = (res_AndLogicOP_81 && (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_82 = true;
    bool res_NotLogicOP_83 = true;
    res_NotLogicOP_83 = (res_NotLogicOP_83 && ! (L_P1__GetParamMainc7(my_id) == ac));
    res_NotLogicOP_82 = (res_NotLogicOP_82 && ! res_NotLogicOP_83);
    res_AndLogicOP_81 = (res_AndLogicOP_81 && res_NotLogicOP_82);
    
    res_AndLogicOP_80 = (res_AndLogicOP_80 && res_AndLogicOP_81);
    res_AndLogicOP_80 = (res_AndLogicOP_80 && (L_P1__GetInMainc6(my_id) == true));
    
    res_AndLogicOP_79 = (res_AndLogicOP_79 && res_AndLogicOP_80);
    res_AndLogicOP_79 = (res_AndLogicOP_79 && (Counter_GetValore(L_P1__GetMainc31(my_id)) == 1u));
    
    res_OrLogicOP_25 = (res_OrLogicOP_25 || res_AndLogicOP_79);
    
    res_ImpliesLogicOp_15 = (res_ImpliesLogicOp_15 && res_OrLogicOP_25);
    }
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_ImpliesLogicOp_15);
    bool res_OrLogicOP_84 = false;
    bool res_NotLogicOP_85 = true;
    res_NotLogicOP_85 = (res_NotLogicOP_85 && ! (L_P1__GetMainc19(my_id) == c270x));
    res_OrLogicOP_84 = (res_OrLogicOP_84 || res_NotLogicOP_85);
    res_OrLogicOP_84 = (res_OrLogicOP_84 || (L_P1__GetMainc21(my_id) == avviox));
    
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_OrLogicOP_84);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_OrLogicOP_14);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *47,48,49,*  *,*  il timer MainClass_C1_timer_T7 sia attivo
    //   *104,* e  che  *36,*  il timer MainClass_C1_timer_T7 sia disattivo
    //   *104,* e  che  *34,*  il parametro MainClass_C1_parametro_P4 non sia  diverso da AC
    //   *104,* e  che   il controllo ConsDef  sia  uguale a FALSE
    bool res_AndLogicOP_86 = true;
    bool res_AndLogicOP_87 = true;
    bool res_AndLogicOP_88 = true;
    res_AndLogicOP_88 = (res_AndLogicOP_88 && Timer_Attivo(L_P1__GetMainc29(my_id)));
    res_AndLogicOP_88 = (res_AndLogicOP_88 && Timer_Disattivo(L_P1__GetMainc29(my_id)));
    
    res_AndLogicOP_87 = (res_AndLogicOP_87 && res_AndLogicOP_88);
    bool res_NotLogicOP_89 = true;
    bool res_NotLogicOP_90 = true;
    res_NotLogicOP_90 = (res_NotLogicOP_90 && ! (L_P1__GetParamMainc7(my_id) == ac));
    res_NotLogicOP_89 = (res_NotLogicOP_89 && ! res_NotLogicOP_90);
    res_AndLogicOP_87 = (res_AndLogicOP_87 && res_NotLogicOP_89);
    
    res_AndLogicOP_86 = (res_AndLogicOP_86 && res_AndLogicOP_87);
    res_AndLogicOP_86 = (res_AndLogicOP_86 && (L_P1__GetInConsd(my_id) == false));
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_AndLogicOP_86);
    
    
    
    return res_AndLogicOP_0;
}


// Macro valorizzate

/*
    CNL corrispondente:
    
    { commento: {[}  se il controllo ConsDef è uguale a FALSE  commento: {38,} e  se il contatore MainClass_C1_contatore_Co1 è  diverso da  commento: {56,} 152 commento: {35,} e  se il controllo MainClass_C1_controllo_C6 non è  diverso da AC commento: {110,} o  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è attivo e  se la macro  MainClass_C1_macrova_M7 ( con argomento_a9   uguale a c120x  e argomento_a3   uguale a AC )  non  è  uguale a  True  commento: {40,}  o  se la macro  MainClass_C1_macrova_M7 ( con argomento_a9   uguale a AC  e argomento_a3   uguale a AC )  non  è  uguale a  True  commento: {40,}  , assegna alla macro il valore avviox
    
     commento: {46,} assegna alla macro il valore avviox commento: {],}
    }
*/
C1_Enumerat2 L_P1__Macro1(instance_id_t const my_id , C1_Enumerat1 argom, bool argom1, C1_Enumerat1 argom2)
{
C1_Enumerat2 res_macro_val;
    
    //  *[*  se il controllo ConsDef è uguale a FALSE  *38,* e  se il contatore MainClass_C1_contatore_Co1 è  diverso da  *56,* 152 *35,* e  se il controllo MainClass_C1_controllo_C6 non è  diverso da AC *110,* o  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è attivo e  se la macro  MainClass_C1_macrova_M7 ( con argomento_a9   uguale a c120x  e argomento_a3   uguale a AC )  non  è  uguale a  True  *40,*  o  se la macro  MainClass_C1_macrova_M7 ( con argomento_a9   uguale a AC  e argomento_a3   uguale a AC )  non  è  uguale a  True
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_AndLogicOP_2 = true;
    bool res_AndLogicOP_3 = true;
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (Counter_GetValore(L_P1__GetMainc31(my_id)) == 152u));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_4);
    
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_AndLogicOP_3);
    bool res_NotLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetInMainc5(my_id) == ac));
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! res_NotLogicOP_6);
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_5);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_2);
    bool res_AndLogicOP_7 = true;
    res_AndLogicOP_7 = (res_AndLogicOP_7 && Timer_Attivo(L_P1__GetMainc24(my_id)));
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__Macro2(my_id,ac,c120x) == true));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_8);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_7);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__Macro2(my_id,ac,ac) == true));
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_9);
    
    if(res_OrLogicOP_0){
    
    res_macro_val = avviox;
    }
    else{
    res_macro_val = avviox;
    }
    return res_macro_val;
}

/*
    CNL corrispondente:
    
    { commento: {[}
     commento: {46,} assegna alla macro il valore  True  commento: {],}
    }
*/
bool L_P1__Macro2(instance_id_t const my_id , C1_Enumerat3 argom3, C1_Enumerat3 argom4)
{
return true;
}



