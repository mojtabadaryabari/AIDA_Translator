#ifndef LIBSTAZIONE_CLASSEL_P1_C3_PRIV_H
#define LIBSTAZIONE_CLASSEL_P1_C3_PRIV_H

#include "Logica/ClasseLDV_MainClass_C1.h"
#include "lds_param.h"


// ********** Comandi automatici **********

typedef struct {
    bool event13;
    bool argom32;
    bool argom33;
} L_P1_C3_Comandi_Auto;

#define L_P1_C3_NUM_COMANDI_AUTO 1


// ********** Struct **********

typedef struct Classe_L_P1_C3 {

    // dati dinamici invisibili
    Timer ldv_m6;
    Counter ldv_m7;
    Counter ldv_m8;
    Counter ldv_m9;
    Counter ldv_m10;
    L_P1_C3_Comandi_Auto comandi_automatici;
    ExecResponse response;
} Classe_L_P1_C3;


// ********** Getter/setter privati **********

// parametri
bool L_P1__GetParamConsd2(instance_id_t const my_id);
bool L_P1__GetParamLdv_m(instance_id_t const my_id);
Intero L_P1__GetParamLdv_m1(instance_id_t const my_id);
C3_Enumerat1 L_P1__GetParamLdv_m2(instance_id_t const my_id);


// record

// comandi automatici
/* bool L_P1__GetCAEvent13(instance_id_t const my_id); */
#define L_P1__GetCAEvent13(my_id) (ldv_Stazione_data->L_P1_C3[my_id].comandi_automatici.event13)

/* bool L_P1__GetCAArgom32(instance_id_t const my_id); */
#define L_P1__GetCAArgom32(my_id)  (ldv_Stazione_data->L_P1_C3[my_id].comandi_automatici.argom32)

/* bool L_P1__GetCAArgom33(instance_id_t const my_id); */
#define L_P1__GetCAArgom33(my_id)  (ldv_Stazione_data->L_P1_C3[my_id].comandi_automatici.argom33)

/* void L_P1__SetCAEvent13(instance_id_t const my_id, bool const value); */
#define L_P1__SetCAEvent13(my_id, value)   ldv_Stazione_data->L_P1_C3[my_id].comandi_automatici.event13 = (value)

/* void L_P1__SetCAArgom32(instance_id_t const my_id, bool const value); */
#define L_P1__SetCAArgom32(my_id, value)  ldv_Stazione_data->L_P1_C3[my_id].comandi_automatici.argom32 = (value)

/* void L_P1__SetCAArgom33(instance_id_t const my_id, bool const value); */
#define L_P1__SetCAArgom33(my_id, value)  ldv_Stazione_data->L_P1_C3[my_id].comandi_automatici.argom33 = (value)



// response
ExecResponse L_P1_C3_GetResponse(instance_id_t const my_id);
void L_P1_C3_SetResponse(instance_id_t const my_id, ExecResponse const value);


#endif // LIBSTAZIONE_CLASSEL_P1_C3_PRIV_H
