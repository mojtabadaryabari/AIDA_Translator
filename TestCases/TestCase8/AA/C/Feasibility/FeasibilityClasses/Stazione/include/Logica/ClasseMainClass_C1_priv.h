#ifndef FEA_LIBSTAZIONE_CLASSEL_P1_C1_PRIV_H
#define FEA_LIBSTAZIONE_CLASSEL_P1_C1_PRIV_H

#include "Logica/ClasseMainClass_C1.h"
#include "lds_param.h"


// ********** Comandi automatici **********


#define L_P1_C1_NUM_COMANDI_AUTO 0


// ********** Struct **********

typedef struct Classe_L_P1_C1 {

    // dati dinamici invisibili
    ExecResponse response;
} Classe_L_P1_C1;


// ********** Getter privati **********

// parametri
Intero L_P1__GetParamMainc2(instance_id_t const my_id);
C1_Enumerat4 L_P1__GetParamMainc3(instance_id_t const my_id);
Intero L_P1__GetParamMainc4(instance_id_t const my_id);


// record

// comandi automatici

// valori sicuri

#endif // LIBSTAZIONE_CLASSEL_P1_C1_PRIV_H
