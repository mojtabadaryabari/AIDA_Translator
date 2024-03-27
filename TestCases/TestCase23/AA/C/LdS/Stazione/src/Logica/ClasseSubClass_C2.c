// Codice del modello 'TestCase23', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#include "Logica/ClasseMainClass_C1.h"
#include "Logica/ClasseSubClass_C2.h"
#include "Logica/ClasseSubClass_C2_priv.h"
#include "config.h"
#include "scheduler.h"


// ********** Gestione comandi automatici **********

static size_t L_P1_C2_NumAutoCmds(instance_id_t const my_id)
{
    size_t n = 0u;
    if (L_P1__GetCAEvent6(my_id)) {
        ++n;
    }
    if (L_P1__GetCAEvent7(my_id)) {
        ++n;
    }
    if (L_P1__GetCAEvent8(my_id)) {
        ++n;
    }
    return n;
}


// ********** Gestione comandi manuali **********

static void L_P1_C2_InitCmdsResponse(instance_id_t const my_id)
{
    // for each manual command of L_P1_C2
    if (L_P1__GetInEvent5(my_id)) {
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
    L_P1__SetSubcl9(my_id, 0);
    L_P1__SetSubcl11(my_id, false);
    L_P1__SetSubcl13(my_id, c120);
    L_P1__SetSubcl15(my_id, 0);
    L_P1__SetSubcl17(my_id, false);
    L_P1__SetSubcl18(my_id, false);
    L_P1__SetSubcl19(my_id, false);
    L_P1__SetSubcl20(my_id, false);
    L_P1__SetSubcl21(my_id, false);
    L_P1__SetSubcl22(my_id, false);
    L_P1__SetSubcl23(my_id, 0);
    L_P1__SetSubcl24(my_id, false);
    // init controlli precedenti
    L_P1__SetSubcl8(my_id, rossogiallo3);
    // init Timer e Counter
    Timer_AggmInit(L_P1__GetSubcl25(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl25_ID);
    Timer_Init(L_P1__GetSubcl25(my_id), 55000);
    Timer_AggmInit(L_P1__GetSubcl26(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl26_ID);
    Timer_Init(L_P1__GetSubcl26(my_id), 55000);
    Timer_AggmInit(L_P1__GetSubcl27(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl27_ID);
    Timer_Init(L_P1__GetSubcl27(my_id), 330000);
    Counter_AggmInit(L_P1__GetSubcl28(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl28_ID);
    Counter_Init(L_P1__GetSubcl28(my_id));
    Counter_AggmInit(L_P1__GetSubcl29(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl29_ID);
    Counter_Init(L_P1__GetSubcl29(my_id));
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
    L_P1__SetSubcl10(my_id, L_P1__GetSubcl9(my_id));
    L_P1__SetSubcl12(my_id, L_P1__GetSubcl11(my_id));
    L_P1__SetSubcl14(my_id, L_P1__GetSubcl13(my_id));
    L_P1__SetSubcl16(my_id, L_P1__GetSubcl15(my_id));
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
    Timer_Exec(L_P1__GetSubcl25(my_id));
    Timer_Exec(L_P1__GetSubcl26(my_id));
    Timer_Exec(L_P1__GetSubcl27(my_id));
}

void L_P1_C2_GSetSafe(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C2(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C2(proc_id);
    L_P1__SetOutSubcl(my_id, giallogiall);
    L_P1__SetOutSubcl1(my_id, rossogiallo3);
}

void L_P1_C2_GUpdatePrev(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C2(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C2(proc_id);
    L_P1__SetSubcl8(my_id, L_P1__GetInSubcl7(my_id));
    L_P1__SetSubcl10(my_id, L_P1__GetSubcl9(my_id));
    L_P1__SetSubcl12(my_id, L_P1__GetSubcl11(my_id));
    L_P1__SetSubcl14(my_id, L_P1__GetSubcl13(my_id));
    L_P1__SetSubcl16(my_id, L_P1__GetSubcl15(my_id));
}

// ********** Definizione macro **********

// Macro di effetto

/*
    CNL corrispondente:
    
    { commento: {110,}  se il ripristino del timer  SubClass_C2_restoreTI_TI1 non è disattivo commento: {38,} o  se il contatore SubClass_C2_contatore_Co5 non è  maggiore di  commento: {54,} 151 commento: {37,} e  se la variabile SubClass_C2_variabile_V6 è  uguale a  False  commento: {38,} e  se il contatore SubClass_C2_contatore_Co5 non è  minore di  commento: {55,} 13 commento: {34,} o  se il parametro SubClass_C2_parametro_P6 è  minore di  commento: {55,} 6, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V1 il valore 4
    
     ,altrimenti   Applica gli effetti
           della macro SubClass_C2_macroef_M7  commento: {73,}
    
    
      se la macro  SubClass_C2_macrova_M9 ( con argomento_a5   uguale a True ,argomento_a3   uguale a avvio ,argomento_a8   uguale a RossoGialloxVerdex  e argomento_a7   uguale a RossoGialloGiallo )   è  diverso da c180 commento: {40,} ,  commento: {44,}  se  MainClass_C1_variabile_V7 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  minore di  commento: {55,} 1, commento: {88,} quando  commento: {44,}    MainClass_C1_variabile_V7 del campo  MainClass_C1     è  maggiore di  commento: {54,} 2 commento: {34,} e  se il parametro SubClass_C2_parametro_P3 è  uguale a RossoGialloGiallo commento: {36,} e  se il timer SubClass_C2_timer_T4 è attivo, commento: {70,}Incrementa il contatore SubClass_C2_contatore_Co5
    
     ,altrimenti  commento: {72,}Azzera il contatore SubClass_C2_contatore_Co5
    
    
     commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  commento: {105,} è  uguale a  commento: {53,}  state1  o  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} e  se il contatore SubClass_C2_contatore_Co5 non è  uguale a  commento: {53,} 13, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V1 il valore 7
    
     ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V6 il valore  True 
    
    
    
    }
*/
void L_P1__Macro8(instance_id_t const my_id )
{
//  *110,*  se il ripristino del timer  SubClass_C2_restoreTI_TI1 non è disattivo *38,* o  se il contatore SubClass_C2_contatore_Co5 non è  maggiore di  *54,* 151 *37,* e  se la variabile SubClass_C2_variabile_V6 è  uguale a  False  *38,* e  se il contatore SubClass_C2_contatore_Co5 non è  minore di  *55,* 13 *34,* o  se il parametro SubClass_C2_parametro_P6 è  minore di  *55,* 6, *67,* Assegna alla variabile SubClass_C2_variabile_V1 il valore 4
    // ,altrimenti   Applica gli effetti
    //       della macro SubClass_C2_macroef_M7
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! Timer_Disattivo(L_P1__GetSubcl26(my_id)));
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_NotLogicOP_2);
    bool res_AndLogicOP_3 = true;
    bool res_AndLogicOP_4 = true;
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (Counter_GetValore(L_P1__GetSubcl28(my_id)) > 151u));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_5);
    res_AndLogicOP_4 = (res_AndLogicOP_4 && (L_P1__GetSubcl24(my_id) == false));
    
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_AndLogicOP_4);
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (Counter_GetValore(L_P1__GetSubcl28(my_id)) < 13u));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_6);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_3);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    res_OrLogicOP_0 = (res_OrLogicOP_0 || (L_P1__GetParamSubcl6(my_id) < 6u));
    
    if(res_OrLogicOP_0){
    
    L_P1__SetSubcl23(my_id,4u);
    }else{
    
    L_P1__Macro11(my_id);
    }
    //  *73,*
    //  se la macro  SubClass_C2_macrova_M9 ( con argomento_a5   uguale a True ,argomento_a3   uguale a avvio ,argomento_a8   uguale a RossoGialloxVerdex  e argomento_a7   uguale a RossoGialloGiallo )   è  diverso da c180 *40,* ,  *44,*  se  MainClass_C1_variabile_V7 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  minore di  *55,* 1, *88,* quando  *44,*    MainClass_C1_variabile_V7 del campo  MainClass_C1     è  maggiore di  *54,* 2 *34,* e  se il parametro SubClass_C2_parametro_P3 è  uguale a RossoGialloGiallo *36,* e  se il timer SubClass_C2_timer_T4 è attivo, *70,*Incrementa il contatore SubClass_C2_contatore_Co5
    // ,altrimenti  *72,*Azzera il contatore SubClass_C2_contatore_Co5
    bool res_AndLogicOP_7 = true;
    bool res_AndLogicOP_8 = true;
    bool res_AndLogicOP_9 = true;
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__Macro13(my_id,avvio,true,rossogiallo3,rossogiallo2) == c180));
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_NotLogicOP_10);
    bool res_ForAllPredicate_11 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl3Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl3(my_id,i);
    bool res_ImpliesLogicOp_12 = true;
    if((L_P1__GetMainc27(it.mainc40) > 2u)){
    res_ImpliesLogicOp_12 = (res_ImpliesLogicOp_12 && (L_P1__GetMainc27(it.mainc40) < 1u));
    }
    res_ForAllPredicate_11 = res_ImpliesLogicOp_12;
    if(!res_ForAllPredicate_11) {break;}
    }
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_ForAllPredicate_11);
    
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_AndLogicOP_9);
    res_AndLogicOP_8 = (res_AndLogicOP_8 && (L_P1__GetParamSubcl5(my_id) == rossogiallo3));
    
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_AndLogicOP_8);
    res_AndLogicOP_7 = (res_AndLogicOP_7 && Timer_Attivo(L_P1__GetSubcl27(my_id)));
    
    if(res_AndLogicOP_7){
    
    Counter_Incr(L_P1__GetSubcl28(my_id));
    }else{
    
    Counter_Res(L_P1__GetSubcl28(my_id));
    }
    //  *111,*  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  *105,* è  uguale a  *53,*  state1  o  se il controllo ConsDef  è  uguale a FALSE  *38,* e  se il contatore SubClass_C2_contatore_Co5 non è  uguale a  *53,* 13, *67,* Assegna alla variabile SubClass_C2_variabile_V1 il valore 7
    // ,altrimenti  *67,* Assegna alla variabile SubClass_C2_variabile_V6 il valore  True
    bool res_OrLogicOP_13 = false;
    bool res_ForAllPredicateNotEmpty_14 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl3Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl3(my_id,i);
    bool res_ImpliesLogicOp_15 = true;
    res_ImpliesLogicOp_15 = (res_ImpliesLogicOp_15 && (L_P1_C1_GetState(it.mainc40) == C1_St_state));
    res_ForAllPredicateNotEmpty_14 = res_ImpliesLogicOp_15;
    if(!res_ForAllPredicateNotEmpty_14) {break;}
    }
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_ForAllPredicateNotEmpty_14);
    bool res_AndLogicOP_16 = true;
    res_AndLogicOP_16 = (res_AndLogicOP_16 && (L_P1__GetInConsd1(my_id) == false));
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! (Counter_GetValore(L_P1__GetSubcl28(my_id)) == 13u));
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_NotLogicOP_17);
    
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_AndLogicOP_16);
    
    if(res_OrLogicOP_13){
    
    L_P1__SetSubcl23(my_id,7u);
    }else{
    
    L_P1__SetSubcl24(my_id,true);
    }
}

/*
    CNL corrispondente:
    
    { commento: {34,}  se lo stato  è  uguale a  commento: {53,}  state1  commento: {106,} commento: {34,} e  se il parametro SubClass_C2_parametro_P6 è  uguale a  commento: {53,} 1 commento: {35,} e  se il controllo SubClass_C2_controllo_C3 è  uguale a RossoGialloGiallo commento: {37,} o  se la variabile SubClass_C2_variabile_V1 è  minore di  commento: {55,} 3 commento: {34,} o  se il parametro SubClass_C2_parametro_P3 non è  uguale a RossoGialloGiallo, commento: {68,}Attiva il timer SubClass_C2_timer_T4
    
       
     commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  commento: {105,} è  diverso da  commento: {56,}  state1  e  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} o  se il contatore SubClass_C2_contatore_Co8 non è  maggiore di  commento: {54,} 1442 commento: {38,} e  se il contatore SubClass_C2_contatore_Co5 non è  minore di  commento: {55,} 14130 commento: {34,} o  se il parametro SubClass_C2_parametro_P6 non è  uguale a  commento: {53,} 3, commento: {66,} Assegna al comando SubClass_C2_comando_C8 il valore RossoGialloGiallo
    
       
     commento: {43,}  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L3 è disattivo commento: {34,} e  se il parametro SubClass_C2_parametro_P2 è  uguale a  commento: {53,} 10, commento: {70,}Incrementa il contatore SubClass_C2_contatore_Co8
    
     ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V1 il valore 8
    
    
    
    }
*/
void L_P1__Macro9(instance_id_t const my_id )
{
//  *34,*  se lo stato  è  uguale a  *53,*  state1  *106,* *34,* e  se il parametro SubClass_C2_parametro_P6 è  uguale a  *53,* 1 *35,* e  se il controllo SubClass_C2_controllo_C3 è  uguale a RossoGialloGiallo *37,* o  se la variabile SubClass_C2_variabile_V1 è  minore di  *55,* 3 *34,* o  se il parametro SubClass_C2_parametro_P3 non è  uguale a RossoGialloGiallo, *68,*Attiva il timer SubClass_C2_timer_T4
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_AndLogicOP_2 = true;
    bool res_AndLogicOP_3 = true;
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (L_P1_C2_GetState(my_id) == C2_St_state));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (L_P1__GetParamSubcl6(my_id) == 1u));
    
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_AndLogicOP_3);
    res_AndLogicOP_2 = (res_AndLogicOP_2 && (L_P1__GetInSubcl2(my_id) == rossogiallo3));
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_2);
    res_OrLogicOP_1 = (res_OrLogicOP_1 || (L_P1__GetSubcl23(my_id) < 3u));
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetParamSubcl5(my_id) == rossogiallo3));
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_4);
    
    if(res_OrLogicOP_0){
    
    Timer_Attiva(L_P1__GetSubcl27(my_id));
    }
    //  *111,*  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  *105,* è  diverso da  *56,*  state1  e  se il controllo ConsDef  è  uguale a FALSE  *38,* o  se il contatore SubClass_C2_contatore_Co8 non è  maggiore di  *54,* 1442 *38,* e  se il contatore SubClass_C2_contatore_Co5 non è  minore di  *55,* 14130 *34,* o  se il parametro SubClass_C2_parametro_P6 non è  uguale a  *53,* 3, *66,* Assegna al comando SubClass_C2_comando_C8 il valore RossoGialloGiallo
    bool res_OrLogicOP_5 = false;
    bool res_OrLogicOP_6 = false;
    bool res_AndLogicOP_7 = true;
    bool res_ForAllPredicateNotEmpty_8 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl3Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl3(my_id,i);
    bool res_ImpliesLogicOp_9 = true;
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1_C1_GetState(it.mainc40) == C1_St_state));
    res_ImpliesLogicOp_9 = (res_ImpliesLogicOp_9 && res_NotLogicOP_10);
    res_ForAllPredicateNotEmpty_8 = res_ImpliesLogicOp_9;
    if(!res_ForAllPredicateNotEmpty_8) {break;}
    }
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_ForAllPredicateNotEmpty_8);
    res_AndLogicOP_7 = (res_AndLogicOP_7 && (L_P1__GetInConsd1(my_id) == false));
    
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_AndLogicOP_7);
    bool res_AndLogicOP_11 = true;
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (Counter_GetValore(L_P1__GetSubcl29(my_id)) > 1442u));
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_NotLogicOP_12);
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (Counter_GetValore(L_P1__GetSubcl28(my_id)) < 14130u));
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_NotLogicOP_13);
    
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_AndLogicOP_11);
    
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_OrLogicOP_6);
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1__GetParamSubcl6(my_id) == 3u));
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_NotLogicOP_14);
    
    if(res_OrLogicOP_5){
    
    L_P1__SetOutSubcl1(my_id,rossogiallo3);
    }
    //  *43,*  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L3 è disattivo *34,* e  se il parametro SubClass_C2_parametro_P2 è  uguale a  *53,* 10, *70,*Incrementa il contatore SubClass_C2_contatore_Co8
    // ,altrimenti  *67,* Assegna alla variabile SubClass_C2_variabile_V1 il valore 8
    bool res_AndLogicOP_15 = true;
    bool res_ForAllPredicate_16 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl3Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl3(my_id,i);
    bool res_ImpliesLogicOp_17 = true;
    res_ImpliesLogicOp_17 = (res_ImpliesLogicOp_17 && Timer_Disattivo(L_P1__GetMainc38(it.mainc40)));
    res_ForAllPredicate_16 = res_ImpliesLogicOp_17;
    if(!res_ForAllPredicate_16) {break;}
    }
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_ForAllPredicate_16);
    res_AndLogicOP_15 = (res_AndLogicOP_15 && (L_P1__GetParamSubcl4(my_id) == 10u));
    
    if(res_AndLogicOP_15){
    
    Counter_Incr(L_P1__GetSubcl29(my_id));
    }else{
    
    L_P1__SetSubcl23(my_id,8u);
    }
}

/*
    CNL corrispondente:
    
    { commento: {41,}  se MainClass_C1_parametro_P5 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  commento: {105,} è  diverso da  False  o  se il controllo ConsDef  è  uguale a FALSE , commento: {66,} Assegna al comando SubClass_C2_comando_C8 il valore RossoGialloGiallo
    
       
     commento: {36,}  se il timer SubClass_C2_timer_T4 non è scaduto,  commento: {44,}  se  MainClass_C1_variabile_V7 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  maggiore di  commento: {54,} 1, commento: {88,} quando  commento: {45,}    MainClass_C1_contatore_Co2 del campo  MainClass_C1     commento: {105,} è  maggiore di  commento: {54,} 142 commento: {35,} e  se il controllo SubClass_C2_controllo_C3 è  uguale a RossoGialloGiallo o  se il controllo ConsDef  è  uguale a FALSE , commento: {70,}Incrementa il contatore SubClass_C2_contatore_Co5
    
       
     commento: {37,}  se la variabile SubClass_C2_variabile_V6 è  uguale a  False ,  commento: {41,}  se MainClass_C1_parametro_P8 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a GialloxVerdex, commento: {88,} quando  commento: {41,}   MainClass_C1_parametro_P8 del campo  MainClass_C1     commento: {105,} è  uguale a GialloxVerdex, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V1 il valore 8
    
       
     commento: {34,}  se lo stato  non è  uguale a  commento: {53,}  state1  commento: {106,} o  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} e  se la variabile SubClass_C2_variabile_V6 è  diverso da  True , commento: {67,} Assegna alla variabile SubClass_C2_variabile_V1 il valore 10
    
     ,altrimenti   Applica gli effetti
           della macro SubClass_C2_macroef_M7  commento: {73,}
    
    
     commento: {109,}  se il ripristino della variabile  SubClass_C2_restoreva_RV1 è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE , commento: {66,} Assegna al comando SubClass_C2_comando_C2 il valore GialloGiallo
    
       
    
    }
*/
void L_P1__Macro10(instance_id_t const my_id )
{
//  *41,*  se MainClass_C1_parametro_P5 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  *105,* è  diverso da  False  o  se il controllo ConsDef  è  uguale a FALSE , *66,* Assegna al comando SubClass_C2_comando_C8 il valore RossoGialloGiallo
    bool res_OrLogicOP_0 = false;
    bool res_ForAllPredicateNotEmpty_1 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl3Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl3(my_id,i);
    bool res_ImpliesLogicOp_2 = true;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__GetParamMainc8(it.mainc40) == false));
    res_ImpliesLogicOp_2 = (res_ImpliesLogicOp_2 && res_NotLogicOP_3);
    res_ForAllPredicateNotEmpty_1 = res_ImpliesLogicOp_2;
    if(!res_ForAllPredicateNotEmpty_1) {break;}
    }
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_ForAllPredicateNotEmpty_1);
    res_OrLogicOP_0 = (res_OrLogicOP_0 || (L_P1__GetInConsd1(my_id) == false));
    
    if(res_OrLogicOP_0){
    
    L_P1__SetOutSubcl1(my_id,rossogiallo3);
    }
    //  *36,*  se il timer SubClass_C2_timer_T4 non è scaduto,  *44,*  se  MainClass_C1_variabile_V7 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  maggiore di  *54,* 1, *88,* quando  *45,*    MainClass_C1_contatore_Co2 del campo  MainClass_C1     *105,* è  maggiore di  *54,* 142 *35,* e  se il controllo SubClass_C2_controllo_C3 è  uguale a RossoGialloGiallo o  se il controllo ConsDef  è  uguale a FALSE , *70,*Incrementa il contatore SubClass_C2_contatore_Co5
    bool res_OrLogicOP_4 = false;
    bool res_AndLogicOP_5 = true;
    bool res_AndLogicOP_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! Timer_Scaduto(L_P1__GetSubcl27(my_id)));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_7);
    bool res_ForAllPredicate_8 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl3Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl3(my_id,i);
    bool res_ImpliesLogicOp_9 = true;
    if((Counter_GetValore(L_P1__GetMainc39(it.mainc40)) > 142u)){
    res_ImpliesLogicOp_9 = (res_ImpliesLogicOp_9 && (L_P1__GetMainc27(it.mainc40) > 1u));
    }
    res_ForAllPredicate_8 = res_ImpliesLogicOp_9;
    if(!res_ForAllPredicate_8) {break;}
    }
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_ForAllPredicate_8);
    
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_AndLogicOP_6);
    res_AndLogicOP_5 = (res_AndLogicOP_5 && (L_P1__GetInSubcl2(my_id) == rossogiallo3));
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_AndLogicOP_5);
    res_OrLogicOP_4 = (res_OrLogicOP_4 || (L_P1__GetInConsd1(my_id) == false));
    
    if(res_OrLogicOP_4){
    
    Counter_Incr(L_P1__GetSubcl28(my_id));
    }
    //  *37,*  se la variabile SubClass_C2_variabile_V6 è  uguale a  False ,  *41,*  se MainClass_C1_parametro_P8 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a GialloxVerdex, *88,* quando  *41,*   MainClass_C1_parametro_P8 del campo  MainClass_C1     *105,* è  uguale a GialloxVerdex, *67,* Assegna alla variabile SubClass_C2_variabile_V1 il valore 8
    bool res_AndLogicOP_10 = true;
    res_AndLogicOP_10 = (res_AndLogicOP_10 && (L_P1__GetSubcl24(my_id) == false));
    bool res_ForAllPredicate_11 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl3Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl3(my_id,i);
    bool res_ImpliesLogicOp_12 = true;
    if((L_P1__GetParamMainc10(it.mainc40) == gialloxverd)){
    res_ImpliesLogicOp_12 = (res_ImpliesLogicOp_12 && (L_P1__GetParamMainc10(it.mainc40) == gialloxverd));
    }
    res_ForAllPredicate_11 = res_ImpliesLogicOp_12;
    if(!res_ForAllPredicate_11) {break;}
    }
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_ForAllPredicate_11);
    
    if(res_AndLogicOP_10){
    
    L_P1__SetSubcl23(my_id,8u);
    }
    //  *34,*  se lo stato  non è  uguale a  *53,*  state1  *106,* o  se il controllo ConsDef  è  uguale a FALSE  *37,* e  se la variabile SubClass_C2_variabile_V6 è  diverso da  True , *67,* Assegna alla variabile SubClass_C2_variabile_V1 il valore 10
    // ,altrimenti   Applica gli effetti
    //       della macro SubClass_C2_macroef_M7
    bool res_OrLogicOP_13 = false;
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1_C2_GetState(my_id) == C2_St_state));
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_NotLogicOP_14);
    bool res_AndLogicOP_15 = true;
    res_AndLogicOP_15 = (res_AndLogicOP_15 && (L_P1__GetInConsd1(my_id) == false));
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (L_P1__GetSubcl24(my_id) == true));
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_NotLogicOP_16);
    
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_AndLogicOP_15);
    
    if(res_OrLogicOP_13){
    
    L_P1__SetSubcl23(my_id,10u);
    }else{
    
    L_P1__Macro11(my_id);
    }
    //  *73,*
    // *109,*  se il ripristino della variabile  SubClass_C2_restoreva_RV1 è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE , *66,* Assegna al comando SubClass_C2_comando_C2 il valore GialloGiallo
    bool res_OrLogicOP_17 = false;
    res_OrLogicOP_17 = (res_OrLogicOP_17 || (L_P1__GetSubcl18(my_id) == true));
    res_OrLogicOP_17 = (res_OrLogicOP_17 || (L_P1__GetInConsd1(my_id) == false));
    
    if(res_OrLogicOP_17){
    
    L_P1__SetOutSubcl(my_id,giallogiall);
    }
}

/*
    CNL corrispondente:
    
    { commento: {34,}  se il parametro SubClass_C2_parametro_P2 non è  minore di  commento: {55,} 5 commento: {34,} e  se il parametro SubClass_C2_parametro_P6 è  diverso da  commento: {56,} 4 commento: {34,} e  se il parametro SubClass_C2_parametro_P6 non è  minore di  commento: {55,} 4 commento: {36,} e  se il timer SubClass_C2_timer_T4 non è scaduto, commento: {68,}Attiva il timer SubClass_C2_timer_T4
    
     ,altrimenti  commento: {66,} Assegna al comando SubClass_C2_comando_C2 il valore GialloGiallo
    
    
     commento: {45,}  se  MainClass_C1_contatore_Co2 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  commento: {105,} è  maggiore di  commento: {54,} 122, commento: {72,}Azzera il contatore SubClass_C2_contatore_Co5
    
       
     commento: {37,}  se la variabile SubClass_C2_variabile_V1 è  uguale a  commento: {53,} 10 commento: {36,} o  se il timer SubClass_C2_timer_T4 è attivo o  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} o  se la variabile SubClass_C2_variabile_V1 non è  maggiore di  commento: {54,} 5,  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V6 il valore  True  commento: {67,}
    
       
      se il ripristino dello stato  è  diverso da  commento: {56,}  state1  commento: {107,} commento: {34,} o  se il parametro SubClass_C2_parametro_P2 non è  uguale a  commento: {53,} 6 commento: {38,} o  se il contatore SubClass_C2_contatore_Co5 non è  maggiore di  commento: {54,} 151 commento: {38,} o  se il contatore SubClass_C2_contatore_Co5 è  uguale a  commento: {53,} 113054, commento: {66,} Assegna al comando SubClass_C2_comando_C8 il valore RossoGialloGiallo
    
     ,altrimenti  commento: {68,}Attiva il timer SubClass_C2_timer_T4
    
    
      se il controllo ConsDef  è  uguale a FALSE ,  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V6 il valore  False commento: {67,}
    
     ,altrimenti   commento: {67,} Assegna alla variabile SubClass_C2_variabile_V6 il valore  True  commento: {67,}
    
    
    
    }
*/
void L_P1__Macro11(instance_id_t const my_id )
{
//  *34,*  se il parametro SubClass_C2_parametro_P2 non è  minore di  *55,* 5 *34,* e  se il parametro SubClass_C2_parametro_P6 è  diverso da  *56,* 4 *34,* e  se il parametro SubClass_C2_parametro_P6 non è  minore di  *55,* 4 *36,* e  se il timer SubClass_C2_timer_T4 non è scaduto, *68,*Attiva il timer SubClass_C2_timer_T4
    // ,altrimenti  *66,* Assegna al comando SubClass_C2_comando_C2 il valore GialloGiallo
    bool res_AndLogicOP_0 = true;
    bool res_AndLogicOP_1 = true;
    bool res_AndLogicOP_2 = true;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__GetParamSubcl4(my_id) < 5u));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_3);
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetParamSubcl6(my_id) == 4u));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_4);
    
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_AndLogicOP_2);
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetParamSubcl6(my_id) < 4u));
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_5);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_AndLogicOP_1);
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! Timer_Scaduto(L_P1__GetSubcl27(my_id)));
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_NotLogicOP_6);
    
    if(res_AndLogicOP_0){
    
    Timer_Attiva(L_P1__GetSubcl27(my_id));
    }else{
    
    L_P1__SetOutSubcl(my_id,giallogiall);
    }
    //  *45,*  se  MainClass_C1_contatore_Co2 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  *105,* è  maggiore di  *54,* 122, *72,*Azzera il contatore SubClass_C2_contatore_Co5
    bool res_ForAllPredicateNotEmpty_7 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl3Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl3(my_id,i);
    bool res_ImpliesLogicOp_8 = true;
    res_ImpliesLogicOp_8 = (res_ImpliesLogicOp_8 && (Counter_GetValore(L_P1__GetMainc39(it.mainc40)) > 122u));
    res_ForAllPredicateNotEmpty_7 = res_ImpliesLogicOp_8;
    if(!res_ForAllPredicateNotEmpty_7) {break;}
    }
    if(res_ForAllPredicateNotEmpty_7){
    
    Counter_Res(L_P1__GetSubcl28(my_id));
    }
    //  *37,*  se la variabile SubClass_C2_variabile_V1 è  uguale a  *53,* 10 *36,* o  se il timer SubClass_C2_timer_T4 è attivo o  se il controllo ConsDef  è  uguale a FALSE  *37,* o  se la variabile SubClass_C2_variabile_V1 non è  maggiore di  *54,* 5,  *67,* Assegna alla variabile SubClass_C2_variabile_V6 il valore  True
    bool res_OrLogicOP_9 = false;
    bool res_OrLogicOP_10 = false;
    bool res_OrLogicOP_11 = false;
    res_OrLogicOP_11 = (res_OrLogicOP_11 || (L_P1__GetSubcl23(my_id) == 10u));
    res_OrLogicOP_11 = (res_OrLogicOP_11 || Timer_Attivo(L_P1__GetSubcl27(my_id)));
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_OrLogicOP_11);
    res_OrLogicOP_10 = (res_OrLogicOP_10 || (L_P1__GetInConsd1(my_id) == false));
    
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_OrLogicOP_10);
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (L_P1__GetSubcl23(my_id) > 5u));
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_NotLogicOP_12);
    
    if(res_OrLogicOP_9){
    
    L_P1__SetSubcl24(my_id,true);
    }
    //  *67,*
    //   
    //  se il ripristino dello stato  è  diverso da  *56,*  state1  *107,* *34,* o  se il parametro SubClass_C2_parametro_P2 non è  uguale a  *53,* 6 *38,* o  se il contatore SubClass_C2_contatore_Co5 non è  maggiore di  *54,* 151 *38,* o  se il contatore SubClass_C2_contatore_Co5 è  uguale a  *53,* 113054, *66,* Assegna al comando SubClass_C2_comando_C8 il valore RossoGialloGiallo
    // ,altrimenti  *68,*Attiva il timer SubClass_C2_timer_T4
    bool res_OrLogicOP_13 = false;
    bool res_OrLogicOP_14 = false;
    bool res_OrLogicOP_15 = false;
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (L_P1__GetStato3(my_id) == C2_St_state));
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_NotLogicOP_16);
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! (L_P1__GetParamSubcl4(my_id) == 6u));
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_NotLogicOP_17);
    
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_OrLogicOP_15);
    bool res_NotLogicOP_18 = true;
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! (Counter_GetValore(L_P1__GetSubcl28(my_id)) > 151u));
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_NotLogicOP_18);
    
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_OrLogicOP_14);
    res_OrLogicOP_13 = (res_OrLogicOP_13 || (Counter_GetValore(L_P1__GetSubcl28(my_id)) == 113054u));
    
    if(res_OrLogicOP_13){
    
    L_P1__SetOutSubcl1(my_id,rossogiallo3);
    }else{
    
    Timer_Attiva(L_P1__GetSubcl27(my_id));
    }
    //  se il controllo ConsDef  è  uguale a FALSE ,  *67,* Assegna alla variabile SubClass_C2_variabile_V6 il valore  False *67,*
    // ,altrimenti   *67,* Assegna alla variabile SubClass_C2_variabile_V6 il valore  True
    if((L_P1__GetInConsd1(my_id) == false)){
    
    L_P1__SetSubcl24(my_id,false);
    }else{
    
    L_P1__SetSubcl24(my_id,true);
    }
}

/*
    CNL corrispondente:
    
    { commento: {44,}  se  MainClass_C1_variabile_V7 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  minore di  commento: {55,} 8 commento: {34,} e  se il parametro SubClass_C2_parametro_P6 è  maggiore di  commento: {54,} 2 commento: {35,} o  se il controllo SubClass_C2_controllo_C3 non è  uguale a RossoGialloGiallo, commento: {71,}Decrementa il contatore SubClass_C2_contatore_Co8
    
       
     commento: {37,}  se la variabile SubClass_C2_variabile_V6 è  diverso da  True ,  commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L3 è  diverso da  commento: {56,}  state1 , commento: {88,} quando  commento: {42,}    MainClass_C1_controllo_C3 del campo  MainClass_C1     commento: {105,} è  uguale a  True  commento: {38,} o  se il contatore SubClass_C2_contatore_Co8 non è  minore di  commento: {55,} 155,  Applica gli effetti
           della macro SubClass_C2_macroef_M1  commento: {73,}
    
       
    
    }
*/
void L_P1__Macro12(instance_id_t const my_id )
{
//  *44,*  se  MainClass_C1_variabile_V7 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  minore di  *55,* 8 *34,* e  se il parametro SubClass_C2_parametro_P6 è  maggiore di  *54,* 2 *35,* o  se il controllo SubClass_C2_controllo_C3 non è  uguale a RossoGialloGiallo, *71,*Decrementa il contatore SubClass_C2_contatore_Co8
    bool res_OrLogicOP_0 = false;
    bool res_AndLogicOP_1 = true;
    bool res_ForAllPredicate_2 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl3Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl3(my_id,i);
    bool res_ImpliesLogicOp_3 = true;
    res_ImpliesLogicOp_3 = (res_ImpliesLogicOp_3 && (L_P1__GetMainc27(it.mainc40) < 8u));
    res_ForAllPredicate_2 = res_ImpliesLogicOp_3;
    if(!res_ForAllPredicate_2) {break;}
    }
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_ForAllPredicate_2);
    res_AndLogicOP_1 = (res_AndLogicOP_1 && (L_P1__GetParamSubcl6(my_id) > 2u));
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_1);
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetInSubcl2(my_id) == rossogiallo3));
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_4);
    
    if(res_OrLogicOP_0){
    
    Counter_Decr(L_P1__GetSubcl29(my_id));
    }
    //  *37,*  se la variabile SubClass_C2_variabile_V6 è  diverso da  True ,  *111,*  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L3 è  diverso da  *56,*  state1 , *88,* quando  *42,*    MainClass_C1_controllo_C3 del campo  MainClass_C1     *105,* è  uguale a  True  *38,* o  se il contatore SubClass_C2_contatore_Co8 non è  minore di  *55,* 155,  Applica gli effetti
    //       della macro SubClass_C2_macroef_M1
    bool res_OrLogicOP_5 = false;
    bool res_AndLogicOP_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetSubcl24(my_id) == true));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_7);
    bool res_ForAllPredicate_8 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl3Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl3(my_id,i);
    bool res_ImpliesLogicOp_9 = true;
    if((L_P1__GetInMainc5(it.mainc40) == true)){
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1_C1_GetState(it.mainc40) == C1_St_state));
    res_ImpliesLogicOp_9 = (res_ImpliesLogicOp_9 && res_NotLogicOP_10);
    }
    res_ForAllPredicate_8 = res_ImpliesLogicOp_9;
    if(!res_ForAllPredicate_8) {break;}
    }
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_ForAllPredicate_8);
    
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_AndLogicOP_6);
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (Counter_GetValore(L_P1__GetSubcl29(my_id)) < 155u));
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_NotLogicOP_11);
    
    if(res_OrLogicOP_5){
    
    L_P1__Macro8(my_id);
    }
}


// Macro di verifica

/*
    CNL corrispondente:
    
    { commento: {63,} commento: {110,}  se il ripristino del timer  SubClass_C2_restoreTI_TI1 non è disattivo e  se l'argomento argomento_ave2 non  è  diverso da GialloGiallo commento: {39,}  commento: {35,} o  se il controllo SubClass_C2_controllo_C3 è  diverso da RossoGialloGiallo commento: {38,} e  se il contatore SubClass_C2_contatore_Co8 non è  uguale a  commento: {53,} 144, Solo una delle seguenti { 
     commento: {63,} commento: {34,}  se il parametro SubClass_C2_parametro_P6 è  uguale a  commento: {53,} 3, Solo una delle seguenti { 
     commento: {62,} commento: {109,}  se il ripristino della variabile  SubClass_C2_restoreva_RV2 è  uguale a  False  o  se l'argomento argomento_ave2 non  è  diverso da GialloGiallo commento: {39,}  commento: {37,} o  se la variabile SubClass_C2_variabile_V1 non è  uguale a  commento: {53,} 8 e  se l'argomento argomento_ave2 non  è  diverso da GialloGiallo commento: {39,} , Almeno una delle seguenti { 
     commento: {61,} commento: {34,}  se lo stato  non è  uguale a  commento: {53,}  state1  commento: {106,} commento: {35,} o  se il controllo SubClass_C2_controllo_C3 non è  diverso da RossoGialloGiallo commento: {34,} o  se il parametro SubClass_C2_parametro_P3 è  diverso da RossoGialloGiallo commento: {38,} o  se il contatore SubClass_C2_contatore_Co5 non è  maggiore di  commento: {54,} 1421 e  se l'argomento argomento_ave2 è  diverso da GialloGiallo commento: {39,} , Tutte le seguenti { 
     commento: {61,} commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  commento: {105,} è  diverso da  commento: {56,}  state1  commento: {34,} o  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  commento: {54,} 3 commento: {36,} e  se il timer SubClass_C2_timer_T4 non è scaduto o  se l'argomento argomento_ave2 non  è  uguale a GialloGiallo commento: {39,}  commento: {38,} o  se il contatore SubClass_C2_contatore_Co5 è  maggiore di  commento: {54,} 153054, Tutte le seguenti { 
     commento: {63,} commento: {42,}  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a GialloxVerdex commento: {37,} e  se la variabile SubClass_C2_variabile_V6 non è  diverso da  False  commento: {34,} e  se il parametro SubClass_C2_parametro_P3 è  uguale a RossoGialloGiallo, Solo una delle seguenti { 
     commento: {63,} commento: {43,}  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  commento: {105,} è disattivo o  se l'argomento argomento_ave6 è  uguale a  False  commento: {39,}  o  se l'argomento argomento_ave2 non  è  diverso da GialloGiallo commento: {39,}  commento: {36,} o  se il timer SubClass_C2_timer_T4 è attivo, Solo una delle seguenti { 
     commento: {42,}  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  commento: {105,} è  diverso da GialloxVerdex commento: {35,} e  se il controllo SubClass_C2_controllo_C3 è  uguale a RossoGialloGiallo commento: {38,} o  se il contatore SubClass_C2_contatore_Co5 è  uguale a  commento: {53,} 122 commento: {36,} o  se il timer SubClass_C2_timer_T4 è disattivo, Verifica che   commento: {47,50,51,52,}  commento: {,}  la variabile SubClass_C2_variabile_V6 sia  uguale a  False 
     commento: {104,} o  che  commento: {37,}  la variabile SubClass_C2_variabile_V1 non sia  maggiore di  commento: {54,} 2
     commento: {104,} e  che   l'argomento argomento_ave2 sia  uguale a GialloGiallo commento: {,} 
     commento: {104,} e  che  commento: {,}  il contatore SubClass_C2_contatore_Co5 sia  maggiore di  commento: {54,} 11
     commento: {104,} o  che  commento: {34,}  il parametro SubClass_C2_parametro_P3 sia  uguale a RossoGialloGiallo
    
    
     } Verifica che   commento: {49,52,}   l'argomento argomento_ave2 non  sia  diverso da GialloGiallo commento: {,} 
     commento: {104,} e  che   l'argomento argomento_ave2 sia  diverso da GialloGiallo commento: {39,} 
     commento: {104,} o  che  commento: {,}  il timer SubClass_C2_timer_T4 sia attivo
    
    
     } Verifica che   commento: {47,48,50,52,}  commento: {,}  il controllo SubClass_C2_controllo_C3 sia  diverso da RossoGialloGiallo
     commento: {104,} e  che  commento: {,}  la variabile SubClass_C2_variabile_V1 non sia  maggiore di  commento: {54,} 9
     commento: {104,} o  che   l'argomento argomento_ave4 non  sia  diverso da avviox commento: {,} 
     commento: {104,} o  che  commento: {34,}  il parametro SubClass_C2_parametro_P6 sia  uguale a  commento: {53,} 8
    
    
     } Verifica che   commento: {49,50,51,52,}  commento: {,}  la variabile SubClass_C2_variabile_V6 non sia  diverso da  True 
     commento: {104,} e  che   l'argomento argomento_ave1 sia  diverso da  False  commento: {,} 
     commento: {104,} e  che  commento: {37,}  la variabile SubClass_C2_variabile_V6 sia  diverso da  False 
     commento: {104,} o  che  commento: {,}  il timer SubClass_C2_timer_T4 non sia disattivo
     commento: {104,} e  che  commento: {,}  il contatore SubClass_C2_contatore_Co5 non sia  maggiore di  commento: {54,} 14
     commento: {104,} e  che  commento: {36,}  il timer SubClass_C2_timer_T4 non sia attivo
    
    
     } Verifica che   commento: {51,52,}   l'argomento argomento_ave2 non  sia  uguale a GialloGiallo commento: {,} 
     commento: {104,} o  che  commento: {,}  il contatore SubClass_C2_contatore_Co8 sia  uguale a  commento: {53,} 12130
     commento: {104,} o  che  commento: {38,}  il contatore SubClass_C2_contatore_Co8 sia  minore di  commento: {55,} 1254
    
    
     } Verifica che   commento: {48,49,50,51,52,}  commento: {,}  la variabile SubClass_C2_variabile_V1 sia  diverso da  commento: {56,} 10
     commento: {104,} e  che   l'argomento argomento_ave10 non  sia  diverso da  False  commento: {,} 
     commento: {104,} o  che  commento: {,}  il controllo SubClass_C2_controllo_C3 sia  uguale a RossoGialloGiallo
     commento: {104,} o  che  commento: {,}  il timer SubClass_C2_timer_T4 non sia disattivo
     commento: {104,} o  che  commento: {,}  il contatore SubClass_C2_contatore_Co5 sia  diverso da  commento: {56,} 152
    
    
     } Verifica che   commento: {47,48,49,52,}  commento: {,}  il timer SubClass_C2_timer_T4 non sia scaduto
     commento: {104,} o  che   l'argomento argomento_ave10 sia  diverso da  False  commento: {,} 
     commento: {104,} o  che  commento: {36,}  il timer SubClass_C2_timer_T4 non sia attivo
     commento: {104,} e  che  commento: {,}  il controllo SubClass_C2_controllo_C3 non sia  uguale a RossoGialloGiallo
     commento: {104,} o  che  commento: {34,}  il parametro SubClass_C2_parametro_P3 sia  diverso da RossoGialloGiallo
     commento: {104,} o  che   l'argomento argomento_ave10 non  sia  uguale a  True  commento: {39,} 
    
    
     } Verifica che   commento: {47,48,}  commento: {34,}  il parametro SubClass_C2_parametro_P2 sia  uguale a  commento: {53,} 10
     commento: {104,} e  che  commento: {34,}  il parametro SubClass_C2_parametro_P3 non sia  diverso da RossoGialloGiallo
     commento: {104,} e  che  commento: {,}  il controllo SubClass_C2_controllo_C3 non sia  uguale a RossoGialloGiallo
    
    
    }
*/
bool L_P1__Macro14(instance_id_t const my_id , bool argom24, bool argom25, C2_Enumerat4 argom26, C2_Enumerat2 argom27, bool argom28, C2_Enumerat1 argom29)
{
bool res_AndLogicOP_0 = true;
    
    //  *63,* *110,*  se il ripristino del timer  SubClass_C2_restoreTI_TI1 non è disattivo e  se l'argomento argomento_ave2 non  è  diverso da GialloGiallo *39,*  *35,* o  se il controllo SubClass_C2_controllo_C3 è  diverso da RossoGialloGiallo *38,* e  se il contatore SubClass_C2_contatore_Co8 non è  uguale a  *53,* 144, Solo una delle seguenti { 
    //   *63,* *34,*  se il parametro SubClass_C2_parametro_P6 è  uguale a  *53,* 3, Solo una delle seguenti { 
    //   *62,* *109,*  se il ripristino della variabile  SubClass_C2_restoreva_RV2 è  uguale a  False  o  se l'argomento argomento_ave2 non  è  diverso da GialloGiallo *39,*  *37,* o  se la variabile SubClass_C2_variabile_V1 non è  uguale a  *53,* 8 e  se l'argomento argomento_ave2 non  è  diverso da GialloGiallo *39,* , Almeno una delle seguenti { 
    //   *61,* *34,*  se lo stato  non è  uguale a  *53,*  state1  *106,* *35,* o  se il controllo SubClass_C2_controllo_C3 non è  diverso da RossoGialloGiallo *34,* o  se il parametro SubClass_C2_parametro_P3 è  diverso da RossoGialloGiallo *38,* o  se il contatore SubClass_C2_contatore_Co5 non è  maggiore di  *54,* 1421 e  se l'argomento argomento_ave2 è  diverso da GialloGiallo *39,* , Tutte le seguenti { 
    //   *61,* *111,*  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  *105,* è  diverso da  *56,*  state1  *34,* o  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  *54,* 3 *36,* e  se il timer SubClass_C2_timer_T4 non è scaduto o  se l'argomento argomento_ave2 non  è  uguale a GialloGiallo *39,*  *38,* o  se il contatore SubClass_C2_contatore_Co5 è  maggiore di  *54,* 153054, Tutte le seguenti { 
    //   *63,* *42,*  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a GialloxVerdex *37,* e  se la variabile SubClass_C2_variabile_V6 non è  diverso da  False  *34,* e  se il parametro SubClass_C2_parametro_P3 è  uguale a RossoGialloGiallo, Solo una delle seguenti { 
    //   *63,* *43,*  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  *105,* è disattivo o  se l'argomento argomento_ave6 è  uguale a  False  *39,*  o  se l'argomento argomento_ave2 non  è  diverso da GialloGiallo *39,*  *36,* o  se il timer SubClass_C2_timer_T4 è attivo, Solo una delle seguenti { 
    //   *42,*  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  *105,* è  diverso da GialloxVerdex *35,* e  se il controllo SubClass_C2_controllo_C3 è  uguale a RossoGialloGiallo *38,* o  se il contatore SubClass_C2_contatore_Co5 è  uguale a  *53,* 122 *36,* o  se il timer SubClass_C2_timer_T4 è disattivo, Verifica che   *47,50,51,52,*  *,*  la variabile SubClass_C2_variabile_V6 sia  uguale a  False 
    //   *104,* o  che  *37,*  la variabile SubClass_C2_variabile_V1 non sia  maggiore di  *54,* 2
    //   *104,* e  che   l'argomento argomento_ave2 sia  uguale a GialloGiallo *,* 
    //   *104,* e  che  *,*  il contatore SubClass_C2_contatore_Co5 sia  maggiore di  *54,* 11
    //   *104,* o  che  *34,*  il parametro SubClass_C2_parametro_P3 sia  uguale a RossoGialloGiallo
    //   } Verifica che   *49,52,*   l'argomento argomento_ave2 non  sia  diverso da GialloGiallo *,* 
    //   *104,* e  che   l'argomento argomento_ave2 sia  diverso da GialloGiallo *39,* 
    //   *104,* o  che  *,*  il timer SubClass_C2_timer_T4 sia attivo
    //   } Verifica che   *47,48,50,52,*  *,*  il controllo SubClass_C2_controllo_C3 sia  diverso da RossoGialloGiallo
    //   *104,* e  che  *,*  la variabile SubClass_C2_variabile_V1 non sia  maggiore di  *54,* 9
    //   *104,* o  che   l'argomento argomento_ave4 non  sia  diverso da avviox *,* 
    //   *104,* o  che  *34,*  il parametro SubClass_C2_parametro_P6 sia  uguale a  *53,* 8
    //   } Verifica che   *49,50,51,52,*  *,*  la variabile SubClass_C2_variabile_V6 non sia  diverso da  True 
    //   *104,* e  che   l'argomento argomento_ave1 sia  diverso da  False  *,* 
    //   *104,* e  che  *37,*  la variabile SubClass_C2_variabile_V6 sia  diverso da  False 
    //   *104,* o  che  *,*  il timer SubClass_C2_timer_T4 non sia disattivo
    //   *104,* e  che  *,*  il contatore SubClass_C2_contatore_Co5 non sia  maggiore di  *54,* 14
    //   *104,* e  che  *36,*  il timer SubClass_C2_timer_T4 non sia attivo
    //   } Verifica che   *51,52,*   l'argomento argomento_ave2 non  sia  uguale a GialloGiallo *,* 
    //   *104,* o  che  *,*  il contatore SubClass_C2_contatore_Co8 sia  uguale a  *53,* 12130
    //   *104,* o  che  *38,*  il contatore SubClass_C2_contatore_Co8 sia  minore di  *55,* 1254
    //   } Verifica che   *48,49,50,51,52,*  *,*  la variabile SubClass_C2_variabile_V1 sia  diverso da  *56,* 10
    //   *104,* e  che   l'argomento argomento_ave10 non  sia  diverso da  False  *,* 
    //   *104,* o  che  *,*  il controllo SubClass_C2_controllo_C3 sia  uguale a RossoGialloGiallo
    //   *104,* o  che  *,*  il timer SubClass_C2_timer_T4 non sia disattivo
    //   *104,* o  che  *,*  il contatore SubClass_C2_contatore_Co5 sia  diverso da  *56,* 152
    //   } Verifica che   *47,48,49,52,*  *,*  il timer SubClass_C2_timer_T4 non sia scaduto
    //   *104,* o  che   l'argomento argomento_ave10 sia  diverso da  False  *,* 
    //   *104,* o  che  *36,*  il timer SubClass_C2_timer_T4 non sia attivo
    //   *104,* e  che  *,*  il controllo SubClass_C2_controllo_C3 non sia  uguale a RossoGialloGiallo
    //   *104,* o  che  *34,*  il parametro SubClass_C2_parametro_P3 sia  diverso da RossoGialloGiallo
    //   *104,* o  che   l'argomento argomento_ave10 non  sia  uguale a  True  *39,* 
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_AndLogicOP_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! Timer_Disattivo(L_P1__GetSubcl26(my_id)));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_4);
    bool res_NotLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (argom26 == giallogiall));
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! res_NotLogicOP_6);
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_5);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_3);
    bool res_AndLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetInSubcl2(my_id) == rossogiallo3));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_8);
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (Counter_GetValore(L_P1__GetSubcl29(my_id)) == 144u));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_9);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_7);
    
    if(res_OrLogicOP_2){
    bool res_XorLogicOP_10 = true;
    int xorIndex_res_XorLogicOP_10 = 0;
    bool res_ImpliesLogicOp_11 = true;
    if((L_P1__GetParamSubcl6(my_id) == 3u)){
    bool res_XorLogicOP_12 = true;
    int xorIndex_res_XorLogicOP_12 = 0;
    bool res_ImpliesLogicOp_13 = true;
    bool res_OrLogicOP_14 = false;
    bool res_OrLogicOP_15 = false;
    res_OrLogicOP_15 = (res_OrLogicOP_15 || (L_P1__GetSubcl20(my_id) == false));
    bool res_NotLogicOP_16 = true;
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! (argom26 == giallogiall));
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! res_NotLogicOP_17);
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_NotLogicOP_16);
    
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_OrLogicOP_15);
    bool res_AndLogicOP_18 = true;
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (L_P1__GetSubcl23(my_id) == 8u));
    res_AndLogicOP_18 = (res_AndLogicOP_18 && res_NotLogicOP_19);
    bool res_NotLogicOP_20 = true;
    bool res_NotLogicOP_21 = true;
    res_NotLogicOP_21 = (res_NotLogicOP_21 && ! (argom26 == giallogiall));
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! res_NotLogicOP_21);
    res_AndLogicOP_18 = (res_AndLogicOP_18 && res_NotLogicOP_20);
    
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_AndLogicOP_18);
    
    if(res_OrLogicOP_14){
    bool res_OrLogicOP_22 = false;
    bool res_ImpliesLogicOp_23 = true;
    bool res_OrLogicOP_24 = false;
    bool res_OrLogicOP_25 = false;
    bool res_OrLogicOP_26 = false;
    bool res_NotLogicOP_27 = true;
    res_NotLogicOP_27 = (res_NotLogicOP_27 && ! (L_P1_C2_GetState(my_id) == C2_St_state));
    res_OrLogicOP_26 = (res_OrLogicOP_26 || res_NotLogicOP_27);
    bool res_NotLogicOP_28 = true;
    bool res_NotLogicOP_29 = true;
    res_NotLogicOP_29 = (res_NotLogicOP_29 && ! (L_P1__GetInSubcl2(my_id) == rossogiallo3));
    res_NotLogicOP_28 = (res_NotLogicOP_28 && ! res_NotLogicOP_29);
    res_OrLogicOP_26 = (res_OrLogicOP_26 || res_NotLogicOP_28);
    
    res_OrLogicOP_25 = (res_OrLogicOP_25 || res_OrLogicOP_26);
    bool res_NotLogicOP_30 = true;
    res_NotLogicOP_30 = (res_NotLogicOP_30 && ! (L_P1__GetParamSubcl5(my_id) == rossogiallo3));
    res_OrLogicOP_25 = (res_OrLogicOP_25 || res_NotLogicOP_30);
    
    res_OrLogicOP_24 = (res_OrLogicOP_24 || res_OrLogicOP_25);
    bool res_AndLogicOP_31 = true;
    bool res_NotLogicOP_32 = true;
    res_NotLogicOP_32 = (res_NotLogicOP_32 && ! (Counter_GetValore(L_P1__GetSubcl28(my_id)) > 1421u));
    res_AndLogicOP_31 = (res_AndLogicOP_31 && res_NotLogicOP_32);
    bool res_NotLogicOP_33 = true;
    res_NotLogicOP_33 = (res_NotLogicOP_33 && ! (argom26 == giallogiall));
    res_AndLogicOP_31 = (res_AndLogicOP_31 && res_NotLogicOP_33);
    
    res_OrLogicOP_24 = (res_OrLogicOP_24 || res_AndLogicOP_31);
    
    if(res_OrLogicOP_24){
    bool res_AndLogicOP_34 = true;
    bool res_ImpliesLogicOp_35 = true;
    bool res_OrLogicOP_36 = false;
    bool res_OrLogicOP_37 = false;
    bool res_OrLogicOP_38 = false;
    bool res_ForAllPredicateNotEmpty_39 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl3Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl3(my_id,i);
    bool res_ImpliesLogicOp_40 = true;
    bool res_NotLogicOP_41 = true;
    res_NotLogicOP_41 = (res_NotLogicOP_41 && ! (L_P1_C1_GetState(it.mainc40) == C1_St_state));
    res_ImpliesLogicOp_40 = (res_ImpliesLogicOp_40 && res_NotLogicOP_41);
    res_ForAllPredicateNotEmpty_39 = res_ImpliesLogicOp_40;
    if(!res_ForAllPredicateNotEmpty_39) {break;}
    }
    res_OrLogicOP_38 = (res_OrLogicOP_38 || res_ForAllPredicateNotEmpty_39);
    bool res_AndLogicOP_42 = true;
    bool res_NotLogicOP_43 = true;
    res_NotLogicOP_43 = (res_NotLogicOP_43 && ! (L_P1__GetParamSubcl6(my_id) > 3u));
    res_AndLogicOP_42 = (res_AndLogicOP_42 && res_NotLogicOP_43);
    bool res_NotLogicOP_44 = true;
    res_NotLogicOP_44 = (res_NotLogicOP_44 && ! Timer_Scaduto(L_P1__GetSubcl27(my_id)));
    res_AndLogicOP_42 = (res_AndLogicOP_42 && res_NotLogicOP_44);
    
    res_OrLogicOP_38 = (res_OrLogicOP_38 || res_AndLogicOP_42);
    
    res_OrLogicOP_37 = (res_OrLogicOP_37 || res_OrLogicOP_38);
    bool res_NotLogicOP_45 = true;
    res_NotLogicOP_45 = (res_NotLogicOP_45 && ! (argom26 == giallogiall));
    res_OrLogicOP_37 = (res_OrLogicOP_37 || res_NotLogicOP_45);
    
    res_OrLogicOP_36 = (res_OrLogicOP_36 || res_OrLogicOP_37);
    res_OrLogicOP_36 = (res_OrLogicOP_36 || (Counter_GetValore(L_P1__GetSubcl28(my_id)) > 153054u));
    
    if(res_OrLogicOP_36){
    bool res_AndLogicOP_46 = true;
    bool res_ImpliesLogicOp_47 = true;
    bool res_AndLogicOP_48 = true;
    bool res_AndLogicOP_49 = true;
    bool res_ForAllPredicate_50 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl3Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl3(my_id,i);
    bool res_ImpliesLogicOp_51 = true;
    res_ImpliesLogicOp_51 = (res_ImpliesLogicOp_51 && (L_P1__GetInMainc6(it.mainc40) == gialloxverd));
    res_ForAllPredicate_50 = res_ImpliesLogicOp_51;
    if(!res_ForAllPredicate_50) {break;}
    }
    res_AndLogicOP_49 = (res_AndLogicOP_49 && res_ForAllPredicate_50);
    bool res_NotLogicOP_52 = true;
    bool res_NotLogicOP_53 = true;
    res_NotLogicOP_53 = (res_NotLogicOP_53 && ! (L_P1__GetSubcl24(my_id) == false));
    res_NotLogicOP_52 = (res_NotLogicOP_52 && ! res_NotLogicOP_53);
    res_AndLogicOP_49 = (res_AndLogicOP_49 && res_NotLogicOP_52);
    
    res_AndLogicOP_48 = (res_AndLogicOP_48 && res_AndLogicOP_49);
    res_AndLogicOP_48 = (res_AndLogicOP_48 && (L_P1__GetParamSubcl5(my_id) == rossogiallo3));
    
    if(res_AndLogicOP_48){
    bool res_XorLogicOP_54 = true;
    int xorIndex_res_XorLogicOP_54 = 0;
    bool res_ImpliesLogicOp_55 = true;
    bool res_OrLogicOP_56 = false;
    bool res_OrLogicOP_57 = false;
    bool res_OrLogicOP_58 = false;
    bool res_ForAllPredicateNotEmpty_59 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl3Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl3(my_id,i);
    bool res_ImpliesLogicOp_60 = true;
    res_ImpliesLogicOp_60 = (res_ImpliesLogicOp_60 && Timer_Disattivo(L_P1__GetMainc38(it.mainc40)));
    res_ForAllPredicateNotEmpty_59 = res_ImpliesLogicOp_60;
    if(!res_ForAllPredicateNotEmpty_59) {break;}
    }
    res_OrLogicOP_58 = (res_OrLogicOP_58 || res_ForAllPredicateNotEmpty_59);
    res_OrLogicOP_58 = (res_OrLogicOP_58 || (argom28 == false));
    
    res_OrLogicOP_57 = (res_OrLogicOP_57 || res_OrLogicOP_58);
    bool res_NotLogicOP_61 = true;
    bool res_NotLogicOP_62 = true;
    res_NotLogicOP_62 = (res_NotLogicOP_62 && ! (argom26 == giallogiall));
    res_NotLogicOP_61 = (res_NotLogicOP_61 && ! res_NotLogicOP_62);
    res_OrLogicOP_57 = (res_OrLogicOP_57 || res_NotLogicOP_61);
    
    res_OrLogicOP_56 = (res_OrLogicOP_56 || res_OrLogicOP_57);
    res_OrLogicOP_56 = (res_OrLogicOP_56 || Timer_Attivo(L_P1__GetSubcl27(my_id)));
    
    if(res_OrLogicOP_56){
    bool res_ImpliesLogicOp_63 = true;
    bool res_OrLogicOP_64 = false;
    bool res_OrLogicOP_65 = false;
    bool res_AndLogicOP_66 = true;
    bool res_ForAllPredicateNotEmpty_67 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl3Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl3(my_id,i);
    bool res_ImpliesLogicOp_68 = true;
    bool res_NotLogicOP_69 = true;
    res_NotLogicOP_69 = (res_NotLogicOP_69 && ! (L_P1__GetInMainc6(it.mainc40) == gialloxverd));
    res_ImpliesLogicOp_68 = (res_ImpliesLogicOp_68 && res_NotLogicOP_69);
    res_ForAllPredicateNotEmpty_67 = res_ImpliesLogicOp_68;
    if(!res_ForAllPredicateNotEmpty_67) {break;}
    }
    res_AndLogicOP_66 = (res_AndLogicOP_66 && res_ForAllPredicateNotEmpty_67);
    res_AndLogicOP_66 = (res_AndLogicOP_66 && (L_P1__GetInSubcl2(my_id) == rossogiallo3));
    
    res_OrLogicOP_65 = (res_OrLogicOP_65 || res_AndLogicOP_66);
    res_OrLogicOP_65 = (res_OrLogicOP_65 || (Counter_GetValore(L_P1__GetSubcl28(my_id)) == 122u));
    
    res_OrLogicOP_64 = (res_OrLogicOP_64 || res_OrLogicOP_65);
    res_OrLogicOP_64 = (res_OrLogicOP_64 || Timer_Disattivo(L_P1__GetSubcl27(my_id)));
    
    if(res_OrLogicOP_64){
    bool res_OrLogicOP_70 = false;
    bool res_OrLogicOP_71 = false;
    res_OrLogicOP_71 = (res_OrLogicOP_71 || (L_P1__GetSubcl24(my_id) == false));
    bool res_AndLogicOP_72 = true;
    bool res_AndLogicOP_73 = true;
    bool res_NotLogicOP_74 = true;
    res_NotLogicOP_74 = (res_NotLogicOP_74 && ! (L_P1__GetSubcl23(my_id) > 2u));
    res_AndLogicOP_73 = (res_AndLogicOP_73 && res_NotLogicOP_74);
    res_AndLogicOP_73 = (res_AndLogicOP_73 && (argom26 == giallogiall));
    
    res_AndLogicOP_72 = (res_AndLogicOP_72 && res_AndLogicOP_73);
    res_AndLogicOP_72 = (res_AndLogicOP_72 && (Counter_GetValore(L_P1__GetSubcl28(my_id)) > 11u));
    
    res_OrLogicOP_71 = (res_OrLogicOP_71 || res_AndLogicOP_72);
    
    res_OrLogicOP_70 = (res_OrLogicOP_70 || res_OrLogicOP_71);
    res_OrLogicOP_70 = (res_OrLogicOP_70 || (L_P1__GetParamSubcl5(my_id) == rossogiallo3));
    
    res_ImpliesLogicOp_63 = (res_ImpliesLogicOp_63 && res_OrLogicOP_70);
    }
    res_ImpliesLogicOp_55 = (res_ImpliesLogicOp_55 && res_ImpliesLogicOp_63);
    }
    if(res_ImpliesLogicOp_55){
    xorIndex_res_XorLogicOP_54 = (xorIndex_res_XorLogicOP_54 + 1);
    }
    bool res_OrLogicOP_75 = false;
    bool res_AndLogicOP_76 = true;
    bool res_NotLogicOP_77 = true;
    bool res_NotLogicOP_78 = true;
    res_NotLogicOP_78 = (res_NotLogicOP_78 && ! (argom26 == giallogiall));
    res_NotLogicOP_77 = (res_NotLogicOP_77 && ! res_NotLogicOP_78);
    res_AndLogicOP_76 = (res_AndLogicOP_76 && res_NotLogicOP_77);
    bool res_NotLogicOP_79 = true;
    res_NotLogicOP_79 = (res_NotLogicOP_79 && ! (argom26 == giallogiall));
    res_AndLogicOP_76 = (res_AndLogicOP_76 && res_NotLogicOP_79);
    
    res_OrLogicOP_75 = (res_OrLogicOP_75 || res_AndLogicOP_76);
    res_OrLogicOP_75 = (res_OrLogicOP_75 || Timer_Attivo(L_P1__GetSubcl27(my_id)));
    
    if(res_OrLogicOP_75){
    xorIndex_res_XorLogicOP_54 = (xorIndex_res_XorLogicOP_54 + 1);
    }
    
    res_XorLogicOP_54 = (res_XorLogicOP_54 && (xorIndex_res_XorLogicOP_54 == 1));
    res_ImpliesLogicOp_47 = (res_ImpliesLogicOp_47 && res_XorLogicOP_54);
    }
    res_AndLogicOP_46 = (res_AndLogicOP_46 && res_ImpliesLogicOp_47);
    bool res_OrLogicOP_80 = false;
    bool res_OrLogicOP_81 = false;
    bool res_AndLogicOP_82 = true;
    bool res_NotLogicOP_83 = true;
    res_NotLogicOP_83 = (res_NotLogicOP_83 && ! (L_P1__GetInSubcl2(my_id) == rossogiallo3));
    res_AndLogicOP_82 = (res_AndLogicOP_82 && res_NotLogicOP_83);
    bool res_NotLogicOP_84 = true;
    res_NotLogicOP_84 = (res_NotLogicOP_84 && ! (L_P1__GetSubcl23(my_id) > 9u));
    res_AndLogicOP_82 = (res_AndLogicOP_82 && res_NotLogicOP_84);
    
    res_OrLogicOP_81 = (res_OrLogicOP_81 || res_AndLogicOP_82);
    bool res_NotLogicOP_85 = true;
    bool res_NotLogicOP_86 = true;
    res_NotLogicOP_86 = (res_NotLogicOP_86 && ! (argom27 == avviox));
    res_NotLogicOP_85 = (res_NotLogicOP_85 && ! res_NotLogicOP_86);
    res_OrLogicOP_81 = (res_OrLogicOP_81 || res_NotLogicOP_85);
    
    res_OrLogicOP_80 = (res_OrLogicOP_80 || res_OrLogicOP_81);
    res_OrLogicOP_80 = (res_OrLogicOP_80 || (L_P1__GetParamSubcl6(my_id) == 8u));
    
    res_AndLogicOP_46 = (res_AndLogicOP_46 && res_OrLogicOP_80);
    
    res_ImpliesLogicOp_35 = (res_ImpliesLogicOp_35 && res_AndLogicOP_46);
    }
    res_AndLogicOP_34 = (res_AndLogicOP_34 && res_ImpliesLogicOp_35);
    bool res_OrLogicOP_87 = false;
    bool res_AndLogicOP_88 = true;
    bool res_AndLogicOP_89 = true;
    bool res_NotLogicOP_90 = true;
    bool res_NotLogicOP_91 = true;
    res_NotLogicOP_91 = (res_NotLogicOP_91 && ! (L_P1__GetSubcl24(my_id) == true));
    res_NotLogicOP_90 = (res_NotLogicOP_90 && ! res_NotLogicOP_91);
    res_AndLogicOP_89 = (res_AndLogicOP_89 && res_NotLogicOP_90);
    bool res_NotLogicOP_92 = true;
    res_NotLogicOP_92 = (res_NotLogicOP_92 && ! (argom24 == false));
    res_AndLogicOP_89 = (res_AndLogicOP_89 && res_NotLogicOP_92);
    
    res_AndLogicOP_88 = (res_AndLogicOP_88 && res_AndLogicOP_89);
    bool res_NotLogicOP_93 = true;
    res_NotLogicOP_93 = (res_NotLogicOP_93 && ! (L_P1__GetSubcl24(my_id) == false));
    res_AndLogicOP_88 = (res_AndLogicOP_88 && res_NotLogicOP_93);
    
    res_OrLogicOP_87 = (res_OrLogicOP_87 || res_AndLogicOP_88);
    bool res_AndLogicOP_94 = true;
    bool res_AndLogicOP_95 = true;
    bool res_NotLogicOP_96 = true;
    res_NotLogicOP_96 = (res_NotLogicOP_96 && ! Timer_Disattivo(L_P1__GetSubcl27(my_id)));
    res_AndLogicOP_95 = (res_AndLogicOP_95 && res_NotLogicOP_96);
    bool res_NotLogicOP_97 = true;
    res_NotLogicOP_97 = (res_NotLogicOP_97 && ! (Counter_GetValore(L_P1__GetSubcl28(my_id)) > 14u));
    res_AndLogicOP_95 = (res_AndLogicOP_95 && res_NotLogicOP_97);
    
    res_AndLogicOP_94 = (res_AndLogicOP_94 && res_AndLogicOP_95);
    bool res_NotLogicOP_98 = true;
    res_NotLogicOP_98 = (res_NotLogicOP_98 && ! Timer_Attivo(L_P1__GetSubcl27(my_id)));
    res_AndLogicOP_94 = (res_AndLogicOP_94 && res_NotLogicOP_98);
    
    res_OrLogicOP_87 = (res_OrLogicOP_87 || res_AndLogicOP_94);
    
    res_AndLogicOP_34 = (res_AndLogicOP_34 && res_OrLogicOP_87);
    
    res_ImpliesLogicOp_23 = (res_ImpliesLogicOp_23 && res_AndLogicOP_34);
    }
    res_OrLogicOP_22 = (res_OrLogicOP_22 || res_ImpliesLogicOp_23);
    bool res_OrLogicOP_99 = false;
    bool res_OrLogicOP_100 = false;
    bool res_NotLogicOP_101 = true;
    res_NotLogicOP_101 = (res_NotLogicOP_101 && ! (argom26 == giallogiall));
    res_OrLogicOP_100 = (res_OrLogicOP_100 || res_NotLogicOP_101);
    res_OrLogicOP_100 = (res_OrLogicOP_100 || (Counter_GetValore(L_P1__GetSubcl29(my_id)) == 12130u));
    
    res_OrLogicOP_99 = (res_OrLogicOP_99 || res_OrLogicOP_100);
    res_OrLogicOP_99 = (res_OrLogicOP_99 || (Counter_GetValore(L_P1__GetSubcl29(my_id)) < 1254u));
    
    res_OrLogicOP_22 = (res_OrLogicOP_22 || res_OrLogicOP_99);
    
    res_ImpliesLogicOp_13 = (res_ImpliesLogicOp_13 && res_OrLogicOP_22);
    }
    if(res_ImpliesLogicOp_13){
    xorIndex_res_XorLogicOP_12 = (xorIndex_res_XorLogicOP_12 + 1);
    }
    bool res_OrLogicOP_102 = false;
    bool res_OrLogicOP_103 = false;
    bool res_OrLogicOP_104 = false;
    bool res_AndLogicOP_105 = true;
    bool res_NotLogicOP_106 = true;
    res_NotLogicOP_106 = (res_NotLogicOP_106 && ! (L_P1__GetSubcl23(my_id) == 10u));
    res_AndLogicOP_105 = (res_AndLogicOP_105 && res_NotLogicOP_106);
    bool res_NotLogicOP_107 = true;
    bool res_NotLogicOP_108 = true;
    res_NotLogicOP_108 = (res_NotLogicOP_108 && ! (argom25 == false));
    res_NotLogicOP_107 = (res_NotLogicOP_107 && ! res_NotLogicOP_108);
    res_AndLogicOP_105 = (res_AndLogicOP_105 && res_NotLogicOP_107);
    
    res_OrLogicOP_104 = (res_OrLogicOP_104 || res_AndLogicOP_105);
    res_OrLogicOP_104 = (res_OrLogicOP_104 || (L_P1__GetInSubcl2(my_id) == rossogiallo3));
    
    res_OrLogicOP_103 = (res_OrLogicOP_103 || res_OrLogicOP_104);
    bool res_NotLogicOP_109 = true;
    res_NotLogicOP_109 = (res_NotLogicOP_109 && ! Timer_Disattivo(L_P1__GetSubcl27(my_id)));
    res_OrLogicOP_103 = (res_OrLogicOP_103 || res_NotLogicOP_109);
    
    res_OrLogicOP_102 = (res_OrLogicOP_102 || res_OrLogicOP_103);
    bool res_NotLogicOP_110 = true;
    res_NotLogicOP_110 = (res_NotLogicOP_110 && ! (Counter_GetValore(L_P1__GetSubcl28(my_id)) == 152u));
    res_OrLogicOP_102 = (res_OrLogicOP_102 || res_NotLogicOP_110);
    
    if(res_OrLogicOP_102){
    xorIndex_res_XorLogicOP_12 = (xorIndex_res_XorLogicOP_12 + 1);
    }
    
    res_XorLogicOP_12 = (res_XorLogicOP_12 && (xorIndex_res_XorLogicOP_12 == 1));
    res_ImpliesLogicOp_11 = (res_ImpliesLogicOp_11 && res_XorLogicOP_12);
    }
    if(res_ImpliesLogicOp_11){
    xorIndex_res_XorLogicOP_10 = (xorIndex_res_XorLogicOP_10 + 1);
    }
    bool res_OrLogicOP_111 = false;
    bool res_OrLogicOP_112 = false;
    bool res_OrLogicOP_113 = false;
    bool res_OrLogicOP_114 = false;
    bool res_NotLogicOP_115 = true;
    res_NotLogicOP_115 = (res_NotLogicOP_115 && ! Timer_Scaduto(L_P1__GetSubcl27(my_id)));
    res_OrLogicOP_114 = (res_OrLogicOP_114 || res_NotLogicOP_115);
    bool res_NotLogicOP_116 = true;
    res_NotLogicOP_116 = (res_NotLogicOP_116 && ! (argom25 == false));
    res_OrLogicOP_114 = (res_OrLogicOP_114 || res_NotLogicOP_116);
    
    res_OrLogicOP_113 = (res_OrLogicOP_113 || res_OrLogicOP_114);
    bool res_AndLogicOP_117 = true;
    bool res_NotLogicOP_118 = true;
    res_NotLogicOP_118 = (res_NotLogicOP_118 && ! Timer_Attivo(L_P1__GetSubcl27(my_id)));
    res_AndLogicOP_117 = (res_AndLogicOP_117 && res_NotLogicOP_118);
    bool res_NotLogicOP_119 = true;
    res_NotLogicOP_119 = (res_NotLogicOP_119 && ! (L_P1__GetInSubcl2(my_id) == rossogiallo3));
    res_AndLogicOP_117 = (res_AndLogicOP_117 && res_NotLogicOP_119);
    
    res_OrLogicOP_113 = (res_OrLogicOP_113 || res_AndLogicOP_117);
    
    res_OrLogicOP_112 = (res_OrLogicOP_112 || res_OrLogicOP_113);
    bool res_NotLogicOP_120 = true;
    res_NotLogicOP_120 = (res_NotLogicOP_120 && ! (L_P1__GetParamSubcl5(my_id) == rossogiallo3));
    res_OrLogicOP_112 = (res_OrLogicOP_112 || res_NotLogicOP_120);
    
    res_OrLogicOP_111 = (res_OrLogicOP_111 || res_OrLogicOP_112);
    bool res_NotLogicOP_121 = true;
    res_NotLogicOP_121 = (res_NotLogicOP_121 && ! (argom25 == true));
    res_OrLogicOP_111 = (res_OrLogicOP_111 || res_NotLogicOP_121);
    
    if(res_OrLogicOP_111){
    xorIndex_res_XorLogicOP_10 = (xorIndex_res_XorLogicOP_10 + 1);
    }
    
    res_XorLogicOP_10 = (res_XorLogicOP_10 && (xorIndex_res_XorLogicOP_10 == 1));
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_XorLogicOP_10);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *47,48,*  *34,*  il parametro SubClass_C2_parametro_P2 sia  uguale a  *53,* 10
    //   *104,* e  che  *34,*  il parametro SubClass_C2_parametro_P3 non sia  diverso da RossoGialloGiallo
    //   *104,* e  che  *,*  il controllo SubClass_C2_controllo_C3 non sia  uguale a RossoGialloGiallo
    bool res_AndLogicOP_122 = true;
    bool res_AndLogicOP_123 = true;
    res_AndLogicOP_123 = (res_AndLogicOP_123 && (L_P1__GetParamSubcl4(my_id) == 10u));
    bool res_NotLogicOP_124 = true;
    bool res_NotLogicOP_125 = true;
    res_NotLogicOP_125 = (res_NotLogicOP_125 && ! (L_P1__GetParamSubcl5(my_id) == rossogiallo3));
    res_NotLogicOP_124 = (res_NotLogicOP_124 && ! res_NotLogicOP_125);
    res_AndLogicOP_123 = (res_AndLogicOP_123 && res_NotLogicOP_124);
    
    res_AndLogicOP_122 = (res_AndLogicOP_122 && res_AndLogicOP_123);
    bool res_NotLogicOP_126 = true;
    res_NotLogicOP_126 = (res_NotLogicOP_126 && ! (L_P1__GetInSubcl2(my_id) == rossogiallo3));
    res_AndLogicOP_122 = (res_AndLogicOP_122 && res_NotLogicOP_126);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_AndLogicOP_122);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
     
    { commento: {34,}  se il parametro SubClass_C2_parametro_P6 non è  diverso da  commento: {56,} 2 commento: {35,} e  se il controllo SubClass_C2_controllo_C3 non è  uguale a RossoGialloGiallo commento: {34,} o  se il parametro SubClass_C2_parametro_P3 è  uguale a RossoGialloGiallo o  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} e  se il timer SubClass_C2_timer_T4 non è scaduto commento: {38,} e  se il contatore SubClass_C2_contatore_Co8 non è  maggiore di  commento: {54,} 151, Verifica che   commento: {47,48,50,51,}  commento: {34,}  il parametro SubClass_C2_parametro_P6 sia  diverso da  commento: {56,} 4
     commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} e  che  commento: {,}  il contatore SubClass_C2_contatore_Co5 sia  uguale a  commento: {53,} 1130
     commento: {104,} e  che  commento: {,}  la variabile SubClass_C2_variabile_V6 non sia  uguale a  False 
     commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
    
    
    }
*/
bool L_P1__Macro15(instance_id_t const my_id )
{
bool res_AndLogicOP_0 = true;
    
    //  *34,*  se il parametro SubClass_C2_parametro_P6 non è  diverso da  *56,* 2 *35,* e  se il controllo SubClass_C2_controllo_C3 non è  uguale a RossoGialloGiallo *34,* o  se il parametro SubClass_C2_parametro_P3 è  uguale a RossoGialloGiallo o  se il controllo ConsDef  è  uguale a FALSE  *36,* e  se il timer SubClass_C2_timer_T4 non è scaduto *38,* e  se il contatore SubClass_C2_contatore_Co8 non è  maggiore di  *54,* 151, Verifica che   *47,48,50,51,*  *34,*  il parametro SubClass_C2_parametro_P6 sia  diverso da  *56,* 4
    //   *104,* e  che   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* e  che  *,*  il contatore SubClass_C2_contatore_Co5 sia  uguale a  *53,* 1130
    //   *104,* e  che  *,*  la variabile SubClass_C2_variabile_V6 non sia  uguale a  False 
    //   *104,* e  che   il controllo ConsDef  sia  uguale a FALSE
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_AndLogicOP_4 = true;
    bool res_NotLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetParamSubcl6(my_id) == 2u));
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! res_NotLogicOP_6);
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_5);
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetInSubcl2(my_id) == rossogiallo3));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_7);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_AndLogicOP_4);
    res_OrLogicOP_3 = (res_OrLogicOP_3 || (L_P1__GetParamSubcl5(my_id) == rossogiallo3));
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    bool res_AndLogicOP_8 = true;
    bool res_AndLogicOP_9 = true;
    res_AndLogicOP_9 = (res_AndLogicOP_9 && (L_P1__GetInConsd1(my_id) == false));
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! Timer_Scaduto(L_P1__GetSubcl27(my_id)));
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_NotLogicOP_10);
    
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_AndLogicOP_9);
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (Counter_GetValore(L_P1__GetSubcl29(my_id)) > 151u));
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_11);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_8);
    
    if(res_OrLogicOP_2){
    bool res_AndLogicOP_12 = true;
    bool res_AndLogicOP_13 = true;
    bool res_AndLogicOP_14 = true;
    bool res_AndLogicOP_15 = true;
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (L_P1__GetParamSubcl6(my_id) == 4u));
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_NotLogicOP_16);
    res_AndLogicOP_15 = (res_AndLogicOP_15 && (L_P1__GetInConsd1(my_id) == false));
    
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_AndLogicOP_15);
    res_AndLogicOP_14 = (res_AndLogicOP_14 && (Counter_GetValore(L_P1__GetSubcl28(my_id)) == 1130u));
    
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_AndLogicOP_14);
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! (L_P1__GetSubcl24(my_id) == false));
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_NotLogicOP_17);
    
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_AndLogicOP_13);
    res_AndLogicOP_12 = (res_AndLogicOP_12 && (L_P1__GetInConsd1(my_id) == false));
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_AndLogicOP_12);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
     
    { commento: {63,}  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} e  se la variabile SubClass_C2_variabile_V1 è  minore di  commento: {55,} 4, Solo una delle seguenti { 
     commento: {63,} commento: {35,}  se il controllo SubClass_C2_controllo_C3 non è  uguale a RossoGialloGiallo commento: {35,} e  se il controllo SubClass_C2_controllo_C3 è  uguale a RossoGialloGiallo commento: {37,} e  se la variabile SubClass_C2_variabile_V1 è  uguale a  commento: {53,} 3 e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} o  se il controllo SubClass_C2_controllo_C3 non è  uguale a RossoGialloGiallo, Solo una delle seguenti { 
     commento: {62,} commento: {109,}  se il ripristino della variabile  SubClass_C2_restoreva_RV3 è  uguale a  False  commento: {36,} e  se il timer SubClass_C2_timer_T4 non è attivo commento: {34,} o  se il parametro SubClass_C2_parametro_P6 non è  diverso da  commento: {56,} 1 commento: {37,} o  se la variabile SubClass_C2_variabile_V6 è  diverso da  True  commento: {38,} e  se il contatore SubClass_C2_contatore_Co5 è  uguale a  commento: {53,} 125 commento: {34,} e  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  commento: {54,} 2, Almeno una delle seguenti { 
     commento: {36,}  se il timer SubClass_C2_timer_T4 è scaduto commento: {34,} e  se il parametro SubClass_C2_parametro_P2 è  uguale a  commento: {53,} 7, Verifica che   commento: {51,}  commento: {,}  il contatore SubClass_C2_contatore_Co8 non sia  minore di  commento: {55,} 11
    
    
     } Verifica che   commento: {47,48,50,51,}   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} o  che  commento: {,}  la variabile SubClass_C2_variabile_V6 non sia  uguale a  False 
     commento: {104,} e  che  commento: {34,}  il parametro SubClass_C2_parametro_P6 sia  maggiore di  commento: {54,} 2
     commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} o  che  commento: {,}  il contatore SubClass_C2_contatore_Co8 non sia  maggiore di  commento: {54,} 1
    
    
     } Verifica che   commento: {50,}  commento: {,}  la variabile SubClass_C2_variabile_V1 sia  minore di  commento: {55,} 8
    
    
     } Verifica che   commento: {48,49,}  commento: {,}  il timer SubClass_C2_timer_T4 sia scaduto
     commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} o  che  commento: {36,}  il timer SubClass_C2_timer_T4 non sia attivo
     commento: {104,} o  che  commento: {36,}  il timer SubClass_C2_timer_T4 sia scaduto
    
    
    }
*/
bool L_P1__Macro16(instance_id_t const my_id )
{
bool res_AndLogicOP_0 = true;
    
    //  *63,*  se il controllo ConsDef  è  uguale a FALSE  *37,* e  se la variabile SubClass_C2_variabile_V1 è  minore di  *55,* 4, Solo una delle seguenti { 
    //   *63,* *35,*  se il controllo SubClass_C2_controllo_C3 non è  uguale a RossoGialloGiallo *35,* e  se il controllo SubClass_C2_controllo_C3 è  uguale a RossoGialloGiallo *37,* e  se la variabile SubClass_C2_variabile_V1 è  uguale a  *53,* 3 e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  *35,* o  se il controllo SubClass_C2_controllo_C3 non è  uguale a RossoGialloGiallo, Solo una delle seguenti { 
    //   *62,* *109,*  se il ripristino della variabile  SubClass_C2_restoreva_RV3 è  uguale a  False  *36,* e  se il timer SubClass_C2_timer_T4 non è attivo *34,* o  se il parametro SubClass_C2_parametro_P6 non è  diverso da  *56,* 1 *37,* o  se la variabile SubClass_C2_variabile_V6 è  diverso da  True  *38,* e  se il contatore SubClass_C2_contatore_Co5 è  uguale a  *53,* 125 *34,* e  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  *54,* 2, Almeno una delle seguenti { 
    //   *36,*  se il timer SubClass_C2_timer_T4 è scaduto *34,* e  se il parametro SubClass_C2_parametro_P2 è  uguale a  *53,* 7, Verifica che   *51,*  *,*  il contatore SubClass_C2_contatore_Co8 non sia  minore di  *55,* 11
    //   } Verifica che   *47,48,50,51,*   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* e  che   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* o  che  *,*  la variabile SubClass_C2_variabile_V6 non sia  uguale a  False 
    //   *104,* e  che  *34,*  il parametro SubClass_C2_parametro_P6 sia  maggiore di  *54,* 2
    //   *104,* o  che   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* o  che  *,*  il contatore SubClass_C2_contatore_Co8 non sia  maggiore di  *54,* 1
    //   } Verifica che   *50,*  *,*  la variabile SubClass_C2_variabile_V1 sia  minore di  *55,* 8
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_AndLogicOP_2 = true;
    res_AndLogicOP_2 = (res_AndLogicOP_2 && (L_P1__GetInConsd1(my_id) == false));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && (L_P1__GetSubcl23(my_id) < 4u));
    
    if(res_AndLogicOP_2){
    bool res_XorLogicOP_3 = true;
    int xorIndex_res_XorLogicOP_3 = 0;
    bool res_ImpliesLogicOp_4 = true;
    bool res_OrLogicOP_5 = false;
    bool res_AndLogicOP_6 = true;
    bool res_AndLogicOP_7 = true;
    bool res_AndLogicOP_8 = true;
    bool res_AndLogicOP_9 = true;
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__GetInSubcl2(my_id) == rossogiallo3));
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_NotLogicOP_10);
    res_AndLogicOP_9 = (res_AndLogicOP_9 && (L_P1__GetInSubcl2(my_id) == rossogiallo3));
    
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_AndLogicOP_9);
    res_AndLogicOP_8 = (res_AndLogicOP_8 && (L_P1__GetSubcl23(my_id) == 3u));
    
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_AndLogicOP_8);
    res_AndLogicOP_7 = (res_AndLogicOP_7 && (L_P1__GetInConsd1(my_id) == false));
    
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_AndLogicOP_7);
    res_AndLogicOP_6 = (res_AndLogicOP_6 && (L_P1__GetInConsd1(my_id) == false));
    
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_AndLogicOP_6);
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (L_P1__GetInSubcl2(my_id) == rossogiallo3));
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_NotLogicOP_11);
    
    if(res_OrLogicOP_5){
    bool res_XorLogicOP_12 = true;
    int xorIndex_res_XorLogicOP_12 = 0;
    bool res_ImpliesLogicOp_13 = true;
    bool res_OrLogicOP_14 = false;
    bool res_OrLogicOP_15 = false;
    bool res_AndLogicOP_16 = true;
    res_AndLogicOP_16 = (res_AndLogicOP_16 && (L_P1__GetSubcl22(my_id) == false));
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! Timer_Attivo(L_P1__GetSubcl27(my_id)));
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_NotLogicOP_17);
    
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_AndLogicOP_16);
    bool res_NotLogicOP_18 = true;
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (L_P1__GetParamSubcl6(my_id) == 1u));
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! res_NotLogicOP_19);
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_NotLogicOP_18);
    
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_OrLogicOP_15);
    bool res_AndLogicOP_20 = true;
    bool res_AndLogicOP_21 = true;
    bool res_NotLogicOP_22 = true;
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! (L_P1__GetSubcl24(my_id) == true));
    res_AndLogicOP_21 = (res_AndLogicOP_21 && res_NotLogicOP_22);
    res_AndLogicOP_21 = (res_AndLogicOP_21 && (Counter_GetValore(L_P1__GetSubcl28(my_id)) == 125u));
    
    res_AndLogicOP_20 = (res_AndLogicOP_20 && res_AndLogicOP_21);
    bool res_NotLogicOP_23 = true;
    res_NotLogicOP_23 = (res_NotLogicOP_23 && ! (L_P1__GetParamSubcl6(my_id) > 2u));
    res_AndLogicOP_20 = (res_AndLogicOP_20 && res_NotLogicOP_23);
    
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_AndLogicOP_20);
    
    if(res_OrLogicOP_14){
    bool res_ImpliesLogicOp_24 = true;
    bool res_AndLogicOP_25 = true;
    res_AndLogicOP_25 = (res_AndLogicOP_25 && Timer_Scaduto(L_P1__GetSubcl27(my_id)));
    res_AndLogicOP_25 = (res_AndLogicOP_25 && (L_P1__GetParamSubcl4(my_id) == 7u));
    
    if(res_AndLogicOP_25){
    bool res_NotLogicOP_26 = true;
    res_NotLogicOP_26 = (res_NotLogicOP_26 && ! (Counter_GetValore(L_P1__GetSubcl29(my_id)) < 11u));
    res_ImpliesLogicOp_24 = (res_ImpliesLogicOp_24 && res_NotLogicOP_26);
    }
    res_ImpliesLogicOp_13 = (res_ImpliesLogicOp_13 && res_ImpliesLogicOp_24);
    }
    if(res_ImpliesLogicOp_13){
    xorIndex_res_XorLogicOP_12 = (xorIndex_res_XorLogicOP_12 + 1);
    }
    bool res_OrLogicOP_27 = false;
    bool res_OrLogicOP_28 = false;
    bool res_OrLogicOP_29 = false;
    bool res_AndLogicOP_30 = true;
    res_AndLogicOP_30 = (res_AndLogicOP_30 && (L_P1__GetInConsd1(my_id) == false));
    res_AndLogicOP_30 = (res_AndLogicOP_30 && (L_P1__GetInConsd1(my_id) == false));
    
    res_OrLogicOP_29 = (res_OrLogicOP_29 || res_AndLogicOP_30);
    bool res_AndLogicOP_31 = true;
    bool res_NotLogicOP_32 = true;
    res_NotLogicOP_32 = (res_NotLogicOP_32 && ! (L_P1__GetSubcl24(my_id) == false));
    res_AndLogicOP_31 = (res_AndLogicOP_31 && res_NotLogicOP_32);
    res_AndLogicOP_31 = (res_AndLogicOP_31 && (L_P1__GetParamSubcl6(my_id) > 2u));
    
    res_OrLogicOP_29 = (res_OrLogicOP_29 || res_AndLogicOP_31);
    
    res_OrLogicOP_28 = (res_OrLogicOP_28 || res_OrLogicOP_29);
    res_OrLogicOP_28 = (res_OrLogicOP_28 || (L_P1__GetInConsd1(my_id) == false));
    
    res_OrLogicOP_27 = (res_OrLogicOP_27 || res_OrLogicOP_28);
    bool res_NotLogicOP_33 = true;
    res_NotLogicOP_33 = (res_NotLogicOP_33 && ! (Counter_GetValore(L_P1__GetSubcl29(my_id)) > 1u));
    res_OrLogicOP_27 = (res_OrLogicOP_27 || res_NotLogicOP_33);
    
    if(res_OrLogicOP_27){
    xorIndex_res_XorLogicOP_12 = (xorIndex_res_XorLogicOP_12 + 1);
    }
    
    res_XorLogicOP_12 = (res_XorLogicOP_12 && (xorIndex_res_XorLogicOP_12 == 1));
    res_ImpliesLogicOp_4 = (res_ImpliesLogicOp_4 && res_XorLogicOP_12);
    }
    if(res_ImpliesLogicOp_4){
    xorIndex_res_XorLogicOP_3 = (xorIndex_res_XorLogicOP_3 + 1);
    }
    if((L_P1__GetSubcl23(my_id) < 8u)){
    xorIndex_res_XorLogicOP_3 = (xorIndex_res_XorLogicOP_3 + 1);
    }
    
    res_XorLogicOP_3 = (res_XorLogicOP_3 && (xorIndex_res_XorLogicOP_3 == 1));
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_XorLogicOP_3);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *48,49,*  *,*  il timer SubClass_C2_timer_T4 sia scaduto
    //   *104,* e  che   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* o  che  *36,*  il timer SubClass_C2_timer_T4 non sia attivo
    //   *104,* o  che  *36,*  il timer SubClass_C2_timer_T4 sia scaduto
    bool res_OrLogicOP_34 = false;
    bool res_OrLogicOP_35 = false;
    bool res_AndLogicOP_36 = true;
    res_AndLogicOP_36 = (res_AndLogicOP_36 && Timer_Scaduto(L_P1__GetSubcl27(my_id)));
    res_AndLogicOP_36 = (res_AndLogicOP_36 && (L_P1__GetInConsd1(my_id) == false));
    
    res_OrLogicOP_35 = (res_OrLogicOP_35 || res_AndLogicOP_36);
    bool res_NotLogicOP_37 = true;
    res_NotLogicOP_37 = (res_NotLogicOP_37 && ! Timer_Attivo(L_P1__GetSubcl27(my_id)));
    res_OrLogicOP_35 = (res_OrLogicOP_35 || res_NotLogicOP_37);
    
    res_OrLogicOP_34 = (res_OrLogicOP_34 || res_OrLogicOP_35);
    res_OrLogicOP_34 = (res_OrLogicOP_34 || Timer_Scaduto(L_P1__GetSubcl27(my_id)));
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_34);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
    
    { commento: {63,} commento: {35,}  se il controllo SubClass_C2_controllo_C3 è  uguale a RossoGialloGiallo e  se l'argomento argomento_ave6 non  è  uguale a c180 commento: {39,} , Solo una delle seguenti { 
     commento: {61,}  se la macro  SubClass_C2_macrova_M9 ( con argomento_a5   uguale a True ,argomento_a3   uguale a avvio ,argomento_a8   uguale a RossoGialloxVerdex  e argomento_a7   uguale a RossoGialloGiallo )  non  è  diverso da c180 commento: {40,} ,  commento: {45,}  se  MainClass_C1_contatore_Co2 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  commento: {105,} è  uguale a  commento: {53,} 1121, commento: {88,} quando  commento: {44,}    MainClass_C1_variabile_V7 del campo  MainClass_C1     è  uguale a  commento: {53,} 4 commento: {34,} o  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  commento: {54,} 1 commento: {34,} e  se il parametro SubClass_C2_parametro_P6 è  maggiore di  commento: {54,} 1 o  se l'argomento argomento_ave2 non  è  uguale a  True  commento: {39,} , Tutte le seguenti { 
     commento: {61,} commento: {34,}  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  commento: {54,} 5, Tutte le seguenti { 
     commento: {38,}  se il contatore SubClass_C2_contatore_Co8 non è  minore di  commento: {55,} 1330,  commento: {43,}  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L3 è disattivo, commento: {88,} quando  commento: {41,}   MainClass_C1_parametro_P8 del campo  MainClass_C1     commento: {105,} è  diverso da GialloxVerdex, Verifica che   commento: {47,52,}   l'argomento argomento_ave2 sia  diverso da  False  commento: {,} 
     commento: {104,} o  che  commento: {34,}  il parametro SubClass_C2_parametro_P2 non sia  uguale a  commento: {53,} 10
    
    
     } Verifica che   commento: {48,50,52,}  commento: {,}  il controllo SubClass_C2_controllo_C3 non sia  diverso da RossoGialloGiallo
     commento: {104,} e  che  commento: {,}  la variabile SubClass_C2_variabile_V1 sia  maggiore di  commento: {54,} 1
     commento: {104,} e  che   l'argomento argomento_ave4 sia  diverso da  True  commento: {,} 
     commento: {104,} e  che  commento: {35,}  il controllo SubClass_C2_controllo_C3 non sia  diverso da RossoGialloGiallo
    
    
     } Verifica che   commento: {48,50,51,52,}  commento: {,}  la variabile SubClass_C2_variabile_V1 sia  diverso da  commento: {56,} 6
     commento: {104,} o  che   l'argomento argomento_ave4 non  sia  diverso da  True  commento: {,} 
     commento: {104,} e  che   l'argomento argomento_ave2 sia  uguale a  True  commento: {39,} 
     commento: {104,} o  che  commento: {,}  il controllo SubClass_C2_controllo_C3 sia  uguale a RossoGialloGiallo
     commento: {104,} o  che  commento: {37,}  la variabile SubClass_C2_variabile_V1 non sia  diverso da  commento: {56,} 2
     commento: {104,} e  che  commento: {,}  il contatore SubClass_C2_contatore_Co5 non sia  maggiore di  commento: {54,} 1554
    
    
     } Verifica che   commento: {47,49,50,51,52,}  commento: {34,}  il parametro SubClass_C2_parametro_P2 non sia  minore di  commento: {55,} 8
     commento: {104,} o  che   l'argomento argomento_ave1 sia  diverso da  True  commento: {,} 
     commento: {104,} e  che  commento: {,}  la variabile SubClass_C2_variabile_V6 non sia  uguale a  True 
     commento: {104,} e  che  commento: {,}  il contatore SubClass_C2_contatore_Co5 sia  minore di  commento: {55,} 132
     commento: {104,} e  che  commento: {,}  il timer SubClass_C2_timer_T4 sia scaduto
    
    
    }
*/
bool L_P1__Macro17(instance_id_t const my_id , bool argom30, C2_Enumerat2 argom31, bool argom32, bool argom33, C2_Enumerat2 argom34, C2_Enumerat3 argom35, bool argom36)
{
bool res_AndLogicOP_0 = true;
    
    //  *63,* *35,*  se il controllo SubClass_C2_controllo_C3 è  uguale a RossoGialloGiallo e  se l'argomento argomento_ave6 non  è  uguale a c180 *39,* , Solo una delle seguenti { 
    //   *61,*  se la macro  SubClass_C2_macrova_M9 ( con argomento_a5   uguale a True ,argomento_a3   uguale a avvio ,argomento_a8   uguale a RossoGialloxVerdex  e argomento_a7   uguale a RossoGialloGiallo )  non  è  diverso da c180 *40,* ,  *45,*  se  MainClass_C1_contatore_Co2 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  *105,* è  uguale a  *53,* 1121, *88,* quando  *44,*    MainClass_C1_variabile_V7 del campo  MainClass_C1     è  uguale a  *53,* 4 *34,* o  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  *54,* 1 *34,* e  se il parametro SubClass_C2_parametro_P6 è  maggiore di  *54,* 1 o  se l'argomento argomento_ave2 non  è  uguale a  True  *39,* , Tutte le seguenti { 
    //   *61,* *34,*  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  *54,* 5, Tutte le seguenti { 
    //   *38,*  se il contatore SubClass_C2_contatore_Co8 non è  minore di  *55,* 1330,  *43,*  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L3 è disattivo, *88,* quando  *41,*   MainClass_C1_parametro_P8 del campo  MainClass_C1     *105,* è  diverso da GialloxVerdex, Verifica che   *47,52,*   l'argomento argomento_ave2 sia  diverso da  False  *,* 
    //   *104,* o  che  *34,*  il parametro SubClass_C2_parametro_P2 non sia  uguale a  *53,* 10
    //   } Verifica che   *48,50,52,*  *,*  il controllo SubClass_C2_controllo_C3 non sia  diverso da RossoGialloGiallo
    //   *104,* e  che  *,*  la variabile SubClass_C2_variabile_V1 sia  maggiore di  *54,* 1
    //   *104,* e  che   l'argomento argomento_ave4 sia  diverso da  True  *,* 
    //   *104,* e  che  *35,*  il controllo SubClass_C2_controllo_C3 non sia  diverso da RossoGialloGiallo
    //   } Verifica che   *48,50,51,52,*  *,*  la variabile SubClass_C2_variabile_V1 sia  diverso da  *56,* 6
    //   *104,* o  che   l'argomento argomento_ave4 non  sia  diverso da  True  *,* 
    //   *104,* e  che   l'argomento argomento_ave2 sia  uguale a  True  *39,* 
    //   *104,* o  che  *,*  il controllo SubClass_C2_controllo_C3 sia  uguale a RossoGialloGiallo
    //   *104,* o  che  *37,*  la variabile SubClass_C2_variabile_V1 non sia  diverso da  *56,* 2
    //   *104,* e  che  *,*  il contatore SubClass_C2_contatore_Co5 non sia  maggiore di  *54,* 1554
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_AndLogicOP_2 = true;
    res_AndLogicOP_2 = (res_AndLogicOP_2 && (L_P1__GetInSubcl2(my_id) == rossogiallo3));
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (argom35 == c180));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_3);
    
    if(res_AndLogicOP_2){
    bool res_XorLogicOP_4 = true;
    int xorIndex_res_XorLogicOP_4 = 0;
    bool res_ImpliesLogicOp_5 = true;
    bool res_OrLogicOP_6 = false;
    bool res_OrLogicOP_7 = false;
    bool res_AndLogicOP_8 = true;
    bool res_NotLogicOP_9 = true;
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__Macro13(my_id,avvio,true,rossogiallo3,rossogiallo2) == c180));
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! res_NotLogicOP_10);
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_9);
    bool res_ForAllPredicateNotEmpty_11 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl3Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl3(my_id,i);
    bool res_ImpliesLogicOp_12 = true;
    if((L_P1__GetMainc27(it.mainc40) == 4u)){
    res_ImpliesLogicOp_12 = (res_ImpliesLogicOp_12 && (Counter_GetValore(L_P1__GetMainc39(it.mainc40)) == 1121u));
    res_ForAllPredicateNotEmpty_11 = res_ImpliesLogicOp_12;
    if(!res_ForAllPredicateNotEmpty_11) {break;}
    }
    }
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_ForAllPredicateNotEmpty_11);
    
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_AndLogicOP_8);
    bool res_AndLogicOP_13 = true;
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1__GetParamSubcl6(my_id) > 1u));
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_NotLogicOP_14);
    res_AndLogicOP_13 = (res_AndLogicOP_13 && (L_P1__GetParamSubcl6(my_id) > 1u));
    
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_AndLogicOP_13);
    
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_OrLogicOP_7);
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (argom32 == true));
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_NotLogicOP_15);
    
    if(res_OrLogicOP_6){
    bool res_AndLogicOP_16 = true;
    bool res_ImpliesLogicOp_17 = true;
    bool res_NotLogicOP_18 = true;
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! (L_P1__GetParamSubcl6(my_id) > 5u));
    if(res_NotLogicOP_18){
    bool res_ImpliesLogicOp_19 = true;
    bool res_AndLogicOP_20 = true;
    bool res_NotLogicOP_21 = true;
    res_NotLogicOP_21 = (res_NotLogicOP_21 && ! (Counter_GetValore(L_P1__GetSubcl29(my_id)) < 1330u));
    res_AndLogicOP_20 = (res_AndLogicOP_20 && res_NotLogicOP_21);
    bool res_ForAllPredicate_22 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl3Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl3(my_id,i);
    bool res_ImpliesLogicOp_23 = true;
    bool res_NotLogicOP_24 = true;
    res_NotLogicOP_24 = (res_NotLogicOP_24 && ! (L_P1__GetParamMainc10(it.mainc40) == gialloxverd));
    if(res_NotLogicOP_24){
    res_ImpliesLogicOp_23 = (res_ImpliesLogicOp_23 && Timer_Disattivo(L_P1__GetMainc38(it.mainc40)));
    }
    res_ForAllPredicate_22 = res_ImpliesLogicOp_23;
    if(!res_ForAllPredicate_22) {break;}
    }
    res_AndLogicOP_20 = (res_AndLogicOP_20 && res_ForAllPredicate_22);
    
    if(res_AndLogicOP_20){
    bool res_OrLogicOP_25 = false;
    bool res_NotLogicOP_26 = true;
    res_NotLogicOP_26 = (res_NotLogicOP_26 && ! (argom32 == false));
    res_OrLogicOP_25 = (res_OrLogicOP_25 || res_NotLogicOP_26);
    bool res_NotLogicOP_27 = true;
    res_NotLogicOP_27 = (res_NotLogicOP_27 && ! (L_P1__GetParamSubcl4(my_id) == 10u));
    res_OrLogicOP_25 = (res_OrLogicOP_25 || res_NotLogicOP_27);
    
    res_ImpliesLogicOp_19 = (res_ImpliesLogicOp_19 && res_OrLogicOP_25);
    }
    res_ImpliesLogicOp_17 = (res_ImpliesLogicOp_17 && res_ImpliesLogicOp_19);
    }
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_ImpliesLogicOp_17);
    bool res_AndLogicOP_28 = true;
    bool res_AndLogicOP_29 = true;
    bool res_AndLogicOP_30 = true;
    bool res_NotLogicOP_31 = true;
    bool res_NotLogicOP_32 = true;
    res_NotLogicOP_32 = (res_NotLogicOP_32 && ! (L_P1__GetInSubcl2(my_id) == rossogiallo3));
    res_NotLogicOP_31 = (res_NotLogicOP_31 && ! res_NotLogicOP_32);
    res_AndLogicOP_30 = (res_AndLogicOP_30 && res_NotLogicOP_31);
    res_AndLogicOP_30 = (res_AndLogicOP_30 && (L_P1__GetSubcl23(my_id) > 1u));
    
    res_AndLogicOP_29 = (res_AndLogicOP_29 && res_AndLogicOP_30);
    bool res_NotLogicOP_33 = true;
    res_NotLogicOP_33 = (res_NotLogicOP_33 && ! (argom33 == true));
    res_AndLogicOP_29 = (res_AndLogicOP_29 && res_NotLogicOP_33);
    
    res_AndLogicOP_28 = (res_AndLogicOP_28 && res_AndLogicOP_29);
    bool res_NotLogicOP_34 = true;
    bool res_NotLogicOP_35 = true;
    res_NotLogicOP_35 = (res_NotLogicOP_35 && ! (L_P1__GetInSubcl2(my_id) == rossogiallo3));
    res_NotLogicOP_34 = (res_NotLogicOP_34 && ! res_NotLogicOP_35);
    res_AndLogicOP_28 = (res_AndLogicOP_28 && res_NotLogicOP_34);
    
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_AndLogicOP_28);
    
    res_ImpliesLogicOp_5 = (res_ImpliesLogicOp_5 && res_AndLogicOP_16);
    }
    if(res_ImpliesLogicOp_5){
    xorIndex_res_XorLogicOP_4 = (xorIndex_res_XorLogicOP_4 + 1);
    }
    bool res_OrLogicOP_36 = false;
    bool res_OrLogicOP_37 = false;
    bool res_OrLogicOP_38 = false;
    bool res_NotLogicOP_39 = true;
    res_NotLogicOP_39 = (res_NotLogicOP_39 && ! (L_P1__GetSubcl23(my_id) == 6u));
    res_OrLogicOP_38 = (res_OrLogicOP_38 || res_NotLogicOP_39);
    bool res_AndLogicOP_40 = true;
    bool res_NotLogicOP_41 = true;
    bool res_NotLogicOP_42 = true;
    res_NotLogicOP_42 = (res_NotLogicOP_42 && ! (argom33 == true));
    res_NotLogicOP_41 = (res_NotLogicOP_41 && ! res_NotLogicOP_42);
    res_AndLogicOP_40 = (res_AndLogicOP_40 && res_NotLogicOP_41);
    res_AndLogicOP_40 = (res_AndLogicOP_40 && (argom32 == true));
    
    res_OrLogicOP_38 = (res_OrLogicOP_38 || res_AndLogicOP_40);
    
    res_OrLogicOP_37 = (res_OrLogicOP_37 || res_OrLogicOP_38);
    res_OrLogicOP_37 = (res_OrLogicOP_37 || (L_P1__GetInSubcl2(my_id) == rossogiallo3));
    
    res_OrLogicOP_36 = (res_OrLogicOP_36 || res_OrLogicOP_37);
    bool res_AndLogicOP_43 = true;
    bool res_NotLogicOP_44 = true;
    bool res_NotLogicOP_45 = true;
    res_NotLogicOP_45 = (res_NotLogicOP_45 && ! (L_P1__GetSubcl23(my_id) == 2u));
    res_NotLogicOP_44 = (res_NotLogicOP_44 && ! res_NotLogicOP_45);
    res_AndLogicOP_43 = (res_AndLogicOP_43 && res_NotLogicOP_44);
    bool res_NotLogicOP_46 = true;
    res_NotLogicOP_46 = (res_NotLogicOP_46 && ! (Counter_GetValore(L_P1__GetSubcl28(my_id)) > 1554u));
    res_AndLogicOP_43 = (res_AndLogicOP_43 && res_NotLogicOP_46);
    
    res_OrLogicOP_36 = (res_OrLogicOP_36 || res_AndLogicOP_43);
    
    if(res_OrLogicOP_36){
    xorIndex_res_XorLogicOP_4 = (xorIndex_res_XorLogicOP_4 + 1);
    }
    
    res_XorLogicOP_4 = (res_XorLogicOP_4 && (xorIndex_res_XorLogicOP_4 == 1));
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_XorLogicOP_4);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *47,49,50,51,52,*  *34,*  il parametro SubClass_C2_parametro_P2 non sia  minore di  *55,* 8
    //   *104,* o  che   l'argomento argomento_ave1 sia  diverso da  True  *,* 
    //   *104,* e  che  *,*  la variabile SubClass_C2_variabile_V6 non sia  uguale a  True 
    //   *104,* e  che  *,*  il contatore SubClass_C2_contatore_Co5 sia  minore di  *55,* 132
    //   *104,* e  che  *,*  il timer SubClass_C2_timer_T4 sia scaduto
    bool res_OrLogicOP_47 = false;
    bool res_NotLogicOP_48 = true;
    res_NotLogicOP_48 = (res_NotLogicOP_48 && ! (L_P1__GetParamSubcl4(my_id) < 8u));
    res_OrLogicOP_47 = (res_OrLogicOP_47 || res_NotLogicOP_48);
    bool res_AndLogicOP_49 = true;
    bool res_AndLogicOP_50 = true;
    bool res_AndLogicOP_51 = true;
    bool res_NotLogicOP_52 = true;
    res_NotLogicOP_52 = (res_NotLogicOP_52 && ! (argom30 == true));
    res_AndLogicOP_51 = (res_AndLogicOP_51 && res_NotLogicOP_52);
    bool res_NotLogicOP_53 = true;
    res_NotLogicOP_53 = (res_NotLogicOP_53 && ! (L_P1__GetSubcl24(my_id) == true));
    res_AndLogicOP_51 = (res_AndLogicOP_51 && res_NotLogicOP_53);
    
    res_AndLogicOP_50 = (res_AndLogicOP_50 && res_AndLogicOP_51);
    res_AndLogicOP_50 = (res_AndLogicOP_50 && (Counter_GetValore(L_P1__GetSubcl28(my_id)) < 132u));
    
    res_AndLogicOP_49 = (res_AndLogicOP_49 && res_AndLogicOP_50);
    res_AndLogicOP_49 = (res_AndLogicOP_49 && Timer_Scaduto(L_P1__GetSubcl27(my_id)));
    
    res_OrLogicOP_47 = (res_OrLogicOP_47 || res_AndLogicOP_49);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_47);
    
    
    
    return res_AndLogicOP_0;
}


// Macro valorizzate

/*
    CNL corrispondente:
    
    { commento: {[}
     commento: {46,} assegna alla macro il valore c180 commento: {],}
    }
*/
C2_Enumerat3 L_P1__Macro13(instance_id_t const my_id , C2_Enumerat4 argom20, bool argom21, C2_Enumerat1 argom22, C2_Enumerat1 argom23)
{
return c180;
}



