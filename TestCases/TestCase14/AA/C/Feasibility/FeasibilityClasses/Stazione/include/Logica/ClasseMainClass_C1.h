#ifndef FEA_LIBSTAZIONE_CLASSEL_P1_C1_H
#define FEA_LIBSTAZIONE_CLASSEL_P1_C1_H

#include "envdt.h"
#include "Timer.h"
#include "Counter.h"


// ********** Comandi manuali e relative risposte **********

typedef struct {
    bool event;
    bool event1;
} L_P1_C1_Comandi_Man;

typedef struct {
    ManCmdResponse event3;
    ManCmdResponse event4;
} L_P1_C1_Ack_Comandi_Man;

#define L_P1_C1_NUM_COMANDI_MAN 2


// ********** Informazioni per AGGM **********

#define CLASS_L_P1_C1_ID  1

#define L_P1_C1_State_ID  (1)

// ID Variabili
#define L_P1__mainc34_ID  (35)

// ID Timer

// ID Counter

// ID Controlli dal piazzale

// ID Comandi al piazzale

// ID Comandi manuali
#define L_P1__event_ID  (51)
#define L_P1__event1_ID  (53)

// ID Risposte ai comandi manuali
#define L_P1__event3Reply_ID  (52)
#define L_P1__event4Reply_ID  (54)


// ********** Getter pubblici **********

/* C1_Stateenu L_P1_C1_GetState(instance_id_t const my_id) */
#define L_P1_C1_GetState(my_id)  \
    (C1_Stateenu) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1_C1_State_ID)

// variabili
/* C1_Enumerat4 L_P1__GetMainc34(instance_id_t const my_id); */
#define L_P1__GetMainc34(my_id)  \
    (C1_Enumerat4) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc34_ID)


// timer

// counter

// controlli dal piazzale

// ********** Altri metodi pubblici**********
// Macro di verifica

// Macro valorizzate

int L_P1_C1_getFeasibility(instance_id_t const my_id, int cmd_id);



#endif // LIBSTAZIONE_CLASSEL_P1_C1_H
