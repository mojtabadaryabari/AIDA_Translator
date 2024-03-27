# Codice del modello 'TestCase7', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
from enum import IntEnum
from GlobalEnums import GlobalEnumeration
from core.lds.acc_class import ParamRecord, srf_value_macro
from core.lds.process_impl import ProcessImpl
from core.runtime.scheduler import ERROR, DISCARDED
from core.runtime.utils import all_notempty
from core.lds.Timer import Timer
from core.lds.Counter import Counter
import Stazione.LdS.Logica.Enumeratives
import os
from core.debugger.debinfo import (  # noqa: F401
    DIBoolExpr, DIExpr, DIStatement, EventDebInfo, TransPhase,
    TransDebInfo, CdLDebInfo, DIVerifyMacro, DIEffectMacro, DIValueMacro,
    add_instance_deb_info, db)

class SubClass_C2(ProcessImpl):
    # ProcessImpl is the class that is extended.
    # ProcessImpl contains the get/set methods for the current state variable and
    # the methods that generate the responses
    def __init__(self, *args, **kwds):
        super(SubClass_C2, self).__init__(*args, **kwds)

        # initialize the state variables

        self.set_subclass_c2_previousva_pv1(GlobalEnumeration.rossogialloverde)
        self.set_subclass_c2_previousva_pv2(False)
        self.set_subclass_c2_previousva_pv3(False)
        self.set_subclass_c2_previousva_pv4(False)
        self.set_subclass_c2_previousva_pv5(GlobalEnumeration.gialloverde)
        self.set_subclass_c2_restoreva_rv1(GlobalEnumeration.c120)
        self.set_subclass_c2_restoreva_rv2(False)
        self.set_subclass_c2_restoreva_rv3(GlobalEnumeration.c120)
        self.set_subclass_c2_restoreva_rv4(GlobalEnumeration.c120)
        self.set_subclass_c2_restoreva_rv5(False)
        self.set_subclass_c2_variabile_v1(False)
        self.set_subclass_c2_variabile_v4(0)
        self.set_subclass_c2_variabile_v5(0)
        self.set_subclass_c2_variabile_v8(0)
        self.set_subclass_c2_variabile_v9(GlobalEnumeration.gialloverde)

        self._expected_commands_map = {
            Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1 : set([]),
        }

    def set_expected_cmds_response(self):
        # for each manual command of SubClass_C2
        if self.is_triggered('eventSubclass_c2_command_comm6'):
            self.set_man_cmd_response('eventSubclass_c2_command_comm6',self.ManCmdResponse.UNEXPECTED)
        else:
            self.set_man_cmd_response('eventSubclass_c2_command_comm6',self.ManCmdResponse.NOOP)



    # enumerative class used by the current init transition variable
    # T_Undef is the value used when the current init transition variable is initialized
    # the other value is the name of the init transition of the state machine
    class InitTransition(IntEnum):
        T_Undef = 0
        _StatoIniziale__State1__initializationSheet__initialization__transitionTo_0 = 1

    # enumerative class used by the current transition variable
    # T_Undef is the value used when the current transition variable is initialized
    # the other values are the names of the transitions of the state machine
    class Transition(IntEnum):
        T_Undef = 0
        _State1__State1__stateSheet_0__permanence = 1

    # method called by the configurator before the use of the scheduler
    # it creates the references of the processes needed
    def init_configuration(self, subclass_c2_lista_l10, subclass_c2_lista_l3, subclass_c2_lista_l4, subclass_c2_lista_l5, subclass_c2_lista_l8, subclass_c2_parametro_p1, subclass_c2_parametro_p2, subclass_c2_parametro_p4, subclass_c2_parametro_p6):
        # initialize the record type parameters
        self.set_subclass_c2_lista_l10(subclass_c2_lista_l10)
        self.set_subclass_c2_lista_l3(subclass_c2_lista_l3)
        self.set_subclass_c2_lista_l4(subclass_c2_lista_l4)
        self.set_subclass_c2_lista_l5(subclass_c2_lista_l5)
        self.set_subclass_c2_lista_l8(subclass_c2_lista_l8)
        # initialize the simple type parameters
        self.set_subclass_c2_parametro_p1(subclass_c2_parametro_p1)
        self.set_subclass_c2_parametro_p2(subclass_c2_parametro_p2)
        self.set_subclass_c2_parametro_p4(subclass_c2_parametro_p4)
        self.set_subclass_c2_parametro_p6(subclass_c2_parametro_p6)

        # initialize the timers
        self.set_subclass_c2_restoreti_ti1(4041000)
        self.set_subclass_c2_restoreti_ti1_restore(4041000)
        self.set_subclass_c2_timer_t10(4041000)
        self.set_subclass_c2_timer_t2(253000)
        self.set_subclass_c2_timer_t4(42000)

        self.timers = [self.subclass_c2_restoreti_ti1,self.subclass_c2_restoreti_ti1_restore,self.subclass_c2_timer_t10,self.subclass_c2_timer_t2,self.subclass_c2_timer_t4,]

        # initialize the counters
        self.set_subclass_c2_contatore_co2(0)
        self.set_subclass_c2_contatore_co6(0)
        self.set_subclass_c2_contatore_co7(0)

    # setters for record type parameters
    def set_subclass_c2_lista_l10(self, subclass_c2_lista_l10):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l10",subclass_c2_lista_l10)

    def set_subclass_c2_lista_l3(self, subclass_c2_lista_l3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l3",subclass_c2_lista_l3)

    def set_subclass_c2_lista_l4(self, subclass_c2_lista_l4):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l4",subclass_c2_lista_l4)

    def set_subclass_c2_lista_l5(self, subclass_c2_lista_l5):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l5",subclass_c2_lista_l5)

    def set_subclass_c2_lista_l8(self, subclass_c2_lista_l8):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l8",subclass_c2_lista_l8)


    # getters for record type parameters
    def get_subclass_c2_lista_l10(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l10")

    def get_subclass_c2_lista_l3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l3")

    def get_subclass_c2_lista_l4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l4")

    def get_subclass_c2_lista_l5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l5")

    def get_subclass_c2_lista_l8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l8")


    # setters for simple type parameters
    def set_subclass_c2_parametro_p1(self, subclass_c2_parametro_p1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p1",subclass_c2_parametro_p1)

    def set_subclass_c2_parametro_p2(self, subclass_c2_parametro_p2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p2",subclass_c2_parametro_p2)

    def set_subclass_c2_parametro_p4(self, subclass_c2_parametro_p4):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p4",subclass_c2_parametro_p4)

    def set_subclass_c2_parametro_p6(self, subclass_c2_parametro_p6):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p6",subclass_c2_parametro_p6)


    # getters for simple type parameters
    def get_subclass_c2_parametro_p1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p1")

    def get_subclass_c2_parametro_p2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p2")

    def get_subclass_c2_parametro_p4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p4")

    def get_subclass_c2_parametro_p6(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p6")


    # setters for comandi al piazzale
    def set_subclass_c2_comando_c7(self, subclass_c2_comando_c7):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_comando_c7",subclass_c2_comando_c7)

    def set_subclass_c2_comando_c9(self, subclass_c2_comando_c9):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_comando_c9",subclass_c2_comando_c9)


    # getters for controlli dal piazzale
    def get_consdef(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"consdef")

    def get_subclass_c2_controllo_c2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_controllo_c2")

    def get_subclass_c2_controllo_c5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_controllo_c5")

    def get_subclass_c2_controllo_c6(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_controllo_c6")

    def get_subclass_c2_previousco_c1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c1")

    def get_subclass_c2_previousco_c10(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c10")

    def get_subclass_c2_previousco_c4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c4")


    # setters for state variables
    def set_subclass_c2_previousco_c1_prev(self, subclass_c2_previousco_c1_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c1_prev",subclass_c2_previousco_c1_prev)
    def set_subclass_c2_previousco_c10_prev(self, subclass_c2_previousco_c10_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c10_prev",subclass_c2_previousco_c10_prev)
    def set_subclass_c2_previousco_c4_prev(self, subclass_c2_previousco_c4_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c4_prev",subclass_c2_previousco_c4_prev)
    def set_subclass_c2_previousva_pv1(self, subclass_c2_previousva_pv1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousva_pv1",subclass_c2_previousva_pv1)
    def set_subclass_c2_previousva_pv1_prev(self, subclass_c2_previousva_pv1_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousva_pv1_prev",subclass_c2_previousva_pv1_prev)
    def set_subclass_c2_previousva_pv2(self, subclass_c2_previousva_pv2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousva_pv2",subclass_c2_previousva_pv2)
    def set_subclass_c2_previousva_pv2_prev(self, subclass_c2_previousva_pv2_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousva_pv2_prev",subclass_c2_previousva_pv2_prev)
    def set_subclass_c2_previousva_pv3(self, subclass_c2_previousva_pv3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousva_pv3",subclass_c2_previousva_pv3)
    def set_subclass_c2_previousva_pv3_prev(self, subclass_c2_previousva_pv3_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousva_pv3_prev",subclass_c2_previousva_pv3_prev)
    def set_subclass_c2_previousva_pv4(self, subclass_c2_previousva_pv4):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousva_pv4",subclass_c2_previousva_pv4)
    def set_subclass_c2_previousva_pv4_prev(self, subclass_c2_previousva_pv4_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousva_pv4_prev",subclass_c2_previousva_pv4_prev)
    def set_subclass_c2_previousva_pv5(self, subclass_c2_previousva_pv5):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousva_pv5",subclass_c2_previousva_pv5)
    def set_subclass_c2_previousva_pv5_prev(self, subclass_c2_previousva_pv5_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousva_pv5_prev",subclass_c2_previousva_pv5_prev)
    def set_subclass_c2_restoreva_rv1(self, subclass_c2_restoreva_rv1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_restoreva_rv1",subclass_c2_restoreva_rv1)
    def set_subclass_c2_restoreva_rv2(self, subclass_c2_restoreva_rv2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_restoreva_rv2",subclass_c2_restoreva_rv2)
    def set_subclass_c2_restoreva_rv3(self, subclass_c2_restoreva_rv3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_restoreva_rv3",subclass_c2_restoreva_rv3)
    def set_subclass_c2_restoreva_rv4(self, subclass_c2_restoreva_rv4):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_restoreva_rv4",subclass_c2_restoreva_rv4)
    def set_subclass_c2_restoreva_rv5(self, subclass_c2_restoreva_rv5):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_restoreva_rv5",subclass_c2_restoreva_rv5)
    def set_subclass_c2_variabile_v1(self, subclass_c2_variabile_v1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v1",subclass_c2_variabile_v1)
    def set_subclass_c2_variabile_v4(self, subclass_c2_variabile_v4):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v4",subclass_c2_variabile_v4)
    def set_subclass_c2_variabile_v5(self, subclass_c2_variabile_v5):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v5",subclass_c2_variabile_v5)
    def set_subclass_c2_variabile_v8(self, subclass_c2_variabile_v8):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v8",subclass_c2_variabile_v8)
    def set_subclass_c2_variabile_v9(self, subclass_c2_variabile_v9):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v9",subclass_c2_variabile_v9)

    # getters for state variables
    def get_stato_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"stato_restore")

    def get_subclass_c2_previousco_c1_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c1_prev")

    def get_subclass_c2_previousco_c10_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c10_prev")

    def get_subclass_c2_previousco_c4_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c4_prev")

    def get_subclass_c2_previousva_pv1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousva_pv1")

    def get_subclass_c2_previousva_pv1_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousva_pv1_prev")

    def get_subclass_c2_previousva_pv2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousva_pv2")

    def get_subclass_c2_previousva_pv2_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousva_pv2_prev")

    def get_subclass_c2_previousva_pv3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousva_pv3")

    def get_subclass_c2_previousva_pv3_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousva_pv3_prev")

    def get_subclass_c2_previousva_pv4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousva_pv4")

    def get_subclass_c2_previousva_pv4_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousva_pv4_prev")

    def get_subclass_c2_previousva_pv5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousva_pv5")

    def get_subclass_c2_previousva_pv5_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousva_pv5_prev")

    def get_subclass_c2_restoreva_rv1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_restoreva_rv1")

    def get_subclass_c2_restoreva_rv1_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_restoreva_rv1_restore")

    def get_subclass_c2_restoreva_rv2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_restoreva_rv2")

    def get_subclass_c2_restoreva_rv2_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_restoreva_rv2_restore")

    def get_subclass_c2_restoreva_rv3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_restoreva_rv3")

    def get_subclass_c2_restoreva_rv3_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_restoreva_rv3_restore")

    def get_subclass_c2_restoreva_rv4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_restoreva_rv4")

    def get_subclass_c2_restoreva_rv4_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_restoreva_rv4_restore")

    def get_subclass_c2_restoreva_rv5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_restoreva_rv5")

    def get_subclass_c2_restoreva_rv5_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_restoreva_rv5_restore")

    def get_subclass_c2_variabile_v1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v1")

    def get_subclass_c2_variabile_v4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v4")

    def get_subclass_c2_variabile_v5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v5")

    def get_subclass_c2_variabile_v8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v8")

    def get_subclass_c2_variabile_v9(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v9")


    # setters for timers
    def set_subclass_c2_restoreti_ti1(self, timerDuration):
        self.subclass_c2_restoreti_ti1 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_restoreti_ti1", self.memory)

    def set_subclass_c2_restoreti_ti1_restore(self, timerDuration):
        self.subclass_c2_restoreti_ti1_restore = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_restoreti_ti1_restore", self.memory)

    def set_subclass_c2_timer_t10(self, timerDuration):
        self.subclass_c2_timer_t10 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_timer_t10", self.memory)

    def set_subclass_c2_timer_t2(self, timerDuration):
        self.subclass_c2_timer_t2 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_timer_t2", self.memory)

    def set_subclass_c2_timer_t4(self, timerDuration):
        self.subclass_c2_timer_t4 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_timer_t4", self.memory)


    # getters for timers
    def get_subclass_c2_restoreti_ti1(self):
        return self.subclass_c2_restoreti_ti1

    def get_subclass_c2_restoreti_ti1_restore(self):
        return self.subclass_c2_restoreti_ti1_restore

    def get_subclass_c2_timer_t10(self):
        return self.subclass_c2_timer_t10

    def get_subclass_c2_timer_t2(self):
        return self.subclass_c2_timer_t2

    def get_subclass_c2_timer_t4(self):
        return self.subclass_c2_timer_t4


    # setters for counters
    def set_subclass_c2_contatore_co2(self, counterInitValue):
        self.subclass_c2_contatore_co2 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "subclass_c2_contatore_co2", self.memory)

    def set_subclass_c2_contatore_co6(self, counterInitValue):
        self.subclass_c2_contatore_co6 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "subclass_c2_contatore_co6", self.memory)

    def set_subclass_c2_contatore_co7(self, counterInitValue):
        self.subclass_c2_contatore_co7 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "subclass_c2_contatore_co7", self.memory)


    # getters for counters
    def get_subclass_c2_contatore_co2(self):
        return self.subclass_c2_contatore_co2

    def get_subclass_c2_contatore_co6(self):
        return self.subclass_c2_contatore_co6

    def get_subclass_c2_contatore_co7(self):
        return self.subclass_c2_contatore_co7



    def is_current_state(self, stateval):
        res = self.get_fsmState() == stateval
        if res:
            self._expected_commands = self._expected_commands_map[stateval]
        return res

    # method called by the scheduler before the method delta_cycle()
    def init(self, env_state):
        self.dbs = (
                    DIBoolExpr("""NAryLogicOP (AND)\nNessuna""", [
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nNessuna""", [
                    ]),#1
                    DIStatement("""ITStatement\n/*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è  uguale a  /*53,*/  state1 , /*72,*/Azzera il contatore SubClass_C2_contatore_Co7""", [
                    DIBoolExpr("""ForAllPredicateNotEmptyImpl\nlo stato del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è  uguale a  /*53,*/  state1""", [
                    DIBoolExpr("""EqualImpl\n(lo stato di 'mainclass_c1 della lista subclass_c2_lista_l8')  è uguale a  (state1)""", [
                    ]),#0
                    ]),#0
                    ]),#2
                    DIStatement("""ITEStatementImpl\n/*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV3 non è  uguale a Verde e  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C2_contatore_Co6 non è  minore di  /*55,*/ 1253, /*66,*/ Assegna al comando SubClass_C2_comando_C9 il valore  True 

 ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V9 il valore GialloaVerdea""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV3 non è  uguale a Verde e  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C2_contatore_Co6 non è  minore di  /*55,*/ 1253""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( negazione di ((subclass_c2_restoreva_rv3_restore)  è uguale a  (verde)) )  e  
( (consdef)  è uguale a  (False) ) )  o  
( (consdef)  è uguale a  (False) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c2_restoreva_rv3_restore)  è uguale a  (verde)) )  e  
( (consdef)  è uguale a  (False) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_restoreva_rv3_restore)  è uguale a  (verde))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_restoreva_rv3_restore)  è uguale a  (verde)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co6)  è minore di  (1253))""", [
                    DIBoolExpr("""LessThanImpl\n(subclass_c2_contatore_co6)  è minore di  (1253)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    ]),#3
                     )
        add_instance_deb_info(self.station_name, self.name, self.instance_name, CdLDebInfo([
            # transizioni iniziali
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.StatoIniziale, Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1,
                         guard=(self.dbs[0], ),
                         effect=(),
                         phase = TransPhase.Stato
                         ),
            # transizioni della fase manuale
            # transizioni della fase di stato
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1,Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1,
                         guard=(self.dbs[1], ),
                         effect=(self.dbs[2], self.dbs[3], ),
                         phase = TransPhase.Stato
                         ),
            # transizioni della fase automatica
        ]))



        self._responses = []
        # check which are the satisfied conditions
        # to set the current initial transition
        # the if conditions are ordered according with the order of the init transitions

        if(self.guard_INITIALIZATION_StatoIniziale_state1_000()):
            self.curr_init_transition = self.InitTransition._StatoIniziale__State1__initializationSheet__initialization__transitionTo_0
        else:
            # if the current init transition is not set, an exception will be raised
            return ERROR("the current init transition is not set")

        # check what is the current initial transition
        # to set the current state and to execute the effects of the current initial transition
        if self.curr_init_transition == self.InitTransition.T_Undef:
            # if the current init transition variable is not set, an exception will be raised
            return ERROR("the current init transition variable is not set")
        elif self.curr_init_transition == self.InitTransition._StatoIniziale__State1__initializationSheet__initialization__transitionTo_0:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1)
            self.effect_INITIALIZATION_StatoIniziale_state1_000()
            self.response_wait()

        self.set_subclass_c2_previousco_c1_prev(False)
        self.set_subclass_c2_previousco_c10_prev(False)
        self.set_subclass_c2_previousco_c4_prev(GlobalEnumeration.rossogiallox)
        self.set_subclass_c2_previousva_pv1_prev(self.get_subclass_c2_previousva_pv1())
        self.set_subclass_c2_previousva_pv2_prev(self.get_subclass_c2_previousva_pv2())
        self.set_subclass_c2_previousva_pv3_prev(self.get_subclass_c2_previousva_pv3())
        self.set_subclass_c2_previousva_pv4_prev(self.get_subclass_c2_previousva_pv4())
        self.set_subclass_c2_previousva_pv5_prev(self.get_subclass_c2_previousva_pv5())

        return self._responses
    # method called by the scheduler the its method execute()
    def execute(self, command, env_state):
        self.begin_execute(command)
        # check what is the current state and which are the satisfied conditions
        # to set the current transition
        # the if conditions are ordered according with the order of the transitions
        if self.is_manual_phase():
            # Set risposte ai comandi manuali
            self.set_expected_cmds_response()
            if self.is_current_state(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1):
                pass #return ERROR("the current state variable is not set (command: %s)" % command)
            else:
                # if the current state variable is not set, an exception will be raised
                return ERROR("the current state variable is not set (command: %s)" % command)

        if self.is_state_phase():
            if self.is_current_state(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1):
                if(self.guard_PERMANENCE_state1_000()):
                    self.curr_transition = self.Transition._State1__State1__stateSheet_0__permanence
            else:
                # if the current state variable is not set, an exception will be raised
                return ERROR("the current state variable is not set (command: %s)" % command)

        if self.is_automatic_phase():
            if self.is_current_state(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1):
                pass #return ERROR("the current state variable is not set (command: %s)" % command)
            else:
                # if the current state variable is not set, an exception will be raised
                return ERROR("the current state variable is not set (command: %s)" % command)

        # check what is the current transition
        # to set the current state and to execute the effects of the current transition
        if self.curr_transition == self.Transition.T_Undef:
            # if the current transition variable is not set, an exception will be raised
            return DISCARDED(self._logger, command, self.get_fsmState(), self._command_unexpected)
        elif self.curr_transition == self.Transition._State1__State1__stateSheet_0__permanence:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1)
            self.effect_PERMANENCE_state1_000()
            self.response_wait()
  
        return self.end_execute()
    # for each guard, the corresponding method is created
    def guard_INITIALIZATION_StatoIniziale_state1_000(self):
        """
        CNL corrispondente:
        
         {
         Nessuna 
         }
        """
        return db((True), self.dbs[0])
    
    def guard_PERMANENCE_state1_000(self):
        """
        CNL corrispondente:
        
        {
        	
        
         Nessuna 
        }
        """
        return db((True), self.dbs[1])
    
    # for each effect, the corresponding method is created
    def effect_INITIALIZATION_StatoIniziale_state1_000(self):
        """
        CNL corrispondente:
        
         {
         Nessuna 
         }
        """
        pass
    
    def effect_PERMANENCE_state1_000(self):
        """
        CNL corrispondente:
        
        {
        
         commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  commento: {105,} è  uguale a  commento: {53,}  state1 , commento: {72,}Azzera il contatore SubClass_C2_contatore_Co7
        
           
         commento: {109,}  se il ripristino della variabile  SubClass_C2_restoreva_RV3 non è  uguale a Verde e  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} o  se il contatore SubClass_C2_contatore_Co6 non è  minore di  commento: {55,} 1253, commento: {66,} Assegna al comando SubClass_C2_comando_C9 il valore  True 
        
         ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V9 il valore GialloaVerdea
        
        
        
        }
        """
        #  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è  uguale a  /*53,*/  state1 , /*72,*/Azzera il contatore SubClass_C2_contatore_Co7
        if db(all_notempty(db(it.get_mainclass_c1().get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, self.dbs[2].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l8())), self.dbs[2].subs[0]):
            self.get_subclass_c2_contatore_co7().resetta()
        #  /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV3 non è  uguale a Verde e  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C2_contatore_Co6 non è  minore di  /*55,*/ 1253, /*66,*/ Assegna al comando SubClass_C2_comando_C9 il valore  True 
        #   ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V9 il valore GialloaVerdea
        if db((db((db((db(not db(self.get_subclass_c2_restoreva_rv3_restore() == GlobalEnumeration.verde, self.dbs[3].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[3].subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, self.dbs[3].subs[0].subs[0].subs[0].subs[1])), self.dbs[3].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, self.dbs[3].subs[0].subs[0].subs[1])), self.dbs[3].subs[0].subs[0]) or db(not db(self.get_subclass_c2_contatore_co6().get_valore() < 1253, self.dbs[3].subs[0].subs[1].subs[0]), self.dbs[3].subs[0].subs[1])), self.dbs[3].subs[0]):
            self.set_subclass_c2_comando_c9(True)
        else:
            self.set_subclass_c2_variabile_v9(GlobalEnumeration.gialloaverdea)
    
    # effect macros
    def macroSubclass_c2_macroef_m1(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        {  se la macro  SubClass_C2_macrova_M6 ( con argomento_a10   uguale a GialloVerde ,argomento_a3   uguale a Verde ,argomento_a9   uguale a c120  e argomento_a6   uguale a GialloVerde )   è  uguale a  True  commento: {40,} ,  Applica gli effetti
               della macro SubClass_C2_macroef_M5  commento: {73,}
        
         ,altrimenti  commento: {70,}Incrementa il contatore SubClass_C2_contatore_Co6
        
        
         commento: {37,}  se la variabile SubClass_C2_variabile_V4 è  maggiore di  commento: {54,} 10 commento: {36,} o  se il timer SubClass_C2_timer_T2 è attivo commento: {34,} e  se il parametro SubClass_C2_parametro_P1 non è  uguale a  commento: {53,} 1 commento: {36,} o  se il timer SubClass_C2_timer_T4 è disattivo commento: {38,} o  se il contatore SubClass_C2_contatore_Co6 non è  minore di  commento: {55,} 13, commento: {71,}Decrementa il contatore SubClass_C2_contatore_Co2
        
           
         commento: {42,}  se  MainClass_C1_controllo_C8 del campo  MainClass_C1 di SubClass_C2_lista_L10 è  uguale a RossoGialloGiallo commento: {36,} e  se il timer SubClass_C2_timer_T10 non è scaduto commento: {36,} o  se il timer SubClass_C2_timer_T2 è attivo, commento: {66,} Assegna al comando SubClass_C2_comando_C7 il valore  False 
        
         ,altrimenti   Applica gli effetti
               della macro SubClass_C2_macroef_M5  commento: {73,}
        
        
         commento: {37,}  se la variabile SubClass_C2_variabile_V4 è  maggiore di  commento: {54,} 7 commento: {36,} o  se il timer SubClass_C2_timer_T2 non è attivo commento: {34,} o  se il parametro SubClass_C2_parametro_P6 è  uguale a  commento: {53,} 1, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V5 il valore 8
        
         ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V4 il valore 6
        
        
         commento: {110,}  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è scaduto commento: {37,} o  se la variabile SubClass_C2_variabile_V5 non è  uguale a  commento: {53,} 10 o  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} o  se il parametro SubClass_C2_parametro_P6 non è  uguale a  commento: {53,} 8, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V9 il valore GialloaVerdea
        
         ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V1 il valore  False 
        
        
        
        }
        """
        def populate_macroSubclass_c2_macroef_m1_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITEStatementImpl\nse la macro  SubClass_C2_macrova_M6 ( con argomento_a10   uguale a GialloVerde ,argomento_a3   uguale a Verde ,argomento_a9   uguale a c120  e argomento_a6   uguale a GialloVerde )   è  uguale a  True  /*40,*/ ,  Applica gli effetti
       della macro SubClass_C2_macroef_M5  /*73,*/

 ,altrimenti  /*70,*/Incrementa il contatore SubClass_C2_contatore_Co6""", [
                            DIBoolExpr("""EqualImpl\nla macro  SubClass_C2_macrova_M6 ( con argomento_a10   uguale a GialloVerde ,argomento_a3   uguale a Verde ,argomento_a9   uguale a c120  e argomento_a6   uguale a GialloVerde )   è  uguale a  True""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroSubclass_c2_macrova_m6'"""),#0
                            ]),#0
                            DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro SubClass_C2_macroef_M5"""),#1
                            ]),#0
                            DIStatement("""ITStatement\n/*37,*/  se la variabile SubClass_C2_variabile_V4 è  maggiore di  /*54,*/ 10 /*36,*/ o  se il timer SubClass_C2_timer_T2 è attivo /*34,*/ e  se il parametro SubClass_C2_parametro_P1 non è  uguale a  /*53,*/ 1 /*36,*/ o  se il timer SubClass_C2_timer_T4 è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co6 non è  minore di  /*55,*/ 13, /*71,*/Decrementa il contatore SubClass_C2_contatore_Co2""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*37,*/  se la variabile SubClass_C2_variabile_V4 è  maggiore di  /*54,*/ 10 /*36,*/ o  se il timer SubClass_C2_timer_T2 è attivo /*34,*/ e  se il parametro SubClass_C2_parametro_P1 non è  uguale a  /*53,*/ 1 /*36,*/ o  se il timer SubClass_C2_timer_T4 è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co6 non è  minore di  /*55,*/ 13""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( (subclass_c2_variabile_v4)  è maggiore di  (10) )  o  
( ( il timer 'subclass_c2_timer_t2' è attivo )  e  
( negazione di ((subclass_c2_parametro_p1)  è uguale a  (1)) ) ) )  o  
( il timer 'subclass_c2_timer_t4' è inattivo )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( (subclass_c2_variabile_v4)  è maggiore di  (10) )  o  
( ( il timer 'subclass_c2_timer_t2' è attivo )  e  
( negazione di ((subclass_c2_parametro_p1)  è uguale a  (1)) ) )""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_variabile_v4)  è maggiore di  (10)""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( il timer 'subclass_c2_timer_t2' è attivo )  e  
( negazione di ((subclass_c2_parametro_p1)  è uguale a  (1)) )""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t2' è attivo""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p1)  è uguale a  (1))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p1)  è uguale a  (1)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t4' è inattivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co6)  è minore di  (13))""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_contatore_co6)  è minore di  (13)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#1
                            DIStatement("""ITEStatementImpl\n/*42,*/  se  MainClass_C1_controllo_C8 del campo  MainClass_C1 di SubClass_C2_lista_L10 è  uguale a RossoGialloGiallo /*36,*/ e  se il timer SubClass_C2_timer_T10 non è scaduto /*36,*/ o  se il timer SubClass_C2_timer_T2 è attivo, /*66,*/ Assegna al comando SubClass_C2_comando_C7 il valore  False 

 ,altrimenti   Applica gli effetti
       della macro SubClass_C2_macroef_M5""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*42,*/  se  MainClass_C1_controllo_C8 del campo  MainClass_C1 di SubClass_C2_lista_L10 è  uguale a RossoGialloGiallo /*36,*/ e  se il timer SubClass_C2_timer_T10 non è scaduto /*36,*/ o  se il timer SubClass_C2_timer_T2 è attivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( per ognuna delle seguenti {((mainclass_c1_controllo_c8 del campo mainclass_c1 della lista subclass_c2_lista_l10)  è uguale a  (rossogiallogiallo))} )  e  
( negazione di (il timer 'subclass_c2_timer_t10' è scaduto) )""", [
                            DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {((mainclass_c1_controllo_c8 del campo mainclass_c1 della lista subclass_c2_lista_l10)  è uguale a  (rossogiallogiallo))}""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c8 del campo mainclass_c1 della lista subclass_c2_lista_l10)  è uguale a  (rossogiallogiallo)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c2_timer_t10' è scaduto)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t10' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t2' è attivo""", [
                            ]),#1
                            ]),#0
                            DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro SubClass_C2_macroef_M5"""),#1
                            ]),#2
                            DIStatement("""ITEStatementImpl\n/*73,*/


 /*37,*/  se la variabile SubClass_C2_variabile_V4 è  maggiore di  /*54,*/ 7 /*36,*/ o  se il timer SubClass_C2_timer_T2 non è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P6 è  uguale a  /*53,*/ 1, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V5 il valore 8

 ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V4 il valore 6""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*73,*/


 /*37,*/  se la variabile SubClass_C2_variabile_V4 è  maggiore di  /*54,*/ 7 /*36,*/ o  se il timer SubClass_C2_timer_T2 non è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P6 è  uguale a  /*53,*/ 1""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( (subclass_c2_variabile_v4)  è maggiore di  (7) )  o  
( negazione di (il timer 'subclass_c2_timer_t2' è attivo) )""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_variabile_v4)  è maggiore di  (7)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c2_timer_t2' è attivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t2' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p6)  è uguale a  (1)""", [
                            ]),#1
                            ]),#0
                            ]),#3
                            DIStatement("""ITEStatementImpl\n/*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è scaduto /*37,*/ o  se la variabile SubClass_C2_variabile_V5 non è  uguale a  /*53,*/ 10 o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro SubClass_C2_parametro_P6 non è  uguale a  /*53,*/ 8, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V9 il valore GialloaVerdea

 ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V1 il valore  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è scaduto /*37,*/ o  se la variabile SubClass_C2_variabile_V5 non è  uguale a  /*53,*/ 10 o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro SubClass_C2_parametro_P6 non è  uguale a  /*53,*/ 8""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( il timer 'subclass_c2_restoreti_ti1_restore' è scaduto )  o  
( negazione di ((subclass_c2_variabile_v5)  è uguale a  (10)) ) )  o  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( il timer 'subclass_c2_restoreti_ti1_restore' è scaduto )  o  
( negazione di ((subclass_c2_variabile_v5)  è uguale a  (10)) )""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_restoreti_ti1_restore' è scaduto""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v5)  è uguale a  (10))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v5)  è uguale a  (10)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p6)  è uguale a  (8))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p6)  è uguale a  (8)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#4
                ])

        populate_macroSubclass_c2_macroef_m1_SrfMacroDefInfo(di_ctx)
        #  se la macro  SubClass_C2_macrova_M6 ( con argomento_a10   uguale a GialloVerde ,argomento_a3   uguale a Verde ,argomento_a9   uguale a c120  e argomento_a6   uguale a GialloVerde )   è  uguale a  True  /*40,*/ ,  Applica gli effetti
        #         della macro SubClass_C2_macroef_M5  /*73,*/
        #   ,altrimenti  /*70,*/Incrementa il contatore SubClass_C2_contatore_Co6
        if db(db(self.macroSubclass_c2_macrova_m6(GlobalEnumeration.gialloverde,GlobalEnumeration.verde,GlobalEnumeration.gialloverde,GlobalEnumeration.c120, di_ctx.subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0]) == True, di_ctx.subs[0].subs[0]):
            self.macroSubclass_c2_macroef_m5(di_ctx.subs[0].subs[1])
        else:
            self.get_subclass_c2_contatore_co6().incrementa()
        #  /*37,*/  se la variabile SubClass_C2_variabile_V4 è  maggiore di  /*54,*/ 10 /*36,*/ o  se il timer SubClass_C2_timer_T2 è attivo /*34,*/ e  se il parametro SubClass_C2_parametro_P1 non è  uguale a  /*53,*/ 1 /*36,*/ o  se il timer SubClass_C2_timer_T4 è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co6 non è  minore di  /*55,*/ 13, /*71,*/Decrementa il contatore SubClass_C2_contatore_Co2
        if db((db((db((db(self.get_subclass_c2_variabile_v4() > 10, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0]) or db((db(self.get_subclass_c2_timer_t2().isAttivato(), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_parametro_p1() == 1, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_timer_t4().isDisattivato(), di_ctx.subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0]) or db(not db(self.get_subclass_c2_contatore_co6().get_valore() < 13, di_ctx.subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.get_subclass_c2_contatore_co2().decrementa()
        #  /*42,*/  se  MainClass_C1_controllo_C8 del campo  MainClass_C1 di SubClass_C2_lista_L10 è  uguale a RossoGialloGiallo /*36,*/ e  se il timer SubClass_C2_timer_T10 non è scaduto /*36,*/ o  se il timer SubClass_C2_timer_T2 è attivo, /*66,*/ Assegna al comando SubClass_C2_comando_C7 il valore  False 
        #   ,altrimenti   Applica gli effetti
        #         della macro SubClass_C2_macroef_M5
        if db((db((db(all(db(it.get_mainclass_c1().get_mainclass_c1_controllo_c8() == GlobalEnumeration.rossogiallogiallo, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l10())), di_ctx.subs[2].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_timer_t10().isScaduto(), di_ctx.subs[2].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0]) or db(self.get_subclass_c2_timer_t2().isAttivato(), di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.set_subclass_c2_comando_c7(False)
        else:
            self.macroSubclass_c2_macroef_m5(di_ctx.subs[2].subs[1])
        #  /*73,*/
        #   /*37,*/  se la variabile SubClass_C2_variabile_V4 è  maggiore di  /*54,*/ 7 /*36,*/ o  se il timer SubClass_C2_timer_T2 non è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P6 è  uguale a  /*53,*/ 1, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V5 il valore 8
        #   ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V4 il valore 6
        if db((db((db(self.get_subclass_c2_variabile_v4() > 7, di_ctx.subs[3].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_timer_t2().isAttivato(), di_ctx.subs[3].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[3].subs[0].subs[0].subs[1])), di_ctx.subs[3].subs[0].subs[0]) or db(self.get_subclass_c2_parametro_p6() == 1, di_ctx.subs[3].subs[0].subs[1])), di_ctx.subs[3].subs[0]):
            self.set_subclass_c2_variabile_v5(8)
        else:
            self.set_subclass_c2_variabile_v4(6)
        #  /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è scaduto /*37,*/ o  se la variabile SubClass_C2_variabile_V5 non è  uguale a  /*53,*/ 10 o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro SubClass_C2_parametro_P6 non è  uguale a  /*53,*/ 8, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V9 il valore GialloaVerdea
        #   ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V1 il valore  False
        if db((db((db((db(self.get_subclass_c2_restoreti_ti1_restore().isScaduto(), di_ctx.subs[4].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_variabile_v5() == 10, di_ctx.subs[4].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[4].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[4].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[4].subs[0].subs[0].subs[1])), di_ctx.subs[4].subs[0].subs[0]) or db(not db(self.get_subclass_c2_parametro_p6() == 8, di_ctx.subs[4].subs[0].subs[1].subs[0]), di_ctx.subs[4].subs[0].subs[1])), di_ctx.subs[4].subs[0]):
            self.set_subclass_c2_variabile_v9(GlobalEnumeration.gialloaverdea)
        else:
            self.set_subclass_c2_variabile_v1(False)
    
    def macroSubclass_c2_macroef_m2(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        {  se il controllo ConsDef  è  uguale a FALSE ,  commento: {44,}  se  MainClass_C1_variabile_V1 del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  commento: {105,} è  uguale a  commento: {53,} 4, commento: {88,} quando  commento: {42,}    MainClass_C1_controllo_C8 del campo  MainClass_C1     è  uguale a RossoGialloGiallo commento: {34,} o  se il parametro SubClass_C2_parametro_P2 è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} e  se la variabile SubClass_C2_variabile_V4 non è  uguale a  commento: {53,} 5 commento: {35,} e  se il controllo SubClass_C2_controllo_C2 non è  diverso da GialloaVerdea, commento: {68,}Attiva il timer SubClass_C2_timer_T4
        
           
         commento: {34,}  se il parametro SubClass_C2_parametro_P1 è  diverso da  commento: {56,} 9 commento: {35,} o  se il controllo SubClass_C2_controllo_C2 non è  uguale a GialloaVerdea commento: {35,} e  se il controllo SubClass_C2_controllo_C5 non è  uguale a GialloaVerdea e  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro SubClass_C2_parametro_P1 è  minore di  commento: {55,} 8 commento: {38,} e  se il contatore SubClass_C2_contatore_Co6 è  uguale a  commento: {53,} 12, commento: {72,}Azzera il contatore SubClass_C2_contatore_Co6
        
           
        
        }
        """
        def populate_macroSubclass_c2_macroef_m2_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\nse il controllo ConsDef  è  uguale a FALSE ,  /*44,*/  se  MainClass_C1_variabile_V1 del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  /*105,*/ è  uguale a  /*53,*/ 4, /*88,*/ quando  /*42,*/    MainClass_C1_controllo_C8 del campo  MainClass_C1     è  uguale a RossoGialloGiallo /*34,*/ o  se il parametro SubClass_C2_parametro_P2 è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C2_variabile_V4 non è  uguale a  /*53,*/ 5 /*35,*/ e  se il controllo SubClass_C2_controllo_C2 non è  diverso da GialloaVerdea, /*68,*/Attiva il timer SubClass_C2_timer_T4""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse il controllo ConsDef  è  uguale a FALSE ,  /*44,*/  se  MainClass_C1_variabile_V1 del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  /*105,*/ è  uguale a  /*53,*/ 4, /*88,*/ quando  /*42,*/    MainClass_C1_controllo_C8 del campo  MainClass_C1     è  uguale a RossoGialloGiallo /*34,*/ o  se il parametro SubClass_C2_parametro_P2 è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C2_variabile_V4 non è  uguale a  /*53,*/ 5 /*35,*/ e  se il controllo SubClass_C2_controllo_C2 non è  diverso da GialloaVerdea""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  
( per ognuna delle seguenti con lista non vuota {se ((mainclass_c1_controllo_c8 del campo mainclass_c1 della lista subclass_c2_lista_l10)  è uguale a  (rossogiallogiallo)) allora ((mainclass_c1_variabile_v1 del campo mainclass_c1 della lista subclass_c2_lista_l10)  è uguale a  (4))} )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {se ((mainclass_c1_controllo_c8 del campo mainclass_c1 della lista subclass_c2_lista_l10)  è uguale a  (rossogiallogiallo)) allora ((mainclass_c1_variabile_v1 del campo mainclass_c1 della lista subclass_c2_lista_l10)  è uguale a  (4))}""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\nse ((mainclass_c1_controllo_c8 del campo mainclass_c1 della lista subclass_c2_lista_l10)  è uguale a  (rossogiallogiallo)) allora ((mainclass_c1_variabile_v1 del campo mainclass_c1 della lista subclass_c2_lista_l10)  è uguale a  (4))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c8 del campo mainclass_c1 della lista subclass_c2_lista_l10)  è uguale a  (rossogiallogiallo)""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v1 del campo mainclass_c1 della lista subclass_c2_lista_l10)  è uguale a  (4)""", [
                            ]),#1
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( ( (subclass_c2_parametro_p2)  è uguale a  (False) )  e  ( (consdef)  è uguale a  (False) ) )  e  ( negazione di ((subclass_c2_variabile_v4)  è uguale a  (5)) ) )  e  
( negazione di (negazione di ((subclass_c2_controllo_c2)  è uguale a  (gialloaverdea))) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( (subclass_c2_parametro_p2)  è uguale a  (False) )  e  ( (consdef)  è uguale a  (False) ) )  e  ( negazione di ((subclass_c2_variabile_v4)  è uguale a  (5)) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (subclass_c2_parametro_p2)  è uguale a  (False) )  e  ( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p2)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v4)  è uguale a  (5))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v4)  è uguale a  (5)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_controllo_c2)  è uguale a  (gialloaverdea)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c2)  è uguale a  (gialloaverdea))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c2)  è uguale a  (gialloaverdea)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITStatement\n/*34,*/  se il parametro SubClass_C2_parametro_P1 è  diverso da  /*56,*/ 9 /*35,*/ o  se il controllo SubClass_C2_controllo_C2 non è  uguale a GialloaVerdea /*35,*/ e  se il controllo SubClass_C2_controllo_C5 non è  uguale a GialloaVerdea e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P1 è  minore di  /*55,*/ 8 /*38,*/ e  se il contatore SubClass_C2_contatore_Co6 è  uguale a  /*53,*/ 12, /*72,*/Azzera il contatore SubClass_C2_contatore_Co6""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se il parametro SubClass_C2_parametro_P1 è  diverso da  /*56,*/ 9 /*35,*/ o  se il controllo SubClass_C2_controllo_C2 non è  uguale a GialloaVerdea /*35,*/ e  se il controllo SubClass_C2_controllo_C5 non è  uguale a GialloaVerdea e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P1 è  minore di  /*55,*/ 8 /*38,*/ e  se il contatore SubClass_C2_contatore_Co6 è  uguale a  /*53,*/ 12""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p1)  è uguale a  (9))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p1)  è uguale a  (9)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( ( ( negazione di ((subclass_c2_controllo_c2)  è uguale a  (gialloaverdea)) )  e  ( negazione di ((subclass_c2_controllo_c5)  è uguale a  (gialloaverdea)) ) )  e  ( (consdef)  è uguale a  (False) ) )  e  ( (subclass_c2_parametro_p1)  è minore di  (8) ) )  e  
( (subclass_c2_contatore_co6)  è uguale a  (12) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( ( negazione di ((subclass_c2_controllo_c2)  è uguale a  (gialloaverdea)) )  e  ( negazione di ((subclass_c2_controllo_c5)  è uguale a  (gialloaverdea)) ) )  e  ( (consdef)  è uguale a  (False) ) )  e  ( (subclass_c2_parametro_p1)  è minore di  (8) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di ((subclass_c2_controllo_c2)  è uguale a  (gialloaverdea)) )  e  ( negazione di ((subclass_c2_controllo_c5)  è uguale a  (gialloaverdea)) ) )  e  ( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c2_controllo_c2)  è uguale a  (gialloaverdea)) )  e  ( negazione di ((subclass_c2_controllo_c5)  è uguale a  (gialloaverdea)) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c2)  è uguale a  (gialloaverdea))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c2)  è uguale a  (gialloaverdea)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c5)  è uguale a  (gialloaverdea))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c5)  è uguale a  (gialloaverdea)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_parametro_p1)  è minore di  (8)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co6)  è uguale a  (12)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#1
                ])

        populate_macroSubclass_c2_macroef_m2_SrfMacroDefInfo(di_ctx)
        #  se il controllo ConsDef  è  uguale a FALSE ,  /*44,*/  se  MainClass_C1_variabile_V1 del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  /*105,*/ è  uguale a  /*53,*/ 4, /*88,*/ quando  /*42,*/    MainClass_C1_controllo_C8 del campo  MainClass_C1     è  uguale a RossoGialloGiallo /*34,*/ o  se il parametro SubClass_C2_parametro_P2 è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C2_variabile_V4 non è  uguale a  /*53,*/ 5 /*35,*/ e  se il controllo SubClass_C2_controllo_C2 non è  diverso da GialloaVerdea, /*68,*/Attiva il timer SubClass_C2_timer_T4
        if db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_variabile_v1() == 4, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[1][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l10()) if db(it.get_mainclass_c1().get_mainclass_c1_controllo_c8() == GlobalEnumeration.rossogiallogiallo, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0][idx])), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db((db((db(self.get_subclass_c2_parametro_p2() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c2_variabile_v4() == 5, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_subclass_c2_controllo_c2() == GlobalEnumeration.gialloaverdea, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.get_subclass_c2_timer_t4().attiva()
        #  /*34,*/  se il parametro SubClass_C2_parametro_P1 è  diverso da  /*56,*/ 9 /*35,*/ o  se il controllo SubClass_C2_controllo_C2 non è  uguale a GialloaVerdea /*35,*/ e  se il controllo SubClass_C2_controllo_C5 non è  uguale a GialloaVerdea e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P1 è  minore di  /*55,*/ 8 /*38,*/ e  se il contatore SubClass_C2_contatore_Co6 è  uguale a  /*53,*/ 12, /*72,*/Azzera il contatore SubClass_C2_contatore_Co6
        if db((db(not db(self.get_subclass_c2_parametro_p1() == 9, di_ctx.subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0]) or db((db((db((db((db(not db(self.get_subclass_c2_controllo_c2() == GlobalEnumeration.gialloaverdea, di_ctx.subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_controllo_c5() == GlobalEnumeration.gialloaverdea, di_ctx.subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[1].subs[0].subs[0]) and db(self.get_subclass_c2_parametro_p1() < 8, di_ctx.subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_contatore_co6().get_valore() == 12, di_ctx.subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.get_subclass_c2_contatore_co6().resetta()
    
    def macroSubclass_c2_macroef_m3(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L8 è  diverso da  commento: {56,}  state1  commento: {38,} e  se il contatore SubClass_C2_contatore_Co2 è  diverso da  commento: {56,} 15041 e  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} o  se il parametro SubClass_C2_parametro_P6 è  uguale a  commento: {53,} 5 commento: {36,} o  se il timer SubClass_C2_timer_T10 non è attivo, commento: {69,}Disattiva il timer SubClass_C2_timer_T2
        
           
         commento: {34,}  se il parametro SubClass_C2_parametro_P6 non è  minore di  commento: {55,} 8 commento: {37,} e  se la variabile SubClass_C2_variabile_V5 non è  minore di  commento: {55,} 2 commento: {34,} e  se il parametro SubClass_C2_parametro_P2 è  diverso da  True , commento: {68,}Attiva il timer SubClass_C2_timer_T4
        
         ,altrimenti  commento: {69,}Disattiva il timer SubClass_C2_timer_T10
        
        
          se la macro  SubClass_C2_macrova_M6 ( con argomento_a10   uguale a GialloaVerdea ,argomento_a3   uguale a c120 ,argomento_a9   uguale a c120  e argomento_a6   uguale a GialloaVerdea )   è  diverso da  False  commento: {40,} ,  commento: {41,}  se MainClass_C1_parametro_P10 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  commento: {105,} è  uguale a  True , commento: {88,} quando  commento: {43,}   MainClass_C1_timer_T5 del campo  MainClass_C1     commento: {105,} è disattivo, commento: {72,}Azzera il contatore SubClass_C2_contatore_Co2
        
         ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V4 il valore 7
        
        
        
        }
        """
        def populate_macroSubclass_c2_macroef_m3_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L8 è  diverso da  /*56,*/  state1  /*38,*/ e  se il contatore SubClass_C2_contatore_Co2 è  diverso da  /*56,*/ 15041 e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro SubClass_C2_parametro_P6 è  uguale a  /*53,*/ 5 /*36,*/ o  se il timer SubClass_C2_timer_T10 non è attivo, /*69,*/Disattiva il timer SubClass_C2_timer_T2""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L8 è  diverso da  /*56,*/  state1  /*38,*/ e  se il contatore SubClass_C2_contatore_Co2 è  diverso da  /*56,*/ 15041 e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro SubClass_C2_parametro_P6 è  uguale a  /*53,*/ 5 /*36,*/ o  se il timer SubClass_C2_timer_T10 non è attivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( ( per ognuna delle seguenti {(negazione di ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l8')  è uguale a  (state1)))} )  e  ( negazione di ((subclass_c2_contatore_co2)  è uguale a  (15041)) ) )  e  
( (consdef)  è uguale a  (False) ) )  o  
( (subclass_c2_parametro_p6)  è uguale a  (5) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( per ognuna delle seguenti {(negazione di ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l8')  è uguale a  (state1)))} )  e  ( negazione di ((subclass_c2_contatore_co2)  è uguale a  (15041)) ) )  e  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( per ognuna delle seguenti {(negazione di ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l8')  è uguale a  (state1)))} )  e  ( negazione di ((subclass_c2_contatore_co2)  è uguale a  (15041)) )""", [
                            DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {(negazione di ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l8')  è uguale a  (state1)))}""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l8')  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'mainclass_c1 della lista subclass_c2_lista_l8')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co2)  è uguale a  (15041))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co2)  è uguale a  (15041)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p6)  è uguale a  (5)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c2_timer_t10' è attivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t10' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITEStatementImpl\n/*34,*/  se il parametro SubClass_C2_parametro_P6 non è  minore di  /*55,*/ 8 /*37,*/ e  se la variabile SubClass_C2_variabile_V5 non è  minore di  /*55,*/ 2 /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  True , /*68,*/Attiva il timer SubClass_C2_timer_T4

 ,altrimenti  /*69,*/Disattiva il timer SubClass_C2_timer_T10""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*34,*/  se il parametro SubClass_C2_parametro_P6 non è  minore di  /*55,*/ 8 /*37,*/ e  se la variabile SubClass_C2_variabile_V5 non è  minore di  /*55,*/ 2 /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c2_parametro_p6)  è minore di  (8)) )  e  ( negazione di ((subclass_c2_variabile_v5)  è minore di  (2)) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p6)  è minore di  (8))""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_parametro_p6)  è minore di  (8)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v5)  è minore di  (2))""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_variabile_v5)  è minore di  (2)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p2)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p2)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#1
                            DIStatement("""ITEStatementImpl\nse la macro  SubClass_C2_macrova_M6 ( con argomento_a10   uguale a GialloaVerdea ,argomento_a3   uguale a c120 ,argomento_a9   uguale a c120  e argomento_a6   uguale a GialloaVerdea )   è  diverso da  False  /*40,*/ ,  /*41,*/  se MainClass_C1_parametro_P10 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è  uguale a  True , /*88,*/ quando  /*43,*/   MainClass_C1_timer_T5 del campo  MainClass_C1     /*105,*/ è disattivo, /*72,*/Azzera il contatore SubClass_C2_contatore_Co2

 ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V4 il valore 7""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse la macro  SubClass_C2_macrova_M6 ( con argomento_a10   uguale a GialloaVerdea ,argomento_a3   uguale a c120 ,argomento_a9   uguale a c120  e argomento_a6   uguale a GialloaVerdea )   è  diverso da  False  /*40,*/ ,  /*41,*/  se MainClass_C1_parametro_P10 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è  uguale a  True , /*88,*/ quando  /*43,*/   MainClass_C1_timer_T5 del campo  MainClass_C1     /*105,*/ è disattivo""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((chiamata alla macro valorizzata 'macroSubclass_c2_macrova_m6')  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroSubclass_c2_macrova_m6')  è uguale a  (False)""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroSubclass_c2_macrova_m6'"""),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {se (il timer 'mainclass_c1_timer_t5 del campo mainclass_c1 della lista subclass_c2_lista_l8' è inattivo) allora ((mainclass_c1_parametro_p10 del campo mainclass_c1 della lista subclass_c2_lista_l8)  è uguale a  (True))}""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\nse (il timer 'mainclass_c1_timer_t5 del campo mainclass_c1 della lista subclass_c2_lista_l8' è inattivo) allora ((mainclass_c1_parametro_p10 del campo mainclass_c1 della lista subclass_c2_lista_l8)  è uguale a  (True))""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t5 del campo mainclass_c1 della lista subclass_c2_lista_l8' è inattivo""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p10 del campo mainclass_c1 della lista subclass_c2_lista_l8)  è uguale a  (True)""", [
                            ]),#1
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#2
                ])

        populate_macroSubclass_c2_macroef_m3_SrfMacroDefInfo(di_ctx)
        #  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L8 è  diverso da  /*56,*/  state1  /*38,*/ e  se il contatore SubClass_C2_contatore_Co2 è  diverso da  /*56,*/ 15041 e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro SubClass_C2_parametro_P6 è  uguale a  /*53,*/ 5 /*36,*/ o  se il timer SubClass_C2_timer_T10 non è attivo, /*69,*/Disattiva il timer SubClass_C2_timer_T2
        if db((db((db((db((db(all(db(not db(it.get_mainclass_c1().get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l8())), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_contatore_co2().get_valore() == 15041, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_parametro_p6() == 5, di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_timer_t10().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.get_subclass_c2_timer_t2().disattiva()
        #  /*34,*/  se il parametro SubClass_C2_parametro_P6 non è  minore di  /*55,*/ 8 /*37,*/ e  se la variabile SubClass_C2_variabile_V5 non è  minore di  /*55,*/ 2 /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  True , /*68,*/Attiva il timer SubClass_C2_timer_T4
        #   ,altrimenti  /*69,*/Disattiva il timer SubClass_C2_timer_T10
        if db((db((db(not db(self.get_subclass_c2_parametro_p6() < 8, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_variabile_v5() < 2, di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c2_parametro_p2() == True, di_ctx.subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.get_subclass_c2_timer_t4().attiva()
        else:
            self.get_subclass_c2_timer_t10().disattiva()
        #  se la macro  SubClass_C2_macrova_M6 ( con argomento_a10   uguale a GialloaVerdea ,argomento_a3   uguale a c120 ,argomento_a9   uguale a c120  e argomento_a6   uguale a GialloaVerdea )   è  diverso da  False  /*40,*/ ,  /*41,*/  se MainClass_C1_parametro_P10 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è  uguale a  True , /*88,*/ quando  /*43,*/   MainClass_C1_timer_T5 del campo  MainClass_C1     /*105,*/ è disattivo, /*72,*/Azzera il contatore SubClass_C2_contatore_Co2
        #   ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V4 il valore 7
        if db((db(not db(db(self.macroSubclass_c2_macrova_m6(GlobalEnumeration.gialloaverdea,GlobalEnumeration.c120,GlobalEnumeration.gialloaverdea,GlobalEnumeration.c120, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0]) == False, di_ctx.subs[2].subs[0].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[0]) and db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_parametro_p10() == True, di_ctx.subs[2].subs[0].subs[1].subs[0].subs[1][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l8()) if db(it.get_mainclass_c1().get_mainclass_c1_timer_t5().isDisattivato(), di_ctx.subs[2].subs[0].subs[1].subs[0].subs[0][idx])), di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.get_subclass_c2_contatore_co2().resetta()
        else:
            self.set_subclass_c2_variabile_v4(7)
    
    def macroSubclass_c2_macroef_m5(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L5 esiste e  commento: {105,} è  diverso da  commento: {56,}  state1  e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} e  se la variabile SubClass_C2_variabile_V1 è  diverso da  True , commento: {66,} Assegna al comando SubClass_C2_comando_C9 il valore  False 
        
         ,altrimenti   commento: {67,} Assegna alla variabile SubClass_C2_variabile_V8 il valore 7 commento: {67,}
        
        
         commento: {43,}  se MainClass_C1_timer_T9 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  commento: {105,} è attivo commento: {38,} e  se il contatore SubClass_C2_contatore_Co7 è  diverso da  commento: {56,} 142,  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V4 il valore 3 commento: {67,}
        
         ,altrimenti  commento: {70,}Incrementa il contatore SubClass_C2_contatore_Co7
        
        
         commento: {36,}  se il timer SubClass_C2_timer_T4 non è disattivo commento: {36,} o  se il timer SubClass_C2_timer_T4 è disattivo commento: {35,} o  se il controllo SubClass_C2_controllo_C6 è  diverso da  True  commento: {35,} e  se il controllo SubClass_C2_controllo_C6 non è  diverso da  True  o  se il controllo ConsDef  è  uguale a FALSE , commento: {66,} Assegna al comando SubClass_C2_comando_C7 il valore  False 
        
         ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V5 il valore 3
        
        
         commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L10 è  diverso da  commento: {56,}  state1  e  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} o  se il contatore SubClass_C2_contatore_Co7 è  diverso da  commento: {56,} 1553 commento: {36,} e  se il timer SubClass_C2_timer_T10 è disattivo commento: {35,} o  se il controllo SubClass_C2_controllo_C2 è  diverso da GialloaVerdea, commento: {66,} Assegna al comando SubClass_C2_comando_C7 il valore  True 
        
         ,altrimenti  commento: {66,} Assegna al comando SubClass_C2_comando_C9 il valore  True 
        
        
        
        }
        """
        def populate_macroSubclass_c2_macroef_m5_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITEStatementImpl\n/*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L5 esiste e  /*105,*/ è  diverso da  /*56,*/  state1  e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C2_variabile_V1 è  diverso da  True , /*66,*/ Assegna al comando SubClass_C2_comando_C9 il valore  False 

 ,altrimenti   /*67,*/ Assegna alla variabile SubClass_C2_variabile_V8 il valore 7""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L5 esiste e  /*105,*/ è  diverso da  /*56,*/  state1  e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C2_variabile_V1 è  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( per ognuna delle seguenti con lista non vuota {(negazione di ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l5')  è uguale a  (state1)))} )  e  ( (consdef)  è uguale a  (False) ) )  e  ( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( per ognuna delle seguenti con lista non vuota {(negazione di ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l5')  è uguale a  (state1)))} )  e  ( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {(negazione di ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l5')  è uguale a  (state1)))}""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l5')  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'mainclass_c1 della lista subclass_c2_lista_l5')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v1)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v1)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITEStatementImpl\n/*67,*/


 /*43,*/  se MainClass_C1_timer_T9 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è attivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  diverso da  /*56,*/ 142,  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V4 il valore 3 /*67,*/

 ,altrimenti  /*70,*/Incrementa il contatore SubClass_C2_contatore_Co7""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*67,*/


 /*43,*/  se MainClass_C1_timer_T9 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è attivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  diverso da  /*56,*/ 142""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {(il timer 'mainclass_c1_timer_t9 del campo mainclass_c1 della lista subclass_c2_lista_l3' è attivo)}""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t9 del campo mainclass_c1 della lista subclass_c2_lista_l3' è attivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co7)  è uguale a  (142))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co7)  è uguale a  (142)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#1
                            DIStatement("""ITEStatementImpl\n/*36,*/  se il timer SubClass_C2_timer_T4 non è disattivo /*36,*/ o  se il timer SubClass_C2_timer_T4 è disattivo /*35,*/ o  se il controllo SubClass_C2_controllo_C6 è  diverso da  True  /*35,*/ e  se il controllo SubClass_C2_controllo_C6 non è  diverso da  True  o  se il controllo ConsDef  è  uguale a FALSE , /*66,*/ Assegna al comando SubClass_C2_comando_C7 il valore  False 

 ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V5 il valore 3""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*36,*/  se il timer SubClass_C2_timer_T4 non è disattivo /*36,*/ o  se il timer SubClass_C2_timer_T4 è disattivo /*35,*/ o  se il controllo SubClass_C2_controllo_C6 è  diverso da  True  /*35,*/ e  se il controllo SubClass_C2_controllo_C6 non è  diverso da  True  o  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( negazione di (il timer 'subclass_c2_timer_t4' è inattivo) )  o  
( il timer 'subclass_c2_timer_t4' è inattivo ) )  o  
( ( negazione di ((subclass_c2_controllo_c6)  è uguale a  (True)) )  e  
( negazione di (negazione di ((subclass_c2_controllo_c6)  è uguale a  (True))) ) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( negazione di (il timer 'subclass_c2_timer_t4' è inattivo) )  o  
( il timer 'subclass_c2_timer_t4' è inattivo )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c2_timer_t4' è inattivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t4' è inattivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t4' è inattivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c2_controllo_c6)  è uguale a  (True)) )  e  
( negazione di (negazione di ((subclass_c2_controllo_c6)  è uguale a  (True))) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c6)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c6)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_controllo_c6)  è uguale a  (True)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c6)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c6)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            ]),#2
                            DIStatement("""ITEStatementImpl\n/*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L10 è  diverso da  /*56,*/  state1  e  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 è  diverso da  /*56,*/ 1553 /*36,*/ e  se il timer SubClass_C2_timer_T10 è disattivo /*35,*/ o  se il controllo SubClass_C2_controllo_C2 è  diverso da GialloaVerdea, /*66,*/ Assegna al comando SubClass_C2_comando_C7 il valore  True 

 ,altrimenti  /*66,*/ Assegna al comando SubClass_C2_comando_C9 il valore  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L10 è  diverso da  /*56,*/  state1  e  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 è  diverso da  /*56,*/ 1553 /*36,*/ e  se il timer SubClass_C2_timer_T10 è disattivo /*35,*/ o  se il controllo SubClass_C2_controllo_C2 è  diverso da GialloaVerdea""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( per ognuna delle seguenti {(negazione di ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l10')  è uguale a  (state1)))} )  e  
( (consdef)  è uguale a  (False) ) )  o  
( ( negazione di ((subclass_c2_contatore_co7)  è uguale a  (1553)) )  e  
( il timer 'subclass_c2_timer_t10' è inattivo ) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( per ognuna delle seguenti {(negazione di ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l10')  è uguale a  (state1)))} )  e  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {(negazione di ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l10')  è uguale a  (state1)))}""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l10')  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'mainclass_c1 della lista subclass_c2_lista_l10')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c2_contatore_co7)  è uguale a  (1553)) )  e  
( il timer 'subclass_c2_timer_t10' è inattivo )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co7)  è uguale a  (1553))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co7)  è uguale a  (1553)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t10' è inattivo""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c2)  è uguale a  (gialloaverdea))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c2)  è uguale a  (gialloaverdea)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#3
                ])

        populate_macroSubclass_c2_macroef_m5_SrfMacroDefInfo(di_ctx)
        #  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L5 esiste e  /*105,*/ è  diverso da  /*56,*/  state1  e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C2_variabile_V1 è  diverso da  True , /*66,*/ Assegna al comando SubClass_C2_comando_C9 il valore  False 
        #   ,altrimenti   /*67,*/ Assegna alla variabile SubClass_C2_variabile_V8 il valore 7
        if db((db((db((db(all_notempty(db(not db(it.get_mainclass_c1().get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l5())), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_variabile_v1() == True, di_ctx.subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.set_subclass_c2_comando_c9(False)
        else:
            self.set_subclass_c2_variabile_v8(7)
        #  /*67,*/
        #   /*43,*/  se MainClass_C1_timer_T9 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è attivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  diverso da  /*56,*/ 142,  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V4 il valore 3 /*67,*/
        #   ,altrimenti  /*70,*/Incrementa il contatore SubClass_C2_contatore_Co7
        if db((db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_timer_t9().isAttivato(), di_ctx.subs[1].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l3())), di_ctx.subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c2_contatore_co7().get_valore() == 142, di_ctx.subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.set_subclass_c2_variabile_v4(3)
        else:
            self.get_subclass_c2_contatore_co7().incrementa()
        #  /*36,*/  se il timer SubClass_C2_timer_T4 non è disattivo /*36,*/ o  se il timer SubClass_C2_timer_T4 è disattivo /*35,*/ o  se il controllo SubClass_C2_controllo_C6 è  diverso da  True  /*35,*/ e  se il controllo SubClass_C2_controllo_C6 non è  diverso da  True  o  se il controllo ConsDef  è  uguale a FALSE , /*66,*/ Assegna al comando SubClass_C2_comando_C7 il valore  False 
        #   ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V5 il valore 3
        if db((db((db((db(not db(self.get_subclass_c2_timer_t4().isDisattivato(), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_timer_t4().isDisattivato(), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_controllo_c6() == True, di_ctx.subs[2].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_subclass_c2_controllo_c6() == True, di_ctx.subs[2].subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[2].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.set_subclass_c2_comando_c7(False)
        else:
            self.set_subclass_c2_variabile_v5(3)
        #  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L10 è  diverso da  /*56,*/  state1  e  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 è  diverso da  /*56,*/ 1553 /*36,*/ e  se il timer SubClass_C2_timer_T10 è disattivo /*35,*/ o  se il controllo SubClass_C2_controllo_C2 è  diverso da GialloaVerdea, /*66,*/ Assegna al comando SubClass_C2_comando_C7 il valore  True 
        #   ,altrimenti  /*66,*/ Assegna al comando SubClass_C2_comando_C9 il valore  True
        if db((db((db((db(all(db(not db(it.get_mainclass_c1().get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[3].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]), di_ctx.subs[3].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l10())), di_ctx.subs[3].subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[3].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[3].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_contatore_co7().get_valore() == 1553, di_ctx.subs[3].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[3].subs[0].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_timer_t10().isDisattivato(), di_ctx.subs[3].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[3].subs[0].subs[0].subs[1])), di_ctx.subs[3].subs[0].subs[0]) or db(not db(self.get_subclass_c2_controllo_c2() == GlobalEnumeration.gialloaverdea, di_ctx.subs[3].subs[0].subs[1].subs[0]), di_ctx.subs[3].subs[0].subs[1])), di_ctx.subs[3].subs[0]):
            self.set_subclass_c2_comando_c7(True)
        else:
            self.set_subclass_c2_comando_c9(True)
    
    def macroSubclass_c2_macroef_m6(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {34,}  se il parametro SubClass_C2_parametro_P6 è  uguale a  commento: {53,} 3,  commento: {42,}  se  MainClass_C1_controllo_C8 del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  commento: {105,} è  diverso da RossoGialloGiallo, commento: {88,} quando  commento: {44,}    MainClass_C1_variabile_V5 del campo  MainClass_C1     è  uguale a  False  commento: {34,} e  se il parametro SubClass_C2_parametro_P4 non è  uguale a Verde commento: {37,} e  se la variabile SubClass_C2_variabile_V5 è  uguale a  commento: {53,} 7 commento: {36,} e  se il timer SubClass_C2_timer_T2 è disattivo commento: {37,} o  se la variabile SubClass_C2_variabile_V5 è  uguale a  commento: {53,} 9, commento: {69,}Disattiva il timer SubClass_C2_timer_T10
        
         ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V4 il valore 1
        
        
        
        }
        """
        def populate_macroSubclass_c2_macroef_m6_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITEStatementImpl\n/*34,*/  se il parametro SubClass_C2_parametro_P6 è  uguale a  /*53,*/ 3,  /*42,*/  se  MainClass_C1_controllo_C8 del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  /*105,*/ è  diverso da RossoGialloGiallo, /*88,*/ quando  /*44,*/    MainClass_C1_variabile_V5 del campo  MainClass_C1     è  uguale a  False  /*34,*/ e  se il parametro SubClass_C2_parametro_P4 non è  uguale a Verde /*37,*/ e  se la variabile SubClass_C2_variabile_V5 è  uguale a  /*53,*/ 7 /*36,*/ e  se il timer SubClass_C2_timer_T2 è disattivo /*37,*/ o  se la variabile SubClass_C2_variabile_V5 è  uguale a  /*53,*/ 9, /*69,*/Disattiva il timer SubClass_C2_timer_T10

 ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V4 il valore 1""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se il parametro SubClass_C2_parametro_P6 è  uguale a  /*53,*/ 3,  /*42,*/  se  MainClass_C1_controllo_C8 del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  /*105,*/ è  diverso da RossoGialloGiallo, /*88,*/ quando  /*44,*/    MainClass_C1_variabile_V5 del campo  MainClass_C1     è  uguale a  False  /*34,*/ e  se il parametro SubClass_C2_parametro_P4 non è  uguale a Verde /*37,*/ e  se la variabile SubClass_C2_variabile_V5 è  uguale a  /*53,*/ 7 /*36,*/ e  se il timer SubClass_C2_timer_T2 è disattivo /*37,*/ o  se la variabile SubClass_C2_variabile_V5 è  uguale a  /*53,*/ 9""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( ( ( (subclass_c2_parametro_p6)  è uguale a  (3) )  e  ( per ognuna delle seguenti con lista non vuota {se ((mainclass_c1_variabile_v5 del campo mainclass_c1 della lista subclass_c2_lista_l10)  è uguale a  (False)) allora (negazione di ((mainclass_c1_controllo_c8 del campo mainclass_c1 della lista subclass_c2_lista_l10)  è uguale a  (rossogiallogiallo)))} ) )  e  ( negazione di ((subclass_c2_parametro_p4)  è uguale a  (verde)) ) )  e  ( (subclass_c2_variabile_v5)  è uguale a  (7) ) )  e  
( il timer 'subclass_c2_timer_t2' è inattivo )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( ( (subclass_c2_parametro_p6)  è uguale a  (3) )  e  ( per ognuna delle seguenti con lista non vuota {se ((mainclass_c1_variabile_v5 del campo mainclass_c1 della lista subclass_c2_lista_l10)  è uguale a  (False)) allora (negazione di ((mainclass_c1_controllo_c8 del campo mainclass_c1 della lista subclass_c2_lista_l10)  è uguale a  (rossogiallogiallo)))} ) )  e  ( negazione di ((subclass_c2_parametro_p4)  è uguale a  (verde)) ) )  e  ( (subclass_c2_variabile_v5)  è uguale a  (7) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( (subclass_c2_parametro_p6)  è uguale a  (3) )  e  ( per ognuna delle seguenti con lista non vuota {se ((mainclass_c1_variabile_v5 del campo mainclass_c1 della lista subclass_c2_lista_l10)  è uguale a  (False)) allora (negazione di ((mainclass_c1_controllo_c8 del campo mainclass_c1 della lista subclass_c2_lista_l10)  è uguale a  (rossogiallogiallo)))} ) )  e  ( negazione di ((subclass_c2_parametro_p4)  è uguale a  (verde)) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (subclass_c2_parametro_p6)  è uguale a  (3) )  e  ( per ognuna delle seguenti con lista non vuota {se ((mainclass_c1_variabile_v5 del campo mainclass_c1 della lista subclass_c2_lista_l10)  è uguale a  (False)) allora (negazione di ((mainclass_c1_controllo_c8 del campo mainclass_c1 della lista subclass_c2_lista_l10)  è uguale a  (rossogiallogiallo)))} )""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p6)  è uguale a  (3)""", [
                            ]),#0
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {se ((mainclass_c1_variabile_v5 del campo mainclass_c1 della lista subclass_c2_lista_l10)  è uguale a  (False)) allora (negazione di ((mainclass_c1_controllo_c8 del campo mainclass_c1 della lista subclass_c2_lista_l10)  è uguale a  (rossogiallogiallo)))}""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\nse ((mainclass_c1_variabile_v5 del campo mainclass_c1 della lista subclass_c2_lista_l10)  è uguale a  (False)) allora (negazione di ((mainclass_c1_controllo_c8 del campo mainclass_c1 della lista subclass_c2_lista_l10)  è uguale a  (rossogiallogiallo)))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v5 del campo mainclass_c1 della lista subclass_c2_lista_l10)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c8 del campo mainclass_c1 della lista subclass_c2_lista_l10)  è uguale a  (rossogiallogiallo))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c8 del campo mainclass_c1 della lista subclass_c2_lista_l10)  è uguale a  (rossogiallogiallo)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p4)  è uguale a  (verde))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p4)  è uguale a  (verde)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v5)  è uguale a  (7)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t2' è inattivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v5)  è uguale a  (9)""", [
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroSubclass_c2_macroef_m6_SrfMacroDefInfo(di_ctx)
        #  /*34,*/  se il parametro SubClass_C2_parametro_P6 è  uguale a  /*53,*/ 3,  /*42,*/  se  MainClass_C1_controllo_C8 del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  /*105,*/ è  diverso da RossoGialloGiallo, /*88,*/ quando  /*44,*/    MainClass_C1_variabile_V5 del campo  MainClass_C1     è  uguale a  False  /*34,*/ e  se il parametro SubClass_C2_parametro_P4 non è  uguale a Verde /*37,*/ e  se la variabile SubClass_C2_variabile_V5 è  uguale a  /*53,*/ 7 /*36,*/ e  se il timer SubClass_C2_timer_T2 è disattivo /*37,*/ o  se la variabile SubClass_C2_variabile_V5 è  uguale a  /*53,*/ 9, /*69,*/Disattiva il timer SubClass_C2_timer_T10
        #   ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V4 il valore 1
        if db((db((db((db((db((db(self.get_subclass_c2_parametro_p6() == 3, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(all_notempty(db(not db(it.get_mainclass_c1().get_mainclass_c1_controllo_c8() == GlobalEnumeration.rossogiallogiallo, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0][idx]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l10()) if db(it.get_mainclass_c1().get_mainclass_c1_variabile_v5() == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0][idx])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_parametro_p4() == GlobalEnumeration.verde, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_variabile_v5() == 7, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_timer_t2().isDisattivato(), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_variabile_v5() == 9, di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.get_subclass_c2_timer_t10().disattiva()
        else:
            self.set_subclass_c2_variabile_v4(1)
    
    # verify macros
    @srf_value_macro("macroSubclass_c2_macrove_m3")
    def macroSubclass_c2_macrove_m3(self, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
         
        { commento: {63,} commento: {43,}  se MainClass_C1_timer_T9 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  commento: {105,} è disattivo commento: {34,} o  se il parametro SubClass_C2_parametro_P4 non è  uguale a Verde, Solo una delle seguenti { 
         commento: {62,} commento: {34,}  se il parametro SubClass_C2_parametro_P4 è  diverso da Verde commento: {36,} o  se il timer SubClass_C2_timer_T2 non è scaduto commento: {38,} o  se il contatore SubClass_C2_contatore_Co2 non è  diverso da  commento: {56,} 13530 commento: {38,} o  se il contatore SubClass_C2_contatore_Co7 non è  uguale a  commento: {53,} 15412 commento: {35,} o  se il controllo SubClass_C2_controllo_C5 è  diverso da GialloaVerdea commento: {36,} e  se il timer SubClass_C2_timer_T4 è scaduto, Almeno una delle seguenti { 
         commento: {63,} commento: {110,}  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è disattivo commento: {36,} e  se il timer SubClass_C2_timer_T2 non è disattivo commento: {38,} o  se il contatore SubClass_C2_contatore_Co6 non è  uguale a  commento: {53,} 1453 commento: {37,} e  se la variabile SubClass_C2_variabile_V5 è  maggiore di  commento: {54,} 9, Solo una delle seguenti { 
         commento: {43,}  se MainClass_C1_timer_T9 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  commento: {105,} è disattivo commento: {36,} e  se il timer SubClass_C2_timer_T4 è disattivo e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   commento: {47,51,}  commento: {34,}  il parametro SubClass_C2_parametro_P4 sia  diverso da Verde
         commento: {104,} e  che  commento: {,}  il contatore SubClass_C2_contatore_Co7 sia  uguale a  commento: {53,} 152
        
        
         } Verifica che   commento: {47,48,50,51,}  commento: {,}  la variabile SubClass_C2_variabile_V4 non sia  diverso da  commento: {56,} 1
         commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} o  che  commento: {34,}  il parametro SubClass_C2_parametro_P6 sia  uguale a  commento: {53,} 2
         commento: {104,} o  che  commento: {,}  il controllo SubClass_C2_controllo_C2 sia  diverso da GialloaVerdea
         commento: {104,} e  che  commento: {,}  il contatore SubClass_C2_contatore_Co2 non sia  maggiore di  commento: {54,} 1153
        
        
         } Verifica che   commento: {51,}  commento: {,}  il contatore SubClass_C2_contatore_Co2 sia  diverso da  commento: {56,} 130
        
        
         } Verifica che   commento: {48,51,}  commento: {,}  il contatore SubClass_C2_contatore_Co7 sia  minore di  commento: {55,} 15
         commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
        
        
        }
        """
        def populate_macroSubclass_c2_macrove_m3_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*43,*/  se MainClass_C1_timer_T9 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è disattivo /*34,*/ o  se il parametro SubClass_C2_parametro_P4 non è  uguale a Verde, Solo una delle seguenti { 
 /*62,*/ /*34,*/  se il parametro SubClass_C2_parametro_P4 è  diverso da Verde /*36,*/ o  se il timer SubClass_C2_timer_T2 non è scaduto /*38,*/ o  se il contatore SubClass_C2_contatore_Co2 non è  diverso da  /*56,*/ 13530 /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 non è  uguale a  /*53,*/ 15412 /*35,*/ o  se il controllo SubClass_C2_controllo_C5 è  diverso da GialloaVerdea /*36,*/ e  se il timer SubClass_C2_timer_T4 è scaduto, Almeno una delle seguenti { 
 /*63,*/ /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T2 non è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co6 non è  uguale a  /*53,*/ 1453 /*37,*/ e  se la variabile SubClass_C2_variabile_V5 è  maggiore di  /*54,*/ 9, Solo una delle seguenti { 
 /*43,*/  se MainClass_C1_timer_T9 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T4 è disattivo e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*47,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P4 sia  diverso da Verde
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 152


 } Verifica che   /*47,48,50,51,*/  /*,*/  la variabile SubClass_C2_variabile_V4 non sia  diverso da  /*56,*/ 1
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  uguale a  /*53,*/ 2
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C2 sia  diverso da GialloaVerdea
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co2 non sia  maggiore di  /*54,*/ 1153


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co2 sia  diverso da  /*56,*/ 130


 } Verifica che   /*48,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  minore di  /*55,*/ 15
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*43,*/  se MainClass_C1_timer_T9 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è disattivo /*34,*/ o  se il parametro SubClass_C2_parametro_P4 non è  uguale a Verde, Solo una delle seguenti { 
 /*62,*/ /*34,*/  se il parametro SubClass_C2_parametro_P4 è  diverso da Verde /*36,*/ o  se il timer SubClass_C2_timer_T2 non è scaduto /*38,*/ o  se il contatore SubClass_C2_contatore_Co2 non è  diverso da  /*56,*/ 13530 /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 non è  uguale a  /*53,*/ 15412 /*35,*/ o  se il controllo SubClass_C2_controllo_C5 è  diverso da GialloaVerdea /*36,*/ e  se il timer SubClass_C2_timer_T4 è scaduto, Almeno una delle seguenti { 
 /*63,*/ /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T2 non è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co6 non è  uguale a  /*53,*/ 1453 /*37,*/ e  se la variabile SubClass_C2_variabile_V5 è  maggiore di  /*54,*/ 9, Solo una delle seguenti { 
 /*43,*/  se MainClass_C1_timer_T9 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T4 è disattivo e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*47,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P4 sia  diverso da Verde
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 152


 } Verifica che   /*47,48,50,51,*/  /*,*/  la variabile SubClass_C2_variabile_V4 non sia  diverso da  /*56,*/ 1
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  uguale a  /*53,*/ 2
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C2 sia  diverso da GialloaVerdea
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co2 non sia  maggiore di  /*54,*/ 1153


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co2 sia  diverso da  /*56,*/ 130


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*43,*/  se MainClass_C1_timer_T9 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è disattivo /*34,*/ o  se il parametro SubClass_C2_parametro_P4 non è  uguale a Verde""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nMainClass_C1_timer_T9 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t9 del campo mainclass_c1 della lista subclass_c2_lista_l3' è inattivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P4 non è  uguale a Verde""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p4)  è uguale a  (verde)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*62,*/ /*34,*/  se il parametro SubClass_C2_parametro_P4 è  diverso da Verde /*36,*/ o  se il timer SubClass_C2_timer_T2 non è scaduto /*38,*/ o  se il contatore SubClass_C2_contatore_Co2 non è  diverso da  /*56,*/ 13530 /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 non è  uguale a  /*53,*/ 15412 /*35,*/ o  se il controllo SubClass_C2_controllo_C5 è  diverso da GialloaVerdea /*36,*/ e  se il timer SubClass_C2_timer_T4 è scaduto, Almeno una delle seguenti { 
 /*63,*/ /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T2 non è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co6 non è  uguale a  /*53,*/ 1453 /*37,*/ e  se la variabile SubClass_C2_variabile_V5 è  maggiore di  /*54,*/ 9, Solo una delle seguenti { 
 /*43,*/  se MainClass_C1_timer_T9 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T4 è disattivo e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*47,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P4 sia  diverso da Verde
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 152


 } Verifica che   /*47,48,50,51,*/  /*,*/  la variabile SubClass_C2_variabile_V4 non sia  diverso da  /*56,*/ 1
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  uguale a  /*53,*/ 2
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C2 sia  diverso da GialloaVerdea
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co2 non sia  maggiore di  /*54,*/ 1153


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co2 sia  diverso da  /*56,*/ 130


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*34,*/  se il parametro SubClass_C2_parametro_P4 è  diverso da Verde /*36,*/ o  se il timer SubClass_C2_timer_T2 non è scaduto /*38,*/ o  se il contatore SubClass_C2_contatore_Co2 non è  diverso da  /*56,*/ 13530 /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 non è  uguale a  /*53,*/ 15412 /*35,*/ o  se il controllo SubClass_C2_controllo_C5 è  diverso da GialloaVerdea /*36,*/ e  se il timer SubClass_C2_timer_T4 è scaduto, Almeno una delle seguenti { 
 /*63,*/ /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T2 non è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co6 non è  uguale a  /*53,*/ 1453 /*37,*/ e  se la variabile SubClass_C2_variabile_V5 è  maggiore di  /*54,*/ 9, Solo una delle seguenti { 
 /*43,*/  se MainClass_C1_timer_T9 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T4 è disattivo e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*47,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P4 sia  diverso da Verde
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 152


 } Verifica che   /*47,48,50,51,*/  /*,*/  la variabile SubClass_C2_variabile_V4 non sia  diverso da  /*56,*/ 1
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  uguale a  /*53,*/ 2
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C2 sia  diverso da GialloaVerdea
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co2 non sia  maggiore di  /*54,*/ 1153


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*34,*/  se il parametro SubClass_C2_parametro_P4 è  diverso da Verde /*36,*/ o  se il timer SubClass_C2_timer_T2 non è scaduto /*38,*/ o  se il contatore SubClass_C2_contatore_Co2 non è  diverso da  /*56,*/ 13530 /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 non è  uguale a  /*53,*/ 15412 /*35,*/ o  se il controllo SubClass_C2_controllo_C5 è  diverso da GialloaVerdea /*36,*/ e  se il timer SubClass_C2_timer_T4 è scaduto""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*34,*/  se il parametro SubClass_C2_parametro_P4 è  diverso da Verde /*36,*/ o  se il timer SubClass_C2_timer_T2 non è scaduto /*38,*/ o  se il contatore SubClass_C2_contatore_Co2 non è  diverso da  /*56,*/ 13530 /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 non è  uguale a  /*53,*/ 15412""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*34,*/  se il parametro SubClass_C2_parametro_P4 è  diverso da Verde /*36,*/ o  se il timer SubClass_C2_timer_T2 non è scaduto /*38,*/ o  se il contatore SubClass_C2_contatore_Co2 non è  diverso da  /*56,*/ 13530""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*34,*/  se il parametro SubClass_C2_parametro_P4 è  diverso da Verde /*36,*/ o  se il timer SubClass_C2_timer_T2 non è scaduto""", [
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P4 è  diverso da Verde""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p4)  è uguale a  (verde)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C2_timer_T2 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t2' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co2 non è  diverso da  /*56,*/ 13530""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co2)  è uguale a  (13530))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co2)  è uguale a  (13530)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co7 non è  uguale a  /*53,*/ 15412""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co7)  è uguale a  (15412)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo SubClass_C2_controllo_C5 è  diverso da GialloaVerdea /*36,*/ e  se il timer SubClass_C2_timer_T4 è scaduto""", [
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C5 è  diverso da GialloaVerdea""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c5)  è uguale a  (gialloaverdea)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T4 è scaduto""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*63,*/ /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T2 non è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co6 non è  uguale a  /*53,*/ 1453 /*37,*/ e  se la variabile SubClass_C2_variabile_V5 è  maggiore di  /*54,*/ 9, Solo una delle seguenti { 
 /*43,*/  se MainClass_C1_timer_T9 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T4 è disattivo e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*47,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P4 sia  diverso da Verde
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 152


 } Verifica che   /*47,48,50,51,*/  /*,*/  la variabile SubClass_C2_variabile_V4 non sia  diverso da  /*56,*/ 1
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  uguale a  /*53,*/ 2
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C2 sia  diverso da GialloaVerdea
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co2 non sia  maggiore di  /*54,*/ 1153


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T2 non è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co6 non è  uguale a  /*53,*/ 1453 /*37,*/ e  se la variabile SubClass_C2_variabile_V5 è  maggiore di  /*54,*/ 9, Solo una delle seguenti { 
 /*43,*/  se MainClass_C1_timer_T9 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T4 è disattivo e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*47,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P4 sia  diverso da Verde
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 152


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T2 non è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co6 non è  uguale a  /*53,*/ 1453 /*37,*/ e  se la variabile SubClass_C2_variabile_V5 è  maggiore di  /*54,*/ 9""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T2 non è disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil ripristino del timer  SubClass_C2_restoreTI_TI1 è disattivo""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C2_timer_T2 non è disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t2' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il contatore SubClass_C2_contatore_Co6 non è  uguale a  /*53,*/ 1453 /*37,*/ e  se la variabile SubClass_C2_variabile_V5 è  maggiore di  /*54,*/ 9""", [
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co6 non è  uguale a  /*53,*/ 1453""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co6)  è uguale a  (1453)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nla variabile SubClass_C2_variabile_V5 è  maggiore di  /*54,*/ 9""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*43,*/  se MainClass_C1_timer_T9 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T4 è disattivo e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*47,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P4 sia  diverso da Verde
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 152""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*43,*/  se MainClass_C1_timer_T9 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T4 è disattivo e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*43,*/  se MainClass_C1_timer_T9 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T4 è disattivo""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nMainClass_C1_timer_T9 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t9 del campo mainclass_c1 della lista subclass_c2_lista_l8' è inattivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T4 è disattivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P4 sia  diverso da Verde
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 152""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P4 sia  diverso da Verde""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p4)  è uguale a  (verde)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 152""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,51,*/  /*,*/  la variabile SubClass_C2_variabile_V4 non sia  diverso da  /*56,*/ 1
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  uguale a  /*53,*/ 2
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C2 sia  diverso da GialloaVerdea
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co2 non sia  maggiore di  /*54,*/ 1153""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,51,*/  /*,*/  la variabile SubClass_C2_variabile_V4 non sia  diverso da  /*56,*/ 1
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  uguale a  /*53,*/ 2""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,50,51,*/  /*,*/  la variabile SubClass_C2_variabile_V4 non sia  diverso da  /*56,*/ 1
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,50,51,*/  /*,*/  la variabile SubClass_C2_variabile_V4 non sia  diverso da  /*56,*/ 1""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v4)  è uguale a  (1))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v4)  è uguale a  (1)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  uguale a  /*53,*/ 2""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il controllo SubClass_C2_controllo_C2 sia  diverso da GialloaVerdea
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co2 non sia  maggiore di  /*54,*/ 1153""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo SubClass_C2_controllo_C2 sia  diverso da GialloaVerdea""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c2)  è uguale a  (gialloaverdea)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore SubClass_C2_contatore_Co2 non sia  maggiore di  /*54,*/ 1153""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_contatore_co2)  è maggiore di  (1153)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co2 sia  diverso da  /*56,*/ 130""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co2)  è uguale a  (130)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  minore di  /*55,*/ 15
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""LessThanImpl\nche   /*48,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  minore di  /*55,*/ 15""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroSubclass_c2_macrove_m3_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_timer_t9().isDisattivato(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l3())), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_parametro_p4() == GlobalEnumeration.verde, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((((db(not db((db((db((db((db(not db(self.get_subclass_c2_parametro_p4() == GlobalEnumeration.verde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_timer_t2().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_subclass_c2_contatore_co2().get_valore() == 13530, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_contatore_co7().get_valore() == 15412, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_controllo_c5() == GlobalEnumeration.gialloaverdea, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_timer_t4().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db(self.get_subclass_c2_restoreti_ti1_restore().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_timer_t2().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_contatore_co6().get_valore() == 1453, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_variabile_v5() > 9, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db((db((db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_timer_t9().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l8())), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_timer_t4().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db(not db(self.get_subclass_c2_parametro_p4() == GlobalEnumeration.verde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) and db(self.get_subclass_c2_contatore_co7().get_valore() == 152, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db((db(not db(not db(self.get_subclass_c2_variabile_v4() == 1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(self.get_subclass_c2_parametro_p6() == 2, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db((db(not db(self.get_subclass_c2_controllo_c2() == GlobalEnumeration.gialloaverdea, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(not db(self.get_subclass_c2_contatore_co2().get_valore() > 1153, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0])) + (db(not db(self.get_subclass_c2_contatore_co2().get_valore() == 130, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db(self.get_subclass_c2_contatore_co7().get_valore() < 15, di_ctx.subs[0].subs[1].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    @srf_value_macro("macroSubclass_c2_macrove_m4")
    def macroSubclass_c2_macrove_m4(self, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
         
        { commento: {110,}  se il ripristino del timer  SubClass_C2_restoreTI_TI1 non è scaduto, Verifica che   commento: {48,49,50,51,}   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} e  che  commento: {,}  la variabile SubClass_C2_variabile_V9 sia  uguale a GialloaVerdea
         commento: {104,} e  che  commento: {,}  il timer SubClass_C2_timer_T10 non sia disattivo
         commento: {104,} o  che  commento: {,}  il controllo SubClass_C2_controllo_C2 sia  diverso da GialloaVerdea
         commento: {104,} e  che  commento: {,}  il contatore SubClass_C2_contatore_Co6 sia  diverso da  commento: {56,} 14
        
        
        }
        """
        def populate_macroSubclass_c2_macrove_m4_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI1 non è scaduto, Verifica che   /*48,49,50,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V9 sia  uguale a GialloaVerdea
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T10 non sia disattivo
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C2 sia  diverso da GialloaVerdea
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co6 sia  diverso da  /*56,*/ 14""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI1 non è scaduto, Verifica che   /*48,49,50,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V9 sia  uguale a GialloaVerdea
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T10 non sia disattivo
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C2 sia  diverso da GialloaVerdea
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co6 sia  diverso da  /*56,*/ 14""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino del timer  SubClass_C2_restoreTI_TI1 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_restoreti_ti1_restore' è scaduto""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,50,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V9 sia  uguale a GialloaVerdea
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T10 non sia disattivo
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C2 sia  diverso da GialloaVerdea
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co6 sia  diverso da  /*56,*/ 14""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,49,50,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V9 sia  uguale a GialloaVerdea
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T10 non sia disattivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,49,50,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V9 sia  uguale a GialloaVerdea""", [
                            DIBoolExpr("""EqualImpl\nche   /*48,49,50,51,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  la variabile SubClass_C2_variabile_V9 sia  uguale a GialloaVerdea""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il timer SubClass_C2_timer_T10 non sia disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t10' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il controllo SubClass_C2_controllo_C2 sia  diverso da GialloaVerdea
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co6 sia  diverso da  /*56,*/ 14""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo SubClass_C2_controllo_C2 sia  diverso da GialloaVerdea""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c2)  è uguale a  (gialloaverdea)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore SubClass_C2_contatore_Co6 sia  diverso da  /*56,*/ 14""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co6)  è uguale a  (14)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroSubclass_c2_macrove_m4_SrfMacroDefInfo(di_ctx)
        return db((db(not db(not db(self.get_subclass_c2_restoreti_ti1_restore().isScaduto(), di_ctx.subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0]) or db((db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_variabile_v9() == GlobalEnumeration.gialloaverdea, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c2_timer_t10().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0]) or db((db(not db(self.get_subclass_c2_controllo_c2() == GlobalEnumeration.gialloaverdea, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) and db(not db(self.get_subclass_c2_contatore_co6().get_valore() == 14, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0])), di_ctx.subs[0])
    
    # value macros
    @srf_value_macro("macroSubclass_c2_macrova_m10")
    def macroSubclass_c2_macrova_m10(self, argomento_a1, argomento_a10, argomento_a2, argomento_a3, argomento_a5, argomento_a8, argomento_a9, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}  se la macro  SubClass_C2_macrova_M7 ( con argomento_a4   uguale a RossoGialloVerde ,argomento_a7   uguale a c120 ,argomento_a1   uguale a AC ,argomento_a5   uguale a GialloVerde  e argomento_a2   uguale a RossoGiallox )   è  uguale a Verde commento: {40,} ,  commento: {43,}  se MainClass_C1_timer_T9 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  commento: {105,} è disattivo, commento: {88,} quando  commento: {41,}   MainClass_C1_parametro_P10 del campo  MainClass_C1     commento: {105,} è  diverso da  True  , assegna alla macro il valore  True 
        
         commento: {46,} assegna alla macro il valore  True  commento: {],}
        }
        """
        def populate_macroSubclass_c2_macrova_m10_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/  se la macro  SubClass_C2_macrova_M7 ( con argomento_a4   uguale a RossoGialloVerde ,argomento_a7   uguale a c120 ,argomento_a1   uguale a AC ,argomento_a5   uguale a GialloVerde  e argomento_a2   uguale a RossoGiallox )   è  uguale a Verde /*40,*/ ,  /*43,*/  se MainClass_C1_timer_T9 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è disattivo, /*88,*/ quando  /*41,*/   MainClass_C1_parametro_P10 del campo  MainClass_C1     /*105,*/ è  diverso da  True  , assegna alla macro il valore  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*[*/  se la macro  SubClass_C2_macrova_M7 ( con argomento_a4   uguale a RossoGialloVerde ,argomento_a7   uguale a c120 ,argomento_a1   uguale a AC ,argomento_a5   uguale a GialloVerde  e argomento_a2   uguale a RossoGiallox )   è  uguale a Verde /*40,*/ ,  /*43,*/  se MainClass_C1_timer_T9 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è disattivo, /*88,*/ quando  /*41,*/   MainClass_C1_parametro_P10 del campo  MainClass_C1     /*105,*/ è  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroSubclass_c2_macrova_m7')  è uguale a  (verde)""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroSubclass_c2_macrova_m7'"""),#0
                            ]),#0
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {se (negazione di ((mainclass_c1_parametro_p10 del campo mainclass_c1 della lista subclass_c2_lista_l8)  è uguale a  (True))) allora (il timer 'mainclass_c1_timer_t9 del campo mainclass_c1 della lista subclass_c2_lista_l8' è inattivo)}""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\nse (negazione di ((mainclass_c1_parametro_p10 del campo mainclass_c1 della lista subclass_c2_lista_l8)  è uguale a  (True))) allora (il timer 'mainclass_c1_timer_t9 del campo mainclass_c1 della lista subclass_c2_lista_l8' è inattivo)""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p10 del campo mainclass_c1 della lista subclass_c2_lista_l8)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p10 del campo mainclass_c1 della lista subclass_c2_lista_l8)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t9 del campo mainclass_c1 della lista subclass_c2_lista_l8' è inattivo""", [
                            ]),#1
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroSubclass_c2_macrova_m10_SrfMacroDefInfo(di_ctx)
        #  /*[*/  se la macro  SubClass_C2_macrova_M7 ( con argomento_a4   uguale a RossoGialloVerde ,argomento_a7   uguale a c120 ,argomento_a1   uguale a AC ,argomento_a5   uguale a GialloVerde  e argomento_a2   uguale a RossoGiallox )   è  uguale a Verde /*40,*/ ,  /*43,*/  se MainClass_C1_timer_T9 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è disattivo, /*88,*/ quando  /*41,*/   MainClass_C1_parametro_P10 del campo  MainClass_C1     /*105,*/ è  diverso da  True  , assegna alla macro il valore  True
        if db((db(db(self.macroSubclass_c2_macrova_m7(GlobalEnumeration.ac,GlobalEnumeration.rossogiallox,GlobalEnumeration.rossogialloverde,GlobalEnumeration.gialloverde,GlobalEnumeration.c120, di_ctx.subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0]) == GlobalEnumeration.verde, di_ctx.subs[0].subs[0].subs[0]) and db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_timer_t9().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l8()) if db(not db(it.get_mainclass_c1().get_mainclass_c1_parametro_p10() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0][idx]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0][idx])), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            return True
        #  /*46,*/ assegna alla macro il valore  True
        return True
    
    @srf_value_macro("macroSubclass_c2_macrova_m2")
    def macroSubclass_c2_macrova_m2(self, argomento_a10, argomento_a3, argomento_a4, argomento_a6, argomento_a7, argomento_a8, argomento_a9, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}  se l'argomento argomento_a3 è  uguale a RossoGiallox commento: {39,}  e  se l'argomento argomento_a8 non  è  diverso da GialloaVerdea commento: {39,} ,  commento: {44,}  se  MainClass_C1_variabile_V1 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  commento: {105,} è  diverso da  commento: {56,} 6, commento: {88,} quando  commento: {41,}   MainClass_C1_parametro_P10 del campo  MainClass_C1     commento: {105,} è  diverso da  False  commento: {44,} o  se  MainClass_C1_variabile_V5 del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  commento: {105,} è  uguale a  False  , assegna alla macro il valore  False 
        
         commento: {46,} assegna alla macro il valore  False  commento: {],}
        }
        """
        def populate_macroSubclass_c2_macrova_m2_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/  se l'argomento argomento_a3 è  uguale a RossoGiallox /*39,*/  e  se l'argomento argomento_a8 non  è  diverso da GialloaVerdea /*39,*/ ,  /*44,*/  se  MainClass_C1_variabile_V1 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  diverso da  /*56,*/ 6, /*88,*/ quando  /*41,*/   MainClass_C1_parametro_P10 del campo  MainClass_C1     /*105,*/ è  diverso da  False  /*44,*/ o  se  MainClass_C1_variabile_V5 del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  /*105,*/ è  uguale a  False  , assegna alla macro il valore  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*[*/  se l'argomento argomento_a3 è  uguale a RossoGiallox /*39,*/  e  se l'argomento argomento_a8 non  è  diverso da GialloaVerdea /*39,*/ ,  /*44,*/  se  MainClass_C1_variabile_V1 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  diverso da  /*56,*/ 6, /*88,*/ quando  /*41,*/   MainClass_C1_parametro_P10 del campo  MainClass_C1     /*105,*/ è  diverso da  False  /*44,*/ o  se  MainClass_C1_variabile_V5 del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  /*105,*/ è  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (argomento_a3)  è uguale a  (rossogiallox) )  e  
( ( negazione di (negazione di ((argomento_a8)  è uguale a  (gialloaverdea))) )  e  ( per ognuna delle seguenti con lista non vuota {se (negazione di ((mainclass_c1_parametro_p10 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (False))) allora (negazione di ((mainclass_c1_variabile_v1 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (6)))} ) )""", [
                            DIBoolExpr("""EqualImpl\n(argomento_a3)  è uguale a  (rossogiallox)""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (negazione di ((argomento_a8)  è uguale a  (gialloaverdea))) )  e  ( per ognuna delle seguenti con lista non vuota {se (negazione di ((mainclass_c1_parametro_p10 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (False))) allora (negazione di ((mainclass_c1_variabile_v1 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (6)))} )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((argomento_a8)  è uguale a  (gialloaverdea)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_a8)  è uguale a  (gialloaverdea))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_a8)  è uguale a  (gialloaverdea)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {se (negazione di ((mainclass_c1_parametro_p10 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (False))) allora (negazione di ((mainclass_c1_variabile_v1 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (6)))}""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\nse (negazione di ((mainclass_c1_parametro_p10 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (False))) allora (negazione di ((mainclass_c1_variabile_v1 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (6)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p10 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p10 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v1 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (6))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v1 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (6)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {((mainclass_c1_variabile_v5 del campo mainclass_c1 della lista subclass_c2_lista_l10)  è uguale a  (False))}""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v5 del campo mainclass_c1 della lista subclass_c2_lista_l10)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroSubclass_c2_macrova_m2_SrfMacroDefInfo(di_ctx)
        #  /*[*/  se l'argomento argomento_a3 è  uguale a RossoGiallox /*39,*/  e  se l'argomento argomento_a8 non  è  diverso da GialloaVerdea /*39,*/ ,  /*44,*/  se  MainClass_C1_variabile_V1 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  diverso da  /*56,*/ 6, /*88,*/ quando  /*41,*/   MainClass_C1_parametro_P10 del campo  MainClass_C1     /*105,*/ è  diverso da  False  /*44,*/ o  se  MainClass_C1_variabile_V5 del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  /*105,*/ è  uguale a  False  , assegna alla macro il valore  False
        if db((db((db(argomento_a3 == GlobalEnumeration.rossogiallox, di_ctx.subs[0].subs[0].subs[0].subs[0]) and db((db(not db(not db(argomento_a8 == GlobalEnumeration.gialloaverdea, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]) and db(all_notempty(db(not db(it.get_mainclass_c1().get_mainclass_c1_variabile_v1() == 6, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0][idx]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1].subs[0].subs[1][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l3()) if db(not db(it.get_mainclass_c1().get_mainclass_c1_parametro_p10() == False, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0][idx]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1].subs[0].subs[0][idx])), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_variabile_v5() == False, di_ctx.subs[0].subs[0].subs[1].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l10())), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            return False
        #  /*46,*/ assegna alla macro il valore  False
        return False
    
    @srf_value_macro("macroSubclass_c2_macrova_m6")
    def macroSubclass_c2_macrova_m6(self, argomento_a10, argomento_a3, argomento_a6, argomento_a9, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}
         commento: {46,} assegna alla macro il valore  True  commento: {],}
        }
        """
        def populate_macroSubclass_c2_macrova_m6_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                ])

        populate_macroSubclass_c2_macrova_m6_SrfMacroDefInfo(di_ctx)
        
        #  /*[*/
        #   /*46,*/ assegna alla macro il valore  True
        return True
    
    @srf_value_macro("macroSubclass_c2_macrova_m7")
    def macroSubclass_c2_macrova_m7(self, argomento_a1, argomento_a2, argomento_a4, argomento_a5, argomento_a7, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[} commento: {109,}  se il ripristino della variabile  SubClass_C2_restoreva_RV5 non è  diverso da  True  commento: {44,} e  se  MainClass_C1_variabile_V5 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  commento: {105,} è  uguale a  False  commento: {44,} e  se  MainClass_C1_variabile_V5 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  commento: {105,} è  uguale a  False  commento: {37,} o  se la variabile SubClass_C2_variabile_V4 è  minore di  commento: {55,} 7 , assegna alla macro il valore Verde
        
         commento: {46,} assegna alla macro il valore Verde commento: {],}
        }
        """
        def populate_macroSubclass_c2_macrova_m7_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/ /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV5 non è  diverso da  True  /*44,*/ e  se  MainClass_C1_variabile_V5 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è  uguale a  False  /*44,*/ e  se  MainClass_C1_variabile_V5 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  uguale a  False  /*37,*/ o  se la variabile SubClass_C2_variabile_V4 è  minore di  /*55,*/ 7 , assegna alla macro il valore Verde""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*[*/ /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV5 non è  diverso da  True  /*44,*/ e  se  MainClass_C1_variabile_V5 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è  uguale a  False  /*44,*/ e  se  MainClass_C1_variabile_V5 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  uguale a  False  /*37,*/ o  se la variabile SubClass_C2_variabile_V4 è  minore di  /*55,*/ 7""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di (negazione di ((subclass_c2_restoreva_rv5_restore)  è uguale a  (True))) )  e  ( per ognuna delle seguenti con lista non vuota {((mainclass_c1_variabile_v5 del campo mainclass_c1 della lista subclass_c2_lista_l8)  è uguale a  (False))} ) )  e  
( per ognuna delle seguenti con lista non vuota {((mainclass_c1_variabile_v5 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (False))} )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (negazione di ((subclass_c2_restoreva_rv5_restore)  è uguale a  (True))) )  e  ( per ognuna delle seguenti con lista non vuota {((mainclass_c1_variabile_v5 del campo mainclass_c1 della lista subclass_c2_lista_l8)  è uguale a  (False))} )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_restoreva_rv5_restore)  è uguale a  (True)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_restoreva_rv5_restore)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_restoreva_rv5_restore)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {((mainclass_c1_variabile_v5 del campo mainclass_c1 della lista subclass_c2_lista_l8)  è uguale a  (False))}""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v5 del campo mainclass_c1 della lista subclass_c2_lista_l8)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {((mainclass_c1_variabile_v5 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (False))}""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v5 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_variabile_v4)  è minore di  (7)""", [
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroSubclass_c2_macrova_m7_SrfMacroDefInfo(di_ctx)
        #  /*[*/ /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV5 non è  diverso da  True  /*44,*/ e  se  MainClass_C1_variabile_V5 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è  uguale a  False  /*44,*/ e  se  MainClass_C1_variabile_V5 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  uguale a  False  /*37,*/ o  se la variabile SubClass_C2_variabile_V4 è  minore di  /*55,*/ 7 , assegna alla macro il valore Verde
        if db((db((db((db(not db(not db(self.get_subclass_c2_restoreva_rv5_restore() == True, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) and db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_variabile_v5() == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l8())), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_variabile_v5() == False, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l3())), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_variabile_v4() < 7, di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            return GlobalEnumeration.verde
        #  /*46,*/ assegna alla macro il valore Verde
        return GlobalEnumeration.verde
    
    # for each manual command, the corresponding method is created
    def eventSubclass_c2_command_comm6(self, notifying_process):
        notifying_process.response_notify_man_cmd(self, 'eventSubclass_c2_command_comm6')
    
    # for each automatic command, the corresponding method is created
    def eventSubclass_c2_command_comm7(self, notifying_process):
        notifying_process.response_notify_auto_cmd(self, 'eventSubclass_c2_command_comm7')
    
    def eventSubclass_c2_command_comm9(self, notifying_process):
        notifying_process.response_notify_auto_cmd(self, 'eventSubclass_c2_command_comm9')
    

    def update_precedente(self):
        # update the variables with previous value
        self.set_subclass_c2_previousco_c1_prev(self.get_subclass_c2_previousco_c1())
        self.set_subclass_c2_previousco_c10_prev(self.get_subclass_c2_previousco_c10())
        self.set_subclass_c2_previousco_c4_prev(self.get_subclass_c2_previousco_c4())
        self.set_subclass_c2_previousva_pv1_prev(self.get_subclass_c2_previousva_pv1())
        self.set_subclass_c2_previousva_pv2_prev(self.get_subclass_c2_previousva_pv2())
        self.set_subclass_c2_previousva_pv3_prev(self.get_subclass_c2_previousva_pv3())
        self.set_subclass_c2_previousva_pv4_prev(self.get_subclass_c2_previousva_pv4())
        self.set_subclass_c2_previousva_pv5_prev(self.get_subclass_c2_previousva_pv5())

class SubClass_C2_RecordHeaderR4(ParamRecord):
    # ProcessImpl is the class that is extended.
    # ProcessImpl contains the get/set methods for the current state variable and
    # the methods that generate the responses

    # method called by the configurator before the use of the scheduler
    # it creates the references of the processes needed
    def init_configuration(self, mainclass_c1, recordfiled17, recordfiled20, recordfiled5):
        self.set_mainclass_c1(mainclass_c1)
        self.set_recordfiled17(recordfiled17)
        self.set_recordfiled20(recordfiled20)
        self.set_recordfiled5(recordfiled5)

    # setters for the fields of record
    def set_mainclass_c1(self, mainclass_c1):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "mainclass_c1"), mainclass_c1)

    def set_recordfiled17(self, recordfiled17):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled17"), recordfiled17)

    def set_recordfiled20(self, recordfiled20):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled20"), recordfiled20)

    def set_recordfiled5(self, recordfiled5):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled5"), recordfiled5)


    # getters for the fields of record
    def get_mainclass_c1(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "mainclass_c1"))

    def get_recordfiled17(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled17"))

    def get_recordfiled20(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled20"))

    def get_recordfiled5(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled5"))



class SubClass_C2_RecordHeaderR7(ParamRecord):
    # ProcessImpl is the class that is extended.
    # ProcessImpl contains the get/set methods for the current state variable and
    # the methods that generate the responses

    # method called by the configurator before the use of the scheduler
    # it creates the references of the processes needed
    def init_configuration(self, mainclass_c1, recordfiled18, recordfiled9, recordfiled7, recordfiled3):
        self.set_mainclass_c1(mainclass_c1)
        self.set_recordfiled18(recordfiled18)
        self.set_recordfiled9(recordfiled9)
        self.set_recordfiled7(recordfiled7)
        self.set_recordfiled3(recordfiled3)

    # setters for the fields of record
    def set_mainclass_c1(self, mainclass_c1):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "mainclass_c1"), mainclass_c1)

    def set_recordfiled18(self, recordfiled18):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled18"), recordfiled18)

    def set_recordfiled9(self, recordfiled9):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled9"), recordfiled9)

    def set_recordfiled7(self, recordfiled7):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled7"), recordfiled7)

    def set_recordfiled3(self, recordfiled3):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled3"), recordfiled3)


    # getters for the fields of record
    def get_mainclass_c1(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "mainclass_c1"))

    def get_recordfiled18(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled18"))

    def get_recordfiled9(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled9"))

    def get_recordfiled7(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled7"))

    def get_recordfiled3(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled3"))



