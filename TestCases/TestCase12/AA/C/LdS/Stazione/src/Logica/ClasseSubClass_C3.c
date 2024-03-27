// Codice del modello 'TestCase12', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#include "Logica/ClasseMainClass_C1.h"
#include "Logica/ClasseSubClass_C2.h"
#include "Logica/ClasseSubClass_C3.h"
#include "Logica/ClasseSubClass_C3_priv.h"
#include "config.h"
#include "scheduler.h"


// ********** Definizione guardie **********

/*
    CNL corrispondente:
    
     {
     Nessuna 
     }
*/
static inline bool L_P1__Guard19(instance_id_t const my_id)
{
    return true;
}


/*
    CNL corrispondente:
    
    {
    
     commento: {68,} commento: {34,}  se il parametro SubClass_C3_parametro_P2 non è  diverso da c120x commento: {34,} o  se il parametro SubClass_C3_parametro_P4 non è  uguale a  commento: {53,} 8 commento: {35,} o  se il controllo SubClass_C3_controllo_C2 non è  uguale a  True  commento: {38,} o  se il contatore SubClass_C3_contatore_Co3 non è  uguale a  commento: {53,} 133, Almeno una delle seguenti { 
     commento: {67,} commento: {36,}  se il timer SubClass_C3_timer_T10 non è disattivo commento: {38,} o  se il contatore SubClass_C3_contatore_Co3 non è  maggiore di  commento: {54,} 140 commento: {35,} o  se il controllo SubClass_C3_controllo_C2 è  uguale a  False , Tutte le seguenti { 
     commento: {67,} commento: {36,}  se il timer SubClass_C3_timer_T7 è scaduto e  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} e  se la variabile SubClass_C3_variabile_V10 non è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} o  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x, Tutte le seguenti { 
     commento: {67,} commento: {38,}  se il contatore SubClass_C3_contatore_Co5 non è  uguale a  commento: {53,} 1245 commento: {38,} e  se il contatore SubClass_C3_contatore_Co5 non è  uguale a  commento: {53,} 111, Tutte le seguenti { 
     commento: {69,} commento: {37,}  se la variabile SubClass_C3_variabile_V8 non è  uguale a  True  commento: {35,} e  se il controllo SubClass_C3_controllo_C10 non è  diverso da c120x commento: {37,} o  se la variabile SubClass_C3_variabile_V3 è  maggiore di  commento: {54,} 1, Solo una delle seguenti { 
     commento: {69,} commento: {36,}  se il timer SubClass_C3_timer_T7 è disattivo commento: {36,} e  se il timer SubClass_C3_timer_T2 non è attivo commento: {34,} o  se il parametro SubClass_C3_parametro_P4 è  minore di  commento: {55,} 6 commento: {35,} o  se il controllo SubClass_C3_controllo_C10 non è  uguale a c120x, Solo una delle seguenti { 
     commento: {68,}  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} o  se la variabile SubClass_C3_variabile_V8 è  uguale a  False  commento: {37,} o  se la variabile SubClass_C3_variabile_V10 non è  diverso da  False  commento: {38,} e  se il contatore SubClass_C3_contatore_Co5 è  maggiore di  commento: {54,} 14 commento: {36,} o  se il timer SubClass_C3_timer_T7 non è scaduto, Almeno una delle seguenti { 
     commento: {67,} commento: {35,}  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x, Tutte le seguenti { 
     commento: {35,}  se il controllo SubClass_C3_controllo_C2 non è  uguale a  False  commento: {37,} o  se la variabile SubClass_C3_variabile_V8 è  uguale a  False  commento: {37,} e  se la variabile SubClass_C3_variabile_V8 non è  uguale a  False , Verifica che   commento: {49,}  commento: {,}  il timer SubClass_C3_timer_T2 non sia disattivo
    
    
     } Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
    
    
     } Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
    
    
     } Verifica che   commento: {51,}  commento: {,}  il contatore SubClass_C3_contatore_Co3 sia  diverso da  commento: {56,} 12
    
    
     } Verifica che   commento: {47,}  commento: {34,}  il parametro SubClass_C3_parametro_P1 non sia  diverso da  False 
    
    
     } Verifica che   commento: {50,}  commento: {,}  la variabile SubClass_C3_variabile_V3 sia  uguale a  commento: {53,} 2
    
    
     } Verifica che   commento: {51,}  commento: {,}  il contatore SubClass_C3_contatore_Co5 non sia  minore di  commento: {55,} 130
    
    
     } Verifica che   commento: {49,}  commento: {,}  il timer SubClass_C3_timer_T7 non sia attivo
    
    
     } Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
    
    
    }
*/
static inline bool L_P1__Guard20(instance_id_t const my_id)
{
    bool res_AndLogicOP_0 = true;
    
    //  *68,* *34,*  se il parametro SubClass_C3_parametro_P2 non è  diverso da c120x *34,* o  se il parametro SubClass_C3_parametro_P4 non è  uguale a  *53,* 8 *35,* o  se il controllo SubClass_C3_controllo_C2 non è  uguale a  True  *38,* o  se il contatore SubClass_C3_contatore_Co3 non è  uguale a  *53,* 133, Almeno una delle seguenti { 
    //   *67,* *36,*  se il timer SubClass_C3_timer_T10 non è disattivo *38,* o  se il contatore SubClass_C3_contatore_Co3 non è  maggiore di  *54,* 140 *35,* o  se il controllo SubClass_C3_controllo_C2 è  uguale a  False , Tutte le seguenti { 
    //   *67,* *36,*  se il timer SubClass_C3_timer_T7 è scaduto e  se il controllo ConsDef  è  uguale a FALSE  *37,* e  se la variabile SubClass_C3_variabile_V10 non è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE  *35,* o  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x, Tutte le seguenti { 
    //   *67,* *38,*  se il contatore SubClass_C3_contatore_Co5 non è  uguale a  *53,* 1245 *38,* e  se il contatore SubClass_C3_contatore_Co5 non è  uguale a  *53,* 111, Tutte le seguenti { 
    //   *69,* *37,*  se la variabile SubClass_C3_variabile_V8 non è  uguale a  True  *35,* e  se il controllo SubClass_C3_controllo_C10 non è  diverso da c120x *37,* o  se la variabile SubClass_C3_variabile_V3 è  maggiore di  *54,* 1, Solo una delle seguenti { 
    //   *69,* *36,*  se il timer SubClass_C3_timer_T7 è disattivo *36,* e  se il timer SubClass_C3_timer_T2 non è attivo *34,* o  se il parametro SubClass_C3_parametro_P4 è  minore di  *55,* 6 *35,* o  se il controllo SubClass_C3_controllo_C10 non è  uguale a c120x, Solo una delle seguenti { 
    //   *68,*  se il controllo ConsDef  è  uguale a FALSE  *37,* o  se la variabile SubClass_C3_variabile_V8 è  uguale a  False  *37,* o  se la variabile SubClass_C3_variabile_V10 non è  diverso da  False  *38,* e  se il contatore SubClass_C3_contatore_Co5 è  maggiore di  *54,* 14 *36,* o  se il timer SubClass_C3_timer_T7 non è scaduto, Almeno una delle seguenti { 
    //   *67,* *35,*  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x, Tutte le seguenti { 
    //   *35,*  se il controllo SubClass_C3_controllo_C2 non è  uguale a  False  *37,* o  se la variabile SubClass_C3_variabile_V8 è  uguale a  False  *37,* e  se la variabile SubClass_C3_variabile_V8 non è  uguale a  False , Verifica che   *49,*  *,*  il timer SubClass_C3_timer_T2 non sia disattivo
    //   } Verifica che   *48,*   il controllo ConsDef  sia  uguale a FALSE 
    //   } Verifica che   *48,*   il controllo ConsDef  sia  uguale a FALSE 
    //   } Verifica che   *51,*  *,*  il contatore SubClass_C3_contatore_Co3 sia  diverso da  *56,* 12
    //   } Verifica che   *47,*  *34,*  il parametro SubClass_C3_parametro_P1 non sia  diverso da  False 
    //   } Verifica che   *50,*  *,*  la variabile SubClass_C3_variabile_V3 sia  uguale a  *53,* 2
    //   } Verifica che   *51,*  *,*  il contatore SubClass_C3_contatore_Co5 non sia  minore di  *55,* 130
    //   } Verifica che   *49,*  *,*  il timer SubClass_C3_timer_T7 non sia attivo
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_OrLogicOP_4 = false;
    bool res_NotLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetParamSubcl52(my_id) == c120x));
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! res_NotLogicOP_6);
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_NotLogicOP_5);
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetParamSubcl54(my_id) == 8u));
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_NotLogicOP_7);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_OrLogicOP_4);
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetInSubcl46(my_id) == true));
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_NotLogicOP_8);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (Counter_GetValore(L_P1__GetSubcl92(my_id)) == 133u));
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_9);
    
    if(res_OrLogicOP_2){
    bool res_OrLogicOP_10 = false;
    bool res_ImpliesLogicOp_11 = true;
    bool res_OrLogicOP_12 = false;
    bool res_OrLogicOP_13 = false;
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! Timer_Disattivo(L_P1__GetSubcl87(my_id)));
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_NotLogicOP_14);
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (Counter_GetValore(L_P1__GetSubcl92(my_id)) > 140u));
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_NotLogicOP_15);
    
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_OrLogicOP_13);
    res_OrLogicOP_12 = (res_OrLogicOP_12 || (L_P1__GetInSubcl46(my_id) == false));
    
    if(res_OrLogicOP_12){
    bool res_AndLogicOP_16 = true;
    bool res_ImpliesLogicOp_17 = true;
    bool res_OrLogicOP_18 = false;
    bool res_OrLogicOP_19 = false;
    bool res_AndLogicOP_20 = true;
    bool res_AndLogicOP_21 = true;
    res_AndLogicOP_21 = (res_AndLogicOP_21 && Timer_Scaduto(L_P1__GetSubcl91(my_id)));
    res_AndLogicOP_21 = (res_AndLogicOP_21 && (L_P1__GetInConsd2(my_id) == false));
    
    res_AndLogicOP_20 = (res_AndLogicOP_20 && res_AndLogicOP_21);
    bool res_NotLogicOP_22 = true;
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! (L_P1__GetSubcl74(my_id) == false));
    res_AndLogicOP_20 = (res_AndLogicOP_20 && res_NotLogicOP_22);
    
    res_OrLogicOP_19 = (res_OrLogicOP_19 || res_AndLogicOP_20);
    res_OrLogicOP_19 = (res_OrLogicOP_19 || (L_P1__GetInConsd2(my_id) == false));
    
    res_OrLogicOP_18 = (res_OrLogicOP_18 || res_OrLogicOP_19);
    res_OrLogicOP_18 = (res_OrLogicOP_18 || (L_P1__GetInSubcl45(my_id) == c120x));
    
    if(res_OrLogicOP_18){
    bool res_AndLogicOP_23 = true;
    bool res_ImpliesLogicOp_24 = true;
    bool res_AndLogicOP_25 = true;
    bool res_NotLogicOP_26 = true;
    res_NotLogicOP_26 = (res_NotLogicOP_26 && ! (Counter_GetValore(L_P1__GetSubcl93(my_id)) == 1245u));
    res_AndLogicOP_25 = (res_AndLogicOP_25 && res_NotLogicOP_26);
    bool res_NotLogicOP_27 = true;
    res_NotLogicOP_27 = (res_NotLogicOP_27 && ! (Counter_GetValore(L_P1__GetSubcl93(my_id)) == 111u));
    res_AndLogicOP_25 = (res_AndLogicOP_25 && res_NotLogicOP_27);
    
    if(res_AndLogicOP_25){
    bool res_AndLogicOP_28 = true;
    bool res_ImpliesLogicOp_29 = true;
    bool res_OrLogicOP_30 = false;
    bool res_AndLogicOP_31 = true;
    bool res_NotLogicOP_32 = true;
    res_NotLogicOP_32 = (res_NotLogicOP_32 && ! (L_P1__GetSubcl76(my_id) == true));
    res_AndLogicOP_31 = (res_AndLogicOP_31 && res_NotLogicOP_32);
    bool res_NotLogicOP_33 = true;
    bool res_NotLogicOP_34 = true;
    res_NotLogicOP_34 = (res_NotLogicOP_34 && ! (L_P1__GetInSubcl45(my_id) == c120x));
    res_NotLogicOP_33 = (res_NotLogicOP_33 && ! res_NotLogicOP_34);
    res_AndLogicOP_31 = (res_AndLogicOP_31 && res_NotLogicOP_33);
    
    res_OrLogicOP_30 = (res_OrLogicOP_30 || res_AndLogicOP_31);
    res_OrLogicOP_30 = (res_OrLogicOP_30 || (L_P1__GetSubcl75(my_id) > 1u));
    
    if(res_OrLogicOP_30){
    bool res_XorLogicOP_35 = true;
    int xorIndex_res_XorLogicOP_35 = 0;
    bool res_ImpliesLogicOp_36 = true;
    bool res_OrLogicOP_37 = false;
    bool res_OrLogicOP_38 = false;
    bool res_AndLogicOP_39 = true;
    res_AndLogicOP_39 = (res_AndLogicOP_39 && Timer_Disattivo(L_P1__GetSubcl91(my_id)));
    bool res_NotLogicOP_40 = true;
    res_NotLogicOP_40 = (res_NotLogicOP_40 && ! Timer_Attivo(L_P1__GetSubcl88(my_id)));
    res_AndLogicOP_39 = (res_AndLogicOP_39 && res_NotLogicOP_40);
    
    res_OrLogicOP_38 = (res_OrLogicOP_38 || res_AndLogicOP_39);
    res_OrLogicOP_38 = (res_OrLogicOP_38 || (L_P1__GetParamSubcl54(my_id) < 6u));
    
    res_OrLogicOP_37 = (res_OrLogicOP_37 || res_OrLogicOP_38);
    bool res_NotLogicOP_41 = true;
    res_NotLogicOP_41 = (res_NotLogicOP_41 && ! (L_P1__GetInSubcl45(my_id) == c120x));
    res_OrLogicOP_37 = (res_OrLogicOP_37 || res_NotLogicOP_41);
    
    if(res_OrLogicOP_37){
    bool res_XorLogicOP_42 = true;
    int xorIndex_res_XorLogicOP_42 = 0;
    bool res_ImpliesLogicOp_43 = true;
    bool res_OrLogicOP_44 = false;
    bool res_OrLogicOP_45 = false;
    bool res_OrLogicOP_46 = false;
    res_OrLogicOP_46 = (res_OrLogicOP_46 || (L_P1__GetInConsd2(my_id) == false));
    res_OrLogicOP_46 = (res_OrLogicOP_46 || (L_P1__GetSubcl76(my_id) == false));
    
    res_OrLogicOP_45 = (res_OrLogicOP_45 || res_OrLogicOP_46);
    bool res_AndLogicOP_47 = true;
    bool res_NotLogicOP_48 = true;
    bool res_NotLogicOP_49 = true;
    res_NotLogicOP_49 = (res_NotLogicOP_49 && ! (L_P1__GetSubcl74(my_id) == false));
    res_NotLogicOP_48 = (res_NotLogicOP_48 && ! res_NotLogicOP_49);
    res_AndLogicOP_47 = (res_AndLogicOP_47 && res_NotLogicOP_48);
    res_AndLogicOP_47 = (res_AndLogicOP_47 && (Counter_GetValore(L_P1__GetSubcl93(my_id)) > 14u));
    
    res_OrLogicOP_45 = (res_OrLogicOP_45 || res_AndLogicOP_47);
    
    res_OrLogicOP_44 = (res_OrLogicOP_44 || res_OrLogicOP_45);
    bool res_NotLogicOP_50 = true;
    res_NotLogicOP_50 = (res_NotLogicOP_50 && ! Timer_Scaduto(L_P1__GetSubcl91(my_id)));
    res_OrLogicOP_44 = (res_OrLogicOP_44 || res_NotLogicOP_50);
    
    if(res_OrLogicOP_44){
    bool res_OrLogicOP_51 = false;
    bool res_ImpliesLogicOp_52 = true;
    if((L_P1__GetInSubcl45(my_id) == c120x)){
    bool res_ImpliesLogicOp_53 = true;
    bool res_OrLogicOP_54 = false;
    bool res_NotLogicOP_55 = true;
    res_NotLogicOP_55 = (res_NotLogicOP_55 && ! (L_P1__GetInSubcl46(my_id) == false));
    res_OrLogicOP_54 = (res_OrLogicOP_54 || res_NotLogicOP_55);
    bool res_AndLogicOP_56 = true;
    res_AndLogicOP_56 = (res_AndLogicOP_56 && (L_P1__GetSubcl76(my_id) == false));
    bool res_NotLogicOP_57 = true;
    res_NotLogicOP_57 = (res_NotLogicOP_57 && ! (L_P1__GetSubcl76(my_id) == false));
    res_AndLogicOP_56 = (res_AndLogicOP_56 && res_NotLogicOP_57);
    
    res_OrLogicOP_54 = (res_OrLogicOP_54 || res_AndLogicOP_56);
    
    if(res_OrLogicOP_54){
    bool res_NotLogicOP_58 = true;
    res_NotLogicOP_58 = (res_NotLogicOP_58 && ! Timer_Disattivo(L_P1__GetSubcl88(my_id)));
    res_ImpliesLogicOp_53 = (res_ImpliesLogicOp_53 && res_NotLogicOP_58);
    }
    res_ImpliesLogicOp_52 = (res_ImpliesLogicOp_52 && res_ImpliesLogicOp_53);
    }
    res_OrLogicOP_51 = (res_OrLogicOP_51 || res_ImpliesLogicOp_52);
    res_OrLogicOP_51 = (res_OrLogicOP_51 || (L_P1__GetInConsd2(my_id) == false));
    
    res_ImpliesLogicOp_43 = (res_ImpliesLogicOp_43 && res_OrLogicOP_51);
    }
    if(res_ImpliesLogicOp_43){
    xorIndex_res_XorLogicOP_42 = (xorIndex_res_XorLogicOP_42 + 1);
    }
    if((L_P1__GetInConsd2(my_id) == false)){
    xorIndex_res_XorLogicOP_42 = (xorIndex_res_XorLogicOP_42 + 1);
    }
    
    res_XorLogicOP_42 = (res_XorLogicOP_42 && (xorIndex_res_XorLogicOP_42 == 1));
    res_ImpliesLogicOp_36 = (res_ImpliesLogicOp_36 && res_XorLogicOP_42);
    }
    if(res_ImpliesLogicOp_36){
    xorIndex_res_XorLogicOP_35 = (xorIndex_res_XorLogicOP_35 + 1);
    }
    bool res_NotLogicOP_59 = true;
    res_NotLogicOP_59 = (res_NotLogicOP_59 && ! (Counter_GetValore(L_P1__GetSubcl92(my_id)) == 12u));
    if(res_NotLogicOP_59){
    xorIndex_res_XorLogicOP_35 = (xorIndex_res_XorLogicOP_35 + 1);
    }
    
    res_XorLogicOP_35 = (res_XorLogicOP_35 && (xorIndex_res_XorLogicOP_35 == 1));
    res_ImpliesLogicOp_29 = (res_ImpliesLogicOp_29 && res_XorLogicOP_35);
    }
    res_AndLogicOP_28 = (res_AndLogicOP_28 && res_ImpliesLogicOp_29);
    bool res_NotLogicOP_60 = true;
    bool res_NotLogicOP_61 = true;
    res_NotLogicOP_61 = (res_NotLogicOP_61 && ! (L_P1__GetParamSubcl51(my_id) == false));
    res_NotLogicOP_60 = (res_NotLogicOP_60 && ! res_NotLogicOP_61);
    res_AndLogicOP_28 = (res_AndLogicOP_28 && res_NotLogicOP_60);
    
    res_ImpliesLogicOp_24 = (res_ImpliesLogicOp_24 && res_AndLogicOP_28);
    }
    res_AndLogicOP_23 = (res_AndLogicOP_23 && res_ImpliesLogicOp_24);
    res_AndLogicOP_23 = (res_AndLogicOP_23 && (L_P1__GetSubcl75(my_id) == 2u));
    
    res_ImpliesLogicOp_17 = (res_ImpliesLogicOp_17 && res_AndLogicOP_23);
    }
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_ImpliesLogicOp_17);
    bool res_NotLogicOP_62 = true;
    res_NotLogicOP_62 = (res_NotLogicOP_62 && ! (Counter_GetValore(L_P1__GetSubcl93(my_id)) < 130u));
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_NotLogicOP_62);
    
    res_ImpliesLogicOp_11 = (res_ImpliesLogicOp_11 && res_AndLogicOP_16);
    }
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_ImpliesLogicOp_11);
    bool res_NotLogicOP_63 = true;
    res_NotLogicOP_63 = (res_NotLogicOP_63 && ! Timer_Attivo(L_P1__GetSubcl91(my_id)));
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_NotLogicOP_63);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_OrLogicOP_10);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *48,*   il controllo ConsDef  sia  uguale a FALSE
    res_AndLogicOP_0 = (res_AndLogicOP_0 && (L_P1__GetInConsd2(my_id) == false));
    
    
    
    return res_AndLogicOP_0;
}


/*
    CNL corrispondente:
     {  Nessuna  }
*/
static inline bool L_P1__Guard21(instance_id_t const my_id)
{
    return true;
}


/*
    CNL corrispondente:
     {  Nessuna  }
*/
static inline bool L_P1__Guard22(instance_id_t const my_id)
{
    return true;
}


/*
    CNL corrispondente:
     {  commento: {67,} commento: {34,}  se il parametro SubClass_C3_parametro_P2 non è  diverso da c120x commento: {37,} o  se la variabile SubClass_C3_variabile_V8 non è  uguale a  False  commento: {36,} e  se il timer SubClass_C3_timer_T7 è attivo, Tutte le seguenti { 
     commento: {35,}  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x commento: {35,} e  se il controllo SubClass_C3_controllo_C2 non è  uguale a  False  commento: {36,} e  se il timer SubClass_C3_timer_T2 è scaduto commento: {35,} o  se il controllo SubClass_C3_controllo_C10 è  diverso da c120x commento: {38,} e  se il contatore SubClass_C3_contatore_Co3 è  minore di  commento: {55,} 115 e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   commento: {48,}  commento: {,}  il controllo SubClass_C3_controllo_C6 sia  uguale a RossoVerde
    
    
     } Verifica che   commento: {48,}  commento: {,}  il controllo SubClass_C3_controllo_C2 non sia  uguale a  False 
    
     }
*/
static inline bool L_P1__Guard23(instance_id_t const my_id)
{
    bool res_AndLogicOP_0 = true;
    
    //  *67,* *34,*  se il parametro SubClass_C3_parametro_P2 non è  diverso da c120x *37,* o  se la variabile SubClass_C3_variabile_V8 non è  uguale a  False  *36,* e  se il timer SubClass_C3_timer_T7 è attivo, Tutte le seguenti { 
    //   *35,*  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x *35,* e  se il controllo SubClass_C3_controllo_C2 non è  uguale a  False  *36,* e  se il timer SubClass_C3_timer_T2 è scaduto *35,* o  se il controllo SubClass_C3_controllo_C10 è  diverso da c120x *38,* e  se il contatore SubClass_C3_contatore_Co3 è  minore di  *55,* 115 e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   *48,*  *,*  il controllo SubClass_C3_controllo_C6 sia  uguale a RossoVerde
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_NotLogicOP_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetParamSubcl52(my_id) == c120x));
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! res_NotLogicOP_4);
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_NotLogicOP_3);
    bool res_AndLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetSubcl76(my_id) == false));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_6);
    res_AndLogicOP_5 = (res_AndLogicOP_5 && Timer_Attivo(L_P1__GetSubcl91(my_id)));
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_5);
    
    if(res_OrLogicOP_2){
    bool res_ImpliesLogicOp_7 = true;
    bool res_OrLogicOP_8 = false;
    bool res_AndLogicOP_9 = true;
    bool res_AndLogicOP_10 = true;
    res_AndLogicOP_10 = (res_AndLogicOP_10 && (L_P1__GetInSubcl45(my_id) == c120x));
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (L_P1__GetInSubcl46(my_id) == false));
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_NotLogicOP_11);
    
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_AndLogicOP_10);
    res_AndLogicOP_9 = (res_AndLogicOP_9 && Timer_Scaduto(L_P1__GetSubcl88(my_id)));
    
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_AndLogicOP_9);
    bool res_AndLogicOP_12 = true;
    bool res_AndLogicOP_13 = true;
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1__GetInSubcl45(my_id) == c120x));
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_NotLogicOP_14);
    res_AndLogicOP_13 = (res_AndLogicOP_13 && (Counter_GetValore(L_P1__GetSubcl92(my_id)) < 115u));
    
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_AndLogicOP_13);
    res_AndLogicOP_12 = (res_AndLogicOP_12 && (L_P1__GetInConsd2(my_id) == false));
    
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_AndLogicOP_12);
    
    if(res_OrLogicOP_8){
    res_ImpliesLogicOp_7 = (res_ImpliesLogicOp_7 && (L_P1__GetInSubcl48(my_id) == rossoverde));
    }
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_ImpliesLogicOp_7);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *48,*  *,*  il controllo SubClass_C3_controllo_C2 non sia  uguale a  False
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (L_P1__GetInSubcl46(my_id) == false));
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_NotLogicOP_15);
    
    
    
    return res_AndLogicOP_0;
}


/*
    CNL corrispondente:
     {  Nessuna  commento: {80,} }
*/
static inline bool L_P1__Guard24(instance_id_t const my_id)
{
    return true;
}


/*
    CNL corrispondente:
     {  Nessuna  }
*/
static inline bool L_P1__Guard25(instance_id_t const my_id)
{
    return true;
}


/*
    CNL corrispondente:
    
    {
    
     Nessuna 
    }
*/
static inline bool L_P1__Guard26(instance_id_t const my_id)
{
    return true;
}


/*
    CNL corrispondente:
    
    {
    
     Nessuna 
    }
*/
static inline bool L_P1__Guard27(instance_id_t const my_id)
{
    return true;
}


/*
    CNL corrispondente:
    
    {
    
     Nessuna 
    }
*/
static inline bool L_P1__Guard28(instance_id_t const my_id)
{
    return true;
}


/*
    CNL corrispondente:
    
    {
    
     Nessuna 
    }
*/
static inline bool L_P1__Guard29(instance_id_t const my_id)
{
    return true;
}


/*
    CNL corrispondente:
     {  Nessuna  }
*/
static inline bool L_P1__Guard30(instance_id_t const my_id)
{
    return true;
}


/*
    CNL corrispondente:
     {  Nessuna  }
*/
static inline bool L_P1__Guard31(instance_id_t const my_id)
{
    return true;
}


/*
    CNL corrispondente:
     {  Nessuna  commento: {80,} }
*/
static inline bool L_P1__Guard32(instance_id_t const my_id)
{
    return true;
}


/*
    CNL corrispondente:
     {  Nessuna  }
*/
static inline bool L_P1__Guard33(instance_id_t const my_id)
{
    return true;
}


/*
    CNL corrispondente:
     {  Nessuna  commento: {80,} }
*/
static inline bool L_P1__Guard34(instance_id_t const my_id)
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
static inline void L_P1__Effec19(instance_id_t const my_id)
{
    
}


/*
    CNL corrispondente:
    
    {
    
     commento: {41,}  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C3_lista_L10 è  uguale a  False  commento: {38,} o  se il contatore SubClass_C3_contatore_Co5 non è  minore di  commento: {55,} 114 commento: {34,} o  se il parametro SubClass_C3_parametro_P2 è  diverso da c120x commento: {37,} e  se la variabile SubClass_C3_variabile_V8 non è  uguale a  True  commento: {36,} e  se il timer SubClass_C3_timer_T5 non è scaduto commento: {36,} e  se il timer SubClass_C3_timer_T7 non è scaduto, commento: {69,}Disattiva il timer SubClass_C3_timer_T7
    
       
     commento: {110,}  se il ripristino del timer  SubClass_C3_restoreTI_TI2 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE ,  Applica gli effetti
           della macro SubClass_C3_macroef_M2  commento: {73,}
    
       
     commento: {35,}  se il controllo SubClass_C3_controllo_C10 è  diverso da c120x commento: {37,} o  se la variabile SubClass_C3_variabile_V10 è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro SubClass_C3_parametro_P2 è  uguale a c120x,  Applica gli effetti
           della macro SubClass_C3_macroef_M10  commento: {73,}
    
       
    
    }
*/
static inline void L_P1__Effec20(instance_id_t const my_id)
{
    
    //  *41,*  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C3_lista_L10 è  uguale a  False  *38,* o  se il contatore SubClass_C3_contatore_Co5 non è  minore di  *55,* 114 *34,* o  se il parametro SubClass_C3_parametro_P2 è  diverso da c120x *37,* e  se la variabile SubClass_C3_variabile_V8 non è  uguale a  True  *36,* e  se il timer SubClass_C3_timer_T5 non è scaduto *36,* e  se il timer SubClass_C3_timer_T7 non è scaduto, *69,*Disattiva il timer SubClass_C3_timer_T7
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_ForAllPredicate_2 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl49Length(my_id); ++i)
    {
    L_P1__Recor1 it = L_P1__GetRecSubcl49(my_id,i);
    bool res_ImpliesLogicOp_3 = true;
    res_ImpliesLogicOp_3 = (res_ImpliesLogicOp_3 && (L_P1__GetParamMainc9(it.mainc48) == false));
    res_ForAllPredicate_2 = res_ImpliesLogicOp_3;
    if(!res_ForAllPredicate_2) {break;}
    }
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_ForAllPredicate_2);
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (Counter_GetValore(L_P1__GetSubcl93(my_id)) < 114u));
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_NotLogicOP_4);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_AndLogicOP_5 = true;
    bool res_AndLogicOP_6 = true;
    bool res_AndLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetParamSubcl52(my_id) == c120x));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_8);
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetSubcl76(my_id) == true));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_9);
    
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_AndLogicOP_7);
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! Timer_Scaduto(L_P1__GetSubcl90(my_id)));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_10);
    
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_AndLogicOP_6);
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! Timer_Scaduto(L_P1__GetSubcl91(my_id)));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_11);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_5);
    
    if(res_OrLogicOP_0){
    
    Timer_Disattiva(L_P1__GetSubcl91(my_id));
    }
    
    //  *110,*  se il ripristino del timer  SubClass_C3_restoreTI_TI2 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE ,  Applica gli effetti
    //         della macro SubClass_C3_macroef_M2
    bool res_OrLogicOP_12 = false;
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! Timer_Disattivo(L_P1__GetSubcl80(my_id)));
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_NotLogicOP_13);
    res_OrLogicOP_12 = (res_OrLogicOP_12 || (L_P1__GetInConsd2(my_id) == false));
    
    if(res_OrLogicOP_12){
    
    L_P1__Macro24(my_id);
    }
    
    //  *73,*
    //     
    //   *35,*  se il controllo SubClass_C3_controllo_C10 è  diverso da c120x *37,* o  se la variabile SubClass_C3_variabile_V10 è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE  *34,* e  se il parametro SubClass_C3_parametro_P2 è  uguale a c120x,  Applica gli effetti
    //         della macro SubClass_C3_macroef_M10
    bool res_OrLogicOP_14 = false;
    bool res_OrLogicOP_15 = false;
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (L_P1__GetInSubcl45(my_id) == c120x));
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_NotLogicOP_16);
    res_OrLogicOP_15 = (res_OrLogicOP_15 || (L_P1__GetSubcl74(my_id) == false));
    
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_OrLogicOP_15);
    bool res_AndLogicOP_17 = true;
    res_AndLogicOP_17 = (res_AndLogicOP_17 && (L_P1__GetInConsd2(my_id) == false));
    res_AndLogicOP_17 = (res_AndLogicOP_17 && (L_P1__GetParamSubcl52(my_id) == c120x));
    
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_AndLogicOP_17);
    
    if(res_OrLogicOP_14){
    
    L_P1__Macro23(my_id);
    }
}


/*
    CNL corrispondente:
     { commento: {34,}  se lo stato  non è  diverso da  commento: {56,}  state1  commento: {106,} commento: {37,} e  se la variabile SubClass_C3_variabile_V10 non è  diverso da  False  commento: {38,} e  se il contatore SubClass_C3_contatore_Co5 non è  minore di  commento: {55,} 12230 commento: {38,} e  se il contatore SubClass_C3_contatore_Co9 è  minore di  commento: {55,} 1445, commento: {66,} Assegna al comando SubClass_C3_comando_C1 il valore  True 
    
       
     }
*/
static inline void L_P1__Effec21(instance_id_t const my_id)
{
    
    //  *34,*  se lo stato  non è  diverso da  *56,*  state1  *106,* *37,* e  se la variabile SubClass_C3_variabile_V10 non è  diverso da  False  *38,* e  se il contatore SubClass_C3_contatore_Co5 non è  minore di  *55,* 12230 *38,* e  se il contatore SubClass_C3_contatore_Co9 è  minore di  *55,* 1445, *66,* Assegna al comando SubClass_C3_comando_C1 il valore  True
    bool res_AndLogicOP_0 = true;
    bool res_AndLogicOP_1 = true;
    bool res_AndLogicOP_2 = true;
    bool res_NotLogicOP_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1_C3_GetState(my_id) == C3_St_state));
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! res_NotLogicOP_4);
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_3);
    bool res_NotLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetSubcl74(my_id) == false));
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! res_NotLogicOP_6);
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_5);
    
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_AndLogicOP_2);
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (Counter_GetValore(L_P1__GetSubcl93(my_id)) < 12230u));
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_7);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_AndLogicOP_1);
    res_AndLogicOP_0 = (res_AndLogicOP_0 && (Counter_GetValore(L_P1__GetSubcl94(my_id)) < 1445u));
    
    if(res_AndLogicOP_0){
    
    L_P1__SetOutSubcl43(my_id,true);
    }
}


/*
    CNL corrispondente:
     { commento: {37,}  se la variabile SubClass_C3_variabile_V8 è  uguale a  True ,  commento: {45,}  se  MainClass_C1_contatore_Co8 del campo  MainClass_C1 di SubClass_C3_lista_L10 è  minore di  commento: {55,} 153, commento: {88,} quando  commento: {45,}    MainClass_C1_contatore_Co8 del campo  MainClass_C1     commento: {105,} è  diverso da  commento: {56,} 15 e  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} o  se la variabile SubClass_C3_variabile_V10 è  diverso da  False  commento: {36,} o  se il timer SubClass_C3_timer_T2 non è disattivo commento: {34,} e  se il parametro SubClass_C3_parametro_P3 è  maggiore di  commento: {54,} 6, commento: {67,} Assegna alla variabile SubClass_C3_variabile_V3 il valore 1
    
       
     commento: {38,}  se il contatore SubClass_C3_contatore_Co9 non è  maggiore di  commento: {54,} 1404 commento: {34,} o  se il parametro SubClass_C3_parametro_P3 è  diverso da  commento: {56,} 1 commento: {37,} e  se la variabile SubClass_C3_variabile_V10 è  diverso da  False , commento: {66,} Assegna al comando SubClass_C3_comando_C1 il valore  False 
    
       
     commento: {35,}  se il controllo SubClass_C3_controllo_C10 è  diverso da c120x commento: {38,} e  se il contatore SubClass_C3_contatore_Co3 è  diverso da  commento: {56,} 14, commento: {67,} Assegna alla variabile SubClass_C3_variabile_V8 il valore  False 
    
     ,altrimenti   Applica gli effetti
           della macro SubClass_C3_macroef_M2  commento: {73,}
    
    
     }
*/
static inline void L_P1__Effec22(instance_id_t const my_id)
{
    
    //  *37,*  se la variabile SubClass_C3_variabile_V8 è  uguale a  True ,  *45,*  se  MainClass_C1_contatore_Co8 del campo  MainClass_C1 di SubClass_C3_lista_L10 è  minore di  *55,* 153, *88,* quando  *45,*    MainClass_C1_contatore_Co8 del campo  MainClass_C1     *105,* è  diverso da  *56,* 15 e  se il controllo ConsDef  è  uguale a FALSE  *37,* o  se la variabile SubClass_C3_variabile_V10 è  diverso da  False  *36,* o  se il timer SubClass_C3_timer_T2 non è disattivo *34,* e  se il parametro SubClass_C3_parametro_P3 è  maggiore di  *54,* 6, *67,* Assegna alla variabile SubClass_C3_variabile_V3 il valore 1
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_AndLogicOP_2 = true;
    bool res_AndLogicOP_3 = true;
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (L_P1__GetSubcl76(my_id) == true));
    bool res_ForAllPredicate_4 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl49Length(my_id); ++i)
    {
    L_P1__Recor1 it = L_P1__GetRecSubcl49(my_id,i);
    bool res_ImpliesLogicOp_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (Counter_GetValore(L_P1__GetMainc45(it.mainc48)) == 15u));
    if(res_NotLogicOP_6){
    res_ImpliesLogicOp_5 = (res_ImpliesLogicOp_5 && (Counter_GetValore(L_P1__GetMainc45(it.mainc48)) < 153u));
    }
    res_ForAllPredicate_4 = res_ImpliesLogicOp_5;
    if(!res_ForAllPredicate_4) {break;}
    }
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_ForAllPredicate_4);
    
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_AndLogicOP_3);
    res_AndLogicOP_2 = (res_AndLogicOP_2 && (L_P1__GetInConsd2(my_id) == false));
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_2);
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetSubcl74(my_id) == false));
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_NotLogicOP_7);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_AndLogicOP_8 = true;
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! Timer_Disattivo(L_P1__GetSubcl88(my_id)));
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_9);
    res_AndLogicOP_8 = (res_AndLogicOP_8 && (L_P1__GetParamSubcl53(my_id) > 6u));
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_8);
    
    if(res_OrLogicOP_0){
    
    L_P1__SetSubcl75(my_id,1u);
    }
    
    //  *38,*  se il contatore SubClass_C3_contatore_Co9 non è  maggiore di  *54,* 1404 *34,* o  se il parametro SubClass_C3_parametro_P3 è  diverso da  *56,* 1 *37,* e  se la variabile SubClass_C3_variabile_V10 è  diverso da  False , *66,* Assegna al comando SubClass_C3_comando_C1 il valore  False
    bool res_OrLogicOP_10 = false;
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (Counter_GetValore(L_P1__GetSubcl94(my_id)) > 1404u));
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_NotLogicOP_11);
    bool res_AndLogicOP_12 = true;
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (L_P1__GetParamSubcl53(my_id) == 1u));
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_NotLogicOP_13);
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1__GetSubcl74(my_id) == false));
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_NotLogicOP_14);
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_AndLogicOP_12);
    
    if(res_OrLogicOP_10){
    
    L_P1__SetOutSubcl43(my_id,false);
    }
    
    //  *35,*  se il controllo SubClass_C3_controllo_C10 è  diverso da c120x *38,* e  se il contatore SubClass_C3_contatore_Co3 è  diverso da  *56,* 14, *67,* Assegna alla variabile SubClass_C3_variabile_V8 il valore  False 
    //   ,altrimenti   Applica gli effetti
    //         della macro SubClass_C3_macroef_M2
    bool res_AndLogicOP_15 = true;
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (L_P1__GetInSubcl45(my_id) == c120x));
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_NotLogicOP_16);
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! (Counter_GetValore(L_P1__GetSubcl92(my_id)) == 14u));
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_NotLogicOP_17);
    
    if(res_AndLogicOP_15){
    
    L_P1__SetSubcl76(my_id,false);
    }else{
    
    L_P1__Macro24(my_id);
    }
}


/*
    CNL corrispondente:
     { commento: {36,}  se il timer SubClass_C3_timer_T2 non è scaduto, commento: {68,}Attiva il timer SubClass_C3_timer_T5
    
       
     }
*/
static inline void L_P1__Effec23(instance_id_t const my_id)
{
    
    //  *36,*  se il timer SubClass_C3_timer_T2 non è scaduto, *68,*Attiva il timer SubClass_C3_timer_T5
    bool res_NotLogicOP_0 = true;
    res_NotLogicOP_0 = (res_NotLogicOP_0 && ! Timer_Scaduto(L_P1__GetSubcl88(my_id)));
    if(res_NotLogicOP_0){
    
    Timer_Attiva(L_P1__GetSubcl90(my_id));
    }
}


/*
    CNL corrispondente:
     { commento: {41,}  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  commento: {105,} è  diverso da  commento: {56,} 4, commento: {72,}Azzera il contatore SubClass_C3_contatore_Co3
    
     ,altrimenti  commento: {70,}Incrementa il contatore SubClass_C3_contatore_Co5
    
    
     commento: {45,}  se  MainClass_C1_contatore_Co8 del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  commento: {105,} è  minore di  commento: {55,} 11 commento: {38,} o  se il contatore SubClass_C3_contatore_Co3 non è  minore di  commento: {55,} 144 commento: {38,} o  se il contatore SubClass_C3_contatore_Co3 è  uguale a  commento: {53,} 14 commento: {34,} o  se il parametro SubClass_C3_parametro_P1 è  diverso da  True , commento: {67,} Assegna alla variabile SubClass_C3_variabile_V10 il valore  False 
    
       
     commento: {45,}  se  MainClass_C1_contatore_Co8 del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  commento: {105,} è  uguale a  commento: {53,} 145 commento: {35,} o  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x commento: {36,} e  se il timer SubClass_C3_timer_T7 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE , commento: {68,}Attiva il timer SubClass_C3_timer_T2
    
       
     commento: {35,}  se il controllo SubClass_C3_controllo_C2 è  diverso da  True  commento: {37,} e  se la variabile SubClass_C3_variabile_V10 è  diverso da  False  commento: {37,} e  se la variabile SubClass_C3_variabile_V3 è  diverso da  commento: {56,} 10 commento: {37,} e  se la variabile SubClass_C3_variabile_V10 non è  diverso da  True , commento: {71,}Decrementa il contatore SubClass_C3_contatore_Co5
    
       
     commento: {34,}  se il parametro SubClass_C3_parametro_P4 è  diverso da  commento: {56,} 2 o  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE ,  Applica gli effetti
           della macro SubClass_C3_macroef_M2  commento: {73,}
    
     ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C3_variabile_V8 il valore  True 
    
    
     }
*/
static inline void L_P1__Effec24(instance_id_t const my_id)
{
    
    //  *41,*  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  *105,* è  diverso da  *56,* 4, *72,*Azzera il contatore SubClass_C3_contatore_Co3
    //   ,altrimenti  *70,*Incrementa il contatore SubClass_C3_contatore_Co5
    bool res_ForAllPredicateNotEmpty_0 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl50Length(my_id); ++i)
    {
    L_P1__Recor2 it = L_P1__GetRecSubcl50(my_id,i);
    bool res_ImpliesLogicOp_1 = true;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (L_P1__GetParamMainc7(it.mainc49) == 4u));
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_NotLogicOP_2);
    res_ForAllPredicateNotEmpty_0 = res_ImpliesLogicOp_1;
    if(!res_ForAllPredicateNotEmpty_0) {break;}
    }
    if(res_ForAllPredicateNotEmpty_0){
    
    Counter_Res(L_P1__GetSubcl92(my_id));
    }else{
    
    Counter_Incr(L_P1__GetSubcl93(my_id));
    }
    
    //  *45,*  se  MainClass_C1_contatore_Co8 del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  *105,* è  minore di  *55,* 11 *38,* o  se il contatore SubClass_C3_contatore_Co3 non è  minore di  *55,* 144 *38,* o  se il contatore SubClass_C3_contatore_Co3 è  uguale a  *53,* 14 *34,* o  se il parametro SubClass_C3_parametro_P1 è  diverso da  True , *67,* Assegna alla variabile SubClass_C3_variabile_V10 il valore  False
    bool res_OrLogicOP_3 = false;
    bool res_OrLogicOP_4 = false;
    bool res_OrLogicOP_5 = false;
    bool res_ForAllPredicateNotEmpty_6 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl49Length(my_id); ++i)
    {
    L_P1__Recor1 it = L_P1__GetRecSubcl49(my_id,i);
    bool res_ImpliesLogicOp_7 = true;
    res_ImpliesLogicOp_7 = (res_ImpliesLogicOp_7 && (Counter_GetValore(L_P1__GetMainc45(it.mainc48)) < 11u));
    res_ForAllPredicateNotEmpty_6 = res_ImpliesLogicOp_7;
    if(!res_ForAllPredicateNotEmpty_6) {break;}
    }
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_ForAllPredicateNotEmpty_6);
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (Counter_GetValore(L_P1__GetSubcl92(my_id)) < 144u));
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_NotLogicOP_8);
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_OrLogicOP_5);
    res_OrLogicOP_4 = (res_OrLogicOP_4 || (Counter_GetValore(L_P1__GetSubcl92(my_id)) == 14u));
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_OrLogicOP_4);
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetParamSubcl51(my_id) == true));
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_NotLogicOP_9);
    
    if(res_OrLogicOP_3){
    
    L_P1__SetSubcl74(my_id,false);
    }
    
    //  *45,*  se  MainClass_C1_contatore_Co8 del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  *105,* è  uguale a  *53,* 145 *35,* o  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x *36,* e  se il timer SubClass_C3_timer_T7 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE , *68,*Attiva il timer SubClass_C3_timer_T2
    bool res_OrLogicOP_10 = false;
    bool res_ForAllPredicateNotEmpty_11 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl49Length(my_id); ++i)
    {
    L_P1__Recor1 it = L_P1__GetRecSubcl49(my_id,i);
    bool res_ImpliesLogicOp_12 = true;
    res_ImpliesLogicOp_12 = (res_ImpliesLogicOp_12 && (Counter_GetValore(L_P1__GetMainc45(it.mainc48)) == 145u));
    res_ForAllPredicateNotEmpty_11 = res_ImpliesLogicOp_12;
    if(!res_ForAllPredicateNotEmpty_11) {break;}
    }
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_ForAllPredicateNotEmpty_11);
    bool res_AndLogicOP_13 = true;
    bool res_AndLogicOP_14 = true;
    res_AndLogicOP_14 = (res_AndLogicOP_14 && (L_P1__GetInSubcl45(my_id) == c120x));
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! Timer_Scaduto(L_P1__GetSubcl91(my_id)));
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_NotLogicOP_15);
    
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_AndLogicOP_14);
    res_AndLogicOP_13 = (res_AndLogicOP_13 && (L_P1__GetInConsd2(my_id) == false));
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_AndLogicOP_13);
    
    if(res_OrLogicOP_10){
    
    Timer_Attiva(L_P1__GetSubcl88(my_id));
    }
    
    //  *35,*  se il controllo SubClass_C3_controllo_C2 è  diverso da  True  *37,* e  se la variabile SubClass_C3_variabile_V10 è  diverso da  False  *37,* e  se la variabile SubClass_C3_variabile_V3 è  diverso da  *56,* 10 *37,* e  se la variabile SubClass_C3_variabile_V10 non è  diverso da  True , *71,*Decrementa il contatore SubClass_C3_contatore_Co5
    bool res_AndLogicOP_16 = true;
    bool res_AndLogicOP_17 = true;
    bool res_AndLogicOP_18 = true;
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (L_P1__GetInSubcl46(my_id) == true));
    res_AndLogicOP_18 = (res_AndLogicOP_18 && res_NotLogicOP_19);
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! (L_P1__GetSubcl74(my_id) == false));
    res_AndLogicOP_18 = (res_AndLogicOP_18 && res_NotLogicOP_20);
    
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_AndLogicOP_18);
    bool res_NotLogicOP_21 = true;
    res_NotLogicOP_21 = (res_NotLogicOP_21 && ! (L_P1__GetSubcl75(my_id) == 10u));
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_NotLogicOP_21);
    
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_AndLogicOP_17);
    bool res_NotLogicOP_22 = true;
    bool res_NotLogicOP_23 = true;
    res_NotLogicOP_23 = (res_NotLogicOP_23 && ! (L_P1__GetSubcl74(my_id) == true));
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! res_NotLogicOP_23);
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_NotLogicOP_22);
    
    if(res_AndLogicOP_16){
    
    Counter_Decr(L_P1__GetSubcl93(my_id));
    }
    
    //  *34,*  se il parametro SubClass_C3_parametro_P4 è  diverso da  *56,* 2 o  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE ,  Applica gli effetti
    //         della macro SubClass_C3_macroef_M2  *73,*
    //   ,altrimenti  *67,* Assegna alla variabile SubClass_C3_variabile_V8 il valore  True
    bool res_OrLogicOP_24 = false;
    bool res_NotLogicOP_25 = true;
    res_NotLogicOP_25 = (res_NotLogicOP_25 && ! (L_P1__GetParamSubcl54(my_id) == 2u));
    res_OrLogicOP_24 = (res_OrLogicOP_24 || res_NotLogicOP_25);
    bool res_AndLogicOP_26 = true;
    res_AndLogicOP_26 = (res_AndLogicOP_26 && (L_P1__GetInConsd2(my_id) == false));
    res_AndLogicOP_26 = (res_AndLogicOP_26 && (L_P1__GetInConsd2(my_id) == false));
    
    res_OrLogicOP_24 = (res_OrLogicOP_24 || res_AndLogicOP_26);
    
    if(res_OrLogicOP_24){
    
    L_P1__Macro24(my_id);
    }else{
    
    L_P1__SetSubcl76(my_id,true);
    }
}


/*
    CNL corrispondente:
     { commento: {41,}  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  diverso da  False  e  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} o  se il parametro SubClass_C3_parametro_P1 non è  diverso da  False  commento: {35,} o  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x e  se il controllo ConsDef  è  uguale a FALSE , commento: {72,}Azzera il contatore SubClass_C3_contatore_Co5
    
       
     commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  commento: {105,} è  uguale a  commento: {53,}  state1 ,  Applica gli effetti
           della macro SubClass_C3_macroef_M1  commento: {73,}
    
     ,altrimenti   Applica gli effetti
           della macro SubClass_C3_macroef_M4  commento: {73,}
    
    
     }
*/
static inline void L_P1__Effec25(instance_id_t const my_id)
{
    
    //  *41,*  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  diverso da  False  e  se il controllo ConsDef  è  uguale a FALSE  *34,* o  se il parametro SubClass_C3_parametro_P1 non è  diverso da  False  *35,* o  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x e  se il controllo ConsDef  è  uguale a FALSE , *72,*Azzera il contatore SubClass_C3_contatore_Co5
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_AndLogicOP_2 = true;
    bool res_ForAllPredicate_3 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl50Length(my_id); ++i)
    {
    L_P1__Recor2 it = L_P1__GetRecSubcl50(my_id,i);
    bool res_ImpliesLogicOp_4 = true;
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetParamMainc9(it.mainc49) == false));
    res_ImpliesLogicOp_4 = (res_ImpliesLogicOp_4 && res_NotLogicOP_5);
    res_ForAllPredicate_3 = res_ImpliesLogicOp_4;
    if(!res_ForAllPredicate_3) {break;}
    }
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_ForAllPredicate_3);
    res_AndLogicOP_2 = (res_AndLogicOP_2 && (L_P1__GetInConsd2(my_id) == false));
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_2);
    bool res_NotLogicOP_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetParamSubcl51(my_id) == false));
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! res_NotLogicOP_7);
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_NotLogicOP_6);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_AndLogicOP_8 = true;
    res_AndLogicOP_8 = (res_AndLogicOP_8 && (L_P1__GetInSubcl45(my_id) == c120x));
    res_AndLogicOP_8 = (res_AndLogicOP_8 && (L_P1__GetInConsd2(my_id) == false));
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_8);
    
    if(res_OrLogicOP_0){
    
    Counter_Res(L_P1__GetSubcl93(my_id));
    }
    
    //  *111,*  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  *105,* è  uguale a  *53,*  state1 ,  Applica gli effetti
    //         della macro SubClass_C3_macroef_M1  *73,*
    //   ,altrimenti   Applica gli effetti
    //         della macro SubClass_C3_macroef_M4
    bool res_ForAllPredicateNotEmpty_9 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl49Length(my_id); ++i)
    {
    L_P1__Recor1 it = L_P1__GetRecSubcl49(my_id,i);
    bool res_ImpliesLogicOp_10 = true;
    res_ImpliesLogicOp_10 = (res_ImpliesLogicOp_10 && (L_P1_C1_GetState(it.mainc48) == C1_St_state));
    res_ForAllPredicateNotEmpty_9 = res_ImpliesLogicOp_10;
    if(!res_ForAllPredicateNotEmpty_9) {break;}
    }
    if(res_ForAllPredicateNotEmpty_9){
    
    L_P1__Macro22(my_id);
    }else{
    
    L_P1__Macro25(my_id);
    }
}


/*
    CNL corrispondente:
    
    {
    
     commento: {43,}  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  commento: {105,} è disattivo, commento: {70,}Incrementa il contatore SubClass_C3_contatore_Co3
    
     ,altrimenti   Applica gli effetti
           della macro SubClass_C3_macroef_M2  commento: {73,}
    
    
     commento: {37,}  se la variabile SubClass_C3_variabile_V3 non è  maggiore di  commento: {54,} 7 commento: {35,} e  se il controllo SubClass_C3_controllo_C2 è  uguale a  True  commento: {36,} o  se il timer SubClass_C3_timer_T7 è attivo commento: {36,} o  se il timer SubClass_C3_timer_T3 è scaduto, commento: {71,}Decrementa il contatore SubClass_C3_contatore_Co9
    
       
     commento: {43,}  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C3_lista_L8 è disattivo commento: {37,} o  se la variabile SubClass_C3_variabile_V10 non è  uguale a  False  commento: {38,} e  se il contatore SubClass_C3_contatore_Co9 è  uguale a  commento: {53,} 12 commento: {34,} o  se il parametro SubClass_C3_parametro_P4 non è  diverso da  commento: {56,} 1, commento: {68,}Attiva il timer SubClass_C3_timer_T7
    
     ,altrimenti  commento: {71,}Decrementa il contatore SubClass_C3_contatore_Co5
    
    
      se la macro  SubClass_C3_macrova_M2 ( con argomento_a1   uguale a RossoGiallox ,argomento_a8   uguale a c120  e argomento_a10   uguale a spento )   è  uguale a  True  commento: {40,} ,  Applica gli effetti
           della macro SubClass_C3_macroef_M4  commento: {73,}
    
     ,altrimenti  commento: {69,}Disattiva il timer SubClass_C3_timer_T7
    
    
     commento: {43,}  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  commento: {105,} è disattivo, commento: {69,}Disattiva il timer SubClass_C3_timer_T7
    
       
    
    }
*/
static inline void L_P1__Effec26(instance_id_t const my_id)
{
    
    //  *43,*  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  *105,* è disattivo, *70,*Incrementa il contatore SubClass_C3_contatore_Co3
    //   ,altrimenti   Applica gli effetti
    //         della macro SubClass_C3_macroef_M2
    bool res_ForAllPredicateNotEmpty_0 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl49Length(my_id); ++i)
    {
    L_P1__Recor1 it = L_P1__GetRecSubcl49(my_id,i);
    bool res_ImpliesLogicOp_1 = true;
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && Timer_Disattivo(L_P1__GetMainc40(it.mainc48)));
    res_ForAllPredicateNotEmpty_0 = res_ImpliesLogicOp_1;
    if(!res_ForAllPredicateNotEmpty_0) {break;}
    }
    if(res_ForAllPredicateNotEmpty_0){
    
    Counter_Incr(L_P1__GetSubcl92(my_id));
    }else{
    
    L_P1__Macro24(my_id);
    }
    
    //  *73,*
    //   *37,*  se la variabile SubClass_C3_variabile_V3 non è  maggiore di  *54,* 7 *35,* e  se il controllo SubClass_C3_controllo_C2 è  uguale a  True  *36,* o  se il timer SubClass_C3_timer_T7 è attivo *36,* o  se il timer SubClass_C3_timer_T3 è scaduto, *71,*Decrementa il contatore SubClass_C3_contatore_Co9
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_AndLogicOP_4 = true;
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetSubcl75(my_id) > 7u));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_5);
    res_AndLogicOP_4 = (res_AndLogicOP_4 && (L_P1__GetInSubcl46(my_id) == true));
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_AndLogicOP_4);
    res_OrLogicOP_3 = (res_OrLogicOP_3 || Timer_Attivo(L_P1__GetSubcl91(my_id)));
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    res_OrLogicOP_2 = (res_OrLogicOP_2 || Timer_Scaduto(L_P1__GetSubcl89(my_id)));
    
    if(res_OrLogicOP_2){
    
    Counter_Decr(L_P1__GetSubcl94(my_id));
    }
    
    //  *43,*  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C3_lista_L8 è disattivo *37,* o  se la variabile SubClass_C3_variabile_V10 non è  uguale a  False  *38,* e  se il contatore SubClass_C3_contatore_Co9 è  uguale a  *53,* 12 *34,* o  se il parametro SubClass_C3_parametro_P4 non è  diverso da  *56,* 1, *68,*Attiva il timer SubClass_C3_timer_T7
    //   ,altrimenti  *71,*Decrementa il contatore SubClass_C3_contatore_Co5
    bool res_OrLogicOP_6 = false;
    bool res_OrLogicOP_7 = false;
    bool res_ForAllPredicate_8 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl50Length(my_id); ++i)
    {
    L_P1__Recor2 it = L_P1__GetRecSubcl50(my_id,i);
    bool res_ImpliesLogicOp_9 = true;
    res_ImpliesLogicOp_9 = (res_ImpliesLogicOp_9 && Timer_Disattivo(L_P1__GetMainc42(it.mainc49)));
    res_ForAllPredicate_8 = res_ImpliesLogicOp_9;
    if(!res_ForAllPredicate_8) {break;}
    }
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_ForAllPredicate_8);
    bool res_AndLogicOP_10 = true;
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (L_P1__GetSubcl74(my_id) == false));
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_NotLogicOP_11);
    res_AndLogicOP_10 = (res_AndLogicOP_10 && (Counter_GetValore(L_P1__GetSubcl94(my_id)) == 12u));
    
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_AndLogicOP_10);
    
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_OrLogicOP_7);
    bool res_NotLogicOP_12 = true;
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (L_P1__GetParamSubcl54(my_id) == 1u));
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! res_NotLogicOP_13);
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_NotLogicOP_12);
    
    if(res_OrLogicOP_6){
    
    Timer_Attiva(L_P1__GetSubcl91(my_id));
    }else{
    
    Counter_Decr(L_P1__GetSubcl93(my_id));
    }
    
    //  se la macro  SubClass_C3_macrova_M2 ( con argomento_a1   uguale a RossoGiallox ,argomento_a8   uguale a c120  e argomento_a10   uguale a spento )   è  uguale a  True  *40,* ,  Applica gli effetti
    //         della macro SubClass_C3_macroef_M4  *73,*
    //   ,altrimenti  *69,*Disattiva il timer SubClass_C3_timer_T7
    if((L_P1__Macro27(my_id,rossogiallo4,spento,c120) == true)){
    
    L_P1__Macro25(my_id);
    }else{
    
    Timer_Disattiva(L_P1__GetSubcl91(my_id));
    }
    
    //  *43,*  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  *105,* è disattivo, *69,*Disattiva il timer SubClass_C3_timer_T7
    bool res_ForAllPredicateNotEmpty_14 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl49Length(my_id); ++i)
    {
    L_P1__Recor1 it = L_P1__GetRecSubcl49(my_id,i);
    bool res_ImpliesLogicOp_15 = true;
    res_ImpliesLogicOp_15 = (res_ImpliesLogicOp_15 && Timer_Disattivo(L_P1__GetMainc40(it.mainc48)));
    res_ForAllPredicateNotEmpty_14 = res_ImpliesLogicOp_15;
    if(!res_ForAllPredicateNotEmpty_14) {break;}
    }
    if(res_ForAllPredicateNotEmpty_14){
    
    Timer_Disattiva(L_P1__GetSubcl91(my_id));
    }
}


/*
    CNL corrispondente:
    
    {
    
     commento: {37,}  se la variabile SubClass_C3_variabile_V10 è  uguale a  False  commento: {36,} o  se il timer SubClass_C3_timer_T7 è attivo,  Applica gli effetti
           della macro SubClass_C3_macroef_M5  commento: {73,}
    
     ,altrimenti   Applica gli effetti
           della macro SubClass_C3_macroef_M1  commento: {73,}
    
    
     commento: {110,}  se il ripristino del timer  SubClass_C3_restoreTI_TI2 è disattivo o  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro SubClass_C3_parametro_P4 non è  diverso da  commento: {56,} 7 commento: {36,} o  se il timer SubClass_C3_timer_T7 non è attivo commento: {38,} e  se il contatore SubClass_C3_contatore_Co5 è  diverso da  commento: {56,} 150 commento: {37,} e  se la variabile SubClass_C3_variabile_V8 non è  diverso da  True ,  Applica gli effetti
           della macro SubClass_C3_macroef_M1  commento: {73,}
    
       
    
    }
*/
static inline void L_P1__Effec27(instance_id_t const my_id)
{
    
    //  *37,*  se la variabile SubClass_C3_variabile_V10 è  uguale a  False  *36,* o  se il timer SubClass_C3_timer_T7 è attivo,  Applica gli effetti
    //         della macro SubClass_C3_macroef_M5  *73,*
    //   ,altrimenti   Applica gli effetti
    //         della macro SubClass_C3_macroef_M1
    bool res_OrLogicOP_0 = false;
    res_OrLogicOP_0 = (res_OrLogicOP_0 || (L_P1__GetSubcl74(my_id) == false));
    res_OrLogicOP_0 = (res_OrLogicOP_0 || Timer_Attivo(L_P1__GetSubcl91(my_id)));
    
    if(res_OrLogicOP_0){
    
    L_P1__Macro26(my_id);
    }else{
    
    L_P1__Macro22(my_id);
    }
    
    //  *73,*
    //   *110,*  se il ripristino del timer  SubClass_C3_restoreTI_TI2 è disattivo o  se il controllo ConsDef  è  uguale a FALSE  *34,* e  se il parametro SubClass_C3_parametro_P4 non è  diverso da  *56,* 7 *36,* o  se il timer SubClass_C3_timer_T7 non è attivo *38,* e  se il contatore SubClass_C3_contatore_Co5 è  diverso da  *56,* 150 *37,* e  se la variabile SubClass_C3_variabile_V8 non è  diverso da  True ,  Applica gli effetti
    //         della macro SubClass_C3_macroef_M1
    bool res_OrLogicOP_1 = false;
    bool res_OrLogicOP_2 = false;
    res_OrLogicOP_2 = (res_OrLogicOP_2 || Timer_Disattivo(L_P1__GetSubcl80(my_id)));
    bool res_AndLogicOP_3 = true;
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (L_P1__GetInConsd2(my_id) == false));
    bool res_NotLogicOP_4 = true;
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetParamSubcl54(my_id) == 7u));
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! res_NotLogicOP_5);
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_NotLogicOP_4);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_3);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_OrLogicOP_2);
    bool res_AndLogicOP_6 = true;
    bool res_AndLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! Timer_Attivo(L_P1__GetSubcl91(my_id)));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_8);
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (Counter_GetValore(L_P1__GetSubcl93(my_id)) == 150u));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_9);
    
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_AndLogicOP_7);
    bool res_NotLogicOP_10 = true;
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (L_P1__GetSubcl76(my_id) == true));
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! res_NotLogicOP_11);
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_10);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_6);
    
    if(res_OrLogicOP_1){
    
    L_P1__Macro22(my_id);
    }
}


/*
    CNL corrispondente:
    
    {
    
     commento: {37,}  se la variabile SubClass_C3_variabile_V8 è  uguale a  True  commento: {38,} e  se il contatore SubClass_C3_contatore_Co5 è  minore di  commento: {55,} 155123, commento: {66,} Assegna al comando SubClass_C3_comando_C5 il valore RossoVerde
    
       
     commento: {109,}  se il ripristino della variabile  SubClass_C3_restoreva_RV1 non è  uguale a  True  commento: {36,} o  se il timer SubClass_C3_timer_T7 è disattivo commento: {36,} e  se il timer SubClass_C3_timer_T7 non è disattivo commento: {35,} e  se il controllo SubClass_C3_controllo_C2 non è  uguale a  True  commento: {36,} e  se il timer SubClass_C3_timer_T10 è disattivo, commento: {67,} Assegna alla variabile SubClass_C3_variabile_V8 il valore  True 
    
     ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C3_variabile_V8 il valore  True 
    
    
      se la macro  SubClass_C3_macrova_M2 ( con argomento_a1   uguale a c120 ,argomento_a8   uguale a c120  e argomento_a10   uguale a RossoVerde )  non  è  uguale a  True  commento: {40,}  commento: {34,} e  se il parametro SubClass_C3_parametro_P4 non è  maggiore di  commento: {54,} 8, commento: {66,} Assegna al comando SubClass_C3_comando_C5 il valore RossoVerde
    
     ,altrimenti  commento: {66,} Assegna al comando SubClass_C3_comando_C1 il valore  True 
    
    
    
    }
*/
static inline void L_P1__Effec28(instance_id_t const my_id)
{
    
    //  *37,*  se la variabile SubClass_C3_variabile_V8 è  uguale a  True  *38,* e  se il contatore SubClass_C3_contatore_Co5 è  minore di  *55,* 155123, *66,* Assegna al comando SubClass_C3_comando_C5 il valore RossoVerde
    bool res_AndLogicOP_0 = true;
    res_AndLogicOP_0 = (res_AndLogicOP_0 && (L_P1__GetSubcl76(my_id) == true));
    res_AndLogicOP_0 = (res_AndLogicOP_0 && (Counter_GetValore(L_P1__GetSubcl93(my_id)) < 155123u));
    
    if(res_AndLogicOP_0){
    
    L_P1__SetOutSubcl44(my_id,rossoverde);
    }
    
    //  *109,*  se il ripristino della variabile  SubClass_C3_restoreva_RV1 non è  uguale a  True  *36,* o  se il timer SubClass_C3_timer_T7 è disattivo *36,* e  se il timer SubClass_C3_timer_T7 non è disattivo *35,* e  se il controllo SubClass_C3_controllo_C2 non è  uguale a  True  *36,* e  se il timer SubClass_C3_timer_T10 è disattivo, *67,* Assegna alla variabile SubClass_C3_variabile_V8 il valore  True 
    //   ,altrimenti  *67,* Assegna alla variabile SubClass_C3_variabile_V8 il valore  True
    bool res_OrLogicOP_1 = false;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (L_P1__GetSubcl73(my_id) == true));
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_NotLogicOP_2);
    bool res_AndLogicOP_3 = true;
    bool res_AndLogicOP_4 = true;
    bool res_AndLogicOP_5 = true;
    res_AndLogicOP_5 = (res_AndLogicOP_5 && Timer_Disattivo(L_P1__GetSubcl91(my_id)));
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! Timer_Disattivo(L_P1__GetSubcl91(my_id)));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_6);
    
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_AndLogicOP_5);
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetInSubcl46(my_id) == true));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_7);
    
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_AndLogicOP_4);
    res_AndLogicOP_3 = (res_AndLogicOP_3 && Timer_Disattivo(L_P1__GetSubcl87(my_id)));
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_3);
    
    if(res_OrLogicOP_1){
    
    L_P1__SetSubcl76(my_id,true);
    }else{
    
    L_P1__SetSubcl76(my_id,true);
    }
    
    //  se la macro  SubClass_C3_macrova_M2 ( con argomento_a1   uguale a c120 ,argomento_a8   uguale a c120  e argomento_a10   uguale a RossoVerde )  non  è  uguale a  True  *40,*  *34,* e  se il parametro SubClass_C3_parametro_P4 non è  maggiore di  *54,* 8, *66,* Assegna al comando SubClass_C3_comando_C5 il valore RossoVerde
    //   ,altrimenti  *66,* Assegna al comando SubClass_C3_comando_C1 il valore  True
    bool res_AndLogicOP_8 = true;
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__Macro27(my_id,c120,rossoverde,c120) == true));
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_9);
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__GetParamSubcl54(my_id) > 8u));
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_10);
    
    if(res_AndLogicOP_8){
    
    L_P1__SetOutSubcl44(my_id,rossoverde);
    }else{
    
    L_P1__SetOutSubcl43(my_id,true);
    }
}


/*
    CNL corrispondente:
    
    {
    
     commento: {37,}  se la variabile SubClass_C3_variabile_V3 è  uguale a  commento: {53,} 6 commento: {37,} o  se la variabile SubClass_C3_variabile_V3 è  diverso da  commento: {56,} 6 commento: {36,} e  se il timer SubClass_C3_timer_T2 è disattivo commento: {37,} e  se la variabile SubClass_C3_variabile_V3 non è  uguale a  commento: {53,} 1, commento: {66,} Assegna al comando SubClass_C3_comando_C1 il valore  False 
    
     ,altrimenti   Applica gli effetti
           della macro SubClass_C3_macroef_M5  commento: {73,}
    
    
    
    }
*/
static inline void L_P1__Effec29(instance_id_t const my_id)
{
    
    //  *37,*  se la variabile SubClass_C3_variabile_V3 è  uguale a  *53,* 6 *37,* o  se la variabile SubClass_C3_variabile_V3 è  diverso da  *56,* 6 *36,* e  se il timer SubClass_C3_timer_T2 è disattivo *37,* e  se la variabile SubClass_C3_variabile_V3 non è  uguale a  *53,* 1, *66,* Assegna al comando SubClass_C3_comando_C1 il valore  False 
    //   ,altrimenti   Applica gli effetti
    //         della macro SubClass_C3_macroef_M5
    bool res_OrLogicOP_0 = false;
    res_OrLogicOP_0 = (res_OrLogicOP_0 || (L_P1__GetSubcl75(my_id) == 6u));
    bool res_AndLogicOP_1 = true;
    bool res_AndLogicOP_2 = true;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__GetSubcl75(my_id) == 6u));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_3);
    res_AndLogicOP_2 = (res_AndLogicOP_2 && Timer_Disattivo(L_P1__GetSubcl88(my_id)));
    
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_AndLogicOP_2);
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetSubcl75(my_id) == 1u));
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_4);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_1);
    
    if(res_OrLogicOP_0){
    
    L_P1__SetOutSubcl43(my_id,false);
    }else{
    
    L_P1__Macro26(my_id);
    }
}


/*
    CNL corrispondente:
     { commento: {109,}  se il ripristino della variabile  SubClass_C3_restoreva_RV1 è  uguale a  True  commento: {34,} o  se il parametro SubClass_C3_parametro_P4 è  maggiore di  commento: {54,} 7 commento: {34,} e  se il parametro SubClass_C3_parametro_P4 è  minore di  commento: {55,} 10 commento: {36,} o  se il timer SubClass_C3_timer_T7 non è attivo e  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} o  se il contatore SubClass_C3_contatore_Co5 è  diverso da  commento: {56,} 141, commento: {70,}Incrementa il contatore SubClass_C3_contatore_Co3
    
     ,altrimenti   Applica gli effetti
           della macro SubClass_C3_macroef_M4  commento: {73,}
    
    
     commento: {44,}  se  MainClass_C1_variabile_V2 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  uguale a  True  commento: {36,} e  se il timer SubClass_C3_timer_T5 è scaduto commento: {36,} e  se il timer SubClass_C3_timer_T2 non è attivo commento: {35,} o  se il controllo SubClass_C3_controllo_C2 è  diverso da  True  commento: {37,} e  se la variabile SubClass_C3_variabile_V10 non è  uguale a  False  commento: {36,} o  se il timer SubClass_C3_timer_T2 è disattivo, commento: {69,}Disattiva il timer SubClass_C3_timer_T2
    
       
      se il ripristino dello stato  non è  uguale a  commento: {53,}  state1  commento: {107,} commento: {38,} e  se il contatore SubClass_C3_contatore_Co3 non è  diverso da  commento: {56,} 1523 commento: {34,} e  se il parametro SubClass_C3_parametro_P1 non è  uguale a  False  commento: {35,} e  se il controllo SubClass_C3_controllo_C6 è  uguale a RossoVerde commento: {34,} e  se il parametro SubClass_C3_parametro_P9 è  minore di  commento: {55,} 8 commento: {35,} o  se il controllo SubClass_C3_controllo_C4 è  uguale a RossoVerde, commento: {67,} Assegna alla variabile SubClass_C3_variabile_V3 il valore 2
    
     ,altrimenti  commento: {68,}Attiva il timer SubClass_C3_timer_T5
    
    
     commento: {43,}  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C3_lista_L10 è disattivo commento: {38,} o  se il contatore SubClass_C3_contatore_Co3 è  uguale a  commento: {53,} 1504 commento: {37,} e  se la variabile SubClass_C3_variabile_V3 è  uguale a  commento: {53,} 3 commento: {38,} e  se il contatore SubClass_C3_contatore_Co9 è  minore di  commento: {55,} 1451 commento: {38,} o  se il contatore SubClass_C3_contatore_Co5 non è  maggiore di  commento: {54,} 12230 e  se il controllo ConsDef  è  uguale a FALSE , commento: {68,}Attiva il timer SubClass_C3_timer_T7
    
     ,altrimenti   Applica gli effetti
           della macro SubClass_C3_macroef_M4  commento: {73,}
    
    
     }
*/
static inline void L_P1__Effec30(instance_id_t const my_id)
{
    
    //  *109,*  se il ripristino della variabile  SubClass_C3_restoreva_RV1 è  uguale a  True  *34,* o  se il parametro SubClass_C3_parametro_P4 è  maggiore di  *54,* 7 *34,* e  se il parametro SubClass_C3_parametro_P4 è  minore di  *55,* 10 *36,* o  se il timer SubClass_C3_timer_T7 non è attivo e  se il controllo ConsDef  è  uguale a FALSE  *38,* o  se il contatore SubClass_C3_contatore_Co5 è  diverso da  *56,* 141, *70,*Incrementa il contatore SubClass_C3_contatore_Co3
    //   ,altrimenti   Applica gli effetti
    //         della macro SubClass_C3_macroef_M4
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_OrLogicOP_2 = false;
    res_OrLogicOP_2 = (res_OrLogicOP_2 || (L_P1__GetSubcl73(my_id) == true));
    bool res_AndLogicOP_3 = true;
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (L_P1__GetParamSubcl54(my_id) > 7u));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (L_P1__GetParamSubcl54(my_id) < 10u));
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_3);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_OrLogicOP_2);
    bool res_AndLogicOP_4 = true;
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! Timer_Attivo(L_P1__GetSubcl91(my_id)));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_5);
    res_AndLogicOP_4 = (res_AndLogicOP_4 && (L_P1__GetInConsd2(my_id) == false));
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_4);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (Counter_GetValore(L_P1__GetSubcl93(my_id)) == 141u));
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_6);
    
    if(res_OrLogicOP_0){
    
    Counter_Incr(L_P1__GetSubcl92(my_id));
    }else{
    
    L_P1__Macro25(my_id);
    }
    
    //  *73,*
    //   *44,*  se  MainClass_C1_variabile_V2 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  uguale a  True  *36,* e  se il timer SubClass_C3_timer_T5 è scaduto *36,* e  se il timer SubClass_C3_timer_T2 non è attivo *35,* o  se il controllo SubClass_C3_controllo_C2 è  diverso da  True  *37,* e  se la variabile SubClass_C3_variabile_V10 non è  uguale a  False  *36,* o  se il timer SubClass_C3_timer_T2 è disattivo, *69,*Disattiva il timer SubClass_C3_timer_T2
    bool res_OrLogicOP_7 = false;
    bool res_OrLogicOP_8 = false;
    bool res_AndLogicOP_9 = true;
    bool res_AndLogicOP_10 = true;
    bool res_ForAllPredicate_11 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl50Length(my_id); ++i)
    {
    L_P1__Recor2 it = L_P1__GetRecSubcl50(my_id,i);
    bool res_ImpliesLogicOp_12 = true;
    res_ImpliesLogicOp_12 = (res_ImpliesLogicOp_12 && (L_P1__GetMainc33(it.mainc49) == true));
    res_ForAllPredicate_11 = res_ImpliesLogicOp_12;
    if(!res_ForAllPredicate_11) {break;}
    }
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_ForAllPredicate_11);
    res_AndLogicOP_10 = (res_AndLogicOP_10 && Timer_Scaduto(L_P1__GetSubcl90(my_id)));
    
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_AndLogicOP_10);
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! Timer_Attivo(L_P1__GetSubcl88(my_id)));
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_NotLogicOP_13);
    
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_AndLogicOP_9);
    bool res_AndLogicOP_14 = true;
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (L_P1__GetInSubcl46(my_id) == true));
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_NotLogicOP_15);
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (L_P1__GetSubcl74(my_id) == false));
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_NotLogicOP_16);
    
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_AndLogicOP_14);
    
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_OrLogicOP_8);
    res_OrLogicOP_7 = (res_OrLogicOP_7 || Timer_Disattivo(L_P1__GetSubcl88(my_id)));
    
    if(res_OrLogicOP_7){
    
    Timer_Disattiva(L_P1__GetSubcl88(my_id));
    }
    
    //  se il ripristino dello stato  non è  uguale a  *53,*  state1  *107,* *38,* e  se il contatore SubClass_C3_contatore_Co3 non è  diverso da  *56,* 1523 *34,* e  se il parametro SubClass_C3_parametro_P1 non è  uguale a  False  *35,* e  se il controllo SubClass_C3_controllo_C6 è  uguale a RossoVerde *34,* e  se il parametro SubClass_C3_parametro_P9 è  minore di  *55,* 8 *35,* o  se il controllo SubClass_C3_controllo_C4 è  uguale a RossoVerde, *67,* Assegna alla variabile SubClass_C3_variabile_V3 il valore 2
    //   ,altrimenti  *68,*Attiva il timer SubClass_C3_timer_T5
    bool res_OrLogicOP_17 = false;
    bool res_AndLogicOP_18 = true;
    bool res_AndLogicOP_19 = true;
    bool res_AndLogicOP_20 = true;
    bool res_AndLogicOP_21 = true;
    bool res_NotLogicOP_22 = true;
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! (L_P1__GetStato5(my_id) == C3_St_state));
    res_AndLogicOP_21 = (res_AndLogicOP_21 && res_NotLogicOP_22);
    bool res_NotLogicOP_23 = true;
    bool res_NotLogicOP_24 = true;
    res_NotLogicOP_24 = (res_NotLogicOP_24 && ! (Counter_GetValore(L_P1__GetSubcl92(my_id)) == 1523u));
    res_NotLogicOP_23 = (res_NotLogicOP_23 && ! res_NotLogicOP_24);
    res_AndLogicOP_21 = (res_AndLogicOP_21 && res_NotLogicOP_23);
    
    res_AndLogicOP_20 = (res_AndLogicOP_20 && res_AndLogicOP_21);
    bool res_NotLogicOP_25 = true;
    res_NotLogicOP_25 = (res_NotLogicOP_25 && ! (L_P1__GetParamSubcl51(my_id) == false));
    res_AndLogicOP_20 = (res_AndLogicOP_20 && res_NotLogicOP_25);
    
    res_AndLogicOP_19 = (res_AndLogicOP_19 && res_AndLogicOP_20);
    res_AndLogicOP_19 = (res_AndLogicOP_19 && (L_P1__GetInSubcl48(my_id) == rossoverde));
    
    res_AndLogicOP_18 = (res_AndLogicOP_18 && res_AndLogicOP_19);
    res_AndLogicOP_18 = (res_AndLogicOP_18 && (L_P1__GetParamSubcl55(my_id) < 8u));
    
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_AndLogicOP_18);
    res_OrLogicOP_17 = (res_OrLogicOP_17 || (L_P1__GetInSubcl47(my_id) == rossoverde));
    
    if(res_OrLogicOP_17){
    
    L_P1__SetSubcl75(my_id,2u);
    }else{
    
    Timer_Attiva(L_P1__GetSubcl90(my_id));
    }
    
    //  *43,*  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C3_lista_L10 è disattivo *38,* o  se il contatore SubClass_C3_contatore_Co3 è  uguale a  *53,* 1504 *37,* e  se la variabile SubClass_C3_variabile_V3 è  uguale a  *53,* 3 *38,* e  se il contatore SubClass_C3_contatore_Co9 è  minore di  *55,* 1451 *38,* o  se il contatore SubClass_C3_contatore_Co5 non è  maggiore di  *54,* 12230 e  se il controllo ConsDef  è  uguale a FALSE , *68,*Attiva il timer SubClass_C3_timer_T7
    //   ,altrimenti   Applica gli effetti
    //         della macro SubClass_C3_macroef_M4
    bool res_OrLogicOP_26 = false;
    bool res_OrLogicOP_27 = false;
    bool res_ForAllPredicate_28 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl49Length(my_id); ++i)
    {
    L_P1__Recor1 it = L_P1__GetRecSubcl49(my_id,i);
    bool res_ImpliesLogicOp_29 = true;
    res_ImpliesLogicOp_29 = (res_ImpliesLogicOp_29 && Timer_Disattivo(L_P1__GetMainc39(it.mainc48)));
    res_ForAllPredicate_28 = res_ImpliesLogicOp_29;
    if(!res_ForAllPredicate_28) {break;}
    }
    res_OrLogicOP_27 = (res_OrLogicOP_27 || res_ForAllPredicate_28);
    bool res_AndLogicOP_30 = true;
    bool res_AndLogicOP_31 = true;
    res_AndLogicOP_31 = (res_AndLogicOP_31 && (Counter_GetValore(L_P1__GetSubcl92(my_id)) == 1504u));
    res_AndLogicOP_31 = (res_AndLogicOP_31 && (L_P1__GetSubcl75(my_id) == 3u));
    
    res_AndLogicOP_30 = (res_AndLogicOP_30 && res_AndLogicOP_31);
    res_AndLogicOP_30 = (res_AndLogicOP_30 && (Counter_GetValore(L_P1__GetSubcl94(my_id)) < 1451u));
    
    res_OrLogicOP_27 = (res_OrLogicOP_27 || res_AndLogicOP_30);
    
    res_OrLogicOP_26 = (res_OrLogicOP_26 || res_OrLogicOP_27);
    bool res_AndLogicOP_32 = true;
    bool res_NotLogicOP_33 = true;
    res_NotLogicOP_33 = (res_NotLogicOP_33 && ! (Counter_GetValore(L_P1__GetSubcl93(my_id)) > 12230u));
    res_AndLogicOP_32 = (res_AndLogicOP_32 && res_NotLogicOP_33);
    res_AndLogicOP_32 = (res_AndLogicOP_32 && (L_P1__GetInConsd2(my_id) == false));
    
    res_OrLogicOP_26 = (res_OrLogicOP_26 || res_AndLogicOP_32);
    
    if(res_OrLogicOP_26){
    
    Timer_Attiva(L_P1__GetSubcl91(my_id));
    }else{
    
    L_P1__Macro25(my_id);
    }
}


/*
    CNL corrispondente:
     { commento: {42,}  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  commento: {105,} è  diverso da RossoGialloaVerdea commento: {35,} o  se il controllo SubClass_C3_controllo_C2 è  diverso da  False ,  Applica gli effetti
           della macro SubClass_C3_macroef_M1  commento: {73,}
    
       
     commento: {34,}  se il parametro SubClass_C3_parametro_P1 è  diverso da  True  commento: {36,} o  se il timer SubClass_C3_timer_T5 è disattivo commento: {35,} o  se il controllo SubClass_C3_controllo_C10 non è  uguale a c120x, commento: {67,} Assegna alla variabile SubClass_C3_variabile_V3 il valore 3
    
     ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C3_variabile_V3 il valore 8
    
    
      se il ripristino dello stato  è  uguale a  commento: {53,}  state1  commento: {107,}, commento: {69,}Disattiva il timer SubClass_C3_timer_T2
    
     ,altrimenti  commento: {69,}Disattiva il timer SubClass_C3_timer_T2
    
    
     }
*/
static inline void L_P1__Effec31(instance_id_t const my_id)
{
    
    //  *42,*  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  *105,* è  diverso da RossoGialloaVerdea *35,* o  se il controllo SubClass_C3_controllo_C2 è  diverso da  False ,  Applica gli effetti
    //         della macro SubClass_C3_macroef_M1
    bool res_OrLogicOP_0 = false;
    bool res_ForAllPredicateNotEmpty_1 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl49Length(my_id); ++i)
    {
    L_P1__Recor1 it = L_P1__GetRecSubcl49(my_id,i);
    bool res_ImpliesLogicOp_2 = true;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__GetInMainc5(it.mainc48) == rossogiallo));
    res_ImpliesLogicOp_2 = (res_ImpliesLogicOp_2 && res_NotLogicOP_3);
    res_ForAllPredicateNotEmpty_1 = res_ImpliesLogicOp_2;
    if(!res_ForAllPredicateNotEmpty_1) {break;}
    }
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_ForAllPredicateNotEmpty_1);
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetInSubcl46(my_id) == false));
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_4);
    
    if(res_OrLogicOP_0){
    
    L_P1__Macro22(my_id);
    }
    
    //  *73,*
    //     
    //   *34,*  se il parametro SubClass_C3_parametro_P1 è  diverso da  True  *36,* o  se il timer SubClass_C3_timer_T5 è disattivo *35,* o  se il controllo SubClass_C3_controllo_C10 non è  uguale a c120x, *67,* Assegna alla variabile SubClass_C3_variabile_V3 il valore 3
    //   ,altrimenti  *67,* Assegna alla variabile SubClass_C3_variabile_V3 il valore 8
    bool res_OrLogicOP_5 = false;
    bool res_OrLogicOP_6 = false;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetParamSubcl51(my_id) == true));
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_NotLogicOP_7);
    res_OrLogicOP_6 = (res_OrLogicOP_6 || Timer_Disattivo(L_P1__GetSubcl90(my_id)));
    
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_OrLogicOP_6);
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetInSubcl45(my_id) == c120x));
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_NotLogicOP_8);
    
    if(res_OrLogicOP_5){
    
    L_P1__SetSubcl75(my_id,3u);
    }else{
    
    L_P1__SetSubcl75(my_id,8u);
    }
    
    //  se il ripristino dello stato  è  uguale a  *53,*  state1  *107,*, *69,*Disattiva il timer SubClass_C3_timer_T2
    //   ,altrimenti  *69,*Disattiva il timer SubClass_C3_timer_T2
    if((L_P1__GetStato5(my_id) == C3_St_state)){
    
    Timer_Disattiva(L_P1__GetSubcl88(my_id));
    }else{
    
    Timer_Disattiva(L_P1__GetSubcl88(my_id));
    }
}


/*
    CNL corrispondente:
     { commento: {44,}  se  MainClass_C1_variabile_V10 del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  commento: {105,} è  diverso da  False  commento: {38,} e  se il contatore SubClass_C3_contatore_Co9 è  minore di  commento: {55,} 12 commento: {34,} o  se il parametro SubClass_C3_parametro_P2 non è  uguale a c120x, commento: {67,} Assegna alla variabile SubClass_C3_variabile_V8 il valore  False 
    
       
      se la macro  SubClass_C3_macrova_M6 ( con argomento_a5   uguale a True ,argomento_a9   uguale a c120x  e argomento_a6   uguale a RossoVerde )   è  diverso da AC commento: {40,}  commento: {34,} e  se il parametro SubClass_C3_parametro_P4 è  diverso da  commento: {56,} 6 commento: {37,} o  se la variabile SubClass_C3_variabile_V8 non è  uguale a  True  commento: {37,} o  se la variabile SubClass_C3_variabile_V8 è  diverso da  True  commento: {37,} e  se la variabile SubClass_C3_variabile_V8 è  diverso da  False , commento: {70,}Incrementa il contatore SubClass_C3_contatore_Co5
    
     ,altrimenti   Applica gli effetti
           della macro SubClass_C3_macroef_M1  commento: {73,}
    
    
     commento: {34,}  se il parametro SubClass_C3_parametro_P4 non è  minore di  commento: {55,} 3,  commento: {41,}  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  commento: {105,} è  diverso da  True , commento: {88,} quando  commento: {45,}    MainClass_C1_contatore_Co8 del campo  MainClass_C1     commento: {105,} è  uguale a  commento: {53,} 1145, commento: {66,} Assegna al comando SubClass_C3_comando_C5 il valore RossoVerde
    
     ,altrimenti  commento: {71,}Decrementa il contatore SubClass_C3_contatore_Co3
    
    
     commento: {45,}  se  MainClass_C1_contatore_Co8 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  commento: {105,} è  maggiore di  commento: {54,} 111230 commento: {34,} e  se il parametro SubClass_C3_parametro_P4 è  maggiore di  commento: {54,} 3 commento: {38,} o  se il contatore SubClass_C3_contatore_Co3 è  maggiore di  commento: {54,} 154, commento: {66,} Assegna al comando SubClass_C3_comando_C5 il valore RossoVerde
    
     ,altrimenti  commento: {69,}Disattiva il timer SubClass_C3_timer_T7
    
    
     }
*/
static inline void L_P1__Effec32(instance_id_t const my_id)
{
    
    //  *44,*  se  MainClass_C1_variabile_V10 del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  *105,* è  diverso da  False  *38,* e  se il contatore SubClass_C3_contatore_Co9 è  minore di  *55,* 12 *34,* o  se il parametro SubClass_C3_parametro_P2 non è  uguale a c120x, *67,* Assegna alla variabile SubClass_C3_variabile_V8 il valore  False
    bool res_OrLogicOP_0 = false;
    bool res_AndLogicOP_1 = true;
    bool res_ForAllPredicateNotEmpty_2 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl49Length(my_id); ++i)
    {
    L_P1__Recor1 it = L_P1__GetRecSubcl49(my_id,i);
    bool res_ImpliesLogicOp_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetMainc32(it.mainc48) == false));
    res_ImpliesLogicOp_3 = (res_ImpliesLogicOp_3 && res_NotLogicOP_4);
    res_ForAllPredicateNotEmpty_2 = res_ImpliesLogicOp_3;
    if(!res_ForAllPredicateNotEmpty_2) {break;}
    }
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_ForAllPredicateNotEmpty_2);
    res_AndLogicOP_1 = (res_AndLogicOP_1 && (Counter_GetValore(L_P1__GetSubcl94(my_id)) < 12u));
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_1);
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetParamSubcl52(my_id) == c120x));
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_5);
    
    if(res_OrLogicOP_0){
    
    L_P1__SetSubcl76(my_id,false);
    }
    
    //  se la macro  SubClass_C3_macrova_M6 ( con argomento_a5   uguale a True ,argomento_a9   uguale a c120x  e argomento_a6   uguale a RossoVerde )   è  diverso da AC *40,*  *34,* e  se il parametro SubClass_C3_parametro_P4 è  diverso da  *56,* 6 *37,* o  se la variabile SubClass_C3_variabile_V8 non è  uguale a  True  *37,* o  se la variabile SubClass_C3_variabile_V8 è  diverso da  True  *37,* e  se la variabile SubClass_C3_variabile_V8 è  diverso da  False , *70,*Incrementa il contatore SubClass_C3_contatore_Co5
    //   ,altrimenti   Applica gli effetti
    //         della macro SubClass_C3_macroef_M1
    bool res_OrLogicOP_6 = false;
    bool res_OrLogicOP_7 = false;
    bool res_AndLogicOP_8 = true;
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__Macro28(my_id,true,rossoverde,c120x) == ac));
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_9);
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__GetParamSubcl54(my_id) == 6u));
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_10);
    
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_AndLogicOP_8);
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (L_P1__GetSubcl76(my_id) == true));
    res_OrLogicOP_7 = (res_OrLogicOP_7 || res_NotLogicOP_11);
    
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_OrLogicOP_7);
    bool res_AndLogicOP_12 = true;
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (L_P1__GetSubcl76(my_id) == true));
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_NotLogicOP_13);
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1__GetSubcl76(my_id) == false));
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_NotLogicOP_14);
    
    res_OrLogicOP_6 = (res_OrLogicOP_6 || res_AndLogicOP_12);
    
    if(res_OrLogicOP_6){
    
    Counter_Incr(L_P1__GetSubcl93(my_id));
    }else{
    
    L_P1__Macro22(my_id);
    }
    
    //  *73,*
    //   *34,*  se il parametro SubClass_C3_parametro_P4 non è  minore di  *55,* 3,  *41,*  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  *105,* è  diverso da  True , *88,* quando  *45,*    MainClass_C1_contatore_Co8 del campo  MainClass_C1     *105,* è  uguale a  *53,* 1145, *66,* Assegna al comando SubClass_C3_comando_C5 il valore RossoVerde
    //   ,altrimenti  *71,*Decrementa il contatore SubClass_C3_contatore_Co3
    bool res_AndLogicOP_15 = true;
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! (L_P1__GetParamSubcl54(my_id) < 3u));
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_NotLogicOP_16);
    bool res_ForAllPredicateNotEmpty_17 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl49Length(my_id); ++i)
    {
    L_P1__Recor1 it = L_P1__GetRecSubcl49(my_id,i);
    bool res_ImpliesLogicOp_18 = true;
    if((Counter_GetValore(L_P1__GetMainc45(it.mainc48)) == 1145u)){
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (L_P1__GetParamMainc9(it.mainc48) == true));
    res_ImpliesLogicOp_18 = (res_ImpliesLogicOp_18 && res_NotLogicOP_19);
    res_ForAllPredicateNotEmpty_17 = res_ImpliesLogicOp_18;
    if(!res_ForAllPredicateNotEmpty_17) {break;}
    }
    }
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_ForAllPredicateNotEmpty_17);
    
    if(res_AndLogicOP_15){
    
    L_P1__SetOutSubcl44(my_id,rossoverde);
    }else{
    
    Counter_Decr(L_P1__GetSubcl92(my_id));
    }
    
    //  *45,*  se  MainClass_C1_contatore_Co8 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  *105,* è  maggiore di  *54,* 111230 *34,* e  se il parametro SubClass_C3_parametro_P4 è  maggiore di  *54,* 3 *38,* o  se il contatore SubClass_C3_contatore_Co3 è  maggiore di  *54,* 154, *66,* Assegna al comando SubClass_C3_comando_C5 il valore RossoVerde
    //   ,altrimenti  *69,*Disattiva il timer SubClass_C3_timer_T7
    bool res_OrLogicOP_20 = false;
    bool res_AndLogicOP_21 = true;
    bool res_ForAllPredicateNotEmpty_22 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl50Length(my_id); ++i)
    {
    L_P1__Recor2 it = L_P1__GetRecSubcl50(my_id,i);
    bool res_ImpliesLogicOp_23 = true;
    res_ImpliesLogicOp_23 = (res_ImpliesLogicOp_23 && (Counter_GetValore(L_P1__GetMainc45(it.mainc49)) > 111230u));
    res_ForAllPredicateNotEmpty_22 = res_ImpliesLogicOp_23;
    if(!res_ForAllPredicateNotEmpty_22) {break;}
    }
    res_AndLogicOP_21 = (res_AndLogicOP_21 && res_ForAllPredicateNotEmpty_22);
    res_AndLogicOP_21 = (res_AndLogicOP_21 && (L_P1__GetParamSubcl54(my_id) > 3u));
    
    res_OrLogicOP_20 = (res_OrLogicOP_20 || res_AndLogicOP_21);
    res_OrLogicOP_20 = (res_OrLogicOP_20 || (Counter_GetValore(L_P1__GetSubcl92(my_id)) > 154u));
    
    if(res_OrLogicOP_20){
    
    L_P1__SetOutSubcl44(my_id,rossoverde);
    }else{
    
    Timer_Disattiva(L_P1__GetSubcl91(my_id));
    }
}


/*
    CNL corrispondente:
     {  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro SubClass_C3_parametro_P2 è  uguale a c120x commento: {35,} e  se il controllo SubClass_C3_controllo_C6 non è  uguale a RossoVerde commento: {38,} e  se il contatore SubClass_C3_contatore_Co9 non è  maggiore di  commento: {54,} 12 commento: {38,} o  se il contatore SubClass_C3_contatore_Co3 è  minore di  commento: {55,} 135 commento: {37,} e  se la variabile SubClass_C3_variabile_V8 non è  diverso da  False , commento: {71,}Decrementa il contatore SubClass_C3_contatore_Co3
    
     ,altrimenti   Applica gli effetti
           della macro SubClass_C3_macroef_M1  commento: {73,}
    
    
      se il controllo ConsDef  è  uguale a FALSE ,  commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  commento: {105,} è  uguale a  commento: {53,}  state1 , commento: {88,} quando  commento: {41,}   MainClass_C1_parametro_P3 del campo  MainClass_C1     è  uguale a  commento: {53,} 7 commento: {37,} e  se la variabile SubClass_C3_variabile_V8 è  uguale a  True  e  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} e  se il timer SubClass_C3_timer_T7 non è disattivo commento: {38,} e  se il contatore SubClass_C3_contatore_Co9 è  maggiore di  commento: {54,} 131, commento: {70,}Incrementa il contatore SubClass_C3_contatore_Co9
    
       
     }
*/
static inline void L_P1__Effec33(instance_id_t const my_id)
{
    
    //  se il controllo ConsDef  è  uguale a FALSE  *34,* e  se il parametro SubClass_C3_parametro_P2 è  uguale a c120x *35,* e  se il controllo SubClass_C3_controllo_C6 non è  uguale a RossoVerde *38,* e  se il contatore SubClass_C3_contatore_Co9 non è  maggiore di  *54,* 12 *38,* o  se il contatore SubClass_C3_contatore_Co3 è  minore di  *55,* 135 *37,* e  se la variabile SubClass_C3_variabile_V8 non è  diverso da  False , *71,*Decrementa il contatore SubClass_C3_contatore_Co3
    //   ,altrimenti   Applica gli effetti
    //         della macro SubClass_C3_macroef_M1
    bool res_OrLogicOP_0 = false;
    bool res_AndLogicOP_1 = true;
    bool res_AndLogicOP_2 = true;
    bool res_AndLogicOP_3 = true;
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (L_P1__GetInConsd2(my_id) == false));
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (L_P1__GetParamSubcl52(my_id) == c120x));
    
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_AndLogicOP_3);
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetInSubcl48(my_id) == rossoverde));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_4);
    
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_AndLogicOP_2);
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (Counter_GetValore(L_P1__GetSubcl94(my_id)) > 12u));
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_5);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_1);
    bool res_AndLogicOP_6 = true;
    res_AndLogicOP_6 = (res_AndLogicOP_6 && (Counter_GetValore(L_P1__GetSubcl92(my_id)) < 135u));
    bool res_NotLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetSubcl76(my_id) == false));
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! res_NotLogicOP_8);
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_7);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_6);
    
    if(res_OrLogicOP_0){
    
    Counter_Decr(L_P1__GetSubcl92(my_id));
    }else{
    
    L_P1__Macro22(my_id);
    }
    
    //  *73,*
    //    se il controllo ConsDef  è  uguale a FALSE ,  *111,*  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  *105,* è  uguale a  *53,*  state1 , *88,* quando  *41,*   MainClass_C1_parametro_P3 del campo  MainClass_C1     è  uguale a  *53,* 7 *37,* e  se la variabile SubClass_C3_variabile_V8 è  uguale a  True  e  se il controllo ConsDef  è  uguale a FALSE  *36,* e  se il timer SubClass_C3_timer_T7 non è disattivo *38,* e  se il contatore SubClass_C3_contatore_Co9 è  maggiore di  *54,* 131, *70,*Incrementa il contatore SubClass_C3_contatore_Co9
    bool res_AndLogicOP_9 = true;
    bool res_AndLogicOP_10 = true;
    bool res_AndLogicOP_11 = true;
    bool res_AndLogicOP_12 = true;
    bool res_AndLogicOP_13 = true;
    res_AndLogicOP_13 = (res_AndLogicOP_13 && (L_P1__GetInConsd2(my_id) == false));
    bool res_ForAllPredicateNotEmpty_14 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl50Length(my_id); ++i)
    {
    L_P1__Recor2 it = L_P1__GetRecSubcl50(my_id,i);
    bool res_ImpliesLogicOp_15 = true;
    if((L_P1__GetParamMainc7(it.mainc49) == 7u)){
    res_ImpliesLogicOp_15 = (res_ImpliesLogicOp_15 && (L_P1_C1_GetState(it.mainc49) == C1_St_state));
    res_ForAllPredicateNotEmpty_14 = res_ImpliesLogicOp_15;
    if(!res_ForAllPredicateNotEmpty_14) {break;}
    }
    }
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_ForAllPredicateNotEmpty_14);
    
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_AndLogicOP_13);
    res_AndLogicOP_12 = (res_AndLogicOP_12 && (L_P1__GetSubcl76(my_id) == true));
    
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_AndLogicOP_12);
    res_AndLogicOP_11 = (res_AndLogicOP_11 && (L_P1__GetInConsd2(my_id) == false));
    
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_AndLogicOP_11);
    bool res_NotLogicOP_16 = true;
    res_NotLogicOP_16 = (res_NotLogicOP_16 && ! Timer_Disattivo(L_P1__GetSubcl91(my_id)));
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_NotLogicOP_16);
    
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_AndLogicOP_10);
    res_AndLogicOP_9 = (res_AndLogicOP_9 && (Counter_GetValore(L_P1__GetSubcl94(my_id)) > 131u));
    
    if(res_AndLogicOP_9){
    
    Counter_Incr(L_P1__GetSubcl94(my_id));
    }
}


/*
    CNL corrispondente:
     { commento: {36,}  se il timer SubClass_C3_timer_T7 è disattivo commento: {34,} e  se il parametro SubClass_C3_parametro_P2 è  diverso da c120x commento: {34,} o  se il parametro SubClass_C3_parametro_P2 non è  uguale a c120x, commento: {66,} Assegna al comando SubClass_C3_comando_C5 il valore RossoVerde
    
     ,altrimenti  commento: {70,}Incrementa il contatore SubClass_C3_contatore_Co3
    
    
     commento: {35,}  se il controllo SubClass_C3_controllo_C10 è  diverso da c120x e  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} o  se il controllo SubClass_C3_controllo_C2 non è  uguale a  False  commento: {35,} e  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x commento: {36,} e  se il timer SubClass_C3_timer_T2 è disattivo, commento: {69,}Disattiva il timer SubClass_C3_timer_T10
    
     ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C3_variabile_V8 il valore  True 
    
    
     }
*/
static inline void L_P1__Effec34(instance_id_t const my_id)
{
    
    //  *36,*  se il timer SubClass_C3_timer_T7 è disattivo *34,* e  se il parametro SubClass_C3_parametro_P2 è  diverso da c120x *34,* o  se il parametro SubClass_C3_parametro_P2 non è  uguale a c120x, *66,* Assegna al comando SubClass_C3_comando_C5 il valore RossoVerde
    //   ,altrimenti  *70,*Incrementa il contatore SubClass_C3_contatore_Co3
    bool res_OrLogicOP_0 = false;
    bool res_AndLogicOP_1 = true;
    res_AndLogicOP_1 = (res_AndLogicOP_1 && Timer_Disattivo(L_P1__GetSubcl91(my_id)));
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (L_P1__GetParamSubcl52(my_id) == c120x));
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_2);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_1);
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__GetParamSubcl52(my_id) == c120x));
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_3);
    
    if(res_OrLogicOP_0){
    
    L_P1__SetOutSubcl44(my_id,rossoverde);
    }else{
    
    Counter_Incr(L_P1__GetSubcl92(my_id));
    }
    
    //  *35,*  se il controllo SubClass_C3_controllo_C10 è  diverso da c120x e  se il controllo ConsDef  è  uguale a FALSE  *35,* o  se il controllo SubClass_C3_controllo_C2 non è  uguale a  False  *35,* e  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x *36,* e  se il timer SubClass_C3_timer_T2 è disattivo, *69,*Disattiva il timer SubClass_C3_timer_T10
    //   ,altrimenti  *67,* Assegna alla variabile SubClass_C3_variabile_V8 il valore  True
    bool res_OrLogicOP_4 = false;
    bool res_AndLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetInSubcl45(my_id) == c120x));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_6);
    res_AndLogicOP_5 = (res_AndLogicOP_5 && (L_P1__GetInConsd2(my_id) == false));
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_AndLogicOP_5);
    bool res_AndLogicOP_7 = true;
    bool res_AndLogicOP_8 = true;
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetInSubcl46(my_id) == false));
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_9);
    res_AndLogicOP_8 = (res_AndLogicOP_8 && (L_P1__GetInSubcl45(my_id) == c120x));
    
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_AndLogicOP_8);
    res_AndLogicOP_7 = (res_AndLogicOP_7 && Timer_Disattivo(L_P1__GetSubcl88(my_id)));
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_AndLogicOP_7);
    
    if(res_OrLogicOP_4){
    
    Timer_Disattiva(L_P1__GetSubcl87(my_id));
    }else{
    
    L_P1__SetSubcl76(my_id,true);
    }
}



// ********** Definizione metodi **********

// Metodi standard

void L_P1_C3_Init(instance_id_t const my_id)
{
    // init variabili di stato
    L_P1__SetStato5(my_id, C3_St_Stato);
    L_P1__SetSubcl64(my_id, spento);
    L_P1__SetSubcl66(my_id, rossogiallo5);
    L_P1__SetSubcl68(my_id, 0);
    L_P1__SetSubcl70(my_id, false);
    L_P1__SetSubcl72(my_id, false);
    L_P1__SetSubcl73(my_id, false);
    L_P1__SetSubcl74(my_id, false);
    L_P1__SetSubcl75(my_id, 0);
    L_P1__SetSubcl76(my_id, false);
    // init controlli precedenti
    L_P1__SetSubcl57(my_id, rossoverde);
    L_P1__SetSubcl59(my_id, true);
    L_P1__SetSubcl61(my_id, rossogiallo4);
    L_P1__SetSubcl63(my_id, false);
    // init Timer e Counter
    Timer_AggmInit(L_P1__GetSubcl77(my_id), true, CLASS_L_P1_C3_ID, my_id, L_P1__subcl77_ID);
    Timer_Init(L_P1__GetSubcl77(my_id), 351000);
    Timer_AggmInit(L_P1__GetSubcl78(my_id), true, CLASS_L_P1_C3_ID, my_id, L_P1__subcl78_ID);
    Timer_Init(L_P1__GetSubcl78(my_id), 351000);
    Timer_AggmInit(L_P1__GetSubcl79(my_id), true, CLASS_L_P1_C3_ID, my_id, L_P1__subcl79_ID);
    Timer_Init(L_P1__GetSubcl79(my_id), 5230000);
    Timer_AggmInit(L_P1__GetSubcl80(my_id), true, CLASS_L_P1_C3_ID, my_id, L_P1__subcl80_ID);
    Timer_Init(L_P1__GetSubcl80(my_id), 5230000);
    Timer_AggmInit(L_P1__GetSubcl81(my_id), true, CLASS_L_P1_C3_ID, my_id, L_P1__subcl81_ID);
    Timer_Init(L_P1__GetSubcl81(my_id), 14000);
    Timer_AggmInit(L_P1__GetSubcl82(my_id), true, CLASS_L_P1_C3_ID, my_id, L_P1__subcl82_ID);
    Timer_Init(L_P1__GetSubcl82(my_id), 14000);
    Timer_AggmInit(L_P1__GetSubcl83(my_id), true, CLASS_L_P1_C3_ID, my_id, L_P1__subcl83_ID);
    Timer_Init(L_P1__GetSubcl83(my_id), 551000);
    Timer_AggmInit(L_P1__GetSubcl84(my_id), true, CLASS_L_P1_C3_ID, my_id, L_P1__subcl84_ID);
    Timer_Init(L_P1__GetSubcl84(my_id), 551000);
    Timer_AggmInit(L_P1__GetSubcl85(my_id), true, CLASS_L_P1_C3_ID, my_id, L_P1__subcl85_ID);
    Timer_Init(L_P1__GetSubcl85(my_id), 423000);
    Timer_AggmInit(L_P1__GetSubcl86(my_id), true, CLASS_L_P1_C3_ID, my_id, L_P1__subcl86_ID);
    Timer_Init(L_P1__GetSubcl86(my_id), 423000);
    Timer_AggmInit(L_P1__GetSubcl87(my_id), true, CLASS_L_P1_C3_ID, my_id, L_P1__subcl87_ID);
    Timer_Init(L_P1__GetSubcl87(my_id), 14000);
    Timer_AggmInit(L_P1__GetSubcl88(my_id), true, CLASS_L_P1_C3_ID, my_id, L_P1__subcl88_ID);
    Timer_Init(L_P1__GetSubcl88(my_id), 31000);
    Timer_AggmInit(L_P1__GetSubcl89(my_id), true, CLASS_L_P1_C3_ID, my_id, L_P1__subcl89_ID);
    Timer_Init(L_P1__GetSubcl89(my_id), 2000);
    Timer_AggmInit(L_P1__GetSubcl90(my_id), true, CLASS_L_P1_C3_ID, my_id, L_P1__subcl90_ID);
    Timer_Init(L_P1__GetSubcl90(my_id), 1230000);
    Timer_AggmInit(L_P1__GetSubcl91(my_id), true, CLASS_L_P1_C3_ID, my_id, L_P1__subcl91_ID);
    Timer_Init(L_P1__GetSubcl91(my_id), 345000);
    Counter_AggmInit(L_P1__GetSubcl92(my_id), true, CLASS_L_P1_C3_ID, my_id, L_P1__subcl92_ID);
    Counter_Init(L_P1__GetSubcl92(my_id));
    Counter_AggmInit(L_P1__GetSubcl93(my_id), true, CLASS_L_P1_C3_ID, my_id, L_P1__subcl93_ID);
    Counter_Init(L_P1__GetSubcl93(my_id));
    Counter_AggmInit(L_P1__GetSubcl94(my_id), true, CLASS_L_P1_C3_ID, my_id, L_P1__subcl94_ID);
    Counter_Init(L_P1__GetSubcl94(my_id));
    // init response
    L_P1_C3_SetResponse(my_id, LDS_SCHED_NOP);

    // transizione iniziale
    if(L_P1__Guard19(my_id)) {
        L_P1_C3_SetState(my_id, C3_St_state);
	L_P1__Effec19(my_id);
    } else {
        STOP_EXECUTION(LOGIC_ERROR);
    }
    // init variabili precedenti
    L_P1__SetSubcl65(my_id, L_P1__GetSubcl64(my_id));
    L_P1__SetSubcl67(my_id, L_P1__GetSubcl66(my_id));
    L_P1__SetSubcl69(my_id, L_P1__GetSubcl68(my_id));
    L_P1__SetSubcl71(my_id, L_P1__GetSubcl70(my_id));
}

void L_P1_C3_Exec(instance_id_t const my_id, Phase const p)
{
    L_P1_C3_SetResponse(my_id, LDS_SCHED_NOP);
    switch (p) {

    case LDS_PHASE_MANUAL:
        break;
 

    case LDS_PHASE_STATE:

        switch (L_P1_C3_GetState(my_id)) {

        case C3_St_state1:
            if (L_P1__Guard26(my_id)) {
                L_P1_C3_SetState(my_id, C3_St_state1);
                L_P1__Effec26(my_id);				
            }
            else
                {STOP_EXECUTION(LOGIC_ERROR); } // fine transizioni da state1 nella fase LDS_PHASE_STATE
            break;

        case C3_St_state:
            if (L_P1__Guard25(my_id)) {
                L_P1_C3_SetState(my_id, C3_St_state2);
                L_P1__Effec25(my_id);				
            }
            else if (L_P1__Guard21(my_id)) {
                L_P1_C3_SetState(my_id, C3_St_state1);
                L_P1__Effec21(my_id);				
            }
            else if (L_P1__Guard22(my_id)) {
                L_P1_C3_SetState(my_id, C3_St_state4);
                L_P1__Effec22(my_id);				
            }
            else if (L_P1__Guard23(my_id)) {
                L_P1_C3_SetState(my_id, C3_St_state3);
                L_P1__Effec23(my_id);				
            }
            else if (L_P1__Guard24(my_id)) {
                L_P1_C3_SetState(my_id, C3_St_state3);
                L_P1__Effec24(my_id);				
            }
            else if (L_P1__Guard20(my_id)) {
                L_P1_C3_SetState(my_id, C3_St_state);
                L_P1__Effec20(my_id);				
            }
            else
                {STOP_EXECUTION(LOGIC_ERROR); } // fine transizioni da state nella fase LDS_PHASE_STATE
            break;

        case C3_St_state4:
            if (L_P1__Guard30(my_id)) {
                L_P1_C3_SetState(my_id, C3_St_state4);
                L_P1__Effec30(my_id);				
            }
            else if (L_P1__Guard31(my_id)) {
                L_P1_C3_SetState(my_id, C3_St_state4);
                L_P1__Effec31(my_id);				
            }
            else if (L_P1__Guard32(my_id)) {
                L_P1_C3_SetState(my_id, C3_St_state);
                L_P1__Effec32(my_id);				
            }
            else if (L_P1__Guard33(my_id)) {
                L_P1_C3_SetState(my_id, C3_St_state1);
                L_P1__Effec33(my_id);				
            }
            else if (L_P1__Guard34(my_id)) {
                L_P1_C3_SetState(my_id, C3_St_state3);
                L_P1__Effec34(my_id);				
            }
            else if (L_P1__Guard29(my_id)) {
                L_P1_C3_SetState(my_id, C3_St_state4);
                L_P1__Effec29(my_id);				
            }
            else
                {STOP_EXECUTION(LOGIC_ERROR); } // fine transizioni da state4 nella fase LDS_PHASE_STATE
            break;

        case C3_St_state3:
            if (L_P1__Guard28(my_id)) {
                L_P1_C3_SetState(my_id, C3_St_state3);
                L_P1__Effec28(my_id);				
            }
            else
                {STOP_EXECUTION(LOGIC_ERROR); } // fine transizioni da state3 nella fase LDS_PHASE_STATE
            break;

        case C3_St_state2:
            if (L_P1__Guard27(my_id)) {
                L_P1_C3_SetState(my_id, C3_St_state2);
                L_P1__Effec27(my_id);				
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
    Timer_Exec(L_P1__GetSubcl77(my_id));
    Timer_Exec(L_P1__GetSubcl78(my_id));
    Timer_Exec(L_P1__GetSubcl79(my_id));
    Timer_Exec(L_P1__GetSubcl80(my_id));
    Timer_Exec(L_P1__GetSubcl81(my_id));
    Timer_Exec(L_P1__GetSubcl82(my_id));
    Timer_Exec(L_P1__GetSubcl83(my_id));
    Timer_Exec(L_P1__GetSubcl84(my_id));
    Timer_Exec(L_P1__GetSubcl85(my_id));
    Timer_Exec(L_P1__GetSubcl86(my_id));
    Timer_Exec(L_P1__GetSubcl87(my_id));
    Timer_Exec(L_P1__GetSubcl88(my_id));
    Timer_Exec(L_P1__GetSubcl89(my_id));
    Timer_Exec(L_P1__GetSubcl90(my_id));
    Timer_Exec(L_P1__GetSubcl91(my_id));
}

void L_P1_C3_GSetSafe(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C3(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C3(proc_id);
    L_P1__SetOutSubcl43(my_id, false);
    L_P1__SetOutSubcl44(my_id, rossoverde);
}

void L_P1_C3_GUpdatePrev(global_id_t const proc_id)
{
    CHECK_LT(GLOBAL_TO_L_P1_C3(proc_id), IID_MAX);
    instance_id_t my_id = (instance_id_t) GLOBAL_TO_L_P1_C3(proc_id);
    L_P1__SetSubcl57(my_id, L_P1__GetInSubcl56(my_id));
    L_P1__SetSubcl59(my_id, L_P1__GetInSubcl58(my_id));
    L_P1__SetSubcl61(my_id, L_P1__GetInSubcl60(my_id));
    L_P1__SetSubcl63(my_id, L_P1__GetInSubcl62(my_id));
    L_P1__SetSubcl65(my_id, L_P1__GetSubcl64(my_id));
    L_P1__SetSubcl67(my_id, L_P1__GetSubcl66(my_id));
    L_P1__SetSubcl69(my_id, L_P1__GetSubcl68(my_id));
    L_P1__SetSubcl71(my_id, L_P1__GetSubcl70(my_id));
}

// ********** Definizione macro **********

// Macro di effetto

/*
    CNL corrispondente:
    
    { commento: {37,}  se la variabile SubClass_C3_variabile_V10 è  diverso da  False , commento: {69,}Disattiva il timer SubClass_C3_timer_T7
    
       
     commento: {35,}  se il controllo SubClass_C3_controllo_C2 è  diverso da  True , commento: {68,}Attiva il timer SubClass_C3_timer_T5
    
       
     commento: {110,}  se il ripristino del timer  SubClass_C3_restoreTI_TI2 non è scaduto commento: {34,} e  se il parametro SubClass_C3_parametro_P4 non è  maggiore di  commento: {54,} 8 commento: {35,} e  se il controllo SubClass_C3_controllo_C10 è  diverso da c120x commento: {35,} e  se il controllo SubClass_C3_controllo_C10 non è  diverso da c120x commento: {38,} e  se il contatore SubClass_C3_contatore_Co3 è  maggiore di  commento: {54,} 1530 commento: {35,} o  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x, commento: {71,}Decrementa il contatore SubClass_C3_contatore_Co5
    
     ,altrimenti  commento: {72,}Azzera il contatore SubClass_C3_contatore_Co5
    
    
     commento: {109,}  se il ripristino della variabile  SubClass_C3_restoreva_RV1 è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} o  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x commento: {34,} e  se il parametro SubClass_C3_parametro_P2 è  diverso da c120x e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE , commento: {72,}Azzera il contatore SubClass_C3_contatore_Co3
    
     ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C3_variabile_V3 il valore 1
    
    
     commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L8 è  uguale a  commento: {53,}  state1  e  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} e  se il controllo SubClass_C3_controllo_C10 non è  diverso da c120x commento: {38,} e  se il contatore SubClass_C3_contatore_Co9 non è  maggiore di  commento: {54,} 1245, commento: {72,}Azzera il contatore SubClass_C3_contatore_Co5
    
       
    
    }
*/
void L_P1__Macro22(instance_id_t const my_id )
{
//  *37,*  se la variabile SubClass_C3_variabile_V10 è  diverso da  False , *69,*Disattiva il timer SubClass_C3_timer_T7
    bool res_NotLogicOP_0 = true;
    res_NotLogicOP_0 = (res_NotLogicOP_0 && ! (L_P1__GetSubcl74(my_id) == false));
    if(res_NotLogicOP_0){
    
    Timer_Disattiva(L_P1__GetSubcl91(my_id));
    }
    //  *35,*  se il controllo SubClass_C3_controllo_C2 è  diverso da  True , *68,*Attiva il timer SubClass_C3_timer_T5
    bool res_NotLogicOP_1 = true;
    res_NotLogicOP_1 = (res_NotLogicOP_1 && ! (L_P1__GetInSubcl46(my_id) == true));
    if(res_NotLogicOP_1){
    
    Timer_Attiva(L_P1__GetSubcl90(my_id));
    }
    //  *110,*  se il ripristino del timer  SubClass_C3_restoreTI_TI2 non è scaduto *34,* e  se il parametro SubClass_C3_parametro_P4 non è  maggiore di  *54,* 8 *35,* e  se il controllo SubClass_C3_controllo_C10 è  diverso da c120x *35,* e  se il controllo SubClass_C3_controllo_C10 non è  diverso da c120x *38,* e  se il contatore SubClass_C3_contatore_Co3 è  maggiore di  *54,* 1530 *35,* o  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x, *71,*Decrementa il contatore SubClass_C3_contatore_Co5
    // ,altrimenti  *72,*Azzera il contatore SubClass_C3_contatore_Co5
    bool res_OrLogicOP_2 = false;
    bool res_AndLogicOP_3 = true;
    bool res_AndLogicOP_4 = true;
    bool res_AndLogicOP_5 = true;
    bool res_AndLogicOP_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! Timer_Scaduto(L_P1__GetSubcl80(my_id)));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_7);
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetParamSubcl54(my_id) > 8u));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_8);
    
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_AndLogicOP_6);
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetInSubcl45(my_id) == c120x));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_9);
    
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_AndLogicOP_5);
    bool res_NotLogicOP_10 = true;
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (L_P1__GetInSubcl45(my_id) == c120x));
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! res_NotLogicOP_11);
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_10);
    
    res_AndLogicOP_3 = (res_AndLogicOP_3 && res_AndLogicOP_4);
    res_AndLogicOP_3 = (res_AndLogicOP_3 && (Counter_GetValore(L_P1__GetSubcl92(my_id)) > 1530u));
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_3);
    res_OrLogicOP_2 = (res_OrLogicOP_2 || (L_P1__GetInSubcl45(my_id) == c120x));
    
    if(res_OrLogicOP_2){
    
    Counter_Decr(L_P1__GetSubcl93(my_id));
    }else{
    
    Counter_Res(L_P1__GetSubcl93(my_id));
    }
    //  *109,*  se il ripristino della variabile  SubClass_C3_restoreva_RV1 è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE  *35,* o  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x *34,* e  se il parametro SubClass_C3_parametro_P2 è  diverso da c120x e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE , *72,*Azzera il contatore SubClass_C3_contatore_Co3
    // ,altrimenti  *67,* Assegna alla variabile SubClass_C3_variabile_V3 il valore 1
    bool res_OrLogicOP_12 = false;
    bool res_OrLogicOP_13 = false;
    res_OrLogicOP_13 = (res_OrLogicOP_13 || (L_P1__GetSubcl73(my_id) == false));
    res_OrLogicOP_13 = (res_OrLogicOP_13 || (L_P1__GetInConsd2(my_id) == false));
    
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_OrLogicOP_13);
    bool res_AndLogicOP_14 = true;
    bool res_AndLogicOP_15 = true;
    bool res_AndLogicOP_16 = true;
    res_AndLogicOP_16 = (res_AndLogicOP_16 && (L_P1__GetInSubcl45(my_id) == c120x));
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! (L_P1__GetParamSubcl52(my_id) == c120x));
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_NotLogicOP_17);
    
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_AndLogicOP_16);
    res_AndLogicOP_15 = (res_AndLogicOP_15 && (L_P1__GetInConsd2(my_id) == false));
    
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_AndLogicOP_15);
    res_AndLogicOP_14 = (res_AndLogicOP_14 && (L_P1__GetInConsd2(my_id) == false));
    
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_AndLogicOP_14);
    
    if(res_OrLogicOP_12){
    
    Counter_Res(L_P1__GetSubcl92(my_id));
    }else{
    
    L_P1__SetSubcl75(my_id,1u);
    }
    //  *111,*  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L8 è  uguale a  *53,*  state1  e  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  *35,* e  se il controllo SubClass_C3_controllo_C10 non è  diverso da c120x *38,* e  se il contatore SubClass_C3_contatore_Co9 non è  maggiore di  *54,* 1245, *72,*Azzera il contatore SubClass_C3_contatore_Co5
    bool res_OrLogicOP_18 = false;
    bool res_AndLogicOP_19 = true;
    bool res_ForAllPredicate_20 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl50Length(my_id); ++i)
    {
    L_P1__Recor2 it = L_P1__GetRecSubcl50(my_id,i);
    bool res_ImpliesLogicOp_21 = true;
    res_ImpliesLogicOp_21 = (res_ImpliesLogicOp_21 && (L_P1_C1_GetState(it.mainc49) == C1_St_state));
    res_ForAllPredicate_20 = res_ImpliesLogicOp_21;
    if(!res_ForAllPredicate_20) {break;}
    }
    res_AndLogicOP_19 = (res_AndLogicOP_19 && res_ForAllPredicate_20);
    res_AndLogicOP_19 = (res_AndLogicOP_19 && (L_P1__GetInConsd2(my_id) == false));
    
    res_OrLogicOP_18 = (res_OrLogicOP_18 || res_AndLogicOP_19);
    bool res_AndLogicOP_22 = true;
    bool res_AndLogicOP_23 = true;
    res_AndLogicOP_23 = (res_AndLogicOP_23 && (L_P1__GetInConsd2(my_id) == false));
    bool res_NotLogicOP_24 = true;
    bool res_NotLogicOP_25 = true;
    res_NotLogicOP_25 = (res_NotLogicOP_25 && ! (L_P1__GetInSubcl45(my_id) == c120x));
    res_NotLogicOP_24 = (res_NotLogicOP_24 && ! res_NotLogicOP_25);
    res_AndLogicOP_23 = (res_AndLogicOP_23 && res_NotLogicOP_24);
    
    res_AndLogicOP_22 = (res_AndLogicOP_22 && res_AndLogicOP_23);
    bool res_NotLogicOP_26 = true;
    res_NotLogicOP_26 = (res_NotLogicOP_26 && ! (Counter_GetValore(L_P1__GetSubcl94(my_id)) > 1245u));
    res_AndLogicOP_22 = (res_AndLogicOP_22 && res_NotLogicOP_26);
    
    res_OrLogicOP_18 = (res_OrLogicOP_18 || res_AndLogicOP_22);
    
    if(res_OrLogicOP_18){
    
    Counter_Res(L_P1__GetSubcl93(my_id));
    }
}

/*
    CNL corrispondente:
    
    {  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} e  se il contatore SubClass_C3_contatore_Co5 è  uguale a  commento: {53,} 12123 commento: {34,} e  se il parametro SubClass_C3_parametro_P4 non è  maggiore di  commento: {54,} 9 commento: {37,} o  se la variabile SubClass_C3_variabile_V3 è  uguale a  commento: {53,} 10, commento: {68,}Attiva il timer SubClass_C3_timer_T2
    
     ,altrimenti  commento: {66,} Assegna al comando SubClass_C3_comando_C1 il valore  False 
    
    
     commento: {41,}  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  commento: {105,} è  uguale a  True  commento: {35,} o  se il controllo SubClass_C3_controllo_C10 non è  diverso da c120x e  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro SubClass_C3_parametro_P4 non è  diverso da  commento: {56,} 1 e  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} o  se il timer SubClass_C3_timer_T7 non è attivo, commento: {67,} Assegna alla variabile SubClass_C3_variabile_V8 il valore  False 
    
     ,altrimenti  commento: {66,} Assegna al comando SubClass_C3_comando_C1 il valore  True 
    
    
     commento: {36,}  se il timer SubClass_C3_timer_T2 non è scaduto,  commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  commento: {105,} è  diverso da  commento: {56,}  state1 , commento: {88,} quando  commento: {111,}   lo stato del campo  MainClass_C1     commento: {105,} è  uguale a  commento: {53,}  state1  commento: {37,} o  se la variabile SubClass_C3_variabile_V3 non è  diverso da  commento: {56,} 9 e  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} o  se la variabile SubClass_C3_variabile_V8 non è  uguale a  False  commento: {38,} e  se il contatore SubClass_C3_contatore_Co3 è  uguale a  commento: {53,} 150, commento: {68,}Attiva il timer SubClass_C3_timer_T2
    
     ,altrimenti   Applica gli effetti
           della macro SubClass_C3_macroef_M1  commento: {73,}
    
    
     commento: {42,}  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  uguale a RossoGialloaVerdea commento: {36,} o  se il timer SubClass_C3_timer_T7 è scaduto, commento: {72,}Azzera il contatore SubClass_C3_contatore_Co3
    
     ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C3_variabile_V8 il valore  False 
    
    
    
    }
*/
void L_P1__Macro23(instance_id_t const my_id )
{
//  se il controllo ConsDef  è  uguale a FALSE  *38,* e  se il contatore SubClass_C3_contatore_Co5 è  uguale a  *53,* 12123 *34,* e  se il parametro SubClass_C3_parametro_P4 non è  maggiore di  *54,* 9 *37,* o  se la variabile SubClass_C3_variabile_V3 è  uguale a  *53,* 10, *68,*Attiva il timer SubClass_C3_timer_T2
    // ,altrimenti  *66,* Assegna al comando SubClass_C3_comando_C1 il valore  False
    bool res_OrLogicOP_0 = false;
    bool res_AndLogicOP_1 = true;
    bool res_AndLogicOP_2 = true;
    res_AndLogicOP_2 = (res_AndLogicOP_2 && (L_P1__GetInConsd2(my_id) == false));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && (Counter_GetValore(L_P1__GetSubcl93(my_id)) == 12123u));
    
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_AndLogicOP_2);
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__GetParamSubcl54(my_id) > 9u));
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_3);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_AndLogicOP_1);
    res_OrLogicOP_0 = (res_OrLogicOP_0 || (L_P1__GetSubcl75(my_id) == 10u));
    
    if(res_OrLogicOP_0){
    
    Timer_Attiva(L_P1__GetSubcl88(my_id));
    }else{
    
    L_P1__SetOutSubcl43(my_id,false);
    }
    //  *41,*  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  *105,* è  uguale a  True  *35,* o  se il controllo SubClass_C3_controllo_C10 non è  diverso da c120x e  se il controllo ConsDef  è  uguale a FALSE  *34,* e  se il parametro SubClass_C3_parametro_P4 non è  diverso da  *56,* 1 e  se il controllo ConsDef  è  uguale a FALSE  *36,* o  se il timer SubClass_C3_timer_T7 non è attivo, *67,* Assegna alla variabile SubClass_C3_variabile_V8 il valore  False 
    // ,altrimenti  *66,* Assegna al comando SubClass_C3_comando_C1 il valore  True
    bool res_OrLogicOP_4 = false;
    bool res_OrLogicOP_5 = false;
    bool res_ForAllPredicateNotEmpty_6 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl50Length(my_id); ++i)
    {
    L_P1__Recor2 it = L_P1__GetRecSubcl50(my_id,i);
    bool res_ImpliesLogicOp_7 = true;
    res_ImpliesLogicOp_7 = (res_ImpliesLogicOp_7 && (L_P1__GetParamMainc9(it.mainc49) == true));
    res_ForAllPredicateNotEmpty_6 = res_ImpliesLogicOp_7;
    if(!res_ForAllPredicateNotEmpty_6) {break;}
    }
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_ForAllPredicateNotEmpty_6);
    bool res_AndLogicOP_8 = true;
    bool res_AndLogicOP_9 = true;
    bool res_AndLogicOP_10 = true;
    bool res_NotLogicOP_11 = true;
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (L_P1__GetInSubcl45(my_id) == c120x));
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! res_NotLogicOP_12);
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_NotLogicOP_11);
    res_AndLogicOP_10 = (res_AndLogicOP_10 && (L_P1__GetInConsd2(my_id) == false));
    
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_AndLogicOP_10);
    bool res_NotLogicOP_13 = true;
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1__GetParamSubcl54(my_id) == 1u));
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! res_NotLogicOP_14);
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_NotLogicOP_13);
    
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_AndLogicOP_9);
    res_AndLogicOP_8 = (res_AndLogicOP_8 && (L_P1__GetInConsd2(my_id) == false));
    
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_AndLogicOP_8);
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_OrLogicOP_5);
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! Timer_Attivo(L_P1__GetSubcl91(my_id)));
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_NotLogicOP_15);
    
    if(res_OrLogicOP_4){
    
    L_P1__SetSubcl76(my_id,false);
    }else{
    
    L_P1__SetOutSubcl43(my_id,true);
    }
    //  *36,*  se il timer SubClass_C3_timer_T2 non è scaduto,  *111,*  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  *105,* è  diverso da  *56,*  state1 , *88,* quando  *111,*   lo stato del campo  MainClass_C1     *105,* è  uguale a  *53,*  state1  *37,* o  se la variabile SubClass_C3_variabile_V3 non è  diverso da  *56,* 9 e  se il controllo ConsDef  è  uguale a FALSE  *37,* o  se la variabile SubClass_C3_variabile_V8 non è  uguale a  False  *38,* e  se il contatore SubClass_C3_contatore_Co3 è  uguale a  *53,* 150, *68,*Attiva il timer SubClass_C3_timer_T2
    // ,altrimenti   Applica gli effetti
    //       della macro SubClass_C3_macroef_M1
    bool res_OrLogicOP_16 = false;
    bool res_OrLogicOP_17 = false;
    bool res_AndLogicOP_18 = true;
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! Timer_Scaduto(L_P1__GetSubcl88(my_id)));
    res_AndLogicOP_18 = (res_AndLogicOP_18 && res_NotLogicOP_19);
    bool res_ForAllPredicateNotEmpty_20 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl49Length(my_id); ++i)
    {
    L_P1__Recor1 it = L_P1__GetRecSubcl49(my_id,i);
    bool res_ImpliesLogicOp_21 = true;
    if((L_P1_C1_GetState(it.mainc48) == C1_St_state)){
    bool res_NotLogicOP_22 = true;
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! (L_P1_C1_GetState(it.mainc48) == C1_St_state));
    res_ImpliesLogicOp_21 = (res_ImpliesLogicOp_21 && res_NotLogicOP_22);
    res_ForAllPredicateNotEmpty_20 = res_ImpliesLogicOp_21;
    if(!res_ForAllPredicateNotEmpty_20) {break;}
    }
    }
    res_AndLogicOP_18 = (res_AndLogicOP_18 && res_ForAllPredicateNotEmpty_20);
    
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_AndLogicOP_18);
    bool res_AndLogicOP_23 = true;
    bool res_NotLogicOP_24 = true;
    bool res_NotLogicOP_25 = true;
    res_NotLogicOP_25 = (res_NotLogicOP_25 && ! (L_P1__GetSubcl75(my_id) == 9u));
    res_NotLogicOP_24 = (res_NotLogicOP_24 && ! res_NotLogicOP_25);
    res_AndLogicOP_23 = (res_AndLogicOP_23 && res_NotLogicOP_24);
    res_AndLogicOP_23 = (res_AndLogicOP_23 && (L_P1__GetInConsd2(my_id) == false));
    
    res_OrLogicOP_17 = (res_OrLogicOP_17 || res_AndLogicOP_23);
    
    res_OrLogicOP_16 = (res_OrLogicOP_16 || res_OrLogicOP_17);
    bool res_AndLogicOP_26 = true;
    bool res_NotLogicOP_27 = true;
    res_NotLogicOP_27 = (res_NotLogicOP_27 && ! (L_P1__GetSubcl76(my_id) == false));
    res_AndLogicOP_26 = (res_AndLogicOP_26 && res_NotLogicOP_27);
    res_AndLogicOP_26 = (res_AndLogicOP_26 && (Counter_GetValore(L_P1__GetSubcl92(my_id)) == 150u));
    
    res_OrLogicOP_16 = (res_OrLogicOP_16 || res_AndLogicOP_26);
    
    if(res_OrLogicOP_16){
    
    Timer_Attiva(L_P1__GetSubcl88(my_id));
    }else{
    
    L_P1__Macro22(my_id);
    }
    //  *73,*
    // *42,*  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  uguale a RossoGialloaVerdea *36,* o  se il timer SubClass_C3_timer_T7 è scaduto, *72,*Azzera il contatore SubClass_C3_contatore_Co3
    // ,altrimenti  *67,* Assegna alla variabile SubClass_C3_variabile_V8 il valore  False
    bool res_OrLogicOP_28 = false;
    bool res_ForAllPredicate_29 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl50Length(my_id); ++i)
    {
    L_P1__Recor2 it = L_P1__GetRecSubcl50(my_id,i);
    bool res_ImpliesLogicOp_30 = true;
    res_ImpliesLogicOp_30 = (res_ImpliesLogicOp_30 && (L_P1__GetInMainc5(it.mainc49) == rossogiallo));
    res_ForAllPredicate_29 = res_ImpliesLogicOp_30;
    if(!res_ForAllPredicate_29) {break;}
    }
    res_OrLogicOP_28 = (res_OrLogicOP_28 || res_ForAllPredicate_29);
    res_OrLogicOP_28 = (res_OrLogicOP_28 || Timer_Scaduto(L_P1__GetSubcl91(my_id)));
    
    if(res_OrLogicOP_28){
    
    Counter_Res(L_P1__GetSubcl92(my_id));
    }else{
    
    L_P1__SetSubcl76(my_id,false);
    }
}

/*
    CNL corrispondente:
    
    { commento: {41,}  se MainClass_C1_parametro_P7 del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  commento: {105,} è  diverso da  commento: {56,} 7, commento: {71,}Decrementa il contatore SubClass_C3_contatore_Co3
    
     ,altrimenti   Applica gli effetti
           della macro SubClass_C3_macroef_M1  commento: {73,}
    
    
      se il controllo ConsDef  è  uguale a FALSE , commento: {67,} Assegna alla variabile SubClass_C3_variabile_V8 il valore  True 
    
       
    
    }
*/
void L_P1__Macro24(instance_id_t const my_id )
{
//  *41,*  se MainClass_C1_parametro_P7 del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  *105,* è  diverso da  *56,* 7, *71,*Decrementa il contatore SubClass_C3_contatore_Co3
    // ,altrimenti   Applica gli effetti
    //       della macro SubClass_C3_macroef_M1
    bool res_ForAllPredicateNotEmpty_0 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl49Length(my_id); ++i)
    {
    L_P1__Recor1 it = L_P1__GetRecSubcl49(my_id,i);
    bool res_ImpliesLogicOp_1 = true;
    bool res_NotLogicOP_2 = true;
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! (L_P1__GetParamMainc8(it.mainc48) == 7u));
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_NotLogicOP_2);
    res_ForAllPredicateNotEmpty_0 = res_ImpliesLogicOp_1;
    if(!res_ForAllPredicateNotEmpty_0) {break;}
    }
    if(res_ForAllPredicateNotEmpty_0){
    
    Counter_Decr(L_P1__GetSubcl92(my_id));
    }else{
    
    L_P1__Macro22(my_id);
    }
    //  *73,*
    //  se il controllo ConsDef  è  uguale a FALSE , *67,* Assegna alla variabile SubClass_C3_variabile_V8 il valore  True
    if((L_P1__GetInConsd2(my_id) == false)){
    
    L_P1__SetSubcl76(my_id,true);
    }
}

/*
    CNL corrispondente:
    
    { commento: {34,}  se il parametro SubClass_C3_parametro_P4 non è  diverso da  commento: {56,} 6 e  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} e  se la variabile SubClass_C3_variabile_V3 è  minore di  commento: {55,} 9,  Applica gli effetti
           della macro SubClass_C3_macroef_M1  commento: {73,}
    
     ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C3_variabile_V8 il valore  True 
    
    
    
    }
*/
void L_P1__Macro25(instance_id_t const my_id )
{
//  *34,*  se il parametro SubClass_C3_parametro_P4 non è  diverso da  *56,* 6 e  se il controllo ConsDef  è  uguale a FALSE  *37,* e  se la variabile SubClass_C3_variabile_V3 è  minore di  *55,* 9,  Applica gli effetti
    //       della macro SubClass_C3_macroef_M1  *73,*
    // ,altrimenti  *67,* Assegna alla variabile SubClass_C3_variabile_V8 il valore  True
    bool res_AndLogicOP_0 = true;
    bool res_AndLogicOP_1 = true;
    bool res_NotLogicOP_2 = true;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__GetParamSubcl54(my_id) == 6u));
    res_NotLogicOP_2 = (res_NotLogicOP_2 && ! res_NotLogicOP_3);
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_2);
    res_AndLogicOP_1 = (res_AndLogicOP_1 && (L_P1__GetInConsd2(my_id) == false));
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_AndLogicOP_1);
    res_AndLogicOP_0 = (res_AndLogicOP_0 && (L_P1__GetSubcl75(my_id) < 9u));
    
    if(res_AndLogicOP_0){
    
    L_P1__Macro22(my_id);
    }else{
    
    L_P1__SetSubcl76(my_id,true);
    }
}

/*
    CNL corrispondente:
    
    { commento: {41,}  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  commento: {105,} è  uguale a  True  commento: {35,} o  se il controllo SubClass_C3_controllo_C10 non è  diverso da c120x commento: {38,} e  se il contatore SubClass_C3_contatore_Co3 è  minore di  commento: {55,} 134 commento: {37,} e  se la variabile SubClass_C3_variabile_V8 è  uguale a  True  commento: {38,} o  se il contatore SubClass_C3_contatore_Co3 è  diverso da  commento: {56,} 125, commento: {72,}Azzera il contatore SubClass_C3_contatore_Co5
    
       
     commento: {109,}  se il ripristino della variabile  SubClass_C3_restoreva_RV1 è  uguale a  False  commento: {38,} o  se il contatore SubClass_C3_contatore_Co3 è  uguale a  commento: {53,} 1112 commento: {34,} e  se il parametro SubClass_C3_parametro_P3 non è  uguale a  commento: {53,} 6 o  se il controllo ConsDef  è  uguale a FALSE ,  Applica gli effetti
           della macro SubClass_C3_macroef_M2  commento: {73,}
    
     ,altrimenti  commento: {72,}Azzera il contatore SubClass_C3_contatore_Co5
    
    
    
    }
*/
void L_P1__Macro26(instance_id_t const my_id )
{
//  *41,*  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  *105,* è  uguale a  True  *35,* o  se il controllo SubClass_C3_controllo_C10 non è  diverso da c120x *38,* e  se il contatore SubClass_C3_contatore_Co3 è  minore di  *55,* 134 *37,* e  se la variabile SubClass_C3_variabile_V8 è  uguale a  True  *38,* o  se il contatore SubClass_C3_contatore_Co3 è  diverso da  *56,* 125, *72,*Azzera il contatore SubClass_C3_contatore_Co5
    bool res_OrLogicOP_0 = false;
    bool res_OrLogicOP_1 = false;
    bool res_ForAllPredicateNotEmpty_2 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl49Length(my_id); ++i)
    {
    L_P1__Recor1 it = L_P1__GetRecSubcl49(my_id,i);
    bool res_ImpliesLogicOp_3 = true;
    res_ImpliesLogicOp_3 = (res_ImpliesLogicOp_3 && (L_P1__GetParamMainc9(it.mainc48) == true));
    res_ForAllPredicateNotEmpty_2 = res_ImpliesLogicOp_3;
    if(!res_ForAllPredicateNotEmpty_2) {break;}
    }
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_ForAllPredicateNotEmpty_2);
    bool res_AndLogicOP_4 = true;
    bool res_AndLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetInSubcl45(my_id) == c120x));
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! res_NotLogicOP_7);
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_6);
    res_AndLogicOP_5 = (res_AndLogicOP_5 && (Counter_GetValore(L_P1__GetSubcl92(my_id)) < 134u));
    
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_AndLogicOP_5);
    res_AndLogicOP_4 = (res_AndLogicOP_4 && (L_P1__GetSubcl76(my_id) == true));
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_4);
    
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_OrLogicOP_1);
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (Counter_GetValore(L_P1__GetSubcl92(my_id)) == 125u));
    res_OrLogicOP_0 = (res_OrLogicOP_0 || res_NotLogicOP_8);
    
    if(res_OrLogicOP_0){
    
    Counter_Res(L_P1__GetSubcl93(my_id));
    }
    //  *109,*  se il ripristino della variabile  SubClass_C3_restoreva_RV1 è  uguale a  False  *38,* o  se il contatore SubClass_C3_contatore_Co3 è  uguale a  *53,* 1112 *34,* e  se il parametro SubClass_C3_parametro_P3 non è  uguale a  *53,* 6 o  se il controllo ConsDef  è  uguale a FALSE ,  Applica gli effetti
    //       della macro SubClass_C3_macroef_M2  *73,*
    // ,altrimenti  *72,*Azzera il contatore SubClass_C3_contatore_Co5
    bool res_OrLogicOP_9 = false;
    bool res_OrLogicOP_10 = false;
    res_OrLogicOP_10 = (res_OrLogicOP_10 || (L_P1__GetSubcl73(my_id) == false));
    bool res_AndLogicOP_11 = true;
    res_AndLogicOP_11 = (res_AndLogicOP_11 && (Counter_GetValore(L_P1__GetSubcl92(my_id)) == 1112u));
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (L_P1__GetParamSubcl53(my_id) == 6u));
    res_AndLogicOP_11 = (res_AndLogicOP_11 && res_NotLogicOP_12);
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_AndLogicOP_11);
    
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_OrLogicOP_10);
    res_OrLogicOP_9 = (res_OrLogicOP_9 || (L_P1__GetInConsd2(my_id) == false));
    
    if(res_OrLogicOP_9){
    
    L_P1__Macro24(my_id);
    }else{
    
    Counter_Res(L_P1__GetSubcl93(my_id));
    }
}


// Macro di verifica

/*
    CNL corrispondente:
    
    { commento: {63,} commento: {36,}  se il timer SubClass_C3_timer_T5 è disattivo commento: {35,} o  se il controllo SubClass_C3_controllo_C2 è  uguale a  True  commento: {35,} e  se il controllo SubClass_C3_controllo_C6 non è  uguale a RossoVerde commento: {36,} o  se il timer SubClass_C3_timer_T2 è attivo commento: {37,} o  se la variabile SubClass_C3_variabile_V8 non è  diverso da  False  commento: {35,} e  se il controllo SubClass_C3_controllo_C10 non è  uguale a c120x, Solo una delle seguenti { 
     commento: {61,} commento: {45,}  se  MainClass_C1_contatore_Co8 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  uguale a  commento: {53,} 11512 commento: {35,} o  se il controllo SubClass_C3_controllo_C2 non è  uguale a  True  commento: {36,} e  se il timer SubClass_C3_timer_T7 è attivo commento: {38,} o  se il contatore SubClass_C3_contatore_Co3 non è  uguale a  commento: {53,} 1130 commento: {35,} o  se il controllo SubClass_C3_controllo_C4 è  diverso da RossoVerde, Tutte le seguenti { 
      se l'argomento argomento_ave4 non  è  uguale a  False  commento: {39,}  commento: {37,} o  se la variabile SubClass_C3_variabile_V10 non è  uguale a  True , Verifica che   commento: {49,}  commento: {,}  il timer SubClass_C3_timer_T7 sia attivo
     commento: {104,} o  che  commento: {36,}  il timer SubClass_C3_timer_T7 sia attivo
    
    
     } Verifica che   commento: {48,51,}  commento: {,}  il controllo SubClass_C3_controllo_C2 non sia  uguale a  True 
     commento: {104,} o  che  commento: {,}  il contatore SubClass_C3_contatore_Co3 non sia  uguale a  commento: {53,} 134
    
    
     } Verifica che   commento: {50,51,}  commento: {,}  la variabile SubClass_C3_variabile_V8 sia  diverso da  True 
     commento: {104,} o  che  commento: {,}  il contatore SubClass_C3_contatore_Co3 sia  maggiore di  commento: {54,} 1
    
    
    }
*/
bool L_P1__Macro29(instance_id_t const my_id , bool argom60, C3_Enumerat4 argom61, bool argom62, C3_Enumerat3 argom63, C3_Enumerat2 argom64)
{
bool res_AndLogicOP_0 = true;
    
    //  *63,* *36,*  se il timer SubClass_C3_timer_T5 è disattivo *35,* o  se il controllo SubClass_C3_controllo_C2 è  uguale a  True  *35,* e  se il controllo SubClass_C3_controllo_C6 non è  uguale a RossoVerde *36,* o  se il timer SubClass_C3_timer_T2 è attivo *37,* o  se la variabile SubClass_C3_variabile_V8 non è  diverso da  False  *35,* e  se il controllo SubClass_C3_controllo_C10 non è  uguale a c120x, Solo una delle seguenti { 
    //   *61,* *45,*  se  MainClass_C1_contatore_Co8 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  uguale a  *53,* 11512 *35,* o  se il controllo SubClass_C3_controllo_C2 non è  uguale a  True  *36,* e  se il timer SubClass_C3_timer_T7 è attivo *38,* o  se il contatore SubClass_C3_contatore_Co3 non è  uguale a  *53,* 1130 *35,* o  se il controllo SubClass_C3_controllo_C4 è  diverso da RossoVerde, Tutte le seguenti { 
    //    se l'argomento argomento_ave4 non  è  uguale a  False  *39,*  *37,* o  se la variabile SubClass_C3_variabile_V10 non è  uguale a  True , Verifica che   *49,*  *,*  il timer SubClass_C3_timer_T7 sia attivo
    //   *104,* o  che  *36,*  il timer SubClass_C3_timer_T7 sia attivo
    //   } Verifica che   *48,51,*  *,*  il controllo SubClass_C3_controllo_C2 non sia  uguale a  True 
    //   *104,* o  che  *,*  il contatore SubClass_C3_contatore_Co3 non sia  uguale a  *53,* 134
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_OrLogicOP_4 = false;
    res_OrLogicOP_4 = (res_OrLogicOP_4 || Timer_Disattivo(L_P1__GetSubcl90(my_id)));
    bool res_AndLogicOP_5 = true;
    res_AndLogicOP_5 = (res_AndLogicOP_5 && (L_P1__GetInSubcl46(my_id) == true));
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetInSubcl48(my_id) == rossoverde));
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_6);
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_AndLogicOP_5);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_OrLogicOP_4);
    res_OrLogicOP_3 = (res_OrLogicOP_3 || Timer_Attivo(L_P1__GetSubcl88(my_id)));
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    bool res_AndLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetSubcl76(my_id) == false));
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! res_NotLogicOP_9);
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_8);
    bool res_NotLogicOP_10 = true;
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! (L_P1__GetInSubcl45(my_id) == c120x));
    res_AndLogicOP_7 = (res_AndLogicOP_7 && res_NotLogicOP_10);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_7);
    
    if(res_OrLogicOP_2){
    bool res_XorLogicOP_11 = true;
    int xorIndex_res_XorLogicOP_11 = 0;
    bool res_ImpliesLogicOp_12 = true;
    bool res_OrLogicOP_13 = false;
    bool res_OrLogicOP_14 = false;
    bool res_OrLogicOP_15 = false;
    bool res_ForAllPredicate_16 = true;
    for (index_t i = 0; i < L_P1__GetParamSubcl50Length(my_id); ++i)
    {
    L_P1__Recor2 it = L_P1__GetRecSubcl50(my_id,i);
    bool res_ImpliesLogicOp_17 = true;
    res_ImpliesLogicOp_17 = (res_ImpliesLogicOp_17 && (Counter_GetValore(L_P1__GetMainc45(it.mainc49)) == 11512u));
    res_ForAllPredicate_16 = res_ImpliesLogicOp_17;
    if(!res_ForAllPredicate_16) {break;}
    }
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_ForAllPredicate_16);
    bool res_AndLogicOP_18 = true;
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (L_P1__GetInSubcl46(my_id) == true));
    res_AndLogicOP_18 = (res_AndLogicOP_18 && res_NotLogicOP_19);
    res_AndLogicOP_18 = (res_AndLogicOP_18 && Timer_Attivo(L_P1__GetSubcl91(my_id)));
    
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_AndLogicOP_18);
    
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_OrLogicOP_15);
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! (Counter_GetValore(L_P1__GetSubcl92(my_id)) == 1130u));
    res_OrLogicOP_14 = (res_OrLogicOP_14 || res_NotLogicOP_20);
    
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_OrLogicOP_14);
    bool res_NotLogicOP_21 = true;
    res_NotLogicOP_21 = (res_NotLogicOP_21 && ! (L_P1__GetInSubcl47(my_id) == rossoverde));
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_NotLogicOP_21);
    
    if(res_OrLogicOP_13){
    bool res_ImpliesLogicOp_22 = true;
    bool res_OrLogicOP_23 = false;
    bool res_NotLogicOP_24 = true;
    res_NotLogicOP_24 = (res_NotLogicOP_24 && ! (argom62 == false));
    res_OrLogicOP_23 = (res_OrLogicOP_23 || res_NotLogicOP_24);
    bool res_NotLogicOP_25 = true;
    res_NotLogicOP_25 = (res_NotLogicOP_25 && ! (L_P1__GetSubcl74(my_id) == true));
    res_OrLogicOP_23 = (res_OrLogicOP_23 || res_NotLogicOP_25);
    
    if(res_OrLogicOP_23){
    bool res_OrLogicOP_26 = false;
    res_OrLogicOP_26 = (res_OrLogicOP_26 || Timer_Attivo(L_P1__GetSubcl91(my_id)));
    res_OrLogicOP_26 = (res_OrLogicOP_26 || Timer_Attivo(L_P1__GetSubcl91(my_id)));
    
    res_ImpliesLogicOp_22 = (res_ImpliesLogicOp_22 && res_OrLogicOP_26);
    }
    res_ImpliesLogicOp_12 = (res_ImpliesLogicOp_12 && res_ImpliesLogicOp_22);
    }
    if(res_ImpliesLogicOp_12){
    xorIndex_res_XorLogicOP_11 = (xorIndex_res_XorLogicOP_11 + 1);
    }
    bool res_OrLogicOP_27 = false;
    bool res_NotLogicOP_28 = true;
    res_NotLogicOP_28 = (res_NotLogicOP_28 && ! (L_P1__GetInSubcl46(my_id) == true));
    res_OrLogicOP_27 = (res_OrLogicOP_27 || res_NotLogicOP_28);
    bool res_NotLogicOP_29 = true;
    res_NotLogicOP_29 = (res_NotLogicOP_29 && ! (Counter_GetValore(L_P1__GetSubcl92(my_id)) == 134u));
    res_OrLogicOP_27 = (res_OrLogicOP_27 || res_NotLogicOP_29);
    
    if(res_OrLogicOP_27){
    xorIndex_res_XorLogicOP_11 = (xorIndex_res_XorLogicOP_11 + 1);
    }
    
    res_XorLogicOP_11 = (res_XorLogicOP_11 && (xorIndex_res_XorLogicOP_11 == 1));
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_XorLogicOP_11);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *50,51,*  *,*  la variabile SubClass_C3_variabile_V8 sia  diverso da  True 
    //   *104,* o  che  *,*  il contatore SubClass_C3_contatore_Co3 sia  maggiore di  *54,* 1
    bool res_OrLogicOP_30 = false;
    bool res_NotLogicOP_31 = true;
    res_NotLogicOP_31 = (res_NotLogicOP_31 && ! (L_P1__GetSubcl76(my_id) == true));
    res_OrLogicOP_30 = (res_OrLogicOP_30 || res_NotLogicOP_31);
    res_OrLogicOP_30 = (res_OrLogicOP_30 || (Counter_GetValore(L_P1__GetSubcl92(my_id)) > 1u));
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_30);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
     
    { commento: {61,} commento: {38,}  se il contatore SubClass_C3_contatore_Co3 è  uguale a  commento: {53,} 14 commento: {38,} o  se il contatore SubClass_C3_contatore_Co3 è  uguale a  commento: {53,} 111 commento: {37,} o  se la variabile SubClass_C3_variabile_V8 è  diverso da  True  commento: {34,} o  se il parametro SubClass_C3_parametro_P1 non è  diverso da  False  e  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
     commento: {61,} commento: {110,}  se il ripristino del timer  SubClass_C3_restoreTI_TI1 non è scaduto commento: {34,} o  se il parametro SubClass_C3_parametro_P4 non è  minore di  commento: {55,} 9 commento: {35,} o  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x commento: {34,} o  se il parametro SubClass_C3_parametro_P4 non è  diverso da  commento: {56,} 2 commento: {38,} e  se il contatore SubClass_C3_contatore_Co9 non è  diverso da  commento: {56,} 11230 commento: {35,} e  se il controllo SubClass_C3_controllo_C6 è  diverso da RossoVerde, Tutte le seguenti { 
     commento: {63,} commento: {38,}  se il contatore SubClass_C3_contatore_Co9 non è  diverso da  commento: {56,} 124 commento: {35,} o  se il controllo SubClass_C3_controllo_C10 non è  diverso da c120x commento: {38,} e  se il contatore SubClass_C3_contatore_Co3 è  maggiore di  commento: {54,} 135 commento: {35,} o  se il controllo SubClass_C3_controllo_C10 è  diverso da c120x o  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} o  se il timer SubClass_C3_timer_T2 non è scaduto, Solo una delle seguenti { 
     commento: {44,}  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  commento: {105,} è  uguale a RossoGialloVerde commento: {34,} e  se il parametro SubClass_C3_parametro_P2 è  uguale a c120x commento: {35,} e  se il controllo SubClass_C3_controllo_C2 non è  uguale a  False  commento: {34,} e  se il parametro SubClass_C3_parametro_P2 è  diverso da c120x commento: {37,} o  se la variabile SubClass_C3_variabile_V10 è  uguale a  False  commento: {37,} e  se la variabile SubClass_C3_variabile_V10 è  uguale a  False , Verifica che   commento: {48,50,}   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} e  che  commento: {,}  la variabile SubClass_C3_variabile_V3 sia  uguale a  commento: {53,} 7
     commento: {104,} e  che  commento: {,}  il controllo SubClass_C3_controllo_C10 sia  diverso da c120x
     commento: {104,} o  che  commento: {35,}  il controllo SubClass_C3_controllo_C2 non sia  diverso da  False 
    
    
     } Verifica che   commento: {50,}  commento: {,}  la variabile SubClass_C3_variabile_V8 sia  diverso da  False 
    
    
     } Verifica che   commento: {47,48,51,}  commento: {,}  il contatore SubClass_C3_contatore_Co3 sia  diverso da  commento: {56,} 151
     commento: {104,} o  che  commento: {34,}  il parametro SubClass_C3_parametro_P9 non sia  minore di  commento: {55,} 2
     commento: {104,} o  che  commento: {34,}  il parametro SubClass_C3_parametro_P4 non sia  diverso da  commento: {56,} 5
     commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} e  che  commento: {,}  il controllo SubClass_C3_controllo_C10 non sia  diverso da c120x
     commento: {104,} o  che  commento: {35,}  il controllo SubClass_C3_controllo_C4 non sia  diverso da RossoVerde
    
    
     } Verifica che   commento: {50,}  commento: {,}  la variabile SubClass_C3_variabile_V8 sia  uguale a  False 
    
    
    }
*/
bool L_P1__Macro30(instance_id_t const my_id )
{
bool res_AndLogicOP_0 = true;
    
    //  *61,* *38,*  se il contatore SubClass_C3_contatore_Co3 è  uguale a  *53,* 14 *38,* o  se il contatore SubClass_C3_contatore_Co3 è  uguale a  *53,* 111 *37,* o  se la variabile SubClass_C3_variabile_V8 è  diverso da  True  *34,* o  se il parametro SubClass_C3_parametro_P1 non è  diverso da  False  e  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
    //   *61,* *110,*  se il ripristino del timer  SubClass_C3_restoreTI_TI1 non è scaduto *34,* o  se il parametro SubClass_C3_parametro_P4 non è  minore di  *55,* 9 *35,* o  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x *34,* o  se il parametro SubClass_C3_parametro_P4 non è  diverso da  *56,* 2 *38,* e  se il contatore SubClass_C3_contatore_Co9 non è  diverso da  *56,* 11230 *35,* e  se il controllo SubClass_C3_controllo_C6 è  diverso da RossoVerde, Tutte le seguenti { 
    //   *63,* *38,*  se il contatore SubClass_C3_contatore_Co9 non è  diverso da  *56,* 124 *35,* o  se il controllo SubClass_C3_controllo_C10 non è  diverso da c120x *38,* e  se il contatore SubClass_C3_contatore_Co3 è  maggiore di  *54,* 135 *35,* o  se il controllo SubClass_C3_controllo_C10 è  diverso da c120x o  se il controllo ConsDef  è  uguale a FALSE  *36,* o  se il timer SubClass_C3_timer_T2 non è scaduto, Solo una delle seguenti { 
    //   *44,*  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  *105,* è  uguale a RossoGialloVerde *34,* e  se il parametro SubClass_C3_parametro_P2 è  uguale a c120x *35,* e  se il controllo SubClass_C3_controllo_C2 non è  uguale a  False  *34,* e  se il parametro SubClass_C3_parametro_P2 è  diverso da c120x *37,* o  se la variabile SubClass_C3_variabile_V10 è  uguale a  False  *37,* e  se la variabile SubClass_C3_variabile_V10 è  uguale a  False , Verifica che   *48,50,*   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* e  che  *,*  la variabile SubClass_C3_variabile_V3 sia  uguale a  *53,* 7
    //   *104,* e  che  *,*  il controllo SubClass_C3_controllo_C10 sia  diverso da c120x
    //   *104,* o  che  *35,*  il controllo SubClass_C3_controllo_C2 non sia  diverso da  False 
    //   } Verifica che   *50,*  *,*  la variabile SubClass_C3_variabile_V8 sia  diverso da  False 
    //   } Verifica che   *47,48,51,*  *,*  il contatore SubClass_C3_contatore_Co3 sia  diverso da  *56,* 151
    //   *104,* o  che  *34,*  il parametro SubClass_C3_parametro_P9 non sia  minore di  *55,* 2
    //   *104,* o  che  *34,*  il parametro SubClass_C3_parametro_P4 non sia  diverso da  *56,* 5
    //   *104,* e  che   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* e  che  *,*  il controllo SubClass_C3_controllo_C10 non sia  diverso da c120x
    //   *104,* o  che  *35,*  il controllo SubClass_C3_controllo_C4 non sia  diverso da RossoVerde
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_OrLogicOP_4 = false;
    res_OrLogicOP_4 = (res_OrLogicOP_4 || (Counter_GetValore(L_P1__GetSubcl92(my_id)) == 14u));
    res_OrLogicOP_4 = (res_OrLogicOP_4 || (Counter_GetValore(L_P1__GetSubcl92(my_id)) == 111u));
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_OrLogicOP_4);
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (L_P1__GetSubcl76(my_id) == true));
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_NotLogicOP_5);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    bool res_AndLogicOP_6 = true;
    bool res_NotLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetParamSubcl51(my_id) == false));
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! res_NotLogicOP_8);
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_7);
    res_AndLogicOP_6 = (res_AndLogicOP_6 && (L_P1__GetInConsd2(my_id) == false));
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_AndLogicOP_6);
    
    if(res_OrLogicOP_2){
    bool res_AndLogicOP_9 = true;
    bool res_ImpliesLogicOp_10 = true;
    bool res_OrLogicOP_11 = false;
    bool res_OrLogicOP_12 = false;
    bool res_OrLogicOP_13 = false;
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! Timer_Scaduto(L_P1__GetSubcl78(my_id)));
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_NotLogicOP_14);
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (L_P1__GetParamSubcl54(my_id) < 9u));
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_NotLogicOP_15);
    
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_OrLogicOP_13);
    res_OrLogicOP_12 = (res_OrLogicOP_12 || (L_P1__GetInSubcl45(my_id) == c120x));
    
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_OrLogicOP_12);
    bool res_AndLogicOP_16 = true;
    bool res_AndLogicOP_17 = true;
    bool res_NotLogicOP_18 = true;
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (L_P1__GetParamSubcl54(my_id) == 2u));
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! res_NotLogicOP_19);
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_NotLogicOP_18);
    bool res_NotLogicOP_20 = true;
    bool res_NotLogicOP_21 = true;
    res_NotLogicOP_21 = (res_NotLogicOP_21 && ! (Counter_GetValore(L_P1__GetSubcl94(my_id)) == 11230u));
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! res_NotLogicOP_21);
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_NotLogicOP_20);
    
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_AndLogicOP_17);
    bool res_NotLogicOP_22 = true;
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! (L_P1__GetInSubcl48(my_id) == rossoverde));
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_NotLogicOP_22);
    
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_AndLogicOP_16);
    
    if(res_OrLogicOP_11){
    bool res_AndLogicOP_23 = true;
    bool res_ImpliesLogicOp_24 = true;
    bool res_OrLogicOP_25 = false;
    bool res_OrLogicOP_26 = false;
    bool res_OrLogicOP_27 = false;
    bool res_OrLogicOP_28 = false;
    bool res_NotLogicOP_29 = true;
    bool res_NotLogicOP_30 = true;
    res_NotLogicOP_30 = (res_NotLogicOP_30 && ! (Counter_GetValore(L_P1__GetSubcl94(my_id)) == 124u));
    res_NotLogicOP_29 = (res_NotLogicOP_29 && ! res_NotLogicOP_30);
    res_OrLogicOP_28 = (res_OrLogicOP_28 || res_NotLogicOP_29);
    bool res_AndLogicOP_31 = true;
    bool res_NotLogicOP_32 = true;
    bool res_NotLogicOP_33 = true;
    res_NotLogicOP_33 = (res_NotLogicOP_33 && ! (L_P1__GetInSubcl45(my_id) == c120x));
    res_NotLogicOP_32 = (res_NotLogicOP_32 && ! res_NotLogicOP_33);
    res_AndLogicOP_31 = (res_AndLogicOP_31 && res_NotLogicOP_32);
    res_AndLogicOP_31 = (res_AndLogicOP_31 && (Counter_GetValore(L_P1__GetSubcl92(my_id)) > 135u));
    
    res_OrLogicOP_28 = (res_OrLogicOP_28 || res_AndLogicOP_31);
    
    res_OrLogicOP_27 = (res_OrLogicOP_27 || res_OrLogicOP_28);
    bool res_NotLogicOP_34 = true;
    res_NotLogicOP_34 = (res_NotLogicOP_34 && ! (L_P1__GetInSubcl45(my_id) == c120x));
    res_OrLogicOP_27 = (res_OrLogicOP_27 || res_NotLogicOP_34);
    
    res_OrLogicOP_26 = (res_OrLogicOP_26 || res_OrLogicOP_27);
    res_OrLogicOP_26 = (res_OrLogicOP_26 || (L_P1__GetInConsd2(my_id) == false));
    
    res_OrLogicOP_25 = (res_OrLogicOP_25 || res_OrLogicOP_26);
    bool res_NotLogicOP_35 = true;
    res_NotLogicOP_35 = (res_NotLogicOP_35 && ! Timer_Scaduto(L_P1__GetSubcl88(my_id)));
    res_OrLogicOP_25 = (res_OrLogicOP_25 || res_NotLogicOP_35);
    
    if(res_OrLogicOP_25){
    bool res_ImpliesLogicOp_36 = true;
    bool res_OrLogicOP_37 = false;
    bool res_AndLogicOP_38 = true;
    bool res_AndLogicOP_39 = true;
    bool res_AndLogicOP_40 = true;
    bool res_ForAllPredicateNotEmpty_41 = false;
    for (index_t i = 0; i < L_P1__GetParamSubcl50Length(my_id); ++i)
    {
    L_P1__Recor2 it = L_P1__GetRecSubcl50(my_id,i);
    bool res_ImpliesLogicOp_42 = true;
    res_ImpliesLogicOp_42 = (res_ImpliesLogicOp_42 && (L_P1__GetMainc34(it.mainc49) == rossogiallo1));
    res_ForAllPredicateNotEmpty_41 = res_ImpliesLogicOp_42;
    if(!res_ForAllPredicateNotEmpty_41) {break;}
    }
    res_AndLogicOP_40 = (res_AndLogicOP_40 && res_ForAllPredicateNotEmpty_41);
    res_AndLogicOP_40 = (res_AndLogicOP_40 && (L_P1__GetParamSubcl52(my_id) == c120x));
    
    res_AndLogicOP_39 = (res_AndLogicOP_39 && res_AndLogicOP_40);
    bool res_NotLogicOP_43 = true;
    res_NotLogicOP_43 = (res_NotLogicOP_43 && ! (L_P1__GetInSubcl46(my_id) == false));
    res_AndLogicOP_39 = (res_AndLogicOP_39 && res_NotLogicOP_43);
    
    res_AndLogicOP_38 = (res_AndLogicOP_38 && res_AndLogicOP_39);
    bool res_NotLogicOP_44 = true;
    res_NotLogicOP_44 = (res_NotLogicOP_44 && ! (L_P1__GetParamSubcl52(my_id) == c120x));
    res_AndLogicOP_38 = (res_AndLogicOP_38 && res_NotLogicOP_44);
    
    res_OrLogicOP_37 = (res_OrLogicOP_37 || res_AndLogicOP_38);
    bool res_AndLogicOP_45 = true;
    res_AndLogicOP_45 = (res_AndLogicOP_45 && (L_P1__GetSubcl74(my_id) == false));
    res_AndLogicOP_45 = (res_AndLogicOP_45 && (L_P1__GetSubcl74(my_id) == false));
    
    res_OrLogicOP_37 = (res_OrLogicOP_37 || res_AndLogicOP_45);
    
    if(res_OrLogicOP_37){
    bool res_OrLogicOP_46 = false;
    bool res_AndLogicOP_47 = true;
    bool res_AndLogicOP_48 = true;
    res_AndLogicOP_48 = (res_AndLogicOP_48 && (L_P1__GetInConsd2(my_id) == false));
    res_AndLogicOP_48 = (res_AndLogicOP_48 && (L_P1__GetSubcl75(my_id) == 7u));
    
    res_AndLogicOP_47 = (res_AndLogicOP_47 && res_AndLogicOP_48);
    bool res_NotLogicOP_49 = true;
    res_NotLogicOP_49 = (res_NotLogicOP_49 && ! (L_P1__GetInSubcl45(my_id) == c120x));
    res_AndLogicOP_47 = (res_AndLogicOP_47 && res_NotLogicOP_49);
    
    res_OrLogicOP_46 = (res_OrLogicOP_46 || res_AndLogicOP_47);
    bool res_NotLogicOP_50 = true;
    bool res_NotLogicOP_51 = true;
    res_NotLogicOP_51 = (res_NotLogicOP_51 && ! (L_P1__GetInSubcl46(my_id) == false));
    res_NotLogicOP_50 = (res_NotLogicOP_50 && ! res_NotLogicOP_51);
    res_OrLogicOP_46 = (res_OrLogicOP_46 || res_NotLogicOP_50);
    
    res_ImpliesLogicOp_36 = (res_ImpliesLogicOp_36 && res_OrLogicOP_46);
    }
    res_ImpliesLogicOp_24 = (res_ImpliesLogicOp_24 && res_ImpliesLogicOp_36);
    }
    res_AndLogicOP_23 = (res_AndLogicOP_23 && res_ImpliesLogicOp_24);
    bool res_NotLogicOP_52 = true;
    res_NotLogicOP_52 = (res_NotLogicOP_52 && ! (L_P1__GetSubcl76(my_id) == false));
    res_AndLogicOP_23 = (res_AndLogicOP_23 && res_NotLogicOP_52);
    
    res_ImpliesLogicOp_10 = (res_ImpliesLogicOp_10 && res_AndLogicOP_23);
    }
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_ImpliesLogicOp_10);
    bool res_OrLogicOP_53 = false;
    bool res_OrLogicOP_54 = false;
    bool res_OrLogicOP_55 = false;
    bool res_NotLogicOP_56 = true;
    res_NotLogicOP_56 = (res_NotLogicOP_56 && ! (Counter_GetValore(L_P1__GetSubcl92(my_id)) == 151u));
    res_OrLogicOP_55 = (res_OrLogicOP_55 || res_NotLogicOP_56);
    bool res_NotLogicOP_57 = true;
    res_NotLogicOP_57 = (res_NotLogicOP_57 && ! (L_P1__GetParamSubcl55(my_id) < 2u));
    res_OrLogicOP_55 = (res_OrLogicOP_55 || res_NotLogicOP_57);
    
    res_OrLogicOP_54 = (res_OrLogicOP_54 || res_OrLogicOP_55);
    bool res_AndLogicOP_58 = true;
    bool res_AndLogicOP_59 = true;
    bool res_NotLogicOP_60 = true;
    bool res_NotLogicOP_61 = true;
    res_NotLogicOP_61 = (res_NotLogicOP_61 && ! (L_P1__GetParamSubcl54(my_id) == 5u));
    res_NotLogicOP_60 = (res_NotLogicOP_60 && ! res_NotLogicOP_61);
    res_AndLogicOP_59 = (res_AndLogicOP_59 && res_NotLogicOP_60);
    res_AndLogicOP_59 = (res_AndLogicOP_59 && (L_P1__GetInConsd2(my_id) == false));
    
    res_AndLogicOP_58 = (res_AndLogicOP_58 && res_AndLogicOP_59);
    bool res_NotLogicOP_62 = true;
    bool res_NotLogicOP_63 = true;
    res_NotLogicOP_63 = (res_NotLogicOP_63 && ! (L_P1__GetInSubcl45(my_id) == c120x));
    res_NotLogicOP_62 = (res_NotLogicOP_62 && ! res_NotLogicOP_63);
    res_AndLogicOP_58 = (res_AndLogicOP_58 && res_NotLogicOP_62);
    
    res_OrLogicOP_54 = (res_OrLogicOP_54 || res_AndLogicOP_58);
    
    res_OrLogicOP_53 = (res_OrLogicOP_53 || res_OrLogicOP_54);
    bool res_NotLogicOP_64 = true;
    bool res_NotLogicOP_65 = true;
    res_NotLogicOP_65 = (res_NotLogicOP_65 && ! (L_P1__GetInSubcl47(my_id) == rossoverde));
    res_NotLogicOP_64 = (res_NotLogicOP_64 && ! res_NotLogicOP_65);
    res_OrLogicOP_53 = (res_OrLogicOP_53 || res_NotLogicOP_64);
    
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_OrLogicOP_53);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_AndLogicOP_9);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *50,*  *,*  la variabile SubClass_C3_variabile_V8 sia  uguale a  False
    res_AndLogicOP_0 = (res_AndLogicOP_0 && (L_P1__GetSubcl76(my_id) == false));
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
     
    { commento: {61,} commento: {110,}  se il ripristino del timer  SubClass_C3_restoreTI_TI5 non è scaduto commento: {38,} o  se il contatore SubClass_C3_contatore_Co5 è  diverso da  commento: {56,} 131230 commento: {36,} o  se il timer SubClass_C3_timer_T2 è disattivo, Tutte le seguenti { 
     commento: {61,}  se il ripristino dello stato  è  uguale a  commento: {53,}  state1  commento: {107,} e  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} o  se il timer SubClass_C3_timer_T2 è scaduto commento: {37,} e  se la variabile SubClass_C3_variabile_V10 è  uguale a  True  e  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
     commento: {38,}  se il contatore SubClass_C3_contatore_Co9 non è  uguale a  commento: {53,} 124 e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} e  se il contatore SubClass_C3_contatore_Co3 non è  minore di  commento: {55,} 11512 commento: {37,} e  se la variabile SubClass_C3_variabile_V3 non è  maggiore di  commento: {54,} 6 commento: {37,} o  se la variabile SubClass_C3_variabile_V8 non è  diverso da  True , Verifica che   commento: {48,50,}  commento: {,}  la variabile SubClass_C3_variabile_V8 sia  uguale a  False 
     commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
    
    
     } Verifica che   commento: {48,49,51,}  commento: {,}  il contatore SubClass_C3_contatore_Co3 non sia  uguale a  commento: {53,} 15
     commento: {104,} e  che  commento: {,}  il timer SubClass_C3_timer_T7 sia disattivo
     commento: {104,} e  che  commento: {,}  il controllo SubClass_C3_controllo_C10 non sia  uguale a c120x
     commento: {104,} o  che  commento: {38,}  il contatore SubClass_C3_contatore_Co3 sia  maggiore di  commento: {54,} 15
    
    
     } Verifica che   commento: {47,48,50,}  commento: {,}  il controllo SubClass_C3_controllo_C10 non sia  diverso da c120x
     commento: {104,} o  che  commento: {34,}  il parametro SubClass_C3_parametro_P4 non sia  minore di  commento: {55,} 2
     commento: {104,} e  che  commento: {34,}  il parametro SubClass_C3_parametro_P4 sia  diverso da  commento: {56,} 5
     commento: {104,} o  che  commento: {,}  la variabile SubClass_C3_variabile_V8 sia  uguale a  True 
     commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
     commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
    
    
    }
*/
bool L_P1__Macro31(instance_id_t const my_id )
{
bool res_AndLogicOP_0 = true;
    
    //  *61,* *110,*  se il ripristino del timer  SubClass_C3_restoreTI_TI5 non è scaduto *38,* o  se il contatore SubClass_C3_contatore_Co5 è  diverso da  *56,* 131230 *36,* o  se il timer SubClass_C3_timer_T2 è disattivo, Tutte le seguenti { 
    //   *61,*  se il ripristino dello stato  è  uguale a  *53,*  state1  *107,* e  se il controllo ConsDef  è  uguale a FALSE  *36,* o  se il timer SubClass_C3_timer_T2 è scaduto *37,* e  se la variabile SubClass_C3_variabile_V10 è  uguale a  True  e  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
    //   *38,*  se il contatore SubClass_C3_contatore_Co9 non è  uguale a  *53,* 124 e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  *38,* e  se il contatore SubClass_C3_contatore_Co3 non è  minore di  *55,* 11512 *37,* e  se la variabile SubClass_C3_variabile_V3 non è  maggiore di  *54,* 6 *37,* o  se la variabile SubClass_C3_variabile_V8 non è  diverso da  True , Verifica che   *48,50,*  *,*  la variabile SubClass_C3_variabile_V8 sia  uguale a  False 
    //   *104,* o  che   il controllo ConsDef  sia  uguale a FALSE 
    //   } Verifica che   *48,49,51,*  *,*  il contatore SubClass_C3_contatore_Co3 non sia  uguale a  *53,* 15
    //   *104,* e  che  *,*  il timer SubClass_C3_timer_T7 sia disattivo
    //   *104,* e  che  *,*  il controllo SubClass_C3_controllo_C10 non sia  uguale a c120x
    //   *104,* o  che  *38,*  il contatore SubClass_C3_contatore_Co3 sia  maggiore di  *54,* 15
    //   }
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! Timer_Scaduto(L_P1__GetSubcl86(my_id)));
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_NotLogicOP_4);
    bool res_NotLogicOP_5 = true;
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! (Counter_GetValore(L_P1__GetSubcl93(my_id)) == 131230u));
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_NotLogicOP_5);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    res_OrLogicOP_2 = (res_OrLogicOP_2 || Timer_Disattivo(L_P1__GetSubcl88(my_id)));
    
    if(res_OrLogicOP_2){
    bool res_AndLogicOP_6 = true;
    bool res_ImpliesLogicOp_7 = true;
    bool res_OrLogicOP_8 = false;
    bool res_AndLogicOP_9 = true;
    res_AndLogicOP_9 = (res_AndLogicOP_9 && (L_P1__GetStato5(my_id) == C3_St_state));
    res_AndLogicOP_9 = (res_AndLogicOP_9 && (L_P1__GetInConsd2(my_id) == false));
    
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_AndLogicOP_9);
    bool res_AndLogicOP_10 = true;
    bool res_AndLogicOP_11 = true;
    res_AndLogicOP_11 = (res_AndLogicOP_11 && Timer_Scaduto(L_P1__GetSubcl88(my_id)));
    res_AndLogicOP_11 = (res_AndLogicOP_11 && (L_P1__GetSubcl74(my_id) == true));
    
    res_AndLogicOP_10 = (res_AndLogicOP_10 && res_AndLogicOP_11);
    res_AndLogicOP_10 = (res_AndLogicOP_10 && (L_P1__GetInConsd2(my_id) == false));
    
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_AndLogicOP_10);
    
    if(res_OrLogicOP_8){
    bool res_ImpliesLogicOp_12 = true;
    bool res_OrLogicOP_13 = false;
    bool res_AndLogicOP_14 = true;
    bool res_AndLogicOP_15 = true;
    bool res_AndLogicOP_16 = true;
    bool res_AndLogicOP_17 = true;
    bool res_NotLogicOP_18 = true;
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! (Counter_GetValore(L_P1__GetSubcl94(my_id)) == 124u));
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_NotLogicOP_18);
    res_AndLogicOP_17 = (res_AndLogicOP_17 && (L_P1__GetInConsd2(my_id) == false));
    
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_AndLogicOP_17);
    res_AndLogicOP_16 = (res_AndLogicOP_16 && (L_P1__GetInConsd2(my_id) == false));
    
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_AndLogicOP_16);
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (Counter_GetValore(L_P1__GetSubcl92(my_id)) < 11512u));
    res_AndLogicOP_15 = (res_AndLogicOP_15 && res_NotLogicOP_19);
    
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_AndLogicOP_15);
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! (L_P1__GetSubcl75(my_id) > 6u));
    res_AndLogicOP_14 = (res_AndLogicOP_14 && res_NotLogicOP_20);
    
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_AndLogicOP_14);
    bool res_NotLogicOP_21 = true;
    bool res_NotLogicOP_22 = true;
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! (L_P1__GetSubcl76(my_id) == true));
    res_NotLogicOP_21 = (res_NotLogicOP_21 && ! res_NotLogicOP_22);
    res_OrLogicOP_13 = (res_OrLogicOP_13 || res_NotLogicOP_21);
    
    if(res_OrLogicOP_13){
    bool res_OrLogicOP_23 = false;
    res_OrLogicOP_23 = (res_OrLogicOP_23 || (L_P1__GetSubcl76(my_id) == false));
    res_OrLogicOP_23 = (res_OrLogicOP_23 || (L_P1__GetInConsd2(my_id) == false));
    
    res_ImpliesLogicOp_12 = (res_ImpliesLogicOp_12 && res_OrLogicOP_23);
    }
    res_ImpliesLogicOp_7 = (res_ImpliesLogicOp_7 && res_ImpliesLogicOp_12);
    }
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_ImpliesLogicOp_7);
    bool res_OrLogicOP_24 = false;
    bool res_AndLogicOP_25 = true;
    bool res_AndLogicOP_26 = true;
    bool res_NotLogicOP_27 = true;
    res_NotLogicOP_27 = (res_NotLogicOP_27 && ! (Counter_GetValore(L_P1__GetSubcl92(my_id)) == 15u));
    res_AndLogicOP_26 = (res_AndLogicOP_26 && res_NotLogicOP_27);
    res_AndLogicOP_26 = (res_AndLogicOP_26 && Timer_Disattivo(L_P1__GetSubcl91(my_id)));
    
    res_AndLogicOP_25 = (res_AndLogicOP_25 && res_AndLogicOP_26);
    bool res_NotLogicOP_28 = true;
    res_NotLogicOP_28 = (res_NotLogicOP_28 && ! (L_P1__GetInSubcl45(my_id) == c120x));
    res_AndLogicOP_25 = (res_AndLogicOP_25 && res_NotLogicOP_28);
    
    res_OrLogicOP_24 = (res_OrLogicOP_24 || res_AndLogicOP_25);
    res_OrLogicOP_24 = (res_OrLogicOP_24 || (Counter_GetValore(L_P1__GetSubcl92(my_id)) > 15u));
    
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_OrLogicOP_24);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_AndLogicOP_6);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    //  che   *47,48,50,*  *,*  il controllo SubClass_C3_controllo_C10 non sia  diverso da c120x
    //   *104,* o  che  *34,*  il parametro SubClass_C3_parametro_P4 non sia  minore di  *55,* 2
    //   *104,* e  che  *34,*  il parametro SubClass_C3_parametro_P4 sia  diverso da  *56,* 5
    //   *104,* o  che  *,*  la variabile SubClass_C3_variabile_V8 sia  uguale a  True 
    //   *104,* o  che   il controllo ConsDef  sia  uguale a FALSE 
    //   *104,* o  che   il controllo ConsDef  sia  uguale a FALSE
    bool res_OrLogicOP_29 = false;
    bool res_OrLogicOP_30 = false;
    bool res_OrLogicOP_31 = false;
    bool res_OrLogicOP_32 = false;
    bool res_NotLogicOP_33 = true;
    bool res_NotLogicOP_34 = true;
    res_NotLogicOP_34 = (res_NotLogicOP_34 && ! (L_P1__GetInSubcl45(my_id) == c120x));
    res_NotLogicOP_33 = (res_NotLogicOP_33 && ! res_NotLogicOP_34);
    res_OrLogicOP_32 = (res_OrLogicOP_32 || res_NotLogicOP_33);
    bool res_AndLogicOP_35 = true;
    bool res_NotLogicOP_36 = true;
    res_NotLogicOP_36 = (res_NotLogicOP_36 && ! (L_P1__GetParamSubcl54(my_id) < 2u));
    res_AndLogicOP_35 = (res_AndLogicOP_35 && res_NotLogicOP_36);
    bool res_NotLogicOP_37 = true;
    res_NotLogicOP_37 = (res_NotLogicOP_37 && ! (L_P1__GetParamSubcl54(my_id) == 5u));
    res_AndLogicOP_35 = (res_AndLogicOP_35 && res_NotLogicOP_37);
    
    res_OrLogicOP_32 = (res_OrLogicOP_32 || res_AndLogicOP_35);
    
    res_OrLogicOP_31 = (res_OrLogicOP_31 || res_OrLogicOP_32);
    res_OrLogicOP_31 = (res_OrLogicOP_31 || (L_P1__GetSubcl76(my_id) == true));
    
    res_OrLogicOP_30 = (res_OrLogicOP_30 || res_OrLogicOP_31);
    res_OrLogicOP_30 = (res_OrLogicOP_30 || (L_P1__GetInConsd2(my_id) == false));
    
    res_OrLogicOP_29 = (res_OrLogicOP_29 || res_OrLogicOP_30);
    res_OrLogicOP_29 = (res_OrLogicOP_29 || (L_P1__GetInConsd2(my_id) == false));
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_29);
    
    
    
    return res_AndLogicOP_0;
}

/*
    CNL corrispondente:
    
    { commento: {109,}  se il ripristino della variabile  SubClass_C3_restoreva_RV1 è  uguale a  True  commento: {38,} o  se il contatore SubClass_C3_contatore_Co3 non è  diverso da  commento: {56,} 11451 commento: {38,} e  se il contatore SubClass_C3_contatore_Co5 è  diverso da  commento: {56,} 13 o  se l'argomento argomento_ave7 è  uguale a  True  commento: {39,} , Verifica che   commento: {48,49,51,}  commento: {,}  il contatore SubClass_C3_contatore_Co5 sia  uguale a  commento: {53,} 112
     commento: {104,} o  che  commento: {,}  il controllo SubClass_C3_controllo_C2 non sia  diverso da  False 
     commento: {104,} o  che  commento: {,}  il timer SubClass_C3_timer_T7 non sia disattivo
    
    
    }
*/
bool L_P1__Macro32(instance_id_t const my_id , C3_Enumerat4 argom65, C3_Enumerat3 argom66, C3_Enumerat4 argom67, bool argom68, C3_Enumerat4 argom69)
{
bool res_AndLogicOP_0 = true;
    
    //  *109,*  se il ripristino della variabile  SubClass_C3_restoreva_RV1 è  uguale a  True  *38,* o  se il contatore SubClass_C3_contatore_Co3 non è  diverso da  *56,* 11451 *38,* e  se il contatore SubClass_C3_contatore_Co5 è  diverso da  *56,* 13 o  se l'argomento argomento_ave7 è  uguale a  True  *39,* , Verifica che   *48,49,51,*  *,*  il contatore SubClass_C3_contatore_Co5 sia  uguale a  *53,* 112
    //   *104,* o  che  *,*  il controllo SubClass_C3_controllo_C2 non sia  diverso da  False 
    //   *104,* o  che  *,*  il timer SubClass_C3_timer_T7 non sia disattivo
    bool res_ImpliesLogicOp_1 = true;
    bool res_OrLogicOP_2 = false;
    bool res_OrLogicOP_3 = false;
    res_OrLogicOP_3 = (res_OrLogicOP_3 || (L_P1__GetSubcl73(my_id) == true));
    bool res_AndLogicOP_4 = true;
    bool res_NotLogicOP_5 = true;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (Counter_GetValore(L_P1__GetSubcl92(my_id)) == 11451u));
    res_NotLogicOP_5 = (res_NotLogicOP_5 && ! res_NotLogicOP_6);
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_5);
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (Counter_GetValore(L_P1__GetSubcl93(my_id)) == 13u));
    res_AndLogicOP_4 = (res_AndLogicOP_4 && res_NotLogicOP_7);
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_AndLogicOP_4);
    
    res_OrLogicOP_2 = (res_OrLogicOP_2 || res_OrLogicOP_3);
    res_OrLogicOP_2 = (res_OrLogicOP_2 || (argom68 == true));
    
    if(res_OrLogicOP_2){
    bool res_OrLogicOP_8 = false;
    bool res_OrLogicOP_9 = false;
    res_OrLogicOP_9 = (res_OrLogicOP_9 || (Counter_GetValore(L_P1__GetSubcl93(my_id)) == 112u));
    bool res_NotLogicOP_10 = true;
    bool res_NotLogicOP_11 = true;
    res_NotLogicOP_11 = (res_NotLogicOP_11 && ! (L_P1__GetInSubcl46(my_id) == false));
    res_NotLogicOP_10 = (res_NotLogicOP_10 && ! res_NotLogicOP_11);
    res_OrLogicOP_9 = (res_OrLogicOP_9 || res_NotLogicOP_10);
    
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_OrLogicOP_9);
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! Timer_Disattivo(L_P1__GetSubcl91(my_id)));
    res_OrLogicOP_8 = (res_OrLogicOP_8 || res_NotLogicOP_12);
    
    res_ImpliesLogicOp_1 = (res_ImpliesLogicOp_1 && res_OrLogicOP_8);
    }
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_ImpliesLogicOp_1);
    
    
    
    return res_AndLogicOP_0;
}


// Macro valorizzate

/*
    CNL corrispondente:
    
    { commento: {[}
     commento: {46,} assegna alla macro il valore  True  commento: {],}
    }
*/
bool L_P1__Macro27(instance_id_t const my_id , C3_Enumerat2 argom54, C3_Enumerat1 argom55, C3_Enumerat2 argom56)
{
return true;
}

/*
    CNL corrispondente:
    
    { commento: {[}
     commento: {46,} assegna alla macro il valore AC commento: {],}
    }
*/
C3_Enumerat4 L_P1__Macro28(instance_id_t const my_id , bool argom57, C3_Enumerat1 argom58, C3_Enumerat3 argom59)
{
return ac;
}



