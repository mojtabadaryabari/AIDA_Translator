#ifndef FEA_LIBSTAZIONE_CLASSEL_P1_C3_H
#define FEA_LIBSTAZIONE_CLASSEL_P1_C3_H

#include "envdt.h"
#include "Timer.h"
#include "Counter.h"


// ********** Comandi manuali e relative risposte **********

typedef struct {
    bool event8;
    bool event9;
} L_P1_C3_Comandi_Man;

typedef struct {
    ManCmdResponse event10;
    ManCmdResponse event11;
} L_P1_C3_Ack_Comandi_Man;

#define L_P1_C3_NUM_COMANDI_MAN 2


// ********** Informazioni per AGGM **********

#define CLASS_L_P1_C3_ID  3

#define L_P1_C3_State_ID  (1)

// ID Variabili

// ID Timer

// ID Counter

// ID Controlli dal piazzale

// ID Comandi al piazzale

// ID Comandi manuali
#define L_P1__event8_ID  (58)
#define L_P1__event9_ID  (60)

// ID Risposte ai comandi manuali
#define L_P1__event10Reply_ID  (59)
#define L_P1__event11Reply_ID  (61)


// ********** Getter pubblici **********

/* C3_Stateenu L_P1_C3_GetState(instance_id_t const my_id) */
#define L_P1_C3_GetState(my_id)  \
    (C3_Stateenu) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1_C3_State_ID)

// variabili

// timer

// counter

// controlli dal piazzale

// ********** Altri metodi pubblici**********
// Macro di verifica

// Macro valorizzate

int L_P1_C3_getFeasibility(instance_id_t const my_id, int cmd_id);



#endif // LIBSTAZIONE_CLASSEL_P1_C3_H
