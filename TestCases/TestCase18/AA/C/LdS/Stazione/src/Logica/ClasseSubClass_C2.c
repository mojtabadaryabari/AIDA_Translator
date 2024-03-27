// Codice del modello 'TestCase18', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#include "Logica/ClasseMainClass_C1.h"
#include "Logica/ClasseSubClass_C2.h"
#include "Logica/ClasseSubClass_C2_priv.h"
#include "config.h"
#include "scheduler.h"


// ********** Gestione comandi automatici **********

static size_t L_P1_C2_NumAutoCmds(instance_id_t const my_id)
{
    size_t n = 0u;
    if (L_P1__GetCAEvent2(my_id)) {
        ++n;
    }
    if (L_P1__GetCAEvent3(my_id)) {
        ++n;
    }
    if (L_P1__GetCAEvent4(my_id)) {
        ++n;
    }
    return n;
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
    L_P1__SetSubcl25(my_id, 0);
    L_P1__SetSubcl27(my_id, false);
    L_P1__SetSubcl29(my_id, false);
    L_P1__SetSubcl30(my_id, false);
    L_P1__SetSubcl31(my_id, rosso);
    L_P1__SetSubcl32(my_id, rosso);
    L_P1__SetSubcl33(my_id, 0);
    L_P1__SetSubcl34(my_id, 0);
    L_P1__SetSubcl35(my_id, false);
    L_P1__SetSubcl36(my_id, false);
    L_P1__SetSubcl37(my_id, c120);
    L_P1__SetSubcl38(my_id, false);
    L_P1__SetSubcl39(my_id, c270);
    // init controlli precedenti
    L_P1__SetSubcl16(my_id, true);
    L_P1__SetSubcl18(my_id, gialloverde);
    L_P1__SetSubcl20(my_id, false);
    L_P1__SetSubcl22(my_id, giallogiall);
    L_P1__SetSubcl24(my_id, spento);
    // init Timer e Counter
    Timer_AggmInit(L_P1__GetSubcl40(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl40_ID);
    Timer_Init(L_P1__GetSubcl40(my_id), 40413000);
    Timer_AggmInit(L_P1__GetSubcl41(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl41_ID);
    Timer_Init(L_P1__GetSubcl41(my_id), 40413000);
    Timer_AggmInit(L_P1__GetSubcl42(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl42_ID);
    Timer_Init(L_P1__GetSubcl42(my_id), 325000);
    Timer_AggmInit(L_P1__GetSubcl43(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl43_ID);
    Timer_Init(L_P1__GetSubcl43(my_id), 325000);
    Timer_AggmInit(L_P1__GetSubcl44(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl44_ID);
    Timer_Init(L_P1__GetSubcl44(my_id), 204000);
    Timer_AggmInit(L_P1__GetSubcl45(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl45_ID);
    Timer_Init(L_P1__GetSubcl45(my_id), 204000);
    Timer_AggmInit(L_P1__GetSubcl46(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl46_ID);
    Timer_Init(L_P1__GetSubcl46(my_id), 4000);
    Timer_AggmInit(L_P1__GetSubcl47(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl47_ID);
    Timer_Init(L_P1__GetSubcl47(my_id), 4000);
    Timer_AggmInit(L_P1__GetSubcl48(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl48_ID);
    Timer_Init(L_P1__GetSubcl48(my_id), 55000);
    Timer_AggmInit(L_P1__GetSubcl49(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl49_ID);
    Timer_Init(L_P1__GetSubcl49(my_id), 3000);
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
    L_P1__SetSubcl26(my_id, L_P1__GetSubcl25(my_id));
    L_P1__SetSubcl28(my_id, L_P1__GetSubcl27(my_id));
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
    Timer_Exec(L_P1__GetSubcl40(my_id));
    Timer_Exec(L_P1__GetSubcl41(my_id));
    Timer_Exec(L_P1__GetSubcl42(my_id));
    Timer_Exec(L_P1__GetSubcl43(my_id));
    Timer_Exec(L_P1__GetSubcl44(my_id));
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
    L_P1__SetOutSubcl(my_id, giallogiall);
    L_P1__SetOutSubcl1(my_id, giallogiall);
    L_P1__SetOutSubcl2(my_id, true);
}

void L_P1_C2_GUpdatePrev(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C2(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C2(proc_id);
    L_P1__SetSubcl16(my_id, L_P1__GetInSubcl15(my_id));
    L_P1__SetSubcl18(my_id, L_P1__GetInSubcl17(my_id));
    L_P1__SetSubcl20(my_id, L_P1__GetInSubcl19(my_id));
    L_P1__SetSubcl22(my_id, L_P1__GetInSubcl21(my_id));
    L_P1__SetSubcl24(my_id, L_P1__GetInSubcl23(my_id));
    L_P1__SetSubcl26(my_id, L_P1__GetSubcl25(my_id));
    L_P1__SetSubcl28(my_id, L_P1__GetSubcl27(my_id));
}

// ********** Definizione macro **********

// Macro di effetto

/*
    CNL corrispondente:
    
    { commento: {36,}  se il timer SubClass_C2_timer_T1 non è disattivo commento: {38,} o  se il contatore SubClass_C2_contatore_Co2 è  minore di  commento: {55,} 14, commento: {69,}Disattiva il timer SubClass_C2_timer_T1
    
     ,altrimenti  commento: {66,} Assegna al comando SubClass_C2_comando_C5 il valore GialloGiallo
    
    
     commento: {41,}  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  commento: {105,} è  maggiore di  commento: {54,} 5 commento: {38,} o  se il contatore SubClass_C2_contatore_Co8 non è  maggiore di  commento: {54,} 115 commento: {34,} e  se il parametro SubClass_C2_parametro_P6 è  diverso da  commento: {56,} 6, commento: {66,} Assegna al comando SubClass_C2_comando_C5 il valore GialloGiallo
    
     ,altrimenti   commento: {67,} Assegna alla variabile SubClass_C2_variabile_V10 il valore spento commento: {67,}
    
    
     commento: {44,}  se  MainClass_C1_variabile_V2 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  diverso da  commento: {56,} 10 commento: {37,} e  se la variabile SubClass_C2_variabile_V5 è  uguale a  False  commento: {36,} o  se il timer SubClass_C2_timer_T1 non è scaduto commento: {38,} e  se il contatore SubClass_C2_contatore_Co4 è  maggiore di  commento: {54,} 11 commento: {38,} e  se il contatore SubClass_C2_contatore_Co8 è  uguale a  commento: {53,} 12041, commento: {71,}Decrementa il contatore SubClass_C2_contatore_Co8
    
     ,altrimenti  commento: {69,}Disattiva il timer SubClass_C2_timer_T3
    
    
      se il controllo ConsDef  è  uguale a FALSE  commento: {38,} e  se il contatore SubClass_C2_contatore_Co4 è  maggiore di  commento: {54,} 1332 commento: {38,} e  se il contatore SubClass_C2_contatore_Co8 è  uguale a  commento: {53,} 155 commento: {34,} e  se il parametro SubClass_C2_parametro_P3 è  minore di  commento: {55,} 1, commento: {68,}Attiva il timer SubClass_C2_timer_T1
    
       
    
    }
*/
void L_P1__Macro13(instance_id_t const my_id )
{
//  *36,*  se il timer SubClass_C2_timer_T1 non è disattivo *38,* o  se il contatore SubClass_C2_contatore_Co2 è  minore di  *55,* 14, *69,*Disattiva il timer SubClass_C2_timer_T1
    // ,altrimenti  *66,* Assegna al comando SubClass_C2_comando_C5 il valore GialloGiallo
    bool res_OrLogicOP_0 = false;
    bool res_NotLogicOP_1 = true;
    res_NotLogicOP_1 = (res_NotLogicOP_1 && ! Timer_Disattivo(L_P1__GetSubcl48(my_id)));
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_1);
    res_OrLogicOP_0 = (res_OrLogicOP_0 || (Counter_GetValore(L_P1__GetSubcl50(my_id)) < 14u));
    
    if(res_OrLogicOP_0){
    
    Timer_Disattiva(L_P1__GetSubcl48(my_id));
    }else{
    
    L_P1__SetOutSubcl1(my_id,giallogiall);
    }
    //  *41,*  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  *105,* è  maggiore di  *54,* 5 *38,* o  se il contatore SubClass_C2_contatore_Co8 non è  maggiore di  *54,* 115 *34,* e  se il parametro SubClass_C2_parametro_P6 è  diverso da  *56,* 6, *66,* Assegna al comando SubClass_C2_comando_C5 il valore GialloGiallo
    // ,altrimenti   *67,* Assegna alla variabile SubClass_C2_variabile_V10 il valore spento
    bool res_OrLogicOP_2 = false;
    bool res_ForAllPredicateNotEmpty_3 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl9Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl9(my_id,i);
    bool res_ImpliesLogicOp_4 = true;
    res_ImpliesLogicOp_4 = (res_ImpliesLogicOp_4 && (L_P1__GetParamMainc9(it.mainc55) > 5u));
    res_ForAllPredicateNotEmpty_3 = res_ImpliesLogicOp_4;
    if(!res_ForAllPredicateNotEmpty_3) {break;}
    }
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_ForAllPredicateNotEmpty_3);
    bool res_AndLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (Counter_GetValore(L_P1__GetSubcl52(my_id)) > 115u));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_6);
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetParamSubcl13(my_id) == 6u));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_7);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_5);
    
    if(res_OrLogicOP_2){
    
    L_P1__SetOutSubcl1(my_id,giallogiall);
    }else{
    
    L_P1__SetSubcl37(my_id,spento);
    }
    //  *67,*
    // *44,*  se  MainClass_C1_variabile_V2 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  diverso da  *56,* 10 *37,* e  se la variabile SubClass_C2_variabile_V5 è  uguale a  False  *36,* o  se il timer SubClass_C2_timer_T1 non è scaduto *38,* e  se il contatore SubClass_C2_contatore_Co4 è  maggiore di  *54,* 11 *38,* e  se il contatore SubClass_C2_contatore_Co8 è  uguale a  *53,* 12041, *71,*Decrementa il contatore SubClass_C2_contatore_Co8
    // ,altrimenti  *69,*Disattiva il timer SubClass_C2_timer_T3
    bool res_OrLogicOP_8 = false;
    bool res_AndLogicOP_9 = true;
    bool res_ForAllPredicate_10 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl7Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl7(my_id,i);
    bool res_ImpliesLogicOp_11 = true;
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (L_P1__GetMainc37(it.mainc55) == 10u));
    res_ImpliesLogicOp_11 = (res_ImpliesLogicOp_11 && res_NotLogicOP_12);
    res_ForAllPredicate_10 = res_ImpliesLogicOp_11;
    if(!res_ForAllPredicate_10) {break;}
    }
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_ForAllPredicate_10);
    res_AndLogicOP_9 = (res_AndLogicOP_9 && (L_P1__GetSubcl38(my_id) == false));
    
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_AndLogicOP_9);
    bool res_AndLogicOP_13 = true;
    bool res_AndLogicOP_14 = true;
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! Timer_Scaduto(L_P1__GetSubcl48(my_id)));
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_NotLogicOP_15);
    res_AndLogicOP_14 = (res_AndLogicOP_14 && (Counter_GetValore(L_P1__GetSubcl51(my_id)) > 11u));
    
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_AndLogicOP_14);
    res_AndLogicOP_13 = (res_AndLogicOP_13 && (Counter_GetValore(L_P1__GetSubcl52(my_id)) == 12041u));
    
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_AndLogicOP_13);
    
    if(res_OrLogicOP_8){
    
    Counter_Decr(L_P1__GetSubcl52(my_id));
    }else{
    
    Timer_Disattiva(L_P1__GetSubcl49(my_id));
    }
    //  se il controllo ConsDef  è  uguale a FALSE  *38,* e  se il contatore SubClass_C2_contatore_Co4 è  maggiore di  *54,* 1332 *38,* e  se il contatore SubClass_C2_contatore_Co8 è  uguale a  *53,* 155 *34,* e  se il parametro SubClass_C2_parametro_P3 è  minore di  *55,* 1, *68,*Attiva il timer SubClass_C2_timer_T1
    bool res_AndLogicOP_16 = true;
    bool res_AndLogicOP_17 = true;
    bool res_AndLogicOP_18 = true;
    res_AndLogicOP_18 = (res_AndLogicOP_18 && (L_P1__GetInConsd1(my_id) == false));
    res_AndLogicOP_18 = (res_AndLogicOP_18 && (Counter_GetValore(L_P1__GetSubcl51(my_id)) > 1332u));
    
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_AndLogicOP_18);
    res_AndLogicOP_17 = (res_AndLogicOP_17 && (Counter_GetValore(L_P1__GetSubcl52(my_id)) == 155u));
    
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_AndLogicOP_17);
    res_AndLogicOP_16 = (res_AndLogicOP_16 && (L_P1__GetParamSubcl12(my_id) < 1u));
    
    if(res_AndLogicOP_16){
    
    Timer_Attiva(L_P1__GetSubcl48(my_id));
    }
}

/*
    CNL corrispondente:
    
    {  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro SubClass_C2_parametro_P3 non è  uguale a  commento: {53,} 4 commento: {34,} o  se il parametro SubClass_C2_parametro_P2 è  diverso da GialloGiallo commento: {37,} o  se la variabile SubClass_C2_variabile_V9 non è  diverso da c120x commento: {37,} o  se la variabile SubClass_C2_variabile_V10 non è  diverso da spento commento: {38,} o  se il contatore SubClass_C2_contatore_Co8 non è  diverso da  commento: {56,} 11, commento: {66,} Assegna al comando SubClass_C2_comando_C5 il valore GialloGiallo
    
       
     commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  commento: {105,} è  uguale a  commento: {53,}  state1  e  se il controllo ConsDef  è  uguale a FALSE , commento: {71,}Decrementa il contatore SubClass_C2_contatore_Co8
    
       
    
    }
*/
void L_P1__Macro14(instance_id_t const my_id )
{
//  se il controllo ConsDef  è  uguale a FALSE  *34,* e  se il parametro SubClass_C2_parametro_P3 non è  uguale a  *53,* 4 *34,* o  se il parametro SubClass_C2_parametro_P2 è  diverso da GialloGiallo *37,* o  se la variabile SubClass_C2_variabile_V9 non è  diverso da c120x *37,* o  se la variabile SubClass_C2_variabile_V10 non è  diverso da spento *38,* o  se il contatore SubClass_C2_contatore_Co8 non è  diverso da  *56,* 11, *66,* Assegna al comando SubClass_C2_comando_C5 il valore GialloGiallo
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_AndLogicOP_4 = true;
    res_AndLogicOP_4 = (res_AndLogicOP_4 && (L_P1__GetInConsd1(my_id) == false));
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetParamSubcl12(my_id) == 4u));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_5);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_AndLogicOP_4);
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetParamSubcl11(my_id) == giallogiall));
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_NotLogicOP_6);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    bool res_NotLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetSubcl39(my_id) == c120x));
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! res_NotLogicOP_8);
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_7);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_OrLogicOP_2);
    bool res_NotLogicOP_9 = true;
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__GetSubcl37(my_id) == spento));
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! res_NotLogicOP_10);
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_NotLogicOP_9);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_NotLogicOP_11 = true;
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (Counter_GetValore(L_P1__GetSubcl52(my_id)) == 11u));
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! res_NotLogicOP_12);
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_11);
    
    if(res_OrLogicOP_0){
    
    L_P1__SetOutSubcl1(my_id,giallogiall);
    }
    //  *111,*  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  *105,* è  uguale a  *53,*  state1  e  se il controllo ConsDef  è  uguale a FALSE , *71,*Decrementa il contatore SubClass_C2_contatore_Co8
    bool res_AndLogicOP_13 = true;
    bool res_ForAllPredicateNotEmpty_14 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl7Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl7(my_id,i);
    bool res_ImpliesLogicOp_15 = true;
    res_ImpliesLogicOp_15 = (res_ImpliesLogicOp_15 && (L_P1_C1_GetState(it.mainc55) == C1_St_state));
    res_ForAllPredicateNotEmpty_14 = res_ImpliesLogicOp_15;
    if(!res_ForAllPredicateNotEmpty_14) {break;}
    }
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_ForAllPredicateNotEmpty_14);
    res_AndLogicOP_13 = (res_AndLogicOP_13 && (L_P1__GetInConsd1(my_id) == false));
    
    if(res_AndLogicOP_13){
    
    Counter_Decr(L_P1__GetSubcl52(my_id));
    }
}

/*
    CNL corrispondente:
    
    { commento: {43,}  se MainClass_C1_timer_T5 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  commento: {105,} è disattivo commento: {34,} e  se il parametro SubClass_C2_parametro_P3 è  minore di  commento: {55,} 9 commento: {38,} o  se il contatore SubClass_C2_contatore_Co4 è  maggiore di  commento: {54,} 11 commento: {37,} e  se la variabile SubClass_C2_variabile_V9 non è  uguale a c120x commento: {35,} e  se il controllo SubClass_C2_controllo_C6 è  diverso da spento commento: {38,} e  se il contatore SubClass_C2_contatore_Co4 è  uguale a  commento: {53,} 13041, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V9 il valore c120x
    
     ,altrimenti   Applica gli effetti
           della macro SubClass_C2_macroef_M10  commento: {73,}
    
    
      se la macro  SubClass_C2_macrova_M1 ( con argomento_a2   uguale a True ,argomento_a4   uguale a c120x  e argomento_a3   uguale a GialloVerde )   è  diverso da c120x commento: {40,}  commento: {37,} o  se la variabile SubClass_C2_variabile_V9 non è  diverso da c120x, commento: {66,} Assegna al comando SubClass_C2_comando_C5 il valore GialloGiallo
    
       
     commento: {42,}  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  commento: {105,} è  diverso da avanzamento, commento: {71,}Decrementa il contatore SubClass_C2_contatore_Co8
    
     ,altrimenti   Applica gli effetti
           della macro SubClass_C2_macroef_M10  commento: {73,}
    
    
     commento: {34,}  se il parametro SubClass_C2_parametro_P7 è  minore di  commento: {55,} 5 commento: {38,} e  se il contatore SubClass_C2_contatore_Co4 è  minore di  commento: {55,} 1532, commento: {68,}Attiva il timer SubClass_C2_timer_T1
    
       
    
    }
*/
void L_P1__Macro15(instance_id_t const my_id )
{
//  *43,*  se MainClass_C1_timer_T5 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  *105,* è disattivo *34,* e  se il parametro SubClass_C2_parametro_P3 è  minore di  *55,* 9 *38,* o  se il contatore SubClass_C2_contatore_Co4 è  maggiore di  *54,* 11 *37,* e  se la variabile SubClass_C2_variabile_V9 non è  uguale a c120x *35,* e  se il controllo SubClass_C2_controllo_C6 è  diverso da spento *38,* e  se il contatore SubClass_C2_contatore_Co4 è  uguale a  *53,* 13041, *67,* Assegna alla variabile SubClass_C2_variabile_V9 il valore c120x
    // ,altrimenti   Applica gli effetti
    //       della macro SubClass_C2_macroef_M10
    bool res_OrLogicOP_0 = false;
    bool res_AndLogicOP_1 = true;
    bool res_ForAllPredicateNotEmpty_2 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl8Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl8(my_id,i);
    bool res_ImpliesLogicOp_3 = true;
    res_ImpliesLogicOp_3 = (res_ImpliesLogicOp_3 && Timer_Disattivo(L_P1__GetMainc51(it.mainc55)));
    res_ForAllPredicateNotEmpty_2 = res_ImpliesLogicOp_3;
    if(!res_ForAllPredicateNotEmpty_2) {break;}
    }
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_ForAllPredicateNotEmpty_2);
    res_AndLogicOP_1 = (res_AndLogicOP_1 && (L_P1__GetParamSubcl12(my_id) < 9u));
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_1);
    bool res_AndLogicOP_4 = true;
    bool res_AndLogicOP_5 = true;
    bool res_AndLogicOP_6 = true;
    res_AndLogicOP_6 = (res_AndLogicOP_6 && (Counter_GetValore(L_P1__GetSubcl51(my_id)) > 11u));
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetSubcl39(my_id) == c120x));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_7);
    
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_AndLogicOP_6);
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetInSubcl5(my_id) == spento));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_8);
    
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_AndLogicOP_5);
    res_AndLogicOP_4 = (res_AndLogicOP_4 && (Counter_GetValore(L_P1__GetSubcl51(my_id)) == 13041u));
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_4);
    
    if(res_OrLogicOP_0){
    
    L_P1__SetSubcl39(my_id,c120x);
    }else{
    
    L_P1__Macro13(my_id);
    }
    //  *73,*
    //  se la macro  SubClass_C2_macrova_M1 ( con argomento_a2   uguale a True ,argomento_a4   uguale a c120x  e argomento_a3   uguale a GialloVerde )   è  diverso da c120x *40,*  *37,* o  se la variabile SubClass_C2_variabile_V9 non è  diverso da c120x, *66,* Assegna al comando SubClass_C2_comando_C5 il valore GialloGiallo
    bool res_OrLogicOP_9 = false;
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__Macro18(my_id,true,gialloverde,c120x) == c120x));
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_NotLogicOP_10);
    bool res_NotLogicOP_11 = true;
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (L_P1__GetSubcl39(my_id) == c120x));
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! res_NotLogicOP_12);
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_NotLogicOP_11);
    
    if(res_OrLogicOP_9){
    
    L_P1__SetOutSubcl1(my_id,giallogiall);
    }
    //  *42,*  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  *105,* è  diverso da avanzamento, *71,*Decrementa il contatore SubClass_C2_contatore_Co8
    // ,altrimenti   Applica gli effetti
    //       della macro SubClass_C2_macroef_M10
    bool res_ForAllPredicateNotEmpty_13 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl7Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl7(my_id,i);
    bool res_ImpliesLogicOp_14 = true;
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (L_P1__GetInMainc4(it.mainc55) == avanzamento));
    res_ImpliesLogicOp_14 = (res_ImpliesLogicOp_14 && res_NotLogicOP_15);
    res_ForAllPredicateNotEmpty_13 = res_ImpliesLogicOp_14;
    if(!res_ForAllPredicateNotEmpty_13) {break;}
    }
    if(res_ForAllPredicateNotEmpty_13){
    
    Counter_Decr(L_P1__GetSubcl52(my_id));
    }else{
    
    L_P1__Macro13(my_id);
    }
    //  *73,*
    // *34,*  se il parametro SubClass_C2_parametro_P7 è  minore di  *55,* 5 *38,* e  se il contatore SubClass_C2_contatore_Co4 è  minore di  *55,* 1532, *68,*Attiva il timer SubClass_C2_timer_T1
    bool res_AndLogicOP_16 = true;
    res_AndLogicOP_16 = (res_AndLogicOP_16 && (L_P1__GetParamSubcl14(my_id) < 5u));
    res_AndLogicOP_16 = (res_AndLogicOP_16 && (Counter_GetValore(L_P1__GetSubcl51(my_id)) < 1532u));
    
    if(res_AndLogicOP_16){
    
    Timer_Attiva(L_P1__GetSubcl48(my_id));
    }
}

/*
    CNL corrispondente:
     
    { commento: {35,}  se il controllo SubClass_C2_controllo_C1 è  uguale a spento e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE , commento: {71,}Decrementa il contatore SubClass_C2_contatore_Co4
    
       
    
    }
*/
void L_P1__Macro16(instance_id_t const my_id )
{
//  *35,*  se il controllo SubClass_C2_controllo_C1 è  uguale a spento e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE , *71,*Decrementa il contatore SubClass_C2_contatore_Co4
    bool res_AndLogicOP_0 = true;
    bool res_AndLogicOP_1 = true;
    res_AndLogicOP_1 = (res_AndLogicOP_1 && (L_P1__GetInSubcl3(my_id) == spento));
    res_AndLogicOP_1 = (res_AndLogicOP_1 && (L_P1__GetInConsd1(my_id) == false));
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_AndLogicOP_1);
    res_AndLogicOP_0 = (res_AndLogicOP_0 && (L_P1__GetInConsd1(my_id) == false));
    
    if(res_AndLogicOP_0){
    
    Counter_Decr(L_P1__GetSubcl51(my_id));
    }
}

/*
    CNL corrispondente:
    
    { commento: {41,}  se MainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C2_lista_L6 è  uguale a avanzamentox o  se l'argomento argomento_af10 non  è  uguale a GialloVerde commento: {39,}  commento: {34,} o  se il parametro SubClass_C2_parametro_P3 è  diverso da  commento: {56,} 4, commento: {66,} Assegna al comando SubClass_C2_comando_C5 il valore GialloGiallo
    
     ,altrimenti  commento: {66,} Assegna al comando SubClass_C2_comando_C6 il valore  True 
    
    
    
    }
*/
void L_P1__Macro17(instance_id_t const my_id , C2_Enumerat4 argom27, C2_Enumerat1 argom28, C2_Enumerat3 argom29, C2_Enumerat4 argom30, bool argom31)
{
//  *41,*  se MainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C2_lista_L6 è  uguale a avanzamentox o  se l'argomento argomento_af10 non  è  uguale a GialloVerde *39,*  *34,* o  se il parametro SubClass_C2_parametro_P3 è  diverso da  *56,* 4, *66,* Assegna al comando SubClass_C2_comando_C5 il valore GialloGiallo
    // ,altrimenti  *66,* Assegna al comando SubClass_C2_comando_C6 il valore  True
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_ForAllPredicate_2 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl8Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl8(my_id,i);
    bool res_ImpliesLogicOp_3 = true;
    res_ImpliesLogicOp_3 = (res_ImpliesLogicOp_3 && (L_P1__GetParamMainc6(it.mainc55) == avanzamento1));
    res_ForAllPredicate_2 = res_ImpliesLogicOp_3;
    if(!res_ForAllPredicate_2) {break;}
    }
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_ForAllPredicate_2);
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (argom27 == gialloverde));
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_NotLogicOP_4);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetParamSubcl12(my_id) == 4u));
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_5);
    
    if(res_OrLogicOP_0){
    
    L_P1__SetOutSubcl1(my_id,giallogiall);
    }else{
    
    L_P1__SetOutSubcl2(my_id,true);
    }
}


// Macro di verifica

/*
    CNL corrispondente:
    
    { commento: {61,} commento: {34,}  se il parametro SubClass_C2_parametro_P10 è  uguale a spento,  commento: {43,}  se MainClass_C1_timer_T5 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  commento: {105,} è attivo, commento: {88,} quando  commento: {44,}    MainClass_C1_variabile_V8 del campo  MainClass_C1     commento: {105,} è  diverso da  commento: {56,} 2 commento: {35,} o  se il controllo SubClass_C2_controllo_C6 non è  uguale a spento commento: {34,} e  se il parametro SubClass_C2_parametro_P10 non è  diverso da spento, Tutte le seguenti { 
     commento: {44,}  se  MainClass_C1_variabile_V10 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  commento: {105,} è  uguale a  True  commento: {35,} o  se il controllo SubClass_C2_controllo_C6 non è  diverso da spento, Verifica che   commento: {47,49,50,52,}  commento: {,}  la variabile SubClass_C2_variabile_V10 non sia  uguale a spento
     commento: {104,} e  che   l'argomento argomento_ave7 sia  uguale a  False  commento: {,} 
     commento: {104,} o  che  commento: {,}  il timer SubClass_C2_timer_T3 non sia scaduto
     commento: {104,} o  che  commento: {34,}  il parametro SubClass_C2_parametro_P2 sia  uguale a GialloGiallo
    
    
     } Verifica che   commento: {47,48,52,}  commento: {34,}  il parametro SubClass_C2_parametro_P3 non sia  maggiore di  commento: {54,} 3
     commento: {104,} e  che  commento: {,}  il controllo SubClass_C2_controllo_C6 sia  diverso da spento
     commento: {104,} e  che   l'argomento argomento_ave10 sia  uguale a  False  commento: {,} 
    
    
    }
*/
bool L_P1__Macro21(instance_id_t const my_id , C2_Enumerat2 argom42, bool argom43, C2_Enumerat2 argom44, bool argom45, C2_Enumerat2 argom46, C2_Enumerat4 argom47)
{
bool res_AndLogicOP_0 = true;
    
    //  *61,* *34,*  se il parametro SubClass_C2_parametro_P10 è  uguale a spento,  *43,*  se MainClass_C1_timer_T5 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  *105,* è attivo, *88,* quando  *44,*    MainClass_C1_variabile_V8 del campo  MainClass_C1     *105,* è  diverso da  *56,* 2 *35,* o  se il controllo SubClass_C2_controllo_C6 non è  uguale a spento *34,* e  se il parametro SubClass_C2_parametro_P10 non è  diverso da spento, Tutte le seguenti { 
    //   *44,*  se  MainClass_C1_variabile_V10 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  *105,* è  uguale a  True  *35,* o  se il controllo SubClass_C2_controllo_C6 non è  diverso da spento, Verifica che   *47,49,50,52,*  *,*  la variabile SubClass_C2_variabile_V10 non sia  uguale a spento
    //   *104,* e  che   l'argomento argomento_ave7 sia  uguale a  False  *,* 
    //   *104,* o  che  *,*  il timer SubClass_C2_timer_T3 non sia scaduto
    //   *104,* o  che  *34,*  il parametro SubClass_C2_parametro_P2 sia  uguale a GialloGiallo
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_AndLogicOP_3 = true;
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (L_P1__GetParamSubcl10(my_id) == spento));
    bool res_ForAllPredicateNotEmpty_4 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl8Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl8(my_id,i);
    bool res_ImpliesLogicOp_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetMainc39(it.mainc55) == 2u));
    if(res_NotLogicOP_6){
    res_ImpliesLogicOp_5 = (res_ImpliesLogicOp_5 && Timer_Attivo(L_P1__GetMainc51(it.mainc55)));
    res_ForAllPredicateNotEmpty_4 = res_ImpliesLogicOp_5;
    if(!res_ForAllPredicateNotEmpty_4) {break;}
    }
    }
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_ForAllPredicateNotEmpty_4);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_3);
    bool res_AndLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetInSubcl5(my_id) == spento));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_8);
    bool res_NotLogicOP_9 = true;
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__GetParamSubcl10(my_id) == spento));
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! res_NotLogicOP_10);
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_9);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_7);
    
    if(res_OrLogicOP_2){
    bool res_ImpliesLogicOp_11 = true;
    bool res_OrLogicOP_12 = false;
    bool res_ForAllPredicateNotEmpty_13 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl8Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl8(my_id,i);
    bool res_ImpliesLogicOp_14 = true;
    res_ImpliesLogicOp_14 = (res_ImpliesLogicOp_14 && (L_P1__GetMainc36(it.mainc55) == true));
    res_ForAllPredicateNotEmpty_13 = res_ImpliesLogicOp_14;
    if(!res_ForAllPredicateNotEmpty_13) {break;}
    }
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_ForAllPredicateNotEmpty_13);
    bool res_NotLogicOP_15 = true;
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (L_P1__GetInSubcl5(my_id) == spento));
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! res_NotLogicOP_16);
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_NotLogicOP_15);
    
    if(res_OrLogicOP_12){
    bool res_OrLogicOP_17 = false;
    bool res_OrLogicOP_18 = false;
    bool res_AndLogicOP_19 = true;
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! (L_P1__GetSubcl37(my_id) == spento));
    res_AndLogicOP_19 = (res_AndLogicOP_19 && res_NotLogicOP_20);
    res_AndLogicOP_19 = (res_AndLogicOP_19 && (argom45 == false));
    
    res_OrLogicOP_18 = (res_OrLogicOP_18 || res_AndLogicOP_19);
    bool res_NotLogicOP_21 = true;
    res_NotLogicOP_21 = (res_NotLogicOP_21 && ! Timer_Scaduto(L_P1__GetSubcl49(my_id)));
    res_OrLogicOP_18 = (res_OrLogicOP_18 || res_NotLogicOP_21);
    
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_OrLogicOP_18);
    res_OrLogicOP_17 = (res_OrLogicOP_17 || (L_P1__GetParamSubcl11(my_id) == giallogiall));
    
    res_ImpliesLogicOp_11 = (res_ImpliesLogicOp_11 && res_OrLogicOP_17);
    }
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_ImpliesLogicOp_11);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *47,48,52,*  *34,*  il parametro SubClass_C2_parametro_P3 non sia  maggiore di  *54,* 3
    //   *104,* e  che  *,*  il controllo SubClass_C2_controllo_C6 sia  diverso da spento
    //   *104,* e  che   l'argomento argomento_ave10 sia  uguale a  False
    bool res_AndLogicOP_22 = true;
    bool res_AndLogicOP_23 = true;
    bool res_NotLogicOP_24 = true;
    res_NotLogicOP_24 = (res_NotLogicOP_24 && ! (L_P1__GetParamSubcl12(my_id) > 3u));
    res_AndLogicOP_23 = (res_AndLogicOP_23 && res_NotLogicOP_24);
    bool res_NotLogicOP_25 = true;
    res_NotLogicOP_25 = (res_NotLogicOP_25 && ! (L_P1__GetInSubcl5(my_id) == spento));
    res_AndLogicOP_23 = (res_AndLogicOP_23 && res_NotLogicOP_25);
    
    res_AndLogicOP_22 = (res_AndLogicOP_22 && res_AndLogicOP_23);
    res_AndLogicOP_22 = (res_AndLogicOP_22 && (argom43 == false));
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_AndLogicOP_22);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
    
    { commento: {63,} commento: {38,}  se il contatore SubClass_C2_contatore_Co8 è  diverso da  commento: {56,} 1532,  commento: {43,}  se MainClass_C1_timer_T5 del campo  MainClass_C1 di SubClass_C2_lista_L6 è attivo, commento: {88,} quando  commento: {41,}   MainClass_C1_parametro_P9 del campo  MainClass_C1     è  minore di  commento: {55,} 6 commento: {38,} o  se il contatore SubClass_C2_contatore_Co2 è  uguale a  commento: {53,} 13 commento: {36,} e  se il timer SubClass_C2_timer_T1 non è attivo o  se l'argomento argomento_ave5 è  diverso da c120x commento: {39,}  commento: {34,} e  se il parametro SubClass_C2_parametro_P2 non è  uguale a GialloGiallo commento: {37,} e  se la variabile SubClass_C2_variabile_V5 non è  uguale a  False , Solo una delle seguenti { 
     commento: {61,} commento: {34,}  se lo stato  è  uguale a  commento: {53,}  state1  commento: {106,} commento: {37,} e  se la variabile SubClass_C2_variabile_V5 è  diverso da  True  commento: {35,} o  se il controllo SubClass_C2_controllo_C6 è  uguale a spento commento: {35,} e  se il controllo SubClass_C2_controllo_C6 non è  diverso da spento commento: {34,} o  se il parametro SubClass_C2_parametro_P3 è  minore di  commento: {55,} 8, Tutte le seguenti { 
     commento: {45,}  se  MainClass_C1_contatore_Co5 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  commento: {105,} è  uguale a  commento: {53,} 12504 commento: {35,} o  se il controllo SubClass_C2_controllo_C4 è  uguale a spento commento: {35,} o  se il controllo SubClass_C2_controllo_C9 non è  diverso da  False  commento: {38,} o  se il contatore SubClass_C2_contatore_Co8 è  diverso da  commento: {56,} 121, Verifica che   commento: {49,51,52,}  commento: {,}  il timer SubClass_C2_timer_T3 non sia attivo
     commento: {104,} e  che  commento: {36,}  il timer SubClass_C2_timer_T1 sia attivo
     commento: {104,} e  che  commento: {,}  il contatore SubClass_C2_contatore_Co2 non sia  diverso da  commento: {56,} 153
     commento: {104,} o  che   l'argomento argomento_ave5 sia  uguale a c120x commento: {,} 
     commento: {104,} o  che   l'argomento argomento_ave5 non  sia  uguale a c120x commento: {39,} 
     commento: {104,} e  che   l'argomento argomento_ave5 sia  uguale a c120x commento: {39,} 
    
    
     } Verifica che   commento: {49,51,52,}  commento: {,}  il timer SubClass_C2_timer_T3 sia disattivo
     commento: {104,} o  che  commento: {,}  il contatore SubClass_C2_contatore_Co8 sia  diverso da  commento: {56,} 15
     commento: {104,} o  che   l'argomento argomento_ave5 non  sia  diverso da c120x commento: {,} 
     commento: {104,} o  che  commento: {36,}  il timer SubClass_C2_timer_T1 non sia scaduto
    
    
     } Verifica che   commento: {50,}  commento: {,}  la variabile SubClass_C2_variabile_V5 non sia  uguale a  True 
    
    
    }
*/
bool L_P1__Macro22(instance_id_t const my_id , C2_Enumerat4 argom48, C2_Enumerat2 argom49)
{
bool res_AndLogicOP_0 = true;
    
    //  *63,* *38,*  se il contatore SubClass_C2_contatore_Co8 è  diverso da  *56,* 1532,  *43,*  se MainClass_C1_timer_T5 del campo  MainClass_C1 di SubClass_C2_lista_L6 è attivo, *88,* quando  *41,*   MainClass_C1_parametro_P9 del campo  MainClass_C1     è  minore di  *55,* 6 *38,* o  se il contatore SubClass_C2_contatore_Co2 è  uguale a  *53,* 13 *36,* e  se il timer SubClass_C2_timer_T1 non è attivo o  se l'argomento argomento_ave5 è  diverso da c120x *39,*  *34,* e  se il parametro SubClass_C2_parametro_P2 non è  uguale a GialloGiallo *37,* e  se la variabile SubClass_C2_variabile_V5 non è  uguale a  False , Solo una delle seguenti { 
    //   *61,* *34,*  se lo stato  è  uguale a  *53,*  state1  *106,* *37,* e  se la variabile SubClass_C2_variabile_V5 è  diverso da  True  *35,* o  se il controllo SubClass_C2_controllo_C6 è  uguale a spento *35,* e  se il controllo SubClass_C2_controllo_C6 non è  diverso da spento *34,* o  se il parametro SubClass_C2_parametro_P3 è  minore di  *55,* 8, Tutte le seguenti { 
    //   *45,*  se  MainClass_C1_contatore_Co5 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  *105,* è  uguale a  *53,* 12504 *35,* o  se il controllo SubClass_C2_controllo_C4 è  uguale a spento *35,* o  se il controllo SubClass_C2_controllo_C9 non è  diverso da  False  *38,* o  se il contatore SubClass_C2_contatore_Co8 è  diverso da  *56,* 121, Verifica che   *49,51,52,*  *,*  il timer SubClass_C2_timer_T3 non sia attivo
    //   *104,* e  che  *36,*  il timer SubClass_C2_timer_T1 sia attivo
    //   *104,* e  che  *,*  il contatore SubClass_C2_contatore_Co2 non sia  diverso da  *56,* 153
    //   *104,* o  che   l'argomento argomento_ave5 sia  uguale a c120x *,* 
    //   *104,* o  che   l'argomento argomento_ave5 non  sia  uguale a c120x *39,* 
    //   *104,* e  che   l'argomento argomento_ave5 sia  uguale a c120x *39,* 
    //   } Verifica che   *49,51,52,*  *,*  il timer SubClass_C2_timer_T3 sia disattivo
    //   *104,* o  che  *,*  il contatore SubClass_C2_contatore_Co8 sia  diverso da  *56,* 15
    //   *104,* o  che   l'argomento argomento_ave5 non  sia  diverso da c120x *,* 
    //   *104,* o  che  *36,*  il timer SubClass_C2_timer_T1 non sia scaduto
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_AndLogicOP_4 = true;
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (Counter_GetValore(L_P1__GetSubcl52(my_id)) == 1532u));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_5);
    bool res_ForAllPredicate_6 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl8Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl8(my_id,i);
    bool res_ImpliesLogicOp_7 = true;
    if((L_P1__GetParamMainc9(it.mainc55) < 6u)){
    res_ImpliesLogicOp_7 = (res_ImpliesLogicOp_7 && Timer_Attivo(L_P1__GetMainc51(it.mainc55)));
    }
    res_ForAllPredicate_6 = res_ImpliesLogicOp_7;
    if(!res_ForAllPredicate_6) {break;}
    }
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_ForAllPredicate_6);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_AndLogicOP_4);
    bool res_AndLogicOP_8 = true;
    res_AndLogicOP_8 = (res_AndLogicOP_8 && (Counter_GetValore(L_P1__GetSubcl50(my_id)) == 13u));
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! Timer_Attivo(L_P1__GetSubcl48(my_id)));
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_9);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_AndLogicOP_8);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    bool res_AndLogicOP_10 = true;
    bool res_AndLogicOP_11 = true;
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (argom49 == c120x));
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_NotLogicOP_12);
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (L_P1__GetParamSubcl11(my_id) == giallogiall));
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_NotLogicOP_13);
    
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_AndLogicOP_11);
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1__GetSubcl38(my_id) == false));
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_NotLogicOP_14);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_10);
    
    if(res_OrLogicOP_2){
    bool res_XorLogicOP_15 = true;
    int xorIndex_res_XorLogicOP_15 = 0;
    bool res_ImpliesLogicOp_16 = true;
    bool res_OrLogicOP_17 = false;
    bool res_OrLogicOP_18 = false;
    bool res_AndLogicOP_19 = true;
    res_AndLogicOP_19 = (res_AndLogicOP_19 && (L_P1_C2_GetState(my_id) == C2_St_state));
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! (L_P1__GetSubcl38(my_id) == true));
    res_AndLogicOP_19 = (res_AndLogicOP_19 && res_NotLogicOP_20);
    
    res_OrLogicOP_18 = (res_OrLogicOP_18 || res_AndLogicOP_19);
    bool res_AndLogicOP_21 = true;
    res_AndLogicOP_21 = (res_AndLogicOP_21 && (L_P1__GetInSubcl5(my_id) == spento));
    bool res_NotLogicOP_22 = true;
    bool res_NotLogicOP_23 = true;
    res_NotLogicOP_23 = (res_NotLogicOP_23 && ! (L_P1__GetInSubcl5(my_id) == spento));
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! res_NotLogicOP_23);
    res_AndLogicOP_21 = (res_AndLogicOP_21 && res_NotLogicOP_22);
    
    res_OrLogicOP_18 = (res_OrLogicOP_18 || res_AndLogicOP_21);
    
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_OrLogicOP_18);
    res_OrLogicOP_17 = (res_OrLogicOP_17 || (L_P1__GetParamSubcl12(my_id) < 8u));
    
    if(res_OrLogicOP_17){
    bool res_ImpliesLogicOp_24 = true;
    bool res_OrLogicOP_25 = false;
    bool res_OrLogicOP_26 = false;
    bool res_OrLogicOP_27 = false;
    bool res_ForAllPredicateNotEmpty_28 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl8Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl8(my_id,i);
    bool res_ImpliesLogicOp_29 = true;
    res_ImpliesLogicOp_29 = (res_ImpliesLogicOp_29 && (Counter_GetValore(L_P1__GetMainc53(it.mainc55)) == 12504u));
    res_ForAllPredicateNotEmpty_28 = res_ImpliesLogicOp_29;
    if(!res_ForAllPredicateNotEmpty_28) {break;}
    }
    res_OrLogicOP_27 = (res_OrLogicOP_27 || res_ForAllPredicateNotEmpty_28);
    res_OrLogicOP_27 = (res_OrLogicOP_27 || (L_P1__GetInSubcl4(my_id) == spento));
    
    res_OrLogicOP_26 = (res_OrLogicOP_26 || res_OrLogicOP_27);
    bool res_NotLogicOP_30 = true;
    bool res_NotLogicOP_31 = true;
    res_NotLogicOP_31 = (res_NotLogicOP_31 && ! (L_P1__GetInSubcl6(my_id) == false));
    res_NotLogicOP_30 = (res_NotLogicOP_30 && ! res_NotLogicOP_31);
    res_OrLogicOP_26 = (res_OrLogicOP_26 || res_NotLogicOP_30);
    
    res_OrLogicOP_25 = (res_OrLogicOP_25 || res_OrLogicOP_26);
    bool res_NotLogicOP_32 = true;
    res_NotLogicOP_32 = (res_NotLogicOP_32 && ! (Counter_GetValore(L_P1__GetSubcl52(my_id)) == 121u));
    res_OrLogicOP_25 = (res_OrLogicOP_25 || res_NotLogicOP_32);
    
    if(res_OrLogicOP_25){
    bool res_OrLogicOP_33 = false;
    bool res_OrLogicOP_34 = false;
    bool res_AndLogicOP_35 = true;
    bool res_AndLogicOP_36 = true;
    bool res_NotLogicOP_37 = true;
    res_NotLogicOP_37 = (res_NotLogicOP_37 && ! Timer_Attivo(L_P1__GetSubcl49(my_id)));
    res_AndLogicOP_36 = (res_AndLogicOP_36 && res_NotLogicOP_37);
    res_AndLogicOP_36 = (res_AndLogicOP_36 && Timer_Attivo(L_P1__GetSubcl48(my_id)));
    
    res_AndLogicOP_35 = (res_AndLogicOP_35 && res_AndLogicOP_36);
    bool res_NotLogicOP_38 = true;
    bool res_NotLogicOP_39 = true;
    res_NotLogicOP_39 = (res_NotLogicOP_39 && ! (Counter_GetValore(L_P1__GetSubcl50(my_id)) == 153u));
    res_NotLogicOP_38 = (res_NotLogicOP_38 && ! res_NotLogicOP_39);
    res_AndLogicOP_35 = (res_AndLogicOP_35 && res_NotLogicOP_38);
    
    res_OrLogicOP_34 = (res_OrLogicOP_34 || res_AndLogicOP_35);
    res_OrLogicOP_34 = (res_OrLogicOP_34 || (argom49 == c120x));
    
    res_OrLogicOP_33 = (res_OrLogicOP_33 || res_OrLogicOP_34);
    bool res_AndLogicOP_40 = true;
    bool res_NotLogicOP_41 = true;
    res_NotLogicOP_41 = (res_NotLogicOP_41 && ! (argom49 == c120x));
    res_AndLogicOP_40 = (res_AndLogicOP_40 && res_NotLogicOP_41);
    res_AndLogicOP_40 = (res_AndLogicOP_40 && (argom49 == c120x));
    
    res_OrLogicOP_33 = (res_OrLogicOP_33 || res_AndLogicOP_40);
    
    res_ImpliesLogicOp_24 = (res_ImpliesLogicOp_24 && res_OrLogicOP_33);
    }
    res_ImpliesLogicOp_16 = (res_ImpliesLogicOp_16 && res_ImpliesLogicOp_24);
    }
    if(res_ImpliesLogicOp_16){
    xorIndex_res_XorLogicOP_15 = (xorIndex_res_XorLogicOP_15 + 1);
    }
    bool res_OrLogicOP_42 = false;
    bool res_OrLogicOP_43 = false;
    bool res_OrLogicOP_44 = false;
    res_OrLogicOP_44 = (res_OrLogicOP_44 || Timer_Disattivo(L_P1__GetSubcl49(my_id)));
    bool res_NotLogicOP_45 = true;
    res_NotLogicOP_45 = (res_NotLogicOP_45 && ! (Counter_GetValore(L_P1__GetSubcl52(my_id)) == 15u));
    res_OrLogicOP_44 = (res_OrLogicOP_44 || res_NotLogicOP_45);
    
    res_OrLogicOP_43 = (res_OrLogicOP_43 || res_OrLogicOP_44);
    bool res_NotLogicOP_46 = true;
    bool res_NotLogicOP_47 = true;
    res_NotLogicOP_47 = (res_NotLogicOP_47 && ! (argom49 == c120x));
    res_NotLogicOP_46 = (res_NotLogicOP_46 && ! res_NotLogicOP_47);
    res_OrLogicOP_43 = (res_OrLogicOP_43 || res_NotLogicOP_46);
    
    res_OrLogicOP_42 = (res_OrLogicOP_42 || res_OrLogicOP_43);
    bool res_NotLogicOP_48 = true;
    res_NotLogicOP_48 = (res_NotLogicOP_48 && ! Timer_Scaduto(L_P1__GetSubcl48(my_id)));
    res_OrLogicOP_42 = (res_OrLogicOP_42 || res_NotLogicOP_48);
    
    if(res_OrLogicOP_42){
    xorIndex_res_XorLogicOP_15 = (xorIndex_res_XorLogicOP_15 + 1);
    }
    
    res_XorLogicOP_15 = (res_XorLogicOP_15 && (xorIndex_res_XorLogicOP_15 == 1));
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_XorLogicOP_15);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *50,*  *,*  la variabile SubClass_C2_variabile_V5 non sia  uguale a  True
    bool res_NotLogicOP_49 = true;
    res_NotLogicOP_49 = (res_NotLogicOP_49 && ! (L_P1__GetSubcl38(my_id) == true));
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_NotLogicOP_49);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
    
    { commento: {62,} commento: {38,}  se il contatore SubClass_C2_contatore_Co8 non è  minore di  commento: {55,} 1325, Almeno una delle seguenti { 
     commento: {63,} commento: {34,}  se il parametro SubClass_C2_parametro_P6 non è  diverso da  commento: {56,} 2, Solo una delle seguenti { 
     commento: {62,} commento: {42,}  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  commento: {105,} è  uguale a avanzamento o  se l'argomento argomento_ave4 è  uguale a GialloGiallo commento: {39,}  commento: {37,} o  se la variabile SubClass_C2_variabile_V10 è  uguale a spento commento: {38,} e  se il contatore SubClass_C2_contatore_Co2 è  minore di  commento: {55,} 140 commento: {35,} e  se il controllo SubClass_C2_controllo_C1 non è  uguale a spento e  se l'argomento argomento_ave2 è  diverso da spento commento: {39,} , Almeno una delle seguenti { 
     commento: {62,} commento: {34,}  se il parametro SubClass_C2_parametro_P6 è  maggiore di  commento: {54,} 1 commento: {38,} o  se il contatore SubClass_C2_contatore_Co4 non è  uguale a  commento: {53,} 144132 commento: {36,} o  se il timer SubClass_C2_timer_T1 non è disattivo commento: {34,} e  se il parametro SubClass_C2_parametro_P3 è  minore di  commento: {55,} 10 commento: {34,} o  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  commento: {54,} 6, Almeno una delle seguenti { 
     commento: {61,} commento: {34,}  se il parametro SubClass_C2_parametro_P3 non è  diverso da  commento: {56,} 6 commento: {36,} e  se il timer SubClass_C2_timer_T3 non è scaduto commento: {36,} o  se il timer SubClass_C2_timer_T3 è scaduto commento: {36,} e  se il timer SubClass_C2_timer_T3 non è scaduto commento: {38,} e  se il contatore SubClass_C2_contatore_Co8 non è  diverso da  commento: {56,} 1250, Tutte le seguenti { 
     commento: {45,}  se  MainClass_C1_contatore_Co10 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  commento: {105,} è  minore di  commento: {55,} 11413 commento: {38,} o  se il contatore SubClass_C2_contatore_Co2 non è  minore di  commento: {55,} 152 commento: {34,} e  se il parametro SubClass_C2_parametro_P10 è  diverso da spento commento: {34,} o  se il parametro SubClass_C2_parametro_P2 è  diverso da GialloGiallo commento: {38,} e  se il contatore SubClass_C2_contatore_Co2 non è  minore di  commento: {55,} 135 commento: {34,} e  se il parametro SubClass_C2_parametro_P6 non è  diverso da  commento: {56,} 10, Verifica che   commento: {47,48,49,52,}   l'argomento argomento_ave2 sia  diverso da spento commento: {,} 
     commento: {104,} o  che  commento: {,}  il timer SubClass_C2_timer_T1 sia attivo
     commento: {104,} e  che  commento: {36,}  il timer SubClass_C2_timer_T3 non sia disattivo
     commento: {104,} o  che  commento: {,}  il controllo SubClass_C2_controllo_C6 sia  diverso da spento
     commento: {104,} e  che  commento: {34,}  il parametro SubClass_C2_parametro_P7 sia  maggiore di  commento: {54,} 10
     commento: {104,} o  che  commento: {34,}  il parametro SubClass_C2_parametro_P6 non sia  diverso da  commento: {56,} 10
    
    
     } Verifica che   commento: {47,50,51,52,}  commento: {,}  il contatore SubClass_C2_contatore_Co8 sia  uguale a  commento: {53,} 1103
     commento: {104,} e  che   l'argomento argomento_ave2 sia  diverso da spento commento: {,} 
     commento: {104,} e  che  commento: {,}  la variabile SubClass_C2_variabile_V10 sia  uguale a spento
     commento: {104,} o  che  commento: {37,}  la variabile SubClass_C2_variabile_V9 non sia  diverso da c120x
     commento: {104,} o  che  commento: {34,}  il parametro SubClass_C2_parametro_P3 non sia  minore di  commento: {55,} 6
     commento: {104,} e  che  commento: {38,}  il contatore SubClass_C2_contatore_Co8 sia  minore di  commento: {55,} 1
    
    
     } Verifica che   commento: {47,52,}  commento: {34,}  il parametro SubClass_C2_parametro_P3 sia  maggiore di  commento: {54,} 2
     commento: {104,} o  che   l'argomento argomento_ave2 sia  uguale a spento commento: {,} 
    
    
     } Verifica che   commento: {47,48,49,50,}  commento: {,}  il timer SubClass_C2_timer_T3 sia attivo
     commento: {104,} o  che  commento: {,}  il controllo SubClass_C2_controllo_C9 non sia  uguale a  True 
     commento: {104,} e  che  commento: {,}  la variabile SubClass_C2_variabile_V10 non sia  diverso da spento
     commento: {104,} o  che  commento: {34,}  il parametro SubClass_C2_parametro_P6 non sia  maggiore di  commento: {54,} 8
     commento: {104,} e  che  commento: {37,}  la variabile SubClass_C2_variabile_V10 sia  diverso da spento
    
    
     } Verifica che   commento: {50,52,}  commento: {,}  la variabile SubClass_C2_variabile_V10 non sia  diverso da spento
     commento: {104,} e  che  commento: {37,}  la variabile SubClass_C2_variabile_V9 non sia  uguale a c120x
     commento: {104,} o  che   l'argomento argomento_ave2 non  sia  diverso da spento commento: {,} 
    
    
     } Verifica che   commento: {47,49,}  commento: {,}  il timer SubClass_C2_timer_T3 non sia scaduto
     commento: {104,} e  che  commento: {34,}  il parametro SubClass_C2_parametro_P6 non sia  maggiore di  commento: {54,} 6
     commento: {104,} e  che  commento: {34,}  il parametro SubClass_C2_parametro_P7 non sia  minore di  commento: {55,} 3
     commento: {104,} e  che  commento: {36,}  il timer SubClass_C2_timer_T1 sia scaduto
     commento: {104,} o  che  commento: {36,}  il timer SubClass_C2_timer_T3 sia scaduto
    
    
    }
*/
bool L_P1__Macro23(instance_id_t const my_id , C2_Enumerat3 argom50, C2_Enumerat1 argom51)
{
bool res_AndLogicOP_0 = true;
    
    //  *62,* *38,*  se il contatore SubClass_C2_contatore_Co8 non è  minore di  *55,* 1325, Almeno una delle seguenti { 
    //   *63,* *34,*  se il parametro SubClass_C2_parametro_P6 non è  diverso da  *56,* 2, Solo una delle seguenti { 
    //   *62,* *42,*  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  *105,* è  uguale a avanzamento o  se l'argomento argomento_ave4 è  uguale a GialloGiallo *39,*  *37,* o  se la variabile SubClass_C2_variabile_V10 è  uguale a spento *38,* e  se il contatore SubClass_C2_contatore_Co2 è  minore di  *55,* 140 *35,* e  se il controllo SubClass_C2_controllo_C1 non è  uguale a spento e  se l'argomento argomento_ave2 è  diverso da spento *39,* , Almeno una delle seguenti { 
    //   *62,* *34,*  se il parametro SubClass_C2_parametro_P6 è  maggiore di  *54,* 1 *38,* o  se il contatore SubClass_C2_contatore_Co4 non è  uguale a  *53,* 144132 *36,* o  se il timer SubClass_C2_timer_T1 non è disattivo *34,* e  se il parametro SubClass_C2_parametro_P3 è  minore di  *55,* 10 *34,* o  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  *54,* 6, Almeno una delle seguenti { 
    //   *61,* *34,*  se il parametro SubClass_C2_parametro_P3 non è  diverso da  *56,* 6 *36,* e  se il timer SubClass_C2_timer_T3 non è scaduto *36,* o  se il timer SubClass_C2_timer_T3 è scaduto *36,* e  se il timer SubClass_C2_timer_T3 non è scaduto *38,* e  se il contatore SubClass_C2_contatore_Co8 non è  diverso da  *56,* 1250, Tutte le seguenti { 
    //   *45,*  se  MainClass_C1_contatore_Co10 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  *105,* è  minore di  *55,* 11413 *38,* o  se il contatore SubClass_C2_contatore_Co2 non è  minore di  *55,* 152 *34,* e  se il parametro SubClass_C2_parametro_P10 è  diverso da spento *34,* o  se il parametro SubClass_C2_parametro_P2 è  diverso da GialloGiallo *38,* e  se il contatore SubClass_C2_contatore_Co2 non è  minore di  *55,* 135 *34,* e  se il parametro SubClass_C2_parametro_P6 non è  diverso da  *56,* 10, Verifica che   *47,48,49,52,*   l'argomento argomento_ave2 sia  diverso da spento *,* 
    //   *104,* o  che  *,*  il timer SubClass_C2_timer_T1 sia attivo
    //   *104,* e  che  *36,*  il timer SubClass_C2_timer_T3 non sia disattivo
    //   *104,* o  che  *,*  il controllo SubClass_C2_controllo_C6 sia  diverso da spento
    //   *104,* e  che  *34,*  il parametro SubClass_C2_parametro_P7 sia  maggiore di  *54,* 10
    //   *104,* o  che  *34,*  il parametro SubClass_C2_parametro_P6 non sia  diverso da  *56,* 10
    //   } Verifica che   *47,50,51,52,*  *,*  il contatore SubClass_C2_contatore_Co8 sia  uguale a  *53,* 1103
    //   *104,* e  che   l'argomento argomento_ave2 sia  diverso da spento *,* 
    //   *104,* e  che  *,*  la variabile SubClass_C2_variabile_V10 sia  uguale a spento
    //   *104,* o  che  *37,*  la variabile SubClass_C2_variabile_V9 non sia  diverso da c120x
    //   *104,* o  che  *34,*  il parametro SubClass_C2_parametro_P3 non sia  minore di  *55,* 6
    //   *104,* e  che  *38,*  il contatore SubClass_C2_contatore_Co8 sia  minore di  *55,* 1
    //   } Verifica che   *47,52,*  *34,*  il parametro SubClass_C2_parametro_P3 sia  maggiore di  *54,* 2
    //   *104,* o  che   l'argomento argomento_ave2 sia  uguale a spento *,* 
    //   } Verifica che   *47,48,49,50,*  *,*  il timer SubClass_C2_timer_T3 sia attivo
    //   *104,* o  che  *,*  il controllo SubClass_C2_controllo_C9 non sia  uguale a  True 
    //   *104,* e  che  *,*  la variabile SubClass_C2_variabile_V10 non sia  diverso da spento
    //   *104,* o  che  *34,*  il parametro SubClass_C2_parametro_P6 non sia  maggiore di  *54,* 8
    //   *104,* e  che  *37,*  la variabile SubClass_C2_variabile_V10 sia  diverso da spento
    //   } Verifica che   *50,52,*  *,*  la variabile SubClass_C2_variabile_V10 non sia  diverso da spento
    //   *104,* e  che  *37,*  la variabile SubClass_C2_variabile_V9 non sia  uguale a c120x
    //   *104,* o  che   l'argomento argomento_ave2 non  sia  diverso da spento *,* 
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (Counter_GetValore(L_P1__GetSubcl52(my_id)) < 1325u));
    if(res_NotLogicOP_2){
    bool res_OrLogicOP_3 = false;
    bool res_ImpliesLogicOp_4 = true;
    bool res_NotLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetParamSubcl13(my_id) == 2u));
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! res_NotLogicOP_6);
    if(res_NotLogicOP_5){
    bool res_XorLogicOP_7 = true;
    int xorIndex_res_XorLogicOP_7 = 0;
    bool res_ImpliesLogicOp_8 = true;
    bool res_OrLogicOP_9 = false;
    bool res_OrLogicOP_10 = false;
    bool res_ForAllPredicateNotEmpty_11 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl8Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl8(my_id,i);
    bool res_ImpliesLogicOp_12 = true;
    res_ImpliesLogicOp_12 = (res_ImpliesLogicOp_12 && (L_P1__GetInMainc4(it.mainc55) == avanzamento));
    res_ForAllPredicateNotEmpty_11 = res_ImpliesLogicOp_12;
    if(!res_ForAllPredicateNotEmpty_11) {break;}
    }
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_ForAllPredicateNotEmpty_11);
    res_OrLogicOP_10 = (res_OrLogicOP_10 || (argom51 == giallogiall));
    
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_OrLogicOP_10);
    bool res_AndLogicOP_13 = true;
    bool res_AndLogicOP_14 = true;
    bool res_AndLogicOP_15 = true;
    res_AndLogicOP_15 = (res_AndLogicOP_15 && (L_P1__GetSubcl37(my_id) == spento));
    res_AndLogicOP_15 = (res_AndLogicOP_15 && (Counter_GetValore(L_P1__GetSubcl50(my_id)) < 140u));
    
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_AndLogicOP_15);
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (L_P1__GetInSubcl3(my_id) == spento));
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_NotLogicOP_16);
    
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_AndLogicOP_14);
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! (argom50 == spento));
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_NotLogicOP_17);
    
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_AndLogicOP_13);
    
    if(res_OrLogicOP_9){
    bool res_OrLogicOP_18 = false;
    bool res_ImpliesLogicOp_19 = true;
    bool res_OrLogicOP_20 = false;
    bool res_OrLogicOP_21 = false;
    bool res_OrLogicOP_22 = false;
    res_OrLogicOP_22 = (res_OrLogicOP_22 || (L_P1__GetParamSubcl13(my_id) > 1u));
    bool res_NotLogicOP_23 = true;
    res_NotLogicOP_23 = (res_NotLogicOP_23 && ! (Counter_GetValore(L_P1__GetSubcl51(my_id)) == 144132u));
    res_OrLogicOP_22 = (res_OrLogicOP_22 || res_NotLogicOP_23);
    
    res_OrLogicOP_21 = (res_OrLogicOP_21 || res_OrLogicOP_22);
    bool res_AndLogicOP_24 = true;
    bool res_NotLogicOP_25 = true;
    res_NotLogicOP_25 = (res_NotLogicOP_25 && ! Timer_Disattivo(L_P1__GetSubcl48(my_id)));
    res_AndLogicOP_24 = (res_AndLogicOP_24 && res_NotLogicOP_25);
    res_AndLogicOP_24 = (res_AndLogicOP_24 && (L_P1__GetParamSubcl12(my_id) < 10u));
    
    res_OrLogicOP_21 = (res_OrLogicOP_21 || res_AndLogicOP_24);
    
    res_OrLogicOP_20 = (res_OrLogicOP_20 || res_OrLogicOP_21);
    bool res_NotLogicOP_26 = true;
    res_NotLogicOP_26 = (res_NotLogicOP_26 && ! (L_P1__GetParamSubcl13(my_id) > 6u));
    res_OrLogicOP_20 = (res_OrLogicOP_20 || res_NotLogicOP_26);
    
    if(res_OrLogicOP_20){
    bool res_OrLogicOP_27 = false;
    bool res_ImpliesLogicOp_28 = true;
    bool res_OrLogicOP_29 = false;
    bool res_AndLogicOP_30 = true;
    bool res_NotLogicOP_31 = true;
    bool res_NotLogicOP_32 = true;
    res_NotLogicOP_32 = (res_NotLogicOP_32 && ! (L_P1__GetParamSubcl12(my_id) == 6u));
    res_NotLogicOP_31 = (res_NotLogicOP_31 && ! res_NotLogicOP_32);
    res_AndLogicOP_30 = (res_AndLogicOP_30 && res_NotLogicOP_31);
    bool res_NotLogicOP_33 = true;
    res_NotLogicOP_33 = (res_NotLogicOP_33 && ! Timer_Scaduto(L_P1__GetSubcl49(my_id)));
    res_AndLogicOP_30 = (res_AndLogicOP_30 && res_NotLogicOP_33);
    
    res_OrLogicOP_29 = (res_OrLogicOP_29 || res_AndLogicOP_30);
    bool res_AndLogicOP_34 = true;
    bool res_AndLogicOP_35 = true;
    res_AndLogicOP_35 = (res_AndLogicOP_35 && Timer_Scaduto(L_P1__GetSubcl49(my_id)));
    bool res_NotLogicOP_36 = true;
    res_NotLogicOP_36 = (res_NotLogicOP_36 && ! Timer_Scaduto(L_P1__GetSubcl49(my_id)));
    res_AndLogicOP_35 = (res_AndLogicOP_35 && res_NotLogicOP_36);
    
    res_AndLogicOP_34 = (res_AndLogicOP_34 && res_AndLogicOP_35);
    bool res_NotLogicOP_37 = true;
    bool res_NotLogicOP_38 = true;
    res_NotLogicOP_38 = (res_NotLogicOP_38 && ! (Counter_GetValore(L_P1__GetSubcl52(my_id)) == 1250u));
    res_NotLogicOP_37 = (res_NotLogicOP_37 && ! res_NotLogicOP_38);
    res_AndLogicOP_34 = (res_AndLogicOP_34 && res_NotLogicOP_37);
    
    res_OrLogicOP_29 = (res_OrLogicOP_29 || res_AndLogicOP_34);
    
    if(res_OrLogicOP_29){
    bool res_ImpliesLogicOp_39 = true;
    bool res_OrLogicOP_40 = false;
    bool res_OrLogicOP_41 = false;
    bool res_ForAllPredicateNotEmpty_42 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl8Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl8(my_id,i);
    bool res_ImpliesLogicOp_43 = true;
    res_ImpliesLogicOp_43 = (res_ImpliesLogicOp_43 && (Counter_GetValore(L_P1__GetMainc52(it.mainc55)) < 11413u));
    res_ForAllPredicateNotEmpty_42 = res_ImpliesLogicOp_43;
    if(!res_ForAllPredicateNotEmpty_42) {break;}
    }
    res_OrLogicOP_41 = (res_OrLogicOP_41 || res_ForAllPredicateNotEmpty_42);
    bool res_AndLogicOP_44 = true;
    bool res_NotLogicOP_45 = true;
    res_NotLogicOP_45 = (res_NotLogicOP_45 && ! (Counter_GetValore(L_P1__GetSubcl50(my_id)) < 152u));
    res_AndLogicOP_44 = (res_AndLogicOP_44 && res_NotLogicOP_45);
    bool res_NotLogicOP_46 = true;
    res_NotLogicOP_46 = (res_NotLogicOP_46 && ! (L_P1__GetParamSubcl10(my_id) == spento));
    res_AndLogicOP_44 = (res_AndLogicOP_44 && res_NotLogicOP_46);
    
    res_OrLogicOP_41 = (res_OrLogicOP_41 || res_AndLogicOP_44);
    
    res_OrLogicOP_40 = (res_OrLogicOP_40 || res_OrLogicOP_41);
    bool res_AndLogicOP_47 = true;
    bool res_AndLogicOP_48 = true;
    bool res_NotLogicOP_49 = true;
    res_NotLogicOP_49 = (res_NotLogicOP_49 && ! (L_P1__GetParamSubcl11(my_id) == giallogiall));
    res_AndLogicOP_48 = (res_AndLogicOP_48 && res_NotLogicOP_49);
    bool res_NotLogicOP_50 = true;
    res_NotLogicOP_50 = (res_NotLogicOP_50 && ! (Counter_GetValore(L_P1__GetSubcl50(my_id)) < 135u));
    res_AndLogicOP_48 = (res_AndLogicOP_48 && res_NotLogicOP_50);
    
    res_AndLogicOP_47 = (res_AndLogicOP_47 && res_AndLogicOP_48);
    bool res_NotLogicOP_51 = true;
    bool res_NotLogicOP_52 = true;
    res_NotLogicOP_52 = (res_NotLogicOP_52 && ! (L_P1__GetParamSubcl13(my_id) == 10u));
    res_NotLogicOP_51 = (res_NotLogicOP_51 && ! res_NotLogicOP_52);
    res_AndLogicOP_47 = (res_AndLogicOP_47 && res_NotLogicOP_51);
    
    res_OrLogicOP_40 = (res_OrLogicOP_40 || res_AndLogicOP_47);
    
    if(res_OrLogicOP_40){
    bool res_OrLogicOP_53 = false;
    bool res_OrLogicOP_54 = false;
    bool res_OrLogicOP_55 = false;
    bool res_NotLogicOP_56 = true;
    res_NotLogicOP_56 = (res_NotLogicOP_56 && ! (argom50 == spento));
    res_OrLogicOP_55 = (res_OrLogicOP_55 || res_NotLogicOP_56);
    bool res_AndLogicOP_57 = true;
    res_AndLogicOP_57 = (res_AndLogicOP_57 && Timer_Attivo(L_P1__GetSubcl48(my_id)));
    bool res_NotLogicOP_58 = true;
    res_NotLogicOP_58 = (res_NotLogicOP_58 && ! Timer_Disattivo(L_P1__GetSubcl49(my_id)));
    res_AndLogicOP_57 = (res_AndLogicOP_57 && res_NotLogicOP_58);
    
    res_OrLogicOP_55 = (res_OrLogicOP_55 || res_AndLogicOP_57);
    
    res_OrLogicOP_54 = (res_OrLogicOP_54 || res_OrLogicOP_55);
    bool res_AndLogicOP_59 = true;
    bool res_NotLogicOP_60 = true;
    res_NotLogicOP_60 = (res_NotLogicOP_60 && ! (L_P1__GetInSubcl5(my_id) == spento));
    res_AndLogicOP_59 = (res_AndLogicOP_59 && res_NotLogicOP_60);
    res_AndLogicOP_59 = (res_AndLogicOP_59 && (L_P1__GetParamSubcl14(my_id) > 10u));
    
    res_OrLogicOP_54 = (res_OrLogicOP_54 || res_AndLogicOP_59);
    
    res_OrLogicOP_53 = (res_OrLogicOP_53 || res_OrLogicOP_54);
    bool res_NotLogicOP_61 = true;
    bool res_NotLogicOP_62 = true;
    res_NotLogicOP_62 = (res_NotLogicOP_62 && ! (L_P1__GetParamSubcl13(my_id) == 10u));
    res_NotLogicOP_61 = (res_NotLogicOP_61 && ! res_NotLogicOP_62);
    res_OrLogicOP_53 = (res_OrLogicOP_53 || res_NotLogicOP_61);
    
    res_ImpliesLogicOp_39 = (res_ImpliesLogicOp_39 && res_OrLogicOP_53);
    }
    res_ImpliesLogicOp_28 = (res_ImpliesLogicOp_28 && res_ImpliesLogicOp_39);
    }
    res_OrLogicOP_27 = (res_OrLogicOP_27 || res_ImpliesLogicOp_28);
    bool res_OrLogicOP_63 = false;
    bool res_OrLogicOP_64 = false;
    bool res_AndLogicOP_65 = true;
    bool res_AndLogicOP_66 = true;
    res_AndLogicOP_66 = (res_AndLogicOP_66 && (Counter_GetValore(L_P1__GetSubcl52(my_id)) == 1103u));
    bool res_NotLogicOP_67 = true;
    res_NotLogicOP_67 = (res_NotLogicOP_67 && ! (argom50 == spento));
    res_AndLogicOP_66 = (res_AndLogicOP_66 && res_NotLogicOP_67);
    
    res_AndLogicOP_65 = (res_AndLogicOP_65 && res_AndLogicOP_66);
    res_AndLogicOP_65 = (res_AndLogicOP_65 && (L_P1__GetSubcl37(my_id) == spento));
    
    res_OrLogicOP_64 = (res_OrLogicOP_64 || res_AndLogicOP_65);
    bool res_NotLogicOP_68 = true;
    bool res_NotLogicOP_69 = true;
    res_NotLogicOP_69 = (res_NotLogicOP_69 && ! (L_P1__GetSubcl39(my_id) == c120x));
    res_NotLogicOP_68 = (res_NotLogicOP_68 && ! res_NotLogicOP_69);
    res_OrLogicOP_64 = (res_OrLogicOP_64 || res_NotLogicOP_68);
    
    res_OrLogicOP_63 = (res_OrLogicOP_63 || res_OrLogicOP_64);
    bool res_AndLogicOP_70 = true;
    bool res_NotLogicOP_71 = true;
    res_NotLogicOP_71 = (res_NotLogicOP_71 && ! (L_P1__GetParamSubcl12(my_id) < 6u));
    res_AndLogicOP_70 = (res_AndLogicOP_70 && res_NotLogicOP_71);
    res_AndLogicOP_70 = (res_AndLogicOP_70 && (Counter_GetValore(L_P1__GetSubcl52(my_id)) < 1u));
    
    res_OrLogicOP_63 = (res_OrLogicOP_63 || res_AndLogicOP_70);
    
    res_OrLogicOP_27 = (res_OrLogicOP_27 || res_OrLogicOP_63);
    
    res_ImpliesLogicOp_19 = (res_ImpliesLogicOp_19 && res_OrLogicOP_27);
    }
    res_OrLogicOP_18 = (res_OrLogicOP_18 || res_ImpliesLogicOp_19);
    bool res_OrLogicOP_72 = false;
    res_OrLogicOP_72 = (res_OrLogicOP_72 || (L_P1__GetParamSubcl12(my_id) > 2u));
    res_OrLogicOP_72 = (res_OrLogicOP_72 || (argom50 == spento));
    
    res_OrLogicOP_18 = (res_OrLogicOP_18 || res_OrLogicOP_72);
    
    res_ImpliesLogicOp_8 = (res_ImpliesLogicOp_8 && res_OrLogicOP_18);
    }
    if(res_ImpliesLogicOp_8){
    xorIndex_res_XorLogicOP_7 = (xorIndex_res_XorLogicOP_7 + 1);
    }
    bool res_OrLogicOP_73 = false;
    bool res_OrLogicOP_74 = false;
    res_OrLogicOP_74 = (res_OrLogicOP_74 || Timer_Attivo(L_P1__GetSubcl49(my_id)));
    bool res_AndLogicOP_75 = true;
    bool res_NotLogicOP_76 = true;
    res_NotLogicOP_76 = (res_NotLogicOP_76 && ! (L_P1__GetInSubcl6(my_id) == true));
    res_AndLogicOP_75 = (res_AndLogicOP_75 && res_NotLogicOP_76);
    bool res_NotLogicOP_77 = true;
    bool res_NotLogicOP_78 = true;
    res_NotLogicOP_78 = (res_NotLogicOP_78 && ! (L_P1__GetSubcl37(my_id) == spento));
    res_NotLogicOP_77 = (res_NotLogicOP_77 && ! res_NotLogicOP_78);
    res_AndLogicOP_75 = (res_AndLogicOP_75 && res_NotLogicOP_77);
    
    res_OrLogicOP_74 = (res_OrLogicOP_74 || res_AndLogicOP_75);
    
    res_OrLogicOP_73 = (res_OrLogicOP_73 || res_OrLogicOP_74);
    bool res_AndLogicOP_79 = true;
    bool res_NotLogicOP_80 = true;
    res_NotLogicOP_80 = (res_NotLogicOP_80 && ! (L_P1__GetParamSubcl13(my_id) > 8u));
    res_AndLogicOP_79 = (res_AndLogicOP_79 && res_NotLogicOP_80);
    bool res_NotLogicOP_81 = true;
    res_NotLogicOP_81 = (res_NotLogicOP_81 && ! (L_P1__GetSubcl37(my_id) == spento));
    res_AndLogicOP_79 = (res_AndLogicOP_79 && res_NotLogicOP_81);
    
    res_OrLogicOP_73 = (res_OrLogicOP_73 || res_AndLogicOP_79);
    
    if(res_OrLogicOP_73){
    xorIndex_res_XorLogicOP_7 = (xorIndex_res_XorLogicOP_7 + 1);
    }
    
    res_XorLogicOP_7 = (res_XorLogicOP_7 && (xorIndex_res_XorLogicOP_7 == 1));
    res_ImpliesLogicOp_4 = (res_ImpliesLogicOp_4 && res_XorLogicOP_7);
    }
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_ImpliesLogicOp_4);
    bool res_OrLogicOP_82 = false;
    bool res_AndLogicOP_83 = true;
    bool res_NotLogicOP_84 = true;
    bool res_NotLogicOP_85 = true;
    res_NotLogicOP_85 = (res_NotLogicOP_85 && ! (L_P1__GetSubcl37(my_id) == spento));
    res_NotLogicOP_84 = (res_NotLogicOP_84 && ! res_NotLogicOP_85);
    res_AndLogicOP_83 = (res_AndLogicOP_83 && res_NotLogicOP_84);
    bool res_NotLogicOP_86 = true;
    res_NotLogicOP_86 = (res_NotLogicOP_86 && ! (L_P1__GetSubcl39(my_id) == c120x));
    res_AndLogicOP_83 = (res_AndLogicOP_83 && res_NotLogicOP_86);
    
    res_OrLogicOP_82 = (res_OrLogicOP_82 || res_AndLogicOP_83);
    bool res_NotLogicOP_87 = true;
    bool res_NotLogicOP_88 = true;
    res_NotLogicOP_88 = (res_NotLogicOP_88 && ! (argom50 == spento));
    res_NotLogicOP_87 = (res_NotLogicOP_87 && ! res_NotLogicOP_88);
    res_OrLogicOP_82 = (res_OrLogicOP_82 || res_NotLogicOP_87);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_OrLogicOP_82);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_OrLogicOP_3);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *47,49,*  *,*  il timer SubClass_C2_timer_T3 non sia scaduto
    //   *104,* e  che  *34,*  il parametro SubClass_C2_parametro_P6 non sia  maggiore di  *54,* 6
    //   *104,* e  che  *34,*  il parametro SubClass_C2_parametro_P7 non sia  minore di  *55,* 3
    //   *104,* e  che  *36,*  il timer SubClass_C2_timer_T1 sia scaduto
    //   *104,* o  che  *36,*  il timer SubClass_C2_timer_T3 sia scaduto
    bool res_OrLogicOP_89 = false;
    bool res_AndLogicOP_90 = true;
    bool res_AndLogicOP_91 = true;
    bool res_AndLogicOP_92 = true;
    bool res_NotLogicOP_93 = true;
    res_NotLogicOP_93 = (res_NotLogicOP_93 && ! Timer_Scaduto(L_P1__GetSubcl49(my_id)));
    res_AndLogicOP_92 = (res_AndLogicOP_92 && res_NotLogicOP_93);
    bool res_NotLogicOP_94 = true;
    res_NotLogicOP_94 = (res_NotLogicOP_94 && ! (L_P1__GetParamSubcl13(my_id) > 6u));
    res_AndLogicOP_92 = (res_AndLogicOP_92 && res_NotLogicOP_94);
    
    res_AndLogicOP_91 = (res_AndLogicOP_91 && res_AndLogicOP_92);
    bool res_NotLogicOP_95 = true;
    res_NotLogicOP_95 = (res_NotLogicOP_95 && ! (L_P1__GetParamSubcl14(my_id) < 3u));
    res_AndLogicOP_91 = (res_AndLogicOP_91 && res_NotLogicOP_95);
    
    res_AndLogicOP_90 = (res_AndLogicOP_90 && res_AndLogicOP_91);
    res_AndLogicOP_90 = (res_AndLogicOP_90 && Timer_Scaduto(L_P1__GetSubcl48(my_id)));
    
    res_OrLogicOP_89 = (res_OrLogicOP_89 || res_AndLogicOP_90);
    res_OrLogicOP_89 = (res_OrLogicOP_89 || Timer_Scaduto(L_P1__GetSubcl49(my_id)));
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_89);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
     
    { commento: {63,}  se il controllo ConsDef  è  uguale a FALSE ,  commento: {43,}  se MainClass_C1_timer_T5 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  commento: {105,} è disattivo, commento: {88,} quando  commento: {42,}    MainClass_C1_controllo_C9 del campo  MainClass_C1     commento: {105,} è  uguale a avanzamento o  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro SubClass_C2_parametro_P3 è  diverso da  commento: {56,} 10, Solo una delle seguenti { 
     commento: {62,} commento: {34,}  se lo stato  non è  uguale a  commento: {53,}  state1  commento: {106,} commento: {35,} e  se il controllo SubClass_C2_controllo_C6 è  diverso da spento commento: {34,} o  se il parametro SubClass_C2_parametro_P3 è  uguale a  commento: {53,} 1 commento: {34,} e  se il parametro SubClass_C2_parametro_P6 è  uguale a  commento: {53,} 9 commento: {36,} e  se il timer SubClass_C2_timer_T1 non è disattivo commento: {35,} e  se il controllo SubClass_C2_controllo_C1 è  diverso da spento, Almeno una delle seguenti { 
     commento: {63,} commento: {44,}  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C2_lista_L6 è  diverso da c270xx commento: {36,} e  se il timer SubClass_C2_timer_T3 è scaduto commento: {38,} o  se il contatore SubClass_C2_contatore_Co2 è  minore di  commento: {55,} 1225 commento: {36,} e  se il timer SubClass_C2_timer_T1 non è scaduto commento: {35,} e  se il controllo SubClass_C2_controllo_C6 è  diverso da spento, Solo una delle seguenti { 
     commento: {41,}  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a  commento: {53,} 4 commento: {36,} o  se il timer SubClass_C2_timer_T3 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} o  se il timer SubClass_C2_timer_T3 è scaduto commento: {38,} e  se il contatore SubClass_C2_contatore_Co8 non è  diverso da  commento: {56,} 140413, Verifica che   commento: {48,}  commento: {,}  il controllo SubClass_C2_controllo_C6 sia  diverso da spento
    
    
     } Verifica che   commento: {47,51,}  commento: {34,}  il parametro SubClass_C2_parametro_P7 non sia  uguale a  commento: {53,} 4
     commento: {104,} o  che  commento: {,}  il contatore SubClass_C2_contatore_Co8 non sia  uguale a  commento: {53,} 122
    
    
     } Verifica che   commento: {49,}  commento: {,}  il timer SubClass_C2_timer_T3 non sia attivo
     commento: {104,} o  che  commento: {36,}  il timer SubClass_C2_timer_T1 non sia scaduto
    
    
     } Verifica che   commento: {50,}  commento: {,}  la variabile SubClass_C2_variabile_V5 non sia  uguale a  True 
    
    
    }
*/
bool L_P1__Macro24(instance_id_t const my_id )
{
bool res_AndLogicOP_0 = true;
    
    //  *63,*  se il controllo ConsDef  è  uguale a FALSE ,  *43,*  se MainClass_C1_timer_T5 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  *105,* è disattivo, *88,* quando  *42,*    MainClass_C1_controllo_C9 del campo  MainClass_C1     *105,* è  uguale a avanzamento o  se il controllo ConsDef  è  uguale a FALSE  *34,* e  se il parametro SubClass_C2_parametro_P3 è  diverso da  *56,* 10, Solo una delle seguenti { 
    //   *62,* *34,*  se lo stato  non è  uguale a  *53,*  state1  *106,* *35,* e  se il controllo SubClass_C2_controllo_C6 è  diverso da spento *34,* o  se il parametro SubClass_C2_parametro_P3 è  uguale a  *53,* 1 *34,* e  se il parametro SubClass_C2_parametro_P6 è  uguale a  *53,* 9 *36,* e  se il timer SubClass_C2_timer_T1 non è disattivo *35,* e  se il controllo SubClass_C2_controllo_C1 è  diverso da spento, Almeno una delle seguenti { 
    //   *63,* *44,*  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C2_lista_L6 è  diverso da c270xx *36,* e  se il timer SubClass_C2_timer_T3 è scaduto *38,* o  se il contatore SubClass_C2_contatore_Co2 è  minore di  *55,* 1225 *36,* e  se il timer SubClass_C2_timer_T1 non è scaduto *35,* e  se il controllo SubClass_C2_controllo_C6 è  diverso da spento, Solo una delle seguenti { 
    //   *41,*  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a  *53,* 4 *36,* o  se il timer SubClass_C2_timer_T3 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  *36,* o  se il timer SubClass_C2_timer_T3 è scaduto *38,* e  se il contatore SubClass_C2_contatore_Co8 non è  diverso da  *56,* 140413, Verifica che   *48,*  *,*  il controllo SubClass_C2_controllo_C6 sia  diverso da spento
    //   } Verifica che   *47,51,*  *34,*  il parametro SubClass_C2_parametro_P7 non sia  uguale a  *53,* 4
    //   *104,* o  che  *,*  il contatore SubClass_C2_contatore_Co8 non sia  uguale a  *53,* 122
    //   } Verifica che   *49,*  *,*  il timer SubClass_C2_timer_T3 non sia attivo
    //   *104,* o  che  *36,*  il timer SubClass_C2_timer_T1 non sia scaduto
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_AndLogicOP_3 = true;
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (L_P1__GetInConsd1(my_id) == false));
    bool res_ForAllPredicateNotEmpty_4 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl7Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl7(my_id,i);
    bool res_ImpliesLogicOp_5 = true;
    if((L_P1__GetInMainc4(it.mainc55) == avanzamento)){
    res_ImpliesLogicOp_5 = (res_ImpliesLogicOp_5 && Timer_Disattivo(L_P1__GetMainc51(it.mainc55)));
    res_ForAllPredicateNotEmpty_4 = res_ImpliesLogicOp_5;
    if(!res_ForAllPredicateNotEmpty_4) {break;}
    }
    }
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_ForAllPredicateNotEmpty_4);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_3);
    bool res_AndLogicOP_6 = true;
    res_AndLogicOP_6 = (res_AndLogicOP_6 && (L_P1__GetInConsd1(my_id) == false));
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetParamSubcl12(my_id) == 10u));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_7);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_6);
    
    if(res_OrLogicOP_2){
    bool res_XorLogicOP_8 = true;
    int xorIndex_res_XorLogicOP_8 = 0;
    bool res_ImpliesLogicOp_9 = true;
    bool res_OrLogicOP_10 = false;
    bool res_AndLogicOP_11 = true;
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (L_P1_C2_GetState(my_id) == C2_St_state));
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_NotLogicOP_12);
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (L_P1__GetInSubcl5(my_id) == spento));
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_NotLogicOP_13);
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_AndLogicOP_11);
    bool res_AndLogicOP_14 = true;
    bool res_AndLogicOP_15 = true;
    bool res_AndLogicOP_16 = true;
    res_AndLogicOP_16 = (res_AndLogicOP_16 && (L_P1__GetParamSubcl12(my_id) == 1u));
    res_AndLogicOP_16 = (res_AndLogicOP_16 && (L_P1__GetParamSubcl13(my_id) == 9u));
    
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_AndLogicOP_16);
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! Timer_Disattivo(L_P1__GetSubcl48(my_id)));
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_NotLogicOP_17);
    
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_AndLogicOP_15);
    bool res_NotLogicOP_18 = true;
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! (L_P1__GetInSubcl3(my_id) == spento));
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_NotLogicOP_18);
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_AndLogicOP_14);
    
    if(res_OrLogicOP_10){
    bool res_OrLogicOP_19 = false;
    bool res_ImpliesLogicOp_20 = true;
    bool res_OrLogicOP_21 = false;
    bool res_AndLogicOP_22 = true;
    bool res_ForAllPredicate_23 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl8Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl8(my_id,i);
    bool res_ImpliesLogicOp_24 = true;
    bool res_NotLogicOP_25 = true;
    res_NotLogicOP_25 = (res_NotLogicOP_25 && ! (L_P1__GetMainc38(it.mainc55) == c270xx));
    res_ImpliesLogicOp_24 = (res_ImpliesLogicOp_24 && res_NotLogicOP_25);
    res_ForAllPredicate_23 = res_ImpliesLogicOp_24;
    if(!res_ForAllPredicate_23) {break;}
    }
    res_AndLogicOP_22 = (res_AndLogicOP_22 && res_ForAllPredicate_23);
    res_AndLogicOP_22 = (res_AndLogicOP_22 && Timer_Scaduto(L_P1__GetSubcl49(my_id)));
    
    res_OrLogicOP_21 = (res_OrLogicOP_21 || res_AndLogicOP_22);
    bool res_AndLogicOP_26 = true;
    bool res_AndLogicOP_27 = true;
    res_AndLogicOP_27 = (res_AndLogicOP_27 && (Counter_GetValore(L_P1__GetSubcl50(my_id)) < 1225u));
    bool res_NotLogicOP_28 = true;
    res_NotLogicOP_28 = (res_NotLogicOP_28 && ! Timer_Scaduto(L_P1__GetSubcl48(my_id)));
    res_AndLogicOP_27 = (res_AndLogicOP_27 && res_NotLogicOP_28);
    
    res_AndLogicOP_26 = (res_AndLogicOP_26 && res_AndLogicOP_27);
    bool res_NotLogicOP_29 = true;
    res_NotLogicOP_29 = (res_NotLogicOP_29 && ! (L_P1__GetInSubcl5(my_id) == spento));
    res_AndLogicOP_26 = (res_AndLogicOP_26 && res_NotLogicOP_29);
    
    res_OrLogicOP_21 = (res_OrLogicOP_21 || res_AndLogicOP_26);
    
    if(res_OrLogicOP_21){
    bool res_ImpliesLogicOp_30 = true;
    bool res_OrLogicOP_31 = false;
    bool res_OrLogicOP_32 = false;
    bool res_ForAllPredicate_33 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl9Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl9(my_id,i);
    bool res_ImpliesLogicOp_34 = true;
    res_ImpliesLogicOp_34 = (res_ImpliesLogicOp_34 && (L_P1__GetParamMainc9(it.mainc55) == 4u));
    res_ForAllPredicate_33 = res_ImpliesLogicOp_34;
    if(!res_ForAllPredicate_33) {break;}
    }
    res_OrLogicOP_32 = (res_OrLogicOP_32 || res_ForAllPredicate_33);
    bool res_AndLogicOP_35 = true;
    bool res_NotLogicOP_36 = true;
    res_NotLogicOP_36 = (res_NotLogicOP_36 && ! Timer_Scaduto(L_P1__GetSubcl49(my_id)));
    res_AndLogicOP_35 = (res_AndLogicOP_35 && res_NotLogicOP_36);
    res_AndLogicOP_35 = (res_AndLogicOP_35 && (L_P1__GetInConsd1(my_id) == false));
    
    res_OrLogicOP_32 = (res_OrLogicOP_32 || res_AndLogicOP_35);
    
    res_OrLogicOP_31 = (res_OrLogicOP_31 || res_OrLogicOP_32);
    bool res_AndLogicOP_37 = true;
    res_AndLogicOP_37 = (res_AndLogicOP_37 && Timer_Scaduto(L_P1__GetSubcl49(my_id)));
    bool res_NotLogicOP_38 = true;
    bool res_NotLogicOP_39 = true;
    res_NotLogicOP_39 = (res_NotLogicOP_39 && ! (Counter_GetValore(L_P1__GetSubcl52(my_id)) == 140413u));
    res_NotLogicOP_38 = (res_NotLogicOP_38 && ! res_NotLogicOP_39);
    res_AndLogicOP_37 = (res_AndLogicOP_37 && res_NotLogicOP_38);
    
    res_OrLogicOP_31 = (res_OrLogicOP_31 || res_AndLogicOP_37);
    
    if(res_OrLogicOP_31){
    bool res_NotLogicOP_40 = true;
    res_NotLogicOP_40 = (res_NotLogicOP_40 && ! (L_P1__GetInSubcl5(my_id) == spento));
    res_ImpliesLogicOp_30 = (res_ImpliesLogicOp_30 && res_NotLogicOP_40);
    }
    res_ImpliesLogicOp_20 = (res_ImpliesLogicOp_20 && res_ImpliesLogicOp_30);
    }
    res_OrLogicOP_19 = (res_OrLogicOP_19 || res_ImpliesLogicOp_20);
    bool res_OrLogicOP_41 = false;
    bool res_NotLogicOP_42 = true;
    res_NotLogicOP_42 = (res_NotLogicOP_42 && ! (L_P1__GetParamSubcl14(my_id) == 4u));
    res_OrLogicOP_41 = (res_OrLogicOP_41 || res_NotLogicOP_42);
    bool res_NotLogicOP_43 = true;
    res_NotLogicOP_43 = (res_NotLogicOP_43 && ! (Counter_GetValore(L_P1__GetSubcl52(my_id)) == 122u));
    res_OrLogicOP_41 = (res_OrLogicOP_41 || res_NotLogicOP_43);
    
    res_OrLogicOP_19 = (res_OrLogicOP_19 || res_OrLogicOP_41);
    
    res_ImpliesLogicOp_9 = (res_ImpliesLogicOp_9 && res_OrLogicOP_19);
    }
    if(res_ImpliesLogicOp_9){
    xorIndex_res_XorLogicOP_8 = (xorIndex_res_XorLogicOP_8 + 1);
    }
    bool res_OrLogicOP_44 = false;
    bool res_NotLogicOP_45 = true;
    res_NotLogicOP_45 = (res_NotLogicOP_45 && ! Timer_Attivo(L_P1__GetSubcl49(my_id)));
    res_OrLogicOP_44 = (res_OrLogicOP_44 || res_NotLogicOP_45);
    bool res_NotLogicOP_46 = true;
    res_NotLogicOP_46 = (res_NotLogicOP_46 && ! Timer_Scaduto(L_P1__GetSubcl48(my_id)));
    res_OrLogicOP_44 = (res_OrLogicOP_44 || res_NotLogicOP_46);
    
    if(res_OrLogicOP_44){
    xorIndex_res_XorLogicOP_8 = (xorIndex_res_XorLogicOP_8 + 1);
    }
    
    res_XorLogicOP_8 = (res_XorLogicOP_8 && (xorIndex_res_XorLogicOP_8 == 1));
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_XorLogicOP_8);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *50,*  *,*  la variabile SubClass_C2_variabile_V5 non sia  uguale a  True
    bool res_NotLogicOP_47 = true;
    res_NotLogicOP_47 = (res_NotLogicOP_47 && ! (L_P1__GetSubcl38(my_id) == true));
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_NotLogicOP_47);
    
    
    
    return res_AndLogicOP_0;
}


// Macro valorizzate

/*
    CNL corrispondente:
    
    { commento: {[} commento: {110,}  se il ripristino del timer  SubClass_C2_restoreTI_TI1 non è attivo commento: {41,} o  se MainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  commento: {105,} è  uguale a avanzamentox commento: {44,} e  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a c270xx , assegna alla macro il valore c120x
    
     commento: {46,} assegna alla macro il valore c120x commento: {],}
    }
*/
C2_Enumerat2 L_P1__Macro18(instance_id_t const my_id , bool argom32, C2_Enumerat4 argom33, C2_Enumerat2 argom34)
{
C2_Enumerat2 res_macro_val;
    
    //  *[* *110,*  se il ripristino del timer  SubClass_C2_restoreTI_TI1 non è attivo *41,* o  se MainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  *105,* è  uguale a avanzamentox *44,* e  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a c270xx
    bool res_OrLogicOP_0 = false;
    bool res_NotLogicOP_1 = true;
    res_NotLogicOP_1 = (res_NotLogicOP_1 && ! Timer_Attivo(L_P1__GetSubcl41(my_id)));
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_1);
    bool res_AndLogicOP_2 = true;
    bool res_ForAllPredicateNotEmpty_3 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl8Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl8(my_id,i);
    bool res_ImpliesLogicOp_4 = true;
    res_ImpliesLogicOp_4 = (res_ImpliesLogicOp_4 && (L_P1__GetParamMainc6(it.mainc55) == avanzamento1));
    res_ForAllPredicateNotEmpty_3 = res_ImpliesLogicOp_4;
    if(!res_ForAllPredicateNotEmpty_3) {break;}
    }
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_ForAllPredicateNotEmpty_3);
    bool res_ForAllPredicate_5 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl7Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl7(my_id,i);
    bool res_ImpliesLogicOp_6 = true;
    res_ImpliesLogicOp_6 = (res_ImpliesLogicOp_6 && (L_P1__GetMainc38(it.mainc55) == c270xx));
    res_ForAllPredicate_5 = res_ImpliesLogicOp_6;
    if(!res_ForAllPredicate_5) {break;}
    }
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_ForAllPredicate_5);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_2);
    
    if(res_OrLogicOP_0){
    
    res_macro_val = c120x;
    }
    else{
    res_macro_val = c120x;
    }
    return res_macro_val;
}

/*
    CNL corrispondente:
    
    { commento: {[}
     commento: {46,} assegna alla macro il valore spento commento: {],}
    }
*/
C2_Enumerat3 L_P1__Macro19(instance_id_t const my_id , C2_Enumerat1 argom35, C2_Enumerat1 argom36, C2_Enumerat1 argom37, C2_Enumerat4 argom38, C2_Enumerat3 argom39, C2_Enumerat4 argom40, C2_Enumerat2 argom41)
{
return spento;
}

/*
    CNL corrispondente:
     
    { commento: {[}
     commento: {46,} assegna alla macro il valore  True  commento: {],}
    }
*/
bool L_P1__Macro20(instance_id_t const my_id )
{
return true;
}



