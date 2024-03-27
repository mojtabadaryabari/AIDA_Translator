#include <string.h>  // memset
#include "config.h"
#include "interface.h"
#include "scheduler.h"
#include "version.h"
#include "LogicInterface.h"

#include "PlatformMngArea.h"
#include "PlatformMngConfiguration.h"
#include "MstAreaAccess.h"
#include "NvsLogConst.h"
#include "PlatformMacros.h"

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

instance_id_t getNumeroL_P1_C3()
{
    CHECK_POINTER(ldv_Stazione_conf.pConfHeader);
    return ldv_Stazione_conf.pConfHeader->numero_L_P1_C3;
}


// ********** Getter e setter Classe L_P1_C3 **********

Timer* L_P1__GetLdv_m6(instance_id_t const my_id)
{
    return &(ldv_Stazione_data->L_P1_C3[my_id].ldv_m6);
}

Counter* L_P1__GetLdv_m7(instance_id_t const my_id)
{
    return &(ldv_Stazione_data->L_P1_C3[my_id].ldv_m7);
}

Counter* L_P1__GetLdv_m8(instance_id_t const my_id)
{
    return &(ldv_Stazione_data->L_P1_C3[my_id].ldv_m8);
}

Counter* L_P1__GetLdv_m9(instance_id_t const my_id)
{
    return &(ldv_Stazione_data->L_P1_C3[my_id].ldv_m9);
}

Counter* L_P1__GetLdv_m10(instance_id_t const my_id)
{
    return &(ldv_Stazione_data->L_P1_C3[my_id].ldv_m10);
}


ExecResponse L_P1_C3_GetResponse(instance_id_t const my_id)
{
    return ldv_Stazione_data->L_P1_C3[my_id].response;
}

void L_P1_C3_SetResponse(instance_id_t const my_id, ExecResponse const value)
{
    ldv_Stazione_data->L_P1_C3[my_id].response = value;
}

// Classe L_P1_C3 - ambiente



// ********** Getter parametri classe L_P1_C3 **********

bool L_P1__GetParamConsd2(instance_id_t const my_id)
{
    CHECK_POINTER(ldv_Stazione_conf.pConfL_P1_C3);
    CHECK_LE(my_id, getNumeroL_P1_C3());
    return ldv_Stazione_conf.pConfL_P1_C3[my_id - 1u].consd2;
}

bool L_P1__GetParamLdv_m(instance_id_t const my_id)
{
    CHECK_POINTER(ldv_Stazione_conf.pConfL_P1_C3);
    CHECK_LE(my_id, getNumeroL_P1_C3());
    return ldv_Stazione_conf.pConfL_P1_C3[my_id - 1u].ldv_m;
}

Intero L_P1__GetParamLdv_m1(instance_id_t const my_id)
{
    CHECK_POINTER(ldv_Stazione_conf.pConfL_P1_C3);
    CHECK_LE(my_id, getNumeroL_P1_C3());
    return ldv_Stazione_conf.pConfL_P1_C3[my_id - 1u].ldv_m1;
}

C3_Enumerat1 L_P1__GetParamLdv_m2(instance_id_t const my_id)
{
    CHECK_POINTER(ldv_Stazione_conf.pConfL_P1_C3);
    CHECK_LE(my_id, getNumeroL_P1_C3());
    return ldv_Stazione_conf.pConfL_P1_C3[my_id - 1u].ldv_m2;
}



// ********** Procedure di attach **********

static void CdlConfAttach() {
    ldv_Stazione_conf.pConfHeader = (ldv_config_enti_header*) PlatformGetConfigArea(MstGetCurrentStationId(TASK_ID_LDS), LDSCORE);
    CHECK_POINTER(ldv_Stazione_conf.pConfHeader);

    {   // Verifica l'informazione di versionamento della logica astratta
        const T_VersionInfo * const ver_ga = &(ldv_Stazione_conf.pConfHeader->pre.version_ga);
        CHECK_POINTER(ver_ga);
        if (LOGIC_VERSION_MAJOR != ver_ga->major ||
                LOGIC_VERSION_MINOR != ver_ga->minor ||
                LOGIC_VERSION_MICRO != ver_ga->micro) {
            NVSLOG_WARN("Versione della configurazione non coerente "
                        "con la logica")
            /* Only when in simulation mode invalid values of version
             * information allows to continue the execution */
#if defined(SIMULENV)
            if (LOGIC_VERSION_INVALID_VAL != ver_ga->major ||
                    LOGIC_VERSION_INVALID_VAL != ver_ga->minor ||
                    LOGIC_VERSION_INVALID_VAL != ver_ga->micro) {
                STOP_EXECUTION(0)
            }
            else {
                NVSLOG_WARN("L'esecuzione prosegue comunque perchè la versione è assente")
            }
#else  /* SIMULENV !defined */
            STOP_EXECUTION(0)
#endif  /* SIMULENV defined */
        }
    }

    // imposta puntatori alle struct parametri
    ldv_Stazione_conf.pConfL_P1_C3 = (Classe_L_P1_C3_Param *)
        ((uint8_t*) ldv_Stazione_conf.pConfHeader + ldv_Stazione_conf.pConfHeader->offset_L_P1_C3);

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
    uint32_t size_L_P1_C3 = (ldv_Stazione_conf.pConfHeader->numero_L_P1_C3 + 1u) * sizeof(Classe_L_P1_C3);

    uint64_t class_data_size = (uint64_t) sizeof(ldvStazioneData)  + size_L_P1_C3 ;
    CHECK_LT(class_data_size, UINT32_MAX);

    uint8_t *pClassData = PlatformCreateStationArea(MstGetCurrentStationId(TASK_ID_LDS), CLASS_DATA, (uint32_t) class_data_size, NOT_SYNCHRONIZABLE);
    (void) memset(pClassData, 0, class_data_size);

    // imposta puntatori alle aree dati classi di logica
    ldv_Stazione_data = (ldvStazioneData *) pClassData;
    uint8_t *start_L_P1_C3 = pClassData + sizeof(ldvStazioneData);

    ldv_Stazione_data->L_P1_C3 = (Classe_L_P1_C3 *) start_L_P1_C3;

    // imposta aree dati
    ldv_Stazione_data->numero_istanze = ldv_Stazione_conf.pConfHeader->numero_L_P1_C3;

    ldv_Stazione_data->base.L_P1_C3 = 0u;
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
    for (instance_id_t i = 1u; i <= getNumeroL_P1_C3(); ++i) {
        L_P1_C3_Init(i);
    }
}

static void SchedulerInit(Scheduler_data *scheduler) {
   // Inizializza virtual table

    // Istanze di Classe L_P1_C3
    for (instance_id_t i = 1; i <= getNumeroL_P1_C3(); ++i) {
        scheduler->tbl[L_P1_C3_TO_GLOBAL(i)].exec_fun = L_P1_C3_GExec;
        scheduler->tbl[L_P1_C3_TO_GLOBAL(i)].tick_fun = L_P1_C3_GTick;
        scheduler->tbl[L_P1_C3_TO_GLOBAL(i)].setsafe_fun = NULL;
        scheduler->tbl[L_P1_C3_TO_GLOBAL(i)].updateprev_fun = NULL;
    }


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
    for (instance_id_t i = 1; i <= getNumeroL_P1_C3(); ++i) {
        L_P1__SetCAEvent15(i, false);
    }
}


#ifdef LDS_DEBUG

static void printconf() {
    // NOTE: printf specifiers in the following are tied to
    // the specific type definitions found in in utils.h

    FILE *out = fopen("conf.log", "w");
    if (out != NULL) {

    (void) fprintf(out,"========== Header ==========\n");
    (void) fprintf(out, "Version GA: <%" PRIu8 ", %" PRIu8 ", %" %PRIu8 ">\n",
                   ldv_Stazione_conf.pConfHeader->pre.version_ga.major,
                   ldv_Stazione_conf.pConfHeader->pre.version_ga.minor,
                   ldv_Stazione_conf.pConfHeader->pre.version_ga.micro);
    (void) fprintf(out, "Version SA: <%" PRIu8 ", %" PRIu8 ", %" %PRIu8 ">\n",
                   ldv_Stazione_conf.pConfHeader->pre.version_sa.major,
                   ldv_Stazione_conf.pConfHeader->pre.version_sa.minor,
                   ldv_Stazione_conf.pConfHeader->pre.version_sa.micro);
    (void) fprintf(out, "Plant Type ID: %" PRIu8 "\n",
                   ldv_Stazione_conf.pConfHeader->pre.plant_type);
    (void) fprintf(out, "Plant ID: %" PRIu8 "\n",
                   ldv_Stazione_conf.pConfHeader->pre.station_id);

    (void) fprintf(out,"Numero di L_P1_C3: %" PRIu16 ", offset: 0x%08" PRIx32 "\n",
           ldv_Stazione_conf.pConfHeader->numero_L_P1_C3,
           ldv_Stazione_conf.pConfHeader->offset_L_P1_C3);

    const uint32_t numero_istanze = ldv_Stazione_conf.pConfHeader->numero_L_P1_C3;
    (void) fprintf(out,"========== Ordine di scheduling per %" PRIu32 " istanze ==========\n", numero_istanze);
    global_id_t *scheduling_order = (global_id_t *)
        ((uint8_t*) ldv_Stazione_conf.pConfHeader + ldv_Stazione_conf.pConfHeader->offset_scheduling_order);
    for (global_id_t i = 1u; i <= numero_istanze; ++i) {
        (void) fprintf(out,"%" PRIu32 " ", scheduling_order[i-1u]);
    }
    (void) fprintf(out,"\n");


    if (ldv_Stazione_conf.pConfHeader->numero_L_P1_C3 != 0) {
        (void) fprintf(out,"========== Parametri classe L_P1_C3 ==========\n");
        for (instance_id_t i = 1u; i <= getNumeroL_P1_C3(); ++i) {
            (void) fprintf(out,"***** Istanza %" PRIu16 ":\n",i);
            (void) fprintf(out,"consd2 = %" PRIu32 "\n", (uint32_t) L_P1__GetParamConsd2(i));
            (void) fprintf(out,"ldv_m = %" PRIu32 "\n", (uint32_t) L_P1__GetParamLdv_m(i));
            (void) fprintf(out,"ldv_m1 = %" PRIu32 "\n", (uint32_t) L_P1__GetParamLdv_m1(i));
            (void) fprintf(out,"ldv_m2 = %" PRIu32 "\n", (uint32_t) L_P1__GetParamLdv_m2(i));
        }
    }
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


