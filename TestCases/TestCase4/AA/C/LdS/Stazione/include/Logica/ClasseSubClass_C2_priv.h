// Codice del modello 'TestCase4', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#ifndef LIBSTAZIONE_CLASSEL_P1_C2_PRIV_H
#define LIBSTAZIONE_CLASSEL_P1_C2_PRIV_H

#include "Logica/ClasseSubClass_C2.h"
#include "lds_param.h"


// ********** Comandi automatici **********


#define L_P1_C2_NUM_COMANDI_AUTO 0


// ********** Struct **********

typedef struct Classe_L_P1_C2 {

    // dati dinamici invisibili
    Timer subcl38;
    Timer subcl39;
    Timer subcl40;
    Timer subcl41;
    Timer subcl42;
    Timer subcl43;
    Timer subcl44;
    Timer subcl45;
    Timer subcl46;
    Timer subcl47;
    Timer subcl48;
    Timer subcl49;
    Counter subcl50;
    ExecResponse response;
} Classe_L_P1_C2;


// ********** Getter/setter privati **********

// parametri
C2_Enumerat2 L_P1__GetParamSubcl10(instance_id_t const my_id);
bool L_P1__GetParamSubcl11(instance_id_t const my_id);
C2_Enumerat3 L_P1__GetParamSubcl12(instance_id_t const my_id);
bool L_P1__GetParamSubcl13(instance_id_t const my_id);

offset_t L_P1__GetParamSubcl8Start(instance_id_t const my_id);
index_t L_P1__GetParamSubcl8Length(instance_id_t const my_id);
offset_t L_P1__GetParamSubcl9Start(instance_id_t const my_id);
index_t L_P1__GetParamSubcl9Length(instance_id_t const my_id);

// record
L_P1__Recor L_P1__GetRecSubcl8(instance_id_t const my_id, index_t const elem_idx);

L_P1__Recor L_P1__GetRecSubcl9(instance_id_t const my_id, index_t const elem_idx);


// comandi automatici


// response
ExecResponse L_P1_C2_GetResponse(instance_id_t const my_id);
void L_P1_C2_SetResponse(instance_id_t const my_id, ExecResponse const value);


#endif // LIBSTAZIONE_CLASSEL_P1_C2_PRIV_H
