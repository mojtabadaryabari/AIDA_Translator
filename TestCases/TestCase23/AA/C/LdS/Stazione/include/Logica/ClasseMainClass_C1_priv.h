// Codice del modello 'TestCase23', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#ifndef LIBSTAZIONE_CLASSEL_P1_C1_PRIV_H
#define LIBSTAZIONE_CLASSEL_P1_C1_PRIV_H

#include "Logica/ClasseMainClass_C1.h"
#include "lds_param.h"


// ********** Comandi automatici **********

typedef struct {
    bool event1;
} L_P1_C1_Comandi_Auto;

#define L_P1_C1_NUM_COMANDI_AUTO 1


// ********** Struct **********

typedef struct Classe_L_P1_C1 {

    // dati dinamici invisibili
    Timer mainc28;
    Timer mainc29;
    Timer mainc30;
    Timer mainc31;
    Timer mainc32;
    Timer mainc33;
    Timer mainc34;
    Timer mainc35;
    Timer mainc36;
    Timer mainc37;
    Timer mainc38;
    Counter mainc39;
    L_P1_C1_Comandi_Auto comandi_automatici;
    ExecResponse response;
} Classe_L_P1_C1;


// ********** Getter/setter privati **********

// parametri
Intero L_P1__GetParamMainc7(instance_id_t const my_id);
bool L_P1__GetParamMainc8(instance_id_t const my_id);
Intero L_P1__GetParamMainc9(instance_id_t const my_id);
C1_Enumerat4 L_P1__GetParamMainc10(instance_id_t const my_id);


// record

// comandi automatici
/* bool L_P1__GetCAEvent1(instance_id_t const my_id); */
#define L_P1__GetCAEvent1(my_id) (lds_Stazione_data->L_P1_C1[my_id].comandi_automatici.event1)

/* void L_P1__SetCAEvent1(instance_id_t const my_id, bool const value); */
#define L_P1__SetCAEvent1(my_id, value)   lds_Stazione_data->L_P1_C1[my_id].comandi_automatici.event1 = (value)



// response
ExecResponse L_P1_C1_GetResponse(instance_id_t const my_id);
void L_P1_C1_SetResponse(instance_id_t const my_id, ExecResponse const value);


#endif // LIBSTAZIONE_CLASSEL_P1_C1_PRIV_H
