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
C3_Enumerat1 L_P1__GetParamSubcl66(instance_id_t const my_id);
Intero L_P1__GetParamSubcl67(instance_id_t const my_id);
bool L_P1__GetParamSubcl68(instance_id_t const my_id);


// record

// comandi automatici

// valori sicuri

#endif // LIBSTAZIONE_CLASSEL_P1_C3_PRIV_H
