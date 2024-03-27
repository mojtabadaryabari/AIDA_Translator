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
C1_Enumerat1 L_P1__GetParamMainc9(instance_id_t const my_id);
bool L_P1__GetParamMainc10(instance_id_t const my_id);
C1_Enumerat2 L_P1__GetParamMainc11(instance_id_t const my_id);


// record

// comandi automatici

// valori sicuri

#endif // LIBSTAZIONE_CLASSEL_P1_C1_PRIV_H
