// Codice del modello 'TestCase7', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
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
    bool mainc6;
    bool mainc7;
    Intero mainc8;
    Intero mainc9;
    bool mainc10;
} Classe_L_P1_C1_Param;

// ********** Record liste enti collegati classe L_P1_C1 **********

// ********** Parametri classe L_P1_C2 **********

typedef struct Classe_L_P1_C2_Param {
    Intero subcl10;
    bool subcl11;
    C2_Enumerat2 subcl12;
    Intero subcl13;
    offset_t subcl5_start;
    index_t subcl5_length;
    offset_t subcl6_start;
    index_t subcl6_length;
    offset_t subcl7_start;
    index_t subcl7_length;
    offset_t subcl8_start;
    index_t subcl8_length;
    offset_t subcl9_start;
    index_t subcl9_length;
} Classe_L_P1_C2_Param;

// ********** Record liste enti collegati classe L_P1_C2 **********

typedef struct L_P1__Recor {
    instance_id_t mainc45;
    bool recor;
    C2_Enumerat1 recor1;
    bool recor2;
} L_P1__Recor;

typedef struct L_P1__Recor1 {
    instance_id_t mainc46;
    bool recor3;
    bool recor4;
    bool recor5;
    C2_Enumerat1 recor6;
} L_P1__Recor1;



#endif // LIBSTAZIONE_PARAM_H
