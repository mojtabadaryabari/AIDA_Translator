#ifndef FEA_LIBSTAZIONE_CLASSEL_P1_C1_PRIV_H
#define FEA_LIBSTAZIONE_CLASSEL_P1_C1_PRIV_H

#include "Logica/ClasseMainClass_C1.h"
#include "lds_param.h"


// ********** Comandi automatici **********


#define L_P1_C1_NUM_COMANDI_AUTO 0


// ********** Struct **********

typedef struct Classe_L_P1_C1 {

    // dati dinamici invisibili
    Timer mainc31;
    Timer mainc32;
    Counter mainc33;
    Counter mainc34;
    Counter mainc35;
    ExecResponse response;
} Classe_L_P1_C1;


// ********** Getter privati **********

// parametri
C1_Enumerat4 L_P1__GetParamMainc5(instance_id_t const my_id);


// record

// comandi automatici

// valori sicuri

#endif // LIBSTAZIONE_CLASSEL_P1_C1_PRIV_H