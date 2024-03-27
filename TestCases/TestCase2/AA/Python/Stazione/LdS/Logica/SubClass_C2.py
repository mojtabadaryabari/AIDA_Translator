# Codice del modello 'TestCase2', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
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

        self.set_subclass_c2_previousva_pv1(GlobalEnumeration.giallox)
        self.set_subclass_c2_previousva_pv2(GlobalEnumeration.gialloverde)
        self.set_subclass_c2_previousva_pv3(False)
        self.set_subclass_c2_previousva_pv4(GlobalEnumeration.giallox)
        self.set_subclass_c2_previousva_pv5(0)
        self.set_subclass_c2_restoreva_rv1(False)
        self.set_subclass_c2_restoreva_rv2(GlobalEnumeration.rossogiallogiallo)
        self.set_subclass_c2_restoreva_rv3(False)
        self.set_subclass_c2_variabile_v2(0)
        self.set_subclass_c2_variabile_v5(GlobalEnumeration.gialloverde)
        self.set_subclass_c2_variabile_v7(0)
        self.set_subclass_c2_variabile_v8(GlobalEnumeration.giallox)

        self._expected_commands_map = {
            Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1 : set([]),
        }

    def set_expected_cmds_response(self):
        # for each manual command of SubClass_C2
        if self.is_triggered('eventSubclass_c2_command_comm1DaSendercda7890b'):
            self.set_man_cmd_response('eventSubclass_c2_command_comm1DaSendercda7890b',self.ManCmdResponse.UNEXPECTED)
        else:
            self.set_man_cmd_response('eventSubclass_c2_command_comm1DaSendercda7890b',self.ManCmdResponse.NOOP)
        if self.is_triggered('eventSubclass_c2_command_comm2'):
            self.set_man_cmd_response('eventSubclass_c2_command_comm2',self.ManCmdResponse.UNEXPECTED)
        else:
            self.set_man_cmd_response('eventSubclass_c2_command_comm2',self.ManCmdResponse.NOOP)
        if self.is_triggered('eventSubclass_c2_command_comm5DaSender94b948c6'):
            self.set_man_cmd_response('eventSubclass_c2_command_comm5DaSender94b948c6',self.ManCmdResponse.UNEXPECTED)
        else:
            self.set_man_cmd_response('eventSubclass_c2_command_comm5DaSender94b948c6',self.ManCmdResponse.NOOP)
        if self.is_triggered('eventSubclass_c2_command_comm9'):
            self.set_man_cmd_response('eventSubclass_c2_command_comm9',self.ManCmdResponse.UNEXPECTED)
        else:
            self.set_man_cmd_response('eventSubclass_c2_command_comm9',self.ManCmdResponse.NOOP)



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
    def init_configuration(self, subclass_c2_lista_l10, subclass_c2_lista_l7, subclass_c2_lista_l8, subclass_c2_lista_l9, subclass_c2_parametro_p1, subclass_c2_parametro_p10, subclass_c2_parametro_p2, subclass_c2_parametro_p4, subclass_c2_parametro_p6):
        # initialize the record type parameters
        self.set_subclass_c2_lista_l10(subclass_c2_lista_l10)
        self.set_subclass_c2_lista_l7(subclass_c2_lista_l7)
        self.set_subclass_c2_lista_l8(subclass_c2_lista_l8)
        self.set_subclass_c2_lista_l9(subclass_c2_lista_l9)
        # initialize the simple type parameters
        self.set_subclass_c2_parametro_p1(subclass_c2_parametro_p1)
        self.set_subclass_c2_parametro_p10(subclass_c2_parametro_p10)
        self.set_subclass_c2_parametro_p2(subclass_c2_parametro_p2)
        self.set_subclass_c2_parametro_p4(subclass_c2_parametro_p4)
        self.set_subclass_c2_parametro_p6(subclass_c2_parametro_p6)

        # initialize the timers
        self.set_subclass_c2_restoreti_ti1(132000)
        self.set_subclass_c2_restoreti_ti1_restore(132000)
        self.set_subclass_c2_restoreti_ti2(3000)
        self.set_subclass_c2_restoreti_ti2_restore(3000)
        self.set_subclass_c2_timer_t10(315000)
        self.set_subclass_c2_timer_t3(204000)

        self.timers = [self.subclass_c2_restoreti_ti1,self.subclass_c2_restoreti_ti1_restore,self.subclass_c2_restoreti_ti2,self.subclass_c2_restoreti_ti2_restore,self.subclass_c2_timer_t10,self.subclass_c2_timer_t3,]

        # initialize the counters
        self.set_subclass_c2_contatore_co3(0)
        self.set_subclass_c2_contatore_co4(0)

    # setters for record type parameters
    def set_subclass_c2_lista_l10(self, subclass_c2_lista_l10):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l10",subclass_c2_lista_l10)

    def set_subclass_c2_lista_l7(self, subclass_c2_lista_l7):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l7",subclass_c2_lista_l7)

    def set_subclass_c2_lista_l8(self, subclass_c2_lista_l8):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l8",subclass_c2_lista_l8)

    def set_subclass_c2_lista_l9(self, subclass_c2_lista_l9):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l9",subclass_c2_lista_l9)


    # getters for record type parameters
    def get_subclass_c2_lista_l10(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l10")

    def get_subclass_c2_lista_l7(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l7")

    def get_subclass_c2_lista_l8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l8")

    def get_subclass_c2_lista_l9(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l9")


    # setters for simple type parameters
    def set_subclass_c2_parametro_p1(self, subclass_c2_parametro_p1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p1",subclass_c2_parametro_p1)

    def set_subclass_c2_parametro_p10(self, subclass_c2_parametro_p10):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p10",subclass_c2_parametro_p10)

    def set_subclass_c2_parametro_p2(self, subclass_c2_parametro_p2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p2",subclass_c2_parametro_p2)

    def set_subclass_c2_parametro_p4(self, subclass_c2_parametro_p4):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p4",subclass_c2_parametro_p4)

    def set_subclass_c2_parametro_p6(self, subclass_c2_parametro_p6):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p6",subclass_c2_parametro_p6)


    # getters for simple type parameters
    def get_subclass_c2_parametro_p1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p1")

    def get_subclass_c2_parametro_p10(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p10")

    def get_subclass_c2_parametro_p2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p2")

    def get_subclass_c2_parametro_p4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p4")

    def get_subclass_c2_parametro_p6(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p6")


    # setters for comandi al piazzale
    def set_subclass_c2_comando_c10(self, subclass_c2_comando_c10):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_comando_c10",subclass_c2_comando_c10)

    def set_subclass_c2_comando_c2(self, subclass_c2_comando_c2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_comando_c2",subclass_c2_comando_c2)

    def set_subclass_c2_comando_c3(self, subclass_c2_comando_c3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_comando_c3",subclass_c2_comando_c3)

    def set_subclass_c2_comando_c4(self, subclass_c2_comando_c4):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_comando_c4",subclass_c2_comando_c4)

    def set_subclass_c2_comando_c6(self, subclass_c2_comando_c6):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_comando_c6",subclass_c2_comando_c6)


    # getters for controlli dal piazzale
    def get_consdef(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"consdef")

    def get_subclass_c2_controllo_c10(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_controllo_c10")

    def get_subclass_c2_controllo_c3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_controllo_c3")

    def get_subclass_c2_previousco_c1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c1")

    def get_subclass_c2_previousco_c5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c5")

    def get_subclass_c2_previousco_c7(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c7")

    def get_subclass_c2_previousco_c8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c8")

    def get_subclass_c2_previousco_c9(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c9")


    # setters for state variables
    def set_subclass_c2_previousco_c1_prev(self, subclass_c2_previousco_c1_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c1_prev",subclass_c2_previousco_c1_prev)
    def set_subclass_c2_previousco_c5_prev(self, subclass_c2_previousco_c5_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c5_prev",subclass_c2_previousco_c5_prev)
    def set_subclass_c2_previousco_c7_prev(self, subclass_c2_previousco_c7_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c7_prev",subclass_c2_previousco_c7_prev)
    def set_subclass_c2_previousco_c8_prev(self, subclass_c2_previousco_c8_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c8_prev",subclass_c2_previousco_c8_prev)
    def set_subclass_c2_previousco_c9_prev(self, subclass_c2_previousco_c9_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c9_prev",subclass_c2_previousco_c9_prev)
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
    def set_subclass_c2_variabile_v2(self, subclass_c2_variabile_v2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v2",subclass_c2_variabile_v2)
    def set_subclass_c2_variabile_v5(self, subclass_c2_variabile_v5):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v5",subclass_c2_variabile_v5)
    def set_subclass_c2_variabile_v7(self, subclass_c2_variabile_v7):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v7",subclass_c2_variabile_v7)
    def set_subclass_c2_variabile_v8(self, subclass_c2_variabile_v8):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v8",subclass_c2_variabile_v8)

    # getters for state variables
    def get_stato_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"stato_restore")

    def get_subclass_c2_previousco_c1_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c1_prev")

    def get_subclass_c2_previousco_c5_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c5_prev")

    def get_subclass_c2_previousco_c7_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c7_prev")

    def get_subclass_c2_previousco_c8_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c8_prev")

    def get_subclass_c2_previousco_c9_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c9_prev")

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

    def get_subclass_c2_variabile_v2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v2")

    def get_subclass_c2_variabile_v5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v5")

    def get_subclass_c2_variabile_v7(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v7")

    def get_subclass_c2_variabile_v8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v8")


    # setters for timers
    def set_subclass_c2_restoreti_ti1(self, timerDuration):
        self.subclass_c2_restoreti_ti1 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_restoreti_ti1", self.memory)

    def set_subclass_c2_restoreti_ti1_restore(self, timerDuration):
        self.subclass_c2_restoreti_ti1_restore = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_restoreti_ti1_restore", self.memory)

    def set_subclass_c2_restoreti_ti2(self, timerDuration):
        self.subclass_c2_restoreti_ti2 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_restoreti_ti2", self.memory)

    def set_subclass_c2_restoreti_ti2_restore(self, timerDuration):
        self.subclass_c2_restoreti_ti2_restore = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_restoreti_ti2_restore", self.memory)

    def set_subclass_c2_timer_t10(self, timerDuration):
        self.subclass_c2_timer_t10 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_timer_t10", self.memory)

    def set_subclass_c2_timer_t3(self, timerDuration):
        self.subclass_c2_timer_t3 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_timer_t3", self.memory)


    # getters for timers
    def get_subclass_c2_restoreti_ti1(self):
        return self.subclass_c2_restoreti_ti1

    def get_subclass_c2_restoreti_ti1_restore(self):
        return self.subclass_c2_restoreti_ti1_restore

    def get_subclass_c2_restoreti_ti2(self):
        return self.subclass_c2_restoreti_ti2

    def get_subclass_c2_restoreti_ti2_restore(self):
        return self.subclass_c2_restoreti_ti2_restore

    def get_subclass_c2_timer_t10(self):
        return self.subclass_c2_timer_t10

    def get_subclass_c2_timer_t3(self):
        return self.subclass_c2_timer_t3


    # setters for counters
    def set_subclass_c2_contatore_co3(self, counterInitValue):
        self.subclass_c2_contatore_co3 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "subclass_c2_contatore_co3", self.memory)

    def set_subclass_c2_contatore_co4(self, counterInitValue):
        self.subclass_c2_contatore_co4 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "subclass_c2_contatore_co4", self.memory)


    # getters for counters
    def get_subclass_c2_contatore_co3(self):
        return self.subclass_c2_contatore_co3

    def get_subclass_c2_contatore_co4(self):
        return self.subclass_c2_contatore_co4



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
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.StatoIniziale, Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1,
                         guard=(self.dbs[0], ),
                         effect=(),
                         phase = TransPhase.Stato
                         ),
            # transizioni della fase manuale
            # transizioni della fase di stato
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1,Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1,
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
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1)
            self.effect_INITIALIZATION_StatoIniziale_state1_000()
            self.response_wait()

        self.set_subclass_c2_previousco_c1_prev(False)
        self.set_subclass_c2_previousco_c5_prev(True)
        self.set_subclass_c2_previousco_c7_prev(True)
        self.set_subclass_c2_previousco_c8_prev(GlobalEnumeration.rossogiallo)
        self.set_subclass_c2_previousco_c9_prev(True)
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
        Nessuna
        }
        """
        pass
    
    # effect macros
    def macroSubclass_c2_macroef_m10(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {38,}  se il contatore SubClass_C2_contatore_Co4 è  diverso da  commento: {56,} 114,  commento: {43,}  se MainClass_C1_timer_T4 del campo  MainClass_C1 di SubClass_C2_lista_L9 è attivo, commento: {88,} quando  commento: {43,}   MainClass_C1_timer_T4 del campo  MainClass_C1     commento: {105,} è attivo commento: {35,} o  se il controllo SubClass_C2_controllo_C3 non è  diverso da Verde commento: {38,} e  se il contatore SubClass_C2_contatore_Co3 è  minore di  commento: {55,} 1432 commento: {37,} e  se la variabile SubClass_C2_variabile_V8 è  diverso da avvio, commento: {66,} Assegna al comando SubClass_C2_comando_C2 il valore  True 
        
         ,altrimenti  commento: {66,} Assegna al comando SubClass_C2_comando_C6 il valore  False 
        
        
         commento: {35,}  se il controllo SubClass_C2_controllo_C10 non è  diverso da RossoGiallo,  commento: {44,}  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  commento: {105,} è  diverso da  True , commento: {88,} quando  commento: {45,}    MainClass_C1_contatore_Co1 del campo  MainClass_C1     commento: {105,} è  maggiore di  commento: {54,} 1115 commento: {34,} e  se il parametro SubClass_C2_parametro_P4 non è  uguale a RossoGialloxVerdex, commento: {66,} Assegna al comando SubClass_C2_comando_C2 il valore  False 
        
           
         commento: {34,}  se il parametro SubClass_C2_parametro_P4 è  uguale a RossoGialloxVerdex commento: {37,} o  se la variabile SubClass_C2_variabile_V2 è  maggiore di  commento: {54,} 7 commento: {38,} e  se il contatore SubClass_C2_contatore_Co4 non è  uguale a  commento: {53,} 1304 commento: {37,} e  se la variabile SubClass_C2_variabile_V8 non è  diverso da avvio, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V7 il valore 4
        
           
         commento: {110,}  se il ripristino del timer  SubClass_C2_restoreTI_TI1 non è disattivo commento: {36,} e  se il timer SubClass_C2_timer_T3 non è scaduto commento: {38,} o  se il contatore SubClass_C2_contatore_Co4 è  diverso da  commento: {56,} 1432, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V8 il valore avvio
        
         ,altrimenti   Applica gli effetti
               della macro SubClass_C2_macroef_M2  commento: {73,}
        
        
        
        }
        """
        def populate_macroSubclass_c2_macroef_m10_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITEStatementImpl\n/*38,*/  se il contatore SubClass_C2_contatore_Co4 è  diverso da  /*56,*/ 114,  /*43,*/  se MainClass_C1_timer_T4 del campo  MainClass_C1 di SubClass_C2_lista_L9 è attivo, /*88,*/ quando  /*43,*/   MainClass_C1_timer_T4 del campo  MainClass_C1     /*105,*/ è attivo /*35,*/ o  se il controllo SubClass_C2_controllo_C3 non è  diverso da Verde /*38,*/ e  se il contatore SubClass_C2_contatore_Co3 è  minore di  /*55,*/ 1432 /*37,*/ e  se la variabile SubClass_C2_variabile_V8 è  diverso da avvio, /*66,*/ Assegna al comando SubClass_C2_comando_C2 il valore  True 

 ,altrimenti  /*66,*/ Assegna al comando SubClass_C2_comando_C6 il valore  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*38,*/  se il contatore SubClass_C2_contatore_Co4 è  diverso da  /*56,*/ 114,  /*43,*/  se MainClass_C1_timer_T4 del campo  MainClass_C1 di SubClass_C2_lista_L9 è attivo, /*88,*/ quando  /*43,*/   MainClass_C1_timer_T4 del campo  MainClass_C1     /*105,*/ è attivo /*35,*/ o  se il controllo SubClass_C2_controllo_C3 non è  diverso da Verde /*38,*/ e  se il contatore SubClass_C2_contatore_Co3 è  minore di  /*55,*/ 1432 /*37,*/ e  se la variabile SubClass_C2_variabile_V8 è  diverso da avvio""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c2_contatore_co4)  è uguale a  (114)) )  e  
( per ognuna delle seguenti {se (il timer 'mainclass_c1_timer_t4 del campo mainclass_c1 della lista subclass_c2_lista_l9' è attivo) allora (il timer 'mainclass_c1_timer_t4 del campo mainclass_c1 della lista subclass_c2_lista_l9' è attivo)} )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co4)  è uguale a  (114))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co4)  è uguale a  (114)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {se (il timer 'mainclass_c1_timer_t4 del campo mainclass_c1 della lista subclass_c2_lista_l9' è attivo) allora (il timer 'mainclass_c1_timer_t4 del campo mainclass_c1 della lista subclass_c2_lista_l9' è attivo)}""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\nse (il timer 'mainclass_c1_timer_t4 del campo mainclass_c1 della lista subclass_c2_lista_l9' è attivo) allora (il timer 'mainclass_c1_timer_t4 del campo mainclass_c1 della lista subclass_c2_lista_l9' è attivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t4 del campo mainclass_c1 della lista subclass_c2_lista_l9' è attivo""", [
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t4 del campo mainclass_c1 della lista subclass_c2_lista_l9' è attivo""", [
                            ]),#1
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di (negazione di ((subclass_c2_controllo_c3)  è uguale a  (verde))) )  e  ( (subclass_c2_contatore_co3)  è minore di  (1432) ) )  e  
( negazione di ((subclass_c2_variabile_v8)  è uguale a  (avvio)) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (negazione di ((subclass_c2_controllo_c3)  è uguale a  (verde))) )  e  ( (subclass_c2_contatore_co3)  è minore di  (1432) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_controllo_c3)  è uguale a  (verde)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c3)  è uguale a  (verde))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c3)  è uguale a  (verde)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_contatore_co3)  è minore di  (1432)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v8)  è uguale a  (avvio))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v8)  è uguale a  (avvio)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITStatement\n/*35,*/  se il controllo SubClass_C2_controllo_C10 non è  diverso da RossoGiallo,  /*44,*/  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è  diverso da  True , /*88,*/ quando  /*45,*/    MainClass_C1_contatore_Co1 del campo  MainClass_C1     /*105,*/ è  maggiore di  /*54,*/ 1115 /*34,*/ e  se il parametro SubClass_C2_parametro_P4 non è  uguale a RossoGialloxVerdex, /*66,*/ Assegna al comando SubClass_C2_comando_C2 il valore  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*35,*/  se il controllo SubClass_C2_controllo_C10 non è  diverso da RossoGiallo,  /*44,*/  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è  diverso da  True , /*88,*/ quando  /*45,*/    MainClass_C1_contatore_Co1 del campo  MainClass_C1     /*105,*/ è  maggiore di  /*54,*/ 1115 /*34,*/ e  se il parametro SubClass_C2_parametro_P4 non è  uguale a RossoGialloxVerdex""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (negazione di ((subclass_c2_controllo_c10)  è uguale a  (rossogiallo))) )  e  ( per ognuna delle seguenti con lista non vuota {se ((mainclass_c1_contatore_co1 del campo mainclass_c1 della lista subclass_c2_lista_l8)  è maggiore di  (1115)) allora (negazione di ((mainclass_c1_variabile_v6 del campo mainclass_c1 della lista subclass_c2_lista_l8)  è uguale a  (True)))} )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_controllo_c10)  è uguale a  (rossogiallo)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c10)  è uguale a  (rossogiallo))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c10)  è uguale a  (rossogiallo)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {se ((mainclass_c1_contatore_co1 del campo mainclass_c1 della lista subclass_c2_lista_l8)  è maggiore di  (1115)) allora (negazione di ((mainclass_c1_variabile_v6 del campo mainclass_c1 della lista subclass_c2_lista_l8)  è uguale a  (True)))}""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\nse ((mainclass_c1_contatore_co1 del campo mainclass_c1 della lista subclass_c2_lista_l8)  è maggiore di  (1115)) allora (negazione di ((mainclass_c1_variabile_v6 del campo mainclass_c1 della lista subclass_c2_lista_l8)  è uguale a  (True)))""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co1 del campo mainclass_c1 della lista subclass_c2_lista_l8)  è maggiore di  (1115)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v6 del campo mainclass_c1 della lista subclass_c2_lista_l8)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v6 del campo mainclass_c1 della lista subclass_c2_lista_l8)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p4)  è uguale a  (rossogialloxverdex))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p4)  è uguale a  (rossogialloxverdex)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#1
                            DIStatement("""ITStatement\n/*34,*/  se il parametro SubClass_C2_parametro_P4 è  uguale a RossoGialloxVerdex /*37,*/ o  se la variabile SubClass_C2_variabile_V2 è  maggiore di  /*54,*/ 7 /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 non è  uguale a  /*53,*/ 1304 /*37,*/ e  se la variabile SubClass_C2_variabile_V8 non è  diverso da avvio, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V7 il valore 4""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se il parametro SubClass_C2_parametro_P4 è  uguale a RossoGialloxVerdex /*37,*/ o  se la variabile SubClass_C2_variabile_V2 è  maggiore di  /*54,*/ 7 /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 non è  uguale a  /*53,*/ 1304 /*37,*/ e  se la variabile SubClass_C2_variabile_V8 non è  diverso da avvio""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p4)  è uguale a  (rossogialloxverdex)""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( (subclass_c2_variabile_v2)  è maggiore di  (7) )  e  ( negazione di ((subclass_c2_contatore_co4)  è uguale a  (1304)) ) )  e  
( negazione di (negazione di ((subclass_c2_variabile_v8)  è uguale a  (avvio))) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (subclass_c2_variabile_v2)  è maggiore di  (7) )  e  ( negazione di ((subclass_c2_contatore_co4)  è uguale a  (1304)) )""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_variabile_v2)  è maggiore di  (7)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co4)  è uguale a  (1304))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co4)  è uguale a  (1304)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_variabile_v8)  è uguale a  (avvio)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v8)  è uguale a  (avvio))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v8)  è uguale a  (avvio)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#2
                            DIStatement("""ITEStatementImpl\n/*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI1 non è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T3 non è scaduto /*38,*/ o  se il contatore SubClass_C2_contatore_Co4 è  diverso da  /*56,*/ 1432, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V8 il valore avvio

 ,altrimenti   Applica gli effetti
       della macro SubClass_C2_macroef_M2""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI1 non è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T3 non è scaduto /*38,*/ o  se il contatore SubClass_C2_contatore_Co4 è  diverso da  /*56,*/ 1432""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (il timer 'subclass_c2_restoreti_ti1_restore' è inattivo) )  e  
( negazione di (il timer 'subclass_c2_timer_t3' è scaduto) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c2_restoreti_ti1_restore' è inattivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_restoreti_ti1_restore' è inattivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c2_timer_t3' è scaduto)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t3' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co4)  è uguale a  (1432))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co4)  è uguale a  (1432)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro SubClass_C2_macroef_M2"""),#1
                            ]),#3
                ])

        populate_macroSubclass_c2_macroef_m10_SrfMacroDefInfo(di_ctx)
        #  /*38,*/  se il contatore SubClass_C2_contatore_Co4 è  diverso da  /*56,*/ 114,  /*43,*/  se MainClass_C1_timer_T4 del campo  MainClass_C1 di SubClass_C2_lista_L9 è attivo, /*88,*/ quando  /*43,*/   MainClass_C1_timer_T4 del campo  MainClass_C1     /*105,*/ è attivo /*35,*/ o  se il controllo SubClass_C2_controllo_C3 non è  diverso da Verde /*38,*/ e  se il contatore SubClass_C2_contatore_Co3 è  minore di  /*55,*/ 1432 /*37,*/ e  se la variabile SubClass_C2_variabile_V8 è  diverso da avvio, /*66,*/ Assegna al comando SubClass_C2_comando_C2 il valore  True 
        #   ,altrimenti  /*66,*/ Assegna al comando SubClass_C2_comando_C6 il valore  False
        if db((db((db(not db(self.get_subclass_c2_contatore_co4().get_valore() == 114, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(all(db(it.get_mainclass_c1().get_mainclass_c1_timer_t4().isAttivato(), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[1][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l9()) if db(it.get_mainclass_c1().get_mainclass_c1_timer_t4().isAttivato(), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0][idx])), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db((db(not db(not db(self.get_subclass_c2_controllo_c3() == GlobalEnumeration.verde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) and db(self.get_subclass_c2_contatore_co3().get_valore() < 1432, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_variabile_v8() == GlobalEnumeration.avvio, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.set_subclass_c2_comando_c2(True)
        else:
            self.set_subclass_c2_comando_c6(False)
        #  /*35,*/  se il controllo SubClass_C2_controllo_C10 non è  diverso da RossoGiallo,  /*44,*/  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è  diverso da  True , /*88,*/ quando  /*45,*/    MainClass_C1_contatore_Co1 del campo  MainClass_C1     /*105,*/ è  maggiore di  /*54,*/ 1115 /*34,*/ e  se il parametro SubClass_C2_parametro_P4 non è  uguale a RossoGialloxVerdex, /*66,*/ Assegna al comando SubClass_C2_comando_C2 il valore  False
        if db((db((db(not db(not db(self.get_subclass_c2_controllo_c10() == GlobalEnumeration.rossogiallo, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0]) and db(all_notempty(db(not db(it.get_mainclass_c1().get_mainclass_c1_variabile_v6() == True, di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0][idx]), di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0].subs[1][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l8()) if db(it.get_mainclass_c1().get_mainclass_c1_contatore_co1().get_valore() > 1115, di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0].subs[0][idx])), di_ctx.subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c2_parametro_p4() == GlobalEnumeration.rossogialloxverdex, di_ctx.subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.set_subclass_c2_comando_c2(False)
        #  /*34,*/  se il parametro SubClass_C2_parametro_P4 è  uguale a RossoGialloxVerdex /*37,*/ o  se la variabile SubClass_C2_variabile_V2 è  maggiore di  /*54,*/ 7 /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 non è  uguale a  /*53,*/ 1304 /*37,*/ e  se la variabile SubClass_C2_variabile_V8 non è  diverso da avvio, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V7 il valore 4
        if db((db(self.get_subclass_c2_parametro_p4() == GlobalEnumeration.rossogialloxverdex, di_ctx.subs[2].subs[0].subs[0]) or db((db((db(self.get_subclass_c2_variabile_v2() > 7, di_ctx.subs[2].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c2_contatore_co4().get_valore() == 1304, di_ctx.subs[2].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_subclass_c2_variabile_v8() == GlobalEnumeration.avvio, di_ctx.subs[2].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[1].subs[1])), di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.set_subclass_c2_variabile_v7(4)
        #  /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI1 non è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T3 non è scaduto /*38,*/ o  se il contatore SubClass_C2_contatore_Co4 è  diverso da  /*56,*/ 1432, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V8 il valore avvio
        #   ,altrimenti   Applica gli effetti
        #         della macro SubClass_C2_macroef_M2
        if db((db((db(not db(self.get_subclass_c2_restoreti_ti1_restore().isDisattivato(), di_ctx.subs[3].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[3].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_timer_t3().isScaduto(), di_ctx.subs[3].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[3].subs[0].subs[0].subs[1])), di_ctx.subs[3].subs[0].subs[0]) or db(not db(self.get_subclass_c2_contatore_co4().get_valore() == 1432, di_ctx.subs[3].subs[0].subs[1].subs[0]), di_ctx.subs[3].subs[0].subs[1])), di_ctx.subs[3].subs[0]):
            self.set_subclass_c2_variabile_v8(GlobalEnumeration.avvio)
        else:
            self.macroSubclass_c2_macroef_m2(di_ctx.subs[3].subs[1])
    
    def macroSubclass_c2_macroef_m2(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {110,}  se il ripristino del timer  SubClass_C2_restoreTI_TI2 non è disattivo commento: {35,} e  se il controllo SubClass_C2_controllo_C10 è  uguale a RossoGiallo commento: {35,} e  se il controllo SubClass_C2_controllo_C3 è  diverso da Verde commento: {35,} e  se il controllo SubClass_C2_controllo_C3 non è  uguale a Verde, commento: {69,}Disattiva il timer SubClass_C2_timer_T10
        
         ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V8 il valore avvio
        
        
         commento: {34,}  se il parametro SubClass_C2_parametro_P2 non è  uguale a Verde e  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} o  se il timer SubClass_C2_timer_T10 è scaduto, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V2 il valore 3
        
           
         commento: {41,}  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  commento: {105,} è  uguale a c270x commento: {37,} e  se la variabile SubClass_C2_variabile_V8 non è  uguale a avvio commento: {35,} e  se il controllo SubClass_C2_controllo_C3 è  uguale a Verde commento: {38,} e  se il contatore SubClass_C2_contatore_Co3 è  uguale a  commento: {53,} 151 o  se il controllo ConsDef  è  uguale a FALSE , commento: {66,} Assegna al comando SubClass_C2_comando_C2 il valore  False 
        
         ,altrimenti  commento: {71,}Decrementa il contatore SubClass_C2_contatore_Co4
        
        
         commento: {41,}  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  commento: {105,} è  diverso da c270x commento: {38,} e  se il contatore SubClass_C2_contatore_Co3 non è  uguale a  commento: {53,} 11 o  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} o  se il controllo SubClass_C2_controllo_C3 è  diverso da Verde e  se il controllo ConsDef  è  uguale a FALSE , commento: {69,}Disattiva il timer SubClass_C2_timer_T10
        
         ,altrimenti  commento: {66,} Assegna al comando SubClass_C2_comando_C6 il valore  False 
        
        
        
        }
        """
        def populate_macroSubclass_c2_macroef_m2_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITEStatementImpl\n/*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI2 non è disattivo /*35,*/ e  se il controllo SubClass_C2_controllo_C10 è  uguale a RossoGiallo /*35,*/ e  se il controllo SubClass_C2_controllo_C3 è  diverso da Verde /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a Verde, /*69,*/Disattiva il timer SubClass_C2_timer_T10

 ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V8 il valore avvio""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI2 non è disattivo /*35,*/ e  se il controllo SubClass_C2_controllo_C10 è  uguale a RossoGiallo /*35,*/ e  se il controllo SubClass_C2_controllo_C3 è  diverso da Verde /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a Verde""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di (il timer 'subclass_c2_restoreti_ti2_restore' è inattivo) )  e  ( (subclass_c2_controllo_c10)  è uguale a  (rossogiallo) ) )  e  ( negazione di ((subclass_c2_controllo_c3)  è uguale a  (verde)) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (il timer 'subclass_c2_restoreti_ti2_restore' è inattivo) )  e  ( (subclass_c2_controllo_c10)  è uguale a  (rossogiallo) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c2_restoreti_ti2_restore' è inattivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_restoreti_ti2_restore' è inattivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c10)  è uguale a  (rossogiallo)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c3)  è uguale a  (verde))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c3)  è uguale a  (verde)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c3)  è uguale a  (verde))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c3)  è uguale a  (verde)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITStatement\n/*34,*/  se il parametro SubClass_C2_parametro_P2 non è  uguale a Verde e  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C2_timer_T10 è scaduto, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V2 il valore 3""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se il parametro SubClass_C2_parametro_P2 non è  uguale a Verde e  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C2_timer_T10 è scaduto""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( negazione di ((subclass_c2_parametro_p2)  è uguale a  (verde)) )  e  
( (consdef)  è uguale a  (False) ) )  o  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c2_parametro_p2)  è uguale a  (verde)) )  e  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p2)  è uguale a  (verde))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p2)  è uguale a  (verde)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t10' è scaduto""", [
                            ]),#1
                            ]),#0
                            ]),#1
                            DIStatement("""ITEStatementImpl\n/*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  /*105,*/ è  uguale a c270x /*37,*/ e  se la variabile SubClass_C2_variabile_V8 non è  uguale a avvio /*35,*/ e  se il controllo SubClass_C2_controllo_C3 è  uguale a Verde /*38,*/ e  se il contatore SubClass_C2_contatore_Co3 è  uguale a  /*53,*/ 151 o  se il controllo ConsDef  è  uguale a FALSE , /*66,*/ Assegna al comando SubClass_C2_comando_C2 il valore  False 

 ,altrimenti  /*71,*/Decrementa il contatore SubClass_C2_contatore_Co4""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  /*105,*/ è  uguale a c270x /*37,*/ e  se la variabile SubClass_C2_variabile_V8 non è  uguale a avvio /*35,*/ e  se il controllo SubClass_C2_controllo_C3 è  uguale a Verde /*38,*/ e  se il contatore SubClass_C2_contatore_Co3 è  uguale a  /*53,*/ 151 o  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( ( per ognuna delle seguenti con lista non vuota {((mainclass_c1_parametro_p3 del campo mainclass_c1 della lista subclass_c2_lista_l10)  è uguale a  (c270x))} )  e  ( negazione di ((subclass_c2_variabile_v8)  è uguale a  (avvio)) ) )  e  ( (subclass_c2_controllo_c3)  è uguale a  (verde) ) )  e  
( (subclass_c2_contatore_co3)  è uguale a  (151) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( per ognuna delle seguenti con lista non vuota {((mainclass_c1_parametro_p3 del campo mainclass_c1 della lista subclass_c2_lista_l10)  è uguale a  (c270x))} )  e  ( negazione di ((subclass_c2_variabile_v8)  è uguale a  (avvio)) ) )  e  ( (subclass_c2_controllo_c3)  è uguale a  (verde) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( per ognuna delle seguenti con lista non vuota {((mainclass_c1_parametro_p3 del campo mainclass_c1 della lista subclass_c2_lista_l10)  è uguale a  (c270x))} )  e  ( negazione di ((subclass_c2_variabile_v8)  è uguale a  (avvio)) )""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {((mainclass_c1_parametro_p3 del campo mainclass_c1 della lista subclass_c2_lista_l10)  è uguale a  (c270x))}""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3 del campo mainclass_c1 della lista subclass_c2_lista_l10)  è uguale a  (c270x)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v8)  è uguale a  (avvio))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v8)  è uguale a  (avvio)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c3)  è uguale a  (verde)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co3)  è uguale a  (151)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            ]),#2
                            DIStatement("""ITEStatementImpl\n/*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è  diverso da c270x /*38,*/ e  se il contatore SubClass_C2_contatore_Co3 non è  uguale a  /*53,*/ 11 o  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo SubClass_C2_controllo_C3 è  diverso da Verde e  se il controllo ConsDef  è  uguale a FALSE , /*69,*/Disattiva il timer SubClass_C2_timer_T10

 ,altrimenti  /*66,*/ Assegna al comando SubClass_C2_comando_C6 il valore  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è  diverso da c270x /*38,*/ e  se il contatore SubClass_C2_contatore_Co3 non è  uguale a  /*53,*/ 11 o  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo SubClass_C2_controllo_C3 è  diverso da Verde e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( per ognuna delle seguenti con lista non vuota {(negazione di ((mainclass_c1_parametro_p3 del campo mainclass_c1 della lista subclass_c2_lista_l8)  è uguale a  (c270x)))} )  e  
( negazione di ((subclass_c2_contatore_co3)  è uguale a  (11)) ) )  o  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( per ognuna delle seguenti con lista non vuota {(negazione di ((mainclass_c1_parametro_p3 del campo mainclass_c1 della lista subclass_c2_lista_l8)  è uguale a  (c270x)))} )  e  
( negazione di ((subclass_c2_contatore_co3)  è uguale a  (11)) )""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {(negazione di ((mainclass_c1_parametro_p3 del campo mainclass_c1 della lista subclass_c2_lista_l8)  è uguale a  (c270x)))}""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p3 del campo mainclass_c1 della lista subclass_c2_lista_l8)  è uguale a  (c270x))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3 del campo mainclass_c1 della lista subclass_c2_lista_l8)  è uguale a  (c270x)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co3)  è uguale a  (11))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co3)  è uguale a  (11)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c2_controllo_c3)  è uguale a  (verde)) )  e  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c3)  è uguale a  (verde))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c3)  è uguale a  (verde)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#3
                ])

        populate_macroSubclass_c2_macroef_m2_SrfMacroDefInfo(di_ctx)
        #  /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI2 non è disattivo /*35,*/ e  se il controllo SubClass_C2_controllo_C10 è  uguale a RossoGiallo /*35,*/ e  se il controllo SubClass_C2_controllo_C3 è  diverso da Verde /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a Verde, /*69,*/Disattiva il timer SubClass_C2_timer_T10
        #   ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V8 il valore avvio
        if db((db((db((db(not db(self.get_subclass_c2_restoreti_ti2_restore().isDisattivato(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_controllo_c10() == GlobalEnumeration.rossogiallo, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_controllo_c3() == GlobalEnumeration.verde, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_controllo_c3() == GlobalEnumeration.verde, di_ctx.subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.get_subclass_c2_timer_t10().disattiva()
        else:
            self.set_subclass_c2_variabile_v8(GlobalEnumeration.avvio)
        #  /*34,*/  se il parametro SubClass_C2_parametro_P2 non è  uguale a Verde e  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C2_timer_T10 è scaduto, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V2 il valore 3
        if db((db((db((db(not db(self.get_subclass_c2_parametro_p2() == GlobalEnumeration.verde, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0]) or db(self.get_subclass_c2_timer_t10().isScaduto(), di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.set_subclass_c2_variabile_v2(3)
        #  /*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  /*105,*/ è  uguale a c270x /*37,*/ e  se la variabile SubClass_C2_variabile_V8 non è  uguale a avvio /*35,*/ e  se il controllo SubClass_C2_controllo_C3 è  uguale a Verde /*38,*/ e  se il contatore SubClass_C2_contatore_Co3 è  uguale a  /*53,*/ 151 o  se il controllo ConsDef  è  uguale a FALSE , /*66,*/ Assegna al comando SubClass_C2_comando_C2 il valore  False 
        #   ,altrimenti  /*71,*/Decrementa il contatore SubClass_C2_contatore_Co4
        if db((db((db((db((db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_parametro_p3() == GlobalEnumeration.c270x, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l10())), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_variabile_v8() == GlobalEnumeration.avvio, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_controllo_c3() == GlobalEnumeration.verde, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_contatore_co3().get_valore() == 151, di_ctx.subs[2].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.set_subclass_c2_comando_c2(False)
        else:
            self.get_subclass_c2_contatore_co4().decrementa()
        #  /*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è  diverso da c270x /*38,*/ e  se il contatore SubClass_C2_contatore_Co3 non è  uguale a  /*53,*/ 11 o  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo SubClass_C2_controllo_C3 è  diverso da Verde e  se il controllo ConsDef  è  uguale a FALSE , /*69,*/Disattiva il timer SubClass_C2_timer_T10
        #   ,altrimenti  /*66,*/ Assegna al comando SubClass_C2_comando_C6 il valore  False
        if db((db((db((db(all_notempty(db(not db(it.get_mainclass_c1().get_mainclass_c1_parametro_p3() == GlobalEnumeration.c270x, di_ctx.subs[3].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]), di_ctx.subs[3].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l8())), di_ctx.subs[3].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_contatore_co3().get_valore() == 11, di_ctx.subs[3].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[3].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[3].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[3].subs[0].subs[0].subs[1])), di_ctx.subs[3].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_controllo_c3() == GlobalEnumeration.verde, di_ctx.subs[3].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[3].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[3].subs[0].subs[1].subs[1])), di_ctx.subs[3].subs[0].subs[1])), di_ctx.subs[3].subs[0]):
            self.get_subclass_c2_timer_t10().disattiva()
        else:
            self.set_subclass_c2_comando_c6(False)
    
    def macroSubclass_c2_macroef_m5(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
         
        { commento: {36,}  se il timer SubClass_C2_timer_T3 non è scaduto commento: {38,} e  se il contatore SubClass_C2_contatore_Co3 è  maggiore di  commento: {54,} 115 commento: {38,} o  se il contatore SubClass_C2_contatore_Co3 è  maggiore di  commento: {54,} 110, commento: {71,}Decrementa il contatore SubClass_C2_contatore_Co4
        
           
         commento: {44,}  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  commento: {105,} è  diverso da c270x commento: {37,} e  se la variabile SubClass_C2_variabile_V8 è  diverso da avvio commento: {34,} o  se il parametro SubClass_C2_parametro_P10 è  diverso da  True  commento: {37,} o  se la variabile SubClass_C2_variabile_V2 non è  diverso da  commento: {56,} 10 commento: {36,} e  se il timer SubClass_C2_timer_T3 non è attivo, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V8 il valore avvio
        
         ,altrimenti   Applica gli effetti
               della macro SubClass_C2_macroef_M2  commento: {73,}
        
        
        
        }
        """
        def populate_macroSubclass_c2_macroef_m5_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*36,*/  se il timer SubClass_C2_timer_T3 non è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co3 è  maggiore di  /*54,*/ 115 /*38,*/ o  se il contatore SubClass_C2_contatore_Co3 è  maggiore di  /*54,*/ 110, /*71,*/Decrementa il contatore SubClass_C2_contatore_Co4""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*36,*/  se il timer SubClass_C2_timer_T3 non è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co3 è  maggiore di  /*54,*/ 115 /*38,*/ o  se il contatore SubClass_C2_contatore_Co3 è  maggiore di  /*54,*/ 110""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (il timer 'subclass_c2_timer_t3' è scaduto) )  e  
( (subclass_c2_contatore_co3)  è maggiore di  (115) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c2_timer_t3' è scaduto)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t3' è scaduto""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_contatore_co3)  è maggiore di  (115)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_contatore_co3)  è maggiore di  (110)""", [
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITEStatementImpl\n/*44,*/  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è  diverso da c270x /*37,*/ e  se la variabile SubClass_C2_variabile_V8 è  diverso da avvio /*34,*/ o  se il parametro SubClass_C2_parametro_P10 è  diverso da  True  /*37,*/ o  se la variabile SubClass_C2_variabile_V2 non è  diverso da  /*56,*/ 10 /*36,*/ e  se il timer SubClass_C2_timer_T3 non è attivo, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V8 il valore avvio

 ,altrimenti   Applica gli effetti
       della macro SubClass_C2_macroef_M2""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*44,*/  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è  diverso da c270x /*37,*/ e  se la variabile SubClass_C2_variabile_V8 è  diverso da avvio /*34,*/ o  se il parametro SubClass_C2_parametro_P10 è  diverso da  True  /*37,*/ o  se la variabile SubClass_C2_variabile_V2 non è  diverso da  /*56,*/ 10 /*36,*/ e  se il timer SubClass_C2_timer_T3 non è attivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( per ognuna delle seguenti con lista non vuota {(negazione di ((mainclass_c1_variabile_v8 del campo mainclass_c1 della lista subclass_c2_lista_l8)  è uguale a  (c270x)))} )  e  
( negazione di ((subclass_c2_variabile_v8)  è uguale a  (avvio)) ) )  o  
( negazione di ((subclass_c2_parametro_p10)  è uguale a  (True)) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( per ognuna delle seguenti con lista non vuota {(negazione di ((mainclass_c1_variabile_v8 del campo mainclass_c1 della lista subclass_c2_lista_l8)  è uguale a  (c270x)))} )  e  
( negazione di ((subclass_c2_variabile_v8)  è uguale a  (avvio)) )""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {(negazione di ((mainclass_c1_variabile_v8 del campo mainclass_c1 della lista subclass_c2_lista_l8)  è uguale a  (c270x)))}""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v8 del campo mainclass_c1 della lista subclass_c2_lista_l8)  è uguale a  (c270x))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v8 del campo mainclass_c1 della lista subclass_c2_lista_l8)  è uguale a  (c270x)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v8)  è uguale a  (avvio))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v8)  è uguale a  (avvio)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p10)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p10)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (negazione di ((subclass_c2_variabile_v2)  è uguale a  (10))) )  e  
( negazione di (il timer 'subclass_c2_timer_t3' è attivo) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_variabile_v2)  è uguale a  (10)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v2)  è uguale a  (10))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v2)  è uguale a  (10)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c2_timer_t3' è attivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t3' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro SubClass_C2_macroef_M2"""),#1
                            ]),#1
                ])

        populate_macroSubclass_c2_macroef_m5_SrfMacroDefInfo(di_ctx)
        #  /*36,*/  se il timer SubClass_C2_timer_T3 non è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co3 è  maggiore di  /*54,*/ 115 /*38,*/ o  se il contatore SubClass_C2_contatore_Co3 è  maggiore di  /*54,*/ 110, /*71,*/Decrementa il contatore SubClass_C2_contatore_Co4
        if db((db((db(not db(self.get_subclass_c2_timer_t3().isScaduto(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_contatore_co3().get_valore() > 115, di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_contatore_co3().get_valore() > 110, di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.get_subclass_c2_contatore_co4().decrementa()
        #  /*44,*/  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è  diverso da c270x /*37,*/ e  se la variabile SubClass_C2_variabile_V8 è  diverso da avvio /*34,*/ o  se il parametro SubClass_C2_parametro_P10 è  diverso da  True  /*37,*/ o  se la variabile SubClass_C2_variabile_V2 non è  diverso da  /*56,*/ 10 /*36,*/ e  se il timer SubClass_C2_timer_T3 non è attivo, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V8 il valore avvio
        #   ,altrimenti   Applica gli effetti
        #         della macro SubClass_C2_macroef_M2
        if db((db((db((db(all_notempty(db(not db(it.get_mainclass_c1().get_mainclass_c1_variabile_v8() == GlobalEnumeration.c270x, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l8())), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_variabile_v8() == GlobalEnumeration.avvio, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_parametro_p10() == True, di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0]) or db((db(not db(not db(self.get_subclass_c2_variabile_v2() == 10, di_ctx.subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_timer_t3().isAttivato(), di_ctx.subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.set_subclass_c2_variabile_v8(GlobalEnumeration.avvio)
        else:
            self.macroSubclass_c2_macroef_m2(di_ctx.subs[1].subs[1])
    
    def macroSubclass_c2_macroef_m9(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {41,}  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a c270x,  Applica gli effetti
               della macro SubClass_C2_macroef_M2  commento: {73,}
        
         ,altrimenti  commento: {68,}Attiva il timer SubClass_C2_timer_T10
        
        
         commento: {36,}  se il timer SubClass_C2_timer_T3 non è scaduto,  commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a  commento: {53,}  state1 , commento: {88,} quando  commento: {42,}    MainClass_C1_controllo_C8 del campo  MainClass_C1     è  uguale a c270x commento: {34,} e  se il parametro SubClass_C2_parametro_P2 non è  uguale a Verde commento: {38,} o  se il contatore SubClass_C2_contatore_Co3 non è  diverso da  commento: {56,} 15 commento: {34,} e  se il parametro SubClass_C2_parametro_P2 è  diverso da Verde commento: {35,} e  se il controllo SubClass_C2_controllo_C3 non è  diverso da Verde, commento: {68,}Attiva il timer SubClass_C2_timer_T3
        
         ,altrimenti  commento: {69,}Disattiva il timer SubClass_C2_timer_T10
        
        
        
        }
        """
        def populate_macroSubclass_c2_macroef_m9_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITEStatementImpl\n/*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a c270x,  Applica gli effetti
       della macro SubClass_C2_macroef_M2  /*73,*/

 ,altrimenti  /*68,*/Attiva il timer SubClass_C2_timer_T10""", [
                            DIBoolExpr("""Predicato ForAll\nMainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a c270x""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3 del campo mainclass_c1 della lista subclass_c2_lista_l9)  è uguale a  (c270x)""", [
                            ]),#0
                            ]),#0
                            DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro SubClass_C2_macroef_M2"""),#1
                            ]),#0
                            DIStatement("""ITEStatementImpl\n/*36,*/  se il timer SubClass_C2_timer_T3 non è scaduto,  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a  /*53,*/  state1 , /*88,*/ quando  /*42,*/    MainClass_C1_controllo_C8 del campo  MainClass_C1     è  uguale a c270x /*34,*/ e  se il parametro SubClass_C2_parametro_P2 non è  uguale a Verde /*38,*/ o  se il contatore SubClass_C2_contatore_Co3 non è  diverso da  /*56,*/ 15 /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da Verde /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  diverso da Verde, /*68,*/Attiva il timer SubClass_C2_timer_T3

 ,altrimenti  /*69,*/Disattiva il timer SubClass_C2_timer_T10""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*36,*/  se il timer SubClass_C2_timer_T3 non è scaduto,  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a  /*53,*/  state1 , /*88,*/ quando  /*42,*/    MainClass_C1_controllo_C8 del campo  MainClass_C1     è  uguale a c270x /*34,*/ e  se il parametro SubClass_C2_parametro_P2 non è  uguale a Verde /*38,*/ o  se il contatore SubClass_C2_contatore_Co3 non è  diverso da  /*56,*/ 15 /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da Verde /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  diverso da Verde""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di (il timer 'subclass_c2_timer_t3' è scaduto) )  e  ( per ognuna delle seguenti {se ((mainclass_c1_controllo_c8 del campo mainclass_c1 della lista subclass_c2_lista_l9)  è uguale a  (c270x)) allora ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l9')  è uguale a  (state1))} ) )  e  
( negazione di ((subclass_c2_parametro_p2)  è uguale a  (verde)) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (il timer 'subclass_c2_timer_t3' è scaduto) )  e  ( per ognuna delle seguenti {se ((mainclass_c1_controllo_c8 del campo mainclass_c1 della lista subclass_c2_lista_l9)  è uguale a  (c270x)) allora ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l9')  è uguale a  (state1))} )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c2_timer_t3' è scaduto)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t3' è scaduto""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {se ((mainclass_c1_controllo_c8 del campo mainclass_c1 della lista subclass_c2_lista_l9)  è uguale a  (c270x)) allora ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l9')  è uguale a  (state1))}""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\nse ((mainclass_c1_controllo_c8 del campo mainclass_c1 della lista subclass_c2_lista_l9)  è uguale a  (c270x)) allora ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l9')  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c8 del campo mainclass_c1 della lista subclass_c2_lista_l9)  è uguale a  (c270x)""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(lo stato di 'mainclass_c1 della lista subclass_c2_lista_l9')  è uguale a  (state1)""", [
                            ]),#1
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p2)  è uguale a  (verde))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p2)  è uguale a  (verde)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di (negazione di ((subclass_c2_contatore_co3)  è uguale a  (15))) )  e  ( negazione di ((subclass_c2_parametro_p2)  è uguale a  (verde)) ) )  e  
( negazione di (negazione di ((subclass_c2_controllo_c3)  è uguale a  (verde))) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (negazione di ((subclass_c2_contatore_co3)  è uguale a  (15))) )  e  ( negazione di ((subclass_c2_parametro_p2)  è uguale a  (verde)) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_contatore_co3)  è uguale a  (15)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co3)  è uguale a  (15))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co3)  è uguale a  (15)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p2)  è uguale a  (verde))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p2)  è uguale a  (verde)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_controllo_c3)  è uguale a  (verde)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c3)  è uguale a  (verde))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c3)  è uguale a  (verde)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#1
                ])

        populate_macroSubclass_c2_macroef_m9_SrfMacroDefInfo(di_ctx)
        #  /*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a c270x,  Applica gli effetti
        #         della macro SubClass_C2_macroef_M2  /*73,*/
        #   ,altrimenti  /*68,*/Attiva il timer SubClass_C2_timer_T10
        if db(all(db(it.get_mainclass_c1().get_mainclass_c1_parametro_p3() == GlobalEnumeration.c270x, di_ctx.subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l9())), di_ctx.subs[0].subs[0]):
            self.macroSubclass_c2_macroef_m2(di_ctx.subs[0].subs[1])
        else:
            self.get_subclass_c2_timer_t10().attiva()
        #  /*36,*/  se il timer SubClass_C2_timer_T3 non è scaduto,  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a  /*53,*/  state1 , /*88,*/ quando  /*42,*/    MainClass_C1_controllo_C8 del campo  MainClass_C1     è  uguale a c270x /*34,*/ e  se il parametro SubClass_C2_parametro_P2 non è  uguale a Verde /*38,*/ o  se il contatore SubClass_C2_contatore_Co3 non è  diverso da  /*56,*/ 15 /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da Verde /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  diverso da Verde, /*68,*/Attiva il timer SubClass_C2_timer_T3
        #   ,altrimenti  /*69,*/Disattiva il timer SubClass_C2_timer_T10
        if db((db((db((db(not db(self.get_subclass_c2_timer_t3().isScaduto(), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0]) and db(all(db(it.get_mainclass_c1().get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l9()) if db(it.get_mainclass_c1().get_mainclass_c1_controllo_c8() == GlobalEnumeration.c270x, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0][idx])), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_parametro_p2() == GlobalEnumeration.verde, di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0]) or db((db((db(not db(not db(self.get_subclass_c2_contatore_co3().get_valore() == 15, di_ctx.subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c2_parametro_p2() == GlobalEnumeration.verde, di_ctx.subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_subclass_c2_controllo_c3() == GlobalEnumeration.verde, di_ctx.subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.get_subclass_c2_timer_t3().attiva()
        else:
            self.get_subclass_c2_timer_t10().disattiva()
    
    # verify macros
    @srf_value_macro("macroSubclass_c2_macrove_m3")
    def macroSubclass_c2_macrove_m3(self, argomento_ave1, argomento_ave5, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        { commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L8 è  uguale a  commento: {53,}  state1  e  se l'argomento argomento_ave1 è  diverso da RossoGialloxVerdex commento: {39,} , Verifica che   commento: {47,49,50,52,}  commento: {34,}  il parametro SubClass_C2_parametro_P1 sia  uguale a RossoGialloxVerdex
         commento: {104,} o  che  commento: {,}  la variabile SubClass_C2_variabile_V2 non sia  diverso da  commento: {56,} 10
         commento: {104,} o  che   l'argomento argomento_ave5 non  sia  uguale a avvio commento: {,} 
         commento: {104,} o  che  commento: {,}  il timer SubClass_C2_timer_T10 sia scaduto
        
        
        }
        """
        def populate_macroSubclass_c2_macrove_m3_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L8 è  uguale a  /*53,*/  state1  e  se l'argomento argomento_ave1 è  diverso da RossoGialloxVerdex /*39,*/ , Verifica che   /*47,49,50,52,*/  /*34,*/  il parametro SubClass_C2_parametro_P1 sia  uguale a RossoGialloxVerdex
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  diverso da  /*56,*/ 10
 /*104,*/ o  che   l'argomento argomento_ave5 non  sia  uguale a avvio /*,*/ 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T10 sia scaduto""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L8 è  uguale a  /*53,*/  state1  e  se l'argomento argomento_ave1 è  diverso da RossoGialloxVerdex /*39,*/ , Verifica che   /*47,49,50,52,*/  /*34,*/  il parametro SubClass_C2_parametro_P1 sia  uguale a RossoGialloxVerdex
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  diverso da  /*56,*/ 10
 /*104,*/ o  che   l'argomento argomento_ave5 non  sia  uguale a avvio /*,*/ 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T10 sia scaduto""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L8 è  uguale a  /*53,*/  state1  e  se l'argomento argomento_ave1 è  diverso da RossoGialloxVerdex""", [
                            DIBoolExpr("""Predicato ForAll\nlo stato del campo  MainClass_C1 di SubClass_C2_lista_L8 è  uguale a  /*53,*/  state1""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'mainclass_c1 della lista subclass_c2_lista_l8')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave1 è  diverso da RossoGialloxVerdex""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave1)  è uguale a  (rossogialloxverdex)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,50,52,*/  /*34,*/  il parametro SubClass_C2_parametro_P1 sia  uguale a RossoGialloxVerdex
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  diverso da  /*56,*/ 10
 /*104,*/ o  che   l'argomento argomento_ave5 non  sia  uguale a avvio /*,*/ 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T10 sia scaduto""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,50,52,*/  /*34,*/  il parametro SubClass_C2_parametro_P1 sia  uguale a RossoGialloxVerdex
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  diverso da  /*56,*/ 10
 /*104,*/ o  che   l'argomento argomento_ave5 non  sia  uguale a avvio""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,50,52,*/  /*34,*/  il parametro SubClass_C2_parametro_P1 sia  uguale a RossoGialloxVerdex
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  diverso da  /*56,*/ 10""", [
                            DIBoolExpr("""EqualImpl\nche   /*47,49,50,52,*/  /*34,*/  il parametro SubClass_C2_parametro_P1 sia  uguale a RossoGialloxVerdex""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  diverso da  /*56,*/ 10""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v2)  è uguale a  (10))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v2)  è uguale a  (10)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave5 non  sia  uguale a avvio""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave5)  è uguale a  (avvio)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer SubClass_C2_timer_T10 sia scaduto""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroSubclass_c2_macrove_m3_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db(all(db(it.get_mainclass_c1().get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l8())), di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(not db(argomento_ave1 == GlobalEnumeration.rossogialloxverdex, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db((db((db(self.get_subclass_c2_parametro_p1() == GlobalEnumeration.rossogialloxverdex, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_subclass_c2_variabile_v2() == 10, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db(not db(argomento_ave5 == GlobalEnumeration.avvio, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0]) or db(self.get_subclass_c2_timer_t10().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0])), di_ctx.subs[0])
    
    @srf_value_macro("macroSubclass_c2_macrove_m4")
    def macroSubclass_c2_macrove_m4(self, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
         
        {  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} o  se il timer SubClass_C2_timer_T3 non è scaduto commento: {34,} o  se il parametro SubClass_C2_parametro_P2 non è  uguale a Verde, Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
        
        
        }
        """
        def populate_macroSubclass_c2_macrove_m4_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C2_timer_T3 non è scaduto /*34,*/ o  se il parametro SubClass_C2_parametro_P2 non è  uguale a Verde, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\nse il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C2_timer_T3 non è scaduto /*34,*/ o  se il parametro SubClass_C2_parametro_P2 non è  uguale a Verde, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C2_timer_T3 non è scaduto /*34,*/ o  se il parametro SubClass_C2_parametro_P2 non è  uguale a Verde""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C2_timer_T3 non è scaduto""", [
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C2_timer_T3 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t3' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P2 non è  uguale a Verde""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p2)  è uguale a  (verde)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""EqualImpl\nche   /*48,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroSubclass_c2_macrove_m4_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_timer_t3().isScaduto(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_parametro_p2() == GlobalEnumeration.verde, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0])), di_ctx.subs[0])
    
    @srf_value_macro("macroSubclass_c2_macrove_m6")
    def macroSubclass_c2_macrove_m6(self, argomento_ave2, argomento_ave3, argomento_ave4, argomento_ave7, argomento_ave8, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        { commento: {62,} commento: {41,}  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L7 è  uguale a c270x commento: {35,} e  se il controllo SubClass_C2_controllo_C3 è  uguale a Verde commento: {38,} o  se il contatore SubClass_C2_contatore_Co3 è  maggiore di  commento: {54,} 11504 commento: {37,} e  se la variabile SubClass_C2_variabile_V8 non è  uguale a avvio, Almeno una delle seguenti { 
         commento: {62,} commento: {41,}  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L8 è  uguale a c270x commento: {34,} e  se il parametro SubClass_C2_parametro_P2 è  diverso da Verde commento: {34,} e  se il parametro SubClass_C2_parametro_P2 non è  diverso da Verde commento: {35,} o  se il controllo SubClass_C2_controllo_C10 non è  uguale a RossoGiallo commento: {38,} e  se il contatore SubClass_C2_contatore_Co3 non è  maggiore di  commento: {54,} 133, Almeno una delle seguenti { 
         commento: {63,} commento: {110,}  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è disattivo commento: {38,} o  se il contatore SubClass_C2_contatore_Co4 è  uguale a  commento: {53,} 1221, Solo una delle seguenti { 
         commento: {63,} commento: {35,}  se il controllo SubClass_C2_controllo_C10 è  uguale a RossoGiallo e  se l'argomento argomento_ave3 non  è  uguale a  False  commento: {39,}  commento: {37,} e  se la variabile SubClass_C2_variabile_V7 è  minore di  commento: {55,} 6 commento: {38,} e  se il contatore SubClass_C2_contatore_Co4 non è  diverso da  commento: {56,} 11504 commento: {36,} o  se il timer SubClass_C2_timer_T3 è disattivo, Solo una delle seguenti { 
         commento: {63,} commento: {42,}  se  MainClass_C1_controllo_C8 del campo  MainClass_C1 di SubClass_C2_lista_L8 è  uguale a c270x commento: {36,} o  se il timer SubClass_C2_timer_T3 non è scaduto commento: {38,} e  se il contatore SubClass_C2_contatore_Co4 è  minore di  commento: {55,} 12504 commento: {36,} o  se il timer SubClass_C2_timer_T3 è attivo, Solo una delle seguenti { 
         commento: {61,} commento: {43,}  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  commento: {105,} è attivo commento: {34,} o  se il parametro SubClass_C2_parametro_P2 non è  uguale a Verde commento: {36,} o  se il timer SubClass_C2_timer_T3 non è disattivo commento: {38,} e  se il contatore SubClass_C2_contatore_Co4 è  diverso da  commento: {56,} 1332 commento: {37,} o  se la variabile SubClass_C2_variabile_V5 è  uguale a RossoGiallo e  se l'argomento argomento_ave4 non  è  uguale a  True  commento: {39,} , Tutte le seguenti { 
         commento: {36,}  se il timer SubClass_C2_timer_T3 è disattivo commento: {34,} e  se il parametro SubClass_C2_parametro_P4 è  uguale a RossoGialloxVerdex commento: {37,} e  se la variabile SubClass_C2_variabile_V2 è  diverso da  commento: {56,} 2 commento: {38,} e  se il contatore SubClass_C2_contatore_Co4 non è  uguale a  commento: {53,} 131 e  se l'argomento argomento_ave2 è  uguale a RossoGialloxVerdex commento: {39,}  commento: {36,} e  se il timer SubClass_C2_timer_T3 non è disattivo, Verifica che   commento: {50,}  commento: {,}  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio
        
        
         } Verifica che   commento: {49,50,51,52,}  commento: {,}  il timer SubClass_C2_timer_T3 non sia disattivo
         commento: {104,} e  che  commento: {,}  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio
         commento: {104,} o  che   l'argomento argomento_ave2 sia  uguale a RossoGialloxVerdex commento: {,} 
         commento: {104,} o  che  commento: {37,}  la variabile SubClass_C2_variabile_V7 sia  uguale a  commento: {53,} 7
         commento: {104,} o  che  commento: {,}  il contatore SubClass_C2_contatore_Co4 sia  maggiore di  commento: {54,} 1550
         commento: {104,} e  che  commento: {37,}  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio
        
        
         } Verifica che   commento: {47,48,49,50,52,}  commento: {34,}  il parametro SubClass_C2_parametro_P2 sia  diverso da Verde
         commento: {104,} e  che  commento: {,}  il controllo SubClass_C2_controllo_C3 non sia  diverso da Verde
         commento: {104,} e  che  commento: {,}  il timer SubClass_C2_timer_T10 sia disattivo
         commento: {104,} o  che  commento: {,}  la variabile SubClass_C2_variabile_V2 sia  diverso da  commento: {56,} 10
         commento: {104,} o  che  commento: {35,}  il controllo SubClass_C2_controllo_C10 non sia  diverso da RossoGiallo
         commento: {104,} e  che   l'argomento argomento_ave4 non  sia  uguale a  False  commento: {,} 
        
        
         } Verifica che   commento: {49,52,}   l'argomento argomento_ave7 non  sia  uguale a  True  commento: {,} 
         commento: {104,} e  che  commento: {,}  il timer SubClass_C2_timer_T10 sia attivo
        
        
         } Verifica che   commento: {47,49,50,}  commento: {,}  il timer SubClass_C2_timer_T10 non sia disattivo
         commento: {104,} e  che  commento: {34,}  il parametro SubClass_C2_parametro_P2 sia  uguale a Verde
         commento: {104,} e  che  commento: {34,}  il parametro SubClass_C2_parametro_P2 non sia  diverso da Verde
         commento: {104,} e  che  commento: {36,}  il timer SubClass_C2_timer_T10 non sia disattivo
         commento: {104,} o  che  commento: {,}  la variabile SubClass_C2_variabile_V8 sia  diverso da avvio
        
        
         } Verifica che   commento: {52,}   l'argomento argomento_ave4 non  sia  uguale a  True  commento: {,} 
        
        
         } Verifica che   commento: {50,51,52,}   l'argomento argomento_ave4 non  sia  uguale a  False  commento: {,} 
         commento: {104,} o  che   l'argomento argomento_ave4 sia  uguale a  True  commento: {39,} 
         commento: {104,} e  che  commento: {,}  la variabile SubClass_C2_variabile_V2 sia  maggiore di  commento: {54,} 6
         commento: {104,} e  che  commento: {,}  il contatore SubClass_C2_contatore_Co3 sia  uguale a  commento: {53,} 13
        
        
        }
        """
        def populate_macroSubclass_c2_macrove_m6_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L7 è  uguale a c270x /*35,*/ e  se il controllo SubClass_C2_controllo_C3 è  uguale a Verde /*38,*/ o  se il contatore SubClass_C2_contatore_Co3 è  maggiore di  /*54,*/ 11504 /*37,*/ e  se la variabile SubClass_C2_variabile_V8 non è  uguale a avvio, Almeno una delle seguenti { 
 /*62,*/ /*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L8 è  uguale a c270x /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da Verde /*34,*/ e  se il parametro SubClass_C2_parametro_P2 non è  diverso da Verde /*35,*/ o  se il controllo SubClass_C2_controllo_C10 non è  uguale a RossoGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co3 non è  maggiore di  /*54,*/ 133, Almeno una delle seguenti { 
 /*63,*/ /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co4 è  uguale a  /*53,*/ 1221, Solo una delle seguenti { 
 /*63,*/ /*35,*/  se il controllo SubClass_C2_controllo_C10 è  uguale a RossoGiallo e  se l'argomento argomento_ave3 non  è  uguale a  False  /*39,*/  /*37,*/ e  se la variabile SubClass_C2_variabile_V7 è  minore di  /*55,*/ 6 /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 non è  diverso da  /*56,*/ 11504 /*36,*/ o  se il timer SubClass_C2_timer_T3 è disattivo, Solo una delle seguenti { 
 /*63,*/ /*42,*/  se  MainClass_C1_controllo_C8 del campo  MainClass_C1 di SubClass_C2_lista_L8 è  uguale a c270x /*36,*/ o  se il timer SubClass_C2_timer_T3 non è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 è  minore di  /*55,*/ 12504 /*36,*/ o  se il timer SubClass_C2_timer_T3 è attivo, Solo una delle seguenti { 
 /*61,*/ /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P2 non è  uguale a Verde /*36,*/ o  se il timer SubClass_C2_timer_T3 non è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 è  diverso da  /*56,*/ 1332 /*37,*/ o  se la variabile SubClass_C2_variabile_V5 è  uguale a RossoGiallo e  se l'argomento argomento_ave4 non  è  uguale a  True  /*39,*/ , Tutte le seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T3 è disattivo /*34,*/ e  se il parametro SubClass_C2_parametro_P4 è  uguale a RossoGialloxVerdex /*37,*/ e  se la variabile SubClass_C2_variabile_V2 è  diverso da  /*56,*/ 2 /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 non è  uguale a  /*53,*/ 131 e  se l'argomento argomento_ave2 è  uguale a RossoGialloxVerdex /*39,*/  /*36,*/ e  se il timer SubClass_C2_timer_T3 non è disattivo, Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio


 } Verifica che   /*49,50,51,52,*/  /*,*/  il timer SubClass_C2_timer_T3 non sia disattivo
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio
 /*104,*/ o  che   l'argomento argomento_ave2 sia  uguale a RossoGialloxVerdex /*,*/ 
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V7 sia  uguale a  /*53,*/ 7
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co4 sia  maggiore di  /*54,*/ 1550
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio


 } Verifica che   /*47,48,49,50,52,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  diverso da Verde
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da Verde
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T10 sia disattivo
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V2 sia  diverso da  /*56,*/ 10
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C2_controllo_C10 non sia  diverso da RossoGiallo
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  uguale a  False  /*,*/ 


 } Verifica che   /*49,52,*/   l'argomento argomento_ave7 non  sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T10 sia attivo


 } Verifica che   /*47,49,50,*/  /*,*/  il timer SubClass_C2_timer_T10 non sia disattivo
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  uguale a Verde
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  diverso da Verde
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T10 non sia disattivo
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V8 sia  diverso da avvio


 } Verifica che   /*52,*/   l'argomento argomento_ave4 non  sia  uguale a  True  /*,*/ 


 } Verifica che   /*50,51,52,*/   l'argomento argomento_ave4 non  sia  uguale a  False  /*,*/ 
 /*104,*/ o  che   l'argomento argomento_ave4 sia  uguale a  True  /*39,*/ 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V2 sia  maggiore di  /*54,*/ 6
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co3 sia  uguale a  /*53,*/ 13""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L7 è  uguale a c270x /*35,*/ e  se il controllo SubClass_C2_controllo_C3 è  uguale a Verde /*38,*/ o  se il contatore SubClass_C2_contatore_Co3 è  maggiore di  /*54,*/ 11504 /*37,*/ e  se la variabile SubClass_C2_variabile_V8 non è  uguale a avvio, Almeno una delle seguenti { 
 /*62,*/ /*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L8 è  uguale a c270x /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da Verde /*34,*/ e  se il parametro SubClass_C2_parametro_P2 non è  diverso da Verde /*35,*/ o  se il controllo SubClass_C2_controllo_C10 non è  uguale a RossoGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co3 non è  maggiore di  /*54,*/ 133, Almeno una delle seguenti { 
 /*63,*/ /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co4 è  uguale a  /*53,*/ 1221, Solo una delle seguenti { 
 /*63,*/ /*35,*/  se il controllo SubClass_C2_controllo_C10 è  uguale a RossoGiallo e  se l'argomento argomento_ave3 non  è  uguale a  False  /*39,*/  /*37,*/ e  se la variabile SubClass_C2_variabile_V7 è  minore di  /*55,*/ 6 /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 non è  diverso da  /*56,*/ 11504 /*36,*/ o  se il timer SubClass_C2_timer_T3 è disattivo, Solo una delle seguenti { 
 /*63,*/ /*42,*/  se  MainClass_C1_controllo_C8 del campo  MainClass_C1 di SubClass_C2_lista_L8 è  uguale a c270x /*36,*/ o  se il timer SubClass_C2_timer_T3 non è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 è  minore di  /*55,*/ 12504 /*36,*/ o  se il timer SubClass_C2_timer_T3 è attivo, Solo una delle seguenti { 
 /*61,*/ /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P2 non è  uguale a Verde /*36,*/ o  se il timer SubClass_C2_timer_T3 non è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 è  diverso da  /*56,*/ 1332 /*37,*/ o  se la variabile SubClass_C2_variabile_V5 è  uguale a RossoGiallo e  se l'argomento argomento_ave4 non  è  uguale a  True  /*39,*/ , Tutte le seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T3 è disattivo /*34,*/ e  se il parametro SubClass_C2_parametro_P4 è  uguale a RossoGialloxVerdex /*37,*/ e  se la variabile SubClass_C2_variabile_V2 è  diverso da  /*56,*/ 2 /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 non è  uguale a  /*53,*/ 131 e  se l'argomento argomento_ave2 è  uguale a RossoGialloxVerdex /*39,*/  /*36,*/ e  se il timer SubClass_C2_timer_T3 non è disattivo, Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio


 } Verifica che   /*49,50,51,52,*/  /*,*/  il timer SubClass_C2_timer_T3 non sia disattivo
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio
 /*104,*/ o  che   l'argomento argomento_ave2 sia  uguale a RossoGialloxVerdex /*,*/ 
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V7 sia  uguale a  /*53,*/ 7
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co4 sia  maggiore di  /*54,*/ 1550
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio


 } Verifica che   /*47,48,49,50,52,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  diverso da Verde
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da Verde
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T10 sia disattivo
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V2 sia  diverso da  /*56,*/ 10
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C2_controllo_C10 non sia  diverso da RossoGiallo
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  uguale a  False  /*,*/ 


 } Verifica che   /*49,52,*/   l'argomento argomento_ave7 non  sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T10 sia attivo


 } Verifica che   /*47,49,50,*/  /*,*/  il timer SubClass_C2_timer_T10 non sia disattivo
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  uguale a Verde
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  diverso da Verde
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T10 non sia disattivo
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V8 sia  diverso da avvio


 } Verifica che   /*52,*/   l'argomento argomento_ave4 non  sia  uguale a  True  /*,*/ 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L7 è  uguale a c270x /*35,*/ e  se il controllo SubClass_C2_controllo_C3 è  uguale a Verde /*38,*/ o  se il contatore SubClass_C2_contatore_Co3 è  maggiore di  /*54,*/ 11504 /*37,*/ e  se la variabile SubClass_C2_variabile_V8 non è  uguale a avvio""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L7 è  uguale a c270x /*35,*/ e  se il controllo SubClass_C2_controllo_C3 è  uguale a Verde""", [
                            DIBoolExpr("""Predicato ForAll\nMainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L7 è  uguale a c270x""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3 del campo mainclass_c1 della lista subclass_c2_lista_l7)  è uguale a  (c270x)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo SubClass_C2_controllo_C3 è  uguale a Verde""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il contatore SubClass_C2_contatore_Co3 è  maggiore di  /*54,*/ 11504 /*37,*/ e  se la variabile SubClass_C2_variabile_V8 non è  uguale a avvio""", [
                            DIBoolExpr("""GreaterThanImpl\nil contatore SubClass_C2_contatore_Co3 è  maggiore di  /*54,*/ 11504""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V8 non è  uguale a avvio""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v8)  è uguale a  (avvio)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*62,*/ /*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L8 è  uguale a c270x /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da Verde /*34,*/ e  se il parametro SubClass_C2_parametro_P2 non è  diverso da Verde /*35,*/ o  se il controllo SubClass_C2_controllo_C10 non è  uguale a RossoGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co3 non è  maggiore di  /*54,*/ 133, Almeno una delle seguenti { 
 /*63,*/ /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co4 è  uguale a  /*53,*/ 1221, Solo una delle seguenti { 
 /*63,*/ /*35,*/  se il controllo SubClass_C2_controllo_C10 è  uguale a RossoGiallo e  se l'argomento argomento_ave3 non  è  uguale a  False  /*39,*/  /*37,*/ e  se la variabile SubClass_C2_variabile_V7 è  minore di  /*55,*/ 6 /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 non è  diverso da  /*56,*/ 11504 /*36,*/ o  se il timer SubClass_C2_timer_T3 è disattivo, Solo una delle seguenti { 
 /*63,*/ /*42,*/  se  MainClass_C1_controllo_C8 del campo  MainClass_C1 di SubClass_C2_lista_L8 è  uguale a c270x /*36,*/ o  se il timer SubClass_C2_timer_T3 non è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 è  minore di  /*55,*/ 12504 /*36,*/ o  se il timer SubClass_C2_timer_T3 è attivo, Solo una delle seguenti { 
 /*61,*/ /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P2 non è  uguale a Verde /*36,*/ o  se il timer SubClass_C2_timer_T3 non è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 è  diverso da  /*56,*/ 1332 /*37,*/ o  se la variabile SubClass_C2_variabile_V5 è  uguale a RossoGiallo e  se l'argomento argomento_ave4 non  è  uguale a  True  /*39,*/ , Tutte le seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T3 è disattivo /*34,*/ e  se il parametro SubClass_C2_parametro_P4 è  uguale a RossoGialloxVerdex /*37,*/ e  se la variabile SubClass_C2_variabile_V2 è  diverso da  /*56,*/ 2 /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 non è  uguale a  /*53,*/ 131 e  se l'argomento argomento_ave2 è  uguale a RossoGialloxVerdex /*39,*/  /*36,*/ e  se il timer SubClass_C2_timer_T3 non è disattivo, Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio


 } Verifica che   /*49,50,51,52,*/  /*,*/  il timer SubClass_C2_timer_T3 non sia disattivo
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio
 /*104,*/ o  che   l'argomento argomento_ave2 sia  uguale a RossoGialloxVerdex /*,*/ 
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V7 sia  uguale a  /*53,*/ 7
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co4 sia  maggiore di  /*54,*/ 1550
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio


 } Verifica che   /*47,48,49,50,52,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  diverso da Verde
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da Verde
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T10 sia disattivo
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V2 sia  diverso da  /*56,*/ 10
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C2_controllo_C10 non sia  diverso da RossoGiallo
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  uguale a  False  /*,*/ 


 } Verifica che   /*49,52,*/   l'argomento argomento_ave7 non  sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T10 sia attivo


 } Verifica che   /*47,49,50,*/  /*,*/  il timer SubClass_C2_timer_T10 non sia disattivo
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  uguale a Verde
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  diverso da Verde
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T10 non sia disattivo
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V8 sia  diverso da avvio


 } Verifica che   /*52,*/   l'argomento argomento_ave4 non  sia  uguale a  True  /*,*/ 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L8 è  uguale a c270x /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da Verde /*34,*/ e  se il parametro SubClass_C2_parametro_P2 non è  diverso da Verde /*35,*/ o  se il controllo SubClass_C2_controllo_C10 non è  uguale a RossoGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co3 non è  maggiore di  /*54,*/ 133, Almeno una delle seguenti { 
 /*63,*/ /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co4 è  uguale a  /*53,*/ 1221, Solo una delle seguenti { 
 /*63,*/ /*35,*/  se il controllo SubClass_C2_controllo_C10 è  uguale a RossoGiallo e  se l'argomento argomento_ave3 non  è  uguale a  False  /*39,*/  /*37,*/ e  se la variabile SubClass_C2_variabile_V7 è  minore di  /*55,*/ 6 /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 non è  diverso da  /*56,*/ 11504 /*36,*/ o  se il timer SubClass_C2_timer_T3 è disattivo, Solo una delle seguenti { 
 /*63,*/ /*42,*/  se  MainClass_C1_controllo_C8 del campo  MainClass_C1 di SubClass_C2_lista_L8 è  uguale a c270x /*36,*/ o  se il timer SubClass_C2_timer_T3 non è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 è  minore di  /*55,*/ 12504 /*36,*/ o  se il timer SubClass_C2_timer_T3 è attivo, Solo una delle seguenti { 
 /*61,*/ /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P2 non è  uguale a Verde /*36,*/ o  se il timer SubClass_C2_timer_T3 non è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 è  diverso da  /*56,*/ 1332 /*37,*/ o  se la variabile SubClass_C2_variabile_V5 è  uguale a RossoGiallo e  se l'argomento argomento_ave4 non  è  uguale a  True  /*39,*/ , Tutte le seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T3 è disattivo /*34,*/ e  se il parametro SubClass_C2_parametro_P4 è  uguale a RossoGialloxVerdex /*37,*/ e  se la variabile SubClass_C2_variabile_V2 è  diverso da  /*56,*/ 2 /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 non è  uguale a  /*53,*/ 131 e  se l'argomento argomento_ave2 è  uguale a RossoGialloxVerdex /*39,*/  /*36,*/ e  se il timer SubClass_C2_timer_T3 non è disattivo, Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio


 } Verifica che   /*49,50,51,52,*/  /*,*/  il timer SubClass_C2_timer_T3 non sia disattivo
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio
 /*104,*/ o  che   l'argomento argomento_ave2 sia  uguale a RossoGialloxVerdex /*,*/ 
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V7 sia  uguale a  /*53,*/ 7
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co4 sia  maggiore di  /*54,*/ 1550
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio


 } Verifica che   /*47,48,49,50,52,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  diverso da Verde
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da Verde
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T10 sia disattivo
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V2 sia  diverso da  /*56,*/ 10
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C2_controllo_C10 non sia  diverso da RossoGiallo
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  uguale a  False  /*,*/ 


 } Verifica che   /*49,52,*/   l'argomento argomento_ave7 non  sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T10 sia attivo


 } Verifica che   /*47,49,50,*/  /*,*/  il timer SubClass_C2_timer_T10 non sia disattivo
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  uguale a Verde
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  diverso da Verde
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T10 non sia disattivo
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V8 sia  diverso da avvio


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L8 è  uguale a c270x /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da Verde /*34,*/ e  se il parametro SubClass_C2_parametro_P2 non è  diverso da Verde /*35,*/ o  se il controllo SubClass_C2_controllo_C10 non è  uguale a RossoGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co3 non è  maggiore di  /*54,*/ 133""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L8 è  uguale a c270x /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da Verde /*34,*/ e  se il parametro SubClass_C2_parametro_P2 non è  diverso da Verde""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L8 è  uguale a c270x /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da Verde""", [
                            DIBoolExpr("""Predicato ForAll\nMainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L8 è  uguale a c270x""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3 del campo mainclass_c1 della lista subclass_c2_lista_l8)  è uguale a  (c270x)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P2 è  diverso da Verde""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p2)  è uguale a  (verde)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P2 non è  diverso da Verde""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p2)  è uguale a  (verde))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p2)  è uguale a  (verde)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo SubClass_C2_controllo_C10 non è  uguale a RossoGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co3 non è  maggiore di  /*54,*/ 133""", [
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C10 non è  uguale a RossoGiallo""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c10)  è uguale a  (rossogiallo)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co3 non è  maggiore di  /*54,*/ 133""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_contatore_co3)  è maggiore di  (133)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*63,*/ /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co4 è  uguale a  /*53,*/ 1221, Solo una delle seguenti { 
 /*63,*/ /*35,*/  se il controllo SubClass_C2_controllo_C10 è  uguale a RossoGiallo e  se l'argomento argomento_ave3 non  è  uguale a  False  /*39,*/  /*37,*/ e  se la variabile SubClass_C2_variabile_V7 è  minore di  /*55,*/ 6 /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 non è  diverso da  /*56,*/ 11504 /*36,*/ o  se il timer SubClass_C2_timer_T3 è disattivo, Solo una delle seguenti { 
 /*63,*/ /*42,*/  se  MainClass_C1_controllo_C8 del campo  MainClass_C1 di SubClass_C2_lista_L8 è  uguale a c270x /*36,*/ o  se il timer SubClass_C2_timer_T3 non è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 è  minore di  /*55,*/ 12504 /*36,*/ o  se il timer SubClass_C2_timer_T3 è attivo, Solo una delle seguenti { 
 /*61,*/ /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P2 non è  uguale a Verde /*36,*/ o  se il timer SubClass_C2_timer_T3 non è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 è  diverso da  /*56,*/ 1332 /*37,*/ o  se la variabile SubClass_C2_variabile_V5 è  uguale a RossoGiallo e  se l'argomento argomento_ave4 non  è  uguale a  True  /*39,*/ , Tutte le seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T3 è disattivo /*34,*/ e  se il parametro SubClass_C2_parametro_P4 è  uguale a RossoGialloxVerdex /*37,*/ e  se la variabile SubClass_C2_variabile_V2 è  diverso da  /*56,*/ 2 /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 non è  uguale a  /*53,*/ 131 e  se l'argomento argomento_ave2 è  uguale a RossoGialloxVerdex /*39,*/  /*36,*/ e  se il timer SubClass_C2_timer_T3 non è disattivo, Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio


 } Verifica che   /*49,50,51,52,*/  /*,*/  il timer SubClass_C2_timer_T3 non sia disattivo
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio
 /*104,*/ o  che   l'argomento argomento_ave2 sia  uguale a RossoGialloxVerdex /*,*/ 
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V7 sia  uguale a  /*53,*/ 7
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co4 sia  maggiore di  /*54,*/ 1550
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio


 } Verifica che   /*47,48,49,50,52,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  diverso da Verde
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da Verde
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T10 sia disattivo
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V2 sia  diverso da  /*56,*/ 10
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C2_controllo_C10 non sia  diverso da RossoGiallo
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  uguale a  False  /*,*/ 


 } Verifica che   /*49,52,*/   l'argomento argomento_ave7 non  sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T10 sia attivo


 } Verifica che   /*47,49,50,*/  /*,*/  il timer SubClass_C2_timer_T10 non sia disattivo
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  uguale a Verde
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  diverso da Verde
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T10 non sia disattivo
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V8 sia  diverso da avvio


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co4 è  uguale a  /*53,*/ 1221, Solo una delle seguenti { 
 /*63,*/ /*35,*/  se il controllo SubClass_C2_controllo_C10 è  uguale a RossoGiallo e  se l'argomento argomento_ave3 non  è  uguale a  False  /*39,*/  /*37,*/ e  se la variabile SubClass_C2_variabile_V7 è  minore di  /*55,*/ 6 /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 non è  diverso da  /*56,*/ 11504 /*36,*/ o  se il timer SubClass_C2_timer_T3 è disattivo, Solo una delle seguenti { 
 /*63,*/ /*42,*/  se  MainClass_C1_controllo_C8 del campo  MainClass_C1 di SubClass_C2_lista_L8 è  uguale a c270x /*36,*/ o  se il timer SubClass_C2_timer_T3 non è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 è  minore di  /*55,*/ 12504 /*36,*/ o  se il timer SubClass_C2_timer_T3 è attivo, Solo una delle seguenti { 
 /*61,*/ /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P2 non è  uguale a Verde /*36,*/ o  se il timer SubClass_C2_timer_T3 non è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 è  diverso da  /*56,*/ 1332 /*37,*/ o  se la variabile SubClass_C2_variabile_V5 è  uguale a RossoGiallo e  se l'argomento argomento_ave4 non  è  uguale a  True  /*39,*/ , Tutte le seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T3 è disattivo /*34,*/ e  se il parametro SubClass_C2_parametro_P4 è  uguale a RossoGialloxVerdex /*37,*/ e  se la variabile SubClass_C2_variabile_V2 è  diverso da  /*56,*/ 2 /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 non è  uguale a  /*53,*/ 131 e  se l'argomento argomento_ave2 è  uguale a RossoGialloxVerdex /*39,*/  /*36,*/ e  se il timer SubClass_C2_timer_T3 non è disattivo, Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio


 } Verifica che   /*49,50,51,52,*/  /*,*/  il timer SubClass_C2_timer_T3 non sia disattivo
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio
 /*104,*/ o  che   l'argomento argomento_ave2 sia  uguale a RossoGialloxVerdex /*,*/ 
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V7 sia  uguale a  /*53,*/ 7
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co4 sia  maggiore di  /*54,*/ 1550
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio


 } Verifica che   /*47,48,49,50,52,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  diverso da Verde
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da Verde
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T10 sia disattivo
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V2 sia  diverso da  /*56,*/ 10
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C2_controllo_C10 non sia  diverso da RossoGiallo
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  uguale a  False  /*,*/ 


 } Verifica che   /*49,52,*/   l'argomento argomento_ave7 non  sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T10 sia attivo


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co4 è  uguale a  /*53,*/ 1221""", [
                            DIBoolExpr("""Predicato Oggetto\nil ripristino del timer  SubClass_C2_restoreTI_TI1 è disattivo""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil contatore SubClass_C2_contatore_Co4 è  uguale a  /*53,*/ 1221""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*63,*/ /*35,*/  se il controllo SubClass_C2_controllo_C10 è  uguale a RossoGiallo e  se l'argomento argomento_ave3 non  è  uguale a  False  /*39,*/  /*37,*/ e  se la variabile SubClass_C2_variabile_V7 è  minore di  /*55,*/ 6 /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 non è  diverso da  /*56,*/ 11504 /*36,*/ o  se il timer SubClass_C2_timer_T3 è disattivo, Solo una delle seguenti { 
 /*63,*/ /*42,*/  se  MainClass_C1_controllo_C8 del campo  MainClass_C1 di SubClass_C2_lista_L8 è  uguale a c270x /*36,*/ o  se il timer SubClass_C2_timer_T3 non è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 è  minore di  /*55,*/ 12504 /*36,*/ o  se il timer SubClass_C2_timer_T3 è attivo, Solo una delle seguenti { 
 /*61,*/ /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P2 non è  uguale a Verde /*36,*/ o  se il timer SubClass_C2_timer_T3 non è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 è  diverso da  /*56,*/ 1332 /*37,*/ o  se la variabile SubClass_C2_variabile_V5 è  uguale a RossoGiallo e  se l'argomento argomento_ave4 non  è  uguale a  True  /*39,*/ , Tutte le seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T3 è disattivo /*34,*/ e  se il parametro SubClass_C2_parametro_P4 è  uguale a RossoGialloxVerdex /*37,*/ e  se la variabile SubClass_C2_variabile_V2 è  diverso da  /*56,*/ 2 /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 non è  uguale a  /*53,*/ 131 e  se l'argomento argomento_ave2 è  uguale a RossoGialloxVerdex /*39,*/  /*36,*/ e  se il timer SubClass_C2_timer_T3 non è disattivo, Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio


 } Verifica che   /*49,50,51,52,*/  /*,*/  il timer SubClass_C2_timer_T3 non sia disattivo
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio
 /*104,*/ o  che   l'argomento argomento_ave2 sia  uguale a RossoGialloxVerdex /*,*/ 
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V7 sia  uguale a  /*53,*/ 7
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co4 sia  maggiore di  /*54,*/ 1550
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio


 } Verifica che   /*47,48,49,50,52,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  diverso da Verde
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da Verde
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T10 sia disattivo
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V2 sia  diverso da  /*56,*/ 10
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C2_controllo_C10 non sia  diverso da RossoGiallo
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  uguale a  False  /*,*/ 


 } Verifica che   /*49,52,*/   l'argomento argomento_ave7 non  sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T10 sia attivo


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*35,*/  se il controllo SubClass_C2_controllo_C10 è  uguale a RossoGiallo e  se l'argomento argomento_ave3 non  è  uguale a  False  /*39,*/  /*37,*/ e  se la variabile SubClass_C2_variabile_V7 è  minore di  /*55,*/ 6 /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 non è  diverso da  /*56,*/ 11504 /*36,*/ o  se il timer SubClass_C2_timer_T3 è disattivo, Solo una delle seguenti { 
 /*63,*/ /*42,*/  se  MainClass_C1_controllo_C8 del campo  MainClass_C1 di SubClass_C2_lista_L8 è  uguale a c270x /*36,*/ o  se il timer SubClass_C2_timer_T3 non è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 è  minore di  /*55,*/ 12504 /*36,*/ o  se il timer SubClass_C2_timer_T3 è attivo, Solo una delle seguenti { 
 /*61,*/ /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P2 non è  uguale a Verde /*36,*/ o  se il timer SubClass_C2_timer_T3 non è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 è  diverso da  /*56,*/ 1332 /*37,*/ o  se la variabile SubClass_C2_variabile_V5 è  uguale a RossoGiallo e  se l'argomento argomento_ave4 non  è  uguale a  True  /*39,*/ , Tutte le seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T3 è disattivo /*34,*/ e  se il parametro SubClass_C2_parametro_P4 è  uguale a RossoGialloxVerdex /*37,*/ e  se la variabile SubClass_C2_variabile_V2 è  diverso da  /*56,*/ 2 /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 non è  uguale a  /*53,*/ 131 e  se l'argomento argomento_ave2 è  uguale a RossoGialloxVerdex /*39,*/  /*36,*/ e  se il timer SubClass_C2_timer_T3 non è disattivo, Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio


 } Verifica che   /*49,50,51,52,*/  /*,*/  il timer SubClass_C2_timer_T3 non sia disattivo
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio
 /*104,*/ o  che   l'argomento argomento_ave2 sia  uguale a RossoGialloxVerdex /*,*/ 
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V7 sia  uguale a  /*53,*/ 7
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co4 sia  maggiore di  /*54,*/ 1550
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio


 } Verifica che   /*47,48,49,50,52,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  diverso da Verde
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da Verde
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T10 sia disattivo
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V2 sia  diverso da  /*56,*/ 10
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C2_controllo_C10 non sia  diverso da RossoGiallo
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  uguale a  False  /*,*/ 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*35,*/  se il controllo SubClass_C2_controllo_C10 è  uguale a RossoGiallo e  se l'argomento argomento_ave3 non  è  uguale a  False  /*39,*/  /*37,*/ e  se la variabile SubClass_C2_variabile_V7 è  minore di  /*55,*/ 6 /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 non è  diverso da  /*56,*/ 11504 /*36,*/ o  se il timer SubClass_C2_timer_T3 è disattivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*35,*/  se il controllo SubClass_C2_controllo_C10 è  uguale a RossoGiallo e  se l'argomento argomento_ave3 non  è  uguale a  False  /*39,*/  /*37,*/ e  se la variabile SubClass_C2_variabile_V7 è  minore di  /*55,*/ 6 /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 non è  diverso da  /*56,*/ 11504""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*35,*/  se il controllo SubClass_C2_controllo_C10 è  uguale a RossoGiallo e  se l'argomento argomento_ave3 non  è  uguale a  False  /*39,*/  /*37,*/ e  se la variabile SubClass_C2_variabile_V7 è  minore di  /*55,*/ 6""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*35,*/  se il controllo SubClass_C2_controllo_C10 è  uguale a RossoGiallo e  se l'argomento argomento_ave3 non  è  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\nil controllo SubClass_C2_controllo_C10 è  uguale a RossoGiallo""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave3 non  è  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave3)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nla variabile SubClass_C2_variabile_V7 è  minore di  /*55,*/ 6""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co4 non è  diverso da  /*56,*/ 11504""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co4)  è uguale a  (11504))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co4)  è uguale a  (11504)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T3 è disattivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*63,*/ /*42,*/  se  MainClass_C1_controllo_C8 del campo  MainClass_C1 di SubClass_C2_lista_L8 è  uguale a c270x /*36,*/ o  se il timer SubClass_C2_timer_T3 non è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 è  minore di  /*55,*/ 12504 /*36,*/ o  se il timer SubClass_C2_timer_T3 è attivo, Solo una delle seguenti { 
 /*61,*/ /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P2 non è  uguale a Verde /*36,*/ o  se il timer SubClass_C2_timer_T3 non è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 è  diverso da  /*56,*/ 1332 /*37,*/ o  se la variabile SubClass_C2_variabile_V5 è  uguale a RossoGiallo e  se l'argomento argomento_ave4 non  è  uguale a  True  /*39,*/ , Tutte le seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T3 è disattivo /*34,*/ e  se il parametro SubClass_C2_parametro_P4 è  uguale a RossoGialloxVerdex /*37,*/ e  se la variabile SubClass_C2_variabile_V2 è  diverso da  /*56,*/ 2 /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 non è  uguale a  /*53,*/ 131 e  se l'argomento argomento_ave2 è  uguale a RossoGialloxVerdex /*39,*/  /*36,*/ e  se il timer SubClass_C2_timer_T3 non è disattivo, Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio


 } Verifica che   /*49,50,51,52,*/  /*,*/  il timer SubClass_C2_timer_T3 non sia disattivo
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio
 /*104,*/ o  che   l'argomento argomento_ave2 sia  uguale a RossoGialloxVerdex /*,*/ 
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V7 sia  uguale a  /*53,*/ 7
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co4 sia  maggiore di  /*54,*/ 1550
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio


 } Verifica che   /*47,48,49,50,52,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  diverso da Verde
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da Verde
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T10 sia disattivo
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V2 sia  diverso da  /*56,*/ 10
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C2_controllo_C10 non sia  diverso da RossoGiallo
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  uguale a  False  /*,*/ 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*42,*/  se  MainClass_C1_controllo_C8 del campo  MainClass_C1 di SubClass_C2_lista_L8 è  uguale a c270x /*36,*/ o  se il timer SubClass_C2_timer_T3 non è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 è  minore di  /*55,*/ 12504 /*36,*/ o  se il timer SubClass_C2_timer_T3 è attivo, Solo una delle seguenti { 
 /*61,*/ /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P2 non è  uguale a Verde /*36,*/ o  se il timer SubClass_C2_timer_T3 non è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 è  diverso da  /*56,*/ 1332 /*37,*/ o  se la variabile SubClass_C2_variabile_V5 è  uguale a RossoGiallo e  se l'argomento argomento_ave4 non  è  uguale a  True  /*39,*/ , Tutte le seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T3 è disattivo /*34,*/ e  se il parametro SubClass_C2_parametro_P4 è  uguale a RossoGialloxVerdex /*37,*/ e  se la variabile SubClass_C2_variabile_V2 è  diverso da  /*56,*/ 2 /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 non è  uguale a  /*53,*/ 131 e  se l'argomento argomento_ave2 è  uguale a RossoGialloxVerdex /*39,*/  /*36,*/ e  se il timer SubClass_C2_timer_T3 non è disattivo, Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio


 } Verifica che   /*49,50,51,52,*/  /*,*/  il timer SubClass_C2_timer_T3 non sia disattivo
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio
 /*104,*/ o  che   l'argomento argomento_ave2 sia  uguale a RossoGialloxVerdex /*,*/ 
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V7 sia  uguale a  /*53,*/ 7
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co4 sia  maggiore di  /*54,*/ 1550
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*42,*/  se  MainClass_C1_controllo_C8 del campo  MainClass_C1 di SubClass_C2_lista_L8 è  uguale a c270x /*36,*/ o  se il timer SubClass_C2_timer_T3 non è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 è  minore di  /*55,*/ 12504 /*36,*/ o  se il timer SubClass_C2_timer_T3 è attivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*42,*/  se  MainClass_C1_controllo_C8 del campo  MainClass_C1 di SubClass_C2_lista_L8 è  uguale a c270x /*36,*/ o  se il timer SubClass_C2_timer_T3 non è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 è  minore di  /*55,*/ 12504""", [
                            DIBoolExpr("""Predicato ForAll\nMainClass_C1_controllo_C8 del campo  MainClass_C1 di SubClass_C2_lista_L8 è  uguale a c270x""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c8 del campo mainclass_c1 della lista subclass_c2_lista_l8)  è uguale a  (c270x)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il timer SubClass_C2_timer_T3 non è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 è  minore di  /*55,*/ 12504""", [
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C2_timer_T3 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t3' è scaduto""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nil contatore SubClass_C2_contatore_Co4 è  minore di  /*55,*/ 12504""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T3 è attivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*61,*/ /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P2 non è  uguale a Verde /*36,*/ o  se il timer SubClass_C2_timer_T3 non è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 è  diverso da  /*56,*/ 1332 /*37,*/ o  se la variabile SubClass_C2_variabile_V5 è  uguale a RossoGiallo e  se l'argomento argomento_ave4 non  è  uguale a  True  /*39,*/ , Tutte le seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T3 è disattivo /*34,*/ e  se il parametro SubClass_C2_parametro_P4 è  uguale a RossoGialloxVerdex /*37,*/ e  se la variabile SubClass_C2_variabile_V2 è  diverso da  /*56,*/ 2 /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 non è  uguale a  /*53,*/ 131 e  se l'argomento argomento_ave2 è  uguale a RossoGialloxVerdex /*39,*/  /*36,*/ e  se il timer SubClass_C2_timer_T3 non è disattivo, Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio


 } Verifica che   /*49,50,51,52,*/  /*,*/  il timer SubClass_C2_timer_T3 non sia disattivo
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio
 /*104,*/ o  che   l'argomento argomento_ave2 sia  uguale a RossoGialloxVerdex /*,*/ 
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V7 sia  uguale a  /*53,*/ 7
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co4 sia  maggiore di  /*54,*/ 1550
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P2 non è  uguale a Verde /*36,*/ o  se il timer SubClass_C2_timer_T3 non è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 è  diverso da  /*56,*/ 1332 /*37,*/ o  se la variabile SubClass_C2_variabile_V5 è  uguale a RossoGiallo e  se l'argomento argomento_ave4 non  è  uguale a  True  /*39,*/ , Tutte le seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T3 è disattivo /*34,*/ e  se il parametro SubClass_C2_parametro_P4 è  uguale a RossoGialloxVerdex /*37,*/ e  se la variabile SubClass_C2_variabile_V2 è  diverso da  /*56,*/ 2 /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 non è  uguale a  /*53,*/ 131 e  se l'argomento argomento_ave2 è  uguale a RossoGialloxVerdex /*39,*/  /*36,*/ e  se il timer SubClass_C2_timer_T3 non è disattivo, Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P2 non è  uguale a Verde /*36,*/ o  se il timer SubClass_C2_timer_T3 non è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 è  diverso da  /*56,*/ 1332 /*37,*/ o  se la variabile SubClass_C2_variabile_V5 è  uguale a RossoGiallo e  se l'argomento argomento_ave4 non  è  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P2 non è  uguale a Verde /*36,*/ o  se il timer SubClass_C2_timer_T3 non è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 è  diverso da  /*56,*/ 1332""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P2 non è  uguale a Verde""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nMainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t6 del campo mainclass_c1 della lista subclass_c2_lista_l8' è attivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P2 non è  uguale a Verde""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p2)  è uguale a  (verde)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il timer SubClass_C2_timer_T3 non è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 è  diverso da  /*56,*/ 1332""", [
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C2_timer_T3 non è disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t3' è inattivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co4 è  diverso da  /*56,*/ 1332""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co4)  è uguale a  (1332)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse la variabile SubClass_C2_variabile_V5 è  uguale a RossoGiallo e  se l'argomento argomento_ave4 non  è  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\nla variabile SubClass_C2_variabile_V5 è  uguale a RossoGiallo""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave4 non  è  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave4)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*36,*/  se il timer SubClass_C2_timer_T3 è disattivo /*34,*/ e  se il parametro SubClass_C2_parametro_P4 è  uguale a RossoGialloxVerdex /*37,*/ e  se la variabile SubClass_C2_variabile_V2 è  diverso da  /*56,*/ 2 /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 non è  uguale a  /*53,*/ 131 e  se l'argomento argomento_ave2 è  uguale a RossoGialloxVerdex /*39,*/  /*36,*/ e  se il timer SubClass_C2_timer_T3 non è disattivo, Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*36,*/  se il timer SubClass_C2_timer_T3 è disattivo /*34,*/ e  se il parametro SubClass_C2_parametro_P4 è  uguale a RossoGialloxVerdex /*37,*/ e  se la variabile SubClass_C2_variabile_V2 è  diverso da  /*56,*/ 2 /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 non è  uguale a  /*53,*/ 131 e  se l'argomento argomento_ave2 è  uguale a RossoGialloxVerdex /*39,*/  /*36,*/ e  se il timer SubClass_C2_timer_T3 non è disattivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*36,*/  se il timer SubClass_C2_timer_T3 è disattivo /*34,*/ e  se il parametro SubClass_C2_parametro_P4 è  uguale a RossoGialloxVerdex /*37,*/ e  se la variabile SubClass_C2_variabile_V2 è  diverso da  /*56,*/ 2 /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 non è  uguale a  /*53,*/ 131 e  se l'argomento argomento_ave2 è  uguale a RossoGialloxVerdex""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*36,*/  se il timer SubClass_C2_timer_T3 è disattivo /*34,*/ e  se il parametro SubClass_C2_parametro_P4 è  uguale a RossoGialloxVerdex /*37,*/ e  se la variabile SubClass_C2_variabile_V2 è  diverso da  /*56,*/ 2 /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 non è  uguale a  /*53,*/ 131""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*36,*/  se il timer SubClass_C2_timer_T3 è disattivo /*34,*/ e  se il parametro SubClass_C2_parametro_P4 è  uguale a RossoGialloxVerdex /*37,*/ e  se la variabile SubClass_C2_variabile_V2 è  diverso da  /*56,*/ 2""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*36,*/  se il timer SubClass_C2_timer_T3 è disattivo /*34,*/ e  se il parametro SubClass_C2_parametro_P4 è  uguale a RossoGialloxVerdex""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T3 è disattivo""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil parametro SubClass_C2_parametro_P4 è  uguale a RossoGialloxVerdex""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V2 è  diverso da  /*56,*/ 2""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v2)  è uguale a  (2)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co4 non è  uguale a  /*53,*/ 131""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co4)  è uguale a  (131)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nl'argomento argomento_ave2 è  uguale a RossoGialloxVerdex""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C2_timer_T3 non è disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t3' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v8)  è uguale a  (avvio)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*49,50,51,52,*/  /*,*/  il timer SubClass_C2_timer_T3 non sia disattivo
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio
 /*104,*/ o  che   l'argomento argomento_ave2 sia  uguale a RossoGialloxVerdex /*,*/ 
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V7 sia  uguale a  /*53,*/ 7
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co4 sia  maggiore di  /*54,*/ 1550
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*49,50,51,52,*/  /*,*/  il timer SubClass_C2_timer_T3 non sia disattivo
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio
 /*104,*/ o  che   l'argomento argomento_ave2 sia  uguale a RossoGialloxVerdex /*,*/ 
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V7 sia  uguale a  /*53,*/ 7""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*49,50,51,52,*/  /*,*/  il timer SubClass_C2_timer_T3 non sia disattivo
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio
 /*104,*/ o  che   l'argomento argomento_ave2 sia  uguale a RossoGialloxVerdex""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*49,50,51,52,*/  /*,*/  il timer SubClass_C2_timer_T3 non sia disattivo
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*49,50,51,52,*/  /*,*/  il timer SubClass_C2_timer_T3 non sia disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t3' è inattivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v8)  è uguale a  (avvio)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   l'argomento argomento_ave2 sia  uguale a RossoGialloxVerdex""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*37,*/  la variabile SubClass_C2_variabile_V7 sia  uguale a  /*53,*/ 7""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il contatore SubClass_C2_contatore_Co4 sia  maggiore di  /*54,*/ 1550
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio""", [
                            DIBoolExpr("""GreaterThanImpl\nche  /*,*/  il contatore SubClass_C2_contatore_Co4 sia  maggiore di  /*54,*/ 1550""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*37,*/  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v8)  è uguale a  (avvio)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,50,52,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  diverso da Verde
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da Verde
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T10 sia disattivo
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V2 sia  diverso da  /*56,*/ 10
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C2_controllo_C10 non sia  diverso da RossoGiallo
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,50,52,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  diverso da Verde
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da Verde
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T10 sia disattivo
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V2 sia  diverso da  /*56,*/ 10""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,49,50,52,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  diverso da Verde
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da Verde
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T10 sia disattivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,49,50,52,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  diverso da Verde
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da Verde""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,49,50,52,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  diverso da Verde""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p2)  è uguale a  (verde)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da Verde""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c3)  è uguale a  (verde))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c3)  è uguale a  (verde)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer SubClass_C2_timer_T10 sia disattivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile SubClass_C2_variabile_V2 sia  diverso da  /*56,*/ 10""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v2)  è uguale a  (10)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*35,*/  il controllo SubClass_C2_controllo_C10 non sia  diverso da RossoGiallo
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  uguale a  False""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*35,*/  il controllo SubClass_C2_controllo_C10 non sia  diverso da RossoGiallo""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c10)  è uguale a  (rossogiallo))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c10)  è uguale a  (rossogiallo)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave4 non  sia  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave4)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*49,52,*/   l'argomento argomento_ave7 non  sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T10 sia attivo""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*49,52,*/   l'argomento argomento_ave7 non  sia  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave7)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer SubClass_C2_timer_T10 sia attivo""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,50,*/  /*,*/  il timer SubClass_C2_timer_T10 non sia disattivo
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  uguale a Verde
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  diverso da Verde
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T10 non sia disattivo
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V8 sia  diverso da avvio""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,49,50,*/  /*,*/  il timer SubClass_C2_timer_T10 non sia disattivo
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  uguale a Verde
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  diverso da Verde
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T10 non sia disattivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,49,50,*/  /*,*/  il timer SubClass_C2_timer_T10 non sia disattivo
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  uguale a Verde
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  diverso da Verde""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,49,50,*/  /*,*/  il timer SubClass_C2_timer_T10 non sia disattivo
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  uguale a Verde""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,49,50,*/  /*,*/  il timer SubClass_C2_timer_T10 non sia disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t10' è inattivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  uguale a Verde""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  diverso da Verde""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p2)  è uguale a  (verde))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p2)  è uguale a  (verde)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*36,*/  il timer SubClass_C2_timer_T10 non sia disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t10' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile SubClass_C2_variabile_V8 sia  diverso da avvio""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v8)  è uguale a  (avvio)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   /*52,*/   l'argomento argomento_ave4 non  sia  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave4)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*50,51,52,*/   l'argomento argomento_ave4 non  sia  uguale a  False  /*,*/ 
 /*104,*/ o  che   l'argomento argomento_ave4 sia  uguale a  True  /*39,*/ 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V2 sia  maggiore di  /*54,*/ 6
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co3 sia  uguale a  /*53,*/ 13""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*50,51,52,*/   l'argomento argomento_ave4 non  sia  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave4)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   l'argomento argomento_ave4 sia  uguale a  True  /*39,*/ 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V2 sia  maggiore di  /*54,*/ 6
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co3 sia  uguale a  /*53,*/ 13""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   l'argomento argomento_ave4 sia  uguale a  True  /*39,*/ 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V2 sia  maggiore di  /*54,*/ 6""", [
                            DIBoolExpr("""EqualImpl\nche   l'argomento argomento_ave4 sia  uguale a  True""", [
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nche  /*,*/  la variabile SubClass_C2_variabile_V2 sia  maggiore di  /*54,*/ 6""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  il contatore SubClass_C2_contatore_Co3 sia  uguale a  /*53,*/ 13""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroSubclass_c2_macrove_m6_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db(all(db(it.get_mainclass_c1().get_mainclass_c1_parametro_p3() == GlobalEnumeration.c270x, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l7())), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_controllo_c3() == GlobalEnumeration.verde, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db((db(self.get_subclass_c2_contatore_co3().get_valore() > 11504, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_variabile_v8() == GlobalEnumeration.avvio, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db((db((db((db(all(db(it.get_mainclass_c1().get_mainclass_c1_parametro_p3() == GlobalEnumeration.c270x, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l8())), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_parametro_p2() == GlobalEnumeration.verde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c2_parametro_p2() == GlobalEnumeration.verde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_controllo_c10() == GlobalEnumeration.rossogiallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_contatore_co3().get_valore() > 133, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db(self.get_subclass_c2_restoreti_ti1_restore().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_contatore_co4().get_valore() == 1221, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db((db((db((db((db(self.get_subclass_c2_controllo_c10() == GlobalEnumeration.rossogiallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(argomento_ave3 == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_variabile_v7() < 6, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c2_contatore_co4().get_valore() == 11504, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_timer_t3().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db((db((db(all(db(it.get_mainclass_c1().get_mainclass_c1_controllo_c8() == GlobalEnumeration.c270x, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l8())), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_timer_t3().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_contatore_co4().get_valore() < 12504, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_timer_t3().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db((db((db((db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_timer_t6().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l8())), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_parametro_p2() == GlobalEnumeration.verde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_timer_t3().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_contatore_co4().get_valore() == 1332, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(self.get_subclass_c2_variabile_v5() == GlobalEnumeration.rossogiallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(argomento_ave4 == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db((db((db((db((db((db(self.get_subclass_c2_timer_t3().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_parametro_p4() == GlobalEnumeration.rossogialloxverdex, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_variabile_v2() == 2, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_contatore_co4().get_valore() == 131, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(argomento_ave2 == GlobalEnumeration.rossogialloxverdex, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c2_timer_t3().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db(not db(self.get_subclass_c2_variabile_v8() == GlobalEnumeration.avvio, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db((db((db((db((db(not db(self.get_subclass_c2_timer_t3().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_variabile_v8() == GlobalEnumeration.avvio, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) or db(argomento_ave2 == GlobalEnumeration.rossogialloxverdex, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(self.get_subclass_c2_variabile_v7() == 7, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db((db(self.get_subclass_c2_contatore_co4().get_valore() > 1550, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(not db(self.get_subclass_c2_variabile_v8() == GlobalEnumeration.avvio, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db((db((db((db((db(not db(self.get_subclass_c2_parametro_p2() == GlobalEnumeration.verde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c2_controllo_c3() == GlobalEnumeration.verde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_timer_t10().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(not db(self.get_subclass_c2_variabile_v2() == 10, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db((db(not db(not db(self.get_subclass_c2_controllo_c10() == GlobalEnumeration.rossogiallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(not db(argomento_ave4 == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db((db(not db(argomento_ave7 == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) and db(self.get_subclass_c2_timer_t10().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db((db((db(not db(self.get_subclass_c2_timer_t10().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_parametro_p2() == GlobalEnumeration.verde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c2_parametro_p2() == GlobalEnumeration.verde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c2_timer_t10().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(not db(self.get_subclass_c2_variabile_v8() == GlobalEnumeration.avvio, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0]) or db(not db(argomento_ave4 == True, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db(not db(argomento_ave4 == False, di_ctx.subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0]) or db((db((db(argomento_ave4 == True, di_ctx.subs[0].subs[1].subs[1].subs[0].subs[0]) and db(self.get_subclass_c2_variabile_v2() > 6, di_ctx.subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[1].subs[0]) and db(self.get_subclass_c2_contatore_co3().get_valore() == 13, di_ctx.subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    @srf_value_macro("macroSubclass_c2_macrove_m8")
    def macroSubclass_c2_macrove_m8(self, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
         
        { commento: {63,}  se la macro  SubClass_C2_macrova_M1 ( con argomento_a2   uguale a avvio ,argomento_a8   uguale a RossoGiallo ,argomento_a6   uguale a Giallox ,argomento_a9   uguale a avvio ,argomento_a1   uguale a RossoGialloGiallo ,argomento_a5   uguale a GialloVerde  e argomento_a10   uguale a RossoGiallo )   è  diverso da avvio commento: {40,}  commento: {35,} o  se il controllo SubClass_C2_controllo_C3 è  diverso da Verde commento: {35,} e  se il controllo SubClass_C2_controllo_C10 non è  diverso da RossoGiallo, Solo una delle seguenti { 
         commento: {62,} commento: {34,}  se il parametro SubClass_C2_parametro_P2 è  uguale a Verde, Almeno una delle seguenti { 
         commento: {63,} commento: {38,}  se il contatore SubClass_C2_contatore_Co4 non è  diverso da  commento: {56,} 1121 commento: {37,} e  se la variabile SubClass_C2_variabile_V5 è  diverso da RossoGiallo, Solo una delle seguenti { 
         commento: {41,}  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  commento: {105,} è  uguale a c270x o  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro SubClass_C2_parametro_P4 non è  uguale a RossoGialloxVerdex commento: {37,} o  se la variabile SubClass_C2_variabile_V8 è  diverso da avvio commento: {34,} e  se il parametro SubClass_C2_parametro_P4 non è  uguale a RossoGialloxVerdex, Verifica che   commento: {47,48,50,}  commento: {34,}  il parametro SubClass_C2_parametro_P2 sia  diverso da Verde
         commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} e  che  commento: {,}  la variabile SubClass_C2_variabile_V5 non sia  uguale a RossoGiallo
        
        
         } Verifica che   commento: {48,49,50,51,}   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} o  che  commento: {,}  il controllo SubClass_C2_controllo_C10 sia  diverso da RossoGiallo
         commento: {104,} e  che  commento: {,}  il contatore SubClass_C2_contatore_Co4 non sia  uguale a  commento: {53,} 1232
         commento: {104,} e  che  commento: {38,}  il contatore SubClass_C2_contatore_Co3 sia  diverso da  commento: {56,} 12
         commento: {104,} o  che  commento: {,}  la variabile SubClass_C2_variabile_V7 sia  uguale a  commento: {53,} 3
         commento: {104,} e  che  commento: {,}  il timer SubClass_C2_timer_T3 sia scaduto
        
        
         } Verifica che   commento: {49,50,}  commento: {,}  il timer SubClass_C2_timer_T3 non sia disattivo
         commento: {104,} o  che  commento: {,}  la variabile SubClass_C2_variabile_V5 sia  uguale a RossoGiallo
        
        
         } Verifica che   commento: {47,48,49,50,}  commento: {,}  la variabile SubClass_C2_variabile_V8 sia  diverso da avvio
         commento: {104,} e  che  commento: {,}  il timer SubClass_C2_timer_T10 sia disattivo
         commento: {104,} e  che  commento: {37,}  la variabile SubClass_C2_variabile_V8 non sia  diverso da avvio
         commento: {104,} o  che  commento: {34,}  il parametro SubClass_C2_parametro_P2 non sia  uguale a Verde
         commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
        
        
        }
        """
        def populate_macroSubclass_c2_macrove_m8_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/  se la macro  SubClass_C2_macrova_M1 ( con argomento_a2   uguale a avvio ,argomento_a8   uguale a RossoGiallo ,argomento_a6   uguale a Giallox ,argomento_a9   uguale a avvio ,argomento_a1   uguale a RossoGialloGiallo ,argomento_a5   uguale a GialloVerde  e argomento_a10   uguale a RossoGiallo )   è  diverso da avvio /*40,*/  /*35,*/ o  se il controllo SubClass_C2_controllo_C3 è  diverso da Verde /*35,*/ e  se il controllo SubClass_C2_controllo_C10 non è  diverso da RossoGiallo, Solo una delle seguenti { 
 /*62,*/ /*34,*/  se il parametro SubClass_C2_parametro_P2 è  uguale a Verde, Almeno una delle seguenti { 
 /*63,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co4 non è  diverso da  /*56,*/ 1121 /*37,*/ e  se la variabile SubClass_C2_variabile_V5 è  diverso da RossoGiallo, Solo una delle seguenti { 
 /*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è  uguale a c270x o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P4 non è  uguale a RossoGialloxVerdex /*37,*/ o  se la variabile SubClass_C2_variabile_V8 è  diverso da avvio /*34,*/ e  se il parametro SubClass_C2_parametro_P4 non è  uguale a RossoGialloxVerdex, Verifica che   /*47,48,50,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  diverso da Verde
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V5 non sia  uguale a RossoGiallo


 } Verifica che   /*48,49,50,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C10 sia  diverso da RossoGiallo
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co4 non sia  uguale a  /*53,*/ 1232
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co3 sia  diverso da  /*56,*/ 12
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V7 sia  uguale a  /*53,*/ 3
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T3 sia scaduto


 } Verifica che   /*49,50,*/  /*,*/  il timer SubClass_C2_timer_T3 non sia disattivo
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V5 sia  uguale a RossoGiallo


 } Verifica che   /*47,48,49,50,*/  /*,*/  la variabile SubClass_C2_variabile_V8 sia  diverso da avvio
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T10 sia disattivo
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V8 non sia  diverso da avvio
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  uguale a Verde
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/  se la macro  SubClass_C2_macrova_M1 ( con argomento_a2   uguale a avvio ,argomento_a8   uguale a RossoGiallo ,argomento_a6   uguale a Giallox ,argomento_a9   uguale a avvio ,argomento_a1   uguale a RossoGialloGiallo ,argomento_a5   uguale a GialloVerde  e argomento_a10   uguale a RossoGiallo )   è  diverso da avvio /*40,*/  /*35,*/ o  se il controllo SubClass_C2_controllo_C3 è  diverso da Verde /*35,*/ e  se il controllo SubClass_C2_controllo_C10 non è  diverso da RossoGiallo, Solo una delle seguenti { 
 /*62,*/ /*34,*/  se il parametro SubClass_C2_parametro_P2 è  uguale a Verde, Almeno una delle seguenti { 
 /*63,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co4 non è  diverso da  /*56,*/ 1121 /*37,*/ e  se la variabile SubClass_C2_variabile_V5 è  diverso da RossoGiallo, Solo una delle seguenti { 
 /*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è  uguale a c270x o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P4 non è  uguale a RossoGialloxVerdex /*37,*/ o  se la variabile SubClass_C2_variabile_V8 è  diverso da avvio /*34,*/ e  se il parametro SubClass_C2_parametro_P4 non è  uguale a RossoGialloxVerdex, Verifica che   /*47,48,50,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  diverso da Verde
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V5 non sia  uguale a RossoGiallo


 } Verifica che   /*48,49,50,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C10 sia  diverso da RossoGiallo
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co4 non sia  uguale a  /*53,*/ 1232
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co3 sia  diverso da  /*56,*/ 12
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V7 sia  uguale a  /*53,*/ 3
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T3 sia scaduto


 } Verifica che   /*49,50,*/  /*,*/  il timer SubClass_C2_timer_T3 non sia disattivo
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V5 sia  uguale a RossoGiallo


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/  se la macro  SubClass_C2_macrova_M1 ( con argomento_a2   uguale a avvio ,argomento_a8   uguale a RossoGiallo ,argomento_a6   uguale a Giallox ,argomento_a9   uguale a avvio ,argomento_a1   uguale a RossoGialloGiallo ,argomento_a5   uguale a GialloVerde  e argomento_a10   uguale a RossoGiallo )   è  diverso da avvio /*40,*/  /*35,*/ o  se il controllo SubClass_C2_controllo_C3 è  diverso da Verde /*35,*/ e  se il controllo SubClass_C2_controllo_C10 non è  diverso da RossoGiallo""", [
                            DIBoolExpr("""Operatore Logico Not\nla macro  SubClass_C2_macrova_M1 ( con argomento_a2   uguale a avvio ,argomento_a8   uguale a RossoGiallo ,argomento_a6   uguale a Giallox ,argomento_a9   uguale a avvio ,argomento_a1   uguale a RossoGialloGiallo ,argomento_a5   uguale a GialloVerde  e argomento_a10   uguale a RossoGiallo )   è  diverso da avvio""", [
                            DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroSubclass_c2_macrova_m1')  è uguale a  (avvio)""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroSubclass_c2_macrova_m1'"""),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo SubClass_C2_controllo_C3 è  diverso da Verde /*35,*/ e  se il controllo SubClass_C2_controllo_C10 non è  diverso da RossoGiallo""", [
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C3 è  diverso da Verde""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c3)  è uguale a  (verde)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C10 non è  diverso da RossoGiallo""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c10)  è uguale a  (rossogiallo))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c10)  è uguale a  (rossogiallo)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*62,*/ /*34,*/  se il parametro SubClass_C2_parametro_P2 è  uguale a Verde, Almeno una delle seguenti { 
 /*63,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co4 non è  diverso da  /*56,*/ 1121 /*37,*/ e  se la variabile SubClass_C2_variabile_V5 è  diverso da RossoGiallo, Solo una delle seguenti { 
 /*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è  uguale a c270x o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P4 non è  uguale a RossoGialloxVerdex /*37,*/ o  se la variabile SubClass_C2_variabile_V8 è  diverso da avvio /*34,*/ e  se il parametro SubClass_C2_parametro_P4 non è  uguale a RossoGialloxVerdex, Verifica che   /*47,48,50,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  diverso da Verde
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V5 non sia  uguale a RossoGiallo


 } Verifica che   /*48,49,50,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C10 sia  diverso da RossoGiallo
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co4 non sia  uguale a  /*53,*/ 1232
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co3 sia  diverso da  /*56,*/ 12
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V7 sia  uguale a  /*53,*/ 3
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T3 sia scaduto


 } Verifica che   /*49,50,*/  /*,*/  il timer SubClass_C2_timer_T3 non sia disattivo
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V5 sia  uguale a RossoGiallo


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*34,*/  se il parametro SubClass_C2_parametro_P2 è  uguale a Verde, Almeno una delle seguenti { 
 /*63,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co4 non è  diverso da  /*56,*/ 1121 /*37,*/ e  se la variabile SubClass_C2_variabile_V5 è  diverso da RossoGiallo, Solo una delle seguenti { 
 /*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è  uguale a c270x o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P4 non è  uguale a RossoGialloxVerdex /*37,*/ o  se la variabile SubClass_C2_variabile_V8 è  diverso da avvio /*34,*/ e  se il parametro SubClass_C2_parametro_P4 non è  uguale a RossoGialloxVerdex, Verifica che   /*47,48,50,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  diverso da Verde
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V5 non sia  uguale a RossoGiallo


 } Verifica che   /*48,49,50,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C10 sia  diverso da RossoGiallo
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co4 non sia  uguale a  /*53,*/ 1232
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co3 sia  diverso da  /*56,*/ 12
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V7 sia  uguale a  /*53,*/ 3
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T3 sia scaduto


 }""", [
                            DIBoolExpr("""EqualImpl\nil parametro SubClass_C2_parametro_P2 è  uguale a Verde""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*63,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co4 non è  diverso da  /*56,*/ 1121 /*37,*/ e  se la variabile SubClass_C2_variabile_V5 è  diverso da RossoGiallo, Solo una delle seguenti { 
 /*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è  uguale a c270x o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P4 non è  uguale a RossoGialloxVerdex /*37,*/ o  se la variabile SubClass_C2_variabile_V8 è  diverso da avvio /*34,*/ e  se il parametro SubClass_C2_parametro_P4 non è  uguale a RossoGialloxVerdex, Verifica che   /*47,48,50,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  diverso da Verde
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V5 non sia  uguale a RossoGiallo


 } Verifica che   /*48,49,50,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C10 sia  diverso da RossoGiallo
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co4 non sia  uguale a  /*53,*/ 1232
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co3 sia  diverso da  /*56,*/ 12
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V7 sia  uguale a  /*53,*/ 3
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T3 sia scaduto


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co4 non è  diverso da  /*56,*/ 1121 /*37,*/ e  se la variabile SubClass_C2_variabile_V5 è  diverso da RossoGiallo, Solo una delle seguenti { 
 /*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è  uguale a c270x o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P4 non è  uguale a RossoGialloxVerdex /*37,*/ o  se la variabile SubClass_C2_variabile_V8 è  diverso da avvio /*34,*/ e  se il parametro SubClass_C2_parametro_P4 non è  uguale a RossoGialloxVerdex, Verifica che   /*47,48,50,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  diverso da Verde
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V5 non sia  uguale a RossoGiallo


 }""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co4 non è  diverso da  /*56,*/ 1121 /*37,*/ e  se la variabile SubClass_C2_variabile_V5 è  diverso da RossoGiallo""", [
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co4 non è  diverso da  /*56,*/ 1121""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co4)  è uguale a  (1121))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co4)  è uguale a  (1121)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V5 è  diverso da RossoGiallo""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v5)  è uguale a  (rossogiallo)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è  uguale a c270x o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P4 non è  uguale a RossoGialloxVerdex /*37,*/ o  se la variabile SubClass_C2_variabile_V8 è  diverso da avvio /*34,*/ e  se il parametro SubClass_C2_parametro_P4 non è  uguale a RossoGialloxVerdex, Verifica che   /*47,48,50,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  diverso da Verde
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V5 non sia  uguale a RossoGiallo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è  uguale a c270x o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P4 non è  uguale a RossoGialloxVerdex /*37,*/ o  se la variabile SubClass_C2_variabile_V8 è  diverso da avvio /*34,*/ e  se il parametro SubClass_C2_parametro_P4 non è  uguale a RossoGialloxVerdex""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è  uguale a c270x o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P4 non è  uguale a RossoGialloxVerdex""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nMainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è  uguale a c270x""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3 del campo mainclass_c1 della lista subclass_c2_lista_l8)  è uguale a  (c270x)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P4 non è  uguale a RossoGialloxVerdex""", [
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P4 non è  uguale a RossoGialloxVerdex""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p4)  è uguale a  (rossogialloxverdex)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse la variabile SubClass_C2_variabile_V8 è  diverso da avvio /*34,*/ e  se il parametro SubClass_C2_parametro_P4 non è  uguale a RossoGialloxVerdex""", [
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V8 è  diverso da avvio""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v8)  è uguale a  (avvio)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P4 non è  uguale a RossoGialloxVerdex""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p4)  è uguale a  (rossogialloxverdex)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  diverso da Verde
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V5 non sia  uguale a RossoGiallo""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,50,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  diverso da Verde""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p2)  è uguale a  (verde)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V5 non sia  uguale a RossoGiallo""", [
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile SubClass_C2_variabile_V5 non sia  uguale a RossoGiallo""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v5)  è uguale a  (rossogiallo)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,50,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C10 sia  diverso da RossoGiallo
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co4 non sia  uguale a  /*53,*/ 1232
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co3 sia  diverso da  /*56,*/ 12
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V7 sia  uguale a  /*53,*/ 3
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T3 sia scaduto""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,50,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C10 sia  diverso da RossoGiallo
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co4 non sia  uguale a  /*53,*/ 1232
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co3 sia  diverso da  /*56,*/ 12""", [
                            DIBoolExpr("""EqualImpl\nche   /*48,49,50,51,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il controllo SubClass_C2_controllo_C10 sia  diverso da RossoGiallo
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co4 non sia  uguale a  /*53,*/ 1232
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co3 sia  diverso da  /*56,*/ 12""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il controllo SubClass_C2_controllo_C10 sia  diverso da RossoGiallo
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co4 non sia  uguale a  /*53,*/ 1232""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo SubClass_C2_controllo_C10 sia  diverso da RossoGiallo""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c10)  è uguale a  (rossogiallo)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore SubClass_C2_contatore_Co4 non sia  uguale a  /*53,*/ 1232""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co4)  è uguale a  (1232)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*38,*/  il contatore SubClass_C2_contatore_Co3 sia  diverso da  /*56,*/ 12""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co3)  è uguale a  (12)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  la variabile SubClass_C2_variabile_V7 sia  uguale a  /*53,*/ 3
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T3 sia scaduto""", [
                            DIBoolExpr("""EqualImpl\nche  /*,*/  la variabile SubClass_C2_variabile_V7 sia  uguale a  /*53,*/ 3""", [
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer SubClass_C2_timer_T3 sia scaduto""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*49,50,*/  /*,*/  il timer SubClass_C2_timer_T3 non sia disattivo
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V5 sia  uguale a RossoGiallo""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*49,50,*/  /*,*/  il timer SubClass_C2_timer_T3 non sia disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t3' è inattivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  la variabile SubClass_C2_variabile_V5 sia  uguale a RossoGiallo""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,50,*/  /*,*/  la variabile SubClass_C2_variabile_V8 sia  diverso da avvio
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T10 sia disattivo
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V8 non sia  diverso da avvio
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  uguale a Verde
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,50,*/  /*,*/  la variabile SubClass_C2_variabile_V8 sia  diverso da avvio
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T10 sia disattivo
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V8 non sia  diverso da avvio
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  uguale a Verde""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,49,50,*/  /*,*/  la variabile SubClass_C2_variabile_V8 sia  diverso da avvio
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T10 sia disattivo
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V8 non sia  diverso da avvio""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,49,50,*/  /*,*/  la variabile SubClass_C2_variabile_V8 sia  diverso da avvio
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T10 sia disattivo""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,49,50,*/  /*,*/  la variabile SubClass_C2_variabile_V8 sia  diverso da avvio""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v8)  è uguale a  (avvio)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer SubClass_C2_timer_T10 sia disattivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*37,*/  la variabile SubClass_C2_variabile_V8 non sia  diverso da avvio""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v8)  è uguale a  (avvio))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v8)  è uguale a  (avvio)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  uguale a Verde""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p2)  è uguale a  (verde)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroSubclass_c2_macrove_m8_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db(not db(db(self.macroSubclass_c2_macrova_m1(GlobalEnumeration.rossogiallogiallo,GlobalEnumeration.rossogiallo,GlobalEnumeration.avvio,GlobalEnumeration.gialloverde,GlobalEnumeration.giallox,GlobalEnumeration.rossogiallo,GlobalEnumeration.avvio, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) == GlobalEnumeration.avvio, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_controllo_c3() == GlobalEnumeration.verde, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_subclass_c2_controllo_c10() == GlobalEnumeration.rossogiallo, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((((db(not db(self.get_subclass_c2_parametro_p2() == GlobalEnumeration.verde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db(not db(not db(self.get_subclass_c2_contatore_co4().get_valore() == 1121, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_variabile_v5() == GlobalEnumeration.rossogiallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db((db((db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_parametro_p3() == GlobalEnumeration.c270x, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l8())), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_parametro_p4() == GlobalEnumeration.rossogialloxverdex, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_variabile_v8() == GlobalEnumeration.avvio, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_parametro_p4() == GlobalEnumeration.rossogialloxverdex, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db(not db(self.get_subclass_c2_parametro_p2() == GlobalEnumeration.verde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(not db(self.get_subclass_c2_variabile_v5() == GlobalEnumeration.rossogiallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db((db((db(not db(self.get_subclass_c2_controllo_c10() == GlobalEnumeration.rossogiallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c2_contatore_co4().get_valore() == 1232, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_contatore_co3().get_valore() == 12, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db((db(self.get_subclass_c2_variabile_v7() == 3, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(self.get_subclass_c2_timer_t3().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0])) + (db((db(not db(self.get_subclass_c2_timer_t3().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) or db(self.get_subclass_c2_variabile_v5() == GlobalEnumeration.rossogiallo, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db((db((db((db(not db(self.get_subclass_c2_variabile_v8() == GlobalEnumeration.avvio, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_timer_t10().isDisattivato(), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c2_variabile_v8() == GlobalEnumeration.avvio, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[0]) or db(not db(self.get_subclass_c2_parametro_p2() == GlobalEnumeration.verde, di_ctx.subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    @srf_value_macro("macroSubclass_c2_macrove_m9")
    def macroSubclass_c2_macrove_m9(self, argomento_ave10, argomento_ave2, argomento_ave3, argomento_ave4, argomento_ave7, argomento_ave8, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        { commento: {63,} commento: {38,}  se il contatore SubClass_C2_contatore_Co3 è  minore di  commento: {55,} 1150 o  se l'argomento argomento_ave2 non  è  diverso da  False  commento: {39,} , Solo una delle seguenti { 
         commento: {62,} commento: {43,}  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  commento: {105,} è disattivo commento: {38,} o  se il contatore SubClass_C2_contatore_Co4 non è  minore di  commento: {55,} 1243 commento: {35,} o  se il controllo SubClass_C2_controllo_C3 è  uguale a Verde commento: {34,} o  se il parametro SubClass_C2_parametro_P4 è  diverso da RossoGialloxVerdex commento: {36,} e  se il timer SubClass_C2_timer_T3 è disattivo, Almeno una delle seguenti { 
         commento: {38,}  se il contatore SubClass_C2_contatore_Co4 è  minore di  commento: {55,} 13215 commento: {38,} e  se il contatore SubClass_C2_contatore_Co4 è  uguale a  commento: {53,} 1504 commento: {37,} e  se la variabile SubClass_C2_variabile_V2 è  maggiore di  commento: {54,} 6, Verifica che   commento: {47,48,}  commento: {,}  il controllo SubClass_C2_controllo_C3 non sia  uguale a Verde
         commento: {104,} e  che  commento: {34,}  il parametro SubClass_C2_parametro_P1 sia  uguale a RossoGialloxVerdex
        
        
         } Verifica che   commento: {47,49,50,52,}  commento: {,}  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio
         commento: {104,} e  che   l'argomento argomento_ave10 non  sia  uguale a  False  commento: {,} 
         commento: {104,} o  che  commento: {37,}  la variabile SubClass_C2_variabile_V8 sia  diverso da avvio
         commento: {104,} o  che   l'argomento argomento_ave4 sia  uguale a  False  commento: {39,} 
         commento: {104,} o  che  commento: {34,}  il parametro SubClass_C2_parametro_P2 non sia  uguale a Verde
         commento: {104,} o  che  commento: {,}  il timer SubClass_C2_timer_T10 non sia scaduto
        
        
         } Verifica che   commento: {47,49,50,51,52,}  commento: {,}  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio
         commento: {104,} e  che  commento: {,}  il contatore SubClass_C2_contatore_Co4 non sia  diverso da  commento: {56,} 12
         commento: {104,} o  che  commento: {34,}  il parametro SubClass_C2_parametro_P10 sia  uguale a  True 
         commento: {104,} e  che  commento: {38,}  il contatore SubClass_C2_contatore_Co4 non sia  diverso da  commento: {56,} 13
         commento: {104,} o  che  commento: {,}  il timer SubClass_C2_timer_T3 non sia attivo
         commento: {104,} o  che   l'argomento argomento_ave7 non  sia  uguale a  True  commento: {,} 
        
        
        }
        """
        def populate_macroSubclass_c2_macrove_m9_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co3 è  minore di  /*55,*/ 1150 o  se l'argomento argomento_ave2 non  è  diverso da  False  /*39,*/ , Solo una delle seguenti { 
 /*62,*/ /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co4 non è  minore di  /*55,*/ 1243 /*35,*/ o  se il controllo SubClass_C2_controllo_C3 è  uguale a Verde /*34,*/ o  se il parametro SubClass_C2_parametro_P4 è  diverso da RossoGialloxVerdex /*36,*/ e  se il timer SubClass_C2_timer_T3 è disattivo, Almeno una delle seguenti { 
 /*38,*/  se il contatore SubClass_C2_contatore_Co4 è  minore di  /*55,*/ 13215 /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 è  uguale a  /*53,*/ 1504 /*37,*/ e  se la variabile SubClass_C2_variabile_V2 è  maggiore di  /*54,*/ 6, Verifica che   /*47,48,*/  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  uguale a Verde
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P1 sia  uguale a RossoGialloxVerdex


 } Verifica che   /*47,49,50,52,*/  /*,*/  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio
 /*104,*/ e  che   l'argomento argomento_ave10 non  sia  uguale a  False  /*,*/ 
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V8 sia  diverso da avvio
 /*104,*/ o  che   l'argomento argomento_ave4 sia  uguale a  False  /*39,*/ 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  uguale a Verde
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T10 non sia scaduto


 } Verifica che   /*47,49,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co4 non sia  diverso da  /*56,*/ 12
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P10 sia  uguale a  True 
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co4 non sia  diverso da  /*56,*/ 13
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T3 non sia attivo
 /*104,*/ o  che   l'argomento argomento_ave7 non  sia  uguale a  True""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co3 è  minore di  /*55,*/ 1150 o  se l'argomento argomento_ave2 non  è  diverso da  False  /*39,*/ , Solo una delle seguenti { 
 /*62,*/ /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co4 non è  minore di  /*55,*/ 1243 /*35,*/ o  se il controllo SubClass_C2_controllo_C3 è  uguale a Verde /*34,*/ o  se il parametro SubClass_C2_parametro_P4 è  diverso da RossoGialloxVerdex /*36,*/ e  se il timer SubClass_C2_timer_T3 è disattivo, Almeno una delle seguenti { 
 /*38,*/  se il contatore SubClass_C2_contatore_Co4 è  minore di  /*55,*/ 13215 /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 è  uguale a  /*53,*/ 1504 /*37,*/ e  se la variabile SubClass_C2_variabile_V2 è  maggiore di  /*54,*/ 6, Verifica che   /*47,48,*/  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  uguale a Verde
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P1 sia  uguale a RossoGialloxVerdex


 } Verifica che   /*47,49,50,52,*/  /*,*/  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio
 /*104,*/ e  che   l'argomento argomento_ave10 non  sia  uguale a  False  /*,*/ 
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V8 sia  diverso da avvio
 /*104,*/ o  che   l'argomento argomento_ave4 sia  uguale a  False  /*39,*/ 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  uguale a Verde
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T10 non sia scaduto


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co3 è  minore di  /*55,*/ 1150 o  se l'argomento argomento_ave2 non  è  diverso da  False""", [
                            DIBoolExpr("""LessThanImpl\nil contatore SubClass_C2_contatore_Co3 è  minore di  /*55,*/ 1150""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave2 non  è  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_ave2)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave2)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*62,*/ /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co4 non è  minore di  /*55,*/ 1243 /*35,*/ o  se il controllo SubClass_C2_controllo_C3 è  uguale a Verde /*34,*/ o  se il parametro SubClass_C2_parametro_P4 è  diverso da RossoGialloxVerdex /*36,*/ e  se il timer SubClass_C2_timer_T3 è disattivo, Almeno una delle seguenti { 
 /*38,*/  se il contatore SubClass_C2_contatore_Co4 è  minore di  /*55,*/ 13215 /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 è  uguale a  /*53,*/ 1504 /*37,*/ e  se la variabile SubClass_C2_variabile_V2 è  maggiore di  /*54,*/ 6, Verifica che   /*47,48,*/  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  uguale a Verde
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P1 sia  uguale a RossoGialloxVerdex


 } Verifica che   /*47,49,50,52,*/  /*,*/  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio
 /*104,*/ e  che   l'argomento argomento_ave10 non  sia  uguale a  False  /*,*/ 
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V8 sia  diverso da avvio
 /*104,*/ o  che   l'argomento argomento_ave4 sia  uguale a  False  /*39,*/ 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  uguale a Verde
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T10 non sia scaduto


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co4 non è  minore di  /*55,*/ 1243 /*35,*/ o  se il controllo SubClass_C2_controllo_C3 è  uguale a Verde /*34,*/ o  se il parametro SubClass_C2_parametro_P4 è  diverso da RossoGialloxVerdex /*36,*/ e  se il timer SubClass_C2_timer_T3 è disattivo, Almeno una delle seguenti { 
 /*38,*/  se il contatore SubClass_C2_contatore_Co4 è  minore di  /*55,*/ 13215 /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 è  uguale a  /*53,*/ 1504 /*37,*/ e  se la variabile SubClass_C2_variabile_V2 è  maggiore di  /*54,*/ 6, Verifica che   /*47,48,*/  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  uguale a Verde
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P1 sia  uguale a RossoGialloxVerdex


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co4 non è  minore di  /*55,*/ 1243 /*35,*/ o  se il controllo SubClass_C2_controllo_C3 è  uguale a Verde /*34,*/ o  se il parametro SubClass_C2_parametro_P4 è  diverso da RossoGialloxVerdex /*36,*/ e  se il timer SubClass_C2_timer_T3 è disattivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co4 non è  minore di  /*55,*/ 1243 /*35,*/ o  se il controllo SubClass_C2_controllo_C3 è  uguale a Verde""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co4 non è  minore di  /*55,*/ 1243""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nMainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t6 del campo mainclass_c1 della lista subclass_c2_lista_l8' è inattivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co4 non è  minore di  /*55,*/ 1243""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_contatore_co4)  è minore di  (1243)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo SubClass_C2_controllo_C3 è  uguale a Verde""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il parametro SubClass_C2_parametro_P4 è  diverso da RossoGialloxVerdex /*36,*/ e  se il timer SubClass_C2_timer_T3 è disattivo""", [
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P4 è  diverso da RossoGialloxVerdex""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p4)  è uguale a  (rossogialloxverdex)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T3 è disattivo""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*38,*/  se il contatore SubClass_C2_contatore_Co4 è  minore di  /*55,*/ 13215 /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 è  uguale a  /*53,*/ 1504 /*37,*/ e  se la variabile SubClass_C2_variabile_V2 è  maggiore di  /*54,*/ 6, Verifica che   /*47,48,*/  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  uguale a Verde
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P1 sia  uguale a RossoGialloxVerdex""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*38,*/  se il contatore SubClass_C2_contatore_Co4 è  minore di  /*55,*/ 13215 /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 è  uguale a  /*53,*/ 1504 /*37,*/ e  se la variabile SubClass_C2_variabile_V2 è  maggiore di  /*54,*/ 6""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*38,*/  se il contatore SubClass_C2_contatore_Co4 è  minore di  /*55,*/ 13215 /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 è  uguale a  /*53,*/ 1504""", [
                            DIBoolExpr("""LessThanImpl\nil contatore SubClass_C2_contatore_Co4 è  minore di  /*55,*/ 13215""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil contatore SubClass_C2_contatore_Co4 è  uguale a  /*53,*/ 1504""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nla variabile SubClass_C2_variabile_V2 è  maggiore di  /*54,*/ 6""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,*/  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  uguale a Verde
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P1 sia  uguale a RossoGialloxVerdex""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,*/  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  uguale a Verde""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c3)  è uguale a  (verde)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*34,*/  il parametro SubClass_C2_parametro_P1 sia  uguale a RossoGialloxVerdex""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,50,52,*/  /*,*/  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio
 /*104,*/ e  che   l'argomento argomento_ave10 non  sia  uguale a  False  /*,*/ 
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V8 sia  diverso da avvio
 /*104,*/ o  che   l'argomento argomento_ave4 sia  uguale a  False  /*39,*/ 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  uguale a Verde
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T10 non sia scaduto""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,50,52,*/  /*,*/  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio
 /*104,*/ e  che   l'argomento argomento_ave10 non  sia  uguale a  False  /*,*/ 
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V8 sia  diverso da avvio
 /*104,*/ o  che   l'argomento argomento_ave4 sia  uguale a  False  /*39,*/ 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  uguale a Verde""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,50,52,*/  /*,*/  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio
 /*104,*/ e  che   l'argomento argomento_ave10 non  sia  uguale a  False  /*,*/ 
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V8 sia  diverso da avvio
 /*104,*/ o  che   l'argomento argomento_ave4 sia  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,50,52,*/  /*,*/  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio
 /*104,*/ e  che   l'argomento argomento_ave10 non  sia  uguale a  False  /*,*/ 
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V8 sia  diverso da avvio""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,49,50,52,*/  /*,*/  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio
 /*104,*/ e  che   l'argomento argomento_ave10 non  sia  uguale a  False""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,49,50,52,*/  /*,*/  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v8)  è uguale a  (avvio)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave10 non  sia  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave10)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*37,*/  la variabile SubClass_C2_variabile_V8 sia  diverso da avvio""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v8)  è uguale a  (avvio)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   l'argomento argomento_ave4 sia  uguale a  False""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  uguale a Verde""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p2)  è uguale a  (verde)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il timer SubClass_C2_timer_T10 non sia scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t10' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co4 non sia  diverso da  /*56,*/ 12
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P10 sia  uguale a  True 
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co4 non sia  diverso da  /*56,*/ 13
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T3 non sia attivo
 /*104,*/ o  che   l'argomento argomento_ave7 non  sia  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co4 non sia  diverso da  /*56,*/ 12
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P10 sia  uguale a  True 
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co4 non sia  diverso da  /*56,*/ 13
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T3 non sia attivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co4 non sia  diverso da  /*56,*/ 12
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P10 sia  uguale a  True 
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co4 non sia  diverso da  /*56,*/ 13""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,49,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co4 non sia  diverso da  /*56,*/ 12""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,49,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V8 non sia  uguale a avvio""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v8)  è uguale a  (avvio)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore SubClass_C2_contatore_Co4 non sia  diverso da  /*56,*/ 12""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co4)  è uguale a  (12))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co4)  è uguale a  (12)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*34,*/  il parametro SubClass_C2_parametro_P10 sia  uguale a  True 
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co4 non sia  diverso da  /*56,*/ 13""", [
                            DIBoolExpr("""EqualImpl\nche  /*34,*/  il parametro SubClass_C2_parametro_P10 sia  uguale a  True""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*38,*/  il contatore SubClass_C2_contatore_Co4 non sia  diverso da  /*56,*/ 13""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co4)  è uguale a  (13))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co4)  è uguale a  (13)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il timer SubClass_C2_timer_T3 non sia attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t3' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave7 non  sia  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave7)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroSubclass_c2_macrove_m9_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db(self.get_subclass_c2_contatore_co3().get_valore() < 1150, di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(not db(not db(argomento_ave2 == False, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((((db(not db((db((db((db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_timer_t6().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l8())), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_contatore_co4().get_valore() < 1243, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_controllo_c3() == GlobalEnumeration.verde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_parametro_p4() == GlobalEnumeration.rossogialloxverdex, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_timer_t3().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db(not db((db((db(self.get_subclass_c2_contatore_co4().get_valore() < 13215, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_contatore_co4().get_valore() == 1504, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) and db(self.get_subclass_c2_variabile_v2() > 6, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db(not db(self.get_subclass_c2_controllo_c3() == GlobalEnumeration.verde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) and db(self.get_subclass_c2_parametro_p1() == GlobalEnumeration.rossogialloxverdex, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0])) + (db((db((db((db((db((db(not db(self.get_subclass_c2_variabile_v8() == GlobalEnumeration.avvio, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(argomento_ave10 == False, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_variabile_v8() == GlobalEnumeration.avvio, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) or db(argomento_ave4 == False, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(not db(self.get_subclass_c2_parametro_p2() == GlobalEnumeration.verde, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) or db(not db(self.get_subclass_c2_timer_t10().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db((db((db((db(not db(self.get_subclass_c2_variabile_v8() == GlobalEnumeration.avvio, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c2_contatore_co4().get_valore() == 12, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(self.get_subclass_c2_parametro_p10() == True, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_subclass_c2_contatore_co4().get_valore() == 13, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[0]) or db(not db(self.get_subclass_c2_timer_t3().isAttivato(), di_ctx.subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0]) or db(not db(argomento_ave7 == True, di_ctx.subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    # value macros
    @srf_value_macro("macroSubclass_c2_macrova_m1")
    def macroSubclass_c2_macrova_m1(self, argomento_a1, argomento_a10, argomento_a2, argomento_a5, argomento_a6, argomento_a8, argomento_a9, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}  se l'argomento argomento_a8 non  è  uguale a RossoGiallo commento: {39,}  , assegna alla macro il valore avvio
        
         commento: {46,} assegna alla macro il valore avvio commento: {],}
        }
        """
        def populate_macroSubclass_c2_macrova_m1_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/  se l'argomento argomento_a8 non  è  uguale a RossoGiallo /*39,*/  , assegna alla macro il valore avvio""", [
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_a8 non  è  uguale a RossoGiallo""", [
                            DIBoolExpr("""EqualImpl\n(argomento_a8)  è uguale a  (rossogiallo)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                ])

        populate_macroSubclass_c2_macrova_m1_SrfMacroDefInfo(di_ctx)
        #  /*[*/  se l'argomento argomento_a8 non  è  uguale a RossoGiallo /*39,*/  , assegna alla macro il valore avvio
        if db(not db(argomento_a8 == GlobalEnumeration.rossogiallo, di_ctx.subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0]):
            return GlobalEnumeration.avvio
        #  /*46,*/ assegna alla macro il valore avvio
        return GlobalEnumeration.avvio
    
    @srf_value_macro("macroSubclass_c2_macrova_m10")
    def macroSubclass_c2_macrova_m10(self, argomento_a2, argomento_a3, argomento_a4, argomento_a6, argomento_a7, argomento_a8, argomento_a9, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}
         commento: {46,} assegna alla macro il valore Verde commento: {],}
        }
        """
        def populate_macroSubclass_c2_macrova_m10_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                ])

        populate_macroSubclass_c2_macrova_m10_SrfMacroDefInfo(di_ctx)
        
        #  /*[*/
        #   /*46,*/ assegna alla macro il valore Verde
        return GlobalEnumeration.verde
    
    # for each manual command, the corresponding method is created
    def eventSubclass_c2_command_comm1DaSendercda7890b(self, notifying_process):
        notifying_process.response_notify_man_cmd(self, 'eventSubclass_c2_command_comm1DaSendercda7890b')
    
    def eventSubclass_c2_command_comm2(self, notifying_process):
        notifying_process.response_notify_man_cmd(self, 'eventSubclass_c2_command_comm2')
    
    def eventSubclass_c2_command_comm5DaSender94b948c6(self, notifying_process):
        notifying_process.response_notify_man_cmd(self, 'eventSubclass_c2_command_comm5DaSender94b948c6')
    
    def eventSubclass_c2_command_comm9(self, notifying_process):
        notifying_process.response_notify_man_cmd(self, 'eventSubclass_c2_command_comm9')
    
    # for each automatic command, the corresponding method is created

    def update_precedente(self):
        # update the variables with previous value
        self.set_subclass_c2_previousco_c1_prev(self.get_subclass_c2_previousco_c1())
        self.set_subclass_c2_previousco_c5_prev(self.get_subclass_c2_previousco_c5())
        self.set_subclass_c2_previousco_c7_prev(self.get_subclass_c2_previousco_c7())
        self.set_subclass_c2_previousco_c8_prev(self.get_subclass_c2_previousco_c8())
        self.set_subclass_c2_previousco_c9_prev(self.get_subclass_c2_previousco_c9())
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
    def init_configuration(self, mainclass_c1, recordfiled5, recordfiled4, recordfiled9):
        self.set_mainclass_c1(mainclass_c1)
        self.set_recordfiled5(recordfiled5)
        self.set_recordfiled4(recordfiled4)
        self.set_recordfiled9(recordfiled9)

    # setters for the fields of record
    def set_mainclass_c1(self, mainclass_c1):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "mainclass_c1"), mainclass_c1)

    def set_recordfiled5(self, recordfiled5):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled5"), recordfiled5)

    def set_recordfiled4(self, recordfiled4):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled4"), recordfiled4)

    def set_recordfiled9(self, recordfiled9):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled9"), recordfiled9)


    # getters for the fields of record
    def get_mainclass_c1(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "mainclass_c1"))

    def get_recordfiled5(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled5"))

    def get_recordfiled4(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled4"))

    def get_recordfiled9(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled9"))



class SubClass_C2_RecordHeaderR7(ParamRecord):
    # ProcessImpl is the class that is extended.
    # ProcessImpl contains the get/set methods for the current state variable and
    # the methods that generate the responses

    # method called by the configurator before the use of the scheduler
    # it creates the references of the processes needed
    def init_configuration(self, mainclass_c1, recordfiled8, recordfiled1):
        self.set_mainclass_c1(mainclass_c1)
        self.set_recordfiled8(recordfiled8)
        self.set_recordfiled1(recordfiled1)

    # setters for the fields of record
    def set_mainclass_c1(self, mainclass_c1):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "mainclass_c1"), mainclass_c1)

    def set_recordfiled8(self, recordfiled8):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled8"), recordfiled8)

    def set_recordfiled1(self, recordfiled1):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled1"), recordfiled1)


    # getters for the fields of record
    def get_mainclass_c1(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "mainclass_c1"))

    def get_recordfiled8(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled8"))

    def get_recordfiled1(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled1"))



