// Codice del modello 'TestCase24', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#ifndef LIBSTAZIONE_CLASSEL_P1_C2_PRIV_H
#define LIBSTAZIONE_CLASSEL_P1_C2_PRIV_H

#include "Logica/ClasseSubClass_C2.h"
#include "lds_param.h"


// ********** Comandi automatici **********

typedef struct {
    bool event7;
    C2_Enumerat4 argom28;
    bool argom29;
} L_P1_C2_Comandi_Auto;

#define L_P1_C2_NUM_COMANDI_AUTO 1


// ********** Struct **********

typedef struct Classe_L_P1_C2 {

    // dati dinamici invisibili
    Timer subcl35;
    Timer subcl36;
    Timer subcl37;
    Timer subcl38;
    Timer subcl39;
    Timer subcl40;
    Timer subcl41;
    Counter subcl42;
    L_P1_C2_Comandi_Auto comandi_automatici;
    ExecResponse response;
} Classe_L_P1_C2;


// ********** Getter/setter privati **********

// parametri
Intero L_P1__GetParamSubcl14(instance_id_t const my_id);
Intero L_P1__GetParamSubcl15(instance_id_t const my_id);
Intero L_P1__GetParamSubcl16(instance_id_t const my_id);
Intero L_P1__GetParamSubcl17(instance_id_t const my_id);

offset_t L_P1__GetParamSubcl9Start(instance_id_t const my_id);
index_t L_P1__GetParamSubcl9Length(instance_id_t const my_id);
offset_t L_P1__GetParamSubcl10Start(instance_id_t const my_id);
index_t L_P1__GetParamSubcl10Length(instance_id_t const my_id);
offset_t L_P1__GetParamSubcl11Start(instance_id_t const my_id);
index_t L_P1__GetParamSubcl11Length(instance_id_t const my_id);
offset_t L_P1__GetParamSubcl12Start(instance_id_t const my_id);
index_t L_P1__GetParamSubcl12Length(instance_id_t const my_id);
offset_t L_P1__GetParamSubcl13Start(instance_id_t const my_id);
index_t L_P1__GetParamSubcl13Length(instance_id_t const my_id);

// record
L_P1__Recor L_P1__GetRecSubcl9(instance_id_t const my_id, index_t const elem_idx);

L_P1__Recor1 L_P1__GetRecSubcl10(instance_id_t const my_id, index_t const elem_idx);

L_P1__Recor1 L_P1__GetRecSubcl11(instance_id_t const my_id, index_t const elem_idx);

L_P1__Recor1 L_P1__GetRecSubcl12(instance_id_t const my_id, index_t const elem_idx);

L_P1__Recor L_P1__GetRecSubcl13(instance_id_t const my_id, index_t const elem_idx);


// comandi automatici
/* bool L_P1__GetCAEvent7(instance_id_t const my_id); */
#define L_P1__GetCAEvent7(my_id) (lds_Stazione_data->L_P1_C2[my_id].comandi_automatici.event7)

/* C2_Enumerat4 L_P1__GetCAArgom28(instance_id_t const my_id); */
#define L_P1__GetCAArgom28(my_id)  (lds_Stazione_data->L_P1_C2[my_id].comandi_automatici.argom28)

/* bool L_P1__GetCAArgom29(instance_id_t const my_id); */
#define L_P1__GetCAArgom29(my_id)  (lds_Stazione_data->L_P1_C2[my_id].comandi_automatici.argom29)

/* void L_P1__SetCAEvent7(instance_id_t const my_id, bool const value); */
#define L_P1__SetCAEvent7(my_id, value)   lds_Stazione_data->L_P1_C2[my_id].comandi_automatici.event7 = (value)

/* void L_P1__SetCAArgom28(instance_id_t const my_id, C2_Enumerat4 const value); */
#define L_P1__SetCAArgom28(my_id, value)  lds_Stazione_data->L_P1_C2[my_id].comandi_automatici.argom28 = (value)

/* void L_P1__SetCAArgom29(instance_id_t const my_id, bool const value); */
#define L_P1__SetCAArgom29(my_id, value)  lds_Stazione_data->L_P1_C2[my_id].comandi_automatici.argom29 = (value)



// response
ExecResponse L_P1_C2_GetResponse(instance_id_t const my_id);
void L_P1_C2_SetResponse(instance_id_t const my_id, ExecResponse const value);


#endif // LIBSTAZIONE_CLASSEL_P1_C2_PRIV_H
