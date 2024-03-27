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
C2_Enumerat4 L_P1__GetParamSubcl13(instance_id_t const my_id);
C2_Enumerat4 L_P1__GetParamSubcl14(instance_id_t const my_id);


// record

// comandi automatici

// valori sicuri

#endif // LIBSTAZIONE_CLASSEL_P1_C2_PRIV_H
