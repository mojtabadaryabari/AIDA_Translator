// Codice del modello 'TestCase19', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
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
    C1_Enumerat2 mainc5;
    C1_Enumerat3 mainc6;
    Intero mainc7;
} Classe_L_P1_C1_Param;

// ********** Record liste enti collegati classe L_P1_C1 **********

// ********** Parametri classe L_P1_C2 **********

typedef struct Classe_L_P1_C2_Param {
    C2_Enumerat4 subcl8;
    C2_Enumerat3 subcl9;
    bool subcl10;
    Intero subcl11;
    offset_t subcl5_start;
    index_t subcl5_length;
    offset_t subcl6_start;
    index_t subcl6_length;
    offset_t subcl7_start;
    index_t subcl7_length;
} Classe_L_P1_C2_Param;

// ********** Record liste enti collegati classe L_P1_C2 **********

typedef struct L_P1__Recor1 {
    instance_id_t mainc40;
    bool recor2;
    bool recor3;
    C2_Enumerat1 recor4;
} L_P1__Recor1;

typedef struct L_P1__Recor {
    instance_id_t mainc39;
    bool recor;
    C2_Enumerat1 recor1;
} L_P1__Recor;



#endif // LIBSTAZIONE_PARAM_H
