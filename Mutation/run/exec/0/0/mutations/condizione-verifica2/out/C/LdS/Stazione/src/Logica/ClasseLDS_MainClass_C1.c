#include "Logica/ClasseLDS_MainClass_C1.h"
#include "Logica/ClasseLDS_SubClass_C2.h"
#include "Logica/ClasseLDS_MainClass_C1_priv.h"
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

static bool L_P1_C1_SetExpectedCmdsResponse(instance_id_t const my_id, C1_Stateenu state)
{        
    bool isCommandPresent = false;

    // for each manual command of L_P1_C1
    if (L_P1__GetInEvent(my_id)) {
        #define IS_STATE_ACCEPTING_Event false // no state is accepting this command!
        L_P1__SetOutEvent4(my_id, IS_STATE_ACCEPTING_Event ? LDS_MANCMD_BLOCKED : LDS_MANCMD_UNEXPECTED);
        isCommandPresent |= true;		
    } else {
        L_P1__SetOutEvent4(my_id, LDS_MANCMD_NOOP);
    }
    if (L_P1__GetInEvent1(my_id)) {
        #define IS_STATE_ACCEPTING_Event1 false // no state is accepting this command!
        L_P1__SetOutEvent5(my_id, IS_STATE_ACCEPTING_Event1 ? LDS_MANCMD_BLOCKED : LDS_MANCMD_UNEXPECTED);
        isCommandPresent |= true;		
    } else {
        L_P1__SetOutEvent5(my_id, LDS_MANCMD_NOOP);
    }
    if (L_P1__GetInEvent3(my_id)) {
        #define IS_STATE_ACCEPTING_Event3 false // no state is accepting this command!
        L_P1__SetOutEvent6(my_id, IS_STATE_ACCEPTING_Event3 ? LDS_MANCMD_BLOCKED : LDS_MANCMD_UNEXPECTED);
        isCommandPresent |= true;		
    } else {
        L_P1__SetOutEvent6(my_id, LDS_MANCMD_NOOP);
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
    Azzera il contatore LDS_MainClass_C1_contatore_Co5
    }
*/
static inline void L_P1__Effec1(instance_id_t const my_id)
{
    
    //  Azzera il contatore LDS_MainClass_C1_contatore_Co5
    Counter_Res(L_P1__GetLds_m16(my_id));
}



// ********** Definizione metodi **********

// Metodi standard

void L_P1_C1_Init(instance_id_t const my_id)
{
    // init variabili di stato
    L_P1__SetLds_m10(my_id, rosso);
    L_P1__SetLds_m11(my_id, giallox);
    L_P1__SetStato1(my_id, 0);
    // init Timer e Counter
    Timer_AggmInit(L_P1__GetLds_m12(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__lds_m12_ID);
    Timer_Init(L_P1__GetLds_m12(my_id), 3000);
    Timer_AggmInit(L_P1__GetLds_m13(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__lds_m13_ID);
    Timer_Init(L_P1__GetLds_m13(my_id), 3152000);
    Timer_AggmInit(L_P1__GetLds_m14(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__lds_m14_ID);
    Timer_Init(L_P1__GetLds_m14(my_id), 1000);
    Timer_AggmInit(L_P1__GetLds_m15(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__lds_m15_ID);
    Timer_Init(L_P1__GetLds_m15(my_id), 1430000);
    Counter_AggmInit(L_P1__GetLds_m16(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__lds_m16_ID);
    Counter_Init(L_P1__GetLds_m16(my_id));
    Counter_AggmInit(L_P1__GetLds_m17(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__lds_m17_ID);
    Counter_Init(L_P1__GetLds_m17(my_id));
    Counter_AggmInit(L_P1__GetLds_m18(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__lds_m18_ID);
    Counter_Init(L_P1__GetLds_m18(my_id));
    Counter_AggmInit(L_P1__GetLds_m19(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__lds_m19_ID);
    Counter_Init(L_P1__GetLds_m19(my_id));
    // init response
    L_P1_C1_SetResponse(my_id, LDS_SCHED_NOP);

    // transizione iniziale
    if(L_P1__Guard(my_id)) {
        L_P1_C1_SetState(my_id, C1_St_state);
	L_P1__Effec(my_id);
    } else {
        STOP_EXECUTION(LOGIC_ERROR);
    }
}

void L_P1_C1_Exec(instance_id_t const my_id, Phase const p)
{
    L_P1_C1_SetResponse(my_id, LDS_SCHED_NOP);
    switch (p) {

    case LDS_PHASE_MANUAL:

        if (true == L_P1_C1_SetExpectedCmdsResponse(my_id, L_P1_C1_GetState(my_id))) {

            switch (L_P1_C1_GetState(my_id)) {

	        case C1_St_state:
	                { } // fine transizioni da state nella fase LDS_PHASE_MANUAL
	            break;
	
	        default:
	            STOP_EXECUTION(LOGIC_ERROR);
	            break;  // Needed for MISRA C syntactic compliance
	        } // switch sugli stati chiuso
        }
        break;
 

    case LDS_PHASE_STATE:

        switch (L_P1_C1_GetState(my_id)) {

        case C1_St_state:
            if (L_P1__Guard1(my_id)) {
                L_P1_C1_SetState(my_id, C1_St_state);
                L_P1__Effec1(my_id);				
                L_P1_C1_SetResponse(my_id, LDS_SCHED_WAIT);
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
    Timer_Exec(L_P1__GetLds_m12(my_id));
    Timer_Exec(L_P1__GetLds_m13(my_id));
    Timer_Exec(L_P1__GetLds_m14(my_id));
    Timer_Exec(L_P1__GetLds_m15(my_id));
}

void L_P1_C1_GSetSafe(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C1(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C1(proc_id);
    L_P1__SetOutLds_m(my_id, true);
    L_P1__SetOutLds_m1(my_id, gialloxverd);
    L_P1__SetOutLds_m2(my_id, true);
}


// ********** Definizione macro **********

// Macro di effetto

/*
    CNL corrispondente:
    
    {  se il parametro ConsDef  è  uguale a FALSE  commento: {37,} e  se la variabile LDS_MainClass_C1_variabile_V1 non è  diverso da c120 commento: {38,} e  se il contatore LDS_MainClass_C1_contatore_Co9 è  uguale a  commento: {53,} 145,  commento: {67,} Assegna alla variabile LDS_MainClass_C1_variabile_V7 il valore RossoVerde commento: {67,}
    
     ,altrimenti  commento: {72,}Azzera il contatore LDS_MainClass_C1_contatore_Co5
    
    
      se la macro  LDS_MainClass_C1_macrova_M10 ( con argomento_a10   uguale a True  e argomento_a9   uguale a Verde )   è  diverso da avanzamento commento: {40,}  commento: {38,} o  se il contatore LDS_MainClass_C1_contatore_Co8 non è  minore di  commento: {55,} contatore LDS_MainClass_C1_contatore_Co6 commento: {38,} e  se il contatore LDS_MainClass_C1_contatore_Co8 non è  diverso da  commento: {56,} contatore LDS_MainClass_C1_contatore_Co8 o  se il parametro ConsDef  è  uguale a FALSE ,  commento: {67,} Assegna alla variabile LDS_MainClass_C1_variabile_V1 il valore c120 commento: {67,}
    
     ,altrimenti  commento: {66,} Assegna al comando LDS_MainClass_C1_comando_C5 il valore GialloxVerdex
    
    
     commento: {38,}  se il contatore LDS_MainClass_C1_contatore_Co9 è  diverso da  commento: {56,} contatore LDS_MainClass_C1_contatore_Co6 o  se il parametro ConsDef  è  uguale a FALSE  e  se il parametro ConsDef è uguale a FALSE ,  commento: {67,} Assegna alla variabile LDS_MainClass_C1_variabile_V7 il valore RossoVerde commento: {67,}
    
     ,altrimenti  commento: {69,}Disattiva il timer LDS_MainClass_C1_timer_T8 
    
     commento: {34,}  se il parametro LDS_MainClass_C1_parametro_P5 è  uguale a  True  commento: {38,} e  se il contatore LDS_MainClass_C1_contatore_Co9 è  uguale a  commento: {53,} 13430 commento: {37,} o  se la variabile LDS_MainClass_C1_variabile_V7 non è  diverso da RossoVerde e  se il parametro ConsDef è uguale a FALSE  e  se il parametro ConsDef è uguale a FALSE  o  se il parametro ConsDef  è  uguale a FALSE , commento: {68,}Attiva il timer LDS_MainClass_C1_timer_T3
    
     ,altrimenti  commento: {66,} Assegna al comando LDS_MainClass_C1_comando_C4 il valore  False 
    
    
      se il parametro ConsDef è uguale a FALSE  commento: {37,} e  se la variabile LDS_MainClass_C1_variabile_V1 è  uguale a variabile LDS_MainClass_C1_variabile_V1, commento: {68,}Attiva il timer LDS_MainClass_C1_timer_T3
    
     ,altrimenti  commento: {68,}Attiva il timer LDS_MainClass_C1_timer_T3
    
    
    
    }
*/
void L_P1__Macro(instance_id_t const my_id )
{
//  se il parametro ConsDef  è  uguale a FALSE  *37,* e  se la variabile LDS_MainClass_C1_variabile_V1 non è  diverso da c120 *38,* e  se il contatore LDS_MainClass_C1_contatore_Co9 è  uguale a  *53,* 145,  *67,* Assegna alla variabile LDS_MainClass_C1_variabile_V7 il valore RossoVerde *67,*
    // ,altrimenti  *72,*Azzera il contatore LDS_MainClass_C1_contatore_Co5
    bool res_AndLogicOP_0 = true;
    bool res_AndLogicOP_1 = true;
    res_AndLogicOP_1 = (res_AndLogicOP_1 && (L_P1__GetParamConsd(my_id) == false));
    bool res_NotLogicOP_2 = true;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__GetLds_m10(my_id) == c120));
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! res_NotLogicOP_3);
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_2);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_AndLogicOP_1);
    res_AndLogicOP_0 = (res_AndLogicOP_0 && (Counter_GetValore(L_P1__GetLds_m19(my_id)) == 145u));
    
    if(res_AndLogicOP_0){
    
    L_P1__SetLds_m11(my_id,rossoverde);
    }else{
    
    Counter_Res(L_P1__GetLds_m16(my_id));
    }
    //  se la macro  LDS_MainClass_C1_macrova_M10 ( con argomento_a10   uguale a True  e argomento_a9   uguale a Verde )   è  diverso da avanzamento *40,*  *38,* o  se il contatore LDS_MainClass_C1_contatore_Co8 non è  minore di  *55,* contatore LDS_MainClass_C1_contatore_Co6 *38,* e  se il contatore LDS_MainClass_C1_contatore_Co8 non è  diverso da  *56,* contatore LDS_MainClass_C1_contatore_Co8 o  se il parametro ConsDef  è  uguale a FALSE ,  *67,* Assegna alla variabile LDS_MainClass_C1_variabile_V1 il valore c120 *67,*
    // ,altrimenti  *66,* Assegna al comando LDS_MainClass_C1_comando_C5 il valore GialloxVerdex
    bool res_OrLogicOP_4 = false;
    bool res_OrLogicOP_5 = false;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__Macro1(my_id,true,verde) == avanzamento));
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_NotLogicOP_6);
    bool res_AndLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (Counter_GetValore(L_P1__GetLds_m18(my_id)) < Counter_GetValore(L_P1__GetLds_m17(my_id))));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_8);
    bool res_NotLogicOP_9 = true;
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (Counter_GetValore(L_P1__GetLds_m18(my_id)) == Counter_GetValore(L_P1__GetLds_m18(my_id))));
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! res_NotLogicOP_10);
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_9);
    
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_AndLogicOP_7);
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_OrLogicOP_5);
    res_OrLogicOP_4 = (res_OrLogicOP_4 || (L_P1__GetParamConsd(my_id) == false));
    
    if(res_OrLogicOP_4){
    
    L_P1__SetLds_m10(my_id,c120);
    }else{
    
    L_P1__SetOutLds_m1(my_id,gialloxverd);
    }
    //  *38,*  se il contatore LDS_MainClass_C1_contatore_Co9 è  diverso da  *56,* contatore LDS_MainClass_C1_contatore_Co6 o  se il parametro ConsDef  è  uguale a FALSE  e  se il parametro ConsDef è uguale a FALSE ,  *67,* Assegna alla variabile LDS_MainClass_C1_variabile_V7 il valore RossoVerde *67,*
    // ,altrimenti  *69,*Disattiva il timer LDS_MainClass_C1_timer_T8
    bool res_OrLogicOP_11 = false;
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (Counter_GetValore(L_P1__GetLds_m19(my_id)) == Counter_GetValore(L_P1__GetLds_m17(my_id))));
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_NotLogicOP_12);
    bool res_AndLogicOP_13 = true;
    res_AndLogicOP_13 = (res_AndLogicOP_13 && (L_P1__GetParamConsd(my_id) == false));
    res_AndLogicOP_13 = (res_AndLogicOP_13 && (L_P1__GetParamConsd(my_id) == false));
    
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_AndLogicOP_13);
    
    if(res_OrLogicOP_11){
    
    L_P1__SetLds_m11(my_id,rossoverde);
    }else{
    
    Timer_Disattiva(L_P1__GetLds_m15(my_id));
    }
    //  *34,*  se il parametro LDS_MainClass_C1_parametro_P5 è  uguale a  True  *38,* e  se il contatore LDS_MainClass_C1_contatore_Co9 è  uguale a  *53,* 13430 *37,* o  se la variabile LDS_MainClass_C1_variabile_V7 non è  diverso da RossoVerde e  se il parametro ConsDef è uguale a FALSE  e  se il parametro ConsDef è uguale a FALSE  o  se il parametro ConsDef  è  uguale a FALSE , *68,*Attiva il timer LDS_MainClass_C1_timer_T3
    // ,altrimenti  *66,* Assegna al comando LDS_MainClass_C1_comando_C4 il valore  False
    bool res_OrLogicOP_14 = false;
    bool res_OrLogicOP_15 = false;
    bool res_AndLogicOP_16 = true;
    res_AndLogicOP_16 = (res_AndLogicOP_16 && (L_P1__GetParamLds_m9(my_id) == true));
    res_AndLogicOP_16 = (res_AndLogicOP_16 && (Counter_GetValore(L_P1__GetLds_m19(my_id)) == 13430u));
    
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_AndLogicOP_16);
    bool res_AndLogicOP_17 = true;
    bool res_AndLogicOP_18 = true;
    bool res_NotLogicOP_19 = true;
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! (L_P1__GetLds_m11(my_id) == rossoverde));
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! res_NotLogicOP_20);
    res_AndLogicOP_18 = (res_AndLogicOP_18 && res_NotLogicOP_19);
    res_AndLogicOP_18 = (res_AndLogicOP_18 && (L_P1__GetParamConsd(my_id) == false));
    
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_AndLogicOP_18);
    res_AndLogicOP_17 = (res_AndLogicOP_17 && (L_P1__GetParamConsd(my_id) == false));
    
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_AndLogicOP_17);
    
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_OrLogicOP_15);
    res_OrLogicOP_14 = (res_OrLogicOP_14 || (L_P1__GetParamConsd(my_id) == false));
    
    if(res_OrLogicOP_14){
    
    Timer_Attiva(L_P1__GetLds_m14(my_id));
    }else{
    
    L_P1__SetOutLds_m(my_id,false);
    }
    //  se il parametro ConsDef è uguale a FALSE  *37,* e  se la variabile LDS_MainClass_C1_variabile_V1 è  uguale a variabile LDS_MainClass_C1_variabile_V1, *68,*Attiva il timer LDS_MainClass_C1_timer_T3
    // ,altrimenti  *68,*Attiva il timer LDS_MainClass_C1_timer_T3
    bool res_AndLogicOP_21 = true;
    res_AndLogicOP_21 = (res_AndLogicOP_21 && (L_P1__GetParamConsd(my_id) == false));
    res_AndLogicOP_21 = (res_AndLogicOP_21 && (L_P1__GetLds_m10(my_id) == L_P1__GetLds_m10(my_id)));
    
    if(res_AndLogicOP_21){
    
    Timer_Attiva(L_P1__GetLds_m14(my_id));
    }else{
    
    Timer_Attiva(L_P1__GetLds_m14(my_id));
    }
}


// Macro di verifica

/*
    CNL corrispondente:
     
    { commento: {62,}  se la macro  LDS_MainClass_C1_macrova_M10 ( con argomento_a10   uguale a True  e argomento_a9   uguale a GialloxVerdex )   è  uguale a avanzamento commento: {40,}  commento: {36,} e  se il timer LDS_MainClass_C1_timer_T3 è disattivo commento: {36,} e  se il timer LDS_MainClass_C1_timer_T8 non è attivo, Almeno una delle seguenti { 
     commento: {62,} commento: {34,}  se il parametro LDS_MainClass_C1_parametro_P5 è  uguale a  True , Almeno una delle seguenti { 
      se la macro  LDS_MainClass_C1_macrova_M10 ( con argomento_a10   uguale a True  e argomento_a9   uguale a GialloxVerdex )   è  uguale a avanzamento commento: {40,} , Verifica che   commento: {47,50,51,}  commento: {34,}  il parametro LDS_MainClass_C1_parametro_P3 non sia  uguale a  False 
     commento: {104,} e  che  commento: {,}  la variabile LDS_MainClass_C1_variabile_V1 sia  uguale a c120
     commento: {104,} o  che  commento: {,}  il contatore LDS_MainClass_C1_contatore_Co9 sia  minore di  commento: {55,} contatore LDS_MainClass_C1_contatore_Co6
     commento: {104,} o  che   il parametro ConsDef  sia  uguale a FALSE 
    
    
     } Verifica che   commento: {50,51,}  commento: {,}  la variabile LDS_MainClass_C1_variabile_V1 sia  uguale a c120
     commento: {104,} e  che  commento: {37,}  la variabile LDS_MainClass_C1_variabile_V1 sia  diverso da c120
     commento: {104,} o  che  commento: {,}  il contatore LDS_MainClass_C1_contatore_Co9 non sia  minore di  commento: {55,} 12
     commento: {104,} e  che  commento: {38,}  il contatore LDS_MainClass_C1_contatore_Co9 sia  uguale a  commento: {53,} contatore LDS_MainClass_C1_contatore_Co8
    
    
     } Verifica che   commento: {47,50,51,}   il parametro ConsDef sia uguale a FALSE 
     commento: {104,} o  che  commento: {34,}  il parametro LDS_MainClass_C1_parametro_P2 sia  diverso da  commento: {56,} 10
     commento: {104,} e  che  commento: {,}  il contatore LDS_MainClass_C1_contatore_Co8 non sia  minore di  commento: {55,} contatore LDS_MainClass_C1_contatore_Co6
     commento: {104,} o  che  commento: {,}  la variabile LDS_MainClass_C1_variabile_V1 non sia  uguale a c120
     commento: {104,} e  che   il parametro ConsDef  sia  uguale a FALSE 
     commento: {104,} o  che  commento: {34,}  il parametro LDS_MainClass_C1_parametro_P3 sia  uguale a  True 
     o che il controllo LDS_MainClass_C1_controllo_C9 non sia  diverso da  True  
    
    }
*/
bool L_P1__Macro2(instance_id_t const my_id )
{
bool res_AndLogicOP_0 = true;
    
    //  *62,*  se la macro  LDS_MainClass_C1_macrova_M10 ( con argomento_a10   uguale a True  e argomento_a9   uguale a GialloxVerdex )   è  uguale a avanzamento *40,*  *36,* e  se il timer LDS_MainClass_C1_timer_T3 è disattivo *36,* e  se il timer LDS_MainClass_C1_timer_T8 non è attivo, Almeno una delle seguenti { 
    //   *62,* *34,*  se il parametro LDS_MainClass_C1_parametro_P5 è  uguale a  True , Almeno una delle seguenti { 
    //    se la macro  LDS_MainClass_C1_macrova_M10 ( con argomento_a10   uguale a True  e argomento_a9   uguale a GialloxVerdex )   è  uguale a avanzamento *40,* , Verifica che   *47,50,51,*  *34,*  il parametro LDS_MainClass_C1_parametro_P3 non sia  uguale a  False 
    //   *104,* e  che  *,*  la variabile LDS_MainClass_C1_variabile_V1 sia  uguale a c120
    //   *104,* o  che  *,*  il contatore LDS_MainClass_C1_contatore_Co9 sia  minore di  *55,* contatore LDS_MainClass_C1_contatore_Co6
    //   *104,* o  che   il parametro ConsDef  sia  uguale a FALSE 
    //   } Verifica che   *50,51,*  *,*  la variabile LDS_MainClass_C1_variabile_V1 sia  uguale a c120
    //   *104,* e  che  *37,*  la variabile LDS_MainClass_C1_variabile_V1 sia  diverso da c120
    //   *104,* o  che  *,*  il contatore LDS_MainClass_C1_contatore_Co9 non sia  minore di  *55,* 12
    //   *104,* e  che  *38,*  il contatore LDS_MainClass_C1_contatore_Co9 sia  uguale a  *53,* contatore LDS_MainClass_C1_contatore_Co8
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_AndLogicOP_2 = true;
    bool res_AndLogicOP_3 = true;
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (L_P1__Macro1(my_id,true,gialloxverd) == avanzamento));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && Timer_Disattivo(L_P1__GetLds_m14(my_id)));
    
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_AndLogicOP_3);
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! Timer_Attivo(L_P1__GetLds_m15(my_id)));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_4);
    
    if(res_AndLogicOP_2){
    bool res_OrLogicOP_5 = false;
    bool res_ImpliesLogicOp_6 = true;
    if((L_P1__GetParamLds_m9(my_id) == true)){
    bool res_ImpliesLogicOp_7 = true;
    if((L_P1__Macro1(my_id,true,gialloxverd) == avanzamento)){
    bool res_OrLogicOP_8 = false;
    bool res_OrLogicOP_9 = false;
    bool res_AndLogicOP_10 = true;
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (L_P1__GetParamLds_m8(my_id) == false));
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_NotLogicOP_11);
    res_AndLogicOP_10 = (res_AndLogicOP_10 && (L_P1__GetLds_m10(my_id) == c120));
    
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_AndLogicOP_10);
    res_OrLogicOP_9 = (res_OrLogicOP_9 || (Counter_GetValore(L_P1__GetLds_m19(my_id)) < Counter_GetValore(L_P1__GetLds_m17(my_id))));
    
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_OrLogicOP_9);
    res_OrLogicOP_8 = (res_OrLogicOP_8 || (L_P1__GetParamConsd(my_id) == false));
    
    res_ImpliesLogicOp_7 = (res_ImpliesLogicOp_7 && res_OrLogicOP_8);
    }
    res_ImpliesLogicOp_6 = (res_ImpliesLogicOp_6 && res_ImpliesLogicOp_7);
    }
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_ImpliesLogicOp_6);
    bool res_OrLogicOP_12 = false;
    bool res_AndLogicOP_13 = true;
    res_AndLogicOP_13 = (res_AndLogicOP_13 && (L_P1__GetLds_m10(my_id) == c120));
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1__GetLds_m10(my_id) == c120));
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_NotLogicOP_14);
    
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_AndLogicOP_13);
    bool res_AndLogicOP_15 = true;
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (Counter_GetValore(L_P1__GetLds_m19(my_id)) < 12u));
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_NotLogicOP_16);
    res_AndLogicOP_15 = (res_AndLogicOP_15 && (Counter_GetValore(L_P1__GetLds_m19(my_id)) == Counter_GetValore(L_P1__GetLds_m18(my_id))));
    
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_AndLogicOP_15);
    
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_OrLogicOP_12);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_OrLogicOP_5);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *47,50,51,*   il parametro ConsDef sia uguale a FALSE 
    //   *104,* o  che  *34,*  il parametro LDS_MainClass_C1_parametro_P2 sia  diverso da  *56,* 10
    //   *104,* e  che  *,*  il contatore LDS_MainClass_C1_contatore_Co8 non sia  minore di  *55,* contatore LDS_MainClass_C1_contatore_Co6
    //   *104,* o  che  *,*  la variabile LDS_MainClass_C1_variabile_V1 non sia  uguale a c120
    //   *104,* e  che   il parametro ConsDef  sia  uguale a FALSE 
    //   *104,* o  che  *34,*  il parametro LDS_MainClass_C1_parametro_P3 sia  uguale a  True 
    //   o che il controllo LDS_MainClass_C1_controllo_C9 non sia  diverso da  True
    bool res_OrLogicOP_17 = false;
    bool res_OrLogicOP_18 = false;
    bool res_OrLogicOP_19 = false;
    bool res_OrLogicOP_20 = false;
    res_OrLogicOP_20 = (res_OrLogicOP_20 || (L_P1__GetParamConsd(my_id) == false));
    bool res_AndLogicOP_21 = true;
    bool res_NotLogicOP_22 = true;
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! (L_P1__GetParamLds_m7(my_id) == 10u));
    res_AndLogicOP_21 = (res_AndLogicOP_21 && res_NotLogicOP_22);
    bool res_NotLogicOP_23 = true;
    res_NotLogicOP_23 = (res_NotLogicOP_23 && ! (Counter_GetValore(L_P1__GetLds_m18(my_id)) < Counter_GetValore(L_P1__GetLds_m17(my_id))));
    res_AndLogicOP_21 = (res_AndLogicOP_21 && res_NotLogicOP_23);
    
    res_OrLogicOP_20 = (res_OrLogicOP_20 || res_AndLogicOP_21);
    
    res_OrLogicOP_19 = (res_OrLogicOP_19 || res_OrLogicOP_20);
    bool res_AndLogicOP_24 = true;
    bool res_NotLogicOP_25 = true;
    res_NotLogicOP_25 = (res_NotLogicOP_25 && ! (L_P1__GetLds_m10(my_id) == c120));
    res_AndLogicOP_24 = (res_AndLogicOP_24 && res_NotLogicOP_25);
    res_AndLogicOP_24 = (res_AndLogicOP_24 && (L_P1__GetParamConsd(my_id) == false));
    
    res_OrLogicOP_19 = (res_OrLogicOP_19 || res_AndLogicOP_24);
    
    res_OrLogicOP_18 = (res_OrLogicOP_18 || res_OrLogicOP_19);
    res_OrLogicOP_18 = (res_OrLogicOP_18 || (L_P1__GetParamLds_m8(my_id) == true));
    
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_OrLogicOP_18);
    bool res_NotLogicOP_26 = true;
    bool res_NotLogicOP_27 = true;
    res_NotLogicOP_27 = (res_NotLogicOP_27 && ! (L_P1__GetInLds_m6(my_id) == true));
    res_NotLogicOP_26 = (res_NotLogicOP_26 && ! res_NotLogicOP_27);
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_NotLogicOP_26);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_17);
    
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
    
    { 
    
    commento: {38,}  se il contatore LDS_MainClass_C1_contatore_Co9 non è  diverso da  commento: {56,} 11430 commento: {36,} e  se il timer LDS_MainClass_C1_timer_T8 non è disattivo e  se l'argomento argomento_ave7 è  uguale a  False  commento: {39,}  commento: {34,} o  se il parametro LDS_MainClass_C1_parametro_P5 è  diverso da  True , Verifica che   commento: {50,}  commento: {,}  la variabile LDS_MainClass_C1_variabile_V1 sia  uguale a c120
    
    
    }
*/
bool L_P1__Macro3(instance_id_t const my_id , bool argom2, C1_Enumerat4 argom3, C1_Enumerat1 argom4, bool argom5, C1_Enumerat4 argom6, C1_Enumerat2 argom7)
{
bool res_AndLogicOP_0 = true;
    
    //  *38,*  se il contatore LDS_MainClass_C1_contatore_Co9 non è  diverso da  *56,* 11430 *36,* e  se il timer LDS_MainClass_C1_timer_T8 non è disattivo e  se l'argomento argomento_ave7 è  uguale a  False  *39,*  *34,* o  se il parametro LDS_MainClass_C1_parametro_P5 è  diverso da  True , Verifica che   *50,*  *,*  la variabile LDS_MainClass_C1_variabile_V1 sia  uguale a c120
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_AndLogicOP_3 = true;
    bool res_AndLogicOP_4 = true;
    bool res_NotLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (Counter_GetValore(L_P1__GetLds_m19(my_id)) == 11430u));
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! res_NotLogicOP_6);
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_5);
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! Timer_Disattivo(L_P1__GetLds_m15(my_id)));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_7);
    
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_AndLogicOP_4);
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (argom5 == false));
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_3);
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetParamLds_m9(my_id) == true));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_8);
    
    if(res_OrLogicOP_2){
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && (L_P1__GetLds_m10(my_id) == c120));
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
     
    { commento: {62,}  se il parametro ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
     commento: {63,} commento: {36,}  se il timer LDS_MainClass_C1_timer_T3 non è attivo commento: {38,} o  se il contatore LDS_MainClass_C1_contatore_Co9 è  minore di  commento: {55,} contatore LDS_MainClass_C1_contatore_Co6 commento: {36,} e  se il timer LDS_MainClass_C1_timer_T8 non è scaduto o  se il parametro ConsDef è uguale a FALSE  e  se il parametro ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
     commento: {61,}  se il parametro ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro LDS_MainClass_C1_parametro_P5 non è  diverso da  True  e  se il parametro ConsDef  è  uguale a FALSE , Tutte le seguenti { 
     commento: {34,}  se il parametro LDS_MainClass_C1_parametro_P5 non è  diverso da  False  commento: {36,} o  se il timer LDS_MainClass_C1_timer_T2 non è scaduto o  se il parametro ConsDef è uguale a FALSE  commento: {34,} e  se il parametro LDS_MainClass_C1_parametro_P5 non è  diverso da  False , Verifica che   commento: {47,}   il parametro ConsDef sia uguale a FALSE 
     commento: {104,} e  che   il parametro ConsDef sia uguale a FALSE 
     commento: {104,} o  che   il parametro ConsDef sia uguale a FALSE 
     commento: {104,} e  che  commento: {34,}  il parametro LDS_MainClass_C1_parametro_P2 sia  uguale a  commento: {53,} 7
    
    
     } Verifica che   commento: {47,50,}  commento: {,}  la variabile LDS_MainClass_C1_variabile_V1 non sia  diverso da c120
     commento: {104,} e  che   il parametro ConsDef sia uguale a FALSE 
     commento: {104,} e  che   il parametro ConsDef sia uguale a FALSE 
     commento: {104,} e  che  commento: {37,}  la variabile LDS_MainClass_C1_variabile_V1 non sia  diverso da variabile LDS_MainClass_C1_variabile_V1
    
    
     } Verifica che   commento: {47,}  commento: {34,}  il parametro LDS_MainClass_C1_parametro_P5 sia  uguale a  True 
    
    
     } Verifica che   commento: {47,49,50,}   il parametro ConsDef  sia  uguale a FALSE 
     commento: {104,} e  che  commento: {,}  la variabile LDS_MainClass_C1_variabile_V1 sia  uguale a c120
     commento: {104,} e  che  commento: {,}  il timer LDS_MainClass_C1_timer_T3 sia disattivo
    
    
    }
*/
bool L_P1__Macro4(instance_id_t const my_id )
{
bool res_AndLogicOP_0 = true;
    
    //  *62,*  se il parametro ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
    //   *63,* *36,*  se il timer LDS_MainClass_C1_timer_T3 non è attivo *38,* o  se il contatore LDS_MainClass_C1_contatore_Co9 è  minore di  *55,* contatore LDS_MainClass_C1_contatore_Co6 *36,* e  se il timer LDS_MainClass_C1_timer_T8 non è scaduto o  se il parametro ConsDef è uguale a FALSE  e  se il parametro ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
    //   *61,*  se il parametro ConsDef  è  uguale a FALSE  *34,* e  se il parametro LDS_MainClass_C1_parametro_P5 non è  diverso da  True  e  se il parametro ConsDef  è  uguale a FALSE , Tutte le seguenti { 
    //   *34,*  se il parametro LDS_MainClass_C1_parametro_P5 non è  diverso da  False  *36,* o  se il timer LDS_MainClass_C1_timer_T2 non è scaduto o  se il parametro ConsDef è uguale a FALSE  *34,* e  se il parametro LDS_MainClass_C1_parametro_P5 non è  diverso da  False , Verifica che   *47,*   il parametro ConsDef sia uguale a FALSE 
    //   *104,* e  che   il parametro ConsDef sia uguale a FALSE 
    //   *104,* o  che   il parametro ConsDef sia uguale a FALSE 
    //   *104,* e  che  *34,*  il parametro LDS_MainClass_C1_parametro_P2 sia  uguale a  *53,* 7
    //   } Verifica che   *47,50,*  *,*  la variabile LDS_MainClass_C1_variabile_V1 non sia  diverso da c120
    //   *104,* e  che   il parametro ConsDef sia uguale a FALSE 
    //   *104,* e  che   il parametro ConsDef sia uguale a FALSE 
    //   *104,* e  che  *37,*  la variabile LDS_MainClass_C1_variabile_V1 non sia  diverso da variabile LDS_MainClass_C1_variabile_V1
    //   } Verifica che   *47,*  *34,*  il parametro LDS_MainClass_C1_parametro_P5 sia  uguale a  True 
    //   }
    bool res_ImpliesLogicOp_1 = true;
    if((L_P1__GetParamConsd(my_id) == false)){
    bool res_OrLogicOP_2 = false;
    bool res_ImpliesLogicOp_3 = true;
    bool res_OrLogicOP_4 = false;
    bool res_OrLogicOP_5 = false;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! Timer_Attivo(L_P1__GetLds_m14(my_id)));
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_NotLogicOP_6);
    bool res_AndLogicOP_7 = true;
    res_AndLogicOP_7 = (res_AndLogicOP_7 && (Counter_GetValore(L_P1__GetLds_m19(my_id)) < Counter_GetValore(L_P1__GetLds_m17(my_id))));
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! Timer_Scaduto(L_P1__GetLds_m15(my_id)));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_8);
    
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_AndLogicOP_7);
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_OrLogicOP_5);
    bool res_AndLogicOP_9 = true;
    res_AndLogicOP_9 = (res_AndLogicOP_9 && (L_P1__GetParamConsd(my_id) == false));
    res_AndLogicOP_9 = (res_AndLogicOP_9 && (L_P1__GetParamConsd(my_id) == false));
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_AndLogicOP_9);
    
    if(res_OrLogicOP_4){
    bool res_XorLogicOP_10 = true;
    int xorIndex_res_XorLogicOP_10 = 0;
    bool res_ImpliesLogicOp_11 = true;
    bool res_AndLogicOP_12 = true;
    bool res_AndLogicOP_13 = true;
    res_AndLogicOP_13 = (res_AndLogicOP_13 && (L_P1__GetParamConsd(my_id) == false));
    bool res_NotLogicOP_14 = true;
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (L_P1__GetParamLds_m9(my_id) == true));
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! res_NotLogicOP_15);
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_NotLogicOP_14);
    
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_AndLogicOP_13);
    res_AndLogicOP_12 = (res_AndLogicOP_12 && (L_P1__GetParamConsd(my_id) == false));
    
    if(res_AndLogicOP_12){
    bool res_ImpliesLogicOp_16 = true;
    bool res_OrLogicOP_17 = false;
    bool res_OrLogicOP_18 = false;
    bool res_NotLogicOP_19 = true;
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! (L_P1__GetParamLds_m9(my_id) == false));
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! res_NotLogicOP_20);
    res_OrLogicOP_18 = (res_OrLogicOP_18 || res_NotLogicOP_19);
    bool res_NotLogicOP_21 = true;
    res_NotLogicOP_21 = (res_NotLogicOP_21 && ! Timer_Scaduto(L_P1__GetLds_m13(my_id)));
    res_OrLogicOP_18 = (res_OrLogicOP_18 || res_NotLogicOP_21);
    
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_OrLogicOP_18);
    bool res_AndLogicOP_22 = true;
    res_AndLogicOP_22 = (res_AndLogicOP_22 && (L_P1__GetParamConsd(my_id) == false));
    bool res_NotLogicOP_23 = true;
    bool res_NotLogicOP_24 = true;
    res_NotLogicOP_24 = (res_NotLogicOP_24 && ! (L_P1__GetParamLds_m9(my_id) == false));
    res_NotLogicOP_23 = (res_NotLogicOP_23 && ! res_NotLogicOP_24);
    res_AndLogicOP_22 = (res_AndLogicOP_22 && res_NotLogicOP_23);
    
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_AndLogicOP_22);
    
    if(res_OrLogicOP_17){
    bool res_OrLogicOP_25 = false;
    bool res_AndLogicOP_26 = true;
    res_AndLogicOP_26 = (res_AndLogicOP_26 && (L_P1__GetParamConsd(my_id) == false));
    res_AndLogicOP_26 = (res_AndLogicOP_26 && (L_P1__GetParamConsd(my_id) == false));
    
    res_OrLogicOP_25 = (res_OrLogicOP_25 || res_AndLogicOP_26);
    bool res_AndLogicOP_27 = true;
    res_AndLogicOP_27 = (res_AndLogicOP_27 && (L_P1__GetParamConsd(my_id) == false));
    res_AndLogicOP_27 = (res_AndLogicOP_27 && (L_P1__GetParamLds_m7(my_id) == 7u));
    
    res_OrLogicOP_25 = (res_OrLogicOP_25 || res_AndLogicOP_27);
    
    res_ImpliesLogicOp_16 = (res_ImpliesLogicOp_16 && res_OrLogicOP_25);
    }
    res_ImpliesLogicOp_11 = (res_ImpliesLogicOp_11 && res_ImpliesLogicOp_16);
    }
    if(res_ImpliesLogicOp_11){
    xorIndex_res_XorLogicOP_10 = (xorIndex_res_XorLogicOP_10 + 1);
    }
    bool res_AndLogicOP_28 = true;
    bool res_AndLogicOP_29 = true;
    bool res_AndLogicOP_30 = true;
    bool res_NotLogicOP_31 = true;
    bool res_NotLogicOP_32 = true;
    res_NotLogicOP_32 = (res_NotLogicOP_32 && ! (L_P1__GetLds_m10(my_id) == c120));
    res_NotLogicOP_31 = (res_NotLogicOP_31 && ! res_NotLogicOP_32);
    res_AndLogicOP_30 = (res_AndLogicOP_30 && res_NotLogicOP_31);
    res_AndLogicOP_30 = (res_AndLogicOP_30 && (L_P1__GetParamConsd(my_id) == false));
    
    res_AndLogicOP_29 = (res_AndLogicOP_29 && res_AndLogicOP_30);
    res_AndLogicOP_29 = (res_AndLogicOP_29 && (L_P1__GetParamConsd(my_id) == false));
    
    res_AndLogicOP_28 = (res_AndLogicOP_28 && res_AndLogicOP_29);
    bool res_NotLogicOP_33 = true;
    bool res_NotLogicOP_34 = true;
    res_NotLogicOP_34 = (res_NotLogicOP_34 && ! (L_P1__GetLds_m10(my_id) == L_P1__GetLds_m10(my_id)));
    res_NotLogicOP_33 = (res_NotLogicOP_33 && ! res_NotLogicOP_34);
    res_AndLogicOP_28 = (res_AndLogicOP_28 && res_NotLogicOP_33);
    
    if(res_AndLogicOP_28){
    xorIndex_res_XorLogicOP_10 = (xorIndex_res_XorLogicOP_10 + 1);
    }
    
    res_XorLogicOP_10 = (res_XorLogicOP_10 && (xorIndex_res_XorLogicOP_10 == 1));
    res_ImpliesLogicOp_3 = (res_ImpliesLogicOp_3 && res_XorLogicOP_10);
    }
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_ImpliesLogicOp_3);
    res_OrLogicOP_2 = (res_OrLogicOP_2 || (L_P1__GetParamLds_m9(my_id) == true));
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_OrLogicOP_2);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *47,49,50,*   il parametro ConsDef  sia  uguale a FALSE 
    //   *104,* e  che  *,*  la variabile LDS_MainClass_C1_variabile_V1 sia  uguale a c120
    //   *104,* e  che  *,*  il timer LDS_MainClass_C1_timer_T3 sia disattivo
    bool res_AndLogicOP_35 = true;
    bool res_AndLogicOP_36 = true;
    res_AndLogicOP_36 = (res_AndLogicOP_36 && (L_P1__GetParamConsd(my_id) == false));
    res_AndLogicOP_36 = (res_AndLogicOP_36 && (L_P1__GetLds_m10(my_id) == c120));
    
    res_AndLogicOP_35 = (res_AndLogicOP_35 && res_AndLogicOP_36);
    res_AndLogicOP_35 = (res_AndLogicOP_35 && Timer_Disattivo(L_P1__GetLds_m14(my_id)));
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_AndLogicOP_35);
    
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
     
    { commento: {62,} commento: {38,}  se il contatore LDS_MainClass_C1_contatore_Co6 è  minore di  commento: {55,} contatore LDS_MainClass_C1_contatore_Co6 e  se il parametro ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
      se il parametro ConsDef è uguale a FALSE  commento: {38,} o  se il contatore LDS_MainClass_C1_contatore_Co9 non è  uguale a  commento: {53,} 14, Verifica che   commento: {47,49,}  commento: {,}  il timer LDS_MainClass_C1_timer_T3 non sia attivo
     commento: {104,} e  che   il parametro ConsDef  sia  uguale a FALSE 
     commento: {104,} o  che  commento: {36,}  il timer LDS_MainClass_C1_timer_T1 sia attivo
     commento: {104,} o  che  commento: {34,}  il parametro LDS_MainClass_C1_parametro_P5 non sia  diverso da  True 
     commento: {104,} e  che  commento: {34,}  il parametro LDS_MainClass_C1_parametro_P3 sia  diverso da  True 
    
    
     } Verifica che   commento: {49,}  commento: {,}  il timer LDS_MainClass_C1_timer_T2 sia attivo
    
    
    }
*/
bool L_P1__Macro5(instance_id_t const my_id )
{
bool res_AndLogicOP_0 = true;
    
    //  *62,* *38,*  se il contatore LDS_MainClass_C1_contatore_Co6 è  minore di  *55,* contatore LDS_MainClass_C1_contatore_Co6 e  se il parametro ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
    //    se il parametro ConsDef è uguale a FALSE  *38,* o  se il contatore LDS_MainClass_C1_contatore_Co9 non è  uguale a  *53,* 14, Verifica che   *47,49,*  *,*  il timer LDS_MainClass_C1_timer_T3 non sia attivo
    //   *104,* e  che   il parametro ConsDef  sia  uguale a FALSE 
    //   *104,* o  che  *36,*  il timer LDS_MainClass_C1_timer_T1 sia attivo
    //   *104,* o  che  *34,*  il parametro LDS_MainClass_C1_parametro_P5 non sia  diverso da  True 
    //   *104,* e  che  *34,*  il parametro LDS_MainClass_C1_parametro_P3 sia  diverso da  True 
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_AndLogicOP_2 = true;
    res_AndLogicOP_2 = (res_AndLogicOP_2 && (Counter_GetValore(L_P1__GetLds_m17(my_id)) < Counter_GetValore(L_P1__GetLds_m17(my_id))));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && (L_P1__GetParamConsd(my_id) == false));
    
    if(res_AndLogicOP_2){
    bool res_ImpliesLogicOp_3 = true;
    bool res_OrLogicOP_4 = false;
    res_OrLogicOP_4 = (res_OrLogicOP_4 || (L_P1__GetParamConsd(my_id) == false));
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (Counter_GetValore(L_P1__GetLds_m19(my_id)) == 14u));
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_NotLogicOP_5);
    
    if(res_OrLogicOP_4){
    bool res_OrLogicOP_6 = false;
    bool res_OrLogicOP_7 = false;
    bool res_AndLogicOP_8 = true;
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! Timer_Attivo(L_P1__GetLds_m14(my_id)));
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_9);
    res_AndLogicOP_8 = (res_AndLogicOP_8 && (L_P1__GetParamConsd(my_id) == false));
    
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_AndLogicOP_8);
    res_OrLogicOP_7 = (res_OrLogicOP_7 || Timer_Attivo(L_P1__GetLds_m12(my_id)));
    
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_OrLogicOP_7);
    bool res_AndLogicOP_10 = true;
    bool res_NotLogicOP_11 = true;
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (L_P1__GetParamLds_m9(my_id) == true));
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! res_NotLogicOP_12);
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_NotLogicOP_11);
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (L_P1__GetParamLds_m8(my_id) == true));
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_NotLogicOP_13);
    
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_AndLogicOP_10);
    
    res_ImpliesLogicOp_3 = (res_ImpliesLogicOp_3 && res_OrLogicOP_6);
    }
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_ImpliesLogicOp_3);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *49,*  *,*  il timer LDS_MainClass_C1_timer_T2 sia attivo
    res_AndLogicOP_0 = (res_AndLogicOP_0 && Timer_Attivo(L_P1__GetLds_m13(my_id)));
    
    
    
    
    return res_AndLogicOP_0;
}


// Macro valorizzate

/*
    CNL corrispondente:
    
    { commento: {[}  se il parametro ConsDef è uguale a FALSE  commento: {37,} e  se la variabile LDS_MainClass_C1_variabile_V1 è  uguale a c120 commento: {34,} o  se lo stato  è  diverso da  commento: {56,}  state1  commento: {106,} , assegna alla macro il valore avanzamento
    
     commento: {46,} assegna alla macro il valore avanzamento commento: {],}
    }
*/
C1_Enumerat1 L_P1__Macro1(instance_id_t const my_id , bool argom, C1_Enumerat4 argom1)
{
C1_Enumerat1 res_macro_val;
    
    //  *[*  se il parametro ConsDef è uguale a FALSE  *37,* e  se la variabile LDS_MainClass_C1_variabile_V1 è  uguale a c120 *34,* o  se lo stato  è  diverso da  *56,*  state1
    bool res_OrLogicOP_0 = false;
    bool res_AndLogicOP_1 = true;
    res_AndLogicOP_1 = (res_AndLogicOP_1 && (L_P1__GetParamConsd(my_id) == false));
    res_AndLogicOP_1 = (res_AndLogicOP_1 && (L_P1__GetLds_m10(my_id) == c120));
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_1);
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (L_P1_C1_GetState(my_id) == C1_St_state));
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_2);
    
    if(res_OrLogicOP_0){
    
    res_macro_val = avanzamento;
    }
    else{
    res_macro_val = avanzamento;
    }
    return res_macro_val;
}



