
#include "Logica/ClasseMainClass_C1_priv.h"
#include "Logica/ClasseSubClass_C2_priv.h"
#include "Logica/ClasseSubClass_C3_priv.h"
#include "config.h"
#include "PlatformMacros.h"

int L_P1_C1_cmd_tmp_id = -1; 

// ********** Dichiarazione guardie **********

static bool L_P1__guard1(instance_id_t const my_id);
static bool L_P1__guard3(instance_id_t const my_id);
static bool L_P1__guard4(instance_id_t const my_id);

// ********** Dichiarazione comandi manuali **********
static bool L_P1__GetInEvent(instance_id_t const my_id) ;

static void L_P1__SetOutEvent2(
	instance_id_t const my_id, 
	ManCmdResponse const value);



// ********** Definizione guardie **********

static bool L_P1__guard1(instance_id_t const my_id)
{
    bool res_AndLogicOP_0 = true;
    
    //  *93,*  Tutte le seguenti {
    //   Ricezione del comando manuale   MainClass_C1_command_comm7   *77,*
    //   *36,*  se il timer MainClass_C1_timer_T4 è attivo e  se il controllo ConsDef  è  uguale a FALSE  *35,* e  se il controllo MainClass_C1_controllo_C7 non è  diverso da GialloxVerdex *37,* o  se la variabile MainClass_C1_variabile_V6 è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   *49,*  *,*  il timer MainClass_C1_timer_T4 sia disattivo
    //  }
    bool res_AndLogicOP_1 = true;
    res_AndLogicOP_1 = (res_AndLogicOP_1 && L_P1__GetInEvent(my_id));
    bool res_ImpliesLogicOp_2 = true;
    bool res_OrLogicOP_3 = false;
    bool res_OrLogicOP_4 = false;
    bool res_AndLogicOP_5 = true;
    bool res_AndLogicOP_6 = true;
    res_AndLogicOP_6 = (res_AndLogicOP_6 && Timer_Attivo(L_P1__GetMainc31(my_id)));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && (L_P1__GetInConsd(my_id) == false));
    
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_AndLogicOP_6);
    bool res_NotLogicOP_7 = true;
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetInMainc2(my_id) == gialloxverd));
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! res_NotLogicOP_8);
    res_AndLogicOP_5 = (res_AndLogicOP_5 && res_NotLogicOP_7);
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_AndLogicOP_5);
    res_OrLogicOP_4 = (res_OrLogicOP_4 || (L_P1__GetMainc22(my_id) == false));
    
    res_OrLogicOP_3 = (res_OrLogicOP_3 || res_OrLogicOP_4);
    res_OrLogicOP_3 = (res_OrLogicOP_3 || (L_P1__GetInConsd(my_id) == false));
    
    if(res_OrLogicOP_3){
    res_ImpliesLogicOp_2 = (res_ImpliesLogicOp_2 && Timer_Disattivo(L_P1__GetMainc31(my_id)));
    }
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_ImpliesLogicOp_2);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_AndLogicOP_1);
    
    if(res_AndLogicOP_1){
    L_P1__SetOutEvent2(my_id,LDS_MANCMD_PROCESSED);
    }
    else{
    
    }
    
    
    return res_AndLogicOP_0;
}

static bool L_P1__guard3(instance_id_t const my_id)
{
    bool res_AndLogicOP_0 = true;
    
    //  *86,*  Almeno una delle seguenti {
    //   *82,*  Ricezione del comando manuale   MainClass_C1_command_comm7   *77,*
    //   *83,*  Tutte le seguenti {
    //   Ricezione del  comando manuale   MainClass_C1_command_comm7   *77,*
    //   *38,*  se il contatore MainClass_C1_contatore_Co5 non è  maggiore di  *54,* 13 *37,* o  se la variabile MainClass_C1_variabile_V2 non è  uguale a AC *34,* o  se il parametro MainClass_C1_parametro_P3 non è  uguale a c270x, Verifica che   *48,*   il controllo ConsDef  sia  uguale a FALSE 
    //  } *82,*  Ricezione del comando manuale   MainClass_C1_command_comm7   *77,*
    //   *83,*  Tutte le seguenti {
    //   Ricezione del  comando manuale   MainClass_C1_command_comm7   *77,*
    //   *69,* *37,*  se la variabile MainClass_C1_variabile_V7 non è  uguale a avviox *37,* e  se la variabile MainClass_C1_variabile_V7 non è  uguale a avviox *37,* o  se la variabile MainClass_C1_variabile_V6 è  uguale a  True  *36,* o  se il timer MainClass_C1_timer_T6 è attivo *34,* e  se il parametro MainClass_C1_parametro_P3 non è  uguale a c270x *37,* e  se la variabile MainClass_C1_variabile_V6 è  diverso da  True , Solo una delle seguenti { 
    //   *68,* *35,*  se il controllo MainClass_C1_controllo_C9 non è  uguale a GialloxVerdex, Almeno una delle seguenti { 
    //   *67,*  se il controllo ConsDef  è  uguale a FALSE  *34,* o  se il parametro MainClass_C1_parametro_P3 non è  diverso da c270x, Tutte le seguenti { 
    //   *38,*  se il contatore MainClass_C1_contatore_Co1 è  maggiore di  *54,* 1415, Verifica che   *50,*  *,*  la variabile MainClass_C1_variabile_V6 non sia  uguale a  False 
    //   } Verifica che   *48,*  *,*  il controllo MainClass_C1_controllo_C7 sia  uguale a GialloxVerdex
    //   } Verifica che   *48,*  *,*  il controllo MainClass_C1_controllo_C7 sia  uguale a GialloxVerdex
    //   } Verifica che   *50,*  *,*  la variabile MainClass_C1_variabile_V6 non sia  uguale a  True 
    //  }
    //  }
    bool res_OrLogicOP_1 = false;
    res_OrLogicOP_1 = (res_OrLogicOP_1 || L_P1__GetInEvent(my_id));
    bool res_AndLogicOP_2 = true;
    res_AndLogicOP_2 = (res_AndLogicOP_2 && L_P1__GetInEvent(my_id));
    bool res_ImpliesLogicOp_3 = true;
    bool res_OrLogicOP_4 = false;
    bool res_OrLogicOP_5 = false;
    bool res_NotLogicOP_6 = true;
    res_NotLogicOP_6 = (res_NotLogicOP_6 && ! (Counter_GetValore(L_P1__GetMainc35(my_id)) > 13u));
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_NotLogicOP_6);
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! (L_P1__GetMainc20(my_id) == ac));
    res_OrLogicOP_5 = (res_OrLogicOP_5 || res_NotLogicOP_7);
    
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_OrLogicOP_5);
    bool res_NotLogicOP_8 = true;
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! (L_P1__GetParamMainc5(my_id) == c270x));
    res_OrLogicOP_4 = (res_OrLogicOP_4 || res_NotLogicOP_8);
    
    if(res_OrLogicOP_4){
    res_ImpliesLogicOp_3 = (res_ImpliesLogicOp_3 && (L_P1__GetInConsd(my_id) == false));
    }
    res_AndLogicOP_2 = (res_AndLogicOP_2 && res_ImpliesLogicOp_3);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_2);
    res_OrLogicOP_1 = (res_OrLogicOP_1 || L_P1__GetInEvent(my_id));
    bool res_AndLogicOP_9 = true;
    res_AndLogicOP_9 = (res_AndLogicOP_9 && L_P1__GetInEvent(my_id));
    bool res_ImpliesLogicOp_10 = true;
    bool res_OrLogicOP_11 = false;
    bool res_OrLogicOP_12 = false;
    bool res_AndLogicOP_13 = true;
    bool res_NotLogicOP_14 = true;
    res_NotLogicOP_14 = (res_NotLogicOP_14 && ! (L_P1__GetMainc23(my_id) == avviox));
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_NotLogicOP_14);
    bool res_NotLogicOP_15 = true;
    res_NotLogicOP_15 = (res_NotLogicOP_15 && ! (L_P1__GetMainc23(my_id) == avviox));
    res_AndLogicOP_13 = (res_AndLogicOP_13 && res_NotLogicOP_15);
    
    res_OrLogicOP_12 = (res_OrLogicOP_12 || res_AndLogicOP_13);
    res_OrLogicOP_12 = (res_OrLogicOP_12 || (L_P1__GetMainc22(my_id) == true));
    
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_OrLogicOP_12);
    bool res_AndLogicOP_16 = true;
    bool res_AndLogicOP_17 = true;
    res_AndLogicOP_17 = (res_AndLogicOP_17 && Timer_Attivo(L_P1__GetMainc32(my_id)));
    bool res_NotLogicOP_18 = true;
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! (L_P1__GetParamMainc5(my_id) == c270x));
    res_AndLogicOP_17 = (res_AndLogicOP_17 && res_NotLogicOP_18);
    
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_AndLogicOP_17);
    bool res_NotLogicOP_19 = true;
    res_NotLogicOP_19 = (res_NotLogicOP_19 && ! (L_P1__GetMainc22(my_id) == true));
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_NotLogicOP_19);
    
    res_OrLogicOP_11 = (res_OrLogicOP_11 || res_AndLogicOP_16);
    
    if(res_OrLogicOP_11){
    bool res_XorLogicOP_20 = true;
    int xorIndex_res_XorLogicOP_20 = 0;
    bool res_ImpliesLogicOp_21 = true;
    bool res_NotLogicOP_22 = true;
    res_NotLogicOP_22 = (res_NotLogicOP_22 && ! (L_P1__GetInMainc4(my_id) == gialloxverd));
    if(res_NotLogicOP_22){
    bool res_OrLogicOP_23 = false;
    bool res_ImpliesLogicOp_24 = true;
    bool res_OrLogicOP_25 = false;
    res_OrLogicOP_25 = (res_OrLogicOP_25 || (L_P1__GetInConsd(my_id) == false));
    bool res_NotLogicOP_26 = true;
    bool res_NotLogicOP_27 = true;
    res_NotLogicOP_27 = (res_NotLogicOP_27 && ! (L_P1__GetParamMainc5(my_id) == c270x));
    res_NotLogicOP_26 = (res_NotLogicOP_26 && ! res_NotLogicOP_27);
    res_OrLogicOP_25 = (res_OrLogicOP_25 || res_NotLogicOP_26);
    
    if(res_OrLogicOP_25){
    bool res_ImpliesLogicOp_28 = true;
    if((Counter_GetValore(L_P1__GetMainc33(my_id)) > 1415u)){
    bool res_NotLogicOP_29 = true;
    res_NotLogicOP_29 = (res_NotLogicOP_29 && ! (L_P1__GetMainc22(my_id) == false));
    res_ImpliesLogicOp_28 = (res_ImpliesLogicOp_28 && res_NotLogicOP_29);
    }
    res_ImpliesLogicOp_24 = (res_ImpliesLogicOp_24 && res_ImpliesLogicOp_28);
    }
    res_OrLogicOP_23 = (res_OrLogicOP_23 || res_ImpliesLogicOp_24);
    res_OrLogicOP_23 = (res_OrLogicOP_23 || (L_P1__GetInMainc2(my_id) == gialloxverd));
    
    res_ImpliesLogicOp_21 = (res_ImpliesLogicOp_21 && res_OrLogicOP_23);
    }
    if(res_ImpliesLogicOp_21){
    xorIndex_res_XorLogicOP_20 = (xorIndex_res_XorLogicOP_20 + 1);
    }
    if((L_P1__GetInMainc2(my_id) == gialloxverd)){
    xorIndex_res_XorLogicOP_20 = (xorIndex_res_XorLogicOP_20 + 1);
    }
    
    res_XorLogicOP_20 = (res_XorLogicOP_20 && (xorIndex_res_XorLogicOP_20 == 1));
    res_ImpliesLogicOp_10 = (res_ImpliesLogicOp_10 && res_XorLogicOP_20);
    }
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_ImpliesLogicOp_10);
    bool res_NotLogicOP_30 = true;
    res_NotLogicOP_30 = (res_NotLogicOP_30 && ! (L_P1__GetMainc22(my_id) == true));
    res_AndLogicOP_9 = (res_AndLogicOP_9 && res_NotLogicOP_30);
    
    res_OrLogicOP_1 = (res_OrLogicOP_1 || res_AndLogicOP_9);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_OrLogicOP_1);
    
    if(res_OrLogicOP_1){
    L_P1__SetOutEvent2(my_id,LDS_MANCMD_PROCESSED);
    }
    else{
    
    }
    
    
    return res_AndLogicOP_0;
}

static bool L_P1__guard4(instance_id_t const my_id)
{
    bool res_AndLogicOP_0 = true;
    
    //  *93,*  Tutte le seguenti {
    //   Ricezione del comando manuale   MainClass_C1_command_comm7   *77,*
    //   *69,* *35,*  se il controllo MainClass_C1_controllo_C7 non è  uguale a GialloxVerdex, Solo una delle seguenti { 
    //   *69,* *36,*  se il timer MainClass_C1_timer_T6 non è attivo *34,* e  se il parametro MainClass_C1_parametro_P3 non è  diverso da c270x, Solo una delle seguenti { 
    //   *69,* *34,*  se il parametro MainClass_C1_parametro_P3 non è  uguale a c270x, Solo una delle seguenti { 
    //   *67,* *38,*  se il contatore MainClass_C1_contatore_Co1 non è  uguale a  *53,* 12150 *38,* e  se il contatore MainClass_C1_contatore_Co1 non è  minore di  *55,* 154 *38,* o  se il contatore MainClass_C1_contatore_Co2 è  uguale a  *53,* 11 *36,* e  se il timer MainClass_C1_timer_T6 non è disattivo, Tutte le seguenti { 
    //   *69,*  se il controllo ConsDef  è  uguale a FALSE  *34,* e  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x *37,* e  se la variabile MainClass_C1_variabile_V6 non è  uguale a  True , Solo una delle seguenti { 
    //   *68,* *38,*  se il contatore MainClass_C1_contatore_Co1 non è  minore di  *55,* 123 e  se il controllo ConsDef  è  uguale a FALSE  *34,* e  se il parametro MainClass_C1_parametro_P3 non è  diverso da c270x, Almeno una delle seguenti { 
    //   *68,* *37,*  se la variabile MainClass_C1_variabile_V6 è  uguale a  True  *38,* o  se il contatore MainClass_C1_contatore_Co1 non è  minore di  *55,* 11 *35,* e  se il controllo MainClass_C1_controllo_C5 è  uguale a c270x e  se il controllo ConsDef  è  uguale a FALSE  *35,* e  se il controllo MainClass_C1_controllo_C7 è  diverso da GialloxVerdex, Almeno una delle seguenti { 
    //   *67,* *37,*  se la variabile MainClass_C1_variabile_V2 è  uguale a AC *34,* e  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x *34,* o  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x *36,* e  se il timer MainClass_C1_timer_T4 è disattivo, Tutte le seguenti { 
    //    se il controllo ConsDef  è  uguale a FALSE  *34,* e  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x *38,* e  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  *56,* 13215, Verifica che   *48,*   il controllo ConsDef  sia  uguale a FALSE 
    //   } Verifica che   *48,*  *,*  il controllo MainClass_C1_controllo_C8 sia  diverso da c270x
    //   } Verifica che   *48,*   il controllo ConsDef  sia  uguale a FALSE 
    //   } Verifica che   *48,*   il controllo ConsDef  sia  uguale a FALSE 
    //   } Verifica che   *48,*  *,*  il controllo MainClass_C1_controllo_C7 sia  uguale a GialloxVerdex
    //   } Verifica che   *50,*  *,*  la variabile MainClass_C1_variabile_V6 sia  diverso da  False 
    //   } Verifica che   *47,*  *34,*  il parametro MainClass_C1_parametro_P3 sia  uguale a c270x
    //   } Verifica che   *47,*  *34,*  il parametro MainClass_C1_parametro_P3 sia  uguale a c270x
    //   } Verifica che   *51,*  *,*  il contatore MainClass_C1_contatore_Co2 non sia  diverso da  *56,* 120
    //  }
    bool res_AndLogicOP_1 = true;
    res_AndLogicOP_1 = (res_AndLogicOP_1 && L_P1__GetInEvent(my_id));
    bool res_ImpliesLogicOp_2 = true;
    bool res_NotLogicOP_3 = true;
    res_NotLogicOP_3 = (res_NotLogicOP_3 && ! (L_P1__GetInMainc2(my_id) == gialloxverd));
    if(res_NotLogicOP_3){
    bool res_XorLogicOP_4 = true;
    int xorIndex_res_XorLogicOP_4 = 0;
    bool res_ImpliesLogicOp_5 = true;
    bool res_AndLogicOP_6 = true;
    bool res_NotLogicOP_7 = true;
    res_NotLogicOP_7 = (res_NotLogicOP_7 && ! Timer_Attivo(L_P1__GetMainc32(my_id)));
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_7);
    bool res_NotLogicOP_8 = true;
    bool res_NotLogicOP_9 = true;
    res_NotLogicOP_9 = (res_NotLogicOP_9 && ! (L_P1__GetParamMainc5(my_id) == c270x));
    res_NotLogicOP_8 = (res_NotLogicOP_8 && ! res_NotLogicOP_9);
    res_AndLogicOP_6 = (res_AndLogicOP_6 && res_NotLogicOP_8);
    
    if(res_AndLogicOP_6){
    bool res_XorLogicOP_10 = true;
    int xorIndex_res_XorLogicOP_10 = 0;
    bool res_ImpliesLogicOp_11 = true;
    bool res_NotLogicOP_12 = true;
    res_NotLogicOP_12 = (res_NotLogicOP_12 && ! (L_P1__GetParamMainc5(my_id) == c270x));
    if(res_NotLogicOP_12){
    bool res_XorLogicOP_13 = true;
    int xorIndex_res_XorLogicOP_13 = 0;
    bool res_ImpliesLogicOp_14 = true;
    bool res_OrLogicOP_15 = false;
    bool res_AndLogicOP_16 = true;
    bool res_NotLogicOP_17 = true;
    res_NotLogicOP_17 = (res_NotLogicOP_17 && ! (Counter_GetValore(L_P1__GetMainc33(my_id)) == 12150u));
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_NotLogicOP_17);
    bool res_NotLogicOP_18 = true;
    res_NotLogicOP_18 = (res_NotLogicOP_18 && ! (Counter_GetValore(L_P1__GetMainc33(my_id)) < 154u));
    res_AndLogicOP_16 = (res_AndLogicOP_16 && res_NotLogicOP_18);
    
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_AndLogicOP_16);
    bool res_AndLogicOP_19 = true;
    res_AndLogicOP_19 = (res_AndLogicOP_19 && (Counter_GetValore(L_P1__GetMainc34(my_id)) == 11u));
    bool res_NotLogicOP_20 = true;
    res_NotLogicOP_20 = (res_NotLogicOP_20 && ! Timer_Disattivo(L_P1__GetMainc32(my_id)));
    res_AndLogicOP_19 = (res_AndLogicOP_19 && res_NotLogicOP_20);
    
    res_OrLogicOP_15 = (res_OrLogicOP_15 || res_AndLogicOP_19);
    
    if(res_OrLogicOP_15){
    bool res_AndLogicOP_21 = true;
    bool res_ImpliesLogicOp_22 = true;
    bool res_AndLogicOP_23 = true;
    bool res_AndLogicOP_24 = true;
    res_AndLogicOP_24 = (res_AndLogicOP_24 && (L_P1__GetInConsd(my_id) == false));
    res_AndLogicOP_24 = (res_AndLogicOP_24 && (L_P1__GetParamMainc5(my_id) == c270x));
    
    res_AndLogicOP_23 = (res_AndLogicOP_23 && res_AndLogicOP_24);
    bool res_NotLogicOP_25 = true;
    res_NotLogicOP_25 = (res_NotLogicOP_25 && ! (L_P1__GetMainc22(my_id) == true));
    res_AndLogicOP_23 = (res_AndLogicOP_23 && res_NotLogicOP_25);
    
    if(res_AndLogicOP_23){
    bool res_XorLogicOP_26 = true;
    int xorIndex_res_XorLogicOP_26 = 0;
    bool res_ImpliesLogicOp_27 = true;
    bool res_AndLogicOP_28 = true;
    bool res_AndLogicOP_29 = true;
    bool res_NotLogicOP_30 = true;
    res_NotLogicOP_30 = (res_NotLogicOP_30 && ! (Counter_GetValore(L_P1__GetMainc33(my_id)) < 123u));
    res_AndLogicOP_29 = (res_AndLogicOP_29 && res_NotLogicOP_30);
    res_AndLogicOP_29 = (res_AndLogicOP_29 && (L_P1__GetInConsd(my_id) == false));
    
    res_AndLogicOP_28 = (res_AndLogicOP_28 && res_AndLogicOP_29);
    bool res_NotLogicOP_31 = true;
    bool res_NotLogicOP_32 = true;
    res_NotLogicOP_32 = (res_NotLogicOP_32 && ! (L_P1__GetParamMainc5(my_id) == c270x));
    res_NotLogicOP_31 = (res_NotLogicOP_31 && ! res_NotLogicOP_32);
    res_AndLogicOP_28 = (res_AndLogicOP_28 && res_NotLogicOP_31);
    
    if(res_AndLogicOP_28){
    bool res_OrLogicOP_33 = false;
    bool res_ImpliesLogicOp_34 = true;
    bool res_OrLogicOP_35 = false;
    res_OrLogicOP_35 = (res_OrLogicOP_35 || (L_P1__GetMainc22(my_id) == true));
    bool res_AndLogicOP_36 = true;
    bool res_AndLogicOP_37 = true;
    bool res_AndLogicOP_38 = true;
    bool res_NotLogicOP_39 = true;
    res_NotLogicOP_39 = (res_NotLogicOP_39 && ! (Counter_GetValore(L_P1__GetMainc33(my_id)) < 11u));
    res_AndLogicOP_38 = (res_AndLogicOP_38 && res_NotLogicOP_39);
    res_AndLogicOP_38 = (res_AndLogicOP_38 && (L_P1__GetInMainc1(my_id) == c270x));
    
    res_AndLogicOP_37 = (res_AndLogicOP_37 && res_AndLogicOP_38);
    res_AndLogicOP_37 = (res_AndLogicOP_37 && (L_P1__GetInConsd(my_id) == false));
    
    res_AndLogicOP_36 = (res_AndLogicOP_36 && res_AndLogicOP_37);
    bool res_NotLogicOP_40 = true;
    res_NotLogicOP_40 = (res_NotLogicOP_40 && ! (L_P1__GetInMainc2(my_id) == gialloxverd));
    res_AndLogicOP_36 = (res_AndLogicOP_36 && res_NotLogicOP_40);
    
    res_OrLogicOP_35 = (res_OrLogicOP_35 || res_AndLogicOP_36);
    
    if(res_OrLogicOP_35){
    bool res_OrLogicOP_41 = false;
    bool res_ImpliesLogicOp_42 = true;
    bool res_OrLogicOP_43 = false;
    bool res_AndLogicOP_44 = true;
    res_AndLogicOP_44 = (res_AndLogicOP_44 && (L_P1__GetMainc20(my_id) == ac));
    bool res_NotLogicOP_45 = true;
    res_NotLogicOP_45 = (res_NotLogicOP_45 && ! (L_P1__GetParamMainc5(my_id) == c270x));
    res_AndLogicOP_44 = (res_AndLogicOP_44 && res_NotLogicOP_45);
    
    res_OrLogicOP_43 = (res_OrLogicOP_43 || res_AndLogicOP_44);
    bool res_AndLogicOP_46 = true;
    bool res_NotLogicOP_47 = true;
    res_NotLogicOP_47 = (res_NotLogicOP_47 && ! (L_P1__GetParamMainc5(my_id) == c270x));
    res_AndLogicOP_46 = (res_AndLogicOP_46 && res_NotLogicOP_47);
    res_AndLogicOP_46 = (res_AndLogicOP_46 && Timer_Disattivo(L_P1__GetMainc31(my_id)));
    
    res_OrLogicOP_43 = (res_OrLogicOP_43 || res_AndLogicOP_46);
    
    if(res_OrLogicOP_43){
    bool res_ImpliesLogicOp_48 = true;
    bool res_AndLogicOP_49 = true;
    bool res_AndLogicOP_50 = true;
    res_AndLogicOP_50 = (res_AndLogicOP_50 && (L_P1__GetInConsd(my_id) == false));
    res_AndLogicOP_50 = (res_AndLogicOP_50 && (L_P1__GetParamMainc5(my_id) == c270x));
    
    res_AndLogicOP_49 = (res_AndLogicOP_49 && res_AndLogicOP_50);
    bool res_NotLogicOP_51 = true;
    bool res_NotLogicOP_52 = true;
    res_NotLogicOP_52 = (res_NotLogicOP_52 && ! (Counter_GetValore(L_P1__GetMainc34(my_id)) == 13215u));
    res_NotLogicOP_51 = (res_NotLogicOP_51 && ! res_NotLogicOP_52);
    res_AndLogicOP_49 = (res_AndLogicOP_49 && res_NotLogicOP_51);
    
    if(res_AndLogicOP_49){
    res_ImpliesLogicOp_48 = (res_ImpliesLogicOp_48 && (L_P1__GetInConsd(my_id) == false));
    }
    res_ImpliesLogicOp_42 = (res_ImpliesLogicOp_42 && res_ImpliesLogicOp_48);
    }
    res_OrLogicOP_41 = (res_OrLogicOP_41 || res_ImpliesLogicOp_42);
    bool res_NotLogicOP_53 = true;
    res_NotLogicOP_53 = (res_NotLogicOP_53 && ! (L_P1__GetInMainc3(my_id) == c270x));
    res_OrLogicOP_41 = (res_OrLogicOP_41 || res_NotLogicOP_53);
    
    res_ImpliesLogicOp_34 = (res_ImpliesLogicOp_34 && res_OrLogicOP_41);
    }
    res_OrLogicOP_33 = (res_OrLogicOP_33 || res_ImpliesLogicOp_34);
    res_OrLogicOP_33 = (res_OrLogicOP_33 || (L_P1__GetInConsd(my_id) == false));
    
    res_ImpliesLogicOp_27 = (res_ImpliesLogicOp_27 && res_OrLogicOP_33);
    }
    if(res_ImpliesLogicOp_27){
    xorIndex_res_XorLogicOP_26 = (xorIndex_res_XorLogicOP_26 + 1);
    }
    if((L_P1__GetInConsd(my_id) == false)){
    xorIndex_res_XorLogicOP_26 = (xorIndex_res_XorLogicOP_26 + 1);
    }
    
    res_XorLogicOP_26 = (res_XorLogicOP_26 && (xorIndex_res_XorLogicOP_26 == 1));
    res_ImpliesLogicOp_22 = (res_ImpliesLogicOp_22 && res_XorLogicOP_26);
    }
    res_AndLogicOP_21 = (res_AndLogicOP_21 && res_ImpliesLogicOp_22);
    res_AndLogicOP_21 = (res_AndLogicOP_21 && (L_P1__GetInMainc2(my_id) == gialloxverd));
    
    res_ImpliesLogicOp_14 = (res_ImpliesLogicOp_14 && res_AndLogicOP_21);
    }
    if(res_ImpliesLogicOp_14){
    xorIndex_res_XorLogicOP_13 = (xorIndex_res_XorLogicOP_13 + 1);
    }
    bool res_NotLogicOP_54 = true;
    res_NotLogicOP_54 = (res_NotLogicOP_54 && ! (L_P1__GetMainc22(my_id) == false));
    if(res_NotLogicOP_54){
    xorIndex_res_XorLogicOP_13 = (xorIndex_res_XorLogicOP_13 + 1);
    }
    
    res_XorLogicOP_13 = (res_XorLogicOP_13 && (xorIndex_res_XorLogicOP_13 == 1));
    res_ImpliesLogicOp_11 = (res_ImpliesLogicOp_11 && res_XorLogicOP_13);
    }
    if(res_ImpliesLogicOp_11){
    xorIndex_res_XorLogicOP_10 = (xorIndex_res_XorLogicOP_10 + 1);
    }
    if((L_P1__GetParamMainc5(my_id) == c270x)){
    xorIndex_res_XorLogicOP_10 = (xorIndex_res_XorLogicOP_10 + 1);
    }
    
    res_XorLogicOP_10 = (res_XorLogicOP_10 && (xorIndex_res_XorLogicOP_10 == 1));
    res_ImpliesLogicOp_5 = (res_ImpliesLogicOp_5 && res_XorLogicOP_10);
    }
    if(res_ImpliesLogicOp_5){
    xorIndex_res_XorLogicOP_4 = (xorIndex_res_XorLogicOP_4 + 1);
    }
    if((L_P1__GetParamMainc5(my_id) == c270x)){
    xorIndex_res_XorLogicOP_4 = (xorIndex_res_XorLogicOP_4 + 1);
    }
    
    res_XorLogicOP_4 = (res_XorLogicOP_4 && (xorIndex_res_XorLogicOP_4 == 1));
    res_ImpliesLogicOp_2 = (res_ImpliesLogicOp_2 && res_XorLogicOP_4);
    }
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_ImpliesLogicOp_2);
    bool res_NotLogicOP_55 = true;
    bool res_NotLogicOP_56 = true;
    res_NotLogicOP_56 = (res_NotLogicOP_56 && ! (Counter_GetValore(L_P1__GetMainc34(my_id)) == 120u));
    res_NotLogicOP_55 = (res_NotLogicOP_55 && ! res_NotLogicOP_56);
    res_AndLogicOP_1 = (res_AndLogicOP_1 && res_NotLogicOP_55);
    
    res_AndLogicOP_0 = (res_AndLogicOP_0 && res_AndLogicOP_1);
    
    if(res_AndLogicOP_1){
    L_P1__SetOutEvent2(my_id,LDS_MANCMD_PROCESSED);
    }
    else{
    
    }
    
    
    return res_AndLogicOP_0;
}


// ********** Definizione macro **********

// Macro di verifica


// Macro valorizzate



//FEASIBILIT
int L_P1_C1_getFeasibility(instance_id_t const my_id, int cmd_id)
{
L_P1_C1_cmd_tmp_id = cmd_id;
int ret = 1;

switch (L_P1_C1_GetState(my_id)) {
	case C1_St_state1:
		switch (cmd_id){
			default:
			break;
		}
	break;
	case C1_St_state:
		switch (cmd_id){
			case 39:
				if(L_P1__guard3(my_id)){
			    	ret = 0;
			    }

				else if(L_P1__guard4(my_id)){
			    	ret = 0;
			    }

				else if(L_P1__guard1(my_id)){
			    	ret = 0;
			    }
		        else { ret = 1; }
		    break;
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
static bool L_P1__GetInEvent(instance_id_t const my_id) 
{
    UNUSED(my_id);
    if(L_P1__event_ID==L_P1_C1_cmd_tmp_id){
		return true;
	}	
	else{
		return false;
	}
}

// risposte ai comandi manuali
static void L_P1__SetOutEvent2(
	instance_id_t const my_id, 
	ManCmdResponse const value) 
{
    UNUSED(my_id);
    UNUSED(value);
}



