// Codice del modello 'TestCase12', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#ifndef LIBSTAZIONE_CLASSEL_P1_C3_PRIV_H
#define LIBSTAZIONE_CLASSEL_P1_C3_PRIV_H

#include "Logica/ClasseSubClass_C3.h"
#include "lds_param.h"


// ********** Comandi automatici **********


#define L_P1_C3_NUM_COMANDI_AUTO 0


// ********** Struct **********

typedef struct Classe_L_P1_C3 {

    // dati dinamici invisibili
    Timer subcl77;
    Timer subcl78;
    Timer subcl79;
    Timer subcl80;
    Timer subcl81;
    Timer subcl82;
    Timer subcl83;
    Timer subcl84;
    Timer subcl85;
    Timer subcl86;
    Timer subcl87;
    Timer subcl88;
    Timer subcl89;
    Timer subcl90;
    Timer subcl91;
    Counter subcl92;
    Counter subcl93;
    Counter subcl94;
    ExecResponse response;
} Classe_L_P1_C3;


// ********** Getter/setter privati **********

// parametri
bool L_P1__GetParamSubcl51(instance_id_t const my_id);
C3_Enumerat3 L_P1__GetParamSubcl52(instance_id_t const my_id);
Intero L_P1__GetParamSubcl53(instance_id_t const my_id);
Intero L_P1__GetParamSubcl54(instance_id_t const my_id);
Intero L_P1__GetParamSubcl55(instance_id_t const my_id);

offset_t L_P1__GetParamSubcl49Start(instance_id_t const my_id);
index_t L_P1__GetParamSubcl49Length(instance_id_t const my_id);
offset_t L_P1__GetParamSubcl50Start(instance_id_t const my_id);
index_t L_P1__GetParamSubcl50Length(instance_id_t const my_id);

// record
L_P1__Recor1 L_P1__GetRecSubcl49(instance_id_t const my_id, index_t const elem_idx);

L_P1__Recor2 L_P1__GetRecSubcl50(instance_id_t const my_id, index_t const elem_idx);


// comandi automatici


// response
ExecResponse L_P1_C3_GetResponse(instance_id_t const my_id);
void L_P1_C3_SetResponse(instance_id_t const my_id, ExecResponse const value);


#endif // LIBSTAZIONE_CLASSEL_P1_C3_PRIV_H
