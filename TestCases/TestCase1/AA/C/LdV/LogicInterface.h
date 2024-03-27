// Codice del modello 'TestCase1', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#ifndef LOGIC_INTERFACE_H
#define LOGIC_INTERFACE_H

// TODO: spostare in PlatformConst
#define LOGIC_BAD_PLANT_TYPE  (101)

typedef enum {
    Stazione = 1 } PlantType;

// Init procedure for Lds/Ldv
void ldv_LogicInit(void);

// Exec procedure for Lds/Ldv
void ldv_LogicExec(void);


#endif // LOGIC_INTERFACE_H
