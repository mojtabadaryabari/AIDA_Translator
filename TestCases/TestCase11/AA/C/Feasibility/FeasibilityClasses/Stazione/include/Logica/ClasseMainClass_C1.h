#ifndef FEA_LIBSTAZIONE_CLASSEL_P1_C1_H
#define FEA_LIBSTAZIONE_CLASSEL_P1_C1_H

#include "envdt.h"
#include "Timer.h"
#include "Counter.h"


// ********** Comandi manuali e relative risposte **********

typedef struct {
    bool event;
    bool event1;
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

// ID Timer

// ID Counter

// ID Controlli dal piazzale

// ID Comandi al piazzale

// ID Comandi manuali
#define L_P1__event_ID  (46)
#define L_P1__event1_ID  (48)
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

// timer

// counter

// controlli dal piazzale

// ********** Altri metodi pubblici**********
// Macro di verifica

// Macro valorizzate

int L_P1_C1_getFeasibility(instance_id_t const my_id, int cmd_id);



#endif // LIBSTAZIONE_CLASSEL_P1_C1_H
