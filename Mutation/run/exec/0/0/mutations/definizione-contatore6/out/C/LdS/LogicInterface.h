#ifndef LOGIC_INTERFACE_H
#define LOGIC_INTERFACE_H

#include "preamble.h"

// TODO: spostare in PlatformConst
#define LOGIC_BAD_PLANT_TYPE  (101)

typedef enum {
    Stazione = 1 } PlantType;

// Init procedure for Lds/Ldv
void lds_LogicInit(void);

// Exec procedure for Lds/Ldv
void lds_LogicExec(void);


#endif // LOGIC_INTERFACE_H
