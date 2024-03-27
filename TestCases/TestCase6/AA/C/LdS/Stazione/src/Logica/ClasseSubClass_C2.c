// Codice del modello 'TestCase6', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#include "Logica/ClasseMainClass_C1.h"
#include "Logica/ClasseSubClass_C2.h"
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
    
    Comanda al campo MainClass_C1 di SubClass_C2_lista_L1
     di eseguire  commento: {113,}  MainClass_C1_command_comm6( con argomento_ave5   uguale a Rosso ,argomento_ave9   uguale a True ,argomento_ave8   uguale a c270 )
    }
*/
static inline void L_P1__Effec3(instance_id_t const my_id)
{
    
    //  Comanda al campo MainClass_C1 di SubClass_C2_lista_L1
    //   di eseguire  *113,*  MainClass_C1_command_comm6( con argomento_ave5   uguale a Rosso ,argomento_ave9   uguale a True ,argomento_ave8   uguale a c270 )
    for (index_t i = 0; i < L_P1__GetParamSubcl9Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl9(my_id,i);
    
    L_P1__SetCAEvent(it.mainc45,true);
    L_P1__SetCAArgom(it.mainc45,rosso);
    L_P1__SetCAArgom1(it.mainc45,c270);
    L_P1__SetCAArgom2(it.mainc45,true);
    scheduler_NotifyCommand(L_P1_C1_TO_GLOBAL(it.mainc45));
    }
}



// ********** Definizione metodi **********

// Metodi standard

void L_P1_C2_Init(instance_id_t const my_id)
{
    // init variabili di stato
    L_P1__SetStato3(my_id, C2_St_Stato);
    L_P1__SetSubcl19(my_id, avviox);
    L_P1__SetSubcl21(my_id, ac);
    L_P1__SetSubcl23(my_id, 0);
    L_P1__SetSubcl25(my_id, false);
    L_P1__SetSubcl26(my_id, false);
    L_P1__SetSubcl27(my_id, c120);
    L_P1__SetSubcl28(my_id, c120);
    L_P1__SetSubcl29(my_id, false);
    L_P1__SetSubcl30(my_id, false);
    L_P1__SetSubcl31(my_id, false);
    L_P1__SetSubcl32(my_id, false);
    L_P1__SetSubcl33(my_id, 0);
    L_P1__SetSubcl34(my_id, 0);
    L_P1__SetSubcl35(my_id, ac);
    // init controlli precedenti
    L_P1__SetSubcl16(my_id, false);
    L_P1__SetSubcl18(my_id, true);
    // init Timer e Counter
    Timer_AggmInit(L_P1__GetSubcl36(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl36_ID);
    Timer_Init(L_P1__GetSubcl36(my_id), 1000);
    Timer_AggmInit(L_P1__GetSubcl37(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl37_ID);
    Timer_Init(L_P1__GetSubcl37(my_id), 1000);
    Timer_AggmInit(L_P1__GetSubcl38(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl38_ID);
    Timer_Init(L_P1__GetSubcl38(my_id), 102000);
    Timer_AggmInit(L_P1__GetSubcl39(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl39_ID);
    Timer_Init(L_P1__GetSubcl39(my_id), 102000);
    Timer_AggmInit(L_P1__GetSubcl40(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl40_ID);
    Timer_Init(L_P1__GetSubcl40(my_id), 5000);
    Timer_AggmInit(L_P1__GetSubcl41(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl41_ID);
    Timer_Init(L_P1__GetSubcl41(my_id), 23000);
    Counter_AggmInit(L_P1__GetSubcl42(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl42_ID);
    Counter_Init(L_P1__GetSubcl42(my_id));
    Counter_AggmInit(L_P1__GetSubcl43(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl43_ID);
    Counter_Init(L_P1__GetSubcl43(my_id));
    Counter_AggmInit(L_P1__GetSubcl44(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl44_ID);
    Counter_Init(L_P1__GetSubcl44(my_id));
    Counter_AggmInit(L_P1__GetSubcl45(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl45_ID);
    Counter_Init(L_P1__GetSubcl45(my_id));
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
    L_P1__SetSubcl20(my_id, L_P1__GetSubcl19(my_id));
    L_P1__SetSubcl22(my_id, L_P1__GetSubcl21(my_id));
    L_P1__SetSubcl24(my_id, L_P1__GetSubcl23(my_id));
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
    L_P1__SetOutSubcl(my_id, false);
    L_P1__SetOutSubcl1(my_id, true);
    L_P1__SetOutSubcl2(my_id, spento);
    L_P1__SetOutSubcl3(my_id, true);
}

void L_P1_C2_GUpdatePrev(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C2(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C2(proc_id);
    L_P1__SetSubcl16(my_id, L_P1__GetInSubcl15(my_id));
    L_P1__SetSubcl18(my_id, L_P1__GetInSubcl17(my_id));
    L_P1__SetSubcl20(my_id, L_P1__GetSubcl19(my_id));
    L_P1__SetSubcl22(my_id, L_P1__GetSubcl21(my_id));
    L_P1__SetSubcl24(my_id, L_P1__GetSubcl23(my_id));
}

// ********** Definizione macro **********

// Macro di effetto

/*
    CNL corrispondente:
    
    { commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L1 è  uguale a  commento: {53,}  state1  commento: {38,} e  se il contatore SubClass_C2_contatore_Co5 non è  diverso da  commento: {56,} 13 commento: {36,} o  se il timer SubClass_C2_timer_T3 è attivo,  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V7 il valore c120x commento: {67,}
    
       
     commento: {109,}  se il ripristino della variabile  SubClass_C2_restoreva_RV1 non è  uguale a  True  e  se l'argomento argomento_af6 è  diverso da  True  commento: {39,} ,  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V7 il valore c120x commento: {67,}
    
       
      se il ripristino dello stato  non è  diverso da  commento: {56,}  state1  commento: {107,}, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V7 il valore c120x
    
       
     commento: {110,}  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è attivo commento: {38,} o  se il contatore SubClass_C2_contatore_Co2 è  diverso da  commento: {56,} 14 commento: {34,} e  se il parametro SubClass_C2_parametro_P5 non è  diverso da c120x, commento: {72,}Azzera il contatore SubClass_C2_contatore_Co5
    
     ,altrimenti   commento: {67,} Assegna alla variabile SubClass_C2_variabile_V7 il valore c120x commento: {67,}
    
    
    
    }
*/
void L_P1__Macro7(instance_id_t const my_id , bool argom24, C2_Enumerat4 argom25, bool argom26, C2_Enumerat4 argom27)
{
//  *111,*  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L1 è  uguale a  *53,*  state1  *38,* e  se il contatore SubClass_C2_contatore_Co5 non è  diverso da  *56,* 13 *36,* o  se il timer SubClass_C2_timer_T3 è attivo,  *67,* Assegna alla variabile SubClass_C2_variabile_V7 il valore c120x
    bool res_OrLogicOP_0 = false;
    bool res_AndLogicOP_1 = true;
    bool res_ForAllPredicate_2 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl9Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl9(my_id,i);
    bool res_ImpliesLogicOp_3 = true;
    res_ImpliesLogicOp_3 = (res_ImpliesLogicOp_3 && (L_P1_C1_GetState(it.mainc45) == C1_St_state));
    res_ForAllPredicate_2 = res_ImpliesLogicOp_3;
    if(!res_ForAllPredicate_2) {break;}
    }
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_ForAllPredicate_2);
    bool res_NotLogicOP_4 = true;
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (Counter_GetValore(L_P1__GetSubcl45(my_id)) == 13u));
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! res_NotLogicOP_5);
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_4);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_1);
    res_OrLogicOP_0 = (res_OrLogicOP_0 || Timer_Attivo(L_P1__GetSubcl40(my_id)));
    
    if(res_OrLogicOP_0){
    
    L_P1__SetSubcl35(my_id,c120x);
    }
    //  *67,*
    //   
    // *109,*  se il ripristino della variabile  SubClass_C2_restoreva_RV1 non è  uguale a  True  e  se l'argomento argomento_af6 è  diverso da  True  *39,* ,  *67,* Assegna alla variabile SubClass_C2_variabile_V7 il valore c120x
    bool res_AndLogicOP_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetSubcl26(my_id) == true));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_7);
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (argom26 == true));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_8);
    
    if(res_AndLogicOP_6){
    
    L_P1__SetSubcl35(my_id,c120x);
    }
    //  *67,*
    //   
    //  se il ripristino dello stato  non è  diverso da  *56,*  state1  *107,*, *67,* Assegna alla variabile SubClass_C2_variabile_V7 il valore c120x
    bool res_NotLogicOP_9 = true;
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__GetStato3(my_id) == C2_St_state));
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! res_NotLogicOP_10);
    if(res_NotLogicOP_9){
    
    L_P1__SetSubcl35(my_id,c120x);
    }
    //  *110,*  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è attivo *38,* o  se il contatore SubClass_C2_contatore_Co2 è  diverso da  *56,* 14 *34,* e  se il parametro SubClass_C2_parametro_P5 non è  diverso da c120x, *72,*Azzera il contatore SubClass_C2_contatore_Co5
    // ,altrimenti   *67,* Assegna alla variabile SubClass_C2_variabile_V7 il valore c120x
    bool res_OrLogicOP_11 = false;
    res_OrLogicOP_11 = (res_OrLogicOP_11 || Timer_Attivo(L_P1__GetSubcl37(my_id)));
    bool res_AndLogicOP_12 = true;
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (Counter_GetValore(L_P1__GetSubcl43(my_id)) == 14u));
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_NotLogicOP_13);
    bool res_NotLogicOP_14 = true;
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (L_P1__GetParamSubcl14(my_id) == c120x));
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! res_NotLogicOP_15);
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_NotLogicOP_14);
    
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_AndLogicOP_12);
    
    if(res_OrLogicOP_11){
    
    Counter_Res(L_P1__GetSubcl45(my_id));
    }else{
    
    L_P1__SetSubcl35(my_id,c120x);
    }
}

/*
    CNL corrispondente:
    
    { commento: {43,}  se MainClass_C1_timer_T9 del campo  MainClass_C1 di SubClass_C2_lista_L8 è disattivo commento: {36,} e  se il timer SubClass_C2_timer_T3 è disattivo commento: {36,} e  se il timer SubClass_C2_timer_T3 è attivo commento: {37,} o  se la variabile SubClass_C2_variabile_V7 non è  uguale a c120x commento: {36,} o  se il timer SubClass_C2_timer_T3 non è disattivo commento: {37,} o  se la variabile SubClass_C2_variabile_V7 non è  uguale a c120x, commento: {72,}Azzera il contatore SubClass_C2_contatore_Co2
    
     ,altrimenti  commento: {66,} Assegna al comando SubClass_C2_comando_C8 il valore  False 
    
    
     commento: {34,}  se il parametro SubClass_C2_parametro_P4 non è  uguale a c120x commento: {34,} o  se il parametro SubClass_C2_parametro_P5 non è  uguale a c120x commento: {37,} e  se la variabile SubClass_C2_variabile_V7 è  uguale a c120x commento: {36,} o  se il timer SubClass_C2_timer_T4 non è scaduto, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V7 il valore c120x
    
     ,altrimenti   Applica gli effetti
           della macro SubClass_C2_macroef_M1( con argomento_af6   uguale a True ,argomento_af2   uguale a True ,argomento_af7   uguale a AC ,argomento_af4   uguale a c120x ) commento: {73,}
    
    
     commento: {45,}  se  MainClass_C1_contatore_Co9 del campo  MainClass_C1 di SubClass_C2_lista_L1 esiste e  commento: {105,} è  uguale a  commento: {53,} 11 commento: {34,} o  se il parametro SubClass_C2_parametro_P4 non è  diverso da c120x, commento: {72,}Azzera il contatore SubClass_C2_contatore_Co3
    
       
    
    }
*/
void L_P1__Macro8(instance_id_t const my_id )
{
//  *43,*  se MainClass_C1_timer_T9 del campo  MainClass_C1 di SubClass_C2_lista_L8 è disattivo *36,* e  se il timer SubClass_C2_timer_T3 è disattivo *36,* e  se il timer SubClass_C2_timer_T3 è attivo *37,* o  se la variabile SubClass_C2_variabile_V7 non è  uguale a c120x *36,* o  se il timer SubClass_C2_timer_T3 non è disattivo *37,* o  se la variabile SubClass_C2_variabile_V7 non è  uguale a c120x, *72,*Azzera il contatore SubClass_C2_contatore_Co2
    // ,altrimenti  *66,* Assegna al comando SubClass_C2_comando_C8 il valore  False
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_OrLogicOP_2 = false;
    bool res_AndLogicOP_3 = true;
    bool res_AndLogicOP_4 = true;
    bool res_ForAllPredicate_5 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl12Length(my_id); ++i)
    {
    L_P1__Recor1 it = L_P1__GetRecSubcl12(my_id,i);
    bool res_ImpliesLogicOp_6 = true;
    res_ImpliesLogicOp_6 = (res_ImpliesLogicOp_6 && Timer_Disattivo(L_P1__GetMainc42(it.mainc46)));
    res_ForAllPredicate_5 = res_ImpliesLogicOp_6;
    if(!res_ForAllPredicate_5) {break;}
    }
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_ForAllPredicate_5);
    res_AndLogicOP_4 = (res_AndLogicOP_4 && Timer_Disattivo(L_P1__GetSubcl40(my_id)));
    
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_AndLogicOP_4);
    res_AndLogicOP_3 = (res_AndLogicOP_3 && Timer_Attivo(L_P1__GetSubcl40(my_id)));
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_3);
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetSubcl35(my_id) == c120x));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_7);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_OrLogicOP_2);
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! Timer_Disattivo(L_P1__GetSubcl40(my_id)));
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_NotLogicOP_8);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetSubcl35(my_id) == c120x));
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_9);
    
    if(res_OrLogicOP_0){
    
    Counter_Res(L_P1__GetSubcl43(my_id));
    }else{
    
    L_P1__SetOutSubcl3(my_id,false);
    }
    //  *34,*  se il parametro SubClass_C2_parametro_P4 non è  uguale a c120x *34,* o  se il parametro SubClass_C2_parametro_P5 non è  uguale a c120x *37,* e  se la variabile SubClass_C2_variabile_V7 è  uguale a c120x *36,* o  se il timer SubClass_C2_timer_T4 non è scaduto, *67,* Assegna alla variabile SubClass_C2_variabile_V7 il valore c120x
    // ,altrimenti   Applica gli effetti
    //       della macro SubClass_C2_macroef_M1( con argomento_af6   uguale a True ,argomento_af2   uguale a True ,argomento_af7   uguale a AC ,argomento_af4   uguale a c120x )
    bool res_OrLogicOP_10 = false;
    bool res_OrLogicOP_11 = false;
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (L_P1__GetParamSubcl13(my_id) == c120x));
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_NotLogicOP_12);
    bool res_AndLogicOP_13 = true;
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1__GetParamSubcl14(my_id) == c120x));
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_NotLogicOP_14);
    res_AndLogicOP_13 = (res_AndLogicOP_13 && (L_P1__GetSubcl35(my_id) == c120x));
    
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_AndLogicOP_13);
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_OrLogicOP_11);
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! Timer_Scaduto(L_P1__GetSubcl41(my_id)));
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_NotLogicOP_15);
    
    if(res_OrLogicOP_10){
    
    L_P1__SetSubcl35(my_id,c120x);
    }else{
    
    L_P1__Macro7(my_id,true,c120x,true,ac);
    }
    //  *73,*
    // *45,*  se  MainClass_C1_contatore_Co9 del campo  MainClass_C1 di SubClass_C2_lista_L1 esiste e  *105,* è  uguale a  *53,* 11 *34,* o  se il parametro SubClass_C2_parametro_P4 non è  diverso da c120x, *72,*Azzera il contatore SubClass_C2_contatore_Co3
    bool res_OrLogicOP_16 = false;
    bool res_ForAllPredicateNotEmpty_17 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl9Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl9(my_id,i);
    bool res_ImpliesLogicOp_18 = true;
    res_ImpliesLogicOp_18 = (res_ImpliesLogicOp_18 && (Counter_GetValore(L_P1__GetMainc44(it.mainc45)) == 11u));
    res_ForAllPredicateNotEmpty_17 = res_ImpliesLogicOp_18;
    if(!res_ForAllPredicateNotEmpty_17) {break;}
    }
    res_OrLogicOP_16 = (res_OrLogicOP_16 || res_ForAllPredicateNotEmpty_17);
    bool res_NotLogicOP_19 = true;
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! (L_P1__GetParamSubcl13(my_id) == c120x));
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! res_NotLogicOP_20);
    res_OrLogicOP_16 = (res_OrLogicOP_16 || res_NotLogicOP_19);
    
    if(res_OrLogicOP_16){
    
    Counter_Res(L_P1__GetSubcl44(my_id));
    }
}


// Macro di verifica

/*
    CNL corrispondente:
    
    { commento: {36,}  se il timer SubClass_C2_timer_T4 non è scaduto, Verifica che   commento: {47,48,49,50,51,}  commento: {34,}  il parametro SubClass_C2_parametro_P5 sia  uguale a c120x
     commento: {104,} e  che  commento: {,}  il controllo SubClass_C2_controllo_C5 sia  uguale a  False 
     commento: {104,} o  che  commento: {,}  il timer SubClass_C2_timer_T4 sia disattivo
     commento: {104,} e  che  commento: {,}  il contatore SubClass_C2_contatore_Co2 non sia  diverso da  commento: {56,} 11024
     commento: {104,} o  che  commento: {,}  la variabile SubClass_C2_variabile_V7 sia  diverso da c120x
    
    
    }
*/
bool L_P1__Macro12(instance_id_t const my_id , C2_Enumerat4 argom37, bool argom38, C2_Enumerat1 argom39, bool argom40)
{
bool res_AndLogicOP_0 = true;
    
    //  *36,*  se il timer SubClass_C2_timer_T4 non è scaduto, Verifica che   *47,48,49,50,51,*  *34,*  il parametro SubClass_C2_parametro_P5 sia  uguale a c120x
    //   *104,* e  che  *,*  il controllo SubClass_C2_controllo_C5 sia  uguale a  False 
    //   *104,* o  che  *,*  il timer SubClass_C2_timer_T4 sia disattivo
    //   *104,* e  che  *,*  il contatore SubClass_C2_contatore_Co2 non sia  diverso da  *56,* 11024
    //   *104,* o  che  *,*  la variabile SubClass_C2_variabile_V7 sia  diverso da c120x
    bool res_ImpliesLogicOp_1 = true;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! Timer_Scaduto(L_P1__GetSubcl41(my_id)));
    if(res_NotLogicOP_2){
    bool res_OrLogicOP_3 = false;
    bool res_OrLogicOP_4 = false;
    bool res_AndLogicOP_5 = true;
    res_AndLogicOP_5 = (res_AndLogicOP_5 && (L_P1__GetParamSubcl14(my_id) == c120x));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && (L_P1__GetInSubcl7(my_id) == false));
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_AndLogicOP_5);
    bool res_AndLogicOP_6 = true;
    res_AndLogicOP_6 = (res_AndLogicOP_6 && Timer_Disattivo(L_P1__GetSubcl41(my_id)));
    bool res_NotLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (Counter_GetValore(L_P1__GetSubcl43(my_id)) == 11024u));
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! res_NotLogicOP_8);
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_7);
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_AndLogicOP_6);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_OrLogicOP_4);
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetSubcl35(my_id) == c120x));
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_NotLogicOP_9);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_OrLogicOP_3);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
    
    { commento: {37,}  se la variabile SubClass_C2_variabile_V7 non è  diverso da c120x commento: {35,} o  se il controllo SubClass_C2_controllo_C9 è  uguale a c120x commento: {38,} o  se il contatore SubClass_C2_contatore_Co2 è  minore di  commento: {55,} 142 commento: {37,} e  se la variabile SubClass_C2_variabile_V7 non è  diverso da c120x commento: {37,} e  se la variabile SubClass_C2_variabile_V7 è  diverso da c120x, Verifica che   commento: {48,50,51,}  commento: {,}  il contatore SubClass_C2_contatore_Co3 sia  minore di  commento: {55,} 15
     commento: {104,} e  che  commento: {,}  il controllo SubClass_C2_controllo_C5 sia  diverso da  False 
     commento: {104,} e  che  commento: {,}  la variabile SubClass_C2_variabile_V7 non sia  diverso da c120x
     commento: {104,} o  che  commento: {37,}  la variabile SubClass_C2_variabile_V7 sia  diverso da c120x
     commento: {104,} o  che  commento: {37,}  la variabile SubClass_C2_variabile_V7 non sia  uguale a c120x
    
    
    }
*/
bool L_P1__Macro13(instance_id_t const my_id , C2_Enumerat4 argom41, bool argom42, C2_Enumerat4 argom43, C2_Enumerat2 argom44, C2_Enumerat4 argom45, bool argom46, C2_Enumerat4 argom47)
{
bool res_AndLogicOP_0 = true;
    
    //  *37,*  se la variabile SubClass_C2_variabile_V7 non è  diverso da c120x *35,* o  se il controllo SubClass_C2_controllo_C9 è  uguale a c120x *38,* o  se il contatore SubClass_C2_contatore_Co2 è  minore di  *55,* 142 *37,* e  se la variabile SubClass_C2_variabile_V7 non è  diverso da c120x *37,* e  se la variabile SubClass_C2_variabile_V7 è  diverso da c120x, Verifica che   *48,50,51,*  *,*  il contatore SubClass_C2_contatore_Co3 sia  minore di  *55,* 15
    //   *104,* e  che  *,*  il controllo SubClass_C2_controllo_C5 sia  diverso da  False 
    //   *104,* e  che  *,*  la variabile SubClass_C2_variabile_V7 non sia  diverso da c120x
    //   *104,* o  che  *37,*  la variabile SubClass_C2_variabile_V7 sia  diverso da c120x
    //   *104,* o  che  *37,*  la variabile SubClass_C2_variabile_V7 non sia  uguale a c120x
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_NotLogicOP_4 = true;
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetSubcl35(my_id) == c120x));
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! res_NotLogicOP_5);
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_NotLogicOP_4);
    res_OrLogicOP_3 = (res_OrLogicOP_3 || (L_P1__GetInSubcl8(my_id) == c120x));
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    bool res_AndLogicOP_6 = true;
    bool res_AndLogicOP_7 = true;
    res_AndLogicOP_7 = (res_AndLogicOP_7 && (Counter_GetValore(L_P1__GetSubcl43(my_id)) < 142u));
    bool res_NotLogicOP_8 = true;
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetSubcl35(my_id) == c120x));
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! res_NotLogicOP_9);
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_8);
    
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_AndLogicOP_7);
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__GetSubcl35(my_id) == c120x));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_10);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_6);
    
    if(res_OrLogicOP_2){
    bool res_OrLogicOP_11 = false;
    bool res_OrLogicOP_12 = false;
    bool res_AndLogicOP_13 = true;
    bool res_AndLogicOP_14 = true;
    res_AndLogicOP_14 = (res_AndLogicOP_14 && (Counter_GetValore(L_P1__GetSubcl44(my_id)) < 15u));
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (L_P1__GetInSubcl7(my_id) == false));
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_NotLogicOP_15);
    
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_AndLogicOP_14);
    bool res_NotLogicOP_16 = true;
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! (L_P1__GetSubcl35(my_id) == c120x));
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! res_NotLogicOP_17);
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_NotLogicOP_16);
    
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_AndLogicOP_13);
    bool res_NotLogicOP_18 = true;
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! (L_P1__GetSubcl35(my_id) == c120x));
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_NotLogicOP_18);
    
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_OrLogicOP_12);
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (L_P1__GetSubcl35(my_id) == c120x));
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_NotLogicOP_19);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_OrLogicOP_11);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
     
    { commento: {63,} commento: {109,}  se il ripristino della variabile  SubClass_C2_restoreva_RV2 è  diverso da c270x commento: {37,} e  se la variabile SubClass_C2_variabile_V7 non è  diverso da c120x commento: {34,} e  se il parametro SubClass_C2_parametro_P5 è  diverso da c120x, Solo una delle seguenti { 
     commento: {37,}  se la variabile SubClass_C2_variabile_V7 è  uguale a c120x commento: {36,} o  se il timer SubClass_C2_timer_T3 non è scaduto commento: {38,} o  se il contatore SubClass_C2_contatore_Co2 è  minore di  commento: {55,} 1124, Verifica che   commento: {48,49,}   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} o  che  commento: {,}  il timer SubClass_C2_timer_T4 non sia attivo
     commento: {104,} e  che  commento: {36,}  il timer SubClass_C2_timer_T3 non sia disattivo
    
    
     } Verifica che   commento: {49,}  commento: {,}  il timer SubClass_C2_timer_T3 sia scaduto
    
    
    }
*/
bool L_P1__Macro14(instance_id_t const my_id )
{
bool res_AndLogicOP_0 = true;
    
    //  *63,* *109,*  se il ripristino della variabile  SubClass_C2_restoreva_RV2 è  diverso da c270x *37,* e  se la variabile SubClass_C2_variabile_V7 non è  diverso da c120x *34,* e  se il parametro SubClass_C2_parametro_P5 è  diverso da c120x, Solo una delle seguenti { 
    //   *37,*  se la variabile SubClass_C2_variabile_V7 è  uguale a c120x *36,* o  se il timer SubClass_C2_timer_T3 non è scaduto *38,* o  se il contatore SubClass_C2_contatore_Co2 è  minore di  *55,* 1124, Verifica che   *48,49,*   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* o  che  *,*  il timer SubClass_C2_timer_T4 non sia attivo
    //   *104,* e  che  *36,*  il timer SubClass_C2_timer_T3 non sia disattivo
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_AndLogicOP_2 = true;
    bool res_AndLogicOP_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetSubcl28(my_id) == c270x));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_4);
    bool res_NotLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetSubcl35(my_id) == c120x));
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! res_NotLogicOP_6);
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_5);
    
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_AndLogicOP_3);
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetParamSubcl14(my_id) == c120x));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_7);
    
    if(res_AndLogicOP_2){
    bool res_ImpliesLogicOp_8 = true;
    bool res_OrLogicOP_9 = false;
    bool res_OrLogicOP_10 = false;
    res_OrLogicOP_10 = (res_OrLogicOP_10 || (L_P1__GetSubcl35(my_id) == c120x));
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! Timer_Scaduto(L_P1__GetSubcl40(my_id)));
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_NotLogicOP_11);
    
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_OrLogicOP_10);
    res_OrLogicOP_9 = (res_OrLogicOP_9 || (Counter_GetValore(L_P1__GetSubcl43(my_id)) < 1124u));
    
    if(res_OrLogicOP_9){
    bool res_OrLogicOP_12 = false;
    res_OrLogicOP_12 = (res_OrLogicOP_12 || (L_P1__GetInConsd1(my_id) == false));
    bool res_AndLogicOP_13 = true;
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! Timer_Attivo(L_P1__GetSubcl41(my_id)));
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_NotLogicOP_14);
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! Timer_Disattivo(L_P1__GetSubcl40(my_id)));
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_NotLogicOP_15);
    
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_AndLogicOP_13);
    
    res_ImpliesLogicOp_8 = (res_ImpliesLogicOp_8 && res_OrLogicOP_12);
    }
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_ImpliesLogicOp_8);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *49,*  *,*  il timer SubClass_C2_timer_T3 sia scaduto
    res_AndLogicOP_0 = (res_AndLogicOP_0 && Timer_Scaduto(L_P1__GetSubcl40(my_id)));
    
    
    
    return res_AndLogicOP_0;
}


// Macro valorizzate

/*
    CNL corrispondente:
    
    { commento: {[}
     commento: {46,} assegna alla macro il valore spento commento: {],}
    }
*/
C2_Enumerat2 L_P1__Macro9(instance_id_t const my_id , C2_Enumerat1 argom28, C2_Enumerat1 argom29)
{
return spento;
}

/*
    CNL corrispondente:
    
    { commento: {[}  se l'argomento argomento_a4 non  è  uguale a  True  commento: {39,} ,  commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  commento: {105,} è  uguale a  commento: {53,}  state1 , commento: {88,} quando  commento: {43,}   MainClass_C1_timer_T9 del campo  MainClass_C1     è attivo commento: {43,} o  se MainClass_C1_timer_T2 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  commento: {105,} è disattivo commento: {34,} e  se lo stato  è  uguale a  commento: {53,}  state1  commento: {106,} commento: {36,} e  se il timer SubClass_C2_timer_T4 non è attivo , assegna alla macro il valore  True 
    
     commento: {46,} assegna alla macro il valore  False  commento: {],}
    }
*/
bool L_P1__Macro10(instance_id_t const my_id , C2_Enumerat1 argom30, C2_Enumerat3 argom31, bool argom32)
{
bool res_macro_val;
    
    //  *[*  se l'argomento argomento_a4 non  è  uguale a  True  *39,* ,  *111,*  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  *105,* è  uguale a  *53,*  state1 , *88,* quando  *43,*   MainClass_C1_timer_T9 del campo  MainClass_C1     è attivo *43,* o  se MainClass_C1_timer_T2 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  *105,* è disattivo *34,* e  se lo stato  è  uguale a  *53,*  state1  *106,* *36,* e  se il timer SubClass_C2_timer_T4 non è attivo
    bool res_OrLogicOP_0 = false;
    bool res_AndLogicOP_1 = true;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (argom32 == true));
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_2);
    bool res_ForAllPredicateNotEmpty_3 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl11Length(my_id); ++i)
    {
    L_P1__Recor1 it = L_P1__GetRecSubcl11(my_id,i);
    bool res_ImpliesLogicOp_4 = true;
    if(Timer_Attivo(L_P1__GetMainc42(it.mainc46))){
    res_ImpliesLogicOp_4 = (res_ImpliesLogicOp_4 && (L_P1_C1_GetState(it.mainc46) == C1_St_state));
    res_ForAllPredicateNotEmpty_3 = res_ImpliesLogicOp_4;
    if(!res_ForAllPredicateNotEmpty_3) {break;}
    }
    }
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_ForAllPredicateNotEmpty_3);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_1);
    bool res_AndLogicOP_5 = true;
    bool res_AndLogicOP_6 = true;
    bool res_ForAllPredicateNotEmpty_7 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl12Length(my_id); ++i)
    {
    L_P1__Recor1 it = L_P1__GetRecSubcl12(my_id,i);
    bool res_ImpliesLogicOp_8 = true;
    res_ImpliesLogicOp_8 = (res_ImpliesLogicOp_8 && Timer_Disattivo(L_P1__GetMainc40(it.mainc46)));
    res_ForAllPredicateNotEmpty_7 = res_ImpliesLogicOp_8;
    if(!res_ForAllPredicateNotEmpty_7) {break;}
    }
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_ForAllPredicateNotEmpty_7);
    res_AndLogicOP_6 = (res_AndLogicOP_6 && (L_P1_C2_GetState(my_id) == C2_St_state));
    
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_AndLogicOP_6);
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! Timer_Attivo(L_P1__GetSubcl41(my_id)));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_9);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_5);
    
    if(res_OrLogicOP_0){
    
    res_macro_val = true;
    }
    else{
    res_macro_val = false;
    }
    return res_macro_val;
}

/*
    CNL corrispondente:
    
    { commento: {[}
     commento: {46,} assegna alla macro il valore  True  commento: {],}
    }
*/
bool L_P1__Macro11(instance_id_t const my_id , C2_Enumerat2 argom33, C2_Enumerat3 argom34, C2_Enumerat1 argom35, C2_Enumerat1 argom36)
{
return true;
}



