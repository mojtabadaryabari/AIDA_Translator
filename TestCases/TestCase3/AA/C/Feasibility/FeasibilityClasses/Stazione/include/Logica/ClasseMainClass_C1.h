#ifndef FEA_LIBSTAZIONE_CLASSEL_P1_C1_H
#define FEA_LIBSTAZIONE_CLASSEL_P1_C1_H

#include "envdt.h"
#include "Timer.h"
#include "Counter.h"


// ********** Comandi manuali e relative risposte **********

typedef struct {
    bool event;
} L_P1_C1_Comandi_Man;

typedef struct {
    ManCmdResponse event3;
} L_P1_C1_Ack_Comandi_Man;

#define L_P1_C1_NUM_COMANDI_MAN 1


// ********** Informazioni per AGGM **********

#define CLASS_L_P1_C1_ID  1

#define L_P1_C1_State_ID  (1)

// ID Variabili
#define L_P1__mainc37_ID  (35)
#define L_P1__mainc40_ID  (38)
#define L_P1__mainc41_ID  (39)

// ID Timer
#define L_P1__mainc50_ID  (49)
#define L_P1__mainc51_ID  (50)

// ID Counter
#define L_P1__mainc52_ID  (51)

// ID Controlli dal piazzale
#define L_P1__consd_ID  (2)
#define L_P1__mainc5_ID  (8)
#define L_P1__mainc7_ID  (10)

// ID Comandi al piazzale

// ID Comandi manuali
#define L_P1__event_ID  (52)

// ID Risposte ai comandi manuali
#define L_P1__event3Reply_ID  (53)


// ********** Getter pubblici **********

/* C1_Stateenu L_P1_C1_GetState(instance_id_t const my_id) */
#define L_P1_C1_GetState(my_id)  \
    (C1_Stateenu) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1_C1_State_ID)

// variabili
/* C1_Enumerat1 L_P1__GetMainc37(instance_id_t const my_id); */
#define L_P1__GetMainc37(my_id)  \
    (C1_Enumerat1) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc37_ID)

/* C1_Enumerat1 L_P1__GetMainc40(instance_id_t const my_id); */
#define L_P1__GetMainc40(my_id)  \
    (C1_Enumerat1) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc40_ID)

/* C1_Enumerat4 L_P1__GetMainc41(instance_id_t const my_id); */
#define L_P1__GetMainc41(my_id)  \
    (C1_Enumerat4) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc41_ID)


// timer
Timer* L_P1__GetMainc50(instance_id_t const my_id);
Timer* L_P1__GetMainc51(instance_id_t const my_id);

// counter
Counter* L_P1__GetMainc52(instance_id_t const my_id);    

// controlli dal piazzale
/* bool L_P1__GetInConsd(instance_id_t const my_id); */
#define L_P1__GetInConsd(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__consd_ID)
/* bool L_P1__GetInMainc5(instance_id_t const my_id); */
#define L_P1__GetInMainc5(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc5_ID)
/* C1_Enumerat1 L_P1__GetInMainc7(instance_id_t const my_id); */
#define L_P1__GetInMainc7(my_id)  \
    (C1_Enumerat1) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc7_ID)

// ********** Altri metodi pubblici**********
// Macro di verifica

// Macro valorizzate

int L_P1_C1_getFeasibility(instance_id_t const my_id, int cmd_id);



#endif // LIBSTAZIONE_CLASSEL_P1_C1_H
