// Codice del modello 'TestCase19', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
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
#define CLASS_DATA "LDVCLD"
#define SCHED_DATA "LDVSCD"


// Definizione aree dati per parametri e dati della logica

ldvStazioneConfData ldv_Stazione_conf = { NULL };  // pConfHeader inizializzato a NULL

ldvStazioneData *ldv_Stazione_data;


// Dichiarazione metodi privati
static void SchedulerInit(Scheduler_data *scheduler);


// ********** Getter numero di istanze **********







// ********** Procedure di attach **********

static void CdlConfAttach() {
    ldv_Stazione_conf.pConfHeader = (ldv_config_enti_header*) PlatformGetConfigArea(MstGetCurrentStationId(TASK_ID_LDS), LDSCORE);
    CHECK_POINTER(ldv_Stazione_conf.pConfHeader);

    // imposta puntatori alle struct parametri
}

static void CdlDataAttach() {

    ldv_Stazione_data = (ldvStazioneData *)
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

    uint64_t class_data_size = (uint64_t) sizeof(ldvStazioneData) ;
    CHECK_LT(class_data_size, UINT32_MAX);

    uint8_t *pClassData = PlatformCreateStationArea(MstGetCurrentStationId(TASK_ID_LDS), CLASS_DATA, (uint32_t) class_data_size, NOT_SYNCHRONIZABLE);
    (void) memset(pClassData, 0, class_data_size);

    // imposta puntatori alle aree dati classi di logica
    ldv_Stazione_data = (ldvStazioneData *) pClassData;



}

static void SchedulerDataInit() {
    // allocazione area dati scheduler
    global_id_t n = ldv_Stazione_data->numero_istanze;
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
        ((uint8_t*) ldv_Stazione_conf.pConfHeader + ldv_Stazione_conf.pConfHeader->offset_scheduling_order);

    // init strutture dati scheduler
    SchedulerInit(scheduler);

    // lo scheduler deve essere pronto per l'esecuzione prima della
    // chiamata a CdlInit (è possibile mandare comandi automatici
    // nelle transizioni iniziali)
    scheduler_SetMemoryArea(scheduler);
}

static void CdlInit() {
}

static void SchedulerInit(Scheduler_data *scheduler) {
   // Inizializza virtual table


    // Inizializzazioni comuni
    for (global_id_t i = 1; i <= ldv_Stazione_data->numero_istanze; ++i) {
        scheduler->tbl[i].has_automatic_commands = false;
        scheduler->tbl[i].is_done = false;
        scheduler->processes_with_automatic_commands[i] = 0;
        scheduler->processes_with_automatic_commands_copy[i] = 0;
    }
    scheduler->num_processes = ldv_Stazione_data->numero_istanze;
    scheduler->num_processes_with_automatic_commands = 0;
}


static void ResetComandiAutomatici() {
}


#ifdef LDS_DEBUG

static void printconf() {
    // NOTE: printf specifiers in the following are tied to
    // the specific type definitions found in in utils.h

    FILE *out = fopen("conf.log", "w");
    if (out != NULL) {

    (void) fprintf(out,"========== Header ==========\n");

    (void) fprintf(out,"========== Ordine di scheduling per %" PRIu32 " istanze ==========\n", ldv_Stazione_data->numero_istanze);
    global_id_t *scheduling_order = (global_id_t *)
        ((uint8_t*) ldv_Stazione_conf.pConfHeader + ldv_Stazione_conf.pConfHeader->offset_scheduling_order);
    for (global_id_t i = 1u; i <= ldv_Stazione_data->numero_istanze; ++i) {
        (void) fprintf(out,"%" PRIu32 " ", scheduling_order[i-1u]);
    }
    (void) fprintf(out,"\n");

    (void)fclose(out);
    }
}
#endif // LDS_DEBUG


// ********** Interfaccia pubblica **********

void Stazione_ldv_Init() {

    CdlConfAttach();
#ifdef LDS_DEBUG
    printconf();
#endif // LDS_DEBUG

    CdlDataInit();
    SchedulerDataInit();

    // Effettua le transizioni iniziali
    CdlInit();
}

void Stazione_ldv_Exec() {

    // Context switch
    CdlConfAttach();
    CdlDataAttach();
    SchedulerDataAttach();

    // Esegui istanze
    scheduler_DeltaCycle();
    ResetComandiAutomatici();
}


