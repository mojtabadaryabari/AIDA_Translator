// Codice del modello 'TestCase10', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#include "Logica/ClasseMainClass_C1.h"
#include "Logica/ClasseSubClass_C2.h"
#include "Logica/ClasseSubClass_C3.h"
#include "Logica/ClasseSubClass_C3_priv.h"
#include "config.h"
#include "scheduler.h"


// ********** Gestione comandi manuali **********

static void L_P1_C3_InitCmdsResponse(instance_id_t const my_id)
{
    // for each manual command of L_P1_C3
    if (L_P1__GetInEvent8(my_id)) {
	    L_P1__SetOutEvent10(my_id, LDS_MANCMD_UNEXPECTED);
    } else {
        L_P1__SetOutEvent10(my_id, LDS_MANCMD_NOOP);
    }
    if (L_P1__GetInEvent9(my_id)) {
	    L_P1__SetOutEvent11(my_id, LDS_MANCMD_UNEXPECTED);
    } else {
        L_P1__SetOutEvent11(my_id, LDS_MANCMD_NOOP);
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
static inline bool L_P1__Guard15(instance_id_t const my_id)
{
    return true;
}


/*
    CNL corrispondente:
    
    {
    
     commento: {68,} commento: {37,}  se la variabile SubClass_C3_variabile_V1 non è  uguale a  commento: {53,} 4 commento: {36,} e  se il timer SubClass_C3_timer_T2 non è scaduto commento: {38,} o  se il contatore SubClass_C3_contatore_Co2 è  diverso da  commento: {56,} 13 commento: {35,} o  se il controllo SubClass_C3_controllo_C4 non è  diverso da  True , Almeno una delle seguenti { 
     commento: {38,}  se il contatore SubClass_C3_contatore_Co4 è  diverso da  commento: {56,} 14215 commento: {38,} e  se il contatore SubClass_C3_contatore_Co2 non è  diverso da  commento: {56,} 12 commento: {35,} o  se il controllo SubClass_C3_controllo_C7 non è  diverso da  False  commento: {35,} e  se il controllo SubClass_C3_controllo_C4 è  uguale a  False  commento: {37,} e  se la variabile SubClass_C3_variabile_V4 è  uguale a  True , Verifica che   commento: {49,}  commento: {,}  il timer SubClass_C3_timer_T1 non sia disattivo
    
    
     } Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
    
    
    }
*/
static inline bool L_P1__Guard16(instance_id_t const my_id)
{
    bool res_AndLogicOP_0 = true;
    
    //  *68,* *37,*  se la variabile SubClass_C3_variabile_V1 non è  uguale a  *53,* 4 *36,* e  se il timer SubClass_C3_timer_T2 non è scaduto *38,* o  se il contatore SubClass_C3_contatore_Co2 è  diverso da  *56,* 13 *35,* o  se il controllo SubClass_C3_controllo_C4 non è  diverso da  True , Almeno una delle seguenti { 
    //   *38,*  se il contatore SubClass_C3_contatore_Co4 è  diverso da  *56,* 14215 *38,* e  se il contatore SubClass_C3_contatore_Co2 non è  diverso da  *56,* 12 *35,* o  se il controllo SubClass_C3_controllo_C7 non è  diverso da  False  *35,* e  se il controllo SubClass_C3_controllo_C4 è  uguale a  False  *37,* e  se la variabile SubClass_C3_variabile_V4 è  uguale a  True , Verifica che   *49,*  *,*  il timer SubClass_C3_timer_T1 non sia disattivo
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_AndLogicOP_4 = true;
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetSubcl76(my_id) == 4u));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_5);
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! Timer_Scaduto(L_P1__GetSubcl92(my_id)));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_6);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_AndLogicOP_4);
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (Counter_GetValore(L_P1__GetSubcl93(my_id)) == 13u));
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_NotLogicOP_7);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    bool res_NotLogicOP_8 = true;
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetInSubcl43(my_id) == true));
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! res_NotLogicOP_9);
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_8);
    
    if(res_OrLogicOP_2){
    bool res_ImpliesLogicOp_10 = true;
    bool res_OrLogicOP_11 = false;
    bool res_AndLogicOP_12 = true;
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (Counter_GetValore(L_P1__GetSubcl94(my_id)) == 14215u));
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_NotLogicOP_13);
    bool res_NotLogicOP_14 = true;
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (Counter_GetValore(L_P1__GetSubcl93(my_id)) == 12u));
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! res_NotLogicOP_15);
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_NotLogicOP_14);
    
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_AndLogicOP_12);
    bool res_AndLogicOP_16 = true;
    bool res_AndLogicOP_17 = true;
    bool res_NotLogicOP_18 = true;
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (L_P1__GetInSubcl45(my_id) == false));
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! res_NotLogicOP_19);
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_NotLogicOP_18);
    res_AndLogicOP_17 = (res_AndLogicOP_17 && (L_P1__GetInSubcl43(my_id) == false));
    
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_AndLogicOP_17);
    res_AndLogicOP_16 = (res_AndLogicOP_16 && (L_P1__GetSubcl79(my_id) == true));
    
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_AndLogicOP_16);
    
    if(res_OrLogicOP_11){
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! Timer_Disattivo(L_P1__GetSubcl91(my_id)));
    res_ImpliesLogicOp_10 = (res_ImpliesLogicOp_10 && res_NotLogicOP_20);
    }
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_ImpliesLogicOp_10);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *48,*   il controllo ConsDef  sia  uguale a FALSE
    res_AndLogicOP_0 = (res_AndLogicOP_0 && (L_P1__GetInConsd2(my_id) == false));
    
    
    
    return res_AndLogicOP_0;
}


// ********** Definizione effetti **********

/*
    CNL corrispondente:
    
     {
     Nessuna 
     
     }
*/
static inline void L_P1__Effec15(instance_id_t const my_id)
{
    
}


/*
    CNL corrispondente:
    
    {
    
    Comanda al campo MainClass_C1 di SubClass_C3_lista_L3
     di eseguire  commento: {113,}  MainClass_C1_command_comm2    commento: {79,}
    }
*/
static inline void L_P1__Effec16(instance_id_t const my_id)
{
    
    //  Comanda al campo MainClass_C1 di SubClass_C3_lista_L3
    //   di eseguire  *113,*  MainClass_C1_command_comm2
    for (index_t i = 0; i < L_P1__GetParamSubcl46Length(my_id); ++i)
    {
    L_P1__Recor1 it = L_P1__GetRecSubcl46(my_id,i);
    
    L_P1__SetCAEvent2(it.mainc33,true);
    scheduler_NotifyCommand(L_P1_C1_TO_GLOBAL(it.mainc33));
    }
}



// ********** Definizione metodi **********

// Metodi standard

void L_P1_C3_Init(instance_id_t const my_id)
{
    // init variabili di stato
    L_P1__SetStato5(my_id, C3_St_Stato);
    L_P1__SetSubcl60(my_id, false);
    L_P1__SetSubcl62(my_id, false);
    L_P1__SetSubcl64(my_id, false);
    L_P1__SetSubcl66(my_id, rossogiallo5);
    L_P1__SetSubcl68(my_id, false);
    L_P1__SetSubcl69(my_id, false);
    L_P1__SetSubcl70(my_id, c270);
    L_P1__SetSubcl71(my_id, c270);
    L_P1__SetSubcl72(my_id, false);
    L_P1__SetSubcl73(my_id, false);
    L_P1__SetSubcl74(my_id, 0);
    L_P1__SetSubcl75(my_id, 0);
    L_P1__SetSubcl76(my_id, 0);
    L_P1__SetSubcl77(my_id, 0);
    L_P1__SetSubcl78(my_id, 0);
    L_P1__SetSubcl79(my_id, false);
    L_P1__SetSubcl80(my_id, false);
    // init controlli precedenti
    L_P1__SetSubcl51(my_id, false);
    L_P1__SetSubcl53(my_id, false);
    L_P1__SetSubcl55(my_id, true);
    L_P1__SetSubcl57(my_id, spento);
    L_P1__SetSubcl59(my_id, true);
    // init Timer e Counter
    Timer_AggmInit(L_P1__GetSubcl81(my_id), true, CLASS_L_P1_C3_ID, my_id, L_P1__subcl81_ID);
    Timer_Init(L_P1__GetSubcl81(my_id), 340000);
    Timer_AggmInit(L_P1__GetSubcl82(my_id), true, CLASS_L_P1_C3_ID, my_id, L_P1__subcl82_ID);
    Timer_Init(L_P1__GetSubcl82(my_id), 340000);
    Timer_AggmInit(L_P1__GetSubcl83(my_id), true, CLASS_L_P1_C3_ID, my_id, L_P1__subcl83_ID);
    Timer_Init(L_P1__GetSubcl83(my_id), 132000);
    Timer_AggmInit(L_P1__GetSubcl84(my_id), true, CLASS_L_P1_C3_ID, my_id, L_P1__subcl84_ID);
    Timer_Init(L_P1__GetSubcl84(my_id), 132000);
    Timer_AggmInit(L_P1__GetSubcl85(my_id), true, CLASS_L_P1_C3_ID, my_id, L_P1__subcl85_ID);
    Timer_Init(L_P1__GetSubcl85(my_id), 41000);
    Timer_AggmInit(L_P1__GetSubcl86(my_id), true, CLASS_L_P1_C3_ID, my_id, L_P1__subcl86_ID);
    Timer_Init(L_P1__GetSubcl86(my_id), 41000);
    Timer_AggmInit(L_P1__GetSubcl87(my_id), true, CLASS_L_P1_C3_ID, my_id, L_P1__subcl87_ID);
    Timer_Init(L_P1__GetSubcl87(my_id), 35000);
    Timer_AggmInit(L_P1__GetSubcl88(my_id), true, CLASS_L_P1_C3_ID, my_id, L_P1__subcl88_ID);
    Timer_Init(L_P1__GetSubcl88(my_id), 35000);
    Timer_AggmInit(L_P1__GetSubcl89(my_id), true, CLASS_L_P1_C3_ID, my_id, L_P1__subcl89_ID);
    Timer_Init(L_P1__GetSubcl89(my_id), 540000);
    Timer_AggmInit(L_P1__GetSubcl90(my_id), true, CLASS_L_P1_C3_ID, my_id, L_P1__subcl90_ID);
    Timer_Init(L_P1__GetSubcl90(my_id), 540000);
    Timer_AggmInit(L_P1__GetSubcl91(my_id), true, CLASS_L_P1_C3_ID, my_id, L_P1__subcl91_ID);
    Timer_Init(L_P1__GetSubcl91(my_id), 2000);
    Timer_AggmInit(L_P1__GetSubcl92(my_id), true, CLASS_L_P1_C3_ID, my_id, L_P1__subcl92_ID);
    Timer_Init(L_P1__GetSubcl92(my_id), 5000);
    Counter_AggmInit(L_P1__GetSubcl93(my_id), true, CLASS_L_P1_C3_ID, my_id, L_P1__subcl93_ID);
    Counter_Init(L_P1__GetSubcl93(my_id));
    Counter_AggmInit(L_P1__GetSubcl94(my_id), true, CLASS_L_P1_C3_ID, my_id, L_P1__subcl94_ID);
    Counter_Init(L_P1__GetSubcl94(my_id));
    // init response
    L_P1_C3_SetResponse(my_id, LDS_SCHED_NOP);

    // transizione iniziale
    if(L_P1__Guard15(my_id)) {
        L_P1_C3_SetState(my_id, C3_St_state);
	L_P1__Effec15(my_id);
    } else {
        STOP_EXECUTION(LOGIC_ERROR);
    }
    // init variabili precedenti
    L_P1__SetSubcl61(my_id, L_P1__GetSubcl60(my_id));
    L_P1__SetSubcl63(my_id, L_P1__GetSubcl62(my_id));
    L_P1__SetSubcl65(my_id, L_P1__GetSubcl64(my_id));
    L_P1__SetSubcl67(my_id, L_P1__GetSubcl66(my_id));
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
            if (L_P1__Guard16(my_id)) {
                L_P1_C3_SetState(my_id, C3_St_state);
                L_P1__Effec16(my_id);				
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
    Timer_Exec(L_P1__GetSubcl81(my_id));
    Timer_Exec(L_P1__GetSubcl82(my_id));
    Timer_Exec(L_P1__GetSubcl83(my_id));
    Timer_Exec(L_P1__GetSubcl84(my_id));
    Timer_Exec(L_P1__GetSubcl85(my_id));
    Timer_Exec(L_P1__GetSubcl86(my_id));
    Timer_Exec(L_P1__GetSubcl87(my_id));
    Timer_Exec(L_P1__GetSubcl88(my_id));
    Timer_Exec(L_P1__GetSubcl89(my_id));
    Timer_Exec(L_P1__GetSubcl90(my_id));
    Timer_Exec(L_P1__GetSubcl91(my_id));
    Timer_Exec(L_P1__GetSubcl92(my_id));
}

void L_P1_C3_GSetSafe(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C3(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C3(proc_id);
    L_P1__SetOutSubcl37(my_id, c180);
    L_P1__SetOutSubcl38(my_id, true);
    L_P1__SetOutSubcl39(my_id, c180);
    L_P1__SetOutSubcl40(my_id, c180);
    L_P1__SetOutSubcl41(my_id, false);
}

void L_P1_C3_GUpdatePrev(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C3(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C3(proc_id);
    L_P1__SetSubcl51(my_id, L_P1__GetInSubcl50(my_id));
    L_P1__SetSubcl53(my_id, L_P1__GetInSubcl52(my_id));
    L_P1__SetSubcl55(my_id, L_P1__GetInSubcl54(my_id));
    L_P1__SetSubcl57(my_id, L_P1__GetInSubcl56(my_id));
    L_P1__SetSubcl59(my_id, L_P1__GetInSubcl58(my_id));
    L_P1__SetSubcl61(my_id, L_P1__GetSubcl60(my_id));
    L_P1__SetSubcl63(my_id, L_P1__GetSubcl62(my_id));
    L_P1__SetSubcl65(my_id, L_P1__GetSubcl64(my_id));
    L_P1__SetSubcl67(my_id, L_P1__GetSubcl66(my_id));
}

// ********** Definizione macro **********

// Macro di effetto

/*
    CNL corrispondente:
    
    { commento: {110,}  se il ripristino del timer  SubClass_C3_restoreTI_TI1 è disattivo e  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} e  se la variabile SubClass_C3_variabile_V1 non è  diverso da  commento: {56,} 2 o  se il controllo ConsDef  è  uguale a FALSE , commento: {70,}Incrementa il contatore SubClass_C3_contatore_Co4
    
     ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C3_variabile_V1 il valore 8
    
    
     commento: {43,}  se MainClass_C1_timer_T4 del campo  MainClass_C1 di SubClass_C3_lista_L3 è disattivo, commento: {67,} Assegna alla variabile SubClass_C3_variabile_V4 il valore  True 
    
     ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C3_variabile_V1 il valore 1
    
    
    
    }
*/
void L_P1__Macro17(instance_id_t const my_id )
{
//  *110,*  se il ripristino del timer  SubClass_C3_restoreTI_TI1 è disattivo e  se il controllo ConsDef  è  uguale a FALSE  *37,* e  se la variabile SubClass_C3_variabile_V1 non è  diverso da  *56,* 2 o  se il controllo ConsDef  è  uguale a FALSE , *70,*Incrementa il contatore SubClass_C3_contatore_Co4
    // ,altrimenti  *67,* Assegna alla variabile SubClass_C3_variabile_V1 il valore 8
    bool res_OrLogicOP_0 = false;
    bool res_AndLogicOP_1 = true;
    bool res_AndLogicOP_2 = true;
    res_AndLogicOP_2 = (res_AndLogicOP_2 && Timer_Disattivo(L_P1__GetSubcl82(my_id)));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && (L_P1__GetInConsd2(my_id) == false));
    
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_AndLogicOP_2);
    bool res_NotLogicOP_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetSubcl76(my_id) == 2u));
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! res_NotLogicOP_4);
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_3);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_1);
    res_OrLogicOP_0 = (res_OrLogicOP_0 || (L_P1__GetInConsd2(my_id) == false));
    
    if(res_OrLogicOP_0){
    
    Counter_Incr(L_P1__GetSubcl94(my_id));
    }else{
    
    L_P1__SetSubcl76(my_id,8u);
    }
    //  *43,*  se MainClass_C1_timer_T4 del campo  MainClass_C1 di SubClass_C3_lista_L3 è disattivo, *67,* Assegna alla variabile SubClass_C3_variabile_V4 il valore  True 
    // ,altrimenti  *67,* Assegna alla variabile SubClass_C3_variabile_V1 il valore 1
    bool res_ForAllPredicate_5 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl46Length(my_id); ++i)
    {
    L_P1__Recor1 it = L_P1__GetRecSubcl46(my_id,i);
    bool res_ImpliesLogicOp_6 = true;
    res_ImpliesLogicOp_6 = (res_ImpliesLogicOp_6 && Timer_Disattivo(L_P1__GetMainc28(it.mainc33)));
    res_ForAllPredicate_5 = res_ImpliesLogicOp_6;
    if(!res_ForAllPredicate_5) {break;}
    }
    if(res_ForAllPredicate_5){
    
    L_P1__SetSubcl79(my_id,true);
    }else{
    
    L_P1__SetSubcl76(my_id,1u);
    }
}


// Macro di verifica

/*
    CNL corrispondente:
    
    { commento: {62,}  se l'argomento argomento_ave5 è  uguale a c180 commento: {39,} ,  commento: {43,}  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C3_lista_L3 esiste e  commento: {105,} è attivo, commento: {88,} quando  commento: {42,}    MainClass_C1_controllo_C7 del campo  MainClass_C1     è  diverso da  True  commento: {34,} o  se il parametro SubClass_C3_parametro_P9 non è  diverso da  True  commento: {34,} e  se il parametro SubClass_C3_parametro_P9 non è  uguale a  False  commento: {35,} e  se il controllo SubClass_C3_controllo_C7 non è  diverso da  False  commento: {38,} o  se il contatore SubClass_C3_contatore_Co4 è  uguale a  commento: {53,} 113, Almeno una delle seguenti { 
     commento: {61,} commento: {37,}  se la variabile SubClass_C3_variabile_V2 è  maggiore di  commento: {54,} 1 commento: {35,} e  se il controllo SubClass_C3_controllo_C7 non è  diverso da  True , Tutte le seguenti { 
     commento: {62,} commento: {41,}  se MainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C3_lista_L3 esiste e  commento: {105,} è  diverso da AC commento: {36,} o  se il timer SubClass_C3_timer_T1 è disattivo commento: {34,} o  se il parametro SubClass_C3_parametro_P1 è  uguale a  commento: {53,} 8, Almeno una delle seguenti { 
     commento: {62,}  se il ripristino dello stato  non è  uguale a  commento: {53,}  state1  commento: {107,} commento: {36,} e  se il timer SubClass_C3_timer_T2 non è attivo commento: {35,} e  se il controllo SubClass_C3_controllo_C1 non è  uguale a spento, Almeno una delle seguenti { 
     commento: {63,} commento: {109,}  se il ripristino della variabile  SubClass_C3_restoreva_RV2 è  diverso da c180 commento: {36,} e  se il timer SubClass_C3_timer_T2 non è attivo commento: {36,} e  se il timer SubClass_C3_timer_T1 non è scaduto commento: {35,} o  se il controllo SubClass_C3_controllo_C4 è  uguale a  True , Solo una delle seguenti { 
     commento: {62,} commento: {41,}  se MainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  uguale a AC commento: {34,} e  se il parametro SubClass_C3_parametro_P1 è  diverso da  commento: {56,} 9 commento: {37,} o  se la variabile SubClass_C3_variabile_V2 non è  maggiore di  commento: {54,} 10 commento: {35,} o  se il controllo SubClass_C3_controllo_C6 non è  uguale a spento commento: {36,} o  se il timer SubClass_C3_timer_T1 non è scaduto commento: {34,} e  se il parametro SubClass_C3_parametro_P9 è  uguale a  True , Almeno una delle seguenti { 
     commento: {62,} commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L3 è  uguale a  commento: {53,}  state1  commento: {35,} e  se il controllo SubClass_C3_controllo_C6 non è  diverso da spento, Almeno una delle seguenti { 
     commento: {62,} commento: {37,}  se la variabile SubClass_C3_variabile_V1 non è  minore di  commento: {55,} 1 commento: {35,} o  se il controllo SubClass_C3_controllo_C7 è  uguale a  False  commento: {36,} o  se il timer SubClass_C3_timer_T1 non è scaduto commento: {34,} o  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  commento: {37,} o  se la variabile SubClass_C3_variabile_V1 non è  maggiore di  commento: {54,} 4 commento: {34,} e  se il parametro SubClass_C3_parametro_P1 non è  diverso da  commento: {56,} 3, Almeno una delle seguenti { 
     commento: {61,} commento: {45,}  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  diverso da  commento: {56,} 12 commento: {37,} e  se la variabile SubClass_C3_variabile_V4 è  uguale a  True , Tutte le seguenti { 
     commento: {62,} commento: {36,}  se il timer SubClass_C3_timer_T1 è scaduto commento: {37,} o  se la variabile SubClass_C3_variabile_V1 non è  uguale a  commento: {53,} 5 e  se l'argomento argomento_ave5 non  è  uguale a c180 commento: {39,} , Almeno una delle seguenti { 
     commento: {62,} commento: {44,}  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  commento: {105,} è  uguale a c270x commento: {38,} e  se il contatore SubClass_C3_contatore_Co4 non è  diverso da  commento: {56,} 1354, Almeno una delle seguenti { 
     commento: {62,}  se l'argomento argomento_ave5 non  è  uguale a c180 commento: {39,}  commento: {37,} e  se la variabile SubClass_C3_variabile_V2 è  uguale a  commento: {53,} 2 commento: {38,} e  se il contatore SubClass_C3_contatore_Co4 è  diverso da  commento: {56,} 1503 commento: {37,} e  se la variabile SubClass_C3_variabile_V4 non è  uguale a  True  commento: {35,} o  se il controllo SubClass_C3_controllo_C7 non è  uguale a  True  commento: {36,} e  se il timer SubClass_C3_timer_T2 non è attivo, Almeno una delle seguenti { 
      se la macro  SubClass_C3_macrova_M5 ( con argomento_a4   uguale a RossoVerde ,argomento_a8   uguale a avanzamento ,argomento_a9   uguale a RossoVerde ,argomento_a3   uguale a spento ,argomento_a2   uguale a avanzamento  e argomento_a6   uguale a spento )   è  uguale a  True  commento: {40,}  commento: {34,} e  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  commento: {34,} e  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  commento: {36,} e  se il timer SubClass_C3_timer_T2 è scaduto, Verifica che   commento: {47,49,50,51,}  commento: {,}  il contatore SubClass_C3_contatore_Co4 sia  uguale a  commento: {53,} 11
     commento: {104,} o  che  commento: {,}  il timer SubClass_C3_timer_T2 sia scaduto
     commento: {104,} e  che  commento: {34,}  il parametro SubClass_C3_parametro_P9 sia  diverso da  True 
     commento: {104,} e  che  commento: {34,}  il parametro SubClass_C3_parametro_P9 sia  diverso da  False 
     commento: {104,} o  che  commento: {,}  la variabile SubClass_C3_variabile_V3 non sia  maggiore di  commento: {54,} 6
    
    
     } Verifica che   commento: {47,}  commento: {34,}  il parametro SubClass_C3_parametro_P1 sia  uguale a  commento: {53,} 10
    
    
     } Verifica che   commento: {47,48,50,51,}  commento: {,}  il contatore SubClass_C3_contatore_Co2 non sia  minore di  commento: {55,} 1121
     commento: {104,} e  che  commento: {,}  il controllo SubClass_C3_controllo_C7 non sia  diverso da  True 
     commento: {104,} o  che  commento: {34,}  il parametro SubClass_C3_parametro_P1 sia  uguale a  commento: {53,} 5
     commento: {104,} o  che  commento: {,}  la variabile SubClass_C3_variabile_V2 sia  uguale a  commento: {53,} 5
     commento: {104,} o  che  commento: {38,}  il contatore SubClass_C3_contatore_Co4 non sia  diverso da  commento: {56,} 135
     commento: {104,} o  che  commento: {35,}  il controllo SubClass_C3_controllo_C4 sia  uguale a  False 
    
    
     } Verifica che   commento: {49,51,}  commento: {,}  il contatore SubClass_C3_contatore_Co2 non sia  maggiore di  commento: {54,} 12
     commento: {104,} o  che  commento: {,}  il timer SubClass_C3_timer_T1 non sia scaduto
    
    
     } Verifica che   commento: {47,49,52,}  commento: {34,}  il parametro SubClass_C3_parametro_P1 sia  maggiore di  commento: {54,} 4
     commento: {104,} o  che  commento: {,}  il timer SubClass_C3_timer_T2 sia scaduto
     commento: {104,} e  che   l'argomento argomento_ave1 sia  diverso da spento commento: {,} 
     commento: {104,} e  che  commento: {36,}  il timer SubClass_C3_timer_T1 non sia scaduto
    
    
     } Verifica che   commento: {48,51,52,}   l'argomento argomento_ave5 sia  diverso da c180 commento: {,} 
     commento: {104,} e  che  commento: {,}  il contatore SubClass_C3_contatore_Co4 non sia  minore di  commento: {55,} 12
     commento: {104,} e  che   l'argomento argomento_ave1 non  sia  diverso da spento commento: {39,} 
     commento: {104,} o  che  commento: {,}  il controllo SubClass_C3_controllo_C4 non sia  diverso da  True 
     commento: {104,} o  che  commento: {38,}  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  commento: {56,} 1515
    
    
     } Verifica che   commento: {48,50,}  commento: {,}  il controllo SubClass_C3_controllo_C7 non sia  diverso da  False 
     commento: {104,} o  che  commento: {,}  la variabile SubClass_C3_variabile_V1 non sia  maggiore di  commento: {54,} 5
     commento: {104,} o  che  commento: {37,}  la variabile SubClass_C3_variabile_V1 non sia  uguale a  commento: {53,} 10
    
    
     } Verifica che   commento: {48,49,50,52,}   l'argomento argomento_ave5 sia  uguale a c180 commento: {,} 
     commento: {104,} e  che  commento: {,}  la variabile SubClass_C3_variabile_V2 non sia  uguale a  commento: {53,} 10
     commento: {104,} o  che  commento: {,}  il timer SubClass_C3_timer_T2 non sia scaduto
     commento: {104,} o  che  commento: {,}  il controllo SubClass_C3_controllo_C6 non sia  diverso da spento
     commento: {104,} e  che  commento: {35,}  il controllo SubClass_C3_controllo_C4 sia  uguale a  True 
    
    
     } Verifica che   commento: {50,}  commento: {,}  la variabile SubClass_C3_variabile_V1 sia  uguale a  commento: {53,} 9
    
    
     } Verifica che   commento: {48,51,52,}   l'argomento argomento_ave5 non  sia  diverso da c180 commento: {,} 
     commento: {104,} e  che   l'argomento argomento_ave5 non  sia  diverso da c180 commento: {39,} 
     commento: {104,} e  che  commento: {,}  il controllo SubClass_C3_controllo_C7 sia  diverso da  True 
     commento: {104,} o  che   l'argomento argomento_ave5 sia  uguale a c180 commento: {39,} 
     commento: {104,} e  che  commento: {,}  il contatore SubClass_C3_contatore_Co4 non sia  diverso da  commento: {56,} 154
     commento: {104,} e  che  commento: {38,}  il contatore SubClass_C3_contatore_Co4 sia  minore di  commento: {55,} 1
    
    
     } Verifica che   commento: {48,49,}  commento: {,}  il timer SubClass_C3_timer_T1 sia scaduto
     commento: {104,} e  che  commento: {,}  il controllo SubClass_C3_controllo_C4 sia  uguale a  True 
    
    
     } Verifica che   commento: {49,}  commento: {,}  il timer SubClass_C3_timer_T2 non sia scaduto
    
    
     } Verifica che   commento: {49,51,}  commento: {,}  il timer SubClass_C3_timer_T2 non sia disattivo
     commento: {104,} o  che  commento: {,}  il contatore SubClass_C3_contatore_Co2 sia  minore di  commento: {55,} 1
     commento: {104,} e  che  commento: {36,}  il timer SubClass_C3_timer_T1 non sia disattivo
    
    
    }
*/
bool L_P1__Macro20(instance_id_t const my_id , C3_Enumerat4 argom51, C3_Enumerat3 argom52)
{
bool res_AndLogicOP_0 = true;
    
    //  *62,*  se l'argomento argomento_ave5 è  uguale a c180 *39,* ,  *43,*  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C3_lista_L3 esiste e  *105,* è attivo, *88,* quando  *42,*    MainClass_C1_controllo_C7 del campo  MainClass_C1     è  diverso da  True  *34,* o  se il parametro SubClass_C3_parametro_P9 non è  diverso da  True  *34,* e  se il parametro SubClass_C3_parametro_P9 non è  uguale a  False  *35,* e  se il controllo SubClass_C3_controllo_C7 non è  diverso da  False  *38,* o  se il contatore SubClass_C3_contatore_Co4 è  uguale a  *53,* 113, Almeno una delle seguenti { 
    //   *61,* *37,*  se la variabile SubClass_C3_variabile_V2 è  maggiore di  *54,* 1 *35,* e  se il controllo SubClass_C3_controllo_C7 non è  diverso da  True , Tutte le seguenti { 
    //   *62,* *41,*  se MainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C3_lista_L3 esiste e  *105,* è  diverso da AC *36,* o  se il timer SubClass_C3_timer_T1 è disattivo *34,* o  se il parametro SubClass_C3_parametro_P1 è  uguale a  *53,* 8, Almeno una delle seguenti { 
    //   *62,*  se il ripristino dello stato  non è  uguale a  *53,*  state1  *107,* *36,* e  se il timer SubClass_C3_timer_T2 non è attivo *35,* e  se il controllo SubClass_C3_controllo_C1 non è  uguale a spento, Almeno una delle seguenti { 
    //   *63,* *109,*  se il ripristino della variabile  SubClass_C3_restoreva_RV2 è  diverso da c180 *36,* e  se il timer SubClass_C3_timer_T2 non è attivo *36,* e  se il timer SubClass_C3_timer_T1 non è scaduto *35,* o  se il controllo SubClass_C3_controllo_C4 è  uguale a  True , Solo una delle seguenti { 
    //   *62,* *41,*  se MainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  uguale a AC *34,* e  se il parametro SubClass_C3_parametro_P1 è  diverso da  *56,* 9 *37,* o  se la variabile SubClass_C3_variabile_V2 non è  maggiore di  *54,* 10 *35,* o  se il controllo SubClass_C3_controllo_C6 non è  uguale a spento *36,* o  se il timer SubClass_C3_timer_T1 non è scaduto *34,* e  se il parametro SubClass_C3_parametro_P9 è  uguale a  True , Almeno una delle seguenti { 
    //   *62,* *111,*  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L3 è  uguale a  *53,*  state1  *35,* e  se il controllo SubClass_C3_controllo_C6 non è  diverso da spento, Almeno una delle seguenti { 
    //   *62,* *37,*  se la variabile SubClass_C3_variabile_V1 non è  minore di  *55,* 1 *35,* o  se il controllo SubClass_C3_controllo_C7 è  uguale a  False  *36,* o  se il timer SubClass_C3_timer_T1 non è scaduto *34,* o  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  *37,* o  se la variabile SubClass_C3_variabile_V1 non è  maggiore di  *54,* 4 *34,* e  se il parametro SubClass_C3_parametro_P1 non è  diverso da  *56,* 3, Almeno una delle seguenti { 
    //   *61,* *45,*  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  diverso da  *56,* 12 *37,* e  se la variabile SubClass_C3_variabile_V4 è  uguale a  True , Tutte le seguenti { 
    //   *62,* *36,*  se il timer SubClass_C3_timer_T1 è scaduto *37,* o  se la variabile SubClass_C3_variabile_V1 non è  uguale a  *53,* 5 e  se l'argomento argomento_ave5 non  è  uguale a c180 *39,* , Almeno una delle seguenti { 
    //   *62,* *44,*  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  *105,* è  uguale a c270x *38,* e  se il contatore SubClass_C3_contatore_Co4 non è  diverso da  *56,* 1354, Almeno una delle seguenti { 
    //   *62,*  se l'argomento argomento_ave5 non  è  uguale a c180 *39,*  *37,* e  se la variabile SubClass_C3_variabile_V2 è  uguale a  *53,* 2 *38,* e  se il contatore SubClass_C3_contatore_Co4 è  diverso da  *56,* 1503 *37,* e  se la variabile SubClass_C3_variabile_V4 non è  uguale a  True  *35,* o  se il controllo SubClass_C3_controllo_C7 non è  uguale a  True  *36,* e  se il timer SubClass_C3_timer_T2 non è attivo, Almeno una delle seguenti { 
    //    se la macro  SubClass_C3_macrova_M5 ( con argomento_a4   uguale a RossoVerde ,argomento_a8   uguale a avanzamento ,argomento_a9   uguale a RossoVerde ,argomento_a3   uguale a spento ,argomento_a2   uguale a avanzamento  e argomento_a6   uguale a spento )   è  uguale a  True  *40,*  *34,* e  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  *34,* e  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  *36,* e  se il timer SubClass_C3_timer_T2 è scaduto, Verifica che   *47,49,50,51,*  *,*  il contatore SubClass_C3_contatore_Co4 sia  uguale a  *53,* 11
    //   *104,* o  che  *,*  il timer SubClass_C3_timer_T2 sia scaduto
    //   *104,* e  che  *34,*  il parametro SubClass_C3_parametro_P9 sia  diverso da  True 
    //   *104,* e  che  *34,*  il parametro SubClass_C3_parametro_P9 sia  diverso da  False 
    //   *104,* o  che  *,*  la variabile SubClass_C3_variabile_V3 non sia  maggiore di  *54,* 6
    //   } Verifica che   *47,*  *34,*  il parametro SubClass_C3_parametro_P1 sia  uguale a  *53,* 10
    //   } Verifica che   *47,48,50,51,*  *,*  il contatore SubClass_C3_contatore_Co2 non sia  minore di  *55,* 1121
    //   *104,* e  che  *,*  il controllo SubClass_C3_controllo_C7 non sia  diverso da  True 
    //   *104,* o  che  *34,*  il parametro SubClass_C3_parametro_P1 sia  uguale a  *53,* 5
    //   *104,* o  che  *,*  la variabile SubClass_C3_variabile_V2 sia  uguale a  *53,* 5
    //   *104,* o  che  *38,*  il contatore SubClass_C3_contatore_Co4 non sia  diverso da  *56,* 135
    //   *104,* o  che  *35,*  il controllo SubClass_C3_controllo_C4 sia  uguale a  False 
    //   } Verifica che   *49,51,*  *,*  il contatore SubClass_C3_contatore_Co2 non sia  maggiore di  *54,* 12
    //   *104,* o  che  *,*  il timer SubClass_C3_timer_T1 non sia scaduto
    //   } Verifica che   *47,49,52,*  *34,*  il parametro SubClass_C3_parametro_P1 sia  maggiore di  *54,* 4
    //   *104,* o  che  *,*  il timer SubClass_C3_timer_T2 sia scaduto
    //   *104,* e  che   l'argomento argomento_ave1 sia  diverso da spento *,* 
    //   *104,* e  che  *36,*  il timer SubClass_C3_timer_T1 non sia scaduto
    //   } Verifica che   *48,51,52,*   l'argomento argomento_ave5 sia  diverso da c180 *,* 
    //   *104,* e  che  *,*  il contatore SubClass_C3_contatore_Co4 non sia  minore di  *55,* 12
    //   *104,* e  che   l'argomento argomento_ave1 non  sia  diverso da spento *39,* 
    //   *104,* o  che  *,*  il controllo SubClass_C3_controllo_C4 non sia  diverso da  True 
    //   *104,* o  che  *38,*  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  *56,* 1515
    //   } Verifica che   *48,50,*  *,*  il controllo SubClass_C3_controllo_C7 non sia  diverso da  False 
    //   *104,* o  che  *,*  la variabile SubClass_C3_variabile_V1 non sia  maggiore di  *54,* 5
    //   *104,* o  che  *37,*  la variabile SubClass_C3_variabile_V1 non sia  uguale a  *53,* 10
    //   } Verifica che   *48,49,50,52,*   l'argomento argomento_ave5 sia  uguale a c180 *,* 
    //   *104,* e  che  *,*  la variabile SubClass_C3_variabile_V2 non sia  uguale a  *53,* 10
    //   *104,* o  che  *,*  il timer SubClass_C3_timer_T2 non sia scaduto
    //   *104,* o  che  *,*  il controllo SubClass_C3_controllo_C6 non sia  diverso da spento
    //   *104,* e  che  *35,*  il controllo SubClass_C3_controllo_C4 sia  uguale a  True 
    //   } Verifica che   *50,*  *,*  la variabile SubClass_C3_variabile_V1 sia  uguale a  *53,* 9
    //   } Verifica che   *48,51,52,*   l'argomento argomento_ave5 non  sia  diverso da c180 *,* 
    //   *104,* e  che   l'argomento argomento_ave5 non  sia  diverso da c180 *39,* 
    //   *104,* e  che  *,*  il controllo SubClass_C3_controllo_C7 sia  diverso da  True 
    //   *104,* o  che   l'argomento argomento_ave5 sia  uguale a c180 *39,* 
    //   *104,* e  che  *,*  il contatore SubClass_C3_contatore_Co4 non sia  diverso da  *56,* 154
    //   *104,* e  che  *38,*  il contatore SubClass_C3_contatore_Co4 sia  minore di  *55,* 1
    //   } Verifica che   *48,49,*  *,*  il timer SubClass_C3_timer_T1 sia scaduto
    //   *104,* e  che  *,*  il controllo SubClass_C3_controllo_C4 sia  uguale a  True 
    //   } Verifica che   *49,*  *,*  il timer SubClass_C3_timer_T2 non sia scaduto
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_AndLogicOP_4 = true;
    res_AndLogicOP_4 = (res_AndLogicOP_4 && (argom52 == c180));
    bool res_ForAllPredicateNotEmpty_5 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl46Length(my_id); ++i)
    {
    L_P1__Recor1 it = L_P1__GetRecSubcl46(my_id,i);
    bool res_ImpliesLogicOp_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetInMainc6(it.mainc33) == true));
    if(res_NotLogicOP_7){
    res_ImpliesLogicOp_6 = (res_ImpliesLogicOp_6 && Timer_Attivo(L_P1__GetMainc27(it.mainc33)));
    res_ForAllPredicateNotEmpty_5 = res_ImpliesLogicOp_6;
    if(!res_ForAllPredicateNotEmpty_5) {break;}
    }
    }
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_ForAllPredicateNotEmpty_5);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_AndLogicOP_4);
    bool res_AndLogicOP_8 = true;
    bool res_AndLogicOP_9 = true;
    bool res_NotLogicOP_10 = true;
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (L_P1__GetParamSubcl49(my_id) == true));
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! res_NotLogicOP_11);
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_NotLogicOP_10);
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (L_P1__GetParamSubcl49(my_id) == false));
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_NotLogicOP_12);
    
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_AndLogicOP_9);
    bool res_NotLogicOP_13 = true;
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1__GetInSubcl45(my_id) == false));
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! res_NotLogicOP_14);
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_13);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_AndLogicOP_8);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    res_OrLogicOP_2 = (res_OrLogicOP_2 || (Counter_GetValore(L_P1__GetSubcl94(my_id)) == 113u));
    
    if(res_OrLogicOP_2){
    bool res_OrLogicOP_15 = false;
    bool res_ImpliesLogicOp_16 = true;
    bool res_AndLogicOP_17 = true;
    res_AndLogicOP_17 = (res_AndLogicOP_17 && (L_P1__GetSubcl77(my_id) > 1u));
    bool res_NotLogicOP_18 = true;
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (L_P1__GetInSubcl45(my_id) == true));
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! res_NotLogicOP_19);
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_NotLogicOP_18);
    
    if(res_AndLogicOP_17){
    bool res_AndLogicOP_20 = true;
    bool res_ImpliesLogicOp_21 = true;
    bool res_OrLogicOP_22 = false;
    bool res_OrLogicOP_23 = false;
    bool res_ForAllPredicateNotEmpty_24 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl46Length(my_id); ++i)
    {
    L_P1__Recor1 it = L_P1__GetRecSubcl46(my_id,i);
    bool res_ImpliesLogicOp_25 = true;
    bool res_NotLogicOP_26 = true;
    res_NotLogicOP_26 = (res_NotLogicOP_26 && ! (L_P1__GetParamMainc7(it.mainc33) == ac));
    res_ImpliesLogicOp_25 = (res_ImpliesLogicOp_25 && res_NotLogicOP_26);
    res_ForAllPredicateNotEmpty_24 = res_ImpliesLogicOp_25;
    if(!res_ForAllPredicateNotEmpty_24) {break;}
    }
    res_OrLogicOP_23 = (res_OrLogicOP_23 || res_ForAllPredicateNotEmpty_24);
    res_OrLogicOP_23 = (res_OrLogicOP_23 || Timer_Disattivo(L_P1__GetSubcl91(my_id)));
    
    res_OrLogicOP_22 = (res_OrLogicOP_22 || res_OrLogicOP_23);
    res_OrLogicOP_22 = (res_OrLogicOP_22 || (L_P1__GetParamSubcl48(my_id) == 8u));
    
    if(res_OrLogicOP_22){
    bool res_OrLogicOP_27 = false;
    bool res_ImpliesLogicOp_28 = true;
    bool res_AndLogicOP_29 = true;
    bool res_AndLogicOP_30 = true;
    bool res_NotLogicOP_31 = true;
    res_NotLogicOP_31 = (res_NotLogicOP_31 && ! (L_P1__GetStato5(my_id) == C3_St_state));
    res_AndLogicOP_30 = (res_AndLogicOP_30 && res_NotLogicOP_31);
    bool res_NotLogicOP_32 = true;
    res_NotLogicOP_32 = (res_NotLogicOP_32 && ! Timer_Attivo(L_P1__GetSubcl92(my_id)));
    res_AndLogicOP_30 = (res_AndLogicOP_30 && res_NotLogicOP_32);
    
    res_AndLogicOP_29 = (res_AndLogicOP_29 && res_AndLogicOP_30);
    bool res_NotLogicOP_33 = true;
    res_NotLogicOP_33 = (res_NotLogicOP_33 && ! (L_P1__GetInSubcl42(my_id) == spento));
    res_AndLogicOP_29 = (res_AndLogicOP_29 && res_NotLogicOP_33);
    
    if(res_AndLogicOP_29){
    bool res_OrLogicOP_34 = false;
    bool res_ImpliesLogicOp_35 = true;
    bool res_OrLogicOP_36 = false;
    bool res_AndLogicOP_37 = true;
    bool res_AndLogicOP_38 = true;
    bool res_NotLogicOP_39 = true;
    res_NotLogicOP_39 = (res_NotLogicOP_39 && ! (L_P1__GetSubcl71(my_id) == c180));
    res_AndLogicOP_38 = (res_AndLogicOP_38 && res_NotLogicOP_39);
    bool res_NotLogicOP_40 = true;
    res_NotLogicOP_40 = (res_NotLogicOP_40 && ! Timer_Attivo(L_P1__GetSubcl92(my_id)));
    res_AndLogicOP_38 = (res_AndLogicOP_38 && res_NotLogicOP_40);
    
    res_AndLogicOP_37 = (res_AndLogicOP_37 && res_AndLogicOP_38);
    bool res_NotLogicOP_41 = true;
    res_NotLogicOP_41 = (res_NotLogicOP_41 && ! Timer_Scaduto(L_P1__GetSubcl91(my_id)));
    res_AndLogicOP_37 = (res_AndLogicOP_37 && res_NotLogicOP_41);
    
    res_OrLogicOP_36 = (res_OrLogicOP_36 || res_AndLogicOP_37);
    res_OrLogicOP_36 = (res_OrLogicOP_36 || (L_P1__GetInSubcl43(my_id) == true));
    
    if(res_OrLogicOP_36){
    bool res_XorLogicOP_42 = true;
    int xorIndex_res_XorLogicOP_42 = 0;
    bool res_ImpliesLogicOp_43 = true;
    bool res_OrLogicOP_44 = false;
    bool res_OrLogicOP_45 = false;
    bool res_OrLogicOP_46 = false;
    bool res_AndLogicOP_47 = true;
    bool res_ForAllPredicate_48 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl47Length(my_id); ++i)
    {
    L_P1__Recor2 it = L_P1__GetRecSubcl47(my_id,i);
    bool res_ImpliesLogicOp_49 = true;
    res_ImpliesLogicOp_49 = (res_ImpliesLogicOp_49 && (L_P1__GetParamMainc7(it.mainc34) == ac));
    res_ForAllPredicate_48 = res_ImpliesLogicOp_49;
    if(!res_ForAllPredicate_48) {break;}
    }
    res_AndLogicOP_47 = (res_AndLogicOP_47 && res_ForAllPredicate_48);
    bool res_NotLogicOP_50 = true;
    res_NotLogicOP_50 = (res_NotLogicOP_50 && ! (L_P1__GetParamSubcl48(my_id) == 9u));
    res_AndLogicOP_47 = (res_AndLogicOP_47 && res_NotLogicOP_50);
    
    res_OrLogicOP_46 = (res_OrLogicOP_46 || res_AndLogicOP_47);
    bool res_NotLogicOP_51 = true;
    res_NotLogicOP_51 = (res_NotLogicOP_51 && ! (L_P1__GetSubcl77(my_id) > 10u));
    res_OrLogicOP_46 = (res_OrLogicOP_46 || res_NotLogicOP_51);
    
    res_OrLogicOP_45 = (res_OrLogicOP_45 || res_OrLogicOP_46);
    bool res_NotLogicOP_52 = true;
    res_NotLogicOP_52 = (res_NotLogicOP_52 && ! (L_P1__GetInSubcl44(my_id) == spento));
    res_OrLogicOP_45 = (res_OrLogicOP_45 || res_NotLogicOP_52);
    
    res_OrLogicOP_44 = (res_OrLogicOP_44 || res_OrLogicOP_45);
    bool res_AndLogicOP_53 = true;
    bool res_NotLogicOP_54 = true;
    res_NotLogicOP_54 = (res_NotLogicOP_54 && ! Timer_Scaduto(L_P1__GetSubcl91(my_id)));
    res_AndLogicOP_53 = (res_AndLogicOP_53 && res_NotLogicOP_54);
    res_AndLogicOP_53 = (res_AndLogicOP_53 && (L_P1__GetParamSubcl49(my_id) == true));
    
    res_OrLogicOP_44 = (res_OrLogicOP_44 || res_AndLogicOP_53);
    
    if(res_OrLogicOP_44){
    bool res_OrLogicOP_55 = false;
    bool res_ImpliesLogicOp_56 = true;
    bool res_AndLogicOP_57 = true;
    bool res_ForAllPredicate_58 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl46Length(my_id); ++i)
    {
    L_P1__Recor1 it = L_P1__GetRecSubcl46(my_id,i);
    bool res_ImpliesLogicOp_59 = true;
    res_ImpliesLogicOp_59 = (res_ImpliesLogicOp_59 && (L_P1_C1_GetState(it.mainc33) == C1_St_state));
    res_ForAllPredicate_58 = res_ImpliesLogicOp_59;
    if(!res_ForAllPredicate_58) {break;}
    }
    res_AndLogicOP_57 = (res_AndLogicOP_57 && res_ForAllPredicate_58);
    bool res_NotLogicOP_60 = true;
    bool res_NotLogicOP_61 = true;
    res_NotLogicOP_61 = (res_NotLogicOP_61 && ! (L_P1__GetInSubcl44(my_id) == spento));
    res_NotLogicOP_60 = (res_NotLogicOP_60 && ! res_NotLogicOP_61);
    res_AndLogicOP_57 = (res_AndLogicOP_57 && res_NotLogicOP_60);
    
    if(res_AndLogicOP_57){
    bool res_OrLogicOP_62 = false;
    bool res_ImpliesLogicOp_63 = true;
    bool res_OrLogicOP_64 = false;
    bool res_OrLogicOP_65 = false;
    bool res_OrLogicOP_66 = false;
    bool res_OrLogicOP_67 = false;
    bool res_NotLogicOP_68 = true;
    res_NotLogicOP_68 = (res_NotLogicOP_68 && ! (L_P1__GetSubcl76(my_id) < 1u));
    res_OrLogicOP_67 = (res_OrLogicOP_67 || res_NotLogicOP_68);
    res_OrLogicOP_67 = (res_OrLogicOP_67 || (L_P1__GetInSubcl45(my_id) == false));
    
    res_OrLogicOP_66 = (res_OrLogicOP_66 || res_OrLogicOP_67);
    bool res_NotLogicOP_69 = true;
    res_NotLogicOP_69 = (res_NotLogicOP_69 && ! Timer_Scaduto(L_P1__GetSubcl91(my_id)));
    res_OrLogicOP_66 = (res_OrLogicOP_66 || res_NotLogicOP_69);
    
    res_OrLogicOP_65 = (res_OrLogicOP_65 || res_OrLogicOP_66);
    bool res_NotLogicOP_70 = true;
    res_NotLogicOP_70 = (res_NotLogicOP_70 && ! (L_P1__GetParamSubcl49(my_id) == true));
    res_OrLogicOP_65 = (res_OrLogicOP_65 || res_NotLogicOP_70);
    
    res_OrLogicOP_64 = (res_OrLogicOP_64 || res_OrLogicOP_65);
    bool res_AndLogicOP_71 = true;
    bool res_NotLogicOP_72 = true;
    res_NotLogicOP_72 = (res_NotLogicOP_72 && ! (L_P1__GetSubcl76(my_id) > 4u));
    res_AndLogicOP_71 = (res_AndLogicOP_71 && res_NotLogicOP_72);
    bool res_NotLogicOP_73 = true;
    bool res_NotLogicOP_74 = true;
    res_NotLogicOP_74 = (res_NotLogicOP_74 && ! (L_P1__GetParamSubcl48(my_id) == 3u));
    res_NotLogicOP_73 = (res_NotLogicOP_73 && ! res_NotLogicOP_74);
    res_AndLogicOP_71 = (res_AndLogicOP_71 && res_NotLogicOP_73);
    
    res_OrLogicOP_64 = (res_OrLogicOP_64 || res_AndLogicOP_71);
    
    if(res_OrLogicOP_64){
    bool res_OrLogicOP_75 = false;
    bool res_ImpliesLogicOp_76 = true;
    bool res_AndLogicOP_77 = true;
    bool res_ForAllPredicate_78 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl47Length(my_id); ++i)
    {
    L_P1__Recor2 it = L_P1__GetRecSubcl47(my_id,i);
    bool res_ImpliesLogicOp_79 = true;
    bool res_NotLogicOP_80 = true;
    res_NotLogicOP_80 = (res_NotLogicOP_80 && ! (Counter_GetValore(L_P1__GetMainc31(it.mainc34)) == 12u));
    res_ImpliesLogicOp_79 = (res_ImpliesLogicOp_79 && res_NotLogicOP_80);
    res_ForAllPredicate_78 = res_ImpliesLogicOp_79;
    if(!res_ForAllPredicate_78) {break;}
    }
    res_AndLogicOP_77 = (res_AndLogicOP_77 && res_ForAllPredicate_78);
    res_AndLogicOP_77 = (res_AndLogicOP_77 && (L_P1__GetSubcl79(my_id) == true));
    
    if(res_AndLogicOP_77){
    bool res_AndLogicOP_81 = true;
    bool res_ImpliesLogicOp_82 = true;
    bool res_OrLogicOP_83 = false;
    res_OrLogicOP_83 = (res_OrLogicOP_83 || Timer_Scaduto(L_P1__GetSubcl91(my_id)));
    bool res_AndLogicOP_84 = true;
    bool res_NotLogicOP_85 = true;
    res_NotLogicOP_85 = (res_NotLogicOP_85 && ! (L_P1__GetSubcl76(my_id) == 5u));
    res_AndLogicOP_84 = (res_AndLogicOP_84 && res_NotLogicOP_85);
    bool res_NotLogicOP_86 = true;
    res_NotLogicOP_86 = (res_NotLogicOP_86 && ! (argom52 == c180));
    res_AndLogicOP_84 = (res_AndLogicOP_84 && res_NotLogicOP_86);
    
    res_OrLogicOP_83 = (res_OrLogicOP_83 || res_AndLogicOP_84);
    
    if(res_OrLogicOP_83){
    bool res_OrLogicOP_87 = false;
    bool res_ImpliesLogicOp_88 = true;
    bool res_AndLogicOP_89 = true;
    bool res_ForAllPredicateNotEmpty_90 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl47Length(my_id); ++i)
    {
    L_P1__Recor2 it = L_P1__GetRecSubcl47(my_id,i);
    bool res_ImpliesLogicOp_91 = true;
    res_ImpliesLogicOp_91 = (res_ImpliesLogicOp_91 && (L_P1__GetMainc19(it.mainc34) == c270x));
    res_ForAllPredicateNotEmpty_90 = res_ImpliesLogicOp_91;
    if(!res_ForAllPredicateNotEmpty_90) {break;}
    }
    res_AndLogicOP_89 = (res_AndLogicOP_89 && res_ForAllPredicateNotEmpty_90);
    bool res_NotLogicOP_92 = true;
    bool res_NotLogicOP_93 = true;
    res_NotLogicOP_93 = (res_NotLogicOP_93 && ! (Counter_GetValore(L_P1__GetSubcl94(my_id)) == 1354u));
    res_NotLogicOP_92 = (res_NotLogicOP_92 && ! res_NotLogicOP_93);
    res_AndLogicOP_89 = (res_AndLogicOP_89 && res_NotLogicOP_92);
    
    if(res_AndLogicOP_89){
    bool res_OrLogicOP_94 = false;
    bool res_ImpliesLogicOp_95 = true;
    bool res_OrLogicOP_96 = false;
    bool res_AndLogicOP_97 = true;
    bool res_AndLogicOP_98 = true;
    bool res_AndLogicOP_99 = true;
    bool res_NotLogicOP_100 = true;
    res_NotLogicOP_100 = (res_NotLogicOP_100 && ! (argom52 == c180));
    res_AndLogicOP_99 = (res_AndLogicOP_99 && res_NotLogicOP_100);
    res_AndLogicOP_99 = (res_AndLogicOP_99 && (L_P1__GetSubcl77(my_id) == 2u));
    
    res_AndLogicOP_98 = (res_AndLogicOP_98 && res_AndLogicOP_99);
    bool res_NotLogicOP_101 = true;
    res_NotLogicOP_101 = (res_NotLogicOP_101 && ! (Counter_GetValore(L_P1__GetSubcl94(my_id)) == 1503u));
    res_AndLogicOP_98 = (res_AndLogicOP_98 && res_NotLogicOP_101);
    
    res_AndLogicOP_97 = (res_AndLogicOP_97 && res_AndLogicOP_98);
    bool res_NotLogicOP_102 = true;
    res_NotLogicOP_102 = (res_NotLogicOP_102 && ! (L_P1__GetSubcl79(my_id) == true));
    res_AndLogicOP_97 = (res_AndLogicOP_97 && res_NotLogicOP_102);
    
    res_OrLogicOP_96 = (res_OrLogicOP_96 || res_AndLogicOP_97);
    bool res_AndLogicOP_103 = true;
    bool res_NotLogicOP_104 = true;
    res_NotLogicOP_104 = (res_NotLogicOP_104 && ! (L_P1__GetInSubcl45(my_id) == true));
    res_AndLogicOP_103 = (res_AndLogicOP_103 && res_NotLogicOP_104);
    bool res_NotLogicOP_105 = true;
    res_NotLogicOP_105 = (res_NotLogicOP_105 && ! Timer_Attivo(L_P1__GetSubcl92(my_id)));
    res_AndLogicOP_103 = (res_AndLogicOP_103 && res_NotLogicOP_105);
    
    res_OrLogicOP_96 = (res_OrLogicOP_96 || res_AndLogicOP_103);
    
    if(res_OrLogicOP_96){
    bool res_ImpliesLogicOp_106 = true;
    bool res_AndLogicOP_107 = true;
    bool res_AndLogicOP_108 = true;
    bool res_AndLogicOP_109 = true;
    res_AndLogicOP_109 = (res_AndLogicOP_109 && (L_P1__Macro18(my_id,avanzamento1,spento,rossoverde,spento,avanzamento1,rossoverde) == true));
    bool res_NotLogicOP_110 = true;
    res_NotLogicOP_110 = (res_NotLogicOP_110 && ! (L_P1__GetParamSubcl49(my_id) == true));
    res_AndLogicOP_109 = (res_AndLogicOP_109 && res_NotLogicOP_110);
    
    res_AndLogicOP_108 = (res_AndLogicOP_108 && res_AndLogicOP_109);
    bool res_NotLogicOP_111 = true;
    res_NotLogicOP_111 = (res_NotLogicOP_111 && ! (L_P1__GetParamSubcl49(my_id) == true));
    res_AndLogicOP_108 = (res_AndLogicOP_108 && res_NotLogicOP_111);
    
    res_AndLogicOP_107 = (res_AndLogicOP_107 && res_AndLogicOP_108);
    res_AndLogicOP_107 = (res_AndLogicOP_107 && Timer_Scaduto(L_P1__GetSubcl92(my_id)));
    
    if(res_AndLogicOP_107){
    bool res_OrLogicOP_112 = false;
    bool res_OrLogicOP_113 = false;
    res_OrLogicOP_113 = (res_OrLogicOP_113 || (Counter_GetValore(L_P1__GetSubcl94(my_id)) == 11u));
    bool res_AndLogicOP_114 = true;
    bool res_AndLogicOP_115 = true;
    res_AndLogicOP_115 = (res_AndLogicOP_115 && Timer_Scaduto(L_P1__GetSubcl92(my_id)));
    bool res_NotLogicOP_116 = true;
    res_NotLogicOP_116 = (res_NotLogicOP_116 && ! (L_P1__GetParamSubcl49(my_id) == true));
    res_AndLogicOP_115 = (res_AndLogicOP_115 && res_NotLogicOP_116);
    
    res_AndLogicOP_114 = (res_AndLogicOP_114 && res_AndLogicOP_115);
    bool res_NotLogicOP_117 = true;
    res_NotLogicOP_117 = (res_NotLogicOP_117 && ! (L_P1__GetParamSubcl49(my_id) == false));
    res_AndLogicOP_114 = (res_AndLogicOP_114 && res_NotLogicOP_117);
    
    res_OrLogicOP_113 = (res_OrLogicOP_113 || res_AndLogicOP_114);
    
    res_OrLogicOP_112 = (res_OrLogicOP_112 || res_OrLogicOP_113);
    bool res_NotLogicOP_118 = true;
    res_NotLogicOP_118 = (res_NotLogicOP_118 && ! (L_P1__GetSubcl78(my_id) > 6u));
    res_OrLogicOP_112 = (res_OrLogicOP_112 || res_NotLogicOP_118);
    
    res_ImpliesLogicOp_106 = (res_ImpliesLogicOp_106 && res_OrLogicOP_112);
    }
    res_ImpliesLogicOp_95 = (res_ImpliesLogicOp_95 && res_ImpliesLogicOp_106);
    }
    res_OrLogicOP_94 = (res_OrLogicOP_94 || res_ImpliesLogicOp_95);
    res_OrLogicOP_94 = (res_OrLogicOP_94 || (L_P1__GetParamSubcl48(my_id) == 10u));
    
    res_ImpliesLogicOp_88 = (res_ImpliesLogicOp_88 && res_OrLogicOP_94);
    }
    res_OrLogicOP_87 = (res_OrLogicOP_87 || res_ImpliesLogicOp_88);
    bool res_OrLogicOP_119 = false;
    bool res_OrLogicOP_120 = false;
    bool res_OrLogicOP_121 = false;
    bool res_OrLogicOP_122 = false;
    bool res_AndLogicOP_123 = true;
    bool res_NotLogicOP_124 = true;
    res_NotLogicOP_124 = (res_NotLogicOP_124 && ! (Counter_GetValore(L_P1__GetSubcl93(my_id)) < 1121u));
    res_AndLogicOP_123 = (res_AndLogicOP_123 && res_NotLogicOP_124);
    bool res_NotLogicOP_125 = true;
    bool res_NotLogicOP_126 = true;
    res_NotLogicOP_126 = (res_NotLogicOP_126 && ! (L_P1__GetInSubcl45(my_id) == true));
    res_NotLogicOP_125 = (res_NotLogicOP_125 && ! res_NotLogicOP_126);
    res_AndLogicOP_123 = (res_AndLogicOP_123 && res_NotLogicOP_125);
    
    res_OrLogicOP_122 = (res_OrLogicOP_122 || res_AndLogicOP_123);
    res_OrLogicOP_122 = (res_OrLogicOP_122 || (L_P1__GetParamSubcl48(my_id) == 5u));
    
    res_OrLogicOP_121 = (res_OrLogicOP_121 || res_OrLogicOP_122);
    res_OrLogicOP_121 = (res_OrLogicOP_121 || (L_P1__GetSubcl77(my_id) == 5u));
    
    res_OrLogicOP_120 = (res_OrLogicOP_120 || res_OrLogicOP_121);
    bool res_NotLogicOP_127 = true;
    bool res_NotLogicOP_128 = true;
    res_NotLogicOP_128 = (res_NotLogicOP_128 && ! (Counter_GetValore(L_P1__GetSubcl94(my_id)) == 135u));
    res_NotLogicOP_127 = (res_NotLogicOP_127 && ! res_NotLogicOP_128);
    res_OrLogicOP_120 = (res_OrLogicOP_120 || res_NotLogicOP_127);
    
    res_OrLogicOP_119 = (res_OrLogicOP_119 || res_OrLogicOP_120);
    res_OrLogicOP_119 = (res_OrLogicOP_119 || (L_P1__GetInSubcl43(my_id) == false));
    
    res_OrLogicOP_87 = (res_OrLogicOP_87 || res_OrLogicOP_119);
    
    res_ImpliesLogicOp_82 = (res_ImpliesLogicOp_82 && res_OrLogicOP_87);
    }
    res_AndLogicOP_81 = (res_AndLogicOP_81 && res_ImpliesLogicOp_82);
    bool res_OrLogicOP_129 = false;
    bool res_NotLogicOP_130 = true;
    res_NotLogicOP_130 = (res_NotLogicOP_130 && ! (Counter_GetValore(L_P1__GetSubcl93(my_id)) > 12u));
    res_OrLogicOP_129 = (res_OrLogicOP_129 || res_NotLogicOP_130);
    bool res_NotLogicOP_131 = true;
    res_NotLogicOP_131 = (res_NotLogicOP_131 && ! Timer_Scaduto(L_P1__GetSubcl91(my_id)));
    res_OrLogicOP_129 = (res_OrLogicOP_129 || res_NotLogicOP_131);
    
    res_AndLogicOP_81 = (res_AndLogicOP_81 && res_OrLogicOP_129);
    
    res_ImpliesLogicOp_76 = (res_ImpliesLogicOp_76 && res_AndLogicOP_81);
    }
    res_OrLogicOP_75 = (res_OrLogicOP_75 || res_ImpliesLogicOp_76);
    bool res_OrLogicOP_132 = false;
    res_OrLogicOP_132 = (res_OrLogicOP_132 || (L_P1__GetParamSubcl48(my_id) > 4u));
    bool res_AndLogicOP_133 = true;
    bool res_AndLogicOP_134 = true;
    res_AndLogicOP_134 = (res_AndLogicOP_134 && Timer_Scaduto(L_P1__GetSubcl92(my_id)));
    bool res_NotLogicOP_135 = true;
    res_NotLogicOP_135 = (res_NotLogicOP_135 && ! (argom51 == spento));
    res_AndLogicOP_134 = (res_AndLogicOP_134 && res_NotLogicOP_135);
    
    res_AndLogicOP_133 = (res_AndLogicOP_133 && res_AndLogicOP_134);
    bool res_NotLogicOP_136 = true;
    res_NotLogicOP_136 = (res_NotLogicOP_136 && ! Timer_Scaduto(L_P1__GetSubcl91(my_id)));
    res_AndLogicOP_133 = (res_AndLogicOP_133 && res_NotLogicOP_136);
    
    res_OrLogicOP_132 = (res_OrLogicOP_132 || res_AndLogicOP_133);
    
    res_OrLogicOP_75 = (res_OrLogicOP_75 || res_OrLogicOP_132);
    
    res_ImpliesLogicOp_63 = (res_ImpliesLogicOp_63 && res_OrLogicOP_75);
    }
    res_OrLogicOP_62 = (res_OrLogicOP_62 || res_ImpliesLogicOp_63);
    bool res_OrLogicOP_137 = false;
    bool res_OrLogicOP_138 = false;
    bool res_AndLogicOP_139 = true;
    bool res_AndLogicOP_140 = true;
    bool res_NotLogicOP_141 = true;
    res_NotLogicOP_141 = (res_NotLogicOP_141 && ! (argom52 == c180));
    res_AndLogicOP_140 = (res_AndLogicOP_140 && res_NotLogicOP_141);
    bool res_NotLogicOP_142 = true;
    res_NotLogicOP_142 = (res_NotLogicOP_142 && ! (Counter_GetValore(L_P1__GetSubcl94(my_id)) < 12u));
    res_AndLogicOP_140 = (res_AndLogicOP_140 && res_NotLogicOP_142);
    
    res_AndLogicOP_139 = (res_AndLogicOP_139 && res_AndLogicOP_140);
    bool res_NotLogicOP_143 = true;
    bool res_NotLogicOP_144 = true;
    res_NotLogicOP_144 = (res_NotLogicOP_144 && ! (argom51 == spento));
    res_NotLogicOP_143 = (res_NotLogicOP_143 && ! res_NotLogicOP_144);
    res_AndLogicOP_139 = (res_AndLogicOP_139 && res_NotLogicOP_143);
    
    res_OrLogicOP_138 = (res_OrLogicOP_138 || res_AndLogicOP_139);
    bool res_NotLogicOP_145 = true;
    bool res_NotLogicOP_146 = true;
    res_NotLogicOP_146 = (res_NotLogicOP_146 && ! (L_P1__GetInSubcl43(my_id) == true));
    res_NotLogicOP_145 = (res_NotLogicOP_145 && ! res_NotLogicOP_146);
    res_OrLogicOP_138 = (res_OrLogicOP_138 || res_NotLogicOP_145);
    
    res_OrLogicOP_137 = (res_OrLogicOP_137 || res_OrLogicOP_138);
    bool res_NotLogicOP_147 = true;
    bool res_NotLogicOP_148 = true;
    res_NotLogicOP_148 = (res_NotLogicOP_148 && ! (Counter_GetValore(L_P1__GetSubcl93(my_id)) == 1515u));
    res_NotLogicOP_147 = (res_NotLogicOP_147 && ! res_NotLogicOP_148);
    res_OrLogicOP_137 = (res_OrLogicOP_137 || res_NotLogicOP_147);
    
    res_OrLogicOP_62 = (res_OrLogicOP_62 || res_OrLogicOP_137);
    
    res_ImpliesLogicOp_56 = (res_ImpliesLogicOp_56 && res_OrLogicOP_62);
    }
    res_OrLogicOP_55 = (res_OrLogicOP_55 || res_ImpliesLogicOp_56);
    bool res_OrLogicOP_149 = false;
    bool res_OrLogicOP_150 = false;
    bool res_NotLogicOP_151 = true;
    bool res_NotLogicOP_152 = true;
    res_NotLogicOP_152 = (res_NotLogicOP_152 && ! (L_P1__GetInSubcl45(my_id) == false));
    res_NotLogicOP_151 = (res_NotLogicOP_151 && ! res_NotLogicOP_152);
    res_OrLogicOP_150 = (res_OrLogicOP_150 || res_NotLogicOP_151);
    bool res_NotLogicOP_153 = true;
    res_NotLogicOP_153 = (res_NotLogicOP_153 && ! (L_P1__GetSubcl76(my_id) > 5u));
    res_OrLogicOP_150 = (res_OrLogicOP_150 || res_NotLogicOP_153);
    
    res_OrLogicOP_149 = (res_OrLogicOP_149 || res_OrLogicOP_150);
    bool res_NotLogicOP_154 = true;
    res_NotLogicOP_154 = (res_NotLogicOP_154 && ! (L_P1__GetSubcl76(my_id) == 10u));
    res_OrLogicOP_149 = (res_OrLogicOP_149 || res_NotLogicOP_154);
    
    res_OrLogicOP_55 = (res_OrLogicOP_55 || res_OrLogicOP_149);
    
    res_ImpliesLogicOp_43 = (res_ImpliesLogicOp_43 && res_OrLogicOP_55);
    }
    if(res_ImpliesLogicOp_43){
    xorIndex_res_XorLogicOP_42 = (xorIndex_res_XorLogicOP_42 + 1);
    }
    bool res_OrLogicOP_155 = false;
    bool res_OrLogicOP_156 = false;
    bool res_AndLogicOP_157 = true;
    res_AndLogicOP_157 = (res_AndLogicOP_157 && (argom52 == c180));
    bool res_NotLogicOP_158 = true;
    res_NotLogicOP_158 = (res_NotLogicOP_158 && ! (L_P1__GetSubcl77(my_id) == 10u));
    res_AndLogicOP_157 = (res_AndLogicOP_157 && res_NotLogicOP_158);
    
    res_OrLogicOP_156 = (res_OrLogicOP_156 || res_AndLogicOP_157);
    bool res_NotLogicOP_159 = true;
    res_NotLogicOP_159 = (res_NotLogicOP_159 && ! Timer_Scaduto(L_P1__GetSubcl92(my_id)));
    res_OrLogicOP_156 = (res_OrLogicOP_156 || res_NotLogicOP_159);
    
    res_OrLogicOP_155 = (res_OrLogicOP_155 || res_OrLogicOP_156);
    bool res_AndLogicOP_160 = true;
    bool res_NotLogicOP_161 = true;
    bool res_NotLogicOP_162 = true;
    res_NotLogicOP_162 = (res_NotLogicOP_162 && ! (L_P1__GetInSubcl44(my_id) == spento));
    res_NotLogicOP_161 = (res_NotLogicOP_161 && ! res_NotLogicOP_162);
    res_AndLogicOP_160 = (res_AndLogicOP_160 && res_NotLogicOP_161);
    res_AndLogicOP_160 = (res_AndLogicOP_160 && (L_P1__GetInSubcl43(my_id) == true));
    
    res_OrLogicOP_155 = (res_OrLogicOP_155 || res_AndLogicOP_160);
    
    if(res_OrLogicOP_155){
    xorIndex_res_XorLogicOP_42 = (xorIndex_res_XorLogicOP_42 + 1);
    }
    
    res_XorLogicOP_42 = (res_XorLogicOP_42 && (xorIndex_res_XorLogicOP_42 == 1));
    res_ImpliesLogicOp_35 = (res_ImpliesLogicOp_35 && res_XorLogicOP_42);
    }
    res_OrLogicOP_34 = (res_OrLogicOP_34 || res_ImpliesLogicOp_35);
    res_OrLogicOP_34 = (res_OrLogicOP_34 || (L_P1__GetSubcl76(my_id) == 9u));
    
    res_ImpliesLogicOp_28 = (res_ImpliesLogicOp_28 && res_OrLogicOP_34);
    }
    res_OrLogicOP_27 = (res_OrLogicOP_27 || res_ImpliesLogicOp_28);
    bool res_OrLogicOP_163 = false;
    bool res_AndLogicOP_164 = true;
    bool res_AndLogicOP_165 = true;
    bool res_NotLogicOP_166 = true;
    bool res_NotLogicOP_167 = true;
    res_NotLogicOP_167 = (res_NotLogicOP_167 && ! (argom52 == c180));
    res_NotLogicOP_166 = (res_NotLogicOP_166 && ! res_NotLogicOP_167);
    res_AndLogicOP_165 = (res_AndLogicOP_165 && res_NotLogicOP_166);
    bool res_NotLogicOP_168 = true;
    bool res_NotLogicOP_169 = true;
    res_NotLogicOP_169 = (res_NotLogicOP_169 && ! (argom52 == c180));
    res_NotLogicOP_168 = (res_NotLogicOP_168 && ! res_NotLogicOP_169);
    res_AndLogicOP_165 = (res_AndLogicOP_165 && res_NotLogicOP_168);
    
    res_AndLogicOP_164 = (res_AndLogicOP_164 && res_AndLogicOP_165);
    bool res_NotLogicOP_170 = true;
    res_NotLogicOP_170 = (res_NotLogicOP_170 && ! (L_P1__GetInSubcl45(my_id) == true));
    res_AndLogicOP_164 = (res_AndLogicOP_164 && res_NotLogicOP_170);
    
    res_OrLogicOP_163 = (res_OrLogicOP_163 || res_AndLogicOP_164);
    bool res_AndLogicOP_171 = true;
    bool res_AndLogicOP_172 = true;
    res_AndLogicOP_172 = (res_AndLogicOP_172 && (argom52 == c180));
    bool res_NotLogicOP_173 = true;
    bool res_NotLogicOP_174 = true;
    res_NotLogicOP_174 = (res_NotLogicOP_174 && ! (Counter_GetValore(L_P1__GetSubcl94(my_id)) == 154u));
    res_NotLogicOP_173 = (res_NotLogicOP_173 && ! res_NotLogicOP_174);
    res_AndLogicOP_172 = (res_AndLogicOP_172 && res_NotLogicOP_173);
    
    res_AndLogicOP_171 = (res_AndLogicOP_171 && res_AndLogicOP_172);
    res_AndLogicOP_171 = (res_AndLogicOP_171 && (Counter_GetValore(L_P1__GetSubcl94(my_id)) < 1u));
    
    res_OrLogicOP_163 = (res_OrLogicOP_163 || res_AndLogicOP_171);
    
    res_OrLogicOP_27 = (res_OrLogicOP_27 || res_OrLogicOP_163);
    
    res_ImpliesLogicOp_21 = (res_ImpliesLogicOp_21 && res_OrLogicOP_27);
    }
    res_AndLogicOP_20 = (res_AndLogicOP_20 && res_ImpliesLogicOp_21);
    bool res_AndLogicOP_175 = true;
    res_AndLogicOP_175 = (res_AndLogicOP_175 && Timer_Scaduto(L_P1__GetSubcl91(my_id)));
    res_AndLogicOP_175 = (res_AndLogicOP_175 && (L_P1__GetInSubcl43(my_id) == true));
    
    res_AndLogicOP_20 = (res_AndLogicOP_20 && res_AndLogicOP_175);
    
    res_ImpliesLogicOp_16 = (res_ImpliesLogicOp_16 && res_AndLogicOP_20);
    }
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_ImpliesLogicOp_16);
    bool res_NotLogicOP_176 = true;
    res_NotLogicOP_176 = (res_NotLogicOP_176 && ! Timer_Scaduto(L_P1__GetSubcl92(my_id)));
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_NotLogicOP_176);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_OrLogicOP_15);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *49,51,*  *,*  il timer SubClass_C3_timer_T2 non sia disattivo
    //   *104,* o  che  *,*  il contatore SubClass_C3_contatore_Co2 sia  minore di  *55,* 1
    //   *104,* e  che  *36,*  il timer SubClass_C3_timer_T1 non sia disattivo
    bool res_OrLogicOP_177 = false;
    bool res_NotLogicOP_178 = true;
    res_NotLogicOP_178 = (res_NotLogicOP_178 && ! Timer_Disattivo(L_P1__GetSubcl92(my_id)));
    res_OrLogicOP_177 = (res_OrLogicOP_177 || res_NotLogicOP_178);
    bool res_AndLogicOP_179 = true;
    res_AndLogicOP_179 = (res_AndLogicOP_179 && (Counter_GetValore(L_P1__GetSubcl93(my_id)) < 1u));
    bool res_NotLogicOP_180 = true;
    res_NotLogicOP_180 = (res_NotLogicOP_180 && ! Timer_Disattivo(L_P1__GetSubcl91(my_id)));
    res_AndLogicOP_179 = (res_AndLogicOP_179 && res_NotLogicOP_180);
    
    res_OrLogicOP_177 = (res_OrLogicOP_177 || res_AndLogicOP_179);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_177);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
    
    { commento: {61,} commento: {109,}  se il ripristino della variabile  SubClass_C3_restoreva_RV1 è  diverso da  True , Tutte le seguenti { 
     commento: {61,}  se il ripristino dello stato  non è  uguale a  commento: {53,}  state1  commento: {107,} commento: {38,} e  se il contatore SubClass_C3_contatore_Co2 è  maggiore di  commento: {54,} 155 commento: {34,} o  se il parametro SubClass_C3_parametro_P9 è  uguale a  False  commento: {35,} e  se il controllo SubClass_C3_controllo_C7 non è  uguale a  False , Tutte le seguenti { 
     commento: {63,}  se la macro  SubClass_C3_macrova_M5 ( con argomento_a4   uguale a spento ,argomento_a8   uguale a avanzamento ,argomento_a9   uguale a spento ,argomento_a3   uguale a RossoGiallox ,argomento_a2   uguale a avanzamento  e argomento_a6   uguale a RossoGiallox )   è  uguale a  True  commento: {40,}  o  se l'argomento argomento_ave4 è  uguale a c180 commento: {39,}  commento: {36,} o  se il timer SubClass_C3_timer_T2 non è disattivo o  se l'argomento argomento_ave3 è  uguale a  True  commento: {39,}  e  se l'argomento argomento_ave9 non  è  uguale a  False  commento: {39,}  commento: {35,} o  se il controllo SubClass_C3_controllo_C4 non è  uguale a  False , Solo una delle seguenti { 
     commento: {36,}  se il timer SubClass_C3_timer_T2 non è disattivo commento: {36,} e  se il timer SubClass_C3_timer_T1 è attivo commento: {36,} o  se il timer SubClass_C3_timer_T2 è attivo, Verifica che   commento: {47,49,52,}  commento: {34,}  il parametro SubClass_C3_parametro_P9 non sia  diverso da  True 
     commento: {104,} e  che  commento: {,}  il timer SubClass_C3_timer_T2 non sia attivo
     commento: {104,} e  che  commento: {34,}  il parametro SubClass_C3_parametro_P9 non sia  diverso da  False 
     commento: {104,} o  che   l'argomento argomento_ave1 non  sia  uguale a  True  commento: {,} 
    
    
     } Verifica che   commento: {47,48,52,}  commento: {,}  il controllo SubClass_C3_controllo_C7 sia  diverso da  False 
     commento: {104,} e  che  commento: {34,}  il parametro SubClass_C3_parametro_P9 non sia  uguale a  False 
     commento: {104,} o  che   l'argomento argomento_ave9 non  sia  diverso da  True  commento: {,} 
    
    
     } Verifica che   commento: {48,}  commento: {,}  il controllo SubClass_C3_controllo_C4 non sia  uguale a  False 
    
    
     } Verifica che   commento: {52,}   l'argomento argomento_ave9 non  sia  diverso da  False  commento: {,} 
    
    
    }
*/
bool L_P1__Macro21(instance_id_t const my_id , bool argom53, C3_Enumerat4 argom54, bool argom55, C3_Enumerat3 argom56, C3_Enumerat3 argom57, bool argom58)
{
bool res_AndLogicOP_0 = true;
    
    //  *61,* *109,*  se il ripristino della variabile  SubClass_C3_restoreva_RV1 è  diverso da  True , Tutte le seguenti { 
    //   *61,*  se il ripristino dello stato  non è  uguale a  *53,*  state1  *107,* *38,* e  se il contatore SubClass_C3_contatore_Co2 è  maggiore di  *54,* 155 *34,* o  se il parametro SubClass_C3_parametro_P9 è  uguale a  False  *35,* e  se il controllo SubClass_C3_controllo_C7 non è  uguale a  False , Tutte le seguenti { 
    //   *63,*  se la macro  SubClass_C3_macrova_M5 ( con argomento_a4   uguale a spento ,argomento_a8   uguale a avanzamento ,argomento_a9   uguale a spento ,argomento_a3   uguale a RossoGiallox ,argomento_a2   uguale a avanzamento  e argomento_a6   uguale a RossoGiallox )   è  uguale a  True  *40,*  o  se l'argomento argomento_ave4 è  uguale a c180 *39,*  *36,* o  se il timer SubClass_C3_timer_T2 non è disattivo o  se l'argomento argomento_ave3 è  uguale a  True  *39,*  e  se l'argomento argomento_ave9 non  è  uguale a  False  *39,*  *35,* o  se il controllo SubClass_C3_controllo_C4 non è  uguale a  False , Solo una delle seguenti { 
    //   *36,*  se il timer SubClass_C3_timer_T2 non è disattivo *36,* e  se il timer SubClass_C3_timer_T1 è attivo *36,* o  se il timer SubClass_C3_timer_T2 è attivo, Verifica che   *47,49,52,*  *34,*  il parametro SubClass_C3_parametro_P9 non sia  diverso da  True 
    //   *104,* e  che  *,*  il timer SubClass_C3_timer_T2 non sia attivo
    //   *104,* e  che  *34,*  il parametro SubClass_C3_parametro_P9 non sia  diverso da  False 
    //   *104,* o  che   l'argomento argomento_ave1 non  sia  uguale a  True  *,* 
    //   } Verifica che   *47,48,52,*  *,*  il controllo SubClass_C3_controllo_C7 sia  diverso da  False 
    //   *104,* e  che  *34,*  il parametro SubClass_C3_parametro_P9 non sia  uguale a  False 
    //   *104,* o  che   l'argomento argomento_ave9 non  sia  diverso da  True  *,* 
    //   } Verifica che   *48,*  *,*  il controllo SubClass_C3_controllo_C4 non sia  uguale a  False 
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (L_P1__GetSubcl69(my_id) == true));
    if(res_NotLogicOP_2){
    bool res_AndLogicOP_3 = true;
    bool res_ImpliesLogicOp_4 = true;
    bool res_OrLogicOP_5 = false;
    bool res_AndLogicOP_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetStato5(my_id) == C3_St_state));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_7);
    res_AndLogicOP_6 = (res_AndLogicOP_6 && (Counter_GetValore(L_P1__GetSubcl93(my_id)) > 155u));
    
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_AndLogicOP_6);
    bool res_AndLogicOP_8 = true;
    res_AndLogicOP_8 = (res_AndLogicOP_8 && (L_P1__GetParamSubcl49(my_id) == false));
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetInSubcl45(my_id) == false));
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_9);
    
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_AndLogicOP_8);
    
    if(res_OrLogicOP_5){
    bool res_AndLogicOP_10 = true;
    bool res_ImpliesLogicOp_11 = true;
    bool res_OrLogicOP_12 = false;
    bool res_OrLogicOP_13 = false;
    bool res_OrLogicOP_14 = false;
    bool res_OrLogicOP_15 = false;
    res_OrLogicOP_15 = (res_OrLogicOP_15 || (L_P1__Macro18(my_id,avanzamento1,rossogiallo5,spento,rossogiallo5,avanzamento1,spento) == true));
    res_OrLogicOP_15 = (res_OrLogicOP_15 || (argom56 == c180));
    
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_OrLogicOP_15);
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! Timer_Disattivo(L_P1__GetSubcl92(my_id)));
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_NotLogicOP_16);
    
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_OrLogicOP_14);
    bool res_AndLogicOP_17 = true;
    res_AndLogicOP_17 = (res_AndLogicOP_17 && (argom55 == true));
    bool res_NotLogicOP_18 = true;
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! (argom58 == false));
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_NotLogicOP_18);
    
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_AndLogicOP_17);
    
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_OrLogicOP_13);
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (L_P1__GetInSubcl43(my_id) == false));
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_NotLogicOP_19);
    
    if(res_OrLogicOP_12){
    bool res_ImpliesLogicOp_20 = true;
    bool res_OrLogicOP_21 = false;
    bool res_AndLogicOP_22 = true;
    bool res_NotLogicOP_23 = true;
    res_NotLogicOP_23 = (res_NotLogicOP_23 && ! Timer_Disattivo(L_P1__GetSubcl92(my_id)));
    res_AndLogicOP_22 = (res_AndLogicOP_22 && res_NotLogicOP_23);
    res_AndLogicOP_22 = (res_AndLogicOP_22 && Timer_Attivo(L_P1__GetSubcl91(my_id)));
    
    res_OrLogicOP_21 = (res_OrLogicOP_21 || res_AndLogicOP_22);
    res_OrLogicOP_21 = (res_OrLogicOP_21 || Timer_Attivo(L_P1__GetSubcl92(my_id)));
    
    if(res_OrLogicOP_21){
    bool res_OrLogicOP_24 = false;
    bool res_AndLogicOP_25 = true;
    bool res_AndLogicOP_26 = true;
    bool res_NotLogicOP_27 = true;
    bool res_NotLogicOP_28 = true;
    res_NotLogicOP_28 = (res_NotLogicOP_28 && ! (L_P1__GetParamSubcl49(my_id) == true));
    res_NotLogicOP_27 = (res_NotLogicOP_27 && ! res_NotLogicOP_28);
    res_AndLogicOP_26 = (res_AndLogicOP_26 && res_NotLogicOP_27);
    bool res_NotLogicOP_29 = true;
    res_NotLogicOP_29 = (res_NotLogicOP_29 && ! Timer_Attivo(L_P1__GetSubcl92(my_id)));
    res_AndLogicOP_26 = (res_AndLogicOP_26 && res_NotLogicOP_29);
    
    res_AndLogicOP_25 = (res_AndLogicOP_25 && res_AndLogicOP_26);
    bool res_NotLogicOP_30 = true;
    bool res_NotLogicOP_31 = true;
    res_NotLogicOP_31 = (res_NotLogicOP_31 && ! (L_P1__GetParamSubcl49(my_id) == false));
    res_NotLogicOP_30 = (res_NotLogicOP_30 && ! res_NotLogicOP_31);
    res_AndLogicOP_25 = (res_AndLogicOP_25 && res_NotLogicOP_30);
    
    res_OrLogicOP_24 = (res_OrLogicOP_24 || res_AndLogicOP_25);
    bool res_NotLogicOP_32 = true;
    res_NotLogicOP_32 = (res_NotLogicOP_32 && ! (argom53 == true));
    res_OrLogicOP_24 = (res_OrLogicOP_24 || res_NotLogicOP_32);
    
    res_ImpliesLogicOp_20 = (res_ImpliesLogicOp_20 && res_OrLogicOP_24);
    }
    res_ImpliesLogicOp_11 = (res_ImpliesLogicOp_11 && res_ImpliesLogicOp_20);
    }
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_ImpliesLogicOp_11);
    bool res_OrLogicOP_33 = false;
    bool res_AndLogicOP_34 = true;
    bool res_NotLogicOP_35 = true;
    res_NotLogicOP_35 = (res_NotLogicOP_35 && ! (L_P1__GetInSubcl45(my_id) == false));
    res_AndLogicOP_34 = (res_AndLogicOP_34 && res_NotLogicOP_35);
    bool res_NotLogicOP_36 = true;
    res_NotLogicOP_36 = (res_NotLogicOP_36 && ! (L_P1__GetParamSubcl49(my_id) == false));
    res_AndLogicOP_34 = (res_AndLogicOP_34 && res_NotLogicOP_36);
    
    res_OrLogicOP_33 = (res_OrLogicOP_33 || res_AndLogicOP_34);
    bool res_NotLogicOP_37 = true;
    bool res_NotLogicOP_38 = true;
    res_NotLogicOP_38 = (res_NotLogicOP_38 && ! (argom58 == true));
    res_NotLogicOP_37 = (res_NotLogicOP_37 && ! res_NotLogicOP_38);
    res_OrLogicOP_33 = (res_OrLogicOP_33 || res_NotLogicOP_37);
    
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_OrLogicOP_33);
    
    res_ImpliesLogicOp_4 = (res_ImpliesLogicOp_4 && res_AndLogicOP_10);
    }
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_ImpliesLogicOp_4);
    bool res_NotLogicOP_39 = true;
    res_NotLogicOP_39 = (res_NotLogicOP_39 && ! (L_P1__GetInSubcl43(my_id) == false));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_39);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_AndLogicOP_3);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *52,*   l'argomento argomento_ave9 non  sia  diverso da  False
    bool res_NotLogicOP_40 = true;
    bool res_NotLogicOP_41 = true;
    res_NotLogicOP_41 = (res_NotLogicOP_41 && ! (argom58 == false));
    res_NotLogicOP_40 = (res_NotLogicOP_40 && ! res_NotLogicOP_41);
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_NotLogicOP_40);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
     
    { commento: {44,}  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  commento: {105,} è  diverso da c270x o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   commento: {48,}  commento: {,}  il controllo SubClass_C3_controllo_C7 sia  diverso da  False 
     commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
    
    
    }
*/
bool L_P1__Macro22(instance_id_t const my_id )
{
bool res_AndLogicOP_0 = true;
    
    //  *44,*  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  *105,* è  diverso da c270x o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   *48,*  *,*  il controllo SubClass_C3_controllo_C7 sia  diverso da  False 
    //   *104,* e  che   il controllo ConsDef  sia  uguale a FALSE
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_ForAllPredicateNotEmpty_3 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl47Length(my_id); ++i)
    {
    L_P1__Recor2 it = L_P1__GetRecSubcl47(my_id,i);
    bool res_ImpliesLogicOp_4 = true;
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetMainc19(it.mainc34) == c270x));
    res_ImpliesLogicOp_4 = (res_ImpliesLogicOp_4 && res_NotLogicOP_5);
    res_ForAllPredicateNotEmpty_3 = res_ImpliesLogicOp_4;
    if(!res_ForAllPredicateNotEmpty_3) {break;}
    }
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_ForAllPredicateNotEmpty_3);
    res_OrLogicOP_2 = (res_OrLogicOP_2 || (L_P1__GetInConsd2(my_id) == false));
    
    if(res_OrLogicOP_2){
    bool res_AndLogicOP_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetInSubcl45(my_id) == false));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_7);
    res_AndLogicOP_6 = (res_AndLogicOP_6 && (L_P1__GetInConsd2(my_id) == false));
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_AndLogicOP_6);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
     
    { commento: {63,} commento: {42,}  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C3_lista_L3 è  uguale a  True  commento: {36,} o  se il timer SubClass_C3_timer_T2 è attivo o  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} o  se il timer SubClass_C3_timer_T1 non è disattivo commento: {37,} e  se la variabile SubClass_C3_variabile_V3 non è  maggiore di  commento: {54,} 1, Solo una delle seguenti { 
     commento: {62,} commento: {36,}  se il timer SubClass_C3_timer_T2 non è scaduto commento: {34,} e  se il parametro SubClass_C3_parametro_P1 è  minore di  commento: {55,} 5, Almeno una delle seguenti { 
     commento: {35,}  se il controllo SubClass_C3_controllo_C6 è  uguale a spento,  commento: {42,}  se  MainClass_C1_controllo_C6 del campo  MainClass_C1 di SubClass_C3_lista_L3 esiste e  commento: {105,} è  diverso da AC, commento: {88,} quando  commento: {42,}    MainClass_C1_controllo_C6 del campo  MainClass_C1     commento: {105,} è  diverso da AC commento: {36,} e  se il timer SubClass_C3_timer_T1 non è disattivo e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} e  se il controllo SubClass_C3_controllo_C6 non è  diverso da spento, Verifica che   commento: {47,}  commento: {34,}  il parametro SubClass_C3_parametro_P1 sia  minore di  commento: {55,} 1
    
    
     } Verifica che   commento: {47,50,}  commento: {34,}  il parametro SubClass_C3_parametro_P1 non sia  diverso da  commento: {56,} 3
     commento: {104,} e  che  commento: {,}  la variabile SubClass_C3_variabile_V1 non sia  minore di  commento: {55,} 3
    
    
     } Verifica che   commento: {47,48,49,50,}  commento: {34,}  il parametro SubClass_C3_parametro_P1 non sia  uguale a  commento: {53,} 2
     commento: {104,} o  che  commento: {,}  il timer SubClass_C3_timer_T1 non sia attivo
     commento: {104,} o  che  commento: {,}  la variabile SubClass_C3_variabile_V1 non sia  uguale a  commento: {53,} 8
     commento: {104,} e  che  commento: {,}  il controllo SubClass_C3_controllo_C4 sia  uguale a  False 
    
    
    }
*/
bool L_P1__Macro23(instance_id_t const my_id )
{
bool res_AndLogicOP_0 = true;
    
    //  *63,* *42,*  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C3_lista_L3 è  uguale a  True  *36,* o  se il timer SubClass_C3_timer_T2 è attivo o  se il controllo ConsDef  è  uguale a FALSE  *36,* o  se il timer SubClass_C3_timer_T1 non è disattivo *37,* e  se la variabile SubClass_C3_variabile_V3 non è  maggiore di  *54,* 1, Solo una delle seguenti { 
    //   *62,* *36,*  se il timer SubClass_C3_timer_T2 non è scaduto *34,* e  se il parametro SubClass_C3_parametro_P1 è  minore di  *55,* 5, Almeno una delle seguenti { 
    //   *35,*  se il controllo SubClass_C3_controllo_C6 è  uguale a spento,  *42,*  se  MainClass_C1_controllo_C6 del campo  MainClass_C1 di SubClass_C3_lista_L3 esiste e  *105,* è  diverso da AC, *88,* quando  *42,*    MainClass_C1_controllo_C6 del campo  MainClass_C1     *105,* è  diverso da AC *36,* e  se il timer SubClass_C3_timer_T1 non è disattivo e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  *35,* e  se il controllo SubClass_C3_controllo_C6 non è  diverso da spento, Verifica che   *47,*  *34,*  il parametro SubClass_C3_parametro_P1 sia  minore di  *55,* 1
    //   } Verifica che   *47,50,*  *34,*  il parametro SubClass_C3_parametro_P1 non sia  diverso da  *56,* 3
    //   *104,* e  che  *,*  la variabile SubClass_C3_variabile_V1 non sia  minore di  *55,* 3
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_OrLogicOP_4 = false;
    bool res_ForAllPredicate_5 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl46Length(my_id); ++i)
    {
    L_P1__Recor1 it = L_P1__GetRecSubcl46(my_id,i);
    bool res_ImpliesLogicOp_6 = true;
    res_ImpliesLogicOp_6 = (res_ImpliesLogicOp_6 && (L_P1__GetInMainc6(it.mainc33) == true));
    res_ForAllPredicate_5 = res_ImpliesLogicOp_6;
    if(!res_ForAllPredicate_5) {break;}
    }
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_ForAllPredicate_5);
    res_OrLogicOP_4 = (res_OrLogicOP_4 || Timer_Attivo(L_P1__GetSubcl92(my_id)));
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_OrLogicOP_4);
    res_OrLogicOP_3 = (res_OrLogicOP_3 || (L_P1__GetInConsd2(my_id) == false));
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    bool res_AndLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! Timer_Disattivo(L_P1__GetSubcl91(my_id)));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_8);
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetSubcl78(my_id) > 1u));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_9);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_7);
    
    if(res_OrLogicOP_2){
    bool res_XorLogicOP_10 = true;
    int xorIndex_res_XorLogicOP_10 = 0;
    bool res_ImpliesLogicOp_11 = true;
    bool res_AndLogicOP_12 = true;
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! Timer_Scaduto(L_P1__GetSubcl92(my_id)));
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_NotLogicOP_13);
    res_AndLogicOP_12 = (res_AndLogicOP_12 && (L_P1__GetParamSubcl48(my_id) < 5u));
    
    if(res_AndLogicOP_12){
    bool res_ImpliesLogicOp_14 = true;
    bool res_AndLogicOP_15 = true;
    bool res_AndLogicOP_16 = true;
    bool res_AndLogicOP_17 = true;
    bool res_AndLogicOP_18 = true;
    bool res_AndLogicOP_19 = true;
    res_AndLogicOP_19 = (res_AndLogicOP_19 && (L_P1__GetInSubcl44(my_id) == spento));
    bool res_ForAllPredicateNotEmpty_20 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl46Length(my_id); ++i)
    {
    L_P1__Recor1 it = L_P1__GetRecSubcl46(my_id,i);
    bool res_ImpliesLogicOp_21 = true;
    bool res_NotLogicOP_22 = true;
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! (L_P1__GetInMainc5(it.mainc33) == ac));
    if(res_NotLogicOP_22){
    bool res_NotLogicOP_23 = true;
    res_NotLogicOP_23 = (res_NotLogicOP_23 && ! (L_P1__GetInMainc5(it.mainc33) == ac));
    res_ImpliesLogicOp_21 = (res_ImpliesLogicOp_21 && res_NotLogicOP_23);
    res_ForAllPredicateNotEmpty_20 = res_ImpliesLogicOp_21;
    if(!res_ForAllPredicateNotEmpty_20) {break;}
    }
    }
    res_AndLogicOP_19 = (res_AndLogicOP_19 && res_ForAllPredicateNotEmpty_20);
    
    res_AndLogicOP_18 = (res_AndLogicOP_18 && res_AndLogicOP_19);
    bool res_NotLogicOP_24 = true;
    res_NotLogicOP_24 = (res_NotLogicOP_24 && ! Timer_Disattivo(L_P1__GetSubcl91(my_id)));
    res_AndLogicOP_18 = (res_AndLogicOP_18 && res_NotLogicOP_24);
    
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_AndLogicOP_18);
    res_AndLogicOP_17 = (res_AndLogicOP_17 && (L_P1__GetInConsd2(my_id) == false));
    
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_AndLogicOP_17);
    res_AndLogicOP_16 = (res_AndLogicOP_16 && (L_P1__GetInConsd2(my_id) == false));
    
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_AndLogicOP_16);
    bool res_NotLogicOP_25 = true;
    bool res_NotLogicOP_26 = true;
    res_NotLogicOP_26 = (res_NotLogicOP_26 && ! (L_P1__GetInSubcl44(my_id) == spento));
    res_NotLogicOP_25 = (res_NotLogicOP_25 && ! res_NotLogicOP_26);
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_NotLogicOP_25);
    
    if(res_AndLogicOP_15){
    res_ImpliesLogicOp_14 = (res_ImpliesLogicOp_14 && (L_P1__GetParamSubcl48(my_id) < 1u));
    }
    res_ImpliesLogicOp_11 = (res_ImpliesLogicOp_11 && res_ImpliesLogicOp_14);
    }
    if(res_ImpliesLogicOp_11){
    xorIndex_res_XorLogicOP_10 = (xorIndex_res_XorLogicOP_10 + 1);
    }
    bool res_AndLogicOP_27 = true;
    bool res_NotLogicOP_28 = true;
    bool res_NotLogicOP_29 = true;
    res_NotLogicOP_29 = (res_NotLogicOP_29 && ! (L_P1__GetParamSubcl48(my_id) == 3u));
    res_NotLogicOP_28 = (res_NotLogicOP_28 && ! res_NotLogicOP_29);
    res_AndLogicOP_27 = (res_AndLogicOP_27 && res_NotLogicOP_28);
    bool res_NotLogicOP_30 = true;
    res_NotLogicOP_30 = (res_NotLogicOP_30 && ! (L_P1__GetSubcl76(my_id) < 3u));
    res_AndLogicOP_27 = (res_AndLogicOP_27 && res_NotLogicOP_30);
    
    if(res_AndLogicOP_27){
    xorIndex_res_XorLogicOP_10 = (xorIndex_res_XorLogicOP_10 + 1);
    }
    
    res_XorLogicOP_10 = (res_XorLogicOP_10 && (xorIndex_res_XorLogicOP_10 == 1));
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_XorLogicOP_10);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *47,48,49,50,*  *34,*  il parametro SubClass_C3_parametro_P1 non sia  uguale a  *53,* 2
    //   *104,* o  che  *,*  il timer SubClass_C3_timer_T1 non sia attivo
    //   *104,* o  che  *,*  la variabile SubClass_C3_variabile_V1 non sia  uguale a  *53,* 8
    //   *104,* e  che  *,*  il controllo SubClass_C3_controllo_C4 sia  uguale a  False
    bool res_OrLogicOP_31 = false;
    bool res_OrLogicOP_32 = false;
    bool res_NotLogicOP_33 = true;
    res_NotLogicOP_33 = (res_NotLogicOP_33 && ! (L_P1__GetParamSubcl48(my_id) == 2u));
    res_OrLogicOP_32 = (res_OrLogicOP_32 || res_NotLogicOP_33);
    bool res_NotLogicOP_34 = true;
    res_NotLogicOP_34 = (res_NotLogicOP_34 && ! Timer_Attivo(L_P1__GetSubcl91(my_id)));
    res_OrLogicOP_32 = (res_OrLogicOP_32 || res_NotLogicOP_34);
    
    res_OrLogicOP_31 = (res_OrLogicOP_31 || res_OrLogicOP_32);
    bool res_AndLogicOP_35 = true;
    bool res_NotLogicOP_36 = true;
    res_NotLogicOP_36 = (res_NotLogicOP_36 && ! (L_P1__GetSubcl76(my_id) == 8u));
    res_AndLogicOP_35 = (res_AndLogicOP_35 && res_NotLogicOP_36);
    res_AndLogicOP_35 = (res_AndLogicOP_35 && (L_P1__GetInSubcl43(my_id) == false));
    
    res_OrLogicOP_31 = (res_OrLogicOP_31 || res_AndLogicOP_35);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_31);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
     
    { commento: {63,} commento: {34,}  se lo stato  è  diverso da  commento: {56,}  state1  commento: {106,} commento: {36,} o  se il timer SubClass_C3_timer_T1 non è scaduto commento: {35,} o  se il controllo SubClass_C3_controllo_C4 è  diverso da  True  commento: {37,} o  se la variabile SubClass_C3_variabile_V4 non è  uguale a  True , Solo una delle seguenti { 
     commento: {62,} commento: {36,}  se il timer SubClass_C3_timer_T2 non è disattivo,  commento: {41,}  se MainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C3_lista_L3 esiste e  commento: {105,} è  diverso da AC, commento: {88,} quando  commento: {44,}    MainClass_C1_variabile_V5 del campo  MainClass_C1     è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} e  se la variabile SubClass_C3_variabile_V1 non è  minore di  commento: {55,} 1 commento: {38,} o  se il contatore SubClass_C3_contatore_Co2 non è  uguale a  commento: {53,} 114, Almeno una delle seguenti { 
     commento: {63,} commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  commento: {105,} è  diverso da  commento: {56,}  state1  commento: {37,} o  se la variabile SubClass_C3_variabile_V4 non è  uguale a  False  commento: {35,} o  se il controllo SubClass_C3_controllo_C4 non è  diverso da  True , Solo una delle seguenti { 
     commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L3 esiste e  commento: {105,} è  uguale a  commento: {53,}  state1  commento: {38,} o  se il contatore SubClass_C3_contatore_Co2 è  maggiore di  commento: {54,} 13, Verifica che   commento: {48,49,51,}  commento: {,}  il contatore SubClass_C3_contatore_Co4 non sia  maggiore di  commento: {54,} 1
     commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} e  che  commento: {,}  il timer SubClass_C3_timer_T2 sia disattivo
     commento: {104,} e  che  commento: {38,}  il contatore SubClass_C3_contatore_Co4 non sia  minore di  commento: {55,} 15
    
    
     } Verifica che   commento: {48,49,50,}  commento: {,}  il timer SubClass_C3_timer_T2 sia attivo
     commento: {104,} e  che  commento: {,}  la variabile SubClass_C3_variabile_V4 non sia  diverso da  True 
     commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
    
    
     } Verifica che   commento: {47,48,49,50,51,}  commento: {34,}  il parametro SubClass_C3_parametro_P1 sia  maggiore di  commento: {54,} 7
     commento: {104,} e  che  commento: {,}  la variabile SubClass_C3_variabile_V8 sia  uguale a  True 
     commento: {104,} e  che  commento: {,}  il timer SubClass_C3_timer_T2 sia scaduto
     commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} e  che  commento: {,}  il contatore SubClass_C3_contatore_Co2 sia  diverso da  commento: {56,} 13
     commento: {104,} e  che  commento: {36,}  il timer SubClass_C3_timer_T1 sia disattivo
    
    
     } Verifica che   commento: {50,}  commento: {,}  la variabile SubClass_C3_variabile_V3 non sia  minore di  commento: {55,} 4
    
    
    }
*/
bool L_P1__Macro24(instance_id_t const my_id )
{
bool res_AndLogicOP_0 = true;
    
    //  *63,* *34,*  se lo stato  è  diverso da  *56,*  state1  *106,* *36,* o  se il timer SubClass_C3_timer_T1 non è scaduto *35,* o  se il controllo SubClass_C3_controllo_C4 è  diverso da  True  *37,* o  se la variabile SubClass_C3_variabile_V4 non è  uguale a  True , Solo una delle seguenti { 
    //   *62,* *36,*  se il timer SubClass_C3_timer_T2 non è disattivo,  *41,*  se MainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C3_lista_L3 esiste e  *105,* è  diverso da AC, *88,* quando  *44,*    MainClass_C1_variabile_V5 del campo  MainClass_C1     è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE  *37,* e  se la variabile SubClass_C3_variabile_V1 non è  minore di  *55,* 1 *38,* o  se il contatore SubClass_C3_contatore_Co2 non è  uguale a  *53,* 114, Almeno una delle seguenti { 
    //   *63,* *111,*  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  *105,* è  diverso da  *56,*  state1  *37,* o  se la variabile SubClass_C3_variabile_V4 non è  uguale a  False  *35,* o  se il controllo SubClass_C3_controllo_C4 non è  diverso da  True , Solo una delle seguenti { 
    //   *111,*  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L3 esiste e  *105,* è  uguale a  *53,*  state1  *38,* o  se il contatore SubClass_C3_contatore_Co2 è  maggiore di  *54,* 13, Verifica che   *48,49,51,*  *,*  il contatore SubClass_C3_contatore_Co4 non sia  maggiore di  *54,* 1
    //   *104,* e  che   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* e  che  *,*  il timer SubClass_C3_timer_T2 sia disattivo
    //   *104,* e  che  *38,*  il contatore SubClass_C3_contatore_Co4 non sia  minore di  *55,* 15
    //   } Verifica che   *48,49,50,*  *,*  il timer SubClass_C3_timer_T2 sia attivo
    //   *104,* e  che  *,*  la variabile SubClass_C3_variabile_V4 non sia  diverso da  True 
    //   *104,* e  che   il controllo ConsDef  sia  uguale a FALSE 
    //   } Verifica che   *47,48,49,50,51,*  *34,*  il parametro SubClass_C3_parametro_P1 sia  maggiore di  *54,* 7
    //   *104,* e  che  *,*  la variabile SubClass_C3_variabile_V8 sia  uguale a  True 
    //   *104,* e  che  *,*  il timer SubClass_C3_timer_T2 sia scaduto
    //   *104,* o  che   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* e  che  *,*  il contatore SubClass_C3_contatore_Co2 sia  diverso da  *56,* 13
    //   *104,* e  che  *36,*  il timer SubClass_C3_timer_T1 sia disattivo
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_OrLogicOP_4 = false;
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1_C3_GetState(my_id) == C3_St_state));
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_NotLogicOP_5);
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! Timer_Scaduto(L_P1__GetSubcl91(my_id)));
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_NotLogicOP_6);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_OrLogicOP_4);
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetInSubcl43(my_id) == true));
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_NotLogicOP_7);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetSubcl79(my_id) == true));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_8);
    
    if(res_OrLogicOP_2){
    bool res_XorLogicOP_9 = true;
    int xorIndex_res_XorLogicOP_9 = 0;
    bool res_ImpliesLogicOp_10 = true;
    bool res_OrLogicOP_11 = false;
    bool res_OrLogicOP_12 = false;
    bool res_AndLogicOP_13 = true;
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! Timer_Disattivo(L_P1__GetSubcl92(my_id)));
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_NotLogicOP_14);
    bool res_ForAllPredicateNotEmpty_15 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl46Length(my_id); ++i)
    {
    L_P1__Recor1 it = L_P1__GetRecSubcl46(my_id,i);
    bool res_ImpliesLogicOp_16 = true;
    if((L_P1__GetMainc20(it.mainc33) == false)){
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! (L_P1__GetParamMainc7(it.mainc33) == ac));
    res_ImpliesLogicOp_16 = (res_ImpliesLogicOp_16 && res_NotLogicOP_17);
    res_ForAllPredicateNotEmpty_15 = res_ImpliesLogicOp_16;
    if(!res_ForAllPredicateNotEmpty_15) {break;}
    }
    }
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_ForAllPredicateNotEmpty_15);
    
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_AndLogicOP_13);
    bool res_AndLogicOP_18 = true;
    res_AndLogicOP_18 = (res_AndLogicOP_18 && (L_P1__GetInConsd2(my_id) == false));
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (L_P1__GetSubcl76(my_id) < 1u));
    res_AndLogicOP_18 = (res_AndLogicOP_18 && res_NotLogicOP_19);
    
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_AndLogicOP_18);
    
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_OrLogicOP_12);
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! (Counter_GetValore(L_P1__GetSubcl93(my_id)) == 114u));
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_NotLogicOP_20);
    
    if(res_OrLogicOP_11){
    bool res_OrLogicOP_21 = false;
    bool res_ImpliesLogicOp_22 = true;
    bool res_OrLogicOP_23 = false;
    bool res_OrLogicOP_24 = false;
    bool res_ForAllPredicateNotEmpty_25 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl47Length(my_id); ++i)
    {
    L_P1__Recor2 it = L_P1__GetRecSubcl47(my_id,i);
    bool res_ImpliesLogicOp_26 = true;
    bool res_NotLogicOP_27 = true;
    res_NotLogicOP_27 = (res_NotLogicOP_27 && ! (L_P1_C1_GetState(it.mainc34) == C1_St_state));
    res_ImpliesLogicOp_26 = (res_ImpliesLogicOp_26 && res_NotLogicOP_27);
    res_ForAllPredicateNotEmpty_25 = res_ImpliesLogicOp_26;
    if(!res_ForAllPredicateNotEmpty_25) {break;}
    }
    res_OrLogicOP_24 = (res_OrLogicOP_24 || res_ForAllPredicateNotEmpty_25);
    bool res_NotLogicOP_28 = true;
    res_NotLogicOP_28 = (res_NotLogicOP_28 && ! (L_P1__GetSubcl79(my_id) == false));
    res_OrLogicOP_24 = (res_OrLogicOP_24 || res_NotLogicOP_28);
    
    res_OrLogicOP_23 = (res_OrLogicOP_23 || res_OrLogicOP_24);
    bool res_NotLogicOP_29 = true;
    bool res_NotLogicOP_30 = true;
    res_NotLogicOP_30 = (res_NotLogicOP_30 && ! (L_P1__GetInSubcl43(my_id) == true));
    res_NotLogicOP_29 = (res_NotLogicOP_29 && ! res_NotLogicOP_30);
    res_OrLogicOP_23 = (res_OrLogicOP_23 || res_NotLogicOP_29);
    
    if(res_OrLogicOP_23){
    bool res_ImpliesLogicOp_31 = true;
    bool res_OrLogicOP_32 = false;
    bool res_ForAllPredicateNotEmpty_33 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl46Length(my_id); ++i)
    {
    L_P1__Recor1 it = L_P1__GetRecSubcl46(my_id,i);
    bool res_ImpliesLogicOp_34 = true;
    res_ImpliesLogicOp_34 = (res_ImpliesLogicOp_34 && (L_P1_C1_GetState(it.mainc33) == C1_St_state));
    res_ForAllPredicateNotEmpty_33 = res_ImpliesLogicOp_34;
    if(!res_ForAllPredicateNotEmpty_33) {break;}
    }
    res_OrLogicOP_32 = (res_OrLogicOP_32 || res_ForAllPredicateNotEmpty_33);
    res_OrLogicOP_32 = (res_OrLogicOP_32 || (Counter_GetValore(L_P1__GetSubcl93(my_id)) > 13u));
    
    if(res_OrLogicOP_32){
    bool res_AndLogicOP_35 = true;
    bool res_AndLogicOP_36 = true;
    bool res_AndLogicOP_37 = true;
    bool res_NotLogicOP_38 = true;
    res_NotLogicOP_38 = (res_NotLogicOP_38 && ! (Counter_GetValore(L_P1__GetSubcl94(my_id)) > 1u));
    res_AndLogicOP_37 = (res_AndLogicOP_37 && res_NotLogicOP_38);
    res_AndLogicOP_37 = (res_AndLogicOP_37 && (L_P1__GetInConsd2(my_id) == false));
    
    res_AndLogicOP_36 = (res_AndLogicOP_36 && res_AndLogicOP_37);
    res_AndLogicOP_36 = (res_AndLogicOP_36 && Timer_Disattivo(L_P1__GetSubcl92(my_id)));
    
    res_AndLogicOP_35 = (res_AndLogicOP_35 && res_AndLogicOP_36);
    bool res_NotLogicOP_39 = true;
    res_NotLogicOP_39 = (res_NotLogicOP_39 && ! (Counter_GetValore(L_P1__GetSubcl94(my_id)) < 15u));
    res_AndLogicOP_35 = (res_AndLogicOP_35 && res_NotLogicOP_39);
    
    res_ImpliesLogicOp_31 = (res_ImpliesLogicOp_31 && res_AndLogicOP_35);
    }
    res_ImpliesLogicOp_22 = (res_ImpliesLogicOp_22 && res_ImpliesLogicOp_31);
    }
    res_OrLogicOP_21 = (res_OrLogicOP_21 || res_ImpliesLogicOp_22);
    bool res_AndLogicOP_40 = true;
    bool res_AndLogicOP_41 = true;
    res_AndLogicOP_41 = (res_AndLogicOP_41 && Timer_Attivo(L_P1__GetSubcl92(my_id)));
    bool res_NotLogicOP_42 = true;
    bool res_NotLogicOP_43 = true;
    res_NotLogicOP_43 = (res_NotLogicOP_43 && ! (L_P1__GetSubcl79(my_id) == true));
    res_NotLogicOP_42 = (res_NotLogicOP_42 && ! res_NotLogicOP_43);
    res_AndLogicOP_41 = (res_AndLogicOP_41 && res_NotLogicOP_42);
    
    res_AndLogicOP_40 = (res_AndLogicOP_40 && res_AndLogicOP_41);
    res_AndLogicOP_40 = (res_AndLogicOP_40 && (L_P1__GetInConsd2(my_id) == false));
    
    res_OrLogicOP_21 = (res_OrLogicOP_21 || res_AndLogicOP_40);
    
    res_ImpliesLogicOp_10 = (res_ImpliesLogicOp_10 && res_OrLogicOP_21);
    }
    if(res_ImpliesLogicOp_10){
    xorIndex_res_XorLogicOP_9 = (xorIndex_res_XorLogicOP_9 + 1);
    }
    bool res_OrLogicOP_44 = false;
    bool res_AndLogicOP_45 = true;
    bool res_AndLogicOP_46 = true;
    res_AndLogicOP_46 = (res_AndLogicOP_46 && (L_P1__GetParamSubcl48(my_id) > 7u));
    res_AndLogicOP_46 = (res_AndLogicOP_46 && (L_P1__GetSubcl80(my_id) == true));
    
    res_AndLogicOP_45 = (res_AndLogicOP_45 && res_AndLogicOP_46);
    res_AndLogicOP_45 = (res_AndLogicOP_45 && Timer_Scaduto(L_P1__GetSubcl92(my_id)));
    
    res_OrLogicOP_44 = (res_OrLogicOP_44 || res_AndLogicOP_45);
    bool res_AndLogicOP_47 = true;
    bool res_AndLogicOP_48 = true;
    res_AndLogicOP_48 = (res_AndLogicOP_48 && (L_P1__GetInConsd2(my_id) == false));
    bool res_NotLogicOP_49 = true;
    res_NotLogicOP_49 = (res_NotLogicOP_49 && ! (Counter_GetValore(L_P1__GetSubcl93(my_id)) == 13u));
    res_AndLogicOP_48 = (res_AndLogicOP_48 && res_NotLogicOP_49);
    
    res_AndLogicOP_47 = (res_AndLogicOP_47 && res_AndLogicOP_48);
    res_AndLogicOP_47 = (res_AndLogicOP_47 && Timer_Disattivo(L_P1__GetSubcl91(my_id)));
    
    res_OrLogicOP_44 = (res_OrLogicOP_44 || res_AndLogicOP_47);
    
    if(res_OrLogicOP_44){
    xorIndex_res_XorLogicOP_9 = (xorIndex_res_XorLogicOP_9 + 1);
    }
    
    res_XorLogicOP_9 = (res_XorLogicOP_9 && (xorIndex_res_XorLogicOP_9 == 1));
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_XorLogicOP_9);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *50,*  *,*  la variabile SubClass_C3_variabile_V3 non sia  minore di  *55,* 4
    bool res_NotLogicOP_50 = true;
    res_NotLogicOP_50 = (res_NotLogicOP_50 && ! (L_P1__GetSubcl78(my_id) < 4u));
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_NotLogicOP_50);
    
    
    
    return res_AndLogicOP_0;
}


// Macro valorizzate

/*
    CNL corrispondente:
    
    { commento: {[}
     commento: {46,} assegna alla macro il valore  False  commento: {],}
    }
*/
bool L_P1__Macro18(instance_id_t const my_id , C3_Enumerat2 argom42, C3_Enumerat4 argom43, C3_Enumerat1 argom44, C3_Enumerat4 argom45, C3_Enumerat2 argom46, C3_Enumerat1 argom47)
{
return false;
}

/*
    CNL corrispondente:
    
    { commento: {[} commento: {109,}  se il ripristino della variabile  SubClass_C3_restoreva_RV4 non è  maggiore di  commento: {54,} 7 commento: {109,} o  se il ripristino della variabile  SubClass_C3_restoreva_RV4 non è  minore di  commento: {55,} 1 commento: {34,} e  se lo stato  è  uguale a  commento: {53,}  state1  commento: {106,} , assegna alla macro il valore RossoGialloVerde
    
     commento: {46,} assegna alla macro il valore RossoGialloVerde commento: {],}
    }
*/
C3_Enumerat2 L_P1__Macro19(instance_id_t const my_id , bool argom48, C3_Enumerat3 argom49, C3_Enumerat2 argom50)
{
C3_Enumerat2 res_macro_val;
    
    //  *[* *109,*  se il ripristino della variabile  SubClass_C3_restoreva_RV4 non è  maggiore di  *54,* 7 *109,* o  se il ripristino della variabile  SubClass_C3_restoreva_RV4 non è  minore di  *55,* 1 *34,* e  se lo stato  è  uguale a  *53,*  state1
    bool res_OrLogicOP_0 = false;
    bool res_NotLogicOP_1 = true;
    res_NotLogicOP_1 = (res_NotLogicOP_1 && ! (L_P1__GetSubcl75(my_id) > 7u));
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_1);
    bool res_AndLogicOP_2 = true;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__GetSubcl75(my_id) < 1u));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_3);
    res_AndLogicOP_2 = (res_AndLogicOP_2 && (L_P1_C3_GetState(my_id) == C3_St_state));
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_2);
    
    if(res_OrLogicOP_0){
    
    res_macro_val = rossogiallo4;
    }
    else{
    res_macro_val = rossogiallo4;
    }
    return res_macro_val;
}



