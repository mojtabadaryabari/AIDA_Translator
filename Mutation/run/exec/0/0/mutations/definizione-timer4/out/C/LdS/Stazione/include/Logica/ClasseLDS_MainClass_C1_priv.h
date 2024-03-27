#ifndef LIBSTAZIONE_CLASSEL_P1_C1_PRIV_H
#define LIBSTAZIONE_CLASSEL_P1_C1_PRIV_H

#include "Logica/ClasseLDS_MainClass_C1.h"
#include "lds_param.h"


// ********** Comandi automatici **********

typedef struct {
    bool event2;
} L_P1_C1_Comandi_Auto;

#define L_P1_C1_NUM_COMANDI_AUTO 1


// ********** Struct **********

typedef struct Classe_L_P1_C1 {

    // dati dinamici invisibili
    Timer lds_m12;
    Timer lds_m13;
    Timer lds_m14;
    Timer lds_m15;
    Timer nabcc;
    Counter lds_m16;
    Counter lds_m17;
    Counter lds_m18;
    Counter lds_m19;
    L_P1_C1_Comandi_Auto comandi_automatici;
    ExecResponse response;
} Classe_L_P1_C1;


// ********** Getter/setter privati **********

// parametri
bool L_P1__GetParamConsd(instance_id_t const my_id);
Intero L_P1__GetParamLds_m7(instance_id_t const my_id);
bool L_P1__GetParamLds_m8(instance_id_t const my_id);
bool L_P1__GetParamLds_m9(instance_id_t const my_id);


// record

// comandi automatici
/* bool L_P1__GetCAEvent2(instance_id_t const my_id); */
#define L_P1__GetCAEvent2(my_id) (lds_Stazione_data->L_P1_C1[my_id].comandi_automatici.event2)

/* void L_P1__SetCAEvent2(instance_id_t const my_id, bool const value); */
#define L_P1__SetCAEvent2(my_id, value)   lds_Stazione_data->L_P1_C1[my_id].comandi_automatici.event2 = (value)



// response
ExecResponse L_P1_C1_GetResponse(instance_id_t const my_id);
void L_P1_C1_SetResponse(instance_id_t const my_id, ExecResponse const value);


#endif // LIBSTAZIONE_CLASSEL_P1_C1_PRIV_H
