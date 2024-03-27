
#include "Logica/ClasseMainClass_C1_priv.h"
#include "Logica/ClasseSubClass_C2_priv.h"
#include "Logica/ClasseSubClass_C3_priv.h"
#include "config.h"
#include "PlatformMacros.h"

int L_P1_C2_cmd_tmp_id = -1; 

// ********** Dichiarazione guardie **********

static bool L_P1__guard13(instance_id_t const my_id);

// ********** Dichiarazione comandi manuali **********
static bool L_P1__GetInEvent6(instance_id_t const my_id) ;

static void L_P1__SetOutEvent7(
	instance_id_t const my_id, 
	ManCmdResponse const value);



// ********** Definizione guardie **********

static bool L_P1__guard13(instance_id_t const my_id)
{
    bool res_AndLogicOP_0 = true;
    
    //  *86,*  Almeno una delle seguenti {
    //   *83,*  Tutte le seguenti {
    //   Ricezione del  comando manuale   SubClass_C2_command_comm4   *77,*
    //   *68,* *35,*  se il controllo SubClass_C2_controllo_C3 è  diverso da  True , Almeno una delle seguenti { 
    //   *38,*  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  *54,* 14, Verifica che   *47,*  *34,*  il parametro SubClass_C2_parametro_P8 non sia  uguale a  *53,* 4
    //   } Verifica che   *51,*  *,*  il contatore SubClass_C2_contatore_Co10 non sia  minore di  *55,* 15
    //  } *83,*  Tutte le seguenti {
    //   Ricezione del  comando manuale   SubClass_C2_command_comm4   *77,*
    //   *68,* *35,*  se il controllo SubClass_C2_controllo_C9 non è  uguale a RossoGiallo *37,* e  se la variabile SubClass_C2_variabile_V9 è  diverso da  True  *37,* o  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False  *37,* o  se la variabile SubClass_C2_variabile_V9 è  uguale a  True , Almeno una delle seguenti { 
    //   *69,*  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
    //   *68,* *35,*  se il controllo SubClass_C2_controllo_C3 è  diverso da  True  *36,* o  se il timer SubClass_C2_timer_T3 è scaduto, Almeno una delle seguenti { 
    //   *69,* *35,*  se il controllo SubClass_C2_controllo_C3 è  uguale a  True  *36,* o  se il timer SubClass_C2_timer_T8 è scaduto, Solo una delle seguenti { 
    //   *69,*  se il controllo ConsDef  è  uguale a FALSE  *36,* o  se il timer SubClass_C2_timer_T5 non è scaduto, Solo una delle seguenti { 
    //   *36,*  se il timer SubClass_C2_timer_T9 è attivo o  se il controllo ConsDef  è  uguale a FALSE  *37,* e  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False  *35,* e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  True , Verifica che   *49,*  *,*  il timer SubClass_C2_timer_T9 sia attivo
    //   } Verifica che   *49,*  *,*  il timer SubClass_C2_timer_T8 non sia scaduto
    //   } Verifica che   *51,*  *,*  il contatore SubClass_C2_contatore_Co10 sia  minore di  *55,* 13
    //   } Verifica che   *48,*  *,*  il controllo SubClass_C2_controllo_C3 non sia  diverso da  True 
    //   } Verifica che   *48,*   il controllo ConsDef  sia  uguale a FALSE 
    //   } Verifica che   *51,*  *,*  il contatore SubClass_C2_contatore_Co10 non sia  uguale a  *53,* 11215
    //  } *83,*  Tutte le seguenti {
    //   Ricezione del  comando manuale   SubClass_C2_command_comm4   *77,*
    //   *68,* *36,*  se il timer SubClass_C2_timer_T5 è scaduto *34,* o  se il parametro SubClass_C2_parametro_P8 è  diverso da  *56,* 2 *38,* o  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  *56,* 12 o  se il controllo ConsDef  è  uguale a FALSE  *38,* e  se il contatore SubClass_C2_contatore_Co10 è  uguale a  *53,* 124, Almeno una delle seguenti { 
    //   *69,* *37,*  se la variabile SubClass_C2_variabile_V5 non è  diverso da  True  *38,* o  se il contatore SubClass_C2_contatore_Co10 è  minore di  *55,* 130 *35,* e  se il controllo SubClass_C2_controllo_C3 è  uguale a  False  *36,* o  se il timer SubClass_C2_timer_T5 è attivo *38,* e  se il contatore SubClass_C2_contatore_Co10 è  minore di  *55,* 11321 *38,* o  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  *56,* 125, Solo una delle seguenti { 
    //   *68,* *38,*  se il contatore SubClass_C2_contatore_Co10 è  uguale a  *53,* 13403, Almeno una delle seguenti { 
    //   *69,*  se il controllo ConsDef  è  uguale a FALSE  *34,* o  se il parametro SubClass_C2_parametro_P8 è  uguale a  *53,* 6 *37,* o  se la variabile SubClass_C2_variabile_V9 è  diverso da  True  *35,* o  se il controllo SubClass_C2_controllo_C9 è  uguale a RossoGiallo *38,* e  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  *56,* 13 *38,* o  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  *54,* 15, Solo una delle seguenti { 
    //   *67,*  se il controllo ConsDef  è  uguale a FALSE  *38,* o  se il contatore SubClass_C2_contatore_Co10 è  minore di  *55,* 14 *34,* o  se il parametro SubClass_C2_parametro_P8 non è  uguale a  *53,* 7 *38,* o  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  *54,* 1421 o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
    //   *67,* *36,*  se il timer SubClass_C2_timer_T7 non è scaduto, Tutte le seguenti { 
    //   *69,* *38,*  se il contatore SubClass_C2_contatore_Co10 non è  minore di  *55,* 11540 *36,* e  se il timer SubClass_C2_timer_T9 è scaduto *38,* o  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  *56,* 11321 *35,* e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  False  *36,* e  se il timer SubClass_C2_timer_T5 è attivo, Solo una delle seguenti { 
    //   *68,* *34,*  se il parametro SubClass_C2_parametro_P8 è  minore di  *55,* 8 *37,* e  se la variabile SubClass_C2_variabile_V9 non è  diverso da  True  *34,* e  se il parametro SubClass_C2_parametro_P8 è  minore di  *55,* 9 *36,* e  se il timer SubClass_C2_timer_T5 è scaduto *38,* e  se il contatore SubClass_C2_contatore_Co10 non è  uguale a  *53,* 13, Almeno una delle seguenti { 
    //   *36,*  se il timer SubClass_C2_timer_T5 non è scaduto *34,* o  se il parametro SubClass_C2_parametro_P8 è  uguale a  *53,* 6 *37,* o  se la variabile SubClass_C2_variabile_V9 non è  uguale a  True  *37,* e  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False  *38,* e  se il contatore SubClass_C2_contatore_Co10 è  uguale a  *53,* 135 *38,* o  se il contatore SubClass_C2_contatore_Co10 non è  maggiore di  *54,* 11403, Verifica che   *49,*  *,*  il timer SubClass_C2_timer_T5 non sia disattivo
    //   } Verifica che   *48,*   il controllo ConsDef  sia  uguale a FALSE 
    //   } Verifica che   *50,*  *,*  la variabile SubClass_C2_variabile_V5 sia  uguale a  False 
    //   } Verifica che   *49,*  *,*  il timer SubClass_C2_timer_T5 sia disattivo
    //   } Verifica che   *47,*  *34,*  il parametro SubClass_C2_parametro_P8 sia  uguale a  *53,* 10
    //   } Verifica che   *48,*   il controllo ConsDef  sia  uguale a FALSE 
    //   } Verifica che   *48,*  *,*  il controllo SubClass_C2_controllo_C9 non sia  diverso da RossoGiallo
    //   } Verifica che   *48,*  *,*  il controllo SubClass_C2_controllo_C9 non sia  diverso da RossoGiallo
    //   } Verifica che   *48,*  *,*  il controllo SubClass_C2_controllo_C3 non sia  uguale a  True 
    //  } *83,*  Tutte le seguenti {
    //   Ricezione del  comando manuale   SubClass_C2_command_comm4   *77,*
    //   *69,* *38,*  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  *54,* 13 *35,* e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  False  *35,* e  se il controllo SubClass_C2_controllo_C3 non è  diverso da  False  *38,* o  se il contatore SubClass_C2_contatore_Co10 è  uguale a  *53,* 13215 *36,* e  se il timer SubClass_C2_timer_T9 è disattivo *38,* e  se il contatore SubClass_C2_contatore_Co10 non è  minore di  *55,* 14, Solo una delle seguenti { 
    //   *67,* *36,*  se il timer SubClass_C2_timer_T5 è disattivo *38,* e  se il contatore SubClass_C2_contatore_Co10 è  diverso da  *56,* 14403 *34,* o  se il parametro SubClass_C2_parametro_P8 è  diverso da  *56,* 1 *35,* e  se il controllo SubClass_C2_controllo_C9 è  diverso da RossoGiallo *36,* o  se il timer SubClass_C2_timer_T9 non è scaduto, Tutte le seguenti { 
    //   *67,* *35,*  se il controllo SubClass_C2_controllo_C9 è  uguale a RossoGiallo *34,* e  se il parametro SubClass_C2_parametro_P8 è  maggiore di  *54,* 2 *35,* o  se il controllo SubClass_C2_controllo_C3 non è  diverso da  False  *37,* o  se la variabile SubClass_C2_variabile_V5 non è  diverso da  False  *36,* e  se il timer SubClass_C2_timer_T8 è attivo *36,* e  se il timer SubClass_C2_timer_T5 non è disattivo, Tutte le seguenti { 
    //   *67,* *36,*  se il timer SubClass_C2_timer_T3 è disattivo *35,* e  se il controllo SubClass_C2_controllo_C9 è  uguale a RossoGiallo *37,* e  se la variabile SubClass_C2_variabile_V5 non è  uguale a  False , Tutte le seguenti { 
    //   *67,* *36,*  se il timer SubClass_C2_timer_T5 è scaduto, Tutte le seguenti { 
    //   *69,* *34,*  se il parametro SubClass_C2_parametro_P8 non è  minore di  *55,* 5 *38,* e  se il contatore SubClass_C2_contatore_Co10 è  diverso da  *56,* 15215 *36,* o  se il timer SubClass_C2_timer_T5 non è scaduto *35,* e  se il controllo SubClass_C2_controllo_C9 è  diverso da RossoGiallo *38,* e  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  *54,* 12403, Solo una delle seguenti { 
    //   *67,* *38,*  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  *56,* 11215 *35,* o  se il controllo SubClass_C2_controllo_C3 è  diverso da  False  *35,* o  se il controllo SubClass_C2_controllo_C3 è  uguale a  True , Tutte le seguenti { 
    //   *34,*  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  *54,* 7 *34,* o  se il parametro SubClass_C2_parametro_P8 non è  minore di  *55,* 4 *38,* o  se il contatore SubClass_C2_contatore_Co10 è  uguale a  *53,* 13, Verifica che   *47,*  *34,*  il parametro SubClass_C2_parametro_P8 sia  maggiore di  *54,* 9
    //   } Verifica che   *47,*  *34,*  il parametro SubClass_C2_parametro_P8 non sia  minore di  *55,* 3
    //   } Verifica che   *51,*  *,*  il contatore SubClass_C2_contatore_Co10 non sia  maggiore di  *54,* 154
    //   } Verifica che   *48,*   il controllo ConsDef  sia  uguale a FALSE 
    //   } Verifica che   *47,*  *34,*  il parametro SubClass_C2_parametro_P8 non sia  uguale a  *53,* 7
    //   } Verifica che   *51,*  *,*  il contatore SubClass_C2_contatore_Co10 non sia  uguale a  *53,* 13
    //   } Verifica che   *50,*  *,*  la variabile SubClass_C2_variabile_V5 sia  diverso da  False 
    //   } Verifica che   *50,*  *,*  la variabile SubClass_C2_variabile_V9 non sia  uguale a  True 
    //  }
    //  }
    bool res_OrLogicOP_1 = false;
    bool res_AndLogicOP_2 = true;
    res_AndLogicOP_2 = (res_AndLogicOP_2 && L_P1__GetInEvent6(my_id));
    bool res_ImpliesLogicOp_3 = true;
    bool res_NotLogicOP_4 = true;
    res_NotLogicOP_4 = (res_NotLogicOP_4 && ! (L_P1__GetInSubcl5(my_id) == true));
    if(res_NotLogicOP_4){
    bool res_ImpliesLogicOp_5 = true;
    if((Counter_GetValore(L_P1__GetSubcl36(my_id)) > 14u)){
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (L_P1__GetParamSubcl8(my_id) == 4u));
    res_ImpliesLogicOp_5 = (res_ImpliesLogicOp_5 && res_NotLogicOP_6);
    }
    res_ImpliesLogicOp_3 = (res_ImpliesLogicOp_3 && res_ImpliesLogicOp_5);
    }
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_ImpliesLogicOp_3);
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (Counter_GetValore(L_P1__GetSubcl36(my_id)) < 15u));
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_NotLogicOP_7);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_2);
    bool res_AndLogicOP_8 = true;
    res_AndLogicOP_8 = (res_AndLogicOP_8 && L_P1__GetInEvent6(my_id));
    bool res_ImpliesLogicOp_9 = true;
    bool res_OrLogicOP_10 = false;
    bool res_OrLogicOP_11 = false;
    bool res_AndLogicOP_12 = true;
    bool res_NotLogicOP_13 = true;
    res_NotLogicOP_13 = (res_NotLogicOP_13 && ! (L_P1__GetInSubcl6(my_id) == rossogiallo1));
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_NotLogicOP_13);
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1__GetSubcl28(my_id) == true));
    res_AndLogicOP_12 = (res_AndLogicOP_12 && res_NotLogicOP_14);
    
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_AndLogicOP_12);
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (L_P1__GetSubcl28(my_id) == false));
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_NotLogicOP_15);
    
    res_OrLogicOP_10 = (res_OrLogicOP_10 || res_OrLogicOP_11);
    res_OrLogicOP_10 = (res_OrLogicOP_10 || (L_P1__GetSubcl28(my_id) == true));
    
    if(res_OrLogicOP_10){
    bool res_OrLogicOP_16 = false;
    bool res_ImpliesLogicOp_17 = true;
    if((L_P1__GetInConsd1(my_id) == false)){
    bool res_XorLogicOP_18 = true;
    int xorIndex_res_XorLogicOP_18 = 0;
    bool res_ImpliesLogicOp_19 = true;
    bool res_OrLogicOP_20 = false;
    bool res_NotLogicOP_21 = true;
    res_NotLogicOP_21 = (res_NotLogicOP_21 && ! (L_P1__GetInSubcl5(my_id) == true));
    res_OrLogicOP_20 = (res_OrLogicOP_20 || res_NotLogicOP_21);
    res_OrLogicOP_20 = (res_OrLogicOP_20 || Timer_Scaduto(L_P1__GetSubcl31(my_id)));
    
    if(res_OrLogicOP_20){
    bool res_OrLogicOP_22 = false;
    bool res_ImpliesLogicOp_23 = true;
    bool res_OrLogicOP_24 = false;
    res_OrLogicOP_24 = (res_OrLogicOP_24 || (L_P1__GetInSubcl5(my_id) == true));
    res_OrLogicOP_24 = (res_OrLogicOP_24 || Timer_Scaduto(L_P1__GetSubcl34(my_id)));
    
    if(res_OrLogicOP_24){
    bool res_XorLogicOP_25 = true;
    int xorIndex_res_XorLogicOP_25 = 0;
    bool res_ImpliesLogicOp_26 = true;
    bool res_OrLogicOP_27 = false;
    res_OrLogicOP_27 = (res_OrLogicOP_27 || (L_P1__GetInConsd1(my_id) == false));
    bool res_NotLogicOP_28 = true;
    res_NotLogicOP_28 = (res_NotLogicOP_28 && ! Timer_Scaduto(L_P1__GetSubcl32(my_id)));
    res_OrLogicOP_27 = (res_OrLogicOP_27 || res_NotLogicOP_28);
    
    if(res_OrLogicOP_27){
    bool res_ImpliesLogicOp_29 = true;
    bool res_OrLogicOP_30 = false;
    res_OrLogicOP_30 = (res_OrLogicOP_30 || Timer_Attivo(L_P1__GetSubcl35(my_id)));
    bool res_AndLogicOP_31 = true;
    bool res_AndLogicOP_32 = true;
    res_AndLogicOP_32 = (res_AndLogicOP_32 && (L_P1__GetInConsd1(my_id) == false));
    bool res_NotLogicOP_33 = true;
    res_NotLogicOP_33 = (res_NotLogicOP_33 && ! (L_P1__GetSubcl28(my_id) == false));
    res_AndLogicOP_32 = (res_AndLogicOP_32 && res_NotLogicOP_33);
    
    res_AndLogicOP_31 = (res_AndLogicOP_31 && res_AndLogicOP_32);
    bool res_NotLogicOP_34 = true;
    res_NotLogicOP_34 = (res_NotLogicOP_34 && ! (L_P1__GetInSubcl5(my_id) == true));
    res_AndLogicOP_31 = (res_AndLogicOP_31 && res_NotLogicOP_34);
    
    res_OrLogicOP_30 = (res_OrLogicOP_30 || res_AndLogicOP_31);
    
    if(res_OrLogicOP_30){
    res_ImpliesLogicOp_29 = (res_ImpliesLogicOp_29 && Timer_Attivo(L_P1__GetSubcl35(my_id)));
    }
    res_ImpliesLogicOp_26 = (res_ImpliesLogicOp_26 && res_ImpliesLogicOp_29);
    }
    if(res_ImpliesLogicOp_26){
    xorIndex_res_XorLogicOP_25 = (xorIndex_res_XorLogicOP_25 + 1);
    }
    bool res_NotLogicOP_35 = true;
    res_NotLogicOP_35 = (res_NotLogicOP_35 && ! Timer_Scaduto(L_P1__GetSubcl34(my_id)));
    if(res_NotLogicOP_35){
    xorIndex_res_XorLogicOP_25 = (xorIndex_res_XorLogicOP_25 + 1);
    }
    
    res_XorLogicOP_25 = (res_XorLogicOP_25 && (xorIndex_res_XorLogicOP_25 == 1));
    res_ImpliesLogicOp_23 = (res_ImpliesLogicOp_23 && res_XorLogicOP_25);
    }
    res_OrLogicOP_22 = (res_OrLogicOP_22 || res_ImpliesLogicOp_23);
    res_OrLogicOP_22 = (res_OrLogicOP_22 || (Counter_GetValore(L_P1__GetSubcl36(my_id)) < 13u));
    
    res_ImpliesLogicOp_19 = (res_ImpliesLogicOp_19 && res_OrLogicOP_22);
    }
    if(res_ImpliesLogicOp_19){
    xorIndex_res_XorLogicOP_18 = (xorIndex_res_XorLogicOP_18 + 1);
    }
    bool res_NotLogicOP_36 = true;
    bool res_NotLogicOP_37 = true;
    res_NotLogicOP_37 = (res_NotLogicOP_37 && ! (L_P1__GetInSubcl5(my_id) == true));
    res_NotLogicOP_36 = (res_NotLogicOP_36 && ! res_NotLogicOP_37);
    if(res_NotLogicOP_36){
    xorIndex_res_XorLogicOP_18 = (xorIndex_res_XorLogicOP_18 + 1);
    }
    
    res_XorLogicOP_18 = (res_XorLogicOP_18 && (xorIndex_res_XorLogicOP_18 == 1));
    res_ImpliesLogicOp_17 = (res_ImpliesLogicOp_17 && res_XorLogicOP_18);
    }
    res_OrLogicOP_16 = (res_OrLogicOP_16 || res_ImpliesLogicOp_17);
    res_OrLogicOP_16 = (res_OrLogicOP_16 || (L_P1__GetInConsd1(my_id) == false));
    
    res_ImpliesLogicOp_9 = (res_ImpliesLogicOp_9 && res_OrLogicOP_16);
    }
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_ImpliesLogicOp_9);
    bool res_NotLogicOP_38 = true;
    res_NotLogicOP_38 = (res_NotLogicOP_38 && ! (Counter_GetValore(L_P1__GetSubcl36(my_id)) == 11215u));
    res_AndLogicOP_8 = (res_AndLogicOP_8 && res_NotLogicOP_38);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_8);
    bool res_AndLogicOP_39 = true;
    res_AndLogicOP_39 = (res_AndLogicOP_39 && L_P1__GetInEvent6(my_id));
    bool res_ImpliesLogicOp_40 = true;
    bool res_OrLogicOP_41 = false;
    bool res_OrLogicOP_42 = false;
    bool res_OrLogicOP_43 = false;
    res_OrLogicOP_43 = (res_OrLogicOP_43 || Timer_Scaduto(L_P1__GetSubcl32(my_id)));
    bool res_NotLogicOP_44 = true;
    res_NotLogicOP_44 = (res_NotLogicOP_44 && ! (L_P1__GetParamSubcl8(my_id) == 2u));
    res_OrLogicOP_43 = (res_OrLogicOP_43 || res_NotLogicOP_44);
    
    res_OrLogicOP_42 = (res_OrLogicOP_42 || res_OrLogicOP_43);
    bool res_NotLogicOP_45 = true;
    bool res_NotLogicOP_46 = true;
    res_NotLogicOP_46 = (res_NotLogicOP_46 && ! (Counter_GetValore(L_P1__GetSubcl36(my_id)) == 12u));
    res_NotLogicOP_45 = (res_NotLogicOP_45 && ! res_NotLogicOP_46);
    res_OrLogicOP_42 = (res_OrLogicOP_42 || res_NotLogicOP_45);
    
    res_OrLogicOP_41 = (res_OrLogicOP_41 || res_OrLogicOP_42);
    bool res_AndLogicOP_47 = true;
    res_AndLogicOP_47 = (res_AndLogicOP_47 && (L_P1__GetInConsd1(my_id) == false));
    res_AndLogicOP_47 = (res_AndLogicOP_47 && (Counter_GetValore(L_P1__GetSubcl36(my_id)) == 124u));
    
    res_OrLogicOP_41 = (res_OrLogicOP_41 || res_AndLogicOP_47);
    
    if(res_OrLogicOP_41){
    bool res_OrLogicOP_48 = false;
    bool res_ImpliesLogicOp_49 = true;
    bool res_OrLogicOP_50 = false;
    bool res_OrLogicOP_51 = false;
    bool res_OrLogicOP_52 = false;
    bool res_NotLogicOP_53 = true;
    bool res_NotLogicOP_54 = true;
    res_NotLogicOP_54 = (res_NotLogicOP_54 && ! (L_P1__GetSubcl27(my_id) == true));
    res_NotLogicOP_53 = (res_NotLogicOP_53 && ! res_NotLogicOP_54);
    res_OrLogicOP_52 = (res_OrLogicOP_52 || res_NotLogicOP_53);
    bool res_AndLogicOP_55 = true;
    res_AndLogicOP_55 = (res_AndLogicOP_55 && (Counter_GetValore(L_P1__GetSubcl36(my_id)) < 130u));
    res_AndLogicOP_55 = (res_AndLogicOP_55 && (L_P1__GetInSubcl5(my_id) == false));
    
    res_OrLogicOP_52 = (res_OrLogicOP_52 || res_AndLogicOP_55);
    
    res_OrLogicOP_51 = (res_OrLogicOP_51 || res_OrLogicOP_52);
    bool res_AndLogicOP_56 = true;
    res_AndLogicOP_56 = (res_AndLogicOP_56 && Timer_Attivo(L_P1__GetSubcl32(my_id)));
    res_AndLogicOP_56 = (res_AndLogicOP_56 && (Counter_GetValore(L_P1__GetSubcl36(my_id)) < 11321u));
    
    res_OrLogicOP_51 = (res_OrLogicOP_51 || res_AndLogicOP_56);
    
    res_OrLogicOP_50 = (res_OrLogicOP_50 || res_OrLogicOP_51);
    bool res_NotLogicOP_57 = true;
    bool res_NotLogicOP_58 = true;
    res_NotLogicOP_58 = (res_NotLogicOP_58 && ! (Counter_GetValore(L_P1__GetSubcl36(my_id)) == 125u));
    res_NotLogicOP_57 = (res_NotLogicOP_57 && ! res_NotLogicOP_58);
    res_OrLogicOP_50 = (res_OrLogicOP_50 || res_NotLogicOP_57);
    
    if(res_OrLogicOP_50){
    bool res_XorLogicOP_59 = true;
    int xorIndex_res_XorLogicOP_59 = 0;
    bool res_ImpliesLogicOp_60 = true;
    if((Counter_GetValore(L_P1__GetSubcl36(my_id)) == 13403u)){
    bool res_OrLogicOP_61 = false;
    bool res_ImpliesLogicOp_62 = true;
    bool res_OrLogicOP_63 = false;
    bool res_OrLogicOP_64 = false;
    bool res_OrLogicOP_65 = false;
    bool res_OrLogicOP_66 = false;
    res_OrLogicOP_66 = (res_OrLogicOP_66 || (L_P1__GetInConsd1(my_id) == false));
    res_OrLogicOP_66 = (res_OrLogicOP_66 || (L_P1__GetParamSubcl8(my_id) == 6u));
    
    res_OrLogicOP_65 = (res_OrLogicOP_65 || res_OrLogicOP_66);
    bool res_NotLogicOP_67 = true;
    res_NotLogicOP_67 = (res_NotLogicOP_67 && ! (L_P1__GetSubcl28(my_id) == true));
    res_OrLogicOP_65 = (res_OrLogicOP_65 || res_NotLogicOP_67);
    
    res_OrLogicOP_64 = (res_OrLogicOP_64 || res_OrLogicOP_65);
    bool res_AndLogicOP_68 = true;
    res_AndLogicOP_68 = (res_AndLogicOP_68 && (L_P1__GetInSubcl6(my_id) == rossogiallo1));
    bool res_NotLogicOP_69 = true;
    bool res_NotLogicOP_70 = true;
    res_NotLogicOP_70 = (res_NotLogicOP_70 && ! (Counter_GetValore(L_P1__GetSubcl36(my_id)) == 13u));
    res_NotLogicOP_69 = (res_NotLogicOP_69 && ! res_NotLogicOP_70);
    res_AndLogicOP_68 = (res_AndLogicOP_68 && res_NotLogicOP_69);
    
    res_OrLogicOP_64 = (res_OrLogicOP_64 || res_AndLogicOP_68);
    
    res_OrLogicOP_63 = (res_OrLogicOP_63 || res_OrLogicOP_64);
    res_OrLogicOP_63 = (res_OrLogicOP_63 || (Counter_GetValore(L_P1__GetSubcl36(my_id)) > 15u));
    
    if(res_OrLogicOP_63){
    bool res_XorLogicOP_71 = true;
    int xorIndex_res_XorLogicOP_71 = 0;
    bool res_ImpliesLogicOp_72 = true;
    bool res_OrLogicOP_73 = false;
    bool res_OrLogicOP_74 = false;
    bool res_OrLogicOP_75 = false;
    bool res_OrLogicOP_76 = false;
    res_OrLogicOP_76 = (res_OrLogicOP_76 || (L_P1__GetInConsd1(my_id) == false));
    res_OrLogicOP_76 = (res_OrLogicOP_76 || (Counter_GetValore(L_P1__GetSubcl36(my_id)) < 14u));
    
    res_OrLogicOP_75 = (res_OrLogicOP_75 || res_OrLogicOP_76);
    bool res_NotLogicOP_77 = true;
    res_NotLogicOP_77 = (res_NotLogicOP_77 && ! (L_P1__GetParamSubcl8(my_id) == 7u));
    res_OrLogicOP_75 = (res_OrLogicOP_75 || res_NotLogicOP_77);
    
    res_OrLogicOP_74 = (res_OrLogicOP_74 || res_OrLogicOP_75);
    res_OrLogicOP_74 = (res_OrLogicOP_74 || (Counter_GetValore(L_P1__GetSubcl36(my_id)) > 1421u));
    
    res_OrLogicOP_73 = (res_OrLogicOP_73 || res_OrLogicOP_74);
    res_OrLogicOP_73 = (res_OrLogicOP_73 || (L_P1__GetInConsd1(my_id) == false));
    
    if(res_OrLogicOP_73){
    bool res_AndLogicOP_78 = true;
    bool res_ImpliesLogicOp_79 = true;
    bool res_NotLogicOP_80 = true;
    res_NotLogicOP_80 = (res_NotLogicOP_80 && ! Timer_Scaduto(L_P1__GetSubcl33(my_id)));
    if(res_NotLogicOP_80){
    bool res_AndLogicOP_81 = true;
    bool res_ImpliesLogicOp_82 = true;
    bool res_OrLogicOP_83 = false;
    bool res_AndLogicOP_84 = true;
    bool res_NotLogicOP_85 = true;
    res_NotLogicOP_85 = (res_NotLogicOP_85 && ! (Counter_GetValore(L_P1__GetSubcl36(my_id)) < 11540u));
    res_AndLogicOP_84 = (res_AndLogicOP_84 && res_NotLogicOP_85);
    res_AndLogicOP_84 = (res_AndLogicOP_84 && Timer_Scaduto(L_P1__GetSubcl35(my_id)));
    
    res_OrLogicOP_83 = (res_OrLogicOP_83 || res_AndLogicOP_84);
    bool res_AndLogicOP_86 = true;
    bool res_AndLogicOP_87 = true;
    bool res_NotLogicOP_88 = true;
    bool res_NotLogicOP_89 = true;
    res_NotLogicOP_89 = (res_NotLogicOP_89 && ! (Counter_GetValore(L_P1__GetSubcl36(my_id)) == 11321u));
    res_NotLogicOP_88 = (res_NotLogicOP_88 && ! res_NotLogicOP_89);
    res_AndLogicOP_87 = (res_AndLogicOP_87 && res_NotLogicOP_88);
    bool res_NotLogicOP_90 = true;
    res_NotLogicOP_90 = (res_NotLogicOP_90 && ! (L_P1__GetInSubcl5(my_id) == false));
    res_AndLogicOP_87 = (res_AndLogicOP_87 && res_NotLogicOP_90);
    
    res_AndLogicOP_86 = (res_AndLogicOP_86 && res_AndLogicOP_87);
    res_AndLogicOP_86 = (res_AndLogicOP_86 && Timer_Attivo(L_P1__GetSubcl32(my_id)));
    
    res_OrLogicOP_83 = (res_OrLogicOP_83 || res_AndLogicOP_86);
    
    if(res_OrLogicOP_83){
    bool res_XorLogicOP_91 = true;
    int xorIndex_res_XorLogicOP_91 = 0;
    bool res_ImpliesLogicOp_92 = true;
    bool res_AndLogicOP_93 = true;
    bool res_AndLogicOP_94 = true;
    bool res_AndLogicOP_95 = true;
    bool res_AndLogicOP_96 = true;
    res_AndLogicOP_96 = (res_AndLogicOP_96 && (L_P1__GetParamSubcl8(my_id) < 8u));
    bool res_NotLogicOP_97 = true;
    bool res_NotLogicOP_98 = true;
    res_NotLogicOP_98 = (res_NotLogicOP_98 && ! (L_P1__GetSubcl28(my_id) == true));
    res_NotLogicOP_97 = (res_NotLogicOP_97 && ! res_NotLogicOP_98);
    res_AndLogicOP_96 = (res_AndLogicOP_96 && res_NotLogicOP_97);
    
    res_AndLogicOP_95 = (res_AndLogicOP_95 && res_AndLogicOP_96);
    res_AndLogicOP_95 = (res_AndLogicOP_95 && (L_P1__GetParamSubcl8(my_id) < 9u));
    
    res_AndLogicOP_94 = (res_AndLogicOP_94 && res_AndLogicOP_95);
    res_AndLogicOP_94 = (res_AndLogicOP_94 && Timer_Scaduto(L_P1__GetSubcl32(my_id)));
    
    res_AndLogicOP_93 = (res_AndLogicOP_93 && res_AndLogicOP_94);
    bool res_NotLogicOP_99 = true;
    res_NotLogicOP_99 = (res_NotLogicOP_99 && ! (Counter_GetValore(L_P1__GetSubcl36(my_id)) == 13u));
    res_AndLogicOP_93 = (res_AndLogicOP_93 && res_NotLogicOP_99);
    
    if(res_AndLogicOP_93){
    bool res_ImpliesLogicOp_100 = true;
    bool res_OrLogicOP_101 = false;
    bool res_OrLogicOP_102 = false;
    bool res_OrLogicOP_103 = false;
    bool res_NotLogicOP_104 = true;
    res_NotLogicOP_104 = (res_NotLogicOP_104 && ! Timer_Scaduto(L_P1__GetSubcl32(my_id)));
    res_OrLogicOP_103 = (res_OrLogicOP_103 || res_NotLogicOP_104);
    res_OrLogicOP_103 = (res_OrLogicOP_103 || (L_P1__GetParamSubcl8(my_id) == 6u));
    
    res_OrLogicOP_102 = (res_OrLogicOP_102 || res_OrLogicOP_103);
    bool res_AndLogicOP_105 = true;
    bool res_AndLogicOP_106 = true;
    bool res_NotLogicOP_107 = true;
    res_NotLogicOP_107 = (res_NotLogicOP_107 && ! (L_P1__GetSubcl28(my_id) == true));
    res_AndLogicOP_106 = (res_AndLogicOP_106 && res_NotLogicOP_107);
    bool res_NotLogicOP_108 = true;
    res_NotLogicOP_108 = (res_NotLogicOP_108 && ! (L_P1__GetSubcl28(my_id) == false));
    res_AndLogicOP_106 = (res_AndLogicOP_106 && res_NotLogicOP_108);
    
    res_AndLogicOP_105 = (res_AndLogicOP_105 && res_AndLogicOP_106);
    res_AndLogicOP_105 = (res_AndLogicOP_105 && (Counter_GetValore(L_P1__GetSubcl36(my_id)) == 135u));
    
    res_OrLogicOP_102 = (res_OrLogicOP_102 || res_AndLogicOP_105);
    
    res_OrLogicOP_101 = (res_OrLogicOP_101 || res_OrLogicOP_102);
    bool res_NotLogicOP_109 = true;
    res_NotLogicOP_109 = (res_NotLogicOP_109 && ! (Counter_GetValore(L_P1__GetSubcl36(my_id)) > 11403u));
    res_OrLogicOP_101 = (res_OrLogicOP_101 || res_NotLogicOP_109);
    
    if(res_OrLogicOP_101){
    bool res_NotLogicOP_110 = true;
    res_NotLogicOP_110 = (res_NotLogicOP_110 && ! Timer_Disattivo(L_P1__GetSubcl32(my_id)));
    res_ImpliesLogicOp_100 = (res_ImpliesLogicOp_100 && res_NotLogicOP_110);
    }
    res_ImpliesLogicOp_92 = (res_ImpliesLogicOp_92 && res_ImpliesLogicOp_100);
    }
    if(res_ImpliesLogicOp_92){
    xorIndex_res_XorLogicOP_91 = (xorIndex_res_XorLogicOP_91 + 1);
    }
    if((L_P1__GetInConsd1(my_id) == false)){
    xorIndex_res_XorLogicOP_91 = (xorIndex_res_XorLogicOP_91 + 1);
    }
    
    res_XorLogicOP_91 = (res_XorLogicOP_91 && (xorIndex_res_XorLogicOP_91 == 1));
    res_ImpliesLogicOp_82 = (res_ImpliesLogicOp_82 && res_XorLogicOP_91);
    }
    res_AndLogicOP_81 = (res_AndLogicOP_81 && res_ImpliesLogicOp_82);
    res_AndLogicOP_81 = (res_AndLogicOP_81 && (L_P1__GetSubcl27(my_id) == false));
    
    res_ImpliesLogicOp_79 = (res_ImpliesLogicOp_79 && res_AndLogicOP_81);
    }
    res_AndLogicOP_78 = (res_AndLogicOP_78 && res_ImpliesLogicOp_79);
    res_AndLogicOP_78 = (res_AndLogicOP_78 && Timer_Disattivo(L_P1__GetSubcl32(my_id)));
    
    res_ImpliesLogicOp_72 = (res_ImpliesLogicOp_72 && res_AndLogicOP_78);
    }
    if(res_ImpliesLogicOp_72){
    xorIndex_res_XorLogicOP_71 = (xorIndex_res_XorLogicOP_71 + 1);
    }
    if((L_P1__GetParamSubcl8(my_id) == 10u)){
    xorIndex_res_XorLogicOP_71 = (xorIndex_res_XorLogicOP_71 + 1);
    }
    
    res_XorLogicOP_71 = (res_XorLogicOP_71 && (xorIndex_res_XorLogicOP_71 == 1));
    res_ImpliesLogicOp_62 = (res_ImpliesLogicOp_62 && res_XorLogicOP_71);
    }
    res_OrLogicOP_61 = (res_OrLogicOP_61 || res_ImpliesLogicOp_62);
    res_OrLogicOP_61 = (res_OrLogicOP_61 || (L_P1__GetInConsd1(my_id) == false));
    
    res_ImpliesLogicOp_60 = (res_ImpliesLogicOp_60 && res_OrLogicOP_61);
    }
    if(res_ImpliesLogicOp_60){
    xorIndex_res_XorLogicOP_59 = (xorIndex_res_XorLogicOP_59 + 1);
    }
    bool res_NotLogicOP_111 = true;
    bool res_NotLogicOP_112 = true;
    res_NotLogicOP_112 = (res_NotLogicOP_112 && ! (L_P1__GetInSubcl6(my_id) == rossogiallo1));
    res_NotLogicOP_111 = (res_NotLogicOP_111 && ! res_NotLogicOP_112);
    if(res_NotLogicOP_111){
    xorIndex_res_XorLogicOP_59 = (xorIndex_res_XorLogicOP_59 + 1);
    }
    
    res_XorLogicOP_59 = (res_XorLogicOP_59 && (xorIndex_res_XorLogicOP_59 == 1));
    res_ImpliesLogicOp_49 = (res_ImpliesLogicOp_49 && res_XorLogicOP_59);
    }
    res_OrLogicOP_48 = (res_OrLogicOP_48 || res_ImpliesLogicOp_49);
    bool res_NotLogicOP_113 = true;
    bool res_NotLogicOP_114 = true;
    res_NotLogicOP_114 = (res_NotLogicOP_114 && ! (L_P1__GetInSubcl6(my_id) == rossogiallo1));
    res_NotLogicOP_113 = (res_NotLogicOP_113 && ! res_NotLogicOP_114);
    res_OrLogicOP_48 = (res_OrLogicOP_48 || res_NotLogicOP_113);
    
    res_ImpliesLogicOp_40 = (res_ImpliesLogicOp_40 && res_OrLogicOP_48);
    }
    res_AndLogicOP_39 = (res_AndLogicOP_39 && res_ImpliesLogicOp_40);
    bool res_NotLogicOP_115 = true;
    res_NotLogicOP_115 = (res_NotLogicOP_115 && ! (L_P1__GetInSubcl5(my_id) == true));
    res_AndLogicOP_39 = (res_AndLogicOP_39 && res_NotLogicOP_115);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_39);
    bool res_AndLogicOP_116 = true;
    res_AndLogicOP_116 = (res_AndLogicOP_116 && L_P1__GetInEvent6(my_id));
    bool res_ImpliesLogicOp_117 = true;
    bool res_OrLogicOP_118 = false;
    bool res_AndLogicOP_119 = true;
    bool res_AndLogicOP_120 = true;
    res_AndLogicOP_120 = (res_AndLogicOP_120 && (Counter_GetValore(L_P1__GetSubcl36(my_id)) > 13u));
    bool res_NotLogicOP_121 = true;
    res_NotLogicOP_121 = (res_NotLogicOP_121 && ! (L_P1__GetInSubcl5(my_id) == false));
    res_AndLogicOP_120 = (res_AndLogicOP_120 && res_NotLogicOP_121);
    
    res_AndLogicOP_119 = (res_AndLogicOP_119 && res_AndLogicOP_120);
    bool res_NotLogicOP_122 = true;
    bool res_NotLogicOP_123 = true;
    res_NotLogicOP_123 = (res_NotLogicOP_123 && ! (L_P1__GetInSubcl5(my_id) == false));
    res_NotLogicOP_122 = (res_NotLogicOP_122 && ! res_NotLogicOP_123);
    res_AndLogicOP_119 = (res_AndLogicOP_119 && res_NotLogicOP_122);
    
    res_OrLogicOP_118 = (res_OrLogicOP_118 || res_AndLogicOP_119);
    bool res_AndLogicOP_124 = true;
    bool res_AndLogicOP_125 = true;
    res_AndLogicOP_125 = (res_AndLogicOP_125 && (Counter_GetValore(L_P1__GetSubcl36(my_id)) == 13215u));
    res_AndLogicOP_125 = (res_AndLogicOP_125 && Timer_Disattivo(L_P1__GetSubcl35(my_id)));
    
    res_AndLogicOP_124 = (res_AndLogicOP_124 && res_AndLogicOP_125);
    bool res_NotLogicOP_126 = true;
    res_NotLogicOP_126 = (res_NotLogicOP_126 && ! (Counter_GetValore(L_P1__GetSubcl36(my_id)) < 14u));
    res_AndLogicOP_124 = (res_AndLogicOP_124 && res_NotLogicOP_126);
    
    res_OrLogicOP_118 = (res_OrLogicOP_118 || res_AndLogicOP_124);
    
    if(res_OrLogicOP_118){
    bool res_XorLogicOP_127 = true;
    int xorIndex_res_XorLogicOP_127 = 0;
    bool res_ImpliesLogicOp_128 = true;
    bool res_OrLogicOP_129 = false;
    bool res_OrLogicOP_130 = false;
    bool res_AndLogicOP_131 = true;
    res_AndLogicOP_131 = (res_AndLogicOP_131 && Timer_Disattivo(L_P1__GetSubcl32(my_id)));
    bool res_NotLogicOP_132 = true;
    res_NotLogicOP_132 = (res_NotLogicOP_132 && ! (Counter_GetValore(L_P1__GetSubcl36(my_id)) == 14403u));
    res_AndLogicOP_131 = (res_AndLogicOP_131 && res_NotLogicOP_132);
    
    res_OrLogicOP_130 = (res_OrLogicOP_130 || res_AndLogicOP_131);
    bool res_AndLogicOP_133 = true;
    bool res_NotLogicOP_134 = true;
    res_NotLogicOP_134 = (res_NotLogicOP_134 && ! (L_P1__GetParamSubcl8(my_id) == 1u));
    res_AndLogicOP_133 = (res_AndLogicOP_133 && res_NotLogicOP_134);
    bool res_NotLogicOP_135 = true;
    res_NotLogicOP_135 = (res_NotLogicOP_135 && ! (L_P1__GetInSubcl6(my_id) == rossogiallo1));
    res_AndLogicOP_133 = (res_AndLogicOP_133 && res_NotLogicOP_135);
    
    res_OrLogicOP_130 = (res_OrLogicOP_130 || res_AndLogicOP_133);
    
    res_OrLogicOP_129 = (res_OrLogicOP_129 || res_OrLogicOP_130);
    bool res_NotLogicOP_136 = true;
    res_NotLogicOP_136 = (res_NotLogicOP_136 && ! Timer_Scaduto(L_P1__GetSubcl35(my_id)));
    res_OrLogicOP_129 = (res_OrLogicOP_129 || res_NotLogicOP_136);
    
    if(res_OrLogicOP_129){
    bool res_AndLogicOP_137 = true;
    bool res_ImpliesLogicOp_138 = true;
    bool res_OrLogicOP_139 = false;
    bool res_OrLogicOP_140 = false;
    bool res_AndLogicOP_141 = true;
    res_AndLogicOP_141 = (res_AndLogicOP_141 && (L_P1__GetInSubcl6(my_id) == rossogiallo1));
    res_AndLogicOP_141 = (res_AndLogicOP_141 && (L_P1__GetParamSubcl8(my_id) > 2u));
    
    res_OrLogicOP_140 = (res_OrLogicOP_140 || res_AndLogicOP_141);
    bool res_NotLogicOP_142 = true;
    bool res_NotLogicOP_143 = true;
    res_NotLogicOP_143 = (res_NotLogicOP_143 && ! (L_P1__GetInSubcl5(my_id) == false));
    res_NotLogicOP_142 = (res_NotLogicOP_142 && ! res_NotLogicOP_143);
    res_OrLogicOP_140 = (res_OrLogicOP_140 || res_NotLogicOP_142);
    
    res_OrLogicOP_139 = (res_OrLogicOP_139 || res_OrLogicOP_140);
    bool res_AndLogicOP_144 = true;
    bool res_AndLogicOP_145 = true;
    bool res_NotLogicOP_146 = true;
    bool res_NotLogicOP_147 = true;
    res_NotLogicOP_147 = (res_NotLogicOP_147 && ! (L_P1__GetSubcl27(my_id) == false));
    res_NotLogicOP_146 = (res_NotLogicOP_146 && ! res_NotLogicOP_147);
    res_AndLogicOP_145 = (res_AndLogicOP_145 && res_NotLogicOP_146);
    res_AndLogicOP_145 = (res_AndLogicOP_145 && Timer_Attivo(L_P1__GetSubcl34(my_id)));
    
    res_AndLogicOP_144 = (res_AndLogicOP_144 && res_AndLogicOP_145);
    bool res_NotLogicOP_148 = true;
    res_NotLogicOP_148 = (res_NotLogicOP_148 && ! Timer_Disattivo(L_P1__GetSubcl32(my_id)));
    res_AndLogicOP_144 = (res_AndLogicOP_144 && res_NotLogicOP_148);
    
    res_OrLogicOP_139 = (res_OrLogicOP_139 || res_AndLogicOP_144);
    
    if(res_OrLogicOP_139){
    bool res_AndLogicOP_149 = true;
    bool res_ImpliesLogicOp_150 = true;
    bool res_AndLogicOP_151 = true;
    bool res_AndLogicOP_152 = true;
    res_AndLogicOP_152 = (res_AndLogicOP_152 && Timer_Disattivo(L_P1__GetSubcl31(my_id)));
    res_AndLogicOP_152 = (res_AndLogicOP_152 && (L_P1__GetInSubcl6(my_id) == rossogiallo1));
    
    res_AndLogicOP_151 = (res_AndLogicOP_151 && res_AndLogicOP_152);
    bool res_NotLogicOP_153 = true;
    res_NotLogicOP_153 = (res_NotLogicOP_153 && ! (L_P1__GetSubcl27(my_id) == false));
    res_AndLogicOP_151 = (res_AndLogicOP_151 && res_NotLogicOP_153);
    
    if(res_AndLogicOP_151){
    bool res_AndLogicOP_154 = true;
    bool res_ImpliesLogicOp_155 = true;
    if(Timer_Scaduto(L_P1__GetSubcl32(my_id))){
    bool res_AndLogicOP_156 = true;
    bool res_ImpliesLogicOp_157 = true;
    bool res_OrLogicOP_158 = false;
    bool res_AndLogicOP_159 = true;
    bool res_NotLogicOP_160 = true;
    res_NotLogicOP_160 = (res_NotLogicOP_160 && ! (L_P1__GetParamSubcl8(my_id) < 5u));
    res_AndLogicOP_159 = (res_AndLogicOP_159 && res_NotLogicOP_160);
    bool res_NotLogicOP_161 = true;
    res_NotLogicOP_161 = (res_NotLogicOP_161 && ! (Counter_GetValore(L_P1__GetSubcl36(my_id)) == 15215u));
    res_AndLogicOP_159 = (res_AndLogicOP_159 && res_NotLogicOP_161);
    
    res_OrLogicOP_158 = (res_OrLogicOP_158 || res_AndLogicOP_159);
    bool res_AndLogicOP_162 = true;
    bool res_AndLogicOP_163 = true;
    bool res_NotLogicOP_164 = true;
    res_NotLogicOP_164 = (res_NotLogicOP_164 && ! Timer_Scaduto(L_P1__GetSubcl32(my_id)));
    res_AndLogicOP_163 = (res_AndLogicOP_163 && res_NotLogicOP_164);
    bool res_NotLogicOP_165 = true;
    res_NotLogicOP_165 = (res_NotLogicOP_165 && ! (L_P1__GetInSubcl6(my_id) == rossogiallo1));
    res_AndLogicOP_163 = (res_AndLogicOP_163 && res_NotLogicOP_165);
    
    res_AndLogicOP_162 = (res_AndLogicOP_162 && res_AndLogicOP_163);
    res_AndLogicOP_162 = (res_AndLogicOP_162 && (Counter_GetValore(L_P1__GetSubcl36(my_id)) > 12403u));
    
    res_OrLogicOP_158 = (res_OrLogicOP_158 || res_AndLogicOP_162);
    
    if(res_OrLogicOP_158){
    bool res_XorLogicOP_166 = true;
    int xorIndex_res_XorLogicOP_166 = 0;
    bool res_ImpliesLogicOp_167 = true;
    bool res_OrLogicOP_168 = false;
    bool res_OrLogicOP_169 = false;
    bool res_NotLogicOP_170 = true;
    bool res_NotLogicOP_171 = true;
    res_NotLogicOP_171 = (res_NotLogicOP_171 && ! (Counter_GetValore(L_P1__GetSubcl36(my_id)) == 11215u));
    res_NotLogicOP_170 = (res_NotLogicOP_170 && ! res_NotLogicOP_171);
    res_OrLogicOP_169 = (res_OrLogicOP_169 || res_NotLogicOP_170);
    bool res_NotLogicOP_172 = true;
    res_NotLogicOP_172 = (res_NotLogicOP_172 && ! (L_P1__GetInSubcl5(my_id) == false));
    res_OrLogicOP_169 = (res_OrLogicOP_169 || res_NotLogicOP_172);
    
    res_OrLogicOP_168 = (res_OrLogicOP_168 || res_OrLogicOP_169);
    res_OrLogicOP_168 = (res_OrLogicOP_168 || (L_P1__GetInSubcl5(my_id) == true));
    
    if(res_OrLogicOP_168){
    bool res_ImpliesLogicOp_173 = true;
    bool res_OrLogicOP_174 = false;
    bool res_OrLogicOP_175 = false;
    bool res_NotLogicOP_176 = true;
    res_NotLogicOP_176 = (res_NotLogicOP_176 && ! (L_P1__GetParamSubcl8(my_id) > 7u));
    res_OrLogicOP_175 = (res_OrLogicOP_175 || res_NotLogicOP_176);
    bool res_NotLogicOP_177 = true;
    res_NotLogicOP_177 = (res_NotLogicOP_177 && ! (L_P1__GetParamSubcl8(my_id) < 4u));
    res_OrLogicOP_175 = (res_OrLogicOP_175 || res_NotLogicOP_177);
    
    res_OrLogicOP_174 = (res_OrLogicOP_174 || res_OrLogicOP_175);
    res_OrLogicOP_174 = (res_OrLogicOP_174 || (Counter_GetValore(L_P1__GetSubcl36(my_id)) == 13u));
    
    if(res_OrLogicOP_174){
    res_ImpliesLogicOp_173 = (res_ImpliesLogicOp_173 && (L_P1__GetParamSubcl8(my_id) > 9u));
    }
    res_ImpliesLogicOp_167 = (res_ImpliesLogicOp_167 && res_ImpliesLogicOp_173);
    }
    if(res_ImpliesLogicOp_167){
    xorIndex_res_XorLogicOP_166 = (xorIndex_res_XorLogicOP_166 + 1);
    }
    bool res_NotLogicOP_178 = true;
    res_NotLogicOP_178 = (res_NotLogicOP_178 && ! (L_P1__GetParamSubcl8(my_id) < 3u));
    if(res_NotLogicOP_178){
    xorIndex_res_XorLogicOP_166 = (xorIndex_res_XorLogicOP_166 + 1);
    }
    
    res_XorLogicOP_166 = (res_XorLogicOP_166 && (xorIndex_res_XorLogicOP_166 == 1));
    res_ImpliesLogicOp_157 = (res_ImpliesLogicOp_157 && res_XorLogicOP_166);
    }
    res_AndLogicOP_156 = (res_AndLogicOP_156 && res_ImpliesLogicOp_157);
    bool res_NotLogicOP_179 = true;
    res_NotLogicOP_179 = (res_NotLogicOP_179 && ! (Counter_GetValore(L_P1__GetSubcl36(my_id)) > 154u));
    res_AndLogicOP_156 = (res_AndLogicOP_156 && res_NotLogicOP_179);
    
    res_ImpliesLogicOp_155 = (res_ImpliesLogicOp_155 && res_AndLogicOP_156);
    }
    res_AndLogicOP_154 = (res_AndLogicOP_154 && res_ImpliesLogicOp_155);
    res_AndLogicOP_154 = (res_AndLogicOP_154 && (L_P1__GetInConsd1(my_id) == false));
    
    res_ImpliesLogicOp_150 = (res_ImpliesLogicOp_150 && res_AndLogicOP_154);
    }
    res_AndLogicOP_149 = (res_AndLogicOP_149 && res_ImpliesLogicOp_150);
    bool res_NotLogicOP_180 = true;
    res_NotLogicOP_180 = (res_NotLogicOP_180 && ! (L_P1__GetParamSubcl8(my_id) == 7u));
    res_AndLogicOP_149 = (res_AndLogicOP_149 && res_NotLogicOP_180);
    
    res_ImpliesLogicOp_138 = (res_ImpliesLogicOp_138 && res_AndLogicOP_149);
    }
    res_AndLogicOP_137 = (res_AndLogicOP_137 && res_ImpliesLogicOp_138);
    bool res_NotLogicOP_181 = true;
    res_NotLogicOP_181 = (res_NotLogicOP_181 && ! (Counter_GetValore(L_P1__GetSubcl36(my_id)) == 13u));
    res_AndLogicOP_137 = (res_AndLogicOP_137 && res_NotLogicOP_181);
    
    res_ImpliesLogicOp_128 = (res_ImpliesLogicOp_128 && res_AndLogicOP_137);
    }
    if(res_ImpliesLogicOp_128){
    xorIndex_res_XorLogicOP_127 = (xorIndex_res_XorLogicOP_127 + 1);
    }
    bool res_NotLogicOP_182 = true;
    res_NotLogicOP_182 = (res_NotLogicOP_182 && ! (L_P1__GetSubcl27(my_id) == false));
    if(res_NotLogicOP_182){
    xorIndex_res_XorLogicOP_127 = (xorIndex_res_XorLogicOP_127 + 1);
    }
    
    res_XorLogicOP_127 = (res_XorLogicOP_127 && (xorIndex_res_XorLogicOP_127 == 1));
    res_ImpliesLogicOp_117 = (res_ImpliesLogicOp_117 && res_XorLogicOP_127);
    }
    res_AndLogicOP_116 = (res_AndLogicOP_116 && res_ImpliesLogicOp_117);
    bool res_NotLogicOP_183 = true;
    res_NotLogicOP_183 = (res_NotLogicOP_183 && ! (L_P1__GetSubcl28(my_id) == true));
    res_AndLogicOP_116 = (res_AndLogicOP_116 && res_NotLogicOP_183);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_116);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_1);
    
    if(res_AndLogicOP_2){
    L_P1__SetOutEvent7(my_id,LDS_MANCMD_PROCESSED);
    }
    else if(res_AndLogicOP_8){
    L_P1__SetOutEvent7(my_id,LDS_MANCMD_PROCESSED);
    }
    else if(res_AndLogicOP_39){
    L_P1__SetOutEvent7(my_id,LDS_MANCMD_PROCESSED);
    }
    else if(res_AndLogicOP_116){
    L_P1__SetOutEvent7(my_id,LDS_MANCMD_PROCESSED);
    }
    else{
    
    }
    
    
    return res_AndLogicOP_0;
}


// ********** Definizione macro **********

// Macro di verifica


// Macro valorizzate



//FEASIBILIT
int L_P1_C2_getFeasibility(instance_id_t const my_id, int cmd_id)
{
L_P1_C2_cmd_tmp_id = cmd_id;
int ret = 1;

switch (L_P1_C2_GetState(my_id)) {
	case C2_St_state1:
		switch (cmd_id){
			default:
			break;
		}
	break;
	case C2_St_state:
		switch (cmd_id){
			default:
			break;
		}
	break;
	case C2_St_state3:
		switch (cmd_id){
			case 39:
				if(L_P1__guard13(my_id)){
			    	ret = 0;
			    }
		        else { ret = 1; }
		    break;
			default:
			break;
		}
	break;
	case C2_St_state2:
		switch (cmd_id){
			default:
			break;
		}
	break;

    default:
        break;  // Needed for MISRA C syntactic compliance
    } // switch sugli stati chiuso
    
    return ret;
}

// comandi manuali
static bool L_P1__GetInEvent6(instance_id_t const my_id) 
{
    UNUSED(my_id);
    if(L_P1__event6_ID==L_P1_C2_cmd_tmp_id){
		return true;
	}	
	else{
		return false;
	}
}

// risposte ai comandi manuali
static void L_P1__SetOutEvent7(
	instance_id_t const my_id, 
	ManCmdResponse const value) 
{
    UNUSED(my_id);
    UNUSED(value);
}



