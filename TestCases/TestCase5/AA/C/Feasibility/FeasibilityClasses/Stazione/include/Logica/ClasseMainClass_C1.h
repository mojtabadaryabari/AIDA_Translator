#ifndef FEA_LIBSTAZIONE_CLASSEL_P1_C1_H
#define FEA_LIBSTAZIONE_CLASSEL_P1_C1_H

#include "envdt.h"
#include "Timer.h"
#include "Counter.h"


// ********** Comandi manuali e relative risposte **********

typedef struct {
    bool event1;
    bool event2;
    bool event3;
    bool event4;
} L_P1_C1_Comandi_Man;

typedef struct {
    ManCmdResponse event5;
    ManCmdResponse event6;
    ManCmdResponse event7;
    ManCmdResponse event8;
} L_P1_C1_Ack_Comandi_Man;

#define L_P1_C1_NUM_COMANDI_MAN 4


// ********** Informazioni per AGGM **********

#define CLASS_L_P1_C1_ID  1

#define L_P1_C1_State_ID  (1)

// ID Variabili
#define L_P1__mainc33_ID  (33)
#define L_P1__mainc34_ID  (34)

// ID Timer
#define L_P1__mainc43_ID  (44)

// ID Counter
#define L_P1__mainc44_ID  (45)

// ID Controlli dal piazzale
#define L_P1__consd_ID  (2)
#define L_P1__mainc4_ID  (7)

// ID Comandi al piazzale

// ID Comandi manuali
#define L_P1__event1_ID  (46)
#define L_P1__event2_ID  (48)
#define L_P1__event3_ID  (50)
#define L_P1__event4_ID  (52)

// ID Risposte ai comandi manuali
#define L_P1__event5Reply_ID  (47)
#define L_P1__event6Reply_ID  (49)
#define L_P1__event7Reply_ID  (51)
#define L_P1__event8Reply_ID  (53)


// ********** Getter pubblici **********

/* C1_Stateenu L_P1_C1_GetState(instance_id_t const my_id) */
#define L_P1_C1_GetState(my_id)  \
    (C1_Stateenu) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1_C1_State_ID)

// variabili
/* Intero L_P1__GetMainc33(instance_id_t const my_id); */
#define L_P1__GetMainc33(my_id)  \
    (Intero) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc33_ID)

/* Intero L_P1__GetMainc34(instance_id_t const my_id); */
#define L_P1__GetMainc34(my_id)  \
    (Intero) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc34_ID)


// timer
Timer* L_P1__GetMainc43(instance_id_t const my_id);

// counter
Counter* L_P1__GetMainc44(instance_id_t const my_id);    

// controlli dal piazzale
/* bool L_P1__GetInConsd(instance_id_t const my_id); */
#define L_P1__GetInConsd(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__consd_ID)
/* C1_Enumerat1 L_P1__GetInMainc4(instance_id_t const my_id); */
#define L_P1__GetInMainc4(my_id)  \
    (C1_Enumerat1) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc4_ID)

// ********** Altri metodi pubblici**********
// Macro di verifica

// Macro valorizzate

int L_P1_C1_getFeasibility(instance_id_t const my_id, int cmd_id);



#endif // LIBSTAZIONE_CLASSEL_P1_C1_H
