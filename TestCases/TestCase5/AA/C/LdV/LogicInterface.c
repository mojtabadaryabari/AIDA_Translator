// Codice del modello 'TestCase5', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#include "LogicInterface.h"
#include "Stazione/include/interface.h"
#include "PlatformConst.h"
#include "PlatformMacros.h"
#include "PlatformMngConfiguration.h"
#include "MstAreaAccess.h"
#include "PlatformMngArea.h"

void ldv_LogicInit(void)
{
    uint8_t *pConfHeader = PlatformGetConfigArea(MstGetCurrentStationId(TASK_ID_LDS), "LDSCORE");
    CHECK_POINTER(pConfHeader);
    uint8_t byteId = *pConfHeader;
    PlantType plantType = (PlantType) byteId;

    switch (plantType) {
    case Stazione:
        Stazione_ldv_Init();
        break;

    default:
        STOP_EXECUTION(LOGIC_BAD_PLANT_TYPE);
        break;
    }
}

void ldv_LogicExec(void)
{
    uint8_t *pConfHeader = PlatformGetConfigArea(MstGetCurrentStationId(TASK_ID_LDS), "LDSCORE");
    CHECK_POINTER(pConfHeader);
    uint8_t byteId = *pConfHeader;
    PlantType plantType = (PlantType) byteId;

    switch (plantType) {
    case Stazione:
        Stazione_ldv_Exec();
        break;

    default:
        STOP_EXECUTION(LOGIC_BAD_PLANT_TYPE);
        break;
    }
}

