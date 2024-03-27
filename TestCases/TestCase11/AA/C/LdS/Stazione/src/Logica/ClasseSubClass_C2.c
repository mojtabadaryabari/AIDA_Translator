// Codice del modello 'TestCase11', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#include "Logica/ClasseMainClass_C1.h"
#include "Logica/ClasseSubClass_C2.h"
#include "Logica/ClasseSubClass_C3.h"
#include "Logica/ClasseSubClass_C4.h"
#include "Logica/ClasseSubClass_C2_priv.h"
#include "config.h"
#include "scheduler.h"


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
    L_P1__SetSubcl17(my_id, false);
    L_P1__SetSubcl19(my_id, false);
    L_P1__SetSubcl21(my_id, spento);
    L_P1__SetSubcl22(my_id, spento);
    L_P1__SetSubcl23(my_id, false);
    L_P1__SetSubcl24(my_id, false);
    L_P1__SetSubcl25(my_id, avvio);
    L_P1__SetSubcl26(my_id, avvio);
    L_P1__SetSubcl27(my_id, false);
    L_P1__SetSubcl28(my_id, 0);
    // init controlli precedenti
    L_P1__SetSubcl14(my_id, c120);
    L_P1__SetSubcl16(my_id, false);
    // init Timer e Counter
    Timer_AggmInit(L_P1__GetSubcl29(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl29_ID);
    Timer_Init(L_P1__GetSubcl29(my_id), 1000);
    Timer_AggmInit(L_P1__GetSubcl30(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl30_ID);
    Timer_Init(L_P1__GetSubcl30(my_id), 1000);
    Timer_AggmInit(L_P1__GetSubcl31(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl31_ID);
    Timer_Init(L_P1__GetSubcl31(my_id), 34000);
    Timer_AggmInit(L_P1__GetSubcl32(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl32_ID);
    Timer_Init(L_P1__GetSubcl32(my_id), 34000);
    Timer_AggmInit(L_P1__GetSubcl33(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl33_ID);
    Timer_Init(L_P1__GetSubcl33(my_id), 3000);
    Timer_AggmInit(L_P1__GetSubcl34(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl34_ID);
    Timer_Init(L_P1__GetSubcl34(my_id), 3000);
    Timer_AggmInit(L_P1__GetSubcl35(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl35_ID);
    Timer_Init(L_P1__GetSubcl35(my_id), 1213000);
    Timer_AggmInit(L_P1__GetSubcl36(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl36_ID);
    Timer_Init(L_P1__GetSubcl36(my_id), 3000);
    Timer_AggmInit(L_P1__GetSubcl37(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl37_ID);
    Timer_Init(L_P1__GetSubcl37(my_id), 3000);
    Timer_AggmInit(L_P1__GetSubcl38(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl38_ID);
    Timer_Init(L_P1__GetSubcl38(my_id), 5000);
    Timer_AggmInit(L_P1__GetSubcl39(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl39_ID);
    Timer_Init(L_P1__GetSubcl39(my_id), 1450000);
    Counter_AggmInit(L_P1__GetSubcl40(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl40_ID);
    Counter_Init(L_P1__GetSubcl40(my_id));
    Counter_AggmInit(L_P1__GetSubcl41(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl41_ID);
    Counter_Init(L_P1__GetSubcl41(my_id));
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
    L_P1__SetSubcl18(my_id, L_P1__GetSubcl17(my_id));
    L_P1__SetSubcl20(my_id, L_P1__GetSubcl19(my_id));
}

void L_P1_C2_Exec(instance_id_t const my_id, Phase const p)
{
    L_P1_C2_SetResponse(my_id, LDS_SCHED_NOP);
    switch (p) {

    case LDS_PHASE_MANUAL:
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
    Timer_Exec(L_P1__GetSubcl29(my_id));
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
}

void L_P1_C2_GSetSafe(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C2(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C2(proc_id);
    L_P1__SetOutSubcl(my_id, giallogiall);
    L_P1__SetOutSubcl1(my_id, false);
    L_P1__SetOutSubcl2(my_id, false);
    L_P1__SetOutSubcl3(my_id, true);
}

void L_P1_C2_GUpdatePrev(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C2(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C2(proc_id);
    L_P1__SetSubcl14(my_id, L_P1__GetInSubcl13(my_id));
    L_P1__SetSubcl16(my_id, L_P1__GetInSubcl15(my_id));
    L_P1__SetSubcl18(my_id, L_P1__GetSubcl17(my_id));
    L_P1__SetSubcl20(my_id, L_P1__GetSubcl19(my_id));
}

// ********** Definizione macro **********

// Macro di effetto

/*
    CNL corrispondente:
    
    { commento: {109,}  se il ripristino della variabile  SubClass_C2_restoreva_RV3 non è  diverso da Rosso commento: {38,} e  se il contatore SubClass_C2_contatore_Co5 non è  maggiore di  commento: {54,} 155021 commento: {38,} e  se il contatore SubClass_C2_contatore_Co5 è  maggiore di  commento: {54,} 1134, commento: {69,}Disattiva il timer SubClass_C2_timer_T8
    
       
     commento: {34,}  se lo stato  è  diverso da  commento: {56,}  state1  commento: {106,}, commento: {68,}Attiva il timer SubClass_C2_timer_T8
    
     ,altrimenti  commento: {66,} Assegna al comando SubClass_C2_comando_C8 il valore  False 
    
    
     commento: {36,}  se il timer SubClass_C2_timer_T8 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} o  se il timer SubClass_C2_timer_T2 non è attivo commento: {37,} e  se la variabile SubClass_C2_variabile_V9 non è  diverso da  commento: {56,} 8, commento: {66,} Assegna al comando SubClass_C2_comando_C2 il valore  True 
    
       
    
    }
*/
void L_P1__Macro10(instance_id_t const my_id )
{
//  *109,*  se il ripristino della variabile  SubClass_C2_restoreva_RV3 non è  diverso da Rosso *38,* e  se il contatore SubClass_C2_contatore_Co5 non è  maggiore di  *54,* 155021 *38,* e  se il contatore SubClass_C2_contatore_Co5 è  maggiore di  *54,* 1134, *69,*Disattiva il timer SubClass_C2_timer_T8
    bool res_AndLogicOP_0 = true;
    bool res_AndLogicOP_1 = true;
    bool res_NotLogicOP_2 = true;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__GetSubcl26(my_id) == rosso));
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! res_NotLogicOP_3);
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_2);
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (Counter_GetValore(L_P1__GetSubcl41(my_id)) > 155021u));
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_4);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_AndLogicOP_1);
    res_AndLogicOP_0 = (res_AndLogicOP_0 && (Counter_GetValore(L_P1__GetSubcl41(my_id)) > 1134u));
    
    if(res_AndLogicOP_0){
    
    Timer_Disattiva(L_P1__GetSubcl38(my_id));
    }
    //  *34,*  se lo stato  è  diverso da  *56,*  state1  *106,*, *68,*Attiva il timer SubClass_C2_timer_T8
    // ,altrimenti  *66,* Assegna al comando SubClass_C2_comando_C8 il valore  False
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1_C2_GetState(my_id) == C2_St_state));
    if(res_NotLogicOP_5){
    
    Timer_Attiva(L_P1__GetSubcl38(my_id));
    }else{
    
    L_P1__SetOutSubcl2(my_id,false);
    }
    //  *36,*  se il timer SubClass_C2_timer_T8 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE  *36,* o  se il timer SubClass_C2_timer_T2 non è attivo *37,* e  se la variabile SubClass_C2_variabile_V9 non è  diverso da  *56,* 8, *66,* Assegna al comando SubClass_C2_comando_C2 il valore  True
    bool res_OrLogicOP_6 = false;
    bool res_OrLogicOP_7 = false;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! Timer_Disattivo(L_P1__GetSubcl38(my_id)));
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_NotLogicOP_8);
    res_OrLogicOP_7 = (res_OrLogicOP_7 || (L_P1__GetInConsd1(my_id) == false));
    
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_OrLogicOP_7);
    bool res_AndLogicOP_9 = true;
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! Timer_Attivo(L_P1__GetSubcl36(my_id)));
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_NotLogicOP_10);
    bool res_NotLogicOP_11 = true;
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (L_P1__GetSubcl28(my_id) == 8u));
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! res_NotLogicOP_12);
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_NotLogicOP_11);
    
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_AndLogicOP_9);
    
    if(res_OrLogicOP_6){
    
    L_P1__SetOutSubcl1(my_id,true);
    }
}

/*
    CNL corrispondente:
    
    { commento: {42,}  se  MainClass_C1_controllo_C1 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  commento: {105,} è  diverso da  True  commento: {34,} o  se il parametro SubClass_C2_parametro_P6 è  maggiore di  commento: {54,} 7 e  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} e  se il controllo SubClass_C2_controllo_C8 non è  uguale a  True ,  Applica gli effetti
           della macro SubClass_C2_macroef_M9( con argomento_af10   uguale a True ,argomento_af6   uguale a c270x ,argomento_af1   uguale a avvio ,argomento_af3   uguale a c75Giallo ,argomento_af2   uguale a c270x ,argomento_af4   uguale a c270x ,argomento_af9   uguale a Rosso ) commento: {73,}
    
     ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V9 il valore 4
    
    
     commento: {109,}  se il ripristino della variabile  SubClass_C2_restoreva_RV1 non è  diverso da c270x commento: {34,} e  se il parametro SubClass_C2_parametro_P6 non è  diverso da  commento: {56,} 2 commento: {35,} e  se il controllo SubClass_C2_controllo_C1 è  uguale a  True , commento: {69,}Disattiva il timer SubClass_C2_timer_T8
    
       
    
    }
*/
void L_P1__Macro11(instance_id_t const my_id )
{
//  *42,*  se  MainClass_C1_controllo_C1 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  *105,* è  diverso da  True  *34,* o  se il parametro SubClass_C2_parametro_P6 è  maggiore di  *54,* 7 e  se il controllo ConsDef  è  uguale a FALSE  *35,* e  se il controllo SubClass_C2_controllo_C8 non è  uguale a  True ,  Applica gli effetti
    //       della macro SubClass_C2_macroef_M9( con argomento_af10   uguale a True ,argomento_af6   uguale a c270x ,argomento_af1   uguale a avvio ,argomento_af3   uguale a c75Giallo ,argomento_af2   uguale a c270x ,argomento_af4   uguale a c270x ,argomento_af9   uguale a Rosso ) *73,*
    // ,altrimenti  *67,* Assegna alla variabile SubClass_C2_variabile_V9 il valore 4
    bool res_OrLogicOP_0 = false;
    bool res_ForAllPredicateNotEmpty_1 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl10Length(my_id); ++i)
    {
    L_P1__Recor1 it = L_P1__GetRecSubcl10(my_id,i);
    bool res_ImpliesLogicOp_2 = true;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__GetInMainc2(it.mainc46) == true));
    res_ImpliesLogicOp_2 = (res_ImpliesLogicOp_2 && res_NotLogicOP_3);
    res_ForAllPredicateNotEmpty_1 = res_ImpliesLogicOp_2;
    if(!res_ForAllPredicateNotEmpty_1) {break;}
    }
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_ForAllPredicateNotEmpty_1);
    bool res_AndLogicOP_4 = true;
    bool res_AndLogicOP_5 = true;
    res_AndLogicOP_5 = (res_AndLogicOP_5 && (L_P1__GetParamSubcl12(my_id) > 7u));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && (L_P1__GetInConsd1(my_id) == false));
    
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_AndLogicOP_5);
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetInSubcl8(my_id) == true));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_6);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_4);
    
    if(res_OrLogicOP_0){
    
    L_P1__Macro14(my_id,avvio,true,c270x,c75giallo,c270x,c270x,rosso);
    }else{
    
    L_P1__SetSubcl28(my_id,4u);
    }
    //  *109,*  se il ripristino della variabile  SubClass_C2_restoreva_RV1 non è  diverso da c270x *34,* e  se il parametro SubClass_C2_parametro_P6 non è  diverso da  *56,* 2 *35,* e  se il controllo SubClass_C2_controllo_C1 è  uguale a  True , *69,*Disattiva il timer SubClass_C2_timer_T8
    bool res_AndLogicOP_7 = true;
    bool res_AndLogicOP_8 = true;
    bool res_NotLogicOP_9 = true;
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__GetSubcl22(my_id) == c270x));
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! res_NotLogicOP_10);
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_9);
    bool res_NotLogicOP_11 = true;
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (L_P1__GetParamSubcl12(my_id) == 2u));
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! res_NotLogicOP_12);
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_11);
    
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_AndLogicOP_8);
    res_AndLogicOP_7 = (res_AndLogicOP_7 && (L_P1__GetInSubcl4(my_id) == true));
    
    if(res_AndLogicOP_7){
    
    Timer_Disattiva(L_P1__GetSubcl38(my_id));
    }
}

/*
    CNL corrispondente:
    
    { commento: {44,}  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  commento: {105,} è  minore di  commento: {55,} 9, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V2 il valore  False 
    
     ,altrimenti  commento: {71,}Decrementa il contatore SubClass_C2_contatore_Co8
    
    
     commento: {37,}  se la variabile SubClass_C2_variabile_V2 non è  diverso da  True  commento: {34,} e  se il parametro SubClass_C2_parametro_P6 non è  diverso da  commento: {56,} 3, commento: {69,}Disattiva il timer SubClass_C2_timer_T1
    
     ,altrimenti  commento: {68,}Attiva il timer SubClass_C2_timer_T2
    
    
     commento: {35,}  se il controllo SubClass_C2_controllo_C6 non è  uguale a  False , commento: {69,}Disattiva il timer SubClass_C2_timer_T8
    
       
    
    }
*/
void L_P1__Macro12(instance_id_t const my_id )
{
//  *44,*  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  *105,* è  minore di  *55,* 9, *67,* Assegna alla variabile SubClass_C2_variabile_V2 il valore  False 
    // ,altrimenti  *71,*Decrementa il contatore SubClass_C2_contatore_Co8
    bool res_ForAllPredicateNotEmpty_0 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl9Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl9(my_id,i);
    bool res_ImpliesLogicOp_1 = true;
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && (L_P1__GetMainc32(it.mainc45) < 9u));
    res_ForAllPredicateNotEmpty_0 = res_ImpliesLogicOp_1;
    if(!res_ForAllPredicateNotEmpty_0) {break;}
    }
    if(res_ForAllPredicateNotEmpty_0){
    
    L_P1__SetSubcl27(my_id,false);
    }else{
    
    Counter_Decr(L_P1__GetSubcl42(my_id));
    }
    //  *37,*  se la variabile SubClass_C2_variabile_V2 non è  diverso da  True  *34,* e  se il parametro SubClass_C2_parametro_P6 non è  diverso da  *56,* 3, *69,*Disattiva il timer SubClass_C2_timer_T1
    // ,altrimenti  *68,*Attiva il timer SubClass_C2_timer_T2
    bool res_AndLogicOP_2 = true;
    bool res_NotLogicOP_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetSubcl27(my_id) == true));
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! res_NotLogicOP_4);
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_3);
    bool res_NotLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetParamSubcl12(my_id) == 3u));
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! res_NotLogicOP_6);
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_5);
    
    if(res_AndLogicOP_2){
    
    Timer_Disattiva(L_P1__GetSubcl35(my_id));
    }else{
    
    Timer_Attiva(L_P1__GetSubcl36(my_id));
    }
    //  *35,*  se il controllo SubClass_C2_controllo_C6 non è  uguale a  False , *69,*Disattiva il timer SubClass_C2_timer_T8
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetInSubcl6(my_id) == false));
    if(res_NotLogicOP_7){
    
    Timer_Disattiva(L_P1__GetSubcl38(my_id));
    }
}

/*
    CNL corrispondente:
     
    { commento: {44,}  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  commento: {105,} è  uguale a  False  commento: {35,} o  se il controllo SubClass_C2_controllo_C3 è  diverso da  True  commento: {38,} e  se il contatore SubClass_C2_contatore_Co8 è  uguale a  commento: {53,} 15213, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V9 il valore 9
    
       
     commento: {43,}  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C2_lista_L9 è attivo commento: {34,} o  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  commento: {54,} 5 commento: {35,} o  se il controllo SubClass_C2_controllo_C7 è  uguale a Rosso, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V2 il valore  False 
    
       
     commento: {41,}  se MainClass_C1_parametro_P2 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a  commento: {53,} 6 o  se il controllo ConsDef  è  uguale a FALSE , commento: {67,} Assegna alla variabile SubClass_C2_variabile_V2 il valore  True 
    
     ,altrimenti  commento: {70,}Incrementa il contatore SubClass_C2_contatore_Co2
    
    
     commento: {110,}  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è attivo commento: {38,} e  se il contatore SubClass_C2_contatore_Co5 non è  uguale a  commento: {53,} 144 commento: {36,} o  se il timer SubClass_C2_timer_T2 non è attivo commento: {36,} e  se il timer SubClass_C2_timer_T2 non è scaduto o  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} e  se il timer SubClass_C2_timer_T2 non è attivo, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V2 il valore  True 
    
     ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V2 il valore  False 
    
    
    
    }
*/
void L_P1__Macro13(instance_id_t const my_id )
{
//  *44,*  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  *105,* è  uguale a  False  *35,* o  se il controllo SubClass_C2_controllo_C3 è  diverso da  True  *38,* e  se il contatore SubClass_C2_contatore_Co8 è  uguale a  *53,* 15213, *67,* Assegna alla variabile SubClass_C2_variabile_V9 il valore 9
    bool res_OrLogicOP_0 = false;
    bool res_ForAllPredicateNotEmpty_1 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl10Length(my_id); ++i)
    {
    L_P1__Recor1 it = L_P1__GetRecSubcl10(my_id,i);
    bool res_ImpliesLogicOp_2 = true;
    res_ImpliesLogicOp_2 = (res_ImpliesLogicOp_2 && (L_P1__GetMainc33(it.mainc46) == false));
    res_ForAllPredicateNotEmpty_1 = res_ImpliesLogicOp_2;
    if(!res_ForAllPredicateNotEmpty_1) {break;}
    }
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_ForAllPredicateNotEmpty_1);
    bool res_AndLogicOP_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetInSubcl5(my_id) == true));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_4);
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (Counter_GetValore(L_P1__GetSubcl42(my_id)) == 15213u));
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_3);
    
    if(res_OrLogicOP_0){
    
    L_P1__SetSubcl28(my_id,9u);
    }
    //  *43,*  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C2_lista_L9 è attivo *34,* o  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  *54,* 5 *35,* o  se il controllo SubClass_C2_controllo_C7 è  uguale a Rosso, *67,* Assegna alla variabile SubClass_C2_variabile_V2 il valore  False
    bool res_OrLogicOP_5 = false;
    bool res_OrLogicOP_6 = false;
    bool res_ForAllPredicate_7 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl10Length(my_id); ++i)
    {
    L_P1__Recor1 it = L_P1__GetRecSubcl10(my_id,i);
    bool res_ImpliesLogicOp_8 = true;
    res_ImpliesLogicOp_8 = (res_ImpliesLogicOp_8 && Timer_Attivo(L_P1__GetMainc42(it.mainc46)));
    res_ForAllPredicate_7 = res_ImpliesLogicOp_8;
    if(!res_ForAllPredicate_7) {break;}
    }
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_ForAllPredicate_7);
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetParamSubcl12(my_id) > 5u));
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_NotLogicOP_9);
    
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_OrLogicOP_6);
    res_OrLogicOP_5 = (res_OrLogicOP_5 || (L_P1__GetInSubcl7(my_id) == rosso));
    
    if(res_OrLogicOP_5){
    
    L_P1__SetSubcl27(my_id,false);
    }
    //  *41,*  se MainClass_C1_parametro_P2 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a  *53,* 6 o  se il controllo ConsDef  è  uguale a FALSE , *67,* Assegna alla variabile SubClass_C2_variabile_V2 il valore  True 
    // ,altrimenti  *70,*Incrementa il contatore SubClass_C2_contatore_Co2
    bool res_OrLogicOP_10 = false;
    bool res_ForAllPredicate_11 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl10Length(my_id); ++i)
    {
    L_P1__Recor1 it = L_P1__GetRecSubcl10(my_id,i);
    bool res_ImpliesLogicOp_12 = true;
    res_ImpliesLogicOp_12 = (res_ImpliesLogicOp_12 && (L_P1__GetParamMainc6(it.mainc46) == 6u));
    res_ForAllPredicate_11 = res_ImpliesLogicOp_12;
    if(!res_ForAllPredicate_11) {break;}
    }
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_ForAllPredicate_11);
    res_OrLogicOP_10 = (res_OrLogicOP_10 || (L_P1__GetInConsd1(my_id) == false));
    
    if(res_OrLogicOP_10){
    
    L_P1__SetSubcl27(my_id,true);
    }else{
    
    Counter_Incr(L_P1__GetSubcl40(my_id));
    }
    //  *110,*  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è attivo *38,* e  se il contatore SubClass_C2_contatore_Co5 non è  uguale a  *53,* 144 *36,* o  se il timer SubClass_C2_timer_T2 non è attivo *36,* e  se il timer SubClass_C2_timer_T2 non è scaduto o  se il controllo ConsDef  è  uguale a FALSE  *36,* e  se il timer SubClass_C2_timer_T2 non è attivo, *67,* Assegna alla variabile SubClass_C2_variabile_V2 il valore  True 
    // ,altrimenti  *67,* Assegna alla variabile SubClass_C2_variabile_V2 il valore  False
    bool res_OrLogicOP_13 = false;
    bool res_OrLogicOP_14 = false;
    bool res_AndLogicOP_15 = true;
    res_AndLogicOP_15 = (res_AndLogicOP_15 && Timer_Attivo(L_P1__GetSubcl30(my_id)));
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (Counter_GetValore(L_P1__GetSubcl41(my_id)) == 144u));
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_NotLogicOP_16);
    
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_AndLogicOP_15);
    bool res_AndLogicOP_17 = true;
    bool res_NotLogicOP_18 = true;
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! Timer_Attivo(L_P1__GetSubcl36(my_id)));
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_NotLogicOP_18);
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! Timer_Scaduto(L_P1__GetSubcl36(my_id)));
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_NotLogicOP_19);
    
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_AndLogicOP_17);
    
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_OrLogicOP_14);
    bool res_AndLogicOP_20 = true;
    res_AndLogicOP_20 = (res_AndLogicOP_20 && (L_P1__GetInConsd1(my_id) == false));
    bool res_NotLogicOP_21 = true;
    res_NotLogicOP_21 = (res_NotLogicOP_21 && ! Timer_Attivo(L_P1__GetSubcl36(my_id)));
    res_AndLogicOP_20 = (res_AndLogicOP_20 && res_NotLogicOP_21);
    
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_AndLogicOP_20);
    
    if(res_OrLogicOP_13){
    
    L_P1__SetSubcl27(my_id,true);
    }else{
    
    L_P1__SetSubcl27(my_id,false);
    }
}

/*
    CNL corrispondente:
    
    {  se l'argomento argomento_af10 è  uguale a  True  commento: {39,} ,  commento: {45,}  se  MainClass_C1_contatore_Co7 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  commento: {105,} è  maggiore di  commento: {54,} 144, commento: {88,} quando  commento: {45,}    MainClass_C1_contatore_Co1 del campo  MainClass_C1     è  diverso da  commento: {56,} 1350 commento: {37,} e  se la variabile SubClass_C2_variabile_V2 non è  diverso da  False  commento: {37,} o  se la variabile SubClass_C2_variabile_V2 non è  uguale a  True  commento: {35,} o  se il controllo SubClass_C2_controllo_C1 è  diverso da  False  commento: {37,} e  se la variabile SubClass_C2_variabile_V9 è  minore di  commento: {55,} 2 e  se l'argomento argomento_af10 è  diverso da  False  commento: {39,} ,  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V2 il valore  True  commento: {67,}
    
       
      se l'argomento argomento_af1 è  diverso da Rosso commento: {39,} , commento: {72,}Azzera il contatore SubClass_C2_contatore_Co2
    
     ,altrimenti  commento: {66,} Assegna al comando SubClass_C2_comando_C10 il valore GialloGiallo
    
    
     commento: {42,}  se  MainClass_C1_controllo_C1 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a  True  o  se l'argomento argomento_af3 non  è  uguale a c120 commento: {39,} , commento: {67,} Assegna alla variabile SubClass_C2_variabile_V2 il valore  False 
    
     ,altrimenti  commento: {66,} Assegna al comando SubClass_C2_comando_C2 il valore  True 
    
    
     commento: {34,}  se il parametro SubClass_C2_parametro_P3 è  minore di  commento: {55,} 3,  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V2 il valore  False commento: {67,}
    
       
     commento: {110,}  se il ripristino del timer  SubClass_C2_restoreTI_TI3 non è scaduto commento: {37,} e  se la variabile SubClass_C2_variabile_V2 non è  uguale a  False ,  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V2 il valore  True  commento: {67,}
    
       
    
    }
*/
void L_P1__Macro14(instance_id_t const my_id , C2_Enumerat1 argom32, bool argom33, C2_Enumerat3 argom34, C2_Enumerat4 argom35, C2_Enumerat3 argom36, C2_Enumerat3 argom37, C2_Enumerat1 argom38)
{
//  se l'argomento argomento_af10 è  uguale a  True  *39,* ,  *45,*  se  MainClass_C1_contatore_Co7 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  *105,* è  maggiore di  *54,* 144, *88,* quando  *45,*    MainClass_C1_contatore_Co1 del campo  MainClass_C1     è  diverso da  *56,* 1350 *37,* e  se la variabile SubClass_C2_variabile_V2 non è  diverso da  False  *37,* o  se la variabile SubClass_C2_variabile_V2 non è  uguale a  True  *35,* o  se il controllo SubClass_C2_controllo_C1 è  diverso da  False  *37,* e  se la variabile SubClass_C2_variabile_V9 è  minore di  *55,* 2 e  se l'argomento argomento_af10 è  diverso da  False  *39,* ,  *67,* Assegna alla variabile SubClass_C2_variabile_V2 il valore  True
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_AndLogicOP_2 = true;
    bool res_AndLogicOP_3 = true;
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (argom33 == true));
    bool res_ForAllPredicateNotEmpty_4 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl9Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl9(my_id,i);
    bool res_ImpliesLogicOp_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (Counter_GetValore(L_P1__GetMainc43(it.mainc45)) == 1350u));
    if(res_NotLogicOP_6){
    res_ImpliesLogicOp_5 = (res_ImpliesLogicOp_5 && (Counter_GetValore(L_P1__GetMainc44(it.mainc45)) > 144u));
    res_ForAllPredicateNotEmpty_4 = res_ImpliesLogicOp_5;
    if(!res_ForAllPredicateNotEmpty_4) {break;}
    }
    }
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_ForAllPredicateNotEmpty_4);
    
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_AndLogicOP_3);
    bool res_NotLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetSubcl27(my_id) == false));
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! res_NotLogicOP_8);
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_7);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_2);
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetSubcl27(my_id) == true));
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_NotLogicOP_9);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_AndLogicOP_10 = true;
    bool res_AndLogicOP_11 = true;
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (L_P1__GetInSubcl4(my_id) == false));
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_NotLogicOP_12);
    res_AndLogicOP_11 = (res_AndLogicOP_11 && (L_P1__GetSubcl28(my_id) < 2u));
    
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_AndLogicOP_11);
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (argom33 == false));
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_NotLogicOP_13);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_10);
    
    if(res_OrLogicOP_0){
    
    L_P1__SetSubcl27(my_id,true);
    }
    //  *67,*
    //   
    //  se l'argomento argomento_af1 è  diverso da Rosso *39,* , *72,*Azzera il contatore SubClass_C2_contatore_Co2
    // ,altrimenti  *66,* Assegna al comando SubClass_C2_comando_C10 il valore GialloGiallo
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (argom32 == rosso));
    if(res_NotLogicOP_14){
    
    Counter_Res(L_P1__GetSubcl40(my_id));
    }else{
    
    L_P1__SetOutSubcl(my_id,giallogiall);
    }
    //  *42,*  se  MainClass_C1_controllo_C1 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a  True  o  se l'argomento argomento_af3 non  è  uguale a c120 *39,* , *67,* Assegna alla variabile SubClass_C2_variabile_V2 il valore  False 
    // ,altrimenti  *66,* Assegna al comando SubClass_C2_comando_C2 il valore  True
    bool res_OrLogicOP_15 = false;
    bool res_ForAllPredicate_16 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl10Length(my_id); ++i)
    {
    L_P1__Recor1 it = L_P1__GetRecSubcl10(my_id,i);
    bool res_ImpliesLogicOp_17 = true;
    res_ImpliesLogicOp_17 = (res_ImpliesLogicOp_17 && (L_P1__GetInMainc2(it.mainc46) == true));
    res_ForAllPredicate_16 = res_ImpliesLogicOp_17;
    if(!res_ForAllPredicate_16) {break;}
    }
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_ForAllPredicate_16);
    bool res_NotLogicOP_18 = true;
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! (argom35 == c120));
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_NotLogicOP_18);
    
    if(res_OrLogicOP_15){
    
    L_P1__SetSubcl27(my_id,false);
    }else{
    
    L_P1__SetOutSubcl1(my_id,true);
    }
    //  *34,*  se il parametro SubClass_C2_parametro_P3 è  minore di  *55,* 3,  *67,* Assegna alla variabile SubClass_C2_variabile_V2 il valore  False
    if((L_P1__GetParamSubcl11(my_id) < 3u)){
    
    L_P1__SetSubcl27(my_id,false);
    }
    //  *67,*
    //   
    // *110,*  se il ripristino del timer  SubClass_C2_restoreTI_TI3 non è scaduto *37,* e  se la variabile SubClass_C2_variabile_V2 non è  uguale a  False ,  *67,* Assegna alla variabile SubClass_C2_variabile_V2 il valore  True
    bool res_AndLogicOP_19 = true;
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! Timer_Scaduto(L_P1__GetSubcl34(my_id)));
    res_AndLogicOP_19 = (res_AndLogicOP_19 && res_NotLogicOP_20);
    bool res_NotLogicOP_21 = true;
    res_NotLogicOP_21 = (res_NotLogicOP_21 && ! (L_P1__GetSubcl27(my_id) == false));
    res_AndLogicOP_19 = (res_AndLogicOP_19 && res_NotLogicOP_21);
    
    if(res_AndLogicOP_19){
    
    L_P1__SetSubcl27(my_id,true);
    }
}


// Macro di verifica

/*
    CNL corrispondente:
     
    { commento: {41,}  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a  False  commento: {35,} e  se il controllo SubClass_C2_controllo_C8 è  diverso da  True  commento: {37,} e  se la variabile SubClass_C2_variabile_V9 è  minore di  commento: {55,} 6 commento: {38,} e  se il contatore SubClass_C2_contatore_Co8 non è  diverso da  commento: {56,} 14 commento: {38,} o  se il contatore SubClass_C2_contatore_Co2 non è  maggiore di  commento: {54,} 1334 commento: {37,} e  se la variabile SubClass_C2_variabile_V9 non è  uguale a  commento: {53,} 3, Verifica che   commento: {47,48,50,}   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} o  che  commento: {,}  la variabile SubClass_C2_variabile_V2 non sia  uguale a  False 
     commento: {104,} e  che  commento: {34,}  il parametro SubClass_C2_parametro_P3 non sia  uguale a  commento: {53,} 3
     commento: {104,} e  che  commento: {34,}  il parametro SubClass_C2_parametro_P3 non sia  minore di  commento: {55,} 7
     commento: {104,} o  che  commento: {,}  il controllo SubClass_C2_controllo_C1 sia  uguale a  False 
    
    
    }
*/
bool L_P1__Macro19(instance_id_t const my_id )
{
bool res_AndLogicOP_0 = true;
    
    //  *41,*  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a  False  *35,* e  se il controllo SubClass_C2_controllo_C8 è  diverso da  True  *37,* e  se la variabile SubClass_C2_variabile_V9 è  minore di  *55,* 6 *38,* e  se il contatore SubClass_C2_contatore_Co8 non è  diverso da  *56,* 14 *38,* o  se il contatore SubClass_C2_contatore_Co2 non è  maggiore di  *54,* 1334 *37,* e  se la variabile SubClass_C2_variabile_V9 non è  uguale a  *53,* 3, Verifica che   *47,48,50,*   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* o  che  *,*  la variabile SubClass_C2_variabile_V2 non sia  uguale a  False 
    //   *104,* e  che  *34,*  il parametro SubClass_C2_parametro_P3 non sia  uguale a  *53,* 3
    //   *104,* e  che  *34,*  il parametro SubClass_C2_parametro_P3 non sia  minore di  *55,* 7
    //   *104,* o  che  *,*  il controllo SubClass_C2_controllo_C1 sia  uguale a  False
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_AndLogicOP_3 = true;
    bool res_AndLogicOP_4 = true;
    bool res_AndLogicOP_5 = true;
    bool res_ForAllPredicate_6 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl9Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl9(my_id,i);
    bool res_ImpliesLogicOp_7 = true;
    res_ImpliesLogicOp_7 = (res_ImpliesLogicOp_7 && (L_P1__GetParamMainc7(it.mainc45) == false));
    res_ForAllPredicate_6 = res_ImpliesLogicOp_7;
    if(!res_ForAllPredicate_6) {break;}
    }
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_ForAllPredicate_6);
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetInSubcl8(my_id) == true));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_8);
    
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_AndLogicOP_5);
    res_AndLogicOP_4 = (res_AndLogicOP_4 && (L_P1__GetSubcl28(my_id) < 6u));
    
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_AndLogicOP_4);
    bool res_NotLogicOP_9 = true;
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (Counter_GetValore(L_P1__GetSubcl42(my_id)) == 14u));
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! res_NotLogicOP_10);
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_9);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_3);
    bool res_AndLogicOP_11 = true;
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (Counter_GetValore(L_P1__GetSubcl40(my_id)) > 1334u));
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_NotLogicOP_12);
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (L_P1__GetSubcl28(my_id) == 3u));
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_NotLogicOP_13);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_11);
    
    if(res_OrLogicOP_2){
    bool res_OrLogicOP_14 = false;
    bool res_OrLogicOP_15 = false;
    res_OrLogicOP_15 = (res_OrLogicOP_15 || (L_P1__GetInConsd1(my_id) == false));
    bool res_AndLogicOP_16 = true;
    bool res_AndLogicOP_17 = true;
    bool res_NotLogicOP_18 = true;
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! (L_P1__GetSubcl27(my_id) == false));
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_NotLogicOP_18);
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (L_P1__GetParamSubcl11(my_id) == 3u));
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_NotLogicOP_19);
    
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_AndLogicOP_17);
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! (L_P1__GetParamSubcl11(my_id) < 7u));
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_NotLogicOP_20);
    
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_AndLogicOP_16);
    
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_OrLogicOP_15);
    res_OrLogicOP_14 = (res_OrLogicOP_14 || (L_P1__GetInSubcl4(my_id) == false));
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_OrLogicOP_14);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
    
    { commento: {63,} commento: {34,}  se il parametro SubClass_C2_parametro_P3 è  maggiore di  commento: {54,} 2, Solo una delle seguenti { 
     commento: {61,} commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  commento: {105,} è  diverso da  commento: {56,}  state1  commento: {34,} e  se il parametro SubClass_C2_parametro_P3 non è  minore di  commento: {55,} 9 commento: {38,} o  se il contatore SubClass_C2_contatore_Co5 non è  diverso da  commento: {56,} 1313 commento: {37,} o  se la variabile SubClass_C2_variabile_V9 è  maggiore di  commento: {54,} 8, Tutte le seguenti { 
     commento: {62,} commento: {42,}  se  MainClass_C1_controllo_C1 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  diverso da  False  commento: {35,} e  se il controllo SubClass_C2_controllo_C6 è  diverso da  True  commento: {38,} e  se il contatore SubClass_C2_contatore_Co5 non è  minore di  commento: {55,} 154 commento: {38,} o  se il contatore SubClass_C2_contatore_Co8 è  diverso da  commento: {56,} 11 e  se l'argomento argomento_ave6 non  è  uguale a  True  commento: {39,}  commento: {36,} e  se il timer SubClass_C2_timer_T2 non è disattivo, Almeno una delle seguenti { 
     commento: {62,} commento: {44,}  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a  True  commento: {35,} e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  True  commento: {36,} e  se il timer SubClass_C2_timer_T6 è scaduto, Almeno una delle seguenti { 
     commento: {62,} commento: {44,}  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  commento: {105,} è  uguale a  True  commento: {36,} o  se il timer SubClass_C2_timer_T9 non è scaduto commento: {35,} o  se il controllo SubClass_C2_controllo_C1 è  diverso da  True , Almeno una delle seguenti { 
     commento: {35,}  se il controllo SubClass_C2_controllo_C8 è  diverso da  False  commento: {38,} e  se il contatore SubClass_C2_contatore_Co2 non è  minore di  commento: {55,} 155021 commento: {34,} o  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  commento: {54,} 4, Verifica che   commento: {47,52,}  commento: {34,}  il parametro SubClass_C2_parametro_P3 sia  uguale a  commento: {53,} 9
     commento: {104,} e  che   l'argomento argomento_ave6 sia  uguale a  True  commento: {,} 
    
    
     } Verifica che   commento: {47,49,50,}  commento: {,}  il timer SubClass_C2_timer_T2 sia disattivo
     commento: {104,} e  che  commento: {34,}  il parametro SubClass_C2_parametro_P6 sia  maggiore di  commento: {54,} 9
     commento: {104,} o  che  commento: {,}  la variabile SubClass_C2_variabile_V2 non sia  diverso da  True 
     commento: {104,} o  che  commento: {36,}  il timer SubClass_C2_timer_T2 non sia disattivo
     commento: {104,} e  che  commento: {36,}  il timer SubClass_C2_timer_T2 sia scaduto
     commento: {104,} o  che  commento: {37,}  la variabile SubClass_C2_variabile_V9 non sia  diverso da  commento: {56,} 9
    
    
     } Verifica che   commento: {48,50,}  commento: {,}  il controllo SubClass_C2_controllo_C8 sia  uguale a  True 
     commento: {104,} e  che  commento: {,}  la variabile SubClass_C2_variabile_V9 non sia  minore di  commento: {55,} 4
    
    
     } Verifica che   commento: {48,49,51,}  commento: {,}  il controllo SubClass_C2_controllo_C1 sia  diverso da  True 
     commento: {104,} e  che  commento: {,}  il timer SubClass_C2_timer_T2 non sia scaduto
     commento: {104,} e  che  commento: {,}  il contatore SubClass_C2_contatore_Co5 non sia  minore di  commento: {55,} 15
    
    
     } Verifica che   commento: {48,}  commento: {,}  il controllo SubClass_C2_controllo_C8 sia  diverso da  True 
    
    
     } Verifica che   commento: {47,48,52,}  commento: {,}  il controllo SubClass_C2_controllo_C8 non sia  diverso da  True 
     commento: {104,} o  che   l'argomento argomento_ave10 non  sia  uguale a c120 commento: {,} 
     commento: {104,} e  che  commento: {35,}  il controllo SubClass_C2_controllo_C8 sia  uguale a  False 
     commento: {104,} o  che   l'argomento argomento_ave10 sia  uguale a c120 commento: {39,} 
     commento: {104,} e  che  commento: {34,}  il parametro SubClass_C2_parametro_P6 sia  maggiore di  commento: {54,} 8
    
    
    }
*/
bool L_P1__Macro20(instance_id_t const my_id , bool argom58, C2_Enumerat4 argom59, C2_Enumerat4 argom60, bool argom61)
{
bool res_AndLogicOP_0 = true;
    
    //  *63,* *34,*  se il parametro SubClass_C2_parametro_P3 è  maggiore di  *54,* 2, Solo una delle seguenti { 
    //   *61,* *111,*  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  *105,* è  diverso da  *56,*  state1  *34,* e  se il parametro SubClass_C2_parametro_P3 non è  minore di  *55,* 9 *38,* o  se il contatore SubClass_C2_contatore_Co5 non è  diverso da  *56,* 1313 *37,* o  se la variabile SubClass_C2_variabile_V9 è  maggiore di  *54,* 8, Tutte le seguenti { 
    //   *62,* *42,*  se  MainClass_C1_controllo_C1 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  diverso da  False  *35,* e  se il controllo SubClass_C2_controllo_C6 è  diverso da  True  *38,* e  se il contatore SubClass_C2_contatore_Co5 non è  minore di  *55,* 154 *38,* o  se il contatore SubClass_C2_contatore_Co8 è  diverso da  *56,* 11 e  se l'argomento argomento_ave6 non  è  uguale a  True  *39,*  *36,* e  se il timer SubClass_C2_timer_T2 non è disattivo, Almeno una delle seguenti { 
    //   *62,* *44,*  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a  True  *35,* e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  True  *36,* e  se il timer SubClass_C2_timer_T6 è scaduto, Almeno una delle seguenti { 
    //   *62,* *44,*  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  *105,* è  uguale a  True  *36,* o  se il timer SubClass_C2_timer_T9 non è scaduto *35,* o  se il controllo SubClass_C2_controllo_C1 è  diverso da  True , Almeno una delle seguenti { 
    //   *35,*  se il controllo SubClass_C2_controllo_C8 è  diverso da  False  *38,* e  se il contatore SubClass_C2_contatore_Co2 non è  minore di  *55,* 155021 *34,* o  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  *54,* 4, Verifica che   *47,52,*  *34,*  il parametro SubClass_C2_parametro_P3 sia  uguale a  *53,* 9
    //   *104,* e  che   l'argomento argomento_ave6 sia  uguale a  True  *,* 
    //   } Verifica che   *47,49,50,*  *,*  il timer SubClass_C2_timer_T2 sia disattivo
    //   *104,* e  che  *34,*  il parametro SubClass_C2_parametro_P6 sia  maggiore di  *54,* 9
    //   *104,* o  che  *,*  la variabile SubClass_C2_variabile_V2 non sia  diverso da  True 
    //   *104,* o  che  *36,*  il timer SubClass_C2_timer_T2 non sia disattivo
    //   *104,* e  che  *36,*  il timer SubClass_C2_timer_T2 sia scaduto
    //   *104,* o  che  *37,*  la variabile SubClass_C2_variabile_V9 non sia  diverso da  *56,* 9
    //   } Verifica che   *48,50,*  *,*  il controllo SubClass_C2_controllo_C8 sia  uguale a  True 
    //   *104,* e  che  *,*  la variabile SubClass_C2_variabile_V9 non sia  minore di  *55,* 4
    //   } Verifica che   *48,49,51,*  *,*  il controllo SubClass_C2_controllo_C1 sia  diverso da  True 
    //   *104,* e  che  *,*  il timer SubClass_C2_timer_T2 non sia scaduto
    //   *104,* e  che  *,*  il contatore SubClass_C2_contatore_Co5 non sia  minore di  *55,* 15
    //   } Verifica che   *48,*  *,*  il controllo SubClass_C2_controllo_C8 sia  diverso da  True 
    //   }
    bool res_ImpliesLogicOp_1 = true;
    if((L_P1__GetParamSubcl11(my_id) > 2u)){
    bool res_XorLogicOP_2 = true;
    int xorIndex_res_XorLogicOP_2 = 0;
    bool res_ImpliesLogicOp_3 = true;
    bool res_OrLogicOP_4 = false;
    bool res_OrLogicOP_5 = false;
    bool res_AndLogicOP_6 = true;
    bool res_ForAllPredicateNotEmpty_7 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl10Length(my_id); ++i)
    {
    L_P1__Recor1 it = L_P1__GetRecSubcl10(my_id,i);
    bool res_ImpliesLogicOp_8 = true;
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1_C1_GetState(it.mainc46) == C1_St_state));
    res_ImpliesLogicOp_8 = (res_ImpliesLogicOp_8 && res_NotLogicOP_9);
    res_ForAllPredicateNotEmpty_7 = res_ImpliesLogicOp_8;
    if(!res_ForAllPredicateNotEmpty_7) {break;}
    }
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_ForAllPredicateNotEmpty_7);
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__GetParamSubcl11(my_id) < 9u));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_10);
    
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_AndLogicOP_6);
    bool res_NotLogicOP_11 = true;
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (Counter_GetValore(L_P1__GetSubcl41(my_id)) == 1313u));
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! res_NotLogicOP_12);
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_NotLogicOP_11);
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_OrLogicOP_5);
    res_OrLogicOP_4 = (res_OrLogicOP_4 || (L_P1__GetSubcl28(my_id) > 8u));
    
    if(res_OrLogicOP_4){
    bool res_AndLogicOP_13 = true;
    bool res_ImpliesLogicOp_14 = true;
    bool res_OrLogicOP_15 = false;
    bool res_AndLogicOP_16 = true;
    bool res_AndLogicOP_17 = true;
    bool res_ForAllPredicate_18 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl10Length(my_id); ++i)
    {
    L_P1__Recor1 it = L_P1__GetRecSubcl10(my_id,i);
    bool res_ImpliesLogicOp_19 = true;
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! (L_P1__GetInMainc2(it.mainc46) == false));
    res_ImpliesLogicOp_19 = (res_ImpliesLogicOp_19 && res_NotLogicOP_20);
    res_ForAllPredicate_18 = res_ImpliesLogicOp_19;
    if(!res_ForAllPredicate_18) {break;}
    }
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_ForAllPredicate_18);
    bool res_NotLogicOP_21 = true;
    res_NotLogicOP_21 = (res_NotLogicOP_21 && ! (L_P1__GetInSubcl6(my_id) == true));
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_NotLogicOP_21);
    
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_AndLogicOP_17);
    bool res_NotLogicOP_22 = true;
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! (Counter_GetValore(L_P1__GetSubcl41(my_id)) < 154u));
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_NotLogicOP_22);
    
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_AndLogicOP_16);
    bool res_AndLogicOP_23 = true;
    bool res_AndLogicOP_24 = true;
    bool res_NotLogicOP_25 = true;
    res_NotLogicOP_25 = (res_NotLogicOP_25 && ! (Counter_GetValore(L_P1__GetSubcl42(my_id)) == 11u));
    res_AndLogicOP_24 = (res_AndLogicOP_24 && res_NotLogicOP_25);
    bool res_NotLogicOP_26 = true;
    res_NotLogicOP_26 = (res_NotLogicOP_26 && ! (argom61 == true));
    res_AndLogicOP_24 = (res_AndLogicOP_24 && res_NotLogicOP_26);
    
    res_AndLogicOP_23 = (res_AndLogicOP_23 && res_AndLogicOP_24);
    bool res_NotLogicOP_27 = true;
    res_NotLogicOP_27 = (res_NotLogicOP_27 && ! Timer_Disattivo(L_P1__GetSubcl36(my_id)));
    res_AndLogicOP_23 = (res_AndLogicOP_23 && res_NotLogicOP_27);
    
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_AndLogicOP_23);
    
    if(res_OrLogicOP_15){
    bool res_OrLogicOP_28 = false;
    bool res_ImpliesLogicOp_29 = true;
    bool res_AndLogicOP_30 = true;
    bool res_AndLogicOP_31 = true;
    bool res_ForAllPredicate_32 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl9Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl9(my_id,i);
    bool res_ImpliesLogicOp_33 = true;
    res_ImpliesLogicOp_33 = (res_ImpliesLogicOp_33 && (L_P1__GetMainc33(it.mainc45) == true));
    res_ForAllPredicate_32 = res_ImpliesLogicOp_33;
    if(!res_ForAllPredicate_32) {break;}
    }
    res_AndLogicOP_31 = (res_AndLogicOP_31 && res_ForAllPredicate_32);
    bool res_NotLogicOP_34 = true;
    res_NotLogicOP_34 = (res_NotLogicOP_34 && ! (L_P1__GetInSubcl5(my_id) == true));
    res_AndLogicOP_31 = (res_AndLogicOP_31 && res_NotLogicOP_34);
    
    res_AndLogicOP_30 = (res_AndLogicOP_30 && res_AndLogicOP_31);
    res_AndLogicOP_30 = (res_AndLogicOP_30 && Timer_Scaduto(L_P1__GetSubcl37(my_id)));
    
    if(res_AndLogicOP_30){
    bool res_OrLogicOP_35 = false;
    bool res_ImpliesLogicOp_36 = true;
    bool res_OrLogicOP_37 = false;
    bool res_OrLogicOP_38 = false;
    bool res_ForAllPredicateNotEmpty_39 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl9Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl9(my_id,i);
    bool res_ImpliesLogicOp_40 = true;
    res_ImpliesLogicOp_40 = (res_ImpliesLogicOp_40 && (L_P1__GetMainc33(it.mainc45) == true));
    res_ForAllPredicateNotEmpty_39 = res_ImpliesLogicOp_40;
    if(!res_ForAllPredicateNotEmpty_39) {break;}
    }
    res_OrLogicOP_38 = (res_OrLogicOP_38 || res_ForAllPredicateNotEmpty_39);
    bool res_NotLogicOP_41 = true;
    res_NotLogicOP_41 = (res_NotLogicOP_41 && ! Timer_Scaduto(L_P1__GetSubcl39(my_id)));
    res_OrLogicOP_38 = (res_OrLogicOP_38 || res_NotLogicOP_41);
    
    res_OrLogicOP_37 = (res_OrLogicOP_37 || res_OrLogicOP_38);
    bool res_NotLogicOP_42 = true;
    res_NotLogicOP_42 = (res_NotLogicOP_42 && ! (L_P1__GetInSubcl4(my_id) == true));
    res_OrLogicOP_37 = (res_OrLogicOP_37 || res_NotLogicOP_42);
    
    if(res_OrLogicOP_37){
    bool res_ImpliesLogicOp_43 = true;
    bool res_OrLogicOP_44 = false;
    bool res_AndLogicOP_45 = true;
    bool res_NotLogicOP_46 = true;
    res_NotLogicOP_46 = (res_NotLogicOP_46 && ! (L_P1__GetInSubcl8(my_id) == false));
    res_AndLogicOP_45 = (res_AndLogicOP_45 && res_NotLogicOP_46);
    bool res_NotLogicOP_47 = true;
    res_NotLogicOP_47 = (res_NotLogicOP_47 && ! (Counter_GetValore(L_P1__GetSubcl40(my_id)) < 155021u));
    res_AndLogicOP_45 = (res_AndLogicOP_45 && res_NotLogicOP_47);
    
    res_OrLogicOP_44 = (res_OrLogicOP_44 || res_AndLogicOP_45);
    bool res_NotLogicOP_48 = true;
    res_NotLogicOP_48 = (res_NotLogicOP_48 && ! (L_P1__GetParamSubcl12(my_id) > 4u));
    res_OrLogicOP_44 = (res_OrLogicOP_44 || res_NotLogicOP_48);
    
    if(res_OrLogicOP_44){
    bool res_AndLogicOP_49 = true;
    res_AndLogicOP_49 = (res_AndLogicOP_49 && (L_P1__GetParamSubcl11(my_id) == 9u));
    res_AndLogicOP_49 = (res_AndLogicOP_49 && (argom61 == true));
    
    res_ImpliesLogicOp_43 = (res_ImpliesLogicOp_43 && res_AndLogicOP_49);
    }
    res_ImpliesLogicOp_36 = (res_ImpliesLogicOp_36 && res_ImpliesLogicOp_43);
    }
    res_OrLogicOP_35 = (res_OrLogicOP_35 || res_ImpliesLogicOp_36);
    bool res_OrLogicOP_50 = false;
    bool res_OrLogicOP_51 = false;
    bool res_OrLogicOP_52 = false;
    bool res_AndLogicOP_53 = true;
    res_AndLogicOP_53 = (res_AndLogicOP_53 && Timer_Disattivo(L_P1__GetSubcl36(my_id)));
    res_AndLogicOP_53 = (res_AndLogicOP_53 && (L_P1__GetParamSubcl12(my_id) > 9u));
    
    res_OrLogicOP_52 = (res_OrLogicOP_52 || res_AndLogicOP_53);
    bool res_NotLogicOP_54 = true;
    bool res_NotLogicOP_55 = true;
    res_NotLogicOP_55 = (res_NotLogicOP_55 && ! (L_P1__GetSubcl27(my_id) == true));
    res_NotLogicOP_54 = (res_NotLogicOP_54 && ! res_NotLogicOP_55);
    res_OrLogicOP_52 = (res_OrLogicOP_52 || res_NotLogicOP_54);
    
    res_OrLogicOP_51 = (res_OrLogicOP_51 || res_OrLogicOP_52);
    bool res_AndLogicOP_56 = true;
    bool res_NotLogicOP_57 = true;
    res_NotLogicOP_57 = (res_NotLogicOP_57 && ! Timer_Disattivo(L_P1__GetSubcl36(my_id)));
    res_AndLogicOP_56 = (res_AndLogicOP_56 && res_NotLogicOP_57);
    res_AndLogicOP_56 = (res_AndLogicOP_56 && Timer_Scaduto(L_P1__GetSubcl36(my_id)));
    
    res_OrLogicOP_51 = (res_OrLogicOP_51 || res_AndLogicOP_56);
    
    res_OrLogicOP_50 = (res_OrLogicOP_50 || res_OrLogicOP_51);
    bool res_NotLogicOP_58 = true;
    bool res_NotLogicOP_59 = true;
    res_NotLogicOP_59 = (res_NotLogicOP_59 && ! (L_P1__GetSubcl28(my_id) == 9u));
    res_NotLogicOP_58 = (res_NotLogicOP_58 && ! res_NotLogicOP_59);
    res_OrLogicOP_50 = (res_OrLogicOP_50 || res_NotLogicOP_58);
    
    res_OrLogicOP_35 = (res_OrLogicOP_35 || res_OrLogicOP_50);
    
    res_ImpliesLogicOp_29 = (res_ImpliesLogicOp_29 && res_OrLogicOP_35);
    }
    res_OrLogicOP_28 = (res_OrLogicOP_28 || res_ImpliesLogicOp_29);
    bool res_AndLogicOP_60 = true;
    res_AndLogicOP_60 = (res_AndLogicOP_60 && (L_P1__GetInSubcl8(my_id) == true));
    bool res_NotLogicOP_61 = true;
    res_NotLogicOP_61 = (res_NotLogicOP_61 && ! (L_P1__GetSubcl28(my_id) < 4u));
    res_AndLogicOP_60 = (res_AndLogicOP_60 && res_NotLogicOP_61);
    
    res_OrLogicOP_28 = (res_OrLogicOP_28 || res_AndLogicOP_60);
    
    res_ImpliesLogicOp_14 = (res_ImpliesLogicOp_14 && res_OrLogicOP_28);
    }
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_ImpliesLogicOp_14);
    bool res_AndLogicOP_62 = true;
    bool res_AndLogicOP_63 = true;
    bool res_NotLogicOP_64 = true;
    res_NotLogicOP_64 = (res_NotLogicOP_64 && ! (L_P1__GetInSubcl4(my_id) == true));
    res_AndLogicOP_63 = (res_AndLogicOP_63 && res_NotLogicOP_64);
    bool res_NotLogicOP_65 = true;
    res_NotLogicOP_65 = (res_NotLogicOP_65 && ! Timer_Scaduto(L_P1__GetSubcl36(my_id)));
    res_AndLogicOP_63 = (res_AndLogicOP_63 && res_NotLogicOP_65);
    
    res_AndLogicOP_62 = (res_AndLogicOP_62 && res_AndLogicOP_63);
    bool res_NotLogicOP_66 = true;
    res_NotLogicOP_66 = (res_NotLogicOP_66 && ! (Counter_GetValore(L_P1__GetSubcl41(my_id)) < 15u));
    res_AndLogicOP_62 = (res_AndLogicOP_62 && res_NotLogicOP_66);
    
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_AndLogicOP_62);
    
    res_ImpliesLogicOp_3 = (res_ImpliesLogicOp_3 && res_AndLogicOP_13);
    }
    if(res_ImpliesLogicOp_3){
    xorIndex_res_XorLogicOP_2 = (xorIndex_res_XorLogicOP_2 + 1);
    }
    bool res_NotLogicOP_67 = true;
    res_NotLogicOP_67 = (res_NotLogicOP_67 && ! (L_P1__GetInSubcl8(my_id) == true));
    if(res_NotLogicOP_67){
    xorIndex_res_XorLogicOP_2 = (xorIndex_res_XorLogicOP_2 + 1);
    }
    
    res_XorLogicOP_2 = (res_XorLogicOP_2 && (xorIndex_res_XorLogicOP_2 == 1));
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_XorLogicOP_2);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *47,48,52,*  *,*  il controllo SubClass_C2_controllo_C8 non sia  diverso da  True 
    //   *104,* o  che   l'argomento argomento_ave10 non  sia  uguale a c120 *,* 
    //   *104,* e  che  *35,*  il controllo SubClass_C2_controllo_C8 sia  uguale a  False 
    //   *104,* o  che   l'argomento argomento_ave10 sia  uguale a c120 *39,* 
    //   *104,* e  che  *34,*  il parametro SubClass_C2_parametro_P6 sia  maggiore di  *54,* 8
    bool res_OrLogicOP_68 = false;
    bool res_OrLogicOP_69 = false;
    bool res_NotLogicOP_70 = true;
    bool res_NotLogicOP_71 = true;
    res_NotLogicOP_71 = (res_NotLogicOP_71 && ! (L_P1__GetInSubcl8(my_id) == true));
    res_NotLogicOP_70 = (res_NotLogicOP_70 && ! res_NotLogicOP_71);
    res_OrLogicOP_69 = (res_OrLogicOP_69 || res_NotLogicOP_70);
    bool res_AndLogicOP_72 = true;
    bool res_NotLogicOP_73 = true;
    res_NotLogicOP_73 = (res_NotLogicOP_73 && ! (argom59 == c120));
    res_AndLogicOP_72 = (res_AndLogicOP_72 && res_NotLogicOP_73);
    res_AndLogicOP_72 = (res_AndLogicOP_72 && (L_P1__GetInSubcl8(my_id) == false));
    
    res_OrLogicOP_69 = (res_OrLogicOP_69 || res_AndLogicOP_72);
    
    res_OrLogicOP_68 = (res_OrLogicOP_68 || res_OrLogicOP_69);
    bool res_AndLogicOP_74 = true;
    res_AndLogicOP_74 = (res_AndLogicOP_74 && (argom59 == c120));
    res_AndLogicOP_74 = (res_AndLogicOP_74 && (L_P1__GetParamSubcl12(my_id) > 8u));
    
    res_OrLogicOP_68 = (res_OrLogicOP_68 || res_AndLogicOP_74);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_68);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
    
    { commento: {41,}  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a c270 commento: {37,} e  se la variabile SubClass_C2_variabile_V9 è  minore di  commento: {55,} 1 commento: {36,} e  se il timer SubClass_C2_timer_T2 è scaduto, Verifica che   commento: {50,52,}  commento: {,}  la variabile SubClass_C2_variabile_V2 sia  diverso da  True 
     commento: {104,} e  che   l'argomento argomento_ave4 non  sia  uguale a GialloGiallo commento: {,} 
    
    
    }
*/
bool L_P1__Macro21(instance_id_t const my_id , C2_Enumerat2 argom62, C2_Enumerat2 argom63, C2_Enumerat3 argom64, C2_Enumerat2 argom65, bool argom66)
{
bool res_AndLogicOP_0 = true;
    
    //  *41,*  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a c270 *37,* e  se la variabile SubClass_C2_variabile_V9 è  minore di  *55,* 1 *36,* e  se il timer SubClass_C2_timer_T2 è scaduto, Verifica che   *50,52,*  *,*  la variabile SubClass_C2_variabile_V2 sia  diverso da  True 
    //   *104,* e  che   l'argomento argomento_ave4 non  sia  uguale a GialloGiallo
    bool res_ImpliesLogicOp_1 = true;
    bool res_AndLogicOP_2 = true;
    bool res_AndLogicOP_3 = true;
    bool res_ForAllPredicate_4 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl9Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl9(my_id,i);
    bool res_ImpliesLogicOp_5 = true;
    res_ImpliesLogicOp_5 = (res_ImpliesLogicOp_5 && (L_P1__GetParamMainc5(it.mainc45) == c270));
    res_ForAllPredicate_4 = res_ImpliesLogicOp_5;
    if(!res_ForAllPredicate_4) {break;}
    }
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_ForAllPredicate_4);
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (L_P1__GetSubcl28(my_id) < 1u));
    
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_AndLogicOP_3);
    res_AndLogicOP_2 = (res_AndLogicOP_2 && Timer_Scaduto(L_P1__GetSubcl36(my_id)));
    
    if(res_AndLogicOP_2){
    bool res_AndLogicOP_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetSubcl27(my_id) == true));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_7);
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (argom62 == giallogiall));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_8);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_AndLogicOP_6);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
    
    { commento: {61,} commento: {45,}  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  commento: {105,} è  maggiore di  commento: {54,} 11 e  se l'argomento argomento_ave3 è  diverso da Rosso commento: {39,}  commento: {34,} e  se il parametro SubClass_C2_parametro_P3 è  diverso da  commento: {56,} 7 commento: {35,} o  se il controllo SubClass_C2_controllo_C8 è  uguale a  True  commento: {35,} o  se il controllo SubClass_C2_controllo_C8 non è  uguale a  False , Tutte le seguenti { 
     commento: {61,} commento: {34,}  se il parametro SubClass_C2_parametro_P3 non è  maggiore di  commento: {54,} 4 commento: {37,} o  se la variabile SubClass_C2_variabile_V2 è  diverso da  True , Tutte le seguenti { 
     commento: {61,} commento: {37,}  se la variabile SubClass_C2_variabile_V2 è  diverso da  False  commento: {38,} e  se il contatore SubClass_C2_contatore_Co2 è  diverso da  commento: {56,} 14 commento: {36,} e  se il timer SubClass_C2_timer_T6 è disattivo commento: {38,} o  se il contatore SubClass_C2_contatore_Co8 è  maggiore di  commento: {54,} 15450, Tutte le seguenti { 
     commento: {61,} commento: {45,}  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a  commento: {53,} 15 commento: {38,} e  se il contatore SubClass_C2_contatore_Co5 non è  maggiore di  commento: {54,} 14213 commento: {38,} e  se il contatore SubClass_C2_contatore_Co8 è  diverso da  commento: {56,} 124 commento: {37,} e  se la variabile SubClass_C2_variabile_V9 non è  diverso da  commento: {56,} 5 commento: {37,} o  se la variabile SubClass_C2_variabile_V2 non è  diverso da  True , Tutte le seguenti { 
     commento: {63,}  se l'argomento argomento_ave4 è  diverso da c120 commento: {39,}  commento: {38,} e  se il contatore SubClass_C2_contatore_Co5 non è  uguale a  commento: {53,} 145 commento: {37,} e  se la variabile SubClass_C2_variabile_V9 non è  maggiore di  commento: {54,} 5 e  se l'argomento argomento_ave1 è  diverso da  True  commento: {39,}  commento: {34,} e  se il parametro SubClass_C2_parametro_P6 è  maggiore di  commento: {54,} 3 commento: {34,} o  se il parametro SubClass_C2_parametro_P3 è  diverso da  commento: {56,} 7, Solo una delle seguenti { 
     commento: {63,} commento: {45,}  se  MainClass_C1_contatore_Co7 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  commento: {105,} è  maggiore di  commento: {54,} 1402, Solo una delle seguenti { 
     commento: {61,} commento: {109,}  se il ripristino della variabile  SubClass_C2_restoreva_RV1 non è  diverso da c270x commento: {34,} e  se il parametro SubClass_C2_parametro_P3 è  uguale a  commento: {53,} 5 commento: {34,} e  se il parametro SubClass_C2_parametro_P3 non è  minore di  commento: {55,} 4 commento: {37,} o  se la variabile SubClass_C2_variabile_V2 è  diverso da  False  commento: {36,} o  se il timer SubClass_C2_timer_T8 è disattivo, Tutte le seguenti { 
     commento: {61,} commento: {110,}  se il ripristino del timer  SubClass_C2_restoreTI_TI2 è disattivo, Tutte le seguenti { 
     commento: {62,} commento: {34,}  se il parametro SubClass_C2_parametro_P6 è  uguale a  commento: {53,} 3 commento: {36,} e  se il timer SubClass_C2_timer_T2 non è disattivo, Almeno una delle seguenti { 
     commento: {34,}  se il parametro SubClass_C2_parametro_P3 è  diverso da  commento: {56,} 6, Verifica che   commento: {47,50,52,}  commento: {,}  la variabile SubClass_C2_variabile_V9 sia  uguale a  commento: {53,} 9
     commento: {104,} e  che   l'argomento argomento_ave2 non  sia  uguale a  False  commento: {,} 
     commento: {104,} o  che   l'argomento argomento_ave1 non  sia  uguale a  True  commento: {39,} 
     commento: {104,} o  che   l'argomento argomento_ave1 sia  uguale a  False  commento: {39,} 
     commento: {104,} e  che  commento: {34,}  il parametro SubClass_C2_parametro_P3 sia  minore di  commento: {55,} 5
    
    
     } Verifica che   commento: {50,51,}  commento: {,}  il contatore SubClass_C2_contatore_Co2 sia  maggiore di  commento: {54,} 1513
     commento: {104,} o  che  commento: {38,}  il contatore SubClass_C2_contatore_Co5 non sia  diverso da  commento: {56,} 11
     commento: {104,} e  che  commento: {,}  la variabile SubClass_C2_variabile_V9 sia  diverso da  commento: {56,} 4
     commento: {104,} e  che  commento: {37,}  la variabile SubClass_C2_variabile_V2 non sia  uguale a  True 
     commento: {104,} e  che  commento: {38,}  il contatore SubClass_C2_contatore_Co5 non sia  uguale a  commento: {53,} 11
    
    
     } Verifica che   commento: {50,52,}   l'argomento argomento_ave1 non  sia  uguale a  True  commento: {,} 
     commento: {104,} e  che  commento: {,}  la variabile SubClass_C2_variabile_V2 non sia  diverso da  False 
    
    
     } Verifica che   commento: {47,48,49,50,51,}  commento: {,}  la variabile SubClass_C2_variabile_V2 non sia  uguale a  True 
     commento: {104,} e  che  commento: {,}  il timer SubClass_C2_timer_T2 non sia scaduto
     commento: {104,} e  che  commento: {,}  il controllo SubClass_C2_controllo_C1 non sia  uguale a  False 
     commento: {104,} o  che  commento: {34,}  il parametro SubClass_C2_parametro_P3 sia  diverso da  commento: {56,} 1
     commento: {104,} e  che  commento: {,}  il contatore SubClass_C2_contatore_Co5 non sia  maggiore di  commento: {54,} 134
     commento: {104,} e  che  commento: {38,}  il contatore SubClass_C2_contatore_Co5 non sia  diverso da  commento: {56,} 135
    
    
     } Verifica che   commento: {51,}  commento: {,}  il contatore SubClass_C2_contatore_Co5 sia  diverso da  commento: {56,} 1302
    
    
     } Verifica che   commento: {47,49,50,51,}  commento: {,}  la variabile SubClass_C2_variabile_V2 non sia  diverso da  True 
     commento: {104,} e  che  commento: {,}  il contatore SubClass_C2_contatore_Co5 sia  maggiore di  commento: {54,} 13
     commento: {104,} e  che  commento: {34,}  il parametro SubClass_C2_parametro_P6 sia  maggiore di  commento: {54,} 10
     commento: {104,} e  che  commento: {,}  il timer SubClass_C2_timer_T2 sia attivo
    
    
     } Verifica che   commento: {51,}  commento: {,}  il contatore SubClass_C2_contatore_Co8 sia  minore di  commento: {55,} 13
    
    
     } Verifica che   commento: {49,}  commento: {,}  il timer SubClass_C2_timer_T2 sia scaduto
    
    
     } Verifica che   commento: {47,48,49,51,}  commento: {,}  il contatore SubClass_C2_contatore_Co2 sia  diverso da  commento: {56,} 154
     commento: {104,} o  che  commento: {,}  il controllo SubClass_C2_controllo_C8 non sia  diverso da  False 
     commento: {104,} e  che  commento: {34,}  il parametro SubClass_C2_parametro_P6 sia  minore di  commento: {55,} 8
     commento: {104,} o  che  commento: {,}  il timer SubClass_C2_timer_T2 non sia disattivo
    
    
     } Verifica che   commento: {47,51,52,}  commento: {34,}  il parametro SubClass_C2_parametro_P3 non sia  diverso da  commento: {56,} 4
     commento: {104,} o  che  commento: {,}  il contatore SubClass_C2_contatore_Co5 non sia  maggiore di  commento: {54,} 115021
     commento: {104,} e  che   l'argomento argomento_ave4 non  sia  uguale a c120 commento: {,} 
    
    
    }
*/
bool L_P1__Macro22(instance_id_t const my_id , bool argom67, bool argom68, C2_Enumerat1 argom69, C2_Enumerat4 argom70)
{
bool res_AndLogicOP_0 = true;
    
    //  *61,* *45,*  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  *105,* è  maggiore di  *54,* 11 e  se l'argomento argomento_ave3 è  diverso da Rosso *39,*  *34,* e  se il parametro SubClass_C2_parametro_P3 è  diverso da  *56,* 7 *35,* o  se il controllo SubClass_C2_controllo_C8 è  uguale a  True  *35,* o  se il controllo SubClass_C2_controllo_C8 non è  uguale a  False , Tutte le seguenti { 
    //   *61,* *34,*  se il parametro SubClass_C2_parametro_P3 non è  maggiore di  *54,* 4 *37,* o  se la variabile SubClass_C2_variabile_V2 è  diverso da  True , Tutte le seguenti { 
    //   *61,* *37,*  se la variabile SubClass_C2_variabile_V2 è  diverso da  False  *38,* e  se il contatore SubClass_C2_contatore_Co2 è  diverso da  *56,* 14 *36,* e  se il timer SubClass_C2_timer_T6 è disattivo *38,* o  se il contatore SubClass_C2_contatore_Co8 è  maggiore di  *54,* 15450, Tutte le seguenti { 
    //   *61,* *45,*  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a  *53,* 15 *38,* e  se il contatore SubClass_C2_contatore_Co5 non è  maggiore di  *54,* 14213 *38,* e  se il contatore SubClass_C2_contatore_Co8 è  diverso da  *56,* 124 *37,* e  se la variabile SubClass_C2_variabile_V9 non è  diverso da  *56,* 5 *37,* o  se la variabile SubClass_C2_variabile_V2 non è  diverso da  True , Tutte le seguenti { 
    //   *63,*  se l'argomento argomento_ave4 è  diverso da c120 *39,*  *38,* e  se il contatore SubClass_C2_contatore_Co5 non è  uguale a  *53,* 145 *37,* e  se la variabile SubClass_C2_variabile_V9 non è  maggiore di  *54,* 5 e  se l'argomento argomento_ave1 è  diverso da  True  *39,*  *34,* e  se il parametro SubClass_C2_parametro_P6 è  maggiore di  *54,* 3 *34,* o  se il parametro SubClass_C2_parametro_P3 è  diverso da  *56,* 7, Solo una delle seguenti { 
    //   *63,* *45,*  se  MainClass_C1_contatore_Co7 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  *105,* è  maggiore di  *54,* 1402, Solo una delle seguenti { 
    //   *61,* *109,*  se il ripristino della variabile  SubClass_C2_restoreva_RV1 non è  diverso da c270x *34,* e  se il parametro SubClass_C2_parametro_P3 è  uguale a  *53,* 5 *34,* e  se il parametro SubClass_C2_parametro_P3 non è  minore di  *55,* 4 *37,* o  se la variabile SubClass_C2_variabile_V2 è  diverso da  False  *36,* o  se il timer SubClass_C2_timer_T8 è disattivo, Tutte le seguenti { 
    //   *61,* *110,*  se il ripristino del timer  SubClass_C2_restoreTI_TI2 è disattivo, Tutte le seguenti { 
    //   *62,* *34,*  se il parametro SubClass_C2_parametro_P6 è  uguale a  *53,* 3 *36,* e  se il timer SubClass_C2_timer_T2 non è disattivo, Almeno una delle seguenti { 
    //   *34,*  se il parametro SubClass_C2_parametro_P3 è  diverso da  *56,* 6, Verifica che   *47,50,52,*  *,*  la variabile SubClass_C2_variabile_V9 sia  uguale a  *53,* 9
    //   *104,* e  che   l'argomento argomento_ave2 non  sia  uguale a  False  *,* 
    //   *104,* o  che   l'argomento argomento_ave1 non  sia  uguale a  True  *39,* 
    //   *104,* o  che   l'argomento argomento_ave1 sia  uguale a  False  *39,* 
    //   *104,* e  che  *34,*  il parametro SubClass_C2_parametro_P3 sia  minore di  *55,* 5
    //   } Verifica che   *50,51,*  *,*  il contatore SubClass_C2_contatore_Co2 sia  maggiore di  *54,* 1513
    //   *104,* o  che  *38,*  il contatore SubClass_C2_contatore_Co5 non sia  diverso da  *56,* 11
    //   *104,* e  che  *,*  la variabile SubClass_C2_variabile_V9 sia  diverso da  *56,* 4
    //   *104,* e  che  *37,*  la variabile SubClass_C2_variabile_V2 non sia  uguale a  True 
    //   *104,* e  che  *38,*  il contatore SubClass_C2_contatore_Co5 non sia  uguale a  *53,* 11
    //   } Verifica che   *50,52,*   l'argomento argomento_ave1 non  sia  uguale a  True  *,* 
    //   *104,* e  che  *,*  la variabile SubClass_C2_variabile_V2 non sia  diverso da  False 
    //   } Verifica che   *47,48,49,50,51,*  *,*  la variabile SubClass_C2_variabile_V2 non sia  uguale a  True 
    //   *104,* e  che  *,*  il timer SubClass_C2_timer_T2 non sia scaduto
    //   *104,* e  che  *,*  il controllo SubClass_C2_controllo_C1 non sia  uguale a  False 
    //   *104,* o  che  *34,*  il parametro SubClass_C2_parametro_P3 sia  diverso da  *56,* 1
    //   *104,* e  che  *,*  il contatore SubClass_C2_contatore_Co5 non sia  maggiore di  *54,* 134
    //   *104,* e  che  *38,*  il contatore SubClass_C2_contatore_Co5 non sia  diverso da  *56,* 135
    //   } Verifica che   *51,*  *,*  il contatore SubClass_C2_contatore_Co5 sia  diverso da  *56,* 1302
    //   } Verifica che   *47,49,50,51,*  *,*  la variabile SubClass_C2_variabile_V2 non sia  diverso da  True 
    //   *104,* e  che  *,*  il contatore SubClass_C2_contatore_Co5 sia  maggiore di  *54,* 13
    //   *104,* e  che  *34,*  il parametro SubClass_C2_parametro_P6 sia  maggiore di  *54,* 10
    //   *104,* e  che  *,*  il timer SubClass_C2_timer_T2 sia attivo
    //   } Verifica che   *51,*  *,*  il contatore SubClass_C2_contatore_Co8 sia  minore di  *55,* 13
    //   } Verifica che   *49,*  *,*  il timer SubClass_C2_timer_T2 sia scaduto
    //   } Verifica che   *47,48,49,51,*  *,*  il contatore SubClass_C2_contatore_Co2 sia  diverso da  *56,* 154
    //   *104,* o  che  *,*  il controllo SubClass_C2_controllo_C8 non sia  diverso da  False 
    //   *104,* e  che  *34,*  il parametro SubClass_C2_parametro_P6 sia  minore di  *55,* 8
    //   *104,* o  che  *,*  il timer SubClass_C2_timer_T2 non sia disattivo
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_AndLogicOP_4 = true;
    bool res_AndLogicOP_5 = true;
    bool res_ForAllPredicateNotEmpty_6 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl10Length(my_id); ++i)
    {
    L_P1__Recor1 it = L_P1__GetRecSubcl10(my_id,i);
    bool res_ImpliesLogicOp_7 = true;
    res_ImpliesLogicOp_7 = (res_ImpliesLogicOp_7 && (Counter_GetValore(L_P1__GetMainc43(it.mainc46)) > 11u));
    res_ForAllPredicateNotEmpty_6 = res_ImpliesLogicOp_7;
    if(!res_ForAllPredicateNotEmpty_6) {break;}
    }
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_ForAllPredicateNotEmpty_6);
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (argom69 == rosso));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_8);
    
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_AndLogicOP_5);
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetParamSubcl11(my_id) == 7u));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_9);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_AndLogicOP_4);
    res_OrLogicOP_3 = (res_OrLogicOP_3 || (L_P1__GetInSubcl8(my_id) == true));
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__GetInSubcl8(my_id) == false));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_10);
    
    if(res_OrLogicOP_2){
    bool res_AndLogicOP_11 = true;
    bool res_ImpliesLogicOp_12 = true;
    bool res_OrLogicOP_13 = false;
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1__GetParamSubcl11(my_id) > 4u));
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_NotLogicOP_14);
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (L_P1__GetSubcl27(my_id) == true));
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_NotLogicOP_15);
    
    if(res_OrLogicOP_13){
    bool res_AndLogicOP_16 = true;
    bool res_ImpliesLogicOp_17 = true;
    bool res_OrLogicOP_18 = false;
    bool res_AndLogicOP_19 = true;
    bool res_AndLogicOP_20 = true;
    bool res_NotLogicOP_21 = true;
    res_NotLogicOP_21 = (res_NotLogicOP_21 && ! (L_P1__GetSubcl27(my_id) == false));
    res_AndLogicOP_20 = (res_AndLogicOP_20 && res_NotLogicOP_21);
    bool res_NotLogicOP_22 = true;
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! (Counter_GetValore(L_P1__GetSubcl40(my_id)) == 14u));
    res_AndLogicOP_20 = (res_AndLogicOP_20 && res_NotLogicOP_22);
    
    res_AndLogicOP_19 = (res_AndLogicOP_19 && res_AndLogicOP_20);
    res_AndLogicOP_19 = (res_AndLogicOP_19 && Timer_Disattivo(L_P1__GetSubcl37(my_id)));
    
    res_OrLogicOP_18 = (res_OrLogicOP_18 || res_AndLogicOP_19);
    res_OrLogicOP_18 = (res_OrLogicOP_18 || (Counter_GetValore(L_P1__GetSubcl42(my_id)) > 15450u));
    
    if(res_OrLogicOP_18){
    bool res_AndLogicOP_23 = true;
    bool res_ImpliesLogicOp_24 = true;
    bool res_OrLogicOP_25 = false;
    bool res_AndLogicOP_26 = true;
    bool res_AndLogicOP_27 = true;
    bool res_AndLogicOP_28 = true;
    bool res_ForAllPredicate_29 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl9Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl9(my_id,i);
    bool res_ImpliesLogicOp_30 = true;
    res_ImpliesLogicOp_30 = (res_ImpliesLogicOp_30 && (Counter_GetValore(L_P1__GetMainc43(it.mainc45)) == 15u));
    res_ForAllPredicate_29 = res_ImpliesLogicOp_30;
    if(!res_ForAllPredicate_29) {break;}
    }
    res_AndLogicOP_28 = (res_AndLogicOP_28 && res_ForAllPredicate_29);
    bool res_NotLogicOP_31 = true;
    res_NotLogicOP_31 = (res_NotLogicOP_31 && ! (Counter_GetValore(L_P1__GetSubcl41(my_id)) > 14213u));
    res_AndLogicOP_28 = (res_AndLogicOP_28 && res_NotLogicOP_31);
    
    res_AndLogicOP_27 = (res_AndLogicOP_27 && res_AndLogicOP_28);
    bool res_NotLogicOP_32 = true;
    res_NotLogicOP_32 = (res_NotLogicOP_32 && ! (Counter_GetValore(L_P1__GetSubcl42(my_id)) == 124u));
    res_AndLogicOP_27 = (res_AndLogicOP_27 && res_NotLogicOP_32);
    
    res_AndLogicOP_26 = (res_AndLogicOP_26 && res_AndLogicOP_27);
    bool res_NotLogicOP_33 = true;
    bool res_NotLogicOP_34 = true;
    res_NotLogicOP_34 = (res_NotLogicOP_34 && ! (L_P1__GetSubcl28(my_id) == 5u));
    res_NotLogicOP_33 = (res_NotLogicOP_33 && ! res_NotLogicOP_34);
    res_AndLogicOP_26 = (res_AndLogicOP_26 && res_NotLogicOP_33);
    
    res_OrLogicOP_25 = (res_OrLogicOP_25 || res_AndLogicOP_26);
    bool res_NotLogicOP_35 = true;
    bool res_NotLogicOP_36 = true;
    res_NotLogicOP_36 = (res_NotLogicOP_36 && ! (L_P1__GetSubcl27(my_id) == true));
    res_NotLogicOP_35 = (res_NotLogicOP_35 && ! res_NotLogicOP_36);
    res_OrLogicOP_25 = (res_OrLogicOP_25 || res_NotLogicOP_35);
    
    if(res_OrLogicOP_25){
    bool res_AndLogicOP_37 = true;
    bool res_ImpliesLogicOp_38 = true;
    bool res_OrLogicOP_39 = false;
    bool res_AndLogicOP_40 = true;
    bool res_AndLogicOP_41 = true;
    bool res_AndLogicOP_42 = true;
    bool res_AndLogicOP_43 = true;
    bool res_NotLogicOP_44 = true;
    res_NotLogicOP_44 = (res_NotLogicOP_44 && ! (argom70 == c120));
    res_AndLogicOP_43 = (res_AndLogicOP_43 && res_NotLogicOP_44);
    bool res_NotLogicOP_45 = true;
    res_NotLogicOP_45 = (res_NotLogicOP_45 && ! (Counter_GetValore(L_P1__GetSubcl41(my_id)) == 145u));
    res_AndLogicOP_43 = (res_AndLogicOP_43 && res_NotLogicOP_45);
    
    res_AndLogicOP_42 = (res_AndLogicOP_42 && res_AndLogicOP_43);
    bool res_NotLogicOP_46 = true;
    res_NotLogicOP_46 = (res_NotLogicOP_46 && ! (L_P1__GetSubcl28(my_id) > 5u));
    res_AndLogicOP_42 = (res_AndLogicOP_42 && res_NotLogicOP_46);
    
    res_AndLogicOP_41 = (res_AndLogicOP_41 && res_AndLogicOP_42);
    bool res_NotLogicOP_47 = true;
    res_NotLogicOP_47 = (res_NotLogicOP_47 && ! (argom67 == true));
    res_AndLogicOP_41 = (res_AndLogicOP_41 && res_NotLogicOP_47);
    
    res_AndLogicOP_40 = (res_AndLogicOP_40 && res_AndLogicOP_41);
    res_AndLogicOP_40 = (res_AndLogicOP_40 && (L_P1__GetParamSubcl12(my_id) > 3u));
    
    res_OrLogicOP_39 = (res_OrLogicOP_39 || res_AndLogicOP_40);
    bool res_NotLogicOP_48 = true;
    res_NotLogicOP_48 = (res_NotLogicOP_48 && ! (L_P1__GetParamSubcl11(my_id) == 7u));
    res_OrLogicOP_39 = (res_OrLogicOP_39 || res_NotLogicOP_48);
    
    if(res_OrLogicOP_39){
    bool res_XorLogicOP_49 = true;
    int xorIndex_res_XorLogicOP_49 = 0;
    bool res_ImpliesLogicOp_50 = true;
    bool res_ForAllPredicateNotEmpty_51 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl9Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl9(my_id,i);
    bool res_ImpliesLogicOp_52 = true;
    res_ImpliesLogicOp_52 = (res_ImpliesLogicOp_52 && (Counter_GetValore(L_P1__GetMainc44(it.mainc45)) > 1402u));
    res_ForAllPredicateNotEmpty_51 = res_ImpliesLogicOp_52;
    if(!res_ForAllPredicateNotEmpty_51) {break;}
    }
    if(res_ForAllPredicateNotEmpty_51){
    bool res_XorLogicOP_53 = true;
    int xorIndex_res_XorLogicOP_53 = 0;
    bool res_ImpliesLogicOp_54 = true;
    bool res_OrLogicOP_55 = false;
    bool res_OrLogicOP_56 = false;
    bool res_AndLogicOP_57 = true;
    bool res_AndLogicOP_58 = true;
    bool res_NotLogicOP_59 = true;
    bool res_NotLogicOP_60 = true;
    res_NotLogicOP_60 = (res_NotLogicOP_60 && ! (L_P1__GetSubcl22(my_id) == c270x));
    res_NotLogicOP_59 = (res_NotLogicOP_59 && ! res_NotLogicOP_60);
    res_AndLogicOP_58 = (res_AndLogicOP_58 && res_NotLogicOP_59);
    res_AndLogicOP_58 = (res_AndLogicOP_58 && (L_P1__GetParamSubcl11(my_id) == 5u));
    
    res_AndLogicOP_57 = (res_AndLogicOP_57 && res_AndLogicOP_58);
    bool res_NotLogicOP_61 = true;
    res_NotLogicOP_61 = (res_NotLogicOP_61 && ! (L_P1__GetParamSubcl11(my_id) < 4u));
    res_AndLogicOP_57 = (res_AndLogicOP_57 && res_NotLogicOP_61);
    
    res_OrLogicOP_56 = (res_OrLogicOP_56 || res_AndLogicOP_57);
    bool res_NotLogicOP_62 = true;
    res_NotLogicOP_62 = (res_NotLogicOP_62 && ! (L_P1__GetSubcl27(my_id) == false));
    res_OrLogicOP_56 = (res_OrLogicOP_56 || res_NotLogicOP_62);
    
    res_OrLogicOP_55 = (res_OrLogicOP_55 || res_OrLogicOP_56);
    res_OrLogicOP_55 = (res_OrLogicOP_55 || Timer_Disattivo(L_P1__GetSubcl38(my_id)));
    
    if(res_OrLogicOP_55){
    bool res_AndLogicOP_63 = true;
    bool res_ImpliesLogicOp_64 = true;
    if(Timer_Disattivo(L_P1__GetSubcl32(my_id))){
    bool res_AndLogicOP_65 = true;
    bool res_ImpliesLogicOp_66 = true;
    bool res_AndLogicOP_67 = true;
    res_AndLogicOP_67 = (res_AndLogicOP_67 && (L_P1__GetParamSubcl12(my_id) == 3u));
    bool res_NotLogicOP_68 = true;
    res_NotLogicOP_68 = (res_NotLogicOP_68 && ! Timer_Disattivo(L_P1__GetSubcl36(my_id)));
    res_AndLogicOP_67 = (res_AndLogicOP_67 && res_NotLogicOP_68);
    
    if(res_AndLogicOP_67){
    bool res_ImpliesLogicOp_69 = true;
    bool res_NotLogicOP_70 = true;
    res_NotLogicOP_70 = (res_NotLogicOP_70 && ! (L_P1__GetParamSubcl11(my_id) == 6u));
    if(res_NotLogicOP_70){
    bool res_OrLogicOP_71 = false;
    bool res_OrLogicOP_72 = false;
    bool res_AndLogicOP_73 = true;
    res_AndLogicOP_73 = (res_AndLogicOP_73 && (L_P1__GetSubcl28(my_id) == 9u));
    bool res_NotLogicOP_74 = true;
    res_NotLogicOP_74 = (res_NotLogicOP_74 && ! (argom68 == false));
    res_AndLogicOP_73 = (res_AndLogicOP_73 && res_NotLogicOP_74);
    
    res_OrLogicOP_72 = (res_OrLogicOP_72 || res_AndLogicOP_73);
    bool res_NotLogicOP_75 = true;
    res_NotLogicOP_75 = (res_NotLogicOP_75 && ! (argom67 == true));
    res_OrLogicOP_72 = (res_OrLogicOP_72 || res_NotLogicOP_75);
    
    res_OrLogicOP_71 = (res_OrLogicOP_71 || res_OrLogicOP_72);
    bool res_AndLogicOP_76 = true;
    res_AndLogicOP_76 = (res_AndLogicOP_76 && (argom67 == false));
    res_AndLogicOP_76 = (res_AndLogicOP_76 && (L_P1__GetParamSubcl11(my_id) < 5u));
    
    res_OrLogicOP_71 = (res_OrLogicOP_71 || res_AndLogicOP_76);
    
    res_ImpliesLogicOp_69 = (res_ImpliesLogicOp_69 && res_OrLogicOP_71);
    }
    res_ImpliesLogicOp_66 = (res_ImpliesLogicOp_66 && res_ImpliesLogicOp_69);
    }
    res_AndLogicOP_65 = (res_AndLogicOP_65 && res_ImpliesLogicOp_66);
    bool res_OrLogicOP_77 = false;
    res_OrLogicOP_77 = (res_OrLogicOP_77 || (Counter_GetValore(L_P1__GetSubcl40(my_id)) > 1513u));
    bool res_AndLogicOP_78 = true;
    bool res_AndLogicOP_79 = true;
    bool res_AndLogicOP_80 = true;
    bool res_NotLogicOP_81 = true;
    bool res_NotLogicOP_82 = true;
    res_NotLogicOP_82 = (res_NotLogicOP_82 && ! (Counter_GetValore(L_P1__GetSubcl41(my_id)) == 11u));
    res_NotLogicOP_81 = (res_NotLogicOP_81 && ! res_NotLogicOP_82);
    res_AndLogicOP_80 = (res_AndLogicOP_80 && res_NotLogicOP_81);
    bool res_NotLogicOP_83 = true;
    res_NotLogicOP_83 = (res_NotLogicOP_83 && ! (L_P1__GetSubcl28(my_id) == 4u));
    res_AndLogicOP_80 = (res_AndLogicOP_80 && res_NotLogicOP_83);
    
    res_AndLogicOP_79 = (res_AndLogicOP_79 && res_AndLogicOP_80);
    bool res_NotLogicOP_84 = true;
    res_NotLogicOP_84 = (res_NotLogicOP_84 && ! (L_P1__GetSubcl27(my_id) == true));
    res_AndLogicOP_79 = (res_AndLogicOP_79 && res_NotLogicOP_84);
    
    res_AndLogicOP_78 = (res_AndLogicOP_78 && res_AndLogicOP_79);
    bool res_NotLogicOP_85 = true;
    res_NotLogicOP_85 = (res_NotLogicOP_85 && ! (Counter_GetValore(L_P1__GetSubcl41(my_id)) == 11u));
    res_AndLogicOP_78 = (res_AndLogicOP_78 && res_NotLogicOP_85);
    
    res_OrLogicOP_77 = (res_OrLogicOP_77 || res_AndLogicOP_78);
    
    res_AndLogicOP_65 = (res_AndLogicOP_65 && res_OrLogicOP_77);
    
    res_ImpliesLogicOp_64 = (res_ImpliesLogicOp_64 && res_AndLogicOP_65);
    }
    res_AndLogicOP_63 = (res_AndLogicOP_63 && res_ImpliesLogicOp_64);
    bool res_AndLogicOP_86 = true;
    bool res_NotLogicOP_87 = true;
    res_NotLogicOP_87 = (res_NotLogicOP_87 && ! (argom67 == true));
    res_AndLogicOP_86 = (res_AndLogicOP_86 && res_NotLogicOP_87);
    bool res_NotLogicOP_88 = true;
    bool res_NotLogicOP_89 = true;
    res_NotLogicOP_89 = (res_NotLogicOP_89 && ! (L_P1__GetSubcl27(my_id) == false));
    res_NotLogicOP_88 = (res_NotLogicOP_88 && ! res_NotLogicOP_89);
    res_AndLogicOP_86 = (res_AndLogicOP_86 && res_NotLogicOP_88);
    
    res_AndLogicOP_63 = (res_AndLogicOP_63 && res_AndLogicOP_86);
    
    res_ImpliesLogicOp_54 = (res_ImpliesLogicOp_54 && res_AndLogicOP_63);
    }
    if(res_ImpliesLogicOp_54){
    xorIndex_res_XorLogicOP_53 = (xorIndex_res_XorLogicOP_53 + 1);
    }
    bool res_OrLogicOP_90 = false;
    bool res_AndLogicOP_91 = true;
    bool res_AndLogicOP_92 = true;
    bool res_NotLogicOP_93 = true;
    res_NotLogicOP_93 = (res_NotLogicOP_93 && ! (L_P1__GetSubcl27(my_id) == true));
    res_AndLogicOP_92 = (res_AndLogicOP_92 && res_NotLogicOP_93);
    bool res_NotLogicOP_94 = true;
    res_NotLogicOP_94 = (res_NotLogicOP_94 && ! Timer_Scaduto(L_P1__GetSubcl36(my_id)));
    res_AndLogicOP_92 = (res_AndLogicOP_92 && res_NotLogicOP_94);
    
    res_AndLogicOP_91 = (res_AndLogicOP_91 && res_AndLogicOP_92);
    bool res_NotLogicOP_95 = true;
    res_NotLogicOP_95 = (res_NotLogicOP_95 && ! (L_P1__GetInSubcl4(my_id) == false));
    res_AndLogicOP_91 = (res_AndLogicOP_91 && res_NotLogicOP_95);
    
    res_OrLogicOP_90 = (res_OrLogicOP_90 || res_AndLogicOP_91);
    bool res_AndLogicOP_96 = true;
    bool res_AndLogicOP_97 = true;
    bool res_NotLogicOP_98 = true;
    res_NotLogicOP_98 = (res_NotLogicOP_98 && ! (L_P1__GetParamSubcl11(my_id) == 1u));
    res_AndLogicOP_97 = (res_AndLogicOP_97 && res_NotLogicOP_98);
    bool res_NotLogicOP_99 = true;
    res_NotLogicOP_99 = (res_NotLogicOP_99 && ! (Counter_GetValore(L_P1__GetSubcl41(my_id)) > 134u));
    res_AndLogicOP_97 = (res_AndLogicOP_97 && res_NotLogicOP_99);
    
    res_AndLogicOP_96 = (res_AndLogicOP_96 && res_AndLogicOP_97);
    bool res_NotLogicOP_100 = true;
    bool res_NotLogicOP_101 = true;
    res_NotLogicOP_101 = (res_NotLogicOP_101 && ! (Counter_GetValore(L_P1__GetSubcl41(my_id)) == 135u));
    res_NotLogicOP_100 = (res_NotLogicOP_100 && ! res_NotLogicOP_101);
    res_AndLogicOP_96 = (res_AndLogicOP_96 && res_NotLogicOP_100);
    
    res_OrLogicOP_90 = (res_OrLogicOP_90 || res_AndLogicOP_96);
    
    if(res_OrLogicOP_90){
    xorIndex_res_XorLogicOP_53 = (xorIndex_res_XorLogicOP_53 + 1);
    }
    
    res_XorLogicOP_53 = (res_XorLogicOP_53 && (xorIndex_res_XorLogicOP_53 == 1));
    res_ImpliesLogicOp_50 = (res_ImpliesLogicOp_50 && res_XorLogicOP_53);
    }
    if(res_ImpliesLogicOp_50){
    xorIndex_res_XorLogicOP_49 = (xorIndex_res_XorLogicOP_49 + 1);
    }
    bool res_NotLogicOP_102 = true;
    res_NotLogicOP_102 = (res_NotLogicOP_102 && ! (Counter_GetValore(L_P1__GetSubcl41(my_id)) == 1302u));
    if(res_NotLogicOP_102){
    xorIndex_res_XorLogicOP_49 = (xorIndex_res_XorLogicOP_49 + 1);
    }
    
    res_XorLogicOP_49 = (res_XorLogicOP_49 && (xorIndex_res_XorLogicOP_49 == 1));
    res_ImpliesLogicOp_38 = (res_ImpliesLogicOp_38 && res_XorLogicOP_49);
    }
    res_AndLogicOP_37 = (res_AndLogicOP_37 && res_ImpliesLogicOp_38);
    bool res_AndLogicOP_103 = true;
    bool res_AndLogicOP_104 = true;
    bool res_AndLogicOP_105 = true;
    bool res_NotLogicOP_106 = true;
    bool res_NotLogicOP_107 = true;
    res_NotLogicOP_107 = (res_NotLogicOP_107 && ! (L_P1__GetSubcl27(my_id) == true));
    res_NotLogicOP_106 = (res_NotLogicOP_106 && ! res_NotLogicOP_107);
    res_AndLogicOP_105 = (res_AndLogicOP_105 && res_NotLogicOP_106);
    res_AndLogicOP_105 = (res_AndLogicOP_105 && (Counter_GetValore(L_P1__GetSubcl41(my_id)) > 13u));
    
    res_AndLogicOP_104 = (res_AndLogicOP_104 && res_AndLogicOP_105);
    res_AndLogicOP_104 = (res_AndLogicOP_104 && (L_P1__GetParamSubcl12(my_id) > 10u));
    
    res_AndLogicOP_103 = (res_AndLogicOP_103 && res_AndLogicOP_104);
    res_AndLogicOP_103 = (res_AndLogicOP_103 && Timer_Attivo(L_P1__GetSubcl36(my_id)));
    
    res_AndLogicOP_37 = (res_AndLogicOP_37 && res_AndLogicOP_103);
    
    res_ImpliesLogicOp_24 = (res_ImpliesLogicOp_24 && res_AndLogicOP_37);
    }
    res_AndLogicOP_23 = (res_AndLogicOP_23 && res_ImpliesLogicOp_24);
    res_AndLogicOP_23 = (res_AndLogicOP_23 && (Counter_GetValore(L_P1__GetSubcl42(my_id)) < 13u));
    
    res_ImpliesLogicOp_17 = (res_ImpliesLogicOp_17 && res_AndLogicOP_23);
    }
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_ImpliesLogicOp_17);
    res_AndLogicOP_16 = (res_AndLogicOP_16 && Timer_Scaduto(L_P1__GetSubcl36(my_id)));
    
    res_ImpliesLogicOp_12 = (res_ImpliesLogicOp_12 && res_AndLogicOP_16);
    }
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_ImpliesLogicOp_12);
    bool res_OrLogicOP_108 = false;
    bool res_OrLogicOP_109 = false;
    bool res_NotLogicOP_110 = true;
    res_NotLogicOP_110 = (res_NotLogicOP_110 && ! (Counter_GetValore(L_P1__GetSubcl40(my_id)) == 154u));
    res_OrLogicOP_109 = (res_OrLogicOP_109 || res_NotLogicOP_110);
    bool res_AndLogicOP_111 = true;
    bool res_NotLogicOP_112 = true;
    bool res_NotLogicOP_113 = true;
    res_NotLogicOP_113 = (res_NotLogicOP_113 && ! (L_P1__GetInSubcl8(my_id) == false));
    res_NotLogicOP_112 = (res_NotLogicOP_112 && ! res_NotLogicOP_113);
    res_AndLogicOP_111 = (res_AndLogicOP_111 && res_NotLogicOP_112);
    res_AndLogicOP_111 = (res_AndLogicOP_111 && (L_P1__GetParamSubcl12(my_id) < 8u));
    
    res_OrLogicOP_109 = (res_OrLogicOP_109 || res_AndLogicOP_111);
    
    res_OrLogicOP_108 = (res_OrLogicOP_108 || res_OrLogicOP_109);
    bool res_NotLogicOP_114 = true;
    res_NotLogicOP_114 = (res_NotLogicOP_114 && ! Timer_Disattivo(L_P1__GetSubcl36(my_id)));
    res_OrLogicOP_108 = (res_OrLogicOP_108 || res_NotLogicOP_114);
    
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_OrLogicOP_108);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_AndLogicOP_11);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *47,51,52,*  *34,*  il parametro SubClass_C2_parametro_P3 non sia  diverso da  *56,* 4
    //   *104,* o  che  *,*  il contatore SubClass_C2_contatore_Co5 non sia  maggiore di  *54,* 115021
    //   *104,* e  che   l'argomento argomento_ave4 non  sia  uguale a c120
    bool res_OrLogicOP_115 = false;
    bool res_NotLogicOP_116 = true;
    bool res_NotLogicOP_117 = true;
    res_NotLogicOP_117 = (res_NotLogicOP_117 && ! (L_P1__GetParamSubcl11(my_id) == 4u));
    res_NotLogicOP_116 = (res_NotLogicOP_116 && ! res_NotLogicOP_117);
    res_OrLogicOP_115 = (res_OrLogicOP_115 || res_NotLogicOP_116);
    bool res_AndLogicOP_118 = true;
    bool res_NotLogicOP_119 = true;
    res_NotLogicOP_119 = (res_NotLogicOP_119 && ! (Counter_GetValore(L_P1__GetSubcl41(my_id)) > 115021u));
    res_AndLogicOP_118 = (res_AndLogicOP_118 && res_NotLogicOP_119);
    bool res_NotLogicOP_120 = true;
    res_NotLogicOP_120 = (res_NotLogicOP_120 && ! (argom70 == c120));
    res_AndLogicOP_118 = (res_AndLogicOP_118 && res_NotLogicOP_120);
    
    res_OrLogicOP_115 = (res_OrLogicOP_115 || res_AndLogicOP_118);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_115);
    
    
    
    return res_AndLogicOP_0;
}


// Macro valorizzate

/*
    CNL corrispondente:
    
    { commento: {[} commento: {37,}  se la variabile SubClass_C2_variabile_V9 non è  minore di  commento: {55,} 2 commento: {36,} e  se il timer SubClass_C2_timer_T8 non è disattivo o  se l'argomento argomento_a4 non  è  uguale a c270x commento: {39,} ,  commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  commento: {105,} è  uguale a  commento: {53,}  state1 , commento: {88,} quando  commento: {45,}    MainClass_C1_contatore_Co7 del campo  MainClass_C1     è  minore di  commento: {55,} 134 commento: {36,} o  se il timer SubClass_C2_timer_T1 non è attivo e  se la macro  SubClass_C2_macrova_M5 ( con argomento_a10   uguale a c270x ,argomento_a6   uguale a avvio ,argomento_a1   uguale a Rosso ,argomento_a3   uguale a c75Giallo  e argomento_a2   uguale a c120 )  non  è  diverso da  True  commento: {40,}  , assegna alla macro il valore  False 
    
     commento: {46,} assegna alla macro il valore  True  commento: {],}
    }
*/
bool L_P1__Macro15(instance_id_t const my_id , C2_Enumerat3 argom39, C2_Enumerat4 argom40, C2_Enumerat1 argom41)
{
bool res_macro_val;
    
    //  *[* *37,*  se la variabile SubClass_C2_variabile_V9 non è  minore di  *55,* 2 *36,* e  se il timer SubClass_C2_timer_T8 non è disattivo o  se l'argomento argomento_a4 non  è  uguale a c270x *39,* ,  *111,*  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  *105,* è  uguale a  *53,*  state1 , *88,* quando  *45,*    MainClass_C1_contatore_Co7 del campo  MainClass_C1     è  minore di  *55,* 134 *36,* o  se il timer SubClass_C2_timer_T1 non è attivo e  se la macro  SubClass_C2_macrova_M5 ( con argomento_a10   uguale a c270x ,argomento_a6   uguale a avvio ,argomento_a1   uguale a Rosso ,argomento_a3   uguale a c75Giallo  e argomento_a2   uguale a c120 )  non  è  diverso da  True
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_AndLogicOP_2 = true;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__GetSubcl28(my_id) < 2u));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_3);
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! Timer_Disattivo(L_P1__GetSubcl38(my_id)));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_4);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_2);
    bool res_AndLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (argom39 == c270x));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_6);
    bool res_ForAllPredicateNotEmpty_7 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl9Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl9(my_id,i);
    bool res_ImpliesLogicOp_8 = true;
    if((Counter_GetValore(L_P1__GetMainc44(it.mainc45)) < 134u)){
    res_ImpliesLogicOp_8 = (res_ImpliesLogicOp_8 && (L_P1_C1_GetState(it.mainc45) == C1_St_state));
    res_ForAllPredicateNotEmpty_7 = res_ImpliesLogicOp_8;
    if(!res_ForAllPredicateNotEmpty_7) {break;}
    }
    }
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_ForAllPredicateNotEmpty_7);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_5);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_AndLogicOP_9 = true;
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! Timer_Attivo(L_P1__GetSubcl35(my_id)));
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_NotLogicOP_10);
    bool res_NotLogicOP_11 = true;
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (L_P1__Macro16(my_id,rosso,c270x,c120,c75giallo,avvio) == true));
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! res_NotLogicOP_12);
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_NotLogicOP_11);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_9);
    
    if(res_OrLogicOP_0){
    
    res_macro_val = false;
    }
    else{
    res_macro_val = true;
    }
    return res_macro_val;
}

/*
    CNL corrispondente:
    
    { commento: {[}
     commento: {46,} assegna alla macro il valore  False  commento: {],}
    }
*/
bool L_P1__Macro16(instance_id_t const my_id , C2_Enumerat1 argom42, C2_Enumerat3 argom43, C2_Enumerat4 argom44, C2_Enumerat4 argom45, C2_Enumerat1 argom46)
{
return false;
}

/*
    CNL corrispondente:
    
    { commento: {[} commento: {42,}  se  MainClass_C1_controllo_C8 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  diverso da avanzamento commento: {41,} o  se MainClass_C1_parametro_P2 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  minore di  commento: {55,} 4 commento: {34,} o  se il parametro SubClass_C2_parametro_P3 non è  uguale a  commento: {53,} 8 commento: {42,} o  se  MainClass_C1_controllo_C1 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  commento: {105,} è  diverso da  True  , assegna alla macro il valore GialloGiallo
    
     commento: {46,} assegna alla macro il valore GialloGiallo commento: {],}
    }
*/
C2_Enumerat2 L_P1__Macro17(instance_id_t const my_id , C2_Enumerat4 argom47, C2_Enumerat2 argom48, C2_Enumerat2 argom49, bool argom50)
{
C2_Enumerat2 res_macro_val;
    
    //  *[* *42,*  se  MainClass_C1_controllo_C8 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  diverso da avanzamento *41,* o  se MainClass_C1_parametro_P2 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  minore di  *55,* 4 *34,* o  se il parametro SubClass_C2_parametro_P3 non è  uguale a  *53,* 8 *42,* o  se  MainClass_C1_controllo_C1 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  *105,* è  diverso da  True
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_OrLogicOP_2 = false;
    bool res_ForAllPredicate_3 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl10Length(my_id); ++i)
    {
    L_P1__Recor1 it = L_P1__GetRecSubcl10(my_id,i);
    bool res_ImpliesLogicOp_4 = true;
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetInMainc4(it.mainc46) == avanzamento));
    res_ImpliesLogicOp_4 = (res_ImpliesLogicOp_4 && res_NotLogicOP_5);
    res_ForAllPredicate_3 = res_ImpliesLogicOp_4;
    if(!res_ForAllPredicate_3) {break;}
    }
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_ForAllPredicate_3);
    bool res_ForAllPredicate_6 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl9Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl9(my_id,i);
    bool res_ImpliesLogicOp_7 = true;
    res_ImpliesLogicOp_7 = (res_ImpliesLogicOp_7 && (L_P1__GetParamMainc6(it.mainc45) < 4u));
    res_ForAllPredicate_6 = res_ImpliesLogicOp_7;
    if(!res_ForAllPredicate_6) {break;}
    }
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_ForAllPredicate_6);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_OrLogicOP_2);
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetParamSubcl11(my_id) == 8u));
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_NotLogicOP_8);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_ForAllPredicateNotEmpty_9 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl10Length(my_id); ++i)
    {
    L_P1__Recor1 it = L_P1__GetRecSubcl10(my_id,i);
    bool res_ImpliesLogicOp_10 = true;
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (L_P1__GetInMainc2(it.mainc46) == true));
    res_ImpliesLogicOp_10 = (res_ImpliesLogicOp_10 && res_NotLogicOP_11);
    res_ForAllPredicateNotEmpty_9 = res_ImpliesLogicOp_10;
    if(!res_ForAllPredicateNotEmpty_9) {break;}
    }
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_ForAllPredicateNotEmpty_9);
    
    if(res_OrLogicOP_0){
    
    res_macro_val = giallogiall;
    }
    else{
    res_macro_val = giallogiall;
    }
    return res_macro_val;
}

/*
    CNL corrispondente:
    
    { commento: {[}
     commento: {46,} assegna alla macro il valore  False  commento: {],}
    }
*/
bool L_P1__Macro18(instance_id_t const my_id , C2_Enumerat3 argom51, C2_Enumerat3 argom52, C2_Enumerat4 argom53, C2_Enumerat4 argom54, bool argom55, C2_Enumerat4 argom56, C2_Enumerat1 argom57)
{
return false;
}



