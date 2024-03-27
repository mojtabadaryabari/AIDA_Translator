#ifndef FEA_LIBSTAZIONE_CLASSEL_P1_C2_PRIV_H
#define FEA_LIBSTAZIONE_CLASSEL_P1_C2_PRIV_H

#include "Logica/ClasseSubClass_C2.h"
#include "lds_param.h"


// ********** Comandi automatici **********


#define L_P1_C2_NUM_COMANDI_AUTO 0


// ********** Struct **********

typedef struct Classe_L_P1_C2 {

    // dati dinamici invisibili
    ExecResponse response;
} Classe_L_P1_C2;


// ********** Getter privati **********

// parametri
Intero L_P1__GetParamSubcl4(instance_id_t const my_id);
C2_Enumerat1 L_P1__GetParamSubcl5(instance_id_t const my_id);
Intero L_P1__GetParamSubcl6(instance_id_t const my_id);


// record

// comandi automatici

// valori sicuri

#endif // LIBSTAZIONE_CLASSEL_P1_C2_PRIV_H
