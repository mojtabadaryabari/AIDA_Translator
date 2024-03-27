# Codice del modello 'TestCase24', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
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

        self.set_mainclass_c1_previousva_pv1(GlobalEnumeration.avanzamentox)
        self.set_mainclass_c1_previousva_pv2(0)
        self.set_mainclass_c1_previousva_pv3(GlobalEnumeration.gialloverde)
        self.set_mainclass_c1_previousva_pv4(GlobalEnumeration.verde)
        self.set_mainclass_c1_restoreva_rv1(0)
        self.set_mainclass_c1_restoreva_rv2(False)
        self.set_mainclass_c1_restoreva_rv3(False)
        self.set_mainclass_c1_restoreva_rv4(False)
        self.set_mainclass_c1_restoreva_rv5(False)
        self.set_mainclass_c1_variabile_v2(0)
        self.set_mainclass_c1_variabile_v3(False)
        self.set_mainclass_c1_variabile_v4(False)
        self.set_mainclass_c1_variabile_v8(0)

        self._expected_commands_map = {
            Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1 : set([]),
        }

    def set_expected_cmds_response(self):
        # for each manual command of MainClass_C1
        if self.is_triggered('eventMainclass_c1_command_comm2DaSender127c0aca'):
            self.set_man_cmd_response('eventMainclass_c1_command_comm2DaSender127c0aca',self.ManCmdResponse.UNEXPECTED)
        else:
            self.set_man_cmd_response('eventMainclass_c1_command_comm2DaSender127c0aca',self.ManCmdResponse.NOOP)
        if self.is_triggered('eventMainclass_c1_command_comm5DaSender83c691f2'):
            self.set_man_cmd_response('eventMainclass_c1_command_comm5DaSender83c691f2',self.ManCmdResponse.UNEXPECTED)
        else:
            self.set_man_cmd_response('eventMainclass_c1_command_comm5DaSender83c691f2',self.ManCmdResponse.NOOP)
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
    def init_configuration(self, mainclass_c1_parametro_p1, mainclass_c1_parametro_p10, mainclass_c1_parametro_p3, mainclass_c1_parametro_p6, mainclass_c1_parametro_p8):
        # initialize the record type parameters
        # initialize the simple type parameters
        self.set_mainclass_c1_parametro_p1(mainclass_c1_parametro_p1)
        self.set_mainclass_c1_parametro_p10(mainclass_c1_parametro_p10)
        self.set_mainclass_c1_parametro_p3(mainclass_c1_parametro_p3)
        self.set_mainclass_c1_parametro_p6(mainclass_c1_parametro_p6)
        self.set_mainclass_c1_parametro_p8(mainclass_c1_parametro_p8)

        # initialize the timers
        self.set_mainclass_c1_restoreti_ti1(24000)
        self.set_mainclass_c1_restoreti_ti1_restore(24000)
        self.set_mainclass_c1_restoreti_ti2(32000)
        self.set_mainclass_c1_restoreti_ti2_restore(32000)
        self.set_mainclass_c1_restoreti_ti3(2130000)
        self.set_mainclass_c1_restoreti_ti3_restore(2130000)
        self.set_mainclass_c1_timer_t10(305000)

        self.timers = [self.mainclass_c1_restoreti_ti1,self.mainclass_c1_restoreti_ti1_restore,self.mainclass_c1_restoreti_ti2,self.mainclass_c1_restoreti_ti2_restore,self.mainclass_c1_restoreti_ti3,self.mainclass_c1_restoreti_ti3_restore,self.mainclass_c1_timer_t10,]

        # initialize the counters
        self.set_mainclass_c1_contatore_co3(0)
        self.set_mainclass_c1_contatore_co5(0)
        self.set_mainclass_c1_contatore_co6(0)
        self.set_mainclass_c1_contatore_co7(0)
        self.set_mainclass_c1_contatore_co9(0)

    # setters for record type parameters

    # getters for record type parameters

    # setters for simple type parameters
    def set_mainclass_c1_parametro_p1(self, mainclass_c1_parametro_p1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p1",mainclass_c1_parametro_p1)

    def set_mainclass_c1_parametro_p10(self, mainclass_c1_parametro_p10):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p10",mainclass_c1_parametro_p10)

    def set_mainclass_c1_parametro_p3(self, mainclass_c1_parametro_p3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p3",mainclass_c1_parametro_p3)

    def set_mainclass_c1_parametro_p6(self, mainclass_c1_parametro_p6):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p6",mainclass_c1_parametro_p6)

    def set_mainclass_c1_parametro_p8(self, mainclass_c1_parametro_p8):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p8",mainclass_c1_parametro_p8)


    # getters for simple type parameters
    def get_mainclass_c1_parametro_p1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p1")

    def get_mainclass_c1_parametro_p10(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p10")

    def get_mainclass_c1_parametro_p3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p3")

    def get_mainclass_c1_parametro_p6(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p6")

    def get_mainclass_c1_parametro_p8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p8")


    # setters for comandi al piazzale
    def set_mainclass_c1_comando_c1(self, mainclass_c1_comando_c1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c1",mainclass_c1_comando_c1)

    def set_mainclass_c1_comando_c2(self, mainclass_c1_comando_c2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c2",mainclass_c1_comando_c2)

    def set_mainclass_c1_comando_c6(self, mainclass_c1_comando_c6):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c6",mainclass_c1_comando_c6)

    def set_mainclass_c1_comando_c8(self, mainclass_c1_comando_c8):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c8",mainclass_c1_comando_c8)


    # getters for controlli dal piazzale
    def get_consdef(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"consdef")

    def get_mainclass_c1_controllo_c3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c3")

    def get_mainclass_c1_controllo_c6(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c6")

    def get_mainclass_c1_controllo_c7(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c7")

    def get_mainclass_c1_controllo_c9(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c9")

    def get_mainclass_c1_previousco_c10(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c10")

    def get_mainclass_c1_previousco_c4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c4")

    def get_mainclass_c1_previousco_c5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c5")


    # setters for state variables
    def set_mainclass_c1_previousco_c10_prev(self, mainclass_c1_previousco_c10_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c10_prev",mainclass_c1_previousco_c10_prev)
    def set_mainclass_c1_previousco_c4_prev(self, mainclass_c1_previousco_c4_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c4_prev",mainclass_c1_previousco_c4_prev)
    def set_mainclass_c1_previousco_c5_prev(self, mainclass_c1_previousco_c5_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c5_prev",mainclass_c1_previousco_c5_prev)
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
    def set_mainclass_c1_variabile_v2(self, mainclass_c1_variabile_v2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v2",mainclass_c1_variabile_v2)
    def set_mainclass_c1_variabile_v3(self, mainclass_c1_variabile_v3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v3",mainclass_c1_variabile_v3)
    def set_mainclass_c1_variabile_v4(self, mainclass_c1_variabile_v4):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v4",mainclass_c1_variabile_v4)
    def set_mainclass_c1_variabile_v8(self, mainclass_c1_variabile_v8):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v8",mainclass_c1_variabile_v8)

    # getters for state variables
    def get_mainclass_c1_previousco_c10_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c10_prev")

    def get_mainclass_c1_previousco_c4_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c4_prev")

    def get_mainclass_c1_previousco_c5_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c5_prev")

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

    def get_mainclass_c1_variabile_v2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v2")

    def get_mainclass_c1_variabile_v3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v3")

    def get_mainclass_c1_variabile_v4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v4")

    def get_mainclass_c1_variabile_v8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v8")

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

    def set_mainclass_c1_timer_t10(self, timerDuration):
        self.mainclass_c1_timer_t10 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_timer_t10", self.memory)


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

    def get_mainclass_c1_timer_t10(self):
        return self.mainclass_c1_timer_t10


    # setters for counters
    def set_mainclass_c1_contatore_co3(self, counterInitValue):
        self.mainclass_c1_contatore_co3 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "mainclass_c1_contatore_co3", self.memory)

    def set_mainclass_c1_contatore_co5(self, counterInitValue):
        self.mainclass_c1_contatore_co5 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "mainclass_c1_contatore_co5", self.memory)

    def set_mainclass_c1_contatore_co6(self, counterInitValue):
        self.mainclass_c1_contatore_co6 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "mainclass_c1_contatore_co6", self.memory)

    def set_mainclass_c1_contatore_co7(self, counterInitValue):
        self.mainclass_c1_contatore_co7 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "mainclass_c1_contatore_co7", self.memory)

    def set_mainclass_c1_contatore_co9(self, counterInitValue):
        self.mainclass_c1_contatore_co9 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "mainclass_c1_contatore_co9", self.memory)


    # getters for counters
    def get_mainclass_c1_contatore_co3(self):
        return self.mainclass_c1_contatore_co3

    def get_mainclass_c1_contatore_co5(self):
        return self.mainclass_c1_contatore_co5

    def get_mainclass_c1_contatore_co6(self):
        return self.mainclass_c1_contatore_co6

    def get_mainclass_c1_contatore_co7(self):
        return self.mainclass_c1_contatore_co7

    def get_mainclass_c1_contatore_co9(self):
        return self.mainclass_c1_contatore_co9



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

        self.set_mainclass_c1_previousco_c10_prev(GlobalEnumeration.rossogialloverde)
        self.set_mainclass_c1_previousco_c4_prev(False)
        self.set_mainclass_c1_previousco_c5_prev(False)
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
        
        { commento: {38,}  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  commento: {53,} 12 commento: {38,} o  se il contatore MainClass_C1_contatore_Co9 non è  uguale a  commento: {53,} 120 commento: {38,} o  se il contatore MainClass_C1_contatore_Co6 non è  maggiore di  commento: {54,} 11 commento: {35,} o  se il controllo MainClass_C1_controllo_C3 non è  uguale a  False , commento: {69,}Disattiva il timer MainClass_C1_timer_T10
        
           
         commento: {34,}  se lo stato  è  uguale a  commento: {53,}  state1  commento: {106,}, commento: {71,}Decrementa il contatore MainClass_C1_contatore_Co7
        
         ,altrimenti  commento: {72,}Azzera il contatore MainClass_C1_contatore_Co7
        
        
         commento: {37,}  se la variabile MainClass_C1_variabile_V3 non è  uguale a  False  commento: {37,} e  se la variabile MainClass_C1_variabile_V3 è  uguale a  True  commento: {37,} o  se la variabile MainClass_C1_variabile_V4 non è  diverso da  True  commento: {37,} e  se la variabile MainClass_C1_variabile_V4 è  diverso da  False ,  Applica gli effetti
               della macro MainClass_C1_macroef_M3( con argomento_af9   uguale a GialloVerde ,argomento_af1   uguale a True ,argomento_af6   uguale a Verde ,argomento_af5   uguale a AC ,argomento_af7   uguale a GialloVerde ,argomento_af3   uguale a avanzamentox ) commento: {73,}
        
         ,altrimenti   Applica gli effetti
               della macro MainClass_C1_macroef_M4  commento: {73,}
        
        
        
        }
        """
        def populate_macroMainclass_c1_macroef_m10_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*38,*/  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  /*53,*/ 12 /*38,*/ o  se il contatore MainClass_C1_contatore_Co9 non è  uguale a  /*53,*/ 120 /*38,*/ o  se il contatore MainClass_C1_contatore_Co6 non è  maggiore di  /*54,*/ 11 /*35,*/ o  se il controllo MainClass_C1_controllo_C3 non è  uguale a  False , /*69,*/Disattiva il timer MainClass_C1_timer_T10""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*38,*/  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  /*53,*/ 12 /*38,*/ o  se il contatore MainClass_C1_contatore_Co9 non è  uguale a  /*53,*/ 120 /*38,*/ o  se il contatore MainClass_C1_contatore_Co6 non è  maggiore di  /*54,*/ 11 /*35,*/ o  se il controllo MainClass_C1_controllo_C3 non è  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( negazione di ((mainclass_c1_contatore_co7)  è uguale a  (12)) )  o  
( negazione di ((mainclass_c1_contatore_co9)  è uguale a  (120)) ) )  o  
( negazione di ((mainclass_c1_contatore_co6)  è maggiore di  (11)) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( negazione di ((mainclass_c1_contatore_co7)  è uguale a  (12)) )  o  
( negazione di ((mainclass_c1_contatore_co9)  è uguale a  (120)) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co7)  è uguale a  (12))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co7)  è uguale a  (12)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co9)  è uguale a  (120))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co9)  è uguale a  (120)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co6)  è maggiore di  (11))""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co6)  è maggiore di  (11)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c3)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c3)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITEStatementImpl\n/*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/, /*71,*/Decrementa il contatore MainClass_C1_contatore_Co7

 ,altrimenti  /*72,*/Azzera il contatore MainClass_C1_contatore_Co7""", [
                            DIBoolExpr("""EqualImpl\nlo stato  è  uguale a  /*53,*/  state1""", [
                            ]),#0
                            ]),#1
                            DIStatement("""ITEStatementImpl\n/*37,*/  se la variabile MainClass_C1_variabile_V3 non è  uguale a  False  /*37,*/ e  se la variabile MainClass_C1_variabile_V3 è  uguale a  True  /*37,*/ o  se la variabile MainClass_C1_variabile_V4 non è  diverso da  True  /*37,*/ e  se la variabile MainClass_C1_variabile_V4 è  diverso da  False ,  Applica gli effetti
       della macro MainClass_C1_macroef_M3( con argomento_af9   uguale a GialloVerde ,argomento_af1   uguale a True ,argomento_af6   uguale a Verde ,argomento_af5   uguale a AC ,argomento_af7   uguale a GialloVerde ,argomento_af3   uguale a avanzamentox ) /*73,*/

 ,altrimenti   Applica gli effetti
       della macro MainClass_C1_macroef_M4""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*37,*/  se la variabile MainClass_C1_variabile_V3 non è  uguale a  False  /*37,*/ e  se la variabile MainClass_C1_variabile_V3 è  uguale a  True  /*37,*/ o  se la variabile MainClass_C1_variabile_V4 non è  diverso da  True  /*37,*/ e  se la variabile MainClass_C1_variabile_V4 è  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_variabile_v3)  è uguale a  (False)) )  e  
( (mainclass_c1_variabile_v3)  è uguale a  (True) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v3)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v3)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v3)  è uguale a  (True)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (negazione di ((mainclass_c1_variabile_v4)  è uguale a  (True))) )  e  
( negazione di ((mainclass_c1_variabile_v4)  è uguale a  (False)) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_variabile_v4)  è uguale a  (True)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v4)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v4)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v4)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v4)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M3( con argomento_af9   uguale a GialloVerde ,argomento_af1   uguale a True ,argomento_af6   uguale a Verde ,argomento_af5   uguale a AC ,argomento_af7   uguale a GialloVerde ,argomento_af3   uguale a avanzamentox )"""),#1
                            DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M4"""),#2
                            ]),#2
                ])

        populate_macroMainclass_c1_macroef_m10_SrfMacroDefInfo(di_ctx)
        #  /*38,*/  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  /*53,*/ 12 /*38,*/ o  se il contatore MainClass_C1_contatore_Co9 non è  uguale a  /*53,*/ 120 /*38,*/ o  se il contatore MainClass_C1_contatore_Co6 non è  maggiore di  /*54,*/ 11 /*35,*/ o  se il controllo MainClass_C1_controllo_C3 non è  uguale a  False , /*69,*/Disattiva il timer MainClass_C1_timer_T10
        if db((db((db((db(not db(self.get_mainclass_c1_contatore_co7().get_valore() == 12, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_contatore_co9().get_valore() == 120, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_contatore_co6().get_valore() > 11, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_controllo_c3() == False, di_ctx.subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.get_mainclass_c1_timer_t10().disattiva()
        #  /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/, /*71,*/Decrementa il contatore MainClass_C1_contatore_Co7
        #   ,altrimenti  /*72,*/Azzera il contatore MainClass_C1_contatore_Co7
        if db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[1].subs[0]):
            self.get_mainclass_c1_contatore_co7().decrementa()
        else:
            self.get_mainclass_c1_contatore_co7().resetta()
        #  /*37,*/  se la variabile MainClass_C1_variabile_V3 non è  uguale a  False  /*37,*/ e  se la variabile MainClass_C1_variabile_V3 è  uguale a  True  /*37,*/ o  se la variabile MainClass_C1_variabile_V4 non è  diverso da  True  /*37,*/ e  se la variabile MainClass_C1_variabile_V4 è  diverso da  False ,  Applica gli effetti
        #         della macro MainClass_C1_macroef_M3( con argomento_af9   uguale a GialloVerde ,argomento_af1   uguale a True ,argomento_af6   uguale a Verde ,argomento_af5   uguale a AC ,argomento_af7   uguale a GialloVerde ,argomento_af3   uguale a avanzamentox ) /*73,*/
        #   ,altrimenti   Applica gli effetti
        #         della macro MainClass_C1_macroef_M4
        if db((db((db(not db(self.get_mainclass_c1_variabile_v3() == False, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_variabile_v3() == True, di_ctx.subs[2].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0]) or db((db(not db(not db(self.get_mainclass_c1_variabile_v4() == True, di_ctx.subs[2].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v4() == False, di_ctx.subs[2].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[1].subs[1])), di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.macroMainclass_c1_macroef_m3(True,GlobalEnumeration.avanzamentox,GlobalEnumeration.ac,GlobalEnumeration.verde,GlobalEnumeration.gialloverde,GlobalEnumeration.gialloverde, di_ctx.subs[2].subs[1])
        else:
            self.macroMainclass_c1_macroef_m4(di_ctx.subs[2].subs[2])
    
    def macroMainclass_c1_macroef_m3(self, argomento_af1, argomento_af3, argomento_af5, argomento_af6, argomento_af7, argomento_af9, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {38,}  se il contatore MainClass_C1_contatore_Co7 è  minore di  commento: {55,} 141 e  se l'argomento argomento_af1 è  diverso da  False  commento: {39,} , commento: {66,} Assegna al comando MainClass_C1_comando_C2 il valore  True 
        
         ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V2 il valore 5
        
        
         commento: {34,}  se il parametro MainClass_C1_parametro_P10 è  uguale a  commento: {53,} 2 commento: {34,} o  se il parametro MainClass_C1_parametro_P8 è  uguale a RossoGialloVerde, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V2 il valore 2
        
           
        
        }
        """
        def populate_macroMainclass_c1_macroef_m3_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITEStatementImpl\n/*38,*/  se il contatore MainClass_C1_contatore_Co7 è  minore di  /*55,*/ 141 e  se l'argomento argomento_af1 è  diverso da  False  /*39,*/ , /*66,*/ Assegna al comando MainClass_C1_comando_C2 il valore  True 

 ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V2 il valore 5""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*38,*/  se il contatore MainClass_C1_contatore_Co7 è  minore di  /*55,*/ 141 e  se l'argomento argomento_af1 è  diverso da  False""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co7)  è minore di  (141)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_af1)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_af1)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITStatement\n/*34,*/  se il parametro MainClass_C1_parametro_P10 è  uguale a  /*53,*/ 2 /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  uguale a RossoGialloVerde, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V2 il valore 2""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se il parametro MainClass_C1_parametro_P10 è  uguale a  /*53,*/ 2 /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  uguale a RossoGialloVerde""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p10)  è uguale a  (2)""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p8)  è uguale a  (rossogialloverde)""", [
                            ]),#1
                            ]),#0
                            ]),#1
                ])

        populate_macroMainclass_c1_macroef_m3_SrfMacroDefInfo(di_ctx)
        #  /*38,*/  se il contatore MainClass_C1_contatore_Co7 è  minore di  /*55,*/ 141 e  se l'argomento argomento_af1 è  diverso da  False  /*39,*/ , /*66,*/ Assegna al comando MainClass_C1_comando_C2 il valore  True 
        #   ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V2 il valore 5
        if db((db(self.get_mainclass_c1_contatore_co7().get_valore() < 141, di_ctx.subs[0].subs[0].subs[0]) and db(not db(argomento_af1 == False, di_ctx.subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.set_mainclass_c1_comando_c2(True)
        else:
            self.set_mainclass_c1_variabile_v2(5)
        #  /*34,*/  se il parametro MainClass_C1_parametro_P10 è  uguale a  /*53,*/ 2 /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  uguale a RossoGialloVerde, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V2 il valore 2
        if db((db(self.get_mainclass_c1_parametro_p10() == 2, di_ctx.subs[1].subs[0].subs[0]) or db(self.get_mainclass_c1_parametro_p8() == GlobalEnumeration.rossogialloverde, di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.set_mainclass_c1_variabile_v2(2)
    
    def macroMainclass_c1_macroef_m4(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  minore di  commento: {55,} 5 commento: {35,} e  se il controllo MainClass_C1_controllo_C7 è  diverso da c120x commento: {36,} o  se il timer MainClass_C1_timer_T10 non è disattivo, commento: {68,}Attiva il timer MainClass_C1_timer_T10
        
         ,altrimenti  commento: {69,}Disattiva il timer MainClass_C1_timer_T10
        
        
         commento: {34,}  se il parametro MainClass_C1_parametro_P8 non è  diverso da RossoGialloVerde e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE , commento: {67,} Assegna alla variabile MainClass_C1_variabile_V3 il valore  False 
        
           
        
        }
        """
        def populate_macroMainclass_c1_macroef_m4_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITEStatementImpl\n/*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  minore di  /*55,*/ 5 /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da c120x /*36,*/ o  se il timer MainClass_C1_timer_T10 non è disattivo, /*68,*/Attiva il timer MainClass_C1_timer_T10

 ,altrimenti  /*69,*/Disattiva il timer MainClass_C1_timer_T10""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  minore di  /*55,*/ 5 /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da c120x /*36,*/ o  se il timer MainClass_C1_timer_T10 non è disattivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (mainclass_c1_restoreva_rv1_restore)  è minore di  (5) )  e  
( negazione di ((mainclass_c1_controllo_c7)  è uguale a  (c120x)) )""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_restoreva_rv1_restore)  è minore di  (5)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c7)  è uguale a  (c120x))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (c120x)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t10' è inattivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t10' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITStatement\n/*34,*/  se il parametro MainClass_C1_parametro_P8 non è  diverso da RossoGialloVerde e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE , /*67,*/ Assegna alla variabile MainClass_C1_variabile_V3 il valore  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*34,*/  se il parametro MainClass_C1_parametro_P8 non è  diverso da RossoGialloVerde e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (negazione di ((mainclass_c1_parametro_p8)  è uguale a  (rossogialloverde))) )  e  ( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_parametro_p8)  è uguale a  (rossogialloverde)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p8)  è uguale a  (rossogialloverde))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p8)  è uguale a  (rossogialloverde)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            ]),#1
                ])

        populate_macroMainclass_c1_macroef_m4_SrfMacroDefInfo(di_ctx)
        #  /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  minore di  /*55,*/ 5 /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da c120x /*36,*/ o  se il timer MainClass_C1_timer_T10 non è disattivo, /*68,*/Attiva il timer MainClass_C1_timer_T10
        #   ,altrimenti  /*69,*/Disattiva il timer MainClass_C1_timer_T10
        if db((db((db(self.get_mainclass_c1_restoreva_rv1_restore() < 5, di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.c120x, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_timer_t10().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.get_mainclass_c1_timer_t10().attiva()
        else:
            self.get_mainclass_c1_timer_t10().disattiva()
        #  /*34,*/  se il parametro MainClass_C1_parametro_P8 non è  diverso da RossoGialloVerde e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE , /*67,*/ Assegna alla variabile MainClass_C1_variabile_V3 il valore  False
        if db((db((db(not db(not db(self.get_mainclass_c1_parametro_p8() == GlobalEnumeration.rossogialloverde, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.set_mainclass_c1_variabile_v3(False)
    
    def macroMainclass_c1_macroef_m7(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
         
        {  se il ripristino dello stato  è  uguale a  commento: {53,}  state1  commento: {107,} commento: {34,} o  se il parametro MainClass_C1_parametro_P10 è  diverso da  commento: {56,} 10, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V8 il valore 4
        
         ,altrimenti  commento: {68,}Attiva il timer MainClass_C1_timer_T10
        
        
         commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI2 è disattivo o  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} o  se il contatore MainClass_C1_contatore_Co7 è  diverso da  commento: {56,} 133 commento: {37,} e  se la variabile MainClass_C1_variabile_V3 è  uguale a  True  commento: {37,} o  se la variabile MainClass_C1_variabile_V3 non è  diverso da  True  commento: {38,} o  se il contatore MainClass_C1_contatore_Co6 non è  minore di  commento: {55,} 12, commento: {68,}Attiva il timer MainClass_C1_timer_T10
        
         ,altrimenti  commento: {68,}Attiva il timer MainClass_C1_timer_T10
        
        
         commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI3 non è scaduto commento: {38,} o  se il contatore MainClass_C1_contatore_Co5 è  minore di  commento: {55,} 15 commento: {35,} e  se il controllo MainClass_C1_controllo_C6 non è  diverso da  True  commento: {37,} e  se la variabile MainClass_C1_variabile_V3 è  diverso da  False  commento: {37,} e  se la variabile MainClass_C1_variabile_V2 è  minore di  commento: {55,} 1,  Applica gli effetti
               della macro MainClass_C1_macroef_M3( con argomento_af9   uguale a AC ,argomento_af1   uguale a True ,argomento_af6   uguale a avanzamento ,argomento_af5   uguale a GialloVerde ,argomento_af7   uguale a GialloVerde ,argomento_af3   uguale a avanzamentox ) commento: {73,}
        
           
        
        }
        """
        def populate_macroMainclass_c1_macroef_m7_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITEStatementImpl\nse il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*34,*/ o  se il parametro MainClass_C1_parametro_P10 è  diverso da  /*56,*/ 10, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V8 il valore 4

 ,altrimenti  /*68,*/Attiva il timer MainClass_C1_timer_T10""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*34,*/ o  se il parametro MainClass_C1_parametro_P10 è  diverso da  /*56,*/ 10""", [
                            DIBoolExpr("""EqualImpl\n(stato_restore)  è uguale a  (state1)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p10)  è uguale a  (10))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p10)  è uguale a  (10)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITEStatementImpl\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI2 è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 è  diverso da  /*56,*/ 133 /*37,*/ e  se la variabile MainClass_C1_variabile_V3 è  uguale a  True  /*37,*/ o  se la variabile MainClass_C1_variabile_V3 non è  diverso da  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co6 non è  minore di  /*55,*/ 12, /*68,*/Attiva il timer MainClass_C1_timer_T10

 ,altrimenti  /*68,*/Attiva il timer MainClass_C1_timer_T10""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI2 è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 è  diverso da  /*56,*/ 133 /*37,*/ e  se la variabile MainClass_C1_variabile_V3 è  uguale a  True  /*37,*/ o  se la variabile MainClass_C1_variabile_V3 non è  diverso da  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co6 non è  minore di  /*55,*/ 12""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( ( il timer 'mainclass_c1_restoreti_ti2_restore' è inattivo )  o  
( (consdef)  è uguale a  (False) ) )  o  
( ( negazione di ((mainclass_c1_contatore_co7)  è uguale a  (133)) )  e  
( (mainclass_c1_variabile_v3)  è uguale a  (True) ) ) )  o  
( negazione di (negazione di ((mainclass_c1_variabile_v3)  è uguale a  (True))) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( il timer 'mainclass_c1_restoreti_ti2_restore' è inattivo )  o  
( (consdef)  è uguale a  (False) ) )  o  
( ( negazione di ((mainclass_c1_contatore_co7)  è uguale a  (133)) )  e  
( (mainclass_c1_variabile_v3)  è uguale a  (True) ) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( il timer 'mainclass_c1_restoreti_ti2_restore' è inattivo )  o  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_restoreti_ti2_restore' è inattivo""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_contatore_co7)  è uguale a  (133)) )  e  
( (mainclass_c1_variabile_v3)  è uguale a  (True) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co7)  è uguale a  (133))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co7)  è uguale a  (133)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v3)  è uguale a  (True)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_variabile_v3)  è uguale a  (True)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v3)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v3)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co6)  è minore di  (12))""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co6)  è minore di  (12)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#1
                            DIStatement("""ITStatement\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI3 non è scaduto /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 è  minore di  /*55,*/ 15 /*35,*/ e  se il controllo MainClass_C1_controllo_C6 non è  diverso da  True  /*37,*/ e  se la variabile MainClass_C1_variabile_V3 è  diverso da  False  /*37,*/ e  se la variabile MainClass_C1_variabile_V2 è  minore di  /*55,*/ 1,  Applica gli effetti
       della macro MainClass_C1_macroef_M3( con argomento_af9   uguale a AC ,argomento_af1   uguale a True ,argomento_af6   uguale a avanzamento ,argomento_af5   uguale a GialloVerde ,argomento_af7   uguale a GialloVerde ,argomento_af3   uguale a avanzamentox )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI3 non è scaduto /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 è  minore di  /*55,*/ 15 /*35,*/ e  se il controllo MainClass_C1_controllo_C6 non è  diverso da  True  /*37,*/ e  se la variabile MainClass_C1_variabile_V3 è  diverso da  False  /*37,*/ e  se la variabile MainClass_C1_variabile_V2 è  minore di  /*55,*/ 1""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_restoreti_ti3_restore' è scaduto)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_restoreti_ti3_restore' è scaduto""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( ( (mainclass_c1_contatore_co5)  è minore di  (15) )  e  ( negazione di (negazione di ((mainclass_c1_controllo_c6)  è uguale a  (True))) ) )  e  ( negazione di ((mainclass_c1_variabile_v3)  è uguale a  (False)) ) )  e  
( (mainclass_c1_variabile_v2)  è minore di  (1) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( (mainclass_c1_contatore_co5)  è minore di  (15) )  e  ( negazione di (negazione di ((mainclass_c1_controllo_c6)  è uguale a  (True))) ) )  e  ( negazione di ((mainclass_c1_variabile_v3)  è uguale a  (False)) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (mainclass_c1_contatore_co5)  è minore di  (15) )  e  ( negazione di (negazione di ((mainclass_c1_controllo_c6)  è uguale a  (True))) )""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co5)  è minore di  (15)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_controllo_c6)  è uguale a  (True)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c6)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c6)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v3)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v3)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_variabile_v2)  è minore di  (1)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M3( con argomento_af9   uguale a AC ,argomento_af1   uguale a True ,argomento_af6   uguale a avanzamento ,argomento_af5   uguale a GialloVerde ,argomento_af7   uguale a GialloVerde ,argomento_af3   uguale a avanzamentox )"""),#1
                            ]),#2
                ])

        populate_macroMainclass_c1_macroef_m7_SrfMacroDefInfo(di_ctx)
        #  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*34,*/ o  se il parametro MainClass_C1_parametro_P10 è  diverso da  /*56,*/ 10, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V8 il valore 4
        #   ,altrimenti  /*68,*/Attiva il timer MainClass_C1_timer_T10
        if db((db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_parametro_p10() == 10, di_ctx.subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.set_mainclass_c1_variabile_v8(4)
        else:
            self.get_mainclass_c1_timer_t10().attiva()
        #  /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI2 è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 è  diverso da  /*56,*/ 133 /*37,*/ e  se la variabile MainClass_C1_variabile_V3 è  uguale a  True  /*37,*/ o  se la variabile MainClass_C1_variabile_V3 non è  diverso da  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co6 non è  minore di  /*55,*/ 12, /*68,*/Attiva il timer MainClass_C1_timer_T10
        #   ,altrimenti  /*68,*/Attiva il timer MainClass_C1_timer_T10
        if db((db((db((db((db(self.get_mainclass_c1_restoreti_ti2_restore().isDisattivato(), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_contatore_co7().get_valore() == 133, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_variabile_v3() == True, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_variabile_v3() == True, di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_contatore_co6().get_valore() < 12, di_ctx.subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.get_mainclass_c1_timer_t10().attiva()
        else:
            self.get_mainclass_c1_timer_t10().attiva()
        #  /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI3 non è scaduto /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 è  minore di  /*55,*/ 15 /*35,*/ e  se il controllo MainClass_C1_controllo_C6 non è  diverso da  True  /*37,*/ e  se la variabile MainClass_C1_variabile_V3 è  diverso da  False  /*37,*/ e  se la variabile MainClass_C1_variabile_V2 è  minore di  /*55,*/ 1,  Applica gli effetti
        #         della macro MainClass_C1_macroef_M3( con argomento_af9   uguale a AC ,argomento_af1   uguale a True ,argomento_af6   uguale a avanzamento ,argomento_af5   uguale a GialloVerde ,argomento_af7   uguale a GialloVerde ,argomento_af3   uguale a avanzamentox )
        if db((db(not db(self.get_mainclass_c1_restoreti_ti3_restore().isScaduto(), di_ctx.subs[2].subs[0].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[0]) or db((db((db((db(self.get_mainclass_c1_contatore_co5().get_valore() < 15, di_ctx.subs[2].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_controllo_c6() == True, di_ctx.subs[2].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v3() == False, di_ctx.subs[2].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_variabile_v2() < 1, di_ctx.subs[2].subs[0].subs[1].subs[1])), di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.macroMainclass_c1_macroef_m3(True,GlobalEnumeration.avanzamentox,GlobalEnumeration.gialloverde,GlobalEnumeration.avanzamento,GlobalEnumeration.gialloverde,GlobalEnumeration.ac, di_ctx.subs[2].subs[1])
    
    # verify macros
    @srf_value_macro("macroMainclass_c1_macrove_m9")
    def macroMainclass_c1_macrove_m9(self, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
         
        { commento: {61,}  se il ripristino dello stato  è  uguale a  commento: {53,}  state1  commento: {107,}, Tutte le seguenti { 
         commento: {61,} commento: {34,}  se lo stato  è  diverso da  commento: {56,}  state1  commento: {106,} commento: {34,} o  se il parametro MainClass_C1_parametro_P10 non è  maggiore di  commento: {54,} 10 commento: {36,} o  se il timer MainClass_C1_timer_T10 non è disattivo commento: {37,} o  se la variabile MainClass_C1_variabile_V3 non è  diverso da  False , Tutte le seguenti { 
         commento: {62,} commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV2 è  diverso da  False , Almeno una delle seguenti { 
         commento: {38,}  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  commento: {53,} 13054 commento: {34,} e  se il parametro MainClass_C1_parametro_P10 non è  maggiore di  commento: {54,} 4 commento: {38,} e  se il contatore MainClass_C1_contatore_Co3 non è  diverso da  commento: {56,} 132 commento: {38,} e  se il contatore MainClass_C1_contatore_Co9 è  uguale a  commento: {53,} 1313, Verifica che   commento: {47,48,50,}  commento: {34,}  il parametro MainClass_C1_parametro_P10 non sia  maggiore di  commento: {54,} 3
         commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C7 non sia  diverso da c120x
         commento: {104,} e  che  commento: {35,}  il controllo MainClass_C1_controllo_C9 non sia  diverso da  False 
         commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V8 non sia  diverso da  commento: {56,} 2
        
        
         } Verifica che   commento: {47,48,51,}  commento: {,}  il contatore MainClass_C1_contatore_Co7 non sia  maggiore di  commento: {54,} 13054
         commento: {104,} e  che  commento: {38,}  il contatore MainClass_C1_contatore_Co7 non sia  minore di  commento: {55,} 11
         commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P10 sia  minore di  commento: {55,} 10
         commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C7 non sia  diverso da c120x
         commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
        
        
         } Verifica che   commento: {47,48,50,}  commento: {,}  il controllo MainClass_C1_controllo_C6 sia  diverso da  False 
         commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P10 sia  maggiore di  commento: {54,} 7
         commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V2 non sia  minore di  commento: {55,} 10
         commento: {104,} e  che  commento: {37,}  la variabile MainClass_C1_variabile_V3 non sia  diverso da  True 
         commento: {104,} o  che  commento: {37,}  la variabile MainClass_C1_variabile_V2 sia  diverso da  commento: {56,} 2
         commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P10 non sia  minore di  commento: {55,} 3
        
        
         } Verifica che   commento: {49,51,}  commento: {,}  il contatore MainClass_C1_contatore_Co5 sia  maggiore di  commento: {54,} 113
         commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T10 non sia attivo
        
        
        }
        """
        def populate_macroMainclass_c1_macrove_m9_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/, Tutte le seguenti { 
 /*61,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*34,*/ o  se il parametro MainClass_C1_parametro_P10 non è  maggiore di  /*54,*/ 10 /*36,*/ o  se il timer MainClass_C1_timer_T10 non è disattivo /*37,*/ o  se la variabile MainClass_C1_variabile_V3 non è  diverso da  False , Tutte le seguenti { 
 /*62,*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV2 è  diverso da  False , Almeno una delle seguenti { 
 /*38,*/  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  /*53,*/ 13054 /*34,*/ e  se il parametro MainClass_C1_parametro_P10 non è  maggiore di  /*54,*/ 4 /*38,*/ e  se il contatore MainClass_C1_contatore_Co3 non è  diverso da  /*56,*/ 132 /*38,*/ e  se il contatore MainClass_C1_contatore_Co9 è  uguale a  /*53,*/ 1313, Verifica che   /*47,48,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P10 non sia  maggiore di  /*54,*/ 3
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  diverso da c120x
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C9 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V8 non sia  diverso da  /*56,*/ 2


 } Verifica che   /*47,48,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  maggiore di  /*54,*/ 13054
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co7 non sia  minore di  /*55,*/ 11
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  minore di  /*55,*/ 10
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  diverso da c120x
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,50,*/  /*,*/  il controllo MainClass_C1_controllo_C6 sia  diverso da  False 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  maggiore di  /*54,*/ 7
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V2 non sia  minore di  /*55,*/ 10
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V3 non sia  diverso da  True 
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V2 sia  diverso da  /*56,*/ 2
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P10 non sia  minore di  /*55,*/ 3


 } Verifica che   /*49,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  maggiore di  /*54,*/ 113
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T10 non sia attivo""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/, Tutte le seguenti { 
 /*61,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*34,*/ o  se il parametro MainClass_C1_parametro_P10 non è  maggiore di  /*54,*/ 10 /*36,*/ o  se il timer MainClass_C1_timer_T10 non è disattivo /*37,*/ o  se la variabile MainClass_C1_variabile_V3 non è  diverso da  False , Tutte le seguenti { 
 /*62,*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV2 è  diverso da  False , Almeno una delle seguenti { 
 /*38,*/  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  /*53,*/ 13054 /*34,*/ e  se il parametro MainClass_C1_parametro_P10 non è  maggiore di  /*54,*/ 4 /*38,*/ e  se il contatore MainClass_C1_contatore_Co3 non è  diverso da  /*56,*/ 132 /*38,*/ e  se il contatore MainClass_C1_contatore_Co9 è  uguale a  /*53,*/ 1313, Verifica che   /*47,48,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P10 non sia  maggiore di  /*54,*/ 3
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  diverso da c120x
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C9 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V8 non sia  diverso da  /*56,*/ 2


 } Verifica che   /*47,48,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  maggiore di  /*54,*/ 13054
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co7 non sia  minore di  /*55,*/ 11
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  minore di  /*55,*/ 10
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  diverso da c120x
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,50,*/  /*,*/  il controllo MainClass_C1_controllo_C6 sia  diverso da  False 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  maggiore di  /*54,*/ 7
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V2 non sia  minore di  /*55,*/ 10
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V3 non sia  diverso da  True 
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V2 sia  diverso da  /*56,*/ 2
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P10 non sia  minore di  /*55,*/ 3


 }""", [
                            DIBoolExpr("""EqualImpl\nil ripristino dello stato  è  uguale a  /*53,*/  state1""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*61,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*34,*/ o  se il parametro MainClass_C1_parametro_P10 non è  maggiore di  /*54,*/ 10 /*36,*/ o  se il timer MainClass_C1_timer_T10 non è disattivo /*37,*/ o  se la variabile MainClass_C1_variabile_V3 non è  diverso da  False , Tutte le seguenti { 
 /*62,*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV2 è  diverso da  False , Almeno una delle seguenti { 
 /*38,*/  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  /*53,*/ 13054 /*34,*/ e  se il parametro MainClass_C1_parametro_P10 non è  maggiore di  /*54,*/ 4 /*38,*/ e  se il contatore MainClass_C1_contatore_Co3 non è  diverso da  /*56,*/ 132 /*38,*/ e  se il contatore MainClass_C1_contatore_Co9 è  uguale a  /*53,*/ 1313, Verifica che   /*47,48,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P10 non sia  maggiore di  /*54,*/ 3
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  diverso da c120x
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C9 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V8 non sia  diverso da  /*56,*/ 2


 } Verifica che   /*47,48,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  maggiore di  /*54,*/ 13054
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co7 non sia  minore di  /*55,*/ 11
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  minore di  /*55,*/ 10
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  diverso da c120x
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,50,*/  /*,*/  il controllo MainClass_C1_controllo_C6 sia  diverso da  False 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  maggiore di  /*54,*/ 7
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V2 non sia  minore di  /*55,*/ 10
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V3 non sia  diverso da  True 
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V2 sia  diverso da  /*56,*/ 2
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P10 non sia  minore di  /*55,*/ 3


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*34,*/ o  se il parametro MainClass_C1_parametro_P10 non è  maggiore di  /*54,*/ 10 /*36,*/ o  se il timer MainClass_C1_timer_T10 non è disattivo /*37,*/ o  se la variabile MainClass_C1_variabile_V3 non è  diverso da  False , Tutte le seguenti { 
 /*62,*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV2 è  diverso da  False , Almeno una delle seguenti { 
 /*38,*/  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  /*53,*/ 13054 /*34,*/ e  se il parametro MainClass_C1_parametro_P10 non è  maggiore di  /*54,*/ 4 /*38,*/ e  se il contatore MainClass_C1_contatore_Co3 non è  diverso da  /*56,*/ 132 /*38,*/ e  se il contatore MainClass_C1_contatore_Co9 è  uguale a  /*53,*/ 1313, Verifica che   /*47,48,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P10 non sia  maggiore di  /*54,*/ 3
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  diverso da c120x
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C9 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V8 non sia  diverso da  /*56,*/ 2


 } Verifica che   /*47,48,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  maggiore di  /*54,*/ 13054
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co7 non sia  minore di  /*55,*/ 11
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  minore di  /*55,*/ 10
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  diverso da c120x
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*34,*/ o  se il parametro MainClass_C1_parametro_P10 non è  maggiore di  /*54,*/ 10 /*36,*/ o  se il timer MainClass_C1_timer_T10 non è disattivo /*37,*/ o  se la variabile MainClass_C1_variabile_V3 non è  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*34,*/ o  se il parametro MainClass_C1_parametro_P10 non è  maggiore di  /*54,*/ 10 /*36,*/ o  se il timer MainClass_C1_timer_T10 non è disattivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*34,*/ o  se il parametro MainClass_C1_parametro_P10 non è  maggiore di  /*54,*/ 10""", [
                            DIBoolExpr("""Operatore Logico Not\nlo stato  è  diverso da  /*56,*/  state1""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P10 non è  maggiore di  /*54,*/ 10""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_parametro_p10)  è maggiore di  (10)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T10 non è disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t10' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V3 non è  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v3)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v3)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*62,*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV2 è  diverso da  False , Almeno una delle seguenti { 
 /*38,*/  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  /*53,*/ 13054 /*34,*/ e  se il parametro MainClass_C1_parametro_P10 non è  maggiore di  /*54,*/ 4 /*38,*/ e  se il contatore MainClass_C1_contatore_Co3 non è  diverso da  /*56,*/ 132 /*38,*/ e  se il contatore MainClass_C1_contatore_Co9 è  uguale a  /*53,*/ 1313, Verifica che   /*47,48,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P10 non sia  maggiore di  /*54,*/ 3
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  diverso da c120x
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C9 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V8 non sia  diverso da  /*56,*/ 2


 } Verifica che   /*47,48,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  maggiore di  /*54,*/ 13054
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co7 non sia  minore di  /*55,*/ 11
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  minore di  /*55,*/ 10
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  diverso da c120x
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV2 è  diverso da  False , Almeno una delle seguenti { 
 /*38,*/  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  /*53,*/ 13054 /*34,*/ e  se il parametro MainClass_C1_parametro_P10 non è  maggiore di  /*54,*/ 4 /*38,*/ e  se il contatore MainClass_C1_contatore_Co3 non è  diverso da  /*56,*/ 132 /*38,*/ e  se il contatore MainClass_C1_contatore_Co9 è  uguale a  /*53,*/ 1313, Verifica che   /*47,48,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P10 non sia  maggiore di  /*54,*/ 3
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  diverso da c120x
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C9 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V8 non sia  diverso da  /*56,*/ 2


 }""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino della variabile  MainClass_C1_restoreva_RV2 è  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_restoreva_rv2_restore)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*38,*/  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  /*53,*/ 13054 /*34,*/ e  se il parametro MainClass_C1_parametro_P10 non è  maggiore di  /*54,*/ 4 /*38,*/ e  se il contatore MainClass_C1_contatore_Co3 non è  diverso da  /*56,*/ 132 /*38,*/ e  se il contatore MainClass_C1_contatore_Co9 è  uguale a  /*53,*/ 1313, Verifica che   /*47,48,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P10 non sia  maggiore di  /*54,*/ 3
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  diverso da c120x
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C9 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V8 non sia  diverso da  /*56,*/ 2""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*38,*/  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  /*53,*/ 13054 /*34,*/ e  se il parametro MainClass_C1_parametro_P10 non è  maggiore di  /*54,*/ 4 /*38,*/ e  se il contatore MainClass_C1_contatore_Co3 non è  diverso da  /*56,*/ 132 /*38,*/ e  se il contatore MainClass_C1_contatore_Co9 è  uguale a  /*53,*/ 1313""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*38,*/  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  /*53,*/ 13054 /*34,*/ e  se il parametro MainClass_C1_parametro_P10 non è  maggiore di  /*54,*/ 4 /*38,*/ e  se il contatore MainClass_C1_contatore_Co3 non è  diverso da  /*56,*/ 132""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*38,*/  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  /*53,*/ 13054 /*34,*/ e  se il parametro MainClass_C1_parametro_P10 non è  maggiore di  /*54,*/ 4""", [
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co7 non è  uguale a  /*53,*/ 13054""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co7)  è uguale a  (13054)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P10 non è  maggiore di  /*54,*/ 4""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_parametro_p10)  è maggiore di  (4)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co3 non è  diverso da  /*56,*/ 132""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co3)  è uguale a  (132))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co3)  è uguale a  (132)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil contatore MainClass_C1_contatore_Co9 è  uguale a  /*53,*/ 1313""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P10 non sia  maggiore di  /*54,*/ 3
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  diverso da c120x
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C9 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V8 non sia  diverso da  /*56,*/ 2""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P10 non sia  maggiore di  /*54,*/ 3""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_parametro_p10)  è maggiore di  (3)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  diverso da c120x
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C9 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V8 non sia  diverso da  /*56,*/ 2""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  diverso da c120x
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C9 non sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  diverso da c120x""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c7)  è uguale a  (c120x))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (c120x)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*35,*/  il controllo MainClass_C1_controllo_C9 non sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c9)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c9)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile MainClass_C1_variabile_V8 non sia  diverso da  /*56,*/ 2""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v8)  è uguale a  (2))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v8)  è uguale a  (2)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  maggiore di  /*54,*/ 13054
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co7 non sia  minore di  /*55,*/ 11
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  minore di  /*55,*/ 10
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  diverso da c120x
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  maggiore di  /*54,*/ 13054
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co7 non sia  minore di  /*55,*/ 11
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  minore di  /*55,*/ 10
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  diverso da c120x""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  maggiore di  /*54,*/ 13054
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co7 non sia  minore di  /*55,*/ 11
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  minore di  /*55,*/ 10""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  maggiore di  /*54,*/ 13054
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co7 non sia  minore di  /*55,*/ 11""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  maggiore di  /*54,*/ 13054""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co7)  è maggiore di  (13054)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*38,*/  il contatore MainClass_C1_contatore_Co7 non sia  minore di  /*55,*/ 11""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co7)  è minore di  (11)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nche  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  minore di  /*55,*/ 10""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  diverso da c120x""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c7)  è uguale a  (c120x))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (c120x)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,*/  /*,*/  il controllo MainClass_C1_controllo_C6 sia  diverso da  False 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  maggiore di  /*54,*/ 7
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V2 non sia  minore di  /*55,*/ 10
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V3 non sia  diverso da  True 
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V2 sia  diverso da  /*56,*/ 2
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P10 non sia  minore di  /*55,*/ 3""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,*/  /*,*/  il controllo MainClass_C1_controllo_C6 sia  diverso da  False 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  maggiore di  /*54,*/ 7
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V2 non sia  minore di  /*55,*/ 10
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V3 non sia  diverso da  True 
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V2 sia  diverso da  /*56,*/ 2""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,*/  /*,*/  il controllo MainClass_C1_controllo_C6 sia  diverso da  False 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  maggiore di  /*54,*/ 7
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V2 non sia  minore di  /*55,*/ 10
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V3 non sia  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,50,*/  /*,*/  il controllo MainClass_C1_controllo_C6 sia  diverso da  False 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  maggiore di  /*54,*/ 7""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,50,*/  /*,*/  il controllo MainClass_C1_controllo_C6 sia  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c6)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nche  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  maggiore di  /*54,*/ 7""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  la variabile MainClass_C1_variabile_V2 non sia  minore di  /*55,*/ 10
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V3 non sia  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile MainClass_C1_variabile_V2 non sia  minore di  /*55,*/ 10""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_variabile_v2)  è minore di  (10)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*37,*/  la variabile MainClass_C1_variabile_V3 non sia  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v3)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v3)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*37,*/  la variabile MainClass_C1_variabile_V2 sia  diverso da  /*56,*/ 2""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v2)  è uguale a  (2)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P10 non sia  minore di  /*55,*/ 3""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_parametro_p10)  è minore di  (3)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*49,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  maggiore di  /*54,*/ 113
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T10 non sia attivo""", [
                            DIBoolExpr("""GreaterThanImpl\nche   /*49,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  maggiore di  /*54,*/ 113""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il timer MainClass_C1_timer_T10 non sia attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t10' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroMainclass_c1_macrove_m9_SrfMacroDefInfo(di_ctx)
        return db((db(not db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0]) or db((db(not db((db((db((db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_parametro_p10() > 10, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_timer_t10().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_variabile_v3() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db((db(not db(not db(self.get_mainclass_c1_restoreva_rv2_restore() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db((db((db((db(not db(self.get_mainclass_c1_contatore_co7().get_valore() == 13054, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p10() > 4, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_contatore_co3().get_valore() == 132, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) and db(self.get_mainclass_c1_contatore_co9().get_valore() == 1313, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db(not db(self.get_mainclass_c1_parametro_p10() > 3, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db((db((db(not db(not db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.c120x, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_controllo_c9() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(not db(not db(self.get_mainclass_c1_variabile_v8() == 2, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) and db((db((db((db((db(not db(self.get_mainclass_c1_contatore_co7().get_valore() > 13054, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co7().get_valore() < 11, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_parametro_p10() < 10, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.c120x, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db((db((db((db((db(not db(self.get_mainclass_c1_controllo_c6() == False, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_parametro_p10() > 7, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_variabile_v2() < 10, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_mainclass_c1_variabile_v3() == True, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_variabile_v2() == 2, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) or db(not db(self.get_mainclass_c1_parametro_p10() < 3, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db(self.get_mainclass_c1_contatore_co5().get_valore() > 113, di_ctx.subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_timer_t10().isAttivato(), di_ctx.subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    # value macros
    @srf_value_macro("macroMainclass_c1_macrova_m1")
    def macroMainclass_c1_macrova_m1(self, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
         
        { commento: {[}  se la macro  MainClass_C1_macrova_M7 ( con argomento_a6   uguale a RossoGialloxVerdex ,argomento_a5   uguale a avanzamento ,argomento_a7   uguale a Verde ,argomento_a3   uguale a RossoGialloxVerdex ,argomento_a10   uguale a RossoGialloVerde  e argomento_a2   uguale a RossoGialloxVerdex )  non  è  uguale a  True  commento: {40,}  , assegna alla macro il valore RossoGialloVerde
        
         commento: {46,} assegna alla macro il valore RossoGialloVerde commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m1_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/  se la macro  MainClass_C1_macrova_M7 ( con argomento_a6   uguale a RossoGialloxVerdex ,argomento_a5   uguale a avanzamento ,argomento_a7   uguale a Verde ,argomento_a3   uguale a RossoGialloxVerdex ,argomento_a10   uguale a RossoGialloVerde  e argomento_a2   uguale a RossoGialloxVerdex )  non  è  uguale a  True  /*40,*/  , assegna alla macro il valore RossoGialloVerde""", [
                            DIBoolExpr("""Operatore Logico Not\nla macro  MainClass_C1_macrova_M7 ( con argomento_a6   uguale a RossoGialloxVerdex ,argomento_a5   uguale a avanzamento ,argomento_a7   uguale a Verde ,argomento_a3   uguale a RossoGialloxVerdex ,argomento_a10   uguale a RossoGialloVerde  e argomento_a2   uguale a RossoGialloxVerdex )  non  è  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m7')  è uguale a  (True)""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroMainclass_c1_macrova_m7'"""),#0
                            ]),#0
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macrova_m1_SrfMacroDefInfo(di_ctx)
        #  /*[*/  se la macro  MainClass_C1_macrova_M7 ( con argomento_a6   uguale a RossoGialloxVerdex ,argomento_a5   uguale a avanzamento ,argomento_a7   uguale a Verde ,argomento_a3   uguale a RossoGialloxVerdex ,argomento_a10   uguale a RossoGialloVerde  e argomento_a2   uguale a RossoGialloxVerdex )  non  è  uguale a  True  /*40,*/  , assegna alla macro il valore RossoGialloVerde
        if db(not db(db(self.macroMainclass_c1_macrova_m7(GlobalEnumeration.rossogialloverde,GlobalEnumeration.rossogialloxverdex,GlobalEnumeration.rossogialloxverdex,GlobalEnumeration.avanzamento,GlobalEnumeration.rossogialloxverdex,GlobalEnumeration.verde, di_ctx.subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0]) == True, di_ctx.subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0]):
            return GlobalEnumeration.rossogialloverde
        #  /*46,*/ assegna alla macro il valore RossoGialloVerde
        return GlobalEnumeration.rossogialloverde
    
    @srf_value_macro("macroMainclass_c1_macrova_m10")
    def macroMainclass_c1_macrova_m10(self, argomento_a1, argomento_a4, argomento_a6, argomento_a8, argomento_a9, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}
         commento: {46,} assegna alla macro il valore  True  commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m10_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                ])

        populate_macroMainclass_c1_macrova_m10_SrfMacroDefInfo(di_ctx)
        
        #  /*[*/
        #   /*46,*/ assegna alla macro il valore  True
        return True
    
    @srf_value_macro("macroMainclass_c1_macrova_m5")
    def macroMainclass_c1_macrova_m5(self, argomento_a10, argomento_a2, argomento_a3, argomento_a4, argomento_a5, argomento_a7, argomento_a8, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[} commento: {34,}  se lo stato  non è  uguale a  commento: {53,}  state1  commento: {106,} commento: {36,} e  se il timer MainClass_C1_timer_T10 è attivo e  se la macro  MainClass_C1_macrova_M1   non  è  uguale a RossoGialloVerde commento: {40,}  , assegna alla macro il valore  False 
        
         commento: {46,} assegna alla macro il valore  False  commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m5_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*36,*/ e  se il timer MainClass_C1_timer_T10 è attivo e  se la macro  MainClass_C1_macrova_M1   non  è  uguale a RossoGialloVerde /*40,*/  , assegna alla macro il valore  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*[*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*36,*/ e  se il timer MainClass_C1_timer_T10 è attivo e  se la macro  MainClass_C1_macrova_M1   non  è  uguale a RossoGialloVerde""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((lo stato di 'self')  è uguale a  (state1)) )  e  ( il timer 'mainclass_c1_timer_t10' è attivo )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lo stato di 'self')  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t10' è attivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m1')  è uguale a  (rossogialloverde))""", [
                            DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m1')  è uguale a  (rossogialloverde)""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroMainclass_c1_macrova_m1'"""),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macrova_m5_SrfMacroDefInfo(di_ctx)
        #  /*[*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*36,*/ e  se il timer MainClass_C1_timer_T10 è attivo e  se la macro  MainClass_C1_macrova_M1   non  è  uguale a RossoGialloVerde /*40,*/  , assegna alla macro il valore  False
        if db((db((db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_timer_t10().isAttivato(), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) and db(not db(db(self.macroMainclass_c1_macrova_m1(di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) == GlobalEnumeration.rossogialloverde, di_ctx.subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            return False
        #  /*46,*/ assegna alla macro il valore  False
        return False
    
    @srf_value_macro("macroMainclass_c1_macrova_m6")
    def macroMainclass_c1_macrova_m6(self, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
         
        { commento: {[} commento: {34,}  se il parametro MainClass_C1_parametro_P10 è  minore di  commento: {55,} 6 o  se il controllo ConsDef è uguale a FALSE  commento: {110,} o  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è scaduto o  se il controllo ConsDef è uguale a FALSE  commento: {34,} e  se il parametro MainClass_C1_parametro_P1 è  diverso da  commento: {56,} 6 , assegna alla macro il valore RossoGialloVerde
        
         commento: {46,} assegna alla macro il valore RossoGialloVerde commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m6_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/ /*34,*/  se il parametro MainClass_C1_parametro_P10 è  minore di  /*55,*/ 6 o  se il controllo ConsDef è uguale a FALSE  /*110,*/ o  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è scaduto o  se il controllo ConsDef è uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P1 è  diverso da  /*56,*/ 6 , assegna alla macro il valore RossoGialloVerde""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*[*/ /*34,*/  se il parametro MainClass_C1_parametro_P10 è  minore di  /*55,*/ 6 o  se il controllo ConsDef è uguale a FALSE  /*110,*/ o  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è scaduto o  se il controllo ConsDef è uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P1 è  diverso da  /*56,*/ 6""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( (mainclass_c1_parametro_p10)  è minore di  (6) )  o  
( (consdef)  è uguale a  (False) ) )  o  
( il timer 'mainclass_c1_restoreti_ti1_restore' è scaduto )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( (mainclass_c1_parametro_p10)  è minore di  (6) )  o  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_parametro_p10)  è minore di  (6)""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_restoreti_ti1_restore' è scaduto""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  
( negazione di ((mainclass_c1_parametro_p1)  è uguale a  (6)) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p1)  è uguale a  (6))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p1)  è uguale a  (6)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macrova_m6_SrfMacroDefInfo(di_ctx)
        #  /*[*/ /*34,*/  se il parametro MainClass_C1_parametro_P10 è  minore di  /*55,*/ 6 o  se il controllo ConsDef è uguale a FALSE  /*110,*/ o  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è scaduto o  se il controllo ConsDef è uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P1 è  diverso da  /*56,*/ 6 , assegna alla macro il valore RossoGialloVerde
        if db((db((db((db(self.get_mainclass_c1_parametro_p10() < 6, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_restoreti_ti1_restore().isScaduto(), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p1() == 6, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            return GlobalEnumeration.rossogialloverde
        #  /*46,*/ assegna alla macro il valore RossoGialloVerde
        return GlobalEnumeration.rossogialloverde
    
    @srf_value_macro("macroMainclass_c1_macrova_m7")
    def macroMainclass_c1_macrova_m7(self, argomento_a10, argomento_a2, argomento_a3, argomento_a5, argomento_a6, argomento_a7, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}  commento: {35,}   se il controllo MainClass_C1_controllo_C9 non è  diverso da  False  commento: {110,} e  se il ripristino del timer  MainClass_C1_restoreTI_TI2 è disattivo , assegna alla macro il valore  True 
        
         commento: {46,} assegna alla macro il valore  False  commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m7_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/  /*35,*/   se il controllo MainClass_C1_controllo_C9 non è  diverso da  False  /*110,*/ e  se il ripristino del timer  MainClass_C1_restoreTI_TI2 è disattivo , assegna alla macro il valore  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*[*/  /*35,*/   se il controllo MainClass_C1_controllo_C9 non è  diverso da  False  /*110,*/ e  se il ripristino del timer  MainClass_C1_restoreTI_TI2 è disattivo""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_controllo_c9)  è uguale a  (False)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c9)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c9)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_restoreti_ti2_restore' è inattivo""", [
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macrova_m7_SrfMacroDefInfo(di_ctx)
        #  /*[*/  /*35,*/   se il controllo MainClass_C1_controllo_C9 non è  diverso da  False  /*110,*/ e  se il ripristino del timer  MainClass_C1_restoreTI_TI2 è disattivo , assegna alla macro il valore  True
        if db((db(not db(not db(self.get_mainclass_c1_controllo_c9() == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_restoreti_ti2_restore().isDisattivato(), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            return True
        #  /*46,*/ assegna alla macro il valore  False
        return False
    
    # for each manual command, the corresponding method is created
    def eventMainclass_c1_command_comm2DaSender127c0aca(self, notifying_process):
        notifying_process.response_notify_man_cmd(self, 'eventMainclass_c1_command_comm2DaSender127c0aca')
    
    def eventMainclass_c1_command_comm5DaSender83c691f2(self, notifying_process):
        notifying_process.response_notify_man_cmd(self, 'eventMainclass_c1_command_comm5DaSender83c691f2')
    
    def eventMainclass_c1_command_comm6(self, notifying_process):
        notifying_process.response_notify_man_cmd(self, 'eventMainclass_c1_command_comm6')
    
    # for each automatic command, the corresponding method is created
    def eventMainclass_c1_command_comm7(self, notifying_process, argomento_ave10, argomento_ave2, argomento_ave4, argomento_ave8):
        notifying_process.response_notify_auto_cmd(self, 'eventMainclass_c1_command_comm7', argomento_ave10=argomento_ave10, argomento_ave2=argomento_ave2, argomento_ave4=argomento_ave4, argomento_ave8=argomento_ave8)
    

    def update_precedente(self):
        # update the variables with previous value
        self.set_mainclass_c1_previousco_c10_prev(self.get_mainclass_c1_previousco_c10())
        self.set_mainclass_c1_previousco_c4_prev(self.get_mainclass_c1_previousco_c4())
        self.set_mainclass_c1_previousco_c5_prev(self.get_mainclass_c1_previousco_c5())
        self.set_mainclass_c1_previousva_pv1_prev(self.get_mainclass_c1_previousva_pv1())
        self.set_mainclass_c1_previousva_pv2_prev(self.get_mainclass_c1_previousva_pv2())
        self.set_mainclass_c1_previousva_pv3_prev(self.get_mainclass_c1_previousva_pv3())
        self.set_mainclass_c1_previousva_pv4_prev(self.get_mainclass_c1_previousva_pv4())

