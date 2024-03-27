// Codice del modello 'TestCase11', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#ifndef LIBSTAZIONE_CLASSEL_P1_C2_H
#define LIBSTAZIONE_CLASSEL_P1_C2_H

#include "envdt.h"
#include "Timer.h"
#include "Counter.h"


// ********** Comandi manuali e relative risposte **********



#define L_P1_C2_NUM_COMANDI_MAN 0


// ********** Informazioni per AGGM **********

#define CLASS_L_P1_C2_ID  2

#define L_P1_C2_State_ID  (1)

// ID Variabili
#define L_P1__stato3_ID  (3)
#define L_P1__subcl14_ID  (14)
#define L_P1__subcl16_ID  (16)
#define L_P1__subcl17_ID  (17)
#define L_P1__subcl18_ID  (18)
#define L_P1__subcl19_ID  (19)
#define L_P1__subcl20_ID  (20)
#define L_P1__subcl21_ID  (21)
#define L_P1__subcl22_ID  (22)
#define L_P1__subcl23_ID  (23)
#define L_P1__subcl24_ID  (24)
#define L_P1__subcl25_ID  (25)
#define L_P1__subcl26_ID  (26)
#define L_P1__subcl27_ID  (27)
#define L_P1__subcl28_ID  (28)

// ID Timer
#define L_P1__subcl29_ID  (30)
#define L_P1__subcl30_ID  (29)
#define L_P1__subcl31_ID  (32)
#define L_P1__subcl32_ID  (31)
#define L_P1__subcl33_ID  (34)
#define L_P1__subcl34_ID  (33)
#define L_P1__subcl35_ID  (35)
#define L_P1__subcl36_ID  (36)
#define L_P1__subcl37_ID  (37)
#define L_P1__subcl38_ID  (38)
#define L_P1__subcl39_ID  (39)

// ID Counter
#define L_P1__subcl40_ID  (40)
#define L_P1__subcl41_ID  (41)
#define L_P1__subcl42_ID  (42)

// ID Controlli dal piazzale
#define L_P1__consd1_ID  (2)
#define L_P1__subcl4_ID  (8)
#define L_P1__subcl5_ID  (9)
#define L_P1__subcl6_ID  (10)
#define L_P1__subcl7_ID  (11)
#define L_P1__subcl8_ID  (12)
#define L_P1__subcl13_ID  (13)
#define L_P1__subcl15_ID  (15)

// ID Comandi al piazzale
#define L_P1__subcl_ID  (4)
#define L_P1__subcl1_ID  (5)
#define L_P1__subcl2_ID  (6)
#define L_P1__subcl3_ID  (7)

// ID Comandi manuali

// ID Risposte ai comandi manuali


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

/* C2_Enumerat4 L_P1__GetSubcl14(instance_id_t const my_id); */
#define L_P1__GetSubcl14(my_id)  \
    (C2_Enumerat4) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl14_ID)
/* void L_P1__SetSubcl14(instance_id_t const my_id, C2_Enumerat4 const value); */
#define L_P1__SetSubcl14(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl14_ID, (Taggm) (value))

/* bool L_P1__GetSubcl16(instance_id_t const my_id); */
#define L_P1__GetSubcl16(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl16_ID)
/* void L_P1__SetSubcl16(instance_id_t const my_id, bool const value); */
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

/* C2_Enumerat3 L_P1__GetSubcl21(instance_id_t const my_id); */
#define L_P1__GetSubcl21(my_id)  \
    (C2_Enumerat3) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl21_ID)
/* void L_P1__SetSubcl21(instance_id_t const my_id, C2_Enumerat3 const value); */
#define L_P1__SetSubcl21(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl21_ID, (Taggm) (value))

/* C2_Enumerat3 L_P1__GetSubcl22(instance_id_t const my_id); */
#define L_P1__GetSubcl22(my_id)  \
    (C2_Enumerat3) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl22_ID)
/* void L_P1__SetSubcl22(instance_id_t const my_id, C2_Enumerat3 const value); */
#define L_P1__SetSubcl22(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl22_ID, (Taggm) (value))

/* bool L_P1__GetSubcl23(instance_id_t const my_id); */
#define L_P1__GetSubcl23(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl23_ID)
/* void L_P1__SetSubcl23(instance_id_t const my_id, bool const value); */
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

/* C2_Enumerat1 L_P1__GetSubcl25(instance_id_t const my_id); */
#define L_P1__GetSubcl25(my_id)  \
    (C2_Enumerat1) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl25_ID)
/* void L_P1__SetSubcl25(instance_id_t const my_id, C2_Enumerat1 const value); */
#define L_P1__SetSubcl25(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl25_ID, (Taggm) (value))

/* C2_Enumerat1 L_P1__GetSubcl26(instance_id_t const my_id); */
#define L_P1__GetSubcl26(my_id)  \
    (C2_Enumerat1) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl26_ID)
/* void L_P1__SetSubcl26(instance_id_t const my_id, C2_Enumerat1 const value); */
#define L_P1__SetSubcl26(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl26_ID, (Taggm) (value))

/* bool L_P1__GetSubcl27(instance_id_t const my_id); */
#define L_P1__GetSubcl27(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl27_ID)
/* void L_P1__SetSubcl27(instance_id_t const my_id, bool const value); */
#define L_P1__SetSubcl27(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl27_ID, (Taggm) (value))

/* Intero L_P1__GetSubcl28(instance_id_t const my_id); */
#define L_P1__GetSubcl28(my_id)  \
    (Intero) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl28_ID)
/* void L_P1__SetSubcl28(instance_id_t const my_id, Intero const value); */
#define L_P1__SetSubcl28(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl28_ID, (Taggm) (value))


// timer
Timer* L_P1__GetSubcl29(instance_id_t const my_id);
Timer* L_P1__GetSubcl30(instance_id_t const my_id);
Timer* L_P1__GetSubcl31(instance_id_t const my_id);
Timer* L_P1__GetSubcl32(instance_id_t const my_id);
Timer* L_P1__GetSubcl33(instance_id_t const my_id);
Timer* L_P1__GetSubcl34(instance_id_t const my_id);
Timer* L_P1__GetSubcl35(instance_id_t const my_id);
Timer* L_P1__GetSubcl36(instance_id_t const my_id);
Timer* L_P1__GetSubcl37(instance_id_t const my_id);
Timer* L_P1__GetSubcl38(instance_id_t const my_id);
Timer* L_P1__GetSubcl39(instance_id_t const my_id);

// counter
Counter* L_P1__GetSubcl40(instance_id_t const my_id);    
Counter* L_P1__GetSubcl41(instance_id_t const my_id);    
Counter* L_P1__GetSubcl42(instance_id_t const my_id);    

// comandi manuali

// risposte ai comandi manuali

// controlli dal piazzale
/* bool L_P1__GetInConsd1(instance_id_t const my_id); */
#define L_P1__GetInConsd1(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__consd1_ID)
/* bool L_P1__GetInSubcl4(instance_id_t const my_id); */
#define L_P1__GetInSubcl4(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl4_ID)
/* bool L_P1__GetInSubcl5(instance_id_t const my_id); */
#define L_P1__GetInSubcl5(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl5_ID)
/* bool L_P1__GetInSubcl6(instance_id_t const my_id); */
#define L_P1__GetInSubcl6(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl6_ID)
/* C2_Enumerat1 L_P1__GetInSubcl7(instance_id_t const my_id); */
#define L_P1__GetInSubcl7(my_id)  \
    (C2_Enumerat1) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl7_ID)
/* bool L_P1__GetInSubcl8(instance_id_t const my_id); */
#define L_P1__GetInSubcl8(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl8_ID)
/* C2_Enumerat4 L_P1__GetInSubcl13(instance_id_t const my_id); */
#define L_P1__GetInSubcl13(my_id)  \
    (C2_Enumerat4) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl13_ID)
/* bool L_P1__GetInSubcl15(instance_id_t const my_id); */
#define L_P1__GetInSubcl15(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl15_ID)

// comandi al piazzale
/* void L_P1__SetOutSubcl(instance_id_t const my_id, C2_Enumerat2 const value); */
#define L_P1__SetOutSubcl(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl_ID, (Taggm) (value))

/* void L_P1__SetOutSubcl1(instance_id_t const my_id, bool const value); */
#define L_P1__SetOutSubcl1(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl1_ID, (Taggm) (value))

/* void L_P1__SetOutSubcl2(instance_id_t const my_id, bool const value); */
#define L_P1__SetOutSubcl2(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl2_ID, (Taggm) (value))

/* void L_P1__SetOutSubcl3(instance_id_t const my_id, bool const value); */
#define L_P1__SetOutSubcl3(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C2_ID, (my_id), L_P1__subcl3_ID, (Taggm) (value))


// ********** Metodi standard **********

void L_P1_C2_Init(instance_id_t const my_id);

void L_P1_C2_Exec(instance_id_t const my_id, Phase const p);

ExecResponse L_P1_C2_GExec(global_id_t const proc_id, Phase const p);

void L_P1_C2_GTick(global_id_t const proc_id);

void L_P1_C2_GSetSafe(global_id_t const proc_id);

void L_P1_C2_GUpdatePrev(global_id_t const proc_id);

// ********** Altri metodi pubblici**********

// Macro di effetto
void L_P1__Macro10(instance_id_t const my_id );
void L_P1__Macro11(instance_id_t const my_id );
void L_P1__Macro12(instance_id_t const my_id );
void L_P1__Macro13(instance_id_t const my_id );
void L_P1__Macro14(instance_id_t const my_id , C2_Enumerat1 argom32, bool argom33, C2_Enumerat3 argom34, C2_Enumerat4 argom35, C2_Enumerat3 argom36, C2_Enumerat3 argom37, C2_Enumerat1 argom38);

// Macro di verifica
bool L_P1__Macro19(instance_id_t const my_id );
bool L_P1__Macro20(instance_id_t const my_id , bool argom58, C2_Enumerat4 argom59, C2_Enumerat4 argom60, bool argom61);
bool L_P1__Macro21(instance_id_t const my_id , C2_Enumerat2 argom62, C2_Enumerat2 argom63, C2_Enumerat3 argom64, C2_Enumerat2 argom65, bool argom66);
bool L_P1__Macro22(instance_id_t const my_id , bool argom67, bool argom68, C2_Enumerat1 argom69, C2_Enumerat4 argom70);

// Macro valorizzate
bool L_P1__Macro15(instance_id_t const my_id , C2_Enumerat3 argom39, C2_Enumerat4 argom40, C2_Enumerat1 argom41);
bool L_P1__Macro16(instance_id_t const my_id , C2_Enumerat1 argom42, C2_Enumerat3 argom43, C2_Enumerat4 argom44, C2_Enumerat4 argom45, C2_Enumerat1 argom46);
C2_Enumerat2 L_P1__Macro17(instance_id_t const my_id , C2_Enumerat4 argom47, C2_Enumerat2 argom48, C2_Enumerat2 argom49, bool argom50);
bool L_P1__Macro18(instance_id_t const my_id , C2_Enumerat3 argom51, C2_Enumerat3 argom52, C2_Enumerat4 argom53, C2_Enumerat4 argom54, bool argom55, C2_Enumerat4 argom56, C2_Enumerat1 argom57);


#endif // LIBSTAZIONE_CLASSEL_P1_C2_H
