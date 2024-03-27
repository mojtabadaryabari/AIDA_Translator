// Codice del modello 'TestCase18', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
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
	    L_P1__SetOutEvent1(my_id, LDS_MANCMD_UNEXPECTED);
    } else {
        L_P1__SetOutEvent1(my_id, LDS_MANCMD_NOOP);
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
    L_P1__SetMainc18(my_id, rossogiallo1);
    L_P1__SetMainc20(my_id, rossogiallo);
    L_P1__SetMainc22(my_id, false);
    L_P1__SetMainc24(my_id, c270x);
    L_P1__SetMainc26(my_id, c270x);
    L_P1__SetMainc27(my_id, c270x);
    L_P1__SetMainc28(my_id, false);
    L_P1__SetMainc29(my_id, false);
    L_P1__SetMainc30(my_id, 0);
    L_P1__SetMainc31(my_id, 0);
    L_P1__SetMainc32(my_id, rossogiallo2);
    L_P1__SetMainc33(my_id, rossogiallo2);
    L_P1__SetMainc34(my_id, false);
    L_P1__SetMainc35(my_id, false);
    L_P1__SetMainc36(my_id, false);
    L_P1__SetMainc37(my_id, 0);
    L_P1__SetMainc38(my_id, rossogiallo1);
    L_P1__SetMainc39(my_id, 0);
    L_P1__SetMainc40(my_id, c270x);
    L_P1__SetStato1(my_id, C1_St_Stato);
    // init controlli precedenti
    L_P1__SetMainc11(my_id, true);
    L_P1__SetMainc13(my_id, false);
    L_P1__SetMainc15(my_id, c270xx);
    L_P1__SetMainc17(my_id, false);
    // init Timer e Counter
    Timer_AggmInit(L_P1__GetMainc41(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc41_ID);
    Timer_Init(L_P1__GetMainc41(my_id), 1325000);
    Timer_AggmInit(L_P1__GetMainc42(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc42_ID);
    Timer_Init(L_P1__GetMainc42(my_id), 1325000);
    Timer_AggmInit(L_P1__GetMainc43(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc43_ID);
    Timer_Init(L_P1__GetMainc43(my_id), 50000);
    Timer_AggmInit(L_P1__GetMainc44(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc44_ID);
    Timer_Init(L_P1__GetMainc44(my_id), 50000);
    Timer_AggmInit(L_P1__GetMainc45(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc45_ID);
    Timer_Init(L_P1__GetMainc45(my_id), 3413000);
    Timer_AggmInit(L_P1__GetMainc46(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc46_ID);
    Timer_Init(L_P1__GetMainc46(my_id), 3413000);
    Timer_AggmInit(L_P1__GetMainc47(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc47_ID);
    Timer_Init(L_P1__GetMainc47(my_id), 32000);
    Timer_AggmInit(L_P1__GetMainc48(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc48_ID);
    Timer_Init(L_P1__GetMainc48(my_id), 32000);
    Timer_AggmInit(L_P1__GetMainc49(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc49_ID);
    Timer_Init(L_P1__GetMainc49(my_id), 55000);
    Timer_AggmInit(L_P1__GetMainc50(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc50_ID);
    Timer_Init(L_P1__GetMainc50(my_id), 55000);
    Timer_AggmInit(L_P1__GetMainc51(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc51_ID);
    Timer_Init(L_P1__GetMainc51(my_id), 41000);
    Counter_AggmInit(L_P1__GetMainc52(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc52_ID);
    Counter_Init(L_P1__GetMainc52(my_id));
    Counter_AggmInit(L_P1__GetMainc53(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc53_ID);
    Counter_Init(L_P1__GetMainc53(my_id));
    Counter_AggmInit(L_P1__GetMainc54(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc54_ID);
    Counter_Init(L_P1__GetMainc54(my_id));
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
    L_P1__SetMainc19(my_id, L_P1__GetMainc18(my_id));
    L_P1__SetMainc21(my_id, L_P1__GetMainc20(my_id));
    L_P1__SetMainc23(my_id, L_P1__GetMainc22(my_id));
    L_P1__SetMainc25(my_id, L_P1__GetMainc24(my_id));
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
    Timer_Exec(L_P1__GetMainc41(my_id));
    Timer_Exec(L_P1__GetMainc42(my_id));
    Timer_Exec(L_P1__GetMainc43(my_id));
    Timer_Exec(L_P1__GetMainc44(my_id));
    Timer_Exec(L_P1__GetMainc45(my_id));
    Timer_Exec(L_P1__GetMainc46(my_id));
    Timer_Exec(L_P1__GetMainc47(my_id));
    Timer_Exec(L_P1__GetMainc48(my_id));
    Timer_Exec(L_P1__GetMainc49(my_id));
    Timer_Exec(L_P1__GetMainc50(my_id));
    Timer_Exec(L_P1__GetMainc51(my_id));
}

void L_P1_C1_GSetSafe(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C1(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C1(proc_id);
    L_P1__SetOutMainc(my_id, true);
}

void L_P1_C1_GUpdatePrev(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C1(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C1(proc_id);
    L_P1__SetMainc11(my_id, L_P1__GetInMainc10(my_id));
    L_P1__SetMainc13(my_id, L_P1__GetInMainc12(my_id));
    L_P1__SetMainc15(my_id, L_P1__GetInMainc14(my_id));
    L_P1__SetMainc17(my_id, L_P1__GetInMainc16(my_id));
    L_P1__SetMainc19(my_id, L_P1__GetMainc18(my_id));
    L_P1__SetMainc21(my_id, L_P1__GetMainc20(my_id));
    L_P1__SetMainc23(my_id, L_P1__GetMainc22(my_id));
    L_P1__SetMainc25(my_id, L_P1__GetMainc24(my_id));
}

// ********** Definizione macro **********

// Macro di effetto

/*
    CNL corrispondente:
    
    { commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV2 non è  diverso da  False  commento: {38,} e  se il contatore MainClass_C1_contatore_Co10 non è  minore di  commento: {55,} 14, commento: {66,} Assegna al comando MainClass_C1_comando_C1 il valore  True 
    
     ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V3 il valore c270xx
    
    
     commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è disattivo commento: {38,} o  se il contatore MainClass_C1_contatore_Co10 è  maggiore di  commento: {54,} 135 e  se il controllo ConsDef  è  uguale a FALSE , commento: {70,}Incrementa il contatore MainClass_C1_contatore_Co7
    
       
     commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} e  se la variabile MainClass_C1_variabile_V3 è  diverso da c270xx e  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} o  se il parametro MainClass_C1_parametro_P5 è  diverso da  True ,  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V2 il valore 6 commento: {67,}
    
     ,altrimenti  commento: {68,}Attiva il timer MainClass_C1_timer_T5
    
    
    
    }
*/
void L_P1__Macro(instance_id_t const my_id )
{
//  *109,*  se il ripristino della variabile  MainClass_C1_restoreva_RV2 non è  diverso da  False  *38,* e  se il contatore MainClass_C1_contatore_Co10 non è  minore di  *55,* 14, *66,* Assegna al comando MainClass_C1_comando_C1 il valore  True 
    // ,altrimenti  *67,* Assegna alla variabile MainClass_C1_variabile_V3 il valore c270xx
    bool res_AndLogicOP_0 = true;
    bool res_NotLogicOP_1 = true;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (L_P1__GetMainc29(my_id) == false));
    res_NotLogicOP_1 = (res_NotLogicOP_1 && ! res_NotLogicOP_2);
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_NotLogicOP_1);
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (Counter_GetValore(L_P1__GetMainc52(my_id)) < 14u));
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_NotLogicOP_3);
    
    if(res_AndLogicOP_0){
    
    L_P1__SetOutMainc(my_id,true);
    }else{
    
    L_P1__SetMainc38(my_id,c270xx);
    }
    //  *110,*  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è disattivo *38,* o  se il contatore MainClass_C1_contatore_Co10 è  maggiore di  *54,* 135 e  se il controllo ConsDef  è  uguale a FALSE , *70,*Incrementa il contatore MainClass_C1_contatore_Co7
    bool res_OrLogicOP_4 = false;
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! Timer_Disattivo(L_P1__GetMainc42(my_id)));
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_NotLogicOP_5);
    bool res_AndLogicOP_6 = true;
    res_AndLogicOP_6 = (res_AndLogicOP_6 && (Counter_GetValore(L_P1__GetMainc52(my_id)) > 135u));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_AndLogicOP_6);
    
    if(res_OrLogicOP_4){
    
    Counter_Incr(L_P1__GetMainc54(my_id));
    }
    //  *110,*  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  *37,* e  se la variabile MainClass_C1_variabile_V3 è  diverso da c270xx e  se il controllo ConsDef  è  uguale a FALSE  *34,* o  se il parametro MainClass_C1_parametro_P5 è  diverso da  True ,  *67,* Assegna alla variabile MainClass_C1_variabile_V2 il valore 6 *67,*
    // ,altrimenti  *68,*Attiva il timer MainClass_C1_timer_T5
    bool res_OrLogicOP_7 = false;
    bool res_AndLogicOP_8 = true;
    bool res_AndLogicOP_9 = true;
    bool res_AndLogicOP_10 = true;
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! Timer_Scaduto(L_P1__GetMainc42(my_id)));
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_NotLogicOP_11);
    res_AndLogicOP_10 = (res_AndLogicOP_10 && (L_P1__GetInConsd(my_id) == false));
    
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_AndLogicOP_10);
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (L_P1__GetMainc38(my_id) == c270xx));
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_NotLogicOP_12);
    
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_AndLogicOP_9);
    res_AndLogicOP_8 = (res_AndLogicOP_8 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_AndLogicOP_8);
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (L_P1__GetParamMainc7(my_id) == true));
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_NotLogicOP_13);
    
    if(res_OrLogicOP_7){
    
    L_P1__SetMainc37(my_id,6u);
    }else{
    
    Timer_Attiva(L_P1__GetMainc51(my_id));
    }
}

/*
    CNL corrispondente:
    
    { commento: {34,}  se il parametro MainClass_C1_parametro_P9 è  minore di  commento: {55,} 9 commento: {34,} e  se il parametro MainClass_C1_parametro_P9 è  maggiore di  commento: {54,} 6, commento: {66,} Assegna al comando MainClass_C1_comando_C1 il valore  True 
    
       
     commento: {35,}  se il controllo MainClass_C1_controllo_C9 è  diverso da avanzamento commento: {37,} e  se la variabile MainClass_C1_variabile_V2 è  uguale a  commento: {53,} 1,  Applica gli effetti
           della macro MainClass_C1_macroef_M10  commento: {73,}
    
       
     commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI2 non è disattivo commento: {37,} o  se la variabile MainClass_C1_variabile_V9 non è  diverso da avanzamento, commento: {72,}Azzera il contatore MainClass_C1_contatore_Co10
    
       
    
    }
*/
void L_P1__Macro1(instance_id_t const my_id )
{
//  *34,*  se il parametro MainClass_C1_parametro_P9 è  minore di  *55,* 9 *34,* e  se il parametro MainClass_C1_parametro_P9 è  maggiore di  *54,* 6, *66,* Assegna al comando MainClass_C1_comando_C1 il valore  True
    bool res_AndLogicOP_0 = true;
    res_AndLogicOP_0 = (res_AndLogicOP_0 && (L_P1__GetParamMainc9(my_id) < 9u));
    res_AndLogicOP_0 = (res_AndLogicOP_0 && (L_P1__GetParamMainc9(my_id) > 6u));
    
    if(res_AndLogicOP_0){
    
    L_P1__SetOutMainc(my_id,true);
    }
    //  *35,*  se il controllo MainClass_C1_controllo_C9 è  diverso da avanzamento *37,* e  se la variabile MainClass_C1_variabile_V2 è  uguale a  *53,* 1,  Applica gli effetti
    //       della macro MainClass_C1_macroef_M10
    bool res_AndLogicOP_1 = true;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (L_P1__GetInMainc4(my_id) == avanzamento));
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_2);
    res_AndLogicOP_1 = (res_AndLogicOP_1 && (L_P1__GetMainc37(my_id) == 1u));
    
    if(res_AndLogicOP_1){
    
    L_P1__Macro(my_id);
    }
    //  *73,*
    //   
    // *110,*  se il ripristino del timer  MainClass_C1_restoreTI_TI2 non è disattivo *37,* o  se la variabile MainClass_C1_variabile_V9 non è  diverso da avanzamento, *72,*Azzera il contatore MainClass_C1_contatore_Co10
    bool res_OrLogicOP_3 = false;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! Timer_Disattivo(L_P1__GetMainc44(my_id)));
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_NotLogicOP_4);
    bool res_NotLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetMainc40(my_id) == avanzamento));
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! res_NotLogicOP_6);
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_NotLogicOP_5);
    
    if(res_OrLogicOP_3){
    
    Counter_Res(L_P1__GetMainc52(my_id));
    }
}

/*
    CNL corrispondente:
    
    { commento: {34,}  se lo stato  non è  diverso da  commento: {56,}  state1  commento: {106,} commento: {36,} e  se il timer MainClass_C1_timer_T5 è disattivo commento: {37,} e  se la variabile MainClass_C1_variabile_V9 non è  diverso da avanzamento commento: {37,} o  se la variabile MainClass_C1_variabile_V8 non è  uguale a  commento: {53,} 2 commento: {34,} e  se il parametro MainClass_C1_parametro_P4 è  diverso da avanzamentox, commento: {66,} Assegna al comando MainClass_C1_comando_C1 il valore  False 
    
       
     commento: {34,}  se lo stato  non è  uguale a  commento: {53,}  state1  commento: {106,} commento: {37,} o  se la variabile MainClass_C1_variabile_V2 non è  maggiore di  commento: {54,} 2 commento: {35,} e  se il controllo MainClass_C1_controllo_C2 è  uguale a avanzamentox commento: {34,} o  se il parametro MainClass_C1_parametro_P9 è  maggiore di  commento: {54,} 8 commento: {34,} o  se il parametro MainClass_C1_parametro_P9 non è  uguale a  commento: {53,} 3, commento: {71,}Decrementa il contatore MainClass_C1_contatore_Co10
    
       
      se il controllo ConsDef è uguale a FALSE  commento: {38,} o  se il contatore MainClass_C1_contatore_Co10 non è  maggiore di  commento: {54,} 145 commento: {37,} e  se la variabile MainClass_C1_variabile_V3 è  diverso da c270xx, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V9 il valore avanzamento
    
       
    
    }
*/
void L_P1__Macro2(instance_id_t const my_id )
{
//  *34,*  se lo stato  non è  diverso da  *56,*  state1  *106,* *36,* e  se il timer MainClass_C1_timer_T5 è disattivo *37,* e  se la variabile MainClass_C1_variabile_V9 non è  diverso da avanzamento *37,* o  se la variabile MainClass_C1_variabile_V8 non è  uguale a  *53,* 2 *34,* e  se il parametro MainClass_C1_parametro_P4 è  diverso da avanzamentox, *66,* Assegna al comando MainClass_C1_comando_C1 il valore  False
    bool res_OrLogicOP_0 = false;
    bool res_AndLogicOP_1 = true;
    bool res_AndLogicOP_2 = true;
    bool res_NotLogicOP_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1_C1_GetState(my_id) == C1_St_state));
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! res_NotLogicOP_4);
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_3);
    res_AndLogicOP_2 = (res_AndLogicOP_2 && Timer_Disattivo(L_P1__GetMainc51(my_id)));
    
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_AndLogicOP_2);
    bool res_NotLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetMainc40(my_id) == avanzamento));
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! res_NotLogicOP_6);
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_5);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_1);
    bool res_AndLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetMainc39(my_id) == 2u));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_8);
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetParamMainc6(my_id) == avanzamento1));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_9);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_7);
    
    if(res_OrLogicOP_0){
    
    L_P1__SetOutMainc(my_id,false);
    }
    //  *34,*  se lo stato  non è  uguale a  *53,*  state1  *106,* *37,* o  se la variabile MainClass_C1_variabile_V2 non è  maggiore di  *54,* 2 *35,* e  se il controllo MainClass_C1_controllo_C2 è  uguale a avanzamentox *34,* o  se il parametro MainClass_C1_parametro_P9 è  maggiore di  *54,* 8 *34,* o  se il parametro MainClass_C1_parametro_P9 non è  uguale a  *53,* 3, *71,*Decrementa il contatore MainClass_C1_contatore_Co10
    bool res_OrLogicOP_10 = false;
    bool res_OrLogicOP_11 = false;
    bool res_OrLogicOP_12 = false;
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (L_P1_C1_GetState(my_id) == C1_St_state));
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_NotLogicOP_13);
    bool res_AndLogicOP_14 = true;
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (L_P1__GetMainc37(my_id) > 2u));
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_NotLogicOP_15);
    res_AndLogicOP_14 = (res_AndLogicOP_14 && (L_P1__GetInMainc2(my_id) == avanzamento1));
    
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_AndLogicOP_14);
    
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_OrLogicOP_12);
    res_OrLogicOP_11 = (res_OrLogicOP_11 || (L_P1__GetParamMainc9(my_id) > 8u));
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_OrLogicOP_11);
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (L_P1__GetParamMainc9(my_id) == 3u));
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_NotLogicOP_16);
    
    if(res_OrLogicOP_10){
    
    Counter_Decr(L_P1__GetMainc52(my_id));
    }
    //  se il controllo ConsDef è uguale a FALSE  *38,* o  se il contatore MainClass_C1_contatore_Co10 non è  maggiore di  *54,* 145 *37,* e  se la variabile MainClass_C1_variabile_V3 è  diverso da c270xx, *67,* Assegna alla variabile MainClass_C1_variabile_V9 il valore avanzamento
    bool res_OrLogicOP_17 = false;
    res_OrLogicOP_17 = (res_OrLogicOP_17 || (L_P1__GetInConsd(my_id) == false));
    bool res_AndLogicOP_18 = true;
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (Counter_GetValore(L_P1__GetMainc52(my_id)) > 145u));
    res_AndLogicOP_18 = (res_AndLogicOP_18 && res_NotLogicOP_19);
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! (L_P1__GetMainc38(my_id) == c270xx));
    res_AndLogicOP_18 = (res_AndLogicOP_18 && res_NotLogicOP_20);
    
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_AndLogicOP_18);
    
    if(res_OrLogicOP_17){
    
    L_P1__SetMainc40(my_id,avanzamento);
    }
}

/*
    CNL corrispondente:
     
    { commento: {37,}  se la variabile MainClass_C1_variabile_V2 è  maggiore di  commento: {54,} 9 commento: {34,} o  se il parametro MainClass_C1_parametro_P9 è  maggiore di  commento: {54,} 1 commento: {34,} o  se il parametro MainClass_C1_parametro_P5 non è  uguale a  False  commento: {34,} o  se il parametro MainClass_C1_parametro_P9 non è  maggiore di  commento: {54,} 6 commento: {36,} o  se il timer MainClass_C1_timer_T5 è disattivo, commento: {69,}Disattiva il timer MainClass_C1_timer_T5
    
       
      se il ripristino dello stato  non è  diverso da  commento: {56,}  state1  commento: {107,} commento: {35,} o  se il controllo MainClass_C1_controllo_C2 è  diverso da avanzamentox e  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} o  se la variabile MainClass_C1_variabile_V2 non è  diverso da  commento: {56,} 3 commento: {36,} o  se il timer MainClass_C1_timer_T5 non è attivo, commento: {66,} Assegna al comando MainClass_C1_comando_C1 il valore  True 
    
       
     commento: {37,}  se la variabile MainClass_C1_variabile_V9 è  diverso da avanzamento commento: {38,} e  se il contatore MainClass_C1_contatore_Co10 è  uguale a  commento: {53,} 1504132 o  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} o  se il timer MainClass_C1_timer_T5 è attivo, commento: {66,} Assegna al comando MainClass_C1_comando_C1 il valore  True 
    
       
      se il ripristino dello stato  non è  uguale a  commento: {53,}  state1  commento: {107,} commento: {35,} e  se il controllo MainClass_C1_controllo_C2 non è  uguale a avanzamentox commento: {35,} o  se il controllo MainClass_C1_controllo_C9 è  uguale a avanzamento e  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} e  se la variabile MainClass_C1_variabile_V2 non è  maggiore di  commento: {54,} 6,  Applica gli effetti
           della macro MainClass_C1_macroef_M10  commento: {73,}
    
     ,altrimenti  commento: {68,}Attiva il timer MainClass_C1_timer_T5
    
    
     commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è scaduto, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V2 il valore 7
    
       
    
    }
*/
void L_P1__Macro3(instance_id_t const my_id )
{
//  *37,*  se la variabile MainClass_C1_variabile_V2 è  maggiore di  *54,* 9 *34,* o  se il parametro MainClass_C1_parametro_P9 è  maggiore di  *54,* 1 *34,* o  se il parametro MainClass_C1_parametro_P5 non è  uguale a  False  *34,* o  se il parametro MainClass_C1_parametro_P9 non è  maggiore di  *54,* 6 *36,* o  se il timer MainClass_C1_timer_T5 è disattivo, *69,*Disattiva il timer MainClass_C1_timer_T5
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    res_OrLogicOP_3 = (res_OrLogicOP_3 || (L_P1__GetMainc37(my_id) > 9u));
    res_OrLogicOP_3 = (res_OrLogicOP_3 || (L_P1__GetParamMainc9(my_id) > 1u));
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetParamMainc7(my_id) == false));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_4);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_OrLogicOP_2);
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetParamMainc9(my_id) > 6u));
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_NotLogicOP_5);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    res_OrLogicOP_0 = (res_OrLogicOP_0 || Timer_Disattivo(L_P1__GetMainc51(my_id)));
    
    if(res_OrLogicOP_0){
    
    Timer_Disattiva(L_P1__GetMainc51(my_id));
    }
    //  se il ripristino dello stato  non è  diverso da  *56,*  state1  *107,* *35,* o  se il controllo MainClass_C1_controllo_C2 è  diverso da avanzamentox e  se il controllo ConsDef  è  uguale a FALSE  *37,* o  se la variabile MainClass_C1_variabile_V2 non è  diverso da  *56,* 3 *36,* o  se il timer MainClass_C1_timer_T5 non è attivo, *66,* Assegna al comando MainClass_C1_comando_C1 il valore  True
    bool res_OrLogicOP_6 = false;
    bool res_OrLogicOP_7 = false;
    bool res_OrLogicOP_8 = false;
    bool res_NotLogicOP_9 = true;
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__GetStato1(my_id) == C1_St_state));
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! res_NotLogicOP_10);
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_NotLogicOP_9);
    bool res_AndLogicOP_11 = true;
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (L_P1__GetInMainc2(my_id) == avanzamento1));
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_NotLogicOP_12);
    res_AndLogicOP_11 = (res_AndLogicOP_11 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_AndLogicOP_11);
    
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_OrLogicOP_8);
    bool res_NotLogicOP_13 = true;
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1__GetMainc37(my_id) == 3u));
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! res_NotLogicOP_14);
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_NotLogicOP_13);
    
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_OrLogicOP_7);
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! Timer_Attivo(L_P1__GetMainc51(my_id)));
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_NotLogicOP_15);
    
    if(res_OrLogicOP_6){
    
    L_P1__SetOutMainc(my_id,true);
    }
    //  *37,*  se la variabile MainClass_C1_variabile_V9 è  diverso da avanzamento *38,* e  se il contatore MainClass_C1_contatore_Co10 è  uguale a  *53,* 1504132 o  se il controllo ConsDef  è  uguale a FALSE  *36,* o  se il timer MainClass_C1_timer_T5 è attivo, *66,* Assegna al comando MainClass_C1_comando_C1 il valore  True
    bool res_OrLogicOP_16 = false;
    bool res_OrLogicOP_17 = false;
    bool res_AndLogicOP_18 = true;
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (L_P1__GetMainc40(my_id) == avanzamento));
    res_AndLogicOP_18 = (res_AndLogicOP_18 && res_NotLogicOP_19);
    res_AndLogicOP_18 = (res_AndLogicOP_18 && (Counter_GetValore(L_P1__GetMainc52(my_id)) == 1504132u));
    
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_AndLogicOP_18);
    res_OrLogicOP_17 = (res_OrLogicOP_17 || (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_16 = (res_OrLogicOP_16 || res_OrLogicOP_17);
    res_OrLogicOP_16 = (res_OrLogicOP_16 || Timer_Attivo(L_P1__GetMainc51(my_id)));
    
    if(res_OrLogicOP_16){
    
    L_P1__SetOutMainc(my_id,true);
    }
    //  se il ripristino dello stato  non è  uguale a  *53,*  state1  *107,* *35,* e  se il controllo MainClass_C1_controllo_C2 non è  uguale a avanzamentox *35,* o  se il controllo MainClass_C1_controllo_C9 è  uguale a avanzamento e  se il controllo ConsDef  è  uguale a FALSE  *37,* e  se la variabile MainClass_C1_variabile_V2 non è  maggiore di  *54,* 6,  Applica gli effetti
    //       della macro MainClass_C1_macroef_M10  *73,*
    // ,altrimenti  *68,*Attiva il timer MainClass_C1_timer_T5
    bool res_OrLogicOP_20 = false;
    bool res_AndLogicOP_21 = true;
    bool res_NotLogicOP_22 = true;
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! (L_P1__GetStato1(my_id) == C1_St_state));
    res_AndLogicOP_21 = (res_AndLogicOP_21 && res_NotLogicOP_22);
    bool res_NotLogicOP_23 = true;
    res_NotLogicOP_23 = (res_NotLogicOP_23 && ! (L_P1__GetInMainc2(my_id) == avanzamento1));
    res_AndLogicOP_21 = (res_AndLogicOP_21 && res_NotLogicOP_23);
    
    res_OrLogicOP_20 = (res_OrLogicOP_20 || res_AndLogicOP_21);
    bool res_AndLogicOP_24 = true;
    bool res_AndLogicOP_25 = true;
    res_AndLogicOP_25 = (res_AndLogicOP_25 && (L_P1__GetInMainc4(my_id) == avanzamento));
    res_AndLogicOP_25 = (res_AndLogicOP_25 && (L_P1__GetInConsd(my_id) == false));
    
    res_AndLogicOP_24 = (res_AndLogicOP_24 && res_AndLogicOP_25);
    bool res_NotLogicOP_26 = true;
    res_NotLogicOP_26 = (res_NotLogicOP_26 && ! (L_P1__GetMainc37(my_id) > 6u));
    res_AndLogicOP_24 = (res_AndLogicOP_24 && res_NotLogicOP_26);
    
    res_OrLogicOP_20 = (res_OrLogicOP_20 || res_AndLogicOP_24);
    
    if(res_OrLogicOP_20){
    
    L_P1__Macro(my_id);
    }else{
    
    Timer_Attiva(L_P1__GetMainc51(my_id));
    }
    //  *110,*  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è scaduto, *67,* Assegna alla variabile MainClass_C1_variabile_V2 il valore 7
    bool res_NotLogicOP_27 = true;
    res_NotLogicOP_27 = (res_NotLogicOP_27 && ! Timer_Scaduto(L_P1__GetMainc42(my_id)));
    if(res_NotLogicOP_27){
    
    L_P1__SetMainc37(my_id,7u);
    }
}

/*
    CNL corrispondente:
    
    { commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV3 è  uguale a  commento: {53,} 7 commento: {34,} e  se il parametro MainClass_C1_parametro_P5 è  diverso da  False , commento: {70,}Incrementa il contatore MainClass_C1_contatore_Co10
    
       
    
    }
*/
void L_P1__Macro4(instance_id_t const my_id , bool argom, C1_Enumerat4 argom1, C1_Enumerat2 argom2, C1_Enumerat3 argom3, bool argom4, C1_Enumerat3 argom5, C1_Enumerat1 argom6)
{
//  *109,*  se il ripristino della variabile  MainClass_C1_restoreva_RV3 è  uguale a  *53,* 7 *34,* e  se il parametro MainClass_C1_parametro_P5 è  diverso da  False , *70,*Incrementa il contatore MainClass_C1_contatore_Co10
    bool res_AndLogicOP_0 = true;
    res_AndLogicOP_0 = (res_AndLogicOP_0 && (L_P1__GetMainc31(my_id) == 7u));
    bool res_NotLogicOP_1 = true;
    res_NotLogicOP_1 = (res_NotLogicOP_1 && ! (L_P1__GetParamMainc7(my_id) == false));
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_NotLogicOP_1);
    
    if(res_AndLogicOP_0){
    
    Counter_Incr(L_P1__GetMainc52(my_id));
    }
}


// Macro di verifica

/*
    CNL corrispondente:
     
    { commento: {62,}  se la macro  MainClass_C1_macrova_M5 ( con argomento_a8   uguale a RossoGialloxVerdex ,argomento_a1   uguale a c270x ,argomento_a5   uguale a RossoVerde  e argomento_a2   uguale a c270x )  non  è  diverso da c270xx commento: {40,}  commento: {36,} e  se il timer MainClass_C1_timer_T5 non è scaduto, Almeno una delle seguenti { 
     commento: {61,} commento: {35,}  se il controllo MainClass_C1_controllo_C2 non è  diverso da avanzamentox commento: {34,} e  se il parametro MainClass_C1_parametro_P4 è  diverso da avanzamentox, Tutte le seguenti { 
     commento: {63,} commento: {34,}  se lo stato  non è  uguale a  commento: {53,}  state1  commento: {106,} commento: {35,} o  se il controllo MainClass_C1_controllo_C10 non è  diverso da  False , Solo una delle seguenti { 
     commento: {63,}  se il ripristino dello stato  non è  diverso da  commento: {56,}  state1  commento: {107,} commento: {36,} e  se il timer MainClass_C1_timer_T5 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} e  se il timer MainClass_C1_timer_T5 non è attivo, Solo una delle seguenti { 
     commento: {61,} commento: {37,}  se la variabile MainClass_C1_variabile_V2 è  diverso da  commento: {56,} 4, Tutte le seguenti { 
     commento: {61,} commento: {34,}  se lo stato  non è  diverso da  commento: {56,}  state1  commento: {106,} commento: {37,} o  se la variabile MainClass_C1_variabile_V8 è  minore di  commento: {55,} 8, Tutte le seguenti { 
      se la macro  MainClass_C1_macrova_M6 ( con argomento_a8   uguale a RossoGialloaVerdea  e argomento_a1   uguale a RossoVerde )   è  uguale a  True  commento: {40,} , Verifica che   commento: {47,48,51,}  commento: {34,}  il parametro MainClass_C1_parametro_P9 non sia  minore di  commento: {55,} 10
     commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co10 non sia  minore di  commento: {55,} 13325
     commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
    
    
     } Verifica che   commento: {47,48,49,}  commento: {,}  il controllo MainClass_C1_controllo_C10 non sia  uguale a  True 
     commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T5 sia scaduto
     commento: {104,} e  che  commento: {35,}  il controllo MainClass_C1_controllo_C9 non sia  uguale a avanzamento
     commento: {104,} o  che  commento: {36,}  il timer MainClass_C1_timer_T5 sia scaduto
     commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P4 non sia  uguale a avanzamentox
     commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
    
    
     } Verifica che   commento: {47,51,}  commento: {,}  il contatore MainClass_C1_contatore_Co10 sia  minore di  commento: {55,} 110
     commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P4 sia  diverso da avanzamentox
    
    
     } Verifica che   commento: {47,48,}  commento: {34,}  il parametro MainClass_C1_parametro_P4 sia  uguale a avanzamentox
     commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P9 non sia  uguale a  commento: {53,} 4
     commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C2 non sia  diverso da avanzamentox
     commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
    
    
     } Verifica che   commento: {48,50,}  commento: {,}  la variabile MainClass_C1_variabile_V2 sia  maggiore di  commento: {54,} 3
     commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
    
    
     } Verifica che   commento: {47,48,50,51,}  commento: {34,}  il parametro MainClass_C1_parametro_P9 sia  minore di  commento: {55,} 3
     commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co10 non sia  maggiore di  commento: {54,} 153
     commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C9 sia  uguale a avanzamento
     commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V2 sia  uguale a  commento: {53,} 3
     commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} e  che  commento: {35,}  il controllo MainClass_C1_controllo_C2 sia  uguale a avanzamentox
    
    
     } Verifica che   commento: {48,49,50,51,}  commento: {,}  la variabile MainClass_C1_variabile_V3 sia  uguale a c270xx
     commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T5 sia attivo
     commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C9 non sia  diverso da avanzamento
     commento: {104,} o  che  commento: {,}  il contatore MainClass_C1_contatore_Co5 non sia  maggiore di  commento: {54,} 152
     commento: {104,} e  che  commento: {38,}  il contatore MainClass_C1_contatore_Co10 sia  minore di  commento: {55,} 12
    
    
    }
*/
bool L_P1__Macro10(instance_id_t const my_id )
{
bool res_AndLogicOP_0 = true;
    
    //  *62,*  se la macro  MainClass_C1_macrova_M5 ( con argomento_a8   uguale a RossoGialloxVerdex ,argomento_a1   uguale a c270x ,argomento_a5   uguale a RossoVerde  e argomento_a2   uguale a c270x )  non  è  diverso da c270xx *40,*  *36,* e  se il timer MainClass_C1_timer_T5 non è scaduto, Almeno una delle seguenti { 
    //   *61,* *35,*  se il controllo MainClass_C1_controllo_C2 non è  diverso da avanzamentox *34,* e  se il parametro MainClass_C1_parametro_P4 è  diverso da avanzamentox, Tutte le seguenti { 
    //   *63,* *34,*  se lo stato  non è  uguale a  *53,*  state1  *106,* *35,* o  se il controllo MainClass_C1_controllo_C10 non è  diverso da  False , Solo una delle seguenti { 
    //   *63,*  se il ripristino dello stato  non è  diverso da  *56,*  state1  *107,* *36,* e  se il timer MainClass_C1_timer_T5 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  *36,* e  se il timer MainClass_C1_timer_T5 non è attivo, Solo una delle seguenti { 
    //   *61,* *37,*  se la variabile MainClass_C1_variabile_V2 è  diverso da  *56,* 4, Tutte le seguenti { 
    //   *61,* *34,*  se lo stato  non è  diverso da  *56,*  state1  *106,* *37,* o  se la variabile MainClass_C1_variabile_V8 è  minore di  *55,* 8, Tutte le seguenti { 
    //    se la macro  MainClass_C1_macrova_M6 ( con argomento_a8   uguale a RossoGialloaVerdea  e argomento_a1   uguale a RossoVerde )   è  uguale a  True  *40,* , Verifica che   *47,48,51,*  *34,*  il parametro MainClass_C1_parametro_P9 non sia  minore di  *55,* 10
    //   *104,* e  che  *,*  il contatore MainClass_C1_contatore_Co10 non sia  minore di  *55,* 13325
    //   *104,* o  che   il controllo ConsDef  sia  uguale a FALSE 
    //   } Verifica che   *47,48,49,*  *,*  il controllo MainClass_C1_controllo_C10 non sia  uguale a  True 
    //   *104,* o  che  *,*  il timer MainClass_C1_timer_T5 sia scaduto
    //   *104,* e  che  *35,*  il controllo MainClass_C1_controllo_C9 non sia  uguale a avanzamento
    //   *104,* o  che  *36,*  il timer MainClass_C1_timer_T5 sia scaduto
    //   *104,* e  che  *34,*  il parametro MainClass_C1_parametro_P4 non sia  uguale a avanzamentox
    //   *104,* e  che   il controllo ConsDef  sia  uguale a FALSE 
    //   } Verifica che   *47,51,*  *,*  il contatore MainClass_C1_contatore_Co10 sia  minore di  *55,* 110
    //   *104,* o  che  *34,*  il parametro MainClass_C1_parametro_P4 sia  diverso da avanzamentox
    //   } Verifica che   *47,48,*  *34,*  il parametro MainClass_C1_parametro_P4 sia  uguale a avanzamentox
    //   *104,* e  che  *34,*  il parametro MainClass_C1_parametro_P9 non sia  uguale a  *53,* 4
    //   *104,* o  che  *,*  il controllo MainClass_C1_controllo_C2 non sia  diverso da avanzamentox
    //   *104,* e  che   il controllo ConsDef  sia  uguale a FALSE 
    //   } Verifica che   *48,50,*  *,*  la variabile MainClass_C1_variabile_V2 sia  maggiore di  *54,* 3
    //   *104,* e  che   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* e  che   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* e  che   il controllo ConsDef  sia  uguale a FALSE 
    //   } Verifica che   *47,48,50,51,*  *34,*  il parametro MainClass_C1_parametro_P9 sia  minore di  *55,* 3
    //   *104,* e  che  *,*  il contatore MainClass_C1_contatore_Co10 non sia  maggiore di  *54,* 153
    //   *104,* e  che  *,*  il controllo MainClass_C1_controllo_C9 sia  uguale a avanzamento
    //   *104,* e  che  *,*  la variabile MainClass_C1_variabile_V2 sia  uguale a  *53,* 3
    //   *104,* o  che   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* e  che  *35,*  il controllo MainClass_C1_controllo_C2 sia  uguale a avanzamentox
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_AndLogicOP_2 = true;
    bool res_NotLogicOP_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__Macro7(my_id,c270x,c270x,rossoverde,rossogiallo1) == c270xx));
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! res_NotLogicOP_4);
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_3);
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! Timer_Scaduto(L_P1__GetMainc51(my_id)));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_5);
    
    if(res_AndLogicOP_2){
    bool res_OrLogicOP_6 = false;
    bool res_ImpliesLogicOp_7 = true;
    bool res_AndLogicOP_8 = true;
    bool res_NotLogicOP_9 = true;
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__GetInMainc2(my_id) == avanzamento1));
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! res_NotLogicOP_10);
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_9);
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (L_P1__GetParamMainc6(my_id) == avanzamento1));
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_11);
    
    if(res_AndLogicOP_8){
    bool res_AndLogicOP_12 = true;
    bool res_ImpliesLogicOp_13 = true;
    bool res_OrLogicOP_14 = false;
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (L_P1_C1_GetState(my_id) == C1_St_state));
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_NotLogicOP_15);
    bool res_NotLogicOP_16 = true;
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! (L_P1__GetInMainc1(my_id) == false));
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! res_NotLogicOP_17);
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_NotLogicOP_16);
    
    if(res_OrLogicOP_14){
    bool res_XorLogicOP_18 = true;
    int xorIndex_res_XorLogicOP_18 = 0;
    bool res_ImpliesLogicOp_19 = true;
    bool res_AndLogicOP_20 = true;
    bool res_AndLogicOP_21 = true;
    bool res_AndLogicOP_22 = true;
    bool res_NotLogicOP_23 = true;
    bool res_NotLogicOP_24 = true;
    res_NotLogicOP_24 = (res_NotLogicOP_24 && ! (L_P1__GetStato1(my_id) == C1_St_state));
    res_NotLogicOP_23 = (res_NotLogicOP_23 && ! res_NotLogicOP_24);
    res_AndLogicOP_22 = (res_AndLogicOP_22 && res_NotLogicOP_23);
    bool res_NotLogicOP_25 = true;
    res_NotLogicOP_25 = (res_NotLogicOP_25 && ! Timer_Scaduto(L_P1__GetMainc51(my_id)));
    res_AndLogicOP_22 = (res_AndLogicOP_22 && res_NotLogicOP_25);
    
    res_AndLogicOP_21 = (res_AndLogicOP_21 && res_AndLogicOP_22);
    res_AndLogicOP_21 = (res_AndLogicOP_21 && (L_P1__GetInConsd(my_id) == false));
    
    res_AndLogicOP_20 = (res_AndLogicOP_20 && res_AndLogicOP_21);
    bool res_NotLogicOP_26 = true;
    res_NotLogicOP_26 = (res_NotLogicOP_26 && ! Timer_Attivo(L_P1__GetMainc51(my_id)));
    res_AndLogicOP_20 = (res_AndLogicOP_20 && res_NotLogicOP_26);
    
    if(res_AndLogicOP_20){
    bool res_XorLogicOP_27 = true;
    int xorIndex_res_XorLogicOP_27 = 0;
    bool res_ImpliesLogicOp_28 = true;
    bool res_NotLogicOP_29 = true;
    res_NotLogicOP_29 = (res_NotLogicOP_29 && ! (L_P1__GetMainc37(my_id) == 4u));
    if(res_NotLogicOP_29){
    bool res_AndLogicOP_30 = true;
    bool res_ImpliesLogicOp_31 = true;
    bool res_OrLogicOP_32 = false;
    bool res_NotLogicOP_33 = true;
    bool res_NotLogicOP_34 = true;
    res_NotLogicOP_34 = (res_NotLogicOP_34 && ! (L_P1_C1_GetState(my_id) == C1_St_state));
    res_NotLogicOP_33 = (res_NotLogicOP_33 && ! res_NotLogicOP_34);
    res_OrLogicOP_32 = (res_OrLogicOP_32 || res_NotLogicOP_33);
    res_OrLogicOP_32 = (res_OrLogicOP_32 || (L_P1__GetMainc39(my_id) < 8u));
    
    if(res_OrLogicOP_32){
    bool res_ImpliesLogicOp_35 = true;
    if((L_P1__Macro8(my_id,rossoverde,rossogiallo2) == true)){
    bool res_OrLogicOP_36 = false;
    bool res_AndLogicOP_37 = true;
    bool res_NotLogicOP_38 = true;
    res_NotLogicOP_38 = (res_NotLogicOP_38 && ! (L_P1__GetParamMainc9(my_id) < 10u));
    res_AndLogicOP_37 = (res_AndLogicOP_37 && res_NotLogicOP_38);
    bool res_NotLogicOP_39 = true;
    res_NotLogicOP_39 = (res_NotLogicOP_39 && ! (Counter_GetValore(L_P1__GetMainc52(my_id)) < 13325u));
    res_AndLogicOP_37 = (res_AndLogicOP_37 && res_NotLogicOP_39);
    
    res_OrLogicOP_36 = (res_OrLogicOP_36 || res_AndLogicOP_37);
    res_OrLogicOP_36 = (res_OrLogicOP_36 || (L_P1__GetInConsd(my_id) == false));
    
    res_ImpliesLogicOp_35 = (res_ImpliesLogicOp_35 && res_OrLogicOP_36);
    }
    res_ImpliesLogicOp_31 = (res_ImpliesLogicOp_31 && res_ImpliesLogicOp_35);
    }
    res_AndLogicOP_30 = (res_AndLogicOP_30 && res_ImpliesLogicOp_31);
    bool res_OrLogicOP_40 = false;
    bool res_OrLogicOP_41 = false;
    bool res_NotLogicOP_42 = true;
    res_NotLogicOP_42 = (res_NotLogicOP_42 && ! (L_P1__GetInMainc1(my_id) == true));
    res_OrLogicOP_41 = (res_OrLogicOP_41 || res_NotLogicOP_42);
    bool res_AndLogicOP_43 = true;
    res_AndLogicOP_43 = (res_AndLogicOP_43 && Timer_Scaduto(L_P1__GetMainc51(my_id)));
    bool res_NotLogicOP_44 = true;
    res_NotLogicOP_44 = (res_NotLogicOP_44 && ! (L_P1__GetInMainc4(my_id) == avanzamento));
    res_AndLogicOP_43 = (res_AndLogicOP_43 && res_NotLogicOP_44);
    
    res_OrLogicOP_41 = (res_OrLogicOP_41 || res_AndLogicOP_43);
    
    res_OrLogicOP_40 = (res_OrLogicOP_40 || res_OrLogicOP_41);
    bool res_AndLogicOP_45 = true;
    bool res_AndLogicOP_46 = true;
    res_AndLogicOP_46 = (res_AndLogicOP_46 && Timer_Scaduto(L_P1__GetMainc51(my_id)));
    bool res_NotLogicOP_47 = true;
    res_NotLogicOP_47 = (res_NotLogicOP_47 && ! (L_P1__GetParamMainc6(my_id) == avanzamento1));
    res_AndLogicOP_46 = (res_AndLogicOP_46 && res_NotLogicOP_47);
    
    res_AndLogicOP_45 = (res_AndLogicOP_45 && res_AndLogicOP_46);
    res_AndLogicOP_45 = (res_AndLogicOP_45 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_40 = (res_OrLogicOP_40 || res_AndLogicOP_45);
    
    res_AndLogicOP_30 = (res_AndLogicOP_30 && res_OrLogicOP_40);
    
    res_ImpliesLogicOp_28 = (res_ImpliesLogicOp_28 && res_AndLogicOP_30);
    }
    if(res_ImpliesLogicOp_28){
    xorIndex_res_XorLogicOP_27 = (xorIndex_res_XorLogicOP_27 + 1);
    }
    bool res_OrLogicOP_48 = false;
    res_OrLogicOP_48 = (res_OrLogicOP_48 || (Counter_GetValore(L_P1__GetMainc52(my_id)) < 110u));
    bool res_NotLogicOP_49 = true;
    res_NotLogicOP_49 = (res_NotLogicOP_49 && ! (L_P1__GetParamMainc6(my_id) == avanzamento1));
    res_OrLogicOP_48 = (res_OrLogicOP_48 || res_NotLogicOP_49);
    
    if(res_OrLogicOP_48){
    xorIndex_res_XorLogicOP_27 = (xorIndex_res_XorLogicOP_27 + 1);
    }
    
    res_XorLogicOP_27 = (res_XorLogicOP_27 && (xorIndex_res_XorLogicOP_27 == 1));
    res_ImpliesLogicOp_19 = (res_ImpliesLogicOp_19 && res_XorLogicOP_27);
    }
    if(res_ImpliesLogicOp_19){
    xorIndex_res_XorLogicOP_18 = (xorIndex_res_XorLogicOP_18 + 1);
    }
    bool res_OrLogicOP_50 = false;
    bool res_AndLogicOP_51 = true;
    res_AndLogicOP_51 = (res_AndLogicOP_51 && (L_P1__GetParamMainc6(my_id) == avanzamento1));
    bool res_NotLogicOP_52 = true;
    res_NotLogicOP_52 = (res_NotLogicOP_52 && ! (L_P1__GetParamMainc9(my_id) == 4u));
    res_AndLogicOP_51 = (res_AndLogicOP_51 && res_NotLogicOP_52);
    
    res_OrLogicOP_50 = (res_OrLogicOP_50 || res_AndLogicOP_51);
    bool res_AndLogicOP_53 = true;
    bool res_NotLogicOP_54 = true;
    bool res_NotLogicOP_55 = true;
    res_NotLogicOP_55 = (res_NotLogicOP_55 && ! (L_P1__GetInMainc2(my_id) == avanzamento1));
    res_NotLogicOP_54 = (res_NotLogicOP_54 && ! res_NotLogicOP_55);
    res_AndLogicOP_53 = (res_AndLogicOP_53 && res_NotLogicOP_54);
    res_AndLogicOP_53 = (res_AndLogicOP_53 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_50 = (res_OrLogicOP_50 || res_AndLogicOP_53);
    
    if(res_OrLogicOP_50){
    xorIndex_res_XorLogicOP_18 = (xorIndex_res_XorLogicOP_18 + 1);
    }
    
    res_XorLogicOP_18 = (res_XorLogicOP_18 && (xorIndex_res_XorLogicOP_18 == 1));
    res_ImpliesLogicOp_13 = (res_ImpliesLogicOp_13 && res_XorLogicOP_18);
    }
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_ImpliesLogicOp_13);
    bool res_AndLogicOP_56 = true;
    bool res_AndLogicOP_57 = true;
    bool res_AndLogicOP_58 = true;
    res_AndLogicOP_58 = (res_AndLogicOP_58 && (L_P1__GetMainc37(my_id) > 3u));
    res_AndLogicOP_58 = (res_AndLogicOP_58 && (L_P1__GetInConsd(my_id) == false));
    
    res_AndLogicOP_57 = (res_AndLogicOP_57 && res_AndLogicOP_58);
    res_AndLogicOP_57 = (res_AndLogicOP_57 && (L_P1__GetInConsd(my_id) == false));
    
    res_AndLogicOP_56 = (res_AndLogicOP_56 && res_AndLogicOP_57);
    res_AndLogicOP_56 = (res_AndLogicOP_56 && (L_P1__GetInConsd(my_id) == false));
    
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_AndLogicOP_56);
    
    res_ImpliesLogicOp_7 = (res_ImpliesLogicOp_7 && res_AndLogicOP_12);
    }
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_ImpliesLogicOp_7);
    bool res_OrLogicOP_59 = false;
    bool res_AndLogicOP_60 = true;
    bool res_AndLogicOP_61 = true;
    bool res_AndLogicOP_62 = true;
    res_AndLogicOP_62 = (res_AndLogicOP_62 && (L_P1__GetParamMainc9(my_id) < 3u));
    bool res_NotLogicOP_63 = true;
    res_NotLogicOP_63 = (res_NotLogicOP_63 && ! (Counter_GetValore(L_P1__GetMainc52(my_id)) > 153u));
    res_AndLogicOP_62 = (res_AndLogicOP_62 && res_NotLogicOP_63);
    
    res_AndLogicOP_61 = (res_AndLogicOP_61 && res_AndLogicOP_62);
    res_AndLogicOP_61 = (res_AndLogicOP_61 && (L_P1__GetInMainc4(my_id) == avanzamento));
    
    res_AndLogicOP_60 = (res_AndLogicOP_60 && res_AndLogicOP_61);
    res_AndLogicOP_60 = (res_AndLogicOP_60 && (L_P1__GetMainc37(my_id) == 3u));
    
    res_OrLogicOP_59 = (res_OrLogicOP_59 || res_AndLogicOP_60);
    bool res_AndLogicOP_64 = true;
    res_AndLogicOP_64 = (res_AndLogicOP_64 && (L_P1__GetInConsd(my_id) == false));
    res_AndLogicOP_64 = (res_AndLogicOP_64 && (L_P1__GetInMainc2(my_id) == avanzamento1));
    
    res_OrLogicOP_59 = (res_OrLogicOP_59 || res_AndLogicOP_64);
    
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_OrLogicOP_59);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_OrLogicOP_6);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *48,49,50,51,*  *,*  la variabile MainClass_C1_variabile_V3 sia  uguale a c270xx
    //   *104,* o  che  *,*  il timer MainClass_C1_timer_T5 sia attivo
    //   *104,* e  che   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* e  che  *,*  il controllo MainClass_C1_controllo_C9 non sia  diverso da avanzamento
    //   *104,* o  che  *,*  il contatore MainClass_C1_contatore_Co5 non sia  maggiore di  *54,* 152
    //   *104,* e  che  *38,*  il contatore MainClass_C1_contatore_Co10 sia  minore di  *55,* 12
    bool res_OrLogicOP_65 = false;
    bool res_OrLogicOP_66 = false;
    res_OrLogicOP_66 = (res_OrLogicOP_66 || (L_P1__GetMainc38(my_id) == c270xx));
    bool res_AndLogicOP_67 = true;
    bool res_AndLogicOP_68 = true;
    res_AndLogicOP_68 = (res_AndLogicOP_68 && Timer_Attivo(L_P1__GetMainc51(my_id)));
    res_AndLogicOP_68 = (res_AndLogicOP_68 && (L_P1__GetInConsd(my_id) == false));
    
    res_AndLogicOP_67 = (res_AndLogicOP_67 && res_AndLogicOP_68);
    bool res_NotLogicOP_69 = true;
    bool res_NotLogicOP_70 = true;
    res_NotLogicOP_70 = (res_NotLogicOP_70 && ! (L_P1__GetInMainc4(my_id) == avanzamento));
    res_NotLogicOP_69 = (res_NotLogicOP_69 && ! res_NotLogicOP_70);
    res_AndLogicOP_67 = (res_AndLogicOP_67 && res_NotLogicOP_69);
    
    res_OrLogicOP_66 = (res_OrLogicOP_66 || res_AndLogicOP_67);
    
    res_OrLogicOP_65 = (res_OrLogicOP_65 || res_OrLogicOP_66);
    bool res_AndLogicOP_71 = true;
    bool res_NotLogicOP_72 = true;
    res_NotLogicOP_72 = (res_NotLogicOP_72 && ! (Counter_GetValore(L_P1__GetMainc53(my_id)) > 152u));
    res_AndLogicOP_71 = (res_AndLogicOP_71 && res_NotLogicOP_72);
    res_AndLogicOP_71 = (res_AndLogicOP_71 && (Counter_GetValore(L_P1__GetMainc52(my_id)) < 12u));
    
    res_OrLogicOP_65 = (res_OrLogicOP_65 || res_AndLogicOP_71);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_65);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
    
    { commento: {62,} commento: {36,}  se il timer MainClass_C1_timer_T5 non è scaduto commento: {37,} e  se la variabile MainClass_C1_variabile_V2 è  diverso da  commento: {56,} 7 commento: {38,} o  se il contatore MainClass_C1_contatore_Co10 è  uguale a  commento: {53,} 1204, Almeno una delle seguenti { 
     commento: {62,} commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  uguale a avanzamento commento: {35,} o  se il controllo MainClass_C1_controllo_C2 non è  uguale a avanzamentox commento: {37,} e  se la variabile MainClass_C1_variabile_V2 non è  diverso da  commento: {56,} 8, Almeno una delle seguenti { 
     commento: {63,}  se l'argomento argomento_ave7 è  uguale a RossoVerde commento: {39,}  commento: {34,} o  se il parametro MainClass_C1_parametro_P9 è  uguale a  commento: {53,} 7, Solo una delle seguenti { 
     commento: {63,}  se il controllo ConsDef è uguale a FALSE  commento: {38,} e  se il contatore MainClass_C1_contatore_Co7 è  diverso da  commento: {56,} 1213 commento: {37,} o  se la variabile MainClass_C1_variabile_V8 è  diverso da  commento: {56,} 7 e  se l'argomento argomento_ave7 è  uguale a RossoVerde commento: {39,}  commento: {35,} e  se il controllo MainClass_C1_controllo_C9 non è  uguale a avanzamento, Solo una delle seguenti { 
     commento: {61,} commento: {36,}  se il timer MainClass_C1_timer_T5 non è scaduto, Tutte le seguenti { 
     commento: {62,} commento: {37,}  se la variabile MainClass_C1_variabile_V3 è  uguale a c270xx, Almeno una delle seguenti { 
     commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI5 non è disattivo commento: {37,} e  se la variabile MainClass_C1_variabile_V2 è  maggiore di  commento: {54,} 5 commento: {35,} o  se il controllo MainClass_C1_controllo_C2 non è  diverso da avanzamentox commento: {38,} o  se il contatore MainClass_C1_contatore_Co10 è  maggiore di  commento: {54,} 122 commento: {34,} o  se il parametro MainClass_C1_parametro_P9 non è  diverso da  commento: {56,} 5, Verifica che   commento: {49,51,}  commento: {,}  il timer MainClass_C1_timer_T5 sia disattivo
     commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co5 sia  uguale a  commento: {53,} 15
    
    
     } Verifica che   commento: {47,49,50,52,}  commento: {,}  il timer MainClass_C1_timer_T5 non sia disattivo
     commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P5 non sia  uguale a  False 
     commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V3 non sia  diverso da c270xx
     commento: {104,} e  che   l'argomento argomento_ave7 non  sia  uguale a RossoVerde commento: {,} 
     commento: {104,} o  che   l'argomento argomento_ave6 sia  uguale a c270xx commento: {39,} 
    
    
     } Verifica che   commento: {47,49,51,52,}   l'argomento argomento_ave7 non  sia  uguale a RossoVerde commento: {,} 
     commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T5 non sia scaduto
     commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P1 non sia  diverso da  False 
     commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co7 sia  diverso da  commento: {56,} 11
     commento: {104,} e  che  commento: {38,}  il contatore MainClass_C1_contatore_Co10 non sia  uguale a  commento: {53,} 1
    
    
     } Verifica che   commento: {48,51,}  commento: {,}  il contatore MainClass_C1_contatore_Co10 sia  uguale a  commento: {53,} 12
     commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C2 non sia  diverso da avanzamentox
     commento: {104,} e  che  commento: {35,}  il controllo MainClass_C1_controllo_C2 non sia  diverso da avanzamentox
    
    
     } Verifica che   commento: {50,52,}   l'argomento argomento_ave7 sia  diverso da RossoVerde commento: {,} 
     commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V3 non sia  uguale a c270xx
     commento: {104,} e  che   l'argomento argomento_ave6 sia  diverso da c270xx commento: {39,} 
     commento: {104,} e  che  commento: {37,}  la variabile MainClass_C1_variabile_V3 sia  diverso da c270xx
    
    
     } Verifica che   commento: {47,49,50,52,}  commento: {34,}  il parametro MainClass_C1_parametro_P9 sia  diverso da  commento: {56,} 8
     commento: {104,} o  che   l'argomento argomento_ave7 non  sia  diverso da RossoVerde commento: {,} 
     commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V9 sia  uguale a avanzamento
     commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P9 sia  minore di  commento: {55,} 1
     commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T5 non sia disattivo
     commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P8 non sia  uguale a  True 
    
    
     } Verifica che   commento: {47,48,49,50,}  commento: {,}  il controllo MainClass_C1_controllo_C9 sia  uguale a avanzamento
     commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P4 non sia  diverso da avanzamentox
     commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V3 non sia  diverso da c270xx
     commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T5 non sia attivo
     commento: {104,} e  che  commento: {35,}  il controllo MainClass_C1_controllo_C7 sia  uguale a  True 
    
    
    }
*/
bool L_P1__Macro11(instance_id_t const my_id , C1_Enumerat3 argom18, C1_Enumerat2 argom19, C1_Enumerat3 argom20)
{
bool res_AndLogicOP_0 = true;
    
    //  *62,* *36,*  se il timer MainClass_C1_timer_T5 non è scaduto *37,* e  se la variabile MainClass_C1_variabile_V2 è  diverso da  *56,* 7 *38,* o  se il contatore MainClass_C1_contatore_Co10 è  uguale a  *53,* 1204, Almeno una delle seguenti { 
    //   *62,* *109,*  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  uguale a avanzamento *35,* o  se il controllo MainClass_C1_controllo_C2 non è  uguale a avanzamentox *37,* e  se la variabile MainClass_C1_variabile_V2 non è  diverso da  *56,* 8, Almeno una delle seguenti { 
    //   *63,*  se l'argomento argomento_ave7 è  uguale a RossoVerde *39,*  *34,* o  se il parametro MainClass_C1_parametro_P9 è  uguale a  *53,* 7, Solo una delle seguenti { 
    //   *63,*  se il controllo ConsDef è uguale a FALSE  *38,* e  se il contatore MainClass_C1_contatore_Co7 è  diverso da  *56,* 1213 *37,* o  se la variabile MainClass_C1_variabile_V8 è  diverso da  *56,* 7 e  se l'argomento argomento_ave7 è  uguale a RossoVerde *39,*  *35,* e  se il controllo MainClass_C1_controllo_C9 non è  uguale a avanzamento, Solo una delle seguenti { 
    //   *61,* *36,*  se il timer MainClass_C1_timer_T5 non è scaduto, Tutte le seguenti { 
    //   *62,* *37,*  se la variabile MainClass_C1_variabile_V3 è  uguale a c270xx, Almeno una delle seguenti { 
    //   *110,*  se il ripristino del timer  MainClass_C1_restoreTI_TI5 non è disattivo *37,* e  se la variabile MainClass_C1_variabile_V2 è  maggiore di  *54,* 5 *35,* o  se il controllo MainClass_C1_controllo_C2 non è  diverso da avanzamentox *38,* o  se il contatore MainClass_C1_contatore_Co10 è  maggiore di  *54,* 122 *34,* o  se il parametro MainClass_C1_parametro_P9 non è  diverso da  *56,* 5, Verifica che   *49,51,*  *,*  il timer MainClass_C1_timer_T5 sia disattivo
    //   *104,* e  che  *,*  il contatore MainClass_C1_contatore_Co5 sia  uguale a  *53,* 15
    //   } Verifica che   *47,49,50,52,*  *,*  il timer MainClass_C1_timer_T5 non sia disattivo
    //   *104,* e  che  *34,*  il parametro MainClass_C1_parametro_P5 non sia  uguale a  False 
    //   *104,* e  che  *,*  la variabile MainClass_C1_variabile_V3 non sia  diverso da c270xx
    //   *104,* e  che   l'argomento argomento_ave7 non  sia  uguale a RossoVerde *,* 
    //   *104,* o  che   l'argomento argomento_ave6 sia  uguale a c270xx *39,* 
    //   } Verifica che   *47,49,51,52,*   l'argomento argomento_ave7 non  sia  uguale a RossoVerde *,* 
    //   *104,* o  che  *,*  il timer MainClass_C1_timer_T5 non sia scaduto
    //   *104,* o  che  *34,*  il parametro MainClass_C1_parametro_P1 non sia  diverso da  False 
    //   *104,* e  che  *,*  il contatore MainClass_C1_contatore_Co7 sia  diverso da  *56,* 11
    //   *104,* e  che  *38,*  il contatore MainClass_C1_contatore_Co10 non sia  uguale a  *53,* 1
    //   } Verifica che   *48,51,*  *,*  il contatore MainClass_C1_contatore_Co10 sia  uguale a  *53,* 12
    //   *104,* o  che  *,*  il controllo MainClass_C1_controllo_C2 non sia  diverso da avanzamentox
    //   *104,* e  che  *35,*  il controllo MainClass_C1_controllo_C2 non sia  diverso da avanzamentox
    //   } Verifica che   *50,52,*   l'argomento argomento_ave7 sia  diverso da RossoVerde *,* 
    //   *104,* o  che  *,*  la variabile MainClass_C1_variabile_V3 non sia  uguale a c270xx
    //   *104,* e  che   l'argomento argomento_ave6 sia  diverso da c270xx *39,* 
    //   *104,* e  che  *37,*  la variabile MainClass_C1_variabile_V3 sia  diverso da c270xx
    //   } Verifica che   *47,49,50,52,*  *34,*  il parametro MainClass_C1_parametro_P9 sia  diverso da  *56,* 8
    //   *104,* o  che   l'argomento argomento_ave7 non  sia  diverso da RossoVerde *,* 
    //   *104,* e  che  *,*  la variabile MainClass_C1_variabile_V9 sia  uguale a avanzamento
    //   *104,* o  che  *34,*  il parametro MainClass_C1_parametro_P9 sia  minore di  *55,* 1
    //   *104,* o  che  *,*  il timer MainClass_C1_timer_T5 non sia disattivo
    //   *104,* e  che  *34,*  il parametro MainClass_C1_parametro_P8 non sia  uguale a  True 
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_AndLogicOP_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! Timer_Scaduto(L_P1__GetMainc51(my_id)));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_4);
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetMainc37(my_id) == 7u));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_5);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_3);
    res_OrLogicOP_2 = (res_OrLogicOP_2 || (Counter_GetValore(L_P1__GetMainc52(my_id)) == 1204u));
    
    if(res_OrLogicOP_2){
    bool res_OrLogicOP_6 = false;
    bool res_ImpliesLogicOp_7 = true;
    bool res_OrLogicOP_8 = false;
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetMainc27(my_id) == avanzamento));
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_NotLogicOP_9);
    bool res_AndLogicOP_10 = true;
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (L_P1__GetInMainc2(my_id) == avanzamento1));
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_NotLogicOP_11);
    bool res_NotLogicOP_12 = true;
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (L_P1__GetMainc37(my_id) == 8u));
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! res_NotLogicOP_13);
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_NotLogicOP_12);
    
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_AndLogicOP_10);
    
    if(res_OrLogicOP_8){
    bool res_OrLogicOP_14 = false;
    bool res_ImpliesLogicOp_15 = true;
    bool res_OrLogicOP_16 = false;
    res_OrLogicOP_16 = (res_OrLogicOP_16 || (argom19 == rossoverde));
    res_OrLogicOP_16 = (res_OrLogicOP_16 || (L_P1__GetParamMainc9(my_id) == 7u));
    
    if(res_OrLogicOP_16){
    bool res_XorLogicOP_17 = true;
    int xorIndex_res_XorLogicOP_17 = 0;
    bool res_ImpliesLogicOp_18 = true;
    bool res_OrLogicOP_19 = false;
    bool res_AndLogicOP_20 = true;
    res_AndLogicOP_20 = (res_AndLogicOP_20 && (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_21 = true;
    res_NotLogicOP_21 = (res_NotLogicOP_21 && ! (Counter_GetValore(L_P1__GetMainc54(my_id)) == 1213u));
    res_AndLogicOP_20 = (res_AndLogicOP_20 && res_NotLogicOP_21);
    
    res_OrLogicOP_19 = (res_OrLogicOP_19 || res_AndLogicOP_20);
    bool res_AndLogicOP_22 = true;
    bool res_AndLogicOP_23 = true;
    bool res_NotLogicOP_24 = true;
    res_NotLogicOP_24 = (res_NotLogicOP_24 && ! (L_P1__GetMainc39(my_id) == 7u));
    res_AndLogicOP_23 = (res_AndLogicOP_23 && res_NotLogicOP_24);
    res_AndLogicOP_23 = (res_AndLogicOP_23 && (argom19 == rossoverde));
    
    res_AndLogicOP_22 = (res_AndLogicOP_22 && res_AndLogicOP_23);
    bool res_NotLogicOP_25 = true;
    res_NotLogicOP_25 = (res_NotLogicOP_25 && ! (L_P1__GetInMainc4(my_id) == avanzamento));
    res_AndLogicOP_22 = (res_AndLogicOP_22 && res_NotLogicOP_25);
    
    res_OrLogicOP_19 = (res_OrLogicOP_19 || res_AndLogicOP_22);
    
    if(res_OrLogicOP_19){
    bool res_XorLogicOP_26 = true;
    int xorIndex_res_XorLogicOP_26 = 0;
    bool res_ImpliesLogicOp_27 = true;
    bool res_NotLogicOP_28 = true;
    res_NotLogicOP_28 = (res_NotLogicOP_28 && ! Timer_Scaduto(L_P1__GetMainc51(my_id)));
    if(res_NotLogicOP_28){
    bool res_AndLogicOP_29 = true;
    bool res_ImpliesLogicOp_30 = true;
    if((L_P1__GetMainc38(my_id) == c270xx)){
    bool res_ImpliesLogicOp_31 = true;
    bool res_OrLogicOP_32 = false;
    bool res_OrLogicOP_33 = false;
    bool res_OrLogicOP_34 = false;
    bool res_AndLogicOP_35 = true;
    bool res_NotLogicOP_36 = true;
    res_NotLogicOP_36 = (res_NotLogicOP_36 && ! Timer_Disattivo(L_P1__GetMainc50(my_id)));
    res_AndLogicOP_35 = (res_AndLogicOP_35 && res_NotLogicOP_36);
    res_AndLogicOP_35 = (res_AndLogicOP_35 && (L_P1__GetMainc37(my_id) > 5u));
    
    res_OrLogicOP_34 = (res_OrLogicOP_34 || res_AndLogicOP_35);
    bool res_NotLogicOP_37 = true;
    bool res_NotLogicOP_38 = true;
    res_NotLogicOP_38 = (res_NotLogicOP_38 && ! (L_P1__GetInMainc2(my_id) == avanzamento1));
    res_NotLogicOP_37 = (res_NotLogicOP_37 && ! res_NotLogicOP_38);
    res_OrLogicOP_34 = (res_OrLogicOP_34 || res_NotLogicOP_37);
    
    res_OrLogicOP_33 = (res_OrLogicOP_33 || res_OrLogicOP_34);
    res_OrLogicOP_33 = (res_OrLogicOP_33 || (Counter_GetValore(L_P1__GetMainc52(my_id)) > 122u));
    
    res_OrLogicOP_32 = (res_OrLogicOP_32 || res_OrLogicOP_33);
    bool res_NotLogicOP_39 = true;
    bool res_NotLogicOP_40 = true;
    res_NotLogicOP_40 = (res_NotLogicOP_40 && ! (L_P1__GetParamMainc9(my_id) == 5u));
    res_NotLogicOP_39 = (res_NotLogicOP_39 && ! res_NotLogicOP_40);
    res_OrLogicOP_32 = (res_OrLogicOP_32 || res_NotLogicOP_39);
    
    if(res_OrLogicOP_32){
    bool res_AndLogicOP_41 = true;
    res_AndLogicOP_41 = (res_AndLogicOP_41 && Timer_Disattivo(L_P1__GetMainc51(my_id)));
    res_AndLogicOP_41 = (res_AndLogicOP_41 && (Counter_GetValore(L_P1__GetMainc53(my_id)) == 15u));
    
    res_ImpliesLogicOp_31 = (res_ImpliesLogicOp_31 && res_AndLogicOP_41);
    }
    res_ImpliesLogicOp_30 = (res_ImpliesLogicOp_30 && res_ImpliesLogicOp_31);
    }
    res_AndLogicOP_29 = (res_AndLogicOP_29 && res_ImpliesLogicOp_30);
    bool res_OrLogicOP_42 = false;
    bool res_AndLogicOP_43 = true;
    bool res_AndLogicOP_44 = true;
    bool res_AndLogicOP_45 = true;
    bool res_NotLogicOP_46 = true;
    res_NotLogicOP_46 = (res_NotLogicOP_46 && ! Timer_Disattivo(L_P1__GetMainc51(my_id)));
    res_AndLogicOP_45 = (res_AndLogicOP_45 && res_NotLogicOP_46);
    bool res_NotLogicOP_47 = true;
    res_NotLogicOP_47 = (res_NotLogicOP_47 && ! (L_P1__GetParamMainc7(my_id) == false));
    res_AndLogicOP_45 = (res_AndLogicOP_45 && res_NotLogicOP_47);
    
    res_AndLogicOP_44 = (res_AndLogicOP_44 && res_AndLogicOP_45);
    bool res_NotLogicOP_48 = true;
    bool res_NotLogicOP_49 = true;
    res_NotLogicOP_49 = (res_NotLogicOP_49 && ! (L_P1__GetMainc38(my_id) == c270xx));
    res_NotLogicOP_48 = (res_NotLogicOP_48 && ! res_NotLogicOP_49);
    res_AndLogicOP_44 = (res_AndLogicOP_44 && res_NotLogicOP_48);
    
    res_AndLogicOP_43 = (res_AndLogicOP_43 && res_AndLogicOP_44);
    bool res_NotLogicOP_50 = true;
    res_NotLogicOP_50 = (res_NotLogicOP_50 && ! (argom19 == rossoverde));
    res_AndLogicOP_43 = (res_AndLogicOP_43 && res_NotLogicOP_50);
    
    res_OrLogicOP_42 = (res_OrLogicOP_42 || res_AndLogicOP_43);
    res_OrLogicOP_42 = (res_OrLogicOP_42 || (argom18 == c270xx));
    
    res_AndLogicOP_29 = (res_AndLogicOP_29 && res_OrLogicOP_42);
    
    res_ImpliesLogicOp_27 = (res_ImpliesLogicOp_27 && res_AndLogicOP_29);
    }
    if(res_ImpliesLogicOp_27){
    xorIndex_res_XorLogicOP_26 = (xorIndex_res_XorLogicOP_26 + 1);
    }
    bool res_OrLogicOP_51 = false;
    bool res_OrLogicOP_52 = false;
    bool res_NotLogicOP_53 = true;
    res_NotLogicOP_53 = (res_NotLogicOP_53 && ! (argom19 == rossoverde));
    res_OrLogicOP_52 = (res_OrLogicOP_52 || res_NotLogicOP_53);
    bool res_NotLogicOP_54 = true;
    res_NotLogicOP_54 = (res_NotLogicOP_54 && ! Timer_Scaduto(L_P1__GetMainc51(my_id)));
    res_OrLogicOP_52 = (res_OrLogicOP_52 || res_NotLogicOP_54);
    
    res_OrLogicOP_51 = (res_OrLogicOP_51 || res_OrLogicOP_52);
    bool res_AndLogicOP_55 = true;
    bool res_AndLogicOP_56 = true;
    bool res_NotLogicOP_57 = true;
    bool res_NotLogicOP_58 = true;
    res_NotLogicOP_58 = (res_NotLogicOP_58 && ! (L_P1__GetParamMainc5(my_id) == false));
    res_NotLogicOP_57 = (res_NotLogicOP_57 && ! res_NotLogicOP_58);
    res_AndLogicOP_56 = (res_AndLogicOP_56 && res_NotLogicOP_57);
    bool res_NotLogicOP_59 = true;
    res_NotLogicOP_59 = (res_NotLogicOP_59 && ! (Counter_GetValore(L_P1__GetMainc54(my_id)) == 11u));
    res_AndLogicOP_56 = (res_AndLogicOP_56 && res_NotLogicOP_59);
    
    res_AndLogicOP_55 = (res_AndLogicOP_55 && res_AndLogicOP_56);
    bool res_NotLogicOP_60 = true;
    res_NotLogicOP_60 = (res_NotLogicOP_60 && ! (Counter_GetValore(L_P1__GetMainc52(my_id)) == 1u));
    res_AndLogicOP_55 = (res_AndLogicOP_55 && res_NotLogicOP_60);
    
    res_OrLogicOP_51 = (res_OrLogicOP_51 || res_AndLogicOP_55);
    
    if(res_OrLogicOP_51){
    xorIndex_res_XorLogicOP_26 = (xorIndex_res_XorLogicOP_26 + 1);
    }
    
    res_XorLogicOP_26 = (res_XorLogicOP_26 && (xorIndex_res_XorLogicOP_26 == 1));
    res_ImpliesLogicOp_18 = (res_ImpliesLogicOp_18 && res_XorLogicOP_26);
    }
    if(res_ImpliesLogicOp_18){
    xorIndex_res_XorLogicOP_17 = (xorIndex_res_XorLogicOP_17 + 1);
    }
    bool res_OrLogicOP_61 = false;
    res_OrLogicOP_61 = (res_OrLogicOP_61 || (Counter_GetValore(L_P1__GetMainc52(my_id)) == 12u));
    bool res_AndLogicOP_62 = true;
    bool res_NotLogicOP_63 = true;
    bool res_NotLogicOP_64 = true;
    res_NotLogicOP_64 = (res_NotLogicOP_64 && ! (L_P1__GetInMainc2(my_id) == avanzamento1));
    res_NotLogicOP_63 = (res_NotLogicOP_63 && ! res_NotLogicOP_64);
    res_AndLogicOP_62 = (res_AndLogicOP_62 && res_NotLogicOP_63);
    bool res_NotLogicOP_65 = true;
    bool res_NotLogicOP_66 = true;
    res_NotLogicOP_66 = (res_NotLogicOP_66 && ! (L_P1__GetInMainc2(my_id) == avanzamento1));
    res_NotLogicOP_65 = (res_NotLogicOP_65 && ! res_NotLogicOP_66);
    res_AndLogicOP_62 = (res_AndLogicOP_62 && res_NotLogicOP_65);
    
    res_OrLogicOP_61 = (res_OrLogicOP_61 || res_AndLogicOP_62);
    
    if(res_OrLogicOP_61){
    xorIndex_res_XorLogicOP_17 = (xorIndex_res_XorLogicOP_17 + 1);
    }
    
    res_XorLogicOP_17 = (res_XorLogicOP_17 && (xorIndex_res_XorLogicOP_17 == 1));
    res_ImpliesLogicOp_15 = (res_ImpliesLogicOp_15 && res_XorLogicOP_17);
    }
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_ImpliesLogicOp_15);
    bool res_OrLogicOP_67 = false;
    bool res_NotLogicOP_68 = true;
    res_NotLogicOP_68 = (res_NotLogicOP_68 && ! (argom19 == rossoverde));
    res_OrLogicOP_67 = (res_OrLogicOP_67 || res_NotLogicOP_68);
    bool res_AndLogicOP_69 = true;
    bool res_AndLogicOP_70 = true;
    bool res_NotLogicOP_71 = true;
    res_NotLogicOP_71 = (res_NotLogicOP_71 && ! (L_P1__GetMainc38(my_id) == c270xx));
    res_AndLogicOP_70 = (res_AndLogicOP_70 && res_NotLogicOP_71);
    bool res_NotLogicOP_72 = true;
    res_NotLogicOP_72 = (res_NotLogicOP_72 && ! (argom18 == c270xx));
    res_AndLogicOP_70 = (res_AndLogicOP_70 && res_NotLogicOP_72);
    
    res_AndLogicOP_69 = (res_AndLogicOP_69 && res_AndLogicOP_70);
    bool res_NotLogicOP_73 = true;
    res_NotLogicOP_73 = (res_NotLogicOP_73 && ! (L_P1__GetMainc38(my_id) == c270xx));
    res_AndLogicOP_69 = (res_AndLogicOP_69 && res_NotLogicOP_73);
    
    res_OrLogicOP_67 = (res_OrLogicOP_67 || res_AndLogicOP_69);
    
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_OrLogicOP_67);
    
    res_ImpliesLogicOp_7 = (res_ImpliesLogicOp_7 && res_OrLogicOP_14);
    }
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_ImpliesLogicOp_7);
    bool res_OrLogicOP_74 = false;
    bool res_OrLogicOP_75 = false;
    bool res_OrLogicOP_76 = false;
    bool res_NotLogicOP_77 = true;
    res_NotLogicOP_77 = (res_NotLogicOP_77 && ! (L_P1__GetParamMainc9(my_id) == 8u));
    res_OrLogicOP_76 = (res_OrLogicOP_76 || res_NotLogicOP_77);
    bool res_AndLogicOP_78 = true;
    bool res_NotLogicOP_79 = true;
    bool res_NotLogicOP_80 = true;
    res_NotLogicOP_80 = (res_NotLogicOP_80 && ! (argom19 == rossoverde));
    res_NotLogicOP_79 = (res_NotLogicOP_79 && ! res_NotLogicOP_80);
    res_AndLogicOP_78 = (res_AndLogicOP_78 && res_NotLogicOP_79);
    res_AndLogicOP_78 = (res_AndLogicOP_78 && (L_P1__GetMainc40(my_id) == avanzamento));
    
    res_OrLogicOP_76 = (res_OrLogicOP_76 || res_AndLogicOP_78);
    
    res_OrLogicOP_75 = (res_OrLogicOP_75 || res_OrLogicOP_76);
    res_OrLogicOP_75 = (res_OrLogicOP_75 || (L_P1__GetParamMainc9(my_id) < 1u));
    
    res_OrLogicOP_74 = (res_OrLogicOP_74 || res_OrLogicOP_75);
    bool res_AndLogicOP_81 = true;
    bool res_NotLogicOP_82 = true;
    res_NotLogicOP_82 = (res_NotLogicOP_82 && ! Timer_Disattivo(L_P1__GetMainc51(my_id)));
    res_AndLogicOP_81 = (res_AndLogicOP_81 && res_NotLogicOP_82);
    bool res_NotLogicOP_83 = true;
    res_NotLogicOP_83 = (res_NotLogicOP_83 && ! (L_P1__GetParamMainc8(my_id) == true));
    res_AndLogicOP_81 = (res_AndLogicOP_81 && res_NotLogicOP_83);
    
    res_OrLogicOP_74 = (res_OrLogicOP_74 || res_AndLogicOP_81);
    
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_OrLogicOP_74);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_OrLogicOP_6);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *47,48,49,50,*  *,*  il controllo MainClass_C1_controllo_C9 sia  uguale a avanzamento
    //   *104,* e  che  *34,*  il parametro MainClass_C1_parametro_P4 non sia  diverso da avanzamentox
    //   *104,* o  che  *,*  la variabile MainClass_C1_variabile_V3 non sia  diverso da c270xx
    //   *104,* o  che  *,*  il timer MainClass_C1_timer_T5 non sia attivo
    //   *104,* e  che  *35,*  il controllo MainClass_C1_controllo_C7 sia  uguale a  True
    bool res_OrLogicOP_84 = false;
    bool res_OrLogicOP_85 = false;
    bool res_AndLogicOP_86 = true;
    res_AndLogicOP_86 = (res_AndLogicOP_86 && (L_P1__GetInMainc4(my_id) == avanzamento));
    bool res_NotLogicOP_87 = true;
    bool res_NotLogicOP_88 = true;
    res_NotLogicOP_88 = (res_NotLogicOP_88 && ! (L_P1__GetParamMainc6(my_id) == avanzamento1));
    res_NotLogicOP_87 = (res_NotLogicOP_87 && ! res_NotLogicOP_88);
    res_AndLogicOP_86 = (res_AndLogicOP_86 && res_NotLogicOP_87);
    
    res_OrLogicOP_85 = (res_OrLogicOP_85 || res_AndLogicOP_86);
    bool res_NotLogicOP_89 = true;
    bool res_NotLogicOP_90 = true;
    res_NotLogicOP_90 = (res_NotLogicOP_90 && ! (L_P1__GetMainc38(my_id) == c270xx));
    res_NotLogicOP_89 = (res_NotLogicOP_89 && ! res_NotLogicOP_90);
    res_OrLogicOP_85 = (res_OrLogicOP_85 || res_NotLogicOP_89);
    
    res_OrLogicOP_84 = (res_OrLogicOP_84 || res_OrLogicOP_85);
    bool res_AndLogicOP_91 = true;
    bool res_NotLogicOP_92 = true;
    res_NotLogicOP_92 = (res_NotLogicOP_92 && ! Timer_Attivo(L_P1__GetMainc51(my_id)));
    res_AndLogicOP_91 = (res_AndLogicOP_91 && res_NotLogicOP_92);
    res_AndLogicOP_91 = (res_AndLogicOP_91 && (L_P1__GetInMainc3(my_id) == true));
    
    res_OrLogicOP_84 = (res_OrLogicOP_84 || res_AndLogicOP_91);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_84);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
    
    {  se la macro  MainClass_C1_macrova_M5 ( con argomento_a8   uguale a c270xx ,argomento_a1   uguale a avanzamento ,argomento_a5   uguale a RossoVerde  e argomento_a2   uguale a avanzamento )  non  è  uguale a c270xx commento: {40,}  commento: {37,} e  se la variabile MainClass_C1_variabile_V8 è  uguale a  commento: {53,} 9 e  se l'argomento argomento_ave1 è  diverso da avanzamentox commento: {39,}  commento: {37,} e  se la variabile MainClass_C1_variabile_V2 non è  diverso da  commento: {56,} 4, Verifica che   commento: {47,51,52,}  commento: {34,}  il parametro MainClass_C1_parametro_P4 sia  uguale a avanzamentox
     commento: {104,} o  che  commento: {,}  il contatore MainClass_C1_contatore_Co10 non sia  diverso da  commento: {56,} 15132
     commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P9 non sia  minore di  commento: {55,} 10
     commento: {104,} e  che   l'argomento argomento_ave5 non  sia  diverso da avanzamento commento: {,} 
    
    
    }
*/
bool L_P1__Macro12(instance_id_t const my_id , C1_Enumerat4 argom21, C1_Enumerat1 argom22)
{
bool res_AndLogicOP_0 = true;
    
    //  se la macro  MainClass_C1_macrova_M5 ( con argomento_a8   uguale a c270xx ,argomento_a1   uguale a avanzamento ,argomento_a5   uguale a RossoVerde  e argomento_a2   uguale a avanzamento )  non  è  uguale a c270xx *40,*  *37,* e  se la variabile MainClass_C1_variabile_V8 è  uguale a  *53,* 9 e  se l'argomento argomento_ave1 è  diverso da avanzamentox *39,*  *37,* e  se la variabile MainClass_C1_variabile_V2 non è  diverso da  *56,* 4, Verifica che   *47,51,52,*  *34,*  il parametro MainClass_C1_parametro_P4 sia  uguale a avanzamentox
    //   *104,* o  che  *,*  il contatore MainClass_C1_contatore_Co10 non sia  diverso da  *56,* 15132
    //   *104,* o  che  *34,*  il parametro MainClass_C1_parametro_P9 non sia  minore di  *55,* 10
    //   *104,* e  che   l'argomento argomento_ave5 non  sia  diverso da avanzamento
    bool res_ImpliesLogicOp_1 = true;
    bool res_AndLogicOP_2 = true;
    bool res_AndLogicOP_3 = true;
    bool res_AndLogicOP_4 = true;
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__Macro7(my_id,avanzamento,avanzamento,rossoverde,c270xx) == c270xx));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_5);
    res_AndLogicOP_4 = (res_AndLogicOP_4 && (L_P1__GetMainc39(my_id) == 9u));
    
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_AndLogicOP_4);
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (argom21 == avanzamento1));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_6);
    
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_AndLogicOP_3);
    bool res_NotLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetMainc37(my_id) == 4u));
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! res_NotLogicOP_8);
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_7);
    
    if(res_AndLogicOP_2){
    bool res_OrLogicOP_9 = false;
    bool res_OrLogicOP_10 = false;
    res_OrLogicOP_10 = (res_OrLogicOP_10 || (L_P1__GetParamMainc6(my_id) == avanzamento1));
    bool res_NotLogicOP_11 = true;
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (Counter_GetValore(L_P1__GetMainc52(my_id)) == 15132u));
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! res_NotLogicOP_12);
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_NotLogicOP_11);
    
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_OrLogicOP_10);
    bool res_AndLogicOP_13 = true;
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1__GetParamMainc9(my_id) < 10u));
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_NotLogicOP_14);
    bool res_NotLogicOP_15 = true;
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (argom22 == avanzamento));
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! res_NotLogicOP_16);
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_NotLogicOP_15);
    
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_AndLogicOP_13);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_OrLogicOP_9);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    
    
    return res_AndLogicOP_0;
}


// Macro valorizzate

/*
    CNL corrispondente:
     
    { commento: {[}
     commento: {46,} assegna alla macro il valore avanzamentox commento: {],}
    }
*/
C1_Enumerat4 L_P1__Macro5(instance_id_t const my_id )
{
return avanzamento1;
}

/*
    CNL corrispondente:
    
    { commento: {[} commento: {36,}  se il timer MainClass_C1_timer_T5 è scaduto e  se l'argomento argomento_a10 non  è  uguale a avanzamento commento: {39,}  o  se il controllo ConsDef è uguale a FALSE  commento: {38,} o  se il contatore MainClass_C1_contatore_Co5 è  minore di  commento: {55,} 15 commento: {35,} e  se il controllo MainClass_C1_controllo_C7 è  diverso da  True  commento: {109,} o  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  diverso da avanzamento , assegna alla macro il valore  True 
    
     commento: {46,} assegna alla macro il valore  True  commento: {],}
    }
*/
bool L_P1__Macro6(instance_id_t const my_id , C1_Enumerat1 argom7, C1_Enumerat3 argom8, bool argom9, C1_Enumerat4 argom10, C1_Enumerat2 argom11)
{
bool res_macro_val;
    
    //  *[* *36,*  se il timer MainClass_C1_timer_T5 è scaduto e  se l'argomento argomento_a10 non  è  uguale a avanzamento *39,*  o  se il controllo ConsDef è uguale a FALSE  *38,* o  se il contatore MainClass_C1_contatore_Co5 è  minore di  *55,* 15 *35,* e  se il controllo MainClass_C1_controllo_C7 è  diverso da  True  *109,* o  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  diverso da avanzamento
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_OrLogicOP_2 = false;
    bool res_AndLogicOP_3 = true;
    res_AndLogicOP_3 = (res_AndLogicOP_3 && Timer_Scaduto(L_P1__GetMainc51(my_id)));
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (argom7 == avanzamento));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_4);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_3);
    res_OrLogicOP_2 = (res_OrLogicOP_2 || (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_OrLogicOP_2);
    bool res_AndLogicOP_5 = true;
    res_AndLogicOP_5 = (res_AndLogicOP_5 && (Counter_GetValore(L_P1__GetMainc53(my_id)) < 15u));
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetInMainc3(my_id) == true));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_6);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_5);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_NotLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetMainc27(my_id) == avanzamento));
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! res_NotLogicOP_8);
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_7);
    
    if(res_OrLogicOP_0){
    
    res_macro_val = true;
    }
    else{
    res_macro_val = true;
    }
    return res_macro_val;
}

/*
    CNL corrispondente:
    
    { commento: {[} commento: {34,}  se lo stato  è  uguale a  commento: {53,}  state1  commento: {106,} , assegna alla macro il valore c270xx
    
     commento: {46,} assegna alla macro il valore c270xx commento: {],}
    }
*/
C1_Enumerat3 L_P1__Macro7(instance_id_t const my_id , C1_Enumerat1 argom12, C1_Enumerat1 argom13, C1_Enumerat2 argom14, C1_Enumerat3 argom15)
{
C1_Enumerat3 res_macro_val;
    if((L_P1_C1_GetState(my_id) == C1_St_state)){
    
    res_macro_val = c270xx;
    }
    else{
    res_macro_val = c270xx;
    }
    return res_macro_val;
}

/*
    CNL corrispondente:
    
    { commento: {[} commento: {37,}  se la variabile MainClass_C1_variabile_V3 è  uguale a c270xx o  se la macro  MainClass_C1_macrova_M1    è  uguale a avanzamentox commento: {40,}  e  se la macro  MainClass_C1_macrova_M1    è  diverso da avanzamentox commento: {40,}  , assegna alla macro il valore  True 
    
     commento: {46,} assegna alla macro il valore  False  commento: {],}
    }
*/
bool L_P1__Macro8(instance_id_t const my_id , C1_Enumerat2 argom16, C1_Enumerat4 argom17)
{
bool res_macro_val;
    
    //  *[* *37,*  se la variabile MainClass_C1_variabile_V3 è  uguale a c270xx o  se la macro  MainClass_C1_macrova_M1    è  uguale a avanzamentox *40,*  e  se la macro  MainClass_C1_macrova_M1    è  diverso da avanzamentox
    bool res_OrLogicOP_0 = false;
    res_OrLogicOP_0 = (res_OrLogicOP_0 || (L_P1__GetMainc38(my_id) == c270xx));
    bool res_AndLogicOP_1 = true;
    res_AndLogicOP_1 = (res_AndLogicOP_1 && (L_P1__Macro5(my_id) == avanzamento1));
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (L_P1__Macro5(my_id) == avanzamento1));
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_2);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_1);
    
    if(res_OrLogicOP_0){
    
    res_macro_val = true;
    }
    else{
    res_macro_val = false;
    }
    return res_macro_val;
}

/*
    CNL corrispondente:
     
    { commento: {[} commento: {35,}  se il controllo MainClass_C1_controllo_C9 non è  uguale a avanzamento commento: {37,} e  se la variabile MainClass_C1_variabile_V10 non è  uguale a  False  , assegna alla macro il valore c270xx
    
     commento: {46,} assegna alla macro il valore c270xx commento: {],}
    }
*/
C1_Enumerat3 L_P1__Macro9(instance_id_t const my_id )
{
C1_Enumerat3 res_macro_val;
    
    //  *[* *35,*  se il controllo MainClass_C1_controllo_C9 non è  uguale a avanzamento *37,* e  se la variabile MainClass_C1_variabile_V10 non è  uguale a  False
    bool res_AndLogicOP_0 = true;
    bool res_NotLogicOP_1 = true;
    res_NotLogicOP_1 = (res_NotLogicOP_1 && ! (L_P1__GetInMainc4(my_id) == avanzamento));
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_NotLogicOP_1);
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (L_P1__GetMainc36(my_id) == false));
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_NotLogicOP_2);
    
    if(res_AndLogicOP_0){
    
    res_macro_val = c270xx;
    }
    else{
    res_macro_val = c270xx;
    }
    return res_macro_val;
}



