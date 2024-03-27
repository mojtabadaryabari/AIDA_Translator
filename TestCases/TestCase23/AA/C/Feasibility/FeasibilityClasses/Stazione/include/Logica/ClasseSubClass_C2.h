#ifndef FEA_LIBSTAZIONE_CLASSEL_P1_C2_H
#define FEA_LIBSTAZIONE_CLASSEL_P1_C2_H

#include "envdt.h"
#include "Timer.h"
#include "Counter.h"


// ********** Comandi manuali e relative risposte **********

typedef struct {
    bool event5;
} L_P1_C2_Comandi_Man;

typedef struct {
    ManCmdResponse event9;
} L_P1_C2_Ack_Comandi_Man;

#define L_P1_C2_NUM_COMANDI_MAN 1


// ********** Informazioni per AGGM **********

#define CLASS_L_P1_C2_ID  2

#define L_P1_C2_State_ID  (1)

// ID Variabili

// ID Timer

// ID Counter

// ID Controlli dal piazzale

// ID Comandi al piazzale

// ID Comandi manuali
#define L_P1__event5_ID  (30)

// ID Risposte ai comandi manuali
#define L_P1__event9Reply_ID  (31)


// ********** Getter pubblici **********

/* C2_Stateenu L_P1_C2_GetState(instance_id_t const my_id) */
#define L_P1_C2_GetState(my_id)  \
    (C2_Stateenu) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1_C2_State_ID)

// variabili

// timer

// counter

// controlli dal piazzale

// ********** Altri metodi pubblici**********
// Macro di verifica

// Macro valorizzate

int L_P1_C2_getFeasibility(instance_id_t const my_id, int cmd_id);



#endif // LIBSTAZIONE_CLASSEL_P1_C2_H
