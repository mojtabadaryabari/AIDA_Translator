#ifndef FEA_LIBSTAZIONE_CLASSEL_P1_C2_PRIV_H
#define FEA_LIBSTAZIONE_CLASSEL_P1_C2_PRIV_H

#include "Logica/ClasseSubClass_C2.h"
#include "lds_param.h"


// ********** Comandi automatici **********


#define L_P1_C2_NUM_COMANDI_AUTO 0


// ********** Struct **********

typedef struct Classe_L_P1_C2 {

    // dati dinamici invisibili
    Timer subcl45;
    Timer subcl47;
    Timer subcl48;
    Timer subcl49;
    Counter subcl50;
    Counter subcl52;
    ExecResponse response;
} Classe_L_P1_C2;


// ********** Getter privati **********

// parametri
C2_Enumerat4 L_P1__GetParamSubcl8(instance_id_t const my_id);
C2_Enumerat3 L_P1__GetParamSubcl9(instance_id_t const my_id);
bool L_P1__GetParamSubcl10(instance_id_t const my_id);
Intero L_P1__GetParamSubcl11(instance_id_t const my_id);


// record

// comandi automatici

// valori sicuri

#endif // LIBSTAZIONE_CLASSEL_P1_C2_PRIV_H
