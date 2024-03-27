// Codice del modello 'TestCase8', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#ifndef LIBSTAZIONE_CLASSEL_P1_C1_PRIV_H
#define LIBSTAZIONE_CLASSEL_P1_C1_PRIV_H

#include "Logica/ClasseMainClass_C1.h"
#include "lds_param.h"


// ********** Comandi automatici **********


#define L_P1_C1_NUM_COMANDI_AUTO 0


// ********** Struct **********

typedef struct Classe_L_P1_C1 {

    // dati dinamici invisibili
    Timer mainc29;
    Timer mainc30;
    Timer mainc31;
    Timer mainc32;
    Timer mainc33;
    Timer mainc34;
    Timer mainc35;
    Counter mainc36;
    Counter mainc37;
    ExecResponse response;
} Classe_L_P1_C1;


// ********** Getter/setter privati **********

// parametri
Intero L_P1__GetParamMainc2(instance_id_t const my_id);
C1_Enumerat4 L_P1__GetParamMainc3(instance_id_t const my_id);
Intero L_P1__GetParamMainc4(instance_id_t const my_id);


// record

// comandi automatici


// response
ExecResponse L_P1_C1_GetResponse(instance_id_t const my_id);
void L_P1_C1_SetResponse(instance_id_t const my_id, ExecResponse const value);


#endif // LIBSTAZIONE_CLASSEL_P1_C1_PRIV_H
