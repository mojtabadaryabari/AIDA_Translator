// Codice del modello 'TestCase3', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#ifndef LIBSTAZIONE_CONFIG_H
#define LIBSTAZIONE_CONFIG_H

#include "lds_param.h"


// ********** Struct per i parametri della logica **********

typedef struct ldvStazioneConfData {
    ldv_config_enti_header *pConfHeader;

} ldvStazioneConfData;

extern ldvStazioneConfData ldv_Stazione_conf;


// ********** Struct per i dati della logica **********


typedef struct ldvStazioneData {
    global_id_t numero_istanze;
} ldvStazioneData;

extern ldvStazioneData *ldv_Stazione_data;


// ********** Getter numero di istanze **********



// ********** Macro di conversione indici locali/globali **********




#endif // LIBSTAZIONE_CONFIG_H
