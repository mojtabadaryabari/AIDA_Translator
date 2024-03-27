# Codice del modello 'TestCase18', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
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

        self.set_mainclass_c1_previousva_pv1(GlobalEnumeration.rossogialloxverdex)
        self.set_mainclass_c1_previousva_pv2(GlobalEnumeration.rossogiallox)
        self.set_mainclass_c1_previousva_pv3(False)
        self.set_mainclass_c1_previousva_pv4(GlobalEnumeration.c270x)
        self.set_mainclass_c1_restoreva_rv1(GlobalEnumeration.c270x)
        self.set_mainclass_c1_restoreva_rv2(False)
        self.set_mainclass_c1_restoreva_rv3(0)
        self.set_mainclass_c1_restoreva_rv4(GlobalEnumeration.rossogialloaverdea)
        self.set_mainclass_c1_restoreva_rv5(False)
        self.set_mainclass_c1_variabile_v10(False)
        self.set_mainclass_c1_variabile_v2(0)
        self.set_mainclass_c1_variabile_v3(GlobalEnumeration.rossogialloxverdex)
        self.set_mainclass_c1_variabile_v8(0)
        self.set_mainclass_c1_variabile_v9(GlobalEnumeration.c270x)

        self._expected_commands_map = {
            Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1 : set([]),
        }

    def set_expected_cmds_response(self):
        # for each manual command of MainClass_C1
        if self.is_triggered('eventMainclass_c1_command_comm2'):
            self.set_man_cmd_response('eventMainclass_c1_command_comm2',self.ManCmdResponse.UNEXPECTED)
        else:
            self.set_man_cmd_response('eventMainclass_c1_command_comm2',self.ManCmdResponse.NOOP)



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
    def init_configuration(self, mainclass_c1_parametro_p1, mainclass_c1_parametro_p4, mainclass_c1_parametro_p5, mainclass_c1_parametro_p8, mainclass_c1_parametro_p9):
        # initialize the record type parameters
        # initialize the simple type parameters
        self.set_mainclass_c1_parametro_p1(mainclass_c1_parametro_p1)
        self.set_mainclass_c1_parametro_p4(mainclass_c1_parametro_p4)
        self.set_mainclass_c1_parametro_p5(mainclass_c1_parametro_p5)
        self.set_mainclass_c1_parametro_p8(mainclass_c1_parametro_p8)
        self.set_mainclass_c1_parametro_p9(mainclass_c1_parametro_p9)

        # initialize the timers
        self.set_mainclass_c1_restoreti_ti1(1325000)
        self.set_mainclass_c1_restoreti_ti1_restore(1325000)
        self.set_mainclass_c1_restoreti_ti2(50000)
        self.set_mainclass_c1_restoreti_ti2_restore(50000)
        self.set_mainclass_c1_restoreti_ti3(3413000)
        self.set_mainclass_c1_restoreti_ti3_restore(3413000)
        self.set_mainclass_c1_restoreti_ti4(32000)
        self.set_mainclass_c1_restoreti_ti4_restore(32000)
        self.set_mainclass_c1_restoreti_ti5(55000)
        self.set_mainclass_c1_restoreti_ti5_restore(55000)
        self.set_mainclass_c1_timer_t5(41000)

        self.timers = [self.mainclass_c1_restoreti_ti1,self.mainclass_c1_restoreti_ti1_restore,self.mainclass_c1_restoreti_ti2,self.mainclass_c1_restoreti_ti2_restore,self.mainclass_c1_restoreti_ti3,self.mainclass_c1_restoreti_ti3_restore,self.mainclass_c1_restoreti_ti4,self.mainclass_c1_restoreti_ti4_restore,self.mainclass_c1_restoreti_ti5,self.mainclass_c1_restoreti_ti5_restore,self.mainclass_c1_timer_t5,]

        # initialize the counters
        self.set_mainclass_c1_contatore_co10(0)
        self.set_mainclass_c1_contatore_co5(0)
        self.set_mainclass_c1_contatore_co7(0)

    # setters for record type parameters

    # getters for record type parameters

    # setters for simple type parameters
    def set_mainclass_c1_parametro_p1(self, mainclass_c1_parametro_p1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p1",mainclass_c1_parametro_p1)

    def set_mainclass_c1_parametro_p4(self, mainclass_c1_parametro_p4):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p4",mainclass_c1_parametro_p4)

    def set_mainclass_c1_parametro_p5(self, mainclass_c1_parametro_p5):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p5",mainclass_c1_parametro_p5)

    def set_mainclass_c1_parametro_p8(self, mainclass_c1_parametro_p8):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p8",mainclass_c1_parametro_p8)

    def set_mainclass_c1_parametro_p9(self, mainclass_c1_parametro_p9):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p9",mainclass_c1_parametro_p9)


    # getters for simple type parameters
    def get_mainclass_c1_parametro_p1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p1")

    def get_mainclass_c1_parametro_p4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p4")

    def get_mainclass_c1_parametro_p5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p5")

    def get_mainclass_c1_parametro_p8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p8")

    def get_mainclass_c1_parametro_p9(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p9")


    # setters for comandi al piazzale
    def set_mainclass_c1_comando_c1(self, mainclass_c1_comando_c1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c1",mainclass_c1_comando_c1)


    # getters for controlli dal piazzale
    def get_consdef(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"consdef")

    def get_mainclass_c1_controllo_c10(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c10")

    def get_mainclass_c1_controllo_c2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c2")

    def get_mainclass_c1_controllo_c7(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c7")

    def get_mainclass_c1_controllo_c9(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c9")

    def get_mainclass_c1_previousco_c3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c3")

    def get_mainclass_c1_previousco_c5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c5")

    def get_mainclass_c1_previousco_c6(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c6")

    def get_mainclass_c1_previousco_c8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c8")


    # setters for state variables
    def set_mainclass_c1_previousco_c3_prev(self, mainclass_c1_previousco_c3_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c3_prev",mainclass_c1_previousco_c3_prev)
    def set_mainclass_c1_previousco_c5_prev(self, mainclass_c1_previousco_c5_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c5_prev",mainclass_c1_previousco_c5_prev)
    def set_mainclass_c1_previousco_c6_prev(self, mainclass_c1_previousco_c6_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c6_prev",mainclass_c1_previousco_c6_prev)
    def set_mainclass_c1_previousco_c8_prev(self, mainclass_c1_previousco_c8_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c8_prev",mainclass_c1_previousco_c8_prev)
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
    def set_mainclass_c1_previousva_pv4(self, mainclass_c1_previousva_pv4):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousva_pv4",mainclass_c1_previousva_pv4)
    def set_mainclass_c1_previousva_pv4_prev(self, mainclass_c1_previousva_pv4_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousva_pv4_prev",mainclass_c1_previousva_pv4_prev)
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
    def set_mainclass_c1_variabile_v10(self, mainclass_c1_variabile_v10):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v10",mainclass_c1_variabile_v10)
    def set_mainclass_c1_variabile_v2(self, mainclass_c1_variabile_v2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v2",mainclass_c1_variabile_v2)
    def set_mainclass_c1_variabile_v3(self, mainclass_c1_variabile_v3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v3",mainclass_c1_variabile_v3)
    def set_mainclass_c1_variabile_v8(self, mainclass_c1_variabile_v8):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v8",mainclass_c1_variabile_v8)
    def set_mainclass_c1_variabile_v9(self, mainclass_c1_variabile_v9):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v9",mainclass_c1_variabile_v9)

    # getters for state variables
    def get_mainclass_c1_previousco_c3_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c3_prev")

    def get_mainclass_c1_previousco_c5_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c5_prev")

    def get_mainclass_c1_previousco_c6_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c6_prev")

    def get_mainclass_c1_previousco_c8_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c8_prev")

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

    def get_mainclass_c1_previousva_pv4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousva_pv4")

    def get_mainclass_c1_previousva_pv4_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousva_pv4_prev")

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

    def get_mainclass_c1_variabile_v10(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v10")

    def get_mainclass_c1_variabile_v2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v2")

    def get_mainclass_c1_variabile_v3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v3")

    def get_mainclass_c1_variabile_v8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v8")

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

    def set_mainclass_c1_restoreti_ti5(self, timerDuration):
        self.mainclass_c1_restoreti_ti5 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_restoreti_ti5", self.memory)

    def set_mainclass_c1_restoreti_ti5_restore(self, timerDuration):
        self.mainclass_c1_restoreti_ti5_restore = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_restoreti_ti5_restore", self.memory)

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

    def get_mainclass_c1_restoreti_ti5(self):
        return self.mainclass_c1_restoreti_ti5

    def get_mainclass_c1_restoreti_ti5_restore(self):
        return self.mainclass_c1_restoreti_ti5_restore

    def get_mainclass_c1_timer_t5(self):
        return self.mainclass_c1_timer_t5


    # setters for counters
    def set_mainclass_c1_contatore_co10(self, counterInitValue):
        self.mainclass_c1_contatore_co10 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "mainclass_c1_contatore_co10", self.memory)

    def set_mainclass_c1_contatore_co5(self, counterInitValue):
        self.mainclass_c1_contatore_co5 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "mainclass_c1_contatore_co5", self.memory)

    def set_mainclass_c1_contatore_co7(self, counterInitValue):
        self.mainclass_c1_contatore_co7 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "mainclass_c1_contatore_co7", self.memory)


    # getters for counters
    def get_mainclass_c1_contatore_co10(self):
        return self.mainclass_c1_contatore_co10

    def get_mainclass_c1_contatore_co5(self):
        return self.mainclass_c1_contatore_co5

    def get_mainclass_c1_contatore_co7(self):
        return self.mainclass_c1_contatore_co7



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
                     )
        add_instance_deb_info(self.station_name, self.name, self.instance_name, CdLDebInfo([
            # transizioni iniziali
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.StatoIniziale, Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1,
                         guard=(self.dbs[0], ),
                         effect=(),
                         phase = TransPhase.Stato
                         ),
            # transizioni della fase manuale
            # transizioni della fase di stato
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1,Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1,
                         guard=(self.dbs[1], ),
                         effect=(),
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
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1)
            self.effect_INITIALIZATION_StatoIniziale_state1_000()
            self.response_wait()

        self.set_mainclass_c1_previousco_c3_prev(True)
        self.set_mainclass_c1_previousco_c5_prev(False)
        self.set_mainclass_c1_previousco_c6_prev(GlobalEnumeration.c270xx)
        self.set_mainclass_c1_previousco_c8_prev(False)
        self.set_mainclass_c1_previousva_pv1_prev(self.get_mainclass_c1_previousva_pv1())
        self.set_mainclass_c1_previousva_pv2_prev(self.get_mainclass_c1_previousva_pv2())
        self.set_mainclass_c1_previousva_pv3_prev(self.get_mainclass_c1_previousva_pv3())
        self.set_mainclass_c1_previousva_pv4_prev(self.get_mainclass_c1_previousva_pv4())

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
                pass #return ERROR("the current state variable is not set (command: %s)" % command)
            else:
                # if the current state variable is not set, an exception will be raised
                return ERROR("the current state variable is not set (command: %s)" % command)

        if self.is_state_phase():
            if self.is_current_state(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1):
                if(self.guard_PERMANENCE_state1_000()):
                    self.curr_transition = self.Transition._State1__State1__stateSheet_0__permanence
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
        Nessuna
        }
        """
        pass
    
    # effect macros
    def macroMainclass_c1_macroef_m10(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV2 non è  diverso da  False  commento: {38,} e  se il contatore MainClass_C1_contatore_Co10 non è  minore di  commento: {55,} 14, commento: {66,} Assegna al comando MainClass_C1_comando_C1 il valore  True 
        
         ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V3 il valore c270xx
        
        
         commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è disattivo commento: {38,} o  se il contatore MainClass_C1_contatore_Co10 è  maggiore di  commento: {54,} 135 e  se il controllo ConsDef  è  uguale a FALSE , commento: {70,}Incrementa il contatore MainClass_C1_contatore_Co7
        
           
         commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} e  se la variabile MainClass_C1_variabile_V3 è  diverso da c270xx e  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} o  se il parametro MainClass_C1_parametro_P5 è  diverso da  True ,  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V2 il valore 6 commento: {67,}
        
         ,altrimenti  commento: {68,}Attiva il timer MainClass_C1_timer_T5
        
        
        
        }
        """
        def populate_macroMainclass_c1_macroef_m10_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITEStatementImpl\n/*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV2 non è  diverso da  False  /*38,*/ e  se il contatore MainClass_C1_contatore_Co10 non è  minore di  /*55,*/ 14, /*66,*/ Assegna al comando MainClass_C1_comando_C1 il valore  True 

 ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V3 il valore c270xx""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV2 non è  diverso da  False  /*38,*/ e  se il contatore MainClass_C1_contatore_Co10 non è  minore di  /*55,*/ 14""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_restoreva_rv2_restore)  è uguale a  (False)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_restoreva_rv2_restore)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_restoreva_rv2_restore)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co10)  è minore di  (14))""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co10)  è minore di  (14)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITStatement\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è disattivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 è  maggiore di  /*54,*/ 135 e  se il controllo ConsDef  è  uguale a FALSE , /*70,*/Incrementa il contatore MainClass_C1_contatore_Co7""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è disattivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 è  maggiore di  /*54,*/ 135 e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_restoreti_ti1_restore' è inattivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_restoreti_ti1_restore' è inattivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( (mainclass_c1_contatore_co10)  è maggiore di  (135) )  e  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co10)  è maggiore di  (135)""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#1
                            DIStatement("""ITEStatementImpl\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V3 è  diverso da c270xx e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P5 è  diverso da  True ,  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V2 il valore 6 /*67,*/

 ,altrimenti  /*68,*/Attiva il timer MainClass_C1_timer_T5""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V3 è  diverso da c270xx e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P5 è  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( ( negazione di (il timer 'mainclass_c1_restoreti_ti1_restore' è scaduto) )  e  ( (consdef)  è uguale a  (False) ) )  e  ( negazione di ((mainclass_c1_variabile_v3)  è uguale a  (c270xx)) ) )  e  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di (il timer 'mainclass_c1_restoreti_ti1_restore' è scaduto) )  e  ( (consdef)  è uguale a  (False) ) )  e  ( negazione di ((mainclass_c1_variabile_v3)  è uguale a  (c270xx)) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (il timer 'mainclass_c1_restoreti_ti1_restore' è scaduto) )  e  ( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_restoreti_ti1_restore' è scaduto)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_restoreti_ti1_restore' è scaduto""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v3)  è uguale a  (c270xx))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v3)  è uguale a  (c270xx)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p5)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p5)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#2
                ])

        populate_macroMainclass_c1_macroef_m10_SrfMacroDefInfo(di_ctx)
        #  /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV2 non è  diverso da  False  /*38,*/ e  se il contatore MainClass_C1_contatore_Co10 non è  minore di  /*55,*/ 14, /*66,*/ Assegna al comando MainClass_C1_comando_C1 il valore  True 
        #   ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V3 il valore c270xx
        if db((db(not db(not db(self.get_mainclass_c1_restoreva_rv2_restore() == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co10().get_valore() < 14, di_ctx.subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.set_mainclass_c1_comando_c1(True)
        else:
            self.set_mainclass_c1_variabile_v3(GlobalEnumeration.c270xx)
        #  /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è disattivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 è  maggiore di  /*54,*/ 135 e  se il controllo ConsDef  è  uguale a FALSE , /*70,*/Incrementa il contatore MainClass_C1_contatore_Co7
        if db((db(not db(self.get_mainclass_c1_restoreti_ti1_restore().isDisattivato(), di_ctx.subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0]) or db((db(self.get_mainclass_c1_contatore_co10().get_valore() > 135, di_ctx.subs[1].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.get_mainclass_c1_contatore_co7().incrementa()
        #  /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V3 è  diverso da c270xx e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P5 è  diverso da  True ,  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V2 il valore 6 /*67,*/
        #   ,altrimenti  /*68,*/Attiva il timer MainClass_C1_timer_T5
        if db((db((db((db((db(not db(self.get_mainclass_c1_restoreti_ti1_restore().isScaduto(), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v3() == GlobalEnumeration.c270xx, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[2].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_parametro_p5() == True, di_ctx.subs[2].subs[0].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.set_mainclass_c1_variabile_v2(6)
        else:
            self.get_mainclass_c1_timer_t5().attiva()
    
    def macroMainclass_c1_macroef_m3(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {34,}  se il parametro MainClass_C1_parametro_P9 è  minore di  commento: {55,} 9 commento: {34,} e  se il parametro MainClass_C1_parametro_P9 è  maggiore di  commento: {54,} 6, commento: {66,} Assegna al comando MainClass_C1_comando_C1 il valore  True 
        
           
         commento: {35,}  se il controllo MainClass_C1_controllo_C9 è  diverso da avanzamento commento: {37,} e  se la variabile MainClass_C1_variabile_V2 è  uguale a  commento: {53,} 1,  Applica gli effetti
               della macro MainClass_C1_macroef_M10  commento: {73,}
        
           
         commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI2 non è disattivo commento: {37,} o  se la variabile MainClass_C1_variabile_V9 non è  diverso da avanzamento, commento: {72,}Azzera il contatore MainClass_C1_contatore_Co10
        
           
        
        }
        """
        def populate_macroMainclass_c1_macroef_m3_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*34,*/  se il parametro MainClass_C1_parametro_P9 è  minore di  /*55,*/ 9 /*34,*/ e  se il parametro MainClass_C1_parametro_P9 è  maggiore di  /*54,*/ 6, /*66,*/ Assegna al comando MainClass_C1_comando_C1 il valore  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*34,*/  se il parametro MainClass_C1_parametro_P9 è  minore di  /*55,*/ 9 /*34,*/ e  se il parametro MainClass_C1_parametro_P9 è  maggiore di  /*54,*/ 6""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_parametro_p9)  è minore di  (9)""", [
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_parametro_p9)  è maggiore di  (6)""", [
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITStatement\n/*35,*/  se il controllo MainClass_C1_controllo_C9 è  diverso da avanzamento /*37,*/ e  se la variabile MainClass_C1_variabile_V2 è  uguale a  /*53,*/ 1,  Applica gli effetti
       della macro MainClass_C1_macroef_M10""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*35,*/  se il controllo MainClass_C1_controllo_C9 è  diverso da avanzamento /*37,*/ e  se la variabile MainClass_C1_variabile_V2 è  uguale a  /*53,*/ 1""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c9)  è uguale a  (avanzamento))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c9)  è uguale a  (avanzamento)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v2)  è uguale a  (1)""", [
                            ]),#1
                            ]),#0
                            DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M10"""),#1
                            ]),#1
                            DIStatement("""ITStatement\n/*73,*/

   
 /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI2 non è disattivo /*37,*/ o  se la variabile MainClass_C1_variabile_V9 non è  diverso da avanzamento, /*72,*/Azzera il contatore MainClass_C1_contatore_Co10""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*73,*/

   
 /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI2 non è disattivo /*37,*/ o  se la variabile MainClass_C1_variabile_V9 non è  diverso da avanzamento""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_restoreti_ti2_restore' è inattivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_restoreti_ti2_restore' è inattivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_variabile_v9)  è uguale a  (avanzamento)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v9)  è uguale a  (avanzamento))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v9)  è uguale a  (avanzamento)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#2
                ])

        populate_macroMainclass_c1_macroef_m3_SrfMacroDefInfo(di_ctx)
        #  /*34,*/  se il parametro MainClass_C1_parametro_P9 è  minore di  /*55,*/ 9 /*34,*/ e  se il parametro MainClass_C1_parametro_P9 è  maggiore di  /*54,*/ 6, /*66,*/ Assegna al comando MainClass_C1_comando_C1 il valore  True
        if db((db(self.get_mainclass_c1_parametro_p9() < 9, di_ctx.subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_parametro_p9() > 6, di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.set_mainclass_c1_comando_c1(True)
        #  /*35,*/  se il controllo MainClass_C1_controllo_C9 è  diverso da avanzamento /*37,*/ e  se la variabile MainClass_C1_variabile_V2 è  uguale a  /*53,*/ 1,  Applica gli effetti
        #         della macro MainClass_C1_macroef_M10
        if db((db(not db(self.get_mainclass_c1_controllo_c9() == GlobalEnumeration.avanzamento, di_ctx.subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0]) and db(self.get_mainclass_c1_variabile_v2() == 1, di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.macroMainclass_c1_macroef_m10(di_ctx.subs[1].subs[1])
        #  /*73,*/
        #     
        #   /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI2 non è disattivo /*37,*/ o  se la variabile MainClass_C1_variabile_V9 non è  diverso da avanzamento, /*72,*/Azzera il contatore MainClass_C1_contatore_Co10
        if db((db(not db(self.get_mainclass_c1_restoreti_ti2_restore().isDisattivato(), di_ctx.subs[2].subs[0].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_variabile_v9() == GlobalEnumeration.avanzamento, di_ctx.subs[2].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.get_mainclass_c1_contatore_co10().resetta()
    
    def macroMainclass_c1_macroef_m4(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {34,}  se lo stato  non è  diverso da  commento: {56,}  state1  commento: {106,} commento: {36,} e  se il timer MainClass_C1_timer_T5 è disattivo commento: {37,} e  se la variabile MainClass_C1_variabile_V9 non è  diverso da avanzamento commento: {37,} o  se la variabile MainClass_C1_variabile_V8 non è  uguale a  commento: {53,} 2 commento: {34,} e  se il parametro MainClass_C1_parametro_P4 è  diverso da avanzamentox, commento: {66,} Assegna al comando MainClass_C1_comando_C1 il valore  False 
        
           
         commento: {34,}  se lo stato  non è  uguale a  commento: {53,}  state1  commento: {106,} commento: {37,} o  se la variabile MainClass_C1_variabile_V2 non è  maggiore di  commento: {54,} 2 commento: {35,} e  se il controllo MainClass_C1_controllo_C2 è  uguale a avanzamentox commento: {34,} o  se il parametro MainClass_C1_parametro_P9 è  maggiore di  commento: {54,} 8 commento: {34,} o  se il parametro MainClass_C1_parametro_P9 non è  uguale a  commento: {53,} 3, commento: {71,}Decrementa il contatore MainClass_C1_contatore_Co10
        
           
          se il controllo ConsDef è uguale a FALSE  commento: {38,} o  se il contatore MainClass_C1_contatore_Co10 non è  maggiore di  commento: {54,} 145 commento: {37,} e  se la variabile MainClass_C1_variabile_V3 è  diverso da c270xx, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V9 il valore avanzamento
        
           
        
        }
        """
        def populate_macroMainclass_c1_macroef_m4_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*36,*/ e  se il timer MainClass_C1_timer_T5 è disattivo /*37,*/ e  se la variabile MainClass_C1_variabile_V9 non è  diverso da avanzamento /*37,*/ o  se la variabile MainClass_C1_variabile_V8 non è  uguale a  /*53,*/ 2 /*34,*/ e  se il parametro MainClass_C1_parametro_P4 è  diverso da avanzamentox, /*66,*/ Assegna al comando MainClass_C1_comando_C1 il valore  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*36,*/ e  se il timer MainClass_C1_timer_T5 è disattivo /*37,*/ e  se la variabile MainClass_C1_variabile_V9 non è  diverso da avanzamento /*37,*/ o  se la variabile MainClass_C1_variabile_V8 non è  uguale a  /*53,*/ 2 /*34,*/ e  se il parametro MainClass_C1_parametro_P4 è  diverso da avanzamentox""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di (negazione di ((lo stato di 'self')  è uguale a  (state1))) )  e  ( il timer 'mainclass_c1_timer_t5' è inattivo ) )  e  
( negazione di (negazione di ((mainclass_c1_variabile_v9)  è uguale a  (avanzamento))) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (negazione di ((lo stato di 'self')  è uguale a  (state1))) )  e  ( il timer 'mainclass_c1_timer_t5' è inattivo )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((lo stato di 'self')  è uguale a  (state1)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lo stato di 'self')  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t5' è inattivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_variabile_v9)  è uguale a  (avanzamento)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v9)  è uguale a  (avanzamento))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v9)  è uguale a  (avanzamento)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_variabile_v8)  è uguale a  (2)) )  e  
( negazione di ((mainclass_c1_parametro_p4)  è uguale a  (avanzamentox)) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v8)  è uguale a  (2))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v8)  è uguale a  (2)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p4)  è uguale a  (avanzamentox))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p4)  è uguale a  (avanzamentox)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITStatement\n/*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*37,*/ o  se la variabile MainClass_C1_variabile_V2 non è  maggiore di  /*54,*/ 2 /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  uguale a avanzamentox /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  maggiore di  /*54,*/ 8 /*34,*/ o  se il parametro MainClass_C1_parametro_P9 non è  uguale a  /*53,*/ 3, /*71,*/Decrementa il contatore MainClass_C1_contatore_Co10""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*37,*/ o  se la variabile MainClass_C1_variabile_V2 non è  maggiore di  /*54,*/ 2 /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  uguale a avanzamentox /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  maggiore di  /*54,*/ 8 /*34,*/ o  se il parametro MainClass_C1_parametro_P9 non è  uguale a  /*53,*/ 3""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( negazione di ((lo stato di 'self')  è uguale a  (state1)) )  o  
( ( negazione di ((mainclass_c1_variabile_v2)  è maggiore di  (2)) )  e  
( (mainclass_c1_controllo_c2)  è uguale a  (avanzamentox) ) ) )  o  
( (mainclass_c1_parametro_p9)  è maggiore di  (8) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( negazione di ((lo stato di 'self')  è uguale a  (state1)) )  o  
( ( negazione di ((mainclass_c1_variabile_v2)  è maggiore di  (2)) )  e  
( (mainclass_c1_controllo_c2)  è uguale a  (avanzamentox) ) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lo stato di 'self')  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_variabile_v2)  è maggiore di  (2)) )  e  
( (mainclass_c1_controllo_c2)  è uguale a  (avanzamentox) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v2)  è maggiore di  (2))""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_variabile_v2)  è maggiore di  (2)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c2)  è uguale a  (avanzamentox)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_parametro_p9)  è maggiore di  (8)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p9)  è uguale a  (3))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p9)  è uguale a  (3)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#1
                            DIStatement("""ITStatement\nse il controllo ConsDef è uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 non è  maggiore di  /*54,*/ 145 /*37,*/ e  se la variabile MainClass_C1_variabile_V3 è  diverso da c270xx, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V9 il valore avanzamento""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse il controllo ConsDef è uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 non è  maggiore di  /*54,*/ 145 /*37,*/ e  se la variabile MainClass_C1_variabile_V3 è  diverso da c270xx""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_contatore_co10)  è maggiore di  (145)) )  e  
( negazione di ((mainclass_c1_variabile_v3)  è uguale a  (c270xx)) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co10)  è maggiore di  (145))""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co10)  è maggiore di  (145)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v3)  è uguale a  (c270xx))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v3)  è uguale a  (c270xx)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#2
                ])

        populate_macroMainclass_c1_macroef_m4_SrfMacroDefInfo(di_ctx)
        #  /*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*36,*/ e  se il timer MainClass_C1_timer_T5 è disattivo /*37,*/ e  se la variabile MainClass_C1_variabile_V9 non è  diverso da avanzamento /*37,*/ o  se la variabile MainClass_C1_variabile_V8 non è  uguale a  /*53,*/ 2 /*34,*/ e  se il parametro MainClass_C1_parametro_P4 è  diverso da avanzamentox, /*66,*/ Assegna al comando MainClass_C1_comando_C1 il valore  False
        if db((db((db((db(not db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_timer_t5().isDisattivato(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_variabile_v9() == GlobalEnumeration.avanzamento, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_variabile_v8() == 2, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p4() == GlobalEnumeration.avanzamentox, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.set_mainclass_c1_comando_c1(False)
        #  /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*37,*/ o  se la variabile MainClass_C1_variabile_V2 non è  maggiore di  /*54,*/ 2 /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  uguale a avanzamentox /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  maggiore di  /*54,*/ 8 /*34,*/ o  se il parametro MainClass_C1_parametro_P9 non è  uguale a  /*53,*/ 3, /*71,*/Decrementa il contatore MainClass_C1_contatore_Co10
        if db((db((db((db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_variabile_v2() > 2, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_controllo_c2() == GlobalEnumeration.avanzamentox, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_parametro_p9() > 8, di_ctx.subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_parametro_p9() == 3, di_ctx.subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.get_mainclass_c1_contatore_co10().decrementa()
        #  se il controllo ConsDef è uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 non è  maggiore di  /*54,*/ 145 /*37,*/ e  se la variabile MainClass_C1_variabile_V3 è  diverso da c270xx, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V9 il valore avanzamento
        if db((db(self.get_consdef() == False, di_ctx.subs[2].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_contatore_co10().get_valore() > 145, di_ctx.subs[2].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v3() == GlobalEnumeration.c270xx, di_ctx.subs[2].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[1].subs[1])), di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.set_mainclass_c1_variabile_v9(GlobalEnumeration.avanzamento)
    
    def macroMainclass_c1_macroef_m5(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
         
        { commento: {37,}  se la variabile MainClass_C1_variabile_V2 è  maggiore di  commento: {54,} 9 commento: {34,} o  se il parametro MainClass_C1_parametro_P9 è  maggiore di  commento: {54,} 1 commento: {34,} o  se il parametro MainClass_C1_parametro_P5 non è  uguale a  False  commento: {34,} o  se il parametro MainClass_C1_parametro_P9 non è  maggiore di  commento: {54,} 6 commento: {36,} o  se il timer MainClass_C1_timer_T5 è disattivo, commento: {69,}Disattiva il timer MainClass_C1_timer_T5
        
           
          se il ripristino dello stato  non è  diverso da  commento: {56,}  state1  commento: {107,} commento: {35,} o  se il controllo MainClass_C1_controllo_C2 è  diverso da avanzamentox e  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} o  se la variabile MainClass_C1_variabile_V2 non è  diverso da  commento: {56,} 3 commento: {36,} o  se il timer MainClass_C1_timer_T5 non è attivo, commento: {66,} Assegna al comando MainClass_C1_comando_C1 il valore  True 
        
           
         commento: {37,}  se la variabile MainClass_C1_variabile_V9 è  diverso da avanzamento commento: {38,} e  se il contatore MainClass_C1_contatore_Co10 è  uguale a  commento: {53,} 1504132 o  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} o  se il timer MainClass_C1_timer_T5 è attivo, commento: {66,} Assegna al comando MainClass_C1_comando_C1 il valore  True 
        
           
          se il ripristino dello stato  non è  uguale a  commento: {53,}  state1  commento: {107,} commento: {35,} e  se il controllo MainClass_C1_controllo_C2 non è  uguale a avanzamentox commento: {35,} o  se il controllo MainClass_C1_controllo_C9 è  uguale a avanzamento e  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} e  se la variabile MainClass_C1_variabile_V2 non è  maggiore di  commento: {54,} 6,  Applica gli effetti
               della macro MainClass_C1_macroef_M10  commento: {73,}
        
         ,altrimenti  commento: {68,}Attiva il timer MainClass_C1_timer_T5
        
        
         commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è scaduto, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V2 il valore 7
        
           
        
        }
        """
        def populate_macroMainclass_c1_macroef_m5_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*37,*/  se la variabile MainClass_C1_variabile_V2 è  maggiore di  /*54,*/ 9 /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  maggiore di  /*54,*/ 1 /*34,*/ o  se il parametro MainClass_C1_parametro_P5 non è  uguale a  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P9 non è  maggiore di  /*54,*/ 6 /*36,*/ o  se il timer MainClass_C1_timer_T5 è disattivo, /*69,*/Disattiva il timer MainClass_C1_timer_T5""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*37,*/  se la variabile MainClass_C1_variabile_V2 è  maggiore di  /*54,*/ 9 /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  maggiore di  /*54,*/ 1 /*34,*/ o  se il parametro MainClass_C1_parametro_P5 non è  uguale a  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P9 non è  maggiore di  /*54,*/ 6 /*36,*/ o  se il timer MainClass_C1_timer_T5 è disattivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( ( (mainclass_c1_variabile_v2)  è maggiore di  (9) )  o  
( (mainclass_c1_parametro_p9)  è maggiore di  (1) ) )  o  
( negazione di ((mainclass_c1_parametro_p5)  è uguale a  (False)) ) )  o  
( negazione di ((mainclass_c1_parametro_p9)  è maggiore di  (6)) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( (mainclass_c1_variabile_v2)  è maggiore di  (9) )  o  
( (mainclass_c1_parametro_p9)  è maggiore di  (1) ) )  o  
( negazione di ((mainclass_c1_parametro_p5)  è uguale a  (False)) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( (mainclass_c1_variabile_v2)  è maggiore di  (9) )  o  
( (mainclass_c1_parametro_p9)  è maggiore di  (1) )""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_variabile_v2)  è maggiore di  (9)""", [
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_parametro_p9)  è maggiore di  (1)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p5)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p5)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p9)  è maggiore di  (6))""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_parametro_p9)  è maggiore di  (6)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t5' è inattivo""", [
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITStatement\nse il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ /*35,*/ o  se il controllo MainClass_C1_controllo_C2 è  diverso da avanzamentox e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile MainClass_C1_variabile_V2 non è  diverso da  /*56,*/ 3 /*36,*/ o  se il timer MainClass_C1_timer_T5 non è attivo, /*66,*/ Assegna al comando MainClass_C1_comando_C1 il valore  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ /*35,*/ o  se il controllo MainClass_C1_controllo_C2 è  diverso da avanzamentox e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile MainClass_C1_variabile_V2 non è  diverso da  /*56,*/ 3 /*36,*/ o  se il timer MainClass_C1_timer_T5 non è attivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( negazione di (negazione di ((stato_restore)  è uguale a  (state1))) )  o  
( ( negazione di ((mainclass_c1_controllo_c2)  è uguale a  (avanzamentox)) )  e  
( (consdef)  è uguale a  (False) ) ) )  o  
( negazione di (negazione di ((mainclass_c1_variabile_v2)  è uguale a  (3))) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( negazione di (negazione di ((stato_restore)  è uguale a  (state1))) )  o  
( ( negazione di ((mainclass_c1_controllo_c2)  è uguale a  (avanzamentox)) )  e  
( (consdef)  è uguale a  (False) ) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((stato_restore)  è uguale a  (state1)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((stato_restore)  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(stato_restore)  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_controllo_c2)  è uguale a  (avanzamentox)) )  e  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c2)  è uguale a  (avanzamentox))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c2)  è uguale a  (avanzamentox)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_variabile_v2)  è uguale a  (3)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v2)  è uguale a  (3))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v2)  è uguale a  (3)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t5' è attivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t5' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#1
                            DIStatement("""ITStatement\n/*37,*/  se la variabile MainClass_C1_variabile_V9 è  diverso da avanzamento /*38,*/ e  se il contatore MainClass_C1_contatore_Co10 è  uguale a  /*53,*/ 1504132 o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer MainClass_C1_timer_T5 è attivo, /*66,*/ Assegna al comando MainClass_C1_comando_C1 il valore  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*37,*/  se la variabile MainClass_C1_variabile_V9 è  diverso da avanzamento /*38,*/ e  se il contatore MainClass_C1_contatore_Co10 è  uguale a  /*53,*/ 1504132 o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer MainClass_C1_timer_T5 è attivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( negazione di ((mainclass_c1_variabile_v9)  è uguale a  (avanzamento)) )  e  
( (mainclass_c1_contatore_co10)  è uguale a  (1504132) ) )  o  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_variabile_v9)  è uguale a  (avanzamento)) )  e  
( (mainclass_c1_contatore_co10)  è uguale a  (1504132) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v9)  è uguale a  (avanzamento))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v9)  è uguale a  (avanzamento)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co10)  è uguale a  (1504132)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t5' è attivo""", [
                            ]),#1
                            ]),#0
                            ]),#2
                            DIStatement("""ITEStatementImpl\nse il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*35,*/ e  se il controllo MainClass_C1_controllo_C2 non è  uguale a avanzamentox /*35,*/ o  se il controllo MainClass_C1_controllo_C9 è  uguale a avanzamento e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V2 non è  maggiore di  /*54,*/ 6,  Applica gli effetti
       della macro MainClass_C1_macroef_M10  /*73,*/

 ,altrimenti  /*68,*/Attiva il timer MainClass_C1_timer_T5""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*35,*/ e  se il controllo MainClass_C1_controllo_C2 non è  uguale a avanzamentox /*35,*/ o  se il controllo MainClass_C1_controllo_C9 è  uguale a avanzamento e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V2 non è  maggiore di  /*54,*/ 6""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((stato_restore)  è uguale a  (state1)) )  e  
( negazione di ((mainclass_c1_controllo_c2)  è uguale a  (avanzamentox)) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((stato_restore)  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(stato_restore)  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c2)  è uguale a  (avanzamentox))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c2)  è uguale a  (avanzamentox)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( (mainclass_c1_controllo_c9)  è uguale a  (avanzamento) )  e  ( (consdef)  è uguale a  (False) ) )  e  
( negazione di ((mainclass_c1_variabile_v2)  è maggiore di  (6)) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (mainclass_c1_controllo_c9)  è uguale a  (avanzamento) )  e  ( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c9)  è uguale a  (avanzamento)""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v2)  è maggiore di  (6))""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_variabile_v2)  è maggiore di  (6)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M10"""),#1
                            ]),#3
                            DIStatement("""ITStatement\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è scaduto, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V2 il valore 7""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino del timer  MainClass_C1_restoreTI_TI1 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_restoreti_ti1_restore' è scaduto""", [
                            ]),#0
                            ]),#0
                            ]),#4
                ])

        populate_macroMainclass_c1_macroef_m5_SrfMacroDefInfo(di_ctx)
        #  /*37,*/  se la variabile MainClass_C1_variabile_V2 è  maggiore di  /*54,*/ 9 /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  maggiore di  /*54,*/ 1 /*34,*/ o  se il parametro MainClass_C1_parametro_P5 non è  uguale a  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P9 non è  maggiore di  /*54,*/ 6 /*36,*/ o  se il timer MainClass_C1_timer_T5 è disattivo, /*69,*/Disattiva il timer MainClass_C1_timer_T5
        if db((db((db((db((db(self.get_mainclass_c1_variabile_v2() > 9, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_parametro_p9() > 1, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_parametro_p5() == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_parametro_p9() > 6, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_timer_t5().isDisattivato(), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.get_mainclass_c1_timer_t5().disattiva()
        #  se il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ /*35,*/ o  se il controllo MainClass_C1_controllo_C2 è  diverso da avanzamentox e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile MainClass_C1_variabile_V2 non è  diverso da  /*56,*/ 3 /*36,*/ o  se il timer MainClass_C1_timer_T5 non è attivo, /*66,*/ Assegna al comando MainClass_C1_comando_C1 il valore  True
        if db((db((db((db(not db(not db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_controllo_c2() == GlobalEnumeration.avanzamentox, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_variabile_v2() == 3, di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_timer_t5().isAttivato(), di_ctx.subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.set_mainclass_c1_comando_c1(True)
        #  /*37,*/  se la variabile MainClass_C1_variabile_V9 è  diverso da avanzamento /*38,*/ e  se il contatore MainClass_C1_contatore_Co10 è  uguale a  /*53,*/ 1504132 o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer MainClass_C1_timer_T5 è attivo, /*66,*/ Assegna al comando MainClass_C1_comando_C1 il valore  True
        if db((db((db((db(not db(self.get_mainclass_c1_variabile_v9() == GlobalEnumeration.avanzamento, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_contatore_co10().get_valore() == 1504132, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[2].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0]) or db(self.get_mainclass_c1_timer_t5().isAttivato(), di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.set_mainclass_c1_comando_c1(True)
        #  se il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*35,*/ e  se il controllo MainClass_C1_controllo_C2 non è  uguale a avanzamentox /*35,*/ o  se il controllo MainClass_C1_controllo_C9 è  uguale a avanzamento e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V2 non è  maggiore di  /*54,*/ 6,  Applica gli effetti
        #         della macro MainClass_C1_macroef_M10  /*73,*/
        #   ,altrimenti  /*68,*/Attiva il timer MainClass_C1_timer_T5
        if db((db((db(not db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[3].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[3].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c2() == GlobalEnumeration.avanzamentox, di_ctx.subs[3].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[3].subs[0].subs[0].subs[1])), di_ctx.subs[3].subs[0].subs[0]) or db((db((db(self.get_mainclass_c1_controllo_c9() == GlobalEnumeration.avanzamento, di_ctx.subs[3].subs[0].subs[1].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[3].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[3].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v2() > 6, di_ctx.subs[3].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[3].subs[0].subs[1].subs[1])), di_ctx.subs[3].subs[0].subs[1])), di_ctx.subs[3].subs[0]):
            self.macroMainclass_c1_macroef_m10(di_ctx.subs[3].subs[1])
        else:
            self.get_mainclass_c1_timer_t5().attiva()
        #  /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è scaduto, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V2 il valore 7
        if db(not db(self.get_mainclass_c1_restoreti_ti1_restore().isScaduto(), di_ctx.subs[4].subs[0].subs[0]), di_ctx.subs[4].subs[0]):
            self.set_mainclass_c1_variabile_v2(7)
    
    def macroMainclass_c1_macroef_m7(self, argomento_af1, argomento_af10, argomento_af2, argomento_af3, argomento_af4, argomento_af5, argomento_af8, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV3 è  uguale a  commento: {53,} 7 commento: {34,} e  se il parametro MainClass_C1_parametro_P5 è  diverso da  False , commento: {70,}Incrementa il contatore MainClass_C1_contatore_Co10
        
           
        
        }
        """
        def populate_macroMainclass_c1_macroef_m7_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV3 è  uguale a  /*53,*/ 7 /*34,*/ e  se il parametro MainClass_C1_parametro_P5 è  diverso da  False , /*70,*/Incrementa il contatore MainClass_C1_contatore_Co10""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV3 è  uguale a  /*53,*/ 7 /*34,*/ e  se il parametro MainClass_C1_parametro_P5 è  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_restoreva_rv3_restore)  è uguale a  (7)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p5)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p5)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macroef_m7_SrfMacroDefInfo(di_ctx)
        #  /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV3 è  uguale a  /*53,*/ 7 /*34,*/ e  se il parametro MainClass_C1_parametro_P5 è  diverso da  False , /*70,*/Incrementa il contatore MainClass_C1_contatore_Co10
        if db((db(self.get_mainclass_c1_restoreva_rv3_restore() == 7, di_ctx.subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p5() == False, di_ctx.subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.get_mainclass_c1_contatore_co10().incrementa()
    
    # verify macros
    @srf_value_macro("macroMainclass_c1_macrove_m2")
    def macroMainclass_c1_macrove_m2(self, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
         
        { commento: {62,}  se la macro  MainClass_C1_macrova_M5 ( con argomento_a8   uguale a RossoGialloxVerdex ,argomento_a1   uguale a c270x ,argomento_a5   uguale a RossoVerde  e argomento_a2   uguale a c270x )  non  è  diverso da c270xx commento: {40,}  commento: {36,} e  se il timer MainClass_C1_timer_T5 non è scaduto, Almeno una delle seguenti { 
         commento: {61,} commento: {35,}  se il controllo MainClass_C1_controllo_C2 non è  diverso da avanzamentox commento: {34,} e  se il parametro MainClass_C1_parametro_P4 è  diverso da avanzamentox, Tutte le seguenti { 
         commento: {63,} commento: {34,}  se lo stato  non è  uguale a  commento: {53,}  state1  commento: {106,} commento: {35,} o  se il controllo MainClass_C1_controllo_C10 non è  diverso da  False , Solo una delle seguenti { 
         commento: {63,}  se il ripristino dello stato  non è  diverso da  commento: {56,}  state1  commento: {107,} commento: {36,} e  se il timer MainClass_C1_timer_T5 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} e  se il timer MainClass_C1_timer_T5 non è attivo, Solo una delle seguenti { 
         commento: {61,} commento: {37,}  se la variabile MainClass_C1_variabile_V2 è  diverso da  commento: {56,} 4, Tutte le seguenti { 
         commento: {61,} commento: {34,}  se lo stato  non è  diverso da  commento: {56,}  state1  commento: {106,} commento: {37,} o  se la variabile MainClass_C1_variabile_V8 è  minore di  commento: {55,} 8, Tutte le seguenti { 
          se la macro  MainClass_C1_macrova_M6 ( con argomento_a8   uguale a RossoGialloaVerdea  e argomento_a1   uguale a RossoVerde )   è  uguale a  True  commento: {40,} , Verifica che   commento: {47,48,51,}  commento: {34,}  il parametro MainClass_C1_parametro_P9 non sia  minore di  commento: {55,} 10
         commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co10 non sia  minore di  commento: {55,} 13325
         commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
        
        
         } Verifica che   commento: {47,48,49,}  commento: {,}  il controllo MainClass_C1_controllo_C10 non sia  uguale a  True 
         commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T5 sia scaduto
         commento: {104,} e  che  commento: {35,}  il controllo MainClass_C1_controllo_C9 non sia  uguale a avanzamento
         commento: {104,} o  che  commento: {36,}  il timer MainClass_C1_timer_T5 sia scaduto
         commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P4 non sia  uguale a avanzamentox
         commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
        
        
         } Verifica che   commento: {47,51,}  commento: {,}  il contatore MainClass_C1_contatore_Co10 sia  minore di  commento: {55,} 110
         commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P4 sia  diverso da avanzamentox
        
        
         } Verifica che   commento: {47,48,}  commento: {34,}  il parametro MainClass_C1_parametro_P4 sia  uguale a avanzamentox
         commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P9 non sia  uguale a  commento: {53,} 4
         commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C2 non sia  diverso da avanzamentox
         commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
        
        
         } Verifica che   commento: {48,50,}  commento: {,}  la variabile MainClass_C1_variabile_V2 sia  maggiore di  commento: {54,} 3
         commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
        
        
         } Verifica che   commento: {47,48,50,51,}  commento: {34,}  il parametro MainClass_C1_parametro_P9 sia  minore di  commento: {55,} 3
         commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co10 non sia  maggiore di  commento: {54,} 153
         commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C9 sia  uguale a avanzamento
         commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V2 sia  uguale a  commento: {53,} 3
         commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} e  che  commento: {35,}  il controllo MainClass_C1_controllo_C2 sia  uguale a avanzamentox
        
        
         } Verifica che   commento: {48,49,50,51,}  commento: {,}  la variabile MainClass_C1_variabile_V3 sia  uguale a c270xx
         commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T5 sia attivo
         commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C9 non sia  diverso da avanzamento
         commento: {104,} o  che  commento: {,}  il contatore MainClass_C1_contatore_Co5 non sia  maggiore di  commento: {54,} 152
         commento: {104,} e  che  commento: {38,}  il contatore MainClass_C1_contatore_Co10 sia  minore di  commento: {55,} 12
        
        
        }
        """
        def populate_macroMainclass_c1_macrove_m2_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/  se la macro  MainClass_C1_macrova_M5 ( con argomento_a8   uguale a RossoGialloxVerdex ,argomento_a1   uguale a c270x ,argomento_a5   uguale a RossoVerde  e argomento_a2   uguale a c270x )  non  è  diverso da c270xx /*40,*/  /*36,*/ e  se il timer MainClass_C1_timer_T5 non è scaduto, Almeno una delle seguenti { 
 /*61,*/ /*35,*/  se il controllo MainClass_C1_controllo_C2 non è  diverso da avanzamentox /*34,*/ e  se il parametro MainClass_C1_parametro_P4 è  diverso da avanzamentox, Tutte le seguenti { 
 /*63,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*35,*/ o  se il controllo MainClass_C1_controllo_C10 non è  diverso da  False , Solo una delle seguenti { 
 /*63,*/  se il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ /*36,*/ e  se il timer MainClass_C1_timer_T5 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T5 non è attivo, Solo una delle seguenti { 
 /*61,*/ /*37,*/  se la variabile MainClass_C1_variabile_V2 è  diverso da  /*56,*/ 4, Tutte le seguenti { 
 /*61,*/ /*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*37,*/ o  se la variabile MainClass_C1_variabile_V8 è  minore di  /*55,*/ 8, Tutte le seguenti { 
  se la macro  MainClass_C1_macrova_M6 ( con argomento_a8   uguale a RossoGialloaVerdea  e argomento_a1   uguale a RossoVerde )   è  uguale a  True  /*40,*/ , Verifica che   /*47,48,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  minore di  /*55,*/ 10
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  minore di  /*55,*/ 13325
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,49,*/  /*,*/  il controllo MainClass_C1_controllo_C10 non sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 sia scaduto
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C9 non sia  uguale a avanzamento
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T5 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a avanzamentox
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co10 sia  minore di  /*55,*/ 110
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  diverso da avanzamentox


 } Verifica che   /*47,48,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  uguale a avanzamentox
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  uguale a  /*53,*/ 4
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da avanzamentox
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,50,*/  /*,*/  la variabile MainClass_C1_variabile_V2 sia  maggiore di  /*54,*/ 3
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,50,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  minore di  /*55,*/ 3
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  maggiore di  /*54,*/ 153
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C9 sia  uguale a avanzamento
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V2 sia  uguale a  /*53,*/ 3
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C2 sia  uguale a avanzamentox


 } Verifica che   /*48,49,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V3 sia  uguale a c270xx
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 sia attivo
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C9 non sia  diverso da avanzamento
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co5 non sia  maggiore di  /*54,*/ 152
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co10 sia  minore di  /*55,*/ 12""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/  se la macro  MainClass_C1_macrova_M5 ( con argomento_a8   uguale a RossoGialloxVerdex ,argomento_a1   uguale a c270x ,argomento_a5   uguale a RossoVerde  e argomento_a2   uguale a c270x )  non  è  diverso da c270xx /*40,*/  /*36,*/ e  se il timer MainClass_C1_timer_T5 non è scaduto, Almeno una delle seguenti { 
 /*61,*/ /*35,*/  se il controllo MainClass_C1_controllo_C2 non è  diverso da avanzamentox /*34,*/ e  se il parametro MainClass_C1_parametro_P4 è  diverso da avanzamentox, Tutte le seguenti { 
 /*63,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*35,*/ o  se il controllo MainClass_C1_controllo_C10 non è  diverso da  False , Solo una delle seguenti { 
 /*63,*/  se il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ /*36,*/ e  se il timer MainClass_C1_timer_T5 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T5 non è attivo, Solo una delle seguenti { 
 /*61,*/ /*37,*/  se la variabile MainClass_C1_variabile_V2 è  diverso da  /*56,*/ 4, Tutte le seguenti { 
 /*61,*/ /*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*37,*/ o  se la variabile MainClass_C1_variabile_V8 è  minore di  /*55,*/ 8, Tutte le seguenti { 
  se la macro  MainClass_C1_macrova_M6 ( con argomento_a8   uguale a RossoGialloaVerdea  e argomento_a1   uguale a RossoVerde )   è  uguale a  True  /*40,*/ , Verifica che   /*47,48,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  minore di  /*55,*/ 10
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  minore di  /*55,*/ 13325
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,49,*/  /*,*/  il controllo MainClass_C1_controllo_C10 non sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 sia scaduto
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C9 non sia  uguale a avanzamento
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T5 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a avanzamentox
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co10 sia  minore di  /*55,*/ 110
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  diverso da avanzamentox


 } Verifica che   /*47,48,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  uguale a avanzamentox
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  uguale a  /*53,*/ 4
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da avanzamentox
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,50,*/  /*,*/  la variabile MainClass_C1_variabile_V2 sia  maggiore di  /*54,*/ 3
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,50,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  minore di  /*55,*/ 3
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  maggiore di  /*54,*/ 153
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C9 sia  uguale a avanzamento
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V2 sia  uguale a  /*53,*/ 3
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C2 sia  uguale a avanzamentox


 }""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/  se la macro  MainClass_C1_macrova_M5 ( con argomento_a8   uguale a RossoGialloxVerdex ,argomento_a1   uguale a c270x ,argomento_a5   uguale a RossoVerde  e argomento_a2   uguale a c270x )  non  è  diverso da c270xx /*40,*/  /*36,*/ e  se il timer MainClass_C1_timer_T5 non è scaduto""", [
                            DIBoolExpr("""Operatore Logico Not\nla macro  MainClass_C1_macrova_M5 ( con argomento_a8   uguale a RossoGialloxVerdex ,argomento_a1   uguale a c270x ,argomento_a5   uguale a RossoVerde  e argomento_a2   uguale a c270x )  non  è  diverso da c270xx""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m5')  è uguale a  (c270xx))""", [
                            DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m5')  è uguale a  (c270xx)""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroMainclass_c1_macrova_m5'"""),#0
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T5 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t5' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*61,*/ /*35,*/  se il controllo MainClass_C1_controllo_C2 non è  diverso da avanzamentox /*34,*/ e  se il parametro MainClass_C1_parametro_P4 è  diverso da avanzamentox, Tutte le seguenti { 
 /*63,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*35,*/ o  se il controllo MainClass_C1_controllo_C10 non è  diverso da  False , Solo una delle seguenti { 
 /*63,*/  se il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ /*36,*/ e  se il timer MainClass_C1_timer_T5 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T5 non è attivo, Solo una delle seguenti { 
 /*61,*/ /*37,*/  se la variabile MainClass_C1_variabile_V2 è  diverso da  /*56,*/ 4, Tutte le seguenti { 
 /*61,*/ /*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*37,*/ o  se la variabile MainClass_C1_variabile_V8 è  minore di  /*55,*/ 8, Tutte le seguenti { 
  se la macro  MainClass_C1_macrova_M6 ( con argomento_a8   uguale a RossoGialloaVerdea  e argomento_a1   uguale a RossoVerde )   è  uguale a  True  /*40,*/ , Verifica che   /*47,48,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  minore di  /*55,*/ 10
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  minore di  /*55,*/ 13325
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,49,*/  /*,*/  il controllo MainClass_C1_controllo_C10 non sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 sia scaduto
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C9 non sia  uguale a avanzamento
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T5 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a avanzamentox
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co10 sia  minore di  /*55,*/ 110
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  diverso da avanzamentox


 } Verifica che   /*47,48,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  uguale a avanzamentox
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  uguale a  /*53,*/ 4
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da avanzamentox
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,50,*/  /*,*/  la variabile MainClass_C1_variabile_V2 sia  maggiore di  /*54,*/ 3
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,50,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  minore di  /*55,*/ 3
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  maggiore di  /*54,*/ 153
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C9 sia  uguale a avanzamento
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V2 sia  uguale a  /*53,*/ 3
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C2 sia  uguale a avanzamentox


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*35,*/  se il controllo MainClass_C1_controllo_C2 non è  diverso da avanzamentox /*34,*/ e  se il parametro MainClass_C1_parametro_P4 è  diverso da avanzamentox, Tutte le seguenti { 
 /*63,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*35,*/ o  se il controllo MainClass_C1_controllo_C10 non è  diverso da  False , Solo una delle seguenti { 
 /*63,*/  se il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ /*36,*/ e  se il timer MainClass_C1_timer_T5 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T5 non è attivo, Solo una delle seguenti { 
 /*61,*/ /*37,*/  se la variabile MainClass_C1_variabile_V2 è  diverso da  /*56,*/ 4, Tutte le seguenti { 
 /*61,*/ /*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*37,*/ o  se la variabile MainClass_C1_variabile_V8 è  minore di  /*55,*/ 8, Tutte le seguenti { 
  se la macro  MainClass_C1_macrova_M6 ( con argomento_a8   uguale a RossoGialloaVerdea  e argomento_a1   uguale a RossoVerde )   è  uguale a  True  /*40,*/ , Verifica che   /*47,48,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  minore di  /*55,*/ 10
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  minore di  /*55,*/ 13325
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,49,*/  /*,*/  il controllo MainClass_C1_controllo_C10 non sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 sia scaduto
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C9 non sia  uguale a avanzamento
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T5 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a avanzamentox
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co10 sia  minore di  /*55,*/ 110
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  diverso da avanzamentox


 } Verifica che   /*47,48,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  uguale a avanzamentox
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  uguale a  /*53,*/ 4
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da avanzamentox
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,50,*/  /*,*/  la variabile MainClass_C1_variabile_V2 sia  maggiore di  /*54,*/ 3
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*35,*/  se il controllo MainClass_C1_controllo_C2 non è  diverso da avanzamentox /*34,*/ e  se il parametro MainClass_C1_parametro_P4 è  diverso da avanzamentox""", [
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C2 non è  diverso da avanzamentox""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c2)  è uguale a  (avanzamentox))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c2)  è uguale a  (avanzamentox)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P4 è  diverso da avanzamentox""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p4)  è uguale a  (avanzamentox)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*63,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*35,*/ o  se il controllo MainClass_C1_controllo_C10 non è  diverso da  False , Solo una delle seguenti { 
 /*63,*/  se il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ /*36,*/ e  se il timer MainClass_C1_timer_T5 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T5 non è attivo, Solo una delle seguenti { 
 /*61,*/ /*37,*/  se la variabile MainClass_C1_variabile_V2 è  diverso da  /*56,*/ 4, Tutte le seguenti { 
 /*61,*/ /*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*37,*/ o  se la variabile MainClass_C1_variabile_V8 è  minore di  /*55,*/ 8, Tutte le seguenti { 
  se la macro  MainClass_C1_macrova_M6 ( con argomento_a8   uguale a RossoGialloaVerdea  e argomento_a1   uguale a RossoVerde )   è  uguale a  True  /*40,*/ , Verifica che   /*47,48,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  minore di  /*55,*/ 10
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  minore di  /*55,*/ 13325
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,49,*/  /*,*/  il controllo MainClass_C1_controllo_C10 non sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 sia scaduto
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C9 non sia  uguale a avanzamento
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T5 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a avanzamentox
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co10 sia  minore di  /*55,*/ 110
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  diverso da avanzamentox


 } Verifica che   /*47,48,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  uguale a avanzamentox
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  uguale a  /*53,*/ 4
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da avanzamentox
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,50,*/  /*,*/  la variabile MainClass_C1_variabile_V2 sia  maggiore di  /*54,*/ 3
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*35,*/ o  se il controllo MainClass_C1_controllo_C10 non è  diverso da  False , Solo una delle seguenti { 
 /*63,*/  se il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ /*36,*/ e  se il timer MainClass_C1_timer_T5 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T5 non è attivo, Solo una delle seguenti { 
 /*61,*/ /*37,*/  se la variabile MainClass_C1_variabile_V2 è  diverso da  /*56,*/ 4, Tutte le seguenti { 
 /*61,*/ /*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*37,*/ o  se la variabile MainClass_C1_variabile_V8 è  minore di  /*55,*/ 8, Tutte le seguenti { 
  se la macro  MainClass_C1_macrova_M6 ( con argomento_a8   uguale a RossoGialloaVerdea  e argomento_a1   uguale a RossoVerde )   è  uguale a  True  /*40,*/ , Verifica che   /*47,48,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  minore di  /*55,*/ 10
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  minore di  /*55,*/ 13325
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,49,*/  /*,*/  il controllo MainClass_C1_controllo_C10 non sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 sia scaduto
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C9 non sia  uguale a avanzamento
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T5 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a avanzamentox
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co10 sia  minore di  /*55,*/ 110
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  diverso da avanzamentox


 } Verifica che   /*47,48,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  uguale a avanzamentox
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  uguale a  /*53,*/ 4
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da avanzamentox
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*35,*/ o  se il controllo MainClass_C1_controllo_C10 non è  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nlo stato  non è  uguale a  /*53,*/  state1""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C10 non è  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c10)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c10)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*63,*/  se il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ /*36,*/ e  se il timer MainClass_C1_timer_T5 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T5 non è attivo, Solo una delle seguenti { 
 /*61,*/ /*37,*/  se la variabile MainClass_C1_variabile_V2 è  diverso da  /*56,*/ 4, Tutte le seguenti { 
 /*61,*/ /*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*37,*/ o  se la variabile MainClass_C1_variabile_V8 è  minore di  /*55,*/ 8, Tutte le seguenti { 
  se la macro  MainClass_C1_macrova_M6 ( con argomento_a8   uguale a RossoGialloaVerdea  e argomento_a1   uguale a RossoVerde )   è  uguale a  True  /*40,*/ , Verifica che   /*47,48,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  minore di  /*55,*/ 10
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  minore di  /*55,*/ 13325
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,49,*/  /*,*/  il controllo MainClass_C1_controllo_C10 non sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 sia scaduto
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C9 non sia  uguale a avanzamento
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T5 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a avanzamentox
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co10 sia  minore di  /*55,*/ 110
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  diverso da avanzamentox


 } Verifica che   /*47,48,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  uguale a avanzamentox
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  uguale a  /*53,*/ 4
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da avanzamentox
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/  se il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ /*36,*/ e  se il timer MainClass_C1_timer_T5 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T5 non è attivo, Solo una delle seguenti { 
 /*61,*/ /*37,*/  se la variabile MainClass_C1_variabile_V2 è  diverso da  /*56,*/ 4, Tutte le seguenti { 
 /*61,*/ /*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*37,*/ o  se la variabile MainClass_C1_variabile_V8 è  minore di  /*55,*/ 8, Tutte le seguenti { 
  se la macro  MainClass_C1_macrova_M6 ( con argomento_a8   uguale a RossoGialloaVerdea  e argomento_a1   uguale a RossoVerde )   è  uguale a  True  /*40,*/ , Verifica che   /*47,48,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  minore di  /*55,*/ 10
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  minore di  /*55,*/ 13325
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,49,*/  /*,*/  il controllo MainClass_C1_controllo_C10 non sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 sia scaduto
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C9 non sia  uguale a avanzamento
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T5 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a avanzamentox
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co10 sia  minore di  /*55,*/ 110
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  diverso da avanzamentox


 }""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/  se il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ /*36,*/ e  se il timer MainClass_C1_timer_T5 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T5 non è attivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/  se il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ /*36,*/ e  se il timer MainClass_C1_timer_T5 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/  se il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ /*36,*/ e  se il timer MainClass_C1_timer_T5 non è scaduto""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino dello stato  non è  diverso da  /*56,*/  state1""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((stato_restore)  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(stato_restore)  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T5 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t5' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T5 non è attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t5' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*61,*/ /*37,*/  se la variabile MainClass_C1_variabile_V2 è  diverso da  /*56,*/ 4, Tutte le seguenti { 
 /*61,*/ /*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*37,*/ o  se la variabile MainClass_C1_variabile_V8 è  minore di  /*55,*/ 8, Tutte le seguenti { 
  se la macro  MainClass_C1_macrova_M6 ( con argomento_a8   uguale a RossoGialloaVerdea  e argomento_a1   uguale a RossoVerde )   è  uguale a  True  /*40,*/ , Verifica che   /*47,48,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  minore di  /*55,*/ 10
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  minore di  /*55,*/ 13325
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,49,*/  /*,*/  il controllo MainClass_C1_controllo_C10 non sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 sia scaduto
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C9 non sia  uguale a avanzamento
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T5 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a avanzamentox
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co10 sia  minore di  /*55,*/ 110
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  diverso da avanzamentox


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*37,*/  se la variabile MainClass_C1_variabile_V2 è  diverso da  /*56,*/ 4, Tutte le seguenti { 
 /*61,*/ /*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*37,*/ o  se la variabile MainClass_C1_variabile_V8 è  minore di  /*55,*/ 8, Tutte le seguenti { 
  se la macro  MainClass_C1_macrova_M6 ( con argomento_a8   uguale a RossoGialloaVerdea  e argomento_a1   uguale a RossoVerde )   è  uguale a  True  /*40,*/ , Verifica che   /*47,48,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  minore di  /*55,*/ 10
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  minore di  /*55,*/ 13325
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,49,*/  /*,*/  il controllo MainClass_C1_controllo_C10 non sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 sia scaduto
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C9 non sia  uguale a avanzamento
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T5 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a avanzamentox
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                            DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V2 è  diverso da  /*56,*/ 4""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v2)  è uguale a  (4)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*61,*/ /*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*37,*/ o  se la variabile MainClass_C1_variabile_V8 è  minore di  /*55,*/ 8, Tutte le seguenti { 
  se la macro  MainClass_C1_macrova_M6 ( con argomento_a8   uguale a RossoGialloaVerdea  e argomento_a1   uguale a RossoVerde )   è  uguale a  True  /*40,*/ , Verifica che   /*47,48,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  minore di  /*55,*/ 10
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  minore di  /*55,*/ 13325
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,49,*/  /*,*/  il controllo MainClass_C1_controllo_C10 non sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 sia scaduto
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C9 non sia  uguale a avanzamento
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T5 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a avanzamentox
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*37,*/ o  se la variabile MainClass_C1_variabile_V8 è  minore di  /*55,*/ 8, Tutte le seguenti { 
  se la macro  MainClass_C1_macrova_M6 ( con argomento_a8   uguale a RossoGialloaVerdea  e argomento_a1   uguale a RossoVerde )   è  uguale a  True  /*40,*/ , Verifica che   /*47,48,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  minore di  /*55,*/ 10
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  minore di  /*55,*/ 13325
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*37,*/ o  se la variabile MainClass_C1_variabile_V8 è  minore di  /*55,*/ 8""", [
                            DIBoolExpr("""Operatore Logico Not\nlo stato  non è  diverso da  /*56,*/  state1""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lo stato di 'self')  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nla variabile MainClass_C1_variabile_V8 è  minore di  /*55,*/ 8""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\nse la macro  MainClass_C1_macrova_M6 ( con argomento_a8   uguale a RossoGialloaVerdea  e argomento_a1   uguale a RossoVerde )   è  uguale a  True  /*40,*/ , Verifica che   /*47,48,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  minore di  /*55,*/ 10
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  minore di  /*55,*/ 13325
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""EqualImpl\nla macro  MainClass_C1_macrova_M6 ( con argomento_a8   uguale a RossoGialloaVerdea  e argomento_a1   uguale a RossoVerde )   è  uguale a  True""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroMainclass_c1_macrova_m6'"""),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  minore di  /*55,*/ 10
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  minore di  /*55,*/ 13325
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  minore di  /*55,*/ 10
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  minore di  /*55,*/ 13325""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  minore di  /*55,*/ 10""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_parametro_p9)  è minore di  (10)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  minore di  /*55,*/ 13325""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co10)  è minore di  (13325)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,*/  /*,*/  il controllo MainClass_C1_controllo_C10 non sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 sia scaduto
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C9 non sia  uguale a avanzamento
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T5 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a avanzamentox
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,*/  /*,*/  il controllo MainClass_C1_controllo_C10 non sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 sia scaduto
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C9 non sia  uguale a avanzamento""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,49,*/  /*,*/  il controllo MainClass_C1_controllo_C10 non sia  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c10)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il timer MainClass_C1_timer_T5 sia scaduto
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C9 non sia  uguale a avanzamento""", [
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer MainClass_C1_timer_T5 sia scaduto""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*35,*/  il controllo MainClass_C1_controllo_C9 non sia  uguale a avanzamento""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c9)  è uguale a  (avanzamento)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*36,*/  il timer MainClass_C1_timer_T5 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a avanzamentox
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*36,*/  il timer MainClass_C1_timer_T5 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a avanzamentox""", [
                            DIBoolExpr("""Predicato Oggetto\nche  /*36,*/  il timer MainClass_C1_timer_T5 sia scaduto""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a avanzamentox""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p4)  è uguale a  (avanzamentox)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co10 sia  minore di  /*55,*/ 110
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  diverso da avanzamentox""", [
                            DIBoolExpr("""LessThanImpl\nche   /*47,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co10 sia  minore di  /*55,*/ 110""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  diverso da avanzamentox""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p4)  è uguale a  (avanzamentox)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  uguale a avanzamentox
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  uguale a  /*53,*/ 4
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da avanzamentox
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  uguale a avanzamentox
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  uguale a  /*53,*/ 4""", [
                            DIBoolExpr("""EqualImpl\nche   /*47,48,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  uguale a avanzamentox""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  uguale a  /*53,*/ 4""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p9)  è uguale a  (4)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da avanzamentox
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da avanzamentox""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c2)  è uguale a  (avanzamentox))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c2)  è uguale a  (avanzamentox)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,50,*/  /*,*/  la variabile MainClass_C1_variabile_V2 sia  maggiore di  /*54,*/ 3
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,50,*/  /*,*/  la variabile MainClass_C1_variabile_V2 sia  maggiore di  /*54,*/ 3
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,50,*/  /*,*/  la variabile MainClass_C1_variabile_V2 sia  maggiore di  /*54,*/ 3
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""GreaterThanImpl\nche   /*48,50,*/  /*,*/  la variabile MainClass_C1_variabile_V2 sia  maggiore di  /*54,*/ 3""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  minore di  /*55,*/ 3
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  maggiore di  /*54,*/ 153
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C9 sia  uguale a avanzamento
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V2 sia  uguale a  /*53,*/ 3
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C2 sia  uguale a avanzamentox""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,50,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  minore di  /*55,*/ 3
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  maggiore di  /*54,*/ 153
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C9 sia  uguale a avanzamento
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V2 sia  uguale a  /*53,*/ 3""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,50,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  minore di  /*55,*/ 3
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  maggiore di  /*54,*/ 153
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C9 sia  uguale a avanzamento""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,50,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  minore di  /*55,*/ 3
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  maggiore di  /*54,*/ 153""", [
                            DIBoolExpr("""LessThanImpl\nche   /*47,48,50,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  minore di  /*55,*/ 3""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  maggiore di  /*54,*/ 153""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co10)  è maggiore di  (153)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  il controllo MainClass_C1_controllo_C9 sia  uguale a avanzamento""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  la variabile MainClass_C1_variabile_V2 sia  uguale a  /*53,*/ 3""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C2 sia  uguale a avanzamentox""", [
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*35,*/  il controllo MainClass_C1_controllo_C2 sia  uguale a avanzamentox""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V3 sia  uguale a c270xx
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 sia attivo
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C9 non sia  diverso da avanzamento
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co5 non sia  maggiore di  /*54,*/ 152
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co10 sia  minore di  /*55,*/ 12""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V3 sia  uguale a c270xx
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 sia attivo
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C9 non sia  diverso da avanzamento""", [
                            DIBoolExpr("""EqualImpl\nche   /*48,49,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V3 sia  uguale a c270xx""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il timer MainClass_C1_timer_T5 sia attivo
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C9 non sia  diverso da avanzamento""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il timer MainClass_C1_timer_T5 sia attivo
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer MainClass_C1_timer_T5 sia attivo""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo MainClass_C1_controllo_C9 non sia  diverso da avanzamento""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c9)  è uguale a  (avanzamento))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c9)  è uguale a  (avanzamento)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il contatore MainClass_C1_contatore_Co5 non sia  maggiore di  /*54,*/ 152
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co10 sia  minore di  /*55,*/ 12""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore MainClass_C1_contatore_Co5 non sia  maggiore di  /*54,*/ 152""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co5)  è maggiore di  (152)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nche  /*38,*/  il contatore MainClass_C1_contatore_Co10 sia  minore di  /*55,*/ 12""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroMainclass_c1_macrove_m2_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db(not db(not db(db(self.macroMainclass_c1_macrova_m5(GlobalEnumeration.c270x,GlobalEnumeration.c270x,GlobalEnumeration.rossoverde,GlobalEnumeration.rossogialloxverdex, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_timer_t5().isScaduto(), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db((db(not db(not db(self.get_mainclass_c1_controllo_c2() == GlobalEnumeration.avanzamentox, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p4() == GlobalEnumeration.avanzamentox, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_controllo_c10() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db((db((db((db(not db(not db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_timer_t5().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_timer_t5().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db(not db(self.get_mainclass_c1_variabile_v2() == 4, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db(not db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_variabile_v8() < 8, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db(db(self.macroMainclass_c1_macrova_m6(GlobalEnumeration.rossoverde,GlobalEnumeration.rossogialloaverdea, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db(not db(self.get_mainclass_c1_parametro_p9() < 10, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co10().get_valore() < 13325, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db((db((db(not db(self.get_mainclass_c1_controllo_c10() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db((db(self.get_mainclass_c1_timer_t5().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c9() == GlobalEnumeration.avanzamento, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db((db((db(self.get_mainclass_c1_timer_t5().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p4() == GlobalEnumeration.avanzamentox, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db((db(self.get_mainclass_c1_contatore_co10().get_valore() < 110, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(not db(self.get_mainclass_c1_parametro_p4() == GlobalEnumeration.avanzamentox, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db((db((db(self.get_mainclass_c1_parametro_p4() == GlobalEnumeration.avanzamentox, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p9() == 4, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db((db(not db(not db(self.get_mainclass_c1_controllo_c2() == GlobalEnumeration.avanzamentox, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) and db((db((db((db(self.get_mainclass_c1_variabile_v2() > 3, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0]) or db((db((db((db((db(self.get_mainclass_c1_parametro_p9() < 3, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co10().get_valore() > 153, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_controllo_c9() == GlobalEnumeration.avanzamento, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(self.get_mainclass_c1_variabile_v2() == 3, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) or db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(self.get_mainclass_c1_controllo_c2() == GlobalEnumeration.avanzamentox, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db((db(self.get_mainclass_c1_variabile_v3() == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[1].subs[0].subs[0]) or db((db((db(self.get_mainclass_c1_timer_t5().isAttivato(), di_ctx.subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_mainclass_c1_controllo_c9() == GlobalEnumeration.avanzamento, di_ctx.subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0]) or db((db(not db(self.get_mainclass_c1_contatore_co5().get_valore() > 152, di_ctx.subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[1].subs[0]) and db(self.get_mainclass_c1_contatore_co10().get_valore() < 12, di_ctx.subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    @srf_value_macro("macroMainclass_c1_macrove_m3")
    def macroMainclass_c1_macrove_m3(self, argomento_ave6, argomento_ave7, argomento_ave9, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        { commento: {62,} commento: {36,}  se il timer MainClass_C1_timer_T5 non è scaduto commento: {37,} e  se la variabile MainClass_C1_variabile_V2 è  diverso da  commento: {56,} 7 commento: {38,} o  se il contatore MainClass_C1_contatore_Co10 è  uguale a  commento: {53,} 1204, Almeno una delle seguenti { 
         commento: {62,} commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  uguale a avanzamento commento: {35,} o  se il controllo MainClass_C1_controllo_C2 non è  uguale a avanzamentox commento: {37,} e  se la variabile MainClass_C1_variabile_V2 non è  diverso da  commento: {56,} 8, Almeno una delle seguenti { 
         commento: {63,}  se l'argomento argomento_ave7 è  uguale a RossoVerde commento: {39,}  commento: {34,} o  se il parametro MainClass_C1_parametro_P9 è  uguale a  commento: {53,} 7, Solo una delle seguenti { 
         commento: {63,}  se il controllo ConsDef è uguale a FALSE  commento: {38,} e  se il contatore MainClass_C1_contatore_Co7 è  diverso da  commento: {56,} 1213 commento: {37,} o  se la variabile MainClass_C1_variabile_V8 è  diverso da  commento: {56,} 7 e  se l'argomento argomento_ave7 è  uguale a RossoVerde commento: {39,}  commento: {35,} e  se il controllo MainClass_C1_controllo_C9 non è  uguale a avanzamento, Solo una delle seguenti { 
         commento: {61,} commento: {36,}  se il timer MainClass_C1_timer_T5 non è scaduto, Tutte le seguenti { 
         commento: {62,} commento: {37,}  se la variabile MainClass_C1_variabile_V3 è  uguale a c270xx, Almeno una delle seguenti { 
         commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI5 non è disattivo commento: {37,} e  se la variabile MainClass_C1_variabile_V2 è  maggiore di  commento: {54,} 5 commento: {35,} o  se il controllo MainClass_C1_controllo_C2 non è  diverso da avanzamentox commento: {38,} o  se il contatore MainClass_C1_contatore_Co10 è  maggiore di  commento: {54,} 122 commento: {34,} o  se il parametro MainClass_C1_parametro_P9 non è  diverso da  commento: {56,} 5, Verifica che   commento: {49,51,}  commento: {,}  il timer MainClass_C1_timer_T5 sia disattivo
         commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co5 sia  uguale a  commento: {53,} 15
        
        
         } Verifica che   commento: {47,49,50,52,}  commento: {,}  il timer MainClass_C1_timer_T5 non sia disattivo
         commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P5 non sia  uguale a  False 
         commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V3 non sia  diverso da c270xx
         commento: {104,} e  che   l'argomento argomento_ave7 non  sia  uguale a RossoVerde commento: {,} 
         commento: {104,} o  che   l'argomento argomento_ave6 sia  uguale a c270xx commento: {39,} 
        
        
         } Verifica che   commento: {47,49,51,52,}   l'argomento argomento_ave7 non  sia  uguale a RossoVerde commento: {,} 
         commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T5 non sia scaduto
         commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P1 non sia  diverso da  False 
         commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co7 sia  diverso da  commento: {56,} 11
         commento: {104,} e  che  commento: {38,}  il contatore MainClass_C1_contatore_Co10 non sia  uguale a  commento: {53,} 1
        
        
         } Verifica che   commento: {48,51,}  commento: {,}  il contatore MainClass_C1_contatore_Co10 sia  uguale a  commento: {53,} 12
         commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C2 non sia  diverso da avanzamentox
         commento: {104,} e  che  commento: {35,}  il controllo MainClass_C1_controllo_C2 non sia  diverso da avanzamentox
        
        
         } Verifica che   commento: {50,52,}   l'argomento argomento_ave7 sia  diverso da RossoVerde commento: {,} 
         commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V3 non sia  uguale a c270xx
         commento: {104,} e  che   l'argomento argomento_ave6 sia  diverso da c270xx commento: {39,} 
         commento: {104,} e  che  commento: {37,}  la variabile MainClass_C1_variabile_V3 sia  diverso da c270xx
        
        
         } Verifica che   commento: {47,49,50,52,}  commento: {34,}  il parametro MainClass_C1_parametro_P9 sia  diverso da  commento: {56,} 8
         commento: {104,} o  che   l'argomento argomento_ave7 non  sia  diverso da RossoVerde commento: {,} 
         commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V9 sia  uguale a avanzamento
         commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P9 sia  minore di  commento: {55,} 1
         commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T5 non sia disattivo
         commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P8 non sia  uguale a  True 
        
        
         } Verifica che   commento: {47,48,49,50,}  commento: {,}  il controllo MainClass_C1_controllo_C9 sia  uguale a avanzamento
         commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P4 non sia  diverso da avanzamentox
         commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V3 non sia  diverso da c270xx
         commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T5 non sia attivo
         commento: {104,} e  che  commento: {35,}  il controllo MainClass_C1_controllo_C7 sia  uguale a  True 
        
        
        }
        """
        def populate_macroMainclass_c1_macrove_m3_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*36,*/  se il timer MainClass_C1_timer_T5 non è scaduto /*37,*/ e  se la variabile MainClass_C1_variabile_V2 è  diverso da  /*56,*/ 7 /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 è  uguale a  /*53,*/ 1204, Almeno una delle seguenti { 
 /*62,*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  uguale a avanzamento /*35,*/ o  se il controllo MainClass_C1_controllo_C2 non è  uguale a avanzamentox /*37,*/ e  se la variabile MainClass_C1_variabile_V2 non è  diverso da  /*56,*/ 8, Almeno una delle seguenti { 
 /*63,*/  se l'argomento argomento_ave7 è  uguale a RossoVerde /*39,*/  /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  uguale a  /*53,*/ 7, Solo una delle seguenti { 
 /*63,*/  se il controllo ConsDef è uguale a FALSE  /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 è  diverso da  /*56,*/ 1213 /*37,*/ o  se la variabile MainClass_C1_variabile_V8 è  diverso da  /*56,*/ 7 e  se l'argomento argomento_ave7 è  uguale a RossoVerde /*39,*/  /*35,*/ e  se il controllo MainClass_C1_controllo_C9 non è  uguale a avanzamento, Solo una delle seguenti { 
 /*61,*/ /*36,*/  se il timer MainClass_C1_timer_T5 non è scaduto, Tutte le seguenti { 
 /*62,*/ /*37,*/  se la variabile MainClass_C1_variabile_V3 è  uguale a c270xx, Almeno una delle seguenti { 
 /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI5 non è disattivo /*37,*/ e  se la variabile MainClass_C1_variabile_V2 è  maggiore di  /*54,*/ 5 /*35,*/ o  se il controllo MainClass_C1_controllo_C2 non è  diverso da avanzamentox /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 è  maggiore di  /*54,*/ 122 /*34,*/ o  se il parametro MainClass_C1_parametro_P9 non è  diverso da  /*56,*/ 5, Verifica che   /*49,51,*/  /*,*/  il timer MainClass_C1_timer_T5 sia disattivo
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  uguale a  /*53,*/ 15


 } Verifica che   /*47,49,50,52,*/  /*,*/  il timer MainClass_C1_timer_T5 non sia disattivo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P5 non sia  uguale a  False 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V3 non sia  diverso da c270xx
 /*104,*/ e  che   l'argomento argomento_ave7 non  sia  uguale a RossoVerde /*,*/ 
 /*104,*/ o  che   l'argomento argomento_ave6 sia  uguale a c270xx /*39,*/ 


 } Verifica che   /*47,49,51,52,*/   l'argomento argomento_ave7 non  sia  uguale a RossoVerde /*,*/ 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  diverso da  /*56,*/ 11
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co10 non sia  uguale a  /*53,*/ 1


 } Verifica che   /*48,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co10 sia  uguale a  /*53,*/ 12
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da avanzamentox
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da avanzamentox


 } Verifica che   /*50,52,*/   l'argomento argomento_ave7 sia  diverso da RossoVerde /*,*/ 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V3 non sia  uguale a c270xx
 /*104,*/ e  che   l'argomento argomento_ave6 sia  diverso da c270xx /*39,*/ 
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V3 sia  diverso da c270xx


 } Verifica che   /*47,49,50,52,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  diverso da  /*56,*/ 8
 /*104,*/ o  che   l'argomento argomento_ave7 non  sia  diverso da RossoVerde /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V9 sia  uguale a avanzamento
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  minore di  /*55,*/ 1
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 non sia disattivo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  uguale a  True 


 } Verifica che   /*47,48,49,50,*/  /*,*/  il controllo MainClass_C1_controllo_C9 sia  uguale a avanzamento
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  diverso da avanzamentox
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V3 non sia  diverso da c270xx
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 non sia attivo
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a  True""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*36,*/  se il timer MainClass_C1_timer_T5 non è scaduto /*37,*/ e  se la variabile MainClass_C1_variabile_V2 è  diverso da  /*56,*/ 7 /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 è  uguale a  /*53,*/ 1204, Almeno una delle seguenti { 
 /*62,*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  uguale a avanzamento /*35,*/ o  se il controllo MainClass_C1_controllo_C2 non è  uguale a avanzamentox /*37,*/ e  se la variabile MainClass_C1_variabile_V2 non è  diverso da  /*56,*/ 8, Almeno una delle seguenti { 
 /*63,*/  se l'argomento argomento_ave7 è  uguale a RossoVerde /*39,*/  /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  uguale a  /*53,*/ 7, Solo una delle seguenti { 
 /*63,*/  se il controllo ConsDef è uguale a FALSE  /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 è  diverso da  /*56,*/ 1213 /*37,*/ o  se la variabile MainClass_C1_variabile_V8 è  diverso da  /*56,*/ 7 e  se l'argomento argomento_ave7 è  uguale a RossoVerde /*39,*/  /*35,*/ e  se il controllo MainClass_C1_controllo_C9 non è  uguale a avanzamento, Solo una delle seguenti { 
 /*61,*/ /*36,*/  se il timer MainClass_C1_timer_T5 non è scaduto, Tutte le seguenti { 
 /*62,*/ /*37,*/  se la variabile MainClass_C1_variabile_V3 è  uguale a c270xx, Almeno una delle seguenti { 
 /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI5 non è disattivo /*37,*/ e  se la variabile MainClass_C1_variabile_V2 è  maggiore di  /*54,*/ 5 /*35,*/ o  se il controllo MainClass_C1_controllo_C2 non è  diverso da avanzamentox /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 è  maggiore di  /*54,*/ 122 /*34,*/ o  se il parametro MainClass_C1_parametro_P9 non è  diverso da  /*56,*/ 5, Verifica che   /*49,51,*/  /*,*/  il timer MainClass_C1_timer_T5 sia disattivo
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  uguale a  /*53,*/ 15


 } Verifica che   /*47,49,50,52,*/  /*,*/  il timer MainClass_C1_timer_T5 non sia disattivo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P5 non sia  uguale a  False 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V3 non sia  diverso da c270xx
 /*104,*/ e  che   l'argomento argomento_ave7 non  sia  uguale a RossoVerde /*,*/ 
 /*104,*/ o  che   l'argomento argomento_ave6 sia  uguale a c270xx /*39,*/ 


 } Verifica che   /*47,49,51,52,*/   l'argomento argomento_ave7 non  sia  uguale a RossoVerde /*,*/ 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  diverso da  /*56,*/ 11
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co10 non sia  uguale a  /*53,*/ 1


 } Verifica che   /*48,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co10 sia  uguale a  /*53,*/ 12
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da avanzamentox
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da avanzamentox


 } Verifica che   /*50,52,*/   l'argomento argomento_ave7 sia  diverso da RossoVerde /*,*/ 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V3 non sia  uguale a c270xx
 /*104,*/ e  che   l'argomento argomento_ave6 sia  diverso da c270xx /*39,*/ 
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V3 sia  diverso da c270xx


 } Verifica che   /*47,49,50,52,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  diverso da  /*56,*/ 8
 /*104,*/ o  che   l'argomento argomento_ave7 non  sia  diverso da RossoVerde /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V9 sia  uguale a avanzamento
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  minore di  /*55,*/ 1
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 non sia disattivo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  uguale a  True 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*36,*/  se il timer MainClass_C1_timer_T5 non è scaduto /*37,*/ e  se la variabile MainClass_C1_variabile_V2 è  diverso da  /*56,*/ 7 /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 è  uguale a  /*53,*/ 1204""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*36,*/  se il timer MainClass_C1_timer_T5 non è scaduto /*37,*/ e  se la variabile MainClass_C1_variabile_V2 è  diverso da  /*56,*/ 7""", [
                            DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T5 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t5' è scaduto""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V2 è  diverso da  /*56,*/ 7""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v2)  è uguale a  (7)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil contatore MainClass_C1_contatore_Co10 è  uguale a  /*53,*/ 1204""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*62,*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  uguale a avanzamento /*35,*/ o  se il controllo MainClass_C1_controllo_C2 non è  uguale a avanzamentox /*37,*/ e  se la variabile MainClass_C1_variabile_V2 non è  diverso da  /*56,*/ 8, Almeno una delle seguenti { 
 /*63,*/  se l'argomento argomento_ave7 è  uguale a RossoVerde /*39,*/  /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  uguale a  /*53,*/ 7, Solo una delle seguenti { 
 /*63,*/  se il controllo ConsDef è uguale a FALSE  /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 è  diverso da  /*56,*/ 1213 /*37,*/ o  se la variabile MainClass_C1_variabile_V8 è  diverso da  /*56,*/ 7 e  se l'argomento argomento_ave7 è  uguale a RossoVerde /*39,*/  /*35,*/ e  se il controllo MainClass_C1_controllo_C9 non è  uguale a avanzamento, Solo una delle seguenti { 
 /*61,*/ /*36,*/  se il timer MainClass_C1_timer_T5 non è scaduto, Tutte le seguenti { 
 /*62,*/ /*37,*/  se la variabile MainClass_C1_variabile_V3 è  uguale a c270xx, Almeno una delle seguenti { 
 /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI5 non è disattivo /*37,*/ e  se la variabile MainClass_C1_variabile_V2 è  maggiore di  /*54,*/ 5 /*35,*/ o  se il controllo MainClass_C1_controllo_C2 non è  diverso da avanzamentox /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 è  maggiore di  /*54,*/ 122 /*34,*/ o  se il parametro MainClass_C1_parametro_P9 non è  diverso da  /*56,*/ 5, Verifica che   /*49,51,*/  /*,*/  il timer MainClass_C1_timer_T5 sia disattivo
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  uguale a  /*53,*/ 15


 } Verifica che   /*47,49,50,52,*/  /*,*/  il timer MainClass_C1_timer_T5 non sia disattivo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P5 non sia  uguale a  False 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V3 non sia  diverso da c270xx
 /*104,*/ e  che   l'argomento argomento_ave7 non  sia  uguale a RossoVerde /*,*/ 
 /*104,*/ o  che   l'argomento argomento_ave6 sia  uguale a c270xx /*39,*/ 


 } Verifica che   /*47,49,51,52,*/   l'argomento argomento_ave7 non  sia  uguale a RossoVerde /*,*/ 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  diverso da  /*56,*/ 11
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co10 non sia  uguale a  /*53,*/ 1


 } Verifica che   /*48,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co10 sia  uguale a  /*53,*/ 12
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da avanzamentox
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da avanzamentox


 } Verifica che   /*50,52,*/   l'argomento argomento_ave7 sia  diverso da RossoVerde /*,*/ 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V3 non sia  uguale a c270xx
 /*104,*/ e  che   l'argomento argomento_ave6 sia  diverso da c270xx /*39,*/ 
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V3 sia  diverso da c270xx


 } Verifica che   /*47,49,50,52,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  diverso da  /*56,*/ 8
 /*104,*/ o  che   l'argomento argomento_ave7 non  sia  diverso da RossoVerde /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V9 sia  uguale a avanzamento
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  minore di  /*55,*/ 1
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 non sia disattivo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  uguale a  True 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  uguale a avanzamento /*35,*/ o  se il controllo MainClass_C1_controllo_C2 non è  uguale a avanzamentox /*37,*/ e  se la variabile MainClass_C1_variabile_V2 non è  diverso da  /*56,*/ 8, Almeno una delle seguenti { 
 /*63,*/  se l'argomento argomento_ave7 è  uguale a RossoVerde /*39,*/  /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  uguale a  /*53,*/ 7, Solo una delle seguenti { 
 /*63,*/  se il controllo ConsDef è uguale a FALSE  /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 è  diverso da  /*56,*/ 1213 /*37,*/ o  se la variabile MainClass_C1_variabile_V8 è  diverso da  /*56,*/ 7 e  se l'argomento argomento_ave7 è  uguale a RossoVerde /*39,*/  /*35,*/ e  se il controllo MainClass_C1_controllo_C9 non è  uguale a avanzamento, Solo una delle seguenti { 
 /*61,*/ /*36,*/  se il timer MainClass_C1_timer_T5 non è scaduto, Tutte le seguenti { 
 /*62,*/ /*37,*/  se la variabile MainClass_C1_variabile_V3 è  uguale a c270xx, Almeno una delle seguenti { 
 /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI5 non è disattivo /*37,*/ e  se la variabile MainClass_C1_variabile_V2 è  maggiore di  /*54,*/ 5 /*35,*/ o  se il controllo MainClass_C1_controllo_C2 non è  diverso da avanzamentox /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 è  maggiore di  /*54,*/ 122 /*34,*/ o  se il parametro MainClass_C1_parametro_P9 non è  diverso da  /*56,*/ 5, Verifica che   /*49,51,*/  /*,*/  il timer MainClass_C1_timer_T5 sia disattivo
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  uguale a  /*53,*/ 15


 } Verifica che   /*47,49,50,52,*/  /*,*/  il timer MainClass_C1_timer_T5 non sia disattivo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P5 non sia  uguale a  False 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V3 non sia  diverso da c270xx
 /*104,*/ e  che   l'argomento argomento_ave7 non  sia  uguale a RossoVerde /*,*/ 
 /*104,*/ o  che   l'argomento argomento_ave6 sia  uguale a c270xx /*39,*/ 


 } Verifica che   /*47,49,51,52,*/   l'argomento argomento_ave7 non  sia  uguale a RossoVerde /*,*/ 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  diverso da  /*56,*/ 11
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co10 non sia  uguale a  /*53,*/ 1


 } Verifica che   /*48,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co10 sia  uguale a  /*53,*/ 12
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da avanzamentox
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da avanzamentox


 } Verifica che   /*50,52,*/   l'argomento argomento_ave7 sia  diverso da RossoVerde /*,*/ 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V3 non sia  uguale a c270xx
 /*104,*/ e  che   l'argomento argomento_ave6 sia  diverso da c270xx /*39,*/ 
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V3 sia  diverso da c270xx


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  uguale a avanzamento /*35,*/ o  se il controllo MainClass_C1_controllo_C2 non è  uguale a avanzamentox /*37,*/ e  se la variabile MainClass_C1_variabile_V2 non è  diverso da  /*56,*/ 8""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino della variabile  MainClass_C1_restoreva_RV1 non è  uguale a avanzamento""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_restoreva_rv1_restore)  è uguale a  (avanzamento)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo MainClass_C1_controllo_C2 non è  uguale a avanzamentox /*37,*/ e  se la variabile MainClass_C1_variabile_V2 non è  diverso da  /*56,*/ 8""", [
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C2 non è  uguale a avanzamentox""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c2)  è uguale a  (avanzamentox)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V2 non è  diverso da  /*56,*/ 8""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v2)  è uguale a  (8))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v2)  è uguale a  (8)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*63,*/  se l'argomento argomento_ave7 è  uguale a RossoVerde /*39,*/  /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  uguale a  /*53,*/ 7, Solo una delle seguenti { 
 /*63,*/  se il controllo ConsDef è uguale a FALSE  /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 è  diverso da  /*56,*/ 1213 /*37,*/ o  se la variabile MainClass_C1_variabile_V8 è  diverso da  /*56,*/ 7 e  se l'argomento argomento_ave7 è  uguale a RossoVerde /*39,*/  /*35,*/ e  se il controllo MainClass_C1_controllo_C9 non è  uguale a avanzamento, Solo una delle seguenti { 
 /*61,*/ /*36,*/  se il timer MainClass_C1_timer_T5 non è scaduto, Tutte le seguenti { 
 /*62,*/ /*37,*/  se la variabile MainClass_C1_variabile_V3 è  uguale a c270xx, Almeno una delle seguenti { 
 /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI5 non è disattivo /*37,*/ e  se la variabile MainClass_C1_variabile_V2 è  maggiore di  /*54,*/ 5 /*35,*/ o  se il controllo MainClass_C1_controllo_C2 non è  diverso da avanzamentox /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 è  maggiore di  /*54,*/ 122 /*34,*/ o  se il parametro MainClass_C1_parametro_P9 non è  diverso da  /*56,*/ 5, Verifica che   /*49,51,*/  /*,*/  il timer MainClass_C1_timer_T5 sia disattivo
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  uguale a  /*53,*/ 15


 } Verifica che   /*47,49,50,52,*/  /*,*/  il timer MainClass_C1_timer_T5 non sia disattivo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P5 non sia  uguale a  False 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V3 non sia  diverso da c270xx
 /*104,*/ e  che   l'argomento argomento_ave7 non  sia  uguale a RossoVerde /*,*/ 
 /*104,*/ o  che   l'argomento argomento_ave6 sia  uguale a c270xx /*39,*/ 


 } Verifica che   /*47,49,51,52,*/   l'argomento argomento_ave7 non  sia  uguale a RossoVerde /*,*/ 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  diverso da  /*56,*/ 11
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co10 non sia  uguale a  /*53,*/ 1


 } Verifica che   /*48,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co10 sia  uguale a  /*53,*/ 12
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da avanzamentox
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da avanzamentox


 } Verifica che   /*50,52,*/   l'argomento argomento_ave7 sia  diverso da RossoVerde /*,*/ 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V3 non sia  uguale a c270xx
 /*104,*/ e  che   l'argomento argomento_ave6 sia  diverso da c270xx /*39,*/ 
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V3 sia  diverso da c270xx


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/  se l'argomento argomento_ave7 è  uguale a RossoVerde /*39,*/  /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  uguale a  /*53,*/ 7, Solo una delle seguenti { 
 /*63,*/  se il controllo ConsDef è uguale a FALSE  /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 è  diverso da  /*56,*/ 1213 /*37,*/ o  se la variabile MainClass_C1_variabile_V8 è  diverso da  /*56,*/ 7 e  se l'argomento argomento_ave7 è  uguale a RossoVerde /*39,*/  /*35,*/ e  se il controllo MainClass_C1_controllo_C9 non è  uguale a avanzamento, Solo una delle seguenti { 
 /*61,*/ /*36,*/  se il timer MainClass_C1_timer_T5 non è scaduto, Tutte le seguenti { 
 /*62,*/ /*37,*/  se la variabile MainClass_C1_variabile_V3 è  uguale a c270xx, Almeno una delle seguenti { 
 /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI5 non è disattivo /*37,*/ e  se la variabile MainClass_C1_variabile_V2 è  maggiore di  /*54,*/ 5 /*35,*/ o  se il controllo MainClass_C1_controllo_C2 non è  diverso da avanzamentox /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 è  maggiore di  /*54,*/ 122 /*34,*/ o  se il parametro MainClass_C1_parametro_P9 non è  diverso da  /*56,*/ 5, Verifica che   /*49,51,*/  /*,*/  il timer MainClass_C1_timer_T5 sia disattivo
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  uguale a  /*53,*/ 15


 } Verifica che   /*47,49,50,52,*/  /*,*/  il timer MainClass_C1_timer_T5 non sia disattivo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P5 non sia  uguale a  False 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V3 non sia  diverso da c270xx
 /*104,*/ e  che   l'argomento argomento_ave7 non  sia  uguale a RossoVerde /*,*/ 
 /*104,*/ o  che   l'argomento argomento_ave6 sia  uguale a c270xx /*39,*/ 


 } Verifica che   /*47,49,51,52,*/   l'argomento argomento_ave7 non  sia  uguale a RossoVerde /*,*/ 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  diverso da  /*56,*/ 11
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co10 non sia  uguale a  /*53,*/ 1


 } Verifica che   /*48,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co10 sia  uguale a  /*53,*/ 12
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da avanzamentox
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da avanzamentox


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/  se l'argomento argomento_ave7 è  uguale a RossoVerde /*39,*/  /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  uguale a  /*53,*/ 7""", [
                            DIBoolExpr("""EqualImpl\nl'argomento argomento_ave7 è  uguale a RossoVerde""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil parametro MainClass_C1_parametro_P9 è  uguale a  /*53,*/ 7""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*63,*/  se il controllo ConsDef è uguale a FALSE  /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 è  diverso da  /*56,*/ 1213 /*37,*/ o  se la variabile MainClass_C1_variabile_V8 è  diverso da  /*56,*/ 7 e  se l'argomento argomento_ave7 è  uguale a RossoVerde /*39,*/  /*35,*/ e  se il controllo MainClass_C1_controllo_C9 non è  uguale a avanzamento, Solo una delle seguenti { 
 /*61,*/ /*36,*/  se il timer MainClass_C1_timer_T5 non è scaduto, Tutte le seguenti { 
 /*62,*/ /*37,*/  se la variabile MainClass_C1_variabile_V3 è  uguale a c270xx, Almeno una delle seguenti { 
 /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI5 non è disattivo /*37,*/ e  se la variabile MainClass_C1_variabile_V2 è  maggiore di  /*54,*/ 5 /*35,*/ o  se il controllo MainClass_C1_controllo_C2 non è  diverso da avanzamentox /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 è  maggiore di  /*54,*/ 122 /*34,*/ o  se il parametro MainClass_C1_parametro_P9 non è  diverso da  /*56,*/ 5, Verifica che   /*49,51,*/  /*,*/  il timer MainClass_C1_timer_T5 sia disattivo
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  uguale a  /*53,*/ 15


 } Verifica che   /*47,49,50,52,*/  /*,*/  il timer MainClass_C1_timer_T5 non sia disattivo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P5 non sia  uguale a  False 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V3 non sia  diverso da c270xx
 /*104,*/ e  che   l'argomento argomento_ave7 non  sia  uguale a RossoVerde /*,*/ 
 /*104,*/ o  che   l'argomento argomento_ave6 sia  uguale a c270xx /*39,*/ 


 } Verifica che   /*47,49,51,52,*/   l'argomento argomento_ave7 non  sia  uguale a RossoVerde /*,*/ 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  diverso da  /*56,*/ 11
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co10 non sia  uguale a  /*53,*/ 1


 } Verifica che   /*48,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co10 sia  uguale a  /*53,*/ 12
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da avanzamentox
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da avanzamentox


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/  se il controllo ConsDef è uguale a FALSE  /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 è  diverso da  /*56,*/ 1213 /*37,*/ o  se la variabile MainClass_C1_variabile_V8 è  diverso da  /*56,*/ 7 e  se l'argomento argomento_ave7 è  uguale a RossoVerde /*39,*/  /*35,*/ e  se il controllo MainClass_C1_controllo_C9 non è  uguale a avanzamento, Solo una delle seguenti { 
 /*61,*/ /*36,*/  se il timer MainClass_C1_timer_T5 non è scaduto, Tutte le seguenti { 
 /*62,*/ /*37,*/  se la variabile MainClass_C1_variabile_V3 è  uguale a c270xx, Almeno una delle seguenti { 
 /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI5 non è disattivo /*37,*/ e  se la variabile MainClass_C1_variabile_V2 è  maggiore di  /*54,*/ 5 /*35,*/ o  se il controllo MainClass_C1_controllo_C2 non è  diverso da avanzamentox /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 è  maggiore di  /*54,*/ 122 /*34,*/ o  se il parametro MainClass_C1_parametro_P9 non è  diverso da  /*56,*/ 5, Verifica che   /*49,51,*/  /*,*/  il timer MainClass_C1_timer_T5 sia disattivo
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  uguale a  /*53,*/ 15


 } Verifica che   /*47,49,50,52,*/  /*,*/  il timer MainClass_C1_timer_T5 non sia disattivo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P5 non sia  uguale a  False 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V3 non sia  diverso da c270xx
 /*104,*/ e  che   l'argomento argomento_ave7 non  sia  uguale a RossoVerde /*,*/ 
 /*104,*/ o  che   l'argomento argomento_ave6 sia  uguale a c270xx /*39,*/ 


 } Verifica che   /*47,49,51,52,*/   l'argomento argomento_ave7 non  sia  uguale a RossoVerde /*,*/ 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  diverso da  /*56,*/ 11
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co10 non sia  uguale a  /*53,*/ 1


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/  se il controllo ConsDef è uguale a FALSE  /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 è  diverso da  /*56,*/ 1213 /*37,*/ o  se la variabile MainClass_C1_variabile_V8 è  diverso da  /*56,*/ 7 e  se l'argomento argomento_ave7 è  uguale a RossoVerde /*39,*/  /*35,*/ e  se il controllo MainClass_C1_controllo_C9 non è  uguale a avanzamento""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/  se il controllo ConsDef è uguale a FALSE  /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 è  diverso da  /*56,*/ 1213""", [
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef è uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co7 è  diverso da  /*56,*/ 1213""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co7)  è uguale a  (1213)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse la variabile MainClass_C1_variabile_V8 è  diverso da  /*56,*/ 7 e  se l'argomento argomento_ave7 è  uguale a RossoVerde /*39,*/  /*35,*/ e  se il controllo MainClass_C1_controllo_C9 non è  uguale a avanzamento""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse la variabile MainClass_C1_variabile_V8 è  diverso da  /*56,*/ 7 e  se l'argomento argomento_ave7 è  uguale a RossoVerde""", [
                            DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V8 è  diverso da  /*56,*/ 7""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v8)  è uguale a  (7)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nl'argomento argomento_ave7 è  uguale a RossoVerde""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C9 non è  uguale a avanzamento""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c9)  è uguale a  (avanzamento)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*61,*/ /*36,*/  se il timer MainClass_C1_timer_T5 non è scaduto, Tutte le seguenti { 
 /*62,*/ /*37,*/  se la variabile MainClass_C1_variabile_V3 è  uguale a c270xx, Almeno una delle seguenti { 
 /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI5 non è disattivo /*37,*/ e  se la variabile MainClass_C1_variabile_V2 è  maggiore di  /*54,*/ 5 /*35,*/ o  se il controllo MainClass_C1_controllo_C2 non è  diverso da avanzamentox /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 è  maggiore di  /*54,*/ 122 /*34,*/ o  se il parametro MainClass_C1_parametro_P9 non è  diverso da  /*56,*/ 5, Verifica che   /*49,51,*/  /*,*/  il timer MainClass_C1_timer_T5 sia disattivo
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  uguale a  /*53,*/ 15


 } Verifica che   /*47,49,50,52,*/  /*,*/  il timer MainClass_C1_timer_T5 non sia disattivo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P5 non sia  uguale a  False 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V3 non sia  diverso da c270xx
 /*104,*/ e  che   l'argomento argomento_ave7 non  sia  uguale a RossoVerde /*,*/ 
 /*104,*/ o  che   l'argomento argomento_ave6 sia  uguale a c270xx /*39,*/ 


 } Verifica che   /*47,49,51,52,*/   l'argomento argomento_ave7 non  sia  uguale a RossoVerde /*,*/ 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  diverso da  /*56,*/ 11
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co10 non sia  uguale a  /*53,*/ 1


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*36,*/  se il timer MainClass_C1_timer_T5 non è scaduto, Tutte le seguenti { 
 /*62,*/ /*37,*/  se la variabile MainClass_C1_variabile_V3 è  uguale a c270xx, Almeno una delle seguenti { 
 /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI5 non è disattivo /*37,*/ e  se la variabile MainClass_C1_variabile_V2 è  maggiore di  /*54,*/ 5 /*35,*/ o  se il controllo MainClass_C1_controllo_C2 non è  diverso da avanzamentox /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 è  maggiore di  /*54,*/ 122 /*34,*/ o  se il parametro MainClass_C1_parametro_P9 non è  diverso da  /*56,*/ 5, Verifica che   /*49,51,*/  /*,*/  il timer MainClass_C1_timer_T5 sia disattivo
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  uguale a  /*53,*/ 15


 } Verifica che   /*47,49,50,52,*/  /*,*/  il timer MainClass_C1_timer_T5 non sia disattivo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P5 non sia  uguale a  False 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V3 non sia  diverso da c270xx
 /*104,*/ e  che   l'argomento argomento_ave7 non  sia  uguale a RossoVerde /*,*/ 
 /*104,*/ o  che   l'argomento argomento_ave6 sia  uguale a c270xx /*39,*/ 


 }""", [
                            DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T5 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t5' è scaduto""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*62,*/ /*37,*/  se la variabile MainClass_C1_variabile_V3 è  uguale a c270xx, Almeno una delle seguenti { 
 /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI5 non è disattivo /*37,*/ e  se la variabile MainClass_C1_variabile_V2 è  maggiore di  /*54,*/ 5 /*35,*/ o  se il controllo MainClass_C1_controllo_C2 non è  diverso da avanzamentox /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 è  maggiore di  /*54,*/ 122 /*34,*/ o  se il parametro MainClass_C1_parametro_P9 non è  diverso da  /*56,*/ 5, Verifica che   /*49,51,*/  /*,*/  il timer MainClass_C1_timer_T5 sia disattivo
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  uguale a  /*53,*/ 15


 } Verifica che   /*47,49,50,52,*/  /*,*/  il timer MainClass_C1_timer_T5 non sia disattivo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P5 non sia  uguale a  False 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V3 non sia  diverso da c270xx
 /*104,*/ e  che   l'argomento argomento_ave7 non  sia  uguale a RossoVerde /*,*/ 
 /*104,*/ o  che   l'argomento argomento_ave6 sia  uguale a c270xx /*39,*/ 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*37,*/  se la variabile MainClass_C1_variabile_V3 è  uguale a c270xx, Almeno una delle seguenti { 
 /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI5 non è disattivo /*37,*/ e  se la variabile MainClass_C1_variabile_V2 è  maggiore di  /*54,*/ 5 /*35,*/ o  se il controllo MainClass_C1_controllo_C2 non è  diverso da avanzamentox /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 è  maggiore di  /*54,*/ 122 /*34,*/ o  se il parametro MainClass_C1_parametro_P9 non è  diverso da  /*56,*/ 5, Verifica che   /*49,51,*/  /*,*/  il timer MainClass_C1_timer_T5 sia disattivo
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  uguale a  /*53,*/ 15


 }""", [
                            DIBoolExpr("""EqualImpl\nla variabile MainClass_C1_variabile_V3 è  uguale a c270xx""", [
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI5 non è disattivo /*37,*/ e  se la variabile MainClass_C1_variabile_V2 è  maggiore di  /*54,*/ 5 /*35,*/ o  se il controllo MainClass_C1_controllo_C2 non è  diverso da avanzamentox /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 è  maggiore di  /*54,*/ 122 /*34,*/ o  se il parametro MainClass_C1_parametro_P9 non è  diverso da  /*56,*/ 5, Verifica che   /*49,51,*/  /*,*/  il timer MainClass_C1_timer_T5 sia disattivo
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  uguale a  /*53,*/ 15""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI5 non è disattivo /*37,*/ e  se la variabile MainClass_C1_variabile_V2 è  maggiore di  /*54,*/ 5 /*35,*/ o  se il controllo MainClass_C1_controllo_C2 non è  diverso da avanzamentox /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 è  maggiore di  /*54,*/ 122 /*34,*/ o  se il parametro MainClass_C1_parametro_P9 non è  diverso da  /*56,*/ 5""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI5 non è disattivo /*37,*/ e  se la variabile MainClass_C1_variabile_V2 è  maggiore di  /*54,*/ 5 /*35,*/ o  se il controllo MainClass_C1_controllo_C2 non è  diverso da avanzamentox /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 è  maggiore di  /*54,*/ 122""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI5 non è disattivo /*37,*/ e  se la variabile MainClass_C1_variabile_V2 è  maggiore di  /*54,*/ 5 /*35,*/ o  se il controllo MainClass_C1_controllo_C2 non è  diverso da avanzamentox""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI5 non è disattivo /*37,*/ e  se la variabile MainClass_C1_variabile_V2 è  maggiore di  /*54,*/ 5""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino del timer  MainClass_C1_restoreTI_TI5 non è disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_restoreti_ti5_restore' è inattivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nla variabile MainClass_C1_variabile_V2 è  maggiore di  /*54,*/ 5""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C2 non è  diverso da avanzamentox""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c2)  è uguale a  (avanzamentox))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c2)  è uguale a  (avanzamentox)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nil contatore MainClass_C1_contatore_Co10 è  maggiore di  /*54,*/ 122""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P9 non è  diverso da  /*56,*/ 5""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p9)  è uguale a  (5))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p9)  è uguale a  (5)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*49,51,*/  /*,*/  il timer MainClass_C1_timer_T5 sia disattivo
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  uguale a  /*53,*/ 15""", [
                            DIBoolExpr("""Predicato Oggetto\nche   /*49,51,*/  /*,*/  il timer MainClass_C1_timer_T5 sia disattivo""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  uguale a  /*53,*/ 15""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,50,52,*/  /*,*/  il timer MainClass_C1_timer_T5 non sia disattivo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P5 non sia  uguale a  False 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V3 non sia  diverso da c270xx
 /*104,*/ e  che   l'argomento argomento_ave7 non  sia  uguale a RossoVerde /*,*/ 
 /*104,*/ o  che   l'argomento argomento_ave6 sia  uguale a c270xx""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,49,50,52,*/  /*,*/  il timer MainClass_C1_timer_T5 non sia disattivo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P5 non sia  uguale a  False 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V3 non sia  diverso da c270xx
 /*104,*/ e  che   l'argomento argomento_ave7 non  sia  uguale a RossoVerde""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,49,50,52,*/  /*,*/  il timer MainClass_C1_timer_T5 non sia disattivo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P5 non sia  uguale a  False 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V3 non sia  diverso da c270xx""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,49,50,52,*/  /*,*/  il timer MainClass_C1_timer_T5 non sia disattivo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P5 non sia  uguale a  False""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,49,50,52,*/  /*,*/  il timer MainClass_C1_timer_T5 non sia disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t5' è inattivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P5 non sia  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p5)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile MainClass_C1_variabile_V3 non sia  diverso da c270xx""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v3)  è uguale a  (c270xx))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v3)  è uguale a  (c270xx)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave7 non  sia  uguale a RossoVerde""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave7)  è uguale a  (rossoverde)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   l'argomento argomento_ave6 sia  uguale a c270xx""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,51,52,*/   l'argomento argomento_ave7 non  sia  uguale a RossoVerde /*,*/ 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  diverso da  /*56,*/ 11
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co10 non sia  uguale a  /*53,*/ 1""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,51,52,*/   l'argomento argomento_ave7 non  sia  uguale a RossoVerde /*,*/ 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,49,51,52,*/   l'argomento argomento_ave7 non  sia  uguale a RossoVerde""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave7)  è uguale a  (rossoverde)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t5' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  diverso da  /*56,*/ 11
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co10 non sia  uguale a  /*53,*/ 1""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  diverso da  /*56,*/ 11""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p1)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p1)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  diverso da  /*56,*/ 11""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co7)  è uguale a  (11)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*38,*/  il contatore MainClass_C1_contatore_Co10 non sia  uguale a  /*53,*/ 1""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co10)  è uguale a  (1)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co10 sia  uguale a  /*53,*/ 12
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da avanzamentox
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da avanzamentox""", [
                            DIBoolExpr("""EqualImpl\nche   /*48,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co10 sia  uguale a  /*53,*/ 12""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da avanzamentox
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da avanzamentox""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da avanzamentox""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c2)  è uguale a  (avanzamentox))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c2)  è uguale a  (avanzamentox)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*35,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da avanzamentox""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c2)  è uguale a  (avanzamentox))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c2)  è uguale a  (avanzamentox)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*50,52,*/   l'argomento argomento_ave7 sia  diverso da RossoVerde /*,*/ 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V3 non sia  uguale a c270xx
 /*104,*/ e  che   l'argomento argomento_ave6 sia  diverso da c270xx /*39,*/ 
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V3 sia  diverso da c270xx""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*50,52,*/   l'argomento argomento_ave7 sia  diverso da RossoVerde""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave7)  è uguale a  (rossoverde)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  la variabile MainClass_C1_variabile_V3 non sia  uguale a c270xx
 /*104,*/ e  che   l'argomento argomento_ave6 sia  diverso da c270xx /*39,*/ 
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V3 sia  diverso da c270xx""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  la variabile MainClass_C1_variabile_V3 non sia  uguale a c270xx
 /*104,*/ e  che   l'argomento argomento_ave6 sia  diverso da c270xx""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile MainClass_C1_variabile_V3 non sia  uguale a c270xx""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v3)  è uguale a  (c270xx)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave6 sia  diverso da c270xx""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave6)  è uguale a  (c270xx)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*37,*/  la variabile MainClass_C1_variabile_V3 sia  diverso da c270xx""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v3)  è uguale a  (c270xx)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,50,52,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  diverso da  /*56,*/ 8
 /*104,*/ o  che   l'argomento argomento_ave7 non  sia  diverso da RossoVerde /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V9 sia  uguale a avanzamento
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  minore di  /*55,*/ 1
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 non sia disattivo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,50,52,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  diverso da  /*56,*/ 8
 /*104,*/ o  che   l'argomento argomento_ave7 non  sia  diverso da RossoVerde /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V9 sia  uguale a avanzamento
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  minore di  /*55,*/ 1""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,50,52,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  diverso da  /*56,*/ 8
 /*104,*/ o  che   l'argomento argomento_ave7 non  sia  diverso da RossoVerde /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V9 sia  uguale a avanzamento""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,49,50,52,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  diverso da  /*56,*/ 8""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p9)  è uguale a  (8)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   l'argomento argomento_ave7 non  sia  diverso da RossoVerde /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V9 sia  uguale a avanzamento""", [
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave7 non  sia  diverso da RossoVerde""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_ave7)  è uguale a  (rossoverde))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave7)  è uguale a  (rossoverde)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  la variabile MainClass_C1_variabile_V9 sia  uguale a avanzamento""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nche  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  minore di  /*55,*/ 1""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il timer MainClass_C1_timer_T5 non sia disattivo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  uguale a  True""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il timer MainClass_C1_timer_T5 non sia disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t5' è inattivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p8)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,50,*/  /*,*/  il controllo MainClass_C1_controllo_C9 sia  uguale a avanzamento
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  diverso da avanzamentox
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V3 non sia  diverso da c270xx
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 non sia attivo
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,50,*/  /*,*/  il controllo MainClass_C1_controllo_C9 sia  uguale a avanzamento
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  diverso da avanzamentox
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V3 non sia  diverso da c270xx""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,49,50,*/  /*,*/  il controllo MainClass_C1_controllo_C9 sia  uguale a avanzamento
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  diverso da avanzamentox""", [
                            DIBoolExpr("""EqualImpl\nche   /*47,48,49,50,*/  /*,*/  il controllo MainClass_C1_controllo_C9 sia  uguale a avanzamento""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  diverso da avanzamentox""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p4)  è uguale a  (avanzamentox))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p4)  è uguale a  (avanzamentox)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile MainClass_C1_variabile_V3 non sia  diverso da c270xx""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v3)  è uguale a  (c270xx))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v3)  è uguale a  (c270xx)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il timer MainClass_C1_timer_T5 non sia attivo
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a  True""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il timer MainClass_C1_timer_T5 non sia attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t5' è attivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a  True""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroMainclass_c1_macrove_m3_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db(not db(self.get_mainclass_c1_timer_t5().isScaduto(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v2() == 7, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_contatore_co10().get_valore() == 1204, di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db((db(not db(self.get_mainclass_c1_restoreva_rv1_restore() == GlobalEnumeration.avanzamento, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_controllo_c2() == GlobalEnumeration.avanzamentox, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_mainclass_c1_variabile_v2() == 8, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db(argomento_ave7 == GlobalEnumeration.rossoverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_parametro_p9() == 7, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co7().get_valore() == 1213, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db((db(not db(self.get_mainclass_c1_variabile_v8() == 7, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(argomento_ave7 == GlobalEnumeration.rossoverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c9() == GlobalEnumeration.avanzamento, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db(not db(self.get_mainclass_c1_timer_t5().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_variabile_v3() == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db((db((db((db((db(not db(self.get_mainclass_c1_restoreti_ti5_restore().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_variabile_v2() > 5, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_controllo_c2() == GlobalEnumeration.avanzamentox, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_contatore_co10().get_valore() > 122, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_parametro_p9() == 5, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db(self.get_mainclass_c1_timer_t5().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) and db(self.get_mainclass_c1_contatore_co5().get_valore() == 15, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db((db((db((db((db(not db(self.get_mainclass_c1_timer_t5().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p5() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_variabile_v3() == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(not db(argomento_ave7 == GlobalEnumeration.rossoverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(argomento_ave6 == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db((db((db(not db(argomento_ave7 == GlobalEnumeration.rossoverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_timer_t5().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db((db((db(not db(not db(self.get_mainclass_c1_parametro_p1() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co7().get_valore() == 11, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co10().get_valore() == 1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db((db(self.get_mainclass_c1_contatore_co10().get_valore() == 12, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db((db(not db(not db(self.get_mainclass_c1_controllo_c2() == GlobalEnumeration.avanzamentox, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(not db(not db(self.get_mainclass_c1_controllo_c2() == GlobalEnumeration.avanzamentox, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db(not db(argomento_ave7 == GlobalEnumeration.rossoverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db((db((db(not db(self.get_mainclass_c1_variabile_v3() == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]) and db(not db(argomento_ave6 == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v3() == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0]) or db((db((db((db(not db(self.get_mainclass_c1_parametro_p9() == 8, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) or db((db(not db(not db(argomento_ave7 == GlobalEnumeration.rossoverde, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_variabile_v9() == GlobalEnumeration.avanzamento, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(self.get_mainclass_c1_parametro_p9() < 1, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) or db((db(not db(self.get_mainclass_c1_timer_t5().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p8() == True, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db((db((db(self.get_mainclass_c1_controllo_c9() == GlobalEnumeration.avanzamento, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_parametro_p4() == GlobalEnumeration.avanzamentox, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_variabile_v3() == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0]) or db((db(not db(self.get_mainclass_c1_timer_t5().isAttivato(), di_ctx.subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[1].subs[0]) and db(self.get_mainclass_c1_controllo_c7() == True, di_ctx.subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    @srf_value_macro("macroMainclass_c1_macrove_m8")
    def macroMainclass_c1_macrove_m8(self, argomento_ave1, argomento_ave5, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        {  se la macro  MainClass_C1_macrova_M5 ( con argomento_a8   uguale a c270xx ,argomento_a1   uguale a avanzamento ,argomento_a5   uguale a RossoVerde  e argomento_a2   uguale a avanzamento )  non  è  uguale a c270xx commento: {40,}  commento: {37,} e  se la variabile MainClass_C1_variabile_V8 è  uguale a  commento: {53,} 9 e  se l'argomento argomento_ave1 è  diverso da avanzamentox commento: {39,}  commento: {37,} e  se la variabile MainClass_C1_variabile_V2 non è  diverso da  commento: {56,} 4, Verifica che   commento: {47,51,52,}  commento: {34,}  il parametro MainClass_C1_parametro_P4 sia  uguale a avanzamentox
         commento: {104,} o  che  commento: {,}  il contatore MainClass_C1_contatore_Co10 non sia  diverso da  commento: {56,} 15132
         commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P9 non sia  minore di  commento: {55,} 10
         commento: {104,} e  che   l'argomento argomento_ave5 non  sia  diverso da avanzamento commento: {,} 
        
        
        }
        """
        def populate_macroMainclass_c1_macrove_m8_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\nse la macro  MainClass_C1_macrova_M5 ( con argomento_a8   uguale a c270xx ,argomento_a1   uguale a avanzamento ,argomento_a5   uguale a RossoVerde  e argomento_a2   uguale a avanzamento )  non  è  uguale a c270xx /*40,*/  /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  uguale a  /*53,*/ 9 e  se l'argomento argomento_ave1 è  diverso da avanzamentox /*39,*/  /*37,*/ e  se la variabile MainClass_C1_variabile_V2 non è  diverso da  /*56,*/ 4, Verifica che   /*47,51,52,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  uguale a avanzamentox
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  diverso da  /*56,*/ 15132
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  minore di  /*55,*/ 10
 /*104,*/ e  che   l'argomento argomento_ave5 non  sia  diverso da avanzamento""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\nse la macro  MainClass_C1_macrova_M5 ( con argomento_a8   uguale a c270xx ,argomento_a1   uguale a avanzamento ,argomento_a5   uguale a RossoVerde  e argomento_a2   uguale a avanzamento )  non  è  uguale a c270xx /*40,*/  /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  uguale a  /*53,*/ 9 e  se l'argomento argomento_ave1 è  diverso da avanzamentox /*39,*/  /*37,*/ e  se la variabile MainClass_C1_variabile_V2 non è  diverso da  /*56,*/ 4, Verifica che   /*47,51,52,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  uguale a avanzamentox
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  diverso da  /*56,*/ 15132
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  minore di  /*55,*/ 10
 /*104,*/ e  che   l'argomento argomento_ave5 non  sia  diverso da avanzamento""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse la macro  MainClass_C1_macrova_M5 ( con argomento_a8   uguale a c270xx ,argomento_a1   uguale a avanzamento ,argomento_a5   uguale a RossoVerde  e argomento_a2   uguale a avanzamento )  non  è  uguale a c270xx /*40,*/  /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  uguale a  /*53,*/ 9 e  se l'argomento argomento_ave1 è  diverso da avanzamentox /*39,*/  /*37,*/ e  se la variabile MainClass_C1_variabile_V2 non è  diverso da  /*56,*/ 4""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse la macro  MainClass_C1_macrova_M5 ( con argomento_a8   uguale a c270xx ,argomento_a1   uguale a avanzamento ,argomento_a5   uguale a RossoVerde  e argomento_a2   uguale a avanzamento )  non  è  uguale a c270xx /*40,*/  /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  uguale a  /*53,*/ 9 e  se l'argomento argomento_ave1 è  diverso da avanzamentox""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse la macro  MainClass_C1_macrova_M5 ( con argomento_a8   uguale a c270xx ,argomento_a1   uguale a avanzamento ,argomento_a5   uguale a RossoVerde  e argomento_a2   uguale a avanzamento )  non  è  uguale a c270xx /*40,*/  /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  uguale a  /*53,*/ 9""", [
                            DIBoolExpr("""Operatore Logico Not\nla macro  MainClass_C1_macrova_M5 ( con argomento_a8   uguale a c270xx ,argomento_a1   uguale a avanzamento ,argomento_a5   uguale a RossoVerde  e argomento_a2   uguale a avanzamento )  non  è  uguale a c270xx""", [
                            DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m5')  è uguale a  (c270xx)""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroMainclass_c1_macrova_m5'"""),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nla variabile MainClass_C1_variabile_V8 è  uguale a  /*53,*/ 9""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave1 è  diverso da avanzamentox""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave1)  è uguale a  (avanzamentox)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V2 non è  diverso da  /*56,*/ 4""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v2)  è uguale a  (4))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v2)  è uguale a  (4)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,51,52,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  uguale a avanzamentox
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  diverso da  /*56,*/ 15132
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  minore di  /*55,*/ 10
 /*104,*/ e  che   l'argomento argomento_ave5 non  sia  diverso da avanzamento""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,51,52,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  uguale a avanzamentox
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  diverso da  /*56,*/ 15132""", [
                            DIBoolExpr("""EqualImpl\nche   /*47,51,52,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  uguale a avanzamentox""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  diverso da  /*56,*/ 15132""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co10)  è uguale a  (15132))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co10)  è uguale a  (15132)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  minore di  /*55,*/ 10
 /*104,*/ e  che   l'argomento argomento_ave5 non  sia  diverso da avanzamento""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  minore di  /*55,*/ 10""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_parametro_p9)  è minore di  (10)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave5 non  sia  diverso da avanzamento""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_ave5)  è uguale a  (avanzamento))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave5)  è uguale a  (avanzamento)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macrove_m8_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db((db(not db(db(self.macroMainclass_c1_macrova_m5(GlobalEnumeration.avanzamento,GlobalEnumeration.avanzamento,GlobalEnumeration.rossoverde,GlobalEnumeration.c270xx, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_variabile_v8() == 9, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(argomento_ave1 == GlobalEnumeration.avanzamentox, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_variabile_v2() == 4, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db((db(self.get_mainclass_c1_parametro_p4() == GlobalEnumeration.avanzamentox, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_contatore_co10().get_valore() == 15132, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0]) or db((db(not db(self.get_mainclass_c1_parametro_p9() < 10, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) and db(not db(not db(argomento_ave5 == GlobalEnumeration.avanzamento, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0])), di_ctx.subs[0])
    
    # value macros
    @srf_value_macro("macroMainclass_c1_macrova_m1")
    def macroMainclass_c1_macrova_m1(self, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
         
        { commento: {[}
         commento: {46,} assegna alla macro il valore avanzamentox commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m1_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                ])

        populate_macroMainclass_c1_macrova_m1_SrfMacroDefInfo(di_ctx)
        
        #  /*[*/
        #   /*46,*/ assegna alla macro il valore avanzamentox
        return GlobalEnumeration.avanzamentox
    
    @srf_value_macro("macroMainclass_c1_macrova_m4")
    def macroMainclass_c1_macrova_m4(self, argomento_a10, argomento_a3, argomento_a4, argomento_a6, argomento_a7, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[} commento: {36,}  se il timer MainClass_C1_timer_T5 è scaduto e  se l'argomento argomento_a10 non  è  uguale a avanzamento commento: {39,}  o  se il controllo ConsDef è uguale a FALSE  commento: {38,} o  se il contatore MainClass_C1_contatore_Co5 è  minore di  commento: {55,} 15 commento: {35,} e  se il controllo MainClass_C1_controllo_C7 è  diverso da  True  commento: {109,} o  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  diverso da avanzamento , assegna alla macro il valore  True 
        
         commento: {46,} assegna alla macro il valore  True  commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m4_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/ /*36,*/  se il timer MainClass_C1_timer_T5 è scaduto e  se l'argomento argomento_a10 non  è  uguale a avanzamento /*39,*/  o  se il controllo ConsDef è uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 è  minore di  /*55,*/ 15 /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da  True  /*109,*/ o  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  diverso da avanzamento , assegna alla macro il valore  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*[*/ /*36,*/  se il timer MainClass_C1_timer_T5 è scaduto e  se l'argomento argomento_a10 non  è  uguale a avanzamento /*39,*/  o  se il controllo ConsDef è uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 è  minore di  /*55,*/ 15 /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da  True  /*109,*/ o  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  diverso da avanzamento""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( ( il timer 'mainclass_c1_timer_t5' è scaduto )  e  
( negazione di ((argomento_a10)  è uguale a  (avanzamento)) ) )  o  
( (consdef)  è uguale a  (False) ) )  o  
( ( (mainclass_c1_contatore_co5)  è minore di  (15) )  e  
( negazione di ((mainclass_c1_controllo_c7)  è uguale a  (True)) ) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( il timer 'mainclass_c1_timer_t5' è scaduto )  e  
( negazione di ((argomento_a10)  è uguale a  (avanzamento)) ) )  o  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( il timer 'mainclass_c1_timer_t5' è scaduto )  e  
( negazione di ((argomento_a10)  è uguale a  (avanzamento)) )""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t5' è scaduto""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_a10)  è uguale a  (avanzamento))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_a10)  è uguale a  (avanzamento)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( (mainclass_c1_contatore_co5)  è minore di  (15) )  e  
( negazione di ((mainclass_c1_controllo_c7)  è uguale a  (True)) )""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co5)  è minore di  (15)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c7)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_restoreva_rv1_restore)  è uguale a  (avanzamento)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_restoreva_rv1_restore)  è uguale a  (avanzamento))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_restoreva_rv1_restore)  è uguale a  (avanzamento)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macrova_m4_SrfMacroDefInfo(di_ctx)
        #  /*[*/ /*36,*/  se il timer MainClass_C1_timer_T5 è scaduto e  se l'argomento argomento_a10 non  è  uguale a avanzamento /*39,*/  o  se il controllo ConsDef è uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 è  minore di  /*55,*/ 15 /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da  True  /*109,*/ o  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  diverso da avanzamento , assegna alla macro il valore  True
        if db((db((db((db((db(self.get_mainclass_c1_timer_t5().isScaduto(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(argomento_a10 == GlobalEnumeration.avanzamento, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db((db(self.get_mainclass_c1_contatore_co5().get_valore() < 15, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c7() == True, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_restoreva_rv1_restore() == GlobalEnumeration.avanzamento, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            return True
        #  /*46,*/ assegna alla macro il valore  True
        return True
    
    @srf_value_macro("macroMainclass_c1_macrova_m5")
    def macroMainclass_c1_macrova_m5(self, argomento_a1, argomento_a2, argomento_a5, argomento_a8, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[} commento: {34,}  se lo stato  è  uguale a  commento: {53,}  state1  commento: {106,} , assegna alla macro il valore c270xx
        
         commento: {46,} assegna alla macro il valore c270xx commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m5_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ , assegna alla macro il valore c270xx""", [
                            DIBoolExpr("""EqualImpl\nlo stato  è  uguale a  /*53,*/  state1""", [
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macrova_m5_SrfMacroDefInfo(di_ctx)
        #  /*[*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ , assegna alla macro il valore c270xx
        if db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0]):
            return GlobalEnumeration.c270xx
        #  /*46,*/ assegna alla macro il valore c270xx
        return GlobalEnumeration.c270xx
    
    @srf_value_macro("macroMainclass_c1_macrova_m6")
    def macroMainclass_c1_macrova_m6(self, argomento_a1, argomento_a8, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[} commento: {37,}  se la variabile MainClass_C1_variabile_V3 è  uguale a c270xx o  se la macro  MainClass_C1_macrova_M1    è  uguale a avanzamentox commento: {40,}  e  se la macro  MainClass_C1_macrova_M1    è  diverso da avanzamentox commento: {40,}  , assegna alla macro il valore  True 
        
         commento: {46,} assegna alla macro il valore  False  commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m6_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/ /*37,*/  se la variabile MainClass_C1_variabile_V3 è  uguale a c270xx o  se la macro  MainClass_C1_macrova_M1    è  uguale a avanzamentox /*40,*/  e  se la macro  MainClass_C1_macrova_M1    è  diverso da avanzamentox /*40,*/  , assegna alla macro il valore  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*[*/ /*37,*/  se la variabile MainClass_C1_variabile_V3 è  uguale a c270xx o  se la macro  MainClass_C1_macrova_M1    è  uguale a avanzamentox /*40,*/  e  se la macro  MainClass_C1_macrova_M1    è  diverso da avanzamentox""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v3)  è uguale a  (c270xx)""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( (chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m1')  è uguale a  (avanzamentox) )  e  
( negazione di ((chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m1')  è uguale a  (avanzamentox)) )""", [
                            DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m1')  è uguale a  (avanzamentox)""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroMainclass_c1_macrova_m1'"""),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m1')  è uguale a  (avanzamentox))""", [
                            DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m1')  è uguale a  (avanzamentox)""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroMainclass_c1_macrova_m1'"""),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macrova_m6_SrfMacroDefInfo(di_ctx)
        #  /*[*/ /*37,*/  se la variabile MainClass_C1_variabile_V3 è  uguale a c270xx o  se la macro  MainClass_C1_macrova_M1    è  uguale a avanzamentox /*40,*/  e  se la macro  MainClass_C1_macrova_M1    è  diverso da avanzamentox /*40,*/  , assegna alla macro il valore  True
        if db((db(self.get_mainclass_c1_variabile_v3() == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[0].subs[0]) or db((db(db(self.macroMainclass_c1_macrova_m1(di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) == GlobalEnumeration.avanzamentox, di_ctx.subs[0].subs[0].subs[1].subs[0]) and db(not db(db(self.macroMainclass_c1_macrova_m1(di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]) == GlobalEnumeration.avanzamentox, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            return True
        #  /*46,*/ assegna alla macro il valore  False
        return False
    
    @srf_value_macro("macroMainclass_c1_macrova_m7")
    def macroMainclass_c1_macrova_m7(self, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
         
        { commento: {[} commento: {35,}  se il controllo MainClass_C1_controllo_C9 non è  uguale a avanzamento commento: {37,} e  se la variabile MainClass_C1_variabile_V10 non è  uguale a  False  , assegna alla macro il valore c270xx
        
         commento: {46,} assegna alla macro il valore c270xx commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m7_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/ /*35,*/  se il controllo MainClass_C1_controllo_C9 non è  uguale a avanzamento /*37,*/ e  se la variabile MainClass_C1_variabile_V10 non è  uguale a  False  , assegna alla macro il valore c270xx""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*[*/ /*35,*/  se il controllo MainClass_C1_controllo_C9 non è  uguale a avanzamento /*37,*/ e  se la variabile MainClass_C1_variabile_V10 non è  uguale a  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c9)  è uguale a  (avanzamento))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c9)  è uguale a  (avanzamento)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v10)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v10)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macrova_m7_SrfMacroDefInfo(di_ctx)
        #  /*[*/ /*35,*/  se il controllo MainClass_C1_controllo_C9 non è  uguale a avanzamento /*37,*/ e  se la variabile MainClass_C1_variabile_V10 non è  uguale a  False  , assegna alla macro il valore c270xx
        if db((db(not db(self.get_mainclass_c1_controllo_c9() == GlobalEnumeration.avanzamento, di_ctx.subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v10() == False, di_ctx.subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            return GlobalEnumeration.c270xx
        #  /*46,*/ assegna alla macro il valore c270xx
        return GlobalEnumeration.c270xx
    
    # for each manual command, the corresponding method is created
    def eventMainclass_c1_command_comm2(self, notifying_process):
        notifying_process.response_notify_man_cmd(self, 'eventMainclass_c1_command_comm2')
    
    # for each automatic command, the corresponding method is created

    def update_precedente(self):
        # update the variables with previous value
        self.set_mainclass_c1_previousco_c3_prev(self.get_mainclass_c1_previousco_c3())
        self.set_mainclass_c1_previousco_c5_prev(self.get_mainclass_c1_previousco_c5())
        self.set_mainclass_c1_previousco_c6_prev(self.get_mainclass_c1_previousco_c6())
        self.set_mainclass_c1_previousco_c8_prev(self.get_mainclass_c1_previousco_c8())
        self.set_mainclass_c1_previousva_pv1_prev(self.get_mainclass_c1_previousva_pv1())
        self.set_mainclass_c1_previousva_pv2_prev(self.get_mainclass_c1_previousva_pv2())
        self.set_mainclass_c1_previousva_pv3_prev(self.get_mainclass_c1_previousva_pv3())
        self.set_mainclass_c1_previousva_pv4_prev(self.get_mainclass_c1_previousva_pv4())

