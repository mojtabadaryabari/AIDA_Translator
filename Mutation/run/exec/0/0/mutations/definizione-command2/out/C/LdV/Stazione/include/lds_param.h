#ifndef LIBSTAZIONE_PARAM_H
#define LIBSTAZIONE_PARAM_H

#include "envdt.h"
#include "preamble.h"  /* for header preable */


// ********** Header **********

typedef struct {
    T_HeaderPreamble pre;  /*< This field MUST be the first */

    instance_id_t numero_L_P1_C3;
    offset_t offset_L_P1_C3;

    offset_t offset_scheduling_order;
} ldv_config_enti_header;


// ********** Parametri classe L_P1_C3 **********

typedef struct Classe_L_P1_C3_Param {
    bool consd2;
    bool ldv_m1;
    Intero ldv_m2;
    C3_Enumerat1 ldv_m3;
} Classe_L_P1_C3_Param;

// ********** Record liste enti collegati classe L_P1_C3 **********



#endif // LIBSTAZIONE_PARAM_H
