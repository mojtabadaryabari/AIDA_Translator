// Codice del modello 'TestCase9', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#include "Logica/ClasseMainClass_C1.h"
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
	    L_P1__SetOutEvent4(my_id, LDS_MANCMD_UNEXPECTED);
    } else {
        L_P1__SetOutEvent4(my_id, LDS_MANCMD_NOOP);
    }
    if (L_P1__GetInEvent1(my_id)) {
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
    L_P1__SetMainc14(my_id, 0);
    L_P1__SetMainc16(my_id, spento);
    L_P1__SetMainc17(my_id, spento);
    L_P1__SetMainc18(my_id, rossogiallo);
    L_P1__SetMainc19(my_id, rossogiallo);
    L_P1__SetMainc20(my_id, 0);
    L_P1__SetMainc21(my_id, 0);
    L_P1__SetMainc22(my_id, spento);
    L_P1__SetMainc23(my_id, spento);
    L_P1__SetMainc24(my_id, false);
    L_P1__SetMainc25(my_id, false);
    L_P1__SetStato1(my_id, C1_St_Stato);
    // init controlli precedenti
    L_P1__SetMainc13(my_id, rossogiallo1);
    // init Timer e Counter
    Timer_AggmInit(L_P1__GetMainc26(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc26_ID);
    Timer_Init(L_P1__GetMainc26(my_id), 120000);
    Timer_AggmInit(L_P1__GetMainc27(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc27_ID);
    Timer_Init(L_P1__GetMainc27(my_id), 120000);
    Timer_AggmInit(L_P1__GetMainc28(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc28_ID);
    Timer_Init(L_P1__GetMainc28(my_id), 23000);
    Timer_AggmInit(L_P1__GetMainc29(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc29_ID);
    Timer_Init(L_P1__GetMainc29(my_id), 23000);
    Timer_AggmInit(L_P1__GetMainc30(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc30_ID);
    Timer_Init(L_P1__GetMainc30(my_id), 11000);
    Timer_AggmInit(L_P1__GetMainc31(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc31_ID);
    Timer_Init(L_P1__GetMainc31(my_id), 545000);
    Counter_AggmInit(L_P1__GetMainc32(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc32_ID);
    Counter_Init(L_P1__GetMainc32(my_id));
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
    L_P1__SetMainc15(my_id, L_P1__GetMainc14(my_id));
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
    Timer_Exec(L_P1__GetMainc26(my_id));
    Timer_Exec(L_P1__GetMainc27(my_id));
    Timer_Exec(L_P1__GetMainc28(my_id));
    Timer_Exec(L_P1__GetMainc29(my_id));
    Timer_Exec(L_P1__GetMainc30(my_id));
    Timer_Exec(L_P1__GetMainc31(my_id));
}

void L_P1_C1_GSetSafe(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C1(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C1(proc_id);
    L_P1__SetOutMainc(my_id, true);
    L_P1__SetOutMainc1(my_id, false);
    L_P1__SetOutMainc2(my_id, rossogiallo1);
    L_P1__SetOutMainc3(my_id, true);
    L_P1__SetOutMainc4(my_id, gialloaverd);
}

void L_P1_C1_GUpdatePrev(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C1(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C1(proc_id);
    L_P1__SetMainc13(my_id, L_P1__GetInMainc12(my_id));
    L_P1__SetMainc15(my_id, L_P1__GetMainc14(my_id));
}

// ********** Definizione macro **********

// Macro di effetto

/*
    CNL corrispondente:
    
    { commento: {38,}  se il contatore MainClass_C1_contatore_Co4 non è  uguale a  commento: {53,} 13120, commento: {68,}Attiva il timer MainClass_C1_timer_T4
    
     ,altrimenti   commento: {67,} Assegna alla variabile MainClass_C1_variabile_V10 il valore  True  commento: {67,}
    
    
    
    }
*/
void L_P1__Macro(instance_id_t const my_id )
{
//  *38,*  se il contatore MainClass_C1_contatore_Co4 non è  uguale a  *53,* 13120, *68,*Attiva il timer MainClass_C1_timer_T4
    // ,altrimenti   *67,* Assegna alla variabile MainClass_C1_variabile_V10 il valore  True
    bool res_NotLogicOP_0 = true;
    res_NotLogicOP_0 = (res_NotLogicOP_0 && ! (Counter_GetValore(L_P1__GetMainc34(my_id)) == 13120u));
    if(res_NotLogicOP_0){
    
    Timer_Attiva(L_P1__GetMainc30(my_id));
    }else{
    
    L_P1__SetMainc24(my_id,true);
    }
}


// Macro di verifica

/*
    CNL corrispondente:
     
    { commento: {62,} commento: {35,}  se il controllo MainClass_C1_controllo_C8 non è  uguale a  False  commento: {36,} e  se il timer MainClass_C1_timer_T4 non è scaduto commento: {35,} o  se il controllo MainClass_C1_controllo_C2 non è  diverso da  True , Almeno una delle seguenti { 
     commento: {63,} commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo commento: {37,} e  se la variabile MainClass_C1_variabile_V7 è  uguale a  True  commento: {34,} e  se il parametro MainClass_C1_parametro_P9 non è  diverso da  False  commento: {34,} o  se il parametro MainClass_C1_parametro_P9 è  uguale a  False  commento: {34,} o  se il parametro MainClass_C1_parametro_P5 non è  diverso da c180, Solo una delle seguenti { 
     commento: {62,} commento: {34,}  se lo stato  non è  uguale a  commento: {53,}  state1  commento: {106,}, Almeno una delle seguenti { 
     commento: {63,} commento: {35,}  se il controllo MainClass_C1_controllo_C9 non è  diverso da c180 commento: {37,} e  se la variabile MainClass_C1_variabile_V7 è  diverso da  False  commento: {36,} e  se il timer MainClass_C1_timer_T4 non è disattivo commento: {35,} e  se il controllo MainClass_C1_controllo_C2 non è  uguale a  True  commento: {34,} e  se il parametro MainClass_C1_parametro_P5 non è  diverso da c180 commento: {37,} e  se la variabile MainClass_C1_variabile_V7 non è  uguale a  True , Solo una delle seguenti { 
     commento: {34,}  se il parametro MainClass_C1_parametro_P5 è  diverso da c180 commento: {35,} e  se il controllo MainClass_C1_controllo_C8 non è  uguale a  True  commento: {37,} o  se la variabile MainClass_C1_variabile_V10 è  uguale a  True  commento: {38,} o  se il contatore MainClass_C1_contatore_Co10 non è  minore di  commento: {55,} 130 commento: {35,} o  se il controllo MainClass_C1_controllo_C8 non è  diverso da  False  commento: {34,} o  se il parametro MainClass_C1_parametro_P1 è  uguale a avviox, Verifica che   commento: {48,49,50,}  commento: {,}  il timer MainClass_C1_timer_T5 sia scaduto
     commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V7 sia  uguale a  False 
    
    
     } Verifica che   commento: {48,}  commento: {,}  il controllo MainClass_C1_controllo_C2 sia  uguale a  True 
    
    
     } Verifica che   commento: {47,48,49,50,}  commento: {34,}  il parametro MainClass_C1_parametro_P9 non sia  diverso da  False 
     commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C2 sia  diverso da  False 
     commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V10 non sia  uguale a  True 
     commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T4 sia disattivo
    
    
     } Verifica che   commento: {47,49,51,}  commento: {,}  il timer MainClass_C1_timer_T5 sia scaduto
     commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P9 non sia  uguale a  True 
     commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co7 sia  uguale a  commento: {53,} 133
    
    
     } Verifica che   commento: {47,48,51,}  commento: {,}  il contatore MainClass_C1_contatore_Co7 sia  maggiore di  commento: {54,} 11
     commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C2 sia  uguale a  True 
     commento: {104,} e  che  commento: {35,}  il controllo MainClass_C1_controllo_C9 non sia  diverso da c180
     commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P5 non sia  diverso da c180
     commento: {104,} e  che  commento: {35,}  il controllo MainClass_C1_controllo_C2 sia  uguale a  True 
    
    
    }
*/
bool L_P1__Macro5(instance_id_t const my_id )
{
bool res_AndLogicOP_0 = true;
    
    //  *62,* *35,*  se il controllo MainClass_C1_controllo_C8 non è  uguale a  False  *36,* e  se il timer MainClass_C1_timer_T4 non è scaduto *35,* o  se il controllo MainClass_C1_controllo_C2 non è  diverso da  True , Almeno una delle seguenti { 
    //   *63,* *110,*  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo *37,* e  se la variabile MainClass_C1_variabile_V7 è  uguale a  True  *34,* e  se il parametro MainClass_C1_parametro_P9 non è  diverso da  False  *34,* o  se il parametro MainClass_C1_parametro_P9 è  uguale a  False  *34,* o  se il parametro MainClass_C1_parametro_P5 non è  diverso da c180, Solo una delle seguenti { 
    //   *62,* *34,*  se lo stato  non è  uguale a  *53,*  state1  *106,*, Almeno una delle seguenti { 
    //   *63,* *35,*  se il controllo MainClass_C1_controllo_C9 non è  diverso da c180 *37,* e  se la variabile MainClass_C1_variabile_V7 è  diverso da  False  *36,* e  se il timer MainClass_C1_timer_T4 non è disattivo *35,* e  se il controllo MainClass_C1_controllo_C2 non è  uguale a  True  *34,* e  se il parametro MainClass_C1_parametro_P5 non è  diverso da c180 *37,* e  se la variabile MainClass_C1_variabile_V7 non è  uguale a  True , Solo una delle seguenti { 
    //   *34,*  se il parametro MainClass_C1_parametro_P5 è  diverso da c180 *35,* e  se il controllo MainClass_C1_controllo_C8 non è  uguale a  True  *37,* o  se la variabile MainClass_C1_variabile_V10 è  uguale a  True  *38,* o  se il contatore MainClass_C1_contatore_Co10 non è  minore di  *55,* 130 *35,* o  se il controllo MainClass_C1_controllo_C8 non è  diverso da  False  *34,* o  se il parametro MainClass_C1_parametro_P1 è  uguale a avviox, Verifica che   *48,49,50,*  *,*  il timer MainClass_C1_timer_T5 sia scaduto
    //   *104,* e  che   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* o  che  *,*  la variabile MainClass_C1_variabile_V7 sia  uguale a  False 
    //   } Verifica che   *48,*  *,*  il controllo MainClass_C1_controllo_C2 sia  uguale a  True 
    //   } Verifica che   *47,48,49,50,*  *34,*  il parametro MainClass_C1_parametro_P9 non sia  diverso da  False 
    //   *104,* e  che  *,*  il controllo MainClass_C1_controllo_C2 sia  diverso da  False 
    //   *104,* o  che  *,*  la variabile MainClass_C1_variabile_V10 non sia  uguale a  True 
    //   *104,* e  che  *,*  il timer MainClass_C1_timer_T4 sia disattivo
    //   } Verifica che   *47,49,51,*  *,*  il timer MainClass_C1_timer_T5 sia scaduto
    //   *104,* o  che  *34,*  il parametro MainClass_C1_parametro_P9 non sia  uguale a  True 
    //   *104,* e  che  *,*  il contatore MainClass_C1_contatore_Co7 sia  uguale a  *53,* 133
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_AndLogicOP_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetInMainc7(my_id) == false));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_4);
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! Timer_Scaduto(L_P1__GetMainc30(my_id)));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_5);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_3);
    bool res_NotLogicOP_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetInMainc5(my_id) == true));
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! res_NotLogicOP_7);
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_6);
    
    if(res_OrLogicOP_2){
    bool res_OrLogicOP_8 = false;
    bool res_ImpliesLogicOp_9 = true;
    bool res_OrLogicOP_10 = false;
    bool res_OrLogicOP_11 = false;
    bool res_AndLogicOP_12 = true;
    bool res_AndLogicOP_13 = true;
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! Timer_Attivo(L_P1__GetMainc27(my_id)));
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_NotLogicOP_14);
    res_AndLogicOP_13 = (res_AndLogicOP_13 && (L_P1__GetMainc25(my_id) == true));
    
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_AndLogicOP_13);
    bool res_NotLogicOP_15 = true;
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (L_P1__GetParamMainc11(my_id) == false));
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! res_NotLogicOP_16);
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_NotLogicOP_15);
    
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_AndLogicOP_12);
    res_OrLogicOP_11 = (res_OrLogicOP_11 || (L_P1__GetParamMainc11(my_id) == false));
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_OrLogicOP_11);
    bool res_NotLogicOP_17 = true;
    bool res_NotLogicOP_18 = true;
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! (L_P1__GetParamMainc10(my_id) == c180));
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! res_NotLogicOP_18);
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_NotLogicOP_17);
    
    if(res_OrLogicOP_10){
    bool res_XorLogicOP_19 = true;
    int xorIndex_res_XorLogicOP_19 = 0;
    bool res_ImpliesLogicOp_20 = true;
    bool res_NotLogicOP_21 = true;
    res_NotLogicOP_21 = (res_NotLogicOP_21 && ! (L_P1_C1_GetState(my_id) == C1_St_state));
    if(res_NotLogicOP_21){
    bool res_OrLogicOP_22 = false;
    bool res_ImpliesLogicOp_23 = true;
    bool res_AndLogicOP_24 = true;
    bool res_AndLogicOP_25 = true;
    bool res_AndLogicOP_26 = true;
    bool res_AndLogicOP_27 = true;
    bool res_AndLogicOP_28 = true;
    bool res_NotLogicOP_29 = true;
    bool res_NotLogicOP_30 = true;
    res_NotLogicOP_30 = (res_NotLogicOP_30 && ! (L_P1__GetInMainc8(my_id) == c180));
    res_NotLogicOP_29 = (res_NotLogicOP_29 && ! res_NotLogicOP_30);
    res_AndLogicOP_28 = (res_AndLogicOP_28 && res_NotLogicOP_29);
    bool res_NotLogicOP_31 = true;
    res_NotLogicOP_31 = (res_NotLogicOP_31 && ! (L_P1__GetMainc25(my_id) == false));
    res_AndLogicOP_28 = (res_AndLogicOP_28 && res_NotLogicOP_31);
    
    res_AndLogicOP_27 = (res_AndLogicOP_27 && res_AndLogicOP_28);
    bool res_NotLogicOP_32 = true;
    res_NotLogicOP_32 = (res_NotLogicOP_32 && ! Timer_Disattivo(L_P1__GetMainc30(my_id)));
    res_AndLogicOP_27 = (res_AndLogicOP_27 && res_NotLogicOP_32);
    
    res_AndLogicOP_26 = (res_AndLogicOP_26 && res_AndLogicOP_27);
    bool res_NotLogicOP_33 = true;
    res_NotLogicOP_33 = (res_NotLogicOP_33 && ! (L_P1__GetInMainc5(my_id) == true));
    res_AndLogicOP_26 = (res_AndLogicOP_26 && res_NotLogicOP_33);
    
    res_AndLogicOP_25 = (res_AndLogicOP_25 && res_AndLogicOP_26);
    bool res_NotLogicOP_34 = true;
    bool res_NotLogicOP_35 = true;
    res_NotLogicOP_35 = (res_NotLogicOP_35 && ! (L_P1__GetParamMainc10(my_id) == c180));
    res_NotLogicOP_34 = (res_NotLogicOP_34 && ! res_NotLogicOP_35);
    res_AndLogicOP_25 = (res_AndLogicOP_25 && res_NotLogicOP_34);
    
    res_AndLogicOP_24 = (res_AndLogicOP_24 && res_AndLogicOP_25);
    bool res_NotLogicOP_36 = true;
    res_NotLogicOP_36 = (res_NotLogicOP_36 && ! (L_P1__GetMainc25(my_id) == true));
    res_AndLogicOP_24 = (res_AndLogicOP_24 && res_NotLogicOP_36);
    
    if(res_AndLogicOP_24){
    bool res_ImpliesLogicOp_37 = true;
    bool res_OrLogicOP_38 = false;
    bool res_OrLogicOP_39 = false;
    bool res_OrLogicOP_40 = false;
    bool res_OrLogicOP_41 = false;
    bool res_AndLogicOP_42 = true;
    bool res_NotLogicOP_43 = true;
    res_NotLogicOP_43 = (res_NotLogicOP_43 && ! (L_P1__GetParamMainc10(my_id) == c180));
    res_AndLogicOP_42 = (res_AndLogicOP_42 && res_NotLogicOP_43);
    bool res_NotLogicOP_44 = true;
    res_NotLogicOP_44 = (res_NotLogicOP_44 && ! (L_P1__GetInMainc7(my_id) == true));
    res_AndLogicOP_42 = (res_AndLogicOP_42 && res_NotLogicOP_44);
    
    res_OrLogicOP_41 = (res_OrLogicOP_41 || res_AndLogicOP_42);
    res_OrLogicOP_41 = (res_OrLogicOP_41 || (L_P1__GetMainc24(my_id) == true));
    
    res_OrLogicOP_40 = (res_OrLogicOP_40 || res_OrLogicOP_41);
    bool res_NotLogicOP_45 = true;
    res_NotLogicOP_45 = (res_NotLogicOP_45 && ! (Counter_GetValore(L_P1__GetMainc33(my_id)) < 130u));
    res_OrLogicOP_40 = (res_OrLogicOP_40 || res_NotLogicOP_45);
    
    res_OrLogicOP_39 = (res_OrLogicOP_39 || res_OrLogicOP_40);
    bool res_NotLogicOP_46 = true;
    bool res_NotLogicOP_47 = true;
    res_NotLogicOP_47 = (res_NotLogicOP_47 && ! (L_P1__GetInMainc7(my_id) == false));
    res_NotLogicOP_46 = (res_NotLogicOP_46 && ! res_NotLogicOP_47);
    res_OrLogicOP_39 = (res_OrLogicOP_39 || res_NotLogicOP_46);
    
    res_OrLogicOP_38 = (res_OrLogicOP_38 || res_OrLogicOP_39);
    res_OrLogicOP_38 = (res_OrLogicOP_38 || (L_P1__GetParamMainc9(my_id) == avviox));
    
    if(res_OrLogicOP_38){
    bool res_OrLogicOP_48 = false;
    bool res_AndLogicOP_49 = true;
    res_AndLogicOP_49 = (res_AndLogicOP_49 && Timer_Scaduto(L_P1__GetMainc31(my_id)));
    res_AndLogicOP_49 = (res_AndLogicOP_49 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_48 = (res_OrLogicOP_48 || res_AndLogicOP_49);
    res_OrLogicOP_48 = (res_OrLogicOP_48 || (L_P1__GetMainc25(my_id) == false));
    
    res_ImpliesLogicOp_37 = (res_ImpliesLogicOp_37 && res_OrLogicOP_48);
    }
    res_ImpliesLogicOp_23 = (res_ImpliesLogicOp_23 && res_ImpliesLogicOp_37);
    }
    res_OrLogicOP_22 = (res_OrLogicOP_22 || res_ImpliesLogicOp_23);
    res_OrLogicOP_22 = (res_OrLogicOP_22 || (L_P1__GetInMainc5(my_id) == true));
    
    res_ImpliesLogicOp_20 = (res_ImpliesLogicOp_20 && res_OrLogicOP_22);
    }
    if(res_ImpliesLogicOp_20){
    xorIndex_res_XorLogicOP_19 = (xorIndex_res_XorLogicOP_19 + 1);
    }
    bool res_OrLogicOP_50 = false;
    bool res_AndLogicOP_51 = true;
    bool res_NotLogicOP_52 = true;
    bool res_NotLogicOP_53 = true;
    res_NotLogicOP_53 = (res_NotLogicOP_53 && ! (L_P1__GetParamMainc11(my_id) == false));
    res_NotLogicOP_52 = (res_NotLogicOP_52 && ! res_NotLogicOP_53);
    res_AndLogicOP_51 = (res_AndLogicOP_51 && res_NotLogicOP_52);
    bool res_NotLogicOP_54 = true;
    res_NotLogicOP_54 = (res_NotLogicOP_54 && ! (L_P1__GetInMainc5(my_id) == false));
    res_AndLogicOP_51 = (res_AndLogicOP_51 && res_NotLogicOP_54);
    
    res_OrLogicOP_50 = (res_OrLogicOP_50 || res_AndLogicOP_51);
    bool res_AndLogicOP_55 = true;
    bool res_NotLogicOP_56 = true;
    res_NotLogicOP_56 = (res_NotLogicOP_56 && ! (L_P1__GetMainc24(my_id) == true));
    res_AndLogicOP_55 = (res_AndLogicOP_55 && res_NotLogicOP_56);
    res_AndLogicOP_55 = (res_AndLogicOP_55 && Timer_Disattivo(L_P1__GetMainc30(my_id)));
    
    res_OrLogicOP_50 = (res_OrLogicOP_50 || res_AndLogicOP_55);
    
    if(res_OrLogicOP_50){
    xorIndex_res_XorLogicOP_19 = (xorIndex_res_XorLogicOP_19 + 1);
    }
    
    res_XorLogicOP_19 = (res_XorLogicOP_19 && (xorIndex_res_XorLogicOP_19 == 1));
    res_ImpliesLogicOp_9 = (res_ImpliesLogicOp_9 && res_XorLogicOP_19);
    }
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_ImpliesLogicOp_9);
    bool res_OrLogicOP_57 = false;
    res_OrLogicOP_57 = (res_OrLogicOP_57 || Timer_Scaduto(L_P1__GetMainc31(my_id)));
    bool res_AndLogicOP_58 = true;
    bool res_NotLogicOP_59 = true;
    res_NotLogicOP_59 = (res_NotLogicOP_59 && ! (L_P1__GetParamMainc11(my_id) == true));
    res_AndLogicOP_58 = (res_AndLogicOP_58 && res_NotLogicOP_59);
    res_AndLogicOP_58 = (res_AndLogicOP_58 && (Counter_GetValore(L_P1__GetMainc35(my_id)) == 133u));
    
    res_OrLogicOP_57 = (res_OrLogicOP_57 || res_AndLogicOP_58);
    
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_OrLogicOP_57);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_OrLogicOP_8);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *47,48,51,*  *,*  il contatore MainClass_C1_contatore_Co7 sia  maggiore di  *54,* 11
    //   *104,* o  che   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* o  che  *,*  il controllo MainClass_C1_controllo_C2 sia  uguale a  True 
    //   *104,* e  che  *35,*  il controllo MainClass_C1_controllo_C9 non sia  diverso da c180
    //   *104,* o  che  *34,*  il parametro MainClass_C1_parametro_P5 non sia  diverso da c180
    //   *104,* e  che  *35,*  il controllo MainClass_C1_controllo_C2 sia  uguale a  True
    bool res_OrLogicOP_60 = false;
    bool res_OrLogicOP_61 = false;
    bool res_OrLogicOP_62 = false;
    res_OrLogicOP_62 = (res_OrLogicOP_62 || (Counter_GetValore(L_P1__GetMainc35(my_id)) > 11u));
    res_OrLogicOP_62 = (res_OrLogicOP_62 || (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_61 = (res_OrLogicOP_61 || res_OrLogicOP_62);
    bool res_AndLogicOP_63 = true;
    res_AndLogicOP_63 = (res_AndLogicOP_63 && (L_P1__GetInMainc5(my_id) == true));
    bool res_NotLogicOP_64 = true;
    bool res_NotLogicOP_65 = true;
    res_NotLogicOP_65 = (res_NotLogicOP_65 && ! (L_P1__GetInMainc8(my_id) == c180));
    res_NotLogicOP_64 = (res_NotLogicOP_64 && ! res_NotLogicOP_65);
    res_AndLogicOP_63 = (res_AndLogicOP_63 && res_NotLogicOP_64);
    
    res_OrLogicOP_61 = (res_OrLogicOP_61 || res_AndLogicOP_63);
    
    res_OrLogicOP_60 = (res_OrLogicOP_60 || res_OrLogicOP_61);
    bool res_AndLogicOP_66 = true;
    bool res_NotLogicOP_67 = true;
    bool res_NotLogicOP_68 = true;
    res_NotLogicOP_68 = (res_NotLogicOP_68 && ! (L_P1__GetParamMainc10(my_id) == c180));
    res_NotLogicOP_67 = (res_NotLogicOP_67 && ! res_NotLogicOP_68);
    res_AndLogicOP_66 = (res_AndLogicOP_66 && res_NotLogicOP_67);
    res_AndLogicOP_66 = (res_AndLogicOP_66 && (L_P1__GetInMainc5(my_id) == true));
    
    res_OrLogicOP_60 = (res_OrLogicOP_60 || res_AndLogicOP_66);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_60);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
    
    { commento: {61,}  se il controllo ConsDef è uguale a FALSE  commento: {36,} o  se il timer MainClass_C1_timer_T4 non è attivo commento: {38,} e  se il contatore MainClass_C1_contatore_Co10 è  uguale a  commento: {53,} 15 commento: {35,} o  se il controllo MainClass_C1_controllo_C9 non è  diverso da c180 commento: {35,} e  se il controllo MainClass_C1_controllo_C2 è  diverso da  True  commento: {37,} o  se la variabile MainClass_C1_variabile_V10 non è  uguale a  False , Tutte le seguenti { 
     commento: {62,} commento: {37,}  se la variabile MainClass_C1_variabile_V7 è  diverso da  True  commento: {34,} e  se il parametro MainClass_C1_parametro_P9 è  uguale a  True  commento: {38,} e  se il contatore MainClass_C1_contatore_Co7 è  uguale a  commento: {53,} 1212 commento: {34,} o  se il parametro MainClass_C1_parametro_P9 è  diverso da  False , Almeno una delle seguenti { 
     commento: {63,} commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  diverso da RossoGialloVerde commento: {34,} o  se il parametro MainClass_C1_parametro_P9 è  diverso da  False  commento: {36,} o  se il timer MainClass_C1_timer_T4 è attivo commento: {36,} o  se il timer MainClass_C1_timer_T5 non è scaduto commento: {37,} o  se la variabile MainClass_C1_variabile_V7 è  diverso da  False , Solo una delle seguenti { 
     commento: {63,}  se il ripristino dello stato  non è  uguale a  commento: {53,}  state1  commento: {107,} commento: {38,} o  se il contatore MainClass_C1_contatore_Co10 è  maggiore di  commento: {54,} 130 commento: {35,} e  se il controllo MainClass_C1_controllo_C2 è  uguale a  True , Solo una delle seguenti { 
     commento: {63,} commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo commento: {38,} e  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  commento: {54,} 15345, Solo una delle seguenti { 
     commento: {61,} commento: {34,}  se il parametro MainClass_C1_parametro_P5 non è  diverso da c180 commento: {37,} e  se la variabile MainClass_C1_variabile_V10 non è  diverso da  True  commento: {37,} o  se la variabile MainClass_C1_variabile_V7 non è  uguale a  False  commento: {38,} o  se il contatore MainClass_C1_contatore_Co10 non è  maggiore di  commento: {54,} 1312, Tutte le seguenti { 
     commento: {61,} commento: {34,}  se lo stato  è  diverso da  commento: {56,}  state1  commento: {106,} commento: {36,} e  se il timer MainClass_C1_timer_T4 è scaduto, Tutte le seguenti { 
     commento: {37,}  se la variabile MainClass_C1_variabile_V10 non è  diverso da  True  commento: {36,} o  se il timer MainClass_C1_timer_T5 non è scaduto, Verifica che   commento: {47,48,50,51,52,}   l'argomento argomento_ave2 sia  diverso da GialloaVerdea commento: {,} 
     commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V7 non sia  diverso da  False 
     commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C2 non sia  uguale a  False 
     commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P5 sia  diverso da c180
     commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co10 sia  minore di  commento: {55,} 1303
    
    
     } Verifica che   commento: {48,51,}  commento: {,}  il controllo MainClass_C1_controllo_C2 non sia  diverso da  False 
     commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co10 non sia  minore di  commento: {55,} 15
     commento: {104,} o  che  commento: {38,}  il contatore MainClass_C1_contatore_Co10 sia  uguale a  commento: {53,} 111203
    
    
     } Verifica che   commento: {49,}  commento: {,}  il timer MainClass_C1_timer_T4 non sia attivo
    
    
     } Verifica che   commento: {47,48,49,51,}  commento: {,}  il contatore MainClass_C1_contatore_Co7 non sia  diverso da  commento: {56,} 15
     commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T5 non sia disattivo
     commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C2 sia  diverso da  False 
     commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P1 non sia  uguale a avviox
    
    
     } Verifica che   commento: {48,}  commento: {,}  il controllo MainClass_C1_controllo_C7 sia  uguale a GialloaVerdea
     commento: {104,} e  che  commento: {35,}  il controllo MainClass_C1_controllo_C2 non sia  diverso da  False 
    
    
     } Verifica che   commento: {47,48,51,}  commento: {,}  il controllo MainClass_C1_controllo_C9 sia  uguale a c180
     commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co7 non sia  uguale a  commento: {53,} 1312
     commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P1 non sia  uguale a avviox
    
    
     } Verifica che   commento: {48,49,50,}  commento: {,}  il timer MainClass_C1_timer_T5 non sia scaduto
     commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C2 non sia  diverso da  False 
     commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V7 non sia  uguale a  True 
    
    
     } Verifica che   commento: {48,49,}  commento: {,}  il controllo MainClass_C1_controllo_C2 sia  uguale a  True 
     commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T5 sia disattivo
     commento: {104,} e  che  commento: {36,}  il timer MainClass_C1_timer_T5 non sia scaduto
    
    
    }
*/
bool L_P1__Macro6(instance_id_t const my_id , bool argom24, C1_Enumerat3 argom25, C1_Enumerat4 argom26, C1_Enumerat3 argom27, C1_Enumerat4 argom28, C1_Enumerat4 argom29, bool argom30)
{
bool res_AndLogicOP_0 = true;
    
    //  *61,*  se il controllo ConsDef è uguale a FALSE  *36,* o  se il timer MainClass_C1_timer_T4 non è attivo *38,* e  se il contatore MainClass_C1_contatore_Co10 è  uguale a  *53,* 15 *35,* o  se il controllo MainClass_C1_controllo_C9 non è  diverso da c180 *35,* e  se il controllo MainClass_C1_controllo_C2 è  diverso da  True  *37,* o  se la variabile MainClass_C1_variabile_V10 non è  uguale a  False , Tutte le seguenti { 
    //   *62,* *37,*  se la variabile MainClass_C1_variabile_V7 è  diverso da  True  *34,* e  se il parametro MainClass_C1_parametro_P9 è  uguale a  True  *38,* e  se il contatore MainClass_C1_contatore_Co7 è  uguale a  *53,* 1212 *34,* o  se il parametro MainClass_C1_parametro_P9 è  diverso da  False , Almeno una delle seguenti { 
    //   *63,* *109,*  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  diverso da RossoGialloVerde *34,* o  se il parametro MainClass_C1_parametro_P9 è  diverso da  False  *36,* o  se il timer MainClass_C1_timer_T4 è attivo *36,* o  se il timer MainClass_C1_timer_T5 non è scaduto *37,* o  se la variabile MainClass_C1_variabile_V7 è  diverso da  False , Solo una delle seguenti { 
    //   *63,*  se il ripristino dello stato  non è  uguale a  *53,*  state1  *107,* *38,* o  se il contatore MainClass_C1_contatore_Co10 è  maggiore di  *54,* 130 *35,* e  se il controllo MainClass_C1_controllo_C2 è  uguale a  True , Solo una delle seguenti { 
    //   *63,* *110,*  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo *38,* e  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  *54,* 15345, Solo una delle seguenti { 
    //   *61,* *34,*  se il parametro MainClass_C1_parametro_P5 non è  diverso da c180 *37,* e  se la variabile MainClass_C1_variabile_V10 non è  diverso da  True  *37,* o  se la variabile MainClass_C1_variabile_V7 non è  uguale a  False  *38,* o  se il contatore MainClass_C1_contatore_Co10 non è  maggiore di  *54,* 1312, Tutte le seguenti { 
    //   *61,* *34,*  se lo stato  è  diverso da  *56,*  state1  *106,* *36,* e  se il timer MainClass_C1_timer_T4 è scaduto, Tutte le seguenti { 
    //   *37,*  se la variabile MainClass_C1_variabile_V10 non è  diverso da  True  *36,* o  se il timer MainClass_C1_timer_T5 non è scaduto, Verifica che   *47,48,50,51,52,*   l'argomento argomento_ave2 sia  diverso da GialloaVerdea *,* 
    //   *104,* e  che  *,*  la variabile MainClass_C1_variabile_V7 non sia  diverso da  False 
    //   *104,* o  che  *,*  il controllo MainClass_C1_controllo_C2 non sia  uguale a  False 
    //   *104,* o  che  *34,*  il parametro MainClass_C1_parametro_P5 sia  diverso da c180
    //   *104,* e  che  *,*  il contatore MainClass_C1_contatore_Co10 sia  minore di  *55,* 1303
    //   } Verifica che   *48,51,*  *,*  il controllo MainClass_C1_controllo_C2 non sia  diverso da  False 
    //   *104,* e  che  *,*  il contatore MainClass_C1_contatore_Co10 non sia  minore di  *55,* 15
    //   *104,* o  che  *38,*  il contatore MainClass_C1_contatore_Co10 sia  uguale a  *53,* 111203
    //   } Verifica che   *49,*  *,*  il timer MainClass_C1_timer_T4 non sia attivo
    //   } Verifica che   *47,48,49,51,*  *,*  il contatore MainClass_C1_contatore_Co7 non sia  diverso da  *56,* 15
    //   *104,* e  che  *,*  il timer MainClass_C1_timer_T5 non sia disattivo
    //   *104,* o  che  *,*  il controllo MainClass_C1_controllo_C2 sia  diverso da  False 
    //   *104,* o  che  *34,*  il parametro MainClass_C1_parametro_P1 non sia  uguale a avviox
    //   } Verifica che   *48,*  *,*  il controllo MainClass_C1_controllo_C7 sia  uguale a GialloaVerdea
    //   *104,* e  che  *35,*  il controllo MainClass_C1_controllo_C2 non sia  diverso da  False 
    //   } Verifica che   *47,48,51,*  *,*  il controllo MainClass_C1_controllo_C9 sia  uguale a c180
    //   *104,* e  che  *,*  il contatore MainClass_C1_contatore_Co7 non sia  uguale a  *53,* 1312
    //   *104,* e  che  *34,*  il parametro MainClass_C1_parametro_P1 non sia  uguale a avviox
    //   } Verifica che   *48,49,50,*  *,*  il timer MainClass_C1_timer_T5 non sia scaduto
    //   *104,* e  che  *,*  il controllo MainClass_C1_controllo_C2 non sia  diverso da  False 
    //   *104,* e  che  *,*  la variabile MainClass_C1_variabile_V7 non sia  uguale a  True 
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_OrLogicOP_4 = false;
    res_OrLogicOP_4 = (res_OrLogicOP_4 || (L_P1__GetInConsd(my_id) == false));
    bool res_AndLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! Timer_Attivo(L_P1__GetMainc30(my_id)));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_6);
    res_AndLogicOP_5 = (res_AndLogicOP_5 && (Counter_GetValore(L_P1__GetMainc33(my_id)) == 15u));
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_AndLogicOP_5);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_OrLogicOP_4);
    bool res_AndLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetInMainc8(my_id) == c180));
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! res_NotLogicOP_9);
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_8);
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__GetInMainc5(my_id) == true));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_10);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_AndLogicOP_7);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (L_P1__GetMainc24(my_id) == false));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_11);
    
    if(res_OrLogicOP_2){
    bool res_AndLogicOP_12 = true;
    bool res_ImpliesLogicOp_13 = true;
    bool res_OrLogicOP_14 = false;
    bool res_AndLogicOP_15 = true;
    bool res_AndLogicOP_16 = true;
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! (L_P1__GetMainc25(my_id) == true));
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_NotLogicOP_17);
    res_AndLogicOP_16 = (res_AndLogicOP_16 && (L_P1__GetParamMainc11(my_id) == true));
    
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_AndLogicOP_16);
    res_AndLogicOP_15 = (res_AndLogicOP_15 && (Counter_GetValore(L_P1__GetMainc35(my_id)) == 1212u));
    
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_AndLogicOP_15);
    bool res_NotLogicOP_18 = true;
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! (L_P1__GetParamMainc11(my_id) == false));
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_NotLogicOP_18);
    
    if(res_OrLogicOP_14){
    bool res_OrLogicOP_19 = false;
    bool res_ImpliesLogicOp_20 = true;
    bool res_OrLogicOP_21 = false;
    bool res_OrLogicOP_22 = false;
    bool res_OrLogicOP_23 = false;
    bool res_OrLogicOP_24 = false;
    bool res_NotLogicOP_25 = true;
    bool res_NotLogicOP_26 = true;
    res_NotLogicOP_26 = (res_NotLogicOP_26 && ! (L_P1__GetMainc17(my_id) == rossogiallo1));
    res_NotLogicOP_25 = (res_NotLogicOP_25 && ! res_NotLogicOP_26);
    res_OrLogicOP_24 = (res_OrLogicOP_24 || res_NotLogicOP_25);
    bool res_NotLogicOP_27 = true;
    res_NotLogicOP_27 = (res_NotLogicOP_27 && ! (L_P1__GetParamMainc11(my_id) == false));
    res_OrLogicOP_24 = (res_OrLogicOP_24 || res_NotLogicOP_27);
    
    res_OrLogicOP_23 = (res_OrLogicOP_23 || res_OrLogicOP_24);
    res_OrLogicOP_23 = (res_OrLogicOP_23 || Timer_Attivo(L_P1__GetMainc30(my_id)));
    
    res_OrLogicOP_22 = (res_OrLogicOP_22 || res_OrLogicOP_23);
    bool res_NotLogicOP_28 = true;
    res_NotLogicOP_28 = (res_NotLogicOP_28 && ! Timer_Scaduto(L_P1__GetMainc31(my_id)));
    res_OrLogicOP_22 = (res_OrLogicOP_22 || res_NotLogicOP_28);
    
    res_OrLogicOP_21 = (res_OrLogicOP_21 || res_OrLogicOP_22);
    bool res_NotLogicOP_29 = true;
    res_NotLogicOP_29 = (res_NotLogicOP_29 && ! (L_P1__GetMainc25(my_id) == false));
    res_OrLogicOP_21 = (res_OrLogicOP_21 || res_NotLogicOP_29);
    
    if(res_OrLogicOP_21){
    bool res_XorLogicOP_30 = true;
    int xorIndex_res_XorLogicOP_30 = 0;
    bool res_ImpliesLogicOp_31 = true;
    bool res_OrLogicOP_32 = false;
    bool res_NotLogicOP_33 = true;
    res_NotLogicOP_33 = (res_NotLogicOP_33 && ! (L_P1__GetStato1(my_id) == C1_St_state));
    res_OrLogicOP_32 = (res_OrLogicOP_32 || res_NotLogicOP_33);
    bool res_AndLogicOP_34 = true;
    res_AndLogicOP_34 = (res_AndLogicOP_34 && (Counter_GetValore(L_P1__GetMainc33(my_id)) > 130u));
    res_AndLogicOP_34 = (res_AndLogicOP_34 && (L_P1__GetInMainc5(my_id) == true));
    
    res_OrLogicOP_32 = (res_OrLogicOP_32 || res_AndLogicOP_34);
    
    if(res_OrLogicOP_32){
    bool res_XorLogicOP_35 = true;
    int xorIndex_res_XorLogicOP_35 = 0;
    bool res_ImpliesLogicOp_36 = true;
    bool res_AndLogicOP_37 = true;
    bool res_NotLogicOP_38 = true;
    res_NotLogicOP_38 = (res_NotLogicOP_38 && ! Timer_Attivo(L_P1__GetMainc27(my_id)));
    res_AndLogicOP_37 = (res_AndLogicOP_37 && res_NotLogicOP_38);
    bool res_NotLogicOP_39 = true;
    res_NotLogicOP_39 = (res_NotLogicOP_39 && ! (Counter_GetValore(L_P1__GetMainc35(my_id)) > 15345u));
    res_AndLogicOP_37 = (res_AndLogicOP_37 && res_NotLogicOP_39);
    
    if(res_AndLogicOP_37){
    bool res_XorLogicOP_40 = true;
    int xorIndex_res_XorLogicOP_40 = 0;
    bool res_ImpliesLogicOp_41 = true;
    bool res_OrLogicOP_42 = false;
    bool res_OrLogicOP_43 = false;
    bool res_AndLogicOP_44 = true;
    bool res_NotLogicOP_45 = true;
    bool res_NotLogicOP_46 = true;
    res_NotLogicOP_46 = (res_NotLogicOP_46 && ! (L_P1__GetParamMainc10(my_id) == c180));
    res_NotLogicOP_45 = (res_NotLogicOP_45 && ! res_NotLogicOP_46);
    res_AndLogicOP_44 = (res_AndLogicOP_44 && res_NotLogicOP_45);
    bool res_NotLogicOP_47 = true;
    bool res_NotLogicOP_48 = true;
    res_NotLogicOP_48 = (res_NotLogicOP_48 && ! (L_P1__GetMainc24(my_id) == true));
    res_NotLogicOP_47 = (res_NotLogicOP_47 && ! res_NotLogicOP_48);
    res_AndLogicOP_44 = (res_AndLogicOP_44 && res_NotLogicOP_47);
    
    res_OrLogicOP_43 = (res_OrLogicOP_43 || res_AndLogicOP_44);
    bool res_NotLogicOP_49 = true;
    res_NotLogicOP_49 = (res_NotLogicOP_49 && ! (L_P1__GetMainc25(my_id) == false));
    res_OrLogicOP_43 = (res_OrLogicOP_43 || res_NotLogicOP_49);
    
    res_OrLogicOP_42 = (res_OrLogicOP_42 || res_OrLogicOP_43);
    bool res_NotLogicOP_50 = true;
    res_NotLogicOP_50 = (res_NotLogicOP_50 && ! (Counter_GetValore(L_P1__GetMainc33(my_id)) > 1312u));
    res_OrLogicOP_42 = (res_OrLogicOP_42 || res_NotLogicOP_50);
    
    if(res_OrLogicOP_42){
    bool res_AndLogicOP_51 = true;
    bool res_ImpliesLogicOp_52 = true;
    bool res_AndLogicOP_53 = true;
    bool res_NotLogicOP_54 = true;
    res_NotLogicOP_54 = (res_NotLogicOP_54 && ! (L_P1_C1_GetState(my_id) == C1_St_state));
    res_AndLogicOP_53 = (res_AndLogicOP_53 && res_NotLogicOP_54);
    res_AndLogicOP_53 = (res_AndLogicOP_53 && Timer_Scaduto(L_P1__GetMainc30(my_id)));
    
    if(res_AndLogicOP_53){
    bool res_ImpliesLogicOp_55 = true;
    bool res_OrLogicOP_56 = false;
    bool res_NotLogicOP_57 = true;
    bool res_NotLogicOP_58 = true;
    res_NotLogicOP_58 = (res_NotLogicOP_58 && ! (L_P1__GetMainc24(my_id) == true));
    res_NotLogicOP_57 = (res_NotLogicOP_57 && ! res_NotLogicOP_58);
    res_OrLogicOP_56 = (res_OrLogicOP_56 || res_NotLogicOP_57);
    bool res_NotLogicOP_59 = true;
    res_NotLogicOP_59 = (res_NotLogicOP_59 && ! Timer_Scaduto(L_P1__GetMainc31(my_id)));
    res_OrLogicOP_56 = (res_OrLogicOP_56 || res_NotLogicOP_59);
    
    if(res_OrLogicOP_56){
    bool res_OrLogicOP_60 = false;
    bool res_OrLogicOP_61 = false;
    bool res_AndLogicOP_62 = true;
    bool res_NotLogicOP_63 = true;
    res_NotLogicOP_63 = (res_NotLogicOP_63 && ! (argom25 == gialloaverd));
    res_AndLogicOP_62 = (res_AndLogicOP_62 && res_NotLogicOP_63);
    bool res_NotLogicOP_64 = true;
    bool res_NotLogicOP_65 = true;
    res_NotLogicOP_65 = (res_NotLogicOP_65 && ! (L_P1__GetMainc25(my_id) == false));
    res_NotLogicOP_64 = (res_NotLogicOP_64 && ! res_NotLogicOP_65);
    res_AndLogicOP_62 = (res_AndLogicOP_62 && res_NotLogicOP_64);
    
    res_OrLogicOP_61 = (res_OrLogicOP_61 || res_AndLogicOP_62);
    bool res_NotLogicOP_66 = true;
    res_NotLogicOP_66 = (res_NotLogicOP_66 && ! (L_P1__GetInMainc5(my_id) == false));
    res_OrLogicOP_61 = (res_OrLogicOP_61 || res_NotLogicOP_66);
    
    res_OrLogicOP_60 = (res_OrLogicOP_60 || res_OrLogicOP_61);
    bool res_AndLogicOP_67 = true;
    bool res_NotLogicOP_68 = true;
    res_NotLogicOP_68 = (res_NotLogicOP_68 && ! (L_P1__GetParamMainc10(my_id) == c180));
    res_AndLogicOP_67 = (res_AndLogicOP_67 && res_NotLogicOP_68);
    res_AndLogicOP_67 = (res_AndLogicOP_67 && (Counter_GetValore(L_P1__GetMainc33(my_id)) < 1303u));
    
    res_OrLogicOP_60 = (res_OrLogicOP_60 || res_AndLogicOP_67);
    
    res_ImpliesLogicOp_55 = (res_ImpliesLogicOp_55 && res_OrLogicOP_60);
    }
    res_ImpliesLogicOp_52 = (res_ImpliesLogicOp_52 && res_ImpliesLogicOp_55);
    }
    res_AndLogicOP_51 = (res_AndLogicOP_51 && res_ImpliesLogicOp_52);
    bool res_OrLogicOP_69 = false;
    bool res_AndLogicOP_70 = true;
    bool res_NotLogicOP_71 = true;
    bool res_NotLogicOP_72 = true;
    res_NotLogicOP_72 = (res_NotLogicOP_72 && ! (L_P1__GetInMainc5(my_id) == false));
    res_NotLogicOP_71 = (res_NotLogicOP_71 && ! res_NotLogicOP_72);
    res_AndLogicOP_70 = (res_AndLogicOP_70 && res_NotLogicOP_71);
    bool res_NotLogicOP_73 = true;
    res_NotLogicOP_73 = (res_NotLogicOP_73 && ! (Counter_GetValore(L_P1__GetMainc33(my_id)) < 15u));
    res_AndLogicOP_70 = (res_AndLogicOP_70 && res_NotLogicOP_73);
    
    res_OrLogicOP_69 = (res_OrLogicOP_69 || res_AndLogicOP_70);
    res_OrLogicOP_69 = (res_OrLogicOP_69 || (Counter_GetValore(L_P1__GetMainc33(my_id)) == 111203u));
    
    res_AndLogicOP_51 = (res_AndLogicOP_51 && res_OrLogicOP_69);
    
    res_ImpliesLogicOp_41 = (res_ImpliesLogicOp_41 && res_AndLogicOP_51);
    }
    if(res_ImpliesLogicOp_41){
    xorIndex_res_XorLogicOP_40 = (xorIndex_res_XorLogicOP_40 + 1);
    }
    bool res_NotLogicOP_74 = true;
    res_NotLogicOP_74 = (res_NotLogicOP_74 && ! Timer_Attivo(L_P1__GetMainc30(my_id)));
    if(res_NotLogicOP_74){
    xorIndex_res_XorLogicOP_40 = (xorIndex_res_XorLogicOP_40 + 1);
    }
    
    res_XorLogicOP_40 = (res_XorLogicOP_40 && (xorIndex_res_XorLogicOP_40 == 1));
    res_ImpliesLogicOp_36 = (res_ImpliesLogicOp_36 && res_XorLogicOP_40);
    }
    if(res_ImpliesLogicOp_36){
    xorIndex_res_XorLogicOP_35 = (xorIndex_res_XorLogicOP_35 + 1);
    }
    bool res_OrLogicOP_75 = false;
    bool res_OrLogicOP_76 = false;
    bool res_AndLogicOP_77 = true;
    bool res_NotLogicOP_78 = true;
    bool res_NotLogicOP_79 = true;
    res_NotLogicOP_79 = (res_NotLogicOP_79 && ! (Counter_GetValore(L_P1__GetMainc35(my_id)) == 15u));
    res_NotLogicOP_78 = (res_NotLogicOP_78 && ! res_NotLogicOP_79);
    res_AndLogicOP_77 = (res_AndLogicOP_77 && res_NotLogicOP_78);
    bool res_NotLogicOP_80 = true;
    res_NotLogicOP_80 = (res_NotLogicOP_80 && ! Timer_Disattivo(L_P1__GetMainc31(my_id)));
    res_AndLogicOP_77 = (res_AndLogicOP_77 && res_NotLogicOP_80);
    
    res_OrLogicOP_76 = (res_OrLogicOP_76 || res_AndLogicOP_77);
    bool res_NotLogicOP_81 = true;
    res_NotLogicOP_81 = (res_NotLogicOP_81 && ! (L_P1__GetInMainc5(my_id) == false));
    res_OrLogicOP_76 = (res_OrLogicOP_76 || res_NotLogicOP_81);
    
    res_OrLogicOP_75 = (res_OrLogicOP_75 || res_OrLogicOP_76);
    bool res_NotLogicOP_82 = true;
    res_NotLogicOP_82 = (res_NotLogicOP_82 && ! (L_P1__GetParamMainc9(my_id) == avviox));
    res_OrLogicOP_75 = (res_OrLogicOP_75 || res_NotLogicOP_82);
    
    if(res_OrLogicOP_75){
    xorIndex_res_XorLogicOP_35 = (xorIndex_res_XorLogicOP_35 + 1);
    }
    
    res_XorLogicOP_35 = (res_XorLogicOP_35 && (xorIndex_res_XorLogicOP_35 == 1));
    res_ImpliesLogicOp_31 = (res_ImpliesLogicOp_31 && res_XorLogicOP_35);
    }
    if(res_ImpliesLogicOp_31){
    xorIndex_res_XorLogicOP_30 = (xorIndex_res_XorLogicOP_30 + 1);
    }
    bool res_AndLogicOP_83 = true;
    res_AndLogicOP_83 = (res_AndLogicOP_83 && (L_P1__GetInMainc6(my_id) == gialloaverd));
    bool res_NotLogicOP_84 = true;
    bool res_NotLogicOP_85 = true;
    res_NotLogicOP_85 = (res_NotLogicOP_85 && ! (L_P1__GetInMainc5(my_id) == false));
    res_NotLogicOP_84 = (res_NotLogicOP_84 && ! res_NotLogicOP_85);
    res_AndLogicOP_83 = (res_AndLogicOP_83 && res_NotLogicOP_84);
    
    if(res_AndLogicOP_83){
    xorIndex_res_XorLogicOP_30 = (xorIndex_res_XorLogicOP_30 + 1);
    }
    
    res_XorLogicOP_30 = (res_XorLogicOP_30 && (xorIndex_res_XorLogicOP_30 == 1));
    res_ImpliesLogicOp_20 = (res_ImpliesLogicOp_20 && res_XorLogicOP_30);
    }
    res_OrLogicOP_19 = (res_OrLogicOP_19 || res_ImpliesLogicOp_20);
    bool res_AndLogicOP_86 = true;
    bool res_AndLogicOP_87 = true;
    res_AndLogicOP_87 = (res_AndLogicOP_87 && (L_P1__GetInMainc8(my_id) == c180));
    bool res_NotLogicOP_88 = true;
    res_NotLogicOP_88 = (res_NotLogicOP_88 && ! (Counter_GetValore(L_P1__GetMainc35(my_id)) == 1312u));
    res_AndLogicOP_87 = (res_AndLogicOP_87 && res_NotLogicOP_88);
    
    res_AndLogicOP_86 = (res_AndLogicOP_86 && res_AndLogicOP_87);
    bool res_NotLogicOP_89 = true;
    res_NotLogicOP_89 = (res_NotLogicOP_89 && ! (L_P1__GetParamMainc9(my_id) == avviox));
    res_AndLogicOP_86 = (res_AndLogicOP_86 && res_NotLogicOP_89);
    
    res_OrLogicOP_19 = (res_OrLogicOP_19 || res_AndLogicOP_86);
    
    res_ImpliesLogicOp_13 = (res_ImpliesLogicOp_13 && res_OrLogicOP_19);
    }
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_ImpliesLogicOp_13);
    bool res_AndLogicOP_90 = true;
    bool res_AndLogicOP_91 = true;
    bool res_NotLogicOP_92 = true;
    res_NotLogicOP_92 = (res_NotLogicOP_92 && ! Timer_Scaduto(L_P1__GetMainc31(my_id)));
    res_AndLogicOP_91 = (res_AndLogicOP_91 && res_NotLogicOP_92);
    bool res_NotLogicOP_93 = true;
    bool res_NotLogicOP_94 = true;
    res_NotLogicOP_94 = (res_NotLogicOP_94 && ! (L_P1__GetInMainc5(my_id) == false));
    res_NotLogicOP_93 = (res_NotLogicOP_93 && ! res_NotLogicOP_94);
    res_AndLogicOP_91 = (res_AndLogicOP_91 && res_NotLogicOP_93);
    
    res_AndLogicOP_90 = (res_AndLogicOP_90 && res_AndLogicOP_91);
    bool res_NotLogicOP_95 = true;
    res_NotLogicOP_95 = (res_NotLogicOP_95 && ! (L_P1__GetMainc25(my_id) == true));
    res_AndLogicOP_90 = (res_AndLogicOP_90 && res_NotLogicOP_95);
    
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_AndLogicOP_90);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_AndLogicOP_12);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *48,49,*  *,*  il controllo MainClass_C1_controllo_C2 sia  uguale a  True 
    //   *104,* o  che  *,*  il timer MainClass_C1_timer_T5 sia disattivo
    //   *104,* e  che  *36,*  il timer MainClass_C1_timer_T5 non sia scaduto
    bool res_OrLogicOP_96 = false;
    res_OrLogicOP_96 = (res_OrLogicOP_96 || (L_P1__GetInMainc5(my_id) == true));
    bool res_AndLogicOP_97 = true;
    res_AndLogicOP_97 = (res_AndLogicOP_97 && Timer_Disattivo(L_P1__GetMainc31(my_id)));
    bool res_NotLogicOP_98 = true;
    res_NotLogicOP_98 = (res_NotLogicOP_98 && ! Timer_Scaduto(L_P1__GetMainc31(my_id)));
    res_AndLogicOP_97 = (res_AndLogicOP_97 && res_NotLogicOP_98);
    
    res_OrLogicOP_96 = (res_OrLogicOP_96 || res_AndLogicOP_97);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_96);
    
    
    
    return res_AndLogicOP_0;
}


// Macro valorizzate

/*
    CNL corrispondente:
    
    { commento: {[}  se il controllo ConsDef è uguale a FALSE  commento: {34,} e  se il parametro MainClass_C1_parametro_P9 non è  diverso da  False  commento: {37,} o  se la variabile MainClass_C1_variabile_V10 non è  uguale a  True  commento: {109,} e  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  uguale a RossoGialloVerde commento: {38,} e  se il contatore MainClass_C1_contatore_Co4 non è  maggiore di  commento: {54,} 155 , assegna alla macro il valore c180
    
     commento: {46,} assegna alla macro il valore c180 commento: {],}
    }
*/
C1_Enumerat1 L_P1__Macro1(instance_id_t const my_id , bool argom3, C1_Enumerat4 argom4, C1_Enumerat2 argom5, C1_Enumerat1 argom6)
{
C1_Enumerat1 res_macro_val;
    
    //  *[*  se il controllo ConsDef è uguale a FALSE  *34,* e  se il parametro MainClass_C1_parametro_P9 non è  diverso da  False  *37,* o  se la variabile MainClass_C1_variabile_V10 non è  uguale a  True  *109,* e  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  uguale a RossoGialloVerde *38,* e  se il contatore MainClass_C1_contatore_Co4 non è  maggiore di  *54,* 155
    bool res_OrLogicOP_0 = false;
    bool res_AndLogicOP_1 = true;
    res_AndLogicOP_1 = (res_AndLogicOP_1 && (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_2 = true;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__GetParamMainc11(my_id) == false));
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! res_NotLogicOP_3);
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_2);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_1);
    bool res_AndLogicOP_4 = true;
    bool res_AndLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetMainc24(my_id) == true));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_6);
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetMainc17(my_id) == rossogiallo1));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_7);
    
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_AndLogicOP_5);
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (Counter_GetValore(L_P1__GetMainc34(my_id)) > 155u));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_8);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_4);
    
    if(res_OrLogicOP_0){
    
    res_macro_val = c180;
    }
    else{
    res_macro_val = c180;
    }
    return res_macro_val;
}

/*
    CNL corrispondente:
    
    { commento: {[}
     commento: {46,} assegna alla macro il valore avviox commento: {],}
    }
*/
C1_Enumerat4 L_P1__Macro2(instance_id_t const my_id , C1_Enumerat3 argom7, C1_Enumerat1 argom8, C1_Enumerat4 argom9, C1_Enumerat3 argom10, C1_Enumerat1 argom11, C1_Enumerat3 argom12)
{
return avviox;
}

/*
    CNL corrispondente:
    
    { commento: {[} commento: {35,}  se il controllo MainClass_C1_controllo_C2 è  diverso da  False  commento: {34,} o  se il parametro MainClass_C1_parametro_P1 è  diverso da avviox commento: {110,} e  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è disattivo commento: {109,} o  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  diverso da RossoGialloVerde commento: {35,} e  se il controllo MainClass_C1_controllo_C2 è  uguale a  True  , assegna alla macro il valore c180
    
     commento: {46,} assegna alla macro il valore c180 commento: {],}
    }
*/
C1_Enumerat1 L_P1__Macro3(instance_id_t const my_id , C1_Enumerat4 argom13, bool argom14, C1_Enumerat3 argom15, C1_Enumerat1 argom16, C1_Enumerat2 argom17)
{
C1_Enumerat1 res_macro_val;
    
    //  *[* *35,*  se il controllo MainClass_C1_controllo_C2 è  diverso da  False  *34,* o  se il parametro MainClass_C1_parametro_P1 è  diverso da avviox *110,* e  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è disattivo *109,* o  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  diverso da RossoGialloVerde *35,* e  se il controllo MainClass_C1_controllo_C2 è  uguale a  True
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (L_P1__GetInMainc5(my_id) == false));
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_NotLogicOP_2);
    bool res_AndLogicOP_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetParamMainc9(my_id) == avviox));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_4);
    res_AndLogicOP_3 = (res_AndLogicOP_3 && Timer_Disattivo(L_P1__GetMainc27(my_id)));
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_3);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_AndLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetMainc17(my_id) == rossogiallo1));
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! res_NotLogicOP_7);
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_6);
    res_AndLogicOP_5 = (res_AndLogicOP_5 && (L_P1__GetInMainc5(my_id) == true));
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_5);
    
    if(res_OrLogicOP_0){
    
    res_macro_val = c180;
    }
    else{
    res_macro_val = c180;
    }
    return res_macro_val;
}

/*
    CNL corrispondente:
    
    { commento: {[}
     commento: {46,} assegna alla macro il valore c180 commento: {],}
    }
*/
C1_Enumerat1 L_P1__Macro4(instance_id_t const my_id , C1_Enumerat4 argom18, C1_Enumerat2 argom19, C1_Enumerat1 argom20, C1_Enumerat1 argom21, C1_Enumerat1 argom22, C1_Enumerat3 argom23)
{
return c180;
}



