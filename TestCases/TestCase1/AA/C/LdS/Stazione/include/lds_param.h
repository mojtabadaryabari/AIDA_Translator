// Codice del modello 'TestCase1', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
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

    offset_t offset_scheduling_order;
} lds_config_enti_header;


// ********** Parametri classe L_P1_C1 **********

typedef struct Classe_L_P1_C1_Param {
    Intero mainc5;
    Intero mainc6;
    C1_Enumerat2 mainc7;
    C1_Enumerat2 mainc8;
    Intero mainc9;
} Classe_L_P1_C1_Param;

// ********** Record liste enti collegati classe L_P1_C1 **********

// ********** Parametri classe L_P1_C2 **********

typedef struct Classe_L_P1_C2_Param {
    Intero subcl8;
    Intero subcl9;
    offset_t subcl4_start;
    index_t subcl4_length;
    offset_t subcl5_start;
    index_t subcl5_length;
    offset_t subcl6_start;
    index_t subcl6_length;
    offset_t subcl7_start;
    index_t subcl7_length;
} Classe_L_P1_C2_Param;

// ********** Record liste enti collegati classe L_P1_C2 **********

typedef struct L_P1__Recor1 {
    instance_id_t mainc37;
    C2_Enumerat3 recor2;
    C2_Enumerat1 recor3;
} L_P1__Recor1;

typedef struct L_P1__Recor {
    instance_id_t mainc36;
    bool recor;
    C2_Enumerat1 recor1;
} L_P1__Recor;



#endif // LIBSTAZIONE_PARAM_H
