// Codice del modello 'TestCase20', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
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
    
     commento: {36,}  se il timer MainClass_C1_timer_T1 non è attivo commento: {38,} e  se il contatore MainClass_C1_contatore_Co10 è  minore di  commento: {55,} 14 commento: {35,} e  se il controllo MainClass_C1_controllo_C10 è  diverso da  False , commento: {66,} Assegna al comando MainClass_C1_comando_C10 il valore c180x
    
       
      se il controllo ConsDef è uguale a FALSE  commento: {35,} e  se il controllo MainClass_C1_controllo_C10 non è  diverso da  False  commento: {34,} o  se il parametro MainClass_C1_parametro_P9 è  maggiore di  commento: {54,} 1 commento: {38,} o  se il contatore MainClass_C1_contatore_Co1 non è  minore di  commento: {55,} 144, commento: {66,} Assegna al comando MainClass_C1_comando_C10 il valore c180x
    
       
     commento: {34,}  se il parametro MainClass_C1_parametro_P10 non è  uguale a  False ,  Applica gli effetti
           della macro MainClass_C1_macroef_M10  commento: {73,}
    
       
    
    }
*/
static inline void L_P1__Effec1(instance_id_t const my_id)
{
    
    //  *36,*  se il timer MainClass_C1_timer_T1 non è attivo *38,* e  se il contatore MainClass_C1_contatore_Co10 è  minore di  *55,* 14 *35,* e  se il controllo MainClass_C1_controllo_C10 è  diverso da  False , *66,* Assegna al comando MainClass_C1_comando_C10 il valore c180x
    bool res_AndLogicOP_0 = true;
    bool res_AndLogicOP_1 = true;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! Timer_Attivo(L_P1__GetMainc46(my_id)));
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_2);
    res_AndLogicOP_1 = (res_AndLogicOP_1 && (Counter_GetValore(L_P1__GetMainc50(my_id)) < 14u));
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_AndLogicOP_1);
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__GetInMainc3(my_id) == false));
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_NotLogicOP_3);
    
    if(res_AndLogicOP_0){
    
    L_P1__SetOutMainc1(my_id,c180x);
    }
    
    //  se il controllo ConsDef è uguale a FALSE  *35,* e  se il controllo MainClass_C1_controllo_C10 non è  diverso da  False  *34,* o  se il parametro MainClass_C1_parametro_P9 è  maggiore di  *54,* 1 *38,* o  se il contatore MainClass_C1_contatore_Co1 non è  minore di  *55,* 144, *66,* Assegna al comando MainClass_C1_comando_C10 il valore c180x
    bool res_OrLogicOP_4 = false;
    bool res_OrLogicOP_5 = false;
    bool res_AndLogicOP_6 = true;
    res_AndLogicOP_6 = (res_AndLogicOP_6 && (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetInMainc3(my_id) == false));
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! res_NotLogicOP_8);
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_7);
    
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_AndLogicOP_6);
    res_OrLogicOP_5 = (res_OrLogicOP_5 || (L_P1__GetParamMainc9(my_id) > 1u));
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_OrLogicOP_5);
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (Counter_GetValore(L_P1__GetMainc49(my_id)) < 144u));
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_NotLogicOP_9);
    
    if(res_OrLogicOP_4){
    
    L_P1__SetOutMainc1(my_id,c180x);
    }
    
    //  *34,*  se il parametro MainClass_C1_parametro_P10 non è  uguale a  False ,  Applica gli effetti
    //         della macro MainClass_C1_macroef_M10
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__GetParamMainc8(my_id) == false));
    if(res_NotLogicOP_10){
    
    L_P1__Macro(my_id);
    }
}



// ********** Definizione metodi **********

// Metodi standard

void L_P1_C1_Init(instance_id_t const my_id)
{
    // init variabili di stato
    L_P1__SetMainc20(my_id, 0);
    L_P1__SetMainc22(my_id, avanzamento);
    L_P1__SetMainc24(my_id, c180);
    L_P1__SetMainc26(my_id, spento);
    L_P1__SetMainc28(my_id, 0);
    L_P1__SetMainc30(my_id, false);
    L_P1__SetMainc31(my_id, false);
    L_P1__SetMainc32(my_id, false);
    L_P1__SetMainc33(my_id, c180);
    L_P1__SetMainc34(my_id, 0);
    L_P1__SetMainc35(my_id, false);
    L_P1__SetStato1(my_id, C1_St_Stato);
    // init controlli precedenti
    L_P1__SetMainc11(my_id, true);
    L_P1__SetMainc13(my_id, false);
    L_P1__SetMainc15(my_id, true);
    L_P1__SetMainc17(my_id, rossogiallo);
    L_P1__SetMainc19(my_id, true);
    // init Timer e Counter
    Timer_AggmInit(L_P1__GetMainc36(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc36_ID);
    Timer_Init(L_P1__GetMainc36(my_id), 431000);
    Timer_AggmInit(L_P1__GetMainc37(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc37_ID);
    Timer_Init(L_P1__GetMainc37(my_id), 431000);
    Timer_AggmInit(L_P1__GetMainc38(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc38_ID);
    Timer_Init(L_P1__GetMainc38(my_id), 4000);
    Timer_AggmInit(L_P1__GetMainc39(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc39_ID);
    Timer_Init(L_P1__GetMainc39(my_id), 4000);
    Timer_AggmInit(L_P1__GetMainc40(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc40_ID);
    Timer_Init(L_P1__GetMainc40(my_id), 420000);
    Timer_AggmInit(L_P1__GetMainc41(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc41_ID);
    Timer_Init(L_P1__GetMainc41(my_id), 420000);
    Timer_AggmInit(L_P1__GetMainc42(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc42_ID);
    Timer_Init(L_P1__GetMainc42(my_id), 4000);
    Timer_AggmInit(L_P1__GetMainc43(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc43_ID);
    Timer_Init(L_P1__GetMainc43(my_id), 4000);
    Timer_AggmInit(L_P1__GetMainc44(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc44_ID);
    Timer_Init(L_P1__GetMainc44(my_id), 1000);
    Timer_AggmInit(L_P1__GetMainc45(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc45_ID);
    Timer_Init(L_P1__GetMainc45(my_id), 1000);
    Timer_AggmInit(L_P1__GetMainc46(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc46_ID);
    Timer_Init(L_P1__GetMainc46(my_id), 2054000);
    Timer_AggmInit(L_P1__GetMainc47(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc47_ID);
    Timer_Init(L_P1__GetMainc47(my_id), 42054000);
    Timer_AggmInit(L_P1__GetMainc48(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc48_ID);
    Timer_Init(L_P1__GetMainc48(my_id), 131000);
    Counter_AggmInit(L_P1__GetMainc49(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc49_ID);
    Counter_Init(L_P1__GetMainc49(my_id));
    Counter_AggmInit(L_P1__GetMainc50(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc50_ID);
    Counter_Init(L_P1__GetMainc50(my_id));
    Counter_AggmInit(L_P1__GetMainc51(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc51_ID);
    Counter_Init(L_P1__GetMainc51(my_id));
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
    L_P1__SetMainc25(my_id, L_P1__GetMainc24(my_id));
    L_P1__SetMainc27(my_id, L_P1__GetMainc26(my_id));
    L_P1__SetMainc29(my_id, L_P1__GetMainc28(my_id));
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
    Timer_Exec(L_P1__GetMainc36(my_id));
    Timer_Exec(L_P1__GetMainc37(my_id));
    Timer_Exec(L_P1__GetMainc38(my_id));
    Timer_Exec(L_P1__GetMainc39(my_id));
    Timer_Exec(L_P1__GetMainc40(my_id));
    Timer_Exec(L_P1__GetMainc41(my_id));
    Timer_Exec(L_P1__GetMainc42(my_id));
    Timer_Exec(L_P1__GetMainc43(my_id));
    Timer_Exec(L_P1__GetMainc44(my_id));
    Timer_Exec(L_P1__GetMainc45(my_id));
    Timer_Exec(L_P1__GetMainc46(my_id));
    Timer_Exec(L_P1__GetMainc47(my_id));
    Timer_Exec(L_P1__GetMainc48(my_id));
}

void L_P1_C1_GSetSafe(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C1(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C1(proc_id);
    L_P1__SetOutMainc(my_id, true);
    L_P1__SetOutMainc1(my_id, c180x);
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
    L_P1__SetMainc25(my_id, L_P1__GetMainc24(my_id));
    L_P1__SetMainc27(my_id, L_P1__GetMainc26(my_id));
    L_P1__SetMainc29(my_id, L_P1__GetMainc28(my_id));
}

// ********** Definizione macro **********

// Macro di effetto

/*
    CNL corrispondente:
    
    { commento: {38,}  se il contatore MainClass_C1_contatore_Co1 è  diverso da  commento: {56,} 15205,  Applica gli effetti
           della macro MainClass_C1_macroef_M7( con argomento_af2   uguale a True ,argomento_af9   uguale a c180 ,argomento_af7   uguale a RossoGiallo ) commento: {73,}
    
     ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V6 il valore  False 
    
    
      se il controllo ConsDef è uguale a FALSE  commento: {37,} o  se la variabile MainClass_C1_variabile_V5 non è  maggiore di  commento: {54,} 1 commento: {34,} e  se il parametro MainClass_C1_parametro_P10 è  uguale a  False , commento: {67,} Assegna alla variabile MainClass_C1_variabile_V4 il valore RossoGiallo
    
     ,altrimenti  commento: {66,} Assegna al comando MainClass_C1_comando_C1 il valore  True 
    
    
      se il controllo ConsDef è uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} o  se il parametro MainClass_C1_parametro_P10 è  diverso da  False , commento: {69,}Disattiva il timer MainClass_C1_timer_T6
    
       
     commento: {34,}  se il parametro MainClass_C1_parametro_P1 è  diverso da  commento: {56,} 3, commento: {68,}Attiva il timer MainClass_C1_timer_T1
    
       
    
    }
*/
void L_P1__Macro(instance_id_t const my_id )
{
//  *38,*  se il contatore MainClass_C1_contatore_Co1 è  diverso da  *56,* 15205,  Applica gli effetti
    //       della macro MainClass_C1_macroef_M7( con argomento_af2   uguale a True ,argomento_af9   uguale a c180 ,argomento_af7   uguale a RossoGiallo ) *73,*
    // ,altrimenti  *67,* Assegna alla variabile MainClass_C1_variabile_V6 il valore  False
    bool res_NotLogicOP_0 = true;
    res_NotLogicOP_0 = (res_NotLogicOP_0 && ! (Counter_GetValore(L_P1__GetMainc49(my_id)) == 15205u));
    if(res_NotLogicOP_0){
    
    L_P1__Macro3(my_id,true,rossogiallo,c180);
    }else{
    
    L_P1__SetMainc35(my_id,false);
    }
    //  se il controllo ConsDef è uguale a FALSE  *37,* o  se la variabile MainClass_C1_variabile_V5 non è  maggiore di  *54,* 1 *34,* e  se il parametro MainClass_C1_parametro_P10 è  uguale a  False , *67,* Assegna alla variabile MainClass_C1_variabile_V4 il valore RossoGiallo
    // ,altrimenti  *66,* Assegna al comando MainClass_C1_comando_C1 il valore  True
    bool res_OrLogicOP_1 = false;
    res_OrLogicOP_1 = (res_OrLogicOP_1 || (L_P1__GetInConsd(my_id) == false));
    bool res_AndLogicOP_2 = true;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__GetMainc34(my_id) > 1u));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_3);
    res_AndLogicOP_2 = (res_AndLogicOP_2 && (L_P1__GetParamMainc8(my_id) == false));
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_2);
    
    if(res_OrLogicOP_1){
    
    L_P1__SetMainc33(my_id,rossogiallo);
    }else{
    
    L_P1__SetOutMainc(my_id,true);
    }
    //  se il controllo ConsDef è uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  *34,* o  se il parametro MainClass_C1_parametro_P10 è  diverso da  False , *69,*Disattiva il timer MainClass_C1_timer_T6
    bool res_OrLogicOP_4 = false;
    bool res_AndLogicOP_5 = true;
    res_AndLogicOP_5 = (res_AndLogicOP_5 && (L_P1__GetInConsd(my_id) == false));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_AndLogicOP_5);
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetParamMainc8(my_id) == false));
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_NotLogicOP_6);
    
    if(res_OrLogicOP_4){
    
    Timer_Disattiva(L_P1__GetMainc47(my_id));
    }
    //  *34,*  se il parametro MainClass_C1_parametro_P1 è  diverso da  *56,* 3, *68,*Attiva il timer MainClass_C1_timer_T1
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetParamMainc7(my_id) == 3u));
    if(res_NotLogicOP_7){
    
    Timer_Attiva(L_P1__GetMainc46(my_id));
    }
}

/*
    CNL corrispondente:
    
    { commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI4 è disattivo o  se il controllo ConsDef  è  uguale a FALSE , commento: {67,} Assegna alla variabile MainClass_C1_variabile_V4 il valore RossoGiallo
    
     ,altrimenti   commento: {67,} Assegna alla variabile MainClass_C1_variabile_V6 il valore  False commento: {67,}
    
    
      se il controllo ConsDef è uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} o  se il controllo MainClass_C1_controllo_C10 è  diverso da  False  commento: {37,} e  se la variabile MainClass_C1_variabile_V4 non è  diverso da RossoGiallo commento: {37,} o  se la variabile MainClass_C1_variabile_V5 è  minore di  commento: {55,} 9, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V4 il valore RossoGiallo
    
     ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V5 il valore 9
    
    
    
    }
*/
void L_P1__Macro1(instance_id_t const my_id )
{
//  *110,*  se il ripristino del timer  MainClass_C1_restoreTI_TI4 è disattivo o  se il controllo ConsDef  è  uguale a FALSE , *67,* Assegna alla variabile MainClass_C1_variabile_V4 il valore RossoGiallo
    // ,altrimenti   *67,* Assegna alla variabile MainClass_C1_variabile_V6 il valore  False
    bool res_OrLogicOP_0 = false;
    res_OrLogicOP_0 = (res_OrLogicOP_0 || Timer_Disattivo(L_P1__GetMainc43(my_id)));
    res_OrLogicOP_0 = (res_OrLogicOP_0 || (L_P1__GetInConsd(my_id) == false));
    
    if(res_OrLogicOP_0){
    
    L_P1__SetMainc33(my_id,rossogiallo);
    }else{
    
    L_P1__SetMainc35(my_id,false);
    }
    //  *67,*
    //  se il controllo ConsDef è uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  *35,* o  se il controllo MainClass_C1_controllo_C10 è  diverso da  False  *37,* e  se la variabile MainClass_C1_variabile_V4 non è  diverso da RossoGiallo *37,* o  se la variabile MainClass_C1_variabile_V5 è  minore di  *55,* 9, *67,* Assegna alla variabile MainClass_C1_variabile_V4 il valore RossoGiallo
    // ,altrimenti  *67,* Assegna alla variabile MainClass_C1_variabile_V5 il valore 9
    bool res_OrLogicOP_1 = false;
    bool res_OrLogicOP_2 = false;
    bool res_AndLogicOP_3 = true;
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (L_P1__GetInConsd(my_id) == false));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_3);
    bool res_AndLogicOP_4 = true;
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetInMainc3(my_id) == false));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_5);
    bool res_NotLogicOP_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetMainc33(my_id) == rossogiallo));
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! res_NotLogicOP_7);
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_6);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_4);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_OrLogicOP_2);
    res_OrLogicOP_1 = (res_OrLogicOP_1 || (L_P1__GetMainc34(my_id) < 9u));
    
    if(res_OrLogicOP_1){
    
    L_P1__SetMainc33(my_id,rossogiallo);
    }else{
    
    L_P1__SetMainc34(my_id,9u);
    }
}

/*
    CNL corrispondente:
    
    {  se il controllo ConsDef  è  uguale a FALSE ,  Applica gli effetti
           della macro MainClass_C1_macroef_M8   commento: {73,}
    
     ,altrimenti  commento: {69,}Disattiva il timer MainClass_C1_timer_T1
    
    
      se il controllo ConsDef è uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} e  se il contatore MainClass_C1_contatore_Co2 è  uguale a  commento: {53,} 13 e  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} o  se il timer MainClass_C1_timer_T1 è attivo commento: {38,} e  se il contatore MainClass_C1_contatore_Co2 non è  maggiore di  commento: {54,} 133, commento: {68,}Attiva il timer MainClass_C1_timer_T7
    
       
     commento: {36,}  se il timer MainClass_C1_timer_T6 è scaduto commento: {36,} e  se il timer MainClass_C1_timer_T1 non è scaduto commento: {34,} e  se il parametro MainClass_C1_parametro_P1 non è  minore di  commento: {55,} 10 commento: {38,} e  se il contatore MainClass_C1_contatore_Co2 è  maggiore di  commento: {54,} 151 commento: {36,} e  se il timer MainClass_C1_timer_T6 non è disattivo, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V5 il valore 3
    
     ,altrimenti  commento: {68,}Attiva il timer MainClass_C1_timer_T7
    
    
    
    }
*/
void L_P1__Macro2(instance_id_t const my_id )
{
//  se il controllo ConsDef  è  uguale a FALSE ,  Applica gli effetti
    //       della macro MainClass_C1_macroef_M8   *73,*
    // ,altrimenti  *69,*Disattiva il timer MainClass_C1_timer_T1
    if((L_P1__GetInConsd(my_id) == false)){
    
    L_P1__Macro4(my_id);
    }else{
    
    Timer_Disattiva(L_P1__GetMainc46(my_id));
    }
    //  se il controllo ConsDef è uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  *38,* e  se il contatore MainClass_C1_contatore_Co2 è  uguale a  *53,* 13 e  se il controllo ConsDef  è  uguale a FALSE  *36,* o  se il timer MainClass_C1_timer_T1 è attivo *38,* e  se il contatore MainClass_C1_contatore_Co2 non è  maggiore di  *54,* 133, *68,*Attiva il timer MainClass_C1_timer_T7
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    res_OrLogicOP_1 = (res_OrLogicOP_1 || (L_P1__GetInConsd(my_id) == false));
    bool res_AndLogicOP_2 = true;
    bool res_AndLogicOP_3 = true;
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (L_P1__GetInConsd(my_id) == false));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (Counter_GetValore(L_P1__GetMainc51(my_id)) == 13u));
    
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_AndLogicOP_3);
    res_AndLogicOP_2 = (res_AndLogicOP_2 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_2);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_AndLogicOP_4 = true;
    res_AndLogicOP_4 = (res_AndLogicOP_4 && Timer_Attivo(L_P1__GetMainc46(my_id)));
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (Counter_GetValore(L_P1__GetMainc51(my_id)) > 133u));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_5);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_4);
    
    if(res_OrLogicOP_0){
    
    Timer_Attiva(L_P1__GetMainc48(my_id));
    }
    //  *36,*  se il timer MainClass_C1_timer_T6 è scaduto *36,* e  se il timer MainClass_C1_timer_T1 non è scaduto *34,* e  se il parametro MainClass_C1_parametro_P1 non è  minore di  *55,* 10 *38,* e  se il contatore MainClass_C1_contatore_Co2 è  maggiore di  *54,* 151 *36,* e  se il timer MainClass_C1_timer_T6 non è disattivo, *67,* Assegna alla variabile MainClass_C1_variabile_V5 il valore 3
    // ,altrimenti  *68,*Attiva il timer MainClass_C1_timer_T7
    bool res_AndLogicOP_6 = true;
    bool res_AndLogicOP_7 = true;
    bool res_AndLogicOP_8 = true;
    bool res_AndLogicOP_9 = true;
    res_AndLogicOP_9 = (res_AndLogicOP_9 && Timer_Scaduto(L_P1__GetMainc47(my_id)));
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! Timer_Scaduto(L_P1__GetMainc46(my_id)));
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_NotLogicOP_10);
    
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_AndLogicOP_9);
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (L_P1__GetParamMainc7(my_id) < 10u));
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_11);
    
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_AndLogicOP_8);
    res_AndLogicOP_7 = (res_AndLogicOP_7 && (Counter_GetValore(L_P1__GetMainc51(my_id)) > 151u));
    
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_AndLogicOP_7);
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! Timer_Disattivo(L_P1__GetMainc47(my_id)));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_12);
    
    if(res_AndLogicOP_6){
    
    L_P1__SetMainc34(my_id,3u);
    }else{
    
    Timer_Attiva(L_P1__GetMainc48(my_id));
    }
}

/*
    CNL corrispondente:
    
    {  se il ripristino dello stato  è  diverso da  commento: {56,}  state1  commento: {107,} o  se l'argomento argomento_af2 è  uguale a  False  commento: {39,}  e  se l'argomento argomento_af2 non  è  uguale a  False  commento: {39,} , commento: {66,} Assegna al comando MainClass_C1_comando_C10 il valore c180x
    
       
    
    }
*/
void L_P1__Macro3(instance_id_t const my_id , bool argom, C1_Enumerat3 argom1, C1_Enumerat3 argom2)
{
//  se il ripristino dello stato  è  diverso da  *56,*  state1  *107,* o  se l'argomento argomento_af2 è  uguale a  False  *39,*  e  se l'argomento argomento_af2 non  è  uguale a  False  *39,* , *66,* Assegna al comando MainClass_C1_comando_C10 il valore c180x
    bool res_OrLogicOP_0 = false;
    bool res_NotLogicOP_1 = true;
    res_NotLogicOP_1 = (res_NotLogicOP_1 && ! (L_P1__GetStato1(my_id) == C1_St_state));
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_1);
    bool res_AndLogicOP_2 = true;
    res_AndLogicOP_2 = (res_AndLogicOP_2 && (argom == false));
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (argom == false));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_3);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_2);
    
    if(res_OrLogicOP_0){
    
    L_P1__SetOutMainc1(my_id,c180x);
    }
}

/*
    CNL corrispondente:
     
    { commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  diverso da  True  commento: {37,} e  se la variabile MainClass_C1_variabile_V3 non è  uguale a  True , commento: {66,} Assegna al comando MainClass_C1_comando_C10 il valore c180x
    
       
    
    }
*/
void L_P1__Macro4(instance_id_t const my_id )
{
//  *109,*  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  diverso da  True  *37,* e  se la variabile MainClass_C1_variabile_V3 non è  uguale a  True , *66,* Assegna al comando MainClass_C1_comando_C10 il valore c180x
    bool res_AndLogicOP_0 = true;
    bool res_NotLogicOP_1 = true;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (L_P1__GetMainc31(my_id) == true));
    res_NotLogicOP_1 = (res_NotLogicOP_1 && ! res_NotLogicOP_2);
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_NotLogicOP_1);
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__GetMainc32(my_id) == true));
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_NotLogicOP_3);
    
    if(res_AndLogicOP_0){
    
    L_P1__SetOutMainc1(my_id,c180x);
    }
}


// Macro di verifica

/*
    CNL corrispondente:
    
    { commento: {61,} commento: {35,}  se il controllo MainClass_C1_controllo_C1 è  uguale a RossoGiallo, Tutte le seguenti { 
     commento: {63,} commento: {36,}  se il timer MainClass_C1_timer_T7 non è disattivo, Solo una delle seguenti { 
     commento: {61,} commento: {37,}  se la variabile MainClass_C1_variabile_V5 non è  uguale a  commento: {53,} 7 commento: {38,} o  se il contatore MainClass_C1_contatore_Co1 non è  diverso da  commento: {56,} 12431 commento: {38,} o  se il contatore MainClass_C1_contatore_Co10 non è  maggiore di  commento: {54,} 132 commento: {35,} e  se il controllo MainClass_C1_controllo_C1 è  diverso da RossoGiallo commento: {34,} e  se il parametro MainClass_C1_parametro_P1 non è  maggiore di  commento: {54,} 3, Tutte le seguenti { 
     commento: {63,}  se la macro  MainClass_C1_macrova_M8 ( con argomento_a6   uguale a True ,argomento_a10   uguale a c180x ,argomento_a5   uguale a avanzamento ,argomento_a8   uguale a Verde ,argomento_a4   uguale a spento ,argomento_a2   uguale a Verde  e argomento_a9   uguale a c120 )   è  uguale a  True  commento: {40,}  commento: {36,} o  se il timer MainClass_C1_timer_T6 non è attivo commento: {37,} o  se la variabile MainClass_C1_variabile_V5 è  diverso da  commento: {56,} 10 o  se l'argomento argomento_ave9 è  diverso da  False  commento: {39,}  o  se l'argomento argomento_ave9 non  è  diverso da  False  commento: {39,}  commento: {36,} o  se il timer MainClass_C1_timer_T1 non è attivo, Solo una delle seguenti { 
     commento: {61,} commento: {37,}  se la variabile MainClass_C1_variabile_V5 è  diverso da  commento: {56,} 4 commento: {35,} e  se il controllo MainClass_C1_controllo_C7 non è  uguale a  True , Tutte le seguenti { 
     commento: {63,} commento: {34,}  se lo stato  è  uguale a  commento: {53,}  state1  commento: {106,} commento: {37,} e  se la variabile MainClass_C1_variabile_V5 è  diverso da  commento: {56,} 5, Solo una delle seguenti { 
     commento: {61,}  se la macro  MainClass_C1_macrova_M8 ( con argomento_a6   uguale a True ,argomento_a10   uguale a avanzamento ,argomento_a5   uguale a c180x ,argomento_a8   uguale a spento ,argomento_a4   uguale a spento ,argomento_a2   uguale a spento  e argomento_a9   uguale a c120 )  non  è  uguale a  False  commento: {40,}  commento: {36,} o  se il timer MainClass_C1_timer_T6 non è disattivo, Tutte le seguenti { 
     commento: {63,}  se il ripristino dello stato  non è  diverso da  commento: {56,}  state1  commento: {107,} commento: {34,} o  se il parametro MainClass_C1_parametro_P9 non è  maggiore di  commento: {54,} 3 commento: {38,} e  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  commento: {56,} 12 commento: {35,} o  se il controllo MainClass_C1_controllo_C10 non è  diverso da  True , Solo una delle seguenti { 
     commento: {61,}  se il ripristino dello stato  non è  diverso da  commento: {56,}  state1  commento: {107,}, Tutte le seguenti { 
     commento: {61,} commento: {34,}  se il parametro MainClass_C1_parametro_P1 è  minore di  commento: {55,} 5 o  se l'argomento argomento_ave3 è  uguale a RossoGiallo commento: {39,}  commento: {37,} o  se la variabile MainClass_C1_variabile_V3 non è  uguale a  False  commento: {37,} o  se la variabile MainClass_C1_variabile_V4 non è  uguale a RossoGiallo, Tutte le seguenti { 
     commento: {61,} commento: {35,}  se il controllo MainClass_C1_controllo_C10 non è  diverso da  False  commento: {37,} e  se la variabile MainClass_C1_variabile_V4 è  diverso da RossoGiallo commento: {34,} o  se il parametro MainClass_C1_parametro_P1 non è  maggiore di  commento: {54,} 4 e  se l'argomento argomento_ave7 non  è  diverso da  True  commento: {39,}  commento: {36,} e  se il timer MainClass_C1_timer_T7 non è disattivo, Tutte le seguenti { 
     commento: {63,} commento: {38,}  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  commento: {53,} 135 e  se l'argomento argomento_ave9 non  è  uguale a  True  commento: {39,}  commento: {37,} e  se la variabile MainClass_C1_variabile_V5 non è  diverso da  commento: {56,} 5 commento: {34,} e  se il parametro MainClass_C1_parametro_P10 non è  diverso da  True  commento: {34,} e  se il parametro MainClass_C1_parametro_P1 non è  diverso da  commento: {56,} 9 commento: {37,} e  se la variabile MainClass_C1_variabile_V4 non è  uguale a RossoGiallo, Solo una delle seguenti { 
     commento: {63,}  se il controllo ConsDef è uguale a FALSE  commento: {36,} o  se il timer MainClass_C1_timer_T1 è disattivo commento: {37,} e  se la variabile MainClass_C1_variabile_V4 non è  uguale a RossoGiallo, Solo una delle seguenti { 
     commento: {63,} commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è scaduto commento: {34,} e  se il parametro MainClass_C1_parametro_P1 è  diverso da  commento: {56,} 3, Solo una delle seguenti { 
     commento: {61,} commento: {38,}  se il contatore MainClass_C1_contatore_Co1 è  maggiore di  commento: {54,} 1543, Tutte le seguenti { 
     commento: {63,} commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è scaduto commento: {38,} o  se il contatore MainClass_C1_contatore_Co1 è  uguale a  commento: {53,} 141 commento: {37,} e  se la variabile MainClass_C1_variabile_V3 è  uguale a  True  commento: {34,} o  se il parametro MainClass_C1_parametro_P1 è  uguale a  commento: {53,} 3 commento: {38,} o  se il contatore MainClass_C1_contatore_Co10 è  uguale a  commento: {53,} 1420 commento: {34,} e  se il parametro MainClass_C1_parametro_P9 è  uguale a  commento: {53,} 7, Solo una delle seguenti { 
     commento: {63,} commento: {35,}  se il controllo MainClass_C1_controllo_C1 è  diverso da RossoGiallo e  se l'argomento argomento_ave1 non  è  diverso da  True  commento: {39,}  commento: {38,} o  se il contatore MainClass_C1_contatore_Co2 è  maggiore di  commento: {54,} 13543, Solo una delle seguenti { 
     commento: {61,} commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI2 non è attivo commento: {36,} o  se il timer MainClass_C1_timer_T1 non è scaduto commento: {36,} o  se il timer MainClass_C1_timer_T1 non è disattivo commento: {35,} e  se il controllo MainClass_C1_controllo_C7 è  uguale a  True  commento: {37,} e  se la variabile MainClass_C1_variabile_V4 è  diverso da RossoGiallo commento: {36,} e  se il timer MainClass_C1_timer_T6 è disattivo, Tutte le seguenti { 
     commento: {61,} commento: {34,}  se lo stato  è  uguale a  commento: {53,}  state1  commento: {106,} o  se l'argomento argomento_ave9 non  è  uguale a  True  commento: {39,}  o  se l'argomento argomento_ave1 è  uguale a  True  commento: {39,} , Tutte le seguenti { 
     commento: {61,} commento: {37,}  se la variabile MainClass_C1_variabile_V4 è  uguale a RossoGiallo commento: {35,} o  se il controllo MainClass_C1_controllo_C7 non è  uguale a  True  commento: {34,} o  se il parametro MainClass_C1_parametro_P9 è  uguale a  commento: {53,} 8 commento: {37,} e  se la variabile MainClass_C1_variabile_V4 è  diverso da RossoGiallo commento: {36,} e  se il timer MainClass_C1_timer_T6 è scaduto commento: {36,} o  se il timer MainClass_C1_timer_T6 non è attivo, Tutte le seguenti { 
     commento: {61,}  se la macro  MainClass_C1_macrova_M7 ( con argomento_a7   uguale a True ,argomento_a3   uguale a c180 ,argomento_a1   uguale a c270x ,argomento_a6   uguale a Verde ,argomento_a10   uguale a RossoGiallo  e argomento_a5   uguale a c270x )  non  è  uguale a  True  commento: {40,} , Tutte le seguenti { 
     commento: {63,} commento: {35,}  se il controllo MainClass_C1_controllo_C4 non è  diverso da c180x commento: {37,} o  se la variabile MainClass_C1_variabile_V4 è  diverso da RossoGiallo o  se l'argomento argomento_ave9 è  uguale a  False  commento: {39,}  commento: {37,} o  se la variabile MainClass_C1_variabile_V4 non è  diverso da RossoGiallo, Solo una delle seguenti { 
     commento: {63,}  se l'argomento argomento_ave7 non  è  diverso da  True  commento: {39,}  o  se l'argomento argomento_ave9 è  diverso da  False  commento: {39,}  commento: {34,} o  se il parametro MainClass_C1_parametro_P10 non è  diverso da  True  commento: {38,} o  se il contatore MainClass_C1_contatore_Co2 non è  maggiore di  commento: {54,} 13054, Solo una delle seguenti { 
     commento: {62,} commento: {38,}  se il contatore MainClass_C1_contatore_Co1 è  diverso da  commento: {56,} 12312 commento: {35,} o  se il controllo MainClass_C1_controllo_C1 non è  uguale a RossoGiallo commento: {38,} o  se il contatore MainClass_C1_contatore_Co10 non è  maggiore di  commento: {54,} 1205 commento: {35,} o  se il controllo MainClass_C1_controllo_C1 non è  diverso da RossoGiallo, Almeno una delle seguenti { 
     commento: {34,}  se lo stato  è  uguale a  commento: {53,}  state1  commento: {106,} commento: {36,} o  se il timer MainClass_C1_timer_T6 è disattivo, Verifica che   commento: {48,49,51,52,}   l'argomento argomento_ave7 sia  uguale a  True  commento: {,} 
     commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C7 sia  uguale a  True 
     commento: {104,} o  che   l'argomento argomento_ave9 non  sia  uguale a  False  commento: {39,} 
     commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T6 sia attivo
     commento: {104,} o  che  commento: {36,}  il timer MainClass_C1_timer_T1 non sia attivo
     commento: {104,} o  che  commento: {,}  il contatore MainClass_C1_contatore_Co10 sia  uguale a  commento: {53,} 11
    
    
     } Verifica che   commento: {47,51,52,}   l'argomento argomento_ave7 non  sia  diverso da  False  commento: {,} 
     commento: {104,} e  che   l'argomento argomento_ave10 sia  uguale a c270x commento: {39,} 
     commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P9 sia  uguale a  commento: {53,} 4
     commento: {104,} e  che   l'argomento argomento_ave9 sia  diverso da  True  commento: {39,} 
     commento: {104,} o  che   l'argomento argomento_ave7 non  sia  diverso da  False  commento: {39,} 
     commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co10 non sia  uguale a  commento: {53,} 114
    
    
     } Verifica che   commento: {47,50,}  commento: {,}  la variabile MainClass_C1_variabile_V4 sia  diverso da RossoGiallo
     commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P1 non sia  maggiore di  commento: {54,} 8
     commento: {104,} o  che  commento: {37,}  la variabile MainClass_C1_variabile_V4 non sia  diverso da RossoGiallo
    
    
     } Verifica che   commento: {47,48,50,52,}  commento: {34,}  il parametro MainClass_C1_parametro_P1 sia  uguale a  commento: {53,} 1
     commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V6 sia  uguale a  False 
     commento: {104,} o  che   l'argomento argomento_ave9 sia  diverso da  True  commento: {,} 
     commento: {104,} e  che   l'argomento argomento_ave3 sia  diverso da RossoGiallo commento: {39,} 
     commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C7 sia  uguale a  False 
     commento: {104,} o  che  commento: {37,}  la variabile MainClass_C1_variabile_V4 non sia  uguale a RossoGiallo
    
    
     } Verifica che   commento: {47,49,51,}  commento: {34,}  il parametro MainClass_C1_parametro_P1 non sia  minore di  commento: {55,} 8
     commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T1 sia scaduto
     commento: {104,} o  che  commento: {,}  il contatore MainClass_C1_contatore_Co1 sia  maggiore di  commento: {54,} 1231
    
    
     } Verifica che   commento: {48,51,}  commento: {,}  il contatore MainClass_C1_contatore_Co1 non sia  minore di  commento: {55,} 1320
     commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C7 non sia  uguale a  False 
     commento: {104,} o  che  commento: {38,}  il contatore MainClass_C1_contatore_Co1 sia  maggiore di  commento: {54,} 1554
     commento: {104,} e  che  commento: {35,}  il controllo MainClass_C1_controllo_C1 sia  diverso da RossoGiallo
     commento: {104,} o  che  commento: {35,}  il controllo MainClass_C1_controllo_C10 sia  diverso da  False 
    
    
     } Verifica che   commento: {49,51,52,}  commento: {,}  il timer MainClass_C1_timer_T1 sia disattivo
     commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co2 non sia  diverso da  commento: {56,} 1131
     commento: {104,} e  che  commento: {38,}  il contatore MainClass_C1_contatore_Co1 non sia  maggiore di  commento: {54,} 15
     commento: {104,} o  che   l'argomento argomento_ave9 non  sia  uguale a  False  commento: {,} 
    
    
     } Verifica che   commento: {48,50,51,52,}  commento: {,}  la variabile MainClass_C1_variabile_V4 sia  uguale a RossoGiallo
     commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co2 sia  minore di  commento: {55,} 14
     commento: {104,} o  che   l'argomento argomento_ave9 non  sia  uguale a  False  commento: {,} 
     commento: {104,} e  che   l'argomento argomento_ave1 sia  uguale a  True  commento: {39,} 
     commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C10 non sia  diverso da  True 
     commento: {104,} e  che  commento: {37,}  la variabile MainClass_C1_variabile_V4 non sia  uguale a RossoGiallo
    
    
     } Verifica che   commento: {48,49,50,51,}  commento: {,}  il contatore MainClass_C1_contatore_Co2 sia  maggiore di  commento: {54,} 152054
     commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C7 non sia  uguale a  True 
     commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V5 sia  maggiore di  commento: {54,} 2
     commento: {104,} e  che  commento: {37,}  la variabile MainClass_C1_variabile_V4 non sia  uguale a RossoGiallo
     commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T7 sia scaduto
    
    
     } Verifica che   commento: {52,}   l'argomento argomento_ave9 non  sia  diverso da  True  commento: {,} 
    
    
     } Verifica che   commento: {49,51,}  commento: {,}  il timer MainClass_C1_timer_T7 sia disattivo
     commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co2 non sia  uguale a  commento: {53,} 133
     commento: {104,} o  che  commento: {36,}  il timer MainClass_C1_timer_T7 non sia attivo
    
    
     } Verifica che   commento: {48,49,51,52,}  commento: {,}  il timer MainClass_C1_timer_T1 sia scaduto
     commento: {104,} o  che   l'argomento argomento_ave9 sia  diverso da  True  commento: {,} 
     commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C10 non sia  diverso da  True 
     commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co10 sia  minore di  commento: {55,} 151
    
    
     } Verifica che   commento: {49,}  commento: {,}  il timer MainClass_C1_timer_T7 non sia scaduto
    
    
     } Verifica che   commento: {47,48,51,52,}   l'argomento argomento_ave7 sia  uguale a  True  commento: {,} 
     commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P10 non sia  uguale a  True 
     commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C4 non sia  diverso da c180x
     commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co2 sia  diverso da  commento: {56,} 11205
     commento: {104,} e  che  commento: {35,}  il controllo MainClass_C1_controllo_C8 sia  diverso da c180x
    
    
     } Verifica che   commento: {48,49,50,51,}  commento: {,}  il timer MainClass_C1_timer_T7 non sia attivo
     commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co2 non sia  maggiore di  commento: {54,} 134
     commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V4 non sia  uguale a RossoGiallo
     commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C7 sia  diverso da  False 
     commento: {104,} o  che  commento: {35,}  il controllo MainClass_C1_controllo_C4 sia  uguale a c180x
     commento: {104,} o  che  commento: {36,}  il timer MainClass_C1_timer_T7 sia disattivo
    
    
     } Verifica che   commento: {48,50,51,}  commento: {,}  il controllo MainClass_C1_controllo_C10 sia  diverso da  False 
     commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V4 non sia  uguale a RossoGiallo
     commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co1 non sia  diverso da  commento: {56,} 1131
     commento: {104,} o  che  commento: {35,}  il controllo MainClass_C1_controllo_C10 sia  diverso da  False 
     commento: {104,} o  che  commento: {35,}  il controllo MainClass_C1_controllo_C7 non sia  uguale a  True 
     commento: {104,} e  che  commento: {35,}  il controllo MainClass_C1_controllo_C10 sia  uguale a  False 
    
    
     } Verifica che   commento: {47,48,51,52,}  commento: {,}  il contatore MainClass_C1_contatore_Co10 sia  maggiore di  commento: {54,} 13
     commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P9 sia  maggiore di  commento: {54,} 8
     commento: {104,} o  che   l'argomento argomento_ave9 non  sia  uguale a  True  commento: {,} 
     commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C10 sia  diverso da  False 
    
    
     } Verifica che   commento: {47,48,49,52,}  commento: {34,}  il parametro MainClass_C1_parametro_P10 sia  uguale a  True 
     commento: {104,} o  che   l'argomento argomento_ave7 sia  uguale a  False  commento: {,} 
     commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T6 sia disattivo
     commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C10 non sia  diverso da  True 
     commento: {104,} e  che  commento: {36,}  il timer MainClass_C1_timer_T7 non sia disattivo
     commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P1 sia  diverso da  commento: {56,} 4
    
    
     } Verifica che   commento: {48,}  commento: {,}  il controllo MainClass_C1_controllo_C1 sia  diverso da RossoGiallo
    
    
     } Verifica che   commento: {50,}  commento: {,}  la variabile MainClass_C1_variabile_V4 sia  uguale a RossoGiallo
    
    
     } Verifica che   commento: {47,48,50,52,}  commento: {34,}  il parametro MainClass_C1_parametro_P1 sia  uguale a  commento: {53,} 5
     commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C10 non sia  diverso da  False 
     commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P10 non sia  diverso da  False 
     commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V4 non sia  uguale a RossoGiallo
     commento: {104,} e  che  commento: {37,}  la variabile MainClass_C1_variabile_V3 non sia  diverso da  False 
     commento: {104,} o  che   l'argomento argomento_ave3 sia  uguale a RossoGiallo commento: {,} 
    
    
     } Verifica che   commento: {47,48,50,}  commento: {,}  il controllo MainClass_C1_controllo_C10 sia  diverso da  True 
     commento: {104,} o  che  commento: {35,}  il controllo MainClass_C1_controllo_C10 sia  uguale a  False 
     commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V3 sia  diverso da  True 
     commento: {104,} e  che  commento: {35,}  il controllo MainClass_C1_controllo_C4 non sia  diverso da c180x
     commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P1 non sia  uguale a  commento: {53,} 10
    
    
     } Verifica che   commento: {47,49,51,52,}  commento: {34,}  il parametro MainClass_C1_parametro_P10 sia  diverso da  True 
     commento: {104,} o  che   l'argomento argomento_ave7 sia  uguale a  True  commento: {,} 
     commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T1 non sia attivo
     commento: {104,} o  che  commento: {,}  il contatore MainClass_C1_contatore_Co10 sia  diverso da  commento: {56,} 1520
     commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P1 non sia  uguale a  commento: {53,} 9
     commento: {104,} e  che  commento: {36,}  il timer MainClass_C1_timer_T1 non sia disattivo
    
    
     } Verifica che   commento: {50,}  commento: {,}  la variabile MainClass_C1_variabile_V4 non sia  uguale a RossoGiallo
    
    
     } Verifica che   commento: {47,50,52,}   l'argomento argomento_ave9 non  sia  uguale a  False  commento: {,} 
     commento: {104,} e  che   l'argomento argomento_ave7 non  sia  uguale a  True  commento: {39,} 
     commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P10 non sia  uguale a  False 
     commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V4 non sia  diverso da RossoGiallo
    
    
    }
*/
bool L_P1__Macro8(instance_id_t const my_id , bool argom21, C1_Enumerat4 argom22, C1_Enumerat3 argom23, bool argom24, bool argom25, bool argom26)
{
bool res_AndLogicOP_0 = true;
    
    //  *61,* *35,*  se il controllo MainClass_C1_controllo_C1 è  uguale a RossoGiallo, Tutte le seguenti { 
    //   *63,* *36,*  se il timer MainClass_C1_timer_T7 non è disattivo, Solo una delle seguenti { 
    //   *61,* *37,*  se la variabile MainClass_C1_variabile_V5 non è  uguale a  *53,* 7 *38,* o  se il contatore MainClass_C1_contatore_Co1 non è  diverso da  *56,* 12431 *38,* o  se il contatore MainClass_C1_contatore_Co10 non è  maggiore di  *54,* 132 *35,* e  se il controllo MainClass_C1_controllo_C1 è  diverso da RossoGiallo *34,* e  se il parametro MainClass_C1_parametro_P1 non è  maggiore di  *54,* 3, Tutte le seguenti { 
    //   *63,*  se la macro  MainClass_C1_macrova_M8 ( con argomento_a6   uguale a True ,argomento_a10   uguale a c180x ,argomento_a5   uguale a avanzamento ,argomento_a8   uguale a Verde ,argomento_a4   uguale a spento ,argomento_a2   uguale a Verde  e argomento_a9   uguale a c120 )   è  uguale a  True  *40,*  *36,* o  se il timer MainClass_C1_timer_T6 non è attivo *37,* o  se la variabile MainClass_C1_variabile_V5 è  diverso da  *56,* 10 o  se l'argomento argomento_ave9 è  diverso da  False  *39,*  o  se l'argomento argomento_ave9 non  è  diverso da  False  *39,*  *36,* o  se il timer MainClass_C1_timer_T1 non è attivo, Solo una delle seguenti { 
    //   *61,* *37,*  se la variabile MainClass_C1_variabile_V5 è  diverso da  *56,* 4 *35,* e  se il controllo MainClass_C1_controllo_C7 non è  uguale a  True , Tutte le seguenti { 
    //   *63,* *34,*  se lo stato  è  uguale a  *53,*  state1  *106,* *37,* e  se la variabile MainClass_C1_variabile_V5 è  diverso da  *56,* 5, Solo una delle seguenti { 
    //   *61,*  se la macro  MainClass_C1_macrova_M8 ( con argomento_a6   uguale a True ,argomento_a10   uguale a avanzamento ,argomento_a5   uguale a c180x ,argomento_a8   uguale a spento ,argomento_a4   uguale a spento ,argomento_a2   uguale a spento  e argomento_a9   uguale a c120 )  non  è  uguale a  False  *40,*  *36,* o  se il timer MainClass_C1_timer_T6 non è disattivo, Tutte le seguenti { 
    //   *63,*  se il ripristino dello stato  non è  diverso da  *56,*  state1  *107,* *34,* o  se il parametro MainClass_C1_parametro_P9 non è  maggiore di  *54,* 3 *38,* e  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  *56,* 12 *35,* o  se il controllo MainClass_C1_controllo_C10 non è  diverso da  True , Solo una delle seguenti { 
    //   *61,*  se il ripristino dello stato  non è  diverso da  *56,*  state1  *107,*, Tutte le seguenti { 
    //   *61,* *34,*  se il parametro MainClass_C1_parametro_P1 è  minore di  *55,* 5 o  se l'argomento argomento_ave3 è  uguale a RossoGiallo *39,*  *37,* o  se la variabile MainClass_C1_variabile_V3 non è  uguale a  False  *37,* o  se la variabile MainClass_C1_variabile_V4 non è  uguale a RossoGiallo, Tutte le seguenti { 
    //   *61,* *35,*  se il controllo MainClass_C1_controllo_C10 non è  diverso da  False  *37,* e  se la variabile MainClass_C1_variabile_V4 è  diverso da RossoGiallo *34,* o  se il parametro MainClass_C1_parametro_P1 non è  maggiore di  *54,* 4 e  se l'argomento argomento_ave7 non  è  diverso da  True  *39,*  *36,* e  se il timer MainClass_C1_timer_T7 non è disattivo, Tutte le seguenti { 
    //   *63,* *38,*  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  *53,* 135 e  se l'argomento argomento_ave9 non  è  uguale a  True  *39,*  *37,* e  se la variabile MainClass_C1_variabile_V5 non è  diverso da  *56,* 5 *34,* e  se il parametro MainClass_C1_parametro_P10 non è  diverso da  True  *34,* e  se il parametro MainClass_C1_parametro_P1 non è  diverso da  *56,* 9 *37,* e  se la variabile MainClass_C1_variabile_V4 non è  uguale a RossoGiallo, Solo una delle seguenti { 
    //   *63,*  se il controllo ConsDef è uguale a FALSE  *36,* o  se il timer MainClass_C1_timer_T1 è disattivo *37,* e  se la variabile MainClass_C1_variabile_V4 non è  uguale a RossoGiallo, Solo una delle seguenti { 
    //   *63,* *110,*  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è scaduto *34,* e  se il parametro MainClass_C1_parametro_P1 è  diverso da  *56,* 3, Solo una delle seguenti { 
    //   *61,* *38,*  se il contatore MainClass_C1_contatore_Co1 è  maggiore di  *54,* 1543, Tutte le seguenti { 
    //   *63,* *110,*  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è scaduto *38,* o  se il contatore MainClass_C1_contatore_Co1 è  uguale a  *53,* 141 *37,* e  se la variabile MainClass_C1_variabile_V3 è  uguale a  True  *34,* o  se il parametro MainClass_C1_parametro_P1 è  uguale a  *53,* 3 *38,* o  se il contatore MainClass_C1_contatore_Co10 è  uguale a  *53,* 1420 *34,* e  se il parametro MainClass_C1_parametro_P9 è  uguale a  *53,* 7, Solo una delle seguenti { 
    //   *63,* *35,*  se il controllo MainClass_C1_controllo_C1 è  diverso da RossoGiallo e  se l'argomento argomento_ave1 non  è  diverso da  True  *39,*  *38,* o  se il contatore MainClass_C1_contatore_Co2 è  maggiore di  *54,* 13543, Solo una delle seguenti { 
    //   *61,* *110,*  se il ripristino del timer  MainClass_C1_restoreTI_TI2 non è attivo *36,* o  se il timer MainClass_C1_timer_T1 non è scaduto *36,* o  se il timer MainClass_C1_timer_T1 non è disattivo *35,* e  se il controllo MainClass_C1_controllo_C7 è  uguale a  True  *37,* e  se la variabile MainClass_C1_variabile_V4 è  diverso da RossoGiallo *36,* e  se il timer MainClass_C1_timer_T6 è disattivo, Tutte le seguenti { 
    //   *61,* *34,*  se lo stato  è  uguale a  *53,*  state1  *106,* o  se l'argomento argomento_ave9 non  è  uguale a  True  *39,*  o  se l'argomento argomento_ave1 è  uguale a  True  *39,* , Tutte le seguenti { 
    //   *61,* *37,*  se la variabile MainClass_C1_variabile_V4 è  uguale a RossoGiallo *35,* o  se il controllo MainClass_C1_controllo_C7 non è  uguale a  True  *34,* o  se il parametro MainClass_C1_parametro_P9 è  uguale a  *53,* 8 *37,* e  se la variabile MainClass_C1_variabile_V4 è  diverso da RossoGiallo *36,* e  se il timer MainClass_C1_timer_T6 è scaduto *36,* o  se il timer MainClass_C1_timer_T6 non è attivo, Tutte le seguenti { 
    //   *61,*  se la macro  MainClass_C1_macrova_M7 ( con argomento_a7   uguale a True ,argomento_a3   uguale a c180 ,argomento_a1   uguale a c270x ,argomento_a6   uguale a Verde ,argomento_a10   uguale a RossoGiallo  e argomento_a5   uguale a c270x )  non  è  uguale a  True  *40,* , Tutte le seguenti { 
    //   *63,* *35,*  se il controllo MainClass_C1_controllo_C4 non è  diverso da c180x *37,* o  se la variabile MainClass_C1_variabile_V4 è  diverso da RossoGiallo o  se l'argomento argomento_ave9 è  uguale a  False  *39,*  *37,* o  se la variabile MainClass_C1_variabile_V4 non è  diverso da RossoGiallo, Solo una delle seguenti { 
    //   *63,*  se l'argomento argomento_ave7 non  è  diverso da  True  *39,*  o  se l'argomento argomento_ave9 è  diverso da  False  *39,*  *34,* o  se il parametro MainClass_C1_parametro_P10 non è  diverso da  True  *38,* o  se il contatore MainClass_C1_contatore_Co2 non è  maggiore di  *54,* 13054, Solo una delle seguenti { 
    //   *62,* *38,*  se il contatore MainClass_C1_contatore_Co1 è  diverso da  *56,* 12312 *35,* o  se il controllo MainClass_C1_controllo_C1 non è  uguale a RossoGiallo *38,* o  se il contatore MainClass_C1_contatore_Co10 non è  maggiore di  *54,* 1205 *35,* o  se il controllo MainClass_C1_controllo_C1 non è  diverso da RossoGiallo, Almeno una delle seguenti { 
    //   *34,*  se lo stato  è  uguale a  *53,*  state1  *106,* *36,* o  se il timer MainClass_C1_timer_T6 è disattivo, Verifica che   *48,49,51,52,*   l'argomento argomento_ave7 sia  uguale a  True  *,* 
    //   *104,* e  che  *,*  il controllo MainClass_C1_controllo_C7 sia  uguale a  True 
    //   *104,* o  che   l'argomento argomento_ave9 non  sia  uguale a  False  *39,* 
    //   *104,* o  che  *,*  il timer MainClass_C1_timer_T6 sia attivo
    //   *104,* o  che  *36,*  il timer MainClass_C1_timer_T1 non sia attivo
    //   *104,* o  che  *,*  il contatore MainClass_C1_contatore_Co10 sia  uguale a  *53,* 11
    //   } Verifica che   *47,51,52,*   l'argomento argomento_ave7 non  sia  diverso da  False  *,* 
    //   *104,* e  che   l'argomento argomento_ave10 sia  uguale a c270x *39,* 
    //   *104,* o  che  *34,*  il parametro MainClass_C1_parametro_P9 sia  uguale a  *53,* 4
    //   *104,* e  che   l'argomento argomento_ave9 sia  diverso da  True  *39,* 
    //   *104,* o  che   l'argomento argomento_ave7 non  sia  diverso da  False  *39,* 
    //   *104,* e  che  *,*  il contatore MainClass_C1_contatore_Co10 non sia  uguale a  *53,* 114
    //   } Verifica che   *47,50,*  *,*  la variabile MainClass_C1_variabile_V4 sia  diverso da RossoGiallo
    //   *104,* e  che  *34,*  il parametro MainClass_C1_parametro_P1 non sia  maggiore di  *54,* 8
    //   *104,* o  che  *37,*  la variabile MainClass_C1_variabile_V4 non sia  diverso da RossoGiallo
    //   } Verifica che   *47,48,50,52,*  *34,*  il parametro MainClass_C1_parametro_P1 sia  uguale a  *53,* 1
    //   *104,* e  che  *,*  la variabile MainClass_C1_variabile_V6 sia  uguale a  False 
    //   *104,* o  che   l'argomento argomento_ave9 sia  diverso da  True  *,* 
    //   *104,* e  che   l'argomento argomento_ave3 sia  diverso da RossoGiallo *39,* 
    //   *104,* e  che  *,*  il controllo MainClass_C1_controllo_C7 sia  uguale a  False 
    //   *104,* o  che  *37,*  la variabile MainClass_C1_variabile_V4 non sia  uguale a RossoGiallo
    //   } Verifica che   *47,49,51,*  *34,*  il parametro MainClass_C1_parametro_P1 non sia  minore di  *55,* 8
    //   *104,* e  che  *,*  il timer MainClass_C1_timer_T1 sia scaduto
    //   *104,* o  che  *,*  il contatore MainClass_C1_contatore_Co1 sia  maggiore di  *54,* 1231
    //   } Verifica che   *48,51,*  *,*  il contatore MainClass_C1_contatore_Co1 non sia  minore di  *55,* 1320
    //   *104,* e  che  *,*  il controllo MainClass_C1_controllo_C7 non sia  uguale a  False 
    //   *104,* o  che  *38,*  il contatore MainClass_C1_contatore_Co1 sia  maggiore di  *54,* 1554
    //   *104,* e  che  *35,*  il controllo MainClass_C1_controllo_C1 sia  diverso da RossoGiallo
    //   *104,* o  che  *35,*  il controllo MainClass_C1_controllo_C10 sia  diverso da  False 
    //   } Verifica che   *49,51,52,*  *,*  il timer MainClass_C1_timer_T1 sia disattivo
    //   *104,* e  che  *,*  il contatore MainClass_C1_contatore_Co2 non sia  diverso da  *56,* 1131
    //   *104,* e  che  *38,*  il contatore MainClass_C1_contatore_Co1 non sia  maggiore di  *54,* 15
    //   *104,* o  che   l'argomento argomento_ave9 non  sia  uguale a  False  *,* 
    //   } Verifica che   *48,50,51,52,*  *,*  la variabile MainClass_C1_variabile_V4 sia  uguale a RossoGiallo
    //   *104,* e  che  *,*  il contatore MainClass_C1_contatore_Co2 sia  minore di  *55,* 14
    //   *104,* o  che   l'argomento argomento_ave9 non  sia  uguale a  False  *,* 
    //   *104,* e  che   l'argomento argomento_ave1 sia  uguale a  True  *39,* 
    //   *104,* o  che  *,*  il controllo MainClass_C1_controllo_C10 non sia  diverso da  True 
    //   *104,* e  che  *37,*  la variabile MainClass_C1_variabile_V4 non sia  uguale a RossoGiallo
    //   } Verifica che   *48,49,50,51,*  *,*  il contatore MainClass_C1_contatore_Co2 sia  maggiore di  *54,* 152054
    //   *104,* o  che  *,*  il controllo MainClass_C1_controllo_C7 non sia  uguale a  True 
    //   *104,* e  che  *,*  la variabile MainClass_C1_variabile_V5 sia  maggiore di  *54,* 2
    //   *104,* e  che  *37,*  la variabile MainClass_C1_variabile_V4 non sia  uguale a RossoGiallo
    //   *104,* o  che  *,*  il timer MainClass_C1_timer_T7 sia scaduto
    //   } Verifica che   *52,*   l'argomento argomento_ave9 non  sia  diverso da  True  *,* 
    //   } Verifica che   *49,51,*  *,*  il timer MainClass_C1_timer_T7 sia disattivo
    //   *104,* e  che  *,*  il contatore MainClass_C1_contatore_Co2 non sia  uguale a  *53,* 133
    //   *104,* o  che  *36,*  il timer MainClass_C1_timer_T7 non sia attivo
    //   } Verifica che   *48,49,51,52,*  *,*  il timer MainClass_C1_timer_T1 sia scaduto
    //   *104,* o  che   l'argomento argomento_ave9 sia  diverso da  True  *,* 
    //   *104,* e  che  *,*  il controllo MainClass_C1_controllo_C10 non sia  diverso da  True 
    //   *104,* e  che  *,*  il contatore MainClass_C1_contatore_Co10 sia  minore di  *55,* 151
    //   } Verifica che   *49,*  *,*  il timer MainClass_C1_timer_T7 non sia scaduto
    //   } Verifica che   *47,48,51,52,*   l'argomento argomento_ave7 sia  uguale a  True  *,* 
    //   *104,* o  che  *34,*  il parametro MainClass_C1_parametro_P10 non sia  uguale a  True 
    //   *104,* e  che  *,*  il controllo MainClass_C1_controllo_C4 non sia  diverso da c180x
    //   *104,* e  che  *,*  il contatore MainClass_C1_contatore_Co2 sia  diverso da  *56,* 11205
    //   *104,* e  che  *35,*  il controllo MainClass_C1_controllo_C8 sia  diverso da c180x
    //   } Verifica che   *48,49,50,51,*  *,*  il timer MainClass_C1_timer_T7 non sia attivo
    //   *104,* e  che  *,*  il contatore MainClass_C1_contatore_Co2 non sia  maggiore di  *54,* 134
    //   *104,* e  che  *,*  la variabile MainClass_C1_variabile_V4 non sia  uguale a RossoGiallo
    //   *104,* o  che  *,*  il controllo MainClass_C1_controllo_C7 sia  diverso da  False 
    //   *104,* o  che  *35,*  il controllo MainClass_C1_controllo_C4 sia  uguale a c180x
    //   *104,* o  che  *36,*  il timer MainClass_C1_timer_T7 sia disattivo
    //   } Verifica che   *48,50,51,*  *,*  il controllo MainClass_C1_controllo_C10 sia  diverso da  False 
    //   *104,* e  che  *,*  la variabile MainClass_C1_variabile_V4 non sia  uguale a RossoGiallo
    //   *104,* e  che  *,*  il contatore MainClass_C1_contatore_Co1 non sia  diverso da  *56,* 1131
    //   *104,* o  che  *35,*  il controllo MainClass_C1_controllo_C10 sia  diverso da  False 
    //   *104,* o  che  *35,*  il controllo MainClass_C1_controllo_C7 non sia  uguale a  True 
    //   *104,* e  che  *35,*  il controllo MainClass_C1_controllo_C10 sia  uguale a  False 
    //   } Verifica che   *47,48,51,52,*  *,*  il contatore MainClass_C1_contatore_Co10 sia  maggiore di  *54,* 13
    //   *104,* o  che  *34,*  il parametro MainClass_C1_parametro_P9 sia  maggiore di  *54,* 8
    //   *104,* o  che   l'argomento argomento_ave9 non  sia  uguale a  True  *,* 
    //   *104,* o  che  *,*  il controllo MainClass_C1_controllo_C10 sia  diverso da  False 
    //   } Verifica che   *47,48,49,52,*  *34,*  il parametro MainClass_C1_parametro_P10 sia  uguale a  True 
    //   *104,* o  che   l'argomento argomento_ave7 sia  uguale a  False  *,* 
    //   *104,* o  che  *,*  il timer MainClass_C1_timer_T6 sia disattivo
    //   *104,* e  che  *,*  il controllo MainClass_C1_controllo_C10 non sia  diverso da  True 
    //   *104,* e  che  *36,*  il timer MainClass_C1_timer_T7 non sia disattivo
    //   *104,* e  che  *34,*  il parametro MainClass_C1_parametro_P1 sia  diverso da  *56,* 4
    //   } Verifica che   *48,*  *,*  il controllo MainClass_C1_controllo_C1 sia  diverso da RossoGiallo
    //   } Verifica che   *50,*  *,*  la variabile MainClass_C1_variabile_V4 sia  uguale a RossoGiallo
    //   } Verifica che   *47,48,50,52,*  *34,*  il parametro MainClass_C1_parametro_P1 sia  uguale a  *53,* 5
    //   *104,* o  che  *,*  il controllo MainClass_C1_controllo_C10 non sia  diverso da  False 
    //   *104,* o  che  *34,*  il parametro MainClass_C1_parametro_P10 non sia  diverso da  False 
    //   *104,* e  che  *,*  la variabile MainClass_C1_variabile_V4 non sia  uguale a RossoGiallo
    //   *104,* e  che  *37,*  la variabile MainClass_C1_variabile_V3 non sia  diverso da  False 
    //   *104,* o  che   l'argomento argomento_ave3 sia  uguale a RossoGiallo *,* 
    //   } Verifica che   *47,48,50,*  *,*  il controllo MainClass_C1_controllo_C10 sia  diverso da  True 
    //   *104,* o  che  *35,*  il controllo MainClass_C1_controllo_C10 sia  uguale a  False 
    //   *104,* o  che  *,*  la variabile MainClass_C1_variabile_V3 sia  diverso da  True 
    //   *104,* e  che  *35,*  il controllo MainClass_C1_controllo_C4 non sia  diverso da c180x
    //   *104,* e  che  *34,*  il parametro MainClass_C1_parametro_P1 non sia  uguale a  *53,* 10
    //   } Verifica che   *47,49,51,52,*  *34,*  il parametro MainClass_C1_parametro_P10 sia  diverso da  True 
    //   *104,* o  che   l'argomento argomento_ave7 sia  uguale a  True  *,* 
    //   *104,* o  che  *,*  il timer MainClass_C1_timer_T1 non sia attivo
    //   *104,* o  che  *,*  il contatore MainClass_C1_contatore_Co10 sia  diverso da  *56,* 1520
    //   *104,* o  che  *34,*  il parametro MainClass_C1_parametro_P1 non sia  uguale a  *53,* 9
    //   *104,* e  che  *36,*  il timer MainClass_C1_timer_T1 non sia disattivo
    //   } Verifica che   *50,*  *,*  la variabile MainClass_C1_variabile_V4 non sia  uguale a RossoGiallo
    //   }
    bool res_ImpliesLogicOp_1 = true;
    if((L_P1__GetInMainc2(my_id) == rossogiallo)){
    bool res_AndLogicOP_2 = true;
    bool res_ImpliesLogicOp_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! Timer_Disattivo(L_P1__GetMainc48(my_id)));
    if(res_NotLogicOP_4){
    bool res_XorLogicOP_5 = true;
    int xorIndex_res_XorLogicOP_5 = 0;
    bool res_ImpliesLogicOp_6 = true;
    bool res_OrLogicOP_7 = false;
    bool res_OrLogicOP_8 = false;
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetMainc34(my_id) == 7u));
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_NotLogicOP_9);
    bool res_NotLogicOP_10 = true;
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (Counter_GetValore(L_P1__GetMainc49(my_id)) == 12431u));
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! res_NotLogicOP_11);
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_NotLogicOP_10);
    
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_OrLogicOP_8);
    bool res_AndLogicOP_12 = true;
    bool res_AndLogicOP_13 = true;
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (Counter_GetValore(L_P1__GetMainc50(my_id)) > 132u));
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_NotLogicOP_14);
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (L_P1__GetInMainc2(my_id) == rossogiallo));
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_NotLogicOP_15);
    
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_AndLogicOP_13);
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (L_P1__GetParamMainc7(my_id) > 3u));
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_NotLogicOP_16);
    
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_AndLogicOP_12);
    
    if(res_OrLogicOP_7){
    bool res_AndLogicOP_17 = true;
    bool res_ImpliesLogicOp_18 = true;
    bool res_OrLogicOP_19 = false;
    bool res_OrLogicOP_20 = false;
    bool res_OrLogicOP_21 = false;
    bool res_OrLogicOP_22 = false;
    bool res_OrLogicOP_23 = false;
    res_OrLogicOP_23 = (res_OrLogicOP_23 || (L_P1__Macro7(my_id,c180x,verde,spento,avanzamento,true,verde,c120) == true));
    bool res_NotLogicOP_24 = true;
    res_NotLogicOP_24 = (res_NotLogicOP_24 && ! Timer_Attivo(L_P1__GetMainc47(my_id)));
    res_OrLogicOP_23 = (res_OrLogicOP_23 || res_NotLogicOP_24);
    
    res_OrLogicOP_22 = (res_OrLogicOP_22 || res_OrLogicOP_23);
    bool res_NotLogicOP_25 = true;
    res_NotLogicOP_25 = (res_NotLogicOP_25 && ! (L_P1__GetMainc34(my_id) == 10u));
    res_OrLogicOP_22 = (res_OrLogicOP_22 || res_NotLogicOP_25);
    
    res_OrLogicOP_21 = (res_OrLogicOP_21 || res_OrLogicOP_22);
    bool res_NotLogicOP_26 = true;
    res_NotLogicOP_26 = (res_NotLogicOP_26 && ! (argom26 == false));
    res_OrLogicOP_21 = (res_OrLogicOP_21 || res_NotLogicOP_26);
    
    res_OrLogicOP_20 = (res_OrLogicOP_20 || res_OrLogicOP_21);
    bool res_NotLogicOP_27 = true;
    bool res_NotLogicOP_28 = true;
    res_NotLogicOP_28 = (res_NotLogicOP_28 && ! (argom26 == false));
    res_NotLogicOP_27 = (res_NotLogicOP_27 && ! res_NotLogicOP_28);
    res_OrLogicOP_20 = (res_OrLogicOP_20 || res_NotLogicOP_27);
    
    res_OrLogicOP_19 = (res_OrLogicOP_19 || res_OrLogicOP_20);
    bool res_NotLogicOP_29 = true;
    res_NotLogicOP_29 = (res_NotLogicOP_29 && ! Timer_Attivo(L_P1__GetMainc46(my_id)));
    res_OrLogicOP_19 = (res_OrLogicOP_19 || res_NotLogicOP_29);
    
    if(res_OrLogicOP_19){
    bool res_XorLogicOP_30 = true;
    int xorIndex_res_XorLogicOP_30 = 0;
    bool res_ImpliesLogicOp_31 = true;
    bool res_AndLogicOP_32 = true;
    bool res_NotLogicOP_33 = true;
    res_NotLogicOP_33 = (res_NotLogicOP_33 && ! (L_P1__GetMainc34(my_id) == 4u));
    res_AndLogicOP_32 = (res_AndLogicOP_32 && res_NotLogicOP_33);
    bool res_NotLogicOP_34 = true;
    res_NotLogicOP_34 = (res_NotLogicOP_34 && ! (L_P1__GetInMainc5(my_id) == true));
    res_AndLogicOP_32 = (res_AndLogicOP_32 && res_NotLogicOP_34);
    
    if(res_AndLogicOP_32){
    bool res_AndLogicOP_35 = true;
    bool res_ImpliesLogicOp_36 = true;
    bool res_AndLogicOP_37 = true;
    res_AndLogicOP_37 = (res_AndLogicOP_37 && (L_P1_C1_GetState(my_id) == C1_St_state));
    bool res_NotLogicOP_38 = true;
    res_NotLogicOP_38 = (res_NotLogicOP_38 && ! (L_P1__GetMainc34(my_id) == 5u));
    res_AndLogicOP_37 = (res_AndLogicOP_37 && res_NotLogicOP_38);
    
    if(res_AndLogicOP_37){
    bool res_XorLogicOP_39 = true;
    int xorIndex_res_XorLogicOP_39 = 0;
    bool res_ImpliesLogicOp_40 = true;
    bool res_OrLogicOP_41 = false;
    bool res_NotLogicOP_42 = true;
    res_NotLogicOP_42 = (res_NotLogicOP_42 && ! (L_P1__Macro7(my_id,avanzamento,spento,spento,c180x,true,spento,c120) == false));
    res_OrLogicOP_41 = (res_OrLogicOP_41 || res_NotLogicOP_42);
    bool res_NotLogicOP_43 = true;
    res_NotLogicOP_43 = (res_NotLogicOP_43 && ! Timer_Disattivo(L_P1__GetMainc47(my_id)));
    res_OrLogicOP_41 = (res_OrLogicOP_41 || res_NotLogicOP_43);
    
    if(res_OrLogicOP_41){
    bool res_AndLogicOP_44 = true;
    bool res_ImpliesLogicOp_45 = true;
    bool res_OrLogicOP_46 = false;
    bool res_OrLogicOP_47 = false;
    bool res_NotLogicOP_48 = true;
    bool res_NotLogicOP_49 = true;
    res_NotLogicOP_49 = (res_NotLogicOP_49 && ! (L_P1__GetStato1(my_id) == C1_St_state));
    res_NotLogicOP_48 = (res_NotLogicOP_48 && ! res_NotLogicOP_49);
    res_OrLogicOP_47 = (res_OrLogicOP_47 || res_NotLogicOP_48);
    bool res_AndLogicOP_50 = true;
    bool res_NotLogicOP_51 = true;
    res_NotLogicOP_51 = (res_NotLogicOP_51 && ! (L_P1__GetParamMainc9(my_id) > 3u));
    res_AndLogicOP_50 = (res_AndLogicOP_50 && res_NotLogicOP_51);
    bool res_NotLogicOP_52 = true;
    bool res_NotLogicOP_53 = true;
    res_NotLogicOP_53 = (res_NotLogicOP_53 && ! (Counter_GetValore(L_P1__GetMainc51(my_id)) == 12u));
    res_NotLogicOP_52 = (res_NotLogicOP_52 && ! res_NotLogicOP_53);
    res_AndLogicOP_50 = (res_AndLogicOP_50 && res_NotLogicOP_52);
    
    res_OrLogicOP_47 = (res_OrLogicOP_47 || res_AndLogicOP_50);
    
    res_OrLogicOP_46 = (res_OrLogicOP_46 || res_OrLogicOP_47);
    bool res_NotLogicOP_54 = true;
    bool res_NotLogicOP_55 = true;
    res_NotLogicOP_55 = (res_NotLogicOP_55 && ! (L_P1__GetInMainc3(my_id) == true));
    res_NotLogicOP_54 = (res_NotLogicOP_54 && ! res_NotLogicOP_55);
    res_OrLogicOP_46 = (res_OrLogicOP_46 || res_NotLogicOP_54);
    
    if(res_OrLogicOP_46){
    bool res_XorLogicOP_56 = true;
    int xorIndex_res_XorLogicOP_56 = 0;
    bool res_ImpliesLogicOp_57 = true;
    bool res_NotLogicOP_58 = true;
    bool res_NotLogicOP_59 = true;
    res_NotLogicOP_59 = (res_NotLogicOP_59 && ! (L_P1__GetStato1(my_id) == C1_St_state));
    res_NotLogicOP_58 = (res_NotLogicOP_58 && ! res_NotLogicOP_59);
    if(res_NotLogicOP_58){
    bool res_AndLogicOP_60 = true;
    bool res_ImpliesLogicOp_61 = true;
    bool res_OrLogicOP_62 = false;
    bool res_OrLogicOP_63 = false;
    bool res_OrLogicOP_64 = false;
    res_OrLogicOP_64 = (res_OrLogicOP_64 || (L_P1__GetParamMainc7(my_id) < 5u));
    res_OrLogicOP_64 = (res_OrLogicOP_64 || (argom23 == rossogiallo));
    
    res_OrLogicOP_63 = (res_OrLogicOP_63 || res_OrLogicOP_64);
    bool res_NotLogicOP_65 = true;
    res_NotLogicOP_65 = (res_NotLogicOP_65 && ! (L_P1__GetMainc32(my_id) == false));
    res_OrLogicOP_63 = (res_OrLogicOP_63 || res_NotLogicOP_65);
    
    res_OrLogicOP_62 = (res_OrLogicOP_62 || res_OrLogicOP_63);
    bool res_NotLogicOP_66 = true;
    res_NotLogicOP_66 = (res_NotLogicOP_66 && ! (L_P1__GetMainc33(my_id) == rossogiallo));
    res_OrLogicOP_62 = (res_OrLogicOP_62 || res_NotLogicOP_66);
    
    if(res_OrLogicOP_62){
    bool res_AndLogicOP_67 = true;
    bool res_ImpliesLogicOp_68 = true;
    bool res_OrLogicOP_69 = false;
    bool res_AndLogicOP_70 = true;
    bool res_NotLogicOP_71 = true;
    bool res_NotLogicOP_72 = true;
    res_NotLogicOP_72 = (res_NotLogicOP_72 && ! (L_P1__GetInMainc3(my_id) == false));
    res_NotLogicOP_71 = (res_NotLogicOP_71 && ! res_NotLogicOP_72);
    res_AndLogicOP_70 = (res_AndLogicOP_70 && res_NotLogicOP_71);
    bool res_NotLogicOP_73 = true;
    res_NotLogicOP_73 = (res_NotLogicOP_73 && ! (L_P1__GetMainc33(my_id) == rossogiallo));
    res_AndLogicOP_70 = (res_AndLogicOP_70 && res_NotLogicOP_73);
    
    res_OrLogicOP_69 = (res_OrLogicOP_69 || res_AndLogicOP_70);
    bool res_AndLogicOP_74 = true;
    bool res_AndLogicOP_75 = true;
    bool res_NotLogicOP_76 = true;
    res_NotLogicOP_76 = (res_NotLogicOP_76 && ! (L_P1__GetParamMainc7(my_id) > 4u));
    res_AndLogicOP_75 = (res_AndLogicOP_75 && res_NotLogicOP_76);
    bool res_NotLogicOP_77 = true;
    bool res_NotLogicOP_78 = true;
    res_NotLogicOP_78 = (res_NotLogicOP_78 && ! (argom25 == true));
    res_NotLogicOP_77 = (res_NotLogicOP_77 && ! res_NotLogicOP_78);
    res_AndLogicOP_75 = (res_AndLogicOP_75 && res_NotLogicOP_77);
    
    res_AndLogicOP_74 = (res_AndLogicOP_74 && res_AndLogicOP_75);
    bool res_NotLogicOP_79 = true;
    res_NotLogicOP_79 = (res_NotLogicOP_79 && ! Timer_Disattivo(L_P1__GetMainc48(my_id)));
    res_AndLogicOP_74 = (res_AndLogicOP_74 && res_NotLogicOP_79);
    
    res_OrLogicOP_69 = (res_OrLogicOP_69 || res_AndLogicOP_74);
    
    if(res_OrLogicOP_69){
    bool res_AndLogicOP_80 = true;
    bool res_ImpliesLogicOp_81 = true;
    bool res_AndLogicOP_82 = true;
    bool res_AndLogicOP_83 = true;
    bool res_AndLogicOP_84 = true;
    bool res_AndLogicOP_85 = true;
    bool res_AndLogicOP_86 = true;
    bool res_NotLogicOP_87 = true;
    res_NotLogicOP_87 = (res_NotLogicOP_87 && ! (Counter_GetValore(L_P1__GetMainc51(my_id)) == 135u));
    res_AndLogicOP_86 = (res_AndLogicOP_86 && res_NotLogicOP_87);
    bool res_NotLogicOP_88 = true;
    res_NotLogicOP_88 = (res_NotLogicOP_88 && ! (argom26 == true));
    res_AndLogicOP_86 = (res_AndLogicOP_86 && res_NotLogicOP_88);
    
    res_AndLogicOP_85 = (res_AndLogicOP_85 && res_AndLogicOP_86);
    bool res_NotLogicOP_89 = true;
    bool res_NotLogicOP_90 = true;
    res_NotLogicOP_90 = (res_NotLogicOP_90 && ! (L_P1__GetMainc34(my_id) == 5u));
    res_NotLogicOP_89 = (res_NotLogicOP_89 && ! res_NotLogicOP_90);
    res_AndLogicOP_85 = (res_AndLogicOP_85 && res_NotLogicOP_89);
    
    res_AndLogicOP_84 = (res_AndLogicOP_84 && res_AndLogicOP_85);
    bool res_NotLogicOP_91 = true;
    bool res_NotLogicOP_92 = true;
    res_NotLogicOP_92 = (res_NotLogicOP_92 && ! (L_P1__GetParamMainc8(my_id) == true));
    res_NotLogicOP_91 = (res_NotLogicOP_91 && ! res_NotLogicOP_92);
    res_AndLogicOP_84 = (res_AndLogicOP_84 && res_NotLogicOP_91);
    
    res_AndLogicOP_83 = (res_AndLogicOP_83 && res_AndLogicOP_84);
    bool res_NotLogicOP_93 = true;
    bool res_NotLogicOP_94 = true;
    res_NotLogicOP_94 = (res_NotLogicOP_94 && ! (L_P1__GetParamMainc7(my_id) == 9u));
    res_NotLogicOP_93 = (res_NotLogicOP_93 && ! res_NotLogicOP_94);
    res_AndLogicOP_83 = (res_AndLogicOP_83 && res_NotLogicOP_93);
    
    res_AndLogicOP_82 = (res_AndLogicOP_82 && res_AndLogicOP_83);
    bool res_NotLogicOP_95 = true;
    res_NotLogicOP_95 = (res_NotLogicOP_95 && ! (L_P1__GetMainc33(my_id) == rossogiallo));
    res_AndLogicOP_82 = (res_AndLogicOP_82 && res_NotLogicOP_95);
    
    if(res_AndLogicOP_82){
    bool res_XorLogicOP_96 = true;
    int xorIndex_res_XorLogicOP_96 = 0;
    bool res_ImpliesLogicOp_97 = true;
    bool res_OrLogicOP_98 = false;
    res_OrLogicOP_98 = (res_OrLogicOP_98 || (L_P1__GetInConsd(my_id) == false));
    bool res_AndLogicOP_99 = true;
    res_AndLogicOP_99 = (res_AndLogicOP_99 && Timer_Disattivo(L_P1__GetMainc46(my_id)));
    bool res_NotLogicOP_100 = true;
    res_NotLogicOP_100 = (res_NotLogicOP_100 && ! (L_P1__GetMainc33(my_id) == rossogiallo));
    res_AndLogicOP_99 = (res_AndLogicOP_99 && res_NotLogicOP_100);
    
    res_OrLogicOP_98 = (res_OrLogicOP_98 || res_AndLogicOP_99);
    
    if(res_OrLogicOP_98){
    bool res_XorLogicOP_101 = true;
    int xorIndex_res_XorLogicOP_101 = 0;
    bool res_ImpliesLogicOp_102 = true;
    bool res_AndLogicOP_103 = true;
    bool res_NotLogicOP_104 = true;
    res_NotLogicOP_104 = (res_NotLogicOP_104 && ! Timer_Scaduto(L_P1__GetMainc37(my_id)));
    res_AndLogicOP_103 = (res_AndLogicOP_103 && res_NotLogicOP_104);
    bool res_NotLogicOP_105 = true;
    res_NotLogicOP_105 = (res_NotLogicOP_105 && ! (L_P1__GetParamMainc7(my_id) == 3u));
    res_AndLogicOP_103 = (res_AndLogicOP_103 && res_NotLogicOP_105);
    
    if(res_AndLogicOP_103){
    bool res_XorLogicOP_106 = true;
    int xorIndex_res_XorLogicOP_106 = 0;
    bool res_ImpliesLogicOp_107 = true;
    if((Counter_GetValore(L_P1__GetMainc49(my_id)) > 1543u)){
    bool res_AndLogicOP_108 = true;
    bool res_ImpliesLogicOp_109 = true;
    bool res_OrLogicOP_110 = false;
    bool res_OrLogicOP_111 = false;
    bool res_OrLogicOP_112 = false;
    bool res_NotLogicOP_113 = true;
    res_NotLogicOP_113 = (res_NotLogicOP_113 && ! Timer_Scaduto(L_P1__GetMainc37(my_id)));
    res_OrLogicOP_112 = (res_OrLogicOP_112 || res_NotLogicOP_113);
    bool res_AndLogicOP_114 = true;
    res_AndLogicOP_114 = (res_AndLogicOP_114 && (Counter_GetValore(L_P1__GetMainc49(my_id)) == 141u));
    res_AndLogicOP_114 = (res_AndLogicOP_114 && (L_P1__GetMainc32(my_id) == true));
    
    res_OrLogicOP_112 = (res_OrLogicOP_112 || res_AndLogicOP_114);
    
    res_OrLogicOP_111 = (res_OrLogicOP_111 || res_OrLogicOP_112);
    res_OrLogicOP_111 = (res_OrLogicOP_111 || (L_P1__GetParamMainc7(my_id) == 3u));
    
    res_OrLogicOP_110 = (res_OrLogicOP_110 || res_OrLogicOP_111);
    bool res_AndLogicOP_115 = true;
    res_AndLogicOP_115 = (res_AndLogicOP_115 && (Counter_GetValore(L_P1__GetMainc50(my_id)) == 1420u));
    res_AndLogicOP_115 = (res_AndLogicOP_115 && (L_P1__GetParamMainc9(my_id) == 7u));
    
    res_OrLogicOP_110 = (res_OrLogicOP_110 || res_AndLogicOP_115);
    
    if(res_OrLogicOP_110){
    bool res_XorLogicOP_116 = true;
    int xorIndex_res_XorLogicOP_116 = 0;
    bool res_ImpliesLogicOp_117 = true;
    bool res_OrLogicOP_118 = false;
    bool res_AndLogicOP_119 = true;
    bool res_NotLogicOP_120 = true;
    res_NotLogicOP_120 = (res_NotLogicOP_120 && ! (L_P1__GetInMainc2(my_id) == rossogiallo));
    res_AndLogicOP_119 = (res_AndLogicOP_119 && res_NotLogicOP_120);
    bool res_NotLogicOP_121 = true;
    bool res_NotLogicOP_122 = true;
    res_NotLogicOP_122 = (res_NotLogicOP_122 && ! (argom21 == true));
    res_NotLogicOP_121 = (res_NotLogicOP_121 && ! res_NotLogicOP_122);
    res_AndLogicOP_119 = (res_AndLogicOP_119 && res_NotLogicOP_121);
    
    res_OrLogicOP_118 = (res_OrLogicOP_118 || res_AndLogicOP_119);
    res_OrLogicOP_118 = (res_OrLogicOP_118 || (Counter_GetValore(L_P1__GetMainc51(my_id)) > 13543u));
    
    if(res_OrLogicOP_118){
    bool res_XorLogicOP_123 = true;
    int xorIndex_res_XorLogicOP_123 = 0;
    bool res_ImpliesLogicOp_124 = true;
    bool res_OrLogicOP_125 = false;
    bool res_OrLogicOP_126 = false;
    bool res_NotLogicOP_127 = true;
    res_NotLogicOP_127 = (res_NotLogicOP_127 && ! Timer_Attivo(L_P1__GetMainc39(my_id)));
    res_OrLogicOP_126 = (res_OrLogicOP_126 || res_NotLogicOP_127);
    bool res_NotLogicOP_128 = true;
    res_NotLogicOP_128 = (res_NotLogicOP_128 && ! Timer_Scaduto(L_P1__GetMainc46(my_id)));
    res_OrLogicOP_126 = (res_OrLogicOP_126 || res_NotLogicOP_128);
    
    res_OrLogicOP_125 = (res_OrLogicOP_125 || res_OrLogicOP_126);
    bool res_AndLogicOP_129 = true;
    bool res_AndLogicOP_130 = true;
    bool res_AndLogicOP_131 = true;
    bool res_NotLogicOP_132 = true;
    res_NotLogicOP_132 = (res_NotLogicOP_132 && ! Timer_Disattivo(L_P1__GetMainc46(my_id)));
    res_AndLogicOP_131 = (res_AndLogicOP_131 && res_NotLogicOP_132);
    res_AndLogicOP_131 = (res_AndLogicOP_131 && (L_P1__GetInMainc5(my_id) == true));
    
    res_AndLogicOP_130 = (res_AndLogicOP_130 && res_AndLogicOP_131);
    bool res_NotLogicOP_133 = true;
    res_NotLogicOP_133 = (res_NotLogicOP_133 && ! (L_P1__GetMainc33(my_id) == rossogiallo));
    res_AndLogicOP_130 = (res_AndLogicOP_130 && res_NotLogicOP_133);
    
    res_AndLogicOP_129 = (res_AndLogicOP_129 && res_AndLogicOP_130);
    res_AndLogicOP_129 = (res_AndLogicOP_129 && Timer_Disattivo(L_P1__GetMainc47(my_id)));
    
    res_OrLogicOP_125 = (res_OrLogicOP_125 || res_AndLogicOP_129);
    
    if(res_OrLogicOP_125){
    bool res_AndLogicOP_134 = true;
    bool res_ImpliesLogicOp_135 = true;
    bool res_OrLogicOP_136 = false;
    bool res_OrLogicOP_137 = false;
    res_OrLogicOP_137 = (res_OrLogicOP_137 || (L_P1_C1_GetState(my_id) == C1_St_state));
    bool res_NotLogicOP_138 = true;
    res_NotLogicOP_138 = (res_NotLogicOP_138 && ! (argom26 == true));
    res_OrLogicOP_137 = (res_OrLogicOP_137 || res_NotLogicOP_138);
    
    res_OrLogicOP_136 = (res_OrLogicOP_136 || res_OrLogicOP_137);
    res_OrLogicOP_136 = (res_OrLogicOP_136 || (argom21 == true));
    
    if(res_OrLogicOP_136){
    bool res_AndLogicOP_139 = true;
    bool res_ImpliesLogicOp_140 = true;
    bool res_OrLogicOP_141 = false;
    bool res_OrLogicOP_142 = false;
    bool res_OrLogicOP_143 = false;
    res_OrLogicOP_143 = (res_OrLogicOP_143 || (L_P1__GetMainc33(my_id) == rossogiallo));
    bool res_NotLogicOP_144 = true;
    res_NotLogicOP_144 = (res_NotLogicOP_144 && ! (L_P1__GetInMainc5(my_id) == true));
    res_OrLogicOP_143 = (res_OrLogicOP_143 || res_NotLogicOP_144);
    
    res_OrLogicOP_142 = (res_OrLogicOP_142 || res_OrLogicOP_143);
    bool res_AndLogicOP_145 = true;
    bool res_AndLogicOP_146 = true;
    res_AndLogicOP_146 = (res_AndLogicOP_146 && (L_P1__GetParamMainc9(my_id) == 8u));
    bool res_NotLogicOP_147 = true;
    res_NotLogicOP_147 = (res_NotLogicOP_147 && ! (L_P1__GetMainc33(my_id) == rossogiallo));
    res_AndLogicOP_146 = (res_AndLogicOP_146 && res_NotLogicOP_147);
    
    res_AndLogicOP_145 = (res_AndLogicOP_145 && res_AndLogicOP_146);
    res_AndLogicOP_145 = (res_AndLogicOP_145 && Timer_Scaduto(L_P1__GetMainc47(my_id)));
    
    res_OrLogicOP_142 = (res_OrLogicOP_142 || res_AndLogicOP_145);
    
    res_OrLogicOP_141 = (res_OrLogicOP_141 || res_OrLogicOP_142);
    bool res_NotLogicOP_148 = true;
    res_NotLogicOP_148 = (res_NotLogicOP_148 && ! Timer_Attivo(L_P1__GetMainc47(my_id)));
    res_OrLogicOP_141 = (res_OrLogicOP_141 || res_NotLogicOP_148);
    
    if(res_OrLogicOP_141){
    bool res_AndLogicOP_149 = true;
    bool res_ImpliesLogicOp_150 = true;
    bool res_NotLogicOP_151 = true;
    res_NotLogicOP_151 = (res_NotLogicOP_151 && ! (L_P1__Macro6(my_id,c270x,rossogiallo,c180,c270x,verde,true) == true));
    if(res_NotLogicOP_151){
    bool res_AndLogicOP_152 = true;
    bool res_ImpliesLogicOp_153 = true;
    bool res_OrLogicOP_154 = false;
    bool res_OrLogicOP_155 = false;
    bool res_OrLogicOP_156 = false;
    bool res_NotLogicOP_157 = true;
    bool res_NotLogicOP_158 = true;
    res_NotLogicOP_158 = (res_NotLogicOP_158 && ! (L_P1__GetInMainc4(my_id) == c180x));
    res_NotLogicOP_157 = (res_NotLogicOP_157 && ! res_NotLogicOP_158);
    res_OrLogicOP_156 = (res_OrLogicOP_156 || res_NotLogicOP_157);
    bool res_NotLogicOP_159 = true;
    res_NotLogicOP_159 = (res_NotLogicOP_159 && ! (L_P1__GetMainc33(my_id) == rossogiallo));
    res_OrLogicOP_156 = (res_OrLogicOP_156 || res_NotLogicOP_159);
    
    res_OrLogicOP_155 = (res_OrLogicOP_155 || res_OrLogicOP_156);
    res_OrLogicOP_155 = (res_OrLogicOP_155 || (argom26 == false));
    
    res_OrLogicOP_154 = (res_OrLogicOP_154 || res_OrLogicOP_155);
    bool res_NotLogicOP_160 = true;
    bool res_NotLogicOP_161 = true;
    res_NotLogicOP_161 = (res_NotLogicOP_161 && ! (L_P1__GetMainc33(my_id) == rossogiallo));
    res_NotLogicOP_160 = (res_NotLogicOP_160 && ! res_NotLogicOP_161);
    res_OrLogicOP_154 = (res_OrLogicOP_154 || res_NotLogicOP_160);
    
    if(res_OrLogicOP_154){
    bool res_XorLogicOP_162 = true;
    int xorIndex_res_XorLogicOP_162 = 0;
    bool res_ImpliesLogicOp_163 = true;
    bool res_OrLogicOP_164 = false;
    bool res_OrLogicOP_165 = false;
    bool res_OrLogicOP_166 = false;
    bool res_NotLogicOP_167 = true;
    bool res_NotLogicOP_168 = true;
    res_NotLogicOP_168 = (res_NotLogicOP_168 && ! (argom25 == true));
    res_NotLogicOP_167 = (res_NotLogicOP_167 && ! res_NotLogicOP_168);
    res_OrLogicOP_166 = (res_OrLogicOP_166 || res_NotLogicOP_167);
    bool res_NotLogicOP_169 = true;
    res_NotLogicOP_169 = (res_NotLogicOP_169 && ! (argom26 == false));
    res_OrLogicOP_166 = (res_OrLogicOP_166 || res_NotLogicOP_169);
    
    res_OrLogicOP_165 = (res_OrLogicOP_165 || res_OrLogicOP_166);
    bool res_NotLogicOP_170 = true;
    bool res_NotLogicOP_171 = true;
    res_NotLogicOP_171 = (res_NotLogicOP_171 && ! (L_P1__GetParamMainc8(my_id) == true));
    res_NotLogicOP_170 = (res_NotLogicOP_170 && ! res_NotLogicOP_171);
    res_OrLogicOP_165 = (res_OrLogicOP_165 || res_NotLogicOP_170);
    
    res_OrLogicOP_164 = (res_OrLogicOP_164 || res_OrLogicOP_165);
    bool res_NotLogicOP_172 = true;
    res_NotLogicOP_172 = (res_NotLogicOP_172 && ! (Counter_GetValore(L_P1__GetMainc51(my_id)) > 13054u));
    res_OrLogicOP_164 = (res_OrLogicOP_164 || res_NotLogicOP_172);
    
    if(res_OrLogicOP_164){
    bool res_XorLogicOP_173 = true;
    int xorIndex_res_XorLogicOP_173 = 0;
    bool res_ImpliesLogicOp_174 = true;
    bool res_OrLogicOP_175 = false;
    bool res_OrLogicOP_176 = false;
    bool res_OrLogicOP_177 = false;
    bool res_NotLogicOP_178 = true;
    res_NotLogicOP_178 = (res_NotLogicOP_178 && ! (Counter_GetValore(L_P1__GetMainc49(my_id)) == 12312u));
    res_OrLogicOP_177 = (res_OrLogicOP_177 || res_NotLogicOP_178);
    bool res_NotLogicOP_179 = true;
    res_NotLogicOP_179 = (res_NotLogicOP_179 && ! (L_P1__GetInMainc2(my_id) == rossogiallo));
    res_OrLogicOP_177 = (res_OrLogicOP_177 || res_NotLogicOP_179);
    
    res_OrLogicOP_176 = (res_OrLogicOP_176 || res_OrLogicOP_177);
    bool res_NotLogicOP_180 = true;
    res_NotLogicOP_180 = (res_NotLogicOP_180 && ! (Counter_GetValore(L_P1__GetMainc50(my_id)) > 1205u));
    res_OrLogicOP_176 = (res_OrLogicOP_176 || res_NotLogicOP_180);
    
    res_OrLogicOP_175 = (res_OrLogicOP_175 || res_OrLogicOP_176);
    bool res_NotLogicOP_181 = true;
    bool res_NotLogicOP_182 = true;
    res_NotLogicOP_182 = (res_NotLogicOP_182 && ! (L_P1__GetInMainc2(my_id) == rossogiallo));
    res_NotLogicOP_181 = (res_NotLogicOP_181 && ! res_NotLogicOP_182);
    res_OrLogicOP_175 = (res_OrLogicOP_175 || res_NotLogicOP_181);
    
    if(res_OrLogicOP_175){
    bool res_ImpliesLogicOp_183 = true;
    bool res_OrLogicOP_184 = false;
    res_OrLogicOP_184 = (res_OrLogicOP_184 || (L_P1_C1_GetState(my_id) == C1_St_state));
    res_OrLogicOP_184 = (res_OrLogicOP_184 || Timer_Disattivo(L_P1__GetMainc47(my_id)));
    
    if(res_OrLogicOP_184){
    bool res_OrLogicOP_185 = false;
    bool res_OrLogicOP_186 = false;
    bool res_OrLogicOP_187 = false;
    bool res_OrLogicOP_188 = false;
    bool res_AndLogicOP_189 = true;
    res_AndLogicOP_189 = (res_AndLogicOP_189 && (argom25 == true));
    res_AndLogicOP_189 = (res_AndLogicOP_189 && (L_P1__GetInMainc5(my_id) == true));
    
    res_OrLogicOP_188 = (res_OrLogicOP_188 || res_AndLogicOP_189);
    bool res_NotLogicOP_190 = true;
    res_NotLogicOP_190 = (res_NotLogicOP_190 && ! (argom26 == false));
    res_OrLogicOP_188 = (res_OrLogicOP_188 || res_NotLogicOP_190);
    
    res_OrLogicOP_187 = (res_OrLogicOP_187 || res_OrLogicOP_188);
    res_OrLogicOP_187 = (res_OrLogicOP_187 || Timer_Attivo(L_P1__GetMainc47(my_id)));
    
    res_OrLogicOP_186 = (res_OrLogicOP_186 || res_OrLogicOP_187);
    bool res_NotLogicOP_191 = true;
    res_NotLogicOP_191 = (res_NotLogicOP_191 && ! Timer_Attivo(L_P1__GetMainc46(my_id)));
    res_OrLogicOP_186 = (res_OrLogicOP_186 || res_NotLogicOP_191);
    
    res_OrLogicOP_185 = (res_OrLogicOP_185 || res_OrLogicOP_186);
    res_OrLogicOP_185 = (res_OrLogicOP_185 || (Counter_GetValore(L_P1__GetMainc50(my_id)) == 11u));
    
    res_ImpliesLogicOp_183 = (res_ImpliesLogicOp_183 && res_OrLogicOP_185);
    }
    res_ImpliesLogicOp_174 = (res_ImpliesLogicOp_174 && res_ImpliesLogicOp_183);
    }
    if(res_ImpliesLogicOp_174){
    xorIndex_res_XorLogicOP_173 = (xorIndex_res_XorLogicOP_173 + 1);
    }
    bool res_OrLogicOP_192 = false;
    bool res_OrLogicOP_193 = false;
    bool res_AndLogicOP_194 = true;
    bool res_NotLogicOP_195 = true;
    bool res_NotLogicOP_196 = true;
    res_NotLogicOP_196 = (res_NotLogicOP_196 && ! (argom25 == false));
    res_NotLogicOP_195 = (res_NotLogicOP_195 && ! res_NotLogicOP_196);
    res_AndLogicOP_194 = (res_AndLogicOP_194 && res_NotLogicOP_195);
    res_AndLogicOP_194 = (res_AndLogicOP_194 && (argom22 == c270x));
    
    res_OrLogicOP_193 = (res_OrLogicOP_193 || res_AndLogicOP_194);
    bool res_AndLogicOP_197 = true;
    res_AndLogicOP_197 = (res_AndLogicOP_197 && (L_P1__GetParamMainc9(my_id) == 4u));
    bool res_NotLogicOP_198 = true;
    res_NotLogicOP_198 = (res_NotLogicOP_198 && ! (argom26 == true));
    res_AndLogicOP_197 = (res_AndLogicOP_197 && res_NotLogicOP_198);
    
    res_OrLogicOP_193 = (res_OrLogicOP_193 || res_AndLogicOP_197);
    
    res_OrLogicOP_192 = (res_OrLogicOP_192 || res_OrLogicOP_193);
    bool res_AndLogicOP_199 = true;
    bool res_NotLogicOP_200 = true;
    bool res_NotLogicOP_201 = true;
    res_NotLogicOP_201 = (res_NotLogicOP_201 && ! (argom25 == false));
    res_NotLogicOP_200 = (res_NotLogicOP_200 && ! res_NotLogicOP_201);
    res_AndLogicOP_199 = (res_AndLogicOP_199 && res_NotLogicOP_200);
    bool res_NotLogicOP_202 = true;
    res_NotLogicOP_202 = (res_NotLogicOP_202 && ! (Counter_GetValore(L_P1__GetMainc50(my_id)) == 114u));
    res_AndLogicOP_199 = (res_AndLogicOP_199 && res_NotLogicOP_202);
    
    res_OrLogicOP_192 = (res_OrLogicOP_192 || res_AndLogicOP_199);
    
    if(res_OrLogicOP_192){
    xorIndex_res_XorLogicOP_173 = (xorIndex_res_XorLogicOP_173 + 1);
    }
    
    res_XorLogicOP_173 = (res_XorLogicOP_173 && (xorIndex_res_XorLogicOP_173 == 1));
    res_ImpliesLogicOp_163 = (res_ImpliesLogicOp_163 && res_XorLogicOP_173);
    }
    if(res_ImpliesLogicOp_163){
    xorIndex_res_XorLogicOP_162 = (xorIndex_res_XorLogicOP_162 + 1);
    }
    bool res_OrLogicOP_203 = false;
    bool res_AndLogicOP_204 = true;
    bool res_NotLogicOP_205 = true;
    res_NotLogicOP_205 = (res_NotLogicOP_205 && ! (L_P1__GetMainc33(my_id) == rossogiallo));
    res_AndLogicOP_204 = (res_AndLogicOP_204 && res_NotLogicOP_205);
    bool res_NotLogicOP_206 = true;
    res_NotLogicOP_206 = (res_NotLogicOP_206 && ! (L_P1__GetParamMainc7(my_id) > 8u));
    res_AndLogicOP_204 = (res_AndLogicOP_204 && res_NotLogicOP_206);
    
    res_OrLogicOP_203 = (res_OrLogicOP_203 || res_AndLogicOP_204);
    bool res_NotLogicOP_207 = true;
    bool res_NotLogicOP_208 = true;
    res_NotLogicOP_208 = (res_NotLogicOP_208 && ! (L_P1__GetMainc33(my_id) == rossogiallo));
    res_NotLogicOP_207 = (res_NotLogicOP_207 && ! res_NotLogicOP_208);
    res_OrLogicOP_203 = (res_OrLogicOP_203 || res_NotLogicOP_207);
    
    if(res_OrLogicOP_203){
    xorIndex_res_XorLogicOP_162 = (xorIndex_res_XorLogicOP_162 + 1);
    }
    
    res_XorLogicOP_162 = (res_XorLogicOP_162 && (xorIndex_res_XorLogicOP_162 == 1));
    res_ImpliesLogicOp_153 = (res_ImpliesLogicOp_153 && res_XorLogicOP_162);
    }
    res_AndLogicOP_152 = (res_AndLogicOP_152 && res_ImpliesLogicOp_153);
    bool res_OrLogicOP_209 = false;
    bool res_OrLogicOP_210 = false;
    bool res_AndLogicOP_211 = true;
    res_AndLogicOP_211 = (res_AndLogicOP_211 && (L_P1__GetParamMainc7(my_id) == 1u));
    res_AndLogicOP_211 = (res_AndLogicOP_211 && (L_P1__GetMainc35(my_id) == false));
    
    res_OrLogicOP_210 = (res_OrLogicOP_210 || res_AndLogicOP_211);
    bool res_AndLogicOP_212 = true;
    bool res_AndLogicOP_213 = true;
    bool res_NotLogicOP_214 = true;
    res_NotLogicOP_214 = (res_NotLogicOP_214 && ! (argom26 == true));
    res_AndLogicOP_213 = (res_AndLogicOP_213 && res_NotLogicOP_214);
    bool res_NotLogicOP_215 = true;
    res_NotLogicOP_215 = (res_NotLogicOP_215 && ! (argom23 == rossogiallo));
    res_AndLogicOP_213 = (res_AndLogicOP_213 && res_NotLogicOP_215);
    
    res_AndLogicOP_212 = (res_AndLogicOP_212 && res_AndLogicOP_213);
    res_AndLogicOP_212 = (res_AndLogicOP_212 && (L_P1__GetInMainc5(my_id) == false));
    
    res_OrLogicOP_210 = (res_OrLogicOP_210 || res_AndLogicOP_212);
    
    res_OrLogicOP_209 = (res_OrLogicOP_209 || res_OrLogicOP_210);
    bool res_NotLogicOP_216 = true;
    res_NotLogicOP_216 = (res_NotLogicOP_216 && ! (L_P1__GetMainc33(my_id) == rossogiallo));
    res_OrLogicOP_209 = (res_OrLogicOP_209 || res_NotLogicOP_216);
    
    res_AndLogicOP_152 = (res_AndLogicOP_152 && res_OrLogicOP_209);
    
    res_ImpliesLogicOp_150 = (res_ImpliesLogicOp_150 && res_AndLogicOP_152);
    }
    res_AndLogicOP_149 = (res_AndLogicOP_149 && res_ImpliesLogicOp_150);
    bool res_OrLogicOP_217 = false;
    bool res_AndLogicOP_218 = true;
    bool res_NotLogicOP_219 = true;
    res_NotLogicOP_219 = (res_NotLogicOP_219 && ! (L_P1__GetParamMainc7(my_id) < 8u));
    res_AndLogicOP_218 = (res_AndLogicOP_218 && res_NotLogicOP_219);
    res_AndLogicOP_218 = (res_AndLogicOP_218 && Timer_Scaduto(L_P1__GetMainc46(my_id)));
    
    res_OrLogicOP_217 = (res_OrLogicOP_217 || res_AndLogicOP_218);
    res_OrLogicOP_217 = (res_OrLogicOP_217 || (Counter_GetValore(L_P1__GetMainc49(my_id)) > 1231u));
    
    res_AndLogicOP_149 = (res_AndLogicOP_149 && res_OrLogicOP_217);
    
    res_ImpliesLogicOp_140 = (res_ImpliesLogicOp_140 && res_AndLogicOP_149);
    }
    res_AndLogicOP_139 = (res_AndLogicOP_139 && res_ImpliesLogicOp_140);
    bool res_OrLogicOP_220 = false;
    bool res_OrLogicOP_221 = false;
    bool res_AndLogicOP_222 = true;
    bool res_NotLogicOP_223 = true;
    res_NotLogicOP_223 = (res_NotLogicOP_223 && ! (Counter_GetValore(L_P1__GetMainc49(my_id)) < 1320u));
    res_AndLogicOP_222 = (res_AndLogicOP_222 && res_NotLogicOP_223);
    bool res_NotLogicOP_224 = true;
    res_NotLogicOP_224 = (res_NotLogicOP_224 && ! (L_P1__GetInMainc5(my_id) == false));
    res_AndLogicOP_222 = (res_AndLogicOP_222 && res_NotLogicOP_224);
    
    res_OrLogicOP_221 = (res_OrLogicOP_221 || res_AndLogicOP_222);
    bool res_AndLogicOP_225 = true;
    res_AndLogicOP_225 = (res_AndLogicOP_225 && (Counter_GetValore(L_P1__GetMainc49(my_id)) > 1554u));
    bool res_NotLogicOP_226 = true;
    res_NotLogicOP_226 = (res_NotLogicOP_226 && ! (L_P1__GetInMainc2(my_id) == rossogiallo));
    res_AndLogicOP_225 = (res_AndLogicOP_225 && res_NotLogicOP_226);
    
    res_OrLogicOP_221 = (res_OrLogicOP_221 || res_AndLogicOP_225);
    
    res_OrLogicOP_220 = (res_OrLogicOP_220 || res_OrLogicOP_221);
    bool res_NotLogicOP_227 = true;
    res_NotLogicOP_227 = (res_NotLogicOP_227 && ! (L_P1__GetInMainc3(my_id) == false));
    res_OrLogicOP_220 = (res_OrLogicOP_220 || res_NotLogicOP_227);
    
    res_AndLogicOP_139 = (res_AndLogicOP_139 && res_OrLogicOP_220);
    
    res_ImpliesLogicOp_135 = (res_ImpliesLogicOp_135 && res_AndLogicOP_139);
    }
    res_AndLogicOP_134 = (res_AndLogicOP_134 && res_ImpliesLogicOp_135);
    bool res_OrLogicOP_228 = false;
    bool res_AndLogicOP_229 = true;
    bool res_AndLogicOP_230 = true;
    res_AndLogicOP_230 = (res_AndLogicOP_230 && Timer_Disattivo(L_P1__GetMainc46(my_id)));
    bool res_NotLogicOP_231 = true;
    bool res_NotLogicOP_232 = true;
    res_NotLogicOP_232 = (res_NotLogicOP_232 && ! (Counter_GetValore(L_P1__GetMainc51(my_id)) == 1131u));
    res_NotLogicOP_231 = (res_NotLogicOP_231 && ! res_NotLogicOP_232);
    res_AndLogicOP_230 = (res_AndLogicOP_230 && res_NotLogicOP_231);
    
    res_AndLogicOP_229 = (res_AndLogicOP_229 && res_AndLogicOP_230);
    bool res_NotLogicOP_233 = true;
    res_NotLogicOP_233 = (res_NotLogicOP_233 && ! (Counter_GetValore(L_P1__GetMainc49(my_id)) > 15u));
    res_AndLogicOP_229 = (res_AndLogicOP_229 && res_NotLogicOP_233);
    
    res_OrLogicOP_228 = (res_OrLogicOP_228 || res_AndLogicOP_229);
    bool res_NotLogicOP_234 = true;
    res_NotLogicOP_234 = (res_NotLogicOP_234 && ! (argom26 == false));
    res_OrLogicOP_228 = (res_OrLogicOP_228 || res_NotLogicOP_234);
    
    res_AndLogicOP_134 = (res_AndLogicOP_134 && res_OrLogicOP_228);
    
    res_ImpliesLogicOp_124 = (res_ImpliesLogicOp_124 && res_AndLogicOP_134);
    }
    if(res_ImpliesLogicOp_124){
    xorIndex_res_XorLogicOP_123 = (xorIndex_res_XorLogicOP_123 + 1);
    }
    bool res_OrLogicOP_235 = false;
    bool res_OrLogicOP_236 = false;
    bool res_AndLogicOP_237 = true;
    res_AndLogicOP_237 = (res_AndLogicOP_237 && (L_P1__GetMainc33(my_id) == rossogiallo));
    res_AndLogicOP_237 = (res_AndLogicOP_237 && (Counter_GetValore(L_P1__GetMainc51(my_id)) < 14u));
    
    res_OrLogicOP_236 = (res_OrLogicOP_236 || res_AndLogicOP_237);
    bool res_AndLogicOP_238 = true;
    bool res_NotLogicOP_239 = true;
    res_NotLogicOP_239 = (res_NotLogicOP_239 && ! (argom26 == false));
    res_AndLogicOP_238 = (res_AndLogicOP_238 && res_NotLogicOP_239);
    res_AndLogicOP_238 = (res_AndLogicOP_238 && (argom21 == true));
    
    res_OrLogicOP_236 = (res_OrLogicOP_236 || res_AndLogicOP_238);
    
    res_OrLogicOP_235 = (res_OrLogicOP_235 || res_OrLogicOP_236);
    bool res_AndLogicOP_240 = true;
    bool res_NotLogicOP_241 = true;
    bool res_NotLogicOP_242 = true;
    res_NotLogicOP_242 = (res_NotLogicOP_242 && ! (L_P1__GetInMainc3(my_id) == true));
    res_NotLogicOP_241 = (res_NotLogicOP_241 && ! res_NotLogicOP_242);
    res_AndLogicOP_240 = (res_AndLogicOP_240 && res_NotLogicOP_241);
    bool res_NotLogicOP_243 = true;
    res_NotLogicOP_243 = (res_NotLogicOP_243 && ! (L_P1__GetMainc33(my_id) == rossogiallo));
    res_AndLogicOP_240 = (res_AndLogicOP_240 && res_NotLogicOP_243);
    
    res_OrLogicOP_235 = (res_OrLogicOP_235 || res_AndLogicOP_240);
    
    if(res_OrLogicOP_235){
    xorIndex_res_XorLogicOP_123 = (xorIndex_res_XorLogicOP_123 + 1);
    }
    
    res_XorLogicOP_123 = (res_XorLogicOP_123 && (xorIndex_res_XorLogicOP_123 == 1));
    res_ImpliesLogicOp_117 = (res_ImpliesLogicOp_117 && res_XorLogicOP_123);
    }
    if(res_ImpliesLogicOp_117){
    xorIndex_res_XorLogicOP_116 = (xorIndex_res_XorLogicOP_116 + 1);
    }
    bool res_OrLogicOP_244 = false;
    bool res_OrLogicOP_245 = false;
    res_OrLogicOP_245 = (res_OrLogicOP_245 || (Counter_GetValore(L_P1__GetMainc51(my_id)) > 152054u));
    bool res_AndLogicOP_246 = true;
    bool res_AndLogicOP_247 = true;
    bool res_NotLogicOP_248 = true;
    res_NotLogicOP_248 = (res_NotLogicOP_248 && ! (L_P1__GetInMainc5(my_id) == true));
    res_AndLogicOP_247 = (res_AndLogicOP_247 && res_NotLogicOP_248);
    res_AndLogicOP_247 = (res_AndLogicOP_247 && (L_P1__GetMainc34(my_id) > 2u));
    
    res_AndLogicOP_246 = (res_AndLogicOP_246 && res_AndLogicOP_247);
    bool res_NotLogicOP_249 = true;
    res_NotLogicOP_249 = (res_NotLogicOP_249 && ! (L_P1__GetMainc33(my_id) == rossogiallo));
    res_AndLogicOP_246 = (res_AndLogicOP_246 && res_NotLogicOP_249);
    
    res_OrLogicOP_245 = (res_OrLogicOP_245 || res_AndLogicOP_246);
    
    res_OrLogicOP_244 = (res_OrLogicOP_244 || res_OrLogicOP_245);
    res_OrLogicOP_244 = (res_OrLogicOP_244 || Timer_Scaduto(L_P1__GetMainc48(my_id)));
    
    if(res_OrLogicOP_244){
    xorIndex_res_XorLogicOP_116 = (xorIndex_res_XorLogicOP_116 + 1);
    }
    
    res_XorLogicOP_116 = (res_XorLogicOP_116 && (xorIndex_res_XorLogicOP_116 == 1));
    res_ImpliesLogicOp_109 = (res_ImpliesLogicOp_109 && res_XorLogicOP_116);
    }
    res_AndLogicOP_108 = (res_AndLogicOP_108 && res_ImpliesLogicOp_109);
    bool res_NotLogicOP_250 = true;
    bool res_NotLogicOP_251 = true;
    res_NotLogicOP_251 = (res_NotLogicOP_251 && ! (argom26 == true));
    res_NotLogicOP_250 = (res_NotLogicOP_250 && ! res_NotLogicOP_251);
    res_AndLogicOP_108 = (res_AndLogicOP_108 && res_NotLogicOP_250);
    
    res_ImpliesLogicOp_107 = (res_ImpliesLogicOp_107 && res_AndLogicOP_108);
    }
    if(res_ImpliesLogicOp_107){
    xorIndex_res_XorLogicOP_106 = (xorIndex_res_XorLogicOP_106 + 1);
    }
    bool res_OrLogicOP_252 = false;
    bool res_AndLogicOP_253 = true;
    res_AndLogicOP_253 = (res_AndLogicOP_253 && Timer_Disattivo(L_P1__GetMainc48(my_id)));
    bool res_NotLogicOP_254 = true;
    res_NotLogicOP_254 = (res_NotLogicOP_254 && ! (Counter_GetValore(L_P1__GetMainc51(my_id)) == 133u));
    res_AndLogicOP_253 = (res_AndLogicOP_253 && res_NotLogicOP_254);
    
    res_OrLogicOP_252 = (res_OrLogicOP_252 || res_AndLogicOP_253);
    bool res_NotLogicOP_255 = true;
    res_NotLogicOP_255 = (res_NotLogicOP_255 && ! Timer_Attivo(L_P1__GetMainc48(my_id)));
    res_OrLogicOP_252 = (res_OrLogicOP_252 || res_NotLogicOP_255);
    
    if(res_OrLogicOP_252){
    xorIndex_res_XorLogicOP_106 = (xorIndex_res_XorLogicOP_106 + 1);
    }
    
    res_XorLogicOP_106 = (res_XorLogicOP_106 && (xorIndex_res_XorLogicOP_106 == 1));
    res_ImpliesLogicOp_102 = (res_ImpliesLogicOp_102 && res_XorLogicOP_106);
    }
    if(res_ImpliesLogicOp_102){
    xorIndex_res_XorLogicOP_101 = (xorIndex_res_XorLogicOP_101 + 1);
    }
    bool res_OrLogicOP_256 = false;
    res_OrLogicOP_256 = (res_OrLogicOP_256 || Timer_Scaduto(L_P1__GetMainc46(my_id)));
    bool res_AndLogicOP_257 = true;
    bool res_AndLogicOP_258 = true;
    bool res_NotLogicOP_259 = true;
    res_NotLogicOP_259 = (res_NotLogicOP_259 && ! (argom26 == true));
    res_AndLogicOP_258 = (res_AndLogicOP_258 && res_NotLogicOP_259);
    bool res_NotLogicOP_260 = true;
    bool res_NotLogicOP_261 = true;
    res_NotLogicOP_261 = (res_NotLogicOP_261 && ! (L_P1__GetInMainc3(my_id) == true));
    res_NotLogicOP_260 = (res_NotLogicOP_260 && ! res_NotLogicOP_261);
    res_AndLogicOP_258 = (res_AndLogicOP_258 && res_NotLogicOP_260);
    
    res_AndLogicOP_257 = (res_AndLogicOP_257 && res_AndLogicOP_258);
    res_AndLogicOP_257 = (res_AndLogicOP_257 && (Counter_GetValore(L_P1__GetMainc50(my_id)) < 151u));
    
    res_OrLogicOP_256 = (res_OrLogicOP_256 || res_AndLogicOP_257);
    
    if(res_OrLogicOP_256){
    xorIndex_res_XorLogicOP_101 = (xorIndex_res_XorLogicOP_101 + 1);
    }
    
    res_XorLogicOP_101 = (res_XorLogicOP_101 && (xorIndex_res_XorLogicOP_101 == 1));
    res_ImpliesLogicOp_97 = (res_ImpliesLogicOp_97 && res_XorLogicOP_101);
    }
    if(res_ImpliesLogicOp_97){
    xorIndex_res_XorLogicOP_96 = (xorIndex_res_XorLogicOP_96 + 1);
    }
    bool res_NotLogicOP_262 = true;
    res_NotLogicOP_262 = (res_NotLogicOP_262 && ! Timer_Scaduto(L_P1__GetMainc48(my_id)));
    if(res_NotLogicOP_262){
    xorIndex_res_XorLogicOP_96 = (xorIndex_res_XorLogicOP_96 + 1);
    }
    
    res_XorLogicOP_96 = (res_XorLogicOP_96 && (xorIndex_res_XorLogicOP_96 == 1));
    res_ImpliesLogicOp_81 = (res_ImpliesLogicOp_81 && res_XorLogicOP_96);
    }
    res_AndLogicOP_80 = (res_AndLogicOP_80 && res_ImpliesLogicOp_81);
    bool res_OrLogicOP_263 = false;
    res_OrLogicOP_263 = (res_OrLogicOP_263 || (argom25 == true));
    bool res_AndLogicOP_264 = true;
    bool res_AndLogicOP_265 = true;
    bool res_AndLogicOP_266 = true;
    bool res_NotLogicOP_267 = true;
    res_NotLogicOP_267 = (res_NotLogicOP_267 && ! (L_P1__GetParamMainc8(my_id) == true));
    res_AndLogicOP_266 = (res_AndLogicOP_266 && res_NotLogicOP_267);
    bool res_NotLogicOP_268 = true;
    bool res_NotLogicOP_269 = true;
    res_NotLogicOP_269 = (res_NotLogicOP_269 && ! (L_P1__GetInMainc4(my_id) == c180x));
    res_NotLogicOP_268 = (res_NotLogicOP_268 && ! res_NotLogicOP_269);
    res_AndLogicOP_266 = (res_AndLogicOP_266 && res_NotLogicOP_268);
    
    res_AndLogicOP_265 = (res_AndLogicOP_265 && res_AndLogicOP_266);
    bool res_NotLogicOP_270 = true;
    res_NotLogicOP_270 = (res_NotLogicOP_270 && ! (Counter_GetValore(L_P1__GetMainc51(my_id)) == 11205u));
    res_AndLogicOP_265 = (res_AndLogicOP_265 && res_NotLogicOP_270);
    
    res_AndLogicOP_264 = (res_AndLogicOP_264 && res_AndLogicOP_265);
    bool res_NotLogicOP_271 = true;
    res_NotLogicOP_271 = (res_NotLogicOP_271 && ! (L_P1__GetInMainc6(my_id) == c180x));
    res_AndLogicOP_264 = (res_AndLogicOP_264 && res_NotLogicOP_271);
    
    res_OrLogicOP_263 = (res_OrLogicOP_263 || res_AndLogicOP_264);
    
    res_AndLogicOP_80 = (res_AndLogicOP_80 && res_OrLogicOP_263);
    
    res_ImpliesLogicOp_68 = (res_ImpliesLogicOp_68 && res_AndLogicOP_80);
    }
    res_AndLogicOP_67 = (res_AndLogicOP_67 && res_ImpliesLogicOp_68);
    bool res_OrLogicOP_272 = false;
    bool res_OrLogicOP_273 = false;
    bool res_OrLogicOP_274 = false;
    bool res_AndLogicOP_275 = true;
    bool res_AndLogicOP_276 = true;
    bool res_NotLogicOP_277 = true;
    res_NotLogicOP_277 = (res_NotLogicOP_277 && ! Timer_Attivo(L_P1__GetMainc48(my_id)));
    res_AndLogicOP_276 = (res_AndLogicOP_276 && res_NotLogicOP_277);
    bool res_NotLogicOP_278 = true;
    res_NotLogicOP_278 = (res_NotLogicOP_278 && ! (Counter_GetValore(L_P1__GetMainc51(my_id)) > 134u));
    res_AndLogicOP_276 = (res_AndLogicOP_276 && res_NotLogicOP_278);
    
    res_AndLogicOP_275 = (res_AndLogicOP_275 && res_AndLogicOP_276);
    bool res_NotLogicOP_279 = true;
    res_NotLogicOP_279 = (res_NotLogicOP_279 && ! (L_P1__GetMainc33(my_id) == rossogiallo));
    res_AndLogicOP_275 = (res_AndLogicOP_275 && res_NotLogicOP_279);
    
    res_OrLogicOP_274 = (res_OrLogicOP_274 || res_AndLogicOP_275);
    bool res_NotLogicOP_280 = true;
    res_NotLogicOP_280 = (res_NotLogicOP_280 && ! (L_P1__GetInMainc5(my_id) == false));
    res_OrLogicOP_274 = (res_OrLogicOP_274 || res_NotLogicOP_280);
    
    res_OrLogicOP_273 = (res_OrLogicOP_273 || res_OrLogicOP_274);
    res_OrLogicOP_273 = (res_OrLogicOP_273 || (L_P1__GetInMainc4(my_id) == c180x));
    
    res_OrLogicOP_272 = (res_OrLogicOP_272 || res_OrLogicOP_273);
    res_OrLogicOP_272 = (res_OrLogicOP_272 || Timer_Disattivo(L_P1__GetMainc48(my_id)));
    
    res_AndLogicOP_67 = (res_AndLogicOP_67 && res_OrLogicOP_272);
    
    res_ImpliesLogicOp_61 = (res_ImpliesLogicOp_61 && res_AndLogicOP_67);
    }
    res_AndLogicOP_60 = (res_AndLogicOP_60 && res_ImpliesLogicOp_61);
    bool res_OrLogicOP_281 = false;
    bool res_OrLogicOP_282 = false;
    bool res_AndLogicOP_283 = true;
    bool res_AndLogicOP_284 = true;
    bool res_NotLogicOP_285 = true;
    res_NotLogicOP_285 = (res_NotLogicOP_285 && ! (L_P1__GetInMainc3(my_id) == false));
    res_AndLogicOP_284 = (res_AndLogicOP_284 && res_NotLogicOP_285);
    bool res_NotLogicOP_286 = true;
    res_NotLogicOP_286 = (res_NotLogicOP_286 && ! (L_P1__GetMainc33(my_id) == rossogiallo));
    res_AndLogicOP_284 = (res_AndLogicOP_284 && res_NotLogicOP_286);
    
    res_AndLogicOP_283 = (res_AndLogicOP_283 && res_AndLogicOP_284);
    bool res_NotLogicOP_287 = true;
    bool res_NotLogicOP_288 = true;
    res_NotLogicOP_288 = (res_NotLogicOP_288 && ! (Counter_GetValore(L_P1__GetMainc49(my_id)) == 1131u));
    res_NotLogicOP_287 = (res_NotLogicOP_287 && ! res_NotLogicOP_288);
    res_AndLogicOP_283 = (res_AndLogicOP_283 && res_NotLogicOP_287);
    
    res_OrLogicOP_282 = (res_OrLogicOP_282 || res_AndLogicOP_283);
    bool res_NotLogicOP_289 = true;
    res_NotLogicOP_289 = (res_NotLogicOP_289 && ! (L_P1__GetInMainc3(my_id) == false));
    res_OrLogicOP_282 = (res_OrLogicOP_282 || res_NotLogicOP_289);
    
    res_OrLogicOP_281 = (res_OrLogicOP_281 || res_OrLogicOP_282);
    bool res_AndLogicOP_290 = true;
    bool res_NotLogicOP_291 = true;
    res_NotLogicOP_291 = (res_NotLogicOP_291 && ! (L_P1__GetInMainc5(my_id) == true));
    res_AndLogicOP_290 = (res_AndLogicOP_290 && res_NotLogicOP_291);
    res_AndLogicOP_290 = (res_AndLogicOP_290 && (L_P1__GetInMainc3(my_id) == false));
    
    res_OrLogicOP_281 = (res_OrLogicOP_281 || res_AndLogicOP_290);
    
    res_AndLogicOP_60 = (res_AndLogicOP_60 && res_OrLogicOP_281);
    
    res_ImpliesLogicOp_57 = (res_ImpliesLogicOp_57 && res_AndLogicOP_60);
    }
    if(res_ImpliesLogicOp_57){
    xorIndex_res_XorLogicOP_56 = (xorIndex_res_XorLogicOP_56 + 1);
    }
    bool res_OrLogicOP_292 = false;
    bool res_OrLogicOP_293 = false;
    bool res_OrLogicOP_294 = false;
    res_OrLogicOP_294 = (res_OrLogicOP_294 || (Counter_GetValore(L_P1__GetMainc50(my_id)) > 13u));
    res_OrLogicOP_294 = (res_OrLogicOP_294 || (L_P1__GetParamMainc9(my_id) > 8u));
    
    res_OrLogicOP_293 = (res_OrLogicOP_293 || res_OrLogicOP_294);
    bool res_NotLogicOP_295 = true;
    res_NotLogicOP_295 = (res_NotLogicOP_295 && ! (argom26 == true));
    res_OrLogicOP_293 = (res_OrLogicOP_293 || res_NotLogicOP_295);
    
    res_OrLogicOP_292 = (res_OrLogicOP_292 || res_OrLogicOP_293);
    bool res_NotLogicOP_296 = true;
    res_NotLogicOP_296 = (res_NotLogicOP_296 && ! (L_P1__GetInMainc3(my_id) == false));
    res_OrLogicOP_292 = (res_OrLogicOP_292 || res_NotLogicOP_296);
    
    if(res_OrLogicOP_292){
    xorIndex_res_XorLogicOP_56 = (xorIndex_res_XorLogicOP_56 + 1);
    }
    
    res_XorLogicOP_56 = (res_XorLogicOP_56 && (xorIndex_res_XorLogicOP_56 == 1));
    res_ImpliesLogicOp_45 = (res_ImpliesLogicOp_45 && res_XorLogicOP_56);
    }
    res_AndLogicOP_44 = (res_AndLogicOP_44 && res_ImpliesLogicOp_45);
    bool res_OrLogicOP_297 = false;
    bool res_OrLogicOP_298 = false;
    res_OrLogicOP_298 = (res_OrLogicOP_298 || (L_P1__GetParamMainc8(my_id) == true));
    res_OrLogicOP_298 = (res_OrLogicOP_298 || (argom25 == false));
    
    res_OrLogicOP_297 = (res_OrLogicOP_297 || res_OrLogicOP_298);
    bool res_AndLogicOP_299 = true;
    bool res_AndLogicOP_300 = true;
    bool res_AndLogicOP_301 = true;
    res_AndLogicOP_301 = (res_AndLogicOP_301 && Timer_Disattivo(L_P1__GetMainc47(my_id)));
    bool res_NotLogicOP_302 = true;
    bool res_NotLogicOP_303 = true;
    res_NotLogicOP_303 = (res_NotLogicOP_303 && ! (L_P1__GetInMainc3(my_id) == true));
    res_NotLogicOP_302 = (res_NotLogicOP_302 && ! res_NotLogicOP_303);
    res_AndLogicOP_301 = (res_AndLogicOP_301 && res_NotLogicOP_302);
    
    res_AndLogicOP_300 = (res_AndLogicOP_300 && res_AndLogicOP_301);
    bool res_NotLogicOP_304 = true;
    res_NotLogicOP_304 = (res_NotLogicOP_304 && ! Timer_Disattivo(L_P1__GetMainc48(my_id)));
    res_AndLogicOP_300 = (res_AndLogicOP_300 && res_NotLogicOP_304);
    
    res_AndLogicOP_299 = (res_AndLogicOP_299 && res_AndLogicOP_300);
    bool res_NotLogicOP_305 = true;
    res_NotLogicOP_305 = (res_NotLogicOP_305 && ! (L_P1__GetParamMainc7(my_id) == 4u));
    res_AndLogicOP_299 = (res_AndLogicOP_299 && res_NotLogicOP_305);
    
    res_OrLogicOP_297 = (res_OrLogicOP_297 || res_AndLogicOP_299);
    
    res_AndLogicOP_44 = (res_AndLogicOP_44 && res_OrLogicOP_297);
    
    res_ImpliesLogicOp_40 = (res_ImpliesLogicOp_40 && res_AndLogicOP_44);
    }
    if(res_ImpliesLogicOp_40){
    xorIndex_res_XorLogicOP_39 = (xorIndex_res_XorLogicOP_39 + 1);
    }
    bool res_NotLogicOP_306 = true;
    res_NotLogicOP_306 = (res_NotLogicOP_306 && ! (L_P1__GetInMainc2(my_id) == rossogiallo));
    if(res_NotLogicOP_306){
    xorIndex_res_XorLogicOP_39 = (xorIndex_res_XorLogicOP_39 + 1);
    }
    
    res_XorLogicOP_39 = (res_XorLogicOP_39 && (xorIndex_res_XorLogicOP_39 == 1));
    res_ImpliesLogicOp_36 = (res_ImpliesLogicOp_36 && res_XorLogicOP_39);
    }
    res_AndLogicOP_35 = (res_AndLogicOP_35 && res_ImpliesLogicOp_36);
    res_AndLogicOP_35 = (res_AndLogicOP_35 && (L_P1__GetMainc33(my_id) == rossogiallo));
    
    res_ImpliesLogicOp_31 = (res_ImpliesLogicOp_31 && res_AndLogicOP_35);
    }
    if(res_ImpliesLogicOp_31){
    xorIndex_res_XorLogicOP_30 = (xorIndex_res_XorLogicOP_30 + 1);
    }
    bool res_OrLogicOP_307 = false;
    bool res_OrLogicOP_308 = false;
    bool res_OrLogicOP_309 = false;
    res_OrLogicOP_309 = (res_OrLogicOP_309 || (L_P1__GetParamMainc7(my_id) == 5u));
    bool res_NotLogicOP_310 = true;
    bool res_NotLogicOP_311 = true;
    res_NotLogicOP_311 = (res_NotLogicOP_311 && ! (L_P1__GetInMainc3(my_id) == false));
    res_NotLogicOP_310 = (res_NotLogicOP_310 && ! res_NotLogicOP_311);
    res_OrLogicOP_309 = (res_OrLogicOP_309 || res_NotLogicOP_310);
    
    res_OrLogicOP_308 = (res_OrLogicOP_308 || res_OrLogicOP_309);
    bool res_AndLogicOP_312 = true;
    bool res_AndLogicOP_313 = true;
    bool res_NotLogicOP_314 = true;
    bool res_NotLogicOP_315 = true;
    res_NotLogicOP_315 = (res_NotLogicOP_315 && ! (L_P1__GetParamMainc8(my_id) == false));
    res_NotLogicOP_314 = (res_NotLogicOP_314 && ! res_NotLogicOP_315);
    res_AndLogicOP_313 = (res_AndLogicOP_313 && res_NotLogicOP_314);
    bool res_NotLogicOP_316 = true;
    res_NotLogicOP_316 = (res_NotLogicOP_316 && ! (L_P1__GetMainc33(my_id) == rossogiallo));
    res_AndLogicOP_313 = (res_AndLogicOP_313 && res_NotLogicOP_316);
    
    res_AndLogicOP_312 = (res_AndLogicOP_312 && res_AndLogicOP_313);
    bool res_NotLogicOP_317 = true;
    bool res_NotLogicOP_318 = true;
    res_NotLogicOP_318 = (res_NotLogicOP_318 && ! (L_P1__GetMainc32(my_id) == false));
    res_NotLogicOP_317 = (res_NotLogicOP_317 && ! res_NotLogicOP_318);
    res_AndLogicOP_312 = (res_AndLogicOP_312 && res_NotLogicOP_317);
    
    res_OrLogicOP_308 = (res_OrLogicOP_308 || res_AndLogicOP_312);
    
    res_OrLogicOP_307 = (res_OrLogicOP_307 || res_OrLogicOP_308);
    res_OrLogicOP_307 = (res_OrLogicOP_307 || (argom23 == rossogiallo));
    
    if(res_OrLogicOP_307){
    xorIndex_res_XorLogicOP_30 = (xorIndex_res_XorLogicOP_30 + 1);
    }
    
    res_XorLogicOP_30 = (res_XorLogicOP_30 && (xorIndex_res_XorLogicOP_30 == 1));
    res_ImpliesLogicOp_18 = (res_ImpliesLogicOp_18 && res_XorLogicOP_30);
    }
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_ImpliesLogicOp_18);
    bool res_OrLogicOP_319 = false;
    bool res_OrLogicOP_320 = false;
    bool res_NotLogicOP_321 = true;
    res_NotLogicOP_321 = (res_NotLogicOP_321 && ! (L_P1__GetInMainc3(my_id) == true));
    res_OrLogicOP_320 = (res_OrLogicOP_320 || res_NotLogicOP_321);
    res_OrLogicOP_320 = (res_OrLogicOP_320 || (L_P1__GetInMainc3(my_id) == false));
    
    res_OrLogicOP_319 = (res_OrLogicOP_319 || res_OrLogicOP_320);
    bool res_AndLogicOP_322 = true;
    bool res_AndLogicOP_323 = true;
    bool res_NotLogicOP_324 = true;
    res_NotLogicOP_324 = (res_NotLogicOP_324 && ! (L_P1__GetMainc32(my_id) == true));
    res_AndLogicOP_323 = (res_AndLogicOP_323 && res_NotLogicOP_324);
    bool res_NotLogicOP_325 = true;
    bool res_NotLogicOP_326 = true;
    res_NotLogicOP_326 = (res_NotLogicOP_326 && ! (L_P1__GetInMainc4(my_id) == c180x));
    res_NotLogicOP_325 = (res_NotLogicOP_325 && ! res_NotLogicOP_326);
    res_AndLogicOP_323 = (res_AndLogicOP_323 && res_NotLogicOP_325);
    
    res_AndLogicOP_322 = (res_AndLogicOP_322 && res_AndLogicOP_323);
    bool res_NotLogicOP_327 = true;
    res_NotLogicOP_327 = (res_NotLogicOP_327 && ! (L_P1__GetParamMainc7(my_id) == 10u));
    res_AndLogicOP_322 = (res_AndLogicOP_322 && res_NotLogicOP_327);
    
    res_OrLogicOP_319 = (res_OrLogicOP_319 || res_AndLogicOP_322);
    
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_OrLogicOP_319);
    
    res_ImpliesLogicOp_6 = (res_ImpliesLogicOp_6 && res_AndLogicOP_17);
    }
    if(res_ImpliesLogicOp_6){
    xorIndex_res_XorLogicOP_5 = (xorIndex_res_XorLogicOP_5 + 1);
    }
    bool res_OrLogicOP_328 = false;
    bool res_OrLogicOP_329 = false;
    bool res_OrLogicOP_330 = false;
    bool res_OrLogicOP_331 = false;
    bool res_NotLogicOP_332 = true;
    res_NotLogicOP_332 = (res_NotLogicOP_332 && ! (L_P1__GetParamMainc8(my_id) == true));
    res_OrLogicOP_331 = (res_OrLogicOP_331 || res_NotLogicOP_332);
    res_OrLogicOP_331 = (res_OrLogicOP_331 || (argom25 == true));
    
    res_OrLogicOP_330 = (res_OrLogicOP_330 || res_OrLogicOP_331);
    bool res_NotLogicOP_333 = true;
    res_NotLogicOP_333 = (res_NotLogicOP_333 && ! Timer_Attivo(L_P1__GetMainc46(my_id)));
    res_OrLogicOP_330 = (res_OrLogicOP_330 || res_NotLogicOP_333);
    
    res_OrLogicOP_329 = (res_OrLogicOP_329 || res_OrLogicOP_330);
    bool res_NotLogicOP_334 = true;
    res_NotLogicOP_334 = (res_NotLogicOP_334 && ! (Counter_GetValore(L_P1__GetMainc50(my_id)) == 1520u));
    res_OrLogicOP_329 = (res_OrLogicOP_329 || res_NotLogicOP_334);
    
    res_OrLogicOP_328 = (res_OrLogicOP_328 || res_OrLogicOP_329);
    bool res_AndLogicOP_335 = true;
    bool res_NotLogicOP_336 = true;
    res_NotLogicOP_336 = (res_NotLogicOP_336 && ! (L_P1__GetParamMainc7(my_id) == 9u));
    res_AndLogicOP_335 = (res_AndLogicOP_335 && res_NotLogicOP_336);
    bool res_NotLogicOP_337 = true;
    res_NotLogicOP_337 = (res_NotLogicOP_337 && ! Timer_Disattivo(L_P1__GetMainc46(my_id)));
    res_AndLogicOP_335 = (res_AndLogicOP_335 && res_NotLogicOP_337);
    
    res_OrLogicOP_328 = (res_OrLogicOP_328 || res_AndLogicOP_335);
    
    if(res_OrLogicOP_328){
    xorIndex_res_XorLogicOP_5 = (xorIndex_res_XorLogicOP_5 + 1);
    }
    
    res_XorLogicOP_5 = (res_XorLogicOP_5 && (xorIndex_res_XorLogicOP_5 == 1));
    res_ImpliesLogicOp_3 = (res_ImpliesLogicOp_3 && res_XorLogicOP_5);
    }
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_ImpliesLogicOp_3);
    bool res_NotLogicOP_338 = true;
    res_NotLogicOP_338 = (res_NotLogicOP_338 && ! (L_P1__GetMainc33(my_id) == rossogiallo));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_338);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_AndLogicOP_2);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *47,50,52,*   l'argomento argomento_ave9 non  sia  uguale a  False  *,* 
    //   *104,* e  che   l'argomento argomento_ave7 non  sia  uguale a  True  *39,* 
    //   *104,* o  che  *34,*  il parametro MainClass_C1_parametro_P10 non sia  uguale a  False 
    //   *104,* o  che  *,*  la variabile MainClass_C1_variabile_V4 non sia  diverso da RossoGiallo
    bool res_OrLogicOP_339 = false;
    bool res_OrLogicOP_340 = false;
    bool res_AndLogicOP_341 = true;
    bool res_NotLogicOP_342 = true;
    res_NotLogicOP_342 = (res_NotLogicOP_342 && ! (argom26 == false));
    res_AndLogicOP_341 = (res_AndLogicOP_341 && res_NotLogicOP_342);
    bool res_NotLogicOP_343 = true;
    res_NotLogicOP_343 = (res_NotLogicOP_343 && ! (argom25 == true));
    res_AndLogicOP_341 = (res_AndLogicOP_341 && res_NotLogicOP_343);
    
    res_OrLogicOP_340 = (res_OrLogicOP_340 || res_AndLogicOP_341);
    bool res_NotLogicOP_344 = true;
    res_NotLogicOP_344 = (res_NotLogicOP_344 && ! (L_P1__GetParamMainc8(my_id) == false));
    res_OrLogicOP_340 = (res_OrLogicOP_340 || res_NotLogicOP_344);
    
    res_OrLogicOP_339 = (res_OrLogicOP_339 || res_OrLogicOP_340);
    bool res_NotLogicOP_345 = true;
    bool res_NotLogicOP_346 = true;
    res_NotLogicOP_346 = (res_NotLogicOP_346 && ! (L_P1__GetMainc33(my_id) == rossogiallo));
    res_NotLogicOP_345 = (res_NotLogicOP_345 && ! res_NotLogicOP_346);
    res_OrLogicOP_339 = (res_OrLogicOP_339 || res_NotLogicOP_345);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_339);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
    
    { commento: {62,} commento: {34,}  se lo stato  non è  diverso da  commento: {56,}  state1  commento: {106,} commento: {35,} o  se il controllo MainClass_C1_controllo_C10 è  uguale a  True  commento: {36,} e  se il timer MainClass_C1_timer_T1 non è attivo, Almeno una delle seguenti { 
     commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI2 è disattivo commento: {38,} e  se il contatore MainClass_C1_contatore_Co10 è  uguale a  commento: {53,} 15431, Verifica che   commento: {48,49,50,}  commento: {,}  il timer MainClass_C1_timer_T7 sia scaduto
     commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C7 sia  diverso da  True 
     commento: {104,} o  che  commento: {35,}  il controllo MainClass_C1_controllo_C1 sia  uguale a RossoGiallo
     commento: {104,} e  che  commento: {35,}  il controllo MainClass_C1_controllo_C10 non sia  uguale a  False 
     commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V4 non sia  diverso da RossoGiallo
     commento: {104,} o  che  commento: {37,}  la variabile MainClass_C1_variabile_V3 sia  uguale a  True 
    
    
     } Verifica che   commento: {47,50,51,}  commento: {,}  il contatore MainClass_C1_contatore_Co1 non sia  diverso da  commento: {56,} 11
     commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V5 sia  minore di  commento: {55,} 2
     commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P1 sia  uguale a  commento: {53,} 4
    
    
    }
*/
bool L_P1__Macro9(instance_id_t const my_id , C1_Enumerat1 argom27, bool argom28, C1_Enumerat4 argom29, C1_Enumerat3 argom30, C1_Enumerat3 argom31, bool argom32, C1_Enumerat1 argom33)
{
bool res_AndLogicOP_0 = true;
    
    //  *62,* *34,*  se lo stato  non è  diverso da  *56,*  state1  *106,* *35,* o  se il controllo MainClass_C1_controllo_C10 è  uguale a  True  *36,* e  se il timer MainClass_C1_timer_T1 non è attivo, Almeno una delle seguenti { 
    //   *110,*  se il ripristino del timer  MainClass_C1_restoreTI_TI2 è disattivo *38,* e  se il contatore MainClass_C1_contatore_Co10 è  uguale a  *53,* 15431, Verifica che   *48,49,50,*  *,*  il timer MainClass_C1_timer_T7 sia scaduto
    //   *104,* o  che  *,*  il controllo MainClass_C1_controllo_C7 sia  diverso da  True 
    //   *104,* o  che  *35,*  il controllo MainClass_C1_controllo_C1 sia  uguale a RossoGiallo
    //   *104,* e  che  *35,*  il controllo MainClass_C1_controllo_C10 non sia  uguale a  False 
    //   *104,* o  che  *,*  la variabile MainClass_C1_variabile_V4 non sia  diverso da RossoGiallo
    //   *104,* o  che  *37,*  la variabile MainClass_C1_variabile_V3 sia  uguale a  True 
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_NotLogicOP_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1_C1_GetState(my_id) == C1_St_state));
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! res_NotLogicOP_4);
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_3);
    bool res_AndLogicOP_5 = true;
    res_AndLogicOP_5 = (res_AndLogicOP_5 && (L_P1__GetInMainc3(my_id) == true));
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! Timer_Attivo(L_P1__GetMainc46(my_id)));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_6);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_5);
    
    if(res_OrLogicOP_2){
    bool res_ImpliesLogicOp_7 = true;
    bool res_AndLogicOP_8 = true;
    res_AndLogicOP_8 = (res_AndLogicOP_8 && Timer_Disattivo(L_P1__GetMainc39(my_id)));
    res_AndLogicOP_8 = (res_AndLogicOP_8 && (Counter_GetValore(L_P1__GetMainc50(my_id)) == 15431u));
    
    if(res_AndLogicOP_8){
    bool res_OrLogicOP_9 = false;
    bool res_OrLogicOP_10 = false;
    bool res_OrLogicOP_11 = false;
    bool res_OrLogicOP_12 = false;
    res_OrLogicOP_12 = (res_OrLogicOP_12 || Timer_Scaduto(L_P1__GetMainc48(my_id)));
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (L_P1__GetInMainc5(my_id) == true));
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_NotLogicOP_13);
    
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_OrLogicOP_12);
    bool res_AndLogicOP_14 = true;
    res_AndLogicOP_14 = (res_AndLogicOP_14 && (L_P1__GetInMainc2(my_id) == rossogiallo));
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (L_P1__GetInMainc3(my_id) == false));
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_NotLogicOP_15);
    
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_AndLogicOP_14);
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_OrLogicOP_11);
    bool res_NotLogicOP_16 = true;
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! (L_P1__GetMainc33(my_id) == rossogiallo));
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! res_NotLogicOP_17);
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_NotLogicOP_16);
    
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_OrLogicOP_10);
    res_OrLogicOP_9 = (res_OrLogicOP_9 || (L_P1__GetMainc32(my_id) == true));
    
    res_ImpliesLogicOp_7 = (res_ImpliesLogicOp_7 && res_OrLogicOP_9);
    }
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_ImpliesLogicOp_7);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *47,50,51,*  *,*  il contatore MainClass_C1_contatore_Co1 non sia  diverso da  *56,* 11
    //   *104,* e  che  *,*  la variabile MainClass_C1_variabile_V5 sia  minore di  *55,* 2
    //   *104,* o  che  *34,*  il parametro MainClass_C1_parametro_P1 sia  uguale a  *53,* 4
    bool res_OrLogicOP_18 = false;
    bool res_AndLogicOP_19 = true;
    bool res_NotLogicOP_20 = true;
    bool res_NotLogicOP_21 = true;
    res_NotLogicOP_21 = (res_NotLogicOP_21 && ! (Counter_GetValore(L_P1__GetMainc49(my_id)) == 11u));
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! res_NotLogicOP_21);
    res_AndLogicOP_19 = (res_AndLogicOP_19 && res_NotLogicOP_20);
    res_AndLogicOP_19 = (res_AndLogicOP_19 && (L_P1__GetMainc34(my_id) < 2u));
    
    res_OrLogicOP_18 = (res_OrLogicOP_18 || res_AndLogicOP_19);
    res_OrLogicOP_18 = (res_OrLogicOP_18 || (L_P1__GetParamMainc7(my_id) == 4u));
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_18);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
    
    { commento: {61,} commento: {35,}  se il controllo MainClass_C1_controllo_C10 è  uguale a  False  commento: {35,} e  se il controllo MainClass_C1_controllo_C1 non è  diverso da RossoGiallo, Tutte le seguenti { 
     commento: {61,}  se l'argomento argomento_ave6 non  è  diverso da  True  commento: {39,}  o  se l'argomento argomento_ave1 è  uguale a  False  commento: {39,}  commento: {34,} o  se il parametro MainClass_C1_parametro_P1 non è  maggiore di  commento: {54,} 3 commento: {36,} o  se il timer MainClass_C1_timer_T7 è scaduto, Tutte le seguenti { 
     commento: {62,} commento: {34,}  se il parametro MainClass_C1_parametro_P9 è  uguale a  commento: {53,} 9 commento: {36,} o  se il timer MainClass_C1_timer_T1 è disattivo e  se l'argomento argomento_ave1 è  uguale a  True  commento: {39,}  e  se l'argomento argomento_ave1 è  diverso da  True  commento: {39,}  commento: {35,} e  se il controllo MainClass_C1_controllo_C1 non è  uguale a RossoGiallo, Almeno una delle seguenti { 
     commento: {61,}  se il ripristino dello stato  non è  diverso da  commento: {56,}  state1  commento: {107,} o  se l'argomento argomento_ave1 è  diverso da  False  commento: {39,}  commento: {35,} e  se il controllo MainClass_C1_controllo_C1 non è  diverso da RossoGiallo, Tutte le seguenti { 
     commento: {62,}  se il ripristino dello stato  non è  diverso da  commento: {56,}  state1  commento: {107,} e  se l'argomento argomento_ave1 è  uguale a  True  commento: {39,}  commento: {34,} e  se il parametro MainClass_C1_parametro_P1 non è  uguale a  commento: {53,} 5 e  se l'argomento argomento_ave10 è  diverso da RossoGiallo commento: {39,}  commento: {34,} o  se il parametro MainClass_C1_parametro_P10 è  uguale a  False , Almeno una delle seguenti { 
     commento: {62,} commento: {34,}  se il parametro MainClass_C1_parametro_P1 è  minore di  commento: {55,} 7 commento: {34,} o  se il parametro MainClass_C1_parametro_P10 non è  uguale a  True  commento: {36,} o  se il timer MainClass_C1_timer_T7 è disattivo commento: {38,} o  se il contatore MainClass_C1_contatore_Co1 non è  maggiore di  commento: {54,} 154, Almeno una delle seguenti { 
     commento: {62,} commento: {36,}  se il timer MainClass_C1_timer_T6 non è disattivo e  se l'argomento argomento_ave1 non  è  uguale a  False  commento: {39,}  commento: {38,} o  se il contatore MainClass_C1_contatore_Co2 non è  minore di  commento: {55,} 11312 commento: {37,} o  se la variabile MainClass_C1_variabile_V5 non è  maggiore di  commento: {54,} 1, Almeno una delle seguenti { 
     commento: {34,}  se lo stato  non è  diverso da  commento: {56,}  state1  commento: {106,} commento: {38,} e  se il contatore MainClass_C1_contatore_Co1 non è  diverso da  commento: {56,} 11054 e  se l'argomento argomento_ave1 non  è  uguale a  True  commento: {39,}  commento: {38,} o  se il contatore MainClass_C1_contatore_Co2 è  diverso da  commento: {56,} 1531 commento: {37,} o  se la variabile MainClass_C1_variabile_V6 non è  diverso da  True , Verifica che   commento: {48,50,}  commento: {,}  il controllo MainClass_C1_controllo_C1 sia  uguale a RossoGiallo
     commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V4 non sia  uguale a RossoGiallo
    
    
     } Verifica che   commento: {47,48,50,52,}  commento: {34,}  il parametro MainClass_C1_parametro_P1 non sia  minore di  commento: {55,} 4
     commento: {104,} o  che   l'argomento argomento_ave1 sia  uguale a  False  commento: {,} 
     commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V4 sia  uguale a RossoGiallo
     commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P1 sia  uguale a  commento: {53,} 2
     commento: {104,} e  che   l'argomento argomento_ave10 non  sia  uguale a RossoGiallo commento: {39,} 
     commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C8 sia  uguale a c180x
    
    
     } Verifica che   commento: {48,49,52,}  commento: {,}  il timer MainClass_C1_timer_T1 non sia attivo
     commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C8 non sia  uguale a c180x
     commento: {104,} o  che   l'argomento argomento_ave1 non  sia  uguale a  True  commento: {,} 
    
    
     } Verifica che   commento: {49,50,}  commento: {,}  il timer MainClass_C1_timer_T1 sia disattivo
     commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V4 non sia  diverso da RossoGiallo
     commento: {104,} e  che  commento: {36,}  il timer MainClass_C1_timer_T7 sia attivo
     commento: {104,} o  che  commento: {37,}  la variabile MainClass_C1_variabile_V4 sia  uguale a RossoGiallo
    
    
     } Verifica che   commento: {47,48,50,}  commento: {,}  la variabile MainClass_C1_variabile_V5 non sia  minore di  commento: {55,} 6
     commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P9 non sia  minore di  commento: {55,} 5
     commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C10 sia  uguale a  True 
    
    
     } Verifica che   commento: {49,50,}  commento: {,}  la variabile MainClass_C1_variabile_V4 sia  diverso da RossoGiallo
     commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T6 non sia attivo
    
    
     } Verifica che   commento: {49,50,}  commento: {,}  la variabile MainClass_C1_variabile_V3 sia  uguale a  True 
     commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T1 sia disattivo
    
    
     } Verifica che   commento: {48,}  commento: {,}  il controllo MainClass_C1_controllo_C10 sia  uguale a  True 
    
    
    }
*/
bool L_P1__Macro10(instance_id_t const my_id , bool argom34, C1_Enumerat3 argom35, bool argom36)
{
bool res_AndLogicOP_0 = true;
    
    //  *61,* *35,*  se il controllo MainClass_C1_controllo_C10 è  uguale a  False  *35,* e  se il controllo MainClass_C1_controllo_C1 non è  diverso da RossoGiallo, Tutte le seguenti { 
    //   *61,*  se l'argomento argomento_ave6 non  è  diverso da  True  *39,*  o  se l'argomento argomento_ave1 è  uguale a  False  *39,*  *34,* o  se il parametro MainClass_C1_parametro_P1 non è  maggiore di  *54,* 3 *36,* o  se il timer MainClass_C1_timer_T7 è scaduto, Tutte le seguenti { 
    //   *62,* *34,*  se il parametro MainClass_C1_parametro_P9 è  uguale a  *53,* 9 *36,* o  se il timer MainClass_C1_timer_T1 è disattivo e  se l'argomento argomento_ave1 è  uguale a  True  *39,*  e  se l'argomento argomento_ave1 è  diverso da  True  *39,*  *35,* e  se il controllo MainClass_C1_controllo_C1 non è  uguale a RossoGiallo, Almeno una delle seguenti { 
    //   *61,*  se il ripristino dello stato  non è  diverso da  *56,*  state1  *107,* o  se l'argomento argomento_ave1 è  diverso da  False  *39,*  *35,* e  se il controllo MainClass_C1_controllo_C1 non è  diverso da RossoGiallo, Tutte le seguenti { 
    //   *62,*  se il ripristino dello stato  non è  diverso da  *56,*  state1  *107,* e  se l'argomento argomento_ave1 è  uguale a  True  *39,*  *34,* e  se il parametro MainClass_C1_parametro_P1 non è  uguale a  *53,* 5 e  se l'argomento argomento_ave10 è  diverso da RossoGiallo *39,*  *34,* o  se il parametro MainClass_C1_parametro_P10 è  uguale a  False , Almeno una delle seguenti { 
    //   *62,* *34,*  se il parametro MainClass_C1_parametro_P1 è  minore di  *55,* 7 *34,* o  se il parametro MainClass_C1_parametro_P10 non è  uguale a  True  *36,* o  se il timer MainClass_C1_timer_T7 è disattivo *38,* o  se il contatore MainClass_C1_contatore_Co1 non è  maggiore di  *54,* 154, Almeno una delle seguenti { 
    //   *62,* *36,*  se il timer MainClass_C1_timer_T6 non è disattivo e  se l'argomento argomento_ave1 non  è  uguale a  False  *39,*  *38,* o  se il contatore MainClass_C1_contatore_Co2 non è  minore di  *55,* 11312 *37,* o  se la variabile MainClass_C1_variabile_V5 non è  maggiore di  *54,* 1, Almeno una delle seguenti { 
    //   *34,*  se lo stato  non è  diverso da  *56,*  state1  *106,* *38,* e  se il contatore MainClass_C1_contatore_Co1 non è  diverso da  *56,* 11054 e  se l'argomento argomento_ave1 non  è  uguale a  True  *39,*  *38,* o  se il contatore MainClass_C1_contatore_Co2 è  diverso da  *56,* 1531 *37,* o  se la variabile MainClass_C1_variabile_V6 non è  diverso da  True , Verifica che   *48,50,*  *,*  il controllo MainClass_C1_controllo_C1 sia  uguale a RossoGiallo
    //   *104,* o  che  *,*  la variabile MainClass_C1_variabile_V4 non sia  uguale a RossoGiallo
    //   } Verifica che   *47,48,50,52,*  *34,*  il parametro MainClass_C1_parametro_P1 non sia  minore di  *55,* 4
    //   *104,* o  che   l'argomento argomento_ave1 sia  uguale a  False  *,* 
    //   *104,* o  che  *,*  la variabile MainClass_C1_variabile_V4 sia  uguale a RossoGiallo
    //   *104,* e  che  *34,*  il parametro MainClass_C1_parametro_P1 sia  uguale a  *53,* 2
    //   *104,* e  che   l'argomento argomento_ave10 non  sia  uguale a RossoGiallo *39,* 
    //   *104,* e  che  *,*  il controllo MainClass_C1_controllo_C8 sia  uguale a c180x
    //   } Verifica che   *48,49,52,*  *,*  il timer MainClass_C1_timer_T1 non sia attivo
    //   *104,* e  che  *,*  il controllo MainClass_C1_controllo_C8 non sia  uguale a c180x
    //   *104,* o  che   l'argomento argomento_ave1 non  sia  uguale a  True  *,* 
    //   } Verifica che   *49,50,*  *,*  il timer MainClass_C1_timer_T1 sia disattivo
    //   *104,* o  che  *,*  la variabile MainClass_C1_variabile_V4 non sia  diverso da RossoGiallo
    //   *104,* e  che  *36,*  il timer MainClass_C1_timer_T7 sia attivo
    //   *104,* o  che  *37,*  la variabile MainClass_C1_variabile_V4 sia  uguale a RossoGiallo
    //   } Verifica che   *47,48,50,*  *,*  la variabile MainClass_C1_variabile_V5 non sia  minore di  *55,* 6
    //   *104,* o  che  *34,*  il parametro MainClass_C1_parametro_P9 non sia  minore di  *55,* 5
    //   *104,* o  che  *,*  il controllo MainClass_C1_controllo_C10 sia  uguale a  True 
    //   } Verifica che   *49,50,*  *,*  la variabile MainClass_C1_variabile_V4 sia  diverso da RossoGiallo
    //   *104,* o  che  *,*  il timer MainClass_C1_timer_T6 non sia attivo
    //   } Verifica che   *49,50,*  *,*  la variabile MainClass_C1_variabile_V3 sia  uguale a  True 
    //   *104,* e  che  *,*  il timer MainClass_C1_timer_T1 sia disattivo
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_AndLogicOP_2 = true;
    res_AndLogicOP_2 = (res_AndLogicOP_2 && (L_P1__GetInMainc3(my_id) == false));
    bool res_NotLogicOP_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetInMainc2(my_id) == rossogiallo));
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! res_NotLogicOP_4);
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_3);
    
    if(res_AndLogicOP_2){
    bool res_AndLogicOP_5 = true;
    bool res_ImpliesLogicOp_6 = true;
    bool res_OrLogicOP_7 = false;
    bool res_OrLogicOP_8 = false;
    bool res_OrLogicOP_9 = false;
    bool res_NotLogicOP_10 = true;
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (argom36 == true));
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! res_NotLogicOP_11);
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_NotLogicOP_10);
    res_OrLogicOP_9 = (res_OrLogicOP_9 || (argom34 == false));
    
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_OrLogicOP_9);
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (L_P1__GetParamMainc7(my_id) > 3u));
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_NotLogicOP_12);
    
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_OrLogicOP_8);
    res_OrLogicOP_7 = (res_OrLogicOP_7 || Timer_Scaduto(L_P1__GetMainc48(my_id)));
    
    if(res_OrLogicOP_7){
    bool res_AndLogicOP_13 = true;
    bool res_ImpliesLogicOp_14 = true;
    bool res_OrLogicOP_15 = false;
    res_OrLogicOP_15 = (res_OrLogicOP_15 || (L_P1__GetParamMainc9(my_id) == 9u));
    bool res_AndLogicOP_16 = true;
    bool res_AndLogicOP_17 = true;
    bool res_AndLogicOP_18 = true;
    res_AndLogicOP_18 = (res_AndLogicOP_18 && Timer_Disattivo(L_P1__GetMainc46(my_id)));
    res_AndLogicOP_18 = (res_AndLogicOP_18 && (argom34 == true));
    
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_AndLogicOP_18);
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (argom34 == true));
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_NotLogicOP_19);
    
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_AndLogicOP_17);
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! (L_P1__GetInMainc2(my_id) == rossogiallo));
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_NotLogicOP_20);
    
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_AndLogicOP_16);
    
    if(res_OrLogicOP_15){
    bool res_OrLogicOP_21 = false;
    bool res_ImpliesLogicOp_22 = true;
    bool res_OrLogicOP_23 = false;
    bool res_NotLogicOP_24 = true;
    bool res_NotLogicOP_25 = true;
    res_NotLogicOP_25 = (res_NotLogicOP_25 && ! (L_P1__GetStato1(my_id) == C1_St_state));
    res_NotLogicOP_24 = (res_NotLogicOP_24 && ! res_NotLogicOP_25);
    res_OrLogicOP_23 = (res_OrLogicOP_23 || res_NotLogicOP_24);
    bool res_AndLogicOP_26 = true;
    bool res_NotLogicOP_27 = true;
    res_NotLogicOP_27 = (res_NotLogicOP_27 && ! (argom34 == false));
    res_AndLogicOP_26 = (res_AndLogicOP_26 && res_NotLogicOP_27);
    bool res_NotLogicOP_28 = true;
    bool res_NotLogicOP_29 = true;
    res_NotLogicOP_29 = (res_NotLogicOP_29 && ! (L_P1__GetInMainc2(my_id) == rossogiallo));
    res_NotLogicOP_28 = (res_NotLogicOP_28 && ! res_NotLogicOP_29);
    res_AndLogicOP_26 = (res_AndLogicOP_26 && res_NotLogicOP_28);
    
    res_OrLogicOP_23 = (res_OrLogicOP_23 || res_AndLogicOP_26);
    
    if(res_OrLogicOP_23){
    bool res_AndLogicOP_30 = true;
    bool res_ImpliesLogicOp_31 = true;
    bool res_OrLogicOP_32 = false;
    bool res_AndLogicOP_33 = true;
    bool res_AndLogicOP_34 = true;
    bool res_AndLogicOP_35 = true;
    bool res_NotLogicOP_36 = true;
    bool res_NotLogicOP_37 = true;
    res_NotLogicOP_37 = (res_NotLogicOP_37 && ! (L_P1__GetStato1(my_id) == C1_St_state));
    res_NotLogicOP_36 = (res_NotLogicOP_36 && ! res_NotLogicOP_37);
    res_AndLogicOP_35 = (res_AndLogicOP_35 && res_NotLogicOP_36);
    res_AndLogicOP_35 = (res_AndLogicOP_35 && (argom34 == true));
    
    res_AndLogicOP_34 = (res_AndLogicOP_34 && res_AndLogicOP_35);
    bool res_NotLogicOP_38 = true;
    res_NotLogicOP_38 = (res_NotLogicOP_38 && ! (L_P1__GetParamMainc7(my_id) == 5u));
    res_AndLogicOP_34 = (res_AndLogicOP_34 && res_NotLogicOP_38);
    
    res_AndLogicOP_33 = (res_AndLogicOP_33 && res_AndLogicOP_34);
    bool res_NotLogicOP_39 = true;
    res_NotLogicOP_39 = (res_NotLogicOP_39 && ! (argom35 == rossogiallo));
    res_AndLogicOP_33 = (res_AndLogicOP_33 && res_NotLogicOP_39);
    
    res_OrLogicOP_32 = (res_OrLogicOP_32 || res_AndLogicOP_33);
    res_OrLogicOP_32 = (res_OrLogicOP_32 || (L_P1__GetParamMainc8(my_id) == false));
    
    if(res_OrLogicOP_32){
    bool res_OrLogicOP_40 = false;
    bool res_ImpliesLogicOp_41 = true;
    bool res_OrLogicOP_42 = false;
    bool res_OrLogicOP_43 = false;
    bool res_OrLogicOP_44 = false;
    res_OrLogicOP_44 = (res_OrLogicOP_44 || (L_P1__GetParamMainc7(my_id) < 7u));
    bool res_NotLogicOP_45 = true;
    res_NotLogicOP_45 = (res_NotLogicOP_45 && ! (L_P1__GetParamMainc8(my_id) == true));
    res_OrLogicOP_44 = (res_OrLogicOP_44 || res_NotLogicOP_45);
    
    res_OrLogicOP_43 = (res_OrLogicOP_43 || res_OrLogicOP_44);
    res_OrLogicOP_43 = (res_OrLogicOP_43 || Timer_Disattivo(L_P1__GetMainc48(my_id)));
    
    res_OrLogicOP_42 = (res_OrLogicOP_42 || res_OrLogicOP_43);
    bool res_NotLogicOP_46 = true;
    res_NotLogicOP_46 = (res_NotLogicOP_46 && ! (Counter_GetValore(L_P1__GetMainc49(my_id)) > 154u));
    res_OrLogicOP_42 = (res_OrLogicOP_42 || res_NotLogicOP_46);
    
    if(res_OrLogicOP_42){
    bool res_OrLogicOP_47 = false;
    bool res_ImpliesLogicOp_48 = true;
    bool res_OrLogicOP_49 = false;
    bool res_OrLogicOP_50 = false;
    bool res_AndLogicOP_51 = true;
    bool res_NotLogicOP_52 = true;
    res_NotLogicOP_52 = (res_NotLogicOP_52 && ! Timer_Disattivo(L_P1__GetMainc47(my_id)));
    res_AndLogicOP_51 = (res_AndLogicOP_51 && res_NotLogicOP_52);
    bool res_NotLogicOP_53 = true;
    res_NotLogicOP_53 = (res_NotLogicOP_53 && ! (argom34 == false));
    res_AndLogicOP_51 = (res_AndLogicOP_51 && res_NotLogicOP_53);
    
    res_OrLogicOP_50 = (res_OrLogicOP_50 || res_AndLogicOP_51);
    bool res_NotLogicOP_54 = true;
    res_NotLogicOP_54 = (res_NotLogicOP_54 && ! (Counter_GetValore(L_P1__GetMainc51(my_id)) < 11312u));
    res_OrLogicOP_50 = (res_OrLogicOP_50 || res_NotLogicOP_54);
    
    res_OrLogicOP_49 = (res_OrLogicOP_49 || res_OrLogicOP_50);
    bool res_NotLogicOP_55 = true;
    res_NotLogicOP_55 = (res_NotLogicOP_55 && ! (L_P1__GetMainc34(my_id) > 1u));
    res_OrLogicOP_49 = (res_OrLogicOP_49 || res_NotLogicOP_55);
    
    if(res_OrLogicOP_49){
    bool res_ImpliesLogicOp_56 = true;
    bool res_OrLogicOP_57 = false;
    bool res_OrLogicOP_58 = false;
    bool res_AndLogicOP_59 = true;
    bool res_AndLogicOP_60 = true;
    bool res_NotLogicOP_61 = true;
    bool res_NotLogicOP_62 = true;
    res_NotLogicOP_62 = (res_NotLogicOP_62 && ! (L_P1_C1_GetState(my_id) == C1_St_state));
    res_NotLogicOP_61 = (res_NotLogicOP_61 && ! res_NotLogicOP_62);
    res_AndLogicOP_60 = (res_AndLogicOP_60 && res_NotLogicOP_61);
    bool res_NotLogicOP_63 = true;
    bool res_NotLogicOP_64 = true;
    res_NotLogicOP_64 = (res_NotLogicOP_64 && ! (Counter_GetValore(L_P1__GetMainc49(my_id)) == 11054u));
    res_NotLogicOP_63 = (res_NotLogicOP_63 && ! res_NotLogicOP_64);
    res_AndLogicOP_60 = (res_AndLogicOP_60 && res_NotLogicOP_63);
    
    res_AndLogicOP_59 = (res_AndLogicOP_59 && res_AndLogicOP_60);
    bool res_NotLogicOP_65 = true;
    res_NotLogicOP_65 = (res_NotLogicOP_65 && ! (argom34 == true));
    res_AndLogicOP_59 = (res_AndLogicOP_59 && res_NotLogicOP_65);
    
    res_OrLogicOP_58 = (res_OrLogicOP_58 || res_AndLogicOP_59);
    bool res_NotLogicOP_66 = true;
    res_NotLogicOP_66 = (res_NotLogicOP_66 && ! (Counter_GetValore(L_P1__GetMainc51(my_id)) == 1531u));
    res_OrLogicOP_58 = (res_OrLogicOP_58 || res_NotLogicOP_66);
    
    res_OrLogicOP_57 = (res_OrLogicOP_57 || res_OrLogicOP_58);
    bool res_NotLogicOP_67 = true;
    bool res_NotLogicOP_68 = true;
    res_NotLogicOP_68 = (res_NotLogicOP_68 && ! (L_P1__GetMainc35(my_id) == true));
    res_NotLogicOP_67 = (res_NotLogicOP_67 && ! res_NotLogicOP_68);
    res_OrLogicOP_57 = (res_OrLogicOP_57 || res_NotLogicOP_67);
    
    if(res_OrLogicOP_57){
    bool res_OrLogicOP_69 = false;
    res_OrLogicOP_69 = (res_OrLogicOP_69 || (L_P1__GetInMainc2(my_id) == rossogiallo));
    bool res_NotLogicOP_70 = true;
    res_NotLogicOP_70 = (res_NotLogicOP_70 && ! (L_P1__GetMainc33(my_id) == rossogiallo));
    res_OrLogicOP_69 = (res_OrLogicOP_69 || res_NotLogicOP_70);
    
    res_ImpliesLogicOp_56 = (res_ImpliesLogicOp_56 && res_OrLogicOP_69);
    }
    res_ImpliesLogicOp_48 = (res_ImpliesLogicOp_48 && res_ImpliesLogicOp_56);
    }
    res_OrLogicOP_47 = (res_OrLogicOP_47 || res_ImpliesLogicOp_48);
    bool res_OrLogicOP_71 = false;
    bool res_OrLogicOP_72 = false;
    bool res_NotLogicOP_73 = true;
    res_NotLogicOP_73 = (res_NotLogicOP_73 && ! (L_P1__GetParamMainc7(my_id) < 4u));
    res_OrLogicOP_72 = (res_OrLogicOP_72 || res_NotLogicOP_73);
    res_OrLogicOP_72 = (res_OrLogicOP_72 || (argom34 == false));
    
    res_OrLogicOP_71 = (res_OrLogicOP_71 || res_OrLogicOP_72);
    bool res_AndLogicOP_74 = true;
    bool res_AndLogicOP_75 = true;
    bool res_AndLogicOP_76 = true;
    res_AndLogicOP_76 = (res_AndLogicOP_76 && (L_P1__GetMainc33(my_id) == rossogiallo));
    res_AndLogicOP_76 = (res_AndLogicOP_76 && (L_P1__GetParamMainc7(my_id) == 2u));
    
    res_AndLogicOP_75 = (res_AndLogicOP_75 && res_AndLogicOP_76);
    bool res_NotLogicOP_77 = true;
    res_NotLogicOP_77 = (res_NotLogicOP_77 && ! (argom35 == rossogiallo));
    res_AndLogicOP_75 = (res_AndLogicOP_75 && res_NotLogicOP_77);
    
    res_AndLogicOP_74 = (res_AndLogicOP_74 && res_AndLogicOP_75);
    res_AndLogicOP_74 = (res_AndLogicOP_74 && (L_P1__GetInMainc6(my_id) == c180x));
    
    res_OrLogicOP_71 = (res_OrLogicOP_71 || res_AndLogicOP_74);
    
    res_OrLogicOP_47 = (res_OrLogicOP_47 || res_OrLogicOP_71);
    
    res_ImpliesLogicOp_41 = (res_ImpliesLogicOp_41 && res_OrLogicOP_47);
    }
    res_OrLogicOP_40 = (res_OrLogicOP_40 || res_ImpliesLogicOp_41);
    bool res_OrLogicOP_78 = false;
    bool res_AndLogicOP_79 = true;
    bool res_NotLogicOP_80 = true;
    res_NotLogicOP_80 = (res_NotLogicOP_80 && ! Timer_Attivo(L_P1__GetMainc46(my_id)));
    res_AndLogicOP_79 = (res_AndLogicOP_79 && res_NotLogicOP_80);
    bool res_NotLogicOP_81 = true;
    res_NotLogicOP_81 = (res_NotLogicOP_81 && ! (L_P1__GetInMainc6(my_id) == c180x));
    res_AndLogicOP_79 = (res_AndLogicOP_79 && res_NotLogicOP_81);
    
    res_OrLogicOP_78 = (res_OrLogicOP_78 || res_AndLogicOP_79);
    bool res_NotLogicOP_82 = true;
    res_NotLogicOP_82 = (res_NotLogicOP_82 && ! (argom34 == true));
    res_OrLogicOP_78 = (res_OrLogicOP_78 || res_NotLogicOP_82);
    
    res_OrLogicOP_40 = (res_OrLogicOP_40 || res_OrLogicOP_78);
    
    res_ImpliesLogicOp_31 = (res_ImpliesLogicOp_31 && res_OrLogicOP_40);
    }
    res_AndLogicOP_30 = (res_AndLogicOP_30 && res_ImpliesLogicOp_31);
    bool res_OrLogicOP_83 = false;
    bool res_OrLogicOP_84 = false;
    res_OrLogicOP_84 = (res_OrLogicOP_84 || Timer_Disattivo(L_P1__GetMainc46(my_id)));
    bool res_AndLogicOP_85 = true;
    bool res_NotLogicOP_86 = true;
    bool res_NotLogicOP_87 = true;
    res_NotLogicOP_87 = (res_NotLogicOP_87 && ! (L_P1__GetMainc33(my_id) == rossogiallo));
    res_NotLogicOP_86 = (res_NotLogicOP_86 && ! res_NotLogicOP_87);
    res_AndLogicOP_85 = (res_AndLogicOP_85 && res_NotLogicOP_86);
    res_AndLogicOP_85 = (res_AndLogicOP_85 && Timer_Attivo(L_P1__GetMainc48(my_id)));
    
    res_OrLogicOP_84 = (res_OrLogicOP_84 || res_AndLogicOP_85);
    
    res_OrLogicOP_83 = (res_OrLogicOP_83 || res_OrLogicOP_84);
    res_OrLogicOP_83 = (res_OrLogicOP_83 || (L_P1__GetMainc33(my_id) == rossogiallo));
    
    res_AndLogicOP_30 = (res_AndLogicOP_30 && res_OrLogicOP_83);
    
    res_ImpliesLogicOp_22 = (res_ImpliesLogicOp_22 && res_AndLogicOP_30);
    }
    res_OrLogicOP_21 = (res_OrLogicOP_21 || res_ImpliesLogicOp_22);
    bool res_OrLogicOP_88 = false;
    bool res_OrLogicOP_89 = false;
    bool res_NotLogicOP_90 = true;
    res_NotLogicOP_90 = (res_NotLogicOP_90 && ! (L_P1__GetMainc34(my_id) < 6u));
    res_OrLogicOP_89 = (res_OrLogicOP_89 || res_NotLogicOP_90);
    bool res_NotLogicOP_91 = true;
    res_NotLogicOP_91 = (res_NotLogicOP_91 && ! (L_P1__GetParamMainc9(my_id) < 5u));
    res_OrLogicOP_89 = (res_OrLogicOP_89 || res_NotLogicOP_91);
    
    res_OrLogicOP_88 = (res_OrLogicOP_88 || res_OrLogicOP_89);
    res_OrLogicOP_88 = (res_OrLogicOP_88 || (L_P1__GetInMainc3(my_id) == true));
    
    res_OrLogicOP_21 = (res_OrLogicOP_21 || res_OrLogicOP_88);
    
    res_ImpliesLogicOp_14 = (res_ImpliesLogicOp_14 && res_OrLogicOP_21);
    }
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_ImpliesLogicOp_14);
    bool res_OrLogicOP_92 = false;
    bool res_NotLogicOP_93 = true;
    res_NotLogicOP_93 = (res_NotLogicOP_93 && ! (L_P1__GetMainc33(my_id) == rossogiallo));
    res_OrLogicOP_92 = (res_OrLogicOP_92 || res_NotLogicOP_93);
    bool res_NotLogicOP_94 = true;
    res_NotLogicOP_94 = (res_NotLogicOP_94 && ! Timer_Attivo(L_P1__GetMainc47(my_id)));
    res_OrLogicOP_92 = (res_OrLogicOP_92 || res_NotLogicOP_94);
    
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_OrLogicOP_92);
    
    res_ImpliesLogicOp_6 = (res_ImpliesLogicOp_6 && res_AndLogicOP_13);
    }
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_ImpliesLogicOp_6);
    bool res_AndLogicOP_95 = true;
    res_AndLogicOP_95 = (res_AndLogicOP_95 && (L_P1__GetMainc32(my_id) == true));
    res_AndLogicOP_95 = (res_AndLogicOP_95 && Timer_Disattivo(L_P1__GetMainc46(my_id)));
    
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_AndLogicOP_95);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_AndLogicOP_5);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *48,*  *,*  il controllo MainClass_C1_controllo_C10 sia  uguale a  True
    res_AndLogicOP_0 = (res_AndLogicOP_0 && (L_P1__GetInMainc3(my_id) == true));
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
    
    { commento: {61,} commento: {35,}  se il controllo MainClass_C1_controllo_C10 è  diverso da  False  commento: {35,} o  se il controllo MainClass_C1_controllo_C4 è  uguale a c180x e  se l'argomento argomento_ave3 non  è  uguale a Verde commento: {39,}  o  se l'argomento argomento_ave3 è  diverso da Verde commento: {39,} , Tutte le seguenti { 
     commento: {63,} commento: {38,}  se il contatore MainClass_C1_contatore_Co2 non è  minore di  commento: {55,} 145 commento: {37,} e  se la variabile MainClass_C1_variabile_V4 è  uguale a RossoGiallo commento: {35,} e  se il controllo MainClass_C1_controllo_C1 è  uguale a RossoGiallo commento: {37,} o  se la variabile MainClass_C1_variabile_V4 è  diverso da RossoGiallo, Solo una delle seguenti { 
     commento: {61,} commento: {34,}  se il parametro MainClass_C1_parametro_P9 non è  minore di  commento: {55,} 4 commento: {36,} o  se il timer MainClass_C1_timer_T6 è scaduto commento: {38,} o  se il contatore MainClass_C1_contatore_Co1 è  uguale a  commento: {53,} 11, Tutte le seguenti { 
     commento: {63,} commento: {34,}  se lo stato  è  uguale a  commento: {53,}  state1  commento: {106,} commento: {36,} o  se il timer MainClass_C1_timer_T1 è attivo commento: {36,} e  se il timer MainClass_C1_timer_T1 è attivo commento: {35,} o  se il controllo MainClass_C1_controllo_C7 non è  diverso da  False  commento: {37,} o  se la variabile MainClass_C1_variabile_V4 è  diverso da RossoGiallo, Solo una delle seguenti { 
     commento: {63,}  se l'argomento argomento_ave3 è  uguale a Verde commento: {39,}  commento: {38,} e  se il contatore MainClass_C1_contatore_Co1 non è  minore di  commento: {55,} 1405, Solo una delle seguenti { 
     commento: {61,}  se il ripristino dello stato  non è  uguale a  commento: {53,}  state1  commento: {107,} commento: {36,} e  se il timer MainClass_C1_timer_T7 è attivo commento: {37,} e  se la variabile MainClass_C1_variabile_V5 è  uguale a  commento: {53,} 1 commento: {34,} e  se il parametro MainClass_C1_parametro_P1 non è  diverso da  commento: {56,} 9 commento: {36,} o  se il timer MainClass_C1_timer_T6 non è attivo, Tutte le seguenti { 
     commento: {63,}  se il ripristino dello stato  è  uguale a  commento: {53,}  state1  commento: {107,} commento: {34,} e  se il parametro MainClass_C1_parametro_P1 non è  uguale a  commento: {53,} 6 commento: {34,} o  se il parametro MainClass_C1_parametro_P1 è  minore di  commento: {55,} 10, Solo una delle seguenti { 
     commento: {62,} commento: {35,}  se il controllo MainClass_C1_controllo_C10 è  diverso da  False  commento: {34,} o  se il parametro MainClass_C1_parametro_P1 è  diverso da  commento: {56,} 6 commento: {38,} o  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  commento: {53,} 13431 commento: {35,} e  se il controllo MainClass_C1_controllo_C10 è  diverso da  True  commento: {34,} e  se il parametro MainClass_C1_parametro_P1 non è  diverso da  commento: {56,} 6 commento: {34,} o  se il parametro MainClass_C1_parametro_P10 è  uguale a  True , Almeno una delle seguenti { 
     commento: {61,} commento: {36,}  se il timer MainClass_C1_timer_T1 non è scaduto commento: {37,} e  se la variabile MainClass_C1_variabile_V3 non è  diverso da  True , Tutte le seguenti { 
     commento: {63,}  se l'argomento argomento_ave1 non  è  uguale a c180x commento: {39,}  commento: {37,} e  se la variabile MainClass_C1_variabile_V4 non è  uguale a RossoGiallo commento: {34,} o  se il parametro MainClass_C1_parametro_P1 non è  minore di  commento: {55,} 6 commento: {38,} e  se il contatore MainClass_C1_contatore_Co10 è  minore di  commento: {55,} 122, Solo una delle seguenti { 
     commento: {62,} commento: {34,}  se lo stato  è  uguale a  commento: {53,}  state1  commento: {106,} commento: {37,} o  se la variabile MainClass_C1_variabile_V3 è  uguale a  False  commento: {34,} e  se il parametro MainClass_C1_parametro_P10 è  diverso da  True  e  se l'argomento argomento_ave3 non  è  uguale a Verde commento: {39,}  commento: {38,} e  se il contatore MainClass_C1_contatore_Co2 è  maggiore di  commento: {54,} 130, Almeno una delle seguenti { 
     commento: {63,}  se il controllo ConsDef è uguale a FALSE  commento: {35,} e  se il controllo MainClass_C1_controllo_C10 non è  diverso da  True  commento: {37,} e  se la variabile MainClass_C1_variabile_V4 non è  diverso da RossoGiallo commento: {36,} e  se il timer MainClass_C1_timer_T1 non è disattivo commento: {38,} o  se il contatore MainClass_C1_contatore_Co1 è  minore di  commento: {55,} 14543 commento: {34,} e  se il parametro MainClass_C1_parametro_P1 non è  diverso da  commento: {56,} 2, Solo una delle seguenti { 
     commento: {62,}  se il controllo ConsDef è uguale a FALSE , Almeno una delle seguenti { 
     commento: {63,}  se la macro  MainClass_C1_macrova_M1 ( con argomento_a7   uguale a True ,argomento_a3   uguale a RossoGiallo ,argomento_a1   uguale a Verde ,argomento_a6   uguale a c180x  e argomento_a10   uguale a avanzamento )   è  uguale a c270x commento: {40,}  o  se l'argomento argomento_ave3 è  uguale a Verde commento: {39,}  commento: {38,} e  se il contatore MainClass_C1_contatore_Co10 non è  maggiore di  commento: {54,} 1512 o  se l'argomento argomento_ave1 non  è  diverso da c180x commento: {39,}  commento: {35,} e  se il controllo MainClass_C1_controllo_C10 non è  diverso da  False  commento: {34,} e  se il parametro MainClass_C1_parametro_P1 è  maggiore di  commento: {54,} 7, Solo una delle seguenti { 
     commento: {62,} commento: {35,}  se il controllo MainClass_C1_controllo_C10 non è  diverso da  False  e  se l'argomento argomento_ave3 non  è  diverso da Verde commento: {39,} , Almeno una delle seguenti { 
     commento: {62,}  se la macro  MainClass_C1_macrova_M8 ( con argomento_a6   uguale a True ,argomento_a10   uguale a c180x ,argomento_a5   uguale a avanzamento ,argomento_a8   uguale a Verde ,argomento_a4   uguale a Verde ,argomento_a2   uguale a Verde  e argomento_a9   uguale a c120 )  non  è  uguale a  False  commento: {40,}  commento: {34,} o  se il parametro MainClass_C1_parametro_P9 non è  minore di  commento: {55,} 10 commento: {34,} o  se il parametro MainClass_C1_parametro_P1 è  uguale a  commento: {53,} 2 commento: {38,} e  se il contatore MainClass_C1_contatore_Co2 non è  minore di  commento: {55,} 1305 commento: {38,} o  se il contatore MainClass_C1_contatore_Co2 non è  minore di  commento: {55,} 11, Almeno una delle seguenti { 
     commento: {35,}  se il controllo MainClass_C1_controllo_C10 non è  diverso da  False  commento: {34,} e  se il parametro MainClass_C1_parametro_P10 è  uguale a  False  commento: {36,} e  se il timer MainClass_C1_timer_T1 è attivo commento: {35,} o  se il controllo MainClass_C1_controllo_C10 è  uguale a  False  commento: {34,} e  se il parametro MainClass_C1_parametro_P9 è  uguale a  commento: {53,} 3, Verifica che   commento: {47,48,49,50,}  commento: {,}  il controllo MainClass_C1_controllo_C1 sia  uguale a RossoGiallo
     commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T1 non sia disattivo
     commento: {104,} o  che  commento: {35,}  il controllo MainClass_C1_controllo_C10 sia  uguale a  True 
     commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V3 non sia  uguale a  False 
     commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P1 sia  minore di  commento: {55,} 7
    
    
     } Verifica che   commento: {47,48,49,50,}  commento: {,}  il controllo MainClass_C1_controllo_C10 sia  diverso da  False 
     commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P9 non sia  minore di  commento: {55,} 9
     commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T1 sia disattivo
     commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V5 non sia  diverso da  commento: {56,} 8
     commento: {104,} e  che  commento: {36,}  il timer MainClass_C1_timer_T1 sia scaduto
     commento: {104,} o  che  commento: {36,}  il timer MainClass_C1_timer_T1 sia scaduto
    
    
     } Verifica che   commento: {48,}  commento: {,}  il controllo MainClass_C1_controllo_C1 sia  diverso da RossoGiallo
    
    
     } Verifica che   commento: {47,48,50,51,}  commento: {,}  il controllo MainClass_C1_controllo_C1 sia  diverso da RossoGiallo
     commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co10 sia  uguale a  commento: {53,} 114
     commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P1 sia  minore di  commento: {55,} 9
     commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V4 non sia  uguale a RossoGiallo
     commento: {104,} o  che  commento: {35,}  il controllo MainClass_C1_controllo_C10 sia  diverso da  True 
    
    
     } Verifica che   commento: {51,}  commento: {,}  il contatore MainClass_C1_contatore_Co1 non sia  uguale a  commento: {53,} 1231
    
    
     } Verifica che   commento: {49,51,}  commento: {,}  il contatore MainClass_C1_contatore_Co1 sia  minore di  commento: {55,} 1120
     commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T1 non sia scaduto
     commento: {104,} e  che  commento: {36,}  il timer MainClass_C1_timer_T1 non sia disattivo
     commento: {104,} o  che  commento: {36,}  il timer MainClass_C1_timer_T7 sia attivo
     commento: {104,} e  che  commento: {36,}  il timer MainClass_C1_timer_T7 non sia attivo
    
    
     } Verifica che   commento: {48,49,52,}  commento: {,}  il controllo MainClass_C1_controllo_C10 sia  uguale a  False 
     commento: {104,} e  che  commento: {35,}  il controllo MainClass_C1_controllo_C1 sia  diverso da RossoGiallo
     commento: {104,} o  che   l'argomento argomento_ave3 non  sia  uguale a Verde commento: {,} 
     commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T6 non sia disattivo
     commento: {104,} o  che  commento: {35,}  il controllo MainClass_C1_controllo_C10 non sia  diverso da  False 
     commento: {104,} e  che  commento: {36,}  il timer MainClass_C1_timer_T1 sia attivo
    
    
     } Verifica che   commento: {47,48,52,}   l'argomento argomento_ave1 non  sia  uguale a c180x commento: {,} 
     commento: {104,} o  che   l'argomento argomento_ave3 non  sia  uguale a Verde commento: {39,} 
     commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C10 sia  uguale a  False 
     commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P9 non sia  maggiore di  commento: {54,} 8
    
    
     } Verifica che   commento: {47,48,49,51,52,}  commento: {,}  il contatore MainClass_C1_contatore_Co1 sia  minore di  commento: {55,} 155
     commento: {104,} e  che   l'argomento argomento_ave3 non  sia  diverso da Verde commento: {,} 
     commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P1 non sia  diverso da  commento: {56,} 4
     commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C10 non sia  diverso da  False 
     commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T1 sia attivo
     commento: {104,} o  che   l'argomento argomento_ave3 non  sia  uguale a Verde commento: {39,} 
    
    
     } Verifica che   commento: {49,51,52,}  commento: {,}  il contatore MainClass_C1_contatore_Co10 sia  uguale a  commento: {53,} 154
     commento: {104,} o  che  commento: {38,}  il contatore MainClass_C1_contatore_Co1 sia  uguale a  commento: {53,} 1131
     commento: {104,} e  che   l'argomento argomento_ave3 sia  diverso da Verde commento: {,} 
     commento: {104,} e  che  commento: {38,}  il contatore MainClass_C1_contatore_Co1 non sia  maggiore di  commento: {54,} 105
     commento: {104,} o  che   l'argomento argomento_ave1 non  sia  uguale a c180x commento: {39,} 
     commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T1 non sia scaduto
    
    
     } Verifica che   commento: {47,48,49,52,}  commento: {34,}  il parametro MainClass_C1_parametro_P1 sia  minore di  commento: {55,} 8
     commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T7 non sia scaduto
     commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P1 non sia  minore di  commento: {55,} 10
     commento: {104,} o  che   l'argomento argomento_ave3 sia  diverso da Verde commento: {,} 
     commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C1 sia  uguale a RossoGiallo
    
    
     } Verifica che   commento: {47,50,51,}  commento: {34,}  il parametro MainClass_C1_parametro_P1 non sia  uguale a  commento: {53,} 9
     commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P1 sia  minore di  commento: {55,} 2
     commento: {104,} o  che  commento: {,}  il contatore MainClass_C1_contatore_Co2 sia  minore di  commento: {55,} 15
     commento: {104,} o  che  commento: {38,}  il contatore MainClass_C1_contatore_Co1 non sia  minore di  commento: {55,} 15
     commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P1 non sia  maggiore di  commento: {54,} 7
     commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V4 non sia  diverso da RossoGiallo
    
    
     } Verifica che   commento: {47,52,}   l'argomento argomento_ave3 non  sia  diverso da Verde commento: {,} 
     commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P1 non sia  minore di  commento: {55,} 10
     commento: {104,} o  che   l'argomento argomento_ave3 sia  uguale a Verde commento: {39,} 
    
    
     } Verifica che   commento: {49,}  commento: {,}  il timer MainClass_C1_timer_T1 sia scaduto
    
    
     } Verifica che   commento: {47,49,}  commento: {,}  il timer MainClass_C1_timer_T7 non sia scaduto
     commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P1 non sia  diverso da  commento: {56,} 4
    
    
     } Verifica che   commento: {47,49,50,51,}  commento: {,}  il timer MainClass_C1_timer_T1 sia attivo
     commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V5 sia  diverso da  commento: {56,} 2
     commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P10 sia  diverso da  False 
     commento: {104,} o  che  commento: {,}  il contatore MainClass_C1_contatore_Co1 sia  uguale a  commento: {53,} 12
     commento: {104,} e  che  commento: {37,}  la variabile MainClass_C1_variabile_V6 non sia  uguale a  False 
     commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P1 sia  diverso da  commento: {56,} 2
    
    
     } Verifica che   commento: {47,49,50,52,}  commento: {34,}  il parametro MainClass_C1_parametro_P1 non sia  uguale a  commento: {53,} 1
     commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T1 sia attivo
     commento: {104,} o  che   l'argomento argomento_ave3 sia  diverso da Verde commento: {,} 
     commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V5 sia  uguale a  commento: {53,} 5
     commento: {104,} e  che  commento: {36,}  il timer MainClass_C1_timer_T1 non sia disattivo
    
    
    }
*/
bool L_P1__Macro11(instance_id_t const my_id , C1_Enumerat1 argom37, C1_Enumerat2 argom38)
{
bool res_AndLogicOP_0 = true;
    
    //  *61,* *35,*  se il controllo MainClass_C1_controllo_C10 è  diverso da  False  *35,* o  se il controllo MainClass_C1_controllo_C4 è  uguale a c180x e  se l'argomento argomento_ave3 non  è  uguale a Verde *39,*  o  se l'argomento argomento_ave3 è  diverso da Verde *39,* , Tutte le seguenti { 
    //   *63,* *38,*  se il contatore MainClass_C1_contatore_Co2 non è  minore di  *55,* 145 *37,* e  se la variabile MainClass_C1_variabile_V4 è  uguale a RossoGiallo *35,* e  se il controllo MainClass_C1_controllo_C1 è  uguale a RossoGiallo *37,* o  se la variabile MainClass_C1_variabile_V4 è  diverso da RossoGiallo, Solo una delle seguenti { 
    //   *61,* *34,*  se il parametro MainClass_C1_parametro_P9 non è  minore di  *55,* 4 *36,* o  se il timer MainClass_C1_timer_T6 è scaduto *38,* o  se il contatore MainClass_C1_contatore_Co1 è  uguale a  *53,* 11, Tutte le seguenti { 
    //   *63,* *34,*  se lo stato  è  uguale a  *53,*  state1  *106,* *36,* o  se il timer MainClass_C1_timer_T1 è attivo *36,* e  se il timer MainClass_C1_timer_T1 è attivo *35,* o  se il controllo MainClass_C1_controllo_C7 non è  diverso da  False  *37,* o  se la variabile MainClass_C1_variabile_V4 è  diverso da RossoGiallo, Solo una delle seguenti { 
    //   *63,*  se l'argomento argomento_ave3 è  uguale a Verde *39,*  *38,* e  se il contatore MainClass_C1_contatore_Co1 non è  minore di  *55,* 1405, Solo una delle seguenti { 
    //   *61,*  se il ripristino dello stato  non è  uguale a  *53,*  state1  *107,* *36,* e  se il timer MainClass_C1_timer_T7 è attivo *37,* e  se la variabile MainClass_C1_variabile_V5 è  uguale a  *53,* 1 *34,* e  se il parametro MainClass_C1_parametro_P1 non è  diverso da  *56,* 9 *36,* o  se il timer MainClass_C1_timer_T6 non è attivo, Tutte le seguenti { 
    //   *63,*  se il ripristino dello stato  è  uguale a  *53,*  state1  *107,* *34,* e  se il parametro MainClass_C1_parametro_P1 non è  uguale a  *53,* 6 *34,* o  se il parametro MainClass_C1_parametro_P1 è  minore di  *55,* 10, Solo una delle seguenti { 
    //   *62,* *35,*  se il controllo MainClass_C1_controllo_C10 è  diverso da  False  *34,* o  se il parametro MainClass_C1_parametro_P1 è  diverso da  *56,* 6 *38,* o  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  *53,* 13431 *35,* e  se il controllo MainClass_C1_controllo_C10 è  diverso da  True  *34,* e  se il parametro MainClass_C1_parametro_P1 non è  diverso da  *56,* 6 *34,* o  se il parametro MainClass_C1_parametro_P10 è  uguale a  True , Almeno una delle seguenti { 
    //   *61,* *36,*  se il timer MainClass_C1_timer_T1 non è scaduto *37,* e  se la variabile MainClass_C1_variabile_V3 non è  diverso da  True , Tutte le seguenti { 
    //   *63,*  se l'argomento argomento_ave1 non  è  uguale a c180x *39,*  *37,* e  se la variabile MainClass_C1_variabile_V4 non è  uguale a RossoGiallo *34,* o  se il parametro MainClass_C1_parametro_P1 non è  minore di  *55,* 6 *38,* e  se il contatore MainClass_C1_contatore_Co10 è  minore di  *55,* 122, Solo una delle seguenti { 
    //   *62,* *34,*  se lo stato  è  uguale a  *53,*  state1  *106,* *37,* o  se la variabile MainClass_C1_variabile_V3 è  uguale a  False  *34,* e  se il parametro MainClass_C1_parametro_P10 è  diverso da  True  e  se l'argomento argomento_ave3 non  è  uguale a Verde *39,*  *38,* e  se il contatore MainClass_C1_contatore_Co2 è  maggiore di  *54,* 130, Almeno una delle seguenti { 
    //   *63,*  se il controllo ConsDef è uguale a FALSE  *35,* e  se il controllo MainClass_C1_controllo_C10 non è  diverso da  True  *37,* e  se la variabile MainClass_C1_variabile_V4 non è  diverso da RossoGiallo *36,* e  se il timer MainClass_C1_timer_T1 non è disattivo *38,* o  se il contatore MainClass_C1_contatore_Co1 è  minore di  *55,* 14543 *34,* e  se il parametro MainClass_C1_parametro_P1 non è  diverso da  *56,* 2, Solo una delle seguenti { 
    //   *62,*  se il controllo ConsDef è uguale a FALSE , Almeno una delle seguenti { 
    //   *63,*  se la macro  MainClass_C1_macrova_M1 ( con argomento_a7   uguale a True ,argomento_a3   uguale a RossoGiallo ,argomento_a1   uguale a Verde ,argomento_a6   uguale a c180x  e argomento_a10   uguale a avanzamento )   è  uguale a c270x *40,*  o  se l'argomento argomento_ave3 è  uguale a Verde *39,*  *38,* e  se il contatore MainClass_C1_contatore_Co10 non è  maggiore di  *54,* 1512 o  se l'argomento argomento_ave1 non  è  diverso da c180x *39,*  *35,* e  se il controllo MainClass_C1_controllo_C10 non è  diverso da  False  *34,* e  se il parametro MainClass_C1_parametro_P1 è  maggiore di  *54,* 7, Solo una delle seguenti { 
    //   *62,* *35,*  se il controllo MainClass_C1_controllo_C10 non è  diverso da  False  e  se l'argomento argomento_ave3 non  è  diverso da Verde *39,* , Almeno una delle seguenti { 
    //   *62,*  se la macro  MainClass_C1_macrova_M8 ( con argomento_a6   uguale a True ,argomento_a10   uguale a c180x ,argomento_a5   uguale a avanzamento ,argomento_a8   uguale a Verde ,argomento_a4   uguale a Verde ,argomento_a2   uguale a Verde  e argomento_a9   uguale a c120 )  non  è  uguale a  False  *40,*  *34,* o  se il parametro MainClass_C1_parametro_P9 non è  minore di  *55,* 10 *34,* o  se il parametro MainClass_C1_parametro_P1 è  uguale a  *53,* 2 *38,* e  se il contatore MainClass_C1_contatore_Co2 non è  minore di  *55,* 1305 *38,* o  se il contatore MainClass_C1_contatore_Co2 non è  minore di  *55,* 11, Almeno una delle seguenti { 
    //   *35,*  se il controllo MainClass_C1_controllo_C10 non è  diverso da  False  *34,* e  se il parametro MainClass_C1_parametro_P10 è  uguale a  False  *36,* e  se il timer MainClass_C1_timer_T1 è attivo *35,* o  se il controllo MainClass_C1_controllo_C10 è  uguale a  False  *34,* e  se il parametro MainClass_C1_parametro_P9 è  uguale a  *53,* 3, Verifica che   *47,48,49,50,*  *,*  il controllo MainClass_C1_controllo_C1 sia  uguale a RossoGiallo
    //   *104,* o  che  *,*  il timer MainClass_C1_timer_T1 non sia disattivo
    //   *104,* o  che  *35,*  il controllo MainClass_C1_controllo_C10 sia  uguale a  True 
    //   *104,* e  che  *,*  la variabile MainClass_C1_variabile_V3 non sia  uguale a  False 
    //   *104,* e  che  *34,*  il parametro MainClass_C1_parametro_P1 sia  minore di  *55,* 7
    //   } Verifica che   *47,48,49,50,*  *,*  il controllo MainClass_C1_controllo_C10 sia  diverso da  False 
    //   *104,* e  che  *34,*  il parametro MainClass_C1_parametro_P9 non sia  minore di  *55,* 9
    //   *104,* o  che  *,*  il timer MainClass_C1_timer_T1 sia disattivo
    //   *104,* o  che  *,*  la variabile MainClass_C1_variabile_V5 non sia  diverso da  *56,* 8
    //   *104,* e  che  *36,*  il timer MainClass_C1_timer_T1 sia scaduto
    //   *104,* o  che  *36,*  il timer MainClass_C1_timer_T1 sia scaduto
    //   } Verifica che   *48,*  *,*  il controllo MainClass_C1_controllo_C1 sia  diverso da RossoGiallo
    //   } Verifica che   *47,48,50,51,*  *,*  il controllo MainClass_C1_controllo_C1 sia  diverso da RossoGiallo
    //   *104,* e  che  *,*  il contatore MainClass_C1_contatore_Co10 sia  uguale a  *53,* 114
    //   *104,* o  che  *34,*  il parametro MainClass_C1_parametro_P1 sia  minore di  *55,* 9
    //   *104,* o  che  *,*  la variabile MainClass_C1_variabile_V4 non sia  uguale a RossoGiallo
    //   *104,* o  che  *35,*  il controllo MainClass_C1_controllo_C10 sia  diverso da  True 
    //   } Verifica che   *51,*  *,*  il contatore MainClass_C1_contatore_Co1 non sia  uguale a  *53,* 1231
    //   } Verifica che   *49,51,*  *,*  il contatore MainClass_C1_contatore_Co1 sia  minore di  *55,* 1120
    //   *104,* o  che  *,*  il timer MainClass_C1_timer_T1 non sia scaduto
    //   *104,* e  che  *36,*  il timer MainClass_C1_timer_T1 non sia disattivo
    //   *104,* o  che  *36,*  il timer MainClass_C1_timer_T7 sia attivo
    //   *104,* e  che  *36,*  il timer MainClass_C1_timer_T7 non sia attivo
    //   } Verifica che   *48,49,52,*  *,*  il controllo MainClass_C1_controllo_C10 sia  uguale a  False 
    //   *104,* e  che  *35,*  il controllo MainClass_C1_controllo_C1 sia  diverso da RossoGiallo
    //   *104,* o  che   l'argomento argomento_ave3 non  sia  uguale a Verde *,* 
    //   *104,* e  che  *,*  il timer MainClass_C1_timer_T6 non sia disattivo
    //   *104,* o  che  *35,*  il controllo MainClass_C1_controllo_C10 non sia  diverso da  False 
    //   *104,* e  che  *36,*  il timer MainClass_C1_timer_T1 sia attivo
    //   } Verifica che   *47,48,52,*   l'argomento argomento_ave1 non  sia  uguale a c180x *,* 
    //   *104,* o  che   l'argomento argomento_ave3 non  sia  uguale a Verde *39,* 
    //   *104,* e  che  *,*  il controllo MainClass_C1_controllo_C10 sia  uguale a  False 
    //   *104,* e  che  *34,*  il parametro MainClass_C1_parametro_P9 non sia  maggiore di  *54,* 8
    //   } Verifica che   *47,48,49,51,52,*  *,*  il contatore MainClass_C1_contatore_Co1 sia  minore di  *55,* 155
    //   *104,* e  che   l'argomento argomento_ave3 non  sia  diverso da Verde *,* 
    //   *104,* o  che  *34,*  il parametro MainClass_C1_parametro_P1 non sia  diverso da  *56,* 4
    //   *104,* o  che  *,*  il controllo MainClass_C1_controllo_C10 non sia  diverso da  False 
    //   *104,* e  che  *,*  il timer MainClass_C1_timer_T1 sia attivo
    //   *104,* o  che   l'argomento argomento_ave3 non  sia  uguale a Verde *39,* 
    //   } Verifica che   *49,51,52,*  *,*  il contatore MainClass_C1_contatore_Co10 sia  uguale a  *53,* 154
    //   *104,* o  che  *38,*  il contatore MainClass_C1_contatore_Co1 sia  uguale a  *53,* 1131
    //   *104,* e  che   l'argomento argomento_ave3 sia  diverso da Verde *,* 
    //   *104,* e  che  *38,*  il contatore MainClass_C1_contatore_Co1 non sia  maggiore di  *54,* 105
    //   *104,* o  che   l'argomento argomento_ave1 non  sia  uguale a c180x *39,* 
    //   *104,* o  che  *,*  il timer MainClass_C1_timer_T1 non sia scaduto
    //   } Verifica che   *47,48,49,52,*  *34,*  il parametro MainClass_C1_parametro_P1 sia  minore di  *55,* 8
    //   *104,* e  che  *,*  il timer MainClass_C1_timer_T7 non sia scaduto
    //   *104,* o  che  *34,*  il parametro MainClass_C1_parametro_P1 non sia  minore di  *55,* 10
    //   *104,* o  che   l'argomento argomento_ave3 sia  diverso da Verde *,* 
    //   *104,* e  che  *,*  il controllo MainClass_C1_controllo_C1 sia  uguale a RossoGiallo
    //   } Verifica che   *47,50,51,*  *34,*  il parametro MainClass_C1_parametro_P1 non sia  uguale a  *53,* 9
    //   *104,* e  che  *34,*  il parametro MainClass_C1_parametro_P1 sia  minore di  *55,* 2
    //   *104,* o  che  *,*  il contatore MainClass_C1_contatore_Co2 sia  minore di  *55,* 15
    //   *104,* o  che  *38,*  il contatore MainClass_C1_contatore_Co1 non sia  minore di  *55,* 15
    //   *104,* o  che  *34,*  il parametro MainClass_C1_parametro_P1 non sia  maggiore di  *54,* 7
    //   *104,* e  che  *,*  la variabile MainClass_C1_variabile_V4 non sia  diverso da RossoGiallo
    //   } Verifica che   *47,52,*   l'argomento argomento_ave3 non  sia  diverso da Verde *,* 
    //   *104,* o  che  *34,*  il parametro MainClass_C1_parametro_P1 non sia  minore di  *55,* 10
    //   *104,* o  che   l'argomento argomento_ave3 sia  uguale a Verde *39,* 
    //   } Verifica che   *49,*  *,*  il timer MainClass_C1_timer_T1 sia scaduto
    //   } Verifica che   *47,49,*  *,*  il timer MainClass_C1_timer_T7 non sia scaduto
    //   *104,* o  che  *34,*  il parametro MainClass_C1_parametro_P1 non sia  diverso da  *56,* 4
    //   } Verifica che   *47,49,50,51,*  *,*  il timer MainClass_C1_timer_T1 sia attivo
    //   *104,* o  che  *,*  la variabile MainClass_C1_variabile_V5 sia  diverso da  *56,* 2
    //   *104,* o  che  *34,*  il parametro MainClass_C1_parametro_P10 sia  diverso da  False 
    //   *104,* o  che  *,*  il contatore MainClass_C1_contatore_Co1 sia  uguale a  *53,* 12
    //   *104,* e  che  *37,*  la variabile MainClass_C1_variabile_V6 non sia  uguale a  False 
    //   *104,* e  che  *34,*  il parametro MainClass_C1_parametro_P1 sia  diverso da  *56,* 2
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetInMainc3(my_id) == false));
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_NotLogicOP_4);
    bool res_AndLogicOP_5 = true;
    res_AndLogicOP_5 = (res_AndLogicOP_5 && (L_P1__GetInMainc4(my_id) == c180x));
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (argom38 == verde));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_6);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_AndLogicOP_5);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (argom38 == verde));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_7);
    
    if(res_OrLogicOP_2){
    bool res_AndLogicOP_8 = true;
    bool res_ImpliesLogicOp_9 = true;
    bool res_OrLogicOP_10 = false;
    bool res_AndLogicOP_11 = true;
    bool res_AndLogicOP_12 = true;
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (Counter_GetValore(L_P1__GetMainc51(my_id)) < 145u));
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_NotLogicOP_13);
    res_AndLogicOP_12 = (res_AndLogicOP_12 && (L_P1__GetMainc33(my_id) == rossogiallo));
    
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_AndLogicOP_12);
    res_AndLogicOP_11 = (res_AndLogicOP_11 && (L_P1__GetInMainc2(my_id) == rossogiallo));
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_AndLogicOP_11);
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1__GetMainc33(my_id) == rossogiallo));
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_NotLogicOP_14);
    
    if(res_OrLogicOP_10){
    bool res_XorLogicOP_15 = true;
    int xorIndex_res_XorLogicOP_15 = 0;
    bool res_ImpliesLogicOp_16 = true;
    bool res_OrLogicOP_17 = false;
    bool res_OrLogicOP_18 = false;
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (L_P1__GetParamMainc9(my_id) < 4u));
    res_OrLogicOP_18 = (res_OrLogicOP_18 || res_NotLogicOP_19);
    res_OrLogicOP_18 = (res_OrLogicOP_18 || Timer_Scaduto(L_P1__GetMainc47(my_id)));
    
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_OrLogicOP_18);
    res_OrLogicOP_17 = (res_OrLogicOP_17 || (Counter_GetValore(L_P1__GetMainc49(my_id)) == 11u));
    
    if(res_OrLogicOP_17){
    bool res_AndLogicOP_20 = true;
    bool res_ImpliesLogicOp_21 = true;
    bool res_OrLogicOP_22 = false;
    bool res_OrLogicOP_23 = false;
    bool res_OrLogicOP_24 = false;
    res_OrLogicOP_24 = (res_OrLogicOP_24 || (L_P1_C1_GetState(my_id) == C1_St_state));
    bool res_AndLogicOP_25 = true;
    res_AndLogicOP_25 = (res_AndLogicOP_25 && Timer_Attivo(L_P1__GetMainc46(my_id)));
    res_AndLogicOP_25 = (res_AndLogicOP_25 && Timer_Attivo(L_P1__GetMainc46(my_id)));
    
    res_OrLogicOP_24 = (res_OrLogicOP_24 || res_AndLogicOP_25);
    
    res_OrLogicOP_23 = (res_OrLogicOP_23 || res_OrLogicOP_24);
    bool res_NotLogicOP_26 = true;
    bool res_NotLogicOP_27 = true;
    res_NotLogicOP_27 = (res_NotLogicOP_27 && ! (L_P1__GetInMainc5(my_id) == false));
    res_NotLogicOP_26 = (res_NotLogicOP_26 && ! res_NotLogicOP_27);
    res_OrLogicOP_23 = (res_OrLogicOP_23 || res_NotLogicOP_26);
    
    res_OrLogicOP_22 = (res_OrLogicOP_22 || res_OrLogicOP_23);
    bool res_NotLogicOP_28 = true;
    res_NotLogicOP_28 = (res_NotLogicOP_28 && ! (L_P1__GetMainc33(my_id) == rossogiallo));
    res_OrLogicOP_22 = (res_OrLogicOP_22 || res_NotLogicOP_28);
    
    if(res_OrLogicOP_22){
    bool res_XorLogicOP_29 = true;
    int xorIndex_res_XorLogicOP_29 = 0;
    bool res_ImpliesLogicOp_30 = true;
    bool res_AndLogicOP_31 = true;
    res_AndLogicOP_31 = (res_AndLogicOP_31 && (argom38 == verde));
    bool res_NotLogicOP_32 = true;
    res_NotLogicOP_32 = (res_NotLogicOP_32 && ! (Counter_GetValore(L_P1__GetMainc49(my_id)) < 1405u));
    res_AndLogicOP_31 = (res_AndLogicOP_31 && res_NotLogicOP_32);
    
    if(res_AndLogicOP_31){
    bool res_XorLogicOP_33 = true;
    int xorIndex_res_XorLogicOP_33 = 0;
    bool res_ImpliesLogicOp_34 = true;
    bool res_OrLogicOP_35 = false;
    bool res_AndLogicOP_36 = true;
    bool res_AndLogicOP_37 = true;
    bool res_AndLogicOP_38 = true;
    bool res_NotLogicOP_39 = true;
    res_NotLogicOP_39 = (res_NotLogicOP_39 && ! (L_P1__GetStato1(my_id) == C1_St_state));
    res_AndLogicOP_38 = (res_AndLogicOP_38 && res_NotLogicOP_39);
    res_AndLogicOP_38 = (res_AndLogicOP_38 && Timer_Attivo(L_P1__GetMainc48(my_id)));
    
    res_AndLogicOP_37 = (res_AndLogicOP_37 && res_AndLogicOP_38);
    res_AndLogicOP_37 = (res_AndLogicOP_37 && (L_P1__GetMainc34(my_id) == 1u));
    
    res_AndLogicOP_36 = (res_AndLogicOP_36 && res_AndLogicOP_37);
    bool res_NotLogicOP_40 = true;
    bool res_NotLogicOP_41 = true;
    res_NotLogicOP_41 = (res_NotLogicOP_41 && ! (L_P1__GetParamMainc7(my_id) == 9u));
    res_NotLogicOP_40 = (res_NotLogicOP_40 && ! res_NotLogicOP_41);
    res_AndLogicOP_36 = (res_AndLogicOP_36 && res_NotLogicOP_40);
    
    res_OrLogicOP_35 = (res_OrLogicOP_35 || res_AndLogicOP_36);
    bool res_NotLogicOP_42 = true;
    res_NotLogicOP_42 = (res_NotLogicOP_42 && ! Timer_Attivo(L_P1__GetMainc47(my_id)));
    res_OrLogicOP_35 = (res_OrLogicOP_35 || res_NotLogicOP_42);
    
    if(res_OrLogicOP_35){
    bool res_AndLogicOP_43 = true;
    bool res_ImpliesLogicOp_44 = true;
    bool res_OrLogicOP_45 = false;
    bool res_AndLogicOP_46 = true;
    res_AndLogicOP_46 = (res_AndLogicOP_46 && (L_P1__GetStato1(my_id) == C1_St_state));
    bool res_NotLogicOP_47 = true;
    res_NotLogicOP_47 = (res_NotLogicOP_47 && ! (L_P1__GetParamMainc7(my_id) == 6u));
    res_AndLogicOP_46 = (res_AndLogicOP_46 && res_NotLogicOP_47);
    
    res_OrLogicOP_45 = (res_OrLogicOP_45 || res_AndLogicOP_46);
    res_OrLogicOP_45 = (res_OrLogicOP_45 || (L_P1__GetParamMainc7(my_id) < 10u));
    
    if(res_OrLogicOP_45){
    bool res_XorLogicOP_48 = true;
    int xorIndex_res_XorLogicOP_48 = 0;
    bool res_ImpliesLogicOp_49 = true;
    bool res_OrLogicOP_50 = false;
    bool res_OrLogicOP_51 = false;
    bool res_OrLogicOP_52 = false;
    bool res_NotLogicOP_53 = true;
    res_NotLogicOP_53 = (res_NotLogicOP_53 && ! (L_P1__GetInMainc3(my_id) == false));
    res_OrLogicOP_52 = (res_OrLogicOP_52 || res_NotLogicOP_53);
    bool res_NotLogicOP_54 = true;
    res_NotLogicOP_54 = (res_NotLogicOP_54 && ! (L_P1__GetParamMainc7(my_id) == 6u));
    res_OrLogicOP_52 = (res_OrLogicOP_52 || res_NotLogicOP_54);
    
    res_OrLogicOP_51 = (res_OrLogicOP_51 || res_OrLogicOP_52);
    bool res_AndLogicOP_55 = true;
    bool res_AndLogicOP_56 = true;
    bool res_NotLogicOP_57 = true;
    res_NotLogicOP_57 = (res_NotLogicOP_57 && ! (Counter_GetValore(L_P1__GetMainc51(my_id)) == 13431u));
    res_AndLogicOP_56 = (res_AndLogicOP_56 && res_NotLogicOP_57);
    bool res_NotLogicOP_58 = true;
    res_NotLogicOP_58 = (res_NotLogicOP_58 && ! (L_P1__GetInMainc3(my_id) == true));
    res_AndLogicOP_56 = (res_AndLogicOP_56 && res_NotLogicOP_58);
    
    res_AndLogicOP_55 = (res_AndLogicOP_55 && res_AndLogicOP_56);
    bool res_NotLogicOP_59 = true;
    bool res_NotLogicOP_60 = true;
    res_NotLogicOP_60 = (res_NotLogicOP_60 && ! (L_P1__GetParamMainc7(my_id) == 6u));
    res_NotLogicOP_59 = (res_NotLogicOP_59 && ! res_NotLogicOP_60);
    res_AndLogicOP_55 = (res_AndLogicOP_55 && res_NotLogicOP_59);
    
    res_OrLogicOP_51 = (res_OrLogicOP_51 || res_AndLogicOP_55);
    
    res_OrLogicOP_50 = (res_OrLogicOP_50 || res_OrLogicOP_51);
    res_OrLogicOP_50 = (res_OrLogicOP_50 || (L_P1__GetParamMainc8(my_id) == true));
    
    if(res_OrLogicOP_50){
    bool res_OrLogicOP_61 = false;
    bool res_ImpliesLogicOp_62 = true;
    bool res_AndLogicOP_63 = true;
    bool res_NotLogicOP_64 = true;
    res_NotLogicOP_64 = (res_NotLogicOP_64 && ! Timer_Scaduto(L_P1__GetMainc46(my_id)));
    res_AndLogicOP_63 = (res_AndLogicOP_63 && res_NotLogicOP_64);
    bool res_NotLogicOP_65 = true;
    bool res_NotLogicOP_66 = true;
    res_NotLogicOP_66 = (res_NotLogicOP_66 && ! (L_P1__GetMainc32(my_id) == true));
    res_NotLogicOP_65 = (res_NotLogicOP_65 && ! res_NotLogicOP_66);
    res_AndLogicOP_63 = (res_AndLogicOP_63 && res_NotLogicOP_65);
    
    if(res_AndLogicOP_63){
    bool res_AndLogicOP_67 = true;
    bool res_ImpliesLogicOp_68 = true;
    bool res_OrLogicOP_69 = false;
    bool res_AndLogicOP_70 = true;
    bool res_NotLogicOP_71 = true;
    res_NotLogicOP_71 = (res_NotLogicOP_71 && ! (argom37 == c180x));
    res_AndLogicOP_70 = (res_AndLogicOP_70 && res_NotLogicOP_71);
    bool res_NotLogicOP_72 = true;
    res_NotLogicOP_72 = (res_NotLogicOP_72 && ! (L_P1__GetMainc33(my_id) == rossogiallo));
    res_AndLogicOP_70 = (res_AndLogicOP_70 && res_NotLogicOP_72);
    
    res_OrLogicOP_69 = (res_OrLogicOP_69 || res_AndLogicOP_70);
    bool res_AndLogicOP_73 = true;
    bool res_NotLogicOP_74 = true;
    res_NotLogicOP_74 = (res_NotLogicOP_74 && ! (L_P1__GetParamMainc7(my_id) < 6u));
    res_AndLogicOP_73 = (res_AndLogicOP_73 && res_NotLogicOP_74);
    res_AndLogicOP_73 = (res_AndLogicOP_73 && (Counter_GetValore(L_P1__GetMainc50(my_id)) < 122u));
    
    res_OrLogicOP_69 = (res_OrLogicOP_69 || res_AndLogicOP_73);
    
    if(res_OrLogicOP_69){
    bool res_XorLogicOP_75 = true;
    int xorIndex_res_XorLogicOP_75 = 0;
    bool res_ImpliesLogicOp_76 = true;
    bool res_OrLogicOP_77 = false;
    res_OrLogicOP_77 = (res_OrLogicOP_77 || (L_P1_C1_GetState(my_id) == C1_St_state));
    bool res_AndLogicOP_78 = true;
    bool res_AndLogicOP_79 = true;
    bool res_AndLogicOP_80 = true;
    res_AndLogicOP_80 = (res_AndLogicOP_80 && (L_P1__GetMainc32(my_id) == false));
    bool res_NotLogicOP_81 = true;
    res_NotLogicOP_81 = (res_NotLogicOP_81 && ! (L_P1__GetParamMainc8(my_id) == true));
    res_AndLogicOP_80 = (res_AndLogicOP_80 && res_NotLogicOP_81);
    
    res_AndLogicOP_79 = (res_AndLogicOP_79 && res_AndLogicOP_80);
    bool res_NotLogicOP_82 = true;
    res_NotLogicOP_82 = (res_NotLogicOP_82 && ! (argom38 == verde));
    res_AndLogicOP_79 = (res_AndLogicOP_79 && res_NotLogicOP_82);
    
    res_AndLogicOP_78 = (res_AndLogicOP_78 && res_AndLogicOP_79);
    res_AndLogicOP_78 = (res_AndLogicOP_78 && (Counter_GetValore(L_P1__GetMainc51(my_id)) > 130u));
    
    res_OrLogicOP_77 = (res_OrLogicOP_77 || res_AndLogicOP_78);
    
    if(res_OrLogicOP_77){
    bool res_OrLogicOP_83 = false;
    bool res_ImpliesLogicOp_84 = true;
    bool res_OrLogicOP_85 = false;
    bool res_AndLogicOP_86 = true;
    bool res_AndLogicOP_87 = true;
    bool res_AndLogicOP_88 = true;
    res_AndLogicOP_88 = (res_AndLogicOP_88 && (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_89 = true;
    bool res_NotLogicOP_90 = true;
    res_NotLogicOP_90 = (res_NotLogicOP_90 && ! (L_P1__GetInMainc3(my_id) == true));
    res_NotLogicOP_89 = (res_NotLogicOP_89 && ! res_NotLogicOP_90);
    res_AndLogicOP_88 = (res_AndLogicOP_88 && res_NotLogicOP_89);
    
    res_AndLogicOP_87 = (res_AndLogicOP_87 && res_AndLogicOP_88);
    bool res_NotLogicOP_91 = true;
    bool res_NotLogicOP_92 = true;
    res_NotLogicOP_92 = (res_NotLogicOP_92 && ! (L_P1__GetMainc33(my_id) == rossogiallo));
    res_NotLogicOP_91 = (res_NotLogicOP_91 && ! res_NotLogicOP_92);
    res_AndLogicOP_87 = (res_AndLogicOP_87 && res_NotLogicOP_91);
    
    res_AndLogicOP_86 = (res_AndLogicOP_86 && res_AndLogicOP_87);
    bool res_NotLogicOP_93 = true;
    res_NotLogicOP_93 = (res_NotLogicOP_93 && ! Timer_Disattivo(L_P1__GetMainc46(my_id)));
    res_AndLogicOP_86 = (res_AndLogicOP_86 && res_NotLogicOP_93);
    
    res_OrLogicOP_85 = (res_OrLogicOP_85 || res_AndLogicOP_86);
    bool res_AndLogicOP_94 = true;
    res_AndLogicOP_94 = (res_AndLogicOP_94 && (Counter_GetValore(L_P1__GetMainc49(my_id)) < 14543u));
    bool res_NotLogicOP_95 = true;
    bool res_NotLogicOP_96 = true;
    res_NotLogicOP_96 = (res_NotLogicOP_96 && ! (L_P1__GetParamMainc7(my_id) == 2u));
    res_NotLogicOP_95 = (res_NotLogicOP_95 && ! res_NotLogicOP_96);
    res_AndLogicOP_94 = (res_AndLogicOP_94 && res_NotLogicOP_95);
    
    res_OrLogicOP_85 = (res_OrLogicOP_85 || res_AndLogicOP_94);
    
    if(res_OrLogicOP_85){
    bool res_XorLogicOP_97 = true;
    int xorIndex_res_XorLogicOP_97 = 0;
    bool res_ImpliesLogicOp_98 = true;
    if((L_P1__GetInConsd(my_id) == false)){
    bool res_OrLogicOP_99 = false;
    bool res_ImpliesLogicOp_100 = true;
    bool res_OrLogicOP_101 = false;
    bool res_OrLogicOP_102 = false;
    res_OrLogicOP_102 = (res_OrLogicOP_102 || (L_P1__Macro5(my_id,verde,avanzamento,rossogiallo,c180x,true) == c270x));
    bool res_AndLogicOP_103 = true;
    res_AndLogicOP_103 = (res_AndLogicOP_103 && (argom38 == verde));
    bool res_NotLogicOP_104 = true;
    res_NotLogicOP_104 = (res_NotLogicOP_104 && ! (Counter_GetValore(L_P1__GetMainc50(my_id)) > 1512u));
    res_AndLogicOP_103 = (res_AndLogicOP_103 && res_NotLogicOP_104);
    
    res_OrLogicOP_102 = (res_OrLogicOP_102 || res_AndLogicOP_103);
    
    res_OrLogicOP_101 = (res_OrLogicOP_101 || res_OrLogicOP_102);
    bool res_AndLogicOP_105 = true;
    bool res_AndLogicOP_106 = true;
    bool res_NotLogicOP_107 = true;
    bool res_NotLogicOP_108 = true;
    res_NotLogicOP_108 = (res_NotLogicOP_108 && ! (argom37 == c180x));
    res_NotLogicOP_107 = (res_NotLogicOP_107 && ! res_NotLogicOP_108);
    res_AndLogicOP_106 = (res_AndLogicOP_106 && res_NotLogicOP_107);
    bool res_NotLogicOP_109 = true;
    bool res_NotLogicOP_110 = true;
    res_NotLogicOP_110 = (res_NotLogicOP_110 && ! (L_P1__GetInMainc3(my_id) == false));
    res_NotLogicOP_109 = (res_NotLogicOP_109 && ! res_NotLogicOP_110);
    res_AndLogicOP_106 = (res_AndLogicOP_106 && res_NotLogicOP_109);
    
    res_AndLogicOP_105 = (res_AndLogicOP_105 && res_AndLogicOP_106);
    res_AndLogicOP_105 = (res_AndLogicOP_105 && (L_P1__GetParamMainc7(my_id) > 7u));
    
    res_OrLogicOP_101 = (res_OrLogicOP_101 || res_AndLogicOP_105);
    
    if(res_OrLogicOP_101){
    bool res_XorLogicOP_111 = true;
    int xorIndex_res_XorLogicOP_111 = 0;
    bool res_ImpliesLogicOp_112 = true;
    bool res_AndLogicOP_113 = true;
    bool res_NotLogicOP_114 = true;
    bool res_NotLogicOP_115 = true;
    res_NotLogicOP_115 = (res_NotLogicOP_115 && ! (L_P1__GetInMainc3(my_id) == false));
    res_NotLogicOP_114 = (res_NotLogicOP_114 && ! res_NotLogicOP_115);
    res_AndLogicOP_113 = (res_AndLogicOP_113 && res_NotLogicOP_114);
    bool res_NotLogicOP_116 = true;
    bool res_NotLogicOP_117 = true;
    res_NotLogicOP_117 = (res_NotLogicOP_117 && ! (argom38 == verde));
    res_NotLogicOP_116 = (res_NotLogicOP_116 && ! res_NotLogicOP_117);
    res_AndLogicOP_113 = (res_AndLogicOP_113 && res_NotLogicOP_116);
    
    if(res_AndLogicOP_113){
    bool res_OrLogicOP_118 = false;
    bool res_ImpliesLogicOp_119 = true;
    bool res_OrLogicOP_120 = false;
    bool res_OrLogicOP_121 = false;
    bool res_OrLogicOP_122 = false;
    bool res_NotLogicOP_123 = true;
    res_NotLogicOP_123 = (res_NotLogicOP_123 && ! (L_P1__Macro7(my_id,c180x,verde,verde,avanzamento,true,verde,c120) == false));
    res_OrLogicOP_122 = (res_OrLogicOP_122 || res_NotLogicOP_123);
    bool res_NotLogicOP_124 = true;
    res_NotLogicOP_124 = (res_NotLogicOP_124 && ! (L_P1__GetParamMainc9(my_id) < 10u));
    res_OrLogicOP_122 = (res_OrLogicOP_122 || res_NotLogicOP_124);
    
    res_OrLogicOP_121 = (res_OrLogicOP_121 || res_OrLogicOP_122);
    bool res_AndLogicOP_125 = true;
    res_AndLogicOP_125 = (res_AndLogicOP_125 && (L_P1__GetParamMainc7(my_id) == 2u));
    bool res_NotLogicOP_126 = true;
    res_NotLogicOP_126 = (res_NotLogicOP_126 && ! (Counter_GetValore(L_P1__GetMainc51(my_id)) < 1305u));
    res_AndLogicOP_125 = (res_AndLogicOP_125 && res_NotLogicOP_126);
    
    res_OrLogicOP_121 = (res_OrLogicOP_121 || res_AndLogicOP_125);
    
    res_OrLogicOP_120 = (res_OrLogicOP_120 || res_OrLogicOP_121);
    bool res_NotLogicOP_127 = true;
    res_NotLogicOP_127 = (res_NotLogicOP_127 && ! (Counter_GetValore(L_P1__GetMainc51(my_id)) < 11u));
    res_OrLogicOP_120 = (res_OrLogicOP_120 || res_NotLogicOP_127);
    
    if(res_OrLogicOP_120){
    bool res_ImpliesLogicOp_128 = true;
    bool res_OrLogicOP_129 = false;
    bool res_AndLogicOP_130 = true;
    bool res_AndLogicOP_131 = true;
    bool res_NotLogicOP_132 = true;
    bool res_NotLogicOP_133 = true;
    res_NotLogicOP_133 = (res_NotLogicOP_133 && ! (L_P1__GetInMainc3(my_id) == false));
    res_NotLogicOP_132 = (res_NotLogicOP_132 && ! res_NotLogicOP_133);
    res_AndLogicOP_131 = (res_AndLogicOP_131 && res_NotLogicOP_132);
    res_AndLogicOP_131 = (res_AndLogicOP_131 && (L_P1__GetParamMainc8(my_id) == false));
    
    res_AndLogicOP_130 = (res_AndLogicOP_130 && res_AndLogicOP_131);
    res_AndLogicOP_130 = (res_AndLogicOP_130 && Timer_Attivo(L_P1__GetMainc46(my_id)));
    
    res_OrLogicOP_129 = (res_OrLogicOP_129 || res_AndLogicOP_130);
    bool res_AndLogicOP_134 = true;
    res_AndLogicOP_134 = (res_AndLogicOP_134 && (L_P1__GetInMainc3(my_id) == false));
    res_AndLogicOP_134 = (res_AndLogicOP_134 && (L_P1__GetParamMainc9(my_id) == 3u));
    
    res_OrLogicOP_129 = (res_OrLogicOP_129 || res_AndLogicOP_134);
    
    if(res_OrLogicOP_129){
    bool res_OrLogicOP_135 = false;
    bool res_OrLogicOP_136 = false;
    res_OrLogicOP_136 = (res_OrLogicOP_136 || (L_P1__GetInMainc2(my_id) == rossogiallo));
    bool res_NotLogicOP_137 = true;
    res_NotLogicOP_137 = (res_NotLogicOP_137 && ! Timer_Disattivo(L_P1__GetMainc46(my_id)));
    res_OrLogicOP_136 = (res_OrLogicOP_136 || res_NotLogicOP_137);
    
    res_OrLogicOP_135 = (res_OrLogicOP_135 || res_OrLogicOP_136);
    bool res_AndLogicOP_138 = true;
    bool res_AndLogicOP_139 = true;
    res_AndLogicOP_139 = (res_AndLogicOP_139 && (L_P1__GetInMainc3(my_id) == true));
    bool res_NotLogicOP_140 = true;
    res_NotLogicOP_140 = (res_NotLogicOP_140 && ! (L_P1__GetMainc32(my_id) == false));
    res_AndLogicOP_139 = (res_AndLogicOP_139 && res_NotLogicOP_140);
    
    res_AndLogicOP_138 = (res_AndLogicOP_138 && res_AndLogicOP_139);
    res_AndLogicOP_138 = (res_AndLogicOP_138 && (L_P1__GetParamMainc7(my_id) < 7u));
    
    res_OrLogicOP_135 = (res_OrLogicOP_135 || res_AndLogicOP_138);
    
    res_ImpliesLogicOp_128 = (res_ImpliesLogicOp_128 && res_OrLogicOP_135);
    }
    res_ImpliesLogicOp_119 = (res_ImpliesLogicOp_119 && res_ImpliesLogicOp_128);
    }
    res_OrLogicOP_118 = (res_OrLogicOP_118 || res_ImpliesLogicOp_119);
    bool res_OrLogicOP_141 = false;
    bool res_OrLogicOP_142 = false;
    bool res_OrLogicOP_143 = false;
    bool res_AndLogicOP_144 = true;
    bool res_NotLogicOP_145 = true;
    res_NotLogicOP_145 = (res_NotLogicOP_145 && ! (L_P1__GetInMainc3(my_id) == false));
    res_AndLogicOP_144 = (res_AndLogicOP_144 && res_NotLogicOP_145);
    bool res_NotLogicOP_146 = true;
    res_NotLogicOP_146 = (res_NotLogicOP_146 && ! (L_P1__GetParamMainc9(my_id) < 9u));
    res_AndLogicOP_144 = (res_AndLogicOP_144 && res_NotLogicOP_146);
    
    res_OrLogicOP_143 = (res_OrLogicOP_143 || res_AndLogicOP_144);
    res_OrLogicOP_143 = (res_OrLogicOP_143 || Timer_Disattivo(L_P1__GetMainc46(my_id)));
    
    res_OrLogicOP_142 = (res_OrLogicOP_142 || res_OrLogicOP_143);
    bool res_AndLogicOP_147 = true;
    bool res_NotLogicOP_148 = true;
    bool res_NotLogicOP_149 = true;
    res_NotLogicOP_149 = (res_NotLogicOP_149 && ! (L_P1__GetMainc34(my_id) == 8u));
    res_NotLogicOP_148 = (res_NotLogicOP_148 && ! res_NotLogicOP_149);
    res_AndLogicOP_147 = (res_AndLogicOP_147 && res_NotLogicOP_148);
    res_AndLogicOP_147 = (res_AndLogicOP_147 && Timer_Scaduto(L_P1__GetMainc46(my_id)));
    
    res_OrLogicOP_142 = (res_OrLogicOP_142 || res_AndLogicOP_147);
    
    res_OrLogicOP_141 = (res_OrLogicOP_141 || res_OrLogicOP_142);
    res_OrLogicOP_141 = (res_OrLogicOP_141 || Timer_Scaduto(L_P1__GetMainc46(my_id)));
    
    res_OrLogicOP_118 = (res_OrLogicOP_118 || res_OrLogicOP_141);
    
    res_ImpliesLogicOp_112 = (res_ImpliesLogicOp_112 && res_OrLogicOP_118);
    }
    if(res_ImpliesLogicOp_112){
    xorIndex_res_XorLogicOP_111 = (xorIndex_res_XorLogicOP_111 + 1);
    }
    bool res_NotLogicOP_150 = true;
    res_NotLogicOP_150 = (res_NotLogicOP_150 && ! (L_P1__GetInMainc2(my_id) == rossogiallo));
    if(res_NotLogicOP_150){
    xorIndex_res_XorLogicOP_111 = (xorIndex_res_XorLogicOP_111 + 1);
    }
    
    res_XorLogicOP_111 = (res_XorLogicOP_111 && (xorIndex_res_XorLogicOP_111 == 1));
    res_ImpliesLogicOp_100 = (res_ImpliesLogicOp_100 && res_XorLogicOP_111);
    }
    res_OrLogicOP_99 = (res_OrLogicOP_99 || res_ImpliesLogicOp_100);
    bool res_OrLogicOP_151 = false;
    bool res_OrLogicOP_152 = false;
    bool res_OrLogicOP_153 = false;
    bool res_AndLogicOP_154 = true;
    bool res_NotLogicOP_155 = true;
    res_NotLogicOP_155 = (res_NotLogicOP_155 && ! (L_P1__GetInMainc2(my_id) == rossogiallo));
    res_AndLogicOP_154 = (res_AndLogicOP_154 && res_NotLogicOP_155);
    res_AndLogicOP_154 = (res_AndLogicOP_154 && (Counter_GetValore(L_P1__GetMainc50(my_id)) == 114u));
    
    res_OrLogicOP_153 = (res_OrLogicOP_153 || res_AndLogicOP_154);
    res_OrLogicOP_153 = (res_OrLogicOP_153 || (L_P1__GetParamMainc7(my_id) < 9u));
    
    res_OrLogicOP_152 = (res_OrLogicOP_152 || res_OrLogicOP_153);
    bool res_NotLogicOP_156 = true;
    res_NotLogicOP_156 = (res_NotLogicOP_156 && ! (L_P1__GetMainc33(my_id) == rossogiallo));
    res_OrLogicOP_152 = (res_OrLogicOP_152 || res_NotLogicOP_156);
    
    res_OrLogicOP_151 = (res_OrLogicOP_151 || res_OrLogicOP_152);
    bool res_NotLogicOP_157 = true;
    res_NotLogicOP_157 = (res_NotLogicOP_157 && ! (L_P1__GetInMainc3(my_id) == true));
    res_OrLogicOP_151 = (res_OrLogicOP_151 || res_NotLogicOP_157);
    
    res_OrLogicOP_99 = (res_OrLogicOP_99 || res_OrLogicOP_151);
    
    res_ImpliesLogicOp_98 = (res_ImpliesLogicOp_98 && res_OrLogicOP_99);
    }
    if(res_ImpliesLogicOp_98){
    xorIndex_res_XorLogicOP_97 = (xorIndex_res_XorLogicOP_97 + 1);
    }
    bool res_NotLogicOP_158 = true;
    res_NotLogicOP_158 = (res_NotLogicOP_158 && ! (Counter_GetValore(L_P1__GetMainc49(my_id)) == 1231u));
    if(res_NotLogicOP_158){
    xorIndex_res_XorLogicOP_97 = (xorIndex_res_XorLogicOP_97 + 1);
    }
    
    res_XorLogicOP_97 = (res_XorLogicOP_97 && (xorIndex_res_XorLogicOP_97 == 1));
    res_ImpliesLogicOp_84 = (res_ImpliesLogicOp_84 && res_XorLogicOP_97);
    }
    res_OrLogicOP_83 = (res_OrLogicOP_83 || res_ImpliesLogicOp_84);
    bool res_OrLogicOP_159 = false;
    bool res_OrLogicOP_160 = false;
    res_OrLogicOP_160 = (res_OrLogicOP_160 || (Counter_GetValore(L_P1__GetMainc49(my_id)) < 1120u));
    bool res_AndLogicOP_161 = true;
    bool res_NotLogicOP_162 = true;
    res_NotLogicOP_162 = (res_NotLogicOP_162 && ! Timer_Scaduto(L_P1__GetMainc46(my_id)));
    res_AndLogicOP_161 = (res_AndLogicOP_161 && res_NotLogicOP_162);
    bool res_NotLogicOP_163 = true;
    res_NotLogicOP_163 = (res_NotLogicOP_163 && ! Timer_Disattivo(L_P1__GetMainc46(my_id)));
    res_AndLogicOP_161 = (res_AndLogicOP_161 && res_NotLogicOP_163);
    
    res_OrLogicOP_160 = (res_OrLogicOP_160 || res_AndLogicOP_161);
    
    res_OrLogicOP_159 = (res_OrLogicOP_159 || res_OrLogicOP_160);
    bool res_AndLogicOP_164 = true;
    res_AndLogicOP_164 = (res_AndLogicOP_164 && Timer_Attivo(L_P1__GetMainc48(my_id)));
    bool res_NotLogicOP_165 = true;
    res_NotLogicOP_165 = (res_NotLogicOP_165 && ! Timer_Attivo(L_P1__GetMainc48(my_id)));
    res_AndLogicOP_164 = (res_AndLogicOP_164 && res_NotLogicOP_165);
    
    res_OrLogicOP_159 = (res_OrLogicOP_159 || res_AndLogicOP_164);
    
    res_OrLogicOP_83 = (res_OrLogicOP_83 || res_OrLogicOP_159);
    
    res_ImpliesLogicOp_76 = (res_ImpliesLogicOp_76 && res_OrLogicOP_83);
    }
    if(res_ImpliesLogicOp_76){
    xorIndex_res_XorLogicOP_75 = (xorIndex_res_XorLogicOP_75 + 1);
    }
    bool res_OrLogicOP_166 = false;
    bool res_OrLogicOP_167 = false;
    bool res_AndLogicOP_168 = true;
    res_AndLogicOP_168 = (res_AndLogicOP_168 && (L_P1__GetInMainc3(my_id) == false));
    bool res_NotLogicOP_169 = true;
    res_NotLogicOP_169 = (res_NotLogicOP_169 && ! (L_P1__GetInMainc2(my_id) == rossogiallo));
    res_AndLogicOP_168 = (res_AndLogicOP_168 && res_NotLogicOP_169);
    
    res_OrLogicOP_167 = (res_OrLogicOP_167 || res_AndLogicOP_168);
    bool res_AndLogicOP_170 = true;
    bool res_NotLogicOP_171 = true;
    res_NotLogicOP_171 = (res_NotLogicOP_171 && ! (argom38 == verde));
    res_AndLogicOP_170 = (res_AndLogicOP_170 && res_NotLogicOP_171);
    bool res_NotLogicOP_172 = true;
    res_NotLogicOP_172 = (res_NotLogicOP_172 && ! Timer_Disattivo(L_P1__GetMainc47(my_id)));
    res_AndLogicOP_170 = (res_AndLogicOP_170 && res_NotLogicOP_172);
    
    res_OrLogicOP_167 = (res_OrLogicOP_167 || res_AndLogicOP_170);
    
    res_OrLogicOP_166 = (res_OrLogicOP_166 || res_OrLogicOP_167);
    bool res_AndLogicOP_173 = true;
    bool res_NotLogicOP_174 = true;
    bool res_NotLogicOP_175 = true;
    res_NotLogicOP_175 = (res_NotLogicOP_175 && ! (L_P1__GetInMainc3(my_id) == false));
    res_NotLogicOP_174 = (res_NotLogicOP_174 && ! res_NotLogicOP_175);
    res_AndLogicOP_173 = (res_AndLogicOP_173 && res_NotLogicOP_174);
    res_AndLogicOP_173 = (res_AndLogicOP_173 && Timer_Attivo(L_P1__GetMainc46(my_id)));
    
    res_OrLogicOP_166 = (res_OrLogicOP_166 || res_AndLogicOP_173);
    
    if(res_OrLogicOP_166){
    xorIndex_res_XorLogicOP_75 = (xorIndex_res_XorLogicOP_75 + 1);
    }
    
    res_XorLogicOP_75 = (res_XorLogicOP_75 && (xorIndex_res_XorLogicOP_75 == 1));
    res_ImpliesLogicOp_68 = (res_ImpliesLogicOp_68 && res_XorLogicOP_75);
    }
    res_AndLogicOP_67 = (res_AndLogicOP_67 && res_ImpliesLogicOp_68);
    bool res_OrLogicOP_176 = false;
    bool res_NotLogicOP_177 = true;
    res_NotLogicOP_177 = (res_NotLogicOP_177 && ! (argom37 == c180x));
    res_OrLogicOP_176 = (res_OrLogicOP_176 || res_NotLogicOP_177);
    bool res_AndLogicOP_178 = true;
    bool res_AndLogicOP_179 = true;
    bool res_NotLogicOP_180 = true;
    res_NotLogicOP_180 = (res_NotLogicOP_180 && ! (argom38 == verde));
    res_AndLogicOP_179 = (res_AndLogicOP_179 && res_NotLogicOP_180);
    res_AndLogicOP_179 = (res_AndLogicOP_179 && (L_P1__GetInMainc3(my_id) == false));
    
    res_AndLogicOP_178 = (res_AndLogicOP_178 && res_AndLogicOP_179);
    bool res_NotLogicOP_181 = true;
    res_NotLogicOP_181 = (res_NotLogicOP_181 && ! (L_P1__GetParamMainc9(my_id) > 8u));
    res_AndLogicOP_178 = (res_AndLogicOP_178 && res_NotLogicOP_181);
    
    res_OrLogicOP_176 = (res_OrLogicOP_176 || res_AndLogicOP_178);
    
    res_AndLogicOP_67 = (res_AndLogicOP_67 && res_OrLogicOP_176);
    
    res_ImpliesLogicOp_62 = (res_ImpliesLogicOp_62 && res_AndLogicOP_67);
    }
    res_OrLogicOP_61 = (res_OrLogicOP_61 || res_ImpliesLogicOp_62);
    bool res_OrLogicOP_182 = false;
    bool res_OrLogicOP_183 = false;
    bool res_OrLogicOP_184 = false;
    bool res_AndLogicOP_185 = true;
    res_AndLogicOP_185 = (res_AndLogicOP_185 && (Counter_GetValore(L_P1__GetMainc49(my_id)) < 155u));
    bool res_NotLogicOP_186 = true;
    bool res_NotLogicOP_187 = true;
    res_NotLogicOP_187 = (res_NotLogicOP_187 && ! (argom38 == verde));
    res_NotLogicOP_186 = (res_NotLogicOP_186 && ! res_NotLogicOP_187);
    res_AndLogicOP_185 = (res_AndLogicOP_185 && res_NotLogicOP_186);
    
    res_OrLogicOP_184 = (res_OrLogicOP_184 || res_AndLogicOP_185);
    bool res_NotLogicOP_188 = true;
    bool res_NotLogicOP_189 = true;
    res_NotLogicOP_189 = (res_NotLogicOP_189 && ! (L_P1__GetParamMainc7(my_id) == 4u));
    res_NotLogicOP_188 = (res_NotLogicOP_188 && ! res_NotLogicOP_189);
    res_OrLogicOP_184 = (res_OrLogicOP_184 || res_NotLogicOP_188);
    
    res_OrLogicOP_183 = (res_OrLogicOP_183 || res_OrLogicOP_184);
    bool res_AndLogicOP_190 = true;
    bool res_NotLogicOP_191 = true;
    bool res_NotLogicOP_192 = true;
    res_NotLogicOP_192 = (res_NotLogicOP_192 && ! (L_P1__GetInMainc3(my_id) == false));
    res_NotLogicOP_191 = (res_NotLogicOP_191 && ! res_NotLogicOP_192);
    res_AndLogicOP_190 = (res_AndLogicOP_190 && res_NotLogicOP_191);
    res_AndLogicOP_190 = (res_AndLogicOP_190 && Timer_Attivo(L_P1__GetMainc46(my_id)));
    
    res_OrLogicOP_183 = (res_OrLogicOP_183 || res_AndLogicOP_190);
    
    res_OrLogicOP_182 = (res_OrLogicOP_182 || res_OrLogicOP_183);
    bool res_NotLogicOP_193 = true;
    res_NotLogicOP_193 = (res_NotLogicOP_193 && ! (argom38 == verde));
    res_OrLogicOP_182 = (res_OrLogicOP_182 || res_NotLogicOP_193);
    
    res_OrLogicOP_61 = (res_OrLogicOP_61 || res_OrLogicOP_182);
    
    res_ImpliesLogicOp_49 = (res_ImpliesLogicOp_49 && res_OrLogicOP_61);
    }
    if(res_ImpliesLogicOp_49){
    xorIndex_res_XorLogicOP_48 = (xorIndex_res_XorLogicOP_48 + 1);
    }
    bool res_OrLogicOP_194 = false;
    bool res_OrLogicOP_195 = false;
    bool res_OrLogicOP_196 = false;
    res_OrLogicOP_196 = (res_OrLogicOP_196 || (Counter_GetValore(L_P1__GetMainc50(my_id)) == 154u));
    bool res_AndLogicOP_197 = true;
    bool res_AndLogicOP_198 = true;
    res_AndLogicOP_198 = (res_AndLogicOP_198 && (Counter_GetValore(L_P1__GetMainc49(my_id)) == 1131u));
    bool res_NotLogicOP_199 = true;
    res_NotLogicOP_199 = (res_NotLogicOP_199 && ! (argom38 == verde));
    res_AndLogicOP_198 = (res_AndLogicOP_198 && res_NotLogicOP_199);
    
    res_AndLogicOP_197 = (res_AndLogicOP_197 && res_AndLogicOP_198);
    bool res_NotLogicOP_200 = true;
    res_NotLogicOP_200 = (res_NotLogicOP_200 && ! (Counter_GetValore(L_P1__GetMainc49(my_id)) > 105u));
    res_AndLogicOP_197 = (res_AndLogicOP_197 && res_NotLogicOP_200);
    
    res_OrLogicOP_196 = (res_OrLogicOP_196 || res_AndLogicOP_197);
    
    res_OrLogicOP_195 = (res_OrLogicOP_195 || res_OrLogicOP_196);
    bool res_NotLogicOP_201 = true;
    res_NotLogicOP_201 = (res_NotLogicOP_201 && ! (argom37 == c180x));
    res_OrLogicOP_195 = (res_OrLogicOP_195 || res_NotLogicOP_201);
    
    res_OrLogicOP_194 = (res_OrLogicOP_194 || res_OrLogicOP_195);
    bool res_NotLogicOP_202 = true;
    res_NotLogicOP_202 = (res_NotLogicOP_202 && ! Timer_Scaduto(L_P1__GetMainc46(my_id)));
    res_OrLogicOP_194 = (res_OrLogicOP_194 || res_NotLogicOP_202);
    
    if(res_OrLogicOP_194){
    xorIndex_res_XorLogicOP_48 = (xorIndex_res_XorLogicOP_48 + 1);
    }
    
    res_XorLogicOP_48 = (res_XorLogicOP_48 && (xorIndex_res_XorLogicOP_48 == 1));
    res_ImpliesLogicOp_44 = (res_ImpliesLogicOp_44 && res_XorLogicOP_48);
    }
    res_AndLogicOP_43 = (res_AndLogicOP_43 && res_ImpliesLogicOp_44);
    bool res_OrLogicOP_203 = false;
    bool res_OrLogicOP_204 = false;
    bool res_AndLogicOP_205 = true;
    res_AndLogicOP_205 = (res_AndLogicOP_205 && (L_P1__GetParamMainc7(my_id) < 8u));
    bool res_NotLogicOP_206 = true;
    res_NotLogicOP_206 = (res_NotLogicOP_206 && ! Timer_Scaduto(L_P1__GetMainc48(my_id)));
    res_AndLogicOP_205 = (res_AndLogicOP_205 && res_NotLogicOP_206);
    
    res_OrLogicOP_204 = (res_OrLogicOP_204 || res_AndLogicOP_205);
    bool res_NotLogicOP_207 = true;
    res_NotLogicOP_207 = (res_NotLogicOP_207 && ! (L_P1__GetParamMainc7(my_id) < 10u));
    res_OrLogicOP_204 = (res_OrLogicOP_204 || res_NotLogicOP_207);
    
    res_OrLogicOP_203 = (res_OrLogicOP_203 || res_OrLogicOP_204);
    bool res_AndLogicOP_208 = true;
    bool res_NotLogicOP_209 = true;
    res_NotLogicOP_209 = (res_NotLogicOP_209 && ! (argom38 == verde));
    res_AndLogicOP_208 = (res_AndLogicOP_208 && res_NotLogicOP_209);
    res_AndLogicOP_208 = (res_AndLogicOP_208 && (L_P1__GetInMainc2(my_id) == rossogiallo));
    
    res_OrLogicOP_203 = (res_OrLogicOP_203 || res_AndLogicOP_208);
    
    res_AndLogicOP_43 = (res_AndLogicOP_43 && res_OrLogicOP_203);
    
    res_ImpliesLogicOp_34 = (res_ImpliesLogicOp_34 && res_AndLogicOP_43);
    }
    if(res_ImpliesLogicOp_34){
    xorIndex_res_XorLogicOP_33 = (xorIndex_res_XorLogicOP_33 + 1);
    }
    bool res_OrLogicOP_210 = false;
    bool res_OrLogicOP_211 = false;
    bool res_OrLogicOP_212 = false;
    bool res_AndLogicOP_213 = true;
    bool res_NotLogicOP_214 = true;
    res_NotLogicOP_214 = (res_NotLogicOP_214 && ! (L_P1__GetParamMainc7(my_id) == 9u));
    res_AndLogicOP_213 = (res_AndLogicOP_213 && res_NotLogicOP_214);
    res_AndLogicOP_213 = (res_AndLogicOP_213 && (L_P1__GetParamMainc7(my_id) < 2u));
    
    res_OrLogicOP_212 = (res_OrLogicOP_212 || res_AndLogicOP_213);
    res_OrLogicOP_212 = (res_OrLogicOP_212 || (Counter_GetValore(L_P1__GetMainc51(my_id)) < 15u));
    
    res_OrLogicOP_211 = (res_OrLogicOP_211 || res_OrLogicOP_212);
    bool res_NotLogicOP_215 = true;
    res_NotLogicOP_215 = (res_NotLogicOP_215 && ! (Counter_GetValore(L_P1__GetMainc49(my_id)) < 15u));
    res_OrLogicOP_211 = (res_OrLogicOP_211 || res_NotLogicOP_215);
    
    res_OrLogicOP_210 = (res_OrLogicOP_210 || res_OrLogicOP_211);
    bool res_AndLogicOP_216 = true;
    bool res_NotLogicOP_217 = true;
    res_NotLogicOP_217 = (res_NotLogicOP_217 && ! (L_P1__GetParamMainc7(my_id) > 7u));
    res_AndLogicOP_216 = (res_AndLogicOP_216 && res_NotLogicOP_217);
    bool res_NotLogicOP_218 = true;
    bool res_NotLogicOP_219 = true;
    res_NotLogicOP_219 = (res_NotLogicOP_219 && ! (L_P1__GetMainc33(my_id) == rossogiallo));
    res_NotLogicOP_218 = (res_NotLogicOP_218 && ! res_NotLogicOP_219);
    res_AndLogicOP_216 = (res_AndLogicOP_216 && res_NotLogicOP_218);
    
    res_OrLogicOP_210 = (res_OrLogicOP_210 || res_AndLogicOP_216);
    
    if(res_OrLogicOP_210){
    xorIndex_res_XorLogicOP_33 = (xorIndex_res_XorLogicOP_33 + 1);
    }
    
    res_XorLogicOP_33 = (res_XorLogicOP_33 && (xorIndex_res_XorLogicOP_33 == 1));
    res_ImpliesLogicOp_30 = (res_ImpliesLogicOp_30 && res_XorLogicOP_33);
    }
    if(res_ImpliesLogicOp_30){
    xorIndex_res_XorLogicOP_29 = (xorIndex_res_XorLogicOP_29 + 1);
    }
    bool res_OrLogicOP_220 = false;
    bool res_OrLogicOP_221 = false;
    bool res_NotLogicOP_222 = true;
    bool res_NotLogicOP_223 = true;
    res_NotLogicOP_223 = (res_NotLogicOP_223 && ! (argom38 == verde));
    res_NotLogicOP_222 = (res_NotLogicOP_222 && ! res_NotLogicOP_223);
    res_OrLogicOP_221 = (res_OrLogicOP_221 || res_NotLogicOP_222);
    bool res_NotLogicOP_224 = true;
    res_NotLogicOP_224 = (res_NotLogicOP_224 && ! (L_P1__GetParamMainc7(my_id) < 10u));
    res_OrLogicOP_221 = (res_OrLogicOP_221 || res_NotLogicOP_224);
    
    res_OrLogicOP_220 = (res_OrLogicOP_220 || res_OrLogicOP_221);
    res_OrLogicOP_220 = (res_OrLogicOP_220 || (argom38 == verde));
    
    if(res_OrLogicOP_220){
    xorIndex_res_XorLogicOP_29 = (xorIndex_res_XorLogicOP_29 + 1);
    }
    
    res_XorLogicOP_29 = (res_XorLogicOP_29 && (xorIndex_res_XorLogicOP_29 == 1));
    res_ImpliesLogicOp_21 = (res_ImpliesLogicOp_21 && res_XorLogicOP_29);
    }
    res_AndLogicOP_20 = (res_AndLogicOP_20 && res_ImpliesLogicOp_21);
    res_AndLogicOP_20 = (res_AndLogicOP_20 && Timer_Scaduto(L_P1__GetMainc46(my_id)));
    
    res_ImpliesLogicOp_16 = (res_ImpliesLogicOp_16 && res_AndLogicOP_20);
    }
    if(res_ImpliesLogicOp_16){
    xorIndex_res_XorLogicOP_15 = (xorIndex_res_XorLogicOP_15 + 1);
    }
    bool res_OrLogicOP_225 = false;
    bool res_NotLogicOP_226 = true;
    res_NotLogicOP_226 = (res_NotLogicOP_226 && ! Timer_Scaduto(L_P1__GetMainc48(my_id)));
    res_OrLogicOP_225 = (res_OrLogicOP_225 || res_NotLogicOP_226);
    bool res_NotLogicOP_227 = true;
    bool res_NotLogicOP_228 = true;
    res_NotLogicOP_228 = (res_NotLogicOP_228 && ! (L_P1__GetParamMainc7(my_id) == 4u));
    res_NotLogicOP_227 = (res_NotLogicOP_227 && ! res_NotLogicOP_228);
    res_OrLogicOP_225 = (res_OrLogicOP_225 || res_NotLogicOP_227);
    
    if(res_OrLogicOP_225){
    xorIndex_res_XorLogicOP_15 = (xorIndex_res_XorLogicOP_15 + 1);
    }
    
    res_XorLogicOP_15 = (res_XorLogicOP_15 && (xorIndex_res_XorLogicOP_15 == 1));
    res_ImpliesLogicOp_9 = (res_ImpliesLogicOp_9 && res_XorLogicOP_15);
    }
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_ImpliesLogicOp_9);
    bool res_OrLogicOP_229 = false;
    bool res_OrLogicOP_230 = false;
    bool res_OrLogicOP_231 = false;
    res_OrLogicOP_231 = (res_OrLogicOP_231 || Timer_Attivo(L_P1__GetMainc46(my_id)));
    bool res_NotLogicOP_232 = true;
    res_NotLogicOP_232 = (res_NotLogicOP_232 && ! (L_P1__GetMainc34(my_id) == 2u));
    res_OrLogicOP_231 = (res_OrLogicOP_231 || res_NotLogicOP_232);
    
    res_OrLogicOP_230 = (res_OrLogicOP_230 || res_OrLogicOP_231);
    bool res_NotLogicOP_233 = true;
    res_NotLogicOP_233 = (res_NotLogicOP_233 && ! (L_P1__GetParamMainc8(my_id) == false));
    res_OrLogicOP_230 = (res_OrLogicOP_230 || res_NotLogicOP_233);
    
    res_OrLogicOP_229 = (res_OrLogicOP_229 || res_OrLogicOP_230);
    bool res_AndLogicOP_234 = true;
    bool res_AndLogicOP_235 = true;
    res_AndLogicOP_235 = (res_AndLogicOP_235 && (Counter_GetValore(L_P1__GetMainc49(my_id)) == 12u));
    bool res_NotLogicOP_236 = true;
    res_NotLogicOP_236 = (res_NotLogicOP_236 && ! (L_P1__GetMainc35(my_id) == false));
    res_AndLogicOP_235 = (res_AndLogicOP_235 && res_NotLogicOP_236);
    
    res_AndLogicOP_234 = (res_AndLogicOP_234 && res_AndLogicOP_235);
    bool res_NotLogicOP_237 = true;
    res_NotLogicOP_237 = (res_NotLogicOP_237 && ! (L_P1__GetParamMainc7(my_id) == 2u));
    res_AndLogicOP_234 = (res_AndLogicOP_234 && res_NotLogicOP_237);
    
    res_OrLogicOP_229 = (res_OrLogicOP_229 || res_AndLogicOP_234);
    
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_OrLogicOP_229);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_AndLogicOP_8);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *47,49,50,52,*  *34,*  il parametro MainClass_C1_parametro_P1 non sia  uguale a  *53,* 1
    //   *104,* e  che  *,*  il timer MainClass_C1_timer_T1 sia attivo
    //   *104,* o  che   l'argomento argomento_ave3 sia  diverso da Verde *,* 
    //   *104,* e  che  *,*  la variabile MainClass_C1_variabile_V5 sia  uguale a  *53,* 5
    //   *104,* e  che  *36,*  il timer MainClass_C1_timer_T1 non sia disattivo
    bool res_OrLogicOP_238 = false;
    bool res_AndLogicOP_239 = true;
    bool res_NotLogicOP_240 = true;
    res_NotLogicOP_240 = (res_NotLogicOP_240 && ! (L_P1__GetParamMainc7(my_id) == 1u));
    res_AndLogicOP_239 = (res_AndLogicOP_239 && res_NotLogicOP_240);
    res_AndLogicOP_239 = (res_AndLogicOP_239 && Timer_Attivo(L_P1__GetMainc46(my_id)));
    
    res_OrLogicOP_238 = (res_OrLogicOP_238 || res_AndLogicOP_239);
    bool res_AndLogicOP_241 = true;
    bool res_AndLogicOP_242 = true;
    bool res_NotLogicOP_243 = true;
    res_NotLogicOP_243 = (res_NotLogicOP_243 && ! (argom38 == verde));
    res_AndLogicOP_242 = (res_AndLogicOP_242 && res_NotLogicOP_243);
    res_AndLogicOP_242 = (res_AndLogicOP_242 && (L_P1__GetMainc34(my_id) == 5u));
    
    res_AndLogicOP_241 = (res_AndLogicOP_241 && res_AndLogicOP_242);
    bool res_NotLogicOP_244 = true;
    res_NotLogicOP_244 = (res_NotLogicOP_244 && ! Timer_Disattivo(L_P1__GetMainc46(my_id)));
    res_AndLogicOP_241 = (res_AndLogicOP_241 && res_NotLogicOP_244);
    
    res_OrLogicOP_238 = (res_OrLogicOP_238 || res_AndLogicOP_241);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_238);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
    
    { commento: {61,} commento: {37,}  se la variabile MainClass_C1_variabile_V4 è  diverso da RossoGiallo e  se l'argomento argomento_ave6 è  diverso da  True  commento: {39,} , Tutte le seguenti { 
     commento: {63,}  se il controllo ConsDef è uguale a FALSE  commento: {36,} e  se il timer MainClass_C1_timer_T6 non è attivo commento: {38,} e  se il contatore MainClass_C1_contatore_Co10 non è  maggiore di  commento: {54,} 1431, Solo una delle seguenti { 
     commento: {62,} commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  uguale a  True  commento: {36,} e  se il timer MainClass_C1_timer_T7 è scaduto commento: {35,} o  se il controllo MainClass_C1_controllo_C10 non è  diverso da  False , Almeno una delle seguenti { 
     commento: {61,} commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è disattivo commento: {38,} e  se il contatore MainClass_C1_contatore_Co10 è  minore di  commento: {55,} 142 commento: {35,} e  se il controllo MainClass_C1_controllo_C1 non è  uguale a RossoGiallo e  se l'argomento argomento_ave6 non  è  diverso da  False  commento: {39,} , Tutte le seguenti { 
     commento: {62,} commento: {38,}  se il contatore MainClass_C1_contatore_Co1 è  diverso da  commento: {56,} 1305 commento: {37,} e  se la variabile MainClass_C1_variabile_V4 è  uguale a RossoGiallo e  se l'argomento argomento_ave8 non  è  diverso da c180x commento: {39,}  commento: {34,} e  se il parametro MainClass_C1_parametro_P9 non è  uguale a  commento: {53,} 1 commento: {35,} o  se il controllo MainClass_C1_controllo_C1 è  diverso da RossoGiallo, Almeno una delle seguenti { 
     commento: {61,}  se il controllo ConsDef è uguale a FALSE  o  se l'argomento argomento_ave6 non  è  diverso da  False  commento: {39,}  commento: {38,} e  se il contatore MainClass_C1_contatore_Co10 non è  maggiore di  commento: {54,} 1512 commento: {38,} o  se il contatore MainClass_C1_contatore_Co1 non è  maggiore di  commento: {54,} 13 commento: {36,} o  se il timer MainClass_C1_timer_T7 è disattivo commento: {35,} o  se il controllo MainClass_C1_controllo_C1 è  diverso da RossoGiallo, Tutte le seguenti { 
     commento: {34,}  se lo stato  non è  uguale a  commento: {53,}  state1  commento: {106,} commento: {34,} o  se il parametro MainClass_C1_parametro_P10 è  diverso da  True , Verifica che   commento: {49,50,51,52,}  commento: {,}  il contatore MainClass_C1_contatore_Co10 non sia  uguale a  commento: {53,} 110
     commento: {104,} o  che   l'argomento argomento_ave5 sia  diverso da  True  commento: {,} 
     commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T1 sia attivo
     commento: {104,} e  che  commento: {36,}  il timer MainClass_C1_timer_T7 non sia attivo
     commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V4 non sia  uguale a RossoGiallo
    
    
     } Verifica che   commento: {49,50,}  commento: {,}  il timer MainClass_C1_timer_T1 non sia disattivo
     commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V6 sia  diverso da  False 
    
    
     } Verifica che   commento: {47,48,50,52,}  commento: {,}  il controllo MainClass_C1_controllo_C10 sia  uguale a  True 
     commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P9 sia  minore di  commento: {55,} 5
     commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V5 sia  maggiore di  commento: {54,} 2
     commento: {104,} e  che  commento: {35,}  il controllo MainClass_C1_controllo_C10 non sia  diverso da  False 
     commento: {104,} e  che   l'argomento argomento_ave8 non  sia  diverso da c180x commento: {,} 
     commento: {104,} o  che   l'argomento argomento_ave10 non  sia  uguale a c270x commento: {39,} 
    
    
     } Verifica che   commento: {47,49,50,}  commento: {,}  il timer MainClass_C1_timer_T1 sia scaduto
     commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P1 sia  uguale a  commento: {53,} 9
     commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V5 non sia  uguale a  commento: {53,} 2
    
    
     } Verifica che   commento: {47,}  commento: {34,}  il parametro MainClass_C1_parametro_P10 sia  uguale a  False 
    
    
     } Verifica che   commento: {48,49,50,51,}  commento: {,}  il contatore MainClass_C1_contatore_Co1 sia  maggiore di  commento: {54,} 15
     commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T6 non sia scaduto
     commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C10 sia  uguale a  False 
     commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V5 sia  maggiore di  commento: {54,} 10
     commento: {104,} o  che  commento: {35,}  il controllo MainClass_C1_controllo_C10 sia  uguale a  True 
    
    
     } Verifica che   commento: {49,51,}  commento: {,}  il contatore MainClass_C1_contatore_Co10 sia  maggiore di  commento: {54,} 14
     commento: {104,} o  che  commento: {38,}  il contatore MainClass_C1_contatore_Co1 sia  maggiore di  commento: {54,} 11
     commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T6 non sia attivo
     commento: {104,} o  che  commento: {38,}  il contatore MainClass_C1_contatore_Co10 sia  maggiore di  commento: {54,} 122
    
    
    }
*/
bool L_P1__Macro12(instance_id_t const my_id , C1_Enumerat4 argom39, bool argom40, bool argom41, C1_Enumerat1 argom42)
{
bool res_AndLogicOP_0 = true;
    
    //  *61,* *37,*  se la variabile MainClass_C1_variabile_V4 è  diverso da RossoGiallo e  se l'argomento argomento_ave6 è  diverso da  True  *39,* , Tutte le seguenti { 
    //   *63,*  se il controllo ConsDef è uguale a FALSE  *36,* e  se il timer MainClass_C1_timer_T6 non è attivo *38,* e  se il contatore MainClass_C1_contatore_Co10 non è  maggiore di  *54,* 1431, Solo una delle seguenti { 
    //   *62,* *109,*  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  uguale a  True  *36,* e  se il timer MainClass_C1_timer_T7 è scaduto *35,* o  se il controllo MainClass_C1_controllo_C10 non è  diverso da  False , Almeno una delle seguenti { 
    //   *61,* *110,*  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è disattivo *38,* e  se il contatore MainClass_C1_contatore_Co10 è  minore di  *55,* 142 *35,* e  se il controllo MainClass_C1_controllo_C1 non è  uguale a RossoGiallo e  se l'argomento argomento_ave6 non  è  diverso da  False  *39,* , Tutte le seguenti { 
    //   *62,* *38,*  se il contatore MainClass_C1_contatore_Co1 è  diverso da  *56,* 1305 *37,* e  se la variabile MainClass_C1_variabile_V4 è  uguale a RossoGiallo e  se l'argomento argomento_ave8 non  è  diverso da c180x *39,*  *34,* e  se il parametro MainClass_C1_parametro_P9 non è  uguale a  *53,* 1 *35,* o  se il controllo MainClass_C1_controllo_C1 è  diverso da RossoGiallo, Almeno una delle seguenti { 
    //   *61,*  se il controllo ConsDef è uguale a FALSE  o  se l'argomento argomento_ave6 non  è  diverso da  False  *39,*  *38,* e  se il contatore MainClass_C1_contatore_Co10 non è  maggiore di  *54,* 1512 *38,* o  se il contatore MainClass_C1_contatore_Co1 non è  maggiore di  *54,* 13 *36,* o  se il timer MainClass_C1_timer_T7 è disattivo *35,* o  se il controllo MainClass_C1_controllo_C1 è  diverso da RossoGiallo, Tutte le seguenti { 
    //   *34,*  se lo stato  non è  uguale a  *53,*  state1  *106,* *34,* o  se il parametro MainClass_C1_parametro_P10 è  diverso da  True , Verifica che   *49,50,51,52,*  *,*  il contatore MainClass_C1_contatore_Co10 non sia  uguale a  *53,* 110
    //   *104,* o  che   l'argomento argomento_ave5 sia  diverso da  True  *,* 
    //   *104,* o  che  *,*  il timer MainClass_C1_timer_T1 sia attivo
    //   *104,* e  che  *36,*  il timer MainClass_C1_timer_T7 non sia attivo
    //   *104,* e  che  *,*  la variabile MainClass_C1_variabile_V4 non sia  uguale a RossoGiallo
    //   } Verifica che   *49,50,*  *,*  il timer MainClass_C1_timer_T1 non sia disattivo
    //   *104,* e  che  *,*  la variabile MainClass_C1_variabile_V6 sia  diverso da  False 
    //   } Verifica che   *47,48,50,52,*  *,*  il controllo MainClass_C1_controllo_C10 sia  uguale a  True 
    //   *104,* o  che  *34,*  il parametro MainClass_C1_parametro_P9 sia  minore di  *55,* 5
    //   *104,* e  che  *,*  la variabile MainClass_C1_variabile_V5 sia  maggiore di  *54,* 2
    //   *104,* e  che  *35,*  il controllo MainClass_C1_controllo_C10 non sia  diverso da  False 
    //   *104,* e  che   l'argomento argomento_ave8 non  sia  diverso da c180x *,* 
    //   *104,* o  che   l'argomento argomento_ave10 non  sia  uguale a c270x *39,* 
    //   } Verifica che   *47,49,50,*  *,*  il timer MainClass_C1_timer_T1 sia scaduto
    //   *104,* o  che  *34,*  il parametro MainClass_C1_parametro_P1 sia  uguale a  *53,* 9
    //   *104,* o  che  *,*  la variabile MainClass_C1_variabile_V5 non sia  uguale a  *53,* 2
    //   } Verifica che   *47,*  *34,*  il parametro MainClass_C1_parametro_P10 sia  uguale a  False 
    //   } Verifica che   *48,49,50,51,*  *,*  il contatore MainClass_C1_contatore_Co1 sia  maggiore di  *54,* 15
    //   *104,* e  che  *,*  il timer MainClass_C1_timer_T6 non sia scaduto
    //   *104,* e  che  *,*  il controllo MainClass_C1_controllo_C10 sia  uguale a  False 
    //   *104,* o  che  *,*  la variabile MainClass_C1_variabile_V5 sia  maggiore di  *54,* 10
    //   *104,* o  che  *35,*  il controllo MainClass_C1_controllo_C10 sia  uguale a  True 
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_AndLogicOP_2 = true;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__GetMainc33(my_id) == rossogiallo));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_3);
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (argom41 == true));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_4);
    
    if(res_AndLogicOP_2){
    bool res_AndLogicOP_5 = true;
    bool res_ImpliesLogicOp_6 = true;
    bool res_AndLogicOP_7 = true;
    bool res_AndLogicOP_8 = true;
    res_AndLogicOP_8 = (res_AndLogicOP_8 && (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! Timer_Attivo(L_P1__GetMainc47(my_id)));
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_9);
    
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_AndLogicOP_8);
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (Counter_GetValore(L_P1__GetMainc50(my_id)) > 1431u));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_10);
    
    if(res_AndLogicOP_7){
    bool res_XorLogicOP_11 = true;
    int xorIndex_res_XorLogicOP_11 = 0;
    bool res_ImpliesLogicOp_12 = true;
    bool res_OrLogicOP_13 = false;
    bool res_AndLogicOP_14 = true;
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (L_P1__GetMainc31(my_id) == true));
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_NotLogicOP_15);
    res_AndLogicOP_14 = (res_AndLogicOP_14 && Timer_Scaduto(L_P1__GetMainc48(my_id)));
    
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_AndLogicOP_14);
    bool res_NotLogicOP_16 = true;
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! (L_P1__GetInMainc3(my_id) == false));
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! res_NotLogicOP_17);
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_NotLogicOP_16);
    
    if(res_OrLogicOP_13){
    bool res_OrLogicOP_18 = false;
    bool res_ImpliesLogicOp_19 = true;
    bool res_AndLogicOP_20 = true;
    bool res_AndLogicOP_21 = true;
    bool res_AndLogicOP_22 = true;
    bool res_NotLogicOP_23 = true;
    res_NotLogicOP_23 = (res_NotLogicOP_23 && ! Timer_Disattivo(L_P1__GetMainc37(my_id)));
    res_AndLogicOP_22 = (res_AndLogicOP_22 && res_NotLogicOP_23);
    res_AndLogicOP_22 = (res_AndLogicOP_22 && (Counter_GetValore(L_P1__GetMainc50(my_id)) < 142u));
    
    res_AndLogicOP_21 = (res_AndLogicOP_21 && res_AndLogicOP_22);
    bool res_NotLogicOP_24 = true;
    res_NotLogicOP_24 = (res_NotLogicOP_24 && ! (L_P1__GetInMainc2(my_id) == rossogiallo));
    res_AndLogicOP_21 = (res_AndLogicOP_21 && res_NotLogicOP_24);
    
    res_AndLogicOP_20 = (res_AndLogicOP_20 && res_AndLogicOP_21);
    bool res_NotLogicOP_25 = true;
    bool res_NotLogicOP_26 = true;
    res_NotLogicOP_26 = (res_NotLogicOP_26 && ! (argom41 == false));
    res_NotLogicOP_25 = (res_NotLogicOP_25 && ! res_NotLogicOP_26);
    res_AndLogicOP_20 = (res_AndLogicOP_20 && res_NotLogicOP_25);
    
    if(res_AndLogicOP_20){
    bool res_AndLogicOP_27 = true;
    bool res_ImpliesLogicOp_28 = true;
    bool res_OrLogicOP_29 = false;
    bool res_AndLogicOP_30 = true;
    bool res_AndLogicOP_31 = true;
    bool res_AndLogicOP_32 = true;
    bool res_NotLogicOP_33 = true;
    res_NotLogicOP_33 = (res_NotLogicOP_33 && ! (Counter_GetValore(L_P1__GetMainc49(my_id)) == 1305u));
    res_AndLogicOP_32 = (res_AndLogicOP_32 && res_NotLogicOP_33);
    res_AndLogicOP_32 = (res_AndLogicOP_32 && (L_P1__GetMainc33(my_id) == rossogiallo));
    
    res_AndLogicOP_31 = (res_AndLogicOP_31 && res_AndLogicOP_32);
    bool res_NotLogicOP_34 = true;
    bool res_NotLogicOP_35 = true;
    res_NotLogicOP_35 = (res_NotLogicOP_35 && ! (argom42 == c180x));
    res_NotLogicOP_34 = (res_NotLogicOP_34 && ! res_NotLogicOP_35);
    res_AndLogicOP_31 = (res_AndLogicOP_31 && res_NotLogicOP_34);
    
    res_AndLogicOP_30 = (res_AndLogicOP_30 && res_AndLogicOP_31);
    bool res_NotLogicOP_36 = true;
    res_NotLogicOP_36 = (res_NotLogicOP_36 && ! (L_P1__GetParamMainc9(my_id) == 1u));
    res_AndLogicOP_30 = (res_AndLogicOP_30 && res_NotLogicOP_36);
    
    res_OrLogicOP_29 = (res_OrLogicOP_29 || res_AndLogicOP_30);
    bool res_NotLogicOP_37 = true;
    res_NotLogicOP_37 = (res_NotLogicOP_37 && ! (L_P1__GetInMainc2(my_id) == rossogiallo));
    res_OrLogicOP_29 = (res_OrLogicOP_29 || res_NotLogicOP_37);
    
    if(res_OrLogicOP_29){
    bool res_OrLogicOP_38 = false;
    bool res_ImpliesLogicOp_39 = true;
    bool res_OrLogicOP_40 = false;
    bool res_OrLogicOP_41 = false;
    bool res_OrLogicOP_42 = false;
    bool res_OrLogicOP_43 = false;
    res_OrLogicOP_43 = (res_OrLogicOP_43 || (L_P1__GetInConsd(my_id) == false));
    bool res_AndLogicOP_44 = true;
    bool res_NotLogicOP_45 = true;
    bool res_NotLogicOP_46 = true;
    res_NotLogicOP_46 = (res_NotLogicOP_46 && ! (argom41 == false));
    res_NotLogicOP_45 = (res_NotLogicOP_45 && ! res_NotLogicOP_46);
    res_AndLogicOP_44 = (res_AndLogicOP_44 && res_NotLogicOP_45);
    bool res_NotLogicOP_47 = true;
    res_NotLogicOP_47 = (res_NotLogicOP_47 && ! (Counter_GetValore(L_P1__GetMainc50(my_id)) > 1512u));
    res_AndLogicOP_44 = (res_AndLogicOP_44 && res_NotLogicOP_47);
    
    res_OrLogicOP_43 = (res_OrLogicOP_43 || res_AndLogicOP_44);
    
    res_OrLogicOP_42 = (res_OrLogicOP_42 || res_OrLogicOP_43);
    bool res_NotLogicOP_48 = true;
    res_NotLogicOP_48 = (res_NotLogicOP_48 && ! (Counter_GetValore(L_P1__GetMainc49(my_id)) > 13u));
    res_OrLogicOP_42 = (res_OrLogicOP_42 || res_NotLogicOP_48);
    
    res_OrLogicOP_41 = (res_OrLogicOP_41 || res_OrLogicOP_42);
    res_OrLogicOP_41 = (res_OrLogicOP_41 || Timer_Disattivo(L_P1__GetMainc48(my_id)));
    
    res_OrLogicOP_40 = (res_OrLogicOP_40 || res_OrLogicOP_41);
    bool res_NotLogicOP_49 = true;
    res_NotLogicOP_49 = (res_NotLogicOP_49 && ! (L_P1__GetInMainc2(my_id) == rossogiallo));
    res_OrLogicOP_40 = (res_OrLogicOP_40 || res_NotLogicOP_49);
    
    if(res_OrLogicOP_40){
    bool res_ImpliesLogicOp_50 = true;
    bool res_OrLogicOP_51 = false;
    bool res_NotLogicOP_52 = true;
    res_NotLogicOP_52 = (res_NotLogicOP_52 && ! (L_P1_C1_GetState(my_id) == C1_St_state));
    res_OrLogicOP_51 = (res_OrLogicOP_51 || res_NotLogicOP_52);
    bool res_NotLogicOP_53 = true;
    res_NotLogicOP_53 = (res_NotLogicOP_53 && ! (L_P1__GetParamMainc8(my_id) == true));
    res_OrLogicOP_51 = (res_OrLogicOP_51 || res_NotLogicOP_53);
    
    if(res_OrLogicOP_51){
    bool res_OrLogicOP_54 = false;
    bool res_OrLogicOP_55 = false;
    bool res_NotLogicOP_56 = true;
    res_NotLogicOP_56 = (res_NotLogicOP_56 && ! (Counter_GetValore(L_P1__GetMainc50(my_id)) == 110u));
    res_OrLogicOP_55 = (res_OrLogicOP_55 || res_NotLogicOP_56);
    bool res_NotLogicOP_57 = true;
    res_NotLogicOP_57 = (res_NotLogicOP_57 && ! (argom40 == true));
    res_OrLogicOP_55 = (res_OrLogicOP_55 || res_NotLogicOP_57);
    
    res_OrLogicOP_54 = (res_OrLogicOP_54 || res_OrLogicOP_55);
    bool res_AndLogicOP_58 = true;
    bool res_AndLogicOP_59 = true;
    res_AndLogicOP_59 = (res_AndLogicOP_59 && Timer_Attivo(L_P1__GetMainc46(my_id)));
    bool res_NotLogicOP_60 = true;
    res_NotLogicOP_60 = (res_NotLogicOP_60 && ! Timer_Attivo(L_P1__GetMainc48(my_id)));
    res_AndLogicOP_59 = (res_AndLogicOP_59 && res_NotLogicOP_60);
    
    res_AndLogicOP_58 = (res_AndLogicOP_58 && res_AndLogicOP_59);
    bool res_NotLogicOP_61 = true;
    res_NotLogicOP_61 = (res_NotLogicOP_61 && ! (L_P1__GetMainc33(my_id) == rossogiallo));
    res_AndLogicOP_58 = (res_AndLogicOP_58 && res_NotLogicOP_61);
    
    res_OrLogicOP_54 = (res_OrLogicOP_54 || res_AndLogicOP_58);
    
    res_ImpliesLogicOp_50 = (res_ImpliesLogicOp_50 && res_OrLogicOP_54);
    }
    res_ImpliesLogicOp_39 = (res_ImpliesLogicOp_39 && res_ImpliesLogicOp_50);
    }
    res_OrLogicOP_38 = (res_OrLogicOP_38 || res_ImpliesLogicOp_39);
    bool res_AndLogicOP_62 = true;
    bool res_NotLogicOP_63 = true;
    res_NotLogicOP_63 = (res_NotLogicOP_63 && ! Timer_Disattivo(L_P1__GetMainc46(my_id)));
    res_AndLogicOP_62 = (res_AndLogicOP_62 && res_NotLogicOP_63);
    bool res_NotLogicOP_64 = true;
    res_NotLogicOP_64 = (res_NotLogicOP_64 && ! (L_P1__GetMainc35(my_id) == false));
    res_AndLogicOP_62 = (res_AndLogicOP_62 && res_NotLogicOP_64);
    
    res_OrLogicOP_38 = (res_OrLogicOP_38 || res_AndLogicOP_62);
    
    res_ImpliesLogicOp_28 = (res_ImpliesLogicOp_28 && res_OrLogicOP_38);
    }
    res_AndLogicOP_27 = (res_AndLogicOP_27 && res_ImpliesLogicOp_28);
    bool res_OrLogicOP_65 = false;
    bool res_OrLogicOP_66 = false;
    res_OrLogicOP_66 = (res_OrLogicOP_66 || (L_P1__GetInMainc3(my_id) == true));
    bool res_AndLogicOP_67 = true;
    bool res_AndLogicOP_68 = true;
    bool res_AndLogicOP_69 = true;
    res_AndLogicOP_69 = (res_AndLogicOP_69 && (L_P1__GetParamMainc9(my_id) < 5u));
    res_AndLogicOP_69 = (res_AndLogicOP_69 && (L_P1__GetMainc34(my_id) > 2u));
    
    res_AndLogicOP_68 = (res_AndLogicOP_68 && res_AndLogicOP_69);
    bool res_NotLogicOP_70 = true;
    bool res_NotLogicOP_71 = true;
    res_NotLogicOP_71 = (res_NotLogicOP_71 && ! (L_P1__GetInMainc3(my_id) == false));
    res_NotLogicOP_70 = (res_NotLogicOP_70 && ! res_NotLogicOP_71);
    res_AndLogicOP_68 = (res_AndLogicOP_68 && res_NotLogicOP_70);
    
    res_AndLogicOP_67 = (res_AndLogicOP_67 && res_AndLogicOP_68);
    bool res_NotLogicOP_72 = true;
    bool res_NotLogicOP_73 = true;
    res_NotLogicOP_73 = (res_NotLogicOP_73 && ! (argom42 == c180x));
    res_NotLogicOP_72 = (res_NotLogicOP_72 && ! res_NotLogicOP_73);
    res_AndLogicOP_67 = (res_AndLogicOP_67 && res_NotLogicOP_72);
    
    res_OrLogicOP_66 = (res_OrLogicOP_66 || res_AndLogicOP_67);
    
    res_OrLogicOP_65 = (res_OrLogicOP_65 || res_OrLogicOP_66);
    bool res_NotLogicOP_74 = true;
    res_NotLogicOP_74 = (res_NotLogicOP_74 && ! (argom39 == c270x));
    res_OrLogicOP_65 = (res_OrLogicOP_65 || res_NotLogicOP_74);
    
    res_AndLogicOP_27 = (res_AndLogicOP_27 && res_OrLogicOP_65);
    
    res_ImpliesLogicOp_19 = (res_ImpliesLogicOp_19 && res_AndLogicOP_27);
    }
    res_OrLogicOP_18 = (res_OrLogicOP_18 || res_ImpliesLogicOp_19);
    bool res_OrLogicOP_75 = false;
    bool res_OrLogicOP_76 = false;
    res_OrLogicOP_76 = (res_OrLogicOP_76 || Timer_Scaduto(L_P1__GetMainc46(my_id)));
    res_OrLogicOP_76 = (res_OrLogicOP_76 || (L_P1__GetParamMainc7(my_id) == 9u));
    
    res_OrLogicOP_75 = (res_OrLogicOP_75 || res_OrLogicOP_76);
    bool res_NotLogicOP_77 = true;
    res_NotLogicOP_77 = (res_NotLogicOP_77 && ! (L_P1__GetMainc34(my_id) == 2u));
    res_OrLogicOP_75 = (res_OrLogicOP_75 || res_NotLogicOP_77);
    
    res_OrLogicOP_18 = (res_OrLogicOP_18 || res_OrLogicOP_75);
    
    res_ImpliesLogicOp_12 = (res_ImpliesLogicOp_12 && res_OrLogicOP_18);
    }
    if(res_ImpliesLogicOp_12){
    xorIndex_res_XorLogicOP_11 = (xorIndex_res_XorLogicOP_11 + 1);
    }
    if((L_P1__GetParamMainc8(my_id) == false)){
    xorIndex_res_XorLogicOP_11 = (xorIndex_res_XorLogicOP_11 + 1);
    }
    
    res_XorLogicOP_11 = (res_XorLogicOP_11 && (xorIndex_res_XorLogicOP_11 == 1));
    res_ImpliesLogicOp_6 = (res_ImpliesLogicOp_6 && res_XorLogicOP_11);
    }
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_ImpliesLogicOp_6);
    bool res_OrLogicOP_78 = false;
    bool res_OrLogicOP_79 = false;
    bool res_AndLogicOP_80 = true;
    bool res_AndLogicOP_81 = true;
    res_AndLogicOP_81 = (res_AndLogicOP_81 && (Counter_GetValore(L_P1__GetMainc49(my_id)) > 15u));
    bool res_NotLogicOP_82 = true;
    res_NotLogicOP_82 = (res_NotLogicOP_82 && ! Timer_Scaduto(L_P1__GetMainc47(my_id)));
    res_AndLogicOP_81 = (res_AndLogicOP_81 && res_NotLogicOP_82);
    
    res_AndLogicOP_80 = (res_AndLogicOP_80 && res_AndLogicOP_81);
    res_AndLogicOP_80 = (res_AndLogicOP_80 && (L_P1__GetInMainc3(my_id) == false));
    
    res_OrLogicOP_79 = (res_OrLogicOP_79 || res_AndLogicOP_80);
    res_OrLogicOP_79 = (res_OrLogicOP_79 || (L_P1__GetMainc34(my_id) > 10u));
    
    res_OrLogicOP_78 = (res_OrLogicOP_78 || res_OrLogicOP_79);
    res_OrLogicOP_78 = (res_OrLogicOP_78 || (L_P1__GetInMainc3(my_id) == true));
    
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_OrLogicOP_78);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_AndLogicOP_5);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *49,51,*  *,*  il contatore MainClass_C1_contatore_Co10 sia  maggiore di  *54,* 14
    //   *104,* o  che  *38,*  il contatore MainClass_C1_contatore_Co1 sia  maggiore di  *54,* 11
    //   *104,* e  che  *,*  il timer MainClass_C1_timer_T6 non sia attivo
    //   *104,* o  che  *38,*  il contatore MainClass_C1_contatore_Co10 sia  maggiore di  *54,* 122
    bool res_OrLogicOP_83 = false;
    bool res_OrLogicOP_84 = false;
    res_OrLogicOP_84 = (res_OrLogicOP_84 || (Counter_GetValore(L_P1__GetMainc50(my_id)) > 14u));
    bool res_AndLogicOP_85 = true;
    res_AndLogicOP_85 = (res_AndLogicOP_85 && (Counter_GetValore(L_P1__GetMainc49(my_id)) > 11u));
    bool res_NotLogicOP_86 = true;
    res_NotLogicOP_86 = (res_NotLogicOP_86 && ! Timer_Attivo(L_P1__GetMainc47(my_id)));
    res_AndLogicOP_85 = (res_AndLogicOP_85 && res_NotLogicOP_86);
    
    res_OrLogicOP_84 = (res_OrLogicOP_84 || res_AndLogicOP_85);
    
    res_OrLogicOP_83 = (res_OrLogicOP_83 || res_OrLogicOP_84);
    res_OrLogicOP_83 = (res_OrLogicOP_83 || (Counter_GetValore(L_P1__GetMainc50(my_id)) > 122u));
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_83);
    
    
    
    return res_AndLogicOP_0;
}


// Macro valorizzate

/*
    CNL corrispondente:
    
    { commento: {[} commento: {35,}  se il controllo MainClass_C1_controllo_C10 non è  diverso da  False  commento: {109,} o  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  diverso da  False  commento: {109,} e  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  diverso da  True  e  se il controllo ConsDef è uguale a FALSE  , assegna alla macro il valore c270x
    
     commento: {46,} assegna alla macro il valore c270x commento: {],}
    }
*/
C1_Enumerat4 L_P1__Macro5(instance_id_t const my_id , C1_Enumerat2 argom3, C1_Enumerat1 argom4, C1_Enumerat3 argom5, C1_Enumerat1 argom6, bool argom7)
{
C1_Enumerat4 res_macro_val;
    
    //  *[* *35,*  se il controllo MainClass_C1_controllo_C10 non è  diverso da  False  *109,* o  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  diverso da  False  *109,* e  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  diverso da  True  e  se il controllo ConsDef è uguale a FALSE
    bool res_OrLogicOP_0 = false;
    bool res_NotLogicOP_1 = true;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (L_P1__GetInMainc3(my_id) == false));
    res_NotLogicOP_1 = (res_NotLogicOP_1 && ! res_NotLogicOP_2);
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_1);
    bool res_AndLogicOP_3 = true;
    bool res_AndLogicOP_4 = true;
    bool res_NotLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetMainc31(my_id) == false));
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! res_NotLogicOP_6);
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_5);
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetMainc31(my_id) == true));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_7);
    
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_AndLogicOP_4);
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_3);
    
    if(res_OrLogicOP_0){
    
    res_macro_val = c270x;
    }
    else{
    res_macro_val = c270x;
    }
    return res_macro_val;
}

/*
    CNL corrispondente:
    
    { commento: {[}  se l'argomento argomento_a7 è  diverso da  True  commento: {39,}  commento: {38,} o  se il contatore MainClass_C1_contatore_Co10 è  diverso da  commento: {56,} 12 , assegna alla macro il valore  True 
    
     commento: {46,} assegna alla macro il valore  True  commento: {],}
    }
*/
bool L_P1__Macro6(instance_id_t const my_id , C1_Enumerat4 argom8, C1_Enumerat3 argom9, C1_Enumerat3 argom10, C1_Enumerat4 argom11, C1_Enumerat2 argom12, bool argom13)
{
bool res_macro_val;
    
    //  *[*  se l'argomento argomento_a7 è  diverso da  True  *39,*  *38,* o  se il contatore MainClass_C1_contatore_Co10 è  diverso da  *56,* 12
    bool res_OrLogicOP_0 = false;
    bool res_NotLogicOP_1 = true;
    res_NotLogicOP_1 = (res_NotLogicOP_1 && ! (argom13 == true));
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_1);
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (Counter_GetValore(L_P1__GetMainc50(my_id)) == 12u));
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_2);
    
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
    
    { commento: {[}
     commento: {46,} assegna alla macro il valore  False  commento: {],}
    }
*/
bool L_P1__Macro7(instance_id_t const my_id , C1_Enumerat1 argom14, C1_Enumerat2 argom15, C1_Enumerat2 argom16, C1_Enumerat1 argom17, bool argom18, C1_Enumerat2 argom19, C1_Enumerat4 argom20)
{
return false;
}



