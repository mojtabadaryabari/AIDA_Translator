// Codice del modello 'TestCase14', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
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
static inline bool L_P1__Guard13(instance_id_t const my_id)
{
    return true;
}


/*
    CNL corrispondente:
     
    {
    Nessuna
    }
*/
static inline bool L_P1__Guard14(instance_id_t const my_id)
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
static inline void L_P1__Effec13(instance_id_t const my_id)
{
    
}


/*
    CNL corrispondente:
     
    {
    Nessuna
    }
*/
static inline void L_P1__Effec14(instance_id_t const my_id)
{
    
}



// ********** Definizione metodi **********

// Metodi standard

void L_P1_C2_Init(instance_id_t const my_id)
{
    // init variabili di stato
    L_P1__SetStato3(my_id, C2_St_Stato);
    L_P1__SetSubcl21(my_id, false);
    L_P1__SetSubcl23(my_id, 0);
    L_P1__SetSubcl25(my_id, 0);
    L_P1__SetSubcl27(my_id, false);
    L_P1__SetSubcl29(my_id, false);
    L_P1__SetSubcl30(my_id, false);
    L_P1__SetSubcl31(my_id, false);
    L_P1__SetSubcl32(my_id, false);
    L_P1__SetSubcl33(my_id, 0);
    // init controlli precedenti
    L_P1__SetSubcl14(my_id, true);
    L_P1__SetSubcl16(my_id, false);
    L_P1__SetSubcl18(my_id, rossoverde);
    L_P1__SetSubcl20(my_id, rossogiallo3);
    // init Timer e Counter
    Timer_AggmInit(L_P1__GetSubcl34(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl34_ID);
    Timer_Init(L_P1__GetSubcl34(my_id), 321000);
    Timer_AggmInit(L_P1__GetSubcl35(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl35_ID);
    Timer_Init(L_P1__GetSubcl35(my_id), 321000);
    Timer_AggmInit(L_P1__GetSubcl36(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl36_ID);
    Timer_Init(L_P1__GetSubcl36(my_id), 5450000);
    Timer_AggmInit(L_P1__GetSubcl37(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl37_ID);
    Timer_Init(L_P1__GetSubcl37(my_id), 5450000);
    Timer_AggmInit(L_P1__GetSubcl38(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl38_ID);
    Timer_Init(L_P1__GetSubcl38(my_id), 103000);
    Timer_AggmInit(L_P1__GetSubcl39(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl39_ID);
    Timer_Init(L_P1__GetSubcl39(my_id), 332000);
    Timer_AggmInit(L_P1__GetSubcl40(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl40_ID);
    Timer_Init(L_P1__GetSubcl40(my_id), 314000);
    Timer_AggmInit(L_P1__GetSubcl41(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl41_ID);
    Timer_Init(L_P1__GetSubcl41(my_id), 45000);
    Counter_AggmInit(L_P1__GetSubcl42(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl42_ID);
    Counter_Init(L_P1__GetSubcl42(my_id));
    Counter_AggmInit(L_P1__GetSubcl43(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl43_ID);
    Counter_Init(L_P1__GetSubcl43(my_id));
    // init response
    L_P1_C2_SetResponse(my_id, LDS_SCHED_NOP);

    // transizione iniziale
    if(L_P1__Guard13(my_id)) {
        L_P1_C2_SetState(my_id, C2_St_state);
	L_P1__Effec13(my_id);
    } else {
        STOP_EXECUTION(LOGIC_ERROR);
    }
    // init variabili precedenti
    L_P1__SetSubcl22(my_id, L_P1__GetSubcl21(my_id));
    L_P1__SetSubcl24(my_id, L_P1__GetSubcl23(my_id));
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
            if (L_P1__Guard14(my_id)) {
                L_P1_C2_SetState(my_id, C2_St_state);
                L_P1__Effec14(my_id);				
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
    Timer_Exec(L_P1__GetSubcl34(my_id));
    Timer_Exec(L_P1__GetSubcl35(my_id));
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
    L_P1__SetOutSubcl(my_id, rossoverde);
    L_P1__SetOutSubcl1(my_id, c180x);
    L_P1__SetOutSubcl2(my_id, c75giallo);
    L_P1__SetOutSubcl3(my_id, rossogiallo3);
}

void L_P1_C2_GUpdatePrev(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C2(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C2(proc_id);
    L_P1__SetSubcl14(my_id, L_P1__GetInSubcl13(my_id));
    L_P1__SetSubcl16(my_id, L_P1__GetInSubcl15(my_id));
    L_P1__SetSubcl18(my_id, L_P1__GetInSubcl17(my_id));
    L_P1__SetSubcl20(my_id, L_P1__GetInSubcl19(my_id));
    L_P1__SetSubcl22(my_id, L_P1__GetSubcl21(my_id));
    L_P1__SetSubcl24(my_id, L_P1__GetSubcl23(my_id));
    L_P1__SetSubcl26(my_id, L_P1__GetSubcl25(my_id));
    L_P1__SetSubcl28(my_id, L_P1__GetSubcl27(my_id));
}

// ********** Definizione macro **********

// Macro di effetto

/*
    CNL corrispondente:
    
    { commento: {109,}  se il ripristino della variabile  SubClass_C2_restoreva_RV2 non è  uguale a  False , commento: {67,} Assegna alla variabile SubClass_C2_variabile_V4 il valore 5
    
       
    
    }
*/
void L_P1__Macro9(instance_id_t const my_id )
{
//  *109,*  se il ripristino della variabile  SubClass_C2_restoreva_RV2 non è  uguale a  False , *67,* Assegna alla variabile SubClass_C2_variabile_V4 il valore 5
    bool res_NotLogicOP_0 = true;
    res_NotLogicOP_0 = (res_NotLogicOP_0 && ! (L_P1__GetSubcl32(my_id) == false));
    if(res_NotLogicOP_0){
    
    L_P1__SetSubcl33(my_id,5u);
    }
}

/*
    CNL corrispondente:
     
    { commento: {35,}  se il controllo SubClass_C2_controllo_C7 è  diverso da  False , commento: {67,} Assegna alla variabile SubClass_C2_variabile_V4 il valore 9
    
       
      se il controllo ConsDef  è  uguale a FALSE ,  commento: {45,}  se  MainClass_C1_contatore_Co4 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  maggiore di  commento: {54,} 14, commento: {88,} quando  commento: {44,}    MainClass_C1_variabile_V8 del campo  MainClass_C1     commento: {105,} è  uguale a  commento: {53,} 7 commento: {38,} e  se il contatore SubClass_C2_contatore_Co6 è  minore di  commento: {55,} 1414 commento: {35,} e  se il controllo SubClass_C2_controllo_C7 non è  diverso da  False , commento: {72,}Azzera il contatore SubClass_C2_contatore_Co6
    
     ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V4 il valore 7
    
    
     commento: {37,}  se la variabile SubClass_C2_variabile_V4 non è  minore di  commento: {55,} 9 commento: {37,} e  se la variabile SubClass_C2_variabile_V4 non è  diverso da  commento: {56,} 10, commento: {72,}Azzera il contatore SubClass_C2_contatore_Co6
    
       
      se il ripristino dello stato  non è  diverso da  commento: {56,}  state1  commento: {107,} o  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} o  se il timer SubClass_C2_timer_T1 non è scaduto commento: {38,} o  se il contatore SubClass_C2_contatore_Co6 non è  minore di  commento: {55,} 1450 commento: {34,} o  se il parametro SubClass_C2_parametro_P5 non è  diverso da RossoVerde, commento: {72,}Azzera il contatore SubClass_C2_contatore_Co6
    
       
    
    }
*/
void L_P1__Macro10(instance_id_t const my_id )
{
//  *35,*  se il controllo SubClass_C2_controllo_C7 è  diverso da  False , *67,* Assegna alla variabile SubClass_C2_variabile_V4 il valore 9
    bool res_NotLogicOP_0 = true;
    res_NotLogicOP_0 = (res_NotLogicOP_0 && ! (L_P1__GetInSubcl8(my_id) == false));
    if(res_NotLogicOP_0){
    
    L_P1__SetSubcl33(my_id,9u);
    }
    //  se il controllo ConsDef  è  uguale a FALSE ,  *45,*  se  MainClass_C1_contatore_Co4 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  maggiore di  *54,* 14, *88,* quando  *44,*    MainClass_C1_variabile_V8 del campo  MainClass_C1     *105,* è  uguale a  *53,* 7 *38,* e  se il contatore SubClass_C2_contatore_Co6 è  minore di  *55,* 1414 *35,* e  se il controllo SubClass_C2_controllo_C7 non è  diverso da  False , *72,*Azzera il contatore SubClass_C2_contatore_Co6
    // ,altrimenti  *67,* Assegna alla variabile SubClass_C2_variabile_V4 il valore 7
    bool res_AndLogicOP_1 = true;
    bool res_AndLogicOP_2 = true;
    bool res_AndLogicOP_3 = true;
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (L_P1__GetInConsd1(my_id) == false));
    bool res_ForAllPredicate_4 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl9Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl9(my_id,i);
    bool res_ImpliesLogicOp_5 = true;
    if((L_P1__GetMainc35(it.mainc49) == 7u)){
    res_ImpliesLogicOp_5 = (res_ImpliesLogicOp_5 && (Counter_GetValore(L_P1__GetMainc48(it.mainc49)) > 14u));
    }
    res_ForAllPredicate_4 = res_ImpliesLogicOp_5;
    if(!res_ForAllPredicate_4) {break;}
    }
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_ForAllPredicate_4);
    
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_AndLogicOP_3);
    res_AndLogicOP_2 = (res_AndLogicOP_2 && (Counter_GetValore(L_P1__GetSubcl42(my_id)) < 1414u));
    
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_AndLogicOP_2);
    bool res_NotLogicOP_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetInSubcl8(my_id) == false));
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! res_NotLogicOP_7);
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_6);
    
    if(res_AndLogicOP_1){
    
    Counter_Res(L_P1__GetSubcl42(my_id));
    }else{
    
    L_P1__SetSubcl33(my_id,7u);
    }
    //  *37,*  se la variabile SubClass_C2_variabile_V4 non è  minore di  *55,* 9 *37,* e  se la variabile SubClass_C2_variabile_V4 non è  diverso da  *56,* 10, *72,*Azzera il contatore SubClass_C2_contatore_Co6
    bool res_AndLogicOP_8 = true;
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetSubcl33(my_id) < 9u));
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_9);
    bool res_NotLogicOP_10 = true;
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (L_P1__GetSubcl33(my_id) == 10u));
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! res_NotLogicOP_11);
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_10);
    
    if(res_AndLogicOP_8){
    
    Counter_Res(L_P1__GetSubcl42(my_id));
    }
    //  se il ripristino dello stato  non è  diverso da  *56,*  state1  *107,* o  se il controllo ConsDef  è  uguale a FALSE  *36,* o  se il timer SubClass_C2_timer_T1 non è scaduto *38,* o  se il contatore SubClass_C2_contatore_Co6 non è  minore di  *55,* 1450 *34,* o  se il parametro SubClass_C2_parametro_P5 non è  diverso da RossoVerde, *72,*Azzera il contatore SubClass_C2_contatore_Co6
    bool res_OrLogicOP_12 = false;
    bool res_OrLogicOP_13 = false;
    bool res_OrLogicOP_14 = false;
    bool res_OrLogicOP_15 = false;
    bool res_NotLogicOP_16 = true;
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! (L_P1__GetStato3(my_id) == C2_St_state));
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! res_NotLogicOP_17);
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_NotLogicOP_16);
    res_OrLogicOP_15 = (res_OrLogicOP_15 || (L_P1__GetInConsd1(my_id) == false));
    
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_OrLogicOP_15);
    bool res_NotLogicOP_18 = true;
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! Timer_Scaduto(L_P1__GetSubcl38(my_id)));
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_NotLogicOP_18);
    
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_OrLogicOP_14);
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (Counter_GetValore(L_P1__GetSubcl42(my_id)) < 1450u));
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_NotLogicOP_19);
    
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_OrLogicOP_13);
    bool res_NotLogicOP_20 = true;
    bool res_NotLogicOP_21 = true;
    res_NotLogicOP_21 = (res_NotLogicOP_21 && ! (L_P1__GetParamSubcl11(my_id) == rossoverde));
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! res_NotLogicOP_21);
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_NotLogicOP_20);
    
    if(res_OrLogicOP_12){
    
    Counter_Res(L_P1__GetSubcl42(my_id));
    }
}

/*
    CNL corrispondente:
    
    { commento: {43,}  se MainClass_C1_timer_T8 del campo  MainClass_C1 di SubClass_C2_lista_L3 è attivo commento: {35,} o  se il controllo SubClass_C2_controllo_C3 non è  diverso da  True , commento: {69,}Disattiva il timer SubClass_C2_timer_T7
    
     ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V4 il valore 4
    
    
     commento: {36,}  se il timer SubClass_C2_timer_T10 non è attivo,  commento: {43,}  se MainClass_C1_timer_T8 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  commento: {105,} è disattivo, commento: {88,} quando  commento: {43,}   MainClass_C1_timer_T8 del campo  MainClass_C1     commento: {105,} è disattivo commento: {35,} e  se il controllo SubClass_C2_controllo_C6 non è  uguale a RossoGiallo o  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro SubClass_C2_parametro_P5 è  diverso da RossoVerde commento: {37,} o  se la variabile SubClass_C2_variabile_V4 non è  maggiore di  commento: {54,} 3, commento: {71,}Decrementa il contatore SubClass_C2_contatore_Co7
    
     ,altrimenti  commento: {72,}Azzera il contatore SubClass_C2_contatore_Co6
    
    
     commento: {110,}  se il ripristino del timer  SubClass_C2_restoreTI_TI2 è disattivo commento: {38,} o  se il contatore SubClass_C2_contatore_Co7 non è  maggiore di  commento: {54,} 1345 commento: {34,} e  se il parametro SubClass_C2_parametro_P1 non è  uguale a RossoVerde commento: {38,} o  se il contatore SubClass_C2_contatore_Co7 è  minore di  commento: {55,} 1303 o  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} o  se il controllo SubClass_C2_controllo_C6 è  uguale a RossoGiallo,  Applica gli effetti
           della macro SubClass_C2_macroef_M10  commento: {73,}
    
     ,altrimenti  commento: {69,}Disattiva il timer SubClass_C2_timer_T10
    
    
     commento: {44,}  se  MainClass_C1_variabile_V5 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  commento: {105,} è  uguale a c270x commento: {38,} o  se il contatore SubClass_C2_contatore_Co6 non è  diverso da  commento: {56,} 12450 commento: {38,} e  se il contatore SubClass_C2_contatore_Co7 è  minore di  commento: {55,} 14 commento: {34,} o  se il parametro SubClass_C2_parametro_P7 non è  uguale a  False  commento: {37,} o  se la variabile SubClass_C2_variabile_V4 non è  diverso da  commento: {56,} 9 commento: {36,} o  se il timer SubClass_C2_timer_T1 non è attivo, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V4 il valore 5
    
     ,altrimenti  commento: {69,}Disattiva il timer SubClass_C2_timer_T10
    
    
     commento: {34,}  se il parametro SubClass_C2_parametro_P5 non è  uguale a RossoVerde commento: {38,} o  se il contatore SubClass_C2_contatore_Co6 è  maggiore di  commento: {54,} 1332 commento: {34,} o  se il parametro SubClass_C2_parametro_P1 è  uguale a RossoVerde commento: {37,} o  se la variabile SubClass_C2_variabile_V4 non è  diverso da  commento: {56,} 10 commento: {35,} o  se il controllo SubClass_C2_controllo_C6 è  uguale a RossoGiallo commento: {36,} e  se il timer SubClass_C2_timer_T10 non è scaduto, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V4 il valore 1
    
       
    
    }
*/
void L_P1__Macro11(instance_id_t const my_id )
{
//  *43,*  se MainClass_C1_timer_T8 del campo  MainClass_C1 di SubClass_C2_lista_L3 è attivo *35,* o  se il controllo SubClass_C2_controllo_C3 non è  diverso da  True , *69,*Disattiva il timer SubClass_C2_timer_T7
    // ,altrimenti  *67,* Assegna alla variabile SubClass_C2_variabile_V4 il valore 4
    bool res_OrLogicOP_0 = false;
    bool res_ForAllPredicate_1 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl9Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl9(my_id,i);
    bool res_ImpliesLogicOp_2 = true;
    res_ImpliesLogicOp_2 = (res_ImpliesLogicOp_2 && Timer_Attivo(L_P1__GetMainc46(it.mainc49)));
    res_ForAllPredicate_1 = res_ImpliesLogicOp_2;
    if(!res_ForAllPredicate_1) {break;}
    }
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_ForAllPredicate_1);
    bool res_NotLogicOP_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetInSubcl5(my_id) == true));
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! res_NotLogicOP_4);
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_3);
    
    if(res_OrLogicOP_0){
    
    Timer_Disattiva(L_P1__GetSubcl41(my_id));
    }else{
    
    L_P1__SetSubcl33(my_id,4u);
    }
    //  *36,*  se il timer SubClass_C2_timer_T10 non è attivo,  *43,*  se MainClass_C1_timer_T8 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  *105,* è disattivo, *88,* quando  *43,*   MainClass_C1_timer_T8 del campo  MainClass_C1     *105,* è disattivo *35,* e  se il controllo SubClass_C2_controllo_C6 non è  uguale a RossoGiallo o  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  *34,* e  se il parametro SubClass_C2_parametro_P5 è  diverso da RossoVerde *37,* o  se la variabile SubClass_C2_variabile_V4 non è  maggiore di  *54,* 3, *71,*Decrementa il contatore SubClass_C2_contatore_Co7
    // ,altrimenti  *72,*Azzera il contatore SubClass_C2_contatore_Co6
    bool res_OrLogicOP_5 = false;
    bool res_OrLogicOP_6 = false;
    bool res_OrLogicOP_7 = false;
    bool res_AndLogicOP_8 = true;
    bool res_AndLogicOP_9 = true;
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! Timer_Attivo(L_P1__GetSubcl39(my_id)));
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_NotLogicOP_10);
    bool res_ForAllPredicateNotEmpty_11 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl9Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl9(my_id,i);
    bool res_ImpliesLogicOp_12 = true;
    if(Timer_Disattivo(L_P1__GetMainc46(it.mainc49))){
    res_ImpliesLogicOp_12 = (res_ImpliesLogicOp_12 && Timer_Disattivo(L_P1__GetMainc46(it.mainc49)));
    res_ForAllPredicateNotEmpty_11 = res_ImpliesLogicOp_12;
    if(!res_ForAllPredicateNotEmpty_11) {break;}
    }
    }
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_ForAllPredicateNotEmpty_11);
    
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_AndLogicOP_9);
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (L_P1__GetInSubcl7(my_id) == rossogiallo3));
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_13);
    
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_AndLogicOP_8);
    res_OrLogicOP_7 = (res_OrLogicOP_7 || (L_P1__GetInConsd1(my_id) == false));
    
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_OrLogicOP_7);
    bool res_AndLogicOP_14 = true;
    res_AndLogicOP_14 = (res_AndLogicOP_14 && (L_P1__GetInConsd1(my_id) == false));
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (L_P1__GetParamSubcl11(my_id) == rossoverde));
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_NotLogicOP_15);
    
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_AndLogicOP_14);
    
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_OrLogicOP_6);
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (L_P1__GetSubcl33(my_id) > 3u));
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_NotLogicOP_16);
    
    if(res_OrLogicOP_5){
    
    Counter_Decr(L_P1__GetSubcl43(my_id));
    }else{
    
    Counter_Res(L_P1__GetSubcl42(my_id));
    }
    //  *110,*  se il ripristino del timer  SubClass_C2_restoreTI_TI2 è disattivo *38,* o  se il contatore SubClass_C2_contatore_Co7 non è  maggiore di  *54,* 1345 *34,* e  se il parametro SubClass_C2_parametro_P1 non è  uguale a RossoVerde *38,* o  se il contatore SubClass_C2_contatore_Co7 è  minore di  *55,* 1303 o  se il controllo ConsDef  è  uguale a FALSE  *35,* o  se il controllo SubClass_C2_controllo_C6 è  uguale a RossoGiallo,  Applica gli effetti
    //       della macro SubClass_C2_macroef_M10  *73,*
    // ,altrimenti  *69,*Disattiva il timer SubClass_C2_timer_T10
    bool res_OrLogicOP_17 = false;
    bool res_OrLogicOP_18 = false;
    bool res_OrLogicOP_19 = false;
    bool res_OrLogicOP_20 = false;
    res_OrLogicOP_20 = (res_OrLogicOP_20 || Timer_Disattivo(L_P1__GetSubcl37(my_id)));
    bool res_AndLogicOP_21 = true;
    bool res_NotLogicOP_22 = true;
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! (Counter_GetValore(L_P1__GetSubcl43(my_id)) > 1345u));
    res_AndLogicOP_21 = (res_AndLogicOP_21 && res_NotLogicOP_22);
    bool res_NotLogicOP_23 = true;
    res_NotLogicOP_23 = (res_NotLogicOP_23 && ! (L_P1__GetParamSubcl10(my_id) == rossoverde));
    res_AndLogicOP_21 = (res_AndLogicOP_21 && res_NotLogicOP_23);
    
    res_OrLogicOP_20 = (res_OrLogicOP_20 || res_AndLogicOP_21);
    
    res_OrLogicOP_19 = (res_OrLogicOP_19 || res_OrLogicOP_20);
    res_OrLogicOP_19 = (res_OrLogicOP_19 || (Counter_GetValore(L_P1__GetSubcl43(my_id)) < 1303u));
    
    res_OrLogicOP_18 = (res_OrLogicOP_18 || res_OrLogicOP_19);
    res_OrLogicOP_18 = (res_OrLogicOP_18 || (L_P1__GetInConsd1(my_id) == false));
    
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_OrLogicOP_18);
    res_OrLogicOP_17 = (res_OrLogicOP_17 || (L_P1__GetInSubcl7(my_id) == rossogiallo3));
    
    if(res_OrLogicOP_17){
    
    L_P1__Macro9(my_id);
    }else{
    
    Timer_Disattiva(L_P1__GetSubcl39(my_id));
    }
    //  *44,*  se  MainClass_C1_variabile_V5 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  *105,* è  uguale a c270x *38,* o  se il contatore SubClass_C2_contatore_Co6 non è  diverso da  *56,* 12450 *38,* e  se il contatore SubClass_C2_contatore_Co7 è  minore di  *55,* 14 *34,* o  se il parametro SubClass_C2_parametro_P7 non è  uguale a  False  *37,* o  se la variabile SubClass_C2_variabile_V4 non è  diverso da  *56,* 9 *36,* o  se il timer SubClass_C2_timer_T1 non è attivo, *67,* Assegna alla variabile SubClass_C2_variabile_V4 il valore 5
    // ,altrimenti  *69,*Disattiva il timer SubClass_C2_timer_T10
    bool res_OrLogicOP_24 = false;
    bool res_OrLogicOP_25 = false;
    bool res_OrLogicOP_26 = false;
    bool res_OrLogicOP_27 = false;
    bool res_ForAllPredicateNotEmpty_28 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl9Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl9(my_id,i);
    bool res_ImpliesLogicOp_29 = true;
    res_ImpliesLogicOp_29 = (res_ImpliesLogicOp_29 && (L_P1__GetMainc34(it.mainc49) == c270x));
    res_ForAllPredicateNotEmpty_28 = res_ImpliesLogicOp_29;
    if(!res_ForAllPredicateNotEmpty_28) {break;}
    }
    res_OrLogicOP_27 = (res_OrLogicOP_27 || res_ForAllPredicateNotEmpty_28);
    bool res_AndLogicOP_30 = true;
    bool res_NotLogicOP_31 = true;
    bool res_NotLogicOP_32 = true;
    res_NotLogicOP_32 = (res_NotLogicOP_32 && ! (Counter_GetValore(L_P1__GetSubcl42(my_id)) == 12450u));
    res_NotLogicOP_31 = (res_NotLogicOP_31 && ! res_NotLogicOP_32);
    res_AndLogicOP_30 = (res_AndLogicOP_30 && res_NotLogicOP_31);
    res_AndLogicOP_30 = (res_AndLogicOP_30 && (Counter_GetValore(L_P1__GetSubcl43(my_id)) < 14u));
    
    res_OrLogicOP_27 = (res_OrLogicOP_27 || res_AndLogicOP_30);
    
    res_OrLogicOP_26 = (res_OrLogicOP_26 || res_OrLogicOP_27);
    bool res_NotLogicOP_33 = true;
    res_NotLogicOP_33 = (res_NotLogicOP_33 && ! (L_P1__GetParamSubcl12(my_id) == false));
    res_OrLogicOP_26 = (res_OrLogicOP_26 || res_NotLogicOP_33);
    
    res_OrLogicOP_25 = (res_OrLogicOP_25 || res_OrLogicOP_26);
    bool res_NotLogicOP_34 = true;
    bool res_NotLogicOP_35 = true;
    res_NotLogicOP_35 = (res_NotLogicOP_35 && ! (L_P1__GetSubcl33(my_id) == 9u));
    res_NotLogicOP_34 = (res_NotLogicOP_34 && ! res_NotLogicOP_35);
    res_OrLogicOP_25 = (res_OrLogicOP_25 || res_NotLogicOP_34);
    
    res_OrLogicOP_24 = (res_OrLogicOP_24 || res_OrLogicOP_25);
    bool res_NotLogicOP_36 = true;
    res_NotLogicOP_36 = (res_NotLogicOP_36 && ! Timer_Attivo(L_P1__GetSubcl38(my_id)));
    res_OrLogicOP_24 = (res_OrLogicOP_24 || res_NotLogicOP_36);
    
    if(res_OrLogicOP_24){
    
    L_P1__SetSubcl33(my_id,5u);
    }else{
    
    Timer_Disattiva(L_P1__GetSubcl39(my_id));
    }
    //  *34,*  se il parametro SubClass_C2_parametro_P5 non è  uguale a RossoVerde *38,* o  se il contatore SubClass_C2_contatore_Co6 è  maggiore di  *54,* 1332 *34,* o  se il parametro SubClass_C2_parametro_P1 è  uguale a RossoVerde *37,* o  se la variabile SubClass_C2_variabile_V4 non è  diverso da  *56,* 10 *35,* o  se il controllo SubClass_C2_controllo_C6 è  uguale a RossoGiallo *36,* e  se il timer SubClass_C2_timer_T10 non è scaduto, *67,* Assegna alla variabile SubClass_C2_variabile_V4 il valore 1
    bool res_OrLogicOP_37 = false;
    bool res_OrLogicOP_38 = false;
    bool res_OrLogicOP_39 = false;
    bool res_OrLogicOP_40 = false;
    bool res_NotLogicOP_41 = true;
    res_NotLogicOP_41 = (res_NotLogicOP_41 && ! (L_P1__GetParamSubcl11(my_id) == rossoverde));
    res_OrLogicOP_40 = (res_OrLogicOP_40 || res_NotLogicOP_41);
    res_OrLogicOP_40 = (res_OrLogicOP_40 || (Counter_GetValore(L_P1__GetSubcl42(my_id)) > 1332u));
    
    res_OrLogicOP_39 = (res_OrLogicOP_39 || res_OrLogicOP_40);
    res_OrLogicOP_39 = (res_OrLogicOP_39 || (L_P1__GetParamSubcl10(my_id) == rossoverde));
    
    res_OrLogicOP_38 = (res_OrLogicOP_38 || res_OrLogicOP_39);
    bool res_NotLogicOP_42 = true;
    bool res_NotLogicOP_43 = true;
    res_NotLogicOP_43 = (res_NotLogicOP_43 && ! (L_P1__GetSubcl33(my_id) == 10u));
    res_NotLogicOP_42 = (res_NotLogicOP_42 && ! res_NotLogicOP_43);
    res_OrLogicOP_38 = (res_OrLogicOP_38 || res_NotLogicOP_42);
    
    res_OrLogicOP_37 = (res_OrLogicOP_37 || res_OrLogicOP_38);
    bool res_AndLogicOP_44 = true;
    res_AndLogicOP_44 = (res_AndLogicOP_44 && (L_P1__GetInSubcl7(my_id) == rossogiallo3));
    bool res_NotLogicOP_45 = true;
    res_NotLogicOP_45 = (res_NotLogicOP_45 && ! Timer_Scaduto(L_P1__GetSubcl39(my_id)));
    res_AndLogicOP_44 = (res_AndLogicOP_44 && res_NotLogicOP_45);
    
    res_OrLogicOP_37 = (res_OrLogicOP_37 || res_AndLogicOP_44);
    
    if(res_OrLogicOP_37){
    
    L_P1__SetSubcl33(my_id,1u);
    }
}


// Macro di verifica

/*
    CNL corrispondente:
     
    { commento: {63,} commento: {36,}  se il timer SubClass_C2_timer_T3 non è scaduto o  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro SubClass_C2_parametro_P1 non è  uguale a RossoVerde commento: {34,} e  se il parametro SubClass_C2_parametro_P5 non è  uguale a RossoVerde e  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} e  se il timer SubClass_C2_timer_T3 non è attivo, Solo una delle seguenti { 
     commento: {62,} commento: {38,}  se il contatore SubClass_C2_contatore_Co6 è  maggiore di  commento: {54,} 15321 commento: {35,} e  se il controllo SubClass_C2_controllo_C6 non è  diverso da RossoGiallo commento: {34,} o  se il parametro SubClass_C2_parametro_P1 è  diverso da RossoVerde commento: {38,} o  se il contatore SubClass_C2_contatore_Co7 non è  uguale a  commento: {53,} 15450 commento: {38,} e  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  commento: {56,} 13, Almeno una delle seguenti { 
     commento: {61,} commento: {110,}  se il ripristino del timer  SubClass_C2_restoreTI_TI1 non è scaduto commento: {37,} o  se la variabile SubClass_C2_variabile_V4 è  diverso da  commento: {56,} 7 commento: {37,} o  se la variabile SubClass_C2_variabile_V4 è  minore di  commento: {55,} 1 o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
      se il controllo ConsDef  è  uguale a FALSE  commento: {38,} o  se il contatore SubClass_C2_contatore_Co6 è  maggiore di  commento: {54,} 14321 commento: {36,} o  se il timer SubClass_C2_timer_T3 non è disattivo commento: {36,} o  se il timer SubClass_C2_timer_T10 è scaduto, Verifica che   commento: {47,}  commento: {34,}  il parametro SubClass_C2_parametro_P1 non sia  diverso da RossoVerde
    
    
     } Verifica che   commento: {47,}  commento: {34,}  il parametro SubClass_C2_parametro_P5 non sia  uguale a RossoVerde
     commento: {104,} o  che  commento: {34,}  il parametro SubClass_C2_parametro_P1 sia  uguale a RossoVerde
    
    
     } Verifica che   commento: {47,48,49,}  commento: {,}  il timer SubClass_C2_timer_T1 non sia attivo
     commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} o  che  commento: {34,}  il parametro SubClass_C2_parametro_P1 sia  uguale a RossoVerde
    
    
     } Verifica che   commento: {47,48,49,}  commento: {34,}  il parametro SubClass_C2_parametro_P1 sia  uguale a RossoVerde
     commento: {104,} o  che  commento: {,}  il timer SubClass_C2_timer_T1 sia disattivo
     commento: {104,} o  che  commento: {,}  il controllo SubClass_C2_controllo_C3 non sia  diverso da  True 
     commento: {104,} o  che  commento: {35,}  il controllo SubClass_C2_controllo_C6 sia  diverso da RossoGiallo
    
    
    }
*/
bool L_P1__Macro14(instance_id_t const my_id )
{
bool res_AndLogicOP_0 = true;
    
    //  *63,* *36,*  se il timer SubClass_C2_timer_T3 non è scaduto o  se il controllo ConsDef  è  uguale a FALSE  *34,* e  se il parametro SubClass_C2_parametro_P1 non è  uguale a RossoVerde *34,* e  se il parametro SubClass_C2_parametro_P5 non è  uguale a RossoVerde e  se il controllo ConsDef  è  uguale a FALSE  *36,* e  se il timer SubClass_C2_timer_T3 non è attivo, Solo una delle seguenti { 
    //   *62,* *38,*  se il contatore SubClass_C2_contatore_Co6 è  maggiore di  *54,* 15321 *35,* e  se il controllo SubClass_C2_controllo_C6 non è  diverso da RossoGiallo *34,* o  se il parametro SubClass_C2_parametro_P1 è  diverso da RossoVerde *38,* o  se il contatore SubClass_C2_contatore_Co7 non è  uguale a  *53,* 15450 *38,* e  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  *56,* 13, Almeno una delle seguenti { 
    //   *61,* *110,*  se il ripristino del timer  SubClass_C2_restoreTI_TI1 non è scaduto *37,* o  se la variabile SubClass_C2_variabile_V4 è  diverso da  *56,* 7 *37,* o  se la variabile SubClass_C2_variabile_V4 è  minore di  *55,* 1 o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
    //    se il controllo ConsDef  è  uguale a FALSE  *38,* o  se il contatore SubClass_C2_contatore_Co6 è  maggiore di  *54,* 14321 *36,* o  se il timer SubClass_C2_timer_T3 non è disattivo *36,* o  se il timer SubClass_C2_timer_T10 è scaduto, Verifica che   *47,*  *34,*  il parametro SubClass_C2_parametro_P1 non sia  diverso da RossoVerde
    //   } Verifica che   *47,*  *34,*  il parametro SubClass_C2_parametro_P5 non sia  uguale a RossoVerde
    //   *104,* o  che  *34,*  il parametro SubClass_C2_parametro_P1 sia  uguale a RossoVerde
    //   } Verifica che   *47,48,49,*  *,*  il timer SubClass_C2_timer_T1 non sia attivo
    //   *104,* o  che   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* o  che  *34,*  il parametro SubClass_C2_parametro_P1 sia  uguale a RossoVerde
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! Timer_Scaduto(L_P1__GetSubcl40(my_id)));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_3);
    bool res_AndLogicOP_4 = true;
    bool res_AndLogicOP_5 = true;
    bool res_AndLogicOP_6 = true;
    bool res_AndLogicOP_7 = true;
    res_AndLogicOP_7 = (res_AndLogicOP_7 && (L_P1__GetInConsd1(my_id) == false));
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetParamSubcl10(my_id) == rossoverde));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_8);
    
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_AndLogicOP_7);
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetParamSubcl11(my_id) == rossoverde));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_9);
    
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_AndLogicOP_6);
    res_AndLogicOP_5 = (res_AndLogicOP_5 && (L_P1__GetInConsd1(my_id) == false));
    
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_AndLogicOP_5);
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! Timer_Attivo(L_P1__GetSubcl40(my_id)));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_10);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_4);
    
    if(res_OrLogicOP_2){
    bool res_XorLogicOP_11 = true;
    int xorIndex_res_XorLogicOP_11 = 0;
    bool res_ImpliesLogicOp_12 = true;
    bool res_OrLogicOP_13 = false;
    bool res_OrLogicOP_14 = false;
    bool res_AndLogicOP_15 = true;
    res_AndLogicOP_15 = (res_AndLogicOP_15 && (Counter_GetValore(L_P1__GetSubcl42(my_id)) > 15321u));
    bool res_NotLogicOP_16 = true;
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! (L_P1__GetInSubcl7(my_id) == rossogiallo3));
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! res_NotLogicOP_17);
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_NotLogicOP_16);
    
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_AndLogicOP_15);
    bool res_NotLogicOP_18 = true;
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! (L_P1__GetParamSubcl10(my_id) == rossoverde));
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_NotLogicOP_18);
    
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_OrLogicOP_14);
    bool res_AndLogicOP_19 = true;
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! (Counter_GetValore(L_P1__GetSubcl43(my_id)) == 15450u));
    res_AndLogicOP_19 = (res_AndLogicOP_19 && res_NotLogicOP_20);
    bool res_NotLogicOP_21 = true;
    bool res_NotLogicOP_22 = true;
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! (Counter_GetValore(L_P1__GetSubcl43(my_id)) == 13u));
    res_NotLogicOP_21 = (res_NotLogicOP_21 && ! res_NotLogicOP_22);
    res_AndLogicOP_19 = (res_AndLogicOP_19 && res_NotLogicOP_21);
    
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_AndLogicOP_19);
    
    if(res_OrLogicOP_13){
    bool res_OrLogicOP_23 = false;
    bool res_ImpliesLogicOp_24 = true;
    bool res_OrLogicOP_25 = false;
    bool res_OrLogicOP_26 = false;
    bool res_OrLogicOP_27 = false;
    bool res_NotLogicOP_28 = true;
    res_NotLogicOP_28 = (res_NotLogicOP_28 && ! Timer_Scaduto(L_P1__GetSubcl35(my_id)));
    res_OrLogicOP_27 = (res_OrLogicOP_27 || res_NotLogicOP_28);
    bool res_NotLogicOP_29 = true;
    res_NotLogicOP_29 = (res_NotLogicOP_29 && ! (L_P1__GetSubcl33(my_id) == 7u));
    res_OrLogicOP_27 = (res_OrLogicOP_27 || res_NotLogicOP_29);
    
    res_OrLogicOP_26 = (res_OrLogicOP_26 || res_OrLogicOP_27);
    res_OrLogicOP_26 = (res_OrLogicOP_26 || (L_P1__GetSubcl33(my_id) < 1u));
    
    res_OrLogicOP_25 = (res_OrLogicOP_25 || res_OrLogicOP_26);
    res_OrLogicOP_25 = (res_OrLogicOP_25 || (L_P1__GetInConsd1(my_id) == false));
    
    if(res_OrLogicOP_25){
    bool res_ImpliesLogicOp_30 = true;
    bool res_OrLogicOP_31 = false;
    bool res_OrLogicOP_32 = false;
    bool res_OrLogicOP_33 = false;
    res_OrLogicOP_33 = (res_OrLogicOP_33 || (L_P1__GetInConsd1(my_id) == false));
    res_OrLogicOP_33 = (res_OrLogicOP_33 || (Counter_GetValore(L_P1__GetSubcl42(my_id)) > 14321u));
    
    res_OrLogicOP_32 = (res_OrLogicOP_32 || res_OrLogicOP_33);
    bool res_NotLogicOP_34 = true;
    res_NotLogicOP_34 = (res_NotLogicOP_34 && ! Timer_Disattivo(L_P1__GetSubcl40(my_id)));
    res_OrLogicOP_32 = (res_OrLogicOP_32 || res_NotLogicOP_34);
    
    res_OrLogicOP_31 = (res_OrLogicOP_31 || res_OrLogicOP_32);
    res_OrLogicOP_31 = (res_OrLogicOP_31 || Timer_Scaduto(L_P1__GetSubcl39(my_id)));
    
    if(res_OrLogicOP_31){
    bool res_NotLogicOP_35 = true;
    bool res_NotLogicOP_36 = true;
    res_NotLogicOP_36 = (res_NotLogicOP_36 && ! (L_P1__GetParamSubcl10(my_id) == rossoverde));
    res_NotLogicOP_35 = (res_NotLogicOP_35 && ! res_NotLogicOP_36);
    res_ImpliesLogicOp_30 = (res_ImpliesLogicOp_30 && res_NotLogicOP_35);
    }
    res_ImpliesLogicOp_24 = (res_ImpliesLogicOp_24 && res_ImpliesLogicOp_30);
    }
    res_OrLogicOP_23 = (res_OrLogicOP_23 || res_ImpliesLogicOp_24);
    bool res_OrLogicOP_37 = false;
    bool res_NotLogicOP_38 = true;
    res_NotLogicOP_38 = (res_NotLogicOP_38 && ! (L_P1__GetParamSubcl11(my_id) == rossoverde));
    res_OrLogicOP_37 = (res_OrLogicOP_37 || res_NotLogicOP_38);
    res_OrLogicOP_37 = (res_OrLogicOP_37 || (L_P1__GetParamSubcl10(my_id) == rossoverde));
    
    res_OrLogicOP_23 = (res_OrLogicOP_23 || res_OrLogicOP_37);
    
    res_ImpliesLogicOp_12 = (res_ImpliesLogicOp_12 && res_OrLogicOP_23);
    }
    if(res_ImpliesLogicOp_12){
    xorIndex_res_XorLogicOP_11 = (xorIndex_res_XorLogicOP_11 + 1);
    }
    bool res_OrLogicOP_39 = false;
    bool res_OrLogicOP_40 = false;
    bool res_NotLogicOP_41 = true;
    res_NotLogicOP_41 = (res_NotLogicOP_41 && ! Timer_Attivo(L_P1__GetSubcl38(my_id)));
    res_OrLogicOP_40 = (res_OrLogicOP_40 || res_NotLogicOP_41);
    res_OrLogicOP_40 = (res_OrLogicOP_40 || (L_P1__GetInConsd1(my_id) == false));
    
    res_OrLogicOP_39 = (res_OrLogicOP_39 || res_OrLogicOP_40);
    res_OrLogicOP_39 = (res_OrLogicOP_39 || (L_P1__GetParamSubcl10(my_id) == rossoverde));
    
    if(res_OrLogicOP_39){
    xorIndex_res_XorLogicOP_11 = (xorIndex_res_XorLogicOP_11 + 1);
    }
    
    res_XorLogicOP_11 = (res_XorLogicOP_11 && (xorIndex_res_XorLogicOP_11 == 1));
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_XorLogicOP_11);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *47,48,49,*  *34,*  il parametro SubClass_C2_parametro_P1 sia  uguale a RossoVerde
    //   *104,* o  che  *,*  il timer SubClass_C2_timer_T1 sia disattivo
    //   *104,* o  che  *,*  il controllo SubClass_C2_controllo_C3 non sia  diverso da  True 
    //   *104,* o  che  *35,*  il controllo SubClass_C2_controllo_C6 sia  diverso da RossoGiallo
    bool res_OrLogicOP_42 = false;
    bool res_OrLogicOP_43 = false;
    bool res_OrLogicOP_44 = false;
    res_OrLogicOP_44 = (res_OrLogicOP_44 || (L_P1__GetParamSubcl10(my_id) == rossoverde));
    res_OrLogicOP_44 = (res_OrLogicOP_44 || Timer_Disattivo(L_P1__GetSubcl38(my_id)));
    
    res_OrLogicOP_43 = (res_OrLogicOP_43 || res_OrLogicOP_44);
    bool res_NotLogicOP_45 = true;
    bool res_NotLogicOP_46 = true;
    res_NotLogicOP_46 = (res_NotLogicOP_46 && ! (L_P1__GetInSubcl5(my_id) == true));
    res_NotLogicOP_45 = (res_NotLogicOP_45 && ! res_NotLogicOP_46);
    res_OrLogicOP_43 = (res_OrLogicOP_43 || res_NotLogicOP_45);
    
    res_OrLogicOP_42 = (res_OrLogicOP_42 || res_OrLogicOP_43);
    bool res_NotLogicOP_47 = true;
    res_NotLogicOP_47 = (res_NotLogicOP_47 && ! (L_P1__GetInSubcl7(my_id) == rossogiallo3));
    res_OrLogicOP_42 = (res_OrLogicOP_42 || res_NotLogicOP_47);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_42);
    
    
    
    return res_AndLogicOP_0;
}


// Macro valorizzate

/*
    CNL corrispondente:
    
    { commento: {[} commento: {41,}  se MainClass_C1_parametro_P8 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  commento: {105,} è  diverso da RossoGialloVerde commento: {34,} e  se lo stato  è  diverso da  commento: {56,}  state1  commento: {106,} commento: {109,} o  se il ripristino della variabile  SubClass_C2_restoreva_RV1 non è  uguale a  True  commento: {35,} e  se il controllo SubClass_C2_controllo_C7 non è  diverso da  False ,  commento: {44,}  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  commento: {105,} è  uguale a  commento: {53,} 4, commento: {88,} quando  commento: {42,}    MainClass_C1_controllo_C1 del campo  MainClass_C1     è  diverso da RossoGialloxVerdex commento: {34,} e  se il parametro SubClass_C2_parametro_P1 è  uguale a RossoVerde commento: {42,} e  se  MainClass_C1_controllo_C10 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  diverso da RossoGialloxVerdex , assegna alla macro il valore  False 
    
     commento: {46,} assegna alla macro il valore  True  commento: {],}
    }
*/
bool L_P1__Macro12(instance_id_t const my_id , C2_Enumerat4 argom23, C2_Enumerat4 argom24, C2_Enumerat3 argom25, C2_Enumerat3 argom26, C2_Enumerat2 argom27, C2_Enumerat3 argom28, C2_Enumerat3 argom29)
{
bool res_macro_val;
    
    //  *[* *41,*  se MainClass_C1_parametro_P8 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  *105,* è  diverso da RossoGialloVerde *34,* e  se lo stato  è  diverso da  *56,*  state1  *106,* *109,* o  se il ripristino della variabile  SubClass_C2_restoreva_RV1 non è  uguale a  True  *35,* e  se il controllo SubClass_C2_controllo_C7 non è  diverso da  False ,  *44,*  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  *105,* è  uguale a  *53,* 4, *88,* quando  *42,*    MainClass_C1_controllo_C1 del campo  MainClass_C1     è  diverso da RossoGialloxVerdex *34,* e  se il parametro SubClass_C2_parametro_P1 è  uguale a RossoVerde *42,* e  se  MainClass_C1_controllo_C10 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  diverso da RossoGialloxVerdex
    bool res_OrLogicOP_0 = false;
    bool res_AndLogicOP_1 = true;
    bool res_ForAllPredicateNotEmpty_2 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl9Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl9(my_id,i);
    bool res_ImpliesLogicOp_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetParamMainc11(it.mainc49) == rossogiallo));
    res_ImpliesLogicOp_3 = (res_ImpliesLogicOp_3 && res_NotLogicOP_4);
    res_ForAllPredicateNotEmpty_2 = res_ImpliesLogicOp_3;
    if(!res_ForAllPredicateNotEmpty_2) {break;}
    }
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_ForAllPredicateNotEmpty_2);
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1_C2_GetState(my_id) == C2_St_state));
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_5);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_1);
    bool res_AndLogicOP_6 = true;
    bool res_AndLogicOP_7 = true;
    bool res_AndLogicOP_8 = true;
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetSubcl30(my_id) == true));
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_9);
    bool res_AndLogicOP_10 = true;
    bool res_NotLogicOP_11 = true;
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (L_P1__GetInSubcl8(my_id) == false));
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! res_NotLogicOP_12);
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_NotLogicOP_11);
    bool res_ForAllPredicateNotEmpty_13 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl9Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl9(my_id,i);
    bool res_ImpliesLogicOp_14 = true;
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (L_P1__GetInMainc5(it.mainc49) == rossogiallo1));
    if(res_NotLogicOP_15){
    res_ImpliesLogicOp_14 = (res_ImpliesLogicOp_14 && (L_P1__GetMainc35(it.mainc49) == 4u));
    res_ForAllPredicateNotEmpty_13 = res_ImpliesLogicOp_14;
    if(!res_ForAllPredicateNotEmpty_13) {break;}
    }
    }
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_ForAllPredicateNotEmpty_13);
    
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_AndLogicOP_10);
    
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_AndLogicOP_8);
    res_AndLogicOP_7 = (res_AndLogicOP_7 && (L_P1__GetParamSubcl10(my_id) == rossoverde));
    
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_AndLogicOP_7);
    bool res_ForAllPredicate_16 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl9Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl9(my_id,i);
    bool res_ImpliesLogicOp_17 = true;
    bool res_NotLogicOP_18 = true;
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! (L_P1__GetInMainc6(it.mainc49) == rossogiallo1));
    res_ImpliesLogicOp_17 = (res_ImpliesLogicOp_17 && res_NotLogicOP_18);
    res_ForAllPredicate_16 = res_ImpliesLogicOp_17;
    if(!res_ForAllPredicate_16) {break;}
    }
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_ForAllPredicate_16);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_6);
    
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
    
    { commento: {[} commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a  commento: {53,}  state1  , assegna alla macro il valore  True 
    
     commento: {46,} assegna alla macro il valore  False  commento: {],}
    }
*/
bool L_P1__Macro13(instance_id_t const my_id , C2_Enumerat4 argom30, C2_Enumerat4 argom31, C2_Enumerat1 argom32)
{
bool res_macro_val;
    
    //  lo stato del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a  *53,*  state1
    bool res_ForAllPredicate_0 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl9Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl9(my_id,i);
    bool res_ImpliesLogicOp_1 = true;
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && (L_P1_C1_GetState(it.mainc49) == C1_St_state));
    res_ForAllPredicate_0 = res_ImpliesLogicOp_1;
    if(!res_ForAllPredicate_0) {break;}
    }
    if(res_ForAllPredicate_0){
    
    res_macro_val = true;
    }
    else{
    res_macro_val = false;
    }
    return res_macro_val;
}



