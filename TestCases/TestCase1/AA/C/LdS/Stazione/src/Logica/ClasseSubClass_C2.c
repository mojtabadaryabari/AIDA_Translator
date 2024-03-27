// Codice del modello 'TestCase1', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#include "Logica/ClasseMainClass_C1.h"
#include "Logica/ClasseSubClass_C2.h"
#include "Logica/ClasseSubClass_C2_priv.h"
#include "config.h"
#include "scheduler.h"


// ********** Gestione comandi automatici **********

static size_t L_P1_C2_NumAutoCmds(instance_id_t const my_id)
{
    size_t n = 0u;
    if (L_P1__GetCAEvent5(my_id)) {
        ++n;
    }
    return n;
}


// ********** Gestione comandi manuali **********

static void L_P1_C2_InitCmdsResponse(instance_id_t const my_id)
{
    // for each manual command of L_P1_C2
    if (L_P1__GetInEvent4(my_id)) {
	    L_P1__SetOutEvent6(my_id, LDS_MANCMD_UNEXPECTED);
    } else {
        L_P1__SetOutEvent6(my_id, LDS_MANCMD_NOOP);
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
    
     commento: {37,}  se la variabile SubClass_C2_variabile_V9 è  diverso da  False , commento: {72,}Azzera il contatore SubClass_C2_contatore_Co4
    
     ,altrimenti  commento: {72,}Azzera il contatore SubClass_C2_contatore_Co4
    
    
    
    }
*/
static inline void L_P1__Effec3(instance_id_t const my_id)
{
    
    //  *37,*  se la variabile SubClass_C2_variabile_V9 è  diverso da  False , *72,*Azzera il contatore SubClass_C2_contatore_Co4
    //   ,altrimenti  *72,*Azzera il contatore SubClass_C2_contatore_Co4
    bool res_NotLogicOP_0 = true;
    res_NotLogicOP_0 = (res_NotLogicOP_0 && ! (L_P1__GetSubcl29(my_id) == false));
    if(res_NotLogicOP_0){
    
    Counter_Res(L_P1__GetSubcl45(my_id));
    }else{
    
    Counter_Res(L_P1__GetSubcl45(my_id));
    }
}



// ********** Definizione metodi **********

// Metodi standard

void L_P1_C2_Init(instance_id_t const my_id)
{
    // init variabili di stato
    L_P1__SetStato3(my_id, C2_St_Stato);
    L_P1__SetSubcl12(my_id, 0);
    L_P1__SetSubcl14(my_id, gialloverde);
    L_P1__SetSubcl16(my_id, false);
    L_P1__SetSubcl18(my_id, 0);
    L_P1__SetSubcl20(my_id, 0);
    L_P1__SetSubcl22(my_id, 0);
    L_P1__SetSubcl23(my_id, 0);
    L_P1__SetSubcl24(my_id, false);
    L_P1__SetSubcl25(my_id, false);
    L_P1__SetSubcl26(my_id, rossogiallo2);
    L_P1__SetSubcl27(my_id, false);
    L_P1__SetSubcl28(my_id, false);
    L_P1__SetSubcl29(my_id, false);
    // init controlli precedenti
    L_P1__SetSubcl11(my_id, c180x);
    // init Timer e Counter
    Timer_AggmInit(L_P1__GetSubcl30(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl30_ID);
    Timer_Init(L_P1__GetSubcl30(my_id), 3000);
    Timer_AggmInit(L_P1__GetSubcl31(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl31_ID);
    Timer_Init(L_P1__GetSubcl31(my_id), 3000);
    Timer_AggmInit(L_P1__GetSubcl32(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl32_ID);
    Timer_Init(L_P1__GetSubcl32(my_id), 44000);
    Timer_AggmInit(L_P1__GetSubcl33(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl33_ID);
    Timer_Init(L_P1__GetSubcl33(my_id), 44000);
    Timer_AggmInit(L_P1__GetSubcl34(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl34_ID);
    Timer_Init(L_P1__GetSubcl34(my_id), 453210000);
    Timer_AggmInit(L_P1__GetSubcl35(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl35_ID);
    Timer_Init(L_P1__GetSubcl35(my_id), 453210000);
    Timer_AggmInit(L_P1__GetSubcl36(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl36_ID);
    Timer_Init(L_P1__GetSubcl36(my_id), 2000);
    Timer_AggmInit(L_P1__GetSubcl37(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl37_ID);
    Timer_Init(L_P1__GetSubcl37(my_id), 2000);
    Timer_AggmInit(L_P1__GetSubcl38(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl38_ID);
    Timer_Init(L_P1__GetSubcl38(my_id), 545000);
    Timer_AggmInit(L_P1__GetSubcl39(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl39_ID);
    Timer_Init(L_P1__GetSubcl39(my_id), 545000);
    Timer_AggmInit(L_P1__GetSubcl40(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl40_ID);
    Timer_Init(L_P1__GetSubcl40(my_id), 2000);
    Timer_AggmInit(L_P1__GetSubcl41(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl41_ID);
    Timer_Init(L_P1__GetSubcl41(my_id), 5000);
    Timer_AggmInit(L_P1__GetSubcl42(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl42_ID);
    Timer_Init(L_P1__GetSubcl42(my_id), 2210000);
    Counter_AggmInit(L_P1__GetSubcl43(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl43_ID);
    Counter_Init(L_P1__GetSubcl43(my_id));
    Counter_AggmInit(L_P1__GetSubcl44(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl44_ID);
    Counter_Init(L_P1__GetSubcl44(my_id));
    Counter_AggmInit(L_P1__GetSubcl45(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl45_ID);
    Counter_Init(L_P1__GetSubcl45(my_id));
    Counter_AggmInit(L_P1__GetSubcl46(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl46_ID);
    Counter_Init(L_P1__GetSubcl46(my_id));
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
    L_P1__SetSubcl13(my_id, L_P1__GetSubcl12(my_id));
    L_P1__SetSubcl15(my_id, L_P1__GetSubcl14(my_id));
    L_P1__SetSubcl17(my_id, L_P1__GetSubcl16(my_id));
    L_P1__SetSubcl19(my_id, L_P1__GetSubcl18(my_id));
    L_P1__SetSubcl21(my_id, L_P1__GetSubcl20(my_id));
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
    Timer_Exec(L_P1__GetSubcl30(my_id));
    Timer_Exec(L_P1__GetSubcl31(my_id));
    Timer_Exec(L_P1__GetSubcl32(my_id));
    Timer_Exec(L_P1__GetSubcl33(my_id));
    Timer_Exec(L_P1__GetSubcl34(my_id));
    Timer_Exec(L_P1__GetSubcl35(my_id));
    Timer_Exec(L_P1__GetSubcl36(my_id));
    Timer_Exec(L_P1__GetSubcl37(my_id));
    Timer_Exec(L_P1__GetSubcl38(my_id));
    Timer_Exec(L_P1__GetSubcl39(my_id));
    Timer_Exec(L_P1__GetSubcl40(my_id));
    Timer_Exec(L_P1__GetSubcl41(my_id));
    Timer_Exec(L_P1__GetSubcl42(my_id));
}

void L_P1_C2_GSetSafe(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C2(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C2(proc_id);
    L_P1__SetOutSubcl(my_id, false);
    L_P1__SetOutSubcl1(my_id, c180);
    L_P1__SetOutSubcl2(my_id, true);
}

void L_P1_C2_GUpdatePrev(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C2(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C2(proc_id);
    L_P1__SetSubcl11(my_id, L_P1__GetInSubcl10(my_id));
    L_P1__SetSubcl13(my_id, L_P1__GetSubcl12(my_id));
    L_P1__SetSubcl15(my_id, L_P1__GetSubcl14(my_id));
    L_P1__SetSubcl17(my_id, L_P1__GetSubcl16(my_id));
    L_P1__SetSubcl19(my_id, L_P1__GetSubcl18(my_id));
    L_P1__SetSubcl21(my_id, L_P1__GetSubcl20(my_id));
}

// ********** Definizione macro **********

// Macro di effetto

/*
    CNL corrispondente:
    
    { commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L7 esiste e  commento: {105,} è  diverso da  commento: {56,}  state1  e  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE ,  Applica gli effetti
           della macro SubClass_C2_macroef_M4  commento: {73,}
    
     ,altrimenti   Applica gli effetti
           della macro SubClass_C2_macroef_M6   commento: {73,}
    
    
    
    }
*/
void L_P1__Macro10(instance_id_t const my_id )
{
//  *111,*  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L7 esiste e  *105,* è  diverso da  *56,*  state1  e  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE ,  Applica gli effetti
    //       della macro SubClass_C2_macroef_M4  *73,*
    // ,altrimenti   Applica gli effetti
    //       della macro SubClass_C2_macroef_M6
    bool res_OrLogicOP_0 = false;
    bool res_AndLogicOP_1 = true;
    bool res_ForAllPredicateNotEmpty_2 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl6Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl6(my_id,i);
    bool res_ImpliesLogicOp_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1_C1_GetState(it.mainc36) == C1_St_state));
    res_ImpliesLogicOp_3 = (res_ImpliesLogicOp_3 && res_NotLogicOP_4);
    res_ForAllPredicateNotEmpty_2 = res_ImpliesLogicOp_3;
    if(!res_ForAllPredicateNotEmpty_2) {break;}
    }
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_ForAllPredicateNotEmpty_2);
    res_AndLogicOP_1 = (res_AndLogicOP_1 && (L_P1__GetInConsd1(my_id) == false));
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_1);
    res_OrLogicOP_0 = (res_OrLogicOP_0 || (L_P1__GetInConsd1(my_id) == false));
    
    if(res_OrLogicOP_0){
    
    L_P1__Macro11(my_id);
    }else{
    
    L_P1__Macro12(my_id);
    }
}

/*
    CNL corrispondente:
    
    { commento: {42,}  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L7 esiste e  commento: {105,} è  diverso da GialloGiallo commento: {35,} e  se il controllo SubClass_C2_controllo_C7 è  diverso da  True  commento: {35,} o  se il controllo SubClass_C2_controllo_C7 è  diverso da  False  commento: {36,} e  se il timer SubClass_C2_timer_T9 è disattivo commento: {38,} o  se il contatore SubClass_C2_contatore_Co6 non è  diverso da  commento: {56,} 14, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V2 il valore RossoGiallox
    
       
     commento: {38,}  se il contatore SubClass_C2_contatore_Co6 è  uguale a  commento: {53,} 1253210 commento: {38,} e  se il contatore SubClass_C2_contatore_Co6 è  uguale a  commento: {53,} 13 commento: {38,} e  se il contatore SubClass_C2_contatore_Co6 non è  minore di  commento: {55,} 15 commento: {38,} o  se il contatore SubClass_C2_contatore_Co6 è  maggiore di  commento: {54,} 12 commento: {35,} e  se il controllo SubClass_C2_controllo_C7 è  uguale a  True , commento: {67,} Assegna alla variabile SubClass_C2_variabile_V9 il valore  True 
    
       
    
    }
*/
void L_P1__Macro11(instance_id_t const my_id )
{
//  *42,*  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L7 esiste e  *105,* è  diverso da GialloGiallo *35,* e  se il controllo SubClass_C2_controllo_C7 è  diverso da  True  *35,* o  se il controllo SubClass_C2_controllo_C7 è  diverso da  False  *36,* e  se il timer SubClass_C2_timer_T9 è disattivo *38,* o  se il contatore SubClass_C2_contatore_Co6 non è  diverso da  *56,* 14, *67,* Assegna alla variabile SubClass_C2_variabile_V2 il valore RossoGiallox
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_AndLogicOP_2 = true;
    bool res_ForAllPredicateNotEmpty_3 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl6Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl6(my_id,i);
    bool res_ImpliesLogicOp_4 = true;
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetInMainc4(it.mainc36) == giallogiall));
    res_ImpliesLogicOp_4 = (res_ImpliesLogicOp_4 && res_NotLogicOP_5);
    res_ForAllPredicateNotEmpty_3 = res_ImpliesLogicOp_4;
    if(!res_ForAllPredicateNotEmpty_3) {break;}
    }
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_ForAllPredicateNotEmpty_3);
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetInSubcl3(my_id) == true));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_6);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_2);
    bool res_AndLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetInSubcl3(my_id) == false));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_8);
    res_AndLogicOP_7 = (res_AndLogicOP_7 && Timer_Disattivo(L_P1__GetSubcl42(my_id)));
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_7);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_NotLogicOP_9 = true;
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (Counter_GetValore(L_P1__GetSubcl46(my_id)) == 14u));
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! res_NotLogicOP_10);
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_9);
    
    if(res_OrLogicOP_0){
    
    L_P1__SetSubcl26(my_id,rossogiallo3);
    }
    //  *38,*  se il contatore SubClass_C2_contatore_Co6 è  uguale a  *53,* 1253210 *38,* e  se il contatore SubClass_C2_contatore_Co6 è  uguale a  *53,* 13 *38,* e  se il contatore SubClass_C2_contatore_Co6 non è  minore di  *55,* 15 *38,* o  se il contatore SubClass_C2_contatore_Co6 è  maggiore di  *54,* 12 *35,* e  se il controllo SubClass_C2_controllo_C7 è  uguale a  True , *67,* Assegna alla variabile SubClass_C2_variabile_V9 il valore  True
    bool res_OrLogicOP_11 = false;
    bool res_AndLogicOP_12 = true;
    bool res_AndLogicOP_13 = true;
    res_AndLogicOP_13 = (res_AndLogicOP_13 && (Counter_GetValore(L_P1__GetSubcl46(my_id)) == 1253210u));
    res_AndLogicOP_13 = (res_AndLogicOP_13 && (Counter_GetValore(L_P1__GetSubcl46(my_id)) == 13u));
    
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_AndLogicOP_13);
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (Counter_GetValore(L_P1__GetSubcl46(my_id)) < 15u));
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_NotLogicOP_14);
    
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_AndLogicOP_12);
    bool res_AndLogicOP_15 = true;
    res_AndLogicOP_15 = (res_AndLogicOP_15 && (Counter_GetValore(L_P1__GetSubcl46(my_id)) > 12u));
    res_AndLogicOP_15 = (res_AndLogicOP_15 && (L_P1__GetInSubcl3(my_id) == true));
    
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_AndLogicOP_15);
    
    if(res_OrLogicOP_11){
    
    L_P1__SetSubcl29(my_id,true);
    }
}

/*
    CNL corrispondente:
     
    { commento: {34,}  se lo stato  non è  uguale a  commento: {53,}  state1  commento: {106,}, commento: {70,}Incrementa il contatore SubClass_C2_contatore_Co6
    
       
    
    }
*/
void L_P1__Macro12(instance_id_t const my_id )
{
//  *34,*  se lo stato  non è  uguale a  *53,*  state1  *106,*, *70,*Incrementa il contatore SubClass_C2_contatore_Co6
    bool res_NotLogicOP_0 = true;
    res_NotLogicOP_0 = (res_NotLogicOP_0 && ! (L_P1_C2_GetState(my_id) == C2_St_state));
    if(res_NotLogicOP_0){
    
    Counter_Incr(L_P1__GetSubcl46(my_id));
    }
}

/*
    CNL corrispondente:
    
    { commento: {43,}  se MainClass_C1_timer_T7 del campo  MainClass_C1 di SubClass_C2_lista_L7 esiste e  commento: {105,} è attivo commento: {36,} o  se il timer SubClass_C2_timer_T9 è attivo e  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} o  se il parametro SubClass_C2_parametro_P5 è  maggiore di  commento: {54,} 1 e  se il controllo ConsDef  è  uguale a FALSE , commento: {68,}Attiva il timer SubClass_C2_timer_T9
    
       
     commento: {36,}  se il timer SubClass_C2_timer_T4 non è scaduto,  commento: {43,}  se MainClass_C1_timer_T5 del campo  MainClass_C1 di SubClass_C2_lista_L5 è attivo, commento: {88,} quando  commento: {44,}    MainClass_C1_variabile_V10 del campo  MainClass_C1     è  diverso da  commento: {56,} 10 commento: {36,} o  se il timer SubClass_C2_timer_T4 non è disattivo commento: {34,} o  se il parametro SubClass_C2_parametro_P7 non è  minore di  commento: {55,} 1 commento: {34,} o  se il parametro SubClass_C2_parametro_P5 è  minore di  commento: {55,} 7 e  se il controllo ConsDef  è  uguale a FALSE , commento: {67,} Assegna alla variabile SubClass_C2_variabile_V9 il valore  True 
    
       
     commento: {109,}  se il ripristino della variabile  SubClass_C2_restoreva_RV2 è  uguale a  False  commento: {35,} e  se il controllo SubClass_C2_controllo_C7 è  diverso da  True  commento: {35,} e  se il controllo SubClass_C2_controllo_C7 è  diverso da  False  commento: {36,} o  se il timer SubClass_C2_timer_T4 è attivo,  Applica gli effetti
           della macro SubClass_C2_macroef_M9  commento: {73,}
    
       
     commento: {35,}  se il controllo SubClass_C2_controllo_C7 è  uguale a  True  commento: {38,} o  se il contatore SubClass_C2_contatore_Co4 è  diverso da  commento: {56,} 11 commento: {35,} e  se il controllo SubClass_C2_controllo_C7 è  diverso da  False  e  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} o  se la variabile SubClass_C2_variabile_V7 è  diverso da  False  commento: {37,} e  se la variabile SubClass_C2_variabile_V9 non è  diverso da  False , commento: {69,}Disattiva il timer SubClass_C2_timer_T9
    
     ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V9 il valore  False 
    
    
    
    }
*/
void L_P1__Macro13(instance_id_t const my_id )
{
//  *43,*  se MainClass_C1_timer_T7 del campo  MainClass_C1 di SubClass_C2_lista_L7 esiste e  *105,* è attivo *36,* o  se il timer SubClass_C2_timer_T9 è attivo e  se il controllo ConsDef  è  uguale a FALSE  *34,* o  se il parametro SubClass_C2_parametro_P5 è  maggiore di  *54,* 1 e  se il controllo ConsDef  è  uguale a FALSE , *68,*Attiva il timer SubClass_C2_timer_T9
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_ForAllPredicateNotEmpty_2 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl6Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl6(my_id,i);
    bool res_ImpliesLogicOp_3 = true;
    res_ImpliesLogicOp_3 = (res_ImpliesLogicOp_3 && Timer_Attivo(L_P1__GetMainc30(it.mainc36)));
    res_ForAllPredicateNotEmpty_2 = res_ImpliesLogicOp_3;
    if(!res_ForAllPredicateNotEmpty_2) {break;}
    }
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_ForAllPredicateNotEmpty_2);
    bool res_AndLogicOP_4 = true;
    res_AndLogicOP_4 = (res_AndLogicOP_4 && Timer_Attivo(L_P1__GetSubcl42(my_id)));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && (L_P1__GetInConsd1(my_id) == false));
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_4);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_AndLogicOP_5 = true;
    res_AndLogicOP_5 = (res_AndLogicOP_5 && (L_P1__GetParamSubcl8(my_id) > 1u));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && (L_P1__GetInConsd1(my_id) == false));
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_5);
    
    if(res_OrLogicOP_0){
    
    Timer_Attiva(L_P1__GetSubcl42(my_id));
    }
    //  *36,*  se il timer SubClass_C2_timer_T4 non è scaduto,  *43,*  se MainClass_C1_timer_T5 del campo  MainClass_C1 di SubClass_C2_lista_L5 è attivo, *88,* quando  *44,*    MainClass_C1_variabile_V10 del campo  MainClass_C1     è  diverso da  *56,* 10 *36,* o  se il timer SubClass_C2_timer_T4 non è disattivo *34,* o  se il parametro SubClass_C2_parametro_P7 non è  minore di  *55,* 1 *34,* o  se il parametro SubClass_C2_parametro_P5 è  minore di  *55,* 7 e  se il controllo ConsDef  è  uguale a FALSE , *67,* Assegna alla variabile SubClass_C2_variabile_V9 il valore  True
    bool res_OrLogicOP_6 = false;
    bool res_OrLogicOP_7 = false;
    bool res_OrLogicOP_8 = false;
    bool res_AndLogicOP_9 = true;
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! Timer_Scaduto(L_P1__GetSubcl41(my_id)));
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_NotLogicOP_10);
    bool res_ForAllPredicate_11 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl5Length(my_id); ++i)
    {
    L_P1__Recor1 it = L_P1__GetRecSubcl5(my_id,i);
    bool res_ImpliesLogicOp_12 = true;
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (L_P1__GetMainc26(it.mainc37) == 10u));
    if(res_NotLogicOP_13){
    res_ImpliesLogicOp_12 = (res_ImpliesLogicOp_12 && Timer_Attivo(L_P1__GetMainc29(it.mainc37)));
    }
    res_ForAllPredicate_11 = res_ImpliesLogicOp_12;
    if(!res_ForAllPredicate_11) {break;}
    }
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_ForAllPredicate_11);
    
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_AndLogicOP_9);
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! Timer_Disattivo(L_P1__GetSubcl41(my_id)));
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_NotLogicOP_14);
    
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_OrLogicOP_8);
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (L_P1__GetParamSubcl9(my_id) < 1u));
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_NotLogicOP_15);
    
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_OrLogicOP_7);
    bool res_AndLogicOP_16 = true;
    res_AndLogicOP_16 = (res_AndLogicOP_16 && (L_P1__GetParamSubcl8(my_id) < 7u));
    res_AndLogicOP_16 = (res_AndLogicOP_16 && (L_P1__GetInConsd1(my_id) == false));
    
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_AndLogicOP_16);
    
    if(res_OrLogicOP_6){
    
    L_P1__SetSubcl29(my_id,true);
    }
    //  *109,*  se il ripristino della variabile  SubClass_C2_restoreva_RV2 è  uguale a  False  *35,* e  se il controllo SubClass_C2_controllo_C7 è  diverso da  True  *35,* e  se il controllo SubClass_C2_controllo_C7 è  diverso da  False  *36,* o  se il timer SubClass_C2_timer_T4 è attivo,  Applica gli effetti
    //       della macro SubClass_C2_macroef_M9
    bool res_OrLogicOP_17 = false;
    bool res_AndLogicOP_18 = true;
    bool res_AndLogicOP_19 = true;
    res_AndLogicOP_19 = (res_AndLogicOP_19 && (L_P1__GetSubcl25(my_id) == false));
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! (L_P1__GetInSubcl3(my_id) == true));
    res_AndLogicOP_19 = (res_AndLogicOP_19 && res_NotLogicOP_20);
    
    res_AndLogicOP_18 = (res_AndLogicOP_18 && res_AndLogicOP_19);
    bool res_NotLogicOP_21 = true;
    res_NotLogicOP_21 = (res_NotLogicOP_21 && ! (L_P1__GetInSubcl3(my_id) == false));
    res_AndLogicOP_18 = (res_AndLogicOP_18 && res_NotLogicOP_21);
    
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_AndLogicOP_18);
    res_OrLogicOP_17 = (res_OrLogicOP_17 || Timer_Attivo(L_P1__GetSubcl41(my_id)));
    
    if(res_OrLogicOP_17){
    
    L_P1__Macro14(my_id);
    }
    //  *73,*
    //   
    // *35,*  se il controllo SubClass_C2_controllo_C7 è  uguale a  True  *38,* o  se il contatore SubClass_C2_contatore_Co4 è  diverso da  *56,* 11 *35,* e  se il controllo SubClass_C2_controllo_C7 è  diverso da  False  e  se il controllo ConsDef  è  uguale a FALSE  *37,* o  se la variabile SubClass_C2_variabile_V7 è  diverso da  False  *37,* e  se la variabile SubClass_C2_variabile_V9 non è  diverso da  False , *69,*Disattiva il timer SubClass_C2_timer_T9
    // ,altrimenti  *67,* Assegna alla variabile SubClass_C2_variabile_V9 il valore  False
    bool res_OrLogicOP_22 = false;
    bool res_OrLogicOP_23 = false;
    res_OrLogicOP_23 = (res_OrLogicOP_23 || (L_P1__GetInSubcl3(my_id) == true));
    bool res_AndLogicOP_24 = true;
    bool res_AndLogicOP_25 = true;
    bool res_NotLogicOP_26 = true;
    res_NotLogicOP_26 = (res_NotLogicOP_26 && ! (Counter_GetValore(L_P1__GetSubcl45(my_id)) == 11u));
    res_AndLogicOP_25 = (res_AndLogicOP_25 && res_NotLogicOP_26);
    bool res_NotLogicOP_27 = true;
    res_NotLogicOP_27 = (res_NotLogicOP_27 && ! (L_P1__GetInSubcl3(my_id) == false));
    res_AndLogicOP_25 = (res_AndLogicOP_25 && res_NotLogicOP_27);
    
    res_AndLogicOP_24 = (res_AndLogicOP_24 && res_AndLogicOP_25);
    res_AndLogicOP_24 = (res_AndLogicOP_24 && (L_P1__GetInConsd1(my_id) == false));
    
    res_OrLogicOP_23 = (res_OrLogicOP_23 || res_AndLogicOP_24);
    
    res_OrLogicOP_22 = (res_OrLogicOP_22 || res_OrLogicOP_23);
    bool res_AndLogicOP_28 = true;
    bool res_NotLogicOP_29 = true;
    res_NotLogicOP_29 = (res_NotLogicOP_29 && ! (L_P1__GetSubcl28(my_id) == false));
    res_AndLogicOP_28 = (res_AndLogicOP_28 && res_NotLogicOP_29);
    bool res_NotLogicOP_30 = true;
    bool res_NotLogicOP_31 = true;
    res_NotLogicOP_31 = (res_NotLogicOP_31 && ! (L_P1__GetSubcl29(my_id) == false));
    res_NotLogicOP_30 = (res_NotLogicOP_30 && ! res_NotLogicOP_31);
    res_AndLogicOP_28 = (res_AndLogicOP_28 && res_NotLogicOP_30);
    
    res_OrLogicOP_22 = (res_OrLogicOP_22 || res_AndLogicOP_28);
    
    if(res_OrLogicOP_22){
    
    Timer_Disattiva(L_P1__GetSubcl42(my_id));
    }else{
    
    L_P1__SetSubcl29(my_id,false);
    }
}

/*
    CNL corrispondente:
    
    { commento: {36,}  se il timer SubClass_C2_timer_T9 è scaduto commento: {38,} e  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  commento: {56,} 144 commento: {35,} e  se il controllo SubClass_C2_controllo_C7 è  uguale a  True  e  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} e  se la variabile SubClass_C2_variabile_V9 è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE , commento: {66,} Assegna al comando SubClass_C2_comando_C2 il valore c180
    
       
     commento: {42,}  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L7 esiste e  commento: {105,} è  uguale a GialloGiallo commento: {37,} o  se la variabile SubClass_C2_variabile_V9 è  uguale a  False  commento: {35,} e  se il controllo SubClass_C2_controllo_C7 non è  uguale a  False  commento: {34,} o  se il parametro SubClass_C2_parametro_P5 non è  uguale a  commento: {53,} 9 commento: {35,} o  se il controllo SubClass_C2_controllo_C7 è  uguale a  True  commento: {35,} o  se il controllo SubClass_C2_controllo_C7 non è  diverso da  False , commento: {70,}Incrementa il contatore SubClass_C2_contatore_Co6
    
     ,altrimenti  commento: {68,}Attiva il timer SubClass_C2_timer_T10
    
    
     commento: {110,}  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è attivo commento: {34,} o  se il parametro SubClass_C2_parametro_P7 è  uguale a  commento: {53,} 10 commento: {36,} o  se il timer SubClass_C2_timer_T9 è attivo, commento: {69,}Disattiva il timer SubClass_C2_timer_T9
    
     ,altrimenti  commento: {69,}Disattiva il timer SubClass_C2_timer_T10
    
    
     commento: {41,}  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L8 è  diverso da  commento: {56,} 4 commento: {36,} o  se il timer SubClass_C2_timer_T9 è disattivo commento: {35,} o  se il controllo SubClass_C2_controllo_C7 è  uguale a  True  commento: {36,} o  se il timer SubClass_C2_timer_T9 non è attivo commento: {36,} o  se il timer SubClass_C2_timer_T4 non è attivo, commento: {66,} Assegna al comando SubClass_C2_comando_C2 il valore c180
    
       
    
    }
*/
void L_P1__Macro14(instance_id_t const my_id )
{
//  *36,*  se il timer SubClass_C2_timer_T9 è scaduto *38,* e  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  *56,* 144 *35,* e  se il controllo SubClass_C2_controllo_C7 è  uguale a  True  e  se il controllo ConsDef  è  uguale a FALSE  *37,* e  se la variabile SubClass_C2_variabile_V9 è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE , *66,* Assegna al comando SubClass_C2_comando_C2 il valore c180
    bool res_AndLogicOP_0 = true;
    bool res_AndLogicOP_1 = true;
    bool res_AndLogicOP_2 = true;
    bool res_AndLogicOP_3 = true;
    bool res_AndLogicOP_4 = true;
    res_AndLogicOP_4 = (res_AndLogicOP_4 && Timer_Scaduto(L_P1__GetSubcl42(my_id)));
    bool res_NotLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (Counter_GetValore(L_P1__GetSubcl44(my_id)) == 144u));
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! res_NotLogicOP_6);
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_5);
    
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_AndLogicOP_4);
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (L_P1__GetInSubcl3(my_id) == true));
    
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_AndLogicOP_3);
    res_AndLogicOP_2 = (res_AndLogicOP_2 && (L_P1__GetInConsd1(my_id) == false));
    
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_AndLogicOP_2);
    res_AndLogicOP_1 = (res_AndLogicOP_1 && (L_P1__GetSubcl29(my_id) == false));
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_AndLogicOP_1);
    res_AndLogicOP_0 = (res_AndLogicOP_0 && (L_P1__GetInConsd1(my_id) == false));
    
    if(res_AndLogicOP_0){
    
    L_P1__SetOutSubcl1(my_id,c180);
    }
    //  *42,*  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L7 esiste e  *105,* è  uguale a GialloGiallo *37,* o  se la variabile SubClass_C2_variabile_V9 è  uguale a  False  *35,* e  se il controllo SubClass_C2_controllo_C7 non è  uguale a  False  *34,* o  se il parametro SubClass_C2_parametro_P5 non è  uguale a  *53,* 9 *35,* o  se il controllo SubClass_C2_controllo_C7 è  uguale a  True  *35,* o  se il controllo SubClass_C2_controllo_C7 non è  diverso da  False , *70,*Incrementa il contatore SubClass_C2_contatore_Co6
    // ,altrimenti  *68,*Attiva il timer SubClass_C2_timer_T10
    bool res_OrLogicOP_7 = false;
    bool res_OrLogicOP_8 = false;
    bool res_OrLogicOP_9 = false;
    bool res_OrLogicOP_10 = false;
    bool res_ForAllPredicateNotEmpty_11 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl6Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl6(my_id,i);
    bool res_ImpliesLogicOp_12 = true;
    res_ImpliesLogicOp_12 = (res_ImpliesLogicOp_12 && (L_P1__GetInMainc4(it.mainc36) == giallogiall));
    res_ForAllPredicateNotEmpty_11 = res_ImpliesLogicOp_12;
    if(!res_ForAllPredicateNotEmpty_11) {break;}
    }
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_ForAllPredicateNotEmpty_11);
    bool res_AndLogicOP_13 = true;
    res_AndLogicOP_13 = (res_AndLogicOP_13 && (L_P1__GetSubcl29(my_id) == false));
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1__GetInSubcl3(my_id) == false));
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_NotLogicOP_14);
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_AndLogicOP_13);
    
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_OrLogicOP_10);
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (L_P1__GetParamSubcl8(my_id) == 9u));
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_NotLogicOP_15);
    
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_OrLogicOP_9);
    res_OrLogicOP_8 = (res_OrLogicOP_8 || (L_P1__GetInSubcl3(my_id) == true));
    
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_OrLogicOP_8);
    bool res_NotLogicOP_16 = true;
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! (L_P1__GetInSubcl3(my_id) == false));
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! res_NotLogicOP_17);
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_NotLogicOP_16);
    
    if(res_OrLogicOP_7){
    
    Counter_Incr(L_P1__GetSubcl46(my_id));
    }else{
    
    Timer_Attiva(L_P1__GetSubcl40(my_id));
    }
    //  *110,*  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è attivo *34,* o  se il parametro SubClass_C2_parametro_P7 è  uguale a  *53,* 10 *36,* o  se il timer SubClass_C2_timer_T9 è attivo, *69,*Disattiva il timer SubClass_C2_timer_T9
    // ,altrimenti  *69,*Disattiva il timer SubClass_C2_timer_T10
    bool res_OrLogicOP_18 = false;
    bool res_OrLogicOP_19 = false;
    res_OrLogicOP_19 = (res_OrLogicOP_19 || Timer_Attivo(L_P1__GetSubcl31(my_id)));
    res_OrLogicOP_19 = (res_OrLogicOP_19 || (L_P1__GetParamSubcl9(my_id) == 10u));
    
    res_OrLogicOP_18 = (res_OrLogicOP_18 || res_OrLogicOP_19);
    res_OrLogicOP_18 = (res_OrLogicOP_18 || Timer_Attivo(L_P1__GetSubcl42(my_id)));
    
    if(res_OrLogicOP_18){
    
    Timer_Disattiva(L_P1__GetSubcl42(my_id));
    }else{
    
    Timer_Disattiva(L_P1__GetSubcl40(my_id));
    }
    //  *41,*  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L8 è  diverso da  *56,* 4 *36,* o  se il timer SubClass_C2_timer_T9 è disattivo *35,* o  se il controllo SubClass_C2_controllo_C7 è  uguale a  True  *36,* o  se il timer SubClass_C2_timer_T9 non è attivo *36,* o  se il timer SubClass_C2_timer_T4 non è attivo, *66,* Assegna al comando SubClass_C2_comando_C2 il valore c180
    bool res_OrLogicOP_20 = false;
    bool res_OrLogicOP_21 = false;
    bool res_OrLogicOP_22 = false;
    bool res_OrLogicOP_23 = false;
    bool res_ForAllPredicate_24 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl7Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl7(my_id,i);
    bool res_ImpliesLogicOp_25 = true;
    bool res_NotLogicOP_26 = true;
    res_NotLogicOP_26 = (res_NotLogicOP_26 && ! (L_P1__GetParamMainc6(it.mainc36) == 4u));
    res_ImpliesLogicOp_25 = (res_ImpliesLogicOp_25 && res_NotLogicOP_26);
    res_ForAllPredicate_24 = res_ImpliesLogicOp_25;
    if(!res_ForAllPredicate_24) {break;}
    }
    res_OrLogicOP_23 = (res_OrLogicOP_23 || res_ForAllPredicate_24);
    res_OrLogicOP_23 = (res_OrLogicOP_23 || Timer_Disattivo(L_P1__GetSubcl42(my_id)));
    
    res_OrLogicOP_22 = (res_OrLogicOP_22 || res_OrLogicOP_23);
    res_OrLogicOP_22 = (res_OrLogicOP_22 || (L_P1__GetInSubcl3(my_id) == true));
    
    res_OrLogicOP_21 = (res_OrLogicOP_21 || res_OrLogicOP_22);
    bool res_NotLogicOP_27 = true;
    res_NotLogicOP_27 = (res_NotLogicOP_27 && ! Timer_Attivo(L_P1__GetSubcl42(my_id)));
    res_OrLogicOP_21 = (res_OrLogicOP_21 || res_NotLogicOP_27);
    
    res_OrLogicOP_20 = (res_OrLogicOP_20 || res_OrLogicOP_21);
    bool res_NotLogicOP_28 = true;
    res_NotLogicOP_28 = (res_NotLogicOP_28 && ! Timer_Attivo(L_P1__GetSubcl41(my_id)));
    res_OrLogicOP_20 = (res_OrLogicOP_20 || res_NotLogicOP_28);
    
    if(res_OrLogicOP_20){
    
    L_P1__SetOutSubcl1(my_id,c180);
    }
}


// Macro di verifica

/*
    CNL corrispondente:
     
    { commento: {44,}  se  MainClass_C1_variabile_V10 del campo  MainClass_C1 di SubClass_C2_lista_L7 è  uguale a  commento: {53,} 8 commento: {37,} e  se la variabile SubClass_C2_variabile_V9 è  uguale a  True , Verifica che   commento: {48,51,}  commento: {,}  il contatore SubClass_C2_contatore_Co6 sia  minore di  commento: {55,} 13
     commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} e  che  commento: {38,}  il contatore SubClass_C2_contatore_Co6 non sia  minore di  commento: {55,} 11
     commento: {104,} e  che  commento: {38,}  il contatore SubClass_C2_contatore_Co10 non sia  maggiore di  commento: {54,} 154
    
    
    }
*/
bool L_P1__Macro16(instance_id_t const my_id )
{
bool res_AndLogicOP_0 = true;
    
    //  *44,*  se  MainClass_C1_variabile_V10 del campo  MainClass_C1 di SubClass_C2_lista_L7 è  uguale a  *53,* 8 *37,* e  se la variabile SubClass_C2_variabile_V9 è  uguale a  True , Verifica che   *48,51,*  *,*  il contatore SubClass_C2_contatore_Co6 sia  minore di  *55,* 13
    //   *104,* e  che   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* e  che  *38,*  il contatore SubClass_C2_contatore_Co6 non sia  minore di  *55,* 11
    //   *104,* e  che  *38,*  il contatore SubClass_C2_contatore_Co10 non sia  maggiore di  *54,* 154
    bool res_ImpliesLogicOp_1 = true;
    bool res_AndLogicOP_2 = true;
    bool res_ForAllPredicate_3 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl6Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl6(my_id,i);
    bool res_ImpliesLogicOp_4 = true;
    res_ImpliesLogicOp_4 = (res_ImpliesLogicOp_4 && (L_P1__GetMainc26(it.mainc36) == 8u));
    res_ForAllPredicate_3 = res_ImpliesLogicOp_4;
    if(!res_ForAllPredicate_3) {break;}
    }
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_ForAllPredicate_3);
    res_AndLogicOP_2 = (res_AndLogicOP_2 && (L_P1__GetSubcl29(my_id) == true));
    
    if(res_AndLogicOP_2){
    bool res_AndLogicOP_5 = true;
    bool res_AndLogicOP_6 = true;
    bool res_AndLogicOP_7 = true;
    res_AndLogicOP_7 = (res_AndLogicOP_7 && (Counter_GetValore(L_P1__GetSubcl46(my_id)) < 13u));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && (L_P1__GetInConsd1(my_id) == false));
    
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_AndLogicOP_7);
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (Counter_GetValore(L_P1__GetSubcl46(my_id)) < 11u));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_8);
    
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_AndLogicOP_6);
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (Counter_GetValore(L_P1__GetSubcl44(my_id)) > 154u));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_9);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_AndLogicOP_5);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    
    
    return res_AndLogicOP_0;
}


// Macro valorizzate

/*
    CNL corrispondente:
    
    { commento: {[} commento: {37,}  se la variabile SubClass_C2_variabile_V9 è  uguale a  True ,  commento: {41,}  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L5 esiste e  commento: {105,} è  maggiore di  commento: {54,} 6, commento: {88,} quando  commento: {43,}   MainClass_C1_timer_T5 del campo  MainClass_C1     commento: {105,} è disattivo commento: {38,} o  se il contatore SubClass_C2_contatore_Co4 è  maggiore di  commento: {54,} 12,  commento: {45,}  se  MainClass_C1_contatore_Co10 del campo  MainClass_C1 di SubClass_C2_lista_L5 esiste e  commento: {105,} è  minore di  commento: {55,} 12453, commento: {88,} quando  commento: {44,}    MainClass_C1_variabile_V10 del campo  MainClass_C1     è  maggiore di  commento: {54,} 1 commento: {36,} e  se il timer SubClass_C2_timer_T4 non è disattivo,  commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L5 esiste e  commento: {105,} è  diverso da  commento: {56,}  state1 , commento: {88,} quando  commento: {43,}   MainClass_C1_timer_T5 del campo  MainClass_C1     commento: {105,} è disattivo commento: {45,} e  se  MainClass_C1_contatore_Co3 del campo  MainClass_C1 di SubClass_C2_lista_L7 è  uguale a  commento: {53,} 14210 commento: {42,} o  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L5 è  diverso da GialloGiallo , assegna alla macro il valore c180
    
     commento: {46,} assegna alla macro il valore c180 commento: {],}
    }
*/
C2_Enumerat4 L_P1__Macro15(instance_id_t const my_id , C2_Enumerat3 argom20, C2_Enumerat2 argom21, C2_Enumerat3 argom22, C2_Enumerat3 argom23, C2_Enumerat3 argom24)
{
C2_Enumerat4 res_macro_val;
    
    //  *[* *37,*  se la variabile SubClass_C2_variabile_V9 è  uguale a  True ,  *41,*  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L5 esiste e  *105,* è  maggiore di  *54,* 6, *88,* quando  *43,*   MainClass_C1_timer_T5 del campo  MainClass_C1     *105,* è disattivo *38,* o  se il contatore SubClass_C2_contatore_Co4 è  maggiore di  *54,* 12,  *45,*  se  MainClass_C1_contatore_Co10 del campo  MainClass_C1 di SubClass_C2_lista_L5 esiste e  *105,* è  minore di  *55,* 12453, *88,* quando  *44,*    MainClass_C1_variabile_V10 del campo  MainClass_C1     è  maggiore di  *54,* 1 *36,* e  se il timer SubClass_C2_timer_T4 non è disattivo,  *111,*  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L5 esiste e  *105,* è  diverso da  *56,*  state1 , *88,* quando  *43,*   MainClass_C1_timer_T5 del campo  MainClass_C1     *105,* è disattivo *45,* e  se  MainClass_C1_contatore_Co3 del campo  MainClass_C1 di SubClass_C2_lista_L7 è  uguale a  *53,* 14210 *42,* o  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L5 è  diverso da GialloGiallo
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_AndLogicOP_2 = true;
    res_AndLogicOP_2 = (res_AndLogicOP_2 && (L_P1__GetSubcl29(my_id) == true));
    bool res_ForAllPredicateNotEmpty_3 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl5Length(my_id); ++i)
    {
    L_P1__Recor1 it = L_P1__GetRecSubcl5(my_id,i);
    bool res_ImpliesLogicOp_4 = true;
    if(Timer_Disattivo(L_P1__GetMainc29(it.mainc37))){
    res_ImpliesLogicOp_4 = (res_ImpliesLogicOp_4 && (L_P1__GetParamMainc6(it.mainc37) > 6u));
    res_ForAllPredicateNotEmpty_3 = res_ImpliesLogicOp_4;
    if(!res_ForAllPredicateNotEmpty_3) {break;}
    }
    }
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_ForAllPredicateNotEmpty_3);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_2);
    bool res_AndLogicOP_5 = true;
    bool res_AndLogicOP_6 = true;
    bool res_AndLogicOP_7 = true;
    res_AndLogicOP_7 = (res_AndLogicOP_7 && (Counter_GetValore(L_P1__GetSubcl45(my_id)) > 12u));
    bool res_ForAllPredicateNotEmpty_8 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl5Length(my_id); ++i)
    {
    L_P1__Recor1 it = L_P1__GetRecSubcl5(my_id,i);
    bool res_ImpliesLogicOp_9 = true;
    if((L_P1__GetMainc26(it.mainc37) > 1u)){
    res_ImpliesLogicOp_9 = (res_ImpliesLogicOp_9 && (Counter_GetValore(L_P1__GetMainc32(it.mainc37)) < 12453u));
    res_ForAllPredicateNotEmpty_8 = res_ImpliesLogicOp_9;
    if(!res_ForAllPredicateNotEmpty_8) {break;}
    }
    }
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_ForAllPredicateNotEmpty_8);
    
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_AndLogicOP_7);
    bool res_AndLogicOP_10 = true;
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! Timer_Disattivo(L_P1__GetSubcl41(my_id)));
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_NotLogicOP_11);
    bool res_ForAllPredicateNotEmpty_12 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl5Length(my_id); ++i)
    {
    L_P1__Recor1 it = L_P1__GetRecSubcl5(my_id,i);
    bool res_ImpliesLogicOp_13 = true;
    if(Timer_Disattivo(L_P1__GetMainc29(it.mainc37))){
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1_C1_GetState(it.mainc37) == C1_St_state));
    res_ImpliesLogicOp_13 = (res_ImpliesLogicOp_13 && res_NotLogicOP_14);
    res_ForAllPredicateNotEmpty_12 = res_ImpliesLogicOp_13;
    if(!res_ForAllPredicateNotEmpty_12) {break;}
    }
    }
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_ForAllPredicateNotEmpty_12);
    
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_AndLogicOP_10);
    
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_AndLogicOP_6);
    bool res_ForAllPredicate_15 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl6Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl6(my_id,i);
    bool res_ImpliesLogicOp_16 = true;
    res_ImpliesLogicOp_16 = (res_ImpliesLogicOp_16 && (Counter_GetValore(L_P1__GetMainc33(it.mainc36)) == 14210u));
    res_ForAllPredicate_15 = res_ImpliesLogicOp_16;
    if(!res_ForAllPredicate_15) {break;}
    }
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_ForAllPredicate_15);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_5);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_ForAllPredicate_17 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl5Length(my_id); ++i)
    {
    L_P1__Recor1 it = L_P1__GetRecSubcl5(my_id,i);
    bool res_ImpliesLogicOp_18 = true;
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (L_P1__GetInMainc4(it.mainc37) == giallogiall));
    res_ImpliesLogicOp_18 = (res_ImpliesLogicOp_18 && res_NotLogicOP_19);
    res_ForAllPredicate_17 = res_ImpliesLogicOp_18;
    if(!res_ForAllPredicate_17) {break;}
    }
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_ForAllPredicate_17);
    
    if(res_OrLogicOP_0){
    
    res_macro_val = c180;
    }
    else{
    res_macro_val = c180;
    }
    return res_macro_val;
}



