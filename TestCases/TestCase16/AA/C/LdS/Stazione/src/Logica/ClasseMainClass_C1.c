// Codice del modello 'TestCase16', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
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
    
     Nessuna  commento: {80,}
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
    
      se il ripristino dello stato  è  diverso da  commento: {56,}  state1  commento: {107,} commento: {35,} e  se il controllo MainClass_C1_controllo_C10 non è  diverso da  True  commento: {34,} e  se il parametro MainClass_C1_parametro_P9 è  uguale a c75Giallo,  Applica gli effetti
           della macro MainClass_C1_macroef_M1  commento: {73,}
    
       
      se il controllo ConsDef è uguale a FALSE  commento: {36,} o  se il timer MainClass_C1_timer_T7 non è attivo commento: {38,} e  se il contatore MainClass_C1_contatore_Co10 è  minore di  commento: {55,} 123 commento: {37,} e  se la variabile MainClass_C1_variabile_V9 è  uguale a c120x commento: {35,} e  se il controllo MainClass_C1_controllo_C6 è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE , commento: {71,}Decrementa il contatore MainClass_C1_contatore_Co9
    
       
     commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  minore di  commento: {55,} 9 commento: {34,} e  se il parametro MainClass_C1_parametro_P9 è  diverso da c75Giallo, commento: {70,}Incrementa il contatore MainClass_C1_contatore_Co9
    
     ,altrimenti  commento: {66,} Assegna al comando MainClass_C1_comando_C1 il valore  True 
    
    
      se il ripristino dello stato  non è  uguale a  commento: {53,}  state1  commento: {107,}, commento: {66,} Assegna al comando MainClass_C1_comando_C1 il valore  True 
    
       
     commento: {34,}  se il parametro MainClass_C1_parametro_P8 non è  minore di  commento: {55,} 8 commento: {37,} o  se la variabile MainClass_C1_variabile_V6 non è  uguale a c75Giallo commento: {36,} e  se il timer MainClass_C1_timer_T7 non è scaduto commento: {37,} o  se la variabile MainClass_C1_variabile_V9 è  uguale a c120x commento: {38,} o  se il contatore MainClass_C1_contatore_Co10 è  uguale a  commento: {53,} 1341, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V5 il valore  False 
    
     ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V6 il valore c75Giallo
    
    
    
    }
*/
static inline void L_P1__Effec1(instance_id_t const my_id)
{
    
    //  se il ripristino dello stato  è  diverso da  *56,*  state1  *107,* *35,* e  se il controllo MainClass_C1_controllo_C10 non è  diverso da  True  *34,* e  se il parametro MainClass_C1_parametro_P9 è  uguale a c75Giallo,  Applica gli effetti
    //         della macro MainClass_C1_macroef_M1
    bool res_AndLogicOP_0 = true;
    bool res_AndLogicOP_1 = true;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (L_P1__GetStato1(my_id) == C1_St_state));
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_2);
    bool res_NotLogicOP_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetInMainc5(my_id) == true));
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! res_NotLogicOP_4);
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_3);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_AndLogicOP_1);
    res_AndLogicOP_0 = (res_AndLogicOP_0 && (L_P1__GetParamMainc10(my_id) == c75giallo));
    
    if(res_AndLogicOP_0){
    
    L_P1__Macro(my_id);
    }
    
    //  *73,*
    //     
    //    se il controllo ConsDef è uguale a FALSE  *36,* o  se il timer MainClass_C1_timer_T7 non è attivo *38,* e  se il contatore MainClass_C1_contatore_Co10 è  minore di  *55,* 123 *37,* e  se la variabile MainClass_C1_variabile_V9 è  uguale a c120x *35,* e  se il controllo MainClass_C1_controllo_C6 è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE , *71,*Decrementa il contatore MainClass_C1_contatore_Co9
    bool res_OrLogicOP_5 = false;
    bool res_OrLogicOP_6 = false;
    res_OrLogicOP_6 = (res_OrLogicOP_6 || (L_P1__GetInConsd(my_id) == false));
    bool res_AndLogicOP_7 = true;
    bool res_AndLogicOP_8 = true;
    bool res_AndLogicOP_9 = true;
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! Timer_Attivo(L_P1__GetMainc38(my_id)));
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_NotLogicOP_10);
    res_AndLogicOP_9 = (res_AndLogicOP_9 && (Counter_GetValore(L_P1__GetMainc39(my_id)) < 123u));
    
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_AndLogicOP_9);
    res_AndLogicOP_8 = (res_AndLogicOP_8 && (L_P1__GetMainc29(my_id) == c120x));
    
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_AndLogicOP_8);
    res_AndLogicOP_7 = (res_AndLogicOP_7 && (L_P1__GetInMainc7(my_id) == false));
    
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_AndLogicOP_7);
    
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_OrLogicOP_6);
    res_OrLogicOP_5 = (res_OrLogicOP_5 || (L_P1__GetInConsd(my_id) == false));
    
    if(res_OrLogicOP_5){
    
    Counter_Decr(L_P1__GetMainc41(my_id));
    }
    
    //  *109,*  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  minore di  *55,* 9 *34,* e  se il parametro MainClass_C1_parametro_P9 è  diverso da c75Giallo, *70,*Incrementa il contatore MainClass_C1_contatore_Co9
    //   ,altrimenti  *66,* Assegna al comando MainClass_C1_comando_C1 il valore  True
    bool res_AndLogicOP_11 = true;
    res_AndLogicOP_11 = (res_AndLogicOP_11 && (L_P1__GetMainc18(my_id) < 9u));
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (L_P1__GetParamMainc10(my_id) == c75giallo));
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_NotLogicOP_12);
    
    if(res_AndLogicOP_11){
    
    Counter_Incr(L_P1__GetMainc41(my_id));
    }else{
    
    L_P1__SetOutMainc(my_id,true);
    }
    
    //  se il ripristino dello stato  non è  uguale a  *53,*  state1  *107,*, *66,* Assegna al comando MainClass_C1_comando_C1 il valore  True
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (L_P1__GetStato1(my_id) == C1_St_state));
    if(res_NotLogicOP_13){
    
    L_P1__SetOutMainc(my_id,true);
    }
    
    //  *34,*  se il parametro MainClass_C1_parametro_P8 non è  minore di  *55,* 8 *37,* o  se la variabile MainClass_C1_variabile_V6 non è  uguale a c75Giallo *36,* e  se il timer MainClass_C1_timer_T7 non è scaduto *37,* o  se la variabile MainClass_C1_variabile_V9 è  uguale a c120x *38,* o  se il contatore MainClass_C1_contatore_Co10 è  uguale a  *53,* 1341, *67,* Assegna alla variabile MainClass_C1_variabile_V5 il valore  False 
    //   ,altrimenti  *67,* Assegna alla variabile MainClass_C1_variabile_V6 il valore c75Giallo
    bool res_OrLogicOP_14 = false;
    bool res_OrLogicOP_15 = false;
    bool res_OrLogicOP_16 = false;
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! (L_P1__GetParamMainc9(my_id) < 8u));
    res_OrLogicOP_16 = (res_OrLogicOP_16 || res_NotLogicOP_17);
    bool res_AndLogicOP_18 = true;
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (L_P1__GetMainc28(my_id) == c75giallo));
    res_AndLogicOP_18 = (res_AndLogicOP_18 && res_NotLogicOP_19);
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! Timer_Scaduto(L_P1__GetMainc38(my_id)));
    res_AndLogicOP_18 = (res_AndLogicOP_18 && res_NotLogicOP_20);
    
    res_OrLogicOP_16 = (res_OrLogicOP_16 || res_AndLogicOP_18);
    
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_OrLogicOP_16);
    res_OrLogicOP_15 = (res_OrLogicOP_15 || (L_P1__GetMainc29(my_id) == c120x));
    
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_OrLogicOP_15);
    res_OrLogicOP_14 = (res_OrLogicOP_14 || (Counter_GetValore(L_P1__GetMainc39(my_id)) == 1341u));
    
    if(res_OrLogicOP_14){
    
    L_P1__SetMainc27(my_id,false);
    }else{
    
    L_P1__SetMainc28(my_id,c75giallo);
    }
}



// ********** Definizione metodi **********

// Metodi standard

void L_P1_C1_Init(instance_id_t const my_id)
{
    // init variabili di stato
    L_P1__SetMainc13(my_id, verde);
    L_P1__SetMainc15(my_id, 0);
    L_P1__SetMainc17(my_id, 0);
    L_P1__SetMainc18(my_id, 0);
    L_P1__SetMainc19(my_id, rossogiallo1);
    L_P1__SetMainc20(my_id, rossogiallo1);
    L_P1__SetMainc21(my_id, false);
    L_P1__SetMainc22(my_id, false);
    L_P1__SetMainc23(my_id, false);
    L_P1__SetMainc24(my_id, false);
    L_P1__SetMainc25(my_id, rossogiallo1);
    L_P1__SetMainc26(my_id, rossogiallo1);
    L_P1__SetMainc27(my_id, false);
    L_P1__SetMainc28(my_id, rosso);
    L_P1__SetMainc29(my_id, c180);
    L_P1__SetStato1(my_id, C1_St_Stato);
    // init controlli precedenti
    L_P1__SetMainc12(my_id, true);
    // init Timer e Counter
    Timer_AggmInit(L_P1__GetMainc30(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc30_ID);
    Timer_Init(L_P1__GetMainc30(my_id), 3000);
    Timer_AggmInit(L_P1__GetMainc31(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc31_ID);
    Timer_Init(L_P1__GetMainc31(my_id), 3000);
    Timer_AggmInit(L_P1__GetMainc32(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc32_ID);
    Timer_Init(L_P1__GetMainc32(my_id), 2000);
    Timer_AggmInit(L_P1__GetMainc33(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc33_ID);
    Timer_Init(L_P1__GetMainc33(my_id), 2000);
    Timer_AggmInit(L_P1__GetMainc34(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc34_ID);
    Timer_Init(L_P1__GetMainc34(my_id), 21320000);
    Timer_AggmInit(L_P1__GetMainc35(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc35_ID);
    Timer_Init(L_P1__GetMainc35(my_id), 21320000);
    Timer_AggmInit(L_P1__GetMainc36(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc36_ID);
    Timer_Init(L_P1__GetMainc36(my_id), 154000);
    Timer_AggmInit(L_P1__GetMainc37(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc37_ID);
    Timer_Init(L_P1__GetMainc37(my_id), 154000);
    Timer_AggmInit(L_P1__GetMainc38(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc38_ID);
    Timer_Init(L_P1__GetMainc38(my_id), 554000);
    Counter_AggmInit(L_P1__GetMainc39(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc39_ID);
    Counter_Init(L_P1__GetMainc39(my_id));
    Counter_AggmInit(L_P1__GetMainc40(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc40_ID);
    Counter_Init(L_P1__GetMainc40(my_id));
    Counter_AggmInit(L_P1__GetMainc41(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc41_ID);
    Counter_Init(L_P1__GetMainc41(my_id));
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
    L_P1__SetMainc14(my_id, L_P1__GetMainc13(my_id));
    L_P1__SetMainc16(my_id, L_P1__GetMainc15(my_id));
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
    Timer_Exec(L_P1__GetMainc30(my_id));
    Timer_Exec(L_P1__GetMainc31(my_id));
    Timer_Exec(L_P1__GetMainc32(my_id));
    Timer_Exec(L_P1__GetMainc33(my_id));
    Timer_Exec(L_P1__GetMainc34(my_id));
    Timer_Exec(L_P1__GetMainc35(my_id));
    Timer_Exec(L_P1__GetMainc36(my_id));
    Timer_Exec(L_P1__GetMainc37(my_id));
    Timer_Exec(L_P1__GetMainc38(my_id));
}

void L_P1_C1_GSetSafe(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C1(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C1(proc_id);
    L_P1__SetOutMainc(my_id, true);
    L_P1__SetOutMainc1(my_id, ac);
    L_P1__SetOutMainc2(my_id, rossogiallo2);
    L_P1__SetOutMainc3(my_id, c75giallo);
    L_P1__SetOutMainc4(my_id, false);
}

void L_P1_C1_GUpdatePrev(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C1(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C1(proc_id);
    L_P1__SetMainc12(my_id, L_P1__GetInMainc11(my_id));
    L_P1__SetMainc14(my_id, L_P1__GetMainc13(my_id));
    L_P1__SetMainc16(my_id, L_P1__GetMainc15(my_id));
}

// ********** Definizione macro **********

// Macro di effetto

/*
    CNL corrispondente:
    
    { commento: {35,}  se il controllo MainClass_C1_controllo_C6 è  diverso da  True  commento: {38,} e  se il contatore MainClass_C1_contatore_Co4 non è  uguale a  commento: {53,} 12 commento: {37,} o  se la variabile MainClass_C1_variabile_V6 non è  uguale a c75Giallo o  se il controllo ConsDef  è  uguale a FALSE , commento: {68,}Attiva il timer MainClass_C1_timer_T7
    
       
    
    }
*/
void L_P1__Macro(instance_id_t const my_id )
{
//  *35,*  se il controllo MainClass_C1_controllo_C6 è  diverso da  True  *38,* e  se il contatore MainClass_C1_contatore_Co4 non è  uguale a  *53,* 12 *37,* o  se la variabile MainClass_C1_variabile_V6 non è  uguale a c75Giallo o  se il controllo ConsDef  è  uguale a FALSE , *68,*Attiva il timer MainClass_C1_timer_T7
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_AndLogicOP_2 = true;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__GetInMainc7(my_id) == true));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_3);
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (Counter_GetValore(L_P1__GetMainc40(my_id)) == 12u));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_4);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_2);
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetMainc28(my_id) == c75giallo));
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_NotLogicOP_5);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    res_OrLogicOP_0 = (res_OrLogicOP_0 || (L_P1__GetInConsd(my_id) == false));
    
    if(res_OrLogicOP_0){
    
    Timer_Attiva(L_P1__GetMainc38(my_id));
    }
}

/*
    CNL corrispondente:
    
    { commento: {36,}  se il timer MainClass_C1_timer_T7 è attivo o  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} e  se il contatore MainClass_C1_contatore_Co4 non è  minore di  commento: {55,} 143 commento: {38,} o  se il contatore MainClass_C1_contatore_Co9 è  minore di  commento: {55,} 12205 o  se il controllo ConsDef  è  uguale a FALSE , commento: {67,} Assegna alla variabile MainClass_C1_variabile_V6 il valore c75Giallo
    
       
     commento: {35,}  se il controllo MainClass_C1_controllo_C6 è  diverso da  True  e  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} o  se la variabile MainClass_C1_variabile_V5 non è  uguale a  True  commento: {36,} o  se il timer MainClass_C1_timer_T7 non è disattivo e  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} o  se il controllo MainClass_C1_controllo_C10 è  diverso da  False , commento: {66,} Assegna al comando MainClass_C1_comando_C1 il valore  False 
    
       
     commento: {37,}  se la variabile MainClass_C1_variabile_V6 non è  uguale a c75Giallo commento: {35,} o  se il controllo MainClass_C1_controllo_C6 è  uguale a  False  commento: {34,} e  se il parametro MainClass_C1_parametro_P10 è  diverso da  False  commento: {38,} o  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  commento: {56,} 124 commento: {35,} o  se il controllo MainClass_C1_controllo_C6 è  uguale a  False , commento: {72,}Azzera il contatore MainClass_C1_contatore_Co9
    
       
     commento: {37,}  se la variabile MainClass_C1_variabile_V6 non è  diverso da c75Giallo commento: {38,} o  se il contatore MainClass_C1_contatore_Co9 non è  diverso da  commento: {56,} 131 o  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro MainClass_C1_parametro_P8 è  diverso da  commento: {56,} 10 commento: {36,} e  se il timer MainClass_C1_timer_T7 è scaduto commento: {36,} o  se il timer MainClass_C1_timer_T7 è disattivo, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V5 il valore  False 
    
       
      se il ripristino dello stato  non è  uguale a  commento: {53,}  state1  commento: {107,}, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V9 il valore c120x
    
     ,altrimenti  commento: {69,}Disattiva il timer MainClass_C1_timer_T7
    
    
    
    }
*/
void L_P1__Macro1(instance_id_t const my_id )
{
//  *36,*  se il timer MainClass_C1_timer_T7 è attivo o  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  *38,* e  se il contatore MainClass_C1_contatore_Co4 non è  minore di  *55,* 143 *38,* o  se il contatore MainClass_C1_contatore_Co9 è  minore di  *55,* 12205 o  se il controllo ConsDef  è  uguale a FALSE , *67,* Assegna alla variabile MainClass_C1_variabile_V6 il valore c75Giallo
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    res_OrLogicOP_3 = (res_OrLogicOP_3 || Timer_Attivo(L_P1__GetMainc38(my_id)));
    res_OrLogicOP_3 = (res_OrLogicOP_3 || (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    bool res_AndLogicOP_4 = true;
    res_AndLogicOP_4 = (res_AndLogicOP_4 && (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (Counter_GetValore(L_P1__GetMainc40(my_id)) < 143u));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_5);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_4);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_OrLogicOP_2);
    res_OrLogicOP_1 = (res_OrLogicOP_1 || (Counter_GetValore(L_P1__GetMainc41(my_id)) < 12205u));
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    res_OrLogicOP_0 = (res_OrLogicOP_0 || (L_P1__GetInConsd(my_id) == false));
    
    if(res_OrLogicOP_0){
    
    L_P1__SetMainc28(my_id,c75giallo);
    }
    //  *35,*  se il controllo MainClass_C1_controllo_C6 è  diverso da  True  e  se il controllo ConsDef  è  uguale a FALSE  *37,* o  se la variabile MainClass_C1_variabile_V5 non è  uguale a  True  *36,* o  se il timer MainClass_C1_timer_T7 non è disattivo e  se il controllo ConsDef  è  uguale a FALSE  *35,* o  se il controllo MainClass_C1_controllo_C10 è  diverso da  False , *66,* Assegna al comando MainClass_C1_comando_C1 il valore  False
    bool res_OrLogicOP_6 = false;
    bool res_OrLogicOP_7 = false;
    bool res_OrLogicOP_8 = false;
    bool res_AndLogicOP_9 = true;
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__GetInMainc7(my_id) == true));
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_NotLogicOP_10);
    res_AndLogicOP_9 = (res_AndLogicOP_9 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_AndLogicOP_9);
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (L_P1__GetMainc27(my_id) == true));
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_NotLogicOP_11);
    
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_OrLogicOP_8);
    bool res_AndLogicOP_12 = true;
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! Timer_Disattivo(L_P1__GetMainc38(my_id)));
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_NotLogicOP_13);
    res_AndLogicOP_12 = (res_AndLogicOP_12 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_AndLogicOP_12);
    
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_OrLogicOP_7);
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1__GetInMainc5(my_id) == false));
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_NotLogicOP_14);
    
    if(res_OrLogicOP_6){
    
    L_P1__SetOutMainc(my_id,false);
    }
    //  *37,*  se la variabile MainClass_C1_variabile_V6 non è  uguale a c75Giallo *35,* o  se il controllo MainClass_C1_controllo_C6 è  uguale a  False  *34,* e  se il parametro MainClass_C1_parametro_P10 è  diverso da  False  *38,* o  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  *56,* 124 *35,* o  se il controllo MainClass_C1_controllo_C6 è  uguale a  False , *72,*Azzera il contatore MainClass_C1_contatore_Co9
    bool res_OrLogicOP_15 = false;
    bool res_OrLogicOP_16 = false;
    bool res_OrLogicOP_17 = false;
    bool res_NotLogicOP_18 = true;
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! (L_P1__GetMainc28(my_id) == c75giallo));
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_NotLogicOP_18);
    bool res_AndLogicOP_19 = true;
    res_AndLogicOP_19 = (res_AndLogicOP_19 && (L_P1__GetInMainc7(my_id) == false));
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! (L_P1__GetParamMainc8(my_id) == false));
    res_AndLogicOP_19 = (res_AndLogicOP_19 && res_NotLogicOP_20);
    
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_AndLogicOP_19);
    
    res_OrLogicOP_16 = (res_OrLogicOP_16 || res_OrLogicOP_17);
    bool res_NotLogicOP_21 = true;
    bool res_NotLogicOP_22 = true;
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! (Counter_GetValore(L_P1__GetMainc40(my_id)) == 124u));
    res_NotLogicOP_21 = (res_NotLogicOP_21 && ! res_NotLogicOP_22);
    res_OrLogicOP_16 = (res_OrLogicOP_16 || res_NotLogicOP_21);
    
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_OrLogicOP_16);
    res_OrLogicOP_15 = (res_OrLogicOP_15 || (L_P1__GetInMainc7(my_id) == false));
    
    if(res_OrLogicOP_15){
    
    Counter_Res(L_P1__GetMainc41(my_id));
    }
    //  *37,*  se la variabile MainClass_C1_variabile_V6 non è  diverso da c75Giallo *38,* o  se il contatore MainClass_C1_contatore_Co9 non è  diverso da  *56,* 131 o  se il controllo ConsDef  è  uguale a FALSE  *34,* e  se il parametro MainClass_C1_parametro_P8 è  diverso da  *56,* 10 *36,* e  se il timer MainClass_C1_timer_T7 è scaduto *36,* o  se il timer MainClass_C1_timer_T7 è disattivo, *67,* Assegna alla variabile MainClass_C1_variabile_V5 il valore  False
    bool res_OrLogicOP_23 = false;
    bool res_OrLogicOP_24 = false;
    bool res_OrLogicOP_25 = false;
    bool res_NotLogicOP_26 = true;
    bool res_NotLogicOP_27 = true;
    res_NotLogicOP_27 = (res_NotLogicOP_27 && ! (L_P1__GetMainc28(my_id) == c75giallo));
    res_NotLogicOP_26 = (res_NotLogicOP_26 && ! res_NotLogicOP_27);
    res_OrLogicOP_25 = (res_OrLogicOP_25 || res_NotLogicOP_26);
    bool res_NotLogicOP_28 = true;
    bool res_NotLogicOP_29 = true;
    res_NotLogicOP_29 = (res_NotLogicOP_29 && ! (Counter_GetValore(L_P1__GetMainc41(my_id)) == 131u));
    res_NotLogicOP_28 = (res_NotLogicOP_28 && ! res_NotLogicOP_29);
    res_OrLogicOP_25 = (res_OrLogicOP_25 || res_NotLogicOP_28);
    
    res_OrLogicOP_24 = (res_OrLogicOP_24 || res_OrLogicOP_25);
    bool res_AndLogicOP_30 = true;
    bool res_AndLogicOP_31 = true;
    res_AndLogicOP_31 = (res_AndLogicOP_31 && (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_32 = true;
    res_NotLogicOP_32 = (res_NotLogicOP_32 && ! (L_P1__GetParamMainc9(my_id) == 10u));
    res_AndLogicOP_31 = (res_AndLogicOP_31 && res_NotLogicOP_32);
    
    res_AndLogicOP_30 = (res_AndLogicOP_30 && res_AndLogicOP_31);
    res_AndLogicOP_30 = (res_AndLogicOP_30 && Timer_Scaduto(L_P1__GetMainc38(my_id)));
    
    res_OrLogicOP_24 = (res_OrLogicOP_24 || res_AndLogicOP_30);
    
    res_OrLogicOP_23 = (res_OrLogicOP_23 || res_OrLogicOP_24);
    res_OrLogicOP_23 = (res_OrLogicOP_23 || Timer_Disattivo(L_P1__GetMainc38(my_id)));
    
    if(res_OrLogicOP_23){
    
    L_P1__SetMainc27(my_id,false);
    }
    //  se il ripristino dello stato  non è  uguale a  *53,*  state1  *107,*, *67,* Assegna alla variabile MainClass_C1_variabile_V9 il valore c120x
    // ,altrimenti  *69,*Disattiva il timer MainClass_C1_timer_T7
    bool res_NotLogicOP_33 = true;
    res_NotLogicOP_33 = (res_NotLogicOP_33 && ! (L_P1__GetStato1(my_id) == C1_St_state));
    if(res_NotLogicOP_33){
    
    L_P1__SetMainc29(my_id,c120x);
    }else{
    
    Timer_Disattiva(L_P1__GetMainc38(my_id));
    }
}

/*
    CNL corrispondente:
    
    { commento: {38,}  se il contatore MainClass_C1_contatore_Co4 è  minore di  commento: {55,} 14 commento: {38,} o  se il contatore MainClass_C1_contatore_Co10 non è  maggiore di  commento: {54,} 14054 commento: {37,} e  se la variabile MainClass_C1_variabile_V9 è  uguale a c120x,  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V5 il valore  False commento: {67,}
    
       
      se il ripristino dello stato  non è  uguale a  commento: {53,}  state1  commento: {107,} commento: {34,} e  se il parametro MainClass_C1_parametro_P9 è  diverso da c75Giallo commento: {34,} o  se il parametro MainClass_C1_parametro_P9 non è  uguale a c75Giallo commento: {35,} o  se il controllo MainClass_C1_controllo_C10 è  uguale a  False  commento: {38,} e  se il contatore MainClass_C1_contatore_Co10 non è  uguale a  commento: {53,} 12,  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V5 il valore  True  commento: {67,}
    
       
    
    }
*/
void L_P1__Macro2(instance_id_t const my_id )
{
//  *38,*  se il contatore MainClass_C1_contatore_Co4 è  minore di  *55,* 14 *38,* o  se il contatore MainClass_C1_contatore_Co10 non è  maggiore di  *54,* 14054 *37,* e  se la variabile MainClass_C1_variabile_V9 è  uguale a c120x,  *67,* Assegna alla variabile MainClass_C1_variabile_V5 il valore  False
    bool res_OrLogicOP_0 = false;
    res_OrLogicOP_0 = (res_OrLogicOP_0 || (Counter_GetValore(L_P1__GetMainc40(my_id)) < 14u));
    bool res_AndLogicOP_1 = true;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (Counter_GetValore(L_P1__GetMainc39(my_id)) > 14054u));
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_2);
    res_AndLogicOP_1 = (res_AndLogicOP_1 && (L_P1__GetMainc29(my_id) == c120x));
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_1);
    
    if(res_OrLogicOP_0){
    
    L_P1__SetMainc27(my_id,false);
    }
    //  *67,*
    //   
    //  se il ripristino dello stato  non è  uguale a  *53,*  state1  *107,* *34,* e  se il parametro MainClass_C1_parametro_P9 è  diverso da c75Giallo *34,* o  se il parametro MainClass_C1_parametro_P9 non è  uguale a c75Giallo *35,* o  se il controllo MainClass_C1_controllo_C10 è  uguale a  False  *38,* e  se il contatore MainClass_C1_contatore_Co10 non è  uguale a  *53,* 12,  *67,* Assegna alla variabile MainClass_C1_variabile_V5 il valore  True
    bool res_OrLogicOP_3 = false;
    bool res_OrLogicOP_4 = false;
    bool res_AndLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetStato1(my_id) == C1_St_state));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_6);
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetParamMainc10(my_id) == c75giallo));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_7);
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_AndLogicOP_5);
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetParamMainc10(my_id) == c75giallo));
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_NotLogicOP_8);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_OrLogicOP_4);
    bool res_AndLogicOP_9 = true;
    res_AndLogicOP_9 = (res_AndLogicOP_9 && (L_P1__GetInMainc5(my_id) == false));
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (Counter_GetValore(L_P1__GetMainc39(my_id)) == 12u));
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_NotLogicOP_10);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_AndLogicOP_9);
    
    if(res_OrLogicOP_3){
    
    L_P1__SetMainc27(my_id,true);
    }
}

/*
    CNL corrispondente:
    
    {  se il controllo ConsDef è uguale a FALSE  commento: {35,} e  se il controllo MainClass_C1_controllo_C10 è  diverso da  False  commento: {36,} e  se il timer MainClass_C1_timer_T7 è disattivo e  se il controllo ConsDef  è  uguale a FALSE , commento: {66,} Assegna al comando MainClass_C1_comando_C1 il valore  False 
    
       
    
    }
*/
void L_P1__Macro3(instance_id_t const my_id )
{
//  se il controllo ConsDef è uguale a FALSE  *35,* e  se il controllo MainClass_C1_controllo_C10 è  diverso da  False  *36,* e  se il timer MainClass_C1_timer_T7 è disattivo e  se il controllo ConsDef  è  uguale a FALSE , *66,* Assegna al comando MainClass_C1_comando_C1 il valore  False
    bool res_AndLogicOP_0 = true;
    bool res_AndLogicOP_1 = true;
    bool res_AndLogicOP_2 = true;
    res_AndLogicOP_2 = (res_AndLogicOP_2 && (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__GetInMainc5(my_id) == false));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_3);
    
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_AndLogicOP_2);
    res_AndLogicOP_1 = (res_AndLogicOP_1 && Timer_Disattivo(L_P1__GetMainc38(my_id)));
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_AndLogicOP_1);
    res_AndLogicOP_0 = (res_AndLogicOP_0 && (L_P1__GetInConsd(my_id) == false));
    
    if(res_AndLogicOP_0){
    
    L_P1__SetOutMainc(my_id,false);
    }
}


// Macro di verifica

/*
    CNL corrispondente:
     
    {  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} o  se il controllo MainClass_C1_controllo_C10 è  uguale a  False , Verifica che   commento: {47,48,50,}  commento: {,}  la variabile MainClass_C1_variabile_V5 non sia  uguale a  True 
     commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P10 sia  diverso da  False 
     commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
    
    
    }
*/
bool L_P1__Macro9(instance_id_t const my_id )
{
bool res_AndLogicOP_0 = true;
    
    //  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  *35,* o  se il controllo MainClass_C1_controllo_C10 è  uguale a  False , Verifica che   *47,48,50,*  *,*  la variabile MainClass_C1_variabile_V5 non sia  uguale a  True 
    //   *104,* e  che   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* e  che  *34,*  il parametro MainClass_C1_parametro_P10 sia  diverso da  False 
    //   *104,* e  che   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* e  che   il controllo ConsDef  sia  uguale a FALSE
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_AndLogicOP_3 = true;
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (L_P1__GetInConsd(my_id) == false));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_3);
    res_OrLogicOP_2 = (res_OrLogicOP_2 || (L_P1__GetInMainc5(my_id) == false));
    
    if(res_OrLogicOP_2){
    bool res_AndLogicOP_4 = true;
    bool res_AndLogicOP_5 = true;
    bool res_AndLogicOP_6 = true;
    bool res_AndLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetMainc27(my_id) == true));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_8);
    res_AndLogicOP_7 = (res_AndLogicOP_7 && (L_P1__GetInConsd(my_id) == false));
    
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_AndLogicOP_7);
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetParamMainc8(my_id) == false));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_9);
    
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_AndLogicOP_6);
    res_AndLogicOP_5 = (res_AndLogicOP_5 && (L_P1__GetInConsd(my_id) == false));
    
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_AndLogicOP_5);
    res_AndLogicOP_4 = (res_AndLogicOP_4 && (L_P1__GetInConsd(my_id) == false));
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_AndLogicOP_4);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
     
    { commento: {37,}  se la variabile MainClass_C1_variabile_V6 è  diverso da c75Giallo, Verifica che   commento: {48,49,50,}  commento: {,}  il controllo MainClass_C1_controllo_C2 non sia  diverso da  False 
     commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T7 non sia attivo
     commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V9 non sia  uguale a c120x
     commento: {104,} e  che  commento: {37,}  la variabile MainClass_C1_variabile_V5 non sia  uguale a  False 
    
    
    }
*/
bool L_P1__Macro10(instance_id_t const my_id )
{
bool res_AndLogicOP_0 = true;
    
    //  *37,*  se la variabile MainClass_C1_variabile_V6 è  diverso da c75Giallo, Verifica che   *48,49,50,*  *,*  il controllo MainClass_C1_controllo_C2 non sia  diverso da  False 
    //   *104,* e  che  *,*  il timer MainClass_C1_timer_T7 non sia attivo
    //   *104,* e  che  *,*  la variabile MainClass_C1_variabile_V9 non sia  uguale a c120x
    //   *104,* e  che  *37,*  la variabile MainClass_C1_variabile_V5 non sia  uguale a  False
    bool res_ImpliesLogicOp_1 = true;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (L_P1__GetMainc28(my_id) == c75giallo));
    if(res_NotLogicOP_2){
    bool res_AndLogicOP_3 = true;
    bool res_AndLogicOP_4 = true;
    bool res_AndLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetInMainc6(my_id) == false));
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! res_NotLogicOP_7);
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_6);
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! Timer_Attivo(L_P1__GetMainc38(my_id)));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_8);
    
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_AndLogicOP_5);
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetMainc29(my_id) == c120x));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_9);
    
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_AndLogicOP_4);
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__GetMainc27(my_id) == false));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_10);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_AndLogicOP_3);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
     
    { commento: {62,} commento: {34,}  se il parametro MainClass_C1_parametro_P9 è  uguale a c75Giallo e  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
     commento: {61,} commento: {34,}  se il parametro MainClass_C1_parametro_P9 è  uguale a c75Giallo commento: {35,} e  se il controllo MainClass_C1_controllo_C6 non è  diverso da  True  commento: {38,} e  se il contatore MainClass_C1_contatore_Co10 non è  minore di  commento: {55,} 132 commento: {35,} e  se il controllo MainClass_C1_controllo_C10 non è  uguale a  True  commento: {34,} e  se il parametro MainClass_C1_parametro_P8 è  uguale a  commento: {53,} 2 o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
     commento: {61,} commento: {34,}  se il parametro MainClass_C1_parametro_P9 è  diverso da c75Giallo commento: {38,} o  se il contatore MainClass_C1_contatore_Co9 non è  maggiore di  commento: {54,} 14054 commento: {35,} e  se il controllo MainClass_C1_controllo_C2 non è  diverso da  True  commento: {36,} e  se il timer MainClass_C1_timer_T7 è attivo e  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
      se il controllo ConsDef è uguale a FALSE , Verifica che   commento: {48,49,50,51,}  commento: {,}  il timer MainClass_C1_timer_T7 sia disattivo
     commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V6 non sia  uguale a c75Giallo
     commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co10 non sia  uguale a  commento: {53,} 122054
     commento: {104,} e  che  commento: {36,}  il timer MainClass_C1_timer_T7 non sia attivo
     commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
    
    
     } Verifica che   commento: {47,48,50,}  commento: {34,}  il parametro MainClass_C1_parametro_P9 sia  diverso da c75Giallo
     commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V6 sia  diverso da c75Giallo
     commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C2 non sia  uguale a  False 
     commento: {104,} e  che  commento: {37,}  la variabile MainClass_C1_variabile_V6 sia  diverso da c75Giallo
    
    
     } Verifica che   commento: {47,50,}  commento: {,}  la variabile MainClass_C1_variabile_V9 sia  diverso da c120x
     commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P9 non sia  uguale a c75Giallo
    
    
     } Verifica che   commento: {47,50,51,}  commento: {34,}  il parametro MainClass_C1_parametro_P9 non sia  diverso da c75Giallo
     commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co10 sia  minore di  commento: {55,} 13
     commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V5 non sia  uguale a  False 
     commento: {104,} o  che  commento: {37,}  la variabile MainClass_C1_variabile_V9 sia  diverso da c120x
    
    
    }
*/
bool L_P1__Macro11(instance_id_t const my_id )
{
bool res_AndLogicOP_0 = true;
    
    //  *62,* *34,*  se il parametro MainClass_C1_parametro_P9 è  uguale a c75Giallo e  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
    //   *61,* *34,*  se il parametro MainClass_C1_parametro_P9 è  uguale a c75Giallo *35,* e  se il controllo MainClass_C1_controllo_C6 non è  diverso da  True  *38,* e  se il contatore MainClass_C1_contatore_Co10 non è  minore di  *55,* 132 *35,* e  se il controllo MainClass_C1_controllo_C10 non è  uguale a  True  *34,* e  se il parametro MainClass_C1_parametro_P8 è  uguale a  *53,* 2 o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
    //   *61,* *34,*  se il parametro MainClass_C1_parametro_P9 è  diverso da c75Giallo *38,* o  se il contatore MainClass_C1_contatore_Co9 non è  maggiore di  *54,* 14054 *35,* e  se il controllo MainClass_C1_controllo_C2 non è  diverso da  True  *36,* e  se il timer MainClass_C1_timer_T7 è attivo e  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
    //    se il controllo ConsDef è uguale a FALSE , Verifica che   *48,49,50,51,*  *,*  il timer MainClass_C1_timer_T7 sia disattivo
    //   *104,* o  che  *,*  la variabile MainClass_C1_variabile_V6 non sia  uguale a c75Giallo
    //   *104,* o  che   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* e  che  *,*  il contatore MainClass_C1_contatore_Co10 non sia  uguale a  *53,* 122054
    //   *104,* e  che  *36,*  il timer MainClass_C1_timer_T7 non sia attivo
    //   *104,* o  che   il controllo ConsDef  sia  uguale a FALSE 
    //   } Verifica che   *47,48,50,*  *34,*  il parametro MainClass_C1_parametro_P9 sia  diverso da c75Giallo
    //   *104,* o  che  *,*  la variabile MainClass_C1_variabile_V6 sia  diverso da c75Giallo
    //   *104,* o  che  *,*  il controllo MainClass_C1_controllo_C2 non sia  uguale a  False 
    //   *104,* e  che  *37,*  la variabile MainClass_C1_variabile_V6 sia  diverso da c75Giallo
    //   } Verifica che   *47,50,*  *,*  la variabile MainClass_C1_variabile_V9 sia  diverso da c120x
    //   *104,* e  che  *34,*  il parametro MainClass_C1_parametro_P9 non sia  uguale a c75Giallo
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_AndLogicOP_2 = true;
    res_AndLogicOP_2 = (res_AndLogicOP_2 && (L_P1__GetParamMainc10(my_id) == c75giallo));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && (L_P1__GetInConsd(my_id) == false));
    
    if(res_AndLogicOP_2){
    bool res_OrLogicOP_3 = false;
    bool res_ImpliesLogicOp_4 = true;
    bool res_OrLogicOP_5 = false;
    bool res_AndLogicOP_6 = true;
    bool res_AndLogicOP_7 = true;
    bool res_AndLogicOP_8 = true;
    bool res_AndLogicOP_9 = true;
    res_AndLogicOP_9 = (res_AndLogicOP_9 && (L_P1__GetParamMainc10(my_id) == c75giallo));
    bool res_NotLogicOP_10 = true;
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (L_P1__GetInMainc7(my_id) == true));
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! res_NotLogicOP_11);
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_NotLogicOP_10);
    
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_AndLogicOP_9);
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (Counter_GetValore(L_P1__GetMainc39(my_id)) < 132u));
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_12);
    
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_AndLogicOP_8);
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (L_P1__GetInMainc5(my_id) == true));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_13);
    
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_AndLogicOP_7);
    res_AndLogicOP_6 = (res_AndLogicOP_6 && (L_P1__GetParamMainc9(my_id) == 2u));
    
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_AndLogicOP_6);
    res_OrLogicOP_5 = (res_OrLogicOP_5 || (L_P1__GetInConsd(my_id) == false));
    
    if(res_OrLogicOP_5){
    bool res_AndLogicOP_14 = true;
    bool res_ImpliesLogicOp_15 = true;
    bool res_OrLogicOP_16 = false;
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! (L_P1__GetParamMainc10(my_id) == c75giallo));
    res_OrLogicOP_16 = (res_OrLogicOP_16 || res_NotLogicOP_17);
    bool res_AndLogicOP_18 = true;
    bool res_AndLogicOP_19 = true;
    bool res_AndLogicOP_20 = true;
    bool res_NotLogicOP_21 = true;
    res_NotLogicOP_21 = (res_NotLogicOP_21 && ! (Counter_GetValore(L_P1__GetMainc41(my_id)) > 14054u));
    res_AndLogicOP_20 = (res_AndLogicOP_20 && res_NotLogicOP_21);
    bool res_NotLogicOP_22 = true;
    bool res_NotLogicOP_23 = true;
    res_NotLogicOP_23 = (res_NotLogicOP_23 && ! (L_P1__GetInMainc6(my_id) == true));
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! res_NotLogicOP_23);
    res_AndLogicOP_20 = (res_AndLogicOP_20 && res_NotLogicOP_22);
    
    res_AndLogicOP_19 = (res_AndLogicOP_19 && res_AndLogicOP_20);
    res_AndLogicOP_19 = (res_AndLogicOP_19 && Timer_Attivo(L_P1__GetMainc38(my_id)));
    
    res_AndLogicOP_18 = (res_AndLogicOP_18 && res_AndLogicOP_19);
    res_AndLogicOP_18 = (res_AndLogicOP_18 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_16 = (res_OrLogicOP_16 || res_AndLogicOP_18);
    
    if(res_OrLogicOP_16){
    bool res_ImpliesLogicOp_24 = true;
    if((L_P1__GetInConsd(my_id) == false)){
    bool res_OrLogicOP_25 = false;
    bool res_OrLogicOP_26 = false;
    bool res_OrLogicOP_27 = false;
    res_OrLogicOP_27 = (res_OrLogicOP_27 || Timer_Disattivo(L_P1__GetMainc38(my_id)));
    bool res_NotLogicOP_28 = true;
    res_NotLogicOP_28 = (res_NotLogicOP_28 && ! (L_P1__GetMainc28(my_id) == c75giallo));
    res_OrLogicOP_27 = (res_OrLogicOP_27 || res_NotLogicOP_28);
    
    res_OrLogicOP_26 = (res_OrLogicOP_26 || res_OrLogicOP_27);
    bool res_AndLogicOP_29 = true;
    bool res_AndLogicOP_30 = true;
    res_AndLogicOP_30 = (res_AndLogicOP_30 && (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_31 = true;
    res_NotLogicOP_31 = (res_NotLogicOP_31 && ! (Counter_GetValore(L_P1__GetMainc39(my_id)) == 122054u));
    res_AndLogicOP_30 = (res_AndLogicOP_30 && res_NotLogicOP_31);
    
    res_AndLogicOP_29 = (res_AndLogicOP_29 && res_AndLogicOP_30);
    bool res_NotLogicOP_32 = true;
    res_NotLogicOP_32 = (res_NotLogicOP_32 && ! Timer_Attivo(L_P1__GetMainc38(my_id)));
    res_AndLogicOP_29 = (res_AndLogicOP_29 && res_NotLogicOP_32);
    
    res_OrLogicOP_26 = (res_OrLogicOP_26 || res_AndLogicOP_29);
    
    res_OrLogicOP_25 = (res_OrLogicOP_25 || res_OrLogicOP_26);
    res_OrLogicOP_25 = (res_OrLogicOP_25 || (L_P1__GetInConsd(my_id) == false));
    
    res_ImpliesLogicOp_24 = (res_ImpliesLogicOp_24 && res_OrLogicOP_25);
    }
    res_ImpliesLogicOp_15 = (res_ImpliesLogicOp_15 && res_ImpliesLogicOp_24);
    }
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_ImpliesLogicOp_15);
    bool res_OrLogicOP_33 = false;
    bool res_OrLogicOP_34 = false;
    bool res_NotLogicOP_35 = true;
    res_NotLogicOP_35 = (res_NotLogicOP_35 && ! (L_P1__GetParamMainc10(my_id) == c75giallo));
    res_OrLogicOP_34 = (res_OrLogicOP_34 || res_NotLogicOP_35);
    bool res_NotLogicOP_36 = true;
    res_NotLogicOP_36 = (res_NotLogicOP_36 && ! (L_P1__GetMainc28(my_id) == c75giallo));
    res_OrLogicOP_34 = (res_OrLogicOP_34 || res_NotLogicOP_36);
    
    res_OrLogicOP_33 = (res_OrLogicOP_33 || res_OrLogicOP_34);
    bool res_AndLogicOP_37 = true;
    bool res_NotLogicOP_38 = true;
    res_NotLogicOP_38 = (res_NotLogicOP_38 && ! (L_P1__GetInMainc6(my_id) == false));
    res_AndLogicOP_37 = (res_AndLogicOP_37 && res_NotLogicOP_38);
    bool res_NotLogicOP_39 = true;
    res_NotLogicOP_39 = (res_NotLogicOP_39 && ! (L_P1__GetMainc28(my_id) == c75giallo));
    res_AndLogicOP_37 = (res_AndLogicOP_37 && res_NotLogicOP_39);
    
    res_OrLogicOP_33 = (res_OrLogicOP_33 || res_AndLogicOP_37);
    
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_OrLogicOP_33);
    
    res_ImpliesLogicOp_4 = (res_ImpliesLogicOp_4 && res_AndLogicOP_14);
    }
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_ImpliesLogicOp_4);
    bool res_AndLogicOP_40 = true;
    bool res_NotLogicOP_41 = true;
    res_NotLogicOP_41 = (res_NotLogicOP_41 && ! (L_P1__GetMainc29(my_id) == c120x));
    res_AndLogicOP_40 = (res_AndLogicOP_40 && res_NotLogicOP_41);
    bool res_NotLogicOP_42 = true;
    res_NotLogicOP_42 = (res_NotLogicOP_42 && ! (L_P1__GetParamMainc10(my_id) == c75giallo));
    res_AndLogicOP_40 = (res_AndLogicOP_40 && res_NotLogicOP_42);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_AndLogicOP_40);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_OrLogicOP_3);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *47,50,51,*  *34,*  il parametro MainClass_C1_parametro_P9 non sia  diverso da c75Giallo
    //   *104,* e  che  *,*  il contatore MainClass_C1_contatore_Co10 sia  minore di  *55,* 13
    //   *104,* o  che  *,*  la variabile MainClass_C1_variabile_V5 non sia  uguale a  False 
    //   *104,* o  che  *37,*  la variabile MainClass_C1_variabile_V9 sia  diverso da c120x
    bool res_OrLogicOP_43 = false;
    bool res_OrLogicOP_44 = false;
    bool res_AndLogicOP_45 = true;
    bool res_NotLogicOP_46 = true;
    bool res_NotLogicOP_47 = true;
    res_NotLogicOP_47 = (res_NotLogicOP_47 && ! (L_P1__GetParamMainc10(my_id) == c75giallo));
    res_NotLogicOP_46 = (res_NotLogicOP_46 && ! res_NotLogicOP_47);
    res_AndLogicOP_45 = (res_AndLogicOP_45 && res_NotLogicOP_46);
    res_AndLogicOP_45 = (res_AndLogicOP_45 && (Counter_GetValore(L_P1__GetMainc39(my_id)) < 13u));
    
    res_OrLogicOP_44 = (res_OrLogicOP_44 || res_AndLogicOP_45);
    bool res_NotLogicOP_48 = true;
    res_NotLogicOP_48 = (res_NotLogicOP_48 && ! (L_P1__GetMainc27(my_id) == false));
    res_OrLogicOP_44 = (res_OrLogicOP_44 || res_NotLogicOP_48);
    
    res_OrLogicOP_43 = (res_OrLogicOP_43 || res_OrLogicOP_44);
    bool res_NotLogicOP_49 = true;
    res_NotLogicOP_49 = (res_NotLogicOP_49 && ! (L_P1__GetMainc29(my_id) == c120x));
    res_OrLogicOP_43 = (res_OrLogicOP_43 || res_NotLogicOP_49);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_43);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
     
    { commento: {62,}  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} e  se il timer MainClass_C1_timer_T7 è scaduto commento: {36,} e  se il timer MainClass_C1_timer_T7 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} o  se il controllo MainClass_C1_controllo_C2 non è  uguale a  False , Almeno una delle seguenti { 
     commento: {63,} commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  diverso da  commento: {56,} 3 commento: {38,} e  se il contatore MainClass_C1_contatore_Co4 è  minore di  commento: {55,} 11 o  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} o  se il contatore MainClass_C1_contatore_Co4 è  uguale a  commento: {53,} 1213, Solo una delle seguenti { 
     commento: {36,}  se il timer MainClass_C1_timer_T7 non è scaduto commento: {38,} o  se il contatore MainClass_C1_contatore_Co4 è  uguale a  commento: {53,} 13205 commento: {35,} o  se il controllo MainClass_C1_controllo_C2 è  uguale a  True  commento: {34,} o  se il parametro MainClass_C1_parametro_P10 è  diverso da  False , Verifica che   commento: {48,50,}  commento: {,}  la variabile MainClass_C1_variabile_V9 non sia  diverso da c120x
     commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
    
    
     } Verifica che   commento: {47,48,51,}  commento: {34,}  il parametro MainClass_C1_parametro_P8 sia  uguale a  commento: {53,} 6
     commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C2 sia  diverso da  False 
     commento: {104,} o  che  commento: {,}  il contatore MainClass_C1_contatore_Co10 non sia  uguale a  commento: {53,} 15
     commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P9 non sia  diverso da c75Giallo
    
    
     } Verifica che   commento: {47,51,}  commento: {,}  il contatore MainClass_C1_contatore_Co10 sia  minore di  commento: {55,} 113
     commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P8 non sia  uguale a  commento: {53,} 6
    
    
    }
*/
bool L_P1__Macro12(instance_id_t const my_id )
{
bool res_AndLogicOP_0 = true;
    
    //  *62,*  se il controllo ConsDef  è  uguale a FALSE  *36,* e  se il timer MainClass_C1_timer_T7 è scaduto *36,* e  se il timer MainClass_C1_timer_T7 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  *35,* o  se il controllo MainClass_C1_controllo_C2 non è  uguale a  False , Almeno una delle seguenti { 
    //   *63,* *109,*  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  diverso da  *56,* 3 *38,* e  se il contatore MainClass_C1_contatore_Co4 è  minore di  *55,* 11 o  se il controllo ConsDef  è  uguale a FALSE  *38,* o  se il contatore MainClass_C1_contatore_Co4 è  uguale a  *53,* 1213, Solo una delle seguenti { 
    //   *36,*  se il timer MainClass_C1_timer_T7 non è scaduto *38,* o  se il contatore MainClass_C1_contatore_Co4 è  uguale a  *53,* 13205 *35,* o  se il controllo MainClass_C1_controllo_C2 è  uguale a  True  *34,* o  se il parametro MainClass_C1_parametro_P10 è  diverso da  False , Verifica che   *48,50,*  *,*  la variabile MainClass_C1_variabile_V9 non sia  diverso da c120x
    //   *104,* e  che   il controllo ConsDef  sia  uguale a FALSE 
    //   } Verifica che   *47,48,51,*  *34,*  il parametro MainClass_C1_parametro_P8 sia  uguale a  *53,* 6
    //   *104,* o  che  *,*  il controllo MainClass_C1_controllo_C2 sia  diverso da  False 
    //   *104,* o  che  *,*  il contatore MainClass_C1_contatore_Co10 non sia  uguale a  *53,* 15
    //   *104,* o  che  *34,*  il parametro MainClass_C1_parametro_P9 non sia  diverso da c75Giallo
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_AndLogicOP_3 = true;
    bool res_AndLogicOP_4 = true;
    bool res_AndLogicOP_5 = true;
    res_AndLogicOP_5 = (res_AndLogicOP_5 && (L_P1__GetInConsd(my_id) == false));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && Timer_Scaduto(L_P1__GetMainc38(my_id)));
    
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_AndLogicOP_5);
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! Timer_Scaduto(L_P1__GetMainc38(my_id)));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_6);
    
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_AndLogicOP_4);
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_3);
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetInMainc6(my_id) == false));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_7);
    
    if(res_OrLogicOP_2){
    bool res_OrLogicOP_8 = false;
    bool res_ImpliesLogicOp_9 = true;
    bool res_OrLogicOP_10 = false;
    bool res_OrLogicOP_11 = false;
    bool res_AndLogicOP_12 = true;
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (L_P1__GetMainc18(my_id) == 3u));
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_NotLogicOP_13);
    res_AndLogicOP_12 = (res_AndLogicOP_12 && (Counter_GetValore(L_P1__GetMainc40(my_id)) < 11u));
    
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_AndLogicOP_12);
    res_OrLogicOP_11 = (res_OrLogicOP_11 || (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_OrLogicOP_11);
    res_OrLogicOP_10 = (res_OrLogicOP_10 || (Counter_GetValore(L_P1__GetMainc40(my_id)) == 1213u));
    
    if(res_OrLogicOP_10){
    bool res_ImpliesLogicOp_14 = true;
    bool res_OrLogicOP_15 = false;
    bool res_OrLogicOP_16 = false;
    bool res_OrLogicOP_17 = false;
    bool res_NotLogicOP_18 = true;
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! Timer_Scaduto(L_P1__GetMainc38(my_id)));
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_NotLogicOP_18);
    res_OrLogicOP_17 = (res_OrLogicOP_17 || (Counter_GetValore(L_P1__GetMainc40(my_id)) == 13205u));
    
    res_OrLogicOP_16 = (res_OrLogicOP_16 || res_OrLogicOP_17);
    res_OrLogicOP_16 = (res_OrLogicOP_16 || (L_P1__GetInMainc6(my_id) == true));
    
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_OrLogicOP_16);
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (L_P1__GetParamMainc8(my_id) == false));
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_NotLogicOP_19);
    
    if(res_OrLogicOP_15){
    bool res_AndLogicOP_20 = true;
    bool res_NotLogicOP_21 = true;
    bool res_NotLogicOP_22 = true;
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! (L_P1__GetMainc29(my_id) == c120x));
    res_NotLogicOP_21 = (res_NotLogicOP_21 && ! res_NotLogicOP_22);
    res_AndLogicOP_20 = (res_AndLogicOP_20 && res_NotLogicOP_21);
    res_AndLogicOP_20 = (res_AndLogicOP_20 && (L_P1__GetInConsd(my_id) == false));
    
    res_ImpliesLogicOp_14 = (res_ImpliesLogicOp_14 && res_AndLogicOP_20);
    }
    res_ImpliesLogicOp_9 = (res_ImpliesLogicOp_9 && res_ImpliesLogicOp_14);
    }
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_ImpliesLogicOp_9);
    bool res_OrLogicOP_23 = false;
    bool res_OrLogicOP_24 = false;
    bool res_OrLogicOP_25 = false;
    res_OrLogicOP_25 = (res_OrLogicOP_25 || (L_P1__GetParamMainc9(my_id) == 6u));
    bool res_NotLogicOP_26 = true;
    res_NotLogicOP_26 = (res_NotLogicOP_26 && ! (L_P1__GetInMainc6(my_id) == false));
    res_OrLogicOP_25 = (res_OrLogicOP_25 || res_NotLogicOP_26);
    
    res_OrLogicOP_24 = (res_OrLogicOP_24 || res_OrLogicOP_25);
    bool res_NotLogicOP_27 = true;
    res_NotLogicOP_27 = (res_NotLogicOP_27 && ! (Counter_GetValore(L_P1__GetMainc39(my_id)) == 15u));
    res_OrLogicOP_24 = (res_OrLogicOP_24 || res_NotLogicOP_27);
    
    res_OrLogicOP_23 = (res_OrLogicOP_23 || res_OrLogicOP_24);
    bool res_NotLogicOP_28 = true;
    bool res_NotLogicOP_29 = true;
    res_NotLogicOP_29 = (res_NotLogicOP_29 && ! (L_P1__GetParamMainc10(my_id) == c75giallo));
    res_NotLogicOP_28 = (res_NotLogicOP_28 && ! res_NotLogicOP_29);
    res_OrLogicOP_23 = (res_OrLogicOP_23 || res_NotLogicOP_28);
    
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_OrLogicOP_23);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_OrLogicOP_8);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *47,51,*  *,*  il contatore MainClass_C1_contatore_Co10 sia  minore di  *55,* 113
    //   *104,* e  che  *34,*  il parametro MainClass_C1_parametro_P8 non sia  uguale a  *53,* 6
    bool res_AndLogicOP_30 = true;
    res_AndLogicOP_30 = (res_AndLogicOP_30 && (Counter_GetValore(L_P1__GetMainc39(my_id)) < 113u));
    bool res_NotLogicOP_31 = true;
    res_NotLogicOP_31 = (res_NotLogicOP_31 && ! (L_P1__GetParamMainc9(my_id) == 6u));
    res_AndLogicOP_30 = (res_AndLogicOP_30 && res_NotLogicOP_31);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_AndLogicOP_30);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
    
    { commento: {63,}  se il ripristino dello stato  non è  diverso da  commento: {56,}  state1  commento: {107,} commento: {34,} o  se il parametro MainClass_C1_parametro_P9 non è  uguale a c75Giallo, Solo una delle seguenti { 
     commento: {35,}  se il controllo MainClass_C1_controllo_C10 è  uguale a  True , Verifica che   commento: {47,49,50,51,}  commento: {,}  la variabile MainClass_C1_variabile_V6 non sia  uguale a c75Giallo
     commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T7 sia disattivo
     commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P9 non sia  diverso da c75Giallo
     commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co10 sia  minore di  commento: {55,} 1532
    
    
     } Verifica che   commento: {49,}  commento: {,}  il timer MainClass_C1_timer_T7 non sia attivo
    
    
    }
*/
bool L_P1__Macro13(instance_id_t const my_id , C1_Enumerat2 argom28, C1_Enumerat2 argom29, C1_Enumerat2 argom30)
{
bool res_AndLogicOP_0 = true;
    
    //  *63,*  se il ripristino dello stato  non è  diverso da  *56,*  state1  *107,* *34,* o  se il parametro MainClass_C1_parametro_P9 non è  uguale a c75Giallo, Solo una delle seguenti { 
    //   *35,*  se il controllo MainClass_C1_controllo_C10 è  uguale a  True , Verifica che   *47,49,50,51,*  *,*  la variabile MainClass_C1_variabile_V6 non sia  uguale a c75Giallo
    //   *104,* o  che  *,*  il timer MainClass_C1_timer_T7 sia disattivo
    //   *104,* o  che  *34,*  il parametro MainClass_C1_parametro_P9 non sia  diverso da c75Giallo
    //   *104,* e  che  *,*  il contatore MainClass_C1_contatore_Co10 sia  minore di  *55,* 1532
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_NotLogicOP_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetStato1(my_id) == C1_St_state));
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! res_NotLogicOP_4);
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_3);
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetParamMainc10(my_id) == c75giallo));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_5);
    
    if(res_OrLogicOP_2){
    bool res_ImpliesLogicOp_6 = true;
    if((L_P1__GetInMainc5(my_id) == true)){
    bool res_OrLogicOP_7 = false;
    bool res_OrLogicOP_8 = false;
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetMainc28(my_id) == c75giallo));
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_NotLogicOP_9);
    res_OrLogicOP_8 = (res_OrLogicOP_8 || Timer_Disattivo(L_P1__GetMainc38(my_id)));
    
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_OrLogicOP_8);
    bool res_AndLogicOP_10 = true;
    bool res_NotLogicOP_11 = true;
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (L_P1__GetParamMainc10(my_id) == c75giallo));
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! res_NotLogicOP_12);
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_NotLogicOP_11);
    res_AndLogicOP_10 = (res_AndLogicOP_10 && (Counter_GetValore(L_P1__GetMainc39(my_id)) < 1532u));
    
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_AndLogicOP_10);
    
    res_ImpliesLogicOp_6 = (res_ImpliesLogicOp_6 && res_OrLogicOP_7);
    }
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_ImpliesLogicOp_6);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *49,*  *,*  il timer MainClass_C1_timer_T7 non sia attivo
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! Timer_Attivo(L_P1__GetMainc38(my_id)));
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_NotLogicOP_13);
    
    
    
    return res_AndLogicOP_0;
}


// Macro valorizzate

/*
    CNL corrispondente:
    
    { commento: {[} commento: {35,}  se il controllo MainClass_C1_controllo_C6 è  diverso da  False  commento: {34,} o  se lo stato  non è  diverso da  commento: {56,}  state1  commento: {106,} , assegna alla macro il valore RossoGialloGiallo
    
     commento: {46,} assegna alla macro il valore RossoGialloGiallo commento: {],}
    }
*/
C1_Enumerat2 L_P1__Macro4(instance_id_t const my_id , C1_Enumerat3 argom, C1_Enumerat4 argom1, bool argom2, C1_Enumerat4 argom3, C1_Enumerat4 argom4)
{
C1_Enumerat2 res_macro_val;
    
    //  *[* *35,*  se il controllo MainClass_C1_controllo_C6 è  diverso da  False  *34,* o  se lo stato  non è  diverso da  *56,*  state1
    bool res_OrLogicOP_0 = false;
    bool res_NotLogicOP_1 = true;
    res_NotLogicOP_1 = (res_NotLogicOP_1 && ! (L_P1__GetInMainc7(my_id) == false));
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_1);
    bool res_NotLogicOP_2 = true;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1_C1_GetState(my_id) == C1_St_state));
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! res_NotLogicOP_3);
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_2);
    
    if(res_OrLogicOP_0){
    
    res_macro_val = rossogiallo2;
    }
    else{
    res_macro_val = rossogiallo2;
    }
    return res_macro_val;
}

/*
    CNL corrispondente:
    
    { commento: {[}
     commento: {46,} assegna alla macro il valore  False  commento: {],}
    }
*/
bool L_P1__Macro5(instance_id_t const my_id , C1_Enumerat2 argom5, C1_Enumerat3 argom6, C1_Enumerat4 argom7, C1_Enumerat4 argom8, C1_Enumerat3 argom9, C1_Enumerat4 argom10)
{
return false;
}

/*
    CNL corrispondente:
    
    { commento: {[}
     commento: {46,} assegna alla macro il valore  False  commento: {],}
    }
*/
bool L_P1__Macro6(instance_id_t const my_id , C1_Enumerat4 argom11, C1_Enumerat2 argom12, C1_Enumerat1 argom13, C1_Enumerat2 argom14, C1_Enumerat2 argom15, C1_Enumerat4 argom16)
{
return false;
}

/*
    CNL corrispondente:
    
    { commento: {[}
     commento: {46,} assegna alla macro il valore c75Giallo commento: {],}
    }
*/
C1_Enumerat3 L_P1__Macro7(instance_id_t const my_id , C1_Enumerat1 argom17, C1_Enumerat4 argom18, C1_Enumerat1 argom19, C1_Enumerat4 argom20, C1_Enumerat4 argom21)
{
return c75giallo;
}

/*
    CNL corrispondente:
    
    { commento: {[}
     commento: {46,} assegna alla macro il valore  True  commento: {],}
    }
*/
bool L_P1__Macro8(instance_id_t const my_id , C1_Enumerat2 argom22, C1_Enumerat3 argom23, C1_Enumerat2 argom24, C1_Enumerat2 argom25, C1_Enumerat1 argom26, C1_Enumerat1 argom27)
{
return true;
}



