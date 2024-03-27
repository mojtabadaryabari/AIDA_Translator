// Codice del modello 'TestCase11', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
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

    instance_id_t numero_L_P1_C4;
    offset_t offset_L_P1_C4;

    offset_t offset_scheduling_order;
} lds_config_enti_header;


// ********** Parametri classe L_P1_C1 **********

typedef struct Classe_L_P1_C1_Param {
    C1_Enumerat1 mainc5;
    Intero mainc6;
    bool mainc7;
} Classe_L_P1_C1_Param;

// ********** Record liste enti collegati classe L_P1_C1 **********

// ********** Parametri classe L_P1_C2 **********

typedef struct Classe_L_P1_C2_Param {
    Intero subcl11;
    Intero subcl12;
    offset_t subcl9_start;
    index_t subcl9_length;
    offset_t subcl10_start;
    index_t subcl10_length;
} Classe_L_P1_C2_Param;

// ********** Record liste enti collegati classe L_P1_C2 **********

typedef struct L_P1__Recor1 {
    instance_id_t mainc46;
    C2_Enumerat3 recor3;
    C2_Enumerat1 recor4;
} L_P1__Recor1;

typedef struct L_P1__Recor {
    instance_id_t mainc45;
    C2_Enumerat3 recor;
    C2_Enumerat2 recor1;
    bool recor2;
} L_P1__Recor;

// ********** Parametri classe L_P1_C3 **********

typedef struct Classe_L_P1_C3_Param {
    bool subcl50;
    Intero subcl51;
    Intero subcl52;
    bool subcl53;
    C3_Enumerat3 subcl54;
    offset_t subcl45_start;
    index_t subcl45_length;
    offset_t subcl46_start;
    index_t subcl46_length;
    offset_t subcl47_start;
    index_t subcl47_length;
    offset_t subcl48_start;
    index_t subcl48_length;
    offset_t subcl49_start;
    index_t subcl49_length;
} Classe_L_P1_C3_Param;

// ********** Record liste enti collegati classe L_P1_C3 **********

typedef struct L_P1__Recor2 {
    instance_id_t mainc47;
    bool recor5;
    bool recor6;
    bool recor7;
    C3_Enumerat4 recor8;
} L_P1__Recor2;

// ********** Parametri classe L_P1_C4 **********

typedef struct Classe_L_P1_C4_Param {
    bool subcl96;
    bool subcl97;
    Intero subcl98;
    offset_t subcl95_start;
    index_t subcl95_length;
} Classe_L_P1_C4_Param;

// ********** Record liste enti collegati classe L_P1_C4 **********

typedef struct L_P1__Recor3 {
    instance_id_t mainc48;
    bool recor9;
    C4_Enumerat3 recor10;
    bool recor11;
    C4_Enumerat4 recor12;
} L_P1__Recor3;



#endif // LIBSTAZIONE_PARAM_H
