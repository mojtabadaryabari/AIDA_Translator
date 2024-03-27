// Codice del modello 'TestCase11', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#ifndef LIBSTAZIONE_CLASSEL_P1_C4_H
#define LIBSTAZIONE_CLASSEL_P1_C4_H

#include "envdt.h"
#include "Timer.h"
#include "Counter.h"


// ********** Comandi manuali e relative risposte **********



#define L_P1_C4_NUM_COMANDI_MAN 0


// ********** Informazioni per AGGM **********

#define CLASS_L_P1_C4_ID  4

#define L_P1_C4_State_ID  (1)

// ID Variabili
#define L_P1__stato7_ID  (3)
#define L_P1__subcl100_ID  (12)
#define L_P1__subcl102_ID  (14)
#define L_P1__subcl104_ID  (16)
#define L_P1__subcl105_ID  (17)
#define L_P1__subcl106_ID  (18)
#define L_P1__subcl107_ID  (19)
#define L_P1__subcl108_ID  (20)
#define L_P1__subcl109_ID  (21)
#define L_P1__subcl110_ID  (22)
#define L_P1__subcl111_ID  (23)
#define L_P1__subcl112_ID  (24)
#define L_P1__subcl113_ID  (25)

// ID Timer
#define L_P1__subcl114_ID  (27)
#define L_P1__subcl115_ID  (26)
#define L_P1__subcl116_ID  (29)
#define L_P1__subcl117_ID  (28)
#define L_P1__subcl118_ID  (31)
#define L_P1__subcl119_ID  (30)
#define L_P1__subcl120_ID  (33)
#define L_P1__subcl121_ID  (32)
#define L_P1__subcl122_ID  (34)
#define L_P1__subcl123_ID  (35)
#define L_P1__subcl124_ID  (36)

// ID Counter
#define L_P1__subcl125_ID  (37)
#define L_P1__subcl126_ID  (38)

// ID Controlli dal piazzale
#define L_P1__consd3_ID  (2)
#define L_P1__subcl91_ID  (7)
#define L_P1__subcl92_ID  (8)
#define L_P1__subcl93_ID  (9)
#define L_P1__subcl94_ID  (10)
#define L_P1__subcl99_ID  (11)
#define L_P1__subcl101_ID  (13)
#define L_P1__subcl103_ID  (15)

// ID Comandi al piazzale
#define L_P1__subcl88_ID  (4)
#define L_P1__subcl89_ID  (5)
#define L_P1__subcl90_ID  (6)

// ID Comandi manuali

// ID Risposte ai comandi manuali


// ********** Getter/setter pubblici **********

/* C4_Stateenu L_P1_C4_GetState(instance_id_t const my_id) */
#define L_P1_C4_GetState(my_id)  \
    (C4_Stateenu) \
    LogicGetAggmVar(CLASS_L_P1_C4_ID, (my_id), L_P1_C4_State_ID)

/* void L_P1_C4_SetState(instance_id_t const my_id, C4_Stateenu const value) */
#define L_P1_C4_SetState(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C4_ID, (my_id), L_P1_C4_State_ID, (Taggm) (value))

// variabili
/* C4_Stateenu L_P1__GetStato7(instance_id_t const my_id); */
#define L_P1__GetStato7(my_id)  \
    (C4_Stateenu) \
    LogicGetAggmVar(CLASS_L_P1_C4_ID, (my_id), L_P1__stato7_ID)
/* void L_P1__SetStato7(instance_id_t const my_id, C4_Stateenu const value); */
#define L_P1__SetStato7(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C4_ID, (my_id), L_P1__stato7_ID, (Taggm) (value))

/* bool L_P1__GetSubcl100(instance_id_t const my_id); */
#define L_P1__GetSubcl100(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C4_ID, (my_id), L_P1__subcl100_ID)
/* void L_P1__SetSubcl100(instance_id_t const my_id, bool const value); */
#define L_P1__SetSubcl100(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C4_ID, (my_id), L_P1__subcl100_ID, (Taggm) (value))

/* C4_Enumerat4 L_P1__GetSubcl102(instance_id_t const my_id); */
#define L_P1__GetSubcl102(my_id)  \
    (C4_Enumerat4) \
    LogicGetAggmVar(CLASS_L_P1_C4_ID, (my_id), L_P1__subcl102_ID)
/* void L_P1__SetSubcl102(instance_id_t const my_id, C4_Enumerat4 const value); */
#define L_P1__SetSubcl102(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C4_ID, (my_id), L_P1__subcl102_ID, (Taggm) (value))

/* C4_Enumerat2 L_P1__GetSubcl104(instance_id_t const my_id); */
#define L_P1__GetSubcl104(my_id)  \
    (C4_Enumerat2) \
    LogicGetAggmVar(CLASS_L_P1_C4_ID, (my_id), L_P1__subcl104_ID)
/* void L_P1__SetSubcl104(instance_id_t const my_id, C4_Enumerat2 const value); */
#define L_P1__SetSubcl104(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C4_ID, (my_id), L_P1__subcl104_ID, (Taggm) (value))

/* bool L_P1__GetSubcl105(instance_id_t const my_id); */
#define L_P1__GetSubcl105(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C4_ID, (my_id), L_P1__subcl105_ID)
/* void L_P1__SetSubcl105(instance_id_t const my_id, bool const value); */
#define L_P1__SetSubcl105(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C4_ID, (my_id), L_P1__subcl105_ID, (Taggm) (value))

/* bool L_P1__GetSubcl106(instance_id_t const my_id); */
#define L_P1__GetSubcl106(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C4_ID, (my_id), L_P1__subcl106_ID)
/* void L_P1__SetSubcl106(instance_id_t const my_id, bool const value); */
#define L_P1__SetSubcl106(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C4_ID, (my_id), L_P1__subcl106_ID, (Taggm) (value))

/* Intero L_P1__GetSubcl107(instance_id_t const my_id); */
#define L_P1__GetSubcl107(my_id)  \
    (Intero) \
    LogicGetAggmVar(CLASS_L_P1_C4_ID, (my_id), L_P1__subcl107_ID)
/* void L_P1__SetSubcl107(instance_id_t const my_id, Intero const value); */
#define L_P1__SetSubcl107(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C4_ID, (my_id), L_P1__subcl107_ID, (Taggm) (value))

/* Intero L_P1__GetSubcl108(instance_id_t const my_id); */
#define L_P1__GetSubcl108(my_id)  \
    (Intero) \
    LogicGetAggmVar(CLASS_L_P1_C4_ID, (my_id), L_P1__subcl108_ID)
/* void L_P1__SetSubcl108(instance_id_t const my_id, Intero const value); */
#define L_P1__SetSubcl108(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C4_ID, (my_id), L_P1__subcl108_ID, (Taggm) (value))

/* Intero L_P1__GetSubcl109(instance_id_t const my_id); */
#define L_P1__GetSubcl109(my_id)  \
    (Intero) \
    LogicGetAggmVar(CLASS_L_P1_C4_ID, (my_id), L_P1__subcl109_ID)
/* void L_P1__SetSubcl109(instance_id_t const my_id, Intero const value); */
#define L_P1__SetSubcl109(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C4_ID, (my_id), L_P1__subcl109_ID, (Taggm) (value))

/* Intero L_P1__GetSubcl110(instance_id_t const my_id); */
#define L_P1__GetSubcl110(my_id)  \
    (Intero) \
    LogicGetAggmVar(CLASS_L_P1_C4_ID, (my_id), L_P1__subcl110_ID)
/* void L_P1__SetSubcl110(instance_id_t const my_id, Intero const value); */
#define L_P1__SetSubcl110(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C4_ID, (my_id), L_P1__subcl110_ID, (Taggm) (value))

/* bool L_P1__GetSubcl111(instance_id_t const my_id); */
#define L_P1__GetSubcl111(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C4_ID, (my_id), L_P1__subcl111_ID)
/* void L_P1__SetSubcl111(instance_id_t const my_id, bool const value); */
#define L_P1__SetSubcl111(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C4_ID, (my_id), L_P1__subcl111_ID, (Taggm) (value))

/* bool L_P1__GetSubcl112(instance_id_t const my_id); */
#define L_P1__GetSubcl112(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C4_ID, (my_id), L_P1__subcl112_ID)
/* void L_P1__SetSubcl112(instance_id_t const my_id, bool const value); */
#define L_P1__SetSubcl112(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C4_ID, (my_id), L_P1__subcl112_ID, (Taggm) (value))

/* C4_Enumerat3 L_P1__GetSubcl113(instance_id_t const my_id); */
#define L_P1__GetSubcl113(my_id)  \
    (C4_Enumerat3) \
    LogicGetAggmVar(CLASS_L_P1_C4_ID, (my_id), L_P1__subcl113_ID)
/* void L_P1__SetSubcl113(instance_id_t const my_id, C4_Enumerat3 const value); */
#define L_P1__SetSubcl113(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C4_ID, (my_id), L_P1__subcl113_ID, (Taggm) (value))


// timer
Timer* L_P1__GetSubcl114(instance_id_t const my_id);
Timer* L_P1__GetSubcl115(instance_id_t const my_id);
Timer* L_P1__GetSubcl116(instance_id_t const my_id);
Timer* L_P1__GetSubcl117(instance_id_t const my_id);
Timer* L_P1__GetSubcl118(instance_id_t const my_id);
Timer* L_P1__GetSubcl119(instance_id_t const my_id);
Timer* L_P1__GetSubcl120(instance_id_t const my_id);
Timer* L_P1__GetSubcl121(instance_id_t const my_id);
Timer* L_P1__GetSubcl122(instance_id_t const my_id);
Timer* L_P1__GetSubcl123(instance_id_t const my_id);
Timer* L_P1__GetSubcl124(instance_id_t const my_id);

// counter
Counter* L_P1__GetSubcl125(instance_id_t const my_id);    
Counter* L_P1__GetSubcl126(instance_id_t const my_id);    

// comandi manuali

// risposte ai comandi manuali

// controlli dal piazzale
/* bool L_P1__GetInConsd3(instance_id_t const my_id); */
#define L_P1__GetInConsd3(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C4_ID, (my_id), L_P1__consd3_ID)
/* bool L_P1__GetInSubcl91(instance_id_t const my_id); */
#define L_P1__GetInSubcl91(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C4_ID, (my_id), L_P1__subcl91_ID)
/* C4_Enumerat1 L_P1__GetInSubcl92(instance_id_t const my_id); */
#define L_P1__GetInSubcl92(my_id)  \
    (C4_Enumerat1) \
    LogicGetAggmVar(CLASS_L_P1_C4_ID, (my_id), L_P1__subcl92_ID)
/* bool L_P1__GetInSubcl93(instance_id_t const my_id); */
#define L_P1__GetInSubcl93(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C4_ID, (my_id), L_P1__subcl93_ID)
/* C4_Enumerat1 L_P1__GetInSubcl94(instance_id_t const my_id); */
#define L_P1__GetInSubcl94(my_id)  \
    (C4_Enumerat1) \
    LogicGetAggmVar(CLASS_L_P1_C4_ID, (my_id), L_P1__subcl94_ID)
/* bool L_P1__GetInSubcl99(instance_id_t const my_id); */
#define L_P1__GetInSubcl99(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C4_ID, (my_id), L_P1__subcl99_ID)
/* C4_Enumerat4 L_P1__GetInSubcl101(instance_id_t const my_id); */
#define L_P1__GetInSubcl101(my_id)  \
    (C4_Enumerat4) \
    LogicGetAggmVar(CLASS_L_P1_C4_ID, (my_id), L_P1__subcl101_ID)
/* C4_Enumerat2 L_P1__GetInSubcl103(instance_id_t const my_id); */
#define L_P1__GetInSubcl103(my_id)  \
    (C4_Enumerat2) \
    LogicGetAggmVar(CLASS_L_P1_C4_ID, (my_id), L_P1__subcl103_ID)

// comandi al piazzale
/* void L_P1__SetOutSubcl88(instance_id_t const my_id, bool const value); */
#define L_P1__SetOutSubcl88(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C4_ID, (my_id), L_P1__subcl88_ID, (Taggm) (value))

/* void L_P1__SetOutSubcl89(instance_id_t const my_id, bool const value); */
#define L_P1__SetOutSubcl89(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C4_ID, (my_id), L_P1__subcl89_ID, (Taggm) (value))

/* void L_P1__SetOutSubcl90(instance_id_t const my_id, C4_Enumerat1 const value); */
#define L_P1__SetOutSubcl90(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C4_ID, (my_id), L_P1__subcl90_ID, (Taggm) (value))


// ********** Metodi standard **********

void L_P1_C4_Init(instance_id_t const my_id);

void L_P1_C4_Exec(instance_id_t const my_id, Phase const p);

ExecResponse L_P1_C4_GExec(global_id_t const proc_id, Phase const p);

void L_P1_C4_GTick(global_id_t const proc_id);

void L_P1_C4_GSetSafe(global_id_t const proc_id);

void L_P1_C4_GUpdatePrev(global_id_t const proc_id);

// ********** Altri metodi pubblici**********

// Macro di effetto
void L_P1__Macro31(instance_id_t const my_id );
void L_P1__Macro32(instance_id_t const my_id , C4_Enumerat3 argom90, bool argom91, C4_Enumerat2 argom92, C4_Enumerat3 argom93);

// Macro di verifica
bool L_P1__Macro35(instance_id_t const my_id , bool argom98, C4_Enumerat4 argom99, C4_Enumerat4 argom100, bool argom101);
bool L_P1__Macro36(instance_id_t const my_id , bool argom102, C4_Enumerat2 argom103, C4_Enumerat2 argom104, C4_Enumerat2 argom105, C4_Enumerat2 argom106, C4_Enumerat4 argom107);
bool L_P1__Macro37(instance_id_t const my_id );
bool L_P1__Macro38(instance_id_t const my_id , bool argom108, C4_Enumerat2 argom109, bool argom110, bool argom111);

// Macro valorizzate
C4_Enumerat2 L_P1__Macro33(instance_id_t const my_id , C4_Enumerat1 argom94, C4_Enumerat1 argom95, C4_Enumerat2 argom96, bool argom97);
C4_Enumerat2 L_P1__Macro34(instance_id_t const my_id );


#endif // LIBSTAZIONE_CLASSEL_P1_C4_H
