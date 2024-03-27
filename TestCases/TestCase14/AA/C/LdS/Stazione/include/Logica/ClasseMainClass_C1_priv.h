// Codice del modello 'TestCase14', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#ifndef LIBSTAZIONE_CLASSEL_P1_C1_PRIV_H
#define LIBSTAZIONE_CLASSEL_P1_C1_PRIV_H

#include "Logica/ClasseMainClass_C1.h"
#include "lds_param.h"


// ********** Comandi automatici **********

typedef struct {
    bool event2;
} L_P1_C1_Comandi_Auto;

#define L_P1_C1_NUM_COMANDI_AUTO 1


// ********** Struct **********

typedef struct Classe_L_P1_C1 {

    // dati dinamici invisibili
    Timer mainc36;
    Timer mainc37;
    Timer mainc38;
    Timer mainc39;
    Timer mainc40;
    Timer mainc41;
    Timer mainc42;
    Timer mainc43;
    Timer mainc44;
    Timer mainc45;
    Timer mainc46;
    Counter mainc47;
    Counter mainc48;
    L_P1_C1_Comandi_Auto comandi_automatici;
    ExecResponse response;
} Classe_L_P1_C1;


// ********** Getter/setter privati **********

// parametri
C1_Enumerat3 L_P1__GetParamMainc10(instance_id_t const my_id);
C1_Enumerat1 L_P1__GetParamMainc11(instance_id_t const my_id);


// record

// comandi automatici
/* bool L_P1__GetCAEvent2(instance_id_t const my_id); */
#define L_P1__GetCAEvent2(my_id) (lds_Stazione_data->L_P1_C1[my_id].comandi_automatici.event2)

/* void L_P1__SetCAEvent2(instance_id_t const my_id, bool const value); */
#define L_P1__SetCAEvent2(my_id, value)   lds_Stazione_data->L_P1_C1[my_id].comandi_automatici.event2 = (value)



// response
ExecResponse L_P1_C1_GetResponse(instance_id_t const my_id);
void L_P1_C1_SetResponse(instance_id_t const my_id, ExecResponse const value);


#endif // LIBSTAZIONE_CLASSEL_P1_C1_PRIV_H
