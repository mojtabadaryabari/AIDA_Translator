// Codice del modello 'TestCase3', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#ifndef LIBSTAZIONE_CLASSEL_P1_C1_PRIV_H
#define LIBSTAZIONE_CLASSEL_P1_C1_PRIV_H

#include "Logica/ClasseMainClass_C1.h"
#include "lds_param.h"


// ********** Comandi automatici **********

typedef struct {
    bool event1;
    bool event2;
    C1_Enumerat1 argom;
    C1_Enumerat3 argom1;
    bool argom2;
    bool argom3;
} L_P1_C1_Comandi_Auto;

#define L_P1_C1_NUM_COMANDI_AUTO 2


// ********** Struct **********

typedef struct Classe_L_P1_C1 {

    // dati dinamici invisibili
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
    L_P1_C1_Comandi_Auto comandi_automatici;
    ExecResponse response;
} Classe_L_P1_C1;


// ********** Getter/setter privati **********

// parametri
Intero L_P1__GetParamMainc8(instance_id_t const my_id);
Intero L_P1__GetParamMainc9(instance_id_t const my_id);
bool L_P1__GetParamMainc10(instance_id_t const my_id);
C1_Enumerat3 L_P1__GetParamMainc11(instance_id_t const my_id);
Intero L_P1__GetParamMainc12(instance_id_t const my_id);


// record

// comandi automatici
/* bool L_P1__GetCAEvent1(instance_id_t const my_id); */
#define L_P1__GetCAEvent1(my_id) (lds_Stazione_data->L_P1_C1[my_id].comandi_automatici.event1)

/* bool L_P1__GetCAEvent2(instance_id_t const my_id); */
#define L_P1__GetCAEvent2(my_id) (lds_Stazione_data->L_P1_C1[my_id].comandi_automatici.event2)

/* C1_Enumerat1 L_P1__GetCAArgom(instance_id_t const my_id); */
#define L_P1__GetCAArgom(my_id)  (lds_Stazione_data->L_P1_C1[my_id].comandi_automatici.argom)

/* C1_Enumerat3 L_P1__GetCAArgom1(instance_id_t const my_id); */
#define L_P1__GetCAArgom1(my_id)  (lds_Stazione_data->L_P1_C1[my_id].comandi_automatici.argom1)

/* bool L_P1__GetCAArgom2(instance_id_t const my_id); */
#define L_P1__GetCAArgom2(my_id)  (lds_Stazione_data->L_P1_C1[my_id].comandi_automatici.argom2)

/* bool L_P1__GetCAArgom3(instance_id_t const my_id); */
#define L_P1__GetCAArgom3(my_id)  (lds_Stazione_data->L_P1_C1[my_id].comandi_automatici.argom3)

/* void L_P1__SetCAEvent1(instance_id_t const my_id, bool const value); */
#define L_P1__SetCAEvent1(my_id, value)   lds_Stazione_data->L_P1_C1[my_id].comandi_automatici.event1 = (value)

/* void L_P1__SetCAEvent2(instance_id_t const my_id, bool const value); */
#define L_P1__SetCAEvent2(my_id, value)   lds_Stazione_data->L_P1_C1[my_id].comandi_automatici.event2 = (value)

/* void L_P1__SetCAArgom(instance_id_t const my_id, C1_Enumerat1 const value); */
#define L_P1__SetCAArgom(my_id, value)  lds_Stazione_data->L_P1_C1[my_id].comandi_automatici.argom = (value)

/* void L_P1__SetCAArgom1(instance_id_t const my_id, C1_Enumerat3 const value); */
#define L_P1__SetCAArgom1(my_id, value)  lds_Stazione_data->L_P1_C1[my_id].comandi_automatici.argom1 = (value)

/* void L_P1__SetCAArgom2(instance_id_t const my_id, bool const value); */
#define L_P1__SetCAArgom2(my_id, value)  lds_Stazione_data->L_P1_C1[my_id].comandi_automatici.argom2 = (value)

/* void L_P1__SetCAArgom3(instance_id_t const my_id, bool const value); */
#define L_P1__SetCAArgom3(my_id, value)  lds_Stazione_data->L_P1_C1[my_id].comandi_automatici.argom3 = (value)



// response
ExecResponse L_P1_C1_GetResponse(instance_id_t const my_id);
void L_P1_C1_SetResponse(instance_id_t const my_id, ExecResponse const value);


#endif // LIBSTAZIONE_CLASSEL_P1_C1_PRIV_H
