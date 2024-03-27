// Codice del modello 'TestCase23', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#include <string.h>  // memset
#include "config.h"
#include "PlatformMngArea.h"
#include "PlatformConst.h"
#include "PlatformMacros.h"
#include "PlatformMngConfiguration.h"
#include "MstAreaAccess.h"


// Identificativi aree dati per primitive libreria Platform
#define FEASCFG "LDSFEAS"
#define CLASS_DATA "FEACLD"

// Definizione aree dati per parametri e dati della logica

ldsStazioneConfData lds_Stazione_conf = { NULL };  // pConfHeader inizializzato a NULL

ldsStazioneData *lds_Stazione_data;


// Diciarazione metodi privati


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


// ********** Getter Classe L_P1_C1 **********


ExecResponse L_P1_C1_GetResponse(instance_id_t const my_id)
{
    return lds_Stazione_data->L_P1_C1[my_id].response;
}

// Classe L_P1_C1 - ambiente


// ********** Getter Classe L_P1_C2 **********


ExecResponse L_P1_C2_GetResponse(instance_id_t const my_id)
{
    return lds_Stazione_data->L_P1_C2[my_id].response;
}

// Classe L_P1_C2 - ambiente




// ********** Getter parametri classe L_P1_C1 **********

Intero L_P1__GetParamMainc7(instance_id_t const my_id)
{
    CHECK_POINTER(lds_Stazione_conf.pConfL_P1_C1);
    CHECK_LE(my_id, getNumeroL_P1_C1());
    return lds_Stazione_conf.pConfL_P1_C1[my_id - 1u].mainc7;
}

bool L_P1__GetParamMainc8(instance_id_t const my_id)
{
    CHECK_POINTER(lds_Stazione_conf.pConfL_P1_C1);
    CHECK_LE(my_id, getNumeroL_P1_C1());
    return lds_Stazione_conf.pConfL_P1_C1[my_id - 1u].mainc8;
}

Intero L_P1__GetParamMainc9(instance_id_t const my_id)
{
    CHECK_POINTER(lds_Stazione_conf.pConfL_P1_C1);
    CHECK_LE(my_id, getNumeroL_P1_C1());
    return lds_Stazione_conf.pConfL_P1_C1[my_id - 1u].mainc9;
}

C1_Enumerat4 L_P1__GetParamMainc10(instance_id_t const my_id)
{
    CHECK_POINTER(lds_Stazione_conf.pConfL_P1_C1);
    CHECK_LE(my_id, getNumeroL_P1_C1());
    return lds_Stazione_conf.pConfL_P1_C1[my_id - 1u].mainc10;
}

// ********** Getter parametri classe L_P1_C2 **********

Intero L_P1__GetParamSubcl4(instance_id_t const my_id)
{
    CHECK_POINTER(lds_Stazione_conf.pConfL_P1_C2);
    CHECK_LE(my_id, getNumeroL_P1_C2());
    return lds_Stazione_conf.pConfL_P1_C2[my_id - 1u].subcl4;
}

C2_Enumerat1 L_P1__GetParamSubcl5(instance_id_t const my_id)
{
    CHECK_POINTER(lds_Stazione_conf.pConfL_P1_C2);
    CHECK_LE(my_id, getNumeroL_P1_C2());
    return lds_Stazione_conf.pConfL_P1_C2[my_id - 1u].subcl5;
}

Intero L_P1__GetParamSubcl6(instance_id_t const my_id)
{
    CHECK_POINTER(lds_Stazione_conf.pConfL_P1_C2);
    CHECK_LE(my_id, getNumeroL_P1_C2());
    return lds_Stazione_conf.pConfL_P1_C2[my_id - 1u].subcl6;
}



// ********** Procedure di attach **********

static void CdlConfAttach() {
    memset(&lds_Stazione_conf, 0, sizeof(ldsStazioneConfData)); 

    lds_Stazione_conf.pConfHeader = (lds_config_enti_header*) PlatformGetConfigArea(MstGetCurrentStationId(TASK_ID_LDS), FEASCFG);
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

// ********** Interfaccia pubblica **********

void StazioneConfAndDataAttach() {

    CdlConfAttach();
    CdlDataInit();
    CdlDataAttach();
}


