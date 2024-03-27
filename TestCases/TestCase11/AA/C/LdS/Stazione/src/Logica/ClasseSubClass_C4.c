// Codice del modello 'TestCase11', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#include "Logica/ClasseMainClass_C1.h"
#include "Logica/ClasseSubClass_C2.h"
#include "Logica/ClasseSubClass_C3.h"
#include "Logica/ClasseSubClass_C4.h"
#include "Logica/ClasseSubClass_C4_priv.h"
#include "config.h"
#include "scheduler.h"


// ********** Definizione guardie **********

/*
    CNL corrispondente:
    
     {
     Nessuna 
     }
*/
static inline bool L_P1__Guard6(instance_id_t const my_id)
{
    return true;
}


/*
    CNL corrispondente:
    
    {
    
     commento: {67,}  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} e  se il timer SubClass_C4_timer_T3 non è disattivo, Tutte le seguenti { 
     commento: {68,}  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} o  se il controllo SubClass_C4_controllo_C1 non è  uguale a  False  commento: {34,} e  se il parametro SubClass_C4_parametro_P9 non è  minore di  commento: {55,} 10, Almeno una delle seguenti { 
     commento: {68,} commento: {35,}  se il controllo SubClass_C4_controllo_C1 è  uguale a  False , Almeno una delle seguenti { 
     commento: {67,} commento: {37,}  se la variabile SubClass_C4_variabile_V3 non è  uguale a c180 commento: {34,} e  se il parametro SubClass_C4_parametro_P9 è  uguale a  commento: {53,} 10 o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
     commento: {68,}  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} o  se il contatore SubClass_C4_contatore_Co5 è  diverso da  commento: {56,} 1250 commento: {38,} e  se il contatore SubClass_C4_contatore_Co8 è  minore di  commento: {55,} 13213 commento: {34,} o  se il parametro SubClass_C4_parametro_P1 non è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} e  se il timer SubClass_C4_timer_T2 non è attivo, Almeno una delle seguenti { 
     commento: {68,} commento: {37,}  se la variabile SubClass_C4_variabile_V3 è  uguale a c180 commento: {34,} o  se il parametro SubClass_C4_parametro_P1 è  uguale a  False , Almeno una delle seguenti { 
     commento: {36,}  se il timer SubClass_C4_timer_T3 è scaduto commento: {34,} e  se il parametro SubClass_C4_parametro_P1 è  uguale a  True  commento: {35,} e  se il controllo SubClass_C4_controllo_C1 non è  uguale a  False  commento: {38,} e  se il contatore SubClass_C4_contatore_Co8 non è  minore di  commento: {55,} 144 commento: {35,} e  se il controllo SubClass_C4_controllo_C1 è  diverso da  False  commento: {37,} e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180, Verifica che   commento: {47,}  commento: {34,}  il parametro SubClass_C4_parametro_P1 non sia  diverso da  True 
    
    
     } Verifica che   commento: {51,}  commento: {,}  il contatore SubClass_C4_contatore_Co8 sia  minore di  commento: {55,} 125021
    
    
     } Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
    
    
     } Verifica che   commento: {51,}  commento: {,}  il contatore SubClass_C4_contatore_Co8 sia  uguale a  commento: {53,} 1534
    
    
     } Verifica che   commento: {50,}  commento: {,}  la variabile SubClass_C4_variabile_V3 sia  diverso da c180
    
    
     } Verifica che   commento: {47,}  commento: {34,}  il parametro SubClass_C4_parametro_P1 non sia  uguale a  True 
    
    
     } Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
    
    
    }
*/
static inline bool L_P1__Guard7(instance_id_t const my_id)
{
    bool res_AndLogicOP_0 = true;
    
    //  *67,*  se il controllo ConsDef  è  uguale a FALSE  *36,* e  se il timer SubClass_C4_timer_T3 non è disattivo, Tutte le seguenti { 
    //   *68,*  se il controllo ConsDef  è  uguale a FALSE  *35,* o  se il controllo SubClass_C4_controllo_C1 non è  uguale a  False  *34,* e  se il parametro SubClass_C4_parametro_P9 non è  minore di  *55,* 10, Almeno una delle seguenti { 
    //   *68,* *35,*  se il controllo SubClass_C4_controllo_C1 è  uguale a  False , Almeno una delle seguenti { 
    //   *67,* *37,*  se la variabile SubClass_C4_variabile_V3 non è  uguale a c180 *34,* e  se il parametro SubClass_C4_parametro_P9 è  uguale a  *53,* 10 o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
    //   *68,*  se il controllo ConsDef  è  uguale a FALSE  *38,* o  se il contatore SubClass_C4_contatore_Co5 è  diverso da  *56,* 1250 *38,* e  se il contatore SubClass_C4_contatore_Co8 è  minore di  *55,* 13213 *34,* o  se il parametro SubClass_C4_parametro_P1 non è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE  *36,* e  se il timer SubClass_C4_timer_T2 non è attivo, Almeno una delle seguenti { 
    //   *68,* *37,*  se la variabile SubClass_C4_variabile_V3 è  uguale a c180 *34,* o  se il parametro SubClass_C4_parametro_P1 è  uguale a  False , Almeno una delle seguenti { 
    //   *36,*  se il timer SubClass_C4_timer_T3 è scaduto *34,* e  se il parametro SubClass_C4_parametro_P1 è  uguale a  True  *35,* e  se il controllo SubClass_C4_controllo_C1 non è  uguale a  False  *38,* e  se il contatore SubClass_C4_contatore_Co8 non è  minore di  *55,* 144 *35,* e  se il controllo SubClass_C4_controllo_C1 è  diverso da  False  *37,* e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180, Verifica che   *47,*  *34,*  il parametro SubClass_C4_parametro_P1 non sia  diverso da  True 
    //   } Verifica che   *51,*  *,*  il contatore SubClass_C4_contatore_Co8 sia  minore di  *55,* 125021
    //   } Verifica che   *48,*   il controllo ConsDef  sia  uguale a FALSE 
    //   } Verifica che   *51,*  *,*  il contatore SubClass_C4_contatore_Co8 sia  uguale a  *53,* 1534
    //   } Verifica che   *50,*  *,*  la variabile SubClass_C4_variabile_V3 sia  diverso da c180
    //   } Verifica che   *47,*  *34,*  il parametro SubClass_C4_parametro_P1 non sia  uguale a  True 
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_AndLogicOP_2 = true;
    res_AndLogicOP_2 = (res_AndLogicOP_2 && (L_P1__GetInConsd3(my_id) == false));
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! Timer_Disattivo(L_P1__GetSubcl123(my_id)));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_3);
    
    if(res_AndLogicOP_2){
    bool res_AndLogicOP_4 = true;
    bool res_ImpliesLogicOp_5 = true;
    bool res_OrLogicOP_6 = false;
    res_OrLogicOP_6 = (res_OrLogicOP_6 || (L_P1__GetInConsd3(my_id) == false));
    bool res_AndLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetInSubcl91(my_id) == false));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_8);
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetParamSubcl98(my_id) < 10u));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_9);
    
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_AndLogicOP_7);
    
    if(res_OrLogicOP_6){
    bool res_OrLogicOP_10 = false;
    bool res_ImpliesLogicOp_11 = true;
    if((L_P1__GetInSubcl91(my_id) == false)){
    bool res_OrLogicOP_12 = false;
    bool res_ImpliesLogicOp_13 = true;
    bool res_OrLogicOP_14 = false;
    bool res_AndLogicOP_15 = true;
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (L_P1__GetSubcl113(my_id) == c180));
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_NotLogicOP_16);
    res_AndLogicOP_15 = (res_AndLogicOP_15 && (L_P1__GetParamSubcl98(my_id) == 10u));
    
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_AndLogicOP_15);
    res_OrLogicOP_14 = (res_OrLogicOP_14 || (L_P1__GetInConsd3(my_id) == false));
    
    if(res_OrLogicOP_14){
    bool res_AndLogicOP_17 = true;
    bool res_ImpliesLogicOp_18 = true;
    bool res_OrLogicOP_19 = false;
    bool res_OrLogicOP_20 = false;
    bool res_OrLogicOP_21 = false;
    res_OrLogicOP_21 = (res_OrLogicOP_21 || (L_P1__GetInConsd3(my_id) == false));
    bool res_AndLogicOP_22 = true;
    bool res_NotLogicOP_23 = true;
    res_NotLogicOP_23 = (res_NotLogicOP_23 && ! (Counter_GetValore(L_P1__GetSubcl125(my_id)) == 1250u));
    res_AndLogicOP_22 = (res_AndLogicOP_22 && res_NotLogicOP_23);
    res_AndLogicOP_22 = (res_AndLogicOP_22 && (Counter_GetValore(L_P1__GetSubcl126(my_id)) < 13213u));
    
    res_OrLogicOP_21 = (res_OrLogicOP_21 || res_AndLogicOP_22);
    
    res_OrLogicOP_20 = (res_OrLogicOP_20 || res_OrLogicOP_21);
    bool res_NotLogicOP_24 = true;
    res_NotLogicOP_24 = (res_NotLogicOP_24 && ! (L_P1__GetParamSubcl96(my_id) == true));
    res_OrLogicOP_20 = (res_OrLogicOP_20 || res_NotLogicOP_24);
    
    res_OrLogicOP_19 = (res_OrLogicOP_19 || res_OrLogicOP_20);
    bool res_AndLogicOP_25 = true;
    res_AndLogicOP_25 = (res_AndLogicOP_25 && (L_P1__GetInConsd3(my_id) == false));
    bool res_NotLogicOP_26 = true;
    res_NotLogicOP_26 = (res_NotLogicOP_26 && ! Timer_Attivo(L_P1__GetSubcl122(my_id)));
    res_AndLogicOP_25 = (res_AndLogicOP_25 && res_NotLogicOP_26);
    
    res_OrLogicOP_19 = (res_OrLogicOP_19 || res_AndLogicOP_25);
    
    if(res_OrLogicOP_19){
    bool res_OrLogicOP_27 = false;
    bool res_ImpliesLogicOp_28 = true;
    bool res_OrLogicOP_29 = false;
    res_OrLogicOP_29 = (res_OrLogicOP_29 || (L_P1__GetSubcl113(my_id) == c180));
    res_OrLogicOP_29 = (res_OrLogicOP_29 || (L_P1__GetParamSubcl96(my_id) == false));
    
    if(res_OrLogicOP_29){
    bool res_ImpliesLogicOp_30 = true;
    bool res_AndLogicOP_31 = true;
    bool res_AndLogicOP_32 = true;
    bool res_AndLogicOP_33 = true;
    bool res_AndLogicOP_34 = true;
    bool res_AndLogicOP_35 = true;
    res_AndLogicOP_35 = (res_AndLogicOP_35 && Timer_Scaduto(L_P1__GetSubcl123(my_id)));
    res_AndLogicOP_35 = (res_AndLogicOP_35 && (L_P1__GetParamSubcl96(my_id) == true));
    
    res_AndLogicOP_34 = (res_AndLogicOP_34 && res_AndLogicOP_35);
    bool res_NotLogicOP_36 = true;
    res_NotLogicOP_36 = (res_NotLogicOP_36 && ! (L_P1__GetInSubcl91(my_id) == false));
    res_AndLogicOP_34 = (res_AndLogicOP_34 && res_NotLogicOP_36);
    
    res_AndLogicOP_33 = (res_AndLogicOP_33 && res_AndLogicOP_34);
    bool res_NotLogicOP_37 = true;
    res_NotLogicOP_37 = (res_NotLogicOP_37 && ! (Counter_GetValore(L_P1__GetSubcl126(my_id)) < 144u));
    res_AndLogicOP_33 = (res_AndLogicOP_33 && res_NotLogicOP_37);
    
    res_AndLogicOP_32 = (res_AndLogicOP_32 && res_AndLogicOP_33);
    bool res_NotLogicOP_38 = true;
    res_NotLogicOP_38 = (res_NotLogicOP_38 && ! (L_P1__GetInSubcl91(my_id) == false));
    res_AndLogicOP_32 = (res_AndLogicOP_32 && res_NotLogicOP_38);
    
    res_AndLogicOP_31 = (res_AndLogicOP_31 && res_AndLogicOP_32);
    bool res_NotLogicOP_39 = true;
    res_NotLogicOP_39 = (res_NotLogicOP_39 && ! (L_P1__GetSubcl113(my_id) == c180));
    res_AndLogicOP_31 = (res_AndLogicOP_31 && res_NotLogicOP_39);
    
    if(res_AndLogicOP_31){
    bool res_NotLogicOP_40 = true;
    bool res_NotLogicOP_41 = true;
    res_NotLogicOP_41 = (res_NotLogicOP_41 && ! (L_P1__GetParamSubcl96(my_id) == true));
    res_NotLogicOP_40 = (res_NotLogicOP_40 && ! res_NotLogicOP_41);
    res_ImpliesLogicOp_30 = (res_ImpliesLogicOp_30 && res_NotLogicOP_40);
    }
    res_ImpliesLogicOp_28 = (res_ImpliesLogicOp_28 && res_ImpliesLogicOp_30);
    }
    res_OrLogicOP_27 = (res_OrLogicOP_27 || res_ImpliesLogicOp_28);
    res_OrLogicOP_27 = (res_OrLogicOP_27 || (Counter_GetValore(L_P1__GetSubcl126(my_id)) < 125021u));
    
    res_ImpliesLogicOp_18 = (res_ImpliesLogicOp_18 && res_OrLogicOP_27);
    }
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_ImpliesLogicOp_18);
    res_AndLogicOP_17 = (res_AndLogicOP_17 && (L_P1__GetInConsd3(my_id) == false));
    
    res_ImpliesLogicOp_13 = (res_ImpliesLogicOp_13 && res_AndLogicOP_17);
    }
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_ImpliesLogicOp_13);
    res_OrLogicOP_12 = (res_OrLogicOP_12 || (Counter_GetValore(L_P1__GetSubcl126(my_id)) == 1534u));
    
    res_ImpliesLogicOp_11 = (res_ImpliesLogicOp_11 && res_OrLogicOP_12);
    }
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_ImpliesLogicOp_11);
    bool res_NotLogicOP_42 = true;
    res_NotLogicOP_42 = (res_NotLogicOP_42 && ! (L_P1__GetSubcl113(my_id) == c180));
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_NotLogicOP_42);
    
    res_ImpliesLogicOp_5 = (res_ImpliesLogicOp_5 && res_OrLogicOP_10);
    }
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_ImpliesLogicOp_5);
    bool res_NotLogicOP_43 = true;
    res_NotLogicOP_43 = (res_NotLogicOP_43 && ! (L_P1__GetParamSubcl96(my_id) == true));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_43);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_AndLogicOP_4);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *48,*   il controllo ConsDef  sia  uguale a FALSE
    res_AndLogicOP_0 = (res_AndLogicOP_0 && (L_P1__GetInConsd3(my_id) == false));
    
    
    
    return res_AndLogicOP_0;
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
     {  commento: {37,}  se la variabile SubClass_C4_variabile_V3 è  uguale a c180 e  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro SubClass_C4_parametro_P9 è  maggiore di  commento: {54,} 8 commento: {38,} e  se il contatore SubClass_C4_contatore_Co5 non è  uguale a  commento: {53,} 15 commento: {36,} e  se il timer SubClass_C4_timer_T8 non è attivo, Verifica che   commento: {50,}  commento: {,}  la variabile SubClass_C4_variabile_V3 sia  uguale a c180
    
     }
*/
static inline bool L_P1__Guard9(instance_id_t const my_id)
{
    bool res_AndLogicOP_0 = true;
    
    //  *37,*  se la variabile SubClass_C4_variabile_V3 è  uguale a c180 e  se il controllo ConsDef  è  uguale a FALSE  *34,* e  se il parametro SubClass_C4_parametro_P9 è  maggiore di  *54,* 8 *38,* e  se il contatore SubClass_C4_contatore_Co5 non è  uguale a  *53,* 15 *36,* e  se il timer SubClass_C4_timer_T8 non è attivo, Verifica che   *50,*  *,*  la variabile SubClass_C4_variabile_V3 sia  uguale a c180
    bool res_ImpliesLogicOp_1 = true;
    bool res_AndLogicOP_2 = true;
    bool res_AndLogicOP_3 = true;
    bool res_AndLogicOP_4 = true;
    bool res_AndLogicOP_5 = true;
    res_AndLogicOP_5 = (res_AndLogicOP_5 && (L_P1__GetSubcl113(my_id) == c180));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && (L_P1__GetInConsd3(my_id) == false));
    
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_AndLogicOP_5);
    res_AndLogicOP_4 = (res_AndLogicOP_4 && (L_P1__GetParamSubcl98(my_id) > 8u));
    
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_AndLogicOP_4);
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (Counter_GetValore(L_P1__GetSubcl125(my_id)) == 15u));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_6);
    
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_AndLogicOP_3);
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! Timer_Attivo(L_P1__GetSubcl124(my_id)));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_7);
    
    if(res_AndLogicOP_2){
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && (L_P1__GetSubcl113(my_id) == c180));
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    
    
    return res_AndLogicOP_0;
}


/*
    CNL corrispondente:
     {  Nessuna  }
*/
static inline bool L_P1__Guard10(instance_id_t const my_id)
{
    return true;
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
     {  commento: {37,}  se la variabile SubClass_C4_variabile_V3 non è  diverso da c180 e  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} o  se il contatore SubClass_C4_contatore_Co8 è  maggiore di  commento: {54,} 1513 commento: {38,} o  se il contatore SubClass_C4_contatore_Co5 non è  uguale a  commento: {53,} 12 commento: {35,} e  se il controllo SubClass_C4_controllo_C8 è  diverso da GialloxVerdex, Verifica che   commento: {48,}  commento: {,}  il controllo SubClass_C4_controllo_C3 sia  diverso da GialloxVerdex
    
     }
*/
static inline bool L_P1__Guard12(instance_id_t const my_id)
{
    bool res_AndLogicOP_0 = true;
    
    //  *37,*  se la variabile SubClass_C4_variabile_V3 non è  diverso da c180 e  se il controllo ConsDef  è  uguale a FALSE  *38,* o  se il contatore SubClass_C4_contatore_Co8 è  maggiore di  *54,* 1513 *38,* o  se il contatore SubClass_C4_contatore_Co5 non è  uguale a  *53,* 12 *35,* e  se il controllo SubClass_C4_controllo_C8 è  diverso da GialloxVerdex, Verifica che   *48,*  *,*  il controllo SubClass_C4_controllo_C3 sia  diverso da GialloxVerdex
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_AndLogicOP_4 = true;
    bool res_NotLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetSubcl113(my_id) == c180));
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! res_NotLogicOP_6);
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_5);
    res_AndLogicOP_4 = (res_AndLogicOP_4 && (L_P1__GetInConsd3(my_id) == false));
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_AndLogicOP_4);
    res_OrLogicOP_3 = (res_OrLogicOP_3 || (Counter_GetValore(L_P1__GetSubcl126(my_id)) > 1513u));
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    bool res_AndLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (Counter_GetValore(L_P1__GetSubcl125(my_id)) == 12u));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_8);
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetInSubcl94(my_id) == gialloxverd));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_9);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_7);
    
    if(res_OrLogicOP_2){
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__GetInSubcl92(my_id) == gialloxverd));
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_NotLogicOP_10);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    
    
    return res_AndLogicOP_0;
}


/*
    CNL corrispondente:
    
    {
    
     commento: {67,} commento: {34,}  se il parametro SubClass_C4_parametro_P2 è  diverso da  True , Tutte le seguenti { 
     commento: {36,}  se il timer SubClass_C4_timer_T3 non è scaduto commento: {35,} o  se il controllo SubClass_C4_controllo_C1 è  diverso da  False  commento: {37,} e  se la variabile SubClass_C4_variabile_V3 è  uguale a c180 commento: {37,} e  se la variabile SubClass_C4_variabile_V3 è  uguale a c180 commento: {35,} e  se il controllo SubClass_C4_controllo_C8 non è  diverso da GialloxVerdex e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
    
    
     } Verifica che   commento: {51,}  commento: {,}  il contatore SubClass_C4_contatore_Co8 non sia  minore di  commento: {55,} 1221
    
    
    }
*/
static inline bool L_P1__Guard13(instance_id_t const my_id)
{
    bool res_AndLogicOP_0 = true;
    
    //  *67,* *34,*  se il parametro SubClass_C4_parametro_P2 è  diverso da  True , Tutte le seguenti { 
    //   *36,*  se il timer SubClass_C4_timer_T3 non è scaduto *35,* o  se il controllo SubClass_C4_controllo_C1 è  diverso da  False  *37,* e  se la variabile SubClass_C4_variabile_V3 è  uguale a c180 *37,* e  se la variabile SubClass_C4_variabile_V3 è  uguale a c180 *35,* e  se il controllo SubClass_C4_controllo_C8 non è  diverso da GialloxVerdex e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   *48,*   il controllo ConsDef  sia  uguale a FALSE 
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (L_P1__GetParamSubcl97(my_id) == true));
    if(res_NotLogicOP_2){
    bool res_ImpliesLogicOp_3 = true;
    bool res_OrLogicOP_4 = false;
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! Timer_Scaduto(L_P1__GetSubcl123(my_id)));
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_NotLogicOP_5);
    bool res_AndLogicOP_6 = true;
    bool res_AndLogicOP_7 = true;
    bool res_AndLogicOP_8 = true;
    bool res_AndLogicOP_9 = true;
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__GetInSubcl91(my_id) == false));
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_NotLogicOP_10);
    res_AndLogicOP_9 = (res_AndLogicOP_9 && (L_P1__GetSubcl113(my_id) == c180));
    
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_AndLogicOP_9);
    res_AndLogicOP_8 = (res_AndLogicOP_8 && (L_P1__GetSubcl113(my_id) == c180));
    
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_AndLogicOP_8);
    bool res_NotLogicOP_11 = true;
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (L_P1__GetInSubcl94(my_id) == gialloxverd));
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! res_NotLogicOP_12);
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_11);
    
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_AndLogicOP_7);
    res_AndLogicOP_6 = (res_AndLogicOP_6 && (L_P1__GetInConsd3(my_id) == false));
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_AndLogicOP_6);
    
    if(res_OrLogicOP_4){
    res_ImpliesLogicOp_3 = (res_ImpliesLogicOp_3 && (L_P1__GetInConsd3(my_id) == false));
    }
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_ImpliesLogicOp_3);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *51,*  *,*  il contatore SubClass_C4_contatore_Co8 non sia  minore di  *55,* 1221
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (Counter_GetValore(L_P1__GetSubcl126(my_id)) < 1221u));
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_NotLogicOP_13);
    
    
    
    return res_AndLogicOP_0;
}


// ********** Definizione effetti **********

/*
    CNL corrispondente:
    
     {
     Nessuna 
     }
*/
static inline void L_P1__Effec6(instance_id_t const my_id)
{
    
}


/*
    CNL corrispondente:
    
    {
    
    Comanda al campo MainClass_C1 di SubClass_C4_lista_L9
     di eseguire  commento: {113,}  MainClass_C1_command_comm4( con argomento_ave4   uguale a avanzamento ,argomento_ave9   uguale a c270 )
    }
*/
static inline void L_P1__Effec7(instance_id_t const my_id)
{
    
    //  Comanda al campo MainClass_C1 di SubClass_C4_lista_L9
    //   di eseguire  *113,*  MainClass_C1_command_comm4( con argomento_ave4   uguale a avanzamento ,argomento_ave9   uguale a c270 )
    for (index_t i = 0; i < L_P1__GetParamSubcl95Length(my_id); ++i)
    {
    L_P1__Recor3 it = L_P1__GetRecSubcl95(my_id,i);
    
    L_P1__SetCAEvent2(it.mainc48,true);
    L_P1__SetCAArgom(it.mainc48,avanzamento);
    L_P1__SetCAArgom1(it.mainc48,c270);
    scheduler_NotifyCommand(L_P1_C1_TO_GLOBAL(it.mainc48));
    }
}


/*
    CNL corrispondente:
     {Comanda al campo MainClass_C1 di SubClass_C4_lista_L9
     di eseguire  commento: {113,}  MainClass_C1_command_comm4( con argomento_ave4   uguale a avanzamento ,argomento_ave9   uguale a c270 ) }
*/
static inline void L_P1__Effec8(instance_id_t const my_id)
{
    
    //  Comanda al campo MainClass_C1 di SubClass_C4_lista_L9
    //   di eseguire  *113,*  MainClass_C1_command_comm4( con argomento_ave4   uguale a avanzamento ,argomento_ave9   uguale a c270 )
    for (index_t i = 0; i < L_P1__GetParamSubcl95Length(my_id); ++i)
    {
    L_P1__Recor3 it = L_P1__GetRecSubcl95(my_id,i);
    
    L_P1__SetCAEvent2(it.mainc48,true);
    L_P1__SetCAArgom(it.mainc48,avanzamento);
    L_P1__SetCAArgom1(it.mainc48,c270);
    scheduler_NotifyCommand(L_P1_C1_TO_GLOBAL(it.mainc48));
    }
}


/*
    CNL corrispondente:
     {Comanda al campo MainClass_C1 di SubClass_C4_lista_L9
     di eseguire  commento: {113,}  MainClass_C1_command_comm4( con argomento_ave4   uguale a GialloxVerdex ,argomento_ave9   uguale a c270 ) }
*/
static inline void L_P1__Effec9(instance_id_t const my_id)
{
    
    //  Comanda al campo MainClass_C1 di SubClass_C4_lista_L9
    //   di eseguire  *113,*  MainClass_C1_command_comm4( con argomento_ave4   uguale a GialloxVerdex ,argomento_ave9   uguale a c270 )
    for (index_t i = 0; i < L_P1__GetParamSubcl95Length(my_id); ++i)
    {
    L_P1__Recor3 it = L_P1__GetRecSubcl95(my_id,i);
    
    L_P1__SetCAEvent2(it.mainc48,true);
    L_P1__SetCAArgom(it.mainc48,gialloxverd);
    L_P1__SetCAArgom1(it.mainc48,c270);
    scheduler_NotifyCommand(L_P1_C1_TO_GLOBAL(it.mainc48));
    }
}


/*
    CNL corrispondente:
     {Comanda al campo MainClass_C1 di SubClass_C4_lista_L9
     di eseguire  commento: {113,}  MainClass_C1_command_comm4( con argomento_ave4   uguale a GialloxVerdex ,argomento_ave9   uguale a avviox ) }
*/
static inline void L_P1__Effec10(instance_id_t const my_id)
{
    
    //  Comanda al campo MainClass_C1 di SubClass_C4_lista_L9
    //   di eseguire  *113,*  MainClass_C1_command_comm4( con argomento_ave4   uguale a GialloxVerdex ,argomento_ave9   uguale a avviox )
    for (index_t i = 0; i < L_P1__GetParamSubcl95Length(my_id); ++i)
    {
    L_P1__Recor3 it = L_P1__GetRecSubcl95(my_id,i);
    
    L_P1__SetCAEvent2(it.mainc48,true);
    L_P1__SetCAArgom(it.mainc48,gialloxverd);
    L_P1__SetCAArgom1(it.mainc48,avviox);
    scheduler_NotifyCommand(L_P1_C1_TO_GLOBAL(it.mainc48));
    }
}


/*
    CNL corrispondente:
     {Comanda al campo MainClass_C1 di SubClass_C4_lista_L9
     di eseguire  commento: {113,}  MainClass_C1_command_comm4( con argomento_ave4   uguale a avanzamento ,argomento_ave9   uguale a avviox ) }
*/
static inline void L_P1__Effec11(instance_id_t const my_id)
{
    
    //  Comanda al campo MainClass_C1 di SubClass_C4_lista_L9
    //   di eseguire  *113,*  MainClass_C1_command_comm4( con argomento_ave4   uguale a avanzamento ,argomento_ave9   uguale a avviox )
    for (index_t i = 0; i < L_P1__GetParamSubcl95Length(my_id); ++i)
    {
    L_P1__Recor3 it = L_P1__GetRecSubcl95(my_id,i);
    
    L_P1__SetCAEvent2(it.mainc48,true);
    L_P1__SetCAArgom(it.mainc48,avanzamento);
    L_P1__SetCAArgom1(it.mainc48,avviox);
    scheduler_NotifyCommand(L_P1_C1_TO_GLOBAL(it.mainc48));
    }
}


/*
    CNL corrispondente:
     {Comanda al campo MainClass_C1 di SubClass_C4_lista_L9
     di eseguire  commento: {113,}  MainClass_C1_command_comm4( con argomento_ave4   uguale a GialloxVerdex ,argomento_ave9   uguale a avviox ) }
*/
static inline void L_P1__Effec12(instance_id_t const my_id)
{
    
    //  Comanda al campo MainClass_C1 di SubClass_C4_lista_L9
    //   di eseguire  *113,*  MainClass_C1_command_comm4( con argomento_ave4   uguale a GialloxVerdex ,argomento_ave9   uguale a avviox )
    for (index_t i = 0; i < L_P1__GetParamSubcl95Length(my_id); ++i)
    {
    L_P1__Recor3 it = L_P1__GetRecSubcl95(my_id,i);
    
    L_P1__SetCAEvent2(it.mainc48,true);
    L_P1__SetCAArgom(it.mainc48,gialloxverd);
    L_P1__SetCAArgom1(it.mainc48,avviox);
    scheduler_NotifyCommand(L_P1_C1_TO_GLOBAL(it.mainc48));
    }
}


/*
    CNL corrispondente:
    
    {
    
    Comanda al campo MainClass_C1 di SubClass_C4_lista_L9
     di eseguire  commento: {113,}  MainClass_C1_command_comm4( con argomento_ave4   uguale a GialloxVerdex ,argomento_ave9   uguale a c270 )
    }
*/
static inline void L_P1__Effec13(instance_id_t const my_id)
{
    
    //  Comanda al campo MainClass_C1 di SubClass_C4_lista_L9
    //   di eseguire  *113,*  MainClass_C1_command_comm4( con argomento_ave4   uguale a GialloxVerdex ,argomento_ave9   uguale a c270 )
    for (index_t i = 0; i < L_P1__GetParamSubcl95Length(my_id); ++i)
    {
    L_P1__Recor3 it = L_P1__GetRecSubcl95(my_id,i);
    
    L_P1__SetCAEvent2(it.mainc48,true);
    L_P1__SetCAArgom(it.mainc48,gialloxverd);
    L_P1__SetCAArgom1(it.mainc48,c270);
    scheduler_NotifyCommand(L_P1_C1_TO_GLOBAL(it.mainc48));
    }
}



// ********** Definizione metodi **********

// Metodi standard

void L_P1_C4_Init(instance_id_t const my_id)
{
    // init variabili di stato
    L_P1__SetStato7(my_id, C4_St_Stato);
    L_P1__SetSubcl105(my_id, false);
    L_P1__SetSubcl107(my_id, 0);
    L_P1__SetSubcl109(my_id, 0);
    L_P1__SetSubcl111(my_id, false);
    L_P1__SetSubcl112(my_id, false);
    L_P1__SetSubcl113(my_id, rossoverde);
    // init controlli precedenti
    L_P1__SetSubcl100(my_id, false);
    L_P1__SetSubcl102(my_id, avanzamento1);
    L_P1__SetSubcl104(my_id, rossogiallo1);
    // init Timer e Counter
    Timer_AggmInit(L_P1__GetSubcl114(my_id), true, CLASS_L_P1_C4_ID, my_id, L_P1__subcl114_ID);
    Timer_Init(L_P1__GetSubcl114(my_id), 2000);
    Timer_AggmInit(L_P1__GetSubcl115(my_id), true, CLASS_L_P1_C4_ID, my_id, L_P1__subcl115_ID);
    Timer_Init(L_P1__GetSubcl115(my_id), 2000);
    Timer_AggmInit(L_P1__GetSubcl116(my_id), true, CLASS_L_P1_C4_ID, my_id, L_P1__subcl116_ID);
    Timer_Init(L_P1__GetSubcl116(my_id), 30213000);
    Timer_AggmInit(L_P1__GetSubcl117(my_id), true, CLASS_L_P1_C4_ID, my_id, L_P1__subcl117_ID);
    Timer_Init(L_P1__GetSubcl117(my_id), 30213000);
    Timer_AggmInit(L_P1__GetSubcl118(my_id), true, CLASS_L_P1_C4_ID, my_id, L_P1__subcl118_ID);
    Timer_Init(L_P1__GetSubcl118(my_id), 1000);
    Timer_AggmInit(L_P1__GetSubcl119(my_id), true, CLASS_L_P1_C4_ID, my_id, L_P1__subcl119_ID);
    Timer_Init(L_P1__GetSubcl119(my_id), 1000);
    Timer_AggmInit(L_P1__GetSubcl120(my_id), true, CLASS_L_P1_C4_ID, my_id, L_P1__subcl120_ID);
    Timer_Init(L_P1__GetSubcl120(my_id), 24000);
    Timer_AggmInit(L_P1__GetSubcl121(my_id), true, CLASS_L_P1_C4_ID, my_id, L_P1__subcl121_ID);
    Timer_Init(L_P1__GetSubcl121(my_id), 24000);
    Timer_AggmInit(L_P1__GetSubcl122(my_id), true, CLASS_L_P1_C4_ID, my_id, L_P1__subcl122_ID);
    Timer_Init(L_P1__GetSubcl122(my_id), 2000);
    Timer_AggmInit(L_P1__GetSubcl123(my_id), true, CLASS_L_P1_C4_ID, my_id, L_P1__subcl123_ID);
    Timer_Init(L_P1__GetSubcl123(my_id), 3000);
    Timer_AggmInit(L_P1__GetSubcl124(my_id), true, CLASS_L_P1_C4_ID, my_id, L_P1__subcl124_ID);
    Timer_Init(L_P1__GetSubcl124(my_id), 545000);
    Counter_AggmInit(L_P1__GetSubcl125(my_id), true, CLASS_L_P1_C4_ID, my_id, L_P1__subcl125_ID);
    Counter_Init(L_P1__GetSubcl125(my_id));
    Counter_AggmInit(L_P1__GetSubcl126(my_id), true, CLASS_L_P1_C4_ID, my_id, L_P1__subcl126_ID);
    Counter_Init(L_P1__GetSubcl126(my_id));
    // init response
    L_P1_C4_SetResponse(my_id, LDS_SCHED_NOP);

    // transizione iniziale
    if(L_P1__Guard6(my_id)) {
        L_P1_C4_SetState(my_id, C4_St_state);
	L_P1__Effec6(my_id);
    } else {
        STOP_EXECUTION(LOGIC_ERROR);
    }
    // init variabili precedenti
    L_P1__SetSubcl106(my_id, L_P1__GetSubcl105(my_id));
    L_P1__SetSubcl108(my_id, L_P1__GetSubcl107(my_id));
    L_P1__SetSubcl110(my_id, L_P1__GetSubcl109(my_id));
}

void L_P1_C4_Exec(instance_id_t const my_id, Phase const p)
{
    L_P1_C4_SetResponse(my_id, LDS_SCHED_NOP);
    switch (p) {

    case LDS_PHASE_MANUAL:
        break;
 

    case LDS_PHASE_STATE:

        switch (L_P1_C4_GetState(my_id)) {

        case C4_St_state1:
            if (L_P1__Guard13(my_id)) {
                L_P1_C4_SetState(my_id, C4_St_state1);
                L_P1__Effec13(my_id);				
            }
            else
                {STOP_EXECUTION(LOGIC_ERROR); } // fine transizioni da state1 nella fase LDS_PHASE_STATE
            break;

        case C4_St_state:
            if (L_P1__Guard12(my_id)) {
                L_P1_C4_SetState(my_id, C4_St_state1);
                L_P1__Effec12(my_id);				
            }
            else if (L_P1__Guard8(my_id)) {
                L_P1_C4_SetState(my_id, C4_St_state);
                L_P1__Effec8(my_id);				
            }
            else if (L_P1__Guard9(my_id)) {
                L_P1_C4_SetState(my_id, C4_St_state1);
                L_P1__Effec9(my_id);				
            }
            else if (L_P1__Guard10(my_id)) {
                L_P1_C4_SetState(my_id, C4_St_state1);
                L_P1__Effec10(my_id);				
            }
            else if (L_P1__Guard11(my_id)) {
                L_P1_C4_SetState(my_id, C4_St_state);
                L_P1__Effec11(my_id);				
            }
            else if (L_P1__Guard7(my_id)) {
                L_P1_C4_SetState(my_id, C4_St_state);
                L_P1__Effec7(my_id);				
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

ExecResponse L_P1_C4_GExec(global_id_t const proc_id, Phase const p)
{
    CHECK_LT(GLOBAL_TO_L_P1_C4(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C4(proc_id);
    L_P1_C4_Exec(my_id, p);
    return L_P1_C4_GetResponse(my_id);
}

void L_P1_C4_GTick(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C4(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C4(proc_id);
    Timer_Exec(L_P1__GetSubcl114(my_id));
    Timer_Exec(L_P1__GetSubcl115(my_id));
    Timer_Exec(L_P1__GetSubcl116(my_id));
    Timer_Exec(L_P1__GetSubcl117(my_id));
    Timer_Exec(L_P1__GetSubcl118(my_id));
    Timer_Exec(L_P1__GetSubcl119(my_id));
    Timer_Exec(L_P1__GetSubcl120(my_id));
    Timer_Exec(L_P1__GetSubcl121(my_id));
    Timer_Exec(L_P1__GetSubcl122(my_id));
    Timer_Exec(L_P1__GetSubcl123(my_id));
    Timer_Exec(L_P1__GetSubcl124(my_id));
}

void L_P1_C4_GSetSafe(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C4(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C4(proc_id);
    L_P1__SetOutSubcl88(my_id, true);
    L_P1__SetOutSubcl89(my_id, false);
    L_P1__SetOutSubcl90(my_id, gialloxverd);
}

void L_P1_C4_GUpdatePrev(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C4(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C4(proc_id);
    L_P1__SetSubcl100(my_id, L_P1__GetInSubcl99(my_id));
    L_P1__SetSubcl102(my_id, L_P1__GetInSubcl101(my_id));
    L_P1__SetSubcl104(my_id, L_P1__GetInSubcl103(my_id));
    L_P1__SetSubcl106(my_id, L_P1__GetSubcl105(my_id));
    L_P1__SetSubcl108(my_id, L_P1__GetSubcl107(my_id));
    L_P1__SetSubcl110(my_id, L_P1__GetSubcl109(my_id));
}

// ********** Definizione macro **********

// Macro di effetto

/*
    CNL corrispondente:
    
    { commento: {109,}  se il ripristino della variabile  SubClass_C4_restoreva_RV1 è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} e  se il contatore SubClass_C4_contatore_Co5 non è  minore di  commento: {55,} 15, commento: {71,}Decrementa il contatore SubClass_C4_contatore_Co8
    
       
      se il controllo ConsDef  è  uguale a FALSE  commento: {38,} o  se il contatore SubClass_C4_contatore_Co5 non è  maggiore di  commento: {54,} 154 commento: {36,} e  se il timer SubClass_C4_timer_T8 non è disattivo commento: {34,} o  se il parametro SubClass_C4_parametro_P1 non è  diverso da  False , commento: {66,} Assegna al comando SubClass_C4_comando_C9 il valore GialloxVerdex
    
     ,altrimenti   Applica gli effetti
           della macro SubClass_C4_macroef_M9( con argomento_af8   uguale a c180 ,argomento_af7   uguale a avanzamento ,argomento_af5   uguale a True ,argomento_af10   uguale a c180 ) commento: {73,}
    
    
     commento: {109,}  se il ripristino della variabile  SubClass_C4_restoreva_RV1 non è  uguale a  False  commento: {34,} e  se il parametro SubClass_C4_parametro_P2 non è  uguale a  True  e  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} o  se il timer SubClass_C4_timer_T8 non è attivo commento: {35,} o  se il controllo SubClass_C4_controllo_C8 è  diverso da GialloxVerdex, commento: {66,} Assegna al comando SubClass_C4_comando_C10 il valore  False 
    
       
     commento: {110,}  se il ripristino del timer  SubClass_C4_restoreTI_TI2 non è scaduto, commento: {68,}Attiva il timer SubClass_C4_timer_T2
    
       
     commento: {35,}  se il controllo SubClass_C4_controllo_C1 non è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE , commento: {70,}Incrementa il contatore SubClass_C4_contatore_Co8
    
     ,altrimenti   Applica gli effetti
           della macro SubClass_C4_macroef_M9( con argomento_af8   uguale a c180 ,argomento_af7   uguale a avanzamento ,argomento_af5   uguale a True ,argomento_af10   uguale a RossoVerde ) commento: {73,}
    
    
    
    }
*/
void L_P1__Macro31(instance_id_t const my_id )
{
//  *109,*  se il ripristino della variabile  SubClass_C4_restoreva_RV1 è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE  *38,* e  se il contatore SubClass_C4_contatore_Co5 non è  minore di  *55,* 15, *71,*Decrementa il contatore SubClass_C4_contatore_Co8
    bool res_AndLogicOP_0 = true;
    bool res_AndLogicOP_1 = true;
    res_AndLogicOP_1 = (res_AndLogicOP_1 && (L_P1__GetSubcl112(my_id) == false));
    res_AndLogicOP_1 = (res_AndLogicOP_1 && (L_P1__GetInConsd3(my_id) == false));
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_AndLogicOP_1);
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (Counter_GetValore(L_P1__GetSubcl125(my_id)) < 15u));
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_NotLogicOP_2);
    
    if(res_AndLogicOP_0){
    
    Counter_Decr(L_P1__GetSubcl126(my_id));
    }
    //  se il controllo ConsDef  è  uguale a FALSE  *38,* o  se il contatore SubClass_C4_contatore_Co5 non è  maggiore di  *54,* 154 *36,* e  se il timer SubClass_C4_timer_T8 non è disattivo *34,* o  se il parametro SubClass_C4_parametro_P1 non è  diverso da  False , *66,* Assegna al comando SubClass_C4_comando_C9 il valore GialloxVerdex
    // ,altrimenti   Applica gli effetti
    //       della macro SubClass_C4_macroef_M9( con argomento_af8   uguale a c180 ,argomento_af7   uguale a avanzamento ,argomento_af5   uguale a True ,argomento_af10   uguale a c180 )
    bool res_OrLogicOP_3 = false;
    bool res_OrLogicOP_4 = false;
    res_OrLogicOP_4 = (res_OrLogicOP_4 || (L_P1__GetInConsd3(my_id) == false));
    bool res_AndLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (Counter_GetValore(L_P1__GetSubcl125(my_id)) > 154u));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_6);
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! Timer_Disattivo(L_P1__GetSubcl124(my_id)));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_7);
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_AndLogicOP_5);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_OrLogicOP_4);
    bool res_NotLogicOP_8 = true;
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetParamSubcl96(my_id) == false));
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! res_NotLogicOP_9);
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_NotLogicOP_8);
    
    if(res_OrLogicOP_3){
    
    L_P1__SetOutSubcl90(my_id,gialloxverd);
    }else{
    
    L_P1__Macro32(my_id,c180,true,avanzamento,c180);
    }
    //  *73,*
    // *109,*  se il ripristino della variabile  SubClass_C4_restoreva_RV1 non è  uguale a  False  *34,* e  se il parametro SubClass_C4_parametro_P2 non è  uguale a  True  e  se il controllo ConsDef  è  uguale a FALSE  *36,* o  se il timer SubClass_C4_timer_T8 non è attivo *35,* o  se il controllo SubClass_C4_controllo_C8 è  diverso da GialloxVerdex, *66,* Assegna al comando SubClass_C4_comando_C10 il valore  False
    bool res_OrLogicOP_10 = false;
    bool res_OrLogicOP_11 = false;
    bool res_AndLogicOP_12 = true;
    bool res_AndLogicOP_13 = true;
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1__GetSubcl112(my_id) == false));
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_NotLogicOP_14);
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (L_P1__GetParamSubcl97(my_id) == true));
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_NotLogicOP_15);
    
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_AndLogicOP_13);
    res_AndLogicOP_12 = (res_AndLogicOP_12 && (L_P1__GetInConsd3(my_id) == false));
    
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_AndLogicOP_12);
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! Timer_Attivo(L_P1__GetSubcl124(my_id)));
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_NotLogicOP_16);
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_OrLogicOP_11);
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! (L_P1__GetInSubcl94(my_id) == gialloxverd));
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_NotLogicOP_17);
    
    if(res_OrLogicOP_10){
    
    L_P1__SetOutSubcl88(my_id,false);
    }
    //  *110,*  se il ripristino del timer  SubClass_C4_restoreTI_TI2 non è scaduto, *68,*Attiva il timer SubClass_C4_timer_T2
    bool res_NotLogicOP_18 = true;
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! Timer_Scaduto(L_P1__GetSubcl117(my_id)));
    if(res_NotLogicOP_18){
    
    Timer_Attiva(L_P1__GetSubcl122(my_id));
    }
    //  *35,*  se il controllo SubClass_C4_controllo_C1 non è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE , *70,*Incrementa il contatore SubClass_C4_contatore_Co8
    // ,altrimenti   Applica gli effetti
    //       della macro SubClass_C4_macroef_M9( con argomento_af8   uguale a c180 ,argomento_af7   uguale a avanzamento ,argomento_af5   uguale a True ,argomento_af10   uguale a RossoVerde )
    bool res_OrLogicOP_19 = false;
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! (L_P1__GetInSubcl91(my_id) == true));
    res_OrLogicOP_19 = (res_OrLogicOP_19 || res_NotLogicOP_20);
    res_OrLogicOP_19 = (res_OrLogicOP_19 || (L_P1__GetInConsd3(my_id) == false));
    
    if(res_OrLogicOP_19){
    
    Counter_Incr(L_P1__GetSubcl126(my_id));
    }else{
    
    L_P1__Macro32(my_id,rossoverde,true,avanzamento,c180);
    }
}

/*
    CNL corrispondente:
    
    { commento: {45,}  se  MainClass_C1_contatore_Co7 del campo  MainClass_C1 di SubClass_C4_lista_L9 è  diverso da  commento: {56,} 145021 commento: {35,} e  se il controllo SubClass_C4_controllo_C8 non è  diverso da GialloxVerdex commento: {35,} o  se il controllo SubClass_C4_controllo_C8 è  diverso da GialloxVerdex commento: {37,} e  se la variabile SubClass_C4_variabile_V3 è  uguale a c180 commento: {38,} o  se il contatore SubClass_C4_contatore_Co5 non è  maggiore di  commento: {54,} 143 commento: {34,} e  se il parametro SubClass_C4_parametro_P1 non è  uguale a  True ,  commento: {67,} Assegna alla variabile SubClass_C4_variabile_V3 il valore c180 commento: {67,}
    
       
    
    }
*/
void L_P1__Macro32(instance_id_t const my_id , C4_Enumerat3 argom90, bool argom91, C4_Enumerat2 argom92, C4_Enumerat3 argom93)
{
//  *45,*  se  MainClass_C1_contatore_Co7 del campo  MainClass_C1 di SubClass_C4_lista_L9 è  diverso da  *56,* 145021 *35,* e  se il controllo SubClass_C4_controllo_C8 non è  diverso da GialloxVerdex *35,* o  se il controllo SubClass_C4_controllo_C8 è  diverso da GialloxVerdex *37,* e  se la variabile SubClass_C4_variabile_V3 è  uguale a c180 *38,* o  se il contatore SubClass_C4_contatore_Co5 non è  maggiore di  *54,* 143 *34,* e  se il parametro SubClass_C4_parametro_P1 non è  uguale a  True ,  *67,* Assegna alla variabile SubClass_C4_variabile_V3 il valore c180
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_AndLogicOP_2 = true;
    bool res_ForAllPredicate_3 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl95Length(my_id); ++i)
    {
    L_P1__Recor3 it = L_P1__GetRecSubcl95(my_id,i);
    bool res_ImpliesLogicOp_4 = true;
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (Counter_GetValore(L_P1__GetMainc44(it.mainc48)) == 145021u));
    res_ImpliesLogicOp_4 = (res_ImpliesLogicOp_4 && res_NotLogicOP_5);
    res_ForAllPredicate_3 = res_ImpliesLogicOp_4;
    if(!res_ForAllPredicate_3) {break;}
    }
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_ForAllPredicate_3);
    bool res_NotLogicOP_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetInSubcl94(my_id) == gialloxverd));
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! res_NotLogicOP_7);
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_6);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_2);
    bool res_AndLogicOP_8 = true;
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetInSubcl94(my_id) == gialloxverd));
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_9);
    res_AndLogicOP_8 = (res_AndLogicOP_8 && (L_P1__GetSubcl113(my_id) == c180));
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_8);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_AndLogicOP_10 = true;
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (Counter_GetValore(L_P1__GetSubcl125(my_id)) > 143u));
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_NotLogicOP_11);
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (L_P1__GetParamSubcl96(my_id) == true));
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_NotLogicOP_12);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_10);
    
    if(res_OrLogicOP_0){
    
    L_P1__SetSubcl113(my_id,c180);
    }
}


// Macro di verifica

/*
    CNL corrispondente:
    
    { commento: {61,} commento: {109,}  se il ripristino della variabile  SubClass_C4_restoreva_RV1 non è  diverso da  False  commento: {38,} e  se il contatore SubClass_C4_contatore_Co5 è  maggiore di  commento: {54,} 154 commento: {35,} o  se il controllo SubClass_C4_controllo_C3 non è  uguale a GialloxVerdex commento: {38,} o  se il contatore SubClass_C4_contatore_Co8 non è  uguale a  commento: {53,} 155 commento: {36,} o  se il timer SubClass_C4_timer_T8 è disattivo, Tutte le seguenti { 
     commento: {61,} commento: {110,}  se il ripristino del timer  SubClass_C4_restoreTI_TI2 non è attivo commento: {34,} e  se il parametro SubClass_C4_parametro_P2 è  diverso da  False  commento: {36,} e  se il timer SubClass_C4_timer_T3 non è scaduto commento: {38,} e  se il contatore SubClass_C4_contatore_Co5 non è  minore di  commento: {55,} 11 commento: {36,} o  se il timer SubClass_C4_timer_T3 non è disattivo commento: {36,} o  se il timer SubClass_C4_timer_T3 non è scaduto, Tutte le seguenti { 
     commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C4_lista_L9 è  diverso da  commento: {56,}  state1  commento: {38,} e  se il contatore SubClass_C4_contatore_Co5 è  maggiore di  commento: {54,} 140213 commento: {34,} o  se il parametro SubClass_C4_parametro_P1 non è  uguale a  False  commento: {34,} e  se il parametro SubClass_C4_parametro_P9 non è  minore di  commento: {55,} 6 commento: {34,} o  se il parametro SubClass_C4_parametro_P1 non è  diverso da  True  commento: {34,} o  se il parametro SubClass_C4_parametro_P1 è  diverso da  True , Verifica che   commento: {47,48,49,50,52,}  commento: {,}  il controllo SubClass_C4_controllo_C8 sia  diverso da GialloxVerdex
     commento: {104,} e  che  commento: {,}  la variabile SubClass_C4_variabile_V3 non sia  uguale a c180
     commento: {104,} o  che  commento: {,}  il timer SubClass_C4_timer_T2 non sia attivo
     commento: {104,} o  che  commento: {37,}  la variabile SubClass_C4_variabile_V3 non sia  diverso da c180
     commento: {104,} e  che   l'argomento argomento_ave2 non  sia  uguale a  True  commento: {,} 
     commento: {104,} o  che  commento: {34,}  il parametro SubClass_C4_parametro_P1 sia  diverso da  False 
    
    
     } Verifica che   commento: {48,49,}  commento: {,}  il controllo SubClass_C4_controllo_C1 non sia  diverso da  False 
     commento: {104,} e  che  commento: {,}  il timer SubClass_C4_timer_T3 non sia attivo
    
    
     } Verifica che   commento: {47,48,51,52,}   l'argomento argomento_ave2 sia  uguale a  False  commento: {,} 
     commento: {104,} e  che  commento: {,}  il contatore SubClass_C4_contatore_Co8 non sia  diverso da  commento: {56,} 15
     commento: {104,} e  che  commento: {34,}  il parametro SubClass_C4_parametro_P9 non sia  uguale a  commento: {53,} 7
     commento: {104,} o  che  commento: {,}  il controllo SubClass_C4_controllo_C1 non sia  uguale a  True 
     commento: {104,} e  che  commento: {35,}  il controllo SubClass_C4_controllo_C1 non sia  uguale a  False 
    
    
    }
*/
bool L_P1__Macro35(instance_id_t const my_id , bool argom98, C4_Enumerat4 argom99, C4_Enumerat4 argom100, bool argom101)
{
bool res_AndLogicOP_0 = true;
    
    //  *61,* *109,*  se il ripristino della variabile  SubClass_C4_restoreva_RV1 non è  diverso da  False  *38,* e  se il contatore SubClass_C4_contatore_Co5 è  maggiore di  *54,* 154 *35,* o  se il controllo SubClass_C4_controllo_C3 non è  uguale a GialloxVerdex *38,* o  se il contatore SubClass_C4_contatore_Co8 non è  uguale a  *53,* 155 *36,* o  se il timer SubClass_C4_timer_T8 è disattivo, Tutte le seguenti { 
    //   *61,* *110,*  se il ripristino del timer  SubClass_C4_restoreTI_TI2 non è attivo *34,* e  se il parametro SubClass_C4_parametro_P2 è  diverso da  False  *36,* e  se il timer SubClass_C4_timer_T3 non è scaduto *38,* e  se il contatore SubClass_C4_contatore_Co5 non è  minore di  *55,* 11 *36,* o  se il timer SubClass_C4_timer_T3 non è disattivo *36,* o  se il timer SubClass_C4_timer_T3 non è scaduto, Tutte le seguenti { 
    //   *111,*  se lo stato del campo  MainClass_C1 di SubClass_C4_lista_L9 è  diverso da  *56,*  state1  *38,* e  se il contatore SubClass_C4_contatore_Co5 è  maggiore di  *54,* 140213 *34,* o  se il parametro SubClass_C4_parametro_P1 non è  uguale a  False  *34,* e  se il parametro SubClass_C4_parametro_P9 non è  minore di  *55,* 6 *34,* o  se il parametro SubClass_C4_parametro_P1 non è  diverso da  True  *34,* o  se il parametro SubClass_C4_parametro_P1 è  diverso da  True , Verifica che   *47,48,49,50,52,*  *,*  il controllo SubClass_C4_controllo_C8 sia  diverso da GialloxVerdex
    //   *104,* e  che  *,*  la variabile SubClass_C4_variabile_V3 non sia  uguale a c180
    //   *104,* o  che  *,*  il timer SubClass_C4_timer_T2 non sia attivo
    //   *104,* o  che  *37,*  la variabile SubClass_C4_variabile_V3 non sia  diverso da c180
    //   *104,* e  che   l'argomento argomento_ave2 non  sia  uguale a  True  *,* 
    //   *104,* o  che  *34,*  il parametro SubClass_C4_parametro_P1 sia  diverso da  False 
    //   } Verifica che   *48,49,*  *,*  il controllo SubClass_C4_controllo_C1 non sia  diverso da  False 
    //   *104,* e  che  *,*  il timer SubClass_C4_timer_T3 non sia attivo
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_OrLogicOP_4 = false;
    bool res_AndLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetSubcl112(my_id) == false));
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! res_NotLogicOP_7);
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_6);
    res_AndLogicOP_5 = (res_AndLogicOP_5 && (Counter_GetValore(L_P1__GetSubcl125(my_id)) > 154u));
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_AndLogicOP_5);
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetInSubcl92(my_id) == gialloxverd));
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_NotLogicOP_8);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_OrLogicOP_4);
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (Counter_GetValore(L_P1__GetSubcl126(my_id)) == 155u));
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_NotLogicOP_9);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    res_OrLogicOP_2 = (res_OrLogicOP_2 || Timer_Disattivo(L_P1__GetSubcl124(my_id)));
    
    if(res_OrLogicOP_2){
    bool res_AndLogicOP_10 = true;
    bool res_ImpliesLogicOp_11 = true;
    bool res_OrLogicOP_12 = false;
    bool res_OrLogicOP_13 = false;
    bool res_AndLogicOP_14 = true;
    bool res_AndLogicOP_15 = true;
    bool res_AndLogicOP_16 = true;
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! Timer_Attivo(L_P1__GetSubcl117(my_id)));
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_NotLogicOP_17);
    bool res_NotLogicOP_18 = true;
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! (L_P1__GetParamSubcl97(my_id) == false));
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_NotLogicOP_18);
    
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_AndLogicOP_16);
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! Timer_Scaduto(L_P1__GetSubcl123(my_id)));
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_NotLogicOP_19);
    
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_AndLogicOP_15);
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! (Counter_GetValore(L_P1__GetSubcl125(my_id)) < 11u));
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_NotLogicOP_20);
    
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_AndLogicOP_14);
    bool res_NotLogicOP_21 = true;
    res_NotLogicOP_21 = (res_NotLogicOP_21 && ! Timer_Disattivo(L_P1__GetSubcl123(my_id)));
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_NotLogicOP_21);
    
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_OrLogicOP_13);
    bool res_NotLogicOP_22 = true;
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! Timer_Scaduto(L_P1__GetSubcl123(my_id)));
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_NotLogicOP_22);
    
    if(res_OrLogicOP_12){
    bool res_ImpliesLogicOp_23 = true;
    bool res_OrLogicOP_24 = false;
    bool res_OrLogicOP_25 = false;
    bool res_OrLogicOP_26 = false;
    bool res_AndLogicOP_27 = true;
    bool res_ForAllPredicate_28 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl95Length(my_id); ++i)
    {
    L_P1__Recor3 it = L_P1__GetRecSubcl95(my_id,i);
    bool res_ImpliesLogicOp_29 = true;
    bool res_NotLogicOP_30 = true;
    res_NotLogicOP_30 = (res_NotLogicOP_30 && ! (L_P1_C1_GetState(it.mainc48) == C1_St_state));
    res_ImpliesLogicOp_29 = (res_ImpliesLogicOp_29 && res_NotLogicOP_30);
    res_ForAllPredicate_28 = res_ImpliesLogicOp_29;
    if(!res_ForAllPredicate_28) {break;}
    }
    res_AndLogicOP_27 = (res_AndLogicOP_27 && res_ForAllPredicate_28);
    res_AndLogicOP_27 = (res_AndLogicOP_27 && (Counter_GetValore(L_P1__GetSubcl125(my_id)) > 140213u));
    
    res_OrLogicOP_26 = (res_OrLogicOP_26 || res_AndLogicOP_27);
    bool res_AndLogicOP_31 = true;
    bool res_NotLogicOP_32 = true;
    res_NotLogicOP_32 = (res_NotLogicOP_32 && ! (L_P1__GetParamSubcl96(my_id) == false));
    res_AndLogicOP_31 = (res_AndLogicOP_31 && res_NotLogicOP_32);
    bool res_NotLogicOP_33 = true;
    res_NotLogicOP_33 = (res_NotLogicOP_33 && ! (L_P1__GetParamSubcl98(my_id) < 6u));
    res_AndLogicOP_31 = (res_AndLogicOP_31 && res_NotLogicOP_33);
    
    res_OrLogicOP_26 = (res_OrLogicOP_26 || res_AndLogicOP_31);
    
    res_OrLogicOP_25 = (res_OrLogicOP_25 || res_OrLogicOP_26);
    bool res_NotLogicOP_34 = true;
    bool res_NotLogicOP_35 = true;
    res_NotLogicOP_35 = (res_NotLogicOP_35 && ! (L_P1__GetParamSubcl96(my_id) == true));
    res_NotLogicOP_34 = (res_NotLogicOP_34 && ! res_NotLogicOP_35);
    res_OrLogicOP_25 = (res_OrLogicOP_25 || res_NotLogicOP_34);
    
    res_OrLogicOP_24 = (res_OrLogicOP_24 || res_OrLogicOP_25);
    bool res_NotLogicOP_36 = true;
    res_NotLogicOP_36 = (res_NotLogicOP_36 && ! (L_P1__GetParamSubcl96(my_id) == true));
    res_OrLogicOP_24 = (res_OrLogicOP_24 || res_NotLogicOP_36);
    
    if(res_OrLogicOP_24){
    bool res_OrLogicOP_37 = false;
    bool res_OrLogicOP_38 = false;
    bool res_OrLogicOP_39 = false;
    bool res_AndLogicOP_40 = true;
    bool res_NotLogicOP_41 = true;
    res_NotLogicOP_41 = (res_NotLogicOP_41 && ! (L_P1__GetInSubcl94(my_id) == gialloxverd));
    res_AndLogicOP_40 = (res_AndLogicOP_40 && res_NotLogicOP_41);
    bool res_NotLogicOP_42 = true;
    res_NotLogicOP_42 = (res_NotLogicOP_42 && ! (L_P1__GetSubcl113(my_id) == c180));
    res_AndLogicOP_40 = (res_AndLogicOP_40 && res_NotLogicOP_42);
    
    res_OrLogicOP_39 = (res_OrLogicOP_39 || res_AndLogicOP_40);
    bool res_NotLogicOP_43 = true;
    res_NotLogicOP_43 = (res_NotLogicOP_43 && ! Timer_Attivo(L_P1__GetSubcl122(my_id)));
    res_OrLogicOP_39 = (res_OrLogicOP_39 || res_NotLogicOP_43);
    
    res_OrLogicOP_38 = (res_OrLogicOP_38 || res_OrLogicOP_39);
    bool res_AndLogicOP_44 = true;
    bool res_NotLogicOP_45 = true;
    bool res_NotLogicOP_46 = true;
    res_NotLogicOP_46 = (res_NotLogicOP_46 && ! (L_P1__GetSubcl113(my_id) == c180));
    res_NotLogicOP_45 = (res_NotLogicOP_45 && ! res_NotLogicOP_46);
    res_AndLogicOP_44 = (res_AndLogicOP_44 && res_NotLogicOP_45);
    bool res_NotLogicOP_47 = true;
    res_NotLogicOP_47 = (res_NotLogicOP_47 && ! (argom98 == true));
    res_AndLogicOP_44 = (res_AndLogicOP_44 && res_NotLogicOP_47);
    
    res_OrLogicOP_38 = (res_OrLogicOP_38 || res_AndLogicOP_44);
    
    res_OrLogicOP_37 = (res_OrLogicOP_37 || res_OrLogicOP_38);
    bool res_NotLogicOP_48 = true;
    res_NotLogicOP_48 = (res_NotLogicOP_48 && ! (L_P1__GetParamSubcl96(my_id) == false));
    res_OrLogicOP_37 = (res_OrLogicOP_37 || res_NotLogicOP_48);
    
    res_ImpliesLogicOp_23 = (res_ImpliesLogicOp_23 && res_OrLogicOP_37);
    }
    res_ImpliesLogicOp_11 = (res_ImpliesLogicOp_11 && res_ImpliesLogicOp_23);
    }
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_ImpliesLogicOp_11);
    bool res_AndLogicOP_49 = true;
    bool res_NotLogicOP_50 = true;
    bool res_NotLogicOP_51 = true;
    res_NotLogicOP_51 = (res_NotLogicOP_51 && ! (L_P1__GetInSubcl91(my_id) == false));
    res_NotLogicOP_50 = (res_NotLogicOP_50 && ! res_NotLogicOP_51);
    res_AndLogicOP_49 = (res_AndLogicOP_49 && res_NotLogicOP_50);
    bool res_NotLogicOP_52 = true;
    res_NotLogicOP_52 = (res_NotLogicOP_52 && ! Timer_Attivo(L_P1__GetSubcl123(my_id)));
    res_AndLogicOP_49 = (res_AndLogicOP_49 && res_NotLogicOP_52);
    
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_AndLogicOP_49);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_AndLogicOP_10);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *47,48,51,52,*   l'argomento argomento_ave2 sia  uguale a  False  *,* 
    //   *104,* e  che  *,*  il contatore SubClass_C4_contatore_Co8 non sia  diverso da  *56,* 15
    //   *104,* e  che  *34,*  il parametro SubClass_C4_parametro_P9 non sia  uguale a  *53,* 7
    //   *104,* o  che  *,*  il controllo SubClass_C4_controllo_C1 non sia  uguale a  True 
    //   *104,* e  che  *35,*  il controllo SubClass_C4_controllo_C1 non sia  uguale a  False
    bool res_OrLogicOP_53 = false;
    bool res_AndLogicOP_54 = true;
    bool res_AndLogicOP_55 = true;
    res_AndLogicOP_55 = (res_AndLogicOP_55 && (argom98 == false));
    bool res_NotLogicOP_56 = true;
    bool res_NotLogicOP_57 = true;
    res_NotLogicOP_57 = (res_NotLogicOP_57 && ! (Counter_GetValore(L_P1__GetSubcl126(my_id)) == 15u));
    res_NotLogicOP_56 = (res_NotLogicOP_56 && ! res_NotLogicOP_57);
    res_AndLogicOP_55 = (res_AndLogicOP_55 && res_NotLogicOP_56);
    
    res_AndLogicOP_54 = (res_AndLogicOP_54 && res_AndLogicOP_55);
    bool res_NotLogicOP_58 = true;
    res_NotLogicOP_58 = (res_NotLogicOP_58 && ! (L_P1__GetParamSubcl98(my_id) == 7u));
    res_AndLogicOP_54 = (res_AndLogicOP_54 && res_NotLogicOP_58);
    
    res_OrLogicOP_53 = (res_OrLogicOP_53 || res_AndLogicOP_54);
    bool res_AndLogicOP_59 = true;
    bool res_NotLogicOP_60 = true;
    res_NotLogicOP_60 = (res_NotLogicOP_60 && ! (L_P1__GetInSubcl91(my_id) == true));
    res_AndLogicOP_59 = (res_AndLogicOP_59 && res_NotLogicOP_60);
    bool res_NotLogicOP_61 = true;
    res_NotLogicOP_61 = (res_NotLogicOP_61 && ! (L_P1__GetInSubcl91(my_id) == false));
    res_AndLogicOP_59 = (res_AndLogicOP_59 && res_NotLogicOP_61);
    
    res_OrLogicOP_53 = (res_OrLogicOP_53 || res_AndLogicOP_59);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_53);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
    
    { commento: {62,} commento: {44,}  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C4_lista_L9 è  uguale a  True  commento: {35,} e  se il controllo SubClass_C4_controllo_C8 è  diverso da GialloxVerdex commento: {34,} e  se il parametro SubClass_C4_parametro_P1 non è  diverso da  True  commento: {36,} o  se il timer SubClass_C4_timer_T3 è attivo commento: {34,} o  se il parametro SubClass_C4_parametro_P9 non è  maggiore di  commento: {54,} 5, Almeno una delle seguenti { 
      se l'argomento argomento_ave5 è  diverso da RossoGialloVerde commento: {39,} ,  commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C4_lista_L9 è  uguale a  commento: {53,}  state1 , commento: {88,} quando  commento: {42,}    MainClass_C1_controllo_C8 del campo  MainClass_C1     commento: {105,} è  uguale a avanzamento, Verifica che   commento: {47,48,51,52,}  commento: {34,}  il parametro SubClass_C4_parametro_P2 non sia  uguale a  True 
     commento: {104,} o  che  commento: {,}  il contatore SubClass_C4_contatore_Co5 non sia  maggiore di  commento: {54,} 11
     commento: {104,} e  che  commento: {38,}  il contatore SubClass_C4_contatore_Co5 sia  minore di  commento: {55,} 134
     commento: {104,} o  che   l'argomento argomento_ave6 non  sia  uguale a avanzamentox commento: {,} 
     commento: {104,} e  che  commento: {,}  il controllo SubClass_C4_controllo_C3 non sia  diverso da GialloxVerdex
     commento: {104,} o  che   l'argomento argomento_ave10 sia  diverso da RossoGialloVerde commento: {39,} 
    
    
     } Verifica che   commento: {50,51,52,}  commento: {,}  il contatore SubClass_C4_contatore_Co5 sia  minore di  commento: {55,} 115
     commento: {104,} o  che  commento: {,}  la variabile SubClass_C4_variabile_V3 non sia  uguale a c180
     commento: {104,} o  che  commento: {37,}  la variabile SubClass_C4_variabile_V3 sia  uguale a c180
     commento: {104,} o  che   l'argomento argomento_ave10 non  sia  uguale a RossoGialloVerde commento: {,} 
     commento: {104,} e  che  commento: {37,}  la variabile SubClass_C4_variabile_V3 sia  uguale a c180
    
    
    }
*/
bool L_P1__Macro36(instance_id_t const my_id , bool argom102, C4_Enumerat2 argom103, C4_Enumerat2 argom104, C4_Enumerat2 argom105, C4_Enumerat2 argom106, C4_Enumerat4 argom107)
{
bool res_AndLogicOP_0 = true;
    
    //  *62,* *44,*  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C4_lista_L9 è  uguale a  True  *35,* e  se il controllo SubClass_C4_controllo_C8 è  diverso da GialloxVerdex *34,* e  se il parametro SubClass_C4_parametro_P1 non è  diverso da  True  *36,* o  se il timer SubClass_C4_timer_T3 è attivo *34,* o  se il parametro SubClass_C4_parametro_P9 non è  maggiore di  *54,* 5, Almeno una delle seguenti { 
    //    se l'argomento argomento_ave5 è  diverso da RossoGialloVerde *39,* ,  *111,*  se lo stato del campo  MainClass_C1 di SubClass_C4_lista_L9 è  uguale a  *53,*  state1 , *88,* quando  *42,*    MainClass_C1_controllo_C8 del campo  MainClass_C1     *105,* è  uguale a avanzamento, Verifica che   *47,48,51,52,*  *34,*  il parametro SubClass_C4_parametro_P2 non sia  uguale a  True 
    //   *104,* o  che  *,*  il contatore SubClass_C4_contatore_Co5 non sia  maggiore di  *54,* 11
    //   *104,* e  che  *38,*  il contatore SubClass_C4_contatore_Co5 sia  minore di  *55,* 134
    //   *104,* o  che   l'argomento argomento_ave6 non  sia  uguale a avanzamentox *,* 
    //   *104,* e  che  *,*  il controllo SubClass_C4_controllo_C3 non sia  diverso da GialloxVerdex
    //   *104,* o  che   l'argomento argomento_ave10 sia  diverso da RossoGialloVerde *39,* 
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_AndLogicOP_4 = true;
    bool res_AndLogicOP_5 = true;
    bool res_ForAllPredicate_6 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl95Length(my_id); ++i)
    {
    L_P1__Recor3 it = L_P1__GetRecSubcl95(my_id,i);
    bool res_ImpliesLogicOp_7 = true;
    res_ImpliesLogicOp_7 = (res_ImpliesLogicOp_7 && (L_P1__GetMainc33(it.mainc48) == true));
    res_ForAllPredicate_6 = res_ImpliesLogicOp_7;
    if(!res_ForAllPredicate_6) {break;}
    }
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_ForAllPredicate_6);
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetInSubcl94(my_id) == gialloxverd));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_8);
    
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_AndLogicOP_5);
    bool res_NotLogicOP_9 = true;
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__GetParamSubcl96(my_id) == true));
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! res_NotLogicOP_10);
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_9);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_AndLogicOP_4);
    res_OrLogicOP_3 = (res_OrLogicOP_3 || Timer_Attivo(L_P1__GetSubcl123(my_id)));
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (L_P1__GetParamSubcl98(my_id) > 5u));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_11);
    
    if(res_OrLogicOP_2){
    bool res_ImpliesLogicOp_12 = true;
    bool res_AndLogicOP_13 = true;
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (argom106 == rossogiallo1));
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_NotLogicOP_14);
    bool res_ForAllPredicate_15 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl95Length(my_id); ++i)
    {
    L_P1__Recor3 it = L_P1__GetRecSubcl95(my_id,i);
    bool res_ImpliesLogicOp_16 = true;
    if((L_P1__GetInMainc4(it.mainc48) == avanzamento)){
    res_ImpliesLogicOp_16 = (res_ImpliesLogicOp_16 && (L_P1_C1_GetState(it.mainc48) == C1_St_state));
    }
    res_ForAllPredicate_15 = res_ImpliesLogicOp_16;
    if(!res_ForAllPredicate_15) {break;}
    }
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_ForAllPredicate_15);
    
    if(res_AndLogicOP_13){
    bool res_OrLogicOP_17 = false;
    bool res_OrLogicOP_18 = false;
    bool res_OrLogicOP_19 = false;
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! (L_P1__GetParamSubcl97(my_id) == true));
    res_OrLogicOP_19 = (res_OrLogicOP_19 || res_NotLogicOP_20);
    bool res_AndLogicOP_21 = true;
    bool res_NotLogicOP_22 = true;
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! (Counter_GetValore(L_P1__GetSubcl125(my_id)) > 11u));
    res_AndLogicOP_21 = (res_AndLogicOP_21 && res_NotLogicOP_22);
    res_AndLogicOP_21 = (res_AndLogicOP_21 && (Counter_GetValore(L_P1__GetSubcl125(my_id)) < 134u));
    
    res_OrLogicOP_19 = (res_OrLogicOP_19 || res_AndLogicOP_21);
    
    res_OrLogicOP_18 = (res_OrLogicOP_18 || res_OrLogicOP_19);
    bool res_AndLogicOP_23 = true;
    bool res_NotLogicOP_24 = true;
    res_NotLogicOP_24 = (res_NotLogicOP_24 && ! (argom107 == avanzamento1));
    res_AndLogicOP_23 = (res_AndLogicOP_23 && res_NotLogicOP_24);
    bool res_NotLogicOP_25 = true;
    bool res_NotLogicOP_26 = true;
    res_NotLogicOP_26 = (res_NotLogicOP_26 && ! (L_P1__GetInSubcl92(my_id) == gialloxverd));
    res_NotLogicOP_25 = (res_NotLogicOP_25 && ! res_NotLogicOP_26);
    res_AndLogicOP_23 = (res_AndLogicOP_23 && res_NotLogicOP_25);
    
    res_OrLogicOP_18 = (res_OrLogicOP_18 || res_AndLogicOP_23);
    
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_OrLogicOP_18);
    bool res_NotLogicOP_27 = true;
    res_NotLogicOP_27 = (res_NotLogicOP_27 && ! (argom103 == rossogiallo1));
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_NotLogicOP_27);
    
    res_ImpliesLogicOp_12 = (res_ImpliesLogicOp_12 && res_OrLogicOP_17);
    }
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_ImpliesLogicOp_12);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *50,51,52,*  *,*  il contatore SubClass_C4_contatore_Co5 sia  minore di  *55,* 115
    //   *104,* o  che  *,*  la variabile SubClass_C4_variabile_V3 non sia  uguale a c180
    //   *104,* o  che  *37,*  la variabile SubClass_C4_variabile_V3 sia  uguale a c180
    //   *104,* o  che   l'argomento argomento_ave10 non  sia  uguale a RossoGialloVerde *,* 
    //   *104,* e  che  *37,*  la variabile SubClass_C4_variabile_V3 sia  uguale a c180
    bool res_OrLogicOP_28 = false;
    bool res_OrLogicOP_29 = false;
    bool res_OrLogicOP_30 = false;
    res_OrLogicOP_30 = (res_OrLogicOP_30 || (Counter_GetValore(L_P1__GetSubcl125(my_id)) < 115u));
    bool res_NotLogicOP_31 = true;
    res_NotLogicOP_31 = (res_NotLogicOP_31 && ! (L_P1__GetSubcl113(my_id) == c180));
    res_OrLogicOP_30 = (res_OrLogicOP_30 || res_NotLogicOP_31);
    
    res_OrLogicOP_29 = (res_OrLogicOP_29 || res_OrLogicOP_30);
    res_OrLogicOP_29 = (res_OrLogicOP_29 || (L_P1__GetSubcl113(my_id) == c180));
    
    res_OrLogicOP_28 = (res_OrLogicOP_28 || res_OrLogicOP_29);
    bool res_AndLogicOP_32 = true;
    bool res_NotLogicOP_33 = true;
    res_NotLogicOP_33 = (res_NotLogicOP_33 && ! (argom103 == rossogiallo1));
    res_AndLogicOP_32 = (res_AndLogicOP_32 && res_NotLogicOP_33);
    res_AndLogicOP_32 = (res_AndLogicOP_32 && (L_P1__GetSubcl113(my_id) == c180));
    
    res_OrLogicOP_28 = (res_OrLogicOP_28 || res_AndLogicOP_32);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_28);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
     
    { commento: {62,} commento: {110,}  se il ripristino del timer  SubClass_C4_restoreTI_TI1 non è scaduto commento: {34,} o  se il parametro SubClass_C4_parametro_P1 è  diverso da  True , Almeno una delle seguenti { 
     commento: {63,} commento: {34,}  se il parametro SubClass_C4_parametro_P1 è  diverso da  False  commento: {35,} e  se il controllo SubClass_C4_controllo_C8 non è  uguale a GialloxVerdex, Solo una delle seguenti { 
     commento: {62,} commento: {34,}  se il parametro SubClass_C4_parametro_P1 è  uguale a  True  e  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro SubClass_C4_parametro_P9 non è  maggiore di  commento: {54,} 9 commento: {36,} e  se il timer SubClass_C4_timer_T3 non è scaduto commento: {34,} o  se il parametro SubClass_C4_parametro_P1 non è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
     commento: {62,} commento: {34,}  se lo stato  è  uguale a  commento: {53,}  state1  commento: {106,} commento: {37,} e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180 commento: {35,} o  se il controllo SubClass_C4_controllo_C8 è  uguale a GialloxVerdex, Almeno una delle seguenti { 
     commento: {61,} commento: {36,}  se il timer SubClass_C4_timer_T2 è scaduto e  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
     commento: {61,}  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
     commento: {61,} commento: {41,}  se MainClass_C1_parametro_P2 del campo  MainClass_C1 di SubClass_C4_lista_L9 è  uguale a  commento: {53,} 5 commento: {38,} e  se il contatore SubClass_C4_contatore_Co5 non è  maggiore di  commento: {54,} 130213, Tutte le seguenti { 
     commento: {63,} commento: {109,}  se il ripristino della variabile  SubClass_C4_restoreva_RV1 è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
     commento: {61,} commento: {34,}  se il parametro SubClass_C4_parametro_P9 è  minore di  commento: {55,} 2, Tutte le seguenti { 
     commento: {63,} commento: {34,}  se il parametro SubClass_C4_parametro_P9 non è  maggiore di  commento: {54,} 5 commento: {37,} o  se la variabile SubClass_C4_variabile_V3 è  diverso da c180 o  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
     commento: {62,} commento: {110,}  se il ripristino del timer  SubClass_C4_restoreTI_TI2 è attivo commento: {34,} e  se il parametro SubClass_C4_parametro_P2 non è  uguale a  False , Almeno una delle seguenti { 
      se il ripristino dello stato  è  diverso da  commento: {56,}  state1  commento: {107,} commento: {37,} e  se la variabile SubClass_C4_variabile_V3 non è  diverso da c180 commento: {34,} o  se il parametro SubClass_C4_parametro_P2 non è  diverso da  False  commento: {35,} o  se il controllo SubClass_C4_controllo_C8 non è  uguale a GialloxVerdex commento: {34,} e  se il parametro SubClass_C4_parametro_P1 è  uguale a  True  commento: {37,} e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180, Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
    
    
     } Verifica che   commento: {47,48,49,}  commento: {,}  il timer SubClass_C4_timer_T2 sia scaduto
     commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} e  che  commento: {34,}  il parametro SubClass_C4_parametro_P1 non sia  diverso da  True 
     commento: {104,} e  che  commento: {34,}  il parametro SubClass_C4_parametro_P1 non sia  diverso da  False 
    
    
     } Verifica che   commento: {51,}  commento: {,}  il contatore SubClass_C4_contatore_Co8 sia  maggiore di  commento: {54,} 11
     commento: {104,} o  che  commento: {38,}  il contatore SubClass_C4_contatore_Co8 sia  diverso da  commento: {56,} 130
    
    
     } Verifica che   commento: {47,50,51,}  commento: {,}  il contatore SubClass_C4_contatore_Co8 non sia  maggiore di  commento: {54,} 11213
     commento: {104,} o  che  commento: {34,}  il parametro SubClass_C4_parametro_P1 sia  uguale a  False 
     commento: {104,} e  che  commento: {34,}  il parametro SubClass_C4_parametro_P1 sia  uguale a  False 
     commento: {104,} o  che  commento: {,}  la variabile SubClass_C4_variabile_V3 sia  diverso da c180
     commento: {104,} o  che  commento: {38,}  il contatore SubClass_C4_contatore_Co5 non sia  maggiore di  commento: {54,} 13
    
    
     } Verifica che   commento: {48,51,}   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} e  che  commento: {,}  il contatore SubClass_C4_contatore_Co5 sia  minore di  commento: {55,} 13
    
    
     } Verifica che   commento: {48,49,50,}  commento: {,}  il timer SubClass_C4_timer_T3 non sia attivo
     commento: {104,} e  che  commento: {,}  la variabile SubClass_C4_variabile_V3 non sia  diverso da c180
     commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} o  che  commento: {36,}  il timer SubClass_C4_timer_T3 non sia disattivo
     commento: {104,} e  che  commento: {36,}  il timer SubClass_C4_timer_T2 sia attivo
     commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
    
    
     } Verifica che   commento: {47,51,}  commento: {34,}  il parametro SubClass_C4_parametro_P1 non sia  diverso da  False 
     commento: {104,} e  che  commento: {,}  il contatore SubClass_C4_contatore_Co8 sia  minore di  commento: {55,} 1213
    
    
     } Verifica che   commento: {48,51,}   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} o  che  commento: {,}  il contatore SubClass_C4_contatore_Co5 non sia  uguale a  commento: {53,} 11
     commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
    
    
     } Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
    
    
     } Verifica che   commento: {47,48,49,50,}  commento: {,}  il controllo SubClass_C4_controllo_C3 non sia  diverso da GialloxVerdex
     commento: {104,} e  che  commento: {,}  il timer SubClass_C4_timer_T8 sia scaduto
     commento: {104,} o  che  commento: {34,}  il parametro SubClass_C4_parametro_P1 sia  uguale a  False 
     commento: {104,} o  che  commento: {,}  la variabile SubClass_C4_variabile_V3 sia  uguale a c180
     commento: {104,} o  che  commento: {36,}  il timer SubClass_C4_timer_T3 non sia disattivo
     commento: {104,} e  che  commento: {35,}  il controllo SubClass_C4_controllo_C8 non sia  diverso da GialloxVerdex
    
    
     } Verifica che   commento: {50,}  commento: {,}  la variabile SubClass_C4_variabile_V3 sia  diverso da c180
    
    
     } Verifica che   commento: {47,48,50,}  commento: {34,}  il parametro SubClass_C4_parametro_P2 sia  uguale a  False 
     commento: {104,} o  che  commento: {,}  la variabile SubClass_C4_variabile_V3 sia  diverso da c180
     commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} e  che  commento: {34,}  il parametro SubClass_C4_parametro_P1 sia  diverso da  True 
     commento: {104,} o  che  commento: {,}  il controllo SubClass_C4_controllo_C8 sia  uguale a GialloxVerdex
     commento: {104,} e  che  commento: {35,}  il controllo SubClass_C4_controllo_C8 non sia  diverso da GialloxVerdex
    
    
    }
*/
bool L_P1__Macro37(instance_id_t const my_id )
{
bool res_AndLogicOP_0 = true;
    
    //  *62,* *110,*  se il ripristino del timer  SubClass_C4_restoreTI_TI1 non è scaduto *34,* o  se il parametro SubClass_C4_parametro_P1 è  diverso da  True , Almeno una delle seguenti { 
    //   *63,* *34,*  se il parametro SubClass_C4_parametro_P1 è  diverso da  False  *35,* e  se il controllo SubClass_C4_controllo_C8 non è  uguale a GialloxVerdex, Solo una delle seguenti { 
    //   *62,* *34,*  se il parametro SubClass_C4_parametro_P1 è  uguale a  True  e  se il controllo ConsDef  è  uguale a FALSE  *34,* e  se il parametro SubClass_C4_parametro_P9 non è  maggiore di  *54,* 9 *36,* e  se il timer SubClass_C4_timer_T3 non è scaduto *34,* o  se il parametro SubClass_C4_parametro_P1 non è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
    //   *62,* *34,*  se lo stato  è  uguale a  *53,*  state1  *106,* *37,* e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180 *35,* o  se il controllo SubClass_C4_controllo_C8 è  uguale a GialloxVerdex, Almeno una delle seguenti { 
    //   *61,* *36,*  se il timer SubClass_C4_timer_T2 è scaduto e  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
    //   *61,*  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
    //   *61,* *41,*  se MainClass_C1_parametro_P2 del campo  MainClass_C1 di SubClass_C4_lista_L9 è  uguale a  *53,* 5 *38,* e  se il contatore SubClass_C4_contatore_Co5 non è  maggiore di  *54,* 130213, Tutte le seguenti { 
    //   *63,* *109,*  se il ripristino della variabile  SubClass_C4_restoreva_RV1 è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
    //   *61,* *34,*  se il parametro SubClass_C4_parametro_P9 è  minore di  *55,* 2, Tutte le seguenti { 
    //   *63,* *34,*  se il parametro SubClass_C4_parametro_P9 non è  maggiore di  *54,* 5 *37,* o  se la variabile SubClass_C4_variabile_V3 è  diverso da c180 o  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
    //   *62,* *110,*  se il ripristino del timer  SubClass_C4_restoreTI_TI2 è attivo *34,* e  se il parametro SubClass_C4_parametro_P2 non è  uguale a  False , Almeno una delle seguenti { 
    //    se il ripristino dello stato  è  diverso da  *56,*  state1  *107,* *37,* e  se la variabile SubClass_C4_variabile_V3 non è  diverso da c180 *34,* o  se il parametro SubClass_C4_parametro_P2 non è  diverso da  False  *35,* o  se il controllo SubClass_C4_controllo_C8 non è  uguale a GialloxVerdex *34,* e  se il parametro SubClass_C4_parametro_P1 è  uguale a  True  *37,* e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180, Verifica che   *48,*   il controllo ConsDef  sia  uguale a FALSE 
    //   } Verifica che   *47,48,49,*  *,*  il timer SubClass_C4_timer_T2 sia scaduto
    //   *104,* o  che   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* e  che  *34,*  il parametro SubClass_C4_parametro_P1 non sia  diverso da  True 
    //   *104,* e  che  *34,*  il parametro SubClass_C4_parametro_P1 non sia  diverso da  False 
    //   } Verifica che   *51,*  *,*  il contatore SubClass_C4_contatore_Co8 sia  maggiore di  *54,* 11
    //   *104,* o  che  *38,*  il contatore SubClass_C4_contatore_Co8 sia  diverso da  *56,* 130
    //   } Verifica che   *47,50,51,*  *,*  il contatore SubClass_C4_contatore_Co8 non sia  maggiore di  *54,* 11213
    //   *104,* o  che  *34,*  il parametro SubClass_C4_parametro_P1 sia  uguale a  False 
    //   *104,* e  che  *34,*  il parametro SubClass_C4_parametro_P1 sia  uguale a  False 
    //   *104,* o  che  *,*  la variabile SubClass_C4_variabile_V3 sia  diverso da c180
    //   *104,* o  che  *38,*  il contatore SubClass_C4_contatore_Co5 non sia  maggiore di  *54,* 13
    //   } Verifica che   *48,51,*   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* e  che  *,*  il contatore SubClass_C4_contatore_Co5 sia  minore di  *55,* 13
    //   } Verifica che   *48,49,50,*  *,*  il timer SubClass_C4_timer_T3 non sia attivo
    //   *104,* e  che  *,*  la variabile SubClass_C4_variabile_V3 non sia  diverso da c180
    //   *104,* o  che   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* o  che  *36,*  il timer SubClass_C4_timer_T3 non sia disattivo
    //   *104,* e  che  *36,*  il timer SubClass_C4_timer_T2 sia attivo
    //   *104,* e  che   il controllo ConsDef  sia  uguale a FALSE 
    //   } Verifica che   *47,51,*  *34,*  il parametro SubClass_C4_parametro_P1 non sia  diverso da  False 
    //   *104,* e  che  *,*  il contatore SubClass_C4_contatore_Co8 sia  minore di  *55,* 1213
    //   } Verifica che   *48,51,*   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* o  che  *,*  il contatore SubClass_C4_contatore_Co5 non sia  uguale a  *53,* 11
    //   *104,* e  che   il controllo ConsDef  sia  uguale a FALSE 
    //   } Verifica che   *48,*   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* e  che   il controllo ConsDef  sia  uguale a FALSE 
    //   } Verifica che   *47,48,49,50,*  *,*  il controllo SubClass_C4_controllo_C3 non sia  diverso da GialloxVerdex
    //   *104,* e  che  *,*  il timer SubClass_C4_timer_T8 sia scaduto
    //   *104,* o  che  *34,*  il parametro SubClass_C4_parametro_P1 sia  uguale a  False 
    //   *104,* o  che  *,*  la variabile SubClass_C4_variabile_V3 sia  uguale a c180
    //   *104,* o  che  *36,*  il timer SubClass_C4_timer_T3 non sia disattivo
    //   *104,* e  che  *35,*  il controllo SubClass_C4_controllo_C8 non sia  diverso da GialloxVerdex
    //   } Verifica che   *50,*  *,*  la variabile SubClass_C4_variabile_V3 sia  diverso da c180
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! Timer_Scaduto(L_P1__GetSubcl115(my_id)));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_3);
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetParamSubcl96(my_id) == true));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_4);
    
    if(res_OrLogicOP_2){
    bool res_OrLogicOP_5 = false;
    bool res_ImpliesLogicOp_6 = true;
    bool res_AndLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetParamSubcl96(my_id) == false));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_8);
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetInSubcl94(my_id) == gialloxverd));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_9);
    
    if(res_AndLogicOP_7){
    bool res_XorLogicOP_10 = true;
    int xorIndex_res_XorLogicOP_10 = 0;
    bool res_ImpliesLogicOp_11 = true;
    bool res_OrLogicOP_12 = false;
    bool res_OrLogicOP_13 = false;
    bool res_AndLogicOP_14 = true;
    bool res_AndLogicOP_15 = true;
    bool res_AndLogicOP_16 = true;
    res_AndLogicOP_16 = (res_AndLogicOP_16 && (L_P1__GetParamSubcl96(my_id) == true));
    res_AndLogicOP_16 = (res_AndLogicOP_16 && (L_P1__GetInConsd3(my_id) == false));
    
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_AndLogicOP_16);
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! (L_P1__GetParamSubcl98(my_id) > 9u));
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_NotLogicOP_17);
    
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_AndLogicOP_15);
    bool res_NotLogicOP_18 = true;
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! Timer_Scaduto(L_P1__GetSubcl123(my_id)));
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_NotLogicOP_18);
    
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_AndLogicOP_14);
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (L_P1__GetParamSubcl96(my_id) == true));
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_NotLogicOP_19);
    
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_OrLogicOP_13);
    res_OrLogicOP_12 = (res_OrLogicOP_12 || (L_P1__GetInConsd3(my_id) == false));
    
    if(res_OrLogicOP_12){
    bool res_OrLogicOP_20 = false;
    bool res_ImpliesLogicOp_21 = true;
    bool res_OrLogicOP_22 = false;
    bool res_AndLogicOP_23 = true;
    res_AndLogicOP_23 = (res_AndLogicOP_23 && (L_P1_C4_GetState(my_id) == C4_St_state));
    bool res_NotLogicOP_24 = true;
    res_NotLogicOP_24 = (res_NotLogicOP_24 && ! (L_P1__GetSubcl113(my_id) == c180));
    res_AndLogicOP_23 = (res_AndLogicOP_23 && res_NotLogicOP_24);
    
    res_OrLogicOP_22 = (res_OrLogicOP_22 || res_AndLogicOP_23);
    res_OrLogicOP_22 = (res_OrLogicOP_22 || (L_P1__GetInSubcl94(my_id) == gialloxverd));
    
    if(res_OrLogicOP_22){
    bool res_OrLogicOP_25 = false;
    bool res_ImpliesLogicOp_26 = true;
    bool res_AndLogicOP_27 = true;
    res_AndLogicOP_27 = (res_AndLogicOP_27 && Timer_Scaduto(L_P1__GetSubcl122(my_id)));
    res_AndLogicOP_27 = (res_AndLogicOP_27 && (L_P1__GetInConsd3(my_id) == false));
    
    if(res_AndLogicOP_27){
    bool res_AndLogicOP_28 = true;
    bool res_ImpliesLogicOp_29 = true;
    if((L_P1__GetInConsd3(my_id) == false)){
    bool res_AndLogicOP_30 = true;
    bool res_ImpliesLogicOp_31 = true;
    bool res_AndLogicOP_32 = true;
    bool res_ForAllPredicate_33 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl95Length(my_id); ++i)
    {
    L_P1__Recor3 it = L_P1__GetRecSubcl95(my_id,i);
    bool res_ImpliesLogicOp_34 = true;
    res_ImpliesLogicOp_34 = (res_ImpliesLogicOp_34 && (L_P1__GetParamMainc6(it.mainc48) == 5u));
    res_ForAllPredicate_33 = res_ImpliesLogicOp_34;
    if(!res_ForAllPredicate_33) {break;}
    }
    res_AndLogicOP_32 = (res_AndLogicOP_32 && res_ForAllPredicate_33);
    bool res_NotLogicOP_35 = true;
    res_NotLogicOP_35 = (res_NotLogicOP_35 && ! (Counter_GetValore(L_P1__GetSubcl125(my_id)) > 130213u));
    res_AndLogicOP_32 = (res_AndLogicOP_32 && res_NotLogicOP_35);
    
    if(res_AndLogicOP_32){
    bool res_AndLogicOP_36 = true;
    bool res_ImpliesLogicOp_37 = true;
    bool res_OrLogicOP_38 = false;
    res_OrLogicOP_38 = (res_OrLogicOP_38 || (L_P1__GetSubcl112(my_id) == true));
    res_OrLogicOP_38 = (res_OrLogicOP_38 || (L_P1__GetInConsd3(my_id) == false));
    
    if(res_OrLogicOP_38){
    bool res_XorLogicOP_39 = true;
    int xorIndex_res_XorLogicOP_39 = 0;
    bool res_ImpliesLogicOp_40 = true;
    if((L_P1__GetParamSubcl98(my_id) < 2u)){
    bool res_AndLogicOP_41 = true;
    bool res_ImpliesLogicOp_42 = true;
    bool res_OrLogicOP_43 = false;
    bool res_OrLogicOP_44 = false;
    bool res_NotLogicOP_45 = true;
    res_NotLogicOP_45 = (res_NotLogicOP_45 && ! (L_P1__GetParamSubcl98(my_id) > 5u));
    res_OrLogicOP_44 = (res_OrLogicOP_44 || res_NotLogicOP_45);
    bool res_NotLogicOP_46 = true;
    res_NotLogicOP_46 = (res_NotLogicOP_46 && ! (L_P1__GetSubcl113(my_id) == c180));
    res_OrLogicOP_44 = (res_OrLogicOP_44 || res_NotLogicOP_46);
    
    res_OrLogicOP_43 = (res_OrLogicOP_43 || res_OrLogicOP_44);
    res_OrLogicOP_43 = (res_OrLogicOP_43 || (L_P1__GetInConsd3(my_id) == false));
    
    if(res_OrLogicOP_43){
    bool res_XorLogicOP_47 = true;
    int xorIndex_res_XorLogicOP_47 = 0;
    bool res_ImpliesLogicOp_48 = true;
    bool res_AndLogicOP_49 = true;
    res_AndLogicOP_49 = (res_AndLogicOP_49 && Timer_Attivo(L_P1__GetSubcl117(my_id)));
    bool res_NotLogicOP_50 = true;
    res_NotLogicOP_50 = (res_NotLogicOP_50 && ! (L_P1__GetParamSubcl97(my_id) == false));
    res_AndLogicOP_49 = (res_AndLogicOP_49 && res_NotLogicOP_50);
    
    if(res_AndLogicOP_49){
    bool res_ImpliesLogicOp_51 = true;
    bool res_OrLogicOP_52 = false;
    bool res_OrLogicOP_53 = false;
    bool res_AndLogicOP_54 = true;
    bool res_NotLogicOP_55 = true;
    res_NotLogicOP_55 = (res_NotLogicOP_55 && ! (L_P1__GetStato7(my_id) == C4_St_state));
    res_AndLogicOP_54 = (res_AndLogicOP_54 && res_NotLogicOP_55);
    bool res_NotLogicOP_56 = true;
    bool res_NotLogicOP_57 = true;
    res_NotLogicOP_57 = (res_NotLogicOP_57 && ! (L_P1__GetSubcl113(my_id) == c180));
    res_NotLogicOP_56 = (res_NotLogicOP_56 && ! res_NotLogicOP_57);
    res_AndLogicOP_54 = (res_AndLogicOP_54 && res_NotLogicOP_56);
    
    res_OrLogicOP_53 = (res_OrLogicOP_53 || res_AndLogicOP_54);
    bool res_NotLogicOP_58 = true;
    bool res_NotLogicOP_59 = true;
    res_NotLogicOP_59 = (res_NotLogicOP_59 && ! (L_P1__GetParamSubcl97(my_id) == false));
    res_NotLogicOP_58 = (res_NotLogicOP_58 && ! res_NotLogicOP_59);
    res_OrLogicOP_53 = (res_OrLogicOP_53 || res_NotLogicOP_58);
    
    res_OrLogicOP_52 = (res_OrLogicOP_52 || res_OrLogicOP_53);
    bool res_AndLogicOP_60 = true;
    bool res_AndLogicOP_61 = true;
    bool res_NotLogicOP_62 = true;
    res_NotLogicOP_62 = (res_NotLogicOP_62 && ! (L_P1__GetInSubcl94(my_id) == gialloxverd));
    res_AndLogicOP_61 = (res_AndLogicOP_61 && res_NotLogicOP_62);
    res_AndLogicOP_61 = (res_AndLogicOP_61 && (L_P1__GetParamSubcl96(my_id) == true));
    
    res_AndLogicOP_60 = (res_AndLogicOP_60 && res_AndLogicOP_61);
    bool res_NotLogicOP_63 = true;
    res_NotLogicOP_63 = (res_NotLogicOP_63 && ! (L_P1__GetSubcl113(my_id) == c180));
    res_AndLogicOP_60 = (res_AndLogicOP_60 && res_NotLogicOP_63);
    
    res_OrLogicOP_52 = (res_OrLogicOP_52 || res_AndLogicOP_60);
    
    if(res_OrLogicOP_52){
    res_ImpliesLogicOp_51 = (res_ImpliesLogicOp_51 && (L_P1__GetInConsd3(my_id) == false));
    }
    res_ImpliesLogicOp_48 = (res_ImpliesLogicOp_48 && res_ImpliesLogicOp_51);
    }
    if(res_ImpliesLogicOp_48){
    xorIndex_res_XorLogicOP_47 = (xorIndex_res_XorLogicOP_47 + 1);
    }
    bool res_OrLogicOP_64 = false;
    res_OrLogicOP_64 = (res_OrLogicOP_64 || Timer_Scaduto(L_P1__GetSubcl122(my_id)));
    bool res_AndLogicOP_65 = true;
    bool res_AndLogicOP_66 = true;
    res_AndLogicOP_66 = (res_AndLogicOP_66 && (L_P1__GetInConsd3(my_id) == false));
    bool res_NotLogicOP_67 = true;
    bool res_NotLogicOP_68 = true;
    res_NotLogicOP_68 = (res_NotLogicOP_68 && ! (L_P1__GetParamSubcl96(my_id) == true));
    res_NotLogicOP_67 = (res_NotLogicOP_67 && ! res_NotLogicOP_68);
    res_AndLogicOP_66 = (res_AndLogicOP_66 && res_NotLogicOP_67);
    
    res_AndLogicOP_65 = (res_AndLogicOP_65 && res_AndLogicOP_66);
    bool res_NotLogicOP_69 = true;
    bool res_NotLogicOP_70 = true;
    res_NotLogicOP_70 = (res_NotLogicOP_70 && ! (L_P1__GetParamSubcl96(my_id) == false));
    res_NotLogicOP_69 = (res_NotLogicOP_69 && ! res_NotLogicOP_70);
    res_AndLogicOP_65 = (res_AndLogicOP_65 && res_NotLogicOP_69);
    
    res_OrLogicOP_64 = (res_OrLogicOP_64 || res_AndLogicOP_65);
    
    if(res_OrLogicOP_64){
    xorIndex_res_XorLogicOP_47 = (xorIndex_res_XorLogicOP_47 + 1);
    }
    
    res_XorLogicOP_47 = (res_XorLogicOP_47 && (xorIndex_res_XorLogicOP_47 == 1));
    res_ImpliesLogicOp_42 = (res_ImpliesLogicOp_42 && res_XorLogicOP_47);
    }
    res_AndLogicOP_41 = (res_AndLogicOP_41 && res_ImpliesLogicOp_42);
    bool res_OrLogicOP_71 = false;
    res_OrLogicOP_71 = (res_OrLogicOP_71 || (Counter_GetValore(L_P1__GetSubcl126(my_id)) > 11u));
    bool res_NotLogicOP_72 = true;
    res_NotLogicOP_72 = (res_NotLogicOP_72 && ! (Counter_GetValore(L_P1__GetSubcl126(my_id)) == 130u));
    res_OrLogicOP_71 = (res_OrLogicOP_71 || res_NotLogicOP_72);
    
    res_AndLogicOP_41 = (res_AndLogicOP_41 && res_OrLogicOP_71);
    
    res_ImpliesLogicOp_40 = (res_ImpliesLogicOp_40 && res_AndLogicOP_41);
    }
    if(res_ImpliesLogicOp_40){
    xorIndex_res_XorLogicOP_39 = (xorIndex_res_XorLogicOP_39 + 1);
    }
    bool res_OrLogicOP_73 = false;
    bool res_OrLogicOP_74 = false;
    bool res_OrLogicOP_75 = false;
    bool res_NotLogicOP_76 = true;
    res_NotLogicOP_76 = (res_NotLogicOP_76 && ! (Counter_GetValore(L_P1__GetSubcl126(my_id)) > 11213u));
    res_OrLogicOP_75 = (res_OrLogicOP_75 || res_NotLogicOP_76);
    bool res_AndLogicOP_77 = true;
    res_AndLogicOP_77 = (res_AndLogicOP_77 && (L_P1__GetParamSubcl96(my_id) == false));
    res_AndLogicOP_77 = (res_AndLogicOP_77 && (L_P1__GetParamSubcl96(my_id) == false));
    
    res_OrLogicOP_75 = (res_OrLogicOP_75 || res_AndLogicOP_77);
    
    res_OrLogicOP_74 = (res_OrLogicOP_74 || res_OrLogicOP_75);
    bool res_NotLogicOP_78 = true;
    res_NotLogicOP_78 = (res_NotLogicOP_78 && ! (L_P1__GetSubcl113(my_id) == c180));
    res_OrLogicOP_74 = (res_OrLogicOP_74 || res_NotLogicOP_78);
    
    res_OrLogicOP_73 = (res_OrLogicOP_73 || res_OrLogicOP_74);
    bool res_NotLogicOP_79 = true;
    res_NotLogicOP_79 = (res_NotLogicOP_79 && ! (Counter_GetValore(L_P1__GetSubcl125(my_id)) > 13u));
    res_OrLogicOP_73 = (res_OrLogicOP_73 || res_NotLogicOP_79);
    
    if(res_OrLogicOP_73){
    xorIndex_res_XorLogicOP_39 = (xorIndex_res_XorLogicOP_39 + 1);
    }
    
    res_XorLogicOP_39 = (res_XorLogicOP_39 && (xorIndex_res_XorLogicOP_39 == 1));
    res_ImpliesLogicOp_37 = (res_ImpliesLogicOp_37 && res_XorLogicOP_39);
    }
    res_AndLogicOP_36 = (res_AndLogicOP_36 && res_ImpliesLogicOp_37);
    bool res_AndLogicOP_80 = true;
    res_AndLogicOP_80 = (res_AndLogicOP_80 && (L_P1__GetInConsd3(my_id) == false));
    res_AndLogicOP_80 = (res_AndLogicOP_80 && (Counter_GetValore(L_P1__GetSubcl125(my_id)) < 13u));
    
    res_AndLogicOP_36 = (res_AndLogicOP_36 && res_AndLogicOP_80);
    
    res_ImpliesLogicOp_31 = (res_ImpliesLogicOp_31 && res_AndLogicOP_36);
    }
    res_AndLogicOP_30 = (res_AndLogicOP_30 && res_ImpliesLogicOp_31);
    bool res_OrLogicOP_81 = false;
    bool res_OrLogicOP_82 = false;
    bool res_AndLogicOP_83 = true;
    bool res_NotLogicOP_84 = true;
    res_NotLogicOP_84 = (res_NotLogicOP_84 && ! Timer_Attivo(L_P1__GetSubcl123(my_id)));
    res_AndLogicOP_83 = (res_AndLogicOP_83 && res_NotLogicOP_84);
    bool res_NotLogicOP_85 = true;
    bool res_NotLogicOP_86 = true;
    res_NotLogicOP_86 = (res_NotLogicOP_86 && ! (L_P1__GetSubcl113(my_id) == c180));
    res_NotLogicOP_85 = (res_NotLogicOP_85 && ! res_NotLogicOP_86);
    res_AndLogicOP_83 = (res_AndLogicOP_83 && res_NotLogicOP_85);
    
    res_OrLogicOP_82 = (res_OrLogicOP_82 || res_AndLogicOP_83);
    res_OrLogicOP_82 = (res_OrLogicOP_82 || (L_P1__GetInConsd3(my_id) == false));
    
    res_OrLogicOP_81 = (res_OrLogicOP_81 || res_OrLogicOP_82);
    bool res_AndLogicOP_87 = true;
    bool res_AndLogicOP_88 = true;
    bool res_NotLogicOP_89 = true;
    res_NotLogicOP_89 = (res_NotLogicOP_89 && ! Timer_Disattivo(L_P1__GetSubcl123(my_id)));
    res_AndLogicOP_88 = (res_AndLogicOP_88 && res_NotLogicOP_89);
    res_AndLogicOP_88 = (res_AndLogicOP_88 && Timer_Attivo(L_P1__GetSubcl122(my_id)));
    
    res_AndLogicOP_87 = (res_AndLogicOP_87 && res_AndLogicOP_88);
    res_AndLogicOP_87 = (res_AndLogicOP_87 && (L_P1__GetInConsd3(my_id) == false));
    
    res_OrLogicOP_81 = (res_OrLogicOP_81 || res_AndLogicOP_87);
    
    res_AndLogicOP_30 = (res_AndLogicOP_30 && res_OrLogicOP_81);
    
    res_ImpliesLogicOp_29 = (res_ImpliesLogicOp_29 && res_AndLogicOP_30);
    }
    res_AndLogicOP_28 = (res_AndLogicOP_28 && res_ImpliesLogicOp_29);
    bool res_AndLogicOP_90 = true;
    bool res_NotLogicOP_91 = true;
    bool res_NotLogicOP_92 = true;
    res_NotLogicOP_92 = (res_NotLogicOP_92 && ! (L_P1__GetParamSubcl96(my_id) == false));
    res_NotLogicOP_91 = (res_NotLogicOP_91 && ! res_NotLogicOP_92);
    res_AndLogicOP_90 = (res_AndLogicOP_90 && res_NotLogicOP_91);
    res_AndLogicOP_90 = (res_AndLogicOP_90 && (Counter_GetValore(L_P1__GetSubcl126(my_id)) < 1213u));
    
    res_AndLogicOP_28 = (res_AndLogicOP_28 && res_AndLogicOP_90);
    
    res_ImpliesLogicOp_26 = (res_ImpliesLogicOp_26 && res_AndLogicOP_28);
    }
    res_OrLogicOP_25 = (res_OrLogicOP_25 || res_ImpliesLogicOp_26);
    bool res_OrLogicOP_93 = false;
    res_OrLogicOP_93 = (res_OrLogicOP_93 || (L_P1__GetInConsd3(my_id) == false));
    bool res_AndLogicOP_94 = true;
    bool res_NotLogicOP_95 = true;
    res_NotLogicOP_95 = (res_NotLogicOP_95 && ! (Counter_GetValore(L_P1__GetSubcl125(my_id)) == 11u));
    res_AndLogicOP_94 = (res_AndLogicOP_94 && res_NotLogicOP_95);
    res_AndLogicOP_94 = (res_AndLogicOP_94 && (L_P1__GetInConsd3(my_id) == false));
    
    res_OrLogicOP_93 = (res_OrLogicOP_93 || res_AndLogicOP_94);
    
    res_OrLogicOP_25 = (res_OrLogicOP_25 || res_OrLogicOP_93);
    
    res_ImpliesLogicOp_21 = (res_ImpliesLogicOp_21 && res_OrLogicOP_25);
    }
    res_OrLogicOP_20 = (res_OrLogicOP_20 || res_ImpliesLogicOp_21);
    bool res_AndLogicOP_96 = true;
    res_AndLogicOP_96 = (res_AndLogicOP_96 && (L_P1__GetInConsd3(my_id) == false));
    res_AndLogicOP_96 = (res_AndLogicOP_96 && (L_P1__GetInConsd3(my_id) == false));
    
    res_OrLogicOP_20 = (res_OrLogicOP_20 || res_AndLogicOP_96);
    
    res_ImpliesLogicOp_11 = (res_ImpliesLogicOp_11 && res_OrLogicOP_20);
    }
    if(res_ImpliesLogicOp_11){
    xorIndex_res_XorLogicOP_10 = (xorIndex_res_XorLogicOP_10 + 1);
    }
    bool res_OrLogicOP_97 = false;
    bool res_OrLogicOP_98 = false;
    bool res_OrLogicOP_99 = false;
    bool res_AndLogicOP_100 = true;
    bool res_NotLogicOP_101 = true;
    bool res_NotLogicOP_102 = true;
    res_NotLogicOP_102 = (res_NotLogicOP_102 && ! (L_P1__GetInSubcl92(my_id) == gialloxverd));
    res_NotLogicOP_101 = (res_NotLogicOP_101 && ! res_NotLogicOP_102);
    res_AndLogicOP_100 = (res_AndLogicOP_100 && res_NotLogicOP_101);
    res_AndLogicOP_100 = (res_AndLogicOP_100 && Timer_Scaduto(L_P1__GetSubcl124(my_id)));
    
    res_OrLogicOP_99 = (res_OrLogicOP_99 || res_AndLogicOP_100);
    res_OrLogicOP_99 = (res_OrLogicOP_99 || (L_P1__GetParamSubcl96(my_id) == false));
    
    res_OrLogicOP_98 = (res_OrLogicOP_98 || res_OrLogicOP_99);
    res_OrLogicOP_98 = (res_OrLogicOP_98 || (L_P1__GetSubcl113(my_id) == c180));
    
    res_OrLogicOP_97 = (res_OrLogicOP_97 || res_OrLogicOP_98);
    bool res_AndLogicOP_103 = true;
    bool res_NotLogicOP_104 = true;
    res_NotLogicOP_104 = (res_NotLogicOP_104 && ! Timer_Disattivo(L_P1__GetSubcl123(my_id)));
    res_AndLogicOP_103 = (res_AndLogicOP_103 && res_NotLogicOP_104);
    bool res_NotLogicOP_105 = true;
    bool res_NotLogicOP_106 = true;
    res_NotLogicOP_106 = (res_NotLogicOP_106 && ! (L_P1__GetInSubcl94(my_id) == gialloxverd));
    res_NotLogicOP_105 = (res_NotLogicOP_105 && ! res_NotLogicOP_106);
    res_AndLogicOP_103 = (res_AndLogicOP_103 && res_NotLogicOP_105);
    
    res_OrLogicOP_97 = (res_OrLogicOP_97 || res_AndLogicOP_103);
    
    if(res_OrLogicOP_97){
    xorIndex_res_XorLogicOP_10 = (xorIndex_res_XorLogicOP_10 + 1);
    }
    
    res_XorLogicOP_10 = (res_XorLogicOP_10 && (xorIndex_res_XorLogicOP_10 == 1));
    res_ImpliesLogicOp_6 = (res_ImpliesLogicOp_6 && res_XorLogicOP_10);
    }
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_ImpliesLogicOp_6);
    bool res_NotLogicOP_107 = true;
    res_NotLogicOP_107 = (res_NotLogicOP_107 && ! (L_P1__GetSubcl113(my_id) == c180));
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_NotLogicOP_107);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_OrLogicOP_5);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *47,48,50,*  *34,*  il parametro SubClass_C4_parametro_P2 sia  uguale a  False 
    //   *104,* o  che  *,*  la variabile SubClass_C4_variabile_V3 sia  diverso da c180
    //   *104,* e  che   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* e  che  *34,*  il parametro SubClass_C4_parametro_P1 sia  diverso da  True 
    //   *104,* o  che  *,*  il controllo SubClass_C4_controllo_C8 sia  uguale a GialloxVerdex
    //   *104,* e  che  *35,*  il controllo SubClass_C4_controllo_C8 non sia  diverso da GialloxVerdex
    bool res_OrLogicOP_108 = false;
    bool res_OrLogicOP_109 = false;
    res_OrLogicOP_109 = (res_OrLogicOP_109 || (L_P1__GetParamSubcl97(my_id) == false));
    bool res_AndLogicOP_110 = true;
    bool res_AndLogicOP_111 = true;
    bool res_NotLogicOP_112 = true;
    res_NotLogicOP_112 = (res_NotLogicOP_112 && ! (L_P1__GetSubcl113(my_id) == c180));
    res_AndLogicOP_111 = (res_AndLogicOP_111 && res_NotLogicOP_112);
    res_AndLogicOP_111 = (res_AndLogicOP_111 && (L_P1__GetInConsd3(my_id) == false));
    
    res_AndLogicOP_110 = (res_AndLogicOP_110 && res_AndLogicOP_111);
    bool res_NotLogicOP_113 = true;
    res_NotLogicOP_113 = (res_NotLogicOP_113 && ! (L_P1__GetParamSubcl96(my_id) == true));
    res_AndLogicOP_110 = (res_AndLogicOP_110 && res_NotLogicOP_113);
    
    res_OrLogicOP_109 = (res_OrLogicOP_109 || res_AndLogicOP_110);
    
    res_OrLogicOP_108 = (res_OrLogicOP_108 || res_OrLogicOP_109);
    bool res_AndLogicOP_114 = true;
    res_AndLogicOP_114 = (res_AndLogicOP_114 && (L_P1__GetInSubcl94(my_id) == gialloxverd));
    bool res_NotLogicOP_115 = true;
    bool res_NotLogicOP_116 = true;
    res_NotLogicOP_116 = (res_NotLogicOP_116 && ! (L_P1__GetInSubcl94(my_id) == gialloxverd));
    res_NotLogicOP_115 = (res_NotLogicOP_115 && ! res_NotLogicOP_116);
    res_AndLogicOP_114 = (res_AndLogicOP_114 && res_NotLogicOP_115);
    
    res_OrLogicOP_108 = (res_OrLogicOP_108 || res_AndLogicOP_114);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_108);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
    
    { commento: {63,} commento: {41,}  se MainClass_C1_parametro_P2 del campo  MainClass_C1 di SubClass_C4_lista_L9 esiste e  commento: {105,} è  maggiore di  commento: {54,} 4 commento: {37,} o  se la variabile SubClass_C4_variabile_V3 è  uguale a c180 commento: {35,} o  se il controllo SubClass_C4_controllo_C1 non è  diverso da  True  commento: {37,} e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180 commento: {34,} o  se il parametro SubClass_C4_parametro_P2 è  uguale a  True  commento: {37,} o  se la variabile SubClass_C4_variabile_V3 è  diverso da c180, Solo una delle seguenti { 
     commento: {61,} commento: {109,}  se il ripristino della variabile  SubClass_C4_restoreva_RV1 è  uguale a  False  commento: {35,} e  se il controllo SubClass_C4_controllo_C1 non è  uguale a  True , Tutte le seguenti { 
     commento: {61,} commento: {41,}  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C4_lista_L9 è  diverso da c270 commento: {34,} o  se il parametro SubClass_C4_parametro_P9 non è  uguale a  commento: {53,} 6 commento: {36,} e  se il timer SubClass_C4_timer_T3 non è attivo commento: {35,} e  se il controllo SubClass_C4_controllo_C3 è  uguale a GialloxVerdex e  se l'argomento argomento_ave7 è  diverso da RossoGialloVerde commento: {39,} , Tutte le seguenti { 
     commento: {63,}  se la macro  SubClass_C4_macrova_M6 ( con argomento_a6   uguale a True ,argomento_a1   uguale a c270 ,argomento_a3   uguale a RossoGialloVerde  e argomento_a2   uguale a c270 )  non  è  uguale a RossoGialloVerde commento: {40,}  commento: {38,} o  se il contatore SubClass_C4_contatore_Co5 è  uguale a  commento: {53,} 134 commento: {36,} o  se il timer SubClass_C4_timer_T2 è scaduto commento: {37,} e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180, Solo una delle seguenti { 
     commento: {61,} commento: {43,}  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C4_lista_L9 è attivo commento: {34,} e  se il parametro SubClass_C4_parametro_P2 è  diverso da  False  commento: {36,} o  se il timer SubClass_C4_timer_T2 non è scaduto commento: {34,} o  se il parametro SubClass_C4_parametro_P9 è  maggiore di  commento: {54,} 3, Tutte le seguenti { 
     commento: {63,} commento: {43,}  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C4_lista_L9 esiste e  commento: {105,} è attivo commento: {35,} e  se il controllo SubClass_C4_controllo_C7 è  uguale a  False  commento: {37,} e  se la variabile SubClass_C4_variabile_V3 non è  diverso da c180, Solo una delle seguenti { 
     commento: {62,} commento: {110,}  se il ripristino del timer  SubClass_C4_restoreTI_TI1 è attivo, Almeno una delle seguenti { 
     commento: {62,} commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C4_lista_L9 esiste e  commento: {105,} è  diverso da  commento: {56,}  state1  commento: {36,} o  se il timer SubClass_C4_timer_T3 è scaduto commento: {34,} e  se il parametro SubClass_C4_parametro_P9 è  uguale a  commento: {53,} 6, Almeno una delle seguenti { 
     commento: {36,}  se il timer SubClass_C4_timer_T2 è scaduto commento: {34,} e  se il parametro SubClass_C4_parametro_P1 non è  diverso da  False , Verifica che   commento: {47,48,50,}  commento: {,}  il controllo SubClass_C4_controllo_C8 sia  uguale a GialloxVerdex
     commento: {104,} o  che  commento: {,}  la variabile SubClass_C4_variabile_V3 sia  diverso da c180
     commento: {104,} e  che  commento: {37,}  la variabile SubClass_C4_variabile_V3 sia  uguale a c180
     commento: {104,} e  che  commento: {34,}  il parametro SubClass_C4_parametro_P1 sia  uguale a  True 
    
    
     } Verifica che   commento: {47,48,50,51,52,}   l'argomento argomento_ave9 non  sia  diverso da  False  commento: {,} 
     commento: {104,} e  che  commento: {,}  il contatore SubClass_C4_contatore_Co5 non sia  uguale a  commento: {53,} 11
     commento: {104,} o  che  commento: {,}  il controllo SubClass_C4_controllo_C7 sia  uguale a  False 
     commento: {104,} o  che  commento: {34,}  il parametro SubClass_C4_parametro_P2 sia  diverso da  False 
     commento: {104,} e  che  commento: {,}  la variabile SubClass_C4_variabile_V3 non sia  uguale a c180
     commento: {104,} o  che  commento: {35,}  il controllo SubClass_C4_controllo_C8 non sia  uguale a GialloxVerdex
    
    
     } Verifica che   commento: {47,51,52,}  commento: {,}  il contatore SubClass_C4_contatore_Co5 sia  minore di  commento: {55,} 11
     commento: {104,} e  che   l'argomento argomento_ave9 sia  diverso da  True  commento: {,} 
     commento: {104,} e  che   l'argomento argomento_ave4 non  sia  uguale a  True  commento: {39,} 
     commento: {104,} o  che  commento: {34,}  il parametro SubClass_C4_parametro_P9 sia  minore di  commento: {55,} 3
    
    
     } Verifica che   commento: {47,}  commento: {34,}  il parametro SubClass_C4_parametro_P9 non sia  diverso da  commento: {56,} 2
    
    
     } Verifica che   commento: {47,52,}  commento: {34,}  il parametro SubClass_C4_parametro_P2 sia  diverso da  True 
     commento: {104,} o  che   l'argomento argomento_ave4 non  sia  diverso da  True  commento: {,} 
    
    
     } Verifica che   commento: {47,49,51,}  commento: {34,}  il parametro SubClass_C4_parametro_P9 non sia  diverso da  commento: {56,} 2
     commento: {104,} e  che  commento: {,}  il timer SubClass_C4_timer_T3 non sia attivo
     commento: {104,} e  che  commento: {,}  il contatore SubClass_C4_contatore_Co5 non sia  maggiore di  commento: {54,} 134
    
    
     } Verifica che   commento: {50,51,52,}   l'argomento argomento_ave9 non  sia  diverso da  True  commento: {,} 
     commento: {104,} e  che  commento: {,}  il contatore SubClass_C4_contatore_Co5 non sia  maggiore di  commento: {54,} 12502
     commento: {104,} e  che   l'argomento argomento_ave8 non  sia  uguale a  True  commento: {39,} 
     commento: {104,} o  che  commento: {38,}  il contatore SubClass_C4_contatore_Co8 sia  minore di  commento: {55,} 1513
     commento: {104,} o  che  commento: {38,}  il contatore SubClass_C4_contatore_Co8 sia  diverso da  commento: {56,} 114
     commento: {104,} o  che  commento: {,}  la variabile SubClass_C4_variabile_V3 non sia  uguale a c180
    
    
     } Verifica che   commento: {48,49,51,52,}   l'argomento argomento_ave4 sia  uguale a  False  commento: {,} 
     commento: {104,} e  che   l'argomento argomento_ave8 sia  uguale a  True  commento: {39,} 
     commento: {104,} o  che  commento: {,}  il timer SubClass_C4_timer_T3 sia disattivo
     commento: {104,} e  che  commento: {36,}  il timer SubClass_C4_timer_T2 non sia scaduto
     commento: {104,} o  che  commento: {,}  il contatore SubClass_C4_contatore_Co5 sia  uguale a  commento: {53,} 155
     commento: {104,} o  che  commento: {,}  il controllo SubClass_C4_controllo_C7 sia  uguale a  False 
    
    
     } Verifica che   commento: {48,51,}  commento: {,}  il controllo SubClass_C4_controllo_C8 non sia  uguale a GialloxVerdex
     commento: {104,} e  che  commento: {,}  il contatore SubClass_C4_contatore_Co8 non sia  minore di  commento: {55,} 1102
    
    
    }
*/
bool L_P1__Macro38(instance_id_t const my_id , bool argom108, C4_Enumerat2 argom109, bool argom110, bool argom111)
{
bool res_AndLogicOP_0 = true;
    
    //  *63,* *41,*  se MainClass_C1_parametro_P2 del campo  MainClass_C1 di SubClass_C4_lista_L9 esiste e  *105,* è  maggiore di  *54,* 4 *37,* o  se la variabile SubClass_C4_variabile_V3 è  uguale a c180 *35,* o  se il controllo SubClass_C4_controllo_C1 non è  diverso da  True  *37,* e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180 *34,* o  se il parametro SubClass_C4_parametro_P2 è  uguale a  True  *37,* o  se la variabile SubClass_C4_variabile_V3 è  diverso da c180, Solo una delle seguenti { 
    //   *61,* *109,*  se il ripristino della variabile  SubClass_C4_restoreva_RV1 è  uguale a  False  *35,* e  se il controllo SubClass_C4_controllo_C1 non è  uguale a  True , Tutte le seguenti { 
    //   *61,* *41,*  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C4_lista_L9 è  diverso da c270 *34,* o  se il parametro SubClass_C4_parametro_P9 non è  uguale a  *53,* 6 *36,* e  se il timer SubClass_C4_timer_T3 non è attivo *35,* e  se il controllo SubClass_C4_controllo_C3 è  uguale a GialloxVerdex e  se l'argomento argomento_ave7 è  diverso da RossoGialloVerde *39,* , Tutte le seguenti { 
    //   *63,*  se la macro  SubClass_C4_macrova_M6 ( con argomento_a6   uguale a True ,argomento_a1   uguale a c270 ,argomento_a3   uguale a RossoGialloVerde  e argomento_a2   uguale a c270 )  non  è  uguale a RossoGialloVerde *40,*  *38,* o  se il contatore SubClass_C4_contatore_Co5 è  uguale a  *53,* 134 *36,* o  se il timer SubClass_C4_timer_T2 è scaduto *37,* e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180, Solo una delle seguenti { 
    //   *61,* *43,*  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C4_lista_L9 è attivo *34,* e  se il parametro SubClass_C4_parametro_P2 è  diverso da  False  *36,* o  se il timer SubClass_C4_timer_T2 non è scaduto *34,* o  se il parametro SubClass_C4_parametro_P9 è  maggiore di  *54,* 3, Tutte le seguenti { 
    //   *63,* *43,*  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C4_lista_L9 esiste e  *105,* è attivo *35,* e  se il controllo SubClass_C4_controllo_C7 è  uguale a  False  *37,* e  se la variabile SubClass_C4_variabile_V3 non è  diverso da c180, Solo una delle seguenti { 
    //   *62,* *110,*  se il ripristino del timer  SubClass_C4_restoreTI_TI1 è attivo, Almeno una delle seguenti { 
    //   *62,* *111,*  se lo stato del campo  MainClass_C1 di SubClass_C4_lista_L9 esiste e  *105,* è  diverso da  *56,*  state1  *36,* o  se il timer SubClass_C4_timer_T3 è scaduto *34,* e  se il parametro SubClass_C4_parametro_P9 è  uguale a  *53,* 6, Almeno una delle seguenti { 
    //   *36,*  se il timer SubClass_C4_timer_T2 è scaduto *34,* e  se il parametro SubClass_C4_parametro_P1 non è  diverso da  False , Verifica che   *47,48,50,*  *,*  il controllo SubClass_C4_controllo_C8 sia  uguale a GialloxVerdex
    //   *104,* o  che  *,*  la variabile SubClass_C4_variabile_V3 sia  diverso da c180
    //   *104,* e  che  *37,*  la variabile SubClass_C4_variabile_V3 sia  uguale a c180
    //   *104,* e  che  *34,*  il parametro SubClass_C4_parametro_P1 sia  uguale a  True 
    //   } Verifica che   *47,48,50,51,52,*   l'argomento argomento_ave9 non  sia  diverso da  False  *,* 
    //   *104,* e  che  *,*  il contatore SubClass_C4_contatore_Co5 non sia  uguale a  *53,* 11
    //   *104,* o  che  *,*  il controllo SubClass_C4_controllo_C7 sia  uguale a  False 
    //   *104,* o  che  *34,*  il parametro SubClass_C4_parametro_P2 sia  diverso da  False 
    //   *104,* e  che  *,*  la variabile SubClass_C4_variabile_V3 non sia  uguale a c180
    //   *104,* o  che  *35,*  il controllo SubClass_C4_controllo_C8 non sia  uguale a GialloxVerdex
    //   } Verifica che   *47,51,52,*  *,*  il contatore SubClass_C4_contatore_Co5 sia  minore di  *55,* 11
    //   *104,* e  che   l'argomento argomento_ave9 sia  diverso da  True  *,* 
    //   *104,* e  che   l'argomento argomento_ave4 non  sia  uguale a  True  *39,* 
    //   *104,* o  che  *34,*  il parametro SubClass_C4_parametro_P9 sia  minore di  *55,* 3
    //   } Verifica che   *47,*  *34,*  il parametro SubClass_C4_parametro_P9 non sia  diverso da  *56,* 2
    //   } Verifica che   *47,52,*  *34,*  il parametro SubClass_C4_parametro_P2 sia  diverso da  True 
    //   *104,* o  che   l'argomento argomento_ave4 non  sia  diverso da  True  *,* 
    //   } Verifica che   *47,49,51,*  *34,*  il parametro SubClass_C4_parametro_P9 non sia  diverso da  *56,* 2
    //   *104,* e  che  *,*  il timer SubClass_C4_timer_T3 non sia attivo
    //   *104,* e  che  *,*  il contatore SubClass_C4_contatore_Co5 non sia  maggiore di  *54,* 134
    //   } Verifica che   *50,51,52,*   l'argomento argomento_ave9 non  sia  diverso da  True  *,* 
    //   *104,* e  che  *,*  il contatore SubClass_C4_contatore_Co5 non sia  maggiore di  *54,* 12502
    //   *104,* e  che   l'argomento argomento_ave8 non  sia  uguale a  True  *39,* 
    //   *104,* o  che  *38,*  il contatore SubClass_C4_contatore_Co8 sia  minore di  *55,* 1513
    //   *104,* o  che  *38,*  il contatore SubClass_C4_contatore_Co8 sia  diverso da  *56,* 114
    //   *104,* o  che  *,*  la variabile SubClass_C4_variabile_V3 non sia  uguale a c180
    //   } Verifica che   *48,49,51,52,*   l'argomento argomento_ave4 sia  uguale a  False  *,* 
    //   *104,* e  che   l'argomento argomento_ave8 sia  uguale a  True  *39,* 
    //   *104,* o  che  *,*  il timer SubClass_C4_timer_T3 sia disattivo
    //   *104,* e  che  *36,*  il timer SubClass_C4_timer_T2 non sia scaduto
    //   *104,* o  che  *,*  il contatore SubClass_C4_contatore_Co5 sia  uguale a  *53,* 155
    //   *104,* o  che  *,*  il controllo SubClass_C4_controllo_C7 sia  uguale a  False 
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_OrLogicOP_4 = false;
    bool res_OrLogicOP_5 = false;
    bool res_ForAllPredicateNotEmpty_6 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl95Length(my_id); ++i)
    {
    L_P1__Recor3 it = L_P1__GetRecSubcl95(my_id,i);
    bool res_ImpliesLogicOp_7 = true;
    res_ImpliesLogicOp_7 = (res_ImpliesLogicOp_7 && (L_P1__GetParamMainc6(it.mainc48) > 4u));
    res_ForAllPredicateNotEmpty_6 = res_ImpliesLogicOp_7;
    if(!res_ForAllPredicateNotEmpty_6) {break;}
    }
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_ForAllPredicateNotEmpty_6);
    res_OrLogicOP_5 = (res_OrLogicOP_5 || (L_P1__GetSubcl113(my_id) == c180));
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_OrLogicOP_5);
    bool res_AndLogicOP_8 = true;
    bool res_NotLogicOP_9 = true;
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__GetInSubcl91(my_id) == true));
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! res_NotLogicOP_10);
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_9);
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (L_P1__GetSubcl113(my_id) == c180));
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_11);
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_AndLogicOP_8);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_OrLogicOP_4);
    res_OrLogicOP_3 = (res_OrLogicOP_3 || (L_P1__GetParamSubcl97(my_id) == true));
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (L_P1__GetSubcl113(my_id) == c180));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_12);
    
    if(res_OrLogicOP_2){
    bool res_XorLogicOP_13 = true;
    int xorIndex_res_XorLogicOP_13 = 0;
    bool res_ImpliesLogicOp_14 = true;
    bool res_AndLogicOP_15 = true;
    res_AndLogicOP_15 = (res_AndLogicOP_15 && (L_P1__GetSubcl112(my_id) == false));
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (L_P1__GetInSubcl91(my_id) == true));
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_NotLogicOP_16);
    
    if(res_AndLogicOP_15){
    bool res_AndLogicOP_17 = true;
    bool res_ImpliesLogicOp_18 = true;
    bool res_OrLogicOP_19 = false;
    bool res_ForAllPredicate_20 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl95Length(my_id); ++i)
    {
    L_P1__Recor3 it = L_P1__GetRecSubcl95(my_id,i);
    bool res_ImpliesLogicOp_21 = true;
    bool res_NotLogicOP_22 = true;
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! (L_P1__GetParamMainc5(it.mainc48) == c270));
    res_ImpliesLogicOp_21 = (res_ImpliesLogicOp_21 && res_NotLogicOP_22);
    res_ForAllPredicate_20 = res_ImpliesLogicOp_21;
    if(!res_ForAllPredicate_20) {break;}
    }
    res_OrLogicOP_19 = (res_OrLogicOP_19 || res_ForAllPredicate_20);
    bool res_AndLogicOP_23 = true;
    bool res_AndLogicOP_24 = true;
    bool res_AndLogicOP_25 = true;
    bool res_NotLogicOP_26 = true;
    res_NotLogicOP_26 = (res_NotLogicOP_26 && ! (L_P1__GetParamSubcl98(my_id) == 6u));
    res_AndLogicOP_25 = (res_AndLogicOP_25 && res_NotLogicOP_26);
    bool res_NotLogicOP_27 = true;
    res_NotLogicOP_27 = (res_NotLogicOP_27 && ! Timer_Attivo(L_P1__GetSubcl123(my_id)));
    res_AndLogicOP_25 = (res_AndLogicOP_25 && res_NotLogicOP_27);
    
    res_AndLogicOP_24 = (res_AndLogicOP_24 && res_AndLogicOP_25);
    res_AndLogicOP_24 = (res_AndLogicOP_24 && (L_P1__GetInSubcl92(my_id) == gialloxverd));
    
    res_AndLogicOP_23 = (res_AndLogicOP_23 && res_AndLogicOP_24);
    bool res_NotLogicOP_28 = true;
    res_NotLogicOP_28 = (res_NotLogicOP_28 && ! (argom109 == rossogiallo1));
    res_AndLogicOP_23 = (res_AndLogicOP_23 && res_NotLogicOP_28);
    
    res_OrLogicOP_19 = (res_OrLogicOP_19 || res_AndLogicOP_23);
    
    if(res_OrLogicOP_19){
    bool res_AndLogicOP_29 = true;
    bool res_ImpliesLogicOp_30 = true;
    bool res_OrLogicOP_31 = false;
    bool res_OrLogicOP_32 = false;
    bool res_NotLogicOP_33 = true;
    res_NotLogicOP_33 = (res_NotLogicOP_33 && ! (L_P1__Macro33(my_id,c270,c270,rossogiallo1,true) == rossogiallo1));
    res_OrLogicOP_32 = (res_OrLogicOP_32 || res_NotLogicOP_33);
    res_OrLogicOP_32 = (res_OrLogicOP_32 || (Counter_GetValore(L_P1__GetSubcl125(my_id)) == 134u));
    
    res_OrLogicOP_31 = (res_OrLogicOP_31 || res_OrLogicOP_32);
    bool res_AndLogicOP_34 = true;
    res_AndLogicOP_34 = (res_AndLogicOP_34 && Timer_Scaduto(L_P1__GetSubcl122(my_id)));
    bool res_NotLogicOP_35 = true;
    res_NotLogicOP_35 = (res_NotLogicOP_35 && ! (L_P1__GetSubcl113(my_id) == c180));
    res_AndLogicOP_34 = (res_AndLogicOP_34 && res_NotLogicOP_35);
    
    res_OrLogicOP_31 = (res_OrLogicOP_31 || res_AndLogicOP_34);
    
    if(res_OrLogicOP_31){
    bool res_XorLogicOP_36 = true;
    int xorIndex_res_XorLogicOP_36 = 0;
    bool res_ImpliesLogicOp_37 = true;
    bool res_OrLogicOP_38 = false;
    bool res_OrLogicOP_39 = false;
    bool res_AndLogicOP_40 = true;
    bool res_ForAllPredicate_41 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl95Length(my_id); ++i)
    {
    L_P1__Recor3 it = L_P1__GetRecSubcl95(my_id,i);
    bool res_ImpliesLogicOp_42 = true;
    res_ImpliesLogicOp_42 = (res_ImpliesLogicOp_42 && Timer_Attivo(L_P1__GetMainc42(it.mainc48)));
    res_ForAllPredicate_41 = res_ImpliesLogicOp_42;
    if(!res_ForAllPredicate_41) {break;}
    }
    res_AndLogicOP_40 = (res_AndLogicOP_40 && res_ForAllPredicate_41);
    bool res_NotLogicOP_43 = true;
    res_NotLogicOP_43 = (res_NotLogicOP_43 && ! (L_P1__GetParamSubcl97(my_id) == false));
    res_AndLogicOP_40 = (res_AndLogicOP_40 && res_NotLogicOP_43);
    
    res_OrLogicOP_39 = (res_OrLogicOP_39 || res_AndLogicOP_40);
    bool res_NotLogicOP_44 = true;
    res_NotLogicOP_44 = (res_NotLogicOP_44 && ! Timer_Scaduto(L_P1__GetSubcl122(my_id)));
    res_OrLogicOP_39 = (res_OrLogicOP_39 || res_NotLogicOP_44);
    
    res_OrLogicOP_38 = (res_OrLogicOP_38 || res_OrLogicOP_39);
    res_OrLogicOP_38 = (res_OrLogicOP_38 || (L_P1__GetParamSubcl98(my_id) > 3u));
    
    if(res_OrLogicOP_38){
    bool res_AndLogicOP_45 = true;
    bool res_ImpliesLogicOp_46 = true;
    bool res_AndLogicOP_47 = true;
    bool res_AndLogicOP_48 = true;
    bool res_ForAllPredicateNotEmpty_49 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl95Length(my_id); ++i)
    {
    L_P1__Recor3 it = L_P1__GetRecSubcl95(my_id,i);
    bool res_ImpliesLogicOp_50 = true;
    res_ImpliesLogicOp_50 = (res_ImpliesLogicOp_50 && Timer_Attivo(L_P1__GetMainc42(it.mainc48)));
    res_ForAllPredicateNotEmpty_49 = res_ImpliesLogicOp_50;
    if(!res_ForAllPredicateNotEmpty_49) {break;}
    }
    res_AndLogicOP_48 = (res_AndLogicOP_48 && res_ForAllPredicateNotEmpty_49);
    res_AndLogicOP_48 = (res_AndLogicOP_48 && (L_P1__GetInSubcl93(my_id) == false));
    
    res_AndLogicOP_47 = (res_AndLogicOP_47 && res_AndLogicOP_48);
    bool res_NotLogicOP_51 = true;
    bool res_NotLogicOP_52 = true;
    res_NotLogicOP_52 = (res_NotLogicOP_52 && ! (L_P1__GetSubcl113(my_id) == c180));
    res_NotLogicOP_51 = (res_NotLogicOP_51 && ! res_NotLogicOP_52);
    res_AndLogicOP_47 = (res_AndLogicOP_47 && res_NotLogicOP_51);
    
    if(res_AndLogicOP_47){
    bool res_XorLogicOP_53 = true;
    int xorIndex_res_XorLogicOP_53 = 0;
    bool res_ImpliesLogicOp_54 = true;
    if(Timer_Attivo(L_P1__GetSubcl115(my_id))){
    bool res_OrLogicOP_55 = false;
    bool res_ImpliesLogicOp_56 = true;
    bool res_OrLogicOP_57 = false;
    bool res_ForAllPredicateNotEmpty_58 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl95Length(my_id); ++i)
    {
    L_P1__Recor3 it = L_P1__GetRecSubcl95(my_id,i);
    bool res_ImpliesLogicOp_59 = true;
    bool res_NotLogicOP_60 = true;
    res_NotLogicOP_60 = (res_NotLogicOP_60 && ! (L_P1_C1_GetState(it.mainc48) == C1_St_state));
    res_ImpliesLogicOp_59 = (res_ImpliesLogicOp_59 && res_NotLogicOP_60);
    res_ForAllPredicateNotEmpty_58 = res_ImpliesLogicOp_59;
    if(!res_ForAllPredicateNotEmpty_58) {break;}
    }
    res_OrLogicOP_57 = (res_OrLogicOP_57 || res_ForAllPredicateNotEmpty_58);
    bool res_AndLogicOP_61 = true;
    res_AndLogicOP_61 = (res_AndLogicOP_61 && Timer_Scaduto(L_P1__GetSubcl123(my_id)));
    res_AndLogicOP_61 = (res_AndLogicOP_61 && (L_P1__GetParamSubcl98(my_id) == 6u));
    
    res_OrLogicOP_57 = (res_OrLogicOP_57 || res_AndLogicOP_61);
    
    if(res_OrLogicOP_57){
    bool res_ImpliesLogicOp_62 = true;
    bool res_AndLogicOP_63 = true;
    res_AndLogicOP_63 = (res_AndLogicOP_63 && Timer_Scaduto(L_P1__GetSubcl122(my_id)));
    bool res_NotLogicOP_64 = true;
    bool res_NotLogicOP_65 = true;
    res_NotLogicOP_65 = (res_NotLogicOP_65 && ! (L_P1__GetParamSubcl96(my_id) == false));
    res_NotLogicOP_64 = (res_NotLogicOP_64 && ! res_NotLogicOP_65);
    res_AndLogicOP_63 = (res_AndLogicOP_63 && res_NotLogicOP_64);
    
    if(res_AndLogicOP_63){
    bool res_OrLogicOP_66 = false;
    res_OrLogicOP_66 = (res_OrLogicOP_66 || (L_P1__GetInSubcl94(my_id) == gialloxverd));
    bool res_AndLogicOP_67 = true;
    bool res_AndLogicOP_68 = true;
    bool res_NotLogicOP_69 = true;
    res_NotLogicOP_69 = (res_NotLogicOP_69 && ! (L_P1__GetSubcl113(my_id) == c180));
    res_AndLogicOP_68 = (res_AndLogicOP_68 && res_NotLogicOP_69);
    res_AndLogicOP_68 = (res_AndLogicOP_68 && (L_P1__GetSubcl113(my_id) == c180));
    
    res_AndLogicOP_67 = (res_AndLogicOP_67 && res_AndLogicOP_68);
    res_AndLogicOP_67 = (res_AndLogicOP_67 && (L_P1__GetParamSubcl96(my_id) == true));
    
    res_OrLogicOP_66 = (res_OrLogicOP_66 || res_AndLogicOP_67);
    
    res_ImpliesLogicOp_62 = (res_ImpliesLogicOp_62 && res_OrLogicOP_66);
    }
    res_ImpliesLogicOp_56 = (res_ImpliesLogicOp_56 && res_ImpliesLogicOp_62);
    }
    res_OrLogicOP_55 = (res_OrLogicOP_55 || res_ImpliesLogicOp_56);
    bool res_OrLogicOP_70 = false;
    bool res_OrLogicOP_71 = false;
    bool res_OrLogicOP_72 = false;
    bool res_AndLogicOP_73 = true;
    bool res_NotLogicOP_74 = true;
    bool res_NotLogicOP_75 = true;
    res_NotLogicOP_75 = (res_NotLogicOP_75 && ! (argom111 == false));
    res_NotLogicOP_74 = (res_NotLogicOP_74 && ! res_NotLogicOP_75);
    res_AndLogicOP_73 = (res_AndLogicOP_73 && res_NotLogicOP_74);
    bool res_NotLogicOP_76 = true;
    res_NotLogicOP_76 = (res_NotLogicOP_76 && ! (Counter_GetValore(L_P1__GetSubcl125(my_id)) == 11u));
    res_AndLogicOP_73 = (res_AndLogicOP_73 && res_NotLogicOP_76);
    
    res_OrLogicOP_72 = (res_OrLogicOP_72 || res_AndLogicOP_73);
    res_OrLogicOP_72 = (res_OrLogicOP_72 || (L_P1__GetInSubcl93(my_id) == false));
    
    res_OrLogicOP_71 = (res_OrLogicOP_71 || res_OrLogicOP_72);
    bool res_AndLogicOP_77 = true;
    bool res_NotLogicOP_78 = true;
    res_NotLogicOP_78 = (res_NotLogicOP_78 && ! (L_P1__GetParamSubcl97(my_id) == false));
    res_AndLogicOP_77 = (res_AndLogicOP_77 && res_NotLogicOP_78);
    bool res_NotLogicOP_79 = true;
    res_NotLogicOP_79 = (res_NotLogicOP_79 && ! (L_P1__GetSubcl113(my_id) == c180));
    res_AndLogicOP_77 = (res_AndLogicOP_77 && res_NotLogicOP_79);
    
    res_OrLogicOP_71 = (res_OrLogicOP_71 || res_AndLogicOP_77);
    
    res_OrLogicOP_70 = (res_OrLogicOP_70 || res_OrLogicOP_71);
    bool res_NotLogicOP_80 = true;
    res_NotLogicOP_80 = (res_NotLogicOP_80 && ! (L_P1__GetInSubcl94(my_id) == gialloxverd));
    res_OrLogicOP_70 = (res_OrLogicOP_70 || res_NotLogicOP_80);
    
    res_OrLogicOP_55 = (res_OrLogicOP_55 || res_OrLogicOP_70);
    
    res_ImpliesLogicOp_54 = (res_ImpliesLogicOp_54 && res_OrLogicOP_55);
    }
    if(res_ImpliesLogicOp_54){
    xorIndex_res_XorLogicOP_53 = (xorIndex_res_XorLogicOP_53 + 1);
    }
    bool res_OrLogicOP_81 = false;
    bool res_AndLogicOP_82 = true;
    bool res_AndLogicOP_83 = true;
    res_AndLogicOP_83 = (res_AndLogicOP_83 && (Counter_GetValore(L_P1__GetSubcl125(my_id)) < 11u));
    bool res_NotLogicOP_84 = true;
    res_NotLogicOP_84 = (res_NotLogicOP_84 && ! (argom111 == true));
    res_AndLogicOP_83 = (res_AndLogicOP_83 && res_NotLogicOP_84);
    
    res_AndLogicOP_82 = (res_AndLogicOP_82 && res_AndLogicOP_83);
    bool res_NotLogicOP_85 = true;
    res_NotLogicOP_85 = (res_NotLogicOP_85 && ! (argom108 == true));
    res_AndLogicOP_82 = (res_AndLogicOP_82 && res_NotLogicOP_85);
    
    res_OrLogicOP_81 = (res_OrLogicOP_81 || res_AndLogicOP_82);
    res_OrLogicOP_81 = (res_OrLogicOP_81 || (L_P1__GetParamSubcl98(my_id) < 3u));
    
    if(res_OrLogicOP_81){
    xorIndex_res_XorLogicOP_53 = (xorIndex_res_XorLogicOP_53 + 1);
    }
    
    res_XorLogicOP_53 = (res_XorLogicOP_53 && (xorIndex_res_XorLogicOP_53 == 1));
    res_ImpliesLogicOp_46 = (res_ImpliesLogicOp_46 && res_XorLogicOP_53);
    }
    res_AndLogicOP_45 = (res_AndLogicOP_45 && res_ImpliesLogicOp_46);
    bool res_NotLogicOP_86 = true;
    bool res_NotLogicOP_87 = true;
    res_NotLogicOP_87 = (res_NotLogicOP_87 && ! (L_P1__GetParamSubcl98(my_id) == 2u));
    res_NotLogicOP_86 = (res_NotLogicOP_86 && ! res_NotLogicOP_87);
    res_AndLogicOP_45 = (res_AndLogicOP_45 && res_NotLogicOP_86);
    
    res_ImpliesLogicOp_37 = (res_ImpliesLogicOp_37 && res_AndLogicOP_45);
    }
    if(res_ImpliesLogicOp_37){
    xorIndex_res_XorLogicOP_36 = (xorIndex_res_XorLogicOP_36 + 1);
    }
    bool res_OrLogicOP_88 = false;
    bool res_NotLogicOP_89 = true;
    res_NotLogicOP_89 = (res_NotLogicOP_89 && ! (L_P1__GetParamSubcl97(my_id) == true));
    res_OrLogicOP_88 = (res_OrLogicOP_88 || res_NotLogicOP_89);
    bool res_NotLogicOP_90 = true;
    bool res_NotLogicOP_91 = true;
    res_NotLogicOP_91 = (res_NotLogicOP_91 && ! (argom108 == true));
    res_NotLogicOP_90 = (res_NotLogicOP_90 && ! res_NotLogicOP_91);
    res_OrLogicOP_88 = (res_OrLogicOP_88 || res_NotLogicOP_90);
    
    if(res_OrLogicOP_88){
    xorIndex_res_XorLogicOP_36 = (xorIndex_res_XorLogicOP_36 + 1);
    }
    
    res_XorLogicOP_36 = (res_XorLogicOP_36 && (xorIndex_res_XorLogicOP_36 == 1));
    res_ImpliesLogicOp_30 = (res_ImpliesLogicOp_30 && res_XorLogicOP_36);
    }
    res_AndLogicOP_29 = (res_AndLogicOP_29 && res_ImpliesLogicOp_30);
    bool res_AndLogicOP_92 = true;
    bool res_AndLogicOP_93 = true;
    bool res_NotLogicOP_94 = true;
    bool res_NotLogicOP_95 = true;
    res_NotLogicOP_95 = (res_NotLogicOP_95 && ! (L_P1__GetParamSubcl98(my_id) == 2u));
    res_NotLogicOP_94 = (res_NotLogicOP_94 && ! res_NotLogicOP_95);
    res_AndLogicOP_93 = (res_AndLogicOP_93 && res_NotLogicOP_94);
    bool res_NotLogicOP_96 = true;
    res_NotLogicOP_96 = (res_NotLogicOP_96 && ! Timer_Attivo(L_P1__GetSubcl123(my_id)));
    res_AndLogicOP_93 = (res_AndLogicOP_93 && res_NotLogicOP_96);
    
    res_AndLogicOP_92 = (res_AndLogicOP_92 && res_AndLogicOP_93);
    bool res_NotLogicOP_97 = true;
    res_NotLogicOP_97 = (res_NotLogicOP_97 && ! (Counter_GetValore(L_P1__GetSubcl125(my_id)) > 134u));
    res_AndLogicOP_92 = (res_AndLogicOP_92 && res_NotLogicOP_97);
    
    res_AndLogicOP_29 = (res_AndLogicOP_29 && res_AndLogicOP_92);
    
    res_ImpliesLogicOp_18 = (res_ImpliesLogicOp_18 && res_AndLogicOP_29);
    }
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_ImpliesLogicOp_18);
    bool res_OrLogicOP_98 = false;
    bool res_OrLogicOP_99 = false;
    bool res_OrLogicOP_100 = false;
    bool res_AndLogicOP_101 = true;
    bool res_AndLogicOP_102 = true;
    bool res_NotLogicOP_103 = true;
    bool res_NotLogicOP_104 = true;
    res_NotLogicOP_104 = (res_NotLogicOP_104 && ! (argom111 == true));
    res_NotLogicOP_103 = (res_NotLogicOP_103 && ! res_NotLogicOP_104);
    res_AndLogicOP_102 = (res_AndLogicOP_102 && res_NotLogicOP_103);
    bool res_NotLogicOP_105 = true;
    res_NotLogicOP_105 = (res_NotLogicOP_105 && ! (Counter_GetValore(L_P1__GetSubcl125(my_id)) > 12502u));
    res_AndLogicOP_102 = (res_AndLogicOP_102 && res_NotLogicOP_105);
    
    res_AndLogicOP_101 = (res_AndLogicOP_101 && res_AndLogicOP_102);
    bool res_NotLogicOP_106 = true;
    res_NotLogicOP_106 = (res_NotLogicOP_106 && ! (argom110 == true));
    res_AndLogicOP_101 = (res_AndLogicOP_101 && res_NotLogicOP_106);
    
    res_OrLogicOP_100 = (res_OrLogicOP_100 || res_AndLogicOP_101);
    res_OrLogicOP_100 = (res_OrLogicOP_100 || (Counter_GetValore(L_P1__GetSubcl126(my_id)) < 1513u));
    
    res_OrLogicOP_99 = (res_OrLogicOP_99 || res_OrLogicOP_100);
    bool res_NotLogicOP_107 = true;
    res_NotLogicOP_107 = (res_NotLogicOP_107 && ! (Counter_GetValore(L_P1__GetSubcl126(my_id)) == 114u));
    res_OrLogicOP_99 = (res_OrLogicOP_99 || res_NotLogicOP_107);
    
    res_OrLogicOP_98 = (res_OrLogicOP_98 || res_OrLogicOP_99);
    bool res_NotLogicOP_108 = true;
    res_NotLogicOP_108 = (res_NotLogicOP_108 && ! (L_P1__GetSubcl113(my_id) == c180));
    res_OrLogicOP_98 = (res_OrLogicOP_98 || res_NotLogicOP_108);
    
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_OrLogicOP_98);
    
    res_ImpliesLogicOp_14 = (res_ImpliesLogicOp_14 && res_AndLogicOP_17);
    }
    if(res_ImpliesLogicOp_14){
    xorIndex_res_XorLogicOP_13 = (xorIndex_res_XorLogicOP_13 + 1);
    }
    bool res_OrLogicOP_109 = false;
    bool res_OrLogicOP_110 = false;
    bool res_OrLogicOP_111 = false;
    bool res_AndLogicOP_112 = true;
    res_AndLogicOP_112 = (res_AndLogicOP_112 && (argom108 == false));
    res_AndLogicOP_112 = (res_AndLogicOP_112 && (argom110 == true));
    
    res_OrLogicOP_111 = (res_OrLogicOP_111 || res_AndLogicOP_112);
    bool res_AndLogicOP_113 = true;
    res_AndLogicOP_113 = (res_AndLogicOP_113 && Timer_Disattivo(L_P1__GetSubcl123(my_id)));
    bool res_NotLogicOP_114 = true;
    res_NotLogicOP_114 = (res_NotLogicOP_114 && ! Timer_Scaduto(L_P1__GetSubcl122(my_id)));
    res_AndLogicOP_113 = (res_AndLogicOP_113 && res_NotLogicOP_114);
    
    res_OrLogicOP_111 = (res_OrLogicOP_111 || res_AndLogicOP_113);
    
    res_OrLogicOP_110 = (res_OrLogicOP_110 || res_OrLogicOP_111);
    res_OrLogicOP_110 = (res_OrLogicOP_110 || (Counter_GetValore(L_P1__GetSubcl125(my_id)) == 155u));
    
    res_OrLogicOP_109 = (res_OrLogicOP_109 || res_OrLogicOP_110);
    res_OrLogicOP_109 = (res_OrLogicOP_109 || (L_P1__GetInSubcl93(my_id) == false));
    
    if(res_OrLogicOP_109){
    xorIndex_res_XorLogicOP_13 = (xorIndex_res_XorLogicOP_13 + 1);
    }
    
    res_XorLogicOP_13 = (res_XorLogicOP_13 && (xorIndex_res_XorLogicOP_13 == 1));
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_XorLogicOP_13);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *48,51,*  *,*  il controllo SubClass_C4_controllo_C8 non sia  uguale a GialloxVerdex
    //   *104,* e  che  *,*  il contatore SubClass_C4_contatore_Co8 non sia  minore di  *55,* 1102
    bool res_AndLogicOP_115 = true;
    bool res_NotLogicOP_116 = true;
    res_NotLogicOP_116 = (res_NotLogicOP_116 && ! (L_P1__GetInSubcl94(my_id) == gialloxverd));
    res_AndLogicOP_115 = (res_AndLogicOP_115 && res_NotLogicOP_116);
    bool res_NotLogicOP_117 = true;
    res_NotLogicOP_117 = (res_NotLogicOP_117 && ! (Counter_GetValore(L_P1__GetSubcl126(my_id)) < 1102u));
    res_AndLogicOP_115 = (res_AndLogicOP_115 && res_NotLogicOP_117);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_AndLogicOP_115);
    
    
    
    return res_AndLogicOP_0;
}


// Macro valorizzate

/*
    CNL corrispondente:
    
    { commento: {[} commento: {36,}  se il timer SubClass_C4_timer_T3 è attivo commento: {34,} e  se lo stato  non è  diverso da  commento: {56,}  state1  commento: {106,} commento: {111,} e  se lo stato del campo  MainClass_C1 di SubClass_C4_lista_L9 esiste e  commento: {105,} è  diverso da  commento: {56,}  state1  commento: {41,} e  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C4_lista_L9 esiste e  commento: {105,} è  uguale a c270 , assegna alla macro il valore RossoGialloVerde
    
     commento: {46,} assegna alla macro il valore RossoGialloVerde commento: {],}
    }
*/
C4_Enumerat2 L_P1__Macro33(instance_id_t const my_id , C4_Enumerat1 argom94, C4_Enumerat1 argom95, C4_Enumerat2 argom96, bool argom97)
{
C4_Enumerat2 res_macro_val;
    
    //  *[* *36,*  se il timer SubClass_C4_timer_T3 è attivo *34,* e  se lo stato  non è  diverso da  *56,*  state1  *106,* *111,* e  se lo stato del campo  MainClass_C1 di SubClass_C4_lista_L9 esiste e  *105,* è  diverso da  *56,*  state1  *41,* e  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C4_lista_L9 esiste e  *105,* è  uguale a c270
    bool res_AndLogicOP_0 = true;
    bool res_AndLogicOP_1 = true;
    bool res_AndLogicOP_2 = true;
    res_AndLogicOP_2 = (res_AndLogicOP_2 && Timer_Attivo(L_P1__GetSubcl123(my_id)));
    bool res_NotLogicOP_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1_C4_GetState(my_id) == C4_St_state));
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! res_NotLogicOP_4);
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_3);
    
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_AndLogicOP_2);
    bool res_ForAllPredicateNotEmpty_5 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl95Length(my_id); ++i)
    {
    L_P1__Recor3 it = L_P1__GetRecSubcl95(my_id,i);
    bool res_ImpliesLogicOp_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1_C1_GetState(it.mainc48) == C1_St_state));
    res_ImpliesLogicOp_6 = (res_ImpliesLogicOp_6 && res_NotLogicOP_7);
    res_ForAllPredicateNotEmpty_5 = res_ImpliesLogicOp_6;
    if(!res_ForAllPredicateNotEmpty_5) {break;}
    }
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_ForAllPredicateNotEmpty_5);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_AndLogicOP_1);
    bool res_ForAllPredicateNotEmpty_8 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl95Length(my_id); ++i)
    {
    L_P1__Recor3 it = L_P1__GetRecSubcl95(my_id,i);
    bool res_ImpliesLogicOp_9 = true;
    res_ImpliesLogicOp_9 = (res_ImpliesLogicOp_9 && (L_P1__GetParamMainc5(it.mainc48) == c270));
    res_ForAllPredicateNotEmpty_8 = res_ImpliesLogicOp_9;
    if(!res_ForAllPredicateNotEmpty_8) {break;}
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ForAllPredicateNotEmpty_8);
    
    if(res_AndLogicOP_0){
    
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
     commento: {46,} assegna alla macro il valore RossoGialloVerde commento: {],}
    }
*/
C4_Enumerat2 L_P1__Macro34(instance_id_t const my_id )
{
return rossogiallo1;
}



