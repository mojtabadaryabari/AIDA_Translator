// Codice del modello 'TestCase10', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#ifndef LIBSTAZIONE_CLASSEL_P1_C1_PRIV_H
#define LIBSTAZIONE_CLASSEL_P1_C1_PRIV_H

#include "Logica/ClasseMainClass_C1.h"
#include "lds_param.h"


// ********** Comandi automatici **********

typedef struct {
    bool event2;
    bool event3;
} L_P1_C1_Comandi_Auto;

#define L_P1_C1_NUM_COMANDI_AUTO 2


// ********** Struct **********

typedef struct Classe_L_P1_C1 {

    // dati dinamici invisibili
    Timer mainc23;
    Timer mainc24;
    Timer mainc25;
    Timer mainc26;
    Timer mainc27;
    Timer mainc28;
    Timer mainc29;
    Timer mainc30;
    Counter mainc31;
    L_P1_C1_Comandi_Auto comandi_automatici;
    ExecResponse response;
} Classe_L_P1_C1;


// ********** Getter/setter privati **********

// parametri
C1_Enumerat3 L_P1__GetParamMainc7(instance_id_t const my_id);


// record

// comandi automatici
/* bool L_P1__GetCAEvent2(instance_id_t const my_id); */
#define L_P1__GetCAEvent2(my_id) (lds_Stazione_data->L_P1_C1[my_id].comandi_automatici.event2)

/* bool L_P1__GetCAEvent3(instance_id_t const my_id); */
#define L_P1__GetCAEvent3(my_id) (lds_Stazione_data->L_P1_C1[my_id].comandi_automatici.event3)

/* void L_P1__SetCAEvent2(instance_id_t const my_id, bool const value); */
#define L_P1__SetCAEvent2(my_id, value)   lds_Stazione_data->L_P1_C1[my_id].comandi_automatici.event2 = (value)

/* void L_P1__SetCAEvent3(instance_id_t const my_id, bool const value); */
#define L_P1__SetCAEvent3(my_id, value)   lds_Stazione_data->L_P1_C1[my_id].comandi_automatici.event3 = (value)



// response
ExecResponse L_P1_C1_GetResponse(instance_id_t const my_id);
void L_P1_C1_SetResponse(instance_id_t const my_id, ExecResponse const value);


#endif // LIBSTAZIONE_CLASSEL_P1_C1_PRIV_H
