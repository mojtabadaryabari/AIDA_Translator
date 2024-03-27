// Codice del modello 'TestCase12', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#ifndef LIBSTAZIONE_CLASSEL_P1_C2_PRIV_H
#define LIBSTAZIONE_CLASSEL_P1_C2_PRIV_H

#include "Logica/ClasseSubClass_C2.h"
#include "lds_param.h"


// ********** Comandi automatici **********


#define L_P1_C2_NUM_COMANDI_AUTO 0


// ********** Struct **********

typedef struct Classe_L_P1_C2 {

    // dati dinamici invisibili
    Timer subcl30;
    Timer subcl31;
    Timer subcl32;
    Timer subcl33;
    Timer subcl34;
    Timer subcl35;
    Timer subcl36;
    Timer subcl37;
    Timer subcl38;
    Timer subcl39;
    Timer subcl40;
    Counter subcl41;
    Counter subcl42;
    ExecResponse response;
} Classe_L_P1_C2;


// ********** Getter/setter privati **********

// parametri
C2_Enumerat2 L_P1__GetParamSubcl10(instance_id_t const my_id);
bool L_P1__GetParamSubcl11(instance_id_t const my_id);
Intero L_P1__GetParamSubcl12(instance_id_t const my_id);

offset_t L_P1__GetParamSubcl7Start(instance_id_t const my_id);
index_t L_P1__GetParamSubcl7Length(instance_id_t const my_id);
offset_t L_P1__GetParamSubcl8Start(instance_id_t const my_id);
index_t L_P1__GetParamSubcl8Length(instance_id_t const my_id);
offset_t L_P1__GetParamSubcl9Start(instance_id_t const my_id);
index_t L_P1__GetParamSubcl9Length(instance_id_t const my_id);

// record
L_P1__Recor L_P1__GetRecSubcl7(instance_id_t const my_id, index_t const elem_idx);

L_P1__Recor L_P1__GetRecSubcl8(instance_id_t const my_id, index_t const elem_idx);

L_P1__Recor L_P1__GetRecSubcl9(instance_id_t const my_id, index_t const elem_idx);


// comandi automatici


// response
ExecResponse L_P1_C2_GetResponse(instance_id_t const my_id);
void L_P1_C2_SetResponse(instance_id_t const my_id, ExecResponse const value);


#endif // LIBSTAZIONE_CLASSEL_P1_C2_PRIV_H
