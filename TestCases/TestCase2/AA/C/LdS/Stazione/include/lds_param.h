// Codice del modello 'TestCase2', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
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
    C1_Enumerat4 mainc5;
} Classe_L_P1_C1_Param;

// ********** Record liste enti collegati classe L_P1_C1 **********

// ********** Parametri classe L_P1_C2 **********

typedef struct Classe_L_P1_C2_Param {
    C2_Enumerat1 subcl11;
    bool subcl12;
    C2_Enumerat4 subcl13;
    C2_Enumerat1 subcl14;
    Intero subcl15;
    offset_t subcl7_start;
    index_t subcl7_length;
    offset_t subcl8_start;
    index_t subcl8_length;
    offset_t subcl9_start;
    index_t subcl9_length;
    offset_t subcl10_start;
    index_t subcl10_length;
} Classe_L_P1_C2_Param;

// ********** Record liste enti collegati classe L_P1_C2 **********

typedef struct L_P1__Recor1 {
    instance_id_t mainc37;
    C2_Enumerat3 recor2;
    C2_Enumerat1 recor3;
    bool recor4;
} L_P1__Recor1;

typedef struct L_P1__Recor {
    instance_id_t mainc36;
    C2_Enumerat4 recor;
    bool recor1;
} L_P1__Recor;

// ********** Parametri classe L_P1_C3 **********

typedef struct Classe_L_P1_C3_Param {
    C3_Enumerat1 subcl66;
    Intero subcl67;
    bool subcl68;
    offset_t subcl63_start;
    index_t subcl63_length;
    offset_t subcl64_start;
    index_t subcl64_length;
    offset_t subcl65_start;
    index_t subcl65_length;
} Classe_L_P1_C3_Param;

// ********** Record liste enti collegati classe L_P1_C3 **********

typedef struct L_P1__Recor2 {
    instance_id_t mainc38;
    C3_Enumerat2 recor5;
    C3_Enumerat4 recor6;
} L_P1__Recor2;



#endif // LIBSTAZIONE_PARAM_H
