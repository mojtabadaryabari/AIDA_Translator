#ifndef LIBSTAZIONE_CONFIG_H
#define LIBSTAZIONE_CONFIG_H

#include "lds_param.h"
#include "Logica/ClasseLDV_MainClass_C1_priv.h"


// ********** Struct per i parametri della logica **********

typedef struct ldvStazioneConfData {
    ldv_config_enti_header *pConfHeader;

    Classe_L_P1_C3_Param *pConfL_P1_C3;
} ldvStazioneConfData;

extern ldvStazioneConfData ldv_Stazione_conf;


// ********** Struct per i dati della logica **********

typedef struct ldvStazioneOffsets {
    global_id_t L_P1_C3;
} ldvStazioneOffsets;

typedef struct ldvStazioneData {
    Classe_L_P1_C3 *L_P1_C3;
    global_id_t numero_istanze;
    ldvStazioneOffsets base;
} ldvStazioneData;

extern ldvStazioneData *ldv_Stazione_data;


// ********** Getter numero di istanze **********

instance_id_t getNumeroL_P1_C3(void);


// ********** Macro di conversione indici locali/globali **********

// instance_id_t GLOBAL_TO_L_P1_C3(global_id_t id)
#define GLOBAL_TO_L_P1_C3(id)  \
    ((id) - ldv_Stazione_data->base.L_P1_C3)

// global_id_t L_P1_C3_TO_GLOBAL(instance_id_t id)
#define L_P1_C3_TO_GLOBAL(id)  \
    (ldv_Stazione_data->base.L_P1_C3 + (id))


#endif // LIBSTAZIONE_CONFIG_H
