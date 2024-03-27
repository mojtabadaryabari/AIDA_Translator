// Codice del modello 'TestCase12', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
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
    C1_Enumerat2 mainc6;
    Intero mainc7;
    Intero mainc8;
    bool mainc9;
} Classe_L_P1_C1_Param;

// ********** Record liste enti collegati classe L_P1_C1 **********

// ********** Parametri classe L_P1_C2 **********

typedef struct Classe_L_P1_C2_Param {
    C2_Enumerat2 subcl10;
    bool subcl11;
    Intero subcl12;
    offset_t subcl7_start;
    index_t subcl7_length;
    offset_t subcl8_start;
    index_t subcl8_length;
    offset_t subcl9_start;
    index_t subcl9_length;
} Classe_L_P1_C2_Param;

// ********** Record liste enti collegati classe L_P1_C2 **********

typedef struct L_P1__Recor {
    instance_id_t mainc47;
    C2_Enumerat1 recor;
    C2_Enumerat4 recor1;
    C2_Enumerat4 recor2;
} L_P1__Recor;

// ********** Parametri classe L_P1_C3 **********

typedef struct Classe_L_P1_C3_Param {
    bool subcl51;
    C3_Enumerat3 subcl52;
    Intero subcl53;
    Intero subcl54;
    Intero subcl55;
    offset_t subcl49_start;
    index_t subcl49_length;
    offset_t subcl50_start;
    index_t subcl50_length;
} Classe_L_P1_C3_Param;

// ********** Record liste enti collegati classe L_P1_C3 **********

typedef struct L_P1__Recor1 {
    instance_id_t mainc48;
    C3_Enumerat1 recor3;
    bool recor4;
} L_P1__Recor1;

typedef struct L_P1__Recor2 {
    instance_id_t mainc49;
    C3_Enumerat1 recor5;
    bool recor6;
} L_P1__Recor2;



#endif // LIBSTAZIONE_PARAM_H
