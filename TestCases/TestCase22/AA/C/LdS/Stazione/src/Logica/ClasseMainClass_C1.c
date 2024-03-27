// Codice del modello 'TestCase22', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#include "Logica/ClasseMainClass_C1.h"
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
    if (L_P1__GetCAEvent1(my_id)) {
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
    L_P1__SetMainc18(my_id, 0);
    L_P1__SetMainc20(my_id, false);
    L_P1__SetMainc22(my_id, 0);
    L_P1__SetMainc23(my_id, 0);
    L_P1__SetMainc24(my_id, 0);
    L_P1__SetMainc25(my_id, 0);
    L_P1__SetMainc26(my_id, false);
    L_P1__SetMainc27(my_id, false);
    L_P1__SetMainc28(my_id, 0);
    L_P1__SetMainc29(my_id, 0);
    L_P1__SetMainc30(my_id, false);
    L_P1__SetMainc31(my_id, false);
    L_P1__SetMainc32(my_id, rossogiallo1);
    L_P1__SetMainc33(my_id, 0);
    L_P1__SetMainc34(my_id, avviox);
    L_P1__SetStato1(my_id, C1_St_Stato);
    // init controlli precedenti
    L_P1__SetMainc11(my_id, rossogiallo2);
    L_P1__SetMainc13(my_id, false);
    L_P1__SetMainc15(my_id, spento);
    L_P1__SetMainc17(my_id, rossoverde);
    // init Timer e Counter
    Timer_AggmInit(L_P1__GetMainc35(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc35_ID);
    Timer_Init(L_P1__GetMainc35(my_id), 30000);
    Timer_AggmInit(L_P1__GetMainc36(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc36_ID);
    Timer_Init(L_P1__GetMainc36(my_id), 30000);
    Timer_AggmInit(L_P1__GetMainc37(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc37_ID);
    Timer_Init(L_P1__GetMainc37(my_id), 23000);
    Timer_AggmInit(L_P1__GetMainc38(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc38_ID);
    Timer_Init(L_P1__GetMainc38(my_id), 23000);
    Timer_AggmInit(L_P1__GetMainc39(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc39_ID);
    Timer_Init(L_P1__GetMainc39(my_id), 2000);
    Timer_AggmInit(L_P1__GetMainc40(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc40_ID);
    Timer_Init(L_P1__GetMainc40(my_id), 41000);
    Timer_AggmInit(L_P1__GetMainc41(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc41_ID);
    Timer_Init(L_P1__GetMainc41(my_id), 2000);
    Timer_AggmInit(L_P1__GetMainc42(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc42_ID);
    Timer_Init(L_P1__GetMainc42(my_id), 1000);
    Timer_AggmInit(L_P1__GetMainc43(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc43_ID);
    Timer_Init(L_P1__GetMainc43(my_id), 3452000);
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
    L_P1__SetMainc19(my_id, L_P1__GetMainc18(my_id));
    L_P1__SetMainc21(my_id, L_P1__GetMainc20(my_id));
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
    Timer_Exec(L_P1__GetMainc35(my_id));
    Timer_Exec(L_P1__GetMainc36(my_id));
    Timer_Exec(L_P1__GetMainc37(my_id));
    Timer_Exec(L_P1__GetMainc38(my_id));
    Timer_Exec(L_P1__GetMainc39(my_id));
    Timer_Exec(L_P1__GetMainc40(my_id));
    Timer_Exec(L_P1__GetMainc41(my_id));
    Timer_Exec(L_P1__GetMainc42(my_id));
    Timer_Exec(L_P1__GetMainc43(my_id));
}

void L_P1_C1_GSetSafe(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C1(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C1(proc_id);
    L_P1__SetOutMainc(my_id, rossogiallo2);
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
}

// ********** Definizione macro **********

// Macro di effetto

/*
    CNL corrispondente:
    
    { commento: {38,}  se il contatore MainClass_C1_contatore_Co5 è  diverso da  commento: {56,} 15145, commento: {72,}Azzera il contatore MainClass_C1_contatore_Co5
    
     ,altrimenti  commento: {72,}Azzera il contatore MainClass_C1_contatore_Co5
    
    
     commento: {34,}  se il parametro MainClass_C1_parametro_P8 non è  minore di  commento: {55,} 6 commento: {36,} o  se il timer MainClass_C1_timer_T5 è scaduto, commento: {66,} Assegna al comando MainClass_C1_comando_C5 il valore RossoGialloxVerdex
    
       
     commento: {37,}  se la variabile MainClass_C1_variabile_V5 non è  uguale a RossoGialloxVerdex o  se il controllo ConsDef  è  uguale a FALSE , commento: {69,}Disattiva il timer MainClass_C1_timer_T10
    
     ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V5 il valore RossoGialloxVerdex
    
    
     commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  diverso da  commento: {56,} 3 commento: {35,} o  se il controllo MainClass_C1_controllo_C3 non è  uguale a  False  commento: {35,} o  se il controllo MainClass_C1_controllo_C6 è  uguale a  False , commento: {67,} Assegna alla variabile MainClass_C1_variabile_V5 il valore RossoGialloxVerdex
    
       
    
    }
*/
void L_P1__Macro(instance_id_t const my_id )
{
//  *38,*  se il contatore MainClass_C1_contatore_Co5 è  diverso da  *56,* 15145, *72,*Azzera il contatore MainClass_C1_contatore_Co5
    // ,altrimenti  *72,*Azzera il contatore MainClass_C1_contatore_Co5
    bool res_NotLogicOP_0 = true;
    res_NotLogicOP_0 = (res_NotLogicOP_0 && ! (Counter_GetValore(L_P1__GetMainc44(my_id)) == 15145u));
    if(res_NotLogicOP_0){
    
    Counter_Res(L_P1__GetMainc44(my_id));
    }else{
    
    Counter_Res(L_P1__GetMainc44(my_id));
    }
    //  *34,*  se il parametro MainClass_C1_parametro_P8 non è  minore di  *55,* 6 *36,* o  se il timer MainClass_C1_timer_T5 è scaduto, *66,* Assegna al comando MainClass_C1_comando_C5 il valore RossoGialloxVerdex
    bool res_OrLogicOP_1 = false;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (L_P1__GetParamMainc8(my_id) < 6u));
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_NotLogicOP_2);
    res_OrLogicOP_1 = (res_OrLogicOP_1 || Timer_Scaduto(L_P1__GetMainc42(my_id)));
    
    if(res_OrLogicOP_1){
    
    L_P1__SetOutMainc(my_id,rossogiallo2);
    }
    //  *37,*  se la variabile MainClass_C1_variabile_V5 non è  uguale a RossoGialloxVerdex o  se il controllo ConsDef  è  uguale a FALSE , *69,*Disattiva il timer MainClass_C1_timer_T10
    // ,altrimenti  *67,* Assegna alla variabile MainClass_C1_variabile_V5 il valore RossoGialloxVerdex
    bool res_OrLogicOP_3 = false;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetMainc32(my_id) == rossogiallo2));
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_NotLogicOP_4);
    res_OrLogicOP_3 = (res_OrLogicOP_3 || (L_P1__GetInConsd(my_id) == false));
    
    if(res_OrLogicOP_3){
    
    Timer_Disattiva(L_P1__GetMainc39(my_id));
    }else{
    
    L_P1__SetMainc32(my_id,rossogiallo2);
    }
    //  *109,*  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  diverso da  *56,* 3 *35,* o  se il controllo MainClass_C1_controllo_C3 non è  uguale a  False  *35,* o  se il controllo MainClass_C1_controllo_C6 è  uguale a  False , *67,* Assegna alla variabile MainClass_C1_variabile_V5 il valore RossoGialloxVerdex
    bool res_OrLogicOP_5 = false;
    bool res_OrLogicOP_6 = false;
    bool res_NotLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetMainc23(my_id) == 3u));
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! res_NotLogicOP_8);
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_NotLogicOP_7);
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetInMainc1(my_id) == false));
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_NotLogicOP_9);
    
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_OrLogicOP_6);
    res_OrLogicOP_5 = (res_OrLogicOP_5 || (L_P1__GetInMainc3(my_id) == false));
    
    if(res_OrLogicOP_5){
    
    L_P1__SetMainc32(my_id,rossogiallo2);
    }
}

/*
    CNL corrispondente:
    
    { commento: {36,}  se il timer MainClass_C1_timer_T9 non è disattivo commento: {37,} o  se la variabile MainClass_C1_variabile_V5 non è  uguale a RossoGialloxVerdex commento: {38,} e  se il contatore MainClass_C1_contatore_Co5 non è  uguale a  commento: {53,} 13, commento: {66,} Assegna al comando MainClass_C1_comando_C5 il valore RossoGialloxVerdex
    
     ,altrimenti   commento: {67,} Assegna alla variabile MainClass_C1_variabile_V8 il valore RossoVerde commento: {67,}
    
    
      se la macro  MainClass_C1_macrova_M3 ( con argomento_a7   uguale a RossoGialloVerde ,argomento_a8   uguale a avvio ,argomento_a2   uguale a Verde ,argomento_a5   uguale a RossoGialloVerde  e argomento_a6   uguale a RossoGialloxVerdex )  non  è  diverso da Verde commento: {40,}  commento: {35,} e  se il controllo MainClass_C1_controllo_C3 non è  diverso da  False  commento: {38,} o  se il contatore MainClass_C1_contatore_Co5 è  uguale a  commento: {53,} 1114 o  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} e  se il timer MainClass_C1_timer_T4 non è attivo commento: {38,} o  se il contatore MainClass_C1_contatore_Co5 non è  minore di  commento: {55,} 11520, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V5 il valore RossoGialloxVerdex
    
     ,altrimenti  commento: {71,}Decrementa il contatore MainClass_C1_contatore_Co5
    
    
      se il controllo ConsDef è uguale a FALSE  commento: {34,} e  se il parametro MainClass_C1_parametro_P5 è  maggiore di  commento: {54,} 4, commento: {70,}Incrementa il contatore MainClass_C1_contatore_Co5
    
     ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V5 il valore RossoGialloxVerdex
    
    
    
    }
*/
void L_P1__Macro1(instance_id_t const my_id )
{
//  *36,*  se il timer MainClass_C1_timer_T9 non è disattivo *37,* o  se la variabile MainClass_C1_variabile_V5 non è  uguale a RossoGialloxVerdex *38,* e  se il contatore MainClass_C1_contatore_Co5 non è  uguale a  *53,* 13, *66,* Assegna al comando MainClass_C1_comando_C5 il valore RossoGialloxVerdex
    // ,altrimenti   *67,* Assegna alla variabile MainClass_C1_variabile_V8 il valore RossoVerde
    bool res_OrLogicOP_0 = false;
    bool res_NotLogicOP_1 = true;
    res_NotLogicOP_1 = (res_NotLogicOP_1 && ! Timer_Disattivo(L_P1__GetMainc43(my_id)));
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_1);
    bool res_AndLogicOP_2 = true;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__GetMainc32(my_id) == rossogiallo2));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_3);
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (Counter_GetValore(L_P1__GetMainc44(my_id)) == 13u));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_4);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_2);
    
    if(res_OrLogicOP_0){
    
    L_P1__SetOutMainc(my_id,rossogiallo2);
    }else{
    
    L_P1__SetMainc34(my_id,rossoverde);
    }
    //  *67,*
    //  se la macro  MainClass_C1_macrova_M3 ( con argomento_a7   uguale a RossoGialloVerde ,argomento_a8   uguale a avvio ,argomento_a2   uguale a Verde ,argomento_a5   uguale a RossoGialloVerde  e argomento_a6   uguale a RossoGialloxVerdex )  non  è  diverso da Verde *40,*  *35,* e  se il controllo MainClass_C1_controllo_C3 non è  diverso da  False  *38,* o  se il contatore MainClass_C1_contatore_Co5 è  uguale a  *53,* 1114 o  se il controllo ConsDef  è  uguale a FALSE  *36,* e  se il timer MainClass_C1_timer_T4 non è attivo *38,* o  se il contatore MainClass_C1_contatore_Co5 non è  minore di  *55,* 11520, *67,* Assegna alla variabile MainClass_C1_variabile_V5 il valore RossoGialloxVerdex
    // ,altrimenti  *71,*Decrementa il contatore MainClass_C1_contatore_Co5
    bool res_OrLogicOP_5 = false;
    bool res_OrLogicOP_6 = false;
    bool res_OrLogicOP_7 = false;
    bool res_AndLogicOP_8 = true;
    bool res_NotLogicOP_9 = true;
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__Macro2(my_id,verde,rossogiallo1,rossogiallo2,rossogiallo1,avvio) == verde));
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! res_NotLogicOP_10);
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_9);
    bool res_NotLogicOP_11 = true;
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (L_P1__GetInMainc1(my_id) == false));
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! res_NotLogicOP_12);
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_11);
    
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_AndLogicOP_8);
    res_OrLogicOP_7 = (res_OrLogicOP_7 || (Counter_GetValore(L_P1__GetMainc44(my_id)) == 1114u));
    
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_OrLogicOP_7);
    bool res_AndLogicOP_13 = true;
    res_AndLogicOP_13 = (res_AndLogicOP_13 && (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! Timer_Attivo(L_P1__GetMainc41(my_id)));
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_NotLogicOP_14);
    
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_AndLogicOP_13);
    
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_OrLogicOP_6);
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (Counter_GetValore(L_P1__GetMainc44(my_id)) < 11520u));
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_NotLogicOP_15);
    
    if(res_OrLogicOP_5){
    
    L_P1__SetMainc32(my_id,rossogiallo2);
    }else{
    
    Counter_Decr(L_P1__GetMainc44(my_id));
    }
    //  se il controllo ConsDef è uguale a FALSE  *34,* e  se il parametro MainClass_C1_parametro_P5 è  maggiore di  *54,* 4, *70,*Incrementa il contatore MainClass_C1_contatore_Co5
    // ,altrimenti  *67,* Assegna alla variabile MainClass_C1_variabile_V5 il valore RossoGialloxVerdex
    bool res_AndLogicOP_16 = true;
    res_AndLogicOP_16 = (res_AndLogicOP_16 && (L_P1__GetInConsd(my_id) == false));
    res_AndLogicOP_16 = (res_AndLogicOP_16 && (L_P1__GetParamMainc7(my_id) > 4u));
    
    if(res_AndLogicOP_16){
    
    Counter_Incr(L_P1__GetMainc44(my_id));
    }else{
    
    L_P1__SetMainc32(my_id,rossogiallo2);
    }
}


// Macro di verifica

/*
    CNL corrispondente:
     
    { commento: {62,}  se la macro  MainClass_C1_macrova_M6 ( con argomento_a8   uguale a True ,argomento_a2   uguale a spento ,argomento_a5   uguale a spento ,argomento_a6   uguale a RossoGialloxVerdex ,argomento_a3   uguale a avviox ,argomento_a9   uguale a avviox  e argomento_a1   uguale a avvio )   è  uguale a  False  commento: {40,}  commento: {36,} e  se il timer MainClass_C1_timer_T4 non è scaduto, Almeno una delle seguenti { 
     commento: {62,} commento: {36,}  se il timer MainClass_C1_timer_T4 non è scaduto, Almeno una delle seguenti { 
      se il controllo ConsDef  è  uguale a FALSE , Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
    
    
     } Verifica che   commento: {50,}  commento: {,}  la variabile MainClass_C1_variabile_V4 sia  diverso da  False 
    
    
     } Verifica che   commento: {47,48,}  commento: {34,}  il parametro MainClass_C1_parametro_P8 non sia  uguale a  commento: {53,} 8
     commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C8 non sia  diverso da RossoGialloxVerdex
     commento: {104,} o  che  commento: {35,}  il controllo MainClass_C1_controllo_C6 sia  uguale a  True 
    
    
    }
*/
bool L_P1__Macro4(instance_id_t const my_id )
{
bool res_AndLogicOP_0 = true;
    
    //  *62,*  se la macro  MainClass_C1_macrova_M6 ( con argomento_a8   uguale a True ,argomento_a2   uguale a spento ,argomento_a5   uguale a spento ,argomento_a6   uguale a RossoGialloxVerdex ,argomento_a3   uguale a avviox ,argomento_a9   uguale a avviox  e argomento_a1   uguale a avvio )   è  uguale a  False  *40,*  *36,* e  se il timer MainClass_C1_timer_T4 non è scaduto, Almeno una delle seguenti { 
    //   *62,* *36,*  se il timer MainClass_C1_timer_T4 non è scaduto, Almeno una delle seguenti { 
    //    se il controllo ConsDef  è  uguale a FALSE , Verifica che   *48,*   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* e  che   il controllo ConsDef  sia  uguale a FALSE 
    //   } Verifica che   *50,*  *,*  la variabile MainClass_C1_variabile_V4 sia  diverso da  False 
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_AndLogicOP_2 = true;
    res_AndLogicOP_2 = (res_AndLogicOP_2 && (L_P1__Macro3(my_id,avvio,spento,avviox,spento,rossogiallo2,true,avviox) == false));
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! Timer_Scaduto(L_P1__GetMainc41(my_id)));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_3);
    
    if(res_AndLogicOP_2){
    bool res_OrLogicOP_4 = false;
    bool res_ImpliesLogicOp_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! Timer_Scaduto(L_P1__GetMainc41(my_id)));
    if(res_NotLogicOP_6){
    bool res_ImpliesLogicOp_7 = true;
    if((L_P1__GetInConsd(my_id) == false)){
    bool res_AndLogicOP_8 = true;
    res_AndLogicOP_8 = (res_AndLogicOP_8 && (L_P1__GetInConsd(my_id) == false));
    res_AndLogicOP_8 = (res_AndLogicOP_8 && (L_P1__GetInConsd(my_id) == false));
    
    res_ImpliesLogicOp_7 = (res_ImpliesLogicOp_7 && res_AndLogicOP_8);
    }
    res_ImpliesLogicOp_5 = (res_ImpliesLogicOp_5 && res_ImpliesLogicOp_7);
    }
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_ImpliesLogicOp_5);
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetMainc31(my_id) == false));
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_NotLogicOP_9);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_OrLogicOP_4);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *47,48,*  *34,*  il parametro MainClass_C1_parametro_P8 non sia  uguale a  *53,* 8
    //   *104,* e  che  *,*  il controllo MainClass_C1_controllo_C8 non sia  diverso da RossoGialloxVerdex
    //   *104,* o  che  *35,*  il controllo MainClass_C1_controllo_C6 sia  uguale a  True
    bool res_OrLogicOP_10 = false;
    bool res_AndLogicOP_11 = true;
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (L_P1__GetParamMainc8(my_id) == 8u));
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_NotLogicOP_12);
    bool res_NotLogicOP_13 = true;
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1__GetInMainc4(my_id) == rossogiallo2));
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! res_NotLogicOP_14);
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_NotLogicOP_13);
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_AndLogicOP_11);
    res_OrLogicOP_10 = (res_OrLogicOP_10 || (L_P1__GetInMainc3(my_id) == true));
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_10);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
     
    { commento: {62,} commento: {36,}  se il timer MainClass_C1_timer_T5 è disattivo commento: {36,} o  se il timer MainClass_C1_timer_T5 è scaduto o  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} o  se la variabile MainClass_C1_variabile_V5 non è  uguale a RossoGialloxVerdex commento: {36,} e  se il timer MainClass_C1_timer_T2 è disattivo, Almeno una delle seguenti { 
     commento: {38,}  se il contatore MainClass_C1_contatore_Co5 non è  uguale a  commento: {53,} 152, Verifica che   commento: {47,48,50,}  commento: {,}  la variabile MainClass_C1_variabile_V8 sia  uguale a RossoVerde
     commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P5 non sia  uguale a  commento: {53,} 9
     commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
    
    
     } Verifica che   commento: {47,48,51,}  commento: {34,}  il parametro MainClass_C1_parametro_P8 non sia  maggiore di  commento: {54,} 4
     commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C3 non sia  diverso da  False 
     commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P10 non sia  uguale a RossoGialloxVerdex
     commento: {104,} o  che  commento: {,}  il contatore MainClass_C1_contatore_Co5 non sia  minore di  commento: {55,} 11
    
    
    }
*/
bool L_P1__Macro5(instance_id_t const my_id )
{
bool res_AndLogicOP_0 = true;
    
    //  *62,* *36,*  se il timer MainClass_C1_timer_T5 è disattivo *36,* o  se il timer MainClass_C1_timer_T5 è scaduto o  se il controllo ConsDef  è  uguale a FALSE  *37,* o  se la variabile MainClass_C1_variabile_V5 non è  uguale a RossoGialloxVerdex *36,* e  se il timer MainClass_C1_timer_T2 è disattivo, Almeno una delle seguenti { 
    //   *38,*  se il contatore MainClass_C1_contatore_Co5 non è  uguale a  *53,* 152, Verifica che   *47,48,50,*  *,*  la variabile MainClass_C1_variabile_V8 sia  uguale a RossoVerde
    //   *104,* o  che  *34,*  il parametro MainClass_C1_parametro_P5 non sia  uguale a  *53,* 9
    //   *104,* o  che   il controllo ConsDef  sia  uguale a FALSE 
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_OrLogicOP_4 = false;
    res_OrLogicOP_4 = (res_OrLogicOP_4 || Timer_Disattivo(L_P1__GetMainc42(my_id)));
    res_OrLogicOP_4 = (res_OrLogicOP_4 || Timer_Scaduto(L_P1__GetMainc42(my_id)));
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_OrLogicOP_4);
    res_OrLogicOP_3 = (res_OrLogicOP_3 || (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    bool res_AndLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetMainc32(my_id) == rossogiallo2));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_6);
    res_AndLogicOP_5 = (res_AndLogicOP_5 && Timer_Disattivo(L_P1__GetMainc40(my_id)));
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_5);
    
    if(res_OrLogicOP_2){
    bool res_ImpliesLogicOp_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (Counter_GetValore(L_P1__GetMainc44(my_id)) == 152u));
    if(res_NotLogicOP_8){
    bool res_OrLogicOP_9 = false;
    bool res_OrLogicOP_10 = false;
    res_OrLogicOP_10 = (res_OrLogicOP_10 || (L_P1__GetMainc34(my_id) == rossoverde));
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (L_P1__GetParamMainc7(my_id) == 9u));
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_NotLogicOP_11);
    
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_OrLogicOP_10);
    res_OrLogicOP_9 = (res_OrLogicOP_9 || (L_P1__GetInConsd(my_id) == false));
    
    res_ImpliesLogicOp_7 = (res_ImpliesLogicOp_7 && res_OrLogicOP_9);
    }
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_ImpliesLogicOp_7);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *47,48,51,*  *34,*  il parametro MainClass_C1_parametro_P8 non sia  maggiore di  *54,* 4
    //   *104,* e  che  *,*  il controllo MainClass_C1_controllo_C3 non sia  diverso da  False 
    //   *104,* o  che  *34,*  il parametro MainClass_C1_parametro_P10 non sia  uguale a RossoGialloxVerdex
    //   *104,* o  che  *,*  il contatore MainClass_C1_contatore_Co5 non sia  minore di  *55,* 11
    bool res_OrLogicOP_12 = false;
    bool res_OrLogicOP_13 = false;
    bool res_AndLogicOP_14 = true;
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (L_P1__GetParamMainc8(my_id) > 4u));
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_NotLogicOP_15);
    bool res_NotLogicOP_16 = true;
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! (L_P1__GetInMainc1(my_id) == false));
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! res_NotLogicOP_17);
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_NotLogicOP_16);
    
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_AndLogicOP_14);
    bool res_NotLogicOP_18 = true;
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! (L_P1__GetParamMainc5(my_id) == rossogiallo2));
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_NotLogicOP_18);
    
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_OrLogicOP_13);
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (Counter_GetValore(L_P1__GetMainc44(my_id)) < 11u));
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_NotLogicOP_19);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_12);
    
    
    
    return res_AndLogicOP_0;
}


// Macro valorizzate

/*
    CNL corrispondente:
    
    { commento: {[} commento: {34,}  se lo stato  non è  uguale a  commento: {53,}  state1  commento: {106,} commento: {37,} e  se la variabile MainClass_C1_variabile_V5 è  diverso da RossoGialloxVerdex commento: {36,} o  se il timer MainClass_C1_timer_T10 non è disattivo o  se il ripristino dello stato  non è  uguale a  commento: {53,}  state1  commento: {107,} e  se l'argomento argomento_a7 è  uguale a RossoGialloxVerdex commento: {39,}  , assegna alla macro il valore Verde
    
     commento: {46,} assegna alla macro il valore Verde commento: {],}
    }
*/
C1_Enumerat2 L_P1__Macro2(instance_id_t const my_id , C1_Enumerat2 argom2, C1_Enumerat1 argom3, C1_Enumerat1 argom4, C1_Enumerat1 argom5, C1_Enumerat2 argom6)
{
C1_Enumerat2 res_macro_val;
    
    //  *[* *34,*  se lo stato  non è  uguale a  *53,*  state1  *106,* *37,* e  se la variabile MainClass_C1_variabile_V5 è  diverso da RossoGialloxVerdex *36,* o  se il timer MainClass_C1_timer_T10 non è disattivo o  se il ripristino dello stato  non è  uguale a  *53,*  state1  *107,* e  se l'argomento argomento_a7 è  uguale a RossoGialloxVerdex
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_AndLogicOP_2 = true;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1_C1_GetState(my_id) == C1_St_state));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_3);
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetMainc32(my_id) == rossogiallo2));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_4);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_2);
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! Timer_Disattivo(L_P1__GetMainc39(my_id)));
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_NotLogicOP_5);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_AndLogicOP_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetStato1(my_id) == C1_St_state));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_7);
    res_AndLogicOP_6 = (res_AndLogicOP_6 && (argom5 == rossogiallo2));
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_6);
    
    if(res_OrLogicOP_0){
    
    res_macro_val = verde;
    }
    else{
    res_macro_val = verde;
    }
    return res_macro_val;
}

/*
    CNL corrispondente:
    
    { commento: {[} commento: {36,}  se il timer MainClass_C1_timer_T4 non è scaduto commento: {34,} e  se il parametro MainClass_C1_parametro_P8 non è  diverso da  commento: {56,} 4  commento: {34,} e  se il parametro MainClass_C1_parametro_P8 non è  maggiore di  commento: {54,} 6 commento: {35,} e  se il controllo MainClass_C1_controllo_C8 non è  uguale a RossoGialloxVerdex , assegna alla macro il valore  True 
    
     commento: {46,} assegna alla macro il valore  False  commento: {],}
    }
*/
bool L_P1__Macro3(instance_id_t const my_id , C1_Enumerat2 argom7, C1_Enumerat3 argom8, C1_Enumerat4 argom9, C1_Enumerat3 argom10, C1_Enumerat1 argom11, bool argom12, C1_Enumerat4 argom13)
{
bool res_macro_val;
    
    //  *[* *36,*  se il timer MainClass_C1_timer_T4 non è scaduto *34,* e  se il parametro MainClass_C1_parametro_P8 non è  diverso da  *56,* 4  *34,* e  se il parametro MainClass_C1_parametro_P8 non è  maggiore di  *54,* 6 *35,* e  se il controllo MainClass_C1_controllo_C8 non è  uguale a RossoGialloxVerdex
    bool res_AndLogicOP_0 = true;
    bool res_AndLogicOP_1 = true;
    bool res_AndLogicOP_2 = true;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! Timer_Scaduto(L_P1__GetMainc41(my_id)));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_3);
    bool res_NotLogicOP_4 = true;
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetParamMainc8(my_id) == 4u));
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! res_NotLogicOP_5);
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_4);
    
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_AndLogicOP_2);
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetParamMainc8(my_id) > 6u));
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_6);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_AndLogicOP_1);
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetInMainc4(my_id) == rossogiallo2));
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_NotLogicOP_7);
    
    if(res_AndLogicOP_0){
    
    res_macro_val = true;
    }
    else{
    res_macro_val = false;
    }
    return res_macro_val;
}



