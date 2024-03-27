#include "Logica/ClasseLDS_MainClass_C1.h"
#include "Logica/ClasseLDS_SubClass_C2.h"
#include "Logica/ClasseLDS_SubClass_C2_priv.h"
#include "config.h"
#include "scheduler.h"


// ********** Gestione comandi manuali **********

static bool L_P1_C2_SetExpectedCmdsResponse(instance_id_t const my_id, C2_Stateenu state)
{        
    bool isCommandPresent = false;

    // for each manual command of L_P1_C2
    if (L_P1__GetInEvent7(my_id)) {
        #define IS_STATE_ACCEPTING_Event7 false // no state is accepting this command!
        L_P1__SetOutEvent9(my_id, IS_STATE_ACCEPTING_Event7 ? LDS_MANCMD_BLOCKED : LDS_MANCMD_UNEXPECTED);
        isCommandPresent |= true;		
    } else {
        L_P1__SetOutEvent9(my_id, LDS_MANCMD_NOOP);
    }
    if (L_P1__GetInEvent8(my_id)) {
        #define IS_STATE_ACCEPTING_Event8 false // no state is accepting this command!
        L_P1__SetOutEvent10(my_id, IS_STATE_ACCEPTING_Event8 ? LDS_MANCMD_BLOCKED : LDS_MANCMD_UNEXPECTED);
        isCommandPresent |= true;		
    } else {
        L_P1__SetOutEvent10(my_id, LDS_MANCMD_NOOP);
    }
    
    return isCommandPresent;
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
    Verifica che il parametro LDS_SubClass_C2_parametro_P4 sia  uguale a c120x
    }
*/
static inline bool L_P1__Guard3(instance_id_t const my_id)
{
    bool res_AndLogicOP_0 = true;
    
    //  che il parametro LDS_SubClass_C2_parametro_P4 sia  uguale a c120x
    res_AndLogicOP_0 = (res_AndLogicOP_0 && (L_P1__GetParamLds_s11(my_id) == c120x));
    
    
    
    
    return res_AndLogicOP_0;
}


/*
    CNL corrispondente:
     {
    	Verifica che il parametro LDS_SubClass_C2_parametro_P4 sia  uguale a c120x
    }
*/
static inline bool L_P1__Guard4(instance_id_t const my_id)
{
    bool res_AndLogicOP_0 = true;
    
    //  che il parametro LDS_SubClass_C2_parametro_P4 sia  uguale a c120x
    res_AndLogicOP_0 = (res_AndLogicOP_0 && (L_P1__GetParamLds_s11(my_id) == c120x));
    
    
    
    
    return res_AndLogicOP_0;
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
    Incrementa il contatore LDS_SubClass_C2_contatore_Co10
    }
*/
static inline void L_P1__Effec3(instance_id_t const my_id)
{
    
    //  Incrementa il contatore LDS_SubClass_C2_contatore_Co10
    Counter_Incr(L_P1__GetLds_s18(my_id));
}


/*
    CNL corrispondente:
     {
     	Incrementa il contatore LDS_SubClass_C2_contatore_Co10
     }
*/
static inline void L_P1__Effec4(instance_id_t const my_id)
{
    
    //  Incrementa il contatore LDS_SubClass_C2_contatore_Co10
    Counter_Incr(L_P1__GetLds_s18(my_id));
}



// ********** Definizione metodi **********

// Metodi standard

void L_P1_C2_Init(instance_id_t const my_id)
{
    // init variabili di stato
    L_P1__SetLds_s12(my_id, false);
    L_P1__SetLds_s13(my_id, rossogiallo2);
    L_P1__SetLds_s14(my_id, rossogiallo2);
    L_P1__SetLds_s15(my_id, 0);
    L_P1__SetLds_s16(my_id, c180x);
    L_P1__SetStato3(my_id, 0);
    // init Timer e Counter
    Timer_AggmInit(L_P1__GetLds_s17(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__lds_s17_ID);
    Timer_Init(L_P1__GetLds_s17(my_id), 45000);
    Counter_AggmInit(L_P1__GetLds_s18(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__lds_s18_ID);
    Counter_Init(L_P1__GetLds_s18(my_id));
    Counter_AggmInit(L_P1__GetLds_s19(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__lds_s19_ID);
    Counter_Init(L_P1__GetLds_s19(my_id));
    Counter_AggmInit(L_P1__GetLds_s20(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__lds_s20_ID);
    Counter_Init(L_P1__GetLds_s20(my_id));
    Counter_AggmInit(L_P1__GetLds_s21(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__lds_s21_ID);
    Counter_Init(L_P1__GetLds_s21(my_id));
    Counter_AggmInit(L_P1__GetLds_s22(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__lds_s22_ID);
    Counter_Init(L_P1__GetLds_s22(my_id));
    // init response
    L_P1_C2_SetResponse(my_id, LDS_SCHED_NOP);

    // transizione iniziale
    if(L_P1__Guard2(my_id)) {
        L_P1_C2_SetState(my_id, C2_St_state);
	L_P1__Effec2(my_id);
    } else {
        STOP_EXECUTION(LOGIC_ERROR);
    }
}

void L_P1_C2_Exec(instance_id_t const my_id, Phase const p)
{
    L_P1_C2_SetResponse(my_id, LDS_SCHED_NOP);
    switch (p) {

    case LDS_PHASE_MANUAL:

        if (true == L_P1_C2_SetExpectedCmdsResponse(my_id, L_P1_C2_GetState(my_id))) {

            switch (L_P1_C2_GetState(my_id)) {

	        case C2_St_state:
	                { } // fine transizioni da state nella fase LDS_PHASE_MANUAL
	            break;
	
	        default:
	            STOP_EXECUTION(LOGIC_ERROR);
	            break;  // Needed for MISRA C syntactic compliance
	        } // switch sugli stati chiuso
        }
        break;
 

    case LDS_PHASE_STATE:

        switch (L_P1_C2_GetState(my_id)) {

        case C2_St_state:
            if (L_P1__Guard4(my_id)) {
                L_P1_C2_SetState(my_id, C2_St_state);
                L_P1__Effec4(my_id);				
                L_P1_C2_SetResponse(my_id, LDS_SCHED_WAIT);
            }
            else if (L_P1__Guard3(my_id)) {
                L_P1_C2_SetState(my_id, C2_St_state);
                L_P1__Effec3(my_id);				
                L_P1_C2_SetResponse(my_id, LDS_SCHED_WAIT);
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
    Timer_Exec(L_P1__GetLds_s17(my_id));
}

void L_P1_C2_GSetSafe(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C2(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C2(proc_id);
    L_P1__SetOutLds_s(my_id, c120x);
    L_P1__SetOutLds_s1(my_id, spento);
    L_P1__SetOutLds_s2(my_id, true);
    L_P1__SetOutLds_s3(my_id, true);
    L_P1__SetOutLds_s4(my_id, true);
}


// ********** Definizione macro **********

// Macro di effetto

/*
    CNL corrispondente:
    
    { commento: {43,}  se LDS_MainClass_C1_timer_T3 del campo LDS_MainClass_C1  di LDS_SubClass_C2_lista_L1 è attivo commento: {37,} e  se la variabile LDS_SubClass_C2_variabile_V3 non è  maggiore di  commento: {54,} 4 commento: {36,} o  se il timer LDS_SubClass_C2_timer_T4 è disattivo, commento: {66,} Assegna al comando LDS_SubClass_C2_comando_C10 il valore c120x
    
    se  LDS_MainClass_C1_controllo_C9 del campo  LDS_MainClass_C1 di LDS_SubClass_C2_lista_L4  è  diverso da False e  
     commento: {41,}  se LDS_MainClass_C1_parametro_P5 del campo LDS_MainClass_C1  di LDS_SubClass_C2_lista_L7 esiste e  commento: {105,} è  diverso da  False  commento: {38,} e  se il contatore LDS_SubClass_C2_contatore_Co8 non è  uguale a  commento: {53,} 135 o  se il parametro ConsDef  è  uguale a FALSE , commento: {66,} Assegna al comando LDS_SubClass_C2_comando_C2 il valore spento
    
       
     commento: {37,}  se la variabile LDS_SubClass_C2_variabile_V3 è  maggiore di  commento: {54,} 3 e  se il parametro ConsDef è uguale a FALSE  commento: {38,} e  se il contatore LDS_SubClass_C2_contatore_Co10 è  uguale a  commento: {53,} 122 commento: {34,} e  se il parametro LDS_SubClass_C2_parametro_P4 non è  uguale a c120x commento: {37,} o  se la variabile LDS_SubClass_C2_variabile_V7 è  diverso da c270x, commento: {66,} Assegna al comando LDS_SubClass_C2_comando_C10 il valore c120x
    
       
    
    }
*/
void L_P1__Macro6(instance_id_t const my_id )
{
//  *43,*  se LDS_MainClass_C1_timer_T3 del campo LDS_MainClass_C1  di LDS_SubClass_C2_lista_L1 è attivo *37,* e  se la variabile LDS_SubClass_C2_variabile_V3 non è  maggiore di  *54,* 4 *36,* o  se il timer LDS_SubClass_C2_timer_T4 è disattivo, *66,* Assegna al comando LDS_SubClass_C2_comando_C10 il valore c120x
    bool res_OrLogicOP_0 = false;
    bool res_AndLogicOP_1 = true;
    bool res_ForAllPredicate_2 = true;
    for (index_t i = 0; i < L_P1__GetParamLds_s8Length(my_id); ++i)
    {
    const L_P1__Recor * it = L_P1__GetRecLds_s8(my_id,i);
    bool res_ImpliesLogicOp_3 = true;
    res_ImpliesLogicOp_3 = (res_ImpliesLogicOp_3 && Timer_Attivo(L_P1__GetLds_m14(it->lds_m20)));
    res_ForAllPredicate_2 = res_ImpliesLogicOp_3;
    if(!res_ForAllPredicate_2) {break;}
    }
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_ForAllPredicate_2);
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetLds_s15(my_id) > 4u));
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_4);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_1);
    res_OrLogicOP_0 = (res_OrLogicOP_0 || Timer_Disattivo(L_P1__GetLds_s17(my_id)));
    
    if(res_OrLogicOP_0){
    
    L_P1__SetOutLds_s(my_id,c120x);
    }
    //  se  LDS_MainClass_C1_controllo_C9 del campo  LDS_MainClass_C1 di LDS_SubClass_C2_lista_L4  è  diverso da False e  
    // *41,*  se LDS_MainClass_C1_parametro_P5 del campo LDS_MainClass_C1  di LDS_SubClass_C2_lista_L7 esiste e  *105,* è  diverso da  False  *38,* e  se il contatore LDS_SubClass_C2_contatore_Co8 non è  uguale a  *53,* 135 o  se il parametro ConsDef  è  uguale a FALSE , *66,* Assegna al comando LDS_SubClass_C2_comando_C2 il valore spento
    bool res_OrLogicOP_5 = false;
    bool res_AndLogicOP_6 = true;
    bool res_AndLogicOP_7 = true;
    bool res_ForAllPredicate_8 = true;
    for (index_t i = 0; i < L_P1__GetParamLds_s9Length(my_id); ++i)
    {
    const L_P1__Recor1 * it = L_P1__GetRecLds_s9(my_id,i);
    bool res_ImpliesLogicOp_9 = true;
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__GetInLds_m6(it->lds_m21) == false));
    res_ImpliesLogicOp_9 = (res_ImpliesLogicOp_9 && res_NotLogicOP_10);
    res_ForAllPredicate_8 = res_ImpliesLogicOp_9;
    if(!res_ForAllPredicate_8) {break;}
    }
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_ForAllPredicate_8);
    bool res_ForAllPredicateNotEmpty_11 = false;
    for (index_t i = 0; i < L_P1__GetParamLds_s10Length(my_id); ++i)
    {
    const L_P1__Recor1 * it = L_P1__GetRecLds_s10(my_id,i);
    bool res_ImpliesLogicOp_12 = true;
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (L_P1__GetParamLds_m9(it->lds_m21) == false));
    res_ImpliesLogicOp_12 = (res_ImpliesLogicOp_12 && res_NotLogicOP_13);
    res_ForAllPredicateNotEmpty_11 = res_ImpliesLogicOp_12;
    if(!res_ForAllPredicateNotEmpty_11) {break;}
    }
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_ForAllPredicateNotEmpty_11);
    
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_AndLogicOP_7);
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (Counter_GetValore(L_P1__GetLds_s21(my_id)) == 135u));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_14);
    
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_AndLogicOP_6);
    res_OrLogicOP_5 = (res_OrLogicOP_5 || (L_P1__GetParamConsd1(my_id) == false));
    
    if(res_OrLogicOP_5){
    
    L_P1__SetOutLds_s1(my_id,spento);
    }
    //  *37,*  se la variabile LDS_SubClass_C2_variabile_V3 è  maggiore di  *54,* 3 e  se il parametro ConsDef è uguale a FALSE  *38,* e  se il contatore LDS_SubClass_C2_contatore_Co10 è  uguale a  *53,* 122 *34,* e  se il parametro LDS_SubClass_C2_parametro_P4 non è  uguale a c120x *37,* o  se la variabile LDS_SubClass_C2_variabile_V7 è  diverso da c270x, *66,* Assegna al comando LDS_SubClass_C2_comando_C10 il valore c120x
    bool res_OrLogicOP_15 = false;
    bool res_AndLogicOP_16 = true;
    bool res_AndLogicOP_17 = true;
    bool res_AndLogicOP_18 = true;
    res_AndLogicOP_18 = (res_AndLogicOP_18 && (L_P1__GetLds_s15(my_id) > 3u));
    res_AndLogicOP_18 = (res_AndLogicOP_18 && (L_P1__GetParamConsd1(my_id) == false));
    
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_AndLogicOP_18);
    res_AndLogicOP_17 = (res_AndLogicOP_17 && (Counter_GetValore(L_P1__GetLds_s18(my_id)) == 122u));
    
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_AndLogicOP_17);
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (L_P1__GetParamLds_s11(my_id) == c120x));
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_NotLogicOP_19);
    
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_AndLogicOP_16);
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! (L_P1__GetLds_s16(my_id) == c270x));
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_NotLogicOP_20);
    
    if(res_OrLogicOP_15){
    
    L_P1__SetOutLds_s(my_id,c120x);
    }
}

/*
    CNL corrispondente:
    
    { commento: {38,}  se il contatore LDS_SubClass_C2_contatore_Co2 è  uguale a  commento: {53,} 14 commento: {34,} e  se il parametro LDS_SubClass_C2_parametro_P4 è  diverso da c120x commento: {36,} e  se il timer LDS_SubClass_C2_timer_T4 non è attivo commento: {36,} e  se il timer LDS_SubClass_C2_timer_T4 non è attivo o  se il parametro ConsDef  è  uguale a FALSE , commento: {72,}Azzera il contatore LDS_SubClass_C2_contatore_Co2
    
     ,altrimenti  commento: {66,} Assegna al comando LDS_SubClass_C2_comando_C7 il valore  True 
    
    
     commento: {44,}  se  LDS_MainClass_C1_variabile_V1 del campo LDS_MainClass_C1  di LDS_SubClass_C2_lista_L7 esiste e  commento: {105,} è  diverso da c120 commento: {38,} e  se il contatore LDS_SubClass_C2_contatore_Co10 non è  uguale a  commento: {53,} 1543 commento: {37,} e  se la variabile LDS_SubClass_C2_variabile_V1 è  uguale a  True  o  se il parametro ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro LDS_SubClass_C2_parametro_P4 non è  diverso da c120x, commento: {67,} Assegna alla variabile LDS_SubClass_C2_variabile_V7 il valore c270x
    
     ,altrimenti  commento: {66,} Assegna al comando LDS_SubClass_C2_comando_C2 il valore spento
    
    
     commento: {34,}  se lo stato  è  uguale a  commento: {53,}  state1  commento: {106,} commento: {37,} e  se la variabile LDS_SubClass_C2_variabile_V2 non è  diverso da c120x commento: {34,} e  se il parametro LDS_SubClass_C2_parametro_P4 non è  diverso da c120x e  se il parametro ConsDef è uguale a FALSE  commento: {38,} o  se il contatore LDS_SubClass_C2_contatore_Co10 è  minore di  commento: {55,} contatore LDS_SubClass_C2_contatore_Co8, commento: {67,} Assegna alla variabile LDS_SubClass_C2_variabile_V3 il valore 6
    
       
     commento: {44,}  se  LDS_MainClass_C1_variabile_V7 del campo LDS_MainClass_C1  di LDS_SubClass_C2_lista_L1 esiste e  commento: {105,} è  uguale a RossoVerde commento: {34,} e  se il parametro LDS_SubClass_C2_parametro_P4 è  diverso da c120x, commento: {72,}Azzera il contatore LDS_SubClass_C2_contatore_Co2
    
     ,altrimenti  commento: {70,}Incrementa il contatore LDS_SubClass_C2_contatore_Co10
    
    
     commento: {38,}  se il contatore LDS_SubClass_C2_contatore_Co10 non è  maggiore di  commento: {54,} 13 commento: {38,} o  se il contatore LDS_SubClass_C2_contatore_Co2 non è  uguale a  commento: {53,} 1215 e  se il parametro ConsDef è uguale a FALSE  commento: {34,} o  se il parametro LDS_SubClass_C2_parametro_P4 è  uguale a c120x, commento: {67,} Assegna alla variabile LDS_SubClass_C2_variabile_V3 il valore 1
    
     ,altrimenti  commento: {69,}Disattiva il timer LDS_SubClass_C2_timer_T4
    
    
    
    }
*/
void L_P1__Macro7(instance_id_t const my_id )
{
//  *38,*  se il contatore LDS_SubClass_C2_contatore_Co2 è  uguale a  *53,* 14 *34,* e  se il parametro LDS_SubClass_C2_parametro_P4 è  diverso da c120x *36,* e  se il timer LDS_SubClass_C2_timer_T4 non è attivo *36,* e  se il timer LDS_SubClass_C2_timer_T4 non è attivo o  se il parametro ConsDef  è  uguale a FALSE , *72,*Azzera il contatore LDS_SubClass_C2_contatore_Co2
    // ,altrimenti  *66,* Assegna al comando LDS_SubClass_C2_comando_C7 il valore  True
    bool res_OrLogicOP_0 = false;
    bool res_AndLogicOP_1 = true;
    bool res_AndLogicOP_2 = true;
    bool res_AndLogicOP_3 = true;
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (Counter_GetValore(L_P1__GetLds_s19(my_id)) == 14u));
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetParamLds_s11(my_id) == c120x));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_4);
    
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_AndLogicOP_3);
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! Timer_Attivo(L_P1__GetLds_s17(my_id)));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_5);
    
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_AndLogicOP_2);
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! Timer_Attivo(L_P1__GetLds_s17(my_id)));
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_6);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_1);
    res_OrLogicOP_0 = (res_OrLogicOP_0 || (L_P1__GetParamConsd1(my_id) == false));
    
    if(res_OrLogicOP_0){
    
    Counter_Res(L_P1__GetLds_s19(my_id));
    }else{
    
    L_P1__SetOutLds_s4(my_id,true);
    }
    //  *44,*  se  LDS_MainClass_C1_variabile_V1 del campo LDS_MainClass_C1  di LDS_SubClass_C2_lista_L7 esiste e  *105,* è  diverso da c120 *38,* e  se il contatore LDS_SubClass_C2_contatore_Co10 non è  uguale a  *53,* 1543 *37,* e  se la variabile LDS_SubClass_C2_variabile_V1 è  uguale a  True  o  se il parametro ConsDef  è  uguale a FALSE  *34,* e  se il parametro LDS_SubClass_C2_parametro_P4 non è  diverso da c120x, *67,* Assegna alla variabile LDS_SubClass_C2_variabile_V7 il valore c270x
    // ,altrimenti  *66,* Assegna al comando LDS_SubClass_C2_comando_C2 il valore spento
    bool res_OrLogicOP_7 = false;
    bool res_AndLogicOP_8 = true;
    bool res_AndLogicOP_9 = true;
    bool res_ForAllPredicateNotEmpty_10 = false;
    for (index_t i = 0; i < L_P1__GetParamLds_s10Length(my_id); ++i)
    {
    const L_P1__Recor1 * it = L_P1__GetRecLds_s10(my_id,i);
    bool res_ImpliesLogicOp_11 = true;
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (L_P1__GetLds_m10(it->lds_m21) == c120));
    res_ImpliesLogicOp_11 = (res_ImpliesLogicOp_11 && res_NotLogicOP_12);
    res_ForAllPredicateNotEmpty_10 = res_ImpliesLogicOp_11;
    if(!res_ForAllPredicateNotEmpty_10) {break;}
    }
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_ForAllPredicateNotEmpty_10);
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (Counter_GetValore(L_P1__GetLds_s18(my_id)) == 1543u));
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_NotLogicOP_13);
    
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_AndLogicOP_9);
    res_AndLogicOP_8 = (res_AndLogicOP_8 && (L_P1__GetLds_s12(my_id) == true));
    
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_AndLogicOP_8);
    bool res_AndLogicOP_14 = true;
    res_AndLogicOP_14 = (res_AndLogicOP_14 && (L_P1__GetParamConsd1(my_id) == false));
    bool res_NotLogicOP_15 = true;
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (L_P1__GetParamLds_s11(my_id) == c120x));
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! res_NotLogicOP_16);
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_NotLogicOP_15);
    
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_AndLogicOP_14);
    
    if(res_OrLogicOP_7){
    
    L_P1__SetLds_s16(my_id,c270x);
    }else{
    
    L_P1__SetOutLds_s1(my_id,spento);
    }
    //  *34,*  se lo stato  è  uguale a  *53,*  state1  *106,* *37,* e  se la variabile LDS_SubClass_C2_variabile_V2 non è  diverso da c120x *34,* e  se il parametro LDS_SubClass_C2_parametro_P4 non è  diverso da c120x e  se il parametro ConsDef è uguale a FALSE  *38,* o  se il contatore LDS_SubClass_C2_contatore_Co10 è  minore di  *55,* contatore LDS_SubClass_C2_contatore_Co8, *67,* Assegna alla variabile LDS_SubClass_C2_variabile_V3 il valore 6
    bool res_OrLogicOP_17 = false;
    bool res_AndLogicOP_18 = true;
    bool res_AndLogicOP_19 = true;
    bool res_AndLogicOP_20 = true;
    res_AndLogicOP_20 = (res_AndLogicOP_20 && (L_P1_C2_GetState(my_id) == C2_St_state));
    bool res_NotLogicOP_21 = true;
    bool res_NotLogicOP_22 = true;
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! (L_P1__GetLds_s14(my_id) == c120x));
    res_NotLogicOP_21 = (res_NotLogicOP_21 && ! res_NotLogicOP_22);
    res_AndLogicOP_20 = (res_AndLogicOP_20 && res_NotLogicOP_21);
    
    res_AndLogicOP_19 = (res_AndLogicOP_19 && res_AndLogicOP_20);
    bool res_NotLogicOP_23 = true;
    bool res_NotLogicOP_24 = true;
    res_NotLogicOP_24 = (res_NotLogicOP_24 && ! (L_P1__GetParamLds_s11(my_id) == c120x));
    res_NotLogicOP_23 = (res_NotLogicOP_23 && ! res_NotLogicOP_24);
    res_AndLogicOP_19 = (res_AndLogicOP_19 && res_NotLogicOP_23);
    
    res_AndLogicOP_18 = (res_AndLogicOP_18 && res_AndLogicOP_19);
    res_AndLogicOP_18 = (res_AndLogicOP_18 && (L_P1__GetParamConsd1(my_id) == false));
    
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_AndLogicOP_18);
    res_OrLogicOP_17 = (res_OrLogicOP_17 || (Counter_GetValore(L_P1__GetLds_s18(my_id)) < Counter_GetValore(L_P1__GetLds_s21(my_id))));
    
    if(res_OrLogicOP_17){
    
    L_P1__SetLds_s15(my_id,6u);
    }
    //  *44,*  se  LDS_MainClass_C1_variabile_V7 del campo LDS_MainClass_C1  di LDS_SubClass_C2_lista_L1 esiste e  *105,* è  uguale a RossoVerde *34,* e  se il parametro LDS_SubClass_C2_parametro_P4 è  diverso da c120x, *72,*Azzera il contatore LDS_SubClass_C2_contatore_Co2
    // ,altrimenti  *70,*Incrementa il contatore LDS_SubClass_C2_contatore_Co10
    bool res_AndLogicOP_25 = true;
    bool res_ForAllPredicateNotEmpty_26 = false;
    for (index_t i = 0; i < L_P1__GetParamLds_s8Length(my_id); ++i)
    {
    const L_P1__Recor * it = L_P1__GetRecLds_s8(my_id,i);
    bool res_ImpliesLogicOp_27 = true;
    res_ImpliesLogicOp_27 = (res_ImpliesLogicOp_27 && (L_P1__GetLds_m11(it->lds_m20) == rossoverde));
    res_ForAllPredicateNotEmpty_26 = res_ImpliesLogicOp_27;
    if(!res_ForAllPredicateNotEmpty_26) {break;}
    }
    res_AndLogicOP_25 = (res_AndLogicOP_25 && res_ForAllPredicateNotEmpty_26);
    bool res_NotLogicOP_28 = true;
    res_NotLogicOP_28 = (res_NotLogicOP_28 && ! (L_P1__GetParamLds_s11(my_id) == c120x));
    res_AndLogicOP_25 = (res_AndLogicOP_25 && res_NotLogicOP_28);
    
    if(res_AndLogicOP_25){
    
    Counter_Res(L_P1__GetLds_s19(my_id));
    }else{
    
    Counter_Incr(L_P1__GetLds_s18(my_id));
    }
    //  *38,*  se il contatore LDS_SubClass_C2_contatore_Co10 non è  maggiore di  *54,* 13 *38,* o  se il contatore LDS_SubClass_C2_contatore_Co2 non è  uguale a  *53,* 1215 e  se il parametro ConsDef è uguale a FALSE  *34,* o  se il parametro LDS_SubClass_C2_parametro_P4 è  uguale a c120x, *67,* Assegna alla variabile LDS_SubClass_C2_variabile_V3 il valore 1
    // ,altrimenti  *69,*Disattiva il timer LDS_SubClass_C2_timer_T4
    bool res_OrLogicOP_29 = false;
    bool res_OrLogicOP_30 = false;
    bool res_NotLogicOP_31 = true;
    res_NotLogicOP_31 = (res_NotLogicOP_31 && ! (Counter_GetValore(L_P1__GetLds_s18(my_id)) > 13u));
    res_OrLogicOP_30 = (res_OrLogicOP_30 || res_NotLogicOP_31);
    bool res_AndLogicOP_32 = true;
    bool res_NotLogicOP_33 = true;
    res_NotLogicOP_33 = (res_NotLogicOP_33 && ! (Counter_GetValore(L_P1__GetLds_s19(my_id)) == 1215u));
    res_AndLogicOP_32 = (res_AndLogicOP_32 && res_NotLogicOP_33);
    res_AndLogicOP_32 = (res_AndLogicOP_32 && (L_P1__GetParamConsd1(my_id) == false));
    
    res_OrLogicOP_30 = (res_OrLogicOP_30 || res_AndLogicOP_32);
    
    res_OrLogicOP_29 = (res_OrLogicOP_29 || res_OrLogicOP_30);
    res_OrLogicOP_29 = (res_OrLogicOP_29 || (L_P1__GetParamLds_s11(my_id) == c120x));
    
    if(res_OrLogicOP_29){
    
    L_P1__SetLds_s15(my_id,1u);
    }else{
    
    Timer_Disattiva(L_P1__GetLds_s17(my_id));
    }
}

/*
    CNL corrispondente:
    
    { commento: {34,}  se il parametro LDS_SubClass_C2_parametro_P4 è  uguale a variabile LDS_SubClass_C2_variabile_V10 commento: {34,} e  se il parametro LDS_SubClass_C2_parametro_P4 è  diverso da c120x commento: {38,} o  se il contatore LDS_SubClass_C2_contatore_Co2 è  minore di  commento: {55,} 12 commento: {34,} o  se il parametro LDS_SubClass_C2_parametro_P4 non è  uguale a c120x o  se il parametro ConsDef è uguale a FALSE  commento: {34,} o  se il parametro LDS_SubClass_C2_parametro_P4 è  diverso da c120x, commento: {66,} Assegna al comando LDS_SubClass_C2_comando_C4 il valore  False 
    
       
    
    }
*/
void L_P1__Macro8(instance_id_t const my_id )
{
//  *34,*  se il parametro LDS_SubClass_C2_parametro_P4 è  uguale a variabile LDS_SubClass_C2_variabile_V10 *34,* e  se il parametro LDS_SubClass_C2_parametro_P4 è  diverso da c120x *38,* o  se il contatore LDS_SubClass_C2_contatore_Co2 è  minore di  *55,* 12 *34,* o  se il parametro LDS_SubClass_C2_parametro_P4 non è  uguale a c120x o  se il parametro ConsDef è uguale a FALSE  *34,* o  se il parametro LDS_SubClass_C2_parametro_P4 è  diverso da c120x, *66,* Assegna al comando LDS_SubClass_C2_comando_C4 il valore  False
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_AndLogicOP_4 = true;
    res_AndLogicOP_4 = (res_AndLogicOP_4 && (L_P1__GetParamLds_s11(my_id) == L_P1__GetLds_s13(my_id)));
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetParamLds_s11(my_id) == c120x));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_5);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_AndLogicOP_4);
    res_OrLogicOP_3 = (res_OrLogicOP_3 || (Counter_GetValore(L_P1__GetLds_s19(my_id)) < 12u));
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetParamLds_s11(my_id) == c120x));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_6);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_OrLogicOP_2);
    res_OrLogicOP_1 = (res_OrLogicOP_1 || (L_P1__GetParamConsd1(my_id) == false));
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetParamLds_s11(my_id) == c120x));
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_7);
    
    if(res_OrLogicOP_0){
    
    L_P1__SetOutLds_s2(my_id,false);
    }
}


// Macro di verifica

/*
    CNL corrispondente:
     
    { commento: {62,}  se la macro  LDS_SubClass_C2_macrova_M8   non  è  diverso da spento commento: {40,}  e  se il parametro ConsDef è uguale a FALSE , Almeno una delle seguenti { 
     commento: {61,} commento: {34,}  se lo stato  è  uguale a  commento: {53,}  state1  commento: {106,} o  se il parametro ConsDef è uguale a FALSE , Tutte le seguenti { 
     commento: {34,}  se il parametro LDS_SubClass_C2_parametro_P4 è  diverso da c120x commento: {38,} e  se il contatore LDS_SubClass_C2_contatore_Co2 non è  diverso da  commento: {56,} 1501, Verifica che   commento: {47,}   il parametro ConsDef  sia  uguale a FALSE 
     commento: {104,} e  che   il parametro ConsDef sia uguale a FALSE 
    
    
     } Verifica che   commento: {47,}   il parametro ConsDef  sia  uguale a FALSE 
     commento: {104,} o  che  commento: {34,}  il parametro LDS_SubClass_C2_parametro_P4 sia  diverso da c120x
    
    
     } Verifica che   commento: {47,49,50,}   il parametro ConsDef  sia  uguale a FALSE 
     commento: {104,} e  che   il parametro ConsDef sia uguale a FALSE 
     commento: {104,} e  che  commento: {,}  la variabile LDS_SubClass_C2_variabile_V3 sia  diverso da  commento: {56,} 10
     commento: {104,} o  che  commento: {,}  il timer LDS_SubClass_C2_timer_T4 non sia attivo
     commento: {104,} e  che  commento: {36,}  il timer LDS_SubClass_C2_timer_T4 sia attivo
    
    
    }
*/
bool L_P1__Macro13(instance_id_t const my_id )
{
bool res_AndLogicOP_0 = true;
    
    //  *62,*  se la macro  LDS_SubClass_C2_macrova_M8   non  è  diverso da spento *40,*  e  se il parametro ConsDef è uguale a FALSE , Almeno una delle seguenti { 
    //   *61,* *34,*  se lo stato  è  uguale a  *53,*  state1  *106,* o  se il parametro ConsDef è uguale a FALSE , Tutte le seguenti { 
    //   *34,*  se il parametro LDS_SubClass_C2_parametro_P4 è  diverso da c120x *38,* e  se il contatore LDS_SubClass_C2_contatore_Co2 non è  diverso da  *56,* 1501, Verifica che   *47,*   il parametro ConsDef  sia  uguale a FALSE 
    //   *104,* e  che   il parametro ConsDef sia uguale a FALSE 
    //   } Verifica che   *47,*   il parametro ConsDef  sia  uguale a FALSE 
    //   *104,* o  che  *34,*  il parametro LDS_SubClass_C2_parametro_P4 sia  diverso da c120x
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_AndLogicOP_2 = true;
    bool res_NotLogicOP_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__Macro12(my_id) == spento));
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! res_NotLogicOP_4);
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_3);
    res_AndLogicOP_2 = (res_AndLogicOP_2 && (L_P1__GetParamConsd1(my_id) == false));
    
    if(res_AndLogicOP_2){
    bool res_OrLogicOP_5 = false;
    bool res_ImpliesLogicOp_6 = true;
    bool res_OrLogicOP_7 = false;
    res_OrLogicOP_7 = (res_OrLogicOP_7 || (L_P1_C2_GetState(my_id) == C2_St_state));
    res_OrLogicOP_7 = (res_OrLogicOP_7 || (L_P1__GetParamConsd1(my_id) == false));
    
    if(res_OrLogicOP_7){
    bool res_ImpliesLogicOp_8 = true;
    bool res_AndLogicOP_9 = true;
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__GetParamLds_s11(my_id) == c120x));
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_NotLogicOP_10);
    bool res_NotLogicOP_11 = true;
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (Counter_GetValore(L_P1__GetLds_s19(my_id)) == 1501u));
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! res_NotLogicOP_12);
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_NotLogicOP_11);
    
    if(res_AndLogicOP_9){
    bool res_AndLogicOP_13 = true;
    res_AndLogicOP_13 = (res_AndLogicOP_13 && (L_P1__GetParamConsd1(my_id) == false));
    res_AndLogicOP_13 = (res_AndLogicOP_13 && (L_P1__GetParamConsd1(my_id) == false));
    
    res_ImpliesLogicOp_8 = (res_ImpliesLogicOp_8 && res_AndLogicOP_13);
    }
    res_ImpliesLogicOp_6 = (res_ImpliesLogicOp_6 && res_ImpliesLogicOp_8);
    }
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_ImpliesLogicOp_6);
    bool res_OrLogicOP_14 = false;
    res_OrLogicOP_14 = (res_OrLogicOP_14 || (L_P1__GetParamConsd1(my_id) == false));
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (L_P1__GetParamLds_s11(my_id) == c120x));
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_NotLogicOP_15);
    
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_OrLogicOP_14);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_OrLogicOP_5);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *47,49,50,*   il parametro ConsDef  sia  uguale a FALSE 
    //   *104,* e  che   il parametro ConsDef sia uguale a FALSE 
    //   *104,* e  che  *,*  la variabile LDS_SubClass_C2_variabile_V3 sia  diverso da  *56,* 10
    //   *104,* o  che  *,*  il timer LDS_SubClass_C2_timer_T4 non sia attivo
    //   *104,* e  che  *36,*  il timer LDS_SubClass_C2_timer_T4 sia attivo
    bool res_OrLogicOP_16 = false;
    bool res_AndLogicOP_17 = true;
    bool res_AndLogicOP_18 = true;
    res_AndLogicOP_18 = (res_AndLogicOP_18 && (L_P1__GetParamConsd1(my_id) == false));
    res_AndLogicOP_18 = (res_AndLogicOP_18 && (L_P1__GetParamConsd1(my_id) == false));
    
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_AndLogicOP_18);
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (L_P1__GetLds_s15(my_id) == 10u));
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_NotLogicOP_19);
    
    res_OrLogicOP_16 = (res_OrLogicOP_16 || res_AndLogicOP_17);
    bool res_AndLogicOP_20 = true;
    bool res_NotLogicOP_21 = true;
    res_NotLogicOP_21 = (res_NotLogicOP_21 && ! Timer_Attivo(L_P1__GetLds_s17(my_id)));
    res_AndLogicOP_20 = (res_AndLogicOP_20 && res_NotLogicOP_21);
    res_AndLogicOP_20 = (res_AndLogicOP_20 && Timer_Attivo(L_P1__GetLds_s17(my_id)));
    
    res_OrLogicOP_16 = (res_OrLogicOP_16 || res_AndLogicOP_20);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_16);
    
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
    
    { commento: {111,}  se lo stato del campo LDS_MainClass_C1  di LDS_SubClass_C2_lista_L4 è  diverso da  commento: {56,}  state1 , Verifica che   commento: {47,52,}   l'argomento argomento_ave6 sia  uguale a c270x commento: {,} 
     commento: {104,} e  che  commento: {34,}  il parametro LDS_SubClass_C2_parametro_P4 sia  uguale a c120x
     commento: {104,} o  che  commento: {34,}  il parametro LDS_SubClass_C2_parametro_P4 non sia  diverso da c120x
     commento: {104,} e  che  commento: {34,}  il parametro LDS_SubClass_C2_parametro_P4 sia  diverso da c120x
    
    
    }
*/
bool L_P1__Macro14(instance_id_t const my_id , C2_Enumerat4 argom19, C2_Enumerat2 argom20, C2_Enumerat3 argom21, C2_Enumerat3 argom22, bool argom23, bool argom24)
{
bool res_AndLogicOP_0 = true;
    
    //  *111,*  se lo stato del campo LDS_MainClass_C1  di LDS_SubClass_C2_lista_L4 è  diverso da  *56,*  state1 , Verifica che   *47,52,*   l'argomento argomento_ave6 sia  uguale a c270x *,* 
    //   *104,* e  che  *34,*  il parametro LDS_SubClass_C2_parametro_P4 sia  uguale a c120x
    //   *104,* o  che  *34,*  il parametro LDS_SubClass_C2_parametro_P4 non sia  diverso da c120x
    //   *104,* e  che  *34,*  il parametro LDS_SubClass_C2_parametro_P4 sia  diverso da c120x
    bool res_ImpliesLogicOp_1 = true;
    bool res_ForAllPredicate_2 = true;
    for (index_t i = 0; i < L_P1__GetParamLds_s9Length(my_id); ++i)
    {
    const L_P1__Recor1 * it = L_P1__GetRecLds_s9(my_id,i);
    bool res_ImpliesLogicOp_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1_C1_GetState(it->lds_m21) == C1_St_state));
    res_ImpliesLogicOp_3 = (res_ImpliesLogicOp_3 && res_NotLogicOP_4);
    res_ForAllPredicate_2 = res_ImpliesLogicOp_3;
    if(!res_ForAllPredicate_2) {break;}
    }
    if(res_ForAllPredicate_2){
    bool res_OrLogicOP_5 = false;
    bool res_AndLogicOP_6 = true;
    res_AndLogicOP_6 = (res_AndLogicOP_6 && (argom22 == c270x));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && (L_P1__GetParamLds_s11(my_id) == c120x));
    
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_AndLogicOP_6);
    bool res_AndLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetParamLds_s11(my_id) == c120x));
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! res_NotLogicOP_9);
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_8);
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__GetParamLds_s11(my_id) == c120x));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_10);
    
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_AndLogicOP_7);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_OrLogicOP_5);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
    
    {
    	
    	 commento: {34,}  se lo stato  è  diverso da  commento: {56,}  state1  commento: {106,} commento: {37,} o  se la variabile LDS_SubClass_C2_variabile_V3 è  minore di  commento: {55,} 5 commento: {36,} e  se il timer LDS_SubClass_C2_timer_T4 non è scaduto, Verifica che   commento: {47,49,50,52,}  commento: {34,}  il parametro LDS_SubClass_C2_parametro_P4 sia  uguale a c120x
     commento: {104,} o  che   l'argomento argomento_ave5 sia  diverso da  False  commento: {,} 
     commento: {104,} o  che   il parametro ConsDef sia uguale a FALSE 
     commento: {104,} e  che  commento: {34,}  il parametro LDS_SubClass_C2_parametro_P4 non sia  uguale a variabile LDS_SubClass_C2_variabile_V10
     commento: {104,} o  che  commento: {,}  il timer LDS_SubClass_C2_timer_T4 sia disattivo
    
    
    }
*/
bool L_P1__Macro15(instance_id_t const my_id , bool argom25, bool argom26, C2_Enumerat2 argom27, C2_Enumerat4 argom28, bool argom29, bool argom30)
{
bool res_AndLogicOP_0 = true;
    
    //  *34,*  se lo stato  è  diverso da  *56,*  state1  *106,* *37,* o  se la variabile LDS_SubClass_C2_variabile_V3 è  minore di  *55,* 5 *36,* e  se il timer LDS_SubClass_C2_timer_T4 non è scaduto, Verifica che   *47,49,50,52,*  *34,*  il parametro LDS_SubClass_C2_parametro_P4 sia  uguale a c120x
    //   *104,* o  che   l'argomento argomento_ave5 sia  diverso da  False  *,* 
    //   *104,* o  che   il parametro ConsDef sia uguale a FALSE 
    //   *104,* e  che  *34,*  il parametro LDS_SubClass_C2_parametro_P4 non sia  uguale a variabile LDS_SubClass_C2_variabile_V10
    //   *104,* o  che  *,*  il timer LDS_SubClass_C2_timer_T4 sia disattivo
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1_C2_GetState(my_id) == C2_St_state));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_3);
    bool res_AndLogicOP_4 = true;
    res_AndLogicOP_4 = (res_AndLogicOP_4 && (L_P1__GetLds_s15(my_id) < 5u));
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! Timer_Scaduto(L_P1__GetLds_s17(my_id)));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_5);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_4);
    
    if(res_OrLogicOP_2){
    bool res_OrLogicOP_6 = false;
    bool res_OrLogicOP_7 = false;
    bool res_OrLogicOP_8 = false;
    res_OrLogicOP_8 = (res_OrLogicOP_8 || (L_P1__GetParamLds_s11(my_id) == c120x));
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (argom29 == false));
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_NotLogicOP_9);
    
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_OrLogicOP_8);
    bool res_AndLogicOP_10 = true;
    res_AndLogicOP_10 = (res_AndLogicOP_10 && (L_P1__GetParamConsd1(my_id) == false));
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (L_P1__GetParamLds_s11(my_id) == L_P1__GetLds_s13(my_id)));
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_NotLogicOP_11);
    
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_AndLogicOP_10);
    
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_OrLogicOP_7);
    res_OrLogicOP_6 = (res_OrLogicOP_6 || Timer_Disattivo(L_P1__GetLds_s17(my_id)));
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_OrLogicOP_6);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    
    
    
    return res_AndLogicOP_0;
}


// Macro valorizzate

/*
    CNL corrispondente:
     
    { commento: {[} commento: {41,}  se LDS_MainClass_C1_parametro_P3 del campo LDS_MainClass_C1  di LDS_SubClass_C2_lista_L4 esiste e  commento: {105,} è  uguale a  False  commento: {34,} e  se il parametro LDS_SubClass_C2_parametro_P4 è  uguale a c120x commento: {36,} o  se il timer LDS_SubClass_C2_timer_T4 è disattivo commento: {34,} e  se il parametro LDS_SubClass_C2_parametro_P4 non è  uguale a c120x commento: {36,} e  se il timer LDS_SubClass_C2_timer_T4 non è attivo , assegna alla macro il valore RossoGiallo
    
     commento: {46,} assegna alla macro il valore RossoGiallo commento: {],}
    }
*/
C2_Enumerat1 L_P1__Macro9(instance_id_t const my_id )
{
C2_Enumerat1 res_macro_val;
    
    //  *[* *41,*  se LDS_MainClass_C1_parametro_P3 del campo LDS_MainClass_C1  di LDS_SubClass_C2_lista_L4 esiste e  *105,* è  uguale a  False  *34,* e  se il parametro LDS_SubClass_C2_parametro_P4 è  uguale a c120x *36,* o  se il timer LDS_SubClass_C2_timer_T4 è disattivo *34,* e  se il parametro LDS_SubClass_C2_parametro_P4 non è  uguale a c120x *36,* e  se il timer LDS_SubClass_C2_timer_T4 non è attivo
    bool res_OrLogicOP_0 = false;
    bool res_AndLogicOP_1 = true;
    bool res_ForAllPredicateNotEmpty_2 = false;
    for (index_t i = 0; i < L_P1__GetParamLds_s9Length(my_id); ++i)
    {
    const L_P1__Recor1 * it = L_P1__GetRecLds_s9(my_id,i);
    bool res_ImpliesLogicOp_3 = true;
    res_ImpliesLogicOp_3 = (res_ImpliesLogicOp_3 && (L_P1__GetParamLds_m8(it->lds_m21) == false));
    res_ForAllPredicateNotEmpty_2 = res_ImpliesLogicOp_3;
    if(!res_ForAllPredicateNotEmpty_2) {break;}
    }
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_ForAllPredicateNotEmpty_2);
    res_AndLogicOP_1 = (res_AndLogicOP_1 && (L_P1__GetParamLds_s11(my_id) == c120x));
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_1);
    bool res_AndLogicOP_4 = true;
    bool res_AndLogicOP_5 = true;
    res_AndLogicOP_5 = (res_AndLogicOP_5 && Timer_Disattivo(L_P1__GetLds_s17(my_id)));
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetParamLds_s11(my_id) == c120x));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_6);
    
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_AndLogicOP_5);
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! Timer_Attivo(L_P1__GetLds_s17(my_id)));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_7);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_4);
    
    if(res_OrLogicOP_0){
    
    res_macro_val = rossogiallo1;
    }
    else{
    res_macro_val = rossogiallo1;
    }
    return res_macro_val;
}

/*
    CNL corrispondente:
    
    { commento: {[}
     commento: {46,} assegna alla macro il valore RossoGiallo commento: {],}
    }
*/
C2_Enumerat1 L_P1__Macro10(instance_id_t const my_id , C2_Enumerat1 argom8, bool argom9, C2_Enumerat1 argom10, C2_Enumerat4 argom11)
{
return rossogiallo1;
}

/*
    CNL corrispondente:
    
    {
    	 commento: {[} commento: {34,}  se il parametro LDS_SubClass_C2_parametro_P4 non è  diverso da c120x,  commento: {43,}   se LDS_MainClass_C1_timer_T8 del campo LDS_MainClass_C1  di LDS_SubClass_C2_lista_L1 esiste e  commento: {105,} è attivo, commento: {88,} quando  commento: {41,}   LDS_MainClass_C1_parametro_P2 del campo LDS_MainClass_C1      commento: {105,} è  uguale a  commento: {53,} 5 , assegna alla macro il valore  True  
     commento: {46,} assegna alla macro il valore  True  commento: {],}
    }
*/
bool L_P1__Macro11(instance_id_t const my_id , C2_Enumerat4 argom12, C2_Enumerat1 argom13, C2_Enumerat4 argom14, C2_Enumerat1 argom15, C2_Enumerat1 argom16, C2_Enumerat2 argom17, C2_Enumerat3 argom18)
{
bool res_macro_val;
    
    //  *[* *34,*  se il parametro LDS_SubClass_C2_parametro_P4 non è  diverso da c120x,  *43,*   se LDS_MainClass_C1_timer_T8 del campo LDS_MainClass_C1  di LDS_SubClass_C2_lista_L1 esiste e  *105,* è attivo, *88,* quando  *41,*   LDS_MainClass_C1_parametro_P2 del campo LDS_MainClass_C1      *105,* è  uguale a  *53,* 5
    bool res_AndLogicOP_0 = true;
    bool res_NotLogicOP_1 = true;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (L_P1__GetParamLds_s11(my_id) == c120x));
    res_NotLogicOP_1 = (res_NotLogicOP_1 && ! res_NotLogicOP_2);
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_NotLogicOP_1);
    bool res_ForAllPredicateNotEmpty_3 = false;
    for (index_t i = 0; i < L_P1__GetParamLds_s8Length(my_id); ++i)
    {
    const L_P1__Recor * it = L_P1__GetRecLds_s8(my_id,i);
    bool res_ImpliesLogicOp_4 = true;
    if((L_P1__GetParamLds_m7(it->lds_m20) == 5u)){
    res_ImpliesLogicOp_4 = (res_ImpliesLogicOp_4 && Timer_Attivo(L_P1__GetLds_m15(it->lds_m20)));
    res_ForAllPredicateNotEmpty_3 = res_ImpliesLogicOp_4;
    if(!res_ForAllPredicateNotEmpty_3) {break;}
    }
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ForAllPredicateNotEmpty_3);
    
    if(res_AndLogicOP_0){
    
    res_macro_val = true;
    }
    else{
    res_macro_val = true;
    }
    return res_macro_val;
}

/*
    CNL corrispondente:
     
    { commento: {[} commento: {43,}  se LDS_MainClass_C1_timer_T3 del campo LDS_MainClass_C1  di LDS_SubClass_C2_lista_L4  è disattivo , assegna alla macro il valore spento
    
     commento: {46,} assegna alla macro il valore spento commento: {],}
    }
*/
C2_Enumerat4 L_P1__Macro12(instance_id_t const my_id )
{
C2_Enumerat4 res_macro_val;
    
    //  LDS_MainClass_C1_timer_T3 del campo LDS_MainClass_C1  di LDS_SubClass_C2_lista_L4  è disattivo
    bool res_ForAllPredicate_0 = true;
    for (index_t i = 0; i < L_P1__GetParamLds_s9Length(my_id); ++i)
    {
    const L_P1__Recor1 * it = L_P1__GetRecLds_s9(my_id,i);
    bool res_ImpliesLogicOp_1 = true;
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && Timer_Disattivo(L_P1__GetLds_m14(it->lds_m21)));
    res_ForAllPredicate_0 = res_ImpliesLogicOp_1;
    if(!res_ForAllPredicate_0) {break;}
    }
    if(res_ForAllPredicate_0){
    
    res_macro_val = spento;
    }
    else{
    res_macro_val = spento;
    }
    return res_macro_val;
}



