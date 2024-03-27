#ifndef FEA_LIBSTAZIONE_CLASSEL_P1_C4_H
#define FEA_LIBSTAZIONE_CLASSEL_P1_C4_H

#include "envdt.h"
#include "Timer.h"
#include "Counter.h"


// ********** Comandi manuali e relative risposte **********



#define L_P1_C4_NUM_COMANDI_MAN 0


// ********** Informazioni per AGGM **********

#define CLASS_L_P1_C4_ID  4

#define L_P1_C4_State_ID  (1)

// ID Variabili

// ID Timer

// ID Counter

// ID Controlli dal piazzale

// ID Comandi al piazzale

// ID Comandi manuali

// ID Risposte ai comandi manuali


// ********** Getter pubblici **********

/* C4_Stateenu L_P1_C4_GetState(instance_id_t const my_id) */
#define L_P1_C4_GetState(my_id)  \
    (C4_Stateenu) \
    LogicGetAggmVar(CLASS_L_P1_C4_ID, (my_id), L_P1_C4_State_ID)

// variabili

// timer

// counter

// controlli dal piazzale

// ********** Altri metodi pubblici**********
// Macro di verifica

// Macro valorizzate

int L_P1_C4_getFeasibility(instance_id_t const my_id, int cmd_id);



#endif // LIBSTAZIONE_CLASSEL_P1_C4_H
