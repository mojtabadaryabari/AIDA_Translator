// Codice del modello 'TestCase1', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#ifndef LIBSTAZIONE_CLASSEL_P1_C2_PRIV_H
#define LIBSTAZIONE_CLASSEL_P1_C2_PRIV_H

#include "Logica/ClasseSubClass_C2.h"
#include "lds_param.h"


// ********** Comandi automatici **********

typedef struct {
    bool event5;
    bool argom16;
    C2_Enumerat2 argom17;
    C2_Enumerat1 argom18;
    C2_Enumerat4 argom19;
} L_P1_C2_Comandi_Auto;

#define L_P1_C2_NUM_COMANDI_AUTO 1


// ********** Struct **********

typedef struct Classe_L_P1_C2 {

    // dati dinamici invisibili
    Timer subcl30;
    Timer subcl31;
    Timer subcl32;
    Timer subcl33;
    Timer subcl34;
    Timer subcl35;
    Timer subcl36;
    Timer subcl37;
    Timer subcl38;
    Timer subcl39;
    Timer subcl40;
    Timer subcl41;
    Timer subcl42;
    Counter subcl43;
    Counter subcl44;
    Counter subcl45;
    Counter subcl46;
    L_P1_C2_Comandi_Auto comandi_automatici;
    ExecResponse response;
} Classe_L_P1_C2;


// ********** Getter/setter privati **********

// parametri
Intero L_P1__GetParamSubcl8(instance_id_t const my_id);
Intero L_P1__GetParamSubcl9(instance_id_t const my_id);

offset_t L_P1__GetParamSubcl4Start(instance_id_t const my_id);
index_t L_P1__GetParamSubcl4Length(instance_id_t const my_id);
offset_t L_P1__GetParamSubcl5Start(instance_id_t const my_id);
index_t L_P1__GetParamSubcl5Length(instance_id_t const my_id);
offset_t L_P1__GetParamSubcl6Start(instance_id_t const my_id);
index_t L_P1__GetParamSubcl6Length(instance_id_t const my_id);
offset_t L_P1__GetParamSubcl7Start(instance_id_t const my_id);
index_t L_P1__GetParamSubcl7Length(instance_id_t const my_id);

// record
L_P1__Recor L_P1__GetRecSubcl4(instance_id_t const my_id, index_t const elem_idx);

L_P1__Recor1 L_P1__GetRecSubcl5(instance_id_t const my_id, index_t const elem_idx);

L_P1__Recor L_P1__GetRecSubcl6(instance_id_t const my_id, index_t const elem_idx);

L_P1__Recor L_P1__GetRecSubcl7(instance_id_t const my_id, index_t const elem_idx);


// comandi automatici
/* bool L_P1__GetCAEvent5(instance_id_t const my_id); */
#define L_P1__GetCAEvent5(my_id) (lds_Stazione_data->L_P1_C2[my_id].comandi_automatici.event5)

/* bool L_P1__GetCAArgom16(instance_id_t const my_id); */
#define L_P1__GetCAArgom16(my_id)  (lds_Stazione_data->L_P1_C2[my_id].comandi_automatici.argom16)

/* C2_Enumerat2 L_P1__GetCAArgom17(instance_id_t const my_id); */
#define L_P1__GetCAArgom17(my_id)  (lds_Stazione_data->L_P1_C2[my_id].comandi_automatici.argom17)

/* C2_Enumerat1 L_P1__GetCAArgom18(instance_id_t const my_id); */
#define L_P1__GetCAArgom18(my_id)  (lds_Stazione_data->L_P1_C2[my_id].comandi_automatici.argom18)

/* C2_Enumerat4 L_P1__GetCAArgom19(instance_id_t const my_id); */
#define L_P1__GetCAArgom19(my_id)  (lds_Stazione_data->L_P1_C2[my_id].comandi_automatici.argom19)

/* void L_P1__SetCAEvent5(instance_id_t const my_id, bool const value); */
#define L_P1__SetCAEvent5(my_id, value)   lds_Stazione_data->L_P1_C2[my_id].comandi_automatici.event5 = (value)

/* void L_P1__SetCAArgom16(instance_id_t const my_id, bool const value); */
#define L_P1__SetCAArgom16(my_id, value)  lds_Stazione_data->L_P1_C2[my_id].comandi_automatici.argom16 = (value)

/* void L_P1__SetCAArgom17(instance_id_t const my_id, C2_Enumerat2 const value); */
#define L_P1__SetCAArgom17(my_id, value)  lds_Stazione_data->L_P1_C2[my_id].comandi_automatici.argom17 = (value)

/* void L_P1__SetCAArgom18(instance_id_t const my_id, C2_Enumerat1 const value); */
#define L_P1__SetCAArgom18(my_id, value)  lds_Stazione_data->L_P1_C2[my_id].comandi_automatici.argom18 = (value)

/* void L_P1__SetCAArgom19(instance_id_t const my_id, C2_Enumerat4 const value); */
#define L_P1__SetCAArgom19(my_id, value)  lds_Stazione_data->L_P1_C2[my_id].comandi_automatici.argom19 = (value)



// response
ExecResponse L_P1_C2_GetResponse(instance_id_t const my_id);
void L_P1_C2_SetResponse(instance_id_t const my_id, ExecResponse const value);


#endif // LIBSTAZIONE_CLASSEL_P1_C2_PRIV_H
