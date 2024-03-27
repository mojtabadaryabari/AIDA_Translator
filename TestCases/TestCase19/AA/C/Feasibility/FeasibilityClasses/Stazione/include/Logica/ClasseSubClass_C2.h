#ifndef FEA_LIBSTAZIONE_CLASSEL_P1_C2_H
#define FEA_LIBSTAZIONE_CLASSEL_P1_C2_H

#include "envdt.h"
#include "Timer.h"
#include "Counter.h"


// ********** Comandi manuali e relative risposte **********

typedef struct {
    bool event1;
    bool event2;
    bool event3;
} L_P1_C2_Comandi_Man;

typedef struct {
    ManCmdResponse event5;
    ManCmdResponse event6;
    ManCmdResponse event7;
} L_P1_C2_Ack_Comandi_Man;

#define L_P1_C2_NUM_COMANDI_MAN 3


// ********** Informazioni per AGGM **********

#define CLASS_L_P1_C2_ID  2

#define L_P1_C2_State_ID  (1)

// ID Variabili
#define L_P1__subcl36_ID  (33)

// ID Timer
#define L_P1__subcl45_ID  (42)
#define L_P1__subcl47_ID  (44)
#define L_P1__subcl48_ID  (45)
#define L_P1__subcl49_ID  (46)

// ID Counter
#define L_P1__subcl50_ID  (47)
#define L_P1__subcl52_ID  (49)

// ID Controlli dal piazzale
#define L_P1__consd1_ID  (2)
#define L_P1__subcl2_ID  (6)
#define L_P1__subcl4_ID  (8)

// ID Comandi al piazzale

// ID Comandi manuali
#define L_P1__event1_ID  (50)
#define L_P1__event2_ID  (52)
#define L_P1__event3_ID  (54)

// ID Risposte ai comandi manuali
#define L_P1__event5Reply_ID  (51)
#define L_P1__event6Reply_ID  (53)
#define L_P1__event7Reply_ID  (55)


// ********** Getter pubblici **********

/* C2_Stateenu L_P1_C2_GetState(instance_id_t const my_id) */
#define L_P1_C2_GetState(my_id)  \
    (C2_Stateenu) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1_C2_State_ID)

// variabili
/* C2_Enumerat4 L_P1__GetSubcl36(instance_id_t const my_id); */
#define L_P1__GetSubcl36(my_id)  \
    (C2_Enumerat4) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl36_ID)


// timer
Timer* L_P1__GetSubcl45(instance_id_t const my_id);
Timer* L_P1__GetSubcl47(instance_id_t const my_id);
Timer* L_P1__GetSubcl48(instance_id_t const my_id);
Timer* L_P1__GetSubcl49(instance_id_t const my_id);

// counter
Counter* L_P1__GetSubcl50(instance_id_t const my_id);    
Counter* L_P1__GetSubcl52(instance_id_t const my_id);    

// controlli dal piazzale
/* bool L_P1__GetInConsd1(instance_id_t const my_id); */
#define L_P1__GetInConsd1(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__consd1_ID)
/* C2_Enumerat3 L_P1__GetInSubcl2(instance_id_t const my_id); */
#define L_P1__GetInSubcl2(my_id)  \
    (C2_Enumerat3) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl2_ID)
/* bool L_P1__GetInSubcl4(instance_id_t const my_id); */
#define L_P1__GetInSubcl4(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl4_ID)

// ********** Altri metodi pubblici**********
// Macro di verifica

// Macro valorizzate

int L_P1_C2_getFeasibility(instance_id_t const my_id, int cmd_id);



#endif // LIBSTAZIONE_CLASSEL_P1_C2_H
