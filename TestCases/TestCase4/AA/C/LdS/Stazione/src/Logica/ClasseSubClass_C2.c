// Codice del modello 'TestCase4', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
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
    
     Nessuna  commento: {80,}
    }
*/
static inline bool L_P1__Guard3(instance_id_t const my_id)
{
    return true;
}


/*
    CNL corrispondente:
     {  Nessuna  }
*/
static inline bool L_P1__Guard4(instance_id_t const my_id)
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
    
     commento: {36,}  se il timer SubClass_C2_timer_T7 non è disattivo, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V7 il valore  True 
    
       
    
    }
*/
static inline void L_P1__Effec3(instance_id_t const my_id)
{
    
    //  *36,*  se il timer SubClass_C2_timer_T7 non è disattivo, *67,* Assegna alla variabile SubClass_C2_variabile_V7 il valore  True
    bool res_NotLogicOP_0 = true;
    res_NotLogicOP_0 = (res_NotLogicOP_0 && ! Timer_Disattivo(L_P1__GetSubcl49(my_id)));
    if(res_NotLogicOP_0){
    
    L_P1__SetSubcl37(my_id,true);
    }
}


/*
    CNL corrispondente:
     { commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L2 è  uguale a  commento: {53,}  state1  commento: {37,} o  se la variabile SubClass_C2_variabile_V10 non è  diverso da  commento: {56,} 6, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V7 il valore  False 
    
       
     }
*/
static inline void L_P1__Effec4(instance_id_t const my_id)
{
    
    //  *111,*  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L2 è  uguale a  *53,*  state1  *37,* o  se la variabile SubClass_C2_variabile_V10 non è  diverso da  *56,* 6, *67,* Assegna alla variabile SubClass_C2_variabile_V7 il valore  False
    bool res_OrLogicOP_0 = false;
    bool res_ForAllPredicate_1 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl9Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl9(my_id,i);
    bool res_ImpliesLogicOp_2 = true;
    res_ImpliesLogicOp_2 = (res_ImpliesLogicOp_2 && (L_P1_C1_GetState(it.mainc39) == C1_St_state));
    res_ForAllPredicate_1 = res_ImpliesLogicOp_2;
    if(!res_ForAllPredicate_1) {break;}
    }
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_ForAllPredicate_1);
    bool res_NotLogicOP_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetSubcl34(my_id) == 6u));
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! res_NotLogicOP_4);
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_3);
    
    if(res_OrLogicOP_0){
    
    L_P1__SetSubcl37(my_id,false);
    }
}



// ********** Definizione metodi **********

// Metodi standard

void L_P1_C2_Init(instance_id_t const my_id)
{
    // init variabili di stato
    L_P1__SetStato3(my_id, C2_St_Stato);
    L_P1__SetSubcl22(my_id, avanzamento);
    L_P1__SetSubcl24(my_id, 0);
    L_P1__SetSubcl26(my_id, avanzamento);
    L_P1__SetSubcl28(my_id, avanzamento);
    L_P1__SetSubcl29(my_id, avanzamento);
    L_P1__SetSubcl30(my_id, 0);
    L_P1__SetSubcl31(my_id, 0);
    L_P1__SetSubcl32(my_id, 0);
    L_P1__SetSubcl33(my_id, 0);
    L_P1__SetSubcl34(my_id, 0);
    L_P1__SetSubcl35(my_id, false);
    L_P1__SetSubcl36(my_id, giallogiall);
    L_P1__SetSubcl37(my_id, false);
    // init controlli precedenti
    L_P1__SetSubcl15(my_id, rossoverde);
    L_P1__SetSubcl17(my_id, rossoverde);
    L_P1__SetSubcl19(my_id, gialloverde);
    L_P1__SetSubcl21(my_id, c270);
    // init Timer e Counter
    Timer_AggmInit(L_P1__GetSubcl38(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl38_ID);
    Timer_Init(L_P1__GetSubcl38(my_id), 4245000);
    Timer_AggmInit(L_P1__GetSubcl39(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl39_ID);
    Timer_Init(L_P1__GetSubcl39(my_id), 4245000);
    Timer_AggmInit(L_P1__GetSubcl40(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl40_ID);
    Timer_Init(L_P1__GetSubcl40(my_id), 530000);
    Timer_AggmInit(L_P1__GetSubcl41(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl41_ID);
    Timer_Init(L_P1__GetSubcl41(my_id), 530000);
    Timer_AggmInit(L_P1__GetSubcl42(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl42_ID);
    Timer_Init(L_P1__GetSubcl42(my_id), 4124000);
    Timer_AggmInit(L_P1__GetSubcl43(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl43_ID);
    Timer_Init(L_P1__GetSubcl43(my_id), 4124000);
    Timer_AggmInit(L_P1__GetSubcl44(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl44_ID);
    Timer_Init(L_P1__GetSubcl44(my_id), 1000);
    Timer_AggmInit(L_P1__GetSubcl45(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl45_ID);
    Timer_Init(L_P1__GetSubcl45(my_id), 1000);
    Timer_AggmInit(L_P1__GetSubcl46(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl46_ID);
    Timer_Init(L_P1__GetSubcl46(my_id), 25000);
    Timer_AggmInit(L_P1__GetSubcl47(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl47_ID);
    Timer_Init(L_P1__GetSubcl47(my_id), 25000);
    Timer_AggmInit(L_P1__GetSubcl48(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl48_ID);
    Timer_Init(L_P1__GetSubcl48(my_id), 53000);
    Timer_AggmInit(L_P1__GetSubcl49(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl49_ID);
    Timer_Init(L_P1__GetSubcl49(my_id), 101000);
    Counter_AggmInit(L_P1__GetSubcl50(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl50_ID);
    Counter_Init(L_P1__GetSubcl50(my_id));
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
    L_P1__SetSubcl23(my_id, L_P1__GetSubcl22(my_id));
    L_P1__SetSubcl25(my_id, L_P1__GetSubcl24(my_id));
    L_P1__SetSubcl27(my_id, L_P1__GetSubcl26(my_id));
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
            if (L_P1__Guard4(my_id)) {
                L_P1_C2_SetState(my_id, C2_St_state);
                L_P1__Effec4(my_id);				
            }
            else if (L_P1__Guard3(my_id)) {
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
    Timer_Exec(L_P1__GetSubcl38(my_id));
    Timer_Exec(L_P1__GetSubcl39(my_id));
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
    L_P1__SetOutSubcl(my_id, true);
    L_P1__SetOutSubcl1(my_id, true);
    L_P1__SetOutSubcl2(my_id, false);
    L_P1__SetOutSubcl3(my_id, c270);
    L_P1__SetOutSubcl4(my_id, true);
}

void L_P1_C2_GUpdatePrev(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C2(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C2(proc_id);
    L_P1__SetSubcl15(my_id, L_P1__GetInSubcl14(my_id));
    L_P1__SetSubcl17(my_id, L_P1__GetInSubcl16(my_id));
    L_P1__SetSubcl19(my_id, L_P1__GetInSubcl18(my_id));
    L_P1__SetSubcl21(my_id, L_P1__GetInSubcl20(my_id));
    L_P1__SetSubcl23(my_id, L_P1__GetSubcl22(my_id));
    L_P1__SetSubcl25(my_id, L_P1__GetSubcl24(my_id));
    L_P1__SetSubcl27(my_id, L_P1__GetSubcl26(my_id));
}

// ********** Definizione macro **********

// Macro di effetto

/*
    CNL corrispondente:
    
    { commento: {34,}  se lo stato  non è  diverso da  commento: {56,}  state1  commento: {106,} commento: {38,} e  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  commento: {56,} 15124 commento: {37,} o  se la variabile SubClass_C2_variabile_V10 non è  diverso da  commento: {56,} 6 commento: {34,} o  se il parametro SubClass_C2_parametro_P2 è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE , commento: {68,}Attiva il timer SubClass_C2_timer_T7
    
     ,altrimenti  commento: {66,} Assegna al comando SubClass_C2_comando_C5 il valore c270
    
    
    
    }
*/
void L_P1__Macro5(instance_id_t const my_id )
{
//  *34,*  se lo stato  non è  diverso da  *56,*  state1  *106,* *38,* e  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  *56,* 15124 *37,* o  se la variabile SubClass_C2_variabile_V10 non è  diverso da  *56,* 6 *34,* o  se il parametro SubClass_C2_parametro_P2 è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE , *68,*Attiva il timer SubClass_C2_timer_T7
    // ,altrimenti  *66,* Assegna al comando SubClass_C2_comando_C5 il valore c270
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_AndLogicOP_2 = true;
    bool res_NotLogicOP_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1_C2_GetState(my_id) == C2_St_state));
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! res_NotLogicOP_4);
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_3);
    bool res_NotLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (Counter_GetValore(L_P1__GetSubcl50(my_id)) == 15124u));
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! res_NotLogicOP_6);
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_5);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_2);
    bool res_NotLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetSubcl34(my_id) == 6u));
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! res_NotLogicOP_8);
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_NotLogicOP_7);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_AndLogicOP_9 = true;
    res_AndLogicOP_9 = (res_AndLogicOP_9 && (L_P1__GetParamSubcl11(my_id) == false));
    res_AndLogicOP_9 = (res_AndLogicOP_9 && (L_P1__GetInConsd1(my_id) == false));
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_9);
    
    if(res_OrLogicOP_0){
    
    Timer_Attiva(L_P1__GetSubcl49(my_id));
    }else{
    
    L_P1__SetOutSubcl3(my_id,c270);
    }
}


// Macro di verifica

/*
    CNL corrispondente:
     
    {  se il ripristino dello stato  è  uguale a  commento: {53,}  state1  commento: {107,} commento: {35,} e  se il controllo SubClass_C2_controllo_C7 non è  diverso da GialloVerde commento: {38,} e  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  commento: {56,} 123 e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   commento: {48,49,}  commento: {,}  il controllo SubClass_C2_controllo_C7 non sia  uguale a GialloVerde
     commento: {104,} o  che  commento: {35,}  il controllo SubClass_C2_controllo_C1 sia  uguale a c270
     commento: {104,} o  che  commento: {,}  il timer SubClass_C2_timer_T7 non sia attivo
     commento: {104,} e  che  commento: {36,}  il timer SubClass_C2_timer_T4 non sia disattivo
     commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
    
    
    }
*/
bool L_P1__Macro11(instance_id_t const my_id )
{
bool res_AndLogicOP_0 = true;
    
    //  se il ripristino dello stato  è  uguale a  *53,*  state1  *107,* *35,* e  se il controllo SubClass_C2_controllo_C7 non è  diverso da GialloVerde *38,* e  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  *56,* 123 e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   *48,49,*  *,*  il controllo SubClass_C2_controllo_C7 non sia  uguale a GialloVerde
    //   *104,* o  che  *35,*  il controllo SubClass_C2_controllo_C1 sia  uguale a c270
    //   *104,* o  che  *,*  il timer SubClass_C2_timer_T7 non sia attivo
    //   *104,* e  che  *36,*  il timer SubClass_C2_timer_T4 non sia disattivo
    //   *104,* e  che   il controllo ConsDef  sia  uguale a FALSE
    bool res_ImpliesLogicOp_1 = true;
    bool res_AndLogicOP_2 = true;
    bool res_AndLogicOP_3 = true;
    bool res_AndLogicOP_4 = true;
    bool res_AndLogicOP_5 = true;
    res_AndLogicOP_5 = (res_AndLogicOP_5 && (L_P1__GetStato3(my_id) == C2_St_state));
    bool res_NotLogicOP_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetInSubcl7(my_id) == gialloverde));
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! res_NotLogicOP_7);
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_6);
    
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_AndLogicOP_5);
    bool res_NotLogicOP_8 = true;
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (Counter_GetValore(L_P1__GetSubcl50(my_id)) == 123u));
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! res_NotLogicOP_9);
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_8);
    
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_AndLogicOP_4);
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (L_P1__GetInConsd1(my_id) == false));
    
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_AndLogicOP_3);
    res_AndLogicOP_2 = (res_AndLogicOP_2 && (L_P1__GetInConsd1(my_id) == false));
    
    if(res_AndLogicOP_2){
    bool res_OrLogicOP_10 = false;
    bool res_OrLogicOP_11 = false;
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (L_P1__GetInSubcl7(my_id) == gialloverde));
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_NotLogicOP_12);
    res_OrLogicOP_11 = (res_OrLogicOP_11 || (L_P1__GetInSubcl5(my_id) == c270));
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_OrLogicOP_11);
    bool res_AndLogicOP_13 = true;
    bool res_AndLogicOP_14 = true;
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! Timer_Attivo(L_P1__GetSubcl49(my_id)));
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_NotLogicOP_15);
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! Timer_Disattivo(L_P1__GetSubcl48(my_id)));
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_NotLogicOP_16);
    
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_AndLogicOP_14);
    res_AndLogicOP_13 = (res_AndLogicOP_13 && (L_P1__GetInConsd1(my_id) == false));
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_AndLogicOP_13);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_OrLogicOP_10);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
     
    { commento: {61,} commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L2 è  uguale a  commento: {53,}  state1 , Tutte le seguenti { 
     commento: {63,} commento: {34,}  se il parametro SubClass_C2_parametro_P9 non è  uguale a  False , Solo una delle seguenti { 
     commento: {34,}  se il parametro SubClass_C2_parametro_P1 è  diverso da c270 commento: {35,} e  se il controllo SubClass_C2_controllo_C2 è  uguale a c120x commento: {35,} o  se il controllo SubClass_C2_controllo_C7 è  uguale a GialloVerde o  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   commento: {47,51,}  commento: {,}  il contatore SubClass_C2_contatore_Co7 non sia  maggiore di  commento: {54,} 1212
     commento: {104,} e  che  commento: {34,}  il parametro SubClass_C2_parametro_P1 sia  diverso da c270
    
    
     } Verifica che   commento: {47,48,49,}  commento: {,}  il timer SubClass_C2_timer_T4 sia attivo
     commento: {104,} o  che  commento: {34,}  il parametro SubClass_C2_parametro_P9 non sia  uguale a  True 
     commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
    
    
     } Verifica che   commento: {48,49,}   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} e  che  commento: {,}  il timer SubClass_C2_timer_T7 non sia disattivo
     commento: {104,} e  che  commento: {,}  il controllo SubClass_C2_controllo_C7 sia  uguale a GialloVerde
    
    
    }
*/
bool L_P1__Macro12(instance_id_t const my_id )
{
bool res_AndLogicOP_0 = true;
    
    //  *61,* *111,*  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L2 è  uguale a  *53,*  state1 , Tutte le seguenti { 
    //   *63,* *34,*  se il parametro SubClass_C2_parametro_P9 non è  uguale a  False , Solo una delle seguenti { 
    //   *34,*  se il parametro SubClass_C2_parametro_P1 è  diverso da c270 *35,* e  se il controllo SubClass_C2_controllo_C2 è  uguale a c120x *35,* o  se il controllo SubClass_C2_controllo_C7 è  uguale a GialloVerde o  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   *47,51,*  *,*  il contatore SubClass_C2_contatore_Co7 non sia  maggiore di  *54,* 1212
    //   *104,* e  che  *34,*  il parametro SubClass_C2_parametro_P1 sia  diverso da c270
    //   } Verifica che   *47,48,49,*  *,*  il timer SubClass_C2_timer_T4 sia attivo
    //   *104,* o  che  *34,*  il parametro SubClass_C2_parametro_P9 non sia  uguale a  True 
    //   *104,* o  che   il controllo ConsDef  sia  uguale a FALSE 
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_ForAllPredicate_2 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl9Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl9(my_id,i);
    bool res_ImpliesLogicOp_3 = true;
    res_ImpliesLogicOp_3 = (res_ImpliesLogicOp_3 && (L_P1_C1_GetState(it.mainc39) == C1_St_state));
    res_ForAllPredicate_2 = res_ImpliesLogicOp_3;
    if(!res_ForAllPredicate_2) {break;}
    }
    if(res_ForAllPredicate_2){
    bool res_AndLogicOP_4 = true;
    bool res_ImpliesLogicOp_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetParamSubcl13(my_id) == false));
    if(res_NotLogicOP_6){
    bool res_ImpliesLogicOp_7 = true;
    bool res_OrLogicOP_8 = false;
    bool res_OrLogicOP_9 = false;
    bool res_AndLogicOP_10 = true;
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (L_P1__GetParamSubcl10(my_id) == c270));
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_NotLogicOP_11);
    res_AndLogicOP_10 = (res_AndLogicOP_10 && (L_P1__GetInSubcl6(my_id) == c120x));
    
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_AndLogicOP_10);
    res_OrLogicOP_9 = (res_OrLogicOP_9 || (L_P1__GetInSubcl7(my_id) == gialloverde));
    
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_OrLogicOP_9);
    bool res_AndLogicOP_12 = true;
    bool res_AndLogicOP_13 = true;
    res_AndLogicOP_13 = (res_AndLogicOP_13 && (L_P1__GetInConsd1(my_id) == false));
    res_AndLogicOP_13 = (res_AndLogicOP_13 && (L_P1__GetInConsd1(my_id) == false));
    
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_AndLogicOP_13);
    res_AndLogicOP_12 = (res_AndLogicOP_12 && (L_P1__GetInConsd1(my_id) == false));
    
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_AndLogicOP_12);
    
    if(res_OrLogicOP_8){
    bool res_AndLogicOP_14 = true;
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (Counter_GetValore(L_P1__GetSubcl50(my_id)) > 1212u));
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_NotLogicOP_15);
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (L_P1__GetParamSubcl10(my_id) == c270));
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_NotLogicOP_16);
    
    res_ImpliesLogicOp_7 = (res_ImpliesLogicOp_7 && res_AndLogicOP_14);
    }
    res_ImpliesLogicOp_5 = (res_ImpliesLogicOp_5 && res_ImpliesLogicOp_7);
    }
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_ImpliesLogicOp_5);
    bool res_OrLogicOP_17 = false;
    bool res_OrLogicOP_18 = false;
    res_OrLogicOP_18 = (res_OrLogicOP_18 || Timer_Attivo(L_P1__GetSubcl48(my_id)));
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (L_P1__GetParamSubcl13(my_id) == true));
    res_OrLogicOP_18 = (res_OrLogicOP_18 || res_NotLogicOP_19);
    
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_OrLogicOP_18);
    res_OrLogicOP_17 = (res_OrLogicOP_17 || (L_P1__GetInConsd1(my_id) == false));
    
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_OrLogicOP_17);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_AndLogicOP_4);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *48,49,*   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* e  che  *,*  il timer SubClass_C2_timer_T7 non sia disattivo
    //   *104,* e  che  *,*  il controllo SubClass_C2_controllo_C7 sia  uguale a GialloVerde
    bool res_AndLogicOP_20 = true;
    bool res_AndLogicOP_21 = true;
    res_AndLogicOP_21 = (res_AndLogicOP_21 && (L_P1__GetInConsd1(my_id) == false));
    bool res_NotLogicOP_22 = true;
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! Timer_Disattivo(L_P1__GetSubcl49(my_id)));
    res_AndLogicOP_21 = (res_AndLogicOP_21 && res_NotLogicOP_22);
    
    res_AndLogicOP_20 = (res_AndLogicOP_20 && res_AndLogicOP_21);
    res_AndLogicOP_20 = (res_AndLogicOP_20 && (L_P1__GetInSubcl7(my_id) == gialloverde));
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_AndLogicOP_20);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
     
    { commento: {62,}  se il ripristino dello stato  è  uguale a  commento: {53,}  state1  commento: {107,} commento: {35,} e  se il controllo SubClass_C2_controllo_C1 è  uguale a c270 commento: {37,} o  se la variabile SubClass_C2_variabile_V7 non è  uguale a  False , Almeno una delle seguenti { 
     commento: {62,} commento: {110,}  se il ripristino del timer  SubClass_C2_restoreTI_TI3 è disattivo commento: {38,} o  se il contatore SubClass_C2_contatore_Co7 non è  uguale a  commento: {53,} 141245 commento: {34,} e  se il parametro SubClass_C2_parametro_P9 non è  diverso da  True  commento: {38,} e  se il contatore SubClass_C2_contatore_Co7 è  diverso da  commento: {56,} 11 commento: {34,} e  se il parametro SubClass_C2_parametro_P1 non è  diverso da c270, Almeno una delle seguenti { 
     commento: {61,} commento: {109,}  se il ripristino della variabile  SubClass_C2_restoreva_RV2 non è  maggiore di  commento: {54,} 4 o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
     commento: {63,} commento: {34,}  se il parametro SubClass_C2_parametro_P1 è  diverso da c270 commento: {37,} o  se la variabile SubClass_C2_variabile_V4 è  diverso da  False , Solo una delle seguenti { 
     commento: {62,} commento: {43,}  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C2_lista_L2 è attivo commento: {34,} o  se il parametro SubClass_C2_parametro_P5 è  diverso da RossoVerde e  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} o  se il parametro SubClass_C2_parametro_P1 non è  uguale a c270 commento: {38,} e  se il contatore SubClass_C2_contatore_Co7 non è  uguale a  commento: {53,} 11, Almeno una delle seguenti { 
     commento: {61,} commento: {36,}  se il timer SubClass_C2_timer_T4 è attivo commento: {35,} o  se il controllo SubClass_C2_controllo_C2 è  diverso da c120x commento: {38,} o  se il contatore SubClass_C2_contatore_Co7 è  maggiore di  commento: {54,} 143, Tutte le seguenti { 
     commento: {110,}  se il ripristino del timer  SubClass_C2_restoreTI_TI3 è scaduto commento: {36,} e  se il timer SubClass_C2_timer_T4 è attivo commento: {34,} o  se il parametro SubClass_C2_parametro_P1 non è  diverso da c270 commento: {35,} o  se il controllo SubClass_C2_controllo_C2 è  uguale a c120x o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   commento: {47,49,50,51,}  commento: {34,}  il parametro SubClass_C2_parametro_P2 non sia  diverso da  False 
     commento: {104,} e  che  commento: {,}  il timer SubClass_C2_timer_T7 non sia disattivo
     commento: {104,} o  che  commento: {,}  la variabile SubClass_C2_variabile_V4 sia  uguale a  False 
     commento: {104,} o  che  commento: {,}  il contatore SubClass_C2_contatore_Co7 sia  uguale a  commento: {53,} 1501
     commento: {104,} o  che  commento: {34,}  il parametro SubClass_C2_parametro_P1 non sia  diverso da c270
    
    
     } Verifica che   commento: {47,49,50,}  commento: {,}  il timer SubClass_C2_timer_T7 non sia scaduto
     commento: {104,} o  che  commento: {34,}  il parametro SubClass_C2_parametro_P5 sia  diverso da RossoVerde
     commento: {104,} e  che  commento: {,}  la variabile SubClass_C2_variabile_V4 sia  diverso da  False 
    
    
     } Verifica che   commento: {48,50,51,}   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} e  che  commento: {,}  la variabile SubClass_C2_variabile_V4 non sia  diverso da  True 
     commento: {104,} e  che  commento: {,}  il contatore SubClass_C2_contatore_Co7 sia  maggiore di  commento: {54,} 1224
     commento: {104,} e  che  commento: {37,}  la variabile SubClass_C2_variabile_V10 sia  uguale a  commento: {53,} 7
     commento: {104,} e  che  commento: {,}  il controllo SubClass_C2_controllo_C2 non sia  uguale a c120x
    
    
     } Verifica che   commento: {48,50,51,}  commento: {,}  la variabile SubClass_C2_variabile_V4 sia  uguale a  True 
     commento: {104,} o  che  commento: {37,}  la variabile SubClass_C2_variabile_V4 non sia  uguale a  True 
     commento: {104,} e  che  commento: {,}  il contatore SubClass_C2_contatore_Co7 sia  uguale a  commento: {53,} 1
     commento: {104,} o  che  commento: {35,}  il controllo SubClass_C2_controllo_C2 non sia  uguale a c120x
     commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} e  che  commento: {38,}  il contatore SubClass_C2_contatore_Co7 non sia  minore di  commento: {55,} 1230
    
    
     } Verifica che   commento: {47,49,50,}  commento: {,}  la variabile SubClass_C2_variabile_V7 sia  uguale a  True 
     commento: {104,} o  che  commento: {34,}  il parametro SubClass_C2_parametro_P1 non sia  uguale a c270
     commento: {104,} e  che  commento: {,}  il timer SubClass_C2_timer_T4 sia attivo
     commento: {104,} o  che  commento: {37,}  la variabile SubClass_C2_variabile_V4 non sia  uguale a  False 
     commento: {104,} e  che  commento: {34,}  il parametro SubClass_C2_parametro_P1 non sia  diverso da c270
    
    
     } Verifica che   commento: {47,48,}  commento: {34,}  il parametro SubClass_C2_parametro_P1 sia  uguale a c270
     commento: {104,} o  che  commento: {,}  il controllo SubClass_C2_controllo_C7 sia  uguale a GialloVerde
    
    
     } Verifica che   commento: {49,}  commento: {,}  il timer SubClass_C2_timer_T4 sia attivo
    
    
    }
*/
bool L_P1__Macro13(instance_id_t const my_id )
{
bool res_AndLogicOP_0 = true;
    
    //  *62,*  se il ripristino dello stato  è  uguale a  *53,*  state1  *107,* *35,* e  se il controllo SubClass_C2_controllo_C1 è  uguale a c270 *37,* o  se la variabile SubClass_C2_variabile_V7 non è  uguale a  False , Almeno una delle seguenti { 
    //   *62,* *110,*  se il ripristino del timer  SubClass_C2_restoreTI_TI3 è disattivo *38,* o  se il contatore SubClass_C2_contatore_Co7 non è  uguale a  *53,* 141245 *34,* e  se il parametro SubClass_C2_parametro_P9 non è  diverso da  True  *38,* e  se il contatore SubClass_C2_contatore_Co7 è  diverso da  *56,* 11 *34,* e  se il parametro SubClass_C2_parametro_P1 non è  diverso da c270, Almeno una delle seguenti { 
    //   *61,* *109,*  se il ripristino della variabile  SubClass_C2_restoreva_RV2 non è  maggiore di  *54,* 4 o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
    //   *63,* *34,*  se il parametro SubClass_C2_parametro_P1 è  diverso da c270 *37,* o  se la variabile SubClass_C2_variabile_V4 è  diverso da  False , Solo una delle seguenti { 
    //   *62,* *43,*  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C2_lista_L2 è attivo *34,* o  se il parametro SubClass_C2_parametro_P5 è  diverso da RossoVerde e  se il controllo ConsDef  è  uguale a FALSE  *34,* o  se il parametro SubClass_C2_parametro_P1 non è  uguale a c270 *38,* e  se il contatore SubClass_C2_contatore_Co7 non è  uguale a  *53,* 11, Almeno una delle seguenti { 
    //   *61,* *36,*  se il timer SubClass_C2_timer_T4 è attivo *35,* o  se il controllo SubClass_C2_controllo_C2 è  diverso da c120x *38,* o  se il contatore SubClass_C2_contatore_Co7 è  maggiore di  *54,* 143, Tutte le seguenti { 
    //   *110,*  se il ripristino del timer  SubClass_C2_restoreTI_TI3 è scaduto *36,* e  se il timer SubClass_C2_timer_T4 è attivo *34,* o  se il parametro SubClass_C2_parametro_P1 non è  diverso da c270 *35,* o  se il controllo SubClass_C2_controllo_C2 è  uguale a c120x o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   *47,49,50,51,*  *34,*  il parametro SubClass_C2_parametro_P2 non sia  diverso da  False 
    //   *104,* e  che  *,*  il timer SubClass_C2_timer_T7 non sia disattivo
    //   *104,* o  che  *,*  la variabile SubClass_C2_variabile_V4 sia  uguale a  False 
    //   *104,* o  che  *,*  il contatore SubClass_C2_contatore_Co7 sia  uguale a  *53,* 1501
    //   *104,* o  che  *34,*  il parametro SubClass_C2_parametro_P1 non sia  diverso da c270
    //   } Verifica che   *47,49,50,*  *,*  il timer SubClass_C2_timer_T7 non sia scaduto
    //   *104,* o  che  *34,*  il parametro SubClass_C2_parametro_P5 sia  diverso da RossoVerde
    //   *104,* e  che  *,*  la variabile SubClass_C2_variabile_V4 sia  diverso da  False 
    //   } Verifica che   *48,50,51,*   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* e  che  *,*  la variabile SubClass_C2_variabile_V4 non sia  diverso da  True 
    //   *104,* e  che  *,*  il contatore SubClass_C2_contatore_Co7 sia  maggiore di  *54,* 1224
    //   *104,* e  che  *37,*  la variabile SubClass_C2_variabile_V10 sia  uguale a  *53,* 7
    //   *104,* e  che  *,*  il controllo SubClass_C2_controllo_C2 non sia  uguale a c120x
    //   } Verifica che   *48,50,51,*  *,*  la variabile SubClass_C2_variabile_V4 sia  uguale a  True 
    //   *104,* o  che  *37,*  la variabile SubClass_C2_variabile_V4 non sia  uguale a  True 
    //   *104,* e  che  *,*  il contatore SubClass_C2_contatore_Co7 sia  uguale a  *53,* 1
    //   *104,* o  che  *35,*  il controllo SubClass_C2_controllo_C2 non sia  uguale a c120x
    //   *104,* e  che   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* e  che  *38,*  il contatore SubClass_C2_contatore_Co7 non sia  minore di  *55,* 1230
    //   } Verifica che   *47,49,50,*  *,*  la variabile SubClass_C2_variabile_V7 sia  uguale a  True 
    //   *104,* o  che  *34,*  il parametro SubClass_C2_parametro_P1 non sia  uguale a c270
    //   *104,* e  che  *,*  il timer SubClass_C2_timer_T4 sia attivo
    //   *104,* o  che  *37,*  la variabile SubClass_C2_variabile_V4 non sia  uguale a  False 
    //   *104,* e  che  *34,*  il parametro SubClass_C2_parametro_P1 non sia  diverso da c270
    //   } Verifica che   *47,48,*  *34,*  il parametro SubClass_C2_parametro_P1 sia  uguale a c270
    //   *104,* o  che  *,*  il controllo SubClass_C2_controllo_C7 sia  uguale a GialloVerde
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_AndLogicOP_3 = true;
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (L_P1__GetStato3(my_id) == C2_St_state));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (L_P1__GetInSubcl5(my_id) == c270));
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_3);
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetSubcl37(my_id) == false));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_4);
    
    if(res_OrLogicOP_2){
    bool res_OrLogicOP_5 = false;
    bool res_ImpliesLogicOp_6 = true;
    bool res_OrLogicOP_7 = false;
    res_OrLogicOP_7 = (res_OrLogicOP_7 || Timer_Disattivo(L_P1__GetSubcl43(my_id)));
    bool res_AndLogicOP_8 = true;
    bool res_AndLogicOP_9 = true;
    bool res_AndLogicOP_10 = true;
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (Counter_GetValore(L_P1__GetSubcl50(my_id)) == 141245u));
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_NotLogicOP_11);
    bool res_NotLogicOP_12 = true;
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (L_P1__GetParamSubcl13(my_id) == true));
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! res_NotLogicOP_13);
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_NotLogicOP_12);
    
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_AndLogicOP_10);
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (Counter_GetValore(L_P1__GetSubcl50(my_id)) == 11u));
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_NotLogicOP_14);
    
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_AndLogicOP_9);
    bool res_NotLogicOP_15 = true;
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (L_P1__GetParamSubcl10(my_id) == c270));
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! res_NotLogicOP_16);
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_15);
    
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_AndLogicOP_8);
    
    if(res_OrLogicOP_7){
    bool res_OrLogicOP_17 = false;
    bool res_ImpliesLogicOp_18 = true;
    bool res_OrLogicOP_19 = false;
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! (L_P1__GetSubcl31(my_id) > 4u));
    res_OrLogicOP_19 = (res_OrLogicOP_19 || res_NotLogicOP_20);
    res_OrLogicOP_19 = (res_OrLogicOP_19 || (L_P1__GetInConsd1(my_id) == false));
    
    if(res_OrLogicOP_19){
    bool res_AndLogicOP_21 = true;
    bool res_ImpliesLogicOp_22 = true;
    bool res_OrLogicOP_23 = false;
    bool res_NotLogicOP_24 = true;
    res_NotLogicOP_24 = (res_NotLogicOP_24 && ! (L_P1__GetParamSubcl10(my_id) == c270));
    res_OrLogicOP_23 = (res_OrLogicOP_23 || res_NotLogicOP_24);
    bool res_NotLogicOP_25 = true;
    res_NotLogicOP_25 = (res_NotLogicOP_25 && ! (L_P1__GetSubcl35(my_id) == false));
    res_OrLogicOP_23 = (res_OrLogicOP_23 || res_NotLogicOP_25);
    
    if(res_OrLogicOP_23){
    bool res_XorLogicOP_26 = true;
    int xorIndex_res_XorLogicOP_26 = 0;
    bool res_ImpliesLogicOp_27 = true;
    bool res_OrLogicOP_28 = false;
    bool res_OrLogicOP_29 = false;
    bool res_ForAllPredicate_30 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl9Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl9(my_id,i);
    bool res_ImpliesLogicOp_31 = true;
    res_ImpliesLogicOp_31 = (res_ImpliesLogicOp_31 && Timer_Attivo(L_P1__GetMainc36(it.mainc39)));
    res_ForAllPredicate_30 = res_ImpliesLogicOp_31;
    if(!res_ForAllPredicate_30) {break;}
    }
    res_OrLogicOP_29 = (res_OrLogicOP_29 || res_ForAllPredicate_30);
    bool res_AndLogicOP_32 = true;
    bool res_NotLogicOP_33 = true;
    res_NotLogicOP_33 = (res_NotLogicOP_33 && ! (L_P1__GetParamSubcl12(my_id) == rossoverde));
    res_AndLogicOP_32 = (res_AndLogicOP_32 && res_NotLogicOP_33);
    res_AndLogicOP_32 = (res_AndLogicOP_32 && (L_P1__GetInConsd1(my_id) == false));
    
    res_OrLogicOP_29 = (res_OrLogicOP_29 || res_AndLogicOP_32);
    
    res_OrLogicOP_28 = (res_OrLogicOP_28 || res_OrLogicOP_29);
    bool res_AndLogicOP_34 = true;
    bool res_NotLogicOP_35 = true;
    res_NotLogicOP_35 = (res_NotLogicOP_35 && ! (L_P1__GetParamSubcl10(my_id) == c270));
    res_AndLogicOP_34 = (res_AndLogicOP_34 && res_NotLogicOP_35);
    bool res_NotLogicOP_36 = true;
    res_NotLogicOP_36 = (res_NotLogicOP_36 && ! (Counter_GetValore(L_P1__GetSubcl50(my_id)) == 11u));
    res_AndLogicOP_34 = (res_AndLogicOP_34 && res_NotLogicOP_36);
    
    res_OrLogicOP_28 = (res_OrLogicOP_28 || res_AndLogicOP_34);
    
    if(res_OrLogicOP_28){
    bool res_OrLogicOP_37 = false;
    bool res_ImpliesLogicOp_38 = true;
    bool res_OrLogicOP_39 = false;
    bool res_OrLogicOP_40 = false;
    res_OrLogicOP_40 = (res_OrLogicOP_40 || Timer_Attivo(L_P1__GetSubcl48(my_id)));
    bool res_NotLogicOP_41 = true;
    res_NotLogicOP_41 = (res_NotLogicOP_41 && ! (L_P1__GetInSubcl6(my_id) == c120x));
    res_OrLogicOP_40 = (res_OrLogicOP_40 || res_NotLogicOP_41);
    
    res_OrLogicOP_39 = (res_OrLogicOP_39 || res_OrLogicOP_40);
    res_OrLogicOP_39 = (res_OrLogicOP_39 || (Counter_GetValore(L_P1__GetSubcl50(my_id)) > 143u));
    
    if(res_OrLogicOP_39){
    bool res_ImpliesLogicOp_42 = true;
    bool res_OrLogicOP_43 = false;
    bool res_OrLogicOP_44 = false;
    bool res_OrLogicOP_45 = false;
    bool res_AndLogicOP_46 = true;
    res_AndLogicOP_46 = (res_AndLogicOP_46 && Timer_Scaduto(L_P1__GetSubcl43(my_id)));
    res_AndLogicOP_46 = (res_AndLogicOP_46 && Timer_Attivo(L_P1__GetSubcl48(my_id)));
    
    res_OrLogicOP_45 = (res_OrLogicOP_45 || res_AndLogicOP_46);
    bool res_NotLogicOP_47 = true;
    bool res_NotLogicOP_48 = true;
    res_NotLogicOP_48 = (res_NotLogicOP_48 && ! (L_P1__GetParamSubcl10(my_id) == c270));
    res_NotLogicOP_47 = (res_NotLogicOP_47 && ! res_NotLogicOP_48);
    res_OrLogicOP_45 = (res_OrLogicOP_45 || res_NotLogicOP_47);
    
    res_OrLogicOP_44 = (res_OrLogicOP_44 || res_OrLogicOP_45);
    res_OrLogicOP_44 = (res_OrLogicOP_44 || (L_P1__GetInSubcl6(my_id) == c120x));
    
    res_OrLogicOP_43 = (res_OrLogicOP_43 || res_OrLogicOP_44);
    res_OrLogicOP_43 = (res_OrLogicOP_43 || (L_P1__GetInConsd1(my_id) == false));
    
    if(res_OrLogicOP_43){
    bool res_OrLogicOP_49 = false;
    bool res_OrLogicOP_50 = false;
    bool res_OrLogicOP_51 = false;
    bool res_AndLogicOP_52 = true;
    bool res_NotLogicOP_53 = true;
    bool res_NotLogicOP_54 = true;
    res_NotLogicOP_54 = (res_NotLogicOP_54 && ! (L_P1__GetParamSubcl11(my_id) == false));
    res_NotLogicOP_53 = (res_NotLogicOP_53 && ! res_NotLogicOP_54);
    res_AndLogicOP_52 = (res_AndLogicOP_52 && res_NotLogicOP_53);
    bool res_NotLogicOP_55 = true;
    res_NotLogicOP_55 = (res_NotLogicOP_55 && ! Timer_Disattivo(L_P1__GetSubcl49(my_id)));
    res_AndLogicOP_52 = (res_AndLogicOP_52 && res_NotLogicOP_55);
    
    res_OrLogicOP_51 = (res_OrLogicOP_51 || res_AndLogicOP_52);
    res_OrLogicOP_51 = (res_OrLogicOP_51 || (L_P1__GetSubcl35(my_id) == false));
    
    res_OrLogicOP_50 = (res_OrLogicOP_50 || res_OrLogicOP_51);
    res_OrLogicOP_50 = (res_OrLogicOP_50 || (Counter_GetValore(L_P1__GetSubcl50(my_id)) == 1501u));
    
    res_OrLogicOP_49 = (res_OrLogicOP_49 || res_OrLogicOP_50);
    bool res_NotLogicOP_56 = true;
    bool res_NotLogicOP_57 = true;
    res_NotLogicOP_57 = (res_NotLogicOP_57 && ! (L_P1__GetParamSubcl10(my_id) == c270));
    res_NotLogicOP_56 = (res_NotLogicOP_56 && ! res_NotLogicOP_57);
    res_OrLogicOP_49 = (res_OrLogicOP_49 || res_NotLogicOP_56);
    
    res_ImpliesLogicOp_42 = (res_ImpliesLogicOp_42 && res_OrLogicOP_49);
    }
    res_ImpliesLogicOp_38 = (res_ImpliesLogicOp_38 && res_ImpliesLogicOp_42);
    }
    res_OrLogicOP_37 = (res_OrLogicOP_37 || res_ImpliesLogicOp_38);
    bool res_OrLogicOP_58 = false;
    bool res_NotLogicOP_59 = true;
    res_NotLogicOP_59 = (res_NotLogicOP_59 && ! Timer_Scaduto(L_P1__GetSubcl49(my_id)));
    res_OrLogicOP_58 = (res_OrLogicOP_58 || res_NotLogicOP_59);
    bool res_AndLogicOP_60 = true;
    bool res_NotLogicOP_61 = true;
    res_NotLogicOP_61 = (res_NotLogicOP_61 && ! (L_P1__GetParamSubcl12(my_id) == rossoverde));
    res_AndLogicOP_60 = (res_AndLogicOP_60 && res_NotLogicOP_61);
    bool res_NotLogicOP_62 = true;
    res_NotLogicOP_62 = (res_NotLogicOP_62 && ! (L_P1__GetSubcl35(my_id) == false));
    res_AndLogicOP_60 = (res_AndLogicOP_60 && res_NotLogicOP_62);
    
    res_OrLogicOP_58 = (res_OrLogicOP_58 || res_AndLogicOP_60);
    
    res_OrLogicOP_37 = (res_OrLogicOP_37 || res_OrLogicOP_58);
    
    res_ImpliesLogicOp_27 = (res_ImpliesLogicOp_27 && res_OrLogicOP_37);
    }
    if(res_ImpliesLogicOp_27){
    xorIndex_res_XorLogicOP_26 = (xorIndex_res_XorLogicOP_26 + 1);
    }
    bool res_AndLogicOP_63 = true;
    bool res_AndLogicOP_64 = true;
    bool res_AndLogicOP_65 = true;
    bool res_AndLogicOP_66 = true;
    res_AndLogicOP_66 = (res_AndLogicOP_66 && (L_P1__GetInConsd1(my_id) == false));
    bool res_NotLogicOP_67 = true;
    bool res_NotLogicOP_68 = true;
    res_NotLogicOP_68 = (res_NotLogicOP_68 && ! (L_P1__GetSubcl35(my_id) == true));
    res_NotLogicOP_67 = (res_NotLogicOP_67 && ! res_NotLogicOP_68);
    res_AndLogicOP_66 = (res_AndLogicOP_66 && res_NotLogicOP_67);
    
    res_AndLogicOP_65 = (res_AndLogicOP_65 && res_AndLogicOP_66);
    res_AndLogicOP_65 = (res_AndLogicOP_65 && (Counter_GetValore(L_P1__GetSubcl50(my_id)) > 1224u));
    
    res_AndLogicOP_64 = (res_AndLogicOP_64 && res_AndLogicOP_65);
    res_AndLogicOP_64 = (res_AndLogicOP_64 && (L_P1__GetSubcl34(my_id) == 7u));
    
    res_AndLogicOP_63 = (res_AndLogicOP_63 && res_AndLogicOP_64);
    bool res_NotLogicOP_69 = true;
    res_NotLogicOP_69 = (res_NotLogicOP_69 && ! (L_P1__GetInSubcl6(my_id) == c120x));
    res_AndLogicOP_63 = (res_AndLogicOP_63 && res_NotLogicOP_69);
    
    if(res_AndLogicOP_63){
    xorIndex_res_XorLogicOP_26 = (xorIndex_res_XorLogicOP_26 + 1);
    }
    
    res_XorLogicOP_26 = (res_XorLogicOP_26 && (xorIndex_res_XorLogicOP_26 == 1));
    res_ImpliesLogicOp_22 = (res_ImpliesLogicOp_22 && res_XorLogicOP_26);
    }
    res_AndLogicOP_21 = (res_AndLogicOP_21 && res_ImpliesLogicOp_22);
    bool res_OrLogicOP_70 = false;
    bool res_OrLogicOP_71 = false;
    res_OrLogicOP_71 = (res_OrLogicOP_71 || (L_P1__GetSubcl35(my_id) == true));
    bool res_AndLogicOP_72 = true;
    bool res_NotLogicOP_73 = true;
    res_NotLogicOP_73 = (res_NotLogicOP_73 && ! (L_P1__GetSubcl35(my_id) == true));
    res_AndLogicOP_72 = (res_AndLogicOP_72 && res_NotLogicOP_73);
    res_AndLogicOP_72 = (res_AndLogicOP_72 && (Counter_GetValore(L_P1__GetSubcl50(my_id)) == 1u));
    
    res_OrLogicOP_71 = (res_OrLogicOP_71 || res_AndLogicOP_72);
    
    res_OrLogicOP_70 = (res_OrLogicOP_70 || res_OrLogicOP_71);
    bool res_AndLogicOP_74 = true;
    bool res_AndLogicOP_75 = true;
    bool res_NotLogicOP_76 = true;
    res_NotLogicOP_76 = (res_NotLogicOP_76 && ! (L_P1__GetInSubcl6(my_id) == c120x));
    res_AndLogicOP_75 = (res_AndLogicOP_75 && res_NotLogicOP_76);
    res_AndLogicOP_75 = (res_AndLogicOP_75 && (L_P1__GetInConsd1(my_id) == false));
    
    res_AndLogicOP_74 = (res_AndLogicOP_74 && res_AndLogicOP_75);
    bool res_NotLogicOP_77 = true;
    res_NotLogicOP_77 = (res_NotLogicOP_77 && ! (Counter_GetValore(L_P1__GetSubcl50(my_id)) < 1230u));
    res_AndLogicOP_74 = (res_AndLogicOP_74 && res_NotLogicOP_77);
    
    res_OrLogicOP_70 = (res_OrLogicOP_70 || res_AndLogicOP_74);
    
    res_AndLogicOP_21 = (res_AndLogicOP_21 && res_OrLogicOP_70);
    
    res_ImpliesLogicOp_18 = (res_ImpliesLogicOp_18 && res_AndLogicOP_21);
    }
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_ImpliesLogicOp_18);
    bool res_OrLogicOP_78 = false;
    bool res_OrLogicOP_79 = false;
    res_OrLogicOP_79 = (res_OrLogicOP_79 || (L_P1__GetSubcl37(my_id) == true));
    bool res_AndLogicOP_80 = true;
    bool res_NotLogicOP_81 = true;
    res_NotLogicOP_81 = (res_NotLogicOP_81 && ! (L_P1__GetParamSubcl10(my_id) == c270));
    res_AndLogicOP_80 = (res_AndLogicOP_80 && res_NotLogicOP_81);
    res_AndLogicOP_80 = (res_AndLogicOP_80 && Timer_Attivo(L_P1__GetSubcl48(my_id)));
    
    res_OrLogicOP_79 = (res_OrLogicOP_79 || res_AndLogicOP_80);
    
    res_OrLogicOP_78 = (res_OrLogicOP_78 || res_OrLogicOP_79);
    bool res_AndLogicOP_82 = true;
    bool res_NotLogicOP_83 = true;
    res_NotLogicOP_83 = (res_NotLogicOP_83 && ! (L_P1__GetSubcl35(my_id) == false));
    res_AndLogicOP_82 = (res_AndLogicOP_82 && res_NotLogicOP_83);
    bool res_NotLogicOP_84 = true;
    bool res_NotLogicOP_85 = true;
    res_NotLogicOP_85 = (res_NotLogicOP_85 && ! (L_P1__GetParamSubcl10(my_id) == c270));
    res_NotLogicOP_84 = (res_NotLogicOP_84 && ! res_NotLogicOP_85);
    res_AndLogicOP_82 = (res_AndLogicOP_82 && res_NotLogicOP_84);
    
    res_OrLogicOP_78 = (res_OrLogicOP_78 || res_AndLogicOP_82);
    
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_OrLogicOP_78);
    
    res_ImpliesLogicOp_6 = (res_ImpliesLogicOp_6 && res_OrLogicOP_17);
    }
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_ImpliesLogicOp_6);
    bool res_OrLogicOP_86 = false;
    res_OrLogicOP_86 = (res_OrLogicOP_86 || (L_P1__GetParamSubcl10(my_id) == c270));
    res_OrLogicOP_86 = (res_OrLogicOP_86 || (L_P1__GetInSubcl7(my_id) == gialloverde));
    
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_OrLogicOP_86);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_OrLogicOP_5);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *49,*  *,*  il timer SubClass_C2_timer_T4 sia attivo
    res_AndLogicOP_0 = (res_AndLogicOP_0 && Timer_Attivo(L_P1__GetSubcl48(my_id)));
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
     
    {  se il controllo ConsDef  è  uguale a FALSE ,  commento: {43,}  se MainClass_C1_timer_T1 del campo  MainClass_C1 di SubClass_C2_lista_L1 è attivo, commento: {88,} quando  commento: {45,}    MainClass_C1_contatore_Co4 del campo  MainClass_C1     è  minore di  commento: {55,} 110 commento: {36,} o  se il timer SubClass_C2_timer_T7 è disattivo commento: {36,} e  se il timer SubClass_C2_timer_T4 è attivo commento: {36,} e  se il timer SubClass_C2_timer_T4 è attivo, Verifica che   commento: {47,48,50,}   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} e  che  commento: {34,}  il parametro SubClass_C2_parametro_P1 sia  uguale a c270
     commento: {104,} e  che  commento: {,}  la variabile SubClass_C2_variabile_V6 non sia  uguale a GialloVerde
     commento: {104,} o  che  commento: {34,}  il parametro SubClass_C2_parametro_P5 sia  uguale a RossoVerde
    
    
    }
*/
bool L_P1__Macro14(instance_id_t const my_id )
{
bool res_AndLogicOP_0 = true;
    
    //  se il controllo ConsDef  è  uguale a FALSE ,  *43,*  se MainClass_C1_timer_T1 del campo  MainClass_C1 di SubClass_C2_lista_L1 è attivo, *88,* quando  *45,*    MainClass_C1_contatore_Co4 del campo  MainClass_C1     è  minore di  *55,* 110 *36,* o  se il timer SubClass_C2_timer_T7 è disattivo *36,* e  se il timer SubClass_C2_timer_T4 è attivo *36,* e  se il timer SubClass_C2_timer_T4 è attivo, Verifica che   *47,48,50,*   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* e  che  *34,*  il parametro SubClass_C2_parametro_P1 sia  uguale a c270
    //   *104,* e  che  *,*  la variabile SubClass_C2_variabile_V6 non sia  uguale a GialloVerde
    //   *104,* o  che  *34,*  il parametro SubClass_C2_parametro_P5 sia  uguale a RossoVerde
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_AndLogicOP_3 = true;
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (L_P1__GetInConsd1(my_id) == false));
    bool res_ForAllPredicate_4 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl8Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl8(my_id,i);
    bool res_ImpliesLogicOp_5 = true;
    if((Counter_GetValore(L_P1__GetMainc38(it.mainc39)) < 110u)){
    res_ImpliesLogicOp_5 = (res_ImpliesLogicOp_5 && Timer_Attivo(L_P1__GetMainc35(it.mainc39)));
    }
    res_ForAllPredicate_4 = res_ImpliesLogicOp_5;
    if(!res_ForAllPredicate_4) {break;}
    }
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_ForAllPredicate_4);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_3);
    bool res_AndLogicOP_6 = true;
    bool res_AndLogicOP_7 = true;
    res_AndLogicOP_7 = (res_AndLogicOP_7 && Timer_Disattivo(L_P1__GetSubcl49(my_id)));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && Timer_Attivo(L_P1__GetSubcl48(my_id)));
    
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_AndLogicOP_7);
    res_AndLogicOP_6 = (res_AndLogicOP_6 && Timer_Attivo(L_P1__GetSubcl48(my_id)));
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_6);
    
    if(res_OrLogicOP_2){
    bool res_OrLogicOP_8 = false;
    bool res_AndLogicOP_9 = true;
    bool res_AndLogicOP_10 = true;
    res_AndLogicOP_10 = (res_AndLogicOP_10 && (L_P1__GetInConsd1(my_id) == false));
    res_AndLogicOP_10 = (res_AndLogicOP_10 && (L_P1__GetParamSubcl10(my_id) == c270));
    
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_AndLogicOP_10);
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (L_P1__GetSubcl36(my_id) == gialloverde));
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_NotLogicOP_11);
    
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_AndLogicOP_9);
    res_OrLogicOP_8 = (res_OrLogicOP_8 || (L_P1__GetParamSubcl12(my_id) == rossoverde));
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_OrLogicOP_8);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    
    
    return res_AndLogicOP_0;
}


// Macro valorizzate

/*
    CNL corrispondente:
    
    { commento: {[}
     commento: {46,} assegna alla macro il valore  False  commento: {],}
    }
*/
bool L_P1__Macro6(instance_id_t const my_id , C2_Enumerat1 argom6, bool argom7, C2_Enumerat3 argom8, C2_Enumerat2 argom9)
{
return false;
}

/*
    CNL corrispondente:
    
    { commento: {[}
     commento: {46,} assegna alla macro il valore  True  commento: {],}
    }
*/
bool L_P1__Macro7(instance_id_t const my_id , C2_Enumerat4 argom10, C2_Enumerat4 argom11, C2_Enumerat1 argom12, C2_Enumerat4 argom13, C2_Enumerat2 argom14, C2_Enumerat1 argom15, C2_Enumerat4 argom16)
{
return true;
}

/*
    CNL corrispondente:
    
    { commento: {[}
     commento: {46,} assegna alla macro il valore c270 commento: {],}
    }
*/
C2_Enumerat2 L_P1__Macro8(instance_id_t const my_id , C2_Enumerat4 argom17, C2_Enumerat1 argom18)
{
return c270;
}

/*
    CNL corrispondente:
    
    { commento: {[}
     commento: {46,} assegna alla macro il valore c120x commento: {],}
    }
*/
C2_Enumerat4 L_P1__Macro9(instance_id_t const my_id , C2_Enumerat1 argom19, C2_Enumerat2 argom20, C2_Enumerat2 argom21, bool argom22, C2_Enumerat2 argom23, C2_Enumerat3 argom24)
{
return c120x;
}

/*
    CNL corrispondente:
    
    { commento: {[} commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L2 è  diverso da  commento: {56,}  state1  o  se la macro  SubClass_C2_macrova_M8 ( con argomento_a7   uguale a True ,argomento_a4   uguale a c270 ,argomento_a8   uguale a Rosso ,argomento_a9   uguale a avanzamento ,argomento_a1   uguale a GialloVerde  e argomento_a2   uguale a Rosso )  non  è  uguale a c120x commento: {40,} ,  commento: {41,}  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L2 è  diverso da  False , commento: {88,} quando  commento: {41,}   MainClass_C1_parametro_P3 del campo  MainClass_C1     è  diverso da  False  commento: {110,} e  se il ripristino del timer  SubClass_C2_restoreTI_TI2 è scaduto commento: {109,} o  se il ripristino della variabile  SubClass_C2_restoreva_RV3 è  uguale a  commento: {53,} 1 commento: {35,} o  se il controllo SubClass_C2_controllo_C7 non è  uguale a GialloVerde commento: {43,} e  se MainClass_C1_timer_T1 del campo  MainClass_C1 di SubClass_C2_lista_L1 esiste e  commento: {105,} è disattivo , assegna alla macro il valore c120x
    
     commento: {46,} assegna alla macro il valore c120x commento: {],}
    }
*/
C2_Enumerat4 L_P1__Macro10(instance_id_t const my_id , C2_Enumerat3 argom25, C2_Enumerat1 argom26, bool argom27, C2_Enumerat3 argom28, C2_Enumerat2 argom29, C2_Enumerat4 argom30)
{
C2_Enumerat4 res_macro_val;
    
    //  *[* *111,*  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L2 è  diverso da  *56,*  state1  o  se la macro  SubClass_C2_macrova_M8 ( con argomento_a7   uguale a True ,argomento_a4   uguale a c270 ,argomento_a8   uguale a Rosso ,argomento_a9   uguale a avanzamento ,argomento_a1   uguale a GialloVerde  e argomento_a2   uguale a Rosso )  non  è  uguale a c120x *40,* ,  *41,*  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L2 è  diverso da  False , *88,* quando  *41,*   MainClass_C1_parametro_P3 del campo  MainClass_C1     è  diverso da  False  *110,* e  se il ripristino del timer  SubClass_C2_restoreTI_TI2 è scaduto *109,* o  se il ripristino della variabile  SubClass_C2_restoreva_RV3 è  uguale a  *53,* 1 *35,* o  se il controllo SubClass_C2_controllo_C7 non è  uguale a GialloVerde *43,* e  se MainClass_C1_timer_T1 del campo  MainClass_C1 di SubClass_C2_lista_L1 esiste e  *105,* è disattivo
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_OrLogicOP_2 = false;
    bool res_ForAllPredicate_3 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl9Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl9(my_id,i);
    bool res_ImpliesLogicOp_4 = true;
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1_C1_GetState(it.mainc39) == C1_St_state));
    res_ImpliesLogicOp_4 = (res_ImpliesLogicOp_4 && res_NotLogicOP_5);
    res_ForAllPredicate_3 = res_ImpliesLogicOp_4;
    if(!res_ForAllPredicate_3) {break;}
    }
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_ForAllPredicate_3);
    bool res_AndLogicOP_6 = true;
    bool res_AndLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__Macro9(my_id,gialloverde,rosso,c270,true,rosso,avanzamento) == c120x));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_8);
    bool res_ForAllPredicate_9 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl9Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl9(my_id,i);
    bool res_ImpliesLogicOp_10 = true;
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (L_P1__GetParamMainc8(it.mainc39) == false));
    if(res_NotLogicOP_11){
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (L_P1__GetParamMainc8(it.mainc39) == false));
    res_ImpliesLogicOp_10 = (res_ImpliesLogicOp_10 && res_NotLogicOP_12);
    }
    res_ForAllPredicate_9 = res_ImpliesLogicOp_10;
    if(!res_ForAllPredicate_9) {break;}
    }
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_ForAllPredicate_9);
    
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_AndLogicOP_7);
    res_AndLogicOP_6 = (res_AndLogicOP_6 && Timer_Scaduto(L_P1__GetSubcl41(my_id)));
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_6);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_OrLogicOP_2);
    res_OrLogicOP_1 = (res_OrLogicOP_1 || (L_P1__GetSubcl33(my_id) == 1u));
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_AndLogicOP_13 = true;
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1__GetInSubcl7(my_id) == gialloverde));
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_NotLogicOP_14);
    bool res_ForAllPredicateNotEmpty_15 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl8Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl8(my_id,i);
    bool res_ImpliesLogicOp_16 = true;
    res_ImpliesLogicOp_16 = (res_ImpliesLogicOp_16 && Timer_Disattivo(L_P1__GetMainc35(it.mainc39)));
    res_ForAllPredicateNotEmpty_15 = res_ImpliesLogicOp_16;
    if(!res_ForAllPredicateNotEmpty_15) {break;}
    }
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_ForAllPredicateNotEmpty_15);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_13);
    
    if(res_OrLogicOP_0){
    
    res_macro_val = c120x;
    }
    else{
    res_macro_val = c120x;
    }
    return res_macro_val;
}



