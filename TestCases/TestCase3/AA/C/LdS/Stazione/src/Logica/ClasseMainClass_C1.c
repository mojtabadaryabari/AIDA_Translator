// Codice del modello 'TestCase3', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#include "Logica/ClasseMainClass_C1.h"
#include "Logica/ClasseMainClass_C1_priv.h"
#include "config.h"
#include "scheduler.h"


// ********** Gestione comandi automatici **********

static size_t L_P1_C1_NumAutoCmds(instance_id_t const my_id)
{
    size_t n = 0u;
    if (L_P1__GetCAEvent1(my_id)) {
        ++n;
    }
    if (L_P1__GetCAEvent2(my_id)) {
        ++n;
    }
    return n;
}


// ********** Gestione comandi manuali **********

static void L_P1_C1_InitCmdsResponse(instance_id_t const my_id)
{
    // for each manual command of L_P1_C1
    if (L_P1__GetInEvent(my_id)) {
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
        if (L_P1__GetInEvent(my_id)) {
            L_P1__SetOutEvent3(my_id, LDS_MANCMD_BLOCKED);
        }
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
    
     commento: {81,}  Ricezione del  comando manuale   MainClass_C1_command_comm10 da  Senderac49796   commento: {76,}
     commento: {67,} commento: {37,}  se la variabile MainClass_C1_variabile_V1 è  diverso da RossoGialloxVerdex e  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} o  se la variabile MainClass_C1_variabile_V3 è  uguale a RossoGialloxVerdex commento: {35,} o  se il controllo MainClass_C1_controllo_C1 è  diverso da  True  e  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} o  se il controllo MainClass_C1_controllo_C9 è  diverso da RossoGialloxVerdex, Tutte le seguenti { 
     commento: {69,} commento: {37,}  se la variabile MainClass_C1_variabile_V9 è  uguale a c180x commento: {37,} e  se la variabile MainClass_C1_variabile_V9 non è  uguale a c180x o  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} o  se il parametro MainClass_C1_parametro_P3 non è  uguale a  commento: {53,} 2 commento: {34,} o  se il parametro MainClass_C1_parametro_P8 è  uguale a  commento: {53,} 8 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
     commento: {38,}  se il contatore MainClass_C1_contatore_Co3 è  minore di  commento: {55,} 13 e  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} o  se il contatore MainClass_C1_contatore_Co3 non è  diverso da  commento: {56,} 14 commento: {36,} o  se il timer MainClass_C1_timer_T2 non è scaduto, Verifica che   commento: {49,}  commento: {,}  il timer MainClass_C1_timer_T5 sia scaduto
    
    
     } Verifica che   commento: {51,}  commento: {,}  il contatore MainClass_C1_contatore_Co3 sia  minore di  commento: {55,} 12
    
    
     } Verifica che   commento: {47,}  commento: {34,}  il parametro MainClass_C1_parametro_P6 sia  diverso da  False 
    
    
    
    }
*/
static inline bool L_P1__Guard1(instance_id_t const my_id)
{
    bool res_AndLogicOP_0 = true;
    
    //  comando manuale   MainClass_C1_command_comm10 da  Senderac49796
    res_AndLogicOP_0 = (res_AndLogicOP_0 && L_P1__GetInEvent(my_id));
    
    //  *76,*
    //   *67,* *37,*  se la variabile MainClass_C1_variabile_V1 è  diverso da RossoGialloxVerdex e  se il controllo ConsDef  è  uguale a FALSE  *37,* o  se la variabile MainClass_C1_variabile_V3 è  uguale a RossoGialloxVerdex *35,* o  se il controllo MainClass_C1_controllo_C1 è  diverso da  True  e  se il controllo ConsDef  è  uguale a FALSE  *35,* o  se il controllo MainClass_C1_controllo_C9 è  diverso da RossoGialloxVerdex, Tutte le seguenti { 
    //   *69,* *37,*  se la variabile MainClass_C1_variabile_V9 è  uguale a c180x *37,* e  se la variabile MainClass_C1_variabile_V9 non è  uguale a c180x o  se il controllo ConsDef  è  uguale a FALSE  *34,* o  se il parametro MainClass_C1_parametro_P3 non è  uguale a  *53,* 2 *34,* o  se il parametro MainClass_C1_parametro_P8 è  uguale a  *53,* 8 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
    //   *38,*  se il contatore MainClass_C1_contatore_Co3 è  minore di  *55,* 13 e  se il controllo ConsDef  è  uguale a FALSE  *38,* o  se il contatore MainClass_C1_contatore_Co3 non è  diverso da  *56,* 14 *36,* o  se il timer MainClass_C1_timer_T2 non è scaduto, Verifica che   *49,*  *,*  il timer MainClass_C1_timer_T5 sia scaduto
    //   } Verifica che   *51,*  *,*  il contatore MainClass_C1_contatore_Co3 sia  minore di  *55,* 12
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_OrLogicOP_4 = false;
    bool res_AndLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetMainc37(my_id) == rossogiallo1));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_6);
    res_AndLogicOP_5 = (res_AndLogicOP_5 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_AndLogicOP_5);
    res_OrLogicOP_4 = (res_OrLogicOP_4 || (L_P1__GetMainc40(my_id) == rossogiallo1));
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_OrLogicOP_4);
    bool res_AndLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetInMainc5(my_id) == true));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_8);
    res_AndLogicOP_7 = (res_AndLogicOP_7 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_AndLogicOP_7);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetInMainc7(my_id) == rossogiallo1));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_9);
    
    if(res_OrLogicOP_2){
    bool res_AndLogicOP_10 = true;
    bool res_ImpliesLogicOp_11 = true;
    bool res_OrLogicOP_12 = false;
    bool res_OrLogicOP_13 = false;
    bool res_OrLogicOP_14 = false;
    bool res_AndLogicOP_15 = true;
    res_AndLogicOP_15 = (res_AndLogicOP_15 && (L_P1__GetMainc41(my_id) == c180x));
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (L_P1__GetMainc41(my_id) == c180x));
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_NotLogicOP_16);
    
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_AndLogicOP_15);
    res_OrLogicOP_14 = (res_OrLogicOP_14 || (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_OrLogicOP_14);
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! (L_P1__GetParamMainc9(my_id) == 2u));
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_NotLogicOP_17);
    
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_OrLogicOP_13);
    bool res_AndLogicOP_18 = true;
    res_AndLogicOP_18 = (res_AndLogicOP_18 && (L_P1__GetParamMainc12(my_id) == 8u));
    res_AndLogicOP_18 = (res_AndLogicOP_18 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_AndLogicOP_18);
    
    if(res_OrLogicOP_12){
    bool res_ImpliesLogicOp_19 = true;
    bool res_OrLogicOP_20 = false;
    bool res_OrLogicOP_21 = false;
    bool res_AndLogicOP_22 = true;
    res_AndLogicOP_22 = (res_AndLogicOP_22 && (Counter_GetValore(L_P1__GetMainc52(my_id)) < 13u));
    res_AndLogicOP_22 = (res_AndLogicOP_22 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_21 = (res_OrLogicOP_21 || res_AndLogicOP_22);
    bool res_NotLogicOP_23 = true;
    bool res_NotLogicOP_24 = true;
    res_NotLogicOP_24 = (res_NotLogicOP_24 && ! (Counter_GetValore(L_P1__GetMainc52(my_id)) == 14u));
    res_NotLogicOP_23 = (res_NotLogicOP_23 && ! res_NotLogicOP_24);
    res_OrLogicOP_21 = (res_OrLogicOP_21 || res_NotLogicOP_23);
    
    res_OrLogicOP_20 = (res_OrLogicOP_20 || res_OrLogicOP_21);
    bool res_NotLogicOP_25 = true;
    res_NotLogicOP_25 = (res_NotLogicOP_25 && ! Timer_Scaduto(L_P1__GetMainc50(my_id)));
    res_OrLogicOP_20 = (res_OrLogicOP_20 || res_NotLogicOP_25);
    
    if(res_OrLogicOP_20){
    res_ImpliesLogicOp_19 = (res_ImpliesLogicOp_19 && Timer_Scaduto(L_P1__GetMainc51(my_id)));
    }
    res_ImpliesLogicOp_11 = (res_ImpliesLogicOp_11 && res_ImpliesLogicOp_19);
    }
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_ImpliesLogicOp_11);
    res_AndLogicOP_10 = (res_AndLogicOP_10 && (Counter_GetValore(L_P1__GetMainc52(my_id)) < 12u));
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_AndLogicOP_10);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *47,*  *34,*  il parametro MainClass_C1_parametro_P6 sia  diverso da  False
    bool res_NotLogicOP_26 = true;
    res_NotLogicOP_26 = (res_NotLogicOP_26 && ! (L_P1__GetParamMainc10(my_id) == false));
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_NotLogicOP_26);
    
    if(res_AndLogicOP_0){
    L_P1__SetOutEvent3(my_id,LDS_MANCMD_PROCESSED);
    }
    else{
    
    }
    
    
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
    
      se il ripristino dello stato  non è  uguale a  commento: {53,}  state1  commento: {107,} commento: {37,} e  se la variabile MainClass_C1_variabile_V10 è  diverso da  commento: {56,} 1 commento: {37,} o  se la variabile MainClass_C1_variabile_V1 non è  uguale a RossoGialloxVerdex commento: {35,} e  se il controllo MainClass_C1_controllo_C2 è  uguale a  True , commento: {68,}Attiva il timer MainClass_C1_timer_T2
    
     ,altrimenti  commento: {66,} Assegna al comando MainClass_C1_comando_C2 il valore  False 
    
    
      se il controllo ConsDef  è  uguale a FALSE  commento: {38,} o  se il contatore MainClass_C1_contatore_Co3 non è  diverso da  commento: {56,} 123,  Applica gli effetti
           della macro MainClass_C1_macroef_M1  commento: {73,}
    
       
    
    }
*/
static inline void L_P1__Effec1(instance_id_t const my_id)
{
    
    //  se il ripristino dello stato  non è  uguale a  *53,*  state1  *107,* *37,* e  se la variabile MainClass_C1_variabile_V10 è  diverso da  *56,* 1 *37,* o  se la variabile MainClass_C1_variabile_V1 non è  uguale a RossoGialloxVerdex *35,* e  se il controllo MainClass_C1_controllo_C2 è  uguale a  True , *68,*Attiva il timer MainClass_C1_timer_T2
    //   ,altrimenti  *66,* Assegna al comando MainClass_C1_comando_C2 il valore  False
    bool res_OrLogicOP_0 = false;
    bool res_AndLogicOP_1 = true;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (L_P1__GetStato1(my_id) == C1_St_state));
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_2);
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__GetMainc38(my_id) == 1u));
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_3);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_1);
    bool res_AndLogicOP_4 = true;
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetMainc37(my_id) == rossogiallo1));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_5);
    res_AndLogicOP_4 = (res_AndLogicOP_4 && (L_P1__GetInMainc6(my_id) == true));
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_4);
    
    if(res_OrLogicOP_0){
    
    Timer_Attiva(L_P1__GetMainc50(my_id));
    }else{
    
    L_P1__SetOutMainc(my_id,false);
    }
    
    //  se il controllo ConsDef  è  uguale a FALSE  *38,* o  se il contatore MainClass_C1_contatore_Co3 non è  diverso da  *56,* 123,  Applica gli effetti
    //         della macro MainClass_C1_macroef_M1
    bool res_OrLogicOP_6 = false;
    res_OrLogicOP_6 = (res_OrLogicOP_6 || (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (Counter_GetValore(L_P1__GetMainc52(my_id)) == 123u));
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! res_NotLogicOP_8);
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_NotLogicOP_7);
    
    if(res_OrLogicOP_6){
    
    L_P1__Macro(my_id);
    }
}



// ********** Definizione metodi **********

// Metodi standard

void L_P1_C1_Init(instance_id_t const my_id)
{
    // init variabili di stato
    L_P1__SetMainc21(my_id, c270xx);
    L_P1__SetMainc23(my_id, 0);
    L_P1__SetMainc25(my_id, 0);
    L_P1__SetMainc27(my_id, avvio);
    L_P1__SetMainc28(my_id, avvio);
    L_P1__SetMainc29(my_id, false);
    L_P1__SetMainc30(my_id, false);
    L_P1__SetMainc31(my_id, false);
    L_P1__SetMainc32(my_id, false);
    L_P1__SetMainc33(my_id, 0);
    L_P1__SetMainc34(my_id, 0);
    L_P1__SetMainc35(my_id, false);
    L_P1__SetMainc36(my_id, false);
    L_P1__SetMainc37(my_id, rossogiallo);
    L_P1__SetMainc38(my_id, 0);
    L_P1__SetMainc39(my_id, 0);
    L_P1__SetMainc40(my_id, rossogiallo);
    L_P1__SetMainc41(my_id, rossoverde);
    L_P1__SetStato1(my_id, C1_St_Stato);
    // init controlli precedenti
    L_P1__SetMainc14(my_id, c180x);
    L_P1__SetMainc16(my_id, false);
    L_P1__SetMainc18(my_id, true);
    L_P1__SetMainc20(my_id, false);
    // init Timer e Counter
    Timer_AggmInit(L_P1__GetMainc42(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc42_ID);
    Timer_Init(L_P1__GetMainc42(my_id), 340000);
    Timer_AggmInit(L_P1__GetMainc43(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc43_ID);
    Timer_Init(L_P1__GetMainc43(my_id), 340000);
    Timer_AggmInit(L_P1__GetMainc44(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc44_ID);
    Timer_Init(L_P1__GetMainc44(my_id), 1315000);
    Timer_AggmInit(L_P1__GetMainc45(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc45_ID);
    Timer_Init(L_P1__GetMainc45(my_id), 1315000);
    Timer_AggmInit(L_P1__GetMainc46(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc46_ID);
    Timer_Init(L_P1__GetMainc46(my_id), 424000);
    Timer_AggmInit(L_P1__GetMainc47(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc47_ID);
    Timer_Init(L_P1__GetMainc47(my_id), 424000);
    Timer_AggmInit(L_P1__GetMainc48(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc48_ID);
    Timer_Init(L_P1__GetMainc48(my_id), 50000);
    Timer_AggmInit(L_P1__GetMainc49(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc49_ID);
    Timer_Init(L_P1__GetMainc49(my_id), 50000);
    Timer_AggmInit(L_P1__GetMainc50(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc50_ID);
    Timer_Init(L_P1__GetMainc50(my_id), 4152000);
    Timer_AggmInit(L_P1__GetMainc51(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc51_ID);
    Timer_Init(L_P1__GetMainc51(my_id), 23000);
    Counter_AggmInit(L_P1__GetMainc52(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc52_ID);
    Counter_Init(L_P1__GetMainc52(my_id));
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
    L_P1__SetMainc22(my_id, L_P1__GetMainc21(my_id));
    L_P1__SetMainc24(my_id, L_P1__GetMainc23(my_id));
    L_P1__SetMainc26(my_id, L_P1__GetMainc25(my_id));
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
            if (L_P1__Guard1(my_id)) {
                L_P1_C1_SetState(my_id, C1_St_state);
                L_P1__Effec1(my_id);				
            }
            else
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
    L_P1__SetOutMainc1(my_id, rossogiallo2);
    L_P1__SetOutMainc2(my_id, rossogiallo2);
    L_P1__SetOutMainc3(my_id, rossogiallo2);
    L_P1__SetOutMainc4(my_id, rossogiallo1);
}

void L_P1_C1_GUpdatePrev(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C1(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C1(proc_id);
    L_P1__SetMainc14(my_id, L_P1__GetInMainc13(my_id));
    L_P1__SetMainc16(my_id, L_P1__GetInMainc15(my_id));
    L_P1__SetMainc18(my_id, L_P1__GetInMainc17(my_id));
    L_P1__SetMainc20(my_id, L_P1__GetInMainc19(my_id));
    L_P1__SetMainc22(my_id, L_P1__GetMainc21(my_id));
    L_P1__SetMainc24(my_id, L_P1__GetMainc23(my_id));
    L_P1__SetMainc26(my_id, L_P1__GetMainc25(my_id));
}

// ********** Definizione macro **********

// Macro di effetto

/*
    CNL corrispondente:
    
    {  se la macro  MainClass_C1_macrova_M5 ( con argomento_a1   uguale a True  e argomento_a8   uguale a RossoVerde )   è  diverso da RossoGialloxVerdex commento: {40,}  commento: {37,} e  se la variabile MainClass_C1_variabile_V1 è  diverso da RossoGialloxVerdex commento: {38,} e  se il contatore MainClass_C1_contatore_Co3 non è  minore di  commento: {55,} 15240, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V1 il valore RossoGialloxVerdex
    
     ,altrimenti  commento: {70,}Incrementa il contatore MainClass_C1_contatore_Co3
    
    
      se il controllo ConsDef  è  uguale a FALSE  commento: {37,} o  se la variabile MainClass_C1_variabile_V1 non è  diverso da RossoGialloxVerdex e  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} o  se il parametro MainClass_C1_parametro_P3 non è  minore di  commento: {55,} 4 commento: {35,} e  se il controllo MainClass_C1_controllo_C9 è  uguale a RossoGialloxVerdex o  se il controllo ConsDef  è  uguale a FALSE , commento: {66,} Assegna al comando MainClass_C1_comando_C3 il valore RossoGiallox
    
     ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V1 il valore RossoGialloxVerdex
    
    
     commento: {38,}  se il contatore MainClass_C1_contatore_Co3 è  minore di  commento: {55,} 11, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V9 il valore c180x
    
     ,altrimenti  commento: {69,}Disattiva il timer MainClass_C1_timer_T2
    
    
     commento: {37,}  se la variabile MainClass_C1_variabile_V9 non è  diverso da c180x o  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} e  se la variabile MainClass_C1_variabile_V9 è  uguale a c180x, commento: {66,} Assegna al comando MainClass_C1_comando_C7 il valore RossoGiallox
    
       
    
    }
*/
void L_P1__Macro(instance_id_t const my_id )
{
//  se la macro  MainClass_C1_macrova_M5 ( con argomento_a1   uguale a True  e argomento_a8   uguale a RossoVerde )   è  diverso da RossoGialloxVerdex *40,*  *37,* e  se la variabile MainClass_C1_variabile_V1 è  diverso da RossoGialloxVerdex *38,* e  se il contatore MainClass_C1_contatore_Co3 non è  minore di  *55,* 15240, *67,* Assegna alla variabile MainClass_C1_variabile_V1 il valore RossoGialloxVerdex
    // ,altrimenti  *70,*Incrementa il contatore MainClass_C1_contatore_Co3
    bool res_AndLogicOP_0 = true;
    bool res_AndLogicOP_1 = true;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (L_P1__Macro2(my_id,true,rossoverde) == rossogiallo1));
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_2);
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__GetMainc37(my_id) == rossogiallo1));
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_3);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_AndLogicOP_1);
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (Counter_GetValore(L_P1__GetMainc52(my_id)) < 15240u));
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_NotLogicOP_4);
    
    if(res_AndLogicOP_0){
    
    L_P1__SetMainc37(my_id,rossogiallo1);
    }else{
    
    Counter_Incr(L_P1__GetMainc52(my_id));
    }
    //  se il controllo ConsDef  è  uguale a FALSE  *37,* o  se la variabile MainClass_C1_variabile_V1 non è  diverso da RossoGialloxVerdex e  se il controllo ConsDef  è  uguale a FALSE  *34,* o  se il parametro MainClass_C1_parametro_P3 non è  minore di  *55,* 4 *35,* e  se il controllo MainClass_C1_controllo_C9 è  uguale a RossoGialloxVerdex o  se il controllo ConsDef  è  uguale a FALSE , *66,* Assegna al comando MainClass_C1_comando_C3 il valore RossoGiallox
    // ,altrimenti  *67,* Assegna alla variabile MainClass_C1_variabile_V1 il valore RossoGialloxVerdex
    bool res_OrLogicOP_5 = false;
    bool res_OrLogicOP_6 = false;
    bool res_OrLogicOP_7 = false;
    res_OrLogicOP_7 = (res_OrLogicOP_7 || (L_P1__GetInConsd(my_id) == false));
    bool res_AndLogicOP_8 = true;
    bool res_NotLogicOP_9 = true;
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__GetMainc37(my_id) == rossogiallo1));
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! res_NotLogicOP_10);
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_9);
    res_AndLogicOP_8 = (res_AndLogicOP_8 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_AndLogicOP_8);
    
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_OrLogicOP_7);
    bool res_AndLogicOP_11 = true;
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (L_P1__GetParamMainc9(my_id) < 4u));
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_NotLogicOP_12);
    res_AndLogicOP_11 = (res_AndLogicOP_11 && (L_P1__GetInMainc7(my_id) == rossogiallo1));
    
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_AndLogicOP_11);
    
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_OrLogicOP_6);
    res_OrLogicOP_5 = (res_OrLogicOP_5 || (L_P1__GetInConsd(my_id) == false));
    
    if(res_OrLogicOP_5){
    
    L_P1__SetOutMainc1(my_id,rossogiallo2);
    }else{
    
    L_P1__SetMainc37(my_id,rossogiallo1);
    }
    //  *38,*  se il contatore MainClass_C1_contatore_Co3 è  minore di  *55,* 11, *67,* Assegna alla variabile MainClass_C1_variabile_V9 il valore c180x
    // ,altrimenti  *69,*Disattiva il timer MainClass_C1_timer_T2
    if((Counter_GetValore(L_P1__GetMainc52(my_id)) < 11u)){
    
    L_P1__SetMainc41(my_id,c180x);
    }else{
    
    Timer_Disattiva(L_P1__GetMainc50(my_id));
    }
    //  *37,*  se la variabile MainClass_C1_variabile_V9 non è  diverso da c180x o  se il controllo ConsDef  è  uguale a FALSE  *37,* e  se la variabile MainClass_C1_variabile_V9 è  uguale a c180x, *66,* Assegna al comando MainClass_C1_comando_C7 il valore RossoGiallox
    bool res_OrLogicOP_13 = false;
    bool res_NotLogicOP_14 = true;
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (L_P1__GetMainc41(my_id) == c180x));
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! res_NotLogicOP_15);
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_NotLogicOP_14);
    bool res_AndLogicOP_16 = true;
    res_AndLogicOP_16 = (res_AndLogicOP_16 && (L_P1__GetInConsd(my_id) == false));
    res_AndLogicOP_16 = (res_AndLogicOP_16 && (L_P1__GetMainc41(my_id) == c180x));
    
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_AndLogicOP_16);
    
    if(res_OrLogicOP_13){
    
    L_P1__SetOutMainc2(my_id,rossogiallo2);
    }
}

/*
    CNL corrispondente:
    
    {  se la macro  MainClass_C1_macrova_M7 ( con argomento_a4   uguale a True ,argomento_a7   uguale a RossoVerde ,argomento_a2   uguale a c180x  e argomento_a6   uguale a c270xx )   è  uguale a RossoGiallox commento: {40,}  commento: {38,} o  se il contatore MainClass_C1_contatore_Co3 non è  diverso da  commento: {56,} 13152 commento: {36,} o  se il timer MainClass_C1_timer_T2 non è disattivo commento: {35,} o  se il controllo MainClass_C1_controllo_C2 è  uguale a  True  commento: {36,} o  se il timer MainClass_C1_timer_T5 è scaduto commento: {35,} o  se il controllo MainClass_C1_controllo_C9 non è  uguale a RossoGialloxVerdex, commento: {68,}Attiva il timer MainClass_C1_timer_T5
    
     ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V1 il valore RossoGialloxVerdex
    
    
     commento: {35,}  se il controllo MainClass_C1_controllo_C9 è  diverso da RossoGialloxVerdex commento: {35,} o  se il controllo MainClass_C1_controllo_C2 è  diverso da  True ,  Applica gli effetti
           della macro MainClass_C1_macroef_M1  commento: {73,}
    
     ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V1 il valore RossoGialloxVerdex
    
    
     commento: {34,}  se lo stato  non è  diverso da  commento: {56,}  state1  commento: {106,} commento: {37,} o  se la variabile MainClass_C1_variabile_V1 è  uguale a RossoGialloxVerdex commento: {34,} e  se il parametro MainClass_C1_parametro_P3 non è  diverso da  commento: {56,} 8 commento: {34,} e  se il parametro MainClass_C1_parametro_P3 è  minore di  commento: {55,} 5, commento: {68,}Attiva il timer MainClass_C1_timer_T5
    
       
      se il controllo ConsDef è uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE , commento: {70,}Incrementa il contatore MainClass_C1_contatore_Co3
    
       
     commento: {34,}  se il parametro MainClass_C1_parametro_P8 non è  minore di  commento: {55,} 4 commento: {34,} e  se il parametro MainClass_C1_parametro_P10 è  diverso da  commento: {56,} 10 e  se il controllo ConsDef  è  uguale a FALSE , commento: {67,} Assegna alla variabile MainClass_C1_variabile_V1 il valore RossoGialloxVerdex
    
       
    
    }
*/
void L_P1__Macro1(instance_id_t const my_id )
{
//  se la macro  MainClass_C1_macrova_M7 ( con argomento_a4   uguale a True ,argomento_a7   uguale a RossoVerde ,argomento_a2   uguale a c180x  e argomento_a6   uguale a c270xx )   è  uguale a RossoGiallox *40,*  *38,* o  se il contatore MainClass_C1_contatore_Co3 non è  diverso da  *56,* 13152 *36,* o  se il timer MainClass_C1_timer_T2 non è disattivo *35,* o  se il controllo MainClass_C1_controllo_C2 è  uguale a  True  *36,* o  se il timer MainClass_C1_timer_T5 è scaduto *35,* o  se il controllo MainClass_C1_controllo_C9 non è  uguale a RossoGialloxVerdex, *68,*Attiva il timer MainClass_C1_timer_T5
    // ,altrimenti  *67,* Assegna alla variabile MainClass_C1_variabile_V1 il valore RossoGialloxVerdex
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_OrLogicOP_4 = false;
    res_OrLogicOP_4 = (res_OrLogicOP_4 || (L_P1__Macro4(my_id,c180x,true,c270xx,rossoverde) == rossogiallo2));
    bool res_NotLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (Counter_GetValore(L_P1__GetMainc52(my_id)) == 13152u));
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! res_NotLogicOP_6);
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_NotLogicOP_5);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_OrLogicOP_4);
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! Timer_Disattivo(L_P1__GetMainc50(my_id)));
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_NotLogicOP_7);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    res_OrLogicOP_2 = (res_OrLogicOP_2 || (L_P1__GetInMainc6(my_id) == true));
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_OrLogicOP_2);
    res_OrLogicOP_1 = (res_OrLogicOP_1 || Timer_Scaduto(L_P1__GetMainc51(my_id)));
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetInMainc7(my_id) == rossogiallo1));
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_8);
    
    if(res_OrLogicOP_0){
    
    Timer_Attiva(L_P1__GetMainc51(my_id));
    }else{
    
    L_P1__SetMainc37(my_id,rossogiallo1);
    }
    //  *35,*  se il controllo MainClass_C1_controllo_C9 è  diverso da RossoGialloxVerdex *35,* o  se il controllo MainClass_C1_controllo_C2 è  diverso da  True ,  Applica gli effetti
    //       della macro MainClass_C1_macroef_M1  *73,*
    // ,altrimenti  *67,* Assegna alla variabile MainClass_C1_variabile_V1 il valore RossoGialloxVerdex
    bool res_OrLogicOP_9 = false;
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__GetInMainc7(my_id) == rossogiallo1));
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_NotLogicOP_10);
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (L_P1__GetInMainc6(my_id) == true));
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_NotLogicOP_11);
    
    if(res_OrLogicOP_9){
    
    L_P1__Macro(my_id);
    }else{
    
    L_P1__SetMainc37(my_id,rossogiallo1);
    }
    //  *34,*  se lo stato  non è  diverso da  *56,*  state1  *106,* *37,* o  se la variabile MainClass_C1_variabile_V1 è  uguale a RossoGialloxVerdex *34,* e  se il parametro MainClass_C1_parametro_P3 non è  diverso da  *56,* 8 *34,* e  se il parametro MainClass_C1_parametro_P3 è  minore di  *55,* 5, *68,*Attiva il timer MainClass_C1_timer_T5
    bool res_OrLogicOP_12 = false;
    bool res_NotLogicOP_13 = true;
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1_C1_GetState(my_id) == C1_St_state));
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! res_NotLogicOP_14);
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_NotLogicOP_13);
    bool res_AndLogicOP_15 = true;
    bool res_AndLogicOP_16 = true;
    res_AndLogicOP_16 = (res_AndLogicOP_16 && (L_P1__GetMainc37(my_id) == rossogiallo1));
    bool res_NotLogicOP_17 = true;
    bool res_NotLogicOP_18 = true;
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! (L_P1__GetParamMainc9(my_id) == 8u));
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! res_NotLogicOP_18);
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_NotLogicOP_17);
    
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_AndLogicOP_16);
    res_AndLogicOP_15 = (res_AndLogicOP_15 && (L_P1__GetParamMainc9(my_id) < 5u));
    
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_AndLogicOP_15);
    
    if(res_OrLogicOP_12){
    
    Timer_Attiva(L_P1__GetMainc51(my_id));
    }
    //  se il controllo ConsDef è uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE , *70,*Incrementa il contatore MainClass_C1_contatore_Co3
    bool res_OrLogicOP_19 = false;
    res_OrLogicOP_19 = (res_OrLogicOP_19 || (L_P1__GetInConsd(my_id) == false));
    res_OrLogicOP_19 = (res_OrLogicOP_19 || (L_P1__GetInConsd(my_id) == false));
    
    if(res_OrLogicOP_19){
    
    Counter_Incr(L_P1__GetMainc52(my_id));
    }
    //  *34,*  se il parametro MainClass_C1_parametro_P8 non è  minore di  *55,* 4 *34,* e  se il parametro MainClass_C1_parametro_P10 è  diverso da  *56,* 10 e  se il controllo ConsDef  è  uguale a FALSE , *67,* Assegna alla variabile MainClass_C1_variabile_V1 il valore RossoGialloxVerdex
    bool res_AndLogicOP_20 = true;
    bool res_AndLogicOP_21 = true;
    bool res_NotLogicOP_22 = true;
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! (L_P1__GetParamMainc12(my_id) < 4u));
    res_AndLogicOP_21 = (res_AndLogicOP_21 && res_NotLogicOP_22);
    bool res_NotLogicOP_23 = true;
    res_NotLogicOP_23 = (res_NotLogicOP_23 && ! (L_P1__GetParamMainc8(my_id) == 10u));
    res_AndLogicOP_21 = (res_AndLogicOP_21 && res_NotLogicOP_23);
    
    res_AndLogicOP_20 = (res_AndLogicOP_20 && res_AndLogicOP_21);
    res_AndLogicOP_20 = (res_AndLogicOP_20 && (L_P1__GetInConsd(my_id) == false));
    
    if(res_AndLogicOP_20){
    
    L_P1__SetMainc37(my_id,rossogiallo1);
    }
}


// Macro di verifica

/*
    CNL corrispondente:
     
    { commento: {62,} commento: {34,}  se il parametro MainClass_C1_parametro_P3 è  minore di  commento: {55,} 2 commento: {35,} e  se il controllo MainClass_C1_controllo_C9 non è  diverso da RossoGialloxVerdex commento: {34,} e  se il parametro MainClass_C1_parametro_P3 è  maggiore di  commento: {54,} 7 commento: {34,} e  se il parametro MainClass_C1_parametro_P3 è  diverso da  commento: {56,} 6 commento: {34,} o  se il parametro MainClass_C1_parametro_P3 non è  maggiore di  commento: {54,} 5 commento: {34,} o  se il parametro MainClass_C1_parametro_P3 non è  uguale a  commento: {53,} 1, Almeno una delle seguenti { 
     commento: {37,}  se la variabile MainClass_C1_variabile_V10 non è  maggiore di  commento: {54,} 3 e  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   commento: {47,48,49,}  commento: {,}  il controllo MainClass_C1_controllo_C1 sia  uguale a  False 
     commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T5 non sia attivo
     commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P8 non sia  maggiore di  commento: {54,} 10
    
    
     } Verifica che   commento: {47,48,}  commento: {,}  il controllo MainClass_C1_controllo_C9 non sia  uguale a RossoGialloxVerdex
     commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P3 sia  minore di  commento: {55,} 6
     commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
    
    
    }
*/
bool L_P1__Macro6(instance_id_t const my_id )
{
bool res_AndLogicOP_0 = true;
    
    //  *62,* *34,*  se il parametro MainClass_C1_parametro_P3 è  minore di  *55,* 2 *35,* e  se il controllo MainClass_C1_controllo_C9 non è  diverso da RossoGialloxVerdex *34,* e  se il parametro MainClass_C1_parametro_P3 è  maggiore di  *54,* 7 *34,* e  se il parametro MainClass_C1_parametro_P3 è  diverso da  *56,* 6 *34,* o  se il parametro MainClass_C1_parametro_P3 non è  maggiore di  *54,* 5 *34,* o  se il parametro MainClass_C1_parametro_P3 non è  uguale a  *53,* 1, Almeno una delle seguenti { 
    //   *37,*  se la variabile MainClass_C1_variabile_V10 non è  maggiore di  *54,* 3 e  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   *47,48,49,*  *,*  il controllo MainClass_C1_controllo_C1 sia  uguale a  False 
    //   *104,* o  che  *,*  il timer MainClass_C1_timer_T5 non sia attivo
    //   *104,* e  che  *34,*  il parametro MainClass_C1_parametro_P8 non sia  maggiore di  *54,* 10
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_AndLogicOP_4 = true;
    bool res_AndLogicOP_5 = true;
    bool res_AndLogicOP_6 = true;
    res_AndLogicOP_6 = (res_AndLogicOP_6 && (L_P1__GetParamMainc9(my_id) < 2u));
    bool res_NotLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetInMainc7(my_id) == rossogiallo1));
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! res_NotLogicOP_8);
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_7);
    
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_AndLogicOP_6);
    res_AndLogicOP_5 = (res_AndLogicOP_5 && (L_P1__GetParamMainc9(my_id) > 7u));
    
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_AndLogicOP_5);
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetParamMainc9(my_id) == 6u));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_9);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_AndLogicOP_4);
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__GetParamMainc9(my_id) > 5u));
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_NotLogicOP_10);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (L_P1__GetParamMainc9(my_id) == 1u));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_11);
    
    if(res_OrLogicOP_2){
    bool res_ImpliesLogicOp_12 = true;
    bool res_OrLogicOP_13 = false;
    bool res_AndLogicOP_14 = true;
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (L_P1__GetMainc38(my_id) > 3u));
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_NotLogicOP_15);
    res_AndLogicOP_14 = (res_AndLogicOP_14 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_AndLogicOP_14);
    res_OrLogicOP_13 = (res_OrLogicOP_13 || (L_P1__GetInConsd(my_id) == false));
    
    if(res_OrLogicOP_13){
    bool res_OrLogicOP_16 = false;
    res_OrLogicOP_16 = (res_OrLogicOP_16 || (L_P1__GetInMainc5(my_id) == false));
    bool res_AndLogicOP_17 = true;
    bool res_NotLogicOP_18 = true;
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! Timer_Attivo(L_P1__GetMainc51(my_id)));
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_NotLogicOP_18);
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (L_P1__GetParamMainc12(my_id) > 10u));
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_NotLogicOP_19);
    
    res_OrLogicOP_16 = (res_OrLogicOP_16 || res_AndLogicOP_17);
    
    res_ImpliesLogicOp_12 = (res_ImpliesLogicOp_12 && res_OrLogicOP_16);
    }
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_ImpliesLogicOp_12);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *47,48,*  *,*  il controllo MainClass_C1_controllo_C9 non sia  uguale a RossoGialloxVerdex
    //   *104,* o  che  *34,*  il parametro MainClass_C1_parametro_P3 sia  minore di  *55,* 6
    //   *104,* e  che   il controllo ConsDef  sia  uguale a FALSE
    bool res_OrLogicOP_20 = false;
    bool res_NotLogicOP_21 = true;
    res_NotLogicOP_21 = (res_NotLogicOP_21 && ! (L_P1__GetInMainc7(my_id) == rossogiallo1));
    res_OrLogicOP_20 = (res_OrLogicOP_20 || res_NotLogicOP_21);
    bool res_AndLogicOP_22 = true;
    res_AndLogicOP_22 = (res_AndLogicOP_22 && (L_P1__GetParamMainc9(my_id) < 6u));
    res_AndLogicOP_22 = (res_AndLogicOP_22 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_20 = (res_OrLogicOP_20 || res_AndLogicOP_22);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_20);
    
    
    
    return res_AndLogicOP_0;
}


// Macro valorizzate

/*
    CNL corrispondente:
    
    { commento: {[} commento: {36,}  se il timer MainClass_C1_timer_T2 non è scaduto , assegna alla macro il valore RossoGialloxVerdex
    
     commento: {46,} assegna alla macro il valore RossoGialloxVerdex commento: {],}
    }
*/
C1_Enumerat1 L_P1__Macro2(instance_id_t const my_id , bool argom4, C1_Enumerat4 argom5)
{
C1_Enumerat1 res_macro_val;
    
    //  il timer MainClass_C1_timer_T2 non è scaduto
    bool res_NotLogicOP_0 = true;
    res_NotLogicOP_0 = (res_NotLogicOP_0 && ! Timer_Scaduto(L_P1__GetMainc50(my_id)));
    if(res_NotLogicOP_0){
    
    res_macro_val = rossogiallo1;
    }
    else{
    res_macro_val = rossogiallo1;
    }
    return res_macro_val;
}

/*
    CNL corrispondente:
    
    { commento: {[}
     commento: {46,} assegna alla macro il valore c180x commento: {],}
    }
*/
C1_Enumerat4 L_P1__Macro3(instance_id_t const my_id , C1_Enumerat2 argom6, C1_Enumerat4 argom7, C1_Enumerat1 argom8, C1_Enumerat1 argom9, C1_Enumerat2 argom10, C1_Enumerat1 argom11)
{
return c180x;
}

/*
    CNL corrispondente:
    
    { commento: {[}
     commento: {46,} assegna alla macro il valore RossoGiallox commento: {],}
    }
*/
C1_Enumerat2 L_P1__Macro4(instance_id_t const my_id , C1_Enumerat4 argom12, bool argom13, C1_Enumerat2 argom14, C1_Enumerat4 argom15)
{
return rossogiallo2;
}

/*
    CNL corrispondente:
    
    { commento: {[} commento: {35,}  se il controllo MainClass_C1_controllo_C9 è  uguale a RossoGialloxVerdex commento: {36,} e  se il timer MainClass_C1_timer_T2 è scaduto e  se la macro  MainClass_C1_macrova_M6 ( con argomento_a4   uguale a RossoGialloaVerdea ,argomento_a7   uguale a RossoGiallox ,argomento_a2   uguale a RossoGiallox ,argomento_a6   uguale a RossoGialloaVerdea ,argomento_a3   uguale a RossoVerde  e argomento_a9   uguale a RossoGialloaVerdea )   è  uguale a c180x commento: {40,}  commento: {34,} e  se lo stato  non è  uguale a  commento: {53,}  state1  commento: {106,} , assegna alla macro il valore  False 
    
     commento: {46,} assegna alla macro il valore  False  commento: {],}
    }
*/
bool L_P1__Macro5(instance_id_t const my_id , C1_Enumerat3 argom16, bool argom17)
{
bool res_macro_val;
    
    //  *[* *35,*  se il controllo MainClass_C1_controllo_C9 è  uguale a RossoGialloxVerdex *36,* e  se il timer MainClass_C1_timer_T2 è scaduto e  se la macro  MainClass_C1_macrova_M6 ( con argomento_a4   uguale a RossoGialloaVerdea ,argomento_a7   uguale a RossoGiallox ,argomento_a2   uguale a RossoGiallox ,argomento_a6   uguale a RossoGialloaVerdea ,argomento_a3   uguale a RossoVerde  e argomento_a9   uguale a RossoGialloaVerdea )   è  uguale a c180x *40,*  *34,* e  se lo stato  non è  uguale a  *53,*  state1
    bool res_AndLogicOP_0 = true;
    bool res_AndLogicOP_1 = true;
    bool res_AndLogicOP_2 = true;
    res_AndLogicOP_2 = (res_AndLogicOP_2 && (L_P1__GetInMainc7(my_id) == rossogiallo1));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && Timer_Scaduto(L_P1__GetMainc50(my_id)));
    
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_AndLogicOP_2);
    res_AndLogicOP_1 = (res_AndLogicOP_1 && (L_P1__Macro3(my_id,rossogiallo2,rossoverde,rossogiallo,rossogiallo,rossogiallo2,rossogiallo) == c180x));
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_AndLogicOP_1);
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1_C1_GetState(my_id) == C1_St_state));
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_NotLogicOP_3);
    
    if(res_AndLogicOP_0){
    
    res_macro_val = false;
    }
    else{
    res_macro_val = false;
    }
    return res_macro_val;
}



