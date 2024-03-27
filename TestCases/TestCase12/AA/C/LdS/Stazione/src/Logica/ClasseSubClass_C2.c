// Codice del modello 'TestCase12', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#include "Logica/ClasseMainClass_C1.h"
#include "Logica/ClasseSubClass_C2.h"
#include "Logica/ClasseSubClass_C3.h"
#include "Logica/ClasseSubClass_C2_priv.h"
#include "config.h"
#include "scheduler.h"


// ********** Definizione guardie **********

/*
    CNL corrispondente:
    
     {
     Nessuna 
     }
*/
static inline bool L_P1__Guard2(instance_id_t const my_id)
{
    return true;
}


/*
    CNL corrispondente:
    
    {
    
     commento: {69,} commento: {37,}  se la variabile SubClass_C2_variabile_V3 è  maggiore di  commento: {54,} 8 commento: {36,} o  se il timer SubClass_C2_timer_T9 non è scaduto, Solo una delle seguenti { 
     commento: {36,}  se il timer SubClass_C2_timer_T9 non è scaduto commento: {34,} e  se il parametro SubClass_C2_parametro_P6 non è  diverso da  False  commento: {34,} o  se il parametro SubClass_C2_parametro_P6 è  uguale a  False  commento: {38,} o  se il contatore SubClass_C2_contatore_Co7 è  diverso da  commento: {56,} 1151 commento: {35,} o  se il controllo SubClass_C2_controllo_C8 è  uguale a  False , Verifica che   commento: {50,}  commento: {,}  la variabile SubClass_C2_variabile_V3 sia  uguale a  commento: {53,} 6
    
    
     } Verifica che   commento: {47,}  commento: {34,}  il parametro SubClass_C2_parametro_P8 non sia  uguale a  commento: {53,} 10
    
    
    }
*/
static inline bool L_P1__Guard3(instance_id_t const my_id)
{
    bool res_AndLogicOP_0 = true;
    
    //  *69,* *37,*  se la variabile SubClass_C2_variabile_V3 è  maggiore di  *54,* 8 *36,* o  se il timer SubClass_C2_timer_T9 non è scaduto, Solo una delle seguenti { 
    //   *36,*  se il timer SubClass_C2_timer_T9 non è scaduto *34,* e  se il parametro SubClass_C2_parametro_P6 non è  diverso da  False  *34,* o  se il parametro SubClass_C2_parametro_P6 è  uguale a  False  *38,* o  se il contatore SubClass_C2_contatore_Co7 è  diverso da  *56,* 1151 *35,* o  se il controllo SubClass_C2_controllo_C8 è  uguale a  False , Verifica che   *50,*  *,*  la variabile SubClass_C2_variabile_V3 sia  uguale a  *53,* 6
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    res_OrLogicOP_2 = (res_OrLogicOP_2 || (L_P1__GetSubcl28(my_id) > 8u));
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! Timer_Scaduto(L_P1__GetSubcl40(my_id)));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_3);
    
    if(res_OrLogicOP_2){
    bool res_ImpliesLogicOp_4 = true;
    bool res_OrLogicOP_5 = false;
    bool res_OrLogicOP_6 = false;
    bool res_OrLogicOP_7 = false;
    bool res_AndLogicOP_8 = true;
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! Timer_Scaduto(L_P1__GetSubcl40(my_id)));
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_9);
    bool res_NotLogicOP_10 = true;
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (L_P1__GetParamSubcl11(my_id) == false));
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! res_NotLogicOP_11);
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_10);
    
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_AndLogicOP_8);
    res_OrLogicOP_7 = (res_OrLogicOP_7 || (L_P1__GetParamSubcl11(my_id) == false));
    
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_OrLogicOP_7);
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (Counter_GetValore(L_P1__GetSubcl42(my_id)) == 1151u));
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_NotLogicOP_12);
    
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_OrLogicOP_6);
    res_OrLogicOP_5 = (res_OrLogicOP_5 || (L_P1__GetInSubcl6(my_id) == false));
    
    if(res_OrLogicOP_5){
    res_ImpliesLogicOp_4 = (res_ImpliesLogicOp_4 && (L_P1__GetSubcl28(my_id) == 6u));
    }
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_ImpliesLogicOp_4);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *47,*  *34,*  il parametro SubClass_C2_parametro_P8 non sia  uguale a  *53,* 10
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (L_P1__GetParamSubcl12(my_id) == 10u));
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_NotLogicOP_13);
    
    
    
    return res_AndLogicOP_0;
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
     {  Nessuna  }
*/
static inline bool L_P1__Guard5(instance_id_t const my_id)
{
    return true;
}


/*
    CNL corrispondente:
     {  commento: {69,} commento: {36,}  se il timer SubClass_C2_timer_T9 è attivo commento: {36,} o  se il timer SubClass_C2_timer_T1 non è disattivo e  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} o  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  commento: {54,} 1 e  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} e  se il controllo SubClass_C2_controllo_C8 è  uguale a  False , Solo una delle seguenti { 
     commento: {68,} commento: {34,}  se il parametro SubClass_C2_parametro_P8 è  uguale a  commento: {53,} 7 commento: {35,} e  se il controllo SubClass_C2_controllo_C8 è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
     commento: {37,}  se la variabile SubClass_C2_variabile_V2 non è  uguale a  True , Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
    
    
     } Verifica che   commento: {49,}  commento: {,}  il timer SubClass_C2_timer_T1 non sia attivo
    
    
     } Verifica che   commento: {49,}  commento: {,}  il timer SubClass_C2_timer_T9 non sia scaduto
    
     }
*/
static inline bool L_P1__Guard6(instance_id_t const my_id)
{
    bool res_AndLogicOP_0 = true;
    
    //  *69,* *36,*  se il timer SubClass_C2_timer_T9 è attivo *36,* o  se il timer SubClass_C2_timer_T1 non è disattivo e  se il controllo ConsDef  è  uguale a FALSE  *34,* o  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  *54,* 1 e  se il controllo ConsDef  è  uguale a FALSE  *35,* e  se il controllo SubClass_C2_controllo_C8 è  uguale a  False , Solo una delle seguenti { 
    //   *68,* *34,*  se il parametro SubClass_C2_parametro_P8 è  uguale a  *53,* 7 *35,* e  se il controllo SubClass_C2_controllo_C8 è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
    //   *37,*  se la variabile SubClass_C2_variabile_V2 non è  uguale a  True , Verifica che   *48,*   il controllo ConsDef  sia  uguale a FALSE 
    //   } Verifica che   *49,*  *,*  il timer SubClass_C2_timer_T1 non sia attivo
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    res_OrLogicOP_3 = (res_OrLogicOP_3 || Timer_Attivo(L_P1__GetSubcl40(my_id)));
    bool res_AndLogicOP_4 = true;
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! Timer_Disattivo(L_P1__GetSubcl38(my_id)));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_5);
    res_AndLogicOP_4 = (res_AndLogicOP_4 && (L_P1__GetInConsd1(my_id) == false));
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_AndLogicOP_4);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    bool res_AndLogicOP_6 = true;
    bool res_AndLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetParamSubcl12(my_id) > 1u));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_8);
    res_AndLogicOP_7 = (res_AndLogicOP_7 && (L_P1__GetInConsd1(my_id) == false));
    
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_AndLogicOP_7);
    res_AndLogicOP_6 = (res_AndLogicOP_6 && (L_P1__GetInSubcl6(my_id) == false));
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_6);
    
    if(res_OrLogicOP_2){
    bool res_XorLogicOP_9 = true;
    int xorIndex_res_XorLogicOP_9 = 0;
    bool res_ImpliesLogicOp_10 = true;
    bool res_OrLogicOP_11 = false;
    bool res_AndLogicOP_12 = true;
    res_AndLogicOP_12 = (res_AndLogicOP_12 && (L_P1__GetParamSubcl12(my_id) == 7u));
    res_AndLogicOP_12 = (res_AndLogicOP_12 && (L_P1__GetInSubcl6(my_id) == false));
    
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_AndLogicOP_12);
    res_OrLogicOP_11 = (res_OrLogicOP_11 || (L_P1__GetInConsd1(my_id) == false));
    
    if(res_OrLogicOP_11){
    bool res_ImpliesLogicOp_13 = true;
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1__GetSubcl27(my_id) == true));
    if(res_NotLogicOP_14){
    res_ImpliesLogicOp_13 = (res_ImpliesLogicOp_13 && (L_P1__GetInConsd1(my_id) == false));
    }
    res_ImpliesLogicOp_10 = (res_ImpliesLogicOp_10 && res_ImpliesLogicOp_13);
    }
    if(res_ImpliesLogicOp_10){
    xorIndex_res_XorLogicOP_9 = (xorIndex_res_XorLogicOP_9 + 1);
    }
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! Timer_Attivo(L_P1__GetSubcl38(my_id)));
    if(res_NotLogicOP_15){
    xorIndex_res_XorLogicOP_9 = (xorIndex_res_XorLogicOP_9 + 1);
    }
    
    res_XorLogicOP_9 = (res_XorLogicOP_9 && (xorIndex_res_XorLogicOP_9 == 1));
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_XorLogicOP_9);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *49,*  *,*  il timer SubClass_C2_timer_T9 non sia scaduto
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! Timer_Scaduto(L_P1__GetSubcl40(my_id)));
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_NotLogicOP_16);
    
    
    
    return res_AndLogicOP_0;
}


/*
    CNL corrispondente:
     {  Nessuna  commento: {80,} }
*/
static inline bool L_P1__Guard7(instance_id_t const my_id)
{
    return true;
}


/*
    CNL corrispondente:
     {  Nessuna  commento: {80,} }
*/
static inline bool L_P1__Guard8(instance_id_t const my_id)
{
    return true;
}


/*
    CNL corrispondente:
     {  Nessuna  }
*/
static inline bool L_P1__Guard9(instance_id_t const my_id)
{
    return true;
}


/*
    CNL corrispondente:
    
    {
    
     Nessuna 
    }
*/
static inline bool L_P1__Guard10(instance_id_t const my_id)
{
    return true;
}


/*
    CNL corrispondente:
    
    {
    
     commento: {67,} commento: {38,}  se il contatore SubClass_C2_contatore_Co7 è  minore di  commento: {55,} 13 commento: {36,} e  se il timer SubClass_C2_timer_T9 non è attivo commento: {38,} o  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  commento: {56,} 12230 commento: {38,} o  se il contatore SubClass_C2_contatore_Co7 è  uguale a  commento: {53,} 11451 commento: {38,} e  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  commento: {56,} 132 commento: {35,} o  se il controllo SubClass_C2_controllo_C1 è  uguale a avanzamentox, Tutte le seguenti { 
     commento: {67,} commento: {36,}  se il timer SubClass_C2_timer_T8 è disattivo o  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro SubClass_C2_parametro_P8 non è  minore di  commento: {55,} 8 o  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} e  se la variabile SubClass_C2_variabile_V6 non è  uguale a GialloxVerdex, Tutte le seguenti { 
     commento: {69,} commento: {36,}  se il timer SubClass_C2_timer_T1 non è disattivo commento: {36,} o  se il timer SubClass_C2_timer_T8 è attivo commento: {35,} e  se il controllo SubClass_C2_controllo_C5 è  uguale a avanzamentox, Solo una delle seguenti { 
     commento: {69,}  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} o  se il timer SubClass_C2_timer_T9 è scaduto, Solo una delle seguenti { 
     commento: {69,} commento: {34,}  se il parametro SubClass_C2_parametro_P5 è  uguale a avanzamentox commento: {36,} o  se il timer SubClass_C2_timer_T8 è disattivo o  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} e  se la variabile SubClass_C2_variabile_V3 non è  minore di  commento: {55,} 6 commento: {37,} o  se la variabile SubClass_C2_variabile_V6 è  uguale a GialloxVerdex commento: {37,} e  se la variabile SubClass_C2_variabile_V6 non è  uguale a GialloxVerdex, Solo una delle seguenti { 
     commento: {69,} commento: {36,}  se il timer SubClass_C2_timer_T1 è attivo commento: {36,} e  se il timer SubClass_C2_timer_T9 è attivo, Solo una delle seguenti { 
     commento: {67,} commento: {36,}  se il timer SubClass_C2_timer_T1 è disattivo commento: {35,} e  se il controllo SubClass_C2_controllo_C8 è  diverso da  False  commento: {36,} e  se il timer SubClass_C2_timer_T1 è attivo, Tutte le seguenti { 
     commento: {69,} commento: {38,}  se il contatore SubClass_C2_contatore_Co7 è  uguale a  commento: {53,} 11 commento: {36,} o  se il timer SubClass_C2_timer_T8 non è attivo commento: {36,} o  se il timer SubClass_C2_timer_T9 non è attivo, Solo una delle seguenti { 
     commento: {67,} commento: {37,}  se la variabile SubClass_C2_variabile_V6 non è  diverso da GialloxVerdex commento: {38,} o  se il contatore SubClass_C2_contatore_Co7 non è  maggiore di  commento: {54,} 1530 commento: {37,} e  se la variabile SubClass_C2_variabile_V3 è  uguale a  commento: {53,} 6 commento: {38,} e  se il contatore SubClass_C2_contatore_Co1 non è  uguale a  commento: {53,} 11 commento: {34,} o  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  commento: {54,} 4, Tutte le seguenti { 
     commento: {37,}  se la variabile SubClass_C2_variabile_V3 non è  maggiore di  commento: {54,} 6 commento: {36,} o  se il timer SubClass_C2_timer_T9 è disattivo, Verifica che   commento: {50,}  commento: {,}  la variabile SubClass_C2_variabile_V3 non sia  minore di  commento: {55,} 10
    
    
     } Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
    
    
     } Verifica che   commento: {47,}  commento: {34,}  il parametro SubClass_C2_parametro_P5 sia  uguale a avanzamentox
    
    
     } Verifica che   commento: {47,}  commento: {34,}  il parametro SubClass_C2_parametro_P6 sia  uguale a  False 
    
    
     } Verifica che   commento: {51,}  commento: {,}  il contatore SubClass_C2_contatore_Co7 non sia  minore di  commento: {55,} 15
    
    
     } Verifica che   commento: {50,}  commento: {,}  la variabile SubClass_C2_variabile_V3 non sia  maggiore di  commento: {54,} 6
    
    
     } Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
    
    
     } Verifica che   commento: {49,}  commento: {,}  il timer SubClass_C2_timer_T8 non sia scaduto
    
    
     } Verifica che   commento: {48,}  commento: {,}  il controllo SubClass_C2_controllo_C8 sia  uguale a  True 
    
    
     } Verifica che   commento: {47,}  commento: {34,}  il parametro SubClass_C2_parametro_P5 sia  uguale a avanzamentox
    
    
    }
*/
static inline bool L_P1__Guard11(instance_id_t const my_id)
{
    bool res_AndLogicOP_0 = true;
    
    //  *67,* *38,*  se il contatore SubClass_C2_contatore_Co7 è  minore di  *55,* 13 *36,* e  se il timer SubClass_C2_timer_T9 non è attivo *38,* o  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  *56,* 12230 *38,* o  se il contatore SubClass_C2_contatore_Co7 è  uguale a  *53,* 11451 *38,* e  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  *56,* 132 *35,* o  se il controllo SubClass_C2_controllo_C1 è  uguale a avanzamentox, Tutte le seguenti { 
    //   *67,* *36,*  se il timer SubClass_C2_timer_T8 è disattivo o  se il controllo ConsDef  è  uguale a FALSE  *34,* e  se il parametro SubClass_C2_parametro_P8 non è  minore di  *55,* 8 o  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  *37,* e  se la variabile SubClass_C2_variabile_V6 non è  uguale a GialloxVerdex, Tutte le seguenti { 
    //   *69,* *36,*  se il timer SubClass_C2_timer_T1 non è disattivo *36,* o  se il timer SubClass_C2_timer_T8 è attivo *35,* e  se il controllo SubClass_C2_controllo_C5 è  uguale a avanzamentox, Solo una delle seguenti { 
    //   *69,*  se il controllo ConsDef  è  uguale a FALSE  *36,* o  se il timer SubClass_C2_timer_T9 è scaduto, Solo una delle seguenti { 
    //   *69,* *34,*  se il parametro SubClass_C2_parametro_P5 è  uguale a avanzamentox *36,* o  se il timer SubClass_C2_timer_T8 è disattivo o  se il controllo ConsDef  è  uguale a FALSE  *37,* e  se la variabile SubClass_C2_variabile_V3 non è  minore di  *55,* 6 *37,* o  se la variabile SubClass_C2_variabile_V6 è  uguale a GialloxVerdex *37,* e  se la variabile SubClass_C2_variabile_V6 non è  uguale a GialloxVerdex, Solo una delle seguenti { 
    //   *69,* *36,*  se il timer SubClass_C2_timer_T1 è attivo *36,* e  se il timer SubClass_C2_timer_T9 è attivo, Solo una delle seguenti { 
    //   *67,* *36,*  se il timer SubClass_C2_timer_T1 è disattivo *35,* e  se il controllo SubClass_C2_controllo_C8 è  diverso da  False  *36,* e  se il timer SubClass_C2_timer_T1 è attivo, Tutte le seguenti { 
    //   *69,* *38,*  se il contatore SubClass_C2_contatore_Co7 è  uguale a  *53,* 11 *36,* o  se il timer SubClass_C2_timer_T8 non è attivo *36,* o  se il timer SubClass_C2_timer_T9 non è attivo, Solo una delle seguenti { 
    //   *67,* *37,*  se la variabile SubClass_C2_variabile_V6 non è  diverso da GialloxVerdex *38,* o  se il contatore SubClass_C2_contatore_Co7 non è  maggiore di  *54,* 1530 *37,* e  se la variabile SubClass_C2_variabile_V3 è  uguale a  *53,* 6 *38,* e  se il contatore SubClass_C2_contatore_Co1 non è  uguale a  *53,* 11 *34,* o  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  *54,* 4, Tutte le seguenti { 
    //   *37,*  se la variabile SubClass_C2_variabile_V3 non è  maggiore di  *54,* 6 *36,* o  se il timer SubClass_C2_timer_T9 è disattivo, Verifica che   *50,*  *,*  la variabile SubClass_C2_variabile_V3 non sia  minore di  *55,* 10
    //   } Verifica che   *48,*   il controllo ConsDef  sia  uguale a FALSE 
    //   } Verifica che   *47,*  *34,*  il parametro SubClass_C2_parametro_P5 sia  uguale a avanzamentox
    //   } Verifica che   *47,*  *34,*  il parametro SubClass_C2_parametro_P6 sia  uguale a  False 
    //   } Verifica che   *51,*  *,*  il contatore SubClass_C2_contatore_Co7 non sia  minore di  *55,* 15
    //   } Verifica che   *50,*  *,*  la variabile SubClass_C2_variabile_V3 non sia  maggiore di  *54,* 6
    //   } Verifica che   *48,*   il controllo ConsDef  sia  uguale a FALSE 
    //   } Verifica che   *49,*  *,*  il timer SubClass_C2_timer_T8 non sia scaduto
    //   } Verifica che   *48,*  *,*  il controllo SubClass_C2_controllo_C8 sia  uguale a  True 
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_OrLogicOP_4 = false;
    bool res_AndLogicOP_5 = true;
    res_AndLogicOP_5 = (res_AndLogicOP_5 && (Counter_GetValore(L_P1__GetSubcl42(my_id)) < 13u));
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! Timer_Attivo(L_P1__GetSubcl40(my_id)));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_6);
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_AndLogicOP_5);
    bool res_NotLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (Counter_GetValore(L_P1__GetSubcl42(my_id)) == 12230u));
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! res_NotLogicOP_8);
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_NotLogicOP_7);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_OrLogicOP_4);
    bool res_AndLogicOP_9 = true;
    res_AndLogicOP_9 = (res_AndLogicOP_9 && (Counter_GetValore(L_P1__GetSubcl42(my_id)) == 11451u));
    bool res_NotLogicOP_10 = true;
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (Counter_GetValore(L_P1__GetSubcl42(my_id)) == 132u));
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! res_NotLogicOP_11);
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_NotLogicOP_10);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_AndLogicOP_9);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    res_OrLogicOP_2 = (res_OrLogicOP_2 || (L_P1__GetInSubcl2(my_id) == avanzamento1));
    
    if(res_OrLogicOP_2){
    bool res_AndLogicOP_12 = true;
    bool res_ImpliesLogicOp_13 = true;
    bool res_OrLogicOP_14 = false;
    bool res_OrLogicOP_15 = false;
    res_OrLogicOP_15 = (res_OrLogicOP_15 || Timer_Disattivo(L_P1__GetSubcl39(my_id)));
    bool res_AndLogicOP_16 = true;
    res_AndLogicOP_16 = (res_AndLogicOP_16 && (L_P1__GetInConsd1(my_id) == false));
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! (L_P1__GetParamSubcl12(my_id) < 8u));
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_NotLogicOP_17);
    
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_AndLogicOP_16);
    
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_OrLogicOP_15);
    bool res_AndLogicOP_18 = true;
    bool res_AndLogicOP_19 = true;
    res_AndLogicOP_19 = (res_AndLogicOP_19 && (L_P1__GetInConsd1(my_id) == false));
    res_AndLogicOP_19 = (res_AndLogicOP_19 && (L_P1__GetInConsd1(my_id) == false));
    
    res_AndLogicOP_18 = (res_AndLogicOP_18 && res_AndLogicOP_19);
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! (L_P1__GetSubcl29(my_id) == gialloxverd));
    res_AndLogicOP_18 = (res_AndLogicOP_18 && res_NotLogicOP_20);
    
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_AndLogicOP_18);
    
    if(res_OrLogicOP_14){
    bool res_AndLogicOP_21 = true;
    bool res_ImpliesLogicOp_22 = true;
    bool res_OrLogicOP_23 = false;
    bool res_NotLogicOP_24 = true;
    res_NotLogicOP_24 = (res_NotLogicOP_24 && ! Timer_Disattivo(L_P1__GetSubcl38(my_id)));
    res_OrLogicOP_23 = (res_OrLogicOP_23 || res_NotLogicOP_24);
    bool res_AndLogicOP_25 = true;
    res_AndLogicOP_25 = (res_AndLogicOP_25 && Timer_Attivo(L_P1__GetSubcl39(my_id)));
    res_AndLogicOP_25 = (res_AndLogicOP_25 && (L_P1__GetInSubcl5(my_id) == avanzamento1));
    
    res_OrLogicOP_23 = (res_OrLogicOP_23 || res_AndLogicOP_25);
    
    if(res_OrLogicOP_23){
    bool res_XorLogicOP_26 = true;
    int xorIndex_res_XorLogicOP_26 = 0;
    bool res_ImpliesLogicOp_27 = true;
    bool res_OrLogicOP_28 = false;
    res_OrLogicOP_28 = (res_OrLogicOP_28 || (L_P1__GetInConsd1(my_id) == false));
    res_OrLogicOP_28 = (res_OrLogicOP_28 || Timer_Scaduto(L_P1__GetSubcl40(my_id)));
    
    if(res_OrLogicOP_28){
    bool res_XorLogicOP_29 = true;
    int xorIndex_res_XorLogicOP_29 = 0;
    bool res_ImpliesLogicOp_30 = true;
    bool res_OrLogicOP_31 = false;
    bool res_OrLogicOP_32 = false;
    bool res_OrLogicOP_33 = false;
    res_OrLogicOP_33 = (res_OrLogicOP_33 || (L_P1__GetParamSubcl10(my_id) == avanzamento1));
    res_OrLogicOP_33 = (res_OrLogicOP_33 || Timer_Disattivo(L_P1__GetSubcl39(my_id)));
    
    res_OrLogicOP_32 = (res_OrLogicOP_32 || res_OrLogicOP_33);
    bool res_AndLogicOP_34 = true;
    res_AndLogicOP_34 = (res_AndLogicOP_34 && (L_P1__GetInConsd1(my_id) == false));
    bool res_NotLogicOP_35 = true;
    res_NotLogicOP_35 = (res_NotLogicOP_35 && ! (L_P1__GetSubcl28(my_id) < 6u));
    res_AndLogicOP_34 = (res_AndLogicOP_34 && res_NotLogicOP_35);
    
    res_OrLogicOP_32 = (res_OrLogicOP_32 || res_AndLogicOP_34);
    
    res_OrLogicOP_31 = (res_OrLogicOP_31 || res_OrLogicOP_32);
    bool res_AndLogicOP_36 = true;
    res_AndLogicOP_36 = (res_AndLogicOP_36 && (L_P1__GetSubcl29(my_id) == gialloxverd));
    bool res_NotLogicOP_37 = true;
    res_NotLogicOP_37 = (res_NotLogicOP_37 && ! (L_P1__GetSubcl29(my_id) == gialloxverd));
    res_AndLogicOP_36 = (res_AndLogicOP_36 && res_NotLogicOP_37);
    
    res_OrLogicOP_31 = (res_OrLogicOP_31 || res_AndLogicOP_36);
    
    if(res_OrLogicOP_31){
    bool res_XorLogicOP_38 = true;
    int xorIndex_res_XorLogicOP_38 = 0;
    bool res_ImpliesLogicOp_39 = true;
    bool res_AndLogicOP_40 = true;
    res_AndLogicOP_40 = (res_AndLogicOP_40 && Timer_Attivo(L_P1__GetSubcl38(my_id)));
    res_AndLogicOP_40 = (res_AndLogicOP_40 && Timer_Attivo(L_P1__GetSubcl40(my_id)));
    
    if(res_AndLogicOP_40){
    bool res_XorLogicOP_41 = true;
    int xorIndex_res_XorLogicOP_41 = 0;
    bool res_ImpliesLogicOp_42 = true;
    bool res_AndLogicOP_43 = true;
    bool res_AndLogicOP_44 = true;
    res_AndLogicOP_44 = (res_AndLogicOP_44 && Timer_Disattivo(L_P1__GetSubcl38(my_id)));
    bool res_NotLogicOP_45 = true;
    res_NotLogicOP_45 = (res_NotLogicOP_45 && ! (L_P1__GetInSubcl6(my_id) == false));
    res_AndLogicOP_44 = (res_AndLogicOP_44 && res_NotLogicOP_45);
    
    res_AndLogicOP_43 = (res_AndLogicOP_43 && res_AndLogicOP_44);
    res_AndLogicOP_43 = (res_AndLogicOP_43 && Timer_Attivo(L_P1__GetSubcl38(my_id)));
    
    if(res_AndLogicOP_43){
    bool res_AndLogicOP_46 = true;
    bool res_ImpliesLogicOp_47 = true;
    bool res_OrLogicOP_48 = false;
    bool res_OrLogicOP_49 = false;
    res_OrLogicOP_49 = (res_OrLogicOP_49 || (Counter_GetValore(L_P1__GetSubcl42(my_id)) == 11u));
    bool res_NotLogicOP_50 = true;
    res_NotLogicOP_50 = (res_NotLogicOP_50 && ! Timer_Attivo(L_P1__GetSubcl39(my_id)));
    res_OrLogicOP_49 = (res_OrLogicOP_49 || res_NotLogicOP_50);
    
    res_OrLogicOP_48 = (res_OrLogicOP_48 || res_OrLogicOP_49);
    bool res_NotLogicOP_51 = true;
    res_NotLogicOP_51 = (res_NotLogicOP_51 && ! Timer_Attivo(L_P1__GetSubcl40(my_id)));
    res_OrLogicOP_48 = (res_OrLogicOP_48 || res_NotLogicOP_51);
    
    if(res_OrLogicOP_48){
    bool res_XorLogicOP_52 = true;
    int xorIndex_res_XorLogicOP_52 = 0;
    bool res_ImpliesLogicOp_53 = true;
    bool res_OrLogicOP_54 = false;
    bool res_OrLogicOP_55 = false;
    bool res_NotLogicOP_56 = true;
    bool res_NotLogicOP_57 = true;
    res_NotLogicOP_57 = (res_NotLogicOP_57 && ! (L_P1__GetSubcl29(my_id) == gialloxverd));
    res_NotLogicOP_56 = (res_NotLogicOP_56 && ! res_NotLogicOP_57);
    res_OrLogicOP_55 = (res_OrLogicOP_55 || res_NotLogicOP_56);
    bool res_AndLogicOP_58 = true;
    bool res_AndLogicOP_59 = true;
    bool res_NotLogicOP_60 = true;
    res_NotLogicOP_60 = (res_NotLogicOP_60 && ! (Counter_GetValore(L_P1__GetSubcl42(my_id)) > 1530u));
    res_AndLogicOP_59 = (res_AndLogicOP_59 && res_NotLogicOP_60);
    res_AndLogicOP_59 = (res_AndLogicOP_59 && (L_P1__GetSubcl28(my_id) == 6u));
    
    res_AndLogicOP_58 = (res_AndLogicOP_58 && res_AndLogicOP_59);
    bool res_NotLogicOP_61 = true;
    res_NotLogicOP_61 = (res_NotLogicOP_61 && ! (Counter_GetValore(L_P1__GetSubcl41(my_id)) == 11u));
    res_AndLogicOP_58 = (res_AndLogicOP_58 && res_NotLogicOP_61);
    
    res_OrLogicOP_55 = (res_OrLogicOP_55 || res_AndLogicOP_58);
    
    res_OrLogicOP_54 = (res_OrLogicOP_54 || res_OrLogicOP_55);
    bool res_NotLogicOP_62 = true;
    res_NotLogicOP_62 = (res_NotLogicOP_62 && ! (L_P1__GetParamSubcl12(my_id) > 4u));
    res_OrLogicOP_54 = (res_OrLogicOP_54 || res_NotLogicOP_62);
    
    if(res_OrLogicOP_54){
    bool res_ImpliesLogicOp_63 = true;
    bool res_OrLogicOP_64 = false;
    bool res_NotLogicOP_65 = true;
    res_NotLogicOP_65 = (res_NotLogicOP_65 && ! (L_P1__GetSubcl28(my_id) > 6u));
    res_OrLogicOP_64 = (res_OrLogicOP_64 || res_NotLogicOP_65);
    res_OrLogicOP_64 = (res_OrLogicOP_64 || Timer_Disattivo(L_P1__GetSubcl40(my_id)));
    
    if(res_OrLogicOP_64){
    bool res_NotLogicOP_66 = true;
    res_NotLogicOP_66 = (res_NotLogicOP_66 && ! (L_P1__GetSubcl28(my_id) < 10u));
    res_ImpliesLogicOp_63 = (res_ImpliesLogicOp_63 && res_NotLogicOP_66);
    }
    res_ImpliesLogicOp_53 = (res_ImpliesLogicOp_53 && res_ImpliesLogicOp_63);
    }
    if(res_ImpliesLogicOp_53){
    xorIndex_res_XorLogicOP_52 = (xorIndex_res_XorLogicOP_52 + 1);
    }
    if((L_P1__GetInConsd1(my_id) == false)){
    xorIndex_res_XorLogicOP_52 = (xorIndex_res_XorLogicOP_52 + 1);
    }
    
    res_XorLogicOP_52 = (res_XorLogicOP_52 && (xorIndex_res_XorLogicOP_52 == 1));
    res_ImpliesLogicOp_47 = (res_ImpliesLogicOp_47 && res_XorLogicOP_52);
    }
    res_AndLogicOP_46 = (res_AndLogicOP_46 && res_ImpliesLogicOp_47);
    res_AndLogicOP_46 = (res_AndLogicOP_46 && (L_P1__GetParamSubcl10(my_id) == avanzamento1));
    
    res_ImpliesLogicOp_42 = (res_ImpliesLogicOp_42 && res_AndLogicOP_46);
    }
    if(res_ImpliesLogicOp_42){
    xorIndex_res_XorLogicOP_41 = (xorIndex_res_XorLogicOP_41 + 1);
    }
    if((L_P1__GetParamSubcl11(my_id) == false)){
    xorIndex_res_XorLogicOP_41 = (xorIndex_res_XorLogicOP_41 + 1);
    }
    
    res_XorLogicOP_41 = (res_XorLogicOP_41 && (xorIndex_res_XorLogicOP_41 == 1));
    res_ImpliesLogicOp_39 = (res_ImpliesLogicOp_39 && res_XorLogicOP_41);
    }
    if(res_ImpliesLogicOp_39){
    xorIndex_res_XorLogicOP_38 = (xorIndex_res_XorLogicOP_38 + 1);
    }
    bool res_NotLogicOP_67 = true;
    res_NotLogicOP_67 = (res_NotLogicOP_67 && ! (Counter_GetValore(L_P1__GetSubcl42(my_id)) < 15u));
    if(res_NotLogicOP_67){
    xorIndex_res_XorLogicOP_38 = (xorIndex_res_XorLogicOP_38 + 1);
    }
    
    res_XorLogicOP_38 = (res_XorLogicOP_38 && (xorIndex_res_XorLogicOP_38 == 1));
    res_ImpliesLogicOp_30 = (res_ImpliesLogicOp_30 && res_XorLogicOP_38);
    }
    if(res_ImpliesLogicOp_30){
    xorIndex_res_XorLogicOP_29 = (xorIndex_res_XorLogicOP_29 + 1);
    }
    bool res_NotLogicOP_68 = true;
    res_NotLogicOP_68 = (res_NotLogicOP_68 && ! (L_P1__GetSubcl28(my_id) > 6u));
    if(res_NotLogicOP_68){
    xorIndex_res_XorLogicOP_29 = (xorIndex_res_XorLogicOP_29 + 1);
    }
    
    res_XorLogicOP_29 = (res_XorLogicOP_29 && (xorIndex_res_XorLogicOP_29 == 1));
    res_ImpliesLogicOp_27 = (res_ImpliesLogicOp_27 && res_XorLogicOP_29);
    }
    if(res_ImpliesLogicOp_27){
    xorIndex_res_XorLogicOP_26 = (xorIndex_res_XorLogicOP_26 + 1);
    }
    if((L_P1__GetInConsd1(my_id) == false)){
    xorIndex_res_XorLogicOP_26 = (xorIndex_res_XorLogicOP_26 + 1);
    }
    
    res_XorLogicOP_26 = (res_XorLogicOP_26 && (xorIndex_res_XorLogicOP_26 == 1));
    res_ImpliesLogicOp_22 = (res_ImpliesLogicOp_22 && res_XorLogicOP_26);
    }
    res_AndLogicOP_21 = (res_AndLogicOP_21 && res_ImpliesLogicOp_22);
    bool res_NotLogicOP_69 = true;
    res_NotLogicOP_69 = (res_NotLogicOP_69 && ! Timer_Scaduto(L_P1__GetSubcl39(my_id)));
    res_AndLogicOP_21 = (res_AndLogicOP_21 && res_NotLogicOP_69);
    
    res_ImpliesLogicOp_13 = (res_ImpliesLogicOp_13 && res_AndLogicOP_21);
    }
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_ImpliesLogicOp_13);
    res_AndLogicOP_12 = (res_AndLogicOP_12 && (L_P1__GetInSubcl6(my_id) == true));
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_AndLogicOP_12);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *47,*  *34,*  il parametro SubClass_C2_parametro_P5 sia  uguale a avanzamentox
    res_AndLogicOP_0 = (res_AndLogicOP_0 && (L_P1__GetParamSubcl10(my_id) == avanzamento1));
    
    
    
    return res_AndLogicOP_0;
}


/*
    CNL corrispondente:
     {  commento: {69,}  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} e  se il timer SubClass_C2_timer_T8 è attivo commento: {34,} e  se il parametro SubClass_C2_parametro_P8 è  maggiore di  commento: {54,} 3 commento: {36,} e  se il timer SubClass_C2_timer_T1 è attivo commento: {34,} o  se il parametro SubClass_C2_parametro_P5 è  uguale a avanzamentox o  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
     commento: {68,} commento: {35,}  se il controllo SubClass_C2_controllo_C5 è  uguale a avanzamentox commento: {38,} e  se il contatore SubClass_C2_contatore_Co1 è  minore di  commento: {55,} 14 e  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} o  se il parametro SubClass_C2_parametro_P6 è  diverso da  True  o  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} e  se il timer SubClass_C2_timer_T1 non è scaduto, Almeno una delle seguenti { 
     commento: {67,} commento: {38,}  se il contatore SubClass_C2_contatore_Co7 è  minore di  commento: {55,} 1230 commento: {34,} o  se il parametro SubClass_C2_parametro_P5 non è  uguale a avanzamentox o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
      se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} o  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  commento: {54,} 7 commento: {36,} e  se il timer SubClass_C2_timer_T9 non è scaduto commento: {37,} o  se la variabile SubClass_C2_variabile_V2 è  uguale a  False  commento: {36,} e  se il timer SubClass_C2_timer_T8 non è attivo, Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
    
    
     } Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
    
    
     } Verifica che   commento: {48,}  commento: {,}  il controllo SubClass_C2_controllo_C8 non sia  diverso da  True 
    
    
     } Verifica che   commento: {48,}  commento: {,}  il controllo SubClass_C2_controllo_C1 sia  diverso da avanzamentox
    
     }
*/
static inline bool L_P1__Guard12(instance_id_t const my_id)
{
    bool res_AndLogicOP_0 = true;
    
    //  *69,*  se il controllo ConsDef  è  uguale a FALSE  *36,* e  se il timer SubClass_C2_timer_T8 è attivo *34,* e  se il parametro SubClass_C2_parametro_P8 è  maggiore di  *54,* 3 *36,* e  se il timer SubClass_C2_timer_T1 è attivo *34,* o  se il parametro SubClass_C2_parametro_P5 è  uguale a avanzamentox o  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
    //   *68,* *35,*  se il controllo SubClass_C2_controllo_C5 è  uguale a avanzamentox *38,* e  se il contatore SubClass_C2_contatore_Co1 è  minore di  *55,* 14 e  se il controllo ConsDef  è  uguale a FALSE  *34,* o  se il parametro SubClass_C2_parametro_P6 è  diverso da  True  o  se il controllo ConsDef  è  uguale a FALSE  *36,* e  se il timer SubClass_C2_timer_T1 non è scaduto, Almeno una delle seguenti { 
    //   *67,* *38,*  se il contatore SubClass_C2_contatore_Co7 è  minore di  *55,* 1230 *34,* o  se il parametro SubClass_C2_parametro_P5 non è  uguale a avanzamentox o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
    //    se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  *34,* o  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  *54,* 7 *36,* e  se il timer SubClass_C2_timer_T9 non è scaduto *37,* o  se la variabile SubClass_C2_variabile_V2 è  uguale a  False  *36,* e  se il timer SubClass_C2_timer_T8 non è attivo, Verifica che   *48,*   il controllo ConsDef  sia  uguale a FALSE 
    //   } Verifica che   *48,*   il controllo ConsDef  sia  uguale a FALSE 
    //   } Verifica che   *48,*  *,*  il controllo SubClass_C2_controllo_C8 non sia  diverso da  True 
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_AndLogicOP_4 = true;
    bool res_AndLogicOP_5 = true;
    bool res_AndLogicOP_6 = true;
    res_AndLogicOP_6 = (res_AndLogicOP_6 && (L_P1__GetInConsd1(my_id) == false));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && Timer_Attivo(L_P1__GetSubcl39(my_id)));
    
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_AndLogicOP_6);
    res_AndLogicOP_5 = (res_AndLogicOP_5 && (L_P1__GetParamSubcl12(my_id) > 3u));
    
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_AndLogicOP_5);
    res_AndLogicOP_4 = (res_AndLogicOP_4 && Timer_Attivo(L_P1__GetSubcl38(my_id)));
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_AndLogicOP_4);
    res_OrLogicOP_3 = (res_OrLogicOP_3 || (L_P1__GetParamSubcl10(my_id) == avanzamento1));
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    res_OrLogicOP_2 = (res_OrLogicOP_2 || (L_P1__GetInConsd1(my_id) == false));
    
    if(res_OrLogicOP_2){
    bool res_XorLogicOP_7 = true;
    int xorIndex_res_XorLogicOP_7 = 0;
    bool res_ImpliesLogicOp_8 = true;
    bool res_OrLogicOP_9 = false;
    bool res_OrLogicOP_10 = false;
    bool res_AndLogicOP_11 = true;
    bool res_AndLogicOP_12 = true;
    res_AndLogicOP_12 = (res_AndLogicOP_12 && (L_P1__GetInSubcl5(my_id) == avanzamento1));
    res_AndLogicOP_12 = (res_AndLogicOP_12 && (Counter_GetValore(L_P1__GetSubcl41(my_id)) < 14u));
    
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_AndLogicOP_12);
    res_AndLogicOP_11 = (res_AndLogicOP_11 && (L_P1__GetInConsd1(my_id) == false));
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_AndLogicOP_11);
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (L_P1__GetParamSubcl11(my_id) == true));
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_NotLogicOP_13);
    
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_OrLogicOP_10);
    bool res_AndLogicOP_14 = true;
    res_AndLogicOP_14 = (res_AndLogicOP_14 && (L_P1__GetInConsd1(my_id) == false));
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! Timer_Scaduto(L_P1__GetSubcl38(my_id)));
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_NotLogicOP_15);
    
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_AndLogicOP_14);
    
    if(res_OrLogicOP_9){
    bool res_OrLogicOP_16 = false;
    bool res_ImpliesLogicOp_17 = true;
    bool res_OrLogicOP_18 = false;
    bool res_OrLogicOP_19 = false;
    res_OrLogicOP_19 = (res_OrLogicOP_19 || (Counter_GetValore(L_P1__GetSubcl42(my_id)) < 1230u));
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! (L_P1__GetParamSubcl10(my_id) == avanzamento1));
    res_OrLogicOP_19 = (res_OrLogicOP_19 || res_NotLogicOP_20);
    
    res_OrLogicOP_18 = (res_OrLogicOP_18 || res_OrLogicOP_19);
    res_OrLogicOP_18 = (res_OrLogicOP_18 || (L_P1__GetInConsd1(my_id) == false));
    
    if(res_OrLogicOP_18){
    bool res_ImpliesLogicOp_21 = true;
    bool res_OrLogicOP_22 = false;
    bool res_OrLogicOP_23 = false;
    bool res_AndLogicOP_24 = true;
    res_AndLogicOP_24 = (res_AndLogicOP_24 && (L_P1__GetInConsd1(my_id) == false));
    res_AndLogicOP_24 = (res_AndLogicOP_24 && (L_P1__GetInConsd1(my_id) == false));
    
    res_OrLogicOP_23 = (res_OrLogicOP_23 || res_AndLogicOP_24);
    bool res_AndLogicOP_25 = true;
    bool res_NotLogicOP_26 = true;
    res_NotLogicOP_26 = (res_NotLogicOP_26 && ! (L_P1__GetParamSubcl12(my_id) > 7u));
    res_AndLogicOP_25 = (res_AndLogicOP_25 && res_NotLogicOP_26);
    bool res_NotLogicOP_27 = true;
    res_NotLogicOP_27 = (res_NotLogicOP_27 && ! Timer_Scaduto(L_P1__GetSubcl40(my_id)));
    res_AndLogicOP_25 = (res_AndLogicOP_25 && res_NotLogicOP_27);
    
    res_OrLogicOP_23 = (res_OrLogicOP_23 || res_AndLogicOP_25);
    
    res_OrLogicOP_22 = (res_OrLogicOP_22 || res_OrLogicOP_23);
    bool res_AndLogicOP_28 = true;
    res_AndLogicOP_28 = (res_AndLogicOP_28 && (L_P1__GetSubcl27(my_id) == false));
    bool res_NotLogicOP_29 = true;
    res_NotLogicOP_29 = (res_NotLogicOP_29 && ! Timer_Attivo(L_P1__GetSubcl39(my_id)));
    res_AndLogicOP_28 = (res_AndLogicOP_28 && res_NotLogicOP_29);
    
    res_OrLogicOP_22 = (res_OrLogicOP_22 || res_AndLogicOP_28);
    
    if(res_OrLogicOP_22){
    res_ImpliesLogicOp_21 = (res_ImpliesLogicOp_21 && (L_P1__GetInConsd1(my_id) == false));
    }
    res_ImpliesLogicOp_17 = (res_ImpliesLogicOp_17 && res_ImpliesLogicOp_21);
    }
    res_OrLogicOP_16 = (res_OrLogicOP_16 || res_ImpliesLogicOp_17);
    res_OrLogicOP_16 = (res_OrLogicOP_16 || (L_P1__GetInConsd1(my_id) == false));
    
    res_ImpliesLogicOp_8 = (res_ImpliesLogicOp_8 && res_OrLogicOP_16);
    }
    if(res_ImpliesLogicOp_8){
    xorIndex_res_XorLogicOP_7 = (xorIndex_res_XorLogicOP_7 + 1);
    }
    bool res_NotLogicOP_30 = true;
    bool res_NotLogicOP_31 = true;
    res_NotLogicOP_31 = (res_NotLogicOP_31 && ! (L_P1__GetInSubcl6(my_id) == true));
    res_NotLogicOP_30 = (res_NotLogicOP_30 && ! res_NotLogicOP_31);
    if(res_NotLogicOP_30){
    xorIndex_res_XorLogicOP_7 = (xorIndex_res_XorLogicOP_7 + 1);
    }
    
    res_XorLogicOP_7 = (res_XorLogicOP_7 && (xorIndex_res_XorLogicOP_7 == 1));
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_XorLogicOP_7);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *48,*  *,*  il controllo SubClass_C2_controllo_C1 sia  diverso da avanzamentox
    bool res_NotLogicOP_32 = true;
    res_NotLogicOP_32 = (res_NotLogicOP_32 && ! (L_P1__GetInSubcl2(my_id) == avanzamento1));
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_NotLogicOP_32);
    
    
    
    return res_AndLogicOP_0;
}


/*
    CNL corrispondente:
     {  Nessuna  commento: {80,} }
*/
static inline bool L_P1__Guard13(instance_id_t const my_id)
{
    return true;
}


/*
    CNL corrispondente:
     {  Nessuna  }
*/
static inline bool L_P1__Guard14(instance_id_t const my_id)
{
    return true;
}


/*
    CNL corrispondente:
     {  Nessuna  }
*/
static inline bool L_P1__Guard15(instance_id_t const my_id)
{
    return true;
}


/*
    CNL corrispondente:
     {  Nessuna  commento: {80,} }
*/
static inline bool L_P1__Guard16(instance_id_t const my_id)
{
    return true;
}


/*
    CNL corrispondente:
     {  commento: {69,} commento: {36,}  se il timer SubClass_C2_timer_T9 è disattivo, Solo una delle seguenti { 
     commento: {69,} commento: {38,}  se il contatore SubClass_C2_contatore_Co1 non è  maggiore di  commento: {54,} 1330 commento: {37,} o  se la variabile SubClass_C2_variabile_V6 è  diverso da GialloxVerdex commento: {34,} o  se il parametro SubClass_C2_parametro_P6 non è  diverso da  False , Solo una delle seguenti { 
     commento: {34,}  se il parametro SubClass_C2_parametro_P8 è  minore di  commento: {55,} 1, Verifica che   commento: {50,}  commento: {,}  la variabile SubClass_C2_variabile_V2 sia  uguale a  False 
    
    
     } Verifica che   commento: {48,}  commento: {,}  il controllo SubClass_C2_controllo_C5 sia  diverso da avanzamentox
    
    
     } Verifica che   commento: {49,}  commento: {,}  il timer SubClass_C2_timer_T9 non sia attivo
    
     }
*/
static inline bool L_P1__Guard17(instance_id_t const my_id)
{
    bool res_AndLogicOP_0 = true;
    
    //  *69,* *36,*  se il timer SubClass_C2_timer_T9 è disattivo, Solo una delle seguenti { 
    //   *69,* *38,*  se il contatore SubClass_C2_contatore_Co1 non è  maggiore di  *54,* 1330 *37,* o  se la variabile SubClass_C2_variabile_V6 è  diverso da GialloxVerdex *34,* o  se il parametro SubClass_C2_parametro_P6 non è  diverso da  False , Solo una delle seguenti { 
    //   *34,*  se il parametro SubClass_C2_parametro_P8 è  minore di  *55,* 1, Verifica che   *50,*  *,*  la variabile SubClass_C2_variabile_V2 sia  uguale a  False 
    //   } Verifica che   *48,*  *,*  il controllo SubClass_C2_controllo_C5 sia  diverso da avanzamentox
    //   }
    bool res_ImpliesLogicOp_1 = true;
    if(Timer_Disattivo(L_P1__GetSubcl40(my_id))){
    bool res_XorLogicOP_2 = true;
    int xorIndex_res_XorLogicOP_2 = 0;
    bool res_ImpliesLogicOp_3 = true;
    bool res_OrLogicOP_4 = false;
    bool res_OrLogicOP_5 = false;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (Counter_GetValore(L_P1__GetSubcl41(my_id)) > 1330u));
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_NotLogicOP_6);
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetSubcl29(my_id) == gialloxverd));
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_NotLogicOP_7);
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_OrLogicOP_5);
    bool res_NotLogicOP_8 = true;
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetParamSubcl11(my_id) == false));
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! res_NotLogicOP_9);
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_NotLogicOP_8);
    
    if(res_OrLogicOP_4){
    bool res_ImpliesLogicOp_10 = true;
    if((L_P1__GetParamSubcl12(my_id) < 1u)){
    res_ImpliesLogicOp_10 = (res_ImpliesLogicOp_10 && (L_P1__GetSubcl27(my_id) == false));
    }
    res_ImpliesLogicOp_3 = (res_ImpliesLogicOp_3 && res_ImpliesLogicOp_10);
    }
    if(res_ImpliesLogicOp_3){
    xorIndex_res_XorLogicOP_2 = (xorIndex_res_XorLogicOP_2 + 1);
    }
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (L_P1__GetInSubcl5(my_id) == avanzamento1));
    if(res_NotLogicOP_11){
    xorIndex_res_XorLogicOP_2 = (xorIndex_res_XorLogicOP_2 + 1);
    }
    
    res_XorLogicOP_2 = (res_XorLogicOP_2 && (xorIndex_res_XorLogicOP_2 == 1));
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_XorLogicOP_2);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *49,*  *,*  il timer SubClass_C2_timer_T9 non sia attivo
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! Timer_Attivo(L_P1__GetSubcl40(my_id)));
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_NotLogicOP_12);
    
    
    
    return res_AndLogicOP_0;
}


/*
    CNL corrispondente:
    
    {
    
     commento: {68,} commento: {34,}  se il parametro SubClass_C2_parametro_P8 è  minore di  commento: {55,} 10 commento: {35,} o  se il controllo SubClass_C2_controllo_C1 non è  diverso da avanzamentox commento: {37,} o  se la variabile SubClass_C2_variabile_V3 non è  maggiore di  commento: {54,} 5, Almeno una delle seguenti { 
     commento: {34,}  se il parametro SubClass_C2_parametro_P6 è  diverso da  True  e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
    
    
     } Verifica che   commento: {48,}  commento: {,}  il controllo SubClass_C2_controllo_C1 sia  uguale a avanzamentox
    
    
    }
*/
static inline bool L_P1__Guard18(instance_id_t const my_id)
{
    bool res_AndLogicOP_0 = true;
    
    //  *68,* *34,*  se il parametro SubClass_C2_parametro_P8 è  minore di  *55,* 10 *35,* o  se il controllo SubClass_C2_controllo_C1 non è  diverso da avanzamentox *37,* o  se la variabile SubClass_C2_variabile_V3 non è  maggiore di  *54,* 5, Almeno una delle seguenti { 
    //   *34,*  se il parametro SubClass_C2_parametro_P6 è  diverso da  True  e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   *48,*   il controllo ConsDef  sia  uguale a FALSE 
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    res_OrLogicOP_3 = (res_OrLogicOP_3 || (L_P1__GetParamSubcl12(my_id) < 10u));
    bool res_NotLogicOP_4 = true;
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetInSubcl2(my_id) == avanzamento1));
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! res_NotLogicOP_5);
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_NotLogicOP_4);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetSubcl28(my_id) > 5u));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_6);
    
    if(res_OrLogicOP_2){
    bool res_ImpliesLogicOp_7 = true;
    bool res_AndLogicOP_8 = true;
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetParamSubcl11(my_id) == true));
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_9);
    res_AndLogicOP_8 = (res_AndLogicOP_8 && (L_P1__GetInConsd1(my_id) == false));
    
    if(res_AndLogicOP_8){
    res_ImpliesLogicOp_7 = (res_ImpliesLogicOp_7 && (L_P1__GetInConsd1(my_id) == false));
    }
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_ImpliesLogicOp_7);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *48,*  *,*  il controllo SubClass_C2_controllo_C1 sia  uguale a avanzamentox
    res_AndLogicOP_0 = (res_AndLogicOP_0 && (L_P1__GetInSubcl2(my_id) == avanzamento1));
    
    
    
    return res_AndLogicOP_0;
}


// ********** Definizione effetti **********

/*
    CNL corrispondente:
    
     {
     Nessuna 
     }
*/
static inline void L_P1__Effec2(instance_id_t const my_id)
{
    
}


/*
    CNL corrispondente:
    
    {
    
     commento: {34,}  se lo stato  è  diverso da  commento: {56,}  state1  commento: {106,} o  se il controllo ConsDef  è  uguale a FALSE ,  Applica gli effetti
           della macro SubClass_C2_macroef_M3( con argomento_af1   uguale a c270 ,argomento_af8   uguale a avanzamento ,argomento_af10   uguale a True ,argomento_af5   uguale a avanzamento ) commento: {73,}
    
       
     commento: {110,}  se il ripristino del timer  SubClass_C2_restoreTI_TI3 è attivo commento: {38,} e  se il contatore SubClass_C2_contatore_Co1 è  minore di  commento: {55,} 122, commento: {69,}Disattiva il timer SubClass_C2_timer_T9
    
       
     commento: {37,}  se la variabile SubClass_C2_variabile_V6 è  uguale a GialloxVerdex,  commento: {43,}  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L6 è attivo, commento: {88,} quando  commento: {42,}    MainClass_C1_controllo_C9 del campo  MainClass_C1     è  uguale a RossoGialloaVerdea commento: {38,} o  se il contatore SubClass_C2_contatore_Co1 non è  uguale a  commento: {53,} 13304, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V6 il valore GialloxVerdex
    
       
    
    }
*/
static inline void L_P1__Effec3(instance_id_t const my_id)
{
    
    //  *34,*  se lo stato  è  diverso da  *56,*  state1  *106,* o  se il controllo ConsDef  è  uguale a FALSE ,  Applica gli effetti
    //         della macro SubClass_C2_macroef_M3( con argomento_af1   uguale a c270 ,argomento_af8   uguale a avanzamento ,argomento_af10   uguale a True ,argomento_af5   uguale a avanzamento )
    bool res_OrLogicOP_0 = false;
    bool res_NotLogicOP_1 = true;
    res_NotLogicOP_1 = (res_NotLogicOP_1 && ! (L_P1_C2_GetState(my_id) == C2_St_state));
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_1);
    res_OrLogicOP_0 = (res_OrLogicOP_0 || (L_P1__GetInConsd1(my_id) == false));
    
    if(res_OrLogicOP_0){
    
    L_P1__Macro11(my_id,c270,true,avanzamento,avanzamento);
    }
    
    //  *73,*
    //     
    //   *110,*  se il ripristino del timer  SubClass_C2_restoreTI_TI3 è attivo *38,* e  se il contatore SubClass_C2_contatore_Co1 è  minore di  *55,* 122, *69,*Disattiva il timer SubClass_C2_timer_T9
    bool res_AndLogicOP_2 = true;
    res_AndLogicOP_2 = (res_AndLogicOP_2 && Timer_Attivo(L_P1__GetSubcl35(my_id)));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && (Counter_GetValore(L_P1__GetSubcl41(my_id)) < 122u));
    
    if(res_AndLogicOP_2){
    
    Timer_Disattiva(L_P1__GetSubcl40(my_id));
    }
    
    //  *37,*  se la variabile SubClass_C2_variabile_V6 è  uguale a GialloxVerdex,  *43,*  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L6 è attivo, *88,* quando  *42,*    MainClass_C1_controllo_C9 del campo  MainClass_C1     è  uguale a RossoGialloaVerdea *38,* o  se il contatore SubClass_C2_contatore_Co1 non è  uguale a  *53,* 13304, *67,* Assegna alla variabile SubClass_C2_variabile_V6 il valore GialloxVerdex
    bool res_OrLogicOP_3 = false;
    bool res_AndLogicOP_4 = true;
    res_AndLogicOP_4 = (res_AndLogicOP_4 && (L_P1__GetSubcl29(my_id) == gialloxverd));
    bool res_ForAllPredicate_5 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl9Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl9(my_id,i);
    bool res_ImpliesLogicOp_6 = true;
    if((L_P1__GetInMainc5(it.mainc47) == rossogiallo)){
    res_ImpliesLogicOp_6 = (res_ImpliesLogicOp_6 && Timer_Attivo(L_P1__GetMainc39(it.mainc47)));
    }
    res_ForAllPredicate_5 = res_ImpliesLogicOp_6;
    if(!res_ForAllPredicate_5) {break;}
    }
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_ForAllPredicate_5);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_AndLogicOP_4);
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (Counter_GetValore(L_P1__GetSubcl41(my_id)) == 13304u));
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_NotLogicOP_7);
    
    if(res_OrLogicOP_3){
    
    L_P1__SetSubcl29(my_id,gialloxverd);
    }
}


/*
    CNL corrispondente:
     { commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  commento: {105,} è  diverso da  commento: {56,}  state1  commento: {37,} o  se la variabile SubClass_C2_variabile_V3 è  diverso da  commento: {56,} 3 commento: {34,} e  se il parametro SubClass_C2_parametro_P8 non è  diverso da  commento: {56,} 1 commento: {35,} o  se il controllo SubClass_C2_controllo_C8 è  uguale a  False  commento: {37,} e  se la variabile SubClass_C2_variabile_V3 è  maggiore di  commento: {54,} 3 e  se il controllo ConsDef  è  uguale a FALSE , commento: {68,}Attiva il timer SubClass_C2_timer_T1
    
     ,altrimenti  commento: {66,} Assegna al comando SubClass_C2_comando_C3 il valore avanzamentox
    
    
     }
*/
static inline void L_P1__Effec4(instance_id_t const my_id)
{
    
    //  *111,*  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  *105,* è  diverso da  *56,*  state1  *37,* o  se la variabile SubClass_C2_variabile_V3 è  diverso da  *56,* 3 *34,* e  se il parametro SubClass_C2_parametro_P8 non è  diverso da  *56,* 1 *35,* o  se il controllo SubClass_C2_controllo_C8 è  uguale a  False  *37,* e  se la variabile SubClass_C2_variabile_V3 è  maggiore di  *54,* 3 e  se il controllo ConsDef  è  uguale a FALSE , *68,*Attiva il timer SubClass_C2_timer_T1
    //   ,altrimenti  *66,* Assegna al comando SubClass_C2_comando_C3 il valore avanzamentox
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_ForAllPredicateNotEmpty_2 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl8Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl8(my_id,i);
    bool res_ImpliesLogicOp_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1_C1_GetState(it.mainc47) == C1_St_state));
    res_ImpliesLogicOp_3 = (res_ImpliesLogicOp_3 && res_NotLogicOP_4);
    res_ForAllPredicateNotEmpty_2 = res_ImpliesLogicOp_3;
    if(!res_ForAllPredicateNotEmpty_2) {break;}
    }
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_ForAllPredicateNotEmpty_2);
    bool res_AndLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetSubcl28(my_id) == 3u));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_6);
    bool res_NotLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetParamSubcl12(my_id) == 1u));
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! res_NotLogicOP_8);
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_7);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_5);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_AndLogicOP_9 = true;
    bool res_AndLogicOP_10 = true;
    res_AndLogicOP_10 = (res_AndLogicOP_10 && (L_P1__GetInSubcl6(my_id) == false));
    res_AndLogicOP_10 = (res_AndLogicOP_10 && (L_P1__GetSubcl28(my_id) > 3u));
    
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_AndLogicOP_10);
    res_AndLogicOP_9 = (res_AndLogicOP_9 && (L_P1__GetInConsd1(my_id) == false));
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_9);
    
    if(res_OrLogicOP_0){
    
    Timer_Attiva(L_P1__GetSubcl38(my_id));
    }else{
    
    L_P1__SetOutSubcl(my_id,avanzamento1);
    }
}


/*
    CNL corrispondente:
     { commento: {110,}  se il ripristino del timer  SubClass_C2_restoreTI_TI2 è attivo commento: {36,} e  se il timer SubClass_C2_timer_T9 è disattivo commento: {37,} o  se la variabile SubClass_C2_variabile_V2 è  diverso da  True  commento: {36,} o  se il timer SubClass_C2_timer_T1 non è disattivo commento: {35,} o  se il controllo SubClass_C2_controllo_C8 non è  diverso da  True , commento: {68,}Attiva il timer SubClass_C2_timer_T9
    
     ,altrimenti   Applica gli effetti
           della macro SubClass_C2_macroef_M3( con argomento_af1   uguale a avanzamentox ,argomento_af8   uguale a avanzamento ,argomento_af10   uguale a True ,argomento_af5   uguale a GialloaVerdea ) commento: {73,}
    
    
     commento: {34,}  se lo stato  è  diverso da  commento: {56,}  state1  commento: {106,} commento: {34,} o  se il parametro SubClass_C2_parametro_P8 è  diverso da  commento: {56,} 8 commento: {35,} o  se il controllo SubClass_C2_controllo_C1 non è  uguale a avanzamentox commento: {35,} o  se il controllo SubClass_C2_controllo_C8 non è  diverso da  False ,  Applica gli effetti
           della macro SubClass_C2_macroef_M3( con argomento_af1   uguale a c270 ,argomento_af8   uguale a GialloaVerdea ,argomento_af10   uguale a True ,argomento_af5   uguale a avanzamento ) commento: {73,}
    
       
     commento: {36,}  se il timer SubClass_C2_timer_T1 non è disattivo commento: {34,} o  se il parametro SubClass_C2_parametro_P6 è  diverso da  False  e  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} o  se il controllo SubClass_C2_controllo_C1 non è  diverso da avanzamentox e  se il controllo ConsDef  è  uguale a FALSE , commento: {66,} Assegna al comando SubClass_C2_comando_C3 il valore avanzamentox
    
       
     commento: {36,}  se il timer SubClass_C2_timer_T9 è attivo,  commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L2 è  uguale a  commento: {53,}  state1 , commento: {88,} quando  commento: {43,}   MainClass_C1_timer_T10 del campo  MainClass_C1     commento: {105,} è attivo commento: {35,} e  se il controllo SubClass_C2_controllo_C8 è  diverso da  False , commento: {68,}Attiva il timer SubClass_C2_timer_T9
    
     ,altrimenti   Applica gli effetti
           della macro SubClass_C2_macroef_M3( con argomento_af1   uguale a avanzamentox ,argomento_af8   uguale a GialloaVerdea ,argomento_af10   uguale a True ,argomento_af5   uguale a GialloaVerdea ) commento: {73,}
    
    
     commento: {37,}  se la variabile SubClass_C2_variabile_V6 è  uguale a GialloxVerdex commento: {38,} e  se il contatore SubClass_C2_contatore_Co1 è  maggiore di  commento: {54,} 12123, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V3 il valore 1
    
     ,altrimenti  commento: {68,}Attiva il timer SubClass_C2_timer_T8
    
    
     }
*/
static inline void L_P1__Effec5(instance_id_t const my_id)
{
    
    //  *110,*  se il ripristino del timer  SubClass_C2_restoreTI_TI2 è attivo *36,* e  se il timer SubClass_C2_timer_T9 è disattivo *37,* o  se la variabile SubClass_C2_variabile_V2 è  diverso da  True  *36,* o  se il timer SubClass_C2_timer_T1 non è disattivo *35,* o  se il controllo SubClass_C2_controllo_C8 non è  diverso da  True , *68,*Attiva il timer SubClass_C2_timer_T9
    //   ,altrimenti   Applica gli effetti
    //         della macro SubClass_C2_macroef_M3( con argomento_af1   uguale a avanzamentox ,argomento_af8   uguale a avanzamento ,argomento_af10   uguale a True ,argomento_af5   uguale a GialloaVerdea )
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_OrLogicOP_2 = false;
    bool res_AndLogicOP_3 = true;
    res_AndLogicOP_3 = (res_AndLogicOP_3 && Timer_Attivo(L_P1__GetSubcl33(my_id)));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && Timer_Disattivo(L_P1__GetSubcl40(my_id)));
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_3);
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetSubcl27(my_id) == true));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_4);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_OrLogicOP_2);
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! Timer_Disattivo(L_P1__GetSubcl38(my_id)));
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_NotLogicOP_5);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_NotLogicOP_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetInSubcl6(my_id) == true));
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! res_NotLogicOP_7);
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_6);
    
    if(res_OrLogicOP_0){
    
    Timer_Attiva(L_P1__GetSubcl40(my_id));
    }else{
    
    L_P1__Macro11(my_id,avanzamento1,true,gialloaverd,avanzamento);
    }
    
    //  *73,*
    //   *34,*  se lo stato  è  diverso da  *56,*  state1  *106,* *34,* o  se il parametro SubClass_C2_parametro_P8 è  diverso da  *56,* 8 *35,* o  se il controllo SubClass_C2_controllo_C1 non è  uguale a avanzamentox *35,* o  se il controllo SubClass_C2_controllo_C8 non è  diverso da  False ,  Applica gli effetti
    //         della macro SubClass_C2_macroef_M3( con argomento_af1   uguale a c270 ,argomento_af8   uguale a GialloaVerdea ,argomento_af10   uguale a True ,argomento_af5   uguale a avanzamento )
    bool res_OrLogicOP_8 = false;
    bool res_OrLogicOP_9 = false;
    bool res_OrLogicOP_10 = false;
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (L_P1_C2_GetState(my_id) == C2_St_state));
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_NotLogicOP_11);
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (L_P1__GetParamSubcl12(my_id) == 8u));
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_NotLogicOP_12);
    
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_OrLogicOP_10);
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (L_P1__GetInSubcl2(my_id) == avanzamento1));
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_NotLogicOP_13);
    
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_OrLogicOP_9);
    bool res_NotLogicOP_14 = true;
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (L_P1__GetInSubcl6(my_id) == false));
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! res_NotLogicOP_15);
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_NotLogicOP_14);
    
    if(res_OrLogicOP_8){
    
    L_P1__Macro11(my_id,c270,true,avanzamento,gialloaverd);
    }
    
    //  *73,*
    //     
    //   *36,*  se il timer SubClass_C2_timer_T1 non è disattivo *34,* o  se il parametro SubClass_C2_parametro_P6 è  diverso da  False  e  se il controllo ConsDef  è  uguale a FALSE  *35,* o  se il controllo SubClass_C2_controllo_C1 non è  diverso da avanzamentox e  se il controllo ConsDef  è  uguale a FALSE , *66,* Assegna al comando SubClass_C2_comando_C3 il valore avanzamentox
    bool res_OrLogicOP_16 = false;
    bool res_OrLogicOP_17 = false;
    bool res_NotLogicOP_18 = true;
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! Timer_Disattivo(L_P1__GetSubcl38(my_id)));
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_NotLogicOP_18);
    bool res_AndLogicOP_19 = true;
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! (L_P1__GetParamSubcl11(my_id) == false));
    res_AndLogicOP_19 = (res_AndLogicOP_19 && res_NotLogicOP_20);
    res_AndLogicOP_19 = (res_AndLogicOP_19 && (L_P1__GetInConsd1(my_id) == false));
    
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_AndLogicOP_19);
    
    res_OrLogicOP_16 = (res_OrLogicOP_16 || res_OrLogicOP_17);
    bool res_AndLogicOP_21 = true;
    bool res_NotLogicOP_22 = true;
    bool res_NotLogicOP_23 = true;
    res_NotLogicOP_23 = (res_NotLogicOP_23 && ! (L_P1__GetInSubcl2(my_id) == avanzamento1));
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! res_NotLogicOP_23);
    res_AndLogicOP_21 = (res_AndLogicOP_21 && res_NotLogicOP_22);
    res_AndLogicOP_21 = (res_AndLogicOP_21 && (L_P1__GetInConsd1(my_id) == false));
    
    res_OrLogicOP_16 = (res_OrLogicOP_16 || res_AndLogicOP_21);
    
    if(res_OrLogicOP_16){
    
    L_P1__SetOutSubcl(my_id,avanzamento1);
    }
    
    //  *36,*  se il timer SubClass_C2_timer_T9 è attivo,  *111,*  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L2 è  uguale a  *53,*  state1 , *88,* quando  *43,*   MainClass_C1_timer_T10 del campo  MainClass_C1     *105,* è attivo *35,* e  se il controllo SubClass_C2_controllo_C8 è  diverso da  False , *68,*Attiva il timer SubClass_C2_timer_T9
    //   ,altrimenti   Applica gli effetti
    //         della macro SubClass_C2_macroef_M3( con argomento_af1   uguale a avanzamentox ,argomento_af8   uguale a GialloaVerdea ,argomento_af10   uguale a True ,argomento_af5   uguale a GialloaVerdea )
    bool res_AndLogicOP_24 = true;
    bool res_AndLogicOP_25 = true;
    res_AndLogicOP_25 = (res_AndLogicOP_25 && Timer_Attivo(L_P1__GetSubcl40(my_id)));
    bool res_ForAllPredicate_26 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl7Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl7(my_id,i);
    bool res_ImpliesLogicOp_27 = true;
    if(Timer_Attivo(L_P1__GetMainc39(it.mainc47))){
    res_ImpliesLogicOp_27 = (res_ImpliesLogicOp_27 && (L_P1_C1_GetState(it.mainc47) == C1_St_state));
    }
    res_ForAllPredicate_26 = res_ImpliesLogicOp_27;
    if(!res_ForAllPredicate_26) {break;}
    }
    res_AndLogicOP_25 = (res_AndLogicOP_25 && res_ForAllPredicate_26);
    
    res_AndLogicOP_24 = (res_AndLogicOP_24 && res_AndLogicOP_25);
    bool res_NotLogicOP_28 = true;
    res_NotLogicOP_28 = (res_NotLogicOP_28 && ! (L_P1__GetInSubcl6(my_id) == false));
    res_AndLogicOP_24 = (res_AndLogicOP_24 && res_NotLogicOP_28);
    
    if(res_AndLogicOP_24){
    
    Timer_Attiva(L_P1__GetSubcl40(my_id));
    }else{
    
    L_P1__Macro11(my_id,avanzamento1,true,gialloaverd,gialloaverd);
    }
    
    //  *73,*
    //   *37,*  se la variabile SubClass_C2_variabile_V6 è  uguale a GialloxVerdex *38,* e  se il contatore SubClass_C2_contatore_Co1 è  maggiore di  *54,* 12123, *67,* Assegna alla variabile SubClass_C2_variabile_V3 il valore 1
    //   ,altrimenti  *68,*Attiva il timer SubClass_C2_timer_T8
    bool res_AndLogicOP_29 = true;
    res_AndLogicOP_29 = (res_AndLogicOP_29 && (L_P1__GetSubcl29(my_id) == gialloxverd));
    res_AndLogicOP_29 = (res_AndLogicOP_29 && (Counter_GetValore(L_P1__GetSubcl41(my_id)) > 12123u));
    
    if(res_AndLogicOP_29){
    
    L_P1__SetSubcl28(my_id,1u);
    }else{
    
    Timer_Attiva(L_P1__GetSubcl39(my_id));
    }
}


/*
    CNL corrispondente:
     { commento: {41,}  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  commento: {105,} è  diverso da  False  commento: {38,} e  se il contatore SubClass_C2_contatore_Co1 è  diverso da  commento: {56,} 150, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V3 il valore 8
    
     ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V6 il valore GialloxVerdex
    
    
     commento: {110,}  se il ripristino del timer  SubClass_C2_restoreTI_TI3 è attivo commento: {35,} o  se il controllo SubClass_C2_controllo_C1 è  diverso da avanzamentox e  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} e  se il controllo SubClass_C2_controllo_C8 è  diverso da  False  commento: {36,} e  se il timer SubClass_C2_timer_T1 non è scaduto,  Applica gli effetti
           della macro SubClass_C2_macroef_M6  commento: {73,}
    
       
     commento: {34,}  se il parametro SubClass_C2_parametro_P5 non è  diverso da avanzamentox e  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} e  se il controllo SubClass_C2_controllo_C1 è  diverso da avanzamentox commento: {37,} o  se la variabile SubClass_C2_variabile_V3 è  minore di  commento: {55,} 7 commento: {35,} e  se il controllo SubClass_C2_controllo_C1 è  diverso da avanzamentox commento: {37,} e  se la variabile SubClass_C2_variabile_V6 è  uguale a GialloxVerdex, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V3 il valore 3
    
       
     commento: {36,}  se il timer SubClass_C2_timer_T9 non è scaduto commento: {37,} o  se la variabile SubClass_C2_variabile_V3 è  diverso da  commento: {56,} 6 commento: {36,} e  se il timer SubClass_C2_timer_T1 è scaduto commento: {36,} o  se il timer SubClass_C2_timer_T1 non è scaduto commento: {36,} e  se il timer SubClass_C2_timer_T9 non è disattivo, commento: {69,}Disattiva il timer SubClass_C2_timer_T9
    
       
     }
*/
static inline void L_P1__Effec6(instance_id_t const my_id)
{
    
    //  *41,*  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  *105,* è  diverso da  False  *38,* e  se il contatore SubClass_C2_contatore_Co1 è  diverso da  *56,* 150, *67,* Assegna alla variabile SubClass_C2_variabile_V3 il valore 8
    //   ,altrimenti  *67,* Assegna alla variabile SubClass_C2_variabile_V6 il valore GialloxVerdex
    bool res_AndLogicOP_0 = true;
    bool res_ForAllPredicateNotEmpty_1 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl8Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl8(my_id,i);
    bool res_ImpliesLogicOp_2 = true;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__GetParamMainc9(it.mainc47) == false));
    res_ImpliesLogicOp_2 = (res_ImpliesLogicOp_2 && res_NotLogicOP_3);
    res_ForAllPredicateNotEmpty_1 = res_ImpliesLogicOp_2;
    if(!res_ForAllPredicateNotEmpty_1) {break;}
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ForAllPredicateNotEmpty_1);
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (Counter_GetValore(L_P1__GetSubcl41(my_id)) == 150u));
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_NotLogicOP_4);
    
    if(res_AndLogicOP_0){
    
    L_P1__SetSubcl28(my_id,8u);
    }else{
    
    L_P1__SetSubcl29(my_id,gialloxverd);
    }
    
    //  *110,*  se il ripristino del timer  SubClass_C2_restoreTI_TI3 è attivo *35,* o  se il controllo SubClass_C2_controllo_C1 è  diverso da avanzamentox e  se il controllo ConsDef  è  uguale a FALSE  *35,* e  se il controllo SubClass_C2_controllo_C8 è  diverso da  False  *36,* e  se il timer SubClass_C2_timer_T1 non è scaduto,  Applica gli effetti
    //         della macro SubClass_C2_macroef_M6
    bool res_OrLogicOP_5 = false;
    res_OrLogicOP_5 = (res_OrLogicOP_5 || Timer_Attivo(L_P1__GetSubcl35(my_id)));
    bool res_AndLogicOP_6 = true;
    bool res_AndLogicOP_7 = true;
    bool res_AndLogicOP_8 = true;
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetInSubcl2(my_id) == avanzamento1));
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_9);
    res_AndLogicOP_8 = (res_AndLogicOP_8 && (L_P1__GetInConsd1(my_id) == false));
    
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_AndLogicOP_8);
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__GetInSubcl6(my_id) == false));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_10);
    
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_AndLogicOP_7);
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! Timer_Scaduto(L_P1__GetSubcl38(my_id)));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_11);
    
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_AndLogicOP_6);
    
    if(res_OrLogicOP_5){
    
    L_P1__Macro12(my_id);
    }
    
    //  *73,*
    //     
    //   *34,*  se il parametro SubClass_C2_parametro_P5 non è  diverso da avanzamentox e  se il controllo ConsDef  è  uguale a FALSE  *35,* e  se il controllo SubClass_C2_controllo_C1 è  diverso da avanzamentox *37,* o  se la variabile SubClass_C2_variabile_V3 è  minore di  *55,* 7 *35,* e  se il controllo SubClass_C2_controllo_C1 è  diverso da avanzamentox *37,* e  se la variabile SubClass_C2_variabile_V6 è  uguale a GialloxVerdex, *67,* Assegna alla variabile SubClass_C2_variabile_V3 il valore 3
    bool res_OrLogicOP_12 = false;
    bool res_AndLogicOP_13 = true;
    bool res_AndLogicOP_14 = true;
    bool res_NotLogicOP_15 = true;
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (L_P1__GetParamSubcl10(my_id) == avanzamento1));
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! res_NotLogicOP_16);
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_NotLogicOP_15);
    res_AndLogicOP_14 = (res_AndLogicOP_14 && (L_P1__GetInConsd1(my_id) == false));
    
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_AndLogicOP_14);
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! (L_P1__GetInSubcl2(my_id) == avanzamento1));
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_NotLogicOP_17);
    
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_AndLogicOP_13);
    bool res_AndLogicOP_18 = true;
    bool res_AndLogicOP_19 = true;
    res_AndLogicOP_19 = (res_AndLogicOP_19 && (L_P1__GetSubcl28(my_id) < 7u));
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! (L_P1__GetInSubcl2(my_id) == avanzamento1));
    res_AndLogicOP_19 = (res_AndLogicOP_19 && res_NotLogicOP_20);
    
    res_AndLogicOP_18 = (res_AndLogicOP_18 && res_AndLogicOP_19);
    res_AndLogicOP_18 = (res_AndLogicOP_18 && (L_P1__GetSubcl29(my_id) == gialloxverd));
    
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_AndLogicOP_18);
    
    if(res_OrLogicOP_12){
    
    L_P1__SetSubcl28(my_id,3u);
    }
    
    //  *36,*  se il timer SubClass_C2_timer_T9 non è scaduto *37,* o  se la variabile SubClass_C2_variabile_V3 è  diverso da  *56,* 6 *36,* e  se il timer SubClass_C2_timer_T1 è scaduto *36,* o  se il timer SubClass_C2_timer_T1 non è scaduto *36,* e  se il timer SubClass_C2_timer_T9 non è disattivo, *69,*Disattiva il timer SubClass_C2_timer_T9
    bool res_OrLogicOP_21 = false;
    bool res_OrLogicOP_22 = false;
    bool res_NotLogicOP_23 = true;
    res_NotLogicOP_23 = (res_NotLogicOP_23 && ! Timer_Scaduto(L_P1__GetSubcl40(my_id)));
    res_OrLogicOP_22 = (res_OrLogicOP_22 || res_NotLogicOP_23);
    bool res_AndLogicOP_24 = true;
    bool res_NotLogicOP_25 = true;
    res_NotLogicOP_25 = (res_NotLogicOP_25 && ! (L_P1__GetSubcl28(my_id) == 6u));
    res_AndLogicOP_24 = (res_AndLogicOP_24 && res_NotLogicOP_25);
    res_AndLogicOP_24 = (res_AndLogicOP_24 && Timer_Scaduto(L_P1__GetSubcl38(my_id)));
    
    res_OrLogicOP_22 = (res_OrLogicOP_22 || res_AndLogicOP_24);
    
    res_OrLogicOP_21 = (res_OrLogicOP_21 || res_OrLogicOP_22);
    bool res_AndLogicOP_26 = true;
    bool res_NotLogicOP_27 = true;
    res_NotLogicOP_27 = (res_NotLogicOP_27 && ! Timer_Scaduto(L_P1__GetSubcl38(my_id)));
    res_AndLogicOP_26 = (res_AndLogicOP_26 && res_NotLogicOP_27);
    bool res_NotLogicOP_28 = true;
    res_NotLogicOP_28 = (res_NotLogicOP_28 && ! Timer_Disattivo(L_P1__GetSubcl40(my_id)));
    res_AndLogicOP_26 = (res_AndLogicOP_26 && res_NotLogicOP_28);
    
    res_OrLogicOP_21 = (res_OrLogicOP_21 || res_AndLogicOP_26);
    
    if(res_OrLogicOP_21){
    
    Timer_Disattiva(L_P1__GetSubcl40(my_id));
    }
}


/*
    CNL corrispondente:
     { commento: {41,}  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C2_lista_L4 è  uguale a  True  commento: {35,} e  se il controllo SubClass_C2_controllo_C1 non è  uguale a avanzamentox commento: {35,} o  se il controllo SubClass_C2_controllo_C1 è  diverso da avanzamentox commento: {36,} o  se il timer SubClass_C2_timer_T9 non è attivo, commento: {66,} Assegna al comando SubClass_C2_comando_C6 il valore avanzamentox
    
     ,altrimenti  commento: {72,}Azzera il contatore SubClass_C2_contatore_Co7
    
    
     commento: {38,}  se il contatore SubClass_C2_contatore_Co7 non è  maggiore di  commento: {54,} 11 e  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} o  se il contatore SubClass_C2_contatore_Co1 è  diverso da  commento: {56,} 12451 commento: {36,} o  se il timer SubClass_C2_timer_T9 è disattivo commento: {34,} o  se il parametro SubClass_C2_parametro_P6 è  diverso da  False  commento: {36,} o  se il timer SubClass_C2_timer_T8 non è disattivo, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V3 il valore 6
    
     ,altrimenti  commento: {66,} Assegna al comando SubClass_C2_comando_C6 il valore avanzamentox
    
    
     }
*/
static inline void L_P1__Effec7(instance_id_t const my_id)
{
    
    //  *41,*  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C2_lista_L4 è  uguale a  True  *35,* e  se il controllo SubClass_C2_controllo_C1 non è  uguale a avanzamentox *35,* o  se il controllo SubClass_C2_controllo_C1 è  diverso da avanzamentox *36,* o  se il timer SubClass_C2_timer_T9 non è attivo, *66,* Assegna al comando SubClass_C2_comando_C6 il valore avanzamentox
    //   ,altrimenti  *72,*Azzera il contatore SubClass_C2_contatore_Co7
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_AndLogicOP_2 = true;
    bool res_ForAllPredicate_3 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl8Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl8(my_id,i);
    bool res_ImpliesLogicOp_4 = true;
    res_ImpliesLogicOp_4 = (res_ImpliesLogicOp_4 && (L_P1__GetParamMainc9(it.mainc47) == true));
    res_ForAllPredicate_3 = res_ImpliesLogicOp_4;
    if(!res_ForAllPredicate_3) {break;}
    }
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_ForAllPredicate_3);
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetInSubcl2(my_id) == avanzamento1));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_5);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_2);
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetInSubcl2(my_id) == avanzamento1));
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_NotLogicOP_6);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! Timer_Attivo(L_P1__GetSubcl40(my_id)));
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_7);
    
    if(res_OrLogicOP_0){
    
    L_P1__SetOutSubcl1(my_id,avanzamento1);
    }else{
    
    Counter_Res(L_P1__GetSubcl42(my_id));
    }
    
    //  *38,*  se il contatore SubClass_C2_contatore_Co7 non è  maggiore di  *54,* 11 e  se il controllo ConsDef  è  uguale a FALSE  *38,* o  se il contatore SubClass_C2_contatore_Co1 è  diverso da  *56,* 12451 *36,* o  se il timer SubClass_C2_timer_T9 è disattivo *34,* o  se il parametro SubClass_C2_parametro_P6 è  diverso da  False  *36,* o  se il timer SubClass_C2_timer_T8 non è disattivo, *67,* Assegna alla variabile SubClass_C2_variabile_V3 il valore 6
    //   ,altrimenti  *66,* Assegna al comando SubClass_C2_comando_C6 il valore avanzamentox
    bool res_OrLogicOP_8 = false;
    bool res_OrLogicOP_9 = false;
    bool res_OrLogicOP_10 = false;
    bool res_OrLogicOP_11 = false;
    bool res_AndLogicOP_12 = true;
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (Counter_GetValore(L_P1__GetSubcl42(my_id)) > 11u));
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_NotLogicOP_13);
    res_AndLogicOP_12 = (res_AndLogicOP_12 && (L_P1__GetInConsd1(my_id) == false));
    
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_AndLogicOP_12);
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (Counter_GetValore(L_P1__GetSubcl41(my_id)) == 12451u));
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_NotLogicOP_14);
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_OrLogicOP_11);
    res_OrLogicOP_10 = (res_OrLogicOP_10 || Timer_Disattivo(L_P1__GetSubcl40(my_id)));
    
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_OrLogicOP_10);
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (L_P1__GetParamSubcl11(my_id) == false));
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_NotLogicOP_15);
    
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_OrLogicOP_9);
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! Timer_Disattivo(L_P1__GetSubcl39(my_id)));
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_NotLogicOP_16);
    
    if(res_OrLogicOP_8){
    
    L_P1__SetSubcl28(my_id,6u);
    }else{
    
    L_P1__SetOutSubcl1(my_id,avanzamento1);
    }
}


/*
    CNL corrispondente:
     { commento: {34,}  se il parametro SubClass_C2_parametro_P8 non è  diverso da  commento: {56,} 4,  commento: {45,}  se  MainClass_C1_contatore_Co3 del campo  MainClass_C1 di SubClass_C2_lista_L2 esiste e  commento: {105,} è  uguale a  commento: {53,} 15230, commento: {88,} quando  commento: {111,}   lo stato del campo  MainClass_C1     commento: {105,} è  uguale a  commento: {53,}  state1 , commento: {67,} Assegna alla variabile SubClass_C2_variabile_V3 il valore 1
    
       
     }
*/
static inline void L_P1__Effec8(instance_id_t const my_id)
{
    
    //  *34,*  se il parametro SubClass_C2_parametro_P8 non è  diverso da  *56,* 4,  *45,*  se  MainClass_C1_contatore_Co3 del campo  MainClass_C1 di SubClass_C2_lista_L2 esiste e  *105,* è  uguale a  *53,* 15230, *88,* quando  *111,*   lo stato del campo  MainClass_C1     *105,* è  uguale a  *53,*  state1 , *67,* Assegna alla variabile SubClass_C2_variabile_V3 il valore 1
    bool res_AndLogicOP_0 = true;
    bool res_NotLogicOP_1 = true;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (L_P1__GetParamSubcl12(my_id) == 4u));
    res_NotLogicOP_1 = (res_NotLogicOP_1 && ! res_NotLogicOP_2);
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_NotLogicOP_1);
    bool res_ForAllPredicateNotEmpty_3 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl7Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl7(my_id,i);
    bool res_ImpliesLogicOp_4 = true;
    if((L_P1_C1_GetState(it.mainc47) == C1_St_state)){
    res_ImpliesLogicOp_4 = (res_ImpliesLogicOp_4 && (Counter_GetValore(L_P1__GetMainc43(it.mainc47)) == 15230u));
    res_ForAllPredicateNotEmpty_3 = res_ImpliesLogicOp_4;
    if(!res_ForAllPredicateNotEmpty_3) {break;}
    }
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ForAllPredicateNotEmpty_3);
    
    if(res_AndLogicOP_0){
    
    L_P1__SetSubcl28(my_id,1u);
    }
}


/*
    CNL corrispondente:
     { commento: {110,}  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è disattivo, commento: {72,}Azzera il contatore SubClass_C2_contatore_Co1
    
       
     commento: {37,}  se la variabile SubClass_C2_variabile_V6 non è  diverso da GialloxVerdex, commento: {68,}Attiva il timer SubClass_C2_timer_T9
    
       
     commento: {42,}  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L6 è  diverso da  False  commento: {38,} o  se il contatore SubClass_C2_contatore_Co1 è  diverso da  commento: {56,} 12, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V6 il valore GialloxVerdex
    
     ,altrimenti  commento: {71,}Decrementa il contatore SubClass_C2_contatore_Co1
    
    
     commento: {38,}  se il contatore SubClass_C2_contatore_Co1 non è  maggiore di  commento: {54,} 13 commento: {36,} o  se il timer SubClass_C2_timer_T1 è disattivo commento: {34,} o  se il parametro SubClass_C2_parametro_P8 non è  minore di  commento: {55,} 5 commento: {38,} o  se il contatore SubClass_C2_contatore_Co1 è  uguale a  commento: {53,} 1251 commento: {34,} o  se il parametro SubClass_C2_parametro_P6 è  diverso da  False  commento: {35,} o  se il controllo SubClass_C2_controllo_C1 è  uguale a avanzamentox, commento: {66,} Assegna al comando SubClass_C2_comando_C3 il valore avanzamentox
    
       
      se il ripristino dello stato  non è  uguale a  commento: {53,}  state1  commento: {107,} commento: {37,} e  se la variabile SubClass_C2_variabile_V2 non è  diverso da  True  commento: {34,} e  se il parametro SubClass_C2_parametro_P5 è  uguale a avanzamentox, commento: {71,}Decrementa il contatore SubClass_C2_contatore_Co1
    
     ,altrimenti  commento: {69,}Disattiva il timer SubClass_C2_timer_T1
    
    
     }
*/
static inline void L_P1__Effec9(instance_id_t const my_id)
{
    
    //  *110,*  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è disattivo, *72,*Azzera il contatore SubClass_C2_contatore_Co1
    if(Timer_Disattivo(L_P1__GetSubcl31(my_id))){
    
    Counter_Res(L_P1__GetSubcl41(my_id));
    }
    
    //  *37,*  se la variabile SubClass_C2_variabile_V6 non è  diverso da GialloxVerdex, *68,*Attiva il timer SubClass_C2_timer_T9
    bool res_NotLogicOP_0 = true;
    bool res_NotLogicOP_1 = true;
    res_NotLogicOP_1 = (res_NotLogicOP_1 && ! (L_P1__GetSubcl29(my_id) == gialloxverd));
    res_NotLogicOP_0 = (res_NotLogicOP_0 && ! res_NotLogicOP_1);
    if(res_NotLogicOP_0){
    
    Timer_Attiva(L_P1__GetSubcl40(my_id));
    }
    
    //  *42,*  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L6 è  diverso da  False  *38,* o  se il contatore SubClass_C2_contatore_Co1 è  diverso da  *56,* 12, *67,* Assegna alla variabile SubClass_C2_variabile_V6 il valore GialloxVerdex
    //   ,altrimenti  *71,*Decrementa il contatore SubClass_C2_contatore_Co1
    bool res_OrLogicOP_2 = false;
    bool res_ForAllPredicate_3 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl9Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl9(my_id,i);
    bool res_ImpliesLogicOp_4 = true;
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetInMainc3(it.mainc47) == false));
    res_ImpliesLogicOp_4 = (res_ImpliesLogicOp_4 && res_NotLogicOP_5);
    res_ForAllPredicate_3 = res_ImpliesLogicOp_4;
    if(!res_ForAllPredicate_3) {break;}
    }
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_ForAllPredicate_3);
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (Counter_GetValore(L_P1__GetSubcl41(my_id)) == 12u));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_6);
    
    if(res_OrLogicOP_2){
    
    L_P1__SetSubcl29(my_id,gialloxverd);
    }else{
    
    Counter_Decr(L_P1__GetSubcl41(my_id));
    }
    
    //  *38,*  se il contatore SubClass_C2_contatore_Co1 non è  maggiore di  *54,* 13 *36,* o  se il timer SubClass_C2_timer_T1 è disattivo *34,* o  se il parametro SubClass_C2_parametro_P8 non è  minore di  *55,* 5 *38,* o  se il contatore SubClass_C2_contatore_Co1 è  uguale a  *53,* 1251 *34,* o  se il parametro SubClass_C2_parametro_P6 è  diverso da  False  *35,* o  se il controllo SubClass_C2_controllo_C1 è  uguale a avanzamentox, *66,* Assegna al comando SubClass_C2_comando_C3 il valore avanzamentox
    bool res_OrLogicOP_7 = false;
    bool res_OrLogicOP_8 = false;
    bool res_OrLogicOP_9 = false;
    bool res_OrLogicOP_10 = false;
    bool res_OrLogicOP_11 = false;
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (Counter_GetValore(L_P1__GetSubcl41(my_id)) > 13u));
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_NotLogicOP_12);
    res_OrLogicOP_11 = (res_OrLogicOP_11 || Timer_Disattivo(L_P1__GetSubcl38(my_id)));
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_OrLogicOP_11);
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (L_P1__GetParamSubcl12(my_id) < 5u));
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_NotLogicOP_13);
    
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_OrLogicOP_10);
    res_OrLogicOP_9 = (res_OrLogicOP_9 || (Counter_GetValore(L_P1__GetSubcl41(my_id)) == 1251u));
    
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_OrLogicOP_9);
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1__GetParamSubcl11(my_id) == false));
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_NotLogicOP_14);
    
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_OrLogicOP_8);
    res_OrLogicOP_7 = (res_OrLogicOP_7 || (L_P1__GetInSubcl2(my_id) == avanzamento1));
    
    if(res_OrLogicOP_7){
    
    L_P1__SetOutSubcl(my_id,avanzamento1);
    }
    
    //  se il ripristino dello stato  non è  uguale a  *53,*  state1  *107,* *37,* e  se la variabile SubClass_C2_variabile_V2 non è  diverso da  True  *34,* e  se il parametro SubClass_C2_parametro_P5 è  uguale a avanzamentox, *71,*Decrementa il contatore SubClass_C2_contatore_Co1
    //   ,altrimenti  *69,*Disattiva il timer SubClass_C2_timer_T1
    bool res_AndLogicOP_15 = true;
    bool res_AndLogicOP_16 = true;
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! (L_P1__GetStato3(my_id) == C2_St_state));
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_NotLogicOP_17);
    bool res_NotLogicOP_18 = true;
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (L_P1__GetSubcl27(my_id) == true));
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! res_NotLogicOP_19);
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_NotLogicOP_18);
    
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_AndLogicOP_16);
    res_AndLogicOP_15 = (res_AndLogicOP_15 && (L_P1__GetParamSubcl10(my_id) == avanzamento1));
    
    if(res_AndLogicOP_15){
    
    Counter_Decr(L_P1__GetSubcl41(my_id));
    }else{
    
    Timer_Disattiva(L_P1__GetSubcl38(my_id));
    }
}


/*
    CNL corrispondente:
    
    {
    
      se il controllo ConsDef  è  uguale a FALSE ,  commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L2 è  uguale a  commento: {53,}  state1 , commento: {88,} quando  commento: {45,}    MainClass_C1_contatore_Co3 del campo  MainClass_C1     è  uguale a  commento: {53,} 12, commento: {66,} Assegna al comando SubClass_C2_comando_C3 il valore avanzamentox
    
       
      se la macro  SubClass_C2_macrova_M9 ( con argomento_a2   uguale a True ,argomento_a7   uguale a GialloGiallo ,argomento_a3   uguale a avanzamento  e argomento_a4   uguale a c75Giallo )  non  è  diverso da avanzamentox commento: {40,} ,  Applica gli effetti
           della macro SubClass_C2_macroef_M9  commento: {73,}
    
       
     commento: {35,}  se il controllo SubClass_C2_controllo_C8 non è  uguale a  True , commento: {72,}Azzera il contatore SubClass_C2_contatore_Co7
    
       
     commento: {34,}  se lo stato  non è  uguale a  commento: {53,}  state1  commento: {106,} commento: {37,} e  se la variabile SubClass_C2_variabile_V3 è  uguale a  commento: {53,} 2 e  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} e  se il controllo SubClass_C2_controllo_C8 è  uguale a  False  commento: {35,} e  se il controllo SubClass_C2_controllo_C5 non è  diverso da avanzamentox commento: {36,} o  se il timer SubClass_C2_timer_T9 è attivo, commento: {70,}Incrementa il contatore SubClass_C2_contatore_Co1
    
     ,altrimenti  commento: {66,} Assegna al comando SubClass_C2_comando_C6 il valore avanzamentox
    
    
      se la macro  SubClass_C2_macrova_M1 ( con argomento_a1   uguale a c75Giallo ,argomento_a8   uguale a GialloxVerdex  e argomento_a10   uguale a GialloxVerdex )   è  diverso da GialloxVerdex commento: {40,} , commento: {71,}Decrementa il contatore SubClass_C2_contatore_Co1
    
     ,altrimenti  commento: {70,}Incrementa il contatore SubClass_C2_contatore_Co1
    
    
    
    }
*/
static inline void L_P1__Effec10(instance_id_t const my_id)
{
    
    //  se il controllo ConsDef  è  uguale a FALSE ,  *111,*  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L2 è  uguale a  *53,*  state1 , *88,* quando  *45,*    MainClass_C1_contatore_Co3 del campo  MainClass_C1     è  uguale a  *53,* 12, *66,* Assegna al comando SubClass_C2_comando_C3 il valore avanzamentox
    bool res_AndLogicOP_0 = true;
    res_AndLogicOP_0 = (res_AndLogicOP_0 && (L_P1__GetInConsd1(my_id) == false));
    bool res_ForAllPredicate_1 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl7Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl7(my_id,i);
    bool res_ImpliesLogicOp_2 = true;
    if((Counter_GetValore(L_P1__GetMainc43(it.mainc47)) == 12u)){
    res_ImpliesLogicOp_2 = (res_ImpliesLogicOp_2 && (L_P1_C1_GetState(it.mainc47) == C1_St_state));
    }
    res_ForAllPredicate_1 = res_ImpliesLogicOp_2;
    if(!res_ForAllPredicate_1) {break;}
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ForAllPredicate_1);
    
    if(res_AndLogicOP_0){
    
    L_P1__SetOutSubcl(my_id,avanzamento1);
    }
    
    //  se la macro  SubClass_C2_macrova_M9 ( con argomento_a2   uguale a True ,argomento_a7   uguale a GialloGiallo ,argomento_a3   uguale a avanzamento  e argomento_a4   uguale a c75Giallo )  non  è  diverso da avanzamentox *40,* ,  Applica gli effetti
    //         della macro SubClass_C2_macroef_M9
    bool res_NotLogicOP_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__Macro19(my_id,true,avanzamento,c75giallo,giallogiall) == avanzamento1));
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! res_NotLogicOP_4);
    if(res_NotLogicOP_3){
    
    L_P1__Macro14(my_id);
    }
    
    //  *73,*
    //     
    //   *35,*  se il controllo SubClass_C2_controllo_C8 non è  uguale a  True , *72,*Azzera il contatore SubClass_C2_contatore_Co7
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetInSubcl6(my_id) == true));
    if(res_NotLogicOP_5){
    
    Counter_Res(L_P1__GetSubcl42(my_id));
    }
    
    //  *34,*  se lo stato  non è  uguale a  *53,*  state1  *106,* *37,* e  se la variabile SubClass_C2_variabile_V3 è  uguale a  *53,* 2 e  se il controllo ConsDef  è  uguale a FALSE  *35,* e  se il controllo SubClass_C2_controllo_C8 è  uguale a  False  *35,* e  se il controllo SubClass_C2_controllo_C5 non è  diverso da avanzamentox *36,* o  se il timer SubClass_C2_timer_T9 è attivo, *70,*Incrementa il contatore SubClass_C2_contatore_Co1
    //   ,altrimenti  *66,* Assegna al comando SubClass_C2_comando_C6 il valore avanzamentox
    bool res_OrLogicOP_6 = false;
    bool res_AndLogicOP_7 = true;
    bool res_AndLogicOP_8 = true;
    bool res_AndLogicOP_9 = true;
    bool res_AndLogicOP_10 = true;
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (L_P1_C2_GetState(my_id) == C2_St_state));
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_NotLogicOP_11);
    res_AndLogicOP_10 = (res_AndLogicOP_10 && (L_P1__GetSubcl28(my_id) == 2u));
    
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_AndLogicOP_10);
    res_AndLogicOP_9 = (res_AndLogicOP_9 && (L_P1__GetInConsd1(my_id) == false));
    
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_AndLogicOP_9);
    res_AndLogicOP_8 = (res_AndLogicOP_8 && (L_P1__GetInSubcl6(my_id) == false));
    
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_AndLogicOP_8);
    bool res_NotLogicOP_12 = true;
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (L_P1__GetInSubcl5(my_id) == avanzamento1));
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! res_NotLogicOP_13);
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_12);
    
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_AndLogicOP_7);
    res_OrLogicOP_6 = (res_OrLogicOP_6 || Timer_Attivo(L_P1__GetSubcl40(my_id)));
    
    if(res_OrLogicOP_6){
    
    Counter_Incr(L_P1__GetSubcl41(my_id));
    }else{
    
    L_P1__SetOutSubcl1(my_id,avanzamento1);
    }
    
    //  se la macro  SubClass_C2_macrova_M1 ( con argomento_a1   uguale a c75Giallo ,argomento_a8   uguale a GialloxVerdex  e argomento_a10   uguale a GialloxVerdex )   è  diverso da GialloxVerdex *40,* , *71,*Decrementa il contatore SubClass_C2_contatore_Co1
    //   ,altrimenti  *70,*Incrementa il contatore SubClass_C2_contatore_Co1
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1__Macro15(my_id,c75giallo,gialloxverd,gialloxverd) == gialloxverd));
    if(res_NotLogicOP_14){
    
    Counter_Decr(L_P1__GetSubcl41(my_id));
    }else{
    
    Counter_Incr(L_P1__GetSubcl41(my_id));
    }
}


/*
    CNL corrispondente:
    
    {
    
      se la macro  SubClass_C2_macrova_M5 ( con argomento_a8   uguale a avanzamento ,argomento_a10   uguale a RossoGialloGiallo ,argomento_a5   uguale a c75Giallo ,argomento_a9   uguale a GialloaVerdea  e argomento_a6   uguale a GialloaVerdea )   è  uguale a  False  commento: {40,}  commento: {38,} o  se il contatore SubClass_C2_contatore_Co1 non è  minore di  commento: {55,} 1512 commento: {35,} e  se il controllo SubClass_C2_controllo_C8 è  uguale a  False  commento: {35,} e  se il controllo SubClass_C2_controllo_C5 non è  uguale a avanzamentox, commento: {68,}Attiva il timer SubClass_C2_timer_T8
    
       
     commento: {43,}  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L4 è attivo commento: {36,} e  se il timer SubClass_C2_timer_T9 è attivo commento: {37,} o  se la variabile SubClass_C2_variabile_V6 è  uguale a GialloxVerdex, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V3 il valore 4
    
     ,altrimenti  commento: {68,}Attiva il timer SubClass_C2_timer_T1
    
    
    
    }
*/
static inline void L_P1__Effec11(instance_id_t const my_id)
{
    
    //  se la macro  SubClass_C2_macrova_M5 ( con argomento_a8   uguale a avanzamento ,argomento_a10   uguale a RossoGialloGiallo ,argomento_a5   uguale a c75Giallo ,argomento_a9   uguale a GialloaVerdea  e argomento_a6   uguale a GialloaVerdea )   è  uguale a  False  *40,*  *38,* o  se il contatore SubClass_C2_contatore_Co1 non è  minore di  *55,* 1512 *35,* e  se il controllo SubClass_C2_controllo_C8 è  uguale a  False  *35,* e  se il controllo SubClass_C2_controllo_C5 non è  uguale a avanzamentox, *68,*Attiva il timer SubClass_C2_timer_T8
    bool res_OrLogicOP_0 = false;
    res_OrLogicOP_0 = (res_OrLogicOP_0 || (L_P1__Macro17(my_id,rossogiallo2,c75giallo,gialloaverd,avanzamento,gialloaverd) == false));
    bool res_AndLogicOP_1 = true;
    bool res_AndLogicOP_2 = true;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (Counter_GetValore(L_P1__GetSubcl41(my_id)) < 1512u));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_3);
    res_AndLogicOP_2 = (res_AndLogicOP_2 && (L_P1__GetInSubcl6(my_id) == false));
    
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_AndLogicOP_2);
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetInSubcl5(my_id) == avanzamento1));
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_4);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_1);
    
    if(res_OrLogicOP_0){
    
    Timer_Attiva(L_P1__GetSubcl39(my_id));
    }
    
    //  *43,*  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L4 è attivo *36,* e  se il timer SubClass_C2_timer_T9 è attivo *37,* o  se la variabile SubClass_C2_variabile_V6 è  uguale a GialloxVerdex, *67,* Assegna alla variabile SubClass_C2_variabile_V3 il valore 4
    //   ,altrimenti  *68,*Attiva il timer SubClass_C2_timer_T1
    bool res_OrLogicOP_5 = false;
    bool res_AndLogicOP_6 = true;
    bool res_ForAllPredicate_7 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl8Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl8(my_id,i);
    bool res_ImpliesLogicOp_8 = true;
    res_ImpliesLogicOp_8 = (res_ImpliesLogicOp_8 && Timer_Attivo(L_P1__GetMainc40(it.mainc47)));
    res_ForAllPredicate_7 = res_ImpliesLogicOp_8;
    if(!res_ForAllPredicate_7) {break;}
    }
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_ForAllPredicate_7);
    res_AndLogicOP_6 = (res_AndLogicOP_6 && Timer_Attivo(L_P1__GetSubcl40(my_id)));
    
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_AndLogicOP_6);
    res_OrLogicOP_5 = (res_OrLogicOP_5 || (L_P1__GetSubcl29(my_id) == gialloxverd));
    
    if(res_OrLogicOP_5){
    
    L_P1__SetSubcl28(my_id,4u);
    }else{
    
    Timer_Attiva(L_P1__GetSubcl38(my_id));
    }
}


/*
    CNL corrispondente:
     { commento: {43,}  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  commento: {105,} è attivo commento: {34,} e  se il parametro SubClass_C2_parametro_P6 non è  uguale a  False  commento: {37,} e  se la variabile SubClass_C2_variabile_V2 non è  diverso da  False  commento: {36,} o  se il timer SubClass_C2_timer_T1 non è attivo, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V2 il valore  True 
    
       
     commento: {110,}  se il ripristino del timer  SubClass_C2_restoreTI_TI2 non è disattivo, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V3 il valore 9
    
     ,altrimenti   Applica gli effetti
           della macro SubClass_C2_macroef_M9  commento: {73,}
    
    
      se il controllo ConsDef  è  uguale a FALSE , commento: {69,}Disattiva il timer SubClass_C2_timer_T1
    
       
     commento: {109,}  se il ripristino della variabile  SubClass_C2_restoreva_RV1 non è  uguale a  False ,  Applica gli effetti
           della macro SubClass_C2_macroef_M9  commento: {73,}
    
     ,altrimenti  commento: {71,}Decrementa il contatore SubClass_C2_contatore_Co1
    
    
     }
*/
static inline void L_P1__Effec12(instance_id_t const my_id)
{
    
    //  *43,*  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  *105,* è attivo *34,* e  se il parametro SubClass_C2_parametro_P6 non è  uguale a  False  *37,* e  se la variabile SubClass_C2_variabile_V2 non è  diverso da  False  *36,* o  se il timer SubClass_C2_timer_T1 non è attivo, *67,* Assegna alla variabile SubClass_C2_variabile_V2 il valore  True
    bool res_OrLogicOP_0 = false;
    bool res_AndLogicOP_1 = true;
    bool res_AndLogicOP_2 = true;
    bool res_ForAllPredicateNotEmpty_3 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl9Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl9(my_id,i);
    bool res_ImpliesLogicOp_4 = true;
    res_ImpliesLogicOp_4 = (res_ImpliesLogicOp_4 && Timer_Attivo(L_P1__GetMainc40(it.mainc47)));
    res_ForAllPredicateNotEmpty_3 = res_ImpliesLogicOp_4;
    if(!res_ForAllPredicateNotEmpty_3) {break;}
    }
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_ForAllPredicateNotEmpty_3);
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetParamSubcl11(my_id) == false));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_5);
    
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_AndLogicOP_2);
    bool res_NotLogicOP_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetSubcl27(my_id) == false));
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! res_NotLogicOP_7);
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_6);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_1);
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! Timer_Attivo(L_P1__GetSubcl38(my_id)));
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_8);
    
    if(res_OrLogicOP_0){
    
    L_P1__SetSubcl27(my_id,true);
    }
    
    //  *110,*  se il ripristino del timer  SubClass_C2_restoreTI_TI2 non è disattivo, *67,* Assegna alla variabile SubClass_C2_variabile_V3 il valore 9
    //   ,altrimenti   Applica gli effetti
    //         della macro SubClass_C2_macroef_M9
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! Timer_Disattivo(L_P1__GetSubcl33(my_id)));
    if(res_NotLogicOP_9){
    
    L_P1__SetSubcl28(my_id,9u);
    }else{
    
    L_P1__Macro14(my_id);
    }
    
    //  *73,*
    //    se il controllo ConsDef  è  uguale a FALSE , *69,*Disattiva il timer SubClass_C2_timer_T1
    if((L_P1__GetInConsd1(my_id) == false)){
    
    Timer_Disattiva(L_P1__GetSubcl38(my_id));
    }
    
    //  *109,*  se il ripristino della variabile  SubClass_C2_restoreva_RV1 non è  uguale a  False ,  Applica gli effetti
    //         della macro SubClass_C2_macroef_M9  *73,*
    //   ,altrimenti  *71,*Decrementa il contatore SubClass_C2_contatore_Co1
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__GetSubcl26(my_id) == false));
    if(res_NotLogicOP_10){
    
    L_P1__Macro14(my_id);
    }else{
    
    Counter_Decr(L_P1__GetSubcl41(my_id));
    }
}


/*
    CNL corrispondente:
     { commento: {37,}  se la variabile SubClass_C2_variabile_V2 è  uguale a  False  commento: {38,} e  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  commento: {56,} 14 o  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} o  se il contatore SubClass_C2_contatore_Co1 non è  minore di  commento: {55,} 11123 commento: {37,} o  se la variabile SubClass_C2_variabile_V3 non è  minore di  commento: {55,} 8 commento: {35,} o  se il controllo SubClass_C2_controllo_C8 è  diverso da  False ,  Applica gli effetti
           della macro SubClass_C2_macroef_M3( con argomento_af1   uguale a c270 ,argomento_af8   uguale a GialloaVerdea ,argomento_af10   uguale a True ,argomento_af5   uguale a GialloaVerdea ) commento: {73,}
    
     ,altrimenti  commento: {66,} Assegna al comando SubClass_C2_comando_C3 il valore avanzamentox
    
    
     }
*/
static inline void L_P1__Effec13(instance_id_t const my_id)
{
    
    //  *37,*  se la variabile SubClass_C2_variabile_V2 è  uguale a  False  *38,* e  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  *56,* 14 o  se il controllo ConsDef  è  uguale a FALSE  *38,* o  se il contatore SubClass_C2_contatore_Co1 non è  minore di  *55,* 11123 *37,* o  se la variabile SubClass_C2_variabile_V3 non è  minore di  *55,* 8 *35,* o  se il controllo SubClass_C2_controllo_C8 è  diverso da  False ,  Applica gli effetti
    //         della macro SubClass_C2_macroef_M3( con argomento_af1   uguale a c270 ,argomento_af8   uguale a GialloaVerdea ,argomento_af10   uguale a True ,argomento_af5   uguale a GialloaVerdea ) *73,*
    //   ,altrimenti  *66,* Assegna al comando SubClass_C2_comando_C3 il valore avanzamentox
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_AndLogicOP_4 = true;
    res_AndLogicOP_4 = (res_AndLogicOP_4 && (L_P1__GetSubcl27(my_id) == false));
    bool res_NotLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (Counter_GetValore(L_P1__GetSubcl42(my_id)) == 14u));
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! res_NotLogicOP_6);
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_5);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_AndLogicOP_4);
    res_OrLogicOP_3 = (res_OrLogicOP_3 || (L_P1__GetInConsd1(my_id) == false));
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (Counter_GetValore(L_P1__GetSubcl41(my_id)) < 11123u));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_7);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_OrLogicOP_2);
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetSubcl28(my_id) < 8u));
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_NotLogicOP_8);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetInSubcl6(my_id) == false));
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_9);
    
    if(res_OrLogicOP_0){
    
    L_P1__Macro11(my_id,c270,true,gialloaverd,gialloaverd);
    }else{
    
    L_P1__SetOutSubcl(my_id,avanzamento1);
    }
}


/*
    CNL corrispondente:
     { commento: {37,}  se la variabile SubClass_C2_variabile_V2 non è  diverso da  True ,  commento: {42,}  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L4 è  uguale a RossoGialloaVerdea, commento: {88,} quando  commento: {45,}    MainClass_C1_contatore_Co9 del campo  MainClass_C1     commento: {105,} è  maggiore di  commento: {54,} 1104 commento: {34,} e  se il parametro SubClass_C2_parametro_P8 è  maggiore di  commento: {54,} 10 commento: {37,} e  se la variabile SubClass_C2_variabile_V3 non è  diverso da  commento: {56,} 4 commento: {35,} o  se il controllo SubClass_C2_controllo_C8 è  uguale a  False  commento: {36,} o  se il timer SubClass_C2_timer_T9 non è disattivo commento: {36,} e  se il timer SubClass_C2_timer_T1 non è attivo, commento: {66,} Assegna al comando SubClass_C2_comando_C6 il valore avanzamentox
    
     ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V2 il valore  False 
    
    
     commento: {34,}  se il parametro SubClass_C2_parametro_P6 è  uguale a  False  commento: {36,} o  se il timer SubClass_C2_timer_T9 è attivo commento: {38,} e  se il contatore SubClass_C2_contatore_Co7 è  uguale a  commento: {53,} 145 o  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} o  se il contatore SubClass_C2_contatore_Co1 non è  uguale a  commento: {53,} 151230, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V2 il valore  True 
    
       
     commento: {110,}  se il ripristino del timer  SubClass_C2_restoreTI_TI4 è disattivo commento: {37,} o  se la variabile SubClass_C2_variabile_V3 è  minore di  commento: {55,} 4 commento: {38,} e  se il contatore SubClass_C2_contatore_Co1 non è  minore di  commento: {55,} 1345 commento: {37,} e  se la variabile SubClass_C2_variabile_V3 non è  uguale a  commento: {53,} 4 commento: {37,} o  se la variabile SubClass_C2_variabile_V2 non è  uguale a  True  commento: {35,} e  se il controllo SubClass_C2_controllo_C8 è  diverso da  False , commento: {72,}Azzera il contatore SubClass_C2_contatore_Co7
    
       
     }
*/
static inline void L_P1__Effec14(instance_id_t const my_id)
{
    
    //  *37,*  se la variabile SubClass_C2_variabile_V2 non è  diverso da  True ,  *42,*  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L4 è  uguale a RossoGialloaVerdea, *88,* quando  *45,*    MainClass_C1_contatore_Co9 del campo  MainClass_C1     *105,* è  maggiore di  *54,* 1104 *34,* e  se il parametro SubClass_C2_parametro_P8 è  maggiore di  *54,* 10 *37,* e  se la variabile SubClass_C2_variabile_V3 non è  diverso da  *56,* 4 *35,* o  se il controllo SubClass_C2_controllo_C8 è  uguale a  False  *36,* o  se il timer SubClass_C2_timer_T9 non è disattivo *36,* e  se il timer SubClass_C2_timer_T1 non è attivo, *66,* Assegna al comando SubClass_C2_comando_C6 il valore avanzamentox
    //   ,altrimenti  *67,* Assegna alla variabile SubClass_C2_variabile_V2 il valore  False
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_AndLogicOP_2 = true;
    bool res_AndLogicOP_3 = true;
    bool res_AndLogicOP_4 = true;
    bool res_NotLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetSubcl27(my_id) == true));
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! res_NotLogicOP_6);
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_5);
    bool res_ForAllPredicate_7 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl8Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl8(my_id,i);
    bool res_ImpliesLogicOp_8 = true;
    if((Counter_GetValore(L_P1__GetMainc46(it.mainc47)) > 1104u)){
    res_ImpliesLogicOp_8 = (res_ImpliesLogicOp_8 && (L_P1__GetInMainc5(it.mainc47) == rossogiallo));
    }
    res_ForAllPredicate_7 = res_ImpliesLogicOp_8;
    if(!res_ForAllPredicate_7) {break;}
    }
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_ForAllPredicate_7);
    
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_AndLogicOP_4);
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (L_P1__GetParamSubcl12(my_id) > 10u));
    
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_AndLogicOP_3);
    bool res_NotLogicOP_9 = true;
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__GetSubcl28(my_id) == 4u));
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! res_NotLogicOP_10);
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_9);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_2);
    res_OrLogicOP_1 = (res_OrLogicOP_1 || (L_P1__GetInSubcl6(my_id) == false));
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_AndLogicOP_11 = true;
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! Timer_Disattivo(L_P1__GetSubcl40(my_id)));
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_NotLogicOP_12);
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! Timer_Attivo(L_P1__GetSubcl38(my_id)));
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_NotLogicOP_13);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_11);
    
    if(res_OrLogicOP_0){
    
    L_P1__SetOutSubcl1(my_id,avanzamento1);
    }else{
    
    L_P1__SetSubcl27(my_id,false);
    }
    
    //  *34,*  se il parametro SubClass_C2_parametro_P6 è  uguale a  False  *36,* o  se il timer SubClass_C2_timer_T9 è attivo *38,* e  se il contatore SubClass_C2_contatore_Co7 è  uguale a  *53,* 145 o  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  *38,* o  se il contatore SubClass_C2_contatore_Co1 non è  uguale a  *53,* 151230, *67,* Assegna alla variabile SubClass_C2_variabile_V2 il valore  True
    bool res_OrLogicOP_14 = false;
    bool res_OrLogicOP_15 = false;
    bool res_OrLogicOP_16 = false;
    bool res_OrLogicOP_17 = false;
    res_OrLogicOP_17 = (res_OrLogicOP_17 || (L_P1__GetParamSubcl11(my_id) == false));
    bool res_AndLogicOP_18 = true;
    res_AndLogicOP_18 = (res_AndLogicOP_18 && Timer_Attivo(L_P1__GetSubcl40(my_id)));
    res_AndLogicOP_18 = (res_AndLogicOP_18 && (Counter_GetValore(L_P1__GetSubcl42(my_id)) == 145u));
    
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_AndLogicOP_18);
    
    res_OrLogicOP_16 = (res_OrLogicOP_16 || res_OrLogicOP_17);
    res_OrLogicOP_16 = (res_OrLogicOP_16 || (L_P1__GetInConsd1(my_id) == false));
    
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_OrLogicOP_16);
    res_OrLogicOP_15 = (res_OrLogicOP_15 || (L_P1__GetInConsd1(my_id) == false));
    
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_OrLogicOP_15);
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (Counter_GetValore(L_P1__GetSubcl41(my_id)) == 151230u));
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_NotLogicOP_19);
    
    if(res_OrLogicOP_14){
    
    L_P1__SetSubcl27(my_id,true);
    }
    
    //  *110,*  se il ripristino del timer  SubClass_C2_restoreTI_TI4 è disattivo *37,* o  se la variabile SubClass_C2_variabile_V3 è  minore di  *55,* 4 *38,* e  se il contatore SubClass_C2_contatore_Co1 non è  minore di  *55,* 1345 *37,* e  se la variabile SubClass_C2_variabile_V3 non è  uguale a  *53,* 4 *37,* o  se la variabile SubClass_C2_variabile_V2 non è  uguale a  True  *35,* e  se il controllo SubClass_C2_controllo_C8 è  diverso da  False , *72,*Azzera il contatore SubClass_C2_contatore_Co7
    bool res_OrLogicOP_20 = false;
    bool res_OrLogicOP_21 = false;
    res_OrLogicOP_21 = (res_OrLogicOP_21 || Timer_Disattivo(L_P1__GetSubcl37(my_id)));
    bool res_AndLogicOP_22 = true;
    bool res_AndLogicOP_23 = true;
    res_AndLogicOP_23 = (res_AndLogicOP_23 && (L_P1__GetSubcl28(my_id) < 4u));
    bool res_NotLogicOP_24 = true;
    res_NotLogicOP_24 = (res_NotLogicOP_24 && ! (Counter_GetValore(L_P1__GetSubcl41(my_id)) < 1345u));
    res_AndLogicOP_23 = (res_AndLogicOP_23 && res_NotLogicOP_24);
    
    res_AndLogicOP_22 = (res_AndLogicOP_22 && res_AndLogicOP_23);
    bool res_NotLogicOP_25 = true;
    res_NotLogicOP_25 = (res_NotLogicOP_25 && ! (L_P1__GetSubcl28(my_id) == 4u));
    res_AndLogicOP_22 = (res_AndLogicOP_22 && res_NotLogicOP_25);
    
    res_OrLogicOP_21 = (res_OrLogicOP_21 || res_AndLogicOP_22);
    
    res_OrLogicOP_20 = (res_OrLogicOP_20 || res_OrLogicOP_21);
    bool res_AndLogicOP_26 = true;
    bool res_NotLogicOP_27 = true;
    res_NotLogicOP_27 = (res_NotLogicOP_27 && ! (L_P1__GetSubcl27(my_id) == true));
    res_AndLogicOP_26 = (res_AndLogicOP_26 && res_NotLogicOP_27);
    bool res_NotLogicOP_28 = true;
    res_NotLogicOP_28 = (res_NotLogicOP_28 && ! (L_P1__GetInSubcl6(my_id) == false));
    res_AndLogicOP_26 = (res_AndLogicOP_26 && res_NotLogicOP_28);
    
    res_OrLogicOP_20 = (res_OrLogicOP_20 || res_AndLogicOP_26);
    
    if(res_OrLogicOP_20){
    
    Counter_Res(L_P1__GetSubcl42(my_id));
    }
}


/*
    CNL corrispondente:
     { commento: {42,}  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L4 è  diverso da RossoGialloaVerdea commento: {35,} e  se il controllo SubClass_C2_controllo_C8 è  uguale a  True  commento: {35,} e  se il controllo SubClass_C2_controllo_C8 non è  diverso da  True  commento: {35,} e  se il controllo SubClass_C2_controllo_C1 non è  uguale a avanzamentox commento: {38,} o  se il contatore SubClass_C2_contatore_Co7 non è  minore di  commento: {55,} 154 commento: {36,} e  se il timer SubClass_C2_timer_T1 è attivo,  Applica gli effetti
           della macro SubClass_C2_macroef_M9  commento: {73,}
    
     ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V3 il valore 2
    
    
     commento: {109,}  se il ripristino della variabile  SubClass_C2_restoreva_RV1 non è  diverso da  True  commento: {34,} e  se il parametro SubClass_C2_parametro_P5 non è  diverso da avanzamentox commento: {34,} e  se il parametro SubClass_C2_parametro_P6 è  diverso da  True ,  Applica gli effetti
           della macro SubClass_C2_macroef_M3( con argomento_af1   uguale a avanzamentox ,argomento_af8   uguale a avanzamento ,argomento_af10   uguale a True ,argomento_af5   uguale a GialloaVerdea ) commento: {73,}
    
     ,altrimenti  commento: {66,} Assegna al comando SubClass_C2_comando_C3 il valore avanzamentox
    
    
     }
*/
static inline void L_P1__Effec15(instance_id_t const my_id)
{
    
    //  *42,*  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L4 è  diverso da RossoGialloaVerdea *35,* e  se il controllo SubClass_C2_controllo_C8 è  uguale a  True  *35,* e  se il controllo SubClass_C2_controllo_C8 non è  diverso da  True  *35,* e  se il controllo SubClass_C2_controllo_C1 non è  uguale a avanzamentox *38,* o  se il contatore SubClass_C2_contatore_Co7 non è  minore di  *55,* 154 *36,* e  se il timer SubClass_C2_timer_T1 è attivo,  Applica gli effetti
    //         della macro SubClass_C2_macroef_M9  *73,*
    //   ,altrimenti  *67,* Assegna alla variabile SubClass_C2_variabile_V3 il valore 2
    bool res_OrLogicOP_0 = false;
    bool res_AndLogicOP_1 = true;
    bool res_AndLogicOP_2 = true;
    bool res_AndLogicOP_3 = true;
    bool res_ForAllPredicate_4 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl8Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl8(my_id,i);
    bool res_ImpliesLogicOp_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetInMainc5(it.mainc47) == rossogiallo));
    res_ImpliesLogicOp_5 = (res_ImpliesLogicOp_5 && res_NotLogicOP_6);
    res_ForAllPredicate_4 = res_ImpliesLogicOp_5;
    if(!res_ForAllPredicate_4) {break;}
    }
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_ForAllPredicate_4);
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (L_P1__GetInSubcl6(my_id) == true));
    
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_AndLogicOP_3);
    bool res_NotLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetInSubcl6(my_id) == true));
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! res_NotLogicOP_8);
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_7);
    
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_AndLogicOP_2);
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetInSubcl2(my_id) == avanzamento1));
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_9);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_1);
    bool res_AndLogicOP_10 = true;
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (Counter_GetValore(L_P1__GetSubcl42(my_id)) < 154u));
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_NotLogicOP_11);
    res_AndLogicOP_10 = (res_AndLogicOP_10 && Timer_Attivo(L_P1__GetSubcl38(my_id)));
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_10);
    
    if(res_OrLogicOP_0){
    
    L_P1__Macro14(my_id);
    }else{
    
    L_P1__SetSubcl28(my_id,2u);
    }
    
    //  *109,*  se il ripristino della variabile  SubClass_C2_restoreva_RV1 non è  diverso da  True  *34,* e  se il parametro SubClass_C2_parametro_P5 non è  diverso da avanzamentox *34,* e  se il parametro SubClass_C2_parametro_P6 è  diverso da  True ,  Applica gli effetti
    //         della macro SubClass_C2_macroef_M3( con argomento_af1   uguale a avanzamentox ,argomento_af8   uguale a avanzamento ,argomento_af10   uguale a True ,argomento_af5   uguale a GialloaVerdea ) *73,*
    //   ,altrimenti  *66,* Assegna al comando SubClass_C2_comando_C3 il valore avanzamentox
    bool res_AndLogicOP_12 = true;
    bool res_AndLogicOP_13 = true;
    bool res_NotLogicOP_14 = true;
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (L_P1__GetSubcl26(my_id) == true));
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! res_NotLogicOP_15);
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_NotLogicOP_14);
    bool res_NotLogicOP_16 = true;
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! (L_P1__GetParamSubcl10(my_id) == avanzamento1));
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! res_NotLogicOP_17);
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_NotLogicOP_16);
    
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_AndLogicOP_13);
    bool res_NotLogicOP_18 = true;
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! (L_P1__GetParamSubcl11(my_id) == true));
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_NotLogicOP_18);
    
    if(res_AndLogicOP_12){
    
    L_P1__Macro11(my_id,avanzamento1,true,gialloaverd,avanzamento);
    }else{
    
    L_P1__SetOutSubcl(my_id,avanzamento1);
    }
}


/*
    CNL corrispondente:
     { commento: {36,}  se il timer SubClass_C2_timer_T9 non è attivo commento: {35,} o  se il controllo SubClass_C2_controllo_C1 è  diverso da avanzamentox commento: {37,} e  se la variabile SubClass_C2_variabile_V6 è  diverso da GialloxVerdex commento: {37,} o  se la variabile SubClass_C2_variabile_V2 è  uguale a  True  commento: {38,} e  se il contatore SubClass_C2_contatore_Co1 è  diverso da  commento: {56,} 11512, commento: {66,} Assegna al comando SubClass_C2_comando_C6 il valore avanzamentox
    
       
     commento: {109,}  se il ripristino della variabile  SubClass_C2_restoreva_RV1 è  diverso da  True  commento: {36,} e  se il timer SubClass_C2_timer_T8 è scaduto commento: {35,} e  se il controllo SubClass_C2_controllo_C1 è  uguale a avanzamentox commento: {37,} e  se la variabile SubClass_C2_variabile_V2 è  diverso da  True  commento: {37,} e  se la variabile SubClass_C2_variabile_V2 è  uguale a  False , commento: {66,} Assegna al comando SubClass_C2_comando_C3 il valore avanzamentox
    
       
      se il controllo ConsDef  è  uguale a FALSE ,  Applica gli effetti
           della macro SubClass_C2_macroef_M7   commento: {73,}
    
     ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V3 il valore 6
    
    
      se il controllo ConsDef  è  uguale a FALSE ,  commento: {41,}  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L4 è  maggiore di  commento: {54,} 7, commento: {88,} quando  commento: {44,}    MainClass_C1_variabile_V10 del campo  MainClass_C1     commento: {105,} è  uguale a  True  commento: {37,} o  se la variabile SubClass_C2_variabile_V6 non è  diverso da GialloxVerdex commento: {35,} e  se il controllo SubClass_C2_controllo_C8 non è  diverso da  True  commento: {37,} o  se la variabile SubClass_C2_variabile_V6 non è  uguale a GialloxVerdex, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V2 il valore  True 
    
     ,altrimenti  commento: {68,}Attiva il timer SubClass_C2_timer_T9
    
    
     commento: {109,}  se il ripristino della variabile  SubClass_C2_restoreva_RV1 è  uguale a  True ,  Applica gli effetti
           della macro SubClass_C2_macroef_M3( con argomento_af1   uguale a avanzamentox ,argomento_af8   uguale a GialloaVerdea ,argomento_af10   uguale a True ,argomento_af5   uguale a GialloaVerdea ) commento: {73,}
    
       
     }
*/
static inline void L_P1__Effec16(instance_id_t const my_id)
{
    
    //  *36,*  se il timer SubClass_C2_timer_T9 non è attivo *35,* o  se il controllo SubClass_C2_controllo_C1 è  diverso da avanzamentox *37,* e  se la variabile SubClass_C2_variabile_V6 è  diverso da GialloxVerdex *37,* o  se la variabile SubClass_C2_variabile_V2 è  uguale a  True  *38,* e  se il contatore SubClass_C2_contatore_Co1 è  diverso da  *56,* 11512, *66,* Assegna al comando SubClass_C2_comando_C6 il valore avanzamentox
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! Timer_Attivo(L_P1__GetSubcl40(my_id)));
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_NotLogicOP_2);
    bool res_AndLogicOP_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetInSubcl2(my_id) == avanzamento1));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_4);
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetSubcl29(my_id) == gialloxverd));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_5);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_3);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_AndLogicOP_6 = true;
    res_AndLogicOP_6 = (res_AndLogicOP_6 && (L_P1__GetSubcl27(my_id) == true));
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (Counter_GetValore(L_P1__GetSubcl41(my_id)) == 11512u));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_7);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_6);
    
    if(res_OrLogicOP_0){
    
    L_P1__SetOutSubcl1(my_id,avanzamento1);
    }
    
    //  *109,*  se il ripristino della variabile  SubClass_C2_restoreva_RV1 è  diverso da  True  *36,* e  se il timer SubClass_C2_timer_T8 è scaduto *35,* e  se il controllo SubClass_C2_controllo_C1 è  uguale a avanzamentox *37,* e  se la variabile SubClass_C2_variabile_V2 è  diverso da  True  *37,* e  se la variabile SubClass_C2_variabile_V2 è  uguale a  False , *66,* Assegna al comando SubClass_C2_comando_C3 il valore avanzamentox
    bool res_AndLogicOP_8 = true;
    bool res_AndLogicOP_9 = true;
    bool res_AndLogicOP_10 = true;
    bool res_AndLogicOP_11 = true;
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (L_P1__GetSubcl26(my_id) == true));
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_NotLogicOP_12);
    res_AndLogicOP_11 = (res_AndLogicOP_11 && Timer_Scaduto(L_P1__GetSubcl39(my_id)));
    
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_AndLogicOP_11);
    res_AndLogicOP_10 = (res_AndLogicOP_10 && (L_P1__GetInSubcl2(my_id) == avanzamento1));
    
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_AndLogicOP_10);
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (L_P1__GetSubcl27(my_id) == true));
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_NotLogicOP_13);
    
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_AndLogicOP_9);
    res_AndLogicOP_8 = (res_AndLogicOP_8 && (L_P1__GetSubcl27(my_id) == false));
    
    if(res_AndLogicOP_8){
    
    L_P1__SetOutSubcl(my_id,avanzamento1);
    }
    
    //  se il controllo ConsDef  è  uguale a FALSE ,  Applica gli effetti
    //         della macro SubClass_C2_macroef_M7   *73,*
    //   ,altrimenti  *67,* Assegna alla variabile SubClass_C2_variabile_V3 il valore 6
    if((L_P1__GetInConsd1(my_id) == false)){
    
    L_P1__Macro13(my_id);
    }else{
    
    L_P1__SetSubcl28(my_id,6u);
    }
    
    //  se il controllo ConsDef  è  uguale a FALSE ,  *41,*  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L4 è  maggiore di  *54,* 7, *88,* quando  *44,*    MainClass_C1_variabile_V10 del campo  MainClass_C1     *105,* è  uguale a  True  *37,* o  se la variabile SubClass_C2_variabile_V6 non è  diverso da GialloxVerdex *35,* e  se il controllo SubClass_C2_controllo_C8 non è  diverso da  True  *37,* o  se la variabile SubClass_C2_variabile_V6 non è  uguale a GialloxVerdex, *67,* Assegna alla variabile SubClass_C2_variabile_V2 il valore  True 
    //   ,altrimenti  *68,*Attiva il timer SubClass_C2_timer_T9
    bool res_OrLogicOP_14 = false;
    bool res_OrLogicOP_15 = false;
    bool res_AndLogicOP_16 = true;
    res_AndLogicOP_16 = (res_AndLogicOP_16 && (L_P1__GetInConsd1(my_id) == false));
    bool res_ForAllPredicate_17 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl8Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl8(my_id,i);
    bool res_ImpliesLogicOp_18 = true;
    if((L_P1__GetMainc32(it.mainc47) == true)){
    res_ImpliesLogicOp_18 = (res_ImpliesLogicOp_18 && (L_P1__GetParamMainc7(it.mainc47) > 7u));
    }
    res_ForAllPredicate_17 = res_ImpliesLogicOp_18;
    if(!res_ForAllPredicate_17) {break;}
    }
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_ForAllPredicate_17);
    
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_AndLogicOP_16);
    bool res_AndLogicOP_19 = true;
    bool res_NotLogicOP_20 = true;
    bool res_NotLogicOP_21 = true;
    res_NotLogicOP_21 = (res_NotLogicOP_21 && ! (L_P1__GetSubcl29(my_id) == gialloxverd));
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! res_NotLogicOP_21);
    res_AndLogicOP_19 = (res_AndLogicOP_19 && res_NotLogicOP_20);
    bool res_NotLogicOP_22 = true;
    bool res_NotLogicOP_23 = true;
    res_NotLogicOP_23 = (res_NotLogicOP_23 && ! (L_P1__GetInSubcl6(my_id) == true));
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! res_NotLogicOP_23);
    res_AndLogicOP_19 = (res_AndLogicOP_19 && res_NotLogicOP_22);
    
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_AndLogicOP_19);
    
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_OrLogicOP_15);
    bool res_NotLogicOP_24 = true;
    res_NotLogicOP_24 = (res_NotLogicOP_24 && ! (L_P1__GetSubcl29(my_id) == gialloxverd));
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_NotLogicOP_24);
    
    if(res_OrLogicOP_14){
    
    L_P1__SetSubcl27(my_id,true);
    }else{
    
    Timer_Attiva(L_P1__GetSubcl40(my_id));
    }
    
    //  *109,*  se il ripristino della variabile  SubClass_C2_restoreva_RV1 è  uguale a  True ,  Applica gli effetti
    //         della macro SubClass_C2_macroef_M3( con argomento_af1   uguale a avanzamentox ,argomento_af8   uguale a GialloaVerdea ,argomento_af10   uguale a True ,argomento_af5   uguale a GialloaVerdea )
    if((L_P1__GetSubcl26(my_id) == true)){
    
    L_P1__Macro11(my_id,avanzamento1,true,gialloaverd,gialloaverd);
    }
}


/*
    CNL corrispondente:
     { commento: {109,}  se il ripristino della variabile  SubClass_C2_restoreva_RV1 è  diverso da  True  e  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} o  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  commento: {54,} 9, commento: {69,}Disattiva il timer SubClass_C2_timer_T9
    
       
     }
*/
static inline void L_P1__Effec17(instance_id_t const my_id)
{
    
    //  *109,*  se il ripristino della variabile  SubClass_C2_restoreva_RV1 è  diverso da  True  e  se il controllo ConsDef  è  uguale a FALSE  *34,* o  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  *54,* 9, *69,*Disattiva il timer SubClass_C2_timer_T9
    bool res_OrLogicOP_0 = false;
    bool res_AndLogicOP_1 = true;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (L_P1__GetSubcl26(my_id) == true));
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_2);
    res_AndLogicOP_1 = (res_AndLogicOP_1 && (L_P1__GetInConsd1(my_id) == false));
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_1);
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__GetParamSubcl12(my_id) > 9u));
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_3);
    
    if(res_OrLogicOP_0){
    
    Timer_Disattiva(L_P1__GetSubcl40(my_id));
    }
}


/*
    CNL corrispondente:
    
    {
    
     commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  commento: {105,} è  uguale a  commento: {53,}  state1  commento: {36,} e  se il timer SubClass_C2_timer_T9 non è attivo commento: {35,} e  se il controllo SubClass_C2_controllo_C8 è  uguale a  True  commento: {34,} o  se il parametro SubClass_C2_parametro_P5 non è  uguale a avanzamentox commento: {36,} o  se il timer SubClass_C2_timer_T1 è attivo commento: {36,} e  se il timer SubClass_C2_timer_T9 non è disattivo, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V3 il valore 6
    
     ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V3 il valore 1
    
    
     commento: {34,}  se il parametro SubClass_C2_parametro_P6 non è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} e  se il controllo SubClass_C2_controllo_C8 non è  uguale a  False  commento: {34,} e  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  commento: {54,} 2,  Applica gli effetti
           della macro SubClass_C2_macroef_M6  commento: {73,}
    
       
     commento: {43,}  se MainClass_C1_timer_T4 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  commento: {105,} è attivo o  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro SubClass_C2_parametro_P8 è  minore di  commento: {55,} 6 o  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} o  se la variabile SubClass_C2_variabile_V3 è  diverso da  commento: {56,} 4 commento: {36,} o  se il timer SubClass_C2_timer_T8 non è disattivo, commento: {72,}Azzera il contatore SubClass_C2_contatore_Co1
    
     ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V3 il valore 6
    
    
     commento: {35,}  se il controllo SubClass_C2_controllo_C8 è  uguale a  True  commento: {38,} e  se il contatore SubClass_C2_contatore_Co1 è  diverso da  commento: {56,} 15 commento: {36,} o  se il timer SubClass_C2_timer_T1 non è disattivo commento: {34,} o  se il parametro SubClass_C2_parametro_P5 non è  diverso da avanzamentox commento: {37,} o  se la variabile SubClass_C2_variabile_V3 è  minore di  commento: {55,} 10 commento: {38,} o  se il contatore SubClass_C2_contatore_Co1 non è  minore di  commento: {55,} 144, commento: {71,}Decrementa il contatore SubClass_C2_contatore_Co1
    
       
    
    }
*/
static inline void L_P1__Effec18(instance_id_t const my_id)
{
    
    //  *111,*  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  *105,* è  uguale a  *53,*  state1  *36,* e  se il timer SubClass_C2_timer_T9 non è attivo *35,* e  se il controllo SubClass_C2_controllo_C8 è  uguale a  True  *34,* o  se il parametro SubClass_C2_parametro_P5 non è  uguale a avanzamentox *36,* o  se il timer SubClass_C2_timer_T1 è attivo *36,* e  se il timer SubClass_C2_timer_T9 non è disattivo, *67,* Assegna alla variabile SubClass_C2_variabile_V3 il valore 6
    //   ,altrimenti  *67,* Assegna alla variabile SubClass_C2_variabile_V3 il valore 1
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_AndLogicOP_2 = true;
    bool res_AndLogicOP_3 = true;
    bool res_ForAllPredicateNotEmpty_4 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl9Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl9(my_id,i);
    bool res_ImpliesLogicOp_5 = true;
    res_ImpliesLogicOp_5 = (res_ImpliesLogicOp_5 && (L_P1_C1_GetState(it.mainc47) == C1_St_state));
    res_ForAllPredicateNotEmpty_4 = res_ImpliesLogicOp_5;
    if(!res_ForAllPredicateNotEmpty_4) {break;}
    }
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_ForAllPredicateNotEmpty_4);
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! Timer_Attivo(L_P1__GetSubcl40(my_id)));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_6);
    
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_AndLogicOP_3);
    res_AndLogicOP_2 = (res_AndLogicOP_2 && (L_P1__GetInSubcl6(my_id) == true));
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_2);
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetParamSubcl10(my_id) == avanzamento1));
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_NotLogicOP_7);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_AndLogicOP_8 = true;
    res_AndLogicOP_8 = (res_AndLogicOP_8 && Timer_Attivo(L_P1__GetSubcl38(my_id)));
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! Timer_Disattivo(L_P1__GetSubcl40(my_id)));
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_9);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_8);
    
    if(res_OrLogicOP_0){
    
    L_P1__SetSubcl28(my_id,6u);
    }else{
    
    L_P1__SetSubcl28(my_id,1u);
    }
    
    //  *34,*  se il parametro SubClass_C2_parametro_P6 non è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE  *35,* e  se il controllo SubClass_C2_controllo_C8 non è  uguale a  False  *34,* e  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  *54,* 2,  Applica gli effetti
    //         della macro SubClass_C2_macroef_M6
    bool res_AndLogicOP_10 = true;
    bool res_AndLogicOP_11 = true;
    bool res_AndLogicOP_12 = true;
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (L_P1__GetParamSubcl11(my_id) == false));
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_NotLogicOP_13);
    res_AndLogicOP_12 = (res_AndLogicOP_12 && (L_P1__GetInConsd1(my_id) == false));
    
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_AndLogicOP_12);
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1__GetInSubcl6(my_id) == false));
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_NotLogicOP_14);
    
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_AndLogicOP_11);
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (L_P1__GetParamSubcl12(my_id) > 2u));
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_NotLogicOP_15);
    
    if(res_AndLogicOP_10){
    
    L_P1__Macro12(my_id);
    }
    
    //  *73,*
    //     
    //   *43,*  se MainClass_C1_timer_T4 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  *105,* è attivo o  se il controllo ConsDef  è  uguale a FALSE  *34,* e  se il parametro SubClass_C2_parametro_P8 è  minore di  *55,* 6 o  se il controllo ConsDef  è  uguale a FALSE  *37,* o  se la variabile SubClass_C2_variabile_V3 è  diverso da  *56,* 4 *36,* o  se il timer SubClass_C2_timer_T8 non è disattivo, *72,*Azzera il contatore SubClass_C2_contatore_Co1
    //   ,altrimenti  *67,* Assegna alla variabile SubClass_C2_variabile_V3 il valore 6
    bool res_OrLogicOP_16 = false;
    bool res_OrLogicOP_17 = false;
    bool res_OrLogicOP_18 = false;
    bool res_OrLogicOP_19 = false;
    bool res_ForAllPredicateNotEmpty_20 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl8Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl8(my_id,i);
    bool res_ImpliesLogicOp_21 = true;
    res_ImpliesLogicOp_21 = (res_ImpliesLogicOp_21 && Timer_Attivo(L_P1__GetMainc41(it.mainc47)));
    res_ForAllPredicateNotEmpty_20 = res_ImpliesLogicOp_21;
    if(!res_ForAllPredicateNotEmpty_20) {break;}
    }
    res_OrLogicOP_19 = (res_OrLogicOP_19 || res_ForAllPredicateNotEmpty_20);
    bool res_AndLogicOP_22 = true;
    res_AndLogicOP_22 = (res_AndLogicOP_22 && (L_P1__GetInConsd1(my_id) == false));
    res_AndLogicOP_22 = (res_AndLogicOP_22 && (L_P1__GetParamSubcl12(my_id) < 6u));
    
    res_OrLogicOP_19 = (res_OrLogicOP_19 || res_AndLogicOP_22);
    
    res_OrLogicOP_18 = (res_OrLogicOP_18 || res_OrLogicOP_19);
    res_OrLogicOP_18 = (res_OrLogicOP_18 || (L_P1__GetInConsd1(my_id) == false));
    
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_OrLogicOP_18);
    bool res_NotLogicOP_23 = true;
    res_NotLogicOP_23 = (res_NotLogicOP_23 && ! (L_P1__GetSubcl28(my_id) == 4u));
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_NotLogicOP_23);
    
    res_OrLogicOP_16 = (res_OrLogicOP_16 || res_OrLogicOP_17);
    bool res_NotLogicOP_24 = true;
    res_NotLogicOP_24 = (res_NotLogicOP_24 && ! Timer_Disattivo(L_P1__GetSubcl39(my_id)));
    res_OrLogicOP_16 = (res_OrLogicOP_16 || res_NotLogicOP_24);
    
    if(res_OrLogicOP_16){
    
    Counter_Res(L_P1__GetSubcl41(my_id));
    }else{
    
    L_P1__SetSubcl28(my_id,6u);
    }
    
    //  *35,*  se il controllo SubClass_C2_controllo_C8 è  uguale a  True  *38,* e  se il contatore SubClass_C2_contatore_Co1 è  diverso da  *56,* 15 *36,* o  se il timer SubClass_C2_timer_T1 non è disattivo *34,* o  se il parametro SubClass_C2_parametro_P5 non è  diverso da avanzamentox *37,* o  se la variabile SubClass_C2_variabile_V3 è  minore di  *55,* 10 *38,* o  se il contatore SubClass_C2_contatore_Co1 non è  minore di  *55,* 144, *71,*Decrementa il contatore SubClass_C2_contatore_Co1
    bool res_OrLogicOP_25 = false;
    bool res_OrLogicOP_26 = false;
    bool res_OrLogicOP_27 = false;
    bool res_OrLogicOP_28 = false;
    bool res_AndLogicOP_29 = true;
    res_AndLogicOP_29 = (res_AndLogicOP_29 && (L_P1__GetInSubcl6(my_id) == true));
    bool res_NotLogicOP_30 = true;
    res_NotLogicOP_30 = (res_NotLogicOP_30 && ! (Counter_GetValore(L_P1__GetSubcl41(my_id)) == 15u));
    res_AndLogicOP_29 = (res_AndLogicOP_29 && res_NotLogicOP_30);
    
    res_OrLogicOP_28 = (res_OrLogicOP_28 || res_AndLogicOP_29);
    bool res_NotLogicOP_31 = true;
    res_NotLogicOP_31 = (res_NotLogicOP_31 && ! Timer_Disattivo(L_P1__GetSubcl38(my_id)));
    res_OrLogicOP_28 = (res_OrLogicOP_28 || res_NotLogicOP_31);
    
    res_OrLogicOP_27 = (res_OrLogicOP_27 || res_OrLogicOP_28);
    bool res_NotLogicOP_32 = true;
    bool res_NotLogicOP_33 = true;
    res_NotLogicOP_33 = (res_NotLogicOP_33 && ! (L_P1__GetParamSubcl10(my_id) == avanzamento1));
    res_NotLogicOP_32 = (res_NotLogicOP_32 && ! res_NotLogicOP_33);
    res_OrLogicOP_27 = (res_OrLogicOP_27 || res_NotLogicOP_32);
    
    res_OrLogicOP_26 = (res_OrLogicOP_26 || res_OrLogicOP_27);
    res_OrLogicOP_26 = (res_OrLogicOP_26 || (L_P1__GetSubcl28(my_id) < 10u));
    
    res_OrLogicOP_25 = (res_OrLogicOP_25 || res_OrLogicOP_26);
    bool res_NotLogicOP_34 = true;
    res_NotLogicOP_34 = (res_NotLogicOP_34 && ! (Counter_GetValore(L_P1__GetSubcl41(my_id)) < 144u));
    res_OrLogicOP_25 = (res_OrLogicOP_25 || res_NotLogicOP_34);
    
    if(res_OrLogicOP_25){
    
    Counter_Decr(L_P1__GetSubcl41(my_id));
    }
}



// ********** Definizione metodi **********

// Metodi standard

void L_P1_C2_Init(instance_id_t const my_id)
{
    // init variabili di stato
    L_P1__SetStato3(my_id, C2_St_Stato);
    L_P1__SetSubcl15(my_id, avanzamento);
    L_P1__SetSubcl17(my_id, false);
    L_P1__SetSubcl19(my_id, false);
    L_P1__SetSubcl21(my_id, 0);
    L_P1__SetSubcl23(my_id, 0);
    L_P1__SetSubcl25(my_id, false);
    L_P1__SetSubcl26(my_id, false);
    L_P1__SetSubcl27(my_id, false);
    L_P1__SetSubcl28(my_id, 0);
    L_P1__SetSubcl29(my_id, c75giallo);
    // init controlli precedenti
    L_P1__SetSubcl14(my_id, false);
    // init Timer e Counter
    Timer_AggmInit(L_P1__GetSubcl30(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl30_ID);
    Timer_Init(L_P1__GetSubcl30(my_id), 530000);
    Timer_AggmInit(L_P1__GetSubcl31(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl31_ID);
    Timer_Init(L_P1__GetSubcl31(my_id), 530000);
    Timer_AggmInit(L_P1__GetSubcl32(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl32_ID);
    Timer_Init(L_P1__GetSubcl32(my_id), 34000);
    Timer_AggmInit(L_P1__GetSubcl33(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl33_ID);
    Timer_Init(L_P1__GetSubcl33(my_id), 34000);
    Timer_AggmInit(L_P1__GetSubcl34(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl34_ID);
    Timer_Init(L_P1__GetSubcl34(my_id), 35000);
    Timer_AggmInit(L_P1__GetSubcl35(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl35_ID);
    Timer_Init(L_P1__GetSubcl35(my_id), 35000);
    Timer_AggmInit(L_P1__GetSubcl36(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl36_ID);
    Timer_Init(L_P1__GetSubcl36(my_id), 11230000);
    Timer_AggmInit(L_P1__GetSubcl37(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl37_ID);
    Timer_Init(L_P1__GetSubcl37(my_id), 11230000);
    Timer_AggmInit(L_P1__GetSubcl38(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl38_ID);
    Timer_Init(L_P1__GetSubcl38(my_id), 24000);
    Timer_AggmInit(L_P1__GetSubcl39(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl39_ID);
    Timer_Init(L_P1__GetSubcl39(my_id), 5512000);
    Timer_AggmInit(L_P1__GetSubcl40(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl40_ID);
    Timer_Init(L_P1__GetSubcl40(my_id), 1000);
    Counter_AggmInit(L_P1__GetSubcl41(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl41_ID);
    Counter_Init(L_P1__GetSubcl41(my_id));
    Counter_AggmInit(L_P1__GetSubcl42(my_id), true, CLASS_L_P1_C2_ID, my_id, L_P1__subcl42_ID);
    Counter_Init(L_P1__GetSubcl42(my_id));
    // init response
    L_P1_C2_SetResponse(my_id, LDS_SCHED_NOP);

    // transizione iniziale
    if(L_P1__Guard2(my_id)) {
        L_P1_C2_SetState(my_id, C2_St_state);
	L_P1__Effec2(my_id);
    } else {
        STOP_EXECUTION(LOGIC_ERROR);
    }
    // init variabili precedenti
    L_P1__SetSubcl16(my_id, L_P1__GetSubcl15(my_id));
    L_P1__SetSubcl18(my_id, L_P1__GetSubcl17(my_id));
    L_P1__SetSubcl20(my_id, L_P1__GetSubcl19(my_id));
    L_P1__SetSubcl22(my_id, L_P1__GetSubcl21(my_id));
    L_P1__SetSubcl24(my_id, L_P1__GetSubcl23(my_id));
}

void L_P1_C2_Exec(instance_id_t const my_id, Phase const p)
{
    L_P1_C2_SetResponse(my_id, LDS_SCHED_NOP);
    switch (p) {

    case LDS_PHASE_MANUAL:
        break;
 

    case LDS_PHASE_STATE:

        switch (L_P1_C2_GetState(my_id)) {

        case C2_St_state1:
            if (L_P1__Guard10(my_id)) {
                L_P1_C2_SetState(my_id, C2_St_state1);
                L_P1__Effec10(my_id);				
            }
            else
                {STOP_EXECUTION(LOGIC_ERROR); } // fine transizioni da state1 nella fase LDS_PHASE_STATE
            break;

        case C2_St_state:
            if (L_P1__Guard9(my_id)) {
                L_P1_C2_SetState(my_id, C2_St_state2);
                L_P1__Effec9(my_id);				
            }
            else if (L_P1__Guard4(my_id)) {
                L_P1_C2_SetState(my_id, C2_St_state2);
                L_P1__Effec4(my_id);				
            }
            else if (L_P1__Guard5(my_id)) {
                L_P1_C2_SetState(my_id, C2_St_state1);
                L_P1__Effec5(my_id);				
            }
            else if (L_P1__Guard6(my_id)) {
                L_P1_C2_SetState(my_id, C2_St_state1);
                L_P1__Effec6(my_id);				
            }
            else if (L_P1__Guard7(my_id)) {
                L_P1_C2_SetState(my_id, C2_St_state2);
                L_P1__Effec7(my_id);				
            }
            else if (L_P1__Guard8(my_id)) {
                L_P1_C2_SetState(my_id, C2_St_state2);
                L_P1__Effec8(my_id);				
            }
            else if (L_P1__Guard3(my_id)) {
                L_P1_C2_SetState(my_id, C2_St_state);
                L_P1__Effec3(my_id);				
            }
            else
                {STOP_EXECUTION(LOGIC_ERROR); } // fine transizioni da state nella fase LDS_PHASE_STATE
            break;

        case C2_St_state3:
            if (L_P1__Guard18(my_id)) {
                L_P1_C2_SetState(my_id, C2_St_state3);
                L_P1__Effec18(my_id);				
            }
            else
                {STOP_EXECUTION(LOGIC_ERROR); } // fine transizioni da state3 nella fase LDS_PHASE_STATE
            break;

        case C2_St_state2:
            if (L_P1__Guard17(my_id)) {
                L_P1_C2_SetState(my_id, C2_St_state3);
                L_P1__Effec17(my_id);				
            }
            else if (L_P1__Guard12(my_id)) {
                L_P1_C2_SetState(my_id, C2_St_state1);
                L_P1__Effec12(my_id);				
            }
            else if (L_P1__Guard13(my_id)) {
                L_P1_C2_SetState(my_id, C2_St_state);
                L_P1__Effec13(my_id);				
            }
            else if (L_P1__Guard14(my_id)) {
                L_P1_C2_SetState(my_id, C2_St_state1);
                L_P1__Effec14(my_id);				
            }
            else if (L_P1__Guard15(my_id)) {
                L_P1_C2_SetState(my_id, C2_St_state1);
                L_P1__Effec15(my_id);				
            }
            else if (L_P1__Guard16(my_id)) {
                L_P1_C2_SetState(my_id, C2_St_state2);
                L_P1__Effec16(my_id);				
            }
            else if (L_P1__Guard11(my_id)) {
                L_P1_C2_SetState(my_id, C2_St_state2);
                L_P1__Effec11(my_id);				
            }
            else
                {STOP_EXECUTION(LOGIC_ERROR); } // fine transizioni da state2 nella fase LDS_PHASE_STATE
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

ExecResponse L_P1_C2_GExec(global_id_t const proc_id, Phase const p)
{
    CHECK_LT(GLOBAL_TO_L_P1_C2(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C2(proc_id);
    L_P1_C2_Exec(my_id, p);
    return L_P1_C2_GetResponse(my_id);
}

void L_P1_C2_GTick(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C2(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C2(proc_id);
    Timer_Exec(L_P1__GetSubcl30(my_id));
    Timer_Exec(L_P1__GetSubcl31(my_id));
    Timer_Exec(L_P1__GetSubcl32(my_id));
    Timer_Exec(L_P1__GetSubcl33(my_id));
    Timer_Exec(L_P1__GetSubcl34(my_id));
    Timer_Exec(L_P1__GetSubcl35(my_id));
    Timer_Exec(L_P1__GetSubcl36(my_id));
    Timer_Exec(L_P1__GetSubcl37(my_id));
    Timer_Exec(L_P1__GetSubcl38(my_id));
    Timer_Exec(L_P1__GetSubcl39(my_id));
    Timer_Exec(L_P1__GetSubcl40(my_id));
}

void L_P1_C2_GSetSafe(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C2(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C2(proc_id);
    L_P1__SetOutSubcl(my_id, avanzamento1);
    L_P1__SetOutSubcl1(my_id, avanzamento1);
}

void L_P1_C2_GUpdatePrev(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C2(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C2(proc_id);
    L_P1__SetSubcl14(my_id, L_P1__GetInSubcl13(my_id));
    L_P1__SetSubcl16(my_id, L_P1__GetSubcl15(my_id));
    L_P1__SetSubcl18(my_id, L_P1__GetSubcl17(my_id));
    L_P1__SetSubcl20(my_id, L_P1__GetSubcl19(my_id));
    L_P1__SetSubcl22(my_id, L_P1__GetSubcl21(my_id));
    L_P1__SetSubcl24(my_id, L_P1__GetSubcl23(my_id));
}

// ********** Definizione macro **********

// Macro di effetto

/*
    CNL corrispondente:
    
    { commento: {42,}  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  commento: {105,} è  uguale a RossoGialloaVerdea, commento: {66,} Assegna al comando SubClass_C2_comando_C3 il valore avanzamentox
    
       
     commento: {43,}  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L2 è attivo commento: {37,} e  se la variabile SubClass_C2_variabile_V3 è  minore di  commento: {55,} 1 commento: {37,} o  se la variabile SubClass_C2_variabile_V3 non è  uguale a  commento: {53,} 9 commento: {36,} e  se il timer SubClass_C2_timer_T8 è disattivo, commento: {71,}Decrementa il contatore SubClass_C2_contatore_Co7
    
     ,altrimenti   commento: {67,} Assegna alla variabile SubClass_C2_variabile_V6 il valore GialloxVerdex commento: {67,}
    
    
     commento: {109,}  se il ripristino della variabile  SubClass_C2_restoreva_RV1 non è  uguale a  False  o  se l'argomento argomento_af5 non  è  diverso da GialloaVerdea commento: {39,}  commento: {37,} e  se la variabile SubClass_C2_variabile_V3 è  minore di  commento: {55,} 2 commento: {35,} e  se il controllo SubClass_C2_controllo_C10 non è  diverso da  True  commento: {34,} e  se il parametro SubClass_C2_parametro_P6 è  diverso da  True  commento: {37,} o  se la variabile SubClass_C2_variabile_V2 non è  uguale a  False , commento: {72,}Azzera il contatore SubClass_C2_contatore_Co7
    
     ,altrimenti  commento: {71,}Decrementa il contatore SubClass_C2_contatore_Co7
    
    
     commento: {43,}  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C2_lista_L4 è disattivo commento: {36,} e  se il timer SubClass_C2_timer_T1 è attivo commento: {36,} o  se il timer SubClass_C2_timer_T8 è attivo commento: {35,} e  se il controllo SubClass_C2_controllo_C5 non è  diverso da avanzamentox commento: {36,} o  se il timer SubClass_C2_timer_T9 è attivo commento: {36,} e  se il timer SubClass_C2_timer_T1 non è scaduto,  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V2 il valore  True  commento: {67,}
    
       
    
    }
*/
void L_P1__Macro11(instance_id_t const my_id , C2_Enumerat2 argom19, bool argom20, C2_Enumerat1 argom21, C2_Enumerat1 argom22)
{
//  *42,*  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  *105,* è  uguale a RossoGialloaVerdea, *66,* Assegna al comando SubClass_C2_comando_C3 il valore avanzamentox
    bool res_ForAllPredicateNotEmpty_0 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl8Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl8(my_id,i);
    bool res_ImpliesLogicOp_1 = true;
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && (L_P1__GetInMainc5(it.mainc47) == rossogiallo));
    res_ForAllPredicateNotEmpty_0 = res_ImpliesLogicOp_1;
    if(!res_ForAllPredicateNotEmpty_0) {break;}
    }
    if(res_ForAllPredicateNotEmpty_0){
    
    L_P1__SetOutSubcl(my_id,avanzamento1);
    }
    //  *43,*  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L2 è attivo *37,* e  se la variabile SubClass_C2_variabile_V3 è  minore di  *55,* 1 *37,* o  se la variabile SubClass_C2_variabile_V3 non è  uguale a  *53,* 9 *36,* e  se il timer SubClass_C2_timer_T8 è disattivo, *71,*Decrementa il contatore SubClass_C2_contatore_Co7
    // ,altrimenti   *67,* Assegna alla variabile SubClass_C2_variabile_V6 il valore GialloxVerdex
    bool res_OrLogicOP_2 = false;
    bool res_AndLogicOP_3 = true;
    bool res_ForAllPredicate_4 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl7Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl7(my_id,i);
    bool res_ImpliesLogicOp_5 = true;
    res_ImpliesLogicOp_5 = (res_ImpliesLogicOp_5 && Timer_Attivo(L_P1__GetMainc40(it.mainc47)));
    res_ForAllPredicate_4 = res_ImpliesLogicOp_5;
    if(!res_ForAllPredicate_4) {break;}
    }
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_ForAllPredicate_4);
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (L_P1__GetSubcl28(my_id) < 1u));
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_3);
    bool res_AndLogicOP_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetSubcl28(my_id) == 9u));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_7);
    res_AndLogicOP_6 = (res_AndLogicOP_6 && Timer_Disattivo(L_P1__GetSubcl39(my_id)));
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_6);
    
    if(res_OrLogicOP_2){
    
    Counter_Decr(L_P1__GetSubcl42(my_id));
    }else{
    
    L_P1__SetSubcl29(my_id,gialloxverd);
    }
    //  *67,*
    // *109,*  se il ripristino della variabile  SubClass_C2_restoreva_RV1 non è  uguale a  False  o  se l'argomento argomento_af5 non  è  diverso da GialloaVerdea *39,*  *37,* e  se la variabile SubClass_C2_variabile_V3 è  minore di  *55,* 2 *35,* e  se il controllo SubClass_C2_controllo_C10 non è  diverso da  True  *34,* e  se il parametro SubClass_C2_parametro_P6 è  diverso da  True  *37,* o  se la variabile SubClass_C2_variabile_V2 non è  uguale a  False , *72,*Azzera il contatore SubClass_C2_contatore_Co7
    // ,altrimenti  *71,*Decrementa il contatore SubClass_C2_contatore_Co7
    bool res_OrLogicOP_8 = false;
    bool res_OrLogicOP_9 = false;
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__GetSubcl26(my_id) == false));
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_NotLogicOP_10);
    bool res_AndLogicOP_11 = true;
    bool res_AndLogicOP_12 = true;
    bool res_AndLogicOP_13 = true;
    bool res_NotLogicOP_14 = true;
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (argom21 == gialloaverd));
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! res_NotLogicOP_15);
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_NotLogicOP_14);
    res_AndLogicOP_13 = (res_AndLogicOP_13 && (L_P1__GetSubcl28(my_id) < 2u));
    
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_AndLogicOP_13);
    bool res_NotLogicOP_16 = true;
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! (L_P1__GetInSubcl3(my_id) == true));
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! res_NotLogicOP_17);
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_NotLogicOP_16);
    
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_AndLogicOP_12);
    bool res_NotLogicOP_18 = true;
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! (L_P1__GetParamSubcl11(my_id) == true));
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_NotLogicOP_18);
    
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_AndLogicOP_11);
    
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_OrLogicOP_9);
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (L_P1__GetSubcl27(my_id) == false));
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_NotLogicOP_19);
    
    if(res_OrLogicOP_8){
    
    Counter_Res(L_P1__GetSubcl42(my_id));
    }else{
    
    Counter_Decr(L_P1__GetSubcl42(my_id));
    }
    //  *43,*  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C2_lista_L4 è disattivo *36,* e  se il timer SubClass_C2_timer_T1 è attivo *36,* o  se il timer SubClass_C2_timer_T8 è attivo *35,* e  se il controllo SubClass_C2_controllo_C5 non è  diverso da avanzamentox *36,* o  se il timer SubClass_C2_timer_T9 è attivo *36,* e  se il timer SubClass_C2_timer_T1 non è scaduto,  *67,* Assegna alla variabile SubClass_C2_variabile_V2 il valore  True
    bool res_OrLogicOP_20 = false;
    bool res_OrLogicOP_21 = false;
    bool res_AndLogicOP_22 = true;
    bool res_ForAllPredicate_23 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl8Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl8(my_id,i);
    bool res_ImpliesLogicOp_24 = true;
    res_ImpliesLogicOp_24 = (res_ImpliesLogicOp_24 && Timer_Disattivo(L_P1__GetMainc42(it.mainc47)));
    res_ForAllPredicate_23 = res_ImpliesLogicOp_24;
    if(!res_ForAllPredicate_23) {break;}
    }
    res_AndLogicOP_22 = (res_AndLogicOP_22 && res_ForAllPredicate_23);
    res_AndLogicOP_22 = (res_AndLogicOP_22 && Timer_Attivo(L_P1__GetSubcl38(my_id)));
    
    res_OrLogicOP_21 = (res_OrLogicOP_21 || res_AndLogicOP_22);
    bool res_AndLogicOP_25 = true;
    res_AndLogicOP_25 = (res_AndLogicOP_25 && Timer_Attivo(L_P1__GetSubcl39(my_id)));
    bool res_NotLogicOP_26 = true;
    bool res_NotLogicOP_27 = true;
    res_NotLogicOP_27 = (res_NotLogicOP_27 && ! (L_P1__GetInSubcl5(my_id) == avanzamento1));
    res_NotLogicOP_26 = (res_NotLogicOP_26 && ! res_NotLogicOP_27);
    res_AndLogicOP_25 = (res_AndLogicOP_25 && res_NotLogicOP_26);
    
    res_OrLogicOP_21 = (res_OrLogicOP_21 || res_AndLogicOP_25);
    
    res_OrLogicOP_20 = (res_OrLogicOP_20 || res_OrLogicOP_21);
    bool res_AndLogicOP_28 = true;
    res_AndLogicOP_28 = (res_AndLogicOP_28 && Timer_Attivo(L_P1__GetSubcl40(my_id)));
    bool res_NotLogicOP_29 = true;
    res_NotLogicOP_29 = (res_NotLogicOP_29 && ! Timer_Scaduto(L_P1__GetSubcl38(my_id)));
    res_AndLogicOP_28 = (res_AndLogicOP_28 && res_NotLogicOP_29);
    
    res_OrLogicOP_20 = (res_OrLogicOP_20 || res_AndLogicOP_28);
    
    if(res_OrLogicOP_20){
    
    L_P1__SetSubcl27(my_id,true);
    }
}

/*
    CNL corrispondente:
    
    { commento: {34,}  se il parametro SubClass_C2_parametro_P8 è  diverso da  commento: {56,} 4 commento: {35,} o  se il controllo SubClass_C2_controllo_C5 è  uguale a avanzamentox commento: {38,} o  se il contatore SubClass_C2_contatore_Co7 non è  uguale a  commento: {53,} 14,  Applica gli effetti
           della macro SubClass_C2_macroef_M3( con argomento_af1   uguale a c270 ,argomento_af8   uguale a avanzamento ,argomento_af10   uguale a True ,argomento_af5   uguale a GialloaVerdea ) commento: {73,}
    
       
     commento: {34,}  se lo stato  non è  uguale a  commento: {53,}  state1  commento: {106,} commento: {38,} o  se il contatore SubClass_C2_contatore_Co1 è  minore di  commento: {55,} 13304, commento: {69,}Disattiva il timer SubClass_C2_timer_T1
    
       
     commento: {35,}  se il controllo SubClass_C2_controllo_C8 non è  diverso da  True  commento: {35,} o  se il controllo SubClass_C2_controllo_C8 è  diverso da  True  commento: {37,} o  se la variabile SubClass_C2_variabile_V3 non è  minore di  commento: {55,} 1, commento: {68,}Attiva il timer SubClass_C2_timer_T1
    
       
    
    }
*/
void L_P1__Macro12(instance_id_t const my_id )
{
//  *34,*  se il parametro SubClass_C2_parametro_P8 è  diverso da  *56,* 4 *35,* o  se il controllo SubClass_C2_controllo_C5 è  uguale a avanzamentox *38,* o  se il contatore SubClass_C2_contatore_Co7 non è  uguale a  *53,* 14,  Applica gli effetti
    //       della macro SubClass_C2_macroef_M3( con argomento_af1   uguale a c270 ,argomento_af8   uguale a avanzamento ,argomento_af10   uguale a True ,argomento_af5   uguale a GialloaVerdea )
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (L_P1__GetParamSubcl12(my_id) == 4u));
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_NotLogicOP_2);
    res_OrLogicOP_1 = (res_OrLogicOP_1 || (L_P1__GetInSubcl5(my_id) == avanzamento1));
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (Counter_GetValore(L_P1__GetSubcl42(my_id)) == 14u));
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_3);
    
    if(res_OrLogicOP_0){
    
    L_P1__Macro11(my_id,c270,true,gialloaverd,avanzamento);
    }
    //  *73,*
    //   
    // *34,*  se lo stato  non è  uguale a  *53,*  state1  *106,* *38,* o  se il contatore SubClass_C2_contatore_Co1 è  minore di  *55,* 13304, *69,*Disattiva il timer SubClass_C2_timer_T1
    bool res_OrLogicOP_4 = false;
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1_C2_GetState(my_id) == C2_St_state));
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_NotLogicOP_5);
    res_OrLogicOP_4 = (res_OrLogicOP_4 || (Counter_GetValore(L_P1__GetSubcl41(my_id)) < 13304u));
    
    if(res_OrLogicOP_4){
    
    Timer_Disattiva(L_P1__GetSubcl38(my_id));
    }
    //  *35,*  se il controllo SubClass_C2_controllo_C8 non è  diverso da  True  *35,* o  se il controllo SubClass_C2_controllo_C8 è  diverso da  True  *37,* o  se la variabile SubClass_C2_variabile_V3 non è  minore di  *55,* 1, *68,*Attiva il timer SubClass_C2_timer_T1
    bool res_OrLogicOP_6 = false;
    bool res_OrLogicOP_7 = false;
    bool res_NotLogicOP_8 = true;
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetInSubcl6(my_id) == true));
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! res_NotLogicOP_9);
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_NotLogicOP_8);
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__GetInSubcl6(my_id) == true));
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_NotLogicOP_10);
    
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_OrLogicOP_7);
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (L_P1__GetSubcl28(my_id) < 1u));
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_NotLogicOP_11);
    
    if(res_OrLogicOP_6){
    
    Timer_Attiva(L_P1__GetSubcl38(my_id));
    }
}

/*
    CNL corrispondente:
     
    { commento: {42,}  se  MainClass_C1_controllo_C8 del campo  MainClass_C1 di SubClass_C2_lista_L2 è  diverso da  True ,  Applica gli effetti
           della macro SubClass_C2_macroef_M3( con argomento_af1   uguale a avanzamentox ,argomento_af8   uguale a GialloaVerdea ,argomento_af10   uguale a True ,argomento_af5   uguale a GialloaVerdea ) commento: {73,}
    
       
    
    }
*/
void L_P1__Macro13(instance_id_t const my_id )
{
//  *42,*  se  MainClass_C1_controllo_C8 del campo  MainClass_C1 di SubClass_C2_lista_L2 è  diverso da  True ,  Applica gli effetti
    //       della macro SubClass_C2_macroef_M3( con argomento_af1   uguale a avanzamentox ,argomento_af8   uguale a GialloaVerdea ,argomento_af10   uguale a True ,argomento_af5   uguale a GialloaVerdea )
    bool res_ForAllPredicate_0 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl7Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl7(my_id,i);
    bool res_ImpliesLogicOp_1 = true;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (L_P1__GetInMainc4(it.mainc47) == true));
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_NotLogicOP_2);
    res_ForAllPredicate_0 = res_ImpliesLogicOp_1;
    if(!res_ForAllPredicate_0) {break;}
    }
    if(res_ForAllPredicate_0){
    
    L_P1__Macro11(my_id,avanzamento1,true,gialloaverd,gialloaverd);
    }
}

/*
    CNL corrispondente:
    
    { commento: {38,}  se il contatore SubClass_C2_contatore_Co1 è  uguale a  commento: {53,} 14512 commento: {36,} e  se il timer SubClass_C2_timer_T1 non è attivo commento: {37,} e  se la variabile SubClass_C2_variabile_V2 non è  diverso da  False  commento: {38,} e  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  commento: {56,} 123,  Applica gli effetti
           della macro SubClass_C2_macroef_M3( con argomento_af1   uguale a avanzamentox ,argomento_af8   uguale a avanzamento ,argomento_af10   uguale a True ,argomento_af5   uguale a GialloaVerdea ) commento: {73,}
    
       
     commento: {109,}  se il ripristino della variabile  SubClass_C2_restoreva_RV1 è  uguale a  False  commento: {37,} o  se la variabile SubClass_C2_variabile_V3 non è  minore di  commento: {55,} 4 commento: {38,} o  se il contatore SubClass_C2_contatore_Co1 è  maggiore di  commento: {54,} 1504 o  se il controllo ConsDef  è  uguale a FALSE , commento: {69,}Disattiva il timer SubClass_C2_timer_T9
    
     ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V6 il valore GialloxVerdex
    
    
    
    }
*/
void L_P1__Macro14(instance_id_t const my_id )
{
//  *38,*  se il contatore SubClass_C2_contatore_Co1 è  uguale a  *53,* 14512 *36,* e  se il timer SubClass_C2_timer_T1 non è attivo *37,* e  se la variabile SubClass_C2_variabile_V2 non è  diverso da  False  *38,* e  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  *56,* 123,  Applica gli effetti
    //       della macro SubClass_C2_macroef_M3( con argomento_af1   uguale a avanzamentox ,argomento_af8   uguale a avanzamento ,argomento_af10   uguale a True ,argomento_af5   uguale a GialloaVerdea )
    bool res_AndLogicOP_0 = true;
    bool res_AndLogicOP_1 = true;
    bool res_AndLogicOP_2 = true;
    res_AndLogicOP_2 = (res_AndLogicOP_2 && (Counter_GetValore(L_P1__GetSubcl41(my_id)) == 14512u));
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! Timer_Attivo(L_P1__GetSubcl38(my_id)));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_3);
    
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_AndLogicOP_2);
    bool res_NotLogicOP_4 = true;
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetSubcl27(my_id) == false));
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! res_NotLogicOP_5);
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_4);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_AndLogicOP_1);
    bool res_NotLogicOP_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (Counter_GetValore(L_P1__GetSubcl42(my_id)) == 123u));
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! res_NotLogicOP_7);
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_NotLogicOP_6);
    
    if(res_AndLogicOP_0){
    
    L_P1__Macro11(my_id,avanzamento1,true,gialloaverd,avanzamento);
    }
    //  *73,*
    //   
    // *109,*  se il ripristino della variabile  SubClass_C2_restoreva_RV1 è  uguale a  False  *37,* o  se la variabile SubClass_C2_variabile_V3 non è  minore di  *55,* 4 *38,* o  se il contatore SubClass_C2_contatore_Co1 è  maggiore di  *54,* 1504 o  se il controllo ConsDef  è  uguale a FALSE , *69,*Disattiva il timer SubClass_C2_timer_T9
    // ,altrimenti  *67,* Assegna alla variabile SubClass_C2_variabile_V6 il valore GialloxVerdex
    bool res_OrLogicOP_8 = false;
    bool res_OrLogicOP_9 = false;
    bool res_OrLogicOP_10 = false;
    res_OrLogicOP_10 = (res_OrLogicOP_10 || (L_P1__GetSubcl26(my_id) == false));
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (L_P1__GetSubcl28(my_id) < 4u));
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_NotLogicOP_11);
    
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_OrLogicOP_10);
    res_OrLogicOP_9 = (res_OrLogicOP_9 || (Counter_GetValore(L_P1__GetSubcl41(my_id)) > 1504u));
    
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_OrLogicOP_9);
    res_OrLogicOP_8 = (res_OrLogicOP_8 || (L_P1__GetInConsd1(my_id) == false));
    
    if(res_OrLogicOP_8){
    
    Timer_Disattiva(L_P1__GetSubcl40(my_id));
    }else{
    
    L_P1__SetSubcl29(my_id,gialloxverd);
    }
}


// Macro di verifica

/*
    CNL corrispondente:
    
    { commento: {63,} commento: {34,}  se il parametro SubClass_C2_parametro_P8 è  maggiore di  commento: {54,} 6 commento: {38,} o  se il contatore SubClass_C2_contatore_Co1 non è  minore di  commento: {55,} 1430 o  se l'argomento argomento_ave5 è  uguale a  True  commento: {39,}  o  se l'argomento argomento_ave5 è  uguale a  True  commento: {39,}  e  se l'argomento argomento_ave5 non  è  uguale a  True  commento: {39,}  commento: {38,} o  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  commento: {56,} 1145, Solo una delle seguenti { 
     commento: {62,} commento: {41,}  se MainClass_C1_parametro_P10 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  commento: {105,} è  diverso da RossoGialloaVerdea commento: {37,} e  se la variabile SubClass_C2_variabile_V3 è  diverso da  commento: {56,} 10 commento: {34,} e  se il parametro SubClass_C2_parametro_P5 è  diverso da avanzamentox commento: {38,} o  se il contatore SubClass_C2_contatore_Co1 è  maggiore di  commento: {54,} 141 commento: {35,} e  se il controllo SubClass_C2_controllo_C5 è  uguale a avanzamentox commento: {35,} o  se il controllo SubClass_C2_controllo_C1 non è  diverso da avanzamentox, Almeno una delle seguenti { 
      se la macro  SubClass_C2_macrova_M7 ( con argomento_a9   uguale a c270 ,argomento_a6   uguale a GialloxVerdex ,argomento_a2   uguale a avanzamentox ,argomento_a7   uguale a c270 ,argomento_a3   uguale a GialloxVerdex  e argomento_a4   uguale a GialloxVerdex )   è  diverso da avanzamentox commento: {40,} ,  commento: {45,}  se  MainClass_C1_contatore_Co3 del campo  MainClass_C1 di SubClass_C2_lista_L2 esiste e  commento: {105,} è  uguale a  commento: {53,} 1223, commento: {88,} quando  commento: {111,}   lo stato del campo  MainClass_C1     è  uguale a  commento: {53,}  state1 , Verifica che   commento: {49,50,}  commento: {,}  la variabile SubClass_C2_variabile_V2 non sia  uguale a  False 
     commento: {104,} o  che  commento: {,}  il timer SubClass_C2_timer_T8 non sia disattivo
    
    
     } Verifica che   commento: {47,52,}  commento: {34,}  il parametro SubClass_C2_parametro_P6 non sia  diverso da  True 
     commento: {104,} e  che   l'argomento argomento_ave9 non  sia  diverso da RossoGialloGiallo commento: {,} 
    
    
     } Verifica che   commento: {48,49,50,51,52,}  commento: {,}  la variabile SubClass_C2_variabile_V2 non sia  diverso da  False 
     commento: {104,} o  che   l'argomento argomento_ave9 non  sia  diverso da RossoGialloGiallo commento: {,} 
     commento: {104,} o  che  commento: {,}  il timer SubClass_C2_timer_T9 sia scaduto
     commento: {104,} e  che   l'argomento argomento_ave2 non  sia  uguale a avanzamentox commento: {39,} 
     commento: {104,} e  che  commento: {,}  il controllo SubClass_C2_controllo_C10 sia  uguale a  False 
     commento: {104,} o  che  commento: {,}  il contatore SubClass_C2_contatore_Co1 non sia  uguale a  commento: {53,} 14
    
    
    }
*/
bool L_P1__Macro20(instance_id_t const my_id , C2_Enumerat2 argom48, C2_Enumerat4 argom49, bool argom50, C2_Enumerat1 argom51, bool argom52, C2_Enumerat4 argom53)
{
bool res_AndLogicOP_0 = true;
    
    //  *63,* *34,*  se il parametro SubClass_C2_parametro_P8 è  maggiore di  *54,* 6 *38,* o  se il contatore SubClass_C2_contatore_Co1 non è  minore di  *55,* 1430 o  se l'argomento argomento_ave5 è  uguale a  True  *39,*  o  se l'argomento argomento_ave5 è  uguale a  True  *39,*  e  se l'argomento argomento_ave5 non  è  uguale a  True  *39,*  *38,* o  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  *56,* 1145, Solo una delle seguenti { 
    //   *62,* *41,*  se MainClass_C1_parametro_P10 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  *105,* è  diverso da RossoGialloaVerdea *37,* e  se la variabile SubClass_C2_variabile_V3 è  diverso da  *56,* 10 *34,* e  se il parametro SubClass_C2_parametro_P5 è  diverso da avanzamentox *38,* o  se il contatore SubClass_C2_contatore_Co1 è  maggiore di  *54,* 141 *35,* e  se il controllo SubClass_C2_controllo_C5 è  uguale a avanzamentox *35,* o  se il controllo SubClass_C2_controllo_C1 non è  diverso da avanzamentox, Almeno una delle seguenti { 
    //    se la macro  SubClass_C2_macrova_M7 ( con argomento_a9   uguale a c270 ,argomento_a6   uguale a GialloxVerdex ,argomento_a2   uguale a avanzamentox ,argomento_a7   uguale a c270 ,argomento_a3   uguale a GialloxVerdex  e argomento_a4   uguale a GialloxVerdex )   è  diverso da avanzamentox *40,* ,  *45,*  se  MainClass_C1_contatore_Co3 del campo  MainClass_C1 di SubClass_C2_lista_L2 esiste e  *105,* è  uguale a  *53,* 1223, *88,* quando  *111,*   lo stato del campo  MainClass_C1     è  uguale a  *53,*  state1 , Verifica che   *49,50,*  *,*  la variabile SubClass_C2_variabile_V2 non sia  uguale a  False 
    //   *104,* o  che  *,*  il timer SubClass_C2_timer_T8 non sia disattivo
    //   } Verifica che   *47,52,*  *34,*  il parametro SubClass_C2_parametro_P6 non sia  diverso da  True 
    //   *104,* e  che   l'argomento argomento_ave9 non  sia  diverso da RossoGialloGiallo *,* 
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_OrLogicOP_4 = false;
    bool res_OrLogicOP_5 = false;
    res_OrLogicOP_5 = (res_OrLogicOP_5 || (L_P1__GetParamSubcl12(my_id) > 6u));
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (Counter_GetValore(L_P1__GetSubcl41(my_id)) < 1430u));
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_NotLogicOP_6);
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_OrLogicOP_5);
    res_OrLogicOP_4 = (res_OrLogicOP_4 || (argom50 == true));
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_OrLogicOP_4);
    bool res_AndLogicOP_7 = true;
    res_AndLogicOP_7 = (res_AndLogicOP_7 && (argom50 == true));
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (argom50 == true));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_8);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_AndLogicOP_7);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    bool res_NotLogicOP_9 = true;
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (Counter_GetValore(L_P1__GetSubcl42(my_id)) == 1145u));
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! res_NotLogicOP_10);
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_9);
    
    if(res_OrLogicOP_2){
    bool res_XorLogicOP_11 = true;
    int xorIndex_res_XorLogicOP_11 = 0;
    bool res_ImpliesLogicOp_12 = true;
    bool res_OrLogicOP_13 = false;
    bool res_OrLogicOP_14 = false;
    bool res_AndLogicOP_15 = true;
    bool res_AndLogicOP_16 = true;
    bool res_ForAllPredicateNotEmpty_17 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl9Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl9(my_id,i);
    bool res_ImpliesLogicOp_18 = true;
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (L_P1__GetParamMainc6(it.mainc47) == rossogiallo));
    res_ImpliesLogicOp_18 = (res_ImpliesLogicOp_18 && res_NotLogicOP_19);
    res_ForAllPredicateNotEmpty_17 = res_ImpliesLogicOp_18;
    if(!res_ForAllPredicateNotEmpty_17) {break;}
    }
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_ForAllPredicateNotEmpty_17);
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! (L_P1__GetSubcl28(my_id) == 10u));
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_NotLogicOP_20);
    
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_AndLogicOP_16);
    bool res_NotLogicOP_21 = true;
    res_NotLogicOP_21 = (res_NotLogicOP_21 && ! (L_P1__GetParamSubcl10(my_id) == avanzamento1));
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_NotLogicOP_21);
    
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_AndLogicOP_15);
    bool res_AndLogicOP_22 = true;
    res_AndLogicOP_22 = (res_AndLogicOP_22 && (Counter_GetValore(L_P1__GetSubcl41(my_id)) > 141u));
    res_AndLogicOP_22 = (res_AndLogicOP_22 && (L_P1__GetInSubcl5(my_id) == avanzamento1));
    
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_AndLogicOP_22);
    
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_OrLogicOP_14);
    bool res_NotLogicOP_23 = true;
    bool res_NotLogicOP_24 = true;
    res_NotLogicOP_24 = (res_NotLogicOP_24 && ! (L_P1__GetInSubcl2(my_id) == avanzamento1));
    res_NotLogicOP_23 = (res_NotLogicOP_23 && ! res_NotLogicOP_24);
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_NotLogicOP_23);
    
    if(res_OrLogicOP_13){
    bool res_ImpliesLogicOp_25 = true;
    bool res_AndLogicOP_26 = true;
    bool res_NotLogicOP_27 = true;
    res_NotLogicOP_27 = (res_NotLogicOP_27 && ! (L_P1__Macro18(my_id,avanzamento1,gialloxverd,gialloxverd,gialloxverd,c270,c270) == avanzamento1));
    res_AndLogicOP_26 = (res_AndLogicOP_26 && res_NotLogicOP_27);
    bool res_ForAllPredicateNotEmpty_28 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl7Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl7(my_id,i);
    bool res_ImpliesLogicOp_29 = true;
    if((L_P1_C1_GetState(it.mainc47) == C1_St_state)){
    res_ImpliesLogicOp_29 = (res_ImpliesLogicOp_29 && (Counter_GetValore(L_P1__GetMainc43(it.mainc47)) == 1223u));
    res_ForAllPredicateNotEmpty_28 = res_ImpliesLogicOp_29;
    if(!res_ForAllPredicateNotEmpty_28) {break;}
    }
    }
    res_AndLogicOP_26 = (res_AndLogicOP_26 && res_ForAllPredicateNotEmpty_28);
    
    if(res_AndLogicOP_26){
    bool res_OrLogicOP_30 = false;
    bool res_NotLogicOP_31 = true;
    res_NotLogicOP_31 = (res_NotLogicOP_31 && ! (L_P1__GetSubcl27(my_id) == false));
    res_OrLogicOP_30 = (res_OrLogicOP_30 || res_NotLogicOP_31);
    bool res_NotLogicOP_32 = true;
    res_NotLogicOP_32 = (res_NotLogicOP_32 && ! Timer_Disattivo(L_P1__GetSubcl39(my_id)));
    res_OrLogicOP_30 = (res_OrLogicOP_30 || res_NotLogicOP_32);
    
    res_ImpliesLogicOp_25 = (res_ImpliesLogicOp_25 && res_OrLogicOP_30);
    }
    res_ImpliesLogicOp_12 = (res_ImpliesLogicOp_12 && res_ImpliesLogicOp_25);
    }
    if(res_ImpliesLogicOp_12){
    xorIndex_res_XorLogicOP_11 = (xorIndex_res_XorLogicOP_11 + 1);
    }
    bool res_AndLogicOP_33 = true;
    bool res_NotLogicOP_34 = true;
    bool res_NotLogicOP_35 = true;
    res_NotLogicOP_35 = (res_NotLogicOP_35 && ! (L_P1__GetParamSubcl11(my_id) == true));
    res_NotLogicOP_34 = (res_NotLogicOP_34 && ! res_NotLogicOP_35);
    res_AndLogicOP_33 = (res_AndLogicOP_33 && res_NotLogicOP_34);
    bool res_NotLogicOP_36 = true;
    bool res_NotLogicOP_37 = true;
    res_NotLogicOP_37 = (res_NotLogicOP_37 && ! (argom53 == rossogiallo2));
    res_NotLogicOP_36 = (res_NotLogicOP_36 && ! res_NotLogicOP_37);
    res_AndLogicOP_33 = (res_AndLogicOP_33 && res_NotLogicOP_36);
    
    if(res_AndLogicOP_33){
    xorIndex_res_XorLogicOP_11 = (xorIndex_res_XorLogicOP_11 + 1);
    }
    
    res_XorLogicOP_11 = (res_XorLogicOP_11 && (xorIndex_res_XorLogicOP_11 == 1));
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_XorLogicOP_11);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *48,49,50,51,52,*  *,*  la variabile SubClass_C2_variabile_V2 non sia  diverso da  False 
    //   *104,* o  che   l'argomento argomento_ave9 non  sia  diverso da RossoGialloGiallo *,* 
    //   *104,* o  che  *,*  il timer SubClass_C2_timer_T9 sia scaduto
    //   *104,* e  che   l'argomento argomento_ave2 non  sia  uguale a avanzamentox *39,* 
    //   *104,* e  che  *,*  il controllo SubClass_C2_controllo_C10 sia  uguale a  False 
    //   *104,* o  che  *,*  il contatore SubClass_C2_contatore_Co1 non sia  uguale a  *53,* 14
    bool res_OrLogicOP_38 = false;
    bool res_OrLogicOP_39 = false;
    bool res_OrLogicOP_40 = false;
    bool res_NotLogicOP_41 = true;
    bool res_NotLogicOP_42 = true;
    res_NotLogicOP_42 = (res_NotLogicOP_42 && ! (L_P1__GetSubcl27(my_id) == false));
    res_NotLogicOP_41 = (res_NotLogicOP_41 && ! res_NotLogicOP_42);
    res_OrLogicOP_40 = (res_OrLogicOP_40 || res_NotLogicOP_41);
    bool res_NotLogicOP_43 = true;
    bool res_NotLogicOP_44 = true;
    res_NotLogicOP_44 = (res_NotLogicOP_44 && ! (argom53 == rossogiallo2));
    res_NotLogicOP_43 = (res_NotLogicOP_43 && ! res_NotLogicOP_44);
    res_OrLogicOP_40 = (res_OrLogicOP_40 || res_NotLogicOP_43);
    
    res_OrLogicOP_39 = (res_OrLogicOP_39 || res_OrLogicOP_40);
    bool res_AndLogicOP_45 = true;
    bool res_AndLogicOP_46 = true;
    res_AndLogicOP_46 = (res_AndLogicOP_46 && Timer_Scaduto(L_P1__GetSubcl40(my_id)));
    bool res_NotLogicOP_47 = true;
    res_NotLogicOP_47 = (res_NotLogicOP_47 && ! (argom48 == avanzamento1));
    res_AndLogicOP_46 = (res_AndLogicOP_46 && res_NotLogicOP_47);
    
    res_AndLogicOP_45 = (res_AndLogicOP_45 && res_AndLogicOP_46);
    res_AndLogicOP_45 = (res_AndLogicOP_45 && (L_P1__GetInSubcl3(my_id) == false));
    
    res_OrLogicOP_39 = (res_OrLogicOP_39 || res_AndLogicOP_45);
    
    res_OrLogicOP_38 = (res_OrLogicOP_38 || res_OrLogicOP_39);
    bool res_NotLogicOP_48 = true;
    res_NotLogicOP_48 = (res_NotLogicOP_48 && ! (Counter_GetValore(L_P1__GetSubcl41(my_id)) == 14u));
    res_OrLogicOP_38 = (res_OrLogicOP_38 || res_NotLogicOP_48);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_38);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
     
    { commento: {36,}  se il timer SubClass_C2_timer_T9 non è disattivo commento: {34,} o  se il parametro SubClass_C2_parametro_P6 è  diverso da  False , Verifica che   commento: {48,}  commento: {,}  il controllo SubClass_C2_controllo_C1 non sia  diverso da avanzamentox
     commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
    
    
    }
*/
bool L_P1__Macro21(instance_id_t const my_id )
{
bool res_AndLogicOP_0 = true;
    
    //  *36,*  se il timer SubClass_C2_timer_T9 non è disattivo *34,* o  se il parametro SubClass_C2_parametro_P6 è  diverso da  False , Verifica che   *48,*  *,*  il controllo SubClass_C2_controllo_C1 non sia  diverso da avanzamentox
    //   *104,* e  che   il controllo ConsDef  sia  uguale a FALSE
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! Timer_Disattivo(L_P1__GetSubcl40(my_id)));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_3);
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetParamSubcl11(my_id) == false));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_4);
    
    if(res_OrLogicOP_2){
    bool res_AndLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetInSubcl2(my_id) == avanzamento1));
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! res_NotLogicOP_7);
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_6);
    res_AndLogicOP_5 = (res_AndLogicOP_5 && (L_P1__GetInConsd1(my_id) == false));
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_AndLogicOP_5);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    
    
    return res_AndLogicOP_0;
}


// Macro valorizzate

/*
    CNL corrispondente:
    
    { commento: {[}
     commento: {46,} assegna alla macro il valore GialloxVerdex commento: {],}
    }
*/
C2_Enumerat3 L_P1__Macro15(instance_id_t const my_id , C2_Enumerat3 argom23, C2_Enumerat3 argom24, C2_Enumerat3 argom25)
{
return gialloxverd;
}

/*
    CNL corrispondente:
    
    { commento: {[} commento: {34,}  se il parametro SubClass_C2_parametro_P6 è  uguale a  False ,  commento: {41,}  se MainClass_C1_parametro_P10 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  commento: {105,} è  diverso da RossoGialloaVerdea, commento: {88,} quando  commento: {111,}   lo stato del campo  MainClass_C1     commento: {105,} è  uguale a  commento: {53,}  state1  commento: {37,} o  se la variabile SubClass_C2_variabile_V3 è  minore di  commento: {55,} 8,  commento: {45,}  se  MainClass_C1_contatore_Co8 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  commento: {105,} è  uguale a  commento: {53,} 152, commento: {88,} quando  commento: {111,}   lo stato del campo  MainClass_C1     è  uguale a  commento: {53,}  state1  commento: {42,} e  se  MainClass_C1_controllo_C5 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  commento: {105,} è  diverso da RossoGialloVerde commento: {44,} o  se  MainClass_C1_variabile_V10 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  commento: {105,} è  uguale a  True  commento: {110,} e  se il ripristino del timer  SubClass_C2_restoreTI_TI4 è attivo e  se l'argomento argomento_a1 è  uguale a  True  commento: {39,} ,  commento: {41,}  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C2_lista_L6 è  uguale a  True , commento: {88,} quando  commento: {43,}   MainClass_C1_timer_T3 del campo  MainClass_C1     è attivo , assegna alla macro il valore  True 
    
     commento: {46,} assegna alla macro il valore  False  commento: {],}
    }
*/
bool L_P1__Macro16(instance_id_t const my_id , bool argom26, C2_Enumerat1 argom27, C2_Enumerat2 argom28, C2_Enumerat1 argom29, C2_Enumerat2 argom30, C2_Enumerat3 argom31, C2_Enumerat4 argom32)
{
bool res_macro_val;
    
    //  *[* *34,*  se il parametro SubClass_C2_parametro_P6 è  uguale a  False ,  *41,*  se MainClass_C1_parametro_P10 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  *105,* è  diverso da RossoGialloaVerdea, *88,* quando  *111,*   lo stato del campo  MainClass_C1     *105,* è  uguale a  *53,*  state1  *37,* o  se la variabile SubClass_C2_variabile_V3 è  minore di  *55,* 8,  *45,*  se  MainClass_C1_contatore_Co8 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  *105,* è  uguale a  *53,* 152, *88,* quando  *111,*   lo stato del campo  MainClass_C1     è  uguale a  *53,*  state1  *42,* e  se  MainClass_C1_controllo_C5 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  *105,* è  diverso da RossoGialloVerde *44,* o  se  MainClass_C1_variabile_V10 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  *105,* è  uguale a  True  *110,* e  se il ripristino del timer  SubClass_C2_restoreTI_TI4 è attivo e  se l'argomento argomento_a1 è  uguale a  True  *39,* ,  *41,*  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C2_lista_L6 è  uguale a  True , *88,* quando  *43,*   MainClass_C1_timer_T3 del campo  MainClass_C1     è attivo
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_AndLogicOP_2 = true;
    res_AndLogicOP_2 = (res_AndLogicOP_2 && (L_P1__GetParamSubcl11(my_id) == false));
    bool res_ForAllPredicateNotEmpty_3 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl9Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl9(my_id,i);
    bool res_ImpliesLogicOp_4 = true;
    if((L_P1_C1_GetState(it.mainc47) == C1_St_state)){
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetParamMainc6(it.mainc47) == rossogiallo));
    res_ImpliesLogicOp_4 = (res_ImpliesLogicOp_4 && res_NotLogicOP_5);
    res_ForAllPredicateNotEmpty_3 = res_ImpliesLogicOp_4;
    if(!res_ForAllPredicateNotEmpty_3) {break;}
    }
    }
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_ForAllPredicateNotEmpty_3);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_2);
    bool res_AndLogicOP_6 = true;
    bool res_AndLogicOP_7 = true;
    res_AndLogicOP_7 = (res_AndLogicOP_7 && (L_P1__GetSubcl28(my_id) < 8u));
    bool res_ForAllPredicateNotEmpty_8 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl8Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl8(my_id,i);
    bool res_ImpliesLogicOp_9 = true;
    if((L_P1_C1_GetState(it.mainc47) == C1_St_state)){
    res_ImpliesLogicOp_9 = (res_ImpliesLogicOp_9 && (Counter_GetValore(L_P1__GetMainc45(it.mainc47)) == 152u));
    res_ForAllPredicateNotEmpty_8 = res_ImpliesLogicOp_9;
    if(!res_ForAllPredicateNotEmpty_8) {break;}
    }
    }
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_ForAllPredicateNotEmpty_8);
    
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_AndLogicOP_7);
    bool res_ForAllPredicateNotEmpty_10 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl8Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl8(my_id,i);
    bool res_ImpliesLogicOp_11 = true;
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (L_P1__GetInMainc2(it.mainc47) == rossogiallo1));
    res_ImpliesLogicOp_11 = (res_ImpliesLogicOp_11 && res_NotLogicOP_12);
    res_ForAllPredicateNotEmpty_10 = res_ImpliesLogicOp_11;
    if(!res_ForAllPredicateNotEmpty_10) {break;}
    }
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_ForAllPredicateNotEmpty_10);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_6);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_AndLogicOP_13 = true;
    bool res_AndLogicOP_14 = true;
    bool res_ForAllPredicateNotEmpty_15 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl9Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl9(my_id,i);
    bool res_ImpliesLogicOp_16 = true;
    res_ImpliesLogicOp_16 = (res_ImpliesLogicOp_16 && (L_P1__GetMainc32(it.mainc47) == true));
    res_ForAllPredicateNotEmpty_15 = res_ImpliesLogicOp_16;
    if(!res_ForAllPredicateNotEmpty_15) {break;}
    }
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_ForAllPredicateNotEmpty_15);
    res_AndLogicOP_14 = (res_AndLogicOP_14 && Timer_Attivo(L_P1__GetSubcl37(my_id)));
    
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_AndLogicOP_14);
    bool res_AndLogicOP_17 = true;
    res_AndLogicOP_17 = (res_AndLogicOP_17 && (argom26 == true));
    bool res_ForAllPredicate_18 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl9Length(my_id); ++i)
    {
    L_P1__Recor it = L_P1__GetRecSubcl9(my_id,i);
    bool res_ImpliesLogicOp_19 = true;
    if(Timer_Attivo(L_P1__GetMainc40(it.mainc47))){
    res_ImpliesLogicOp_19 = (res_ImpliesLogicOp_19 && (L_P1__GetParamMainc9(it.mainc47) == true));
    }
    res_ForAllPredicate_18 = res_ImpliesLogicOp_19;
    if(!res_ForAllPredicate_18) {break;}
    }
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_ForAllPredicate_18);
    
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_AndLogicOP_17);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_13);
    
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
    
    { commento: {[}
     commento: {46,} assegna alla macro il valore  False  commento: {],}
    }
*/
bool L_P1__Macro17(instance_id_t const my_id , C2_Enumerat4 argom33, C2_Enumerat3 argom34, C2_Enumerat1 argom35, C2_Enumerat1 argom36, C2_Enumerat1 argom37)
{
return false;
}

/*
    CNL corrispondente:
    
    { commento: {[}
     commento: {46,} assegna alla macro il valore avanzamentox commento: {],}
    }
*/
C2_Enumerat2 L_P1__Macro18(instance_id_t const my_id , C2_Enumerat2 argom38, C2_Enumerat3 argom39, C2_Enumerat3 argom40, C2_Enumerat3 argom41, C2_Enumerat2 argom42, C2_Enumerat2 argom43)
{
return avanzamento1;
}

/*
    CNL corrispondente:
    
    { commento: {[} commento: {36,}  se il timer SubClass_C2_timer_T1 non è scaduto , assegna alla macro il valore avanzamentox
    
     commento: {46,} assegna alla macro il valore avanzamentox commento: {],}
    }
*/
C2_Enumerat2 L_P1__Macro19(instance_id_t const my_id , bool argom44, C2_Enumerat1 argom45, C2_Enumerat3 argom46, C2_Enumerat4 argom47)
{
C2_Enumerat2 res_macro_val;
    
    //  il timer SubClass_C2_timer_T1 non è scaduto
    bool res_NotLogicOP_0 = true;
    res_NotLogicOP_0 = (res_NotLogicOP_0 && ! Timer_Scaduto(L_P1__GetSubcl38(my_id)));
    if(res_NotLogicOP_0){
    
    res_macro_val = avanzamento1;
    }
    else{
    res_macro_val = avanzamento1;
    }
    return res_macro_val;
}



