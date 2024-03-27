#ifndef LIBSTAZIONE_PARAM_H
#define LIBSTAZIONE_PARAM_H

#include "envdt.h"
#include "preamble.h"  /* for header preable */


// ********** Header **********

typedef struct {
    T_HeaderPreamble pre;  /*< This field MUST be the first */

    instance_id_t numero_L_P1_C1;
    offset_t offset_L_P1_C1;

    instance_id_t numero_L_P1_C2;
    offset_t offset_L_P1_C2;

    offset_t offset_scheduling_order;
} lds_config_enti_header;


// ********** Parametri classe L_P1_C1 **********

typedef struct Classe_L_P1_C1_Param {
    bool consd;
    Intero lds_m7;
    bool lds_m8;
    bool lds_m9;
    C1_Enumerat3 nabcc;
} Classe_L_P1_C1_Param;

// ********** Record liste enti collegati classe L_P1_C1 **********

// ********** Parametri classe L_P1_C2 **********

typedef struct Classe_L_P1_C2_Param {
    bool consd1;
    C2_Enumerat2 lds_s11;
    offset_t lds_s8_start;
    index_t lds_s8_length;
    offset_t lds_s9_start;
    index_t lds_s9_length;
    offset_t lds_s10_start;
    index_t lds_s10_length;
} Classe_L_P1_C2_Param;

// ********** Record liste enti collegati classe L_P1_C2 **********

typedef struct L_P1__Recor {
    instance_id_t lds_m20;
    C2_Enumerat2 recor;
    C2_Enumerat3 recor1;
    C2_Enumerat3 recor2;
    C2_Enumerat2 recor3;
} L_P1__Recor;

typedef struct L_P1__Recor1 {
    instance_id_t lds_m21;
    bool recor4;
    bool recor5;
    bool recor6;
} L_P1__Recor1;



#endif // LIBSTAZIONE_PARAM_H
