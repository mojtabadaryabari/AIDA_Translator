// Codice del modello 'TestCase7', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#ifndef LIBSTAZIONE_CLASSEL_P1_C2_PRIV_H
#define LIBSTAZIONE_CLASSEL_P1_C2_PRIV_H

#include "Logica/ClasseSubClass_C2.h"
#include "lds_param.h"


// ********** Comandi automatici **********

typedef struct {
    bool event7;
    bool event8;
} L_P1_C2_Comandi_Auto;

#define L_P1_C2_NUM_COMANDI_AUTO 2


// ********** Struct **********

typedef struct Classe_L_P1_C2 {

    // dati dinamici invisibili
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
Intero L_P1__GetParamSubcl10(instance_id_t const my_id);
bool L_P1__GetParamSubcl11(instance_id_t const my_id);
C2_Enumerat2 L_P1__GetParamSubcl12(instance_id_t const my_id);
Intero L_P1__GetParamSubcl13(instance_id_t const my_id);

offset_t L_P1__GetParamSubcl5Start(instance_id_t const my_id);
index_t L_P1__GetParamSubcl5Length(instance_id_t const my_id);
offset_t L_P1__GetParamSubcl6Start(instance_id_t const my_id);
index_t L_P1__GetParamSubcl6Length(instance_id_t const my_id);
offset_t L_P1__GetParamSubcl7Start(instance_id_t const my_id);
index_t L_P1__GetParamSubcl7Length(instance_id_t const my_id);
offset_t L_P1__GetParamSubcl8Start(instance_id_t const my_id);
index_t L_P1__GetParamSubcl8Length(instance_id_t const my_id);
offset_t L_P1__GetParamSubcl9Start(instance_id_t const my_id);
index_t L_P1__GetParamSubcl9Length(instance_id_t const my_id);

// record
L_P1__Recor L_P1__GetRecSubcl5(instance_id_t const my_id, index_t const elem_idx);

L_P1__Recor1 L_P1__GetRecSubcl6(instance_id_t const my_id, index_t const elem_idx);

L_P1__Recor1 L_P1__GetRecSubcl7(instance_id_t const my_id, index_t const elem_idx);

L_P1__Recor L_P1__GetRecSubcl8(instance_id_t const my_id, index_t const elem_idx);

L_P1__Recor L_P1__GetRecSubcl9(instance_id_t const my_id, index_t const elem_idx);


// comandi automatici
/* bool L_P1__GetCAEvent7(instance_id_t const my_id); */
#define L_P1__GetCAEvent7(my_id) (lds_Stazione_data->L_P1_C2[my_id].comandi_automatici.event7)

/* bool L_P1__GetCAEvent8(instance_id_t const my_id); */
#define L_P1__GetCAEvent8(my_id) (lds_Stazione_data->L_P1_C2[my_id].comandi_automatici.event8)

/* void L_P1__SetCAEvent7(instance_id_t const my_id, bool const value); */
#define L_P1__SetCAEvent7(my_id, value)   lds_Stazione_data->L_P1_C2[my_id].comandi_automatici.event7 = (value)

/* void L_P1__SetCAEvent8(instance_id_t const my_id, bool const value); */
#define L_P1__SetCAEvent8(my_id, value)   lds_Stazione_data->L_P1_C2[my_id].comandi_automatici.event8 = (value)



// response
ExecResponse L_P1_C2_GetResponse(instance_id_t const my_id);
void L_P1_C2_SetResponse(instance_id_t const my_id, ExecResponse const value);


#endif // LIBSTAZIONE_CLASSEL_P1_C2_PRIV_H
