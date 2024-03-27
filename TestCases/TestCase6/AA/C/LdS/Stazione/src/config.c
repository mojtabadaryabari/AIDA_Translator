// Codice del modello 'TestCase6', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#include <string.h>  // memset
#include "config.h"
#include "interface.h"
#include "scheduler.h"
#include "PlatformMngArea.h"
#include "PlatformMngConfiguration.h"
#include "MstAreaAccess.h"
#ifdef LDS_DEBUG
#include <stdio.h>
#include <inttypes.h>
#endif

// Identificativi aree dati per primitive libreria Platform
#define LDSCORE "LDSCORE"
#define CLASS_DATA "LDSCLD"
#define SCHED_DATA "LDSSCD"


// Definizione aree dati per parametri e dati della logica

ldsStazioneConfData lds_Stazione_conf = { NULL };  // pConfHeader inizializzato a NULL

ldsStazioneData *lds_Stazione_data;


// Dichiarazione metodi privati
static void SchedulerInit(Scheduler_data *scheduler);


// ********** Getter numero di istanze **********

instance_id_t getNumeroL_P1_C1()
{
    CHECK_POINTER(lds_Stazione_conf.pConfHeader);
    return lds_Stazione_conf.pConfHeader->numero_L_P1_C1;
}
instance_id_t getNumeroL_P1_C2()
{
    CHECK_POINTER(lds_Stazione_conf.pConfHeader);
    return lds_Stazione_conf.pConfHeader->numero_L_P1_C2;
}


// ********** Getter e setter Classe L_P1_C1 **********

Timer* L_P1__GetMainc35(instance_id_t const my_id)
{
    return &(lds_Stazione_data->L_P1_C1[my_id].mainc35);
}

Timer* L_P1__GetMainc36(instance_id_t const my_id)
{
    return &(lds_Stazione_data->L_P1_C1[my_id].mainc36);
}

Timer* L_P1__GetMainc37(instance_id_t const my_id)
{
    return &(lds_Stazione_data->L_P1_C1[my_id].mainc37);
}

Timer* L_P1__GetMainc38(instance_id_t const my_id)
{
    return &(lds_Stazione_data->L_P1_C1[my_id].mainc38);
}

Timer* L_P1__GetMainc39(instance_id_t const my_id)
{
    return &(lds_Stazione_data->L_P1_C1[my_id].mainc39);
}

Timer* L_P1__GetMainc40(instance_id_t const my_id)
{
    return &(lds_Stazione_data->L_P1_C1[my_id].mainc40);
}

Timer* L_P1__GetMainc41(instance_id_t const my_id)
{
    return &(lds_Stazione_data->L_P1_C1[my_id].mainc41);
}

Timer* L_P1__GetMainc42(instance_id_t const my_id)
{
    return &(lds_Stazione_data->L_P1_C1[my_id].mainc42);
}

Counter* L_P1__GetMainc43(instance_id_t const my_id)
{
    return &(lds_Stazione_data->L_P1_C1[my_id].mainc43);
}

Counter* L_P1__GetMainc44(instance_id_t const my_id)
{
    return &(lds_Stazione_data->L_P1_C1[my_id].mainc44);
}


ExecResponse L_P1_C1_GetResponse(instance_id_t const my_id)
{
    return lds_Stazione_data->L_P1_C1[my_id].response;
}

void L_P1_C1_SetResponse(instance_id_t const my_id, ExecResponse const value)
{
    lds_Stazione_data->L_P1_C1[my_id].response = value;
}

// Classe L_P1_C1 - ambiente

// ********** Getter e setter Classe L_P1_C2 **********

Timer* L_P1__GetSubcl36(instance_id_t const my_id)
{
    return &(lds_Stazione_data->L_P1_C2[my_id].subcl36);
}

Timer* L_P1__GetSubcl37(instance_id_t const my_id)
{
    return &(lds_Stazione_data->L_P1_C2[my_id].subcl37);
}

Timer* L_P1__GetSubcl38(instance_id_t const my_id)
{
    return &(lds_Stazione_data->L_P1_C2[my_id].subcl38);
}

Timer* L_P1__GetSubcl39(instance_id_t const my_id)
{
    return &(lds_Stazione_data->L_P1_C2[my_id].subcl39);
}

Timer* L_P1__GetSubcl40(instance_id_t const my_id)
{
    return &(lds_Stazione_data->L_P1_C2[my_id].subcl40);
}

Timer* L_P1__GetSubcl41(instance_id_t const my_id)
{
    return &(lds_Stazione_data->L_P1_C2[my_id].subcl41);
}

Counter* L_P1__GetSubcl42(instance_id_t const my_id)
{
    return &(lds_Stazione_data->L_P1_C2[my_id].subcl42);
}

Counter* L_P1__GetSubcl43(instance_id_t const my_id)
{
    return &(lds_Stazione_data->L_P1_C2[my_id].subcl43);
}

Counter* L_P1__GetSubcl44(instance_id_t const my_id)
{
    return &(lds_Stazione_data->L_P1_C2[my_id].subcl44);
}

Counter* L_P1__GetSubcl45(instance_id_t const my_id)
{
    return &(lds_Stazione_data->L_P1_C2[my_id].subcl45);
}


ExecResponse L_P1_C2_GetResponse(instance_id_t const my_id)
{
    return lds_Stazione_data->L_P1_C2[my_id].response;
}

void L_P1_C2_SetResponse(instance_id_t const my_id, ExecResponse const value)
{
    lds_Stazione_data->L_P1_C2[my_id].response = value;
}

// Classe L_P1_C2 - ambiente



// ********** Getter parametri classe L_P1_C1 **********

C1_Enumerat4 L_P1__GetParamMainc9(instance_id_t const my_id)
{
    CHECK_POINTER(lds_Stazione_conf.pConfL_P1_C1);
    CHECK_LE(my_id, getNumeroL_P1_C1());
    return lds_Stazione_conf.pConfL_P1_C1[my_id - 1u].mainc9;
}

C1_Enumerat2 L_P1__GetParamMainc10(instance_id_t const my_id)
{
    CHECK_POINTER(lds_Stazione_conf.pConfL_P1_C1);
    CHECK_LE(my_id, getNumeroL_P1_C1());
    return lds_Stazione_conf.pConfL_P1_C1[my_id - 1u].mainc10;
}

bool L_P1__GetParamMainc11(instance_id_t const my_id)
{
    CHECK_POINTER(lds_Stazione_conf.pConfL_P1_C1);
    CHECK_LE(my_id, getNumeroL_P1_C1());
    return lds_Stazione_conf.pConfL_P1_C1[my_id - 1u].mainc11;
}

bool L_P1__GetParamMainc12(instance_id_t const my_id)
{
    CHECK_POINTER(lds_Stazione_conf.pConfL_P1_C1);
    CHECK_LE(my_id, getNumeroL_P1_C1());
    return lds_Stazione_conf.pConfL_P1_C1[my_id - 1u].mainc12;
}

Intero L_P1__GetParamMainc13(instance_id_t const my_id)
{
    CHECK_POINTER(lds_Stazione_conf.pConfL_P1_C1);
    CHECK_LE(my_id, getNumeroL_P1_C1());
    return lds_Stazione_conf.pConfL_P1_C1[my_id - 1u].mainc13;
}

// ********** Getter parametri classe L_P1_C2 **********

C2_Enumerat4 L_P1__GetParamSubcl13(instance_id_t const my_id)
{
    CHECK_POINTER(lds_Stazione_conf.pConfL_P1_C2);
    CHECK_LE(my_id, getNumeroL_P1_C2());
    return lds_Stazione_conf.pConfL_P1_C2[my_id - 1u].subcl13;
}

C2_Enumerat4 L_P1__GetParamSubcl14(instance_id_t const my_id)
{
    CHECK_POINTER(lds_Stazione_conf.pConfL_P1_C2);
    CHECK_LE(my_id, getNumeroL_P1_C2());
    return lds_Stazione_conf.pConfL_P1_C2[my_id - 1u].subcl14;
}

offset_t L_P1__GetParamSubcl9Start(instance_id_t const my_id)
{
    CHECK_POINTER(lds_Stazione_conf.pConfL_P1_C2);
    CHECK_LE(my_id, getNumeroL_P1_C2());
    return lds_Stazione_conf.pConfL_P1_C2[my_id - 1u].subcl9_start;
}

index_t L_P1__GetParamSubcl9Length(instance_id_t const my_id)
{
    CHECK_POINTER(lds_Stazione_conf.pConfL_P1_C2);
    CHECK_LE(my_id, getNumeroL_P1_C2());
    return lds_Stazione_conf.pConfL_P1_C2[my_id - 1u].subcl9_length;
}

L_P1__Recor L_P1__GetRecSubcl9(instance_id_t const my_id, index_t const elem_idx)
{
    offset_t const start = L_P1__GetParamSubcl9Start(my_id);
    L_P1__Recor *p = (L_P1__Recor *)
        ((uint8_t*) lds_Stazione_conf.pConfHeader + start);
    CHECK_LT(elem_idx, L_P1__GetParamSubcl9Length(my_id));
    return p[elem_idx];
}

offset_t L_P1__GetParamSubcl10Start(instance_id_t const my_id)
{
    CHECK_POINTER(lds_Stazione_conf.pConfL_P1_C2);
    CHECK_LE(my_id, getNumeroL_P1_C2());
    return lds_Stazione_conf.pConfL_P1_C2[my_id - 1u].subcl10_start;
}

index_t L_P1__GetParamSubcl10Length(instance_id_t const my_id)
{
    CHECK_POINTER(lds_Stazione_conf.pConfL_P1_C2);
    CHECK_LE(my_id, getNumeroL_P1_C2());
    return lds_Stazione_conf.pConfL_P1_C2[my_id - 1u].subcl10_length;
}

L_P1__Recor1 L_P1__GetRecSubcl10(instance_id_t const my_id, index_t const elem_idx)
{
    offset_t const start = L_P1__GetParamSubcl10Start(my_id);
    L_P1__Recor1 *p = (L_P1__Recor1 *)
        ((uint8_t*) lds_Stazione_conf.pConfHeader + start);
    CHECK_LT(elem_idx, L_P1__GetParamSubcl10Length(my_id));
    return p[elem_idx];
}

offset_t L_P1__GetParamSubcl11Start(instance_id_t const my_id)
{
    CHECK_POINTER(lds_Stazione_conf.pConfL_P1_C2);
    CHECK_LE(my_id, getNumeroL_P1_C2());
    return lds_Stazione_conf.pConfL_P1_C2[my_id - 1u].subcl11_start;
}

index_t L_P1__GetParamSubcl11Length(instance_id_t const my_id)
{
    CHECK_POINTER(lds_Stazione_conf.pConfL_P1_C2);
    CHECK_LE(my_id, getNumeroL_P1_C2());
    return lds_Stazione_conf.pConfL_P1_C2[my_id - 1u].subcl11_length;
}

L_P1__Recor1 L_P1__GetRecSubcl11(instance_id_t const my_id, index_t const elem_idx)
{
    offset_t const start = L_P1__GetParamSubcl11Start(my_id);
    L_P1__Recor1 *p = (L_P1__Recor1 *)
        ((uint8_t*) lds_Stazione_conf.pConfHeader + start);
    CHECK_LT(elem_idx, L_P1__GetParamSubcl11Length(my_id));
    return p[elem_idx];
}

offset_t L_P1__GetParamSubcl12Start(instance_id_t const my_id)
{
    CHECK_POINTER(lds_Stazione_conf.pConfL_P1_C2);
    CHECK_LE(my_id, getNumeroL_P1_C2());
    return lds_Stazione_conf.pConfL_P1_C2[my_id - 1u].subcl12_start;
}

index_t L_P1__GetParamSubcl12Length(instance_id_t const my_id)
{
    CHECK_POINTER(lds_Stazione_conf.pConfL_P1_C2);
    CHECK_LE(my_id, getNumeroL_P1_C2());
    return lds_Stazione_conf.pConfL_P1_C2[my_id - 1u].subcl12_length;
}

L_P1__Recor1 L_P1__GetRecSubcl12(instance_id_t const my_id, index_t const elem_idx)
{
    offset_t const start = L_P1__GetParamSubcl12Start(my_id);
    L_P1__Recor1 *p = (L_P1__Recor1 *)
        ((uint8_t*) lds_Stazione_conf.pConfHeader + start);
    CHECK_LT(elem_idx, L_P1__GetParamSubcl12Length(my_id));
    return p[elem_idx];
}



// ********** Procedure di attach **********

static void CdlConfAttach() {
    lds_Stazione_conf.pConfHeader = (lds_config_enti_header*) PlatformGetConfigArea(MstGetCurrentStationId(TASK_ID_LDS), LDSCORE);
    CHECK_POINTER(lds_Stazione_conf.pConfHeader);

    // imposta puntatori alle struct parametri
    lds_Stazione_conf.pConfL_P1_C1 = (Classe_L_P1_C1_Param *)
        ((uint8_t*) lds_Stazione_conf.pConfHeader + lds_Stazione_conf.pConfHeader->offset_L_P1_C1);

    lds_Stazione_conf.pConfL_P1_C2 = (Classe_L_P1_C2_Param *)
        ((uint8_t*) lds_Stazione_conf.pConfHeader + lds_Stazione_conf.pConfHeader->offset_L_P1_C2);

}

static void CdlDataAttach() {

    lds_Stazione_data = (ldsStazioneData *)
        PlatformGetStationArea(MstGetCurrentStationId(TASK_ID_LDS), CLASS_DATA);
}

static void SchedulerDataAttach() {

    Scheduler_data *sched_data = (Scheduler_data *)
        PlatformGetStationArea(MstGetCurrentStationId(TASK_ID_LDS), SCHED_DATA);
    scheduler_SetMemoryArea(sched_data);
}


// ********** Procedure di inizializzazione **********

static void CdlDataInit() {
    // allocazione area dati classi di logica
    uint32_t size_L_P1_C1 = (lds_Stazione_conf.pConfHeader->numero_L_P1_C1 + 1u) * sizeof(Classe_L_P1_C1);
    uint32_t size_L_P1_C2 = (lds_Stazione_conf.pConfHeader->numero_L_P1_C2 + 1u) * sizeof(Classe_L_P1_C2);

    uint64_t class_data_size = (uint64_t) sizeof(ldsStazioneData)  + size_L_P1_C1 + size_L_P1_C2 ;
    CHECK_LT(class_data_size, UINT32_MAX);

    uint8_t *pClassData = PlatformCreateStationArea(MstGetCurrentStationId(TASK_ID_LDS), CLASS_DATA, (uint32_t) class_data_size, NOT_SYNCHRONIZABLE);
    (void) memset(pClassData, 0, class_data_size);

    // imposta puntatori alle aree dati classi di logica
    lds_Stazione_data = (ldsStazioneData *) pClassData;
    uint8_t *start_L_P1_C1 = pClassData + sizeof(ldsStazioneData);
    uint8_t *start_L_P1_C2 = start_L_P1_C1 + size_L_P1_C1;

    lds_Stazione_data->L_P1_C1 = (Classe_L_P1_C1 *) start_L_P1_C1;
    lds_Stazione_data->L_P1_C2 = (Classe_L_P1_C2 *) start_L_P1_C2;

    // imposta aree dati
    lds_Stazione_data->numero_istanze = lds_Stazione_conf.pConfHeader->numero_L_P1_C1 + lds_Stazione_conf.pConfHeader->numero_L_P1_C2;

    lds_Stazione_data->base.L_P1_C1 = 0u;
    lds_Stazione_data->base.L_P1_C2 = lds_Stazione_data->base.L_P1_C1 + lds_Stazione_conf.pConfHeader->numero_L_P1_C1;
}

static void SchedulerDataInit() {
    // allocazione area dati scheduler
    global_id_t n = lds_Stazione_data->numero_istanze;
    size_t size_scheduler_data = sizeof(Scheduler_data);
    size_t size_scheduler_tbl = (n + 1u) * sizeof(Scheduler_process_data);
    size_t size_scheduler_pac = (n + 1u) * sizeof(global_id_t);

    size_t sched_data_size = size_scheduler_data + size_scheduler_tbl + (size_scheduler_pac * 2u);
    CHECK_LT(sched_data_size, UINT32_MAX);

    uint8_t *pSchedData = PlatformCreateStationArea(MstGetCurrentStationId(TASK_ID_LDS), SCHED_DATA, (uint32_t) sched_data_size, NOT_SYNCHRONIZABLE);
    (void) memset(pSchedData, 0, sched_data_size);

    // imposta puntatori struct Scheduler_data
    Scheduler_data *scheduler = (Scheduler_data *) pSchedData;

    uint8_t *start_tbl = pSchedData + size_scheduler_data;
    scheduler->tbl = (Scheduler_process_data *) start_tbl;

    uint8_t *start_pac = pSchedData + size_scheduler_data + size_scheduler_tbl;
    scheduler->processes_with_automatic_commands = (global_id_t *) start_pac;
    
    uint8_t *start_pac_copy = pSchedData + size_scheduler_data + size_scheduler_tbl + size_scheduler_pac;
    scheduler->processes_with_automatic_commands_copy = (global_id_t *) start_pac_copy;

    scheduler->scheduling_order = (global_id_t *)
        ((uint8_t*) lds_Stazione_conf.pConfHeader + lds_Stazione_conf.pConfHeader->offset_scheduling_order);

    // init strutture dati scheduler
    SchedulerInit(scheduler);

    // lo scheduler deve essere pronto per l'esecuzione prima della
    // chiamata a CdlInit (è possibile mandare comandi automatici
    // nelle transizioni iniziali)
    scheduler_SetMemoryArea(scheduler);
}

static void CdlInit() {
    for (instance_id_t i = 1u; i <= getNumeroL_P1_C1(); ++i) {
        L_P1_C1_Init(i);
    }
    for (instance_id_t i = 1u; i <= getNumeroL_P1_C2(); ++i) {
        L_P1_C2_Init(i);
    }
}

static void SchedulerInit(Scheduler_data *scheduler) {
   // Inizializza virtual table

    // Istanze di Classe L_P1_C1
    for (instance_id_t i = 1; i <= getNumeroL_P1_C1(); ++i) {
        scheduler->tbl[L_P1_C1_TO_GLOBAL(i)].exec_fun = L_P1_C1_GExec;
        scheduler->tbl[L_P1_C1_TO_GLOBAL(i)].tick_fun = L_P1_C1_GTick;
        scheduler->tbl[L_P1_C1_TO_GLOBAL(i)].setsafe_fun = L_P1_C1_GSetSafe;
        scheduler->tbl[L_P1_C1_TO_GLOBAL(i)].updateprev_fun = L_P1_C1_GUpdatePrev;
    }

    // Istanze di Classe L_P1_C2
    for (instance_id_t i = 1; i <= getNumeroL_P1_C2(); ++i) {
        scheduler->tbl[L_P1_C2_TO_GLOBAL(i)].exec_fun = L_P1_C2_GExec;
        scheduler->tbl[L_P1_C2_TO_GLOBAL(i)].tick_fun = L_P1_C2_GTick;
        scheduler->tbl[L_P1_C2_TO_GLOBAL(i)].setsafe_fun = L_P1_C2_GSetSafe;
        scheduler->tbl[L_P1_C2_TO_GLOBAL(i)].updateprev_fun = L_P1_C2_GUpdatePrev;
    }


    // Inizializzazioni comuni
    for (global_id_t i = 1; i <= lds_Stazione_data->numero_istanze; ++i) {
        scheduler->tbl[i].has_automatic_commands = false;
        scheduler->tbl[i].is_done = false;
        scheduler->processes_with_automatic_commands[i] = 0;
        scheduler->processes_with_automatic_commands_copy[i] = 0;
    }
    scheduler->num_processes = lds_Stazione_data->numero_istanze;
    scheduler->num_processes_with_automatic_commands = 0;
}


static void ResetComandiAutomatici() {
    for (instance_id_t i = 1; i <= getNumeroL_P1_C1(); ++i) {
        L_P1__SetCAEvent(i, false);
    }
}


#ifdef LDS_DEBUG

static void printconf() {
    // NOTE: printf specifiers in the following are tied to
    // the specific type definitions found in in utils.h

    FILE *out = fopen("conf.log", "w");
    if (out != NULL) {

    (void) fprintf(out,"========== Header ==========\n");
    (void) fprintf(out,"Numero di L_P1_C1: %" PRIu16 ", offset: 0x%08" PRIx32 "\n",
           lds_Stazione_conf.pConfHeader->numero_L_P1_C1,
           lds_Stazione_conf.pConfHeader->offset_L_P1_C1);
    (void) fprintf(out,"Numero di L_P1_C2: %" PRIu16 ", offset: 0x%08" PRIx32 "\n",
           lds_Stazione_conf.pConfHeader->numero_L_P1_C2,
           lds_Stazione_conf.pConfHeader->offset_L_P1_C2);

    (void) fprintf(out,"========== Ordine di scheduling per %" PRIu32 " istanze ==========\n", lds_Stazione_data->numero_istanze);
    global_id_t *scheduling_order = (global_id_t *)
        ((uint8_t*) lds_Stazione_conf.pConfHeader + lds_Stazione_conf.pConfHeader->offset_scheduling_order);
    for (global_id_t i = 1u; i <= lds_Stazione_data->numero_istanze; ++i) {
        (void) fprintf(out,"%" PRIu32 " ", scheduling_order[i-1u]);
    }
    (void) fprintf(out,"\n");


    if (lds_Stazione_conf.pConfHeader->numero_L_P1_C1 != 0) {
        (void) fprintf(out,"========== Parametri classe L_P1_C1 ==========\n");
        for (instance_id_t i = 1u; i <= getNumeroL_P1_C1(); ++i) {
            (void) fprintf(out,"***** Istanza %" PRIu16 ":\n",i);
            (void) fprintf(out,"mainc9 = %" PRIu32 "\n", (uint32_t) L_P1__GetParamMainc9(i));
            (void) fprintf(out,"mainc10 = %" PRIu32 "\n", (uint32_t) L_P1__GetParamMainc10(i));
            (void) fprintf(out,"mainc11 = %" PRIu32 "\n", (uint32_t) L_P1__GetParamMainc11(i));
            (void) fprintf(out,"mainc12 = %" PRIu32 "\n", (uint32_t) L_P1__GetParamMainc12(i));
            (void) fprintf(out,"mainc13 = %" PRIu32 "\n", (uint32_t) L_P1__GetParamMainc13(i));
        }
    }

    if (lds_Stazione_conf.pConfHeader->numero_L_P1_C2 != 0) {
        (void) fprintf(out,"========== Parametri classe L_P1_C2 ==========\n");
        for (instance_id_t i = 1u; i <= getNumeroL_P1_C2(); ++i) {
            (void) fprintf(out,"***** Istanza %" PRIu16 ":\n",i);
            (void) fprintf(out,"subcl13 = %" PRIu32 "\n", (uint32_t) L_P1__GetParamSubcl13(i));
            (void) fprintf(out,"subcl14 = %" PRIu32 "\n", (uint32_t) L_P1__GetParamSubcl14(i));
            (void) fprintf(out,"subcl9 start = 0x%08" PRIx32 ", length = %" PRIu32 " : [",
                L_P1__GetParamSubcl9Start(i),
                L_P1__GetParamSubcl9Length(i));
            for (index_t j = 0u; j < L_P1__GetParamSubcl9Length(i); ++j) {
                L_P1__Recor it = L_P1__GetRecSubcl9(i,j);
                (void) fprintf(out,"(%" PRIu32 " %" PRIu32 " %" PRIu32 " %" PRIu32 " %" PRIu32 ")", (uint32_t) it.mainc45, (uint32_t) it.recor, (uint32_t) it.recor1, (uint32_t) it.recor2, (uint32_t) it.recor3);
                if (j != L_P1__GetParamSubcl9Length(i)-1u) {
                    (void) fprintf(out,", ");
                }
            }
            (void) fprintf(out,"]\n");
            (void) fprintf(out,"subcl10 start = 0x%08" PRIx32 ", length = %" PRIu32 " : [",
                L_P1__GetParamSubcl10Start(i),
                L_P1__GetParamSubcl10Length(i));
            for (index_t j = 0u; j < L_P1__GetParamSubcl10Length(i); ++j) {
                L_P1__Recor1 it = L_P1__GetRecSubcl10(i,j);
                (void) fprintf(out,"(%" PRIu32 " %" PRIu32 " %" PRIu32 " %" PRIu32 " %" PRIu32 ")", (uint32_t) it.mainc46, (uint32_t) it.recor4, (uint32_t) it.recor5, (uint32_t) it.recor6, (uint32_t) it.recor7);
                if (j != L_P1__GetParamSubcl10Length(i)-1u) {
                    (void) fprintf(out,", ");
                }
            }
            (void) fprintf(out,"]\n");
            (void) fprintf(out,"subcl11 start = 0x%08" PRIx32 ", length = %" PRIu32 " : [",
                L_P1__GetParamSubcl11Start(i),
                L_P1__GetParamSubcl11Length(i));
            for (index_t j = 0u; j < L_P1__GetParamSubcl11Length(i); ++j) {
                L_P1__Recor1 it = L_P1__GetRecSubcl11(i,j);
                (void) fprintf(out,"(%" PRIu32 " %" PRIu32 " %" PRIu32 " %" PRIu32 " %" PRIu32 ")", (uint32_t) it.mainc46, (uint32_t) it.recor4, (uint32_t) it.recor5, (uint32_t) it.recor6, (uint32_t) it.recor7);
                if (j != L_P1__GetParamSubcl11Length(i)-1u) {
                    (void) fprintf(out,", ");
                }
            }
            (void) fprintf(out,"]\n");
            (void) fprintf(out,"subcl12 start = 0x%08" PRIx32 ", length = %" PRIu32 " : [",
                L_P1__GetParamSubcl12Start(i),
                L_P1__GetParamSubcl12Length(i));
            for (index_t j = 0u; j < L_P1__GetParamSubcl12Length(i); ++j) {
                L_P1__Recor1 it = L_P1__GetRecSubcl12(i,j);
                (void) fprintf(out,"(%" PRIu32 " %" PRIu32 " %" PRIu32 " %" PRIu32 " %" PRIu32 ")", (uint32_t) it.mainc46, (uint32_t) it.recor4, (uint32_t) it.recor5, (uint32_t) it.recor6, (uint32_t) it.recor7);
                if (j != L_P1__GetParamSubcl12Length(i)-1u) {
                    (void) fprintf(out,", ");
                }
            }
            (void) fprintf(out,"]\n");
        }
    }
    (void)fclose(out);
    }
}
#endif // LDS_DEBUG


// ********** Interfaccia pubblica **********

void Stazione_lds_Init() {

    CdlConfAttach();
#ifdef LDS_DEBUG
    printconf();
#endif // LDS_DEBUG

    CdlDataInit();
    SchedulerDataInit();

    // Effettua le transizioni iniziali
    CdlInit();
}

void Stazione_lds_Exec() {

    // Context switch
    CdlConfAttach();
    CdlDataAttach();
    SchedulerDataAttach();

    // Esegui istanze
    scheduler_DeltaCycle();
    ResetComandiAutomatici();
}


