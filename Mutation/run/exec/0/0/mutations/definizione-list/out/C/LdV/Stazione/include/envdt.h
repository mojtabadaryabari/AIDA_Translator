#ifndef LIBSTAZIONE_ENVDT_H
#define LIBSTAZIONE_ENVDT_H

#include "logic_utils.h"

// ********** Enumerazioni **********

// State Enumerators
typedef enum {
    C3_St_state = 0,
    C3_St_Stato = 1
} C3_Stateenu;			



// Unique Ordered Set Enumeration
typedef enum {
    avvio = 0,
    spento = 1,
    rossogiallo = 2,
    c75giallo = 3,
    rossogiallo3 = 4,
    rossogiallo4 = 5,
    giallogiall = 6,
    avanzamento = 7,
    gialloaverd = 8,
    rossogiallo1 = 9,
    avviox = 10,
    rossogiallo5 = 11,
    rosso = 12,
    c120 = 13,
    rossogiallo2 = 14,
    c120x = 15,
    ac = 16,
    gialloverde = 17,
    giallox = 18,
    rossoverde = 19,
    c180x = 20,
    c270x = 21,
    c270 = 22,
    c270xx = 23,
    verde = 24,
    gialloxverd = 25,
    avanzamento1 = 26,
    c180 = 27
} GlobalEnumeration;


typedef GlobalEnumeration C3_Enumerat;
typedef GlobalEnumeration C3_Enumerat1;
typedef GlobalEnumeration C3_Enumerat2;
typedef GlobalEnumeration C3_Enumerat3;
typedef GlobalEnumeration C3_Enumerat4;


#endif // LIBSTAZIONE_ENVDT_H
