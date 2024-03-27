#ifndef FEA_LIBSTAZIONE_CLASSEL_P1_C2_H
#define FEA_LIBSTAZIONE_CLASSEL_P1_C2_H

#include "envdt.h"
#include "Timer.h"
#include "Counter.h"


// ********** Comandi manuali e relative risposte **********

typedef struct {
    bool event6;
} L_P1_C2_Comandi_Man;

typedef struct {
    ManCmdResponse event7;
} L_P1_C2_Ack_Comandi_Man;

#define L_P1_C2_NUM_COMANDI_MAN 1


// ********** Informazioni per AGGM **********

#define CLASS_L_P1_C2_ID  2

#define L_P1_C2_State_ID  (1)

// ID Variabili
#define L_P1__subcl27_ID  (29)
#define L_P1__subcl28_ID  (30)

// ID Timer
#define L_P1__subcl31_ID  (33)
#define L_P1__subcl32_ID  (34)
#define L_P1__subcl33_ID  (35)
#define L_P1__subcl34_ID  (36)
#define L_P1__subcl35_ID  (37)

// ID Counter
#define L_P1__subcl36_ID  (38)

// ID Controlli dal piazzale
#define L_P1__consd1_ID  (2)
#define L_P1__subcl5_ID  (9)
#define L_P1__subcl6_ID  (10)

// ID Comandi al piazzale

// ID Comandi manuali
#define L_P1__event6_ID  (39)

// ID Risposte ai comandi manuali
#define L_P1__event7Reply_ID  (40)


// ********** Getter pubblici **********

/* C2_Stateenu L_P1_C2_GetState(instance_id_t const my_id) */
#define L_P1_C2_GetState(my_id)  \
    (C2_Stateenu) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1_C2_State_ID)

// variabili
/* bool L_P1__GetSubcl27(instance_id_t const my_id); */
#define L_P1__GetSubcl27(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl27_ID)

/* bool L_P1__GetSubcl28(instance_id_t const my_id); */
#define L_P1__GetSubcl28(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl28_ID)


// timer
Timer* L_P1__GetSubcl31(instance_id_t const my_id);
Timer* L_P1__GetSubcl32(instance_id_t const my_id);
Timer* L_P1__GetSubcl33(instance_id_t const my_id);
Timer* L_P1__GetSubcl34(instance_id_t const my_id);
Timer* L_P1__GetSubcl35(instance_id_t const my_id);

// counter
Counter* L_P1__GetSubcl36(instance_id_t const my_id);    

// controlli dal piazzale
/* bool L_P1__GetInConsd1(instance_id_t const my_id); */
#define L_P1__GetInConsd1(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__consd1_ID)
/* bool L_P1__GetInSubcl5(instance_id_t const my_id); */
#define L_P1__GetInSubcl5(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl5_ID)
/* C2_Enumerat3 L_P1__GetInSubcl6(instance_id_t const my_id); */
#define L_P1__GetInSubcl6(my_id)  \
    (C2_Enumerat3) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl6_ID)

// ********** Altri metodi pubblici**********
// Macro di verifica

// Macro valorizzate

int L_P1_C2_getFeasibility(instance_id_t const my_id, int cmd_id);



#endif // LIBSTAZIONE_CLASSEL_P1_C2_H
