// Codice del modello 'TestCase12', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#include "Logica/ClasseMainClass_C1.h"
#include "Logica/ClasseSubClass_C2.h"
#include "Logica/ClasseSubClass_C3.h"
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
    L_P1__SetMainc20(my_id, avvio);
    L_P1__SetMainc22(my_id, 0);
    L_P1__SetMainc24(my_id, false);
    L_P1__SetMainc25(my_id, false);
    L_P1__SetMainc26(my_id, false);
    L_P1__SetMainc27(my_id, false);
    L_P1__SetMainc28(my_id, avvio);
    L_P1__SetMainc29(my_id, avvio);
    L_P1__SetMainc30(my_id, c180);
    L_P1__SetMainc31(my_id, c180);
    L_P1__SetMainc32(my_id, false);
    L_P1__SetMainc33(my_id, false);
    L_P1__SetMainc34(my_id, c180);
    L_P1__SetMainc35(my_id, 0);
    L_P1__SetMainc36(my_id, false);
    L_P1__SetStato1(my_id, C1_St_Stato);
    // init controlli precedenti
    L_P1__SetMainc11(my_id, true);
    L_P1__SetMainc13(my_id, true);
    L_P1__SetMainc15(my_id, rossogiallo1);
    L_P1__SetMainc17(my_id, true);
    L_P1__SetMainc19(my_id, true);
    // init Timer e Counter
    Timer_AggmInit(L_P1__GetMainc37(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc37_ID);
    Timer_Init(L_P1__GetMainc37(my_id), 34000);
    Timer_AggmInit(L_P1__GetMainc38(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc38_ID);
    Timer_Init(L_P1__GetMainc38(my_id), 34000);
    Timer_AggmInit(L_P1__GetMainc39(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc39_ID);
    Timer_Init(L_P1__GetMainc39(my_id), 512000);
    Timer_AggmInit(L_P1__GetMainc40(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc40_ID);
    Timer_Init(L_P1__GetMainc40(my_id), 45000);
    Timer_AggmInit(L_P1__GetMainc41(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc41_ID);
    Timer_Init(L_P1__GetMainc41(my_id), 130000);
    Timer_AggmInit(L_P1__GetMainc42(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc42_ID);
    Timer_Init(L_P1__GetMainc42(my_id), 5000);
    Counter_AggmInit(L_P1__GetMainc43(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc43_ID);
    Counter_Init(L_P1__GetMainc43(my_id));
    Counter_AggmInit(L_P1__GetMainc44(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc44_ID);
    Counter_Init(L_P1__GetMainc44(my_id));
    Counter_AggmInit(L_P1__GetMainc45(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc45_ID);
    Counter_Init(L_P1__GetMainc45(my_id));
    Counter_AggmInit(L_P1__GetMainc46(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc46_ID);
    Counter_Init(L_P1__GetMainc46(my_id));
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
    L_P1__SetMainc21(my_id, L_P1__GetMainc20(my_id));
    L_P1__SetMainc23(my_id, L_P1__GetMainc22(my_id));
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
    Timer_Exec(L_P1__GetMainc37(my_id));
    Timer_Exec(L_P1__GetMainc38(my_id));
    Timer_Exec(L_P1__GetMainc39(my_id));
    Timer_Exec(L_P1__GetMainc40(my_id));
    Timer_Exec(L_P1__GetMainc41(my_id));
    Timer_Exec(L_P1__GetMainc42(my_id));
}

void L_P1_C1_GSetSafe(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C1(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C1(proc_id);
    L_P1__SetOutMainc(my_id, false);
}

void L_P1_C1_GUpdatePrev(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C1(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C1(proc_id);
    L_P1__SetMainc11(my_id, L_P1__GetInMainc10(my_id));
    L_P1__SetMainc13(my_id, L_P1__GetInMainc12(my_id));
    L_P1__SetMainc15(my_id, L_P1__GetInMainc14(my_id));
    L_P1__SetMainc17(my_id, L_P1__GetInMainc16(my_id));
    L_P1__SetMainc19(my_id, L_P1__GetInMainc18(my_id));
    L_P1__SetMainc21(my_id, L_P1__GetMainc20(my_id));
    L_P1__SetMainc23(my_id, L_P1__GetMainc22(my_id));
}

// ********** Definizione macro **********

// Macro di effetto

/*
    CNL corrispondente:
    
    {  se il ripristino dello stato  è  diverso da  commento: {56,}  state1  commento: {107,},  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V3 il valore RossoGialloVerde commento: {67,}
    
     ,altrimenti  commento: {68,}Attiva il timer MainClass_C1_timer_T4
    
    
      se il controllo ConsDef è uguale a FALSE  commento: {37,} e  se la variabile MainClass_C1_variabile_V10 non è  uguale a  True  commento: {34,} o  se il parametro MainClass_C1_parametro_P9 è  uguale a  False ,  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V10 il valore  False commento: {67,}
    
       
     commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è attivo o  se l'argomento argomento_af9 non  è  diverso da RossoGialloaVerdea commento: {39,} , commento: {69,}Disattiva il timer MainClass_C1_timer_T3
    
       
    
    }
*/
void L_P1__Macro(instance_id_t const my_id , bool argom, C1_Enumerat1 argom1, C1_Enumerat2 argom2)
{
//  se il ripristino dello stato  è  diverso da  *56,*  state1  *107,*,  *67,* Assegna alla variabile MainClass_C1_variabile_V3 il valore RossoGialloVerde *67,*
    // ,altrimenti  *68,*Attiva il timer MainClass_C1_timer_T4
    bool res_NotLogicOP_0 = true;
    res_NotLogicOP_0 = (res_NotLogicOP_0 && ! (L_P1__GetStato1(my_id) == C1_St_state));
    if(res_NotLogicOP_0){
    
    L_P1__SetMainc34(my_id,rossogiallo1);
    }else{
    
    Timer_Attiva(L_P1__GetMainc41(my_id));
    }
    //  se il controllo ConsDef è uguale a FALSE  *37,* e  se la variabile MainClass_C1_variabile_V10 non è  uguale a  True  *34,* o  se il parametro MainClass_C1_parametro_P9 è  uguale a  False ,  *67,* Assegna alla variabile MainClass_C1_variabile_V10 il valore  False
    bool res_OrLogicOP_1 = false;
    bool res_AndLogicOP_2 = true;
    res_AndLogicOP_2 = (res_AndLogicOP_2 && (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__GetMainc32(my_id) == true));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_3);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_2);
    res_OrLogicOP_1 = (res_OrLogicOP_1 || (L_P1__GetParamMainc9(my_id) == false));
    
    if(res_OrLogicOP_1){
    
    L_P1__SetMainc32(my_id,false);
    }
    //  *67,*
    //   
    // *110,*  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è attivo o  se l'argomento argomento_af9 non  è  diverso da RossoGialloaVerdea *39,* , *69,*Disattiva il timer MainClass_C1_timer_T3
    bool res_OrLogicOP_4 = false;
    res_OrLogicOP_4 = (res_OrLogicOP_4 || Timer_Attivo(L_P1__GetMainc38(my_id)));
    bool res_NotLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (argom2 == rossogiallo));
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! res_NotLogicOP_6);
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_NotLogicOP_5);
    
    if(res_OrLogicOP_4){
    
    Timer_Disattiva(L_P1__GetMainc40(my_id));
    }
}

/*
    CNL corrispondente:
    
    { commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV2 è  uguale a  True  commento: {37,} e  se la variabile MainClass_C1_variabile_V10 non è  uguale a  True  commento: {36,} e  se il timer MainClass_C1_timer_T3 non è attivo commento: {36,} e  se il timer MainClass_C1_timer_T6 non è scaduto o  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro MainClass_C1_parametro_P3 non è  maggiore di  commento: {54,} 4, commento: {69,}Disattiva il timer MainClass_C1_timer_T4
    
     ,altrimenti   Applica gli effetti
           della macro MainClass_C1_macroef_M3( con argomento_af5   uguale a True ,argomento_af9   uguale a Rosso ,argomento_af6   uguale a Giallox ) commento: {73,}
    
    
     commento: {38,}  se il contatore MainClass_C1_contatore_Co5 non è  maggiore di  commento: {54,} 15 commento: {35,} o  se il controllo MainClass_C1_controllo_C9 non è  diverso da RossoGialloaVerdea commento: {37,} o  se la variabile MainClass_C1_variabile_V6 è  uguale a  False  commento: {35,} e  se il controllo MainClass_C1_controllo_C9 è  diverso da RossoGialloaVerdea commento: {34,} o  se il parametro MainClass_C1_parametro_P9 non è  diverso da  False  commento: {36,} o  se il timer MainClass_C1_timer_T3 non è attivo, commento: {66,} Assegna al comando MainClass_C1_comando_C9 il valore  True 
    
       
     commento: {35,}  se il controllo MainClass_C1_controllo_C9 è  diverso da RossoGialloaVerdea commento: {36,} o  se il timer MainClass_C1_timer_T3 non è attivo commento: {34,} e  se il parametro MainClass_C1_parametro_P9 non è  uguale a  True  commento: {38,} o  se il contatore MainClass_C1_contatore_Co8 è  diverso da  commento: {56,} 13123 commento: {37,} e  se la variabile MainClass_C1_variabile_V3 è  diverso da RossoGialloVerde, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V2 il valore  False 
    
     ,altrimenti  commento: {71,}Decrementa il contatore MainClass_C1_contatore_Co8
    
    
      se il ripristino dello stato  è  uguale a  commento: {53,}  state1  commento: {107,} commento: {38,} o  se il contatore MainClass_C1_contatore_Co9 non è  minore di  commento: {55,} 14, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V10 il valore  True 
    
     ,altrimenti  commento: {66,} Assegna al comando MainClass_C1_comando_C9 il valore  True 
    
    
     commento: {34,}  se il parametro MainClass_C1_parametro_P3 non è  uguale a  commento: {53,} 9 commento: {38,} o  se il contatore MainClass_C1_contatore_Co3 non è  diverso da  commento: {56,} 1404 commento: {36,} o  se il timer MainClass_C1_timer_T4 non è scaduto o  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} e  se il contatore MainClass_C1_contatore_Co8 non è  maggiore di  commento: {54,} 1151, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V10 il valore  True 
    
     ,altrimenti  commento: {72,}Azzera il contatore MainClass_C1_contatore_Co8
    
    
    
    }
*/
void L_P1__Macro1(instance_id_t const my_id )
{
//  *109,*  se il ripristino della variabile  MainClass_C1_restoreva_RV2 è  uguale a  True  *37,* e  se la variabile MainClass_C1_variabile_V10 non è  uguale a  True  *36,* e  se il timer MainClass_C1_timer_T3 non è attivo *36,* e  se il timer MainClass_C1_timer_T6 non è scaduto o  se il controllo ConsDef  è  uguale a FALSE  *34,* e  se il parametro MainClass_C1_parametro_P3 non è  maggiore di  *54,* 4, *69,*Disattiva il timer MainClass_C1_timer_T4
    // ,altrimenti   Applica gli effetti
    //       della macro MainClass_C1_macroef_M3( con argomento_af5   uguale a True ,argomento_af9   uguale a Rosso ,argomento_af6   uguale a Giallox )
    bool res_OrLogicOP_0 = false;
    bool res_AndLogicOP_1 = true;
    bool res_AndLogicOP_2 = true;
    bool res_AndLogicOP_3 = true;
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (L_P1__GetMainc27(my_id) == true));
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetMainc32(my_id) == true));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_4);
    
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_AndLogicOP_3);
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! Timer_Attivo(L_P1__GetMainc40(my_id)));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_5);
    
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_AndLogicOP_2);
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! Timer_Scaduto(L_P1__GetMainc42(my_id)));
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_6);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_1);
    bool res_AndLogicOP_7 = true;
    res_AndLogicOP_7 = (res_AndLogicOP_7 && (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetParamMainc7(my_id) > 4u));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_8);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_7);
    
    if(res_OrLogicOP_0){
    
    Timer_Disattiva(L_P1__GetMainc41(my_id));
    }else{
    
    L_P1__Macro(my_id,true,giallox,rosso);
    }
    //  *73,*
    // *38,*  se il contatore MainClass_C1_contatore_Co5 non è  maggiore di  *54,* 15 *35,* o  se il controllo MainClass_C1_controllo_C9 non è  diverso da RossoGialloaVerdea *37,* o  se la variabile MainClass_C1_variabile_V6 è  uguale a  False  *35,* e  se il controllo MainClass_C1_controllo_C9 è  diverso da RossoGialloaVerdea *34,* o  se il parametro MainClass_C1_parametro_P9 non è  diverso da  False  *36,* o  se il timer MainClass_C1_timer_T3 non è attivo, *66,* Assegna al comando MainClass_C1_comando_C9 il valore  True
    bool res_OrLogicOP_9 = false;
    bool res_OrLogicOP_10 = false;
    bool res_OrLogicOP_11 = false;
    bool res_OrLogicOP_12 = false;
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (Counter_GetValore(L_P1__GetMainc44(my_id)) > 15u));
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_NotLogicOP_13);
    bool res_NotLogicOP_14 = true;
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (L_P1__GetInMainc5(my_id) == rossogiallo));
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! res_NotLogicOP_15);
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_NotLogicOP_14);
    
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_OrLogicOP_12);
    bool res_AndLogicOP_16 = true;
    res_AndLogicOP_16 = (res_AndLogicOP_16 && (L_P1__GetMainc36(my_id) == false));
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! (L_P1__GetInMainc5(my_id) == rossogiallo));
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_NotLogicOP_17);
    
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_AndLogicOP_16);
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_OrLogicOP_11);
    bool res_NotLogicOP_18 = true;
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (L_P1__GetParamMainc9(my_id) == false));
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! res_NotLogicOP_19);
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_NotLogicOP_18);
    
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_OrLogicOP_10);
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! Timer_Attivo(L_P1__GetMainc40(my_id)));
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_NotLogicOP_20);
    
    if(res_OrLogicOP_9){
    
    L_P1__SetOutMainc(my_id,true);
    }
    //  *35,*  se il controllo MainClass_C1_controllo_C9 è  diverso da RossoGialloaVerdea *36,* o  se il timer MainClass_C1_timer_T3 non è attivo *34,* e  se il parametro MainClass_C1_parametro_P9 non è  uguale a  True  *38,* o  se il contatore MainClass_C1_contatore_Co8 è  diverso da  *56,* 13123 *37,* e  se la variabile MainClass_C1_variabile_V3 è  diverso da RossoGialloVerde, *67,* Assegna alla variabile MainClass_C1_variabile_V2 il valore  False 
    // ,altrimenti  *71,*Decrementa il contatore MainClass_C1_contatore_Co8
    bool res_OrLogicOP_21 = false;
    bool res_OrLogicOP_22 = false;
    bool res_NotLogicOP_23 = true;
    res_NotLogicOP_23 = (res_NotLogicOP_23 && ! (L_P1__GetInMainc5(my_id) == rossogiallo));
    res_OrLogicOP_22 = (res_OrLogicOP_22 || res_NotLogicOP_23);
    bool res_AndLogicOP_24 = true;
    bool res_NotLogicOP_25 = true;
    res_NotLogicOP_25 = (res_NotLogicOP_25 && ! Timer_Attivo(L_P1__GetMainc40(my_id)));
    res_AndLogicOP_24 = (res_AndLogicOP_24 && res_NotLogicOP_25);
    bool res_NotLogicOP_26 = true;
    res_NotLogicOP_26 = (res_NotLogicOP_26 && ! (L_P1__GetParamMainc9(my_id) == true));
    res_AndLogicOP_24 = (res_AndLogicOP_24 && res_NotLogicOP_26);
    
    res_OrLogicOP_22 = (res_OrLogicOP_22 || res_AndLogicOP_24);
    
    res_OrLogicOP_21 = (res_OrLogicOP_21 || res_OrLogicOP_22);
    bool res_AndLogicOP_27 = true;
    bool res_NotLogicOP_28 = true;
    res_NotLogicOP_28 = (res_NotLogicOP_28 && ! (Counter_GetValore(L_P1__GetMainc45(my_id)) == 13123u));
    res_AndLogicOP_27 = (res_AndLogicOP_27 && res_NotLogicOP_28);
    bool res_NotLogicOP_29 = true;
    res_NotLogicOP_29 = (res_NotLogicOP_29 && ! (L_P1__GetMainc34(my_id) == rossogiallo1));
    res_AndLogicOP_27 = (res_AndLogicOP_27 && res_NotLogicOP_29);
    
    res_OrLogicOP_21 = (res_OrLogicOP_21 || res_AndLogicOP_27);
    
    if(res_OrLogicOP_21){
    
    L_P1__SetMainc33(my_id,false);
    }else{
    
    Counter_Decr(L_P1__GetMainc45(my_id));
    }
    //  se il ripristino dello stato  è  uguale a  *53,*  state1  *107,* *38,* o  se il contatore MainClass_C1_contatore_Co9 non è  minore di  *55,* 14, *67,* Assegna alla variabile MainClass_C1_variabile_V10 il valore  True 
    // ,altrimenti  *66,* Assegna al comando MainClass_C1_comando_C9 il valore  True
    bool res_OrLogicOP_30 = false;
    res_OrLogicOP_30 = (res_OrLogicOP_30 || (L_P1__GetStato1(my_id) == C1_St_state));
    bool res_NotLogicOP_31 = true;
    res_NotLogicOP_31 = (res_NotLogicOP_31 && ! (Counter_GetValore(L_P1__GetMainc46(my_id)) < 14u));
    res_OrLogicOP_30 = (res_OrLogicOP_30 || res_NotLogicOP_31);
    
    if(res_OrLogicOP_30){
    
    L_P1__SetMainc32(my_id,true);
    }else{
    
    L_P1__SetOutMainc(my_id,true);
    }
    //  *34,*  se il parametro MainClass_C1_parametro_P3 non è  uguale a  *53,* 9 *38,* o  se il contatore MainClass_C1_contatore_Co3 non è  diverso da  *56,* 1404 *36,* o  se il timer MainClass_C1_timer_T4 non è scaduto o  se il controllo ConsDef  è  uguale a FALSE  *38,* e  se il contatore MainClass_C1_contatore_Co8 non è  maggiore di  *54,* 1151, *67,* Assegna alla variabile MainClass_C1_variabile_V10 il valore  True 
    // ,altrimenti  *72,*Azzera il contatore MainClass_C1_contatore_Co8
    bool res_OrLogicOP_32 = false;
    bool res_OrLogicOP_33 = false;
    bool res_OrLogicOP_34 = false;
    bool res_NotLogicOP_35 = true;
    res_NotLogicOP_35 = (res_NotLogicOP_35 && ! (L_P1__GetParamMainc7(my_id) == 9u));
    res_OrLogicOP_34 = (res_OrLogicOP_34 || res_NotLogicOP_35);
    bool res_NotLogicOP_36 = true;
    bool res_NotLogicOP_37 = true;
    res_NotLogicOP_37 = (res_NotLogicOP_37 && ! (Counter_GetValore(L_P1__GetMainc43(my_id)) == 1404u));
    res_NotLogicOP_36 = (res_NotLogicOP_36 && ! res_NotLogicOP_37);
    res_OrLogicOP_34 = (res_OrLogicOP_34 || res_NotLogicOP_36);
    
    res_OrLogicOP_33 = (res_OrLogicOP_33 || res_OrLogicOP_34);
    bool res_NotLogicOP_38 = true;
    res_NotLogicOP_38 = (res_NotLogicOP_38 && ! Timer_Scaduto(L_P1__GetMainc41(my_id)));
    res_OrLogicOP_33 = (res_OrLogicOP_33 || res_NotLogicOP_38);
    
    res_OrLogicOP_32 = (res_OrLogicOP_32 || res_OrLogicOP_33);
    bool res_AndLogicOP_39 = true;
    res_AndLogicOP_39 = (res_AndLogicOP_39 && (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_40 = true;
    res_NotLogicOP_40 = (res_NotLogicOP_40 && ! (Counter_GetValore(L_P1__GetMainc45(my_id)) > 1151u));
    res_AndLogicOP_39 = (res_AndLogicOP_39 && res_NotLogicOP_40);
    
    res_OrLogicOP_32 = (res_OrLogicOP_32 || res_AndLogicOP_39);
    
    if(res_OrLogicOP_32){
    
    L_P1__SetMainc32(my_id,true);
    }else{
    
    Counter_Res(L_P1__GetMainc45(my_id));
    }
}

/*
    CNL corrispondente:
     
    {  se il ripristino dello stato  non è  uguale a  commento: {53,}  state1  commento: {107,},  Applica gli effetti
           della macro MainClass_C1_macroef_M6  commento: {73,}
    
     ,altrimenti  commento: {72,}Azzera il contatore MainClass_C1_contatore_Co9
    
    
     commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  uguale a  False  commento: {34,} o  se il parametro MainClass_C1_parametro_P3 è  uguale a  commento: {53,} 8 commento: {37,} o  se la variabile MainClass_C1_variabile_V10 non è  diverso da  False  commento: {35,} e  se il controllo MainClass_C1_controllo_C8 non è  diverso da  False , commento: {66,} Assegna al comando MainClass_C1_comando_C9 il valore  False 
    
     ,altrimenti  commento: {69,}Disattiva il timer MainClass_C1_timer_T4
    
    
     commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  uguale a  True , commento: {70,}Incrementa il contatore MainClass_C1_contatore_Co5
    
     ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V5 il valore 9
    
    
      se il controllo ConsDef  è  uguale a FALSE  commento: {36,} o  se il timer MainClass_C1_timer_T4 è attivo commento: {38,} o  se il contatore MainClass_C1_contatore_Co8 non è  minore di  commento: {55,} 142 commento: {38,} o  se il contatore MainClass_C1_contatore_Co3 non è  maggiore di  commento: {54,} 1430, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V10 il valore  True 
    
     ,altrimenti   Applica gli effetti
           della macro MainClass_C1_macroef_M3( con argomento_af5   uguale a True ,argomento_af9   uguale a Rosso ,argomento_af6   uguale a Giallox ) commento: {73,}
    
    
      se il controllo ConsDef  è  uguale a FALSE  commento: {37,} e  se la variabile MainClass_C1_variabile_V2 non è  uguale a  False  commento: {35,} e  se il controllo MainClass_C1_controllo_C7 non è  uguale a  True  commento: {34,} e  se il parametro MainClass_C1_parametro_P9 è  diverso da  False  commento: {34,} e  se il parametro MainClass_C1_parametro_P9 è  uguale a  True , commento: {67,} Assegna alla variabile MainClass_C1_variabile_V3 il valore RossoGialloVerde
    
     ,altrimenti   Applica gli effetti
           della macro MainClass_C1_macroef_M9  commento: {73,}
    
    
    
    }
*/
void L_P1__Macro2(instance_id_t const my_id )
{
//  se il ripristino dello stato  non è  uguale a  *53,*  state1  *107,*,  Applica gli effetti
    //       della macro MainClass_C1_macroef_M6  *73,*
    // ,altrimenti  *72,*Azzera il contatore MainClass_C1_contatore_Co9
    bool res_NotLogicOP_0 = true;
    res_NotLogicOP_0 = (res_NotLogicOP_0 && ! (L_P1__GetStato1(my_id) == C1_St_state));
    if(res_NotLogicOP_0){
    
    L_P1__Macro1(my_id);
    }else{
    
    Counter_Res(L_P1__GetMainc46(my_id));
    }
    //  *109,*  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  uguale a  False  *34,* o  se il parametro MainClass_C1_parametro_P3 è  uguale a  *53,* 8 *37,* o  se la variabile MainClass_C1_variabile_V10 non è  diverso da  False  *35,* e  se il controllo MainClass_C1_controllo_C8 non è  diverso da  False , *66,* Assegna al comando MainClass_C1_comando_C9 il valore  False 
    // ,altrimenti  *69,*Disattiva il timer MainClass_C1_timer_T4
    bool res_OrLogicOP_1 = false;
    bool res_OrLogicOP_2 = false;
    res_OrLogicOP_2 = (res_OrLogicOP_2 || (L_P1__GetMainc25(my_id) == false));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || (L_P1__GetParamMainc7(my_id) == 8u));
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_OrLogicOP_2);
    bool res_AndLogicOP_3 = true;
    bool res_NotLogicOP_4 = true;
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetMainc32(my_id) == false));
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! res_NotLogicOP_5);
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_4);
    bool res_NotLogicOP_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetInMainc4(my_id) == false));
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! res_NotLogicOP_7);
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_6);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_3);
    
    if(res_OrLogicOP_1){
    
    L_P1__SetOutMainc(my_id,false);
    }else{
    
    Timer_Disattiva(L_P1__GetMainc41(my_id));
    }
    //  *109,*  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  uguale a  True , *70,*Incrementa il contatore MainClass_C1_contatore_Co5
    // ,altrimenti  *67,* Assegna alla variabile MainClass_C1_variabile_V5 il valore 9
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetMainc25(my_id) == true));
    if(res_NotLogicOP_8){
    
    Counter_Incr(L_P1__GetMainc44(my_id));
    }else{
    
    L_P1__SetMainc35(my_id,9u);
    }
    //  se il controllo ConsDef  è  uguale a FALSE  *36,* o  se il timer MainClass_C1_timer_T4 è attivo *38,* o  se il contatore MainClass_C1_contatore_Co8 non è  minore di  *55,* 142 *38,* o  se il contatore MainClass_C1_contatore_Co3 non è  maggiore di  *54,* 1430, *67,* Assegna alla variabile MainClass_C1_variabile_V10 il valore  True 
    // ,altrimenti   Applica gli effetti
    //       della macro MainClass_C1_macroef_M3( con argomento_af5   uguale a True ,argomento_af9   uguale a Rosso ,argomento_af6   uguale a Giallox )
    bool res_OrLogicOP_9 = false;
    bool res_OrLogicOP_10 = false;
    bool res_OrLogicOP_11 = false;
    res_OrLogicOP_11 = (res_OrLogicOP_11 || (L_P1__GetInConsd(my_id) == false));
    res_OrLogicOP_11 = (res_OrLogicOP_11 || Timer_Attivo(L_P1__GetMainc41(my_id)));
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_OrLogicOP_11);
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (Counter_GetValore(L_P1__GetMainc45(my_id)) < 142u));
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_NotLogicOP_12);
    
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_OrLogicOP_10);
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (Counter_GetValore(L_P1__GetMainc43(my_id)) > 1430u));
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_NotLogicOP_13);
    
    if(res_OrLogicOP_9){
    
    L_P1__SetMainc32(my_id,true);
    }else{
    
    L_P1__Macro(my_id,true,giallox,rosso);
    }
    //  *73,*
    //  se il controllo ConsDef  è  uguale a FALSE  *37,* e  se la variabile MainClass_C1_variabile_V2 non è  uguale a  False  *35,* e  se il controllo MainClass_C1_controllo_C7 non è  uguale a  True  *34,* e  se il parametro MainClass_C1_parametro_P9 è  diverso da  False  *34,* e  se il parametro MainClass_C1_parametro_P9 è  uguale a  True , *67,* Assegna alla variabile MainClass_C1_variabile_V3 il valore RossoGialloVerde
    // ,altrimenti   Applica gli effetti
    //       della macro MainClass_C1_macroef_M9
    bool res_AndLogicOP_14 = true;
    bool res_AndLogicOP_15 = true;
    bool res_AndLogicOP_16 = true;
    bool res_AndLogicOP_17 = true;
    res_AndLogicOP_17 = (res_AndLogicOP_17 && (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_18 = true;
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! (L_P1__GetMainc33(my_id) == false));
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_NotLogicOP_18);
    
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_AndLogicOP_17);
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (L_P1__GetInMainc3(my_id) == true));
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_NotLogicOP_19);
    
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_AndLogicOP_16);
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! (L_P1__GetParamMainc9(my_id) == false));
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_NotLogicOP_20);
    
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_AndLogicOP_15);
    res_AndLogicOP_14 = (res_AndLogicOP_14 && (L_P1__GetParamMainc9(my_id) == true));
    
    if(res_AndLogicOP_14){
    
    L_P1__SetMainc34(my_id,rossogiallo1);
    }else{
    
    L_P1__Macro4(my_id);
    }
}

/*
    CNL corrispondente:
    
    { commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è scaduto commento: {36,} e  se il timer MainClass_C1_timer_T3 non è attivo commento: {36,} o  se il timer MainClass_C1_timer_T6 non è scaduto commento: {38,} e  se il contatore MainClass_C1_contatore_Co8 è  uguale a  commento: {53,} 14 commento: {34,} o  se il parametro MainClass_C1_parametro_P9 è  diverso da  False  commento: {34,} o  se il parametro MainClass_C1_parametro_P9 non è  diverso da  False ,  Applica gli effetti
           della macro MainClass_C1_macroef_M6  commento: {73,}
    
     ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V6 il valore  True 
    
    
     commento: {35,}  se il controllo MainClass_C1_controllo_C9 è  diverso da RossoGialloaVerdea commento: {38,} o  se il contatore MainClass_C1_contatore_Co3 è  minore di  commento: {55,} 13451 o  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro MainClass_C1_parametro_P10 non è  uguale a RossoGialloaVerdea commento: {34,} e  se il parametro MainClass_C1_parametro_P3 è  minore di  commento: {55,} 7, commento: {66,} Assegna al comando MainClass_C1_comando_C9 il valore  False 
    
       
      se la macro  MainClass_C1_macrova_M9 ( con argomento_a9   uguale a True ,argomento_a6   uguale a RossoGialloVerde ,argomento_a2   uguale a c180x ,argomento_a7   uguale a c180 ,argomento_a3   uguale a RossoGialloVerde  e argomento_a4   uguale a c180 )   è  diverso da Verde commento: {40,}  commento: {38,} o  se il contatore MainClass_C1_contatore_Co8 è  diverso da  commento: {56,} 152 o  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} e  se il contatore MainClass_C1_contatore_Co5 è  uguale a  commento: {53,} 133, commento: {66,} Assegna al comando MainClass_C1_comando_C9 il valore  True 
    
     ,altrimenti  commento: {68,}Attiva il timer MainClass_C1_timer_T3
    
    
     commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  diverso da  False ,  Applica gli effetti
           della macro MainClass_C1_macroef_M7   commento: {73,}
    
       
    
    }
*/
void L_P1__Macro3(instance_id_t const my_id )
{
//  *110,*  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è scaduto *36,* e  se il timer MainClass_C1_timer_T3 non è attivo *36,* o  se il timer MainClass_C1_timer_T6 non è scaduto *38,* e  se il contatore MainClass_C1_contatore_Co8 è  uguale a  *53,* 14 *34,* o  se il parametro MainClass_C1_parametro_P9 è  diverso da  False  *34,* o  se il parametro MainClass_C1_parametro_P9 non è  diverso da  False ,  Applica gli effetti
    //       della macro MainClass_C1_macroef_M6  *73,*
    // ,altrimenti  *67,* Assegna alla variabile MainClass_C1_variabile_V6 il valore  True
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_OrLogicOP_2 = false;
    bool res_AndLogicOP_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! Timer_Scaduto(L_P1__GetMainc38(my_id)));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_4);
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! Timer_Attivo(L_P1__GetMainc40(my_id)));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_5);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_3);
    bool res_AndLogicOP_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! Timer_Scaduto(L_P1__GetMainc42(my_id)));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_7);
    res_AndLogicOP_6 = (res_AndLogicOP_6 && (Counter_GetValore(L_P1__GetMainc45(my_id)) == 14u));
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_6);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_OrLogicOP_2);
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetParamMainc9(my_id) == false));
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_NotLogicOP_8);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_NotLogicOP_9 = true;
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__GetParamMainc9(my_id) == false));
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! res_NotLogicOP_10);
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_9);
    
    if(res_OrLogicOP_0){
    
    L_P1__Macro1(my_id);
    }else{
    
    L_P1__SetMainc36(my_id,true);
    }
    //  *35,*  se il controllo MainClass_C1_controllo_C9 è  diverso da RossoGialloaVerdea *38,* o  se il contatore MainClass_C1_contatore_Co3 è  minore di  *55,* 13451 o  se il controllo ConsDef  è  uguale a FALSE  *34,* e  se il parametro MainClass_C1_parametro_P10 non è  uguale a RossoGialloaVerdea *34,* e  se il parametro MainClass_C1_parametro_P3 è  minore di  *55,* 7, *66,* Assegna al comando MainClass_C1_comando_C9 il valore  False
    bool res_OrLogicOP_11 = false;
    bool res_OrLogicOP_12 = false;
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (L_P1__GetInMainc5(my_id) == rossogiallo));
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_NotLogicOP_13);
    res_OrLogicOP_12 = (res_OrLogicOP_12 || (Counter_GetValore(L_P1__GetMainc43(my_id)) < 13451u));
    
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_OrLogicOP_12);
    bool res_AndLogicOP_14 = true;
    bool res_AndLogicOP_15 = true;
    res_AndLogicOP_15 = (res_AndLogicOP_15 && (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (L_P1__GetParamMainc6(my_id) == rossogiallo));
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_NotLogicOP_16);
    
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_AndLogicOP_15);
    res_AndLogicOP_14 = (res_AndLogicOP_14 && (L_P1__GetParamMainc7(my_id) < 7u));
    
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_AndLogicOP_14);
    
    if(res_OrLogicOP_11){
    
    L_P1__SetOutMainc(my_id,false);
    }
    //  se la macro  MainClass_C1_macrova_M9 ( con argomento_a9   uguale a True ,argomento_a6   uguale a RossoGialloVerde ,argomento_a2   uguale a c180x ,argomento_a7   uguale a c180 ,argomento_a3   uguale a RossoGialloVerde  e argomento_a4   uguale a c180 )   è  diverso da Verde *40,*  *38,* o  se il contatore MainClass_C1_contatore_Co8 è  diverso da  *56,* 152 o  se il controllo ConsDef  è  uguale a FALSE  *38,* e  se il contatore MainClass_C1_contatore_Co5 è  uguale a  *53,* 133, *66,* Assegna al comando MainClass_C1_comando_C9 il valore  True 
    // ,altrimenti  *68,*Attiva il timer MainClass_C1_timer_T3
    bool res_OrLogicOP_17 = false;
    bool res_OrLogicOP_18 = false;
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (L_P1__Macro7(my_id,c180x,rossogiallo1,c180,rossogiallo1,c180,true) == verde));
    res_OrLogicOP_18 = (res_OrLogicOP_18 || res_NotLogicOP_19);
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! (Counter_GetValore(L_P1__GetMainc45(my_id)) == 152u));
    res_OrLogicOP_18 = (res_OrLogicOP_18 || res_NotLogicOP_20);
    
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_OrLogicOP_18);
    bool res_AndLogicOP_21 = true;
    res_AndLogicOP_21 = (res_AndLogicOP_21 && (L_P1__GetInConsd(my_id) == false));
    res_AndLogicOP_21 = (res_AndLogicOP_21 && (Counter_GetValore(L_P1__GetMainc44(my_id)) == 133u));
    
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_AndLogicOP_21);
    
    if(res_OrLogicOP_17){
    
    L_P1__SetOutMainc(my_id,true);
    }else{
    
    Timer_Attiva(L_P1__GetMainc40(my_id));
    }
    //  *109,*  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  diverso da  False ,  Applica gli effetti
    //       della macro MainClass_C1_macroef_M7
    bool res_NotLogicOP_22 = true;
    bool res_NotLogicOP_23 = true;
    res_NotLogicOP_23 = (res_NotLogicOP_23 && ! (L_P1__GetMainc25(my_id) == false));
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! res_NotLogicOP_23);
    if(res_NotLogicOP_22){
    
    L_P1__Macro2(my_id);
    }
}

/*
    CNL corrispondente:
    
    { commento: {34,}  se lo stato  non è  diverso da  commento: {56,}  state1  commento: {106,} o  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} e  se il controllo MainClass_C1_controllo_C7 è  diverso da  False , commento: {66,} Assegna al comando MainClass_C1_comando_C9 il valore  False 
    
     ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V10 il valore  False 
    
    
    
    }
*/
void L_P1__Macro4(instance_id_t const my_id )
{
//  *34,*  se lo stato  non è  diverso da  *56,*  state1  *106,* o  se il controllo ConsDef  è  uguale a FALSE  *35,* e  se il controllo MainClass_C1_controllo_C7 è  diverso da  False , *66,* Assegna al comando MainClass_C1_comando_C9 il valore  False 
    // ,altrimenti  *67,* Assegna alla variabile MainClass_C1_variabile_V10 il valore  False
    bool res_OrLogicOP_0 = false;
    bool res_NotLogicOP_1 = true;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (L_P1_C1_GetState(my_id) == C1_St_state));
    res_NotLogicOP_1 = (res_NotLogicOP_1 && ! res_NotLogicOP_2);
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_1);
    bool res_AndLogicOP_3 = true;
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetInMainc3(my_id) == false));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_4);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_3);
    
    if(res_OrLogicOP_0){
    
    L_P1__SetOutMainc(my_id,false);
    }else{
    
    L_P1__SetMainc32(my_id,false);
    }
}


// Macro di verifica

/*
    CNL corrispondente:
     
    { commento: {37,}  se la variabile MainClass_C1_variabile_V2 non è  uguale a  True  commento: {36,} o  se il timer MainClass_C1_timer_T10 è attivo, Verifica che   commento: {47,48,50,51,}  commento: {,}  il controllo MainClass_C1_controllo_C7 non sia  diverso da  True 
     commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P9 non sia  diverso da  True 
     commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V5 sia  uguale a  commento: {53,} 5
     commento: {104,} o  che  commento: {35,}  il controllo MainClass_C1_controllo_C7 sia  uguale a  True 
     commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co3 sia  maggiore di  commento: {54,} 151
    
    
    }
*/
bool L_P1__Macro8(instance_id_t const my_id )
{
bool res_AndLogicOP_0 = true;
    
    //  *37,*  se la variabile MainClass_C1_variabile_V2 non è  uguale a  True  *36,* o  se il timer MainClass_C1_timer_T10 è attivo, Verifica che   *47,48,50,51,*  *,*  il controllo MainClass_C1_controllo_C7 non sia  diverso da  True 
    //   *104,* e  che  *34,*  il parametro MainClass_C1_parametro_P9 non sia  diverso da  True 
    //   *104,* o  che  *,*  la variabile MainClass_C1_variabile_V5 sia  uguale a  *53,* 5
    //   *104,* o  che  *35,*  il controllo MainClass_C1_controllo_C7 sia  uguale a  True 
    //   *104,* e  che  *,*  il contatore MainClass_C1_contatore_Co3 sia  maggiore di  *54,* 151
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__GetMainc33(my_id) == true));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_3);
    res_OrLogicOP_2 = (res_OrLogicOP_2 || Timer_Attivo(L_P1__GetMainc39(my_id)));
    
    if(res_OrLogicOP_2){
    bool res_OrLogicOP_4 = false;
    bool res_OrLogicOP_5 = false;
    bool res_AndLogicOP_6 = true;
    bool res_NotLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetInMainc3(my_id) == true));
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! res_NotLogicOP_8);
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_7);
    bool res_NotLogicOP_9 = true;
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__GetParamMainc9(my_id) == true));
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! res_NotLogicOP_10);
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_9);
    
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_AndLogicOP_6);
    res_OrLogicOP_5 = (res_OrLogicOP_5 || (L_P1__GetMainc35(my_id) == 5u));
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_OrLogicOP_5);
    bool res_AndLogicOP_11 = true;
    res_AndLogicOP_11 = (res_AndLogicOP_11 && (L_P1__GetInMainc3(my_id) == true));
    res_AndLogicOP_11 = (res_AndLogicOP_11 && (Counter_GetValore(L_P1__GetMainc43(my_id)) > 151u));
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_AndLogicOP_11);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_OrLogicOP_4);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
     
    { commento: {36,}  se il timer MainClass_C1_timer_T6 non è scaduto, Verifica che   commento: {48,49,}  commento: {,}  il timer MainClass_C1_timer_T3 non sia disattivo
     commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C5 sia  diverso da RossoGialloVerde
     commento: {104,} o  che  commento: {36,}  il timer MainClass_C1_timer_T10 non sia scaduto
    
    
    }
*/
bool L_P1__Macro9(instance_id_t const my_id )
{
bool res_AndLogicOP_0 = true;
    
    //  *36,*  se il timer MainClass_C1_timer_T6 non è scaduto, Verifica che   *48,49,*  *,*  il timer MainClass_C1_timer_T3 non sia disattivo
    //   *104,* e  che  *,*  il controllo MainClass_C1_controllo_C5 sia  diverso da RossoGialloVerde
    //   *104,* o  che  *36,*  il timer MainClass_C1_timer_T10 non sia scaduto
    bool res_ImpliesLogicOp_1 = true;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! Timer_Scaduto(L_P1__GetMainc42(my_id)));
    if(res_NotLogicOP_2){
    bool res_OrLogicOP_3 = false;
    bool res_AndLogicOP_4 = true;
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! Timer_Disattivo(L_P1__GetMainc40(my_id)));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_5);
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetInMainc2(my_id) == rossogiallo1));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_6);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_AndLogicOP_4);
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! Timer_Scaduto(L_P1__GetMainc39(my_id)));
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_NotLogicOP_7);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_OrLogicOP_3);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
     
    { commento: {61,}  se la macro  MainClass_C1_macrova_M4 ( con argomento_a1   uguale a c180 ,argomento_a8   uguale a avvio ,argomento_a10   uguale a RossoGialloVerde ,argomento_a5   uguale a RossoGialloaVerdea  e argomento_a9   uguale a RossoGialloaVerdea )   è  diverso da Giallox commento: {40,}  commento: {36,} o  se il timer MainClass_C1_timer_T3 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} e  se il controllo MainClass_C1_controllo_C7 non è  diverso da  False  commento: {34,} e  se il parametro MainClass_C1_parametro_P10 è  diverso da RossoGialloaVerdea e  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
     commento: {62,}  se la macro  MainClass_C1_macrova_M4 ( con argomento_a1   uguale a RossoGialloVerde ,argomento_a8   uguale a avvio ,argomento_a10   uguale a RossoGialloVerde ,argomento_a5   uguale a Rosso  e argomento_a9   uguale a RossoGialloaVerdea )   è  diverso da Giallox commento: {40,}  commento: {36,} e  se il timer MainClass_C1_timer_T3 non è disattivo commento: {36,} o  se il timer MainClass_C1_timer_T3 è attivo commento: {34,} e  se il parametro MainClass_C1_parametro_P7 è  maggiore di  commento: {54,} 2, Almeno una delle seguenti { 
     commento: {62,}  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} o  se il contatore MainClass_C1_contatore_Co8 non è  minore di  commento: {55,} 122 commento: {35,} e  se il controllo MainClass_C1_controllo_C7 è  diverso da  True  commento: {37,} e  se la variabile MainClass_C1_variabile_V10 è  diverso da  False  commento: {36,} o  se il timer MainClass_C1_timer_T10 non è scaduto, Almeno una delle seguenti { 
     commento: {63,} commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo commento: {34,} o  se il parametro MainClass_C1_parametro_P7 non è  maggiore di  commento: {54,} 4 commento: {38,} e  se il contatore MainClass_C1_contatore_Co9 è  uguale a  commento: {53,} 1430 e  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} o  se la variabile MainClass_C1_variabile_V3 è  diverso da RossoGialloVerde commento: {34,} e  se il parametro MainClass_C1_parametro_P9 non è  diverso da  True , Solo una delle seguenti { 
      se il controllo ConsDef è uguale a FALSE  commento: {36,} e  se il timer MainClass_C1_timer_T3 non è disattivo, Verifica che   commento: {48,49,}   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T3 sia disattivo
    
    
     } Verifica che   commento: {47,48,}   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P3 non sia  maggiore di  commento: {54,} 6
     commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P3 non sia  minore di  commento: {55,} 3
    
    
     } Verifica che   commento: {49,50,51,}  commento: {,}  il contatore MainClass_C1_contatore_Co9 sia  minore di  commento: {55,} 14
     commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V2 non sia  uguale a  True 
     commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T3 non sia scaduto
    
    
     } Verifica che   commento: {49,51,}  commento: {,}  il timer MainClass_C1_timer_T4 sia disattivo
     commento: {104,} o  che  commento: {,}  il contatore MainClass_C1_contatore_Co3 non sia  minore di  commento: {55,} 14
     commento: {104,} o  che  commento: {38,}  il contatore MainClass_C1_contatore_Co3 sia  minore di  commento: {55,} 14
    
    
     } Verifica che   commento: {47,48,50,}  commento: {34,}  il parametro MainClass_C1_parametro_P3 sia  minore di  commento: {55,} 7
     commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V10 sia  uguale a  True 
     commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
    
    
    }
*/
bool L_P1__Macro10(instance_id_t const my_id )
{
bool res_AndLogicOP_0 = true;
    
    //  *61,*  se la macro  MainClass_C1_macrova_M4 ( con argomento_a1   uguale a c180 ,argomento_a8   uguale a avvio ,argomento_a10   uguale a RossoGialloVerde ,argomento_a5   uguale a RossoGialloaVerdea  e argomento_a9   uguale a RossoGialloaVerdea )   è  diverso da Giallox *40,*  *36,* o  se il timer MainClass_C1_timer_T3 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  *35,* e  se il controllo MainClass_C1_controllo_C7 non è  diverso da  False  *34,* e  se il parametro MainClass_C1_parametro_P10 è  diverso da RossoGialloaVerdea e  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
    //   *62,*  se la macro  MainClass_C1_macrova_M4 ( con argomento_a1   uguale a RossoGialloVerde ,argomento_a8   uguale a avvio ,argomento_a10   uguale a RossoGialloVerde ,argomento_a5   uguale a Rosso  e argomento_a9   uguale a RossoGialloaVerdea )   è  diverso da Giallox *40,*  *36,* e  se il timer MainClass_C1_timer_T3 non è disattivo *36,* o  se il timer MainClass_C1_timer_T3 è attivo *34,* e  se il parametro MainClass_C1_parametro_P7 è  maggiore di  *54,* 2, Almeno una delle seguenti { 
    //   *62,*  se il controllo ConsDef  è  uguale a FALSE  *38,* o  se il contatore MainClass_C1_contatore_Co8 non è  minore di  *55,* 122 *35,* e  se il controllo MainClass_C1_controllo_C7 è  diverso da  True  *37,* e  se la variabile MainClass_C1_variabile_V10 è  diverso da  False  *36,* o  se il timer MainClass_C1_timer_T10 non è scaduto, Almeno una delle seguenti { 
    //   *63,* *110,*  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo *34,* o  se il parametro MainClass_C1_parametro_P7 non è  maggiore di  *54,* 4 *38,* e  se il contatore MainClass_C1_contatore_Co9 è  uguale a  *53,* 1430 e  se il controllo ConsDef  è  uguale a FALSE  *37,* o  se la variabile MainClass_C1_variabile_V3 è  diverso da RossoGialloVerde *34,* e  se il parametro MainClass_C1_parametro_P9 non è  diverso da  True , Solo una delle seguenti { 
    //    se il controllo ConsDef è uguale a FALSE  *36,* e  se il timer MainClass_C1_timer_T3 non è disattivo, Verifica che   *48,49,*   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* o  che   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* o  che  *,*  il timer MainClass_C1_timer_T3 sia disattivo
    //   } Verifica che   *47,48,*   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* e  che  *34,*  il parametro MainClass_C1_parametro_P3 non sia  maggiore di  *54,* 6
    //   *104,* e  che  *34,*  il parametro MainClass_C1_parametro_P3 non sia  minore di  *55,* 3
    //   } Verifica che   *49,50,51,*  *,*  il contatore MainClass_C1_contatore_Co9 sia  minore di  *55,* 14
    //   *104,* o  che  *,*  la variabile MainClass_C1_variabile_V2 non sia  uguale a  True 
    //   *104,* o  che  *,*  il timer MainClass_C1_timer_T3 non sia scaduto
    //   } Verifica che   *49,51,*  *,*  il timer MainClass_C1_timer_T4 sia disattivo
    //   *104,* o  che  *,*  il contatore MainClass_C1_contatore_Co3 non sia  minore di  *55,* 14
    //   *104,* o  che  *38,*  il contatore MainClass_C1_contatore_Co3 sia  minore di  *55,* 14
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__Macro5(my_id,c180,rossogiallo1,rossogiallo,avvio,rossogiallo) == giallox));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_3);
    bool res_AndLogicOP_4 = true;
    bool res_AndLogicOP_5 = true;
    bool res_AndLogicOP_6 = true;
    bool res_AndLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! Timer_Scaduto(L_P1__GetMainc40(my_id)));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_8);
    res_AndLogicOP_7 = (res_AndLogicOP_7 && (L_P1__GetInConsd(my_id) == false));
    
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_AndLogicOP_7);
    bool res_NotLogicOP_9 = true;
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__GetInMainc3(my_id) == false));
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! res_NotLogicOP_10);
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_9);
    
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_AndLogicOP_6);
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (L_P1__GetParamMainc6(my_id) == rossogiallo));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_11);
    
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_AndLogicOP_5);
    res_AndLogicOP_4 = (res_AndLogicOP_4 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_4);
    
    if(res_OrLogicOP_2){
    bool res_AndLogicOP_12 = true;
    bool res_ImpliesLogicOp_13 = true;
    bool res_OrLogicOP_14 = false;
    bool res_AndLogicOP_15 = true;
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (L_P1__Macro5(my_id,rossogiallo1,rossogiallo1,rosso,avvio,rossogiallo) == giallox));
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_NotLogicOP_16);
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! Timer_Disattivo(L_P1__GetMainc40(my_id)));
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_NotLogicOP_17);
    
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_AndLogicOP_15);
    bool res_AndLogicOP_18 = true;
    res_AndLogicOP_18 = (res_AndLogicOP_18 && Timer_Attivo(L_P1__GetMainc40(my_id)));
    res_AndLogicOP_18 = (res_AndLogicOP_18 && (L_P1__GetParamMainc8(my_id) > 2u));
    
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_AndLogicOP_18);
    
    if(res_OrLogicOP_14){
    bool res_OrLogicOP_19 = false;
    bool res_ImpliesLogicOp_20 = true;
    bool res_OrLogicOP_21 = false;
    bool res_OrLogicOP_22 = false;
    res_OrLogicOP_22 = (res_OrLogicOP_22 || (L_P1__GetInConsd(my_id) == false));
    bool res_AndLogicOP_23 = true;
    bool res_AndLogicOP_24 = true;
    bool res_NotLogicOP_25 = true;
    res_NotLogicOP_25 = (res_NotLogicOP_25 && ! (Counter_GetValore(L_P1__GetMainc45(my_id)) < 122u));
    res_AndLogicOP_24 = (res_AndLogicOP_24 && res_NotLogicOP_25);
    bool res_NotLogicOP_26 = true;
    res_NotLogicOP_26 = (res_NotLogicOP_26 && ! (L_P1__GetInMainc3(my_id) == true));
    res_AndLogicOP_24 = (res_AndLogicOP_24 && res_NotLogicOP_26);
    
    res_AndLogicOP_23 = (res_AndLogicOP_23 && res_AndLogicOP_24);
    bool res_NotLogicOP_27 = true;
    res_NotLogicOP_27 = (res_NotLogicOP_27 && ! (L_P1__GetMainc32(my_id) == false));
    res_AndLogicOP_23 = (res_AndLogicOP_23 && res_NotLogicOP_27);
    
    res_OrLogicOP_22 = (res_OrLogicOP_22 || res_AndLogicOP_23);
    
    res_OrLogicOP_21 = (res_OrLogicOP_21 || res_OrLogicOP_22);
    bool res_NotLogicOP_28 = true;
    res_NotLogicOP_28 = (res_NotLogicOP_28 && ! Timer_Scaduto(L_P1__GetMainc39(my_id)));
    res_OrLogicOP_21 = (res_OrLogicOP_21 || res_NotLogicOP_28);
    
    if(res_OrLogicOP_21){
    bool res_OrLogicOP_29 = false;
    bool res_ImpliesLogicOp_30 = true;
    bool res_OrLogicOP_31 = false;
    bool res_OrLogicOP_32 = false;
    bool res_NotLogicOP_33 = true;
    res_NotLogicOP_33 = (res_NotLogicOP_33 && ! Timer_Attivo(L_P1__GetMainc38(my_id)));
    res_OrLogicOP_32 = (res_OrLogicOP_32 || res_NotLogicOP_33);
    bool res_AndLogicOP_34 = true;
    bool res_AndLogicOP_35 = true;
    bool res_NotLogicOP_36 = true;
    res_NotLogicOP_36 = (res_NotLogicOP_36 && ! (L_P1__GetParamMainc8(my_id) > 4u));
    res_AndLogicOP_35 = (res_AndLogicOP_35 && res_NotLogicOP_36);
    res_AndLogicOP_35 = (res_AndLogicOP_35 && (Counter_GetValore(L_P1__GetMainc46(my_id)) == 1430u));
    
    res_AndLogicOP_34 = (res_AndLogicOP_34 && res_AndLogicOP_35);
    res_AndLogicOP_34 = (res_AndLogicOP_34 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_32 = (res_OrLogicOP_32 || res_AndLogicOP_34);
    
    res_OrLogicOP_31 = (res_OrLogicOP_31 || res_OrLogicOP_32);
    bool res_AndLogicOP_37 = true;
    bool res_NotLogicOP_38 = true;
    res_NotLogicOP_38 = (res_NotLogicOP_38 && ! (L_P1__GetMainc34(my_id) == rossogiallo1));
    res_AndLogicOP_37 = (res_AndLogicOP_37 && res_NotLogicOP_38);
    bool res_NotLogicOP_39 = true;
    bool res_NotLogicOP_40 = true;
    res_NotLogicOP_40 = (res_NotLogicOP_40 && ! (L_P1__GetParamMainc9(my_id) == true));
    res_NotLogicOP_39 = (res_NotLogicOP_39 && ! res_NotLogicOP_40);
    res_AndLogicOP_37 = (res_AndLogicOP_37 && res_NotLogicOP_39);
    
    res_OrLogicOP_31 = (res_OrLogicOP_31 || res_AndLogicOP_37);
    
    if(res_OrLogicOP_31){
    bool res_ImpliesLogicOp_41 = true;
    bool res_AndLogicOP_42 = true;
    res_AndLogicOP_42 = (res_AndLogicOP_42 && (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_43 = true;
    res_NotLogicOP_43 = (res_NotLogicOP_43 && ! Timer_Disattivo(L_P1__GetMainc40(my_id)));
    res_AndLogicOP_42 = (res_AndLogicOP_42 && res_NotLogicOP_43);
    
    if(res_AndLogicOP_42){
    bool res_OrLogicOP_44 = false;
    bool res_OrLogicOP_45 = false;
    res_OrLogicOP_45 = (res_OrLogicOP_45 || (L_P1__GetInConsd(my_id) == false));
    res_OrLogicOP_45 = (res_OrLogicOP_45 || (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_44 = (res_OrLogicOP_44 || res_OrLogicOP_45);
    res_OrLogicOP_44 = (res_OrLogicOP_44 || Timer_Disattivo(L_P1__GetMainc40(my_id)));
    
    res_ImpliesLogicOp_41 = (res_ImpliesLogicOp_41 && res_OrLogicOP_44);
    }
    res_ImpliesLogicOp_30 = (res_ImpliesLogicOp_30 && res_ImpliesLogicOp_41);
    }
    res_OrLogicOP_29 = (res_OrLogicOP_29 || res_ImpliesLogicOp_30);
    bool res_AndLogicOP_46 = true;
    bool res_AndLogicOP_47 = true;
    res_AndLogicOP_47 = (res_AndLogicOP_47 && (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_48 = true;
    res_NotLogicOP_48 = (res_NotLogicOP_48 && ! (L_P1__GetParamMainc7(my_id) > 6u));
    res_AndLogicOP_47 = (res_AndLogicOP_47 && res_NotLogicOP_48);
    
    res_AndLogicOP_46 = (res_AndLogicOP_46 && res_AndLogicOP_47);
    bool res_NotLogicOP_49 = true;
    res_NotLogicOP_49 = (res_NotLogicOP_49 && ! (L_P1__GetParamMainc7(my_id) < 3u));
    res_AndLogicOP_46 = (res_AndLogicOP_46 && res_NotLogicOP_49);
    
    res_OrLogicOP_29 = (res_OrLogicOP_29 || res_AndLogicOP_46);
    
    res_ImpliesLogicOp_20 = (res_ImpliesLogicOp_20 && res_OrLogicOP_29);
    }
    res_OrLogicOP_19 = (res_OrLogicOP_19 || res_ImpliesLogicOp_20);
    bool res_OrLogicOP_50 = false;
    bool res_OrLogicOP_51 = false;
    res_OrLogicOP_51 = (res_OrLogicOP_51 || (Counter_GetValore(L_P1__GetMainc46(my_id)) < 14u));
    bool res_NotLogicOP_52 = true;
    res_NotLogicOP_52 = (res_NotLogicOP_52 && ! (L_P1__GetMainc33(my_id) == true));
    res_OrLogicOP_51 = (res_OrLogicOP_51 || res_NotLogicOP_52);
    
    res_OrLogicOP_50 = (res_OrLogicOP_50 || res_OrLogicOP_51);
    bool res_NotLogicOP_53 = true;
    res_NotLogicOP_53 = (res_NotLogicOP_53 && ! Timer_Scaduto(L_P1__GetMainc40(my_id)));
    res_OrLogicOP_50 = (res_OrLogicOP_50 || res_NotLogicOP_53);
    
    res_OrLogicOP_19 = (res_OrLogicOP_19 || res_OrLogicOP_50);
    
    res_ImpliesLogicOp_13 = (res_ImpliesLogicOp_13 && res_OrLogicOP_19);
    }
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_ImpliesLogicOp_13);
    bool res_OrLogicOP_54 = false;
    bool res_OrLogicOP_55 = false;
    res_OrLogicOP_55 = (res_OrLogicOP_55 || Timer_Disattivo(L_P1__GetMainc41(my_id)));
    bool res_NotLogicOP_56 = true;
    res_NotLogicOP_56 = (res_NotLogicOP_56 && ! (Counter_GetValore(L_P1__GetMainc43(my_id)) < 14u));
    res_OrLogicOP_55 = (res_OrLogicOP_55 || res_NotLogicOP_56);
    
    res_OrLogicOP_54 = (res_OrLogicOP_54 || res_OrLogicOP_55);
    res_OrLogicOP_54 = (res_OrLogicOP_54 || (Counter_GetValore(L_P1__GetMainc43(my_id)) < 14u));
    
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_OrLogicOP_54);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_AndLogicOP_12);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *47,48,50,*  *34,*  il parametro MainClass_C1_parametro_P3 sia  minore di  *55,* 7
    //   *104,* o  che  *,*  la variabile MainClass_C1_variabile_V10 sia  uguale a  True 
    //   *104,* e  che   il controllo ConsDef  sia  uguale a FALSE
    bool res_OrLogicOP_57 = false;
    res_OrLogicOP_57 = (res_OrLogicOP_57 || (L_P1__GetParamMainc7(my_id) < 7u));
    bool res_AndLogicOP_58 = true;
    res_AndLogicOP_58 = (res_AndLogicOP_58 && (L_P1__GetMainc32(my_id) == true));
    res_AndLogicOP_58 = (res_AndLogicOP_58 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_57 = (res_OrLogicOP_57 || res_AndLogicOP_58);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_57);
    
    
    
    return res_AndLogicOP_0;
}


// Macro valorizzate

/*
    CNL corrispondente:
    
    { commento: {[} commento: {34,}  se il parametro MainClass_C1_parametro_P9 non è  diverso da  True  commento: {109,} o  se il ripristino della variabile  MainClass_C1_restoreva_RV3 non è  diverso da Giallox commento: {37,} e  se la variabile MainClass_C1_variabile_V3 è  diverso da RossoGialloVerde e  se la macro  MainClass_C1_macrova_M9 ( con argomento_a9   uguale a True ,argomento_a6   uguale a c180 ,argomento_a2   uguale a Verde ,argomento_a7   uguale a RossoGialloVerde ,argomento_a3   uguale a c180  e argomento_a4   uguale a c180 )   è  diverso da Verde commento: {40,}  , assegna alla macro il valore Giallox
    
     commento: {46,} assegna alla macro il valore Giallox commento: {],}
    }
*/
C1_Enumerat1 L_P1__Macro5(instance_id_t const my_id , C1_Enumerat3 argom3, C1_Enumerat3 argom4, C1_Enumerat2 argom5, C1_Enumerat1 argom6, C1_Enumerat2 argom7)
{
C1_Enumerat1 res_macro_val;
    
    //  *[* *34,*  se il parametro MainClass_C1_parametro_P9 non è  diverso da  True  *109,* o  se il ripristino della variabile  MainClass_C1_restoreva_RV3 non è  diverso da Giallox *37,* e  se la variabile MainClass_C1_variabile_V3 è  diverso da RossoGialloVerde e  se la macro  MainClass_C1_macrova_M9 ( con argomento_a9   uguale a True ,argomento_a6   uguale a c180 ,argomento_a2   uguale a Verde ,argomento_a7   uguale a RossoGialloVerde ,argomento_a3   uguale a c180  e argomento_a4   uguale a c180 )   è  diverso da Verde
    bool res_OrLogicOP_0 = false;
    bool res_NotLogicOP_1 = true;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (L_P1__GetParamMainc9(my_id) == true));
    res_NotLogicOP_1 = (res_NotLogicOP_1 && ! res_NotLogicOP_2);
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_1);
    bool res_AndLogicOP_3 = true;
    bool res_AndLogicOP_4 = true;
    bool res_NotLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetMainc29(my_id) == giallox));
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! res_NotLogicOP_6);
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_5);
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetMainc34(my_id) == rossogiallo1));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_7);
    
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_AndLogicOP_4);
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__Macro7(my_id,verde,c180,c180,c180,rossogiallo1,true) == verde));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_8);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_3);
    
    if(res_OrLogicOP_0){
    
    res_macro_val = giallox;
    }
    else{
    res_macro_val = giallox;
    }
    return res_macro_val;
}

/*
    CNL corrispondente:
    
    { commento: {[}  se la macro  MainClass_C1_macrova_M4 ( con argomento_a1   uguale a c180 ,argomento_a8   uguale a avvio ,argomento_a10   uguale a RossoGialloVerde ,argomento_a5   uguale a Rosso  e argomento_a9   uguale a RossoGialloaVerdea )   è  diverso da Giallox commento: {40,}  commento: {35,} o  se il controllo MainClass_C1_controllo_C9 è  diverso da RossoGialloaVerdea commento: {34,} o  se lo stato  è  diverso da  commento: {56,}  state1  commento: {106,} commento: {35,} e  se il controllo MainClass_C1_controllo_C7 non è  diverso da  False  , assegna alla macro il valore Giallox
    
     commento: {46,} assegna alla macro il valore Giallox commento: {],}
    }
*/
C1_Enumerat1 L_P1__Macro6(instance_id_t const my_id , C1_Enumerat4 argom8, C1_Enumerat4 argom9, C1_Enumerat2 argom10, bool argom11, C1_Enumerat3 argom12)
{
C1_Enumerat1 res_macro_val;
    
    //  *[*  se la macro  MainClass_C1_macrova_M4 ( con argomento_a1   uguale a c180 ,argomento_a8   uguale a avvio ,argomento_a10   uguale a RossoGialloVerde ,argomento_a5   uguale a Rosso  e argomento_a9   uguale a RossoGialloaVerdea )   è  diverso da Giallox *40,*  *35,* o  se il controllo MainClass_C1_controllo_C9 è  diverso da RossoGialloaVerdea *34,* o  se lo stato  è  diverso da  *56,*  state1  *106,* *35,* e  se il controllo MainClass_C1_controllo_C7 non è  diverso da  False
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (L_P1__Macro5(my_id,c180,rossogiallo1,rosso,avvio,rossogiallo) == giallox));
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_NotLogicOP_2);
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__GetInMainc5(my_id) == rossogiallo));
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_NotLogicOP_3);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_AndLogicOP_4 = true;
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1_C1_GetState(my_id) == C1_St_state));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_5);
    bool res_NotLogicOP_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetInMainc3(my_id) == false));
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! res_NotLogicOP_7);
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_6);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_4);
    
    if(res_OrLogicOP_0){
    
    res_macro_val = giallox;
    }
    else{
    res_macro_val = giallox;
    }
    return res_macro_val;
}

/*
    CNL corrispondente:
    
    { commento: {[}  se il controllo ConsDef è uguale a FALSE  commento: {35,} e  se il controllo MainClass_C1_controllo_C7 è  uguale a  True  commento: {109,} o  se il ripristino della variabile  MainClass_C1_restoreva_RV3 è  diverso da Giallox e  se il controllo ConsDef è uguale a FALSE  e  se l'argomento argomento_a2 non  è  uguale a Verde commento: {39,}  o  se il ripristino dello stato  è  uguale a  commento: {53,}  state1  commento: {107,} , assegna alla macro il valore Verde
    
     commento: {46,} assegna alla macro il valore Verde commento: {],}
    }
*/
C1_Enumerat4 L_P1__Macro7(instance_id_t const my_id , C1_Enumerat4 argom13, C1_Enumerat3 argom14, C1_Enumerat3 argom15, C1_Enumerat3 argom16, C1_Enumerat3 argom17, bool argom18)
{
C1_Enumerat4 res_macro_val;
    
    //  *[*  se il controllo ConsDef è uguale a FALSE  *35,* e  se il controllo MainClass_C1_controllo_C7 è  uguale a  True  *109,* o  se il ripristino della variabile  MainClass_C1_restoreva_RV3 è  diverso da Giallox e  se il controllo ConsDef è uguale a FALSE  e  se l'argomento argomento_a2 non  è  uguale a Verde *39,*  o  se il ripristino dello stato  è  uguale a  *53,*  state1
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_AndLogicOP_2 = true;
    res_AndLogicOP_2 = (res_AndLogicOP_2 && (L_P1__GetInConsd(my_id) == false));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && (L_P1__GetInMainc3(my_id) == true));
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_2);
    bool res_AndLogicOP_3 = true;
    bool res_AndLogicOP_4 = true;
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetMainc29(my_id) == giallox));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_5);
    res_AndLogicOP_4 = (res_AndLogicOP_4 && (L_P1__GetInConsd(my_id) == false));
    
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_AndLogicOP_4);
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (argom13 == verde));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_6);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_3);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    res_OrLogicOP_0 = (res_OrLogicOP_0 || (L_P1__GetStato1(my_id) == C1_St_state));
    
    if(res_OrLogicOP_0){
    
    res_macro_val = verde;
    }
    else{
    res_macro_val = verde;
    }
    return res_macro_val;
}



