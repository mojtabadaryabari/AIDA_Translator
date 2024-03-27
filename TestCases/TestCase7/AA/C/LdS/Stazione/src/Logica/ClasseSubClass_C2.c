// Codice del modello 'TestCase7', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#include "Logica/ClasseMainClass_C1.h"
#include "Logica/ClasseSubClass_C2.h"
#include "Logica/ClasseSubClass_C2_priv.h"
#include "config.h"
#include "scheduler.h"


// ********** Gestione comandi automatici **********

static size_t L_P1_C2_NumAutoCmds(instance_id_t const my_id)
{
    size_t n = 0u;
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
    if (L_P1__GetInEvent6(my_id)) {
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
    
     commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  commento: {105,} è  uguale a  commento: {53,}  state1 , commento: {72,}Azzera il contatore SubClass_C2_contatore_Co7
    
       
     commento: {109,}  se il ripristino della variabile  SubClass_C2_restoreva_RV3 non è  uguale a Verde e  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} o  se il contatore SubClass_C2_contatore_Co6 non è  minore di  commento: {55,} 1253, commento: {66,} Assegna al comando SubClass_C2_comando_C9 il valore  True 
    
     ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V9 il valore GialloaVerdea
    
    
    
    }
*/
static inline void L_P1__Effec3(instance_id_t const my_id)
{
    
    //  *111,*  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  *105,* è  uguale a  *53,*  state1 , *72,*Azzera il contatore SubClass_C2_contatore_Co7
    bool res_ForAllPredicateNotEmpty_0 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl9Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl9(my_id,i);
    bool res_ImpliesLogicOp_1 = true;
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && (L_P1_C1_GetState(it.mainc45) == C1_St_state));
    res_ForAllPredicateNotEmpty_0 = res_ImpliesLogicOp_1;
    if(!res_ForAllPredicateNotEmpty_0) {break;}
    }
    if(res_ForAllPredicateNotEmpty_0){
    
    Counter_Res(L_P1__GetSubcl52(my_id));
    }
    
    //  *109,*  se il ripristino della variabile  SubClass_C2_restoreva_RV3 non è  uguale a Verde e  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  *38,* o  se il contatore SubClass_C2_contatore_Co6 non è  minore di  *55,* 1253, *66,* Assegna al comando SubClass_C2_comando_C9 il valore  True 
    //   ,altrimenti  *67,* Assegna alla variabile SubClass_C2_variabile_V9 il valore GialloaVerdea
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_AndLogicOP_4 = true;
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetSubcl35(my_id) == verde));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_5);
    res_AndLogicOP_4 = (res_AndLogicOP_4 && (L_P1__GetInConsd1(my_id) == false));
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_AndLogicOP_4);
    res_OrLogicOP_3 = (res_OrLogicOP_3 || (L_P1__GetInConsd1(my_id) == false));
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (Counter_GetValore(L_P1__GetSubcl51(my_id)) < 1253u));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_6);
    
    if(res_OrLogicOP_2){
    
    L_P1__SetOutSubcl1(my_id,true);
    }else{
    
    L_P1__SetSubcl44(my_id,gialloaverd);
    }
}



// ********** Definizione metodi **********

// Metodi standard

void L_P1_C2_Init(instance_id_t const my_id)
{
    // init variabili di stato
    L_P1__SetStato3(my_id, C2_St_Stato);
    L_P1__SetSubcl20(my_id, rossogiallo3);
    L_P1__SetSubcl22(my_id, false);
    L_P1__SetSubcl24(my_id, false);
    L_P1__SetSubcl26(my_id, false);
    L_P1__SetSubcl28(my_id, gialloverde);
    L_P1__SetSubcl30(my_id, c120);
    L_P1__SetSubcl31(my_id, c120);
    L_P1__SetSubcl32(my_id, false);
    L_P1__SetSubcl33(my_id, false);
    L_P1__SetSubcl34(my_id, c120);
    L_P1__SetSubcl35(my_id, c120);
    L_P1__SetSubcl36(my_id, c120);
    L_P1__SetSubcl37(my_id, c120);
    L_P1__SetSubcl38(my_id, false);
    L_P1__SetSubcl39(my_id, false);
    L_P1__SetSubcl40(my_id, false);
    L_P1__SetSubcl41(my_id, 0);
    L_P1__SetSubcl42(my_id, 0);
    L_P1__SetSubcl43(my_id, 0);
    L_P1__SetSubcl44(my_id, gialloverde);
    // init controlli precedenti
    L_P1__SetSubcl15(my_id, false);
    L_P1__SetSubcl17(my_id, false);
    L_P1__SetSubcl19(my_id, rossogiallo4);
    // init Timer e Counter
    Timer_AggmInit(L_P1__GetSubcl45(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl45_ID);
    Timer_Init(L_P1__GetSubcl45(my_id), 4041000);
    Timer_AggmInit(L_P1__GetSubcl46(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl46_ID);
    Timer_Init(L_P1__GetSubcl46(my_id), 4041000);
    Timer_AggmInit(L_P1__GetSubcl47(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl47_ID);
    Timer_Init(L_P1__GetSubcl47(my_id), 4041000);
    Timer_AggmInit(L_P1__GetSubcl48(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl48_ID);
    Timer_Init(L_P1__GetSubcl48(my_id), 253000);
    Timer_AggmInit(L_P1__GetSubcl49(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl49_ID);
    Timer_Init(L_P1__GetSubcl49(my_id), 42000);
    Counter_AggmInit(L_P1__GetSubcl50(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl50_ID);
    Counter_Init(L_P1__GetSubcl50(my_id));
    Counter_AggmInit(L_P1__GetSubcl51(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl51_ID);
    Counter_Init(L_P1__GetSubcl51(my_id));
    Counter_AggmInit(L_P1__GetSubcl52(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl52_ID);
    Counter_Init(L_P1__GetSubcl52(my_id));
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
    L_P1__SetSubcl21(my_id, L_P1__GetSubcl20(my_id));
    L_P1__SetSubcl23(my_id, L_P1__GetSubcl22(my_id));
    L_P1__SetSubcl25(my_id, L_P1__GetSubcl24(my_id));
    L_P1__SetSubcl27(my_id, L_P1__GetSubcl26(my_id));
    L_P1__SetSubcl29(my_id, L_P1__GetSubcl28(my_id));
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
    Timer_Exec(L_P1__GetSubcl45(my_id));
    Timer_Exec(L_P1__GetSubcl46(my_id));
    Timer_Exec(L_P1__GetSubcl47(my_id));
    Timer_Exec(L_P1__GetSubcl48(my_id));
    Timer_Exec(L_P1__GetSubcl49(my_id));
}

void L_P1_C2_GSetSafe(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C2(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C2(proc_id);
    L_P1__SetOutSubcl(my_id, false);
    L_P1__SetOutSubcl1(my_id, true);
}

void L_P1_C2_GUpdatePrev(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C2(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C2(proc_id);
    L_P1__SetSubcl15(my_id, L_P1__GetInSubcl14(my_id));
    L_P1__SetSubcl17(my_id, L_P1__GetInSubcl16(my_id));
    L_P1__SetSubcl19(my_id, L_P1__GetInSubcl18(my_id));
    L_P1__SetSubcl21(my_id, L_P1__GetSubcl20(my_id));
    L_P1__SetSubcl23(my_id, L_P1__GetSubcl22(my_id));
    L_P1__SetSubcl25(my_id, L_P1__GetSubcl24(my_id));
    L_P1__SetSubcl27(my_id, L_P1__GetSubcl26(my_id));
    L_P1__SetSubcl29(my_id, L_P1__GetSubcl28(my_id));
}

// ********** Definizione macro **********

// Macro di effetto

/*
    CNL corrispondente:
    
    {  se la macro  SubClass_C2_macrova_M6 ( con argomento_a10   uguale a GialloVerde ,argomento_a3   uguale a Verde ,argomento_a9   uguale a c120  e argomento_a6   uguale a GialloVerde )   è  uguale a  True  commento: {40,} ,  Applica gli effetti
           della macro SubClass_C2_macroef_M5  commento: {73,}
    
     ,altrimenti  commento: {70,}Incrementa il contatore SubClass_C2_contatore_Co6
    
    
     commento: {37,}  se la variabile SubClass_C2_variabile_V4 è  maggiore di  commento: {54,} 10 commento: {36,} o  se il timer SubClass_C2_timer_T2 è attivo commento: {34,} e  se il parametro SubClass_C2_parametro_P1 non è  uguale a  commento: {53,} 1 commento: {36,} o  se il timer SubClass_C2_timer_T4 è disattivo commento: {38,} o  se il contatore SubClass_C2_contatore_Co6 non è  minore di  commento: {55,} 13, commento: {71,}Decrementa il contatore SubClass_C2_contatore_Co2
    
       
     commento: {42,}  se  MainClass_C1_controllo_C8 del campo  MainClass_C1 di SubClass_C2_lista_L10 è  uguale a RossoGialloGiallo commento: {36,} e  se il timer SubClass_C2_timer_T10 non è scaduto commento: {36,} o  se il timer SubClass_C2_timer_T2 è attivo, commento: {66,} Assegna al comando SubClass_C2_comando_C7 il valore  False 
    
     ,altrimenti   Applica gli effetti
           della macro SubClass_C2_macroef_M5  commento: {73,}
    
    
     commento: {37,}  se la variabile SubClass_C2_variabile_V4 è  maggiore di  commento: {54,} 7 commento: {36,} o  se il timer SubClass_C2_timer_T2 non è attivo commento: {34,} o  se il parametro SubClass_C2_parametro_P6 è  uguale a  commento: {53,} 1, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V5 il valore 8
    
     ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V4 il valore 6
    
    
     commento: {110,}  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è scaduto commento: {37,} o  se la variabile SubClass_C2_variabile_V5 non è  uguale a  commento: {53,} 10 o  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} o  se il parametro SubClass_C2_parametro_P6 non è  uguale a  commento: {53,} 8, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V9 il valore GialloaVerdea
    
     ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V1 il valore  False 
    
    
    
    }
*/
void L_P1__Macro5(instance_id_t const my_id )
{
//  se la macro  SubClass_C2_macrova_M6 ( con argomento_a10   uguale a GialloVerde ,argomento_a3   uguale a Verde ,argomento_a9   uguale a c120  e argomento_a6   uguale a GialloVerde )   è  uguale a  True  *40,* ,  Applica gli effetti
    //       della macro SubClass_C2_macroef_M5  *73,*
    // ,altrimenti  *70,*Incrementa il contatore SubClass_C2_contatore_Co6
    if((L_P1__Macro12(my_id,gialloverde,verde,gialloverde,c120) == true)){
    
    L_P1__Macro8(my_id);
    }else{
    
    Counter_Incr(L_P1__GetSubcl51(my_id));
    }
    //  *37,*  se la variabile SubClass_C2_variabile_V4 è  maggiore di  *54,* 10 *36,* o  se il timer SubClass_C2_timer_T2 è attivo *34,* e  se il parametro SubClass_C2_parametro_P1 non è  uguale a  *53,* 1 *36,* o  se il timer SubClass_C2_timer_T4 è disattivo *38,* o  se il contatore SubClass_C2_contatore_Co6 non è  minore di  *55,* 13, *71,*Decrementa il contatore SubClass_C2_contatore_Co2
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_OrLogicOP_2 = false;
    res_OrLogicOP_2 = (res_OrLogicOP_2 || (L_P1__GetSubcl41(my_id) > 10u));
    bool res_AndLogicOP_3 = true;
    res_AndLogicOP_3 = (res_AndLogicOP_3 && Timer_Attivo(L_P1__GetSubcl48(my_id)));
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetParamSubcl10(my_id) == 1u));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_4);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_3);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_OrLogicOP_2);
    res_OrLogicOP_1 = (res_OrLogicOP_1 || Timer_Disattivo(L_P1__GetSubcl49(my_id)));
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (Counter_GetValore(L_P1__GetSubcl51(my_id)) < 13u));
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_5);
    
    if(res_OrLogicOP_0){
    
    Counter_Decr(L_P1__GetSubcl50(my_id));
    }
    //  *42,*  se  MainClass_C1_controllo_C8 del campo  MainClass_C1 di SubClass_C2_lista_L10 è  uguale a RossoGialloGiallo *36,* e  se il timer SubClass_C2_timer_T10 non è scaduto *36,* o  se il timer SubClass_C2_timer_T2 è attivo, *66,* Assegna al comando SubClass_C2_comando_C7 il valore  False 
    // ,altrimenti   Applica gli effetti
    //       della macro SubClass_C2_macroef_M5
    bool res_OrLogicOP_6 = false;
    bool res_AndLogicOP_7 = true;
    bool res_ForAllPredicate_8 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl5Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl5(my_id,i);
    bool res_ImpliesLogicOp_9 = true;
    res_ImpliesLogicOp_9 = (res_ImpliesLogicOp_9 && (L_P1__GetInMainc5(it.mainc45) == rossogiallo));
    res_ForAllPredicate_8 = res_ImpliesLogicOp_9;
    if(!res_ForAllPredicate_8) {break;}
    }
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_ForAllPredicate_8);
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! Timer_Scaduto(L_P1__GetSubcl47(my_id)));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_10);
    
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_AndLogicOP_7);
    res_OrLogicOP_6 = (res_OrLogicOP_6 || Timer_Attivo(L_P1__GetSubcl48(my_id)));
    
    if(res_OrLogicOP_6){
    
    L_P1__SetOutSubcl(my_id,false);
    }else{
    
    L_P1__Macro8(my_id);
    }
    //  *73,*
    // *37,*  se la variabile SubClass_C2_variabile_V4 è  maggiore di  *54,* 7 *36,* o  se il timer SubClass_C2_timer_T2 non è attivo *34,* o  se il parametro SubClass_C2_parametro_P6 è  uguale a  *53,* 1, *67,* Assegna alla variabile SubClass_C2_variabile_V5 il valore 8
    // ,altrimenti  *67,* Assegna alla variabile SubClass_C2_variabile_V4 il valore 6
    bool res_OrLogicOP_11 = false;
    bool res_OrLogicOP_12 = false;
    res_OrLogicOP_12 = (res_OrLogicOP_12 || (L_P1__GetSubcl41(my_id) > 7u));
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! Timer_Attivo(L_P1__GetSubcl48(my_id)));
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_NotLogicOP_13);
    
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_OrLogicOP_12);
    res_OrLogicOP_11 = (res_OrLogicOP_11 || (L_P1__GetParamSubcl13(my_id) == 1u));
    
    if(res_OrLogicOP_11){
    
    L_P1__SetSubcl42(my_id,8u);
    }else{
    
    L_P1__SetSubcl41(my_id,6u);
    }
    //  *110,*  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è scaduto *37,* o  se la variabile SubClass_C2_variabile_V5 non è  uguale a  *53,* 10 o  se il controllo ConsDef  è  uguale a FALSE  *34,* o  se il parametro SubClass_C2_parametro_P6 non è  uguale a  *53,* 8, *67,* Assegna alla variabile SubClass_C2_variabile_V9 il valore GialloaVerdea
    // ,altrimenti  *67,* Assegna alla variabile SubClass_C2_variabile_V1 il valore  False
    bool res_OrLogicOP_14 = false;
    bool res_OrLogicOP_15 = false;
    bool res_OrLogicOP_16 = false;
    res_OrLogicOP_16 = (res_OrLogicOP_16 || Timer_Scaduto(L_P1__GetSubcl46(my_id)));
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! (L_P1__GetSubcl42(my_id) == 10u));
    res_OrLogicOP_16 = (res_OrLogicOP_16 || res_NotLogicOP_17);
    
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_OrLogicOP_16);
    res_OrLogicOP_15 = (res_OrLogicOP_15 || (L_P1__GetInConsd1(my_id) == false));
    
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_OrLogicOP_15);
    bool res_NotLogicOP_18 = true;
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! (L_P1__GetParamSubcl13(my_id) == 8u));
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_NotLogicOP_18);
    
    if(res_OrLogicOP_14){
    
    L_P1__SetSubcl44(my_id,gialloaverd);
    }else{
    
    L_P1__SetSubcl40(my_id,false);
    }
}

/*
    CNL corrispondente:
    
    {  se il controllo ConsDef  è  uguale a FALSE ,  commento: {44,}  se  MainClass_C1_variabile_V1 del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  commento: {105,} è  uguale a  commento: {53,} 4, commento: {88,} quando  commento: {42,}    MainClass_C1_controllo_C8 del campo  MainClass_C1     è  uguale a RossoGialloGiallo commento: {34,} o  se il parametro SubClass_C2_parametro_P2 è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} e  se la variabile SubClass_C2_variabile_V4 non è  uguale a  commento: {53,} 5 commento: {35,} e  se il controllo SubClass_C2_controllo_C2 non è  diverso da GialloaVerdea, commento: {68,}Attiva il timer SubClass_C2_timer_T4
    
       
     commento: {34,}  se il parametro SubClass_C2_parametro_P1 è  diverso da  commento: {56,} 9 commento: {35,} o  se il controllo SubClass_C2_controllo_C2 non è  uguale a GialloaVerdea commento: {35,} e  se il controllo SubClass_C2_controllo_C5 non è  uguale a GialloaVerdea e  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro SubClass_C2_parametro_P1 è  minore di  commento: {55,} 8 commento: {38,} e  se il contatore SubClass_C2_contatore_Co6 è  uguale a  commento: {53,} 12, commento: {72,}Azzera il contatore SubClass_C2_contatore_Co6
    
       
    
    }
*/
void L_P1__Macro6(instance_id_t const my_id )
{
//  se il controllo ConsDef  è  uguale a FALSE ,  *44,*  se  MainClass_C1_variabile_V1 del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  *105,* è  uguale a  *53,* 4, *88,* quando  *42,*    MainClass_C1_controllo_C8 del campo  MainClass_C1     è  uguale a RossoGialloGiallo *34,* o  se il parametro SubClass_C2_parametro_P2 è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE  *37,* e  se la variabile SubClass_C2_variabile_V4 non è  uguale a  *53,* 5 *35,* e  se il controllo SubClass_C2_controllo_C2 non è  diverso da GialloaVerdea, *68,*Attiva il timer SubClass_C2_timer_T4
    bool res_OrLogicOP_0 = false;
    bool res_AndLogicOP_1 = true;
    res_AndLogicOP_1 = (res_AndLogicOP_1 && (L_P1__GetInConsd1(my_id) == false));
    bool res_ForAllPredicateNotEmpty_2 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl5Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl5(my_id,i);
    bool res_ImpliesLogicOp_3 = true;
    if((L_P1__GetInMainc5(it.mainc45) == rossogiallo)){
    res_ImpliesLogicOp_3 = (res_ImpliesLogicOp_3 && (L_P1__GetMainc33(it.mainc45) == 4u));
    res_ForAllPredicateNotEmpty_2 = res_ImpliesLogicOp_3;
    if(!res_ForAllPredicateNotEmpty_2) {break;}
    }
    }
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_ForAllPredicateNotEmpty_2);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_1);
    bool res_AndLogicOP_4 = true;
    bool res_AndLogicOP_5 = true;
    bool res_AndLogicOP_6 = true;
    res_AndLogicOP_6 = (res_AndLogicOP_6 && (L_P1__GetParamSubcl11(my_id) == false));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && (L_P1__GetInConsd1(my_id) == false));
    
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_AndLogicOP_6);
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetSubcl41(my_id) == 5u));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_7);
    
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_AndLogicOP_5);
    bool res_NotLogicOP_8 = true;
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetInSubcl2(my_id) == gialloaverd));
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! res_NotLogicOP_9);
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_8);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_4);
    
    if(res_OrLogicOP_0){
    
    Timer_Attiva(L_P1__GetSubcl49(my_id));
    }
    //  *34,*  se il parametro SubClass_C2_parametro_P1 è  diverso da  *56,* 9 *35,* o  se il controllo SubClass_C2_controllo_C2 non è  uguale a GialloaVerdea *35,* e  se il controllo SubClass_C2_controllo_C5 non è  uguale a GialloaVerdea e  se il controllo ConsDef  è  uguale a FALSE  *34,* e  se il parametro SubClass_C2_parametro_P1 è  minore di  *55,* 8 *38,* e  se il contatore SubClass_C2_contatore_Co6 è  uguale a  *53,* 12, *72,*Azzera il contatore SubClass_C2_contatore_Co6
    bool res_OrLogicOP_10 = false;
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (L_P1__GetParamSubcl10(my_id) == 9u));
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_NotLogicOP_11);
    bool res_AndLogicOP_12 = true;
    bool res_AndLogicOP_13 = true;
    bool res_AndLogicOP_14 = true;
    bool res_AndLogicOP_15 = true;
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (L_P1__GetInSubcl2(my_id) == gialloaverd));
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_NotLogicOP_16);
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! (L_P1__GetInSubcl3(my_id) == gialloaverd));
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_NotLogicOP_17);
    
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_AndLogicOP_15);
    res_AndLogicOP_14 = (res_AndLogicOP_14 && (L_P1__GetInConsd1(my_id) == false));
    
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_AndLogicOP_14);
    res_AndLogicOP_13 = (res_AndLogicOP_13 && (L_P1__GetParamSubcl10(my_id) < 8u));
    
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_AndLogicOP_13);
    res_AndLogicOP_12 = (res_AndLogicOP_12 && (Counter_GetValore(L_P1__GetSubcl51(my_id)) == 12u));
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_AndLogicOP_12);
    
    if(res_OrLogicOP_10){
    
    Counter_Res(L_P1__GetSubcl51(my_id));
    }
}

/*
    CNL corrispondente:
    
    { commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L8 è  diverso da  commento: {56,}  state1  commento: {38,} e  se il contatore SubClass_C2_contatore_Co2 è  diverso da  commento: {56,} 15041 e  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} o  se il parametro SubClass_C2_parametro_P6 è  uguale a  commento: {53,} 5 commento: {36,} o  se il timer SubClass_C2_timer_T10 non è attivo, commento: {69,}Disattiva il timer SubClass_C2_timer_T2
    
       
     commento: {34,}  se il parametro SubClass_C2_parametro_P6 non è  minore di  commento: {55,} 8 commento: {37,} e  se la variabile SubClass_C2_variabile_V5 non è  minore di  commento: {55,} 2 commento: {34,} e  se il parametro SubClass_C2_parametro_P2 è  diverso da  True , commento: {68,}Attiva il timer SubClass_C2_timer_T4
    
     ,altrimenti  commento: {69,}Disattiva il timer SubClass_C2_timer_T10
    
    
      se la macro  SubClass_C2_macrova_M6 ( con argomento_a10   uguale a GialloaVerdea ,argomento_a3   uguale a c120 ,argomento_a9   uguale a c120  e argomento_a6   uguale a GialloaVerdea )   è  diverso da  False  commento: {40,} ,  commento: {41,}  se MainClass_C1_parametro_P10 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  commento: {105,} è  uguale a  True , commento: {88,} quando  commento: {43,}   MainClass_C1_timer_T5 del campo  MainClass_C1     commento: {105,} è disattivo, commento: {72,}Azzera il contatore SubClass_C2_contatore_Co2
    
     ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V4 il valore 7
    
    
    
    }
*/
void L_P1__Macro7(instance_id_t const my_id )
{
//  *111,*  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L8 è  diverso da  *56,*  state1  *38,* e  se il contatore SubClass_C2_contatore_Co2 è  diverso da  *56,* 15041 e  se il controllo ConsDef  è  uguale a FALSE  *34,* o  se il parametro SubClass_C2_parametro_P6 è  uguale a  *53,* 5 *36,* o  se il timer SubClass_C2_timer_T10 non è attivo, *69,*Disattiva il timer SubClass_C2_timer_T2
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_AndLogicOP_2 = true;
    bool res_AndLogicOP_3 = true;
    bool res_ForAllPredicate_4 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl9Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl9(my_id,i);
    bool res_ImpliesLogicOp_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1_C1_GetState(it.mainc45) == C1_St_state));
    res_ImpliesLogicOp_5 = (res_ImpliesLogicOp_5 && res_NotLogicOP_6);
    res_ForAllPredicate_4 = res_ImpliesLogicOp_5;
    if(!res_ForAllPredicate_4) {break;}
    }
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_ForAllPredicate_4);
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (Counter_GetValore(L_P1__GetSubcl50(my_id)) == 15041u));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_7);
    
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_AndLogicOP_3);
    res_AndLogicOP_2 = (res_AndLogicOP_2 && (L_P1__GetInConsd1(my_id) == false));
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_2);
    res_OrLogicOP_1 = (res_OrLogicOP_1 || (L_P1__GetParamSubcl13(my_id) == 5u));
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! Timer_Attivo(L_P1__GetSubcl47(my_id)));
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_8);
    
    if(res_OrLogicOP_0){
    
    Timer_Disattiva(L_P1__GetSubcl48(my_id));
    }
    //  *34,*  se il parametro SubClass_C2_parametro_P6 non è  minore di  *55,* 8 *37,* e  se la variabile SubClass_C2_variabile_V5 non è  minore di  *55,* 2 *34,* e  se il parametro SubClass_C2_parametro_P2 è  diverso da  True , *68,*Attiva il timer SubClass_C2_timer_T4
    // ,altrimenti  *69,*Disattiva il timer SubClass_C2_timer_T10
    bool res_AndLogicOP_9 = true;
    bool res_AndLogicOP_10 = true;
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (L_P1__GetParamSubcl13(my_id) < 8u));
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_NotLogicOP_11);
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (L_P1__GetSubcl42(my_id) < 2u));
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_NotLogicOP_12);
    
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_AndLogicOP_10);
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (L_P1__GetParamSubcl11(my_id) == true));
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_NotLogicOP_13);
    
    if(res_AndLogicOP_9){
    
    Timer_Attiva(L_P1__GetSubcl49(my_id));
    }else{
    
    Timer_Disattiva(L_P1__GetSubcl47(my_id));
    }
    //  se la macro  SubClass_C2_macrova_M6 ( con argomento_a10   uguale a GialloaVerdea ,argomento_a3   uguale a c120 ,argomento_a9   uguale a c120  e argomento_a6   uguale a GialloaVerdea )   è  diverso da  False  *40,* ,  *41,*  se MainClass_C1_parametro_P10 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  *105,* è  uguale a  True , *88,* quando  *43,*   MainClass_C1_timer_T5 del campo  MainClass_C1     *105,* è disattivo, *72,*Azzera il contatore SubClass_C2_contatore_Co2
    // ,altrimenti  *67,* Assegna alla variabile SubClass_C2_variabile_V4 il valore 7
    bool res_AndLogicOP_14 = true;
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (L_P1__Macro12(my_id,gialloaverd,c120,gialloaverd,c120) == false));
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_NotLogicOP_15);
    bool res_ForAllPredicateNotEmpty_16 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl9Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl9(my_id,i);
    bool res_ImpliesLogicOp_17 = true;
    if(Timer_Disattivo(L_P1__GetMainc40(it.mainc45))){
    res_ImpliesLogicOp_17 = (res_ImpliesLogicOp_17 && (L_P1__GetParamMainc6(it.mainc45) == true));
    res_ForAllPredicateNotEmpty_16 = res_ImpliesLogicOp_17;
    if(!res_ForAllPredicateNotEmpty_16) {break;}
    }
    }
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_ForAllPredicateNotEmpty_16);
    
    if(res_AndLogicOP_14){
    
    Counter_Res(L_P1__GetSubcl50(my_id));
    }else{
    
    L_P1__SetSubcl41(my_id,7u);
    }
}

/*
    CNL corrispondente:
    
    { commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L5 esiste e  commento: {105,} è  diverso da  commento: {56,}  state1  e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} e  se la variabile SubClass_C2_variabile_V1 è  diverso da  True , commento: {66,} Assegna al comando SubClass_C2_comando_C9 il valore  False 
    
     ,altrimenti   commento: {67,} Assegna alla variabile SubClass_C2_variabile_V8 il valore 7 commento: {67,}
    
    
     commento: {43,}  se MainClass_C1_timer_T9 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  commento: {105,} è attivo commento: {38,} e  se il contatore SubClass_C2_contatore_Co7 è  diverso da  commento: {56,} 142,  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V4 il valore 3 commento: {67,}
    
     ,altrimenti  commento: {70,}Incrementa il contatore SubClass_C2_contatore_Co7
    
    
     commento: {36,}  se il timer SubClass_C2_timer_T4 non è disattivo commento: {36,} o  se il timer SubClass_C2_timer_T4 è disattivo commento: {35,} o  se il controllo SubClass_C2_controllo_C6 è  diverso da  True  commento: {35,} e  se il controllo SubClass_C2_controllo_C6 non è  diverso da  True  o  se il controllo ConsDef  è  uguale a FALSE , commento: {66,} Assegna al comando SubClass_C2_comando_C7 il valore  False 
    
     ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V5 il valore 3
    
    
     commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L10 è  diverso da  commento: {56,}  state1  e  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} o  se il contatore SubClass_C2_contatore_Co7 è  diverso da  commento: {56,} 1553 commento: {36,} e  se il timer SubClass_C2_timer_T10 è disattivo commento: {35,} o  se il controllo SubClass_C2_controllo_C2 è  diverso da GialloaVerdea, commento: {66,} Assegna al comando SubClass_C2_comando_C7 il valore  True 
    
     ,altrimenti  commento: {66,} Assegna al comando SubClass_C2_comando_C9 il valore  True 
    
    
    
    }
*/
void L_P1__Macro8(instance_id_t const my_id )
{
//  *111,*  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L5 esiste e  *105,* è  diverso da  *56,*  state1  e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  *37,* e  se la variabile SubClass_C2_variabile_V1 è  diverso da  True , *66,* Assegna al comando SubClass_C2_comando_C9 il valore  False 
    // ,altrimenti   *67,* Assegna alla variabile SubClass_C2_variabile_V8 il valore 7
    bool res_AndLogicOP_0 = true;
    bool res_AndLogicOP_1 = true;
    bool res_AndLogicOP_2 = true;
    bool res_ForAllPredicateNotEmpty_3 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl8Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl8(my_id,i);
    bool res_ImpliesLogicOp_4 = true;
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1_C1_GetState(it.mainc45) == C1_St_state));
    res_ImpliesLogicOp_4 = (res_ImpliesLogicOp_4 && res_NotLogicOP_5);
    res_ForAllPredicateNotEmpty_3 = res_ImpliesLogicOp_4;
    if(!res_ForAllPredicateNotEmpty_3) {break;}
    }
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_ForAllPredicateNotEmpty_3);
    res_AndLogicOP_2 = (res_AndLogicOP_2 && (L_P1__GetInConsd1(my_id) == false));
    
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_AndLogicOP_2);
    res_AndLogicOP_1 = (res_AndLogicOP_1 && (L_P1__GetInConsd1(my_id) == false));
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_AndLogicOP_1);
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetSubcl40(my_id) == true));
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_NotLogicOP_6);
    
    if(res_AndLogicOP_0){
    
    L_P1__SetOutSubcl1(my_id,false);
    }else{
    
    L_P1__SetSubcl43(my_id,7u);
    }
    //  *67,*
    // *43,*  se MainClass_C1_timer_T9 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  *105,* è attivo *38,* e  se il contatore SubClass_C2_contatore_Co7 è  diverso da  *56,* 142,  *67,* Assegna alla variabile SubClass_C2_variabile_V4 il valore 3 *67,*
    // ,altrimenti  *70,*Incrementa il contatore SubClass_C2_contatore_Co7
    bool res_AndLogicOP_7 = true;
    bool res_ForAllPredicateNotEmpty_8 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl6Length(my_id); ++i)
    {
    L_P1__Recor1 it = L_P1__GetRecSubcl6(my_id,i);
    bool res_ImpliesLogicOp_9 = true;
    res_ImpliesLogicOp_9 = (res_ImpliesLogicOp_9 && Timer_Attivo(L_P1__GetMainc41(it.mainc46)));
    res_ForAllPredicateNotEmpty_8 = res_ImpliesLogicOp_9;
    if(!res_ForAllPredicateNotEmpty_8) {break;}
    }
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_ForAllPredicateNotEmpty_8);
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (Counter_GetValore(L_P1__GetSubcl52(my_id)) == 142u));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_10);
    
    if(res_AndLogicOP_7){
    
    L_P1__SetSubcl41(my_id,3u);
    }else{
    
    Counter_Incr(L_P1__GetSubcl52(my_id));
    }
    //  *36,*  se il timer SubClass_C2_timer_T4 non è disattivo *36,* o  se il timer SubClass_C2_timer_T4 è disattivo *35,* o  se il controllo SubClass_C2_controllo_C6 è  diverso da  True  *35,* e  se il controllo SubClass_C2_controllo_C6 non è  diverso da  True  o  se il controllo ConsDef  è  uguale a FALSE , *66,* Assegna al comando SubClass_C2_comando_C7 il valore  False 
    // ,altrimenti  *67,* Assegna alla variabile SubClass_C2_variabile_V5 il valore 3
    bool res_OrLogicOP_11 = false;
    bool res_OrLogicOP_12 = false;
    bool res_OrLogicOP_13 = false;
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! Timer_Disattivo(L_P1__GetSubcl49(my_id)));
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_NotLogicOP_14);
    res_OrLogicOP_13 = (res_OrLogicOP_13 || Timer_Disattivo(L_P1__GetSubcl49(my_id)));
    
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_OrLogicOP_13);
    bool res_AndLogicOP_15 = true;
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (L_P1__GetInSubcl4(my_id) == true));
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_NotLogicOP_16);
    bool res_NotLogicOP_17 = true;
    bool res_NotLogicOP_18 = true;
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! (L_P1__GetInSubcl4(my_id) == true));
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! res_NotLogicOP_18);
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_NotLogicOP_17);
    
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_AndLogicOP_15);
    
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_OrLogicOP_12);
    res_OrLogicOP_11 = (res_OrLogicOP_11 || (L_P1__GetInConsd1(my_id) == false));
    
    if(res_OrLogicOP_11){
    
    L_P1__SetOutSubcl(my_id,false);
    }else{
    
    L_P1__SetSubcl42(my_id,3u);
    }
    //  *111,*  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L10 è  diverso da  *56,*  state1  e  se il controllo ConsDef  è  uguale a FALSE  *38,* o  se il contatore SubClass_C2_contatore_Co7 è  diverso da  *56,* 1553 *36,* e  se il timer SubClass_C2_timer_T10 è disattivo *35,* o  se il controllo SubClass_C2_controllo_C2 è  diverso da GialloaVerdea, *66,* Assegna al comando SubClass_C2_comando_C7 il valore  True 
    // ,altrimenti  *66,* Assegna al comando SubClass_C2_comando_C9 il valore  True
    bool res_OrLogicOP_19 = false;
    bool res_OrLogicOP_20 = false;
    bool res_AndLogicOP_21 = true;
    bool res_ForAllPredicate_22 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl5Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl5(my_id,i);
    bool res_ImpliesLogicOp_23 = true;
    bool res_NotLogicOP_24 = true;
    res_NotLogicOP_24 = (res_NotLogicOP_24 && ! (L_P1_C1_GetState(it.mainc45) == C1_St_state));
    res_ImpliesLogicOp_23 = (res_ImpliesLogicOp_23 && res_NotLogicOP_24);
    res_ForAllPredicate_22 = res_ImpliesLogicOp_23;
    if(!res_ForAllPredicate_22) {break;}
    }
    res_AndLogicOP_21 = (res_AndLogicOP_21 && res_ForAllPredicate_22);
    res_AndLogicOP_21 = (res_AndLogicOP_21 && (L_P1__GetInConsd1(my_id) == false));
    
    res_OrLogicOP_20 = (res_OrLogicOP_20 || res_AndLogicOP_21);
    bool res_AndLogicOP_25 = true;
    bool res_NotLogicOP_26 = true;
    res_NotLogicOP_26 = (res_NotLogicOP_26 && ! (Counter_GetValore(L_P1__GetSubcl52(my_id)) == 1553u));
    res_AndLogicOP_25 = (res_AndLogicOP_25 && res_NotLogicOP_26);
    res_AndLogicOP_25 = (res_AndLogicOP_25 && Timer_Disattivo(L_P1__GetSubcl47(my_id)));
    
    res_OrLogicOP_20 = (res_OrLogicOP_20 || res_AndLogicOP_25);
    
    res_OrLogicOP_19 = (res_OrLogicOP_19 || res_OrLogicOP_20);
    bool res_NotLogicOP_27 = true;
    res_NotLogicOP_27 = (res_NotLogicOP_27 && ! (L_P1__GetInSubcl2(my_id) == gialloaverd));
    res_OrLogicOP_19 = (res_OrLogicOP_19 || res_NotLogicOP_27);
    
    if(res_OrLogicOP_19){
    
    L_P1__SetOutSubcl(my_id,true);
    }else{
    
    L_P1__SetOutSubcl1(my_id,true);
    }
}

/*
    CNL corrispondente:
    
    { commento: {34,}  se il parametro SubClass_C2_parametro_P6 è  uguale a  commento: {53,} 3,  commento: {42,}  se  MainClass_C1_controllo_C8 del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  commento: {105,} è  diverso da RossoGialloGiallo, commento: {88,} quando  commento: {44,}    MainClass_C1_variabile_V5 del campo  MainClass_C1     è  uguale a  False  commento: {34,} e  se il parametro SubClass_C2_parametro_P4 non è  uguale a Verde commento: {37,} e  se la variabile SubClass_C2_variabile_V5 è  uguale a  commento: {53,} 7 commento: {36,} e  se il timer SubClass_C2_timer_T2 è disattivo commento: {37,} o  se la variabile SubClass_C2_variabile_V5 è  uguale a  commento: {53,} 9, commento: {69,}Disattiva il timer SubClass_C2_timer_T10
    
     ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V4 il valore 1
    
    
    
    }
*/
void L_P1__Macro9(instance_id_t const my_id )
{
//  *34,*  se il parametro SubClass_C2_parametro_P6 è  uguale a  *53,* 3,  *42,*  se  MainClass_C1_controllo_C8 del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  *105,* è  diverso da RossoGialloGiallo, *88,* quando  *44,*    MainClass_C1_variabile_V5 del campo  MainClass_C1     è  uguale a  False  *34,* e  se il parametro SubClass_C2_parametro_P4 non è  uguale a Verde *37,* e  se la variabile SubClass_C2_variabile_V5 è  uguale a  *53,* 7 *36,* e  se il timer SubClass_C2_timer_T2 è disattivo *37,* o  se la variabile SubClass_C2_variabile_V5 è  uguale a  *53,* 9, *69,*Disattiva il timer SubClass_C2_timer_T10
    // ,altrimenti  *67,* Assegna alla variabile SubClass_C2_variabile_V4 il valore 1
    bool res_OrLogicOP_0 = false;
    bool res_AndLogicOP_1 = true;
    bool res_AndLogicOP_2 = true;
    bool res_AndLogicOP_3 = true;
    bool res_AndLogicOP_4 = true;
    res_AndLogicOP_4 = (res_AndLogicOP_4 && (L_P1__GetParamSubcl13(my_id) == 3u));
    bool res_ForAllPredicateNotEmpty_5 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl5Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl5(my_id,i);
    bool res_ImpliesLogicOp_6 = true;
    if((L_P1__GetMainc34(it.mainc45) == false)){
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetInMainc5(it.mainc45) == rossogiallo));
    res_ImpliesLogicOp_6 = (res_ImpliesLogicOp_6 && res_NotLogicOP_7);
    res_ForAllPredicateNotEmpty_5 = res_ImpliesLogicOp_6;
    if(!res_ForAllPredicateNotEmpty_5) {break;}
    }
    }
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_ForAllPredicateNotEmpty_5);
    
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_AndLogicOP_4);
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetParamSubcl12(my_id) == verde));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_8);
    
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_AndLogicOP_3);
    res_AndLogicOP_2 = (res_AndLogicOP_2 && (L_P1__GetSubcl42(my_id) == 7u));
    
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_AndLogicOP_2);
    res_AndLogicOP_1 = (res_AndLogicOP_1 && Timer_Disattivo(L_P1__GetSubcl48(my_id)));
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_1);
    res_OrLogicOP_0 = (res_OrLogicOP_0 || (L_P1__GetSubcl42(my_id) == 9u));
    
    if(res_OrLogicOP_0){
    
    Timer_Disattiva(L_P1__GetSubcl47(my_id));
    }else{
    
    L_P1__SetSubcl41(my_id,1u);
    }
}


// Macro di verifica

/*
    CNL corrispondente:
     
    { commento: {63,} commento: {43,}  se MainClass_C1_timer_T9 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  commento: {105,} è disattivo commento: {34,} o  se il parametro SubClass_C2_parametro_P4 non è  uguale a Verde, Solo una delle seguenti { 
     commento: {62,} commento: {34,}  se il parametro SubClass_C2_parametro_P4 è  diverso da Verde commento: {36,} o  se il timer SubClass_C2_timer_T2 non è scaduto commento: {38,} o  se il contatore SubClass_C2_contatore_Co2 non è  diverso da  commento: {56,} 13530 commento: {38,} o  se il contatore SubClass_C2_contatore_Co7 non è  uguale a  commento: {53,} 15412 commento: {35,} o  se il controllo SubClass_C2_controllo_C5 è  diverso da GialloaVerdea commento: {36,} e  se il timer SubClass_C2_timer_T4 è scaduto, Almeno una delle seguenti { 
     commento: {63,} commento: {110,}  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è disattivo commento: {36,} e  se il timer SubClass_C2_timer_T2 non è disattivo commento: {38,} o  se il contatore SubClass_C2_contatore_Co6 non è  uguale a  commento: {53,} 1453 commento: {37,} e  se la variabile SubClass_C2_variabile_V5 è  maggiore di  commento: {54,} 9, Solo una delle seguenti { 
     commento: {43,}  se MainClass_C1_timer_T9 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  commento: {105,} è disattivo commento: {36,} e  se il timer SubClass_C2_timer_T4 è disattivo e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   commento: {47,51,}  commento: {34,}  il parametro SubClass_C2_parametro_P4 sia  diverso da Verde
     commento: {104,} e  che  commento: {,}  il contatore SubClass_C2_contatore_Co7 sia  uguale a  commento: {53,} 152
    
    
     } Verifica che   commento: {47,48,50,51,}  commento: {,}  la variabile SubClass_C2_variabile_V4 non sia  diverso da  commento: {56,} 1
     commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} o  che  commento: {34,}  il parametro SubClass_C2_parametro_P6 sia  uguale a  commento: {53,} 2
     commento: {104,} o  che  commento: {,}  il controllo SubClass_C2_controllo_C2 sia  diverso da GialloaVerdea
     commento: {104,} e  che  commento: {,}  il contatore SubClass_C2_contatore_Co2 non sia  maggiore di  commento: {54,} 1153
    
    
     } Verifica che   commento: {51,}  commento: {,}  il contatore SubClass_C2_contatore_Co2 sia  diverso da  commento: {56,} 130
    
    
     } Verifica che   commento: {48,51,}  commento: {,}  il contatore SubClass_C2_contatore_Co7 sia  minore di  commento: {55,} 15
     commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
    
    
    }
*/
bool L_P1__Macro14(instance_id_t const my_id )
{
bool res_AndLogicOP_0 = true;
    
    //  *63,* *43,*  se MainClass_C1_timer_T9 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  *105,* è disattivo *34,* o  se il parametro SubClass_C2_parametro_P4 non è  uguale a Verde, Solo una delle seguenti { 
    //   *62,* *34,*  se il parametro SubClass_C2_parametro_P4 è  diverso da Verde *36,* o  se il timer SubClass_C2_timer_T2 non è scaduto *38,* o  se il contatore SubClass_C2_contatore_Co2 non è  diverso da  *56,* 13530 *38,* o  se il contatore SubClass_C2_contatore_Co7 non è  uguale a  *53,* 15412 *35,* o  se il controllo SubClass_C2_controllo_C5 è  diverso da GialloaVerdea *36,* e  se il timer SubClass_C2_timer_T4 è scaduto, Almeno una delle seguenti { 
    //   *63,* *110,*  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è disattivo *36,* e  se il timer SubClass_C2_timer_T2 non è disattivo *38,* o  se il contatore SubClass_C2_contatore_Co6 non è  uguale a  *53,* 1453 *37,* e  se la variabile SubClass_C2_variabile_V5 è  maggiore di  *54,* 9, Solo una delle seguenti { 
    //   *43,*  se MainClass_C1_timer_T9 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  *105,* è disattivo *36,* e  se il timer SubClass_C2_timer_T4 è disattivo e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   *47,51,*  *34,*  il parametro SubClass_C2_parametro_P4 sia  diverso da Verde
    //   *104,* e  che  *,*  il contatore SubClass_C2_contatore_Co7 sia  uguale a  *53,* 152
    //   } Verifica che   *47,48,50,51,*  *,*  la variabile SubClass_C2_variabile_V4 non sia  diverso da  *56,* 1
    //   *104,* e  che   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* o  che  *34,*  il parametro SubClass_C2_parametro_P6 sia  uguale a  *53,* 2
    //   *104,* o  che  *,*  il controllo SubClass_C2_controllo_C2 sia  diverso da GialloaVerdea
    //   *104,* e  che  *,*  il contatore SubClass_C2_contatore_Co2 non sia  maggiore di  *54,* 1153
    //   } Verifica che   *51,*  *,*  il contatore SubClass_C2_contatore_Co2 sia  diverso da  *56,* 130
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_ForAllPredicateNotEmpty_3 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl6Length(my_id); ++i)
    {
    L_P1__Recor1 it = L_P1__GetRecSubcl6(my_id,i);
    bool res_ImpliesLogicOp_4 = true;
    res_ImpliesLogicOp_4 = (res_ImpliesLogicOp_4 && Timer_Disattivo(L_P1__GetMainc41(it.mainc46)));
    res_ForAllPredicateNotEmpty_3 = res_ImpliesLogicOp_4;
    if(!res_ForAllPredicateNotEmpty_3) {break;}
    }
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_ForAllPredicateNotEmpty_3);
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetParamSubcl12(my_id) == verde));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_5);
    
    if(res_OrLogicOP_2){
    bool res_XorLogicOP_6 = true;
    int xorIndex_res_XorLogicOP_6 = 0;
    bool res_ImpliesLogicOp_7 = true;
    bool res_OrLogicOP_8 = false;
    bool res_OrLogicOP_9 = false;
    bool res_OrLogicOP_10 = false;
    bool res_OrLogicOP_11 = false;
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (L_P1__GetParamSubcl12(my_id) == verde));
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_NotLogicOP_12);
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! Timer_Scaduto(L_P1__GetSubcl48(my_id)));
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_NotLogicOP_13);
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_OrLogicOP_11);
    bool res_NotLogicOP_14 = true;
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (Counter_GetValore(L_P1__GetSubcl50(my_id)) == 13530u));
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! res_NotLogicOP_15);
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_NotLogicOP_14);
    
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_OrLogicOP_10);
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (Counter_GetValore(L_P1__GetSubcl52(my_id)) == 15412u));
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_NotLogicOP_16);
    
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_OrLogicOP_9);
    bool res_AndLogicOP_17 = true;
    bool res_NotLogicOP_18 = true;
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! (L_P1__GetInSubcl3(my_id) == gialloaverd));
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_NotLogicOP_18);
    res_AndLogicOP_17 = (res_AndLogicOP_17 && Timer_Scaduto(L_P1__GetSubcl49(my_id)));
    
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_AndLogicOP_17);
    
    if(res_OrLogicOP_8){
    bool res_OrLogicOP_19 = false;
    bool res_ImpliesLogicOp_20 = true;
    bool res_OrLogicOP_21 = false;
    bool res_AndLogicOP_22 = true;
    res_AndLogicOP_22 = (res_AndLogicOP_22 && Timer_Disattivo(L_P1__GetSubcl46(my_id)));
    bool res_NotLogicOP_23 = true;
    res_NotLogicOP_23 = (res_NotLogicOP_23 && ! Timer_Disattivo(L_P1__GetSubcl48(my_id)));
    res_AndLogicOP_22 = (res_AndLogicOP_22 && res_NotLogicOP_23);
    
    res_OrLogicOP_21 = (res_OrLogicOP_21 || res_AndLogicOP_22);
    bool res_AndLogicOP_24 = true;
    bool res_NotLogicOP_25 = true;
    res_NotLogicOP_25 = (res_NotLogicOP_25 && ! (Counter_GetValore(L_P1__GetSubcl51(my_id)) == 1453u));
    res_AndLogicOP_24 = (res_AndLogicOP_24 && res_NotLogicOP_25);
    res_AndLogicOP_24 = (res_AndLogicOP_24 && (L_P1__GetSubcl42(my_id) > 9u));
    
    res_OrLogicOP_21 = (res_OrLogicOP_21 || res_AndLogicOP_24);
    
    if(res_OrLogicOP_21){
    bool res_ImpliesLogicOp_26 = true;
    bool res_AndLogicOP_27 = true;
    bool res_AndLogicOP_28 = true;
    bool res_ForAllPredicateNotEmpty_29 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl9Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl9(my_id,i);
    bool res_ImpliesLogicOp_30 = true;
    res_ImpliesLogicOp_30 = (res_ImpliesLogicOp_30 && Timer_Disattivo(L_P1__GetMainc41(it.mainc45)));
    res_ForAllPredicateNotEmpty_29 = res_ImpliesLogicOp_30;
    if(!res_ForAllPredicateNotEmpty_29) {break;}
    }
    res_AndLogicOP_28 = (res_AndLogicOP_28 && res_ForAllPredicateNotEmpty_29);
    res_AndLogicOP_28 = (res_AndLogicOP_28 && Timer_Disattivo(L_P1__GetSubcl49(my_id)));
    
    res_AndLogicOP_27 = (res_AndLogicOP_27 && res_AndLogicOP_28);
    res_AndLogicOP_27 = (res_AndLogicOP_27 && (L_P1__GetInConsd1(my_id) == false));
    
    if(res_AndLogicOP_27){
    bool res_AndLogicOP_31 = true;
    bool res_NotLogicOP_32 = true;
    res_NotLogicOP_32 = (res_NotLogicOP_32 && ! (L_P1__GetParamSubcl12(my_id) == verde));
    res_AndLogicOP_31 = (res_AndLogicOP_31 && res_NotLogicOP_32);
    res_AndLogicOP_31 = (res_AndLogicOP_31 && (Counter_GetValore(L_P1__GetSubcl52(my_id)) == 152u));
    
    res_ImpliesLogicOp_26 = (res_ImpliesLogicOp_26 && res_AndLogicOP_31);
    }
    res_ImpliesLogicOp_20 = (res_ImpliesLogicOp_20 && res_ImpliesLogicOp_26);
    }
    res_OrLogicOP_19 = (res_OrLogicOP_19 || res_ImpliesLogicOp_20);
    bool res_OrLogicOP_33 = false;
    bool res_OrLogicOP_34 = false;
    bool res_AndLogicOP_35 = true;
    bool res_NotLogicOP_36 = true;
    bool res_NotLogicOP_37 = true;
    res_NotLogicOP_37 = (res_NotLogicOP_37 && ! (L_P1__GetSubcl41(my_id) == 1u));
    res_NotLogicOP_36 = (res_NotLogicOP_36 && ! res_NotLogicOP_37);
    res_AndLogicOP_35 = (res_AndLogicOP_35 && res_NotLogicOP_36);
    res_AndLogicOP_35 = (res_AndLogicOP_35 && (L_P1__GetInConsd1(my_id) == false));
    
    res_OrLogicOP_34 = (res_OrLogicOP_34 || res_AndLogicOP_35);
    res_OrLogicOP_34 = (res_OrLogicOP_34 || (L_P1__GetParamSubcl13(my_id) == 2u));
    
    res_OrLogicOP_33 = (res_OrLogicOP_33 || res_OrLogicOP_34);
    bool res_AndLogicOP_38 = true;
    bool res_NotLogicOP_39 = true;
    res_NotLogicOP_39 = (res_NotLogicOP_39 && ! (L_P1__GetInSubcl2(my_id) == gialloaverd));
    res_AndLogicOP_38 = (res_AndLogicOP_38 && res_NotLogicOP_39);
    bool res_NotLogicOP_40 = true;
    res_NotLogicOP_40 = (res_NotLogicOP_40 && ! (Counter_GetValore(L_P1__GetSubcl50(my_id)) > 1153u));
    res_AndLogicOP_38 = (res_AndLogicOP_38 && res_NotLogicOP_40);
    
    res_OrLogicOP_33 = (res_OrLogicOP_33 || res_AndLogicOP_38);
    
    res_OrLogicOP_19 = (res_OrLogicOP_19 || res_OrLogicOP_33);
    
    res_ImpliesLogicOp_7 = (res_ImpliesLogicOp_7 && res_OrLogicOP_19);
    }
    if(res_ImpliesLogicOp_7){
    xorIndex_res_XorLogicOP_6 = (xorIndex_res_XorLogicOP_6 + 1);
    }
    bool res_NotLogicOP_41 = true;
    res_NotLogicOP_41 = (res_NotLogicOP_41 && ! (Counter_GetValore(L_P1__GetSubcl50(my_id)) == 130u));
    if(res_NotLogicOP_41){
    xorIndex_res_XorLogicOP_6 = (xorIndex_res_XorLogicOP_6 + 1);
    }
    
    res_XorLogicOP_6 = (res_XorLogicOP_6 && (xorIndex_res_XorLogicOP_6 == 1));
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_XorLogicOP_6);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *48,51,*  *,*  il contatore SubClass_C2_contatore_Co7 sia  minore di  *55,* 15
    //   *104,* o  che   il controllo ConsDef  sia  uguale a FALSE
    bool res_OrLogicOP_42 = false;
    res_OrLogicOP_42 = (res_OrLogicOP_42 || (Counter_GetValore(L_P1__GetSubcl52(my_id)) < 15u));
    res_OrLogicOP_42 = (res_OrLogicOP_42 || (L_P1__GetInConsd1(my_id) == false));
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_42);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
     
    { commento: {110,}  se il ripristino del timer  SubClass_C2_restoreTI_TI1 non è scaduto, Verifica che   commento: {48,49,50,51,}   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} e  che  commento: {,}  la variabile SubClass_C2_variabile_V9 sia  uguale a GialloaVerdea
     commento: {104,} e  che  commento: {,}  il timer SubClass_C2_timer_T10 non sia disattivo
     commento: {104,} o  che  commento: {,}  il controllo SubClass_C2_controllo_C2 sia  diverso da GialloaVerdea
     commento: {104,} e  che  commento: {,}  il contatore SubClass_C2_contatore_Co6 sia  diverso da  commento: {56,} 14
    
    
    }
*/
bool L_P1__Macro15(instance_id_t const my_id )
{
bool res_AndLogicOP_0 = true;
    
    //  *110,*  se il ripristino del timer  SubClass_C2_restoreTI_TI1 non è scaduto, Verifica che   *48,49,50,51,*   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* e  che  *,*  la variabile SubClass_C2_variabile_V9 sia  uguale a GialloaVerdea
    //   *104,* e  che  *,*  il timer SubClass_C2_timer_T10 non sia disattivo
    //   *104,* o  che  *,*  il controllo SubClass_C2_controllo_C2 sia  diverso da GialloaVerdea
    //   *104,* e  che  *,*  il contatore SubClass_C2_contatore_Co6 sia  diverso da  *56,* 14
    bool res_ImpliesLogicOp_1 = true;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! Timer_Scaduto(L_P1__GetSubcl46(my_id)));
    if(res_NotLogicOP_2){
    bool res_OrLogicOP_3 = false;
    bool res_AndLogicOP_4 = true;
    bool res_AndLogicOP_5 = true;
    res_AndLogicOP_5 = (res_AndLogicOP_5 && (L_P1__GetInConsd1(my_id) == false));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && (L_P1__GetSubcl44(my_id) == gialloaverd));
    
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_AndLogicOP_5);
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! Timer_Disattivo(L_P1__GetSubcl47(my_id)));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_6);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_AndLogicOP_4);
    bool res_AndLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetInSubcl2(my_id) == gialloaverd));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_8);
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (Counter_GetValore(L_P1__GetSubcl51(my_id)) == 14u));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_9);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_AndLogicOP_7);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_OrLogicOP_3);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    
    
    return res_AndLogicOP_0;
}


// Macro valorizzate

/*
    CNL corrispondente:
    
    { commento: {[}  se la macro  SubClass_C2_macrova_M7 ( con argomento_a4   uguale a RossoGialloVerde ,argomento_a7   uguale a c120 ,argomento_a1   uguale a AC ,argomento_a5   uguale a GialloVerde  e argomento_a2   uguale a RossoGiallox )   è  uguale a Verde commento: {40,} ,  commento: {43,}  se MainClass_C1_timer_T9 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  commento: {105,} è disattivo, commento: {88,} quando  commento: {41,}   MainClass_C1_parametro_P10 del campo  MainClass_C1     commento: {105,} è  diverso da  True  , assegna alla macro il valore  True 
    
     commento: {46,} assegna alla macro il valore  True  commento: {],}
    }
*/
bool L_P1__Macro10(instance_id_t const my_id , bool argom22, C2_Enumerat2 argom23, C2_Enumerat3 argom24, C2_Enumerat2 argom25, C2_Enumerat2 argom26, C2_Enumerat1 argom27, C2_Enumerat2 argom28)
{
bool res_macro_val;
    
    //  *[*  se la macro  SubClass_C2_macrova_M7 ( con argomento_a4   uguale a RossoGialloVerde ,argomento_a7   uguale a c120 ,argomento_a1   uguale a AC ,argomento_a5   uguale a GialloVerde  e argomento_a2   uguale a RossoGiallox )   è  uguale a Verde *40,* ,  *43,*  se MainClass_C1_timer_T9 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  *105,* è disattivo, *88,* quando  *41,*   MainClass_C1_parametro_P10 del campo  MainClass_C1     *105,* è  diverso da  True
    bool res_AndLogicOP_0 = true;
    res_AndLogicOP_0 = (res_AndLogicOP_0 && (L_P1__Macro13(my_id,ac,rossogiallo4,rossogiallo3,gialloverde,c120) == verde));
    bool res_ForAllPredicateNotEmpty_1 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl9Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl9(my_id,i);
    bool res_ImpliesLogicOp_2 = true;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__GetParamMainc6(it.mainc45) == true));
    if(res_NotLogicOP_3){
    res_ImpliesLogicOp_2 = (res_ImpliesLogicOp_2 && Timer_Disattivo(L_P1__GetMainc41(it.mainc45)));
    res_ForAllPredicateNotEmpty_1 = res_ImpliesLogicOp_2;
    if(!res_ForAllPredicateNotEmpty_1) {break;}
    }
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ForAllPredicateNotEmpty_1);
    
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
    
    { commento: {[}  se l'argomento argomento_a3 è  uguale a RossoGiallox commento: {39,}  e  se l'argomento argomento_a8 non  è  diverso da GialloaVerdea commento: {39,} ,  commento: {44,}  se  MainClass_C1_variabile_V1 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  commento: {105,} è  diverso da  commento: {56,} 6, commento: {88,} quando  commento: {41,}   MainClass_C1_parametro_P10 del campo  MainClass_C1     commento: {105,} è  diverso da  False  commento: {44,} o  se  MainClass_C1_variabile_V5 del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  commento: {105,} è  uguale a  False  , assegna alla macro il valore  False 
    
     commento: {46,} assegna alla macro il valore  False  commento: {],}
    }
*/
bool L_P1__Macro11(instance_id_t const my_id , C2_Enumerat3 argom29, C2_Enumerat4 argom30, C2_Enumerat4 argom31, C2_Enumerat1 argom32, C2_Enumerat2 argom33, C2_Enumerat1 argom34, C2_Enumerat3 argom35)
{
bool res_macro_val;
    
    //  *[*  se l'argomento argomento_a3 è  uguale a RossoGiallox *39,*  e  se l'argomento argomento_a8 non  è  diverso da GialloaVerdea *39,* ,  *44,*  se  MainClass_C1_variabile_V1 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  *105,* è  diverso da  *56,* 6, *88,* quando  *41,*   MainClass_C1_parametro_P10 del campo  MainClass_C1     *105,* è  diverso da  False  *44,* o  se  MainClass_C1_variabile_V5 del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  *105,* è  uguale a  False
    bool res_OrLogicOP_0 = false;
    bool res_AndLogicOP_1 = true;
    res_AndLogicOP_1 = (res_AndLogicOP_1 && (argom30 == rossogiallo4));
    bool res_AndLogicOP_2 = true;
    bool res_NotLogicOP_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (argom34 == gialloaverd));
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! res_NotLogicOP_4);
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_3);
    bool res_ForAllPredicateNotEmpty_5 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl6Length(my_id); ++i)
    {
    L_P1__Recor1 it = L_P1__GetRecSubcl6(my_id,i);
    bool res_ImpliesLogicOp_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetParamMainc6(it.mainc46) == false));
    if(res_NotLogicOP_7){
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetMainc33(it.mainc46) == 6u));
    res_ImpliesLogicOp_6 = (res_ImpliesLogicOp_6 && res_NotLogicOP_8);
    res_ForAllPredicateNotEmpty_5 = res_ImpliesLogicOp_6;
    if(!res_ForAllPredicateNotEmpty_5) {break;}
    }
    }
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_ForAllPredicateNotEmpty_5);
    
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_AndLogicOP_2);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_1);
    bool res_ForAllPredicateNotEmpty_9 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl5Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl5(my_id,i);
    bool res_ImpliesLogicOp_10 = true;
    res_ImpliesLogicOp_10 = (res_ImpliesLogicOp_10 && (L_P1__GetMainc34(it.mainc45) == false));
    res_ForAllPredicateNotEmpty_9 = res_ImpliesLogicOp_10;
    if(!res_ForAllPredicateNotEmpty_9) {break;}
    }
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_ForAllPredicateNotEmpty_9);
    
    if(res_OrLogicOP_0){
    
    res_macro_val = false;
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
bool L_P1__Macro12(instance_id_t const my_id , C2_Enumerat1 argom36, C2_Enumerat2 argom37, C2_Enumerat1 argom38, C2_Enumerat2 argom39)
{
return true;
}

/*
    CNL corrispondente:
    
    { commento: {[} commento: {109,}  se il ripristino della variabile  SubClass_C2_restoreva_RV5 non è  diverso da  True  commento: {44,} e  se  MainClass_C1_variabile_V5 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  commento: {105,} è  uguale a  False  commento: {44,} e  se  MainClass_C1_variabile_V5 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  commento: {105,} è  uguale a  False  commento: {37,} o  se la variabile SubClass_C2_variabile_V4 è  minore di  commento: {55,} 7 , assegna alla macro il valore Verde
    
     commento: {46,} assegna alla macro il valore Verde commento: {],}
    }
*/
C2_Enumerat2 L_P1__Macro13(instance_id_t const my_id , C2_Enumerat3 argom40, C2_Enumerat4 argom41, C2_Enumerat4 argom42, C2_Enumerat1 argom43, C2_Enumerat2 argom44)
{
C2_Enumerat2 res_macro_val;
    
    //  *[* *109,*  se il ripristino della variabile  SubClass_C2_restoreva_RV5 non è  diverso da  True  *44,* e  se  MainClass_C1_variabile_V5 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  *105,* è  uguale a  False  *44,* e  se  MainClass_C1_variabile_V5 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  *105,* è  uguale a  False  *37,* o  se la variabile SubClass_C2_variabile_V4 è  minore di  *55,* 7
    bool res_OrLogicOP_0 = false;
    bool res_AndLogicOP_1 = true;
    bool res_AndLogicOP_2 = true;
    bool res_NotLogicOP_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetSubcl39(my_id) == true));
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! res_NotLogicOP_4);
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_3);
    bool res_ForAllPredicateNotEmpty_5 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl9Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl9(my_id,i);
    bool res_ImpliesLogicOp_6 = true;
    res_ImpliesLogicOp_6 = (res_ImpliesLogicOp_6 && (L_P1__GetMainc34(it.mainc45) == false));
    res_ForAllPredicateNotEmpty_5 = res_ImpliesLogicOp_6;
    if(!res_ForAllPredicateNotEmpty_5) {break;}
    }
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_ForAllPredicateNotEmpty_5);
    
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_AndLogicOP_2);
    bool res_ForAllPredicateNotEmpty_7 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl6Length(my_id); ++i)
    {
    L_P1__Recor1 it = L_P1__GetRecSubcl6(my_id,i);
    bool res_ImpliesLogicOp_8 = true;
    res_ImpliesLogicOp_8 = (res_ImpliesLogicOp_8 && (L_P1__GetMainc34(it.mainc46) == false));
    res_ForAllPredicateNotEmpty_7 = res_ImpliesLogicOp_8;
    if(!res_ForAllPredicateNotEmpty_7) {break;}
    }
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_ForAllPredicateNotEmpty_7);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_1);
    res_OrLogicOP_0 = (res_OrLogicOP_0 || (L_P1__GetSubcl41(my_id) < 7u));
    
    if(res_OrLogicOP_0){
    
    res_macro_val = verde;
    }
    else{
    res_macro_val = verde;
    }
    return res_macro_val;
}



