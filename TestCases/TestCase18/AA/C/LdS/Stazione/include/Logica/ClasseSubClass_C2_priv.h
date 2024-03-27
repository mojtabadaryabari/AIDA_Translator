// Codice del modello 'TestCase18', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#ifndef LIBSTAZIONE_CLASSEL_P1_C2_PRIV_H
#define LIBSTAZIONE_CLASSEL_P1_C2_PRIV_H

#include "Logica/ClasseSubClass_C2.h"
#include "lds_param.h"


// ********** Comandi automatici **********

typedef struct {
    bool event2;
    bool event3;
    bool event4;
    C2_Enumerat1 argom23;
    bool argom24;
    C2_Enumerat1 argom25;
    C2_Enumerat4 argom26;
} L_P1_C2_Comandi_Auto;

#define L_P1_C2_NUM_COMANDI_AUTO 3


// ********** Struct **********

typedef struct Classe_L_P1_C2 {

    // dati dinamici invisibili
    Timer subcl40;
    Timer subcl41;
    Timer subcl42;
    Timer subcl43;
    Timer subcl44;
    Timer subcl45;
    Timer subcl46;
    Timer subcl47;
    Timer subcl48;
    Timer subcl49;
    Counter subcl50;
    Counter subcl51;
    Counter subcl52;
    L_P1_C2_Comandi_Auto comandi_automatici;
    ExecResponse response;
} Classe_L_P1_C2;


// ********** Getter/setter privati **********

// parametri
C2_Enumerat3 L_P1__GetParamSubcl10(instance_id_t const my_id);
C2_Enumerat1 L_P1__GetParamSubcl11(instance_id_t const my_id);
Intero L_P1__GetParamSubcl12(instance_id_t const my_id);
Intero L_P1__GetParamSubcl13(instance_id_t const my_id);
Intero L_P1__GetParamSubcl14(instance_id_t const my_id);

offset_t L_P1__GetParamSubcl7Start(instance_id_t const my_id);
index_t L_P1__GetParamSubcl7Length(instance_id_t const my_id);
offset_t L_P1__GetParamSubcl8Start(instance_id_t const my_id);
index_t L_P1__GetParamSubcl8Length(instance_id_t const my_id);
offset_t L_P1__GetParamSubcl9Start(instance_id_t const my_id);
index_t L_P1__GetParamSubcl9Length(instance_id_t const my_id);

// record
L_P1__Recor L_P1__GetRecSubcl7(instance_id_t const my_id, index_t const elem_idx);

L_P1__Recor L_P1__GetRecSubcl8(instance_id_t const my_id, index_t const elem_idx);

L_P1__Recor L_P1__GetRecSubcl9(instance_id_t const my_id, index_t const elem_idx);


// comandi automatici
/* bool L_P1__GetCAEvent2(instance_id_t const my_id); */
#define L_P1__GetCAEvent2(my_id) (lds_Stazione_data->L_P1_C2[my_id].comandi_automatici.event2)

/* bool L_P1__GetCAEvent3(instance_id_t const my_id); */
#define L_P1__GetCAEvent3(my_id) (lds_Stazione_data->L_P1_C2[my_id].comandi_automatici.event3)

/* bool L_P1__GetCAEvent4(instance_id_t const my_id); */
#define L_P1__GetCAEvent4(my_id) (lds_Stazione_data->L_P1_C2[my_id].comandi_automatici.event4)

/* C2_Enumerat1 L_P1__GetCAArgom23(instance_id_t const my_id); */
#define L_P1__GetCAArgom23(my_id)  (lds_Stazione_data->L_P1_C2[my_id].comandi_automatici.argom23)

/* bool L_P1__GetCAArgom24(instance_id_t const my_id); */
#define L_P1__GetCAArgom24(my_id)  (lds_Stazione_data->L_P1_C2[my_id].comandi_automatici.argom24)

/* C2_Enumerat1 L_P1__GetCAArgom25(instance_id_t const my_id); */
#define L_P1__GetCAArgom25(my_id)  (lds_Stazione_data->L_P1_C2[my_id].comandi_automatici.argom25)

/* C2_Enumerat4 L_P1__GetCAArgom26(instance_id_t const my_id); */
#define L_P1__GetCAArgom26(my_id)  (lds_Stazione_data->L_P1_C2[my_id].comandi_automatici.argom26)

/* void L_P1__SetCAEvent2(instance_id_t const my_id, bool const value); */
#define L_P1__SetCAEvent2(my_id, value)   lds_Stazione_data->L_P1_C2[my_id].comandi_automatici.event2 = (value)

/* void L_P1__SetCAEvent3(instance_id_t const my_id, bool const value); */
#define L_P1__SetCAEvent3(my_id, value)   lds_Stazione_data->L_P1_C2[my_id].comandi_automatici.event3 = (value)

/* void L_P1__SetCAEvent4(instance_id_t const my_id, bool const value); */
#define L_P1__SetCAEvent4(my_id, value)   lds_Stazione_data->L_P1_C2[my_id].comandi_automatici.event4 = (value)

/* void L_P1__SetCAArgom23(instance_id_t const my_id, C2_Enumerat1 const value); */
#define L_P1__SetCAArgom23(my_id, value)  lds_Stazione_data->L_P1_C2[my_id].comandi_automatici.argom23 = (value)

/* void L_P1__SetCAArgom24(instance_id_t const my_id, bool const value); */
#define L_P1__SetCAArgom24(my_id, value)  lds_Stazione_data->L_P1_C2[my_id].comandi_automatici.argom24 = (value)

/* void L_P1__SetCAArgom25(instance_id_t const my_id, C2_Enumerat1 const value); */
#define L_P1__SetCAArgom25(my_id, value)  lds_Stazione_data->L_P1_C2[my_id].comandi_automatici.argom25 = (value)

/* void L_P1__SetCAArgom26(instance_id_t const my_id, C2_Enumerat4 const value); */
#define L_P1__SetCAArgom26(my_id, value)  lds_Stazione_data->L_P1_C2[my_id].comandi_automatici.argom26 = (value)



// response
ExecResponse L_P1_C2_GetResponse(instance_id_t const my_id);
void L_P1_C2_SetResponse(instance_id_t const my_id, ExecResponse const value);


#endif // LIBSTAZIONE_CLASSEL_P1_C2_PRIV_H
