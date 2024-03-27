#include "Logica/ClasseLDV_MainClass_C1.h"
#include "Logica/ClasseLDV_MainClass_C1_priv.h"
#include "config.h"
#include "scheduler.h"


// ********** Gestione comandi automatici **********

static size_t L_P1_C3_NumAutoCmds(instance_id_t const my_id)
{
    size_t n = 0u;
    if (L_P1__GetCAEvent13(my_id)) {
        ++n;
    }
    return n;
}


// ********** Gestione comandi manuali **********

static bool L_P1_C3_SetExpectedCmdsResponse(instance_id_t const my_id, C3_Stateenu state)
{        
    bool isCommandPresent = false;

    // for each manual command of L_P1_C3
    if (L_P1__GetInEvent11(my_id)) {
        #define IS_STATE_ACCEPTING_Event11 false // no state is accepting this command!
        L_P1__SetOutEvent14(my_id, IS_STATE_ACCEPTING_Event11 ? LDS_MANCMD_BLOCKED : LDS_MANCMD_UNEXPECTED);
        isCommandPresent |= true;		
    } else {
        L_P1__SetOutEvent14(my_id, LDS_MANCMD_NOOP);
    }
    if (L_P1__GetInEvent12(my_id)) {
        #define IS_STATE_ACCEPTING_Event12 false // no state is accepting this command!
        L_P1__SetOutEvent15(my_id, IS_STATE_ACCEPTING_Event12 ? LDS_MANCMD_BLOCKED : LDS_MANCMD_UNEXPECTED);
        isCommandPresent |= true;		
    } else {
        L_P1__SetOutEvent15(my_id, LDS_MANCMD_NOOP);
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
static inline bool L_P1__Guard5(instance_id_t const my_id)
{
    return true;
}


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
    	Verifica che il parametro LDV_MainClass_C1_parametro_P1 sia  uguale a False
    }
*/
static inline bool L_P1__Guard7(instance_id_t const my_id)
{
    bool res_AndLogicOP_0 = true;
    
    //  che il parametro LDV_MainClass_C1_parametro_P1 sia  uguale a False
    res_AndLogicOP_0 = (res_AndLogicOP_0 && (L_P1__GetParamLdv_m(my_id) == false));
    
    
    
    
    return res_AndLogicOP_0;
}


// ********** Definizione effetti **********

/*
    CNL corrispondente:
    
     {
     Nessuna 
     }
*/
static inline void L_P1__Effec5(instance_id_t const my_id)
{
    
}


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
     	Nessuno
     }
*/
static inline void L_P1__Effec7(instance_id_t const my_id)
{
    
}



// ********** Definizione metodi **********

// Metodi standard

void L_P1_C3_Init(instance_id_t const my_id)
{
    // init variabili di stato
    L_P1__SetLdv_m3(my_id, 0);
    L_P1__SetLdv_m4(my_id, false);
    L_P1__SetLdv_m5(my_id, c270);
    L_P1__SetStato5(my_id, 0);
    // init Timer e Counter
    Timer_AggmInit(L_P1__GetLdv_m6(my_id), true, CLASS_L_P1_C3_ID, my_id, L_P1__ldv_m6_ID);
    Timer_Init(L_P1__GetLdv_m6(my_id), 10000);
    Counter_AggmInit(L_P1__GetLdv_m7(my_id), true, CLASS_L_P1_C3_ID, my_id, L_P1__ldv_m7_ID);
    Counter_Init(L_P1__GetLdv_m7(my_id));
    Counter_AggmInit(L_P1__GetLdv_m8(my_id), true, CLASS_L_P1_C3_ID, my_id, L_P1__ldv_m8_ID);
    Counter_Init(L_P1__GetLdv_m8(my_id));
    Counter_AggmInit(L_P1__GetLdv_m9(my_id), true, CLASS_L_P1_C3_ID, my_id, L_P1__ldv_m9_ID);
    Counter_Init(L_P1__GetLdv_m9(my_id));
    Counter_AggmInit(L_P1__GetLdv_m10(my_id), true, CLASS_L_P1_C3_ID, my_id, L_P1__ldv_m10_ID);
    Counter_Init(L_P1__GetLdv_m10(my_id));
    // init response
    L_P1_C3_SetResponse(my_id, LDS_SCHED_NOP);

    // transizione iniziale
    if(L_P1__Guard5(my_id)) {
        L_P1_C3_SetState(my_id, C3_St_state);
	L_P1__Effec5(my_id);
    } else {
        STOP_EXECUTION(LOGIC_ERROR);
    }
}

void L_P1_C3_Exec(instance_id_t const my_id, Phase const p)
{
    L_P1_C3_SetResponse(my_id, LDS_SCHED_NOP);
    switch (p) {

    case LDS_PHASE_MANUAL:

        if (true == L_P1_C3_SetExpectedCmdsResponse(my_id, L_P1_C3_GetState(my_id))) {

            switch (L_P1_C3_GetState(my_id)) {

	        case C3_St_state:
	                { } // fine transizioni da state nella fase LDS_PHASE_MANUAL
	            break;
	
	        default:
	            STOP_EXECUTION(LOGIC_ERROR);
	            break;  // Needed for MISRA C syntactic compliance
	        } // switch sugli stati chiuso
        }
        break;
 

    case LDS_PHASE_STATE:

        switch (L_P1_C3_GetState(my_id)) {

        case C3_St_state:
            if (L_P1__Guard7(my_id)) {
                L_P1_C3_SetState(my_id, C3_St_state);
                L_P1__Effec7(my_id);				
                L_P1_C3_SetResponse(my_id, LDS_SCHED_WAIT);
            }
            else if (L_P1__Guard6(my_id)) {
                L_P1_C3_SetState(my_id, C3_St_state);
                L_P1__Effec6(my_id);				
                L_P1_C3_SetResponse(my_id, LDS_SCHED_WAIT);
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
        size_t auto_commands_before = L_P1_C3_NumAutoCmds(my_id);
        switch (L_P1_C3_GetState(my_id)) {

        case C3_St_state:
                { } // fine transizioni da state nella fase LDS_PHASE_AUTO
            break;

        default:
            STOP_EXECUTION(LOGIC_ERROR);
            break;  // Needed for MISRA C syntactic compliance
        } // switch sugli stati chiuso
        size_t auto_commands_after = L_P1_C3_NumAutoCmds(my_id);
        CHECK_GE(auto_commands_before, auto_commands_after);

        if ((auto_commands_after > 0u) && (auto_commands_before > auto_commands_after)) {
            L_P1_C3_SetResponse(my_id, LDS_SCHED_CONTINUE);
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
    Timer_Exec(L_P1__GetLdv_m6(my_id));
}



// ********** Definizione macro **********

// Macro di effetto

/*
    CNL corrispondente:
    
    { commento: {36,}  se il timer LDV_MainClass_C1_timer_T3 è scaduto e  se il parametro ConsDef  è  uguale a FALSE  commento: {36,} e  se il timer LDV_MainClass_C1_timer_T3 non è scaduto commento: {36,} e  se il timer LDV_MainClass_C1_timer_T3 non è disattivo, commento: {67,} Assegna alla variabile LDV_MainClass_C1_variabile_V9 il valore c270xx
    
     ,altrimenti  commento: {70,}Incrementa il contatore LDV_MainClass_C1_contatore_Co6
    
    
      se il parametro ConsDef è uguale a FALSE ,  Applica gli effetti
           della macro LDV_MainClass_C1_macroef_M3   commento: {73,}
    
     ,altrimenti  commento: {67,} Assegna alla variabile LDV_MainClass_C1_variabile_V8 il valore  True 
    
    
      se il parametro ConsDef è uguale a FALSE  commento: {38,} o  se il contatore LDV_MainClass_C1_contatore_Co6 non è  minore di  commento: {55,} contatore LDV_MainClass_C1_contatore_Co7 commento: {38,} o  se il contatore LDV_MainClass_C1_contatore_Co7 non è  uguale a  commento: {53,} 1452 commento: {34,} o  se il parametro LDV_MainClass_C1_parametro_P9 è  uguale a RossoGialloGiallo commento: {37,} o  se la variabile LDV_MainClass_C1_variabile_V3 non è  uguale a  commento: {53,} 10, commento: {72,}Azzera il contatore LDV_MainClass_C1_contatore_Co6
    
       
     commento: {38,}  se il contatore LDV_MainClass_C1_contatore_Co6 non è  maggiore di  commento: {54,} contatore LDV_MainClass_C1_contatore_Co7 commento: {38,} o  se il contatore LDV_MainClass_C1_contatore_Co6 non è  uguale a  commento: {53,} contatore LDV_MainClass_C1_contatore_Co1 o  se il parametro ConsDef è uguale a FALSE , commento: {68,}Attiva il timer LDV_MainClass_C1_timer_T3
    
     ,altrimenti   Applica gli effetti
           della macro LDV_MainClass_C1_macroef_M7  commento: {73,}
    
    
     commento: {34,}  se il parametro LDV_MainClass_C1_parametro_P1 è  diverso da  True  e  se il parametro ConsDef  è  uguale a FALSE  commento: {38,} e  se il contatore LDV_MainClass_C1_contatore_Co1 non è  uguale a  commento: {53,} contatore LDV_MainClass_C1_contatore_Co4 o  se il parametro ConsDef  è  uguale a FALSE  o  se il parametro ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro LDV_MainClass_C1_parametro_P1 è  uguale a  True ,  Applica gli effetti
           della macro LDV_MainClass_C1_macroef_M8  commento: {73,}
    
     ,altrimenti  commento: {70,}Incrementa il contatore LDV_MainClass_C1_contatore_Co6
    
    
    
    }
*/
void L_P1__Macro17(instance_id_t const my_id )
{
//  *36,*  se il timer LDV_MainClass_C1_timer_T3 è scaduto e  se il parametro ConsDef  è  uguale a FALSE  *36,* e  se il timer LDV_MainClass_C1_timer_T3 non è scaduto *36,* e  se il timer LDV_MainClass_C1_timer_T3 non è disattivo, *67,* Assegna alla variabile LDV_MainClass_C1_variabile_V9 il valore c270xx
    // ,altrimenti  *70,*Incrementa il contatore LDV_MainClass_C1_contatore_Co6
    bool res_AndLogicOP_0 = true;
    bool res_AndLogicOP_1 = true;
    bool res_AndLogicOP_2 = true;
    res_AndLogicOP_2 = (res_AndLogicOP_2 && Timer_Scaduto(L_P1__GetLdv_m6(my_id)));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && (L_P1__GetParamConsd2(my_id) == false));
    
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_AndLogicOP_2);
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! Timer_Scaduto(L_P1__GetLdv_m6(my_id)));
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_3);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_AndLogicOP_1);
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! Timer_Disattivo(L_P1__GetLdv_m6(my_id)));
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_NotLogicOP_4);
    
    if(res_AndLogicOP_0){
    
    L_P1__SetLdv_m5(my_id,c270xx);
    }else{
    
    Counter_Incr(L_P1__GetLdv_m9(my_id));
    }
    //  se il parametro ConsDef è uguale a FALSE ,  Applica gli effetti
    //       della macro LDV_MainClass_C1_macroef_M3   *73,*
    // ,altrimenti  *67,* Assegna alla variabile LDV_MainClass_C1_variabile_V8 il valore  True
    if((L_P1__GetParamConsd2(my_id) == false)){
    
    L_P1__Macro18(my_id);
    }else{
    
    L_P1__SetLdv_m4(my_id,true);
    }
    //  se il parametro ConsDef è uguale a FALSE  *38,* o  se il contatore LDV_MainClass_C1_contatore_Co6 non è  minore di  *55,* contatore LDV_MainClass_C1_contatore_Co7 *38,* o  se il contatore LDV_MainClass_C1_contatore_Co7 non è  uguale a  *53,* 1452 *34,* o  se il parametro LDV_MainClass_C1_parametro_P9 è  uguale a RossoGialloGiallo *37,* o  se la variabile LDV_MainClass_C1_variabile_V3 non è  uguale a  *53,* 10, *72,*Azzera il contatore LDV_MainClass_C1_contatore_Co6
    bool res_OrLogicOP_5 = false;
    bool res_OrLogicOP_6 = false;
    bool res_OrLogicOP_7 = false;
    bool res_OrLogicOP_8 = false;
    res_OrLogicOP_8 = (res_OrLogicOP_8 || (L_P1__GetParamConsd2(my_id) == false));
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (Counter_GetValore(L_P1__GetLdv_m9(my_id)) < Counter_GetValore(L_P1__GetLdv_m10(my_id))));
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_NotLogicOP_9);
    
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_OrLogicOP_8);
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (Counter_GetValore(L_P1__GetLdv_m10(my_id)) == 1452u));
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_NotLogicOP_10);
    
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_OrLogicOP_7);
    res_OrLogicOP_6 = (res_OrLogicOP_6 || (L_P1__GetParamLdv_m2(my_id) == rossogiallo5));
    
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_OrLogicOP_6);
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (L_P1__GetLdv_m3(my_id) == 10u));
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_NotLogicOP_11);
    
    if(res_OrLogicOP_5){
    
    Counter_Res(L_P1__GetLdv_m9(my_id));
    }
    //  *38,*  se il contatore LDV_MainClass_C1_contatore_Co6 non è  maggiore di  *54,* contatore LDV_MainClass_C1_contatore_Co7 *38,* o  se il contatore LDV_MainClass_C1_contatore_Co6 non è  uguale a  *53,* contatore LDV_MainClass_C1_contatore_Co1 o  se il parametro ConsDef è uguale a FALSE , *68,*Attiva il timer LDV_MainClass_C1_timer_T3
    // ,altrimenti   Applica gli effetti
    //       della macro LDV_MainClass_C1_macroef_M7
    bool res_OrLogicOP_12 = false;
    bool res_OrLogicOP_13 = false;
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (Counter_GetValore(L_P1__GetLdv_m9(my_id)) > Counter_GetValore(L_P1__GetLdv_m10(my_id))));
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_NotLogicOP_14);
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (Counter_GetValore(L_P1__GetLdv_m9(my_id)) == Counter_GetValore(L_P1__GetLdv_m7(my_id))));
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_NotLogicOP_15);
    
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_OrLogicOP_13);
    res_OrLogicOP_12 = (res_OrLogicOP_12 || (L_P1__GetParamConsd2(my_id) == false));
    
    if(res_OrLogicOP_12){
    
    Timer_Attiva(L_P1__GetLdv_m6(my_id));
    }else{
    
    L_P1__Macro20(my_id);
    }
    //  *73,*
    // *34,*  se il parametro LDV_MainClass_C1_parametro_P1 è  diverso da  True  e  se il parametro ConsDef  è  uguale a FALSE  *38,* e  se il contatore LDV_MainClass_C1_contatore_Co1 non è  uguale a  *53,* contatore LDV_MainClass_C1_contatore_Co4 o  se il parametro ConsDef  è  uguale a FALSE  o  se il parametro ConsDef  è  uguale a FALSE  *34,* e  se il parametro LDV_MainClass_C1_parametro_P1 è  uguale a  True ,  Applica gli effetti
    //       della macro LDV_MainClass_C1_macroef_M8  *73,*
    // ,altrimenti  *70,*Incrementa il contatore LDV_MainClass_C1_contatore_Co6
    bool res_OrLogicOP_16 = false;
    bool res_OrLogicOP_17 = false;
    bool res_AndLogicOP_18 = true;
    bool res_AndLogicOP_19 = true;
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! (L_P1__GetParamLdv_m(my_id) == true));
    res_AndLogicOP_19 = (res_AndLogicOP_19 && res_NotLogicOP_20);
    res_AndLogicOP_19 = (res_AndLogicOP_19 && (L_P1__GetParamConsd2(my_id) == false));
    
    res_AndLogicOP_18 = (res_AndLogicOP_18 && res_AndLogicOP_19);
    bool res_NotLogicOP_21 = true;
    res_NotLogicOP_21 = (res_NotLogicOP_21 && ! (Counter_GetValore(L_P1__GetLdv_m7(my_id)) == Counter_GetValore(L_P1__GetLdv_m8(my_id))));
    res_AndLogicOP_18 = (res_AndLogicOP_18 && res_NotLogicOP_21);
    
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_AndLogicOP_18);
    res_OrLogicOP_17 = (res_OrLogicOP_17 || (L_P1__GetParamConsd2(my_id) == false));
    
    res_OrLogicOP_16 = (res_OrLogicOP_16 || res_OrLogicOP_17);
    bool res_AndLogicOP_22 = true;
    res_AndLogicOP_22 = (res_AndLogicOP_22 && (L_P1__GetParamConsd2(my_id) == false));
    res_AndLogicOP_22 = (res_AndLogicOP_22 && (L_P1__GetParamLdv_m(my_id) == true));
    
    res_OrLogicOP_16 = (res_OrLogicOP_16 || res_AndLogicOP_22);
    
    if(res_OrLogicOP_16){
    
    L_P1__Macro21(my_id);
    }else{
    
    Counter_Incr(L_P1__GetLdv_m9(my_id));
    }
}

/*
    CNL corrispondente:
     
    {  se il parametro ConsDef è uguale a FALSE  e  se il parametro ConsDef è uguale a FALSE , commento: {71,}Decrementa il contatore LDV_MainClass_C1_contatore_Co6
    
       
     commento: {34,}  se il parametro LDV_MainClass_C1_parametro_P1 è  uguale a  False , commento: {67,} Assegna alla variabile LDV_MainClass_C1_variabile_V9 il valore c270xx
    
       
      se il parametro ConsDef  è  uguale a FALSE  commento: {36,} e  se il timer LDV_MainClass_C1_timer_T3 non è disattivo o  se il parametro ConsDef è uguale a FALSE  o  se il parametro ConsDef  è  uguale a FALSE , commento: {67,} Assegna alla variabile LDV_MainClass_C1_variabile_V8 il valore  True 
    
     ,altrimenti  commento: {68,}Attiva il timer LDV_MainClass_C1_timer_T3
    
    
    
    }
*/
void L_P1__Macro18(instance_id_t const my_id )
{
//  se il parametro ConsDef è uguale a FALSE  e  se il parametro ConsDef è uguale a FALSE , *71,*Decrementa il contatore LDV_MainClass_C1_contatore_Co6
    bool res_AndLogicOP_0 = true;
    res_AndLogicOP_0 = (res_AndLogicOP_0 && (L_P1__GetParamConsd2(my_id) == false));
    res_AndLogicOP_0 = (res_AndLogicOP_0 && (L_P1__GetParamConsd2(my_id) == false));
    
    if(res_AndLogicOP_0){
    
    Counter_Decr(L_P1__GetLdv_m9(my_id));
    }
    //  *34,*  se il parametro LDV_MainClass_C1_parametro_P1 è  uguale a  False , *67,* Assegna alla variabile LDV_MainClass_C1_variabile_V9 il valore c270xx
    if((L_P1__GetParamLdv_m(my_id) == false)){
    
    L_P1__SetLdv_m5(my_id,c270xx);
    }
    //  se il parametro ConsDef  è  uguale a FALSE  *36,* e  se il timer LDV_MainClass_C1_timer_T3 non è disattivo o  se il parametro ConsDef è uguale a FALSE  o  se il parametro ConsDef  è  uguale a FALSE , *67,* Assegna alla variabile LDV_MainClass_C1_variabile_V8 il valore  True 
    // ,altrimenti  *68,*Attiva il timer LDV_MainClass_C1_timer_T3
    bool res_OrLogicOP_1 = false;
    bool res_OrLogicOP_2 = false;
    bool res_AndLogicOP_3 = true;
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (L_P1__GetParamConsd2(my_id) == false));
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! Timer_Disattivo(L_P1__GetLdv_m6(my_id)));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_4);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_3);
    res_OrLogicOP_2 = (res_OrLogicOP_2 || (L_P1__GetParamConsd2(my_id) == false));
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_OrLogicOP_2);
    res_OrLogicOP_1 = (res_OrLogicOP_1 || (L_P1__GetParamConsd2(my_id) == false));
    
    if(res_OrLogicOP_1){
    
    L_P1__SetLdv_m4(my_id,true);
    }else{
    
    Timer_Attiva(L_P1__GetLdv_m6(my_id));
    }
}

/*
    CNL corrispondente:
    
    { commento: {37,}  se la variabile LDV_MainClass_C1_variabile_V3 è  diverso da  commento: {56,} 9 commento: {37,} o  se la variabile LDV_MainClass_C1_variabile_V3 non è  minore di  commento: {55,} 8 o  se il parametro ConsDef  è  uguale a FALSE  o  se il parametro ConsDef è uguale a FALSE , commento: {68,}Attiva il timer LDV_MainClass_C1_timer_T3
    
       
      se il parametro ConsDef è uguale a FALSE  commento: {37,} o  se la variabile LDV_MainClass_C1_variabile_V8 non è  diverso da  True , commento: {67,} Assegna alla variabile LDV_MainClass_C1_variabile_V9 il valore c270xx
    
     ,altrimenti  commento: {70,}Incrementa il contatore LDV_MainClass_C1_contatore_Co6
    
    
     commento: {34,}  se lo stato  è  uguale a  commento: {53,}  state1  commento: {106,} commento: {36,} o  se il timer LDV_MainClass_C1_timer_T3 è scaduto commento: {34,} e  se il parametro LDV_MainClass_C1_parametro_P7 è  minore di  commento: {55,} 10 commento: {37,} e  se la variabile LDV_MainClass_C1_variabile_V9 è  uguale a c270xx, commento: {67,} Assegna alla variabile LDV_MainClass_C1_variabile_V8 il valore  False 
    
       
    
    }
*/
void L_P1__Macro19(instance_id_t const my_id )
{
//  *37,*  se la variabile LDV_MainClass_C1_variabile_V3 è  diverso da  *56,* 9 *37,* o  se la variabile LDV_MainClass_C1_variabile_V3 non è  minore di  *55,* 8 o  se il parametro ConsDef  è  uguale a FALSE  o  se il parametro ConsDef è uguale a FALSE , *68,*Attiva il timer LDV_MainClass_C1_timer_T3
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_OrLogicOP_2 = false;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__GetLdv_m3(my_id) == 9u));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_3);
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetLdv_m3(my_id) < 8u));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_4);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_OrLogicOP_2);
    res_OrLogicOP_1 = (res_OrLogicOP_1 || (L_P1__GetParamConsd2(my_id) == false));
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    res_OrLogicOP_0 = (res_OrLogicOP_0 || (L_P1__GetParamConsd2(my_id) == false));
    
    if(res_OrLogicOP_0){
    
    Timer_Attiva(L_P1__GetLdv_m6(my_id));
    }
    //  se il parametro ConsDef è uguale a FALSE  *37,* o  se la variabile LDV_MainClass_C1_variabile_V8 non è  diverso da  True , *67,* Assegna alla variabile LDV_MainClass_C1_variabile_V9 il valore c270xx
    // ,altrimenti  *70,*Incrementa il contatore LDV_MainClass_C1_contatore_Co6
    bool res_OrLogicOP_5 = false;
    res_OrLogicOP_5 = (res_OrLogicOP_5 || (L_P1__GetParamConsd2(my_id) == false));
    bool res_NotLogicOP_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetLdv_m4(my_id) == true));
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! res_NotLogicOP_7);
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_NotLogicOP_6);
    
    if(res_OrLogicOP_5){
    
    L_P1__SetLdv_m5(my_id,c270xx);
    }else{
    
    Counter_Incr(L_P1__GetLdv_m9(my_id));
    }
    //  *34,*  se lo stato  è  uguale a  *53,*  state1  *106,* *36,* o  se il timer LDV_MainClass_C1_timer_T3 è scaduto *34,* e  se il parametro LDV_MainClass_C1_parametro_P7 è  minore di  *55,* 10 *37,* e  se la variabile LDV_MainClass_C1_variabile_V9 è  uguale a c270xx, *67,* Assegna alla variabile LDV_MainClass_C1_variabile_V8 il valore  False
    bool res_OrLogicOP_8 = false;
    res_OrLogicOP_8 = (res_OrLogicOP_8 || (L_P1_C3_GetState(my_id) == C3_St_state));
    bool res_AndLogicOP_9 = true;
    bool res_AndLogicOP_10 = true;
    res_AndLogicOP_10 = (res_AndLogicOP_10 && Timer_Scaduto(L_P1__GetLdv_m6(my_id)));
    res_AndLogicOP_10 = (res_AndLogicOP_10 && (L_P1__GetParamLdv_m1(my_id) < 10u));
    
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_AndLogicOP_10);
    res_AndLogicOP_9 = (res_AndLogicOP_9 && (L_P1__GetLdv_m5(my_id) == c270xx));
    
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_AndLogicOP_9);
    
    if(res_OrLogicOP_8){
    
    L_P1__SetLdv_m4(my_id,false);
    }
}

/*
    CNL corrispondente:
    
    {  se il parametro ConsDef è uguale a FALSE  commento: {37,} o  se la variabile LDV_MainClass_C1_variabile_V9 non è  uguale a c270xx commento: {38,} o  se il contatore LDV_MainClass_C1_contatore_Co4 non è  diverso da  commento: {56,} contatore LDV_MainClass_C1_contatore_Co1, commento: {69,}Disattiva il timer LDV_MainClass_C1_timer_T3
    
     ,altrimenti  commento: {67,} Assegna alla variabile LDV_MainClass_C1_variabile_V9 il valore c270xx
    
    
     commento: {34,}  se il parametro LDV_MainClass_C1_parametro_P1 non è  uguale a  True  commento: {37,} e  se la variabile LDV_MainClass_C1_variabile_V3 è  uguale a  commento: {53,} 2 commento: {34,} o  se il parametro LDV_MainClass_C1_parametro_P1 non è  uguale a  False , commento: {69,}Disattiva il timer LDV_MainClass_C1_timer_T3
    
     ,altrimenti   Applica gli effetti
           della macro LDV_MainClass_C1_macroef_M3   commento: {73,}
    
    
      se il parametro ConsDef è uguale a FALSE  commento: {38,} o  se il contatore LDV_MainClass_C1_contatore_Co6 non è  minore di  commento: {55,} 11 commento: {36,} o  se il timer LDV_MainClass_C1_timer_T3 è scaduto commento: {34,} e  se il parametro LDV_MainClass_C1_parametro_P7 non è  maggiore di  commento: {54,} 2 commento: {36,} e  se il timer LDV_MainClass_C1_timer_T3 è disattivo o  se il parametro ConsDef è uguale a FALSE , commento: {69,}Disattiva il timer LDV_MainClass_C1_timer_T3
    
       
     commento: {38,}  se il contatore LDV_MainClass_C1_contatore_Co6 è  uguale a  commento: {53,} contatore LDV_MainClass_C1_contatore_Co7, commento: {69,}Disattiva il timer LDV_MainClass_C1_timer_T3
    
       
    
    }
*/
void L_P1__Macro20(instance_id_t const my_id )
{
//  se il parametro ConsDef è uguale a FALSE  *37,* o  se la variabile LDV_MainClass_C1_variabile_V9 non è  uguale a c270xx *38,* o  se il contatore LDV_MainClass_C1_contatore_Co4 non è  diverso da  *56,* contatore LDV_MainClass_C1_contatore_Co1, *69,*Disattiva il timer LDV_MainClass_C1_timer_T3
    // ,altrimenti  *67,* Assegna alla variabile LDV_MainClass_C1_variabile_V9 il valore c270xx
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    res_OrLogicOP_1 = (res_OrLogicOP_1 || (L_P1__GetParamConsd2(my_id) == false));
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (L_P1__GetLdv_m5(my_id) == c270xx));
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_NotLogicOP_2);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_NotLogicOP_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (Counter_GetValore(L_P1__GetLdv_m8(my_id)) == Counter_GetValore(L_P1__GetLdv_m7(my_id))));
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! res_NotLogicOP_4);
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_3);
    
    if(res_OrLogicOP_0){
    
    Timer_Disattiva(L_P1__GetLdv_m6(my_id));
    }else{
    
    L_P1__SetLdv_m5(my_id,c270xx);
    }
    //  *34,*  se il parametro LDV_MainClass_C1_parametro_P1 non è  uguale a  True  *37,* e  se la variabile LDV_MainClass_C1_variabile_V3 è  uguale a  *53,* 2 *34,* o  se il parametro LDV_MainClass_C1_parametro_P1 non è  uguale a  False , *69,*Disattiva il timer LDV_MainClass_C1_timer_T3
    // ,altrimenti   Applica gli effetti
    //       della macro LDV_MainClass_C1_macroef_M3
    bool res_OrLogicOP_5 = false;
    bool res_AndLogicOP_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetParamLdv_m(my_id) == true));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_7);
    res_AndLogicOP_6 = (res_AndLogicOP_6 && (L_P1__GetLdv_m3(my_id) == 2u));
    
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_AndLogicOP_6);
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetParamLdv_m(my_id) == false));
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_NotLogicOP_8);
    
    if(res_OrLogicOP_5){
    
    Timer_Disattiva(L_P1__GetLdv_m6(my_id));
    }else{
    
    L_P1__Macro18(my_id);
    }
    //  *73,*
    //  se il parametro ConsDef è uguale a FALSE  *38,* o  se il contatore LDV_MainClass_C1_contatore_Co6 non è  minore di  *55,* 11 *36,* o  se il timer LDV_MainClass_C1_timer_T3 è scaduto *34,* e  se il parametro LDV_MainClass_C1_parametro_P7 non è  maggiore di  *54,* 2 *36,* e  se il timer LDV_MainClass_C1_timer_T3 è disattivo o  se il parametro ConsDef è uguale a FALSE , *69,*Disattiva il timer LDV_MainClass_C1_timer_T3
    bool res_OrLogicOP_9 = false;
    bool res_OrLogicOP_10 = false;
    bool res_OrLogicOP_11 = false;
    res_OrLogicOP_11 = (res_OrLogicOP_11 || (L_P1__GetParamConsd2(my_id) == false));
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (Counter_GetValore(L_P1__GetLdv_m9(my_id)) < 11u));
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_NotLogicOP_12);
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_OrLogicOP_11);
    bool res_AndLogicOP_13 = true;
    bool res_AndLogicOP_14 = true;
    res_AndLogicOP_14 = (res_AndLogicOP_14 && Timer_Scaduto(L_P1__GetLdv_m6(my_id)));
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (L_P1__GetParamLdv_m1(my_id) > 2u));
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_NotLogicOP_15);
    
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_AndLogicOP_14);
    res_AndLogicOP_13 = (res_AndLogicOP_13 && Timer_Disattivo(L_P1__GetLdv_m6(my_id)));
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_AndLogicOP_13);
    
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_OrLogicOP_10);
    res_OrLogicOP_9 = (res_OrLogicOP_9 || (L_P1__GetParamConsd2(my_id) == false));
    
    if(res_OrLogicOP_9){
    
    Timer_Disattiva(L_P1__GetLdv_m6(my_id));
    }
    //  *38,*  se il contatore LDV_MainClass_C1_contatore_Co6 è  uguale a  *53,* contatore LDV_MainClass_C1_contatore_Co7, *69,*Disattiva il timer LDV_MainClass_C1_timer_T3
    if((Counter_GetValore(L_P1__GetLdv_m9(my_id)) == Counter_GetValore(L_P1__GetLdv_m10(my_id)))){
    
    Timer_Disattiva(L_P1__GetLdv_m6(my_id));
    }
}

/*
    CNL corrispondente:
    
    {  se il parametro ConsDef è uguale a FALSE  commento: {38,} e  se il contatore LDV_MainClass_C1_contatore_Co7 è  uguale a  commento: {53,} 1215, commento: {69,}Disattiva il timer LDV_MainClass_C1_timer_T3
    
       
    
    }
*/
void L_P1__Macro21(instance_id_t const my_id )
{
//  se il parametro ConsDef è uguale a FALSE  *38,* e  se il contatore LDV_MainClass_C1_contatore_Co7 è  uguale a  *53,* 1215, *69,*Disattiva il timer LDV_MainClass_C1_timer_T3
    bool res_AndLogicOP_0 = true;
    res_AndLogicOP_0 = (res_AndLogicOP_0 && (L_P1__GetParamConsd2(my_id) == false));
    res_AndLogicOP_0 = (res_AndLogicOP_0 && (Counter_GetValore(L_P1__GetLdv_m10(my_id)) == 1215u));
    
    if(res_AndLogicOP_0){
    
    Timer_Disattiva(L_P1__GetLdv_m6(my_id));
    }
}


// Macro di verifica

/*
    CNL corrispondente:
    
    { commento: {36,}  se il timer LDV_MainClass_C1_timer_T3 non è disattivo e  se l'argomento argomento_ave1 non  è  diverso da  False  commento: {39,}  commento: {37,} e  se la variabile LDV_MainClass_C1_variabile_V3 non è  diverso da  commento: {56,} 10 commento: {38,} e  se il contatore LDV_MainClass_C1_contatore_Co4 è  uguale a  commento: {53,} 111 e  se l'argomento argomento_ave4 non  è  uguale a  True  commento: {39,} , Verifica che   commento: {47,50,52,}  commento: {34,}  il parametro LDV_MainClass_C1_parametro_P1 sia  uguale a  False 
     commento: {104,} o  che   l'argomento argomento_ave1 sia  diverso da  True  commento: {,} 
     commento: {104,} o  che  commento: {,}  la variabile LDV_MainClass_C1_variabile_V3 non sia  minore di  commento: {55,} 4
     commento: {104,} e  che  commento: {37,}  la variabile LDV_MainClass_C1_variabile_V8 sia  diverso da  False 
     commento: {104,} e  che   l'argomento argomento_ave1 non  sia  diverso da  False  commento: {39,} 
     commento: {104,} o  che   l'argomento argomento_ave1 non  sia  uguale a  True  commento: {39,} 
    
    
    }
*/
bool L_P1__Macro24(instance_id_t const my_id , bool argom40, C3_Enumerat4 argom41, bool argom42, C3_Enumerat1 argom43)
{
bool res_AndLogicOP_0 = true;
    
    //  *36,*  se il timer LDV_MainClass_C1_timer_T3 non è disattivo e  se l'argomento argomento_ave1 non  è  diverso da  False  *39,*  *37,* e  se la variabile LDV_MainClass_C1_variabile_V3 non è  diverso da  *56,* 10 *38,* e  se il contatore LDV_MainClass_C1_contatore_Co4 è  uguale a  *53,* 111 e  se l'argomento argomento_ave4 non  è  uguale a  True  *39,* , Verifica che   *47,50,52,*  *34,*  il parametro LDV_MainClass_C1_parametro_P1 sia  uguale a  False 
    //   *104,* o  che   l'argomento argomento_ave1 sia  diverso da  True  *,* 
    //   *104,* o  che  *,*  la variabile LDV_MainClass_C1_variabile_V3 non sia  minore di  *55,* 4
    //   *104,* e  che  *37,*  la variabile LDV_MainClass_C1_variabile_V8 sia  diverso da  False 
    //   *104,* e  che   l'argomento argomento_ave1 non  sia  diverso da  False  *39,* 
    //   *104,* o  che   l'argomento argomento_ave1 non  sia  uguale a  True
    bool res_ImpliesLogicOp_1 = true;
    bool res_AndLogicOP_2 = true;
    bool res_AndLogicOP_3 = true;
    bool res_AndLogicOP_4 = true;
    bool res_AndLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! Timer_Disattivo(L_P1__GetLdv_m6(my_id)));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_6);
    bool res_NotLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (argom40 == false));
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! res_NotLogicOP_8);
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_7);
    
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_AndLogicOP_5);
    bool res_NotLogicOP_9 = true;
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__GetLdv_m3(my_id) == 10u));
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! res_NotLogicOP_10);
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_9);
    
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_AndLogicOP_4);
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (Counter_GetValore(L_P1__GetLdv_m8(my_id)) == 111u));
    
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_AndLogicOP_3);
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (argom42 == true));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_11);
    
    if(res_AndLogicOP_2){
    bool res_OrLogicOP_12 = false;
    bool res_OrLogicOP_13 = false;
    bool res_OrLogicOP_14 = false;
    res_OrLogicOP_14 = (res_OrLogicOP_14 || (L_P1__GetParamLdv_m(my_id) == false));
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (argom40 == true));
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_NotLogicOP_15);
    
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_OrLogicOP_14);
    bool res_AndLogicOP_16 = true;
    bool res_AndLogicOP_17 = true;
    bool res_NotLogicOP_18 = true;
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! (L_P1__GetLdv_m3(my_id) < 4u));
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_NotLogicOP_18);
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (L_P1__GetLdv_m4(my_id) == false));
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_NotLogicOP_19);
    
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_AndLogicOP_17);
    bool res_NotLogicOP_20 = true;
    bool res_NotLogicOP_21 = true;
    res_NotLogicOP_21 = (res_NotLogicOP_21 && ! (argom40 == false));
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! res_NotLogicOP_21);
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_NotLogicOP_20);
    
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_AndLogicOP_16);
    
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_OrLogicOP_13);
    bool res_NotLogicOP_22 = true;
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! (argom40 == true));
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_NotLogicOP_22);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_OrLogicOP_12);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
    
    { commento: {62,} commento: {34,}  se lo stato  è  diverso da  commento: {56,}  state1  commento: {106,} commento: {36,} e  se il timer LDV_MainClass_C1_timer_T3 non è attivo commento: {36,} o  se il timer LDV_MainClass_C1_timer_T3 non è disattivo o  se l'argomento argomento_ave5 è  diverso da avvio commento: {39,}  commento: {36,} o  se il timer LDV_MainClass_C1_timer_T3 non è scaduto, Almeno una delle seguenti { 
     commento: {63,} commento: {34,}  se il parametro LDV_MainClass_C1_parametro_P1 è  uguale a  True  commento: {34,} o  se il parametro LDV_MainClass_C1_parametro_P7 non è  minore di  commento: {55,} 4 commento: {36,} e  se il timer LDV_MainClass_C1_timer_T3 è disattivo commento: {38,} o  se il contatore LDV_MainClass_C1_contatore_Co6 è  minore di  commento: {55,} contatore LDV_MainClass_C1_contatore_Co1 commento: {37,} o  se la variabile LDV_MainClass_C1_variabile_V8 è  uguale a  False  e  se il parametro ConsDef è uguale a FALSE , Solo una delle seguenti { 
     commento: {63,} commento: {36,}  se il timer LDV_MainClass_C1_timer_T3 è scaduto commento: {38,} e  se il contatore LDV_MainClass_C1_contatore_Co4 è  diverso da  commento: {56,} contatore LDV_MainClass_C1_contatore_Co7 commento: {37,} e  se la variabile LDV_MainClass_C1_variabile_V3 è  uguale a  commento: {53,} 8, Solo una delle seguenti { 
     commento: {63,} commento: {34,}  se il parametro LDV_MainClass_C1_parametro_P1 non è  diverso da  True  commento: {34,} e  se il parametro LDV_MainClass_C1_parametro_P1 non è  diverso da  False  e  se l'argomento argomento_ave8 è  diverso da  False  commento: {39,}  e  se l'argomento argomento_ave6 non  è  uguale a RossoGialloGiallo commento: {39,} , Solo una delle seguenti { 
     commento: {34,}  se il parametro LDV_MainClass_C1_parametro_P7 è  uguale a  commento: {53,} 1 commento: {37,} e  se la variabile LDV_MainClass_C1_variabile_V8 è  uguale a  False  o  se il parametro ConsDef è uguale a FALSE , Verifica che   commento: {47,49,51,}  commento: {,}  il timer LDV_MainClass_C1_timer_T3 non sia attivo
     commento: {104,} o  che  commento: {34,}  il parametro LDV_MainClass_C1_parametro_P1 non sia  uguale a  False 
     commento: {104,} o  che  commento: {,}  il contatore LDV_MainClass_C1_contatore_Co6 non sia  diverso da  commento: {56,} 140
     commento: {104,} e  che  commento: {36,}  il timer LDV_MainClass_C1_timer_T3 sia attivo
    
    
     } Verifica che   commento: {47,52,}   l'argomento argomento_ave8 non  sia  diverso da  False  commento: {,} 
     commento: {104,} e  che  commento: {34,}  il parametro LDV_MainClass_C1_parametro_P1 sia  uguale a  True 
    
    
     } Verifica che   commento: {47,49,50,51,}  commento: {,}  la variabile LDV_MainClass_C1_variabile_V9 sia  diverso da c270xx
     commento: {104,} o  che  commento: {34,}  il parametro LDV_MainClass_C1_parametro_P1 non sia  diverso da  False 
     commento: {104,} o  che  commento: {34,}  il parametro LDV_MainClass_C1_parametro_P1 sia  diverso da  True 
     commento: {104,} o  che  commento: {,}  il timer LDV_MainClass_C1_timer_T3 non sia attivo
     commento: {104,} e  che   il parametro ConsDef sia uguale a FALSE 
     commento: {104,} o  che  commento: {,}  il contatore LDV_MainClass_C1_contatore_Co6 non sia  minore di  commento: {55,} 121
    
    
     } Verifica che   commento: {49,50,51,}  commento: {,}  la variabile LDV_MainClass_C1_variabile_V9 sia  uguale a variabile LDV_MainClass_C1_variabile_V9
     commento: {104,} o  che  commento: {,}  il contatore LDV_MainClass_C1_contatore_Co1 sia  diverso da  commento: {56,} 1152
     commento: {104,} o  che  commento: {,}  il timer LDV_MainClass_C1_timer_T3 sia scaduto
     commento: {104,} e  che  commento: {38,}  il contatore LDV_MainClass_C1_contatore_Co6 non sia  maggiore di  commento: {54,} 13
     commento: {104,} o  che  commento: {38,}  il contatore LDV_MainClass_C1_contatore_Co6 sia  minore di  commento: {55,} contatore LDV_MainClass_C1_contatore_Co4
    
    
     } Verifica che   commento: {47,49,50,52,}   l'argomento argomento_ave3 sia  uguale a  False  commento: {,} 
     commento: {104,} e  che  commento: {,}  il timer LDV_MainClass_C1_timer_T3 non sia disattivo
     commento: {104,} o  che  commento: {,}  la variabile LDV_MainClass_C1_variabile_V8 sia  diverso da  False 
     commento: {104,} e  che  commento: {36,}  il timer LDV_MainClass_C1_timer_T3 non sia scaduto
     commento: {104,} e  che  commento: {34,}  il parametro LDV_MainClass_C1_parametro_P1 non sia  diverso da  True 
    
    
    }
*/
bool L_P1__Macro25(instance_id_t const my_id , C3_Enumerat1 argom44, C3_Enumerat4 argom45, bool argom46, C3_Enumerat4 argom47, C3_Enumerat4 argom48, C3_Enumerat1 argom49, bool argom50)
{
bool res_AndLogicOP_0 = true;
    
    //  *62,* *34,*  se lo stato  è  diverso da  *56,*  state1  *106,* *36,* e  se il timer LDV_MainClass_C1_timer_T3 non è attivo *36,* o  se il timer LDV_MainClass_C1_timer_T3 non è disattivo o  se l'argomento argomento_ave5 è  diverso da avvio *39,*  *36,* o  se il timer LDV_MainClass_C1_timer_T3 non è scaduto, Almeno una delle seguenti { 
    //   *63,* *34,*  se il parametro LDV_MainClass_C1_parametro_P1 è  uguale a  True  *34,* o  se il parametro LDV_MainClass_C1_parametro_P7 non è  minore di  *55,* 4 *36,* e  se il timer LDV_MainClass_C1_timer_T3 è disattivo *38,* o  se il contatore LDV_MainClass_C1_contatore_Co6 è  minore di  *55,* contatore LDV_MainClass_C1_contatore_Co1 *37,* o  se la variabile LDV_MainClass_C1_variabile_V8 è  uguale a  False  e  se il parametro ConsDef è uguale a FALSE , Solo una delle seguenti { 
    //   *63,* *36,*  se il timer LDV_MainClass_C1_timer_T3 è scaduto *38,* e  se il contatore LDV_MainClass_C1_contatore_Co4 è  diverso da  *56,* contatore LDV_MainClass_C1_contatore_Co7 *37,* e  se la variabile LDV_MainClass_C1_variabile_V3 è  uguale a  *53,* 8, Solo una delle seguenti { 
    //   *63,* *34,*  se il parametro LDV_MainClass_C1_parametro_P1 non è  diverso da  True  *34,* e  se il parametro LDV_MainClass_C1_parametro_P1 non è  diverso da  False  e  se l'argomento argomento_ave8 è  diverso da  False  *39,*  e  se l'argomento argomento_ave6 non  è  uguale a RossoGialloGiallo *39,* , Solo una delle seguenti { 
    //   *34,*  se il parametro LDV_MainClass_C1_parametro_P7 è  uguale a  *53,* 1 *37,* e  se la variabile LDV_MainClass_C1_variabile_V8 è  uguale a  False  o  se il parametro ConsDef è uguale a FALSE , Verifica che   *47,49,51,*  *,*  il timer LDV_MainClass_C1_timer_T3 non sia attivo
    //   *104,* o  che  *34,*  il parametro LDV_MainClass_C1_parametro_P1 non sia  uguale a  False 
    //   *104,* o  che  *,*  il contatore LDV_MainClass_C1_contatore_Co6 non sia  diverso da  *56,* 140
    //   *104,* e  che  *36,*  il timer LDV_MainClass_C1_timer_T3 sia attivo
    //   } Verifica che   *47,52,*   l'argomento argomento_ave8 non  sia  diverso da  False  *,* 
    //   *104,* e  che  *34,*  il parametro LDV_MainClass_C1_parametro_P1 sia  uguale a  True 
    //   } Verifica che   *47,49,50,51,*  *,*  la variabile LDV_MainClass_C1_variabile_V9 sia  diverso da c270xx
    //   *104,* o  che  *34,*  il parametro LDV_MainClass_C1_parametro_P1 non sia  diverso da  False 
    //   *104,* o  che  *34,*  il parametro LDV_MainClass_C1_parametro_P1 sia  diverso da  True 
    //   *104,* o  che  *,*  il timer LDV_MainClass_C1_timer_T3 non sia attivo
    //   *104,* e  che   il parametro ConsDef sia uguale a FALSE 
    //   *104,* o  che  *,*  il contatore LDV_MainClass_C1_contatore_Co6 non sia  minore di  *55,* 121
    //   } Verifica che   *49,50,51,*  *,*  la variabile LDV_MainClass_C1_variabile_V9 sia  uguale a variabile LDV_MainClass_C1_variabile_V9
    //   *104,* o  che  *,*  il contatore LDV_MainClass_C1_contatore_Co1 sia  diverso da  *56,* 1152
    //   *104,* o  che  *,*  il timer LDV_MainClass_C1_timer_T3 sia scaduto
    //   *104,* e  che  *38,*  il contatore LDV_MainClass_C1_contatore_Co6 non sia  maggiore di  *54,* 13
    //   *104,* o  che  *38,*  il contatore LDV_MainClass_C1_contatore_Co6 sia  minore di  *55,* contatore LDV_MainClass_C1_contatore_Co4
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_OrLogicOP_4 = false;
    bool res_AndLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1_C3_GetState(my_id) == C3_St_state));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_6);
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! Timer_Attivo(L_P1__GetLdv_m6(my_id)));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_7);
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_AndLogicOP_5);
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! Timer_Disattivo(L_P1__GetLdv_m6(my_id)));
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_NotLogicOP_8);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_OrLogicOP_4);
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (argom48 == avvio));
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_NotLogicOP_9);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! Timer_Scaduto(L_P1__GetLdv_m6(my_id)));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_10);
    
    if(res_OrLogicOP_2){
    bool res_OrLogicOP_11 = false;
    bool res_ImpliesLogicOp_12 = true;
    bool res_OrLogicOP_13 = false;
    bool res_OrLogicOP_14 = false;
    bool res_OrLogicOP_15 = false;
    res_OrLogicOP_15 = (res_OrLogicOP_15 || (L_P1__GetParamLdv_m(my_id) == true));
    bool res_AndLogicOP_16 = true;
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! (L_P1__GetParamLdv_m1(my_id) < 4u));
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_NotLogicOP_17);
    res_AndLogicOP_16 = (res_AndLogicOP_16 && Timer_Disattivo(L_P1__GetLdv_m6(my_id)));
    
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_AndLogicOP_16);
    
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_OrLogicOP_15);
    res_OrLogicOP_14 = (res_OrLogicOP_14 || (Counter_GetValore(L_P1__GetLdv_m9(my_id)) < Counter_GetValore(L_P1__GetLdv_m7(my_id))));
    
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_OrLogicOP_14);
    bool res_AndLogicOP_18 = true;
    res_AndLogicOP_18 = (res_AndLogicOP_18 && (L_P1__GetLdv_m4(my_id) == false));
    res_AndLogicOP_18 = (res_AndLogicOP_18 && (L_P1__GetParamConsd2(my_id) == false));
    
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_AndLogicOP_18);
    
    if(res_OrLogicOP_13){
    bool res_XorLogicOP_19 = true;
    int xorIndex_res_XorLogicOP_19 = 0;
    bool res_ImpliesLogicOp_20 = true;
    bool res_AndLogicOP_21 = true;
    bool res_AndLogicOP_22 = true;
    res_AndLogicOP_22 = (res_AndLogicOP_22 && Timer_Scaduto(L_P1__GetLdv_m6(my_id)));
    bool res_NotLogicOP_23 = true;
    res_NotLogicOP_23 = (res_NotLogicOP_23 && ! (Counter_GetValore(L_P1__GetLdv_m8(my_id)) == Counter_GetValore(L_P1__GetLdv_m10(my_id))));
    res_AndLogicOP_22 = (res_AndLogicOP_22 && res_NotLogicOP_23);
    
    res_AndLogicOP_21 = (res_AndLogicOP_21 && res_AndLogicOP_22);
    res_AndLogicOP_21 = (res_AndLogicOP_21 && (L_P1__GetLdv_m3(my_id) == 8u));
    
    if(res_AndLogicOP_21){
    bool res_XorLogicOP_24 = true;
    int xorIndex_res_XorLogicOP_24 = 0;
    bool res_ImpliesLogicOp_25 = true;
    bool res_AndLogicOP_26 = true;
    bool res_AndLogicOP_27 = true;
    bool res_AndLogicOP_28 = true;
    bool res_NotLogicOP_29 = true;
    bool res_NotLogicOP_30 = true;
    res_NotLogicOP_30 = (res_NotLogicOP_30 && ! (L_P1__GetParamLdv_m(my_id) == true));
    res_NotLogicOP_29 = (res_NotLogicOP_29 && ! res_NotLogicOP_30);
    res_AndLogicOP_28 = (res_AndLogicOP_28 && res_NotLogicOP_29);
    bool res_NotLogicOP_31 = true;
    bool res_NotLogicOP_32 = true;
    res_NotLogicOP_32 = (res_NotLogicOP_32 && ! (L_P1__GetParamLdv_m(my_id) == false));
    res_NotLogicOP_31 = (res_NotLogicOP_31 && ! res_NotLogicOP_32);
    res_AndLogicOP_28 = (res_AndLogicOP_28 && res_NotLogicOP_31);
    
    res_AndLogicOP_27 = (res_AndLogicOP_27 && res_AndLogicOP_28);
    bool res_NotLogicOP_33 = true;
    res_NotLogicOP_33 = (res_NotLogicOP_33 && ! (argom50 == false));
    res_AndLogicOP_27 = (res_AndLogicOP_27 && res_NotLogicOP_33);
    
    res_AndLogicOP_26 = (res_AndLogicOP_26 && res_AndLogicOP_27);
    bool res_NotLogicOP_34 = true;
    res_NotLogicOP_34 = (res_NotLogicOP_34 && ! (argom49 == rossogiallo5));
    res_AndLogicOP_26 = (res_AndLogicOP_26 && res_NotLogicOP_34);
    
    if(res_AndLogicOP_26){
    bool res_ImpliesLogicOp_35 = true;
    bool res_OrLogicOP_36 = false;
    bool res_AndLogicOP_37 = true;
    res_AndLogicOP_37 = (res_AndLogicOP_37 && (L_P1__GetParamLdv_m1(my_id) == 1u));
    res_AndLogicOP_37 = (res_AndLogicOP_37 && (L_P1__GetLdv_m4(my_id) == false));
    
    res_OrLogicOP_36 = (res_OrLogicOP_36 || res_AndLogicOP_37);
    res_OrLogicOP_36 = (res_OrLogicOP_36 || (L_P1__GetParamConsd2(my_id) == false));
    
    if(res_OrLogicOP_36){
    bool res_OrLogicOP_38 = false;
    bool res_OrLogicOP_39 = false;
    bool res_NotLogicOP_40 = true;
    res_NotLogicOP_40 = (res_NotLogicOP_40 && ! Timer_Attivo(L_P1__GetLdv_m6(my_id)));
    res_OrLogicOP_39 = (res_OrLogicOP_39 || res_NotLogicOP_40);
    bool res_NotLogicOP_41 = true;
    res_NotLogicOP_41 = (res_NotLogicOP_41 && ! (L_P1__GetParamLdv_m(my_id) == false));
    res_OrLogicOP_39 = (res_OrLogicOP_39 || res_NotLogicOP_41);
    
    res_OrLogicOP_38 = (res_OrLogicOP_38 || res_OrLogicOP_39);
    bool res_AndLogicOP_42 = true;
    bool res_NotLogicOP_43 = true;
    bool res_NotLogicOP_44 = true;
    res_NotLogicOP_44 = (res_NotLogicOP_44 && ! (Counter_GetValore(L_P1__GetLdv_m9(my_id)) == 140u));
    res_NotLogicOP_43 = (res_NotLogicOP_43 && ! res_NotLogicOP_44);
    res_AndLogicOP_42 = (res_AndLogicOP_42 && res_NotLogicOP_43);
    res_AndLogicOP_42 = (res_AndLogicOP_42 && Timer_Attivo(L_P1__GetLdv_m6(my_id)));
    
    res_OrLogicOP_38 = (res_OrLogicOP_38 || res_AndLogicOP_42);
    
    res_ImpliesLogicOp_35 = (res_ImpliesLogicOp_35 && res_OrLogicOP_38);
    }
    res_ImpliesLogicOp_25 = (res_ImpliesLogicOp_25 && res_ImpliesLogicOp_35);
    }
    if(res_ImpliesLogicOp_25){
    xorIndex_res_XorLogicOP_24 = (xorIndex_res_XorLogicOP_24 + 1);
    }
    bool res_AndLogicOP_45 = true;
    bool res_NotLogicOP_46 = true;
    bool res_NotLogicOP_47 = true;
    res_NotLogicOP_47 = (res_NotLogicOP_47 && ! (argom50 == false));
    res_NotLogicOP_46 = (res_NotLogicOP_46 && ! res_NotLogicOP_47);
    res_AndLogicOP_45 = (res_AndLogicOP_45 && res_NotLogicOP_46);
    res_AndLogicOP_45 = (res_AndLogicOP_45 && (L_P1__GetParamLdv_m(my_id) == true));
    
    if(res_AndLogicOP_45){
    xorIndex_res_XorLogicOP_24 = (xorIndex_res_XorLogicOP_24 + 1);
    }
    
    res_XorLogicOP_24 = (res_XorLogicOP_24 && (xorIndex_res_XorLogicOP_24 == 1));
    res_ImpliesLogicOp_20 = (res_ImpliesLogicOp_20 && res_XorLogicOP_24);
    }
    if(res_ImpliesLogicOp_20){
    xorIndex_res_XorLogicOP_19 = (xorIndex_res_XorLogicOP_19 + 1);
    }
    bool res_OrLogicOP_48 = false;
    bool res_OrLogicOP_49 = false;
    bool res_OrLogicOP_50 = false;
    bool res_OrLogicOP_51 = false;
    bool res_NotLogicOP_52 = true;
    res_NotLogicOP_52 = (res_NotLogicOP_52 && ! (L_P1__GetLdv_m5(my_id) == c270xx));
    res_OrLogicOP_51 = (res_OrLogicOP_51 || res_NotLogicOP_52);
    bool res_NotLogicOP_53 = true;
    bool res_NotLogicOP_54 = true;
    res_NotLogicOP_54 = (res_NotLogicOP_54 && ! (L_P1__GetParamLdv_m(my_id) == false));
    res_NotLogicOP_53 = (res_NotLogicOP_53 && ! res_NotLogicOP_54);
    res_OrLogicOP_51 = (res_OrLogicOP_51 || res_NotLogicOP_53);
    
    res_OrLogicOP_50 = (res_OrLogicOP_50 || res_OrLogicOP_51);
    bool res_NotLogicOP_55 = true;
    res_NotLogicOP_55 = (res_NotLogicOP_55 && ! (L_P1__GetParamLdv_m(my_id) == true));
    res_OrLogicOP_50 = (res_OrLogicOP_50 || res_NotLogicOP_55);
    
    res_OrLogicOP_49 = (res_OrLogicOP_49 || res_OrLogicOP_50);
    bool res_AndLogicOP_56 = true;
    bool res_NotLogicOP_57 = true;
    res_NotLogicOP_57 = (res_NotLogicOP_57 && ! Timer_Attivo(L_P1__GetLdv_m6(my_id)));
    res_AndLogicOP_56 = (res_AndLogicOP_56 && res_NotLogicOP_57);
    res_AndLogicOP_56 = (res_AndLogicOP_56 && (L_P1__GetParamConsd2(my_id) == false));
    
    res_OrLogicOP_49 = (res_OrLogicOP_49 || res_AndLogicOP_56);
    
    res_OrLogicOP_48 = (res_OrLogicOP_48 || res_OrLogicOP_49);
    bool res_NotLogicOP_58 = true;
    res_NotLogicOP_58 = (res_NotLogicOP_58 && ! (Counter_GetValore(L_P1__GetLdv_m9(my_id)) < 121u));
    res_OrLogicOP_48 = (res_OrLogicOP_48 || res_NotLogicOP_58);
    
    if(res_OrLogicOP_48){
    xorIndex_res_XorLogicOP_19 = (xorIndex_res_XorLogicOP_19 + 1);
    }
    
    res_XorLogicOP_19 = (res_XorLogicOP_19 && (xorIndex_res_XorLogicOP_19 == 1));
    res_ImpliesLogicOp_12 = (res_ImpliesLogicOp_12 && res_XorLogicOP_19);
    }
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_ImpliesLogicOp_12);
    bool res_OrLogicOP_59 = false;
    bool res_OrLogicOP_60 = false;
    bool res_OrLogicOP_61 = false;
    res_OrLogicOP_61 = (res_OrLogicOP_61 || (L_P1__GetLdv_m5(my_id) == L_P1__GetLdv_m5(my_id)));
    bool res_NotLogicOP_62 = true;
    res_NotLogicOP_62 = (res_NotLogicOP_62 && ! (Counter_GetValore(L_P1__GetLdv_m7(my_id)) == 1152u));
    res_OrLogicOP_61 = (res_OrLogicOP_61 || res_NotLogicOP_62);
    
    res_OrLogicOP_60 = (res_OrLogicOP_60 || res_OrLogicOP_61);
    bool res_AndLogicOP_63 = true;
    res_AndLogicOP_63 = (res_AndLogicOP_63 && Timer_Scaduto(L_P1__GetLdv_m6(my_id)));
    bool res_NotLogicOP_64 = true;
    res_NotLogicOP_64 = (res_NotLogicOP_64 && ! (Counter_GetValore(L_P1__GetLdv_m9(my_id)) > 13u));
    res_AndLogicOP_63 = (res_AndLogicOP_63 && res_NotLogicOP_64);
    
    res_OrLogicOP_60 = (res_OrLogicOP_60 || res_AndLogicOP_63);
    
    res_OrLogicOP_59 = (res_OrLogicOP_59 || res_OrLogicOP_60);
    res_OrLogicOP_59 = (res_OrLogicOP_59 || (Counter_GetValore(L_P1__GetLdv_m9(my_id)) < Counter_GetValore(L_P1__GetLdv_m8(my_id))));
    
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_OrLogicOP_59);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_OrLogicOP_11);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *47,49,50,52,*   l'argomento argomento_ave3 sia  uguale a  False  *,* 
    //   *104,* e  che  *,*  il timer LDV_MainClass_C1_timer_T3 non sia disattivo
    //   *104,* o  che  *,*  la variabile LDV_MainClass_C1_variabile_V8 sia  diverso da  False 
    //   *104,* e  che  *36,*  il timer LDV_MainClass_C1_timer_T3 non sia scaduto
    //   *104,* e  che  *34,*  il parametro LDV_MainClass_C1_parametro_P1 non sia  diverso da  True
    bool res_OrLogicOP_65 = false;
    bool res_AndLogicOP_66 = true;
    res_AndLogicOP_66 = (res_AndLogicOP_66 && (argom46 == false));
    bool res_NotLogicOP_67 = true;
    res_NotLogicOP_67 = (res_NotLogicOP_67 && ! Timer_Disattivo(L_P1__GetLdv_m6(my_id)));
    res_AndLogicOP_66 = (res_AndLogicOP_66 && res_NotLogicOP_67);
    
    res_OrLogicOP_65 = (res_OrLogicOP_65 || res_AndLogicOP_66);
    bool res_AndLogicOP_68 = true;
    bool res_AndLogicOP_69 = true;
    bool res_NotLogicOP_70 = true;
    res_NotLogicOP_70 = (res_NotLogicOP_70 && ! (L_P1__GetLdv_m4(my_id) == false));
    res_AndLogicOP_69 = (res_AndLogicOP_69 && res_NotLogicOP_70);
    bool res_NotLogicOP_71 = true;
    res_NotLogicOP_71 = (res_NotLogicOP_71 && ! Timer_Scaduto(L_P1__GetLdv_m6(my_id)));
    res_AndLogicOP_69 = (res_AndLogicOP_69 && res_NotLogicOP_71);
    
    res_AndLogicOP_68 = (res_AndLogicOP_68 && res_AndLogicOP_69);
    bool res_NotLogicOP_72 = true;
    bool res_NotLogicOP_73 = true;
    res_NotLogicOP_73 = (res_NotLogicOP_73 && ! (L_P1__GetParamLdv_m(my_id) == true));
    res_NotLogicOP_72 = (res_NotLogicOP_72 && ! res_NotLogicOP_73);
    res_AndLogicOP_68 = (res_AndLogicOP_68 && res_NotLogicOP_72);
    
    res_OrLogicOP_65 = (res_OrLogicOP_65 || res_AndLogicOP_68);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_65);
    
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
    
    { commento: {62,} commento: {38,}  se il contatore LDV_MainClass_C1_contatore_Co6 è  minore di  commento: {55,} contatore LDV_MainClass_C1_contatore_Co7 commento: {37,} o  se la variabile LDV_MainClass_C1_variabile_V8 non è  diverso da  False , Almeno una delle seguenti { 
     commento: {62,} commento: {34,}  se il parametro LDV_MainClass_C1_parametro_P9 non è  diverso da RossoGialloGiallo e  se l'argomento argomento_ave1 non  è  uguale a c270xx commento: {39,} , Almeno una delle seguenti { 
     commento: {61,}  se il parametro ConsDef è uguale a FALSE  commento: {38,} e  se il contatore LDV_MainClass_C1_contatore_Co6 non è  minore di  commento: {55,} 143 o  se il parametro ConsDef è uguale a FALSE  commento: {36,} e  se il timer LDV_MainClass_C1_timer_T3 è disattivo o  se il parametro ConsDef è uguale a FALSE  commento: {37,} e  se la variabile LDV_MainClass_C1_variabile_V3 è  maggiore di  commento: {54,} 9, Tutte le seguenti { 
     commento: {62,}  se il parametro ConsDef è uguale a FALSE  commento: {34,} o  se il parametro LDV_MainClass_C1_parametro_P9 non è  uguale a RossoGialloGiallo commento: {37,} e  se la variabile LDV_MainClass_C1_variabile_V9 è  uguale a c270xx commento: {36,} e  se il timer LDV_MainClass_C1_timer_T3 è scaduto o  se l'argomento argomento_ave7 non  è  diverso da  False  commento: {39,} , Almeno una delle seguenti { 
     commento: {62,}  se la macro  LDV_MainClass_C1_macrova_M1 ( con argomento_a2   uguale a True ,argomento_a7   uguale a c180 ,argomento_a6   uguale a RossoGialloGiallo  e argomento_a8   uguale a RossoGialloGiallo )  non  è  diverso da  True  commento: {40,}  commento: {34,} e  se il parametro LDV_MainClass_C1_parametro_P1 non è  uguale a  False  commento: {37,} o  se la variabile LDV_MainClass_C1_variabile_V8 non è  diverso da  True  e  se l'argomento argomento_ave1 è  uguale a c270xx commento: {39,}  commento: {34,} o  se il parametro LDV_MainClass_C1_parametro_P7 è  maggiore di  commento: {54,} 2, Almeno una delle seguenti { 
     commento: {62,}  se il parametro ConsDef è uguale a FALSE  commento: {34,} e  se il parametro LDV_MainClass_C1_parametro_P9 non è  diverso da RossoGialloGiallo commento: {37,} o  se la variabile LDV_MainClass_C1_variabile_V8 è  diverso da  False  commento: {36,} e  se il timer LDV_MainClass_C1_timer_T3 non è disattivo commento: {34,} o  se il parametro LDV_MainClass_C1_parametro_P7 non è  maggiore di  commento: {54,} 10, Almeno una delle seguenti { 
     commento: {34,}  se lo stato  è  uguale a  commento: {53,}  state1  commento: {106,} commento: {34,} o  se il parametro LDV_MainClass_C1_parametro_P1 non è  diverso da  True  o  se il parametro ConsDef è uguale a FALSE  commento: {36,} o  se il timer LDV_MainClass_C1_timer_T3 è scaduto o  se il parametro ConsDef è uguale a FALSE , Verifica che   commento: {47,51,}  commento: {,}  il contatore LDV_MainClass_C1_contatore_Co6 sia  maggiore di  commento: {54,} 11
     commento: {104,} e  che  commento: {38,}  il contatore LDV_MainClass_C1_contatore_Co4 sia  uguale a  commento: {53,} 12
     commento: {104,} o  che  commento: {34,}  il parametro LDV_MainClass_C1_parametro_P7 sia  minore di  commento: {55,} 10
    
    
     } Verifica che   commento: {50,52,}   l'argomento argomento_ave1 sia  diverso da c270xx commento: {,} 
     commento: {104,} e  che  commento: {,}  la variabile LDV_MainClass_C1_variabile_V3 sia  uguale a  commento: {53,} 8
    
    
     } Verifica che   commento: {47,}   il parametro ConsDef sia uguale a FALSE 
     commento: {104,} e  che   il parametro ConsDef sia uguale a FALSE 
    
    
     } Verifica che   commento: {47,}   il parametro ConsDef sia uguale a FALSE 
    
    
     } Verifica che   commento: {47,49,50,51,52,}   l'argomento argomento_ave10 sia  uguale a avvio commento: {,} 
     commento: {104,} o  che  commento: {,}  il timer LDV_MainClass_C1_timer_T3 sia disattivo
     commento: {104,} o  che  commento: {,}  il contatore LDV_MainClass_C1_contatore_Co6 sia  maggiore di  commento: {54,} contatore LDV_MainClass_C1_contatore_Co7
     commento: {104,} e  che  commento: {,}  la variabile LDV_MainClass_C1_variabile_V8 sia  uguale a  False 
     commento: {104,} e  che  commento: {34,}  il parametro LDV_MainClass_C1_parametro_P1 non sia  uguale a  False 
     commento: {104,} e  che  commento: {34,}  il parametro LDV_MainClass_C1_parametro_P7 non sia  diverso da  commento: {56,} 7
    
    
     } Verifica che   commento: {47,49,51,52,}   l'argomento argomento_ave10 non  sia  diverso da avvio commento: {,} 
     commento: {104,} e  che  commento: {,}  il timer LDV_MainClass_C1_timer_T3 sia attivo
     commento: {104,} e  che   il parametro ConsDef sia uguale a FALSE 
     commento: {104,} e  che  commento: {,}  il contatore LDV_MainClass_C1_contatore_Co4 non sia  uguale a  commento: {53,} 121
    
    
     } Verifica che   commento: {49,50,51,52,}  commento: {,}  la variabile LDV_MainClass_C1_variabile_V9 non sia  diverso da c270xx
     commento: {104,} o  che   l'argomento argomento_ave10 sia  diverso da avvio commento: {,} 
     commento: {104,} e  che  commento: {,}  il timer LDV_MainClass_C1_timer_T3 sia disattivo
     commento: {104,} o  che  commento: {,}  il contatore LDV_MainClass_C1_contatore_Co6 sia  diverso da  commento: {56,} 11
     commento: {104,} o  che  commento: {38,}  il contatore LDV_MainClass_C1_contatore_Co6 non sia  diverso da  commento: {56,} contatore LDV_MainClass_C1_contatore_Co7
    
    
    }
*/
bool L_P1__Macro26(instance_id_t const my_id , C3_Enumerat3 argom51, C3_Enumerat4 argom52, C3_Enumerat3 argom53, C3_Enumerat1 argom54, bool argom55, C3_Enumerat3 argom56, C3_Enumerat4 argom57)
{
bool res_AndLogicOP_0 = true;
    
    //  *62,* *38,*  se il contatore LDV_MainClass_C1_contatore_Co6 è  minore di  *55,* contatore LDV_MainClass_C1_contatore_Co7 *37,* o  se la variabile LDV_MainClass_C1_variabile_V8 non è  diverso da  False , Almeno una delle seguenti { 
    //   *62,* *34,*  se il parametro LDV_MainClass_C1_parametro_P9 non è  diverso da RossoGialloGiallo e  se l'argomento argomento_ave1 non  è  uguale a c270xx *39,* , Almeno una delle seguenti { 
    //   *61,*  se il parametro ConsDef è uguale a FALSE  *38,* e  se il contatore LDV_MainClass_C1_contatore_Co6 non è  minore di  *55,* 143 o  se il parametro ConsDef è uguale a FALSE  *36,* e  se il timer LDV_MainClass_C1_timer_T3 è disattivo o  se il parametro ConsDef è uguale a FALSE  *37,* e  se la variabile LDV_MainClass_C1_variabile_V3 è  maggiore di  *54,* 9, Tutte le seguenti { 
    //   *62,*  se il parametro ConsDef è uguale a FALSE  *34,* o  se il parametro LDV_MainClass_C1_parametro_P9 non è  uguale a RossoGialloGiallo *37,* e  se la variabile LDV_MainClass_C1_variabile_V9 è  uguale a c270xx *36,* e  se il timer LDV_MainClass_C1_timer_T3 è scaduto o  se l'argomento argomento_ave7 non  è  diverso da  False  *39,* , Almeno una delle seguenti { 
    //   *62,*  se la macro  LDV_MainClass_C1_macrova_M1 ( con argomento_a2   uguale a True ,argomento_a7   uguale a c180 ,argomento_a6   uguale a RossoGialloGiallo  e argomento_a8   uguale a RossoGialloGiallo )  non  è  diverso da  True  *40,*  *34,* e  se il parametro LDV_MainClass_C1_parametro_P1 non è  uguale a  False  *37,* o  se la variabile LDV_MainClass_C1_variabile_V8 non è  diverso da  True  e  se l'argomento argomento_ave1 è  uguale a c270xx *39,*  *34,* o  se il parametro LDV_MainClass_C1_parametro_P7 è  maggiore di  *54,* 2, Almeno una delle seguenti { 
    //   *62,*  se il parametro ConsDef è uguale a FALSE  *34,* e  se il parametro LDV_MainClass_C1_parametro_P9 non è  diverso da RossoGialloGiallo *37,* o  se la variabile LDV_MainClass_C1_variabile_V8 è  diverso da  False  *36,* e  se il timer LDV_MainClass_C1_timer_T3 non è disattivo *34,* o  se il parametro LDV_MainClass_C1_parametro_P7 non è  maggiore di  *54,* 10, Almeno una delle seguenti { 
    //   *34,*  se lo stato  è  uguale a  *53,*  state1  *106,* *34,* o  se il parametro LDV_MainClass_C1_parametro_P1 non è  diverso da  True  o  se il parametro ConsDef è uguale a FALSE  *36,* o  se il timer LDV_MainClass_C1_timer_T3 è scaduto o  se il parametro ConsDef è uguale a FALSE , Verifica che   *47,51,*  *,*  il contatore LDV_MainClass_C1_contatore_Co6 sia  maggiore di  *54,* 11
    //   *104,* e  che  *38,*  il contatore LDV_MainClass_C1_contatore_Co4 sia  uguale a  *53,* 12
    //   *104,* o  che  *34,*  il parametro LDV_MainClass_C1_parametro_P7 sia  minore di  *55,* 10
    //   } Verifica che   *50,52,*   l'argomento argomento_ave1 sia  diverso da c270xx *,* 
    //   *104,* e  che  *,*  la variabile LDV_MainClass_C1_variabile_V3 sia  uguale a  *53,* 8
    //   } Verifica che   *47,*   il parametro ConsDef sia uguale a FALSE 
    //   *104,* e  che   il parametro ConsDef sia uguale a FALSE 
    //   } Verifica che   *47,*   il parametro ConsDef sia uguale a FALSE 
    //   } Verifica che   *47,49,50,51,52,*   l'argomento argomento_ave10 sia  uguale a avvio *,* 
    //   *104,* o  che  *,*  il timer LDV_MainClass_C1_timer_T3 sia disattivo
    //   *104,* o  che  *,*  il contatore LDV_MainClass_C1_contatore_Co6 sia  maggiore di  *54,* contatore LDV_MainClass_C1_contatore_Co7
    //   *104,* e  che  *,*  la variabile LDV_MainClass_C1_variabile_V8 sia  uguale a  False 
    //   *104,* e  che  *34,*  il parametro LDV_MainClass_C1_parametro_P1 non sia  uguale a  False 
    //   *104,* e  che  *34,*  il parametro LDV_MainClass_C1_parametro_P7 non sia  diverso da  *56,* 7
    //   } Verifica che   *47,49,51,52,*   l'argomento argomento_ave10 non  sia  diverso da avvio *,* 
    //   *104,* e  che  *,*  il timer LDV_MainClass_C1_timer_T3 sia attivo
    //   *104,* e  che   il parametro ConsDef sia uguale a FALSE 
    //   *104,* e  che  *,*  il contatore LDV_MainClass_C1_contatore_Co4 non sia  uguale a  *53,* 121
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    res_OrLogicOP_2 = (res_OrLogicOP_2 || (Counter_GetValore(L_P1__GetLdv_m9(my_id)) < Counter_GetValore(L_P1__GetLdv_m10(my_id))));
    bool res_NotLogicOP_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetLdv_m4(my_id) == false));
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! res_NotLogicOP_4);
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_3);
    
    if(res_OrLogicOP_2){
    bool res_OrLogicOP_5 = false;
    bool res_ImpliesLogicOp_6 = true;
    bool res_AndLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetParamLdv_m2(my_id) == rossogiallo5));
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! res_NotLogicOP_9);
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_8);
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (argom51 == c270xx));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_10);
    
    if(res_AndLogicOP_7){
    bool res_OrLogicOP_11 = false;
    bool res_ImpliesLogicOp_12 = true;
    bool res_OrLogicOP_13 = false;
    bool res_OrLogicOP_14 = false;
    bool res_AndLogicOP_15 = true;
    res_AndLogicOP_15 = (res_AndLogicOP_15 && (L_P1__GetParamConsd2(my_id) == false));
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (Counter_GetValore(L_P1__GetLdv_m9(my_id)) < 143u));
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_NotLogicOP_16);
    
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_AndLogicOP_15);
    bool res_AndLogicOP_17 = true;
    res_AndLogicOP_17 = (res_AndLogicOP_17 && (L_P1__GetParamConsd2(my_id) == false));
    res_AndLogicOP_17 = (res_AndLogicOP_17 && Timer_Disattivo(L_P1__GetLdv_m6(my_id)));
    
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_AndLogicOP_17);
    
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_OrLogicOP_14);
    bool res_AndLogicOP_18 = true;
    res_AndLogicOP_18 = (res_AndLogicOP_18 && (L_P1__GetParamConsd2(my_id) == false));
    res_AndLogicOP_18 = (res_AndLogicOP_18 && (L_P1__GetLdv_m3(my_id) > 9u));
    
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_AndLogicOP_18);
    
    if(res_OrLogicOP_13){
    bool res_AndLogicOP_19 = true;
    bool res_ImpliesLogicOp_20 = true;
    bool res_OrLogicOP_21 = false;
    bool res_OrLogicOP_22 = false;
    res_OrLogicOP_22 = (res_OrLogicOP_22 || (L_P1__GetParamConsd2(my_id) == false));
    bool res_AndLogicOP_23 = true;
    bool res_AndLogicOP_24 = true;
    bool res_NotLogicOP_25 = true;
    res_NotLogicOP_25 = (res_NotLogicOP_25 && ! (L_P1__GetParamLdv_m2(my_id) == rossogiallo5));
    res_AndLogicOP_24 = (res_AndLogicOP_24 && res_NotLogicOP_25);
    res_AndLogicOP_24 = (res_AndLogicOP_24 && (L_P1__GetLdv_m5(my_id) == c270xx));
    
    res_AndLogicOP_23 = (res_AndLogicOP_23 && res_AndLogicOP_24);
    res_AndLogicOP_23 = (res_AndLogicOP_23 && Timer_Scaduto(L_P1__GetLdv_m6(my_id)));
    
    res_OrLogicOP_22 = (res_OrLogicOP_22 || res_AndLogicOP_23);
    
    res_OrLogicOP_21 = (res_OrLogicOP_21 || res_OrLogicOP_22);
    bool res_NotLogicOP_26 = true;
    bool res_NotLogicOP_27 = true;
    res_NotLogicOP_27 = (res_NotLogicOP_27 && ! (argom55 == false));
    res_NotLogicOP_26 = (res_NotLogicOP_26 && ! res_NotLogicOP_27);
    res_OrLogicOP_21 = (res_OrLogicOP_21 || res_NotLogicOP_26);
    
    if(res_OrLogicOP_21){
    bool res_OrLogicOP_28 = false;
    bool res_ImpliesLogicOp_29 = true;
    bool res_OrLogicOP_30 = false;
    bool res_OrLogicOP_31 = false;
    bool res_AndLogicOP_32 = true;
    bool res_NotLogicOP_33 = true;
    bool res_NotLogicOP_34 = true;
    res_NotLogicOP_34 = (res_NotLogicOP_34 && ! (L_P1__Macro22(my_id,true,rossogiallo5,c180,rossogiallo5) == true));
    res_NotLogicOP_33 = (res_NotLogicOP_33 && ! res_NotLogicOP_34);
    res_AndLogicOP_32 = (res_AndLogicOP_32 && res_NotLogicOP_33);
    bool res_NotLogicOP_35 = true;
    res_NotLogicOP_35 = (res_NotLogicOP_35 && ! (L_P1__GetParamLdv_m(my_id) == false));
    res_AndLogicOP_32 = (res_AndLogicOP_32 && res_NotLogicOP_35);
    
    res_OrLogicOP_31 = (res_OrLogicOP_31 || res_AndLogicOP_32);
    bool res_AndLogicOP_36 = true;
    bool res_NotLogicOP_37 = true;
    bool res_NotLogicOP_38 = true;
    res_NotLogicOP_38 = (res_NotLogicOP_38 && ! (L_P1__GetLdv_m4(my_id) == true));
    res_NotLogicOP_37 = (res_NotLogicOP_37 && ! res_NotLogicOP_38);
    res_AndLogicOP_36 = (res_AndLogicOP_36 && res_NotLogicOP_37);
    res_AndLogicOP_36 = (res_AndLogicOP_36 && (argom51 == c270xx));
    
    res_OrLogicOP_31 = (res_OrLogicOP_31 || res_AndLogicOP_36);
    
    res_OrLogicOP_30 = (res_OrLogicOP_30 || res_OrLogicOP_31);
    res_OrLogicOP_30 = (res_OrLogicOP_30 || (L_P1__GetParamLdv_m1(my_id) > 2u));
    
    if(res_OrLogicOP_30){
    bool res_OrLogicOP_39 = false;
    bool res_ImpliesLogicOp_40 = true;
    bool res_OrLogicOP_41 = false;
    bool res_OrLogicOP_42 = false;
    bool res_AndLogicOP_43 = true;
    res_AndLogicOP_43 = (res_AndLogicOP_43 && (L_P1__GetParamConsd2(my_id) == false));
    bool res_NotLogicOP_44 = true;
    bool res_NotLogicOP_45 = true;
    res_NotLogicOP_45 = (res_NotLogicOP_45 && ! (L_P1__GetParamLdv_m2(my_id) == rossogiallo5));
    res_NotLogicOP_44 = (res_NotLogicOP_44 && ! res_NotLogicOP_45);
    res_AndLogicOP_43 = (res_AndLogicOP_43 && res_NotLogicOP_44);
    
    res_OrLogicOP_42 = (res_OrLogicOP_42 || res_AndLogicOP_43);
    bool res_AndLogicOP_46 = true;
    bool res_NotLogicOP_47 = true;
    res_NotLogicOP_47 = (res_NotLogicOP_47 && ! (L_P1__GetLdv_m4(my_id) == false));
    res_AndLogicOP_46 = (res_AndLogicOP_46 && res_NotLogicOP_47);
    bool res_NotLogicOP_48 = true;
    res_NotLogicOP_48 = (res_NotLogicOP_48 && ! Timer_Disattivo(L_P1__GetLdv_m6(my_id)));
    res_AndLogicOP_46 = (res_AndLogicOP_46 && res_NotLogicOP_48);
    
    res_OrLogicOP_42 = (res_OrLogicOP_42 || res_AndLogicOP_46);
    
    res_OrLogicOP_41 = (res_OrLogicOP_41 || res_OrLogicOP_42);
    bool res_NotLogicOP_49 = true;
    res_NotLogicOP_49 = (res_NotLogicOP_49 && ! (L_P1__GetParamLdv_m1(my_id) > 10u));
    res_OrLogicOP_41 = (res_OrLogicOP_41 || res_NotLogicOP_49);
    
    if(res_OrLogicOP_41){
    bool res_ImpliesLogicOp_50 = true;
    bool res_OrLogicOP_51 = false;
    bool res_OrLogicOP_52 = false;
    bool res_OrLogicOP_53 = false;
    bool res_OrLogicOP_54 = false;
    res_OrLogicOP_54 = (res_OrLogicOP_54 || (L_P1_C3_GetState(my_id) == C3_St_state));
    bool res_NotLogicOP_55 = true;
    bool res_NotLogicOP_56 = true;
    res_NotLogicOP_56 = (res_NotLogicOP_56 && ! (L_P1__GetParamLdv_m(my_id) == true));
    res_NotLogicOP_55 = (res_NotLogicOP_55 && ! res_NotLogicOP_56);
    res_OrLogicOP_54 = (res_OrLogicOP_54 || res_NotLogicOP_55);
    
    res_OrLogicOP_53 = (res_OrLogicOP_53 || res_OrLogicOP_54);
    res_OrLogicOP_53 = (res_OrLogicOP_53 || (L_P1__GetParamConsd2(my_id) == false));
    
    res_OrLogicOP_52 = (res_OrLogicOP_52 || res_OrLogicOP_53);
    res_OrLogicOP_52 = (res_OrLogicOP_52 || Timer_Scaduto(L_P1__GetLdv_m6(my_id)));
    
    res_OrLogicOP_51 = (res_OrLogicOP_51 || res_OrLogicOP_52);
    res_OrLogicOP_51 = (res_OrLogicOP_51 || (L_P1__GetParamConsd2(my_id) == false));
    
    if(res_OrLogicOP_51){
    bool res_OrLogicOP_57 = false;
    bool res_AndLogicOP_58 = true;
    res_AndLogicOP_58 = (res_AndLogicOP_58 && (Counter_GetValore(L_P1__GetLdv_m9(my_id)) > 11u));
    res_AndLogicOP_58 = (res_AndLogicOP_58 && (Counter_GetValore(L_P1__GetLdv_m8(my_id)) == 12u));
    
    res_OrLogicOP_57 = (res_OrLogicOP_57 || res_AndLogicOP_58);
    res_OrLogicOP_57 = (res_OrLogicOP_57 || (L_P1__GetParamLdv_m1(my_id) < 10u));
    
    res_ImpliesLogicOp_50 = (res_ImpliesLogicOp_50 && res_OrLogicOP_57);
    }
    res_ImpliesLogicOp_40 = (res_ImpliesLogicOp_40 && res_ImpliesLogicOp_50);
    }
    res_OrLogicOP_39 = (res_OrLogicOP_39 || res_ImpliesLogicOp_40);
    bool res_AndLogicOP_59 = true;
    bool res_NotLogicOP_60 = true;
    res_NotLogicOP_60 = (res_NotLogicOP_60 && ! (argom51 == c270xx));
    res_AndLogicOP_59 = (res_AndLogicOP_59 && res_NotLogicOP_60);
    res_AndLogicOP_59 = (res_AndLogicOP_59 && (L_P1__GetLdv_m3(my_id) == 8u));
    
    res_OrLogicOP_39 = (res_OrLogicOP_39 || res_AndLogicOP_59);
    
    res_ImpliesLogicOp_29 = (res_ImpliesLogicOp_29 && res_OrLogicOP_39);
    }
    res_OrLogicOP_28 = (res_OrLogicOP_28 || res_ImpliesLogicOp_29);
    bool res_AndLogicOP_61 = true;
    res_AndLogicOP_61 = (res_AndLogicOP_61 && (L_P1__GetParamConsd2(my_id) == false));
    res_AndLogicOP_61 = (res_AndLogicOP_61 && (L_P1__GetParamConsd2(my_id) == false));
    
    res_OrLogicOP_28 = (res_OrLogicOP_28 || res_AndLogicOP_61);
    
    res_ImpliesLogicOp_20 = (res_ImpliesLogicOp_20 && res_OrLogicOP_28);
    }
    res_AndLogicOP_19 = (res_AndLogicOP_19 && res_ImpliesLogicOp_20);
    res_AndLogicOP_19 = (res_AndLogicOP_19 && (L_P1__GetParamConsd2(my_id) == false));
    
    res_ImpliesLogicOp_12 = (res_ImpliesLogicOp_12 && res_AndLogicOP_19);
    }
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_ImpliesLogicOp_12);
    bool res_OrLogicOP_62 = false;
    bool res_OrLogicOP_63 = false;
    res_OrLogicOP_63 = (res_OrLogicOP_63 || (argom52 == avvio));
    res_OrLogicOP_63 = (res_OrLogicOP_63 || Timer_Disattivo(L_P1__GetLdv_m6(my_id)));
    
    res_OrLogicOP_62 = (res_OrLogicOP_62 || res_OrLogicOP_63);
    bool res_AndLogicOP_64 = true;
    bool res_AndLogicOP_65 = true;
    bool res_AndLogicOP_66 = true;
    res_AndLogicOP_66 = (res_AndLogicOP_66 && (Counter_GetValore(L_P1__GetLdv_m9(my_id)) > Counter_GetValore(L_P1__GetLdv_m10(my_id))));
    res_AndLogicOP_66 = (res_AndLogicOP_66 && (L_P1__GetLdv_m4(my_id) == false));
    
    res_AndLogicOP_65 = (res_AndLogicOP_65 && res_AndLogicOP_66);
    bool res_NotLogicOP_67 = true;
    res_NotLogicOP_67 = (res_NotLogicOP_67 && ! (L_P1__GetParamLdv_m(my_id) == false));
    res_AndLogicOP_65 = (res_AndLogicOP_65 && res_NotLogicOP_67);
    
    res_AndLogicOP_64 = (res_AndLogicOP_64 && res_AndLogicOP_65);
    bool res_NotLogicOP_68 = true;
    bool res_NotLogicOP_69 = true;
    res_NotLogicOP_69 = (res_NotLogicOP_69 && ! (L_P1__GetParamLdv_m1(my_id) == 7u));
    res_NotLogicOP_68 = (res_NotLogicOP_68 && ! res_NotLogicOP_69);
    res_AndLogicOP_64 = (res_AndLogicOP_64 && res_NotLogicOP_68);
    
    res_OrLogicOP_62 = (res_OrLogicOP_62 || res_AndLogicOP_64);
    
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_OrLogicOP_62);
    
    res_ImpliesLogicOp_6 = (res_ImpliesLogicOp_6 && res_OrLogicOP_11);
    }
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_ImpliesLogicOp_6);
    bool res_AndLogicOP_70 = true;
    bool res_AndLogicOP_71 = true;
    bool res_AndLogicOP_72 = true;
    bool res_NotLogicOP_73 = true;
    bool res_NotLogicOP_74 = true;
    res_NotLogicOP_74 = (res_NotLogicOP_74 && ! (argom52 == avvio));
    res_NotLogicOP_73 = (res_NotLogicOP_73 && ! res_NotLogicOP_74);
    res_AndLogicOP_72 = (res_AndLogicOP_72 && res_NotLogicOP_73);
    res_AndLogicOP_72 = (res_AndLogicOP_72 && Timer_Attivo(L_P1__GetLdv_m6(my_id)));
    
    res_AndLogicOP_71 = (res_AndLogicOP_71 && res_AndLogicOP_72);
    res_AndLogicOP_71 = (res_AndLogicOP_71 && (L_P1__GetParamConsd2(my_id) == false));
    
    res_AndLogicOP_70 = (res_AndLogicOP_70 && res_AndLogicOP_71);
    bool res_NotLogicOP_75 = true;
    res_NotLogicOP_75 = (res_NotLogicOP_75 && ! (Counter_GetValore(L_P1__GetLdv_m8(my_id)) == 121u));
    res_AndLogicOP_70 = (res_AndLogicOP_70 && res_NotLogicOP_75);
    
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_AndLogicOP_70);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_OrLogicOP_5);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *49,50,51,52,*  *,*  la variabile LDV_MainClass_C1_variabile_V9 non sia  diverso da c270xx
    //   *104,* o  che   l'argomento argomento_ave10 sia  diverso da avvio *,* 
    //   *104,* e  che  *,*  il timer LDV_MainClass_C1_timer_T3 sia disattivo
    //   *104,* o  che  *,*  il contatore LDV_MainClass_C1_contatore_Co6 sia  diverso da  *56,* 11
    //   *104,* o  che  *38,*  il contatore LDV_MainClass_C1_contatore_Co6 non sia  diverso da  *56,* contatore LDV_MainClass_C1_contatore_Co7
    bool res_OrLogicOP_76 = false;
    bool res_OrLogicOP_77 = false;
    bool res_OrLogicOP_78 = false;
    bool res_NotLogicOP_79 = true;
    bool res_NotLogicOP_80 = true;
    res_NotLogicOP_80 = (res_NotLogicOP_80 && ! (L_P1__GetLdv_m5(my_id) == c270xx));
    res_NotLogicOP_79 = (res_NotLogicOP_79 && ! res_NotLogicOP_80);
    res_OrLogicOP_78 = (res_OrLogicOP_78 || res_NotLogicOP_79);
    bool res_AndLogicOP_81 = true;
    bool res_NotLogicOP_82 = true;
    res_NotLogicOP_82 = (res_NotLogicOP_82 && ! (argom52 == avvio));
    res_AndLogicOP_81 = (res_AndLogicOP_81 && res_NotLogicOP_82);
    res_AndLogicOP_81 = (res_AndLogicOP_81 && Timer_Disattivo(L_P1__GetLdv_m6(my_id)));
    
    res_OrLogicOP_78 = (res_OrLogicOP_78 || res_AndLogicOP_81);
    
    res_OrLogicOP_77 = (res_OrLogicOP_77 || res_OrLogicOP_78);
    bool res_NotLogicOP_83 = true;
    res_NotLogicOP_83 = (res_NotLogicOP_83 && ! (Counter_GetValore(L_P1__GetLdv_m9(my_id)) == 11u));
    res_OrLogicOP_77 = (res_OrLogicOP_77 || res_NotLogicOP_83);
    
    res_OrLogicOP_76 = (res_OrLogicOP_76 || res_OrLogicOP_77);
    bool res_NotLogicOP_84 = true;
    bool res_NotLogicOP_85 = true;
    res_NotLogicOP_85 = (res_NotLogicOP_85 && ! (Counter_GetValore(L_P1__GetLdv_m9(my_id)) == Counter_GetValore(L_P1__GetLdv_m10(my_id))));
    res_NotLogicOP_84 = (res_NotLogicOP_84 && ! res_NotLogicOP_85);
    res_OrLogicOP_76 = (res_OrLogicOP_76 || res_NotLogicOP_84);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_76);
    
    
    
    
    return res_AndLogicOP_0;
}


// Macro valorizzate

/*
    CNL corrispondente:
    
    { commento: {[}
     commento: {46,} assegna alla macro il valore  False  commento: {],}
    }
*/
bool L_P1__Macro22(instance_id_t const my_id , bool argom34, C3_Enumerat1 argom35, C3_Enumerat4 argom36, C3_Enumerat1 argom37)
{
return false;
}

/*
    CNL corrispondente:
    
    { commento: {[}
     commento: {46,} assegna alla macro il valore  False  commento: {],}
    }
*/
bool L_P1__Macro23(instance_id_t const my_id , bool argom38, C3_Enumerat4 argom39)
{
return false;
}



