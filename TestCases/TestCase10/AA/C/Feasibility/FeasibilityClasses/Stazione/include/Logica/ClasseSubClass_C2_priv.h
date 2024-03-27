#ifndef FEA_LIBSTAZIONE_CLASSEL_P1_C2_PRIV_H
#define FEA_LIBSTAZIONE_CLASSEL_P1_C2_PRIV_H

#include "Logica/ClasseSubClass_C2.h"
#include "lds_param.h"


// ********** Comandi automatici **********


#define L_P1_C2_NUM_COMANDI_AUTO 0


// ********** Struct **********

typedef struct Classe_L_P1_C2 {

    // dati dinamici invisibili
    Timer subcl31;
    Timer subcl32;
    Timer subcl33;
    Timer subcl34;
    Timer subcl35;
    Counter subcl36;
    ExecResponse response;
} Classe_L_P1_C2;


// ********** Getter privati **********

// parametri
Intero L_P1__GetParamSubcl8(instance_id_t const my_id);


// record

// comandi automatici

// valori sicuri

#endif // LIBSTAZIONE_CLASSEL_P1_C2_PRIV_H
