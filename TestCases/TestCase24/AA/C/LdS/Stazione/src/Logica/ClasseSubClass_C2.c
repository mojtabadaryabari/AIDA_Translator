// Codice del modello 'TestCase24', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#include "Logica/ClasseMainClass_C1.h"
#include "Logica/ClasseSubClass_C2.h"
#include "Logica/ClasseSubClass_C2_priv.h"
#include "config.h"
#include "scheduler.h"


// ********** Gestione comandi automatici **********

static size_t L_P1_C2_NumAutoCmds(instance_id_t const my_id)
{
    size_t n = 0u;
    if (L_P1__GetCAEvent7(my_id)) {
        ++n;
    }
    return n;
}


// ********** Gestione comandi manuali **********

static void L_P1_C2_InitCmdsResponse(instance_id_t const my_id)
{
    // for each manual command of L_P1_C2
    if (L_P1__GetInEvent8(my_id)) {
	    L_P1__SetOutEvent9(my_id, LDS_MANCMD_UNEXPECTED);
    } else {
        L_P1__SetOutEvent9(my_id, LDS_MANCMD_NOOP);
    }
}

static void L_P1_C2_SetExpectedCmdsResponse(instance_id_t const my_id, C2_Stateenu state)
{        
    switch (state) {
    case C2_St_state:
        // manual commands of L_P1_C2 that can be received in C2_St_state
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
static inline bool L_P1__Guard2(instance_id_t const my_id)
{
    return true;
}


/*
    CNL corrispondente:
     
    {
    Nessuna
    }
*/
static inline bool L_P1__Guard3(instance_id_t const my_id)
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
static inline void L_P1__Effec2(instance_id_t const my_id)
{
    
}


/*
    CNL corrispondente:
     
    {
    Nessuna
    }
*/
static inline void L_P1__Effec3(instance_id_t const my_id)
{
    
}



// ********** Definizione metodi **********

// Metodi standard

void L_P1_C2_Init(instance_id_t const my_id)
{
    // init variabili di stato
    L_P1__SetStato3(my_id, C2_St_Stato);
    L_P1__SetSubcl22(my_id, 0);
    L_P1__SetSubcl24(my_id, spento);
    L_P1__SetSubcl26(my_id, false);
    L_P1__SetSubcl28(my_id, false);
    L_P1__SetSubcl30(my_id, 0);
    L_P1__SetSubcl31(my_id, 0);
    L_P1__SetSubcl32(my_id, giallox);
    L_P1__SetSubcl33(my_id, giallox);
    L_P1__SetSubcl34(my_id, 0);
    // init controlli precedenti
    L_P1__SetSubcl19(my_id, false);
    L_P1__SetSubcl21(my_id, rossogiallo3);
    // init Timer e Counter
    Timer_AggmInit(L_P1__GetSubcl35(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl35_ID);
    Timer_Init(L_P1__GetSubcl35(my_id), 121000);
    Timer_AggmInit(L_P1__GetSubcl36(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl36_ID);
    Timer_Init(L_P1__GetSubcl36(my_id), 121000);
    Timer_AggmInit(L_P1__GetSubcl37(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl37_ID);
    Timer_Init(L_P1__GetSubcl37(my_id), 31000);
    Timer_AggmInit(L_P1__GetSubcl38(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl38_ID);
    Timer_Init(L_P1__GetSubcl38(my_id), 43000);
    Timer_AggmInit(L_P1__GetSubcl39(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl39_ID);
    Timer_Init(L_P1__GetSubcl39(my_id), 2542000);
    Timer_AggmInit(L_P1__GetSubcl40(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl40_ID);
    Timer_Init(L_P1__GetSubcl40(my_id), 5000);
    Timer_AggmInit(L_P1__GetSubcl41(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl41_ID);
    Timer_Init(L_P1__GetSubcl41(my_id), 4054000);
    Counter_AggmInit(L_P1__GetSubcl42(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl42_ID);
    Counter_Init(L_P1__GetSubcl42(my_id));
    // init response
    L_P1_C2_SetResponse(my_id, LDS_SCHED_NOP);

    // transizione iniziale
    if(L_P1__Guard2(my_id)) {
        L_P1_C2_SetState(my_id, C2_St_state);
	L_P1__Effec2(my_id);
    } else {
        STOP_EXECUTION(LOGIC_ERROR);
    }
    // init variabili precedenti
    L_P1__SetSubcl23(my_id, L_P1__GetSubcl22(my_id));
    L_P1__SetSubcl25(my_id, L_P1__GetSubcl24(my_id));
    L_P1__SetSubcl27(my_id, L_P1__GetSubcl26(my_id));
    L_P1__SetSubcl29(my_id, L_P1__GetSubcl28(my_id));
}

void L_P1_C2_Exec(instance_id_t const my_id, Phase const p)
{
    L_P1_C2_SetResponse(my_id, LDS_SCHED_NOP);
    switch (p) {

    case LDS_PHASE_MANUAL:
        // Reset risposte ai comandi manuali
        L_P1_C2_InitCmdsResponse(my_id);
	L_P1_C2_SetExpectedCmdsResponse(my_id, L_P1_C2_GetState(my_id));
        switch (L_P1_C2_GetState(my_id)) {

        case C2_St_state:
                { } // fine transizioni da state nella fase LDS_PHASE_MANUAL
            break;

        default:
            STOP_EXECUTION(LOGIC_ERROR);
            break;  // Needed for MISRA C syntactic compliance
        } // switch sugli stati chiuso
        break;
 

    case LDS_PHASE_STATE:

        switch (L_P1_C2_GetState(my_id)) {

        case C2_St_state:
            if (L_P1__Guard3(my_id)) {
                L_P1_C2_SetState(my_id, C2_St_state);
                L_P1__Effec3(my_id);				
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
        size_t auto_commands_before = L_P1_C2_NumAutoCmds(my_id);
        switch (L_P1_C2_GetState(my_id)) {

        case C2_St_state:
                { } // fine transizioni da state nella fase LDS_PHASE_AUTO
            break;

        default:
            STOP_EXECUTION(LOGIC_ERROR);
            break;  // Needed for MISRA C syntactic compliance
        } // switch sugli stati chiuso
        size_t auto_commands_after = L_P1_C2_NumAutoCmds(my_id);
        CHECK_GE(auto_commands_before, auto_commands_after);

        if ((auto_commands_after > 0u) && (auto_commands_before > auto_commands_after)) {
            L_P1_C2_SetResponse(my_id, LDS_SCHED_CONTINUE);
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

ExecResponse L_P1_C2_GExec(global_id_t const proc_id, Phase const p)
{
    CHECK_LT(GLOBAL_TO_L_P1_C2(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C2(proc_id);
    L_P1_C2_Exec(my_id, p);
    return L_P1_C2_GetResponse(my_id);
}

void L_P1_C2_GTick(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C2(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C2(proc_id);
    Timer_Exec(L_P1__GetSubcl35(my_id));
    Timer_Exec(L_P1__GetSubcl36(my_id));
    Timer_Exec(L_P1__GetSubcl37(my_id));
    Timer_Exec(L_P1__GetSubcl38(my_id));
    Timer_Exec(L_P1__GetSubcl39(my_id));
    Timer_Exec(L_P1__GetSubcl40(my_id));
    Timer_Exec(L_P1__GetSubcl41(my_id));
}

void L_P1_C2_GSetSafe(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C2(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C2(proc_id);
    L_P1__SetOutSubcl(my_id, rossogiallo2);
    L_P1__SetOutSubcl1(my_id, false);
    L_P1__SetOutSubcl2(my_id, false);
    L_P1__SetOutSubcl3(my_id, true);
}

void L_P1_C2_GUpdatePrev(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C2(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C2(proc_id);
    L_P1__SetSubcl19(my_id, L_P1__GetInSubcl18(my_id));
    L_P1__SetSubcl21(my_id, L_P1__GetInSubcl20(my_id));
    L_P1__SetSubcl23(my_id, L_P1__GetSubcl22(my_id));
    L_P1__SetSubcl25(my_id, L_P1__GetSubcl24(my_id));
    L_P1__SetSubcl27(my_id, L_P1__GetSubcl26(my_id));
    L_P1__SetSubcl29(my_id, L_P1__GetSubcl28(my_id));
}

// ********** Definizione macro **********

// Macro di effetto

/*
    CNL corrispondente:
    
    { commento: {34,}  se il parametro SubClass_C2_parametro_P4 non è  minore di  commento: {55,} 6 commento: {37,} e  se la variabile SubClass_C2_variabile_V6 non è  minore di  commento: {55,} 6 o  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} o  se il timer SubClass_C2_timer_T3 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE , commento: {66,} Assegna al comando SubClass_C2_comando_C5 il valore  False 
    
       
     commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L1 è  diverso da  commento: {56,}  state1  commento: {38,} o  se il contatore SubClass_C2_contatore_Co7 è  maggiore di  commento: {54,} 13, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V6 il valore 9
    
     ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V6 il valore 1
    
    
    
    }
*/
void L_P1__Macro10(instance_id_t const my_id )
{
//  *34,*  se il parametro SubClass_C2_parametro_P4 non è  minore di  *55,* 6 *37,* e  se la variabile SubClass_C2_variabile_V6 non è  minore di  *55,* 6 o  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  *36,* o  se il timer SubClass_C2_timer_T3 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE , *66,* Assegna al comando SubClass_C2_comando_C5 il valore  False
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_OrLogicOP_2 = false;
    bool res_AndLogicOP_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetParamSubcl15(my_id) < 6u));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_4);
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetSubcl34(my_id) < 6u));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_5);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_3);
    bool res_AndLogicOP_6 = true;
    res_AndLogicOP_6 = (res_AndLogicOP_6 && (L_P1__GetInConsd1(my_id) == false));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && (L_P1__GetInConsd1(my_id) == false));
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_6);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_OrLogicOP_2);
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! Timer_Disattivo(L_P1__GetSubcl38(my_id)));
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_NotLogicOP_7);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    res_OrLogicOP_0 = (res_OrLogicOP_0 || (L_P1__GetInConsd1(my_id) == false));
    
    if(res_OrLogicOP_0){
    
    L_P1__SetOutSubcl2(my_id,false);
    }
    //  *111,*  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L1 è  diverso da  *56,*  state1  *38,* o  se il contatore SubClass_C2_contatore_Co7 è  maggiore di  *54,* 13, *67,* Assegna alla variabile SubClass_C2_variabile_V6 il valore 9
    // ,altrimenti  *67,* Assegna alla variabile SubClass_C2_variabile_V6 il valore 1
    bool res_OrLogicOP_8 = false;
    bool res_ForAllPredicate_9 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl9Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl9(my_id,i);
    bool res_ImpliesLogicOp_10 = true;
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (L_P1_C1_GetState(it.mainc53) == C1_St_state));
    res_ImpliesLogicOp_10 = (res_ImpliesLogicOp_10 && res_NotLogicOP_11);
    res_ForAllPredicate_9 = res_ImpliesLogicOp_10;
    if(!res_ForAllPredicate_9) {break;}
    }
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_ForAllPredicate_9);
    res_OrLogicOP_8 = (res_OrLogicOP_8 || (Counter_GetValore(L_P1__GetSubcl42(my_id)) > 13u));
    
    if(res_OrLogicOP_8){
    
    L_P1__SetSubcl34(my_id,9u);
    }else{
    
    L_P1__SetSubcl34(my_id,1u);
    }
}


// Macro di verifica

/*
    CNL corrispondente:
     
    { commento: {63,} commento: {109,}  se il ripristino della variabile  SubClass_C2_restoreva_RV2 è  diverso da spento commento: {38,} o  se il contatore SubClass_C2_contatore_Co7 non è  uguale a  commento: {53,} 14 commento: {34,} e  se il parametro SubClass_C2_parametro_P2 è  minore di  commento: {55,} 4 commento: {35,} e  se il controllo SubClass_C2_controllo_C6 non è  uguale a spento e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
     commento: {62,} commento: {37,}  se la variabile SubClass_C2_variabile_V6 non è  maggiore di  commento: {54,} 7 commento: {34,} o  se il parametro SubClass_C2_parametro_P2 è  diverso da  commento: {56,} 5 commento: {37,} o  se la variabile SubClass_C2_variabile_V6 è  diverso da  commento: {56,} 5 commento: {34,} e  se il parametro SubClass_C2_parametro_P2 non è  uguale a  commento: {53,} 5 commento: {36,} e  se il timer SubClass_C2_timer_T9 è scaduto, Almeno una delle seguenti { 
     commento: {63,} commento: {38,}  se il contatore SubClass_C2_contatore_Co7 è  maggiore di  commento: {54,} 1413, Solo una delle seguenti { 
     commento: {63,} commento: {37,}  se la variabile SubClass_C2_variabile_V6 non è  uguale a  commento: {53,} 4 commento: {35,} o  se il controllo SubClass_C2_controllo_C8 non è  uguale a RossoGiallox commento: {38,} e  se il contatore SubClass_C2_contatore_Co7 non è  minore di  commento: {55,} 13054, Solo una delle seguenti { 
     commento: {62,} commento: {44,}  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C2_lista_L4 è  uguale a  False  commento: {36,} o  se il timer SubClass_C2_timer_T8 non è attivo, Almeno una delle seguenti { 
     commento: {63,}  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} e  se il timer SubClass_C2_timer_T8 non è scaduto commento: {35,} e  se il controllo SubClass_C2_controllo_C6 è  uguale a spento, Solo una delle seguenti { 
     commento: {63,} commento: {43,}  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L10 è disattivo commento: {35,} e  se il controllo SubClass_C2_controllo_C6 è  diverso da spento, Solo una delle seguenti { 
     commento: {62,} commento: {37,}  se la variabile SubClass_C2_variabile_V6 è  minore di  commento: {55,} 8 commento: {34,} e  se il parametro SubClass_C2_parametro_P5 è  diverso da  commento: {56,} 2 commento: {35,} e  se il controllo SubClass_C2_controllo_C7 è  diverso da  True  commento: {38,} e  se il contatore SubClass_C2_contatore_Co7 è  diverso da  commento: {56,} 142, Almeno una delle seguenti { 
     commento: {62,}  se il controllo ConsDef  è  uguale a FALSE ,  commento: {42,}  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  commento: {105,} è  uguale a c120x, commento: {88,} quando  commento: {111,}   lo stato del campo  MainClass_C1     commento: {105,} è  uguale a  commento: {53,}  state1  o  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro SubClass_C2_parametro_P5 è  minore di  commento: {55,} 6 commento: {37,} o  se la variabile SubClass_C2_variabile_V6 non è  uguale a  commento: {53,} 5 commento: {34,} e  se il parametro SubClass_C2_parametro_P4 è  minore di  commento: {55,} 3 commento: {36,} e  se il timer SubClass_C2_timer_T4 è scaduto, Almeno una delle seguenti { 
     commento: {61,} commento: {36,}  se il timer SubClass_C2_timer_T4 è scaduto, Tutte le seguenti { 
     commento: {61,}  se il ripristino dello stato  è  uguale a  commento: {53,}  state1  commento: {107,} commento: {37,} e  se la variabile SubClass_C2_variabile_V6 non è  maggiore di  commento: {54,} 1 commento: {35,} e  se il controllo SubClass_C2_controllo_C8 è  diverso da RossoGiallox commento: {36,} o  se il timer SubClass_C2_timer_T8 è attivo, Tutte le seguenti { 
     commento: {61,} commento: {38,}  se il contatore SubClass_C2_contatore_Co7 è  minore di  commento: {55,} 1113 commento: {36,} o  se il timer SubClass_C2_timer_T3 è disattivo commento: {34,} o  se il parametro SubClass_C2_parametro_P9 è  minore di  commento: {55,} 3 commento: {36,} e  se il timer SubClass_C2_timer_T8 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} o  se il controllo SubClass_C2_controllo_C7 è  uguale a  True , Tutte le seguenti { 
     commento: {61,} commento: {37,}  se la variabile SubClass_C2_variabile_V6 non è  uguale a  commento: {53,} 9, Tutte le seguenti { 
     commento: {62,} commento: {34,}  se lo stato  non è  uguale a  commento: {53,}  state1  commento: {106,} commento: {34,} e  se il parametro SubClass_C2_parametro_P2 è  maggiore di  commento: {54,} 6 commento: {37,} o  se la variabile SubClass_C2_variabile_V6 è  maggiore di  commento: {54,} 5, Almeno una delle seguenti { 
     commento: {63,} commento: {41,}  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  commento: {105,} è  minore di  commento: {55,} 9 commento: {34,} o  se il parametro SubClass_C2_parametro_P2 è  maggiore di  commento: {54,} 9 commento: {36,} e  se il timer SubClass_C2_timer_T1 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro SubClass_C2_parametro_P2 è  diverso da  commento: {56,} 2 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
     commento: {43,}  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L1 è disattivo commento: {36,} e  se il timer SubClass_C2_timer_T4 è disattivo commento: {37,} e  se la variabile SubClass_C2_variabile_V6 è  minore di  commento: {55,} 10 commento: {34,} e  se il parametro SubClass_C2_parametro_P2 è  diverso da  commento: {56,} 5 commento: {38,} e  se il contatore SubClass_C2_contatore_Co7 è  uguale a  commento: {53,} 122, Verifica che   commento: {48,50,}  commento: {,}  la variabile SubClass_C2_variabile_V6 sia  minore di  commento: {55,} 5
     commento: {104,} e  che  commento: {37,}  la variabile SubClass_C2_variabile_V6 non sia  diverso da  commento: {56,} 9
     commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
    
    
     } Verifica che   commento: {48,50,51,}  commento: {,}  il contatore SubClass_C2_contatore_Co7 sia  uguale a  commento: {53,} 151
     commento: {104,} e  che  commento: {,}  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento
     commento: {104,} e  che  commento: {,}  la variabile SubClass_C2_variabile_V6 sia  diverso da  commento: {56,} 3
     commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
    
    
     } Verifica che   commento: {48,49,}   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} o  che  commento: {,}  il timer SubClass_C2_timer_T4 sia disattivo
    
    
     } Verifica che   commento: {48,49,50,}   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} o  che  commento: {,}  la variabile SubClass_C2_variabile_V6 sia  diverso da  commento: {56,} 6
     commento: {104,} o  che  commento: {,}  il timer SubClass_C2_timer_T8 sia scaduto
    
    
     } Verifica che   commento: {47,49,}  commento: {34,}  il parametro SubClass_C2_parametro_P2 sia  maggiore di  commento: {54,} 4
     commento: {104,} e  che  commento: {,}  il timer SubClass_C2_timer_T9 non sia disattivo
     commento: {104,} o  che  commento: {36,}  il timer SubClass_C2_timer_T4 sia disattivo
    
    
     } Verifica che   commento: {47,}  commento: {34,}  il parametro SubClass_C2_parametro_P2 sia  minore di  commento: {55,} 1
    
    
     } Verifica che   commento: {48,}  commento: {,}  il controllo SubClass_C2_controllo_C8 non sia  uguale a RossoGiallox
    
    
     } Verifica che   commento: {48,49,50,}  commento: {,}  il timer SubClass_C2_timer_T1 non sia disattivo
     commento: {104,} o  che  commento: {,}  il controllo SubClass_C2_controllo_C8 non sia  diverso da RossoGiallox
     commento: {104,} e  che  commento: {,}  la variabile SubClass_C2_variabile_V6 sia  diverso da  commento: {56,} 8
    
    
     } Verifica che   commento: {47,48,49,50,51,}  commento: {,}  il timer SubClass_C2_timer_T8 non sia scaduto
     commento: {104,} o  che  commento: {,}  il controllo SubClass_C2_controllo_C8 non sia  diverso da RossoGiallox
     commento: {104,} o  che  commento: {,}  la variabile SubClass_C2_variabile_V6 non sia  uguale a  commento: {53,} 8
     commento: {104,} e  che  commento: {34,}  il parametro SubClass_C2_parametro_P2 non sia  minore di  commento: {55,} 2
     commento: {104,} o  che  commento: {,}  il contatore SubClass_C2_contatore_Co7 non sia  minore di  commento: {55,} 13305
    
    
     } Verifica che   commento: {47,48,50,}   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} o  che  commento: {34,}  il parametro SubClass_C2_parametro_P5 non sia  maggiore di  commento: {54,} 7
     commento: {104,} e  che  commento: {,}  la variabile SubClass_C2_variabile_V6 non sia  minore di  commento: {55,} 4
     commento: {104,} e  che  commento: {,}  il controllo SubClass_C2_controllo_C8 sia  diverso da RossoGiallox
     commento: {104,} e  che  commento: {35,}  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento
     commento: {104,} o  che  commento: {34,}  il parametro SubClass_C2_parametro_P4 non sia  diverso da  commento: {56,} 10
    
    
     } Verifica che   commento: {48,}  commento: {,}  il controllo SubClass_C2_controllo_C8 non sia  diverso da RossoGiallox
     commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} o  che  commento: {35,}  il controllo SubClass_C2_controllo_C6 sia  uguale a spento
     commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
    
    
     } Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
    
    
     } Verifica che   commento: {48,}  commento: {,}  il controllo SubClass_C2_controllo_C3 non sia  diverso da  False 
     commento: {104,} e  che  commento: {35,}  il controllo SubClass_C2_controllo_C6 non sia  diverso da spento
     commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
    
    
     } Verifica che   commento: {47,50,}  commento: {,}  la variabile SubClass_C2_variabile_V6 non sia  diverso da  commento: {56,} 7
     commento: {104,} e  che  commento: {34,}  il parametro SubClass_C2_parametro_P2 non sia  uguale a  commento: {53,} 8
    
    
     } Verifica che   commento: {47,48,49,51,}  commento: {,}  il contatore SubClass_C2_contatore_Co7 non sia  minore di  commento: {55,} 12
     commento: {104,} e  che  commento: {,}  il timer SubClass_C2_timer_T9 non sia disattivo
     commento: {104,} o  che  commento: {,}  il controllo SubClass_C2_controllo_C8 non sia  uguale a RossoGiallox
     commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} o  che  commento: {34,}  il parametro SubClass_C2_parametro_P2 non sia  maggiore di  commento: {54,} 9
    
    
     } Verifica che   commento: {50,51,}  commento: {,}  il contatore SubClass_C2_contatore_Co7 sia  maggiore di  commento: {54,} 114
     commento: {104,} e  che  commento: {,}  la variabile SubClass_C2_variabile_V6 sia  minore di  commento: {55,} 1
     commento: {104,} o  che  commento: {38,}  il contatore SubClass_C2_contatore_Co7 non sia  minore di  commento: {55,} 132
    
    
    }
*/
bool L_P1__Macro12(instance_id_t const my_id )
{
bool res_AndLogicOP_0 = true;
    
    //  *63,* *109,*  se il ripristino della variabile  SubClass_C2_restoreva_RV2 è  diverso da spento *38,* o  se il contatore SubClass_C2_contatore_Co7 non è  uguale a  *53,* 14 *34,* e  se il parametro SubClass_C2_parametro_P2 è  minore di  *55,* 4 *35,* e  se il controllo SubClass_C2_controllo_C6 non è  uguale a spento e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
    //   *62,* *37,*  se la variabile SubClass_C2_variabile_V6 non è  maggiore di  *54,* 7 *34,* o  se il parametro SubClass_C2_parametro_P2 è  diverso da  *56,* 5 *37,* o  se la variabile SubClass_C2_variabile_V6 è  diverso da  *56,* 5 *34,* e  se il parametro SubClass_C2_parametro_P2 non è  uguale a  *53,* 5 *36,* e  se il timer SubClass_C2_timer_T9 è scaduto, Almeno una delle seguenti { 
    //   *63,* *38,*  se il contatore SubClass_C2_contatore_Co7 è  maggiore di  *54,* 1413, Solo una delle seguenti { 
    //   *63,* *37,*  se la variabile SubClass_C2_variabile_V6 non è  uguale a  *53,* 4 *35,* o  se il controllo SubClass_C2_controllo_C8 non è  uguale a RossoGiallox *38,* e  se il contatore SubClass_C2_contatore_Co7 non è  minore di  *55,* 13054, Solo una delle seguenti { 
    //   *62,* *44,*  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C2_lista_L4 è  uguale a  False  *36,* o  se il timer SubClass_C2_timer_T8 non è attivo, Almeno una delle seguenti { 
    //   *63,*  se il controllo ConsDef  è  uguale a FALSE  *36,* e  se il timer SubClass_C2_timer_T8 non è scaduto *35,* e  se il controllo SubClass_C2_controllo_C6 è  uguale a spento, Solo una delle seguenti { 
    //   *63,* *43,*  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L10 è disattivo *35,* e  se il controllo SubClass_C2_controllo_C6 è  diverso da spento, Solo una delle seguenti { 
    //   *62,* *37,*  se la variabile SubClass_C2_variabile_V6 è  minore di  *55,* 8 *34,* e  se il parametro SubClass_C2_parametro_P5 è  diverso da  *56,* 2 *35,* e  se il controllo SubClass_C2_controllo_C7 è  diverso da  True  *38,* e  se il contatore SubClass_C2_contatore_Co7 è  diverso da  *56,* 142, Almeno una delle seguenti { 
    //   *62,*  se il controllo ConsDef  è  uguale a FALSE ,  *42,*  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  *105,* è  uguale a c120x, *88,* quando  *111,*   lo stato del campo  MainClass_C1     *105,* è  uguale a  *53,*  state1  o  se il controllo ConsDef  è  uguale a FALSE  *34,* e  se il parametro SubClass_C2_parametro_P5 è  minore di  *55,* 6 *37,* o  se la variabile SubClass_C2_variabile_V6 non è  uguale a  *53,* 5 *34,* e  se il parametro SubClass_C2_parametro_P4 è  minore di  *55,* 3 *36,* e  se il timer SubClass_C2_timer_T4 è scaduto, Almeno una delle seguenti { 
    //   *61,* *36,*  se il timer SubClass_C2_timer_T4 è scaduto, Tutte le seguenti { 
    //   *61,*  se il ripristino dello stato  è  uguale a  *53,*  state1  *107,* *37,* e  se la variabile SubClass_C2_variabile_V6 non è  maggiore di  *54,* 1 *35,* e  se il controllo SubClass_C2_controllo_C8 è  diverso da RossoGiallox *36,* o  se il timer SubClass_C2_timer_T8 è attivo, Tutte le seguenti { 
    //   *61,* *38,*  se il contatore SubClass_C2_contatore_Co7 è  minore di  *55,* 1113 *36,* o  se il timer SubClass_C2_timer_T3 è disattivo *34,* o  se il parametro SubClass_C2_parametro_P9 è  minore di  *55,* 3 *36,* e  se il timer SubClass_C2_timer_T8 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  *35,* o  se il controllo SubClass_C2_controllo_C7 è  uguale a  True , Tutte le seguenti { 
    //   *61,* *37,*  se la variabile SubClass_C2_variabile_V6 non è  uguale a  *53,* 9, Tutte le seguenti { 
    //   *62,* *34,*  se lo stato  non è  uguale a  *53,*  state1  *106,* *34,* e  se il parametro SubClass_C2_parametro_P2 è  maggiore di  *54,* 6 *37,* o  se la variabile SubClass_C2_variabile_V6 è  maggiore di  *54,* 5, Almeno una delle seguenti { 
    //   *63,* *41,*  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  *105,* è  minore di  *55,* 9 *34,* o  se il parametro SubClass_C2_parametro_P2 è  maggiore di  *54,* 9 *36,* e  se il timer SubClass_C2_timer_T1 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE  *34,* e  se il parametro SubClass_C2_parametro_P2 è  diverso da  *56,* 2 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
    //   *43,*  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L1 è disattivo *36,* e  se il timer SubClass_C2_timer_T4 è disattivo *37,* e  se la variabile SubClass_C2_variabile_V6 è  minore di  *55,* 10 *34,* e  se il parametro SubClass_C2_parametro_P2 è  diverso da  *56,* 5 *38,* e  se il contatore SubClass_C2_contatore_Co7 è  uguale a  *53,* 122, Verifica che   *48,50,*  *,*  la variabile SubClass_C2_variabile_V6 sia  minore di  *55,* 5
    //   *104,* e  che  *37,*  la variabile SubClass_C2_variabile_V6 non sia  diverso da  *56,* 9
    //   *104,* o  che   il controllo ConsDef  sia  uguale a FALSE 
    //   } Verifica che   *48,50,51,*  *,*  il contatore SubClass_C2_contatore_Co7 sia  uguale a  *53,* 151
    //   *104,* e  che  *,*  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento
    //   *104,* e  che  *,*  la variabile SubClass_C2_variabile_V6 sia  diverso da  *56,* 3
    //   *104,* e  che   il controllo ConsDef  sia  uguale a FALSE 
    //   } Verifica che   *48,49,*   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* o  che   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* o  che  *,*  il timer SubClass_C2_timer_T4 sia disattivo
    //   } Verifica che   *48,49,50,*   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* o  che  *,*  la variabile SubClass_C2_variabile_V6 sia  diverso da  *56,* 6
    //   *104,* o  che  *,*  il timer SubClass_C2_timer_T8 sia scaduto
    //   } Verifica che   *47,49,*  *34,*  il parametro SubClass_C2_parametro_P2 sia  maggiore di  *54,* 4
    //   *104,* e  che  *,*  il timer SubClass_C2_timer_T9 non sia disattivo
    //   *104,* o  che  *36,*  il timer SubClass_C2_timer_T4 sia disattivo
    //   } Verifica che   *47,*  *34,*  il parametro SubClass_C2_parametro_P2 sia  minore di  *55,* 1
    //   } Verifica che   *48,*  *,*  il controllo SubClass_C2_controllo_C8 non sia  uguale a RossoGiallox
    //   } Verifica che   *48,49,50,*  *,*  il timer SubClass_C2_timer_T1 non sia disattivo
    //   *104,* o  che  *,*  il controllo SubClass_C2_controllo_C8 non sia  diverso da RossoGiallox
    //   *104,* e  che  *,*  la variabile SubClass_C2_variabile_V6 sia  diverso da  *56,* 8
    //   } Verifica che   *47,48,49,50,51,*  *,*  il timer SubClass_C2_timer_T8 non sia scaduto
    //   *104,* o  che  *,*  il controllo SubClass_C2_controllo_C8 non sia  diverso da RossoGiallox
    //   *104,* o  che  *,*  la variabile SubClass_C2_variabile_V6 non sia  uguale a  *53,* 8
    //   *104,* e  che  *34,*  il parametro SubClass_C2_parametro_P2 non sia  minore di  *55,* 2
    //   *104,* o  che  *,*  il contatore SubClass_C2_contatore_Co7 non sia  minore di  *55,* 13305
    //   } Verifica che   *47,48,50,*   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* o  che  *34,*  il parametro SubClass_C2_parametro_P5 non sia  maggiore di  *54,* 7
    //   *104,* e  che  *,*  la variabile SubClass_C2_variabile_V6 non sia  minore di  *55,* 4
    //   *104,* e  che  *,*  il controllo SubClass_C2_controllo_C8 sia  diverso da RossoGiallox
    //   *104,* e  che  *35,*  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento
    //   *104,* o  che  *34,*  il parametro SubClass_C2_parametro_P4 non sia  diverso da  *56,* 10
    //   } Verifica che   *48,*  *,*  il controllo SubClass_C2_controllo_C8 non sia  diverso da RossoGiallox
    //   *104,* e  che   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* o  che  *35,*  il controllo SubClass_C2_controllo_C6 sia  uguale a spento
    //   *104,* e  che   il controllo ConsDef  sia  uguale a FALSE 
    //   } Verifica che   *48,*   il controllo ConsDef  sia  uguale a FALSE 
    //   } Verifica che   *48,*  *,*  il controllo SubClass_C2_controllo_C3 non sia  diverso da  False 
    //   *104,* e  che  *35,*  il controllo SubClass_C2_controllo_C6 non sia  diverso da spento
    //   *104,* e  che   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* e  che   il controllo ConsDef  sia  uguale a FALSE 
    //   } Verifica che   *47,50,*  *,*  la variabile SubClass_C2_variabile_V6 non sia  diverso da  *56,* 7
    //   *104,* e  che  *34,*  il parametro SubClass_C2_parametro_P2 non sia  uguale a  *53,* 8
    //   } Verifica che   *47,48,49,51,*  *,*  il contatore SubClass_C2_contatore_Co7 non sia  minore di  *55,* 12
    //   *104,* e  che  *,*  il timer SubClass_C2_timer_T9 non sia disattivo
    //   *104,* o  che  *,*  il controllo SubClass_C2_controllo_C8 non sia  uguale a RossoGiallox
    //   *104,* e  che   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* o  che  *34,*  il parametro SubClass_C2_parametro_P2 non sia  maggiore di  *54,* 9
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__GetSubcl33(my_id) == spento));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_3);
    bool res_AndLogicOP_4 = true;
    bool res_AndLogicOP_5 = true;
    bool res_AndLogicOP_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (Counter_GetValore(L_P1__GetSubcl42(my_id)) == 14u));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_7);
    res_AndLogicOP_6 = (res_AndLogicOP_6 && (L_P1__GetParamSubcl14(my_id) < 4u));
    
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_AndLogicOP_6);
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetInSubcl5(my_id) == spento));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_8);
    
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_AndLogicOP_5);
    res_AndLogicOP_4 = (res_AndLogicOP_4 && (L_P1__GetInConsd1(my_id) == false));
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_4);
    
    if(res_OrLogicOP_2){
    bool res_XorLogicOP_9 = true;
    int xorIndex_res_XorLogicOP_9 = 0;
    bool res_ImpliesLogicOp_10 = true;
    bool res_OrLogicOP_11 = false;
    bool res_OrLogicOP_12 = false;
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (L_P1__GetSubcl34(my_id) > 7u));
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_NotLogicOP_13);
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1__GetParamSubcl14(my_id) == 5u));
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_NotLogicOP_14);
    
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_OrLogicOP_12);
    bool res_AndLogicOP_15 = true;
    bool res_AndLogicOP_16 = true;
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! (L_P1__GetSubcl34(my_id) == 5u));
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_NotLogicOP_17);
    bool res_NotLogicOP_18 = true;
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! (L_P1__GetParamSubcl14(my_id) == 5u));
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_NotLogicOP_18);
    
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_AndLogicOP_16);
    res_AndLogicOP_15 = (res_AndLogicOP_15 && Timer_Scaduto(L_P1__GetSubcl41(my_id)));
    
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_AndLogicOP_15);
    
    if(res_OrLogicOP_11){
    bool res_OrLogicOP_19 = false;
    bool res_ImpliesLogicOp_20 = true;
    if((Counter_GetValore(L_P1__GetSubcl42(my_id)) > 1413u)){
    bool res_XorLogicOP_21 = true;
    int xorIndex_res_XorLogicOP_21 = 0;
    bool res_ImpliesLogicOp_22 = true;
    bool res_OrLogicOP_23 = false;
    bool res_NotLogicOP_24 = true;
    res_NotLogicOP_24 = (res_NotLogicOP_24 && ! (L_P1__GetSubcl34(my_id) == 4u));
    res_OrLogicOP_23 = (res_OrLogicOP_23 || res_NotLogicOP_24);
    bool res_AndLogicOP_25 = true;
    bool res_NotLogicOP_26 = true;
    res_NotLogicOP_26 = (res_NotLogicOP_26 && ! (L_P1__GetInSubcl7(my_id) == rossogiallo3));
    res_AndLogicOP_25 = (res_AndLogicOP_25 && res_NotLogicOP_26);
    bool res_NotLogicOP_27 = true;
    res_NotLogicOP_27 = (res_NotLogicOP_27 && ! (Counter_GetValore(L_P1__GetSubcl42(my_id)) < 13054u));
    res_AndLogicOP_25 = (res_AndLogicOP_25 && res_NotLogicOP_27);
    
    res_OrLogicOP_23 = (res_OrLogicOP_23 || res_AndLogicOP_25);
    
    if(res_OrLogicOP_23){
    bool res_XorLogicOP_28 = true;
    int xorIndex_res_XorLogicOP_28 = 0;
    bool res_ImpliesLogicOp_29 = true;
    bool res_OrLogicOP_30 = false;
    bool res_ForAllPredicate_31 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl12Length(my_id); ++i)
    {
    L_P1__Recor1 it = L_P1__GetRecSubcl12(my_id,i);
    bool res_ImpliesLogicOp_32 = true;
    res_ImpliesLogicOp_32 = (res_ImpliesLogicOp_32 && (L_P1__GetMainc38(it.mainc54) == false));
    res_ForAllPredicate_31 = res_ImpliesLogicOp_32;
    if(!res_ForAllPredicate_31) {break;}
    }
    res_OrLogicOP_30 = (res_OrLogicOP_30 || res_ForAllPredicate_31);
    bool res_NotLogicOP_33 = true;
    res_NotLogicOP_33 = (res_NotLogicOP_33 && ! Timer_Attivo(L_P1__GetSubcl40(my_id)));
    res_OrLogicOP_30 = (res_OrLogicOP_30 || res_NotLogicOP_33);
    
    if(res_OrLogicOP_30){
    bool res_OrLogicOP_34 = false;
    bool res_ImpliesLogicOp_35 = true;
    bool res_AndLogicOP_36 = true;
    bool res_AndLogicOP_37 = true;
    res_AndLogicOP_37 = (res_AndLogicOP_37 && (L_P1__GetInConsd1(my_id) == false));
    bool res_NotLogicOP_38 = true;
    res_NotLogicOP_38 = (res_NotLogicOP_38 && ! Timer_Scaduto(L_P1__GetSubcl40(my_id)));
    res_AndLogicOP_37 = (res_AndLogicOP_37 && res_NotLogicOP_38);
    
    res_AndLogicOP_36 = (res_AndLogicOP_36 && res_AndLogicOP_37);
    res_AndLogicOP_36 = (res_AndLogicOP_36 && (L_P1__GetInSubcl5(my_id) == spento));
    
    if(res_AndLogicOP_36){
    bool res_XorLogicOP_39 = true;
    int xorIndex_res_XorLogicOP_39 = 0;
    bool res_ImpliesLogicOp_40 = true;
    bool res_AndLogicOP_41 = true;
    bool res_ForAllPredicate_42 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl10Length(my_id); ++i)
    {
    L_P1__Recor1 it = L_P1__GetRecSubcl10(my_id,i);
    bool res_ImpliesLogicOp_43 = true;
    res_ImpliesLogicOp_43 = (res_ImpliesLogicOp_43 && Timer_Disattivo(L_P1__GetMainc47(it.mainc54)));
    res_ForAllPredicate_42 = res_ImpliesLogicOp_43;
    if(!res_ForAllPredicate_42) {break;}
    }
    res_AndLogicOP_41 = (res_AndLogicOP_41 && res_ForAllPredicate_42);
    bool res_NotLogicOP_44 = true;
    res_NotLogicOP_44 = (res_NotLogicOP_44 && ! (L_P1__GetInSubcl5(my_id) == spento));
    res_AndLogicOP_41 = (res_AndLogicOP_41 && res_NotLogicOP_44);
    
    if(res_AndLogicOP_41){
    bool res_XorLogicOP_45 = true;
    int xorIndex_res_XorLogicOP_45 = 0;
    bool res_ImpliesLogicOp_46 = true;
    bool res_AndLogicOP_47 = true;
    bool res_AndLogicOP_48 = true;
    bool res_AndLogicOP_49 = true;
    res_AndLogicOP_49 = (res_AndLogicOP_49 && (L_P1__GetSubcl34(my_id) < 8u));
    bool res_NotLogicOP_50 = true;
    res_NotLogicOP_50 = (res_NotLogicOP_50 && ! (L_P1__GetParamSubcl16(my_id) == 2u));
    res_AndLogicOP_49 = (res_AndLogicOP_49 && res_NotLogicOP_50);
    
    res_AndLogicOP_48 = (res_AndLogicOP_48 && res_AndLogicOP_49);
    bool res_NotLogicOP_51 = true;
    res_NotLogicOP_51 = (res_NotLogicOP_51 && ! (L_P1__GetInSubcl6(my_id) == true));
    res_AndLogicOP_48 = (res_AndLogicOP_48 && res_NotLogicOP_51);
    
    res_AndLogicOP_47 = (res_AndLogicOP_47 && res_AndLogicOP_48);
    bool res_NotLogicOP_52 = true;
    res_NotLogicOP_52 = (res_NotLogicOP_52 && ! (Counter_GetValore(L_P1__GetSubcl42(my_id)) == 142u));
    res_AndLogicOP_47 = (res_AndLogicOP_47 && res_NotLogicOP_52);
    
    if(res_AndLogicOP_47){
    bool res_OrLogicOP_53 = false;
    bool res_ImpliesLogicOp_54 = true;
    bool res_OrLogicOP_55 = false;
    bool res_OrLogicOP_56 = false;
    bool res_AndLogicOP_57 = true;
    res_AndLogicOP_57 = (res_AndLogicOP_57 && (L_P1__GetInConsd1(my_id) == false));
    bool res_ForAllPredicateNotEmpty_58 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl12Length(my_id); ++i)
    {
    L_P1__Recor1 it = L_P1__GetRecSubcl12(my_id,i);
    bool res_ImpliesLogicOp_59 = true;
    if((L_P1_C1_GetState(it.mainc54) == C1_St_state)){
    res_ImpliesLogicOp_59 = (res_ImpliesLogicOp_59 && (L_P1__GetInMainc6(it.mainc54) == c120x));
    res_ForAllPredicateNotEmpty_58 = res_ImpliesLogicOp_59;
    if(!res_ForAllPredicateNotEmpty_58) {break;}
    }
    }
    res_AndLogicOP_57 = (res_AndLogicOP_57 && res_ForAllPredicateNotEmpty_58);
    
    res_OrLogicOP_56 = (res_OrLogicOP_56 || res_AndLogicOP_57);
    bool res_AndLogicOP_60 = true;
    res_AndLogicOP_60 = (res_AndLogicOP_60 && (L_P1__GetInConsd1(my_id) == false));
    res_AndLogicOP_60 = (res_AndLogicOP_60 && (L_P1__GetParamSubcl16(my_id) < 6u));
    
    res_OrLogicOP_56 = (res_OrLogicOP_56 || res_AndLogicOP_60);
    
    res_OrLogicOP_55 = (res_OrLogicOP_55 || res_OrLogicOP_56);
    bool res_AndLogicOP_61 = true;
    bool res_AndLogicOP_62 = true;
    bool res_NotLogicOP_63 = true;
    res_NotLogicOP_63 = (res_NotLogicOP_63 && ! (L_P1__GetSubcl34(my_id) == 5u));
    res_AndLogicOP_62 = (res_AndLogicOP_62 && res_NotLogicOP_63);
    res_AndLogicOP_62 = (res_AndLogicOP_62 && (L_P1__GetParamSubcl15(my_id) < 3u));
    
    res_AndLogicOP_61 = (res_AndLogicOP_61 && res_AndLogicOP_62);
    res_AndLogicOP_61 = (res_AndLogicOP_61 && Timer_Scaduto(L_P1__GetSubcl39(my_id)));
    
    res_OrLogicOP_55 = (res_OrLogicOP_55 || res_AndLogicOP_61);
    
    if(res_OrLogicOP_55){
    bool res_OrLogicOP_64 = false;
    bool res_ImpliesLogicOp_65 = true;
    if(Timer_Scaduto(L_P1__GetSubcl39(my_id))){
    bool res_AndLogicOP_66 = true;
    bool res_ImpliesLogicOp_67 = true;
    bool res_OrLogicOP_68 = false;
    bool res_AndLogicOP_69 = true;
    bool res_AndLogicOP_70 = true;
    res_AndLogicOP_70 = (res_AndLogicOP_70 && (L_P1__GetStato3(my_id) == C2_St_state));
    bool res_NotLogicOP_71 = true;
    res_NotLogicOP_71 = (res_NotLogicOP_71 && ! (L_P1__GetSubcl34(my_id) > 1u));
    res_AndLogicOP_70 = (res_AndLogicOP_70 && res_NotLogicOP_71);
    
    res_AndLogicOP_69 = (res_AndLogicOP_69 && res_AndLogicOP_70);
    bool res_NotLogicOP_72 = true;
    res_NotLogicOP_72 = (res_NotLogicOP_72 && ! (L_P1__GetInSubcl7(my_id) == rossogiallo3));
    res_AndLogicOP_69 = (res_AndLogicOP_69 && res_NotLogicOP_72);
    
    res_OrLogicOP_68 = (res_OrLogicOP_68 || res_AndLogicOP_69);
    res_OrLogicOP_68 = (res_OrLogicOP_68 || Timer_Attivo(L_P1__GetSubcl40(my_id)));
    
    if(res_OrLogicOP_68){
    bool res_AndLogicOP_73 = true;
    bool res_ImpliesLogicOp_74 = true;
    bool res_OrLogicOP_75 = false;
    bool res_OrLogicOP_76 = false;
    bool res_OrLogicOP_77 = false;
    res_OrLogicOP_77 = (res_OrLogicOP_77 || (Counter_GetValore(L_P1__GetSubcl42(my_id)) < 1113u));
    res_OrLogicOP_77 = (res_OrLogicOP_77 || Timer_Disattivo(L_P1__GetSubcl38(my_id)));
    
    res_OrLogicOP_76 = (res_OrLogicOP_76 || res_OrLogicOP_77);
    bool res_AndLogicOP_78 = true;
    bool res_AndLogicOP_79 = true;
    res_AndLogicOP_79 = (res_AndLogicOP_79 && (L_P1__GetParamSubcl17(my_id) < 3u));
    bool res_NotLogicOP_80 = true;
    res_NotLogicOP_80 = (res_NotLogicOP_80 && ! Timer_Scaduto(L_P1__GetSubcl40(my_id)));
    res_AndLogicOP_79 = (res_AndLogicOP_79 && res_NotLogicOP_80);
    
    res_AndLogicOP_78 = (res_AndLogicOP_78 && res_AndLogicOP_79);
    res_AndLogicOP_78 = (res_AndLogicOP_78 && (L_P1__GetInConsd1(my_id) == false));
    
    res_OrLogicOP_76 = (res_OrLogicOP_76 || res_AndLogicOP_78);
    
    res_OrLogicOP_75 = (res_OrLogicOP_75 || res_OrLogicOP_76);
    res_OrLogicOP_75 = (res_OrLogicOP_75 || (L_P1__GetInSubcl6(my_id) == true));
    
    if(res_OrLogicOP_75){
    bool res_AndLogicOP_81 = true;
    bool res_ImpliesLogicOp_82 = true;
    bool res_NotLogicOP_83 = true;
    res_NotLogicOP_83 = (res_NotLogicOP_83 && ! (L_P1__GetSubcl34(my_id) == 9u));
    if(res_NotLogicOP_83){
    bool res_AndLogicOP_84 = true;
    bool res_ImpliesLogicOp_85 = true;
    bool res_OrLogicOP_86 = false;
    bool res_AndLogicOP_87 = true;
    bool res_NotLogicOP_88 = true;
    res_NotLogicOP_88 = (res_NotLogicOP_88 && ! (L_P1_C2_GetState(my_id) == C2_St_state));
    res_AndLogicOP_87 = (res_AndLogicOP_87 && res_NotLogicOP_88);
    res_AndLogicOP_87 = (res_AndLogicOP_87 && (L_P1__GetParamSubcl14(my_id) > 6u));
    
    res_OrLogicOP_86 = (res_OrLogicOP_86 || res_AndLogicOP_87);
    res_OrLogicOP_86 = (res_OrLogicOP_86 || (L_P1__GetSubcl34(my_id) > 5u));
    
    if(res_OrLogicOP_86){
    bool res_OrLogicOP_89 = false;
    bool res_ImpliesLogicOp_90 = true;
    bool res_OrLogicOP_91 = false;
    bool res_OrLogicOP_92 = false;
    bool res_ForAllPredicateNotEmpty_93 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl12Length(my_id); ++i)
    {
    L_P1__Recor1 it = L_P1__GetRecSubcl12(my_id,i);
    bool res_ImpliesLogicOp_94 = true;
    res_ImpliesLogicOp_94 = (res_ImpliesLogicOp_94 && (L_P1__GetParamMainc8(it.mainc54) < 9u));
    res_ForAllPredicateNotEmpty_93 = res_ImpliesLogicOp_94;
    if(!res_ForAllPredicateNotEmpty_93) {break;}
    }
    res_OrLogicOP_92 = (res_OrLogicOP_92 || res_ForAllPredicateNotEmpty_93);
    bool res_AndLogicOP_95 = true;
    res_AndLogicOP_95 = (res_AndLogicOP_95 && (L_P1__GetParamSubcl14(my_id) > 9u));
    bool res_NotLogicOP_96 = true;
    res_NotLogicOP_96 = (res_NotLogicOP_96 && ! Timer_Disattivo(L_P1__GetSubcl37(my_id)));
    res_AndLogicOP_95 = (res_AndLogicOP_95 && res_NotLogicOP_96);
    
    res_OrLogicOP_92 = (res_OrLogicOP_92 || res_AndLogicOP_95);
    
    res_OrLogicOP_91 = (res_OrLogicOP_91 || res_OrLogicOP_92);
    bool res_AndLogicOP_97 = true;
    bool res_AndLogicOP_98 = true;
    res_AndLogicOP_98 = (res_AndLogicOP_98 && (L_P1__GetInConsd1(my_id) == false));
    bool res_NotLogicOP_99 = true;
    res_NotLogicOP_99 = (res_NotLogicOP_99 && ! (L_P1__GetParamSubcl14(my_id) == 2u));
    res_AndLogicOP_98 = (res_AndLogicOP_98 && res_NotLogicOP_99);
    
    res_AndLogicOP_97 = (res_AndLogicOP_97 && res_AndLogicOP_98);
    res_AndLogicOP_97 = (res_AndLogicOP_97 && (L_P1__GetInConsd1(my_id) == false));
    
    res_OrLogicOP_91 = (res_OrLogicOP_91 || res_AndLogicOP_97);
    
    if(res_OrLogicOP_91){
    bool res_ImpliesLogicOp_100 = true;
    bool res_AndLogicOP_101 = true;
    bool res_AndLogicOP_102 = true;
    bool res_AndLogicOP_103 = true;
    bool res_AndLogicOP_104 = true;
    bool res_ForAllPredicate_105 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl9Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl9(my_id,i);
    bool res_ImpliesLogicOp_106 = true;
    res_ImpliesLogicOp_106 = (res_ImpliesLogicOp_106 && Timer_Disattivo(L_P1__GetMainc47(it.mainc53)));
    res_ForAllPredicate_105 = res_ImpliesLogicOp_106;
    if(!res_ForAllPredicate_105) {break;}
    }
    res_AndLogicOP_104 = (res_AndLogicOP_104 && res_ForAllPredicate_105);
    res_AndLogicOP_104 = (res_AndLogicOP_104 && Timer_Disattivo(L_P1__GetSubcl39(my_id)));
    
    res_AndLogicOP_103 = (res_AndLogicOP_103 && res_AndLogicOP_104);
    res_AndLogicOP_103 = (res_AndLogicOP_103 && (L_P1__GetSubcl34(my_id) < 10u));
    
    res_AndLogicOP_102 = (res_AndLogicOP_102 && res_AndLogicOP_103);
    bool res_NotLogicOP_107 = true;
    res_NotLogicOP_107 = (res_NotLogicOP_107 && ! (L_P1__GetParamSubcl14(my_id) == 5u));
    res_AndLogicOP_102 = (res_AndLogicOP_102 && res_NotLogicOP_107);
    
    res_AndLogicOP_101 = (res_AndLogicOP_101 && res_AndLogicOP_102);
    res_AndLogicOP_101 = (res_AndLogicOP_101 && (Counter_GetValore(L_P1__GetSubcl42(my_id)) == 122u));
    
    if(res_AndLogicOP_101){
    bool res_OrLogicOP_108 = false;
    bool res_AndLogicOP_109 = true;
    res_AndLogicOP_109 = (res_AndLogicOP_109 && (L_P1__GetSubcl34(my_id) < 5u));
    bool res_NotLogicOP_110 = true;
    bool res_NotLogicOP_111 = true;
    res_NotLogicOP_111 = (res_NotLogicOP_111 && ! (L_P1__GetSubcl34(my_id) == 9u));
    res_NotLogicOP_110 = (res_NotLogicOP_110 && ! res_NotLogicOP_111);
    res_AndLogicOP_109 = (res_AndLogicOP_109 && res_NotLogicOP_110);
    
    res_OrLogicOP_108 = (res_OrLogicOP_108 || res_AndLogicOP_109);
    res_OrLogicOP_108 = (res_OrLogicOP_108 || (L_P1__GetInConsd1(my_id) == false));
    
    res_ImpliesLogicOp_100 = (res_ImpliesLogicOp_100 && res_OrLogicOP_108);
    }
    res_ImpliesLogicOp_90 = (res_ImpliesLogicOp_90 && res_ImpliesLogicOp_100);
    }
    res_OrLogicOP_89 = (res_OrLogicOP_89 || res_ImpliesLogicOp_90);
    bool res_AndLogicOP_112 = true;
    bool res_AndLogicOP_113 = true;
    bool res_AndLogicOP_114 = true;
    res_AndLogicOP_114 = (res_AndLogicOP_114 && (Counter_GetValore(L_P1__GetSubcl42(my_id)) == 151u));
    bool res_NotLogicOP_115 = true;
    res_NotLogicOP_115 = (res_NotLogicOP_115 && ! (L_P1__GetInSubcl5(my_id) == spento));
    res_AndLogicOP_114 = (res_AndLogicOP_114 && res_NotLogicOP_115);
    
    res_AndLogicOP_113 = (res_AndLogicOP_113 && res_AndLogicOP_114);
    bool res_NotLogicOP_116 = true;
    res_NotLogicOP_116 = (res_NotLogicOP_116 && ! (L_P1__GetSubcl34(my_id) == 3u));
    res_AndLogicOP_113 = (res_AndLogicOP_113 && res_NotLogicOP_116);
    
    res_AndLogicOP_112 = (res_AndLogicOP_112 && res_AndLogicOP_113);
    res_AndLogicOP_112 = (res_AndLogicOP_112 && (L_P1__GetInConsd1(my_id) == false));
    
    res_OrLogicOP_89 = (res_OrLogicOP_89 || res_AndLogicOP_112);
    
    res_ImpliesLogicOp_85 = (res_ImpliesLogicOp_85 && res_OrLogicOP_89);
    }
    res_AndLogicOP_84 = (res_AndLogicOP_84 && res_ImpliesLogicOp_85);
    bool res_OrLogicOP_117 = false;
    bool res_OrLogicOP_118 = false;
    res_OrLogicOP_118 = (res_OrLogicOP_118 || (L_P1__GetInConsd1(my_id) == false));
    res_OrLogicOP_118 = (res_OrLogicOP_118 || (L_P1__GetInConsd1(my_id) == false));
    
    res_OrLogicOP_117 = (res_OrLogicOP_117 || res_OrLogicOP_118);
    res_OrLogicOP_117 = (res_OrLogicOP_117 || Timer_Disattivo(L_P1__GetSubcl39(my_id)));
    
    res_AndLogicOP_84 = (res_AndLogicOP_84 && res_OrLogicOP_117);
    
    res_ImpliesLogicOp_82 = (res_ImpliesLogicOp_82 && res_AndLogicOP_84);
    }
    res_AndLogicOP_81 = (res_AndLogicOP_81 && res_ImpliesLogicOp_82);
    bool res_OrLogicOP_119 = false;
    bool res_OrLogicOP_120 = false;
    res_OrLogicOP_120 = (res_OrLogicOP_120 || (L_P1__GetInConsd1(my_id) == false));
    bool res_NotLogicOP_121 = true;
    res_NotLogicOP_121 = (res_NotLogicOP_121 && ! (L_P1__GetSubcl34(my_id) == 6u));
    res_OrLogicOP_120 = (res_OrLogicOP_120 || res_NotLogicOP_121);
    
    res_OrLogicOP_119 = (res_OrLogicOP_119 || res_OrLogicOP_120);
    res_OrLogicOP_119 = (res_OrLogicOP_119 || Timer_Scaduto(L_P1__GetSubcl40(my_id)));
    
    res_AndLogicOP_81 = (res_AndLogicOP_81 && res_OrLogicOP_119);
    
    res_ImpliesLogicOp_74 = (res_ImpliesLogicOp_74 && res_AndLogicOP_81);
    }
    res_AndLogicOP_73 = (res_AndLogicOP_73 && res_ImpliesLogicOp_74);
    bool res_OrLogicOP_122 = false;
    bool res_AndLogicOP_123 = true;
    res_AndLogicOP_123 = (res_AndLogicOP_123 && (L_P1__GetParamSubcl14(my_id) > 4u));
    bool res_NotLogicOP_124 = true;
    res_NotLogicOP_124 = (res_NotLogicOP_124 && ! Timer_Disattivo(L_P1__GetSubcl41(my_id)));
    res_AndLogicOP_123 = (res_AndLogicOP_123 && res_NotLogicOP_124);
    
    res_OrLogicOP_122 = (res_OrLogicOP_122 || res_AndLogicOP_123);
    res_OrLogicOP_122 = (res_OrLogicOP_122 || Timer_Disattivo(L_P1__GetSubcl39(my_id)));
    
    res_AndLogicOP_73 = (res_AndLogicOP_73 && res_OrLogicOP_122);
    
    res_ImpliesLogicOp_67 = (res_ImpliesLogicOp_67 && res_AndLogicOP_73);
    }
    res_AndLogicOP_66 = (res_AndLogicOP_66 && res_ImpliesLogicOp_67);
    res_AndLogicOP_66 = (res_AndLogicOP_66 && (L_P1__GetParamSubcl14(my_id) < 1u));
    
    res_ImpliesLogicOp_65 = (res_ImpliesLogicOp_65 && res_AndLogicOP_66);
    }
    res_OrLogicOP_64 = (res_OrLogicOP_64 || res_ImpliesLogicOp_65);
    bool res_NotLogicOP_125 = true;
    res_NotLogicOP_125 = (res_NotLogicOP_125 && ! (L_P1__GetInSubcl7(my_id) == rossogiallo3));
    res_OrLogicOP_64 = (res_OrLogicOP_64 || res_NotLogicOP_125);
    
    res_ImpliesLogicOp_54 = (res_ImpliesLogicOp_54 && res_OrLogicOP_64);
    }
    res_OrLogicOP_53 = (res_OrLogicOP_53 || res_ImpliesLogicOp_54);
    bool res_OrLogicOP_126 = false;
    bool res_NotLogicOP_127 = true;
    res_NotLogicOP_127 = (res_NotLogicOP_127 && ! Timer_Disattivo(L_P1__GetSubcl37(my_id)));
    res_OrLogicOP_126 = (res_OrLogicOP_126 || res_NotLogicOP_127);
    bool res_AndLogicOP_128 = true;
    bool res_NotLogicOP_129 = true;
    bool res_NotLogicOP_130 = true;
    res_NotLogicOP_130 = (res_NotLogicOP_130 && ! (L_P1__GetInSubcl7(my_id) == rossogiallo3));
    res_NotLogicOP_129 = (res_NotLogicOP_129 && ! res_NotLogicOP_130);
    res_AndLogicOP_128 = (res_AndLogicOP_128 && res_NotLogicOP_129);
    bool res_NotLogicOP_131 = true;
    res_NotLogicOP_131 = (res_NotLogicOP_131 && ! (L_P1__GetSubcl34(my_id) == 8u));
    res_AndLogicOP_128 = (res_AndLogicOP_128 && res_NotLogicOP_131);
    
    res_OrLogicOP_126 = (res_OrLogicOP_126 || res_AndLogicOP_128);
    
    res_OrLogicOP_53 = (res_OrLogicOP_53 || res_OrLogicOP_126);
    
    res_ImpliesLogicOp_46 = (res_ImpliesLogicOp_46 && res_OrLogicOP_53);
    }
    if(res_ImpliesLogicOp_46){
    xorIndex_res_XorLogicOP_45 = (xorIndex_res_XorLogicOP_45 + 1);
    }
    bool res_OrLogicOP_132 = false;
    bool res_OrLogicOP_133 = false;
    bool res_OrLogicOP_134 = false;
    bool res_NotLogicOP_135 = true;
    res_NotLogicOP_135 = (res_NotLogicOP_135 && ! Timer_Scaduto(L_P1__GetSubcl40(my_id)));
    res_OrLogicOP_134 = (res_OrLogicOP_134 || res_NotLogicOP_135);
    bool res_NotLogicOP_136 = true;
    bool res_NotLogicOP_137 = true;
    res_NotLogicOP_137 = (res_NotLogicOP_137 && ! (L_P1__GetInSubcl7(my_id) == rossogiallo3));
    res_NotLogicOP_136 = (res_NotLogicOP_136 && ! res_NotLogicOP_137);
    res_OrLogicOP_134 = (res_OrLogicOP_134 || res_NotLogicOP_136);
    
    res_OrLogicOP_133 = (res_OrLogicOP_133 || res_OrLogicOP_134);
    bool res_AndLogicOP_138 = true;
    bool res_NotLogicOP_139 = true;
    res_NotLogicOP_139 = (res_NotLogicOP_139 && ! (L_P1__GetSubcl34(my_id) == 8u));
    res_AndLogicOP_138 = (res_AndLogicOP_138 && res_NotLogicOP_139);
    bool res_NotLogicOP_140 = true;
    res_NotLogicOP_140 = (res_NotLogicOP_140 && ! (L_P1__GetParamSubcl14(my_id) < 2u));
    res_AndLogicOP_138 = (res_AndLogicOP_138 && res_NotLogicOP_140);
    
    res_OrLogicOP_133 = (res_OrLogicOP_133 || res_AndLogicOP_138);
    
    res_OrLogicOP_132 = (res_OrLogicOP_132 || res_OrLogicOP_133);
    bool res_NotLogicOP_141 = true;
    res_NotLogicOP_141 = (res_NotLogicOP_141 && ! (Counter_GetValore(L_P1__GetSubcl42(my_id)) < 13305u));
    res_OrLogicOP_132 = (res_OrLogicOP_132 || res_NotLogicOP_141);
    
    if(res_OrLogicOP_132){
    xorIndex_res_XorLogicOP_45 = (xorIndex_res_XorLogicOP_45 + 1);
    }
    
    res_XorLogicOP_45 = (res_XorLogicOP_45 && (xorIndex_res_XorLogicOP_45 == 1));
    res_ImpliesLogicOp_40 = (res_ImpliesLogicOp_40 && res_XorLogicOP_45);
    }
    if(res_ImpliesLogicOp_40){
    xorIndex_res_XorLogicOP_39 = (xorIndex_res_XorLogicOP_39 + 1);
    }
    bool res_OrLogicOP_142 = false;
    bool res_OrLogicOP_143 = false;
    res_OrLogicOP_143 = (res_OrLogicOP_143 || (L_P1__GetInConsd1(my_id) == false));
    bool res_AndLogicOP_144 = true;
    bool res_AndLogicOP_145 = true;
    bool res_AndLogicOP_146 = true;
    bool res_NotLogicOP_147 = true;
    res_NotLogicOP_147 = (res_NotLogicOP_147 && ! (L_P1__GetParamSubcl16(my_id) > 7u));
    res_AndLogicOP_146 = (res_AndLogicOP_146 && res_NotLogicOP_147);
    bool res_NotLogicOP_148 = true;
    res_NotLogicOP_148 = (res_NotLogicOP_148 && ! (L_P1__GetSubcl34(my_id) < 4u));
    res_AndLogicOP_146 = (res_AndLogicOP_146 && res_NotLogicOP_148);
    
    res_AndLogicOP_145 = (res_AndLogicOP_145 && res_AndLogicOP_146);
    bool res_NotLogicOP_149 = true;
    res_NotLogicOP_149 = (res_NotLogicOP_149 && ! (L_P1__GetInSubcl7(my_id) == rossogiallo3));
    res_AndLogicOP_145 = (res_AndLogicOP_145 && res_NotLogicOP_149);
    
    res_AndLogicOP_144 = (res_AndLogicOP_144 && res_AndLogicOP_145);
    bool res_NotLogicOP_150 = true;
    res_NotLogicOP_150 = (res_NotLogicOP_150 && ! (L_P1__GetInSubcl5(my_id) == spento));
    res_AndLogicOP_144 = (res_AndLogicOP_144 && res_NotLogicOP_150);
    
    res_OrLogicOP_143 = (res_OrLogicOP_143 || res_AndLogicOP_144);
    
    res_OrLogicOP_142 = (res_OrLogicOP_142 || res_OrLogicOP_143);
    bool res_NotLogicOP_151 = true;
    bool res_NotLogicOP_152 = true;
    res_NotLogicOP_152 = (res_NotLogicOP_152 && ! (L_P1__GetParamSubcl15(my_id) == 10u));
    res_NotLogicOP_151 = (res_NotLogicOP_151 && ! res_NotLogicOP_152);
    res_OrLogicOP_142 = (res_OrLogicOP_142 || res_NotLogicOP_151);
    
    if(res_OrLogicOP_142){
    xorIndex_res_XorLogicOP_39 = (xorIndex_res_XorLogicOP_39 + 1);
    }
    
    res_XorLogicOP_39 = (res_XorLogicOP_39 && (xorIndex_res_XorLogicOP_39 == 1));
    res_ImpliesLogicOp_35 = (res_ImpliesLogicOp_35 && res_XorLogicOP_39);
    }
    res_OrLogicOP_34 = (res_OrLogicOP_34 || res_ImpliesLogicOp_35);
    bool res_OrLogicOP_153 = false;
    bool res_AndLogicOP_154 = true;
    bool res_NotLogicOP_155 = true;
    bool res_NotLogicOP_156 = true;
    res_NotLogicOP_156 = (res_NotLogicOP_156 && ! (L_P1__GetInSubcl7(my_id) == rossogiallo3));
    res_NotLogicOP_155 = (res_NotLogicOP_155 && ! res_NotLogicOP_156);
    res_AndLogicOP_154 = (res_AndLogicOP_154 && res_NotLogicOP_155);
    res_AndLogicOP_154 = (res_AndLogicOP_154 && (L_P1__GetInConsd1(my_id) == false));
    
    res_OrLogicOP_153 = (res_OrLogicOP_153 || res_AndLogicOP_154);
    bool res_AndLogicOP_157 = true;
    res_AndLogicOP_157 = (res_AndLogicOP_157 && (L_P1__GetInSubcl5(my_id) == spento));
    res_AndLogicOP_157 = (res_AndLogicOP_157 && (L_P1__GetInConsd1(my_id) == false));
    
    res_OrLogicOP_153 = (res_OrLogicOP_153 || res_AndLogicOP_157);
    
    res_OrLogicOP_34 = (res_OrLogicOP_34 || res_OrLogicOP_153);
    
    res_ImpliesLogicOp_29 = (res_ImpliesLogicOp_29 && res_OrLogicOP_34);
    }
    if(res_ImpliesLogicOp_29){
    xorIndex_res_XorLogicOP_28 = (xorIndex_res_XorLogicOP_28 + 1);
    }
    if((L_P1__GetInConsd1(my_id) == false)){
    xorIndex_res_XorLogicOP_28 = (xorIndex_res_XorLogicOP_28 + 1);
    }
    
    res_XorLogicOP_28 = (res_XorLogicOP_28 && (xorIndex_res_XorLogicOP_28 == 1));
    res_ImpliesLogicOp_22 = (res_ImpliesLogicOp_22 && res_XorLogicOP_28);
    }
    if(res_ImpliesLogicOp_22){
    xorIndex_res_XorLogicOP_21 = (xorIndex_res_XorLogicOP_21 + 1);
    }
    bool res_AndLogicOP_158 = true;
    bool res_AndLogicOP_159 = true;
    bool res_AndLogicOP_160 = true;
    bool res_NotLogicOP_161 = true;
    bool res_NotLogicOP_162 = true;
    res_NotLogicOP_162 = (res_NotLogicOP_162 && ! (L_P1__GetInSubcl4(my_id) == false));
    res_NotLogicOP_161 = (res_NotLogicOP_161 && ! res_NotLogicOP_162);
    res_AndLogicOP_160 = (res_AndLogicOP_160 && res_NotLogicOP_161);
    bool res_NotLogicOP_163 = true;
    bool res_NotLogicOP_164 = true;
    res_NotLogicOP_164 = (res_NotLogicOP_164 && ! (L_P1__GetInSubcl5(my_id) == spento));
    res_NotLogicOP_163 = (res_NotLogicOP_163 && ! res_NotLogicOP_164);
    res_AndLogicOP_160 = (res_AndLogicOP_160 && res_NotLogicOP_163);
    
    res_AndLogicOP_159 = (res_AndLogicOP_159 && res_AndLogicOP_160);
    res_AndLogicOP_159 = (res_AndLogicOP_159 && (L_P1__GetInConsd1(my_id) == false));
    
    res_AndLogicOP_158 = (res_AndLogicOP_158 && res_AndLogicOP_159);
    res_AndLogicOP_158 = (res_AndLogicOP_158 && (L_P1__GetInConsd1(my_id) == false));
    
    if(res_AndLogicOP_158){
    xorIndex_res_XorLogicOP_21 = (xorIndex_res_XorLogicOP_21 + 1);
    }
    
    res_XorLogicOP_21 = (res_XorLogicOP_21 && (xorIndex_res_XorLogicOP_21 == 1));
    res_ImpliesLogicOp_20 = (res_ImpliesLogicOp_20 && res_XorLogicOP_21);
    }
    res_OrLogicOP_19 = (res_OrLogicOP_19 || res_ImpliesLogicOp_20);
    bool res_AndLogicOP_165 = true;
    bool res_NotLogicOP_166 = true;
    bool res_NotLogicOP_167 = true;
    res_NotLogicOP_167 = (res_NotLogicOP_167 && ! (L_P1__GetSubcl34(my_id) == 7u));
    res_NotLogicOP_166 = (res_NotLogicOP_166 && ! res_NotLogicOP_167);
    res_AndLogicOP_165 = (res_AndLogicOP_165 && res_NotLogicOP_166);
    bool res_NotLogicOP_168 = true;
    res_NotLogicOP_168 = (res_NotLogicOP_168 && ! (L_P1__GetParamSubcl14(my_id) == 8u));
    res_AndLogicOP_165 = (res_AndLogicOP_165 && res_NotLogicOP_168);
    
    res_OrLogicOP_19 = (res_OrLogicOP_19 || res_AndLogicOP_165);
    
    res_ImpliesLogicOp_10 = (res_ImpliesLogicOp_10 && res_OrLogicOP_19);
    }
    if(res_ImpliesLogicOp_10){
    xorIndex_res_XorLogicOP_9 = (xorIndex_res_XorLogicOP_9 + 1);
    }
    bool res_OrLogicOP_169 = false;
    bool res_OrLogicOP_170 = false;
    bool res_AndLogicOP_171 = true;
    bool res_NotLogicOP_172 = true;
    res_NotLogicOP_172 = (res_NotLogicOP_172 && ! (Counter_GetValore(L_P1__GetSubcl42(my_id)) < 12u));
    res_AndLogicOP_171 = (res_AndLogicOP_171 && res_NotLogicOP_172);
    bool res_NotLogicOP_173 = true;
    res_NotLogicOP_173 = (res_NotLogicOP_173 && ! Timer_Disattivo(L_P1__GetSubcl41(my_id)));
    res_AndLogicOP_171 = (res_AndLogicOP_171 && res_NotLogicOP_173);
    
    res_OrLogicOP_170 = (res_OrLogicOP_170 || res_AndLogicOP_171);
    bool res_AndLogicOP_174 = true;
    bool res_NotLogicOP_175 = true;
    res_NotLogicOP_175 = (res_NotLogicOP_175 && ! (L_P1__GetInSubcl7(my_id) == rossogiallo3));
    res_AndLogicOP_174 = (res_AndLogicOP_174 && res_NotLogicOP_175);
    res_AndLogicOP_174 = (res_AndLogicOP_174 && (L_P1__GetInConsd1(my_id) == false));
    
    res_OrLogicOP_170 = (res_OrLogicOP_170 || res_AndLogicOP_174);
    
    res_OrLogicOP_169 = (res_OrLogicOP_169 || res_OrLogicOP_170);
    bool res_NotLogicOP_176 = true;
    res_NotLogicOP_176 = (res_NotLogicOP_176 && ! (L_P1__GetParamSubcl14(my_id) > 9u));
    res_OrLogicOP_169 = (res_OrLogicOP_169 || res_NotLogicOP_176);
    
    if(res_OrLogicOP_169){
    xorIndex_res_XorLogicOP_9 = (xorIndex_res_XorLogicOP_9 + 1);
    }
    
    res_XorLogicOP_9 = (res_XorLogicOP_9 && (xorIndex_res_XorLogicOP_9 == 1));
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_XorLogicOP_9);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *50,51,*  *,*  il contatore SubClass_C2_contatore_Co7 sia  maggiore di  *54,* 114
    //   *104,* e  che  *,*  la variabile SubClass_C2_variabile_V6 sia  minore di  *55,* 1
    //   *104,* o  che  *38,*  il contatore SubClass_C2_contatore_Co7 non sia  minore di  *55,* 132
    bool res_OrLogicOP_177 = false;
    bool res_AndLogicOP_178 = true;
    res_AndLogicOP_178 = (res_AndLogicOP_178 && (Counter_GetValore(L_P1__GetSubcl42(my_id)) > 114u));
    res_AndLogicOP_178 = (res_AndLogicOP_178 && (L_P1__GetSubcl34(my_id) < 1u));
    
    res_OrLogicOP_177 = (res_OrLogicOP_177 || res_AndLogicOP_178);
    bool res_NotLogicOP_179 = true;
    res_NotLogicOP_179 = (res_NotLogicOP_179 && ! (Counter_GetValore(L_P1__GetSubcl42(my_id)) < 132u));
    res_OrLogicOP_177 = (res_OrLogicOP_177 || res_NotLogicOP_179);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_177);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
    
    { commento: {62,} commento: {110,}  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è scaduto commento: {36,} e  se il timer SubClass_C2_timer_T8 non è scaduto commento: {35,} e  se il controllo SubClass_C2_controllo_C8 è  uguale a RossoGiallox, Almeno una delle seguenti { 
     commento: {62,} commento: {37,}  se la variabile SubClass_C2_variabile_V6 non è  minore di  commento: {55,} 5 o  se l'argomento argomento_ave1 non  è  uguale a RossoGialloGiallo commento: {39,}  commento: {37,} o  se la variabile SubClass_C2_variabile_V6 non è  maggiore di  commento: {54,} 2 commento: {38,} o  se il contatore SubClass_C2_contatore_Co7 non è  maggiore di  commento: {54,} 11, Almeno una delle seguenti { 
     commento: {34,}  se il parametro SubClass_C2_parametro_P2 è  maggiore di  commento: {54,} 1 commento: {37,} o  se la variabile SubClass_C2_variabile_V6 è  minore di  commento: {55,} 3 commento: {38,} e  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  commento: {56,} 124 commento: {36,} o  se il timer SubClass_C2_timer_T8 è disattivo commento: {38,} e  se il contatore SubClass_C2_contatore_Co7 non è  maggiore di  commento: {54,} 152 commento: {38,} e  se il contatore SubClass_C2_contatore_Co7 non è  minore di  commento: {55,} 11, Verifica che   commento: {48,49,50,51,}  commento: {,}  il contatore SubClass_C2_contatore_Co7 sia  diverso da  commento: {56,} 13
     commento: {104,} e  che  commento: {,}  il controllo SubClass_C2_controllo_C7 non sia  diverso da  False 
     commento: {104,} e  che  commento: {38,}  il contatore SubClass_C2_contatore_Co7 sia  maggiore di  commento: {54,} 14
     commento: {104,} o  che  commento: {,}  la variabile SubClass_C2_variabile_V6 sia  diverso da  commento: {56,} 7
     commento: {104,} e  che  commento: {,}  il timer SubClass_C2_timer_T4 sia attivo
     commento: {104,} e  che  commento: {37,}  la variabile SubClass_C2_variabile_V6 non sia  minore di  commento: {55,} 1
    
    
     } Verifica che   commento: {47,48,52,}  commento: {,}  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento
     commento: {104,} e  che   l'argomento argomento_ave6 non  sia  uguale a RossoGiallox commento: {,} 
     commento: {104,} o  che  commento: {34,}  il parametro SubClass_C2_parametro_P9 non sia  uguale a  commento: {53,} 7
     commento: {104,} e  che   l'argomento argomento_ave1 non  sia  uguale a RossoGialloGiallo commento: {39,} 
    
    
     } Verifica che   commento: {48,49,50,}  commento: {,}  la variabile SubClass_C2_variabile_V6 sia  maggiore di  commento: {54,} 6
     commento: {104,} o  che  commento: {,}  il controllo SubClass_C2_controllo_C8 sia  diverso da RossoGiallox
     commento: {104,} o  che  commento: {,}  il timer SubClass_C2_timer_T4 sia disattivo
     commento: {104,} o  che  commento: {35,}  il controllo SubClass_C2_controllo_C6 non sia  diverso da spento
    
    
    }
*/
bool L_P1__Macro13(instance_id_t const my_id , C2_Enumerat2 argom32, C2_Enumerat3 argom33)
{
bool res_AndLogicOP_0 = true;
    
    //  *62,* *110,*  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è scaduto *36,* e  se il timer SubClass_C2_timer_T8 non è scaduto *35,* e  se il controllo SubClass_C2_controllo_C8 è  uguale a RossoGiallox, Almeno una delle seguenti { 
    //   *62,* *37,*  se la variabile SubClass_C2_variabile_V6 non è  minore di  *55,* 5 o  se l'argomento argomento_ave1 non  è  uguale a RossoGialloGiallo *39,*  *37,* o  se la variabile SubClass_C2_variabile_V6 non è  maggiore di  *54,* 2 *38,* o  se il contatore SubClass_C2_contatore_Co7 non è  maggiore di  *54,* 11, Almeno una delle seguenti { 
    //   *34,*  se il parametro SubClass_C2_parametro_P2 è  maggiore di  *54,* 1 *37,* o  se la variabile SubClass_C2_variabile_V6 è  minore di  *55,* 3 *38,* e  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  *56,* 124 *36,* o  se il timer SubClass_C2_timer_T8 è disattivo *38,* e  se il contatore SubClass_C2_contatore_Co7 non è  maggiore di  *54,* 152 *38,* e  se il contatore SubClass_C2_contatore_Co7 non è  minore di  *55,* 11, Verifica che   *48,49,50,51,*  *,*  il contatore SubClass_C2_contatore_Co7 sia  diverso da  *56,* 13
    //   *104,* e  che  *,*  il controllo SubClass_C2_controllo_C7 non sia  diverso da  False 
    //   *104,* e  che  *38,*  il contatore SubClass_C2_contatore_Co7 sia  maggiore di  *54,* 14
    //   *104,* o  che  *,*  la variabile SubClass_C2_variabile_V6 sia  diverso da  *56,* 7
    //   *104,* e  che  *,*  il timer SubClass_C2_timer_T4 sia attivo
    //   *104,* e  che  *37,*  la variabile SubClass_C2_variabile_V6 non sia  minore di  *55,* 1
    //   } Verifica che   *47,48,52,*  *,*  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento
    //   *104,* e  che   l'argomento argomento_ave6 non  sia  uguale a RossoGiallox *,* 
    //   *104,* o  che  *34,*  il parametro SubClass_C2_parametro_P9 non sia  uguale a  *53,* 7
    //   *104,* e  che   l'argomento argomento_ave1 non  sia  uguale a RossoGialloGiallo *39,* 
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_AndLogicOP_2 = true;
    bool res_AndLogicOP_3 = true;
    res_AndLogicOP_3 = (res_AndLogicOP_3 && Timer_Scaduto(L_P1__GetSubcl36(my_id)));
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! Timer_Scaduto(L_P1__GetSubcl40(my_id)));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_4);
    
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_AndLogicOP_3);
    res_AndLogicOP_2 = (res_AndLogicOP_2 && (L_P1__GetInSubcl7(my_id) == rossogiallo3));
    
    if(res_AndLogicOP_2){
    bool res_OrLogicOP_5 = false;
    bool res_ImpliesLogicOp_6 = true;
    bool res_OrLogicOP_7 = false;
    bool res_OrLogicOP_8 = false;
    bool res_OrLogicOP_9 = false;
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__GetSubcl34(my_id) < 5u));
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_NotLogicOP_10);
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (argom32 == rossogiallo2));
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_NotLogicOP_11);
    
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_OrLogicOP_9);
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (L_P1__GetSubcl34(my_id) > 2u));
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_NotLogicOP_12);
    
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_OrLogicOP_8);
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (Counter_GetValore(L_P1__GetSubcl42(my_id)) > 11u));
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_NotLogicOP_13);
    
    if(res_OrLogicOP_7){
    bool res_ImpliesLogicOp_14 = true;
    bool res_OrLogicOP_15 = false;
    bool res_OrLogicOP_16 = false;
    res_OrLogicOP_16 = (res_OrLogicOP_16 || (L_P1__GetParamSubcl14(my_id) > 1u));
    bool res_AndLogicOP_17 = true;
    res_AndLogicOP_17 = (res_AndLogicOP_17 && (L_P1__GetSubcl34(my_id) < 3u));
    bool res_NotLogicOP_18 = true;
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (Counter_GetValore(L_P1__GetSubcl42(my_id)) == 124u));
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! res_NotLogicOP_19);
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_NotLogicOP_18);
    
    res_OrLogicOP_16 = (res_OrLogicOP_16 || res_AndLogicOP_17);
    
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_OrLogicOP_16);
    bool res_AndLogicOP_20 = true;
    bool res_AndLogicOP_21 = true;
    res_AndLogicOP_21 = (res_AndLogicOP_21 && Timer_Disattivo(L_P1__GetSubcl40(my_id)));
    bool res_NotLogicOP_22 = true;
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! (Counter_GetValore(L_P1__GetSubcl42(my_id)) > 152u));
    res_AndLogicOP_21 = (res_AndLogicOP_21 && res_NotLogicOP_22);
    
    res_AndLogicOP_20 = (res_AndLogicOP_20 && res_AndLogicOP_21);
    bool res_NotLogicOP_23 = true;
    res_NotLogicOP_23 = (res_NotLogicOP_23 && ! (Counter_GetValore(L_P1__GetSubcl42(my_id)) < 11u));
    res_AndLogicOP_20 = (res_AndLogicOP_20 && res_NotLogicOP_23);
    
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_AndLogicOP_20);
    
    if(res_OrLogicOP_15){
    bool res_OrLogicOP_24 = false;
    bool res_AndLogicOP_25 = true;
    bool res_AndLogicOP_26 = true;
    bool res_NotLogicOP_27 = true;
    res_NotLogicOP_27 = (res_NotLogicOP_27 && ! (Counter_GetValore(L_P1__GetSubcl42(my_id)) == 13u));
    res_AndLogicOP_26 = (res_AndLogicOP_26 && res_NotLogicOP_27);
    bool res_NotLogicOP_28 = true;
    bool res_NotLogicOP_29 = true;
    res_NotLogicOP_29 = (res_NotLogicOP_29 && ! (L_P1__GetInSubcl6(my_id) == false));
    res_NotLogicOP_28 = (res_NotLogicOP_28 && ! res_NotLogicOP_29);
    res_AndLogicOP_26 = (res_AndLogicOP_26 && res_NotLogicOP_28);
    
    res_AndLogicOP_25 = (res_AndLogicOP_25 && res_AndLogicOP_26);
    res_AndLogicOP_25 = (res_AndLogicOP_25 && (Counter_GetValore(L_P1__GetSubcl42(my_id)) > 14u));
    
    res_OrLogicOP_24 = (res_OrLogicOP_24 || res_AndLogicOP_25);
    bool res_AndLogicOP_30 = true;
    bool res_AndLogicOP_31 = true;
    bool res_NotLogicOP_32 = true;
    res_NotLogicOP_32 = (res_NotLogicOP_32 && ! (L_P1__GetSubcl34(my_id) == 7u));
    res_AndLogicOP_31 = (res_AndLogicOP_31 && res_NotLogicOP_32);
    res_AndLogicOP_31 = (res_AndLogicOP_31 && Timer_Attivo(L_P1__GetSubcl39(my_id)));
    
    res_AndLogicOP_30 = (res_AndLogicOP_30 && res_AndLogicOP_31);
    bool res_NotLogicOP_33 = true;
    res_NotLogicOP_33 = (res_NotLogicOP_33 && ! (L_P1__GetSubcl34(my_id) < 1u));
    res_AndLogicOP_30 = (res_AndLogicOP_30 && res_NotLogicOP_33);
    
    res_OrLogicOP_24 = (res_OrLogicOP_24 || res_AndLogicOP_30);
    
    res_ImpliesLogicOp_14 = (res_ImpliesLogicOp_14 && res_OrLogicOP_24);
    }
    res_ImpliesLogicOp_6 = (res_ImpliesLogicOp_6 && res_ImpliesLogicOp_14);
    }
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_ImpliesLogicOp_6);
    bool res_OrLogicOP_34 = false;
    bool res_AndLogicOP_35 = true;
    bool res_NotLogicOP_36 = true;
    res_NotLogicOP_36 = (res_NotLogicOP_36 && ! (L_P1__GetInSubcl5(my_id) == spento));
    res_AndLogicOP_35 = (res_AndLogicOP_35 && res_NotLogicOP_36);
    bool res_NotLogicOP_37 = true;
    res_NotLogicOP_37 = (res_NotLogicOP_37 && ! (argom33 == rossogiallo3));
    res_AndLogicOP_35 = (res_AndLogicOP_35 && res_NotLogicOP_37);
    
    res_OrLogicOP_34 = (res_OrLogicOP_34 || res_AndLogicOP_35);
    bool res_AndLogicOP_38 = true;
    bool res_NotLogicOP_39 = true;
    res_NotLogicOP_39 = (res_NotLogicOP_39 && ! (L_P1__GetParamSubcl17(my_id) == 7u));
    res_AndLogicOP_38 = (res_AndLogicOP_38 && res_NotLogicOP_39);
    bool res_NotLogicOP_40 = true;
    res_NotLogicOP_40 = (res_NotLogicOP_40 && ! (argom32 == rossogiallo2));
    res_AndLogicOP_38 = (res_AndLogicOP_38 && res_NotLogicOP_40);
    
    res_OrLogicOP_34 = (res_OrLogicOP_34 || res_AndLogicOP_38);
    
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_OrLogicOP_34);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_OrLogicOP_5);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *48,49,50,*  *,*  la variabile SubClass_C2_variabile_V6 sia  maggiore di  *54,* 6
    //   *104,* o  che  *,*  il controllo SubClass_C2_controllo_C8 sia  diverso da RossoGiallox
    //   *104,* o  che  *,*  il timer SubClass_C2_timer_T4 sia disattivo
    //   *104,* o  che  *35,*  il controllo SubClass_C2_controllo_C6 non sia  diverso da spento
    bool res_OrLogicOP_41 = false;
    bool res_OrLogicOP_42 = false;
    bool res_OrLogicOP_43 = false;
    res_OrLogicOP_43 = (res_OrLogicOP_43 || (L_P1__GetSubcl34(my_id) > 6u));
    bool res_NotLogicOP_44 = true;
    res_NotLogicOP_44 = (res_NotLogicOP_44 && ! (L_P1__GetInSubcl7(my_id) == rossogiallo3));
    res_OrLogicOP_43 = (res_OrLogicOP_43 || res_NotLogicOP_44);
    
    res_OrLogicOP_42 = (res_OrLogicOP_42 || res_OrLogicOP_43);
    res_OrLogicOP_42 = (res_OrLogicOP_42 || Timer_Disattivo(L_P1__GetSubcl39(my_id)));
    
    res_OrLogicOP_41 = (res_OrLogicOP_41 || res_OrLogicOP_42);
    bool res_NotLogicOP_45 = true;
    bool res_NotLogicOP_46 = true;
    res_NotLogicOP_46 = (res_NotLogicOP_46 && ! (L_P1__GetInSubcl5(my_id) == spento));
    res_NotLogicOP_45 = (res_NotLogicOP_45 && ! res_NotLogicOP_46);
    res_OrLogicOP_41 = (res_OrLogicOP_41 || res_NotLogicOP_45);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_41);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
    
    { commento: {63,} commento: {41,}  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  commento: {105,} è  maggiore di  commento: {54,} 9 commento: {36,} e  se il timer SubClass_C2_timer_T4 non è disattivo commento: {37,} o  se la variabile SubClass_C2_variabile_V6 è  maggiore di  commento: {54,} 8 commento: {36,} o  se il timer SubClass_C2_timer_T4 è disattivo, Solo una delle seguenti { 
     commento: {34,}  se il parametro SubClass_C2_parametro_P2 non è  diverso da  commento: {56,} 9,  commento: {43,}  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L2 è attivo, commento: {88,} quando  commento: {111,}   lo stato del campo  MainClass_C1     è  uguale a  commento: {53,}  state1  commento: {36,} e  se il timer SubClass_C2_timer_T4 non è attivo commento: {37,} e  se la variabile SubClass_C2_variabile_V6 è  diverso da  commento: {56,} 7 commento: {34,} e  se il parametro SubClass_C2_parametro_P2 non è  diverso da  commento: {56,} 7, Verifica che   commento: {48,52,}   l'argomento argomento_ave2 non  sia  diverso da  False  commento: {,} 
     commento: {104,} o  che  commento: {,}  il controllo SubClass_C2_controllo_C8 sia  uguale a RossoGiallox
    
    
     } Verifica che   commento: {47,48,49,50,52,}  commento: {,}  la variabile SubClass_C2_variabile_V6 sia  minore di  commento: {55,} 6
     commento: {104,} e  che  commento: {,}  il controllo SubClass_C2_controllo_C8 non sia  uguale a RossoGiallox
     commento: {104,} e  che  commento: {34,}  il parametro SubClass_C2_parametro_P2 sia  maggiore di  commento: {54,} 8
     commento: {104,} e  che  commento: {,}  il timer SubClass_C2_timer_T8 non sia disattivo
     commento: {104,} e  che   l'argomento argomento_ave4 sia  diverso da RossoGiallox commento: {,} 
    
    
    }
*/
bool L_P1__Macro14(instance_id_t const my_id , C2_Enumerat2 argom34, bool argom35, C2_Enumerat3 argom36, C2_Enumerat3 argom37, C2_Enumerat1 argom38, bool argom39, bool argom40)
{
bool res_AndLogicOP_0 = true;
    
    //  *63,* *41,*  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  *105,* è  maggiore di  *54,* 9 *36,* e  se il timer SubClass_C2_timer_T4 non è disattivo *37,* o  se la variabile SubClass_C2_variabile_V6 è  maggiore di  *54,* 8 *36,* o  se il timer SubClass_C2_timer_T4 è disattivo, Solo una delle seguenti { 
    //   *34,*  se il parametro SubClass_C2_parametro_P2 non è  diverso da  *56,* 9,  *43,*  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L2 è attivo, *88,* quando  *111,*   lo stato del campo  MainClass_C1     è  uguale a  *53,*  state1  *36,* e  se il timer SubClass_C2_timer_T4 non è attivo *37,* e  se la variabile SubClass_C2_variabile_V6 è  diverso da  *56,* 7 *34,* e  se il parametro SubClass_C2_parametro_P2 non è  diverso da  *56,* 7, Verifica che   *48,52,*   l'argomento argomento_ave2 non  sia  diverso da  False  *,* 
    //   *104,* o  che  *,*  il controllo SubClass_C2_controllo_C8 sia  uguale a RossoGiallox
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_AndLogicOP_4 = true;
    bool res_ForAllPredicateNotEmpty_5 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl12Length(my_id); ++i)
    {
    L_P1__Recor1 it = L_P1__GetRecSubcl12(my_id,i);
    bool res_ImpliesLogicOp_6 = true;
    res_ImpliesLogicOp_6 = (res_ImpliesLogicOp_6 && (L_P1__GetParamMainc8(it.mainc54) > 9u));
    res_ForAllPredicateNotEmpty_5 = res_ImpliesLogicOp_6;
    if(!res_ForAllPredicateNotEmpty_5) {break;}
    }
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_ForAllPredicateNotEmpty_5);
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! Timer_Disattivo(L_P1__GetSubcl39(my_id)));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_7);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_AndLogicOP_4);
    res_OrLogicOP_3 = (res_OrLogicOP_3 || (L_P1__GetSubcl34(my_id) > 8u));
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    res_OrLogicOP_2 = (res_OrLogicOP_2 || Timer_Disattivo(L_P1__GetSubcl39(my_id)));
    
    if(res_OrLogicOP_2){
    bool res_ImpliesLogicOp_8 = true;
    bool res_AndLogicOP_9 = true;
    bool res_AndLogicOP_10 = true;
    bool res_AndLogicOP_11 = true;
    bool res_AndLogicOP_12 = true;
    bool res_NotLogicOP_13 = true;
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1__GetParamSubcl14(my_id) == 9u));
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! res_NotLogicOP_14);
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_NotLogicOP_13);
    bool res_ForAllPredicate_15 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl11Length(my_id); ++i)
    {
    L_P1__Recor1 it = L_P1__GetRecSubcl11(my_id,i);
    bool res_ImpliesLogicOp_16 = true;
    if((L_P1_C1_GetState(it.mainc54) == C1_St_state)){
    res_ImpliesLogicOp_16 = (res_ImpliesLogicOp_16 && Timer_Attivo(L_P1__GetMainc47(it.mainc54)));
    }
    res_ForAllPredicate_15 = res_ImpliesLogicOp_16;
    if(!res_ForAllPredicate_15) {break;}
    }
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_ForAllPredicate_15);
    
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_AndLogicOP_12);
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! Timer_Attivo(L_P1__GetSubcl39(my_id)));
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_NotLogicOP_17);
    
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_AndLogicOP_11);
    bool res_NotLogicOP_18 = true;
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! (L_P1__GetSubcl34(my_id) == 7u));
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_NotLogicOP_18);
    
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_AndLogicOP_10);
    bool res_NotLogicOP_19 = true;
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! (L_P1__GetParamSubcl14(my_id) == 7u));
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! res_NotLogicOP_20);
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_NotLogicOP_19);
    
    if(res_AndLogicOP_9){
    bool res_OrLogicOP_21 = false;
    bool res_NotLogicOP_22 = true;
    bool res_NotLogicOP_23 = true;
    res_NotLogicOP_23 = (res_NotLogicOP_23 && ! (argom35 == false));
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! res_NotLogicOP_23);
    res_OrLogicOP_21 = (res_OrLogicOP_21 || res_NotLogicOP_22);
    res_OrLogicOP_21 = (res_OrLogicOP_21 || (L_P1__GetInSubcl7(my_id) == rossogiallo3));
    
    res_ImpliesLogicOp_8 = (res_ImpliesLogicOp_8 && res_OrLogicOP_21);
    }
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_ImpliesLogicOp_8);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *47,48,49,50,52,*  *,*  la variabile SubClass_C2_variabile_V6 sia  minore di  *55,* 6
    //   *104,* e  che  *,*  il controllo SubClass_C2_controllo_C8 non sia  uguale a RossoGiallox
    //   *104,* e  che  *34,*  il parametro SubClass_C2_parametro_P2 sia  maggiore di  *54,* 8
    //   *104,* e  che  *,*  il timer SubClass_C2_timer_T8 non sia disattivo
    //   *104,* e  che   l'argomento argomento_ave4 sia  diverso da RossoGiallox
    bool res_AndLogicOP_24 = true;
    bool res_AndLogicOP_25 = true;
    bool res_AndLogicOP_26 = true;
    bool res_AndLogicOP_27 = true;
    res_AndLogicOP_27 = (res_AndLogicOP_27 && (L_P1__GetSubcl34(my_id) < 6u));
    bool res_NotLogicOP_28 = true;
    res_NotLogicOP_28 = (res_NotLogicOP_28 && ! (L_P1__GetInSubcl7(my_id) == rossogiallo3));
    res_AndLogicOP_27 = (res_AndLogicOP_27 && res_NotLogicOP_28);
    
    res_AndLogicOP_26 = (res_AndLogicOP_26 && res_AndLogicOP_27);
    res_AndLogicOP_26 = (res_AndLogicOP_26 && (L_P1__GetParamSubcl14(my_id) > 8u));
    
    res_AndLogicOP_25 = (res_AndLogicOP_25 && res_AndLogicOP_26);
    bool res_NotLogicOP_29 = true;
    res_NotLogicOP_29 = (res_NotLogicOP_29 && ! Timer_Disattivo(L_P1__GetSubcl40(my_id)));
    res_AndLogicOP_25 = (res_AndLogicOP_25 && res_NotLogicOP_29);
    
    res_AndLogicOP_24 = (res_AndLogicOP_24 && res_AndLogicOP_25);
    bool res_NotLogicOP_30 = true;
    res_NotLogicOP_30 = (res_NotLogicOP_30 && ! (argom36 == rossogiallo3));
    res_AndLogicOP_24 = (res_AndLogicOP_24 && res_NotLogicOP_30);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_AndLogicOP_24);
    
    
    
    return res_AndLogicOP_0;
}


// Macro valorizzate

/*
    CNL corrispondente:
    
    { commento: {[}
     commento: {46,} assegna alla macro il valore RossoGiallox commento: {],}
    }
*/
C2_Enumerat3 L_P1__Macro11(instance_id_t const my_id , bool argom30, C2_Enumerat4 argom31)
{
return rossogiallo3;
}



