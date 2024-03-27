#ifndef FEA_LIBSTAZIONE_CLASSEL_P1_C4_PRIV_H
#define FEA_LIBSTAZIONE_CLASSEL_P1_C4_PRIV_H

#include "Logica/ClasseSubClass_C4.h"
#include "lds_param.h"


// ********** Comandi automatici **********


#define L_P1_C4_NUM_COMANDI_AUTO 0


// ********** Struct **********

typedef struct Classe_L_P1_C4 {

    // dati dinamici invisibili
    ExecResponse response;
} Classe_L_P1_C4;


// ********** Getter privati **********

// parametri
bool L_P1__GetParamSubcl96(instance_id_t const my_id);
bool L_P1__GetParamSubcl97(instance_id_t const my_id);
Intero L_P1__GetParamSubcl98(instance_id_t const my_id);


// record

// comandi automatici

// valori sicuri

#endif // LIBSTAZIONE_CLASSEL_P1_C4_PRIV_H
