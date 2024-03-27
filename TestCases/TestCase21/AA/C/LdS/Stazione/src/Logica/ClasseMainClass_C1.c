// Codice del modello 'TestCase21', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
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
    if (L_P1__GetCAEvent2(my_id)) {
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
    L_P1__SetMainc10(my_id, 0);
    L_P1__SetMainc12(my_id, 0);
    L_P1__SetMainc13(my_id, 0);
    L_P1__SetMainc14(my_id, c270x);
    L_P1__SetMainc15(my_id, 0);
    L_P1__SetMainc16(my_id, ac);
    L_P1__SetMainc17(my_id, ac);
    L_P1__SetMainc18(my_id, false);
    L_P1__SetStato1(my_id, C1_St_Stato);
    // init controlli precedenti
    L_P1__SetMainc9(my_id, spento);
    // init Timer e Counter
    Timer_AggmInit(L_P1__GetMainc19(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc19_ID);
    Timer_Init(L_P1__GetMainc19(my_id), 42000);
    Timer_AggmInit(L_P1__GetMainc20(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc20_ID);
    Timer_Init(L_P1__GetMainc20(my_id), 42000);
    Timer_AggmInit(L_P1__GetMainc21(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc21_ID);
    Timer_Init(L_P1__GetMainc21(my_id), 205000);
    Timer_AggmInit(L_P1__GetMainc22(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc22_ID);
    Timer_Init(L_P1__GetMainc22(my_id), 205000);
    Timer_AggmInit(L_P1__GetMainc23(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc23_ID);
    Timer_Init(L_P1__GetMainc23(my_id), 534000);
    Timer_AggmInit(L_P1__GetMainc24(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc24_ID);
    Timer_Init(L_P1__GetMainc24(my_id), 534000);
    Timer_AggmInit(L_P1__GetMainc25(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc25_ID);
    Timer_Init(L_P1__GetMainc25(my_id), 4120000);
    Timer_AggmInit(L_P1__GetMainc26(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc26_ID);
    Timer_Init(L_P1__GetMainc26(my_id), 4120000);
    Timer_AggmInit(L_P1__GetMainc27(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc27_ID);
    Timer_Init(L_P1__GetMainc27(my_id), 2000);
    Timer_AggmInit(L_P1__GetMainc28(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc28_ID);
    Timer_Init(L_P1__GetMainc28(my_id), 2000);
    Timer_AggmInit(L_P1__GetMainc29(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc29_ID);
    Timer_Init(L_P1__GetMainc29(my_id), 4341000);
    Timer_AggmInit(L_P1__GetMainc30(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc30_ID);
    Timer_Init(L_P1__GetMainc30(my_id), 2000);
    Counter_AggmInit(L_P1__GetMainc31(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc31_ID);
    Counter_Init(L_P1__GetMainc31(my_id));
    Counter_AggmInit(L_P1__GetMainc32(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc32_ID);
    Counter_Init(L_P1__GetMainc32(my_id));
    Counter_AggmInit(L_P1__GetMainc33(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc33_ID);
    Counter_Init(L_P1__GetMainc33(my_id));
    Counter_AggmInit(L_P1__GetMainc34(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc34_ID);
    Counter_Init(L_P1__GetMainc34(my_id));
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
    L_P1__SetMainc11(my_id, L_P1__GetMainc10(my_id));
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
    Timer_Exec(L_P1__GetMainc19(my_id));
    Timer_Exec(L_P1__GetMainc20(my_id));
    Timer_Exec(L_P1__GetMainc21(my_id));
    Timer_Exec(L_P1__GetMainc22(my_id));
    Timer_Exec(L_P1__GetMainc23(my_id));
    Timer_Exec(L_P1__GetMainc24(my_id));
    Timer_Exec(L_P1__GetMainc25(my_id));
    Timer_Exec(L_P1__GetMainc26(my_id));
    Timer_Exec(L_P1__GetMainc27(my_id));
    Timer_Exec(L_P1__GetMainc28(my_id));
    Timer_Exec(L_P1__GetMainc29(my_id));
    Timer_Exec(L_P1__GetMainc30(my_id));
}

void L_P1_C1_GSetSafe(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C1(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C1(proc_id);
    L_P1__SetOutMainc(my_id, c120);
    L_P1__SetOutMainc1(my_id, true);
    L_P1__SetOutMainc2(my_id, false);
    L_P1__SetOutMainc3(my_id, false);
    L_P1__SetOutMainc4(my_id, spento);
}

void L_P1_C1_GUpdatePrev(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C1(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C1(proc_id);
    L_P1__SetMainc9(my_id, L_P1__GetInMainc8(my_id));
    L_P1__SetMainc11(my_id, L_P1__GetMainc10(my_id));
}

// ********** Definizione macro **********

// Macro di effetto

/*
    CNL corrispondente:
     
    { commento: {34,}  se lo stato  è  diverso da  commento: {56,}  state1  commento: {106,}, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V5 il valore c120
    
     ,altrimenti  commento: {66,} Assegna al comando MainClass_C1_comando_C8 il valore  False 
    
    
     commento: {37,}  se la variabile MainClass_C1_variabile_V1 non è  uguale a avvio o  se il controllo ConsDef  è  uguale a FALSE , commento: {71,}Decrementa il contatore MainClass_C1_contatore_Co7
    
     ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V2 il valore c120
    
    
    
    }
*/
void L_P1__Macro(instance_id_t const my_id )
{
//  *34,*  se lo stato  è  diverso da  *56,*  state1  *106,*, *67,* Assegna alla variabile MainClass_C1_variabile_V5 il valore c120
    // ,altrimenti  *66,* Assegna al comando MainClass_C1_comando_C8 il valore  False
    bool res_NotLogicOP_0 = true;
    res_NotLogicOP_0 = (res_NotLogicOP_0 && ! (L_P1_C1_GetState(my_id) == C1_St_state));
    if(res_NotLogicOP_0){
    
    L_P1__SetMainc17(my_id,c120);
    }else{
    
    L_P1__SetOutMainc3(my_id,false);
    }
    //  *37,*  se la variabile MainClass_C1_variabile_V1 non è  uguale a avvio o  se il controllo ConsDef  è  uguale a FALSE , *71,*Decrementa il contatore MainClass_C1_contatore_Co7
    // ,altrimenti  *67,* Assegna alla variabile MainClass_C1_variabile_V2 il valore c120
    bool res_OrLogicOP_1 = false;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (L_P1__GetMainc14(my_id) == avvio));
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_NotLogicOP_2);
    res_OrLogicOP_1 = (res_OrLogicOP_1 || (L_P1__GetInConsd(my_id) == false));
    
    if(res_OrLogicOP_1){
    
    Counter_Decr(L_P1__GetMainc34(my_id));
    }else{
    
    L_P1__SetMainc16(my_id,c120);
    }
}


// Macro di verifica

/*
    CNL corrispondente:
     
    { commento: {62,} commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è attivo commento: {34,} o  se il parametro MainClass_C1_parametro_P10 è  diverso da spento commento: {35,} o  se il controllo MainClass_C1_controllo_C10 è  diverso da c180x, Almeno una delle seguenti { 
     commento: {35,}  se il controllo MainClass_C1_controllo_C10 non è  uguale a c180x e  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} o  se la variabile MainClass_C1_variabile_V1 non è  uguale a avvio, Verifica che   commento: {48,49,50,}  commento: {,}  il timer MainClass_C1_timer_T4 sia disattivo
     commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V2 non sia  uguale a c120
     commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} o  che  commento: {37,}  la variabile MainClass_C1_variabile_V10 non sia  diverso da  commento: {56,} 4
     commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C10 sia  uguale a c180x
     commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
    
    
     } Verifica che   commento: {47,48,49,50,}  commento: {,}  il controllo MainClass_C1_controllo_C10 non sia  diverso da c180x
     commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T4 non sia attivo
     commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P8 sia  minore di  commento: {55,} 3
     commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V1 sia  uguale a avvio
    
    
    }
*/
bool L_P1__Macro5(instance_id_t const my_id )
{
bool res_AndLogicOP_0 = true;
    
    //  *62,* *110,*  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è attivo *34,* o  se il parametro MainClass_C1_parametro_P10 è  diverso da spento *35,* o  se il controllo MainClass_C1_controllo_C10 è  diverso da c180x, Almeno una delle seguenti { 
    //   *35,*  se il controllo MainClass_C1_controllo_C10 non è  uguale a c180x e  se il controllo ConsDef  è  uguale a FALSE  *37,* o  se la variabile MainClass_C1_variabile_V1 non è  uguale a avvio, Verifica che   *48,49,50,*  *,*  il timer MainClass_C1_timer_T4 sia disattivo
    //   *104,* e  che  *,*  la variabile MainClass_C1_variabile_V2 non sia  uguale a c120
    //   *104,* e  che   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* o  che  *37,*  la variabile MainClass_C1_variabile_V10 non sia  diverso da  *56,* 4
    //   *104,* e  che  *,*  il controllo MainClass_C1_controllo_C10 sia  uguale a c180x
    //   *104,* o  che   il controllo ConsDef  sia  uguale a FALSE 
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    res_OrLogicOP_3 = (res_OrLogicOP_3 || Timer_Attivo(L_P1__GetMainc20(my_id)));
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetParamMainc6(my_id) == spento));
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_NotLogicOP_4);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetInMainc5(my_id) == c180x));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_5);
    
    if(res_OrLogicOP_2){
    bool res_ImpliesLogicOp_6 = true;
    bool res_OrLogicOP_7 = false;
    bool res_AndLogicOP_8 = true;
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetInMainc5(my_id) == c180x));
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_9);
    res_AndLogicOP_8 = (res_AndLogicOP_8 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_AndLogicOP_8);
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__GetMainc14(my_id) == avvio));
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_NotLogicOP_10);
    
    if(res_OrLogicOP_7){
    bool res_OrLogicOP_11 = false;
    bool res_OrLogicOP_12 = false;
    bool res_AndLogicOP_13 = true;
    bool res_AndLogicOP_14 = true;
    res_AndLogicOP_14 = (res_AndLogicOP_14 && Timer_Disattivo(L_P1__GetMainc29(my_id)));
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (L_P1__GetMainc16(my_id) == c120));
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_NotLogicOP_15);
    
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_AndLogicOP_14);
    res_AndLogicOP_13 = (res_AndLogicOP_13 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_AndLogicOP_13);
    bool res_AndLogicOP_16 = true;
    bool res_NotLogicOP_17 = true;
    bool res_NotLogicOP_18 = true;
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! (L_P1__GetMainc15(my_id) == 4u));
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! res_NotLogicOP_18);
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_NotLogicOP_17);
    res_AndLogicOP_16 = (res_AndLogicOP_16 && (L_P1__GetInMainc5(my_id) == c180x));
    
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_AndLogicOP_16);
    
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_OrLogicOP_12);
    res_OrLogicOP_11 = (res_OrLogicOP_11 || (L_P1__GetInConsd(my_id) == false));
    
    res_ImpliesLogicOp_6 = (res_ImpliesLogicOp_6 && res_OrLogicOP_11);
    }
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_ImpliesLogicOp_6);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *47,48,49,50,*  *,*  il controllo MainClass_C1_controllo_C10 non sia  diverso da c180x
    //   *104,* o  che  *,*  il timer MainClass_C1_timer_T4 non sia attivo
    //   *104,* o  che  *34,*  il parametro MainClass_C1_parametro_P8 sia  minore di  *55,* 3
    //   *104,* o  che  *,*  la variabile MainClass_C1_variabile_V1 sia  uguale a avvio
    bool res_OrLogicOP_19 = false;
    bool res_OrLogicOP_20 = false;
    bool res_OrLogicOP_21 = false;
    bool res_NotLogicOP_22 = true;
    bool res_NotLogicOP_23 = true;
    res_NotLogicOP_23 = (res_NotLogicOP_23 && ! (L_P1__GetInMainc5(my_id) == c180x));
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! res_NotLogicOP_23);
    res_OrLogicOP_21 = (res_OrLogicOP_21 || res_NotLogicOP_22);
    bool res_NotLogicOP_24 = true;
    res_NotLogicOP_24 = (res_NotLogicOP_24 && ! Timer_Attivo(L_P1__GetMainc29(my_id)));
    res_OrLogicOP_21 = (res_OrLogicOP_21 || res_NotLogicOP_24);
    
    res_OrLogicOP_20 = (res_OrLogicOP_20 || res_OrLogicOP_21);
    res_OrLogicOP_20 = (res_OrLogicOP_20 || (L_P1__GetParamMainc7(my_id) < 3u));
    
    res_OrLogicOP_19 = (res_OrLogicOP_19 || res_OrLogicOP_20);
    res_OrLogicOP_19 = (res_OrLogicOP_19 || (L_P1__GetMainc14(my_id) == avvio));
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_19);
    
    
    
    return res_AndLogicOP_0;
}


// Macro valorizzate

/*
    CNL corrispondente:
    
    { commento: {[}
     commento: {46,} assegna alla macro il valore spento commento: {],}
    }
*/
C1_Enumerat4 L_P1__Macro1(instance_id_t const my_id , C1_Enumerat3 argom8, C1_Enumerat3 argom9, C1_Enumerat1 argom10, C1_Enumerat2 argom11, C1_Enumerat4 argom12, C1_Enumerat3 argom13)
{
return spento;
}

/*
    CNL corrispondente:
    
    { commento: {[}  se la macro  MainClass_C1_macrova_M3 ( con argomento_a2   uguale a c270x ,argomento_a3   uguale a c180x ,argomento_a8   uguale a spento ,argomento_a9   uguale a AC ,argomento_a1   uguale a AC  e argomento_a10   uguale a AC )  non  è  diverso da spento commento: {40,}  e  se il ripristino dello stato  è  diverso da  commento: {56,}  state1  commento: {107,} commento: {109,} o  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  uguale a  commento: {53,} 3 commento: {34,} e  se lo stato  non è  uguale a  commento: {53,}  state1  commento: {106,} , assegna alla macro il valore c180x
    
     commento: {46,} assegna alla macro il valore c180x commento: {],}
    }
*/
C1_Enumerat2 L_P1__Macro2(instance_id_t const my_id , bool argom14, C1_Enumerat1 argom15, C1_Enumerat3 argom16, C1_Enumerat4 argom17, C1_Enumerat3 argom18, C1_Enumerat4 argom19, C1_Enumerat2 argom20)
{
C1_Enumerat2 res_macro_val;
    
    //  *[*  se la macro  MainClass_C1_macrova_M3 ( con argomento_a2   uguale a c270x ,argomento_a3   uguale a c180x ,argomento_a8   uguale a spento ,argomento_a9   uguale a AC ,argomento_a1   uguale a AC  e argomento_a10   uguale a AC )  non  è  diverso da spento *40,*  e  se il ripristino dello stato  è  diverso da  *56,*  state1  *107,* *109,* o  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  uguale a  *53,* 3 *34,* e  se lo stato  non è  uguale a  *53,*  state1
    bool res_OrLogicOP_0 = false;
    bool res_AndLogicOP_1 = true;
    bool res_NotLogicOP_2 = true;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__Macro1(my_id,ac,ac,c270x,c180x,spento,ac) == spento));
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! res_NotLogicOP_3);
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_2);
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetStato1(my_id) == C1_St_state));
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_4);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_1);
    bool res_AndLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetMainc13(my_id) == 3u));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_6);
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1_C1_GetState(my_id) == C1_St_state));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_7);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_5);
    
    if(res_OrLogicOP_0){
    
    res_macro_val = c180x;
    }
    else{
    res_macro_val = c180x;
    }
    return res_macro_val;
}

/*
    CNL corrispondente:
     
    { commento: {[} commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  maggiore di  commento: {54,} 10 commento: {38,} e  se il contatore MainClass_C1_contatore_Co1 non è  uguale a  commento: {53,} 1153 commento: {35,} e  se il controllo MainClass_C1_controllo_C10 non è  uguale a c180x , assegna alla macro il valore  True 
    
     commento: {46,} assegna alla macro il valore  True  commento: {],}
    }
*/
bool L_P1__Macro3(instance_id_t const my_id )
{
bool res_macro_val;
    
    //  *[* *109,*  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  maggiore di  *54,* 10 *38,* e  se il contatore MainClass_C1_contatore_Co1 non è  uguale a  *53,* 1153 *35,* e  se il controllo MainClass_C1_controllo_C10 non è  uguale a c180x
    bool res_AndLogicOP_0 = true;
    bool res_AndLogicOP_1 = true;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (L_P1__GetMainc13(my_id) > 10u));
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_2);
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (Counter_GetValore(L_P1__GetMainc31(my_id)) == 1153u));
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_3);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_AndLogicOP_1);
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetInMainc5(my_id) == c180x));
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_NotLogicOP_4);
    
    if(res_AndLogicOP_0){
    
    res_macro_val = true;
    }
    else{
    res_macro_val = true;
    }
    return res_macro_val;
}

/*
    CNL corrispondente:
    
    { commento: {[} commento: {34,}  se lo stato  non è  uguale a  commento: {53,}  state1  commento: {106,} o  se il ripristino dello stato  è  uguale a  commento: {53,}  state1  commento: {107,} commento: {34,} e  se lo stato  è  diverso da  commento: {56,}  state1  commento: {106,} , assegna alla macro il valore spento
    
     commento: {46,} assegna alla macro il valore spento commento: {],}
    }
*/
C1_Enumerat4 L_P1__Macro4(instance_id_t const my_id , bool argom21, C1_Enumerat4 argom22, C1_Enumerat4 argom23, C1_Enumerat4 argom24, C1_Enumerat4 argom25)
{
C1_Enumerat4 res_macro_val;
    
    //  *[* *34,*  se lo stato  non è  uguale a  *53,*  state1  *106,* o  se il ripristino dello stato  è  uguale a  *53,*  state1  *107,* *34,* e  se lo stato  è  diverso da  *56,*  state1
    bool res_OrLogicOP_0 = false;
    bool res_NotLogicOP_1 = true;
    res_NotLogicOP_1 = (res_NotLogicOP_1 && ! (L_P1_C1_GetState(my_id) == C1_St_state));
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_1);
    bool res_AndLogicOP_2 = true;
    res_AndLogicOP_2 = (res_AndLogicOP_2 && (L_P1__GetStato1(my_id) == C1_St_state));
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1_C1_GetState(my_id) == C1_St_state));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_3);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_2);
    
    if(res_OrLogicOP_0){
    
    res_macro_val = spento;
    }
    else{
    res_macro_val = spento;
    }
    return res_macro_val;
}



