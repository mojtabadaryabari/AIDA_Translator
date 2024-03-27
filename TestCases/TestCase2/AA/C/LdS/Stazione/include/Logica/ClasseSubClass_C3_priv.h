// Codice del modello 'TestCase2', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#ifndef LIBSTAZIONE_CLASSEL_P1_C3_PRIV_H
#define LIBSTAZIONE_CLASSEL_P1_C3_PRIV_H

#include "Logica/ClasseSubClass_C3.h"
#include "lds_param.h"


// ********** Comandi automatici **********


#define L_P1_C3_NUM_COMANDI_AUTO 0


// ********** Struct **********

typedef struct Classe_L_P1_C3 {

    // dati dinamici invisibili
    Timer subcl102;
    Timer subcl103;
    Timer subcl104;
    Timer subcl105;
    Timer subcl106;
    Timer subcl107;
    Timer subcl108;
    Timer subcl109;
    Timer subcl110;
    Timer subcl111;
    Timer subcl112;
    Timer subcl113;
    Counter subcl114;
    Counter subcl115;
    Counter subcl116;
    Counter subcl117;
    ExecResponse response;
} Classe_L_P1_C3;


// ********** Getter/setter privati **********

// parametri
C3_Enumerat1 L_P1__GetParamSubcl66(instance_id_t const my_id);
Intero L_P1__GetParamSubcl67(instance_id_t const my_id);
bool L_P1__GetParamSubcl68(instance_id_t const my_id);

offset_t L_P1__GetParamSubcl63Start(instance_id_t const my_id);
index_t L_P1__GetParamSubcl63Length(instance_id_t const my_id);
offset_t L_P1__GetParamSubcl64Start(instance_id_t const my_id);
index_t L_P1__GetParamSubcl64Length(instance_id_t const my_id);
offset_t L_P1__GetParamSubcl65Start(instance_id_t const my_id);
index_t L_P1__GetParamSubcl65Length(instance_id_t const my_id);

// record
L_P1__Recor2 L_P1__GetRecSubcl63(instance_id_t const my_id, index_t const elem_idx);

L_P1__Recor2 L_P1__GetRecSubcl64(instance_id_t const my_id, index_t const elem_idx);

L_P1__Recor2 L_P1__GetRecSubcl65(instance_id_t const my_id, index_t const elem_idx);


// comandi automatici


// response
ExecResponse L_P1_C3_GetResponse(instance_id_t const my_id);
void L_P1_C3_SetResponse(instance_id_t const my_id, ExecResponse const value);


#endif // LIBSTAZIONE_CLASSEL_P1_C3_PRIV_H
