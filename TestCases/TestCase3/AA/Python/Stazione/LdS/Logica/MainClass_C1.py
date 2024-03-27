# Codice del modello 'TestCase3', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
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

class MainClass_C1(ProcessImpl):
    # ProcessImpl is the class that is extended.
    # ProcessImpl contains the get/set methods for the current state variable and
    # the methods that generate the responses
    def __init__(self, *args, **kwds):
        super(MainClass_C1, self).__init__(*args, **kwds)

        # initialize the state variables

        self.set_mainclass_c1_previousva_pv1(GlobalEnumeration.c270xx)
        self.set_mainclass_c1_previousva_pv2(0)
        self.set_mainclass_c1_previousva_pv3(0)
        self.set_mainclass_c1_restoreva_rv1(GlobalEnumeration.avvio)
        self.set_mainclass_c1_restoreva_rv2(False)
        self.set_mainclass_c1_restoreva_rv3(False)
        self.set_mainclass_c1_restoreva_rv4(0)
        self.set_mainclass_c1_restoreva_rv5(False)
        self.set_mainclass_c1_variabile_v1(GlobalEnumeration.rossogialloaverdea)
        self.set_mainclass_c1_variabile_v10(0)
        self.set_mainclass_c1_variabile_v2(0)
        self.set_mainclass_c1_variabile_v3(GlobalEnumeration.rossogialloaverdea)
        self.set_mainclass_c1_variabile_v9(GlobalEnumeration.rossoverde)

        self._expected_commands_map = {
            Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1 : set(['eventMainclass_c1_command_comm10DaSenderac49796',]),
        }

    def set_expected_cmds_response(self):
        # for each manual command of MainClass_C1
        if self.is_triggered('eventMainclass_c1_command_comm10DaSenderac49796'):
            self.set_man_cmd_response('eventMainclass_c1_command_comm10DaSenderac49796',self.ManCmdResponse.UNEXPECTED)
        else:
            self.set_man_cmd_response('eventMainclass_c1_command_comm10DaSenderac49796',self.ManCmdResponse.NOOP)


        if self.is_current_state(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1):
        # for each manual command that can be received in Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1
            if self.is_triggered('eventMainclass_c1_command_comm10DaSenderac49796'):
                self.set_man_cmd_response('eventMainclass_c1_command_comm10DaSenderac49796',self.ManCmdResponse.BLOCKED)

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
    def init_configuration(self, mainclass_c1_parametro_p10, mainclass_c1_parametro_p3, mainclass_c1_parametro_p6, mainclass_c1_parametro_p7, mainclass_c1_parametro_p8):
        # initialize the record type parameters
        # initialize the simple type parameters
        self.set_mainclass_c1_parametro_p10(mainclass_c1_parametro_p10)
        self.set_mainclass_c1_parametro_p3(mainclass_c1_parametro_p3)
        self.set_mainclass_c1_parametro_p6(mainclass_c1_parametro_p6)
        self.set_mainclass_c1_parametro_p7(mainclass_c1_parametro_p7)
        self.set_mainclass_c1_parametro_p8(mainclass_c1_parametro_p8)

        # initialize the timers
        self.set_mainclass_c1_restoreti_ti1(340000)
        self.set_mainclass_c1_restoreti_ti1_restore(340000)
        self.set_mainclass_c1_restoreti_ti2(1315000)
        self.set_mainclass_c1_restoreti_ti2_restore(1315000)
        self.set_mainclass_c1_restoreti_ti3(424000)
        self.set_mainclass_c1_restoreti_ti3_restore(424000)
        self.set_mainclass_c1_restoreti_ti4(50000)
        self.set_mainclass_c1_restoreti_ti4_restore(50000)
        self.set_mainclass_c1_timer_t2(4152000)
        self.set_mainclass_c1_timer_t5(23000)

        self.timers = [self.mainclass_c1_restoreti_ti1,self.mainclass_c1_restoreti_ti1_restore,self.mainclass_c1_restoreti_ti2,self.mainclass_c1_restoreti_ti2_restore,self.mainclass_c1_restoreti_ti3,self.mainclass_c1_restoreti_ti3_restore,self.mainclass_c1_restoreti_ti4,self.mainclass_c1_restoreti_ti4_restore,self.mainclass_c1_timer_t2,self.mainclass_c1_timer_t5,]

        # initialize the counters
        self.set_mainclass_c1_contatore_co3(0)

    # setters for record type parameters

    # getters for record type parameters

    # setters for simple type parameters
    def set_mainclass_c1_parametro_p10(self, mainclass_c1_parametro_p10):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p10",mainclass_c1_parametro_p10)

    def set_mainclass_c1_parametro_p3(self, mainclass_c1_parametro_p3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p3",mainclass_c1_parametro_p3)

    def set_mainclass_c1_parametro_p6(self, mainclass_c1_parametro_p6):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p6",mainclass_c1_parametro_p6)

    def set_mainclass_c1_parametro_p7(self, mainclass_c1_parametro_p7):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p7",mainclass_c1_parametro_p7)

    def set_mainclass_c1_parametro_p8(self, mainclass_c1_parametro_p8):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p8",mainclass_c1_parametro_p8)


    # getters for simple type parameters
    def get_mainclass_c1_parametro_p10(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p10")

    def get_mainclass_c1_parametro_p3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p3")

    def get_mainclass_c1_parametro_p6(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p6")

    def get_mainclass_c1_parametro_p7(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p7")

    def get_mainclass_c1_parametro_p8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p8")


    # setters for comandi al piazzale
    def set_mainclass_c1_comando_c2(self, mainclass_c1_comando_c2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c2",mainclass_c1_comando_c2)

    def set_mainclass_c1_comando_c3(self, mainclass_c1_comando_c3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c3",mainclass_c1_comando_c3)

    def set_mainclass_c1_comando_c7(self, mainclass_c1_comando_c7):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c7",mainclass_c1_comando_c7)

    def set_mainclass_c1_comando_c8(self, mainclass_c1_comando_c8):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c8",mainclass_c1_comando_c8)

    def set_mainclass_c1_comando_c9(self, mainclass_c1_comando_c9):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c9",mainclass_c1_comando_c9)


    # getters for controlli dal piazzale
    def get_consdef(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"consdef")

    def get_mainclass_c1_controllo_c1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c1")

    def get_mainclass_c1_controllo_c2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c2")

    def get_mainclass_c1_controllo_c9(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c9")

    def get_mainclass_c1_previousco_c10(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c10")

    def get_mainclass_c1_previousco_c4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c4")

    def get_mainclass_c1_previousco_c5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c5")

    def get_mainclass_c1_previousco_c6(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c6")


    # setters for state variables
    def set_mainclass_c1_previousco_c10_prev(self, mainclass_c1_previousco_c10_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c10_prev",mainclass_c1_previousco_c10_prev)
    def set_mainclass_c1_previousco_c4_prev(self, mainclass_c1_previousco_c4_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c4_prev",mainclass_c1_previousco_c4_prev)
    def set_mainclass_c1_previousco_c5_prev(self, mainclass_c1_previousco_c5_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c5_prev",mainclass_c1_previousco_c5_prev)
    def set_mainclass_c1_previousco_c6_prev(self, mainclass_c1_previousco_c6_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c6_prev",mainclass_c1_previousco_c6_prev)
    def set_mainclass_c1_previousva_pv1(self, mainclass_c1_previousva_pv1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousva_pv1",mainclass_c1_previousva_pv1)
    def set_mainclass_c1_previousva_pv1_prev(self, mainclass_c1_previousva_pv1_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousva_pv1_prev",mainclass_c1_previousva_pv1_prev)
    def set_mainclass_c1_previousva_pv2(self, mainclass_c1_previousva_pv2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousva_pv2",mainclass_c1_previousva_pv2)
    def set_mainclass_c1_previousva_pv2_prev(self, mainclass_c1_previousva_pv2_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousva_pv2_prev",mainclass_c1_previousva_pv2_prev)
    def set_mainclass_c1_previousva_pv3(self, mainclass_c1_previousva_pv3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousva_pv3",mainclass_c1_previousva_pv3)
    def set_mainclass_c1_previousva_pv3_prev(self, mainclass_c1_previousva_pv3_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousva_pv3_prev",mainclass_c1_previousva_pv3_prev)
    def set_mainclass_c1_restoreva_rv1(self, mainclass_c1_restoreva_rv1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv1",mainclass_c1_restoreva_rv1)
    def set_mainclass_c1_restoreva_rv2(self, mainclass_c1_restoreva_rv2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv2",mainclass_c1_restoreva_rv2)
    def set_mainclass_c1_restoreva_rv3(self, mainclass_c1_restoreva_rv3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv3",mainclass_c1_restoreva_rv3)
    def set_mainclass_c1_restoreva_rv4(self, mainclass_c1_restoreva_rv4):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv4",mainclass_c1_restoreva_rv4)
    def set_mainclass_c1_restoreva_rv5(self, mainclass_c1_restoreva_rv5):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv5",mainclass_c1_restoreva_rv5)
    def set_mainclass_c1_variabile_v1(self, mainclass_c1_variabile_v1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v1",mainclass_c1_variabile_v1)
    def set_mainclass_c1_variabile_v10(self, mainclass_c1_variabile_v10):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v10",mainclass_c1_variabile_v10)
    def set_mainclass_c1_variabile_v2(self, mainclass_c1_variabile_v2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v2",mainclass_c1_variabile_v2)
    def set_mainclass_c1_variabile_v3(self, mainclass_c1_variabile_v3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v3",mainclass_c1_variabile_v3)
    def set_mainclass_c1_variabile_v9(self, mainclass_c1_variabile_v9):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v9",mainclass_c1_variabile_v9)

    # getters for state variables
    def get_mainclass_c1_previousco_c10_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c10_prev")

    def get_mainclass_c1_previousco_c4_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c4_prev")

    def get_mainclass_c1_previousco_c5_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c5_prev")

    def get_mainclass_c1_previousco_c6_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c6_prev")

    def get_mainclass_c1_previousva_pv1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousva_pv1")

    def get_mainclass_c1_previousva_pv1_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousva_pv1_prev")

    def get_mainclass_c1_previousva_pv2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousva_pv2")

    def get_mainclass_c1_previousva_pv2_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousva_pv2_prev")

    def get_mainclass_c1_previousva_pv3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousva_pv3")

    def get_mainclass_c1_previousva_pv3_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousva_pv3_prev")

    def get_mainclass_c1_restoreva_rv1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv1")

    def get_mainclass_c1_restoreva_rv1_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv1_restore")

    def get_mainclass_c1_restoreva_rv2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv2")

    def get_mainclass_c1_restoreva_rv2_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv2_restore")

    def get_mainclass_c1_restoreva_rv3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv3")

    def get_mainclass_c1_restoreva_rv3_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv3_restore")

    def get_mainclass_c1_restoreva_rv4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv4")

    def get_mainclass_c1_restoreva_rv4_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv4_restore")

    def get_mainclass_c1_restoreva_rv5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv5")

    def get_mainclass_c1_restoreva_rv5_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv5_restore")

    def get_mainclass_c1_variabile_v1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v1")

    def get_mainclass_c1_variabile_v10(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v10")

    def get_mainclass_c1_variabile_v2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v2")

    def get_mainclass_c1_variabile_v3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v3")

    def get_mainclass_c1_variabile_v9(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v9")

    def get_stato_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"stato_restore")


    # setters for timers
    def set_mainclass_c1_restoreti_ti1(self, timerDuration):
        self.mainclass_c1_restoreti_ti1 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_restoreti_ti1", self.memory)

    def set_mainclass_c1_restoreti_ti1_restore(self, timerDuration):
        self.mainclass_c1_restoreti_ti1_restore = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_restoreti_ti1_restore", self.memory)

    def set_mainclass_c1_restoreti_ti2(self, timerDuration):
        self.mainclass_c1_restoreti_ti2 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_restoreti_ti2", self.memory)

    def set_mainclass_c1_restoreti_ti2_restore(self, timerDuration):
        self.mainclass_c1_restoreti_ti2_restore = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_restoreti_ti2_restore", self.memory)

    def set_mainclass_c1_restoreti_ti3(self, timerDuration):
        self.mainclass_c1_restoreti_ti3 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_restoreti_ti3", self.memory)

    def set_mainclass_c1_restoreti_ti3_restore(self, timerDuration):
        self.mainclass_c1_restoreti_ti3_restore = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_restoreti_ti3_restore", self.memory)

    def set_mainclass_c1_restoreti_ti4(self, timerDuration):
        self.mainclass_c1_restoreti_ti4 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_restoreti_ti4", self.memory)

    def set_mainclass_c1_restoreti_ti4_restore(self, timerDuration):
        self.mainclass_c1_restoreti_ti4_restore = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_restoreti_ti4_restore", self.memory)

    def set_mainclass_c1_timer_t2(self, timerDuration):
        self.mainclass_c1_timer_t2 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_timer_t2", self.memory)

    def set_mainclass_c1_timer_t5(self, timerDuration):
        self.mainclass_c1_timer_t5 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_timer_t5", self.memory)


    # getters for timers
    def get_mainclass_c1_restoreti_ti1(self):
        return self.mainclass_c1_restoreti_ti1

    def get_mainclass_c1_restoreti_ti1_restore(self):
        return self.mainclass_c1_restoreti_ti1_restore

    def get_mainclass_c1_restoreti_ti2(self):
        return self.mainclass_c1_restoreti_ti2

    def get_mainclass_c1_restoreti_ti2_restore(self):
        return self.mainclass_c1_restoreti_ti2_restore

    def get_mainclass_c1_restoreti_ti3(self):
        return self.mainclass_c1_restoreti_ti3

    def get_mainclass_c1_restoreti_ti3_restore(self):
        return self.mainclass_c1_restoreti_ti3_restore

    def get_mainclass_c1_restoreti_ti4(self):
        return self.mainclass_c1_restoreti_ti4

    def get_mainclass_c1_restoreti_ti4_restore(self):
        return self.mainclass_c1_restoreti_ti4_restore

    def get_mainclass_c1_timer_t2(self):
        return self.mainclass_c1_timer_t2

    def get_mainclass_c1_timer_t5(self):
        return self.mainclass_c1_timer_t5


    # setters for counters
    def set_mainclass_c1_contatore_co3(self, counterInitValue):
        self.mainclass_c1_contatore_co3 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "mainclass_c1_contatore_co3", self.memory)


    # getters for counters
    def get_mainclass_c1_contatore_co3(self):
        return self.mainclass_c1_contatore_co3



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
                    DIBoolExpr("""NAryLogicOP (AND)\n/*81,*/  Ricezione del  comando manuale   MainClass_C1_command_comm10 da  Senderac49796   /*76,*/
 /*67,*/ /*37,*/  se la variabile MainClass_C1_variabile_V1 è  diverso da RossoGialloxVerdex e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile MainClass_C1_variabile_V3 è  uguale a RossoGialloxVerdex /*35,*/ o  se il controllo MainClass_C1_controllo_C1 è  diverso da  True  e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C9 è  diverso da RossoGialloxVerdex, Tutte le seguenti { 
 /*69,*/ /*37,*/  se la variabile MainClass_C1_variabile_V9 è  uguale a c180x /*37,*/ e  se la variabile MainClass_C1_variabile_V9 non è  uguale a c180x o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  uguale a  /*53,*/ 2 /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  uguale a  /*53,*/ 8 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*38,*/  se il contatore MainClass_C1_contatore_Co3 è  minore di  /*55,*/ 13 e  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co3 non è  diverso da  /*56,*/ 14 /*36,*/ o  se il timer MainClass_C1_timer_T2 non è scaduto, Verifica che   /*49,*/  /*,*/  il timer MainClass_C1_timer_T5 sia scaduto


 } Verifica che   /*51,*/  /*,*/  il contatore MainClass_C1_contatore_Co3 sia  minore di  /*55,*/ 12


 } Verifica che   /*47,*/  /*34,*/  il parametro MainClass_C1_parametro_P6 sia  diverso da  False""", [
                    EventDebInfo("""Ricezione Comando Manuale\ncomando manuale   MainClass_C1_command_comm10 da  Senderac49796"""),#0
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*76,*/
 /*67,*/ /*37,*/  se la variabile MainClass_C1_variabile_V1 è  diverso da RossoGialloxVerdex e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile MainClass_C1_variabile_V3 è  uguale a RossoGialloxVerdex /*35,*/ o  se il controllo MainClass_C1_controllo_C1 è  diverso da  True  e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C9 è  diverso da RossoGialloxVerdex, Tutte le seguenti { 
 /*69,*/ /*37,*/  se la variabile MainClass_C1_variabile_V9 è  uguale a c180x /*37,*/ e  se la variabile MainClass_C1_variabile_V9 non è  uguale a c180x o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  uguale a  /*53,*/ 2 /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  uguale a  /*53,*/ 8 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*38,*/  se il contatore MainClass_C1_contatore_Co3 è  minore di  /*55,*/ 13 e  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co3 non è  diverso da  /*56,*/ 14 /*36,*/ o  se il timer MainClass_C1_timer_T2 non è scaduto, Verifica che   /*49,*/  /*,*/  il timer MainClass_C1_timer_T5 sia scaduto


 } Verifica che   /*51,*/  /*,*/  il contatore MainClass_C1_contatore_Co3 sia  minore di  /*55,*/ 12


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*76,*/
 /*67,*/ /*37,*/  se la variabile MainClass_C1_variabile_V1 è  diverso da RossoGialloxVerdex e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile MainClass_C1_variabile_V3 è  uguale a RossoGialloxVerdex /*35,*/ o  se il controllo MainClass_C1_controllo_C1 è  diverso da  True  e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C9 è  diverso da RossoGialloxVerdex""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*76,*/
 /*67,*/ /*37,*/  se la variabile MainClass_C1_variabile_V1 è  diverso da RossoGialloxVerdex e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile MainClass_C1_variabile_V3 è  uguale a RossoGialloxVerdex /*35,*/ o  se il controllo MainClass_C1_controllo_C1 è  diverso da  True  e  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*76,*/
 /*67,*/ /*37,*/  se la variabile MainClass_C1_variabile_V1 è  diverso da RossoGialloxVerdex e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile MainClass_C1_variabile_V3 è  uguale a RossoGialloxVerdex""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*76,*/
 /*67,*/ /*37,*/  se la variabile MainClass_C1_variabile_V1 è  diverso da RossoGialloxVerdex e  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V1 è  diverso da RossoGialloxVerdex""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v1)  è uguale a  (rossogialloxverdex)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nla variabile MainClass_C1_variabile_V3 è  uguale a RossoGialloxVerdex""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nse il controllo MainClass_C1_controllo_C1 è  diverso da  True  e  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C1 è  diverso da  True""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c1)  è uguale a  (True)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C9 è  diverso da RossoGialloxVerdex""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c9)  è uguale a  (rossogialloxverdex)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*69,*/ /*37,*/  se la variabile MainClass_C1_variabile_V9 è  uguale a c180x /*37,*/ e  se la variabile MainClass_C1_variabile_V9 non è  uguale a c180x o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  uguale a  /*53,*/ 2 /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  uguale a  /*53,*/ 8 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*38,*/  se il contatore MainClass_C1_contatore_Co3 è  minore di  /*55,*/ 13 e  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co3 non è  diverso da  /*56,*/ 14 /*36,*/ o  se il timer MainClass_C1_timer_T2 non è scaduto, Verifica che   /*49,*/  /*,*/  il timer MainClass_C1_timer_T5 sia scaduto


 } Verifica che   /*51,*/  /*,*/  il contatore MainClass_C1_contatore_Co3 sia  minore di  /*55,*/ 12


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*69,*/ /*37,*/  se la variabile MainClass_C1_variabile_V9 è  uguale a c180x /*37,*/ e  se la variabile MainClass_C1_variabile_V9 non è  uguale a c180x o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  uguale a  /*53,*/ 2 /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  uguale a  /*53,*/ 8 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*38,*/  se il contatore MainClass_C1_contatore_Co3 è  minore di  /*55,*/ 13 e  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co3 non è  diverso da  /*56,*/ 14 /*36,*/ o  se il timer MainClass_C1_timer_T2 non è scaduto, Verifica che   /*49,*/  /*,*/  il timer MainClass_C1_timer_T5 sia scaduto


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*69,*/ /*37,*/  se la variabile MainClass_C1_variabile_V9 è  uguale a c180x /*37,*/ e  se la variabile MainClass_C1_variabile_V9 non è  uguale a c180x o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  uguale a  /*53,*/ 2 /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  uguale a  /*53,*/ 8 e  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*69,*/ /*37,*/  se la variabile MainClass_C1_variabile_V9 è  uguale a c180x /*37,*/ e  se la variabile MainClass_C1_variabile_V9 non è  uguale a c180x o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  uguale a  /*53,*/ 2""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*69,*/ /*37,*/  se la variabile MainClass_C1_variabile_V9 è  uguale a c180x /*37,*/ e  se la variabile MainClass_C1_variabile_V9 non è  uguale a c180x o  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*69,*/ /*37,*/  se la variabile MainClass_C1_variabile_V9 è  uguale a c180x /*37,*/ e  se la variabile MainClass_C1_variabile_V9 non è  uguale a c180x""", [
                    DIBoolExpr("""EqualImpl\nla variabile MainClass_C1_variabile_V9 è  uguale a c180x""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V9 non è  uguale a c180x""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v9)  è uguale a  (c180x)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P3 non è  uguale a  /*53,*/ 2""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3)  è uguale a  (2)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nse il parametro MainClass_C1_parametro_P8 è  uguale a  /*53,*/ 8 e  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""EqualImpl\nil parametro MainClass_C1_parametro_P8 è  uguale a  /*53,*/ 8""", [
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*38,*/  se il contatore MainClass_C1_contatore_Co3 è  minore di  /*55,*/ 13 e  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co3 non è  diverso da  /*56,*/ 14 /*36,*/ o  se il timer MainClass_C1_timer_T2 non è scaduto, Verifica che   /*49,*/  /*,*/  il timer MainClass_C1_timer_T5 sia scaduto""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*38,*/  se il contatore MainClass_C1_contatore_Co3 è  minore di  /*55,*/ 13 e  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co3 non è  diverso da  /*56,*/ 14 /*36,*/ o  se il timer MainClass_C1_timer_T2 non è scaduto""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*38,*/  se il contatore MainClass_C1_contatore_Co3 è  minore di  /*55,*/ 13 e  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co3 non è  diverso da  /*56,*/ 14""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*38,*/  se il contatore MainClass_C1_contatore_Co3 è  minore di  /*55,*/ 13 e  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""LessThanImpl\nil contatore MainClass_C1_contatore_Co3 è  minore di  /*55,*/ 13""", [
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co3 non è  diverso da  /*56,*/ 14""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co3)  è uguale a  (14))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co3)  è uguale a  (14)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T2 non è scaduto""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t2' è scaduto""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nche   /*49,*/  /*,*/  il timer MainClass_C1_timer_T5 sia scaduto""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""LessThanImpl\nche   /*51,*/  /*,*/  il contatore MainClass_C1_contatore_Co3 sia  minore di  /*55,*/ 12""", [
                    ]),#1
                    ]),#1
                    ]),#1
                    DIBoolExpr("""Operatore Logico Not\nche   /*47,*/  /*34,*/  il parametro MainClass_C1_parametro_P6 sia  diverso da  False""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p6)  è uguale a  (False)""", [
                    ]),#0
                    ]),#2
                    ]),#1
                    DIStatement("""ITEStatementImpl\nse il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*37,*/ e  se la variabile MainClass_C1_variabile_V10 è  diverso da  /*56,*/ 1 /*37,*/ o  se la variabile MainClass_C1_variabile_V1 non è  uguale a RossoGialloxVerdex /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  uguale a  True , /*68,*/Attiva il timer MainClass_C1_timer_T2

 ,altrimenti  /*66,*/ Assegna al comando MainClass_C1_comando_C2 il valore  False""", [
                    DIBoolExpr("""NAryLogicOP (OR)\nse il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*37,*/ e  se la variabile MainClass_C1_variabile_V10 è  diverso da  /*56,*/ 1 /*37,*/ o  se la variabile MainClass_C1_variabile_V1 non è  uguale a RossoGialloxVerdex /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  uguale a  True""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((stato_restore)  è uguale a  (state1)) )  e  
( negazione di ((mainclass_c1_variabile_v10)  è uguale a  (1)) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((stato_restore)  è uguale a  (state1))""", [
                    DIBoolExpr("""EqualImpl\n(stato_restore)  è uguale a  (state1)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v10)  è uguale a  (1))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v10)  è uguale a  (1)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_variabile_v1)  è uguale a  (rossogialloxverdex)) )  e  
( (mainclass_c1_controllo_c2)  è uguale a  (True) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v1)  è uguale a  (rossogialloxverdex))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v1)  è uguale a  (rossogialloxverdex)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c2)  è uguale a  (True)""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    ]),#2
                    DIStatement("""ITStatement\nse il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co3 non è  diverso da  /*56,*/ 123,  Applica gli effetti
       della macro MainClass_C1_macroef_M1""", [
                    DIBoolExpr("""NAryLogicOP (OR)\nse il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co3 non è  diverso da  /*56,*/ 123""", [
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_contatore_co3)  è uguale a  (123)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co3)  è uguale a  (123))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co3)  è uguale a  (123)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M1"""),#1
                    ]),#3
                     )
        add_instance_deb_info(self.station_name, self.name, self.instance_name, CdLDebInfo([
            # transizioni iniziali
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.StatoIniziale, Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1,
                         guard=(self.dbs[0], ),
                         effect=(),
                         phase = TransPhase.Stato
                         ),
            # transizioni della fase manuale
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1,Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1,
                         guard=(self.dbs[1], ),
                         effect=(self.dbs[2], self.dbs[3], ),
                         phase = TransPhase.Manuale
                         ),
            # transizioni della fase di stato
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
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1)
            self.effect_INITIALIZATION_StatoIniziale_state1_000()
            self.response_wait()

        self.set_mainclass_c1_previousco_c10_prev(GlobalEnumeration.c180x)
        self.set_mainclass_c1_previousco_c4_prev(False)
        self.set_mainclass_c1_previousco_c5_prev(True)
        self.set_mainclass_c1_previousco_c6_prev(False)
        self.set_mainclass_c1_previousva_pv1_prev(self.get_mainclass_c1_previousva_pv1())
        self.set_mainclass_c1_previousva_pv2_prev(self.get_mainclass_c1_previousva_pv2())
        self.set_mainclass_c1_previousva_pv3_prev(self.get_mainclass_c1_previousva_pv3())

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
            if self.is_current_state(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1):
                if(self.guard_PERMANENCE_state1_000()):
                    self.curr_transition = self.Transition._State1__State1__stateSheet_0__permanence
            else:
                # if the current state variable is not set, an exception will be raised
                return ERROR("the current state variable is not set (command: %s)" % command)

        if self.is_state_phase():
            if self.is_current_state(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1):
                pass #return ERROR("the current state variable is not set (command: %s)" % command)
            else:
                # if the current state variable is not set, an exception will be raised
                return ERROR("the current state variable is not set (command: %s)" % command)

        if self.is_automatic_phase():
            if self.is_current_state(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1):
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
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1)
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
        
         commento: {81,}  Ricezione del  comando manuale   MainClass_C1_command_comm10 da  Senderac49796   commento: {76,}
         commento: {67,} commento: {37,}  se la variabile MainClass_C1_variabile_V1 è  diverso da RossoGialloxVerdex e  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} o  se la variabile MainClass_C1_variabile_V3 è  uguale a RossoGialloxVerdex commento: {35,} o  se il controllo MainClass_C1_controllo_C1 è  diverso da  True  e  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} o  se il controllo MainClass_C1_controllo_C9 è  diverso da RossoGialloxVerdex, Tutte le seguenti { 
         commento: {69,} commento: {37,}  se la variabile MainClass_C1_variabile_V9 è  uguale a c180x commento: {37,} e  se la variabile MainClass_C1_variabile_V9 non è  uguale a c180x o  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} o  se il parametro MainClass_C1_parametro_P3 non è  uguale a  commento: {53,} 2 commento: {34,} o  se il parametro MainClass_C1_parametro_P8 è  uguale a  commento: {53,} 8 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
         commento: {38,}  se il contatore MainClass_C1_contatore_Co3 è  minore di  commento: {55,} 13 e  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} o  se il contatore MainClass_C1_contatore_Co3 non è  diverso da  commento: {56,} 14 commento: {36,} o  se il timer MainClass_C1_timer_T2 non è scaduto, Verifica che   commento: {49,}  commento: {,}  il timer MainClass_C1_timer_T5 sia scaduto
        
        
         } Verifica che   commento: {51,}  commento: {,}  il contatore MainClass_C1_contatore_Co3 sia  minore di  commento: {55,} 12
        
        
         } Verifica che   commento: {47,}  commento: {34,}  il parametro MainClass_C1_parametro_P6 sia  diverso da  False 
        
        
        
        }
        """
        res_manCmdCondition_0 = (db(self.is_triggered('eventMainclass_c1_command_comm10DaSenderac49796'), self.dbs[1].subs[0]) and db(not db((db((db((db((db(not db(self.get_mainclass_c1_variabile_v1() == GlobalEnumeration.rossogialloxverdex, self.dbs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, self.dbs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[1].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_variabile_v3() == GlobalEnumeration.rossogialloxverdex, self.dbs[1].subs[1].subs[0].subs[0].subs[0].subs[1])), self.dbs[1].subs[1].subs[0].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_controllo_c1() == True, self.dbs[1].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[1].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, self.dbs[1].subs[1].subs[0].subs[0].subs[1].subs[1])), self.dbs[1].subs[1].subs[0].subs[0].subs[1])), self.dbs[1].subs[1].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_controllo_c9() == GlobalEnumeration.rossogialloxverdex, self.dbs[1].subs[1].subs[0].subs[1].subs[0]), self.dbs[1].subs[1].subs[0].subs[1])), self.dbs[1].subs[1].subs[0]) or db((db(not db((db((db((db((db(self.get_mainclass_c1_variabile_v9() == GlobalEnumeration.c180x, self.dbs[1].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v9() == GlobalEnumeration.c180x, self.dbs[1].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[1].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[1].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, self.dbs[1].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[1].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_parametro_p3() == 2, self.dbs[1].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[1].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1])), self.dbs[1].subs[1].subs[1].subs[0].subs[0].subs[0]) or db((db(self.get_mainclass_c1_parametro_p8() == 8, self.dbs[1].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, self.dbs[1].subs[1].subs[1].subs[0].subs[0].subs[1].subs[1])), self.dbs[1].subs[1].subs[1].subs[0].subs[0].subs[1])), self.dbs[1].subs[1].subs[1].subs[0].subs[0]) or db(not db((db((db((db(self.get_mainclass_c1_contatore_co3().get_valore() < 13, self.dbs[1].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, self.dbs[1].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), self.dbs[1].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_contatore_co3().get_valore() == 14, self.dbs[1].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[1].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), self.dbs[1].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[1].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_timer_t2().isScaduto(), self.dbs[1].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]), self.dbs[1].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1])), self.dbs[1].subs[1].subs[1].subs[0].subs[1].subs[0]) or db(self.get_mainclass_c1_timer_t5().isScaduto(), self.dbs[1].subs[1].subs[1].subs[0].subs[1].subs[1]), self.dbs[1].subs[1].subs[1].subs[0].subs[1]), self.dbs[1].subs[1].subs[1].subs[0]) and db(self.get_mainclass_c1_contatore_co3().get_valore() < 12, self.dbs[1].subs[1].subs[1].subs[1])), self.dbs[1].subs[1].subs[1]), self.dbs[1].subs[1]) and db(not db(self.get_mainclass_c1_parametro_p6() == False, self.dbs[1].subs[2].subs[0]), self.dbs[1].subs[2]))
        if res_manCmdCondition_0:
            self.set_man_cmd_response('eventMainclass_c1_command_comm10DaSenderac49796',self.ManCmdResponse.PROCESSED)
        return db(res_manCmdCondition_0, self.dbs[1])
    
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
        
          se il ripristino dello stato  non è  uguale a  commento: {53,}  state1  commento: {107,} commento: {37,} e  se la variabile MainClass_C1_variabile_V10 è  diverso da  commento: {56,} 1 commento: {37,} o  se la variabile MainClass_C1_variabile_V1 non è  uguale a RossoGialloxVerdex commento: {35,} e  se il controllo MainClass_C1_controllo_C2 è  uguale a  True , commento: {68,}Attiva il timer MainClass_C1_timer_T2
        
         ,altrimenti  commento: {66,} Assegna al comando MainClass_C1_comando_C2 il valore  False 
        
        
          se il controllo ConsDef  è  uguale a FALSE  commento: {38,} o  se il contatore MainClass_C1_contatore_Co3 non è  diverso da  commento: {56,} 123,  Applica gli effetti
               della macro MainClass_C1_macroef_M1  commento: {73,}
        
           
        
        }
        """
        #  se il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*37,*/ e  se la variabile MainClass_C1_variabile_V10 è  diverso da  /*56,*/ 1 /*37,*/ o  se la variabile MainClass_C1_variabile_V1 non è  uguale a RossoGialloxVerdex /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  uguale a  True , /*68,*/Attiva il timer MainClass_C1_timer_T2
        #   ,altrimenti  /*66,*/ Assegna al comando MainClass_C1_comando_C2 il valore  False
        if db((db((db(not db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, self.dbs[2].subs[0].subs[0].subs[0].subs[0]), self.dbs[2].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v10() == 1, self.dbs[2].subs[0].subs[0].subs[1].subs[0]), self.dbs[2].subs[0].subs[0].subs[1])), self.dbs[2].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_variabile_v1() == GlobalEnumeration.rossogialloxverdex, self.dbs[2].subs[0].subs[1].subs[0].subs[0]), self.dbs[2].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_controllo_c2() == True, self.dbs[2].subs[0].subs[1].subs[1])), self.dbs[2].subs[0].subs[1])), self.dbs[2].subs[0]):
            self.get_mainclass_c1_timer_t2().attiva()
        else:
            self.set_mainclass_c1_comando_c2(False)
        #  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co3 non è  diverso da  /*56,*/ 123,  Applica gli effetti
        #         della macro MainClass_C1_macroef_M1
        if db((db(self.get_consdef() == False, self.dbs[3].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_contatore_co3().get_valore() == 123, self.dbs[3].subs[0].subs[1].subs[0].subs[0]), self.dbs[3].subs[0].subs[1].subs[0]), self.dbs[3].subs[0].subs[1])), self.dbs[3].subs[0]):
            self.macroMainclass_c1_macroef_m1(self.dbs[3].subs[1])
    
    # effect macros
    def macroMainclass_c1_macroef_m1(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        {  se la macro  MainClass_C1_macrova_M5 ( con argomento_a1   uguale a True  e argomento_a8   uguale a RossoVerde )   è  diverso da RossoGialloxVerdex commento: {40,}  commento: {37,} e  se la variabile MainClass_C1_variabile_V1 è  diverso da RossoGialloxVerdex commento: {38,} e  se il contatore MainClass_C1_contatore_Co3 non è  minore di  commento: {55,} 15240, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V1 il valore RossoGialloxVerdex
        
         ,altrimenti  commento: {70,}Incrementa il contatore MainClass_C1_contatore_Co3
        
        
          se il controllo ConsDef  è  uguale a FALSE  commento: {37,} o  se la variabile MainClass_C1_variabile_V1 non è  diverso da RossoGialloxVerdex e  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} o  se il parametro MainClass_C1_parametro_P3 non è  minore di  commento: {55,} 4 commento: {35,} e  se il controllo MainClass_C1_controllo_C9 è  uguale a RossoGialloxVerdex o  se il controllo ConsDef  è  uguale a FALSE , commento: {66,} Assegna al comando MainClass_C1_comando_C3 il valore RossoGiallox
        
         ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V1 il valore RossoGialloxVerdex
        
        
         commento: {38,}  se il contatore MainClass_C1_contatore_Co3 è  minore di  commento: {55,} 11, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V9 il valore c180x
        
         ,altrimenti  commento: {69,}Disattiva il timer MainClass_C1_timer_T2
        
        
         commento: {37,}  se la variabile MainClass_C1_variabile_V9 non è  diverso da c180x o  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} e  se la variabile MainClass_C1_variabile_V9 è  uguale a c180x, commento: {66,} Assegna al comando MainClass_C1_comando_C7 il valore RossoGiallox
        
           
        
        }
        """
        def populate_macroMainclass_c1_macroef_m1_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITEStatementImpl\nse la macro  MainClass_C1_macrova_M5 ( con argomento_a1   uguale a True  e argomento_a8   uguale a RossoVerde )   è  diverso da RossoGialloxVerdex /*40,*/  /*37,*/ e  se la variabile MainClass_C1_variabile_V1 è  diverso da RossoGialloxVerdex /*38,*/ e  se il contatore MainClass_C1_contatore_Co3 non è  minore di  /*55,*/ 15240, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V1 il valore RossoGialloxVerdex

 ,altrimenti  /*70,*/Incrementa il contatore MainClass_C1_contatore_Co3""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse la macro  MainClass_C1_macrova_M5 ( con argomento_a1   uguale a True  e argomento_a8   uguale a RossoVerde )   è  diverso da RossoGialloxVerdex /*40,*/  /*37,*/ e  se la variabile MainClass_C1_variabile_V1 è  diverso da RossoGialloxVerdex /*38,*/ e  se il contatore MainClass_C1_contatore_Co3 non è  minore di  /*55,*/ 15240""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m5')  è uguale a  (rossogialloxverdex)) )  e  ( negazione di ((mainclass_c1_variabile_v1)  è uguale a  (rossogialloxverdex)) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m5')  è uguale a  (rossogialloxverdex))""", [
                            DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m5')  è uguale a  (rossogialloxverdex)""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroMainclass_c1_macrova_m5'"""),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v1)  è uguale a  (rossogialloxverdex))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v1)  è uguale a  (rossogialloxverdex)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co3)  è minore di  (15240))""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co3)  è minore di  (15240)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITEStatementImpl\nse il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile MainClass_C1_variabile_V1 non è  diverso da RossoGialloxVerdex e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  minore di  /*55,*/ 4 /*35,*/ e  se il controllo MainClass_C1_controllo_C9 è  uguale a RossoGialloxVerdex o  se il controllo ConsDef  è  uguale a FALSE , /*66,*/ Assegna al comando MainClass_C1_comando_C3 il valore RossoGiallox

 ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V1 il valore RossoGialloxVerdex""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile MainClass_C1_variabile_V1 non è  diverso da RossoGialloxVerdex e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  minore di  /*55,*/ 4 /*35,*/ e  se il controllo MainClass_C1_controllo_C9 è  uguale a RossoGialloxVerdex o  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( (consdef)  è uguale a  (False) )  o  
( ( negazione di (negazione di ((mainclass_c1_variabile_v1)  è uguale a  (rossogialloxverdex))) )  e  
( (consdef)  è uguale a  (False) ) ) )  o  
( ( negazione di ((mainclass_c1_parametro_p3)  è minore di  (4)) )  e  
( (mainclass_c1_controllo_c9)  è uguale a  (rossogialloxverdex) ) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( (consdef)  è uguale a  (False) )  o  
( ( negazione di (negazione di ((mainclass_c1_variabile_v1)  è uguale a  (rossogialloxverdex))) )  e  
( (consdef)  è uguale a  (False) ) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (negazione di ((mainclass_c1_variabile_v1)  è uguale a  (rossogialloxverdex))) )  e  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_variabile_v1)  è uguale a  (rossogialloxverdex)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v1)  è uguale a  (rossogialloxverdex))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v1)  è uguale a  (rossogialloxverdex)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_parametro_p3)  è minore di  (4)) )  e  
( (mainclass_c1_controllo_c9)  è uguale a  (rossogialloxverdex) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p3)  è minore di  (4))""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_parametro_p3)  è minore di  (4)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c9)  è uguale a  (rossogialloxverdex)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            ]),#1
                            DIStatement("""ITEStatementImpl\n/*38,*/  se il contatore MainClass_C1_contatore_Co3 è  minore di  /*55,*/ 11, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V9 il valore c180x

 ,altrimenti  /*69,*/Disattiva il timer MainClass_C1_timer_T2""", [
                            DIBoolExpr("""LessThanImpl\nil contatore MainClass_C1_contatore_Co3 è  minore di  /*55,*/ 11""", [
                            ]),#0
                            ]),#2
                            DIStatement("""ITStatement\n/*37,*/  se la variabile MainClass_C1_variabile_V9 non è  diverso da c180x o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V9 è  uguale a c180x, /*66,*/ Assegna al comando MainClass_C1_comando_C7 il valore RossoGiallox""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*37,*/  se la variabile MainClass_C1_variabile_V9 non è  diverso da c180x o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V9 è  uguale a c180x""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_variabile_v9)  è uguale a  (c180x)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v9)  è uguale a  (c180x))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v9)  è uguale a  (c180x)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  
( (mainclass_c1_variabile_v9)  è uguale a  (c180x) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v9)  è uguale a  (c180x)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#3
                ])

        populate_macroMainclass_c1_macroef_m1_SrfMacroDefInfo(di_ctx)
        #  se la macro  MainClass_C1_macrova_M5 ( con argomento_a1   uguale a True  e argomento_a8   uguale a RossoVerde )   è  diverso da RossoGialloxVerdex /*40,*/  /*37,*/ e  se la variabile MainClass_C1_variabile_V1 è  diverso da RossoGialloxVerdex /*38,*/ e  se il contatore MainClass_C1_contatore_Co3 non è  minore di  /*55,*/ 15240, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V1 il valore RossoGialloxVerdex
        #   ,altrimenti  /*70,*/Incrementa il contatore MainClass_C1_contatore_Co3
        if db((db((db(not db(db(self.macroMainclass_c1_macrova_m5(True,GlobalEnumeration.rossoverde, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) == GlobalEnumeration.rossogialloxverdex, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v1() == GlobalEnumeration.rossogialloxverdex, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co3().get_valore() < 15240, di_ctx.subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.set_mainclass_c1_variabile_v1(GlobalEnumeration.rossogialloxverdex)
        else:
            self.get_mainclass_c1_contatore_co3().incrementa()
        #  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile MainClass_C1_variabile_V1 non è  diverso da RossoGialloxVerdex e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  minore di  /*55,*/ 4 /*35,*/ e  se il controllo MainClass_C1_controllo_C9 è  uguale a RossoGialloxVerdex o  se il controllo ConsDef  è  uguale a FALSE , /*66,*/ Assegna al comando MainClass_C1_comando_C3 il valore RossoGiallox
        #   ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V1 il valore RossoGialloxVerdex
        if db((db((db((db(self.get_consdef() == False, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0]) or db((db(not db(not db(self.get_mainclass_c1_variabile_v1() == GlobalEnumeration.rossogialloxverdex, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_parametro_p3() < 4, di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_controllo_c9() == GlobalEnumeration.rossogialloxverdex, di_ctx.subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.set_mainclass_c1_comando_c3(GlobalEnumeration.rossogiallox)
        else:
            self.set_mainclass_c1_variabile_v1(GlobalEnumeration.rossogialloxverdex)
        #  /*38,*/  se il contatore MainClass_C1_contatore_Co3 è  minore di  /*55,*/ 11, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V9 il valore c180x
        #   ,altrimenti  /*69,*/Disattiva il timer MainClass_C1_timer_T2
        if db(self.get_mainclass_c1_contatore_co3().get_valore() < 11, di_ctx.subs[2].subs[0]):
            self.set_mainclass_c1_variabile_v9(GlobalEnumeration.c180x)
        else:
            self.get_mainclass_c1_timer_t2().disattiva()
        #  /*37,*/  se la variabile MainClass_C1_variabile_V9 non è  diverso da c180x o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V9 è  uguale a c180x, /*66,*/ Assegna al comando MainClass_C1_comando_C7 il valore RossoGiallox
        if db((db(not db(not db(self.get_mainclass_c1_variabile_v9() == GlobalEnumeration.c180x, di_ctx.subs[3].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[3].subs[0].subs[0].subs[0]), di_ctx.subs[3].subs[0].subs[0]) or db((db(self.get_consdef() == False, di_ctx.subs[3].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_variabile_v9() == GlobalEnumeration.c180x, di_ctx.subs[3].subs[0].subs[1].subs[1])), di_ctx.subs[3].subs[0].subs[1])), di_ctx.subs[3].subs[0]):
            self.set_mainclass_c1_comando_c7(GlobalEnumeration.rossogiallox)
    
    def macroMainclass_c1_macroef_m2(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        {  se la macro  MainClass_C1_macrova_M7 ( con argomento_a4   uguale a True ,argomento_a7   uguale a RossoVerde ,argomento_a2   uguale a c180x  e argomento_a6   uguale a c270xx )   è  uguale a RossoGiallox commento: {40,}  commento: {38,} o  se il contatore MainClass_C1_contatore_Co3 non è  diverso da  commento: {56,} 13152 commento: {36,} o  se il timer MainClass_C1_timer_T2 non è disattivo commento: {35,} o  se il controllo MainClass_C1_controllo_C2 è  uguale a  True  commento: {36,} o  se il timer MainClass_C1_timer_T5 è scaduto commento: {35,} o  se il controllo MainClass_C1_controllo_C9 non è  uguale a RossoGialloxVerdex, commento: {68,}Attiva il timer MainClass_C1_timer_T5
        
         ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V1 il valore RossoGialloxVerdex
        
        
         commento: {35,}  se il controllo MainClass_C1_controllo_C9 è  diverso da RossoGialloxVerdex commento: {35,} o  se il controllo MainClass_C1_controllo_C2 è  diverso da  True ,  Applica gli effetti
               della macro MainClass_C1_macroef_M1  commento: {73,}
        
         ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V1 il valore RossoGialloxVerdex
        
        
         commento: {34,}  se lo stato  non è  diverso da  commento: {56,}  state1  commento: {106,} commento: {37,} o  se la variabile MainClass_C1_variabile_V1 è  uguale a RossoGialloxVerdex commento: {34,} e  se il parametro MainClass_C1_parametro_P3 non è  diverso da  commento: {56,} 8 commento: {34,} e  se il parametro MainClass_C1_parametro_P3 è  minore di  commento: {55,} 5, commento: {68,}Attiva il timer MainClass_C1_timer_T5
        
           
          se il controllo ConsDef è uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE , commento: {70,}Incrementa il contatore MainClass_C1_contatore_Co3
        
           
         commento: {34,}  se il parametro MainClass_C1_parametro_P8 non è  minore di  commento: {55,} 4 commento: {34,} e  se il parametro MainClass_C1_parametro_P10 è  diverso da  commento: {56,} 10 e  se il controllo ConsDef  è  uguale a FALSE , commento: {67,} Assegna alla variabile MainClass_C1_variabile_V1 il valore RossoGialloxVerdex
        
           
        
        }
        """
        def populate_macroMainclass_c1_macroef_m2_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITEStatementImpl\nse la macro  MainClass_C1_macrova_M7 ( con argomento_a4   uguale a True ,argomento_a7   uguale a RossoVerde ,argomento_a2   uguale a c180x  e argomento_a6   uguale a c270xx )   è  uguale a RossoGiallox /*40,*/  /*38,*/ o  se il contatore MainClass_C1_contatore_Co3 non è  diverso da  /*56,*/ 13152 /*36,*/ o  se il timer MainClass_C1_timer_T2 non è disattivo /*35,*/ o  se il controllo MainClass_C1_controllo_C2 è  uguale a  True  /*36,*/ o  se il timer MainClass_C1_timer_T5 è scaduto /*35,*/ o  se il controllo MainClass_C1_controllo_C9 non è  uguale a RossoGialloxVerdex, /*68,*/Attiva il timer MainClass_C1_timer_T5

 ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V1 il valore RossoGialloxVerdex""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse la macro  MainClass_C1_macrova_M7 ( con argomento_a4   uguale a True ,argomento_a7   uguale a RossoVerde ,argomento_a2   uguale a c180x  e argomento_a6   uguale a c270xx )   è  uguale a RossoGiallox /*40,*/  /*38,*/ o  se il contatore MainClass_C1_contatore_Co3 non è  diverso da  /*56,*/ 13152 /*36,*/ o  se il timer MainClass_C1_timer_T2 non è disattivo /*35,*/ o  se il controllo MainClass_C1_controllo_C2 è  uguale a  True  /*36,*/ o  se il timer MainClass_C1_timer_T5 è scaduto /*35,*/ o  se il controllo MainClass_C1_controllo_C9 non è  uguale a RossoGialloxVerdex""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( ( ( (chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m7')  è uguale a  (rossogiallox) )  o  
( negazione di (negazione di ((mainclass_c1_contatore_co3)  è uguale a  (13152))) ) )  o  
( negazione di (il timer 'mainclass_c1_timer_t2' è inattivo) ) )  o  
( (mainclass_c1_controllo_c2)  è uguale a  (True) ) )  o  
( il timer 'mainclass_c1_timer_t5' è scaduto )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( ( (chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m7')  è uguale a  (rossogiallox) )  o  
( negazione di (negazione di ((mainclass_c1_contatore_co3)  è uguale a  (13152))) ) )  o  
( negazione di (il timer 'mainclass_c1_timer_t2' è inattivo) ) )  o  
( (mainclass_c1_controllo_c2)  è uguale a  (True) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( (chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m7')  è uguale a  (rossogiallox) )  o  
( negazione di (negazione di ((mainclass_c1_contatore_co3)  è uguale a  (13152))) ) )  o  
( negazione di (il timer 'mainclass_c1_timer_t2' è inattivo) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( (chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m7')  è uguale a  (rossogiallox) )  o  
( negazione di (negazione di ((mainclass_c1_contatore_co3)  è uguale a  (13152))) )""", [
                            DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m7')  è uguale a  (rossogiallox)""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroMainclass_c1_macrova_m7'"""),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_contatore_co3)  è uguale a  (13152)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co3)  è uguale a  (13152))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co3)  è uguale a  (13152)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t2' è inattivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t2' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c2)  è uguale a  (True)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t5' è scaduto""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c9)  è uguale a  (rossogialloxverdex))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c9)  è uguale a  (rossogialloxverdex)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITEStatementImpl\n/*35,*/  se il controllo MainClass_C1_controllo_C9 è  diverso da RossoGialloxVerdex /*35,*/ o  se il controllo MainClass_C1_controllo_C2 è  diverso da  True ,  Applica gli effetti
       della macro MainClass_C1_macroef_M1  /*73,*/

 ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V1 il valore RossoGialloxVerdex""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*35,*/  se il controllo MainClass_C1_controllo_C9 è  diverso da RossoGialloxVerdex /*35,*/ o  se il controllo MainClass_C1_controllo_C2 è  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c9)  è uguale a  (rossogialloxverdex))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c9)  è uguale a  (rossogialloxverdex)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c2)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c2)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M1"""),#1
                            ]),#1
                            DIStatement("""ITStatement\n/*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*37,*/ o  se la variabile MainClass_C1_variabile_V1 è  uguale a RossoGialloxVerdex /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  diverso da  /*56,*/ 8 /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  minore di  /*55,*/ 5, /*68,*/Attiva il timer MainClass_C1_timer_T5""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*37,*/ o  se la variabile MainClass_C1_variabile_V1 è  uguale a RossoGialloxVerdex /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  diverso da  /*56,*/ 8 /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  minore di  /*55,*/ 5""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((lo stato di 'self')  è uguale a  (state1)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lo stato di 'self')  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( (mainclass_c1_variabile_v1)  è uguale a  (rossogialloxverdex) )  e  ( negazione di (negazione di ((mainclass_c1_parametro_p3)  è uguale a  (8))) ) )  e  
( (mainclass_c1_parametro_p3)  è minore di  (5) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (mainclass_c1_variabile_v1)  è uguale a  (rossogialloxverdex) )  e  ( negazione di (negazione di ((mainclass_c1_parametro_p3)  è uguale a  (8))) )""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v1)  è uguale a  (rossogialloxverdex)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_parametro_p3)  è uguale a  (8)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p3)  è uguale a  (8))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3)  è uguale a  (8)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_parametro_p3)  è minore di  (5)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#2
                            DIStatement("""ITStatement\nse il controllo ConsDef è uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE , /*70,*/Incrementa il contatore MainClass_C1_contatore_Co3""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse il controllo ConsDef è uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            ]),#3
                            DIStatement("""ITStatement\n/*34,*/  se il parametro MainClass_C1_parametro_P8 non è  minore di  /*55,*/ 4 /*34,*/ e  se il parametro MainClass_C1_parametro_P10 è  diverso da  /*56,*/ 10 e  se il controllo ConsDef  è  uguale a FALSE , /*67,*/ Assegna alla variabile MainClass_C1_variabile_V1 il valore RossoGialloxVerdex""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*34,*/  se il parametro MainClass_C1_parametro_P8 non è  minore di  /*55,*/ 4 /*34,*/ e  se il parametro MainClass_C1_parametro_P10 è  diverso da  /*56,*/ 10 e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_parametro_p8)  è minore di  (4)) )  e  ( negazione di ((mainclass_c1_parametro_p10)  è uguale a  (10)) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p8)  è minore di  (4))""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_parametro_p8)  è minore di  (4)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p10)  è uguale a  (10))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p10)  è uguale a  (10)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            ]),#4
                ])

        populate_macroMainclass_c1_macroef_m2_SrfMacroDefInfo(di_ctx)
        #  se la macro  MainClass_C1_macrova_M7 ( con argomento_a4   uguale a True ,argomento_a7   uguale a RossoVerde ,argomento_a2   uguale a c180x  e argomento_a6   uguale a c270xx )   è  uguale a RossoGiallox /*40,*/  /*38,*/ o  se il contatore MainClass_C1_contatore_Co3 non è  diverso da  /*56,*/ 13152 /*36,*/ o  se il timer MainClass_C1_timer_T2 non è disattivo /*35,*/ o  se il controllo MainClass_C1_controllo_C2 è  uguale a  True  /*36,*/ o  se il timer MainClass_C1_timer_T5 è scaduto /*35,*/ o  se il controllo MainClass_C1_controllo_C9 non è  uguale a RossoGialloxVerdex, /*68,*/Attiva il timer MainClass_C1_timer_T5
        #   ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V1 il valore RossoGialloxVerdex
        if db((db((db((db((db((db(db(self.macroMainclass_c1_macrova_m7(GlobalEnumeration.c180x,True,GlobalEnumeration.c270xx,GlobalEnumeration.rossoverde, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) == GlobalEnumeration.rossogiallox, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_contatore_co3().get_valore() == 13152, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_timer_t2().isDisattivato(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_controllo_c2() == True, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_timer_t5().isScaduto(), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_controllo_c9() == GlobalEnumeration.rossogialloxverdex, di_ctx.subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.get_mainclass_c1_timer_t5().attiva()
        else:
            self.set_mainclass_c1_variabile_v1(GlobalEnumeration.rossogialloxverdex)
        #  /*35,*/  se il controllo MainClass_C1_controllo_C9 è  diverso da RossoGialloxVerdex /*35,*/ o  se il controllo MainClass_C1_controllo_C2 è  diverso da  True ,  Applica gli effetti
        #         della macro MainClass_C1_macroef_M1  /*73,*/
        #   ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V1 il valore RossoGialloxVerdex
        if db((db(not db(self.get_mainclass_c1_controllo_c9() == GlobalEnumeration.rossogialloxverdex, di_ctx.subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_controllo_c2() == True, di_ctx.subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.macroMainclass_c1_macroef_m1(di_ctx.subs[1].subs[1])
        else:
            self.set_mainclass_c1_variabile_v1(GlobalEnumeration.rossogialloxverdex)
        #  /*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*37,*/ o  se la variabile MainClass_C1_variabile_V1 è  uguale a RossoGialloxVerdex /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  diverso da  /*56,*/ 8 /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  minore di  /*55,*/ 5, /*68,*/Attiva il timer MainClass_C1_timer_T5
        if db((db(not db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[0]) or db((db((db(self.get_mainclass_c1_variabile_v1() == GlobalEnumeration.rossogialloxverdex, di_ctx.subs[2].subs[0].subs[1].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_parametro_p3() == 8, di_ctx.subs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_parametro_p3() < 5, di_ctx.subs[2].subs[0].subs[1].subs[1])), di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.get_mainclass_c1_timer_t5().attiva()
        #  se il controllo ConsDef è uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE , /*70,*/Incrementa il contatore MainClass_C1_contatore_Co3
        if db((db(self.get_consdef() == False, di_ctx.subs[3].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[3].subs[0].subs[1])), di_ctx.subs[3].subs[0]):
            self.get_mainclass_c1_contatore_co3().incrementa()
        #  /*34,*/  se il parametro MainClass_C1_parametro_P8 non è  minore di  /*55,*/ 4 /*34,*/ e  se il parametro MainClass_C1_parametro_P10 è  diverso da  /*56,*/ 10 e  se il controllo ConsDef  è  uguale a FALSE , /*67,*/ Assegna alla variabile MainClass_C1_variabile_V1 il valore RossoGialloxVerdex
        if db((db((db(not db(self.get_mainclass_c1_parametro_p8() < 4, di_ctx.subs[4].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[4].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p10() == 10, di_ctx.subs[4].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[4].subs[0].subs[0].subs[1])), di_ctx.subs[4].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[4].subs[0].subs[1])), di_ctx.subs[4].subs[0]):
            self.set_mainclass_c1_variabile_v1(GlobalEnumeration.rossogialloxverdex)
    
    # verify macros
    @srf_value_macro("macroMainclass_c1_macrove_m4")
    def macroMainclass_c1_macrove_m4(self, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
         
        { commento: {62,} commento: {34,}  se il parametro MainClass_C1_parametro_P3 è  minore di  commento: {55,} 2 commento: {35,} e  se il controllo MainClass_C1_controllo_C9 non è  diverso da RossoGialloxVerdex commento: {34,} e  se il parametro MainClass_C1_parametro_P3 è  maggiore di  commento: {54,} 7 commento: {34,} e  se il parametro MainClass_C1_parametro_P3 è  diverso da  commento: {56,} 6 commento: {34,} o  se il parametro MainClass_C1_parametro_P3 non è  maggiore di  commento: {54,} 5 commento: {34,} o  se il parametro MainClass_C1_parametro_P3 non è  uguale a  commento: {53,} 1, Almeno una delle seguenti { 
         commento: {37,}  se la variabile MainClass_C1_variabile_V10 non è  maggiore di  commento: {54,} 3 e  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   commento: {47,48,49,}  commento: {,}  il controllo MainClass_C1_controllo_C1 sia  uguale a  False 
         commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T5 non sia attivo
         commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P8 non sia  maggiore di  commento: {54,} 10
        
        
         } Verifica che   commento: {47,48,}  commento: {,}  il controllo MainClass_C1_controllo_C9 non sia  uguale a RossoGialloxVerdex
         commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P3 sia  minore di  commento: {55,} 6
         commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
        
        
        }
        """
        def populate_macroMainclass_c1_macrove_m4_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*34,*/  se il parametro MainClass_C1_parametro_P3 è  minore di  /*55,*/ 2 /*35,*/ e  se il controllo MainClass_C1_controllo_C9 non è  diverso da RossoGialloxVerdex /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  maggiore di  /*54,*/ 7 /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da  /*56,*/ 6 /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  maggiore di  /*54,*/ 5 /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  uguale a  /*53,*/ 1, Almeno una delle seguenti { 
 /*37,*/  se la variabile MainClass_C1_variabile_V10 non è  maggiore di  /*54,*/ 3 e  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*47,48,49,*/  /*,*/  il controllo MainClass_C1_controllo_C1 sia  uguale a  False 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 non sia attivo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  maggiore di  /*54,*/ 10


 } Verifica che   /*47,48,*/  /*,*/  il controllo MainClass_C1_controllo_C9 non sia  uguale a RossoGialloxVerdex
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P3 sia  minore di  /*55,*/ 6
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*34,*/  se il parametro MainClass_C1_parametro_P3 è  minore di  /*55,*/ 2 /*35,*/ e  se il controllo MainClass_C1_controllo_C9 non è  diverso da RossoGialloxVerdex /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  maggiore di  /*54,*/ 7 /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da  /*56,*/ 6 /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  maggiore di  /*54,*/ 5 /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  uguale a  /*53,*/ 1, Almeno una delle seguenti { 
 /*37,*/  se la variabile MainClass_C1_variabile_V10 non è  maggiore di  /*54,*/ 3 e  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*47,48,49,*/  /*,*/  il controllo MainClass_C1_controllo_C1 sia  uguale a  False 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 non sia attivo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  maggiore di  /*54,*/ 10


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*34,*/  se il parametro MainClass_C1_parametro_P3 è  minore di  /*55,*/ 2 /*35,*/ e  se il controllo MainClass_C1_controllo_C9 non è  diverso da RossoGialloxVerdex /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  maggiore di  /*54,*/ 7 /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da  /*56,*/ 6 /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  maggiore di  /*54,*/ 5 /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  uguale a  /*53,*/ 1""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*34,*/  se il parametro MainClass_C1_parametro_P3 è  minore di  /*55,*/ 2 /*35,*/ e  se il controllo MainClass_C1_controllo_C9 non è  diverso da RossoGialloxVerdex /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  maggiore di  /*54,*/ 7 /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da  /*56,*/ 6 /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  maggiore di  /*54,*/ 5""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*34,*/  se il parametro MainClass_C1_parametro_P3 è  minore di  /*55,*/ 2 /*35,*/ e  se il controllo MainClass_C1_controllo_C9 non è  diverso da RossoGialloxVerdex /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  maggiore di  /*54,*/ 7 /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da  /*56,*/ 6""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*34,*/  se il parametro MainClass_C1_parametro_P3 è  minore di  /*55,*/ 2 /*35,*/ e  se il controllo MainClass_C1_controllo_C9 non è  diverso da RossoGialloxVerdex /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  maggiore di  /*54,*/ 7""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*34,*/  se il parametro MainClass_C1_parametro_P3 è  minore di  /*55,*/ 2 /*35,*/ e  se il controllo MainClass_C1_controllo_C9 non è  diverso da RossoGialloxVerdex""", [
                            DIBoolExpr("""LessThanImpl\nil parametro MainClass_C1_parametro_P3 è  minore di  /*55,*/ 2""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C9 non è  diverso da RossoGialloxVerdex""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c9)  è uguale a  (rossogialloxverdex))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c9)  è uguale a  (rossogialloxverdex)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nil parametro MainClass_C1_parametro_P3 è  maggiore di  /*54,*/ 7""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P3 è  diverso da  /*56,*/ 6""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3)  è uguale a  (6)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P3 non è  maggiore di  /*54,*/ 5""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_parametro_p3)  è maggiore di  (5)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P3 non è  uguale a  /*53,*/ 1""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3)  è uguale a  (1)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*37,*/  se la variabile MainClass_C1_variabile_V10 non è  maggiore di  /*54,*/ 3 e  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*47,48,49,*/  /*,*/  il controllo MainClass_C1_controllo_C1 sia  uguale a  False 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 non sia attivo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  maggiore di  /*54,*/ 10""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*37,*/  se la variabile MainClass_C1_variabile_V10 non è  maggiore di  /*54,*/ 3 e  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*37,*/  se la variabile MainClass_C1_variabile_V10 non è  maggiore di  /*54,*/ 3 e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V10 non è  maggiore di  /*54,*/ 3""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_variabile_v10)  è maggiore di  (3)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,*/  /*,*/  il controllo MainClass_C1_controllo_C1 sia  uguale a  False 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 non sia attivo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  maggiore di  /*54,*/ 10""", [
                            DIBoolExpr("""EqualImpl\nche   /*47,48,49,*/  /*,*/  il controllo MainClass_C1_controllo_C1 sia  uguale a  False""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il timer MainClass_C1_timer_T5 non sia attivo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  maggiore di  /*54,*/ 10""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il timer MainClass_C1_timer_T5 non sia attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t5' è attivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  maggiore di  /*54,*/ 10""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_parametro_p8)  è maggiore di  (10)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,*/  /*,*/  il controllo MainClass_C1_controllo_C9 non sia  uguale a RossoGialloxVerdex
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P3 sia  minore di  /*55,*/ 6
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,*/  /*,*/  il controllo MainClass_C1_controllo_C9 non sia  uguale a RossoGialloxVerdex""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c9)  è uguale a  (rossogialloxverdex)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*34,*/  il parametro MainClass_C1_parametro_P3 sia  minore di  /*55,*/ 6
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""LessThanImpl\nche  /*34,*/  il parametro MainClass_C1_parametro_P3 sia  minore di  /*55,*/ 6""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroMainclass_c1_macrove_m4_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db((db((db((db(self.get_mainclass_c1_parametro_p3() < 2, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_controllo_c9() == GlobalEnumeration.rossogialloxverdex, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_parametro_p3() > 7, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p3() == 6, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_parametro_p3() > 5, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_parametro_p3() == 1, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(not db((db((db(not db(self.get_mainclass_c1_variabile_v10() > 3, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0]) or db((db(self.get_mainclass_c1_controllo_c1() == False, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) or db((db(not db(self.get_mainclass_c1_timer_t5().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p8() > 10, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db(not db(self.get_mainclass_c1_controllo_c9() == GlobalEnumeration.rossogialloxverdex, di_ctx.subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0]) or db((db(self.get_mainclass_c1_parametro_p3() < 6, di_ctx.subs[0].subs[1].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    # value macros
    @srf_value_macro("macroMainclass_c1_macrova_m5")
    def macroMainclass_c1_macrova_m5(self, argomento_a1, argomento_a8, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[} commento: {36,}  se il timer MainClass_C1_timer_T2 non è scaduto , assegna alla macro il valore RossoGialloxVerdex
        
         commento: {46,} assegna alla macro il valore RossoGialloxVerdex commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m5_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/ /*36,*/  se il timer MainClass_C1_timer_T2 non è scaduto , assegna alla macro il valore RossoGialloxVerdex""", [
                            DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T2 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t2' è scaduto""", [
                            ]),#0
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macrova_m5_SrfMacroDefInfo(di_ctx)
        #  /*[*/ /*36,*/  se il timer MainClass_C1_timer_T2 non è scaduto , assegna alla macro il valore RossoGialloxVerdex
        if db(not db(self.get_mainclass_c1_timer_t2().isScaduto(), di_ctx.subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0]):
            return GlobalEnumeration.rossogialloxverdex
        #  /*46,*/ assegna alla macro il valore RossoGialloxVerdex
        return GlobalEnumeration.rossogialloxverdex
    
    @srf_value_macro("macroMainclass_c1_macrova_m6")
    def macroMainclass_c1_macrova_m6(self, argomento_a2, argomento_a3, argomento_a4, argomento_a6, argomento_a7, argomento_a9, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}
         commento: {46,} assegna alla macro il valore c180x commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m6_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                ])

        populate_macroMainclass_c1_macrova_m6_SrfMacroDefInfo(di_ctx)
        
        #  /*[*/
        #   /*46,*/ assegna alla macro il valore c180x
        return GlobalEnumeration.c180x
    
    @srf_value_macro("macroMainclass_c1_macrova_m7")
    def macroMainclass_c1_macrova_m7(self, argomento_a2, argomento_a4, argomento_a6, argomento_a7, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}
         commento: {46,} assegna alla macro il valore RossoGiallox commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m7_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                ])

        populate_macroMainclass_c1_macrova_m7_SrfMacroDefInfo(di_ctx)
        
        #  /*[*/
        #   /*46,*/ assegna alla macro il valore RossoGiallox
        return GlobalEnumeration.rossogiallox
    
    @srf_value_macro("macroMainclass_c1_macrova_m8")
    def macroMainclass_c1_macrova_m8(self, argomento_a10, argomento_a5, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[} commento: {35,}  se il controllo MainClass_C1_controllo_C9 è  uguale a RossoGialloxVerdex commento: {36,} e  se il timer MainClass_C1_timer_T2 è scaduto e  se la macro  MainClass_C1_macrova_M6 ( con argomento_a4   uguale a RossoGialloaVerdea ,argomento_a7   uguale a RossoGiallox ,argomento_a2   uguale a RossoGiallox ,argomento_a6   uguale a RossoGialloaVerdea ,argomento_a3   uguale a RossoVerde  e argomento_a9   uguale a RossoGialloaVerdea )   è  uguale a c180x commento: {40,}  commento: {34,} e  se lo stato  non è  uguale a  commento: {53,}  state1  commento: {106,} , assegna alla macro il valore  False 
        
         commento: {46,} assegna alla macro il valore  False  commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m8_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/ /*35,*/  se il controllo MainClass_C1_controllo_C9 è  uguale a RossoGialloxVerdex /*36,*/ e  se il timer MainClass_C1_timer_T2 è scaduto e  se la macro  MainClass_C1_macrova_M6 ( con argomento_a4   uguale a RossoGialloaVerdea ,argomento_a7   uguale a RossoGiallox ,argomento_a2   uguale a RossoGiallox ,argomento_a6   uguale a RossoGialloaVerdea ,argomento_a3   uguale a RossoVerde  e argomento_a9   uguale a RossoGialloaVerdea )   è  uguale a c180x /*40,*/  /*34,*/ e  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ , assegna alla macro il valore  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*[*/ /*35,*/  se il controllo MainClass_C1_controllo_C9 è  uguale a RossoGialloxVerdex /*36,*/ e  se il timer MainClass_C1_timer_T2 è scaduto e  se la macro  MainClass_C1_macrova_M6 ( con argomento_a4   uguale a RossoGialloaVerdea ,argomento_a7   uguale a RossoGiallox ,argomento_a2   uguale a RossoGiallox ,argomento_a6   uguale a RossoGialloaVerdea ,argomento_a3   uguale a RossoVerde  e argomento_a9   uguale a RossoGialloaVerdea )   è  uguale a c180x /*40,*/  /*34,*/ e  se lo stato  non è  uguale a  /*53,*/  state1""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( (mainclass_c1_controllo_c9)  è uguale a  (rossogialloxverdex) )  e  ( il timer 'mainclass_c1_timer_t2' è scaduto ) )  e  ( (chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m6')  è uguale a  (c180x) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (mainclass_c1_controllo_c9)  è uguale a  (rossogialloxverdex) )  e  ( il timer 'mainclass_c1_timer_t2' è scaduto )""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c9)  è uguale a  (rossogialloxverdex)""", [
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t2' è scaduto""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m6')  è uguale a  (c180x)""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroMainclass_c1_macrova_m6'"""),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lo stato di 'self')  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macrova_m8_SrfMacroDefInfo(di_ctx)
        #  /*[*/ /*35,*/  se il controllo MainClass_C1_controllo_C9 è  uguale a RossoGialloxVerdex /*36,*/ e  se il timer MainClass_C1_timer_T2 è scaduto e  se la macro  MainClass_C1_macrova_M6 ( con argomento_a4   uguale a RossoGialloaVerdea ,argomento_a7   uguale a RossoGiallox ,argomento_a2   uguale a RossoGiallox ,argomento_a6   uguale a RossoGialloaVerdea ,argomento_a3   uguale a RossoVerde  e argomento_a9   uguale a RossoGialloaVerdea )   è  uguale a c180x /*40,*/  /*34,*/ e  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ , assegna alla macro il valore  False
        if db((db((db((db(self.get_mainclass_c1_controllo_c9() == GlobalEnumeration.rossogialloxverdex, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_timer_t2().isScaduto(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(db(self.macroMainclass_c1_macrova_m6(GlobalEnumeration.rossogiallox,GlobalEnumeration.rossoverde,GlobalEnumeration.rossogialloaverdea,GlobalEnumeration.rossogialloaverdea,GlobalEnumeration.rossogiallox,GlobalEnumeration.rossogialloaverdea, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]) == GlobalEnumeration.c180x, di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) and db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            return False
        #  /*46,*/ assegna alla macro il valore  False
        return False
    
    # for each manual command, the corresponding method is created
    def eventMainclass_c1_command_comm10DaSenderac49796(self, notifying_process):
        notifying_process.response_notify_man_cmd(self, 'eventMainclass_c1_command_comm10DaSenderac49796')
    
    # for each automatic command, the corresponding method is created
    def eventMainclass_c1_command_comm7(self, notifying_process):
        notifying_process.response_notify_auto_cmd(self, 'eventMainclass_c1_command_comm7')
    
    def eventMainclass_c1_command_comm8(self, notifying_process, argomento_ave1, argomento_ave10, argomento_ave5, argomento_ave9):
        notifying_process.response_notify_auto_cmd(self, 'eventMainclass_c1_command_comm8', argomento_ave1=argomento_ave1, argomento_ave10=argomento_ave10, argomento_ave5=argomento_ave5, argomento_ave9=argomento_ave9)
    

    def update_precedente(self):
        # update the variables with previous value
        self.set_mainclass_c1_previousco_c10_prev(self.get_mainclass_c1_previousco_c10())
        self.set_mainclass_c1_previousco_c4_prev(self.get_mainclass_c1_previousco_c4())
        self.set_mainclass_c1_previousco_c5_prev(self.get_mainclass_c1_previousco_c5())
        self.set_mainclass_c1_previousco_c6_prev(self.get_mainclass_c1_previousco_c6())
        self.set_mainclass_c1_previousva_pv1_prev(self.get_mainclass_c1_previousva_pv1())
        self.set_mainclass_c1_previousva_pv2_prev(self.get_mainclass_c1_previousva_pv2())
        self.set_mainclass_c1_previousva_pv3_prev(self.get_mainclass_c1_previousva_pv3())

