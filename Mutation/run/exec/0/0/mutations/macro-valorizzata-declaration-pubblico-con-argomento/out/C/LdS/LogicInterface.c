#include "LogicInterface.h"
#include "Stazione/include/interface.h"
#include "PlatformConst.h"
#include "PlatformMacros.h"
#include "PlatformMngConfiguration.h"
#include "MstAreaAccess.h"
#include "PlatformMngArea.h"

void lds_LogicInit(void)
{
    const T_HeaderPreamble * const pConfHeaderPre = (T_HeaderPreamble *) \
        PlatformGetConfigArea(MstGetCurrentStationId(TASK_ID_LDS), "LDSCORE");
    CHECK_POINTER(pConfHeaderPre);

    switch (pConfHeaderPre->plant_type) {
    case Stazione:
        Stazione_lds_Init();
        break;

    default:
        STOP_EXECUTION(LOGIC_BAD_PLANT_TYPE);
        break;
    }
}

void lds_LogicExec(void)
{
     const T_HeaderPreamble * const pConfHeaderPre = (T_HeaderPreamble *) \
        PlatformGetConfigArea(MstGetCurrentStationId(TASK_ID_LDS), "LDSCORE");
    CHECK_POINTER(pConfHeaderPre);

    switch (pConfHeaderPre->plant_type) {
    case Stazione:
        Stazione_lds_Exec();
        break;

    default:
        STOP_EXECUTION(LOGIC_BAD_PLANT_TYPE);
        break;
    }
}

