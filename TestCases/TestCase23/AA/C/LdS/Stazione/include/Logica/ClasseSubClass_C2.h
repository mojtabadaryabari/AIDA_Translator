// Codice del modello 'TestCase23', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#ifndef LIBSTAZIONE_CLASSEL_P1_C2_H
#define LIBSTAZIONE_CLASSEL_P1_C2_H

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
#define L_P1__stato3_ID  (3)
#define L_P1__subcl8_ID  (8)
#define L_P1__subcl9_ID  (9)
#define L_P1__subcl10_ID  (10)
#define L_P1__subcl11_ID  (11)
#define L_P1__subcl12_ID  (12)
#define L_P1__subcl13_ID  (13)
#define L_P1__subcl14_ID  (14)
#define L_P1__subcl15_ID  (15)
#define L_P1__subcl16_ID  (16)
#define L_P1__subcl17_ID  (17)
#define L_P1__subcl18_ID  (18)
#define L_P1__subcl19_ID  (19)
#define L_P1__subcl20_ID  (20)
#define L_P1__subcl21_ID  (21)
#define L_P1__subcl22_ID  (22)
#define L_P1__subcl23_ID  (23)
#define L_P1__subcl24_ID  (24)

// ID Timer
#define L_P1__subcl25_ID  (26)
#define L_P1__subcl26_ID  (25)
#define L_P1__subcl27_ID  (27)

// ID Counter
#define L_P1__subcl28_ID  (28)
#define L_P1__subcl29_ID  (29)

// ID Controlli dal piazzale
#define L_P1__consd1_ID  (2)
#define L_P1__subcl2_ID  (6)
#define L_P1__subcl7_ID  (7)

// ID Comandi al piazzale
#define L_P1__subcl_ID  (4)
#define L_P1__subcl1_ID  (5)

// ID Comandi manuali
#define L_P1__event5_ID  (30)

// ID Risposte ai comandi manuali
#define L_P1__event9Reply_ID  (31)


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
/* C2_Stateenu L_P1__GetStato3(instance_id_t const my_id); */
#define L_P1__GetStato3(my_id)  \
    (C2_Stateenu) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__stato3_ID)
/* void L_P1__SetStato3(instance_id_t const my_id, C2_Stateenu const value); */
#define L_P1__SetStato3(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__stato3_ID, (Taggm) (value))

/* C2_Enumerat1 L_P1__GetSubcl8(instance_id_t const my_id); */
#define L_P1__GetSubcl8(my_id)  \
    (C2_Enumerat1) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl8_ID)
/* void L_P1__SetSubcl8(instance_id_t const my_id, C2_Enumerat1 const value); */
#define L_P1__SetSubcl8(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl8_ID, (Taggm) (value))

/* Intero L_P1__GetSubcl9(instance_id_t const my_id); */
#define L_P1__GetSubcl9(my_id)  \
    (Intero) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl9_ID)
/* void L_P1__SetSubcl9(instance_id_t const my_id, Intero const value); */
#define L_P1__SetSubcl9(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl9_ID, (Taggm) (value))

/* Intero L_P1__GetSubcl10(instance_id_t const my_id); */
#define L_P1__GetSubcl10(my_id)  \
    (Intero) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl10_ID)
/* void L_P1__SetSubcl10(instance_id_t const my_id, Intero const value); */
#define L_P1__SetSubcl10(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl10_ID, (Taggm) (value))

/* bool L_P1__GetSubcl11(instance_id_t const my_id); */
#define L_P1__GetSubcl11(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl11_ID)
/* void L_P1__SetSubcl11(instance_id_t const my_id, bool const value); */
#define L_P1__SetSubcl11(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl11_ID, (Taggm) (value))

/* bool L_P1__GetSubcl12(instance_id_t const my_id); */
#define L_P1__GetSubcl12(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl12_ID)
/* void L_P1__SetSubcl12(instance_id_t const my_id, bool const value); */
#define L_P1__SetSubcl12(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl12_ID, (Taggm) (value))

/* C2_Enumerat3 L_P1__GetSubcl13(instance_id_t const my_id); */
#define L_P1__GetSubcl13(my_id)  \
    (C2_Enumerat3) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl13_ID)
/* void L_P1__SetSubcl13(instance_id_t const my_id, C2_Enumerat3 const value); */
#define L_P1__SetSubcl13(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl13_ID, (Taggm) (value))

/* C2_Enumerat3 L_P1__GetSubcl14(instance_id_t const my_id); */
#define L_P1__GetSubcl14(my_id)  \
    (C2_Enumerat3) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl14_ID)
/* void L_P1__SetSubcl14(instance_id_t const my_id, C2_Enumerat3 const value); */
#define L_P1__SetSubcl14(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl14_ID, (Taggm) (value))

/* Intero L_P1__GetSubcl15(instance_id_t const my_id); */
#define L_P1__GetSubcl15(my_id)  \
    (Intero) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl15_ID)
/* void L_P1__SetSubcl15(instance_id_t const my_id, Intero const value); */
#define L_P1__SetSubcl15(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl15_ID, (Taggm) (value))

/* Intero L_P1__GetSubcl16(instance_id_t const my_id); */
#define L_P1__GetSubcl16(my_id)  \
    (Intero) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl16_ID)
/* void L_P1__SetSubcl16(instance_id_t const my_id, Intero const value); */
#define L_P1__SetSubcl16(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl16_ID, (Taggm) (value))

/* bool L_P1__GetSubcl17(instance_id_t const my_id); */
#define L_P1__GetSubcl17(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl17_ID)
/* void L_P1__SetSubcl17(instance_id_t const my_id, bool const value); */
#define L_P1__SetSubcl17(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl17_ID, (Taggm) (value))

/* bool L_P1__GetSubcl18(instance_id_t const my_id); */
#define L_P1__GetSubcl18(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl18_ID)
/* void L_P1__SetSubcl18(instance_id_t const my_id, bool const value); */
#define L_P1__SetSubcl18(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl18_ID, (Taggm) (value))

/* bool L_P1__GetSubcl19(instance_id_t const my_id); */
#define L_P1__GetSubcl19(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl19_ID)
/* void L_P1__SetSubcl19(instance_id_t const my_id, bool const value); */
#define L_P1__SetSubcl19(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl19_ID, (Taggm) (value))

/* bool L_P1__GetSubcl20(instance_id_t const my_id); */
#define L_P1__GetSubcl20(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl20_ID)
/* void L_P1__SetSubcl20(instance_id_t const my_id, bool const value); */
#define L_P1__SetSubcl20(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl20_ID, (Taggm) (value))

/* bool L_P1__GetSubcl21(instance_id_t const my_id); */
#define L_P1__GetSubcl21(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl21_ID)
/* void L_P1__SetSubcl21(instance_id_t const my_id, bool const value); */
#define L_P1__SetSubcl21(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl21_ID, (Taggm) (value))

/* bool L_P1__GetSubcl22(instance_id_t const my_id); */
#define L_P1__GetSubcl22(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl22_ID)
/* void L_P1__SetSubcl22(instance_id_t const my_id, bool const value); */
#define L_P1__SetSubcl22(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl22_ID, (Taggm) (value))

/* Intero L_P1__GetSubcl23(instance_id_t const my_id); */
#define L_P1__GetSubcl23(my_id)  \
    (Intero) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl23_ID)
/* void L_P1__SetSubcl23(instance_id_t const my_id, Intero const value); */
#define L_P1__SetSubcl23(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl23_ID, (Taggm) (value))

/* bool L_P1__GetSubcl24(instance_id_t const my_id); */
#define L_P1__GetSubcl24(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl24_ID)
/* void L_P1__SetSubcl24(instance_id_t const my_id, bool const value); */
#define L_P1__SetSubcl24(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl24_ID, (Taggm) (value))


// timer
Timer* L_P1__GetSubcl25(instance_id_t const my_id);
Timer* L_P1__GetSubcl26(instance_id_t const my_id);
Timer* L_P1__GetSubcl27(instance_id_t const my_id);

// counter
Counter* L_P1__GetSubcl28(instance_id_t const my_id);    
Counter* L_P1__GetSubcl29(instance_id_t const my_id);    

// comandi manuali
/* bool L_P1__GetInEvent5(instance_id_t const my_id); */
#define L_P1__GetInEvent5(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__event5_ID)

// risposte ai comandi manuali
/* void L_P1__SetOutEvent9(instance_id_t const my_id, ManCmdResponse const value); */
#define L_P1__SetOutEvent9(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__event9Reply_ID, (Taggm) (value))

// controlli dal piazzale
/* bool L_P1__GetInConsd1(instance_id_t const my_id); */
#define L_P1__GetInConsd1(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__consd1_ID)
/* C2_Enumerat1 L_P1__GetInSubcl2(instance_id_t const my_id); */
#define L_P1__GetInSubcl2(my_id)  \
    (C2_Enumerat1) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl2_ID)
/* C2_Enumerat1 L_P1__GetInSubcl7(instance_id_t const my_id); */
#define L_P1__GetInSubcl7(my_id)  \
    (C2_Enumerat1) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl7_ID)

// comandi al piazzale
/* void L_P1__SetOutSubcl(instance_id_t const my_id, C2_Enumerat4 const value); */
#define L_P1__SetOutSubcl(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl_ID, (Taggm) (value))

/* void L_P1__SetOutSubcl1(instance_id_t const my_id, C2_Enumerat1 const value); */
#define L_P1__SetOutSubcl1(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl1_ID, (Taggm) (value))


// ********** Metodi standard **********

void L_P1_C2_Init(instance_id_t const my_id);

void L_P1_C2_Exec(instance_id_t const my_id, Phase const p);

ExecResponse L_P1_C2_GExec(global_id_t const proc_id, Phase const p);

void L_P1_C2_GTick(global_id_t const proc_id);

void L_P1_C2_GSetSafe(global_id_t const proc_id);

void L_P1_C2_GUpdatePrev(global_id_t const proc_id);

// ********** Altri metodi pubblici**********

// Macro di effetto
void L_P1__Macro8(instance_id_t const my_id );
void L_P1__Macro9(instance_id_t const my_id );
void L_P1__Macro10(instance_id_t const my_id );
void L_P1__Macro11(instance_id_t const my_id );
void L_P1__Macro12(instance_id_t const my_id );

// Macro di verifica
bool L_P1__Macro14(instance_id_t const my_id , bool argom24, bool argom25, C2_Enumerat4 argom26, C2_Enumerat2 argom27, bool argom28, C2_Enumerat1 argom29);
bool L_P1__Macro15(instance_id_t const my_id );
bool L_P1__Macro16(instance_id_t const my_id );
bool L_P1__Macro17(instance_id_t const my_id , bool argom30, C2_Enumerat2 argom31, bool argom32, bool argom33, C2_Enumerat2 argom34, C2_Enumerat3 argom35, bool argom36);

// Macro valorizzate
C2_Enumerat3 L_P1__Macro13(instance_id_t const my_id , C2_Enumerat4 argom20, bool argom21, C2_Enumerat1 argom22, C2_Enumerat1 argom23);


#endif // LIBSTAZIONE_CLASSEL_P1_C2_H
