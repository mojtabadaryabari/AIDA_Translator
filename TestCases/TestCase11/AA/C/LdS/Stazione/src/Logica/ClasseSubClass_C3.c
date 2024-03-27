// Codice del modello 'TestCase11', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#include "Logica/ClasseMainClass_C1.h"
#include "Logica/ClasseSubClass_C2.h"
#include "Logica/ClasseSubClass_C3.h"
#include "Logica/ClasseSubClass_C4.h"
#include "Logica/ClasseSubClass_C3_priv.h"
#include "config.h"
#include "scheduler.h"


// ********** Gestione comandi manuali **********

static void L_P1_C3_InitCmdsResponse(instance_id_t const my_id)
{
    // for each manual command of L_P1_C3
    if (L_P1__GetInEvent9(my_id)) {
	    L_P1__SetOutEvent10(my_id, LDS_MANCMD_UNEXPECTED);
    } else {
        L_P1__SetOutEvent10(my_id, LDS_MANCMD_NOOP);
    }
}

static void L_P1_C3_SetExpectedCmdsResponse(instance_id_t const my_id, C3_Stateenu state)
{        
    switch (state) {
    case C3_St_state:
        // manual commands of L_P1_C3 that can be received in C3_St_state
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
static inline bool L_P1__Guard4(instance_id_t const my_id)
{
    return true;
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


// ********** Definizione effetti **********

/*
    CNL corrispondente:
    
     {
     Nessuna 
     }
*/
static inline void L_P1__Effec4(instance_id_t const my_id)
{
    
}


/*
    CNL corrispondente:
     
    {
    Nessuna
    }
*/
static inline void L_P1__Effec5(instance_id_t const my_id)
{
    
}



// ********** Definizione metodi **********

// Metodi standard

void L_P1_C3_Init(instance_id_t const my_id)
{
    // init variabili di stato
    L_P1__SetStato5(my_id, C3_St_Stato);
    L_P1__SetSubcl65(my_id, false);
    L_P1__SetSubcl67(my_id, false);
    L_P1__SetSubcl69(my_id, false);
    L_P1__SetSubcl71(my_id, spento);
    L_P1__SetSubcl73(my_id, false);
    L_P1__SetSubcl75(my_id, rossogiallo4);
    L_P1__SetSubcl76(my_id, rossogiallo4);
    L_P1__SetSubcl77(my_id, rossogiallo4);
    L_P1__SetSubcl78(my_id, rossogiallo4);
    L_P1__SetSubcl79(my_id, 0);
    // init controlli precedenti
    L_P1__SetSubcl56(my_id, true);
    L_P1__SetSubcl58(my_id, gialloaverd);
    L_P1__SetSubcl60(my_id, true);
    L_P1__SetSubcl62(my_id, true);
    L_P1__SetSubcl64(my_id, true);
    // init Timer e Counter
    Timer_AggmInit(L_P1__GetSubcl80(my_id), true, CLASS_L_P1_C3_ID, my_id, L_P1__subcl80_ID);
    Timer_Init(L_P1__GetSubcl80(my_id), 345000);
    Timer_AggmInit(L_P1__GetSubcl81(my_id), true, CLASS_L_P1_C3_ID, my_id, L_P1__subcl81_ID);
    Timer_Init(L_P1__GetSubcl81(my_id), 345000);
    Timer_AggmInit(L_P1__GetSubcl82(my_id), true, CLASS_L_P1_C3_ID, my_id, L_P1__subcl82_ID);
    Timer_Init(L_P1__GetSubcl82(my_id), 40213000);
    Timer_AggmInit(L_P1__GetSubcl83(my_id), true, CLASS_L_P1_C3_ID, my_id, L_P1__subcl83_ID);
    Timer_Init(L_P1__GetSubcl83(my_id), 40213000);
    Timer_AggmInit(L_P1__GetSubcl84(my_id), true, CLASS_L_P1_C3_ID, my_id, L_P1__subcl84_ID);
    Timer_Init(L_P1__GetSubcl84(my_id), 350213000);
    Timer_AggmInit(L_P1__GetSubcl85(my_id), true, CLASS_L_P1_C3_ID, my_id, L_P1__subcl85_ID);
    Timer_Init(L_P1__GetSubcl85(my_id), 4000);
    Timer_AggmInit(L_P1__GetSubcl86(my_id), true, CLASS_L_P1_C3_ID, my_id, L_P1__subcl86_ID);
    Timer_Init(L_P1__GetSubcl86(my_id), 5000);
    Counter_AggmInit(L_P1__GetSubcl87(my_id), true, CLASS_L_P1_C3_ID, my_id, L_P1__subcl87_ID);
    Counter_Init(L_P1__GetSubcl87(my_id));
    // init response
    L_P1_C3_SetResponse(my_id, LDS_SCHED_NOP);

    // transizione iniziale
    if(L_P1__Guard4(my_id)) {
        L_P1_C3_SetState(my_id, C3_St_state);
	L_P1__Effec4(my_id);
    } else {
        STOP_EXECUTION(LOGIC_ERROR);
    }
    // init variabili precedenti
    L_P1__SetSubcl66(my_id, L_P1__GetSubcl65(my_id));
    L_P1__SetSubcl68(my_id, L_P1__GetSubcl67(my_id));
    L_P1__SetSubcl70(my_id, L_P1__GetSubcl69(my_id));
    L_P1__SetSubcl72(my_id, L_P1__GetSubcl71(my_id));
    L_P1__SetSubcl74(my_id, L_P1__GetSubcl73(my_id));
}

void L_P1_C3_Exec(instance_id_t const my_id, Phase const p)
{
    L_P1_C3_SetResponse(my_id, LDS_SCHED_NOP);
    switch (p) {

    case LDS_PHASE_MANUAL:
        // Reset risposte ai comandi manuali
        L_P1_C3_InitCmdsResponse(my_id);
	L_P1_C3_SetExpectedCmdsResponse(my_id, L_P1_C3_GetState(my_id));
        switch (L_P1_C3_GetState(my_id)) {

        case C3_St_state:
                { } // fine transizioni da state nella fase LDS_PHASE_MANUAL
            break;

        default:
            STOP_EXECUTION(LOGIC_ERROR);
            break;  // Needed for MISRA C syntactic compliance
        } // switch sugli stati chiuso
        break;
 

    case LDS_PHASE_STATE:

        switch (L_P1_C3_GetState(my_id)) {

        case C3_St_state:
            if (L_P1__Guard5(my_id)) {
                L_P1_C3_SetState(my_id, C3_St_state);
                L_P1__Effec5(my_id);				
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
        break;
 
    default:
        STOP_EXECUTION(LOGIC_ERROR);
        break;
    }
}

ExecResponse L_P1_C3_GExec(global_id_t const proc_id, Phase const p)
{
    CHECK_LT(GLOBAL_TO_L_P1_C3(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C3(proc_id);
    L_P1_C3_Exec(my_id, p);
    return L_P1_C3_GetResponse(my_id);
}

void L_P1_C3_GTick(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C3(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C3(proc_id);
    Timer_Exec(L_P1__GetSubcl80(my_id));
    Timer_Exec(L_P1__GetSubcl81(my_id));
    Timer_Exec(L_P1__GetSubcl82(my_id));
    Timer_Exec(L_P1__GetSubcl83(my_id));
    Timer_Exec(L_P1__GetSubcl84(my_id));
    Timer_Exec(L_P1__GetSubcl85(my_id));
    Timer_Exec(L_P1__GetSubcl86(my_id));
}

void L_P1_C3_GSetSafe(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C3(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C3(proc_id);
    L_P1__SetOutSubcl43(my_id, false);
}

void L_P1_C3_GUpdatePrev(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C3(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C3(proc_id);
    L_P1__SetSubcl56(my_id, L_P1__GetInSubcl55(my_id));
    L_P1__SetSubcl58(my_id, L_P1__GetInSubcl57(my_id));
    L_P1__SetSubcl60(my_id, L_P1__GetInSubcl59(my_id));
    L_P1__SetSubcl62(my_id, L_P1__GetInSubcl61(my_id));
    L_P1__SetSubcl64(my_id, L_P1__GetInSubcl63(my_id));
    L_P1__SetSubcl66(my_id, L_P1__GetSubcl65(my_id));
    L_P1__SetSubcl68(my_id, L_P1__GetSubcl67(my_id));
    L_P1__SetSubcl70(my_id, L_P1__GetSubcl69(my_id));
    L_P1__SetSubcl72(my_id, L_P1__GetSubcl71(my_id));
    L_P1__SetSubcl74(my_id, L_P1__GetSubcl73(my_id));
}

// ********** Definizione macro **********

// Macro di effetto

/*
    CNL corrispondente:
    
    { commento: {44,}  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C3_lista_L4 esiste e  commento: {105,} è  uguale a  commento: {53,} 1 commento: {38,} o  se il contatore SubClass_C3_contatore_Co3 non è  maggiore di  commento: {54,} 1250213 commento: {37,} e  se la variabile SubClass_C3_variabile_V9 non è  maggiore di  commento: {54,} 4, commento: {67,} Assegna alla variabile SubClass_C3_variabile_V9 il valore 5
    
       
     commento: {36,}  se il timer SubClass_C3_timer_T5 non è scaduto commento: {36,} o  se il timer SubClass_C3_timer_T5 non è disattivo commento: {37,} o  se la variabile SubClass_C3_variabile_V9 è  diverso da  commento: {56,} 4 commento: {37,} e  se la variabile SubClass_C3_variabile_V9 non è  diverso da  commento: {56,} 4 commento: {36,} o  se il timer SubClass_C3_timer_T5 è disattivo, commento: {68,}Attiva il timer SubClass_C3_timer_T7
    
       
    
    }
*/
void L_P1__Macro23(instance_id_t const my_id )
{
//  *44,*  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C3_lista_L4 esiste e  *105,* è  uguale a  *53,* 1 *38,* o  se il contatore SubClass_C3_contatore_Co3 non è  maggiore di  *54,* 1250213 *37,* e  se la variabile SubClass_C3_variabile_V9 non è  maggiore di  *54,* 4, *67,* Assegna alla variabile SubClass_C3_variabile_V9 il valore 5
    bool res_OrLogicOP_0 = false;
    bool res_ForAllPredicateNotEmpty_1 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl47Length(my_id); ++i)
    {
    L_P1__Recor2 it = L_P1__GetRecSubcl47(my_id,i);
    bool res_ImpliesLogicOp_2 = true;
    res_ImpliesLogicOp_2 = (res_ImpliesLogicOp_2 && (L_P1__GetMainc32(it.mainc47) == 1u));
    res_ForAllPredicateNotEmpty_1 = res_ImpliesLogicOp_2;
    if(!res_ForAllPredicateNotEmpty_1) {break;}
    }
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_ForAllPredicateNotEmpty_1);
    bool res_AndLogicOP_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (Counter_GetValore(L_P1__GetSubcl87(my_id)) > 1250213u));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_4);
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetSubcl79(my_id) > 4u));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_5);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_3);
    
    if(res_OrLogicOP_0){
    
    L_P1__SetSubcl79(my_id,5u);
    }
    //  *36,*  se il timer SubClass_C3_timer_T5 non è scaduto *36,* o  se il timer SubClass_C3_timer_T5 non è disattivo *37,* o  se la variabile SubClass_C3_variabile_V9 è  diverso da  *56,* 4 *37,* e  se la variabile SubClass_C3_variabile_V9 non è  diverso da  *56,* 4 *36,* o  se il timer SubClass_C3_timer_T5 è disattivo, *68,*Attiva il timer SubClass_C3_timer_T7
    bool res_OrLogicOP_6 = false;
    bool res_OrLogicOP_7 = false;
    bool res_OrLogicOP_8 = false;
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! Timer_Scaduto(L_P1__GetSubcl85(my_id)));
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_NotLogicOP_9);
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! Timer_Disattivo(L_P1__GetSubcl85(my_id)));
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_NotLogicOP_10);
    
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_OrLogicOP_8);
    bool res_AndLogicOP_11 = true;
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (L_P1__GetSubcl79(my_id) == 4u));
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_NotLogicOP_12);
    bool res_NotLogicOP_13 = true;
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1__GetSubcl79(my_id) == 4u));
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! res_NotLogicOP_14);
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_NotLogicOP_13);
    
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_AndLogicOP_11);
    
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_OrLogicOP_7);
    res_OrLogicOP_6 = (res_OrLogicOP_6 || Timer_Disattivo(L_P1__GetSubcl85(my_id)));
    
    if(res_OrLogicOP_6){
    
    Timer_Attiva(L_P1__GetSubcl86(my_id));
    }
}

/*
    CNL corrispondente:
    
    { commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L1 esiste e  commento: {105,} è  uguale a  commento: {53,}  state1  commento: {36,} e  se il timer SubClass_C3_timer_T7 non è scaduto,  Applica gli effetti
           della macro SubClass_C3_macroef_M6  commento: {73,}
    
       
     commento: {44,}  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C3_lista_L10 è  diverso da  False , commento: {67,} Assegna alla variabile SubClass_C3_variabile_V9 il valore 4
    
     ,altrimenti  commento: {66,} Assegna al comando SubClass_C3_comando_C6 il valore  True 
    
    
    
    }
*/
void L_P1__Macro24(instance_id_t const my_id )
{
//  *111,*  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L1 esiste e  *105,* è  uguale a  *53,*  state1  *36,* e  se il timer SubClass_C3_timer_T7 non è scaduto,  Applica gli effetti
    //       della macro SubClass_C3_macroef_M6
    bool res_AndLogicOP_0 = true;
    bool res_ForAllPredicateNotEmpty_1 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl45Length(my_id); ++i)
    {
    L_P1__Recor2 it = L_P1__GetRecSubcl45(my_id,i);
    bool res_ImpliesLogicOp_2 = true;
    res_ImpliesLogicOp_2 = (res_ImpliesLogicOp_2 && (L_P1_C1_GetState(it.mainc47) == C1_St_state));
    res_ForAllPredicateNotEmpty_1 = res_ImpliesLogicOp_2;
    if(!res_ForAllPredicateNotEmpty_1) {break;}
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ForAllPredicateNotEmpty_1);
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! Timer_Scaduto(L_P1__GetSubcl86(my_id)));
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_NotLogicOP_3);
    
    if(res_AndLogicOP_0){
    
    L_P1__Macro26(my_id);
    }
    //  *73,*
    //   
    // *44,*  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C3_lista_L10 è  diverso da  False , *67,* Assegna alla variabile SubClass_C3_variabile_V9 il valore 4
    // ,altrimenti  *66,* Assegna al comando SubClass_C3_comando_C6 il valore  True
    bool res_ForAllPredicate_4 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl46Length(my_id); ++i)
    {
    L_P1__Recor2 it = L_P1__GetRecSubcl46(my_id,i);
    bool res_ImpliesLogicOp_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetMainc33(it.mainc47) == false));
    res_ImpliesLogicOp_5 = (res_ImpliesLogicOp_5 && res_NotLogicOP_6);
    res_ForAllPredicate_4 = res_ImpliesLogicOp_5;
    if(!res_ForAllPredicate_4) {break;}
    }
    if(res_ForAllPredicate_4){
    
    L_P1__SetSubcl79(my_id,4u);
    }else{
    
    L_P1__SetOutSubcl43(my_id,true);
    }
}

/*
    CNL corrispondente:
    
    { commento: {41,}  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C3_lista_L4 è  diverso da c270, commento: {70,}Incrementa il contatore SubClass_C3_contatore_Co3
    
       
     commento: {109,}  se il ripristino della variabile  SubClass_C3_restoreva_RV1 non è  uguale a AC,  Applica gli effetti
           della macro SubClass_C3_macroef_M1  commento: {73,}
    
     ,altrimenti  commento: {69,}Disattiva il timer SubClass_C3_timer_T7
    
    
    
    }
*/
void L_P1__Macro25(instance_id_t const my_id )
{
//  *41,*  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C3_lista_L4 è  diverso da c270, *70,*Incrementa il contatore SubClass_C3_contatore_Co3
    bool res_ForAllPredicate_0 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl47Length(my_id); ++i)
    {
    L_P1__Recor2 it = L_P1__GetRecSubcl47(my_id,i);
    bool res_ImpliesLogicOp_1 = true;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (L_P1__GetParamMainc5(it.mainc47) == c270));
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_NotLogicOP_2);
    res_ForAllPredicate_0 = res_ImpliesLogicOp_1;
    if(!res_ForAllPredicate_0) {break;}
    }
    if(res_ForAllPredicate_0){
    
    Counter_Incr(L_P1__GetSubcl87(my_id));
    }
    //  *109,*  se il ripristino della variabile  SubClass_C3_restoreva_RV1 non è  uguale a AC,  Applica gli effetti
    //       della macro SubClass_C3_macroef_M1  *73,*
    // ,altrimenti  *69,*Disattiva il timer SubClass_C3_timer_T7
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__GetSubcl76(my_id) == ac));
    if(res_NotLogicOP_3){
    
    L_P1__Macro23(my_id);
    }else{
    
    Timer_Disattiva(L_P1__GetSubcl86(my_id));
    }
}

/*
    CNL corrispondente:
    
    { commento: {34,}  se il parametro SubClass_C3_parametro_P5 è  diverso da  commento: {56,} 10 commento: {37,} e  se la variabile SubClass_C3_variabile_V9 è  minore di  commento: {55,} 6 commento: {35,} e  se il controllo SubClass_C3_controllo_C9 è  uguale a  True  commento: {35,} e  se il controllo SubClass_C3_controllo_C9 non è  diverso da  False , commento: {66,} Assegna al comando SubClass_C3_comando_C6 il valore  False 
    
     ,altrimenti   commento: {67,} Assegna alla variabile SubClass_C3_variabile_V9 il valore 1 commento: {67,}
    
    
     commento: {35,}  se il controllo SubClass_C3_controllo_C9 è  diverso da  False  o  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} e  se il timer SubClass_C3_timer_T10 non è attivo e  se il controllo ConsDef  è  uguale a FALSE , commento: {67,} Assegna alla variabile SubClass_C3_variabile_V9 il valore 6
    
       
     commento: {37,}  se la variabile SubClass_C3_variabile_V9 è  maggiore di  commento: {54,} 2,  commento: {67,} Assegna alla variabile SubClass_C3_variabile_V9 il valore 7 commento: {67,}
    
     ,altrimenti  commento: {66,} Assegna al comando SubClass_C3_comando_C6 il valore  False 
    
    
     commento: {35,}  se il controllo SubClass_C3_controllo_C9 è  diverso da  True  commento: {36,} e  se il timer SubClass_C3_timer_T7 non è disattivo, commento: {66,} Assegna al comando SubClass_C3_comando_C6 il valore  False 
    
     ,altrimenti  commento: {66,} Assegna al comando SubClass_C3_comando_C6 il valore  True 
    
    
    
    }
*/
void L_P1__Macro26(instance_id_t const my_id )
{
//  *34,*  se il parametro SubClass_C3_parametro_P5 è  diverso da  *56,* 10 *37,* e  se la variabile SubClass_C3_variabile_V9 è  minore di  *55,* 6 *35,* e  se il controllo SubClass_C3_controllo_C9 è  uguale a  True  *35,* e  se il controllo SubClass_C3_controllo_C9 non è  diverso da  False , *66,* Assegna al comando SubClass_C3_comando_C6 il valore  False 
    // ,altrimenti   *67,* Assegna alla variabile SubClass_C3_variabile_V9 il valore 1
    bool res_AndLogicOP_0 = true;
    bool res_AndLogicOP_1 = true;
    bool res_AndLogicOP_2 = true;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__GetParamSubcl52(my_id) == 10u));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_3);
    res_AndLogicOP_2 = (res_AndLogicOP_2 && (L_P1__GetSubcl79(my_id) < 6u));
    
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_AndLogicOP_2);
    res_AndLogicOP_1 = (res_AndLogicOP_1 && (L_P1__GetInSubcl44(my_id) == true));
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_AndLogicOP_1);
    bool res_NotLogicOP_4 = true;
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetInSubcl44(my_id) == false));
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! res_NotLogicOP_5);
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_NotLogicOP_4);
    
    if(res_AndLogicOP_0){
    
    L_P1__SetOutSubcl43(my_id,false);
    }else{
    
    L_P1__SetSubcl79(my_id,1u);
    }
    //  *67,*
    // *35,*  se il controllo SubClass_C3_controllo_C9 è  diverso da  False  o  se il controllo ConsDef  è  uguale a FALSE  *36,* e  se il timer SubClass_C3_timer_T10 non è attivo e  se il controllo ConsDef  è  uguale a FALSE , *67,* Assegna alla variabile SubClass_C3_variabile_V9 il valore 6
    bool res_OrLogicOP_6 = false;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetInSubcl44(my_id) == false));
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_NotLogicOP_7);
    bool res_AndLogicOP_8 = true;
    bool res_AndLogicOP_9 = true;
    res_AndLogicOP_9 = (res_AndLogicOP_9 && (L_P1__GetInConsd2(my_id) == false));
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! Timer_Attivo(L_P1__GetSubcl84(my_id)));
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_NotLogicOP_10);
    
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_AndLogicOP_9);
    res_AndLogicOP_8 = (res_AndLogicOP_8 && (L_P1__GetInConsd2(my_id) == false));
    
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_AndLogicOP_8);
    
    if(res_OrLogicOP_6){
    
    L_P1__SetSubcl79(my_id,6u);
    }
    //  *37,*  se la variabile SubClass_C3_variabile_V9 è  maggiore di  *54,* 2,  *67,* Assegna alla variabile SubClass_C3_variabile_V9 il valore 7 *67,*
    // ,altrimenti  *66,* Assegna al comando SubClass_C3_comando_C6 il valore  False
    if((L_P1__GetSubcl79(my_id) > 2u)){
    
    L_P1__SetSubcl79(my_id,7u);
    }else{
    
    L_P1__SetOutSubcl43(my_id,false);
    }
    //  *35,*  se il controllo SubClass_C3_controllo_C9 è  diverso da  True  *36,* e  se il timer SubClass_C3_timer_T7 non è disattivo, *66,* Assegna al comando SubClass_C3_comando_C6 il valore  False 
    // ,altrimenti  *66,* Assegna al comando SubClass_C3_comando_C6 il valore  True
    bool res_AndLogicOP_11 = true;
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (L_P1__GetInSubcl44(my_id) == true));
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_NotLogicOP_12);
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! Timer_Disattivo(L_P1__GetSubcl86(my_id)));
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_NotLogicOP_13);
    
    if(res_AndLogicOP_11){
    
    L_P1__SetOutSubcl43(my_id,false);
    }else{
    
    L_P1__SetOutSubcl43(my_id,true);
    }
}


// Macro di verifica

/*
    CNL corrispondente:
    
    { commento: {63,} commento: {36,}  se il timer SubClass_C3_timer_T5 è attivo,  commento: {44,}  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C3_lista_L4 è  diverso da  False , commento: {88,} quando  commento: {41,}   MainClass_C1_parametro_P2 del campo  MainClass_C1     è  minore di  commento: {55,} 4 commento: {34,} e  se il parametro SubClass_C3_parametro_P5 non è  minore di  commento: {55,} 2 commento: {37,} o  se la variabile SubClass_C3_variabile_V9 non è  maggiore di  commento: {54,} 5 commento: {36,} o  se il timer SubClass_C3_timer_T7 non è attivo o  se l'argomento argomento_ave8 è  uguale a  True  commento: {39,}  o  se l'argomento argomento_ave7 non  è  diverso da AC commento: {39,} , Solo una delle seguenti { 
     commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  commento: {105,} è  uguale a  commento: {53,}  state1  commento: {36,} o  se il timer SubClass_C3_timer_T10 è scaduto commento: {36,} e  se il timer SubClass_C3_timer_T10 non è disattivo commento: {34,} o  se il parametro SubClass_C3_parametro_P10 non è  diverso da  True  commento: {37,} o  se la variabile SubClass_C3_variabile_V9 non è  maggiore di  commento: {54,} 5 o  se l'argomento argomento_ave8 non  è  diverso da  False  commento: {39,} , Verifica che   commento: {47,48,49,}  commento: {,}  il controllo SubClass_C3_controllo_C9 non sia  diverso da  True 
     commento: {104,} o  che  commento: {34,}  il parametro SubClass_C3_parametro_P10 non sia  uguale a  True 
     commento: {104,} e  che  commento: {,}  il timer SubClass_C3_timer_T5 sia disattivo
     commento: {104,} e  che  commento: {36,}  il timer SubClass_C3_timer_T7 sia scaduto
     commento: {104,} o  che  commento: {34,}  il parametro SubClass_C3_parametro_P5 non sia  maggiore di  commento: {54,} 6
     commento: {104,} e  che  commento: {34,}  il parametro SubClass_C3_parametro_P10 non sia  diverso da  False 
    
    
     } Verifica che   commento: {48,49,50,}  commento: {,}  il timer SubClass_C3_timer_T5 sia attivo
     commento: {104,} e  che  commento: {,}  il controllo SubClass_C3_controllo_C9 sia  uguale a  False 
     commento: {104,} o  che  commento: {,}  la variabile SubClass_C3_variabile_V9 non sia  minore di  commento: {55,} 10
    
    
    }
*/
bool L_P1__Macro29(instance_id_t const my_id , C3_Enumerat4 argom81, bool argom82, C3_Enumerat2 argom83, C3_Enumerat1 argom84, bool argom85)
{
bool res_AndLogicOP_0 = true;
    
    //  *63,* *36,*  se il timer SubClass_C3_timer_T5 è attivo,  *44,*  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C3_lista_L4 è  diverso da  False , *88,* quando  *41,*   MainClass_C1_parametro_P2 del campo  MainClass_C1     è  minore di  *55,* 4 *34,* e  se il parametro SubClass_C3_parametro_P5 non è  minore di  *55,* 2 *37,* o  se la variabile SubClass_C3_variabile_V9 non è  maggiore di  *54,* 5 *36,* o  se il timer SubClass_C3_timer_T7 non è attivo o  se l'argomento argomento_ave8 è  uguale a  True  *39,*  o  se l'argomento argomento_ave7 non  è  diverso da AC *39,* , Solo una delle seguenti { 
    //   *111,*  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  *105,* è  uguale a  *53,*  state1  *36,* o  se il timer SubClass_C3_timer_T10 è scaduto *36,* e  se il timer SubClass_C3_timer_T10 non è disattivo *34,* o  se il parametro SubClass_C3_parametro_P10 non è  diverso da  True  *37,* o  se la variabile SubClass_C3_variabile_V9 non è  maggiore di  *54,* 5 o  se l'argomento argomento_ave8 non  è  diverso da  False  *39,* , Verifica che   *47,48,49,*  *,*  il controllo SubClass_C3_controllo_C9 non sia  diverso da  True 
    //   *104,* o  che  *34,*  il parametro SubClass_C3_parametro_P10 non sia  uguale a  True 
    //   *104,* e  che  *,*  il timer SubClass_C3_timer_T5 sia disattivo
    //   *104,* e  che  *36,*  il timer SubClass_C3_timer_T7 sia scaduto
    //   *104,* o  che  *34,*  il parametro SubClass_C3_parametro_P5 non sia  maggiore di  *54,* 6
    //   *104,* e  che  *34,*  il parametro SubClass_C3_parametro_P10 non sia  diverso da  False 
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_OrLogicOP_4 = false;
    bool res_OrLogicOP_5 = false;
    bool res_AndLogicOP_6 = true;
    bool res_AndLogicOP_7 = true;
    res_AndLogicOP_7 = (res_AndLogicOP_7 && Timer_Attivo(L_P1__GetSubcl85(my_id)));
    bool res_ForAllPredicate_8 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl47Length(my_id); ++i)
    {
    L_P1__Recor2 it = L_P1__GetRecSubcl47(my_id,i);
    bool res_ImpliesLogicOp_9 = true;
    if((L_P1__GetParamMainc6(it.mainc47) < 4u)){
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__GetMainc33(it.mainc47) == false));
    res_ImpliesLogicOp_9 = (res_ImpliesLogicOp_9 && res_NotLogicOP_10);
    }
    res_ForAllPredicate_8 = res_ImpliesLogicOp_9;
    if(!res_ForAllPredicate_8) {break;}
    }
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_ForAllPredicate_8);
    
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_AndLogicOP_7);
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (L_P1__GetParamSubcl52(my_id) < 2u));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_11);
    
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_AndLogicOP_6);
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (L_P1__GetSubcl79(my_id) > 5u));
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_NotLogicOP_12);
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_OrLogicOP_5);
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! Timer_Attivo(L_P1__GetSubcl86(my_id)));
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_NotLogicOP_13);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_OrLogicOP_4);
    res_OrLogicOP_3 = (res_OrLogicOP_3 || (argom85 == true));
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    bool res_NotLogicOP_14 = true;
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (argom84 == ac));
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! res_NotLogicOP_15);
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_14);
    
    if(res_OrLogicOP_2){
    bool res_ImpliesLogicOp_16 = true;
    bool res_OrLogicOP_17 = false;
    bool res_OrLogicOP_18 = false;
    bool res_OrLogicOP_19 = false;
    bool res_OrLogicOP_20 = false;
    bool res_ForAllPredicateNotEmpty_21 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl48Length(my_id); ++i)
    {
    L_P1__Recor2 it = L_P1__GetRecSubcl48(my_id,i);
    bool res_ImpliesLogicOp_22 = true;
    res_ImpliesLogicOp_22 = (res_ImpliesLogicOp_22 && (L_P1_C1_GetState(it.mainc47) == C1_St_state));
    res_ForAllPredicateNotEmpty_21 = res_ImpliesLogicOp_22;
    if(!res_ForAllPredicateNotEmpty_21) {break;}
    }
    res_OrLogicOP_20 = (res_OrLogicOP_20 || res_ForAllPredicateNotEmpty_21);
    bool res_AndLogicOP_23 = true;
    res_AndLogicOP_23 = (res_AndLogicOP_23 && Timer_Scaduto(L_P1__GetSubcl84(my_id)));
    bool res_NotLogicOP_24 = true;
    res_NotLogicOP_24 = (res_NotLogicOP_24 && ! Timer_Disattivo(L_P1__GetSubcl84(my_id)));
    res_AndLogicOP_23 = (res_AndLogicOP_23 && res_NotLogicOP_24);
    
    res_OrLogicOP_20 = (res_OrLogicOP_20 || res_AndLogicOP_23);
    
    res_OrLogicOP_19 = (res_OrLogicOP_19 || res_OrLogicOP_20);
    bool res_NotLogicOP_25 = true;
    bool res_NotLogicOP_26 = true;
    res_NotLogicOP_26 = (res_NotLogicOP_26 && ! (L_P1__GetParamSubcl50(my_id) == true));
    res_NotLogicOP_25 = (res_NotLogicOP_25 && ! res_NotLogicOP_26);
    res_OrLogicOP_19 = (res_OrLogicOP_19 || res_NotLogicOP_25);
    
    res_OrLogicOP_18 = (res_OrLogicOP_18 || res_OrLogicOP_19);
    bool res_NotLogicOP_27 = true;
    res_NotLogicOP_27 = (res_NotLogicOP_27 && ! (L_P1__GetSubcl79(my_id) > 5u));
    res_OrLogicOP_18 = (res_OrLogicOP_18 || res_NotLogicOP_27);
    
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_OrLogicOP_18);
    bool res_NotLogicOP_28 = true;
    bool res_NotLogicOP_29 = true;
    res_NotLogicOP_29 = (res_NotLogicOP_29 && ! (argom85 == false));
    res_NotLogicOP_28 = (res_NotLogicOP_28 && ! res_NotLogicOP_29);
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_NotLogicOP_28);
    
    if(res_OrLogicOP_17){
    bool res_OrLogicOP_30 = false;
    bool res_OrLogicOP_31 = false;
    bool res_NotLogicOP_32 = true;
    bool res_NotLogicOP_33 = true;
    res_NotLogicOP_33 = (res_NotLogicOP_33 && ! (L_P1__GetInSubcl44(my_id) == true));
    res_NotLogicOP_32 = (res_NotLogicOP_32 && ! res_NotLogicOP_33);
    res_OrLogicOP_31 = (res_OrLogicOP_31 || res_NotLogicOP_32);
    bool res_AndLogicOP_34 = true;
    bool res_AndLogicOP_35 = true;
    bool res_NotLogicOP_36 = true;
    res_NotLogicOP_36 = (res_NotLogicOP_36 && ! (L_P1__GetParamSubcl50(my_id) == true));
    res_AndLogicOP_35 = (res_AndLogicOP_35 && res_NotLogicOP_36);
    res_AndLogicOP_35 = (res_AndLogicOP_35 && Timer_Disattivo(L_P1__GetSubcl85(my_id)));
    
    res_AndLogicOP_34 = (res_AndLogicOP_34 && res_AndLogicOP_35);
    res_AndLogicOP_34 = (res_AndLogicOP_34 && Timer_Scaduto(L_P1__GetSubcl86(my_id)));
    
    res_OrLogicOP_31 = (res_OrLogicOP_31 || res_AndLogicOP_34);
    
    res_OrLogicOP_30 = (res_OrLogicOP_30 || res_OrLogicOP_31);
    bool res_AndLogicOP_37 = true;
    bool res_NotLogicOP_38 = true;
    res_NotLogicOP_38 = (res_NotLogicOP_38 && ! (L_P1__GetParamSubcl52(my_id) > 6u));
    res_AndLogicOP_37 = (res_AndLogicOP_37 && res_NotLogicOP_38);
    bool res_NotLogicOP_39 = true;
    bool res_NotLogicOP_40 = true;
    res_NotLogicOP_40 = (res_NotLogicOP_40 && ! (L_P1__GetParamSubcl50(my_id) == false));
    res_NotLogicOP_39 = (res_NotLogicOP_39 && ! res_NotLogicOP_40);
    res_AndLogicOP_37 = (res_AndLogicOP_37 && res_NotLogicOP_39);
    
    res_OrLogicOP_30 = (res_OrLogicOP_30 || res_AndLogicOP_37);
    
    res_ImpliesLogicOp_16 = (res_ImpliesLogicOp_16 && res_OrLogicOP_30);
    }
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_ImpliesLogicOp_16);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *48,49,50,*  *,*  il timer SubClass_C3_timer_T5 sia attivo
    //   *104,* e  che  *,*  il controllo SubClass_C3_controllo_C9 sia  uguale a  False 
    //   *104,* o  che  *,*  la variabile SubClass_C3_variabile_V9 non sia  minore di  *55,* 10
    bool res_OrLogicOP_41 = false;
    bool res_AndLogicOP_42 = true;
    res_AndLogicOP_42 = (res_AndLogicOP_42 && Timer_Attivo(L_P1__GetSubcl85(my_id)));
    res_AndLogicOP_42 = (res_AndLogicOP_42 && (L_P1__GetInSubcl44(my_id) == false));
    
    res_OrLogicOP_41 = (res_OrLogicOP_41 || res_AndLogicOP_42);
    bool res_NotLogicOP_43 = true;
    res_NotLogicOP_43 = (res_NotLogicOP_43 && ! (L_P1__GetSubcl79(my_id) < 10u));
    res_OrLogicOP_41 = (res_OrLogicOP_41 || res_NotLogicOP_43);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_41);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
    
    { commento: {38,}  se il contatore SubClass_C3_contatore_Co3 non è  maggiore di  commento: {54,} 12 commento: {37,} e  se la variabile SubClass_C3_variabile_V9 è  minore di  commento: {55,} 9 commento: {38,} e  se il contatore SubClass_C3_contatore_Co3 è  maggiore di  commento: {54,} 11 commento: {38,} o  se il contatore SubClass_C3_contatore_Co3 non è  diverso da  commento: {56,} 144 commento: {38,} o  se il contatore SubClass_C3_contatore_Co3 è  uguale a  commento: {53,} 13 o  se l'argomento argomento_ave2 non  è  diverso da  False  commento: {39,} , Verifica che   commento: {49,50,}  commento: {,}  la variabile SubClass_C3_variabile_V9 sia  diverso da  commento: {56,} 10
     commento: {104,} e  che  commento: {,}  il timer SubClass_C3_timer_T7 non sia disattivo
    
    
    }
*/
bool L_P1__Macro30(instance_id_t const my_id , C3_Enumerat1 argom86, bool argom87, C3_Enumerat2 argom88, C3_Enumerat1 argom89)
{
bool res_AndLogicOP_0 = true;
    
    //  *38,*  se il contatore SubClass_C3_contatore_Co3 non è  maggiore di  *54,* 12 *37,* e  se la variabile SubClass_C3_variabile_V9 è  minore di  *55,* 9 *38,* e  se il contatore SubClass_C3_contatore_Co3 è  maggiore di  *54,* 11 *38,* o  se il contatore SubClass_C3_contatore_Co3 non è  diverso da  *56,* 144 *38,* o  se il contatore SubClass_C3_contatore_Co3 è  uguale a  *53,* 13 o  se l'argomento argomento_ave2 non  è  diverso da  False  *39,* , Verifica che   *49,50,*  *,*  la variabile SubClass_C3_variabile_V9 sia  diverso da  *56,* 10
    //   *104,* e  che  *,*  il timer SubClass_C3_timer_T7 non sia disattivo
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_OrLogicOP_4 = false;
    bool res_AndLogicOP_5 = true;
    bool res_AndLogicOP_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (Counter_GetValore(L_P1__GetSubcl87(my_id)) > 12u));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_7);
    res_AndLogicOP_6 = (res_AndLogicOP_6 && (L_P1__GetSubcl79(my_id) < 9u));
    
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_AndLogicOP_6);
    res_AndLogicOP_5 = (res_AndLogicOP_5 && (Counter_GetValore(L_P1__GetSubcl87(my_id)) > 11u));
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_AndLogicOP_5);
    bool res_NotLogicOP_8 = true;
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (Counter_GetValore(L_P1__GetSubcl87(my_id)) == 144u));
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! res_NotLogicOP_9);
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_NotLogicOP_8);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_OrLogicOP_4);
    res_OrLogicOP_3 = (res_OrLogicOP_3 || (Counter_GetValore(L_P1__GetSubcl87(my_id)) == 13u));
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    bool res_NotLogicOP_10 = true;
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (argom87 == false));
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! res_NotLogicOP_11);
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_10);
    
    if(res_OrLogicOP_2){
    bool res_AndLogicOP_12 = true;
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (L_P1__GetSubcl79(my_id) == 10u));
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_NotLogicOP_13);
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! Timer_Disattivo(L_P1__GetSubcl86(my_id)));
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_NotLogicOP_14);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_AndLogicOP_12);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    
    
    return res_AndLogicOP_0;
}


// Macro valorizzate

/*
    CNL corrispondente:
    
    { commento: {[} commento: {35,}  se il controllo SubClass_C3_controllo_C9 è  diverso da  True ,  commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L4 esiste e  commento: {105,} è  diverso da  commento: {56,}  state1 , commento: {88,} quando  commento: {41,}   MainClass_C1_parametro_P1 del campo  MainClass_C1     commento: {105,} è  diverso da c270 , assegna alla macro il valore  False 
    
     commento: {46,} assegna alla macro il valore  True  commento: {],}
    }
*/
bool L_P1__Macro27(instance_id_t const my_id , C3_Enumerat1 argom71, C3_Enumerat2 argom72, C3_Enumerat4 argom73, C3_Enumerat1 argom74, bool argom75)
{
bool res_macro_val;
    
    //  *[* *35,*  se il controllo SubClass_C3_controllo_C9 è  diverso da  True ,  *111,*  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L4 esiste e  *105,* è  diverso da  *56,*  state1 , *88,* quando  *41,*   MainClass_C1_parametro_P1 del campo  MainClass_C1     *105,* è  diverso da c270
    bool res_AndLogicOP_0 = true;
    bool res_NotLogicOP_1 = true;
    res_NotLogicOP_1 = (res_NotLogicOP_1 && ! (L_P1__GetInSubcl44(my_id) == true));
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_NotLogicOP_1);
    bool res_ForAllPredicateNotEmpty_2 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl47Length(my_id); ++i)
    {
    L_P1__Recor2 it = L_P1__GetRecSubcl47(my_id,i);
    bool res_ImpliesLogicOp_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetParamMainc5(it.mainc47) == c270));
    if(res_NotLogicOP_4){
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1_C1_GetState(it.mainc47) == C1_St_state));
    res_ImpliesLogicOp_3 = (res_ImpliesLogicOp_3 && res_NotLogicOP_5);
    res_ForAllPredicateNotEmpty_2 = res_ImpliesLogicOp_3;
    if(!res_ForAllPredicateNotEmpty_2) {break;}
    }
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ForAllPredicateNotEmpty_2);
    
    if(res_AndLogicOP_0){
    
    res_macro_val = false;
    }
    else{
    res_macro_val = true;
    }
    return res_macro_val;
}

/*
    CNL corrispondente:
    
    { commento: {[} commento: {110,}  se il ripristino del timer  SubClass_C3_restoreTI_TI2 non è disattivo commento: {110,} e  se il ripristino del timer  SubClass_C3_restoreTI_TI2 è scaduto commento: {41,} e  se MainClass_C1_parametro_P2 del campo  MainClass_C1 di SubClass_C3_lista_L7 è  maggiore di  commento: {54,} 5 commento: {109,} o  se il ripristino della variabile  SubClass_C3_restoreva_RV2 non è  uguale a AC commento: {38,} e  se il contatore SubClass_C3_contatore_Co3 non è  maggiore di  commento: {54,} 15 commento: {44,} o  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C3_lista_L4 è  uguale a  False  , assegna alla macro il valore  False 
    
     commento: {46,} assegna alla macro il valore  True  commento: {],}
    }
*/
bool L_P1__Macro28(instance_id_t const my_id , C3_Enumerat2 argom76, C3_Enumerat1 argom77, C3_Enumerat3 argom78, C3_Enumerat1 argom79, bool argom80)
{
bool res_macro_val;
    
    //  *[* *110,*  se il ripristino del timer  SubClass_C3_restoreTI_TI2 non è disattivo *110,* e  se il ripristino del timer  SubClass_C3_restoreTI_TI2 è scaduto *41,* e  se MainClass_C1_parametro_P2 del campo  MainClass_C1 di SubClass_C3_lista_L7 è  maggiore di  *54,* 5 *109,* o  se il ripristino della variabile  SubClass_C3_restoreva_RV2 non è  uguale a AC *38,* e  se il contatore SubClass_C3_contatore_Co3 non è  maggiore di  *54,* 15 *44,* o  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C3_lista_L4 è  uguale a  False
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_AndLogicOP_2 = true;
    bool res_AndLogicOP_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! Timer_Disattivo(L_P1__GetSubcl83(my_id)));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_4);
    res_AndLogicOP_3 = (res_AndLogicOP_3 && Timer_Scaduto(L_P1__GetSubcl83(my_id)));
    
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_AndLogicOP_3);
    bool res_ForAllPredicate_5 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl49Length(my_id); ++i)
    {
    L_P1__Recor2 it = L_P1__GetRecSubcl49(my_id,i);
    bool res_ImpliesLogicOp_6 = true;
    res_ImpliesLogicOp_6 = (res_ImpliesLogicOp_6 && (L_P1__GetParamMainc6(it.mainc47) > 5u));
    res_ForAllPredicate_5 = res_ImpliesLogicOp_6;
    if(!res_ForAllPredicate_5) {break;}
    }
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_ForAllPredicate_5);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_2);
    bool res_AndLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetSubcl78(my_id) == ac));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_8);
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (Counter_GetValore(L_P1__GetSubcl87(my_id)) > 15u));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_9);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_7);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_ForAllPredicate_10 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl47Length(my_id); ++i)
    {
    L_P1__Recor2 it = L_P1__GetRecSubcl47(my_id,i);
    bool res_ImpliesLogicOp_11 = true;
    res_ImpliesLogicOp_11 = (res_ImpliesLogicOp_11 && (L_P1__GetMainc33(it.mainc47) == false));
    res_ForAllPredicate_10 = res_ImpliesLogicOp_11;
    if(!res_ForAllPredicate_10) {break;}
    }
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_ForAllPredicate_10);
    
    if(res_OrLogicOP_0){
    
    res_macro_val = false;
    }
    else{
    res_macro_val = true;
    }
    return res_macro_val;
}



