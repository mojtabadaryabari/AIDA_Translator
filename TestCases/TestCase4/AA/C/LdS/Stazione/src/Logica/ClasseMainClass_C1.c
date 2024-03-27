// Codice del modello 'TestCase4', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#include "Logica/ClasseMainClass_C1.h"
#include "Logica/ClasseSubClass_C2.h"
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
    L_P1__SetMainc11(my_id, 0);
    L_P1__SetMainc13(my_id, 0);
    L_P1__SetMainc15(my_id, c270xx);
    L_P1__SetMainc17(my_id, false);
    L_P1__SetMainc19(my_id, 0);
    L_P1__SetMainc20(my_id, 0);
    L_P1__SetMainc21(my_id, gialloaverd);
    L_P1__SetMainc22(my_id, gialloaverd);
    L_P1__SetMainc23(my_id, c180x);
    L_P1__SetMainc24(my_id, c180x);
    L_P1__SetMainc25(my_id, 0);
    L_P1__SetMainc26(my_id, 0);
    L_P1__SetMainc27(my_id, false);
    L_P1__SetMainc28(my_id, false);
    L_P1__SetMainc29(my_id, c270x);
    L_P1__SetMainc30(my_id, 0);
    L_P1__SetMainc31(my_id, false);
    L_P1__SetMainc32(my_id, 0);
    L_P1__SetStato1(my_id, C1_St_Stato);
    // init controlli precedenti
    L_P1__SetMainc10(my_id, true);
    // init Timer e Counter
    Timer_AggmInit(L_P1__GetMainc33(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc33_ID);
    Timer_Init(L_P1__GetMainc33(my_id), 201000);
    Timer_AggmInit(L_P1__GetMainc34(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc34_ID);
    Timer_Init(L_P1__GetMainc34(my_id), 201000);
    Timer_AggmInit(L_P1__GetMainc35(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc35_ID);
    Timer_Init(L_P1__GetMainc35(my_id), 453000);
    Timer_AggmInit(L_P1__GetMainc36(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc36_ID);
    Timer_Init(L_P1__GetMainc36(my_id), 44000);
    Timer_AggmInit(L_P1__GetMainc37(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc37_ID);
    Timer_Init(L_P1__GetMainc37(my_id), 312000);
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
    Timer_Exec(L_P1__GetMainc33(my_id));
    Timer_Exec(L_P1__GetMainc34(my_id));
    Timer_Exec(L_P1__GetMainc35(my_id));
    Timer_Exec(L_P1__GetMainc36(my_id));
    Timer_Exec(L_P1__GetMainc37(my_id));
}

void L_P1_C1_GSetSafe(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C1(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C1(proc_id);
    L_P1__SetOutMainc(my_id, true);
    L_P1__SetOutMainc1(my_id, false);
    L_P1__SetOutMainc2(my_id, giallox);
    L_P1__SetOutMainc3(my_id, rossogiallo2);
}

void L_P1_C1_GUpdatePrev(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C1(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C1(proc_id);
    L_P1__SetMainc10(my_id, L_P1__GetInMainc9(my_id));
    L_P1__SetMainc12(my_id, L_P1__GetMainc11(my_id));
    L_P1__SetMainc14(my_id, L_P1__GetMainc13(my_id));
    L_P1__SetMainc16(my_id, L_P1__GetMainc15(my_id));
    L_P1__SetMainc18(my_id, L_P1__GetMainc17(my_id));
}

// ********** Definizione macro **********

// Macro di effetto

/*
    CNL corrispondente:
    
    { commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo commento: {37,} o  se la variabile MainClass_C1_variabile_V4 non è  diverso da RossoGialloVerde commento: {36,} e  se il timer MainClass_C1_timer_T1 non è disattivo commento: {34,} o  se il parametro MainClass_C1_parametro_P3 non è  diverso da  False , commento: {70,}Incrementa il contatore MainClass_C1_contatore_Co4
    
       
     commento: {35,}  se il controllo MainClass_C1_controllo_C8 è  uguale a RossoGialloxVerdex e  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} o  se il controllo MainClass_C1_controllo_C9 è  diverso da  False  commento: {36,} e  se il timer MainClass_C1_timer_T8 non è disattivo commento: {37,} e  se la variabile MainClass_C1_variabile_V4 è  diverso da RossoGialloVerde commento: {37,} e  se la variabile MainClass_C1_variabile_V5 non è  minore di  commento: {55,} 9, commento: {66,} Assegna al comando MainClass_C1_comando_C5 il valore RossoGialloxVerdex
    
       
     commento: {34,}  se il parametro MainClass_C1_parametro_P3 non è  diverso da  True  commento: {37,} o  se la variabile MainClass_C1_variabile_V5 è  uguale a  commento: {53,} 8 commento: {37,} o  se la variabile MainClass_C1_variabile_V5 è  uguale a  commento: {53,} 10 commento: {35,} e  se il controllo MainClass_C1_controllo_C1 non è  uguale a  False  commento: {36,} o  se il timer MainClass_C1_timer_T8 è disattivo, commento: {66,} Assegna al comando MainClass_C1_comando_C3 il valore  True 
    
       
      se il ripristino dello stato  è  diverso da  commento: {56,}  state1  commento: {107,} commento: {37,} o  se la variabile MainClass_C1_variabile_V5 è  maggiore di  commento: {54,} 10 commento: {38,} o  se il contatore MainClass_C1_contatore_Co4 è  maggiore di  commento: {54,} 123 commento: {38,} e  se il contatore MainClass_C1_contatore_Co4 è  diverso da  commento: {56,} 11 commento: {38,} e  se il contatore MainClass_C1_contatore_Co4 non è  maggiore di  commento: {54,} 15 commento: {35,} o  se il controllo MainClass_C1_controllo_C2 è  diverso da Giallox, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V5 il valore 5
    
     ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V5 il valore 7
    
    
    
    }
*/
void L_P1__Macro(instance_id_t const my_id )
{
//  *110,*  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo *37,* o  se la variabile MainClass_C1_variabile_V4 non è  diverso da RossoGialloVerde *36,* e  se il timer MainClass_C1_timer_T1 non è disattivo *34,* o  se il parametro MainClass_C1_parametro_P3 non è  diverso da  False , *70,*Incrementa il contatore MainClass_C1_contatore_Co4
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! Timer_Attivo(L_P1__GetMainc34(my_id)));
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_NotLogicOP_2);
    bool res_AndLogicOP_3 = true;
    bool res_NotLogicOP_4 = true;
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetMainc29(my_id) == rossogiallo));
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! res_NotLogicOP_5);
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_4);
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! Timer_Disattivo(L_P1__GetMainc35(my_id)));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_6);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_3);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_NotLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetParamMainc8(my_id) == false));
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! res_NotLogicOP_8);
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_7);
    
    if(res_OrLogicOP_0){
    
    Counter_Incr(L_P1__GetMainc38(my_id));
    }
    //  *35,*  se il controllo MainClass_C1_controllo_C8 è  uguale a RossoGialloxVerdex e  se il controllo ConsDef  è  uguale a FALSE  *35,* o  se il controllo MainClass_C1_controllo_C9 è  diverso da  False  *36,* e  se il timer MainClass_C1_timer_T8 non è disattivo *37,* e  se la variabile MainClass_C1_variabile_V4 è  diverso da RossoGialloVerde *37,* e  se la variabile MainClass_C1_variabile_V5 non è  minore di  *55,* 9, *66,* Assegna al comando MainClass_C1_comando_C5 il valore RossoGialloxVerdex
    bool res_OrLogicOP_9 = false;
    bool res_AndLogicOP_10 = true;
    res_AndLogicOP_10 = (res_AndLogicOP_10 && (L_P1__GetInMainc6(my_id) == rossogiallo2));
    res_AndLogicOP_10 = (res_AndLogicOP_10 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_AndLogicOP_10);
    bool res_AndLogicOP_11 = true;
    bool res_AndLogicOP_12 = true;
    bool res_AndLogicOP_13 = true;
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1__GetInMainc7(my_id) == false));
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_NotLogicOP_14);
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! Timer_Disattivo(L_P1__GetMainc37(my_id)));
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_NotLogicOP_15);
    
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_AndLogicOP_13);
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (L_P1__GetMainc29(my_id) == rossogiallo));
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_NotLogicOP_16);
    
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_AndLogicOP_12);
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! (L_P1__GetMainc30(my_id) < 9u));
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_NotLogicOP_17);
    
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_AndLogicOP_11);
    
    if(res_OrLogicOP_9){
    
    L_P1__SetOutMainc3(my_id,rossogiallo2);
    }
    //  *34,*  se il parametro MainClass_C1_parametro_P3 non è  diverso da  True  *37,* o  se la variabile MainClass_C1_variabile_V5 è  uguale a  *53,* 8 *37,* o  se la variabile MainClass_C1_variabile_V5 è  uguale a  *53,* 10 *35,* e  se il controllo MainClass_C1_controllo_C1 non è  uguale a  False  *36,* o  se il timer MainClass_C1_timer_T8 è disattivo, *66,* Assegna al comando MainClass_C1_comando_C3 il valore  True
    bool res_OrLogicOP_18 = false;
    bool res_OrLogicOP_19 = false;
    bool res_OrLogicOP_20 = false;
    bool res_NotLogicOP_21 = true;
    bool res_NotLogicOP_22 = true;
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! (L_P1__GetParamMainc8(my_id) == true));
    res_NotLogicOP_21 = (res_NotLogicOP_21 && ! res_NotLogicOP_22);
    res_OrLogicOP_20 = (res_OrLogicOP_20 || res_NotLogicOP_21);
    res_OrLogicOP_20 = (res_OrLogicOP_20 || (L_P1__GetMainc30(my_id) == 8u));
    
    res_OrLogicOP_19 = (res_OrLogicOP_19 || res_OrLogicOP_20);
    bool res_AndLogicOP_23 = true;
    res_AndLogicOP_23 = (res_AndLogicOP_23 && (L_P1__GetMainc30(my_id) == 10u));
    bool res_NotLogicOP_24 = true;
    res_NotLogicOP_24 = (res_NotLogicOP_24 && ! (L_P1__GetInMainc4(my_id) == false));
    res_AndLogicOP_23 = (res_AndLogicOP_23 && res_NotLogicOP_24);
    
    res_OrLogicOP_19 = (res_OrLogicOP_19 || res_AndLogicOP_23);
    
    res_OrLogicOP_18 = (res_OrLogicOP_18 || res_OrLogicOP_19);
    res_OrLogicOP_18 = (res_OrLogicOP_18 || Timer_Disattivo(L_P1__GetMainc37(my_id)));
    
    if(res_OrLogicOP_18){
    
    L_P1__SetOutMainc1(my_id,true);
    }
    //  se il ripristino dello stato  è  diverso da  *56,*  state1  *107,* *37,* o  se la variabile MainClass_C1_variabile_V5 è  maggiore di  *54,* 10 *38,* o  se il contatore MainClass_C1_contatore_Co4 è  maggiore di  *54,* 123 *38,* e  se il contatore MainClass_C1_contatore_Co4 è  diverso da  *56,* 11 *38,* e  se il contatore MainClass_C1_contatore_Co4 non è  maggiore di  *54,* 15 *35,* o  se il controllo MainClass_C1_controllo_C2 è  diverso da Giallox, *67,* Assegna alla variabile MainClass_C1_variabile_V5 il valore 5
    // ,altrimenti  *67,* Assegna alla variabile MainClass_C1_variabile_V5 il valore 7
    bool res_OrLogicOP_25 = false;
    bool res_OrLogicOP_26 = false;
    bool res_OrLogicOP_27 = false;
    bool res_NotLogicOP_28 = true;
    res_NotLogicOP_28 = (res_NotLogicOP_28 && ! (L_P1__GetStato1(my_id) == C1_St_state));
    res_OrLogicOP_27 = (res_OrLogicOP_27 || res_NotLogicOP_28);
    res_OrLogicOP_27 = (res_OrLogicOP_27 || (L_P1__GetMainc30(my_id) > 10u));
    
    res_OrLogicOP_26 = (res_OrLogicOP_26 || res_OrLogicOP_27);
    bool res_AndLogicOP_29 = true;
    bool res_AndLogicOP_30 = true;
    res_AndLogicOP_30 = (res_AndLogicOP_30 && (Counter_GetValore(L_P1__GetMainc38(my_id)) > 123u));
    bool res_NotLogicOP_31 = true;
    res_NotLogicOP_31 = (res_NotLogicOP_31 && ! (Counter_GetValore(L_P1__GetMainc38(my_id)) == 11u));
    res_AndLogicOP_30 = (res_AndLogicOP_30 && res_NotLogicOP_31);
    
    res_AndLogicOP_29 = (res_AndLogicOP_29 && res_AndLogicOP_30);
    bool res_NotLogicOP_32 = true;
    res_NotLogicOP_32 = (res_NotLogicOP_32 && ! (Counter_GetValore(L_P1__GetMainc38(my_id)) > 15u));
    res_AndLogicOP_29 = (res_AndLogicOP_29 && res_NotLogicOP_32);
    
    res_OrLogicOP_26 = (res_OrLogicOP_26 || res_AndLogicOP_29);
    
    res_OrLogicOP_25 = (res_OrLogicOP_25 || res_OrLogicOP_26);
    bool res_NotLogicOP_33 = true;
    res_NotLogicOP_33 = (res_NotLogicOP_33 && ! (L_P1__GetInMainc5(my_id) == giallox));
    res_OrLogicOP_25 = (res_OrLogicOP_25 || res_NotLogicOP_33);
    
    if(res_OrLogicOP_25){
    
    L_P1__SetMainc30(my_id,5u);
    }else{
    
    L_P1__SetMainc30(my_id,7u);
    }
}

/*
    CNL corrispondente:
    
    {  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} o  se il contatore MainClass_C1_contatore_Co4 è  maggiore di  commento: {54,} 110124 commento: {37,} o  se la variabile MainClass_C1_variabile_V5 non è  minore di  commento: {55,} 7, commento: {66,} Assegna al comando MainClass_C1_comando_C10 il valore  False 
    
     ,altrimenti  commento: {72,}Azzera il contatore MainClass_C1_contatore_Co4
    
    
     commento: {36,}  se il timer MainClass_C1_timer_T8 è disattivo commento: {35,} o  se il controllo MainClass_C1_controllo_C9 è  uguale a  False  commento: {35,} e  se il controllo MainClass_C1_controllo_C1 è  diverso da  True  commento: {37,} e  se la variabile MainClass_C1_variabile_V5 è  diverso da  commento: {56,} 5 commento: {38,} o  se il contatore MainClass_C1_contatore_Co4 non è  maggiore di  commento: {54,} 145, commento: {68,}Attiva il timer MainClass_C1_timer_T6
    
       
      se il ripristino dello stato  è  uguale a  commento: {53,}  state1  commento: {107,} commento: {37,} e  se la variabile MainClass_C1_variabile_V6 è  uguale a  False , commento: {66,} Assegna al comando MainClass_C1_comando_C5 il valore RossoGialloxVerdex
    
       
     commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è disattivo commento: {35,} o  se il controllo MainClass_C1_controllo_C1 è  uguale a  True  commento: {36,} e  se il timer MainClass_C1_timer_T6 non è scaduto, commento: {69,}Disattiva il timer MainClass_C1_timer_T8
    
       
    
    }
*/
void L_P1__Macro1(instance_id_t const my_id )
{
//  se il controllo ConsDef  è  uguale a FALSE  *38,* o  se il contatore MainClass_C1_contatore_Co4 è  maggiore di  *54,* 110124 *37,* o  se la variabile MainClass_C1_variabile_V5 non è  minore di  *55,* 7, *66,* Assegna al comando MainClass_C1_comando_C10 il valore  False 
    // ,altrimenti  *72,*Azzera il contatore MainClass_C1_contatore_Co4
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    res_OrLogicOP_1 = (res_OrLogicOP_1 || (L_P1__GetInConsd(my_id) == false));
    res_OrLogicOP_1 = (res_OrLogicOP_1 || (Counter_GetValore(L_P1__GetMainc38(my_id)) > 110124u));
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (L_P1__GetMainc30(my_id) < 7u));
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_2);
    
    if(res_OrLogicOP_0){
    
    L_P1__SetOutMainc(my_id,false);
    }else{
    
    Counter_Res(L_P1__GetMainc38(my_id));
    }
    //  *36,*  se il timer MainClass_C1_timer_T8 è disattivo *35,* o  se il controllo MainClass_C1_controllo_C9 è  uguale a  False  *35,* e  se il controllo MainClass_C1_controllo_C1 è  diverso da  True  *37,* e  se la variabile MainClass_C1_variabile_V5 è  diverso da  *56,* 5 *38,* o  se il contatore MainClass_C1_contatore_Co4 non è  maggiore di  *54,* 145, *68,*Attiva il timer MainClass_C1_timer_T6
    bool res_OrLogicOP_3 = false;
    bool res_OrLogicOP_4 = false;
    res_OrLogicOP_4 = (res_OrLogicOP_4 || Timer_Disattivo(L_P1__GetMainc37(my_id)));
    bool res_AndLogicOP_5 = true;
    bool res_AndLogicOP_6 = true;
    res_AndLogicOP_6 = (res_AndLogicOP_6 && (L_P1__GetInMainc7(my_id) == false));
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetInMainc4(my_id) == true));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_7);
    
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_AndLogicOP_6);
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetMainc30(my_id) == 5u));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_8);
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_AndLogicOP_5);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_OrLogicOP_4);
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (Counter_GetValore(L_P1__GetMainc38(my_id)) > 145u));
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_NotLogicOP_9);
    
    if(res_OrLogicOP_3){
    
    Timer_Attiva(L_P1__GetMainc36(my_id));
    }
    //  se il ripristino dello stato  è  uguale a  *53,*  state1  *107,* *37,* e  se la variabile MainClass_C1_variabile_V6 è  uguale a  False , *66,* Assegna al comando MainClass_C1_comando_C5 il valore RossoGialloxVerdex
    bool res_AndLogicOP_10 = true;
    res_AndLogicOP_10 = (res_AndLogicOP_10 && (L_P1__GetStato1(my_id) == C1_St_state));
    res_AndLogicOP_10 = (res_AndLogicOP_10 && (L_P1__GetMainc31(my_id) == false));
    
    if(res_AndLogicOP_10){
    
    L_P1__SetOutMainc3(my_id,rossogiallo2);
    }
    //  *110,*  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è disattivo *35,* o  se il controllo MainClass_C1_controllo_C1 è  uguale a  True  *36,* e  se il timer MainClass_C1_timer_T6 non è scaduto, *69,*Disattiva il timer MainClass_C1_timer_T8
    bool res_OrLogicOP_11 = false;
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! Timer_Disattivo(L_P1__GetMainc34(my_id)));
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_NotLogicOP_12);
    bool res_AndLogicOP_13 = true;
    res_AndLogicOP_13 = (res_AndLogicOP_13 && (L_P1__GetInMainc4(my_id) == true));
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! Timer_Scaduto(L_P1__GetMainc36(my_id)));
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_NotLogicOP_14);
    
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_AndLogicOP_13);
    
    if(res_OrLogicOP_11){
    
    Timer_Disattiva(L_P1__GetMainc37(my_id));
    }
}


// Macro di verifica

/*
    CNL corrispondente:
     
    { commento: {63,}  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
     commento: {63,}  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} o  se il controllo MainClass_C1_controllo_C9 non è  uguale a  True , Solo una delle seguenti { 
     commento: {38,}  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  commento: {56,} 150 commento: {37,} e  se la variabile MainClass_C1_variabile_V6 non è  diverso da  True  commento: {34,} e  se il parametro MainClass_C1_parametro_P3 è  diverso da  True  commento: {34,} o  se il parametro MainClass_C1_parametro_P3 è  uguale a  False  commento: {35,} o  se il controllo MainClass_C1_controllo_C9 non è  diverso da  False  commento: {35,} e  se il controllo MainClass_C1_controllo_C2 è  diverso da Giallox, Verifica che   commento: {47,48,50,}  commento: {,}  il controllo MainClass_C1_controllo_C9 non sia  diverso da  False 
     commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V4 non sia  uguale a RossoGialloVerde
     commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P3 sia  diverso da  True 
    
    
     } Verifica che   commento: {47,48,49,50,51,}  commento: {,}  il contatore MainClass_C1_contatore_Co4 sia  maggiore di  commento: {54,} 13
     commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V4 sia  uguale a RossoGialloVerde
     commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P3 non sia  uguale a  True 
     commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C1 non sia  diverso da  False 
     commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T6 sia disattivo
    
    
     } Verifica che   commento: {47,48,}  commento: {34,}  il parametro MainClass_C1_parametro_P3 sia  uguale a  False 
     commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C2 non sia  diverso da Giallox
    
    
    }
*/
bool L_P1__Macro3(instance_id_t const my_id )
{
bool res_AndLogicOP_0 = true;
    
    //  *63,*  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
    //   *63,*  se il controllo ConsDef  è  uguale a FALSE  *35,* o  se il controllo MainClass_C1_controllo_C9 non è  uguale a  True , Solo una delle seguenti { 
    //   *38,*  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  *56,* 150 *37,* e  se la variabile MainClass_C1_variabile_V6 non è  diverso da  True  *34,* e  se il parametro MainClass_C1_parametro_P3 è  diverso da  True  *34,* o  se il parametro MainClass_C1_parametro_P3 è  uguale a  False  *35,* o  se il controllo MainClass_C1_controllo_C9 non è  diverso da  False  *35,* e  se il controllo MainClass_C1_controllo_C2 è  diverso da Giallox, Verifica che   *47,48,50,*  *,*  il controllo MainClass_C1_controllo_C9 non sia  diverso da  False 
    //   *104,* o  che  *,*  la variabile MainClass_C1_variabile_V4 non sia  uguale a RossoGialloVerde
    //   *104,* o  che  *34,*  il parametro MainClass_C1_parametro_P3 sia  diverso da  True 
    //   } Verifica che   *47,48,49,50,51,*  *,*  il contatore MainClass_C1_contatore_Co4 sia  maggiore di  *54,* 13
    //   *104,* o  che  *,*  la variabile MainClass_C1_variabile_V4 sia  uguale a RossoGialloVerde
    //   *104,* e  che  *34,*  il parametro MainClass_C1_parametro_P3 non sia  uguale a  True 
    //   *104,* e  che  *,*  il controllo MainClass_C1_controllo_C1 non sia  diverso da  False 
    //   *104,* o  che  *,*  il timer MainClass_C1_timer_T6 sia disattivo
    //   }
    bool res_ImpliesLogicOp_1 = true;
    if((L_P1__GetInConsd(my_id) == false)){
    bool res_XorLogicOP_2 = true;
    int xorIndex_res_XorLogicOP_2 = 0;
    bool res_ImpliesLogicOp_3 = true;
    bool res_OrLogicOP_4 = false;
    res_OrLogicOP_4 = (res_OrLogicOP_4 || (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetInMainc7(my_id) == true));
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_NotLogicOP_5);
    
    if(res_OrLogicOP_4){
    bool res_ImpliesLogicOp_6 = true;
    bool res_OrLogicOP_7 = false;
    bool res_OrLogicOP_8 = false;
    bool res_AndLogicOP_9 = true;
    bool res_AndLogicOP_10 = true;
    bool res_NotLogicOP_11 = true;
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (Counter_GetValore(L_P1__GetMainc38(my_id)) == 150u));
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! res_NotLogicOP_12);
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_NotLogicOP_11);
    bool res_NotLogicOP_13 = true;
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1__GetMainc31(my_id) == true));
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! res_NotLogicOP_14);
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_NotLogicOP_13);
    
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_AndLogicOP_10);
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (L_P1__GetParamMainc8(my_id) == true));
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_NotLogicOP_15);
    
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_AndLogicOP_9);
    res_OrLogicOP_8 = (res_OrLogicOP_8 || (L_P1__GetParamMainc8(my_id) == false));
    
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_OrLogicOP_8);
    bool res_AndLogicOP_16 = true;
    bool res_NotLogicOP_17 = true;
    bool res_NotLogicOP_18 = true;
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! (L_P1__GetInMainc7(my_id) == false));
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! res_NotLogicOP_18);
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_NotLogicOP_17);
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (L_P1__GetInMainc5(my_id) == giallox));
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_NotLogicOP_19);
    
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_AndLogicOP_16);
    
    if(res_OrLogicOP_7){
    bool res_OrLogicOP_20 = false;
    bool res_OrLogicOP_21 = false;
    bool res_NotLogicOP_22 = true;
    bool res_NotLogicOP_23 = true;
    res_NotLogicOP_23 = (res_NotLogicOP_23 && ! (L_P1__GetInMainc7(my_id) == false));
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! res_NotLogicOP_23);
    res_OrLogicOP_21 = (res_OrLogicOP_21 || res_NotLogicOP_22);
    bool res_NotLogicOP_24 = true;
    res_NotLogicOP_24 = (res_NotLogicOP_24 && ! (L_P1__GetMainc29(my_id) == rossogiallo));
    res_OrLogicOP_21 = (res_OrLogicOP_21 || res_NotLogicOP_24);
    
    res_OrLogicOP_20 = (res_OrLogicOP_20 || res_OrLogicOP_21);
    bool res_NotLogicOP_25 = true;
    res_NotLogicOP_25 = (res_NotLogicOP_25 && ! (L_P1__GetParamMainc8(my_id) == true));
    res_OrLogicOP_20 = (res_OrLogicOP_20 || res_NotLogicOP_25);
    
    res_ImpliesLogicOp_6 = (res_ImpliesLogicOp_6 && res_OrLogicOP_20);
    }
    res_ImpliesLogicOp_3 = (res_ImpliesLogicOp_3 && res_ImpliesLogicOp_6);
    }
    if(res_ImpliesLogicOp_3){
    xorIndex_res_XorLogicOP_2 = (xorIndex_res_XorLogicOP_2 + 1);
    }
    bool res_OrLogicOP_26 = false;
    bool res_OrLogicOP_27 = false;
    res_OrLogicOP_27 = (res_OrLogicOP_27 || (Counter_GetValore(L_P1__GetMainc38(my_id)) > 13u));
    bool res_AndLogicOP_28 = true;
    bool res_AndLogicOP_29 = true;
    res_AndLogicOP_29 = (res_AndLogicOP_29 && (L_P1__GetMainc29(my_id) == rossogiallo));
    bool res_NotLogicOP_30 = true;
    res_NotLogicOP_30 = (res_NotLogicOP_30 && ! (L_P1__GetParamMainc8(my_id) == true));
    res_AndLogicOP_29 = (res_AndLogicOP_29 && res_NotLogicOP_30);
    
    res_AndLogicOP_28 = (res_AndLogicOP_28 && res_AndLogicOP_29);
    bool res_NotLogicOP_31 = true;
    bool res_NotLogicOP_32 = true;
    res_NotLogicOP_32 = (res_NotLogicOP_32 && ! (L_P1__GetInMainc4(my_id) == false));
    res_NotLogicOP_31 = (res_NotLogicOP_31 && ! res_NotLogicOP_32);
    res_AndLogicOP_28 = (res_AndLogicOP_28 && res_NotLogicOP_31);
    
    res_OrLogicOP_27 = (res_OrLogicOP_27 || res_AndLogicOP_28);
    
    res_OrLogicOP_26 = (res_OrLogicOP_26 || res_OrLogicOP_27);
    res_OrLogicOP_26 = (res_OrLogicOP_26 || Timer_Disattivo(L_P1__GetMainc36(my_id)));
    
    if(res_OrLogicOP_26){
    xorIndex_res_XorLogicOP_2 = (xorIndex_res_XorLogicOP_2 + 1);
    }
    
    res_XorLogicOP_2 = (res_XorLogicOP_2 && (xorIndex_res_XorLogicOP_2 == 1));
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_XorLogicOP_2);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *47,48,*  *34,*  il parametro MainClass_C1_parametro_P3 sia  uguale a  False 
    //   *104,* e  che   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* o  che  *,*  il controllo MainClass_C1_controllo_C2 non sia  diverso da Giallox
    bool res_OrLogicOP_33 = false;
    bool res_AndLogicOP_34 = true;
    res_AndLogicOP_34 = (res_AndLogicOP_34 && (L_P1__GetParamMainc8(my_id) == false));
    res_AndLogicOP_34 = (res_AndLogicOP_34 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_33 = (res_OrLogicOP_33 || res_AndLogicOP_34);
    bool res_NotLogicOP_35 = true;
    bool res_NotLogicOP_36 = true;
    res_NotLogicOP_36 = (res_NotLogicOP_36 && ! (L_P1__GetInMainc5(my_id) == giallox));
    res_NotLogicOP_35 = (res_NotLogicOP_35 && ! res_NotLogicOP_36);
    res_OrLogicOP_33 = (res_OrLogicOP_33 || res_NotLogicOP_35);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_33);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
     
    { commento: {63,} commento: {34,}  se lo stato  non è  uguale a  commento: {53,}  state1  commento: {106,} commento: {35,} o  se il controllo MainClass_C1_controllo_C8 non è  uguale a RossoGialloxVerdex commento: {37,} o  se la variabile MainClass_C1_variabile_V6 non è  diverso da  True , Solo una delle seguenti { 
     commento: {62,}  se il ripristino dello stato  non è  diverso da  commento: {56,}  state1  commento: {107,} commento: {37,} e  se la variabile MainClass_C1_variabile_V6 è  uguale a  False  commento: {38,} o  se il contatore MainClass_C1_contatore_Co4 è  maggiore di  commento: {54,} 124, Almeno una delle seguenti { 
     commento: {63,} commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è scaduto commento: {38,} o  se il contatore MainClass_C1_contatore_Co4 è  diverso da  commento: {56,} 125, Solo una delle seguenti { 
      se il ripristino dello stato  non è  uguale a  commento: {53,}  state1  commento: {107,} commento: {38,} e  se il contatore MainClass_C1_contatore_Co4 è  minore di  commento: {55,} 12 e  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} e  se la variabile MainClass_C1_variabile_V7 è  minore di  commento: {55,} 7 commento: {35,} e  se il controllo MainClass_C1_controllo_C1 è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   commento: {47,48,49,51,}  commento: {,}  il controllo MainClass_C1_controllo_C1 sia  diverso da  False 
     commento: {104,} o  che  commento: {,}  il contatore MainClass_C1_contatore_Co4 sia  maggiore di  commento: {54,} 15301
     commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T1 non sia attivo
     commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P3 non sia  diverso da  True 
    
    
     } Verifica che   commento: {47,48,49,}  commento: {,}  il timer MainClass_C1_timer_T1 sia disattivo
     commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} o  che  commento: {36,}  il timer MainClass_C1_timer_T6 sia disattivo
     commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P3 non sia  uguale a  False 
    
    
     } Verifica che   commento: {47,48,49,51,}  commento: {,}  il timer MainClass_C1_timer_T6 non sia attivo
     commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C1 sia  diverso da  True 
     commento: {104,} o  che  commento: {,}  il contatore MainClass_C1_contatore_Co4 sia  maggiore di  commento: {54,} 11
     commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P3 non sia  uguale a  False 
     commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P3 non sia  diverso da  True 
     commento: {104,} e  che  commento: {36,}  il timer MainClass_C1_timer_T8 non sia disattivo
    
    
     } Verifica che   commento: {47,48,49,51,}  commento: {,}  il contatore MainClass_C1_contatore_Co4 sia  uguale a  commento: {53,} 1324
     commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T1 non sia scaduto
     commento: {104,} o  che  commento: {38,}  il contatore MainClass_C1_contatore_Co4 non sia  diverso da  commento: {56,} 115
     commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P3 sia  diverso da  True 
     commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} e  che  commento: {36,}  il timer MainClass_C1_timer_T1 sia attivo
    
    
    }
*/
bool L_P1__Macro4(instance_id_t const my_id )
{
bool res_AndLogicOP_0 = true;
    
    //  *63,* *34,*  se lo stato  non è  uguale a  *53,*  state1  *106,* *35,* o  se il controllo MainClass_C1_controllo_C8 non è  uguale a RossoGialloxVerdex *37,* o  se la variabile MainClass_C1_variabile_V6 non è  diverso da  True , Solo una delle seguenti { 
    //   *62,*  se il ripristino dello stato  non è  diverso da  *56,*  state1  *107,* *37,* e  se la variabile MainClass_C1_variabile_V6 è  uguale a  False  *38,* o  se il contatore MainClass_C1_contatore_Co4 è  maggiore di  *54,* 124, Almeno una delle seguenti { 
    //   *63,* *110,*  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è scaduto *38,* o  se il contatore MainClass_C1_contatore_Co4 è  diverso da  *56,* 125, Solo una delle seguenti { 
    //    se il ripristino dello stato  non è  uguale a  *53,*  state1  *107,* *38,* e  se il contatore MainClass_C1_contatore_Co4 è  minore di  *55,* 12 e  se il controllo ConsDef  è  uguale a FALSE  *37,* e  se la variabile MainClass_C1_variabile_V7 è  minore di  *55,* 7 *35,* e  se il controllo MainClass_C1_controllo_C1 è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   *47,48,49,51,*  *,*  il controllo MainClass_C1_controllo_C1 sia  diverso da  False 
    //   *104,* o  che  *,*  il contatore MainClass_C1_contatore_Co4 sia  maggiore di  *54,* 15301
    //   *104,* o  che  *,*  il timer MainClass_C1_timer_T1 non sia attivo
    //   *104,* e  che  *34,*  il parametro MainClass_C1_parametro_P3 non sia  diverso da  True 
    //   } Verifica che   *47,48,49,*  *,*  il timer MainClass_C1_timer_T1 sia disattivo
    //   *104,* o  che   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* o  che  *36,*  il timer MainClass_C1_timer_T6 sia disattivo
    //   *104,* o  che  *34,*  il parametro MainClass_C1_parametro_P3 non sia  uguale a  False 
    //   } Verifica che   *47,48,49,51,*  *,*  il timer MainClass_C1_timer_T6 non sia attivo
    //   *104,* e  che  *,*  il controllo MainClass_C1_controllo_C1 sia  diverso da  True 
    //   *104,* o  che  *,*  il contatore MainClass_C1_contatore_Co4 sia  maggiore di  *54,* 11
    //   *104,* o  che  *34,*  il parametro MainClass_C1_parametro_P3 non sia  uguale a  False 
    //   *104,* o  che  *34,*  il parametro MainClass_C1_parametro_P3 non sia  diverso da  True 
    //   *104,* e  che  *36,*  il timer MainClass_C1_timer_T8 non sia disattivo
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1_C1_GetState(my_id) == C1_St_state));
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_NotLogicOP_4);
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetInMainc6(my_id) == rossogiallo2));
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_NotLogicOP_5);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    bool res_NotLogicOP_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetMainc31(my_id) == true));
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! res_NotLogicOP_7);
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_6);
    
    if(res_OrLogicOP_2){
    bool res_XorLogicOP_8 = true;
    int xorIndex_res_XorLogicOP_8 = 0;
    bool res_ImpliesLogicOp_9 = true;
    bool res_OrLogicOP_10 = false;
    bool res_AndLogicOP_11 = true;
    bool res_NotLogicOP_12 = true;
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (L_P1__GetStato1(my_id) == C1_St_state));
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! res_NotLogicOP_13);
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_NotLogicOP_12);
    res_AndLogicOP_11 = (res_AndLogicOP_11 && (L_P1__GetMainc31(my_id) == false));
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_AndLogicOP_11);
    res_OrLogicOP_10 = (res_OrLogicOP_10 || (Counter_GetValore(L_P1__GetMainc38(my_id)) > 124u));
    
    if(res_OrLogicOP_10){
    bool res_OrLogicOP_14 = false;
    bool res_ImpliesLogicOp_15 = true;
    bool res_OrLogicOP_16 = false;
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! Timer_Scaduto(L_P1__GetMainc34(my_id)));
    res_OrLogicOP_16 = (res_OrLogicOP_16 || res_NotLogicOP_17);
    bool res_NotLogicOP_18 = true;
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! (Counter_GetValore(L_P1__GetMainc38(my_id)) == 125u));
    res_OrLogicOP_16 = (res_OrLogicOP_16 || res_NotLogicOP_18);
    
    if(res_OrLogicOP_16){
    bool res_ImpliesLogicOp_19 = true;
    bool res_AndLogicOP_20 = true;
    bool res_AndLogicOP_21 = true;
    bool res_AndLogicOP_22 = true;
    bool res_AndLogicOP_23 = true;
    bool res_AndLogicOP_24 = true;
    bool res_NotLogicOP_25 = true;
    res_NotLogicOP_25 = (res_NotLogicOP_25 && ! (L_P1__GetStato1(my_id) == C1_St_state));
    res_AndLogicOP_24 = (res_AndLogicOP_24 && res_NotLogicOP_25);
    res_AndLogicOP_24 = (res_AndLogicOP_24 && (Counter_GetValore(L_P1__GetMainc38(my_id)) < 12u));
    
    res_AndLogicOP_23 = (res_AndLogicOP_23 && res_AndLogicOP_24);
    res_AndLogicOP_23 = (res_AndLogicOP_23 && (L_P1__GetInConsd(my_id) == false));
    
    res_AndLogicOP_22 = (res_AndLogicOP_22 && res_AndLogicOP_23);
    res_AndLogicOP_22 = (res_AndLogicOP_22 && (L_P1__GetMainc32(my_id) < 7u));
    
    res_AndLogicOP_21 = (res_AndLogicOP_21 && res_AndLogicOP_22);
    res_AndLogicOP_21 = (res_AndLogicOP_21 && (L_P1__GetInMainc4(my_id) == false));
    
    res_AndLogicOP_20 = (res_AndLogicOP_20 && res_AndLogicOP_21);
    res_AndLogicOP_20 = (res_AndLogicOP_20 && (L_P1__GetInConsd(my_id) == false));
    
    if(res_AndLogicOP_20){
    bool res_OrLogicOP_26 = false;
    bool res_OrLogicOP_27 = false;
    bool res_NotLogicOP_28 = true;
    res_NotLogicOP_28 = (res_NotLogicOP_28 && ! (L_P1__GetInMainc4(my_id) == false));
    res_OrLogicOP_27 = (res_OrLogicOP_27 || res_NotLogicOP_28);
    res_OrLogicOP_27 = (res_OrLogicOP_27 || (Counter_GetValore(L_P1__GetMainc38(my_id)) > 15301u));
    
    res_OrLogicOP_26 = (res_OrLogicOP_26 || res_OrLogicOP_27);
    bool res_AndLogicOP_29 = true;
    bool res_NotLogicOP_30 = true;
    res_NotLogicOP_30 = (res_NotLogicOP_30 && ! Timer_Attivo(L_P1__GetMainc35(my_id)));
    res_AndLogicOP_29 = (res_AndLogicOP_29 && res_NotLogicOP_30);
    bool res_NotLogicOP_31 = true;
    bool res_NotLogicOP_32 = true;
    res_NotLogicOP_32 = (res_NotLogicOP_32 && ! (L_P1__GetParamMainc8(my_id) == true));
    res_NotLogicOP_31 = (res_NotLogicOP_31 && ! res_NotLogicOP_32);
    res_AndLogicOP_29 = (res_AndLogicOP_29 && res_NotLogicOP_31);
    
    res_OrLogicOP_26 = (res_OrLogicOP_26 || res_AndLogicOP_29);
    
    res_ImpliesLogicOp_19 = (res_ImpliesLogicOp_19 && res_OrLogicOP_26);
    }
    res_ImpliesLogicOp_15 = (res_ImpliesLogicOp_15 && res_ImpliesLogicOp_19);
    }
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_ImpliesLogicOp_15);
    bool res_OrLogicOP_33 = false;
    bool res_OrLogicOP_34 = false;
    bool res_OrLogicOP_35 = false;
    res_OrLogicOP_35 = (res_OrLogicOP_35 || Timer_Disattivo(L_P1__GetMainc35(my_id)));
    res_OrLogicOP_35 = (res_OrLogicOP_35 || (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_34 = (res_OrLogicOP_34 || res_OrLogicOP_35);
    res_OrLogicOP_34 = (res_OrLogicOP_34 || Timer_Disattivo(L_P1__GetMainc36(my_id)));
    
    res_OrLogicOP_33 = (res_OrLogicOP_33 || res_OrLogicOP_34);
    bool res_NotLogicOP_36 = true;
    res_NotLogicOP_36 = (res_NotLogicOP_36 && ! (L_P1__GetParamMainc8(my_id) == false));
    res_OrLogicOP_33 = (res_OrLogicOP_33 || res_NotLogicOP_36);
    
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_OrLogicOP_33);
    
    res_ImpliesLogicOp_9 = (res_ImpliesLogicOp_9 && res_OrLogicOP_14);
    }
    if(res_ImpliesLogicOp_9){
    xorIndex_res_XorLogicOP_8 = (xorIndex_res_XorLogicOP_8 + 1);
    }
    bool res_OrLogicOP_37 = false;
    bool res_OrLogicOP_38 = false;
    bool res_OrLogicOP_39 = false;
    bool res_AndLogicOP_40 = true;
    bool res_NotLogicOP_41 = true;
    res_NotLogicOP_41 = (res_NotLogicOP_41 && ! Timer_Attivo(L_P1__GetMainc36(my_id)));
    res_AndLogicOP_40 = (res_AndLogicOP_40 && res_NotLogicOP_41);
    bool res_NotLogicOP_42 = true;
    res_NotLogicOP_42 = (res_NotLogicOP_42 && ! (L_P1__GetInMainc4(my_id) == true));
    res_AndLogicOP_40 = (res_AndLogicOP_40 && res_NotLogicOP_42);
    
    res_OrLogicOP_39 = (res_OrLogicOP_39 || res_AndLogicOP_40);
    res_OrLogicOP_39 = (res_OrLogicOP_39 || (Counter_GetValore(L_P1__GetMainc38(my_id)) > 11u));
    
    res_OrLogicOP_38 = (res_OrLogicOP_38 || res_OrLogicOP_39);
    bool res_NotLogicOP_43 = true;
    res_NotLogicOP_43 = (res_NotLogicOP_43 && ! (L_P1__GetParamMainc8(my_id) == false));
    res_OrLogicOP_38 = (res_OrLogicOP_38 || res_NotLogicOP_43);
    
    res_OrLogicOP_37 = (res_OrLogicOP_37 || res_OrLogicOP_38);
    bool res_AndLogicOP_44 = true;
    bool res_NotLogicOP_45 = true;
    bool res_NotLogicOP_46 = true;
    res_NotLogicOP_46 = (res_NotLogicOP_46 && ! (L_P1__GetParamMainc8(my_id) == true));
    res_NotLogicOP_45 = (res_NotLogicOP_45 && ! res_NotLogicOP_46);
    res_AndLogicOP_44 = (res_AndLogicOP_44 && res_NotLogicOP_45);
    bool res_NotLogicOP_47 = true;
    res_NotLogicOP_47 = (res_NotLogicOP_47 && ! Timer_Disattivo(L_P1__GetMainc37(my_id)));
    res_AndLogicOP_44 = (res_AndLogicOP_44 && res_NotLogicOP_47);
    
    res_OrLogicOP_37 = (res_OrLogicOP_37 || res_AndLogicOP_44);
    
    if(res_OrLogicOP_37){
    xorIndex_res_XorLogicOP_8 = (xorIndex_res_XorLogicOP_8 + 1);
    }
    
    res_XorLogicOP_8 = (res_XorLogicOP_8 && (xorIndex_res_XorLogicOP_8 == 1));
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_XorLogicOP_8);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *47,48,49,51,*  *,*  il contatore MainClass_C1_contatore_Co4 sia  uguale a  *53,* 1324
    //   *104,* e  che  *,*  il timer MainClass_C1_timer_T1 non sia scaduto
    //   *104,* o  che  *38,*  il contatore MainClass_C1_contatore_Co4 non sia  diverso da  *56,* 115
    //   *104,* o  che  *34,*  il parametro MainClass_C1_parametro_P3 sia  diverso da  True 
    //   *104,* e  che   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* e  che  *36,*  il timer MainClass_C1_timer_T1 sia attivo
    bool res_OrLogicOP_48 = false;
    bool res_OrLogicOP_49 = false;
    bool res_AndLogicOP_50 = true;
    res_AndLogicOP_50 = (res_AndLogicOP_50 && (Counter_GetValore(L_P1__GetMainc38(my_id)) == 1324u));
    bool res_NotLogicOP_51 = true;
    res_NotLogicOP_51 = (res_NotLogicOP_51 && ! Timer_Scaduto(L_P1__GetMainc35(my_id)));
    res_AndLogicOP_50 = (res_AndLogicOP_50 && res_NotLogicOP_51);
    
    res_OrLogicOP_49 = (res_OrLogicOP_49 || res_AndLogicOP_50);
    bool res_NotLogicOP_52 = true;
    bool res_NotLogicOP_53 = true;
    res_NotLogicOP_53 = (res_NotLogicOP_53 && ! (Counter_GetValore(L_P1__GetMainc38(my_id)) == 115u));
    res_NotLogicOP_52 = (res_NotLogicOP_52 && ! res_NotLogicOP_53);
    res_OrLogicOP_49 = (res_OrLogicOP_49 || res_NotLogicOP_52);
    
    res_OrLogicOP_48 = (res_OrLogicOP_48 || res_OrLogicOP_49);
    bool res_AndLogicOP_54 = true;
    bool res_AndLogicOP_55 = true;
    bool res_NotLogicOP_56 = true;
    res_NotLogicOP_56 = (res_NotLogicOP_56 && ! (L_P1__GetParamMainc8(my_id) == true));
    res_AndLogicOP_55 = (res_AndLogicOP_55 && res_NotLogicOP_56);
    res_AndLogicOP_55 = (res_AndLogicOP_55 && (L_P1__GetInConsd(my_id) == false));
    
    res_AndLogicOP_54 = (res_AndLogicOP_54 && res_AndLogicOP_55);
    res_AndLogicOP_54 = (res_AndLogicOP_54 && Timer_Attivo(L_P1__GetMainc35(my_id)));
    
    res_OrLogicOP_48 = (res_OrLogicOP_48 || res_AndLogicOP_54);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_48);
    
    
    
    return res_AndLogicOP_0;
}


// Macro valorizzate

/*
    CNL corrispondente:
    
    { commento: {[}
     commento: {46,} assegna alla macro il valore Giallox commento: {],}
    }
*/
C1_Enumerat1 L_P1__Macro2(instance_id_t const my_id , C1_Enumerat4 argom, bool argom1, C1_Enumerat4 argom2, C1_Enumerat1 argom3, C1_Enumerat2 argom4, C1_Enumerat1 argom5)
{
return giallox;
}



