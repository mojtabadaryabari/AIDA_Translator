// Codice del modello 'TestCase2', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#ifndef LIBSTAZIONE_CLASSEL_P1_C3_H
#define LIBSTAZIONE_CLASSEL_P1_C3_H

#include "envdt.h"
#include "Timer.h"
#include "Counter.h"


// ********** Comandi manuali e relative risposte **********

typedef struct {
    bool event11;
    bool event12;
    bool event13;
    bool event14;
} L_P1_C3_Comandi_Man;

typedef struct {
    ManCmdResponse event15;
    ManCmdResponse event16;
    ManCmdResponse event17;
    ManCmdResponse event18;
} L_P1_C3_Ack_Comandi_Man;

#define L_P1_C3_NUM_COMANDI_MAN 4


// ********** Informazioni per AGGM **********

#define CLASS_L_P1_C3_ID  3

#define L_P1_C3_State_ID  (1)

// ID Variabili
#define L_P1__stato5_ID  (3)
#define L_P1__subcl70_ID  (14)
#define L_P1__subcl72_ID  (16)
#define L_P1__subcl74_ID  (18)
#define L_P1__subcl76_ID  (20)
#define L_P1__subcl78_ID  (22)
#define L_P1__subcl79_ID  (23)
#define L_P1__subcl80_ID  (24)
#define L_P1__subcl81_ID  (25)
#define L_P1__subcl82_ID  (26)
#define L_P1__subcl83_ID  (27)
#define L_P1__subcl84_ID  (28)
#define L_P1__subcl85_ID  (29)
#define L_P1__subcl86_ID  (30)
#define L_P1__subcl87_ID  (31)
#define L_P1__subcl88_ID  (32)
#define L_P1__subcl89_ID  (33)
#define L_P1__subcl90_ID  (34)
#define L_P1__subcl91_ID  (35)
#define L_P1__subcl92_ID  (36)
#define L_P1__subcl93_ID  (37)
#define L_P1__subcl94_ID  (38)
#define L_P1__subcl95_ID  (39)
#define L_P1__subcl96_ID  (40)
#define L_P1__subcl97_ID  (41)
#define L_P1__subcl98_ID  (42)
#define L_P1__subcl99_ID  (43)
#define L_P1__subcl100_ID  (44)
#define L_P1__subcl101_ID  (45)

// ID Timer
#define L_P1__subcl102_ID  (47)
#define L_P1__subcl103_ID  (46)
#define L_P1__subcl104_ID  (49)
#define L_P1__subcl105_ID  (48)
#define L_P1__subcl106_ID  (51)
#define L_P1__subcl107_ID  (50)
#define L_P1__subcl108_ID  (53)
#define L_P1__subcl109_ID  (52)
#define L_P1__subcl110_ID  (55)
#define L_P1__subcl111_ID  (54)
#define L_P1__subcl112_ID  (56)
#define L_P1__subcl113_ID  (57)

// ID Counter
#define L_P1__subcl114_ID  (58)
#define L_P1__subcl115_ID  (59)
#define L_P1__subcl116_ID  (60)
#define L_P1__subcl117_ID  (61)

// ID Controlli dal piazzale
#define L_P1__consd2_ID  (2)
#define L_P1__subcl59_ID  (9)
#define L_P1__subcl60_ID  (10)
#define L_P1__subcl61_ID  (11)
#define L_P1__subcl62_ID  (12)
#define L_P1__subcl69_ID  (13)
#define L_P1__subcl71_ID  (15)
#define L_P1__subcl73_ID  (17)
#define L_P1__subcl75_ID  (19)
#define L_P1__subcl77_ID  (21)

// ID Comandi al piazzale
#define L_P1__subcl54_ID  (4)
#define L_P1__subcl55_ID  (5)
#define L_P1__subcl56_ID  (6)
#define L_P1__subcl57_ID  (7)
#define L_P1__subcl58_ID  (8)

// ID Comandi manuali
#define L_P1__event11_ID  (62)
#define L_P1__event12_ID  (64)
#define L_P1__event13_ID  (66)
#define L_P1__event14_ID  (68)

// ID Risposte ai comandi manuali
#define L_P1__event15Reply_ID  (63)
#define L_P1__event16Reply_ID  (65)
#define L_P1__event17Reply_ID  (67)
#define L_P1__event18Reply_ID  (69)


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
/* C3_Stateenu L_P1__GetStato5(instance_id_t const my_id); */
#define L_P1__GetStato5(my_id)  \
    (C3_Stateenu) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__stato5_ID)
/* void L_P1__SetStato5(instance_id_t const my_id, C3_Stateenu const value); */
#define L_P1__SetStato5(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__stato5_ID, (Taggm) (value))

/* bool L_P1__GetSubcl70(instance_id_t const my_id); */
#define L_P1__GetSubcl70(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl70_ID)
/* void L_P1__SetSubcl70(instance_id_t const my_id, bool const value); */
#define L_P1__SetSubcl70(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl70_ID, (Taggm) (value))

/* C3_Enumerat1 L_P1__GetSubcl72(instance_id_t const my_id); */
#define L_P1__GetSubcl72(my_id)  \
    (C3_Enumerat1) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl72_ID)
/* void L_P1__SetSubcl72(instance_id_t const my_id, C3_Enumerat1 const value); */
#define L_P1__SetSubcl72(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl72_ID, (Taggm) (value))

/* bool L_P1__GetSubcl74(instance_id_t const my_id); */
#define L_P1__GetSubcl74(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl74_ID)
/* void L_P1__SetSubcl74(instance_id_t const my_id, bool const value); */
#define L_P1__SetSubcl74(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl74_ID, (Taggm) (value))

/* C3_Enumerat2 L_P1__GetSubcl76(instance_id_t const my_id); */
#define L_P1__GetSubcl76(my_id)  \
    (C3_Enumerat2) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl76_ID)
/* void L_P1__SetSubcl76(instance_id_t const my_id, C3_Enumerat2 const value); */
#define L_P1__SetSubcl76(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl76_ID, (Taggm) (value))

/* bool L_P1__GetSubcl78(instance_id_t const my_id); */
#define L_P1__GetSubcl78(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl78_ID)
/* void L_P1__SetSubcl78(instance_id_t const my_id, bool const value); */
#define L_P1__SetSubcl78(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl78_ID, (Taggm) (value))

/* bool L_P1__GetSubcl79(instance_id_t const my_id); */
#define L_P1__GetSubcl79(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl79_ID)
/* void L_P1__SetSubcl79(instance_id_t const my_id, bool const value); */
#define L_P1__SetSubcl79(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl79_ID, (Taggm) (value))

/* bool L_P1__GetSubcl80(instance_id_t const my_id); */
#define L_P1__GetSubcl80(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl80_ID)
/* void L_P1__SetSubcl80(instance_id_t const my_id, bool const value); */
#define L_P1__SetSubcl80(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl80_ID, (Taggm) (value))

/* bool L_P1__GetSubcl81(instance_id_t const my_id); */
#define L_P1__GetSubcl81(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl81_ID)
/* void L_P1__SetSubcl81(instance_id_t const my_id, bool const value); */
#define L_P1__SetSubcl81(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl81_ID, (Taggm) (value))

/* bool L_P1__GetSubcl82(instance_id_t const my_id); */
#define L_P1__GetSubcl82(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl82_ID)
/* void L_P1__SetSubcl82(instance_id_t const my_id, bool const value); */
#define L_P1__SetSubcl82(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl82_ID, (Taggm) (value))

/* C3_Enumerat4 L_P1__GetSubcl83(instance_id_t const my_id); */
#define L_P1__GetSubcl83(my_id)  \
    (C3_Enumerat4) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl83_ID)
/* void L_P1__SetSubcl83(instance_id_t const my_id, C3_Enumerat4 const value); */
#define L_P1__SetSubcl83(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl83_ID, (Taggm) (value))

/* C3_Enumerat4 L_P1__GetSubcl84(instance_id_t const my_id); */
#define L_P1__GetSubcl84(my_id)  \
    (C3_Enumerat4) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl84_ID)
/* void L_P1__SetSubcl84(instance_id_t const my_id, C3_Enumerat4 const value); */
#define L_P1__SetSubcl84(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl84_ID, (Taggm) (value))

/* bool L_P1__GetSubcl85(instance_id_t const my_id); */
#define L_P1__GetSubcl85(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl85_ID)
/* void L_P1__SetSubcl85(instance_id_t const my_id, bool const value); */
#define L_P1__SetSubcl85(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl85_ID, (Taggm) (value))

/* bool L_P1__GetSubcl86(instance_id_t const my_id); */
#define L_P1__GetSubcl86(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl86_ID)
/* void L_P1__SetSubcl86(instance_id_t const my_id, bool const value); */
#define L_P1__SetSubcl86(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl86_ID, (Taggm) (value))

/* C3_Enumerat1 L_P1__GetSubcl87(instance_id_t const my_id); */
#define L_P1__GetSubcl87(my_id)  \
    (C3_Enumerat1) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl87_ID)
/* void L_P1__SetSubcl87(instance_id_t const my_id, C3_Enumerat1 const value); */
#define L_P1__SetSubcl87(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl87_ID, (Taggm) (value))

/* C3_Enumerat1 L_P1__GetSubcl88(instance_id_t const my_id); */
#define L_P1__GetSubcl88(my_id)  \
    (C3_Enumerat1) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl88_ID)
/* void L_P1__SetSubcl88(instance_id_t const my_id, C3_Enumerat1 const value); */
#define L_P1__SetSubcl88(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl88_ID, (Taggm) (value))

/* Intero L_P1__GetSubcl89(instance_id_t const my_id); */
#define L_P1__GetSubcl89(my_id)  \
    (Intero) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl89_ID)
/* void L_P1__SetSubcl89(instance_id_t const my_id, Intero const value); */
#define L_P1__SetSubcl89(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl89_ID, (Taggm) (value))

/* Intero L_P1__GetSubcl90(instance_id_t const my_id); */
#define L_P1__GetSubcl90(my_id)  \
    (Intero) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl90_ID)
/* void L_P1__SetSubcl90(instance_id_t const my_id, Intero const value); */
#define L_P1__SetSubcl90(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl90_ID, (Taggm) (value))

/* C3_Enumerat1 L_P1__GetSubcl91(instance_id_t const my_id); */
#define L_P1__GetSubcl91(my_id)  \
    (C3_Enumerat1) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl91_ID)
/* void L_P1__SetSubcl91(instance_id_t const my_id, C3_Enumerat1 const value); */
#define L_P1__SetSubcl91(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl91_ID, (Taggm) (value))

/* C3_Enumerat1 L_P1__GetSubcl92(instance_id_t const my_id); */
#define L_P1__GetSubcl92(my_id)  \
    (C3_Enumerat1) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl92_ID)
/* void L_P1__SetSubcl92(instance_id_t const my_id, C3_Enumerat1 const value); */
#define L_P1__SetSubcl92(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl92_ID, (Taggm) (value))

/* bool L_P1__GetSubcl93(instance_id_t const my_id); */
#define L_P1__GetSubcl93(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl93_ID)
/* void L_P1__SetSubcl93(instance_id_t const my_id, bool const value); */
#define L_P1__SetSubcl93(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl93_ID, (Taggm) (value))

/* bool L_P1__GetSubcl94(instance_id_t const my_id); */
#define L_P1__GetSubcl94(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl94_ID)
/* void L_P1__SetSubcl94(instance_id_t const my_id, bool const value); */
#define L_P1__SetSubcl94(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl94_ID, (Taggm) (value))

/* Intero L_P1__GetSubcl95(instance_id_t const my_id); */
#define L_P1__GetSubcl95(my_id)  \
    (Intero) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl95_ID)
/* void L_P1__SetSubcl95(instance_id_t const my_id, Intero const value); */
#define L_P1__SetSubcl95(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl95_ID, (Taggm) (value))

/* Intero L_P1__GetSubcl96(instance_id_t const my_id); */
#define L_P1__GetSubcl96(my_id)  \
    (Intero) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl96_ID)
/* void L_P1__SetSubcl96(instance_id_t const my_id, Intero const value); */
#define L_P1__SetSubcl96(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl96_ID, (Taggm) (value))

/* C3_Enumerat3 L_P1__GetSubcl97(instance_id_t const my_id); */
#define L_P1__GetSubcl97(my_id)  \
    (C3_Enumerat3) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl97_ID)
/* void L_P1__SetSubcl97(instance_id_t const my_id, C3_Enumerat3 const value); */
#define L_P1__SetSubcl97(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl97_ID, (Taggm) (value))

/* Intero L_P1__GetSubcl98(instance_id_t const my_id); */
#define L_P1__GetSubcl98(my_id)  \
    (Intero) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl98_ID)
/* void L_P1__SetSubcl98(instance_id_t const my_id, Intero const value); */
#define L_P1__SetSubcl98(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl98_ID, (Taggm) (value))

/* bool L_P1__GetSubcl99(instance_id_t const my_id); */
#define L_P1__GetSubcl99(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl99_ID)
/* void L_P1__SetSubcl99(instance_id_t const my_id, bool const value); */
#define L_P1__SetSubcl99(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl99_ID, (Taggm) (value))

/* C3_Enumerat2 L_P1__GetSubcl100(instance_id_t const my_id); */
#define L_P1__GetSubcl100(my_id)  \
    (C3_Enumerat2) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl100_ID)
/* void L_P1__SetSubcl100(instance_id_t const my_id, C3_Enumerat2 const value); */
#define L_P1__SetSubcl100(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl100_ID, (Taggm) (value))

/* bool L_P1__GetSubcl101(instance_id_t const my_id); */
#define L_P1__GetSubcl101(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl101_ID)
/* void L_P1__SetSubcl101(instance_id_t const my_id, bool const value); */
#define L_P1__SetSubcl101(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl101_ID, (Taggm) (value))


// timer
Timer* L_P1__GetSubcl102(instance_id_t const my_id);
Timer* L_P1__GetSubcl103(instance_id_t const my_id);
Timer* L_P1__GetSubcl104(instance_id_t const my_id);
Timer* L_P1__GetSubcl105(instance_id_t const my_id);
Timer* L_P1__GetSubcl106(instance_id_t const my_id);
Timer* L_P1__GetSubcl107(instance_id_t const my_id);
Timer* L_P1__GetSubcl108(instance_id_t const my_id);
Timer* L_P1__GetSubcl109(instance_id_t const my_id);
Timer* L_P1__GetSubcl110(instance_id_t const my_id);
Timer* L_P1__GetSubcl111(instance_id_t const my_id);
Timer* L_P1__GetSubcl112(instance_id_t const my_id);
Timer* L_P1__GetSubcl113(instance_id_t const my_id);

// counter
Counter* L_P1__GetSubcl114(instance_id_t const my_id);    
Counter* L_P1__GetSubcl115(instance_id_t const my_id);    
Counter* L_P1__GetSubcl116(instance_id_t const my_id);    
Counter* L_P1__GetSubcl117(instance_id_t const my_id);    

// comandi manuali
/* bool L_P1__GetInEvent11(instance_id_t const my_id); */
#define L_P1__GetInEvent11(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__event11_ID)
/* bool L_P1__GetInEvent12(instance_id_t const my_id); */
#define L_P1__GetInEvent12(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__event12_ID)
/* bool L_P1__GetInEvent13(instance_id_t const my_id); */
#define L_P1__GetInEvent13(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__event13_ID)
/* bool L_P1__GetInEvent14(instance_id_t const my_id); */
#define L_P1__GetInEvent14(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__event14_ID)

// risposte ai comandi manuali
/* void L_P1__SetOutEvent15(instance_id_t const my_id, ManCmdResponse const value); */
#define L_P1__SetOutEvent15(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__event15Reply_ID, (Taggm) (value))
/* void L_P1__SetOutEvent16(instance_id_t const my_id, ManCmdResponse const value); */
#define L_P1__SetOutEvent16(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__event16Reply_ID, (Taggm) (value))
/* void L_P1__SetOutEvent17(instance_id_t const my_id, ManCmdResponse const value); */
#define L_P1__SetOutEvent17(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__event17Reply_ID, (Taggm) (value))
/* void L_P1__SetOutEvent18(instance_id_t const my_id, ManCmdResponse const value); */
#define L_P1__SetOutEvent18(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__event18Reply_ID, (Taggm) (value))

// controlli dal piazzale
/* bool L_P1__GetInConsd2(instance_id_t const my_id); */
#define L_P1__GetInConsd2(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__consd2_ID)
/* C3_Enumerat2 L_P1__GetInSubcl59(instance_id_t const my_id); */
#define L_P1__GetInSubcl59(my_id)  \
    (C3_Enumerat2) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl59_ID)
/* C3_Enumerat2 L_P1__GetInSubcl60(instance_id_t const my_id); */
#define L_P1__GetInSubcl60(my_id)  \
    (C3_Enumerat2) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl60_ID)
/* C3_Enumerat2 L_P1__GetInSubcl61(instance_id_t const my_id); */
#define L_P1__GetInSubcl61(my_id)  \
    (C3_Enumerat2) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl61_ID)
/* bool L_P1__GetInSubcl62(instance_id_t const my_id); */
#define L_P1__GetInSubcl62(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl62_ID)
/* bool L_P1__GetInSubcl69(instance_id_t const my_id); */
#define L_P1__GetInSubcl69(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl69_ID)
/* C3_Enumerat1 L_P1__GetInSubcl71(instance_id_t const my_id); */
#define L_P1__GetInSubcl71(my_id)  \
    (C3_Enumerat1) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl71_ID)
/* bool L_P1__GetInSubcl73(instance_id_t const my_id); */
#define L_P1__GetInSubcl73(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl73_ID)
/* C3_Enumerat2 L_P1__GetInSubcl75(instance_id_t const my_id); */
#define L_P1__GetInSubcl75(my_id)  \
    (C3_Enumerat2) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl75_ID)
/* bool L_P1__GetInSubcl77(instance_id_t const my_id); */
#define L_P1__GetInSubcl77(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl77_ID)

// comandi al piazzale
/* void L_P1__SetOutSubcl54(instance_id_t const my_id, C3_Enumerat1 const value); */
#define L_P1__SetOutSubcl54(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl54_ID, (Taggm) (value))

/* void L_P1__SetOutSubcl55(instance_id_t const my_id, bool const value); */
#define L_P1__SetOutSubcl55(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl55_ID, (Taggm) (value))

/* void L_P1__SetOutSubcl56(instance_id_t const my_id, C3_Enumerat2 const value); */
#define L_P1__SetOutSubcl56(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl56_ID, (Taggm) (value))

/* void L_P1__SetOutSubcl57(instance_id_t const my_id, C3_Enumerat4 const value); */
#define L_P1__SetOutSubcl57(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl57_ID, (Taggm) (value))

/* void L_P1__SetOutSubcl58(instance_id_t const my_id, bool const value); */
#define L_P1__SetOutSubcl58(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl58_ID, (Taggm) (value))


// ********** Metodi standard **********

void L_P1_C3_Init(instance_id_t const my_id);

void L_P1_C3_Exec(instance_id_t const my_id, Phase const p);

ExecResponse L_P1_C3_GExec(global_id_t const proc_id, Phase const p);

void L_P1_C3_GTick(global_id_t const proc_id);

void L_P1_C3_GSetSafe(global_id_t const proc_id);

void L_P1_C3_GUpdatePrev(global_id_t const proc_id);

// ********** Altri metodi pubblici**********

// Macro di effetto
void L_P1__Macro15(instance_id_t const my_id );
void L_P1__Macro16(instance_id_t const my_id );

// Macro di verifica
bool L_P1__Macro20(instance_id_t const my_id , C3_Enumerat4 argom46, C3_Enumerat1 argom47, C3_Enumerat2 argom48);
bool L_P1__Macro21(instance_id_t const my_id , C3_Enumerat1 argom49, bool argom50, C3_Enumerat1 argom51, C3_Enumerat1 argom52);

// Macro valorizzate
C3_Enumerat2 L_P1__Macro17(instance_id_t const my_id , C3_Enumerat3 argom36, C3_Enumerat3 argom37, C3_Enumerat1 argom38, C3_Enumerat2 argom39);
C3_Enumerat4 L_P1__Macro18(instance_id_t const my_id , bool argom40, C3_Enumerat4 argom41);
bool L_P1__Macro19(instance_id_t const my_id , C3_Enumerat3 argom42, C3_Enumerat1 argom43, C3_Enumerat1 argom44, C3_Enumerat4 argom45);


#endif // LIBSTAZIONE_CLASSEL_P1_C3_H
