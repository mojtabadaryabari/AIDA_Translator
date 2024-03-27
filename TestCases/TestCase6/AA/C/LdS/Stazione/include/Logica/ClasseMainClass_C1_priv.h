// Codice del modello 'TestCase6', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#ifndef LIBSTAZIONE_CLASSEL_P1_C1_PRIV_H
#define LIBSTAZIONE_CLASSEL_P1_C1_PRIV_H

#include "Logica/ClasseMainClass_C1.h"
#include "lds_param.h"


// ********** Comandi automatici **********

typedef struct {
    bool event;
    C1_Enumerat1 argom;
    C1_Enumerat3 argom1;
    bool argom2;
} L_P1_C1_Comandi_Auto;

#define L_P1_C1_NUM_COMANDI_AUTO 1


// ********** Struct **********

typedef struct Classe_L_P1_C1 {

    // dati dinamici invisibili
    Timer mainc35;
    Timer mainc36;
    Timer mainc37;
    Timer mainc38;
    Timer mainc39;
    Timer mainc40;
    Timer mainc41;
    Timer mainc42;
    Counter mainc43;
    Counter mainc44;
    L_P1_C1_Comandi_Auto comandi_automatici;
    ExecResponse response;
} Classe_L_P1_C1;


// ********** Getter/setter privati **********

// parametri
C1_Enumerat4 L_P1__GetParamMainc9(instance_id_t const my_id);
C1_Enumerat2 L_P1__GetParamMainc10(instance_id_t const my_id);
bool L_P1__GetParamMainc11(instance_id_t const my_id);
bool L_P1__GetParamMainc12(instance_id_t const my_id);
Intero L_P1__GetParamMainc13(instance_id_t const my_id);


// record

// comandi automatici
/* bool L_P1__GetCAEvent(instance_id_t const my_id); */
#define L_P1__GetCAEvent(my_id) (lds_Stazione_data->L_P1_C1[my_id].comandi_automatici.event)

/* C1_Enumerat1 L_P1__GetCAArgom(instance_id_t const my_id); */
#define L_P1__GetCAArgom(my_id)  (lds_Stazione_data->L_P1_C1[my_id].comandi_automatici.argom)

/* C1_Enumerat3 L_P1__GetCAArgom1(instance_id_t const my_id); */
#define L_P1__GetCAArgom1(my_id)  (lds_Stazione_data->L_P1_C1[my_id].comandi_automatici.argom1)

/* bool L_P1__GetCAArgom2(instance_id_t const my_id); */
#define L_P1__GetCAArgom2(my_id)  (lds_Stazione_data->L_P1_C1[my_id].comandi_automatici.argom2)

/* void L_P1__SetCAEvent(instance_id_t const my_id, bool const value); */
#define L_P1__SetCAEvent(my_id, value)   lds_Stazione_data->L_P1_C1[my_id].comandi_automatici.event = (value)

/* void L_P1__SetCAArgom(instance_id_t const my_id, C1_Enumerat1 const value); */
#define L_P1__SetCAArgom(my_id, value)  lds_Stazione_data->L_P1_C1[my_id].comandi_automatici.argom = (value)

/* void L_P1__SetCAArgom1(instance_id_t const my_id, C1_Enumerat3 const value); */
#define L_P1__SetCAArgom1(my_id, value)  lds_Stazione_data->L_P1_C1[my_id].comandi_automatici.argom1 = (value)

/* void L_P1__SetCAArgom2(instance_id_t const my_id, bool const value); */
#define L_P1__SetCAArgom2(my_id, value)  lds_Stazione_data->L_P1_C1[my_id].comandi_automatici.argom2 = (value)



// response
ExecResponse L_P1_C1_GetResponse(instance_id_t const my_id);
void L_P1_C1_SetResponse(instance_id_t const my_id, ExecResponse const value);


#endif // LIBSTAZIONE_CLASSEL_P1_C1_PRIV_H
