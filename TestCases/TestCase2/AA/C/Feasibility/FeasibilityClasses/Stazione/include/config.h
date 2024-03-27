// Codice del modello 'TestCase2', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
#ifndef LIBSTAZIONE_CNF_H
#define LIBSTAZIONE_CNF_H

#include "lds_param.h"
#include "Logica/ClasseMainClass_C1_priv.h"
#include "Logica/ClasseSubClass_C2_priv.h"
#include "Logica/ClasseSubClass_C3_priv.h"

#if !defined(UNUSED)
/* This is used to silencing warnings about unused parameters */
#  define UNUSED(expr)  \
    (void)(expr)
#endif

// ********** Struct per i parametri della logica **********

typedef struct ldsStazioneConfData {
    lds_config_enti_header *pConfHeader;

    Classe_L_P1_C1_Param *pConfL_P1_C1;
    Classe_L_P1_C2_Param *pConfL_P1_C2;
    Classe_L_P1_C3_Param *pConfL_P1_C3;
} ldsStazioneConfData;

extern ldsStazioneConfData lds_Stazione_conf;


// ********** Struct per i dati della logica **********
typedef struct ldsStazioneOffsets {
    global_id_t L_P1_C1;
    global_id_t L_P1_C2;
    global_id_t L_P1_C3;
} ldsStazioneOffsets;

typedef struct ldsStazioneData {
    Classe_L_P1_C1 *L_P1_C1;
    Classe_L_P1_C2 *L_P1_C2;
    Classe_L_P1_C3 *L_P1_C3;
    global_id_t numero_istanze;
    ldsStazioneOffsets base;
} ldsStazioneData;

extern ldsStazioneData *lds_Stazione_data;


// ********** Getter numero di istanze **********

instance_id_t getNumeroL_P1_C1(void);
instance_id_t getNumeroL_P1_C2(void);
instance_id_t getNumeroL_P1_C3(void);


// ********** Macro di conversione indici locali/globali **********

// instance_id_t GLOBAL_TO_L_P1_C1(global_id_t id)
#define GLOBAL_TO_L_P1_C1(id)  \
    ((id) - lds_Stazione_data->base.L_P1_C1)
// instance_id_t GLOBAL_TO_L_P1_C2(global_id_t id)
#define GLOBAL_TO_L_P1_C2(id)  \
    ((id) - lds_Stazione_data->base.L_P1_C2)
// instance_id_t GLOBAL_TO_L_P1_C3(global_id_t id)
#define GLOBAL_TO_L_P1_C3(id)  \
    ((id) - lds_Stazione_data->base.L_P1_C3)

// global_id_t L_P1_C1_TO_GLOBAL(instance_id_t id)
#define L_P1_C1_TO_GLOBAL(id)  \
    (lds_Stazione_data->base.L_P1_C1 + (id))
// global_id_t L_P1_C2_TO_GLOBAL(instance_id_t id)
#define L_P1_C2_TO_GLOBAL(id)  \
    (lds_Stazione_data->base.L_P1_C2 + (id))
// global_id_t L_P1_C3_TO_GLOBAL(instance_id_t id)
#define L_P1_C3_TO_GLOBAL(id)  \
    (lds_Stazione_data->base.L_P1_C3 + (id))


#endif // LIBSTAZIONE_CONFIG_H
