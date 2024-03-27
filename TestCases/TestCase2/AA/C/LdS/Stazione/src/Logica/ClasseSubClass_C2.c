// Codice del modello 'TestCase2', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#include "Logica/ClasseMainClass_C1.h"
#include "Logica/ClasseSubClass_C2.h"
#include "Logica/ClasseSubClass_C3.h"
#include "Logica/ClasseSubClass_C2_priv.h"
#include "config.h"
#include "scheduler.h"


// ********** Gestione comandi manuali **********

static void L_P1_C2_InitCmdsResponse(instance_id_t const my_id)
{
    // for each manual command of L_P1_C2
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
    if (L_P1__GetInEvent5(my_id)) {
	    L_P1__SetOutEvent9(my_id, LDS_MANCMD_UNEXPECTED);
    } else {
        L_P1__SetOutEvent9(my_id, LDS_MANCMD_NOOP);
    }
    if (L_P1__GetInEvent6(my_id)) {
	    L_P1__SetOutEvent10(my_id, LDS_MANCMD_UNEXPECTED);
    } else {
        L_P1__SetOutEvent10(my_id, LDS_MANCMD_NOOP);
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
static inline bool L_P1__Guard6(instance_id_t const my_id)
{
    return true;
}


/*
    CNL corrispondente:
     
    {
    	
    Nessuna
    }
*/
static inline bool L_P1__Guard7(instance_id_t const my_id)
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
static inline void L_P1__Effec6(instance_id_t const my_id)
{
    
}


/*
    CNL corrispondente:
     
    {
    Nessuna
    }
*/
static inline void L_P1__Effec7(instance_id_t const my_id)
{
    
}



// ********** Definizione metodi **********

// Metodi standard

void L_P1_C2_Init(instance_id_t const my_id)
{
    // init variabili di stato
    L_P1__SetStato3(my_id, C2_St_Stato);
    L_P1__SetSubcl26(my_id, giallox);
    L_P1__SetSubcl28(my_id, gialloverde);
    L_P1__SetSubcl30(my_id, false);
    L_P1__SetSubcl32(my_id, giallox);
    L_P1__SetSubcl34(my_id, 0);
    L_P1__SetSubcl36(my_id, false);
    L_P1__SetSubcl37(my_id, false);
    L_P1__SetSubcl38(my_id, rossogiallo3);
    L_P1__SetSubcl39(my_id, rossogiallo3);
    L_P1__SetSubcl40(my_id, false);
    L_P1__SetSubcl41(my_id, false);
    L_P1__SetSubcl42(my_id, 0);
    L_P1__SetSubcl43(my_id, gialloverde);
    L_P1__SetSubcl44(my_id, 0);
    L_P1__SetSubcl45(my_id, giallox);
    // init controlli precedenti
    L_P1__SetSubcl17(my_id, false);
    L_P1__SetSubcl19(my_id, true);
    L_P1__SetSubcl21(my_id, true);
    L_P1__SetSubcl23(my_id, rossogiallo2);
    L_P1__SetSubcl25(my_id, true);
    // init Timer e Counter
    Timer_AggmInit(L_P1__GetSubcl46(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl46_ID);
    Timer_Init(L_P1__GetSubcl46(my_id), 132000);
    Timer_AggmInit(L_P1__GetSubcl47(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl47_ID);
    Timer_Init(L_P1__GetSubcl47(my_id), 132000);
    Timer_AggmInit(L_P1__GetSubcl48(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl48_ID);
    Timer_Init(L_P1__GetSubcl48(my_id), 3000);
    Timer_AggmInit(L_P1__GetSubcl49(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl49_ID);
    Timer_Init(L_P1__GetSubcl49(my_id), 3000);
    Timer_AggmInit(L_P1__GetSubcl50(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl50_ID);
    Timer_Init(L_P1__GetSubcl50(my_id), 315000);
    Timer_AggmInit(L_P1__GetSubcl51(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl51_ID);
    Timer_Init(L_P1__GetSubcl51(my_id), 204000);
    Counter_AggmInit(L_P1__GetSubcl52(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl52_ID);
    Counter_Init(L_P1__GetSubcl52(my_id));
    Counter_AggmInit(L_P1__GetSubcl53(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl53_ID);
    Counter_Init(L_P1__GetSubcl53(my_id));
    // init response
    L_P1_C2_SetResponse(my_id, LDS_SCHED_NOP);

    // transizione iniziale
    if(L_P1__Guard6(my_id)) {
        L_P1_C2_SetState(my_id, C2_St_state);
	L_P1__Effec6(my_id);
    } else {
        STOP_EXECUTION(LOGIC_ERROR);
    }
    // init variabili precedenti
    L_P1__SetSubcl27(my_id, L_P1__GetSubcl26(my_id));
    L_P1__SetSubcl29(my_id, L_P1__GetSubcl28(my_id));
    L_P1__SetSubcl31(my_id, L_P1__GetSubcl30(my_id));
    L_P1__SetSubcl33(my_id, L_P1__GetSubcl32(my_id));
    L_P1__SetSubcl35(my_id, L_P1__GetSubcl34(my_id));
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
            if (L_P1__Guard7(my_id)) {
                L_P1_C2_SetState(my_id, C2_St_state);
                L_P1__Effec7(my_id);				
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
    Timer_Exec(L_P1__GetSubcl46(my_id));
    Timer_Exec(L_P1__GetSubcl47(my_id));
    Timer_Exec(L_P1__GetSubcl48(my_id));
    Timer_Exec(L_P1__GetSubcl49(my_id));
    Timer_Exec(L_P1__GetSubcl50(my_id));
    Timer_Exec(L_P1__GetSubcl51(my_id));
}

void L_P1_C2_GSetSafe(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C2(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C2(proc_id);
    L_P1__SetOutSubcl(my_id, rossogiallo1);
    L_P1__SetOutSubcl1(my_id, false);
    L_P1__SetOutSubcl2(my_id, false);
    L_P1__SetOutSubcl3(my_id, true);
    L_P1__SetOutSubcl4(my_id, true);
}

void L_P1_C2_GUpdatePrev(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C2(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C2(proc_id);
    L_P1__SetSubcl17(my_id, L_P1__GetInSubcl16(my_id));
    L_P1__SetSubcl19(my_id, L_P1__GetInSubcl18(my_id));
    L_P1__SetSubcl21(my_id, L_P1__GetInSubcl20(my_id));
    L_P1__SetSubcl23(my_id, L_P1__GetInSubcl22(my_id));
    L_P1__SetSubcl25(my_id, L_P1__GetInSubcl24(my_id));
    L_P1__SetSubcl27(my_id, L_P1__GetSubcl26(my_id));
    L_P1__SetSubcl29(my_id, L_P1__GetSubcl28(my_id));
    L_P1__SetSubcl31(my_id, L_P1__GetSubcl30(my_id));
    L_P1__SetSubcl33(my_id, L_P1__GetSubcl32(my_id));
    L_P1__SetSubcl35(my_id, L_P1__GetSubcl34(my_id));
}

// ********** Definizione macro **********

// Macro di effetto

/*
    CNL corrispondente:
    
    { commento: {38,}  se il contatore SubClass_C2_contatore_Co4 è  diverso da  commento: {56,} 114,  commento: {43,}  se MainClass_C1_timer_T4 del campo  MainClass_C1 di SubClass_C2_lista_L9 è attivo, commento: {88,} quando  commento: {43,}   MainClass_C1_timer_T4 del campo  MainClass_C1     commento: {105,} è attivo commento: {35,} o  se il controllo SubClass_C2_controllo_C3 non è  diverso da Verde commento: {38,} e  se il contatore SubClass_C2_contatore_Co3 è  minore di  commento: {55,} 1432 commento: {37,} e  se la variabile SubClass_C2_variabile_V8 è  diverso da avvio, commento: {66,} Assegna al comando SubClass_C2_comando_C2 il valore  True 
    
     ,altrimenti  commento: {66,} Assegna al comando SubClass_C2_comando_C6 il valore  False 
    
    
     commento: {35,}  se il controllo SubClass_C2_controllo_C10 non è  diverso da RossoGiallo,  commento: {44,}  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  commento: {105,} è  diverso da  True , commento: {88,} quando  commento: {45,}    MainClass_C1_contatore_Co1 del campo  MainClass_C1     commento: {105,} è  maggiore di  commento: {54,} 1115 commento: {34,} e  se il parametro SubClass_C2_parametro_P4 non è  uguale a RossoGialloxVerdex, commento: {66,} Assegna al comando SubClass_C2_comando_C2 il valore  False 
    
       
     commento: {34,}  se il parametro SubClass_C2_parametro_P4 è  uguale a RossoGialloxVerdex commento: {37,} o  se la variabile SubClass_C2_variabile_V2 è  maggiore di  commento: {54,} 7 commento: {38,} e  se il contatore SubClass_C2_contatore_Co4 non è  uguale a  commento: {53,} 1304 commento: {37,} e  se la variabile SubClass_C2_variabile_V8 non è  diverso da avvio, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V7 il valore 4
    
       
     commento: {110,}  se il ripristino del timer  SubClass_C2_restoreTI_TI1 non è disattivo commento: {36,} e  se il timer SubClass_C2_timer_T3 non è scaduto commento: {38,} o  se il contatore SubClass_C2_contatore_Co4 è  diverso da  commento: {56,} 1432, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V8 il valore avvio
    
     ,altrimenti   Applica gli effetti
           della macro SubClass_C2_macroef_M2  commento: {73,}
    
    
    
    }
*/
void L_P1__Macro4(instance_id_t const my_id )
{
//  *38,*  se il contatore SubClass_C2_contatore_Co4 è  diverso da  *56,* 114,  *43,*  se MainClass_C1_timer_T4 del campo  MainClass_C1 di SubClass_C2_lista_L9 è attivo, *88,* quando  *43,*   MainClass_C1_timer_T4 del campo  MainClass_C1     *105,* è attivo *35,* o  se il controllo SubClass_C2_controllo_C3 non è  diverso da Verde *38,* e  se il contatore SubClass_C2_contatore_Co3 è  minore di  *55,* 1432 *37,* e  se la variabile SubClass_C2_variabile_V8 è  diverso da avvio, *66,* Assegna al comando SubClass_C2_comando_C2 il valore  True 
    // ,altrimenti  *66,* Assegna al comando SubClass_C2_comando_C6 il valore  False
    bool res_OrLogicOP_0 = false;
    bool res_AndLogicOP_1 = true;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (Counter_GetValore(L_P1__GetSubcl53(my_id)) == 114u));
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_2);
    bool res_ForAllPredicate_3 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl10Length(my_id); ++i)
    {
    L_P1__Recor1 it = L_P1__GetRecSubcl10(my_id,i);
    bool res_ImpliesLogicOp_4 = true;
    if(Timer_Attivo(L_P1__GetMainc31(it.mainc37))){
    res_ImpliesLogicOp_4 = (res_ImpliesLogicOp_4 && Timer_Attivo(L_P1__GetMainc31(it.mainc37)));
    }
    res_ForAllPredicate_3 = res_ImpliesLogicOp_4;
    if(!res_ForAllPredicate_3) {break;}
    }
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_ForAllPredicate_3);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_1);
    bool res_AndLogicOP_5 = true;
    bool res_AndLogicOP_6 = true;
    bool res_NotLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetInSubcl6(my_id) == verde));
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! res_NotLogicOP_8);
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_7);
    res_AndLogicOP_6 = (res_AndLogicOP_6 && (Counter_GetValore(L_P1__GetSubcl52(my_id)) < 1432u));
    
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_AndLogicOP_6);
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetSubcl45(my_id) == avvio));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_9);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_5);
    
    if(res_OrLogicOP_0){
    
    L_P1__SetOutSubcl1(my_id,true);
    }else{
    
    L_P1__SetOutSubcl4(my_id,false);
    }
    //  *35,*  se il controllo SubClass_C2_controllo_C10 non è  diverso da RossoGiallo,  *44,*  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  *105,* è  diverso da  True , *88,* quando  *45,*    MainClass_C1_contatore_Co1 del campo  MainClass_C1     *105,* è  maggiore di  *54,* 1115 *34,* e  se il parametro SubClass_C2_parametro_P4 non è  uguale a RossoGialloxVerdex, *66,* Assegna al comando SubClass_C2_comando_C2 il valore  False
    bool res_AndLogicOP_10 = true;
    bool res_AndLogicOP_11 = true;
    bool res_NotLogicOP_12 = true;
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (L_P1__GetInSubcl5(my_id) == rossogiallo2));
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! res_NotLogicOP_13);
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_NotLogicOP_12);
    bool res_ForAllPredicateNotEmpty_14 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl9Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl9(my_id,i);
    bool res_ImpliesLogicOp_15 = true;
    if((Counter_GetValore(L_P1__GetMainc33(it.mainc36)) > 1115u)){
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (L_P1__GetMainc22(it.mainc36) == true));
    res_ImpliesLogicOp_15 = (res_ImpliesLogicOp_15 && res_NotLogicOP_16);
    res_ForAllPredicateNotEmpty_14 = res_ImpliesLogicOp_15;
    if(!res_ForAllPredicateNotEmpty_14) {break;}
    }
    }
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_ForAllPredicateNotEmpty_14);
    
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_AndLogicOP_11);
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! (L_P1__GetParamSubcl14(my_id) == rossogiallo1));
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_NotLogicOP_17);
    
    if(res_AndLogicOP_10){
    
    L_P1__SetOutSubcl1(my_id,false);
    }
    //  *34,*  se il parametro SubClass_C2_parametro_P4 è  uguale a RossoGialloxVerdex *37,* o  se la variabile SubClass_C2_variabile_V2 è  maggiore di  *54,* 7 *38,* e  se il contatore SubClass_C2_contatore_Co4 non è  uguale a  *53,* 1304 *37,* e  se la variabile SubClass_C2_variabile_V8 non è  diverso da avvio, *67,* Assegna alla variabile SubClass_C2_variabile_V7 il valore 4
    bool res_OrLogicOP_18 = false;
    res_OrLogicOP_18 = (res_OrLogicOP_18 || (L_P1__GetParamSubcl14(my_id) == rossogiallo1));
    bool res_AndLogicOP_19 = true;
    bool res_AndLogicOP_20 = true;
    res_AndLogicOP_20 = (res_AndLogicOP_20 && (L_P1__GetSubcl42(my_id) > 7u));
    bool res_NotLogicOP_21 = true;
    res_NotLogicOP_21 = (res_NotLogicOP_21 && ! (Counter_GetValore(L_P1__GetSubcl53(my_id)) == 1304u));
    res_AndLogicOP_20 = (res_AndLogicOP_20 && res_NotLogicOP_21);
    
    res_AndLogicOP_19 = (res_AndLogicOP_19 && res_AndLogicOP_20);
    bool res_NotLogicOP_22 = true;
    bool res_NotLogicOP_23 = true;
    res_NotLogicOP_23 = (res_NotLogicOP_23 && ! (L_P1__GetSubcl45(my_id) == avvio));
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! res_NotLogicOP_23);
    res_AndLogicOP_19 = (res_AndLogicOP_19 && res_NotLogicOP_22);
    
    res_OrLogicOP_18 = (res_OrLogicOP_18 || res_AndLogicOP_19);
    
    if(res_OrLogicOP_18){
    
    L_P1__SetSubcl44(my_id,4u);
    }
    //  *110,*  se il ripristino del timer  SubClass_C2_restoreTI_TI1 non è disattivo *36,* e  se il timer SubClass_C2_timer_T3 non è scaduto *38,* o  se il contatore SubClass_C2_contatore_Co4 è  diverso da  *56,* 1432, *67,* Assegna alla variabile SubClass_C2_variabile_V8 il valore avvio
    // ,altrimenti   Applica gli effetti
    //       della macro SubClass_C2_macroef_M2
    bool res_OrLogicOP_24 = false;
    bool res_AndLogicOP_25 = true;
    bool res_NotLogicOP_26 = true;
    res_NotLogicOP_26 = (res_NotLogicOP_26 && ! Timer_Disattivo(L_P1__GetSubcl47(my_id)));
    res_AndLogicOP_25 = (res_AndLogicOP_25 && res_NotLogicOP_26);
    bool res_NotLogicOP_27 = true;
    res_NotLogicOP_27 = (res_NotLogicOP_27 && ! Timer_Scaduto(L_P1__GetSubcl51(my_id)));
    res_AndLogicOP_25 = (res_AndLogicOP_25 && res_NotLogicOP_27);
    
    res_OrLogicOP_24 = (res_OrLogicOP_24 || res_AndLogicOP_25);
    bool res_NotLogicOP_28 = true;
    res_NotLogicOP_28 = (res_NotLogicOP_28 && ! (Counter_GetValore(L_P1__GetSubcl53(my_id)) == 1432u));
    res_OrLogicOP_24 = (res_OrLogicOP_24 || res_NotLogicOP_28);
    
    if(res_OrLogicOP_24){
    
    L_P1__SetSubcl45(my_id,avvio);
    }else{
    
    L_P1__Macro5(my_id);
    }
}

/*
    CNL corrispondente:
    
    { commento: {110,}  se il ripristino del timer  SubClass_C2_restoreTI_TI2 non è disattivo commento: {35,} e  se il controllo SubClass_C2_controllo_C10 è  uguale a RossoGiallo commento: {35,} e  se il controllo SubClass_C2_controllo_C3 è  diverso da Verde commento: {35,} e  se il controllo SubClass_C2_controllo_C3 non è  uguale a Verde, commento: {69,}Disattiva il timer SubClass_C2_timer_T10
    
     ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V8 il valore avvio
    
    
     commento: {34,}  se il parametro SubClass_C2_parametro_P2 non è  uguale a Verde e  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} o  se il timer SubClass_C2_timer_T10 è scaduto, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V2 il valore 3
    
       
     commento: {41,}  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  commento: {105,} è  uguale a c270x commento: {37,} e  se la variabile SubClass_C2_variabile_V8 non è  uguale a avvio commento: {35,} e  se il controllo SubClass_C2_controllo_C3 è  uguale a Verde commento: {38,} e  se il contatore SubClass_C2_contatore_Co3 è  uguale a  commento: {53,} 151 o  se il controllo ConsDef  è  uguale a FALSE , commento: {66,} Assegna al comando SubClass_C2_comando_C2 il valore  False 
    
     ,altrimenti  commento: {71,}Decrementa il contatore SubClass_C2_contatore_Co4
    
    
     commento: {41,}  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  commento: {105,} è  diverso da c270x commento: {38,} e  se il contatore SubClass_C2_contatore_Co3 non è  uguale a  commento: {53,} 11 o  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} o  se il controllo SubClass_C2_controllo_C3 è  diverso da Verde e  se il controllo ConsDef  è  uguale a FALSE , commento: {69,}Disattiva il timer SubClass_C2_timer_T10
    
     ,altrimenti  commento: {66,} Assegna al comando SubClass_C2_comando_C6 il valore  False 
    
    
    
    }
*/
void L_P1__Macro5(instance_id_t const my_id )
{
//  *110,*  se il ripristino del timer  SubClass_C2_restoreTI_TI2 non è disattivo *35,* e  se il controllo SubClass_C2_controllo_C10 è  uguale a RossoGiallo *35,* e  se il controllo SubClass_C2_controllo_C3 è  diverso da Verde *35,* e  se il controllo SubClass_C2_controllo_C3 non è  uguale a Verde, *69,*Disattiva il timer SubClass_C2_timer_T10
    // ,altrimenti  *67,* Assegna alla variabile SubClass_C2_variabile_V8 il valore avvio
    bool res_AndLogicOP_0 = true;
    bool res_AndLogicOP_1 = true;
    bool res_AndLogicOP_2 = true;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! Timer_Disattivo(L_P1__GetSubcl49(my_id)));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_3);
    res_AndLogicOP_2 = (res_AndLogicOP_2 && (L_P1__GetInSubcl5(my_id) == rossogiallo2));
    
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_AndLogicOP_2);
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetInSubcl6(my_id) == verde));
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_4);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_AndLogicOP_1);
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetInSubcl6(my_id) == verde));
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_NotLogicOP_5);
    
    if(res_AndLogicOP_0){
    
    Timer_Disattiva(L_P1__GetSubcl50(my_id));
    }else{
    
    L_P1__SetSubcl45(my_id,avvio);
    }
    //  *34,*  se il parametro SubClass_C2_parametro_P2 non è  uguale a Verde e  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  *36,* o  se il timer SubClass_C2_timer_T10 è scaduto, *67,* Assegna alla variabile SubClass_C2_variabile_V2 il valore 3
    bool res_OrLogicOP_6 = false;
    bool res_OrLogicOP_7 = false;
    bool res_AndLogicOP_8 = true;
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetParamSubcl13(my_id) == verde));
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_9);
    res_AndLogicOP_8 = (res_AndLogicOP_8 && (L_P1__GetInConsd1(my_id) == false));
    
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_AndLogicOP_8);
    res_OrLogicOP_7 = (res_OrLogicOP_7 || (L_P1__GetInConsd1(my_id) == false));
    
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_OrLogicOP_7);
    res_OrLogicOP_6 = (res_OrLogicOP_6 || Timer_Scaduto(L_P1__GetSubcl50(my_id)));
    
    if(res_OrLogicOP_6){
    
    L_P1__SetSubcl42(my_id,3u);
    }
    //  *41,*  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  *105,* è  uguale a c270x *37,* e  se la variabile SubClass_C2_variabile_V8 non è  uguale a avvio *35,* e  se il controllo SubClass_C2_controllo_C3 è  uguale a Verde *38,* e  se il contatore SubClass_C2_contatore_Co3 è  uguale a  *53,* 151 o  se il controllo ConsDef  è  uguale a FALSE , *66,* Assegna al comando SubClass_C2_comando_C2 il valore  False 
    // ,altrimenti  *71,*Decrementa il contatore SubClass_C2_contatore_Co4
    bool res_OrLogicOP_10 = false;
    bool res_AndLogicOP_11 = true;
    bool res_AndLogicOP_12 = true;
    bool res_AndLogicOP_13 = true;
    bool res_ForAllPredicateNotEmpty_14 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl7Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl7(my_id,i);
    bool res_ImpliesLogicOp_15 = true;
    res_ImpliesLogicOp_15 = (res_ImpliesLogicOp_15 && (L_P1__GetParamMainc5(it.mainc36) == c270x));
    res_ForAllPredicateNotEmpty_14 = res_ImpliesLogicOp_15;
    if(!res_ForAllPredicateNotEmpty_14) {break;}
    }
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_ForAllPredicateNotEmpty_14);
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (L_P1__GetSubcl45(my_id) == avvio));
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_NotLogicOP_16);
    
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_AndLogicOP_13);
    res_AndLogicOP_12 = (res_AndLogicOP_12 && (L_P1__GetInSubcl6(my_id) == verde));
    
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_AndLogicOP_12);
    res_AndLogicOP_11 = (res_AndLogicOP_11 && (Counter_GetValore(L_P1__GetSubcl52(my_id)) == 151u));
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_AndLogicOP_11);
    res_OrLogicOP_10 = (res_OrLogicOP_10 || (L_P1__GetInConsd1(my_id) == false));
    
    if(res_OrLogicOP_10){
    
    L_P1__SetOutSubcl1(my_id,false);
    }else{
    
    Counter_Decr(L_P1__GetSubcl53(my_id));
    }
    //  *41,*  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  *105,* è  diverso da c270x *38,* e  se il contatore SubClass_C2_contatore_Co3 non è  uguale a  *53,* 11 o  se il controllo ConsDef  è  uguale a FALSE  *35,* o  se il controllo SubClass_C2_controllo_C3 è  diverso da Verde e  se il controllo ConsDef  è  uguale a FALSE , *69,*Disattiva il timer SubClass_C2_timer_T10
    // ,altrimenti  *66,* Assegna al comando SubClass_C2_comando_C6 il valore  False
    bool res_OrLogicOP_17 = false;
    bool res_OrLogicOP_18 = false;
    bool res_AndLogicOP_19 = true;
    bool res_ForAllPredicateNotEmpty_20 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl9Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl9(my_id,i);
    bool res_ImpliesLogicOp_21 = true;
    bool res_NotLogicOP_22 = true;
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! (L_P1__GetParamMainc5(it.mainc36) == c270x));
    res_ImpliesLogicOp_21 = (res_ImpliesLogicOp_21 && res_NotLogicOP_22);
    res_ForAllPredicateNotEmpty_20 = res_ImpliesLogicOp_21;
    if(!res_ForAllPredicateNotEmpty_20) {break;}
    }
    res_AndLogicOP_19 = (res_AndLogicOP_19 && res_ForAllPredicateNotEmpty_20);
    bool res_NotLogicOP_23 = true;
    res_NotLogicOP_23 = (res_NotLogicOP_23 && ! (Counter_GetValore(L_P1__GetSubcl52(my_id)) == 11u));
    res_AndLogicOP_19 = (res_AndLogicOP_19 && res_NotLogicOP_23);
    
    res_OrLogicOP_18 = (res_OrLogicOP_18 || res_AndLogicOP_19);
    res_OrLogicOP_18 = (res_OrLogicOP_18 || (L_P1__GetInConsd1(my_id) == false));
    
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_OrLogicOP_18);
    bool res_AndLogicOP_24 = true;
    bool res_NotLogicOP_25 = true;
    res_NotLogicOP_25 = (res_NotLogicOP_25 && ! (L_P1__GetInSubcl6(my_id) == verde));
    res_AndLogicOP_24 = (res_AndLogicOP_24 && res_NotLogicOP_25);
    res_AndLogicOP_24 = (res_AndLogicOP_24 && (L_P1__GetInConsd1(my_id) == false));
    
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_AndLogicOP_24);
    
    if(res_OrLogicOP_17){
    
    Timer_Disattiva(L_P1__GetSubcl50(my_id));
    }else{
    
    L_P1__SetOutSubcl4(my_id,false);
    }
}

/*
    CNL corrispondente:
     
    { commento: {36,}  se il timer SubClass_C2_timer_T3 non è scaduto commento: {38,} e  se il contatore SubClass_C2_contatore_Co3 è  maggiore di  commento: {54,} 115 commento: {38,} o  se il contatore SubClass_C2_contatore_Co3 è  maggiore di  commento: {54,} 110, commento: {71,}Decrementa il contatore SubClass_C2_contatore_Co4
    
       
     commento: {44,}  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  commento: {105,} è  diverso da c270x commento: {37,} e  se la variabile SubClass_C2_variabile_V8 è  diverso da avvio commento: {34,} o  se il parametro SubClass_C2_parametro_P10 è  diverso da  True  commento: {37,} o  se la variabile SubClass_C2_variabile_V2 non è  diverso da  commento: {56,} 10 commento: {36,} e  se il timer SubClass_C2_timer_T3 non è attivo, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V8 il valore avvio
    
     ,altrimenti   Applica gli effetti
           della macro SubClass_C2_macroef_M2  commento: {73,}
    
    
    
    }
*/
void L_P1__Macro6(instance_id_t const my_id )
{
//  *36,*  se il timer SubClass_C2_timer_T3 non è scaduto *38,* e  se il contatore SubClass_C2_contatore_Co3 è  maggiore di  *54,* 115 *38,* o  se il contatore SubClass_C2_contatore_Co3 è  maggiore di  *54,* 110, *71,*Decrementa il contatore SubClass_C2_contatore_Co4
    bool res_OrLogicOP_0 = false;
    bool res_AndLogicOP_1 = true;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! Timer_Scaduto(L_P1__GetSubcl51(my_id)));
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_2);
    res_AndLogicOP_1 = (res_AndLogicOP_1 && (Counter_GetValore(L_P1__GetSubcl52(my_id)) > 115u));
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_1);
    res_OrLogicOP_0 = (res_OrLogicOP_0 || (Counter_GetValore(L_P1__GetSubcl52(my_id)) > 110u));
    
    if(res_OrLogicOP_0){
    
    Counter_Decr(L_P1__GetSubcl53(my_id));
    }
    //  *44,*  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  *105,* è  diverso da c270x *37,* e  se la variabile SubClass_C2_variabile_V8 è  diverso da avvio *34,* o  se il parametro SubClass_C2_parametro_P10 è  diverso da  True  *37,* o  se la variabile SubClass_C2_variabile_V2 non è  diverso da  *56,* 10 *36,* e  se il timer SubClass_C2_timer_T3 non è attivo, *67,* Assegna alla variabile SubClass_C2_variabile_V8 il valore avvio
    // ,altrimenti   Applica gli effetti
    //       della macro SubClass_C2_macroef_M2
    bool res_OrLogicOP_3 = false;
    bool res_OrLogicOP_4 = false;
    bool res_AndLogicOP_5 = true;
    bool res_ForAllPredicateNotEmpty_6 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl9Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl9(my_id,i);
    bool res_ImpliesLogicOp_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetMainc24(it.mainc36) == c270x));
    res_ImpliesLogicOp_7 = (res_ImpliesLogicOp_7 && res_NotLogicOP_8);
    res_ForAllPredicateNotEmpty_6 = res_ImpliesLogicOp_7;
    if(!res_ForAllPredicateNotEmpty_6) {break;}
    }
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_ForAllPredicateNotEmpty_6);
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetSubcl45(my_id) == avvio));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_9);
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_AndLogicOP_5);
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__GetParamSubcl12(my_id) == true));
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_NotLogicOP_10);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_OrLogicOP_4);
    bool res_AndLogicOP_11 = true;
    bool res_NotLogicOP_12 = true;
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (L_P1__GetSubcl42(my_id) == 10u));
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! res_NotLogicOP_13);
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_NotLogicOP_12);
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! Timer_Attivo(L_P1__GetSubcl51(my_id)));
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_NotLogicOP_14);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_AndLogicOP_11);
    
    if(res_OrLogicOP_3){
    
    L_P1__SetSubcl45(my_id,avvio);
    }else{
    
    L_P1__Macro5(my_id);
    }
}

/*
    CNL corrispondente:
    
    { commento: {41,}  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a c270x,  Applica gli effetti
           della macro SubClass_C2_macroef_M2  commento: {73,}
    
     ,altrimenti  commento: {68,}Attiva il timer SubClass_C2_timer_T10
    
    
     commento: {36,}  se il timer SubClass_C2_timer_T3 non è scaduto,  commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a  commento: {53,}  state1 , commento: {88,} quando  commento: {42,}    MainClass_C1_controllo_C8 del campo  MainClass_C1     è  uguale a c270x commento: {34,} e  se il parametro SubClass_C2_parametro_P2 non è  uguale a Verde commento: {38,} o  se il contatore SubClass_C2_contatore_Co3 non è  diverso da  commento: {56,} 15 commento: {34,} e  se il parametro SubClass_C2_parametro_P2 è  diverso da Verde commento: {35,} e  se il controllo SubClass_C2_controllo_C3 non è  diverso da Verde, commento: {68,}Attiva il timer SubClass_C2_timer_T3
    
     ,altrimenti  commento: {69,}Disattiva il timer SubClass_C2_timer_T10
    
    
    
    }
*/
void L_P1__Macro7(instance_id_t const my_id )
{
//  *41,*  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a c270x,  Applica gli effetti
    //       della macro SubClass_C2_macroef_M2  *73,*
    // ,altrimenti  *68,*Attiva il timer SubClass_C2_timer_T10
    bool res_ForAllPredicate_0 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl10Length(my_id); ++i)
    {
    L_P1__Recor1 it = L_P1__GetRecSubcl10(my_id,i);
    bool res_ImpliesLogicOp_1 = true;
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && (L_P1__GetParamMainc5(it.mainc37) == c270x));
    res_ForAllPredicate_0 = res_ImpliesLogicOp_1;
    if(!res_ForAllPredicate_0) {break;}
    }
    if(res_ForAllPredicate_0){
    
    L_P1__Macro5(my_id);
    }else{
    
    Timer_Attiva(L_P1__GetSubcl50(my_id));
    }
    //  *36,*  se il timer SubClass_C2_timer_T3 non è scaduto,  *111,*  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a  *53,*  state1 , *88,* quando  *42,*    MainClass_C1_controllo_C8 del campo  MainClass_C1     è  uguale a c270x *34,* e  se il parametro SubClass_C2_parametro_P2 non è  uguale a Verde *38,* o  se il contatore SubClass_C2_contatore_Co3 non è  diverso da  *56,* 15 *34,* e  se il parametro SubClass_C2_parametro_P2 è  diverso da Verde *35,* e  se il controllo SubClass_C2_controllo_C3 non è  diverso da Verde, *68,*Attiva il timer SubClass_C2_timer_T3
    // ,altrimenti  *69,*Disattiva il timer SubClass_C2_timer_T10
    bool res_OrLogicOP_2 = false;
    bool res_AndLogicOP_3 = true;
    bool res_AndLogicOP_4 = true;
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! Timer_Scaduto(L_P1__GetSubcl51(my_id)));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_5);
    bool res_ForAllPredicate_6 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl10Length(my_id); ++i)
    {
    L_P1__Recor1 it = L_P1__GetRecSubcl10(my_id,i);
    bool res_ImpliesLogicOp_7 = true;
    if((L_P1__GetInMainc3(it.mainc37) == c270x)){
    res_ImpliesLogicOp_7 = (res_ImpliesLogicOp_7 && (L_P1_C1_GetState(it.mainc37) == C1_St_state));
    }
    res_ForAllPredicate_6 = res_ImpliesLogicOp_7;
    if(!res_ForAllPredicate_6) {break;}
    }
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_ForAllPredicate_6);
    
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_AndLogicOP_4);
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetParamSubcl13(my_id) == verde));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_8);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_3);
    bool res_AndLogicOP_9 = true;
    bool res_AndLogicOP_10 = true;
    bool res_NotLogicOP_11 = true;
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (Counter_GetValore(L_P1__GetSubcl52(my_id)) == 15u));
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! res_NotLogicOP_12);
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_NotLogicOP_11);
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (L_P1__GetParamSubcl13(my_id) == verde));
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_NotLogicOP_13);
    
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_AndLogicOP_10);
    bool res_NotLogicOP_14 = true;
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (L_P1__GetInSubcl6(my_id) == verde));
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! res_NotLogicOP_15);
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_NotLogicOP_14);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_9);
    
    if(res_OrLogicOP_2){
    
    Timer_Attiva(L_P1__GetSubcl51(my_id));
    }else{
    
    Timer_Disattiva(L_P1__GetSubcl50(my_id));
    }
}


// Macro di verifica

/*
    CNL corrispondente:
    
    { commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L8 è  uguale a  commento: {53,}  state1  e  se l'argomento argomento_ave1 è  diverso da RossoGialloxVerdex commento: {39,} , Verifica che   commento: {47,49,50,52,}  commento: {34,}  il parametro SubClass_C2_parametro_P1 sia  uguale a RossoGialloxVerdex
     commento: {104,} o  che  commento: {,}  la variabile SubClass_C2_variabile_V2 non sia  diverso da  commento: {56,} 10
     commento: {104,} o  che   l'argomento argomento_ave5 non  sia  uguale a avvio commento: {,} 
     commento: {104,} o  che  commento: {,}  il timer SubClass_C2_timer_T10 sia scaduto
    
    
    }
*/
bool L_P1__Macro10(instance_id_t const my_id , C2_Enumerat1 argom23, C2_Enumerat2 argom24)
{
bool res_AndLogicOP_0 = true;
    
    //  *111,*  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L8 è  uguale a  *53,*  state1  e  se l'argomento argomento_ave1 è  diverso da RossoGialloxVerdex *39,* , Verifica che   *47,49,50,52,*  *34,*  il parametro SubClass_C2_parametro_P1 sia  uguale a RossoGialloxVerdex
    //   *104,* o  che  *,*  la variabile SubClass_C2_variabile_V2 non sia  diverso da  *56,* 10
    //   *104,* o  che   l'argomento argomento_ave5 non  sia  uguale a avvio *,* 
    //   *104,* o  che  *,*  il timer SubClass_C2_timer_T10 sia scaduto
    bool res_ImpliesLogicOp_1 = true;
    bool res_AndLogicOP_2 = true;
    bool res_ForAllPredicate_3 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl9Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl9(my_id,i);
    bool res_ImpliesLogicOp_4 = true;
    res_ImpliesLogicOp_4 = (res_ImpliesLogicOp_4 && (L_P1_C1_GetState(it.mainc36) == C1_St_state));
    res_ForAllPredicate_3 = res_ImpliesLogicOp_4;
    if(!res_ForAllPredicate_3) {break;}
    }
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_ForAllPredicate_3);
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (argom23 == rossogiallo1));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_5);
    
    if(res_AndLogicOP_2){
    bool res_OrLogicOP_6 = false;
    bool res_OrLogicOP_7 = false;
    bool res_OrLogicOP_8 = false;
    res_OrLogicOP_8 = (res_OrLogicOP_8 || (L_P1__GetParamSubcl11(my_id) == rossogiallo1));
    bool res_NotLogicOP_9 = true;
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__GetSubcl42(my_id) == 10u));
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! res_NotLogicOP_10);
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_NotLogicOP_9);
    
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_OrLogicOP_8);
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (argom24 == avvio));
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_NotLogicOP_11);
    
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_OrLogicOP_7);
    res_OrLogicOP_6 = (res_OrLogicOP_6 || Timer_Scaduto(L_P1__GetSubcl50(my_id)));
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_OrLogicOP_6);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
     
    {  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} o  se il timer SubClass_C2_timer_T3 non è scaduto commento: {34,} o  se il parametro SubClass_C2_parametro_P2 non è  uguale a Verde, Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
    
    
    }
*/
bool L_P1__Macro11(instance_id_t const my_id )
{
bool res_AndLogicOP_0 = true;
    
    //  se il controllo ConsDef  è  uguale a FALSE  *36,* o  se il timer SubClass_C2_timer_T3 non è scaduto *34,* o  se il parametro SubClass_C2_parametro_P2 non è  uguale a Verde, Verifica che   *48,*   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* e  che   il controllo ConsDef  sia  uguale a FALSE
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    res_OrLogicOP_3 = (res_OrLogicOP_3 || (L_P1__GetInConsd1(my_id) == false));
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! Timer_Scaduto(L_P1__GetSubcl51(my_id)));
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_NotLogicOP_4);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetParamSubcl13(my_id) == verde));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_5);
    
    if(res_OrLogicOP_2){
    bool res_AndLogicOP_6 = true;
    res_AndLogicOP_6 = (res_AndLogicOP_6 && (L_P1__GetInConsd1(my_id) == false));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && (L_P1__GetInConsd1(my_id) == false));
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_AndLogicOP_6);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
    
    { commento: {62,} commento: {41,}  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L7 è  uguale a c270x commento: {35,} e  se il controllo SubClass_C2_controllo_C3 è  uguale a Verde commento: {38,} o  se il contatore SubClass_C2_contatore_Co3 è  maggiore di  commento: {54,} 11504 commento: {37,} e  se la variabile SubClass_C2_variabile_V8 non è  uguale a avvio, Almeno una delle seguenti { 
     commento: {62,} commento: {41,}  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L8 è  uguale a c270x commento: {34,} e  se il parametro SubClass_C2_parametro_P2 è  diverso da Verde commento: {34,} e  se il parametro SubClass_C2_parametro_P2 non è  diverso da Verde commento: {35,} o  se il controllo SubClass_C2_controllo_C10 non è  uguale a RossoGiallo commento: {38,} e  se il contatore SubClass_C2_contatore_Co3 non è  maggiore di  commento: {54,} 133, Almeno una delle seguenti { 
     commento: {63,} commento: {110,}  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è disattivo commento: {38,} o  se il contatore SubClass_C2_contatore_Co4 è  uguale a  commento: {53,} 1221, Solo una delle seguenti { 
     commento: {63,} commento: {35,}  se il controllo SubClass_C2_controllo_C10 è  uguale a RossoGiallo e  se l'argomento argomento_ave3 non  è  uguale a  False  commento: {39,}  commento: {37,} e  se la variabile SubClass_C2_variabile_V7 è  minore di  commento: {55,} 6 commento: {38,} e  se il contatore SubClass_C2_contatore_Co4 non è  diverso da  commento: {56,} 11504 commento: {36,} o  se il timer SubClass_C2_timer_T3 è disattivo, Solo una delle seguenti { 
     commento: {63,} commento: {42,}  se  MainClass_C1_controllo_C8 del campo  MainClass_C1 di SubClass_C2_lista_L8 è  uguale a c270x commento: {36,} o  se il timer SubClass_C2_timer_T3 non è scaduto commento: {38,} e  se il contatore SubClass_C2_contatore_Co4 è  minore di  commento: {55,} 12504 commento: {36,} o  se il timer SubClass_C2_timer_T3 è attivo, Solo una delle seguenti { 
     commento: {61,} commento: {43,}  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  commento: {105,} è attivo commento: {34,} o  se il parametro SubClass_C2_parametro_P2 non è  uguale a Verde commento: {36,} o  se il timer SubClass_C2_timer_T3 non è disattivo commento: {38,} e  se il contatore SubClass_C2_contatore_Co4 è  diverso da  commento: {56,} 1332 commento: {37,} o  se la variabile SubClass_C2_variabile_V5 è  uguale a RossoGiallo e  se l'argomento argomento_ave4 non  è  uguale a  True  commento: {39,} , Tutte le seguenti { 
     commento: {36,}  se il timer SubClass_C2_timer_T3 è disattivo commento: {34,} e  se il parametro SubClass_C2_parametro_P4 è  uguale a RossoGialloxVerdex commento: {37,} e  se la variabile SubClass_C2_variabile_V2 è  diverso da  commento: {56,} 2 commento: {38,} e  se il contatore SubClass_C2_contatore_Co4 non è  uguale a  commento: {53,} 131 e  se l'argomento argomento_ave2 è  uguale a RossoGialloxVerdex commento: {39,}  commento: {36,} e  se il timer SubClass_C2_timer_T3 non è disattivo, Verifica che   commento: {50,}  commento: {,}  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio
    
    
     } Verifica che   commento: {49,50,51,52,}  commento: {,}  il timer SubClass_C2_timer_T3 non sia disattivo
     commento: {104,} e  che  commento: {,}  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio
     commento: {104,} o  che   l'argomento argomento_ave2 sia  uguale a RossoGialloxVerdex commento: {,} 
     commento: {104,} o  che  commento: {37,}  la variabile SubClass_C2_variabile_V7 sia  uguale a  commento: {53,} 7
     commento: {104,} o  che  commento: {,}  il contatore SubClass_C2_contatore_Co4 sia  maggiore di  commento: {54,} 1550
     commento: {104,} e  che  commento: {37,}  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio
    
    
     } Verifica che   commento: {47,48,49,50,52,}  commento: {34,}  il parametro SubClass_C2_parametro_P2 sia  diverso da Verde
     commento: {104,} e  che  commento: {,}  il controllo SubClass_C2_controllo_C3 non sia  diverso da Verde
     commento: {104,} e  che  commento: {,}  il timer SubClass_C2_timer_T10 sia disattivo
     commento: {104,} o  che  commento: {,}  la variabile SubClass_C2_variabile_V2 sia  diverso da  commento: {56,} 10
     commento: {104,} o  che  commento: {35,}  il controllo SubClass_C2_controllo_C10 non sia  diverso da RossoGiallo
     commento: {104,} e  che   l'argomento argomento_ave4 non  sia  uguale a  False  commento: {,} 
    
    
     } Verifica che   commento: {49,52,}   l'argomento argomento_ave7 non  sia  uguale a  True  commento: {,} 
     commento: {104,} e  che  commento: {,}  il timer SubClass_C2_timer_T10 sia attivo
    
    
     } Verifica che   commento: {47,49,50,}  commento: {,}  il timer SubClass_C2_timer_T10 non sia disattivo
     commento: {104,} e  che  commento: {34,}  il parametro SubClass_C2_parametro_P2 sia  uguale a Verde
     commento: {104,} e  che  commento: {34,}  il parametro SubClass_C2_parametro_P2 non sia  diverso da Verde
     commento: {104,} e  che  commento: {36,}  il timer SubClass_C2_timer_T10 non sia disattivo
     commento: {104,} o  che  commento: {,}  la variabile SubClass_C2_variabile_V8 sia  diverso da avvio
    
    
     } Verifica che   commento: {52,}   l'argomento argomento_ave4 non  sia  uguale a  True  commento: {,} 
    
    
     } Verifica che   commento: {50,51,52,}   l'argomento argomento_ave4 non  sia  uguale a  False  commento: {,} 
     commento: {104,} o  che   l'argomento argomento_ave4 sia  uguale a  True  commento: {39,} 
     commento: {104,} e  che  commento: {,}  la variabile SubClass_C2_variabile_V2 sia  maggiore di  commento: {54,} 6
     commento: {104,} e  che  commento: {,}  il contatore SubClass_C2_contatore_Co3 sia  uguale a  commento: {53,} 13
    
    
    }
*/
bool L_P1__Macro12(instance_id_t const my_id , C2_Enumerat1 argom25, bool argom26, bool argom27, bool argom28, C2_Enumerat3 argom29)
{
bool res_AndLogicOP_0 = true;
    
    //  *62,* *41,*  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L7 è  uguale a c270x *35,* e  se il controllo SubClass_C2_controllo_C3 è  uguale a Verde *38,* o  se il contatore SubClass_C2_contatore_Co3 è  maggiore di  *54,* 11504 *37,* e  se la variabile SubClass_C2_variabile_V8 non è  uguale a avvio, Almeno una delle seguenti { 
    //   *62,* *41,*  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L8 è  uguale a c270x *34,* e  se il parametro SubClass_C2_parametro_P2 è  diverso da Verde *34,* e  se il parametro SubClass_C2_parametro_P2 non è  diverso da Verde *35,* o  se il controllo SubClass_C2_controllo_C10 non è  uguale a RossoGiallo *38,* e  se il contatore SubClass_C2_contatore_Co3 non è  maggiore di  *54,* 133, Almeno una delle seguenti { 
    //   *63,* *110,*  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è disattivo *38,* o  se il contatore SubClass_C2_contatore_Co4 è  uguale a  *53,* 1221, Solo una delle seguenti { 
    //   *63,* *35,*  se il controllo SubClass_C2_controllo_C10 è  uguale a RossoGiallo e  se l'argomento argomento_ave3 non  è  uguale a  False  *39,*  *37,* e  se la variabile SubClass_C2_variabile_V7 è  minore di  *55,* 6 *38,* e  se il contatore SubClass_C2_contatore_Co4 non è  diverso da  *56,* 11504 *36,* o  se il timer SubClass_C2_timer_T3 è disattivo, Solo una delle seguenti { 
    //   *63,* *42,*  se  MainClass_C1_controllo_C8 del campo  MainClass_C1 di SubClass_C2_lista_L8 è  uguale a c270x *36,* o  se il timer SubClass_C2_timer_T3 non è scaduto *38,* e  se il contatore SubClass_C2_contatore_Co4 è  minore di  *55,* 12504 *36,* o  se il timer SubClass_C2_timer_T3 è attivo, Solo una delle seguenti { 
    //   *61,* *43,*  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  *105,* è attivo *34,* o  se il parametro SubClass_C2_parametro_P2 non è  uguale a Verde *36,* o  se il timer SubClass_C2_timer_T3 non è disattivo *38,* e  se il contatore SubClass_C2_contatore_Co4 è  diverso da  *56,* 1332 *37,* o  se la variabile SubClass_C2_variabile_V5 è  uguale a RossoGiallo e  se l'argomento argomento_ave4 non  è  uguale a  True  *39,* , Tutte le seguenti { 
    //   *36,*  se il timer SubClass_C2_timer_T3 è disattivo *34,* e  se il parametro SubClass_C2_parametro_P4 è  uguale a RossoGialloxVerdex *37,* e  se la variabile SubClass_C2_variabile_V2 è  diverso da  *56,* 2 *38,* e  se il contatore SubClass_C2_contatore_Co4 non è  uguale a  *53,* 131 e  se l'argomento argomento_ave2 è  uguale a RossoGialloxVerdex *39,*  *36,* e  se il timer SubClass_C2_timer_T3 non è disattivo, Verifica che   *50,*  *,*  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio
    //   } Verifica che   *49,50,51,52,*  *,*  il timer SubClass_C2_timer_T3 non sia disattivo
    //   *104,* e  che  *,*  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio
    //   *104,* o  che   l'argomento argomento_ave2 sia  uguale a RossoGialloxVerdex *,* 
    //   *104,* o  che  *37,*  la variabile SubClass_C2_variabile_V7 sia  uguale a  *53,* 7
    //   *104,* o  che  *,*  il contatore SubClass_C2_contatore_Co4 sia  maggiore di  *54,* 1550
    //   *104,* e  che  *37,*  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio
    //   } Verifica che   *47,48,49,50,52,*  *34,*  il parametro SubClass_C2_parametro_P2 sia  diverso da Verde
    //   *104,* e  che  *,*  il controllo SubClass_C2_controllo_C3 non sia  diverso da Verde
    //   *104,* e  che  *,*  il timer SubClass_C2_timer_T10 sia disattivo
    //   *104,* o  che  *,*  la variabile SubClass_C2_variabile_V2 sia  diverso da  *56,* 10
    //   *104,* o  che  *35,*  il controllo SubClass_C2_controllo_C10 non sia  diverso da RossoGiallo
    //   *104,* e  che   l'argomento argomento_ave4 non  sia  uguale a  False  *,* 
    //   } Verifica che   *49,52,*   l'argomento argomento_ave7 non  sia  uguale a  True  *,* 
    //   *104,* e  che  *,*  il timer SubClass_C2_timer_T10 sia attivo
    //   } Verifica che   *47,49,50,*  *,*  il timer SubClass_C2_timer_T10 non sia disattivo
    //   *104,* e  che  *34,*  il parametro SubClass_C2_parametro_P2 sia  uguale a Verde
    //   *104,* e  che  *34,*  il parametro SubClass_C2_parametro_P2 non sia  diverso da Verde
    //   *104,* e  che  *36,*  il timer SubClass_C2_timer_T10 non sia disattivo
    //   *104,* o  che  *,*  la variabile SubClass_C2_variabile_V8 sia  diverso da avvio
    //   } Verifica che   *52,*   l'argomento argomento_ave4 non  sia  uguale a  True  *,* 
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_AndLogicOP_3 = true;
    bool res_ForAllPredicate_4 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl8Length(my_id); ++i)
    {
    L_P1__Recor1 it = L_P1__GetRecSubcl8(my_id,i);
    bool res_ImpliesLogicOp_5 = true;
    res_ImpliesLogicOp_5 = (res_ImpliesLogicOp_5 && (L_P1__GetParamMainc5(it.mainc37) == c270x));
    res_ForAllPredicate_4 = res_ImpliesLogicOp_5;
    if(!res_ForAllPredicate_4) {break;}
    }
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_ForAllPredicate_4);
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (L_P1__GetInSubcl6(my_id) == verde));
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_3);
    bool res_AndLogicOP_6 = true;
    res_AndLogicOP_6 = (res_AndLogicOP_6 && (Counter_GetValore(L_P1__GetSubcl52(my_id)) > 11504u));
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetSubcl45(my_id) == avvio));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_7);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_6);
    
    if(res_OrLogicOP_2){
    bool res_OrLogicOP_8 = false;
    bool res_ImpliesLogicOp_9 = true;
    bool res_OrLogicOP_10 = false;
    bool res_AndLogicOP_11 = true;
    bool res_AndLogicOP_12 = true;
    bool res_ForAllPredicate_13 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl9Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl9(my_id,i);
    bool res_ImpliesLogicOp_14 = true;
    res_ImpliesLogicOp_14 = (res_ImpliesLogicOp_14 && (L_P1__GetParamMainc5(it.mainc36) == c270x));
    res_ForAllPredicate_13 = res_ImpliesLogicOp_14;
    if(!res_ForAllPredicate_13) {break;}
    }
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_ForAllPredicate_13);
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (L_P1__GetParamSubcl13(my_id) == verde));
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_NotLogicOP_15);
    
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_AndLogicOP_12);
    bool res_NotLogicOP_16 = true;
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! (L_P1__GetParamSubcl13(my_id) == verde));
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! res_NotLogicOP_17);
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_NotLogicOP_16);
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_AndLogicOP_11);
    bool res_AndLogicOP_18 = true;
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (L_P1__GetInSubcl5(my_id) == rossogiallo2));
    res_AndLogicOP_18 = (res_AndLogicOP_18 && res_NotLogicOP_19);
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! (Counter_GetValore(L_P1__GetSubcl52(my_id)) > 133u));
    res_AndLogicOP_18 = (res_AndLogicOP_18 && res_NotLogicOP_20);
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_AndLogicOP_18);
    
    if(res_OrLogicOP_10){
    bool res_OrLogicOP_21 = false;
    bool res_ImpliesLogicOp_22 = true;
    bool res_OrLogicOP_23 = false;
    res_OrLogicOP_23 = (res_OrLogicOP_23 || Timer_Disattivo(L_P1__GetSubcl47(my_id)));
    res_OrLogicOP_23 = (res_OrLogicOP_23 || (Counter_GetValore(L_P1__GetSubcl53(my_id)) == 1221u));
    
    if(res_OrLogicOP_23){
    bool res_XorLogicOP_24 = true;
    int xorIndex_res_XorLogicOP_24 = 0;
    bool res_ImpliesLogicOp_25 = true;
    bool res_OrLogicOP_26 = false;
    bool res_AndLogicOP_27 = true;
    bool res_AndLogicOP_28 = true;
    bool res_AndLogicOP_29 = true;
    res_AndLogicOP_29 = (res_AndLogicOP_29 && (L_P1__GetInSubcl5(my_id) == rossogiallo2));
    bool res_NotLogicOP_30 = true;
    res_NotLogicOP_30 = (res_NotLogicOP_30 && ! (argom26 == false));
    res_AndLogicOP_29 = (res_AndLogicOP_29 && res_NotLogicOP_30);
    
    res_AndLogicOP_28 = (res_AndLogicOP_28 && res_AndLogicOP_29);
    res_AndLogicOP_28 = (res_AndLogicOP_28 && (L_P1__GetSubcl44(my_id) < 6u));
    
    res_AndLogicOP_27 = (res_AndLogicOP_27 && res_AndLogicOP_28);
    bool res_NotLogicOP_31 = true;
    bool res_NotLogicOP_32 = true;
    res_NotLogicOP_32 = (res_NotLogicOP_32 && ! (Counter_GetValore(L_P1__GetSubcl53(my_id)) == 11504u));
    res_NotLogicOP_31 = (res_NotLogicOP_31 && ! res_NotLogicOP_32);
    res_AndLogicOP_27 = (res_AndLogicOP_27 && res_NotLogicOP_31);
    
    res_OrLogicOP_26 = (res_OrLogicOP_26 || res_AndLogicOP_27);
    res_OrLogicOP_26 = (res_OrLogicOP_26 || Timer_Disattivo(L_P1__GetSubcl51(my_id)));
    
    if(res_OrLogicOP_26){
    bool res_XorLogicOP_33 = true;
    int xorIndex_res_XorLogicOP_33 = 0;
    bool res_ImpliesLogicOp_34 = true;
    bool res_OrLogicOP_35 = false;
    bool res_OrLogicOP_36 = false;
    bool res_ForAllPredicate_37 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl9Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl9(my_id,i);
    bool res_ImpliesLogicOp_38 = true;
    res_ImpliesLogicOp_38 = (res_ImpliesLogicOp_38 && (L_P1__GetInMainc3(it.mainc36) == c270x));
    res_ForAllPredicate_37 = res_ImpliesLogicOp_38;
    if(!res_ForAllPredicate_37) {break;}
    }
    res_OrLogicOP_36 = (res_OrLogicOP_36 || res_ForAllPredicate_37);
    bool res_AndLogicOP_39 = true;
    bool res_NotLogicOP_40 = true;
    res_NotLogicOP_40 = (res_NotLogicOP_40 && ! Timer_Scaduto(L_P1__GetSubcl51(my_id)));
    res_AndLogicOP_39 = (res_AndLogicOP_39 && res_NotLogicOP_40);
    res_AndLogicOP_39 = (res_AndLogicOP_39 && (Counter_GetValore(L_P1__GetSubcl53(my_id)) < 12504u));
    
    res_OrLogicOP_36 = (res_OrLogicOP_36 || res_AndLogicOP_39);
    
    res_OrLogicOP_35 = (res_OrLogicOP_35 || res_OrLogicOP_36);
    res_OrLogicOP_35 = (res_OrLogicOP_35 || Timer_Attivo(L_P1__GetSubcl51(my_id)));
    
    if(res_OrLogicOP_35){
    bool res_XorLogicOP_41 = true;
    int xorIndex_res_XorLogicOP_41 = 0;
    bool res_ImpliesLogicOp_42 = true;
    bool res_OrLogicOP_43 = false;
    bool res_OrLogicOP_44 = false;
    bool res_OrLogicOP_45 = false;
    bool res_ForAllPredicateNotEmpty_46 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl9Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl9(my_id,i);
    bool res_ImpliesLogicOp_47 = true;
    res_ImpliesLogicOp_47 = (res_ImpliesLogicOp_47 && Timer_Attivo(L_P1__GetMainc32(it.mainc36)));
    res_ForAllPredicateNotEmpty_46 = res_ImpliesLogicOp_47;
    if(!res_ForAllPredicateNotEmpty_46) {break;}
    }
    res_OrLogicOP_45 = (res_OrLogicOP_45 || res_ForAllPredicateNotEmpty_46);
    bool res_NotLogicOP_48 = true;
    res_NotLogicOP_48 = (res_NotLogicOP_48 && ! (L_P1__GetParamSubcl13(my_id) == verde));
    res_OrLogicOP_45 = (res_OrLogicOP_45 || res_NotLogicOP_48);
    
    res_OrLogicOP_44 = (res_OrLogicOP_44 || res_OrLogicOP_45);
    bool res_AndLogicOP_49 = true;
    bool res_NotLogicOP_50 = true;
    res_NotLogicOP_50 = (res_NotLogicOP_50 && ! Timer_Disattivo(L_P1__GetSubcl51(my_id)));
    res_AndLogicOP_49 = (res_AndLogicOP_49 && res_NotLogicOP_50);
    bool res_NotLogicOP_51 = true;
    res_NotLogicOP_51 = (res_NotLogicOP_51 && ! (Counter_GetValore(L_P1__GetSubcl53(my_id)) == 1332u));
    res_AndLogicOP_49 = (res_AndLogicOP_49 && res_NotLogicOP_51);
    
    res_OrLogicOP_44 = (res_OrLogicOP_44 || res_AndLogicOP_49);
    
    res_OrLogicOP_43 = (res_OrLogicOP_43 || res_OrLogicOP_44);
    bool res_AndLogicOP_52 = true;
    res_AndLogicOP_52 = (res_AndLogicOP_52 && (L_P1__GetSubcl43(my_id) == rossogiallo2));
    bool res_NotLogicOP_53 = true;
    res_NotLogicOP_53 = (res_NotLogicOP_53 && ! (argom27 == true));
    res_AndLogicOP_52 = (res_AndLogicOP_52 && res_NotLogicOP_53);
    
    res_OrLogicOP_43 = (res_OrLogicOP_43 || res_AndLogicOP_52);
    
    if(res_OrLogicOP_43){
    bool res_ImpliesLogicOp_54 = true;
    bool res_AndLogicOP_55 = true;
    bool res_AndLogicOP_56 = true;
    bool res_AndLogicOP_57 = true;
    bool res_AndLogicOP_58 = true;
    bool res_AndLogicOP_59 = true;
    res_AndLogicOP_59 = (res_AndLogicOP_59 && Timer_Disattivo(L_P1__GetSubcl51(my_id)));
    res_AndLogicOP_59 = (res_AndLogicOP_59 && (L_P1__GetParamSubcl14(my_id) == rossogiallo1));
    
    res_AndLogicOP_58 = (res_AndLogicOP_58 && res_AndLogicOP_59);
    bool res_NotLogicOP_60 = true;
    res_NotLogicOP_60 = (res_NotLogicOP_60 && ! (L_P1__GetSubcl42(my_id) == 2u));
    res_AndLogicOP_58 = (res_AndLogicOP_58 && res_NotLogicOP_60);
    
    res_AndLogicOP_57 = (res_AndLogicOP_57 && res_AndLogicOP_58);
    bool res_NotLogicOP_61 = true;
    res_NotLogicOP_61 = (res_NotLogicOP_61 && ! (Counter_GetValore(L_P1__GetSubcl53(my_id)) == 131u));
    res_AndLogicOP_57 = (res_AndLogicOP_57 && res_NotLogicOP_61);
    
    res_AndLogicOP_56 = (res_AndLogicOP_56 && res_AndLogicOP_57);
    res_AndLogicOP_56 = (res_AndLogicOP_56 && (argom25 == rossogiallo1));
    
    res_AndLogicOP_55 = (res_AndLogicOP_55 && res_AndLogicOP_56);
    bool res_NotLogicOP_62 = true;
    res_NotLogicOP_62 = (res_NotLogicOP_62 && ! Timer_Disattivo(L_P1__GetSubcl51(my_id)));
    res_AndLogicOP_55 = (res_AndLogicOP_55 && res_NotLogicOP_62);
    
    if(res_AndLogicOP_55){
    bool res_NotLogicOP_63 = true;
    res_NotLogicOP_63 = (res_NotLogicOP_63 && ! (L_P1__GetSubcl45(my_id) == avvio));
    res_ImpliesLogicOp_54 = (res_ImpliesLogicOp_54 && res_NotLogicOP_63);
    }
    res_ImpliesLogicOp_42 = (res_ImpliesLogicOp_42 && res_ImpliesLogicOp_54);
    }
    if(res_ImpliesLogicOp_42){
    xorIndex_res_XorLogicOP_41 = (xorIndex_res_XorLogicOP_41 + 1);
    }
    bool res_OrLogicOP_64 = false;
    bool res_OrLogicOP_65 = false;
    bool res_OrLogicOP_66 = false;
    bool res_AndLogicOP_67 = true;
    bool res_NotLogicOP_68 = true;
    res_NotLogicOP_68 = (res_NotLogicOP_68 && ! Timer_Disattivo(L_P1__GetSubcl51(my_id)));
    res_AndLogicOP_67 = (res_AndLogicOP_67 && res_NotLogicOP_68);
    bool res_NotLogicOP_69 = true;
    res_NotLogicOP_69 = (res_NotLogicOP_69 && ! (L_P1__GetSubcl45(my_id) == avvio));
    res_AndLogicOP_67 = (res_AndLogicOP_67 && res_NotLogicOP_69);
    
    res_OrLogicOP_66 = (res_OrLogicOP_66 || res_AndLogicOP_67);
    res_OrLogicOP_66 = (res_OrLogicOP_66 || (argom25 == rossogiallo1));
    
    res_OrLogicOP_65 = (res_OrLogicOP_65 || res_OrLogicOP_66);
    res_OrLogicOP_65 = (res_OrLogicOP_65 || (L_P1__GetSubcl44(my_id) == 7u));
    
    res_OrLogicOP_64 = (res_OrLogicOP_64 || res_OrLogicOP_65);
    bool res_AndLogicOP_70 = true;
    res_AndLogicOP_70 = (res_AndLogicOP_70 && (Counter_GetValore(L_P1__GetSubcl53(my_id)) > 1550u));
    bool res_NotLogicOP_71 = true;
    res_NotLogicOP_71 = (res_NotLogicOP_71 && ! (L_P1__GetSubcl45(my_id) == avvio));
    res_AndLogicOP_70 = (res_AndLogicOP_70 && res_NotLogicOP_71);
    
    res_OrLogicOP_64 = (res_OrLogicOP_64 || res_AndLogicOP_70);
    
    if(res_OrLogicOP_64){
    xorIndex_res_XorLogicOP_41 = (xorIndex_res_XorLogicOP_41 + 1);
    }
    
    res_XorLogicOP_41 = (res_XorLogicOP_41 && (xorIndex_res_XorLogicOP_41 == 1));
    res_ImpliesLogicOp_34 = (res_ImpliesLogicOp_34 && res_XorLogicOP_41);
    }
    if(res_ImpliesLogicOp_34){
    xorIndex_res_XorLogicOP_33 = (xorIndex_res_XorLogicOP_33 + 1);
    }
    bool res_OrLogicOP_72 = false;
    bool res_OrLogicOP_73 = false;
    bool res_AndLogicOP_74 = true;
    bool res_AndLogicOP_75 = true;
    bool res_NotLogicOP_76 = true;
    res_NotLogicOP_76 = (res_NotLogicOP_76 && ! (L_P1__GetParamSubcl13(my_id) == verde));
    res_AndLogicOP_75 = (res_AndLogicOP_75 && res_NotLogicOP_76);
    bool res_NotLogicOP_77 = true;
    bool res_NotLogicOP_78 = true;
    res_NotLogicOP_78 = (res_NotLogicOP_78 && ! (L_P1__GetInSubcl6(my_id) == verde));
    res_NotLogicOP_77 = (res_NotLogicOP_77 && ! res_NotLogicOP_78);
    res_AndLogicOP_75 = (res_AndLogicOP_75 && res_NotLogicOP_77);
    
    res_AndLogicOP_74 = (res_AndLogicOP_74 && res_AndLogicOP_75);
    res_AndLogicOP_74 = (res_AndLogicOP_74 && Timer_Disattivo(L_P1__GetSubcl50(my_id)));
    
    res_OrLogicOP_73 = (res_OrLogicOP_73 || res_AndLogicOP_74);
    bool res_NotLogicOP_79 = true;
    res_NotLogicOP_79 = (res_NotLogicOP_79 && ! (L_P1__GetSubcl42(my_id) == 10u));
    res_OrLogicOP_73 = (res_OrLogicOP_73 || res_NotLogicOP_79);
    
    res_OrLogicOP_72 = (res_OrLogicOP_72 || res_OrLogicOP_73);
    bool res_AndLogicOP_80 = true;
    bool res_NotLogicOP_81 = true;
    bool res_NotLogicOP_82 = true;
    res_NotLogicOP_82 = (res_NotLogicOP_82 && ! (L_P1__GetInSubcl5(my_id) == rossogiallo2));
    res_NotLogicOP_81 = (res_NotLogicOP_81 && ! res_NotLogicOP_82);
    res_AndLogicOP_80 = (res_AndLogicOP_80 && res_NotLogicOP_81);
    bool res_NotLogicOP_83 = true;
    res_NotLogicOP_83 = (res_NotLogicOP_83 && ! (argom27 == false));
    res_AndLogicOP_80 = (res_AndLogicOP_80 && res_NotLogicOP_83);
    
    res_OrLogicOP_72 = (res_OrLogicOP_72 || res_AndLogicOP_80);
    
    if(res_OrLogicOP_72){
    xorIndex_res_XorLogicOP_33 = (xorIndex_res_XorLogicOP_33 + 1);
    }
    
    res_XorLogicOP_33 = (res_XorLogicOP_33 && (xorIndex_res_XorLogicOP_33 == 1));
    res_ImpliesLogicOp_25 = (res_ImpliesLogicOp_25 && res_XorLogicOP_33);
    }
    if(res_ImpliesLogicOp_25){
    xorIndex_res_XorLogicOP_24 = (xorIndex_res_XorLogicOP_24 + 1);
    }
    bool res_AndLogicOP_84 = true;
    bool res_NotLogicOP_85 = true;
    res_NotLogicOP_85 = (res_NotLogicOP_85 && ! (argom28 == true));
    res_AndLogicOP_84 = (res_AndLogicOP_84 && res_NotLogicOP_85);
    res_AndLogicOP_84 = (res_AndLogicOP_84 && Timer_Attivo(L_P1__GetSubcl50(my_id)));
    
    if(res_AndLogicOP_84){
    xorIndex_res_XorLogicOP_24 = (xorIndex_res_XorLogicOP_24 + 1);
    }
    
    res_XorLogicOP_24 = (res_XorLogicOP_24 && (xorIndex_res_XorLogicOP_24 == 1));
    res_ImpliesLogicOp_22 = (res_ImpliesLogicOp_22 && res_XorLogicOP_24);
    }
    res_OrLogicOP_21 = (res_OrLogicOP_21 || res_ImpliesLogicOp_22);
    bool res_OrLogicOP_86 = false;
    bool res_AndLogicOP_87 = true;
    bool res_AndLogicOP_88 = true;
    bool res_AndLogicOP_89 = true;
    bool res_NotLogicOP_90 = true;
    res_NotLogicOP_90 = (res_NotLogicOP_90 && ! Timer_Disattivo(L_P1__GetSubcl50(my_id)));
    res_AndLogicOP_89 = (res_AndLogicOP_89 && res_NotLogicOP_90);
    res_AndLogicOP_89 = (res_AndLogicOP_89 && (L_P1__GetParamSubcl13(my_id) == verde));
    
    res_AndLogicOP_88 = (res_AndLogicOP_88 && res_AndLogicOP_89);
    bool res_NotLogicOP_91 = true;
    bool res_NotLogicOP_92 = true;
    res_NotLogicOP_92 = (res_NotLogicOP_92 && ! (L_P1__GetParamSubcl13(my_id) == verde));
    res_NotLogicOP_91 = (res_NotLogicOP_91 && ! res_NotLogicOP_92);
    res_AndLogicOP_88 = (res_AndLogicOP_88 && res_NotLogicOP_91);
    
    res_AndLogicOP_87 = (res_AndLogicOP_87 && res_AndLogicOP_88);
    bool res_NotLogicOP_93 = true;
    res_NotLogicOP_93 = (res_NotLogicOP_93 && ! Timer_Disattivo(L_P1__GetSubcl50(my_id)));
    res_AndLogicOP_87 = (res_AndLogicOP_87 && res_NotLogicOP_93);
    
    res_OrLogicOP_86 = (res_OrLogicOP_86 || res_AndLogicOP_87);
    bool res_NotLogicOP_94 = true;
    res_NotLogicOP_94 = (res_NotLogicOP_94 && ! (L_P1__GetSubcl45(my_id) == avvio));
    res_OrLogicOP_86 = (res_OrLogicOP_86 || res_NotLogicOP_94);
    
    res_OrLogicOP_21 = (res_OrLogicOP_21 || res_OrLogicOP_86);
    
    res_ImpliesLogicOp_9 = (res_ImpliesLogicOp_9 && res_OrLogicOP_21);
    }
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_ImpliesLogicOp_9);
    bool res_NotLogicOP_95 = true;
    res_NotLogicOP_95 = (res_NotLogicOP_95 && ! (argom27 == true));
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_NotLogicOP_95);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_OrLogicOP_8);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *50,51,52,*   l'argomento argomento_ave4 non  sia  uguale a  False  *,* 
    //   *104,* o  che   l'argomento argomento_ave4 sia  uguale a  True  *39,* 
    //   *104,* e  che  *,*  la variabile SubClass_C2_variabile_V2 sia  maggiore di  *54,* 6
    //   *104,* e  che  *,*  il contatore SubClass_C2_contatore_Co3 sia  uguale a  *53,* 13
    bool res_OrLogicOP_96 = false;
    bool res_NotLogicOP_97 = true;
    res_NotLogicOP_97 = (res_NotLogicOP_97 && ! (argom27 == false));
    res_OrLogicOP_96 = (res_OrLogicOP_96 || res_NotLogicOP_97);
    bool res_AndLogicOP_98 = true;
    bool res_AndLogicOP_99 = true;
    res_AndLogicOP_99 = (res_AndLogicOP_99 && (argom27 == true));
    res_AndLogicOP_99 = (res_AndLogicOP_99 && (L_P1__GetSubcl42(my_id) > 6u));
    
    res_AndLogicOP_98 = (res_AndLogicOP_98 && res_AndLogicOP_99);
    res_AndLogicOP_98 = (res_AndLogicOP_98 && (Counter_GetValore(L_P1__GetSubcl52(my_id)) == 13u));
    
    res_OrLogicOP_96 = (res_OrLogicOP_96 || res_AndLogicOP_98);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_96);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
     
    { commento: {63,}  se la macro  SubClass_C2_macrova_M1 ( con argomento_a2   uguale a avvio ,argomento_a8   uguale a RossoGiallo ,argomento_a6   uguale a Giallox ,argomento_a9   uguale a avvio ,argomento_a1   uguale a RossoGialloGiallo ,argomento_a5   uguale a GialloVerde  e argomento_a10   uguale a RossoGiallo )   è  diverso da avvio commento: {40,}  commento: {35,} o  se il controllo SubClass_C2_controllo_C3 è  diverso da Verde commento: {35,} e  se il controllo SubClass_C2_controllo_C10 non è  diverso da RossoGiallo, Solo una delle seguenti { 
     commento: {62,} commento: {34,}  se il parametro SubClass_C2_parametro_P2 è  uguale a Verde, Almeno una delle seguenti { 
     commento: {63,} commento: {38,}  se il contatore SubClass_C2_contatore_Co4 non è  diverso da  commento: {56,} 1121 commento: {37,} e  se la variabile SubClass_C2_variabile_V5 è  diverso da RossoGiallo, Solo una delle seguenti { 
     commento: {41,}  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  commento: {105,} è  uguale a c270x o  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro SubClass_C2_parametro_P4 non è  uguale a RossoGialloxVerdex commento: {37,} o  se la variabile SubClass_C2_variabile_V8 è  diverso da avvio commento: {34,} e  se il parametro SubClass_C2_parametro_P4 non è  uguale a RossoGialloxVerdex, Verifica che   commento: {47,48,50,}  commento: {34,}  il parametro SubClass_C2_parametro_P2 sia  diverso da Verde
     commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} e  che  commento: {,}  la variabile SubClass_C2_variabile_V5 non sia  uguale a RossoGiallo
    
    
     } Verifica che   commento: {48,49,50,51,}   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} o  che  commento: {,}  il controllo SubClass_C2_controllo_C10 sia  diverso da RossoGiallo
     commento: {104,} e  che  commento: {,}  il contatore SubClass_C2_contatore_Co4 non sia  uguale a  commento: {53,} 1232
     commento: {104,} e  che  commento: {38,}  il contatore SubClass_C2_contatore_Co3 sia  diverso da  commento: {56,} 12
     commento: {104,} o  che  commento: {,}  la variabile SubClass_C2_variabile_V7 sia  uguale a  commento: {53,} 3
     commento: {104,} e  che  commento: {,}  il timer SubClass_C2_timer_T3 sia scaduto
    
    
     } Verifica che   commento: {49,50,}  commento: {,}  il timer SubClass_C2_timer_T3 non sia disattivo
     commento: {104,} o  che  commento: {,}  la variabile SubClass_C2_variabile_V5 sia  uguale a RossoGiallo
    
    
     } Verifica che   commento: {47,48,49,50,}  commento: {,}  la variabile SubClass_C2_variabile_V8 sia  diverso da avvio
     commento: {104,} e  che  commento: {,}  il timer SubClass_C2_timer_T10 sia disattivo
     commento: {104,} e  che  commento: {37,}  la variabile SubClass_C2_variabile_V8 non sia  diverso da avvio
     commento: {104,} o  che  commento: {34,}  il parametro SubClass_C2_parametro_P2 non sia  uguale a Verde
     commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
    
    
    }
*/
bool L_P1__Macro13(instance_id_t const my_id )
{
bool res_AndLogicOP_0 = true;
    
    //  *63,*  se la macro  SubClass_C2_macrova_M1 ( con argomento_a2   uguale a avvio ,argomento_a8   uguale a RossoGiallo ,argomento_a6   uguale a Giallox ,argomento_a9   uguale a avvio ,argomento_a1   uguale a RossoGialloGiallo ,argomento_a5   uguale a GialloVerde  e argomento_a10   uguale a RossoGiallo )   è  diverso da avvio *40,*  *35,* o  se il controllo SubClass_C2_controllo_C3 è  diverso da Verde *35,* e  se il controllo SubClass_C2_controllo_C10 non è  diverso da RossoGiallo, Solo una delle seguenti { 
    //   *62,* *34,*  se il parametro SubClass_C2_parametro_P2 è  uguale a Verde, Almeno una delle seguenti { 
    //   *63,* *38,*  se il contatore SubClass_C2_contatore_Co4 non è  diverso da  *56,* 1121 *37,* e  se la variabile SubClass_C2_variabile_V5 è  diverso da RossoGiallo, Solo una delle seguenti { 
    //   *41,*  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  *105,* è  uguale a c270x o  se il controllo ConsDef  è  uguale a FALSE  *34,* e  se il parametro SubClass_C2_parametro_P4 non è  uguale a RossoGialloxVerdex *37,* o  se la variabile SubClass_C2_variabile_V8 è  diverso da avvio *34,* e  se il parametro SubClass_C2_parametro_P4 non è  uguale a RossoGialloxVerdex, Verifica che   *47,48,50,*  *34,*  il parametro SubClass_C2_parametro_P2 sia  diverso da Verde
    //   *104,* o  che   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* e  che  *,*  la variabile SubClass_C2_variabile_V5 non sia  uguale a RossoGiallo
    //   } Verifica che   *48,49,50,51,*   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* o  che  *,*  il controllo SubClass_C2_controllo_C10 sia  diverso da RossoGiallo
    //   *104,* e  che  *,*  il contatore SubClass_C2_contatore_Co4 non sia  uguale a  *53,* 1232
    //   *104,* e  che  *38,*  il contatore SubClass_C2_contatore_Co3 sia  diverso da  *56,* 12
    //   *104,* o  che  *,*  la variabile SubClass_C2_variabile_V7 sia  uguale a  *53,* 3
    //   *104,* e  che  *,*  il timer SubClass_C2_timer_T3 sia scaduto
    //   } Verifica che   *49,50,*  *,*  il timer SubClass_C2_timer_T3 non sia disattivo
    //   *104,* o  che  *,*  la variabile SubClass_C2_variabile_V5 sia  uguale a RossoGiallo
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__Macro8(my_id,rossogiallo3,rossogiallo2,avvio,gialloverde,giallox,rossogiallo2,avvio) == avvio));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_3);
    bool res_AndLogicOP_4 = true;
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetInSubcl6(my_id) == verde));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_5);
    bool res_NotLogicOP_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetInSubcl5(my_id) == rossogiallo2));
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! res_NotLogicOP_7);
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_6);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_4);
    
    if(res_OrLogicOP_2){
    bool res_XorLogicOP_8 = true;
    int xorIndex_res_XorLogicOP_8 = 0;
    bool res_ImpliesLogicOp_9 = true;
    if((L_P1__GetParamSubcl13(my_id) == verde)){
    bool res_OrLogicOP_10 = false;
    bool res_ImpliesLogicOp_11 = true;
    bool res_AndLogicOP_12 = true;
    bool res_NotLogicOP_13 = true;
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (Counter_GetValore(L_P1__GetSubcl53(my_id)) == 1121u));
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! res_NotLogicOP_14);
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_NotLogicOP_13);
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (L_P1__GetSubcl43(my_id) == rossogiallo2));
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_NotLogicOP_15);
    
    if(res_AndLogicOP_12){
    bool res_ImpliesLogicOp_16 = true;
    bool res_OrLogicOP_17 = false;
    bool res_OrLogicOP_18 = false;
    bool res_ForAllPredicateNotEmpty_19 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl9Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl9(my_id,i);
    bool res_ImpliesLogicOp_20 = true;
    res_ImpliesLogicOp_20 = (res_ImpliesLogicOp_20 && (L_P1__GetParamMainc5(it.mainc36) == c270x));
    res_ForAllPredicateNotEmpty_19 = res_ImpliesLogicOp_20;
    if(!res_ForAllPredicateNotEmpty_19) {break;}
    }
    res_OrLogicOP_18 = (res_OrLogicOP_18 || res_ForAllPredicateNotEmpty_19);
    bool res_AndLogicOP_21 = true;
    res_AndLogicOP_21 = (res_AndLogicOP_21 && (L_P1__GetInConsd1(my_id) == false));
    bool res_NotLogicOP_22 = true;
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! (L_P1__GetParamSubcl14(my_id) == rossogiallo1));
    res_AndLogicOP_21 = (res_AndLogicOP_21 && res_NotLogicOP_22);
    
    res_OrLogicOP_18 = (res_OrLogicOP_18 || res_AndLogicOP_21);
    
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_OrLogicOP_18);
    bool res_AndLogicOP_23 = true;
    bool res_NotLogicOP_24 = true;
    res_NotLogicOP_24 = (res_NotLogicOP_24 && ! (L_P1__GetSubcl45(my_id) == avvio));
    res_AndLogicOP_23 = (res_AndLogicOP_23 && res_NotLogicOP_24);
    bool res_NotLogicOP_25 = true;
    res_NotLogicOP_25 = (res_NotLogicOP_25 && ! (L_P1__GetParamSubcl14(my_id) == rossogiallo1));
    res_AndLogicOP_23 = (res_AndLogicOP_23 && res_NotLogicOP_25);
    
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_AndLogicOP_23);
    
    if(res_OrLogicOP_17){
    bool res_OrLogicOP_26 = false;
    bool res_NotLogicOP_27 = true;
    res_NotLogicOP_27 = (res_NotLogicOP_27 && ! (L_P1__GetParamSubcl13(my_id) == verde));
    res_OrLogicOP_26 = (res_OrLogicOP_26 || res_NotLogicOP_27);
    bool res_AndLogicOP_28 = true;
    res_AndLogicOP_28 = (res_AndLogicOP_28 && (L_P1__GetInConsd1(my_id) == false));
    bool res_NotLogicOP_29 = true;
    res_NotLogicOP_29 = (res_NotLogicOP_29 && ! (L_P1__GetSubcl43(my_id) == rossogiallo2));
    res_AndLogicOP_28 = (res_AndLogicOP_28 && res_NotLogicOP_29);
    
    res_OrLogicOP_26 = (res_OrLogicOP_26 || res_AndLogicOP_28);
    
    res_ImpliesLogicOp_16 = (res_ImpliesLogicOp_16 && res_OrLogicOP_26);
    }
    res_ImpliesLogicOp_11 = (res_ImpliesLogicOp_11 && res_ImpliesLogicOp_16);
    }
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_ImpliesLogicOp_11);
    bool res_OrLogicOP_30 = false;
    bool res_OrLogicOP_31 = false;
    res_OrLogicOP_31 = (res_OrLogicOP_31 || (L_P1__GetInConsd1(my_id) == false));
    bool res_AndLogicOP_32 = true;
    bool res_AndLogicOP_33 = true;
    bool res_NotLogicOP_34 = true;
    res_NotLogicOP_34 = (res_NotLogicOP_34 && ! (L_P1__GetInSubcl5(my_id) == rossogiallo2));
    res_AndLogicOP_33 = (res_AndLogicOP_33 && res_NotLogicOP_34);
    bool res_NotLogicOP_35 = true;
    res_NotLogicOP_35 = (res_NotLogicOP_35 && ! (Counter_GetValore(L_P1__GetSubcl53(my_id)) == 1232u));
    res_AndLogicOP_33 = (res_AndLogicOP_33 && res_NotLogicOP_35);
    
    res_AndLogicOP_32 = (res_AndLogicOP_32 && res_AndLogicOP_33);
    bool res_NotLogicOP_36 = true;
    res_NotLogicOP_36 = (res_NotLogicOP_36 && ! (Counter_GetValore(L_P1__GetSubcl52(my_id)) == 12u));
    res_AndLogicOP_32 = (res_AndLogicOP_32 && res_NotLogicOP_36);
    
    res_OrLogicOP_31 = (res_OrLogicOP_31 || res_AndLogicOP_32);
    
    res_OrLogicOP_30 = (res_OrLogicOP_30 || res_OrLogicOP_31);
    bool res_AndLogicOP_37 = true;
    res_AndLogicOP_37 = (res_AndLogicOP_37 && (L_P1__GetSubcl44(my_id) == 3u));
    res_AndLogicOP_37 = (res_AndLogicOP_37 && Timer_Scaduto(L_P1__GetSubcl51(my_id)));
    
    res_OrLogicOP_30 = (res_OrLogicOP_30 || res_AndLogicOP_37);
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_OrLogicOP_30);
    
    res_ImpliesLogicOp_9 = (res_ImpliesLogicOp_9 && res_OrLogicOP_10);
    }
    if(res_ImpliesLogicOp_9){
    xorIndex_res_XorLogicOP_8 = (xorIndex_res_XorLogicOP_8 + 1);
    }
    bool res_OrLogicOP_38 = false;
    bool res_NotLogicOP_39 = true;
    res_NotLogicOP_39 = (res_NotLogicOP_39 && ! Timer_Disattivo(L_P1__GetSubcl51(my_id)));
    res_OrLogicOP_38 = (res_OrLogicOP_38 || res_NotLogicOP_39);
    res_OrLogicOP_38 = (res_OrLogicOP_38 || (L_P1__GetSubcl43(my_id) == rossogiallo2));
    
    if(res_OrLogicOP_38){
    xorIndex_res_XorLogicOP_8 = (xorIndex_res_XorLogicOP_8 + 1);
    }
    
    res_XorLogicOP_8 = (res_XorLogicOP_8 && (xorIndex_res_XorLogicOP_8 == 1));
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_XorLogicOP_8);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *47,48,49,50,*  *,*  la variabile SubClass_C2_variabile_V8 sia  diverso da avvio
    //   *104,* e  che  *,*  il timer SubClass_C2_timer_T10 sia disattivo
    //   *104,* e  che  *37,*  la variabile SubClass_C2_variabile_V8 non sia  diverso da avvio
    //   *104,* o  che  *34,*  il parametro SubClass_C2_parametro_P2 non sia  uguale a Verde
    //   *104,* o  che   il controllo ConsDef  sia  uguale a FALSE
    bool res_OrLogicOP_40 = false;
    bool res_OrLogicOP_41 = false;
    bool res_AndLogicOP_42 = true;
    bool res_AndLogicOP_43 = true;
    bool res_NotLogicOP_44 = true;
    res_NotLogicOP_44 = (res_NotLogicOP_44 && ! (L_P1__GetSubcl45(my_id) == avvio));
    res_AndLogicOP_43 = (res_AndLogicOP_43 && res_NotLogicOP_44);
    res_AndLogicOP_43 = (res_AndLogicOP_43 && Timer_Disattivo(L_P1__GetSubcl50(my_id)));
    
    res_AndLogicOP_42 = (res_AndLogicOP_42 && res_AndLogicOP_43);
    bool res_NotLogicOP_45 = true;
    bool res_NotLogicOP_46 = true;
    res_NotLogicOP_46 = (res_NotLogicOP_46 && ! (L_P1__GetSubcl45(my_id) == avvio));
    res_NotLogicOP_45 = (res_NotLogicOP_45 && ! res_NotLogicOP_46);
    res_AndLogicOP_42 = (res_AndLogicOP_42 && res_NotLogicOP_45);
    
    res_OrLogicOP_41 = (res_OrLogicOP_41 || res_AndLogicOP_42);
    bool res_NotLogicOP_47 = true;
    res_NotLogicOP_47 = (res_NotLogicOP_47 && ! (L_P1__GetParamSubcl13(my_id) == verde));
    res_OrLogicOP_41 = (res_OrLogicOP_41 || res_NotLogicOP_47);
    
    res_OrLogicOP_40 = (res_OrLogicOP_40 || res_OrLogicOP_41);
    res_OrLogicOP_40 = (res_OrLogicOP_40 || (L_P1__GetInConsd1(my_id) == false));
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_40);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
    
    { commento: {63,} commento: {38,}  se il contatore SubClass_C2_contatore_Co3 è  minore di  commento: {55,} 1150 o  se l'argomento argomento_ave2 non  è  diverso da  False  commento: {39,} , Solo una delle seguenti { 
     commento: {62,} commento: {43,}  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  commento: {105,} è disattivo commento: {38,} o  se il contatore SubClass_C2_contatore_Co4 non è  minore di  commento: {55,} 1243 commento: {35,} o  se il controllo SubClass_C2_controllo_C3 è  uguale a Verde commento: {34,} o  se il parametro SubClass_C2_parametro_P4 è  diverso da RossoGialloxVerdex commento: {36,} e  se il timer SubClass_C2_timer_T3 è disattivo, Almeno una delle seguenti { 
     commento: {38,}  se il contatore SubClass_C2_contatore_Co4 è  minore di  commento: {55,} 13215 commento: {38,} e  se il contatore SubClass_C2_contatore_Co4 è  uguale a  commento: {53,} 1504 commento: {37,} e  se la variabile SubClass_C2_variabile_V2 è  maggiore di  commento: {54,} 6, Verifica che   commento: {47,48,}  commento: {,}  il controllo SubClass_C2_controllo_C3 non sia  uguale a Verde
     commento: {104,} e  che  commento: {34,}  il parametro SubClass_C2_parametro_P1 sia  uguale a RossoGialloxVerdex
    
    
     } Verifica che   commento: {47,49,50,52,}  commento: {,}  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio
     commento: {104,} e  che   l'argomento argomento_ave10 non  sia  uguale a  False  commento: {,} 
     commento: {104,} o  che  commento: {37,}  la variabile SubClass_C2_variabile_V8 sia  diverso da avvio
     commento: {104,} o  che   l'argomento argomento_ave4 sia  uguale a  False  commento: {39,} 
     commento: {104,} o  che  commento: {34,}  il parametro SubClass_C2_parametro_P2 non sia  uguale a Verde
     commento: {104,} o  che  commento: {,}  il timer SubClass_C2_timer_T10 non sia scaduto
    
    
     } Verifica che   commento: {47,49,50,51,52,}  commento: {,}  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio
     commento: {104,} e  che  commento: {,}  il contatore SubClass_C2_contatore_Co4 non sia  diverso da  commento: {56,} 12
     commento: {104,} o  che  commento: {34,}  il parametro SubClass_C2_parametro_P10 sia  uguale a  True 
     commento: {104,} e  che  commento: {38,}  il contatore SubClass_C2_contatore_Co4 non sia  diverso da  commento: {56,} 13
     commento: {104,} o  che  commento: {,}  il timer SubClass_C2_timer_T3 non sia attivo
     commento: {104,} o  che   l'argomento argomento_ave7 non  sia  uguale a  True  commento: {,} 
    
    
    }
*/
bool L_P1__Macro14(instance_id_t const my_id , bool argom30, bool argom31, C2_Enumerat3 argom32, bool argom33, bool argom34, C2_Enumerat4 argom35)
{
bool res_AndLogicOP_0 = true;
    
    //  *63,* *38,*  se il contatore SubClass_C2_contatore_Co3 è  minore di  *55,* 1150 o  se l'argomento argomento_ave2 non  è  diverso da  False  *39,* , Solo una delle seguenti { 
    //   *62,* *43,*  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  *105,* è disattivo *38,* o  se il contatore SubClass_C2_contatore_Co4 non è  minore di  *55,* 1243 *35,* o  se il controllo SubClass_C2_controllo_C3 è  uguale a Verde *34,* o  se il parametro SubClass_C2_parametro_P4 è  diverso da RossoGialloxVerdex *36,* e  se il timer SubClass_C2_timer_T3 è disattivo, Almeno una delle seguenti { 
    //   *38,*  se il contatore SubClass_C2_contatore_Co4 è  minore di  *55,* 13215 *38,* e  se il contatore SubClass_C2_contatore_Co4 è  uguale a  *53,* 1504 *37,* e  se la variabile SubClass_C2_variabile_V2 è  maggiore di  *54,* 6, Verifica che   *47,48,*  *,*  il controllo SubClass_C2_controllo_C3 non sia  uguale a Verde
    //   *104,* e  che  *34,*  il parametro SubClass_C2_parametro_P1 sia  uguale a RossoGialloxVerdex
    //   } Verifica che   *47,49,50,52,*  *,*  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio
    //   *104,* e  che   l'argomento argomento_ave10 non  sia  uguale a  False  *,* 
    //   *104,* o  che  *37,*  la variabile SubClass_C2_variabile_V8 sia  diverso da avvio
    //   *104,* o  che   l'argomento argomento_ave4 sia  uguale a  False  *39,* 
    //   *104,* o  che  *34,*  il parametro SubClass_C2_parametro_P2 non sia  uguale a Verde
    //   *104,* o  che  *,*  il timer SubClass_C2_timer_T10 non sia scaduto
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    res_OrLogicOP_2 = (res_OrLogicOP_2 || (Counter_GetValore(L_P1__GetSubcl52(my_id)) < 1150u));
    bool res_NotLogicOP_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (argom31 == false));
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! res_NotLogicOP_4);
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_3);
    
    if(res_OrLogicOP_2){
    bool res_XorLogicOP_5 = true;
    int xorIndex_res_XorLogicOP_5 = 0;
    bool res_ImpliesLogicOp_6 = true;
    bool res_OrLogicOP_7 = false;
    bool res_OrLogicOP_8 = false;
    bool res_OrLogicOP_9 = false;
    bool res_ForAllPredicateNotEmpty_10 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl9Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl9(my_id,i);
    bool res_ImpliesLogicOp_11 = true;
    res_ImpliesLogicOp_11 = (res_ImpliesLogicOp_11 && Timer_Disattivo(L_P1__GetMainc32(it.mainc36)));
    res_ForAllPredicateNotEmpty_10 = res_ImpliesLogicOp_11;
    if(!res_ForAllPredicateNotEmpty_10) {break;}
    }
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_ForAllPredicateNotEmpty_10);
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (Counter_GetValore(L_P1__GetSubcl53(my_id)) < 1243u));
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_NotLogicOP_12);
    
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_OrLogicOP_9);
    res_OrLogicOP_8 = (res_OrLogicOP_8 || (L_P1__GetInSubcl6(my_id) == verde));
    
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_OrLogicOP_8);
    bool res_AndLogicOP_13 = true;
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1__GetParamSubcl14(my_id) == rossogiallo1));
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_NotLogicOP_14);
    res_AndLogicOP_13 = (res_AndLogicOP_13 && Timer_Disattivo(L_P1__GetSubcl51(my_id)));
    
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_AndLogicOP_13);
    
    if(res_OrLogicOP_7){
    bool res_ImpliesLogicOp_15 = true;
    bool res_AndLogicOP_16 = true;
    bool res_AndLogicOP_17 = true;
    res_AndLogicOP_17 = (res_AndLogicOP_17 && (Counter_GetValore(L_P1__GetSubcl53(my_id)) < 13215u));
    res_AndLogicOP_17 = (res_AndLogicOP_17 && (Counter_GetValore(L_P1__GetSubcl53(my_id)) == 1504u));
    
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_AndLogicOP_17);
    res_AndLogicOP_16 = (res_AndLogicOP_16 && (L_P1__GetSubcl42(my_id) > 6u));
    
    if(res_AndLogicOP_16){
    bool res_AndLogicOP_18 = true;
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (L_P1__GetInSubcl6(my_id) == verde));
    res_AndLogicOP_18 = (res_AndLogicOP_18 && res_NotLogicOP_19);
    res_AndLogicOP_18 = (res_AndLogicOP_18 && (L_P1__GetParamSubcl11(my_id) == rossogiallo1));
    
    res_ImpliesLogicOp_15 = (res_ImpliesLogicOp_15 && res_AndLogicOP_18);
    }
    res_ImpliesLogicOp_6 = (res_ImpliesLogicOp_6 && res_ImpliesLogicOp_15);
    }
    if(res_ImpliesLogicOp_6){
    xorIndex_res_XorLogicOP_5 = (xorIndex_res_XorLogicOP_5 + 1);
    }
    bool res_OrLogicOP_20 = false;
    bool res_OrLogicOP_21 = false;
    bool res_OrLogicOP_22 = false;
    bool res_OrLogicOP_23 = false;
    bool res_AndLogicOP_24 = true;
    bool res_NotLogicOP_25 = true;
    res_NotLogicOP_25 = (res_NotLogicOP_25 && ! (L_P1__GetSubcl45(my_id) == avvio));
    res_AndLogicOP_24 = (res_AndLogicOP_24 && res_NotLogicOP_25);
    bool res_NotLogicOP_26 = true;
    res_NotLogicOP_26 = (res_NotLogicOP_26 && ! (argom30 == false));
    res_AndLogicOP_24 = (res_AndLogicOP_24 && res_NotLogicOP_26);
    
    res_OrLogicOP_23 = (res_OrLogicOP_23 || res_AndLogicOP_24);
    bool res_NotLogicOP_27 = true;
    res_NotLogicOP_27 = (res_NotLogicOP_27 && ! (L_P1__GetSubcl45(my_id) == avvio));
    res_OrLogicOP_23 = (res_OrLogicOP_23 || res_NotLogicOP_27);
    
    res_OrLogicOP_22 = (res_OrLogicOP_22 || res_OrLogicOP_23);
    res_OrLogicOP_22 = (res_OrLogicOP_22 || (argom33 == false));
    
    res_OrLogicOP_21 = (res_OrLogicOP_21 || res_OrLogicOP_22);
    bool res_NotLogicOP_28 = true;
    res_NotLogicOP_28 = (res_NotLogicOP_28 && ! (L_P1__GetParamSubcl13(my_id) == verde));
    res_OrLogicOP_21 = (res_OrLogicOP_21 || res_NotLogicOP_28);
    
    res_OrLogicOP_20 = (res_OrLogicOP_20 || res_OrLogicOP_21);
    bool res_NotLogicOP_29 = true;
    res_NotLogicOP_29 = (res_NotLogicOP_29 && ! Timer_Scaduto(L_P1__GetSubcl50(my_id)));
    res_OrLogicOP_20 = (res_OrLogicOP_20 || res_NotLogicOP_29);
    
    if(res_OrLogicOP_20){
    xorIndex_res_XorLogicOP_5 = (xorIndex_res_XorLogicOP_5 + 1);
    }
    
    res_XorLogicOP_5 = (res_XorLogicOP_5 && (xorIndex_res_XorLogicOP_5 == 1));
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_XorLogicOP_5);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *47,49,50,51,52,*  *,*  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio
    //   *104,* e  che  *,*  il contatore SubClass_C2_contatore_Co4 non sia  diverso da  *56,* 12
    //   *104,* o  che  *34,*  il parametro SubClass_C2_parametro_P10 sia  uguale a  True 
    //   *104,* e  che  *38,*  il contatore SubClass_C2_contatore_Co4 non sia  diverso da  *56,* 13
    //   *104,* o  che  *,*  il timer SubClass_C2_timer_T3 non sia attivo
    //   *104,* o  che   l'argomento argomento_ave7 non  sia  uguale a  True
    bool res_OrLogicOP_30 = false;
    bool res_OrLogicOP_31 = false;
    bool res_OrLogicOP_32 = false;
    bool res_AndLogicOP_33 = true;
    bool res_NotLogicOP_34 = true;
    res_NotLogicOP_34 = (res_NotLogicOP_34 && ! (L_P1__GetSubcl45(my_id) == avvio));
    res_AndLogicOP_33 = (res_AndLogicOP_33 && res_NotLogicOP_34);
    bool res_NotLogicOP_35 = true;
    bool res_NotLogicOP_36 = true;
    res_NotLogicOP_36 = (res_NotLogicOP_36 && ! (Counter_GetValore(L_P1__GetSubcl53(my_id)) == 12u));
    res_NotLogicOP_35 = (res_NotLogicOP_35 && ! res_NotLogicOP_36);
    res_AndLogicOP_33 = (res_AndLogicOP_33 && res_NotLogicOP_35);
    
    res_OrLogicOP_32 = (res_OrLogicOP_32 || res_AndLogicOP_33);
    bool res_AndLogicOP_37 = true;
    res_AndLogicOP_37 = (res_AndLogicOP_37 && (L_P1__GetParamSubcl12(my_id) == true));
    bool res_NotLogicOP_38 = true;
    bool res_NotLogicOP_39 = true;
    res_NotLogicOP_39 = (res_NotLogicOP_39 && ! (Counter_GetValore(L_P1__GetSubcl53(my_id)) == 13u));
    res_NotLogicOP_38 = (res_NotLogicOP_38 && ! res_NotLogicOP_39);
    res_AndLogicOP_37 = (res_AndLogicOP_37 && res_NotLogicOP_38);
    
    res_OrLogicOP_32 = (res_OrLogicOP_32 || res_AndLogicOP_37);
    
    res_OrLogicOP_31 = (res_OrLogicOP_31 || res_OrLogicOP_32);
    bool res_NotLogicOP_40 = true;
    res_NotLogicOP_40 = (res_NotLogicOP_40 && ! Timer_Attivo(L_P1__GetSubcl51(my_id)));
    res_OrLogicOP_31 = (res_OrLogicOP_31 || res_NotLogicOP_40);
    
    res_OrLogicOP_30 = (res_OrLogicOP_30 || res_OrLogicOP_31);
    bool res_NotLogicOP_41 = true;
    res_NotLogicOP_41 = (res_NotLogicOP_41 && ! (argom34 == true));
    res_OrLogicOP_30 = (res_OrLogicOP_30 || res_NotLogicOP_41);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_30);
    
    
    
    return res_AndLogicOP_0;
}


// Macro valorizzate

/*
    CNL corrispondente:
    
    { commento: {[}  se l'argomento argomento_a8 non  è  uguale a RossoGiallo commento: {39,}  , assegna alla macro il valore avvio
    
     commento: {46,} assegna alla macro il valore avvio commento: {],}
    }
*/
C2_Enumerat2 L_P1__Macro8(instance_id_t const my_id , C2_Enumerat4 argom9, C2_Enumerat3 argom10, C2_Enumerat2 argom11, C2_Enumerat3 argom12, C2_Enumerat2 argom13, C2_Enumerat3 argom14, C2_Enumerat2 argom15)
{
C2_Enumerat2 res_macro_val;
    
    //  l'argomento argomento_a8 non  è  uguale a RossoGiallo
    bool res_NotLogicOP_0 = true;
    res_NotLogicOP_0 = (res_NotLogicOP_0 && ! (argom14 == rossogiallo2));
    if(res_NotLogicOP_0){
    
    res_macro_val = avvio;
    }
    else{
    res_macro_val = avvio;
    }
    return res_macro_val;
}

/*
    CNL corrispondente:
    
    { commento: {[}
     commento: {46,} assegna alla macro il valore Verde commento: {],}
    }
*/
C2_Enumerat4 L_P1__Macro9(instance_id_t const my_id , C2_Enumerat1 argom16, C2_Enumerat4 argom17, C2_Enumerat3 argom18, C2_Enumerat4 argom19, C2_Enumerat4 argom20, C2_Enumerat4 argom21, C2_Enumerat3 argom22)
{
return verde;
}



