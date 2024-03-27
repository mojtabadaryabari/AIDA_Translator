// Codice del modello 'TestCase6', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#ifndef LIBSTAZIONE_CLASSEL_P1_C2_PRIV_H
#define LIBSTAZIONE_CLASSEL_P1_C2_PRIV_H

#include "Logica/ClasseSubClass_C2.h"
#include "lds_param.h"


// ********** Comandi automatici **********


#define L_P1_C2_NUM_COMANDI_AUTO 0


// ********** Struct **********

typedef struct Classe_L_P1_C2 {

    // dati dinamici invisibili
    Timer subcl36;
    Timer subcl37;
    Timer subcl38;
    Timer subcl39;
    Timer subcl40;
    Timer subcl41;
    Counter subcl42;
    Counter subcl43;
    Counter subcl44;
    Counter subcl45;
    ExecResponse response;
} Classe_L_P1_C2;


// ********** Getter/setter privati **********

// parametri
C2_Enumerat4 L_P1__GetParamSubcl13(instance_id_t const my_id);
C2_Enumerat4 L_P1__GetParamSubcl14(instance_id_t const my_id);

offset_t L_P1__GetParamSubcl9Start(instance_id_t const my_id);
index_t L_P1__GetParamSubcl9Length(instance_id_t const my_id);
offset_t L_P1__GetParamSubcl10Start(instance_id_t const my_id);
index_t L_P1__GetParamSubcl10Length(instance_id_t const my_id);
offset_t L_P1__GetParamSubcl11Start(instance_id_t const my_id);
index_t L_P1__GetParamSubcl11Length(instance_id_t const my_id);
offset_t L_P1__GetParamSubcl12Start(instance_id_t const my_id);
index_t L_P1__GetParamSubcl12Length(instance_id_t const my_id);

// record
L_P1__Recor L_P1__GetRecSubcl9(instance_id_t const my_id, index_t const elem_idx);

L_P1__Recor1 L_P1__GetRecSubcl10(instance_id_t const my_id, index_t const elem_idx);

L_P1__Recor1 L_P1__GetRecSubcl11(instance_id_t const my_id, index_t const elem_idx);

L_P1__Recor1 L_P1__GetRecSubcl12(instance_id_t const my_id, index_t const elem_idx);


// comandi automatici


// response
ExecResponse L_P1_C2_GetResponse(instance_id_t const my_id);
void L_P1_C2_SetResponse(instance_id_t const my_id, ExecResponse const value);


#endif // LIBSTAZIONE_CLASSEL_P1_C2_PRIV_H
