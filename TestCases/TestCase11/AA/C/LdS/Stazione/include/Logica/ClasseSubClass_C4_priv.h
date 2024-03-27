// Codice del modello 'TestCase11', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#ifndef LIBSTAZIONE_CLASSEL_P1_C4_PRIV_H
#define LIBSTAZIONE_CLASSEL_P1_C4_PRIV_H

#include "Logica/ClasseSubClass_C4.h"
#include "lds_param.h"


// ********** Comandi automatici **********


#define L_P1_C4_NUM_COMANDI_AUTO 0


// ********** Struct **********

typedef struct Classe_L_P1_C4 {

    // dati dinamici invisibili
    Timer subcl114;
    Timer subcl115;
    Timer subcl116;
    Timer subcl117;
    Timer subcl118;
    Timer subcl119;
    Timer subcl120;
    Timer subcl121;
    Timer subcl122;
    Timer subcl123;
    Timer subcl124;
    Counter subcl125;
    Counter subcl126;
    ExecResponse response;
} Classe_L_P1_C4;


// ********** Getter/setter privati **********

// parametri
bool L_P1__GetParamSubcl96(instance_id_t const my_id);
bool L_P1__GetParamSubcl97(instance_id_t const my_id);
Intero L_P1__GetParamSubcl98(instance_id_t const my_id);

offset_t L_P1__GetParamSubcl95Start(instance_id_t const my_id);
index_t L_P1__GetParamSubcl95Length(instance_id_t const my_id);

// record
L_P1__Recor3 L_P1__GetRecSubcl95(instance_id_t const my_id, index_t const elem_idx);


// comandi automatici


// response
ExecResponse L_P1_C4_GetResponse(instance_id_t const my_id);
void L_P1_C4_SetResponse(instance_id_t const my_id, ExecResponse const value);


#endif // LIBSTAZIONE_CLASSEL_P1_C4_PRIV_H
