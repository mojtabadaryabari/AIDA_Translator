// Codice del modello 'TestCase14', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#include "Logica/ClasseMainClass_C1.h"
#include "Logica/ClasseSubClass_C2.h"
#include "Logica/ClasseMainClass_C1_priv.h"
#include "config.h"
#include "scheduler.h"


// ********** Gestione comandi automatici **********

static size_t L_P1_C1_NumAutoCmds(instance_id_t const my_id)
{
    size_t n = 0u;
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
    if (L_P1__GetInEvent1(my_id)) {
	    L_P1__SetOutEvent4(my_id, LDS_MANCMD_UNEXPECTED);
    } else {
        L_P1__SetOutEvent4(my_id, LDS_MANCMD_NOOP);
    }
}

static void L_P1_C1_SetExpectedCmdsResponse(instance_id_t const my_id, C1_Stateenu state)
{        
    switch (state) {
    case C1_St_state1:
        // manual commands of L_P1_C1 that can be received in C1_St_state1
        if (L_P1__GetInEvent1(my_id)) {
            L_P1__SetOutEvent4(my_id, LDS_MANCMD_BLOCKED);
        }
	break;

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
    
     commento: {69,} commento: {35,}  se il controllo MainClass_C1_controllo_C5 è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
     commento: {37,}  se la variabile MainClass_C1_variabile_V8 è  minore di  commento: {55,} 1 commento: {34,} e  se il parametro MainClass_C1_parametro_P3 è  diverso da Verde commento: {37,} o  se la variabile MainClass_C1_variabile_V5 non è  diverso da c270x commento: {35,} e  se il controllo MainClass_C1_controllo_C2 è  diverso da Verde o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   commento: {51,}  commento: {,}  il contatore MainClass_C1_contatore_Co4 non sia  diverso da  commento: {56,} 15
    
    
     } Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
    
    
    }
*/
static inline bool L_P1__Guard1(instance_id_t const my_id)
{
    bool res_AndLogicOP_0 = true;
    
    //  *69,* *35,*  se il controllo MainClass_C1_controllo_C5 è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
    //   *37,*  se la variabile MainClass_C1_variabile_V8 è  minore di  *55,* 1 *34,* e  se il parametro MainClass_C1_parametro_P3 è  diverso da Verde *37,* o  se la variabile MainClass_C1_variabile_V5 non è  diverso da c270x *35,* e  se il controllo MainClass_C1_controllo_C2 è  diverso da Verde o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   *51,*  *,*  il contatore MainClass_C1_contatore_Co4 non sia  diverso da  *56,* 15
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    res_OrLogicOP_2 = (res_OrLogicOP_2 || (L_P1__GetInMainc8(my_id) == true));
    bool res_AndLogicOP_3 = true;
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (L_P1__GetInConsd(my_id) == false));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_3);
    
    if(res_OrLogicOP_2){
    bool res_ImpliesLogicOp_4 = true;
    bool res_OrLogicOP_5 = false;
    bool res_OrLogicOP_6 = false;
    bool res_AndLogicOP_7 = true;
    res_AndLogicOP_7 = (res_AndLogicOP_7 && (L_P1__GetMainc35(my_id) < 1u));
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetParamMainc10(my_id) == verde));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_8);
    
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_AndLogicOP_7);
    bool res_AndLogicOP_9 = true;
    bool res_NotLogicOP_10 = true;
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (L_P1__GetMainc34(my_id) == c270x));
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! res_NotLogicOP_11);
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_NotLogicOP_10);
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (L_P1__GetInMainc7(my_id) == verde));
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_NotLogicOP_12);
    
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_AndLogicOP_9);
    
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_OrLogicOP_6);
    res_OrLogicOP_5 = (res_OrLogicOP_5 || (L_P1__GetInConsd(my_id) == false));
    
    if(res_OrLogicOP_5){
    bool res_NotLogicOP_13 = true;
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (Counter_GetValore(L_P1__GetMainc48(my_id)) == 15u));
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! res_NotLogicOP_14);
    res_ImpliesLogicOp_4 = (res_ImpliesLogicOp_4 && res_NotLogicOP_13);
    }
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_ImpliesLogicOp_4);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *48,*   il controllo ConsDef  sia  uguale a FALSE
    res_AndLogicOP_0 = (res_AndLogicOP_0 && (L_P1__GetInConsd(my_id) == false));
    
    
    
    return res_AndLogicOP_0;
}


/*
    CNL corrispondente:
     {  Nessuna  }
*/
static inline bool L_P1__Guard2(instance_id_t const my_id)
{
    return true;
}


/*
    CNL corrispondente:
     {  Nessuna  }
*/
static inline bool L_P1__Guard3(instance_id_t const my_id)
{
    return true;
}


/*
    CNL corrispondente:
     {  Nessuna  commento: {80,} }
*/
static inline bool L_P1__Guard4(instance_id_t const my_id)
{
    return true;
}


/*
    CNL corrispondente:
     {  Nessuna  commento: {80,} }
*/
static inline bool L_P1__Guard5(instance_id_t const my_id)
{
    return true;
}


/*
    CNL corrispondente:
     {  Nessuna  }
*/
static inline bool L_P1__Guard6(instance_id_t const my_id)
{
    return true;
}


/*
    CNL corrispondente:
    
    {
    
     Nessuna  commento: {80,}
    }
*/
static inline bool L_P1__Guard7(instance_id_t const my_id)
{
    return true;
}


/*
    CNL corrispondente:
     {  Nessuna  }
*/
static inline bool L_P1__Guard8(instance_id_t const my_id)
{
    return true;
}


/*
    CNL corrispondente:
     {  Nessuna  commento: {80,} }
*/
static inline bool L_P1__Guard9(instance_id_t const my_id)
{
    return true;
}


/*
    CNL corrispondente:
     {  commento: {86,}  Almeno una delle seguenti {
     commento: {82,}  Ricezione del comando manuale   MainClass_C1_command_comm5   commento: {75,}
     commento: {83,}  Tutte le seguenti {
     Ricezione del  comando manuale   MainClass_C1_command_comm5   commento: {75,}
     commento: {34,}  se il parametro MainClass_C1_parametro_P8 non è  uguale a RossoGialloVerde, Verifica che   commento: {50,}  commento: {,}  la variabile MainClass_C1_variabile_V5 sia  diverso da c270x
    
    
    }
    } }
*/
static inline bool L_P1__Guard10(instance_id_t const my_id)
{
    bool res_AndLogicOP_0 = true;
    
    //  *86,*  Almeno una delle seguenti {
    //   *82,*  Ricezione del comando manuale   MainClass_C1_command_comm5   *75,*
    //   *83,*  Tutte le seguenti {
    //   Ricezione del  comando manuale   MainClass_C1_command_comm5   *75,*
    //   *34,*  se il parametro MainClass_C1_parametro_P8 non è  uguale a RossoGialloVerde, Verifica che   *50,*  *,*  la variabile MainClass_C1_variabile_V5 sia  diverso da c270x
    //  }
    //  }
    bool res_OrLogicOP_1 = false;
    res_OrLogicOP_1 = (res_OrLogicOP_1 || L_P1__GetInEvent1(my_id));
    bool res_AndLogicOP_2 = true;
    res_AndLogicOP_2 = (res_AndLogicOP_2 && L_P1__GetInEvent1(my_id));
    bool res_ImpliesLogicOp_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetParamMainc11(my_id) == rossogiallo));
    if(res_NotLogicOP_4){
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetMainc34(my_id) == c270x));
    res_ImpliesLogicOp_3 = (res_ImpliesLogicOp_3 && res_NotLogicOP_5);
    }
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_ImpliesLogicOp_3);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_2);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_1);
    
    if(res_OrLogicOP_1){
    L_P1__SetOutEvent4(my_id,LDS_MANCMD_PROCESSED);
    }
    else{
    
    }
    
    
    return res_AndLogicOP_0;
}


/*
    CNL corrispondente:
     {  Nessuna  }
*/
static inline bool L_P1__Guard11(instance_id_t const my_id)
{
    return true;
}


/*
    CNL corrispondente:
     {  commento: {86,}  Almeno una delle seguenti {
     commento: {82,}  Ricezione del comando manuale   MainClass_C1_command_comm5   commento: {75,}
    
    } }
*/
static inline bool L_P1__Guard12(instance_id_t const my_id)
{
    bool res_AndLogicOP_0 = true;
    
    //  comando manuale   MainClass_C1_command_comm5
    res_AndLogicOP_0 = (res_AndLogicOP_0 && L_P1__GetInEvent1(my_id));
    
    if(res_AndLogicOP_0){
    L_P1__SetOutEvent4(my_id,LDS_MANCMD_PROCESSED);
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
    
     commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è scaduto, commento: {66,} Assegna al comando MainClass_C1_comando_C4 il valore  True 
    
       
    
    }
*/
static inline void L_P1__Effec1(instance_id_t const my_id)
{
    
    //  *110,*  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è scaduto, *66,* Assegna al comando MainClass_C1_comando_C4 il valore  True
    if(Timer_Scaduto(L_P1__GetMainc37(my_id))){
    
    L_P1__SetOutMainc3(my_id,true);
    }
}


/*
    CNL corrispondente:
     {  se il controllo ConsDef è uguale a FALSE  commento: {34,} o  se il parametro MainClass_C1_parametro_P3 è  diverso da Verde commento: {38,} o  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  commento: {56,} 150 commento: {36,} o  se il timer MainClass_C1_timer_T6 è disattivo o  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} o  se la variabile MainClass_C1_variabile_V8 è  diverso da  commento: {56,} 3, commento: {66,} Assegna al comando MainClass_C1_comando_C10 il valore RossoGialloxVerdex
    
     ,altrimenti  commento: {71,}Decrementa il contatore MainClass_C1_contatore_Co4
    
    
     commento: {38,}  se il contatore MainClass_C1_contatore_Co4 è  diverso da  commento: {56,} 153 commento: {36,} o  se il timer MainClass_C1_timer_T2 è disattivo commento: {38,} o  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  commento: {56,} 15 commento: {35,} o  se il controllo MainClass_C1_controllo_C10 non è  diverso da RossoGialloxVerdex, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V8 il valore 8
    
     ,altrimenti  commento: {70,}Incrementa il contatore MainClass_C1_contatore_Co4
    
    
     commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV2 è  uguale a RossoGialloVerde commento: {35,} e  se il controllo MainClass_C1_controllo_C2 è  uguale a Verde commento: {35,} e  se il controllo MainClass_C1_controllo_C10 è  uguale a RossoGialloxVerdex commento: {38,} e  se il contatore MainClass_C1_contatore_Co2 è  diverso da  commento: {56,} 122 commento: {37,} o  se la variabile MainClass_C1_variabile_V5 è  uguale a c270x o  se il controllo ConsDef  è  uguale a FALSE , commento: {69,}Disattiva il timer MainClass_C1_timer_T6
    
       
      se il controllo ConsDef è uguale a FALSE  commento: {35,} o  se il controllo MainClass_C1_controllo_C2 non è  diverso da Verde commento: {38,} o  se il contatore MainClass_C1_contatore_Co4 è  maggiore di  commento: {54,} 141, commento: {72,}Azzera il contatore MainClass_C1_contatore_Co2
    
       
     }
*/
static inline void L_P1__Effec2(instance_id_t const my_id)
{
    
    //  se il controllo ConsDef è uguale a FALSE  *34,* o  se il parametro MainClass_C1_parametro_P3 è  diverso da Verde *38,* o  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  *56,* 150 *36,* o  se il timer MainClass_C1_timer_T6 è disattivo o  se il controllo ConsDef  è  uguale a FALSE  *37,* o  se la variabile MainClass_C1_variabile_V8 è  diverso da  *56,* 3, *66,* Assegna al comando MainClass_C1_comando_C10 il valore RossoGialloxVerdex
    //   ,altrimenti  *71,*Decrementa il contatore MainClass_C1_contatore_Co4
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_OrLogicOP_4 = false;
    res_OrLogicOP_4 = (res_OrLogicOP_4 || (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetParamMainc10(my_id) == verde));
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_NotLogicOP_5);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_OrLogicOP_4);
    bool res_NotLogicOP_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (Counter_GetValore(L_P1__GetMainc48(my_id)) == 150u));
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! res_NotLogicOP_7);
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_NotLogicOP_6);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    res_OrLogicOP_2 = (res_OrLogicOP_2 || Timer_Disattivo(L_P1__GetMainc45(my_id)));
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_OrLogicOP_2);
    res_OrLogicOP_1 = (res_OrLogicOP_1 || (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetMainc35(my_id) == 3u));
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_8);
    
    if(res_OrLogicOP_0){
    
    L_P1__SetOutMainc1(my_id,rossogiallo1);
    }else{
    
    Counter_Decr(L_P1__GetMainc48(my_id));
    }
    
    //  *38,*  se il contatore MainClass_C1_contatore_Co4 è  diverso da  *56,* 153 *36,* o  se il timer MainClass_C1_timer_T2 è disattivo *38,* o  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  *56,* 15 *35,* o  se il controllo MainClass_C1_controllo_C10 non è  diverso da RossoGialloxVerdex, *67,* Assegna alla variabile MainClass_C1_variabile_V8 il valore 8
    //   ,altrimenti  *70,*Incrementa il contatore MainClass_C1_contatore_Co4
    bool res_OrLogicOP_9 = false;
    bool res_OrLogicOP_10 = false;
    bool res_OrLogicOP_11 = false;
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (Counter_GetValore(L_P1__GetMainc48(my_id)) == 153u));
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_NotLogicOP_12);
    res_OrLogicOP_11 = (res_OrLogicOP_11 || Timer_Disattivo(L_P1__GetMainc44(my_id)));
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_OrLogicOP_11);
    bool res_NotLogicOP_13 = true;
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (Counter_GetValore(L_P1__GetMainc47(my_id)) == 15u));
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! res_NotLogicOP_14);
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_NotLogicOP_13);
    
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_OrLogicOP_10);
    bool res_NotLogicOP_15 = true;
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (L_P1__GetInMainc6(my_id) == rossogiallo1));
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! res_NotLogicOP_16);
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_NotLogicOP_15);
    
    if(res_OrLogicOP_9){
    
    L_P1__SetMainc35(my_id,8u);
    }else{
    
    Counter_Incr(L_P1__GetMainc48(my_id));
    }
    
    //  *109,*  se il ripristino della variabile  MainClass_C1_restoreva_RV2 è  uguale a RossoGialloVerde *35,* e  se il controllo MainClass_C1_controllo_C2 è  uguale a Verde *35,* e  se il controllo MainClass_C1_controllo_C10 è  uguale a RossoGialloxVerdex *38,* e  se il contatore MainClass_C1_contatore_Co2 è  diverso da  *56,* 122 *37,* o  se la variabile MainClass_C1_variabile_V5 è  uguale a c270x o  se il controllo ConsDef  è  uguale a FALSE , *69,*Disattiva il timer MainClass_C1_timer_T6
    bool res_OrLogicOP_17 = false;
    bool res_OrLogicOP_18 = false;
    bool res_AndLogicOP_19 = true;
    bool res_AndLogicOP_20 = true;
    bool res_AndLogicOP_21 = true;
    res_AndLogicOP_21 = (res_AndLogicOP_21 && (L_P1__GetMainc33(my_id) == rossogiallo));
    res_AndLogicOP_21 = (res_AndLogicOP_21 && (L_P1__GetInMainc7(my_id) == verde));
    
    res_AndLogicOP_20 = (res_AndLogicOP_20 && res_AndLogicOP_21);
    res_AndLogicOP_20 = (res_AndLogicOP_20 && (L_P1__GetInMainc6(my_id) == rossogiallo1));
    
    res_AndLogicOP_19 = (res_AndLogicOP_19 && res_AndLogicOP_20);
    bool res_NotLogicOP_22 = true;
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! (Counter_GetValore(L_P1__GetMainc47(my_id)) == 122u));
    res_AndLogicOP_19 = (res_AndLogicOP_19 && res_NotLogicOP_22);
    
    res_OrLogicOP_18 = (res_OrLogicOP_18 || res_AndLogicOP_19);
    res_OrLogicOP_18 = (res_OrLogicOP_18 || (L_P1__GetMainc34(my_id) == c270x));
    
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_OrLogicOP_18);
    res_OrLogicOP_17 = (res_OrLogicOP_17 || (L_P1__GetInConsd(my_id) == false));
    
    if(res_OrLogicOP_17){
    
    Timer_Disattiva(L_P1__GetMainc45(my_id));
    }
    
    //  se il controllo ConsDef è uguale a FALSE  *35,* o  se il controllo MainClass_C1_controllo_C2 non è  diverso da Verde *38,* o  se il contatore MainClass_C1_contatore_Co4 è  maggiore di  *54,* 141, *72,*Azzera il contatore MainClass_C1_contatore_Co2
    bool res_OrLogicOP_23 = false;
    bool res_OrLogicOP_24 = false;
    res_OrLogicOP_24 = (res_OrLogicOP_24 || (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_25 = true;
    bool res_NotLogicOP_26 = true;
    res_NotLogicOP_26 = (res_NotLogicOP_26 && ! (L_P1__GetInMainc7(my_id) == verde));
    res_NotLogicOP_25 = (res_NotLogicOP_25 && ! res_NotLogicOP_26);
    res_OrLogicOP_24 = (res_OrLogicOP_24 || res_NotLogicOP_25);
    
    res_OrLogicOP_23 = (res_OrLogicOP_23 || res_OrLogicOP_24);
    res_OrLogicOP_23 = (res_OrLogicOP_23 || (Counter_GetValore(L_P1__GetMainc48(my_id)) > 141u));
    
    if(res_OrLogicOP_23){
    
    Counter_Res(L_P1__GetMainc47(my_id));
    }
}


/*
    CNL corrispondente:
     { commento: {34,}  se lo stato  non è  diverso da  commento: {56,}  state1  commento: {106,} commento: {34,} e  se il parametro MainClass_C1_parametro_P3 non è  uguale a Verde e  se il controllo ConsDef  è  uguale a FALSE ,  Applica gli effetti
           della macro MainClass_C1_macroef_M6   commento: {73,}
    
       
     commento: {38,}  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  commento: {53,} 1232 commento: {36,} o  se il timer MainClass_C1_timer_T8 non è attivo commento: {36,} e  se il timer MainClass_C1_timer_T2 non è scaduto, commento: {71,}Decrementa il contatore MainClass_C1_contatore_Co2
    
     ,altrimenti  commento: {72,}Azzera il contatore MainClass_C1_contatore_Co4
    
    
     commento: {35,}  se il controllo MainClass_C1_controllo_C10 è  diverso da RossoGialloxVerdex commento: {34,} o  se il parametro MainClass_C1_parametro_P8 non è  uguale a RossoGialloVerde commento: {37,} o  se la variabile MainClass_C1_variabile_V8 non è  maggiore di  commento: {54,} 4 commento: {35,} o  se il controllo MainClass_C1_controllo_C2 è  diverso da Verde o  se il controllo ConsDef  è  uguale a FALSE , commento: {69,}Disattiva il timer MainClass_C1_timer_T6
    
     ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V5 il valore c270x
    
    
      se il controllo ConsDef  è  uguale a FALSE  commento: {38,} o  se il contatore MainClass_C1_contatore_Co2 è  minore di  commento: {55,} 12145 commento: {35,} e  se il controllo MainClass_C1_controllo_C10 è  uguale a RossoGialloxVerdex, commento: {69,}Disattiva il timer MainClass_C1_timer_T2
    
       
     commento: {35,}  se il controllo MainClass_C1_controllo_C9 è  uguale a  False  commento: {38,} e  se il contatore MainClass_C1_contatore_Co2 è  maggiore di  commento: {54,} 1203, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V5 il valore c270x
    
     ,altrimenti  commento: {66,} Assegna al comando MainClass_C1_comando_C4 il valore  True 
    
    
     }
*/
static inline void L_P1__Effec3(instance_id_t const my_id)
{
    
    //  *34,*  se lo stato  non è  diverso da  *56,*  state1  *106,* *34,* e  se il parametro MainClass_C1_parametro_P3 non è  uguale a Verde e  se il controllo ConsDef  è  uguale a FALSE ,  Applica gli effetti
    //         della macro MainClass_C1_macroef_M6
    bool res_AndLogicOP_0 = true;
    bool res_AndLogicOP_1 = true;
    bool res_NotLogicOP_2 = true;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1_C1_GetState(my_id) == C1_St_state));
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! res_NotLogicOP_3);
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_2);
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetParamMainc10(my_id) == verde));
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_4);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_AndLogicOP_1);
    res_AndLogicOP_0 = (res_AndLogicOP_0 && (L_P1__GetInConsd(my_id) == false));
    
    if(res_AndLogicOP_0){
    
    L_P1__Macro1(my_id);
    }
    
    //  *73,*
    //     
    //   *38,*  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  *53,* 1232 *36,* o  se il timer MainClass_C1_timer_T8 non è attivo *36,* e  se il timer MainClass_C1_timer_T2 non è scaduto, *71,*Decrementa il contatore MainClass_C1_contatore_Co2
    //   ,altrimenti  *72,*Azzera il contatore MainClass_C1_contatore_Co4
    bool res_OrLogicOP_5 = false;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (Counter_GetValore(L_P1__GetMainc47(my_id)) == 1232u));
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_NotLogicOP_6);
    bool res_AndLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! Timer_Attivo(L_P1__GetMainc46(my_id)));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_8);
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! Timer_Scaduto(L_P1__GetMainc44(my_id)));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_9);
    
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_AndLogicOP_7);
    
    if(res_OrLogicOP_5){
    
    Counter_Decr(L_P1__GetMainc47(my_id));
    }else{
    
    Counter_Res(L_P1__GetMainc48(my_id));
    }
    
    //  *35,*  se il controllo MainClass_C1_controllo_C10 è  diverso da RossoGialloxVerdex *34,* o  se il parametro MainClass_C1_parametro_P8 non è  uguale a RossoGialloVerde *37,* o  se la variabile MainClass_C1_variabile_V8 non è  maggiore di  *54,* 4 *35,* o  se il controllo MainClass_C1_controllo_C2 è  diverso da Verde o  se il controllo ConsDef  è  uguale a FALSE , *69,*Disattiva il timer MainClass_C1_timer_T6
    //   ,altrimenti  *67,* Assegna alla variabile MainClass_C1_variabile_V5 il valore c270x
    bool res_OrLogicOP_10 = false;
    bool res_OrLogicOP_11 = false;
    bool res_OrLogicOP_12 = false;
    bool res_OrLogicOP_13 = false;
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1__GetInMainc6(my_id) == rossogiallo1));
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_NotLogicOP_14);
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (L_P1__GetParamMainc11(my_id) == rossogiallo));
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_NotLogicOP_15);
    
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_OrLogicOP_13);
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (L_P1__GetMainc35(my_id) > 4u));
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_NotLogicOP_16);
    
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_OrLogicOP_12);
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! (L_P1__GetInMainc7(my_id) == verde));
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_NotLogicOP_17);
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_OrLogicOP_11);
    res_OrLogicOP_10 = (res_OrLogicOP_10 || (L_P1__GetInConsd(my_id) == false));
    
    if(res_OrLogicOP_10){
    
    Timer_Disattiva(L_P1__GetMainc45(my_id));
    }else{
    
    L_P1__SetMainc34(my_id,c270x);
    }
    
    //  se il controllo ConsDef  è  uguale a FALSE  *38,* o  se il contatore MainClass_C1_contatore_Co2 è  minore di  *55,* 12145 *35,* e  se il controllo MainClass_C1_controllo_C10 è  uguale a RossoGialloxVerdex, *69,*Disattiva il timer MainClass_C1_timer_T2
    bool res_OrLogicOP_18 = false;
    res_OrLogicOP_18 = (res_OrLogicOP_18 || (L_P1__GetInConsd(my_id) == false));
    bool res_AndLogicOP_19 = true;
    res_AndLogicOP_19 = (res_AndLogicOP_19 && (Counter_GetValore(L_P1__GetMainc47(my_id)) < 12145u));
    res_AndLogicOP_19 = (res_AndLogicOP_19 && (L_P1__GetInMainc6(my_id) == rossogiallo1));
    
    res_OrLogicOP_18 = (res_OrLogicOP_18 || res_AndLogicOP_19);
    
    if(res_OrLogicOP_18){
    
    Timer_Disattiva(L_P1__GetMainc44(my_id));
    }
    
    //  *35,*  se il controllo MainClass_C1_controllo_C9 è  uguale a  False  *38,* e  se il contatore MainClass_C1_contatore_Co2 è  maggiore di  *54,* 1203, *67,* Assegna alla variabile MainClass_C1_variabile_V5 il valore c270x
    //   ,altrimenti  *66,* Assegna al comando MainClass_C1_comando_C4 il valore  True
    bool res_AndLogicOP_20 = true;
    res_AndLogicOP_20 = (res_AndLogicOP_20 && (L_P1__GetInMainc9(my_id) == false));
    res_AndLogicOP_20 = (res_AndLogicOP_20 && (Counter_GetValore(L_P1__GetMainc47(my_id)) > 1203u));
    
    if(res_AndLogicOP_20){
    
    L_P1__SetMainc34(my_id,c270x);
    }else{
    
    L_P1__SetOutMainc3(my_id,true);
    }
}


/*
    CNL corrispondente:
     { commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è attivo commento: {38,} e  se il contatore MainClass_C1_contatore_Co2 è  diverso da  commento: {56,} 142145 commento: {34,} o  se il parametro MainClass_C1_parametro_P8 è  uguale a RossoGialloVerde commento: {34,} e  se il parametro MainClass_C1_parametro_P8 è  uguale a RossoGialloVerde commento: {35,} e  se il controllo MainClass_C1_controllo_C2 è  diverso da Verde,  Applica gli effetti
           della macro MainClass_C1_macroef_M8  commento: {73,}
    
       
     commento: {35,}  se il controllo MainClass_C1_controllo_C2 è  uguale a Verde, commento: {68,}Attiva il timer MainClass_C1_timer_T8
    
     ,altrimenti  commento: {68,}Attiva il timer MainClass_C1_timer_T8
    
    
      se la macro  MainClass_C1_macrova_M1 ( con argomento_a2   uguale a GialloaVerdea ,argomento_a10   uguale a GialloGiallo ,argomento_a5   uguale a Verde ,argomento_a6   uguale a Verde  e argomento_a1   uguale a RossoGiallox )   è  diverso da  True  commento: {40,}  commento: {36,} e  se il timer MainClass_C1_timer_T2 non è disattivo commento: {37,} e  se la variabile MainClass_C1_variabile_V5 non è  uguale a c270x commento: {36,} e  se il timer MainClass_C1_timer_T2 non è attivo commento: {34,} e  se il parametro MainClass_C1_parametro_P8 è  uguale a RossoGialloVerde commento: {35,} o  se il controllo MainClass_C1_controllo_C10 non è  uguale a RossoGialloxVerdex, commento: {66,} Assegna al comando MainClass_C1_comando_C4 il valore  True 
    
     ,altrimenti   Applica gli effetti
           della macro MainClass_C1_macroef_M10  commento: {73,}
    
    
     commento: {37,}  se la variabile MainClass_C1_variabile_V8 è  maggiore di  commento: {54,} 10 commento: {38,} o  se il contatore MainClass_C1_contatore_Co2 è  diverso da  commento: {56,} 1303 commento: {37,} o  se la variabile MainClass_C1_variabile_V8 è  uguale a  commento: {53,} 4,  Applica gli effetti
           della macro MainClass_C1_macroef_M8  commento: {73,}
    
     ,altrimenti   Applica gli effetti
           della macro MainClass_C1_macroef_M6   commento: {73,}
    
    
     commento: {34,}  se lo stato  non è  diverso da  commento: {56,}  state1  commento: {106,} commento: {36,} e  se il timer MainClass_C1_timer_T6 non è scaduto commento: {38,} e  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  commento: {56,} 11 commento: {38,} e  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  commento: {53,} 14214,  Applica gli effetti
           della macro MainClass_C1_macroef_M8  commento: {73,}
    
       
     }
*/
static inline void L_P1__Effec4(instance_id_t const my_id)
{
    
    //  *110,*  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è attivo *38,* e  se il contatore MainClass_C1_contatore_Co2 è  diverso da  *56,* 142145 *34,* o  se il parametro MainClass_C1_parametro_P8 è  uguale a RossoGialloVerde *34,* e  se il parametro MainClass_C1_parametro_P8 è  uguale a RossoGialloVerde *35,* e  se il controllo MainClass_C1_controllo_C2 è  diverso da Verde,  Applica gli effetti
    //         della macro MainClass_C1_macroef_M8
    bool res_OrLogicOP_0 = false;
    bool res_AndLogicOP_1 = true;
    res_AndLogicOP_1 = (res_AndLogicOP_1 && Timer_Attivo(L_P1__GetMainc37(my_id)));
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (Counter_GetValore(L_P1__GetMainc47(my_id)) == 142145u));
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_2);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_1);
    bool res_AndLogicOP_3 = true;
    bool res_AndLogicOP_4 = true;
    res_AndLogicOP_4 = (res_AndLogicOP_4 && (L_P1__GetParamMainc11(my_id) == rossogiallo));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && (L_P1__GetParamMainc11(my_id) == rossogiallo));
    
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_AndLogicOP_4);
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetInMainc7(my_id) == verde));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_5);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_3);
    
    if(res_OrLogicOP_0){
    
    L_P1__Macro2(my_id);
    }
    
    //  *73,*
    //     
    //   *35,*  se il controllo MainClass_C1_controllo_C2 è  uguale a Verde, *68,*Attiva il timer MainClass_C1_timer_T8
    //   ,altrimenti  *68,*Attiva il timer MainClass_C1_timer_T8
    if((L_P1__GetInMainc7(my_id) == verde)){
    
    Timer_Attiva(L_P1__GetMainc46(my_id));
    }else{
    
    Timer_Attiva(L_P1__GetMainc46(my_id));
    }
    
    //  se la macro  MainClass_C1_macrova_M1 ( con argomento_a2   uguale a GialloaVerdea ,argomento_a10   uguale a GialloGiallo ,argomento_a5   uguale a Verde ,argomento_a6   uguale a Verde  e argomento_a1   uguale a RossoGiallox )   è  diverso da  True  *40,*  *36,* e  se il timer MainClass_C1_timer_T2 non è disattivo *37,* e  se la variabile MainClass_C1_variabile_V5 non è  uguale a c270x *36,* e  se il timer MainClass_C1_timer_T2 non è attivo *34,* e  se il parametro MainClass_C1_parametro_P8 è  uguale a RossoGialloVerde *35,* o  se il controllo MainClass_C1_controllo_C10 non è  uguale a RossoGialloxVerdex, *66,* Assegna al comando MainClass_C1_comando_C4 il valore  True 
    //   ,altrimenti   Applica gli effetti
    //         della macro MainClass_C1_macroef_M10
    bool res_OrLogicOP_6 = false;
    bool res_AndLogicOP_7 = true;
    bool res_AndLogicOP_8 = true;
    bool res_AndLogicOP_9 = true;
    bool res_AndLogicOP_10 = true;
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (L_P1__Macro3(my_id,rossogiallo2,giallogiall,gialloaverd,verde,verde) == true));
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_NotLogicOP_11);
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! Timer_Disattivo(L_P1__GetMainc44(my_id)));
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_NotLogicOP_12);
    
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_AndLogicOP_10);
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (L_P1__GetMainc34(my_id) == c270x));
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_NotLogicOP_13);
    
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_AndLogicOP_9);
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! Timer_Attivo(L_P1__GetMainc44(my_id)));
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_14);
    
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_AndLogicOP_8);
    res_AndLogicOP_7 = (res_AndLogicOP_7 && (L_P1__GetParamMainc11(my_id) == rossogiallo));
    
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_AndLogicOP_7);
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (L_P1__GetInMainc6(my_id) == rossogiallo1));
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_NotLogicOP_15);
    
    if(res_OrLogicOP_6){
    
    L_P1__SetOutMainc3(my_id,true);
    }else{
    
    L_P1__Macro(my_id);
    }
    
    //  *73,*
    //   *37,*  se la variabile MainClass_C1_variabile_V8 è  maggiore di  *54,* 10 *38,* o  se il contatore MainClass_C1_contatore_Co2 è  diverso da  *56,* 1303 *37,* o  se la variabile MainClass_C1_variabile_V8 è  uguale a  *53,* 4,  Applica gli effetti
    //         della macro MainClass_C1_macroef_M8  *73,*
    //   ,altrimenti   Applica gli effetti
    //         della macro MainClass_C1_macroef_M6
    bool res_OrLogicOP_16 = false;
    bool res_OrLogicOP_17 = false;
    res_OrLogicOP_17 = (res_OrLogicOP_17 || (L_P1__GetMainc35(my_id) > 10u));
    bool res_NotLogicOP_18 = true;
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! (Counter_GetValore(L_P1__GetMainc47(my_id)) == 1303u));
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_NotLogicOP_18);
    
    res_OrLogicOP_16 = (res_OrLogicOP_16 || res_OrLogicOP_17);
    res_OrLogicOP_16 = (res_OrLogicOP_16 || (L_P1__GetMainc35(my_id) == 4u));
    
    if(res_OrLogicOP_16){
    
    L_P1__Macro2(my_id);
    }else{
    
    L_P1__Macro1(my_id);
    }
    
    //  *73,*
    //   *34,*  se lo stato  non è  diverso da  *56,*  state1  *106,* *36,* e  se il timer MainClass_C1_timer_T6 non è scaduto *38,* e  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  *56,* 11 *38,* e  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  *53,* 14214,  Applica gli effetti
    //         della macro MainClass_C1_macroef_M8
    bool res_AndLogicOP_19 = true;
    bool res_AndLogicOP_20 = true;
    bool res_AndLogicOP_21 = true;
    bool res_NotLogicOP_22 = true;
    bool res_NotLogicOP_23 = true;
    res_NotLogicOP_23 = (res_NotLogicOP_23 && ! (L_P1_C1_GetState(my_id) == C1_St_state));
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! res_NotLogicOP_23);
    res_AndLogicOP_21 = (res_AndLogicOP_21 && res_NotLogicOP_22);
    bool res_NotLogicOP_24 = true;
    res_NotLogicOP_24 = (res_NotLogicOP_24 && ! Timer_Scaduto(L_P1__GetMainc45(my_id)));
    res_AndLogicOP_21 = (res_AndLogicOP_21 && res_NotLogicOP_24);
    
    res_AndLogicOP_20 = (res_AndLogicOP_20 && res_AndLogicOP_21);
    bool res_NotLogicOP_25 = true;
    bool res_NotLogicOP_26 = true;
    res_NotLogicOP_26 = (res_NotLogicOP_26 && ! (Counter_GetValore(L_P1__GetMainc47(my_id)) == 11u));
    res_NotLogicOP_25 = (res_NotLogicOP_25 && ! res_NotLogicOP_26);
    res_AndLogicOP_20 = (res_AndLogicOP_20 && res_NotLogicOP_25);
    
    res_AndLogicOP_19 = (res_AndLogicOP_19 && res_AndLogicOP_20);
    bool res_NotLogicOP_27 = true;
    res_NotLogicOP_27 = (res_NotLogicOP_27 && ! (Counter_GetValore(L_P1__GetMainc47(my_id)) == 14214u));
    res_AndLogicOP_19 = (res_AndLogicOP_19 && res_NotLogicOP_27);
    
    if(res_AndLogicOP_19){
    
    L_P1__Macro2(my_id);
    }
}


/*
    CNL corrispondente:
     { commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV2 non è  uguale a RossoGialloVerde, commento: {71,}Decrementa il contatore MainClass_C1_contatore_Co4
    
       
     commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI3 non è attivo commento: {34,} e  se il parametro MainClass_C1_parametro_P3 è  uguale a Verde, commento: {66,} Assegna al comando MainClass_C1_comando_C4 il valore  False 
    
       
      se il controllo ConsDef è uguale a FALSE  commento: {36,} e  se il timer MainClass_C1_timer_T8 non è disattivo, commento: {68,}Attiva il timer MainClass_C1_timer_T8
    
       
     }
*/
static inline void L_P1__Effec5(instance_id_t const my_id)
{
    
    //  *109,*  se il ripristino della variabile  MainClass_C1_restoreva_RV2 non è  uguale a RossoGialloVerde, *71,*Decrementa il contatore MainClass_C1_contatore_Co4
    bool res_NotLogicOP_0 = true;
    res_NotLogicOP_0 = (res_NotLogicOP_0 && ! (L_P1__GetMainc33(my_id) == rossogiallo));
    if(res_NotLogicOP_0){
    
    Counter_Decr(L_P1__GetMainc48(my_id));
    }
    
    //  *110,*  se il ripristino del timer  MainClass_C1_restoreTI_TI3 non è attivo *34,* e  se il parametro MainClass_C1_parametro_P3 è  uguale a Verde, *66,* Assegna al comando MainClass_C1_comando_C4 il valore  False
    bool res_AndLogicOP_1 = true;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! Timer_Attivo(L_P1__GetMainc41(my_id)));
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_2);
    res_AndLogicOP_1 = (res_AndLogicOP_1 && (L_P1__GetParamMainc10(my_id) == verde));
    
    if(res_AndLogicOP_1){
    
    L_P1__SetOutMainc3(my_id,false);
    }
    
    //  se il controllo ConsDef è uguale a FALSE  *36,* e  se il timer MainClass_C1_timer_T8 non è disattivo, *68,*Attiva il timer MainClass_C1_timer_T8
    bool res_AndLogicOP_3 = true;
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! Timer_Disattivo(L_P1__GetMainc46(my_id)));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_4);
    
    if(res_AndLogicOP_3){
    
    Timer_Attiva(L_P1__GetMainc46(my_id));
    }
}


/*
    CNL corrispondente:
     { commento: {35,}  se il controllo MainClass_C1_controllo_C10 è  diverso da RossoGialloxVerdex commento: {35,} e  se il controllo MainClass_C1_controllo_C2 non è  diverso da Verde,  Applica gli effetti
           della macro MainClass_C1_macroef_M6   commento: {73,}
    
       
     }
*/
static inline void L_P1__Effec6(instance_id_t const my_id)
{
    
    //  *35,*  se il controllo MainClass_C1_controllo_C10 è  diverso da RossoGialloxVerdex *35,* e  se il controllo MainClass_C1_controllo_C2 non è  diverso da Verde,  Applica gli effetti
    //         della macro MainClass_C1_macroef_M6
    bool res_AndLogicOP_0 = true;
    bool res_NotLogicOP_1 = true;
    res_NotLogicOP_1 = (res_NotLogicOP_1 && ! (L_P1__GetInMainc6(my_id) == rossogiallo1));
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_NotLogicOP_1);
    bool res_NotLogicOP_2 = true;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__GetInMainc7(my_id) == verde));
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! res_NotLogicOP_3);
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_NotLogicOP_2);
    
    if(res_AndLogicOP_0){
    
    L_P1__Macro1(my_id);
    }
}


/*
    CNL corrispondente:
    
    {
    
     commento: {35,}  se il controllo MainClass_C1_controllo_C2 è  uguale a Verde commento: {38,} o  se il contatore MainClass_C1_contatore_Co4 è  minore di  commento: {55,} 12 e  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} e  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  commento: {56,} 11321 commento: {36,} e  se il timer MainClass_C1_timer_T6 è disattivo, commento: {66,} Assegna al comando MainClass_C1_comando_C1 il valore  False 
    
       
     commento: {35,}  se il controllo MainClass_C1_controllo_C1 è  diverso da RossoGialloxVerdex commento: {38,} o  se il contatore MainClass_C1_contatore_Co2 è  maggiore di  commento: {54,} 1545 commento: {36,} e  se il timer MainClass_C1_timer_T2 è disattivo,  Applica gli effetti
           della macro MainClass_C1_macroef_M8  commento: {73,}
    
     ,altrimenti  commento: {69,}Disattiva il timer MainClass_C1_timer_T2
    
    
      se il controllo ConsDef è uguale a FALSE , commento: {67,} Assegna alla variabile MainClass_C1_variabile_V5 il valore c270x
    
     ,altrimenti  commento: {69,}Disattiva il timer MainClass_C1_timer_T2
    
    
     commento: {38,}  se il contatore MainClass_C1_contatore_Co4 è  minore di  commento: {55,} 110 commento: {38,} o  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  commento: {56,} 143 commento: {37,} e  se la variabile MainClass_C1_variabile_V8 è  maggiore di  commento: {54,} 5 commento: {38,} o  se il contatore MainClass_C1_contatore_Co2 non è  minore di  commento: {55,} 142145 e  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} e  se la variabile MainClass_C1_variabile_V8 è  minore di  commento: {55,} 6, commento: {72,}Azzera il contatore MainClass_C1_contatore_Co4
    
     ,altrimenti  commento: {66,} Assegna al comando MainClass_C1_comando_C4 il valore  False 
    
    
     commento: {38,}  se il contatore MainClass_C1_contatore_Co2 non è  maggiore di  commento: {54,} 120 commento: {36,} e  se il timer MainClass_C1_timer_T2 è scaduto, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V5 il valore c270x
    
       
    
    }
*/
static inline void L_P1__Effec7(instance_id_t const my_id)
{
    
    //  *35,*  se il controllo MainClass_C1_controllo_C2 è  uguale a Verde *38,* o  se il contatore MainClass_C1_contatore_Co4 è  minore di  *55,* 12 e  se il controllo ConsDef  è  uguale a FALSE  *38,* e  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  *56,* 11321 *36,* e  se il timer MainClass_C1_timer_T6 è disattivo, *66,* Assegna al comando MainClass_C1_comando_C1 il valore  False
    bool res_OrLogicOP_0 = false;
    res_OrLogicOP_0 = (res_OrLogicOP_0 || (L_P1__GetInMainc7(my_id) == verde));
    bool res_AndLogicOP_1 = true;
    bool res_AndLogicOP_2 = true;
    bool res_AndLogicOP_3 = true;
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (Counter_GetValore(L_P1__GetMainc48(my_id)) < 12u));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (L_P1__GetInConsd(my_id) == false));
    
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_AndLogicOP_3);
    bool res_NotLogicOP_4 = true;
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (Counter_GetValore(L_P1__GetMainc48(my_id)) == 11321u));
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! res_NotLogicOP_5);
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_4);
    
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_AndLogicOP_2);
    res_AndLogicOP_1 = (res_AndLogicOP_1 && Timer_Disattivo(L_P1__GetMainc45(my_id)));
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_1);
    
    if(res_OrLogicOP_0){
    
    L_P1__SetOutMainc(my_id,false);
    }
    
    //  *35,*  se il controllo MainClass_C1_controllo_C1 è  diverso da RossoGialloxVerdex *38,* o  se il contatore MainClass_C1_contatore_Co2 è  maggiore di  *54,* 1545 *36,* e  se il timer MainClass_C1_timer_T2 è disattivo,  Applica gli effetti
    //         della macro MainClass_C1_macroef_M8  *73,*
    //   ,altrimenti  *69,*Disattiva il timer MainClass_C1_timer_T2
    bool res_OrLogicOP_6 = false;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetInMainc5(my_id) == rossogiallo1));
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_NotLogicOP_7);
    bool res_AndLogicOP_8 = true;
    res_AndLogicOP_8 = (res_AndLogicOP_8 && (Counter_GetValore(L_P1__GetMainc47(my_id)) > 1545u));
    res_AndLogicOP_8 = (res_AndLogicOP_8 && Timer_Disattivo(L_P1__GetMainc44(my_id)));
    
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_AndLogicOP_8);
    
    if(res_OrLogicOP_6){
    
    L_P1__Macro2(my_id);
    }else{
    
    Timer_Disattiva(L_P1__GetMainc44(my_id));
    }
    
    //  se il controllo ConsDef è uguale a FALSE , *67,* Assegna alla variabile MainClass_C1_variabile_V5 il valore c270x
    //   ,altrimenti  *69,*Disattiva il timer MainClass_C1_timer_T2
    if((L_P1__GetInConsd(my_id) == false)){
    
    L_P1__SetMainc34(my_id,c270x);
    }else{
    
    Timer_Disattiva(L_P1__GetMainc44(my_id));
    }
    
    //  *38,*  se il contatore MainClass_C1_contatore_Co4 è  minore di  *55,* 110 *38,* o  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  *56,* 143 *37,* e  se la variabile MainClass_C1_variabile_V8 è  maggiore di  *54,* 5 *38,* o  se il contatore MainClass_C1_contatore_Co2 non è  minore di  *55,* 142145 e  se il controllo ConsDef  è  uguale a FALSE  *37,* e  se la variabile MainClass_C1_variabile_V8 è  minore di  *55,* 6, *72,*Azzera il contatore MainClass_C1_contatore_Co4
    //   ,altrimenti  *66,* Assegna al comando MainClass_C1_comando_C4 il valore  False
    bool res_OrLogicOP_9 = false;
    bool res_OrLogicOP_10 = false;
    res_OrLogicOP_10 = (res_OrLogicOP_10 || (Counter_GetValore(L_P1__GetMainc48(my_id)) < 110u));
    bool res_AndLogicOP_11 = true;
    bool res_NotLogicOP_12 = true;
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (Counter_GetValore(L_P1__GetMainc47(my_id)) == 143u));
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! res_NotLogicOP_13);
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_NotLogicOP_12);
    res_AndLogicOP_11 = (res_AndLogicOP_11 && (L_P1__GetMainc35(my_id) > 5u));
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_AndLogicOP_11);
    
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_OrLogicOP_10);
    bool res_AndLogicOP_14 = true;
    bool res_AndLogicOP_15 = true;
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (Counter_GetValore(L_P1__GetMainc47(my_id)) < 142145u));
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_NotLogicOP_16);
    res_AndLogicOP_15 = (res_AndLogicOP_15 && (L_P1__GetInConsd(my_id) == false));
    
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_AndLogicOP_15);
    res_AndLogicOP_14 = (res_AndLogicOP_14 && (L_P1__GetMainc35(my_id) < 6u));
    
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_AndLogicOP_14);
    
    if(res_OrLogicOP_9){
    
    Counter_Res(L_P1__GetMainc48(my_id));
    }else{
    
    L_P1__SetOutMainc3(my_id,false);
    }
    
    //  *38,*  se il contatore MainClass_C1_contatore_Co2 non è  maggiore di  *54,* 120 *36,* e  se il timer MainClass_C1_timer_T2 è scaduto, *67,* Assegna alla variabile MainClass_C1_variabile_V5 il valore c270x
    bool res_AndLogicOP_17 = true;
    bool res_NotLogicOP_18 = true;
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! (Counter_GetValore(L_P1__GetMainc47(my_id)) > 120u));
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_NotLogicOP_18);
    res_AndLogicOP_17 = (res_AndLogicOP_17 && Timer_Scaduto(L_P1__GetMainc44(my_id)));
    
    if(res_AndLogicOP_17){
    
    L_P1__SetMainc34(my_id,c270x);
    }
}


/*
    CNL corrispondente:
     { commento: {36,}  se il timer MainClass_C1_timer_T2 è attivo commento: {36,} e  se il timer MainClass_C1_timer_T6 non è disattivo commento: {36,} e  se il timer MainClass_C1_timer_T2 non è scaduto commento: {35,} o  se il controllo MainClass_C1_controllo_C2 è  uguale a Verde o  se il controllo ConsDef  è  uguale a FALSE , commento: {71,}Decrementa il contatore MainClass_C1_contatore_Co2
    
     ,altrimenti  commento: {69,}Disattiva il timer MainClass_C1_timer_T2
    
    
     commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV2 è  diverso da RossoGialloVerde commento: {36,} e  se il timer MainClass_C1_timer_T6 è attivo, commento: {66,} Assegna al comando MainClass_C1_comando_C4 il valore  False 
    
     ,altrimenti  commento: {66,} Assegna al comando MainClass_C1_comando_C4 il valore  True 
    
    
     commento: {36,}  se il timer MainClass_C1_timer_T2 è attivo, commento: {66,} Assegna al comando MainClass_C1_comando_C4 il valore  True 
    
     ,altrimenti   Applica gli effetti
           della macro MainClass_C1_macroef_M8  commento: {73,}
    
    
     commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI4 è scaduto commento: {38,} o  se il contatore MainClass_C1_contatore_Co4 non è  uguale a  commento: {53,} 133214 commento: {38,} e  se il contatore MainClass_C1_contatore_Co4 è  maggiore di  commento: {54,} 155, commento: {66,} Assegna al comando MainClass_C1_comando_C2 il valore RossoGialloVerde
    
     ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V8 il valore 10
    
    
     }
*/
static inline void L_P1__Effec8(instance_id_t const my_id)
{
    
    //  *36,*  se il timer MainClass_C1_timer_T2 è attivo *36,* e  se il timer MainClass_C1_timer_T6 non è disattivo *36,* e  se il timer MainClass_C1_timer_T2 non è scaduto *35,* o  se il controllo MainClass_C1_controllo_C2 è  uguale a Verde o  se il controllo ConsDef  è  uguale a FALSE , *71,*Decrementa il contatore MainClass_C1_contatore_Co2
    //   ,altrimenti  *69,*Disattiva il timer MainClass_C1_timer_T2
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_AndLogicOP_2 = true;
    bool res_AndLogicOP_3 = true;
    res_AndLogicOP_3 = (res_AndLogicOP_3 && Timer_Attivo(L_P1__GetMainc44(my_id)));
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! Timer_Disattivo(L_P1__GetMainc45(my_id)));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_4);
    
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_AndLogicOP_3);
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! Timer_Scaduto(L_P1__GetMainc44(my_id)));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_5);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_2);
    res_OrLogicOP_1 = (res_OrLogicOP_1 || (L_P1__GetInMainc7(my_id) == verde));
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    res_OrLogicOP_0 = (res_OrLogicOP_0 || (L_P1__GetInConsd(my_id) == false));
    
    if(res_OrLogicOP_0){
    
    Counter_Decr(L_P1__GetMainc47(my_id));
    }else{
    
    Timer_Disattiva(L_P1__GetMainc44(my_id));
    }
    
    //  *109,*  se il ripristino della variabile  MainClass_C1_restoreva_RV2 è  diverso da RossoGialloVerde *36,* e  se il timer MainClass_C1_timer_T6 è attivo, *66,* Assegna al comando MainClass_C1_comando_C4 il valore  False 
    //   ,altrimenti  *66,* Assegna al comando MainClass_C1_comando_C4 il valore  True
    bool res_AndLogicOP_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetMainc33(my_id) == rossogiallo));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_7);
    res_AndLogicOP_6 = (res_AndLogicOP_6 && Timer_Attivo(L_P1__GetMainc45(my_id)));
    
    if(res_AndLogicOP_6){
    
    L_P1__SetOutMainc3(my_id,false);
    }else{
    
    L_P1__SetOutMainc3(my_id,true);
    }
    
    //  *36,*  se il timer MainClass_C1_timer_T2 è attivo, *66,* Assegna al comando MainClass_C1_comando_C4 il valore  True 
    //   ,altrimenti   Applica gli effetti
    //         della macro MainClass_C1_macroef_M8
    if(Timer_Attivo(L_P1__GetMainc44(my_id))){
    
    L_P1__SetOutMainc3(my_id,true);
    }else{
    
    L_P1__Macro2(my_id);
    }
    
    //  *73,*
    //   *110,*  se il ripristino del timer  MainClass_C1_restoreTI_TI4 è scaduto *38,* o  se il contatore MainClass_C1_contatore_Co4 non è  uguale a  *53,* 133214 *38,* e  se il contatore MainClass_C1_contatore_Co4 è  maggiore di  *54,* 155, *66,* Assegna al comando MainClass_C1_comando_C2 il valore RossoGialloVerde
    //   ,altrimenti  *67,* Assegna alla variabile MainClass_C1_variabile_V8 il valore 10
    bool res_OrLogicOP_8 = false;
    res_OrLogicOP_8 = (res_OrLogicOP_8 || Timer_Scaduto(L_P1__GetMainc43(my_id)));
    bool res_AndLogicOP_9 = true;
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (Counter_GetValore(L_P1__GetMainc48(my_id)) == 133214u));
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_NotLogicOP_10);
    res_AndLogicOP_9 = (res_AndLogicOP_9 && (Counter_GetValore(L_P1__GetMainc48(my_id)) > 155u));
    
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_AndLogicOP_9);
    
    if(res_OrLogicOP_8){
    
    L_P1__SetOutMainc2(my_id,rossogiallo);
    }else{
    
    L_P1__SetMainc35(my_id,10u);
    }
}


/*
    CNL corrispondente:
     { commento: {37,}  se la variabile MainClass_C1_variabile_V8 è  diverso da  commento: {56,} 8 commento: {36,} o  se il timer MainClass_C1_timer_T2 non è scaduto commento: {37,} o  se la variabile MainClass_C1_variabile_V5 non è  diverso da c270x commento: {35,} o  se il controllo MainClass_C1_controllo_C2 è  uguale a Verde,  Applica gli effetti
           della macro MainClass_C1_macroef_M6   commento: {73,}
    
     ,altrimenti  commento: {68,}Attiva il timer MainClass_C1_timer_T2
    
    
     commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è scaduto commento: {38,} e  se il contatore MainClass_C1_contatore_Co2 è  diverso da  commento: {56,} 12321 commento: {36,} e  se il timer MainClass_C1_timer_T2 è scaduto commento: {38,} o  se il contatore MainClass_C1_contatore_Co4 non è  minore di  commento: {55,} 13 commento: {34,} o  se il parametro MainClass_C1_parametro_P8 non è  diverso da RossoGialloVerde commento: {34,} o  se il parametro MainClass_C1_parametro_P8 non è  diverso da RossoGialloVerde,  Applica gli effetti
           della macro MainClass_C1_macroef_M10  commento: {73,}
    
     ,altrimenti  commento: {71,}Decrementa il contatore MainClass_C1_contatore_Co4
    
    
     }
*/
static inline void L_P1__Effec9(instance_id_t const my_id)
{
    
    //  *37,*  se la variabile MainClass_C1_variabile_V8 è  diverso da  *56,* 8 *36,* o  se il timer MainClass_C1_timer_T2 non è scaduto *37,* o  se la variabile MainClass_C1_variabile_V5 non è  diverso da c270x *35,* o  se il controllo MainClass_C1_controllo_C2 è  uguale a Verde,  Applica gli effetti
    //         della macro MainClass_C1_macroef_M6   *73,*
    //   ,altrimenti  *68,*Attiva il timer MainClass_C1_timer_T2
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_OrLogicOP_2 = false;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__GetMainc35(my_id) == 8u));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_3);
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! Timer_Scaduto(L_P1__GetMainc44(my_id)));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_4);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_OrLogicOP_2);
    bool res_NotLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetMainc34(my_id) == c270x));
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! res_NotLogicOP_6);
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_NotLogicOP_5);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    res_OrLogicOP_0 = (res_OrLogicOP_0 || (L_P1__GetInMainc7(my_id) == verde));
    
    if(res_OrLogicOP_0){
    
    L_P1__Macro1(my_id);
    }else{
    
    Timer_Attiva(L_P1__GetMainc44(my_id));
    }
    
    //  *110,*  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è scaduto *38,* e  se il contatore MainClass_C1_contatore_Co2 è  diverso da  *56,* 12321 *36,* e  se il timer MainClass_C1_timer_T2 è scaduto *38,* o  se il contatore MainClass_C1_contatore_Co4 non è  minore di  *55,* 13 *34,* o  se il parametro MainClass_C1_parametro_P8 non è  diverso da RossoGialloVerde *34,* o  se il parametro MainClass_C1_parametro_P8 non è  diverso da RossoGialloVerde,  Applica gli effetti
    //         della macro MainClass_C1_macroef_M10  *73,*
    //   ,altrimenti  *71,*Decrementa il contatore MainClass_C1_contatore_Co4
    bool res_OrLogicOP_7 = false;
    bool res_OrLogicOP_8 = false;
    bool res_OrLogicOP_9 = false;
    bool res_AndLogicOP_10 = true;
    bool res_AndLogicOP_11 = true;
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! Timer_Scaduto(L_P1__GetMainc37(my_id)));
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_NotLogicOP_12);
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (Counter_GetValore(L_P1__GetMainc47(my_id)) == 12321u));
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_NotLogicOP_13);
    
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_AndLogicOP_11);
    res_AndLogicOP_10 = (res_AndLogicOP_10 && Timer_Scaduto(L_P1__GetMainc44(my_id)));
    
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_AndLogicOP_10);
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (Counter_GetValore(L_P1__GetMainc48(my_id)) < 13u));
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_NotLogicOP_14);
    
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_OrLogicOP_9);
    bool res_NotLogicOP_15 = true;
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (L_P1__GetParamMainc11(my_id) == rossogiallo));
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! res_NotLogicOP_16);
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_NotLogicOP_15);
    
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_OrLogicOP_8);
    bool res_NotLogicOP_17 = true;
    bool res_NotLogicOP_18 = true;
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! (L_P1__GetParamMainc11(my_id) == rossogiallo));
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! res_NotLogicOP_18);
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_NotLogicOP_17);
    
    if(res_OrLogicOP_7){
    
    L_P1__Macro(my_id);
    }else{
    
    Counter_Decr(L_P1__GetMainc48(my_id));
    }
}


/*
    CNL corrispondente:
     {  se il ripristino dello stato  non è  diverso da  commento: {56,}  state1  commento: {107,} commento: {38,} o  se il contatore MainClass_C1_contatore_Co2 non è  maggiore di  commento: {54,} 15450 commento: {35,} e  se il controllo MainClass_C1_controllo_C2 è  diverso da Verde commento: {38,} e  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  commento: {56,} 13, commento: {72,}Azzera il contatore MainClass_C1_contatore_Co4
    
       
     }
*/
static inline void L_P1__Effec10(instance_id_t const my_id)
{
    
    //  se il ripristino dello stato  non è  diverso da  *56,*  state1  *107,* *38,* o  se il contatore MainClass_C1_contatore_Co2 non è  maggiore di  *54,* 15450 *35,* e  se il controllo MainClass_C1_controllo_C2 è  diverso da Verde *38,* e  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  *56,* 13, *72,*Azzera il contatore MainClass_C1_contatore_Co4
    bool res_OrLogicOP_0 = false;
    bool res_NotLogicOP_1 = true;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (L_P1__GetStato1(my_id) == C1_St_state));
    res_NotLogicOP_1 = (res_NotLogicOP_1 && ! res_NotLogicOP_2);
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_1);
    bool res_AndLogicOP_3 = true;
    bool res_AndLogicOP_4 = true;
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (Counter_GetValore(L_P1__GetMainc47(my_id)) > 15450u));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_5);
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetInMainc7(my_id) == verde));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_6);
    
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_AndLogicOP_4);
    bool res_NotLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (Counter_GetValore(L_P1__GetMainc47(my_id)) == 13u));
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! res_NotLogicOP_8);
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_7);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_3);
    
    if(res_OrLogicOP_0){
    
    Counter_Res(L_P1__GetMainc48(my_id));
    }
}


/*
    CNL corrispondente:
     {  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} e  se il controllo MainClass_C1_controllo_C2 non è  uguale a Verde commento: {34,} e  se il parametro MainClass_C1_parametro_P8 non è  uguale a RossoGialloVerde, commento: {69,}Disattiva il timer MainClass_C1_timer_T2
    
     ,altrimenti  commento: {69,}Disattiva il timer MainClass_C1_timer_T6
    
    
     }
*/
static inline void L_P1__Effec11(instance_id_t const my_id)
{
    
    //  se il controllo ConsDef  è  uguale a FALSE  *35,* e  se il controllo MainClass_C1_controllo_C2 non è  uguale a Verde *34,* e  se il parametro MainClass_C1_parametro_P8 non è  uguale a RossoGialloVerde, *69,*Disattiva il timer MainClass_C1_timer_T2
    //   ,altrimenti  *69,*Disattiva il timer MainClass_C1_timer_T6
    bool res_AndLogicOP_0 = true;
    bool res_AndLogicOP_1 = true;
    res_AndLogicOP_1 = (res_AndLogicOP_1 && (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (L_P1__GetInMainc7(my_id) == verde));
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_2);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_AndLogicOP_1);
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__GetParamMainc11(my_id) == rossogiallo));
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_NotLogicOP_3);
    
    if(res_AndLogicOP_0){
    
    Timer_Disattiva(L_P1__GetMainc44(my_id));
    }else{
    
    Timer_Disattiva(L_P1__GetMainc45(my_id));
    }
}


/*
    CNL corrispondente:
     {  se il ripristino dello stato  non è  uguale a  commento: {53,}  state1  commento: {107,} o  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro MainClass_C1_parametro_P3 non è  diverso da Verde commento: {35,} o  se il controllo MainClass_C1_controllo_C2 non è  uguale a Verde commento: {37,} o  se la variabile MainClass_C1_variabile_V5 non è  diverso da c270x,  Applica gli effetti
           della macro MainClass_C1_macroef_M6   commento: {73,}
    
     ,altrimenti   Applica gli effetti
           della macro MainClass_C1_macroef_M8  commento: {73,}
    
    
     }
*/
static inline void L_P1__Effec12(instance_id_t const my_id)
{
    
    //  se il ripristino dello stato  non è  uguale a  *53,*  state1  *107,* o  se il controllo ConsDef  è  uguale a FALSE  *34,* e  se il parametro MainClass_C1_parametro_P3 non è  diverso da Verde *35,* o  se il controllo MainClass_C1_controllo_C2 non è  uguale a Verde *37,* o  se la variabile MainClass_C1_variabile_V5 non è  diverso da c270x,  Applica gli effetti
    //         della macro MainClass_C1_macroef_M6   *73,*
    //   ,altrimenti   Applica gli effetti
    //         della macro MainClass_C1_macroef_M8
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_OrLogicOP_2 = false;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__GetStato1(my_id) == C1_St_state));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_3);
    bool res_AndLogicOP_4 = true;
    res_AndLogicOP_4 = (res_AndLogicOP_4 && (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetParamMainc10(my_id) == verde));
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! res_NotLogicOP_6);
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_5);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_4);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_OrLogicOP_2);
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetInMainc7(my_id) == verde));
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_NotLogicOP_7);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_NotLogicOP_8 = true;
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetMainc34(my_id) == c270x));
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! res_NotLogicOP_9);
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_8);
    
    if(res_OrLogicOP_0){
    
    L_P1__Macro1(my_id);
    }else{
    
    L_P1__Macro2(my_id);
    }
}



// ********** Definizione metodi **********

// Metodi standard

void L_P1_C1_Init(instance_id_t const my_id)
{
    // init variabili di stato
    L_P1__SetMainc20(my_id, gialloaverd);
    L_P1__SetMainc22(my_id, false);
    L_P1__SetMainc24(my_id, giallogiall);
    L_P1__SetMainc26(my_id, 0);
    L_P1__SetMainc28(my_id, false);
    L_P1__SetMainc30(my_id, 0);
    L_P1__SetMainc31(my_id, 0);
    L_P1__SetMainc32(my_id, gialloaverd);
    L_P1__SetMainc33(my_id, gialloaverd);
    L_P1__SetMainc34(my_id, rossogiallo2);
    L_P1__SetMainc35(my_id, 0);
    L_P1__SetStato1(my_id, C1_St_Stato);
    // init controlli precedenti
    L_P1__SetMainc13(my_id, false);
    L_P1__SetMainc15(my_id, true);
    L_P1__SetMainc17(my_id, rossogiallo1);
    L_P1__SetMainc19(my_id, c270x);
    // init Timer e Counter
    Timer_AggmInit(L_P1__GetMainc36(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc36_ID);
    Timer_Init(L_P1__GetMainc36(my_id), 50000);
    Timer_AggmInit(L_P1__GetMainc37(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc37_ID);
    Timer_Init(L_P1__GetMainc37(my_id), 50000);
    Timer_AggmInit(L_P1__GetMainc38(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc38_ID);
    Timer_Init(L_P1__GetMainc38(my_id), 1000);
    Timer_AggmInit(L_P1__GetMainc39(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc39_ID);
    Timer_Init(L_P1__GetMainc39(my_id), 1000);
    Timer_AggmInit(L_P1__GetMainc40(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc40_ID);
    Timer_Init(L_P1__GetMainc40(my_id), 5000);
    Timer_AggmInit(L_P1__GetMainc41(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc41_ID);
    Timer_Init(L_P1__GetMainc41(my_id), 5000);
    Timer_AggmInit(L_P1__GetMainc42(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc42_ID);
    Timer_Init(L_P1__GetMainc42(my_id), 5000);
    Timer_AggmInit(L_P1__GetMainc43(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc43_ID);
    Timer_Init(L_P1__GetMainc43(my_id), 5000);
    Timer_AggmInit(L_P1__GetMainc44(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc44_ID);
    Timer_Init(L_P1__GetMainc44(my_id), 4000);
    Timer_AggmInit(L_P1__GetMainc45(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc45_ID);
    Timer_Init(L_P1__GetMainc45(my_id), 52145000);
    Timer_AggmInit(L_P1__GetMainc46(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc46_ID);
    Timer_Init(L_P1__GetMainc46(my_id), 43000);
    Counter_AggmInit(L_P1__GetMainc47(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc47_ID);
    Counter_Init(L_P1__GetMainc47(my_id));
    Counter_AggmInit(L_P1__GetMainc48(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc48_ID);
    Counter_Init(L_P1__GetMainc48(my_id));
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
        // Reset risposte ai comandi manuali
        L_P1_C1_InitCmdsResponse(my_id);
	L_P1_C1_SetExpectedCmdsResponse(my_id, L_P1_C1_GetState(my_id));
        switch (L_P1_C1_GetState(my_id)) {

        case C1_St_state1:
            if (L_P1__Guard12(my_id)) {
                L_P1_C1_SetState(my_id, C1_St_state1);
                L_P1__Effec12(my_id);				
            }
            else if (L_P1__Guard10(my_id)) {
                L_P1_C1_SetState(my_id, C1_St_state1);
                L_P1__Effec10(my_id);				
            }
            else
                { } // fine transizioni da state1 nella fase LDS_PHASE_MANUAL
            break;

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

        case C1_St_state1:
            if (L_P1__Guard8(my_id)) {
                L_P1_C1_SetState(my_id, C1_St_state1);
                L_P1__Effec8(my_id);				
            }
            else if (L_P1__Guard9(my_id)) {
                L_P1_C1_SetState(my_id, C1_St_state);
                L_P1__Effec9(my_id);				
            }
            else if (L_P1__Guard11(my_id)) {
                L_P1_C1_SetState(my_id, C1_St_state);
                L_P1__Effec11(my_id);				
            }
            else if (L_P1__Guard7(my_id)) {
                L_P1_C1_SetState(my_id, C1_St_state1);
                L_P1__Effec7(my_id);				
            }
            else
                {STOP_EXECUTION(LOGIC_ERROR); } // fine transizioni da state1 nella fase LDS_PHASE_STATE
            break;

        case C1_St_state:
            if (L_P1__Guard6(my_id)) {
                L_P1_C1_SetState(my_id, C1_St_state1);
                L_P1__Effec6(my_id);				
            }
            else if (L_P1__Guard2(my_id)) {
                L_P1_C1_SetState(my_id, C1_St_state);
                L_P1__Effec2(my_id);				
            }
            else if (L_P1__Guard3(my_id)) {
                L_P1_C1_SetState(my_id, C1_St_state1);
                L_P1__Effec3(my_id);				
            }
            else if (L_P1__Guard4(my_id)) {
                L_P1_C1_SetState(my_id, C1_St_state);
                L_P1__Effec4(my_id);				
            }
            else if (L_P1__Guard5(my_id)) {
                L_P1_C1_SetState(my_id, C1_St_state);
                L_P1__Effec5(my_id);				
            }
            else if (L_P1__Guard1(my_id)) {
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

        case C1_St_state1:
                { } // fine transizioni da state1 nella fase LDS_PHASE_AUTO
            break;

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
}

void L_P1_C1_GSetSafe(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C1(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C1(proc_id);
    L_P1__SetOutMainc(my_id, false);
    L_P1__SetOutMainc1(my_id, rossogiallo1);
    L_P1__SetOutMainc2(my_id, rossogiallo);
    L_P1__SetOutMainc3(my_id, true);
    L_P1__SetOutMainc4(my_id, c270x);
}

void L_P1_C1_GUpdatePrev(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C1(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C1(proc_id);
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
    
    {  se il controllo ConsDef  è  uguale a FALSE , commento: {66,} Assegna al comando MainClass_C1_comando_C2 il valore RossoGialloVerde
    
     ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V5 il valore c270x
    
    
     commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  minore di  commento: {55,} 6 commento: {38,} o  se il contatore MainClass_C1_contatore_Co2 è  maggiore di  commento: {54,} 13 commento: {37,} e  se la variabile MainClass_C1_variabile_V8 non è  minore di  commento: {55,} 4 commento: {35,} e  se il controllo MainClass_C1_controllo_C2 non è  diverso da Verde o  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} e  se il controllo MainClass_C1_controllo_C2 è  uguale a Verde, commento: {71,}Decrementa il contatore MainClass_C1_contatore_Co2
    
     ,altrimenti   commento: {67,} Assegna alla variabile MainClass_C1_variabile_V8 il valore 10 commento: {67,}
    
    
    
    }
*/
void L_P1__Macro(instance_id_t const my_id )
{
//  se il controllo ConsDef  è  uguale a FALSE , *66,* Assegna al comando MainClass_C1_comando_C2 il valore RossoGialloVerde
    // ,altrimenti  *67,* Assegna alla variabile MainClass_C1_variabile_V5 il valore c270x
    if((L_P1__GetInConsd(my_id) == false)){
    
    L_P1__SetOutMainc2(my_id,rossogiallo);
    }else{
    
    L_P1__SetMainc34(my_id,c270x);
    }
    //  *109,*  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  minore di  *55,* 6 *38,* o  se il contatore MainClass_C1_contatore_Co2 è  maggiore di  *54,* 13 *37,* e  se la variabile MainClass_C1_variabile_V8 non è  minore di  *55,* 4 *35,* e  se il controllo MainClass_C1_controllo_C2 non è  diverso da Verde o  se il controllo ConsDef  è  uguale a FALSE  *35,* e  se il controllo MainClass_C1_controllo_C2 è  uguale a Verde, *71,*Decrementa il contatore MainClass_C1_contatore_Co2
    // ,altrimenti   *67,* Assegna alla variabile MainClass_C1_variabile_V8 il valore 10
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    res_OrLogicOP_1 = (res_OrLogicOP_1 || (L_P1__GetMainc31(my_id) < 6u));
    bool res_AndLogicOP_2 = true;
    bool res_AndLogicOP_3 = true;
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (Counter_GetValore(L_P1__GetMainc47(my_id)) > 13u));
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetMainc35(my_id) < 4u));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_4);
    
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_AndLogicOP_3);
    bool res_NotLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetInMainc7(my_id) == verde));
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! res_NotLogicOP_6);
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_5);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_2);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_AndLogicOP_7 = true;
    res_AndLogicOP_7 = (res_AndLogicOP_7 && (L_P1__GetInConsd(my_id) == false));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && (L_P1__GetInMainc7(my_id) == verde));
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_7);
    
    if(res_OrLogicOP_0){
    
    Counter_Decr(L_P1__GetMainc47(my_id));
    }else{
    
    L_P1__SetMainc35(my_id,10u);
    }
}

/*
    CNL corrispondente:
     
    { commento: {36,}  se il timer MainClass_C1_timer_T8 è attivo, commento: {66,} Assegna al comando MainClass_C1_comando_C2 il valore RossoGialloVerde
    
     ,altrimenti  commento: {66,} Assegna al comando MainClass_C1_comando_C9 il valore c270x
    
    
     commento: {34,}  se il parametro MainClass_C1_parametro_P3 è  diverso da Verde commento: {36,} e  se il timer MainClass_C1_timer_T2 non è scaduto, commento: {66,} Assegna al comando MainClass_C1_comando_C4 il valore  True 
    
     ,altrimenti  commento: {69,}Disattiva il timer MainClass_C1_timer_T6
    
    
     commento: {35,}  se il controllo MainClass_C1_controllo_C2 non è  uguale a Verde commento: {36,} o  se il timer MainClass_C1_timer_T2 è attivo,  Applica gli effetti
           della macro MainClass_C1_macroef_M8  commento: {73,}
    
     ,altrimenti  commento: {69,}Disattiva il timer MainClass_C1_timer_T6
    
    
    
    }
*/
void L_P1__Macro1(instance_id_t const my_id )
{
//  *36,*  se il timer MainClass_C1_timer_T8 è attivo, *66,* Assegna al comando MainClass_C1_comando_C2 il valore RossoGialloVerde
    // ,altrimenti  *66,* Assegna al comando MainClass_C1_comando_C9 il valore c270x
    if(Timer_Attivo(L_P1__GetMainc46(my_id))){
    
    L_P1__SetOutMainc2(my_id,rossogiallo);
    }else{
    
    L_P1__SetOutMainc4(my_id,c270x);
    }
    //  *34,*  se il parametro MainClass_C1_parametro_P3 è  diverso da Verde *36,* e  se il timer MainClass_C1_timer_T2 non è scaduto, *66,* Assegna al comando MainClass_C1_comando_C4 il valore  True 
    // ,altrimenti  *69,*Disattiva il timer MainClass_C1_timer_T6
    bool res_AndLogicOP_0 = true;
    bool res_NotLogicOP_1 = true;
    res_NotLogicOP_1 = (res_NotLogicOP_1 && ! (L_P1__GetParamMainc10(my_id) == verde));
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_NotLogicOP_1);
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! Timer_Scaduto(L_P1__GetMainc44(my_id)));
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_NotLogicOP_2);
    
    if(res_AndLogicOP_0){
    
    L_P1__SetOutMainc3(my_id,true);
    }else{
    
    Timer_Disattiva(L_P1__GetMainc45(my_id));
    }
    //  *35,*  se il controllo MainClass_C1_controllo_C2 non è  uguale a Verde *36,* o  se il timer MainClass_C1_timer_T2 è attivo,  Applica gli effetti
    //       della macro MainClass_C1_macroef_M8  *73,*
    // ,altrimenti  *69,*Disattiva il timer MainClass_C1_timer_T6
    bool res_OrLogicOP_3 = false;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetInMainc7(my_id) == verde));
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_NotLogicOP_4);
    res_OrLogicOP_3 = (res_OrLogicOP_3 || Timer_Attivo(L_P1__GetMainc44(my_id)));
    
    if(res_OrLogicOP_3){
    
    L_P1__Macro2(my_id);
    }else{
    
    Timer_Disattiva(L_P1__GetMainc45(my_id));
    }
}

/*
    CNL corrispondente:
    
    {  se il ripristino dello stato  è  diverso da  commento: {56,}  state1  commento: {107,} commento: {37,} e  se la variabile MainClass_C1_variabile_V5 è  uguale a c270x commento: {37,} e  se la variabile MainClass_C1_variabile_V8 non è  uguale a  commento: {53,} 8 e  se il controllo ConsDef  è  uguale a FALSE , commento: {67,} Assegna alla variabile MainClass_C1_variabile_V5 il valore c270x
    
       
     commento: {35,}  se il controllo MainClass_C1_controllo_C10 è  diverso da RossoGialloxVerdex commento: {36,} o  se il timer MainClass_C1_timer_T6 non è attivo commento: {34,} o  se il parametro MainClass_C1_parametro_P8 non è  diverso da RossoGialloVerde commento: {37,} e  se la variabile MainClass_C1_variabile_V5 è  uguale a c270x, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V5 il valore c270x
    
       
     commento: {35,}  se il controllo MainClass_C1_controllo_C9 non è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro MainClass_C1_parametro_P3 è  diverso da Verde, commento: {72,}Azzera il contatore MainClass_C1_contatore_Co2
    
       
    
    }
*/
void L_P1__Macro2(instance_id_t const my_id )
{
//  se il ripristino dello stato  è  diverso da  *56,*  state1  *107,* *37,* e  se la variabile MainClass_C1_variabile_V5 è  uguale a c270x *37,* e  se la variabile MainClass_C1_variabile_V8 non è  uguale a  *53,* 8 e  se il controllo ConsDef  è  uguale a FALSE , *67,* Assegna alla variabile MainClass_C1_variabile_V5 il valore c270x
    bool res_AndLogicOP_0 = true;
    bool res_AndLogicOP_1 = true;
    bool res_AndLogicOP_2 = true;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__GetStato1(my_id) == C1_St_state));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_3);
    res_AndLogicOP_2 = (res_AndLogicOP_2 && (L_P1__GetMainc34(my_id) == c270x));
    
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_AndLogicOP_2);
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetMainc35(my_id) == 8u));
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_4);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_AndLogicOP_1);
    res_AndLogicOP_0 = (res_AndLogicOP_0 && (L_P1__GetInConsd(my_id) == false));
    
    if(res_AndLogicOP_0){
    
    L_P1__SetMainc34(my_id,c270x);
    }
    //  *35,*  se il controllo MainClass_C1_controllo_C10 è  diverso da RossoGialloxVerdex *36,* o  se il timer MainClass_C1_timer_T6 non è attivo *34,* o  se il parametro MainClass_C1_parametro_P8 non è  diverso da RossoGialloVerde *37,* e  se la variabile MainClass_C1_variabile_V5 è  uguale a c270x, *67,* Assegna alla variabile MainClass_C1_variabile_V5 il valore c270x
    bool res_OrLogicOP_5 = false;
    bool res_OrLogicOP_6 = false;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetInMainc6(my_id) == rossogiallo1));
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_NotLogicOP_7);
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! Timer_Attivo(L_P1__GetMainc45(my_id)));
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_NotLogicOP_8);
    
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_OrLogicOP_6);
    bool res_AndLogicOP_9 = true;
    bool res_NotLogicOP_10 = true;
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (L_P1__GetParamMainc11(my_id) == rossogiallo));
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! res_NotLogicOP_11);
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_NotLogicOP_10);
    res_AndLogicOP_9 = (res_AndLogicOP_9 && (L_P1__GetMainc34(my_id) == c270x));
    
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_AndLogicOP_9);
    
    if(res_OrLogicOP_5){
    
    L_P1__SetMainc34(my_id,c270x);
    }
    //  *35,*  se il controllo MainClass_C1_controllo_C9 non è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE  *34,* e  se il parametro MainClass_C1_parametro_P3 è  diverso da Verde, *72,*Azzera il contatore MainClass_C1_contatore_Co2
    bool res_AndLogicOP_12 = true;
    bool res_AndLogicOP_13 = true;
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1__GetInMainc9(my_id) == false));
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_NotLogicOP_14);
    res_AndLogicOP_13 = (res_AndLogicOP_13 && (L_P1__GetInConsd(my_id) == false));
    
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_AndLogicOP_13);
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (L_P1__GetParamMainc10(my_id) == verde));
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_NotLogicOP_15);
    
    if(res_AndLogicOP_12){
    
    Counter_Res(L_P1__GetMainc47(my_id));
    }
}


// Macro di verifica

/*
    CNL corrispondente:
    
    { commento: {61,} commento: {37,}  se la variabile MainClass_C1_variabile_V8 è  diverso da  commento: {56,} 5 commento: {38,} e  se il contatore MainClass_C1_contatore_Co2 è  uguale a  commento: {53,} 1303 commento: {37,} o  se la variabile MainClass_C1_variabile_V8 non è  uguale a  commento: {53,} 4 commento: {34,} o  se il parametro MainClass_C1_parametro_P8 è  diverso da RossoGialloVerde commento: {35,} e  se il controllo MainClass_C1_controllo_C10 è  uguale a RossoGialloxVerdex commento: {38,} o  se il contatore MainClass_C1_contatore_Co4 è  maggiore di  commento: {54,} 152, Tutte le seguenti { 
     commento: {63,} commento: {34,}  se il parametro MainClass_C1_parametro_P8 è  diverso da RossoGialloVerde commento: {38,} o  se il contatore MainClass_C1_contatore_Co2 è  diverso da  commento: {56,} 13 commento: {37,} o  se la variabile MainClass_C1_variabile_V8 è  uguale a  commento: {53,} 7 commento: {37,} e  se la variabile MainClass_C1_variabile_V8 non è  maggiore di  commento: {54,} 3, Solo una delle seguenti { 
     commento: {62,} commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  uguale a  commento: {53,} 1 o  se l'argomento argomento_ave8 è  uguale a  True  commento: {39,}  commento: {36,} o  se il timer MainClass_C1_timer_T6 è disattivo commento: {38,} e  se il contatore MainClass_C1_contatore_Co4 è  minore di  commento: {55,} 12, Almeno una delle seguenti { 
     commento: {62,} commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV2 non è  diverso da RossoGialloVerde e  se l'argomento argomento_ave4 è  diverso da  True  commento: {39,}  commento: {38,} e  se il contatore MainClass_C1_contatore_Co4 è  diverso da  commento: {56,} 11 commento: {35,} e  se il controllo MainClass_C1_controllo_C2 è  uguale a Verde o  se l'argomento argomento_ave4 è  uguale a  False  commento: {39,} , Almeno una delle seguenti { 
     commento: {62,} commento: {38,}  se il contatore MainClass_C1_contatore_Co2 non è  minore di  commento: {55,} 121 commento: {36,} e  se il timer MainClass_C1_timer_T2 è attivo commento: {36,} o  se il timer MainClass_C1_timer_T6 è attivo commento: {34,} o  se il parametro MainClass_C1_parametro_P8 è  diverso da RossoGialloVerde commento: {35,} e  se il controllo MainClass_C1_controllo_C10 è  uguale a RossoGialloxVerdex, Almeno una delle seguenti { 
     commento: {62,}  se l'argomento argomento_ave8 è  uguale a  True  commento: {39,}  commento: {36,} e  se il timer MainClass_C1_timer_T2 è scaduto, Almeno una delle seguenti { 
     commento: {62,} commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI2 non è disattivo, Almeno una delle seguenti { 
      se l'argomento argomento_ave8 non  è  diverso da  False  commento: {39,}  commento: {35,} e  se il controllo MainClass_C1_controllo_C2 è  diverso da Verde commento: {38,} o  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  commento: {56,} 114 commento: {37,} e  se la variabile MainClass_C1_variabile_V8 non è  minore di  commento: {55,} 5 commento: {37,} e  se la variabile MainClass_C1_variabile_V8 è  diverso da  commento: {56,} 4 o  se l'argomento argomento_ave4 non  è  uguale a  False  commento: {39,} , Verifica che   commento: {49,50,}  commento: {,}  il timer MainClass_C1_timer_T8 sia attivo
     commento: {104,} e  che  commento: {36,}  il timer MainClass_C1_timer_T2 sia disattivo
     commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V8 sia  diverso da  commento: {56,} 10
    
    
     } Verifica che   commento: {47,51,52,}  commento: {,}  il contatore MainClass_C1_contatore_Co2 non sia  diverso da  commento: {56,} 12
     commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P8 sia  uguale a RossoGialloVerde
     commento: {104,} e  che   l'argomento argomento_ave8 sia  diverso da  False  commento: {,} 
     commento: {104,} e  che  commento: {38,}  il contatore MainClass_C1_contatore_Co4 sia  maggiore di  commento: {54,} 10
    
    
     } Verifica che   commento: {48,49,51,52,}  commento: {,}  il timer MainClass_C1_timer_T2 non sia attivo
     commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C2 non sia  diverso da Verde
     commento: {104,} e  che   l'argomento argomento_ave4 non  sia  uguale a  True  commento: {,} 
     commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co2 sia  minore di  commento: {55,} 113
     commento: {104,} e  che  commento: {35,}  il controllo MainClass_C1_controllo_C10 sia  diverso da RossoGialloxVerdex
     commento: {104,} o  che  commento: {35,}  il controllo MainClass_C1_controllo_C2 non sia  uguale a Verde
    
    
     } Verifica che   commento: {47,48,49,}  commento: {,}  il controllo MainClass_C1_controllo_C10 sia  diverso da RossoGialloxVerdex
     commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T2 non sia scaduto
     commento: {104,} e  che  commento: {36,}  il timer MainClass_C1_timer_T2 sia disattivo
     commento: {104,} o  che  commento: {36,}  il timer MainClass_C1_timer_T2 sia scaduto
     commento: {104,} o  che  commento: {35,}  il controllo MainClass_C1_controllo_C10 non sia  diverso da RossoGialloxVerdex
     commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P3 non sia  uguale a Verde
    
    
     } Verifica che   commento: {50,52,}  commento: {,}  la variabile MainClass_C1_variabile_V8 non sia  minore di  commento: {55,} 6
     commento: {104,} o  che   l'argomento argomento_ave4 non  sia  uguale a  True  commento: {,} 
    
    
     } Verifica che   commento: {49,52,}   l'argomento argomento_ave5 sia  uguale a Verde commento: {,} 
     commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T6 sia attivo
     commento: {104,} e  che   l'argomento argomento_ave8 sia  diverso da  True  commento: {39,} 
     commento: {104,} e  che   l'argomento argomento_ave3 non  sia  uguale a  True  commento: {39,} 
    
    
     } Verifica che   commento: {48,49,50,51,52,}  commento: {,}  il contatore MainClass_C1_contatore_Co2 non sia  diverso da  commento: {56,} 14
     commento: {104,} o  che   l'argomento argomento_ave4 non  sia  uguale a  False  commento: {,} 
     commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C2 non sia  uguale a Verde
     commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V5 sia  diverso da c270x
     commento: {104,} o  che   l'argomento argomento_ave3 non  sia  diverso da  False  commento: {39,} 
     commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T8 non sia scaduto
    
    
     } Verifica che   commento: {48,50,51,52,}  commento: {,}  il controllo MainClass_C1_controllo_C5 non sia  diverso da  True 
     commento: {104,} o  che   l'argomento argomento_ave8 non  sia  diverso da  False  commento: {,} 
     commento: {104,} o  che  commento: {,}  il contatore MainClass_C1_contatore_Co4 non sia  maggiore di  commento: {54,} 1121
     commento: {104,} o  che  commento: {35,}  il controllo MainClass_C1_controllo_C2 sia  uguale a Verde
     commento: {104,} e  che   l'argomento argomento_ave4 sia  diverso da  False  commento: {39,} 
     commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V5 sia  uguale a c270x
    
    
    }
*/
bool L_P1__Macro6(instance_id_t const my_id , C1_Enumerat2 argom13, C1_Enumerat2 argom14, bool argom15, bool argom16, C1_Enumerat3 argom17, C1_Enumerat3 argom18, bool argom19)
{
bool res_AndLogicOP_0 = true;
    
    //  *61,* *37,*  se la variabile MainClass_C1_variabile_V8 è  diverso da  *56,* 5 *38,* e  se il contatore MainClass_C1_contatore_Co2 è  uguale a  *53,* 1303 *37,* o  se la variabile MainClass_C1_variabile_V8 non è  uguale a  *53,* 4 *34,* o  se il parametro MainClass_C1_parametro_P8 è  diverso da RossoGialloVerde *35,* e  se il controllo MainClass_C1_controllo_C10 è  uguale a RossoGialloxVerdex *38,* o  se il contatore MainClass_C1_contatore_Co4 è  maggiore di  *54,* 152, Tutte le seguenti { 
    //   *63,* *34,*  se il parametro MainClass_C1_parametro_P8 è  diverso da RossoGialloVerde *38,* o  se il contatore MainClass_C1_contatore_Co2 è  diverso da  *56,* 13 *37,* o  se la variabile MainClass_C1_variabile_V8 è  uguale a  *53,* 7 *37,* e  se la variabile MainClass_C1_variabile_V8 non è  maggiore di  *54,* 3, Solo una delle seguenti { 
    //   *62,* *109,*  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  uguale a  *53,* 1 o  se l'argomento argomento_ave8 è  uguale a  True  *39,*  *36,* o  se il timer MainClass_C1_timer_T6 è disattivo *38,* e  se il contatore MainClass_C1_contatore_Co4 è  minore di  *55,* 12, Almeno una delle seguenti { 
    //   *62,* *109,*  se il ripristino della variabile  MainClass_C1_restoreva_RV2 non è  diverso da RossoGialloVerde e  se l'argomento argomento_ave4 è  diverso da  True  *39,*  *38,* e  se il contatore MainClass_C1_contatore_Co4 è  diverso da  *56,* 11 *35,* e  se il controllo MainClass_C1_controllo_C2 è  uguale a Verde o  se l'argomento argomento_ave4 è  uguale a  False  *39,* , Almeno una delle seguenti { 
    //   *62,* *38,*  se il contatore MainClass_C1_contatore_Co2 non è  minore di  *55,* 121 *36,* e  se il timer MainClass_C1_timer_T2 è attivo *36,* o  se il timer MainClass_C1_timer_T6 è attivo *34,* o  se il parametro MainClass_C1_parametro_P8 è  diverso da RossoGialloVerde *35,* e  se il controllo MainClass_C1_controllo_C10 è  uguale a RossoGialloxVerdex, Almeno una delle seguenti { 
    //   *62,*  se l'argomento argomento_ave8 è  uguale a  True  *39,*  *36,* e  se il timer MainClass_C1_timer_T2 è scaduto, Almeno una delle seguenti { 
    //   *62,* *110,*  se il ripristino del timer  MainClass_C1_restoreTI_TI2 non è disattivo, Almeno una delle seguenti { 
    //    se l'argomento argomento_ave8 non  è  diverso da  False  *39,*  *35,* e  se il controllo MainClass_C1_controllo_C2 è  diverso da Verde *38,* o  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  *56,* 114 *37,* e  se la variabile MainClass_C1_variabile_V8 non è  minore di  *55,* 5 *37,* e  se la variabile MainClass_C1_variabile_V8 è  diverso da  *56,* 4 o  se l'argomento argomento_ave4 non  è  uguale a  False  *39,* , Verifica che   *49,50,*  *,*  il timer MainClass_C1_timer_T8 sia attivo
    //   *104,* e  che  *36,*  il timer MainClass_C1_timer_T2 sia disattivo
    //   *104,* e  che  *,*  la variabile MainClass_C1_variabile_V8 sia  diverso da  *56,* 10
    //   } Verifica che   *47,51,52,*  *,*  il contatore MainClass_C1_contatore_Co2 non sia  diverso da  *56,* 12
    //   *104,* o  che  *34,*  il parametro MainClass_C1_parametro_P8 sia  uguale a RossoGialloVerde
    //   *104,* e  che   l'argomento argomento_ave8 sia  diverso da  False  *,* 
    //   *104,* e  che  *38,*  il contatore MainClass_C1_contatore_Co4 sia  maggiore di  *54,* 10
    //   } Verifica che   *48,49,51,52,*  *,*  il timer MainClass_C1_timer_T2 non sia attivo
    //   *104,* o  che  *,*  il controllo MainClass_C1_controllo_C2 non sia  diverso da Verde
    //   *104,* e  che   l'argomento argomento_ave4 non  sia  uguale a  True  *,* 
    //   *104,* e  che  *,*  il contatore MainClass_C1_contatore_Co2 sia  minore di  *55,* 113
    //   *104,* e  che  *35,*  il controllo MainClass_C1_controllo_C10 sia  diverso da RossoGialloxVerdex
    //   *104,* o  che  *35,*  il controllo MainClass_C1_controllo_C2 non sia  uguale a Verde
    //   } Verifica che   *47,48,49,*  *,*  il controllo MainClass_C1_controllo_C10 sia  diverso da RossoGialloxVerdex
    //   *104,* e  che  *,*  il timer MainClass_C1_timer_T2 non sia scaduto
    //   *104,* e  che  *36,*  il timer MainClass_C1_timer_T2 sia disattivo
    //   *104,* o  che  *36,*  il timer MainClass_C1_timer_T2 sia scaduto
    //   *104,* o  che  *35,*  il controllo MainClass_C1_controllo_C10 non sia  diverso da RossoGialloxVerdex
    //   *104,* o  che  *34,*  il parametro MainClass_C1_parametro_P3 non sia  uguale a Verde
    //   } Verifica che   *50,52,*  *,*  la variabile MainClass_C1_variabile_V8 non sia  minore di  *55,* 6
    //   *104,* o  che   l'argomento argomento_ave4 non  sia  uguale a  True  *,* 
    //   } Verifica che   *49,52,*   l'argomento argomento_ave5 sia  uguale a Verde *,* 
    //   *104,* o  che  *,*  il timer MainClass_C1_timer_T6 sia attivo
    //   *104,* e  che   l'argomento argomento_ave8 sia  diverso da  True  *39,* 
    //   *104,* e  che   l'argomento argomento_ave3 non  sia  uguale a  True  *39,* 
    //   } Verifica che   *48,49,50,51,52,*  *,*  il contatore MainClass_C1_contatore_Co2 non sia  diverso da  *56,* 14
    //   *104,* o  che   l'argomento argomento_ave4 non  sia  uguale a  False  *,* 
    //   *104,* o  che  *,*  il controllo MainClass_C1_controllo_C2 non sia  uguale a Verde
    //   *104,* e  che  *,*  la variabile MainClass_C1_variabile_V5 sia  diverso da c270x
    //   *104,* o  che   l'argomento argomento_ave3 non  sia  diverso da  False  *39,* 
    //   *104,* e  che  *,*  il timer MainClass_C1_timer_T8 non sia scaduto
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_OrLogicOP_4 = false;
    bool res_AndLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetMainc35(my_id) == 5u));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_6);
    res_AndLogicOP_5 = (res_AndLogicOP_5 && (Counter_GetValore(L_P1__GetMainc47(my_id)) == 1303u));
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_AndLogicOP_5);
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetMainc35(my_id) == 4u));
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_NotLogicOP_7);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_OrLogicOP_4);
    bool res_AndLogicOP_8 = true;
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetParamMainc11(my_id) == rossogiallo));
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_9);
    res_AndLogicOP_8 = (res_AndLogicOP_8 && (L_P1__GetInMainc6(my_id) == rossogiallo1));
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_AndLogicOP_8);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    res_OrLogicOP_2 = (res_OrLogicOP_2 || (Counter_GetValore(L_P1__GetMainc48(my_id)) > 152u));
    
    if(res_OrLogicOP_2){
    bool res_AndLogicOP_10 = true;
    bool res_ImpliesLogicOp_11 = true;
    bool res_OrLogicOP_12 = false;
    bool res_OrLogicOP_13 = false;
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1__GetParamMainc11(my_id) == rossogiallo));
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_NotLogicOP_14);
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (Counter_GetValore(L_P1__GetMainc47(my_id)) == 13u));
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_NotLogicOP_15);
    
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_OrLogicOP_13);
    bool res_AndLogicOP_16 = true;
    res_AndLogicOP_16 = (res_AndLogicOP_16 && (L_P1__GetMainc35(my_id) == 7u));
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! (L_P1__GetMainc35(my_id) > 3u));
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_NotLogicOP_17);
    
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_AndLogicOP_16);
    
    if(res_OrLogicOP_12){
    bool res_XorLogicOP_18 = true;
    int xorIndex_res_XorLogicOP_18 = 0;
    bool res_ImpliesLogicOp_19 = true;
    bool res_OrLogicOP_20 = false;
    bool res_OrLogicOP_21 = false;
    res_OrLogicOP_21 = (res_OrLogicOP_21 || (L_P1__GetMainc31(my_id) == 1u));
    res_OrLogicOP_21 = (res_OrLogicOP_21 || (argom19 == true));
    
    res_OrLogicOP_20 = (res_OrLogicOP_20 || res_OrLogicOP_21);
    bool res_AndLogicOP_22 = true;
    res_AndLogicOP_22 = (res_AndLogicOP_22 && Timer_Disattivo(L_P1__GetMainc45(my_id)));
    res_AndLogicOP_22 = (res_AndLogicOP_22 && (Counter_GetValore(L_P1__GetMainc48(my_id)) < 12u));
    
    res_OrLogicOP_20 = (res_OrLogicOP_20 || res_AndLogicOP_22);
    
    if(res_OrLogicOP_20){
    bool res_OrLogicOP_23 = false;
    bool res_ImpliesLogicOp_24 = true;
    bool res_OrLogicOP_25 = false;
    bool res_AndLogicOP_26 = true;
    bool res_AndLogicOP_27 = true;
    bool res_AndLogicOP_28 = true;
    bool res_NotLogicOP_29 = true;
    bool res_NotLogicOP_30 = true;
    res_NotLogicOP_30 = (res_NotLogicOP_30 && ! (L_P1__GetMainc33(my_id) == rossogiallo));
    res_NotLogicOP_29 = (res_NotLogicOP_29 && ! res_NotLogicOP_30);
    res_AndLogicOP_28 = (res_AndLogicOP_28 && res_NotLogicOP_29);
    bool res_NotLogicOP_31 = true;
    res_NotLogicOP_31 = (res_NotLogicOP_31 && ! (argom16 == true));
    res_AndLogicOP_28 = (res_AndLogicOP_28 && res_NotLogicOP_31);
    
    res_AndLogicOP_27 = (res_AndLogicOP_27 && res_AndLogicOP_28);
    bool res_NotLogicOP_32 = true;
    res_NotLogicOP_32 = (res_NotLogicOP_32 && ! (Counter_GetValore(L_P1__GetMainc48(my_id)) == 11u));
    res_AndLogicOP_27 = (res_AndLogicOP_27 && res_NotLogicOP_32);
    
    res_AndLogicOP_26 = (res_AndLogicOP_26 && res_AndLogicOP_27);
    res_AndLogicOP_26 = (res_AndLogicOP_26 && (L_P1__GetInMainc7(my_id) == verde));
    
    res_OrLogicOP_25 = (res_OrLogicOP_25 || res_AndLogicOP_26);
    res_OrLogicOP_25 = (res_OrLogicOP_25 || (argom16 == false));
    
    if(res_OrLogicOP_25){
    bool res_OrLogicOP_33 = false;
    bool res_ImpliesLogicOp_34 = true;
    bool res_OrLogicOP_35 = false;
    bool res_OrLogicOP_36 = false;
    bool res_AndLogicOP_37 = true;
    bool res_NotLogicOP_38 = true;
    res_NotLogicOP_38 = (res_NotLogicOP_38 && ! (Counter_GetValore(L_P1__GetMainc47(my_id)) < 121u));
    res_AndLogicOP_37 = (res_AndLogicOP_37 && res_NotLogicOP_38);
    res_AndLogicOP_37 = (res_AndLogicOP_37 && Timer_Attivo(L_P1__GetMainc44(my_id)));
    
    res_OrLogicOP_36 = (res_OrLogicOP_36 || res_AndLogicOP_37);
    res_OrLogicOP_36 = (res_OrLogicOP_36 || Timer_Attivo(L_P1__GetMainc45(my_id)));
    
    res_OrLogicOP_35 = (res_OrLogicOP_35 || res_OrLogicOP_36);
    bool res_AndLogicOP_39 = true;
    bool res_NotLogicOP_40 = true;
    res_NotLogicOP_40 = (res_NotLogicOP_40 && ! (L_P1__GetParamMainc11(my_id) == rossogiallo));
    res_AndLogicOP_39 = (res_AndLogicOP_39 && res_NotLogicOP_40);
    res_AndLogicOP_39 = (res_AndLogicOP_39 && (L_P1__GetInMainc6(my_id) == rossogiallo1));
    
    res_OrLogicOP_35 = (res_OrLogicOP_35 || res_AndLogicOP_39);
    
    if(res_OrLogicOP_35){
    bool res_OrLogicOP_41 = false;
    bool res_ImpliesLogicOp_42 = true;
    bool res_AndLogicOP_43 = true;
    res_AndLogicOP_43 = (res_AndLogicOP_43 && (argom19 == true));
    res_AndLogicOP_43 = (res_AndLogicOP_43 && Timer_Scaduto(L_P1__GetMainc44(my_id)));
    
    if(res_AndLogicOP_43){
    bool res_OrLogicOP_44 = false;
    bool res_ImpliesLogicOp_45 = true;
    bool res_NotLogicOP_46 = true;
    res_NotLogicOP_46 = (res_NotLogicOP_46 && ! Timer_Disattivo(L_P1__GetMainc39(my_id)));
    if(res_NotLogicOP_46){
    bool res_ImpliesLogicOp_47 = true;
    bool res_OrLogicOP_48 = false;
    bool res_OrLogicOP_49 = false;
    bool res_AndLogicOP_50 = true;
    bool res_NotLogicOP_51 = true;
    bool res_NotLogicOP_52 = true;
    res_NotLogicOP_52 = (res_NotLogicOP_52 && ! (argom19 == false));
    res_NotLogicOP_51 = (res_NotLogicOP_51 && ! res_NotLogicOP_52);
    res_AndLogicOP_50 = (res_AndLogicOP_50 && res_NotLogicOP_51);
    bool res_NotLogicOP_53 = true;
    res_NotLogicOP_53 = (res_NotLogicOP_53 && ! (L_P1__GetInMainc7(my_id) == verde));
    res_AndLogicOP_50 = (res_AndLogicOP_50 && res_NotLogicOP_53);
    
    res_OrLogicOP_49 = (res_OrLogicOP_49 || res_AndLogicOP_50);
    bool res_AndLogicOP_54 = true;
    bool res_AndLogicOP_55 = true;
    bool res_NotLogicOP_56 = true;
    bool res_NotLogicOP_57 = true;
    res_NotLogicOP_57 = (res_NotLogicOP_57 && ! (Counter_GetValore(L_P1__GetMainc48(my_id)) == 114u));
    res_NotLogicOP_56 = (res_NotLogicOP_56 && ! res_NotLogicOP_57);
    res_AndLogicOP_55 = (res_AndLogicOP_55 && res_NotLogicOP_56);
    bool res_NotLogicOP_58 = true;
    res_NotLogicOP_58 = (res_NotLogicOP_58 && ! (L_P1__GetMainc35(my_id) < 5u));
    res_AndLogicOP_55 = (res_AndLogicOP_55 && res_NotLogicOP_58);
    
    res_AndLogicOP_54 = (res_AndLogicOP_54 && res_AndLogicOP_55);
    bool res_NotLogicOP_59 = true;
    res_NotLogicOP_59 = (res_NotLogicOP_59 && ! (L_P1__GetMainc35(my_id) == 4u));
    res_AndLogicOP_54 = (res_AndLogicOP_54 && res_NotLogicOP_59);
    
    res_OrLogicOP_49 = (res_OrLogicOP_49 || res_AndLogicOP_54);
    
    res_OrLogicOP_48 = (res_OrLogicOP_48 || res_OrLogicOP_49);
    bool res_NotLogicOP_60 = true;
    res_NotLogicOP_60 = (res_NotLogicOP_60 && ! (argom16 == false));
    res_OrLogicOP_48 = (res_OrLogicOP_48 || res_NotLogicOP_60);
    
    if(res_OrLogicOP_48){
    bool res_AndLogicOP_61 = true;
    bool res_AndLogicOP_62 = true;
    res_AndLogicOP_62 = (res_AndLogicOP_62 && Timer_Attivo(L_P1__GetMainc46(my_id)));
    res_AndLogicOP_62 = (res_AndLogicOP_62 && Timer_Disattivo(L_P1__GetMainc44(my_id)));
    
    res_AndLogicOP_61 = (res_AndLogicOP_61 && res_AndLogicOP_62);
    bool res_NotLogicOP_63 = true;
    res_NotLogicOP_63 = (res_NotLogicOP_63 && ! (L_P1__GetMainc35(my_id) == 10u));
    res_AndLogicOP_61 = (res_AndLogicOP_61 && res_NotLogicOP_63);
    
    res_ImpliesLogicOp_47 = (res_ImpliesLogicOp_47 && res_AndLogicOP_61);
    }
    res_ImpliesLogicOp_45 = (res_ImpliesLogicOp_45 && res_ImpliesLogicOp_47);
    }
    res_OrLogicOP_44 = (res_OrLogicOP_44 || res_ImpliesLogicOp_45);
    bool res_OrLogicOP_64 = false;
    bool res_NotLogicOP_65 = true;
    bool res_NotLogicOP_66 = true;
    res_NotLogicOP_66 = (res_NotLogicOP_66 && ! (Counter_GetValore(L_P1__GetMainc47(my_id)) == 12u));
    res_NotLogicOP_65 = (res_NotLogicOP_65 && ! res_NotLogicOP_66);
    res_OrLogicOP_64 = (res_OrLogicOP_64 || res_NotLogicOP_65);
    bool res_AndLogicOP_67 = true;
    bool res_AndLogicOP_68 = true;
    res_AndLogicOP_68 = (res_AndLogicOP_68 && (L_P1__GetParamMainc11(my_id) == rossogiallo));
    bool res_NotLogicOP_69 = true;
    res_NotLogicOP_69 = (res_NotLogicOP_69 && ! (argom19 == false));
    res_AndLogicOP_68 = (res_AndLogicOP_68 && res_NotLogicOP_69);
    
    res_AndLogicOP_67 = (res_AndLogicOP_67 && res_AndLogicOP_68);
    res_AndLogicOP_67 = (res_AndLogicOP_67 && (Counter_GetValore(L_P1__GetMainc48(my_id)) > 10u));
    
    res_OrLogicOP_64 = (res_OrLogicOP_64 || res_AndLogicOP_67);
    
    res_OrLogicOP_44 = (res_OrLogicOP_44 || res_OrLogicOP_64);
    
    res_ImpliesLogicOp_42 = (res_ImpliesLogicOp_42 && res_OrLogicOP_44);
    }
    res_OrLogicOP_41 = (res_OrLogicOP_41 || res_ImpliesLogicOp_42);
    bool res_OrLogicOP_70 = false;
    bool res_OrLogicOP_71 = false;
    bool res_NotLogicOP_72 = true;
    res_NotLogicOP_72 = (res_NotLogicOP_72 && ! Timer_Attivo(L_P1__GetMainc44(my_id)));
    res_OrLogicOP_71 = (res_OrLogicOP_71 || res_NotLogicOP_72);
    bool res_AndLogicOP_73 = true;
    bool res_AndLogicOP_74 = true;
    bool res_AndLogicOP_75 = true;
    bool res_NotLogicOP_76 = true;
    bool res_NotLogicOP_77 = true;
    res_NotLogicOP_77 = (res_NotLogicOP_77 && ! (L_P1__GetInMainc7(my_id) == verde));
    res_NotLogicOP_76 = (res_NotLogicOP_76 && ! res_NotLogicOP_77);
    res_AndLogicOP_75 = (res_AndLogicOP_75 && res_NotLogicOP_76);
    bool res_NotLogicOP_78 = true;
    res_NotLogicOP_78 = (res_NotLogicOP_78 && ! (argom16 == true));
    res_AndLogicOP_75 = (res_AndLogicOP_75 && res_NotLogicOP_78);
    
    res_AndLogicOP_74 = (res_AndLogicOP_74 && res_AndLogicOP_75);
    res_AndLogicOP_74 = (res_AndLogicOP_74 && (Counter_GetValore(L_P1__GetMainc47(my_id)) < 113u));
    
    res_AndLogicOP_73 = (res_AndLogicOP_73 && res_AndLogicOP_74);
    bool res_NotLogicOP_79 = true;
    res_NotLogicOP_79 = (res_NotLogicOP_79 && ! (L_P1__GetInMainc6(my_id) == rossogiallo1));
    res_AndLogicOP_73 = (res_AndLogicOP_73 && res_NotLogicOP_79);
    
    res_OrLogicOP_71 = (res_OrLogicOP_71 || res_AndLogicOP_73);
    
    res_OrLogicOP_70 = (res_OrLogicOP_70 || res_OrLogicOP_71);
    bool res_NotLogicOP_80 = true;
    res_NotLogicOP_80 = (res_NotLogicOP_80 && ! (L_P1__GetInMainc7(my_id) == verde));
    res_OrLogicOP_70 = (res_OrLogicOP_70 || res_NotLogicOP_80);
    
    res_OrLogicOP_41 = (res_OrLogicOP_41 || res_OrLogicOP_70);
    
    res_ImpliesLogicOp_34 = (res_ImpliesLogicOp_34 && res_OrLogicOP_41);
    }
    res_OrLogicOP_33 = (res_OrLogicOP_33 || res_ImpliesLogicOp_34);
    bool res_OrLogicOP_81 = false;
    bool res_OrLogicOP_82 = false;
    bool res_OrLogicOP_83 = false;
    bool res_AndLogicOP_84 = true;
    bool res_AndLogicOP_85 = true;
    bool res_NotLogicOP_86 = true;
    res_NotLogicOP_86 = (res_NotLogicOP_86 && ! (L_P1__GetInMainc6(my_id) == rossogiallo1));
    res_AndLogicOP_85 = (res_AndLogicOP_85 && res_NotLogicOP_86);
    bool res_NotLogicOP_87 = true;
    res_NotLogicOP_87 = (res_NotLogicOP_87 && ! Timer_Scaduto(L_P1__GetMainc44(my_id)));
    res_AndLogicOP_85 = (res_AndLogicOP_85 && res_NotLogicOP_87);
    
    res_AndLogicOP_84 = (res_AndLogicOP_84 && res_AndLogicOP_85);
    res_AndLogicOP_84 = (res_AndLogicOP_84 && Timer_Disattivo(L_P1__GetMainc44(my_id)));
    
    res_OrLogicOP_83 = (res_OrLogicOP_83 || res_AndLogicOP_84);
    res_OrLogicOP_83 = (res_OrLogicOP_83 || Timer_Scaduto(L_P1__GetMainc44(my_id)));
    
    res_OrLogicOP_82 = (res_OrLogicOP_82 || res_OrLogicOP_83);
    bool res_NotLogicOP_88 = true;
    bool res_NotLogicOP_89 = true;
    res_NotLogicOP_89 = (res_NotLogicOP_89 && ! (L_P1__GetInMainc6(my_id) == rossogiallo1));
    res_NotLogicOP_88 = (res_NotLogicOP_88 && ! res_NotLogicOP_89);
    res_OrLogicOP_82 = (res_OrLogicOP_82 || res_NotLogicOP_88);
    
    res_OrLogicOP_81 = (res_OrLogicOP_81 || res_OrLogicOP_82);
    bool res_NotLogicOP_90 = true;
    res_NotLogicOP_90 = (res_NotLogicOP_90 && ! (L_P1__GetParamMainc10(my_id) == verde));
    res_OrLogicOP_81 = (res_OrLogicOP_81 || res_NotLogicOP_90);
    
    res_OrLogicOP_33 = (res_OrLogicOP_33 || res_OrLogicOP_81);
    
    res_ImpliesLogicOp_24 = (res_ImpliesLogicOp_24 && res_OrLogicOP_33);
    }
    res_OrLogicOP_23 = (res_OrLogicOP_23 || res_ImpliesLogicOp_24);
    bool res_OrLogicOP_91 = false;
    bool res_NotLogicOP_92 = true;
    res_NotLogicOP_92 = (res_NotLogicOP_92 && ! (L_P1__GetMainc35(my_id) < 6u));
    res_OrLogicOP_91 = (res_OrLogicOP_91 || res_NotLogicOP_92);
    bool res_NotLogicOP_93 = true;
    res_NotLogicOP_93 = (res_NotLogicOP_93 && ! (argom16 == true));
    res_OrLogicOP_91 = (res_OrLogicOP_91 || res_NotLogicOP_93);
    
    res_OrLogicOP_23 = (res_OrLogicOP_23 || res_OrLogicOP_91);
    
    res_ImpliesLogicOp_19 = (res_ImpliesLogicOp_19 && res_OrLogicOP_23);
    }
    if(res_ImpliesLogicOp_19){
    xorIndex_res_XorLogicOP_18 = (xorIndex_res_XorLogicOP_18 + 1);
    }
    bool res_OrLogicOP_94 = false;
    res_OrLogicOP_94 = (res_OrLogicOP_94 || (argom17 == verde));
    bool res_AndLogicOP_95 = true;
    bool res_AndLogicOP_96 = true;
    res_AndLogicOP_96 = (res_AndLogicOP_96 && Timer_Attivo(L_P1__GetMainc45(my_id)));
    bool res_NotLogicOP_97 = true;
    res_NotLogicOP_97 = (res_NotLogicOP_97 && ! (argom19 == true));
    res_AndLogicOP_96 = (res_AndLogicOP_96 && res_NotLogicOP_97);
    
    res_AndLogicOP_95 = (res_AndLogicOP_95 && res_AndLogicOP_96);
    bool res_NotLogicOP_98 = true;
    res_NotLogicOP_98 = (res_NotLogicOP_98 && ! (argom15 == true));
    res_AndLogicOP_95 = (res_AndLogicOP_95 && res_NotLogicOP_98);
    
    res_OrLogicOP_94 = (res_OrLogicOP_94 || res_AndLogicOP_95);
    
    if(res_OrLogicOP_94){
    xorIndex_res_XorLogicOP_18 = (xorIndex_res_XorLogicOP_18 + 1);
    }
    
    res_XorLogicOP_18 = (res_XorLogicOP_18 && (xorIndex_res_XorLogicOP_18 == 1));
    res_ImpliesLogicOp_11 = (res_ImpliesLogicOp_11 && res_XorLogicOP_18);
    }
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_ImpliesLogicOp_11);
    bool res_OrLogicOP_99 = false;
    bool res_OrLogicOP_100 = false;
    bool res_OrLogicOP_101 = false;
    bool res_NotLogicOP_102 = true;
    bool res_NotLogicOP_103 = true;
    res_NotLogicOP_103 = (res_NotLogicOP_103 && ! (Counter_GetValore(L_P1__GetMainc47(my_id)) == 14u));
    res_NotLogicOP_102 = (res_NotLogicOP_102 && ! res_NotLogicOP_103);
    res_OrLogicOP_101 = (res_OrLogicOP_101 || res_NotLogicOP_102);
    bool res_NotLogicOP_104 = true;
    res_NotLogicOP_104 = (res_NotLogicOP_104 && ! (argom16 == false));
    res_OrLogicOP_101 = (res_OrLogicOP_101 || res_NotLogicOP_104);
    
    res_OrLogicOP_100 = (res_OrLogicOP_100 || res_OrLogicOP_101);
    bool res_AndLogicOP_105 = true;
    bool res_NotLogicOP_106 = true;
    res_NotLogicOP_106 = (res_NotLogicOP_106 && ! (L_P1__GetInMainc7(my_id) == verde));
    res_AndLogicOP_105 = (res_AndLogicOP_105 && res_NotLogicOP_106);
    bool res_NotLogicOP_107 = true;
    res_NotLogicOP_107 = (res_NotLogicOP_107 && ! (L_P1__GetMainc34(my_id) == c270x));
    res_AndLogicOP_105 = (res_AndLogicOP_105 && res_NotLogicOP_107);
    
    res_OrLogicOP_100 = (res_OrLogicOP_100 || res_AndLogicOP_105);
    
    res_OrLogicOP_99 = (res_OrLogicOP_99 || res_OrLogicOP_100);
    bool res_AndLogicOP_108 = true;
    bool res_NotLogicOP_109 = true;
    bool res_NotLogicOP_110 = true;
    res_NotLogicOP_110 = (res_NotLogicOP_110 && ! (argom15 == false));
    res_NotLogicOP_109 = (res_NotLogicOP_109 && ! res_NotLogicOP_110);
    res_AndLogicOP_108 = (res_AndLogicOP_108 && res_NotLogicOP_109);
    bool res_NotLogicOP_111 = true;
    res_NotLogicOP_111 = (res_NotLogicOP_111 && ! Timer_Scaduto(L_P1__GetMainc46(my_id)));
    res_AndLogicOP_108 = (res_AndLogicOP_108 && res_NotLogicOP_111);
    
    res_OrLogicOP_99 = (res_OrLogicOP_99 || res_AndLogicOP_108);
    
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_OrLogicOP_99);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_AndLogicOP_10);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *48,50,51,52,*  *,*  il controllo MainClass_C1_controllo_C5 non sia  diverso da  True 
    //   *104,* o  che   l'argomento argomento_ave8 non  sia  diverso da  False  *,* 
    //   *104,* o  che  *,*  il contatore MainClass_C1_contatore_Co4 non sia  maggiore di  *54,* 1121
    //   *104,* o  che  *35,*  il controllo MainClass_C1_controllo_C2 sia  uguale a Verde
    //   *104,* e  che   l'argomento argomento_ave4 sia  diverso da  False  *39,* 
    //   *104,* o  che  *,*  la variabile MainClass_C1_variabile_V5 sia  uguale a c270x
    bool res_OrLogicOP_112 = false;
    bool res_OrLogicOP_113 = false;
    bool res_OrLogicOP_114 = false;
    bool res_OrLogicOP_115 = false;
    bool res_NotLogicOP_116 = true;
    bool res_NotLogicOP_117 = true;
    res_NotLogicOP_117 = (res_NotLogicOP_117 && ! (L_P1__GetInMainc8(my_id) == true));
    res_NotLogicOP_116 = (res_NotLogicOP_116 && ! res_NotLogicOP_117);
    res_OrLogicOP_115 = (res_OrLogicOP_115 || res_NotLogicOP_116);
    bool res_NotLogicOP_118 = true;
    bool res_NotLogicOP_119 = true;
    res_NotLogicOP_119 = (res_NotLogicOP_119 && ! (argom19 == false));
    res_NotLogicOP_118 = (res_NotLogicOP_118 && ! res_NotLogicOP_119);
    res_OrLogicOP_115 = (res_OrLogicOP_115 || res_NotLogicOP_118);
    
    res_OrLogicOP_114 = (res_OrLogicOP_114 || res_OrLogicOP_115);
    bool res_NotLogicOP_120 = true;
    res_NotLogicOP_120 = (res_NotLogicOP_120 && ! (Counter_GetValore(L_P1__GetMainc48(my_id)) > 1121u));
    res_OrLogicOP_114 = (res_OrLogicOP_114 || res_NotLogicOP_120);
    
    res_OrLogicOP_113 = (res_OrLogicOP_113 || res_OrLogicOP_114);
    bool res_AndLogicOP_121 = true;
    res_AndLogicOP_121 = (res_AndLogicOP_121 && (L_P1__GetInMainc7(my_id) == verde));
    bool res_NotLogicOP_122 = true;
    res_NotLogicOP_122 = (res_NotLogicOP_122 && ! (argom16 == false));
    res_AndLogicOP_121 = (res_AndLogicOP_121 && res_NotLogicOP_122);
    
    res_OrLogicOP_113 = (res_OrLogicOP_113 || res_AndLogicOP_121);
    
    res_OrLogicOP_112 = (res_OrLogicOP_112 || res_OrLogicOP_113);
    res_OrLogicOP_112 = (res_OrLogicOP_112 || (L_P1__GetMainc34(my_id) == c270x));
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_112);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
    
    { commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  uguale a  commento: {53,} 4 commento: {34,} e  se il parametro MainClass_C1_parametro_P8 è  diverso da RossoGialloVerde o  se l'argomento argomento_ave8 è  uguale a  False  commento: {39,} , Verifica che   commento: {49,}  commento: {,}  il timer MainClass_C1_timer_T2 non sia attivo
    
    
    }
*/
bool L_P1__Macro7(instance_id_t const my_id , C1_Enumerat1 argom20, bool argom21, bool argom22)
{
bool res_AndLogicOP_0 = true;
    
    //  *109,*  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  uguale a  *53,* 4 *34,* e  se il parametro MainClass_C1_parametro_P8 è  diverso da RossoGialloVerde o  se l'argomento argomento_ave8 è  uguale a  False  *39,* , Verifica che   *49,*  *,*  il timer MainClass_C1_timer_T2 non sia attivo
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_AndLogicOP_3 = true;
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (L_P1__GetMainc31(my_id) == 4u));
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetParamMainc11(my_id) == rossogiallo));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_4);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_3);
    res_OrLogicOP_2 = (res_OrLogicOP_2 || (argom22 == false));
    
    if(res_OrLogicOP_2){
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! Timer_Attivo(L_P1__GetMainc44(my_id)));
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_NotLogicOP_5);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
     
    { commento: {63,}  se la macro  MainClass_C1_macrova_M4 ( con argomento_a10   uguale a Verde ,argomento_a5   uguale a GialloVerde ,argomento_a6   uguale a c270x ,argomento_a1   uguale a c270x ,argomento_a7   uguale a RossoGialloxVerdex  e argomento_a9   uguale a GialloVerde )   è  diverso da  False  commento: {40,}  commento: {34,} o  se il parametro MainClass_C1_parametro_P8 non è  diverso da RossoGialloVerde e  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} e  se il timer MainClass_C1_timer_T2 è attivo, Solo una delle seguenti { 
     commento: {38,}  se il contatore MainClass_C1_contatore_Co2 non è  maggiore di  commento: {54,} 15 o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   commento: {48,49,50,}   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V8 non sia  uguale a  commento: {53,} 4
     commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T2 sia attivo
     commento: {104,} o  che  commento: {37,}  la variabile MainClass_C1_variabile_V8 sia  minore di  commento: {55,} 9
    
    
     } Verifica che   commento: {48,49,50,51,}  commento: {,}  la variabile MainClass_C1_variabile_V8 sia  minore di  commento: {55,} 8
     commento: {104,} e  che  commento: {37,}  la variabile MainClass_C1_variabile_V8 non sia  uguale a  commento: {53,} 5
     commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co2 sia  diverso da  commento: {56,} 11
     commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T6 non sia disattivo
     commento: {104,} o  che  commento: {38,}  il contatore MainClass_C1_contatore_Co4 non sia  minore di  commento: {55,} 120
     commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C5 non sia  uguale a  True 
    
    
    }
*/
bool L_P1__Macro8(instance_id_t const my_id )
{
bool res_AndLogicOP_0 = true;
    
    //  *63,*  se la macro  MainClass_C1_macrova_M4 ( con argomento_a10   uguale a Verde ,argomento_a5   uguale a GialloVerde ,argomento_a6   uguale a c270x ,argomento_a1   uguale a c270x ,argomento_a7   uguale a RossoGialloxVerdex  e argomento_a9   uguale a GialloVerde )   è  diverso da  False  *40,*  *34,* o  se il parametro MainClass_C1_parametro_P8 non è  diverso da RossoGialloVerde e  se il controllo ConsDef  è  uguale a FALSE  *36,* e  se il timer MainClass_C1_timer_T2 è attivo, Solo una delle seguenti { 
    //   *38,*  se il contatore MainClass_C1_contatore_Co2 non è  maggiore di  *54,* 15 o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   *48,49,50,*   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* e  che   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* o  che  *,*  la variabile MainClass_C1_variabile_V8 non sia  uguale a  *53,* 4
    //   *104,* e  che   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* e  che  *,*  il timer MainClass_C1_timer_T2 sia attivo
    //   *104,* o  che  *37,*  la variabile MainClass_C1_variabile_V8 sia  minore di  *55,* 9
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__Macro4(my_id,c270x,verde,gialloverde,c270x,rossogiallo1,gialloverde) == false));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_3);
    bool res_AndLogicOP_4 = true;
    bool res_AndLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetParamMainc11(my_id) == rossogiallo));
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! res_NotLogicOP_7);
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_6);
    res_AndLogicOP_5 = (res_AndLogicOP_5 && (L_P1__GetInConsd(my_id) == false));
    
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_AndLogicOP_5);
    res_AndLogicOP_4 = (res_AndLogicOP_4 && Timer_Attivo(L_P1__GetMainc44(my_id)));
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_4);
    
    if(res_OrLogicOP_2){
    bool res_ImpliesLogicOp_8 = true;
    bool res_OrLogicOP_9 = false;
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (Counter_GetValore(L_P1__GetMainc47(my_id)) > 15u));
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_NotLogicOP_10);
    res_OrLogicOP_9 = (res_OrLogicOP_9 || (L_P1__GetInConsd(my_id) == false));
    
    if(res_OrLogicOP_9){
    bool res_OrLogicOP_11 = false;
    bool res_OrLogicOP_12 = false;
    bool res_AndLogicOP_13 = true;
    res_AndLogicOP_13 = (res_AndLogicOP_13 && (L_P1__GetInConsd(my_id) == false));
    res_AndLogicOP_13 = (res_AndLogicOP_13 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_AndLogicOP_13);
    bool res_AndLogicOP_14 = true;
    bool res_AndLogicOP_15 = true;
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (L_P1__GetMainc35(my_id) == 4u));
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_NotLogicOP_16);
    res_AndLogicOP_15 = (res_AndLogicOP_15 && (L_P1__GetInConsd(my_id) == false));
    
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_AndLogicOP_15);
    res_AndLogicOP_14 = (res_AndLogicOP_14 && Timer_Attivo(L_P1__GetMainc44(my_id)));
    
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_AndLogicOP_14);
    
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_OrLogicOP_12);
    res_OrLogicOP_11 = (res_OrLogicOP_11 || (L_P1__GetMainc35(my_id) < 9u));
    
    res_ImpliesLogicOp_8 = (res_ImpliesLogicOp_8 && res_OrLogicOP_11);
    }
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_ImpliesLogicOp_8);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *48,49,50,51,*  *,*  la variabile MainClass_C1_variabile_V8 sia  minore di  *55,* 8
    //   *104,* e  che  *37,*  la variabile MainClass_C1_variabile_V8 non sia  uguale a  *53,* 5
    //   *104,* e  che  *,*  il contatore MainClass_C1_contatore_Co2 sia  diverso da  *56,* 11
    //   *104,* e  che  *,*  il timer MainClass_C1_timer_T6 non sia disattivo
    //   *104,* o  che  *38,*  il contatore MainClass_C1_contatore_Co4 non sia  minore di  *55,* 120
    //   *104,* e  che  *,*  il controllo MainClass_C1_controllo_C5 non sia  uguale a  True
    bool res_OrLogicOP_17 = false;
    bool res_AndLogicOP_18 = true;
    bool res_AndLogicOP_19 = true;
    bool res_AndLogicOP_20 = true;
    res_AndLogicOP_20 = (res_AndLogicOP_20 && (L_P1__GetMainc35(my_id) < 8u));
    bool res_NotLogicOP_21 = true;
    res_NotLogicOP_21 = (res_NotLogicOP_21 && ! (L_P1__GetMainc35(my_id) == 5u));
    res_AndLogicOP_20 = (res_AndLogicOP_20 && res_NotLogicOP_21);
    
    res_AndLogicOP_19 = (res_AndLogicOP_19 && res_AndLogicOP_20);
    bool res_NotLogicOP_22 = true;
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! (Counter_GetValore(L_P1__GetMainc47(my_id)) == 11u));
    res_AndLogicOP_19 = (res_AndLogicOP_19 && res_NotLogicOP_22);
    
    res_AndLogicOP_18 = (res_AndLogicOP_18 && res_AndLogicOP_19);
    bool res_NotLogicOP_23 = true;
    res_NotLogicOP_23 = (res_NotLogicOP_23 && ! Timer_Disattivo(L_P1__GetMainc45(my_id)));
    res_AndLogicOP_18 = (res_AndLogicOP_18 && res_NotLogicOP_23);
    
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_AndLogicOP_18);
    bool res_AndLogicOP_24 = true;
    bool res_NotLogicOP_25 = true;
    res_NotLogicOP_25 = (res_NotLogicOP_25 && ! (Counter_GetValore(L_P1__GetMainc48(my_id)) < 120u));
    res_AndLogicOP_24 = (res_AndLogicOP_24 && res_NotLogicOP_25);
    bool res_NotLogicOP_26 = true;
    res_NotLogicOP_26 = (res_NotLogicOP_26 && ! (L_P1__GetInMainc8(my_id) == true));
    res_AndLogicOP_24 = (res_AndLogicOP_24 && res_NotLogicOP_26);
    
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_AndLogicOP_24);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_17);
    
    
    
    return res_AndLogicOP_0;
}


// Macro valorizzate

/*
    CNL corrispondente:
    
    { commento: {[} commento: {35,}  se il controllo MainClass_C1_controllo_C5 non è  diverso da  True  o  se il controllo ConsDef è uguale a FALSE  e  se l'argomento argomento_a2 è  diverso da RossoGialloVerde commento: {39,}  , assegna alla macro il valore  True 
    
     commento: {46,} assegna alla macro il valore  True  commento: {],}
    }
*/
bool L_P1__Macro3(instance_id_t const my_id , C1_Enumerat4 argom, C1_Enumerat3 argom1, C1_Enumerat1 argom2, C1_Enumerat3 argom3, C1_Enumerat3 argom4)
{
bool res_macro_val;
    
    //  *[* *35,*  se il controllo MainClass_C1_controllo_C5 non è  diverso da  True  o  se il controllo ConsDef è uguale a FALSE  e  se l'argomento argomento_a2 è  diverso da RossoGialloVerde
    bool res_OrLogicOP_0 = false;
    bool res_NotLogicOP_1 = true;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (L_P1__GetInMainc8(my_id) == true));
    res_NotLogicOP_1 = (res_NotLogicOP_1 && ! res_NotLogicOP_2);
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_1);
    bool res_AndLogicOP_3 = true;
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (argom2 == rossogiallo));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_4);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_3);
    
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
     commento: {46,} assegna alla macro il valore  True  commento: {],}
    }
*/
bool L_P1__Macro4(instance_id_t const my_id , C1_Enumerat4 argom5, C1_Enumerat3 argom6, C1_Enumerat2 argom7, C1_Enumerat4 argom8, C1_Enumerat2 argom9, C1_Enumerat2 argom10)
{
return true;
}

/*
    CNL corrispondente:
    
    { commento: {[}
     commento: {46,} assegna alla macro il valore  False  commento: {],}
    }
*/
bool L_P1__Macro5(instance_id_t const my_id , C1_Enumerat3 argom11, C1_Enumerat2 argom12)
{
return false;
}



