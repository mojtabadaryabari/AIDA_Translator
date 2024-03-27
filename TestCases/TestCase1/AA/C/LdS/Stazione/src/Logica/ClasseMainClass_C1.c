// Codice del modello 'TestCase1', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
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
	    L_P1__SetOutEvent2(my_id, LDS_MANCMD_UNEXPECTED);
    } else {
        L_P1__SetOutEvent2(my_id, LDS_MANCMD_NOOP);
    }
    if (L_P1__GetInEvent1(my_id)) {
	    L_P1__SetOutEvent3(my_id, LDS_MANCMD_UNEXPECTED);
    } else {
        L_P1__SetOutEvent3(my_id, LDS_MANCMD_NOOP);
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
    L_P1__SetMainc14(my_id, 0);
    L_P1__SetMainc16(my_id, 0);
    L_P1__SetMainc18(my_id, false);
    L_P1__SetMainc20(my_id, false);
    L_P1__SetMainc21(my_id, false);
    L_P1__SetMainc22(my_id, rossoverde);
    L_P1__SetMainc23(my_id, rossoverde);
    L_P1__SetMainc24(my_id, false);
    L_P1__SetMainc25(my_id, false);
    L_P1__SetMainc26(my_id, 0);
    L_P1__SetStato1(my_id, C1_St_Stato);
    // init controlli precedenti
    L_P1__SetMainc11(my_id, true);
    L_P1__SetMainc13(my_id, false);
    // init Timer e Counter
    Timer_AggmInit(L_P1__GetMainc27(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc27_ID);
    Timer_Init(L_P1__GetMainc27(my_id), 1000);
    Timer_AggmInit(L_P1__GetMainc28(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc28_ID);
    Timer_Init(L_P1__GetMainc28(my_id), 1000);
    Timer_AggmInit(L_P1__GetMainc29(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc29_ID);
    Timer_Init(L_P1__GetMainc29(my_id), 40000);
    Timer_AggmInit(L_P1__GetMainc30(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc30_ID);
    Timer_Init(L_P1__GetMainc30(my_id), 55321000);
    Counter_AggmInit(L_P1__GetMainc31(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc31_ID);
    Counter_Init(L_P1__GetMainc31(my_id));
    Counter_AggmInit(L_P1__GetMainc32(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc32_ID);
    Counter_Init(L_P1__GetMainc32(my_id));
    Counter_AggmInit(L_P1__GetMainc33(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc33_ID);
    Counter_Init(L_P1__GetMainc33(my_id));
    Counter_AggmInit(L_P1__GetMainc34(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc34_ID);
    Counter_Init(L_P1__GetMainc34(my_id));
    Counter_AggmInit(L_P1__GetMainc35(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc35_ID);
    Counter_Init(L_P1__GetMainc35(my_id));
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
    L_P1__SetMainc15(my_id, L_P1__GetMainc14(my_id));
    L_P1__SetMainc17(my_id, L_P1__GetMainc16(my_id));
    L_P1__SetMainc19(my_id, L_P1__GetMainc18(my_id));
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
    Timer_Exec(L_P1__GetMainc27(my_id));
    Timer_Exec(L_P1__GetMainc28(my_id));
    Timer_Exec(L_P1__GetMainc29(my_id));
    Timer_Exec(L_P1__GetMainc30(my_id));
}

void L_P1_C1_GSetSafe(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C1(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C1(proc_id);
    L_P1__SetOutMainc(my_id, c270xx);
    L_P1__SetOutMainc1(my_id, giallogiall);
    L_P1__SetOutMainc2(my_id, false);
    L_P1__SetOutMainc3(my_id, giallogiall);
}

void L_P1_C1_GUpdatePrev(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C1(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C1(proc_id);
    L_P1__SetMainc11(my_id, L_P1__GetInMainc10(my_id));
    L_P1__SetMainc13(my_id, L_P1__GetInMainc12(my_id));
    L_P1__SetMainc15(my_id, L_P1__GetMainc14(my_id));
    L_P1__SetMainc17(my_id, L_P1__GetMainc16(my_id));
    L_P1__SetMainc19(my_id, L_P1__GetMainc18(my_id));
}

// ********** Definizione macro **********

// Macro di effetto

/*
    CNL corrispondente:
    
    {  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} e  se la variabile MainClass_C1_variabile_V10 è  minore di  commento: {55,} 7 commento: {36,} o  se il timer MainClass_C1_timer_T7 non è scaduto commento: {38,} e  se il contatore MainClass_C1_contatore_Co10 è  diverso da  commento: {56,} 115321, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V10 il valore 9
    
       
     commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è disattivo commento: {37,} e  se la variabile MainClass_C1_variabile_V10 non è  maggiore di  commento: {54,} 2 commento: {37,} o  se la variabile MainClass_C1_variabile_V10 è  minore di  commento: {55,} 1 commento: {38,} o  se il contatore MainClass_C1_contatore_Co4 non è  minore di  commento: {55,} 130, commento: {66,} Assegna al comando MainClass_C1_comando_C10 il valore GialloGiallo
    
       
     commento: {34,}  se il parametro MainClass_C1_parametro_P4 è  diverso da RossoGialloGiallo commento: {34,} e  se il parametro MainClass_C1_parametro_P8 non è  diverso da  commento: {56,} 8 commento: {38,} e  se il contatore MainClass_C1_contatore_Co4 è  maggiore di  commento: {54,} 13 commento: {36,} o  se il timer MainClass_C1_timer_T5 è disattivo commento: {38,} e  se il contatore MainClass_C1_contatore_Co4 è  uguale a  commento: {53,} 11 commento: {38,} o  se il contatore MainClass_C1_contatore_Co10 è  maggiore di  commento: {54,} 134532, commento: {68,}Attiva il timer MainClass_C1_timer_T7
    
     ,altrimenti   commento: {67,} Assegna alla variabile MainClass_C1_variabile_V10 il valore 4 commento: {67,}
    
    
     commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è scaduto commento: {37,} o  se la variabile MainClass_C1_variabile_V10 è  diverso da  commento: {56,} 4, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V10 il valore 2
    
     ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V10 il valore 6
    
    
    
    }
*/
void L_P1__Macro(instance_id_t const my_id )
{
//  se il controllo ConsDef  è  uguale a FALSE  *37,* e  se la variabile MainClass_C1_variabile_V10 è  minore di  *55,* 7 *36,* o  se il timer MainClass_C1_timer_T7 non è scaduto *38,* e  se il contatore MainClass_C1_contatore_Co10 è  diverso da  *56,* 115321, *67,* Assegna alla variabile MainClass_C1_variabile_V10 il valore 9
    bool res_OrLogicOP_0 = false;
    bool res_AndLogicOP_1 = true;
    res_AndLogicOP_1 = (res_AndLogicOP_1 && (L_P1__GetInConsd(my_id) == false));
    res_AndLogicOP_1 = (res_AndLogicOP_1 && (L_P1__GetMainc26(my_id) < 7u));
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_1);
    bool res_AndLogicOP_2 = true;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! Timer_Scaduto(L_P1__GetMainc30(my_id)));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_3);
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (Counter_GetValore(L_P1__GetMainc32(my_id)) == 115321u));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_4);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_2);
    
    if(res_OrLogicOP_0){
    
    L_P1__SetMainc26(my_id,9u);
    }
    //  *110,*  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è disattivo *37,* e  se la variabile MainClass_C1_variabile_V10 non è  maggiore di  *54,* 2 *37,* o  se la variabile MainClass_C1_variabile_V10 è  minore di  *55,* 1 *38,* o  se il contatore MainClass_C1_contatore_Co4 non è  minore di  *55,* 130, *66,* Assegna al comando MainClass_C1_comando_C10 il valore GialloGiallo
    bool res_OrLogicOP_5 = false;
    bool res_OrLogicOP_6 = false;
    bool res_AndLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! Timer_Disattivo(L_P1__GetMainc28(my_id)));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_8);
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetMainc26(my_id) > 2u));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_9);
    
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_AndLogicOP_7);
    res_OrLogicOP_6 = (res_OrLogicOP_6 || (L_P1__GetMainc26(my_id) < 1u));
    
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_OrLogicOP_6);
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (Counter_GetValore(L_P1__GetMainc34(my_id)) < 130u));
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_NotLogicOP_10);
    
    if(res_OrLogicOP_5){
    
    L_P1__SetOutMainc1(my_id,giallogiall);
    }
    //  *34,*  se il parametro MainClass_C1_parametro_P4 è  diverso da RossoGialloGiallo *34,* e  se il parametro MainClass_C1_parametro_P8 non è  diverso da  *56,* 8 *38,* e  se il contatore MainClass_C1_contatore_Co4 è  maggiore di  *54,* 13 *36,* o  se il timer MainClass_C1_timer_T5 è disattivo *38,* e  se il contatore MainClass_C1_contatore_Co4 è  uguale a  *53,* 11 *38,* o  se il contatore MainClass_C1_contatore_Co10 è  maggiore di  *54,* 134532, *68,*Attiva il timer MainClass_C1_timer_T7
    // ,altrimenti   *67,* Assegna alla variabile MainClass_C1_variabile_V10 il valore 4
    bool res_OrLogicOP_11 = false;
    bool res_OrLogicOP_12 = false;
    bool res_AndLogicOP_13 = true;
    bool res_AndLogicOP_14 = true;
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (L_P1__GetParamMainc7(my_id) == rossogiallo));
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_NotLogicOP_15);
    bool res_NotLogicOP_16 = true;
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! (L_P1__GetParamMainc9(my_id) == 8u));
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! res_NotLogicOP_17);
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_NotLogicOP_16);
    
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_AndLogicOP_14);
    res_AndLogicOP_13 = (res_AndLogicOP_13 && (Counter_GetValore(L_P1__GetMainc34(my_id)) > 13u));
    
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_AndLogicOP_13);
    bool res_AndLogicOP_18 = true;
    res_AndLogicOP_18 = (res_AndLogicOP_18 && Timer_Disattivo(L_P1__GetMainc29(my_id)));
    res_AndLogicOP_18 = (res_AndLogicOP_18 && (Counter_GetValore(L_P1__GetMainc34(my_id)) == 11u));
    
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_AndLogicOP_18);
    
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_OrLogicOP_12);
    res_OrLogicOP_11 = (res_OrLogicOP_11 || (Counter_GetValore(L_P1__GetMainc32(my_id)) > 134532u));
    
    if(res_OrLogicOP_11){
    
    Timer_Attiva(L_P1__GetMainc30(my_id));
    }else{
    
    L_P1__SetMainc26(my_id,4u);
    }
    //  *67,*
    // *110,*  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è scaduto *37,* o  se la variabile MainClass_C1_variabile_V10 è  diverso da  *56,* 4, *67,* Assegna alla variabile MainClass_C1_variabile_V10 il valore 2
    // ,altrimenti  *67,* Assegna alla variabile MainClass_C1_variabile_V10 il valore 6
    bool res_OrLogicOP_19 = false;
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! Timer_Scaduto(L_P1__GetMainc28(my_id)));
    res_OrLogicOP_19 = (res_OrLogicOP_19 || res_NotLogicOP_20);
    bool res_NotLogicOP_21 = true;
    res_NotLogicOP_21 = (res_NotLogicOP_21 && ! (L_P1__GetMainc26(my_id) == 4u));
    res_OrLogicOP_19 = (res_OrLogicOP_19 || res_NotLogicOP_21);
    
    if(res_OrLogicOP_19){
    
    L_P1__SetMainc26(my_id,2u);
    }else{
    
    L_P1__SetMainc26(my_id,6u);
    }
}

/*
    CNL corrispondente:
    
    { commento: {36,}  se il timer MainClass_C1_timer_T7 non è scaduto commento: {38,} o  se il contatore MainClass_C1_contatore_Co4 è  uguale a  commento: {53,} 11, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V10 il valore 8
    
     ,altrimenti  commento: {66,} Assegna al comando MainClass_C1_comando_C10 il valore GialloGiallo
    
    
     commento: {38,}  se il contatore MainClass_C1_contatore_Co4 è  diverso da  commento: {56,} 15 commento: {36,} e  se il timer MainClass_C1_timer_T5 non è attivo commento: {37,} o  se la variabile MainClass_C1_variabile_V10 è  maggiore di  commento: {54,} 4, commento: {66,} Assegna al comando MainClass_C1_comando_C10 il valore GialloGiallo
    
       
     commento: {34,}  se il parametro MainClass_C1_parametro_P6 non è  diverso da RossoGialloGiallo commento: {38,} o  se il contatore MainClass_C1_contatore_Co10 non è  maggiore di  commento: {54,} 114532, commento: {66,} Assegna al comando MainClass_C1_comando_C1 il valore c270xx
    
       
    
    }
*/
void L_P1__Macro1(instance_id_t const my_id )
{
//  *36,*  se il timer MainClass_C1_timer_T7 non è scaduto *38,* o  se il contatore MainClass_C1_contatore_Co4 è  uguale a  *53,* 11, *67,* Assegna alla variabile MainClass_C1_variabile_V10 il valore 8
    // ,altrimenti  *66,* Assegna al comando MainClass_C1_comando_C10 il valore GialloGiallo
    bool res_OrLogicOP_0 = false;
    bool res_NotLogicOP_1 = true;
    res_NotLogicOP_1 = (res_NotLogicOP_1 && ! Timer_Scaduto(L_P1__GetMainc30(my_id)));
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_1);
    res_OrLogicOP_0 = (res_OrLogicOP_0 || (Counter_GetValore(L_P1__GetMainc34(my_id)) == 11u));
    
    if(res_OrLogicOP_0){
    
    L_P1__SetMainc26(my_id,8u);
    }else{
    
    L_P1__SetOutMainc1(my_id,giallogiall);
    }
    //  *38,*  se il contatore MainClass_C1_contatore_Co4 è  diverso da  *56,* 15 *36,* e  se il timer MainClass_C1_timer_T5 non è attivo *37,* o  se la variabile MainClass_C1_variabile_V10 è  maggiore di  *54,* 4, *66,* Assegna al comando MainClass_C1_comando_C10 il valore GialloGiallo
    bool res_OrLogicOP_2 = false;
    bool res_AndLogicOP_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (Counter_GetValore(L_P1__GetMainc34(my_id)) == 15u));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_4);
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! Timer_Attivo(L_P1__GetMainc29(my_id)));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_5);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_3);
    res_OrLogicOP_2 = (res_OrLogicOP_2 || (L_P1__GetMainc26(my_id) > 4u));
    
    if(res_OrLogicOP_2){
    
    L_P1__SetOutMainc1(my_id,giallogiall);
    }
    //  *34,*  se il parametro MainClass_C1_parametro_P6 non è  diverso da RossoGialloGiallo *38,* o  se il contatore MainClass_C1_contatore_Co10 non è  maggiore di  *54,* 114532, *66,* Assegna al comando MainClass_C1_comando_C1 il valore c270xx
    bool res_OrLogicOP_6 = false;
    bool res_NotLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetParamMainc8(my_id) == rossogiallo));
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! res_NotLogicOP_8);
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_NotLogicOP_7);
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (Counter_GetValore(L_P1__GetMainc32(my_id)) > 114532u));
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_NotLogicOP_9);
    
    if(res_OrLogicOP_6){
    
    L_P1__SetOutMainc(my_id,c270xx);
    }
}

/*
    CNL corrispondente:
     
    {  se il controllo ConsDef  è  uguale a FALSE , commento: {67,} Assegna alla variabile MainClass_C1_variabile_V10 il valore 7
    
     ,altrimenti  commento: {70,}Incrementa il contatore MainClass_C1_contatore_Co4
    
    
      se il controllo ConsDef  è  uguale a FALSE  commento: {37,} e  se la variabile MainClass_C1_variabile_V10 è  diverso da  commento: {56,} 9 commento: {34,} e  se il parametro MainClass_C1_parametro_P3 non è  diverso da  commento: {56,} 9 commento: {34,} e  se il parametro MainClass_C1_parametro_P3 non è  diverso da  commento: {56,} 7 e  se il controllo ConsDef  è  uguale a FALSE , commento: {70,}Incrementa il contatore MainClass_C1_contatore_Co1
    
     ,altrimenti  commento: {66,} Assegna al comando MainClass_C1_comando_C1 il valore c270xx
    
    
     commento: {38,}  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  commento: {56,} 1310 commento: {35,} e  se il controllo MainClass_C1_controllo_C7 non è  uguale a GialloGiallo commento: {34,} e  se il parametro MainClass_C1_parametro_P1 non è  minore di  commento: {55,} 9 commento: {35,} o  se il controllo MainClass_C1_controllo_C7 è  uguale a GialloGiallo commento: {36,} o  se il timer MainClass_C1_timer_T5 è disattivo,  Applica gli effetti
           della macro MainClass_C1_macroef_M4  commento: {73,}
    
       
      se il controllo ConsDef  è  uguale a FALSE  commento: {34,} o  se il parametro MainClass_C1_parametro_P3 non è  maggiore di  commento: {54,} 7 commento: {36,} o  se il timer MainClass_C1_timer_T7 non è attivo commento: {36,} o  se il timer MainClass_C1_timer_T7 è attivo commento: {36,} e  se il timer MainClass_C1_timer_T7 è disattivo, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V10 il valore 3
    
     ,altrimenti  commento: {66,} Assegna al comando MainClass_C1_comando_C1 il valore c270xx
    
    
      se il ripristino dello stato  è  uguale a  commento: {53,}  state1  commento: {107,} o  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} e  se il controllo MainClass_C1_controllo_C7 non è  uguale a GialloGiallo o  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} o  se il timer MainClass_C1_timer_T5 non è scaduto, commento: {68,}Attiva il timer MainClass_C1_timer_T5
    
       
    
    }
*/
void L_P1__Macro2(instance_id_t const my_id )
{
//  se il controllo ConsDef  è  uguale a FALSE , *67,* Assegna alla variabile MainClass_C1_variabile_V10 il valore 7
    // ,altrimenti  *70,*Incrementa il contatore MainClass_C1_contatore_Co4
    if((L_P1__GetInConsd(my_id) == false)){
    
    L_P1__SetMainc26(my_id,7u);
    }else{
    
    Counter_Incr(L_P1__GetMainc34(my_id));
    }
    //  se il controllo ConsDef  è  uguale a FALSE  *37,* e  se la variabile MainClass_C1_variabile_V10 è  diverso da  *56,* 9 *34,* e  se il parametro MainClass_C1_parametro_P3 non è  diverso da  *56,* 9 *34,* e  se il parametro MainClass_C1_parametro_P3 non è  diverso da  *56,* 7 e  se il controllo ConsDef  è  uguale a FALSE , *70,*Incrementa il contatore MainClass_C1_contatore_Co1
    // ,altrimenti  *66,* Assegna al comando MainClass_C1_comando_C1 il valore c270xx
    bool res_AndLogicOP_0 = true;
    bool res_AndLogicOP_1 = true;
    bool res_AndLogicOP_2 = true;
    bool res_AndLogicOP_3 = true;
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetMainc26(my_id) == 9u));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_4);
    
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_AndLogicOP_3);
    bool res_NotLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetParamMainc6(my_id) == 9u));
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! res_NotLogicOP_6);
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_5);
    
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_AndLogicOP_2);
    bool res_NotLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetParamMainc6(my_id) == 7u));
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! res_NotLogicOP_8);
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_7);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_AndLogicOP_1);
    res_AndLogicOP_0 = (res_AndLogicOP_0 && (L_P1__GetInConsd(my_id) == false));
    
    if(res_AndLogicOP_0){
    
    Counter_Incr(L_P1__GetMainc31(my_id));
    }else{
    
    L_P1__SetOutMainc(my_id,c270xx);
    }
    //  *38,*  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  *56,* 1310 *35,* e  se il controllo MainClass_C1_controllo_C7 non è  uguale a GialloGiallo *34,* e  se il parametro MainClass_C1_parametro_P1 non è  minore di  *55,* 9 *35,* o  se il controllo MainClass_C1_controllo_C7 è  uguale a GialloGiallo *36,* o  se il timer MainClass_C1_timer_T5 è disattivo,  Applica gli effetti
    //       della macro MainClass_C1_macroef_M4
    bool res_OrLogicOP_9 = false;
    bool res_OrLogicOP_10 = false;
    bool res_AndLogicOP_11 = true;
    bool res_AndLogicOP_12 = true;
    bool res_NotLogicOP_13 = true;
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (Counter_GetValore(L_P1__GetMainc34(my_id)) == 1310u));
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! res_NotLogicOP_14);
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_NotLogicOP_13);
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (L_P1__GetInMainc4(my_id) == giallogiall));
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_NotLogicOP_15);
    
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_AndLogicOP_12);
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (L_P1__GetParamMainc5(my_id) < 9u));
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_NotLogicOP_16);
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_AndLogicOP_11);
    res_OrLogicOP_10 = (res_OrLogicOP_10 || (L_P1__GetInMainc4(my_id) == giallogiall));
    
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_OrLogicOP_10);
    res_OrLogicOP_9 = (res_OrLogicOP_9 || Timer_Disattivo(L_P1__GetMainc29(my_id)));
    
    if(res_OrLogicOP_9){
    
    L_P1__Macro1(my_id);
    }
    //  *73,*
    //   
    //  se il controllo ConsDef  è  uguale a FALSE  *34,* o  se il parametro MainClass_C1_parametro_P3 non è  maggiore di  *54,* 7 *36,* o  se il timer MainClass_C1_timer_T7 non è attivo *36,* o  se il timer MainClass_C1_timer_T7 è attivo *36,* e  se il timer MainClass_C1_timer_T7 è disattivo, *67,* Assegna alla variabile MainClass_C1_variabile_V10 il valore 3
    // ,altrimenti  *66,* Assegna al comando MainClass_C1_comando_C1 il valore c270xx
    bool res_OrLogicOP_17 = false;
    bool res_OrLogicOP_18 = false;
    bool res_OrLogicOP_19 = false;
    res_OrLogicOP_19 = (res_OrLogicOP_19 || (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! (L_P1__GetParamMainc6(my_id) > 7u));
    res_OrLogicOP_19 = (res_OrLogicOP_19 || res_NotLogicOP_20);
    
    res_OrLogicOP_18 = (res_OrLogicOP_18 || res_OrLogicOP_19);
    bool res_NotLogicOP_21 = true;
    res_NotLogicOP_21 = (res_NotLogicOP_21 && ! Timer_Attivo(L_P1__GetMainc30(my_id)));
    res_OrLogicOP_18 = (res_OrLogicOP_18 || res_NotLogicOP_21);
    
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_OrLogicOP_18);
    bool res_AndLogicOP_22 = true;
    res_AndLogicOP_22 = (res_AndLogicOP_22 && Timer_Attivo(L_P1__GetMainc30(my_id)));
    res_AndLogicOP_22 = (res_AndLogicOP_22 && Timer_Disattivo(L_P1__GetMainc30(my_id)));
    
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_AndLogicOP_22);
    
    if(res_OrLogicOP_17){
    
    L_P1__SetMainc26(my_id,3u);
    }else{
    
    L_P1__SetOutMainc(my_id,c270xx);
    }
    //  se il ripristino dello stato  è  uguale a  *53,*  state1  *107,* o  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  *35,* e  se il controllo MainClass_C1_controllo_C7 non è  uguale a GialloGiallo o  se il controllo ConsDef  è  uguale a FALSE  *36,* o  se il timer MainClass_C1_timer_T5 non è scaduto, *68,*Attiva il timer MainClass_C1_timer_T5
    bool res_OrLogicOP_23 = false;
    bool res_OrLogicOP_24 = false;
    bool res_OrLogicOP_25 = false;
    bool res_OrLogicOP_26 = false;
    res_OrLogicOP_26 = (res_OrLogicOP_26 || (L_P1__GetStato1(my_id) == C1_St_state));
    res_OrLogicOP_26 = (res_OrLogicOP_26 || (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_25 = (res_OrLogicOP_25 || res_OrLogicOP_26);
    bool res_AndLogicOP_27 = true;
    res_AndLogicOP_27 = (res_AndLogicOP_27 && (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_28 = true;
    res_NotLogicOP_28 = (res_NotLogicOP_28 && ! (L_P1__GetInMainc4(my_id) == giallogiall));
    res_AndLogicOP_27 = (res_AndLogicOP_27 && res_NotLogicOP_28);
    
    res_OrLogicOP_25 = (res_OrLogicOP_25 || res_AndLogicOP_27);
    
    res_OrLogicOP_24 = (res_OrLogicOP_24 || res_OrLogicOP_25);
    res_OrLogicOP_24 = (res_OrLogicOP_24 || (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_23 = (res_OrLogicOP_23 || res_OrLogicOP_24);
    bool res_NotLogicOP_29 = true;
    res_NotLogicOP_29 = (res_NotLogicOP_29 && ! Timer_Scaduto(L_P1__GetMainc29(my_id)));
    res_OrLogicOP_23 = (res_OrLogicOP_23 || res_NotLogicOP_29);
    
    if(res_OrLogicOP_23){
    
    Timer_Attiva(L_P1__GetMainc29(my_id));
    }
}

/*
    CNL corrispondente:
    
    {  se il ripristino dello stato  non è  diverso da  commento: {56,}  state1  commento: {107,} commento: {38,} o  se il contatore MainClass_C1_contatore_Co1 non è  minore di  commento: {55,} 1310,  Applica gli effetti
           della macro MainClass_C1_macroef_M2  commento: {73,}
    
       
     commento: {34,}  se lo stato  è  uguale a  commento: {53,}  state1  commento: {106,}, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V10 il valore 8
    
       
      se il controllo ConsDef è uguale a FALSE , commento: {69,}Disattiva il timer MainClass_C1_timer_T5
    
       
     commento: {38,}  se il contatore MainClass_C1_contatore_Co3 è  diverso da  commento: {56,} 1145 commento: {38,} o  se il contatore MainClass_C1_contatore_Co10 è  uguale a  commento: {53,} 133210 commento: {34,} e  se il parametro MainClass_C1_parametro_P6 è  uguale a RossoGialloGiallo e  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} o  se il parametro MainClass_C1_parametro_P3 è  minore di  commento: {55,} 9, commento: {66,} Assegna al comando MainClass_C1_comando_C4 il valore  False 
    
     ,altrimenti  commento: {69,}Disattiva il timer MainClass_C1_timer_T5
    
    
     commento: {35,}  se il controllo MainClass_C1_controllo_C7 è  diverso da GialloGiallo, commento: {71,}Decrementa il contatore MainClass_C1_contatore_Co10
    
       
    
    }
*/
void L_P1__Macro3(instance_id_t const my_id )
{
//  se il ripristino dello stato  non è  diverso da  *56,*  state1  *107,* *38,* o  se il contatore MainClass_C1_contatore_Co1 non è  minore di  *55,* 1310,  Applica gli effetti
    //       della macro MainClass_C1_macroef_M2
    bool res_OrLogicOP_0 = false;
    bool res_NotLogicOP_1 = true;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (L_P1__GetStato1(my_id) == C1_St_state));
    res_NotLogicOP_1 = (res_NotLogicOP_1 && ! res_NotLogicOP_2);
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_1);
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (Counter_GetValore(L_P1__GetMainc31(my_id)) < 1310u));
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_3);
    
    if(res_OrLogicOP_0){
    
    L_P1__Macro(my_id);
    }
    //  *73,*
    //   
    // *34,*  se lo stato  è  uguale a  *53,*  state1  *106,*, *67,* Assegna alla variabile MainClass_C1_variabile_V10 il valore 8
    if((L_P1_C1_GetState(my_id) == C1_St_state)){
    
    L_P1__SetMainc26(my_id,8u);
    }
    //  se il controllo ConsDef è uguale a FALSE , *69,*Disattiva il timer MainClass_C1_timer_T5
    if((L_P1__GetInConsd(my_id) == false)){
    
    Timer_Disattiva(L_P1__GetMainc29(my_id));
    }
    //  *38,*  se il contatore MainClass_C1_contatore_Co3 è  diverso da  *56,* 1145 *38,* o  se il contatore MainClass_C1_contatore_Co10 è  uguale a  *53,* 133210 *34,* e  se il parametro MainClass_C1_parametro_P6 è  uguale a RossoGialloGiallo e  se il controllo ConsDef  è  uguale a FALSE  *34,* o  se il parametro MainClass_C1_parametro_P3 è  minore di  *55,* 9, *66,* Assegna al comando MainClass_C1_comando_C4 il valore  False 
    // ,altrimenti  *69,*Disattiva il timer MainClass_C1_timer_T5
    bool res_OrLogicOP_4 = false;
    bool res_OrLogicOP_5 = false;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (Counter_GetValore(L_P1__GetMainc33(my_id)) == 1145u));
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_NotLogicOP_6);
    bool res_AndLogicOP_7 = true;
    bool res_AndLogicOP_8 = true;
    res_AndLogicOP_8 = (res_AndLogicOP_8 && (Counter_GetValore(L_P1__GetMainc32(my_id)) == 133210u));
    res_AndLogicOP_8 = (res_AndLogicOP_8 && (L_P1__GetParamMainc8(my_id) == rossogiallo));
    
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_AndLogicOP_8);
    res_AndLogicOP_7 = (res_AndLogicOP_7 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_AndLogicOP_7);
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_OrLogicOP_5);
    res_OrLogicOP_4 = (res_OrLogicOP_4 || (L_P1__GetParamMainc6(my_id) < 9u));
    
    if(res_OrLogicOP_4){
    
    L_P1__SetOutMainc2(my_id,false);
    }else{
    
    Timer_Disattiva(L_P1__GetMainc29(my_id));
    }
    //  *35,*  se il controllo MainClass_C1_controllo_C7 è  diverso da GialloGiallo, *71,*Decrementa il contatore MainClass_C1_contatore_Co10
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetInMainc4(my_id) == giallogiall));
    if(res_NotLogicOP_9){
    
    Counter_Decr(L_P1__GetMainc32(my_id));
    }
}


// Macro di verifica

/*
    CNL corrispondente:
    
    { commento: {34,}  se il parametro MainClass_C1_parametro_P6 non è  diverso da RossoGialloGiallo commento: {36,} o  se il timer MainClass_C1_timer_T5 non è disattivo commento: {36,} e  se il timer MainClass_C1_timer_T7 non è scaduto commento: {35,} e  se il controllo MainClass_C1_controllo_C7 è  uguale a GialloGiallo commento: {37,} e  se la variabile MainClass_C1_variabile_V10 è  diverso da  commento: {56,} 3, Verifica che   commento: {47,50,}  commento: {34,}  il parametro MainClass_C1_parametro_P8 sia  minore di  commento: {55,} 3
     commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V10 sia  minore di  commento: {55,} 9
     commento: {104,} o  che  commento: {37,}  la variabile MainClass_C1_variabile_V10 sia  diverso da  commento: {56,} 9
    
    
    }
*/
bool L_P1__Macro6(instance_id_t const my_id , C1_Enumerat4 argom9, C1_Enumerat4 argom10)
{
bool res_AndLogicOP_0 = true;
    
    //  *34,*  se il parametro MainClass_C1_parametro_P6 non è  diverso da RossoGialloGiallo *36,* o  se il timer MainClass_C1_timer_T5 non è disattivo *36,* e  se il timer MainClass_C1_timer_T7 non è scaduto *35,* e  se il controllo MainClass_C1_controllo_C7 è  uguale a GialloGiallo *37,* e  se la variabile MainClass_C1_variabile_V10 è  diverso da  *56,* 3, Verifica che   *47,50,*  *34,*  il parametro MainClass_C1_parametro_P8 sia  minore di  *55,* 3
    //   *104,* o  che  *,*  la variabile MainClass_C1_variabile_V10 sia  minore di  *55,* 9
    //   *104,* o  che  *37,*  la variabile MainClass_C1_variabile_V10 sia  diverso da  *56,* 9
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_NotLogicOP_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetParamMainc8(my_id) == rossogiallo));
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! res_NotLogicOP_4);
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_3);
    bool res_AndLogicOP_5 = true;
    bool res_AndLogicOP_6 = true;
    bool res_AndLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! Timer_Disattivo(L_P1__GetMainc29(my_id)));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_8);
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! Timer_Scaduto(L_P1__GetMainc30(my_id)));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_9);
    
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_AndLogicOP_7);
    res_AndLogicOP_6 = (res_AndLogicOP_6 && (L_P1__GetInMainc4(my_id) == giallogiall));
    
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_AndLogicOP_6);
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__GetMainc26(my_id) == 3u));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_10);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_5);
    
    if(res_OrLogicOP_2){
    bool res_OrLogicOP_11 = false;
    bool res_OrLogicOP_12 = false;
    res_OrLogicOP_12 = (res_OrLogicOP_12 || (L_P1__GetParamMainc9(my_id) < 3u));
    res_OrLogicOP_12 = (res_OrLogicOP_12 || (L_P1__GetMainc26(my_id) < 9u));
    
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_OrLogicOP_12);
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (L_P1__GetMainc26(my_id) == 9u));
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_NotLogicOP_13);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_OrLogicOP_11);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
     
    { commento: {61,} commento: {34,}  se lo stato  è  uguale a  commento: {53,}  state1  commento: {106,} commento: {38,} o  se il contatore MainClass_C1_contatore_Co10 non è  maggiore di  commento: {54,} 140 commento: {34,} o  se il parametro MainClass_C1_parametro_P6 non è  diverso da RossoGialloGiallo commento: {37,} o  se la variabile MainClass_C1_variabile_V10 non è  minore di  commento: {55,} 2 commento: {34,} o  se il parametro MainClass_C1_parametro_P3 non è  maggiore di  commento: {54,} 1, Tutte le seguenti { 
     commento: {62,} commento: {37,}  se la variabile MainClass_C1_variabile_V10 non è  minore di  commento: {55,} 9 commento: {35,} o  se il controllo MainClass_C1_controllo_C7 è  uguale a GialloGiallo commento: {38,} e  se il contatore MainClass_C1_contatore_Co10 è  uguale a  commento: {53,} 1545321, Almeno una delle seguenti { 
      se il ripristino dello stato  non è  diverso da  commento: {56,}  state1  commento: {107,} o  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} e  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  commento: {56,} 150 o  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} e  se il controllo MainClass_C1_controllo_C7 non è  uguale a GialloGiallo, Verifica che   commento: {49,}  commento: {,}  il timer MainClass_C1_timer_T7 non sia disattivo
     commento: {104,} o  che  commento: {36,}  il timer MainClass_C1_timer_T7 sia disattivo
    
    
     } Verifica che   commento: {48,49,}  commento: {,}  il timer MainClass_C1_timer_T5 non sia disattivo
     commento: {104,} o  che  commento: {36,}  il timer MainClass_C1_timer_T5 sia scaduto
     commento: {104,} e  che  commento: {36,}  il timer MainClass_C1_timer_T7 non sia attivo
     commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C7 non sia  uguale a GialloGiallo
    
    
     } Verifica che   commento: {48,49,50,}  commento: {,}  il timer MainClass_C1_timer_T5 non sia scaduto
     commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C7 sia  uguale a GialloGiallo
     commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V10 sia  maggiore di  commento: {54,} 10
     commento: {104,} e  che  commento: {37,}  la variabile MainClass_C1_variabile_V10 non sia  diverso da  commento: {56,} 2
    
    
    }
*/
bool L_P1__Macro7(instance_id_t const my_id )
{
bool res_AndLogicOP_0 = true;
    
    //  *61,* *34,*  se lo stato  è  uguale a  *53,*  state1  *106,* *38,* o  se il contatore MainClass_C1_contatore_Co10 non è  maggiore di  *54,* 140 *34,* o  se il parametro MainClass_C1_parametro_P6 non è  diverso da RossoGialloGiallo *37,* o  se la variabile MainClass_C1_variabile_V10 non è  minore di  *55,* 2 *34,* o  se il parametro MainClass_C1_parametro_P3 non è  maggiore di  *54,* 1, Tutte le seguenti { 
    //   *62,* *37,*  se la variabile MainClass_C1_variabile_V10 non è  minore di  *55,* 9 *35,* o  se il controllo MainClass_C1_controllo_C7 è  uguale a GialloGiallo *38,* e  se il contatore MainClass_C1_contatore_Co10 è  uguale a  *53,* 1545321, Almeno una delle seguenti { 
    //    se il ripristino dello stato  non è  diverso da  *56,*  state1  *107,* o  se il controllo ConsDef  è  uguale a FALSE  *38,* e  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  *56,* 150 o  se il controllo ConsDef  è  uguale a FALSE  *35,* e  se il controllo MainClass_C1_controllo_C7 non è  uguale a GialloGiallo, Verifica che   *49,*  *,*  il timer MainClass_C1_timer_T7 non sia disattivo
    //   *104,* o  che  *36,*  il timer MainClass_C1_timer_T7 sia disattivo
    //   } Verifica che   *48,49,*  *,*  il timer MainClass_C1_timer_T5 non sia disattivo
    //   *104,* o  che  *36,*  il timer MainClass_C1_timer_T5 sia scaduto
    //   *104,* e  che  *36,*  il timer MainClass_C1_timer_T7 non sia attivo
    //   *104,* e  che  *,*  il controllo MainClass_C1_controllo_C7 non sia  uguale a GialloGiallo
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_OrLogicOP_4 = false;
    bool res_OrLogicOP_5 = false;
    res_OrLogicOP_5 = (res_OrLogicOP_5 || (L_P1_C1_GetState(my_id) == C1_St_state));
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (Counter_GetValore(L_P1__GetMainc32(my_id)) > 140u));
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_NotLogicOP_6);
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_OrLogicOP_5);
    bool res_NotLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetParamMainc8(my_id) == rossogiallo));
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! res_NotLogicOP_8);
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_NotLogicOP_7);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_OrLogicOP_4);
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetMainc26(my_id) < 2u));
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_NotLogicOP_9);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__GetParamMainc6(my_id) > 1u));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_10);
    
    if(res_OrLogicOP_2){
    bool res_AndLogicOP_11 = true;
    bool res_ImpliesLogicOp_12 = true;
    bool res_OrLogicOP_13 = false;
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1__GetMainc26(my_id) < 9u));
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_NotLogicOP_14);
    bool res_AndLogicOP_15 = true;
    res_AndLogicOP_15 = (res_AndLogicOP_15 && (L_P1__GetInMainc4(my_id) == giallogiall));
    res_AndLogicOP_15 = (res_AndLogicOP_15 && (Counter_GetValore(L_P1__GetMainc32(my_id)) == 1545321u));
    
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_AndLogicOP_15);
    
    if(res_OrLogicOP_13){
    bool res_ImpliesLogicOp_16 = true;
    bool res_OrLogicOP_17 = false;
    bool res_OrLogicOP_18 = false;
    bool res_NotLogicOP_19 = true;
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! (L_P1__GetStato1(my_id) == C1_St_state));
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! res_NotLogicOP_20);
    res_OrLogicOP_18 = (res_OrLogicOP_18 || res_NotLogicOP_19);
    bool res_AndLogicOP_21 = true;
    res_AndLogicOP_21 = (res_AndLogicOP_21 && (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_22 = true;
    bool res_NotLogicOP_23 = true;
    res_NotLogicOP_23 = (res_NotLogicOP_23 && ! (Counter_GetValore(L_P1__GetMainc34(my_id)) == 150u));
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! res_NotLogicOP_23);
    res_AndLogicOP_21 = (res_AndLogicOP_21 && res_NotLogicOP_22);
    
    res_OrLogicOP_18 = (res_OrLogicOP_18 || res_AndLogicOP_21);
    
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_OrLogicOP_18);
    bool res_AndLogicOP_24 = true;
    res_AndLogicOP_24 = (res_AndLogicOP_24 && (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_25 = true;
    res_NotLogicOP_25 = (res_NotLogicOP_25 && ! (L_P1__GetInMainc4(my_id) == giallogiall));
    res_AndLogicOP_24 = (res_AndLogicOP_24 && res_NotLogicOP_25);
    
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_AndLogicOP_24);
    
    if(res_OrLogicOP_17){
    bool res_OrLogicOP_26 = false;
    bool res_NotLogicOP_27 = true;
    res_NotLogicOP_27 = (res_NotLogicOP_27 && ! Timer_Disattivo(L_P1__GetMainc30(my_id)));
    res_OrLogicOP_26 = (res_OrLogicOP_26 || res_NotLogicOP_27);
    res_OrLogicOP_26 = (res_OrLogicOP_26 || Timer_Disattivo(L_P1__GetMainc30(my_id)));
    
    res_ImpliesLogicOp_16 = (res_ImpliesLogicOp_16 && res_OrLogicOP_26);
    }
    res_ImpliesLogicOp_12 = (res_ImpliesLogicOp_12 && res_ImpliesLogicOp_16);
    }
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_ImpliesLogicOp_12);
    bool res_OrLogicOP_28 = false;
    bool res_NotLogicOP_29 = true;
    res_NotLogicOP_29 = (res_NotLogicOP_29 && ! Timer_Disattivo(L_P1__GetMainc29(my_id)));
    res_OrLogicOP_28 = (res_OrLogicOP_28 || res_NotLogicOP_29);
    bool res_AndLogicOP_30 = true;
    bool res_AndLogicOP_31 = true;
    res_AndLogicOP_31 = (res_AndLogicOP_31 && Timer_Scaduto(L_P1__GetMainc29(my_id)));
    bool res_NotLogicOP_32 = true;
    res_NotLogicOP_32 = (res_NotLogicOP_32 && ! Timer_Attivo(L_P1__GetMainc30(my_id)));
    res_AndLogicOP_31 = (res_AndLogicOP_31 && res_NotLogicOP_32);
    
    res_AndLogicOP_30 = (res_AndLogicOP_30 && res_AndLogicOP_31);
    bool res_NotLogicOP_33 = true;
    res_NotLogicOP_33 = (res_NotLogicOP_33 && ! (L_P1__GetInMainc4(my_id) == giallogiall));
    res_AndLogicOP_30 = (res_AndLogicOP_30 && res_NotLogicOP_33);
    
    res_OrLogicOP_28 = (res_OrLogicOP_28 || res_AndLogicOP_30);
    
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_OrLogicOP_28);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_AndLogicOP_11);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *48,49,50,*  *,*  il timer MainClass_C1_timer_T5 non sia scaduto
    //   *104,* o  che  *,*  il controllo MainClass_C1_controllo_C7 sia  uguale a GialloGiallo
    //   *104,* e  che  *,*  la variabile MainClass_C1_variabile_V10 sia  maggiore di  *54,* 10
    //   *104,* e  che  *37,*  la variabile MainClass_C1_variabile_V10 non sia  diverso da  *56,* 2
    bool res_OrLogicOP_34 = false;
    bool res_NotLogicOP_35 = true;
    res_NotLogicOP_35 = (res_NotLogicOP_35 && ! Timer_Scaduto(L_P1__GetMainc29(my_id)));
    res_OrLogicOP_34 = (res_OrLogicOP_34 || res_NotLogicOP_35);
    bool res_AndLogicOP_36 = true;
    bool res_AndLogicOP_37 = true;
    res_AndLogicOP_37 = (res_AndLogicOP_37 && (L_P1__GetInMainc4(my_id) == giallogiall));
    res_AndLogicOP_37 = (res_AndLogicOP_37 && (L_P1__GetMainc26(my_id) > 10u));
    
    res_AndLogicOP_36 = (res_AndLogicOP_36 && res_AndLogicOP_37);
    bool res_NotLogicOP_38 = true;
    bool res_NotLogicOP_39 = true;
    res_NotLogicOP_39 = (res_NotLogicOP_39 && ! (L_P1__GetMainc26(my_id) == 2u));
    res_NotLogicOP_38 = (res_NotLogicOP_38 && ! res_NotLogicOP_39);
    res_AndLogicOP_36 = (res_AndLogicOP_36 && res_NotLogicOP_38);
    
    res_OrLogicOP_34 = (res_OrLogicOP_34 || res_AndLogicOP_36);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_34);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
     
    {  se la macro  MainClass_C1_macrova_M4 ( con argomento_a5   uguale a True ,argomento_a6   uguale a c120 ,argomento_a4   uguale a c270xx  e argomento_a3   uguale a RossoVerde )  non  è  diverso da  True  commento: {40,}  commento: {34,} o  se il parametro MainClass_C1_parametro_P3 è  maggiore di  commento: {54,} 10 commento: {34,} o  se il parametro MainClass_C1_parametro_P3 non è  minore di  commento: {55,} 2 commento: {35,} o  se il controllo MainClass_C1_controllo_C7 è  uguale a GialloGiallo commento: {36,} e  se il timer MainClass_C1_timer_T5 non è disattivo commento: {37,} e  se la variabile MainClass_C1_variabile_V10 è  uguale a  commento: {53,} 10, Verifica che   commento: {47,48,49,51,}   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P3 non sia  minore di  commento: {55,} 9
     commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P1 sia  maggiore di  commento: {54,} 6
     commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T7 sia attivo
     commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co1 sia  diverso da  commento: {56,} 134
    
    
    }
*/
bool L_P1__Macro8(instance_id_t const my_id )
{
bool res_AndLogicOP_0 = true;
    
    //  se la macro  MainClass_C1_macrova_M4 ( con argomento_a5   uguale a True ,argomento_a6   uguale a c120 ,argomento_a4   uguale a c270xx  e argomento_a3   uguale a RossoVerde )  non  è  diverso da  True  *40,*  *34,* o  se il parametro MainClass_C1_parametro_P3 è  maggiore di  *54,* 10 *34,* o  se il parametro MainClass_C1_parametro_P3 non è  minore di  *55,* 2 *35,* o  se il controllo MainClass_C1_controllo_C7 è  uguale a GialloGiallo *36,* e  se il timer MainClass_C1_timer_T5 non è disattivo *37,* e  se la variabile MainClass_C1_variabile_V10 è  uguale a  *53,* 10, Verifica che   *47,48,49,51,*   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* o  che  *34,*  il parametro MainClass_C1_parametro_P3 non sia  minore di  *55,* 9
    //   *104,* o  che  *34,*  il parametro MainClass_C1_parametro_P1 sia  maggiore di  *54,* 6
    //   *104,* e  che  *,*  il timer MainClass_C1_timer_T7 sia attivo
    //   *104,* o  che   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* e  che  *,*  il contatore MainClass_C1_contatore_Co1 sia  diverso da  *56,* 134
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_OrLogicOP_4 = false;
    bool res_NotLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__Macro5(my_id,rossoverde,c270xx,true,c120) == true));
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! res_NotLogicOP_6);
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_NotLogicOP_5);
    res_OrLogicOP_4 = (res_OrLogicOP_4 || (L_P1__GetParamMainc6(my_id) > 10u));
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_OrLogicOP_4);
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetParamMainc6(my_id) < 2u));
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_NotLogicOP_7);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    bool res_AndLogicOP_8 = true;
    bool res_AndLogicOP_9 = true;
    res_AndLogicOP_9 = (res_AndLogicOP_9 && (L_P1__GetInMainc4(my_id) == giallogiall));
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! Timer_Disattivo(L_P1__GetMainc29(my_id)));
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_NotLogicOP_10);
    
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_AndLogicOP_9);
    res_AndLogicOP_8 = (res_AndLogicOP_8 && (L_P1__GetMainc26(my_id) == 10u));
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_8);
    
    if(res_OrLogicOP_2){
    bool res_OrLogicOP_11 = false;
    bool res_OrLogicOP_12 = false;
    bool res_OrLogicOP_13 = false;
    res_OrLogicOP_13 = (res_OrLogicOP_13 || (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1__GetParamMainc6(my_id) < 9u));
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_NotLogicOP_14);
    
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_OrLogicOP_13);
    bool res_AndLogicOP_15 = true;
    res_AndLogicOP_15 = (res_AndLogicOP_15 && (L_P1__GetParamMainc5(my_id) > 6u));
    res_AndLogicOP_15 = (res_AndLogicOP_15 && Timer_Attivo(L_P1__GetMainc30(my_id)));
    
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_AndLogicOP_15);
    
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_OrLogicOP_12);
    bool res_AndLogicOP_16 = true;
    res_AndLogicOP_16 = (res_AndLogicOP_16 && (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! (Counter_GetValore(L_P1__GetMainc31(my_id)) == 134u));
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_NotLogicOP_17);
    
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_AndLogicOP_16);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_OrLogicOP_11);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
    
    { commento: {35,}  se il controllo MainClass_C1_controllo_C7 è  uguale a GialloGiallo, Verifica che   commento: {49,}  commento: {,}  il timer MainClass_C1_timer_T5 non sia scaduto
     commento: {104,} e  che  commento: {36,}  il timer MainClass_C1_timer_T7 non sia disattivo
    
    
    }
*/
bool L_P1__Macro9(instance_id_t const my_id , C1_Enumerat4 argom11, C1_Enumerat4 argom12, bool argom13, C1_Enumerat4 argom14, C1_Enumerat4 argom15)
{
bool res_AndLogicOP_0 = true;
    
    //  *35,*  se il controllo MainClass_C1_controllo_C7 è  uguale a GialloGiallo, Verifica che   *49,*  *,*  il timer MainClass_C1_timer_T5 non sia scaduto
    //   *104,* e  che  *36,*  il timer MainClass_C1_timer_T7 non sia disattivo
    bool res_ImpliesLogicOp_1 = true;
    if((L_P1__GetInMainc4(my_id) == giallogiall)){
    bool res_AndLogicOP_2 = true;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! Timer_Scaduto(L_P1__GetMainc29(my_id)));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_3);
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! Timer_Disattivo(L_P1__GetMainc30(my_id)));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_4);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_AndLogicOP_2);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    
    
    return res_AndLogicOP_0;
}


// Macro valorizzate

/*
    CNL corrispondente:
    
    { commento: {[} commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV2 è  diverso da RossoGialloGiallo commento: {38,} e  se il contatore MainClass_C1_contatore_Co1 è  minore di  commento: {55,} 135321 o  se la macro  MainClass_C1_macrova_M4 ( con argomento_a5   uguale a True ,argomento_a6   uguale a c120 ,argomento_a4   uguale a avanzamento  e argomento_a3   uguale a RossoVerde )  non  è  diverso da  False  commento: {40,}  , assegna alla macro il valore  False 
    
     commento: {46,} assegna alla macro il valore  True  commento: {],}
    }
*/
bool L_P1__Macro4(instance_id_t const my_id , C1_Enumerat2 argom, C1_Enumerat1 argom1, C1_Enumerat3 argom2, C1_Enumerat4 argom3, C1_Enumerat1 argom4)
{
bool res_macro_val;
    
    //  *[* *109,*  se il ripristino della variabile  MainClass_C1_restoreva_RV2 è  diverso da RossoGialloGiallo *38,* e  se il contatore MainClass_C1_contatore_Co1 è  minore di  *55,* 135321 o  se la macro  MainClass_C1_macrova_M4 ( con argomento_a5   uguale a True ,argomento_a6   uguale a c120 ,argomento_a4   uguale a avanzamento  e argomento_a3   uguale a RossoVerde )  non  è  diverso da  False
    bool res_OrLogicOP_0 = false;
    bool res_AndLogicOP_1 = true;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (L_P1__GetMainc23(my_id) == rossogiallo));
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_2);
    res_AndLogicOP_1 = (res_AndLogicOP_1 && (Counter_GetValore(L_P1__GetMainc31(my_id)) < 135321u));
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_1);
    bool res_NotLogicOP_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__Macro5(my_id,rossoverde,avanzamento,true,c120) == false));
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! res_NotLogicOP_4);
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_3);
    
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
    
    { commento: {[}  se il controllo ConsDef è uguale a FALSE  commento: {36,} e  se il timer MainClass_C1_timer_T7 è attivo , assegna alla macro il valore  True 
    
     commento: {46,} assegna alla macro il valore  True  commento: {],}
    }
*/
bool L_P1__Macro5(instance_id_t const my_id , C1_Enumerat2 argom5, C1_Enumerat3 argom6, bool argom7, C1_Enumerat4 argom8)
{
bool res_macro_val;
    
    //  *[*  se il controllo ConsDef è uguale a FALSE  *36,* e  se il timer MainClass_C1_timer_T7 è attivo
    bool res_AndLogicOP_0 = true;
    res_AndLogicOP_0 = (res_AndLogicOP_0 && (L_P1__GetInConsd(my_id) == false));
    res_AndLogicOP_0 = (res_AndLogicOP_0 && Timer_Attivo(L_P1__GetMainc30(my_id)));
    
    if(res_AndLogicOP_0){
    
    res_macro_val = true;
    }
    else{
    res_macro_val = true;
    }
    return res_macro_val;
}



