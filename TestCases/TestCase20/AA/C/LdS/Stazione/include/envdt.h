// Codice del modello 'TestCase20', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#ifndef LIBSTAZIONE_ENVDT_H
#define LIBSTAZIONE_ENVDT_H

#include "logic_utils.h"

// ********** Enumerazioni **********

// State Enumerators
typedef enum {
    C1_St_state = 0,
    C1_St_Stato = 1
} C1_Stateenu;			



// Unique Ordered Set Enumeration
typedef enum {
    ac = 0,
    rosso = 1,
    avanzamento = 2,
    c180x = 3,
    spento = 4,
    verde = 5,
    c180 = 6,
    rossogiallo = 7,
    c120 = 8,
    c270x = 9
} GlobalEnumeration;


typedef GlobalEnumeration C1_Enumerat;
typedef GlobalEnumeration C1_Enumerat1;
typedef GlobalEnumeration C1_Enumerat2;
typedef GlobalEnumeration C1_Enumerat3;
typedef GlobalEnumeration C1_Enumerat4;


#endif // LIBSTAZIONE_ENVDT_H
