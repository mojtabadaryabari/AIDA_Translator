// Codice del modello 'TestCase8', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#include "Logica/ClasseMainClass_C1.h"
#include "Logica/ClasseMainClass_C1_priv.h"
#include "config.h"
#include "scheduler.h"


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
    Nessuna
    }
*/
static inline void L_P1__Effec1(instance_id_t const my_id)
{
    
}



// ********** Definizione metodi **********

// Metodi standard

void L_P1_C1_Init(instance_id_t const my_id)
{
    // init variabili di stato
    L_P1__SetMainc9(my_id, false);
    L_P1__SetMainc11(my_id, rossogiallo1);
    L_P1__SetMainc13(my_id, 0);
    L_P1__SetMainc15(my_id, c120x);
    L_P1__SetMainc17(my_id, 0);
    L_P1__SetMainc19(my_id, false);
    L_P1__SetMainc20(my_id, false);
    L_P1__SetMainc21(my_id, 0);
    L_P1__SetMainc22(my_id, 0);
    L_P1__SetMainc23(my_id, rossogiallo1);
    L_P1__SetMainc24(my_id, rossogiallo1);
    L_P1__SetMainc25(my_id, 0);
    L_P1__SetMainc26(my_id, false);
    L_P1__SetMainc27(my_id, false);
    L_P1__SetMainc28(my_id, 0);
    L_P1__SetStato1(my_id, C1_St_Stato);
    // init controlli precedenti
    L_P1__SetMainc6(my_id, false);
    L_P1__SetMainc8(my_id, ac);
    // init Timer e Counter
    Timer_AggmInit(L_P1__GetMainc29(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc29_ID);
    Timer_Init(L_P1__GetMainc29(my_id), 42000);
    Timer_AggmInit(L_P1__GetMainc30(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc30_ID);
    Timer_Init(L_P1__GetMainc30(my_id), 42000);
    Timer_AggmInit(L_P1__GetMainc31(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc31_ID);
    Timer_Init(L_P1__GetMainc31(my_id), 51000);
    Timer_AggmInit(L_P1__GetMainc32(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc32_ID);
    Timer_Init(L_P1__GetMainc32(my_id), 51000);
    Timer_AggmInit(L_P1__GetMainc33(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc33_ID);
    Timer_Init(L_P1__GetMainc33(my_id), 3453000);
    Timer_AggmInit(L_P1__GetMainc34(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc34_ID);
    Timer_Init(L_P1__GetMainc34(my_id), 3453000);
    Timer_AggmInit(L_P1__GetMainc35(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc35_ID);
    Timer_Init(L_P1__GetMainc35(my_id), 230000);
    Counter_AggmInit(L_P1__GetMainc36(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc36_ID);
    Counter_Init(L_P1__GetMainc36(my_id));
    Counter_AggmInit(L_P1__GetMainc37(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc37_ID);
    Counter_Init(L_P1__GetMainc37(my_id));
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
    L_P1__SetMainc10(my_id, L_P1__GetMainc9(my_id));
    L_P1__SetMainc12(my_id, L_P1__GetMainc11(my_id));
    L_P1__SetMainc14(my_id, L_P1__GetMainc13(my_id));
    L_P1__SetMainc16(my_id, L_P1__GetMainc15(my_id));
    L_P1__SetMainc18(my_id, L_P1__GetMainc17(my_id));
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
    L_P1__SetOutMainc(my_id, ac);
}

void L_P1_C1_GUpdatePrev(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C1(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C1(proc_id);
    L_P1__SetMainc6(my_id, L_P1__GetInMainc5(my_id));
    L_P1__SetMainc8(my_id, L_P1__GetInMainc7(my_id));
    L_P1__SetMainc10(my_id, L_P1__GetMainc9(my_id));
    L_P1__SetMainc12(my_id, L_P1__GetMainc11(my_id));
    L_P1__SetMainc14(my_id, L_P1__GetMainc13(my_id));
    L_P1__SetMainc16(my_id, L_P1__GetMainc15(my_id));
    L_P1__SetMainc18(my_id, L_P1__GetMainc17(my_id));
}

// ********** Definizione macro **********

// Macro di effetto

/*
    CNL corrispondente:
     
    { commento: {38,}  se il contatore MainClass_C1_contatore_Co5 è  uguale a  commento: {53,} 13 commento: {38,} o  se il contatore MainClass_C1_contatore_Co8 non è  uguale a  commento: {53,} 13 e  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} e  se il timer MainClass_C1_timer_T5 non è scaduto o  se il controllo ConsDef  è  uguale a FALSE , commento: {66,} Assegna al comando MainClass_C1_comando_C8 il valore AC
    
     ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V9 il valore 2
    
    
     commento: {38,}  se il contatore MainClass_C1_contatore_Co8 non è  diverso da  commento: {56,} 13214, commento: {68,}Attiva il timer MainClass_C1_timer_T5
    
       
     commento: {37,}  se la variabile MainClass_C1_variabile_V1 è  maggiore di  commento: {54,} 9 commento: {34,} e  se il parametro MainClass_C1_parametro_P4 è  minore di  commento: {55,} 2 commento: {36,} o  se il timer MainClass_C1_timer_T5 è disattivo commento: {34,} o  se il parametro MainClass_C1_parametro_P6 è  uguale a c270xx commento: {37,} o  se la variabile MainClass_C1_variabile_V9 non è  uguale a  commento: {53,} 3, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V4 il valore  True 
    
       
     commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  diverso da  False  commento: {35,} o  se il controllo MainClass_C1_controllo_C7 è  uguale a c270xx, commento: {66,} Assegna al comando MainClass_C1_comando_C8 il valore AC
    
     ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V1 il valore 3
    
    
      se la macro  MainClass_C1_macrova_M7 ( con argomento_a10   uguale a True ,argomento_a1   uguale a avanzamento ,argomento_a3   uguale a AC ,argomento_a7   uguale a c270  e argomento_a9   uguale a c270 )  non  è  diverso da RossoGialloaVerdea commento: {40,}  commento: {34,} o  se il parametro MainClass_C1_parametro_P8 è  maggiore di  commento: {54,} 10 e  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} o  se il controllo MainClass_C1_controllo_C7 è  uguale a c270xx, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V4 il valore  True 
    
     ,altrimenti  commento: {70,}Incrementa il contatore MainClass_C1_contatore_Co8
    
    
    
    }
*/
void L_P1__Macro(instance_id_t const my_id )
{
//  *38,*  se il contatore MainClass_C1_contatore_Co5 è  uguale a  *53,* 13 *38,* o  se il contatore MainClass_C1_contatore_Co8 non è  uguale a  *53,* 13 e  se il controllo ConsDef  è  uguale a FALSE  *36,* e  se il timer MainClass_C1_timer_T5 non è scaduto o  se il controllo ConsDef  è  uguale a FALSE , *66,* Assegna al comando MainClass_C1_comando_C8 il valore AC
    // ,altrimenti  *67,* Assegna alla variabile MainClass_C1_variabile_V9 il valore 2
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    res_OrLogicOP_1 = (res_OrLogicOP_1 || (Counter_GetValore(L_P1__GetMainc36(my_id)) == 13u));
    bool res_AndLogicOP_2 = true;
    bool res_AndLogicOP_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (Counter_GetValore(L_P1__GetMainc37(my_id)) == 13u));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_4);
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (L_P1__GetInConsd(my_id) == false));
    
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_AndLogicOP_3);
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! Timer_Scaduto(L_P1__GetMainc35(my_id)));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_5);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_2);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    res_OrLogicOP_0 = (res_OrLogicOP_0 || (L_P1__GetInConsd(my_id) == false));
    
    if(res_OrLogicOP_0){
    
    L_P1__SetOutMainc(my_id,ac);
    }else{
    
    L_P1__SetMainc28(my_id,2u);
    }
    //  *38,*  se il contatore MainClass_C1_contatore_Co8 non è  diverso da  *56,* 13214, *68,*Attiva il timer MainClass_C1_timer_T5
    bool res_NotLogicOP_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (Counter_GetValore(L_P1__GetMainc37(my_id)) == 13214u));
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! res_NotLogicOP_7);
    if(res_NotLogicOP_6){
    
    Timer_Attiva(L_P1__GetMainc35(my_id));
    }
    //  *37,*  se la variabile MainClass_C1_variabile_V1 è  maggiore di  *54,* 9 *34,* e  se il parametro MainClass_C1_parametro_P4 è  minore di  *55,* 2 *36,* o  se il timer MainClass_C1_timer_T5 è disattivo *34,* o  se il parametro MainClass_C1_parametro_P6 è  uguale a c270xx *37,* o  se la variabile MainClass_C1_variabile_V9 non è  uguale a  *53,* 3, *67,* Assegna alla variabile MainClass_C1_variabile_V4 il valore  True
    bool res_OrLogicOP_8 = false;
    bool res_OrLogicOP_9 = false;
    bool res_OrLogicOP_10 = false;
    bool res_AndLogicOP_11 = true;
    res_AndLogicOP_11 = (res_AndLogicOP_11 && (L_P1__GetMainc25(my_id) > 9u));
    res_AndLogicOP_11 = (res_AndLogicOP_11 && (L_P1__GetParamMainc2(my_id) < 2u));
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_AndLogicOP_11);
    res_OrLogicOP_10 = (res_OrLogicOP_10 || Timer_Disattivo(L_P1__GetMainc35(my_id)));
    
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_OrLogicOP_10);
    res_OrLogicOP_9 = (res_OrLogicOP_9 || (L_P1__GetParamMainc3(my_id) == c270xx));
    
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_OrLogicOP_9);
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (L_P1__GetMainc28(my_id) == 3u));
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_NotLogicOP_12);
    
    if(res_OrLogicOP_8){
    
    L_P1__SetMainc27(my_id,true);
    }
    //  *109,*  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  diverso da  False  *35,* o  se il controllo MainClass_C1_controllo_C7 è  uguale a c270xx, *66,* Assegna al comando MainClass_C1_comando_C8 il valore AC
    // ,altrimenti  *67,* Assegna alla variabile MainClass_C1_variabile_V1 il valore 3
    bool res_OrLogicOP_13 = false;
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1__GetMainc20(my_id) == false));
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_NotLogicOP_14);
    res_OrLogicOP_13 = (res_OrLogicOP_13 || (L_P1__GetInMainc1(my_id) == c270xx));
    
    if(res_OrLogicOP_13){
    
    L_P1__SetOutMainc(my_id,ac);
    }else{
    
    L_P1__SetMainc25(my_id,3u);
    }
    //  se la macro  MainClass_C1_macrova_M7 ( con argomento_a10   uguale a True ,argomento_a1   uguale a avanzamento ,argomento_a3   uguale a AC ,argomento_a7   uguale a c270  e argomento_a9   uguale a c270 )  non  è  diverso da RossoGialloaVerdea *40,*  *34,* o  se il parametro MainClass_C1_parametro_P8 è  maggiore di  *54,* 10 e  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  *35,* o  se il controllo MainClass_C1_controllo_C7 è  uguale a c270xx, *67,* Assegna alla variabile MainClass_C1_variabile_V4 il valore  True 
    // ,altrimenti  *70,*Incrementa il contatore MainClass_C1_contatore_Co8
    bool res_OrLogicOP_15 = false;
    bool res_OrLogicOP_16 = false;
    bool res_OrLogicOP_17 = false;
    bool res_NotLogicOP_18 = true;
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (L_P1__Macro2(my_id,avanzamento,true,ac,c270,c270) == rossogiallo));
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! res_NotLogicOP_19);
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_NotLogicOP_18);
    bool res_AndLogicOP_20 = true;
    res_AndLogicOP_20 = (res_AndLogicOP_20 && (L_P1__GetParamMainc4(my_id) > 10u));
    res_AndLogicOP_20 = (res_AndLogicOP_20 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_AndLogicOP_20);
    
    res_OrLogicOP_16 = (res_OrLogicOP_16 || res_OrLogicOP_17);
    res_OrLogicOP_16 = (res_OrLogicOP_16 || (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_OrLogicOP_16);
    res_OrLogicOP_15 = (res_OrLogicOP_15 || (L_P1__GetInMainc1(my_id) == c270xx));
    
    if(res_OrLogicOP_15){
    
    L_P1__SetMainc27(my_id,true);
    }else{
    
    Counter_Incr(L_P1__GetMainc37(my_id));
    }
}

/*
    CNL corrispondente:
    
    { commento: {35,}  se il controllo MainClass_C1_controllo_C7 non è  uguale a c270xx commento: {34,} e  se il parametro MainClass_C1_parametro_P8 non è  diverso da  commento: {56,} 10 commento: {37,} e  se la variabile MainClass_C1_variabile_V4 è  diverso da  True , commento: {70,}Incrementa il contatore MainClass_C1_contatore_Co5
    
     ,altrimenti  commento: {70,}Incrementa il contatore MainClass_C1_contatore_Co5
    
    
      se il controllo ConsDef è uguale a FALSE  commento: {38,} e  se il contatore MainClass_C1_contatore_Co5 è  minore di  commento: {55,} 12 commento: {34,} o  se il parametro MainClass_C1_parametro_P4 è  maggiore di  commento: {54,} 1 o  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} o  se il contatore MainClass_C1_contatore_Co8 è  diverso da  commento: {56,} 121453 commento: {36,} e  se il timer MainClass_C1_timer_T5 è disattivo, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V9 il valore 10
    
     ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V4 il valore  True 
    
    
      se il controllo ConsDef è uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro MainClass_C1_parametro_P6 è  uguale a c270xx commento: {36,} o  se il timer MainClass_C1_timer_T5 è attivo o  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} o  se il contatore MainClass_C1_contatore_Co8 non è  maggiore di  commento: {54,} 150, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V4 il valore  True 
    
     ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V4 il valore  False 
    
    
    
    }
*/
void L_P1__Macro1(instance_id_t const my_id )
{
//  *35,*  se il controllo MainClass_C1_controllo_C7 non è  uguale a c270xx *34,* e  se il parametro MainClass_C1_parametro_P8 non è  diverso da  *56,* 10 *37,* e  se la variabile MainClass_C1_variabile_V4 è  diverso da  True , *70,*Incrementa il contatore MainClass_C1_contatore_Co5
    // ,altrimenti  *70,*Incrementa il contatore MainClass_C1_contatore_Co5
    bool res_AndLogicOP_0 = true;
    bool res_AndLogicOP_1 = true;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (L_P1__GetInMainc1(my_id) == c270xx));
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_2);
    bool res_NotLogicOP_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetParamMainc4(my_id) == 10u));
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! res_NotLogicOP_4);
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_3);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_AndLogicOP_1);
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetMainc27(my_id) == true));
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_NotLogicOP_5);
    
    if(res_AndLogicOP_0){
    
    Counter_Incr(L_P1__GetMainc36(my_id));
    }else{
    
    Counter_Incr(L_P1__GetMainc36(my_id));
    }
    //  se il controllo ConsDef è uguale a FALSE  *38,* e  se il contatore MainClass_C1_contatore_Co5 è  minore di  *55,* 12 *34,* o  se il parametro MainClass_C1_parametro_P4 è  maggiore di  *54,* 1 o  se il controllo ConsDef  è  uguale a FALSE  *38,* o  se il contatore MainClass_C1_contatore_Co8 è  diverso da  *56,* 121453 *36,* e  se il timer MainClass_C1_timer_T5 è disattivo, *67,* Assegna alla variabile MainClass_C1_variabile_V9 il valore 10
    // ,altrimenti  *67,* Assegna alla variabile MainClass_C1_variabile_V4 il valore  True
    bool res_OrLogicOP_6 = false;
    bool res_OrLogicOP_7 = false;
    bool res_OrLogicOP_8 = false;
    bool res_AndLogicOP_9 = true;
    res_AndLogicOP_9 = (res_AndLogicOP_9 && (L_P1__GetInConsd(my_id) == false));
    res_AndLogicOP_9 = (res_AndLogicOP_9 && (Counter_GetValore(L_P1__GetMainc36(my_id)) < 12u));
    
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_AndLogicOP_9);
    res_OrLogicOP_8 = (res_OrLogicOP_8 || (L_P1__GetParamMainc2(my_id) > 1u));
    
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_OrLogicOP_8);
    res_OrLogicOP_7 = (res_OrLogicOP_7 || (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_OrLogicOP_7);
    bool res_AndLogicOP_10 = true;
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (Counter_GetValore(L_P1__GetMainc37(my_id)) == 121453u));
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_NotLogicOP_11);
    res_AndLogicOP_10 = (res_AndLogicOP_10 && Timer_Disattivo(L_P1__GetMainc35(my_id)));
    
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_AndLogicOP_10);
    
    if(res_OrLogicOP_6){
    
    L_P1__SetMainc28(my_id,10u);
    }else{
    
    L_P1__SetMainc27(my_id,true);
    }
    //  se il controllo ConsDef è uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  *34,* e  se il parametro MainClass_C1_parametro_P6 è  uguale a c270xx *36,* o  se il timer MainClass_C1_timer_T5 è attivo o  se il controllo ConsDef  è  uguale a FALSE  *38,* o  se il contatore MainClass_C1_contatore_Co8 non è  maggiore di  *54,* 150, *67,* Assegna alla variabile MainClass_C1_variabile_V4 il valore  True 
    // ,altrimenti  *67,* Assegna alla variabile MainClass_C1_variabile_V4 il valore  False
    bool res_OrLogicOP_12 = false;
    bool res_OrLogicOP_13 = false;
    bool res_OrLogicOP_14 = false;
    bool res_OrLogicOP_15 = false;
    res_OrLogicOP_15 = (res_OrLogicOP_15 || (L_P1__GetInConsd(my_id) == false));
    bool res_AndLogicOP_16 = true;
    res_AndLogicOP_16 = (res_AndLogicOP_16 && (L_P1__GetInConsd(my_id) == false));
    res_AndLogicOP_16 = (res_AndLogicOP_16 && (L_P1__GetParamMainc3(my_id) == c270xx));
    
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_AndLogicOP_16);
    
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_OrLogicOP_15);
    res_OrLogicOP_14 = (res_OrLogicOP_14 || Timer_Attivo(L_P1__GetMainc35(my_id)));
    
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_OrLogicOP_14);
    res_OrLogicOP_13 = (res_OrLogicOP_13 || (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_OrLogicOP_13);
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! (Counter_GetValore(L_P1__GetMainc37(my_id)) > 150u));
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_NotLogicOP_17);
    
    if(res_OrLogicOP_12){
    
    L_P1__SetMainc27(my_id,true);
    }else{
    
    L_P1__SetMainc27(my_id,false);
    }
}


// Macro di verifica

/*
    CNL corrispondente:
     
    { commento: {61,}  se il ripristino dello stato  non è  diverso da  commento: {56,}  state1  commento: {107,} commento: {37,} e  se la variabile MainClass_C1_variabile_V4 è  uguale a  False , Tutte le seguenti { 
     commento: {61,} commento: {38,}  se il contatore MainClass_C1_contatore_Co8 non è  uguale a  commento: {53,} 1302 commento: {35,} e  se il controllo MainClass_C1_controllo_C7 non è  diverso da c270xx commento: {34,} e  se il parametro MainClass_C1_parametro_P8 è  maggiore di  commento: {54,} 8 o  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} e  se il timer MainClass_C1_timer_T5 non è disattivo, Tutte le seguenti { 
     commento: {63,} commento: {34,}  se il parametro MainClass_C1_parametro_P4 non è  maggiore di  commento: {54,} 5 commento: {38,} o  se il contatore MainClass_C1_contatore_Co8 è  uguale a  commento: {53,} 131, Solo una delle seguenti { 
     commento: {63,} commento: {38,}  se il contatore MainClass_C1_contatore_Co5 non è  diverso da  commento: {56,} 13453, Solo una delle seguenti { 
     commento: {34,}  se lo stato  non è  uguale a  commento: {53,}  state1  commento: {106,}, Verifica che   commento: {48,49,50,}   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T5 non sia scaduto
     commento: {104,} e  che  commento: {36,}  il timer MainClass_C1_timer_T5 sia attivo
     commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V4 non sia  uguale a  True 
     commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
    
    
     } Verifica che   commento: {48,49,}  commento: {,}  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
     commento: {104,} e  che  commento: {35,}  il controllo MainClass_C1_controllo_C7 sia  uguale a c270xx
     commento: {104,} e  che  commento: {35,}  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
     commento: {104,} e  che  commento: {35,}  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
     commento: {104,} o  che  commento: {35,}  il controllo MainClass_C1_controllo_C7 non sia  diverso da c270xx
     commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T5 sia scaduto
    
    
     } Verifica che   commento: {48,49,50,}  commento: {,}  il timer MainClass_C1_timer_T5 non sia scaduto
     commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V9 non sia  uguale a  commento: {53,} 7
     commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
    
    
     } Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
    
    
     } Verifica che   commento: {47,48,50,51,}  commento: {,}  la variabile MainClass_C1_variabile_V4 sia  diverso da  True 
     commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P8 sia  minore di  commento: {55,} 2
     commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} o  che  commento: {,}  il contatore MainClass_C1_contatore_Co5 non sia  minore di  commento: {55,} 11
     commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P4 sia  diverso da  commento: {56,} 6
     commento: {104,} e  che  commento: {37,}  la variabile MainClass_C1_variabile_V4 non sia  uguale a  True 
    
    
    }
*/
bool L_P1__Macro4(instance_id_t const my_id )
{
bool res_AndLogicOP_0 = true;
    
    //  *61,*  se il ripristino dello stato  non è  diverso da  *56,*  state1  *107,* *37,* e  se la variabile MainClass_C1_variabile_V4 è  uguale a  False , Tutte le seguenti { 
    //   *61,* *38,*  se il contatore MainClass_C1_contatore_Co8 non è  uguale a  *53,* 1302 *35,* e  se il controllo MainClass_C1_controllo_C7 non è  diverso da c270xx *34,* e  se il parametro MainClass_C1_parametro_P8 è  maggiore di  *54,* 8 o  se il controllo ConsDef  è  uguale a FALSE  *36,* e  se il timer MainClass_C1_timer_T5 non è disattivo, Tutte le seguenti { 
    //   *63,* *34,*  se il parametro MainClass_C1_parametro_P4 non è  maggiore di  *54,* 5 *38,* o  se il contatore MainClass_C1_contatore_Co8 è  uguale a  *53,* 131, Solo una delle seguenti { 
    //   *63,* *38,*  se il contatore MainClass_C1_contatore_Co5 non è  diverso da  *56,* 13453, Solo una delle seguenti { 
    //   *34,*  se lo stato  non è  uguale a  *53,*  state1  *106,*, Verifica che   *48,49,50,*   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* e  che  *,*  il timer MainClass_C1_timer_T5 non sia scaduto
    //   *104,* e  che  *36,*  il timer MainClass_C1_timer_T5 sia attivo
    //   *104,* o  che  *,*  la variabile MainClass_C1_variabile_V4 non sia  uguale a  True 
    //   *104,* o  che  *,*  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
    //   } Verifica che   *48,49,*  *,*  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
    //   *104,* e  che  *35,*  il controllo MainClass_C1_controllo_C7 sia  uguale a c270xx
    //   *104,* e  che  *35,*  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
    //   *104,* e  che  *35,*  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
    //   *104,* o  che  *35,*  il controllo MainClass_C1_controllo_C7 non sia  diverso da c270xx
    //   *104,* o  che  *,*  il timer MainClass_C1_timer_T5 sia scaduto
    //   } Verifica che   *48,49,50,*  *,*  il timer MainClass_C1_timer_T5 non sia scaduto
    //   *104,* e  che  *,*  la variabile MainClass_C1_variabile_V9 non sia  uguale a  *53,* 7
    //   *104,* o  che  *,*  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
    //   } Verifica che   *48,*   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* e  che   il controllo ConsDef  sia  uguale a FALSE 
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_AndLogicOP_2 = true;
    bool res_NotLogicOP_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetStato1(my_id) == C1_St_state));
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! res_NotLogicOP_4);
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_3);
    res_AndLogicOP_2 = (res_AndLogicOP_2 && (L_P1__GetMainc27(my_id) == false));
    
    if(res_AndLogicOP_2){
    bool res_AndLogicOP_5 = true;
    bool res_ImpliesLogicOp_6 = true;
    bool res_OrLogicOP_7 = false;
    bool res_AndLogicOP_8 = true;
    bool res_AndLogicOP_9 = true;
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (Counter_GetValore(L_P1__GetMainc37(my_id)) == 1302u));
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_NotLogicOP_10);
    bool res_NotLogicOP_11 = true;
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (L_P1__GetInMainc1(my_id) == c270xx));
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! res_NotLogicOP_12);
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_NotLogicOP_11);
    
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_AndLogicOP_9);
    res_AndLogicOP_8 = (res_AndLogicOP_8 && (L_P1__GetParamMainc4(my_id) > 8u));
    
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_AndLogicOP_8);
    bool res_AndLogicOP_13 = true;
    res_AndLogicOP_13 = (res_AndLogicOP_13 && (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! Timer_Disattivo(L_P1__GetMainc35(my_id)));
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_NotLogicOP_14);
    
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_AndLogicOP_13);
    
    if(res_OrLogicOP_7){
    bool res_AndLogicOP_15 = true;
    bool res_ImpliesLogicOp_16 = true;
    bool res_OrLogicOP_17 = false;
    bool res_NotLogicOP_18 = true;
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! (L_P1__GetParamMainc2(my_id) > 5u));
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_NotLogicOP_18);
    res_OrLogicOP_17 = (res_OrLogicOP_17 || (Counter_GetValore(L_P1__GetMainc37(my_id)) == 131u));
    
    if(res_OrLogicOP_17){
    bool res_XorLogicOP_19 = true;
    int xorIndex_res_XorLogicOP_19 = 0;
    bool res_ImpliesLogicOp_20 = true;
    bool res_NotLogicOP_21 = true;
    bool res_NotLogicOP_22 = true;
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! (Counter_GetValore(L_P1__GetMainc36(my_id)) == 13453u));
    res_NotLogicOP_21 = (res_NotLogicOP_21 && ! res_NotLogicOP_22);
    if(res_NotLogicOP_21){
    bool res_ImpliesLogicOp_23 = true;
    bool res_NotLogicOP_24 = true;
    res_NotLogicOP_24 = (res_NotLogicOP_24 && ! (L_P1_C1_GetState(my_id) == C1_St_state));
    if(res_NotLogicOP_24){
    bool res_OrLogicOP_25 = false;
    bool res_OrLogicOP_26 = false;
    bool res_AndLogicOP_27 = true;
    bool res_AndLogicOP_28 = true;
    res_AndLogicOP_28 = (res_AndLogicOP_28 && (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_29 = true;
    res_NotLogicOP_29 = (res_NotLogicOP_29 && ! Timer_Scaduto(L_P1__GetMainc35(my_id)));
    res_AndLogicOP_28 = (res_AndLogicOP_28 && res_NotLogicOP_29);
    
    res_AndLogicOP_27 = (res_AndLogicOP_27 && res_AndLogicOP_28);
    res_AndLogicOP_27 = (res_AndLogicOP_27 && Timer_Attivo(L_P1__GetMainc35(my_id)));
    
    res_OrLogicOP_26 = (res_OrLogicOP_26 || res_AndLogicOP_27);
    bool res_NotLogicOP_30 = true;
    res_NotLogicOP_30 = (res_NotLogicOP_30 && ! (L_P1__GetMainc27(my_id) == true));
    res_OrLogicOP_26 = (res_OrLogicOP_26 || res_NotLogicOP_30);
    
    res_OrLogicOP_25 = (res_OrLogicOP_25 || res_OrLogicOP_26);
    bool res_NotLogicOP_31 = true;
    res_NotLogicOP_31 = (res_NotLogicOP_31 && ! (L_P1__GetInMainc1(my_id) == c270xx));
    res_OrLogicOP_25 = (res_OrLogicOP_25 || res_NotLogicOP_31);
    
    res_ImpliesLogicOp_23 = (res_ImpliesLogicOp_23 && res_OrLogicOP_25);
    }
    res_ImpliesLogicOp_20 = (res_ImpliesLogicOp_20 && res_ImpliesLogicOp_23);
    }
    if(res_ImpliesLogicOp_20){
    xorIndex_res_XorLogicOP_19 = (xorIndex_res_XorLogicOP_19 + 1);
    }
    bool res_OrLogicOP_32 = false;
    bool res_OrLogicOP_33 = false;
    bool res_AndLogicOP_34 = true;
    bool res_AndLogicOP_35 = true;
    bool res_AndLogicOP_36 = true;
    bool res_NotLogicOP_37 = true;
    res_NotLogicOP_37 = (res_NotLogicOP_37 && ! (L_P1__GetInMainc1(my_id) == c270xx));
    res_AndLogicOP_36 = (res_AndLogicOP_36 && res_NotLogicOP_37);
    res_AndLogicOP_36 = (res_AndLogicOP_36 && (L_P1__GetInMainc1(my_id) == c270xx));
    
    res_AndLogicOP_35 = (res_AndLogicOP_35 && res_AndLogicOP_36);
    bool res_NotLogicOP_38 = true;
    res_NotLogicOP_38 = (res_NotLogicOP_38 && ! (L_P1__GetInMainc1(my_id) == c270xx));
    res_AndLogicOP_35 = (res_AndLogicOP_35 && res_NotLogicOP_38);
    
    res_AndLogicOP_34 = (res_AndLogicOP_34 && res_AndLogicOP_35);
    bool res_NotLogicOP_39 = true;
    res_NotLogicOP_39 = (res_NotLogicOP_39 && ! (L_P1__GetInMainc1(my_id) == c270xx));
    res_AndLogicOP_34 = (res_AndLogicOP_34 && res_NotLogicOP_39);
    
    res_OrLogicOP_33 = (res_OrLogicOP_33 || res_AndLogicOP_34);
    bool res_NotLogicOP_40 = true;
    bool res_NotLogicOP_41 = true;
    res_NotLogicOP_41 = (res_NotLogicOP_41 && ! (L_P1__GetInMainc1(my_id) == c270xx));
    res_NotLogicOP_40 = (res_NotLogicOP_40 && ! res_NotLogicOP_41);
    res_OrLogicOP_33 = (res_OrLogicOP_33 || res_NotLogicOP_40);
    
    res_OrLogicOP_32 = (res_OrLogicOP_32 || res_OrLogicOP_33);
    res_OrLogicOP_32 = (res_OrLogicOP_32 || Timer_Scaduto(L_P1__GetMainc35(my_id)));
    
    if(res_OrLogicOP_32){
    xorIndex_res_XorLogicOP_19 = (xorIndex_res_XorLogicOP_19 + 1);
    }
    
    res_XorLogicOP_19 = (res_XorLogicOP_19 && (xorIndex_res_XorLogicOP_19 == 1));
    res_ImpliesLogicOp_16 = (res_ImpliesLogicOp_16 && res_XorLogicOP_19);
    }
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_ImpliesLogicOp_16);
    bool res_OrLogicOP_42 = false;
    bool res_AndLogicOP_43 = true;
    bool res_NotLogicOP_44 = true;
    res_NotLogicOP_44 = (res_NotLogicOP_44 && ! Timer_Scaduto(L_P1__GetMainc35(my_id)));
    res_AndLogicOP_43 = (res_AndLogicOP_43 && res_NotLogicOP_44);
    bool res_NotLogicOP_45 = true;
    res_NotLogicOP_45 = (res_NotLogicOP_45 && ! (L_P1__GetMainc28(my_id) == 7u));
    res_AndLogicOP_43 = (res_AndLogicOP_43 && res_NotLogicOP_45);
    
    res_OrLogicOP_42 = (res_OrLogicOP_42 || res_AndLogicOP_43);
    bool res_NotLogicOP_46 = true;
    res_NotLogicOP_46 = (res_NotLogicOP_46 && ! (L_P1__GetInMainc1(my_id) == c270xx));
    res_OrLogicOP_42 = (res_OrLogicOP_42 || res_NotLogicOP_46);
    
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_OrLogicOP_42);
    
    res_ImpliesLogicOp_6 = (res_ImpliesLogicOp_6 && res_AndLogicOP_15);
    }
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_ImpliesLogicOp_6);
    bool res_AndLogicOP_47 = true;
    res_AndLogicOP_47 = (res_AndLogicOP_47 && (L_P1__GetInConsd(my_id) == false));
    res_AndLogicOP_47 = (res_AndLogicOP_47 && (L_P1__GetInConsd(my_id) == false));
    
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_AndLogicOP_47);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_AndLogicOP_5);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *47,48,50,51,*  *,*  la variabile MainClass_C1_variabile_V4 sia  diverso da  True 
    //   *104,* o  che  *34,*  il parametro MainClass_C1_parametro_P8 sia  minore di  *55,* 2
    //   *104,* e  che   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* o  che  *,*  il contatore MainClass_C1_contatore_Co5 non sia  minore di  *55,* 11
    //   *104,* e  che  *34,*  il parametro MainClass_C1_parametro_P4 sia  diverso da  *56,* 6
    //   *104,* e  che  *37,*  la variabile MainClass_C1_variabile_V4 non sia  uguale a  True
    bool res_OrLogicOP_48 = false;
    bool res_OrLogicOP_49 = false;
    bool res_NotLogicOP_50 = true;
    res_NotLogicOP_50 = (res_NotLogicOP_50 && ! (L_P1__GetMainc27(my_id) == true));
    res_OrLogicOP_49 = (res_OrLogicOP_49 || res_NotLogicOP_50);
    bool res_AndLogicOP_51 = true;
    res_AndLogicOP_51 = (res_AndLogicOP_51 && (L_P1__GetParamMainc4(my_id) < 2u));
    res_AndLogicOP_51 = (res_AndLogicOP_51 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_49 = (res_OrLogicOP_49 || res_AndLogicOP_51);
    
    res_OrLogicOP_48 = (res_OrLogicOP_48 || res_OrLogicOP_49);
    bool res_AndLogicOP_52 = true;
    bool res_AndLogicOP_53 = true;
    bool res_NotLogicOP_54 = true;
    res_NotLogicOP_54 = (res_NotLogicOP_54 && ! (Counter_GetValore(L_P1__GetMainc36(my_id)) < 11u));
    res_AndLogicOP_53 = (res_AndLogicOP_53 && res_NotLogicOP_54);
    bool res_NotLogicOP_55 = true;
    res_NotLogicOP_55 = (res_NotLogicOP_55 && ! (L_P1__GetParamMainc2(my_id) == 6u));
    res_AndLogicOP_53 = (res_AndLogicOP_53 && res_NotLogicOP_55);
    
    res_AndLogicOP_52 = (res_AndLogicOP_52 && res_AndLogicOP_53);
    bool res_NotLogicOP_56 = true;
    res_NotLogicOP_56 = (res_NotLogicOP_56 && ! (L_P1__GetMainc27(my_id) == true));
    res_AndLogicOP_52 = (res_AndLogicOP_52 && res_NotLogicOP_56);
    
    res_OrLogicOP_48 = (res_OrLogicOP_48 || res_AndLogicOP_52);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_48);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
    
    { commento: {61,} commento: {38,}  se il contatore MainClass_C1_contatore_Co5 non è  diverso da  commento: {56,} 11 commento: {36,} e  se il timer MainClass_C1_timer_T5 è disattivo commento: {37,} o  se la variabile MainClass_C1_variabile_V3 non è  diverso da  False  commento: {35,} o  se il controllo MainClass_C1_controllo_C7 non è  uguale a c270xx commento: {38,} o  se il contatore MainClass_C1_contatore_Co5 è  diverso da  commento: {56,} 11 e  se l'argomento argomento_ave6 è  uguale a c270xx commento: {39,} , Tutte le seguenti { 
     commento: {61,} commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI3 è scaduto, Tutte le seguenti { 
     commento: {62,} commento: {34,}  se il parametro MainClass_C1_parametro_P4 è  uguale a  commento: {53,} 1 commento: {34,} e  se il parametro MainClass_C1_parametro_P6 è  uguale a c270xx commento: {38,} o  se il contatore MainClass_C1_contatore_Co8 è  uguale a  commento: {53,} 140 e  se l'argomento argomento_ave6 è  diverso da c270xx commento: {39,}  commento: {34,} e  se il parametro MainClass_C1_parametro_P4 non è  diverso da  commento: {56,} 6 commento: {36,} e  se il timer MainClass_C1_timer_T5 non è attivo, Almeno una delle seguenti { 
     commento: {61,} commento: {35,}  se il controllo MainClass_C1_controllo_C7 non è  diverso da c270xx commento: {35,} o  se il controllo MainClass_C1_controllo_C7 è  diverso da c270xx o  se l'argomento argomento_ave6 è  diverso da c270xx commento: {39,}  commento: {35,} o  se il controllo MainClass_C1_controllo_C7 non è  uguale a c270xx commento: {35,} o  se il controllo MainClass_C1_controllo_C7 è  diverso da c270xx, Tutte le seguenti { 
     commento: {62,} commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo, Almeno una delle seguenti { 
     commento: {63,} commento: {38,}  se il contatore MainClass_C1_contatore_Co5 non è  diverso da  commento: {56,} 152 commento: {36,} o  se il timer MainClass_C1_timer_T5 non è disattivo commento: {34,} o  se il parametro MainClass_C1_parametro_P6 è  diverso da c270xx, Solo una delle seguenti { 
     commento: {63,}  se il controllo ConsDef è uguale a FALSE  commento: {35,} o  se il controllo MainClass_C1_controllo_C7 è  uguale a c270xx, Solo una delle seguenti { 
      se il ripristino dello stato  è  uguale a  commento: {53,}  state1  commento: {107,} commento: {37,} e  se la variabile MainClass_C1_variabile_V9 è  diverso da  commento: {56,} 1 o  se l'argomento argomento_ave8 è  uguale a  False  commento: {39,} , Verifica che   commento: {47,48,51,}  commento: {,}  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
     commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P4 sia  uguale a  commento: {53,} 5
     commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co5 sia  maggiore di  commento: {54,} 15
     commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P8 sia  uguale a  commento: {53,} 1
     commento: {104,} o  che  commento: {38,}  il contatore MainClass_C1_contatore_Co5 non sia  maggiore di  commento: {54,} 1513
     commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P6 sia  uguale a c270xx
    
    
     } Verifica che   commento: {48,49,51,}  commento: {,}  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
     commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T5 sia disattivo
     commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co8 sia  uguale a  commento: {53,} 1302
    
    
     } Verifica che   commento: {48,49,52,}  commento: {,}  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
     commento: {104,} o  che  commento: {35,}  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
     commento: {104,} o  che   l'argomento argomento_ave6 non  sia  uguale a c270xx commento: {,} 
     commento: {104,} o  che  commento: {35,}  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
     commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T5 non sia scaduto
    
    
     } Verifica che   commento: {50,51,52,}  commento: {,}  il contatore MainClass_C1_contatore_Co8 non sia  maggiore di  commento: {54,} 1314
     commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V9 non sia  uguale a  commento: {53,} 5
     commento: {104,} o  che   l'argomento argomento_ave8 non  sia  diverso da  True  commento: {,} 
     commento: {104,} o  che  commento: {38,}  il contatore MainClass_C1_contatore_Co8 sia  uguale a  commento: {53,} 13
    
    
     } Verifica che   commento: {48,50,51,}  commento: {,}  la variabile MainClass_C1_variabile_V4 sia  diverso da  True 
     commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
     commento: {104,} e  che  commento: {37,}  la variabile MainClass_C1_variabile_V9 sia  diverso da  commento: {56,} 8
     commento: {104,} e  che  commento: {35,}  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
     commento: {104,} o  che  commento: {35,}  il controllo MainClass_C1_controllo_C7 sia  uguale a c270xx
     commento: {104,} o  che  commento: {,}  il contatore MainClass_C1_contatore_Co8 non sia  diverso da  commento: {56,} 15
    
    
     } Verifica che   commento: {48,50,51,52,}  commento: {,}  la variabile MainClass_C1_variabile_V4 sia  diverso da  False 
     commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co5 sia  diverso da  commento: {56,} 1502
     commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
     commento: {104,} o  che  commento: {37,}  la variabile MainClass_C1_variabile_V1 sia  diverso da  commento: {56,} 7
     commento: {104,} e  che   l'argomento argomento_ave4 non  sia  uguale a  False  commento: {,} 
     commento: {104,} o  che  commento: {35,}  il controllo MainClass_C1_controllo_C7 sia  uguale a c270xx
    
    
     } Verifica che   commento: {51,52,}  commento: {,}  il contatore MainClass_C1_contatore_Co8 sia  minore di  commento: {55,} 14
     commento: {104,} e  che   l'argomento argomento_ave6 sia  diverso da c270xx commento: {,} 
    
    
     } Verifica che   commento: {47,48,49,51,}  commento: {,}  il controllo MainClass_C1_controllo_C7 non sia  diverso da c270xx
     commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co5 sia  maggiore di  commento: {54,} 131
     commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T5 non sia disattivo
     commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P4 non sia  uguale a  commento: {53,} 5
    
    
    }
*/
bool L_P1__Macro5(instance_id_t const my_id , C1_Enumerat3 argom11, bool argom12, C1_Enumerat4 argom13, bool argom14)
{
bool res_AndLogicOP_0 = true;
    
    //  *61,* *38,*  se il contatore MainClass_C1_contatore_Co5 non è  diverso da  *56,* 11 *36,* e  se il timer MainClass_C1_timer_T5 è disattivo *37,* o  se la variabile MainClass_C1_variabile_V3 non è  diverso da  False  *35,* o  se il controllo MainClass_C1_controllo_C7 non è  uguale a c270xx *38,* o  se il contatore MainClass_C1_contatore_Co5 è  diverso da  *56,* 11 e  se l'argomento argomento_ave6 è  uguale a c270xx *39,* , Tutte le seguenti { 
    //   *61,* *110,*  se il ripristino del timer  MainClass_C1_restoreTI_TI3 è scaduto, Tutte le seguenti { 
    //   *62,* *34,*  se il parametro MainClass_C1_parametro_P4 è  uguale a  *53,* 1 *34,* e  se il parametro MainClass_C1_parametro_P6 è  uguale a c270xx *38,* o  se il contatore MainClass_C1_contatore_Co8 è  uguale a  *53,* 140 e  se l'argomento argomento_ave6 è  diverso da c270xx *39,*  *34,* e  se il parametro MainClass_C1_parametro_P4 non è  diverso da  *56,* 6 *36,* e  se il timer MainClass_C1_timer_T5 non è attivo, Almeno una delle seguenti { 
    //   *61,* *35,*  se il controllo MainClass_C1_controllo_C7 non è  diverso da c270xx *35,* o  se il controllo MainClass_C1_controllo_C7 è  diverso da c270xx o  se l'argomento argomento_ave6 è  diverso da c270xx *39,*  *35,* o  se il controllo MainClass_C1_controllo_C7 non è  uguale a c270xx *35,* o  se il controllo MainClass_C1_controllo_C7 è  diverso da c270xx, Tutte le seguenti { 
    //   *62,* *110,*  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo, Almeno una delle seguenti { 
    //   *63,* *38,*  se il contatore MainClass_C1_contatore_Co5 non è  diverso da  *56,* 152 *36,* o  se il timer MainClass_C1_timer_T5 non è disattivo *34,* o  se il parametro MainClass_C1_parametro_P6 è  diverso da c270xx, Solo una delle seguenti { 
    //   *63,*  se il controllo ConsDef è uguale a FALSE  *35,* o  se il controllo MainClass_C1_controllo_C7 è  uguale a c270xx, Solo una delle seguenti { 
    //    se il ripristino dello stato  è  uguale a  *53,*  state1  *107,* *37,* e  se la variabile MainClass_C1_variabile_V9 è  diverso da  *56,* 1 o  se l'argomento argomento_ave8 è  uguale a  False  *39,* , Verifica che   *47,48,51,*  *,*  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
    //   *104,* e  che  *34,*  il parametro MainClass_C1_parametro_P4 sia  uguale a  *53,* 5
    //   *104,* e  che  *,*  il contatore MainClass_C1_contatore_Co5 sia  maggiore di  *54,* 15
    //   *104,* e  che  *34,*  il parametro MainClass_C1_parametro_P8 sia  uguale a  *53,* 1
    //   *104,* o  che  *38,*  il contatore MainClass_C1_contatore_Co5 non sia  maggiore di  *54,* 1513
    //   *104,* e  che  *34,*  il parametro MainClass_C1_parametro_P6 sia  uguale a c270xx
    //   } Verifica che   *48,49,51,*  *,*  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
    //   *104,* o  che  *,*  il timer MainClass_C1_timer_T5 sia disattivo
    //   *104,* e  che  *,*  il contatore MainClass_C1_contatore_Co8 sia  uguale a  *53,* 1302
    //   } Verifica che   *48,49,52,*  *,*  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
    //   *104,* o  che  *35,*  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
    //   *104,* o  che   l'argomento argomento_ave6 non  sia  uguale a c270xx *,* 
    //   *104,* o  che  *35,*  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
    //   *104,* o  che  *,*  il timer MainClass_C1_timer_T5 non sia scaduto
    //   } Verifica che   *50,51,52,*  *,*  il contatore MainClass_C1_contatore_Co8 non sia  maggiore di  *54,* 1314
    //   *104,* e  che  *,*  la variabile MainClass_C1_variabile_V9 non sia  uguale a  *53,* 5
    //   *104,* o  che   l'argomento argomento_ave8 non  sia  diverso da  True  *,* 
    //   *104,* o  che  *38,*  il contatore MainClass_C1_contatore_Co8 sia  uguale a  *53,* 13
    //   } Verifica che   *48,50,51,*  *,*  la variabile MainClass_C1_variabile_V4 sia  diverso da  True 
    //   *104,* e  che  *,*  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
    //   *104,* e  che  *37,*  la variabile MainClass_C1_variabile_V9 sia  diverso da  *56,* 8
    //   *104,* e  che  *35,*  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
    //   *104,* o  che  *35,*  il controllo MainClass_C1_controllo_C7 sia  uguale a c270xx
    //   *104,* o  che  *,*  il contatore MainClass_C1_contatore_Co8 non sia  diverso da  *56,* 15
    //   } Verifica che   *48,50,51,52,*  *,*  la variabile MainClass_C1_variabile_V4 sia  diverso da  False 
    //   *104,* e  che  *,*  il contatore MainClass_C1_contatore_Co5 sia  diverso da  *56,* 1502
    //   *104,* e  che  *,*  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
    //   *104,* o  che  *37,*  la variabile MainClass_C1_variabile_V1 sia  diverso da  *56,* 7
    //   *104,* e  che   l'argomento argomento_ave4 non  sia  uguale a  False  *,* 
    //   *104,* o  che  *35,*  il controllo MainClass_C1_controllo_C7 sia  uguale a c270xx
    //   } Verifica che   *51,52,*  *,*  il contatore MainClass_C1_contatore_Co8 sia  minore di  *55,* 14
    //   *104,* e  che   l'argomento argomento_ave6 sia  diverso da c270xx *,* 
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_OrLogicOP_4 = false;
    bool res_AndLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (Counter_GetValore(L_P1__GetMainc36(my_id)) == 11u));
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! res_NotLogicOP_7);
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_6);
    res_AndLogicOP_5 = (res_AndLogicOP_5 && Timer_Disattivo(L_P1__GetMainc35(my_id)));
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_AndLogicOP_5);
    bool res_NotLogicOP_8 = true;
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetMainc26(my_id) == false));
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! res_NotLogicOP_9);
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_NotLogicOP_8);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_OrLogicOP_4);
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__GetInMainc1(my_id) == c270xx));
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_NotLogicOP_10);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    bool res_AndLogicOP_11 = true;
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (Counter_GetValore(L_P1__GetMainc36(my_id)) == 11u));
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_NotLogicOP_12);
    res_AndLogicOP_11 = (res_AndLogicOP_11 && (argom13 == c270xx));
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_11);
    
    if(res_OrLogicOP_2){
    bool res_AndLogicOP_13 = true;
    bool res_ImpliesLogicOp_14 = true;
    if(Timer_Scaduto(L_P1__GetMainc34(my_id))){
    bool res_AndLogicOP_15 = true;
    bool res_ImpliesLogicOp_16 = true;
    bool res_OrLogicOP_17 = false;
    bool res_AndLogicOP_18 = true;
    res_AndLogicOP_18 = (res_AndLogicOP_18 && (L_P1__GetParamMainc2(my_id) == 1u));
    res_AndLogicOP_18 = (res_AndLogicOP_18 && (L_P1__GetParamMainc3(my_id) == c270xx));
    
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_AndLogicOP_18);
    bool res_AndLogicOP_19 = true;
    bool res_AndLogicOP_20 = true;
    bool res_AndLogicOP_21 = true;
    res_AndLogicOP_21 = (res_AndLogicOP_21 && (Counter_GetValore(L_P1__GetMainc37(my_id)) == 140u));
    bool res_NotLogicOP_22 = true;
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! (argom13 == c270xx));
    res_AndLogicOP_21 = (res_AndLogicOP_21 && res_NotLogicOP_22);
    
    res_AndLogicOP_20 = (res_AndLogicOP_20 && res_AndLogicOP_21);
    bool res_NotLogicOP_23 = true;
    bool res_NotLogicOP_24 = true;
    res_NotLogicOP_24 = (res_NotLogicOP_24 && ! (L_P1__GetParamMainc2(my_id) == 6u));
    res_NotLogicOP_23 = (res_NotLogicOP_23 && ! res_NotLogicOP_24);
    res_AndLogicOP_20 = (res_AndLogicOP_20 && res_NotLogicOP_23);
    
    res_AndLogicOP_19 = (res_AndLogicOP_19 && res_AndLogicOP_20);
    bool res_NotLogicOP_25 = true;
    res_NotLogicOP_25 = (res_NotLogicOP_25 && ! Timer_Attivo(L_P1__GetMainc35(my_id)));
    res_AndLogicOP_19 = (res_AndLogicOP_19 && res_NotLogicOP_25);
    
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_AndLogicOP_19);
    
    if(res_OrLogicOP_17){
    bool res_OrLogicOP_26 = false;
    bool res_ImpliesLogicOp_27 = true;
    bool res_OrLogicOP_28 = false;
    bool res_OrLogicOP_29 = false;
    bool res_OrLogicOP_30 = false;
    bool res_OrLogicOP_31 = false;
    bool res_NotLogicOP_32 = true;
    bool res_NotLogicOP_33 = true;
    res_NotLogicOP_33 = (res_NotLogicOP_33 && ! (L_P1__GetInMainc1(my_id) == c270xx));
    res_NotLogicOP_32 = (res_NotLogicOP_32 && ! res_NotLogicOP_33);
    res_OrLogicOP_31 = (res_OrLogicOP_31 || res_NotLogicOP_32);
    bool res_NotLogicOP_34 = true;
    res_NotLogicOP_34 = (res_NotLogicOP_34 && ! (L_P1__GetInMainc1(my_id) == c270xx));
    res_OrLogicOP_31 = (res_OrLogicOP_31 || res_NotLogicOP_34);
    
    res_OrLogicOP_30 = (res_OrLogicOP_30 || res_OrLogicOP_31);
    bool res_NotLogicOP_35 = true;
    res_NotLogicOP_35 = (res_NotLogicOP_35 && ! (argom13 == c270xx));
    res_OrLogicOP_30 = (res_OrLogicOP_30 || res_NotLogicOP_35);
    
    res_OrLogicOP_29 = (res_OrLogicOP_29 || res_OrLogicOP_30);
    bool res_NotLogicOP_36 = true;
    res_NotLogicOP_36 = (res_NotLogicOP_36 && ! (L_P1__GetInMainc1(my_id) == c270xx));
    res_OrLogicOP_29 = (res_OrLogicOP_29 || res_NotLogicOP_36);
    
    res_OrLogicOP_28 = (res_OrLogicOP_28 || res_OrLogicOP_29);
    bool res_NotLogicOP_37 = true;
    res_NotLogicOP_37 = (res_NotLogicOP_37 && ! (L_P1__GetInMainc1(my_id) == c270xx));
    res_OrLogicOP_28 = (res_OrLogicOP_28 || res_NotLogicOP_37);
    
    if(res_OrLogicOP_28){
    bool res_AndLogicOP_38 = true;
    bool res_ImpliesLogicOp_39 = true;
    bool res_NotLogicOP_40 = true;
    res_NotLogicOP_40 = (res_NotLogicOP_40 && ! Timer_Attivo(L_P1__GetMainc30(my_id)));
    if(res_NotLogicOP_40){
    bool res_OrLogicOP_41 = false;
    bool res_ImpliesLogicOp_42 = true;
    bool res_OrLogicOP_43 = false;
    bool res_OrLogicOP_44 = false;
    bool res_NotLogicOP_45 = true;
    bool res_NotLogicOP_46 = true;
    res_NotLogicOP_46 = (res_NotLogicOP_46 && ! (Counter_GetValore(L_P1__GetMainc36(my_id)) == 152u));
    res_NotLogicOP_45 = (res_NotLogicOP_45 && ! res_NotLogicOP_46);
    res_OrLogicOP_44 = (res_OrLogicOP_44 || res_NotLogicOP_45);
    bool res_NotLogicOP_47 = true;
    res_NotLogicOP_47 = (res_NotLogicOP_47 && ! Timer_Disattivo(L_P1__GetMainc35(my_id)));
    res_OrLogicOP_44 = (res_OrLogicOP_44 || res_NotLogicOP_47);
    
    res_OrLogicOP_43 = (res_OrLogicOP_43 || res_OrLogicOP_44);
    bool res_NotLogicOP_48 = true;
    res_NotLogicOP_48 = (res_NotLogicOP_48 && ! (L_P1__GetParamMainc3(my_id) == c270xx));
    res_OrLogicOP_43 = (res_OrLogicOP_43 || res_NotLogicOP_48);
    
    if(res_OrLogicOP_43){
    bool res_XorLogicOP_49 = true;
    int xorIndex_res_XorLogicOP_49 = 0;
    bool res_ImpliesLogicOp_50 = true;
    bool res_OrLogicOP_51 = false;
    res_OrLogicOP_51 = (res_OrLogicOP_51 || (L_P1__GetInConsd(my_id) == false));
    res_OrLogicOP_51 = (res_OrLogicOP_51 || (L_P1__GetInMainc1(my_id) == c270xx));
    
    if(res_OrLogicOP_51){
    bool res_ImpliesLogicOp_52 = true;
    bool res_OrLogicOP_53 = false;
    bool res_AndLogicOP_54 = true;
    res_AndLogicOP_54 = (res_AndLogicOP_54 && (L_P1__GetStato1(my_id) == C1_St_state));
    bool res_NotLogicOP_55 = true;
    res_NotLogicOP_55 = (res_NotLogicOP_55 && ! (L_P1__GetMainc28(my_id) == 1u));
    res_AndLogicOP_54 = (res_AndLogicOP_54 && res_NotLogicOP_55);
    
    res_OrLogicOP_53 = (res_OrLogicOP_53 || res_AndLogicOP_54);
    res_OrLogicOP_53 = (res_OrLogicOP_53 || (argom14 == false));
    
    if(res_OrLogicOP_53){
    bool res_OrLogicOP_56 = false;
    bool res_AndLogicOP_57 = true;
    bool res_AndLogicOP_58 = true;
    bool res_AndLogicOP_59 = true;
    bool res_NotLogicOP_60 = true;
    res_NotLogicOP_60 = (res_NotLogicOP_60 && ! (L_P1__GetInMainc1(my_id) == c270xx));
    res_AndLogicOP_59 = (res_AndLogicOP_59 && res_NotLogicOP_60);
    res_AndLogicOP_59 = (res_AndLogicOP_59 && (L_P1__GetParamMainc2(my_id) == 5u));
    
    res_AndLogicOP_58 = (res_AndLogicOP_58 && res_AndLogicOP_59);
    res_AndLogicOP_58 = (res_AndLogicOP_58 && (Counter_GetValore(L_P1__GetMainc36(my_id)) > 15u));
    
    res_AndLogicOP_57 = (res_AndLogicOP_57 && res_AndLogicOP_58);
    res_AndLogicOP_57 = (res_AndLogicOP_57 && (L_P1__GetParamMainc4(my_id) == 1u));
    
    res_OrLogicOP_56 = (res_OrLogicOP_56 || res_AndLogicOP_57);
    bool res_AndLogicOP_61 = true;
    bool res_NotLogicOP_62 = true;
    res_NotLogicOP_62 = (res_NotLogicOP_62 && ! (Counter_GetValore(L_P1__GetMainc36(my_id)) > 1513u));
    res_AndLogicOP_61 = (res_AndLogicOP_61 && res_NotLogicOP_62);
    res_AndLogicOP_61 = (res_AndLogicOP_61 && (L_P1__GetParamMainc3(my_id) == c270xx));
    
    res_OrLogicOP_56 = (res_OrLogicOP_56 || res_AndLogicOP_61);
    
    res_ImpliesLogicOp_52 = (res_ImpliesLogicOp_52 && res_OrLogicOP_56);
    }
    res_ImpliesLogicOp_50 = (res_ImpliesLogicOp_50 && res_ImpliesLogicOp_52);
    }
    if(res_ImpliesLogicOp_50){
    xorIndex_res_XorLogicOP_49 = (xorIndex_res_XorLogicOP_49 + 1);
    }
    bool res_OrLogicOP_63 = false;
    bool res_NotLogicOP_64 = true;
    res_NotLogicOP_64 = (res_NotLogicOP_64 && ! (L_P1__GetInMainc1(my_id) == c270xx));
    res_OrLogicOP_63 = (res_OrLogicOP_63 || res_NotLogicOP_64);
    bool res_AndLogicOP_65 = true;
    res_AndLogicOP_65 = (res_AndLogicOP_65 && Timer_Disattivo(L_P1__GetMainc35(my_id)));
    res_AndLogicOP_65 = (res_AndLogicOP_65 && (Counter_GetValore(L_P1__GetMainc37(my_id)) == 1302u));
    
    res_OrLogicOP_63 = (res_OrLogicOP_63 || res_AndLogicOP_65);
    
    if(res_OrLogicOP_63){
    xorIndex_res_XorLogicOP_49 = (xorIndex_res_XorLogicOP_49 + 1);
    }
    
    res_XorLogicOP_49 = (res_XorLogicOP_49 && (xorIndex_res_XorLogicOP_49 == 1));
    res_ImpliesLogicOp_42 = (res_ImpliesLogicOp_42 && res_XorLogicOP_49);
    }
    res_OrLogicOP_41 = (res_OrLogicOP_41 || res_ImpliesLogicOp_42);
    bool res_OrLogicOP_66 = false;
    bool res_OrLogicOP_67 = false;
    bool res_OrLogicOP_68 = false;
    bool res_OrLogicOP_69 = false;
    bool res_NotLogicOP_70 = true;
    res_NotLogicOP_70 = (res_NotLogicOP_70 && ! (L_P1__GetInMainc1(my_id) == c270xx));
    res_OrLogicOP_69 = (res_OrLogicOP_69 || res_NotLogicOP_70);
    bool res_NotLogicOP_71 = true;
    res_NotLogicOP_71 = (res_NotLogicOP_71 && ! (L_P1__GetInMainc1(my_id) == c270xx));
    res_OrLogicOP_69 = (res_OrLogicOP_69 || res_NotLogicOP_71);
    
    res_OrLogicOP_68 = (res_OrLogicOP_68 || res_OrLogicOP_69);
    bool res_NotLogicOP_72 = true;
    res_NotLogicOP_72 = (res_NotLogicOP_72 && ! (argom13 == c270xx));
    res_OrLogicOP_68 = (res_OrLogicOP_68 || res_NotLogicOP_72);
    
    res_OrLogicOP_67 = (res_OrLogicOP_67 || res_OrLogicOP_68);
    bool res_NotLogicOP_73 = true;
    res_NotLogicOP_73 = (res_NotLogicOP_73 && ! (L_P1__GetInMainc1(my_id) == c270xx));
    res_OrLogicOP_67 = (res_OrLogicOP_67 || res_NotLogicOP_73);
    
    res_OrLogicOP_66 = (res_OrLogicOP_66 || res_OrLogicOP_67);
    bool res_NotLogicOP_74 = true;
    res_NotLogicOP_74 = (res_NotLogicOP_74 && ! Timer_Scaduto(L_P1__GetMainc35(my_id)));
    res_OrLogicOP_66 = (res_OrLogicOP_66 || res_NotLogicOP_74);
    
    res_OrLogicOP_41 = (res_OrLogicOP_41 || res_OrLogicOP_66);
    
    res_ImpliesLogicOp_39 = (res_ImpliesLogicOp_39 && res_OrLogicOP_41);
    }
    res_AndLogicOP_38 = (res_AndLogicOP_38 && res_ImpliesLogicOp_39);
    bool res_OrLogicOP_75 = false;
    bool res_OrLogicOP_76 = false;
    bool res_AndLogicOP_77 = true;
    bool res_NotLogicOP_78 = true;
    res_NotLogicOP_78 = (res_NotLogicOP_78 && ! (Counter_GetValore(L_P1__GetMainc37(my_id)) > 1314u));
    res_AndLogicOP_77 = (res_AndLogicOP_77 && res_NotLogicOP_78);
    bool res_NotLogicOP_79 = true;
    res_NotLogicOP_79 = (res_NotLogicOP_79 && ! (L_P1__GetMainc28(my_id) == 5u));
    res_AndLogicOP_77 = (res_AndLogicOP_77 && res_NotLogicOP_79);
    
    res_OrLogicOP_76 = (res_OrLogicOP_76 || res_AndLogicOP_77);
    bool res_NotLogicOP_80 = true;
    bool res_NotLogicOP_81 = true;
    res_NotLogicOP_81 = (res_NotLogicOP_81 && ! (argom14 == true));
    res_NotLogicOP_80 = (res_NotLogicOP_80 && ! res_NotLogicOP_81);
    res_OrLogicOP_76 = (res_OrLogicOP_76 || res_NotLogicOP_80);
    
    res_OrLogicOP_75 = (res_OrLogicOP_75 || res_OrLogicOP_76);
    res_OrLogicOP_75 = (res_OrLogicOP_75 || (Counter_GetValore(L_P1__GetMainc37(my_id)) == 13u));
    
    res_AndLogicOP_38 = (res_AndLogicOP_38 && res_OrLogicOP_75);
    
    res_ImpliesLogicOp_27 = (res_ImpliesLogicOp_27 && res_AndLogicOP_38);
    }
    res_OrLogicOP_26 = (res_OrLogicOP_26 || res_ImpliesLogicOp_27);
    bool res_OrLogicOP_82 = false;
    bool res_OrLogicOP_83 = false;
    bool res_AndLogicOP_84 = true;
    bool res_AndLogicOP_85 = true;
    bool res_AndLogicOP_86 = true;
    bool res_NotLogicOP_87 = true;
    res_NotLogicOP_87 = (res_NotLogicOP_87 && ! (L_P1__GetMainc27(my_id) == true));
    res_AndLogicOP_86 = (res_AndLogicOP_86 && res_NotLogicOP_87);
    bool res_NotLogicOP_88 = true;
    res_NotLogicOP_88 = (res_NotLogicOP_88 && ! (L_P1__GetInMainc1(my_id) == c270xx));
    res_AndLogicOP_86 = (res_AndLogicOP_86 && res_NotLogicOP_88);
    
    res_AndLogicOP_85 = (res_AndLogicOP_85 && res_AndLogicOP_86);
    bool res_NotLogicOP_89 = true;
    res_NotLogicOP_89 = (res_NotLogicOP_89 && ! (L_P1__GetMainc28(my_id) == 8u));
    res_AndLogicOP_85 = (res_AndLogicOP_85 && res_NotLogicOP_89);
    
    res_AndLogicOP_84 = (res_AndLogicOP_84 && res_AndLogicOP_85);
    bool res_NotLogicOP_90 = true;
    res_NotLogicOP_90 = (res_NotLogicOP_90 && ! (L_P1__GetInMainc1(my_id) == c270xx));
    res_AndLogicOP_84 = (res_AndLogicOP_84 && res_NotLogicOP_90);
    
    res_OrLogicOP_83 = (res_OrLogicOP_83 || res_AndLogicOP_84);
    res_OrLogicOP_83 = (res_OrLogicOP_83 || (L_P1__GetInMainc1(my_id) == c270xx));
    
    res_OrLogicOP_82 = (res_OrLogicOP_82 || res_OrLogicOP_83);
    bool res_NotLogicOP_91 = true;
    bool res_NotLogicOP_92 = true;
    res_NotLogicOP_92 = (res_NotLogicOP_92 && ! (Counter_GetValore(L_P1__GetMainc37(my_id)) == 15u));
    res_NotLogicOP_91 = (res_NotLogicOP_91 && ! res_NotLogicOP_92);
    res_OrLogicOP_82 = (res_OrLogicOP_82 || res_NotLogicOP_91);
    
    res_OrLogicOP_26 = (res_OrLogicOP_26 || res_OrLogicOP_82);
    
    res_ImpliesLogicOp_16 = (res_ImpliesLogicOp_16 && res_OrLogicOP_26);
    }
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_ImpliesLogicOp_16);
    bool res_OrLogicOP_93 = false;
    bool res_OrLogicOP_94 = false;
    bool res_AndLogicOP_95 = true;
    bool res_AndLogicOP_96 = true;
    bool res_NotLogicOP_97 = true;
    res_NotLogicOP_97 = (res_NotLogicOP_97 && ! (L_P1__GetMainc27(my_id) == false));
    res_AndLogicOP_96 = (res_AndLogicOP_96 && res_NotLogicOP_97);
    bool res_NotLogicOP_98 = true;
    res_NotLogicOP_98 = (res_NotLogicOP_98 && ! (Counter_GetValore(L_P1__GetMainc36(my_id)) == 1502u));
    res_AndLogicOP_96 = (res_AndLogicOP_96 && res_NotLogicOP_98);
    
    res_AndLogicOP_95 = (res_AndLogicOP_95 && res_AndLogicOP_96);
    bool res_NotLogicOP_99 = true;
    res_NotLogicOP_99 = (res_NotLogicOP_99 && ! (L_P1__GetInMainc1(my_id) == c270xx));
    res_AndLogicOP_95 = (res_AndLogicOP_95 && res_NotLogicOP_99);
    
    res_OrLogicOP_94 = (res_OrLogicOP_94 || res_AndLogicOP_95);
    bool res_AndLogicOP_100 = true;
    bool res_NotLogicOP_101 = true;
    res_NotLogicOP_101 = (res_NotLogicOP_101 && ! (L_P1__GetMainc25(my_id) == 7u));
    res_AndLogicOP_100 = (res_AndLogicOP_100 && res_NotLogicOP_101);
    bool res_NotLogicOP_102 = true;
    res_NotLogicOP_102 = (res_NotLogicOP_102 && ! (argom12 == false));
    res_AndLogicOP_100 = (res_AndLogicOP_100 && res_NotLogicOP_102);
    
    res_OrLogicOP_94 = (res_OrLogicOP_94 || res_AndLogicOP_100);
    
    res_OrLogicOP_93 = (res_OrLogicOP_93 || res_OrLogicOP_94);
    res_OrLogicOP_93 = (res_OrLogicOP_93 || (L_P1__GetInMainc1(my_id) == c270xx));
    
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_OrLogicOP_93);
    
    res_ImpliesLogicOp_14 = (res_ImpliesLogicOp_14 && res_AndLogicOP_15);
    }
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_ImpliesLogicOp_14);
    bool res_AndLogicOP_103 = true;
    res_AndLogicOP_103 = (res_AndLogicOP_103 && (Counter_GetValore(L_P1__GetMainc37(my_id)) < 14u));
    bool res_NotLogicOP_104 = true;
    res_NotLogicOP_104 = (res_NotLogicOP_104 && ! (argom13 == c270xx));
    res_AndLogicOP_103 = (res_AndLogicOP_103 && res_NotLogicOP_104);
    
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_AndLogicOP_103);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_AndLogicOP_13);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *47,48,49,51,*  *,*  il controllo MainClass_C1_controllo_C7 non sia  diverso da c270xx
    //   *104,* e  che  *,*  il contatore MainClass_C1_contatore_Co5 sia  maggiore di  *54,* 131
    //   *104,* e  che  *,*  il timer MainClass_C1_timer_T5 non sia disattivo
    //   *104,* o  che  *34,*  il parametro MainClass_C1_parametro_P4 non sia  uguale a  *53,* 5
    bool res_OrLogicOP_105 = false;
    bool res_AndLogicOP_106 = true;
    bool res_AndLogicOP_107 = true;
    bool res_NotLogicOP_108 = true;
    bool res_NotLogicOP_109 = true;
    res_NotLogicOP_109 = (res_NotLogicOP_109 && ! (L_P1__GetInMainc1(my_id) == c270xx));
    res_NotLogicOP_108 = (res_NotLogicOP_108 && ! res_NotLogicOP_109);
    res_AndLogicOP_107 = (res_AndLogicOP_107 && res_NotLogicOP_108);
    res_AndLogicOP_107 = (res_AndLogicOP_107 && (Counter_GetValore(L_P1__GetMainc36(my_id)) > 131u));
    
    res_AndLogicOP_106 = (res_AndLogicOP_106 && res_AndLogicOP_107);
    bool res_NotLogicOP_110 = true;
    res_NotLogicOP_110 = (res_NotLogicOP_110 && ! Timer_Disattivo(L_P1__GetMainc35(my_id)));
    res_AndLogicOP_106 = (res_AndLogicOP_106 && res_NotLogicOP_110);
    
    res_OrLogicOP_105 = (res_OrLogicOP_105 || res_AndLogicOP_106);
    bool res_NotLogicOP_111 = true;
    res_NotLogicOP_111 = (res_NotLogicOP_111 && ! (L_P1__GetParamMainc2(my_id) == 5u));
    res_OrLogicOP_105 = (res_OrLogicOP_105 || res_NotLogicOP_111);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_105);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
    
    { commento: {62,}  se l'argomento argomento_ave1 è  diverso da  False  commento: {39,}  commento: {36,} o  se il timer MainClass_C1_timer_T5 non è scaduto commento: {34,} e  se il parametro MainClass_C1_parametro_P4 non è  diverso da  commento: {56,} 8 commento: {34,} e  se il parametro MainClass_C1_parametro_P6 è  uguale a c270xx commento: {34,} e  se il parametro MainClass_C1_parametro_P4 non è  uguale a  commento: {53,} 6, Almeno una delle seguenti { 
     commento: {62,} commento: {34,}  se il parametro MainClass_C1_parametro_P4 non è  diverso da  commento: {56,} 5 o  se l'argomento argomento_ave7 è  diverso da RossoGialloGiallo commento: {39,}  commento: {34,} o  se il parametro MainClass_C1_parametro_P8 è  minore di  commento: {55,} 7 commento: {38,} e  se il contatore MainClass_C1_contatore_Co5 è  diverso da  commento: {56,} 12453 commento: {34,} e  se il parametro MainClass_C1_parametro_P4 è  minore di  commento: {55,} 7, Almeno una delle seguenti { 
     commento: {61,} commento: {35,}  se il controllo MainClass_C1_controllo_C7 è  diverso da c270xx commento: {38,} o  se il contatore MainClass_C1_contatore_Co5 è  uguale a  commento: {53,} 144 commento: {35,} e  se il controllo MainClass_C1_controllo_C7 non è  diverso da c270xx, Tutte le seguenti { 
      se la macro  MainClass_C1_macrova_M7 ( con argomento_a10   uguale a True ,argomento_a1   uguale a AC ,argomento_a3   uguale a AC ,argomento_a7   uguale a c270  e argomento_a9   uguale a c270 )   è  diverso da RossoGialloaVerdea commento: {40,}  commento: {34,} o  se il parametro MainClass_C1_parametro_P4 non è  maggiore di  commento: {54,} 5 commento: {34,} e  se il parametro MainClass_C1_parametro_P4 non è  uguale a  commento: {53,} 7 commento: {37,} e  se la variabile MainClass_C1_variabile_V4 non è  uguale a  True  commento: {36,} o  se il timer MainClass_C1_timer_T5 è disattivo commento: {38,} o  se il contatore MainClass_C1_contatore_Co8 è  uguale a  commento: {53,} 11, Verifica che   commento: {47,49,50,52,}  commento: {,}  il timer MainClass_C1_timer_T5 non sia scaduto
     commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P4 sia  diverso da  commento: {56,} 8
     commento: {104,} o  che   l'argomento argomento_ave3 non  sia  diverso da  True  commento: {,} 
     commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V4 sia  uguale a  True 
     commento: {104,} o  che  commento: {36,}  il timer MainClass_C1_timer_T5 non sia disattivo
    
    
     } Verifica che   commento: {47,49,50,}  commento: {34,}  il parametro MainClass_C1_parametro_P4 non sia  maggiore di  commento: {54,} 6
     commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V1 non sia  minore di  commento: {55,} 7
     commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T5 sia attivo
    
    
     } Verifica che   commento: {47,48,49,50,}  commento: {,}  la variabile MainClass_C1_variabile_V4 non sia  diverso da  False 
     commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T5 non sia scaduto
     commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P6 non sia  uguale a c270xx
     commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
    
    
     } Verifica che   commento: {47,51,}  commento: {,}  il contatore MainClass_C1_contatore_Co8 non sia  uguale a  commento: {53,} 12
     commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P8 sia  uguale a  commento: {53,} 7
     commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P4 non sia  diverso da  commento: {56,} 6
    
    
    }
*/
bool L_P1__Macro6(instance_id_t const my_id , bool argom15, C1_Enumerat3 argom16, bool argom17, C1_Enumerat3 argom18, bool argom19)
{
bool res_AndLogicOP_0 = true;
    
    //  *62,*  se l'argomento argomento_ave1 è  diverso da  False  *39,*  *36,* o  se il timer MainClass_C1_timer_T5 non è scaduto *34,* e  se il parametro MainClass_C1_parametro_P4 non è  diverso da  *56,* 8 *34,* e  se il parametro MainClass_C1_parametro_P6 è  uguale a c270xx *34,* e  se il parametro MainClass_C1_parametro_P4 non è  uguale a  *53,* 6, Almeno una delle seguenti { 
    //   *62,* *34,*  se il parametro MainClass_C1_parametro_P4 non è  diverso da  *56,* 5 o  se l'argomento argomento_ave7 è  diverso da RossoGialloGiallo *39,*  *34,* o  se il parametro MainClass_C1_parametro_P8 è  minore di  *55,* 7 *38,* e  se il contatore MainClass_C1_contatore_Co5 è  diverso da  *56,* 12453 *34,* e  se il parametro MainClass_C1_parametro_P4 è  minore di  *55,* 7, Almeno una delle seguenti { 
    //   *61,* *35,*  se il controllo MainClass_C1_controllo_C7 è  diverso da c270xx *38,* o  se il contatore MainClass_C1_contatore_Co5 è  uguale a  *53,* 144 *35,* e  se il controllo MainClass_C1_controllo_C7 non è  diverso da c270xx, Tutte le seguenti { 
    //    se la macro  MainClass_C1_macrova_M7 ( con argomento_a10   uguale a True ,argomento_a1   uguale a AC ,argomento_a3   uguale a AC ,argomento_a7   uguale a c270  e argomento_a9   uguale a c270 )   è  diverso da RossoGialloaVerdea *40,*  *34,* o  se il parametro MainClass_C1_parametro_P4 non è  maggiore di  *54,* 5 *34,* e  se il parametro MainClass_C1_parametro_P4 non è  uguale a  *53,* 7 *37,* e  se la variabile MainClass_C1_variabile_V4 non è  uguale a  True  *36,* o  se il timer MainClass_C1_timer_T5 è disattivo *38,* o  se il contatore MainClass_C1_contatore_Co8 è  uguale a  *53,* 11, Verifica che   *47,49,50,52,*  *,*  il timer MainClass_C1_timer_T5 non sia scaduto
    //   *104,* e  che  *34,*  il parametro MainClass_C1_parametro_P4 sia  diverso da  *56,* 8
    //   *104,* o  che   l'argomento argomento_ave3 non  sia  diverso da  True  *,* 
    //   *104,* o  che  *,*  la variabile MainClass_C1_variabile_V4 sia  uguale a  True 
    //   *104,* o  che  *36,*  il timer MainClass_C1_timer_T5 non sia disattivo
    //   } Verifica che   *47,49,50,*  *34,*  il parametro MainClass_C1_parametro_P4 non sia  maggiore di  *54,* 6
    //   *104,* e  che  *,*  la variabile MainClass_C1_variabile_V1 non sia  minore di  *55,* 7
    //   *104,* o  che  *,*  il timer MainClass_C1_timer_T5 sia attivo
    //   } Verifica che   *47,48,49,50,*  *,*  la variabile MainClass_C1_variabile_V4 non sia  diverso da  False 
    //   *104,* o  che  *,*  il timer MainClass_C1_timer_T5 non sia scaduto
    //   *104,* o  che  *34,*  il parametro MainClass_C1_parametro_P6 non sia  uguale a c270xx
    //   *104,* o  che  *,*  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (argom15 == false));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_3);
    bool res_AndLogicOP_4 = true;
    bool res_AndLogicOP_5 = true;
    bool res_AndLogicOP_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! Timer_Scaduto(L_P1__GetMainc35(my_id)));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_7);
    bool res_NotLogicOP_8 = true;
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetParamMainc2(my_id) == 8u));
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! res_NotLogicOP_9);
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_8);
    
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_AndLogicOP_6);
    res_AndLogicOP_5 = (res_AndLogicOP_5 && (L_P1__GetParamMainc3(my_id) == c270xx));
    
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_AndLogicOP_5);
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__GetParamMainc2(my_id) == 6u));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_10);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_4);
    
    if(res_OrLogicOP_2){
    bool res_OrLogicOP_11 = false;
    bool res_ImpliesLogicOp_12 = true;
    bool res_OrLogicOP_13 = false;
    bool res_OrLogicOP_14 = false;
    bool res_NotLogicOP_15 = true;
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (L_P1__GetParamMainc2(my_id) == 5u));
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! res_NotLogicOP_16);
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_NotLogicOP_15);
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! (argom18 == rossogiallo2));
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_NotLogicOP_17);
    
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_OrLogicOP_14);
    bool res_AndLogicOP_18 = true;
    bool res_AndLogicOP_19 = true;
    res_AndLogicOP_19 = (res_AndLogicOP_19 && (L_P1__GetParamMainc4(my_id) < 7u));
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! (Counter_GetValore(L_P1__GetMainc36(my_id)) == 12453u));
    res_AndLogicOP_19 = (res_AndLogicOP_19 && res_NotLogicOP_20);
    
    res_AndLogicOP_18 = (res_AndLogicOP_18 && res_AndLogicOP_19);
    res_AndLogicOP_18 = (res_AndLogicOP_18 && (L_P1__GetParamMainc2(my_id) < 7u));
    
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_AndLogicOP_18);
    
    if(res_OrLogicOP_13){
    bool res_OrLogicOP_21 = false;
    bool res_ImpliesLogicOp_22 = true;
    bool res_OrLogicOP_23 = false;
    bool res_NotLogicOP_24 = true;
    res_NotLogicOP_24 = (res_NotLogicOP_24 && ! (L_P1__GetInMainc1(my_id) == c270xx));
    res_OrLogicOP_23 = (res_OrLogicOP_23 || res_NotLogicOP_24);
    bool res_AndLogicOP_25 = true;
    res_AndLogicOP_25 = (res_AndLogicOP_25 && (Counter_GetValore(L_P1__GetMainc36(my_id)) == 144u));
    bool res_NotLogicOP_26 = true;
    bool res_NotLogicOP_27 = true;
    res_NotLogicOP_27 = (res_NotLogicOP_27 && ! (L_P1__GetInMainc1(my_id) == c270xx));
    res_NotLogicOP_26 = (res_NotLogicOP_26 && ! res_NotLogicOP_27);
    res_AndLogicOP_25 = (res_AndLogicOP_25 && res_NotLogicOP_26);
    
    res_OrLogicOP_23 = (res_OrLogicOP_23 || res_AndLogicOP_25);
    
    if(res_OrLogicOP_23){
    bool res_ImpliesLogicOp_28 = true;
    bool res_OrLogicOP_29 = false;
    bool res_OrLogicOP_30 = false;
    bool res_OrLogicOP_31 = false;
    bool res_NotLogicOP_32 = true;
    res_NotLogicOP_32 = (res_NotLogicOP_32 && ! (L_P1__Macro2(my_id,ac,true,ac,c270,c270) == rossogiallo));
    res_OrLogicOP_31 = (res_OrLogicOP_31 || res_NotLogicOP_32);
    bool res_AndLogicOP_33 = true;
    bool res_AndLogicOP_34 = true;
    bool res_NotLogicOP_35 = true;
    res_NotLogicOP_35 = (res_NotLogicOP_35 && ! (L_P1__GetParamMainc2(my_id) > 5u));
    res_AndLogicOP_34 = (res_AndLogicOP_34 && res_NotLogicOP_35);
    bool res_NotLogicOP_36 = true;
    res_NotLogicOP_36 = (res_NotLogicOP_36 && ! (L_P1__GetParamMainc2(my_id) == 7u));
    res_AndLogicOP_34 = (res_AndLogicOP_34 && res_NotLogicOP_36);
    
    res_AndLogicOP_33 = (res_AndLogicOP_33 && res_AndLogicOP_34);
    bool res_NotLogicOP_37 = true;
    res_NotLogicOP_37 = (res_NotLogicOP_37 && ! (L_P1__GetMainc27(my_id) == true));
    res_AndLogicOP_33 = (res_AndLogicOP_33 && res_NotLogicOP_37);
    
    res_OrLogicOP_31 = (res_OrLogicOP_31 || res_AndLogicOP_33);
    
    res_OrLogicOP_30 = (res_OrLogicOP_30 || res_OrLogicOP_31);
    res_OrLogicOP_30 = (res_OrLogicOP_30 || Timer_Disattivo(L_P1__GetMainc35(my_id)));
    
    res_OrLogicOP_29 = (res_OrLogicOP_29 || res_OrLogicOP_30);
    res_OrLogicOP_29 = (res_OrLogicOP_29 || (Counter_GetValore(L_P1__GetMainc37(my_id)) == 11u));
    
    if(res_OrLogicOP_29){
    bool res_OrLogicOP_38 = false;
    bool res_OrLogicOP_39 = false;
    bool res_OrLogicOP_40 = false;
    bool res_AndLogicOP_41 = true;
    bool res_NotLogicOP_42 = true;
    res_NotLogicOP_42 = (res_NotLogicOP_42 && ! Timer_Scaduto(L_P1__GetMainc35(my_id)));
    res_AndLogicOP_41 = (res_AndLogicOP_41 && res_NotLogicOP_42);
    bool res_NotLogicOP_43 = true;
    res_NotLogicOP_43 = (res_NotLogicOP_43 && ! (L_P1__GetParamMainc2(my_id) == 8u));
    res_AndLogicOP_41 = (res_AndLogicOP_41 && res_NotLogicOP_43);
    
    res_OrLogicOP_40 = (res_OrLogicOP_40 || res_AndLogicOP_41);
    bool res_NotLogicOP_44 = true;
    bool res_NotLogicOP_45 = true;
    res_NotLogicOP_45 = (res_NotLogicOP_45 && ! (argom17 == true));
    res_NotLogicOP_44 = (res_NotLogicOP_44 && ! res_NotLogicOP_45);
    res_OrLogicOP_40 = (res_OrLogicOP_40 || res_NotLogicOP_44);
    
    res_OrLogicOP_39 = (res_OrLogicOP_39 || res_OrLogicOP_40);
    res_OrLogicOP_39 = (res_OrLogicOP_39 || (L_P1__GetMainc27(my_id) == true));
    
    res_OrLogicOP_38 = (res_OrLogicOP_38 || res_OrLogicOP_39);
    bool res_NotLogicOP_46 = true;
    res_NotLogicOP_46 = (res_NotLogicOP_46 && ! Timer_Disattivo(L_P1__GetMainc35(my_id)));
    res_OrLogicOP_38 = (res_OrLogicOP_38 || res_NotLogicOP_46);
    
    res_ImpliesLogicOp_28 = (res_ImpliesLogicOp_28 && res_OrLogicOP_38);
    }
    res_ImpliesLogicOp_22 = (res_ImpliesLogicOp_22 && res_ImpliesLogicOp_28);
    }
    res_OrLogicOP_21 = (res_OrLogicOP_21 || res_ImpliesLogicOp_22);
    bool res_OrLogicOP_47 = false;
    bool res_AndLogicOP_48 = true;
    bool res_NotLogicOP_49 = true;
    res_NotLogicOP_49 = (res_NotLogicOP_49 && ! (L_P1__GetParamMainc2(my_id) > 6u));
    res_AndLogicOP_48 = (res_AndLogicOP_48 && res_NotLogicOP_49);
    bool res_NotLogicOP_50 = true;
    res_NotLogicOP_50 = (res_NotLogicOP_50 && ! (L_P1__GetMainc25(my_id) < 7u));
    res_AndLogicOP_48 = (res_AndLogicOP_48 && res_NotLogicOP_50);
    
    res_OrLogicOP_47 = (res_OrLogicOP_47 || res_AndLogicOP_48);
    res_OrLogicOP_47 = (res_OrLogicOP_47 || Timer_Attivo(L_P1__GetMainc35(my_id)));
    
    res_OrLogicOP_21 = (res_OrLogicOP_21 || res_OrLogicOP_47);
    
    res_ImpliesLogicOp_12 = (res_ImpliesLogicOp_12 && res_OrLogicOP_21);
    }
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_ImpliesLogicOp_12);
    bool res_OrLogicOP_51 = false;
    bool res_OrLogicOP_52 = false;
    bool res_OrLogicOP_53 = false;
    bool res_NotLogicOP_54 = true;
    bool res_NotLogicOP_55 = true;
    res_NotLogicOP_55 = (res_NotLogicOP_55 && ! (L_P1__GetMainc27(my_id) == false));
    res_NotLogicOP_54 = (res_NotLogicOP_54 && ! res_NotLogicOP_55);
    res_OrLogicOP_53 = (res_OrLogicOP_53 || res_NotLogicOP_54);
    bool res_NotLogicOP_56 = true;
    res_NotLogicOP_56 = (res_NotLogicOP_56 && ! Timer_Scaduto(L_P1__GetMainc35(my_id)));
    res_OrLogicOP_53 = (res_OrLogicOP_53 || res_NotLogicOP_56);
    
    res_OrLogicOP_52 = (res_OrLogicOP_52 || res_OrLogicOP_53);
    bool res_NotLogicOP_57 = true;
    res_NotLogicOP_57 = (res_NotLogicOP_57 && ! (L_P1__GetParamMainc3(my_id) == c270xx));
    res_OrLogicOP_52 = (res_OrLogicOP_52 || res_NotLogicOP_57);
    
    res_OrLogicOP_51 = (res_OrLogicOP_51 || res_OrLogicOP_52);
    bool res_NotLogicOP_58 = true;
    res_NotLogicOP_58 = (res_NotLogicOP_58 && ! (L_P1__GetInMainc1(my_id) == c270xx));
    res_OrLogicOP_51 = (res_OrLogicOP_51 || res_NotLogicOP_58);
    
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_OrLogicOP_51);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_OrLogicOP_11);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *47,51,*  *,*  il contatore MainClass_C1_contatore_Co8 non sia  uguale a  *53,* 12
    //   *104,* e  che  *34,*  il parametro MainClass_C1_parametro_P8 sia  uguale a  *53,* 7
    //   *104,* e  che  *34,*  il parametro MainClass_C1_parametro_P4 non sia  diverso da  *56,* 6
    bool res_AndLogicOP_59 = true;
    bool res_AndLogicOP_60 = true;
    bool res_NotLogicOP_61 = true;
    res_NotLogicOP_61 = (res_NotLogicOP_61 && ! (Counter_GetValore(L_P1__GetMainc37(my_id)) == 12u));
    res_AndLogicOP_60 = (res_AndLogicOP_60 && res_NotLogicOP_61);
    res_AndLogicOP_60 = (res_AndLogicOP_60 && (L_P1__GetParamMainc4(my_id) == 7u));
    
    res_AndLogicOP_59 = (res_AndLogicOP_59 && res_AndLogicOP_60);
    bool res_NotLogicOP_62 = true;
    bool res_NotLogicOP_63 = true;
    res_NotLogicOP_63 = (res_NotLogicOP_63 && ! (L_P1__GetParamMainc2(my_id) == 6u));
    res_NotLogicOP_62 = (res_NotLogicOP_62 && ! res_NotLogicOP_63);
    res_AndLogicOP_59 = (res_AndLogicOP_59 && res_NotLogicOP_62);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_AndLogicOP_59);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
    
    { commento: {62,} commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è scaduto, Almeno una delle seguenti { 
     commento: {61,} commento: {34,}  se il parametro MainClass_C1_parametro_P8 è  uguale a  commento: {53,} 5, Tutte le seguenti { 
     commento: {62,} commento: {37,}  se la variabile MainClass_C1_variabile_V4 è  diverso da  False  commento: {35,} e  se il controllo MainClass_C1_controllo_C7 non è  diverso da c270xx o  se l'argomento argomento_ave1 non  è  diverso da c270xx commento: {39,} , Almeno una delle seguenti { 
     commento: {63,} commento: {38,}  se il contatore MainClass_C1_contatore_Co8 è  diverso da  commento: {56,} 132 commento: {36,} o  se il timer MainClass_C1_timer_T5 è disattivo, Solo una delle seguenti { 
     commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI3 è attivo commento: {38,} o  se il contatore MainClass_C1_contatore_Co8 è  uguale a  commento: {53,} 12145 commento: {36,} e  se il timer MainClass_C1_timer_T5 è disattivo commento: {37,} o  se la variabile MainClass_C1_variabile_V4 è  uguale a  False  o  se l'argomento argomento_ave1 non  è  uguale a c270xx commento: {39,} , Verifica che   commento: {47,51,}  commento: {,}  il contatore MainClass_C1_contatore_Co5 non sia  maggiore di  commento: {54,} 12
     commento: {104,} e  che  commento: {38,}  il contatore MainClass_C1_contatore_Co8 non sia  diverso da  commento: {56,} 13
     commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P4 sia  minore di  commento: {55,} 2
     commento: {104,} e  che  commento: {38,}  il contatore MainClass_C1_contatore_Co8 sia  diverso da  commento: {56,} 123
    
    
     } Verifica che   commento: {47,}  commento: {34,}  il parametro MainClass_C1_parametro_P4 sia  maggiore di  commento: {54,} 7
    
    
     } Verifica che   commento: {47,48,50,51,}  commento: {,}  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
     commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V9 sia  maggiore di  commento: {54,} 5
     commento: {104,} o  che  commento: {37,}  la variabile MainClass_C1_variabile_V4 sia  uguale a  True 
     commento: {104,} o  che  commento: {,}  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  commento: {54,} 12
     commento: {104,} o  che  commento: {38,}  il contatore MainClass_C1_contatore_Co5 sia  diverso da  commento: {56,} 151
     commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P8 non sia  maggiore di  commento: {54,} 9
    
    
     } Verifica che   commento: {49,50,51,}  commento: {,}  la variabile MainClass_C1_variabile_V4 sia  diverso da  True 
     commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co8 non sia  diverso da  commento: {56,} 15302
     commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T5 sia scaduto
     commento: {104,} o  che  commento: {37,}  la variabile MainClass_C1_variabile_V9 sia  uguale a  commento: {53,} 8
    
    
     } Verifica che   commento: {47,48,50,51,}  commento: {,}  la variabile MainClass_C1_variabile_V3 non sia  diverso da  True 
     commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co5 non sia  uguale a  commento: {53,} 151
     commento: {104,} o  che  commento: {38,}  il contatore MainClass_C1_contatore_Co8 non sia  minore di  commento: {55,} 124
     commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P8 non sia  maggiore di  commento: {54,} 3
     commento: {104,} e  che  commento: {38,}  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  commento: {54,} 1153
     commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C7 non sia  diverso da c270xx
    
    
    }
*/
bool L_P1__Macro7(instance_id_t const my_id , C1_Enumerat4 argom20, bool argom21)
{
bool res_AndLogicOP_0 = true;
    
    //  *62,* *110,*  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è scaduto, Almeno una delle seguenti { 
    //   *61,* *34,*  se il parametro MainClass_C1_parametro_P8 è  uguale a  *53,* 5, Tutte le seguenti { 
    //   *62,* *37,*  se la variabile MainClass_C1_variabile_V4 è  diverso da  False  *35,* e  se il controllo MainClass_C1_controllo_C7 non è  diverso da c270xx o  se l'argomento argomento_ave1 non  è  diverso da c270xx *39,* , Almeno una delle seguenti { 
    //   *63,* *38,*  se il contatore MainClass_C1_contatore_Co8 è  diverso da  *56,* 132 *36,* o  se il timer MainClass_C1_timer_T5 è disattivo, Solo una delle seguenti { 
    //   *110,*  se il ripristino del timer  MainClass_C1_restoreTI_TI3 è attivo *38,* o  se il contatore MainClass_C1_contatore_Co8 è  uguale a  *53,* 12145 *36,* e  se il timer MainClass_C1_timer_T5 è disattivo *37,* o  se la variabile MainClass_C1_variabile_V4 è  uguale a  False  o  se l'argomento argomento_ave1 non  è  uguale a c270xx *39,* , Verifica che   *47,51,*  *,*  il contatore MainClass_C1_contatore_Co5 non sia  maggiore di  *54,* 12
    //   *104,* e  che  *38,*  il contatore MainClass_C1_contatore_Co8 non sia  diverso da  *56,* 13
    //   *104,* o  che  *34,*  il parametro MainClass_C1_parametro_P4 sia  minore di  *55,* 2
    //   *104,* e  che  *38,*  il contatore MainClass_C1_contatore_Co8 sia  diverso da  *56,* 123
    //   } Verifica che   *47,*  *34,*  il parametro MainClass_C1_parametro_P4 sia  maggiore di  *54,* 7
    //   } Verifica che   *47,48,50,51,*  *,*  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
    //   *104,* e  che  *,*  la variabile MainClass_C1_variabile_V9 sia  maggiore di  *54,* 5
    //   *104,* o  che  *37,*  la variabile MainClass_C1_variabile_V4 sia  uguale a  True 
    //   *104,* o  che  *,*  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  *54,* 12
    //   *104,* o  che  *38,*  il contatore MainClass_C1_contatore_Co5 sia  diverso da  *56,* 151
    //   *104,* o  che  *34,*  il parametro MainClass_C1_parametro_P8 non sia  maggiore di  *54,* 9
    //   } Verifica che   *49,50,51,*  *,*  la variabile MainClass_C1_variabile_V4 sia  diverso da  True 
    //   *104,* e  che  *,*  il contatore MainClass_C1_contatore_Co8 non sia  diverso da  *56,* 15302
    //   *104,* o  che  *,*  il timer MainClass_C1_timer_T5 sia scaduto
    //   *104,* o  che  *37,*  la variabile MainClass_C1_variabile_V9 sia  uguale a  *53,* 8
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! Timer_Scaduto(L_P1__GetMainc30(my_id)));
    if(res_NotLogicOP_2){
    bool res_OrLogicOP_3 = false;
    bool res_ImpliesLogicOp_4 = true;
    if((L_P1__GetParamMainc4(my_id) == 5u)){
    bool res_AndLogicOP_5 = true;
    bool res_ImpliesLogicOp_6 = true;
    bool res_OrLogicOP_7 = false;
    bool res_AndLogicOP_8 = true;
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetMainc27(my_id) == false));
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_9);
    bool res_NotLogicOP_10 = true;
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (L_P1__GetInMainc1(my_id) == c270xx));
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! res_NotLogicOP_11);
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_10);
    
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_AndLogicOP_8);
    bool res_NotLogicOP_12 = true;
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (argom20 == c270xx));
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! res_NotLogicOP_13);
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_NotLogicOP_12);
    
    if(res_OrLogicOP_7){
    bool res_OrLogicOP_14 = false;
    bool res_ImpliesLogicOp_15 = true;
    bool res_OrLogicOP_16 = false;
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! (Counter_GetValore(L_P1__GetMainc37(my_id)) == 132u));
    res_OrLogicOP_16 = (res_OrLogicOP_16 || res_NotLogicOP_17);
    res_OrLogicOP_16 = (res_OrLogicOP_16 || Timer_Disattivo(L_P1__GetMainc35(my_id)));
    
    if(res_OrLogicOP_16){
    bool res_ImpliesLogicOp_18 = true;
    bool res_OrLogicOP_19 = false;
    bool res_OrLogicOP_20 = false;
    bool res_OrLogicOP_21 = false;
    res_OrLogicOP_21 = (res_OrLogicOP_21 || Timer_Attivo(L_P1__GetMainc34(my_id)));
    bool res_AndLogicOP_22 = true;
    res_AndLogicOP_22 = (res_AndLogicOP_22 && (Counter_GetValore(L_P1__GetMainc37(my_id)) == 12145u));
    res_AndLogicOP_22 = (res_AndLogicOP_22 && Timer_Disattivo(L_P1__GetMainc35(my_id)));
    
    res_OrLogicOP_21 = (res_OrLogicOP_21 || res_AndLogicOP_22);
    
    res_OrLogicOP_20 = (res_OrLogicOP_20 || res_OrLogicOP_21);
    res_OrLogicOP_20 = (res_OrLogicOP_20 || (L_P1__GetMainc27(my_id) == false));
    
    res_OrLogicOP_19 = (res_OrLogicOP_19 || res_OrLogicOP_20);
    bool res_NotLogicOP_23 = true;
    res_NotLogicOP_23 = (res_NotLogicOP_23 && ! (argom20 == c270xx));
    res_OrLogicOP_19 = (res_OrLogicOP_19 || res_NotLogicOP_23);
    
    if(res_OrLogicOP_19){
    bool res_OrLogicOP_24 = false;
    bool res_AndLogicOP_25 = true;
    bool res_NotLogicOP_26 = true;
    res_NotLogicOP_26 = (res_NotLogicOP_26 && ! (Counter_GetValore(L_P1__GetMainc36(my_id)) > 12u));
    res_AndLogicOP_25 = (res_AndLogicOP_25 && res_NotLogicOP_26);
    bool res_NotLogicOP_27 = true;
    bool res_NotLogicOP_28 = true;
    res_NotLogicOP_28 = (res_NotLogicOP_28 && ! (Counter_GetValore(L_P1__GetMainc37(my_id)) == 13u));
    res_NotLogicOP_27 = (res_NotLogicOP_27 && ! res_NotLogicOP_28);
    res_AndLogicOP_25 = (res_AndLogicOP_25 && res_NotLogicOP_27);
    
    res_OrLogicOP_24 = (res_OrLogicOP_24 || res_AndLogicOP_25);
    bool res_AndLogicOP_29 = true;
    res_AndLogicOP_29 = (res_AndLogicOP_29 && (L_P1__GetParamMainc2(my_id) < 2u));
    bool res_NotLogicOP_30 = true;
    res_NotLogicOP_30 = (res_NotLogicOP_30 && ! (Counter_GetValore(L_P1__GetMainc37(my_id)) == 123u));
    res_AndLogicOP_29 = (res_AndLogicOP_29 && res_NotLogicOP_30);
    
    res_OrLogicOP_24 = (res_OrLogicOP_24 || res_AndLogicOP_29);
    
    res_ImpliesLogicOp_18 = (res_ImpliesLogicOp_18 && res_OrLogicOP_24);
    }
    res_ImpliesLogicOp_15 = (res_ImpliesLogicOp_15 && res_ImpliesLogicOp_18);
    }
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_ImpliesLogicOp_15);
    res_OrLogicOP_14 = (res_OrLogicOP_14 || (L_P1__GetParamMainc2(my_id) > 7u));
    
    res_ImpliesLogicOp_6 = (res_ImpliesLogicOp_6 && res_OrLogicOP_14);
    }
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_ImpliesLogicOp_6);
    bool res_OrLogicOP_31 = false;
    bool res_OrLogicOP_32 = false;
    bool res_OrLogicOP_33 = false;
    bool res_OrLogicOP_34 = false;
    bool res_AndLogicOP_35 = true;
    bool res_NotLogicOP_36 = true;
    res_NotLogicOP_36 = (res_NotLogicOP_36 && ! (L_P1__GetInMainc1(my_id) == c270xx));
    res_AndLogicOP_35 = (res_AndLogicOP_35 && res_NotLogicOP_36);
    res_AndLogicOP_35 = (res_AndLogicOP_35 && (L_P1__GetMainc28(my_id) > 5u));
    
    res_OrLogicOP_34 = (res_OrLogicOP_34 || res_AndLogicOP_35);
    res_OrLogicOP_34 = (res_OrLogicOP_34 || (L_P1__GetMainc27(my_id) == true));
    
    res_OrLogicOP_33 = (res_OrLogicOP_33 || res_OrLogicOP_34);
    res_OrLogicOP_33 = (res_OrLogicOP_33 || (Counter_GetValore(L_P1__GetMainc37(my_id)) > 12u));
    
    res_OrLogicOP_32 = (res_OrLogicOP_32 || res_OrLogicOP_33);
    bool res_NotLogicOP_37 = true;
    res_NotLogicOP_37 = (res_NotLogicOP_37 && ! (Counter_GetValore(L_P1__GetMainc36(my_id)) == 151u));
    res_OrLogicOP_32 = (res_OrLogicOP_32 || res_NotLogicOP_37);
    
    res_OrLogicOP_31 = (res_OrLogicOP_31 || res_OrLogicOP_32);
    bool res_NotLogicOP_38 = true;
    res_NotLogicOP_38 = (res_NotLogicOP_38 && ! (L_P1__GetParamMainc4(my_id) > 9u));
    res_OrLogicOP_31 = (res_OrLogicOP_31 || res_NotLogicOP_38);
    
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_OrLogicOP_31);
    
    res_ImpliesLogicOp_4 = (res_ImpliesLogicOp_4 && res_AndLogicOP_5);
    }
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_ImpliesLogicOp_4);
    bool res_OrLogicOP_39 = false;
    bool res_OrLogicOP_40 = false;
    bool res_AndLogicOP_41 = true;
    bool res_NotLogicOP_42 = true;
    res_NotLogicOP_42 = (res_NotLogicOP_42 && ! (L_P1__GetMainc27(my_id) == true));
    res_AndLogicOP_41 = (res_AndLogicOP_41 && res_NotLogicOP_42);
    bool res_NotLogicOP_43 = true;
    bool res_NotLogicOP_44 = true;
    res_NotLogicOP_44 = (res_NotLogicOP_44 && ! (Counter_GetValore(L_P1__GetMainc37(my_id)) == 15302u));
    res_NotLogicOP_43 = (res_NotLogicOP_43 && ! res_NotLogicOP_44);
    res_AndLogicOP_41 = (res_AndLogicOP_41 && res_NotLogicOP_43);
    
    res_OrLogicOP_40 = (res_OrLogicOP_40 || res_AndLogicOP_41);
    res_OrLogicOP_40 = (res_OrLogicOP_40 || Timer_Scaduto(L_P1__GetMainc35(my_id)));
    
    res_OrLogicOP_39 = (res_OrLogicOP_39 || res_OrLogicOP_40);
    res_OrLogicOP_39 = (res_OrLogicOP_39 || (L_P1__GetMainc28(my_id) == 8u));
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_OrLogicOP_39);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_OrLogicOP_3);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *47,48,50,51,*  *,*  la variabile MainClass_C1_variabile_V3 non sia  diverso da  True 
    //   *104,* e  che  *,*  il contatore MainClass_C1_contatore_Co5 non sia  uguale a  *53,* 151
    //   *104,* o  che  *38,*  il contatore MainClass_C1_contatore_Co8 non sia  minore di  *55,* 124
    //   *104,* e  che  *34,*  il parametro MainClass_C1_parametro_P8 non sia  maggiore di  *54,* 3
    //   *104,* e  che  *38,*  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  *54,* 1153
    //   *104,* o  che  *,*  il controllo MainClass_C1_controllo_C7 non sia  diverso da c270xx
    bool res_OrLogicOP_45 = false;
    bool res_OrLogicOP_46 = false;
    bool res_AndLogicOP_47 = true;
    bool res_NotLogicOP_48 = true;
    bool res_NotLogicOP_49 = true;
    res_NotLogicOP_49 = (res_NotLogicOP_49 && ! (L_P1__GetMainc26(my_id) == true));
    res_NotLogicOP_48 = (res_NotLogicOP_48 && ! res_NotLogicOP_49);
    res_AndLogicOP_47 = (res_AndLogicOP_47 && res_NotLogicOP_48);
    bool res_NotLogicOP_50 = true;
    res_NotLogicOP_50 = (res_NotLogicOP_50 && ! (Counter_GetValore(L_P1__GetMainc36(my_id)) == 151u));
    res_AndLogicOP_47 = (res_AndLogicOP_47 && res_NotLogicOP_50);
    
    res_OrLogicOP_46 = (res_OrLogicOP_46 || res_AndLogicOP_47);
    bool res_AndLogicOP_51 = true;
    bool res_AndLogicOP_52 = true;
    bool res_NotLogicOP_53 = true;
    res_NotLogicOP_53 = (res_NotLogicOP_53 && ! (Counter_GetValore(L_P1__GetMainc37(my_id)) < 124u));
    res_AndLogicOP_52 = (res_AndLogicOP_52 && res_NotLogicOP_53);
    bool res_NotLogicOP_54 = true;
    res_NotLogicOP_54 = (res_NotLogicOP_54 && ! (L_P1__GetParamMainc4(my_id) > 3u));
    res_AndLogicOP_52 = (res_AndLogicOP_52 && res_NotLogicOP_54);
    
    res_AndLogicOP_51 = (res_AndLogicOP_51 && res_AndLogicOP_52);
    res_AndLogicOP_51 = (res_AndLogicOP_51 && (Counter_GetValore(L_P1__GetMainc37(my_id)) > 1153u));
    
    res_OrLogicOP_46 = (res_OrLogicOP_46 || res_AndLogicOP_51);
    
    res_OrLogicOP_45 = (res_OrLogicOP_45 || res_OrLogicOP_46);
    bool res_NotLogicOP_55 = true;
    bool res_NotLogicOP_56 = true;
    res_NotLogicOP_56 = (res_NotLogicOP_56 && ! (L_P1__GetInMainc1(my_id) == c270xx));
    res_NotLogicOP_55 = (res_NotLogicOP_55 && ! res_NotLogicOP_56);
    res_OrLogicOP_45 = (res_OrLogicOP_45 || res_NotLogicOP_55);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_45);
    
    
    
    return res_AndLogicOP_0;
}


// Macro valorizzate

/*
    CNL corrispondente:
    
    { commento: {[}
     commento: {46,} assegna alla macro il valore RossoGialloaVerdea commento: {],}
    }
*/
C1_Enumerat1 L_P1__Macro2(instance_id_t const my_id , C1_Enumerat2 argom, bool argom1, C1_Enumerat2 argom2, C1_Enumerat1 argom3, C1_Enumerat1 argom4)
{
return rossogiallo;
}

/*
    CNL corrispondente:
    
    { commento: {[}
     commento: {46,} assegna alla macro il valore  False  commento: {],}
    }
*/
bool L_P1__Macro3(instance_id_t const my_id , C1_Enumerat3 argom5, bool argom6, C1_Enumerat3 argom7, C1_Enumerat4 argom8, C1_Enumerat4 argom9, C1_Enumerat2 argom10)
{
return false;
}



