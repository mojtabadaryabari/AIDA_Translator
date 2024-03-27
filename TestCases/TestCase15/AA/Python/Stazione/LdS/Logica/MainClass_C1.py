# Codice del modello 'TestCase15', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
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

        self.set_mainclass_c1_previousva_pv1(0)
        self.set_mainclass_c1_previousva_pv2(GlobalEnumeration.giallox)
        self.set_mainclass_c1_previousva_pv3(0)
        self.set_mainclass_c1_previousva_pv4(GlobalEnumeration.c180x)
        self.set_mainclass_c1_restoreva_rv1(False)
        self.set_mainclass_c1_restoreva_rv2(False)
        self.set_mainclass_c1_restoreva_rv3(False)
        self.set_mainclass_c1_restoreva_rv4(GlobalEnumeration.rossogiallo)
        self.set_mainclass_c1_variabile_v10(False)
        self.set_mainclass_c1_variabile_v9(False)

        self._expected_commands_map = {
            Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1 : set([]),
        }

    def set_expected_cmds_response(self):
        # for each manual command of MainClass_C1
        if self.is_triggered('eventMainclass_c1_command_comm4'):
            self.set_man_cmd_response('eventMainclass_c1_command_comm4',self.ManCmdResponse.UNEXPECTED)
        else:
            self.set_man_cmd_response('eventMainclass_c1_command_comm4',self.ManCmdResponse.NOOP)
        if self.is_triggered('eventMainclass_c1_command_comm5'):
            self.set_man_cmd_response('eventMainclass_c1_command_comm5',self.ManCmdResponse.UNEXPECTED)
        else:
            self.set_man_cmd_response('eventMainclass_c1_command_comm5',self.ManCmdResponse.NOOP)
        if self.is_triggered('eventMainclass_c1_command_comm6'):
            self.set_man_cmd_response('eventMainclass_c1_command_comm6',self.ManCmdResponse.UNEXPECTED)
        else:
            self.set_man_cmd_response('eventMainclass_c1_command_comm6',self.ManCmdResponse.NOOP)



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
    def init_configuration(self, mainclass_c1_parametro_p10, mainclass_c1_parametro_p2, mainclass_c1_parametro_p4, mainclass_c1_parametro_p8, mainclass_c1_parametro_p9):
        # initialize the record type parameters
        # initialize the simple type parameters
        self.set_mainclass_c1_parametro_p10(mainclass_c1_parametro_p10)
        self.set_mainclass_c1_parametro_p2(mainclass_c1_parametro_p2)
        self.set_mainclass_c1_parametro_p4(mainclass_c1_parametro_p4)
        self.set_mainclass_c1_parametro_p8(mainclass_c1_parametro_p8)
        self.set_mainclass_c1_parametro_p9(mainclass_c1_parametro_p9)

        # initialize the timers
        self.set_mainclass_c1_restoreti_ti1(20254000)
        self.set_mainclass_c1_restoreti_ti1_restore(20254000)
        self.set_mainclass_c1_restoreti_ti2(113000)
        self.set_mainclass_c1_restoreti_ti2_restore(113000)
        self.set_mainclass_c1_restoreti_ti3(1000)
        self.set_mainclass_c1_restoreti_ti3_restore(1000)
        self.set_mainclass_c1_restoreti_ti4(4000)
        self.set_mainclass_c1_restoreti_ti4_restore(4000)
        self.set_mainclass_c1_timer_t10(413000)
        self.set_mainclass_c1_timer_t2(330000)
        self.set_mainclass_c1_timer_t9(3254000)

        self.timers = [self.mainclass_c1_restoreti_ti1,self.mainclass_c1_restoreti_ti1_restore,self.mainclass_c1_restoreti_ti2,self.mainclass_c1_restoreti_ti2_restore,self.mainclass_c1_restoreti_ti3,self.mainclass_c1_restoreti_ti3_restore,self.mainclass_c1_restoreti_ti4,self.mainclass_c1_restoreti_ti4_restore,self.mainclass_c1_timer_t10,self.mainclass_c1_timer_t2,self.mainclass_c1_timer_t9,]

        # initialize the counters
        self.set_mainclass_c1_contatore_co10(0)
        self.set_mainclass_c1_contatore_co5(0)
        self.set_mainclass_c1_contatore_co6(0)
        self.set_mainclass_c1_contatore_co7(0)
        self.set_mainclass_c1_contatore_co8(0)

    # setters for record type parameters

    # getters for record type parameters

    # setters for simple type parameters
    def set_mainclass_c1_parametro_p10(self, mainclass_c1_parametro_p10):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p10",mainclass_c1_parametro_p10)

    def set_mainclass_c1_parametro_p2(self, mainclass_c1_parametro_p2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p2",mainclass_c1_parametro_p2)

    def set_mainclass_c1_parametro_p4(self, mainclass_c1_parametro_p4):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p4",mainclass_c1_parametro_p4)

    def set_mainclass_c1_parametro_p8(self, mainclass_c1_parametro_p8):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p8",mainclass_c1_parametro_p8)

    def set_mainclass_c1_parametro_p9(self, mainclass_c1_parametro_p9):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p9",mainclass_c1_parametro_p9)


    # getters for simple type parameters
    def get_mainclass_c1_parametro_p10(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p10")

    def get_mainclass_c1_parametro_p2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p2")

    def get_mainclass_c1_parametro_p4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p4")

    def get_mainclass_c1_parametro_p8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p8")

    def get_mainclass_c1_parametro_p9(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p9")


    # setters for comandi al piazzale
    def set_mainclass_c1_comando_c10(self, mainclass_c1_comando_c10):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c10",mainclass_c1_comando_c10)

    def set_mainclass_c1_comando_c3(self, mainclass_c1_comando_c3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c3",mainclass_c1_comando_c3)

    def set_mainclass_c1_comando_c5(self, mainclass_c1_comando_c5):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c5",mainclass_c1_comando_c5)

    def set_mainclass_c1_comando_c8(self, mainclass_c1_comando_c8):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c8",mainclass_c1_comando_c8)

    def set_mainclass_c1_comando_c9(self, mainclass_c1_comando_c9):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c9",mainclass_c1_comando_c9)


    # getters for controlli dal piazzale
    def get_consdef(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"consdef")

    def get_mainclass_c1_controllo_c10(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c10")

    def get_mainclass_c1_controllo_c3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c3")

    def get_mainclass_c1_controllo_c6(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c6")

    def get_mainclass_c1_controllo_c8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c8")

    def get_mainclass_c1_previousco_c1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c1")

    def get_mainclass_c1_previousco_c2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c2")

    def get_mainclass_c1_previousco_c4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c4")

    def get_mainclass_c1_previousco_c7(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c7")


    # setters for state variables
    def set_mainclass_c1_previousco_c1_prev(self, mainclass_c1_previousco_c1_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c1_prev",mainclass_c1_previousco_c1_prev)
    def set_mainclass_c1_previousco_c2_prev(self, mainclass_c1_previousco_c2_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c2_prev",mainclass_c1_previousco_c2_prev)
    def set_mainclass_c1_previousco_c4_prev(self, mainclass_c1_previousco_c4_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c4_prev",mainclass_c1_previousco_c4_prev)
    def set_mainclass_c1_previousco_c7_prev(self, mainclass_c1_previousco_c7_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c7_prev",mainclass_c1_previousco_c7_prev)
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
    def set_mainclass_c1_variabile_v10(self, mainclass_c1_variabile_v10):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v10",mainclass_c1_variabile_v10)
    def set_mainclass_c1_variabile_v9(self, mainclass_c1_variabile_v9):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v9",mainclass_c1_variabile_v9)

    # getters for state variables
    def get_mainclass_c1_previousco_c1_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c1_prev")

    def get_mainclass_c1_previousco_c2_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c2_prev")

    def get_mainclass_c1_previousco_c4_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c4_prev")

    def get_mainclass_c1_previousco_c7_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c7_prev")

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

    def get_mainclass_c1_variabile_v10(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v10")

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

    def set_mainclass_c1_timer_t10(self, timerDuration):
        self.mainclass_c1_timer_t10 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_timer_t10", self.memory)

    def set_mainclass_c1_timer_t2(self, timerDuration):
        self.mainclass_c1_timer_t2 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_timer_t2", self.memory)

    def set_mainclass_c1_timer_t9(self, timerDuration):
        self.mainclass_c1_timer_t9 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_timer_t9", self.memory)


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

    def get_mainclass_c1_timer_t10(self):
        return self.mainclass_c1_timer_t10

    def get_mainclass_c1_timer_t2(self):
        return self.mainclass_c1_timer_t2

    def get_mainclass_c1_timer_t9(self):
        return self.mainclass_c1_timer_t9


    # setters for counters
    def set_mainclass_c1_contatore_co10(self, counterInitValue):
        self.mainclass_c1_contatore_co10 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "mainclass_c1_contatore_co10", self.memory)

    def set_mainclass_c1_contatore_co5(self, counterInitValue):
        self.mainclass_c1_contatore_co5 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "mainclass_c1_contatore_co5", self.memory)

    def set_mainclass_c1_contatore_co6(self, counterInitValue):
        self.mainclass_c1_contatore_co6 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "mainclass_c1_contatore_co6", self.memory)

    def set_mainclass_c1_contatore_co7(self, counterInitValue):
        self.mainclass_c1_contatore_co7 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "mainclass_c1_contatore_co7", self.memory)

    def set_mainclass_c1_contatore_co8(self, counterInitValue):
        self.mainclass_c1_contatore_co8 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "mainclass_c1_contatore_co8", self.memory)


    # getters for counters
    def get_mainclass_c1_contatore_co10(self):
        return self.mainclass_c1_contatore_co10

    def get_mainclass_c1_contatore_co5(self):
        return self.mainclass_c1_contatore_co5

    def get_mainclass_c1_contatore_co6(self):
        return self.mainclass_c1_contatore_co6

    def get_mainclass_c1_contatore_co7(self):
        return self.mainclass_c1_contatore_co7

    def get_mainclass_c1_contatore_co8(self):
        return self.mainclass_c1_contatore_co8



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

        self.set_mainclass_c1_previousco_c1_prev(GlobalEnumeration.avanzamentox)
        self.set_mainclass_c1_previousco_c2_prev(False)
        self.set_mainclass_c1_previousco_c4_prev(True)
        self.set_mainclass_c1_previousco_c7_prev(GlobalEnumeration.rossogiallox)
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
    def macroMainclass_c1_macroef_m3(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {38,}  se il contatore MainClass_C1_contatore_Co6 non è  diverso da  commento: {56,} 14, commento: {66,} Assegna al comando MainClass_C1_comando_C10 il valore  False 
        
           
         commento: {35,}  se il controllo MainClass_C1_controllo_C3 è  diverso da  True  o  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} e  se il timer MainClass_C1_timer_T2 non è attivo,  Applica gli effetti
               della macro MainClass_C1_macroef_M9  commento: {73,}
        
         ,altrimenti  commento: {66,} Assegna al comando MainClass_C1_comando_C5 il valore RossoGiallox
        
        
         commento: {34,}  se lo stato  è  diverso da  commento: {56,}  state1  commento: {106,} commento: {36,} o  se il timer MainClass_C1_timer_T2 non è scaduto commento: {35,} o  se il controllo MainClass_C1_controllo_C3 è  uguale a  False  commento: {34,} e  se il parametro MainClass_C1_parametro_P8 è  maggiore di  commento: {54,} 2, commento: {71,}Decrementa il contatore MainClass_C1_contatore_Co6
        
         ,altrimenti   Applica gli effetti
               della macro MainClass_C1_macroef_M9  commento: {73,}
        
        
          se il ripristino dello stato  è  diverso da  commento: {56,}  state1  commento: {107,}, commento: {71,}Decrementa il contatore MainClass_C1_contatore_Co10
        
         ,altrimenti  commento: {66,} Assegna al comando MainClass_C1_comando_C5 il valore RossoGiallox
        
        
         commento: {36,}  se il timer MainClass_C1_timer_T2 non è scaduto commento: {37,} o  se la variabile MainClass_C1_variabile_V10 è  diverso da  False  commento: {36,} e  se il timer MainClass_C1_timer_T10 non è disattivo, commento: {66,} Assegna al comando MainClass_C1_comando_C5 il valore RossoGiallox
        
           
        
        }
        """
        def populate_macroMainclass_c1_macroef_m3_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*38,*/  se il contatore MainClass_C1_contatore_Co6 non è  diverso da  /*56,*/ 14, /*66,*/ Assegna al comando MainClass_C1_comando_C10 il valore  False""", [
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co6 non è  diverso da  /*56,*/ 14""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co6)  è uguale a  (14))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co6)  è uguale a  (14)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            ]),#0
                            DIStatement("""ITEStatementImpl\n/*35,*/  se il controllo MainClass_C1_controllo_C3 è  diverso da  True  o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T2 non è attivo,  Applica gli effetti
       della macro MainClass_C1_macroef_M9  /*73,*/

 ,altrimenti  /*66,*/ Assegna al comando MainClass_C1_comando_C5 il valore RossoGiallox""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*35,*/  se il controllo MainClass_C1_controllo_C3 è  diverso da  True  o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T2 non è attivo""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c3)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c3)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  
( negazione di (il timer 'mainclass_c1_timer_t2' è attivo) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t2' è attivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t2' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M9"""),#1
                            ]),#1
                            DIStatement("""ITEStatementImpl\n/*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*36,*/ o  se il timer MainClass_C1_timer_T2 non è scaduto /*35,*/ o  se il controllo MainClass_C1_controllo_C3 è  uguale a  False  /*34,*/ e  se il parametro MainClass_C1_parametro_P8 è  maggiore di  /*54,*/ 2, /*71,*/Decrementa il contatore MainClass_C1_contatore_Co6

 ,altrimenti   Applica gli effetti
       della macro MainClass_C1_macroef_M9""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*36,*/ o  se il timer MainClass_C1_timer_T2 non è scaduto /*35,*/ o  se il controllo MainClass_C1_controllo_C3 è  uguale a  False  /*34,*/ e  se il parametro MainClass_C1_parametro_P8 è  maggiore di  /*54,*/ 2""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( negazione di ((lo stato di 'self')  è uguale a  (state1)) )  o  
( negazione di (il timer 'mainclass_c1_timer_t2' è scaduto) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lo stato di 'self')  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t2' è scaduto)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t2' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( (mainclass_c1_controllo_c3)  è uguale a  (False) )  e  
( (mainclass_c1_parametro_p8)  è maggiore di  (2) )""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c3)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_parametro_p8)  è maggiore di  (2)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M9"""),#1
                            ]),#2
                            DIStatement("""ITEStatementImpl\n/*73,*/


  se il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/, /*71,*/Decrementa il contatore MainClass_C1_contatore_Co10

 ,altrimenti  /*66,*/ Assegna al comando MainClass_C1_comando_C5 il valore RossoGiallox""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino dello stato  è  diverso da  /*56,*/  state1""", [
                            DIBoolExpr("""EqualImpl\n(stato_restore)  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            ]),#3
                            DIStatement("""ITStatement\n/*36,*/  se il timer MainClass_C1_timer_T2 non è scaduto /*37,*/ o  se la variabile MainClass_C1_variabile_V10 è  diverso da  False  /*36,*/ e  se il timer MainClass_C1_timer_T10 non è disattivo, /*66,*/ Assegna al comando MainClass_C1_comando_C5 il valore RossoGiallox""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*36,*/  se il timer MainClass_C1_timer_T2 non è scaduto /*37,*/ o  se la variabile MainClass_C1_variabile_V10 è  diverso da  False  /*36,*/ e  se il timer MainClass_C1_timer_T10 non è disattivo""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t2' è scaduto)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t2' è scaduto""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_variabile_v10)  è uguale a  (False)) )  e  
( negazione di (il timer 'mainclass_c1_timer_t10' è inattivo) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v10)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v10)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t10' è inattivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t10' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#4
                ])

        populate_macroMainclass_c1_macroef_m3_SrfMacroDefInfo(di_ctx)
        #  /*38,*/  se il contatore MainClass_C1_contatore_Co6 non è  diverso da  /*56,*/ 14, /*66,*/ Assegna al comando MainClass_C1_comando_C10 il valore  False
        if db(not db(not db(self.get_mainclass_c1_contatore_co6().get_valore() == 14, di_ctx.subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0]):
            self.set_mainclass_c1_comando_c10(False)
        #  /*35,*/  se il controllo MainClass_C1_controllo_C3 è  diverso da  True  o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T2 non è attivo,  Applica gli effetti
        #         della macro MainClass_C1_macroef_M9  /*73,*/
        #   ,altrimenti  /*66,*/ Assegna al comando MainClass_C1_comando_C5 il valore RossoGiallox
        if db((db(not db(self.get_mainclass_c1_controllo_c3() == True, di_ctx.subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0]) or db((db(self.get_consdef() == False, di_ctx.subs[1].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_timer_t2().isAttivato(), di_ctx.subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.macroMainclass_c1_macroef_m9(di_ctx.subs[1].subs[1])
        else:
            self.set_mainclass_c1_comando_c5(GlobalEnumeration.rossogiallox)
        #  /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*36,*/ o  se il timer MainClass_C1_timer_T2 non è scaduto /*35,*/ o  se il controllo MainClass_C1_controllo_C3 è  uguale a  False  /*34,*/ e  se il parametro MainClass_C1_parametro_P8 è  maggiore di  /*54,*/ 2, /*71,*/Decrementa il contatore MainClass_C1_contatore_Co6
        #   ,altrimenti   Applica gli effetti
        #         della macro MainClass_C1_macroef_M9
        if db((db((db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_timer_t2().isScaduto(), di_ctx.subs[2].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0]) or db((db(self.get_mainclass_c1_controllo_c3() == False, di_ctx.subs[2].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_parametro_p8() > 2, di_ctx.subs[2].subs[0].subs[1].subs[1])), di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.get_mainclass_c1_contatore_co6().decrementa()
        else:
            self.macroMainclass_c1_macroef_m9(di_ctx.subs[2].subs[1])
        #  /*73,*/
        #    se il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/, /*71,*/Decrementa il contatore MainClass_C1_contatore_Co10
        #   ,altrimenti  /*66,*/ Assegna al comando MainClass_C1_comando_C5 il valore RossoGiallox
        if db(not db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[3].subs[0].subs[0]), di_ctx.subs[3].subs[0]):
            self.get_mainclass_c1_contatore_co10().decrementa()
        else:
            self.set_mainclass_c1_comando_c5(GlobalEnumeration.rossogiallox)
        #  /*36,*/  se il timer MainClass_C1_timer_T2 non è scaduto /*37,*/ o  se la variabile MainClass_C1_variabile_V10 è  diverso da  False  /*36,*/ e  se il timer MainClass_C1_timer_T10 non è disattivo, /*66,*/ Assegna al comando MainClass_C1_comando_C5 il valore RossoGiallox
        if db((db(not db(self.get_mainclass_c1_timer_t2().isScaduto(), di_ctx.subs[4].subs[0].subs[0].subs[0]), di_ctx.subs[4].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_variabile_v10() == False, di_ctx.subs[4].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[4].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_timer_t10().isDisattivato(), di_ctx.subs[4].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[4].subs[0].subs[1].subs[1])), di_ctx.subs[4].subs[0].subs[1])), di_ctx.subs[4].subs[0]):
            self.set_mainclass_c1_comando_c5(GlobalEnumeration.rossogiallox)
    
    def macroMainclass_c1_macroef_m9(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {34,}  se lo stato  non è  uguale a  commento: {53,}  state1  commento: {106,} commento: {35,} o  se il controllo MainClass_C1_controllo_C3 è  diverso da  False  commento: {38,} o  se il contatore MainClass_C1_contatore_Co7 non è  minore di  commento: {55,} 122 commento: {34,} o  se il parametro MainClass_C1_parametro_P8 è  uguale a  commento: {53,} 1 commento: {34,} o  se il parametro MainClass_C1_parametro_P9 non è  diverso da RossoGialloxVerdex commento: {37,} e  se la variabile MainClass_C1_variabile_V10 è  uguale a  True , commento: {72,}Azzera il contatore MainClass_C1_contatore_Co6
        
           
         commento: {34,}  se lo stato  non è  uguale a  commento: {53,}  state1  commento: {106,}, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V9 il valore  False 
        
           
        
        }
        """
        def populate_macroMainclass_c1_macroef_m9_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*35,*/ o  se il controllo MainClass_C1_controllo_C3 è  diverso da  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 non è  minore di  /*55,*/ 122 /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  uguale a  /*53,*/ 1 /*34,*/ o  se il parametro MainClass_C1_parametro_P9 non è  diverso da RossoGialloxVerdex /*37,*/ e  se la variabile MainClass_C1_variabile_V10 è  uguale a  True , /*72,*/Azzera il contatore MainClass_C1_contatore_Co6""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*35,*/ o  se il controllo MainClass_C1_controllo_C3 è  diverso da  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 non è  minore di  /*55,*/ 122 /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  uguale a  /*53,*/ 1 /*34,*/ o  se il parametro MainClass_C1_parametro_P9 non è  diverso da RossoGialloxVerdex /*37,*/ e  se la variabile MainClass_C1_variabile_V10 è  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( ( negazione di ((lo stato di 'self')  è uguale a  (state1)) )  o  
( negazione di ((mainclass_c1_controllo_c3)  è uguale a  (False)) ) )  o  
( negazione di ((mainclass_c1_contatore_co7)  è minore di  (122)) ) )  o  
( (mainclass_c1_parametro_p8)  è uguale a  (1) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( negazione di ((lo stato di 'self')  è uguale a  (state1)) )  o  
( negazione di ((mainclass_c1_controllo_c3)  è uguale a  (False)) ) )  o  
( negazione di ((mainclass_c1_contatore_co7)  è minore di  (122)) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( negazione di ((lo stato di 'self')  è uguale a  (state1)) )  o  
( negazione di ((mainclass_c1_controllo_c3)  è uguale a  (False)) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lo stato di 'self')  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c3)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c3)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co7)  è minore di  (122))""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co7)  è minore di  (122)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p8)  è uguale a  (1)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (negazione di ((mainclass_c1_parametro_p9)  è uguale a  (rossogialloxverdex))) )  e  
( (mainclass_c1_variabile_v10)  è uguale a  (True) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_parametro_p9)  è uguale a  (rossogialloxverdex)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p9)  è uguale a  (rossogialloxverdex))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p9)  è uguale a  (rossogialloxverdex)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v10)  è uguale a  (True)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITStatement\n/*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V9 il valore  False""", [
                            DIBoolExpr("""Operatore Logico Not\nlo stato  non è  uguale a  /*53,*/  state1""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                ])

        populate_macroMainclass_c1_macroef_m9_SrfMacroDefInfo(di_ctx)
        #  /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*35,*/ o  se il controllo MainClass_C1_controllo_C3 è  diverso da  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 non è  minore di  /*55,*/ 122 /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  uguale a  /*53,*/ 1 /*34,*/ o  se il parametro MainClass_C1_parametro_P9 non è  diverso da RossoGialloxVerdex /*37,*/ e  se la variabile MainClass_C1_variabile_V10 è  uguale a  True , /*72,*/Azzera il contatore MainClass_C1_contatore_Co6
        if db((db((db((db((db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_controllo_c3() == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_contatore_co7().get_valore() < 122, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_parametro_p8() == 1, di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db(not db(self.get_mainclass_c1_parametro_p9() == GlobalEnumeration.rossogialloxverdex, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_variabile_v10() == True, di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.get_mainclass_c1_contatore_co6().resetta()
        #  /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V9 il valore  False
        if db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[1].subs[0].subs[0]), di_ctx.subs[1].subs[0]):
            self.set_mainclass_c1_variabile_v9(False)
    
    # verify macros
    @srf_value_macro("macroMainclass_c1_macrove_m10")
    def macroMainclass_c1_macrove_m10(self, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
         
        {  se il ripristino dello stato  non è  diverso da  commento: {56,}  state1  commento: {107,} commento: {38,} e  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  commento: {53,} 131 commento: {37,} o  se la variabile MainClass_C1_variabile_V9 è  uguale a  True  commento: {34,} o  se il parametro MainClass_C1_parametro_P8 non è  diverso da  commento: {56,} 7 o  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} e  se la variabile MainClass_C1_variabile_V9 non è  diverso da  False , Verifica che   commento: {48,49,50,51,}  commento: {,}  la variabile MainClass_C1_variabile_V10 sia  diverso da  True 
         commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C8 non sia  diverso da  False 
         commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T2 sia attivo
         commento: {104,} o  che  commento: {,}  il contatore MainClass_C1_contatore_Co6 sia  maggiore di  commento: {54,} 1130
        
        
        }
        """
        def populate_macroMainclass_c1_macrove_m10_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\nse il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  /*53,*/ 131 /*37,*/ o  se la variabile MainClass_C1_variabile_V9 è  uguale a  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  diverso da  /*56,*/ 7 o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V9 non è  diverso da  False , Verifica che   /*48,49,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V10 sia  diverso da  True 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T2 sia attivo
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co6 sia  maggiore di  /*54,*/ 1130""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\nse il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  /*53,*/ 131 /*37,*/ o  se la variabile MainClass_C1_variabile_V9 è  uguale a  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  diverso da  /*56,*/ 7 o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V9 non è  diverso da  False , Verifica che   /*48,49,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V10 sia  diverso da  True 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T2 sia attivo
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co6 sia  maggiore di  /*54,*/ 1130""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  /*53,*/ 131 /*37,*/ o  se la variabile MainClass_C1_variabile_V9 è  uguale a  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  diverso da  /*56,*/ 7 o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V9 non è  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  /*53,*/ 131 /*37,*/ o  se la variabile MainClass_C1_variabile_V9 è  uguale a  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  diverso da  /*56,*/ 7""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  /*53,*/ 131 /*37,*/ o  se la variabile MainClass_C1_variabile_V9 è  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  /*53,*/ 131""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino dello stato  non è  diverso da  /*56,*/  state1""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((stato_restore)  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(stato_restore)  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co7 non è  uguale a  /*53,*/ 131""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co7)  è uguale a  (131)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nla variabile MainClass_C1_variabile_V9 è  uguale a  True""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P8 non è  diverso da  /*56,*/ 7""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p8)  è uguale a  (7))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p8)  è uguale a  (7)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V9 non è  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V9 non è  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v9)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v9)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V10 sia  diverso da  True 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T2 sia attivo
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co6 sia  maggiore di  /*54,*/ 1130""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V10 sia  diverso da  True 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T2 sia attivo""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,49,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V10 sia  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v10)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T2 sia attivo""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c8)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c8)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer MainClass_C1_timer_T2 sia attivo""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nche  /*,*/  il contatore MainClass_C1_contatore_Co6 sia  maggiore di  /*54,*/ 1130""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macrove_m10_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db((db((db(not db(not db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co7().get_valore() == 131, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_variabile_v9() == True, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_parametro_p8() == 7, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_mainclass_c1_variabile_v9() == False, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db((db(not db(self.get_mainclass_c1_variabile_v10() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db((db(not db(not db(self.get_mainclass_c1_controllo_c8() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_timer_t2().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0]) or db(self.get_mainclass_c1_contatore_co6().get_valore() > 1130, di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0])), di_ctx.subs[0])
    
    @srf_value_macro("macroMainclass_c1_macrove_m2")
    def macroMainclass_c1_macrove_m2(self, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
         
        { commento: {63,}  se la macro  MainClass_C1_macrova_M7 ( con argomento_a4   uguale a True ,argomento_a7   uguale a RossoGialloGiallo ,argomento_a1   uguale a Giallox ,argomento_a3   uguale a c180x ,argomento_a6   uguale a RossoGiallo  e argomento_a5   uguale a c180x )   è  diverso da RossoGialloGiallo commento: {40,}  commento: {34,} e  se il parametro MainClass_C1_parametro_P8 non è  maggiore di  commento: {54,} 4 commento: {37,} o  se la variabile MainClass_C1_variabile_V9 non è  diverso da  True  commento: {38,} o  se il contatore MainClass_C1_contatore_Co6 non è  uguale a  commento: {53,} 1202 commento: {36,} e  se il timer MainClass_C1_timer_T10 è disattivo commento: {36,} e  se il timer MainClass_C1_timer_T2 non è scaduto, Solo una delle seguenti { 
         commento: {35,}  se il controllo MainClass_C1_controllo_C3 è  uguale a  False  commento: {36,} e  se il timer MainClass_C1_timer_T10 non è scaduto o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   commento: {47,48,49,}  commento: {34,}  il parametro MainClass_C1_parametro_P4 sia  uguale a RossoGialloxVerdex
         commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T2 sia attivo
         commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C3 non sia  diverso da  True 
         commento: {104,} o  che  commento: {36,}  il timer MainClass_C1_timer_T9 non sia disattivo
        
        
         } Verifica che   commento: {47,51,}  commento: {34,}  il parametro MainClass_C1_parametro_P4 sia  diverso da RossoGialloxVerdex
         commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co8 sia  minore di  commento: {55,} 14
        
        
        }
        """
        def populate_macroMainclass_c1_macrove_m2_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/  se la macro  MainClass_C1_macrova_M7 ( con argomento_a4   uguale a True ,argomento_a7   uguale a RossoGialloGiallo ,argomento_a1   uguale a Giallox ,argomento_a3   uguale a c180x ,argomento_a6   uguale a RossoGiallo  e argomento_a5   uguale a c180x )   è  diverso da RossoGialloGiallo /*40,*/  /*34,*/ e  se il parametro MainClass_C1_parametro_P8 non è  maggiore di  /*54,*/ 4 /*37,*/ o  se la variabile MainClass_C1_variabile_V9 non è  diverso da  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co6 non è  uguale a  /*53,*/ 1202 /*36,*/ e  se il timer MainClass_C1_timer_T10 è disattivo /*36,*/ e  se il timer MainClass_C1_timer_T2 non è scaduto, Solo una delle seguenti { 
 /*35,*/  se il controllo MainClass_C1_controllo_C3 è  uguale a  False  /*36,*/ e  se il timer MainClass_C1_timer_T10 non è scaduto o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*47,48,49,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  uguale a RossoGialloxVerdex
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T2 sia attivo
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C3 non sia  diverso da  True 
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T9 non sia disattivo


 } Verifica che   /*47,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  diverso da RossoGialloxVerdex
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  minore di  /*55,*/ 14""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/  se la macro  MainClass_C1_macrova_M7 ( con argomento_a4   uguale a True ,argomento_a7   uguale a RossoGialloGiallo ,argomento_a1   uguale a Giallox ,argomento_a3   uguale a c180x ,argomento_a6   uguale a RossoGiallo  e argomento_a5   uguale a c180x )   è  diverso da RossoGialloGiallo /*40,*/  /*34,*/ e  se il parametro MainClass_C1_parametro_P8 non è  maggiore di  /*54,*/ 4 /*37,*/ o  se la variabile MainClass_C1_variabile_V9 non è  diverso da  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co6 non è  uguale a  /*53,*/ 1202 /*36,*/ e  se il timer MainClass_C1_timer_T10 è disattivo /*36,*/ e  se il timer MainClass_C1_timer_T2 non è scaduto, Solo una delle seguenti { 
 /*35,*/  se il controllo MainClass_C1_controllo_C3 è  uguale a  False  /*36,*/ e  se il timer MainClass_C1_timer_T10 non è scaduto o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*47,48,49,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  uguale a RossoGialloxVerdex
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T2 sia attivo
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C3 non sia  diverso da  True 
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T9 non sia disattivo


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/  se la macro  MainClass_C1_macrova_M7 ( con argomento_a4   uguale a True ,argomento_a7   uguale a RossoGialloGiallo ,argomento_a1   uguale a Giallox ,argomento_a3   uguale a c180x ,argomento_a6   uguale a RossoGiallo  e argomento_a5   uguale a c180x )   è  diverso da RossoGialloGiallo /*40,*/  /*34,*/ e  se il parametro MainClass_C1_parametro_P8 non è  maggiore di  /*54,*/ 4 /*37,*/ o  se la variabile MainClass_C1_variabile_V9 non è  diverso da  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co6 non è  uguale a  /*53,*/ 1202 /*36,*/ e  se il timer MainClass_C1_timer_T10 è disattivo /*36,*/ e  se il timer MainClass_C1_timer_T2 non è scaduto""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/  se la macro  MainClass_C1_macrova_M7 ( con argomento_a4   uguale a True ,argomento_a7   uguale a RossoGialloGiallo ,argomento_a1   uguale a Giallox ,argomento_a3   uguale a c180x ,argomento_a6   uguale a RossoGiallo  e argomento_a5   uguale a c180x )   è  diverso da RossoGialloGiallo /*40,*/  /*34,*/ e  se il parametro MainClass_C1_parametro_P8 non è  maggiore di  /*54,*/ 4 /*37,*/ o  se la variabile MainClass_C1_variabile_V9 non è  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/  se la macro  MainClass_C1_macrova_M7 ( con argomento_a4   uguale a True ,argomento_a7   uguale a RossoGialloGiallo ,argomento_a1   uguale a Giallox ,argomento_a3   uguale a c180x ,argomento_a6   uguale a RossoGiallo  e argomento_a5   uguale a c180x )   è  diverso da RossoGialloGiallo /*40,*/  /*34,*/ e  se il parametro MainClass_C1_parametro_P8 non è  maggiore di  /*54,*/ 4""", [
                            DIBoolExpr("""Operatore Logico Not\nla macro  MainClass_C1_macrova_M7 ( con argomento_a4   uguale a True ,argomento_a7   uguale a RossoGialloGiallo ,argomento_a1   uguale a Giallox ,argomento_a3   uguale a c180x ,argomento_a6   uguale a RossoGiallo  e argomento_a5   uguale a c180x )   è  diverso da RossoGialloGiallo""", [
                            DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m7')  è uguale a  (rossogiallogiallo)""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroMainclass_c1_macrova_m7'"""),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P8 non è  maggiore di  /*54,*/ 4""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_parametro_p8)  è maggiore di  (4)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V9 non è  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v9)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v9)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il contatore MainClass_C1_contatore_Co6 non è  uguale a  /*53,*/ 1202 /*36,*/ e  se il timer MainClass_C1_timer_T10 è disattivo /*36,*/ e  se il timer MainClass_C1_timer_T2 non è scaduto""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il contatore MainClass_C1_contatore_Co6 non è  uguale a  /*53,*/ 1202 /*36,*/ e  se il timer MainClass_C1_timer_T10 è disattivo""", [
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co6 non è  uguale a  /*53,*/ 1202""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co6)  è uguale a  (1202)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T10 è disattivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T2 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t2' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*35,*/  se il controllo MainClass_C1_controllo_C3 è  uguale a  False  /*36,*/ e  se il timer MainClass_C1_timer_T10 non è scaduto o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*47,48,49,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  uguale a RossoGialloxVerdex
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T2 sia attivo
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C3 non sia  diverso da  True 
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T9 non sia disattivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*35,*/  se il controllo MainClass_C1_controllo_C3 è  uguale a  False  /*36,*/ e  se il timer MainClass_C1_timer_T10 non è scaduto o  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*35,*/  se il controllo MainClass_C1_controllo_C3 è  uguale a  False  /*36,*/ e  se il timer MainClass_C1_timer_T10 non è scaduto""", [
                            DIBoolExpr("""EqualImpl\nil controllo MainClass_C1_controllo_C3 è  uguale a  False""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T10 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t10' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  uguale a RossoGialloxVerdex
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T2 sia attivo
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C3 non sia  diverso da  True 
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T9 non sia disattivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  uguale a RossoGialloxVerdex
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T2 sia attivo
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C3 non sia  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  uguale a RossoGialloxVerdex
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T2 sia attivo""", [
                            DIBoolExpr("""EqualImpl\nche   /*47,48,49,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  uguale a RossoGialloxVerdex""", [
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer MainClass_C1_timer_T2 sia attivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C3 non sia  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo MainClass_C1_controllo_C3 non sia  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c3)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c3)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*36,*/  il timer MainClass_C1_timer_T9 non sia disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t9' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  diverso da RossoGialloxVerdex
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  minore di  /*55,*/ 14""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  diverso da RossoGialloxVerdex""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p4)  è uguale a  (rossogialloxverdex)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nche  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  minore di  /*55,*/ 14""", [
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroMainclass_c1_macrove_m2_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db((db(not db(db(self.macroMainclass_c1_macrova_m7(GlobalEnumeration.giallox,GlobalEnumeration.c180x,True,GlobalEnumeration.c180x,GlobalEnumeration.rossogiallo,GlobalEnumeration.rossogiallogiallo, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) == GlobalEnumeration.rossogiallogiallo, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p8() > 4, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_variabile_v9() == True, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db((db((db(not db(self.get_mainclass_c1_contatore_co6().get_valore() == 1202, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(self.get_mainclass_c1_timer_t10().isDisattivato(), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_timer_t2().isScaduto(), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(not db((db((db(self.get_mainclass_c1_controllo_c3() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_timer_t10().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0]) or db((db((db((db(self.get_mainclass_c1_parametro_p4() == GlobalEnumeration.rossogialloxverdex, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_timer_t2().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]) or db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_mainclass_c1_controllo_c3() == True, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) or db(not db(self.get_mainclass_c1_timer_t9().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db(not db(self.get_mainclass_c1_parametro_p4() == GlobalEnumeration.rossogialloxverdex, di_ctx.subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_contatore_co8().get_valore() < 14, di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    @srf_value_macro("macroMainclass_c1_macrove_m4")
    def macroMainclass_c1_macrove_m4(self, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
         
        { commento: {36,}  se il timer MainClass_C1_timer_T2 è attivo e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   commento: {48,51,}  commento: {,}  il contatore MainClass_C1_contatore_Co6 non sia  maggiore di  commento: {54,} 13
         commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
        
        
        }
        """
        def populate_macroMainclass_c1_macrove_m4_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*36,*/  se il timer MainClass_C1_timer_T2 è attivo e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*48,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co6 non sia  maggiore di  /*54,*/ 13
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*36,*/  se il timer MainClass_C1_timer_T2 è attivo e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*48,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co6 non sia  maggiore di  /*54,*/ 13
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*36,*/  se il timer MainClass_C1_timer_T2 è attivo e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T2 è attivo""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co6 non sia  maggiore di  /*54,*/ 13
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co6 non sia  maggiore di  /*54,*/ 13""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co6)  è maggiore di  (13)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macrove_m4_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db(self.get_mainclass_c1_timer_t2().isAttivato(), di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_contatore_co6().get_valore() > 13, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0])), di_ctx.subs[0])
    
    @srf_value_macro("macroMainclass_c1_macrove_m8")
    def macroMainclass_c1_macrove_m8(self, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
         
        { commento: {61,} commento: {34,}  se il parametro MainClass_C1_parametro_P4 è  uguale a RossoGialloxVerdex commento: {37,} e  se la variabile MainClass_C1_variabile_V10 è  diverso da  False  commento: {37,} e  se la variabile MainClass_C1_variabile_V9 è  uguale a  True  commento: {36,} e  se il timer MainClass_C1_timer_T10 non è scaduto commento: {36,} o  se il timer MainClass_C1_timer_T10 è scaduto commento: {35,} o  se il controllo MainClass_C1_controllo_C3 non è  uguale a  True , Tutte le seguenti { 
         commento: {63,}  se il controllo ConsDef è uguale a FALSE , Solo una delle seguenti { 
         commento: {61,}  se la macro  MainClass_C1_macrova_M3 ( con argomento_a6   uguale a True ,argomento_a5   uguale a RossoGiallox  e argomento_a10   uguale a avvio )   è  diverso da  False  commento: {40,}  commento: {38,} e  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  commento: {53,} 131 commento: {36,} o  se il timer MainClass_C1_timer_T10 non è disattivo commento: {38,} o  se il contatore MainClass_C1_contatore_Co6 non è  minore di  commento: {55,} 11 commento: {37,} o  se la variabile MainClass_C1_variabile_V9 è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
         commento: {63,} commento: {34,}  se il parametro MainClass_C1_parametro_P2 è  uguale a RossoGialloGiallo, Solo una delle seguenti { 
         commento: {62,}  se la macro  MainClass_C1_macrova_M3 ( con argomento_a6   uguale a True ,argomento_a5   uguale a RossoGiallox  e argomento_a10   uguale a avvio )  non  è  uguale a  True  commento: {40,}  o  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro MainClass_C1_parametro_P9 è  uguale a RossoGialloxVerdex commento: {36,} o  se il timer MainClass_C1_timer_T2 non è scaduto commento: {38,} e  se il contatore MainClass_C1_contatore_Co5 non è  diverso da  commento: {56,} 14, Almeno una delle seguenti { 
         commento: {62,} commento: {36,}  se il timer MainClass_C1_timer_T2 è disattivo commento: {36,} e  se il timer MainClass_C1_timer_T2 è attivo commento: {38,} e  se il contatore MainClass_C1_contatore_Co5 non è  minore di  commento: {55,} 11 commento: {36,} o  se il timer MainClass_C1_timer_T9 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
         commento: {35,}  se il controllo MainClass_C1_controllo_C6 è  uguale a  True , Verifica che   commento: {48,50,51,}  commento: {,}  la variabile MainClass_C1_variabile_V9 sia  diverso da  True 
         commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co6 non sia  uguale a  commento: {53,} 1130
         commento: {104,} e  che  commento: {38,}  il contatore MainClass_C1_contatore_Co6 non sia  maggiore di  commento: {54,} 11
         commento: {104,} o  che  commento: {38,}  il contatore MainClass_C1_contatore_Co10 non sia  maggiore di  commento: {54,} 13254
         commento: {104,} o  che  commento: {37,}  la variabile MainClass_C1_variabile_V10 sia  diverso da  False 
        
        
         } Verifica che   commento: {47,49,51,}  commento: {,}  il timer MainClass_C1_timer_T9 sia scaduto
         commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P8 non sia  uguale a  commento: {53,} 8
         commento: {104,} o  che  commento: {,}  il contatore MainClass_C1_contatore_Co6 sia  uguale a  commento: {53,} 13
         commento: {104,} o  che  commento: {38,}  il contatore MainClass_C1_contatore_Co6 sia  maggiore di  commento: {54,} 125
        
        
         } Verifica che   commento: {47,49,51,}  commento: {,}  il timer MainClass_C1_timer_T10 non sia attivo
         commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co7 non sia  diverso da  commento: {56,} 11
         commento: {104,} e  che  commento: {36,}  il timer MainClass_C1_timer_T2 sia scaduto
         commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P9 non sia  diverso da RossoGialloxVerdex
        
        
         } Verifica che   commento: {47,48,51,}   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C3 non sia  uguale a  False 
         commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P8 non sia  uguale a  commento: {53,} 4
         commento: {104,} o  che  commento: {,}  il contatore MainClass_C1_contatore_Co7 non sia  minore di  commento: {55,} 133
        
        
         } Verifica che   commento: {48,49,51,}  commento: {,}  il contatore MainClass_C1_contatore_Co7 non sia  diverso da  commento: {56,} 13025
         commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T2 sia attivo
         commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C3 sia  diverso da  False 
         commento: {104,} e  che  commento: {36,}  il timer MainClass_C1_timer_T10 non sia disattivo
        
        
         } Verifica che   commento: {47,49,51,}  commento: {,}  il contatore MainClass_C1_contatore_Co7 non sia  uguale a  commento: {53,} 15
         commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T9 sia attivo
         commento: {104,} e  che  commento: {38,}  il contatore MainClass_C1_contatore_Co10 non sia  minore di  commento: {55,} 113
         commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P4 sia  diverso da RossoGialloxVerdex
        
        
         } Verifica che   commento: {48,49,50,}  commento: {,}  il timer MainClass_C1_timer_T10 sia disattivo
         commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V10 sia  diverso da  True 
         commento: {104,} o  che  commento: {37,}  la variabile MainClass_C1_variabile_V10 sia  uguale a  True 
         commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C3 sia  uguale a  False 
        
        
        }
        """
        def populate_macroMainclass_c1_macrove_m8_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*34,*/  se il parametro MainClass_C1_parametro_P4 è  uguale a RossoGialloxVerdex /*37,*/ e  se la variabile MainClass_C1_variabile_V10 è  diverso da  False  /*37,*/ e  se la variabile MainClass_C1_variabile_V9 è  uguale a  True  /*36,*/ e  se il timer MainClass_C1_timer_T10 non è scaduto /*36,*/ o  se il timer MainClass_C1_timer_T10 è scaduto /*35,*/ o  se il controllo MainClass_C1_controllo_C3 non è  uguale a  True , Tutte le seguenti { 
 /*63,*/  se il controllo ConsDef è uguale a FALSE , Solo una delle seguenti { 
 /*61,*/  se la macro  MainClass_C1_macrova_M3 ( con argomento_a6   uguale a True ,argomento_a5   uguale a RossoGiallox  e argomento_a10   uguale a avvio )   è  diverso da  False  /*40,*/  /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  /*53,*/ 131 /*36,*/ o  se il timer MainClass_C1_timer_T10 non è disattivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co6 non è  minore di  /*55,*/ 11 /*37,*/ o  se la variabile MainClass_C1_variabile_V9 è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*63,*/ /*34,*/  se il parametro MainClass_C1_parametro_P2 è  uguale a RossoGialloGiallo, Solo una delle seguenti { 
 /*62,*/  se la macro  MainClass_C1_macrova_M3 ( con argomento_a6   uguale a True ,argomento_a5   uguale a RossoGiallox  e argomento_a10   uguale a avvio )  non  è  uguale a  True  /*40,*/  o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P9 è  uguale a RossoGialloxVerdex /*36,*/ o  se il timer MainClass_C1_timer_T2 non è scaduto /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 non è  diverso da  /*56,*/ 14, Almeno una delle seguenti { 
 /*62,*/ /*36,*/  se il timer MainClass_C1_timer_T2 è disattivo /*36,*/ e  se il timer MainClass_C1_timer_T2 è attivo /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 non è  minore di  /*55,*/ 11 /*36,*/ o  se il timer MainClass_C1_timer_T9 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
 /*35,*/  se il controllo MainClass_C1_controllo_C6 è  uguale a  True , Verifica che   /*48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V9 sia  diverso da  True 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co6 non sia  uguale a  /*53,*/ 1130
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co6 non sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co10 non sia  maggiore di  /*54,*/ 13254
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V10 sia  diverso da  False 


 } Verifica che   /*47,49,51,*/  /*,*/  il timer MainClass_C1_timer_T9 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  uguale a  /*53,*/ 8
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co6 sia  uguale a  /*53,*/ 13
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co6 sia  maggiore di  /*54,*/ 125


 } Verifica che   /*47,49,51,*/  /*,*/  il timer MainClass_C1_timer_T10 non sia attivo
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  diverso da  /*56,*/ 11
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T2 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  diverso da RossoGialloxVerdex


 } Verifica che   /*47,48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C3 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  uguale a  /*53,*/ 4
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  minore di  /*55,*/ 133


 } Verifica che   /*48,49,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  diverso da  /*56,*/ 13025
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T2 sia attivo
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C3 sia  diverso da  False 
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T10 non sia disattivo


 } Verifica che   /*47,49,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  uguale a  /*53,*/ 15
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T9 sia attivo
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co10 non sia  minore di  /*55,*/ 113
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  diverso da RossoGialloxVerdex


 } Verifica che   /*48,49,50,*/  /*,*/  il timer MainClass_C1_timer_T10 sia disattivo
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V10 sia  diverso da  True 
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V10 sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C3 sia  uguale a  False""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*34,*/  se il parametro MainClass_C1_parametro_P4 è  uguale a RossoGialloxVerdex /*37,*/ e  se la variabile MainClass_C1_variabile_V10 è  diverso da  False  /*37,*/ e  se la variabile MainClass_C1_variabile_V9 è  uguale a  True  /*36,*/ e  se il timer MainClass_C1_timer_T10 non è scaduto /*36,*/ o  se il timer MainClass_C1_timer_T10 è scaduto /*35,*/ o  se il controllo MainClass_C1_controllo_C3 non è  uguale a  True , Tutte le seguenti { 
 /*63,*/  se il controllo ConsDef è uguale a FALSE , Solo una delle seguenti { 
 /*61,*/  se la macro  MainClass_C1_macrova_M3 ( con argomento_a6   uguale a True ,argomento_a5   uguale a RossoGiallox  e argomento_a10   uguale a avvio )   è  diverso da  False  /*40,*/  /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  /*53,*/ 131 /*36,*/ o  se il timer MainClass_C1_timer_T10 non è disattivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co6 non è  minore di  /*55,*/ 11 /*37,*/ o  se la variabile MainClass_C1_variabile_V9 è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*63,*/ /*34,*/  se il parametro MainClass_C1_parametro_P2 è  uguale a RossoGialloGiallo, Solo una delle seguenti { 
 /*62,*/  se la macro  MainClass_C1_macrova_M3 ( con argomento_a6   uguale a True ,argomento_a5   uguale a RossoGiallox  e argomento_a10   uguale a avvio )  non  è  uguale a  True  /*40,*/  o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P9 è  uguale a RossoGialloxVerdex /*36,*/ o  se il timer MainClass_C1_timer_T2 non è scaduto /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 non è  diverso da  /*56,*/ 14, Almeno una delle seguenti { 
 /*62,*/ /*36,*/  se il timer MainClass_C1_timer_T2 è disattivo /*36,*/ e  se il timer MainClass_C1_timer_T2 è attivo /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 non è  minore di  /*55,*/ 11 /*36,*/ o  se il timer MainClass_C1_timer_T9 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
 /*35,*/  se il controllo MainClass_C1_controllo_C6 è  uguale a  True , Verifica che   /*48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V9 sia  diverso da  True 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co6 non sia  uguale a  /*53,*/ 1130
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co6 non sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co10 non sia  maggiore di  /*54,*/ 13254
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V10 sia  diverso da  False 


 } Verifica che   /*47,49,51,*/  /*,*/  il timer MainClass_C1_timer_T9 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  uguale a  /*53,*/ 8
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co6 sia  uguale a  /*53,*/ 13
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co6 sia  maggiore di  /*54,*/ 125


 } Verifica che   /*47,49,51,*/  /*,*/  il timer MainClass_C1_timer_T10 non sia attivo
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  diverso da  /*56,*/ 11
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T2 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  diverso da RossoGialloxVerdex


 } Verifica che   /*47,48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C3 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  uguale a  /*53,*/ 4
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  minore di  /*55,*/ 133


 } Verifica che   /*48,49,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  diverso da  /*56,*/ 13025
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T2 sia attivo
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C3 sia  diverso da  False 
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T10 non sia disattivo


 } Verifica che   /*47,49,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  uguale a  /*53,*/ 15
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T9 sia attivo
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co10 non sia  minore di  /*55,*/ 113
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  diverso da RossoGialloxVerdex


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*34,*/  se il parametro MainClass_C1_parametro_P4 è  uguale a RossoGialloxVerdex /*37,*/ e  se la variabile MainClass_C1_variabile_V10 è  diverso da  False  /*37,*/ e  se la variabile MainClass_C1_variabile_V9 è  uguale a  True  /*36,*/ e  se il timer MainClass_C1_timer_T10 non è scaduto /*36,*/ o  se il timer MainClass_C1_timer_T10 è scaduto /*35,*/ o  se il controllo MainClass_C1_controllo_C3 non è  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*34,*/  se il parametro MainClass_C1_parametro_P4 è  uguale a RossoGialloxVerdex /*37,*/ e  se la variabile MainClass_C1_variabile_V10 è  diverso da  False  /*37,*/ e  se la variabile MainClass_C1_variabile_V9 è  uguale a  True  /*36,*/ e  se il timer MainClass_C1_timer_T10 non è scaduto /*36,*/ o  se il timer MainClass_C1_timer_T10 è scaduto""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*34,*/  se il parametro MainClass_C1_parametro_P4 è  uguale a RossoGialloxVerdex /*37,*/ e  se la variabile MainClass_C1_variabile_V10 è  diverso da  False  /*37,*/ e  se la variabile MainClass_C1_variabile_V9 è  uguale a  True  /*36,*/ e  se il timer MainClass_C1_timer_T10 non è scaduto""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*34,*/  se il parametro MainClass_C1_parametro_P4 è  uguale a RossoGialloxVerdex /*37,*/ e  se la variabile MainClass_C1_variabile_V10 è  diverso da  False  /*37,*/ e  se la variabile MainClass_C1_variabile_V9 è  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*34,*/  se il parametro MainClass_C1_parametro_P4 è  uguale a RossoGialloxVerdex /*37,*/ e  se la variabile MainClass_C1_variabile_V10 è  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\nil parametro MainClass_C1_parametro_P4 è  uguale a RossoGialloxVerdex""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V10 è  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v10)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nla variabile MainClass_C1_variabile_V9 è  uguale a  True""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T10 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t10' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T10 è scaduto""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C3 non è  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c3)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*63,*/  se il controllo ConsDef è uguale a FALSE , Solo una delle seguenti { 
 /*61,*/  se la macro  MainClass_C1_macrova_M3 ( con argomento_a6   uguale a True ,argomento_a5   uguale a RossoGiallox  e argomento_a10   uguale a avvio )   è  diverso da  False  /*40,*/  /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  /*53,*/ 131 /*36,*/ o  se il timer MainClass_C1_timer_T10 non è disattivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co6 non è  minore di  /*55,*/ 11 /*37,*/ o  se la variabile MainClass_C1_variabile_V9 è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*63,*/ /*34,*/  se il parametro MainClass_C1_parametro_P2 è  uguale a RossoGialloGiallo, Solo una delle seguenti { 
 /*62,*/  se la macro  MainClass_C1_macrova_M3 ( con argomento_a6   uguale a True ,argomento_a5   uguale a RossoGiallox  e argomento_a10   uguale a avvio )  non  è  uguale a  True  /*40,*/  o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P9 è  uguale a RossoGialloxVerdex /*36,*/ o  se il timer MainClass_C1_timer_T2 non è scaduto /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 non è  diverso da  /*56,*/ 14, Almeno una delle seguenti { 
 /*62,*/ /*36,*/  se il timer MainClass_C1_timer_T2 è disattivo /*36,*/ e  se il timer MainClass_C1_timer_T2 è attivo /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 non è  minore di  /*55,*/ 11 /*36,*/ o  se il timer MainClass_C1_timer_T9 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
 /*35,*/  se il controllo MainClass_C1_controllo_C6 è  uguale a  True , Verifica che   /*48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V9 sia  diverso da  True 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co6 non sia  uguale a  /*53,*/ 1130
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co6 non sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co10 non sia  maggiore di  /*54,*/ 13254
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V10 sia  diverso da  False 


 } Verifica che   /*47,49,51,*/  /*,*/  il timer MainClass_C1_timer_T9 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  uguale a  /*53,*/ 8
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co6 sia  uguale a  /*53,*/ 13
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co6 sia  maggiore di  /*54,*/ 125


 } Verifica che   /*47,49,51,*/  /*,*/  il timer MainClass_C1_timer_T10 non sia attivo
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  diverso da  /*56,*/ 11
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T2 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  diverso da RossoGialloxVerdex


 } Verifica che   /*47,48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C3 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  uguale a  /*53,*/ 4
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  minore di  /*55,*/ 133


 } Verifica che   /*48,49,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  diverso da  /*56,*/ 13025
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T2 sia attivo
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C3 sia  diverso da  False 
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T10 non sia disattivo


 } Verifica che   /*47,49,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  uguale a  /*53,*/ 15
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T9 sia attivo
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co10 non sia  minore di  /*55,*/ 113
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  diverso da RossoGialloxVerdex


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/  se il controllo ConsDef è uguale a FALSE , Solo una delle seguenti { 
 /*61,*/  se la macro  MainClass_C1_macrova_M3 ( con argomento_a6   uguale a True ,argomento_a5   uguale a RossoGiallox  e argomento_a10   uguale a avvio )   è  diverso da  False  /*40,*/  /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  /*53,*/ 131 /*36,*/ o  se il timer MainClass_C1_timer_T10 non è disattivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co6 non è  minore di  /*55,*/ 11 /*37,*/ o  se la variabile MainClass_C1_variabile_V9 è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*63,*/ /*34,*/  se il parametro MainClass_C1_parametro_P2 è  uguale a RossoGialloGiallo, Solo una delle seguenti { 
 /*62,*/  se la macro  MainClass_C1_macrova_M3 ( con argomento_a6   uguale a True ,argomento_a5   uguale a RossoGiallox  e argomento_a10   uguale a avvio )  non  è  uguale a  True  /*40,*/  o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P9 è  uguale a RossoGialloxVerdex /*36,*/ o  se il timer MainClass_C1_timer_T2 non è scaduto /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 non è  diverso da  /*56,*/ 14, Almeno una delle seguenti { 
 /*62,*/ /*36,*/  se il timer MainClass_C1_timer_T2 è disattivo /*36,*/ e  se il timer MainClass_C1_timer_T2 è attivo /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 non è  minore di  /*55,*/ 11 /*36,*/ o  se il timer MainClass_C1_timer_T9 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
 /*35,*/  se il controllo MainClass_C1_controllo_C6 è  uguale a  True , Verifica che   /*48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V9 sia  diverso da  True 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co6 non sia  uguale a  /*53,*/ 1130
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co6 non sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co10 non sia  maggiore di  /*54,*/ 13254
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V10 sia  diverso da  False 


 } Verifica che   /*47,49,51,*/  /*,*/  il timer MainClass_C1_timer_T9 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  uguale a  /*53,*/ 8
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co6 sia  uguale a  /*53,*/ 13
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co6 sia  maggiore di  /*54,*/ 125


 } Verifica che   /*47,49,51,*/  /*,*/  il timer MainClass_C1_timer_T10 non sia attivo
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  diverso da  /*56,*/ 11
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T2 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  diverso da RossoGialloxVerdex


 } Verifica che   /*47,48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C3 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  uguale a  /*53,*/ 4
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  minore di  /*55,*/ 133


 } Verifica che   /*48,49,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  diverso da  /*56,*/ 13025
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T2 sia attivo
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C3 sia  diverso da  False 
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T10 non sia disattivo


 }""", [
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef è uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*61,*/  se la macro  MainClass_C1_macrova_M3 ( con argomento_a6   uguale a True ,argomento_a5   uguale a RossoGiallox  e argomento_a10   uguale a avvio )   è  diverso da  False  /*40,*/  /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  /*53,*/ 131 /*36,*/ o  se il timer MainClass_C1_timer_T10 non è disattivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co6 non è  minore di  /*55,*/ 11 /*37,*/ o  se la variabile MainClass_C1_variabile_V9 è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*63,*/ /*34,*/  se il parametro MainClass_C1_parametro_P2 è  uguale a RossoGialloGiallo, Solo una delle seguenti { 
 /*62,*/  se la macro  MainClass_C1_macrova_M3 ( con argomento_a6   uguale a True ,argomento_a5   uguale a RossoGiallox  e argomento_a10   uguale a avvio )  non  è  uguale a  True  /*40,*/  o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P9 è  uguale a RossoGialloxVerdex /*36,*/ o  se il timer MainClass_C1_timer_T2 non è scaduto /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 non è  diverso da  /*56,*/ 14, Almeno una delle seguenti { 
 /*62,*/ /*36,*/  se il timer MainClass_C1_timer_T2 è disattivo /*36,*/ e  se il timer MainClass_C1_timer_T2 è attivo /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 non è  minore di  /*55,*/ 11 /*36,*/ o  se il timer MainClass_C1_timer_T9 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
 /*35,*/  se il controllo MainClass_C1_controllo_C6 è  uguale a  True , Verifica che   /*48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V9 sia  diverso da  True 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co6 non sia  uguale a  /*53,*/ 1130
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co6 non sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co10 non sia  maggiore di  /*54,*/ 13254
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V10 sia  diverso da  False 


 } Verifica che   /*47,49,51,*/  /*,*/  il timer MainClass_C1_timer_T9 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  uguale a  /*53,*/ 8
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co6 sia  uguale a  /*53,*/ 13
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co6 sia  maggiore di  /*54,*/ 125


 } Verifica che   /*47,49,51,*/  /*,*/  il timer MainClass_C1_timer_T10 non sia attivo
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  diverso da  /*56,*/ 11
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T2 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  diverso da RossoGialloxVerdex


 } Verifica che   /*47,48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C3 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  uguale a  /*53,*/ 4
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  minore di  /*55,*/ 133


 } Verifica che   /*48,49,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  diverso da  /*56,*/ 13025
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T2 sia attivo
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C3 sia  diverso da  False 
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T10 non sia disattivo


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/  se la macro  MainClass_C1_macrova_M3 ( con argomento_a6   uguale a True ,argomento_a5   uguale a RossoGiallox  e argomento_a10   uguale a avvio )   è  diverso da  False  /*40,*/  /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  /*53,*/ 131 /*36,*/ o  se il timer MainClass_C1_timer_T10 non è disattivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co6 non è  minore di  /*55,*/ 11 /*37,*/ o  se la variabile MainClass_C1_variabile_V9 è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*63,*/ /*34,*/  se il parametro MainClass_C1_parametro_P2 è  uguale a RossoGialloGiallo, Solo una delle seguenti { 
 /*62,*/  se la macro  MainClass_C1_macrova_M3 ( con argomento_a6   uguale a True ,argomento_a5   uguale a RossoGiallox  e argomento_a10   uguale a avvio )  non  è  uguale a  True  /*40,*/  o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P9 è  uguale a RossoGialloxVerdex /*36,*/ o  se il timer MainClass_C1_timer_T2 non è scaduto /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 non è  diverso da  /*56,*/ 14, Almeno una delle seguenti { 
 /*62,*/ /*36,*/  se il timer MainClass_C1_timer_T2 è disattivo /*36,*/ e  se il timer MainClass_C1_timer_T2 è attivo /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 non è  minore di  /*55,*/ 11 /*36,*/ o  se il timer MainClass_C1_timer_T9 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
 /*35,*/  se il controllo MainClass_C1_controllo_C6 è  uguale a  True , Verifica che   /*48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V9 sia  diverso da  True 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co6 non sia  uguale a  /*53,*/ 1130
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co6 non sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co10 non sia  maggiore di  /*54,*/ 13254
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V10 sia  diverso da  False 


 } Verifica che   /*47,49,51,*/  /*,*/  il timer MainClass_C1_timer_T9 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  uguale a  /*53,*/ 8
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co6 sia  uguale a  /*53,*/ 13
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co6 sia  maggiore di  /*54,*/ 125


 } Verifica che   /*47,49,51,*/  /*,*/  il timer MainClass_C1_timer_T10 non sia attivo
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  diverso da  /*56,*/ 11
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T2 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  diverso da RossoGialloxVerdex


 } Verifica che   /*47,48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C3 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  uguale a  /*53,*/ 4
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  minore di  /*55,*/ 133


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/  se la macro  MainClass_C1_macrova_M3 ( con argomento_a6   uguale a True ,argomento_a5   uguale a RossoGiallox  e argomento_a10   uguale a avvio )   è  diverso da  False  /*40,*/  /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  /*53,*/ 131 /*36,*/ o  se il timer MainClass_C1_timer_T10 non è disattivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co6 non è  minore di  /*55,*/ 11 /*37,*/ o  se la variabile MainClass_C1_variabile_V9 è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/  se la macro  MainClass_C1_macrova_M3 ( con argomento_a6   uguale a True ,argomento_a5   uguale a RossoGiallox  e argomento_a10   uguale a avvio )   è  diverso da  False  /*40,*/  /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  /*53,*/ 131 /*36,*/ o  se il timer MainClass_C1_timer_T10 non è disattivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co6 non è  minore di  /*55,*/ 11 /*37,*/ o  se la variabile MainClass_C1_variabile_V9 è  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/  se la macro  MainClass_C1_macrova_M3 ( con argomento_a6   uguale a True ,argomento_a5   uguale a RossoGiallox  e argomento_a10   uguale a avvio )   è  diverso da  False  /*40,*/  /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  /*53,*/ 131 /*36,*/ o  se il timer MainClass_C1_timer_T10 non è disattivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co6 non è  minore di  /*55,*/ 11""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/  se la macro  MainClass_C1_macrova_M3 ( con argomento_a6   uguale a True ,argomento_a5   uguale a RossoGiallox  e argomento_a10   uguale a avvio )   è  diverso da  False  /*40,*/  /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  /*53,*/ 131 /*36,*/ o  se il timer MainClass_C1_timer_T10 non è disattivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/  se la macro  MainClass_C1_macrova_M3 ( con argomento_a6   uguale a True ,argomento_a5   uguale a RossoGiallox  e argomento_a10   uguale a avvio )   è  diverso da  False  /*40,*/  /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  /*53,*/ 131""", [
                            DIBoolExpr("""Operatore Logico Not\nla macro  MainClass_C1_macrova_M3 ( con argomento_a6   uguale a True ,argomento_a5   uguale a RossoGiallox  e argomento_a10   uguale a avvio )   è  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m3')  è uguale a  (False)""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroMainclass_c1_macrova_m3'"""),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co7 non è  uguale a  /*53,*/ 131""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co7)  è uguale a  (131)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T10 non è disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t10' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co6 non è  minore di  /*55,*/ 11""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co6)  è minore di  (11)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nla variabile MainClass_C1_variabile_V9 è  uguale a  False""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*63,*/ /*34,*/  se il parametro MainClass_C1_parametro_P2 è  uguale a RossoGialloGiallo, Solo una delle seguenti { 
 /*62,*/  se la macro  MainClass_C1_macrova_M3 ( con argomento_a6   uguale a True ,argomento_a5   uguale a RossoGiallox  e argomento_a10   uguale a avvio )  non  è  uguale a  True  /*40,*/  o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P9 è  uguale a RossoGialloxVerdex /*36,*/ o  se il timer MainClass_C1_timer_T2 non è scaduto /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 non è  diverso da  /*56,*/ 14, Almeno una delle seguenti { 
 /*62,*/ /*36,*/  se il timer MainClass_C1_timer_T2 è disattivo /*36,*/ e  se il timer MainClass_C1_timer_T2 è attivo /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 non è  minore di  /*55,*/ 11 /*36,*/ o  se il timer MainClass_C1_timer_T9 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
 /*35,*/  se il controllo MainClass_C1_controllo_C6 è  uguale a  True , Verifica che   /*48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V9 sia  diverso da  True 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co6 non sia  uguale a  /*53,*/ 1130
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co6 non sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co10 non sia  maggiore di  /*54,*/ 13254
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V10 sia  diverso da  False 


 } Verifica che   /*47,49,51,*/  /*,*/  il timer MainClass_C1_timer_T9 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  uguale a  /*53,*/ 8
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co6 sia  uguale a  /*53,*/ 13
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co6 sia  maggiore di  /*54,*/ 125


 } Verifica che   /*47,49,51,*/  /*,*/  il timer MainClass_C1_timer_T10 non sia attivo
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  diverso da  /*56,*/ 11
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T2 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  diverso da RossoGialloxVerdex


 } Verifica che   /*47,48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C3 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  uguale a  /*53,*/ 4
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  minore di  /*55,*/ 133


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*34,*/  se il parametro MainClass_C1_parametro_P2 è  uguale a RossoGialloGiallo, Solo una delle seguenti { 
 /*62,*/  se la macro  MainClass_C1_macrova_M3 ( con argomento_a6   uguale a True ,argomento_a5   uguale a RossoGiallox  e argomento_a10   uguale a avvio )  non  è  uguale a  True  /*40,*/  o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P9 è  uguale a RossoGialloxVerdex /*36,*/ o  se il timer MainClass_C1_timer_T2 non è scaduto /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 non è  diverso da  /*56,*/ 14, Almeno una delle seguenti { 
 /*62,*/ /*36,*/  se il timer MainClass_C1_timer_T2 è disattivo /*36,*/ e  se il timer MainClass_C1_timer_T2 è attivo /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 non è  minore di  /*55,*/ 11 /*36,*/ o  se il timer MainClass_C1_timer_T9 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
 /*35,*/  se il controllo MainClass_C1_controllo_C6 è  uguale a  True , Verifica che   /*48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V9 sia  diverso da  True 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co6 non sia  uguale a  /*53,*/ 1130
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co6 non sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co10 non sia  maggiore di  /*54,*/ 13254
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V10 sia  diverso da  False 


 } Verifica che   /*47,49,51,*/  /*,*/  il timer MainClass_C1_timer_T9 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  uguale a  /*53,*/ 8
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co6 sia  uguale a  /*53,*/ 13
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co6 sia  maggiore di  /*54,*/ 125


 } Verifica che   /*47,49,51,*/  /*,*/  il timer MainClass_C1_timer_T10 non sia attivo
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  diverso da  /*56,*/ 11
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T2 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  diverso da RossoGialloxVerdex


 }""", [
                            DIBoolExpr("""EqualImpl\nil parametro MainClass_C1_parametro_P2 è  uguale a RossoGialloGiallo""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*62,*/  se la macro  MainClass_C1_macrova_M3 ( con argomento_a6   uguale a True ,argomento_a5   uguale a RossoGiallox  e argomento_a10   uguale a avvio )  non  è  uguale a  True  /*40,*/  o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P9 è  uguale a RossoGialloxVerdex /*36,*/ o  se il timer MainClass_C1_timer_T2 non è scaduto /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 non è  diverso da  /*56,*/ 14, Almeno una delle seguenti { 
 /*62,*/ /*36,*/  se il timer MainClass_C1_timer_T2 è disattivo /*36,*/ e  se il timer MainClass_C1_timer_T2 è attivo /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 non è  minore di  /*55,*/ 11 /*36,*/ o  se il timer MainClass_C1_timer_T9 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
 /*35,*/  se il controllo MainClass_C1_controllo_C6 è  uguale a  True , Verifica che   /*48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V9 sia  diverso da  True 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co6 non sia  uguale a  /*53,*/ 1130
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co6 non sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co10 non sia  maggiore di  /*54,*/ 13254
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V10 sia  diverso da  False 


 } Verifica che   /*47,49,51,*/  /*,*/  il timer MainClass_C1_timer_T9 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  uguale a  /*53,*/ 8
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co6 sia  uguale a  /*53,*/ 13
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co6 sia  maggiore di  /*54,*/ 125


 } Verifica che   /*47,49,51,*/  /*,*/  il timer MainClass_C1_timer_T10 non sia attivo
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  diverso da  /*56,*/ 11
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T2 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  diverso da RossoGialloxVerdex


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/  se la macro  MainClass_C1_macrova_M3 ( con argomento_a6   uguale a True ,argomento_a5   uguale a RossoGiallox  e argomento_a10   uguale a avvio )  non  è  uguale a  True  /*40,*/  o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P9 è  uguale a RossoGialloxVerdex /*36,*/ o  se il timer MainClass_C1_timer_T2 non è scaduto /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 non è  diverso da  /*56,*/ 14, Almeno una delle seguenti { 
 /*62,*/ /*36,*/  se il timer MainClass_C1_timer_T2 è disattivo /*36,*/ e  se il timer MainClass_C1_timer_T2 è attivo /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 non è  minore di  /*55,*/ 11 /*36,*/ o  se il timer MainClass_C1_timer_T9 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
 /*35,*/  se il controllo MainClass_C1_controllo_C6 è  uguale a  True , Verifica che   /*48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V9 sia  diverso da  True 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co6 non sia  uguale a  /*53,*/ 1130
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co6 non sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co10 non sia  maggiore di  /*54,*/ 13254
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V10 sia  diverso da  False 


 } Verifica che   /*47,49,51,*/  /*,*/  il timer MainClass_C1_timer_T9 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  uguale a  /*53,*/ 8
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co6 sia  uguale a  /*53,*/ 13
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co6 sia  maggiore di  /*54,*/ 125


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/  se la macro  MainClass_C1_macrova_M3 ( con argomento_a6   uguale a True ,argomento_a5   uguale a RossoGiallox  e argomento_a10   uguale a avvio )  non  è  uguale a  True  /*40,*/  o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P9 è  uguale a RossoGialloxVerdex /*36,*/ o  se il timer MainClass_C1_timer_T2 non è scaduto /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 non è  diverso da  /*56,*/ 14""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/  se la macro  MainClass_C1_macrova_M3 ( con argomento_a6   uguale a True ,argomento_a5   uguale a RossoGiallox  e argomento_a10   uguale a avvio )  non  è  uguale a  True  /*40,*/  o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P9 è  uguale a RossoGialloxVerdex""", [
                            DIBoolExpr("""Operatore Logico Not\nla macro  MainClass_C1_macrova_M3 ( con argomento_a6   uguale a True ,argomento_a5   uguale a RossoGiallox  e argomento_a10   uguale a avvio )  non  è  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m3')  è uguale a  (True)""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroMainclass_c1_macrova_m3'"""),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P9 è  uguale a RossoGialloxVerdex""", [
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil parametro MainClass_C1_parametro_P9 è  uguale a RossoGialloxVerdex""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il timer MainClass_C1_timer_T2 non è scaduto /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 non è  diverso da  /*56,*/ 14""", [
                            DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T2 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t2' è scaduto""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co5 non è  diverso da  /*56,*/ 14""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co5)  è uguale a  (14))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co5)  è uguale a  (14)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*62,*/ /*36,*/  se il timer MainClass_C1_timer_T2 è disattivo /*36,*/ e  se il timer MainClass_C1_timer_T2 è attivo /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 non è  minore di  /*55,*/ 11 /*36,*/ o  se il timer MainClass_C1_timer_T9 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
 /*35,*/  se il controllo MainClass_C1_controllo_C6 è  uguale a  True , Verifica che   /*48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V9 sia  diverso da  True 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co6 non sia  uguale a  /*53,*/ 1130
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co6 non sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co10 non sia  maggiore di  /*54,*/ 13254
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V10 sia  diverso da  False 


 } Verifica che   /*47,49,51,*/  /*,*/  il timer MainClass_C1_timer_T9 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  uguale a  /*53,*/ 8
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co6 sia  uguale a  /*53,*/ 13
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co6 sia  maggiore di  /*54,*/ 125


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*36,*/  se il timer MainClass_C1_timer_T2 è disattivo /*36,*/ e  se il timer MainClass_C1_timer_T2 è attivo /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 non è  minore di  /*55,*/ 11 /*36,*/ o  se il timer MainClass_C1_timer_T9 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
 /*35,*/  se il controllo MainClass_C1_controllo_C6 è  uguale a  True , Verifica che   /*48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V9 sia  diverso da  True 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co6 non sia  uguale a  /*53,*/ 1130
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co6 non sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co10 non sia  maggiore di  /*54,*/ 13254
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V10 sia  diverso da  False 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*36,*/  se il timer MainClass_C1_timer_T2 è disattivo /*36,*/ e  se il timer MainClass_C1_timer_T2 è attivo /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 non è  minore di  /*55,*/ 11 /*36,*/ o  se il timer MainClass_C1_timer_T9 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*36,*/  se il timer MainClass_C1_timer_T2 è disattivo /*36,*/ e  se il timer MainClass_C1_timer_T2 è attivo /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 non è  minore di  /*55,*/ 11""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*36,*/  se il timer MainClass_C1_timer_T2 è disattivo /*36,*/ e  se il timer MainClass_C1_timer_T2 è attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T2 è disattivo""", [
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T2 è attivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co5 non è  minore di  /*55,*/ 11""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co5)  è minore di  (11)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il timer MainClass_C1_timer_T9 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T9 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t9' è scaduto""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*35,*/  se il controllo MainClass_C1_controllo_C6 è  uguale a  True , Verifica che   /*48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V9 sia  diverso da  True 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co6 non sia  uguale a  /*53,*/ 1130
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co6 non sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co10 non sia  maggiore di  /*54,*/ 13254
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V10 sia  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\nil controllo MainClass_C1_controllo_C6 è  uguale a  True""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V9 sia  diverso da  True 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co6 non sia  uguale a  /*53,*/ 1130
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co6 non sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co10 non sia  maggiore di  /*54,*/ 13254
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V10 sia  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V9 sia  diverso da  True 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co6 non sia  uguale a  /*53,*/ 1130
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co6 non sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co10 non sia  maggiore di  /*54,*/ 13254""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V9 sia  diverso da  True 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co6 non sia  uguale a  /*53,*/ 1130
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co6 non sia  maggiore di  /*54,*/ 11""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V9 sia  diverso da  True 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co6 non sia  uguale a  /*53,*/ 1130""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V9 sia  diverso da  True 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V9 sia  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v9)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore MainClass_C1_contatore_Co6 non sia  uguale a  /*53,*/ 1130""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co6)  è uguale a  (1130)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*38,*/  il contatore MainClass_C1_contatore_Co6 non sia  maggiore di  /*54,*/ 11""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co6)  è maggiore di  (11)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*38,*/  il contatore MainClass_C1_contatore_Co10 non sia  maggiore di  /*54,*/ 13254""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co10)  è maggiore di  (13254)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*37,*/  la variabile MainClass_C1_variabile_V10 sia  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v10)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,51,*/  /*,*/  il timer MainClass_C1_timer_T9 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  uguale a  /*53,*/ 8
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co6 sia  uguale a  /*53,*/ 13
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co6 sia  maggiore di  /*54,*/ 125""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,51,*/  /*,*/  il timer MainClass_C1_timer_T9 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  uguale a  /*53,*/ 8
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co6 sia  uguale a  /*53,*/ 13""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,49,51,*/  /*,*/  il timer MainClass_C1_timer_T9 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  uguale a  /*53,*/ 8""", [
                            DIBoolExpr("""Predicato Oggetto\nche   /*47,49,51,*/  /*,*/  il timer MainClass_C1_timer_T9 sia scaduto""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  uguale a  /*53,*/ 8""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p8)  è uguale a  (8)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  il contatore MainClass_C1_contatore_Co6 sia  uguale a  /*53,*/ 13""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nche  /*38,*/  il contatore MainClass_C1_contatore_Co6 sia  maggiore di  /*54,*/ 125""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,49,51,*/  /*,*/  il timer MainClass_C1_timer_T10 non sia attivo
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  diverso da  /*56,*/ 11
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T2 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  diverso da RossoGialloxVerdex""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,49,51,*/  /*,*/  il timer MainClass_C1_timer_T10 non sia attivo
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  diverso da  /*56,*/ 11
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T2 sia scaduto""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,49,51,*/  /*,*/  il timer MainClass_C1_timer_T10 non sia attivo
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  diverso da  /*56,*/ 11""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,49,51,*/  /*,*/  il timer MainClass_C1_timer_T10 non sia attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t10' è attivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  diverso da  /*56,*/ 11""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co7)  è uguale a  (11))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co7)  è uguale a  (11)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*36,*/  il timer MainClass_C1_timer_T2 sia scaduto""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  diverso da RossoGialloxVerdex""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p9)  è uguale a  (rossogialloxverdex))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p9)  è uguale a  (rossogialloxverdex)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C3 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  uguale a  /*53,*/ 4
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  minore di  /*55,*/ 133""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C3 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  uguale a  /*53,*/ 4""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C3 non sia  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""EqualImpl\nche   /*47,48,51,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo MainClass_C1_controllo_C3 non sia  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c3)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  uguale a  /*53,*/ 4""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p8)  è uguale a  (4)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  minore di  /*55,*/ 133""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co7)  è minore di  (133)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,49,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  diverso da  /*56,*/ 13025
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T2 sia attivo
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C3 sia  diverso da  False 
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T10 non sia disattivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,49,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  diverso da  /*56,*/ 13025
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T2 sia attivo
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C3 sia  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,49,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  diverso da  /*56,*/ 13025
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T2 sia attivo""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,49,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  diverso da  /*56,*/ 13025""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co7)  è uguale a  (13025))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co7)  è uguale a  (13025)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer MainClass_C1_timer_T2 sia attivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo MainClass_C1_controllo_C3 sia  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c3)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*36,*/  il timer MainClass_C1_timer_T10 non sia disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t10' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  uguale a  /*53,*/ 15
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T9 sia attivo
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co10 non sia  minore di  /*55,*/ 113
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  diverso da RossoGialloxVerdex""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,49,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  uguale a  /*53,*/ 15
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T9 sia attivo
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co10 non sia  minore di  /*55,*/ 113""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,49,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  uguale a  /*53,*/ 15
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T9 sia attivo""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,49,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  uguale a  /*53,*/ 15""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co7)  è uguale a  (15)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer MainClass_C1_timer_T9 sia attivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*38,*/  il contatore MainClass_C1_contatore_Co10 non sia  minore di  /*55,*/ 113""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co10)  è minore di  (113)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  diverso da RossoGialloxVerdex""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p4)  è uguale a  (rossogialloxverdex)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,50,*/  /*,*/  il timer MainClass_C1_timer_T10 sia disattivo
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V10 sia  diverso da  True 
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V10 sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C3 sia  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,50,*/  /*,*/  il timer MainClass_C1_timer_T10 sia disattivo
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V10 sia  diverso da  True 
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V10 sia  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,49,50,*/  /*,*/  il timer MainClass_C1_timer_T10 sia disattivo
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V10 sia  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,49,50,*/  /*,*/  il timer MainClass_C1_timer_T10 sia disattivo
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""Predicato Oggetto\nche   /*48,49,50,*/  /*,*/  il timer MainClass_C1_timer_T10 sia disattivo""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile MainClass_C1_variabile_V10 sia  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v10)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*37,*/  la variabile MainClass_C1_variabile_V10 sia  uguale a  True""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  il controllo MainClass_C1_controllo_C3 sia  uguale a  False""", [
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroMainclass_c1_macrove_m8_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db((db((db((db(self.get_mainclass_c1_parametro_p4() == GlobalEnumeration.rossogialloxverdex, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v10() == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_variabile_v9() == True, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_timer_t10().isScaduto(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_timer_t10().isScaduto(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_controllo_c3() == True, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db((db((db((db((db((db(not db(db(self.macroMainclass_c1_macrova_m3(GlobalEnumeration.avvio,GlobalEnumeration.rossogiallox,True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co7().get_valore() == 131, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_timer_t10().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_contatore_co6().get_valore() < 11, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_variabile_v9() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_parametro_p2() == GlobalEnumeration.rossogiallogiallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db((db((db(not db(db(self.macroMainclass_c1_macrova_m3(GlobalEnumeration.avvio,GlobalEnumeration.rossogiallox,True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_parametro_p9() == GlobalEnumeration.rossogialloxverdex, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_timer_t2().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_mainclass_c1_contatore_co5().get_valore() == 14, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db((db(self.get_mainclass_c1_timer_t2().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_timer_t2().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co5().get_valore() < 11, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_timer_t9().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_controllo_c6() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db((db((db((db(not db(self.get_mainclass_c1_variabile_v9() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co6().get_valore() == 1130, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co6().get_valore() > 11, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_contatore_co10().get_valore() > 13254, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(not db(self.get_mainclass_c1_variabile_v10() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db((db(self.get_mainclass_c1_timer_t9().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p8() == 8, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(self.get_mainclass_c1_contatore_co6().get_valore() == 13, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(self.get_mainclass_c1_contatore_co6().get_valore() > 125, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db((db((db((db(not db(self.get_mainclass_c1_timer_t10().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_contatore_co7().get_valore() == 11, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(self.get_mainclass_c1_timer_t2().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) and db(not db(not db(self.get_mainclass_c1_parametro_p9() == GlobalEnumeration.rossogialloxverdex, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db((db((db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c3() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p8() == 4, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(not db(self.get_mainclass_c1_contatore_co7().get_valore() < 133, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db((db((db((db(not db(not db(self.get_mainclass_c1_contatore_co7().get_valore() == 13025, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_timer_t2().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c3() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_timer_t10().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db((db((db((db(not db(self.get_mainclass_c1_contatore_co7().get_valore() == 15, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_timer_t9().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co10().get_valore() < 113, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) or db(not db(self.get_mainclass_c1_parametro_p4() == GlobalEnumeration.rossogialloxverdex, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db((db((db((db(self.get_mainclass_c1_timer_t10().isDisattivato(), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v10() == True, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[0]) or db(self.get_mainclass_c1_variabile_v10() == True, di_ctx.subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0]) or db(self.get_mainclass_c1_controllo_c3() == False, di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    # value macros
    @srf_value_macro("macroMainclass_c1_macrova_m1")
    def macroMainclass_c1_macrova_m1(self, argomento_a10, argomento_a2, argomento_a3, argomento_a5, argomento_a6, argomento_a8, argomento_a9, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}
         commento: {46,} assegna alla macro il valore RossoGialloGiallo commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m1_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                ])

        populate_macroMainclass_c1_macrova_m1_SrfMacroDefInfo(di_ctx)
        
        #  /*[*/
        #   /*46,*/ assegna alla macro il valore RossoGialloGiallo
        return GlobalEnumeration.rossogiallogiallo
    
    @srf_value_macro("macroMainclass_c1_macrova_m3")
    def macroMainclass_c1_macrova_m3(self, argomento_a10, argomento_a5, argomento_a6, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}
         commento: {46,} assegna alla macro il valore  False  commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m3_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                ])

        populate_macroMainclass_c1_macrova_m3_SrfMacroDefInfo(di_ctx)
        
        #  /*[*/
        #   /*46,*/ assegna alla macro il valore  False
        return False
    
    @srf_value_macro("macroMainclass_c1_macrova_m5")
    def macroMainclass_c1_macrova_m5(self, argomento_a1, argomento_a2, argomento_a4, argomento_a7, argomento_a8, argomento_a9, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}
         commento: {46,} assegna alla macro il valore RossoGialloxVerdex commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m5_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                ])

        populate_macroMainclass_c1_macrova_m5_SrfMacroDefInfo(di_ctx)
        
        #  /*[*/
        #   /*46,*/ assegna alla macro il valore RossoGialloxVerdex
        return GlobalEnumeration.rossogialloxverdex
    
    @srf_value_macro("macroMainclass_c1_macrova_m6")
    def macroMainclass_c1_macrova_m6(self, argomento_a1, argomento_a3, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[} commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI2 non è attivo commento: {34,} e  se il parametro MainClass_C1_parametro_P8 non è  uguale a  commento: {53,} 4 commento: {37,} e  se la variabile MainClass_C1_variabile_V10 è  diverso da  False  commento: {34,} e  se il parametro MainClass_C1_parametro_P2 è  uguale a RossoGialloGiallo , assegna alla macro il valore  True 
        
         commento: {46,} assegna alla macro il valore  False  commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m6_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI2 non è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P8 non è  uguale a  /*53,*/ 4 /*37,*/ e  se la variabile MainClass_C1_variabile_V10 è  diverso da  False  /*34,*/ e  se il parametro MainClass_C1_parametro_P2 è  uguale a RossoGialloGiallo , assegna alla macro il valore  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*[*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI2 non è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P8 non è  uguale a  /*53,*/ 4 /*37,*/ e  se la variabile MainClass_C1_variabile_V10 è  diverso da  False  /*34,*/ e  se il parametro MainClass_C1_parametro_P2 è  uguale a RossoGialloGiallo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di (il timer 'mainclass_c1_restoreti_ti2_restore' è attivo) )  e  ( negazione di ((mainclass_c1_parametro_p8)  è uguale a  (4)) ) )  e  ( negazione di ((mainclass_c1_variabile_v10)  è uguale a  (False)) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (il timer 'mainclass_c1_restoreti_ti2_restore' è attivo) )  e  ( negazione di ((mainclass_c1_parametro_p8)  è uguale a  (4)) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_restoreti_ti2_restore' è attivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_restoreti_ti2_restore' è attivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p8)  è uguale a  (4))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p8)  è uguale a  (4)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v10)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v10)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p2)  è uguale a  (rossogiallogiallo)""", [
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macrova_m6_SrfMacroDefInfo(di_ctx)
        #  /*[*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI2 non è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P8 non è  uguale a  /*53,*/ 4 /*37,*/ e  se la variabile MainClass_C1_variabile_V10 è  diverso da  False  /*34,*/ e  se il parametro MainClass_C1_parametro_P2 è  uguale a RossoGialloGiallo , assegna alla macro il valore  True
        if db((db((db((db(not db(self.get_mainclass_c1_restoreti_ti2_restore().isAttivato(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p8() == 4, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v10() == False, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_parametro_p2() == GlobalEnumeration.rossogiallogiallo, di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            return True
        #  /*46,*/ assegna alla macro il valore  False
        return False
    
    @srf_value_macro("macroMainclass_c1_macrova_m7")
    def macroMainclass_c1_macrova_m7(self, argomento_a1, argomento_a3, argomento_a4, argomento_a5, argomento_a6, argomento_a7, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}
         commento: {46,} assegna alla macro il valore RossoGialloGiallo commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m7_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                ])

        populate_macroMainclass_c1_macrova_m7_SrfMacroDefInfo(di_ctx)
        
        #  /*[*/
        #   /*46,*/ assegna alla macro il valore RossoGialloGiallo
        return GlobalEnumeration.rossogiallogiallo
    
    # for each manual command, the corresponding method is created
    def eventMainclass_c1_command_comm4(self, notifying_process):
        notifying_process.response_notify_man_cmd(self, 'eventMainclass_c1_command_comm4')
    
    def eventMainclass_c1_command_comm5(self, notifying_process):
        notifying_process.response_notify_man_cmd(self, 'eventMainclass_c1_command_comm5')
    
    def eventMainclass_c1_command_comm6(self, notifying_process):
        notifying_process.response_notify_man_cmd(self, 'eventMainclass_c1_command_comm6')
    
    # for each automatic command, the corresponding method is created
    def eventMainclass_c1_command_comm3(self, notifying_process):
        notifying_process.response_notify_auto_cmd(self, 'eventMainclass_c1_command_comm3')
    

    def update_precedente(self):
        # update the variables with previous value
        self.set_mainclass_c1_previousco_c1_prev(self.get_mainclass_c1_previousco_c1())
        self.set_mainclass_c1_previousco_c2_prev(self.get_mainclass_c1_previousco_c2())
        self.set_mainclass_c1_previousco_c4_prev(self.get_mainclass_c1_previousco_c4())
        self.set_mainclass_c1_previousco_c7_prev(self.get_mainclass_c1_previousco_c7())
        self.set_mainclass_c1_previousva_pv1_prev(self.get_mainclass_c1_previousva_pv1())
        self.set_mainclass_c1_previousva_pv2_prev(self.get_mainclass_c1_previousva_pv2())
        self.set_mainclass_c1_previousva_pv3_prev(self.get_mainclass_c1_previousva_pv3())
        self.set_mainclass_c1_previousva_pv4_prev(self.get_mainclass_c1_previousva_pv4())

