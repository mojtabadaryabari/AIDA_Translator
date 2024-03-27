// Codice del modello 'TestCase24', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
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
    Intero mainc8;
    Intero mainc9;
    bool mainc10;
    C1_Enumerat2 mainc11;
    C1_Enumerat4 mainc12;
} Classe_L_P1_C1_Param;

// ********** Record liste enti collegati classe L_P1_C1 **********

// ********** Parametri classe L_P1_C2 **********

typedef struct Classe_L_P1_C2_Param {
    Intero subcl14;
    Intero subcl15;
    Intero subcl16;
    Intero subcl17;
    offset_t subcl9_start;
    index_t subcl9_length;
    offset_t subcl10_start;
    index_t subcl10_length;
    offset_t subcl11_start;
    index_t subcl11_length;
    offset_t subcl12_start;
    index_t subcl12_length;
    offset_t subcl13_start;
    index_t subcl13_length;
} Classe_L_P1_C2_Param;

// ********** Record liste enti collegati classe L_P1_C2 **********

typedef struct L_P1__Recor {
    instance_id_t mainc53;
    bool recor;
    C2_Enumerat4 recor1;
    bool recor2;
} L_P1__Recor;

typedef struct L_P1__Recor1 {
    instance_id_t mainc54;
    C2_Enumerat4 recor3;
    bool recor4;
    C2_Enumerat2 recor5;
} L_P1__Recor1;



#endif // LIBSTAZIONE_PARAM_H
