// Codice del modello 'TestCase19', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#include "Logica/ClasseMainClass_C1.h"
#include "Logica/ClasseSubClass_C2.h"
#include "Logica/ClasseMainClass_C1_priv.h"
#include "config.h"
#include "scheduler.h"


// ********** Gestione comandi automatici **********

static size_t L_P1_C1_NumAutoCmds(instance_id_t const my_id)
{
    size_t n = 0u;
    if (L_P1__GetCAEvent(my_id)) {
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
static inline bool L_P1__Guard(instance_id_t const my_id)
{
    return true;
}


/*
    CNL corrispondente:
    
    {
    
     commento: {67,} commento: {34,}  se il parametro MainClass_C1_parametro_P10 non è  uguale a GialloVerde commento: {37,} o  se la variabile MainClass_C1_variabile_V4 non è  uguale a  False  commento: {38,} o  se il contatore MainClass_C1_contatore_Co1 non è  maggiore di  commento: {54,} 15 e  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} o  se il timer MainClass_C1_timer_T4 è disattivo, Tutte le seguenti { 
     commento: {68,} commento: {38,}  se il contatore MainClass_C1_contatore_Co6 è  uguale a  commento: {53,} 144 commento: {34,} o  se il parametro MainClass_C1_parametro_P9 è  uguale a  commento: {53,} 8 commento: {34,} e  se il parametro MainClass_C1_parametro_P10 è  uguale a GialloVerde commento: {34,} e  se il parametro MainClass_C1_parametro_P9 è  uguale a  commento: {53,} 7 commento: {37,} e  se la variabile MainClass_C1_variabile_V7 non è  diverso da c180x, Almeno una delle seguenti { 
     commento: {69,} commento: {35,}  se il controllo MainClass_C1_controllo_C8 è  diverso da  False  o  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} o  se il parametro MainClass_C1_parametro_P10 è  diverso da GialloVerde commento: {36,} o  se il timer MainClass_C1_timer_T3 è attivo commento: {37,} e  se la variabile MainClass_C1_variabile_V3 è  diverso da  commento: {56,} 6 commento: {38,} e  se il contatore MainClass_C1_contatore_Co6 è  diverso da  commento: {56,} 145, Solo una delle seguenti { 
     commento: {68,}  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} e  se la variabile MainClass_C1_variabile_V3 è  maggiore di  commento: {54,} 2 commento: {34,} o  se il parametro MainClass_C1_parametro_P9 è  diverso da  commento: {56,} 5, Almeno una delle seguenti { 
      se il controllo ConsDef  è  uguale a FALSE , Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
    
    
     } Verifica che   commento: {48,}  commento: {,}  il controllo MainClass_C1_controllo_C8 non sia  uguale a  False 
    
    
     } Verifica che   commento: {47,}  commento: {34,}  il parametro MainClass_C1_parametro_P9 sia  diverso da  commento: {56,} 2
    
    
     } Verifica che   commento: {49,}  commento: {,}  il timer MainClass_C1_timer_T2 non sia scaduto
    
    
     } Verifica che   commento: {51,}  commento: {,}  il contatore MainClass_C1_contatore_Co6 sia  uguale a  commento: {53,} 1332
    
    
    }
*/
static inline bool L_P1__Guard1(instance_id_t const my_id)
{
    bool res_AndLogicOP_0 = true;
    
    //  *67,* *34,*  se il parametro MainClass_C1_parametro_P10 non è  uguale a GialloVerde *37,* o  se la variabile MainClass_C1_variabile_V4 non è  uguale a  False  *38,* o  se il contatore MainClass_C1_contatore_Co1 non è  maggiore di  *54,* 15 e  se il controllo ConsDef  è  uguale a FALSE  *36,* o  se il timer MainClass_C1_timer_T4 è disattivo, Tutte le seguenti { 
    //   *68,* *38,*  se il contatore MainClass_C1_contatore_Co6 è  uguale a  *53,* 144 *34,* o  se il parametro MainClass_C1_parametro_P9 è  uguale a  *53,* 8 *34,* e  se il parametro MainClass_C1_parametro_P10 è  uguale a GialloVerde *34,* e  se il parametro MainClass_C1_parametro_P9 è  uguale a  *53,* 7 *37,* e  se la variabile MainClass_C1_variabile_V7 non è  diverso da c180x, Almeno una delle seguenti { 
    //   *69,* *35,*  se il controllo MainClass_C1_controllo_C8 è  diverso da  False  o  se il controllo ConsDef  è  uguale a FALSE  *34,* o  se il parametro MainClass_C1_parametro_P10 è  diverso da GialloVerde *36,* o  se il timer MainClass_C1_timer_T3 è attivo *37,* e  se la variabile MainClass_C1_variabile_V3 è  diverso da  *56,* 6 *38,* e  se il contatore MainClass_C1_contatore_Co6 è  diverso da  *56,* 145, Solo una delle seguenti { 
    //   *68,*  se il controllo ConsDef  è  uguale a FALSE  *37,* e  se la variabile MainClass_C1_variabile_V3 è  maggiore di  *54,* 2 *34,* o  se il parametro MainClass_C1_parametro_P9 è  diverso da  *56,* 5, Almeno una delle seguenti { 
    //    se il controllo ConsDef  è  uguale a FALSE , Verifica che   *48,*   il controllo ConsDef  sia  uguale a FALSE 
    //   } Verifica che   *48,*  *,*  il controllo MainClass_C1_controllo_C8 non sia  uguale a  False 
    //   } Verifica che   *47,*  *34,*  il parametro MainClass_C1_parametro_P9 sia  diverso da  *56,* 2
    //   } Verifica che   *49,*  *,*  il timer MainClass_C1_timer_T2 non sia scaduto
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_OrLogicOP_4 = false;
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetParamMainc6(my_id) == gialloverde));
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_NotLogicOP_5);
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetMainc27(my_id) == false));
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_NotLogicOP_6);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_OrLogicOP_4);
    bool res_AndLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (Counter_GetValore(L_P1__GetMainc36(my_id)) > 15u));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_8);
    res_AndLogicOP_7 = (res_AndLogicOP_7 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_AndLogicOP_7);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    res_OrLogicOP_2 = (res_OrLogicOP_2 || Timer_Disattivo(L_P1__GetMainc35(my_id)));
    
    if(res_OrLogicOP_2){
    bool res_AndLogicOP_9 = true;
    bool res_ImpliesLogicOp_10 = true;
    bool res_OrLogicOP_11 = false;
    res_OrLogicOP_11 = (res_OrLogicOP_11 || (Counter_GetValore(L_P1__GetMainc37(my_id)) == 144u));
    bool res_AndLogicOP_12 = true;
    bool res_AndLogicOP_13 = true;
    bool res_AndLogicOP_14 = true;
    res_AndLogicOP_14 = (res_AndLogicOP_14 && (L_P1__GetParamMainc7(my_id) == 8u));
    res_AndLogicOP_14 = (res_AndLogicOP_14 && (L_P1__GetParamMainc6(my_id) == gialloverde));
    
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_AndLogicOP_14);
    res_AndLogicOP_13 = (res_AndLogicOP_13 && (L_P1__GetParamMainc7(my_id) == 7u));
    
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_AndLogicOP_13);
    bool res_NotLogicOP_15 = true;
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (L_P1__GetMainc28(my_id) == c180x));
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! res_NotLogicOP_16);
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_NotLogicOP_15);
    
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_AndLogicOP_12);
    
    if(res_OrLogicOP_11){
    bool res_OrLogicOP_17 = false;
    bool res_ImpliesLogicOp_18 = true;
    bool res_OrLogicOP_19 = false;
    bool res_OrLogicOP_20 = false;
    bool res_OrLogicOP_21 = false;
    bool res_NotLogicOP_22 = true;
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! (L_P1__GetInMainc4(my_id) == false));
    res_OrLogicOP_21 = (res_OrLogicOP_21 || res_NotLogicOP_22);
    res_OrLogicOP_21 = (res_OrLogicOP_21 || (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_20 = (res_OrLogicOP_20 || res_OrLogicOP_21);
    bool res_NotLogicOP_23 = true;
    res_NotLogicOP_23 = (res_NotLogicOP_23 && ! (L_P1__GetParamMainc6(my_id) == gialloverde));
    res_OrLogicOP_20 = (res_OrLogicOP_20 || res_NotLogicOP_23);
    
    res_OrLogicOP_19 = (res_OrLogicOP_19 || res_OrLogicOP_20);
    bool res_AndLogicOP_24 = true;
    bool res_AndLogicOP_25 = true;
    res_AndLogicOP_25 = (res_AndLogicOP_25 && Timer_Attivo(L_P1__GetMainc34(my_id)));
    bool res_NotLogicOP_26 = true;
    res_NotLogicOP_26 = (res_NotLogicOP_26 && ! (L_P1__GetMainc26(my_id) == 6u));
    res_AndLogicOP_25 = (res_AndLogicOP_25 && res_NotLogicOP_26);
    
    res_AndLogicOP_24 = (res_AndLogicOP_24 && res_AndLogicOP_25);
    bool res_NotLogicOP_27 = true;
    res_NotLogicOP_27 = (res_NotLogicOP_27 && ! (Counter_GetValore(L_P1__GetMainc37(my_id)) == 145u));
    res_AndLogicOP_24 = (res_AndLogicOP_24 && res_NotLogicOP_27);
    
    res_OrLogicOP_19 = (res_OrLogicOP_19 || res_AndLogicOP_24);
    
    if(res_OrLogicOP_19){
    bool res_XorLogicOP_28 = true;
    int xorIndex_res_XorLogicOP_28 = 0;
    bool res_ImpliesLogicOp_29 = true;
    bool res_OrLogicOP_30 = false;
    bool res_AndLogicOP_31 = true;
    res_AndLogicOP_31 = (res_AndLogicOP_31 && (L_P1__GetInConsd(my_id) == false));
    res_AndLogicOP_31 = (res_AndLogicOP_31 && (L_P1__GetMainc26(my_id) > 2u));
    
    res_OrLogicOP_30 = (res_OrLogicOP_30 || res_AndLogicOP_31);
    bool res_NotLogicOP_32 = true;
    res_NotLogicOP_32 = (res_NotLogicOP_32 && ! (L_P1__GetParamMainc7(my_id) == 5u));
    res_OrLogicOP_30 = (res_OrLogicOP_30 || res_NotLogicOP_32);
    
    if(res_OrLogicOP_30){
    bool res_ImpliesLogicOp_33 = true;
    if((L_P1__GetInConsd(my_id) == false)){
    res_ImpliesLogicOp_33 = (res_ImpliesLogicOp_33 && (L_P1__GetInConsd(my_id) == false));
    }
    res_ImpliesLogicOp_29 = (res_ImpliesLogicOp_29 && res_ImpliesLogicOp_33);
    }
    if(res_ImpliesLogicOp_29){
    xorIndex_res_XorLogicOP_28 = (xorIndex_res_XorLogicOP_28 + 1);
    }
    bool res_NotLogicOP_34 = true;
    res_NotLogicOP_34 = (res_NotLogicOP_34 && ! (L_P1__GetInMainc4(my_id) == false));
    if(res_NotLogicOP_34){
    xorIndex_res_XorLogicOP_28 = (xorIndex_res_XorLogicOP_28 + 1);
    }
    
    res_XorLogicOP_28 = (res_XorLogicOP_28 && (xorIndex_res_XorLogicOP_28 == 1));
    res_ImpliesLogicOp_18 = (res_ImpliesLogicOp_18 && res_XorLogicOP_28);
    }
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_ImpliesLogicOp_18);
    bool res_NotLogicOP_35 = true;
    res_NotLogicOP_35 = (res_NotLogicOP_35 && ! (L_P1__GetParamMainc7(my_id) == 2u));
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_NotLogicOP_35);
    
    res_ImpliesLogicOp_10 = (res_ImpliesLogicOp_10 && res_OrLogicOP_17);
    }
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_ImpliesLogicOp_10);
    bool res_NotLogicOP_36 = true;
    res_NotLogicOP_36 = (res_NotLogicOP_36 && ! Timer_Scaduto(L_P1__GetMainc33(my_id)));
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_NotLogicOP_36);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_AndLogicOP_9);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *51,*  *,*  il contatore MainClass_C1_contatore_Co6 sia  uguale a  *53,* 1332
    res_AndLogicOP_0 = (res_AndLogicOP_0 && (Counter_GetValore(L_P1__GetMainc37(my_id)) == 1332u));
    
    
    
    return res_AndLogicOP_0;
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
    
      se il ripristino dello stato  è  diverso da  commento: {56,}  state1  commento: {107,}, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V4 il valore  False 
    
       
      se la macro  MainClass_C1_macrova_M6 ( con argomento_a6   uguale a True ,argomento_a9   uguale a Verde ,argomento_a4   uguale a AC ,argomento_a3   uguale a GialloVerde ,argomento_a7   uguale a c180 ,argomento_a2   uguale a RossoGialloxVerdex  e argomento_a1   uguale a RossoGialloxVerdex )   è  diverso da  False  commento: {40,}  commento: {37,} e  se la variabile MainClass_C1_variabile_V10 non è  uguale a  commento: {53,} 6 commento: {36,} e  se il timer MainClass_C1_timer_T4 è scaduto commento: {35,} o  se il controllo MainClass_C1_controllo_C8 è  uguale a  True , commento: {67,} Assegna alla variabile MainClass_C1_variabile_V4 il valore  True 
    
     ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V3 il valore 2
    
    
    
    }
*/
static inline void L_P1__Effec1(instance_id_t const my_id)
{
    
    //  se il ripristino dello stato  è  diverso da  *56,*  state1  *107,*, *67,* Assegna alla variabile MainClass_C1_variabile_V4 il valore  False
    bool res_NotLogicOP_0 = true;
    res_NotLogicOP_0 = (res_NotLogicOP_0 && ! (L_P1__GetStato1(my_id) == C1_St_state));
    if(res_NotLogicOP_0){
    
    L_P1__SetMainc27(my_id,false);
    }
    
    //  se la macro  MainClass_C1_macrova_M6 ( con argomento_a6   uguale a True ,argomento_a9   uguale a Verde ,argomento_a4   uguale a AC ,argomento_a3   uguale a GialloVerde ,argomento_a7   uguale a c180 ,argomento_a2   uguale a RossoGialloxVerdex  e argomento_a1   uguale a RossoGialloxVerdex )   è  diverso da  False  *40,*  *37,* e  se la variabile MainClass_C1_variabile_V10 non è  uguale a  *53,* 6 *36,* e  se il timer MainClass_C1_timer_T4 è scaduto *35,* o  se il controllo MainClass_C1_controllo_C8 è  uguale a  True , *67,* Assegna alla variabile MainClass_C1_variabile_V4 il valore  True 
    //   ,altrimenti  *67,* Assegna alla variabile MainClass_C1_variabile_V3 il valore 2
    bool res_OrLogicOP_1 = false;
    bool res_AndLogicOP_2 = true;
    bool res_AndLogicOP_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__Macro1(my_id,rossogiallo,rossogiallo,gialloverde,ac,true,c180,verde) == false));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_4);
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetMainc25(my_id) == 6u));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_5);
    
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_AndLogicOP_3);
    res_AndLogicOP_2 = (res_AndLogicOP_2 && Timer_Scaduto(L_P1__GetMainc35(my_id)));
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_2);
    res_OrLogicOP_1 = (res_OrLogicOP_1 || (L_P1__GetInMainc4(my_id) == true));
    
    if(res_OrLogicOP_1){
    
    L_P1__SetMainc27(my_id,true);
    }else{
    
    L_P1__SetMainc26(my_id,2u);
    }
}



// ********** Definizione metodi **********

// Metodi standard

void L_P1_C1_Init(instance_id_t const my_id)
{
    // init variabili di stato
    L_P1__SetMainc10(my_id, verde);
    L_P1__SetMainc12(my_id, 0);
    L_P1__SetMainc14(my_id, false);
    L_P1__SetMainc16(my_id, 0);
    L_P1__SetMainc18(my_id, 0);
    L_P1__SetMainc19(my_id, 0);
    L_P1__SetMainc20(my_id, false);
    L_P1__SetMainc21(my_id, false);
    L_P1__SetMainc22(my_id, rossoverde);
    L_P1__SetMainc23(my_id, rossoverde);
    L_P1__SetMainc24(my_id, false);
    L_P1__SetMainc25(my_id, 0);
    L_P1__SetMainc26(my_id, 0);
    L_P1__SetMainc27(my_id, false);
    L_P1__SetMainc28(my_id, rossoverde);
    L_P1__SetStato1(my_id, C1_St_Stato);
    // init controlli precedenti
    L_P1__SetMainc9(my_id, true);
    // init Timer e Counter
    Timer_AggmInit(L_P1__GetMainc29(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc29_ID);
    Timer_Init(L_P1__GetMainc29(my_id), 3000);
    Timer_AggmInit(L_P1__GetMainc30(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc30_ID);
    Timer_Init(L_P1__GetMainc30(my_id), 3000);
    Timer_AggmInit(L_P1__GetMainc31(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc31_ID);
    Timer_Init(L_P1__GetMainc31(my_id), 34000);
    Timer_AggmInit(L_P1__GetMainc32(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc32_ID);
    Timer_Init(L_P1__GetMainc32(my_id), 34000);
    Timer_AggmInit(L_P1__GetMainc33(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc33_ID);
    Timer_Init(L_P1__GetMainc33(my_id), 3000);
    Timer_AggmInit(L_P1__GetMainc34(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc34_ID);
    Timer_Init(L_P1__GetMainc34(my_id), 310000);
    Timer_AggmInit(L_P1__GetMainc35(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc35_ID);
    Timer_Init(L_P1__GetMainc35(my_id), 432000);
    Counter_AggmInit(L_P1__GetMainc36(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc36_ID);
    Counter_Init(L_P1__GetMainc36(my_id));
    Counter_AggmInit(L_P1__GetMainc37(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc37_ID);
    Counter_Init(L_P1__GetMainc37(my_id));
    Counter_AggmInit(L_P1__GetMainc38(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc38_ID);
    Counter_Init(L_P1__GetMainc38(my_id));
    // init response
    L_P1_C1_SetResponse(my_id, LDS_SCHED_NOP);

    // transizione iniziale
    if(L_P1__Guard(my_id)) {
        L_P1_C1_SetState(my_id, C1_St_state);
	L_P1__Effec(my_id);
    } else {
        STOP_EXECUTION(LOGIC_ERROR);
    }
    // init variabili precedenti
    L_P1__SetMainc11(my_id, L_P1__GetMainc10(my_id));
    L_P1__SetMainc13(my_id, L_P1__GetMainc12(my_id));
    L_P1__SetMainc15(my_id, L_P1__GetMainc14(my_id));
    L_P1__SetMainc17(my_id, L_P1__GetMainc16(my_id));
}

void L_P1_C1_Exec(instance_id_t const my_id, Phase const p)
{
    L_P1_C1_SetResponse(my_id, LDS_SCHED_NOP);
    switch (p) {

    case LDS_PHASE_MANUAL:
        break;
 

    case LDS_PHASE_STATE:

        switch (L_P1_C1_GetState(my_id)) {

        case C1_St_state:
            if (L_P1__Guard1(my_id)) {
                L_P1_C1_SetState(my_id, C1_St_state);
                L_P1__Effec1(my_id);				
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
    Timer_Exec(L_P1__GetMainc29(my_id));
    Timer_Exec(L_P1__GetMainc30(my_id));
    Timer_Exec(L_P1__GetMainc31(my_id));
    Timer_Exec(L_P1__GetMainc32(my_id));
    Timer_Exec(L_P1__GetMainc33(my_id));
    Timer_Exec(L_P1__GetMainc34(my_id));
    Timer_Exec(L_P1__GetMainc35(my_id));
}

void L_P1_C1_GSetSafe(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C1(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C1(proc_id);
    L_P1__SetOutMainc(my_id, c180x);
    L_P1__SetOutMainc1(my_id, c180x);
    L_P1__SetOutMainc2(my_id, c180);
}

void L_P1_C1_GUpdatePrev(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C1(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C1(proc_id);
    L_P1__SetMainc9(my_id, L_P1__GetInMainc8(my_id));
    L_P1__SetMainc11(my_id, L_P1__GetMainc10(my_id));
    L_P1__SetMainc13(my_id, L_P1__GetMainc12(my_id));
    L_P1__SetMainc15(my_id, L_P1__GetMainc14(my_id));
    L_P1__SetMainc17(my_id, L_P1__GetMainc16(my_id));
}

// ********** Definizione macro **********

// Macro di effetto

/*
    CNL corrispondente:
    
    {  se il controllo ConsDef  è  uguale a FALSE , commento: {69,}Disattiva il timer MainClass_C1_timer_T4
    
       
    
    }
*/
void L_P1__Macro(instance_id_t const my_id )
{
//  se il controllo ConsDef  è  uguale a FALSE , *69,*Disattiva il timer MainClass_C1_timer_T4
    if((L_P1__GetInConsd(my_id) == false)){
    
    Timer_Disattiva(L_P1__GetMainc35(my_id));
    }
}


// Macro di verifica

/*
    CNL corrispondente:
    
    { commento: {62,} commento: {37,}  se la variabile MainClass_C1_variabile_V3 non è  maggiore di  commento: {54,} 10 commento: {37,} e  se la variabile MainClass_C1_variabile_V3 è  uguale a  commento: {53,} 8, Almeno una delle seguenti { 
     commento: {63,} commento: {34,}  se lo stato  non è  uguale a  commento: {53,}  state1  commento: {106,} commento: {36,} e  se il timer MainClass_C1_timer_T4 è scaduto, Solo una delle seguenti { 
     commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI2 non è attivo, Verifica che   commento: {48,52,}  commento: {,}  il controllo MainClass_C1_controllo_C7 sia  diverso da  True 
     commento: {104,} e  che   l'argomento argomento_ave9 non  sia  diverso da c180 commento: {,} 
     commento: {104,} e  che  commento: {35,}  il controllo MainClass_C1_controllo_C7 sia  diverso da  True 
    
    
     } Verifica che   commento: {47,51,52,}  commento: {,}  il contatore MainClass_C1_contatore_Co6 non sia  diverso da  commento: {56,} 11
     commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P1 sia  uguale a c180
     commento: {104,} e  che   l'argomento argomento_ave6 sia  uguale a GialloVerde commento: {,} 
     commento: {104,} o  che  commento: {38,}  il contatore MainClass_C1_contatore_Co7 sia  minore di  commento: {55,} 113
    
    
     } Verifica che   commento: {47,49,51,52,}  commento: {34,}  il parametro MainClass_C1_parametro_P10 sia  diverso da GialloVerde
     commento: {104,} e  che   l'argomento argomento_ave3 non  sia  diverso da c180x commento: {,} 
     commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co1 sia  maggiore di  commento: {54,} 11
     commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T2 sia attivo
     commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P9 non sia  diverso da  commento: {56,} 5
     commento: {104,} e  che  commento: {36,}  il timer MainClass_C1_timer_T4 sia attivo
    
    
    }
*/
bool L_P1__Macro2(instance_id_t const my_id , C1_Enumerat2 argom9, C1_Enumerat3 argom10, C1_Enumerat4 argom11, bool argom12, C1_Enumerat3 argom13, bool argom14, C1_Enumerat2 argom15)
{
bool res_AndLogicOP_0 = true;
    
    //  *62,* *37,*  se la variabile MainClass_C1_variabile_V3 non è  maggiore di  *54,* 10 *37,* e  se la variabile MainClass_C1_variabile_V3 è  uguale a  *53,* 8, Almeno una delle seguenti { 
    //   *63,* *34,*  se lo stato  non è  uguale a  *53,*  state1  *106,* *36,* e  se il timer MainClass_C1_timer_T4 è scaduto, Solo una delle seguenti { 
    //   *110,*  se il ripristino del timer  MainClass_C1_restoreTI_TI2 non è attivo, Verifica che   *48,52,*  *,*  il controllo MainClass_C1_controllo_C7 sia  diverso da  True 
    //   *104,* e  che   l'argomento argomento_ave9 non  sia  diverso da c180 *,* 
    //   *104,* e  che  *35,*  il controllo MainClass_C1_controllo_C7 sia  diverso da  True 
    //   } Verifica che   *47,51,52,*  *,*  il contatore MainClass_C1_contatore_Co6 non sia  diverso da  *56,* 11
    //   *104,* e  che  *34,*  il parametro MainClass_C1_parametro_P1 sia  uguale a c180
    //   *104,* e  che   l'argomento argomento_ave6 sia  uguale a GialloVerde *,* 
    //   *104,* o  che  *38,*  il contatore MainClass_C1_contatore_Co7 sia  minore di  *55,* 113
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_AndLogicOP_2 = true;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__GetMainc26(my_id) > 10u));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_3);
    res_AndLogicOP_2 = (res_AndLogicOP_2 && (L_P1__GetMainc26(my_id) == 8u));
    
    if(res_AndLogicOP_2){
    bool res_OrLogicOP_4 = false;
    bool res_ImpliesLogicOp_5 = true;
    bool res_AndLogicOP_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1_C1_GetState(my_id) == C1_St_state));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_7);
    res_AndLogicOP_6 = (res_AndLogicOP_6 && Timer_Scaduto(L_P1__GetMainc35(my_id)));
    
    if(res_AndLogicOP_6){
    bool res_ImpliesLogicOp_8 = true;
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! Timer_Attivo(L_P1__GetMainc32(my_id)));
    if(res_NotLogicOP_9){
    bool res_AndLogicOP_10 = true;
    bool res_AndLogicOP_11 = true;
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (L_P1__GetInMainc3(my_id) == true));
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_NotLogicOP_12);
    bool res_NotLogicOP_13 = true;
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (argom15 == c180));
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! res_NotLogicOP_14);
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_NotLogicOP_13);
    
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_AndLogicOP_11);
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (L_P1__GetInMainc3(my_id) == true));
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_NotLogicOP_15);
    
    res_ImpliesLogicOp_8 = (res_ImpliesLogicOp_8 && res_AndLogicOP_10);
    }
    res_ImpliesLogicOp_5 = (res_ImpliesLogicOp_5 && res_ImpliesLogicOp_8);
    }
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_ImpliesLogicOp_5);
    bool res_OrLogicOP_16 = false;
    bool res_AndLogicOP_17 = true;
    bool res_AndLogicOP_18 = true;
    bool res_NotLogicOP_19 = true;
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! (Counter_GetValore(L_P1__GetMainc37(my_id)) == 11u));
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! res_NotLogicOP_20);
    res_AndLogicOP_18 = (res_AndLogicOP_18 && res_NotLogicOP_19);
    res_AndLogicOP_18 = (res_AndLogicOP_18 && (L_P1__GetParamMainc5(my_id) == c180));
    
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_AndLogicOP_18);
    res_AndLogicOP_17 = (res_AndLogicOP_17 && (argom13 == gialloverde));
    
    res_OrLogicOP_16 = (res_OrLogicOP_16 || res_AndLogicOP_17);
    res_OrLogicOP_16 = (res_OrLogicOP_16 || (Counter_GetValore(L_P1__GetMainc38(my_id)) < 113u));
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_OrLogicOP_16);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_OrLogicOP_4);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *47,49,51,52,*  *34,*  il parametro MainClass_C1_parametro_P10 sia  diverso da GialloVerde
    //   *104,* e  che   l'argomento argomento_ave3 non  sia  diverso da c180x *,* 
    //   *104,* e  che  *,*  il contatore MainClass_C1_contatore_Co1 sia  maggiore di  *54,* 11
    //   *104,* o  che  *,*  il timer MainClass_C1_timer_T2 sia attivo
    //   *104,* e  che  *34,*  il parametro MainClass_C1_parametro_P9 non sia  diverso da  *56,* 5
    //   *104,* e  che  *36,*  il timer MainClass_C1_timer_T4 sia attivo
    bool res_OrLogicOP_21 = false;
    bool res_AndLogicOP_22 = true;
    bool res_AndLogicOP_23 = true;
    bool res_NotLogicOP_24 = true;
    res_NotLogicOP_24 = (res_NotLogicOP_24 && ! (L_P1__GetParamMainc6(my_id) == gialloverde));
    res_AndLogicOP_23 = (res_AndLogicOP_23 && res_NotLogicOP_24);
    bool res_NotLogicOP_25 = true;
    bool res_NotLogicOP_26 = true;
    res_NotLogicOP_26 = (res_NotLogicOP_26 && ! (argom11 == c180x));
    res_NotLogicOP_25 = (res_NotLogicOP_25 && ! res_NotLogicOP_26);
    res_AndLogicOP_23 = (res_AndLogicOP_23 && res_NotLogicOP_25);
    
    res_AndLogicOP_22 = (res_AndLogicOP_22 && res_AndLogicOP_23);
    res_AndLogicOP_22 = (res_AndLogicOP_22 && (Counter_GetValore(L_P1__GetMainc36(my_id)) > 11u));
    
    res_OrLogicOP_21 = (res_OrLogicOP_21 || res_AndLogicOP_22);
    bool res_AndLogicOP_27 = true;
    bool res_AndLogicOP_28 = true;
    res_AndLogicOP_28 = (res_AndLogicOP_28 && Timer_Attivo(L_P1__GetMainc33(my_id)));
    bool res_NotLogicOP_29 = true;
    bool res_NotLogicOP_30 = true;
    res_NotLogicOP_30 = (res_NotLogicOP_30 && ! (L_P1__GetParamMainc7(my_id) == 5u));
    res_NotLogicOP_29 = (res_NotLogicOP_29 && ! res_NotLogicOP_30);
    res_AndLogicOP_28 = (res_AndLogicOP_28 && res_NotLogicOP_29);
    
    res_AndLogicOP_27 = (res_AndLogicOP_27 && res_AndLogicOP_28);
    res_AndLogicOP_27 = (res_AndLogicOP_27 && Timer_Attivo(L_P1__GetMainc35(my_id)));
    
    res_OrLogicOP_21 = (res_OrLogicOP_21 || res_AndLogicOP_27);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_21);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
    
    { commento: {63,} commento: {34,}  se il parametro MainClass_C1_parametro_P10 è  uguale a GialloVerde commento: {38,} o  se il contatore MainClass_C1_contatore_Co6 è  minore di  commento: {55,} 121 commento: {36,} e  se il timer MainClass_C1_timer_T2 è scaduto o  se l'argomento argomento_ave6 non  è  uguale a c180x commento: {39,} , Solo una delle seguenti { 
     commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è scaduto, Verifica che   commento: {48,}  commento: {,}  il controllo MainClass_C1_controllo_C7 sia  diverso da  True 
    
    
     } Verifica che   commento: {47,49,}  commento: {,}  il timer MainClass_C1_timer_T4 non sia disattivo
     commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P10 non sia  diverso da GialloVerde
    
    
    }
*/
bool L_P1__Macro3(instance_id_t const my_id , bool argom16, C1_Enumerat1 argom17, C1_Enumerat4 argom18, bool argom19, C1_Enumerat4 argom20, bool argom21, bool argom22)
{
bool res_AndLogicOP_0 = true;
    
    //  *63,* *34,*  se il parametro MainClass_C1_parametro_P10 è  uguale a GialloVerde *38,* o  se il contatore MainClass_C1_contatore_Co6 è  minore di  *55,* 121 *36,* e  se il timer MainClass_C1_timer_T2 è scaduto o  se l'argomento argomento_ave6 non  è  uguale a c180x *39,* , Solo una delle seguenti { 
    //   *110,*  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è scaduto, Verifica che   *48,*  *,*  il controllo MainClass_C1_controllo_C7 sia  diverso da  True 
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    res_OrLogicOP_3 = (res_OrLogicOP_3 || (L_P1__GetParamMainc6(my_id) == gialloverde));
    bool res_AndLogicOP_4 = true;
    res_AndLogicOP_4 = (res_AndLogicOP_4 && (Counter_GetValore(L_P1__GetMainc37(my_id)) < 121u));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && Timer_Scaduto(L_P1__GetMainc33(my_id)));
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_AndLogicOP_4);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (argom20 == c180x));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_5);
    
    if(res_OrLogicOP_2){
    bool res_ImpliesLogicOp_6 = true;
    if(Timer_Scaduto(L_P1__GetMainc30(my_id))){
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetInMainc3(my_id) == true));
    res_ImpliesLogicOp_6 = (res_ImpliesLogicOp_6 && res_NotLogicOP_7);
    }
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_ImpliesLogicOp_6);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *47,49,*  *,*  il timer MainClass_C1_timer_T4 non sia disattivo
    //   *104,* o  che  *34,*  il parametro MainClass_C1_parametro_P10 non sia  diverso da GialloVerde
    bool res_OrLogicOP_8 = false;
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! Timer_Disattivo(L_P1__GetMainc35(my_id)));
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_NotLogicOP_9);
    bool res_NotLogicOP_10 = true;
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (L_P1__GetParamMainc6(my_id) == gialloverde));
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! res_NotLogicOP_11);
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_NotLogicOP_10);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_8);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
     
    { commento: {61,}  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
     commento: {62,}  se la macro  MainClass_C1_macrova_M6 ( con argomento_a6   uguale a True ,argomento_a9   uguale a Verde ,argomento_a4   uguale a c270x ,argomento_a3   uguale a GialloVerde ,argomento_a7   uguale a RossoGialloxVerdex ,argomento_a2   uguale a c180  e argomento_a1   uguale a RossoGialloxVerdex )   è  diverso da  False  commento: {40,}  o  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
     commento: {61,} commento: {34,}  se lo stato  non è  diverso da  commento: {56,}  state1  commento: {106,} commento: {38,} o  se il contatore MainClass_C1_contatore_Co6 è  uguale a  commento: {53,} 110 commento: {35,} e  se il controllo MainClass_C1_controllo_C7 non è  uguale a  True  commento: {35,} o  se il controllo MainClass_C1_controllo_C8 non è  diverso da  True  commento: {38,} o  se il contatore MainClass_C1_contatore_Co6 non è  maggiore di  commento: {54,} 1245 commento: {36,} o  se il timer MainClass_C1_timer_T3 non è disattivo, Tutte le seguenti { 
     commento: {61,} commento: {34,}  se il parametro MainClass_C1_parametro_P10 non è  diverso da GialloVerde commento: {36,} e  se il timer MainClass_C1_timer_T4 è disattivo commento: {35,} o  se il controllo MainClass_C1_controllo_C7 non è  diverso da  True  o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
     commento: {35,}  se il controllo MainClass_C1_controllo_C7 non è  uguale a  False  commento: {38,} o  se il contatore MainClass_C1_contatore_Co6 è  diverso da  commento: {56,} 123210 commento: {37,} e  se la variabile MainClass_C1_variabile_V3 non è  minore di  commento: {55,} 4 commento: {35,} e  se il controllo MainClass_C1_controllo_C7 è  diverso da  False  e  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} o  se la variabile MainClass_C1_variabile_V7 è  uguale a c180x, Verifica che   commento: {47,48,51,}  commento: {,}  il controllo MainClass_C1_controllo_C8 sia  uguale a  False 
     commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} o  che  commento: {,}  il contatore MainClass_C1_contatore_Co1 non sia  uguale a  commento: {53,} 134
     commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P10 sia  diverso da GialloVerde
    
    
     } Verifica che   commento: {47,48,}   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P10 sia  diverso da GialloVerde
     commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C7 sia  diverso da  True 
     commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P1 sia  uguale a c180
    
    
     } Verifica che   commento: {48,49,50,}  commento: {,}  la variabile MainClass_C1_variabile_V7 non sia  diverso da c180x
     commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C7 sia  uguale a  True 
     commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T4 non sia attivo
    
    
     } Verifica che   commento: {47,48,49,51,}  commento: {,}  il timer MainClass_C1_timer_T3 non sia attivo
     commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C7 sia  diverso da  True 
     commento: {104,} e  che  commento: {35,}  il controllo MainClass_C1_controllo_C8 non sia  diverso da  False 
     commento: {104,} o  che  commento: {,}  il contatore MainClass_C1_contatore_Co7 non sia  minore di  commento: {55,} 13
     commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P10 sia  uguale a GialloVerde
    
    
     } Verifica che   commento: {49,}  commento: {,}  il timer MainClass_C1_timer_T4 non sia disattivo
    
    
    }
*/
bool L_P1__Macro4(instance_id_t const my_id )
{
bool res_AndLogicOP_0 = true;
    
    //  *61,*  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
    //   *62,*  se la macro  MainClass_C1_macrova_M6 ( con argomento_a6   uguale a True ,argomento_a9   uguale a Verde ,argomento_a4   uguale a c270x ,argomento_a3   uguale a GialloVerde ,argomento_a7   uguale a RossoGialloxVerdex ,argomento_a2   uguale a c180  e argomento_a1   uguale a RossoGialloxVerdex )   è  diverso da  False  *40,*  o  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
    //   *61,* *34,*  se lo stato  non è  diverso da  *56,*  state1  *106,* *38,* o  se il contatore MainClass_C1_contatore_Co6 è  uguale a  *53,* 110 *35,* e  se il controllo MainClass_C1_controllo_C7 non è  uguale a  True  *35,* o  se il controllo MainClass_C1_controllo_C8 non è  diverso da  True  *38,* o  se il contatore MainClass_C1_contatore_Co6 non è  maggiore di  *54,* 1245 *36,* o  se il timer MainClass_C1_timer_T3 non è disattivo, Tutte le seguenti { 
    //   *61,* *34,*  se il parametro MainClass_C1_parametro_P10 non è  diverso da GialloVerde *36,* e  se il timer MainClass_C1_timer_T4 è disattivo *35,* o  se il controllo MainClass_C1_controllo_C7 non è  diverso da  True  o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
    //   *35,*  se il controllo MainClass_C1_controllo_C7 non è  uguale a  False  *38,* o  se il contatore MainClass_C1_contatore_Co6 è  diverso da  *56,* 123210 *37,* e  se la variabile MainClass_C1_variabile_V3 non è  minore di  *55,* 4 *35,* e  se il controllo MainClass_C1_controllo_C7 è  diverso da  False  e  se il controllo ConsDef  è  uguale a FALSE  *37,* o  se la variabile MainClass_C1_variabile_V7 è  uguale a c180x, Verifica che   *47,48,51,*  *,*  il controllo MainClass_C1_controllo_C8 sia  uguale a  False 
    //   *104,* e  che   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* o  che  *,*  il contatore MainClass_C1_contatore_Co1 non sia  uguale a  *53,* 134
    //   *104,* o  che  *34,*  il parametro MainClass_C1_parametro_P10 sia  diverso da GialloVerde
    //   } Verifica che   *47,48,*   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* o  che  *34,*  il parametro MainClass_C1_parametro_P10 sia  diverso da GialloVerde
    //   *104,* e  che  *,*  il controllo MainClass_C1_controllo_C7 sia  diverso da  True 
    //   *104,* o  che   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* e  che  *34,*  il parametro MainClass_C1_parametro_P1 sia  uguale a c180
    //   } Verifica che   *48,49,50,*  *,*  la variabile MainClass_C1_variabile_V7 non sia  diverso da c180x
    //   *104,* o  che  *,*  il controllo MainClass_C1_controllo_C7 sia  uguale a  True 
    //   *104,* o  che  *,*  il timer MainClass_C1_timer_T4 non sia attivo
    //   } Verifica che   *47,48,49,51,*  *,*  il timer MainClass_C1_timer_T3 non sia attivo
    //   *104,* o  che  *,*  il controllo MainClass_C1_controllo_C7 sia  diverso da  True 
    //   *104,* e  che  *35,*  il controllo MainClass_C1_controllo_C8 non sia  diverso da  False 
    //   *104,* o  che  *,*  il contatore MainClass_C1_contatore_Co7 non sia  minore di  *55,* 13
    //   *104,* e  che  *34,*  il parametro MainClass_C1_parametro_P10 sia  uguale a GialloVerde
    //   }
    bool res_ImpliesLogicOp_1 = true;
    if((L_P1__GetInConsd(my_id) == false)){
    bool res_AndLogicOP_2 = true;
    bool res_ImpliesLogicOp_3 = true;
    bool res_OrLogicOP_4 = false;
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__Macro1(my_id,rossogiallo,c180,gialloverde,c270x,true,rossogiallo,verde) == false));
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_NotLogicOP_5);
    res_OrLogicOP_4 = (res_OrLogicOP_4 || (L_P1__GetInConsd(my_id) == false));
    
    if(res_OrLogicOP_4){
    bool res_OrLogicOP_6 = false;
    bool res_ImpliesLogicOp_7 = true;
    bool res_OrLogicOP_8 = false;
    bool res_OrLogicOP_9 = false;
    bool res_OrLogicOP_10 = false;
    bool res_OrLogicOP_11 = false;
    bool res_NotLogicOP_12 = true;
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (L_P1_C1_GetState(my_id) == C1_St_state));
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! res_NotLogicOP_13);
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_NotLogicOP_12);
    bool res_AndLogicOP_14 = true;
    res_AndLogicOP_14 = (res_AndLogicOP_14 && (Counter_GetValore(L_P1__GetMainc37(my_id)) == 110u));
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (L_P1__GetInMainc3(my_id) == true));
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_NotLogicOP_15);
    
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_AndLogicOP_14);
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_OrLogicOP_11);
    bool res_NotLogicOP_16 = true;
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! (L_P1__GetInMainc4(my_id) == true));
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! res_NotLogicOP_17);
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_NotLogicOP_16);
    
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_OrLogicOP_10);
    bool res_NotLogicOP_18 = true;
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! (Counter_GetValore(L_P1__GetMainc37(my_id)) > 1245u));
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_NotLogicOP_18);
    
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_OrLogicOP_9);
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! Timer_Disattivo(L_P1__GetMainc34(my_id)));
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_NotLogicOP_19);
    
    if(res_OrLogicOP_8){
    bool res_AndLogicOP_20 = true;
    bool res_ImpliesLogicOp_21 = true;
    bool res_OrLogicOP_22 = false;
    bool res_OrLogicOP_23 = false;
    bool res_AndLogicOP_24 = true;
    bool res_NotLogicOP_25 = true;
    bool res_NotLogicOP_26 = true;
    res_NotLogicOP_26 = (res_NotLogicOP_26 && ! (L_P1__GetParamMainc6(my_id) == gialloverde));
    res_NotLogicOP_25 = (res_NotLogicOP_25 && ! res_NotLogicOP_26);
    res_AndLogicOP_24 = (res_AndLogicOP_24 && res_NotLogicOP_25);
    res_AndLogicOP_24 = (res_AndLogicOP_24 && Timer_Disattivo(L_P1__GetMainc35(my_id)));
    
    res_OrLogicOP_23 = (res_OrLogicOP_23 || res_AndLogicOP_24);
    bool res_NotLogicOP_27 = true;
    bool res_NotLogicOP_28 = true;
    res_NotLogicOP_28 = (res_NotLogicOP_28 && ! (L_P1__GetInMainc3(my_id) == true));
    res_NotLogicOP_27 = (res_NotLogicOP_27 && ! res_NotLogicOP_28);
    res_OrLogicOP_23 = (res_OrLogicOP_23 || res_NotLogicOP_27);
    
    res_OrLogicOP_22 = (res_OrLogicOP_22 || res_OrLogicOP_23);
    res_OrLogicOP_22 = (res_OrLogicOP_22 || (L_P1__GetInConsd(my_id) == false));
    
    if(res_OrLogicOP_22){
    bool res_ImpliesLogicOp_29 = true;
    bool res_OrLogicOP_30 = false;
    bool res_OrLogicOP_31 = false;
    bool res_NotLogicOP_32 = true;
    res_NotLogicOP_32 = (res_NotLogicOP_32 && ! (L_P1__GetInMainc3(my_id) == false));
    res_OrLogicOP_31 = (res_OrLogicOP_31 || res_NotLogicOP_32);
    bool res_AndLogicOP_33 = true;
    bool res_AndLogicOP_34 = true;
    bool res_AndLogicOP_35 = true;
    bool res_NotLogicOP_36 = true;
    res_NotLogicOP_36 = (res_NotLogicOP_36 && ! (Counter_GetValore(L_P1__GetMainc37(my_id)) == 123210u));
    res_AndLogicOP_35 = (res_AndLogicOP_35 && res_NotLogicOP_36);
    bool res_NotLogicOP_37 = true;
    res_NotLogicOP_37 = (res_NotLogicOP_37 && ! (L_P1__GetMainc26(my_id) < 4u));
    res_AndLogicOP_35 = (res_AndLogicOP_35 && res_NotLogicOP_37);
    
    res_AndLogicOP_34 = (res_AndLogicOP_34 && res_AndLogicOP_35);
    bool res_NotLogicOP_38 = true;
    res_NotLogicOP_38 = (res_NotLogicOP_38 && ! (L_P1__GetInMainc3(my_id) == false));
    res_AndLogicOP_34 = (res_AndLogicOP_34 && res_NotLogicOP_38);
    
    res_AndLogicOP_33 = (res_AndLogicOP_33 && res_AndLogicOP_34);
    res_AndLogicOP_33 = (res_AndLogicOP_33 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_31 = (res_OrLogicOP_31 || res_AndLogicOP_33);
    
    res_OrLogicOP_30 = (res_OrLogicOP_30 || res_OrLogicOP_31);
    res_OrLogicOP_30 = (res_OrLogicOP_30 || (L_P1__GetMainc28(my_id) == c180x));
    
    if(res_OrLogicOP_30){
    bool res_OrLogicOP_39 = false;
    bool res_OrLogicOP_40 = false;
    bool res_AndLogicOP_41 = true;
    res_AndLogicOP_41 = (res_AndLogicOP_41 && (L_P1__GetInMainc4(my_id) == false));
    res_AndLogicOP_41 = (res_AndLogicOP_41 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_40 = (res_OrLogicOP_40 || res_AndLogicOP_41);
    bool res_NotLogicOP_42 = true;
    res_NotLogicOP_42 = (res_NotLogicOP_42 && ! (Counter_GetValore(L_P1__GetMainc36(my_id)) == 134u));
    res_OrLogicOP_40 = (res_OrLogicOP_40 || res_NotLogicOP_42);
    
    res_OrLogicOP_39 = (res_OrLogicOP_39 || res_OrLogicOP_40);
    bool res_NotLogicOP_43 = true;
    res_NotLogicOP_43 = (res_NotLogicOP_43 && ! (L_P1__GetParamMainc6(my_id) == gialloverde));
    res_OrLogicOP_39 = (res_OrLogicOP_39 || res_NotLogicOP_43);
    
    res_ImpliesLogicOp_29 = (res_ImpliesLogicOp_29 && res_OrLogicOP_39);
    }
    res_ImpliesLogicOp_21 = (res_ImpliesLogicOp_21 && res_ImpliesLogicOp_29);
    }
    res_AndLogicOP_20 = (res_AndLogicOP_20 && res_ImpliesLogicOp_21);
    bool res_OrLogicOP_44 = false;
    bool res_OrLogicOP_45 = false;
    res_OrLogicOP_45 = (res_OrLogicOP_45 || (L_P1__GetInConsd(my_id) == false));
    bool res_AndLogicOP_46 = true;
    bool res_NotLogicOP_47 = true;
    res_NotLogicOP_47 = (res_NotLogicOP_47 && ! (L_P1__GetParamMainc6(my_id) == gialloverde));
    res_AndLogicOP_46 = (res_AndLogicOP_46 && res_NotLogicOP_47);
    bool res_NotLogicOP_48 = true;
    res_NotLogicOP_48 = (res_NotLogicOP_48 && ! (L_P1__GetInMainc3(my_id) == true));
    res_AndLogicOP_46 = (res_AndLogicOP_46 && res_NotLogicOP_48);
    
    res_OrLogicOP_45 = (res_OrLogicOP_45 || res_AndLogicOP_46);
    
    res_OrLogicOP_44 = (res_OrLogicOP_44 || res_OrLogicOP_45);
    bool res_AndLogicOP_49 = true;
    res_AndLogicOP_49 = (res_AndLogicOP_49 && (L_P1__GetInConsd(my_id) == false));
    res_AndLogicOP_49 = (res_AndLogicOP_49 && (L_P1__GetParamMainc5(my_id) == c180));
    
    res_OrLogicOP_44 = (res_OrLogicOP_44 || res_AndLogicOP_49);
    
    res_AndLogicOP_20 = (res_AndLogicOP_20 && res_OrLogicOP_44);
    
    res_ImpliesLogicOp_7 = (res_ImpliesLogicOp_7 && res_AndLogicOP_20);
    }
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_ImpliesLogicOp_7);
    bool res_OrLogicOP_50 = false;
    bool res_OrLogicOP_51 = false;
    bool res_NotLogicOP_52 = true;
    bool res_NotLogicOP_53 = true;
    res_NotLogicOP_53 = (res_NotLogicOP_53 && ! (L_P1__GetMainc28(my_id) == c180x));
    res_NotLogicOP_52 = (res_NotLogicOP_52 && ! res_NotLogicOP_53);
    res_OrLogicOP_51 = (res_OrLogicOP_51 || res_NotLogicOP_52);
    res_OrLogicOP_51 = (res_OrLogicOP_51 || (L_P1__GetInMainc3(my_id) == true));
    
    res_OrLogicOP_50 = (res_OrLogicOP_50 || res_OrLogicOP_51);
    bool res_NotLogicOP_54 = true;
    res_NotLogicOP_54 = (res_NotLogicOP_54 && ! Timer_Attivo(L_P1__GetMainc35(my_id)));
    res_OrLogicOP_50 = (res_OrLogicOP_50 || res_NotLogicOP_54);
    
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_OrLogicOP_50);
    
    res_ImpliesLogicOp_3 = (res_ImpliesLogicOp_3 && res_OrLogicOP_6);
    }
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_ImpliesLogicOp_3);
    bool res_OrLogicOP_55 = false;
    bool res_OrLogicOP_56 = false;
    bool res_NotLogicOP_57 = true;
    res_NotLogicOP_57 = (res_NotLogicOP_57 && ! Timer_Attivo(L_P1__GetMainc34(my_id)));
    res_OrLogicOP_56 = (res_OrLogicOP_56 || res_NotLogicOP_57);
    bool res_AndLogicOP_58 = true;
    bool res_NotLogicOP_59 = true;
    res_NotLogicOP_59 = (res_NotLogicOP_59 && ! (L_P1__GetInMainc3(my_id) == true));
    res_AndLogicOP_58 = (res_AndLogicOP_58 && res_NotLogicOP_59);
    bool res_NotLogicOP_60 = true;
    bool res_NotLogicOP_61 = true;
    res_NotLogicOP_61 = (res_NotLogicOP_61 && ! (L_P1__GetInMainc4(my_id) == false));
    res_NotLogicOP_60 = (res_NotLogicOP_60 && ! res_NotLogicOP_61);
    res_AndLogicOP_58 = (res_AndLogicOP_58 && res_NotLogicOP_60);
    
    res_OrLogicOP_56 = (res_OrLogicOP_56 || res_AndLogicOP_58);
    
    res_OrLogicOP_55 = (res_OrLogicOP_55 || res_OrLogicOP_56);
    bool res_AndLogicOP_62 = true;
    bool res_NotLogicOP_63 = true;
    res_NotLogicOP_63 = (res_NotLogicOP_63 && ! (Counter_GetValore(L_P1__GetMainc38(my_id)) < 13u));
    res_AndLogicOP_62 = (res_AndLogicOP_62 && res_NotLogicOP_63);
    res_AndLogicOP_62 = (res_AndLogicOP_62 && (L_P1__GetParamMainc6(my_id) == gialloverde));
    
    res_OrLogicOP_55 = (res_OrLogicOP_55 || res_AndLogicOP_62);
    
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_OrLogicOP_55);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_AndLogicOP_2);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *49,*  *,*  il timer MainClass_C1_timer_T4 non sia disattivo
    bool res_NotLogicOP_64 = true;
    res_NotLogicOP_64 = (res_NotLogicOP_64 && ! Timer_Disattivo(L_P1__GetMainc35(my_id)));
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_NotLogicOP_64);
    
    
    
    return res_AndLogicOP_0;
}


// Macro valorizzate

/*
    CNL corrispondente:
    
    { commento: {[} commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI2 non è attivo o  se il controllo ConsDef è uguale a FALSE  commento: {109,} e  se il ripristino della variabile  MainClass_C1_restoreva_RV2 è  uguale a  True  o  se il ripristino dello stato  è  diverso da  commento: {56,}  state1  commento: {107,} commento: {109,} o  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  maggiore di  commento: {54,} 6 , assegna alla macro il valore  True 
    
     commento: {46,} assegna alla macro il valore  True  commento: {],}
    }
*/
bool L_P1__Macro1(instance_id_t const my_id , C1_Enumerat2 argom2, C1_Enumerat2 argom3, C1_Enumerat3 argom4, C1_Enumerat1 argom5, bool argom6, C1_Enumerat2 argom7, C1_Enumerat3 argom8)
{
bool res_macro_val;
    
    //  *[* *110,*  se il ripristino del timer  MainClass_C1_restoreTI_TI2 non è attivo o  se il controllo ConsDef è uguale a FALSE  *109,* e  se il ripristino della variabile  MainClass_C1_restoreva_RV2 è  uguale a  True  o  se il ripristino dello stato  è  diverso da  *56,*  state1  *107,* *109,* o  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  maggiore di  *54,* 6
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_OrLogicOP_2 = false;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! Timer_Attivo(L_P1__GetMainc32(my_id)));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_3);
    bool res_AndLogicOP_4 = true;
    res_AndLogicOP_4 = (res_AndLogicOP_4 && (L_P1__GetInConsd(my_id) == false));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && (L_P1__GetMainc21(my_id) == true));
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_4);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_OrLogicOP_2);
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetStato1(my_id) == C1_St_state));
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_NotLogicOP_5);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetMainc19(my_id) > 6u));
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_6);
    
    if(res_OrLogicOP_0){
    
    res_macro_val = true;
    }
    else{
    res_macro_val = true;
    }
    return res_macro_val;
}



