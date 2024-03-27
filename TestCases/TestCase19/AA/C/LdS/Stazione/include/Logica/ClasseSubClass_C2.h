// Codice del modello 'TestCase19', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#ifndef LIBSTAZIONE_CLASSEL_P1_C2_H
#define LIBSTAZIONE_CLASSEL_P1_C2_H

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
#define L_P1__stato3_ID  (3)
#define L_P1__subcl13_ID  (10)
#define L_P1__subcl15_ID  (12)
#define L_P1__subcl17_ID  (14)
#define L_P1__subcl19_ID  (16)
#define L_P1__subcl21_ID  (18)
#define L_P1__subcl22_ID  (19)
#define L_P1__subcl23_ID  (20)
#define L_P1__subcl24_ID  (21)
#define L_P1__subcl25_ID  (22)
#define L_P1__subcl26_ID  (23)
#define L_P1__subcl27_ID  (24)
#define L_P1__subcl28_ID  (25)
#define L_P1__subcl29_ID  (26)
#define L_P1__subcl30_ID  (27)
#define L_P1__subcl31_ID  (28)
#define L_P1__subcl32_ID  (29)
#define L_P1__subcl33_ID  (30)
#define L_P1__subcl34_ID  (31)
#define L_P1__subcl35_ID  (32)
#define L_P1__subcl36_ID  (33)

// ID Timer
#define L_P1__subcl37_ID  (35)
#define L_P1__subcl38_ID  (34)
#define L_P1__subcl39_ID  (37)
#define L_P1__subcl40_ID  (36)
#define L_P1__subcl41_ID  (39)
#define L_P1__subcl42_ID  (38)
#define L_P1__subcl43_ID  (41)
#define L_P1__subcl44_ID  (40)
#define L_P1__subcl45_ID  (42)
#define L_P1__subcl46_ID  (43)
#define L_P1__subcl47_ID  (44)
#define L_P1__subcl48_ID  (45)
#define L_P1__subcl49_ID  (46)

// ID Counter
#define L_P1__subcl50_ID  (47)
#define L_P1__subcl51_ID  (48)
#define L_P1__subcl52_ID  (49)

// ID Controlli dal piazzale
#define L_P1__consd1_ID  (2)
#define L_P1__subcl2_ID  (6)
#define L_P1__subcl3_ID  (7)
#define L_P1__subcl4_ID  (8)
#define L_P1__subcl12_ID  (9)
#define L_P1__subcl14_ID  (11)
#define L_P1__subcl16_ID  (13)
#define L_P1__subcl18_ID  (15)
#define L_P1__subcl20_ID  (17)

// ID Comandi al piazzale
#define L_P1__subcl_ID  (4)
#define L_P1__subcl1_ID  (5)

// ID Comandi manuali
#define L_P1__event1_ID  (50)
#define L_P1__event2_ID  (52)
#define L_P1__event3_ID  (54)

// ID Risposte ai comandi manuali
#define L_P1__event5Reply_ID  (51)
#define L_P1__event6Reply_ID  (53)
#define L_P1__event7Reply_ID  (55)


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

/* bool L_P1__GetSubcl13(instance_id_t const my_id); */
#define L_P1__GetSubcl13(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl13_ID)
/* void L_P1__SetSubcl13(instance_id_t const my_id, bool const value); */
#define L_P1__SetSubcl13(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl13_ID, (Taggm) (value))

/* bool L_P1__GetSubcl15(instance_id_t const my_id); */
#define L_P1__GetSubcl15(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl15_ID)
/* void L_P1__SetSubcl15(instance_id_t const my_id, bool const value); */
#define L_P1__SetSubcl15(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl15_ID, (Taggm) (value))

/* bool L_P1__GetSubcl17(instance_id_t const my_id); */
#define L_P1__GetSubcl17(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl17_ID)
/* void L_P1__SetSubcl17(instance_id_t const my_id, bool const value); */
#define L_P1__SetSubcl17(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl17_ID, (Taggm) (value))

/* C2_Enumerat2 L_P1__GetSubcl19(instance_id_t const my_id); */
#define L_P1__GetSubcl19(my_id)  \
    (C2_Enumerat2) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl19_ID)
/* void L_P1__SetSubcl19(instance_id_t const my_id, C2_Enumerat2 const value); */
#define L_P1__SetSubcl19(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl19_ID, (Taggm) (value))

/* bool L_P1__GetSubcl21(instance_id_t const my_id); */
#define L_P1__GetSubcl21(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl21_ID)
/* void L_P1__SetSubcl21(instance_id_t const my_id, bool const value); */
#define L_P1__SetSubcl21(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl21_ID, (Taggm) (value))

/* Intero L_P1__GetSubcl22(instance_id_t const my_id); */
#define L_P1__GetSubcl22(my_id)  \
    (Intero) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl22_ID)
/* void L_P1__SetSubcl22(instance_id_t const my_id, Intero const value); */
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

/* C2_Enumerat4 L_P1__GetSubcl24(instance_id_t const my_id); */
#define L_P1__GetSubcl24(my_id)  \
    (C2_Enumerat4) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl24_ID)
/* void L_P1__SetSubcl24(instance_id_t const my_id, C2_Enumerat4 const value); */
#define L_P1__SetSubcl24(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl24_ID, (Taggm) (value))

/* C2_Enumerat4 L_P1__GetSubcl25(instance_id_t const my_id); */
#define L_P1__GetSubcl25(my_id)  \
    (C2_Enumerat4) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl25_ID)
/* void L_P1__SetSubcl25(instance_id_t const my_id, C2_Enumerat4 const value); */
#define L_P1__SetSubcl25(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl25_ID, (Taggm) (value))

/* Intero L_P1__GetSubcl26(instance_id_t const my_id); */
#define L_P1__GetSubcl26(my_id)  \
    (Intero) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl26_ID)
/* void L_P1__SetSubcl26(instance_id_t const my_id, Intero const value); */
#define L_P1__SetSubcl26(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl26_ID, (Taggm) (value))

/* Intero L_P1__GetSubcl27(instance_id_t const my_id); */
#define L_P1__GetSubcl27(my_id)  \
    (Intero) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl27_ID)
/* void L_P1__SetSubcl27(instance_id_t const my_id, Intero const value); */
#define L_P1__SetSubcl27(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl27_ID, (Taggm) (value))

/* C2_Enumerat2 L_P1__GetSubcl28(instance_id_t const my_id); */
#define L_P1__GetSubcl28(my_id)  \
    (C2_Enumerat2) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl28_ID)
/* void L_P1__SetSubcl28(instance_id_t const my_id, C2_Enumerat2 const value); */
#define L_P1__SetSubcl28(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl28_ID, (Taggm) (value))

/* C2_Enumerat2 L_P1__GetSubcl29(instance_id_t const my_id); */
#define L_P1__GetSubcl29(my_id)  \
    (C2_Enumerat2) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl29_ID)
/* void L_P1__SetSubcl29(instance_id_t const my_id, C2_Enumerat2 const value); */
#define L_P1__SetSubcl29(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl29_ID, (Taggm) (value))

/* Intero L_P1__GetSubcl30(instance_id_t const my_id); */
#define L_P1__GetSubcl30(my_id)  \
    (Intero) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl30_ID)
/* void L_P1__SetSubcl30(instance_id_t const my_id, Intero const value); */
#define L_P1__SetSubcl30(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl30_ID, (Taggm) (value))

/* Intero L_P1__GetSubcl31(instance_id_t const my_id); */
#define L_P1__GetSubcl31(my_id)  \
    (Intero) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl31_ID)
/* void L_P1__SetSubcl31(instance_id_t const my_id, Intero const value); */
#define L_P1__SetSubcl31(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl31_ID, (Taggm) (value))

/* C2_Enumerat3 L_P1__GetSubcl32(instance_id_t const my_id); */
#define L_P1__GetSubcl32(my_id)  \
    (C2_Enumerat3) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl32_ID)
/* void L_P1__SetSubcl32(instance_id_t const my_id, C2_Enumerat3 const value); */
#define L_P1__SetSubcl32(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl32_ID, (Taggm) (value))

/* C2_Enumerat3 L_P1__GetSubcl33(instance_id_t const my_id); */
#define L_P1__GetSubcl33(my_id)  \
    (C2_Enumerat3) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl33_ID)
/* void L_P1__SetSubcl33(instance_id_t const my_id, C2_Enumerat3 const value); */
#define L_P1__SetSubcl33(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl33_ID, (Taggm) (value))

/* Intero L_P1__GetSubcl34(instance_id_t const my_id); */
#define L_P1__GetSubcl34(my_id)  \
    (Intero) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl34_ID)
/* void L_P1__SetSubcl34(instance_id_t const my_id, Intero const value); */
#define L_P1__SetSubcl34(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl34_ID, (Taggm) (value))

/* Intero L_P1__GetSubcl35(instance_id_t const my_id); */
#define L_P1__GetSubcl35(my_id)  \
    (Intero) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl35_ID)
/* void L_P1__SetSubcl35(instance_id_t const my_id, Intero const value); */
#define L_P1__SetSubcl35(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl35_ID, (Taggm) (value))

/* C2_Enumerat4 L_P1__GetSubcl36(instance_id_t const my_id); */
#define L_P1__GetSubcl36(my_id)  \
    (C2_Enumerat4) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl36_ID)
/* void L_P1__SetSubcl36(instance_id_t const my_id, C2_Enumerat4 const value); */
#define L_P1__SetSubcl36(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl36_ID, (Taggm) (value))


// timer
Timer* L_P1__GetSubcl37(instance_id_t const my_id);
Timer* L_P1__GetSubcl38(instance_id_t const my_id);
Timer* L_P1__GetSubcl39(instance_id_t const my_id);
Timer* L_P1__GetSubcl40(instance_id_t const my_id);
Timer* L_P1__GetSubcl41(instance_id_t const my_id);
Timer* L_P1__GetSubcl42(instance_id_t const my_id);
Timer* L_P1__GetSubcl43(instance_id_t const my_id);
Timer* L_P1__GetSubcl44(instance_id_t const my_id);
Timer* L_P1__GetSubcl45(instance_id_t const my_id);
Timer* L_P1__GetSubcl46(instance_id_t const my_id);
Timer* L_P1__GetSubcl47(instance_id_t const my_id);
Timer* L_P1__GetSubcl48(instance_id_t const my_id);
Timer* L_P1__GetSubcl49(instance_id_t const my_id);

// counter
Counter* L_P1__GetSubcl50(instance_id_t const my_id);    
Counter* L_P1__GetSubcl51(instance_id_t const my_id);    
Counter* L_P1__GetSubcl52(instance_id_t const my_id);    

// comandi manuali
/* bool L_P1__GetInEvent1(instance_id_t const my_id); */
#define L_P1__GetInEvent1(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__event1_ID)
/* bool L_P1__GetInEvent2(instance_id_t const my_id); */
#define L_P1__GetInEvent2(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__event2_ID)
/* bool L_P1__GetInEvent3(instance_id_t const my_id); */
#define L_P1__GetInEvent3(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__event3_ID)

// risposte ai comandi manuali
/* void L_P1__SetOutEvent5(instance_id_t const my_id, ManCmdResponse const value); */
#define L_P1__SetOutEvent5(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__event5Reply_ID, (Taggm) (value))
/* void L_P1__SetOutEvent6(instance_id_t const my_id, ManCmdResponse const value); */
#define L_P1__SetOutEvent6(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__event6Reply_ID, (Taggm) (value))
/* void L_P1__SetOutEvent7(instance_id_t const my_id, ManCmdResponse const value); */
#define L_P1__SetOutEvent7(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__event7Reply_ID, (Taggm) (value))

// controlli dal piazzale
/* bool L_P1__GetInConsd1(instance_id_t const my_id); */
#define L_P1__GetInConsd1(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__consd1_ID)
/* C2_Enumerat3 L_P1__GetInSubcl2(instance_id_t const my_id); */
#define L_P1__GetInSubcl2(my_id)  \
    (C2_Enumerat3) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl2_ID)
/* C2_Enumerat1 L_P1__GetInSubcl3(instance_id_t const my_id); */
#define L_P1__GetInSubcl3(my_id)  \
    (C2_Enumerat1) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl3_ID)
/* bool L_P1__GetInSubcl4(instance_id_t const my_id); */
#define L_P1__GetInSubcl4(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl4_ID)
/* bool L_P1__GetInSubcl12(instance_id_t const my_id); */
#define L_P1__GetInSubcl12(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl12_ID)
/* bool L_P1__GetInSubcl14(instance_id_t const my_id); */
#define L_P1__GetInSubcl14(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl14_ID)
/* bool L_P1__GetInSubcl16(instance_id_t const my_id); */
#define L_P1__GetInSubcl16(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl16_ID)
/* C2_Enumerat2 L_P1__GetInSubcl18(instance_id_t const my_id); */
#define L_P1__GetInSubcl18(my_id)  \
    (C2_Enumerat2) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl18_ID)
/* bool L_P1__GetInSubcl20(instance_id_t const my_id); */
#define L_P1__GetInSubcl20(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl20_ID)

// comandi al piazzale
/* void L_P1__SetOutSubcl(instance_id_t const my_id, C2_Enumerat2 const value); */
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
void L_P1__Macro5(instance_id_t const my_id );
void L_P1__Macro6(instance_id_t const my_id );
void L_P1__Macro7(instance_id_t const my_id );
void L_P1__Macro8(instance_id_t const my_id , C2_Enumerat3 argom23, C2_Enumerat2 argom24);

// Macro di verifica
bool L_P1__Macro14(instance_id_t const my_id , C2_Enumerat3 argom42, C2_Enumerat2 argom43, C2_Enumerat2 argom44, bool argom45, C2_Enumerat1 argom46, C2_Enumerat4 argom47);

// Macro valorizzate
bool L_P1__Macro9(instance_id_t const my_id , bool argom25, C2_Enumerat1 argom26, C2_Enumerat1 argom27);
bool L_P1__Macro10(instance_id_t const my_id , C2_Enumerat1 argom28, C2_Enumerat4 argom29, bool argom30);
C2_Enumerat2 L_P1__Macro11(instance_id_t const my_id , C2_Enumerat4 argom31, C2_Enumerat1 argom32, bool argom33, C2_Enumerat4 argom34, C2_Enumerat2 argom35, C2_Enumerat4 argom36);
C2_Enumerat1 L_P1__Macro12(instance_id_t const my_id , C2_Enumerat3 argom37, C2_Enumerat4 argom38, C2_Enumerat1 argom39);
bool L_P1__Macro13(instance_id_t const my_id , C2_Enumerat2 argom40, bool argom41);


#endif // LIBSTAZIONE_CLASSEL_P1_C2_H
