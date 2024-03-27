
#ifndef PREAMBLE_H
#define PREAMBLE_H

#include <stdint.h>

/** This structure contains information about version.
 *
 * This is used in configuration to hold version of Generic Application and
 * Specific Application */
typedef struct {
    uint8_t major;
    uint8_t minor;
    uint8_t micro;
    uint8_t _reserved;
} T_VersionInfo;


/** Preable of the header of the PlantType configuration
 *
 * This contains information for version and plan. The preable must be the first
 * field of the header, positioned at offset 0 */
typedef struct {
    T_VersionInfo version_ga;  /*!< Version of the Generic Application */
    T_VersionInfo version_sa;  /*!< Version of the Specific Application */
    uint8_t plant_type;  /*!< ID of the PlantType */
    uint8_t station_id;  /*!< ID of the station/plant */
} T_HeaderPreamble;

#endif // LOGIC_INTERFACE_H
