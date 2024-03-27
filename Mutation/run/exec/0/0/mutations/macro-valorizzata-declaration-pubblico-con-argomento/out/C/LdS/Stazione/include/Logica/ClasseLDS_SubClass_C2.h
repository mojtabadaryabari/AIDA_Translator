#ifndef LIBSTAZIONE_CLASSEL_P1_C2_H
#define LIBSTAZIONE_CLASSEL_P1_C2_H

#include "envdt.h"
#include "Timer.h"
#include "Counter.h"


// ********** Comandi manuali e relative risposte **********

typedef struct {
    bool event7;
    bool event8;
} L_P1_C2_Comandi_Man;

typedef struct {
    ManCmdResponse event9;
    ManCmdResponse event10;
} L_P1_C2_Ack_Comandi_Man;

#define L_P1_C2_NUM_COMANDI_MAN 2


// ********** Informazioni per AGGM **********

#define CLASS_L_P1_C2_ID  2

#define L_P1_C2_State_ID  (1)

// ID Variabili
#define L_P1__lds_s12_ID  (10)
#define L_P1__lds_s13_ID  (11)
#define L_P1__lds_s14_ID  (12)
#define L_P1__lds_s15_ID  (13)
#define L_P1__lds_s16_ID  (14)
#define L_P1__stato3_ID  (15)

// ID Timer
#define L_P1__lds_s17_ID  (16)

// ID Counter
#define L_P1__lds_s18_ID  (17)
#define L_P1__lds_s19_ID  (18)
#define L_P1__lds_s20_ID  (19)
#define L_P1__lds_s21_ID  (20)
#define L_P1__lds_s22_ID  (21)

// ID Controlli dal piazzale
#define L_P1__lds_s5_ID  (7)
#define L_P1__lds_s6_ID  (8)
#define L_P1__lds_s7_ID  (9)

// ID Comandi al piazzale
#define L_P1__lds_s_ID  (2)
#define L_P1__lds_s1_ID  (3)
#define L_P1__lds_s2_ID  (4)
#define L_P1__lds_s3_ID  (5)
#define L_P1__lds_s4_ID  (6)

// ID Comandi manuali
#define L_P1__event7_ID  (22)
#define L_P1__event8_ID  (24)

// ID Risposte ai comandi manuali
#define L_P1__event9Reply_ID  (23)
#define L_P1__event10Reply_ID  (25)


// ********** Getter/setter pubblici **********

/* C2_Stateenu L_P1_C2_GetState(instance_id_t const my_id) */
#define L_P1_C2_GetState(my_id)  \
    (C2_Stateenu) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1_C2_State_ID)

/* void L_P1_C2_SetState(instance_id_t const my_id, C2_Stateenu const value) */
#define L_P1_C2_SetState(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1_C2_State_ID, (Taggm) (value))

// variabili
/* bool L_P1__GetLds_s12(instance_id_t const my_id); */
#define L_P1__GetLds_s12(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__lds_s12_ID)
/* void L_P1__SetLds_s12(instance_id_t const my_id, bool const value); */
#define L_P1__SetLds_s12(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__lds_s12_ID, (Taggm) (value))

/* C2_Enumerat2 L_P1__GetLds_s13(instance_id_t const my_id); */
#define L_P1__GetLds_s13(my_id)  \
    (C2_Enumerat2) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__lds_s13_ID)
/* void L_P1__SetLds_s13(instance_id_t const my_id, C2_Enumerat2 const value); */
#define L_P1__SetLds_s13(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__lds_s13_ID, (Taggm) (value))

/* C2_Enumerat2 L_P1__GetLds_s14(instance_id_t const my_id); */
#define L_P1__GetLds_s14(my_id)  \
    (C2_Enumerat2) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__lds_s14_ID)
/* void L_P1__SetLds_s14(instance_id_t const my_id, C2_Enumerat2 const value); */
#define L_P1__SetLds_s14(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__lds_s14_ID, (Taggm) (value))

/* Intero L_P1__GetLds_s15(instance_id_t const my_id); */
#define L_P1__GetLds_s15(my_id)  \
    (Intero) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__lds_s15_ID)
/* void L_P1__SetLds_s15(instance_id_t const my_id, Intero const value); */
#define L_P1__SetLds_s15(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__lds_s15_ID, (Taggm) (value))

/* C2_Enumerat3 L_P1__GetLds_s16(instance_id_t const my_id); */
#define L_P1__GetLds_s16(my_id)  \
    (C2_Enumerat3) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__lds_s16_ID)
/* void L_P1__SetLds_s16(instance_id_t const my_id, C2_Enumerat3 const value); */
#define L_P1__SetLds_s16(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__lds_s16_ID, (Taggm) (value))

/* C2_Stateenu L_P1__GetStato3(instance_id_t const my_id); */
#define L_P1__GetStato3(my_id)  \
    (C2_Stateenu) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__stato3_ID)
/* void L_P1__SetStato3(instance_id_t const my_id, C2_Stateenu const value); */
#define L_P1__SetStato3(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__stato3_ID, (Taggm) (value))


// timer
Timer* L_P1__GetLds_s17(instance_id_t const my_id);

// counter
Counter* L_P1__GetLds_s18(instance_id_t const my_id);    
Counter* L_P1__GetLds_s19(instance_id_t const my_id);    
Counter* L_P1__GetLds_s20(instance_id_t const my_id);    
Counter* L_P1__GetLds_s21(instance_id_t const my_id);    
Counter* L_P1__GetLds_s22(instance_id_t const my_id);    

// comandi manuali
/* bool L_P1__GetInEvent7(instance_id_t const my_id); */
#define L_P1__GetInEvent7(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__event7_ID)
/* bool L_P1__GetInEvent8(instance_id_t const my_id); */
#define L_P1__GetInEvent8(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__event8_ID)

// risposte ai comandi manuali
/* void L_P1__SetOutEvent9(instance_id_t const my_id, ManCmdResponse const value); */
#define L_P1__SetOutEvent9(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__event9Reply_ID, (Taggm) (value))
/* void L_P1__SetOutEvent10(instance_id_t const my_id, ManCmdResponse const value); */
#define L_P1__SetOutEvent10(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__event10Reply_ID, (Taggm) (value))

// controlli dal piazzale
/* C2_Enumerat2 L_P1__GetInLds_s5(instance_id_t const my_id); */
#define L_P1__GetInLds_s5(my_id)  \
    (C2_Enumerat2) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__lds_s5_ID)
/* C2_Enumerat3 L_P1__GetInLds_s6(instance_id_t const my_id); */
#define L_P1__GetInLds_s6(my_id)  \
    (C2_Enumerat3) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__lds_s6_ID)
/* C2_Enumerat1 L_P1__GetInLds_s7(instance_id_t const my_id); */
#define L_P1__GetInLds_s7(my_id)  \
    (C2_Enumerat1) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__lds_s7_ID)

// comandi al piazzale
/* void L_P1__SetOutLds_s(instance_id_t const my_id, C2_Enumerat2 const value); */
#define L_P1__SetOutLds_s(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__lds_s_ID, (Taggm) (value))

/* void L_P1__SetOutLds_s1(instance_id_t const my_id, C2_Enumerat4 const value); */
#define L_P1__SetOutLds_s1(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__lds_s1_ID, (Taggm) (value))

/* void L_P1__SetOutLds_s2(instance_id_t const my_id, bool const value); */
#define L_P1__SetOutLds_s2(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__lds_s2_ID, (Taggm) (value))

/* void L_P1__SetOutLds_s3(instance_id_t const my_id, bool const value); */
#define L_P1__SetOutLds_s3(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__lds_s3_ID, (Taggm) (value))

/* void L_P1__SetOutLds_s4(instance_id_t const my_id, bool const value); */
#define L_P1__SetOutLds_s4(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__lds_s4_ID, (Taggm) (value))


// ********** Metodi standard **********

void L_P1_C2_Init(instance_id_t const my_id);

void L_P1_C2_Exec(instance_id_t const my_id, Phase const p);

ExecResponse L_P1_C2_GExec(global_id_t const proc_id, Phase const p);

void L_P1_C2_GTick(global_id_t const proc_id);

void L_P1_C2_GSetSafe(global_id_t const proc_id);


// ********** Altri metodi pubblici**********

// Macro di effetto
void L_P1__Macro7(instance_id_t const my_id );
void L_P1__Macro8(instance_id_t const my_id );
void L_P1__Macro9(instance_id_t const my_id );

// Macro di verifica
bool L_P1__Macro14(instance_id_t const my_id );
bool L_P1__Macro15(instance_id_t const my_id , C2_Enumerat4 argom20, C2_Enumerat2 argom21, C2_Enumerat3 argom22, C2_Enumerat3 argom23, bool argom24, bool argom25);
bool L_P1__Macro16(instance_id_t const my_id , bool argom26, bool argom27, C2_Enumerat2 argom28, C2_Enumerat4 argom29, bool argom30, bool argom31);

// Macro valorizzate
C2_Enumerat1 L_P1__Macro10(instance_id_t const my_id );
C2_Enumerat1 L_P1__Macro11(instance_id_t const my_id , C2_Enumerat1 argom9, bool argom10, C2_Enumerat1 argom11, C2_Enumerat4 argom12);
bool L_P1__Macro12(instance_id_t const my_id , C2_Enumerat4 argom13, C2_Enumerat1 argom14, C2_Enumerat4 argom15, C2_Enumerat1 argom16, C2_Enumerat1 argom17, C2_Enumerat2 argom18, C2_Enumerat3 argom19);
C2_Enumerat4 L_P1__Macro13(instance_id_t const my_id );


#endif // LIBSTAZIONE_CLASSEL_P1_C2_H
