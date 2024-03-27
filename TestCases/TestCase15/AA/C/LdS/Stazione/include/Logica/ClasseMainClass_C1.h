// Codice del modello 'TestCase15', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#ifndef LIBSTAZIONE_CLASSEL_P1_C1_H
#define LIBSTAZIONE_CLASSEL_P1_C1_H

#include "envdt.h"
#include "Timer.h"
#include "Counter.h"


// ********** Comandi manuali e relative risposte **********

typedef struct {
    bool event1;
    bool event2;
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
#define L_P1__mainc15_ID  (13)
#define L_P1__mainc17_ID  (15)
#define L_P1__mainc19_ID  (17)
#define L_P1__mainc21_ID  (19)
#define L_P1__mainc22_ID  (20)
#define L_P1__mainc23_ID  (21)
#define L_P1__mainc24_ID  (22)
#define L_P1__mainc25_ID  (23)
#define L_P1__mainc26_ID  (24)
#define L_P1__mainc27_ID  (25)
#define L_P1__mainc28_ID  (26)
#define L_P1__mainc29_ID  (27)
#define L_P1__mainc30_ID  (28)
#define L_P1__mainc31_ID  (29)
#define L_P1__mainc32_ID  (30)
#define L_P1__mainc33_ID  (31)
#define L_P1__mainc34_ID  (32)
#define L_P1__mainc35_ID  (33)
#define L_P1__mainc36_ID  (34)
#define L_P1__mainc37_ID  (35)
#define L_P1__mainc38_ID  (36)
#define L_P1__mainc39_ID  (37)
#define L_P1__stato1_ID  (38)

// ID Timer
#define L_P1__mainc40_ID  (40)
#define L_P1__mainc41_ID  (39)
#define L_P1__mainc42_ID  (42)
#define L_P1__mainc43_ID  (41)
#define L_P1__mainc44_ID  (44)
#define L_P1__mainc45_ID  (43)
#define L_P1__mainc46_ID  (46)
#define L_P1__mainc47_ID  (45)
#define L_P1__mainc48_ID  (47)
#define L_P1__mainc49_ID  (48)
#define L_P1__mainc50_ID  (49)

// ID Counter
#define L_P1__mainc51_ID  (50)
#define L_P1__mainc52_ID  (51)
#define L_P1__mainc53_ID  (52)
#define L_P1__mainc54_ID  (53)
#define L_P1__mainc55_ID  (54)

// ID Controlli dal piazzale
#define L_P1__consd_ID  (2)
#define L_P1__mainc5_ID  (8)
#define L_P1__mainc6_ID  (9)
#define L_P1__mainc7_ID  (10)
#define L_P1__mainc8_ID  (11)
#define L_P1__mainc14_ID  (12)
#define L_P1__mainc16_ID  (14)
#define L_P1__mainc18_ID  (16)
#define L_P1__mainc20_ID  (18)

// ID Comandi al piazzale
#define L_P1__mainc_ID  (3)
#define L_P1__mainc1_ID  (4)
#define L_P1__mainc2_ID  (5)
#define L_P1__mainc3_ID  (6)
#define L_P1__mainc4_ID  (7)

// ID Comandi manuali
#define L_P1__event1_ID  (55)
#define L_P1__event2_ID  (57)
#define L_P1__event3_ID  (59)

// ID Risposte ai comandi manuali
#define L_P1__event4Reply_ID  (56)
#define L_P1__event5Reply_ID  (58)
#define L_P1__event6Reply_ID  (60)


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
/* C1_Enumerat3 L_P1__GetMainc15(instance_id_t const my_id); */
#define L_P1__GetMainc15(my_id)  \
    (C1_Enumerat3) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc15_ID)
/* void L_P1__SetMainc15(instance_id_t const my_id, C1_Enumerat3 const value); */
#define L_P1__SetMainc15(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc15_ID, (Taggm) (value))

/* bool L_P1__GetMainc17(instance_id_t const my_id); */
#define L_P1__GetMainc17(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc17_ID)
/* void L_P1__SetMainc17(instance_id_t const my_id, bool const value); */
#define L_P1__SetMainc17(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc17_ID, (Taggm) (value))

/* bool L_P1__GetMainc19(instance_id_t const my_id); */
#define L_P1__GetMainc19(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc19_ID)
/* void L_P1__SetMainc19(instance_id_t const my_id, bool const value); */
#define L_P1__SetMainc19(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc19_ID, (Taggm) (value))

/* C1_Enumerat4 L_P1__GetMainc21(instance_id_t const my_id); */
#define L_P1__GetMainc21(my_id)  \
    (C1_Enumerat4) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc21_ID)
/* void L_P1__SetMainc21(instance_id_t const my_id, C1_Enumerat4 const value); */
#define L_P1__SetMainc21(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc21_ID, (Taggm) (value))

/* Intero L_P1__GetMainc22(instance_id_t const my_id); */
#define L_P1__GetMainc22(my_id)  \
    (Intero) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc22_ID)
/* void L_P1__SetMainc22(instance_id_t const my_id, Intero const value); */
#define L_P1__SetMainc22(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc22_ID, (Taggm) (value))

/* Intero L_P1__GetMainc23(instance_id_t const my_id); */
#define L_P1__GetMainc23(my_id)  \
    (Intero) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc23_ID)
/* void L_P1__SetMainc23(instance_id_t const my_id, Intero const value); */
#define L_P1__SetMainc23(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc23_ID, (Taggm) (value))

/* C1_Enumerat1 L_P1__GetMainc24(instance_id_t const my_id); */
#define L_P1__GetMainc24(my_id)  \
    (C1_Enumerat1) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc24_ID)
/* void L_P1__SetMainc24(instance_id_t const my_id, C1_Enumerat1 const value); */
#define L_P1__SetMainc24(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc24_ID, (Taggm) (value))

/* C1_Enumerat1 L_P1__GetMainc25(instance_id_t const my_id); */
#define L_P1__GetMainc25(my_id)  \
    (C1_Enumerat1) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc25_ID)
/* void L_P1__SetMainc25(instance_id_t const my_id, C1_Enumerat1 const value); */
#define L_P1__SetMainc25(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc25_ID, (Taggm) (value))

/* Intero L_P1__GetMainc26(instance_id_t const my_id); */
#define L_P1__GetMainc26(my_id)  \
    (Intero) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc26_ID)
/* void L_P1__SetMainc26(instance_id_t const my_id, Intero const value); */
#define L_P1__SetMainc26(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc26_ID, (Taggm) (value))

/* Intero L_P1__GetMainc27(instance_id_t const my_id); */
#define L_P1__GetMainc27(my_id)  \
    (Intero) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc27_ID)
/* void L_P1__SetMainc27(instance_id_t const my_id, Intero const value); */
#define L_P1__SetMainc27(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc27_ID, (Taggm) (value))

/* C1_Enumerat2 L_P1__GetMainc28(instance_id_t const my_id); */
#define L_P1__GetMainc28(my_id)  \
    (C1_Enumerat2) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc28_ID)
/* void L_P1__SetMainc28(instance_id_t const my_id, C1_Enumerat2 const value); */
#define L_P1__SetMainc28(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc28_ID, (Taggm) (value))

/* C1_Enumerat2 L_P1__GetMainc29(instance_id_t const my_id); */
#define L_P1__GetMainc29(my_id)  \
    (C1_Enumerat2) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc29_ID)
/* void L_P1__SetMainc29(instance_id_t const my_id, C1_Enumerat2 const value); */
#define L_P1__SetMainc29(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc29_ID, (Taggm) (value))

/* bool L_P1__GetMainc30(instance_id_t const my_id); */
#define L_P1__GetMainc30(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc30_ID)
/* void L_P1__SetMainc30(instance_id_t const my_id, bool const value); */
#define L_P1__SetMainc30(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc30_ID, (Taggm) (value))

/* bool L_P1__GetMainc31(instance_id_t const my_id); */
#define L_P1__GetMainc31(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc31_ID)
/* void L_P1__SetMainc31(instance_id_t const my_id, bool const value); */
#define L_P1__SetMainc31(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc31_ID, (Taggm) (value))

/* bool L_P1__GetMainc32(instance_id_t const my_id); */
#define L_P1__GetMainc32(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc32_ID)
/* void L_P1__SetMainc32(instance_id_t const my_id, bool const value); */
#define L_P1__SetMainc32(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc32_ID, (Taggm) (value))

/* bool L_P1__GetMainc33(instance_id_t const my_id); */
#define L_P1__GetMainc33(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc33_ID)
/* void L_P1__SetMainc33(instance_id_t const my_id, bool const value); */
#define L_P1__SetMainc33(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc33_ID, (Taggm) (value))

/* bool L_P1__GetMainc34(instance_id_t const my_id); */
#define L_P1__GetMainc34(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc34_ID)
/* void L_P1__SetMainc34(instance_id_t const my_id, bool const value); */
#define L_P1__SetMainc34(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc34_ID, (Taggm) (value))

/* bool L_P1__GetMainc35(instance_id_t const my_id); */
#define L_P1__GetMainc35(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc35_ID)
/* void L_P1__SetMainc35(instance_id_t const my_id, bool const value); */
#define L_P1__SetMainc35(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc35_ID, (Taggm) (value))

/* C1_Enumerat3 L_P1__GetMainc36(instance_id_t const my_id); */
#define L_P1__GetMainc36(my_id)  \
    (C1_Enumerat3) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc36_ID)
/* void L_P1__SetMainc36(instance_id_t const my_id, C1_Enumerat3 const value); */
#define L_P1__SetMainc36(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc36_ID, (Taggm) (value))

/* C1_Enumerat3 L_P1__GetMainc37(instance_id_t const my_id); */
#define L_P1__GetMainc37(my_id)  \
    (C1_Enumerat3) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc37_ID)
/* void L_P1__SetMainc37(instance_id_t const my_id, C1_Enumerat3 const value); */
#define L_P1__SetMainc37(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc37_ID, (Taggm) (value))

/* bool L_P1__GetMainc38(instance_id_t const my_id); */
#define L_P1__GetMainc38(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc38_ID)
/* void L_P1__SetMainc38(instance_id_t const my_id, bool const value); */
#define L_P1__SetMainc38(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc38_ID, (Taggm) (value))

/* bool L_P1__GetMainc39(instance_id_t const my_id); */
#define L_P1__GetMainc39(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc39_ID)
/* void L_P1__SetMainc39(instance_id_t const my_id, bool const value); */
#define L_P1__SetMainc39(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc39_ID, (Taggm) (value))

/* C1_Stateenu L_P1__GetStato1(instance_id_t const my_id); */
#define L_P1__GetStato1(my_id)  \
    (C1_Stateenu) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__stato1_ID)
/* void L_P1__SetStato1(instance_id_t const my_id, C1_Stateenu const value); */
#define L_P1__SetStato1(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__stato1_ID, (Taggm) (value))


// timer
Timer* L_P1__GetMainc40(instance_id_t const my_id);
Timer* L_P1__GetMainc41(instance_id_t const my_id);
Timer* L_P1__GetMainc42(instance_id_t const my_id);
Timer* L_P1__GetMainc43(instance_id_t const my_id);
Timer* L_P1__GetMainc44(instance_id_t const my_id);
Timer* L_P1__GetMainc45(instance_id_t const my_id);
Timer* L_P1__GetMainc46(instance_id_t const my_id);
Timer* L_P1__GetMainc47(instance_id_t const my_id);
Timer* L_P1__GetMainc48(instance_id_t const my_id);
Timer* L_P1__GetMainc49(instance_id_t const my_id);
Timer* L_P1__GetMainc50(instance_id_t const my_id);

// counter
Counter* L_P1__GetMainc51(instance_id_t const my_id);    
Counter* L_P1__GetMainc52(instance_id_t const my_id);    
Counter* L_P1__GetMainc53(instance_id_t const my_id);    
Counter* L_P1__GetMainc54(instance_id_t const my_id);    
Counter* L_P1__GetMainc55(instance_id_t const my_id);    

// comandi manuali
/* bool L_P1__GetInEvent1(instance_id_t const my_id); */
#define L_P1__GetInEvent1(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__event1_ID)
/* bool L_P1__GetInEvent2(instance_id_t const my_id); */
#define L_P1__GetInEvent2(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__event2_ID)
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
/* bool L_P1__GetInConsd(instance_id_t const my_id); */
#define L_P1__GetInConsd(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__consd_ID)
/* C1_Enumerat1 L_P1__GetInMainc5(instance_id_t const my_id); */
#define L_P1__GetInMainc5(my_id)  \
    (C1_Enumerat1) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc5_ID)
/* bool L_P1__GetInMainc6(instance_id_t const my_id); */
#define L_P1__GetInMainc6(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc6_ID)
/* bool L_P1__GetInMainc7(instance_id_t const my_id); */
#define L_P1__GetInMainc7(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc7_ID)
/* bool L_P1__GetInMainc8(instance_id_t const my_id); */
#define L_P1__GetInMainc8(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc8_ID)
/* C1_Enumerat3 L_P1__GetInMainc14(instance_id_t const my_id); */
#define L_P1__GetInMainc14(my_id)  \
    (C1_Enumerat3) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc14_ID)
/* bool L_P1__GetInMainc16(instance_id_t const my_id); */
#define L_P1__GetInMainc16(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc16_ID)
/* bool L_P1__GetInMainc18(instance_id_t const my_id); */
#define L_P1__GetInMainc18(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc18_ID)
/* C1_Enumerat4 L_P1__GetInMainc20(instance_id_t const my_id); */
#define L_P1__GetInMainc20(my_id)  \
    (C1_Enumerat4) \
    LogicGetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc20_ID)

// comandi al piazzale
/* void L_P1__SetOutMainc(instance_id_t const my_id, bool const value); */
#define L_P1__SetOutMainc(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc_ID, (Taggm) (value))

/* void L_P1__SetOutMainc1(instance_id_t const my_id, bool const value); */
#define L_P1__SetOutMainc1(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc1_ID, (Taggm) (value))

/* void L_P1__SetOutMainc2(instance_id_t const my_id, C1_Enumerat4 const value); */
#define L_P1__SetOutMainc2(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc2_ID, (Taggm) (value))

/* void L_P1__SetOutMainc3(instance_id_t const my_id, C1_Enumerat2 const value); */
#define L_P1__SetOutMainc3(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc3_ID, (Taggm) (value))

/* void L_P1__SetOutMainc4(instance_id_t const my_id, bool const value); */
#define L_P1__SetOutMainc4(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C1_ID, (my_id), L_P1__mainc4_ID, (Taggm) (value))


// ********** Metodi standard **********

void L_P1_C1_Init(instance_id_t const my_id);

void L_P1_C1_Exec(instance_id_t const my_id, Phase const p);

ExecResponse L_P1_C1_GExec(global_id_t const proc_id, Phase const p);

void L_P1_C1_GTick(global_id_t const proc_id);

void L_P1_C1_GSetSafe(global_id_t const proc_id);

void L_P1_C1_GUpdatePrev(global_id_t const proc_id);

// ********** Altri metodi pubblici**********

// Macro di effetto
void L_P1__Macro(instance_id_t const my_id );
void L_P1__Macro1(instance_id_t const my_id );

// Macro di verifica
bool L_P1__Macro7(instance_id_t const my_id );
bool L_P1__Macro8(instance_id_t const my_id );
bool L_P1__Macro9(instance_id_t const my_id );
bool L_P1__Macro10(instance_id_t const my_id );

// Macro valorizzate
C1_Enumerat1 L_P1__Macro2(instance_id_t const my_id , C1_Enumerat2 argom, C1_Enumerat1 argom1, bool argom2, C1_Enumerat2 argom3, C1_Enumerat4 argom4, C1_Enumerat3 argom5, C1_Enumerat4 argom6);
bool L_P1__Macro3(instance_id_t const my_id , C1_Enumerat4 argom7, C1_Enumerat4 argom8, bool argom9);
C1_Enumerat2 L_P1__Macro4(instance_id_t const my_id , C1_Enumerat2 argom10, C1_Enumerat1 argom11, C1_Enumerat3 argom12, C1_Enumerat2 argom13, C1_Enumerat3 argom14, C1_Enumerat4 argom15);
bool L_P1__Macro5(instance_id_t const my_id , C1_Enumerat1 argom16, C1_Enumerat2 argom17);
C1_Enumerat1 L_P1__Macro6(instance_id_t const my_id , C1_Enumerat1 argom18, C1_Enumerat2 argom19, bool argom20, C1_Enumerat2 argom21, C1_Enumerat3 argom22, C1_Enumerat1 argom23);


#endif // LIBSTAZIONE_CLASSEL_P1_C1_H
