#ifndef FEA_LIBSTAZIONE_CLASSEL_P1_C3_PRIV_H
#define FEA_LIBSTAZIONE_CLASSEL_P1_C3_PRIV_H

#include "Logica/ClasseSubClass_C3.h"
#include "lds_param.h"


// ********** Comandi automatici **********


#define L_P1_C3_NUM_COMANDI_AUTO 0


// ********** Struct **********

typedef struct Classe_L_P1_C3 {

    // dati dinamici invisibili
    ExecResponse response;
} Classe_L_P1_C3;


// ********** Getter privati **********

// parametri
bool L_P1__GetParamSubcl51(instance_id_t const my_id);
C3_Enumerat3 L_P1__GetParamSubcl52(instance_id_t const my_id);
Intero L_P1__GetParamSubcl53(instance_id_t const my_id);
Intero L_P1__GetParamSubcl54(instance_id_t const my_id);
Intero L_P1__GetParamSubcl55(instance_id_t const my_id);


// record

// comandi automatici

// valori sicuri

#endif // LIBSTAZIONE_CLASSEL_P1_C3_PRIV_H
