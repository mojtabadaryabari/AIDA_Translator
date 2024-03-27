// Codice del modello 'TestCase18', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#ifndef LIBSTAZIONE_CLASSEL_P1_C1_PRIV_H
#define LIBSTAZIONE_CLASSEL_P1_C1_PRIV_H

#include "Logica/ClasseMainClass_C1.h"
#include "lds_param.h"


// ********** Comandi automatici **********


#define L_P1_C1_NUM_COMANDI_AUTO 0


// ********** Struct **********

typedef struct Classe_L_P1_C1 {

    // dati dinamici invisibili
    Timer mainc41;
    Timer mainc42;
    Timer mainc43;
    Timer mainc44;
    Timer mainc45;
    Timer mainc46;
    Timer mainc47;
    Timer mainc48;
    Timer mainc49;
    Timer mainc50;
    Timer mainc51;
    Counter mainc52;
    Counter mainc53;
    Counter mainc54;
    ExecResponse response;
} Classe_L_P1_C1;


// ********** Getter/setter privati **********

// parametri
bool L_P1__GetParamMainc5(instance_id_t const my_id);
C1_Enumerat4 L_P1__GetParamMainc6(instance_id_t const my_id);
bool L_P1__GetParamMainc7(instance_id_t const my_id);
bool L_P1__GetParamMainc8(instance_id_t const my_id);
Intero L_P1__GetParamMainc9(instance_id_t const my_id);


// record

// comandi automatici


// response
ExecResponse L_P1_C1_GetResponse(instance_id_t const my_id);
void L_P1_C1_SetResponse(instance_id_t const my_id, ExecResponse const value);


#endif // LIBSTAZIONE_CLASSEL_P1_C1_PRIV_H
