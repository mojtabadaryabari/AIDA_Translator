#ifndef LIBSTAZIONE_CLASSEL_P1_C1_H
#define LIBSTAZIONE_CLASSEL_P1_C1_H

#include "envdt.h"
#include "Timer.h"
#include "Counter.h"


// ********** Comandi manuali e relative risposte **********

typedef struct {
    bool event;
    bool event1;
    bool event3;
} L_P1_C1_Comandi_Man;

typedef struct {
    ManCmdResponse event4;
    ManCmdResponse event5;
    ManCmdResponse event6;
} L_P1_C1_Ack_Comandi_Man;

#define L_P1_C1_NUM_COMANDI_MAN 3


// ********** Informazioni per AGGM **********

#define CLASS_L_P1_C1_ID  1

#define L_P1_C1_State_ID  (1)

// ID Variabili
#define L_P1__lds_m10_ID  (9)
#define L_P1__lds_m11_ID  (10)
#define L_P1__stato1_ID  (12)

// ID Timer
#define L_P1__lds_m12_ID  (13)
#define L_P1__lds_m13_ID  (14)
#define L_P1__lds_m14_ID  (15)
#define L_P1__lds_m15_ID  (16)

// ID Counter
#define L_P1__lds_m16_ID  (17)
#define L_P1__lds_m17_ID  (18)
#define L_P1__lds_m18_ID  (19)
#define L_P1__lds_m19_ID  (20)

// ID Controlli dal piazzale
#define L_P1__lds_m3_ID  (5)
#define L_P1__lds_m4_ID  (6)
#define L_P1__lds_m5_ID  (7)
#define L_P1__lds_m6_ID  (8)

// ID Comandi al piazzale
#define L_P1__lds_m_ID  (2)
#define L_P1__lds_m1_ID  (3)
#define L_P1__lds_m2_ID  (4)
#define L_P1__nabcc_ID  (11)

// ID Comandi manuali
#define L_P1__event_ID  (21)
#define L_P1__event1_ID  (23)
#define L_P1__event3_ID  (25)

// ID Risposte ai comandi manuali
#define L_P1__event4Reply_ID  (22)
#define L_P1__event5Reply_ID  (24)
#define L_P1__event6Reply_ID  (26)


// ********** Getter/setter pubblici **********

/* C1_Stateenu L_P1_C1_GetState(instance_id_t const my_id) */
#define L_P1_C1_GetState(my_id)  \
    (C1_Stateenu) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1_C1_State_ID)

/* void L_P1_C1_SetState(instance_id_t const my_id, C1_Stateenu const value) */
#define L_P1_C1_SetState(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1_C1_State_ID, (Taggm) (value))

// variabili
/* C1_Enumerat2 L_P1__GetLds_m10(instance_id_t const my_id); */
#define L_P1__GetLds_m10(my_id)  \
    (C1_Enumerat2) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__lds_m10_ID)
/* void L_P1__SetLds_m10(instance_id_t const my_id, C1_Enumerat2 const value); */
#define L_P1__SetLds_m10(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__lds_m10_ID, (Taggm) (value))

/* C1_Enumerat3 L_P1__GetLds_m11(instance_id_t const my_id); */
#define L_P1__GetLds_m11(my_id)  \
    (C1_Enumerat3) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__lds_m11_ID)
/* void L_P1__SetLds_m11(instance_id_t const my_id, C1_Enumerat3 const value); */
#define L_P1__SetLds_m11(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__lds_m11_ID, (Taggm) (value))

/* C1_Stateenu L_P1__GetStato1(instance_id_t const my_id); */
#define L_P1__GetStato1(my_id)  \
    (C1_Stateenu) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__stato1_ID)
/* void L_P1__SetStato1(instance_id_t const my_id, C1_Stateenu const value); */
#define L_P1__SetStato1(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__stato1_ID, (Taggm) (value))


// timer
Timer* L_P1__GetLds_m12(instance_id_t const my_id);
Timer* L_P1__GetLds_m13(instance_id_t const my_id);
Timer* L_P1__GetLds_m14(instance_id_t const my_id);
Timer* L_P1__GetLds_m15(instance_id_t const my_id);

// counter
Counter* L_P1__GetLds_m16(instance_id_t const my_id);    
Counter* L_P1__GetLds_m17(instance_id_t const my_id);    
Counter* L_P1__GetLds_m18(instance_id_t const my_id);    
Counter* L_P1__GetLds_m19(instance_id_t const my_id);    

// comandi manuali
/* bool L_P1__GetInEvent(instance_id_t const my_id); */
#define L_P1__GetInEvent(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__event_ID)
/* bool L_P1__GetInEvent1(instance_id_t const my_id); */
#define L_P1__GetInEvent1(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__event1_ID)
/* bool L_P1__GetInEvent3(instance_id_t const my_id); */
#define L_P1__GetInEvent3(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__event3_ID)

// risposte ai comandi manuali
/* void L_P1__SetOutEvent4(instance_id_t const my_id, ManCmdResponse const value); */
#define L_P1__SetOutEvent4(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__event4Reply_ID, (Taggm) (value))
/* void L_P1__SetOutEvent5(instance_id_t const my_id, ManCmdResponse const value); */
#define L_P1__SetOutEvent5(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__event5Reply_ID, (Taggm) (value))
/* void L_P1__SetOutEvent6(instance_id_t const my_id, ManCmdResponse const value); */
#define L_P1__SetOutEvent6(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__event6Reply_ID, (Taggm) (value))

// controlli dal piazzale
/* C1_Enumerat3 L_P1__GetInLds_m3(instance_id_t const my_id); */
#define L_P1__GetInLds_m3(my_id)  \
    (C1_Enumerat3) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__lds_m3_ID)
/* bool L_P1__GetInLds_m4(instance_id_t const my_id); */
#define L_P1__GetInLds_m4(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__lds_m4_ID)
/* C1_Enumerat2 L_P1__GetInLds_m5(instance_id_t const my_id); */
#define L_P1__GetInLds_m5(my_id)  \
    (C1_Enumerat2) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__lds_m5_ID)
/* bool L_P1__GetInLds_m6(instance_id_t const my_id); */
#define L_P1__GetInLds_m6(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__lds_m6_ID)

// comandi al piazzale
/* void L_P1__SetOutLds_m(instance_id_t const my_id, bool const value); */
#define L_P1__SetOutLds_m(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__lds_m_ID, (Taggm) (value))

/* void L_P1__SetOutLds_m1(instance_id_t const my_id, C1_Enumerat4 const value); */
#define L_P1__SetOutLds_m1(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__lds_m1_ID, (Taggm) (value))

/* void L_P1__SetOutLds_m2(instance_id_t const my_id, bool const value); */
#define L_P1__SetOutLds_m2(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__lds_m2_ID, (Taggm) (value))

/* void L_P1__SetOutNabcc(instance_id_t const my_id, C1_Enumerat4 const value); */
#define L_P1__SetOutNabcc(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__nabcc_ID, (Taggm) (value))


// ********** Metodi standard **********

void L_P1_C1_Init(instance_id_t const my_id);

void L_P1_C1_Exec(instance_id_t const my_id, Phase const p);

ExecResponse L_P1_C1_GExec(global_id_t const proc_id, Phase const p);

void L_P1_C1_GTick(global_id_t const proc_id);

void L_P1_C1_GSetSafe(global_id_t const proc_id);


// ********** Altri metodi pubblici**********

// Macro di effetto
void L_P1__Macro(instance_id_t const my_id );

// Macro di verifica
bool L_P1__Macro2(instance_id_t const my_id );
bool L_P1__Macro3(instance_id_t const my_id , bool argom2, C1_Enumerat4 argom3, C1_Enumerat1 argom4, bool argom5, C1_Enumerat4 argom6, C1_Enumerat2 argom7);
bool L_P1__Macro4(instance_id_t const my_id );
bool L_P1__Macro5(instance_id_t const my_id );

// Macro valorizzate
C1_Enumerat1 L_P1__Macro1(instance_id_t const my_id , bool argom, C1_Enumerat4 argom1);


#endif // LIBSTAZIONE_CLASSEL_P1_C1_H
