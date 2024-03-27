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
    ManCmdResponse event2;
} L_P1_C1_Ack_Comandi_Man;

#define L_P1_C1_NUM_COMANDI_MAN 1


// ********** Informazioni per AGGM **********

#define CLASS_L_P1_C1_ID  1

#define L_P1_C1_State_ID  (1)

// ID Variabili
#define L_P1__mainc20_ID  (22)
#define L_P1__mainc22_ID  (24)
#define L_P1__mainc23_ID  (25)

// ID Timer
#define L_P1__mainc31_ID  (34)
#define L_P1__mainc32_ID  (35)

// ID Counter
#define L_P1__mainc33_ID  (36)
#define L_P1__mainc34_ID  (37)
#define L_P1__mainc35_ID  (38)

// ID Controlli dal piazzale
#define L_P1__consd_ID  (2)
#define L_P1__mainc1_ID  (4)
#define L_P1__mainc2_ID  (5)
#define L_P1__mainc3_ID  (6)
#define L_P1__mainc4_ID  (7)

// ID Comandi al piazzale

// ID Comandi manuali
#define L_P1__event_ID  (39)

// ID Risposte ai comandi manuali
#define L_P1__event2Reply_ID  (40)


// ********** Getter pubblici **********

/* C1_Stateenu L_P1_C1_GetState(instance_id_t const my_id) */
#define L_P1_C1_GetState(my_id)  \
    (C1_Stateenu) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1_C1_State_ID)

// variabili
/* C1_Enumerat3 L_P1__GetMainc20(instance_id_t const my_id); */
#define L_P1__GetMainc20(my_id)  \
    (C1_Enumerat3) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc20_ID)

/* bool L_P1__GetMainc22(instance_id_t const my_id); */
#define L_P1__GetMainc22(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc22_ID)

/* C1_Enumerat2 L_P1__GetMainc23(instance_id_t const my_id); */
#define L_P1__GetMainc23(my_id)  \
    (C1_Enumerat2) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc23_ID)


// timer
Timer* L_P1__GetMainc31(instance_id_t const my_id);
Timer* L_P1__GetMainc32(instance_id_t const my_id);

// counter
Counter* L_P1__GetMainc33(instance_id_t const my_id);    
Counter* L_P1__GetMainc34(instance_id_t const my_id);    
Counter* L_P1__GetMainc35(instance_id_t const my_id);    

// controlli dal piazzale
/* bool L_P1__GetInConsd(instance_id_t const my_id); */
#define L_P1__GetInConsd(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__consd_ID)
/* C1_Enumerat4 L_P1__GetInMainc1(instance_id_t const my_id); */
#define L_P1__GetInMainc1(my_id)  \
    (C1_Enumerat4) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc1_ID)
/* C1_Enumerat1 L_P1__GetInMainc2(instance_id_t const my_id); */
#define L_P1__GetInMainc2(my_id)  \
    (C1_Enumerat1) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc2_ID)
/* C1_Enumerat4 L_P1__GetInMainc3(instance_id_t const my_id); */
#define L_P1__GetInMainc3(my_id)  \
    (C1_Enumerat4) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc3_ID)
/* C1_Enumerat1 L_P1__GetInMainc4(instance_id_t const my_id); */
#define L_P1__GetInMainc4(my_id)  \
    (C1_Enumerat1) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc4_ID)

// ********** Altri metodi pubblici**********
// Macro di verifica

// Macro valorizzate

int L_P1_C1_getFeasibility(instance_id_t const my_id, int cmd_id);



#endif // LIBSTAZIONE_CLASSEL_P1_C1_H
