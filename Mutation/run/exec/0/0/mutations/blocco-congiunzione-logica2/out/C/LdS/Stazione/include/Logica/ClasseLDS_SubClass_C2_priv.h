#ifndef LIBSTAZIONE_CLASSEL_P1_C2_PRIV_H
#define LIBSTAZIONE_CLASSEL_P1_C2_PRIV_H

#include "Logica/ClasseLDS_SubClass_C2.h"
#include "lds_param.h"


// ********** Comandi automatici **********


#define L_P1_C2_NUM_COMANDI_AUTO 0


// ********** Struct **********

typedef struct Classe_L_P1_C2 {

    // dati dinamici invisibili
    Timer lds_s17;
    Counter lds_s18;
    Counter lds_s19;
    Counter lds_s20;
    Counter lds_s21;
    Counter lds_s22;
    ExecResponse response;
} Classe_L_P1_C2;


// ********** Getter/setter privati **********

// parametri
bool L_P1__GetParamConsd1(instance_id_t const my_id);
C2_Enumerat2 L_P1__GetParamLds_s11(instance_id_t const my_id);

offset_t L_P1__GetParamLds_s8Start(instance_id_t const my_id);
index_t L_P1__GetParamLds_s8Length(instance_id_t const my_id);
offset_t L_P1__GetParamLds_s9Start(instance_id_t const my_id);
index_t L_P1__GetParamLds_s9Length(instance_id_t const my_id);
offset_t L_P1__GetParamLds_s10Start(instance_id_t const my_id);
index_t L_P1__GetParamLds_s10Length(instance_id_t const my_id);

// record
const L_P1__Recor* L_P1__GetRecLds_s8(instance_id_t const my_id, index_t const elem_idx);

const L_P1__Recor1* L_P1__GetRecLds_s9(instance_id_t const my_id, index_t const elem_idx);

const L_P1__Recor1* L_P1__GetRecLds_s10(instance_id_t const my_id, index_t const elem_idx);


// comandi automatici


// response
ExecResponse L_P1_C2_GetResponse(instance_id_t const my_id);
void L_P1_C2_SetResponse(instance_id_t const my_id, ExecResponse const value);


#endif // LIBSTAZIONE_CLASSEL_P1_C2_PRIV_H
