// Codice del modello 'TestCase10', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#ifndef LIBSTAZIONE_PARAM_H
#define LIBSTAZIONE_PARAM_H

#include "envdt.h"


// ********** Header **********

typedef struct {
    uint8_t plant_type;
    uint8_t station_id;

    instance_id_t numero_L_P1_C1;
    offset_t offset_L_P1_C1;

    instance_id_t numero_L_P1_C2;
    offset_t offset_L_P1_C2;

    instance_id_t numero_L_P1_C3;
    offset_t offset_L_P1_C3;

    offset_t offset_scheduling_order;
} lds_config_enti_header;


// ********** Parametri classe L_P1_C1 **********

typedef struct Classe_L_P1_C1_Param {
    C1_Enumerat3 mainc7;
} Classe_L_P1_C1_Param;

// ********** Record liste enti collegati classe L_P1_C1 **********

// ********** Parametri classe L_P1_C2 **********

typedef struct Classe_L_P1_C2_Param {
    Intero subcl8;
    offset_t subcl7_start;
    index_t subcl7_length;
} Classe_L_P1_C2_Param;

// ********** Record liste enti collegati classe L_P1_C2 **********

typedef struct L_P1__Recor {
    instance_id_t mainc32;
    C2_Enumerat1 recor;
    C2_Enumerat3 recor1;
    bool recor2;
} L_P1__Recor;

// ********** Parametri classe L_P1_C3 **********

typedef struct Classe_L_P1_C3_Param {
    Intero subcl48;
    bool subcl49;
    offset_t subcl46_start;
    index_t subcl46_length;
    offset_t subcl47_start;
    index_t subcl47_length;
} Classe_L_P1_C3_Param;

// ********** Record liste enti collegati classe L_P1_C3 **********

typedef struct L_P1__Recor2 {
    instance_id_t mainc34;
    C3_Enumerat2 recor7;
    C3_Enumerat4 recor8;
} L_P1__Recor2;

typedef struct L_P1__Recor1 {
    instance_id_t mainc33;
    bool recor3;
    C3_Enumerat3 recor4;
    C3_Enumerat2 recor5;
    C3_Enumerat4 recor6;
} L_P1__Recor1;



#endif // LIBSTAZIONE_PARAM_H
