// Codice del modello 'TestCase7', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#include "Logica/ClasseMainClass_C1.h"
#include "Logica/ClasseSubClass_C2.h"
#include "Logica/ClasseMainClass_C1_priv.h"
#include "config.h"
#include "scheduler.h"


// ********** Gestione comandi manuali **********

static void L_P1_C1_InitCmdsResponse(instance_id_t const my_id)
{
    // for each manual command of L_P1_C1
    if (L_P1__GetInEvent(my_id)) {
	    L_P1__SetOutEvent3(my_id, LDS_MANCMD_UNEXPECTED);
    } else {
        L_P1__SetOutEvent3(my_id, LDS_MANCMD_NOOP);
    }
    if (L_P1__GetInEvent1(my_id)) {
	    L_P1__SetOutEvent4(my_id, LDS_MANCMD_UNEXPECTED);
    } else {
        L_P1__SetOutEvent4(my_id, LDS_MANCMD_NOOP);
    }
    if (L_P1__GetInEvent2(my_id)) {
	    L_P1__SetOutEvent5(my_id, LDS_MANCMD_UNEXPECTED);
    } else {
        L_P1__SetOutEvent5(my_id, LDS_MANCMD_NOOP);
    }
}

static void L_P1_C1_SetExpectedCmdsResponse(instance_id_t const my_id, C1_Stateenu state)
{        
    switch (state) {
    case C1_St_state:
        // manual commands of L_P1_C1 that can be received in C1_St_state
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
    L_P1__SetMainc15(my_id, gialloxverd);
    L_P1__SetMainc17(my_id, false);
    L_P1__SetMainc19(my_id, rossogiallo1);
    L_P1__SetMainc21(my_id, false);
    L_P1__SetMainc23(my_id, 0);
    L_P1__SetMainc25(my_id, 0);
    L_P1__SetMainc26(my_id, 0);
    L_P1__SetMainc27(my_id, false);
    L_P1__SetMainc28(my_id, false);
    L_P1__SetMainc29(my_id, spento);
    L_P1__SetMainc30(my_id, spento);
    L_P1__SetMainc31(my_id, gialloxverd);
    L_P1__SetMainc32(my_id, gialloxverd);
    L_P1__SetMainc33(my_id, 0);
    L_P1__SetMainc34(my_id, false);
    L_P1__SetMainc35(my_id, false);
    L_P1__SetStato1(my_id, C1_St_Stato);
    // init controlli precedenti
    L_P1__SetMainc12(my_id, rossogiallo2);
    L_P1__SetMainc14(my_id, c180x);
    // init Timer e Counter
    Timer_AggmInit(L_P1__GetMainc36(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc36_ID);
    Timer_Init(L_P1__GetMainc36(my_id), 14000);
    Timer_AggmInit(L_P1__GetMainc37(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc37_ID);
    Timer_Init(L_P1__GetMainc37(my_id), 14000);
    Timer_AggmInit(L_P1__GetMainc38(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc38_ID);
    Timer_Init(L_P1__GetMainc38(my_id), 11000);
    Timer_AggmInit(L_P1__GetMainc39(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc39_ID);
    Timer_Init(L_P1__GetMainc39(my_id), 11000);
    Timer_AggmInit(L_P1__GetMainc40(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc40_ID);
    Timer_Init(L_P1__GetMainc40(my_id), 3530000);
    Timer_AggmInit(L_P1__GetMainc41(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc41_ID);
    Timer_Init(L_P1__GetMainc41(my_id), 5000);
    Counter_AggmInit(L_P1__GetMainc42(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc42_ID);
    Counter_Init(L_P1__GetMainc42(my_id));
    Counter_AggmInit(L_P1__GetMainc43(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc43_ID);
    Counter_Init(L_P1__GetMainc43(my_id));
    Counter_AggmInit(L_P1__GetMainc44(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc44_ID);
    Counter_Init(L_P1__GetMainc44(my_id));
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
    L_P1__SetMainc16(my_id, L_P1__GetMainc15(my_id));
    L_P1__SetMainc18(my_id, L_P1__GetMainc17(my_id));
    L_P1__SetMainc20(my_id, L_P1__GetMainc19(my_id));
    L_P1__SetMainc22(my_id, L_P1__GetMainc21(my_id));
    L_P1__SetMainc24(my_id, L_P1__GetMainc23(my_id));
}

void L_P1_C1_Exec(instance_id_t const my_id, Phase const p)
{
    L_P1_C1_SetResponse(my_id, LDS_SCHED_NOP);
    switch (p) {

    case LDS_PHASE_MANUAL:
        // Reset risposte ai comandi manuali
        L_P1_C1_InitCmdsResponse(my_id);
	L_P1_C1_SetExpectedCmdsResponse(my_id, L_P1_C1_GetState(my_id));
        switch (L_P1_C1_GetState(my_id)) {

        case C1_St_state:
                { } // fine transizioni da state nella fase LDS_PHASE_MANUAL
            break;

        default:
            STOP_EXECUTION(LOGIC_ERROR);
            break;  // Needed for MISRA C syntactic compliance
        } // switch sugli stati chiuso
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
    Timer_Exec(L_P1__GetMainc36(my_id));
    Timer_Exec(L_P1__GetMainc37(my_id));
    Timer_Exec(L_P1__GetMainc38(my_id));
    Timer_Exec(L_P1__GetMainc39(my_id));
    Timer_Exec(L_P1__GetMainc40(my_id));
    Timer_Exec(L_P1__GetMainc41(my_id));
}

void L_P1_C1_GSetSafe(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C1(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C1(proc_id);
    L_P1__SetOutMainc(my_id, avvio);
    L_P1__SetOutMainc1(my_id, false);
    L_P1__SetOutMainc2(my_id, avvio);
    L_P1__SetOutMainc3(my_id, rossogiallo);
    L_P1__SetOutMainc4(my_id, rossogiallo2);
}

void L_P1_C1_GUpdatePrev(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C1(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C1(proc_id);
    L_P1__SetMainc12(my_id, L_P1__GetInMainc11(my_id));
    L_P1__SetMainc14(my_id, L_P1__GetInMainc13(my_id));
    L_P1__SetMainc16(my_id, L_P1__GetMainc15(my_id));
    L_P1__SetMainc18(my_id, L_P1__GetMainc17(my_id));
    L_P1__SetMainc20(my_id, L_P1__GetMainc19(my_id));
    L_P1__SetMainc22(my_id, L_P1__GetMainc21(my_id));
    L_P1__SetMainc24(my_id, L_P1__GetMainc23(my_id));
}

// ********** Definizione macro **********

// Macro di effetto

/*
    CNL corrispondente:
    
    { commento: {36,}  se il timer MainClass_C1_timer_T5 non è attivo commento: {38,} o  se il contatore MainClass_C1_contatore_Co1 è  maggiore di  commento: {54,} 1525 commento: {36,} o  se il timer MainClass_C1_timer_T9 è scaduto commento: {34,} e  se il parametro MainClass_C1_parametro_P9 non è  diverso da  False  commento: {37,} o  se la variabile MainClass_C1_variabile_V1 è  minore di  commento: {55,} 2 commento: {37,} o  se la variabile MainClass_C1_variabile_V5 è  diverso da  True , commento: {72,}Azzera il contatore MainClass_C1_contatore_Co7
    
       
    
    }
*/
void L_P1__Macro(instance_id_t const my_id )
{
//  *36,*  se il timer MainClass_C1_timer_T5 non è attivo *38,* o  se il contatore MainClass_C1_contatore_Co1 è  maggiore di  *54,* 1525 *36,* o  se il timer MainClass_C1_timer_T9 è scaduto *34,* e  se il parametro MainClass_C1_parametro_P9 non è  diverso da  False  *37,* o  se la variabile MainClass_C1_variabile_V1 è  minore di  *55,* 2 *37,* o  se la variabile MainClass_C1_variabile_V5 è  diverso da  True , *72,*Azzera il contatore MainClass_C1_contatore_Co7
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! Timer_Attivo(L_P1__GetMainc40(my_id)));
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_NotLogicOP_4);
    res_OrLogicOP_3 = (res_OrLogicOP_3 || (Counter_GetValore(L_P1__GetMainc42(my_id)) > 1525u));
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    bool res_AndLogicOP_5 = true;
    res_AndLogicOP_5 = (res_AndLogicOP_5 && Timer_Scaduto(L_P1__GetMainc41(my_id)));
    bool res_NotLogicOP_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetParamMainc10(my_id) == false));
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! res_NotLogicOP_7);
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_6);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_5);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_OrLogicOP_2);
    res_OrLogicOP_1 = (res_OrLogicOP_1 || (L_P1__GetMainc33(my_id) < 2u));
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetMainc34(my_id) == true));
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_8);
    
    if(res_OrLogicOP_0){
    
    Counter_Res(L_P1__GetMainc43(my_id));
    }
}


// Macro di verifica

/*
    CNL corrispondente:
    
    { commento: {35,}  se il controllo MainClass_C1_controllo_C8 non è  uguale a RossoGialloGiallo commento: {36,} e  se il timer MainClass_C1_timer_T5 è attivo, Verifica che   commento: {48,49,50,}  commento: {,}  il timer MainClass_C1_timer_T5 sia scaduto
     commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V5 sia  diverso da  True 
     commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C8 non sia  diverso da RossoGialloGiallo
    
    
    }
*/
bool L_P1__Macro2(instance_id_t const my_id , bool argom3, C1_Enumerat2 argom4, bool argom5, bool argom6, bool argom7, C1_Enumerat3 argom8)
{
bool res_AndLogicOP_0 = true;
    
    //  *35,*  se il controllo MainClass_C1_controllo_C8 non è  uguale a RossoGialloGiallo *36,* e  se il timer MainClass_C1_timer_T5 è attivo, Verifica che   *48,49,50,*  *,*  il timer MainClass_C1_timer_T5 sia scaduto
    //   *104,* e  che  *,*  la variabile MainClass_C1_variabile_V5 sia  diverso da  True 
    //   *104,* e  che  *,*  il controllo MainClass_C1_controllo_C8 non sia  diverso da RossoGialloGiallo
    bool res_ImpliesLogicOp_1 = true;
    bool res_AndLogicOP_2 = true;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__GetInMainc5(my_id) == rossogiallo));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_3);
    res_AndLogicOP_2 = (res_AndLogicOP_2 && Timer_Attivo(L_P1__GetMainc40(my_id)));
    
    if(res_AndLogicOP_2){
    bool res_AndLogicOP_4 = true;
    bool res_AndLogicOP_5 = true;
    res_AndLogicOP_5 = (res_AndLogicOP_5 && Timer_Scaduto(L_P1__GetMainc40(my_id)));
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetMainc34(my_id) == true));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_6);
    
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_AndLogicOP_5);
    bool res_NotLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetInMainc5(my_id) == rossogiallo));
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! res_NotLogicOP_8);
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_7);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_AndLogicOP_4);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
    
    { commento: {62,} commento: {36,}  se il timer MainClass_C1_timer_T9 è disattivo commento: {38,} o  se il contatore MainClass_C1_contatore_Co7 è  uguale a  commento: {53,} 14, Almeno una delle seguenti { 
     commento: {36,}  se il timer MainClass_C1_timer_T9 non è scaduto commento: {35,} o  se il controllo MainClass_C1_controllo_C8 è  uguale a RossoGialloGiallo commento: {36,} e  se il timer MainClass_C1_timer_T9 è scaduto commento: {36,} o  se il timer MainClass_C1_timer_T5 non è disattivo commento: {38,} o  se il contatore MainClass_C1_contatore_Co7 non è  minore di  commento: {55,} 11, Verifica che   commento: {49,}  commento: {,}  il timer MainClass_C1_timer_T5 non sia attivo
    
    
     } Verifica che   commento: {50,51,52,}  commento: {,}  la variabile MainClass_C1_variabile_V5 non sia  uguale a  True 
     commento: {104,} o  che  commento: {,}  il contatore MainClass_C1_contatore_Co7 non sia  uguale a  commento: {53,} 155304
     commento: {104,} o  che   l'argomento argomento_ave2 sia  diverso da  True  commento: {,} 
    
    
    }
*/
bool L_P1__Macro3(instance_id_t const my_id , C1_Enumerat3 argom9, bool argom10, C1_Enumerat4 argom11, C1_Enumerat1 argom12, bool argom13, C1_Enumerat3 argom14)
{
bool res_AndLogicOP_0 = true;
    
    //  *62,* *36,*  se il timer MainClass_C1_timer_T9 è disattivo *38,* o  se il contatore MainClass_C1_contatore_Co7 è  uguale a  *53,* 14, Almeno una delle seguenti { 
    //   *36,*  se il timer MainClass_C1_timer_T9 non è scaduto *35,* o  se il controllo MainClass_C1_controllo_C8 è  uguale a RossoGialloGiallo *36,* e  se il timer MainClass_C1_timer_T9 è scaduto *36,* o  se il timer MainClass_C1_timer_T5 non è disattivo *38,* o  se il contatore MainClass_C1_contatore_Co7 non è  minore di  *55,* 11, Verifica che   *49,*  *,*  il timer MainClass_C1_timer_T5 non sia attivo
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    res_OrLogicOP_2 = (res_OrLogicOP_2 || Timer_Disattivo(L_P1__GetMainc41(my_id)));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || (Counter_GetValore(L_P1__GetMainc43(my_id)) == 14u));
    
    if(res_OrLogicOP_2){
    bool res_ImpliesLogicOp_3 = true;
    bool res_OrLogicOP_4 = false;
    bool res_OrLogicOP_5 = false;
    bool res_OrLogicOP_6 = false;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! Timer_Scaduto(L_P1__GetMainc41(my_id)));
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_NotLogicOP_7);
    bool res_AndLogicOP_8 = true;
    res_AndLogicOP_8 = (res_AndLogicOP_8 && (L_P1__GetInMainc5(my_id) == rossogiallo));
    res_AndLogicOP_8 = (res_AndLogicOP_8 && Timer_Scaduto(L_P1__GetMainc41(my_id)));
    
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_AndLogicOP_8);
    
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_OrLogicOP_6);
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! Timer_Disattivo(L_P1__GetMainc40(my_id)));
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_NotLogicOP_9);
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_OrLogicOP_5);
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (Counter_GetValore(L_P1__GetMainc43(my_id)) < 11u));
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_NotLogicOP_10);
    
    if(res_OrLogicOP_4){
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! Timer_Attivo(L_P1__GetMainc40(my_id)));
    res_ImpliesLogicOp_3 = (res_ImpliesLogicOp_3 && res_NotLogicOP_11);
    }
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_ImpliesLogicOp_3);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *50,51,52,*  *,*  la variabile MainClass_C1_variabile_V5 non sia  uguale a  True 
    //   *104,* o  che  *,*  il contatore MainClass_C1_contatore_Co7 non sia  uguale a  *53,* 155304
    //   *104,* o  che   l'argomento argomento_ave2 sia  diverso da  True
    bool res_OrLogicOP_12 = false;
    bool res_OrLogicOP_13 = false;
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1__GetMainc34(my_id) == true));
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_NotLogicOP_14);
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (Counter_GetValore(L_P1__GetMainc43(my_id)) == 155304u));
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_NotLogicOP_15);
    
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_OrLogicOP_13);
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (argom10 == true));
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_NotLogicOP_16);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_12);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
    
    {  se la macro  MainClass_C1_macrova_M9 ( con argomento_a10   uguale a avvio ,argomento_a3   uguale a RossoGialloaVerdea  e argomento_a9   uguale a RossoGialloaVerdea )   è  uguale a  False  commento: {40,}  commento: {36,} e  se il timer MainClass_C1_timer_T9 non è scaduto commento: {36,} o  se il timer MainClass_C1_timer_T9 è disattivo commento: {36,} e  se il timer MainClass_C1_timer_T5 non è disattivo commento: {34,} o  se il parametro MainClass_C1_parametro_P10 non è  diverso da  True  commento: {37,} e  se la variabile MainClass_C1_variabile_V8 è  uguale a  False , Verifica che   commento: {52,}   l'argomento argomento_ave8 sia  diverso da RossoGialloaVerdea commento: {,} 
    
    
    }
*/
bool L_P1__Macro4(instance_id_t const my_id , C1_Enumerat3 argom15, bool argom16, bool argom17, C1_Enumerat2 argom18, C1_Enumerat4 argom19, C1_Enumerat3 argom20, bool argom21)
{
bool res_AndLogicOP_0 = true;
    
    //  se la macro  MainClass_C1_macrova_M9 ( con argomento_a10   uguale a avvio ,argomento_a3   uguale a RossoGialloaVerdea  e argomento_a9   uguale a RossoGialloaVerdea )   è  uguale a  False  *40,*  *36,* e  se il timer MainClass_C1_timer_T9 non è scaduto *36,* o  se il timer MainClass_C1_timer_T9 è disattivo *36,* e  se il timer MainClass_C1_timer_T5 non è disattivo *34,* o  se il parametro MainClass_C1_parametro_P10 non è  diverso da  True  *37,* e  se la variabile MainClass_C1_variabile_V8 è  uguale a  False , Verifica che   *52,*   l'argomento argomento_ave8 sia  diverso da RossoGialloaVerdea
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_AndLogicOP_4 = true;
    res_AndLogicOP_4 = (res_AndLogicOP_4 && (L_P1__Macro1(my_id,avvio,rossogiallo2,rossogiallo2) == false));
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! Timer_Scaduto(L_P1__GetMainc41(my_id)));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_5);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_AndLogicOP_4);
    bool res_AndLogicOP_6 = true;
    res_AndLogicOP_6 = (res_AndLogicOP_6 && Timer_Disattivo(L_P1__GetMainc41(my_id)));
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! Timer_Disattivo(L_P1__GetMainc40(my_id)));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_7);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_AndLogicOP_6);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    bool res_AndLogicOP_8 = true;
    bool res_NotLogicOP_9 = true;
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__GetParamMainc6(my_id) == true));
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! res_NotLogicOP_10);
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_9);
    res_AndLogicOP_8 = (res_AndLogicOP_8 && (L_P1__GetMainc35(my_id) == false));
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_8);
    
    if(res_OrLogicOP_2){
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (argom20 == rossogiallo2));
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_NotLogicOP_11);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    
    
    return res_AndLogicOP_0;
}


// Macro valorizzate

/*
    CNL corrispondente:
    
    { commento: {[}  se il controllo ConsDef è uguale a FALSE   commento: {36,} o  se il timer MainClass_C1_timer_T9 non è disattivo o  se l'argomento argomento_a10 non  è  diverso da avvio commento: {39,}  commento: {35,} o  se il controllo MainClass_C1_controllo_C8 non è  uguale a RossoGialloGiallo , assegna alla macro il valore  False 
    
     commento: {46,} assegna alla macro il valore  False  commento: {],}
    }
*/
bool L_P1__Macro1(instance_id_t const my_id , C1_Enumerat1 argom, C1_Enumerat3 argom1, C1_Enumerat3 argom2)
{
bool res_macro_val;
    
    //  *[*  se il controllo ConsDef è uguale a FALSE   *36,* o  se il timer MainClass_C1_timer_T9 non è disattivo o  se l'argomento argomento_a10 non  è  diverso da avvio *39,*  *35,* o  se il controllo MainClass_C1_controllo_C8 non è  uguale a RossoGialloGiallo
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_OrLogicOP_2 = false;
    res_OrLogicOP_2 = (res_OrLogicOP_2 || (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! Timer_Disattivo(L_P1__GetMainc41(my_id)));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_3);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_OrLogicOP_2);
    bool res_NotLogicOP_4 = true;
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (argom == avvio));
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! res_NotLogicOP_5);
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_NotLogicOP_4);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetInMainc5(my_id) == rossogiallo));
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_6);
    
    if(res_OrLogicOP_0){
    
    res_macro_val = false;
    }
    else{
    res_macro_val = false;
    }
    return res_macro_val;
}



