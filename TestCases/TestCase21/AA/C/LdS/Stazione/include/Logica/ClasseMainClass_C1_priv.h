// Codice del modello 'TestCase21', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#ifndef LIBSTAZIONE_CLASSEL_P1_C1_PRIV_H
#define LIBSTAZIONE_CLASSEL_P1_C1_PRIV_H

#include "Logica/ClasseMainClass_C1.h"
#include "lds_param.h"


// ********** Comandi automatici **********

typedef struct {
    bool event;
    bool event1;
    bool event2;
    bool argom;
    C1_Enumerat3 argom1;
    bool argom2;
    C1_Enumerat4 argom3;
    C1_Enumerat3 argom4;
    bool argom5;
    bool argom6;
    C1_Enumerat2 argom7;
} L_P1_C1_Comandi_Auto;

#define L_P1_C1_NUM_COMANDI_AUTO 3


// ********** Struct **********

typedef struct Classe_L_P1_C1 {

    // dati dinamici invisibili
    Timer mainc19;
    Timer mainc20;
    Timer mainc21;
    Timer mainc22;
    Timer mainc23;
    Timer mainc24;
    Timer mainc25;
    Timer mainc26;
    Timer mainc27;
    Timer mainc28;
    Timer mainc29;
    Timer mainc30;
    Counter mainc31;
    Counter mainc32;
    Counter mainc33;
    Counter mainc34;
    L_P1_C1_Comandi_Auto comandi_automatici;
    ExecResponse response;
} Classe_L_P1_C1;


// ********** Getter/setter privati **********

// parametri
C1_Enumerat4 L_P1__GetParamMainc6(instance_id_t const my_id);
Intero L_P1__GetParamMainc7(instance_id_t const my_id);


// record

// comandi automatici
/* bool L_P1__GetCAEvent(instance_id_t const my_id); */
#define L_P1__GetCAEvent(my_id) (lds_Stazione_data->L_P1_C1[my_id].comandi_automatici.event)

/* bool L_P1__GetCAEvent1(instance_id_t const my_id); */
#define L_P1__GetCAEvent1(my_id) (lds_Stazione_data->L_P1_C1[my_id].comandi_automatici.event1)

/* bool L_P1__GetCAEvent2(instance_id_t const my_id); */
#define L_P1__GetCAEvent2(my_id) (lds_Stazione_data->L_P1_C1[my_id].comandi_automatici.event2)

/* bool L_P1__GetCAArgom(instance_id_t const my_id); */
#define L_P1__GetCAArgom(my_id)  (lds_Stazione_data->L_P1_C1[my_id].comandi_automatici.argom)

/* C1_Enumerat3 L_P1__GetCAArgom1(instance_id_t const my_id); */
#define L_P1__GetCAArgom1(my_id)  (lds_Stazione_data->L_P1_C1[my_id].comandi_automatici.argom1)

/* bool L_P1__GetCAArgom2(instance_id_t const my_id); */
#define L_P1__GetCAArgom2(my_id)  (lds_Stazione_data->L_P1_C1[my_id].comandi_automatici.argom2)

/* C1_Enumerat4 L_P1__GetCAArgom3(instance_id_t const my_id); */
#define L_P1__GetCAArgom3(my_id)  (lds_Stazione_data->L_P1_C1[my_id].comandi_automatici.argom3)

/* C1_Enumerat3 L_P1__GetCAArgom4(instance_id_t const my_id); */
#define L_P1__GetCAArgom4(my_id)  (lds_Stazione_data->L_P1_C1[my_id].comandi_automatici.argom4)

/* bool L_P1__GetCAArgom5(instance_id_t const my_id); */
#define L_P1__GetCAArgom5(my_id)  (lds_Stazione_data->L_P1_C1[my_id].comandi_automatici.argom5)

/* bool L_P1__GetCAArgom6(instance_id_t const my_id); */
#define L_P1__GetCAArgom6(my_id)  (lds_Stazione_data->L_P1_C1[my_id].comandi_automatici.argom6)

/* C1_Enumerat2 L_P1__GetCAArgom7(instance_id_t const my_id); */
#define L_P1__GetCAArgom7(my_id)  (lds_Stazione_data->L_P1_C1[my_id].comandi_automatici.argom7)

/* void L_P1__SetCAEvent(instance_id_t const my_id, bool const value); */
#define L_P1__SetCAEvent(my_id, value)   lds_Stazione_data->L_P1_C1[my_id].comandi_automatici.event = (value)

/* void L_P1__SetCAEvent1(instance_id_t const my_id, bool const value); */
#define L_P1__SetCAEvent1(my_id, value)   lds_Stazione_data->L_P1_C1[my_id].comandi_automatici.event1 = (value)

/* void L_P1__SetCAEvent2(instance_id_t const my_id, bool const value); */
#define L_P1__SetCAEvent2(my_id, value)   lds_Stazione_data->L_P1_C1[my_id].comandi_automatici.event2 = (value)

/* void L_P1__SetCAArgom(instance_id_t const my_id, bool const value); */
#define L_P1__SetCAArgom(my_id, value)  lds_Stazione_data->L_P1_C1[my_id].comandi_automatici.argom = (value)

/* void L_P1__SetCAArgom1(instance_id_t const my_id, C1_Enumerat3 const value); */
#define L_P1__SetCAArgom1(my_id, value)  lds_Stazione_data->L_P1_C1[my_id].comandi_automatici.argom1 = (value)

/* void L_P1__SetCAArgom2(instance_id_t const my_id, bool const value); */
#define L_P1__SetCAArgom2(my_id, value)  lds_Stazione_data->L_P1_C1[my_id].comandi_automatici.argom2 = (value)

/* void L_P1__SetCAArgom3(instance_id_t const my_id, C1_Enumerat4 const value); */
#define L_P1__SetCAArgom3(my_id, value)  lds_Stazione_data->L_P1_C1[my_id].comandi_automatici.argom3 = (value)

/* void L_P1__SetCAArgom4(instance_id_t const my_id, C1_Enumerat3 const value); */
#define L_P1__SetCAArgom4(my_id, value)  lds_Stazione_data->L_P1_C1[my_id].comandi_automatici.argom4 = (value)

/* void L_P1__SetCAArgom5(instance_id_t const my_id, bool const value); */
#define L_P1__SetCAArgom5(my_id, value)  lds_Stazione_data->L_P1_C1[my_id].comandi_automatici.argom5 = (value)

/* void L_P1__SetCAArgom6(instance_id_t const my_id, bool const value); */
#define L_P1__SetCAArgom6(my_id, value)  lds_Stazione_data->L_P1_C1[my_id].comandi_automatici.argom6 = (value)

/* void L_P1__SetCAArgom7(instance_id_t const my_id, C1_Enumerat2 const value); */
#define L_P1__SetCAArgom7(my_id, value)  lds_Stazione_data->L_P1_C1[my_id].comandi_automatici.argom7 = (value)



// response
ExecResponse L_P1_C1_GetResponse(instance_id_t const my_id);
void L_P1_C1_SetResponse(instance_id_t const my_id, ExecResponse const value);


#endif // LIBSTAZIONE_CLASSEL_P1_C1_PRIV_H
