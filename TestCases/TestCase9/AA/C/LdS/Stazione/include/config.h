// Codice del modello 'TestCase9', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#ifndef LIBSTAZIONE_CONFIG_H
#define LIBSTAZIONE_CONFIG_H

#include "lds_param.h"
#include "Logica/ClasseMainClass_C1_priv.h"


// ********** Struct per i parametri della logica **********

typedef struct ldsStazioneConfData {
    lds_config_enti_header *pConfHeader;

    Classe_L_P1_C1_Param *pConfL_P1_C1;
} ldsStazioneConfData;

extern ldsStazioneConfData lds_Stazione_conf;


// ********** Struct per i dati della logica **********

typedef struct ldsStazioneOffsets {
    global_id_t L_P1_C1;
} ldsStazioneOffsets;

typedef struct ldsStazioneData {
    Classe_L_P1_C1 *L_P1_C1;
    global_id_t numero_istanze;
    ldsStazioneOffsets base;
} ldsStazioneData;

extern ldsStazioneData *lds_Stazione_data;


// ********** Getter numero di istanze **********

instance_id_t getNumeroL_P1_C1(void);


// ********** Macro di conversione indici locali/globali **********

// instance_id_t GLOBAL_TO_L_P1_C1(global_id_t id)
#define GLOBAL_TO_L_P1_C1(id)  \
    ((id) - lds_Stazione_data->base.L_P1_C1)

// global_id_t L_P1_C1_TO_GLOBAL(instance_id_t id)
#define L_P1_C1_TO_GLOBAL(id)  \
    (lds_Stazione_data->base.L_P1_C1 + (id))


#endif // LIBSTAZIONE_CONFIG_H
