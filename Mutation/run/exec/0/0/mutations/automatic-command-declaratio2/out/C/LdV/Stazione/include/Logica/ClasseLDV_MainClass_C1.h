#ifndef LIBSTAZIONE_CLASSEL_P1_C3_H
#define LIBSTAZIONE_CLASSEL_P1_C3_H

#include "envdt.h"
#include "Timer.h"
#include "Counter.h"


// ********** Comandi manuali e relative risposte **********

typedef struct {
    bool event12;
    bool event13;
} L_P1_C3_Comandi_Man;

typedef struct {
    ManCmdResponse event15;
    ManCmdResponse event16;
} L_P1_C3_Ack_Comandi_Man;

#define L_P1_C3_NUM_COMANDI_MAN 2


// ********** Informazioni per AGGM **********

#define CLASS_L_P1_C3_ID  3

#define L_P1_C3_State_ID  (1)

// ID Variabili
#define L_P1__ldv_m3_ID  (2)
#define L_P1__ldv_m4_ID  (3)
#define L_P1__ldv_m5_ID  (4)
#define L_P1__stato5_ID  (5)

// ID Timer
#define L_P1__ldv_m6_ID  (6)

// ID Counter
#define L_P1__ldv_m7_ID  (7)
#define L_P1__ldv_m8_ID  (8)
#define L_P1__ldv_m9_ID  (9)
#define L_P1__ldv_m10_ID  (10)

// ID Controlli dal piazzale

// ID Comandi al piazzale

// ID Comandi manuali
#define L_P1__event12_ID  (11)
#define L_P1__event13_ID  (13)

// ID Risposte ai comandi manuali
#define L_P1__event15Reply_ID  (12)
#define L_P1__event16Reply_ID  (14)


// ********** Getter/setter pubblici **********

/* C3_Stateenu L_P1_C3_GetState(instance_id_t const my_id) */
#define L_P1_C3_GetState(my_id)  \
    (C3_Stateenu) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1_C3_State_ID)

/* void L_P1_C3_SetState(instance_id_t const my_id, C3_Stateenu const value) */
#define L_P1_C3_SetState(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1_C3_State_ID, (Taggm) (value))

// variabili
/* Intero L_P1__GetLdv_m3(instance_id_t const my_id); */
#define L_P1__GetLdv_m3(my_id)  \
    (Intero) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__ldv_m3_ID)
/* void L_P1__SetLdv_m3(instance_id_t const my_id, Intero const value); */
#define L_P1__SetLdv_m3(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__ldv_m3_ID, (Taggm) (value))

/* bool L_P1__GetLdv_m4(instance_id_t const my_id); */
#define L_P1__GetLdv_m4(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__ldv_m4_ID)
/* void L_P1__SetLdv_m4(instance_id_t const my_id, bool const value); */
#define L_P1__SetLdv_m4(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__ldv_m4_ID, (Taggm) (value))

/* C3_Enumerat3 L_P1__GetLdv_m5(instance_id_t const my_id); */
#define L_P1__GetLdv_m5(my_id)  \
    (C3_Enumerat3) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__ldv_m5_ID)
/* void L_P1__SetLdv_m5(instance_id_t const my_id, C3_Enumerat3 const value); */
#define L_P1__SetLdv_m5(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__ldv_m5_ID, (Taggm) (value))

/* C3_Stateenu L_P1__GetStato5(instance_id_t const my_id); */
#define L_P1__GetStato5(my_id)  \
    (C3_Stateenu) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__stato5_ID)
/* void L_P1__SetStato5(instance_id_t const my_id, C3_Stateenu const value); */
#define L_P1__SetStato5(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__stato5_ID, (Taggm) (value))


// timer
Timer* L_P1__GetLdv_m6(instance_id_t const my_id);

// counter
Counter* L_P1__GetLdv_m7(instance_id_t const my_id);    
Counter* L_P1__GetLdv_m8(instance_id_t const my_id);    
Counter* L_P1__GetLdv_m9(instance_id_t const my_id);    
Counter* L_P1__GetLdv_m10(instance_id_t const my_id);    

// comandi manuali
/* bool L_P1__GetInEvent12(instance_id_t const my_id); */
#define L_P1__GetInEvent12(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__event12_ID)
/* bool L_P1__GetInEvent13(instance_id_t const my_id); */
#define L_P1__GetInEvent13(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__event13_ID)

// risposte ai comandi manuali
/* void L_P1__SetOutEvent15(instance_id_t const my_id, ManCmdResponse const value); */
#define L_P1__SetOutEvent15(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__event15Reply_ID, (Taggm) (value))
/* void L_P1__SetOutEvent16(instance_id_t const my_id, ManCmdResponse const value); */
#define L_P1__SetOutEvent16(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__event16Reply_ID, (Taggm) (value))

// controlli dal piazzale

// comandi al piazzale

// ********** Metodi standard **********

void L_P1_C3_Init(instance_id_t const my_id);

void L_P1_C3_Exec(instance_id_t const my_id, Phase const p);

ExecResponse L_P1_C3_GExec(global_id_t const proc_id, Phase const p);

void L_P1_C3_GTick(global_id_t const proc_id);



// ********** Altri metodi pubblici**********

// Macro di effetto
void L_P1__Macro16(instance_id_t const my_id );
void L_P1__Macro17(instance_id_t const my_id );
void L_P1__Macro18(instance_id_t const my_id );
void L_P1__Macro19(instance_id_t const my_id );
void L_P1__Macro20(instance_id_t const my_id );

// Macro di verifica
bool L_P1__Macro23(instance_id_t const my_id , bool argom39, C3_Enumerat4 argom40, bool argom41, C3_Enumerat1 argom42);
bool L_P1__Macro24(instance_id_t const my_id , C3_Enumerat1 argom43, C3_Enumerat4 argom44, bool argom45, C3_Enumerat4 argom46, C3_Enumerat4 argom47, C3_Enumerat1 argom48, bool argom49);
bool L_P1__Macro25(instance_id_t const my_id , C3_Enumerat3 argom50, C3_Enumerat4 argom51, C3_Enumerat3 argom52, C3_Enumerat1 argom53, bool argom54, C3_Enumerat3 argom55, C3_Enumerat4 argom56);

// Macro valorizzate
bool L_P1__Macro21(instance_id_t const my_id , bool argom33, C3_Enumerat1 argom34, C3_Enumerat4 argom35, C3_Enumerat1 argom36);
bool L_P1__Macro22(instance_id_t const my_id , bool argom37, C3_Enumerat4 argom38);


#endif // LIBSTAZIONE_CLASSEL_P1_C3_H
