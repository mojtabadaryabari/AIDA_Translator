// Codice del modello 'TestCase18', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
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
    bool mainc5;
    C1_Enumerat4 mainc6;
    bool mainc7;
    bool mainc8;
    Intero mainc9;
} Classe_L_P1_C1_Param;

// ********** Record liste enti collegati classe L_P1_C1 **********

// ********** Parametri classe L_P1_C2 **********

typedef struct Classe_L_P1_C2_Param {
    C2_Enumerat3 subcl10;
    C2_Enumerat1 subcl11;
    Intero subcl12;
    Intero subcl13;
    Intero subcl14;
    offset_t subcl7_start;
    index_t subcl7_length;
    offset_t subcl8_start;
    index_t subcl8_length;
    offset_t subcl9_start;
    index_t subcl9_length;
} Classe_L_P1_C2_Param;

// ********** Record liste enti collegati classe L_P1_C2 **********

typedef struct L_P1__Recor {
    instance_id_t mainc55;
    bool recor;
    bool recor1;
} L_P1__Recor;



#endif // LIBSTAZIONE_PARAM_H
