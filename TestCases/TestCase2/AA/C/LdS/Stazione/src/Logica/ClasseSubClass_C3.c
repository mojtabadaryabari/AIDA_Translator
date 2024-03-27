// Codice del modello 'TestCase2', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#include "Logica/ClasseMainClass_C1.h"
#include "Logica/ClasseSubClass_C2.h"
#include "Logica/ClasseSubClass_C3.h"
#include "Logica/ClasseSubClass_C3_priv.h"
#include "config.h"
#include "scheduler.h"


// ********** Gestione comandi manuali **********

static void L_P1_C3_InitCmdsResponse(instance_id_t const my_id)
{
    // for each manual command of L_P1_C3
    if (L_P1__GetInEvent11(my_id)) {
	    L_P1__SetOutEvent15(my_id, LDS_MANCMD_UNEXPECTED);
    } else {
        L_P1__SetOutEvent15(my_id, LDS_MANCMD_NOOP);
    }
    if (L_P1__GetInEvent12(my_id)) {
	    L_P1__SetOutEvent16(my_id, LDS_MANCMD_UNEXPECTED);
    } else {
        L_P1__SetOutEvent16(my_id, LDS_MANCMD_NOOP);
    }
    if (L_P1__GetInEvent13(my_id)) {
	    L_P1__SetOutEvent17(my_id, LDS_MANCMD_UNEXPECTED);
    } else {
        L_P1__SetOutEvent17(my_id, LDS_MANCMD_NOOP);
    }
    if (L_P1__GetInEvent14(my_id)) {
	    L_P1__SetOutEvent18(my_id, LDS_MANCMD_UNEXPECTED);
    } else {
        L_P1__SetOutEvent18(my_id, LDS_MANCMD_NOOP);
    }
}

static void L_P1_C3_SetExpectedCmdsResponse(instance_id_t const my_id, C3_Stateenu state)
{        
    switch (state) {
    case C3_St_state:
        // manual commands of L_P1_C3 that can be received in C3_St_state
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
static inline bool L_P1__Guard8(instance_id_t const my_id)
{
    return true;
}


/*
    CNL corrispondente:
     
    {
    Nessuna
    
    }
*/
static inline bool L_P1__Guard9(instance_id_t const my_id)
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
static inline void L_P1__Effec8(instance_id_t const my_id)
{
    
}


/*
    CNL corrispondente:
     
    {
    Nessuna
    }
*/
static inline void L_P1__Effec9(instance_id_t const my_id)
{
    
}



// ********** Definizione metodi **********

// Metodi standard

void L_P1_C3_Init(instance_id_t const my_id)
{
    // init variabili di stato
    L_P1__SetStato5(my_id, C3_St_Stato);
    L_P1__SetSubcl79(my_id, false);
    L_P1__SetSubcl81(my_id, false);
    L_P1__SetSubcl83(my_id, c180);
    L_P1__SetSubcl85(my_id, false);
    L_P1__SetSubcl87(my_id, avanzamento1);
    L_P1__SetSubcl89(my_id, 0);
    L_P1__SetSubcl90(my_id, 0);
    L_P1__SetSubcl91(my_id, avanzamento1);
    L_P1__SetSubcl92(my_id, avanzamento1);
    L_P1__SetSubcl93(my_id, false);
    L_P1__SetSubcl94(my_id, false);
    L_P1__SetSubcl95(my_id, 0);
    L_P1__SetSubcl96(my_id, 0);
    L_P1__SetSubcl97(my_id, rossogiallo5);
    L_P1__SetSubcl98(my_id, 0);
    L_P1__SetSubcl99(my_id, false);
    L_P1__SetSubcl100(my_id, gialloaverd);
    L_P1__SetSubcl101(my_id, false);
    // init controlli precedenti
    L_P1__SetSubcl70(my_id, false);
    L_P1__SetSubcl72(my_id, rossoverde);
    L_P1__SetSubcl74(my_id, false);
    L_P1__SetSubcl76(my_id, rossogiallo4);
    L_P1__SetSubcl78(my_id, false);
    // init Timer e Counter
    Timer_AggmInit(L_P1__GetSubcl102(my_id), true, CLASS_L_P1_C3_ID, my_id, L_P1__subcl102_ID);
    Timer_Init(L_P1__GetSubcl102(my_id), 521000);
    Timer_AggmInit(L_P1__GetSubcl103(my_id), true, CLASS_L_P1_C3_ID, my_id, L_P1__subcl103_ID);
    Timer_Init(L_P1__GetSubcl103(my_id), 521000);
    Timer_AggmInit(L_P1__GetSubcl104(my_id), true, CLASS_L_P1_C3_ID, my_id, L_P1__subcl104_ID);
    Timer_Init(L_P1__GetSubcl104(my_id), 25000);
    Timer_AggmInit(L_P1__GetSubcl105(my_id), true, CLASS_L_P1_C3_ID, my_id, L_P1__subcl105_ID);
    Timer_Init(L_P1__GetSubcl105(my_id), 25000);
    Timer_AggmInit(L_P1__GetSubcl106(my_id), true, CLASS_L_P1_C3_ID, my_id, L_P1__subcl106_ID);
    Timer_Init(L_P1__GetSubcl106(my_id), 104000);
    Timer_AggmInit(L_P1__GetSubcl107(my_id), true, CLASS_L_P1_C3_ID, my_id, L_P1__subcl107_ID);
    Timer_Init(L_P1__GetSubcl107(my_id), 104000);
    Timer_AggmInit(L_P1__GetSubcl108(my_id), true, CLASS_L_P1_C3_ID, my_id, L_P1__subcl108_ID);
    Timer_Init(L_P1__GetSubcl108(my_id), 4321000);
    Timer_AggmInit(L_P1__GetSubcl109(my_id), true, CLASS_L_P1_C3_ID, my_id, L_P1__subcl109_ID);
    Timer_Init(L_P1__GetSubcl109(my_id), 4321000);
    Timer_AggmInit(L_P1__GetSubcl110(my_id), true, CLASS_L_P1_C3_ID, my_id, L_P1__subcl110_ID);
    Timer_Init(L_P1__GetSubcl110(my_id), 45000);
    Timer_AggmInit(L_P1__GetSubcl111(my_id), true, CLASS_L_P1_C3_ID, my_id, L_P1__subcl111_ID);
    Timer_Init(L_P1__GetSubcl111(my_id), 45000);
    Timer_AggmInit(L_P1__GetSubcl112(my_id), true, CLASS_L_P1_C3_ID, my_id, L_P1__subcl112_ID);
    Timer_Init(L_P1__GetSubcl112(my_id), 550000);
    Timer_AggmInit(L_P1__GetSubcl113(my_id), true, CLASS_L_P1_C3_ID, my_id, L_P1__subcl113_ID);
    Timer_Init(L_P1__GetSubcl113(my_id), 343000);
    Counter_AggmInit(L_P1__GetSubcl114(my_id), true, CLASS_L_P1_C3_ID, my_id, L_P1__subcl114_ID);
    Counter_Init(L_P1__GetSubcl114(my_id));
    Counter_AggmInit(L_P1__GetSubcl115(my_id), true, CLASS_L_P1_C3_ID, my_id, L_P1__subcl115_ID);
    Counter_Init(L_P1__GetSubcl115(my_id));
    Counter_AggmInit(L_P1__GetSubcl116(my_id), true, CLASS_L_P1_C3_ID, my_id, L_P1__subcl116_ID);
    Counter_Init(L_P1__GetSubcl116(my_id));
    Counter_AggmInit(L_P1__GetSubcl117(my_id), true, CLASS_L_P1_C3_ID, my_id, L_P1__subcl117_ID);
    Counter_Init(L_P1__GetSubcl117(my_id));
    // init response
    L_P1_C3_SetResponse(my_id, LDS_SCHED_NOP);

    // transizione iniziale
    if(L_P1__Guard8(my_id)) {
        L_P1_C3_SetState(my_id, C3_St_state);
	L_P1__Effec8(my_id);
    } else {
        STOP_EXECUTION(LOGIC_ERROR);
    }
    // init variabili precedenti
    L_P1__SetSubcl80(my_id, L_P1__GetSubcl79(my_id));
    L_P1__SetSubcl82(my_id, L_P1__GetSubcl81(my_id));
    L_P1__SetSubcl84(my_id, L_P1__GetSubcl83(my_id));
    L_P1__SetSubcl86(my_id, L_P1__GetSubcl85(my_id));
    L_P1__SetSubcl88(my_id, L_P1__GetSubcl87(my_id));
}

void L_P1_C3_Exec(instance_id_t const my_id, Phase const p)
{
    L_P1_C3_SetResponse(my_id, LDS_SCHED_NOP);
    switch (p) {

    case LDS_PHASE_MANUAL:
        // Reset risposte ai comandi manuali
        L_P1_C3_InitCmdsResponse(my_id);
	L_P1_C3_SetExpectedCmdsResponse(my_id, L_P1_C3_GetState(my_id));
        switch (L_P1_C3_GetState(my_id)) {

        case C3_St_state:
                { } // fine transizioni da state nella fase LDS_PHASE_MANUAL
            break;

        default:
            STOP_EXECUTION(LOGIC_ERROR);
            break;  // Needed for MISRA C syntactic compliance
        } // switch sugli stati chiuso
        break;
 

    case LDS_PHASE_STATE:

        switch (L_P1_C3_GetState(my_id)) {

        case C3_St_state:
            if (L_P1__Guard9(my_id)) {
                L_P1_C3_SetState(my_id, C3_St_state);
                L_P1__Effec9(my_id);				
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

ExecResponse L_P1_C3_GExec(global_id_t const proc_id, Phase const p)
{
    CHECK_LT(GLOBAL_TO_L_P1_C3(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C3(proc_id);
    L_P1_C3_Exec(my_id, p);
    return L_P1_C3_GetResponse(my_id);
}

void L_P1_C3_GTick(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C3(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C3(proc_id);
    Timer_Exec(L_P1__GetSubcl102(my_id));
    Timer_Exec(L_P1__GetSubcl103(my_id));
    Timer_Exec(L_P1__GetSubcl104(my_id));
    Timer_Exec(L_P1__GetSubcl105(my_id));
    Timer_Exec(L_P1__GetSubcl106(my_id));
    Timer_Exec(L_P1__GetSubcl107(my_id));
    Timer_Exec(L_P1__GetSubcl108(my_id));
    Timer_Exec(L_P1__GetSubcl109(my_id));
    Timer_Exec(L_P1__GetSubcl110(my_id));
    Timer_Exec(L_P1__GetSubcl111(my_id));
    Timer_Exec(L_P1__GetSubcl112(my_id));
    Timer_Exec(L_P1__GetSubcl113(my_id));
}

void L_P1_C3_GSetSafe(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C3(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C3(proc_id);
    L_P1__SetOutSubcl54(my_id, rossoverde);
    L_P1__SetOutSubcl55(my_id, false);
    L_P1__SetOutSubcl56(my_id, rossogiallo4);
    L_P1__SetOutSubcl57(my_id, avanzamento);
    L_P1__SetOutSubcl58(my_id, true);
}

void L_P1_C3_GUpdatePrev(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C3(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C3(proc_id);
    L_P1__SetSubcl70(my_id, L_P1__GetInSubcl69(my_id));
    L_P1__SetSubcl72(my_id, L_P1__GetInSubcl71(my_id));
    L_P1__SetSubcl74(my_id, L_P1__GetInSubcl73(my_id));
    L_P1__SetSubcl76(my_id, L_P1__GetInSubcl75(my_id));
    L_P1__SetSubcl78(my_id, L_P1__GetInSubcl77(my_id));
    L_P1__SetSubcl80(my_id, L_P1__GetSubcl79(my_id));
    L_P1__SetSubcl82(my_id, L_P1__GetSubcl81(my_id));
    L_P1__SetSubcl84(my_id, L_P1__GetSubcl83(my_id));
    L_P1__SetSubcl86(my_id, L_P1__GetSubcl85(my_id));
    L_P1__SetSubcl88(my_id, L_P1__GetSubcl87(my_id));
}

// ********** Definizione macro **********

// Macro di effetto

/*
    CNL corrispondente:
    
    { commento: {37,}  se la variabile SubClass_C3_variabile_V6 è  diverso da  False ,  Applica gli effetti
           della macro SubClass_C3_macroef_M6  commento: {73,}
    
     ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C3_variabile_V8 il valore  True 
    
    
     commento: {110,}  se il ripristino del timer  SubClass_C3_restoreTI_TI5 è scaduto,  Applica gli effetti
           della macro SubClass_C3_macroef_M6  commento: {73,}
    
       
    
    }
*/
void L_P1__Macro15(instance_id_t const my_id )
{
//  *37,*  se la variabile SubClass_C3_variabile_V6 è  diverso da  False ,  Applica gli effetti
    //       della macro SubClass_C3_macroef_M6  *73,*
    // ,altrimenti  *67,* Assegna alla variabile SubClass_C3_variabile_V8 il valore  True
    bool res_NotLogicOP_0 = true;
    res_NotLogicOP_0 = (res_NotLogicOP_0 && ! (L_P1__GetSubcl99(my_id) == false));
    if(res_NotLogicOP_0){
    
    L_P1__Macro16(my_id);
    }else{
    
    L_P1__SetSubcl101(my_id,true);
    }
    //  *110,*  se il ripristino del timer  SubClass_C3_restoreTI_TI5 è scaduto,  Applica gli effetti
    //       della macro SubClass_C3_macroef_M6
    if(Timer_Scaduto(L_P1__GetSubcl111(my_id))){
    
    L_P1__Macro16(my_id);
    }
}

/*
    CNL corrispondente:
    
    { commento: {109,}  se il ripristino della variabile  SubClass_C3_restoreva_RV3 è  diverso da  False , commento: {71,}Decrementa il contatore SubClass_C3_contatore_Co10
    
     ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C3_variabile_V8 il valore  False 
    
    
    
    }
*/
void L_P1__Macro16(instance_id_t const my_id )
{
//  *109,*  se il ripristino della variabile  SubClass_C3_restoreva_RV3 è  diverso da  False , *71,*Decrementa il contatore SubClass_C3_contatore_Co10
    // ,altrimenti  *67,* Assegna alla variabile SubClass_C3_variabile_V8 il valore  False
    bool res_NotLogicOP_0 = true;
    res_NotLogicOP_0 = (res_NotLogicOP_0 && ! (L_P1__GetSubcl94(my_id) == false));
    if(res_NotLogicOP_0){
    
    Counter_Decr(L_P1__GetSubcl114(my_id));
    }else{
    
    L_P1__SetSubcl101(my_id,false);
    }
}


// Macro di verifica

/*
    CNL corrispondente:
    
    { commento: {63,} commento: {109,}  se il ripristino della variabile  SubClass_C3_restoreva_RV3 è  diverso da  False  commento: {36,} o  se il timer SubClass_C3_timer_T4 è scaduto commento: {38,} o  se il contatore SubClass_C3_contatore_Co8 è  minore di  commento: {55,} 1515 e  se l'argomento argomento_ave4 non  è  uguale a RossoVerde commento: {39,} , Solo una delle seguenti { 
     commento: {62,} commento: {38,}  se il contatore SubClass_C3_contatore_Co2 non è  uguale a  commento: {53,} 130 commento: {35,} o  se il controllo SubClass_C3_controllo_C8 non è  uguale a RossoGialloVerde commento: {36,} o  se il timer SubClass_C3_timer_T6 non è scaduto commento: {35,} o  se il controllo SubClass_C3_controllo_C7 è  uguale a RossoGialloVerde commento: {35,} o  se il controllo SubClass_C3_controllo_C7 è  uguale a RossoGialloVerde commento: {35,} e  se il controllo SubClass_C3_controllo_C8 non è  uguale a RossoGialloVerde, Almeno una delle seguenti { 
     commento: {61,} commento: {34,}  se il parametro SubClass_C3_parametro_P5 non è  uguale a RossoVerde commento: {37,} e  se la variabile SubClass_C3_variabile_V6 non è  uguale a  True  commento: {36,} e  se il timer SubClass_C3_timer_T4 non è disattivo, Tutte le seguenti { 
     commento: {109,}  se il ripristino della variabile  SubClass_C3_restoreva_RV1 è  uguale a  commento: {53,} 4 o  se l'argomento argomento_ave4 è  uguale a RossoVerde commento: {39,}  commento: {37,} o  se la variabile SubClass_C3_variabile_V5 è  minore di  commento: {55,} 1, Verifica che   commento: {47,50,51,52,}  commento: {,}  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  commento: {56,} 124
     commento: {104,} e  che   l'argomento argomento_ave4 non  sia  diverso da RossoVerde commento: {,} 
     commento: {104,} e  che  commento: {38,}  il contatore SubClass_C3_contatore_Co2 sia  maggiore di  commento: {54,} 13
     commento: {104,} o  che  commento: {34,}  il parametro SubClass_C3_parametro_P5 sia  diverso da RossoVerde
     commento: {104,} o  che  commento: {,}  la variabile SubClass_C3_variabile_V6 non sia  uguale a  False 
     commento: {104,} e  che  commento: {34,}  il parametro SubClass_C3_parametro_P5 non sia  diverso da RossoVerde
    
    
     } Verifica che   commento: {50,51,}  commento: {,}  il contatore SubClass_C3_contatore_Co2 sia  minore di  commento: {55,} 1532
     commento: {104,} e  che  commento: {,}  la variabile SubClass_C3_variabile_V6 non sia  uguale a  True 
    
    
     } Verifica che   commento: {47,51,52,}  commento: {,}  il contatore SubClass_C3_contatore_Co8 sia  minore di  commento: {55,} 15
     commento: {104,} e  che   l'argomento argomento_ave3 sia  diverso da avanzamentox commento: {,} 
     commento: {104,} e  che  commento: {34,}  il parametro SubClass_C3_parametro_P7 sia  maggiore di  commento: {54,} 3
    
    
     } Verifica che   commento: {47,49,}  commento: {34,}  il parametro SubClass_C3_parametro_P5 non sia  diverso da RossoVerde
     commento: {104,} o  che  commento: {,}  il timer SubClass_C3_timer_T4 sia attivo
    
    
    }
*/
bool L_P1__Macro20(instance_id_t const my_id , C3_Enumerat4 argom46, C3_Enumerat1 argom47, C3_Enumerat2 argom48)
{
bool res_AndLogicOP_0 = true;
    
    //  *63,* *109,*  se il ripristino della variabile  SubClass_C3_restoreva_RV3 è  diverso da  False  *36,* o  se il timer SubClass_C3_timer_T4 è scaduto *38,* o  se il contatore SubClass_C3_contatore_Co8 è  minore di  *55,* 1515 e  se l'argomento argomento_ave4 non  è  uguale a RossoVerde *39,* , Solo una delle seguenti { 
    //   *62,* *38,*  se il contatore SubClass_C3_contatore_Co2 non è  uguale a  *53,* 130 *35,* o  se il controllo SubClass_C3_controllo_C8 non è  uguale a RossoGialloVerde *36,* o  se il timer SubClass_C3_timer_T6 non è scaduto *35,* o  se il controllo SubClass_C3_controllo_C7 è  uguale a RossoGialloVerde *35,* o  se il controllo SubClass_C3_controllo_C7 è  uguale a RossoGialloVerde *35,* e  se il controllo SubClass_C3_controllo_C8 non è  uguale a RossoGialloVerde, Almeno una delle seguenti { 
    //   *61,* *34,*  se il parametro SubClass_C3_parametro_P5 non è  uguale a RossoVerde *37,* e  se la variabile SubClass_C3_variabile_V6 non è  uguale a  True  *36,* e  se il timer SubClass_C3_timer_T4 non è disattivo, Tutte le seguenti { 
    //   *109,*  se il ripristino della variabile  SubClass_C3_restoreva_RV1 è  uguale a  *53,* 4 o  se l'argomento argomento_ave4 è  uguale a RossoVerde *39,*  *37,* o  se la variabile SubClass_C3_variabile_V5 è  minore di  *55,* 1, Verifica che   *47,50,51,52,*  *,*  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  *56,* 124
    //   *104,* e  che   l'argomento argomento_ave4 non  sia  diverso da RossoVerde *,* 
    //   *104,* e  che  *38,*  il contatore SubClass_C3_contatore_Co2 sia  maggiore di  *54,* 13
    //   *104,* o  che  *34,*  il parametro SubClass_C3_parametro_P5 sia  diverso da RossoVerde
    //   *104,* o  che  *,*  la variabile SubClass_C3_variabile_V6 non sia  uguale a  False 
    //   *104,* e  che  *34,*  il parametro SubClass_C3_parametro_P5 non sia  diverso da RossoVerde
    //   } Verifica che   *50,51,*  *,*  il contatore SubClass_C3_contatore_Co2 sia  minore di  *55,* 1532
    //   *104,* e  che  *,*  la variabile SubClass_C3_variabile_V6 non sia  uguale a  True 
    //   } Verifica che   *47,51,52,*  *,*  il contatore SubClass_C3_contatore_Co8 sia  minore di  *55,* 15
    //   *104,* e  che   l'argomento argomento_ave3 sia  diverso da avanzamentox *,* 
    //   *104,* e  che  *34,*  il parametro SubClass_C3_parametro_P7 sia  maggiore di  *54,* 3
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetSubcl94(my_id) == false));
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_NotLogicOP_4);
    res_OrLogicOP_3 = (res_OrLogicOP_3 || Timer_Scaduto(L_P1__GetSubcl112(my_id)));
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    bool res_AndLogicOP_5 = true;
    res_AndLogicOP_5 = (res_AndLogicOP_5 && (Counter_GetValore(L_P1__GetSubcl116(my_id)) < 1515u));
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (argom47 == rossoverde));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_6);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_5);
    
    if(res_OrLogicOP_2){
    bool res_XorLogicOP_7 = true;
    int xorIndex_res_XorLogicOP_7 = 0;
    bool res_ImpliesLogicOp_8 = true;
    bool res_OrLogicOP_9 = false;
    bool res_OrLogicOP_10 = false;
    bool res_OrLogicOP_11 = false;
    bool res_OrLogicOP_12 = false;
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (Counter_GetValore(L_P1__GetSubcl115(my_id)) == 130u));
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_NotLogicOP_13);
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1__GetInSubcl61(my_id) == rossogiallo4));
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_NotLogicOP_14);
    
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_OrLogicOP_12);
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! Timer_Scaduto(L_P1__GetSubcl113(my_id)));
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_NotLogicOP_15);
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_OrLogicOP_11);
    res_OrLogicOP_10 = (res_OrLogicOP_10 || (L_P1__GetInSubcl60(my_id) == rossogiallo4));
    
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_OrLogicOP_10);
    bool res_AndLogicOP_16 = true;
    res_AndLogicOP_16 = (res_AndLogicOP_16 && (L_P1__GetInSubcl60(my_id) == rossogiallo4));
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! (L_P1__GetInSubcl61(my_id) == rossogiallo4));
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_NotLogicOP_17);
    
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_AndLogicOP_16);
    
    if(res_OrLogicOP_9){
    bool res_OrLogicOP_18 = false;
    bool res_ImpliesLogicOp_19 = true;
    bool res_AndLogicOP_20 = true;
    bool res_AndLogicOP_21 = true;
    bool res_NotLogicOP_22 = true;
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! (L_P1__GetParamSubcl66(my_id) == rossoverde));
    res_AndLogicOP_21 = (res_AndLogicOP_21 && res_NotLogicOP_22);
    bool res_NotLogicOP_23 = true;
    res_NotLogicOP_23 = (res_NotLogicOP_23 && ! (L_P1__GetSubcl99(my_id) == true));
    res_AndLogicOP_21 = (res_AndLogicOP_21 && res_NotLogicOP_23);
    
    res_AndLogicOP_20 = (res_AndLogicOP_20 && res_AndLogicOP_21);
    bool res_NotLogicOP_24 = true;
    res_NotLogicOP_24 = (res_NotLogicOP_24 && ! Timer_Disattivo(L_P1__GetSubcl112(my_id)));
    res_AndLogicOP_20 = (res_AndLogicOP_20 && res_NotLogicOP_24);
    
    if(res_AndLogicOP_20){
    bool res_ImpliesLogicOp_25 = true;
    bool res_OrLogicOP_26 = false;
    bool res_OrLogicOP_27 = false;
    res_OrLogicOP_27 = (res_OrLogicOP_27 || (L_P1__GetSubcl90(my_id) == 4u));
    res_OrLogicOP_27 = (res_OrLogicOP_27 || (argom47 == rossoverde));
    
    res_OrLogicOP_26 = (res_OrLogicOP_26 || res_OrLogicOP_27);
    res_OrLogicOP_26 = (res_OrLogicOP_26 || (L_P1__GetSubcl98(my_id) < 1u));
    
    if(res_OrLogicOP_26){
    bool res_OrLogicOP_28 = false;
    bool res_OrLogicOP_29 = false;
    bool res_AndLogicOP_30 = true;
    bool res_AndLogicOP_31 = true;
    bool res_NotLogicOP_32 = true;
    bool res_NotLogicOP_33 = true;
    res_NotLogicOP_33 = (res_NotLogicOP_33 && ! (Counter_GetValore(L_P1__GetSubcl115(my_id)) == 124u));
    res_NotLogicOP_32 = (res_NotLogicOP_32 && ! res_NotLogicOP_33);
    res_AndLogicOP_31 = (res_AndLogicOP_31 && res_NotLogicOP_32);
    bool res_NotLogicOP_34 = true;
    bool res_NotLogicOP_35 = true;
    res_NotLogicOP_35 = (res_NotLogicOP_35 && ! (argom47 == rossoverde));
    res_NotLogicOP_34 = (res_NotLogicOP_34 && ! res_NotLogicOP_35);
    res_AndLogicOP_31 = (res_AndLogicOP_31 && res_NotLogicOP_34);
    
    res_AndLogicOP_30 = (res_AndLogicOP_30 && res_AndLogicOP_31);
    res_AndLogicOP_30 = (res_AndLogicOP_30 && (Counter_GetValore(L_P1__GetSubcl115(my_id)) > 13u));
    
    res_OrLogicOP_29 = (res_OrLogicOP_29 || res_AndLogicOP_30);
    bool res_NotLogicOP_36 = true;
    res_NotLogicOP_36 = (res_NotLogicOP_36 && ! (L_P1__GetParamSubcl66(my_id) == rossoverde));
    res_OrLogicOP_29 = (res_OrLogicOP_29 || res_NotLogicOP_36);
    
    res_OrLogicOP_28 = (res_OrLogicOP_28 || res_OrLogicOP_29);
    bool res_AndLogicOP_37 = true;
    bool res_NotLogicOP_38 = true;
    res_NotLogicOP_38 = (res_NotLogicOP_38 && ! (L_P1__GetSubcl99(my_id) == false));
    res_AndLogicOP_37 = (res_AndLogicOP_37 && res_NotLogicOP_38);
    bool res_NotLogicOP_39 = true;
    bool res_NotLogicOP_40 = true;
    res_NotLogicOP_40 = (res_NotLogicOP_40 && ! (L_P1__GetParamSubcl66(my_id) == rossoverde));
    res_NotLogicOP_39 = (res_NotLogicOP_39 && ! res_NotLogicOP_40);
    res_AndLogicOP_37 = (res_AndLogicOP_37 && res_NotLogicOP_39);
    
    res_OrLogicOP_28 = (res_OrLogicOP_28 || res_AndLogicOP_37);
    
    res_ImpliesLogicOp_25 = (res_ImpliesLogicOp_25 && res_OrLogicOP_28);
    }
    res_ImpliesLogicOp_19 = (res_ImpliesLogicOp_19 && res_ImpliesLogicOp_25);
    }
    res_OrLogicOP_18 = (res_OrLogicOP_18 || res_ImpliesLogicOp_19);
    bool res_AndLogicOP_41 = true;
    res_AndLogicOP_41 = (res_AndLogicOP_41 && (Counter_GetValore(L_P1__GetSubcl115(my_id)) < 1532u));
    bool res_NotLogicOP_42 = true;
    res_NotLogicOP_42 = (res_NotLogicOP_42 && ! (L_P1__GetSubcl99(my_id) == true));
    res_AndLogicOP_41 = (res_AndLogicOP_41 && res_NotLogicOP_42);
    
    res_OrLogicOP_18 = (res_OrLogicOP_18 || res_AndLogicOP_41);
    
    res_ImpliesLogicOp_8 = (res_ImpliesLogicOp_8 && res_OrLogicOP_18);
    }
    if(res_ImpliesLogicOp_8){
    xorIndex_res_XorLogicOP_7 = (xorIndex_res_XorLogicOP_7 + 1);
    }
    bool res_AndLogicOP_43 = true;
    bool res_AndLogicOP_44 = true;
    res_AndLogicOP_44 = (res_AndLogicOP_44 && (Counter_GetValore(L_P1__GetSubcl116(my_id)) < 15u));
    bool res_NotLogicOP_45 = true;
    res_NotLogicOP_45 = (res_NotLogicOP_45 && ! (argom46 == avanzamento));
    res_AndLogicOP_44 = (res_AndLogicOP_44 && res_NotLogicOP_45);
    
    res_AndLogicOP_43 = (res_AndLogicOP_43 && res_AndLogicOP_44);
    res_AndLogicOP_43 = (res_AndLogicOP_43 && (L_P1__GetParamSubcl67(my_id) > 3u));
    
    if(res_AndLogicOP_43){
    xorIndex_res_XorLogicOP_7 = (xorIndex_res_XorLogicOP_7 + 1);
    }
    
    res_XorLogicOP_7 = (res_XorLogicOP_7 && (xorIndex_res_XorLogicOP_7 == 1));
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_XorLogicOP_7);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *47,49,*  *34,*  il parametro SubClass_C3_parametro_P5 non sia  diverso da RossoVerde
    //   *104,* o  che  *,*  il timer SubClass_C3_timer_T4 sia attivo
    bool res_OrLogicOP_46 = false;
    bool res_NotLogicOP_47 = true;
    bool res_NotLogicOP_48 = true;
    res_NotLogicOP_48 = (res_NotLogicOP_48 && ! (L_P1__GetParamSubcl66(my_id) == rossoverde));
    res_NotLogicOP_47 = (res_NotLogicOP_47 && ! res_NotLogicOP_48);
    res_OrLogicOP_46 = (res_OrLogicOP_46 || res_NotLogicOP_47);
    res_OrLogicOP_46 = (res_OrLogicOP_46 || Timer_Attivo(L_P1__GetSubcl112(my_id)));
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_46);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
    
    { commento: {61,} commento: {38,}  se il contatore SubClass_C3_contatore_Co8 non è  diverso da  commento: {56,} 1121 commento: {35,} o  se il controllo SubClass_C3_controllo_C7 è  uguale a RossoGialloVerde, Tutte le seguenti { 
     commento: {63,} commento: {34,}  se il parametro SubClass_C3_parametro_P8 è  uguale a  True  commento: {36,} e  se il timer SubClass_C3_timer_T6 è disattivo commento: {35,} o  se il controllo SubClass_C3_controllo_C9 è  uguale a  False , Solo una delle seguenti { 
     commento: {61,} commento: {37,}  se la variabile SubClass_C3_variabile_V5 non è  minore di  commento: {55,} 8,  commento: {45,}  se  MainClass_C1_contatore_Co5 del campo  MainClass_C1 di SubClass_C3_lista_L1 esiste e  commento: {105,} è  minore di  commento: {55,} 15504, commento: {88,} quando  commento: {45,}    MainClass_C1_contatore_Co1 del campo  MainClass_C1     è  uguale a  commento: {53,} 14321 commento: {34,} e  se il parametro SubClass_C3_parametro_P5 è  uguale a RossoVerde commento: {38,} o  se il contatore SubClass_C3_contatore_Co8 è  diverso da  commento: {56,} 13 commento: {34,} e  se il parametro SubClass_C3_parametro_P8 è  uguale a  True , Tutte le seguenti { 
     commento: {61,} commento: {110,}  se il ripristino del timer  SubClass_C3_restoreTI_TI3 è attivo, Tutte le seguenti { 
     commento: {61,} commento: {38,}  se il contatore SubClass_C3_contatore_Co2 non è  diverso da  commento: {56,} 1350,  commento: {44,}  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  commento: {105,} è  diverso da c270x, commento: {88,} quando  commento: {42,}    MainClass_C1_controllo_C7 del campo  MainClass_C1     è  uguale a GialloxVerdex commento: {36,} o  se il timer SubClass_C3_timer_T4 è disattivo commento: {36,} o  se il timer SubClass_C3_timer_T4 è scaduto commento: {37,} e  se la variabile SubClass_C3_variabile_V2 non è  uguale a c120 commento: {36,} e  se il timer SubClass_C3_timer_T4 non è attivo commento: {35,} o  se il controllo SubClass_C3_controllo_C8 non è  uguale a RossoGialloVerde, Tutte le seguenti { 
     commento: {62,}  se la macro  SubClass_C3_macrova_M3 ( con argomento_a2   uguale a RossoGialloaVerdea ,argomento_a8   uguale a RossoVerde ,argomento_a6   uguale a RossoVerde  e argomento_a9   uguale a c180 )  non  è  diverso da  False  commento: {40,}  commento: {38,} e  se il contatore SubClass_C3_contatore_Co9 non è  minore di  commento: {55,} 13432, Almeno una delle seguenti { 
     commento: {63,} commento: {44,}  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  commento: {105,} è  diverso da  True  commento: {35,} o  se il controllo SubClass_C3_controllo_C5 è  diverso da RossoGialloVerde o  se l'argomento argomento_ave1 è  diverso da RossoVerde commento: {39,}  o  se l'argomento argomento_ave1 è  diverso da RossoVerde commento: {39,}  e  se l'argomento argomento_ave1 è  uguale a RossoVerde commento: {39,}  commento: {38,} e  se il contatore SubClass_C3_contatore_Co9 non è  minore di  commento: {55,} 1115, Solo una delle seguenti { 
     commento: {62,} commento: {34,}  se lo stato  non è  uguale a  commento: {53,}  state1  commento: {106,}, Almeno una delle seguenti { 
     commento: {61,} commento: {42,}  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C3_lista_L1 è  uguale a GialloxVerdex commento: {34,} e  se il parametro SubClass_C3_parametro_P5 è  diverso da RossoVerde commento: {35,} e  se il controllo SubClass_C3_controllo_C7 non è  uguale a RossoGialloVerde commento: {35,} e  se il controllo SubClass_C3_controllo_C8 non è  uguale a RossoGialloVerde, Tutte le seguenti { 
     commento: {63,} commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  commento: {105,} è  uguale a  commento: {53,}  state1  commento: {36,} e  se il timer SubClass_C3_timer_T4 non è attivo commento: {37,} o  se la variabile SubClass_C3_variabile_V6 è  uguale a  False  commento: {37,} o  se la variabile SubClass_C3_variabile_V6 non è  diverso da  True , Solo una delle seguenti { 
     commento: {61,} commento: {44,}  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  commento: {105,} è  diverso da  False  commento: {36,} o  se il timer SubClass_C3_timer_T4 è disattivo commento: {37,} o  se la variabile SubClass_C3_variabile_V8 non è  uguale a  False  commento: {36,} e  se il timer SubClass_C3_timer_T4 è attivo commento: {35,} o  se il controllo SubClass_C3_controllo_C7 non è  diverso da RossoGialloVerde commento: {37,} e  se la variabile SubClass_C3_variabile_V8 è  diverso da  False , Tutte le seguenti { 
     commento: {41,}  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  commento: {105,} è  uguale a c270x o  se l'argomento argomento_ave5 è  uguale a RossoVerde commento: {39,} , Verifica che   commento: {47,50,52,}  commento: {,}  la variabile SubClass_C3_variabile_V8 sia  uguale a  True 
     commento: {104,} e  che  commento: {34,}  il parametro SubClass_C3_parametro_P5 sia  diverso da RossoVerde
     commento: {104,} e  che   l'argomento argomento_ave5 sia  diverso da RossoVerde commento: {,} 
    
    
     } Verifica che   commento: {51,}  commento: {,}  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  commento: {56,} 133
    
    
     } Verifica che   commento: {47,52,}   l'argomento argomento_ave1 sia  diverso da RossoVerde commento: {,} 
     commento: {104,} e  che  commento: {34,}  il parametro SubClass_C3_parametro_P5 non sia  diverso da RossoVerde
    
    
     } Verifica che   commento: {52,}   l'argomento argomento_ave1 sia  uguale a RossoVerde commento: {,} 
     commento: {104,} e  che   l'argomento argomento_ave10 non  sia  uguale a  False  commento: {39,} 
    
    
     } Verifica che   commento: {50,}  commento: {,}  la variabile SubClass_C3_variabile_V8 non sia  uguale a  True 
    
    
     } Verifica che   commento: {47,49,50,51,}  commento: {34,}  il parametro SubClass_C3_parametro_P8 non sia  uguale a  False 
     commento: {104,} o  che  commento: {,}  il timer SubClass_C3_timer_T4 sia scaduto
     commento: {104,} o  che  commento: {,}  la variabile SubClass_C3_variabile_V6 sia  uguale a  False 
     commento: {104,} e  che  commento: {,}  il contatore SubClass_C3_contatore_Co2 sia  diverso da  commento: {56,} 11
    
    
     } Verifica che   commento: {47,48,}  commento: {34,}  il parametro SubClass_C3_parametro_P7 non sia  diverso da  commento: {56,} 9
     commento: {104,} o  che  commento: {,}  il controllo SubClass_C3_controllo_C5 non sia  diverso da RossoGialloVerde
     commento: {104,} e  che  commento: {34,}  il parametro SubClass_C3_parametro_P7 non sia  minore di  commento: {55,} 4
    
    
     } Verifica che   commento: {50,51,}  commento: {,}  la variabile SubClass_C3_variabile_V7 sia  uguale a RossoGialloVerde
     commento: {104,} e  che  commento: {,}  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  commento: {56,} 12
    
    
     } Verifica che   commento: {48,49,50,}  commento: {,}  la variabile SubClass_C3_variabile_V6 non sia  diverso da  True 
     commento: {104,} e  che  commento: {,}  il controllo SubClass_C3_controllo_C9 non sia  uguale a  False 
     commento: {104,} e  che  commento: {37,}  la variabile SubClass_C3_variabile_V6 non sia  uguale a  True 
     commento: {104,} o  che  commento: {,}  il timer SubClass_C3_timer_T6 sia scaduto
    
    
     } Verifica che   commento: {50,}  commento: {,}  la variabile SubClass_C3_variabile_V6 sia  diverso da  True 
    
    
     } Verifica che   commento: {48,49,51,52,}  commento: {,}  il timer SubClass_C3_timer_T6 non sia scaduto
     commento: {104,} e  che  commento: {,}  il contatore SubClass_C3_contatore_Co2 sia  diverso da  commento: {56,} 11
     commento: {104,} o  che  commento: {38,}  il contatore SubClass_C3_contatore_Co8 sia  minore di  commento: {55,} 155
     commento: {104,} e  che  commento: {36,}  il timer SubClass_C3_timer_T6 non sia scaduto
     commento: {104,} o  che   l'argomento argomento_ave10 non  sia  uguale a  True  commento: {,} 
     commento: {104,} e  che  commento: {,}  il controllo SubClass_C3_controllo_C7 non sia  diverso da RossoGialloVerde
    
    
     } Verifica che   commento: {50,51,52,}  commento: {,}  la variabile SubClass_C3_variabile_V6 sia  uguale a  True 
     commento: {104,} e  che   l'argomento argomento_ave1 sia  uguale a RossoVerde commento: {,} 
     commento: {104,} e  che  commento: {,}  il contatore SubClass_C3_contatore_Co2 sia  uguale a  commento: {53,} 1504
    
    
    }
*/
bool L_P1__Macro21(instance_id_t const my_id , C3_Enumerat1 argom49, bool argom50, C3_Enumerat1 argom51, C3_Enumerat1 argom52)
{
bool res_AndLogicOP_0 = true;
    
    //  *61,* *38,*  se il contatore SubClass_C3_contatore_Co8 non è  diverso da  *56,* 1121 *35,* o  se il controllo SubClass_C3_controllo_C7 è  uguale a RossoGialloVerde, Tutte le seguenti { 
    //   *63,* *34,*  se il parametro SubClass_C3_parametro_P8 è  uguale a  True  *36,* e  se il timer SubClass_C3_timer_T6 è disattivo *35,* o  se il controllo SubClass_C3_controllo_C9 è  uguale a  False , Solo una delle seguenti { 
    //   *61,* *37,*  se la variabile SubClass_C3_variabile_V5 non è  minore di  *55,* 8,  *45,*  se  MainClass_C1_contatore_Co5 del campo  MainClass_C1 di SubClass_C3_lista_L1 esiste e  *105,* è  minore di  *55,* 15504, *88,* quando  *45,*    MainClass_C1_contatore_Co1 del campo  MainClass_C1     è  uguale a  *53,* 14321 *34,* e  se il parametro SubClass_C3_parametro_P5 è  uguale a RossoVerde *38,* o  se il contatore SubClass_C3_contatore_Co8 è  diverso da  *56,* 13 *34,* e  se il parametro SubClass_C3_parametro_P8 è  uguale a  True , Tutte le seguenti { 
    //   *61,* *110,*  se il ripristino del timer  SubClass_C3_restoreTI_TI3 è attivo, Tutte le seguenti { 
    //   *61,* *38,*  se il contatore SubClass_C3_contatore_Co2 non è  diverso da  *56,* 1350,  *44,*  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  *105,* è  diverso da c270x, *88,* quando  *42,*    MainClass_C1_controllo_C7 del campo  MainClass_C1     è  uguale a GialloxVerdex *36,* o  se il timer SubClass_C3_timer_T4 è disattivo *36,* o  se il timer SubClass_C3_timer_T4 è scaduto *37,* e  se la variabile SubClass_C3_variabile_V2 non è  uguale a c120 *36,* e  se il timer SubClass_C3_timer_T4 non è attivo *35,* o  se il controllo SubClass_C3_controllo_C8 non è  uguale a RossoGialloVerde, Tutte le seguenti { 
    //   *62,*  se la macro  SubClass_C3_macrova_M3 ( con argomento_a2   uguale a RossoGialloaVerdea ,argomento_a8   uguale a RossoVerde ,argomento_a6   uguale a RossoVerde  e argomento_a9   uguale a c180 )  non  è  diverso da  False  *40,*  *38,* e  se il contatore SubClass_C3_contatore_Co9 non è  minore di  *55,* 13432, Almeno una delle seguenti { 
    //   *63,* *44,*  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  *105,* è  diverso da  True  *35,* o  se il controllo SubClass_C3_controllo_C5 è  diverso da RossoGialloVerde o  se l'argomento argomento_ave1 è  diverso da RossoVerde *39,*  o  se l'argomento argomento_ave1 è  diverso da RossoVerde *39,*  e  se l'argomento argomento_ave1 è  uguale a RossoVerde *39,*  *38,* e  se il contatore SubClass_C3_contatore_Co9 non è  minore di  *55,* 1115, Solo una delle seguenti { 
    //   *62,* *34,*  se lo stato  non è  uguale a  *53,*  state1  *106,*, Almeno una delle seguenti { 
    //   *61,* *42,*  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C3_lista_L1 è  uguale a GialloxVerdex *34,* e  se il parametro SubClass_C3_parametro_P5 è  diverso da RossoVerde *35,* e  se il controllo SubClass_C3_controllo_C7 non è  uguale a RossoGialloVerde *35,* e  se il controllo SubClass_C3_controllo_C8 non è  uguale a RossoGialloVerde, Tutte le seguenti { 
    //   *63,* *111,*  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  *105,* è  uguale a  *53,*  state1  *36,* e  se il timer SubClass_C3_timer_T4 non è attivo *37,* o  se la variabile SubClass_C3_variabile_V6 è  uguale a  False  *37,* o  se la variabile SubClass_C3_variabile_V6 non è  diverso da  True , Solo una delle seguenti { 
    //   *61,* *44,*  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  *105,* è  diverso da  False  *36,* o  se il timer SubClass_C3_timer_T4 è disattivo *37,* o  se la variabile SubClass_C3_variabile_V8 non è  uguale a  False  *36,* e  se il timer SubClass_C3_timer_T4 è attivo *35,* o  se il controllo SubClass_C3_controllo_C7 non è  diverso da RossoGialloVerde *37,* e  se la variabile SubClass_C3_variabile_V8 è  diverso da  False , Tutte le seguenti { 
    //   *41,*  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  *105,* è  uguale a c270x o  se l'argomento argomento_ave5 è  uguale a RossoVerde *39,* , Verifica che   *47,50,52,*  *,*  la variabile SubClass_C3_variabile_V8 sia  uguale a  True 
    //   *104,* e  che  *34,*  il parametro SubClass_C3_parametro_P5 sia  diverso da RossoVerde
    //   *104,* e  che   l'argomento argomento_ave5 sia  diverso da RossoVerde *,* 
    //   } Verifica che   *51,*  *,*  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  *56,* 133
    //   } Verifica che   *47,52,*   l'argomento argomento_ave1 sia  diverso da RossoVerde *,* 
    //   *104,* e  che  *34,*  il parametro SubClass_C3_parametro_P5 non sia  diverso da RossoVerde
    //   } Verifica che   *52,*   l'argomento argomento_ave1 sia  uguale a RossoVerde *,* 
    //   *104,* e  che   l'argomento argomento_ave10 non  sia  uguale a  False  *39,* 
    //   } Verifica che   *50,*  *,*  la variabile SubClass_C3_variabile_V8 non sia  uguale a  True 
    //   } Verifica che   *47,49,50,51,*  *34,*  il parametro SubClass_C3_parametro_P8 non sia  uguale a  False 
    //   *104,* o  che  *,*  il timer SubClass_C3_timer_T4 sia scaduto
    //   *104,* o  che  *,*  la variabile SubClass_C3_variabile_V6 sia  uguale a  False 
    //   *104,* e  che  *,*  il contatore SubClass_C3_contatore_Co2 sia  diverso da  *56,* 11
    //   } Verifica che   *47,48,*  *34,*  il parametro SubClass_C3_parametro_P7 non sia  diverso da  *56,* 9
    //   *104,* o  che  *,*  il controllo SubClass_C3_controllo_C5 non sia  diverso da RossoGialloVerde
    //   *104,* e  che  *34,*  il parametro SubClass_C3_parametro_P7 non sia  minore di  *55,* 4
    //   } Verifica che   *50,51,*  *,*  la variabile SubClass_C3_variabile_V7 sia  uguale a RossoGialloVerde
    //   *104,* e  che  *,*  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  *56,* 12
    //   } Verifica che   *48,49,50,*  *,*  la variabile SubClass_C3_variabile_V6 non sia  diverso da  True 
    //   *104,* e  che  *,*  il controllo SubClass_C3_controllo_C9 non sia  uguale a  False 
    //   *104,* e  che  *37,*  la variabile SubClass_C3_variabile_V6 non sia  uguale a  True 
    //   *104,* o  che  *,*  il timer SubClass_C3_timer_T6 sia scaduto
    //   } Verifica che   *50,*  *,*  la variabile SubClass_C3_variabile_V6 sia  diverso da  True 
    //   } Verifica che   *48,49,51,52,*  *,*  il timer SubClass_C3_timer_T6 non sia scaduto
    //   *104,* e  che  *,*  il contatore SubClass_C3_contatore_Co2 sia  diverso da  *56,* 11
    //   *104,* o  che  *38,*  il contatore SubClass_C3_contatore_Co8 sia  minore di  *55,* 155
    //   *104,* e  che  *36,*  il timer SubClass_C3_timer_T6 non sia scaduto
    //   *104,* o  che   l'argomento argomento_ave10 non  sia  uguale a  True  *,* 
    //   *104,* e  che  *,*  il controllo SubClass_C3_controllo_C7 non sia  diverso da RossoGialloVerde
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_NotLogicOP_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (Counter_GetValore(L_P1__GetSubcl116(my_id)) == 1121u));
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! res_NotLogicOP_4);
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_3);
    res_OrLogicOP_2 = (res_OrLogicOP_2 || (L_P1__GetInSubcl60(my_id) == rossogiallo4));
    
    if(res_OrLogicOP_2){
    bool res_AndLogicOP_5 = true;
    bool res_ImpliesLogicOp_6 = true;
    bool res_OrLogicOP_7 = false;
    bool res_AndLogicOP_8 = true;
    res_AndLogicOP_8 = (res_AndLogicOP_8 && (L_P1__GetParamSubcl68(my_id) == true));
    res_AndLogicOP_8 = (res_AndLogicOP_8 && Timer_Disattivo(L_P1__GetSubcl113(my_id)));
    
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_AndLogicOP_8);
    res_OrLogicOP_7 = (res_OrLogicOP_7 || (L_P1__GetInSubcl62(my_id) == false));
    
    if(res_OrLogicOP_7){
    bool res_XorLogicOP_9 = true;
    int xorIndex_res_XorLogicOP_9 = 0;
    bool res_ImpliesLogicOp_10 = true;
    bool res_OrLogicOP_11 = false;
    bool res_AndLogicOP_12 = true;
    bool res_AndLogicOP_13 = true;
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1__GetSubcl98(my_id) < 8u));
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_NotLogicOP_14);
    bool res_ForAllPredicateNotEmpty_15 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl63Length(my_id); ++i)
    {
    L_P1__Recor2 it = L_P1__GetRecSubcl63(my_id,i);
    bool res_ImpliesLogicOp_16 = true;
    if((Counter_GetValore(L_P1__GetMainc33(it.mainc38)) == 14321u)){
    res_ImpliesLogicOp_16 = (res_ImpliesLogicOp_16 && (Counter_GetValore(L_P1__GetMainc35(it.mainc38)) < 15504u));
    res_ForAllPredicateNotEmpty_15 = res_ImpliesLogicOp_16;
    if(!res_ForAllPredicateNotEmpty_15) {break;}
    }
    }
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_ForAllPredicateNotEmpty_15);
    
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_AndLogicOP_13);
    res_AndLogicOP_12 = (res_AndLogicOP_12 && (L_P1__GetParamSubcl66(my_id) == rossoverde));
    
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_AndLogicOP_12);
    bool res_AndLogicOP_17 = true;
    bool res_NotLogicOP_18 = true;
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! (Counter_GetValore(L_P1__GetSubcl116(my_id)) == 13u));
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_NotLogicOP_18);
    res_AndLogicOP_17 = (res_AndLogicOP_17 && (L_P1__GetParamSubcl68(my_id) == true));
    
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_AndLogicOP_17);
    
    if(res_OrLogicOP_11){
    bool res_AndLogicOP_19 = true;
    bool res_ImpliesLogicOp_20 = true;
    if(Timer_Attivo(L_P1__GetSubcl107(my_id))){
    bool res_AndLogicOP_21 = true;
    bool res_ImpliesLogicOp_22 = true;
    bool res_OrLogicOP_23 = false;
    bool res_OrLogicOP_24 = false;
    bool res_OrLogicOP_25 = false;
    bool res_AndLogicOP_26 = true;
    bool res_NotLogicOP_27 = true;
    bool res_NotLogicOP_28 = true;
    res_NotLogicOP_28 = (res_NotLogicOP_28 && ! (Counter_GetValore(L_P1__GetSubcl115(my_id)) == 1350u));
    res_NotLogicOP_27 = (res_NotLogicOP_27 && ! res_NotLogicOP_28);
    res_AndLogicOP_26 = (res_AndLogicOP_26 && res_NotLogicOP_27);
    bool res_ForAllPredicateNotEmpty_29 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl64Length(my_id); ++i)
    {
    L_P1__Recor2 it = L_P1__GetRecSubcl64(my_id,i);
    bool res_ImpliesLogicOp_30 = true;
    if((L_P1__GetInMainc2(it.mainc38) == gialloxverd)){
    bool res_NotLogicOP_31 = true;
    res_NotLogicOP_31 = (res_NotLogicOP_31 && ! (L_P1__GetMainc24(it.mainc38) == c270x));
    res_ImpliesLogicOp_30 = (res_ImpliesLogicOp_30 && res_NotLogicOP_31);
    res_ForAllPredicateNotEmpty_29 = res_ImpliesLogicOp_30;
    if(!res_ForAllPredicateNotEmpty_29) {break;}
    }
    }
    res_AndLogicOP_26 = (res_AndLogicOP_26 && res_ForAllPredicateNotEmpty_29);
    
    res_OrLogicOP_25 = (res_OrLogicOP_25 || res_AndLogicOP_26);
    res_OrLogicOP_25 = (res_OrLogicOP_25 || Timer_Disattivo(L_P1__GetSubcl112(my_id)));
    
    res_OrLogicOP_24 = (res_OrLogicOP_24 || res_OrLogicOP_25);
    bool res_AndLogicOP_32 = true;
    bool res_AndLogicOP_33 = true;
    res_AndLogicOP_33 = (res_AndLogicOP_33 && Timer_Scaduto(L_P1__GetSubcl112(my_id)));
    bool res_NotLogicOP_34 = true;
    res_NotLogicOP_34 = (res_NotLogicOP_34 && ! (L_P1__GetSubcl97(my_id) == c120));
    res_AndLogicOP_33 = (res_AndLogicOP_33 && res_NotLogicOP_34);
    
    res_AndLogicOP_32 = (res_AndLogicOP_32 && res_AndLogicOP_33);
    bool res_NotLogicOP_35 = true;
    res_NotLogicOP_35 = (res_NotLogicOP_35 && ! Timer_Attivo(L_P1__GetSubcl112(my_id)));
    res_AndLogicOP_32 = (res_AndLogicOP_32 && res_NotLogicOP_35);
    
    res_OrLogicOP_24 = (res_OrLogicOP_24 || res_AndLogicOP_32);
    
    res_OrLogicOP_23 = (res_OrLogicOP_23 || res_OrLogicOP_24);
    bool res_NotLogicOP_36 = true;
    res_NotLogicOP_36 = (res_NotLogicOP_36 && ! (L_P1__GetInSubcl61(my_id) == rossogiallo4));
    res_OrLogicOP_23 = (res_OrLogicOP_23 || res_NotLogicOP_36);
    
    if(res_OrLogicOP_23){
    bool res_AndLogicOP_37 = true;
    bool res_ImpliesLogicOp_38 = true;
    bool res_AndLogicOP_39 = true;
    bool res_NotLogicOP_40 = true;
    bool res_NotLogicOP_41 = true;
    res_NotLogicOP_41 = (res_NotLogicOP_41 && ! (L_P1__Macro19(my_id,rossogiallo5,rossoverde,rossoverde,c180) == false));
    res_NotLogicOP_40 = (res_NotLogicOP_40 && ! res_NotLogicOP_41);
    res_AndLogicOP_39 = (res_AndLogicOP_39 && res_NotLogicOP_40);
    bool res_NotLogicOP_42 = true;
    res_NotLogicOP_42 = (res_NotLogicOP_42 && ! (Counter_GetValore(L_P1__GetSubcl117(my_id)) < 13432u));
    res_AndLogicOP_39 = (res_AndLogicOP_39 && res_NotLogicOP_42);
    
    if(res_AndLogicOP_39){
    bool res_OrLogicOP_43 = false;
    bool res_ImpliesLogicOp_44 = true;
    bool res_OrLogicOP_45 = false;
    bool res_OrLogicOP_46 = false;
    bool res_OrLogicOP_47 = false;
    bool res_ForAllPredicateNotEmpty_48 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl64Length(my_id); ++i)
    {
    L_P1__Recor2 it = L_P1__GetRecSubcl64(my_id,i);
    bool res_ImpliesLogicOp_49 = true;
    bool res_NotLogicOP_50 = true;
    res_NotLogicOP_50 = (res_NotLogicOP_50 && ! (L_P1__GetMainc22(it.mainc38) == true));
    res_ImpliesLogicOp_49 = (res_ImpliesLogicOp_49 && res_NotLogicOP_50);
    res_ForAllPredicateNotEmpty_48 = res_ImpliesLogicOp_49;
    if(!res_ForAllPredicateNotEmpty_48) {break;}
    }
    res_OrLogicOP_47 = (res_OrLogicOP_47 || res_ForAllPredicateNotEmpty_48);
    bool res_NotLogicOP_51 = true;
    res_NotLogicOP_51 = (res_NotLogicOP_51 && ! (L_P1__GetInSubcl59(my_id) == rossogiallo4));
    res_OrLogicOP_47 = (res_OrLogicOP_47 || res_NotLogicOP_51);
    
    res_OrLogicOP_46 = (res_OrLogicOP_46 || res_OrLogicOP_47);
    bool res_NotLogicOP_52 = true;
    res_NotLogicOP_52 = (res_NotLogicOP_52 && ! (argom49 == rossoverde));
    res_OrLogicOP_46 = (res_OrLogicOP_46 || res_NotLogicOP_52);
    
    res_OrLogicOP_45 = (res_OrLogicOP_45 || res_OrLogicOP_46);
    bool res_AndLogicOP_53 = true;
    bool res_AndLogicOP_54 = true;
    bool res_NotLogicOP_55 = true;
    res_NotLogicOP_55 = (res_NotLogicOP_55 && ! (argom49 == rossoverde));
    res_AndLogicOP_54 = (res_AndLogicOP_54 && res_NotLogicOP_55);
    res_AndLogicOP_54 = (res_AndLogicOP_54 && (argom49 == rossoverde));
    
    res_AndLogicOP_53 = (res_AndLogicOP_53 && res_AndLogicOP_54);
    bool res_NotLogicOP_56 = true;
    res_NotLogicOP_56 = (res_NotLogicOP_56 && ! (Counter_GetValore(L_P1__GetSubcl117(my_id)) < 1115u));
    res_AndLogicOP_53 = (res_AndLogicOP_53 && res_NotLogicOP_56);
    
    res_OrLogicOP_45 = (res_OrLogicOP_45 || res_AndLogicOP_53);
    
    if(res_OrLogicOP_45){
    bool res_XorLogicOP_57 = true;
    int xorIndex_res_XorLogicOP_57 = 0;
    bool res_ImpliesLogicOp_58 = true;
    bool res_NotLogicOP_59 = true;
    res_NotLogicOP_59 = (res_NotLogicOP_59 && ! (L_P1_C3_GetState(my_id) == C3_St_state));
    if(res_NotLogicOP_59){
    bool res_OrLogicOP_60 = false;
    bool res_ImpliesLogicOp_61 = true;
    bool res_AndLogicOP_62 = true;
    bool res_AndLogicOP_63 = true;
    bool res_AndLogicOP_64 = true;
    bool res_ForAllPredicate_65 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl63Length(my_id); ++i)
    {
    L_P1__Recor2 it = L_P1__GetRecSubcl63(my_id,i);
    bool res_ImpliesLogicOp_66 = true;
    res_ImpliesLogicOp_66 = (res_ImpliesLogicOp_66 && (L_P1__GetInMainc2(it.mainc38) == gialloxverd));
    res_ForAllPredicate_65 = res_ImpliesLogicOp_66;
    if(!res_ForAllPredicate_65) {break;}
    }
    res_AndLogicOP_64 = (res_AndLogicOP_64 && res_ForAllPredicate_65);
    bool res_NotLogicOP_67 = true;
    res_NotLogicOP_67 = (res_NotLogicOP_67 && ! (L_P1__GetParamSubcl66(my_id) == rossoverde));
    res_AndLogicOP_64 = (res_AndLogicOP_64 && res_NotLogicOP_67);
    
    res_AndLogicOP_63 = (res_AndLogicOP_63 && res_AndLogicOP_64);
    bool res_NotLogicOP_68 = true;
    res_NotLogicOP_68 = (res_NotLogicOP_68 && ! (L_P1__GetInSubcl60(my_id) == rossogiallo4));
    res_AndLogicOP_63 = (res_AndLogicOP_63 && res_NotLogicOP_68);
    
    res_AndLogicOP_62 = (res_AndLogicOP_62 && res_AndLogicOP_63);
    bool res_NotLogicOP_69 = true;
    res_NotLogicOP_69 = (res_NotLogicOP_69 && ! (L_P1__GetInSubcl61(my_id) == rossogiallo4));
    res_AndLogicOP_62 = (res_AndLogicOP_62 && res_NotLogicOP_69);
    
    if(res_AndLogicOP_62){
    bool res_AndLogicOP_70 = true;
    bool res_ImpliesLogicOp_71 = true;
    bool res_OrLogicOP_72 = false;
    bool res_OrLogicOP_73 = false;
    bool res_AndLogicOP_74 = true;
    bool res_ForAllPredicateNotEmpty_75 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl64Length(my_id); ++i)
    {
    L_P1__Recor2 it = L_P1__GetRecSubcl64(my_id,i);
    bool res_ImpliesLogicOp_76 = true;
    res_ImpliesLogicOp_76 = (res_ImpliesLogicOp_76 && (L_P1_C1_GetState(it.mainc38) == C1_St_state));
    res_ForAllPredicateNotEmpty_75 = res_ImpliesLogicOp_76;
    if(!res_ForAllPredicateNotEmpty_75) {break;}
    }
    res_AndLogicOP_74 = (res_AndLogicOP_74 && res_ForAllPredicateNotEmpty_75);
    bool res_NotLogicOP_77 = true;
    res_NotLogicOP_77 = (res_NotLogicOP_77 && ! Timer_Attivo(L_P1__GetSubcl112(my_id)));
    res_AndLogicOP_74 = (res_AndLogicOP_74 && res_NotLogicOP_77);
    
    res_OrLogicOP_73 = (res_OrLogicOP_73 || res_AndLogicOP_74);
    res_OrLogicOP_73 = (res_OrLogicOP_73 || (L_P1__GetSubcl99(my_id) == false));
    
    res_OrLogicOP_72 = (res_OrLogicOP_72 || res_OrLogicOP_73);
    bool res_NotLogicOP_78 = true;
    bool res_NotLogicOP_79 = true;
    res_NotLogicOP_79 = (res_NotLogicOP_79 && ! (L_P1__GetSubcl99(my_id) == true));
    res_NotLogicOP_78 = (res_NotLogicOP_78 && ! res_NotLogicOP_79);
    res_OrLogicOP_72 = (res_OrLogicOP_72 || res_NotLogicOP_78);
    
    if(res_OrLogicOP_72){
    bool res_XorLogicOP_80 = true;
    int xorIndex_res_XorLogicOP_80 = 0;
    bool res_ImpliesLogicOp_81 = true;
    bool res_OrLogicOP_82 = false;
    bool res_OrLogicOP_83 = false;
    bool res_OrLogicOP_84 = false;
    bool res_ForAllPredicateNotEmpty_85 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl65Length(my_id); ++i)
    {
    L_P1__Recor2 it = L_P1__GetRecSubcl65(my_id,i);
    bool res_ImpliesLogicOp_86 = true;
    bool res_NotLogicOP_87 = true;
    res_NotLogicOP_87 = (res_NotLogicOP_87 && ! (L_P1__GetMainc22(it.mainc38) == false));
    res_ImpliesLogicOp_86 = (res_ImpliesLogicOp_86 && res_NotLogicOP_87);
    res_ForAllPredicateNotEmpty_85 = res_ImpliesLogicOp_86;
    if(!res_ForAllPredicateNotEmpty_85) {break;}
    }
    res_OrLogicOP_84 = (res_OrLogicOP_84 || res_ForAllPredicateNotEmpty_85);
    res_OrLogicOP_84 = (res_OrLogicOP_84 || Timer_Disattivo(L_P1__GetSubcl112(my_id)));
    
    res_OrLogicOP_83 = (res_OrLogicOP_83 || res_OrLogicOP_84);
    bool res_AndLogicOP_88 = true;
    bool res_NotLogicOP_89 = true;
    res_NotLogicOP_89 = (res_NotLogicOP_89 && ! (L_P1__GetSubcl101(my_id) == false));
    res_AndLogicOP_88 = (res_AndLogicOP_88 && res_NotLogicOP_89);
    res_AndLogicOP_88 = (res_AndLogicOP_88 && Timer_Attivo(L_P1__GetSubcl112(my_id)));
    
    res_OrLogicOP_83 = (res_OrLogicOP_83 || res_AndLogicOP_88);
    
    res_OrLogicOP_82 = (res_OrLogicOP_82 || res_OrLogicOP_83);
    bool res_AndLogicOP_90 = true;
    bool res_NotLogicOP_91 = true;
    bool res_NotLogicOP_92 = true;
    res_NotLogicOP_92 = (res_NotLogicOP_92 && ! (L_P1__GetInSubcl60(my_id) == rossogiallo4));
    res_NotLogicOP_91 = (res_NotLogicOP_91 && ! res_NotLogicOP_92);
    res_AndLogicOP_90 = (res_AndLogicOP_90 && res_NotLogicOP_91);
    bool res_NotLogicOP_93 = true;
    res_NotLogicOP_93 = (res_NotLogicOP_93 && ! (L_P1__GetSubcl101(my_id) == false));
    res_AndLogicOP_90 = (res_AndLogicOP_90 && res_NotLogicOP_93);
    
    res_OrLogicOP_82 = (res_OrLogicOP_82 || res_AndLogicOP_90);
    
    if(res_OrLogicOP_82){
    bool res_ImpliesLogicOp_94 = true;
    bool res_OrLogicOP_95 = false;
    bool res_ForAllPredicateNotEmpty_96 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl65Length(my_id); ++i)
    {
    L_P1__Recor2 it = L_P1__GetRecSubcl65(my_id,i);
    bool res_ImpliesLogicOp_97 = true;
    res_ImpliesLogicOp_97 = (res_ImpliesLogicOp_97 && (L_P1__GetParamMainc5(it.mainc38) == c270x));
    res_ForAllPredicateNotEmpty_96 = res_ImpliesLogicOp_97;
    if(!res_ForAllPredicateNotEmpty_96) {break;}
    }
    res_OrLogicOP_95 = (res_OrLogicOP_95 || res_ForAllPredicateNotEmpty_96);
    res_OrLogicOP_95 = (res_OrLogicOP_95 || (argom52 == rossoverde));
    
    if(res_OrLogicOP_95){
    bool res_AndLogicOP_98 = true;
    bool res_AndLogicOP_99 = true;
    res_AndLogicOP_99 = (res_AndLogicOP_99 && (L_P1__GetSubcl101(my_id) == true));
    bool res_NotLogicOP_100 = true;
    res_NotLogicOP_100 = (res_NotLogicOP_100 && ! (L_P1__GetParamSubcl66(my_id) == rossoverde));
    res_AndLogicOP_99 = (res_AndLogicOP_99 && res_NotLogicOP_100);
    
    res_AndLogicOP_98 = (res_AndLogicOP_98 && res_AndLogicOP_99);
    bool res_NotLogicOP_101 = true;
    res_NotLogicOP_101 = (res_NotLogicOP_101 && ! (argom52 == rossoverde));
    res_AndLogicOP_98 = (res_AndLogicOP_98 && res_NotLogicOP_101);
    
    res_ImpliesLogicOp_94 = (res_ImpliesLogicOp_94 && res_AndLogicOP_98);
    }
    res_ImpliesLogicOp_81 = (res_ImpliesLogicOp_81 && res_ImpliesLogicOp_94);
    }
    if(res_ImpliesLogicOp_81){
    xorIndex_res_XorLogicOP_80 = (xorIndex_res_XorLogicOP_80 + 1);
    }
    bool res_NotLogicOP_102 = true;
    bool res_NotLogicOP_103 = true;
    res_NotLogicOP_103 = (res_NotLogicOP_103 && ! (Counter_GetValore(L_P1__GetSubcl115(my_id)) == 133u));
    res_NotLogicOP_102 = (res_NotLogicOP_102 && ! res_NotLogicOP_103);
    if(res_NotLogicOP_102){
    xorIndex_res_XorLogicOP_80 = (xorIndex_res_XorLogicOP_80 + 1);
    }
    
    res_XorLogicOP_80 = (res_XorLogicOP_80 && (xorIndex_res_XorLogicOP_80 == 1));
    res_ImpliesLogicOp_71 = (res_ImpliesLogicOp_71 && res_XorLogicOP_80);
    }
    res_AndLogicOP_70 = (res_AndLogicOP_70 && res_ImpliesLogicOp_71);
    bool res_AndLogicOP_104 = true;
    bool res_NotLogicOP_105 = true;
    res_NotLogicOP_105 = (res_NotLogicOP_105 && ! (argom49 == rossoverde));
    res_AndLogicOP_104 = (res_AndLogicOP_104 && res_NotLogicOP_105);
    bool res_NotLogicOP_106 = true;
    bool res_NotLogicOP_107 = true;
    res_NotLogicOP_107 = (res_NotLogicOP_107 && ! (L_P1__GetParamSubcl66(my_id) == rossoverde));
    res_NotLogicOP_106 = (res_NotLogicOP_106 && ! res_NotLogicOP_107);
    res_AndLogicOP_104 = (res_AndLogicOP_104 && res_NotLogicOP_106);
    
    res_AndLogicOP_70 = (res_AndLogicOP_70 && res_AndLogicOP_104);
    
    res_ImpliesLogicOp_61 = (res_ImpliesLogicOp_61 && res_AndLogicOP_70);
    }
    res_OrLogicOP_60 = (res_OrLogicOP_60 || res_ImpliesLogicOp_61);
    bool res_AndLogicOP_108 = true;
    res_AndLogicOP_108 = (res_AndLogicOP_108 && (argom49 == rossoverde));
    bool res_NotLogicOP_109 = true;
    res_NotLogicOP_109 = (res_NotLogicOP_109 && ! (argom50 == false));
    res_AndLogicOP_108 = (res_AndLogicOP_108 && res_NotLogicOP_109);
    
    res_OrLogicOP_60 = (res_OrLogicOP_60 || res_AndLogicOP_108);
    
    res_ImpliesLogicOp_58 = (res_ImpliesLogicOp_58 && res_OrLogicOP_60);
    }
    if(res_ImpliesLogicOp_58){
    xorIndex_res_XorLogicOP_57 = (xorIndex_res_XorLogicOP_57 + 1);
    }
    bool res_NotLogicOP_110 = true;
    res_NotLogicOP_110 = (res_NotLogicOP_110 && ! (L_P1__GetSubcl101(my_id) == true));
    if(res_NotLogicOP_110){
    xorIndex_res_XorLogicOP_57 = (xorIndex_res_XorLogicOP_57 + 1);
    }
    
    res_XorLogicOP_57 = (res_XorLogicOP_57 && (xorIndex_res_XorLogicOP_57 == 1));
    res_ImpliesLogicOp_44 = (res_ImpliesLogicOp_44 && res_XorLogicOP_57);
    }
    res_OrLogicOP_43 = (res_OrLogicOP_43 || res_ImpliesLogicOp_44);
    bool res_OrLogicOP_111 = false;
    bool res_OrLogicOP_112 = false;
    bool res_NotLogicOP_113 = true;
    res_NotLogicOP_113 = (res_NotLogicOP_113 && ! (L_P1__GetParamSubcl68(my_id) == false));
    res_OrLogicOP_112 = (res_OrLogicOP_112 || res_NotLogicOP_113);
    res_OrLogicOP_112 = (res_OrLogicOP_112 || Timer_Scaduto(L_P1__GetSubcl112(my_id)));
    
    res_OrLogicOP_111 = (res_OrLogicOP_111 || res_OrLogicOP_112);
    bool res_AndLogicOP_114 = true;
    res_AndLogicOP_114 = (res_AndLogicOP_114 && (L_P1__GetSubcl99(my_id) == false));
    bool res_NotLogicOP_115 = true;
    res_NotLogicOP_115 = (res_NotLogicOP_115 && ! (Counter_GetValore(L_P1__GetSubcl115(my_id)) == 11u));
    res_AndLogicOP_114 = (res_AndLogicOP_114 && res_NotLogicOP_115);
    
    res_OrLogicOP_111 = (res_OrLogicOP_111 || res_AndLogicOP_114);
    
    res_OrLogicOP_43 = (res_OrLogicOP_43 || res_OrLogicOP_111);
    
    res_ImpliesLogicOp_38 = (res_ImpliesLogicOp_38 && res_OrLogicOP_43);
    }
    res_AndLogicOP_37 = (res_AndLogicOP_37 && res_ImpliesLogicOp_38);
    bool res_OrLogicOP_116 = false;
    bool res_NotLogicOP_117 = true;
    bool res_NotLogicOP_118 = true;
    res_NotLogicOP_118 = (res_NotLogicOP_118 && ! (L_P1__GetParamSubcl67(my_id) == 9u));
    res_NotLogicOP_117 = (res_NotLogicOP_117 && ! res_NotLogicOP_118);
    res_OrLogicOP_116 = (res_OrLogicOP_116 || res_NotLogicOP_117);
    bool res_AndLogicOP_119 = true;
    bool res_NotLogicOP_120 = true;
    bool res_NotLogicOP_121 = true;
    res_NotLogicOP_121 = (res_NotLogicOP_121 && ! (L_P1__GetInSubcl59(my_id) == rossogiallo4));
    res_NotLogicOP_120 = (res_NotLogicOP_120 && ! res_NotLogicOP_121);
    res_AndLogicOP_119 = (res_AndLogicOP_119 && res_NotLogicOP_120);
    bool res_NotLogicOP_122 = true;
    res_NotLogicOP_122 = (res_NotLogicOP_122 && ! (L_P1__GetParamSubcl67(my_id) < 4u));
    res_AndLogicOP_119 = (res_AndLogicOP_119 && res_NotLogicOP_122);
    
    res_OrLogicOP_116 = (res_OrLogicOP_116 || res_AndLogicOP_119);
    
    res_AndLogicOP_37 = (res_AndLogicOP_37 && res_OrLogicOP_116);
    
    res_ImpliesLogicOp_22 = (res_ImpliesLogicOp_22 && res_AndLogicOP_37);
    }
    res_AndLogicOP_21 = (res_AndLogicOP_21 && res_ImpliesLogicOp_22);
    bool res_AndLogicOP_123 = true;
    res_AndLogicOP_123 = (res_AndLogicOP_123 && (L_P1__GetSubcl100(my_id) == rossogiallo4));
    bool res_NotLogicOP_124 = true;
    bool res_NotLogicOP_125 = true;
    res_NotLogicOP_125 = (res_NotLogicOP_125 && ! (Counter_GetValore(L_P1__GetSubcl115(my_id)) == 12u));
    res_NotLogicOP_124 = (res_NotLogicOP_124 && ! res_NotLogicOP_125);
    res_AndLogicOP_123 = (res_AndLogicOP_123 && res_NotLogicOP_124);
    
    res_AndLogicOP_21 = (res_AndLogicOP_21 && res_AndLogicOP_123);
    
    res_ImpliesLogicOp_20 = (res_ImpliesLogicOp_20 && res_AndLogicOP_21);
    }
    res_AndLogicOP_19 = (res_AndLogicOP_19 && res_ImpliesLogicOp_20);
    bool res_OrLogicOP_126 = false;
    bool res_AndLogicOP_127 = true;
    bool res_AndLogicOP_128 = true;
    bool res_NotLogicOP_129 = true;
    bool res_NotLogicOP_130 = true;
    res_NotLogicOP_130 = (res_NotLogicOP_130 && ! (L_P1__GetSubcl99(my_id) == true));
    res_NotLogicOP_129 = (res_NotLogicOP_129 && ! res_NotLogicOP_130);
    res_AndLogicOP_128 = (res_AndLogicOP_128 && res_NotLogicOP_129);
    bool res_NotLogicOP_131 = true;
    res_NotLogicOP_131 = (res_NotLogicOP_131 && ! (L_P1__GetInSubcl62(my_id) == false));
    res_AndLogicOP_128 = (res_AndLogicOP_128 && res_NotLogicOP_131);
    
    res_AndLogicOP_127 = (res_AndLogicOP_127 && res_AndLogicOP_128);
    bool res_NotLogicOP_132 = true;
    res_NotLogicOP_132 = (res_NotLogicOP_132 && ! (L_P1__GetSubcl99(my_id) == true));
    res_AndLogicOP_127 = (res_AndLogicOP_127 && res_NotLogicOP_132);
    
    res_OrLogicOP_126 = (res_OrLogicOP_126 || res_AndLogicOP_127);
    res_OrLogicOP_126 = (res_OrLogicOP_126 || Timer_Scaduto(L_P1__GetSubcl113(my_id)));
    
    res_AndLogicOP_19 = (res_AndLogicOP_19 && res_OrLogicOP_126);
    
    res_ImpliesLogicOp_10 = (res_ImpliesLogicOp_10 && res_AndLogicOP_19);
    }
    if(res_ImpliesLogicOp_10){
    xorIndex_res_XorLogicOP_9 = (xorIndex_res_XorLogicOP_9 + 1);
    }
    bool res_NotLogicOP_133 = true;
    res_NotLogicOP_133 = (res_NotLogicOP_133 && ! (L_P1__GetSubcl99(my_id) == true));
    if(res_NotLogicOP_133){
    xorIndex_res_XorLogicOP_9 = (xorIndex_res_XorLogicOP_9 + 1);
    }
    
    res_XorLogicOP_9 = (res_XorLogicOP_9 && (xorIndex_res_XorLogicOP_9 == 1));
    res_ImpliesLogicOp_6 = (res_ImpliesLogicOp_6 && res_XorLogicOP_9);
    }
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_ImpliesLogicOp_6);
    bool res_OrLogicOP_134 = false;
    bool res_OrLogicOP_135 = false;
    bool res_AndLogicOP_136 = true;
    bool res_NotLogicOP_137 = true;
    res_NotLogicOP_137 = (res_NotLogicOP_137 && ! Timer_Scaduto(L_P1__GetSubcl113(my_id)));
    res_AndLogicOP_136 = (res_AndLogicOP_136 && res_NotLogicOP_137);
    bool res_NotLogicOP_138 = true;
    res_NotLogicOP_138 = (res_NotLogicOP_138 && ! (Counter_GetValore(L_P1__GetSubcl115(my_id)) == 11u));
    res_AndLogicOP_136 = (res_AndLogicOP_136 && res_NotLogicOP_138);
    
    res_OrLogicOP_135 = (res_OrLogicOP_135 || res_AndLogicOP_136);
    bool res_AndLogicOP_139 = true;
    res_AndLogicOP_139 = (res_AndLogicOP_139 && (Counter_GetValore(L_P1__GetSubcl116(my_id)) < 155u));
    bool res_NotLogicOP_140 = true;
    res_NotLogicOP_140 = (res_NotLogicOP_140 && ! Timer_Scaduto(L_P1__GetSubcl113(my_id)));
    res_AndLogicOP_139 = (res_AndLogicOP_139 && res_NotLogicOP_140);
    
    res_OrLogicOP_135 = (res_OrLogicOP_135 || res_AndLogicOP_139);
    
    res_OrLogicOP_134 = (res_OrLogicOP_134 || res_OrLogicOP_135);
    bool res_AndLogicOP_141 = true;
    bool res_NotLogicOP_142 = true;
    res_NotLogicOP_142 = (res_NotLogicOP_142 && ! (argom50 == true));
    res_AndLogicOP_141 = (res_AndLogicOP_141 && res_NotLogicOP_142);
    bool res_NotLogicOP_143 = true;
    bool res_NotLogicOP_144 = true;
    res_NotLogicOP_144 = (res_NotLogicOP_144 && ! (L_P1__GetInSubcl60(my_id) == rossogiallo4));
    res_NotLogicOP_143 = (res_NotLogicOP_143 && ! res_NotLogicOP_144);
    res_AndLogicOP_141 = (res_AndLogicOP_141 && res_NotLogicOP_143);
    
    res_OrLogicOP_134 = (res_OrLogicOP_134 || res_AndLogicOP_141);
    
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_OrLogicOP_134);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_AndLogicOP_5);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *50,51,52,*  *,*  la variabile SubClass_C3_variabile_V6 sia  uguale a  True 
    //   *104,* e  che   l'argomento argomento_ave1 sia  uguale a RossoVerde *,* 
    //   *104,* e  che  *,*  il contatore SubClass_C3_contatore_Co2 sia  uguale a  *53,* 1504
    bool res_AndLogicOP_145 = true;
    bool res_AndLogicOP_146 = true;
    res_AndLogicOP_146 = (res_AndLogicOP_146 && (L_P1__GetSubcl99(my_id) == true));
    res_AndLogicOP_146 = (res_AndLogicOP_146 && (argom49 == rossoverde));
    
    res_AndLogicOP_145 = (res_AndLogicOP_145 && res_AndLogicOP_146);
    res_AndLogicOP_145 = (res_AndLogicOP_145 && (Counter_GetValore(L_P1__GetSubcl115(my_id)) == 1504u));
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_AndLogicOP_145);
    
    
    
    return res_AndLogicOP_0;
}


// Macro valorizzate

/*
    CNL corrispondente:
    
    { commento: {[} commento: {35,}  se il controllo SubClass_C3_controllo_C7 non è  diverso da RossoGialloVerde,  commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L5 è  diverso da  commento: {56,}  state1 , commento: {88,} quando  commento: {111,}   lo stato del campo  MainClass_C1     è  uguale a  commento: {53,}  state1  commento: {38,} e  se il contatore SubClass_C3_contatore_Co8 è  maggiore di  commento: {54,} 12,  commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  commento: {105,} è  diverso da  commento: {56,}  state1 , commento: {88,} quando  commento: {45,}    MainClass_C1_contatore_Co2 del campo  MainClass_C1     è  diverso da  commento: {56,} 113 commento: {34,} o  se il parametro SubClass_C3_parametro_P5 non è  uguale a RossoVerde commento: {111,} e  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L1 è  uguale a  commento: {53,}  state1  commento: {110,} o  se il ripristino del timer  SubClass_C3_restoreTI_TI4 non è scaduto , assegna alla macro il valore RossoGialloVerde
    
     commento: {46,} assegna alla macro il valore RossoGialloVerde commento: {],}
    }
*/
C3_Enumerat2 L_P1__Macro17(instance_id_t const my_id , C3_Enumerat3 argom36, C3_Enumerat3 argom37, C3_Enumerat1 argom38, C3_Enumerat2 argom39)
{
C3_Enumerat2 res_macro_val;
    
    //  *[* *35,*  se il controllo SubClass_C3_controllo_C7 non è  diverso da RossoGialloVerde,  *111,*  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L5 è  diverso da  *56,*  state1 , *88,* quando  *111,*   lo stato del campo  MainClass_C1     è  uguale a  *53,*  state1  *38,* e  se il contatore SubClass_C3_contatore_Co8 è  maggiore di  *54,* 12,  *111,*  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  *105,* è  diverso da  *56,*  state1 , *88,* quando  *45,*    MainClass_C1_contatore_Co2 del campo  MainClass_C1     è  diverso da  *56,* 113 *34,* o  se il parametro SubClass_C3_parametro_P5 non è  uguale a RossoVerde *111,* e  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L1 è  uguale a  *53,*  state1  *110,* o  se il ripristino del timer  SubClass_C3_restoreTI_TI4 non è scaduto
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_AndLogicOP_2 = true;
    bool res_AndLogicOP_3 = true;
    bool res_NotLogicOP_4 = true;
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetInSubcl60(my_id) == rossogiallo4));
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! res_NotLogicOP_5);
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_4);
    bool res_ForAllPredicate_6 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl64Length(my_id); ++i)
    {
    L_P1__Recor2 it = L_P1__GetRecSubcl64(my_id,i);
    bool res_ImpliesLogicOp_7 = true;
    if((L_P1_C1_GetState(it.mainc38) == C1_St_state)){
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1_C1_GetState(it.mainc38) == C1_St_state));
    res_ImpliesLogicOp_7 = (res_ImpliesLogicOp_7 && res_NotLogicOP_8);
    }
    res_ForAllPredicate_6 = res_ImpliesLogicOp_7;
    if(!res_ForAllPredicate_6) {break;}
    }
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_ForAllPredicate_6);
    
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_AndLogicOP_3);
    bool res_AndLogicOP_9 = true;
    res_AndLogicOP_9 = (res_AndLogicOP_9 && (Counter_GetValore(L_P1__GetSubcl116(my_id)) > 12u));
    bool res_ForAllPredicateNotEmpty_10 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl65Length(my_id); ++i)
    {
    L_P1__Recor2 it = L_P1__GetRecSubcl65(my_id,i);
    bool res_ImpliesLogicOp_11 = true;
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (Counter_GetValore(L_P1__GetMainc34(it.mainc38)) == 113u));
    if(res_NotLogicOP_12){
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (L_P1_C1_GetState(it.mainc38) == C1_St_state));
    res_ImpliesLogicOp_11 = (res_ImpliesLogicOp_11 && res_NotLogicOP_13);
    res_ForAllPredicateNotEmpty_10 = res_ImpliesLogicOp_11;
    if(!res_ForAllPredicateNotEmpty_10) {break;}
    }
    }
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_ForAllPredicateNotEmpty_10);
    
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_AndLogicOP_9);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_2);
    bool res_AndLogicOP_14 = true;
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (L_P1__GetParamSubcl66(my_id) == rossoverde));
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_NotLogicOP_15);
    bool res_ForAllPredicate_16 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl63Length(my_id); ++i)
    {
    L_P1__Recor2 it = L_P1__GetRecSubcl63(my_id,i);
    bool res_ImpliesLogicOp_17 = true;
    res_ImpliesLogicOp_17 = (res_ImpliesLogicOp_17 && (L_P1_C1_GetState(it.mainc38) == C1_St_state));
    res_ForAllPredicate_16 = res_ImpliesLogicOp_17;
    if(!res_ForAllPredicate_16) {break;}
    }
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_ForAllPredicate_16);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_14);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_NotLogicOP_18 = true;
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! Timer_Scaduto(L_P1__GetSubcl109(my_id)));
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_18);
    
    if(res_OrLogicOP_0){
    
    res_macro_val = rossogiallo4;
    }
    else{
    res_macro_val = rossogiallo4;
    }
    return res_macro_val;
}

/*
    CNL corrispondente:
    
    { commento: {[}
     commento: {46,} assegna alla macro il valore avanzamentox commento: {],}
    }
*/
C3_Enumerat4 L_P1__Macro18(instance_id_t const my_id , bool argom40, C3_Enumerat4 argom41)
{
return avanzamento;
}

/*
    CNL corrispondente:
    
    { commento: {[}
     commento: {46,} assegna alla macro il valore  False  commento: {],}
    }
*/
bool L_P1__Macro19(instance_id_t const my_id , C3_Enumerat3 argom42, C3_Enumerat1 argom43, C3_Enumerat1 argom44, C3_Enumerat4 argom45)
{
return false;
}



