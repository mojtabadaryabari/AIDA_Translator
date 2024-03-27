// Codice del modello 'TestCase13', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
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
    
     commento: {84,}  Ricezione del comando   MainClass_C1_command_comm3( con argomento_ave2   ,argomento_ave8    e argomento_ave9   )   commento: {78,}
    
    }
*/
static inline bool L_P1__Guard1(instance_id_t const my_id)
{
    bool res_AndLogicOP_0 = true;
    
    //  comando   MainClass_C1_command_comm3( con argomento_ave2   ,argomento_ave8    e argomento_ave9   )
    res_AndLogicOP_0 = (res_AndLogicOP_0 && L_P1__GetCAEvent(my_id));
    
    if(res_AndLogicOP_0){
    L_P1__SetCAEvent(my_id,false);
    }
    else{
    
    }
    
    
    return res_AndLogicOP_0;
}


/*
    CNL corrispondente:
     {  commento: {69,}  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} o  se il contatore MainClass_C1_contatore_Co9 è  diverso da  commento: {56,} 13204 commento: {36,} e  se il timer MainClass_C1_timer_T8 è disattivo commento: {36,} o  se il timer MainClass_C1_timer_T8 non è disattivo e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
     commento: {68,} commento: {35,}  se il controllo MainClass_C1_controllo_C6 è  diverso da  False  commento: {34,} o  se il parametro MainClass_C1_parametro_P8 non è  diverso da Verde commento: {38,} e  se il contatore MainClass_C1_contatore_Co5 non è  maggiore di  commento: {54,} 1435 commento: {37,} o  se la variabile MainClass_C1_variabile_V1 è  diverso da  False , Almeno una delle seguenti { 
     commento: {68,} commento: {36,}  se il timer MainClass_C1_timer_T8 è attivo commento: {36,} e  se il timer MainClass_C1_timer_T8 è scaduto commento: {38,} o  se il contatore MainClass_C1_contatore_Co9 non è  uguale a  commento: {53,} 13 commento: {36,} o  se il timer MainClass_C1_timer_T8 non è attivo commento: {36,} o  se il timer MainClass_C1_timer_T8 è scaduto commento: {36,} o  se il timer MainClass_C1_timer_T8 non è attivo, Almeno una delle seguenti { 
     commento: {38,}  se il contatore MainClass_C1_contatore_Co9 non è  minore di  commento: {55,} 14 commento: {35,} o  se il controllo MainClass_C1_controllo_C6 è  diverso da  False  commento: {38,} o  se il contatore MainClass_C1_contatore_Co5 non è  maggiore di  commento: {54,} 141, Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
    
    
     } Verifica che   commento: {51,}  commento: {,}  il contatore MainClass_C1_contatore_Co9 non sia  diverso da  commento: {56,} 15204
    
    
     } Verifica che   commento: {48,}  commento: {,}  il controllo MainClass_C1_controllo_C10 non sia  diverso da c270
    
    
     } Verifica che   commento: {48,}  commento: {,}  il controllo MainClass_C1_controllo_C5 non sia  uguale a  False 
    
     }
*/
static inline bool L_P1__Guard2(instance_id_t const my_id)
{
    bool res_AndLogicOP_0 = true;
    
    //  *69,*  se il controllo ConsDef  è  uguale a FALSE  *38,* o  se il contatore MainClass_C1_contatore_Co9 è  diverso da  *56,* 13204 *36,* e  se il timer MainClass_C1_timer_T8 è disattivo *36,* o  se il timer MainClass_C1_timer_T8 non è disattivo e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
    //   *68,* *35,*  se il controllo MainClass_C1_controllo_C6 è  diverso da  False  *34,* o  se il parametro MainClass_C1_parametro_P8 non è  diverso da Verde *38,* e  se il contatore MainClass_C1_contatore_Co5 non è  maggiore di  *54,* 1435 *37,* o  se la variabile MainClass_C1_variabile_V1 è  diverso da  False , Almeno una delle seguenti { 
    //   *68,* *36,*  se il timer MainClass_C1_timer_T8 è attivo *36,* e  se il timer MainClass_C1_timer_T8 è scaduto *38,* o  se il contatore MainClass_C1_contatore_Co9 non è  uguale a  *53,* 13 *36,* o  se il timer MainClass_C1_timer_T8 non è attivo *36,* o  se il timer MainClass_C1_timer_T8 è scaduto *36,* o  se il timer MainClass_C1_timer_T8 non è attivo, Almeno una delle seguenti { 
    //   *38,*  se il contatore MainClass_C1_contatore_Co9 non è  minore di  *55,* 14 *35,* o  se il controllo MainClass_C1_controllo_C6 è  diverso da  False  *38,* o  se il contatore MainClass_C1_contatore_Co5 non è  maggiore di  *54,* 141, Verifica che   *48,*   il controllo ConsDef  sia  uguale a FALSE 
    //   } Verifica che   *51,*  *,*  il contatore MainClass_C1_contatore_Co9 non sia  diverso da  *56,* 15204
    //   } Verifica che   *48,*  *,*  il controllo MainClass_C1_controllo_C10 non sia  diverso da c270
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    res_OrLogicOP_3 = (res_OrLogicOP_3 || (L_P1__GetInConsd(my_id) == false));
    bool res_AndLogicOP_4 = true;
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (Counter_GetValore(L_P1__GetMainc32(my_id)) == 13204u));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_5);
    res_AndLogicOP_4 = (res_AndLogicOP_4 && Timer_Disattivo(L_P1__GetMainc30(my_id)));
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_AndLogicOP_4);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    bool res_AndLogicOP_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! Timer_Disattivo(L_P1__GetMainc30(my_id)));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_7);
    res_AndLogicOP_6 = (res_AndLogicOP_6 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_6);
    
    if(res_OrLogicOP_2){
    bool res_XorLogicOP_8 = true;
    int xorIndex_res_XorLogicOP_8 = 0;
    bool res_ImpliesLogicOp_9 = true;
    bool res_OrLogicOP_10 = false;
    bool res_OrLogicOP_11 = false;
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (L_P1__GetInMainc7(my_id) == false));
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_NotLogicOP_12);
    bool res_AndLogicOP_13 = true;
    bool res_NotLogicOP_14 = true;
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (L_P1__GetParamMainc11(my_id) == verde));
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! res_NotLogicOP_15);
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_NotLogicOP_14);
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (Counter_GetValore(L_P1__GetMainc31(my_id)) > 1435u));
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_NotLogicOP_16);
    
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_AndLogicOP_13);
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_OrLogicOP_11);
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! (L_P1__GetMainc24(my_id) == false));
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_NotLogicOP_17);
    
    if(res_OrLogicOP_10){
    bool res_OrLogicOP_18 = false;
    bool res_ImpliesLogicOp_19 = true;
    bool res_OrLogicOP_20 = false;
    bool res_OrLogicOP_21 = false;
    bool res_OrLogicOP_22 = false;
    bool res_OrLogicOP_23 = false;
    bool res_AndLogicOP_24 = true;
    res_AndLogicOP_24 = (res_AndLogicOP_24 && Timer_Attivo(L_P1__GetMainc30(my_id)));
    res_AndLogicOP_24 = (res_AndLogicOP_24 && Timer_Scaduto(L_P1__GetMainc30(my_id)));
    
    res_OrLogicOP_23 = (res_OrLogicOP_23 || res_AndLogicOP_24);
    bool res_NotLogicOP_25 = true;
    res_NotLogicOP_25 = (res_NotLogicOP_25 && ! (Counter_GetValore(L_P1__GetMainc32(my_id)) == 13u));
    res_OrLogicOP_23 = (res_OrLogicOP_23 || res_NotLogicOP_25);
    
    res_OrLogicOP_22 = (res_OrLogicOP_22 || res_OrLogicOP_23);
    bool res_NotLogicOP_26 = true;
    res_NotLogicOP_26 = (res_NotLogicOP_26 && ! Timer_Attivo(L_P1__GetMainc30(my_id)));
    res_OrLogicOP_22 = (res_OrLogicOP_22 || res_NotLogicOP_26);
    
    res_OrLogicOP_21 = (res_OrLogicOP_21 || res_OrLogicOP_22);
    res_OrLogicOP_21 = (res_OrLogicOP_21 || Timer_Scaduto(L_P1__GetMainc30(my_id)));
    
    res_OrLogicOP_20 = (res_OrLogicOP_20 || res_OrLogicOP_21);
    bool res_NotLogicOP_27 = true;
    res_NotLogicOP_27 = (res_NotLogicOP_27 && ! Timer_Attivo(L_P1__GetMainc30(my_id)));
    res_OrLogicOP_20 = (res_OrLogicOP_20 || res_NotLogicOP_27);
    
    if(res_OrLogicOP_20){
    bool res_ImpliesLogicOp_28 = true;
    bool res_OrLogicOP_29 = false;
    bool res_OrLogicOP_30 = false;
    bool res_NotLogicOP_31 = true;
    res_NotLogicOP_31 = (res_NotLogicOP_31 && ! (Counter_GetValore(L_P1__GetMainc32(my_id)) < 14u));
    res_OrLogicOP_30 = (res_OrLogicOP_30 || res_NotLogicOP_31);
    bool res_NotLogicOP_32 = true;
    res_NotLogicOP_32 = (res_NotLogicOP_32 && ! (L_P1__GetInMainc7(my_id) == false));
    res_OrLogicOP_30 = (res_OrLogicOP_30 || res_NotLogicOP_32);
    
    res_OrLogicOP_29 = (res_OrLogicOP_29 || res_OrLogicOP_30);
    bool res_NotLogicOP_33 = true;
    res_NotLogicOP_33 = (res_NotLogicOP_33 && ! (Counter_GetValore(L_P1__GetMainc31(my_id)) > 141u));
    res_OrLogicOP_29 = (res_OrLogicOP_29 || res_NotLogicOP_33);
    
    if(res_OrLogicOP_29){
    res_ImpliesLogicOp_28 = (res_ImpliesLogicOp_28 && (L_P1__GetInConsd(my_id) == false));
    }
    res_ImpliesLogicOp_19 = (res_ImpliesLogicOp_19 && res_ImpliesLogicOp_28);
    }
    res_OrLogicOP_18 = (res_OrLogicOP_18 || res_ImpliesLogicOp_19);
    bool res_NotLogicOP_34 = true;
    bool res_NotLogicOP_35 = true;
    res_NotLogicOP_35 = (res_NotLogicOP_35 && ! (Counter_GetValore(L_P1__GetMainc32(my_id)) == 15204u));
    res_NotLogicOP_34 = (res_NotLogicOP_34 && ! res_NotLogicOP_35);
    res_OrLogicOP_18 = (res_OrLogicOP_18 || res_NotLogicOP_34);
    
    res_ImpliesLogicOp_9 = (res_ImpliesLogicOp_9 && res_OrLogicOP_18);
    }
    if(res_ImpliesLogicOp_9){
    xorIndex_res_XorLogicOP_8 = (xorIndex_res_XorLogicOP_8 + 1);
    }
    bool res_NotLogicOP_36 = true;
    bool res_NotLogicOP_37 = true;
    res_NotLogicOP_37 = (res_NotLogicOP_37 && ! (L_P1__GetInMainc4(my_id) == c270));
    res_NotLogicOP_36 = (res_NotLogicOP_36 && ! res_NotLogicOP_37);
    if(res_NotLogicOP_36){
    xorIndex_res_XorLogicOP_8 = (xorIndex_res_XorLogicOP_8 + 1);
    }
    
    res_XorLogicOP_8 = (res_XorLogicOP_8 && (xorIndex_res_XorLogicOP_8 == 1));
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_XorLogicOP_8);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *48,*  *,*  il controllo MainClass_C1_controllo_C5 non sia  uguale a  False
    bool res_NotLogicOP_38 = true;
    res_NotLogicOP_38 = (res_NotLogicOP_38 && ! (L_P1__GetInMainc6(my_id) == false));
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_NotLogicOP_38);
    
    
    
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
    
      se la macro  MainClass_C1_macrova_M10 ( con argomento_a7   uguale a True  e argomento_a10   uguale a spento )  non  è  diverso da  True  commento: {40,}  commento: {38,} o  se il contatore MainClass_C1_contatore_Co9 è  maggiore di  commento: {54,} 122, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V8 il valore 1
    
     ,altrimenti  commento: {69,}Disattiva il timer MainClass_C1_timer_T8
    
    
      se il ripristino dello stato  è  diverso da  commento: {56,}  state1  commento: {107,} commento: {35,} o  se il controllo MainClass_C1_controllo_C7 è  uguale a c270 commento: {34,} o  se il parametro MainClass_C1_parametro_P8 non è  uguale a Verde commento: {34,} e  se il parametro MainClass_C1_parametro_P8 è  uguale a Verde commento: {38,} e  se il contatore MainClass_C1_contatore_Co5 è  uguale a  commento: {53,} 14 e  se il controllo ConsDef  è  uguale a FALSE , commento: {67,} Assegna alla variabile MainClass_C1_variabile_V1 il valore  True 
    
     ,altrimenti  commento: {69,}Disattiva il timer MainClass_C1_timer_T8
    
    
    
    }
*/
static inline void L_P1__Effec1(instance_id_t const my_id)
{
    
    //  se la macro  MainClass_C1_macrova_M10 ( con argomento_a7   uguale a True  e argomento_a10   uguale a spento )  non  è  diverso da  True  *40,*  *38,* o  se il contatore MainClass_C1_contatore_Co9 è  maggiore di  *54,* 122, *67,* Assegna alla variabile MainClass_C1_variabile_V8 il valore 1
    //   ,altrimenti  *69,*Disattiva il timer MainClass_C1_timer_T8
    bool res_OrLogicOP_0 = false;
    bool res_NotLogicOP_1 = true;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (L_P1__Macro3(my_id,spento,true) == true));
    res_NotLogicOP_1 = (res_NotLogicOP_1 && ! res_NotLogicOP_2);
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_1);
    res_OrLogicOP_0 = (res_OrLogicOP_0 || (Counter_GetValore(L_P1__GetMainc32(my_id)) > 122u));
    
    if(res_OrLogicOP_0){
    
    L_P1__SetMainc27(my_id,1u);
    }else{
    
    Timer_Disattiva(L_P1__GetMainc30(my_id));
    }
    
    //  se il ripristino dello stato  è  diverso da  *56,*  state1  *107,* *35,* o  se il controllo MainClass_C1_controllo_C7 è  uguale a c270 *34,* o  se il parametro MainClass_C1_parametro_P8 non è  uguale a Verde *34,* e  se il parametro MainClass_C1_parametro_P8 è  uguale a Verde *38,* e  se il contatore MainClass_C1_contatore_Co5 è  uguale a  *53,* 14 e  se il controllo ConsDef  è  uguale a FALSE , *67,* Assegna alla variabile MainClass_C1_variabile_V1 il valore  True 
    //   ,altrimenti  *69,*Disattiva il timer MainClass_C1_timer_T8
    bool res_OrLogicOP_3 = false;
    bool res_OrLogicOP_4 = false;
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetStato1(my_id) == C1_St_state));
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_NotLogicOP_5);
    res_OrLogicOP_4 = (res_OrLogicOP_4 || (L_P1__GetInMainc8(my_id) == c270));
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_OrLogicOP_4);
    bool res_AndLogicOP_6 = true;
    bool res_AndLogicOP_7 = true;
    bool res_AndLogicOP_8 = true;
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetParamMainc11(my_id) == verde));
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_9);
    res_AndLogicOP_8 = (res_AndLogicOP_8 && (L_P1__GetParamMainc11(my_id) == verde));
    
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_AndLogicOP_8);
    res_AndLogicOP_7 = (res_AndLogicOP_7 && (Counter_GetValore(L_P1__GetMainc31(my_id)) == 14u));
    
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_AndLogicOP_7);
    res_AndLogicOP_6 = (res_AndLogicOP_6 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_AndLogicOP_6);
    
    if(res_OrLogicOP_3){
    
    L_P1__SetMainc24(my_id,true);
    }else{
    
    Timer_Disattiva(L_P1__GetMainc30(my_id));
    }
}


/*
    CNL corrispondente:
     { commento: {37,}  se la variabile MainClass_C1_variabile_V8 non è  maggiore di  commento: {54,} 5 commento: {37,} e  se la variabile MainClass_C1_variabile_V2 non è  diverso da c270 o  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} e  se il timer MainClass_C1_timer_T8 è disattivo,  Applica gli effetti
           della macro MainClass_C1_macroef_M7   commento: {73,}
    
     ,altrimenti  commento: {71,}Decrementa il contatore MainClass_C1_contatore_Co5
    
    
     commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è disattivo e  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} o  se il parametro MainClass_C1_parametro_P8 non è  uguale a Verde commento: {38,} e  se il contatore MainClass_C1_contatore_Co9 è  uguale a  commento: {53,} 13 commento: {38,} e  se il contatore MainClass_C1_contatore_Co5 è  diverso da  commento: {56,} 1112, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V1 il valore  True 
    
       
     }
*/
static inline void L_P1__Effec2(instance_id_t const my_id)
{
    
    //  *37,*  se la variabile MainClass_C1_variabile_V8 non è  maggiore di  *54,* 5 *37,* e  se la variabile MainClass_C1_variabile_V2 non è  diverso da c270 o  se il controllo ConsDef  è  uguale a FALSE  *36,* e  se il timer MainClass_C1_timer_T8 è disattivo,  Applica gli effetti
    //         della macro MainClass_C1_macroef_M7   *73,*
    //   ,altrimenti  *71,*Decrementa il contatore MainClass_C1_contatore_Co5
    bool res_OrLogicOP_0 = false;
    bool res_AndLogicOP_1 = true;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (L_P1__GetMainc27(my_id) > 5u));
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_2);
    bool res_NotLogicOP_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetMainc25(my_id) == c270));
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! res_NotLogicOP_4);
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_3);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_1);
    bool res_AndLogicOP_5 = true;
    res_AndLogicOP_5 = (res_AndLogicOP_5 && (L_P1__GetInConsd(my_id) == false));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && Timer_Disattivo(L_P1__GetMainc30(my_id)));
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_5);
    
    if(res_OrLogicOP_0){
    
    L_P1__Macro1(my_id);
    }else{
    
    Counter_Decr(L_P1__GetMainc31(my_id));
    }
    
    //  *110,*  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è disattivo e  se il controllo ConsDef  è  uguale a FALSE  *34,* o  se il parametro MainClass_C1_parametro_P8 non è  uguale a Verde *38,* e  se il contatore MainClass_C1_contatore_Co9 è  uguale a  *53,* 13 *38,* e  se il contatore MainClass_C1_contatore_Co5 è  diverso da  *56,* 1112, *67,* Assegna alla variabile MainClass_C1_variabile_V1 il valore  True
    bool res_OrLogicOP_6 = false;
    bool res_AndLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! Timer_Disattivo(L_P1__GetMainc29(my_id)));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_8);
    res_AndLogicOP_7 = (res_AndLogicOP_7 && (L_P1__GetInConsd(my_id) == false));
    
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_AndLogicOP_7);
    bool res_AndLogicOP_9 = true;
    bool res_AndLogicOP_10 = true;
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (L_P1__GetParamMainc11(my_id) == verde));
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_NotLogicOP_11);
    res_AndLogicOP_10 = (res_AndLogicOP_10 && (Counter_GetValore(L_P1__GetMainc32(my_id)) == 13u));
    
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_AndLogicOP_10);
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (Counter_GetValore(L_P1__GetMainc31(my_id)) == 1112u));
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_NotLogicOP_12);
    
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_AndLogicOP_9);
    
    if(res_OrLogicOP_6){
    
    L_P1__SetMainc24(my_id,true);
    }
}



// ********** Definizione metodi **********

// Metodi standard

void L_P1_C1_Init(instance_id_t const my_id)
{
    // init variabili di stato
    L_P1__SetMainc16(my_id, rossogiallo1);
    L_P1__SetMainc18(my_id, false);
    L_P1__SetMainc20(my_id, false);
    L_P1__SetMainc22(my_id, false);
    L_P1__SetMainc23(my_id, false);
    L_P1__SetMainc24(my_id, false);
    L_P1__SetMainc25(my_id, spento);
    L_P1__SetMainc26(my_id, false);
    L_P1__SetMainc27(my_id, 0);
    L_P1__SetStato1(my_id, C1_St_Stato);
    // init controlli precedenti
    L_P1__SetMainc13(my_id, false);
    L_P1__SetMainc15(my_id, verde);
    // init Timer e Counter
    Timer_AggmInit(L_P1__GetMainc28(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc28_ID);
    Timer_Init(L_P1__GetMainc28(my_id), 20435000);
    Timer_AggmInit(L_P1__GetMainc29(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc29_ID);
    Timer_Init(L_P1__GetMainc29(my_id), 20435000);
    Timer_AggmInit(L_P1__GetMainc30(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc30_ID);
    Timer_Init(L_P1__GetMainc30(my_id), 22000);
    Counter_AggmInit(L_P1__GetMainc31(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc31_ID);
    Counter_Init(L_P1__GetMainc31(my_id));
    Counter_AggmInit(L_P1__GetMainc32(my_id), true, CLASS_L_P1_C1_ID, my_id, L_P1__mainc32_ID);
    Counter_Init(L_P1__GetMainc32(my_id));
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
    L_P1__SetMainc17(my_id, L_P1__GetMainc16(my_id));
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
            if (L_P1__Guard2(my_id)) {
                L_P1_C1_SetState(my_id, C1_St_state);
                L_P1__Effec2(my_id);				
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
            if (L_P1__Guard1(my_id)) {
                L_P1_C1_SetState(my_id, C1_St_state);
                L_P1__Effec1(my_id);				
            }
            else
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
    Timer_Exec(L_P1__GetMainc28(my_id));
    Timer_Exec(L_P1__GetMainc29(my_id));
    Timer_Exec(L_P1__GetMainc30(my_id));
}

void L_P1_C1_GSetSafe(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C1(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C1(proc_id);
    L_P1__SetOutMainc(my_id, false);
    L_P1__SetOutMainc1(my_id, true);
    L_P1__SetOutMainc2(my_id, c270);
    L_P1__SetOutMainc3(my_id, giallogiall);
}

void L_P1_C1_GUpdatePrev(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C1(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C1(proc_id);
    L_P1__SetMainc13(my_id, L_P1__GetInMainc12(my_id));
    L_P1__SetMainc15(my_id, L_P1__GetInMainc14(my_id));
    L_P1__SetMainc17(my_id, L_P1__GetMainc16(my_id));
    L_P1__SetMainc19(my_id, L_P1__GetMainc18(my_id));
    L_P1__SetMainc21(my_id, L_P1__GetMainc20(my_id));
}

// ********** Definizione macro **********

// Macro di effetto

/*
    CNL corrispondente:
    
    {  se la macro  MainClass_C1_macrova_M10 ( con argomento_a7   uguale a True  e argomento_a10   uguale a spento )  non  è  diverso da  False  commento: {40,}  o  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} e  se il timer MainClass_C1_timer_T8 non è attivo commento: {37,} o  se la variabile MainClass_C1_variabile_V1 è  diverso da  False  commento: {34,} e  se il parametro MainClass_C1_parametro_P10 è  uguale a c180, commento: {69,}Disattiva il timer MainClass_C1_timer_T8
    
     ,altrimenti   commento: {67,} Assegna alla variabile MainClass_C1_variabile_V2 il valore c270 commento: {67,}
    
    
     commento: {34,}  se lo stato  è  uguale a  commento: {53,}  state1  commento: {106,} commento: {37,} e  se la variabile MainClass_C1_variabile_V8 è  minore di  commento: {55,} 2 commento: {34,} o  se il parametro MainClass_C1_parametro_P8 non è  diverso da Verde o  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} e  se il timer MainClass_C1_timer_T8 è attivo,  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V8 il valore 3 commento: {67,}
    
     ,altrimenti  commento: {69,}Disattiva il timer MainClass_C1_timer_T8
    
    
     commento: {38,}  se il contatore MainClass_C1_contatore_Co9 non è  uguale a  commento: {53,} 141 commento: {37,} o  se la variabile MainClass_C1_variabile_V1 non è  diverso da  True  commento: {37,} o  se la variabile MainClass_C1_variabile_V1 non è  uguale a  True  commento: {35,} e  se il controllo MainClass_C1_controllo_C3 è  uguale a  True  commento: {37,} e  se la variabile MainClass_C1_variabile_V1 non è  uguale a  False  commento: {34,} o  se il parametro MainClass_C1_parametro_P8 è  diverso da Verde, commento: {71,}Decrementa il contatore MainClass_C1_contatore_Co5
    
       
     commento: {36,}  se il timer MainClass_C1_timer_T8 non è scaduto, commento: {69,}Disattiva il timer MainClass_C1_timer_T8
    
     ,altrimenti  commento: {68,}Attiva il timer MainClass_C1_timer_T8
    
    
      se la macro  MainClass_C1_macrova_M10 ( con argomento_a7   uguale a True  e argomento_a10   uguale a spento )  non  è  diverso da  True  commento: {40,}  commento: {34,} e  se il parametro MainClass_C1_parametro_P6 è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} e  se il controllo MainClass_C1_controllo_C5 non è  diverso da  False  commento: {35,} o  se il controllo MainClass_C1_controllo_C5 non è  uguale a  True , commento: {67,} Assegna alla variabile MainClass_C1_variabile_V8 il valore 7
    
     ,altrimenti  commento: {68,}Attiva il timer MainClass_C1_timer_T8
    
    
    
    }
*/
void L_P1__Macro(instance_id_t const my_id )
{
//  se la macro  MainClass_C1_macrova_M10 ( con argomento_a7   uguale a True  e argomento_a10   uguale a spento )  non  è  diverso da  False  *40,*  o  se il controllo ConsDef  è  uguale a FALSE  *36,* e  se il timer MainClass_C1_timer_T8 non è attivo *37,* o  se la variabile MainClass_C1_variabile_V1 è  diverso da  False  *34,* e  se il parametro MainClass_C1_parametro_P10 è  uguale a c180, *69,*Disattiva il timer MainClass_C1_timer_T8
    // ,altrimenti   *67,* Assegna alla variabile MainClass_C1_variabile_V2 il valore c270
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_NotLogicOP_2 = true;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__Macro3(my_id,spento,true) == false));
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! res_NotLogicOP_3);
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_NotLogicOP_2);
    bool res_AndLogicOP_4 = true;
    res_AndLogicOP_4 = (res_AndLogicOP_4 && (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! Timer_Attivo(L_P1__GetMainc30(my_id)));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_5);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_4);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_AndLogicOP_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetMainc24(my_id) == false));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_7);
    res_AndLogicOP_6 = (res_AndLogicOP_6 && (L_P1__GetParamMainc9(my_id) == c180));
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_6);
    
    if(res_OrLogicOP_0){
    
    Timer_Disattiva(L_P1__GetMainc30(my_id));
    }else{
    
    L_P1__SetMainc25(my_id,c270);
    }
    //  *67,*
    // *34,*  se lo stato  è  uguale a  *53,*  state1  *106,* *37,* e  se la variabile MainClass_C1_variabile_V8 è  minore di  *55,* 2 *34,* o  se il parametro MainClass_C1_parametro_P8 non è  diverso da Verde o  se il controllo ConsDef  è  uguale a FALSE  *36,* e  se il timer MainClass_C1_timer_T8 è attivo,  *67,* Assegna alla variabile MainClass_C1_variabile_V8 il valore 3 *67,*
    // ,altrimenti  *69,*Disattiva il timer MainClass_C1_timer_T8
    bool res_OrLogicOP_8 = false;
    bool res_OrLogicOP_9 = false;
    bool res_AndLogicOP_10 = true;
    res_AndLogicOP_10 = (res_AndLogicOP_10 && (L_P1_C1_GetState(my_id) == C1_St_state));
    res_AndLogicOP_10 = (res_AndLogicOP_10 && (L_P1__GetMainc27(my_id) < 2u));
    
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_AndLogicOP_10);
    bool res_NotLogicOP_11 = true;
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (L_P1__GetParamMainc11(my_id) == verde));
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! res_NotLogicOP_12);
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_NotLogicOP_11);
    
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_OrLogicOP_9);
    bool res_AndLogicOP_13 = true;
    res_AndLogicOP_13 = (res_AndLogicOP_13 && (L_P1__GetInConsd(my_id) == false));
    res_AndLogicOP_13 = (res_AndLogicOP_13 && Timer_Attivo(L_P1__GetMainc30(my_id)));
    
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_AndLogicOP_13);
    
    if(res_OrLogicOP_8){
    
    L_P1__SetMainc27(my_id,3u);
    }else{
    
    Timer_Disattiva(L_P1__GetMainc30(my_id));
    }
    //  *38,*  se il contatore MainClass_C1_contatore_Co9 non è  uguale a  *53,* 141 *37,* o  se la variabile MainClass_C1_variabile_V1 non è  diverso da  True  *37,* o  se la variabile MainClass_C1_variabile_V1 non è  uguale a  True  *35,* e  se il controllo MainClass_C1_controllo_C3 è  uguale a  True  *37,* e  se la variabile MainClass_C1_variabile_V1 non è  uguale a  False  *34,* o  se il parametro MainClass_C1_parametro_P8 è  diverso da Verde, *71,*Decrementa il contatore MainClass_C1_contatore_Co5
    bool res_OrLogicOP_14 = false;
    bool res_OrLogicOP_15 = false;
    bool res_OrLogicOP_16 = false;
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! (Counter_GetValore(L_P1__GetMainc32(my_id)) == 141u));
    res_OrLogicOP_16 = (res_OrLogicOP_16 || res_NotLogicOP_17);
    bool res_NotLogicOP_18 = true;
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (L_P1__GetMainc24(my_id) == true));
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! res_NotLogicOP_19);
    res_OrLogicOP_16 = (res_OrLogicOP_16 || res_NotLogicOP_18);
    
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_OrLogicOP_16);
    bool res_AndLogicOP_20 = true;
    bool res_AndLogicOP_21 = true;
    bool res_NotLogicOP_22 = true;
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! (L_P1__GetMainc24(my_id) == true));
    res_AndLogicOP_21 = (res_AndLogicOP_21 && res_NotLogicOP_22);
    res_AndLogicOP_21 = (res_AndLogicOP_21 && (L_P1__GetInMainc5(my_id) == true));
    
    res_AndLogicOP_20 = (res_AndLogicOP_20 && res_AndLogicOP_21);
    bool res_NotLogicOP_23 = true;
    res_NotLogicOP_23 = (res_NotLogicOP_23 && ! (L_P1__GetMainc24(my_id) == false));
    res_AndLogicOP_20 = (res_AndLogicOP_20 && res_NotLogicOP_23);
    
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_AndLogicOP_20);
    
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_OrLogicOP_15);
    bool res_NotLogicOP_24 = true;
    res_NotLogicOP_24 = (res_NotLogicOP_24 && ! (L_P1__GetParamMainc11(my_id) == verde));
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_NotLogicOP_24);
    
    if(res_OrLogicOP_14){
    
    Counter_Decr(L_P1__GetMainc31(my_id));
    }
    //  *36,*  se il timer MainClass_C1_timer_T8 non è scaduto, *69,*Disattiva il timer MainClass_C1_timer_T8
    // ,altrimenti  *68,*Attiva il timer MainClass_C1_timer_T8
    bool res_NotLogicOP_25 = true;
    res_NotLogicOP_25 = (res_NotLogicOP_25 && ! Timer_Scaduto(L_P1__GetMainc30(my_id)));
    if(res_NotLogicOP_25){
    
    Timer_Disattiva(L_P1__GetMainc30(my_id));
    }else{
    
    Timer_Attiva(L_P1__GetMainc30(my_id));
    }
    //  se la macro  MainClass_C1_macrova_M10 ( con argomento_a7   uguale a True  e argomento_a10   uguale a spento )  non  è  diverso da  True  *40,*  *34,* e  se il parametro MainClass_C1_parametro_P6 è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE  *35,* e  se il controllo MainClass_C1_controllo_C5 non è  diverso da  False  *35,* o  se il controllo MainClass_C1_controllo_C5 non è  uguale a  True , *67,* Assegna alla variabile MainClass_C1_variabile_V8 il valore 7
    // ,altrimenti  *68,*Attiva il timer MainClass_C1_timer_T8
    bool res_OrLogicOP_26 = false;
    bool res_OrLogicOP_27 = false;
    bool res_AndLogicOP_28 = true;
    bool res_NotLogicOP_29 = true;
    bool res_NotLogicOP_30 = true;
    res_NotLogicOP_30 = (res_NotLogicOP_30 && ! (L_P1__Macro3(my_id,spento,true) == true));
    res_NotLogicOP_29 = (res_NotLogicOP_29 && ! res_NotLogicOP_30);
    res_AndLogicOP_28 = (res_AndLogicOP_28 && res_NotLogicOP_29);
    res_AndLogicOP_28 = (res_AndLogicOP_28 && (L_P1__GetParamMainc10(my_id) == true));
    
    res_OrLogicOP_27 = (res_OrLogicOP_27 || res_AndLogicOP_28);
    bool res_AndLogicOP_31 = true;
    res_AndLogicOP_31 = (res_AndLogicOP_31 && (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_32 = true;
    bool res_NotLogicOP_33 = true;
    res_NotLogicOP_33 = (res_NotLogicOP_33 && ! (L_P1__GetInMainc6(my_id) == false));
    res_NotLogicOP_32 = (res_NotLogicOP_32 && ! res_NotLogicOP_33);
    res_AndLogicOP_31 = (res_AndLogicOP_31 && res_NotLogicOP_32);
    
    res_OrLogicOP_27 = (res_OrLogicOP_27 || res_AndLogicOP_31);
    
    res_OrLogicOP_26 = (res_OrLogicOP_26 || res_OrLogicOP_27);
    bool res_NotLogicOP_34 = true;
    res_NotLogicOP_34 = (res_NotLogicOP_34 && ! (L_P1__GetInMainc6(my_id) == true));
    res_OrLogicOP_26 = (res_OrLogicOP_26 || res_NotLogicOP_34);
    
    if(res_OrLogicOP_26){
    
    L_P1__SetMainc27(my_id,7u);
    }else{
    
    Timer_Attiva(L_P1__GetMainc30(my_id));
    }
}

/*
    CNL corrispondente:
     
    { commento: {38,}  se il contatore MainClass_C1_contatore_Co9 non è  uguale a  commento: {53,} 14204, commento: {71,}Decrementa il contatore MainClass_C1_contatore_Co5
    
       
      se la macro  MainClass_C1_macrova_M10 ( con argomento_a7   uguale a True  e argomento_a10   uguale a spento )   è  uguale a  True  commento: {40,}  commento: {36,} e  se il timer MainClass_C1_timer_T8 è scaduto commento: {36,} o  se il timer MainClass_C1_timer_T8 non è scaduto commento: {36,} o  se il timer MainClass_C1_timer_T8 è attivo,  Applica gli effetti
           della macro MainClass_C1_macroef_M5  commento: {73,}
    
     ,altrimenti  commento: {69,}Disattiva il timer MainClass_C1_timer_T8
    
    
     commento: {37,}  se la variabile MainClass_C1_variabile_V4 non è  uguale a  True  commento: {38,} o  se il contatore MainClass_C1_contatore_Co9 è  maggiore di  commento: {54,} 14351 commento: {35,} e  se il controllo MainClass_C1_controllo_C10 non è  diverso da c270 commento: {38,} o  se il contatore MainClass_C1_contatore_Co9 è  maggiore di  commento: {54,} 11, commento: {69,}Disattiva il timer MainClass_C1_timer_T8
    
     ,altrimenti   Applica gli effetti
           della macro MainClass_C1_macroef_M5  commento: {73,}
    
    
      se il controllo ConsDef è uguale a FALSE  commento: {35,} e  se il controllo MainClass_C1_controllo_C5 non è  diverso da  True  commento: {34,} o  se il parametro MainClass_C1_parametro_P8 è  uguale a Verde, commento: {66,} Assegna al comando MainClass_C1_comando_C9 il valore GialloGiallo
    
     ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V4 il valore  False 
    
    
     commento: {34,}  se il parametro MainClass_C1_parametro_P8 è  uguale a Verde commento: {37,} e  se la variabile MainClass_C1_variabile_V1 non è  uguale a  True  commento: {36,} e  se il timer MainClass_C1_timer_T8 è attivo commento: {38,} o  se il contatore MainClass_C1_contatore_Co9 non è  uguale a  commento: {53,} 13, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V8 il valore 2
    
       
    
    }
*/
void L_P1__Macro1(instance_id_t const my_id )
{
//  *38,*  se il contatore MainClass_C1_contatore_Co9 non è  uguale a  *53,* 14204, *71,*Decrementa il contatore MainClass_C1_contatore_Co5
    bool res_NotLogicOP_0 = true;
    res_NotLogicOP_0 = (res_NotLogicOP_0 && ! (Counter_GetValore(L_P1__GetMainc32(my_id)) == 14204u));
    if(res_NotLogicOP_0){
    
    Counter_Decr(L_P1__GetMainc31(my_id));
    }
    //  se la macro  MainClass_C1_macrova_M10 ( con argomento_a7   uguale a True  e argomento_a10   uguale a spento )   è  uguale a  True  *40,*  *36,* e  se il timer MainClass_C1_timer_T8 è scaduto *36,* o  se il timer MainClass_C1_timer_T8 non è scaduto *36,* o  se il timer MainClass_C1_timer_T8 è attivo,  Applica gli effetti
    //       della macro MainClass_C1_macroef_M5  *73,*
    // ,altrimenti  *69,*Disattiva il timer MainClass_C1_timer_T8
    bool res_OrLogicOP_1 = false;
    bool res_OrLogicOP_2 = false;
    bool res_AndLogicOP_3 = true;
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (L_P1__Macro3(my_id,spento,true) == true));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && Timer_Scaduto(L_P1__GetMainc30(my_id)));
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_3);
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! Timer_Scaduto(L_P1__GetMainc30(my_id)));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_4);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_OrLogicOP_2);
    res_OrLogicOP_1 = (res_OrLogicOP_1 || Timer_Attivo(L_P1__GetMainc30(my_id)));
    
    if(res_OrLogicOP_1){
    
    L_P1__Macro(my_id);
    }else{
    
    Timer_Disattiva(L_P1__GetMainc30(my_id));
    }
    //  *37,*  se la variabile MainClass_C1_variabile_V4 non è  uguale a  True  *38,* o  se il contatore MainClass_C1_contatore_Co9 è  maggiore di  *54,* 14351 *35,* e  se il controllo MainClass_C1_controllo_C10 non è  diverso da c270 *38,* o  se il contatore MainClass_C1_contatore_Co9 è  maggiore di  *54,* 11, *69,*Disattiva il timer MainClass_C1_timer_T8
    // ,altrimenti   Applica gli effetti
    //       della macro MainClass_C1_macroef_M5
    bool res_OrLogicOP_5 = false;
    bool res_OrLogicOP_6 = false;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetMainc26(my_id) == true));
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_NotLogicOP_7);
    bool res_AndLogicOP_8 = true;
    res_AndLogicOP_8 = (res_AndLogicOP_8 && (Counter_GetValore(L_P1__GetMainc32(my_id)) > 14351u));
    bool res_NotLogicOP_9 = true;
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__GetInMainc4(my_id) == c270));
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! res_NotLogicOP_10);
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_9);
    
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_AndLogicOP_8);
    
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_OrLogicOP_6);
    res_OrLogicOP_5 = (res_OrLogicOP_5 || (Counter_GetValore(L_P1__GetMainc32(my_id)) > 11u));
    
    if(res_OrLogicOP_5){
    
    Timer_Disattiva(L_P1__GetMainc30(my_id));
    }else{
    
    L_P1__Macro(my_id);
    }
    //  *73,*
    //  se il controllo ConsDef è uguale a FALSE  *35,* e  se il controllo MainClass_C1_controllo_C5 non è  diverso da  True  *34,* o  se il parametro MainClass_C1_parametro_P8 è  uguale a Verde, *66,* Assegna al comando MainClass_C1_comando_C9 il valore GialloGiallo
    // ,altrimenti  *67,* Assegna alla variabile MainClass_C1_variabile_V4 il valore  False
    bool res_OrLogicOP_11 = false;
    bool res_AndLogicOP_12 = true;
    res_AndLogicOP_12 = (res_AndLogicOP_12 && (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_13 = true;
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1__GetInMainc6(my_id) == true));
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! res_NotLogicOP_14);
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_NotLogicOP_13);
    
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_AndLogicOP_12);
    res_OrLogicOP_11 = (res_OrLogicOP_11 || (L_P1__GetParamMainc11(my_id) == verde));
    
    if(res_OrLogicOP_11){
    
    L_P1__SetOutMainc3(my_id,giallogiall);
    }else{
    
    L_P1__SetMainc26(my_id,false);
    }
    //  *34,*  se il parametro MainClass_C1_parametro_P8 è  uguale a Verde *37,* e  se la variabile MainClass_C1_variabile_V1 non è  uguale a  True  *36,* e  se il timer MainClass_C1_timer_T8 è attivo *38,* o  se il contatore MainClass_C1_contatore_Co9 non è  uguale a  *53,* 13, *67,* Assegna alla variabile MainClass_C1_variabile_V8 il valore 2
    bool res_OrLogicOP_15 = false;
    bool res_AndLogicOP_16 = true;
    bool res_AndLogicOP_17 = true;
    res_AndLogicOP_17 = (res_AndLogicOP_17 && (L_P1__GetParamMainc11(my_id) == verde));
    bool res_NotLogicOP_18 = true;
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! (L_P1__GetMainc24(my_id) == true));
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_NotLogicOP_18);
    
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_AndLogicOP_17);
    res_AndLogicOP_16 = (res_AndLogicOP_16 && Timer_Attivo(L_P1__GetMainc30(my_id)));
    
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_AndLogicOP_16);
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (Counter_GetValore(L_P1__GetMainc32(my_id)) == 13u));
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_NotLogicOP_19);
    
    if(res_OrLogicOP_15){
    
    L_P1__SetMainc27(my_id,2u);
    }
}

/*
    CNL corrispondente:
    
    { commento: {37,}  se la variabile MainClass_C1_variabile_V4 non è  uguale a  True  o  se l'argomento argomento_af1 è  uguale a  True  commento: {39,} , commento: {67,} Assegna alla variabile MainClass_C1_variabile_V2 il valore c270
    
       
    
    }
*/
void L_P1__Macro2(instance_id_t const my_id , bool argom3, C1_Enumerat2 argom4, C1_Enumerat3 argom5, bool argom6, C1_Enumerat2 argom7, C1_Enumerat4 argom8, C1_Enumerat1 argom9)
{
//  *37,*  se la variabile MainClass_C1_variabile_V4 non è  uguale a  True  o  se l'argomento argomento_af1 è  uguale a  True  *39,* , *67,* Assegna alla variabile MainClass_C1_variabile_V2 il valore c270
    bool res_OrLogicOP_0 = false;
    bool res_NotLogicOP_1 = true;
    res_NotLogicOP_1 = (res_NotLogicOP_1 && ! (L_P1__GetMainc26(my_id) == true));
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_1);
    res_OrLogicOP_0 = (res_OrLogicOP_0 || (argom3 == true));
    
    if(res_OrLogicOP_0){
    
    L_P1__SetMainc25(my_id,c270);
    }
}


// Macro di verifica

/*
    CNL corrispondente:
    
    { commento: {62,} commento: {34,}  se il parametro MainClass_C1_parametro_P8 è  diverso da Verde commento: {34,} o  se il parametro MainClass_C1_parametro_P6 non è  diverso da  True  commento: {38,} e  se il contatore MainClass_C1_contatore_Co9 è  maggiore di  commento: {54,} 1443 commento: {38,} o  se il contatore MainClass_C1_contatore_Co9 è  uguale a  commento: {53,} 1151, Almeno una delle seguenti { 
     commento: {63,}  se il controllo ConsDef è uguale a FALSE  commento: {34,} o  se il parametro MainClass_C1_parametro_P10 è  diverso da c180 commento: {38,} e  se il contatore MainClass_C1_contatore_Co5 è  maggiore di  commento: {54,} 15204, Solo una delle seguenti { 
     commento: {63,} commento: {34,}  se il parametro MainClass_C1_parametro_P6 è  diverso da  False  commento: {34,} o  se il parametro MainClass_C1_parametro_P8 è  uguale a Verde commento: {36,} e  se il timer MainClass_C1_timer_T8 è disattivo commento: {34,} e  se il parametro MainClass_C1_parametro_P6 non è  diverso da  False  commento: {35,} e  se il controllo MainClass_C1_controllo_C10 non è  uguale a c270, Solo una delle seguenti { 
     commento: {61,} commento: {34,}  se lo stato  non è  uguale a  commento: {53,}  state1  commento: {106,} commento: {34,} o  se il parametro MainClass_C1_parametro_P6 è  diverso da  False  commento: {34,} o  se il parametro MainClass_C1_parametro_P8 non è  uguale a Verde, Tutte le seguenti { 
     commento: {63,} commento: {36,}  se il timer MainClass_C1_timer_T8 non è disattivo commento: {38,} o  se il contatore MainClass_C1_contatore_Co5 è  diverso da  commento: {56,} 13351 commento: {35,} e  se il controllo MainClass_C1_controllo_C10 non è  diverso da c270 commento: {35,} e  se il controllo MainClass_C1_controllo_C10 è  diverso da c270, Solo una delle seguenti { 
     commento: {61,}  se l'argomento argomento_ave2 è  uguale a  True  commento: {39,}  commento: {34,} o  se il parametro MainClass_C1_parametro_P10 è  uguale a c180 commento: {36,} o  se il timer MainClass_C1_timer_T8 è attivo e  se l'argomento argomento_ave9 è  diverso da GialloGiallo commento: {39,}  commento: {38,} e  se il contatore MainClass_C1_contatore_Co9 non è  minore di  commento: {55,} 14, Tutte le seguenti { 
     commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  uguale a  True  commento: {34,} o  se il parametro MainClass_C1_parametro_P6 è  diverso da  False  commento: {38,} o  se il contatore MainClass_C1_contatore_Co5 non è  maggiore di  commento: {54,} 12204 commento: {38,} e  se il contatore MainClass_C1_contatore_Co9 è  diverso da  commento: {56,} 153, Verifica che   commento: {51,}  commento: {,}  il contatore MainClass_C1_contatore_Co5 sia  uguale a  commento: {53,} 115
    
    
     } Verifica che   commento: {47,48,50,51,}  commento: {,}  la variabile MainClass_C1_variabile_V1 non sia  diverso da  True 
     commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P8 sia  uguale a Verde
     commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C6 non sia  uguale a  False 
     commento: {104,} o  che  commento: {35,}  il controllo MainClass_C1_controllo_C6 non sia  uguale a  True 
     commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co9 sia  diverso da  commento: {56,} 1
    
    
     } Verifica che   commento: {52,}   l'argomento argomento_ave2 non  sia  uguale a  False  commento: {,} 
    
    
     } Verifica che   commento: {48,50,52,}   l'argomento argomento_ave2 sia  uguale a  True  commento: {,} 
     commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V1 sia  uguale a  True 
     commento: {104,} e  che  commento: {37,}  la variabile MainClass_C1_variabile_V2 non sia  uguale a c270
     commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C5 sia  diverso da  True 
    
    
     } Verifica che   commento: {47,48,49,50,51,52,}  commento: {,}  la variabile MainClass_C1_variabile_V1 sia  uguale a  True 
     commento: {104,} o  che  commento: {,}  il contatore MainClass_C1_contatore_Co9 sia  diverso da  commento: {56,} 1520
     commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T8 sia attivo
     commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P8 non sia  diverso da Verde
     commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C10 non sia  uguale a c270
     commento: {104,} o  che   l'argomento argomento_ave8 sia  diverso da Verde commento: {,} 
    
    
     } Verifica che   commento: {47,51,}  commento: {34,}  il parametro MainClass_C1_parametro_P8 sia  uguale a Verde
     commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co9 non sia  diverso da  commento: {56,} 1
    
    
     } Verifica che   commento: {50,}  commento: {,}  la variabile MainClass_C1_variabile_V2 sia  diverso da c270
     commento: {104,} e  che  commento: {37,}  la variabile MainClass_C1_variabile_V8 sia  maggiore di  commento: {54,} 1
    
    
    }
*/
bool L_P1__Macro4(instance_id_t const my_id , C1_Enumerat4 argom12, bool argom13, C1_Enumerat3 argom14, C1_Enumerat2 argom15, C1_Enumerat4 argom16)
{
bool res_AndLogicOP_0 = true;
    
    //  *62,* *34,*  se il parametro MainClass_C1_parametro_P8 è  diverso da Verde *34,* o  se il parametro MainClass_C1_parametro_P6 non è  diverso da  True  *38,* e  se il contatore MainClass_C1_contatore_Co9 è  maggiore di  *54,* 1443 *38,* o  se il contatore MainClass_C1_contatore_Co9 è  uguale a  *53,* 1151, Almeno una delle seguenti { 
    //   *63,*  se il controllo ConsDef è uguale a FALSE  *34,* o  se il parametro MainClass_C1_parametro_P10 è  diverso da c180 *38,* e  se il contatore MainClass_C1_contatore_Co5 è  maggiore di  *54,* 15204, Solo una delle seguenti { 
    //   *63,* *34,*  se il parametro MainClass_C1_parametro_P6 è  diverso da  False  *34,* o  se il parametro MainClass_C1_parametro_P8 è  uguale a Verde *36,* e  se il timer MainClass_C1_timer_T8 è disattivo *34,* e  se il parametro MainClass_C1_parametro_P6 non è  diverso da  False  *35,* e  se il controllo MainClass_C1_controllo_C10 non è  uguale a c270, Solo una delle seguenti { 
    //   *61,* *34,*  se lo stato  non è  uguale a  *53,*  state1  *106,* *34,* o  se il parametro MainClass_C1_parametro_P6 è  diverso da  False  *34,* o  se il parametro MainClass_C1_parametro_P8 non è  uguale a Verde, Tutte le seguenti { 
    //   *63,* *36,*  se il timer MainClass_C1_timer_T8 non è disattivo *38,* o  se il contatore MainClass_C1_contatore_Co5 è  diverso da  *56,* 13351 *35,* e  se il controllo MainClass_C1_controllo_C10 non è  diverso da c270 *35,* e  se il controllo MainClass_C1_controllo_C10 è  diverso da c270, Solo una delle seguenti { 
    //   *61,*  se l'argomento argomento_ave2 è  uguale a  True  *39,*  *34,* o  se il parametro MainClass_C1_parametro_P10 è  uguale a c180 *36,* o  se il timer MainClass_C1_timer_T8 è attivo e  se l'argomento argomento_ave9 è  diverso da GialloGiallo *39,*  *38,* e  se il contatore MainClass_C1_contatore_Co9 non è  minore di  *55,* 14, Tutte le seguenti { 
    //   *109,*  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  uguale a  True  *34,* o  se il parametro MainClass_C1_parametro_P6 è  diverso da  False  *38,* o  se il contatore MainClass_C1_contatore_Co5 non è  maggiore di  *54,* 12204 *38,* e  se il contatore MainClass_C1_contatore_Co9 è  diverso da  *56,* 153, Verifica che   *51,*  *,*  il contatore MainClass_C1_contatore_Co5 sia  uguale a  *53,* 115
    //   } Verifica che   *47,48,50,51,*  *,*  la variabile MainClass_C1_variabile_V1 non sia  diverso da  True 
    //   *104,* o  che  *34,*  il parametro MainClass_C1_parametro_P8 sia  uguale a Verde
    //   *104,* o  che  *,*  il controllo MainClass_C1_controllo_C6 non sia  uguale a  False 
    //   *104,* o  che  *35,*  il controllo MainClass_C1_controllo_C6 non sia  uguale a  True 
    //   *104,* e  che  *,*  il contatore MainClass_C1_contatore_Co9 sia  diverso da  *56,* 1
    //   } Verifica che   *52,*   l'argomento argomento_ave2 non  sia  uguale a  False  *,* 
    //   } Verifica che   *48,50,52,*   l'argomento argomento_ave2 sia  uguale a  True  *,* 
    //   *104,* e  che  *,*  la variabile MainClass_C1_variabile_V1 sia  uguale a  True 
    //   *104,* e  che  *37,*  la variabile MainClass_C1_variabile_V2 non sia  uguale a c270
    //   *104,* o  che  *,*  il controllo MainClass_C1_controllo_C5 sia  diverso da  True 
    //   } Verifica che   *47,48,49,50,51,52,*  *,*  la variabile MainClass_C1_variabile_V1 sia  uguale a  True 
    //   *104,* o  che  *,*  il contatore MainClass_C1_contatore_Co9 sia  diverso da  *56,* 1520
    //   *104,* o  che  *,*  il timer MainClass_C1_timer_T8 sia attivo
    //   *104,* e  che  *34,*  il parametro MainClass_C1_parametro_P8 non sia  diverso da Verde
    //   *104,* e  che  *,*  il controllo MainClass_C1_controllo_C10 non sia  uguale a c270
    //   *104,* o  che   l'argomento argomento_ave8 sia  diverso da Verde *,* 
    //   } Verifica che   *47,51,*  *34,*  il parametro MainClass_C1_parametro_P8 sia  uguale a Verde
    //   *104,* e  che  *,*  il contatore MainClass_C1_contatore_Co9 non sia  diverso da  *56,* 1
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetParamMainc11(my_id) == verde));
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_NotLogicOP_4);
    bool res_AndLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetParamMainc10(my_id) == true));
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! res_NotLogicOP_7);
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_6);
    res_AndLogicOP_5 = (res_AndLogicOP_5 && (Counter_GetValore(L_P1__GetMainc32(my_id)) > 1443u));
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_AndLogicOP_5);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    res_OrLogicOP_2 = (res_OrLogicOP_2 || (Counter_GetValore(L_P1__GetMainc32(my_id)) == 1151u));
    
    if(res_OrLogicOP_2){
    bool res_OrLogicOP_8 = false;
    bool res_ImpliesLogicOp_9 = true;
    bool res_OrLogicOP_10 = false;
    res_OrLogicOP_10 = (res_OrLogicOP_10 || (L_P1__GetInConsd(my_id) == false));
    bool res_AndLogicOP_11 = true;
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (L_P1__GetParamMainc9(my_id) == c180));
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_NotLogicOP_12);
    res_AndLogicOP_11 = (res_AndLogicOP_11 && (Counter_GetValore(L_P1__GetMainc31(my_id)) > 15204u));
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_AndLogicOP_11);
    
    if(res_OrLogicOP_10){
    bool res_XorLogicOP_13 = true;
    int xorIndex_res_XorLogicOP_13 = 0;
    bool res_ImpliesLogicOp_14 = true;
    bool res_OrLogicOP_15 = false;
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (L_P1__GetParamMainc10(my_id) == false));
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_NotLogicOP_16);
    bool res_AndLogicOP_17 = true;
    bool res_AndLogicOP_18 = true;
    bool res_AndLogicOP_19 = true;
    res_AndLogicOP_19 = (res_AndLogicOP_19 && (L_P1__GetParamMainc11(my_id) == verde));
    res_AndLogicOP_19 = (res_AndLogicOP_19 && Timer_Disattivo(L_P1__GetMainc30(my_id)));
    
    res_AndLogicOP_18 = (res_AndLogicOP_18 && res_AndLogicOP_19);
    bool res_NotLogicOP_20 = true;
    bool res_NotLogicOP_21 = true;
    res_NotLogicOP_21 = (res_NotLogicOP_21 && ! (L_P1__GetParamMainc10(my_id) == false));
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! res_NotLogicOP_21);
    res_AndLogicOP_18 = (res_AndLogicOP_18 && res_NotLogicOP_20);
    
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_AndLogicOP_18);
    bool res_NotLogicOP_22 = true;
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! (L_P1__GetInMainc4(my_id) == c270));
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_NotLogicOP_22);
    
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_AndLogicOP_17);
    
    if(res_OrLogicOP_15){
    bool res_XorLogicOP_23 = true;
    int xorIndex_res_XorLogicOP_23 = 0;
    bool res_ImpliesLogicOp_24 = true;
    bool res_OrLogicOP_25 = false;
    bool res_OrLogicOP_26 = false;
    bool res_NotLogicOP_27 = true;
    res_NotLogicOP_27 = (res_NotLogicOP_27 && ! (L_P1_C1_GetState(my_id) == C1_St_state));
    res_OrLogicOP_26 = (res_OrLogicOP_26 || res_NotLogicOP_27);
    bool res_NotLogicOP_28 = true;
    res_NotLogicOP_28 = (res_NotLogicOP_28 && ! (L_P1__GetParamMainc10(my_id) == false));
    res_OrLogicOP_26 = (res_OrLogicOP_26 || res_NotLogicOP_28);
    
    res_OrLogicOP_25 = (res_OrLogicOP_25 || res_OrLogicOP_26);
    bool res_NotLogicOP_29 = true;
    res_NotLogicOP_29 = (res_NotLogicOP_29 && ! (L_P1__GetParamMainc11(my_id) == verde));
    res_OrLogicOP_25 = (res_OrLogicOP_25 || res_NotLogicOP_29);
    
    if(res_OrLogicOP_25){
    bool res_AndLogicOP_30 = true;
    bool res_ImpliesLogicOp_31 = true;
    bool res_OrLogicOP_32 = false;
    bool res_NotLogicOP_33 = true;
    res_NotLogicOP_33 = (res_NotLogicOP_33 && ! Timer_Disattivo(L_P1__GetMainc30(my_id)));
    res_OrLogicOP_32 = (res_OrLogicOP_32 || res_NotLogicOP_33);
    bool res_AndLogicOP_34 = true;
    bool res_AndLogicOP_35 = true;
    bool res_NotLogicOP_36 = true;
    res_NotLogicOP_36 = (res_NotLogicOP_36 && ! (Counter_GetValore(L_P1__GetMainc31(my_id)) == 13351u));
    res_AndLogicOP_35 = (res_AndLogicOP_35 && res_NotLogicOP_36);
    bool res_NotLogicOP_37 = true;
    bool res_NotLogicOP_38 = true;
    res_NotLogicOP_38 = (res_NotLogicOP_38 && ! (L_P1__GetInMainc4(my_id) == c270));
    res_NotLogicOP_37 = (res_NotLogicOP_37 && ! res_NotLogicOP_38);
    res_AndLogicOP_35 = (res_AndLogicOP_35 && res_NotLogicOP_37);
    
    res_AndLogicOP_34 = (res_AndLogicOP_34 && res_AndLogicOP_35);
    bool res_NotLogicOP_39 = true;
    res_NotLogicOP_39 = (res_NotLogicOP_39 && ! (L_P1__GetInMainc4(my_id) == c270));
    res_AndLogicOP_34 = (res_AndLogicOP_34 && res_NotLogicOP_39);
    
    res_OrLogicOP_32 = (res_OrLogicOP_32 || res_AndLogicOP_34);
    
    if(res_OrLogicOP_32){
    bool res_XorLogicOP_40 = true;
    int xorIndex_res_XorLogicOP_40 = 0;
    bool res_ImpliesLogicOp_41 = true;
    bool res_OrLogicOP_42 = false;
    bool res_OrLogicOP_43 = false;
    res_OrLogicOP_43 = (res_OrLogicOP_43 || (argom13 == true));
    res_OrLogicOP_43 = (res_OrLogicOP_43 || (L_P1__GetParamMainc9(my_id) == c180));
    
    res_OrLogicOP_42 = (res_OrLogicOP_42 || res_OrLogicOP_43);
    bool res_AndLogicOP_44 = true;
    bool res_AndLogicOP_45 = true;
    res_AndLogicOP_45 = (res_AndLogicOP_45 && Timer_Attivo(L_P1__GetMainc30(my_id)));
    bool res_NotLogicOP_46 = true;
    res_NotLogicOP_46 = (res_NotLogicOP_46 && ! (argom16 == giallogiall));
    res_AndLogicOP_45 = (res_AndLogicOP_45 && res_NotLogicOP_46);
    
    res_AndLogicOP_44 = (res_AndLogicOP_44 && res_AndLogicOP_45);
    bool res_NotLogicOP_47 = true;
    res_NotLogicOP_47 = (res_NotLogicOP_47 && ! (Counter_GetValore(L_P1__GetMainc32(my_id)) < 14u));
    res_AndLogicOP_44 = (res_AndLogicOP_44 && res_NotLogicOP_47);
    
    res_OrLogicOP_42 = (res_OrLogicOP_42 || res_AndLogicOP_44);
    
    if(res_OrLogicOP_42){
    bool res_ImpliesLogicOp_48 = true;
    bool res_OrLogicOP_49 = false;
    bool res_OrLogicOP_50 = false;
    res_OrLogicOP_50 = (res_OrLogicOP_50 || (L_P1__GetMainc23(my_id) == true));
    bool res_NotLogicOP_51 = true;
    res_NotLogicOP_51 = (res_NotLogicOP_51 && ! (L_P1__GetParamMainc10(my_id) == false));
    res_OrLogicOP_50 = (res_OrLogicOP_50 || res_NotLogicOP_51);
    
    res_OrLogicOP_49 = (res_OrLogicOP_49 || res_OrLogicOP_50);
    bool res_AndLogicOP_52 = true;
    bool res_NotLogicOP_53 = true;
    res_NotLogicOP_53 = (res_NotLogicOP_53 && ! (Counter_GetValore(L_P1__GetMainc31(my_id)) > 12204u));
    res_AndLogicOP_52 = (res_AndLogicOP_52 && res_NotLogicOP_53);
    bool res_NotLogicOP_54 = true;
    res_NotLogicOP_54 = (res_NotLogicOP_54 && ! (Counter_GetValore(L_P1__GetMainc32(my_id)) == 153u));
    res_AndLogicOP_52 = (res_AndLogicOP_52 && res_NotLogicOP_54);
    
    res_OrLogicOP_49 = (res_OrLogicOP_49 || res_AndLogicOP_52);
    
    if(res_OrLogicOP_49){
    res_ImpliesLogicOp_48 = (res_ImpliesLogicOp_48 && (Counter_GetValore(L_P1__GetMainc31(my_id)) == 115u));
    }
    res_ImpliesLogicOp_41 = (res_ImpliesLogicOp_41 && res_ImpliesLogicOp_48);
    }
    if(res_ImpliesLogicOp_41){
    xorIndex_res_XorLogicOP_40 = (xorIndex_res_XorLogicOP_40 + 1);
    }
    bool res_OrLogicOP_55 = false;
    bool res_OrLogicOP_56 = false;
    bool res_OrLogicOP_57 = false;
    bool res_NotLogicOP_58 = true;
    bool res_NotLogicOP_59 = true;
    res_NotLogicOP_59 = (res_NotLogicOP_59 && ! (L_P1__GetMainc24(my_id) == true));
    res_NotLogicOP_58 = (res_NotLogicOP_58 && ! res_NotLogicOP_59);
    res_OrLogicOP_57 = (res_OrLogicOP_57 || res_NotLogicOP_58);
    res_OrLogicOP_57 = (res_OrLogicOP_57 || (L_P1__GetParamMainc11(my_id) == verde));
    
    res_OrLogicOP_56 = (res_OrLogicOP_56 || res_OrLogicOP_57);
    bool res_NotLogicOP_60 = true;
    res_NotLogicOP_60 = (res_NotLogicOP_60 && ! (L_P1__GetInMainc7(my_id) == false));
    res_OrLogicOP_56 = (res_OrLogicOP_56 || res_NotLogicOP_60);
    
    res_OrLogicOP_55 = (res_OrLogicOP_55 || res_OrLogicOP_56);
    bool res_AndLogicOP_61 = true;
    bool res_NotLogicOP_62 = true;
    res_NotLogicOP_62 = (res_NotLogicOP_62 && ! (L_P1__GetInMainc7(my_id) == true));
    res_AndLogicOP_61 = (res_AndLogicOP_61 && res_NotLogicOP_62);
    bool res_NotLogicOP_63 = true;
    res_NotLogicOP_63 = (res_NotLogicOP_63 && ! (Counter_GetValore(L_P1__GetMainc32(my_id)) == 1u));
    res_AndLogicOP_61 = (res_AndLogicOP_61 && res_NotLogicOP_63);
    
    res_OrLogicOP_55 = (res_OrLogicOP_55 || res_AndLogicOP_61);
    
    if(res_OrLogicOP_55){
    xorIndex_res_XorLogicOP_40 = (xorIndex_res_XorLogicOP_40 + 1);
    }
    
    res_XorLogicOP_40 = (res_XorLogicOP_40 && (xorIndex_res_XorLogicOP_40 == 1));
    res_ImpliesLogicOp_31 = (res_ImpliesLogicOp_31 && res_XorLogicOP_40);
    }
    res_AndLogicOP_30 = (res_AndLogicOP_30 && res_ImpliesLogicOp_31);
    bool res_NotLogicOP_64 = true;
    res_NotLogicOP_64 = (res_NotLogicOP_64 && ! (argom13 == false));
    res_AndLogicOP_30 = (res_AndLogicOP_30 && res_NotLogicOP_64);
    
    res_ImpliesLogicOp_24 = (res_ImpliesLogicOp_24 && res_AndLogicOP_30);
    }
    if(res_ImpliesLogicOp_24){
    xorIndex_res_XorLogicOP_23 = (xorIndex_res_XorLogicOP_23 + 1);
    }
    bool res_OrLogicOP_65 = false;
    bool res_AndLogicOP_66 = true;
    bool res_AndLogicOP_67 = true;
    res_AndLogicOP_67 = (res_AndLogicOP_67 && (argom13 == true));
    res_AndLogicOP_67 = (res_AndLogicOP_67 && (L_P1__GetMainc24(my_id) == true));
    
    res_AndLogicOP_66 = (res_AndLogicOP_66 && res_AndLogicOP_67);
    bool res_NotLogicOP_68 = true;
    res_NotLogicOP_68 = (res_NotLogicOP_68 && ! (L_P1__GetMainc25(my_id) == c270));
    res_AndLogicOP_66 = (res_AndLogicOP_66 && res_NotLogicOP_68);
    
    res_OrLogicOP_65 = (res_OrLogicOP_65 || res_AndLogicOP_66);
    bool res_NotLogicOP_69 = true;
    res_NotLogicOP_69 = (res_NotLogicOP_69 && ! (L_P1__GetInMainc6(my_id) == true));
    res_OrLogicOP_65 = (res_OrLogicOP_65 || res_NotLogicOP_69);
    
    if(res_OrLogicOP_65){
    xorIndex_res_XorLogicOP_23 = (xorIndex_res_XorLogicOP_23 + 1);
    }
    
    res_XorLogicOP_23 = (res_XorLogicOP_23 && (xorIndex_res_XorLogicOP_23 == 1));
    res_ImpliesLogicOp_14 = (res_ImpliesLogicOp_14 && res_XorLogicOP_23);
    }
    if(res_ImpliesLogicOp_14){
    xorIndex_res_XorLogicOP_13 = (xorIndex_res_XorLogicOP_13 + 1);
    }
    bool res_OrLogicOP_70 = false;
    bool res_OrLogicOP_71 = false;
    bool res_OrLogicOP_72 = false;
    res_OrLogicOP_72 = (res_OrLogicOP_72 || (L_P1__GetMainc24(my_id) == true));
    bool res_NotLogicOP_73 = true;
    res_NotLogicOP_73 = (res_NotLogicOP_73 && ! (Counter_GetValore(L_P1__GetMainc32(my_id)) == 1520u));
    res_OrLogicOP_72 = (res_OrLogicOP_72 || res_NotLogicOP_73);
    
    res_OrLogicOP_71 = (res_OrLogicOP_71 || res_OrLogicOP_72);
    bool res_AndLogicOP_74 = true;
    bool res_AndLogicOP_75 = true;
    res_AndLogicOP_75 = (res_AndLogicOP_75 && Timer_Attivo(L_P1__GetMainc30(my_id)));
    bool res_NotLogicOP_76 = true;
    bool res_NotLogicOP_77 = true;
    res_NotLogicOP_77 = (res_NotLogicOP_77 && ! (L_P1__GetParamMainc11(my_id) == verde));
    res_NotLogicOP_76 = (res_NotLogicOP_76 && ! res_NotLogicOP_77);
    res_AndLogicOP_75 = (res_AndLogicOP_75 && res_NotLogicOP_76);
    
    res_AndLogicOP_74 = (res_AndLogicOP_74 && res_AndLogicOP_75);
    bool res_NotLogicOP_78 = true;
    res_NotLogicOP_78 = (res_NotLogicOP_78 && ! (L_P1__GetInMainc4(my_id) == c270));
    res_AndLogicOP_74 = (res_AndLogicOP_74 && res_NotLogicOP_78);
    
    res_OrLogicOP_71 = (res_OrLogicOP_71 || res_AndLogicOP_74);
    
    res_OrLogicOP_70 = (res_OrLogicOP_70 || res_OrLogicOP_71);
    bool res_NotLogicOP_79 = true;
    res_NotLogicOP_79 = (res_NotLogicOP_79 && ! (argom15 == verde));
    res_OrLogicOP_70 = (res_OrLogicOP_70 || res_NotLogicOP_79);
    
    if(res_OrLogicOP_70){
    xorIndex_res_XorLogicOP_13 = (xorIndex_res_XorLogicOP_13 + 1);
    }
    
    res_XorLogicOP_13 = (res_XorLogicOP_13 && (xorIndex_res_XorLogicOP_13 == 1));
    res_ImpliesLogicOp_9 = (res_ImpliesLogicOp_9 && res_XorLogicOP_13);
    }
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_ImpliesLogicOp_9);
    bool res_AndLogicOP_80 = true;
    res_AndLogicOP_80 = (res_AndLogicOP_80 && (L_P1__GetParamMainc11(my_id) == verde));
    bool res_NotLogicOP_81 = true;
    bool res_NotLogicOP_82 = true;
    res_NotLogicOP_82 = (res_NotLogicOP_82 && ! (Counter_GetValore(L_P1__GetMainc32(my_id)) == 1u));
    res_NotLogicOP_81 = (res_NotLogicOP_81 && ! res_NotLogicOP_82);
    res_AndLogicOP_80 = (res_AndLogicOP_80 && res_NotLogicOP_81);
    
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_AndLogicOP_80);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_OrLogicOP_8);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *50,*  *,*  la variabile MainClass_C1_variabile_V2 sia  diverso da c270
    //   *104,* e  che  *37,*  la variabile MainClass_C1_variabile_V8 sia  maggiore di  *54,* 1
    bool res_AndLogicOP_83 = true;
    bool res_NotLogicOP_84 = true;
    res_NotLogicOP_84 = (res_NotLogicOP_84 && ! (L_P1__GetMainc25(my_id) == c270));
    res_AndLogicOP_83 = (res_AndLogicOP_83 && res_NotLogicOP_84);
    res_AndLogicOP_83 = (res_AndLogicOP_83 && (L_P1__GetMainc27(my_id) > 1u));
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_AndLogicOP_83);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
    
    { commento: {61,} commento: {37,}  se la variabile MainClass_C1_variabile_V1 è  diverso da  True  o  se l'argomento argomento_ave7 non  è  uguale a c180 commento: {39,}  commento: {37,} o  se la variabile MainClass_C1_variabile_V1 è  uguale a  True , Tutte le seguenti { 
     commento: {63,} commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è scaduto, Solo una delle seguenti { 
     commento: {62,}  se il controllo ConsDef è uguale a FALSE  commento: {35,} e  se il controllo MainClass_C1_controllo_C10 è  diverso da c270, Almeno una delle seguenti { 
     commento: {62,} commento: {37,}  se la variabile MainClass_C1_variabile_V1 è  uguale a  False , Almeno una delle seguenti { 
     commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è disattivo commento: {35,} e  se il controllo MainClass_C1_controllo_C10 non è  uguale a c270 commento: {37,} e  se la variabile MainClass_C1_variabile_V1 non è  diverso da  True  commento: {34,} o  se il parametro MainClass_C1_parametro_P10 non è  diverso da c180 commento: {35,} o  se il controllo MainClass_C1_controllo_C5 non è  diverso da  False  commento: {35,} o  se il controllo MainClass_C1_controllo_C7 è  diverso da c270, Verifica che   commento: {49,50,52,}  commento: {,}  il timer MainClass_C1_timer_T8 non sia disattivo
     commento: {104,} o  che   l'argomento argomento_ave7 non  sia  diverso da c180 commento: {,} 
     commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V1 sia  uguale a  False 
    
    
     } Verifica che   commento: {47,48,51,52,}  commento: {,}  il contatore MainClass_C1_contatore_Co9 non sia  diverso da  commento: {56,} 1504
     commento: {104,} e  che  commento: {35,}  il controllo MainClass_C1_controllo_C10 sia  diverso da c270
     commento: {104,} o  che   l'argomento argomento_ave7 sia  diverso da c180 commento: {,} 
     commento: {104,} e  che   l'argomento argomento_ave7 non  sia  uguale a c180 commento: {39,} 
     commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P8 sia  uguale a Verde
    
    
     } Verifica che   commento: {47,50,}  commento: {,}  la variabile MainClass_C1_variabile_V1 sia  diverso da  False 
     commento: {104,} e  che  commento: {37,}  la variabile MainClass_C1_variabile_V1 non sia  diverso da  True 
     commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P6 non sia  diverso da  False 
     commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P8 sia  uguale a Verde
     commento: {104,} e  che  commento: {37,}  la variabile MainClass_C1_variabile_V8 sia  uguale a  commento: {53,} 4
    
    
     } Verifica che   commento: {52,}   l'argomento argomento_ave7 non  sia  diverso da c180 commento: {,} 
    
    
     } Verifica che   commento: {48,49,}  commento: {,}  il timer MainClass_C1_timer_T8 non sia attivo
     commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C5 sia  diverso da  True 
    
    
    }
*/
bool L_P1__Macro5(instance_id_t const my_id , C1_Enumerat4 argom17, C1_Enumerat1 argom18)
{
bool res_AndLogicOP_0 = true;
    
    //  *61,* *37,*  se la variabile MainClass_C1_variabile_V1 è  diverso da  True  o  se l'argomento argomento_ave7 non  è  uguale a c180 *39,*  *37,* o  se la variabile MainClass_C1_variabile_V1 è  uguale a  True , Tutte le seguenti { 
    //   *63,* *110,*  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è scaduto, Solo una delle seguenti { 
    //   *62,*  se il controllo ConsDef è uguale a FALSE  *35,* e  se il controllo MainClass_C1_controllo_C10 è  diverso da c270, Almeno una delle seguenti { 
    //   *62,* *37,*  se la variabile MainClass_C1_variabile_V1 è  uguale a  False , Almeno una delle seguenti { 
    //   *110,*  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è disattivo *35,* e  se il controllo MainClass_C1_controllo_C10 non è  uguale a c270 *37,* e  se la variabile MainClass_C1_variabile_V1 non è  diverso da  True  *34,* o  se il parametro MainClass_C1_parametro_P10 non è  diverso da c180 *35,* o  se il controllo MainClass_C1_controllo_C5 non è  diverso da  False  *35,* o  se il controllo MainClass_C1_controllo_C7 è  diverso da c270, Verifica che   *49,50,52,*  *,*  il timer MainClass_C1_timer_T8 non sia disattivo
    //   *104,* o  che   l'argomento argomento_ave7 non  sia  diverso da c180 *,* 
    //   *104,* o  che  *,*  la variabile MainClass_C1_variabile_V1 sia  uguale a  False 
    //   } Verifica che   *47,48,51,52,*  *,*  il contatore MainClass_C1_contatore_Co9 non sia  diverso da  *56,* 1504
    //   *104,* e  che  *35,*  il controllo MainClass_C1_controllo_C10 sia  diverso da c270
    //   *104,* o  che   l'argomento argomento_ave7 sia  diverso da c180 *,* 
    //   *104,* e  che   l'argomento argomento_ave7 non  sia  uguale a c180 *39,* 
    //   *104,* e  che  *34,*  il parametro MainClass_C1_parametro_P8 sia  uguale a Verde
    //   } Verifica che   *47,50,*  *,*  la variabile MainClass_C1_variabile_V1 sia  diverso da  False 
    //   *104,* e  che  *37,*  la variabile MainClass_C1_variabile_V1 non sia  diverso da  True 
    //   *104,* o  che  *34,*  il parametro MainClass_C1_parametro_P6 non sia  diverso da  False 
    //   *104,* o  che  *34,*  il parametro MainClass_C1_parametro_P8 sia  uguale a Verde
    //   *104,* e  che  *37,*  la variabile MainClass_C1_variabile_V8 sia  uguale a  *53,* 4
    //   } Verifica che   *52,*   l'argomento argomento_ave7 non  sia  diverso da c180 *,* 
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetMainc24(my_id) == true));
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_NotLogicOP_4);
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (argom18 == c180));
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_NotLogicOP_5);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    res_OrLogicOP_2 = (res_OrLogicOP_2 || (L_P1__GetMainc24(my_id) == true));
    
    if(res_OrLogicOP_2){
    bool res_AndLogicOP_6 = true;
    bool res_ImpliesLogicOp_7 = true;
    if(Timer_Scaduto(L_P1__GetMainc29(my_id))){
    bool res_XorLogicOP_8 = true;
    int xorIndex_res_XorLogicOP_8 = 0;
    bool res_ImpliesLogicOp_9 = true;
    bool res_AndLogicOP_10 = true;
    res_AndLogicOP_10 = (res_AndLogicOP_10 && (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (L_P1__GetInMainc4(my_id) == c270));
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_NotLogicOP_11);
    
    if(res_AndLogicOP_10){
    bool res_OrLogicOP_12 = false;
    bool res_ImpliesLogicOp_13 = true;
    if((L_P1__GetMainc24(my_id) == false)){
    bool res_ImpliesLogicOp_14 = true;
    bool res_OrLogicOP_15 = false;
    bool res_OrLogicOP_16 = false;
    bool res_OrLogicOP_17 = false;
    bool res_AndLogicOP_18 = true;
    bool res_AndLogicOP_19 = true;
    res_AndLogicOP_19 = (res_AndLogicOP_19 && Timer_Disattivo(L_P1__GetMainc29(my_id)));
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! (L_P1__GetInMainc4(my_id) == c270));
    res_AndLogicOP_19 = (res_AndLogicOP_19 && res_NotLogicOP_20);
    
    res_AndLogicOP_18 = (res_AndLogicOP_18 && res_AndLogicOP_19);
    bool res_NotLogicOP_21 = true;
    bool res_NotLogicOP_22 = true;
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! (L_P1__GetMainc24(my_id) == true));
    res_NotLogicOP_21 = (res_NotLogicOP_21 && ! res_NotLogicOP_22);
    res_AndLogicOP_18 = (res_AndLogicOP_18 && res_NotLogicOP_21);
    
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_AndLogicOP_18);
    bool res_NotLogicOP_23 = true;
    bool res_NotLogicOP_24 = true;
    res_NotLogicOP_24 = (res_NotLogicOP_24 && ! (L_P1__GetParamMainc9(my_id) == c180));
    res_NotLogicOP_23 = (res_NotLogicOP_23 && ! res_NotLogicOP_24);
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_NotLogicOP_23);
    
    res_OrLogicOP_16 = (res_OrLogicOP_16 || res_OrLogicOP_17);
    bool res_NotLogicOP_25 = true;
    bool res_NotLogicOP_26 = true;
    res_NotLogicOP_26 = (res_NotLogicOP_26 && ! (L_P1__GetInMainc6(my_id) == false));
    res_NotLogicOP_25 = (res_NotLogicOP_25 && ! res_NotLogicOP_26);
    res_OrLogicOP_16 = (res_OrLogicOP_16 || res_NotLogicOP_25);
    
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_OrLogicOP_16);
    bool res_NotLogicOP_27 = true;
    res_NotLogicOP_27 = (res_NotLogicOP_27 && ! (L_P1__GetInMainc8(my_id) == c270));
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_NotLogicOP_27);
    
    if(res_OrLogicOP_15){
    bool res_OrLogicOP_28 = false;
    bool res_OrLogicOP_29 = false;
    bool res_NotLogicOP_30 = true;
    res_NotLogicOP_30 = (res_NotLogicOP_30 && ! Timer_Disattivo(L_P1__GetMainc30(my_id)));
    res_OrLogicOP_29 = (res_OrLogicOP_29 || res_NotLogicOP_30);
    bool res_NotLogicOP_31 = true;
    bool res_NotLogicOP_32 = true;
    res_NotLogicOP_32 = (res_NotLogicOP_32 && ! (argom18 == c180));
    res_NotLogicOP_31 = (res_NotLogicOP_31 && ! res_NotLogicOP_32);
    res_OrLogicOP_29 = (res_OrLogicOP_29 || res_NotLogicOP_31);
    
    res_OrLogicOP_28 = (res_OrLogicOP_28 || res_OrLogicOP_29);
    res_OrLogicOP_28 = (res_OrLogicOP_28 || (L_P1__GetMainc24(my_id) == false));
    
    res_ImpliesLogicOp_14 = (res_ImpliesLogicOp_14 && res_OrLogicOP_28);
    }
    res_ImpliesLogicOp_13 = (res_ImpliesLogicOp_13 && res_ImpliesLogicOp_14);
    }
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_ImpliesLogicOp_13);
    bool res_OrLogicOP_33 = false;
    bool res_AndLogicOP_34 = true;
    bool res_NotLogicOP_35 = true;
    bool res_NotLogicOP_36 = true;
    res_NotLogicOP_36 = (res_NotLogicOP_36 && ! (Counter_GetValore(L_P1__GetMainc32(my_id)) == 1504u));
    res_NotLogicOP_35 = (res_NotLogicOP_35 && ! res_NotLogicOP_36);
    res_AndLogicOP_34 = (res_AndLogicOP_34 && res_NotLogicOP_35);
    bool res_NotLogicOP_37 = true;
    res_NotLogicOP_37 = (res_NotLogicOP_37 && ! (L_P1__GetInMainc4(my_id) == c270));
    res_AndLogicOP_34 = (res_AndLogicOP_34 && res_NotLogicOP_37);
    
    res_OrLogicOP_33 = (res_OrLogicOP_33 || res_AndLogicOP_34);
    bool res_AndLogicOP_38 = true;
    bool res_AndLogicOP_39 = true;
    bool res_NotLogicOP_40 = true;
    res_NotLogicOP_40 = (res_NotLogicOP_40 && ! (argom18 == c180));
    res_AndLogicOP_39 = (res_AndLogicOP_39 && res_NotLogicOP_40);
    bool res_NotLogicOP_41 = true;
    res_NotLogicOP_41 = (res_NotLogicOP_41 && ! (argom18 == c180));
    res_AndLogicOP_39 = (res_AndLogicOP_39 && res_NotLogicOP_41);
    
    res_AndLogicOP_38 = (res_AndLogicOP_38 && res_AndLogicOP_39);
    res_AndLogicOP_38 = (res_AndLogicOP_38 && (L_P1__GetParamMainc11(my_id) == verde));
    
    res_OrLogicOP_33 = (res_OrLogicOP_33 || res_AndLogicOP_38);
    
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_OrLogicOP_33);
    
    res_ImpliesLogicOp_9 = (res_ImpliesLogicOp_9 && res_OrLogicOP_12);
    }
    if(res_ImpliesLogicOp_9){
    xorIndex_res_XorLogicOP_8 = (xorIndex_res_XorLogicOP_8 + 1);
    }
    bool res_OrLogicOP_42 = false;
    bool res_OrLogicOP_43 = false;
    bool res_AndLogicOP_44 = true;
    bool res_NotLogicOP_45 = true;
    res_NotLogicOP_45 = (res_NotLogicOP_45 && ! (L_P1__GetMainc24(my_id) == false));
    res_AndLogicOP_44 = (res_AndLogicOP_44 && res_NotLogicOP_45);
    bool res_NotLogicOP_46 = true;
    bool res_NotLogicOP_47 = true;
    res_NotLogicOP_47 = (res_NotLogicOP_47 && ! (L_P1__GetMainc24(my_id) == true));
    res_NotLogicOP_46 = (res_NotLogicOP_46 && ! res_NotLogicOP_47);
    res_AndLogicOP_44 = (res_AndLogicOP_44 && res_NotLogicOP_46);
    
    res_OrLogicOP_43 = (res_OrLogicOP_43 || res_AndLogicOP_44);
    bool res_NotLogicOP_48 = true;
    bool res_NotLogicOP_49 = true;
    res_NotLogicOP_49 = (res_NotLogicOP_49 && ! (L_P1__GetParamMainc10(my_id) == false));
    res_NotLogicOP_48 = (res_NotLogicOP_48 && ! res_NotLogicOP_49);
    res_OrLogicOP_43 = (res_OrLogicOP_43 || res_NotLogicOP_48);
    
    res_OrLogicOP_42 = (res_OrLogicOP_42 || res_OrLogicOP_43);
    bool res_AndLogicOP_50 = true;
    res_AndLogicOP_50 = (res_AndLogicOP_50 && (L_P1__GetParamMainc11(my_id) == verde));
    res_AndLogicOP_50 = (res_AndLogicOP_50 && (L_P1__GetMainc27(my_id) == 4u));
    
    res_OrLogicOP_42 = (res_OrLogicOP_42 || res_AndLogicOP_50);
    
    if(res_OrLogicOP_42){
    xorIndex_res_XorLogicOP_8 = (xorIndex_res_XorLogicOP_8 + 1);
    }
    
    res_XorLogicOP_8 = (res_XorLogicOP_8 && (xorIndex_res_XorLogicOP_8 == 1));
    res_ImpliesLogicOp_7 = (res_ImpliesLogicOp_7 && res_XorLogicOP_8);
    }
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_ImpliesLogicOp_7);
    bool res_NotLogicOP_51 = true;
    bool res_NotLogicOP_52 = true;
    res_NotLogicOP_52 = (res_NotLogicOP_52 && ! (argom18 == c180));
    res_NotLogicOP_51 = (res_NotLogicOP_51 && ! res_NotLogicOP_52);
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_51);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_AndLogicOP_6);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *48,49,*  *,*  il timer MainClass_C1_timer_T8 non sia attivo
    //   *104,* o  che  *,*  il controllo MainClass_C1_controllo_C5 sia  diverso da  True
    bool res_OrLogicOP_53 = false;
    bool res_NotLogicOP_54 = true;
    res_NotLogicOP_54 = (res_NotLogicOP_54 && ! Timer_Attivo(L_P1__GetMainc30(my_id)));
    res_OrLogicOP_53 = (res_OrLogicOP_53 || res_NotLogicOP_54);
    bool res_NotLogicOP_55 = true;
    res_NotLogicOP_55 = (res_NotLogicOP_55 && ! (L_P1__GetInMainc6(my_id) == true));
    res_OrLogicOP_53 = (res_OrLogicOP_53 || res_NotLogicOP_55);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_53);
    
    
    
    return res_AndLogicOP_0;
}


// Macro valorizzate

/*
    CNL corrispondente:
    
    { commento: {[}
     commento: {46,} assegna alla macro il valore  True  commento: {],}
    }
*/
bool L_P1__Macro3(instance_id_t const my_id , C1_Enumerat3 argom10, bool argom11)
{
return true;
}



