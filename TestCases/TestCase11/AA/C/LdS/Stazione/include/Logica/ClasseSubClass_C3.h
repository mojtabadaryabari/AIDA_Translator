// Codice del modello 'TestCase11', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#ifndef LIBSTAZIONE_CLASSEL_P1_C3_H
#define LIBSTAZIONE_CLASSEL_P1_C3_H

#include "envdt.h"
#include "Timer.h"
#include "Counter.h"


// ********** Comandi manuali e relative risposte **********

typedef struct {
    bool event9;
} L_P1_C3_Comandi_Man;

typedef struct {
    ManCmdResponse event10;
} L_P1_C3_Ack_Comandi_Man;

#define L_P1_C3_NUM_COMANDI_MAN 1


// ********** Informazioni per AGGM **********

#define CLASS_L_P1_C3_ID  3

#define L_P1_C3_State_ID  (1)

// ID Variabili
#define L_P1__stato5_ID  (3)
#define L_P1__subcl56_ID  (7)
#define L_P1__subcl58_ID  (9)
#define L_P1__subcl60_ID  (11)
#define L_P1__subcl62_ID  (13)
#define L_P1__subcl64_ID  (15)
#define L_P1__subcl65_ID  (16)
#define L_P1__subcl66_ID  (17)
#define L_P1__subcl67_ID  (18)
#define L_P1__subcl68_ID  (19)
#define L_P1__subcl69_ID  (20)
#define L_P1__subcl70_ID  (21)
#define L_P1__subcl71_ID  (22)
#define L_P1__subcl72_ID  (23)
#define L_P1__subcl73_ID  (24)
#define L_P1__subcl74_ID  (25)
#define L_P1__subcl75_ID  (26)
#define L_P1__subcl76_ID  (27)
#define L_P1__subcl77_ID  (28)
#define L_P1__subcl78_ID  (29)
#define L_P1__subcl79_ID  (30)

// ID Timer
#define L_P1__subcl80_ID  (32)
#define L_P1__subcl81_ID  (31)
#define L_P1__subcl82_ID  (34)
#define L_P1__subcl83_ID  (33)
#define L_P1__subcl84_ID  (35)
#define L_P1__subcl85_ID  (36)
#define L_P1__subcl86_ID  (37)

// ID Counter
#define L_P1__subcl87_ID  (38)

// ID Controlli dal piazzale
#define L_P1__consd2_ID  (2)
#define L_P1__subcl44_ID  (5)
#define L_P1__subcl55_ID  (6)
#define L_P1__subcl57_ID  (8)
#define L_P1__subcl59_ID  (10)
#define L_P1__subcl61_ID  (12)
#define L_P1__subcl63_ID  (14)

// ID Comandi al piazzale
#define L_P1__subcl43_ID  (4)

// ID Comandi manuali
#define L_P1__event9_ID  (39)

// ID Risposte ai comandi manuali
#define L_P1__event10Reply_ID  (40)


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

/* bool L_P1__GetSubcl56(instance_id_t const my_id); */
#define L_P1__GetSubcl56(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl56_ID)
/* void L_P1__SetSubcl56(instance_id_t const my_id, bool const value); */
#define L_P1__SetSubcl56(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl56_ID, (Taggm) (value))

/* C3_Enumerat3 L_P1__GetSubcl58(instance_id_t const my_id); */
#define L_P1__GetSubcl58(my_id)  \
    (C3_Enumerat3) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl58_ID)
/* void L_P1__SetSubcl58(instance_id_t const my_id, C3_Enumerat3 const value); */
#define L_P1__SetSubcl58(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl58_ID, (Taggm) (value))

/* bool L_P1__GetSubcl60(instance_id_t const my_id); */
#define L_P1__GetSubcl60(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl60_ID)
/* void L_P1__SetSubcl60(instance_id_t const my_id, bool const value); */
#define L_P1__SetSubcl60(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl60_ID, (Taggm) (value))

/* bool L_P1__GetSubcl62(instance_id_t const my_id); */
#define L_P1__GetSubcl62(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl62_ID)
/* void L_P1__SetSubcl62(instance_id_t const my_id, bool const value); */
#define L_P1__SetSubcl62(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl62_ID, (Taggm) (value))

/* bool L_P1__GetSubcl64(instance_id_t const my_id); */
#define L_P1__GetSubcl64(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl64_ID)
/* void L_P1__SetSubcl64(instance_id_t const my_id, bool const value); */
#define L_P1__SetSubcl64(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl64_ID, (Taggm) (value))

/* bool L_P1__GetSubcl65(instance_id_t const my_id); */
#define L_P1__GetSubcl65(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl65_ID)
/* void L_P1__SetSubcl65(instance_id_t const my_id, bool const value); */
#define L_P1__SetSubcl65(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl65_ID, (Taggm) (value))

/* bool L_P1__GetSubcl66(instance_id_t const my_id); */
#define L_P1__GetSubcl66(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl66_ID)
/* void L_P1__SetSubcl66(instance_id_t const my_id, bool const value); */
#define L_P1__SetSubcl66(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl66_ID, (Taggm) (value))

/* bool L_P1__GetSubcl67(instance_id_t const my_id); */
#define L_P1__GetSubcl67(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl67_ID)
/* void L_P1__SetSubcl67(instance_id_t const my_id, bool const value); */
#define L_P1__SetSubcl67(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl67_ID, (Taggm) (value))

/* bool L_P1__GetSubcl68(instance_id_t const my_id); */
#define L_P1__GetSubcl68(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl68_ID)
/* void L_P1__SetSubcl68(instance_id_t const my_id, bool const value); */
#define L_P1__SetSubcl68(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl68_ID, (Taggm) (value))

/* bool L_P1__GetSubcl69(instance_id_t const my_id); */
#define L_P1__GetSubcl69(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl69_ID)
/* void L_P1__SetSubcl69(instance_id_t const my_id, bool const value); */
#define L_P1__SetSubcl69(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl69_ID, (Taggm) (value))

/* bool L_P1__GetSubcl70(instance_id_t const my_id); */
#define L_P1__GetSubcl70(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl70_ID)
/* void L_P1__SetSubcl70(instance_id_t const my_id, bool const value); */
#define L_P1__SetSubcl70(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl70_ID, (Taggm) (value))

/* C3_Enumerat2 L_P1__GetSubcl71(instance_id_t const my_id); */
#define L_P1__GetSubcl71(my_id)  \
    (C3_Enumerat2) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl71_ID)
/* void L_P1__SetSubcl71(instance_id_t const my_id, C3_Enumerat2 const value); */
#define L_P1__SetSubcl71(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl71_ID, (Taggm) (value))

/* C3_Enumerat2 L_P1__GetSubcl72(instance_id_t const my_id); */
#define L_P1__GetSubcl72(my_id)  \
    (C3_Enumerat2) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl72_ID)
/* void L_P1__SetSubcl72(instance_id_t const my_id, C3_Enumerat2 const value); */
#define L_P1__SetSubcl72(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl72_ID, (Taggm) (value))

/* bool L_P1__GetSubcl73(instance_id_t const my_id); */
#define L_P1__GetSubcl73(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl73_ID)
/* void L_P1__SetSubcl73(instance_id_t const my_id, bool const value); */
#define L_P1__SetSubcl73(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl73_ID, (Taggm) (value))

/* bool L_P1__GetSubcl74(instance_id_t const my_id); */
#define L_P1__GetSubcl74(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl74_ID)
/* void L_P1__SetSubcl74(instance_id_t const my_id, bool const value); */
#define L_P1__SetSubcl74(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl74_ID, (Taggm) (value))

/* C3_Enumerat1 L_P1__GetSubcl75(instance_id_t const my_id); */
#define L_P1__GetSubcl75(my_id)  \
    (C3_Enumerat1) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl75_ID)
/* void L_P1__SetSubcl75(instance_id_t const my_id, C3_Enumerat1 const value); */
#define L_P1__SetSubcl75(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl75_ID, (Taggm) (value))

/* C3_Enumerat1 L_P1__GetSubcl76(instance_id_t const my_id); */
#define L_P1__GetSubcl76(my_id)  \
    (C3_Enumerat1) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl76_ID)
/* void L_P1__SetSubcl76(instance_id_t const my_id, C3_Enumerat1 const value); */
#define L_P1__SetSubcl76(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl76_ID, (Taggm) (value))

/* C3_Enumerat1 L_P1__GetSubcl77(instance_id_t const my_id); */
#define L_P1__GetSubcl77(my_id)  \
    (C3_Enumerat1) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl77_ID)
/* void L_P1__SetSubcl77(instance_id_t const my_id, C3_Enumerat1 const value); */
#define L_P1__SetSubcl77(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl77_ID, (Taggm) (value))

/* C3_Enumerat1 L_P1__GetSubcl78(instance_id_t const my_id); */
#define L_P1__GetSubcl78(my_id)  \
    (C3_Enumerat1) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl78_ID)
/* void L_P1__SetSubcl78(instance_id_t const my_id, C3_Enumerat1 const value); */
#define L_P1__SetSubcl78(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl78_ID, (Taggm) (value))

/* Intero L_P1__GetSubcl79(instance_id_t const my_id); */
#define L_P1__GetSubcl79(my_id)  \
    (Intero) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl79_ID)
/* void L_P1__SetSubcl79(instance_id_t const my_id, Intero const value); */
#define L_P1__SetSubcl79(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl79_ID, (Taggm) (value))


// timer
Timer* L_P1__GetSubcl80(instance_id_t const my_id);
Timer* L_P1__GetSubcl81(instance_id_t const my_id);
Timer* L_P1__GetSubcl82(instance_id_t const my_id);
Timer* L_P1__GetSubcl83(instance_id_t const my_id);
Timer* L_P1__GetSubcl84(instance_id_t const my_id);
Timer* L_P1__GetSubcl85(instance_id_t const my_id);
Timer* L_P1__GetSubcl86(instance_id_t const my_id);

// counter
Counter* L_P1__GetSubcl87(instance_id_t const my_id);    

// comandi manuali
/* bool L_P1__GetInEvent9(instance_id_t const my_id); */
#define L_P1__GetInEvent9(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__event9_ID)

// risposte ai comandi manuali
/* void L_P1__SetOutEvent10(instance_id_t const my_id, ManCmdResponse const value); */
#define L_P1__SetOutEvent10(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__event10Reply_ID, (Taggm) (value))

// controlli dal piazzale
/* bool L_P1__GetInConsd2(instance_id_t const my_id); */
#define L_P1__GetInConsd2(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__consd2_ID)
/* bool L_P1__GetInSubcl44(instance_id_t const my_id); */
#define L_P1__GetInSubcl44(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl44_ID)
/* bool L_P1__GetInSubcl55(instance_id_t const my_id); */
#define L_P1__GetInSubcl55(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl55_ID)
/* C3_Enumerat3 L_P1__GetInSubcl57(instance_id_t const my_id); */
#define L_P1__GetInSubcl57(my_id)  \
    (C3_Enumerat3) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl57_ID)
/* bool L_P1__GetInSubcl59(instance_id_t const my_id); */
#define L_P1__GetInSubcl59(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl59_ID)
/* bool L_P1__GetInSubcl61(instance_id_t const my_id); */
#define L_P1__GetInSubcl61(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl61_ID)
/* bool L_P1__GetInSubcl63(instance_id_t const my_id); */
#define L_P1__GetInSubcl63(my_id)  \
    (bool) \
    LogicGetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl63_ID)

// comandi al piazzale
/* void L_P1__SetOutSubcl43(instance_id_t const my_id, bool const value); */
#define L_P1__SetOutSubcl43(my_id, value)  \
    CHECK_LE((value), TAGGM_MAX); \
    LogicSetAggmVar(CLASS_L_P1_C3_ID, (my_id), L_P1__subcl43_ID, (Taggm) (value))


// ********** Metodi standard **********

void L_P1_C3_Init(instance_id_t const my_id);

void L_P1_C3_Exec(instance_id_t const my_id, Phase const p);

ExecResponse L_P1_C3_GExec(global_id_t const proc_id, Phase const p);

void L_P1_C3_GTick(global_id_t const proc_id);

void L_P1_C3_GSetSafe(global_id_t const proc_id);

void L_P1_C3_GUpdatePrev(global_id_t const proc_id);

// ********** Altri metodi pubblici**********

// Macro di effetto
void L_P1__Macro23(instance_id_t const my_id );
void L_P1__Macro24(instance_id_t const my_id );
void L_P1__Macro25(instance_id_t const my_id );
void L_P1__Macro26(instance_id_t const my_id );

// Macro di verifica
bool L_P1__Macro29(instance_id_t const my_id , C3_Enumerat4 argom81, bool argom82, C3_Enumerat2 argom83, C3_Enumerat1 argom84, bool argom85);
bool L_P1__Macro30(instance_id_t const my_id , C3_Enumerat1 argom86, bool argom87, C3_Enumerat2 argom88, C3_Enumerat1 argom89);

// Macro valorizzate
bool L_P1__Macro27(instance_id_t const my_id , C3_Enumerat1 argom71, C3_Enumerat2 argom72, C3_Enumerat4 argom73, C3_Enumerat1 argom74, bool argom75);
bool L_P1__Macro28(instance_id_t const my_id , C3_Enumerat2 argom76, C3_Enumerat1 argom77, C3_Enumerat3 argom78, C3_Enumerat1 argom79, bool argom80);


#endif // LIBSTAZIONE_CLASSEL_P1_C3_H
